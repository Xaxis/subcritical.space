#!/usr/bin/env python3
"""E1: capability against training compute, and whether algorithmic progress depends on scale.

Three questions from the computational chapter (A1, A3) and the endpoint (D1, F3), answered from
public data only.

(a) Capability against compute. Epoch's data on AI models gives training compute; the Epoch
Capabilities Index (ECI) gives a stitched capability score. The two are joined by model name (the
models file first, then the model metadata shipped with the benchmark data, both Epoch's). ECI is
fitted on log10 training compute with a date term by least squares, as in the Rosetta paper. The
fit is then tested out of sample one order of magnitude (OOM) beyond its range: for each cut X in
23, 24, 25 and 26 (log10 FLOP), fit on models at or below X and forecast the models in (X, X + 1].
Errors are reported in ECI points, in compute-equivalent OOM, and per benchmark in percentage points
(each forecast ECI is turned into a score on each benchmark the model took, through Epoch's own
benchmark difficulty and slope), against Owen's 6 pp and 18 pp. The share of models above the
fit's one-sided 95% upper prediction bound is the share that would cross a threshold unforecast.
The date term gives a compute-equivalent rate of progress at fixed compute, and with the ledger's
frontier compute growth, the share of capability growth that compute explains. Neither is
identified: Epoch publishes no compute estimate for most frontier models (23 of the 25 with the
highest ECI), so the joined sample is mostly open weights, and the same fit on six samples (all,
not open weights, confident estimates, two compute floors, 2024 on) moves the rate by orders of
magnitude. All six are reported. An interaction of compute and date is fitted too; it says how the
rate at fixed compute changes with scale (C2's a(C)), and is reported at 1e24 and 1e26 FLOP.

(b) Algorithmic progress by scale. Ho et al.'s fit is rerun from their released code and data: the
preferred model (their model 7, L1 penalty 0.0025, SLSQP from zeros, top three results per paper),
reimplemented line by line from their notebook at a pinned commit, on their dataset as published
in the sheet their code reads. It reproduces their fitted parameters. The models are then split
into terciles of physical compute (6ND), and the same model is fitted with a separate year term per
bin and shared scaling exponents, so each bin gets its own rate of effective-compute growth.
Scale dependence (Gundlach et al.) predicts a rate that rises with compute; a flat rate refutes it.
Fully separate fits per bin, the literal reading of the spec, are recorded too; they are poorly
identified on narrow compute ranges and are not the headline.

(c) Clusters won and generality. No public data compare a model with an organisation at matched
time and budget, so D1's fraction of clusters won cannot be computed. What the data allow: (i) a search
of every table in Epoch's archive for columns that compare with people, which finds human time for
AI research and cyber, and a won-or-lost bar for three clusters, each a ledger baseline or one built
into the benchmark (science: GPQA Diamond against PhD experts; strategy: ForecastBench against the
superforecaster median; economic production: GDPval against industry experts, won when wins plus
half the ties exceed one half), counted for models whose compute is known; whether training
compute or effective compute (compute plus the date term from (a)) separates winners from losers;
and how often the verdict flips with the reasoning setting at the same training compute. (ii)
Generality as "clusters rise together": each model's ability within a cluster of benchmarks is
fitted on Epoch's benchmark curves and compared with its ability fitted on all its other
benchmarks; the deviation's slope on compute says whether a cluster pulls ahead or falls behind as
compute grows, and the spread of deviations across clusters says whether models become more or
less even. The cluster map is a design choice by benchmark name and is recorded in the result.

Serves C2 (scale-dependent efficiency, the scale term's survival), C10 (whether the fraction won
rises smoothly with effective compute) and C12 (whether compute is nearly necessary in practice).

Randomness: bootstraps resample models with numpy's default_rng(SEED). One check reruns Ho et al.'s
own bootstrap exactly as their notebook seeds it (the legacy generator at seed 0, 100 draws), to
compare with their published interval; it is deterministic too.

  heavy .venv/bin/python tools/exp/e01_capability_compute.py    (CPU, about three minutes)
"""

from __future__ import annotations

import csv
import io
import json
import math
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import minimize, minimize_scalar

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

MODELS_URL = "https://epoch.ai/data/all_ai_models.csv"
BENCH_URL = "https://epoch.ai/data/benchmark_data.zip"
HO_COMMIT = "29c7d852b6cd19ae11bb6662e9c1e61c03b1e4a7"
HO_CODE_URL = f"https://raw.githubusercontent.com/epoch-research/lm-algorithmic-progress/{HO_COMMIT}/section3.ipynb"
# The sheet and tab that section3.ipynb reads (its last assignment of `path`), exported as CSV.
HO_DATA_URL = (
    "https://docs.google.com/spreadsheets/d/11m8O_mU0cUkOB_5wluPne4PNsuvsKNbbVAzbYNy-NXY/"
    "export?gid=2087221150&format=csv"
)

SEED = 20261127
ECI_DRAWS = 2000
HO_DRAWS = 1000
HO_ORIG_DRAWS = 100  # as in their notebook
HO_DELTA = 0.0025  # their L1 penalty for the preferred model; checked against the notebook below
L_REF = 25.0  # log10 FLOP at which intercepts are stated
T0 = date(2024, 1, 1)  # time origin for the date term, in years
CUTS = [23.0, 24.0, 25.0, 26.0]  # out-of-sample schedule: fit at or below X, forecast (X, X + 1]
CUTS_OFFSET = [23.5, 24.5, 25.5]  # the same schedule shifted by half an OOM, as a check
MIN_FIT = 8  # fewest models a fit may rest on
MIN_CLUSTER = 10  # fewest compute-known models for a cluster's slope
SPLIT_DATE = date(2025, 7, 1)  # time-split check: fit before, forecast after
T95 = 0.95

# Benchmarks in the ECI mapped to clusters by name and, where known, by their published scope.
# The six decisive clusters of D1 are AI research, cyber, weapons-relevant science, strategy,
# persuasion and economic production; no benchmark here measures persuasion. Benchmarks not listed
# stay in the ECI and in each model's "rest" ability, but in no cluster.
CLUSTERS = {
    "software and AI research": [
        "METR Time Horizons", "WeirdML", "WeirdML v3", "PostTrainBench", "GSO-Bench",
        "Aider polyglot", "Terminal Bench", "FrontierCode", "FrontierSWE",
    ],
    "cyber": ["Cybench", "ExploitBench"],
    "science": ["GPQA diamond"],
    "mathematics": [
        "MATH level 5", "OTIS Mock AIME 2024-2025", "FrontierMath-2025-02-28-Private",
        "FrontierMath-Tier-4-2025-07-01-Private", "FrontierMath-Tiers-1-3-v2-Private",
        "FrontierMath-Tier-4-v2-Private", "ProofBench", "GSM8K",
    ],
    "strategy and games": ["Chess Puzzles", "Balrog", "SpireClimb", "ForecastBench"],
    "economic production": [
        "GDPval", "Remote Labor Index", "APEX-Agents", "The Agent Company", "OSWorld",
        "OSWorld 2.0", "DeepResearch Bench",
    ],
    "abstract reasoning": ["ARC-AGI", "ARC-AGI-2", "SimpleBench", "BBH", "ANLI"],
    "knowledge and language": [
        "MMLU", "TriviaQA", "SimpleQA Verified", "LAMBADA", "PIQA", "HellaSwag", "Winogrande",
        "OpenBookQA", "ARC AI2", "Fiction.LiveBench", "GeoBench",
    ],
}
# Column names that mark a comparison with people (a human score, bar, time or head-to-head).
HUMAN_COLUMNS = r"human|superforecaster|expert|professional|first.?solve|time horizon|minutes|win rate|win \+ tie|better than"
# Tables whose benchmark the metadata file does not name.
FILE_BENCH = {"forecastbench_external.csv": "ForecastBench"}
GDPVAL_PARITY = 0.5  # design choice: won when win rate plus half the tie rate exceeds one half

