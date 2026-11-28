#!/usr/bin/env python3
"""E18: the cap leak, C2's fixed-compute case, over the ledger's ranges and backtested on the
open-closed record.

What it measures. A party held at a training-compute cap reaches the agreed effective compute C*
when algorithmic drift closes the headroom h left after its one-off jumps. The formal file's
Corollary 2.3 gives the leak time t = max(0, (h - J - S_v) / log10 gamma), with physical compute fixed
at the cap, drift at a constant log10 gamma a year, J the post-training jump and S_v the inference
span, both in OOM. This experiment (1) evaluates that expression over a grid of headrooms on the
ranges the ledger gives, and the headroom a cap needs for its leak time to exceed m * T_r; (2) asks
C2(b) in its fixed-compute form: at which headrooms the expression's interval and a single
multiplier's interval (h / log10 gamma, no jumps, the memo's form) do not overlap; (3) backtests the
expression on Epoch's open-closed data (C2(c)).

Data. (a) The ledger, read by id from data/numbers.json (the ids are recorded in the result). (b)
E1's six samples of the drift rate, read from E1's result file and checked against the ledger's two
ends. (c) Epoch's chart data for "Open models lag state-of-the-art closed models by 4 months"
[@edwards2026openclosed]: each model's ECI with its interval, release date, accessibility and
training compute. (d) The figures that insight publishes (its window, the strict lag, the ECI gap),
compiled by hand in tools/exp/data/e18_cap_leak.csv.

Method. E10 has not run, so J and S_v take Part I's ranges, one jump at a time as Part I does: a class
without a cheap verifier (J from the typical to the high post-training jump, S_v = 0) and a class with
one (J = 0, S_v from one technique's typical saving to the cheap-verifier span). The drift rate is not
identified (E1), so no single rate is used: each named range is evaluated on its own (Part I's
bracket, Ho et al.'s interval, the Rosetta families, E1's full sample, E1's six samples, and the rates
the backtest implies). At fixed compute every input but C* raises the left side, so assumption (A2.1)
holds and Theorem 2.1 makes the interval exact at two corners; those corners are the result. A Monte
Carlo inside each box is an illustration only, run under three different laws for the rate to show
that its median is set by the law, not by data; the run stops if any draw leaves the corners.

The backtest follows Part I's design: set a hypothetical cap at the compute of a then-frontier model
(each ECI record holder with a compute estimate, after the first date a closed model has an ECI),
and find when a model with compute at or below the cap first matched that record's ECI. At that cap
the expression predicts zero for every input. The cap is then lowered by h OOM below the record's
compute and the first match found again, which gives the leak time against headroom on real data with
no conversion from ECI to compute: each first match implies a rate 10^(h / t). J is set to zero there,
since the record is itself post-trained and gains beyond it were not known at its release; Part I's J
range is a sensitivity. Epoch's day-by-day lag is reproduced from the same file with point estimates
(the strict version, which Epoch puts at six months; its four-month headline needs paired bootstrap
samples it does not publish). Selection: only models with a public compute estimate can be placed
under a cap, and most frontier models since 2024 have none, so first matches are late or censored
(biasing leak times up); open models may score higher on public benchmarks than on private ones, as
Epoch notes (biasing them down).

Serves C2 ((b) and (c); (a) is cut) and C1 through m * T_r.

  .venv/bin/python tools/exp/e18_cap_leak.py      (CPU, seconds; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import json
import math
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

URL = "https://epoch.ai/data/charts/open-closed-eci-gap/benchmarked_models.csv"
TABLE = ROOT / "tools" / "exp" / "data" / "e18_cap_leak.csv"
E1_RESULT = ROOT / "data" / "results" / "e01_capability_compute.json"
SEED = 20261127
DRAWS = 20_000
H_GRID = [round(0.25 * i, 2) for i in range(25)]  # headroom, 0 to 6 OOM
H_BACKTEST = [round(0.25 * i, 2) for i in range(11)]  # caps lowered 0 to 2.5 OOM below the record
FINE = 1e-4  # grid step for the numerical check of the separation boundary
YEAR = 365.25
MONTH = YEAR / 12

LEDGER_IDS = {
    "headroom": "comp-example-headroom-oom",
    "j_lo": "comp-oneoff-lo-oom",
    "j_hi": "comp-oneoff-hi-oom",
    "sv_lo": "comp-tradeoff-typical-oom",
    "sv_hi": "comp-span-cheapver-train",
    "g_small": "comp-gundlach-small-annual-max",
    "g_ho": "comp-ho-annual",
    "g_ho_lo": "comp-ho-annual-lo",
    "g_ho_hi": "comp-ho-annual-hi",
    "g_ros": "comp-rosetta-algo",
    "g_ros_lo": "comp-rosetta-algo-lo",
    "g_ros_hi": "comp-rosetta-algo-hi",
    "e1": "e1-algo-annual",
    "e1_lo": "e1-algo-annual-lo",
    "e1_hi": "e1-algo-annual-hi",
    "e1_sub_min": "e1-algo-annual-subset-min",
    "e1_sub_max": "e1-algo-annual-subset-max",
    "e1_1e24": "e1-algo-annual-1e24",
    "e1_1e24_lo": "e1-algo-annual-1e24-lo",
    "e1_1e24_hi": "e1-algo-annual-1e24-hi",
    "e1_1e26": "e1-algo-annual-1e26",
    "e1_1e26_lo": "e1-algo-annual-1e26-lo",
    "e1_1e26_hi": "e1-algo-annual-1e26-hi",
    "m": "prot-margin",
    "tr": "prot-tr-declared",
    "line": "prot-line-declared",
    "tr_part1": "comp-response-years",
    "td_declared_days": "e5-td-declared-days",
    "tresp_km": "e24-halt-km-median-years",
    "never_halted": "e24-halt-share-never",
    "oc_lag_months": "comp-open-closed-lag",
}

# Named rate ranges: (low end, central or None, high end, what it is). Each is evaluated on its own.
RANGES = {
    "part1_bracket": ("g_small", "g_ho", "g_ros",
                      "Part I's bracket: the small-compute bound to the Rosetta rate, Ho et al. central"),
    "ho_95ci": ("g_ho_lo", "g_ho", "g_ho_hi", "Ho et al.'s 95% interval"),
    "rosetta_families": ("g_ros_lo", "g_ros", "g_ros_hi",
                         "the Rosetta fit across model families; its low end of 1 means no drift"),
    "e1_full_sample": ("e1_lo", "e1", "e1_hi", "E1 on all joined models, 2.5th to 97.5th percentile of resampling"),
    "e1_subsets": ("e1_sub_min", None, "e1_sub_max", "E1's six samples of the same models, lowest to highest point"),
}
MC_RANGES = ["e1_full_sample", "e1_subsets", "ho_95ci", "part1_bracket"]  # rosetta_families has an unbounded end
LAWS = ["log_uniform", "uniform", "log_triangular"]


def sig(x: float, n: int = 6):
    """Round for the detail tables; None for an unbounded value."""
    if x is None or not math.isfinite(x):
        return None
    return float(f"{x:.{n}g}")


def log10g(g: float) -> float:
    if g < 1:
        raise ValueError(f"a yearly efficiency gain below 1 ({g}) is not drift")
    return math.log10(g)


def leak(h: float, jump: float, lg: float) -> float:
    """Corollary 2.3: years for drift at log10 gamma = lg to close headroom h after one-off jumps."""
    rest = max(0.0, h - jump)
    if rest == 0.0:
        return 0.0
    return math.inf if lg == 0.0 else rest / lg


# ---------------------------------------------------------------- the backtest's data


def load_models(path: Path, dates_from: str = "version", blank_is_open: bool = False) -> list[dict]:
    """One entry per model on the ECI (the chart file repeats a model once per version). The default
    reading takes each model's earliest version release date and counts as open weights only rows the
    file marks so; the other readings exist to show how the reproduced lag moves with them."""
    by = defaultdict(list)
    with path.open(newline="") as f:
        for r in csv.DictReader(f):
            if r["ECI"]:
                by[r["Slug"]].append(r)
    if len(by) < 100:
        raise SystemExit(f"only {len(by)} models with an ECI; the chart file changed shape")
    out = []
    for slug in sorted(by):
        rs = by[slug]
        ecis = {float(r["ECI"]) for r in rs}
        comps = {float(r["Training compute (FLOP)"]) for r in rs if r["Training compute (FLOP)"]}
        if max(ecis) - min(ecis) > 1e-9 or len(comps) > 1:
            raise SystemExit(f"{slug}: rows disagree on ECI or compute")
        version = sorted(r["Version release date"] for r in rs if r["Version release date"])
        published = sorted(r["Publication date"] for r in rs if r["Publication date"])
        dates = (version or published) if dates_from == "version" else (published or version)
        if not dates:
            continue
        access = sorted({r["Model accessibility"] for r in rs if r["Model accessibility"]})
        conf = sorted({r["Confidence"] for r in rs if r["Confidence"]})
        name = rs[0]["Model group"] or rs[0]["Model"] or rs[0]["Display name"]
        out.append({
            "slug": slug,
            "name": name,
            "date": date.fromisoformat(dates[0]),
            "eci": min(ecis),
            "eci_lo": float(rs[0]["ECI CI low"]),
            "access": access,
            "open": any(a.startswith("Open weights") for a in access) or (blank_is_open and not access),
            "closed": any(a in ("API access", "Hosted access (no API)", "Unreleased") for a in access),
            "log_c": math.log10(next(iter(comps))) if comps else None,
            "confidence": conf,
        })
    out.sort(key=lambda e: (e["date"], -e["eci"], e["slug"]))
    return out


def records(models: list[dict]) -> list[dict]:
    """Each model that set a new ECI high on its release date."""
    out, best = [], -math.inf
    for e in models:
        if e["eci"] > best:
            best = e["eci"]
            out.append(e)
    return out


def catch_up(target: dict, models: list[dict], end: date, pop: str, sure_only: bool = False) -> dict:
    """When models at or below a cap first matched the target's ECI, for caps lowered by h below its compute."""
    def ok(m):
        if m is target or m["log_c"] is None or m["eci"] < target["eci"]:
            return False
        if pop == "open" and not m["open"]:
            return False
        return not (sure_only and not set(m["confidence"]) & {"Confident", "Likely"})

    cands = [m for m in models if ok(m)]
    earlier = [m for m in cands if m["date"] < target["date"] and m["log_c"] <= target["log_c"]]
    first = {}
    for h in H_BACKTEST:
        hits = [m for m in cands if m["date"] >= target["date"] and m["log_c"] <= target["log_c"] - h + 1e-12]
        if hits:
            m = min(hits, key=lambda x: (x["date"], x["slug"]))
            first[str(h)] = {"years": sig((m["date"] - target["date"]).days / YEAR), "by": m["name"],
                             "censored": False}
        else:
            first[str(h)] = {"years": sig((end - target["date"]).days / YEAR), "by": None, "censored": True}
    # The record-setting catch-ups: each closes more headroom than any earlier one.
    events = []
    for m in sorted(cands, key=lambda x: (x["date"], x["log_c"], x["slug"])):
        h = target["log_c"] - m["log_c"]
        if m["date"] < target["date"] or h <= 0:
            continue
        if not events or h > events[-1]["h"] + 1e-12:
            t = (m["date"] - target["date"]).days / YEAR
            events.append({"h": h, "years": t, "by": m["name"], "date": m["date"].isoformat()})
    return {"first_match": first, "events": events, "matched_before_release": [m["name"] for m in earlier]}


