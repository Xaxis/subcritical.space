#!/usr/bin/env python3
"""E5: detection as the evader sees it, and the historical discovery rate of covert programmes.

Two parts, for claims C3, C1, C8 and C12 in research/04-claims.md.

Part 1, the discovery rate. A survival fit over covert programmes compiled case by case in
tools/exp/data/e05_detection.csv, wider than the seven of the organisational chapter (O4): sixteen
programmes and undeclared experiments, each with a start and a discovery or disclosure date and the
source that gives each. Time runs from the decision or construction start to the first outside
discovery. Programmes the party disclosed itself are censored at the disclosure. Fitted: the
constant hazard (discoveries over programme-years, with an exact Poisson interval and a case
bootstrap), a Weibull with censoring (is discovery likelier early or late?) and the Kaplan-Meier
median. A sensitivity analysis reruns the fit over which cases are included and how the disputed
ones are coded, and leaves out each case in turn. The record is a convenience sample of programmes
that were eventually found or disclosed; programmes never found are missing by construction.

Part 2, C3's Monte Carlo. Paths open to a party (the declared fleet, one undeclared site, sites
spread below the satellite line, the untraced chip pool, cloud rental, distillation) and the
channels that watch each, with rates from the ledger: chip sampling [Shavit], facility power
metering [Kimpson], detection of diversion [Epoch's smuggling model], satellite imagery
[Koopmanschap], and the historical rate from part 1 for intelligence, insiders and the media.
Channels sharing a trust anchor or a tip source merge into one with the larger rate: sampling
with metering (both need the host's access to a declared site), imagery with intelligence (imagery
historically confirmed tips). The evader's miss is the maximum over paths; the memo's is the
product of every channel's miss. Each path's detection time T_d is the window it needs to bring
its miss chance to the prevention beta. No path's breakout time is assumed: misses are reported
at the memo's placeholder breakout time and the hardwired-pause horizon, from the ledger.

All randomness comes from one numpy generator seeded with SEED. No data are fetched: the inputs
are the hand-compiled case table and ledger values read from data/numbers.json.

  .venv/bin/python tools/exp/e05_detection.py      (CPU, under a minute; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np
from scipy import optimize, stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results  # noqa: E402

SEED = 20261127
CASES = Path(__file__).resolve().parent / "data" / "e05_detection.csv"
BOOT = 10_000  # case bootstrap draws for the hazard
BOOT_WEIBULL = 2_000  # case bootstrap draws for the Weibull shape (each is an optimisation)
DRAWS = 200_000  # Monte Carlo draws for C3
YEAR = 365.25

LEDGER_IDS = [
    "org-iraq-years", "org-libya-years", "org-iran-years", "org-fordow-years-low",
    "org-syria-years", "org-biopreparat-years", "org-sa-years", "org-covert-hazard",
    "def-prevent-beta", "claim-confidence", "org-memo-detect-rate", "breakout-years",
    "org-hwp-tb", "miss-prob-one-channel", "phys-shavit-prob", "phys-shavit-days",
    "phys-meter-day-detect", "org-diversion-detect", "org-diversion-detect-low",
    "org-diversion-detect-high", "phys-sat-reliable", "phys-sat-miss-max",
    "phys-floor-power-1e26-now", "phys-floor-power-1e26-pause",
]
O4_YEARS = LEDGER_IDS[:7]


# Dates as the sources give them, turned into one calendar date by a stated rule.
DATE_RULES = {
    "YYYY-MM-DD": "that day",
    "YYYY-MM-late": "the 25th of the month",
    "YYYY-MM": "the 15th of the month",
    "YYYY-MM/MM": "the first day of the second month (the midpoint of the two)",
    "YYYY": "2 July (mid-year)",
    "early YYYY": "1 March",
    "spring YYYY": "15 April",
    "mid YYYY": "2 July",
    "late YYYY": "15 November",
    "early YYY0s": "2 July of the decade's second year (1.5 years in)",
    "about N years before D": "D moved back N years",
}


def to_date(text: str) -> date:
    t = text.strip()
    if m := re.fullmatch(r"about (\d+) years before (.+)", t):
        d = to_date(m.group(2))
        return d.replace(year=d.year - int(m.group(1)))
    if m := re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", t):
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if m := re.fullmatch(r"(\d{4})-(\d{2})-late", t):
        return date(int(m.group(1)), int(m.group(2)), 25)
    if m := re.fullmatch(r"(\d{4})-(\d{2})/(\d{2})", t):
        return date(int(m.group(1)), int(m.group(3)), 1)
    if m := re.fullmatch(r"(\d{4})-(\d{2})", t):
        return date(int(m.group(1)), int(m.group(2)), 15)
    if m := re.fullmatch(r"(\d{4})", t):
        return date(int(m.group(1)), 7, 2)
    if m := re.fullmatch(r"(early|spring|mid|late) (\d{4})", t):
        month, day = {"early": (3, 1), "spring": (4, 15), "mid": (7, 2), "late": (11, 15)}[m.group(1)]
        return date(int(m.group(2)), month, day)
    if m := re.fullmatch(r"early (\d{3})0s", t):
        return date(int(m.group(1)) * 10 + 1, 7, 2)
    raise ValueError(f"no date rule for {text!r}")


def years(a: date, b: date) -> float:
    return (b.toordinal() - a.toordinal()) / YEAR


def load_cases() -> list[dict]:
    with CASES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 8:
        raise SystemExit(f"{CASES.name} has {len(rows)} cases; expected the full table")
    for r in rows:
        for key in ("start", "found"):
            to_date(r[key])
        if r["outcome"] not in ("found", "disclosed"):
            raise SystemExit(f"{r['id']}: outcome must be found or disclosed")
    return rows


def coded(r: dict, *, start_alt=False, use_alt=False, censor_after_end=False) -> tuple[float, int]:
    """(years to discovery or censoring, 1 if discovered) for one case under one coding."""
    start = to_date(r["start_alt"] if start_alt and r["start_alt"] else r["start"])
    found, outcome = r["found"], r["outcome"]
    if use_alt and r["alt_outcome"]:
        found, outcome = r["alt_found"], r["alt_outcome"]
    end = to_date(found)
    event = 1 if outcome == "found" else 0
    if censor_after_end and event and r["ended"] and to_date(r["ended"]) < end:
        end, event = to_date(r["ended"]), 0
    return years(start, end), event


def exp_fit(t: np.ndarray, e: np.ndarray, conf: float) -> dict:
    d, total = int(e.sum()), float(t.sum())
    a = 1 - conf
    lo = stats.chi2.ppf(a / 2, 2 * d) / (2 * total) if d > 0 else 0.0
    hi = stats.chi2.ppf(1 - a / 2, 2 * d + 2) / (2 * total)
    return {"events": d, "exposure_years": total, "hazard": d / total, "lo": lo, "hi": hi}


def weibull_nll(params: np.ndarray, t: np.ndarray, e: np.ndarray) -> float:
    k, lam = np.exp(params)
    z = t / lam
    return -float(np.sum(e * (np.log(k / lam) + (k - 1) * np.log(z))) - np.sum(z**k))


def weibull_fit(t: np.ndarray, e: np.ndarray) -> tuple[float, float, float]:
    """Shape k, scale and the maximised log-likelihood. k above 1: discovery likelier later."""
    x0 = np.array([0.0, math.log(t.sum() / max(e.sum(), 1))])
    res = optimize.minimize(weibull_nll, x0, args=(t, e), method="Nelder-Mead",
                            options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
    k, lam = np.exp(res.x)
    return float(k), float(lam), -float(res.fun)


def km_median(t: np.ndarray, e: np.ndarray) -> float:
    """Kaplan-Meier median; inf if the curve never falls to one half."""
    order = np.lexsort((-e, t))  # events before censorings at a tie
    s, at_risk = 1.0, len(t)
    for i in order:
        if e[i]:
            s *= 1 - 1 / at_risk
            if s <= 0.5:
                return float(t[i])
        at_risk -= 1
    return float("inf")


def q(x: np.ndarray, p: float) -> float:
    return float(np.quantile(x, p))


def main() -> int:
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    led = {i: numbers[i]["value"] for i in LEDGER_IDS}
    res = Results("E5", "e05_detection", seed=SEED)
    res.detail("ledger_inputs", led)
    conf = led["claim-confidence"]
    plo, phi = (1 - conf) / 2, 1 - (1 - conf) / 2
    beta = led["def-prevent-beta"]
    gen = np.random.default_rng(SEED)

    # ---- Part 1: the discovery rate -------------------------------------------------------
    rows = load_cases()
    ids = [r["id"] for r in rows]
    main_t, main_e = map(np.array, zip(*(coded(r) for r in rows)))
    main_e = main_e.astype(int)
    fit = exp_fit(main_t, main_e, conf)
    lam_hat = fit["hazard"]

    k_hat, scale_hat, ll_w = weibull_fit(main_t, main_e)
    ll_exp = float(np.sum(main_e * math.log(lam_hat)) - lam_hat * main_t.sum())
    lr_p = float(stats.chi2.sf(2 * (ll_w - ll_exp), 1))
    km = km_median(main_t, main_e)

    n = len(rows)
    idx = gen.integers(0, n, (BOOT, n))
    boot_d, boot_T = main_e[idx].sum(1), main_t[idx].sum(1)
    boot_lam = boot_d / boot_T
    boot_k = []
    for row in idx[:BOOT_WEIBULL]:
        if main_e[row].sum() >= 2:
            boot_k.append(weibull_fit(main_t[row], main_e[row])[0])
    boot_k = np.array(boot_k)

    # O4's own arithmetic, from the ledger, reproduced; then with self-disclosed South Africa censored.
    o4_years = [led[i] for i in O4_YEARS]
    o4_hazard = 7 / sum(o4_years)
    o4_censored = 6 / sum(o4_years)

    # Sensitivity: which cases, and how the disputed ones are coded.
    def subset(keep=lambda r: True, alt=(), start_alt=False, censor_after_end=False) -> dict:
        """The constant-rate fit over the kept cases, with the cases in `alt` on their alternative coding."""
        sel = [r for r in rows if keep(r)]
        t, e = map(np.array, zip(*(coded(r, use_alt=r["id"] in alt, start_alt=start_alt,
                                         censor_after_end=censor_after_end) for r in sel)))
        out = exp_fit(t, e.astype(int), conf)
        out["cases"] = len(sel)
        return out

    first_per_party = {}
    for r in sorted(rows, key=lambda r: to_date(r["start"])):
        first_per_party.setdefault(r["party"], r["id"])
    in_o4 = lambda r: r["in_o4"] == "yes"  # noqa: E731
    lower = {r["id"] for r in rows if r["alt_outcome"] and r["alt_outcome"] != "found"}
    raise_ = {r["id"] for r in rows if r["alt_outcome"] == "found"}
    variants = {
        "main: every case, main codings": subset(),
        "O4's seven, coded from the case table": subset(in_o4),
        "O4's seven, South Africa coded as O4 did": subset(in_o4, alt={"south-africa"}),
        "states only (without Aum Shinrikyo)": subset(lambda r: r["actor"] == "state"),
        "nuclear only": subset(lambda r: r["domain"] == "nuclear"),
        "programmes only (without laboratory experiments)": subset(lambda r: r["kind"] == "programme"),
        "under a treaty or Council obligation only": subset(
            lambda r: r["under_obligation"] not in ("none", "national law")),
        "first programme per party only": subset(lambda r: first_per_party[r["party"]] == r["id"]),
        "Fordow from 2002": subset(start_alt=True),
        "discoveries after the activity ended censored at its end": subset(censor_after_end=True),
        "every coding that lowers the rate at once": subset(alt=lower, start_alt=True, censor_after_end=True),
        "every coding that raises the rate at once": subset(alt=raise_),
    }
    for r in rows:
        if r["alt_outcome"]:
            variants[f"{r['id']} coded {r['alt_outcome']} at {r['alt_found']}"] = subset(alt={r["id"]})
    sens = [v["hazard"] for v in variants.values()]

    loo = {}
    for i, rid in enumerate(ids):
        keep = np.arange(n) != i
        loo[rid] = main_e[keep].sum() / main_t[keep].sum()
    loo_vals = np.array(list(loo.values()))

    # ---- Part 2: C3's Monte Carlo ---------------------------------------------------------
    # Historical channel: resample the cases in every draw, as the bootstrap does.
    idx = gen.integers(0, n, (DRAWS, n))
    lam_h = main_e[idx].sum(1) / main_t[idx].sum(1)
    # Diversion detection: Epoch's median and 90% interval, a two-piece normal in log-odds.
    logit = lambda p: math.log(p / (1 - p))  # noqa: E731
    mu = logit(led["org-diversion-detect"])
    z95 = stats.norm.ppf(0.95)
    s_lo = (mu - logit(led["org-diversion-detect-low"])) / z95
    s_hi = (logit(led["org-diversion-detect-high"]) - mu) / z95
    zd = gen.standard_normal(DRAWS)
    p_div = 1 / (1 + np.exp(-(mu + zd * np.where(zd < 0, s_lo, s_hi))))
    # Satellite discovery of a site: the classifier found every facility above its line in a small
    # sample and missed all below it, but finding an undeclared site from scratch is judged perhaps
    # infeasible. Above the line the chance is drawn uniform on [0, 1]; below it, zero.
    u_sat = gen.random(DRAWS)
    sat_line = led["phys-sat-reliable"]
    power = {"site-now": led["phys-floor-power-1e26-now"], "site-pause": led["phys-floor-power-1e26-pause"]}
    p_sat = {k: (u_sat if v >= sat_line else np.zeros(DRAWS)) for k, v in power.items()}
    lam_meter = -math.log(1 - led["phys-meter-day-detect"]) * YEAR  # per year, strongest disguise
    lam_samp = -math.log(1 - led["phys-shavit-prob"]) / (led["phys-shavit-days"] / YEAR)

    def td_hist(m_oneshot: np.ndarray, lam: np.ndarray) -> np.ndarray:
        """Window to bring m_oneshot * exp(-lam w) down to beta (0 if already there, inf if never)."""
        with np.errstate(divide="ignore", invalid="ignore"):
            w = np.log(m_oneshot / beta) / lam
        w = np.where(m_oneshot <= beta, 0.0, w)
        return np.where((m_oneshot > beta) & (lam <= 0), np.inf, w)

    one = np.ones(DRAWS)
    td = {
        "declared, merged": np.full(DRAWS, math.log(1 / beta) / max(lam_meter, lam_samp)),
        "declared, independent": np.full(DRAWS, math.log(1 / beta) / (lam_meter + lam_samp)),
        # Merged {imagery, intelligence}: min(1 - p_sat, exp(-lam w)); the one-shot diversion check apart.
        "site-now, merged": np.where((1 - p_div) * (1 - p_sat["site-now"]) <= beta, 0.0,
                                     td_hist(1 - p_div, lam_h)),
        "site-now, independent": td_hist((1 - p_div) * (1 - p_sat["site-now"]), lam_h),
        "site-pause": td_hist((1 - p_div) * (1 - p_sat["site-pause"]), lam_h),
        "distributed": td_hist(1 - p_div, lam_h),
        "pool": td_hist(one, lam_h),
        "cloud": td_hist(one, lam_h),
        "distillation": td_hist(one, lam_h),
    }
    sat_opt = np.where(power["site-now"] >= sat_line, 1.0, 0.0)
    td_site_sat_opt = np.where((1 - p_div) * (1 - sat_opt) <= beta, 0.0, td_hist(1 - p_div, lam_h))

    def misses(w: float) -> dict:
        h = np.exp(-lam_h * w)
        m = {
            "declared": np.full(DRAWS, math.exp(-max(lam_meter, lam_samp) * w)),
            "site-now": (1 - p_div) * np.minimum(1 - p_sat["site-now"], h),
            "site-pause": (1 - p_div) * np.minimum(1 - p_sat["site-pause"], h),
            "distributed": (1 - p_div) * h,
            "pool": h, "cloud": h, "distillation": h,
        }
        evader = np.max(np.stack(list(m.values())), axis=0)
        # The memo's form: every channel watches the programme, independently.
        log10_memo = (np.log10(1 - p_div) + np.log10(np.maximum(1 - p_sat["site-now"], 1e-300))
                      - (lam_meter + lam_samp + lam_h) * w / math.log(10))
        site_indep = (1 - p_div) * (1 - p_sat["site-now"]) * h
        return {"paths": m, "evader": evader, "log10_memo": log10_memo, "site_indep": site_indep}

    w1, w2 = led["breakout-years"], led["org-hwp-tb"]
    m1, m2 = misses(w1), misses(w2)
    prop_b = float(np.mean(m1["log10_memo"] <= np.log10(m1["evader"]) + 1e-12))
    ratio = td["pool"] / td["declared, merged"]

    # ---- Numbers ---------------------------------------------------------------------------
    pct = f"{plo * 100:.0f}th"
    pct_hi = f"{phi * 100:.0f}th"
    res.number("e5-cases", n, unit="cases", fmt=",.0f",
               label="covert programmes and undeclared experiments in the case table")
    res.number("e5-events", fit["events"], unit="discoveries", fmt=",.0f",
               label="cases discovered from outside (the rest disclosed by the party, so censored)")
    res.number("e5-exposure-years", fit["exposure_years"], unit="programme-years", fmt=",.0f",
               label="programme-years from start to discovery or disclosure, summed over the cases")
    res.number("e5-hazard", lam_hat, unit="/yr", fmt=".3f",
               label="historical discovery rate of covert programmes, discoveries over programme-years (main coding)")
    res.number("e5-hazard-lo", fit["lo"], unit="/yr", fmt=".3f",
               label=f"discovery rate, {pct} percentile of the exact Poisson interval")
    res.number("e5-hazard-hi", fit["hi"], unit="/yr", fmt=".3f",
               label=f"discovery rate, {pct_hi} percentile of the exact Poisson interval")
    res.number("e5-hazard-boot-lo", q(boot_lam, plo), unit="/yr", fmt=".3f",
               label=f"discovery rate, {pct} percentile of resampling the cases")
    res.number("e5-hazard-boot-hi", q(boot_lam, phi), unit="/yr", fmt=".3f",
               label=f"discovery rate, {pct_hi} percentile of resampling the cases")
    res.number("e5-mean-years", 1 / lam_hat, unit="years", fmt=".1f",
               label="mean time to discovery at the fitted rate")
    res.number("e5-km-median-years", km, unit="years", fmt=".1f",
               label="Kaplan-Meier median time to discovery, disclosures censored")
    res.number("e5-weibull-shape", k_hat, fmt=".2f",
               label="Weibull shape of the time to discovery (1 is a constant rate; above 1, discovery likelier later)")
    res.number("e5-weibull-shape-lo", q(boot_k, plo), fmt=".2f",
               label=f"Weibull shape, {pct} percentile of resampling the cases")
    res.number("e5-weibull-shape-hi", q(boot_k, phi), fmt=".2f",
               label=f"Weibull shape, {pct_hi} percentile of resampling the cases")
    res.number("e5-weibull-lr-p", lr_p, fmt=".2f",
               label="p-value of the likelihood-ratio test of a Weibull against a constant rate")
    res.number("e5-o4-hazard", o4_hazard, unit="/yr", fmt=".3f",
               label="O4's seven programmes from the ledger, seven discoveries over their summed years (reproduces O4)")
    res.number("e5-o4-hazard-censored", o4_censored, unit="/yr", fmt=".3f",
               label="the same seven with self-disclosed South Africa censored, as a survival fit requires")
    res.number("e5-sens-min", min(sens), unit="/yr", fmt=".3f",
               label="lowest discovery rate across the sensitivity variants (cases and codings)")
    res.number("e5-sens-max", max(sens), unit="/yr", fmt=".3f",
               label="highest discovery rate across the sensitivity variants (cases and codings)")
    res.number("e5-loo-min", float(loo_vals.min()), unit="/yr", fmt=".3f",
               label="lowest discovery rate leaving out one case at a time")
    res.number("e5-loo-max", float(loo_vals.max()), unit="/yr", fmt=".3f",
               label="highest discovery rate leaving out one case at a time")
    res.number("e5-memo-over-hazard", led["org-memo-detect-rate"] / lam_hat, fmt=".1f",
               label="the memo's placeholder detection rate over the fitted historical rate")
    res.number("e5-memo-over-sens-max", led["org-memo-detect-rate"] / max(sens), fmt=".1f",
               label="the memo's placeholder rate over the highest rate any sensitivity variant gives")
    td_h = math.log(1 / beta) / lam_hat
    res.number("e5-td-hist-years", td_h, unit="years", fmt=",.0f",
               label="detection time at the prevention miss chance for a path only the historical channels see")
    res.number("e5-td-weibull-years", scale_hat * math.log(1 / beta) ** (1 / k_hat), unit="years", fmt=",.0f",
               label="the same detection time under the Weibull fit")

    def tdq(key: str, p: float) -> float:
        return q(td[key], p)

    res.number("e5-td-declared-days", tdq("declared, merged", 0.5) * YEAR, unit="days", fmt=".1f",
               label="detection time on the declared path (sampling and metering merged), at the prevention miss chance")
    res.number("e5-td-site-now-years", tdq("site-now, merged", 0.5), unit="years", fmt=",.0f",
               label="detection time, one undeclared site above the satellite line, median of the Monte Carlo")
    res.number("e5-td-site-now-years-lo", tdq("site-now, merged", plo), unit="years", fmt=",.0f",
               label=f"detection time, one undeclared site above the satellite line, {pct} percentile")
    res.number("e5-td-site-now-years-hi", tdq("site-now, merged", phi), unit="years", fmt=",.0f",
               label=f"detection time, one undeclared site above the satellite line, {pct_hi} percentile")
    res.number("e5-td-site-indep-years", tdq("site-now, independent", 0.5), unit="years", fmt=",.0f",
               label="detection time for the same site if imagery and intelligence were independent, median")
    res.number("e5-td-site-satopt-years", float(np.median(td_site_sat_opt)), unit="years", fmt=",.1f",
               label="detection time for the same site if satellites found every site above their line, median")
    res.number("e5-td-site-pause-years", tdq("site-pause", 0.5), unit="years", fmt=",.0f",
               label="detection time, one undeclared site sized for a pause's longest run (below the satellite line), median")
    res.number("e5-td-distributed-years", tdq("distributed", 0.5), unit="years", fmt=",.0f",
               label="detection time, smuggled chips spread over sites below the satellite line, median")
    res.number("e5-td-pool-years", tdq("pool", 0.5), unit="years", fmt=",.0f",
               label="detection time, the untraced chip pool (no acquisition to catch), median")
    res.number("e5-td-pool-years-lo", tdq("pool", plo), unit="years", fmt=",.0f",
               label=f"detection time, the untraced chip pool, {pct} percentile")
    res.number("e5-td-pool-years-hi", tdq("pool", phi), unit="years", fmt=",.0f",
               label=f"detection time, the untraced chip pool, {pct_hi} percentile")
    res.number("e5-td-ratio", float(np.median(ratio)), fmt=",.0f",
               label="detection time of the evader's best undeclared path over the declared path's, median")
    res.number("e5-pmiss-max-1y", float(np.median(m1["evader"])), fmt="%",
               label="chance a breakout is missed on the evader's best path over the memo's placeholder breakout time, with no response time")
    res.number("e5-pmiss-max-1y-lo", q(m1["evader"], plo), fmt="%",
               label=f"the same miss chance, {pct} percentile")
    res.number("e5-pmiss-max-1y-hi", q(m1["evader"], phi), fmt="%",
               label=f"the same miss chance, {pct_hi} percentile")
    res.number("e5-pmiss-max-2y", float(np.median(m2["evader"])), fmt="%",
               label="chance a breakout is missed on the evader's best path over the hardwired-pause horizon, with no response time")
    res.number("e5-memo-log10-miss-1y", float(np.median(m1["log10_memo"])), fmt=",.0f",
               label="log10 of the memo-style miss chance over the same time: the product over every channel, as if each watched the programme")
    res.number("e5-pmiss-site-merged-1y", float(np.median(m1["paths"]["site-now"])), fmt="%",
               label="miss chance for one undeclared site above the satellite line, imagery and intelligence merged, median")
    res.number("e5-pmiss-site-indep-1y", float(np.median(m1["site_indep"])), fmt="%",
               label="the same miss chance with imagery and intelligence independent; also the memo-style product over the channels that watch undeclared work")
    res.number("e5-product-le-max-share", prop_b, fmt="%",
               label="share of Monte Carlo draws in which the memo's product is at most the evader's miss (the proposition says all)")

    res.detail("date_rules", DATE_RULES)
    res.detail("cases", [
        {"id": r["id"], "start": r["start"], "found": r["found"], "outcome": r["outcome"],
         "channel": r["channel"], "years": round(float(t), 4), "discovered": int(e),
         "source": r["source"], "start_source": r["start_source"]}
        for r, t, e in zip(rows, main_t, main_e)
    ])
    res.detail("discovery_fit", {
        **fit, "km_median_years": km, "weibull": {"shape": k_hat, "scale_years": scale_hat,
                                                  "loglik": ll_w, "loglik_exponential": ll_exp},
        "bootstrap": {"draws": BOOT, "weibull_draws": int(boot_k.size)},
    })
    res.detail("channels_by_discovery", {
        ch: int(sum(1 for r in rows if r["channel"] == ch and r["outcome"] == "found"))
        for ch in sorted({r["channel"] for r in rows})
    })
    res.detail("sensitivity", {k: {kk: (round(vv, 6) if isinstance(vv, float) else vv) for kk, vv in v.items()}
                               for k, v in variants.items()})
    res.detail("leave_one_out", {k: round(float(v), 6) for k, v in loo.items()})
    res.detail("channels", {
        "chip sampling, per year": lam_samp, "power metering under the strongest disguise, per year": lam_meter,
        "diversion detection": "two-piece normal in log-odds through Epoch's median and 90% interval",
        "satellite": f"uniform [0, 1] above {sat_line} MW, zero below",
        "historical": "the case bootstrap of part 1, redrawn in every Monte Carlo draw",
        "merged groups": ["sampling with metering (the host's access)", "imagery with intelligence (tips)"],
        "facility power, MW": power,
    })
    res.detail("paths", {
        "declared": "registered chips at a metered declared site: sampling, metering",
        "site-now": "one undeclared site of smuggled chips for 1e26 FLOP over today's longest run: diversion, imagery, intelligence",
        "site-pause": "the same over a pause's longest run, below the satellite line: diversion, intelligence",
        "distributed": "smuggled chips spread over sites below the satellite line: diversion, intelligence",
        "pool": "untraced chips already held: intelligence",
        "cloud": "rented across providers; no sourced rate for customer checks: intelligence",
        "distillation": "queries to others' models; no sourced channel: intelligence",
    })
    res.detail("detection_time_years", {k: {"median": q(v, 0.5), "lo": q(v, plo), "hi": q(v, phi),
                                            "share_infinite": float(np.mean(np.isinf(v)))}
                                        for k, v in td.items()})
    res.detail("miss_by_path_1y", {k: q(v, 0.5) for k, v in m1["paths"].items()})
    res.detail("windows_years", {"memo_placeholder": w1, "hardwired_pause": w2})
    res.detail("monte_carlo", {"draws": DRAWS})
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