LEDGER_IDS = [
    "comp-frontier-compute-growth",
    "comp-ho-halving",
    "comp-ho-halving-lo",
    "comp-ho-halving-hi",
    "comp-bbh-mae-1oom",
    "comp-task-mae-1oom",
    "cog-gpqa-diamond-expert",
    "cog-forecast-super-index",
]


# ---------------------------------------------------------------------------------------------
# Small tools


def years(d: date) -> float:
    return (d.toordinal() - T0.toordinal()) / 365.25


def ols(X: np.ndarray, y: np.ndarray):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    dof = len(y) - X.shape[1]
    s2 = float(res @ res / dof)
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, cov, s2, dof


def design(L: np.ndarray, t: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones_like(L), L - L_REF, t])


def pct(a, p: float) -> float:
    return float(np.percentile(np.asarray(a, float), p))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def best_threshold_accuracy(score: np.ndarray, won: np.ndarray) -> float:
    """Share of cases a single threshold on `score` classifies correctly (won above it)."""
    order = np.argsort(score, kind="stable")
    s, w = score[order], won[order].astype(int)
    n = len(s)
    best = max(w.sum(), n - w.sum()) / n  # everything one side
    losers_below = np.cumsum(1 - w)
    winners_above = w.sum() - np.cumsum(w)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            continue
        best = max(best, (losers_below[i] + winners_above[i]) / n)
    return float(best)


def r4(x: float) -> float:
    return float(round(x, 4))


# ---------------------------------------------------------------------------------------------
# Data


def read_csv_text(text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(text)))


def load_bench(path: Path) -> dict:
    """Read the members of Epoch's benchmark ZIP in memory (nothing is extracted)."""
    out = {}
    with zipfile.ZipFile(path) as z:
        for name in [
            "epoch_capabilities_index/eci_scores.csv",
            "epoch_capabilities_index/edi_scores.csv",
            "epoch_capabilities_index/processed_data_for_eci.csv",
            "benchmark_metadata.csv",
            "model_metadata.csv",
            "gpqa_diamond.csv",
            "forecastbench_external.csv",
            "gdpval_external.csv",
        ]:
            out[name.split("/")[-1]] = read_csv_text(z.read(name).decode("utf-8"))
        # Every table's header, for the search for human comparisons in part (c).
        out["_headers"] = {
            name: next(csv.reader(io.StringIO(z.read(name).decode("utf-8"))))
            for name in sorted(z.namelist()) if name.endswith(".csv")
        }
    return out


def join_eci(models: list[dict], bench: dict) -> list[dict]:
    by_name = {r["Model"]: r for r in models}
    group_compute: dict[str, list[float]] = {}
    for r in bench["model_metadata.csv"]:
        if r["training_compute_flop"]:
            group_compute.setdefault(r["model_group"], []).append(float(r["training_compute_flop"]))
    rows = []
    for r in bench["eci_scores.csv"]:
        name = r["Model"]
        m = by_name.get(name, {})
        if m.get("Training compute (FLOP)"):
            flop, via = float(m["Training compute (FLOP)"]), "models"
        elif name in group_compute:
            flop, via = min(group_compute[name]), "benchmark model metadata"
        else:
            continue
        d = date.fromisoformat(r["date"])
        rows.append(
            {
                "model": name,
                "date": d.isoformat(),
                "t": years(d),
                "log10_flop": math.log10(flop),
                "eci": float(r["eci"]),
                "eci_lo": float(r["eci_ci_low"]) if r["eci_ci_low"] else None,
                "eci_hi": float(r["eci_ci_high"]) if r["eci_ci_high"] else None,
                "confidence": m.get("Confidence", ""),
                "access": r["Accessibility group"],
                "compute_from": via,
            }
        )
    return rows


# ---------------------------------------------------------------------------------------------
# (a) Capability against compute