def open_closed_lag(models: list[dict], w0: date, w1: date) -> dict:
    """Epoch's day-by-day lag with point estimates (the strict version), and the vertical ECI gap."""
    recs = records(models)
    lags, gaps, evaluable, segments = [], [], 0, []
    day = w0
    while day <= w1:
        avail = [e for e in models if e["date"] <= day]
        o = max((e for e in avail if e["open"]), key=lambda e: (e["eci"], -e["date"].toordinal(), e["slug"]))
        gaps.append(max(e["eci"] for e in avail) - o["eci"])
        above = [e for e in models if e is not o and e["eci"] >= o["eci"]]
        t_first = min(e["date"] for e in above) if above else None
        if t_first is None or t_first > day:
            lag, matched = 0, o
        else:
            lag = (day - t_first).days + 1
            matched = [r for r in recs if r["date"] < t_first][-1]
        lags.append(lag)
        both = o["log_c"] is not None and matched["log_c"] is not None
        evaluable += both
        seg = (o["name"], matched["name"], both)
        if not segments or segments[-1]["key"] != seg:
            segments.append({"key": seg, "from": day.isoformat(), "lag_days_on_first_day": lag})
        day += timedelta(days=1)
    return {
        "days": len(lags),
        "mean_lag_months": float(np.mean(lags)) / MONTH,
        "mean_eci_gap": float(np.mean(gaps)),
        "evaluable_days": int(evaluable),
        "segments": [{"from": x["from"], "open_model": x["key"][0], "record_matched": x["key"][1],
                      "both_computes_known": x["key"][2], "lag_days_on_first_day": x["lag_days_on_first_day"]}
                     for x in segments],
    }


