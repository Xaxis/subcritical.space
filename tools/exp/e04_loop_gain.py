#!/usr/bin/env python3
"""E4, parts (c) and (a): can a staged loop-gain estimator decide which side of 1 the gain is on,
and what the NanoGPT speedrun's history says about returns to research at fixed hardware.

Serves C4 (a loop-gain estimator staged at fixed inputs, binding on its upper confidence bound) and
C2 (breakout time, whose algorithmic drift rises with research labour through C4's gain).

Part (c), simulation. The common growth law of research/013-dynamical.md, (1/X) dX/dt = theta *
X^(-beta) * E^lambda with r = lambda / beta, run as C4's staged experiment: rounds of equal budget at
one, two and four times a base agent budget, so each "round" is three staged rounds. Round k's gain
on a log compute-equivalent axis follows the first-order law Delta_k = Delta_1 * exp(-b u_k) *
(B / B0)^lambda * noise, u_k the stock delivered before round k, fitted in level form, ln Delta_k =
c + lambda ln B - b u_k, with a 90% interval for r from a recursive residual bootstrap (the fitted law
regenerates each run from resampled residuals and the estimator is refitted). Reported against the
number of rounds: coverage, the upper-bound trigger's false-alarm rate (true r below the margin K*,
upper bound above it), its late-firing rate, the lower-bound rule's miss rate, and how far the
trigger's firing rate at the corrected 95th percentile of r exceeds its rate at the median. The
trigger is on the loop gain K = e r (Part III, Corollary 4.5a), whose bound is the closure's bound
times r's, each at its own share of the error: the K rule is reported beside r's with the closure's
bound at 1 (a loop that may be fully closed) and r's share of the one-sided error halved (an even
split, a design choice), so it fires at least as often as the rule on r. lambda is
the Davidson and Houlden median, b = lambda / r. The noise per round is calibrated on the speedrun's
monthly gains (part a) and swept. The margin K* has no value in the research yet (K* = 1 - m *
K_dot * T_r needs an unmeasured drift rate), so a placeholder, G_STAR, is used and swept.
Robustness: data from Part III's exact round law (A4.1), fitted by the first-order form, by least
squares on the exact identity and by its maximum likelihood; and noise resampled from the
speedrun's own residuals. Sandbaggers choose when to hide (uniformly, in late rounds, at large
budgets, both, or the luck of good rounds), and each is measured by the share of its achievable gain
it withheld, the shortfall an elicitation step would have to catch. A bias table compares every
estimator, including C4's difference regression and the exact identity of Part III's Lemma 4.1, on
one and on two held-out sets, with the noise all real variation in gain, half measurement error, or
all measurement error.

Part (a), history. The speedrun's record list from three public sources: Epoch's series of the 92
records (dates, times, contributors), the repository's README record table (re-timings after the
rule change at record 21, and a cross-check of every time), and METR's classification of records 1
to 77 (category, depth, provenance, AI credit). The axis is ln of 8xH100 wall-clock to the fixed
target loss, which is physical compute at fixed hardware. Systems changes (METR's categories
Parallelization, Kernel Opt, Framework and Data Type) raise throughput without reducing FLOP and are
kept apart from algorithmic ones, so the algorithmic subset approximates an effective-compute axis.
The spec asked for FLOP per record from the logs; that was not built (see FLOP_NOTE). Per-record
gains are split by kind and by AI credit; METR's depth result and the survey's window paces are
recomputed; and the growth law is fitted to monthly gains by Poisson pseudo-maximum likelihood with
human contributors over the trailing 180 days as the research input and a moving-block bootstrap.

  .venv/bin/python tools/exp/e04_loop_gain.py                (part a alone runs in seconds)
  heavy .venv/bin/python tools/exp/e04_loop_gain.py          (the full run, CPU, a few minutes)
"""

from __future__ import annotations

import csv
import io
import json
import math
import re
import sys
import tomllib
from datetime import date, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127

EPOCH_URL = "https://epoch.ai/data/ai-impacts/series/nanogpt-speedrun-record-time.csv"
README_URL = "https://raw.githubusercontent.com/KellerJordan/modded-nanogpt/master/README.md"
METR_URL = "https://metr.org/assets/data/ai-rd-nanogpt-progress/classifications.csv"

FLOP_NOTE = (
    "FLOP per record was not computed from the run logs. Each log embeds the training code, whose "
    "model shape, batch schedule and sequence length change form across records (and several "
    "records link a folder or no log), so per-record FLOP would need a parser per era. The axis "
    "used is wall-clock on fixed 8xH100 hardware, physical compute to the target, with METR's "
    "systems categories split out as throughput gains."
)

# METR's categories that raise throughput (FLOP per second) rather than cut the FLOP to the target.
SYSTEMS = {"Parallelization", "Kernel Opt", "Framework", "Data Type"}
ALGORITHMIC = {"Embeddings", "Optimizer", "Architecture", "Attention", "HP Tuning", "Training Strategy"}
DEPTH = {"Low": "shallow", "Med": "moderate", "High": "deep", "Top": "breakthrough"}

# Part (a) fit design.
INPUT_WINDOW_DAYS = 180  # research input: distinct human contributors over this many days before a month
INPUT_WINDOWS_ALT = (90, 365)
BLOCK_MONTHS = 3
FIT_DRAWS = 4000

# Part (c) design. The grids are design choices, stated as such in the result.
G_STAR = 0.9  # placeholder margin below 1; the research sets none yet
G_STAR_SWEEP = (0.7, 0.8, 0.9, 1.0)
# The K rule (Part III, Corollary 4.5a): it fires when U_e * U_r > K*, the closure's bound U_e and r's
# bound U_r each at its own share of the upper bound's one-sided error. U_E = 1: a loop that may be
# fully closed. K_SPLIT: r's share when the closure's bound is measured too (even, a design choice).
U_E = 1.0
K_SPLIT = 0.5
BUDGETS = (1.0, 2.0, 4.0)  # agent budget per round, multiples of the base (C4's one, two and four)
N_GRID = (3, 5, 8, 12, 20, 50)  # rounds per budget; each is one staged round at each of the three budgets
R_EXTRA = (0.75, 1.0, 1.5)  # true r added to the ledger's three and to G_STAR
D1_GRID = (0.3, 1.0)  # first-round gains at the base budget (e-folds) swept beside the speedrun's
SIGMA_GRID = (0.25, 0.5)  # noise per round (sd of ln gain) swept beside the speedrun's
D1_FINE = (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0)  # for the gain a 5-round test needs
FAVOURABLE = (1.0, 0.25)  # a large, tightly measured round: first-round gain 1 e-fold, noise 0.25
MIDDLE = (0.3, 0.5)  # a middling round, where the red team found the two-set remedy nearly works
STRATEGIES = ("uniform", "late", "budget", "targeted", "luck")  # when a sandbagger hides
HIDE_GRID = (0.1, 0.25, 0.5)  # mean share of each round's achievable gain withheld
MEAS_MIX = (0.0, 0.5, 1.0)  # share of the noise variance that is error in measuring the gain
BIAS_SIMS = 2000  # runs per cell of the bias table (point estimates only)
GN_ITERS = 4  # Gauss-Newton steps for least squares on the exact identity in level form
ML_LO, ML_HI, ML_STEP, ML_GOLDEN = -1.0, 8.0, 0.5, 12  # likelihood search over b: grid, then golden section
FP_ITERS = 12  # fixed-point steps for the exact identity in difference form
SIMS = 400  # simulated staged experiments per cell
BOOT = 200  # bootstrap draws per simulated experiment
CHUNK = 50  # simulated experiments per vectorised chunk
STEP_CAP = 20.0  # a bootstrap path regenerated from an explosive fit is capped at exp(20) per round


# -------------------------------------------------------------------------------------------------
# The ledger


def ledger(ids: list[str]) -> dict[str, float]:
    """Values by id from data/numbers.json. An input the model has not yet written there is read
    from the inputs file the ledger loads it from, which holds the same value."""
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    inputs: dict[str, float] = {}
    for path in [ROOT / "data" / "inputs.toml", *sorted((ROOT / "data" / "inputs").glob("*.toml"))]:
        if path.exists():
            for key, spec in tomllib.loads(path.read_text()).items():
                inputs[key] = float(spec["value"])
    out = {}
    for i in ids:
        if i in numbers:
            out[i] = float(numbers[i]["value"])
        elif i in inputs:
            out[i] = inputs[i]
        else:
            raise SystemExit(f"ledger id {i} is in neither data/numbers.json nor the inputs")
    return out


# -------------------------------------------------------------------------------------------------
# Part (a): the speedrun


def read_epoch(path: Path) -> list[dict]:
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
    out = []
    for r in rows:
        out.append(
            {
                "record": int(r["record"]),
                "date": date.fromisoformat(r["date"]),
                "seconds": float(r["value"]),
                "description": r["description"],
                "contributors": r["contributors"],
            }
        )
    out.sort(key=lambda r: r["record"])
    if [r["record"] for r in out] != list(range(1, len(out) + 1)):
        raise SystemExit("Epoch's series does not number its records 1..n; it changed shape")
    return out


ROW = re.compile(r"^(\d+)\s*\|\s*([\d.]+) minutes\s*\|(.*?)\|\s*(\d\d)/(\d\d)/(\d\d)\s*\|(.*?)\|(.*)$")


def read_readme(path: Path) -> tuple[dict[int, float], list[dict]]:
    """The README's record table: each record's time, and the re-timings ("not a new record")."""
    times: dict[int, float] = {}
    retimes = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line.strip())
        if not m:
            continue
        num, minutes = int(m.group(1)), float(m.group(2))
        when = date(2000 + int(m.group(6)), int(m.group(4)), int(m.group(5)))
        if "not a new record" in m.group(8):
            retimes.append({"record": num, "seconds": minutes * 60, "date": when, "why": m.group(3).strip()})
        elif num not in times:
            times[num] = minutes * 60
    return times, retimes