def part_a(res: Results, rows: list[dict], bench: dict, ledger: dict, gen) -> dict:
    L = np.array([r["log10_flop"] for r in rows])
    t = np.array([r["t"] for r in rows])
    y = np.array([r["eci"] for r in rows])
    n = len(rows)
    X = design(L, t)
    beta, cov, s2, dof = ols(X, y)
    a0, b, c = (float(v) for v in beta)
    r2 = 1 - s2 * dof / float(np.sum((y - y.mean()) ** 2))
    gfront = math.log10(ledger["comp-frontier-compute-growth"])  # OOM a year
    share = b * gfront / (b * gfront + c)
    beta_i, cov_i, *_ = ols(np.column_stack([X, (L - L_REF) * t]), y)

    # What the interaction implies. With ECI = a + b (L - 25) + c t + d (L - 25) t, the gain at
    # fixed compute, in compute-equivalent OOM a year, is (c + d (L - 25)) / (b + d t); it is
    # evaluated at the sample's median release date. Its change per OOM of compute is the drift
    # of the algorithmic rate with scale (A3 and C2's a(C)).
    t_mid = float(np.median(t))

    def implied(bi):
        den = bi[1] + bi[3] * t_mid
        return {"r24": (bi[2] + bi[3] * (24 - L_REF)) / den, "r26": (bi[2] + bi[3] * (26 - L_REF)) / den,
                "drift": bi[3] / den}

    imp = implied(beta_i)

    boots = {"b": [], "c": [], "algo": [], "share": [], "inter": [], "r24": [], "r26": [], "drift": []}
    for _ in range(ECI_DRAWS):
        pick = gen.integers(0, n, n)
        Xb = X[pick]
        if np.linalg.matrix_rank(Xb) < 3:
            continue
        bb, *_ = ols(Xb, y[pick])
        bi, *_ = ols(np.column_stack([Xb, (L[pick] - L_REF) * t[pick]]), y[pick])
        boots["b"].append(bb[1])
        boots["c"].append(bb[2])
        boots["algo"].append(10 ** (bb[2] / bb[1]))
        boots["share"].append(bb[1] * gfront / (bb[1] * gfront + bb[2]))
        boots["inter"].append(bi[3])
        for k, v in implied(bi).items():
            boots[k].append(v)

    # The same fits on other samples. Epoch publishes no compute estimate for most frontier
    # models, so the joined sample is mostly open weights; these subsets show how far the rate
    # and the compute share move with the choice of models.
    subsets = {
        "all joined models": np.ones(n, bool),
        "not open weights": np.array([r["access"] != "Open weights" for r in rows]),
        "confident compute estimates only": np.array([r["confidence"] == "Confident" for r in rows]),
        "at or above 1e24 FLOP": L >= 24,
        "at or above 1e24.5 FLOP": L >= 24.5,
        "released 2024 on": t >= 0,
    }
    sub_table = {}
    for label, m in subsets.items():
        Ls, ts, ys = L[m], t[m], y[m]
        Xs = design(Ls, ts)
        bs_, *_ = ols(Xs, ys)
        bis, *_ = ols(np.column_stack([Xs, (Ls - L_REF) * ts]), ys)
        draws = {"algo": [], "share": [], "inter": []}
        for _ in range(ECI_DRAWS):
            pick = gen.integers(0, int(m.sum()), int(m.sum()))
            if np.linalg.matrix_rank(Xs[pick]) < 3:
                continue
            bb, *_ = ols(Xs[pick], ys[pick])
            bi, *_ = ols(np.column_stack([Xs[pick], (Ls[pick] - L_REF) * ts[pick]]), ys[pick])
            draws["algo"].append(10 ** (bb[2] / bb[1]))
            draws["share"].append(bb[1] * gfront / (bb[1] * gfront + bb[2]))
            draws["inter"].append(bi[3])
        sub_table[label] = {
            "models": int(m.sum()),
            "eci_per_oom": r4(bs_[1]), "eci_per_year": r4(bs_[2]),
            "algo_annual": r4(10 ** (bs_[2] / bs_[1])),
            "algo_annual_p2_5": r4(pct(draws["algo"], 2.5)), "algo_annual_p97_5": r4(pct(draws["algo"], 97.5)),
            "compute_share": r4(bs_[1] * gfront / (bs_[1] * gfront + bs_[2])),
            "compute_share_p2_5": r4(pct(draws["share"], 2.5)), "compute_share_p97_5": r4(pct(draws["share"], 97.5)),
            "interaction": r4(bis[3]),
            "interaction_p2_5": r4(pct(draws["inter"], 2.5)), "interaction_p97_5": r4(pct(draws["inter"], 97.5)),
        }
    ranked = sorted(bench["eci_scores.csv"], key=lambda r: -float(r["eci"]))[:25]
    joined = {r["model"] for r in rows}
    top_dropped = sum(1 for r in ranked if r["Model"] not in joined)
    open_share = float(np.mean([r["access"] == "Open weights" for r in rows]))

    # Benchmark curves, to turn an ECI into a score on each benchmark (Epoch's IRT form; the
    # processed scores are normalised between the random baseline and the ceiling).
    curve = {
        r["benchmark_name"]: (float(r["edi"]), float(r["estimated_slope_scaled"]))
        for r in bench["edi_scores.csv"]
    }
    meta = {r["benchmark"]: r for r in bench["benchmark_metadata.csv"]}
    span = {k: float(m["score_ceiling"]) - float(m["random_baseline"]) for k, m in meta.items()}
    scores: dict[str, list[tuple[str, float]]] = {}
    for r in bench["processed_data_for_eci.csv"]:
        scores.setdefault(r["Model"], []).append((r["benchmark"], float(r["performance"])))

    # The IRT form itself, checked on every score in the index with the model's own ECI.
    eci_all = {r["Model"]: float(r["eci"]) for r in bench["eci_scores.csv"]}
    form_err = []
    for mname, lst in scores.items():
        for bname, p in lst:
            dd, ss = curve[bname]
            form_err.append(abs(float(sigmoid(ss * (eci_all[mname] - dd))) - p) * span[bname] * 100)

    def run_schedule(cuts):
        preds, per_cut = [], []
        for X0 in cuts:
            tr = L <= X0
            te = (L > X0) & (L <= X0 + 1)
            if tr.sum() < MIN_FIT or te.sum() == 0:
                continue
            bt, ct, st, dft = ols(design(L[tr], t[tr]), y[tr])
            Xe = design(L[te], t[te])
            yhat = Xe @ bt
            se = np.sqrt(st + np.einsum("ij,jk,ik->i", Xe, ct, Xe))
            upper = yhat + stats.t.ppf(T95, dft) * se
            idx = np.where(te)[0]
            errs = y[te] - yhat
            per_cut.append(
                {
                    "cut_log10_flop": X0,
                    "fit_models": int(tr.sum()),
                    "test_models": int(te.sum()),
                    "fit_eci_per_oom": r4(bt[1]),
                    "fit_eci_per_year": r4(bt[2]),
                    "mae_eci": r4(np.mean(np.abs(errs))),
                    "bias_eci": r4(np.mean(errs)),
                    "above_upper_95": int(np.sum(y[te] > upper)),
                }
            )
            for k, i in enumerate(idx):
                preds.append(
                    {
                        "model": rows[i]["model"],
                        "cut": X0,
                        "log10_flop": r4(L[i]),
                        "eci": r4(y[i]),
                        "forecast": r4(yhat[k]),
                        "upper_95": r4(upper[k]),
                    }
                )
        return preds, per_cut

    preds, per_cut = run_schedule(CUTS)
    preds_off, per_cut_off = run_schedule(CUTS_OFFSET)
    err = np.array([p["eci"] - p["forecast"] for p in preds])
    above = np.array([p["eci"] > p["upper_95"] for p in preds])

    # Per benchmark, in percentage points of the raw score.
    bench_err, bench_floor, agg_err = [], [], []
    per_bench: dict[str, list[float]] = {}
    for p in preds:
        signed = []
        for bname, perf in scores.get(p["model"], []):
            dd, ss = curve[bname]
            f = float(sigmoid(ss * (p["forecast"] - dd)))
            fl = float(sigmoid(ss * (p["eci"] - dd)))
            e_pp = (f - perf) * span[bname] * 100
            bench_err.append(abs(e_pp))
            bench_floor.append(abs(fl - perf) * span[bname] * 100)
            per_bench.setdefault(bname, []).append(abs(e_pp))
            signed.append(e_pp)
        if signed:
            agg_err.append(abs(float(np.mean(signed))))

    # Checks: offset schedule, confident compute estimates only, and a split in time.
    conf = np.array([r["confidence"] == "Confident" for r in rows])
    Lc, tc, yc = L[conf], t[conf], y[conf]
    conf_err = []
    for X0 in CUTS:
        tr = Lc <= X0
        te = (Lc > X0) & (Lc <= X0 + 1)
        if tr.sum() < MIN_FIT or te.sum() == 0:
            continue
        bt, *_ = ols(design(Lc[tr], tc[tr]), yc[tr])
        conf_err.extend((yc[te] - design(Lc[te], tc[te]) @ bt).tolist())
    split_t = years(SPLIT_DATE)
    tr, te = t < split_t, t >= split_t
    bt, *_ = ols(design(L[tr], t[tr]), y[tr])
    split_err = y[te] - design(L[te], t[te]) @ bt

    algo = 10 ** (c / b)
    res.number("e1-models", n, unit="models", fmt=",.0f",
               label="models with both an Epoch Capabilities Index score and a training-compute estimate")
    res.number("e1-eci-per-oom", b, unit="ECI points", fmt=".1f",
               label="ECI points gained per order of magnitude of training compute, date held fixed")
    res.number("e1-eci-per-oom-lo", pct(boots["b"], 2.5), unit="ECI points", fmt=".1f",
               label="ECI points per OOM of compute, 2.5th percentile of resampling models")
    res.number("e1-eci-per-oom-hi", pct(boots["b"], 97.5), unit="ECI points", fmt=".1f",
               label="ECI points per OOM of compute, 97.5th percentile of resampling models")
    res.number("e1-eci-per-year", c, unit="ECI points", fmt=".1f",
               label="ECI points gained per year at fixed training compute")
    res.number("e1-algo-annual", algo, fmt=".0f",
               label="compute-equivalent gain a year at fixed compute implied by the ECI fit on all joined models (multiplier)",
               note="not identified: the joined sample is mostly open weights and lacks most frontier models, and the "
                    "rate moves from e1-algo-annual-subset-min to e1-algo-annual-subset-max across samples; it also "
                    "includes post-training, distillation and inference settings, not only pretraining algorithms")
    res.number("e1-algo-annual-lo", pct(boots["algo"], 2.5), fmt=".0f",
               label="compute-equivalent gain a year from the ECI fit, 2.5th percentile of resampling models")
    res.number("e1-algo-annual-hi", pct(boots["algo"], 97.5), fmt=".0f",
               label="compute-equivalent gain a year from the ECI fit, 97.5th percentile of resampling models")
    res.number("e1-compute-share", share, fmt=".0%",
               label="share of ECI growth explained by training compute on all joined models, at the ledger's frontier compute growth",
               note="not identified: it moves from e1-compute-share-subset-min to e1-compute-share-subset-max across samples, "
                    "and the joined sample lacks most frontier models")
    res.number("e1-compute-share-lo", pct(boots["share"], 2.5), fmt=".0%",
               label="share of frontier ECI growth from compute, 2.5th percentile of resampling models")
    res.number("e1-compute-share-hi", pct(boots["share"], 97.5), fmt=".0%",
               label="share of frontier ECI growth from compute, 97.5th percentile of resampling models")
    res.number("e1-eci-slope-change", float(beta_i[3]), unit="ECI points", fmt=".1f",
               label="interaction of compute and date: change a year in ECI points per OOM, equally the change per OOM in ECI points gained a year",
               note="negative: capability at fixed compute rose faster for smaller models; its sign is not stable across "
                    "samples (see eci_subsets)")
    res.number("e1-algo-annual-1e24", 10 ** imp["r24"], fmt=".0f",
               label="compute-equivalent gain a year at fixed compute, at 1e24 FLOP, from the interaction fit at the sample's median date (multiplier)")
    res.number("e1-algo-annual-1e24-lo", 10 ** pct(boots["r24"], 2.5), fmt=".0f",
               label="gain a year at 1e24 FLOP, 2.5th percentile of resampling models")
    res.number("e1-algo-annual-1e24-hi", 10 ** pct(boots["r24"], 97.5), fmt=".0f",
               label="gain a year at 1e24 FLOP, 97.5th percentile of resampling models")
    res.number("e1-algo-annual-1e26", 10 ** imp["r26"], fmt=".1f",
               label="compute-equivalent gain a year at fixed compute, at 1e26 FLOP, from the interaction fit at the sample's median date (multiplier)")
    res.number("e1-algo-annual-1e26-lo", 10 ** pct(boots["r26"], 2.5), fmt=".1f",
               label="gain a year at 1e26 FLOP, 2.5th percentile of resampling models")
    res.number("e1-algo-annual-1e26-hi", 10 ** pct(boots["r26"], 97.5), fmt=".1f",
               label="gain a year at 1e26 FLOP, 97.5th percentile of resampling models")
    res.number("e1-drift-per-oom", imp["drift"], unit="OOM a year per OOM", fmt=".2f",
               label="change in the compute-equivalent gain a year per OOM of compute (negative: drift falls with scale, against A3)",
               note="from the interaction fit at the sample's median date; with this value, log10 C + a(C) t falls with "
                    "log10 C once t exceeds -1 / e1-drift-per-oom years")
    res.number("e1-drift-per-oom-lo", pct(boots["drift"], 2.5), unit="OOM a year per OOM", fmt=".2f",
               label="drift with scale, 2.5th percentile of resampling models")
    res.number("e1-drift-per-oom-hi", pct(boots["drift"], 97.5), unit="OOM a year per OOM", fmt=".2f",
               label="drift with scale, 97.5th percentile of resampling models")
    sub_algo = [v["algo_annual"] for v in sub_table.values()]
    sub_share = [v["compute_share"] for v in sub_table.values()]
    res.number("e1-eci-models", len(bench["eci_scores.csv"]), unit="models", fmt=",.0f",
               label="models with an Epoch Capabilities Index score")
    res.number("e1-top25-dropped", top_dropped, unit="models", fmt=",.0f",
               label="of the 25 models with the highest ECI, those without a public training-compute estimate (left out of every fit)")
    res.number("e1-open-share", open_share, fmt=".0%",
               label="share of the joined models with open weights")
    res.number("e1-algo-annual-subset-min", min(sub_algo), fmt=".1f",
               label=f"lowest compute-equivalent gain a year across six samples of the joined models ({min(sub_table, key=lambda k: sub_table[k]['algo_annual'])})")
    res.number("e1-algo-annual-subset-max", max(sub_algo), fmt=",.0f",
               label=f"highest compute-equivalent gain a year across six samples of the joined models ({max(sub_table, key=lambda k: sub_table[k]['algo_annual'])})")
    res.number("e1-compute-share-subset-min", min(sub_share), fmt=".0%",
               label=f"lowest compute share of ECI growth across the six samples ({min(sub_table, key=lambda k: sub_table[k]['compute_share'])})")
    res.number("e1-compute-share-subset-max", max(sub_share), fmt=".0%",
               label=f"highest compute share of ECI growth across the six samples ({max(sub_table, key=lambda k: sub_table[k]['compute_share'])})")
    res.number("e1-eci-slope-change-lo", pct(boots["inter"], 2.5), unit="ECI points", fmt=".1f",
               label="change a year in ECI points per OOM, 2.5th percentile of resampling models")
    res.number("e1-eci-slope-change-hi", pct(boots["inter"], 97.5), unit="ECI points", fmt=".1f",
               label="change a year in ECI points per OOM, 97.5th percentile of resampling models")
    res.number("e1-oos-n", len(preds), unit="forecasts", fmt=",.0f",
               label="out-of-sample forecasts one OOM beyond the fitting range (cuts at 1e23 to 1e26 FLOP)")
    res.number("e1-oos-mae", float(np.mean(np.abs(err))), unit="ECI points", fmt=".1f",
               label="mean absolute error of ECI forecast one OOM of compute beyond the fitting range")
    res.number("e1-oos-mae-oom", float(np.mean(np.abs(err))) / b, unit="OOM", fmt=".2f",
               label="the same error as compute-equivalent orders of magnitude (divided by the full fit's slope)")
    res.number("e1-oos-bias", float(np.mean(err)), unit="ECI points", fmt=".1f",
               label="mean signed error of the one-OOM forecasts (actual minus forecast; negative means overforecast)")
    res.number("e1-oos-unforecast-share", float(np.mean(above)), fmt=".1%",
               label="share of one-OOM forecasts the actual ECI exceeds the one-sided 95% upper prediction bound (5% if calibrated)")
    top = next(c for c in per_cut if c["cut_log10_flop"] == 25.0)
    res.number("e1-oos-n-1e25", top["test_models"], unit="models", fmt=",.0f",
               label="models between 1e25 and 1e26 FLOP forecast from a fit on models at or below 1e25 FLOP")
    res.number("e1-oos-mae-1e25", top["mae_eci"], unit="ECI points", fmt=".1f",
               label="mean absolute error of the ECI forecast from 1e25 FLOP to the decade above it")
    res.number("e1-oos-bias-1e25", top["bias_eci"], unit="ECI points", fmt=".1f",
               label="mean signed error of the forecast from 1e25 FLOP (actual minus forecast; negative means overforecast)")
    res.number("e1-oos-bench-mae-pp", float(np.mean(bench_err)), unit="pp", fmt=".1f",
               label="mean absolute error per benchmark score, from the one-OOM ECI forecast")
    res.number("e1-oos-bench-floor-pp", float(np.mean(bench_floor)), unit="pp", fmt=".1f",
               label="mean absolute error per benchmark score with the model's actual ECI (the index's own floor)")
    res.number("e1-oos-agg-mae-pp", float(np.mean(agg_err)), unit="pp", fmt=".1f",
               label="mean absolute error of a model's average benchmark score, from the one-OOM ECI forecast")

    res.detail("eci_fit", {
        "form": "ECI = a + b (log10 FLOP - 25) + c (years since 2024-01-01), least squares",
        "a": r4(a0), "b": r4(b), "c": r4(c),
        "se": [r4(v) for v in np.sqrt(np.diag(cov))],
        "rmse": r4(math.sqrt(s2)), "r2": r4(r2), "n": n,
        "interaction": {"coef": [r4(v) for v in beta_i], "se": [r4(v) for v in np.sqrt(np.diag(cov_i))]},
        "frontier_compute_oom_per_year": r4(gfront),
        "corr_log_compute_date": r4(float(np.corrcoef(L, t)[0, 1])),
        "interaction_implied": {"median_date_years_since_2024": r4(t_mid), "oom_a_year_at_1e24": r4(imp["r24"]),
                                "oom_a_year_at_1e26": r4(imp["r26"]), "drift_per_oom": r4(imp["drift"]),
                                "years_after_which_more_compute_is_later": r4(-1 / imp["drift"]) if imp["drift"] < 0 else None},
        "draws": ECI_DRAWS, "kept": len(boots["b"]),
    })
    res.detail("eci_subsets", {"note": "the rate is not identified: it moves across samples by far more than any "
                                       "one sample's resampling interval", "table": sub_table})
    res.detail("eci_out_of_sample", {
        "schedule": per_cut, "forecasts": preds,
        "offset_schedule": per_cut_off,
        "offset_mae_eci": r4(np.mean([abs(p["eci"] - p["forecast"]) for p in preds_off])),
        "offset_unforecast_share": r4(np.mean([p["eci"] > p["upper_95"] for p in preds_off])),
        "confident_compute_only": {"forecasts": len(conf_err), "mae_eci": r4(np.mean(np.abs(conf_err)))},
        "time_split": {"split": SPLIT_DATE.isoformat(), "fit_models": int(tr.sum()), "test_models": int(te.sum()),
                       "mae_eci": r4(np.mean(np.abs(split_err))), "bias_eci": r4(np.mean(split_err))},
        "per_benchmark_mae_pp": {k: {"n": len(v), "mae_pp": r4(np.mean(v))} for k, v in sorted(per_bench.items())},
        "benchmark_scores_scored": len(bench_err),
        "irt_form_check_mae_pp_all_scores": r4(np.mean(form_err)),
    })
    res.detail("joined_models", [
        {k: (r4(v) if isinstance(v, float) else v) for k, v in r.items() if k != "t"} for r in rows
    ])
    return {"b": b, "c": c}