def judge(h: float, t: float, censored: bool, lg_lo: float, lg_hi: float, j_lo: float, j_hi: float) -> str:
    """Is an observed leak time inside the expression's exact interval at headroom h?"""
    lo = leak(h, j_hi, lg_hi)
    hi = leak(h, j_lo, lg_lo)
    if censored:
        return "slower" if t > hi else "undetermined"
    if t < lo - 1e-12:
        return "faster"
    if t > hi + 1e-12:
        return "slower"
    return "inside"


def test_points(cu: dict) -> list[dict]:
    """The points a backtest judges: the first match at the record's own compute, then each catch-up."""
    f0 = cu["first_match"]["0.0"]
    pts = [{"h": 0.0, "years": f0["years"], "censored": f0["censored"], "by": f0["by"]}]
    pts += [{"h": e["h"], "years": e["years"], "censored": False, "by": e["by"]} for e in cu["events"]]
    return pts


# ---------------------------------------------------------------- main


def main() -> int:
    res = Results("E18", "e18_cap_leak", seed=SEED)
    gen = np.random.default_rng(SEED)
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    L = {k: float(numbers[v]["value"]) for k, v in LEDGER_IDS.items()}
    res.detail("ledger_inputs", {v: L[k] for k, v in sorted(LEDGER_IDS.items())})

    m, tr = L["m"], L["tr"]
    line = m * tr
    assert abs(line - L["line"]) < 1e-9, "the ledger's line is no longer m * T_r"
    tr_record = L["td_declared_days"] / YEAR + L["tresp_km"]
    h_ex = L["headroom"]

    # E1's six samples, from its result file, checked against the ledger's ends.
    e1 = json.loads(E1_RESULT.read_text())
    subsets = {k: float(v["algo_annual"]) for k, v in sorted(e1["details"]["eci_subsets"]["table"].items())}
    if len(subsets) != 6:
        raise SystemExit(f"E1 has {len(subsets)} samples, not six; its result changed shape")
    for got, want in ((min(subsets.values()), L["e1_sub_min"]), (max(subsets.values()), L["e1_sub_max"])):
        if abs(got / want - 1) > 1e-6:
            raise SystemExit("E1's result file and the ledger disagree on the samples' ends; rerun make model")
    res.detail("e1_samples_read", {"from": E1_RESULT.relative_to(ROOT).as_posix(), "algo_annual": subsets})

    classes = {
        "no_cheap_verifier": (L["j_lo"], L["j_hi"], "J from the typical to the high post-training jump, S_v = 0"),
        "cheap_verifier": (L["sv_lo"], L["sv_hi"],
                           "J = 0, S_v from one technique's typical saving to the cheap-verifier span"),
    }
    ranges = {k: (L[a], L[c] if c else None, L[b], what) for k, (a, c, b, what) in RANGES.items()}

    # ---- (1) The exact interval at two corners, over headrooms, and the headroom a cap needs.
    corners = {}
    for cname, (j_lo, j_hi, _) in classes.items():
        for rname, (g_lo, _g_c, g_hi, _) in ranges.items():
            lg_lo, lg_hi = log10g(g_lo), log10g(g_hi)
            corners[f"{cname}|{rname}"] = {
                "leak_years": {str(h): [sig(leak(h, j_hi, lg_hi)), sig(leak(h, j_lo, lg_lo))] for h in H_GRID},
                "headroom_needed_oom": [sig(j_lo + line * lg_lo), sig(j_hi + line * lg_hi)],
                "headroom_needed_oom_record_tr": [sig(j_lo + m * tr_record * lg_lo),
                                                  sig(j_hi + m * tr_record * lg_hi)],
            }
            # The headroom needed is where the leak time equals m * T_r: check the algebra, not evidence.
            for j, lg in ((j_lo, lg_lo), (j_hi, lg_hi)):
                if lg > 0:
                    assert abs(leak(j + line * lg, j, lg) - line) < 1e-9
    res.detail("corners", {
        "what": "the exact interval of the leak time (years) at each headroom (OOM), [fast corner, slow corner], "
                "and the headroom a cap needs for the leak time to exceed m * T_r, [low, high]; by Theorem 2.1 "
                "every input in the box gives a value between the two; null means unbounded (a rate of 1)",
        "classes": {k: v[2] for k, v in classes.items()},
        "ranges": {k: {"low": v[0], "central": v[1], "high": v[2], "what": v[3]} for k, v in ranges.items()},
        "m_times_tr_years": line,
        "record_tr_years": sig(tr_record),
        "record_tr_note": "E5's declared-path detection time plus E24's Kaplan-Meier median response; a median, not "
                          "a high quantile, and a share of findings were never halted",
        "table": corners,
    })

    # ---- The Monte Carlo inside each box: an illustration under three laws for the rate.
    h_arr = np.array(H_GRID)
    mc = {}
    for law in LAWS:
        for cname, (j_lo, j_hi, _) in classes.items():
            for rname in MC_RANGES:
                g_lo, g_c, g_hi, _ = ranges[rname]
                lg_lo, lg_hi = log10g(g_lo), log10g(g_hi)
                if law == "log_uniform":
                    lg = gen.uniform(lg_lo, lg_hi, DRAWS)
                elif law == "uniform":
                    lg = np.log10(gen.uniform(g_lo, g_hi, DRAWS))
                else:
                    mode = log10g(g_c) if g_c else 0.5 * (lg_lo + lg_hi)
                    lg = gen.triangular(lg_lo, mode, lg_hi, DRAWS)
                jump = gen.uniform(j_lo, j_hi, DRAWS)
                t = np.maximum(0.0, h_arr[:, None] - jump[None, :]) / lg[None, :]
                fast = np.array([leak(h, j_hi, lg_hi) for h in H_GRID])
                slow = np.array([leak(h, j_lo, lg_lo) for h in H_GRID])
                # Theorem 2.1 at fixed compute: no draw can leave the corners. An assertion, not a result.
                assert np.all(t >= fast[:, None] - 1e-9) and np.all(t <= slow[:, None] + 1e-9), "a draw left the corners"
                need = jump + line * lg
                mc[f"{law}|{cname}|{rname}"] = {
                    "leak_years_p5_p50_p95": {
                        str(h): [sig(float(q)) for q in np.quantile(t[i], [0.05, 0.5, 0.95])]
                        for i, h in enumerate(H_GRID)},
                    "share_above_line": {str(h): sig(float(np.mean(t[i] >= line))) for i, h in enumerate(H_GRID)},
                    "headroom_needed_p5_p50_p95": [sig(float(q)) for q in np.quantile(need, [0.05, 0.5, 0.95])],
                }
    if h_ex not in H_GRID:
        raise SystemExit(f"the example headroom {h_ex} is not on the headroom grid")
    med ={law: mc[f"{law}|no_cheap_verifier|part1_bracket"]["leak_years_p5_p50_p95"][str(h_ex)][1] for law in LAWS}
    res.detail("monte_carlo", {
        "what": "percentiles of the leak time inside each box, an illustration only: the box's corners are the "
                "result, and the median moves with the assumed law for the rate",
        "draws": DRAWS,
        "laws": {"log_uniform": "log10 gamma uniform", "uniform": "gamma uniform",
                 "log_triangular": "log10 gamma triangular, peaked at the range's central value (its log midpoint "
                                   "when it has none)"},
        "jumps": "J or S_v uniform on its range",
        "example_headroom_median_by_law": med,
        "table": mc,
    })

    # ---- How the leak time and the headroom needed move across E1's six samples.
    j_lo, j_hi, _ = classes["no_cheap_verifier"]
    s_lo, s_hi, _ = classes["cheap_verifier"]
    by_sample, verdicts = {}, {"inside": 0, "outside": 0, "mixed": 0}
    for name, g in subsets.items():
        lg = log10g(g)
        t_fast, t_slow = leak(h_ex, j_hi, lg), leak(h_ex, j_lo, lg)
        verdict = "inside" if t_slow < line else "outside" if t_fast >= line else "mixed"
        verdicts[verdict] += 1
        by_sample[name] = {
            "gamma": g,
            "leak_years_example_no_verifier": [sig(t_fast), sig(t_slow)],
            "leak_years_example_cheap_verifier": [sig(leak(h_ex, s_hi, lg)), sig(leak(h_ex, s_lo, lg))],
            "headroom_needed_no_verifier": [sig(j_lo + line * lg), sig(j_hi + line * lg)],
            "headroom_needed_cheap_verifier": [sig(s_lo + line * lg), sig(s_hi + line * lg)],
            "headroom_needed_no_verifier_record_tr": [sig(j_lo + m * tr_record * lg), sig(j_hi + m * tr_record * lg)],
            "example_cap_against_line": verdict,
        }
    res.detail("by_e1_sample", {
        "what": "at the example headroom, the leak time [high jump, low jump] and the headroom needed [low jump, high "
                "jump] at each of E1's six sample rates; 'inside' means the leak time is below m * T_r at every jump "
                "in the range (the example cap fails the line), 'outside' that it exceeds it at every jump",
        "example_headroom_oom": h_ex,
        "table": by_sample,
        "verdicts": verdicts,
    })

    # ---- (2) C2(b) at fixed compute: does the expression's interval separate from one multiplier's?
    sep = {}
    for cname, (a_lo, a_hi, _) in classes.items():
        for rname in ("part1_bracket", "ho_95ci", "e1_full_sample", "e1_subsets"):
            g_lo, _gc, g_hi, _ = ranges[rname]
            lg_lo, lg_hi = log10g(g_lo), log10g(g_hi)
            # Disjoint when the expression's slow corner is below the single multiplier's fast corner.
            analytic = a_lo * lg_hi / (lg_hi - lg_lo)
            grid = np.arange(FINE, 8.0, FINE)
            disjoint = np.array([leak(h, a_lo, lg_lo) < h / lg_hi for h in grid])
            last = float(grid[disjoint][-1]) if disjoint.any() else 0.0
            assert disjoint[: int(analytic / FINE) - 2].all() and not disjoint[int(analytic / FINE) + 2:].any(), \
                "the separation is not one interval below the boundary"
            assert abs(last - analytic) <= 2 * FINE, "numerical and analytic boundaries differ"
            need_lo = a_lo + line * lg_lo
            sep[f"{cname}|{rname}"] = {
                "boundary_oom": sig(analytic),
                "headroom_needed_low_corner_oom": sig(need_lo),
                "separates_only_where_cap_fails_line": bool(analytic < need_lo),
                "disjoint_at_example": bool(leak(h_ex, a_lo, lg_lo) < h_ex / lg_hi),
                "expression_at_example": [sig(leak(h_ex, a_hi, lg_hi)), sig(leak(h_ex, a_lo, lg_lo))],
                "single_multiplier_at_example": [sig(h_ex / lg_hi), sig(h_ex / lg_lo)],
            }
    # The scale term: the memo's one rate (Ho et al.) against E1's full-sample rate at the cap's scale.
    scale = {}
    ho_lo, ho_hi = log10g(L["g_ho_lo"]), log10g(L["g_ho_hi"])
    for scale_name, (lo_k, hi_k) in {"1e24": ("e1_1e24_lo", "e1_1e24_hi"), "1e26": ("e1_1e26_lo", "e1_1e26_hi")}.items():
        c_lo, c_hi = log10g(L[lo_k]), log10g(L[hi_k])
        expr = [leak(h_ex, j_hi, c_hi), leak(h_ex, j_lo, c_lo)]
        single = [h_ex / ho_hi, h_ex / ho_lo]
        scale[scale_name] = {"expression": [sig(x) for x in expr], "single_multiplier_ho": [sig(x) for x in single],
                             "disjoint": bool(expr[1] < single[0] or single[1] < expr[0])}
    res.detail("c2b_fixed_compute", {
        "what": "C2(b) read as: the two intervals do not overlap. Where the boundary is below the headroom needed at "
                "the low corner, every headroom at which they separate is one where the cap's leak time is below "
                "m * T_r at every input in the box. Same rate range for both, so the difference is the "
                "jump terms alone; below the boundary headroom the intervals are disjoint, above it they overlap. "
                "This is arithmetic on Part I's input ranges, not evidence that either form is right",
        "separation": sep,
        "scale_term_if_e1_full_sample_were_trusted": {
            "what": "the expression with E1's full-sample rate at the cap's scale (interaction fit) against one "
                    "multiplier at Ho et al.'s interval, example headroom, no cheap verifier; E1's six samples do not "
                    "support that rate (at or above 1e24 FLOP they give 393 and 1,512 a year), so this is not a test",
            "table": scale,
        },
    })

    # ---- (3) The backtest on Epoch's open-closed data.
    csv_path = fetch(URL, "epoch/open_closed_eci_gap_benchmarked_models.csv", res,
                     what="Epoch AI, ECI scores of open- and closed-weight models (chart data, open-closed gap insight)")
    models = load_models(csv_path)
    end = max(e["date"] for e in models)
    first_closed = min(e["date"] for e in models if e["closed"])
    recs = records(models)
    targets = [r for r in recs if r["log_c"] is not None and r["date"] >= first_closed]
    if len(targets) < 2:
        raise SystemExit("fewer than two ECI records with a compute estimate; the chart file changed shape")

    def run(target_list, pop, sure_only=False):
        out = {}
        for tg in target_list:
            cu = catch_up(tg, models, end, pop, sure_only)
            out[tg["name"]] = {"date": tg["date"].isoformat(), "eci": sig(tg["eci"]), "log10_flop": sig(tg["log_c"]),
                               "confidence": tg["confidence"], **cu}
        return out

    def score(bt, j_range=(0.0, 0.0)):
        """Count test points inside, faster or slower than each range's exact interval."""
        tally = {}
        for rname in sorted(RANGES):
            g_lo, _gc, g_hi, _ = ranges[rname]
            lg_lo, lg_hi = log10g(g_lo), log10g(g_hi)
            c = {"inside": 0, "faster": 0, "slower": 0, "undetermined": 0}
            for tg in bt.values():
                if tg["matched_before_release"]:
                    continue
                for p in test_points(tg):
                    c[judge(p["h"], p["years"], p["censored"], lg_lo, lg_hi, *j_range)] += 1
            tally[rname] = c
        return tally

    bt_all = run(targets, "all")
    bt_open = run(targets, "open")
    events = [e for tg in bt_all.values() for e in tg["events"] if e["years"] > 0]
    implied = sorted(10 ** (e["h"] / e["years"]) for e in events)
    h0 = [tg["first_match"]["0.0"] for tg in bt_all.values()]
    h0_obs = sorted(f["years"] for f in h0 if not f["censored"])
    h0_cens = sorted(f["years"] for f in h0 if f["censored"])
    if len(h0_obs) < 2 or len(implied) < 2:
        raise SystemExit("too few catch-ups to report; the chart file changed shape")
    local = []
    for tname, tg in bt_all.items():
        ev = tg["events"]
        for a, b in zip(ev, ev[1:]):
            local.append({"target": tname, "from": a["by"], "to": b["by"], "oom_closed": sig(b["h"] - a["h"]),
                          "days": round((b["years"] - a["years"]) * YEAR)})
    tally_j0 = score(bt_all)
    tally_j = score(bt_all, (L["j_lo"], L["j_hi"]))
    n_points = sum(tally_j0["part1_bracket"].values())
    ranges["backtest_events"] = (implied[0], None, implied[-1], "the rates the backtest's catch-ups imply, J = 0")

    # Sensitivities: near-frontier targets, and compute estimates that are confident or likely only.
    def standing(day):
        return [r for r in recs if r["date"] <= day][-1]
    near = [e for e in models if e["log_c"] is not None and e["date"] >= first_closed
            and e["eci"] >= standing(e["date"])["eci_lo"]]
    bt_near = run(near, "all")
    sure_targets = [t for t in targets if set(t["confidence"]) & {"Confident", "Likely"}]
    bt_sure = run(sure_targets, "all", sure_only=True)

    def summary(bt):
        kept = {k: v for k, v in bt.items() if not v["matched_before_release"]}
        f0 = [v["first_match"]["0.0"] for v in kept.values()]
        obs = sorted(f["years"] for f in f0 if not f["censored"])
        ev = [e for v in kept.values() for e in v["events"] if e["years"] > 0]
        imp = sorted(10 ** (e["h"] / e["years"]) for e in ev)
        return {"targets": len(bt), "targets_matched_under_own_compute_before_release": len(bt) - len(kept),
                "first_match_at_own_compute_years": [sig(x) for x in obs],
                "censored_at_own_compute": sum(1 for f in f0 if f["censored"]),
                "implied_gamma_min_max": [sig(imp[0]), sig(imp[-1])] if imp else None,
                "tally_j0": score(kept)}

    def jsonable(bt):
        return {k: {**v, "events": [{**e, "h": sig(e["h"]), "years": sig(e["years"])} for e in v["events"]]}
                for k, v in bt.items()}

    res.detail("backtest", {
        "what": "Part I's design: a cap at a then-frontier model's compute (h = 0) and at h OOM below it; the first "
                "model at or below the cap to match the record's ECI. At h = 0 the expression predicts 0 for every "
                "input. Each catch-up closing more headroom than any earlier one is an event, implying a rate "
                "10^(h / t) with J = 0",
        "data_end": end.isoformat(),
        "first_closed_model_with_eci": first_closed.isoformat(),
        "records": [{"name": r["name"], "date": r["date"].isoformat(), "eci": sig(r["eci"]),
                     "log10_flop": sig(r["log_c"]) if r["log_c"] is not None else None} for r in recs],
        "targets_all_models": jsonable(bt_all),
        "targets_open_weights_only": jsonable(bt_open),
        "open_only_same_as_all": json.dumps(jsonable(bt_open), sort_keys=True) == json.dumps(jsonable(bt_all), sort_keys=True),
        "implied_gamma_by_event": [sig(x) for x in implied],
        "steps_between_catch_ups": local,
        "tally_j0": tally_j0,
        "tally_j_part1_range": tally_j,
        "sensitivity_near_frontier": {
            "what": "targets: every model with a compute estimate whose ECI is at least the standing record's lower "
                    "interval end at its release; a target already matched under its own compute before its release "
                    "was not at the efficient frontier and is left out of the tallies",
            **summary(bt_near)},
        "sensitivity_confident_or_likely": {
            "what": "targets and catch-up models whose compute estimate Epoch rates confident or likely",
            **summary(bt_sure)},
    })

    # Epoch's day-by-day lag, reproduced with point estimates, and how many of its days the expression can use.
    with TABLE.open(newline="") as f:
        pub = {r["id"]: r for r in csv.DictReader(f)}
    w0, w1 = date.fromisoformat(pub["oc-window-start"]["value"]), date.fromisoformat(pub["oc-window-end"]["value"])
    oc = open_closed_lag(models, w0, w1)
    readings = {
        "publication_dates": open_closed_lag(load_models(csv_path, dates_from="publication"), w0, w1),
        "blank_accessibility_as_open": open_closed_lag(load_models(csv_path, blank_is_open=True), w0, w1),
    }
    n_days, evaluable = oc["days"], oc["evaluable_days"]
    lag_months, gap_eci = oc["mean_lag_months"], oc["mean_eci_gap"]
    pub_strict, pub_gap = float(pub["oc-lag-strict"]["value"]), float(pub["oc-gap-eci"]["value"])
    blank = sum(1 for e in models if not e["access"])
    res.detail("open_closed_lag", {
        "what": "Epoch's method with point estimates: each day, the best open-weight model so far, and the days since "
                "the last date on which the state of the art was strictly below it; the vertical gap is the state "
                "of the art minus that open model's ECI",
        "window": [w0.isoformat(), w1.isoformat()],
        "days": n_days,
        "mean_lag_months": sig(lag_months),
        "published_strict_months": pub_strict,
        "published_headline_months": L["oc_lag_months"],
        "mean_eci_gap": sig(gap_eci),
        "published_eci_gap_lo_mid_hi": [float(pub["oc-gap-eci-lo"]["value"]), pub_gap,
                                        float(pub["oc-gap-eci-hi"]["value"])],
        "segments": oc["segments"],
        "evaluable_days": evaluable,
        "models_with_blank_accessibility": blank,
        "other_readings": {
            "what": "how the reproduced strict lag moves with two choices the page leaves open; counting blank rows as "
                    "open also counts closed models (o3-pro, Gemini 3.5 Flash) as open, so it is not Epoch's reading "
                    "either",
            **{k: {"mean_lag_months": sig(v["mean_lag_months"]), "mean_eci_gap": sig(v["mean_eci_gap"]),
                   "segments": v["segments"]} for k, v in readings.items()},
        },
    })

    # ---------------------------------------------------------------- numbers for the ledger
    pb = ranges["part1_bracket"]
    lg_pb_lo, lg_pb_hi = log10g(pb[0]), log10g(pb[2])
    lg_s_lo, lg_s_hi = log10g(L["e1_sub_min"]), log10g(L["e1_sub_max"])
    s_pb = sep["no_cheap_verifier|part1_bracket"]
    s_sub = sep["no_cheap_verifier|e1_subsets"]
    v_pb = sep["cheap_verifier|part1_bracket"]
    v_sub = sep["cheap_verifier|e1_subsets"]
    n_disjoint_ex = sum(v["disjoint_at_example"] for v in sep.values())

    res.number("e18-leak-part1-lo", leak(h_ex, j_hi, lg_pb_hi), unit="years", fmt=".1f",
               label="leak time of the example cap, no cheap verifier, fast corner of Part I's bracket (Rosetta rate, "
                     "high post-training jump); the exact interval's lower end")
    res.number("e18-leak-part1-hi", leak(h_ex, j_lo, lg_pb_lo), unit="years", fmt=".1f",
               label="leak time of the example cap, no cheap verifier, slow corner of Part I's bracket (small-compute "
                     "bound, typical jump); the exact interval's upper end")
    res.number("e18-leak-subset-lo", leak(h_ex, j_hi, lg_s_hi), unit="years", fmt=".2f",
               label="leak time of the example cap at the fastest of E1's six sample rates (at or above 1e24.5 FLOP) "
                     "and the high post-training jump")
    res.number("e18-leak-subset-hi", leak(h_ex, j_lo, lg_s_lo), unit="years", fmt=".1f",
               label="leak time of the example cap at the slowest of E1's six sample rates (not open weights) and the "
                     "typical post-training jump")
    res.number("e18-leak-verifier-hi", leak(h_ex, s_lo, lg_pb_lo), unit="years", fmt=".1f",
               label="leak time of the example cap with a cheap verifier, slow corner of Part I's bracket (span of one "
                     "typical technique); the fast corner is 0, the span covering the headroom")
    res.number("e18-subsets-inside-line", verdicts["inside"], unit="samples", fmt=",.0f",
               label="of E1's six sample rates, those at which the example cap's leak time is below m * T_r at every "
                     "post-training jump in Part I's range (the cap fails the illustrative line)")
    res.number("e18-subsets-outside-line", verdicts["outside"], unit="samples", fmt=",.0f",
               label="of E1's six sample rates, those at which the example cap's leak time exceeds m * T_r at every "
                     "post-training jump in Part I's range")
    res.number("e18-need-part1-lo", j_lo + line * lg_pb_lo, unit="OOM", fmt=".1f",
               label="headroom a cap needs for its leak time to exceed m * T_r, no cheap verifier, low corner of "
                     "Part I's bracket")
    res.number("e18-need-part1-hi", j_hi + line * lg_pb_hi, unit="OOM", fmt=".1f",
               label="headroom a cap needs for its leak time to exceed m * T_r, no cheap verifier, high corner of "
                     "Part I's bracket")
    res.number("e18-need-verifier-part1-hi", s_hi + line * lg_pb_hi, unit="OOM", fmt=".1f",
               label="headroom a cap needs for its leak time to exceed m * T_r, cheap verifier, high corner of Part I's "
                     "bracket")
    res.number("e18-need-subset-lo", j_lo + line * lg_s_lo, unit="OOM", fmt=".1f",
               label="headroom a cap needs for its leak time to exceed m * T_r at the slowest of E1's six sample rates, "
                     "no cheap verifier, typical jump")
    res.number("e18-need-subset-hi", j_hi + line * lg_s_hi, unit="OOM", fmt=".1f",
               label="headroom a cap needs for its leak time to exceed m * T_r at the fastest of E1's six sample rates, "
                     "no cheap verifier, high jump")
    res.number("e18-need-verifier-subset-hi", s_hi + line * lg_s_hi, unit="OOM", fmt=".1f",
               label="headroom a cap needs at the fastest of E1's six sample rates with a cheap verifier's full span")
    res.number("e18-need-record-tr-part1-hi", j_hi + m * tr_record * lg_pb_hi, unit="OOM", fmt=".1f",
               label="headroom needed, no cheap verifier, high corner of Part I's bracket, with T_r from the record "
                     "(E5's declared-path detection plus E24's median response, not a high quantile)")
    res.number("e18-mc-median-spread", max(med.values()) / min(med.values()), fmt=".2f",
               label="illustration: largest over smallest Monte Carlo median of the example cap's leak time across "
                     "three assumed laws for the rate inside Part I's bracket (the median is the law's, not data's)")
    res.number("e18-b-sep-part1", s_pb["boundary_oom"], unit="OOM", fmt=".2f",
               label="C2(b) at fixed compute, no cheap verifier, Part I's bracket for both: largest headroom at which "
                     "the expression's interval and a single multiplier's do not overlap (arithmetic on the ranges)")
    res.number("e18-b-sep-subsets", s_sub["boundary_oom"], unit="OOM", fmt=".2f",
               label="the same boundary with the rate across E1's six samples")
    res.number("e18-b-sep-verifier-part1", v_pb["boundary_oom"], unit="OOM", fmt=".2f",
               label="the same boundary with a cheap verifier, Part I's bracket")
    res.number("e18-b-sep-verifier-subsets", v_sub["boundary_oom"], unit="OOM", fmt=".2f",
               label="the same boundary with a cheap verifier, rate across E1's six samples")
    res.number("e18-b-sep-fails-line", sum(v["separates_only_where_cap_fails_line"] for v in sep.values()),
               unit="cases", fmt=",.0f",
               label=f"of {len(sep)} pairs of class and rate range, those in which every headroom where the two "
                     "intervals separate is one where the cap's leak time is below m * T_r at every input")
    res.number("e18-b-disjoint-example", n_disjoint_ex, unit="cases", fmt=",.0f",
               label=f"of {len(sep)} pairs of class and rate range, those in which the expression's interval and a "
                     "single multiplier's do not overlap at the example headroom")
    res.number("e18-bt-targets", len(targets), unit="records", fmt=",.0f",
               label="ECI records with a compute estimate, set on or after the first closed model's ECI: the "
                     "then-frontier caps the backtest can place")
    res.number("e18-bt-h0-lo", h0_obs[0], unit="years", fmt=".2f",
               label="shortest time until a model at or below a then-frontier record's compute matched its ECI "
                     "(the expression predicts 0 for every input)")
    res.number("e18-bt-h0-hi", h0_obs[-1], unit="years", fmt=".2f",
               label="longest such time among the records that were matched")
    res.number("e18-bt-censored", len(h0_cens), unit="records", fmt=",.0f",
               label="records not yet matched by any model with a compute estimate at or below their own compute "
                     "when the data end",
               note=f"censored at {h0_cens[0]:.2f} years" if h0_cens else "")
    res.number("e18-bt-events", len(events), unit="catch-ups", fmt=",.0f",
               label="catch-ups below a record's compute that close more headroom than any earlier one")
    res.number("e18-bt-gamma-lo", implied[0], fmt=".2f",
               label="lowest yearly rate a catch-up implies, 10^(h / t) with J = 0 (lower end of the observed range, "
                     "not an interval)")
    res.number("e18-bt-gamma-hi", implied[-1], fmt=",.0f",
               label="highest yearly rate a catch-up implies, 10^(h / t) with J = 0 (upper end of the observed range)")
    res.number("e18-bt-max-headroom", max(e["h"] for e in events), unit="OOM", fmt=".2f",
               label="largest headroom closed below a record's compute in the backtest")
    res.number("e18-bt-inside-part1", tally_j0["part1_bracket"]["inside"], unit="points", fmt=",.0f",
               label=f"of {n_points} backtest points (first matches at the record's compute and catch-ups), those "
                     "inside the expression's exact interval with Part I's bracket and J = 0")
    res.number("e18-bt-inside-subsets", tally_j0["e1_subsets"]["inside"], unit="points", fmt=",.0f",
               label=f"of {n_points} backtest points, those inside the exact interval with the rate across E1's six "
                     "samples and J = 0")
    res.number("e18-bt-inside-part1-j", tally_j["part1_bracket"]["inside"], unit="points", fmt=",.0f",
               label=f"of {n_points} backtest points, those inside the exact interval with Part I's bracket and J over "
                     "Part I's post-training range")
    res.number("e18-oc-lag-strict", lag_months, unit="months", fmt=".1f",
               label="Epoch's open-closed lag over its 2026 window, reproduced from its chart data with point "
                     "estimates (the strict version)")
    res.number("e18-oc-lag-over-published", lag_months / pub_strict, fmt=".2f",
               label="reproduced strict lag over the strict lag Epoch publishes (1 means it reproduces)")
    res.number("e18-oc-gap-eci", gap_eci, unit="ECI points", fmt=".1f",
               label="mean ECI gap between the state of the art and the best open model over Epoch's 2026 window, "
                     "reproduced")
    res.number("e18-oc-evaluable-days", evaluable, unit="days", fmt=",.0f",
               label=f"of the window's {n_days} days, those on which both the best open model and the record it "
                     "matched have a public compute estimate, so the expression could predict the lag")
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