def read_metr(path: Path) -> dict[int, dict]:
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
    return {
        int(r["number"]): {
            "minutes": float(r["time_minutes"]),
            "depth": DEPTH.get(r["apple"], "n/a"),
            "provenance": r["provenance"],
            "category": r["category"],
            "ai": r["ai_assisted"].strip() == "True",
        }
        for r in rows
    }


AI_TEXT = re.compile(r"\bAI system\b", re.IGNORECASE)
HANDLE = re.compile(r"@[A-Za-z0-9_.\-]+")


def humans(contributors: str) -> list[str]:
    """Human handles credited on a record (the AI systems' names carry no handle)."""
    return sorted({h.rstrip(".").lower() for h in HANDLE.findall(contributors)})


def ppml(y: np.ndarray, X: np.ndarray, iters: int = 100) -> np.ndarray | None:
    """Poisson pseudo-maximum likelihood, E[y] = exp(X b), by iteratively reweighted least squares.
    It keeps months with no gain, which a log regression would drop."""
    b = np.zeros(X.shape[1])
    b[0] = math.log(max(y.mean(), 1e-12))
    for _ in range(iters):
        eta = X @ b
        if eta.max() > 50:
            return None
        mu = np.exp(eta)
        if not np.all(mu > 0):  # a resample whose fit runs off to zero gain has no solution
            return None
        z = eta + (y - mu) / mu
        XtW = X.T * mu
        try:
            nb = np.linalg.solve(XtW @ X, XtW @ z)
        except np.linalg.LinAlgError:
            return None
        if not np.all(np.isfinite(nb)):
            return None
        if np.max(np.abs(nb - b)) < 1e-10:
            return nb
        b = nb
    return b


def month_start(d: date) -> date:
    return date(d.year, d.month, 1)