# ---------------------------------------------------------------------------------------------
# (b) Ho et al.'s algorithmic progress, rerun, then by compute bin


def num(s: str) -> float:
    try:
        return float(s)
    except (TypeError, ValueError):
        return math.nan


def frac_year(s: str) -> float:
    """Their conversion: year + (day of year - 1) / 365, from a YYYY/MM/DD date."""
    try:
        y, m, d = (int(v) for v in s.split("/"))
        dt = date(y, m, d)
    except (ValueError, TypeError):
        return math.nan
    return y + (dt.timetuple().tm_yday - 1) / 365.0


def ho_data(text: str) -> dict:
    """section3.ipynb, cells 8 to 13, reproduced: filters, stacking by benchmark, the combined
    perplexity column (their code keeps it for every stacked row), and the top three per paper."""
    recs = []
    for r in read_csv_text(text):
        p, d = num(r["Parameters"]), num(r["Dataset Size"])
        if not (p > 0 and d > 0):
            continue
        if num(r["Include?"]) == 0 or num(r["Outlier?"]) == 1:
            continue
        ppl = {k: num(r[f"Perplexity ({k.upper()})"]) for k in ("wt103", "wt2", "ptb")}
        if all(math.isnan(v) for v in ppl.values()):
            continue
        combined = next(ppl[k] for k in ("wt103", "wt2", "ptb") if not math.isnan(ppl[k]))
        recs.append({"system": r["System"], "ref": r["Reference"], "year": frac_year(r["Publication date"]),
                     "param": p, "dataset": d, "ppl": ppl, "combined": combined,
                     "uncertain": num(r["uncertain"])})
    stacked = [dict(x, bench=b) for b in ("wt103", "wt2", "ptb") for x in recs if not math.isnan(x["ppl"][b])]
    n_stacked = len(stacked)
    keep = []
    drop = {"GPT3-6.7B + muP", "LLaMA-65B (LoRA finetuned)", "LLaMA-13B (LoRA finetuned)", "LLaMA-7B (LoRA finetuned)"}
    for x in stacked:
        if x["uncertain"] != 0 or x["system"] in drop:
            continue
        if any(math.isnan(v) or math.isinf(v) for v in (math.log(x["param"]), math.log(x["dataset"]), x["year"], x["combined"])):
            continue
        if x["system"] == "Gopher (280B)":
            x["param"] = 280e9
        if x["system"] == "Gopher (7.1B)":
            x["param"] = 7.1e9
        keep.append(x)
    n_df1 = len(keep)
    keep.sort(key=lambda x: (x["ref"], x["combined"]))
    count: dict[str, int] = {}
    head = []
    for x in keep:
        count[x["ref"]] = count.get(x["ref"], 0) + 1
        if count[x["ref"]] <= 3:
            head.append(x)
    return {
        "year": np.array([x["year"] for x in head]),
        "N": np.array([x["param"] for x in head]),
        "D": np.array([x["dataset"] for x in head]),
        "lp": np.log([x["combined"] for x in head]),
        "ptb": np.array([x["bench"] == "ptb" for x in head], float),
        "wt2": np.array([x["bench"] == "wt2" for x in head], float),
        "dropped_head": n_stacked - len(head),
        "dropped_cluster": n_stacked - n_df1,
        "rows": len(head),
    }


