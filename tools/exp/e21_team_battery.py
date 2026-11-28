#!/usr/bin/env python3
"""E21: the matched-budget team battery, public part. Where AI systems stand against human
comparisons at matched time, the crossover budget t*, and whether t* saturates.

C10 defines the crossover budget t* as the largest tested time budget at which the system's score
is at least the comparison's at equal compute and money, on a grid of budgets fixed in advance,
censored (never extrapolated) when the system still wins at the largest budget tested
(research/05-formal.md, Proposition 10.1). C10(c) claims that t* is estimable with an interval and
rises across model generations without saturating. This experiment estimates t* where public data
allow, says "not identified" where they do not, labels every human comparison for what it is, and
tests the saturation clause. The grid is GRID_H below, doubling from 7.5 minutes to 32 hours; each
battery can test only the part of it where its human data exist.

Four public batteries, each fetched at a pinned commit or from a named file:

(1) AI research, RE-Bench. METR's public run data for its time-horizon reports holds every human
expert's 8-hour attempt and every agent run on the RE-Bench environments, with METR's continuous
score (capped at 1, the mean score of the 7-to-9-hour human runs on that environment). In Time
Horizon 1.1 the agents also had an 8-hour limit per run (wall-clock with pauses runs longer on both
sides), so best-of-k on each side gives matched time and matched hardware (each run has the
environment's GPUs) at 8, 16 and 32 hours. The ratio
kappa(t) is the system's mean best-of-k score over the experts' (environments weighted equally, as
RE-Bench does); t* follows Proposition 10.1 on those three budgets. Humans' scores below 8 hours are
not in the data, so t* below 8 hours is censored low. The interval resamples environments and, within
each, runs on both sides (DRAWS draws, seeded). The comparison is the best of k independent single
experts, not a team. Money is not matched: an agent run costs a fraction of an expert's pay
(ledger cog-rebench-cost-ratio, 2024 prices), so a money match buys the agent more runs and can only
raise kappa; that variant is reported, censored at the runs observed. The cap matters: once an
agent reaches it everywhere, kappa sits at its ceiling, 1 over the experts' best of k, and the
battery cannot show it further ahead; how often the best model is there is reported. Time Horizon 1.0 (seven
environments, agents allowed 10 or 20 hours per run against the experts' 8) is a second suite whose
unequal allowance favours the agent. The RE-Bench paper's own curve (ledger cog-rebench-*) is the
reproduction check.

(2) Cyber, Cybench. Each of the 40 tasks has the first-solve time (FST) of the original contest: the
time from the contest's start to the first team's solve, so the comparison is the contest field's
fastest team on each task, a different team per task (an order statistic over contest teams, a
crowd), and the FST overstates a dedicated team's time. The human score at budget t is the share of
tasks with FST at most t; the agent's is its unguided solve share (Epoch's table of reported results),
its own wall-clock not counted (runs are bounded by iterations, not hours). Because both scores are
counts, t* depends only on the solve share and the FST distribution, not on which tasks were solved.
The interval resamples tasks and draws the solve count binomially, independently of each other,
which ignores that solved tasks are the short ones and so widens the interval. Trend: the rank
correlation of t* with release date, the doubling time of t* and a curvature term, each with a
resampling interval (the fits use models with t* inside the grid, which leaves out early models
below it and so lengthens the doubling time); and the ceiling that the pool's longest FST puts on t*.

(3) AI research, MLE-bench. The per-competition grading reports compare each agent run with the
Kaggle leaderboard's median, bronze and gold thresholds: contest entrants (teams or individuals) at
a stated rank, who had weeks or months (chan2024mlebench, section 3.4) against the agent's 12 to 36
hours, with tools of the competition's own date. A run that beats an entrant's final score shows
kappa(t) >= 1 for every t from the agent's budget to the competition's length, if both sides' scores
do not fall with time, so t* is censored above the grid's top (32 hours) on that competition for
agents allowed 32 hours or less; a loss identifies nothing. The share won against each rank, how much
the verdict moves when the comparison moves within its class (median to gold), and the trend across
entries are reported. One 100-hour run group was graded every hour, which shows the agent side's
returns to time.

(4) Strategy, forecasting. ForecastBench's tournament and baseline leaderboards against the
superforecaster median (an aggregate of a crowd of individuals), and Metaculus's Pro-against-bot
rounds (a team of professional forecasters, aggregated) tabulated by hand from the opened report
in tools/exp/data/e21_team_battery.csv. Neither varies the budget, so t* is not identified.

Serves C10: (c) directly, (b) on contest entrants (not organisations), and the labels C10's
statement requires. Selection: only published runs and reported scores (developers' own reports for
the newest Cybench and MLE-bench entries), contest teams and experts rather than organisations, and
benchmark pools fixed before the newest models; each is named where it bites.

  .venv/bin/python tools/exp/e21_team_battery.py      (CPU, about ten seconds after the first fetch)
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
from math import comb
from pathlib import Path

import numpy as np
import yaml
from scipy.stats import spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261121
DRAWS = 2000
# The budget grid of Proposition 10.1, fixed before any result was computed: doubling from 7.5 min.
GRID_H = (0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0)
T0 = date(2024, 1, 1)

METR_COMMIT = "52cb829c7a2efb2d659285c4b1768d191d97f8d2"
METR_RAW = f"https://raw.githubusercontent.com/METR/eval-analysis-public/{METR_COMMIT}"
TH11_URL = f"{METR_RAW}/reports/time-horizon-1-1/data/raw/runs.jsonl"
TH10_URL = f"{METR_RAW}/reports/time-horizon-1-0/data/raw/runs.jsonl"
DATES_URL = f"{METR_RAW}/data/external/release_dates.yaml"

CYBENCH_COMMIT = "ca483c6443f17a20ba7d6bac3d274859a1721e51"
CYBENCH_RAW = f"https://raw.githubusercontent.com/andyzorigin/cybench/{CYBENCH_COMMIT}"
FST_URL = f"{CYBENCH_RAW}/analytics/CTF%20fastest%20solve%20times.json"
TASKS_URL = f"{CYBENCH_RAW}/task_list.txt"
EPOCH_URL = "https://epoch.ai/data/benchmark_data.zip"

# The last commit whose run-group map is a valid file; the next one committed a merge conflict
# into it, so the one entry added after it (Famou-Agent 2.0 with Gemini 3 Pro) is left out.
MLE_COMMIT = "c5631ba61ceeb0573235a6ce209db435327a1e84"
MLE_TREE_URL = f"https://api.github.com/repos/openai/mle-bench/git/trees/{MLE_COMMIT}?recursive=1"
MLE_MEDIA = f"https://media.githubusercontent.com/media/openai/mle-bench/{MLE_COMMIT}"
MLE_RAW = f"https://raw.githubusercontent.com/openai/mle-bench/{MLE_COMMIT}"
# Not comparable with the leaderboard, by the leaderboard's own note: test-set feedback.
MLE_TEST_FEEDBACK = ("Disarray", "LoongFlow")
# The paper's resource and description ablations (sections 3.3 and 3.4), not leaderboard entries.
MLE_ABLATIONS = ("biggpu-gpt4o-aide", "cpu-gpt4o-aide", "extratime-gpt4o-aide", "obfuscation-gpt4o-aide")
MLE_DEFAULT_HOURS = 24  # the benchmark's standard runtime, used where an entry states none
MLE_HOURLY = (1, 2, 4, 8, 16, 24, 32, 64, 100)

FB_COMMIT = "5b415c0fb3dc7c5c24cba804c2f8bf3732bbacc9"
FB_RAW = f"https://raw.githubusercontent.com/forecastingresearch/forecastbench-datasets/{FB_COMMIT}"
FB_TOURNAMENT_URL = f"{FB_RAW}/leaderboards/csv/leaderboard_tournament.csv"
FB_BASELINE_URL = f"{FB_RAW}/leaderboards/csv/leaderboard_baseline.csv"
FB_PARITY_URL = f"{FB_RAW}/datasets/parity_dates/parity_dates.tournament_leaderboard.json"
FB_HUMAN_ROWS = ("Superforecaster median forecast", "Public median forecast")

HAND_TABLE = ROOT / "tools" / "exp" / "data" / "e21_team_battery.csv"
LEDGER_IDS = (
    "cog-rebench-run-hours", "cog-rebench-ai-over-human-2h", "cog-rebench-human-over-ai-32h",
    "cog-rebench-budget-short", "cog-rebench-budget-mid", "cog-rebench-budget-long",
    "cog-rebench-cost-ratio", "cog-cybench-hardest-hours", "cog-cybench-tasks",
    "cog-mlebench-competitions", "cog-forecast-super-index", "cog-forecast-top-index",
    "cog-metaculus-pro-lead", "cog-metaculus-questions", "cog-metaculus-p",
)


# ---------------------------------------------------------------- the crossover rule

def ratio(a: float, h: float) -> float:
    """kappa, the system's score over the comparison's. A comparison at zero is beaten by any
    positive score and tied by zero."""
    if h > 0:
        return a / h
    return math.inf if a > 0 else 1.0


def crossover(budgets, ratios) -> tuple[str, float]:
    """Proposition 10.1, the same rule as tools/formal/c10_crossover.py: the largest tested crossing,
    interpolated linearly in log kappa against log t; censored high when kappa >= 1 at the largest
    budget, censored low when kappa < 1 at every budget. A bracket whose left end is infinite or
    whose right end is zero cannot be interpolated in logs, so t* is its left end (the low choice)."""
    if ratios[-1] >= 1:
        return "above", budgets[-1]
    idx = [i for i in range(len(budgets) - 1) if ratios[i] >= 1 > ratios[i + 1]]
    if not idx:
        return "below", budgets[0]
    i = idx[-1]
    r0, r1 = ratios[i], ratios[i + 1]
    if not math.isfinite(r0) or r1 <= 0:
        return "found", budgets[i]
    x0, x1 = math.log(budgets[i]), math.log(budgets[i + 1])
    y0, y1 = math.log(r0), math.log(r1)
    return "found", math.exp(x0 + (0 - y0) * (x1 - x0) / (y1 - y0))


def encode(kind: str, value: float) -> float:
    """t* on one ordered axis: censored low as 0, censored high as infinity."""
    return 0.0 if kind == "below" else math.inf if kind == "above" else value


def decode(x: float, budgets) -> dict:
    if x == 0.0:
        return {"kind": "below", "bound_h": budgets[0]}
    if math.isinf(x):
        return {"kind": "above", "bound_h": budgets[-1]}
    return {"kind": "found", "t_star_h": round(x, 4)}


def ordinal_q(x: np.ndarray, q: float) -> float:
    """A percentile that is always an actual draw, so censored draws keep their meaning."""
    return float(np.quantile(x, q, method="inverted_cdf"))


def as_number(x: float, budgets) -> tuple[float, str]:
    """A ledger value and the words that say what it is."""
    if x == 0.0:
        return budgets[0], f"censored: below {budgets[0]:g} h, so an upper bound"
    if math.isinf(x):
        return budgets[-1], f"censored: above {budgets[-1]:g} h, so a lower bound"
    return x, "inside the tested budgets"


def years(d: str) -> float:
    return (date.fromisoformat(d[:10]).toordinal() - T0.toordinal()) / 365.25


def emax_weights(n: int, k: int) -> np.ndarray:
    """Weights on the sorted scores (ascending) giving the expected best of k runs drawn without
    replacement from n."""
    k = min(k, n)
    return np.array([comb(j, k - 1) for j in range(n)], float) / comb(n, k)


def spearman(x, y) -> float:
    if len(set(x)) < 2 or len(set(y)) < 2:
        return math.nan
    return float(spearmanr(x, y).statistic)


# ---------------------------------------------------------------- (1) RE-Bench

def rebench_load(path: Path) -> tuple[list, dict, dict, dict]:
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    rows = [r for r in rows if str(r.get("task_family", "")).startswith("ai_rd_")]
    envs = sorted({r["task_family"] for r in rows})
    scores: dict = {}
    limits: dict = {}
    for r in rows:
        scores.setdefault(r["alias"], {}).setdefault(r["task_family"], []).append(float(r["score_cont"] or 0.0))
        limits.setdefault(r["alias"], set()).add(r.get("time_limit"))
    scores = {a: {e: np.sort(np.array(v)) for e, v in d.items()} for a, d in scores.items()}
    human = scores.pop("human")
    if sorted(human) != envs:
        raise SystemExit(f"{path.name}: human runs do not cover every environment")
    if float(max(max(v) for d in scores.values() for v in d.values())) > 1 or max(max(v) for v in human.values()) > 1:
        raise SystemExit(f"{path.name}: a score above 1; METR's capped score changed meaning")
    return envs, human, scores, limits


def best_of(x: np.ndarray, k: int) -> float:
    return float(x @ emax_weights(len(x), k))


def rebench_suite(path, run_hours, cost_ratio, dates, gen, bootstrap: bool):
    envs, human, agents, limits = rebench_load(path)
    budgets = tuple(t for t in GRID_H if t >= run_hours and abs(t / run_hours - round(t / run_hours)) < 1e-9)
    ks = [int(round(t / run_hours)) for t in budgets]
    complete = sorted(a for a, d in agents.items() if all(e in d for e in envs))
    dropped = sorted(set(agents) - set(complete))
    hmean = [float(np.mean([best_of(human[e], k) for e in envs])) for k in ks]
    models = {}
    for a in complete:
        d = agents[a]
        lim = sorted(x for x in limits[a] if x is not None)
        allowance_h = [x / 3600 for x in lim]
        amean = [float(np.mean([best_of(d[e], k) for e in envs])) for k in ks]
        kap = [ratio(x, h) for x, h in zip(amean, hmean)]
        kind, t = crossover(budgets, kap)
        # Money match: copies bought with the experts' pay, as many runs as were observed at most.
        kmoney = [int(math.floor(k * cost_ratio)) for k in ks]
        amoney = [float(np.mean([best_of(d[e], km) for e in envs])) for km in kmoney]
        kap_m = [ratio(x, h) for x, h in zip(amoney, hmean)]
        kind_m, t_m = crossover(budgets, kap_m)
        if a not in dates:
            raise SystemExit(f"no release date for {a!r} in METR's release_dates.yaml")
        models[a] = {
            "release": dates[a],
            "runs_per_env": {e: int(len(d[e])) for e in envs},
            "allowance_h": allowance_h,
            "matched_time": bool(allowance_h) and all(abs(x - run_hours) < 1e-9 for x in allowance_h),
            "agent_best_of_k": [round(x, 4) for x in amean],
            "kappa": [round(x, 4) for x in kap],
            "t_star": decode(encode(kind, t), budgets),
            "censored_runs": any(k > len(d[e]) for k in ks for e in envs),
            # At the cap in every environment: the capped score cannot show this model further ahead.
            "at_cap_everywhere": [bool(all(best_of(d[e], k) >= 1 - 1e-9 for e in envs)) for k in ks],
            "money_match": {"agent_runs_per_human_run": int(math.floor(cost_ratio)),
                            "kappa": [round(x, 4) for x in kap_m],
                            "t_star": decode(encode(kind_m, t_m), budgets),
                            "note": "agent score censored at the best of its observed runs"},
        }
    out = {
        "environments": envs,
        "budgets_h": list(budgets),
        "human_runs_per_env": {e: int(len(human[e])) for e in envs},
        "human_best_of_k": [round(x, 4) for x in hmean],
        "kappa_ceiling": [round(1 / x, 4) for x in hmean],
        "models": models,
        "dropped_incomplete": dropped,
    }
    if not bootstrap:
        return out, None
    # Resample environments, then runs within each environment on both sides.
    nE = len(envs)
    env_idx = gen.integers(0, nE, (DRAWS, nE))
    rows_d = np.arange(DRAWS)[:, None]

    def side(scores_by_env):
        arr = np.empty((nE, DRAWS, len(ks)))
        for j, e in enumerate(envs):
            x = scores_by_env[e]
            s = np.sort(x[gen.integers(0, len(x), (DRAWS, len(x)))], axis=1)
            for c, k in enumerate(ks):
                arr[j, :, c] = s @ emax_weights(len(x), k)
        return arr[env_idx, rows_d, :].mean(axis=1)

    H = side(human)
    draws = {}
    for a in complete:
        A = side(agents[a])
        kap = A / H
        enc = np.array([encode(*crossover(budgets, list(kap[d]))) for d in range(DRAWS)])
        draws[a] = {"t": enc, "kappa": kap, "agent": A}
    return out, (draws, budgets)


def rebench_trend(models: dict, draws: dict, gen) -> dict:
    names = sorted(models)
    x = np.array([years(models[a]["release"]) for a in names])
    point = np.array([encode(models[a]["t_star"]["kind"], models[a]["t_star"].get("t_star_h", 0.0)) for a in names])
    rank_t = lambda v: np.where(np.isinf(v), 1e9, v)  # noqa: E731
    k8 = np.array([models[a]["kappa"][0] for a in names])
    rho_t = spearman(x, rank_t(point))
    rho_k = spearman(x, k8)
    boot_t, boot_k = [], []
    M = len(names)
    T = np.stack([draws[a]["t"] for a in names])  # (M, DRAWS)
    K = np.stack([draws[a]["kappa"][:, 0] for a in names])
    for d in range(DRAWS):
        pick = gen.integers(0, M, M)
        r = spearman(x[pick], rank_t(T[pick, d]))
        if not math.isnan(r):
            boot_t.append(r)
        r = spearman(x[pick], K[pick, d])
        if not math.isnan(r):
            boot_k.append(r)
    return {
        "rho_tstar": rho_t, "rho_tstar_lo": float(np.quantile(boot_t, 0.025)), "rho_tstar_hi": float(np.quantile(boot_t, 0.975)),
        "rho_kappa8": rho_k, "rho_kappa8_lo": float(np.quantile(boot_k, 0.025)), "rho_kappa8_hi": float(np.quantile(boot_k, 0.975)),
        "draws_kept": [len(boot_t), len(boot_k)],
    }


# ---------------------------------------------------------------- (2) Cybench

def fst_hours(s: str) -> float:
    h, m, sec = (int(p) for p in s.split(":"))
    return h + m / 60 + sec / 3600


def cybench(res, gen, led) -> dict:
    fst = json.loads(fetch(FST_URL, f"cybench/{CYBENCH_COMMIT[:7]}/fst.json", res,
                           what="Cybench first-solve times of the original contests").read_text())
    tasks = [t.strip().rstrip("/") for t in fetch(TASKS_URL, f"cybench/{CYBENCH_COMMIT[:7]}/task_list.txt", res,
                                                   what="Cybench's 40-task list").read_text().splitlines() if t.strip()]
    by_dir = {e["challenge_dir"].rstrip("/"): fst_hours(e["challenge_fastest_solve_time"]) for e in fst}
    missing = [t for t in tasks if t not in by_dir]
    if missing or len(tasks) != int(led["cog-cybench-tasks"]):
        raise SystemExit(f"Cybench task list changed: {len(tasks)} tasks, {len(missing)} without a solve time")
    hours = np.sort(np.array([by_dir[t] for t in tasks]))
    n = len(hours)

    zpath = fetch(EPOCH_URL, "epoch/benchmark_data.zip", res, what="Epoch AI benchmark data (Cybench table)")
    with zipfile.ZipFile(zpath) as z:
        table = list(csv.DictReader(io.StringIO(z.read("cybench_external.csv").decode("utf-8"))))
    rows = []
    for r in table:
        if not r["Unguided % Solved"] or not r["Release date"]:
            continue
        notes = r.get("Notes", "")
        model = r["Model version"]
        rows.append({
            "model": model,
            "base": model.split("_")[0],
            "share": float(r["Unguided % Solved"]),
            "release": r["Release date"][:10],
            "tasks": 37 if "37 problems" in notes else n,
            "flag_inflated": "inflated" in notes and any(t in model for t in ("o3-mini", "o1-mini")),
            "hardest_solved_min": float(r["Unguided most difficult task solved (minutes)"]) if r["Unguided most difficult task solved (minutes)"] else None,
            "source": r["Source"],
        })
    best: dict = {}
    for r in sorted(rows, key=lambda r: (r["base"], -r["share"], r["model"])):
        best.setdefault(r["base"], r)
    kept = [best[b] for b in sorted(best)]
    dropped = sorted(r["model"] for r in rows if best[r["base"]] is not r)

    H = [float((hours <= t).mean()) for t in GRID_H]
    models = {}
    for r in kept:
        kap = [ratio(r["share"], h) for h in H]
        kind, t = crossover(GRID_H, kap)
        # The crossing on the step function itself: just below the first solve time whose share of
        # tasks at or under it exceeds the agent's share.
        above = hours[np.arange(1, n + 1) / n > r["share"] + 1e-12]
        k = int(round(r["share"] * n))
        models[r["model"]] = dict(r, kappa=[round(x, 4) if math.isfinite(x) else "inf" for x in kap],
                                  t_star=decode(encode(kind, t), GRID_H),
                                  t_star_step_h=round(float(above[0]), 4) if above.size else None,
                                  fst_order_hardest_min=round(float(hours[k - 1] * 60), 2) if k >= 1 else None)

    # Interval: resample tasks; draw each model's solve count binomially, independently.
    names = sorted(models)
    idx = gen.integers(0, n, (DRAWS, n))
    Hd = np.stack([(hours[idx] <= t).mean(axis=1) for t in GRID_H], axis=1)  # (DRAWS, len(GRID_H))
    T = np.empty((len(names), DRAWS))
    for m, name in enumerate(names):
        r = models[name]
        p = gen.binomial(r["tasks"], r["share"], DRAWS) / r["tasks"]
        for d in range(DRAWS):
            T[m, d] = encode(*crossover(GRID_H, [ratio(p[d], h) for h in Hd[d]]))
        models[name]["t_star_lo"] = decode(ordinal_q(T[m], 0.025), GRID_H)
        models[name]["t_star_hi"] = decode(ordinal_q(T[m], 0.975), GRID_H)

    def trend(sel):
        x = np.array([years(models[a]["release"]) for a in sel])
        pt = np.array([encode(models[a]["t_star"]["kind"], models[a]["t_star"].get("t_star_h", 0.0)) for a in sel])
        rank_t = lambda v: np.where(np.isinf(v), 1e9, v)  # noqa: E731
        Ts = T[[names.index(a) for a in sel]]

        def fits(xx, tt):
            ok = (tt > 0) & np.isfinite(tt)
            if np.unique(xx[ok]).size < 4:
                return math.nan, math.nan
            y = np.log(tt[ok])
            xc = xx[ok] - xx[ok].mean()
            b = float(np.polyfit(xc, y, 1)[0])
            c = float(np.polyfit(xc, y, 2)[0])
            return b, c

        b0, c0 = fits(x, pt)
        rho0 = spearman(x, rank_t(pt))
        bs, cs, rhos = [], [], []
        M = len(sel)
        for d in range(DRAWS):
            pick = gen.integers(0, M, M)
            b, c = fits(x[pick], Ts[pick, d])
            if not math.isnan(b):
                bs.append(b)
                cs.append(c)
            r = spearman(x[pick], rank_t(Ts[pick, d]))
            if not math.isnan(r):
                rhos.append(r)
        bs, cs = np.array(bs), np.array(cs)
        dbl = lambda b: math.log(2) / b * 365.25 if b > 0 else None  # noqa: E731  (None: not rising)
        return {
            "models": M,
            "found_points": int(((pt > 0) & np.isfinite(pt)).sum()),
            "slope_ln_per_year": b0, "doubling_days": dbl(b0),
            "doubling_days_lo": dbl(float(np.quantile(bs, 0.975))), "doubling_days_hi": dbl(float(np.quantile(bs, 0.025))),
            "share_draws_slope_not_positive": float((bs <= 0).mean()),
            "curvature": c0, "curvature_lo": float(np.quantile(cs, 0.025)), "curvature_hi": float(np.quantile(cs, 0.975)),
            "rho": rho0, "rho_lo": float(np.quantile(rhos, 0.025)), "rho_hi": float(np.quantile(rhos, 0.975)),
            "draws_kept": [int(bs.size), len(rhos)],
        }

    all_trend = trend(names)
    clean = [a for a in names if not models[a]["flag_inflated"]]
    clean_trend = trend(clean)
    latest = max(names, key=lambda a: (models[a]["release"], models[a]["share"]))
    return {
        "fst_hours_sorted": [round(float(h), 4) for h in hours],
        "human_share_at_grid": dict(zip([f"{t:g}" for t in GRID_H], [round(h, 4) for h in H])),
        "models": models,
        "dropped_duplicates": dropped,
        "trend_all": all_trend,
        "trend_without_flagged": clean_trend,
        "latest": latest,
        "ceiling_h": float(hours[-1]),
        "second_longest_h": float(hours[-2]),
        "share_to_pass_second_longest": (n - 1) / n,
    }


# ---------------------------------------------------------------- (3) MLE-bench

def mle(res, gen, led) -> dict:
    tree = json.loads(fetch(MLE_TREE_URL, f"mlebench/{MLE_COMMIT[:7]}/tree.json", res,
                            what="MLE-bench file tree at the pinned commit").read_text())
    if tree.get("truncated"):
        raise SystemExit("MLE-bench tree listing truncated")
    paths = sorted(x["path"] for x in tree["tree"] if x["type"] == "blob"
                   and x["path"].startswith("runs/") and x["path"].endswith(".json"))
    mapping = list(csv.DictReader(io.StringIO(fetch(f"{MLE_MEDIA}/runs/run_group_experiments.csv",
                                                    f"mlebench/{MLE_COMMIT[:7]}/run_group_experiments.csv", res,
                                                    what="MLE-bench map from experiment to run groups").read_text())))
    split = [c.strip() for c in fetch(f"{MLE_RAW}/experiments/splits/split75.txt", f"mlebench/{MLE_COMMIT[:7]}/split75.txt",
                                      res, what="MLE-bench 75-competition split").read_text().splitlines() if c.strip()]
    if len(split) != int(led["cog-mlebench-competitions"]):
        raise SystemExit(f"split75 has {len(split)} competitions")
    board = fetch(f"{MLE_RAW}/README.md", f"mlebench/{MLE_COMMIT[:7]}/README.md", res,
                  what="MLE-bench README with the leaderboard").read_text()
    board_all = []
    for line in board.split("### Producing Scores")[0].splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 10 and "±" in cells[5]:
            board_all.append(float(cells[5].split("±")[0].strip()) / 100)
    readme = fetch(f"{MLE_RAW}/runs/README.md", f"mlebench/{MLE_COMMIT[:7]}/runs_README.md", res,
                   what="MLE-bench runs README (experiment notes)").read_text()
    hours_by_exp = {}
    for line in readme.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and not cells[0].startswith("-") and cells[0] != "**experiment_id**":
            m = re.search(r"(\d+)\s*hours", cells[1])
            hours_by_exp[cells[0].lower()] = int(m.group(1)) if m else MLE_DEFAULT_HOURS

    def report(path: str) -> list:
        p = fetch(f"{MLE_MEDIA}/{path}", f"mlebench/{MLE_COMMIT[:7]}/{path}", res,
                  what="MLE-bench grading report")
        try:
            return json.loads(p.read_text())["competition_reports"]
        except (json.JSONDecodeError, KeyError):
            raise SystemExit(f"{path} is not a grading report (a Git LFS pointer?)") from None

    groups: dict = {}
    for r in mapping:
        groups.setdefault(r["experiment_id"].strip(), []).append(r["run_group"].strip())
    hourly_curve = {}
    exps = {}
    for exp in sorted(groups):
        entries = []
        for g in sorted(groups[exp]):
            mine = [p for p in paths if p.startswith(f"runs/{g}/")]
            top = [p for p in mine if "/hourly/" not in p]
            hourly = [p for p in mine if "/hourly/" in p]
            if top:
                for p in top:
                    entries.append(report(p))
            elif hourly:
                last = max(hourly, key=lambda p: int(re.search(r"_(\d+)\.json$", p).group(1)))
                entries.append(report(last))
                for h in MLE_HOURLY:
                    cr = report(f"runs/{g}/hourly/grading_report_{h}.json")
                    k = len(cr)
                    hourly_curve[str(h)] = {
                        "competition_seed_entries": k,
                        "above_median": round(sum(bool(c["above_median"]) for c in cr) / k, 4),
                        "any_medal": round(sum(bool(c["any_medal"]) for c in cr) / k, 4),
                        "gold": round(sum(bool(c["gold_medal"]) for c in cr) / k, 4),
                        "group": g, "experiment": exp,
                    }
            else:
                raise SystemExit(f"run group {g} has no grading report")
        per = {c: [] for c in split}
        stamps = []
        for cr in entries:
            for c in cr:
                if c["competition_id"] in per:
                    per[c["competition_id"]].append((bool(c["above_median"]), bool(c["any_medal"]), bool(c["gold_medal"])))
                if c.get("created_at"):
                    stamps.append(c["created_at"][:10])
        # Per competition, the share of seeds that win; a competition with no run counts as lost.
        win = np.array([[np.mean([v[i] for v in per[c]]) if per[c] else 0.0 for i in range(3)] for c in split])
        exps[exp] = {
            "groups": len(groups[exp]),
            "reports": len(entries),
            "competitions_with_runs": int(sum(1 for c in split if per[c])),
            "date": sorted(stamps)[len(stamps) // 2] if stamps else None,
            "hours": hours_by_exp.get(exp.lower()),
            "share_above_median": round(float(win[:, 0].mean()), 4),
            "share_medal": round(float(win[:, 1].mean()), 4),
            "share_gold": round(float(win[:, 2].mean()), 4),
            "comparable": exp not in MLE_TEST_FEEDBACK and exp not in MLE_ABLATIONS,
            "_win": win,
        }
    comp = sorted(e for e in exps if exps[e]["comparable"])
    best = max(comp, key=lambda e: (exps[e]["share_medal"], e))
    first = max((e for e in comp if exps[e]["date"] and exps[e]["date"] < "2025-01-01"), key=lambda e: (exps[e]["share_medal"], e))
    W = exps[best]["_win"]
    pick = gen.integers(0, len(split), (DRAWS, len(split)))
    boot = W[pick].mean(axis=1)  # (DRAWS, 3)
    # The trend needs a date; reports without a grading timestamp (one entry) are left out of it.
    dated = [e for e in comp if exps[e]["date"]]
    x = [years(exps[e]["date"]) for e in dated]
    y = [exps[e]["share_medal"] for e in dated]
    rhos = []
    for _ in range(DRAWS):
        p = gen.integers(0, len(dated), len(dated))
        r = spearman([x[i] for i in p], [y[i] for i in p])
        if not math.isnan(r):
            rhos.append(r)
    for e in exps.values():
        e.pop("_win")
    # Reproduction: each entry's medal share against the nearest "All (%)" on the published board.
    near = {e: min(abs(exps[e]["share_medal"] - v) for v in board_all) for e in comp} if board_all else {}
    return {
        "board_reproduction": {"board_rows": len(board_all),
                               "entries_within_half_point": sum(1 for v in near.values() if v <= 0.005),
                               "entries": len(near),
                               "largest_gap": max(near.values()) if near else None,
                               "note": "matched by value, not name; the board pads incomplete seeds with failures, as here"},
        "experiments": exps,
        "comparable": comp,
        "best": best,
        "best_2024": first,
        "best_boot": {"above_median": [float(np.quantile(boot[:, 0], q)) for q in (0.025, 0.975)],
                      "medal": [float(np.quantile(boot[:, 1], q)) for q in (0.025, 0.975)],
                      "gold": [float(np.quantile(boot[:, 2], q)) for q in (0.025, 0.975)]},
        "undated": sorted(set(comp) - set(dated)),
        "rho_date_medal": spearman(x, y),
        "rho_date_medal_lo": float(np.quantile(rhos, 0.025)),
        "rho_date_medal_hi": float(np.quantile(rhos, 0.975)),
        "hourly_extratime": hourly_curve,
    }


# ---------------------------------------------------------------- (4) forecasting

def interval(s: str) -> list[float]:
    a, b = (float(v) for v in s.strip("[] ").split(","))
    return [a, b]


def forecasting(res, led) -> dict:
    out = {}
    for name, url in (("tournament", FB_TOURNAMENT_URL), ("baseline", FB_BASELINE_URL)):
        rows = list(csv.DictReader(io.StringIO(fetch(url, f"forecastbench/{FB_COMMIT[:7]}/leaderboard_{name}.csv", res,
                                                     what=f"ForecastBench {name} leaderboard").read_text())))
        sup = [r for r in rows if r["Model"] == FB_HUMAN_ROWS[0]]
        if len(sup) != 1:
            raise SystemExit(f"ForecastBench {name}: no single superforecaster row")
        sup = sup[0]
        ai = [r for r in rows if r["Model"] not in FB_HUMAN_ROWS]
        top = max(ai, key=lambda r: (float(r["Overall"]), r["Model"]))
        s = float(sup["Overall"])
        out[name] = {
            "superforecaster_median": s, "superforecaster_ci": interval(sup["Overall 95% CI"]),
            "top_entry": {"team": top["Team"], "model": top["Model"], "overall": float(top["Overall"]),
                          "ci": interval(top["Overall 95% CI"]), "p_supers_better": top["p-val Supers > Forecaster?"]},
            "top_margin": float(top["Overall"]) - s,
            "entries": len(ai),
            "entries_at_or_above_supers": sum(1 for r in ai if float(r["Overall"]) >= s),
        }
    parity = json.loads(fetch(FB_PARITY_URL, f"forecastbench/{FB_COMMIT[:7]}/parity_dates.json", res,
                              what="ForecastBench projected parity dates").read_text())
    out["parity_dates_published"] = parity
    with HAND_TABLE.open(newline="") as f:
        rounds = [r for r in csv.DictReader(f) if r["case_id"].startswith("metaculus-")]
    meta = []
    for r in rounds:
        v, lo, hi = float(r["value"]), float(r["ci_low"]), float(r["ci_high"])
        meta.append({"round": r["round"], "bot_team_score": v, "ci": [lo, hi],
                     "decided": "pros ahead" if hi < 0 else "bots ahead" if lo > 0 else "not decided",
                     "comparison_kind": r["comparison_kind"], "source": r["source"], "where": r["where"]})
    spring = [r for r in rounds if r["case_id"] == "metaculus-2026spring"][0]
    out["metaculus"] = meta
    out["metaculus_time"] = {"pros_days": float(spring["human_time_days"]), "bots_h": float(spring["ai_time_h"]),
                             "pros_over_bots": float(spring["human_time_days"]) * 24 / float(spring["ai_time_h"])}
    out["reproduction"] = {
        "supers_index": [out["tournament"]["superforecaster_median"], led["cog-forecast-super-index"]],
        "top_index": [out["tournament"]["top_entry"]["overall"], led["cog-forecast-top-index"]],
        "metaculus_lead": [-float(spring["value"]), led["cog-metaculus-pro-lead"]],
        "metaculus_questions": [float(spring["n_questions"]), led["cog-metaculus-questions"]],
        "metaculus_p": [float(spring["p_one_sided"]), led["cog-metaculus-p"]],
    }
    out["reproduction"]["all_match"] = all(abs(a - b) < 1e-9 for a, b in out["reproduction"].values())
    return out


# ---------------------------------------------------------------- main

def main() -> int:
    res = Results("E21", "e21_team_battery", seed=SEED)
    gen = np.random.default_rng(SEED)
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    led = {i: numbers[i]["value"] for i in LEDGER_IDS}
    res.detail("ledger_inputs", led)
    run_hours = float(led["cog-rebench-run-hours"])

    dates_raw = yaml.safe_load(fetch(DATES_URL, f"metr/{METR_COMMIT[:7]}/release_dates.yaml", res,
                                     what="METR model release dates").read_text())["date"]
    dates = {k: (v.isoformat() if isinstance(v, date) else str(v)) for k, v in dates_raw.items()}

    # (1) RE-Bench, Time Horizon 1.1: matched 8-hour runs.
    th11 = fetch(TH11_URL, f"metr/{METR_COMMIT[:7]}/th11_runs.jsonl", res, what="METR Time Horizon 1.1 runs")
    rb, (rb_draws, rb_budgets) = rebench_suite(th11, run_hours, led["cog-rebench-cost-ratio"], dates, gen, True)
    for a, m in rb["models"].items():
        m["t_star_lo"] = decode(ordinal_q(rb_draws[a]["t"], 0.025), rb_budgets)
        m["t_star_hi"] = decode(ordinal_q(rb_draws[a]["t"], 0.975), rb_budgets)
        m["kappa8_interval"] = [round(float(np.quantile(rb_draws[a]["kappa"][:, 0], q)), 4) for q in (0.025, 0.975)]
    matched = {a: m for a, m in rb["models"].items() if m["matched_time"]}
    rb_trend = rebench_trend(matched, {a: rb_draws[a] for a in matched}, gen)
    # Time Horizon 1.0: agents allowed 10 or 20 hours per run against 8, point estimates only.
    th10 = fetch(TH10_URL, f"metr/{METR_COMMIT[:7]}/th10_runs.jsonl", res, what="METR Time Horizon 1.0 runs")
    rb10, _ = rebench_suite(th10, run_hours, led["cog-rebench-cost-ratio"], dates, gen, False)

    def tkey(m):
        t = m["t_star"]
        return (encode(t["kind"], t.get("t_star_h", 0.0)), m["kappa"][0])

    rb_best = max(sorted(matched), key=lambda a: tkey(matched[a]))
    bm = matched[rb_best]
    best_t = encode(bm["t_star"]["kind"], bm["t_star"].get("t_star_h", 0.0))
    paper_k2 = led["cog-rebench-ai-over-human-2h"]
    paper_k32 = 1 / led["cog-rebench-human-over-ai-32h"]
    early_all = {a: m for a, m in rb["models"].items() if m["release"] < "2025-01-01"}
    reproduction = {
        "paper": {"kappa_2h": paper_k2, "kappa_32h": paper_k32,
                  "t_star_bracket_h": [led["cog-rebench-budget-short"], led["cog-rebench-budget-mid"]],
                  "note": "the paper puts humans narrowly ahead at 8 h, so its largest crossing lies in this bracket"},
        "here_2024_models": {a: {"t_star": m["t_star"], "kappa_32h": m["kappa"][-1]} for a, m in sorted(early_all.items())},
        "consistent_below_8h": all(m["t_star"]["kind"] == "below" for m in early_all.values()),
        "max_kappa_32h_2024": max(m["kappa"][-1] for m in early_all.values()),
    }
    sat = {
        "kappa_ceiling_by_budget": dict(zip([f"{t:g}" for t in rb_budgets], rb["kappa_ceiling"])),
        "models_censored_above": sorted(a for a, m in matched.items() if m["t_star"]["kind"] == "above"),
        "models_found": sorted(a for a, m in matched.items() if m["t_star"]["kind"] == "found"),
        "models_below": sorted(a for a, m in matched.items() if m["t_star"]["kind"] == "below"),
    }
    capped = bm["t_star"]["kind"] == "above" and bm["at_cap_everywhere"][-1]
    sat["verdict"] = (
        f"saturated: {rb_best} is censored above the largest budget the public data can test and sits at the "
        f"score's cap in every environment there, where an agent can lead by at most {rb['kappa_ceiling'][-1]:.3f}; "
        "the battery cannot show t* rising further" if capped else
        "censored above the largest budget, not at the cap" if bm["t_star"]["kind"] == "above" else
        "not censored at the largest tested budget")
    res.detail("rebench_th11", rb)
    res.detail("rebench_th11_trend", rb_trend)
    res.detail("rebench_th10_unequal_allowance", rb10)
    res.detail("rebench_reproduction", reproduction)

    # (2) Cybench.
    cy = cybench(res, gen, led)
    res.detail("cybench", cy)

    # (3) MLE-bench.
    ml = mle(res, gen, led)
    res.detail("mlebench", ml)

    # (4) Forecasting.
    fc = forecasting(res, led)
    res.detail("forecasting", fc)

    # Which clusters give t* with an interval: a model whose t* is inside the grid or censored above,
    # with the interval's lower end not censored below.
    def identified(models, lo_key="t_star_lo"):
        return [a for a, m in models.items() if m["t_star"]["kind"] in ("found", "above") and m[lo_key]["kind"] != "below"]

    def two_sided(models):
        return [a for a, m in models.items() if m["t_star_lo"]["kind"] == "found" and m["t_star_hi"]["kind"] == "found"]

    ident = {"AI research (RE-Bench)": identified(matched), "cyber (Cybench)": identified(cy["models"]),
             "AI research (MLE-bench)": [], "strategy (forecasting)": []}
    ident2 = {"AI research (RE-Bench)": two_sided(matched), "cyber (Cybench)": two_sided(cy["models"]),
              "AI research (MLE-bench)": [], "strategy (forecasting)": []}
    res.detail("tstar_identified_by_battery", {"one_sided_allowed": ident, "two_sided_inside_grid": ident2})
    # The best RE-Bench model at the cap: how often the 32-hour comparison is a tie at the cap, and how
    # often the agent sits at the cap in every resampled environment.
    kd = rb_draws[rb_best]
    cap_diag = {
        "share_draws_tie_32h": float((np.abs(kd["kappa"][:, -1] - 1) < 1e-12).mean()),
        "share_draws_agent_at_cap": [float((kd["agent"][:, c] >= 1 - 1e-9).mean()) for c in range(len(rb_budgets))],
        "budgets_h": list(rb_budgets),
    }
    sat["best_model_cap"] = cap_diag
    res.detail("rebench_th11_saturation", sat)
    res.detail("caveats", [
        "No battery here compares with an organisation: experts, contest entrants, contest crowds and forecaster teams.",
        "RE-Bench: four to eight agent runs per environment; METR's own elicitation; experts had AI tools (kwa2025horizon, C.1.2), which raises their scores.",
        "RE-Bench: the capped score ties the sides at the cap; at 16 and 32 hours the best model is at the ceiling.",
        "Cybench: newest scores are developers' own reports, some on a 37-task subset; first-solve times count from the contest start.",
        "MLE-bench: entries are self-submitted; old Kaggle solutions are public and may be in training data; test splits are rebuilt from training data, so the board comparison is approximate (chan2024mlebench).",
        "MLE-bench: the run-group map after the pinned commit is a merge conflict, so the newest entry (Famou-Agent 2.0 with Gemini 3 Pro) is left out.",
        "Forecasting: the budget is not varied; the superforecaster median is a crowd aggregate, the Metaculus Pros a team of ten in spring 2026.",
    ])
    res.detail("baselines", [
        {"cluster": "AI research", "battery": "RE-Bench (METR runs, Time Horizon 1.1)",
         "comparison": "best of k independent single experts, each with 8 hours", "kind": "single expert",
         "matched": "wall-clock time and hardware per run; money not matched (agents cheaper)",
         "source": "metr2026evalanalysis; wijk2024rebench"},
        {"cluster": "AI research", "battery": "MLE-bench grading reports",
         "comparison": "Kaggle entrant at the median, bronze or gold threshold of the final private leaderboard",
         "kind": "contest team or individual entrant", "matched": "nothing: entrants had weeks or months, agents 12 to 36 hours",
         "source": "openai2026mlebenchruns; chan2024mlebench"},
        {"cluster": "cyber", "battery": "Cybench",
         "comparison": "the contest field's fastest team on each task, a different team per task",
         "kind": "crowd of contest teams (order statistic)", "matched": "wall-clock time from the contest start; agent time uncounted",
         "source": "cybench2024repo; zhang2024cybench; epoch2026hub"},
        {"cluster": "strategy", "battery": "ForecastBench",
         "comparison": "median of the superforecasters' forecasts", "kind": "crowd of individuals (aggregate)",
         "matched": "the same questions; budget not stated", "source": "forecastbench2026datasets"},
        {"cluster": "strategy", "battery": "Metaculus FutureEval",
         "comparison": "a team of professional forecasters, aggregated", "kind": "team (aggregated forecasts)",
         "matched": "the same questions; Pros had 3 days, bots 1.5 hours", "source": "metaculus2026futureeval"},
    ])

    # ------------------------------------------------------------ numbers
    n = res.number
    n("e21-clusters", 3, unit="clusters", fmt=",.0f",
      label="decisive clusters with a public human comparison examined here (AI research, cyber, strategy)")
    n("e21-clusters-tstar", sum(1 for k in ("AI research", "cyber", "strategy")
                                if any(v for b, v in ident.items() if b.startswith(k))), unit="clusters", fmt=",.0f",
      label="of those, clusters where t* has an interval for at least one model, censored above allowed (its lower end not censored below the grid)")
    n("e21-clusters-tstar-two-sided", sum(1 for k in ("AI research", "cyber", "strategy")
                                          if any(v for b, v in ident2.items() if b.startswith(k))), unit="clusters", fmt=",.0f",
      label="of those, clusters where some model's t* interval lies wholly inside the tested budgets (neither end censored)")

    n("e21-rebench-models", len(matched), unit="models", fmt=",.0f",
      label="models with matched 8-hour runs on every RE-Bench environment in METR's Time Horizon 1.1 data")
    n("e21-rebench-cross-8h", sum(1 for m in matched.values() if m["kappa"][0] >= 1), unit="models", fmt=",.0f",
      label="of those, models whose mean best score at 8 hours is at least the experts' (kappa(8 h) >= 1, point estimates)")
    v, what = as_number(best_t, rb_budgets)
    n("e21-rebench-tstar-best", v, unit="h", fmt=".1f",
      label=f"largest crossover budget t* of any model on RE-Bench at matched time ({rb_best}, released {bm['release']}; {what})",
      note="capped score: 1 is the mean 8-hour expert result on the environment")
    lo = ordinal_q(rb_draws[rb_best]["t"], 0.025)
    v, what = as_number(lo, rb_budgets)
    n("e21-rebench-tstar-best-lo", v, unit="h", fmt=".1f",
      label=f"that model's t*, 2.5th percentile of resampling environments and runs ({what})")
    n("e21-rebench-kappa8-best", bm["kappa"][0], fmt=".2f",
      label=f"that model's score over the experts' at 8 hours, mean best of one run each side ({rb_best})")
    n("e21-rebench-kappa8-best-lo", bm["kappa8_interval"][0], fmt=".2f",
      label="that ratio, 2.5th percentile of resampling environments and runs")
    n("e21-rebench-kappa8-best-hi", bm["kappa8_interval"][1], fmt=".2f",
      label="that ratio, 97.5th percentile of resampling environments and runs")
    n("e21-rebench-kappa32-best", bm["kappa"][-1], fmt=".3f",
      label=f"that model's score over the experts' at 32 hours (best of four runs each side, {rb_best})")
    n("e21-rebench-cap-32h", sat["best_model_cap"]["share_draws_agent_at_cap"][-1], fmt=".1%",
      label=f"share of resampling draws in which {rb_best} is at the score's cap in every environment at 32 hours")
    n("e21-rebench-ceiling-32h", rb["kappa_ceiling"][-1], fmt=".3f",
      label="the largest ratio any agent can reach at 32 hours on METR's capped score (1 over the experts' best of four)",
      note="at the ceiling a win is a tie at the cap; the battery cannot show t* rising further")
    n("e21-rebench-rho", rb_trend["rho_tstar"], fmt=".2f",
      label="rank correlation of t* (censored values ranked at their ends) with release date across those models")
    n("e21-rebench-rho-lo", rb_trend["rho_tstar_lo"], fmt=".2f",
      label="that correlation, 2.5th percentile of resampling models, environments and runs")
    n("e21-rebench-rho-hi", rb_trend["rho_tstar_hi"], fmt=".2f",
      label="that correlation, 97.5th percentile of resampling models, environments and runs")
    n("e21-rebench-below-8h", len(sat["models_below"]), unit="models", fmt=",.0f",
      label="models whose t* is censored below 8 hours, the smallest budget with expert data")

    lat = cy["models"][cy["latest"]]
    lt = encode(lat["t_star"]["kind"], lat["t_star"].get("t_star_h", 0.0))
    n("e21-cyber-models", len(cy["models"]), unit="models", fmt=",.0f",
      label="models with a reported unguided Cybench score and release date (best report per model)")
    v, what = as_number(lt, GRID_H)
    n("e21-cyber-tstar-latest", v, unit="h", fmt=".1f",
      label=f"t* of the latest model on Cybench against the contest field's fastest team ({cy['latest']}, {lat['release']}; {what})",
      note="developer-reported score; first-solve times overstate a dedicated team's time, which raises t*")
    for key, q in (("lo", lat["t_star_lo"]), ("hi", lat["t_star_hi"])):
        x = 0.0 if q["kind"] == "below" else math.inf if q["kind"] == "above" else q["t_star_h"]
        v, what = as_number(x, GRID_H)
        n(f"e21-cyber-tstar-latest-{key}", v, unit="h", fmt=".1f",
          label=f"that t*, {'2.5th' if key == 'lo' else '97.5th'} percentile of resampling tasks and solve counts ({what})")
    tr = cy["trend_all"]
    n("e21-cyber-doubling-days", tr["doubling_days"], unit="days", fmt=",.0f",
      label="doubling time of t* on Cybench across release dates (models with t* inside the grid; least squares on ln t*)")
    n("e21-cyber-doubling-days-lo", tr["doubling_days_lo"], unit="days", fmt=",.0f",
      label="that doubling time, 2.5th percentile of resampling models, tasks and solve counts")
    n("e21-cyber-doubling-days-hi", tr["doubling_days_hi"], unit="days", fmt=",.0f",
      label="that doubling time, 97.5th percentile of resampling models, tasks and solve counts")
    n("e21-cyber-curvature", tr["curvature"], unit="per year squared", fmt=".2f",
      label="curvature of ln t* against release date (negative would mean slowing)")
    n("e21-cyber-curvature-lo", tr["curvature_lo"], unit="per year squared", fmt=".2f",
      label="that curvature, 2.5th percentile of resampling")
    n("e21-cyber-curvature-hi", tr["curvature_hi"], unit="per year squared", fmt=".2f",
      label="that curvature, 97.5th percentile of resampling")
    n("e21-cyber-rho", tr["rho"], fmt=".2f", label="rank correlation of Cybench t* with release date")
    n("e21-cyber-rho-lo", tr["rho_lo"], fmt=".2f", label="that correlation, 2.5th percentile of resampling models, tasks and solve counts")
    n("e21-cyber-rho-hi", tr["rho_hi"], fmt=".2f", label="that correlation, 97.5th percentile of resampling models, tasks and solve counts")
    n("e21-cyber-ceiling-h", cy["ceiling_h"], unit="h", fmt=".1f",
      label="the longest first-solve time in Cybench, above which t* on this pool cannot be measured",
      note="the latest share leaves one step before t* is pinned between the two longest solve times")

    exps = ml["experiments"]
    b = exps[ml["best"]]
    n("e21-mle-entries", len(ml["comparable"]), unit="entries", fmt=",.0f",
      label="MLE-bench leaderboard entries with grading reports at the pinned commit (test-set-feedback entries and ablations left out)")
    n("e21-mle-median-best", b["share_above_median"], fmt=".1%",
      label=f"share of the 75 competitions in which the best entry beats the median Kaggle entrant ({ml['best']}, best by medal share, so biased up)")
    n("e21-mle-medal-best", b["share_medal"], fmt=".1%",
      label="its share beating the bronze-medal threshold entrant, a contest entrant at that rank")
    n("e21-mle-medal-best-lo", ml["best_boot"]["medal"][0], fmt=".1%",
      label="that share, 2.5th percentile of resampling competitions")
    n("e21-mle-medal-best-hi", ml["best_boot"]["medal"][1], fmt=".1%",
      label="that share, 97.5th percentile of resampling competitions")
    n("e21-mle-gold-best", b["share_gold"], fmt=".1%", label="its share beating the gold-medal threshold entrant")
    n("e21-mle-flip-best", b["share_above_median"] - b["share_gold"], fmt=".1%",
      label="share of competitions whose verdict flips when the comparison moves from the median entrant to the gold-threshold entrant")
    n("e21-mle-medal-2024", exps[ml["best_2024"]]["share_medal"], fmt=".1%",
      label=f"share beating the bronze-threshold entrant for the best 2024 entry ({ml['best_2024']})")
    n("e21-mle-rho", ml["rho_date_medal"], fmt=".2f",
      label="rank correlation of the medal share with the entry's grading date across leaderboard entries")

    t, bl = fc["tournament"], fc["baseline"]
    n("e21-fb-top-margin", t["top_margin"], unit="points", fmt=".1f",
      label="top ForecastBench tournament entry minus the superforecaster median, Brier Index (intervals overlap)")
    n("e21-fb-above", t["entries_at_or_above_supers"], unit="entries", fmt=",.0f",
      label="ForecastBench tournament AI entries at or above the superforecaster median")
    n("e21-fb-entries", t["entries"], unit="entries", fmt=",.0f", label="ForecastBench tournament AI entries")
    n("e21-fb-llm-margin", bl["top_margin"], unit="points", fmt=".1f",
      label="best single model run by ForecastBench itself minus the superforecaster median on its baseline board")
    n("e21-meta-decided", sum(1 for r in fc["metaculus"] if r["decided"] != "not decided"), unit="rounds", fmt=",.0f",
      label="Metaculus Pro-against-bot rounds whose 95% interval excludes parity (all in the Pros' favour)")
    n("e21-meta-rounds", len(fc["metaculus"]), unit="rounds", fmt=",.0f", label="Metaculus Pro-against-bot rounds reported")

    crossers = sorted((m["release"], a) for a, m in matched.items() if m["t_star"]["kind"] != "below")
    first_cross = crossers[0][1] if crossers else None
    late_below = sorted(a for a, m in matched.items()
                        if crossers and m["t_star"]["kind"] == "below" and m["release"] > crossers[0][0])
    res.detail("verdict_c10", {
        "c_estimable": (
            f"RE-Bench at matched time: t* is censored below 8 h for {len(sat['models_below'])} of {len(matched)} models, "
            f"inside 8 to 32 h for {len(sat['models_found'])} (each interval runs from below 8 h to above 32 h, four to "
            f"eight runs per environment), and censored above 32 h for {len(sat['models_censored_above'])}. Cybench: t* "
            f"lies inside the grid for {cy['trend_all']['found_points']} of {len(cy['models'])} models, "
            f"{len(ident2['cyber (Cybench)'])} of them with an interval wholly inside it."),
        "c_rises": (
            f"yes on both: rank correlation with release date {rb_trend['rho_tstar']:.2f} "
            f"({rb_trend['rho_tstar_lo']:.2f} to {rb_trend['rho_tstar_hi']:.2f}) on RE-Bench and "
            f"{tr['rho']:.2f} ({tr['rho_lo']:.2f} to {tr['rho_hi']:.2f}) on Cybench, where t* doubles every "
            f"{tr['doubling_days']:.0f} days ({tr['doubling_days_lo']:.0f} to {tr['doubling_days_hi']:.0f}). "
            + (f"Not monotone by model on RE-Bench: {', '.join(late_below)} came after the first crossing "
               f"({first_cross}) and sit below 8 h." if late_below else "Monotone by model on RE-Bench.")),
        "c_saturates": (
            f"{sat['verdict']}. On Cybench the curvature of ln t* is {tr['curvature']:.2f} per year squared "
            f"({tr['curvature_lo']:.2f} to {tr['curvature_hi']:.2f}): no sign of slowing yet, but the pool's longest "
            f"solve time ({cy['ceiling_h']:.1f} h) caps what can be measured. On a fixed pool t* saturates with the "
            f"pool, so 'rises without saturating' is not a property t* has; it holds only while the battery's human "
            f"baselines reach beyond the systems tested."),
        "b": (
            f"on MLE-bench, against contest entrants, not organisations, the best entry's verdict flips on "
            f"{b['share_above_median'] - b['share_gold']:.0%} of competitions when the comparison moves from the "
            f"median entrant to the gold-threshold entrant: the verdict is not stable within the class unless the "
            f"rank is named. The share won rises with the entry's date (rank correlation {ml['rho_date_medal']:.2f})."),
        "forecasting": "t* not identified: neither ForecastBench nor Metaculus varies the budget.",
        "mlebench_tstar": ("not identified, except as a lower bound: where an entry allowed 32 h or less beats an "
                           "entrant's final score, t* lies above the grid's top on that competition, if neither "
                           "side's score falls with time; a loss identifies nothing."),
    })
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