def add_month(d: date) -> date:
    return date(d.year + d.month // 12, d.month % 12 + 1, 1)


def monthly(records: list[dict], gain_key: str, window: int, upto: date) -> dict:
    """Gains per calendar month (the month a record was set), the stock before each month, and
    the research input: distinct human contributors on records in the `window` days before it."""
    # Months start at record 2's month: record 1 is the baseline and gains nothing.
    first = month_start(records[1]["date"])
    months, m = [], first
    while m <= upto:
        months.append(m)
        m = add_month(m)
    gains, stock, inputs = [], [], []
    for m in months:
        nxt = add_month(m)
        gains.append(sum(r[gain_key] for r in records if m <= r["date"] < nxt and r[gain_key] is not None))
        stock.append(sum(r[gain_key] for r in records if r["date"] < m and r[gain_key] is not None))
        lo = m - timedelta(days=window)
        people = set()
        for r in records:
            if lo <= r["date"] < m:
                people.update(r["humans"])
        inputs.append(len(people))
    return {
        "months": [m.isoformat()[:7] for m in months],
        "gain": np.array(gains),
        "stock": np.array(stock),
        "input": np.array(inputs, float),
    }


def fit_growth(series: dict, gen: np.random.Generator, draws: int) -> dict:
    """E[gain in month m] = exp(c - beta * stock_m + lambda * ln input_m), and r = lambda / beta,
    with a moving-block bootstrap of months for the interval."""
    y, u, e = series["gain"], series["stock"], series["input"]
    keep = e > 0
    y, u, e = y[keep], u[keep], e[keep]
    X = np.column_stack([np.ones_like(u), -u, np.log(e)])
    b = ppml(y, X)
    if b is None:
        raise SystemExit("the growth-law fit to the speedrun did not converge")
    mu = np.exp(X @ b)
    pos = y > 0
    sigma = float(np.std(np.log(y[pos] / mu[pos]), ddof=3))
    n = len(y)
    nblocks = math.ceil(n / BLOCK_MONTHS)
    betas, lams, rs = [], [], []
    failed = 0
    for _ in range(draws):
        starts = gen.integers(0, n - BLOCK_MONTHS + 1, nblocks)
        idx = np.concatenate([np.arange(s, s + BLOCK_MONTHS) for s in starts])[:n]
        bb = ppml(y[idx], X[idx])
        if bb is None:
            failed += 1
            continue
        betas.append(bb[1])
        lams.append(bb[2])
        rs.append(bb[2] / bb[1] if bb[1] > 0 else math.inf)
    betas, lams, rs = np.array(betas), np.array(lams), np.array(rs)
    q = lambda a, p: float(np.quantile(a, p, method="inverted_cdf"))  # noqa: E731
    # r is unbounded when beta <= 0. JSON has no infinity, so an unbounded r or quantile is
    # recorded as null; the p_ shares below say how often.
    fin = lambda x: x if math.isfinite(x) else None  # noqa: E731
    lo, hi = (1 - CONF) / 2, 1 - (1 - CONF) / 2
    up, pl = betas > 0, lams > 0
    return {
        "months": n,
        "beta": float(b[1]),
        "lambda": float(b[2]),
        "r": fin(float(b[2] / b[1]) if b[1] > 0 else math.inf),
        "beta_lo": q(betas, lo),
        "beta_hi": q(betas, hi),
        "lambda_lo": q(lams, lo),
        "lambda_hi": q(lams, hi),
        "r_lo": fin(q(rs, lo)),
        "r_hi": fin(q(rs, hi)),
        # The draws by sign: only beta > 0 and lambda > 0 is a diminishing-returns law with a
        # positive return; the other three cells are not estimates of r at all.
        "p_both_positive_r_below_1": float(np.mean(up & pl & (rs < 1))),
        "p_both_positive_r_at_least_1": float(np.mean(up & pl & (rs >= 1))),
        "p_beta_positive_lambda_not": float(np.mean(up & ~pl)),
        "p_beta_not_lambda_positive": float(np.mean(~up & pl)),
        "p_both_not_positive": float(np.mean(~up & ~pl)),
        "p_beta_positive": float(np.mean(up)),
        "p_lambda_not_positive": float(np.mean(~pl)),
        "corr_stock_log_input": float(np.corrcoef(u, np.log(e))[0, 1]),
        "corr_beta_lambda_draws": float(np.corrcoef(betas, lams)[0, 1]),
        "draws_kept": int(len(rs)),
        "draws_failed": failed,
        "log_residual_sd": sigma,
        "log_residuals": [float(x) for x in np.log(y[pos] / mu[pos])],
        "months_with_gain": int(pos.sum()),
    }


def part_a(res: Results, L: dict, gen: np.random.Generator) -> dict:
    epoch = read_epoch(fetch(EPOCH_URL, "speedrun/epoch-nanogpt-speedrun-record-time.csv", res,
                             what="Epoch AI, NanoGPT speedrun record training time (series CSV)"))
    readme_times, retimes = read_readme(fetch(README_URL, "speedrun/modded-nanogpt-README.md", res,
                                              what="Modded-NanoGPT README, world record history table"))
    metr = read_metr(fetch(METR_URL, "speedrun/metr-classifications.csv", res,
                           what="METR, classifications of NanoGPT speedrun records 1 to 77"))

    # Cross-check every time across the three sources.
    for r in epoch:
        k = r["record"]
        if k not in readme_times or abs(readme_times[k] / r["seconds"] - 1) > 0.005:
            raise SystemExit(f"record {k}: Epoch's {r['seconds']} s and the README's time disagree")
        if k in metr and abs(metr[k]["minutes"] * 60 / r["seconds"] - 1) > 0.005:
            raise SystemExit(f"record {k}: Epoch's {r['seconds']} s and METR's time disagree")
    if not retimes:
        raise SystemExit("the README lists no re-timings; the rule change at record 21 should be there")

    # Per-record gain: ln(previous time / this time), where the previous time is the latest timing of
    # the previous record (original or re-timed) on or before this record's date.
    for i, r in enumerate(epoch):
        r["humans"] = humans(r["contributors"])
        r["ai_text"] = bool(AI_TEXT.search(r["contributors"]))
        m = metr.get(r["record"])
        r["category"] = m["category"] if m else None
        r["depth"] = m["depth"] if m else None
        r["provenance"] = m["provenance"] if m else None
        r["ai"] = m["ai"] if m else r["ai_text"]
        r["kind"] = None if not m else "systems" if m["category"] in SYSTEMS else "algorithmic" if m["category"] in ALGORITHMIC else None
        if i == 0:
            r["prev_seconds"], r["gain"] = None, None
            continue
        prev = epoch[i - 1]
        prev_s = prev["seconds"]
        for t in sorted(retimes, key=lambda t: t["date"]):
            if t["record"] == prev["record"] and t["date"] <= r["date"]:
                prev_s = t["seconds"]
        r["prev_seconds"] = prev_s
        r["gain"] = math.log(prev_s / r["seconds"])

    # The text rule for AI credit must reproduce METR's flags where both exist.
    disagree = [r["record"] for r in epoch if r["record"] in metr and r["ai_text"] != metr[r["record"]]["ai"]]
    if disagree:
        raise SystemExit(f"the AI-credit text rule disagrees with METR on records {disagree}")
    for r in epoch:
        if r["record"] > 1 and r["kind"] is None and r["record"] in metr:
            raise SystemExit(f"record {r['record']}: METR category {r['category']!r} is not mapped")

    gains = [r for r in epoch if r["gain"] is not None]
    total = sum(r["gain"] for r in gains)
    raw = math.log(epoch[0]["seconds"] / epoch[-1]["seconds"])
    last21 = max((t for t in retimes if t["record"] == 21), key=lambda t: t["date"])
    retime_factor = math.exp(total - raw)

    coded = [r for r in gains if r["record"] in metr]
    algo = sum(r["gain"] for r in coded if r["kind"] == "algorithmic")
    syst = sum(r["gain"] for r in coded if r["kind"] == "systems")
    coded_days = (epoch[len(coded)]["date"] - epoch[0]["date"]).days
    years = lambda d: d / 365.25  # noqa: E731

    ai = [r for r in gains if r["ai"]]
    ai_from, ai_to = min(r["date"] for r in ai), max(r["date"] for r in ai)
    peers = [r for r in gains if not r["ai"] and ai_from <= r["date"] <= ai_to]
    cut = lambda g: 1 - math.exp(-g)  # noqa: E731  share of the training time a record cut

    # METR's depth result from METR's own times (their per-record ratio, re-timing not removed).
    mt = {k: v["minutes"] for k, v in metr.items()}
    by_depth: dict[str, float] = {}
    for k in sorted(metr):
        if k == 1:
            continue
        by_depth[metr[k]["depth"]] = by_depth.get(metr[k]["depth"], 0.0) + math.log(mt[k - 1] / mt[k])
    shallow_moderate = math.exp(by_depth.get("shallow", 0) + by_depth.get("moderate", 0))
    by_prov: dict[str, float] = {}
    for k in sorted(metr):
        if k > 1:
            by_prov[metr[k]["provenance"]] = by_prov.get(metr[k]["provenance"], 0.0) + math.log(mt[k - 1] / mt[k])

    # Window paces, the survey's definitions recomputed from per-record gains.
    def pace(start: date, end: date) -> tuple[float, float]:
        g = sum(r["gain"] for r in gains if start < r["date"] <= end)
        return math.exp(g), math.exp(g * 365.25 / (end - start).days)

    d0 = epoch[0]["date"]
    eight = date(d0.year + (d0.month + 8 - 1) // 12, (d0.month + 8 - 1) % 12 + 1, d0.day)
    first8 = pace(d0, eight)
    y2025 = pace(date(2025, 1, 26), date(2026, 1, 1))
    y2026 = pace(date(2026, 1, 1), epoch[-1]["date"])
    whole = pace(d0, epoch[-1]["date"])

    # Growth-law fit on monthly gains: all records, and the algorithmic ones METR coded.
    last_month = month_start(epoch[-1]["date"])
    for r in epoch:
        r["algo_gain"] = r["gain"] if r["kind"] == "algorithmic" else (0.0 if r["gain"] is not None and r["kind"] else None)
    s_all = monthly(epoch, "gain", INPUT_WINDOW_DAYS, last_month)
    fit_all = fit_growth(s_all, gen, FIT_DRAWS)
    coded_recs = [r for r in epoch if r["record"] in metr]
    s_algo = monthly(coded_recs, "algo_gain", INPUT_WINDOW_DAYS, month_start(coded_recs[-1]["date"]))
    fit_algo = fit_growth(s_algo, gen, FIT_DRAWS)
    alt = {}
    for w in INPUT_WINDOWS_ALT:
        f = fit_growth(monthly(epoch, "gain", w, last_month), gen, FIT_DRAWS // 4)
        alt[f"{w}_days"] = {k: f[k] for k in ("beta", "lambda", "r", "p_both_positive_r_below_1", "p_beta_positive")}
    # Placebo inputs that carry no information about research effort. If they give an r like the
    # contributors' one, the fit is reading the curvature of a time trend, not a return to input.
    placebo = {}
    months = [date.fromisoformat(m + "-01") for m in s_all["months"]]
    for name, values in (
        ("months_since_start", [i + 1 for i in range(len(months))]),
        (f"records_in_previous_{INPUT_WINDOW_DAYS}_days",
         [sum(1 for r in gains if m - timedelta(days=INPUT_WINDOW_DAYS) <= r["date"] < m) for m in months]),
    ):
        f = fit_growth({**s_all, "input": np.array(values, float)}, gen, FIT_DRAWS // 4)
        placebo[name] = {k: f[k] for k in ("beta", "lambda", "r", "corr_stock_log_input")}
    pos_gain = s_all["gain"][s_all["gain"] > 0]

    n_rec = len(epoch)
    res.number("e4-records", n_rec, unit="records", fmt=",.0f",
               label="NanoGPT speedrun records in Epoch's series, record 1 (the llm.c baseline) included")
    res.number("e4-speedup", math.exp(total), fmt=",.0f",
               label="speedrun speedup on fixed 8xH100 hardware, the product of every record's gain over the previous record's time under the rules then in force")
    res.number("e4-retime-factor", retime_factor, fmt=".3f",
               label="factor by which re-timings lengthened record 21 (the compile-flag ban, then a newer PyTorch), progress the raw first-to-last ratio misses",
               note=f"record 21 went from {epoch[20]['seconds']:.2f} s to {last21['seconds']:.2f} s without a change of method")
    res.number("e4-efolds", total, unit="e-folds", fmt=".2f",
               label="speedrun progress on a log compute-equivalent axis, natural log of the speedup")
    res.number("e4-algo-factor", math.exp(algo), fmt=",.1f",
               label=f"speedup from algorithmic records 2 to {coded[-1]['record']} (METR's categories other than systems)")
    res.number("e4-systems-factor", math.exp(syst), fmt=",.1f",
               label=f"speedup from systems records 2 to {coded[-1]['record']} (parallelisation, kernels, framework upgrades, number formats)")
    res.number("e4-algo-share", algo / (algo + syst), fmt="%",
               label=f"algorithmic records' share of the log speedup, records 2 to {coded[-1]['record']}")
    res.number("e4-algo-annual", math.exp(algo / years(coded_days)), fmt=".1f",
               label=f"yearly algorithmic speedup at fixed small-scale hardware, records 2 to {coded[-1]['record']} (multiplier)")
    res.number("e4-systems-annual", math.exp(syst / years(coded_days)), fmt=".1f",
               label=f"yearly systems speedup at fixed hardware, records 2 to {coded[-1]['record']} (multiplier)")
    res.number("e4-ai-records", len(ai), unit="records", fmt=",.0f",
               label="records credited to an AI system (each with a human), all 92 records")
    res.number("e4-ai-factor", math.exp(sum(r["gain"] for r in ai)), fmt=".3f",
               label="combined speedup of the AI-credited records")
    res.number("e4-ai-share", sum(r["gain"] for r in ai) / total, fmt=".1%",
               label="AI-credited records' share of the speedrun's log speedup")
    res.number("e4-ai-median-cut", cut(float(np.median([r["gain"] for r in ai]))), fmt=".1%",
               label="median cut in training time per AI-credited record")
    res.number("e4-peer-median-cut", cut(float(np.median([r["gain"] for r in peers]))), fmt=".1%",
               label=f"median cut per human record over the same dates ({ai_from.isoformat()} to {ai_to.isoformat()})")
    res.number("e4-ai-period-share", sum(r["gain"] for r in ai) / (sum(r["gain"] for r in ai) + sum(r["gain"] for r in peers)), fmt="%",
               label="AI-credited records' share of the log speedup over the dates on which AI-credited records were set")
    res.number("e4-metr-shallow-moderate", shallow_moderate, fmt=".1f",
               label="speedup from records METR rates shallow or moderate, recomputed from METR's classifications (METR states about 21)")
    res.number("e4-pace-first8", first8[1], fmt=",.0f",
               label=f"annualised speedup in the first 8 months ({d0.isoformat()} to {eight.isoformat()})")
    res.number("e4-pace-2025", y2025[0], fmt=".2f",
               label="speedup from 2025-01-26 to 2026-01-01, with the re-timing of record 21 removed")
    res.number("e4-pace-2026", y2026[1], fmt=".1f",
               label=f"annualised speedup from 2026-01-01 to {epoch[-1]['date'].isoformat()}")
    res.number("e4-pace-whole", whole[1], fmt=".1f",
               label="annualised speedup over the whole record, re-timing removed")
    # The growth-law fit identifies nothing: stock and log input are nearly collinear trends, and
    # placebo inputs give similar values. Its point estimates stay in details, marked so; the ledger
    # gets only the diagnostics that say why.
    res.number("e4-sr-collinearity", fit_all["corr_stock_log_input"], fmt=".2f",
               label=f"correlation across months between the speedrun's stock (log speedup) and the log of its research input (contributors over the previous {INPUT_WINDOW_DAYS} days)")
    res.number("e4-sr-boot-corr", fit_all["corr_beta_lambda_draws"], fmt=".2f",
               label="correlation between beta and lambda across block-bootstrap draws of the speedrun's growth-law fit")
    res.number("e4-sr-placebo-r-time", placebo["months_since_start"]["r"], fmt=".2f",
               label="the speedrun's r with months since the start put in place of contributors (a placebo input)")
    res.number("e4-sr-placebo-r-records", placebo[f"records_in_previous_{INPUT_WINDOW_DAYS}_days"]["r"], fmt=".2f",
               label=f"the speedrun's r with the count of records over the previous {INPUT_WINDOW_DAYS} days put in place of contributors (a placebo input)")
    res.number("e4-sr-p-unbounded", 1 - fit_all["p_beta_positive"], fmt="%",
               label="share of block-bootstrap draws in which monthly gains do not fall as the speedup grows (beta at or below 0)",
               note=f"{fit_all['p_beta_not_lambda_positive']:.1%} with lambda above 0 (r unbounded) and {fit_all['p_both_not_positive']:.1%} with both signs flipped")
    res.number("e4-sr-p-below-1", fit_all["p_both_positive_r_below_1"], fmt="%",
               label="share of block-bootstrap draws giving a diminishing-returns law with a positive return below 1 (beta and lambda above 0, r below 1)")
    res.number("e4-sr-p-negative-lambda", fit_all["p_lambda_not_positive"], fmt="%",
               label="share of block-bootstrap draws in which more contributors predict smaller gains (lambda at or below 0)")
    res.number("e4-sr-sigma", fit_all["log_residual_sd"], fmt=".2f",
               label="spread of the speedrun's monthly gains about the fitted law (sd of ln gain over fitted, months with a record): the noise part (c) is calibrated on")
    res.number("e4-sr-month-gain", float(np.median(pos_gain)), unit="e-folds", fmt=".3f",
               label="median monthly gain of the speedrun, months with a record, natural log of the speedup")

    res.detail("records", [
        {
            "record": r["record"], "date": r["date"].isoformat(), "seconds": r["seconds"],
            "previous_seconds": r["prev_seconds"], "gain_efolds": r["gain"], "kind": r["kind"],
            "metr_category": r["category"], "metr_depth": r["depth"], "metr_provenance": r["provenance"],
            "ai_credited": r["ai"], "human_contributors": len(r["humans"]),
        }
        for r in epoch
    ])
    res.detail("retimings", [{**t, "date": t["date"].isoformat()} for t in retimes])
    res.detail("by_metr_depth_efolds", by_depth)
    res.detail("by_metr_provenance_efolds", by_prov)
    res.detail("windows", {
        "first_8_months": {"from": d0.isoformat(), "to": eight.isoformat(), "factor": first8[0], "annual": first8[1]},
        "2025": {"from": "2025-01-26", "to": "2026-01-01", "factor": y2025[0], "annual": y2025[1]},
        "2026": {"from": "2026-01-01", "to": epoch[-1]["date"].isoformat(), "factor": y2026[0], "annual": y2026[1]},
        "whole": {"from": d0.isoformat(), "to": epoch[-1]["date"].isoformat(), "factor": whole[0], "annual": whole[1]},
        "survey_values": {k: L[k] for k in ("dyn-speedrun-first-annual", "dyn-speedrun-rate-2025",
                                            "dyn-speedrun-2026-annual", "dyn-speedrun-annual")},
    })
    res.detail("growth_fit_all_records", {**fit_all, "monthly": {
        "months": s_all["months"], "gain": s_all["gain"].tolist(), "stock": s_all["stock"].tolist(),
        "input": s_all["input"].tolist()}})
    res.detail("growth_fit_algorithmic", fit_algo)
    res.detail("growth_fit_input_window_sensitivity", alt)
    res.detail("growth_fit_placebo_inputs", placebo)
    res.detail("growth_fit_note", (
        "Not an estimate of r. Over the fitted months the stock and the log input rise together "
        "(see e4-sr-collinearity), so beta and lambda trade off in the bootstrap, and placebo inputs "
        "give similar values of r. The input counts people credited on records that succeeded, so it "
        "depends on the gains it is meant to explain, even lagged. The point estimates are kept here "
        "only to show the fit; the ledger carries the diagnostics."))
    res.detail("axis_note", FLOP_NOTE)
    res.detail("classification_note", (
        "Systems: METR categories " + ", ".join(sorted(SYSTEMS)) + ". Algorithmic: " + ", ".join(sorted(ALGORITHMIC)) +
        f". Records after {coded[-1]['record']} are not classified by METR and enter only totals, paces and the all-record fit. "
        "AI credit: METR's flag for records it coded, else the text 'AI system' in the contributors; the rule reproduces METR's flags."))
    return {"sigma": fit_all["log_residual_sd"], "month_gain": float(np.median(pos_gain)),
            "residuals": fit_all["log_residuals"]}


# -------------------------------------------------------------------------------------------------
# Part (c): the staged estimator in simulation

LNB = np.log(np.array(BUDGETS))


def f_corr(x: np.ndarray) -> np.ndarray:
    """f(x) = ln((e^x - 1) / x), the gap between the exact round identity and its first-order form
    (Part III, Corollary 4.1a). Smooth through 0, where it is x / 2; computed piecewise so that it
    neither overflows nor cancels."""
    with np.errstate(all="ignore"):
        mid = np.log(np.expm1(x) / x)
        pos = x + np.log1p(-np.exp(-x)) - np.log(x)
        neg = np.log1p(-np.exp(x)) - np.log(-x)
        out = np.where(x > 1, pos, np.where(x < -1, neg, mid))
        return np.where(np.abs(x) < 1e-6, x / 2, out)


def f_slope(x: np.ndarray) -> np.ndarray:
    """f'(x) = 1 / (1 - e^(-x)) - 1 / x, which rises from 0 to 1 through 1/2 at 0."""
    with np.errstate(all="ignore"):
        out = 1.0 / (-np.expm1(-x)) - 1.0 / x
        return np.where(np.abs(x) < 1e-6, 0.5 + x / 12, out)


def log_gain(v: np.ndarray, b) -> np.ndarray:
    """ln Delta under the exact round law of Part III (A4.1) with a fixed researcher:
    e^(b Delta) - 1 = b e^v, so Delta = ln(1 + b e^v) / b, and e^v at b = 0. A round whose law
    explodes (1 + b e^v <= 0, possible only for b < 0) is capped at STEP_CAP."""
    with np.errstate(all="ignore"):
        t = b * np.exp(np.minimum(v, 700.0))
        g = np.where(np.abs(t) < 1e-8, -t / 2, np.log(np.log1p(t) / t))
        return np.where(t <= -1.0, STEP_CAP, np.minimum(v + g, STEP_CAP))


def solve3(y: np.ndarray, w: np.ndarray):
    """Least squares of y on [1, ln B, -w] for every leading index at once; y and w have shape
    (..., budgets, rounds). Returns the intercept, the coefficient on ln B and the one on -w."""
    cols = [np.ones_like(y), np.broadcast_to(LNB[:, None], y.shape), -w]
    XtX = np.empty(y.shape[:-2] + (3, 3))
    Xty = np.empty(y.shape[:-2] + (3,))
    for i in range(3):
        Xty[..., i] = (cols[i] * y).sum(axis=(-2, -1))
        for j in range(i, 3):
            XtX[..., i, j] = XtX[..., j, i] = (cols[i] * cols[j]).sum(axis=(-2, -1))
    sol = np.linalg.solve(XtX, Xty[..., None])[..., 0]
    return sol[..., 0], sol[..., 1], sol[..., 2]


def fit_level(y, u, yb=None):
    """First-order level form: ln Delta = c + lambda ln B - b u. Misspecified under the exact law."""
    return solve3(y if yb is None else yb, u)


def fit_exact_nls(y, u, yb=None):
    """The exact round identity in level form, ln Delta + f(b Delta) = c + lambda ln B - b u, by
    Gauss-Newton from the first-order fit: least squares on the identity's residual. It ignores that
    the transform of the data depends on b, so it favours a b that shrinks the transformed spread;
    kept to show that bias. With a second held-out set, yb is the response and y (with u) the
    regressor side."""
    resp = y if yb is None else yb
    c, lam, b = solve3(resp, u)
    gain = np.exp(np.minimum(resp, STEP_CAP))
    for _ in range(GN_ITERS):
        x = b[..., None, None] * gain
        fs = f_slope(x)
        c, lam, b = solve3(resp + f_corr(x) - fs * x, u + fs * gain)
    return c, lam, b


def log_jacobian(x: np.ndarray) -> np.ndarray:
    """ln(x / (1 - e^(-x))) = ln(1 + x f'(x)), the log of d[ln Delta + f(b Delta)] / d ln Delta at
    x = b Delta; 0 at x = 0."""
    with np.errstate(all="ignore"):
        mid = np.log(x / (-np.expm1(-x)))
        out = np.where(x > 30, np.log(x), np.where(x < -30, np.log(-x) + x, mid))
        return np.where(np.abs(x) < 1e-6, x / 2, out)


def profile_loglik(b: np.ndarray, resp: np.ndarray, gain: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Profile log-likelihood of b under the exact law with normal errors in v: c and lambda are
    concentrated out by least squares, and the Jacobian of the b-dependent transform is added."""
    bb = b[..., None, None]
    x = bb * gain
    q = resp + f_corr(x) + bb * u
    qm = q.mean(axis=-1)
    bc = LNB - LNB.mean()
    slope = (qm * bc).sum(axis=-1) / (bc * bc).sum()
    fitted = qm.mean(axis=-1)[..., None] + slope[..., None] * bc
    rss = ((q - fitted[..., None]) ** 2).sum(axis=(-2, -1))
    ll = -0.5 * q.shape[-1] * q.shape[-2] * np.log(rss) + log_jacobian(x).sum(axis=(-2, -1))
    return np.where(np.isfinite(ll), ll, -np.inf)


def fit_exact_ml(y, u, yb=None):
    """The exact round identity by maximum likelihood: a grid over b, then golden-section search
    around the best grid point. b at or below 0 (gains that do not diminish) is allowed."""
    resp = y if yb is None else yb
    gain = np.exp(np.minimum(resp, STEP_CAP))
    shape = resp.shape[:-2]
    grid = np.arange(ML_LO, ML_HI + ML_STEP / 2, ML_STEP)
    ll = np.stack([profile_loglik(np.full(shape, g), resp, gain, u) for g in grid], axis=-1)
    best = grid[np.argmax(ll, axis=-1)]
    lo, hi = best - ML_STEP, best + ML_STEP
    gr = (math.sqrt(5) - 1) / 2
    for _ in range(ML_GOLDEN):
        m1, m2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
        left = profile_loglik(m1, resp, gain, u) > profile_loglik(m2, resp, gain, u)
        hi, lo = np.where(left, m2, hi), np.where(left, lo, m1)
    b = (lo + hi) / 2
    c, lam = budgets_fit(resp + f_corr(b[..., None, None] * gain), b, u)
    return c, lam, b


def budgets_fit(h: np.ndarray, b: np.ndarray, u: np.ndarray):
    """lambda and the intercept from how the gain scales with budget once b u is added back."""
    w = (h + b[..., None, None] * u).mean(axis=-1)
    bc = LNB - LNB.mean()
    lam = (w * bc).sum(axis=-1) / (bc * bc).sum()
    return w.mean(axis=-1) - lam * LNB.mean(), lam


def fit_diff1(y, u, yb=None):
    """C4 as first written: ln(Delta_(k+1) / Delta_k) = -b Delta_k through the origin, pooled over
    budgets, then lambda from the budgets. With two held-out sets the regressor Delta_k comes from
    set A (y) and the response from set B (yb), as Part III's Proposition 4.6 proposes."""
    resp = y if yb is None else yb
    z = resp[..., 1:] - resp[..., :-1]
    x = np.exp(np.minimum(y, STEP_CAP))[..., :-1]
    b = -(x * z).sum(axis=(-2, -1)) / (x * x).sum(axis=(-2, -1))
    c, lam = budgets_fit(resp, b, u)
    return c, lam, b


def fit_diffx(y, u, yb=None):
    """Lemma 4.1 with a fixed researcher, [ln Delta + f(b Delta)]_(k+1) - [same]_k = -b Delta_k,
    solved by fixed-point iteration so that the regressor stays on set A."""
    resp = y if yb is None else yb
    _, _, b = fit_diff1(y, u, yb)
    x = np.exp(np.minimum(y, STEP_CAP))[..., :-1]
    sxx = (x * x).sum(axis=(-2, -1))
    gb = np.exp(np.minimum(resp, STEP_CAP))
    for _ in range(FP_ITERS):
        h = resp + f_corr(b[..., None, None] * gb)
        b = -(x * (h[..., 1:] - h[..., :-1])).sum(axis=(-2, -1)) / sxx
    c, lam = budgets_fit(resp + f_corr(b[..., None, None] * gb), b, u)
    return c, lam, b


# Each estimator with the law its bootstrap regenerates from (its own fitted law).
FITS = {"level": (fit_level, "first"), "difference": (fit_diff1, "first"), "exact_ml": (fit_exact_ml, "exact")}


def stock_before(gains: np.ndarray) -> np.ndarray:
    """u_k, the stock gained before round k: 0, D_1, D_1 + D_2, ..."""
    c = np.cumsum(gains, axis=-1)
    return np.concatenate([np.zeros(gains.shape[:-1] + (1,)), c[..., :-1]], axis=-1)


def ratio(lam: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """r = lambda / b, infinite where the gains do not diminish (b at or below 0)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(beta > 0, lam / np.where(beta > 0, beta, 1.0), np.inf)


def interval(gen: np.random.Generator, y: np.ndarray, u: np.ndarray, est: str, boot: int):
    """Point estimate of r and its two-sided interval by a recursive residual bootstrap: the fitted
    law regenerates each run round by round from resampled residuals, and the estimator is refitted.
    Also r's upper bound at the K rule's share of the one-sided error, K_SPLIT * (1 - CONF) / 2."""
    fit, law = FITS[est]
    c, lam, b = fit(y, u)
    m, nb, n = y.shape
    lhs = y + f_corr(b[:, None, None] * np.exp(np.minimum(y, STEP_CAP))) if law == "exact" else y
    resid = lhs - (c[:, None, None] + lam[:, None, None] * LNB[:, None] - b[:, None, None] * u)
    # Centred, and inflated by sqrt(N / (N - 3)) for the three fitted parameters, since least-squares
    # residuals are smaller than the errors they estimate (the usual degrees-of-freedom adjustment).
    resid = (resid - resid.mean(axis=(-2, -1), keepdims=True)).reshape(m, nb * n)
    resid = resid * math.sqrt(nb * n / (nb * n - 3))
    pick = gen.integers(0, nb * n, (m, boot, nb * n))
    e = np.take_along_axis(resid[:, None, :], pick, axis=-1).reshape(m, boot, nb, n)
    ys = np.empty((m, boot, nb, n))
    us = np.empty((m, boot, nb, n))
    stock = np.zeros((m, boot, nb))
    base = c[:, None, None] + lam[:, None, None] * LNB
    bb = b[:, None, None]
    for k in range(n):
        us[..., k] = stock
        v = base - bb * stock + e[..., k]
        ys[..., k] = log_gain(v, bb) if law == "exact" else v
        stock = stock + np.exp(np.minimum(ys[..., k], STEP_CAP))
    _, lam_b, b_b = fit(ys, us)
    r_b = ratio(lam_b, b_b)
    lo = np.quantile(r_b, (1 - CONF) / 2, axis=1, method="inverted_cdf")
    hi = np.quantile(r_b, (1 + CONF) / 2, axis=1, method="inverted_cdf")
    hi_k = np.quantile(r_b, 1 - K_SPLIT * (1 - CONF) / 2, axis=1, method="inverted_cdf")
    return ratio(lam, b), lo, hi, hi_k


def withheld(strategy: str, t: float, n: int) -> np.ndarray:
    """Share of each round's achievable gain a sandbagger withholds, by budget (rows) and round,
    for the patterns that choose when to hide; scaled so the mean share is t, capped at 0.95."""
    k = np.arange(n) / max(n - 1, 1)
    j = np.arange(len(BUDGETS)) / (len(BUDGETS) - 1)
    w = {"uniform": np.ones((len(BUDGETS), n)), "late": np.broadcast_to(k, (len(BUDGETS), n)),
         "budget": np.broadcast_to(j[:, None], (len(BUDGETS), n)), "targeted": j[:, None] * k}[strategy]
    return np.minimum(t * w / w.mean(), 0.95)


def simulate(gen: np.random.Generator, r: float, lam: float, d1: float, sigma: float, nmax: int, sims: int,
             law: str = "first", meas: float = 0.0, sets: int = 1, strategy: str = "honest", t: float = 0.0,
             pool: np.ndarray | None = None) -> dict:
    """True paths of `sims` staged experiments and their measured gains. The researcher is fixed
    (closure 0), so r = lambda / b is the gain the loop would have if closed. sigma is the sd of the
    log gain per round: a share `meas` of its variance is error in measuring the gain (drawn afresh
    for each held-out set), the rest is real variation in the round's productivity. With `pool`, the
    real variation is drawn from that set of residuals instead of a normal. A sandbagger delivers
    less than it achieves; what it withholds is not banked, so its stock grows by what it delivers."""
    b = lam / r
    sp, sm = sigma * math.sqrt(1 - meas), sigma * math.sqrt(meas)
    nb = len(BUDGETS)
    c0 = math.log(d1) + float(f_corr(np.array(b * d1))) if law == "exact" else math.log(d1)
    if pool is not None:
        eps = gen.choice(pool - pool.mean(), size=(sims, nb, nmax))
    else:
        eps = gen.normal(0.0, sp, (sims, nb, nmax))
    stock = np.zeros((sims, nb))
    y = np.empty((sims, nb, nmax))
    able = np.zeros(sims)
    gave = np.zeros(sims)
    share = withheld(strategy, t, nmax) if strategy in ("uniform", "late", "budget", "targeted") else None
    for k in range(nmax):
        v = c0 + lam * LNB - b * stock
        cap = log_gain(v + eps[..., k], b) if law == "exact" else v + eps[..., k]
        if strategy == "honest":
            got = cap
        elif strategy == "luck":  # withholds a share t of whatever the round's luck added
            typical = log_gain(v, b) if law == "exact" else v
            got = cap + np.log1p(-t * np.maximum(-np.expm1(typical - cap), 0.0))
        else:
            got = cap + np.log1p(-share[:, k])
        y[..., k] = got
        if strategy != "honest":
            able += np.exp(cap).sum(axis=-1)
            gave += np.exp(got).sum(axis=-1)
        stock = stock + np.exp(got)
    out = {"y": y, "hidden": 1 - gave / able if strategy != "honest" else np.zeros(sims)}
    meas_sets = []
    for _ in range(sets):
        meas_sets.append(y + gen.normal(0.0, sm, y.shape) if meas > 0 else y)
    out["sets"] = meas_sets
    return out


def cell(gen: np.random.Generator, r: float, lam: float, d1: float, sigma: float, rounds: tuple,
         est: str = "level", **kw) -> dict:
    """SIMS staged experiments at one setting, each evaluated after every round count in `rounds`:
    coverage of the interval for r, how often each rule fires, and the hidden share. Keys are the
    round counts alone (JSON sorts keys, so an int and a str cannot share a level); the hidden share,
    taken over all max(rounds) rounds, sits in each round count's entry."""
    nmax = max(rounds)
    tally = {n: {"cover": 0, "cover_upper": 0, "ub_inf": 0, "lb_fires": 0, "point": [],
                 "ub_fires": {g: 0 for g in G_STAR_SWEEP}, "kb_fires": {g: 0 for g in G_STAR_SWEEP},
                 "cover_upper_k": 0} for n in rounds}
    hidden = []
    for _ in range(SIMS // CHUNK):
        sim = simulate(gen, r, lam, d1, sigma, nmax, CHUNK, **kw)
        y = sim["sets"][0]
        hidden.append(sim["hidden"])
        for n in rounds:
            point, lo, hi, hi_k = interval(gen, y[..., :n], stock_before(np.exp(y[..., :n])), est, BOOT)
            tl = tally[n]
            tl["cover"] += int(((lo <= r) & (r <= hi)).sum())
            tl["cover_upper"] += int((r <= hi).sum())
            tl["ub_inf"] += int(np.isinf(hi).sum())
            tl["lb_fires"] += int((lo >= 1.0).sum())
            # True closure 1, so the true K is r; the K rule's bound is U_E times r's wider bound.
            tl["cover_upper_k"] += int((r <= U_E * hi_k).sum())
            for g in G_STAR_SWEEP:
                tl["ub_fires"][g] += int((hi > g).sum())
                tl["kb_fires"][g] += int((U_E * hi_k > g).sum())
            tl["point"].append(point)
    hidden_share = float(np.mean(np.concatenate(hidden)))
    out = {}
    for n, tl in tally.items():
        pts = np.concatenate(tl["point"])
        out[n] = {
            "coverage": tl["cover"] / SIMS,
            "upper_coverage": tl["cover_upper"] / SIMS,
            "upper_unbounded": tl["ub_inf"] / SIMS,
            "lower_rule_fires": tl["lb_fires"] / SIMS,
            "upper_rule_fires": {f"{g:g}": v / SIMS for g, v in tl["ub_fires"].items()},
            "k_rule_fires": {f"{g:g}": v / SIMS for g, v in tl["kb_fires"].items()},
            "k_upper_coverage": tl["cover_upper_k"] / SIMS,
            "median_estimate_over_true": float(np.median(pts) / r),
            "hidden_share": hidden_share,
        }
    return out


BIAS_FITS = {"level_first_order": fit_level, "level_exact_least_squares": fit_exact_nls,
             "level_exact_likelihood": fit_exact_ml,
             "difference_first_order": fit_diff1, "difference_exact": fit_diffx}


def bias_cell(gen: np.random.Generator, r: float, lam: float, d1: float, sigma: float, n: int,
              law: str, meas: float) -> dict:
    """Median point estimate of r over the truth, every estimator on one or two held-out sets, from
    the same BIAS_SIMS runs. Two sets: the regressor side (the stock, and Delta_k in the difference
    forms) from set A, the response from set B."""
    sim = simulate(gen, r, lam, d1, sigma, n, BIAS_SIMS, law=law, meas=meas, sets=2)
    ya, yb = sim["sets"]
    ua = stock_before(np.exp(ya))
    out = {}
    for name, fit in BIAS_FITS.items():
        for sets, resp in (("one_set", None), ("two_sets", yb)):
            _, lam_h, b_h = fit(ya, ua, resp)
            rh = ratio(lam_h, b_h)
            med = float(np.median(rh) / r)
            # More than half the draws unbounded leaves no finite median; JSON has no infinity, so
            # record null and let share_unbounded say why.
            out[f"{name}_{sets}"] = {"median_over_true": med if np.isfinite(med) else None,
                                     "share_unbounded": float(np.mean(np.isinf(rh)))}
    return out


def part_c(res: Results, L: dict, cal: dict, gen: np.random.Generator) -> None:
    lam = L["dyn-sie-lambda"]
    r_med, r_hi, r_lo = L["dyn-r-lm-corrected"], L["dyn-r-lm-hi-corrected"], L["dyn-r-lm-lo-corrected"]
    n5 = int(L["claim-d2-rounds"])
    nb = len(BUDGETS)
    target = 1 - CONF
    rounds = tuple(sorted(set(N_GRID) | {n5}))
    r_grid = tuple(sorted({r_lo, r_med, r_hi, G_STAR, *R_EXTRA}))
    main = (cal["month_gain"], cal["sigma"])
    fav = FAVOURABLE
    mid = MIDDLE
    d1s = (main[0], *D1_GRID)
    sigmas = (*SIGMA_GRID, main[1])
    pool = np.array(cal["residuals"])
    key = lambda r, d1, s: f"r={r:.3f} d1={d1:.3f} sigma={s:.3f}"  # noqa: E731
    bud = ", ".join(f"{x:g}" for x in BUDGETS[:-1]) + f" and {BUDGETS[-1]:g}"
    staged = lambda n: f"{n} rounds at each of {nb} budgets ({bud} times the base; {n * nb} staged rounds)"  # noqa: E731
    per_round = {"cal": f"speedrun-calibrated rounds (first-round gain {main[0]:.3f} e-folds at the base budget, noise sd {main[1]:.2f} in each round's ln gain)",
                 "fav": f"favourable rounds (first-round gain {fav[0]:g} e-fold at the base budget, noise sd {fav[1]:g} in each round's ln gain)"}
    k_rule = (f"the K rule: fires when the closure's upper bound ({U_E:g}, a loop that may be fully closed) times r's upper bound at "
              f"{K_SPLIT:.0%} of the one-sided error exceeds K* = {G_STAR:g}, true closure 1 so the true K is r")
    mc = lambda p: math.sqrt(max(p * (1 - p), 1e-12) / SIMS)  # noqa: E731
    k_note = ("for r alone: the trigger on K multiplies r's bound by the closure's at a share of the error "
              "(Part III, Corollary 4.5a), so the K rule fires at least as often; its own rates are the e4-k-* numbers")

    # The trigger: the first-order law fitted in its own level form, honest agent.
    sweep = {}
    for d1 in d1s:
        for s in sigmas:
            for r in r_grid:
                sweep[key(r, d1, s)] = cell(gen, r, lam, d1, s, rounds)
    # The same with the real variation drawn from the speedrun's own monthly residuals (not normal).
    empirical = {key(r, main[0], main[1]): cell(gen, r, lam, main[0], main[1], rounds, pool=pool)
                 for r in (r_med, r_hi)}
    # Data from Part III's exact round law: fitted by the first-order level form (misspecified), and
    # by the exact identity's likelihood. And the first-order difference form with its own interval.
    first = {key(r, *st): cell(gen, r, lam, *st, rounds, law="exact") for r in (r_med, r_hi) for st in (main, fav)}
    xml = {key(r, *st): cell(gen, r, lam, *st, (n5,), est="exact_ml", law="exact") for r in (r_med, r_hi) for st in (main, fav)}
    diff = {key(r_med, *st): cell(gen, r_med, lam, *st, (n5,), est="difference") for st in (main, fav)}
    # Sandbaggers that choose when to hide, after n5 rounds, with the true r at the corrected 95th
    # percentile, where the rule should fire.
    sandbag = {}
    for st, name in ((main, "cal"), (fav, "fav")):
        for strategy in STRATEGIES:
            for t in HIDE_GRID:
                sandbag[f"{name} {strategy} t={t:g}"] = cell(gen, r_hi, lam, *st, (n5,), strategy=strategy, t=t)
    # The first-round gain a 5-round test needs.
    need = {}
    for s in sigmas:
        for d1 in D1_FINE:
            need[key(r_med, d1, s)] = cell(gen, r_med, lam, d1, s, (n5,))[n5]
    # Bias of every estimator on one and two held-out sets, by how much of the noise is measurement.
    bias = {}
    for law in ("exact", "first"):
        for st, name in ((main, "cal"), (mid, "mid"), (fav, "fav")):
            for meas in MEAS_MIX:
                bias[f"{law} {name} meas={meas:g}"] = bias_cell(gen, r_med, lam, *st, n5, law, meas)

    g = f"{G_STAR:g}"
    at = lambda table, r, st, n: table[key(r, *st)][n]  # noqa: E731
    fire = lambda table, r, st, n: at(table, r, st, n)["upper_rule_fires"][g]  # noqa: E731
    kfire = lambda table, r, st, n: at(table, r, st, n)["k_rule_fires"][g]  # noqa: E731

    cov5 = {k: v[n5]["coverage"] for k, v in sweep.items()}
    slack = 2 * math.sqrt(CONF * (1 - CONF) / SIMS)  # two Monte Carlo standard errors
    holds = [n for n in rounds if all(v[n]["coverage"] >= CONF - slack for v in sweep.values())]
    fa_main = [fire(sweep, r_med, main, n) for n in rounds]
    fa_fav = [fire(sweep, r_med, fav, n) for n in rounds]
    gap_main = [fire(sweep, r_hi, main, n) - fire(sweep, r_med, main, n) for n in rounds]
    n_fa_main = next((n for n, f in zip(rounds, fa_main) if f <= target), None)
    n_fa_fav = next((n for n, f in zip(rounds, fa_fav) if f <= target), None)
    need_d1 = {f"{s:.3f}": next((d1 for d1 in D1_FINE if need[key(r_med, d1, s)]["upper_rule_fires"][g] <= target), None)
               for s in sigmas}
    fa5 = fire(sweep, r_med, main, n5)

    res.number("e4-gstar", G_STAR, fmt=".2f",
               label="margin K* below 1 (g* in earlier drafts) that the simulated upper bound is compared with, a placeholder: the research sets none yet",
               note="the result sweeps " + ", ".join(f"{x:g}" for x in G_STAR_SWEEP) + " in details")
    res.number("e4-cal-d1", main[0], unit="e-folds", fmt=".3f",
               label="first-round gain at the base budget in the speedrun-calibrated setting (the speedrun's median monthly gain)")
    res.number("e4-cal-sigma", main[1], fmt=".2f",
               label="noise per round in the speedrun-calibrated setting (sd of ln gain; the speedrun's monthly spread about its fitted law)")
    res.number("e4-cov-n5", cov5[key(r_med, *main)], fmt="%",
               label=f"coverage of the {CONF:.0%} interval for r after {staged(n5)}, true r at the corrected median, {per_round['cal']}, the first-order law fitted in its own level form")
    res.number("e4-cov-n5-min", min(cov5.values()), fmt="%",
               label=f"lowest coverage of the {CONF:.0%} interval after {staged(n5)} over the whole grid of true r, round size and noise")
    res.number("e4-cov-nmax-min", min(v[max(rounds)]["coverage"] for v in sweep.values()), fmt="%",
               label=f"lowest coverage of the {CONF:.0%} interval after {staged(max(rounds))} over the same grid")
    if holds:
        res.number("e4-cov-rounds", holds[0], unit="rounds per budget", fmt=",.0f",
                   label=f"fewest rounds per budget, of {', '.join(map(str, rounds))}, after which coverage is within two Monte Carlo errors of {CONF:.0%} everywhere on the grid; three budgets make each round three staged rounds")
    res.number("e4-ub-unbounded-n5", at(sweep, r_med, main, n5)["upper_unbounded"], fmt="%",
               label=f"share of speedrun-calibrated runs whose upper bound on r is unbounded after {staged(n5)} (true r at the corrected median)")
    res.number("e4-fa-n5", fa5, fmt="%",
               label=f"false-alarm rate of the upper-bound trigger on r after {staged(n5)}: true r at the corrected median, {per_round['cal']}, K* = {G_STAR:g}",
               note=f"{k_note}; Monte Carlo standard error {mc(fa5):.1%}")
    res.number("e4-fa-n5-fav", fire(sweep, r_med, fav, n5), fmt="%",
               label=f"the same false-alarm rate with large, tightly measured rounds (first-round gain {fav[0]:g} e-fold, noise {fav[1]:g})",
               note=k_note)
    res.number("e4-fa-gstar-n5", fire(sweep, G_STAR, fav, n5), fmt="%",
               label=f"upper-bound trigger's firing rate with the true gain exactly at K*, after {staged(n5)}, favourable rounds (a calibrated bound gives about {(1 + CONF) / 2:.0%})")
    res.number("e4-fa-nmax", fire(sweep, r_med, main, max(rounds)), fmt="%",
               label=f"false-alarm rate after {staged(max(rounds))}, true r at the corrected median, speedrun-calibrated rounds",
               note=k_note)
    if n_fa_main is not None:
        res.number("e4-fa-rounds", n_fa_main, unit="rounds per budget", fmt=",.0f",
                   label=f"fewest rounds per budget bringing the false-alarm rate at the corrected median to {target:.0%} or less, speedrun-calibrated rounds ({nb} staged rounds each)")
    if n_fa_fav is not None:
        res.number("e4-fa-rounds-fav", n_fa_fav, unit="rounds per budget", fmt=",.0f",
                   label=f"fewest rounds per budget bringing the false-alarm rate at the corrected median to {target:.0%} or less, favourable rounds ({n_fa_fav * nb} staged rounds in all)")
    res.number("e4-fire-gap-n5", gap_main[rounds.index(n5)], fmt="%",
               label=f"upper-bound trigger's firing rate at the corrected 95th percentile of r minus its rate at the corrected median, after {staged(n5)}, speedrun-calibrated rounds: how well it tells the two apart",
               note=f"each rate has a Monte Carlo standard error near {mc(fa5):.1%}")
    res.number("e4-fire-gap-nmax", gap_main[-1], fmt="%",
               label=f"the same difference after {staged(max(rounds))}")
    res.number("e4-fire-gap-n5-fav", fire(sweep, r_hi, fav, n5) - fire(sweep, r_med, fav, n5), fmt="%",
               label=f"the same difference after {staged(n5)} with favourable rounds")
    emp_med, emp_hi = at(empirical, r_med, main, n5), at(empirical, r_hi, main, n5)
    res.number("e4-fa-n5-emp", emp_med["upper_rule_fires"][g], fmt="%",
               label=f"false-alarm rate after {staged(n5)} at the corrected median with each round's real variation drawn from the speedrun's own monthly residuals rather than a normal")
    res.number("e4-fire-gap-n5-emp", emp_hi["upper_rule_fires"][g] - emp_med["upper_rule_fires"][g], fmt="%",
               label="firing rate at the corrected 95th percentile minus at the median, in the same resampled-residual runs")
    res.number("e4-fa-n5-level1", at(first, r_med, main, n5)["upper_rule_fires"][g], fmt="%",
               label=f"false-alarm rate after {staged(n5)} at the corrected median, speedrun-calibrated rounds, when the first-order level form is fitted to data from Part III's exact round law")
    res.number("e4-fire-gap-n5-level1", at(first, r_hi, main, n5)["upper_rule_fires"][g] - at(first, r_med, main, n5)["upper_rule_fires"][g], fmt="%",
               label="firing rate at the corrected 95th percentile minus at the median, in the same exact-law runs")
    res.number("e4-fa-n5-xml", at(xml, r_med, main, n5)["upper_rule_fires"][g], fmt="%",
               label=f"false-alarm rate after {staged(n5)} at the corrected median, speedrun-calibrated rounds, exact-law data fitted by the exact identity's maximum likelihood")
    res.number("e4-fire-gap-n5-xml", at(xml, r_hi, main, n5)["upper_rule_fires"][g] - at(xml, r_med, main, n5)["upper_rule_fires"][g], fmt="%",
               label="firing rate at the corrected 95th percentile minus at the median, in the same runs")
    res.number("e4-cov-n5-xml", at(xml, r_med, main, n5)["coverage"], fmt="%",
               label=f"coverage of the {CONF:.0%} interval in the same runs (true r at the corrected median)")
    for s_key, d1 in need_d1.items():
        if d1 is not None and float(s_key) in (main[1], fav[1]):
            which = "speedrun-calibrated noise" if float(s_key) == main[1] else f"noise {fav[1]:g}"
            res.number("e4-need-d1-cal" if float(s_key) == main[1] else "e4-need-d1-fav", d1, unit="e-folds", fmt=".2f",
                       label=f"smallest first-round gain, of {', '.join(f'{x:g}' for x in D1_FINE)}, at which {staged(n5)} bring the false-alarm rate at the corrected median to {target:.0%} or less ({which})")
    best = min((need[key(r_med, d1, fav[1])]["upper_rule_fires"][g], d1) for d1 in D1_FINE)
    res.number("e4-fa-n5-best", best[0], fmt="%",
               label=f"lowest false-alarm rate at the corrected median after {staged(n5)} over every first-round gain from {D1_FINE[0]:g} to {D1_FINE[-1]:g} e-folds, noise {fav[1]:g}",
               note=f"reached at a first-round gain of {best[1]:g} e-folds")

    # Bias: each estimator on the law it comes from, speedrun-calibrated rounds, n5 rounds per budget.
    bc = lambda m, name, sets, law, setting="cal": bias[f"{law} {setting} meas={m:g}"][f"{name}_{sets}"]["median_over_true"]  # noqa: E731
    real = ("all of the noise is real variation in the round's gain, which a second held-out set "
            "measures identically, so two sets cannot remove this bias")
    res.number("e4-diff-bias", bc(0, "difference_first_order", "one_set", "first"), fmt=".2f",
               label=f"median estimate of r over the true r, C4's first-order difference regression on its own law, {staged(n5)}, speedrun-calibrated rounds, true r at the corrected median, all noise real variation in gain",
               note=real)
    res.number("e4-diff-bias-meas1", bc(1, "difference_first_order", "one_set", "first"), fmt=".2f",
               label="the same ratio when all of the noise is error in measuring each round's gain, one held-out set")
    res.number("e4-diff-bias-meas2", bc(1, "difference_first_order", "two_sets", "first"), fmt=".2f",
               label="the same with two held-out sets (regressor from one, response from the other)")
    res.number("e4-xdiff-bias-real", bc(0, "difference_exact", "one_set", "exact"), fmt=".2f",
               label=f"median estimate of r over the true r from the exact round identity in difference form (Part III, Lemma 4.1) on data from the exact law, {staged(n5)}, speedrun-calibrated rounds, all noise real variation",
               note=real)
    res.number("e4-xdiff-bias-half1", bc(0.5, "difference_exact", "one_set", "exact"), fmt=".2f",
               label="the same estimator with half the noise variance measurement error, one held-out set")
    res.number("e4-xdiff-bias-half2", bc(0.5, "difference_exact", "two_sets", "exact"), fmt=".2f",
               label="the same with two held-out sets, the remedy Part II adopts")
    res.number("e4-xdiff-bias-half2-mid", bc(0.5, "difference_exact", "two_sets", "exact", "mid"), fmt=".2f",
               label=f"the exact difference form on two held-out sets with half the noise measurement error, at smaller noise (first-round gain {mid[0]:g} e-folds, noise {mid[1]:g})")
    res.number("e4-level-bias", bc(0, "level_first_order", "one_set", "first"), fmt=".2f",
               label=f"median estimate of r over the true r from the first-order level form on its own law, {staged(n5)}, speedrun-calibrated rounds, all noise real variation")
    res.number("e4-level-bias-half", bc(0.5, "level_first_order", "one_set", "first"), fmt=".2f",
               label="the same with half the noise variance measurement error, one held-out set (the stock then carries the errors)")
    res.number("e4-level1-bias", bc(0, "level_first_order", "one_set", "exact"), fmt=".2f",
               label="median estimate of r over the true r when the first-order level form is fitted to data from Part III's exact round law (misspecified), speedrun-calibrated rounds, all noise real variation")
    res.number("e4-xnls-bias", bc(0, "level_exact_least_squares", "one_set", "exact"), fmt=".2f",
               label="the same ratio for least squares on the exact identity in level form, exact-law data: the transform depends on b, and least squares ignores its Jacobian")
    res.number("e4-xml-bias", bc(0, "level_exact_likelihood", "one_set", "exact"), fmt=".2f",
               label="the same ratio for maximum likelihood on the exact identity in level form (Jacobian included), exact-law data")
    res.number("e4-diff-cov-n5", at(diff, r_med, main, n5)["coverage"], fmt="%",
               label=f"coverage of the first-order difference form's {CONF:.0%} interval, {staged(n5)}, speedrun-calibrated rounds, true r at the corrected median")
    res.number("e4-diff-fav-bias", bc(0, "difference_first_order", "one_set", "first", "fav"), fmt=".2f",
               label=f"the first-order difference form's median estimate over the true r with favourable rounds, {staged(n5)}, all noise real variation")

    # The honest agent at the corrected 95th percentile, then sandbaggers that choose when to hide.
    for name, st in (("cal", main), ("fav", fav)):
        cv = at(sweep, r_hi, st, n5)
        which = "speedrun-calibrated" if name == "cal" else "favourable"
        res.number(f"e4-late-ub-s0-{name}", 1 - cv["upper_rule_fires"][g], fmt="%",
                   label=f"late-firing rate of the upper-bound trigger on r after {staged(n5)}: true r at the corrected 95th percentile, honest agent, {per_round[name]}")
        res.number(f"e4-miss-lb-s0-{name}", 1 - cv["lower_rule_fires"], fmt="%",
                   label=f"miss rate of the lower-bound rule (fires when the lower bound reaches 1) in the same runs, {which} rounds")
        t_mid = HIDE_GRID[len(HIDE_GRID) // 2]
        cells = {s: sandbag[f"{name} {s} t={t_mid:g}"] for s in STRATEGIES}
        worst = max(STRATEGIES, key=lambda s: (1 - cells[s][n5]["upper_rule_fires"][g], s))
        wv = cells[worst]
        res.number(f"e4-late-ub-hide{int(t_mid * 100)}-{name}", 1 - wv[n5]["upper_rule_fires"][g], fmt="%",
                   label=f"late-firing rate of the upper-bound trigger after {staged(n5)}, true r at the corrected 95th percentile, {which} rounds, an agent withholding on average {t_mid:.0%} of each round's achievable gain in the pattern that most delays the trigger",
                   note=f"pattern: {worst}; it withheld {wv[n5]['hidden_share']:.0%} of the gain it could have delivered")
        res.number(f"e4-miss-lb-hide{int(t_mid * 100)}-{name}", 1 - wv[n5]["lower_rule_fires"], fmt="%",
                   label=f"miss rate of the lower-bound rule against the same agent, {which} rounds")
        res.number(f"e4-late-ub-uniform{int(t_mid * 100)}-{name}", 1 - cells["uniform"][n5]["upper_rule_fires"][g], fmt="%",
                   label=f"late-firing rate of the upper-bound trigger against an agent withholding {t_mid:.0%} of every round alike, {which} rounds (a uniform shortfall moves only the intercept)")
        silent = [(v[n5]["hidden_share"], k) for k, v in sandbag.items()
                  if k.startswith(name + " ") and 1 - v[n5]["upper_rule_fires"][g] >= 0.5]
        if silent:
            h, k = min(silent)
            res.number(f"e4-hide-silence-{name}", h, fmt="%",
                       label=f"smallest share of its achievable gain an agent withheld, over every pattern and strength tried, while keeping the upper-bound trigger silent in at least half of the runs: true r at the corrected 95th percentile, {staged(n5)}, {which} rounds",
                       note=f"cell: {k}. It is the shortfall an elicitation step measuring each round's achievable gain would have to catch")

    # The K rule's own rates (Part III, Corollary 4.5a), beside r's: the trigger is on K = e r.
    res.number("e4-k-alpha-r", K_SPLIT * (1 - CONF) / 2, fmt="%",
               label=f"one-sided error left to r's upper bound in the K rule: {K_SPLIT:.0%} of the {(1 - CONF) / 2:.0%} r's bound has alone, the rest going to the closure's bound (an even split, a design choice)")
    kfa = {"cal": [kfire(sweep, r_med, main, n) for n in rounds], "fav": [kfire(sweep, r_med, fav, n) for n in rounds]}
    kgap = {"cal": [kfire(sweep, r_hi, main, n) - kfire(sweep, r_med, main, n) for n in rounds],
            "fav": [kfire(sweep, r_hi, fav, n) - kfire(sweep, r_med, fav, n) for n in rounds]}
    for name, st in (("cal", main), ("fav", fav)):
        sfx = "" if name == "cal" else "-fav"
        kf = kfire(sweep, r_med, st, n5)
        res.number(f"e4-k-fa-n5{sfx}", kf, fmt="%",
                   label=f"false-alarm rate of the K rule (closure's bound {U_E:g}, r's bound at {K_SPLIT:.0%} of the one-sided error, K* = {G_STAR:g}) after {staged(n5)}: true K at the corrected median of r, {per_round[name]}",
                   note=f"{k_rule}; the rule on r alone fires in {fire(sweep, r_med, st, n5):.1%} of the same runs; Monte Carlo standard error {mc(kf):.1%}")
        res.number(f"e4-k-late-{name}", 1 - kfire(sweep, r_hi, st, n5), fmt="%",
                   label=f"miss rate of the K rule after {staged(n5)}: true K at the corrected 95th percentile of r (closure 1), honest agent, {per_round[name]}",
                   note=f"the rule on r alone misses {1 - fire(sweep, r_hi, st, n5):.1%} of the same runs")
        res.number(f"e4-k-fire-gap-n5{sfx}", kgap[name][rounds.index(n5)], fmt="%",
                   label=f"the K rule's firing rate at the corrected 95th percentile of r minus its rate at the corrected median, after {staged(n5)}, {per_round[name]}: how well it tells the two apart")
        n_k = next((n for n, f in zip(rounds, kfa[name]) if f <= target), None)
        if n_k is not None:
            res.number(f"e4-k-fa-rounds{sfx}", n_k, unit="rounds per budget", fmt=",.0f",
                       label=f"fewest rounds per budget, of {', '.join(map(str, rounds))}, bringing the K rule's false-alarm rate at the corrected median of r to {target:.0%} or less, {per_round[name]}, {nb} staged rounds each ({n_k * nb} in all)")
        t_mid = HIDE_GRID[len(HIDE_GRID) // 2]
        cells = {s_: sandbag[f"{name} {s_} t={t_mid:g}"] for s_ in STRATEGIES}
        worst = max(STRATEGIES, key=lambda s_: (1 - cells[s_][n5]["k_rule_fires"][g], s_))
        res.number(f"e4-k-late-hide{int(t_mid * 100)}-{name}", 1 - cells[worst][n5]["k_rule_fires"][g], fmt="%",
                   label=f"miss rate of the K rule after {staged(n5)}, true K at the corrected 95th percentile of r, {per_round[name]}, an agent withholding on average {t_mid:.0%} of each round's achievable gain in the pattern that most delays the rule",
                   note=f"pattern: {worst}; it withheld {cells[worst][n5]['hidden_share']:.0%} of the gain it could have delivered")
    res.number("e4-k-fa-nmax", kfa["cal"][-1], fmt="%",
               label=f"false-alarm rate of the K rule after {staged(max(rounds))}, true K at the corrected median of r, {per_round['cal']}",
               note=f"the rule on r alone fires in {fa_main[-1]:.1%} of the same runs")
    res.number("e4-k-fa-n5-xml", at(xml, r_med, main, n5)["k_rule_fires"][g], fmt="%",
               label=f"false-alarm rate of the K rule after {staged(n5)}, true K at the corrected median of r, {per_round['cal']}, exact-law data fitted by the exact identity's maximum likelihood")
    res.number("e4-k-fire-gap-n5-xml", at(xml, r_hi, main, n5)["k_rule_fires"][g] - at(xml, r_med, main, n5)["k_rule_fires"][g], fmt="%",
               label="the K rule's firing rate at the corrected 95th percentile of r minus its rate at the median, in the same runs")

    res.detail("simulation_design", {
        "law": "first order: Delta_k = d1 * exp(-b u_k) * (B / B0)^lambda * exp(noise), u_k the stock delivered before round k; robustness cells use Part III's exact law (A4.1, fixed researcher), e^(b Delta_k) - 1 = b exp(c + lambda ln(B / B0) - b u_k + noise), and noise resampled from the speedrun's residuals",
        "estimator": "first-order level form by least squares; in the exact-law cells also the exact identity by maximum likelihood (grid then golden section over b) and by least squares (Gauss-Newton)",
        "lambda": lam, "b": "lambda / r", "budgets": BUDGETS, "rounds_per_budget": rounds, "true_r": r_grid,
        "d1": d1s, "sigma": sigmas, "favourable": fav, "middle": mid, "g_star": G_STAR, "g_star_sweep": G_STAR_SWEEP,
        "sims_per_cell": SIMS, "bootstrap_draws": BOOT, "bias_sims_per_cell": BIAS_SIMS,
        "interval": f"two-sided {CONF:.0%} percentile, recursive residual bootstrap from the estimator's own fitted law",
        "upper_rule": "fires while the upper bound on r exceeds K* (G_STAR)", "lower_rule": "fires once the lower bound on r reaches 1",
        "k_rule": k_rule, "k_closure_bound": U_E, "k_error_share_to_r": K_SPLIT,
        "k_r_bound_quantile": 1 - K_SPLIT * (1 - CONF) / 2,
        "false_alarm_target": target, "coverage_slack": slack, "step_cap": STEP_CAP,
        "monte_carlo_se_at_0.85": mc(0.85),
        "sandbaggers": {"strategies": STRATEGIES, "mean_withheld_share": HIDE_GRID,
                        "patterns": "uniform: every round alike; late: rising with the round; budget: rising with the budget; targeted: late rounds at large budgets; luck: a share t of what each round's luck added above its typical gain",
                        "banked": "no: withheld work is not added to the stock"},
        "round_cost": f"each round count is per budget; {nb} budgets make each round {nb} staged rounds",
        "scope": k_note,
    })
    res.detail("sweep_first_order", sweep)
    res.detail("empirical_noise", empirical)
    res.detail("first_order_level_fit_to_exact_law", first)
    res.detail("exact_likelihood_fit_to_exact_law", xml)
    res.detail("difference_form_interval", diff)
    res.detail("sandbaggers", sandbag)
    res.detail("bias", bias)
    res.detail("first_round_gain_needed_n5", {"by_sigma": need_d1, "cells": need})
    res.detail("trigger_curves_speedrun_calibrated", {
        "rounds_per_budget": rounds, "false_alarm_at_median": fa_main,
        "fires_at_95th_minus_at_median": gap_main, "false_alarm_at_median_favourable": fa_fav,
        "k_rule_false_alarm_at_median": kfa["cal"], "k_rule_false_alarm_at_median_favourable": kfa["fav"],
        "k_rule_fires_at_95th_minus_at_median": kgap["cal"],
        "k_rule_fires_at_95th_minus_at_median_favourable": kgap["fav"]})


CONF = 0.9  # replaced by claim-confidence in main(); used by part (a)'s intervals


def main() -> int:
    global CONF
    ids = ["claim-confidence", "claim-d2-rounds", "dyn-sie-lambda", "dyn-r-lm-corrected",
           "dyn-r-lm-hi-corrected", "dyn-r-lm-lo-corrected", "dyn-r-lm",
           "dyn-speedrun-first-annual", "dyn-speedrun-rate-2025", "dyn-speedrun-2026-annual",
           "dyn-speedrun-annual"]
    L = ledger(ids)
    CONF = L["claim-confidence"]
    res = Results("E4", "e04_loop_gain", seed=SEED)
    res.detail("ledger_inputs", L)
    gen = np.random.default_rng(SEED)
    cal = part_a(res, L, gen)
    if "--part-a" in sys.argv:  # a quick look at the history; writes nothing
        print(json.dumps({k: v["value"] for k, v in res.out["numbers"].items()}, indent=1))
        return 0
    part_c(res, L, cal, gen)
    path = res.write()
    text = path.read_text()
    if chr(0x2014) in text or "\\u2014" in text:
        raise SystemExit("the result contains an em dash; a source string leaked into it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