def ho_fit(h: dict, idx: np.ndarray, bins: np.ndarray | None, K: int):
    """Their model 7, with K year terms per component when bins are given (K = 1 is theirs).
    Constants (minimum year, parameters, data) are taken on the full sample, as in their code."""
    y0, N0, D0 = h["year"].min(), h["N"].min(), h["D"].min()
    Y, n, d = h["year"][idx], h["N"][idx], h["D"][idx]
    pt, w2, lp = h["ptb"][idx], h["wt2"][idx], h["lp"][idx]
    onehot = np.ones((len(idx), 1)) if bins is None else np.eye(K)[bins[idx]]
    lnN, lnD = np.log(n) - np.log(N0), np.log(d) - np.log(D0)

    def unpack(p):
        # Their parameter order, with K year terms in place of one: ac, acp, acw, ay..., an,
        # bc, bcp, bcw, by..., bd. For K = 1 it is exactly theirs, so SLSQP takes their path.
        ac, acp, acw = p[:3]
        ay = p[3:3 + K]
        an, bc, bcp, bcw = p[3 + K:7 + K]
        by = p[7 + K:7 + 2 * K]
        bd = p[7 + 2 * K]
        return ac, acp, acw, an, bc, bcp, bcw, bd, ay, by

    def obj(p):
        ac, acp, acw, an, bc, bcp, bcw, bd, ay, by = unpack(p)
        a = ac + acp * pt + acw * w2 - (onehot @ ay) * (Y - y0) - an * lnN
        b = bc + bcp * pt + bcw * w2 - (onehot @ by) * (Y - y0) - bd * lnD
        r = lp - (np.exp(a) + np.exp(b))
        return np.mean(r * r) + HO_DELTA * np.sum(np.abs(p))

    with np.errstate(over="ignore", invalid="ignore"):
        out = minimize(obj, np.zeros(8 + 2 * K), method="SLSQP")
    ac, acp, acw, an, bc, bcp, bcw, bd, ay, by = unpack(out.x)
    rate = ay / an + by / bd  # natural log of effective compute gained per year, per bin
    return out, rate


def ho_fit_alone(h: dict, idx: np.ndarray) -> dict:
    """Model 7 fitted on a subset alone, with its own constants: the literal per-bin fit."""
    sub = {k: (v[idx] if isinstance(v, np.ndarray) else v) for k, v in h.items()}
    out, rate = ho_fit(sub, np.arange(len(idx)), None, 1)
    return {"annual_multiplier": r4(math.exp(float(rate[0]))), "alpha_param": r4(out.x[4]),
            "beta_data": r4(out.x[9]), "alpha_year": r4(out.x[3]), "beta_year": r4(out.x[8])}


def halving_months(rate: float) -> float:
    return 12 * math.log(2) / rate


def part_b(res: Results, h: dict, ledger: dict, gen) -> None:
    n = h["rows"]
    allidx = np.arange(n)
    out, rate = ho_fit(h, allidx, None, 1)
    names = ["alpha_const", "alpha_const_ptb", "alpha_const_wt2", "alpha_year", "alpha_param",
             "beta_const", "beta_const_ptb", "beta_const_wt2", "beta_year", "beta_data"]
    params = dict(zip(names, (r4(v) for v in out.x)))

    # Their own bootstrap, as their notebook seeds it, to compare with the published interval.
    legacy = np.random.RandomState(0)
    orig = []
    for _ in range(HO_ORIG_DRAWS):
        pick = legacy.choice(allidx, size=n, replace=True)
        orig.append(halving_months(float(ho_fit(h, pick, None, 1)[1][0])))
    # Ours: more draws, from the experiment's generator.
    ours = []
    for _ in range(HO_DRAWS):
        pick = gen.integers(0, n, n)
        ours.append(float(ho_fit(h, pick, None, 1)[1][0]))
    ours = np.array(ours)

    L = np.log10(6 * h["N"] * h["D"])
    binned = {}
    for label, q in (("terciles", [100 / 3, 200 / 3]), ("halves", [50.0])):
        edges = np.percentile(L, q)
        bins = np.digitize(L, edges)
        K = len(edges) + 1
        fit, rates = ho_fit(h, allidx, bins, K)
        draws = []
        for _ in range(HO_DRAWS):
            pick = gen.integers(0, n, n)
            draws.append(ho_fit(h, pick, bins, K)[1])
        draws = np.array(draws)
        oom = draws / math.log(10)
        diff = oom[:, -1] - oom[:, 0]
        alone = [ho_fit_alone(h, np.where(bins == k)[0]) for k in range(K)]
        binned[label] = {
            "edges_log10_flop": [r4(e) for e in edges],
            "models_per_bin": np.bincount(bins, minlength=K).tolist(),
            "bin_log10_flop_range": [[r4(L[bins == k].min()), r4(L[bins == k].max())] for k in range(K)],
            "annual_multiplier": [r4(math.exp(v)) for v in rates],
            "annual_multiplier_p2_5": [r4(math.exp(pct(draws[:, k], 2.5))) for k in range(K)],
            "annual_multiplier_p50": [r4(math.exp(pct(draws[:, k], 50))) for k in range(K)],
            "annual_multiplier_p97_5": [r4(math.exp(pct(draws[:, k], 97.5))) for k in range(K)],
            "halving_months": [r4(halving_months(v)) if v > 0 else None for v in rates],
            "top_minus_bottom_oom_per_year": r4(float(rates[-1] - rates[0]) / math.log(10)),
            "top_minus_bottom_p2_5": r4(pct(diff, 2.5)),
            "top_minus_bottom_p97_5": r4(pct(diff, 97.5)),
            "share_draws_top_faster": r4(float(np.mean(diff > 0))),
            "objective": r4(float(fit.fun)),
            "separate_fits": alone,
            "separate_fits_note": "model 7 fitted on each bin alone; the scaling exponents are poorly identified on a narrow compute range",
        }
        if label == "terciles":
            terc = (rates, draws, diff)

    rates, draws, diff = terc
    point = halving_months(float(rate[0]))
    res.number("e1-ho-rows", n, unit="results", fmt=",.0f",
               label="results in Ho et al.'s preferred sample, rebuilt from their sheet with their code's filters")
    res.number("e1-ho-halving-fit", point, unit="months", fmt=".1f",
               label="halving time of compute for fixed perplexity, our rerun of Ho et al.'s model 7, point fit")
    res.number("e1-ho-halving", halving_months(float(np.median(ours))), unit="months", fmt=".1f",
               label="halving time of compute for fixed perplexity, median of our resampling (their headline is a median)")
    res.number("e1-ho-halving-lo", halving_months(pct(ours, 97.5)), unit="months", fmt=".1f",
               label="halving time, 2.5th percentile of our resampling")
    res.number("e1-ho-halving-hi", halving_months(pct(ours, 2.5)), unit="months", fmt=".1f",
               label="halving time, 97.5th percentile of our resampling")
    res.number("e1-ho-orig-median", pct(orig, 50), unit="months", fmt=".2f",
               label="halving time, median of their own bootstrap rerun as their notebook seeds it")
    res.number("e1-ho-refit-over-published", pct(orig, 50) / ledger["comp-ho-halving"], fmt=".3f",
               label="their bootstrap rerun over their published halving time (1 means it reproduces)")
    res.number("e1-ho-annual-low", math.exp(rates[0]), fmt=".2f",
               label="yearly effective-compute gain in the lowest compute tercile of Ho et al.'s data (multiplier)")
    res.number("e1-ho-annual-low-lo", math.exp(pct(draws[:, 0], 2.5)), fmt=".2f",
               label="yearly gain, lowest compute tercile, 2.5th percentile of resampling")
    res.number("e1-ho-annual-low-hi", math.exp(pct(draws[:, 0], 97.5)), fmt=".2f",
               label="yearly gain, lowest compute tercile, 97.5th percentile of resampling")
    res.number("e1-ho-annual-mid", math.exp(rates[1]), fmt=".2f",
               label="yearly effective-compute gain in the middle compute tercile (multiplier)")
    res.number("e1-ho-annual-high", math.exp(rates[2]), fmt=".2f",
               label="yearly effective-compute gain in the highest compute tercile of Ho et al.'s data (multiplier)")
    res.number("e1-ho-annual-high-lo", math.exp(pct(draws[:, 2], 2.5)), fmt=".2f",
               label="yearly gain, highest compute tercile, 2.5th percentile of resampling")
    res.number("e1-ho-annual-high-hi", math.exp(pct(draws[:, 2], 97.5)), fmt=".2f",
               label="yearly gain, highest compute tercile, 97.5th percentile of resampling")
    res.number("e1-ho-top-faster-share", float(np.mean(diff > 0)), fmt=".0%",
               label="share of resamples in which the highest compute tercile progresses faster than the lowest")
    res.number("e1-ho-bin-edge-lo", 10 ** binned["terciles"]["edges_log10_flop"][0], unit="FLOP", fmt=".1e",
               label="training compute (6ND) at the edge between the lowest and middle terciles")
    res.number("e1-ho-bin-edge-hi", 10 ** binned["terciles"]["edges_log10_flop"][1], unit="FLOP", fmt=".1e",
               label="training compute (6ND) at the edge between the middle and highest terciles")
    res.detail("ho_rerun", {
        "code": f"section3.ipynb at commit {HO_COMMIT}, model 7, delta {HO_DELTA}, SLSQP from zeros",
        "rows_dropped_before_head": h["dropped_head"],
        "rows_dropped_before_cluster": h["dropped_cluster"],
        "objective": float(round(out.fun, 10)),
        "params": params,
        "published": {"halving_months": ledger["comp-ho-halving"], "lo": ledger["comp-ho-halving-lo"],
                      "hi": ledger["comp-ho-halving-hi"]},
        "their_bootstrap_rerun": {"draws": HO_ORIG_DRAWS, "p2_5": r4(pct(orig, 2.5)), "p50": r4(pct(orig, 50)),
                                  "p97_5": r4(pct(orig, 97.5))},
        "our_bootstrap": {"draws": HO_DRAWS, "share_negative_rate": r4(float(np.mean(ours <= 0)))},
        "compute_range_log10_flop": [r4(L.min()), r4(L.max())],
    })
    res.detail("ho_by_compute", binned)


# ---------------------------------------------------------------------------------------------
# (c) Clusters won and generality


def fit_ability(lst, curve) -> float:
    d = np.array([curve[b][0] for b, _ in lst])
    s = np.array([curve[b][1] for b, _ in lst])
    p = np.array([v for _, v in lst])
    r = minimize_scalar(lambda th: float(np.sum((p - sigmoid(s * (th - d))) ** 2)), bounds=(0.0, 250.0),
                        method="bounded", options={"xatol": 1e-6})
    return float(r.x)


def part_c(res: Results, rows: list[dict], bench: dict, ledger: dict, fit_a: dict, gen) -> None:
    curve = {r["benchmark_name"]: (float(r["edi"]), float(r["estimated_slope_scaled"])) for r in bench["edi_scores.csv"]}
    b2c = {b: k for k, bs in CLUSTERS.items() for b in bs}
    unmapped = sorted(b for b in curve if b not in b2c)
    known = {r["model"]: r for r in rows}
    scores: dict[str, list[tuple[str, float]]] = {}
    for r in bench["processed_data_for_eci.csv"]:
        if r["Model"] in known:
            scores.setdefault(r["Model"], []).append((r["benchmark"], float(r["performance"])))

    dev: dict[tuple[str, str], float] = {}
    for m in sorted(scores):
        lst = scores[m]
        for k in CLUSTERS:
            inside = [x for x in lst if b2c.get(x[0]) == k]
            outside = [x for x in lst if b2c.get(x[0]) != k]
            if inside and len(outside) >= 3:
                dev[(m, k)] = fit_ability(inside, curve) - fit_ability(outside, curve)

    slopes = {}
    for k in CLUSTERS:
        ms = [m for (m, kk) in dev if kk == k]
        entry = {"models": len(ms)}
        if len(ms) >= MIN_CLUSTER:
            L = np.array([known[m]["log10_flop"] for m in ms])
            t = np.array([known[m]["t"] for m in ms])
            v = np.array([dev[(m, k)] for m in ms])
            X = design(L, t)
            bk, *_ = ols(X, v)
            draws = []
            for _ in range(ECI_DRAWS):
                pick = gen.integers(0, len(ms), len(ms))
                if np.linalg.matrix_rank(X[pick]) < 3:
                    continue
                draws.append(ols(X[pick], v[pick])[0][1])
            entry.update({"deviation_per_oom": r4(bk[1]), "p2_5": r4(pct(draws, 2.5)), "p97_5": r4(pct(draws, 97.5)),
                          "deviation_per_year": r4(bk[2]), "mean_deviation": r4(float(v.mean()))})
        slopes[k] = entry
    fitted = {k: e for k, e in slopes.items() if "deviation_per_oom" in e}
    worst = max(fitted, key=lambda k: abs(fitted[k]["deviation_per_oom"]))
    excl = sum(1 for e in fitted.values() if e["p2_5"] > 0 or e["p97_5"] < 0)

    spread = []
    for m in sorted(known):
        vals = [dev[(m, k)] for k in CLUSTERS if (m, k) in dev]
        if len(vals) >= 3:
            spread.append((known[m]["log10_flop"], known[m]["t"], float(np.std(vals, ddof=1))))
    sp = np.array(spread)
    Xs = design(sp[:, 0], sp[:, 1])
    bs, *_ = ols(Xs, sp[:, 2])
    sdraws = []
    for _ in range(ECI_DRAWS):
        pick = gen.integers(0, len(sp), len(sp))
        if np.linalg.matrix_rank(Xs[pick]) < 3:
            continue
        sdraws.append(ols(Xs[pick], sp[pick, 2])[0][1])

    # Clusters with a human comparison. Model versions are grouped into models by Epoch's metadata.
    group = {r["model_version"]: r["model_group"] for r in bench["model_metadata.csv"] if r["model_version"]}

    def by_model(table: str, score) -> dict:
        out: dict[str, dict] = {}
        for r in bench[table]:
            if not r["Training compute (FLOP)"]:
                continue
            g = group.get(r["Model version"], r["Model version"])
            e = out.setdefault(g, {"log10_flop": math.log10(float(r["Training compute (FLOP)"])),
                                   "t": years(date.fromisoformat(r["Release date"])), "scores": []})
            e["scores"].append(score(r))
        return out

    gpqa = by_model("gpqa_diamond.csv", lambda r: float(r["Best score (across scorers)"]))
    fore = by_model("forecastbench_external.csv", lambda r: float(r["Overall score"]))
    gdp = by_model("gdpval_external.csv",
                   lambda r: (float(r["Win Rate (%)"]) + float(r["Win + tie rate (%)"])) / 2)
    bar_gpqa = ledger["cog-gpqa-diamond-expert"]
    bar_fore = ledger["cog-forecast-super-index"]
    won = {
        "science (GPQA Diamond against PhD experts)": {m: max(e["scores"]) > bar_gpqa for m, e in gpqa.items()},
        "strategy (ForecastBench against the superforecaster median)": {m: max(e["scores"]) > bar_fore for m, e in fore.items()},
        "economic production (GDPval against industry experts)": {m: max(e["scores"]) > GDPVAL_PARITY for m, e in gdp.items()},
    }
    flips = sorted(m for m, e in gpqa.items() if max(e["scores"]) > bar_gpqa >= min(e["scores"]) and len(e["scores"]) > 1)
    multi = sum(1 for e in gpqa.values() if len(e["scores"]) > 1)
    gm = sorted(gpqa)
    Lg = np.array([gpqa[m]["log10_flop"] for m in gm])
    tg = np.array([gpqa[m]["t"] for m in gm])
    wg = np.array([won["science (GPQA Diamond against PhD experts)"][m] for m in gm])
    oom_per_year = fit_a["c"] / fit_a["b"]
    Leff = Lg + oom_per_year * tg
    acc_phys = best_threshold_accuracy(Lg, wg)
    acc_eff = best_threshold_accuracy(Leff, wg)
    acc_date = best_threshold_accuracy(tg, wg)
    overlap = float(Lg[~wg].max() - Lg[wg].min()) if wg.any() and (~wg).any() else 0.0
    by_decade = {}
    for lo in range(21, 28):
        sel = (Lg >= lo) & (Lg < lo + 1)
        if sel.any():
            by_decade[f"1e{lo} to 1e{lo + 1}"] = {"models": int(sel.sum()), "won": int(wg[sel].sum())}
    clusters_with_winner = sum(1 for v in won.values() if any(v.values()))

    # Which decisive clusters have any human comparison: a search of every table's columns in
    # Epoch's archive, plus the GPQA expert bar, which the ledger holds from Epoch's GPQA page.
    file_bench = {m["source_file"]: m["benchmark"] for m in bench["benchmark_metadata.csv"] if m["source_file"]}
    file_bench.update(FILE_BENCH)
    found = []
    for name, header in bench["_headers"].items():
        cols = [h for h in header if re.search(HUMAN_COLUMNS, h, re.I)]
        if cols:
            bname = file_bench.get(name.split("/")[-1], "")
            found.append({"file": name, "columns": cols, "benchmark": bname, "cluster": b2c.get(bname, "")})
    human_clusters = sorted({f["cluster"] for f in found if f["cluster"]} | {"science"})

    res.number("e1-cluster-dev-max", fitted[worst]["deviation_per_oom"], unit="ECI points", fmt=".1f",
               label=f"largest drift per OOM of compute of one cluster's ability from the model's other benchmarks ({worst})")
    res.number("e1-cluster-dev-max-lo", fitted[worst]["p2_5"], unit="ECI points", fmt=".1f",
               label="that cluster's drift per OOM, 2.5th percentile of resampling models")
    res.number("e1-cluster-dev-max-hi", fitted[worst]["p97_5"], unit="ECI points", fmt=".1f",
               label="that cluster's drift per OOM, 97.5th percentile of resampling models")
    res.number("e1-clusters-fitted", len(fitted), unit="clusters", fmt=",.0f",
               label=f"clusters with at least {MIN_CLUSTER} compute-known models, so a drift on compute can be fitted")
    res.number("e1-clusters-drifting", excl, unit="clusters", fmt=",.0f",
               label="of those, clusters whose drift per OOM has a 95% interval that excludes zero")
    res.number("e1-spread-per-oom", float(bs[1]), unit="ECI points", fmt=".2f",
               label="change per OOM of compute in the spread of a model's cluster abilities (negative means more even)")
    res.number("e1-spread-per-oom-lo", pct(sdraws, 2.5), unit="ECI points", fmt=".2f",
               label="change per OOM in the spread of cluster abilities, 2.5th percentile of resampling models")
    res.number("e1-spread-per-oom-hi", pct(sdraws, 97.5), unit="ECI points", fmt=".2f",
               label="change per OOM in the spread of cluster abilities, 97.5th percentile of resampling models")
    res.number("e1-spread-mean", float(sp[:, 2].mean()), unit="ECI points", fmt=".1f",
               label="mean spread (standard deviation) of a model's cluster abilities around its other benchmarks")
    res.number("e1-clusters-baselined", len(human_clusters), unit="clusters", fmt=",.0f",
               label="clusters with any human comparison in the public data, by a search of the archive's columns plus "
                     "the ledger's GPQA expert bar (none is an organisation at matched budget)",
               note="persuasion has none; AI research and cyber have human time (METR horizons, Cybench first-solve "
                    "times), not a won-or-lost bar")
    res.number("e1-clusters-verdict", len(won), unit="clusters", fmt=",.0f",
               label="of those, clusters whose comparison gives a won-or-lost bar scored here (GPQA experts, the "
                     "superforecaster median, GDPval parity)")
    res.number("e1-clusters-with-winner", clusters_with_winner, unit="clusters", fmt=",.0f",
               label="of the scored clusters, those in which any compute-known model beats the human comparison")
    res.number("e1-gpqa-models", len(gm), unit="models", fmt=",.0f",
               label="compute-known models with a GPQA Diamond score in Epoch's data")
    res.number("e1-gpqa-won", int(wg.sum()), unit="models", fmt=",.0f",
               label="of those, models whose best setting beats PhD experts on GPQA Diamond")
    res.number("e1-gpqa-overlap-oom", overlap, unit="OOM", fmt=".1f",
               label="training compute of the largest losing model over the smallest winning one on GPQA Diamond, in OOM")
    res.number("e1-gpqa-acc-compute", acc_phys, fmt=".0%",
               label="share of GPQA verdicts against PhD experts the best single training-compute threshold gets right")
    res.number("e1-gpqa-acc-effective", acc_eff, fmt=".0%",
               label="share of GPQA verdicts the best single effective-compute threshold gets right (compute plus the ECI date term)")
    res.number("e1-gpqa-acc-date", acc_date, fmt=".0%",
               label="share of GPQA verdicts the best single release-date threshold gets right")
    res.number("e1-gpqa-flips", len(flips), unit="models", fmt=",.0f",
               label="models whose GPQA verdict against PhD experts flips with the reasoning setting at the same training compute")
    res.detail("ledger_inputs", {i: ledger[i] for i in LEDGER_IDS})
    res.detail("clusters", {
        "map": CLUSTERS, "unmapped_benchmarks": unmapped,
        "drift": slopes,
        "method": "ability in a cluster minus ability on the model's other benchmarks, each fitted to Epoch's benchmark "
                  "curves by least squares; drift is the slope of that difference on log10 compute with a date term",
        "spread": {"models": len(sp), "coef": [r4(v) for v in bs]},
    })
    res.detail("clusters_won", {
        "baselines": {"gpqa_phd_experts": bar_gpqa, "forecast_superforecaster_median": bar_fore,
                      "gdpval_parity_win_plus_half_tie": GDPVAL_PARITY},
        "per_cluster": {k: {"models": len(v), "won": int(sum(v.values()))} for k, v in won.items()},
        "human_comparison_search": {"pattern": HUMAN_COLUMNS, "tables": found, "clusters": human_clusters},
        "gpqa_by_compute_decade": by_decade,
        "gpqa_models_with_several_settings": multi,
        "gpqa_flip_models": flips,
        "effective_compute_oom_per_year": r4(oom_per_year),
        "not_measurable": ["AI research against an organisation", "cyber operations against an organisation",
                           "persuasion", "any cluster at matched time and budget"],
    })


# ---------------------------------------------------------------------------------------------


def main() -> int:
    res = Results("E1", "e01_capability_compute", seed=SEED)
    ledger_all = json.loads((ROOT / "data" / "numbers.json").read_text())
    ledger = {i: float(ledger_all[i]["value"]) for i in LEDGER_IDS}

    models_path = fetch(MODELS_URL, "epoch/all_ai_models.csv", res, what="Epoch AI, Data on AI models (all models)")
    bench_path = fetch(BENCH_URL, "epoch/benchmark_data.zip", res,
                       what="Epoch AI, benchmark data with the Epoch Capabilities Index")
    code_path = fetch(HO_CODE_URL, f"ho2024/section3-{HO_COMMIT[:7]}.ipynb", res,
                      what="Ho et al., section3.ipynb at a pinned commit (the code rerun here)")
    ho_path = fetch(HO_DATA_URL, "ho2024/lm_algorithmic_progress.csv", res,
                    what="Ho et al.'s dataset, the sheet tab their code reads, as CSV")

    code = "".join("".join(c["source"]) for c in json.loads(code_path.read_text())["cells"])
    for needle in ('model_name_str = "model_7"', f"delta = {HO_DELTA}", "groupby('Reference').head(3)",
                   "gid=2087221150", "l1_reg = delta * np.sum(np.abs(params))"):
        if needle not in code:
            raise SystemExit(f"their notebook no longer contains {needle!r}; the rerun would not be theirs")

    models = read_csv_text(models_path.read_text(encoding="utf-8"))
    bench = load_bench(bench_path)
    rows = join_eci(models, bench)
    if len(rows) < 30:
        raise SystemExit(f"only {len(rows)} models joined; the files changed shape")
    gen = np.random.default_rng(SEED)
    fit_a = part_a(res, rows, bench, ledger, gen)
    h = ho_data(ho_path.read_text(encoding="utf-8"))
    part_b(res, h, ledger, gen)
    part_c(res, rows, bench, ledger, fit_a, gen)
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
