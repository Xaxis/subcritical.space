#!/usr/bin/env python3
"""E24: how long the arms-control record took from a confirmed finding to an effective response.

C1's line needs T_resp, the time from a confirmed finding to an effective halt, and C7's coalition
share is derived from it. No regime has measured it in drills, so this compiles the record case by
case in tools/exp/data/e24_response_latency.csv: each finding (a special inspection request, a
nuclear test detected, a covert plant exposed, a chemical attack attributed), its date and source,
and every dated response the sources give, with its type:

  statement   a formal finding, demand, referral or demarche with no enforcement (IAEA Board,
              Security Council without sanctions, diplomatic notes, an inspection visit)
  sanctions   a measure that imposes costs (Security Council sanctions, suspended supplies)
  halt        the first physical halt: a verified shutdown, removal, destruction or agreed suspension
  military    a strike
  exit        the violator's own move to leave the regime (withdrawal, expelling inspectors)

Findings with no halt by the end of what the sources cover are censored there. For each type the
script takes the first response per finding and reports the empirical median with a case
bootstrap; for halts, the Kaplan-Meier median and a log-normal fitted with censoring, the share of
findings never halted, and the share of halts later reversed.

The halt analysis leads with findings made while the party was still in the treaty it was found
violating. A finding after the party's withdrawal took effect (the date the source gives, in the
exit_effective column) answers a breakout already completed and an exit already made, not a
breakout in progress under the regime, which is what C1's T_resp is about: the DPRK's nuclear
tests from 2006 on. They still breached the Security Council's demands, so they stay in the table
and their figures are reported apart, with every finding pooled. A second sensitivity keeps only
the first finding per programme, since one state's repeated findings dominate the table. The record
is thin (eight findings from six programmes in the lead halt analysis), and the script says what it
does and does not support rather than forcing a fit.

All randomness comes from one numpy generator seeded with SEED. No data are fetched: the input is
the hand-compiled case table, and ledger values read from data/numbers.json.

  .venv/bin/python tools/exp/e24_response_latency.py      (CPU, seconds; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np
from scipy import optimize, special, stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results  # noqa: E402

SEED = 20261127
CASES = Path(__file__).resolve().parent / "data" / "e24_response_latency.csv"
BOOT = 10_000
BOOT_FIT = 2_000  # bootstrap draws for the censored log-normal (each is an optimisation)
YEAR = 365.25
TYPES = ("statement", "sanctions", "halt", "military", "exit")
LEDGER_IDS = ["claim-confidence", "org-dprk-withdrawal-days", "org-miri-withdrawal", "org-hwp-tb"]

DATE_RULES = {
    "YYYY-MM-DD": "that day",
    "YYYY-MM-late": "the 25th of the month",
    "YYYY-MM": "the 15th of the month",
    "YYYY-MM/MM": "the first day of the second month (the midpoint of the two)",
}


def to_date(text: str) -> date:
    t = text.strip()
    if m := re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", t):
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if m := re.fullmatch(r"(\d{4})-(\d{2})-late", t):
        return date(int(m.group(1)), int(m.group(2)), 25)
    if m := re.fullmatch(r"(\d{4})-(\d{2})/(\d{2})", t):
        return date(int(m.group(1)), int(m.group(3)), 1)
    if m := re.fullmatch(r"(\d{4})-(\d{2})", t):
        return date(int(m.group(1)), int(m.group(2)), 15)
    raise ValueError(f"no date rule for {text!r}")


def days(a: str, b: str) -> int:
    return to_date(b).toordinal() - to_date(a).toordinal()


def km_median(t: np.ndarray, e: np.ndarray) -> float:
    """Kaplan-Meier median; inf if the curve never falls to one half."""
    order = np.lexsort((-e, t))
    s, at_risk = 1.0, len(t)
    for i in order:
        if e[i]:
            s *= 1 - 1 / at_risk
            if s <= 0.5:
                return float(t[i])
        at_risk -= 1
    return float("inf")


def lognormal_fit(t: np.ndarray, e: np.ndarray) -> tuple[float, float]:
    """mu and sigma of ln(days), by maximum likelihood with right censoring."""
    x = np.log(t)

    half_log_2pi = 0.5 * math.log(2 * math.pi)

    def nll(p):
        mu, s = p[0], math.exp(p[1])
        z = (x - mu) / s
        logpdf = -0.5 * z * z - half_log_2pi - math.log(s) - x
        return -float(np.sum(e * logpdf) + np.sum((1 - e) * special.log_ndtr(-z)))

    ev = x[e == 1]
    x0 = np.array([ev.mean() if ev.size else x.mean(), math.log(max(ev.std(), 0.3) if ev.size > 1 else 1.0)])
    r = optimize.minimize(nll, x0, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
    return float(r.x[0]), float(math.exp(r.x[1]))


def main() -> int:
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    led = {i: numbers[i]["value"] for i in LEDGER_IDS}
    res = Results("E24", "e24_response_latency", seed=SEED)
    res.detail("ledger_inputs", led)
    conf = led["claim-confidence"]
    plo, phi = (1 - conf) / 2, 1 - (1 - conf) / 2
    gen = np.random.default_rng(SEED)

    with CASES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 20:
        raise SystemExit(f"{CASES.name} has {len(rows)} rows; expected the full table")
    for r in rows:
        if r["response_type"] not in TYPES:
            raise SystemExit(f"{r['case']}: unknown response type {r['response_type']!r}")
        if bool(r["response_date"]) == bool(r["censored_at"]):
            raise SystemExit(f"{r['case']}: give a response date or a censoring date, not both")
        if r["censored_at"] and r["response_type"] != "halt":
            raise SystemExit(f"{r['case']}: only a halt may be censored")

    findings = {}
    for r in rows:
        findings.setdefault(r["case"], {"programme": r["programme"], "date": r["finding_date"],
                                        "finding": r["finding"], "source": r["finding_source"]})
    first = defaultdict(dict)  # first[type][case] = (days, event, row)
    table = []
    for r in rows:
        if r["response_date"]:
            d, ev = days(r["finding_date"], r["response_date"]), 1
        else:
            d, ev = days(r["finding_date"], r["censored_at"]), 0
        if d < 0:
            raise SystemExit(f"{r['case']}: response before finding")
        table.append({"case": r["case"], "type": r["response_type"], "response": r["response"],
                      "days": d, "event": ev, "source": r["source"], "where": r["where"]})
        cur = first[r["response_type"]].get(r["case"])
        if cur is None or (ev, -d) > (cur[1], -cur[0]):
            first[r["response_type"]][r["case"]] = (d, ev, r)

    def empirical(kind: str, cases=None) -> dict:
        items = [(c, v) for c, v in sorted(first[kind].items()) if cases is None or c in cases]
        d = np.array([v[0] for _, v in items], float)
        if d.size == 0:
            return {"n": 0}
        b = np.median(d[gen.integers(0, d.size, (BOOT, d.size))], axis=1)
        return {"n": int(d.size), "median": float(np.median(d)), "lo": float(np.quantile(b, plo)),
                "hi": float(np.quantile(b, phi)), "min": float(d.min()), "max": float(d.max()),
                "days": {c: int(v[0]) for c, v in items}}

    statement = empirical("statement")
    sanctions = empirical("sanctions")
    military = empirical("military")
    exit_ = empirical("exit")

    # Halts: censored where none came.
    def halt_stats(cases=None, fit=True) -> dict:
        items = [(c, v) for c, v in sorted(first["halt"].items()) if cases is None or c in cases]
        t = np.array([v[0] for _, v in items], float)
        e = np.array([v[1] for _, v in items], int)
        out = {"n": int(t.size), "halted": int(e.sum()), "km_median_days": km_median(t, e),
               "median_if_halted_days": float(np.median(t[e == 1])) if e.any() else float("nan"),
               "share_never": float(1 - e.mean())}
        idx = gen.integers(0, t.size, (BOOT, t.size))
        km_b = np.array([km_median(t[i], e[i]) for i in idx])
        # No interpolation: an upper percentile may be unbounded (the curve never reaches one half).
        finite = lambda v: float(v) if np.isfinite(v) else None  # noqa: E731
        out["km_lo_days"] = finite(np.quantile(km_b, plo, method="inverted_cdf"))
        out["km_hi_days"] = finite(np.quantile(km_b, phi, method="inverted_cdf"))
        out["km_share_inf"] = float(np.mean(np.isinf(km_b)))
        out["km_median_days"] = finite(out["km_median_days"])
        if fit:
            mu, s = lognormal_fit(t, e)
            out["lognormal"] = {"mu": mu, "sigma": s, "median_days": math.exp(mu),
                                "q05_days": math.exp(mu + s * stats.norm.ppf(plo)),
                                "q95_days": math.exp(mu + s * stats.norm.ppf(phi))}
            med_b = []
            for i in idx[:BOOT_FIT]:
                if e[i].sum() >= 2:
                    med_b.append(math.exp(lognormal_fit(t[i], e[i])[0]))
            med_b = np.array(med_b)
            out["lognormal"]["median_lo_days"] = float(np.quantile(med_b, plo))
            out["lognormal"]["median_hi_days"] = float(np.quantile(med_b, phi))
            out["lognormal"]["bootstrap_draws"] = int(med_b.size)
        out["days"] = {c: [int(v[0]), int(v[1])] for c, v in items}
        return out

    # Findings after the party's withdrawal from the treaty took effect, by programme.
    exit_effective = {}
    for r in rows:
        if r["exit_effective"]:
            if r["response_type"] != "exit":
                raise SystemExit(f"{r['case']}: an effective withdrawal date belongs on an exit row")
            d = to_date(r["exit_effective"])
            p = r["programme"]
            exit_effective[p] = min(d, exit_effective.get(p, d))
    after_exit = {c for c, f in findings.items()
                  if f["programme"] in exit_effective and to_date(f["date"]) >= exit_effective[f["programme"]]}
    in_treaty = set(findings) - after_exit

    halt = halt_stats(in_treaty)
    halt_all = halt_stats(fit=False)
    first_finding = {}
    for c, f in sorted(findings.items(), key=lambda kv: to_date(kv[1]["date"])):
        first_finding.setdefault(f["programme"], c)
    firsts = set(first_finding.values())
    halt_first = halt_stats(firsts, fit=False)
    statement_first = empirical("statement", firsts)

    halted_all = [v for v in first["halt"].values() if v[1] == 1]
    halted = [v for v in halted_all if v[2]["case"] in in_treaty]
    reversed_ = [v for v in halted if v[2]["reversed_date"]]
    reversed_all = [v for v in halted_all if v[2]["reversed_date"]]
    durable = {v[2]["case"]: (days(v[2]["response_date"], v[2]["reversed_date"]) if v[2]["reversed_date"] else None)
               for v in halted_all}

    # ---- Numbers ---------------------------------------------------------------------------
    if None in (halt["km_median_days"], halt_all["km_median_days"], halt_first["km_median_days"]):
        raise SystemExit("fewer than half the findings are ever halted: the Kaplan-Meier median does not exist")
    pct, pct_hi = f"{plo * 100:.0f}th", f"{phi * 100:.0f}th"
    yr = lambda d: d / YEAR  # noqa: E731
    res.number("e24-findings", len(findings), unit="findings", fmt=",.0f",
               label="confirmed findings in the response table")
    res.number("e24-programmes", len({f["programme"] for f in findings.values()}), unit="programmes", fmt=",.0f",
               label="distinct programmes those findings concern")
    res.number("e24-responses", sum(1 for r in table if r["event"]), unit="responses", fmt=",.0f",
               label="dated responses in the table")
    res.number("e24-statement-median-days", statement["median"], unit="days", fmt=",.0f",
               label="median days from a finding to its first formal statement, demand or referral")
    res.number("e24-statement-median-days-lo", statement["lo"], unit="days", fmt=",.0f",
               label=f"the same median, {pct} percentile of resampling the findings")
    res.number("e24-statement-median-days-hi", statement["hi"], unit="days", fmt=",.0f",
               label=f"the same median, {pct_hi} percentile of resampling the findings")
    res.number("e24-statement-max-days", statement["max"], unit="days", fmt=",.0f",
               label="longest wait from a finding to its first formal statement in the table")
    res.number("e24-sanctions-median-days", sanctions["median"], unit="days", fmt=",.0f",
               label="median days from a finding to its first sanctions")
    res.number("e24-sanctions-median-days-lo", sanctions["lo"], unit="days", fmt=",.0f",
               label=f"the same median, {pct} percentile of resampling the findings")
    res.number("e24-sanctions-median-days-hi", sanctions["hi"], unit="days", fmt=",.0f",
               label=f"the same median, {pct_hi} percentile of resampling the findings")
    res.number("e24-halt-findings", halt["n"], unit="findings", fmt=",.0f",
               label="findings in the halt analysis: made while the party was in the treaty, with sources that say whether a halt followed")
    res.number("e24-halt-share-never", halt["share_never"], fmt="%",
               label="share of those findings followed by no halt by the end of what the sources cover")
    res.number("e24-halt-median-if-halted-years", yr(halt["median_if_halted_days"]), unit="years", fmt=".1f",
               label="median years from a finding to the first halt, among those findings that were halted (the unhalted left out)")
    res.number("e24-halt-km-median-years", yr(halt["km_median_days"]), unit="years", fmt=".1f",
               label="Kaplan-Meier median years from a finding to a halt, findings never halted censored")
    res.number("e24-halt-km-median-years-lo", yr(halt["km_lo_days"]), unit="years", fmt=".1f",
               label=f"the same median, {pct} percentile of resampling the findings")
    res.number("e24-halt-km-share-unbounded", halt["km_share_inf"], fmt="%",
               label="share of resampled tables in which fewer than half the findings are ever halted (no median)")
    res.number("e24-halt-lognormal-median-years", yr(halt["lognormal"]["median_days"]), unit="years", fmt=".1f",
               label="median years to a halt of a log-normal fitted with censoring")
    res.number("e24-halt-lognormal-median-years-lo", yr(halt["lognormal"]["median_lo_days"]), unit="years", fmt=".1f",
               label=f"the log-normal median, {pct} percentile of resampling the findings")
    res.number("e24-halt-lognormal-median-years-hi", yr(halt["lognormal"]["median_hi_days"]), unit="years", fmt=".1f",
               label=f"the log-normal median, {pct_hi} percentile of resampling the findings")
    res.number("e24-halt-after-exit", len(after_exit & set(first["halt"])), unit="findings", fmt=",.0f",
               label="findings made after the party's withdrawal from the treaty took effect, left out of the halt analysis")
    res.number("e24-halt-findings-all", halt_all["n"], unit="findings", fmt=",.0f",
               label="findings with a halt record, including those after the party's withdrawal")
    res.number("e24-halt-share-never-all", halt_all["share_never"], fmt="%",
               label="share never halted, every finding including those after the party's withdrawal")
    res.number("e24-halt-km-median-years-all", yr(halt_all["km_median_days"]), unit="years", fmt=".1f",
               label="Kaplan-Meier median years to a halt, every finding including those after the party's withdrawal")
    res.number("e24-halt-first-km-median-years", yr(halt_first["km_median_days"]), unit="years", fmt=".1f",
               label="Kaplan-Meier median years to a halt, first finding per programme only")
    res.number("e24-halt-first-share-never", halt_first["share_never"], fmt="%",
               label="share never halted, first finding per programme only")
    res.number("e24-halt-share-reversed", len(reversed_) / len(halted), fmt="%",
               label="share of halts in the halt analysis later reversed or shown incomplete in the same sources")
    res.number("e24-halt-min-days", min(v[0] for v in halted_all), unit="days", fmt=",.0f",
               label="fastest halt after a finding in the table")
    res.number("e24-military-max-days", military["max"], unit="days", fmt=",.0f",
               label="slowest of the strikes in the table, days after the attack they answered")
    res.number("e24-exit-min-days", exit_["min"], unit="days", fmt=",.0f",
               label="fastest exit by the violator after a finding (its withdrawal notice)")
    res.number("e24-halt-over-exit", halt["median_if_halted_days"] / exit_["min"], fmt=",.0f",
               label="median time to a halt, among findings halted, over the violator's fastest exit")
    if exit_["min"] != led["org-dprk-withdrawal-days"]:
        raise SystemExit("the fastest exit no longer matches the ledger's DPRK withdrawal notice; check the table")
    res.number("e24-halt-km-over-hwp", yr(halt["km_median_days"]) / led["org-hwp-tb"], fmt=".1f",
               label="Kaplan-Meier median time to a halt over the reaction horizon the hardwired-pause paper chooses")
    res.number("e24-miri-notice-over-halt", led["org-miri-withdrawal"] / (halt["median_if_halted_days"] / YEAR * 12),
               fmt=".1f", label="MIRI's draft withdrawal notice over the median time to a halt among findings halted")

    res.detail("date_rules", DATE_RULES)
    res.detail("types", {"statement": "formal finding, demand, referral or demarche, no enforcement",
                         "sanctions": "a measure imposing costs", "halt": "first physical halt",
                         "military": "a strike", "exit": "the violator leaves the regime"})
    res.detail("findings", findings)
    res.detail("responses", table)
    res.detail("first_response", {"statement": statement, "sanctions": sanctions, "military": military,
                                  "exit": exit_, "statement_first_finding_only": statement_first})
    res.detail("halt", {**halt, "cases": sorted(in_treaty & set(first["halt"]))})
    res.detail("halt_after_exit", {"exit_effective": {p: d.isoformat() for p, d in exit_effective.items()},
                                   "findings": sorted(after_exit)})
    res.detail("halt_all_findings", {**halt_all, "share_reversed": len(reversed_all) / len(halted_all),
                                     "median_if_halted_years": yr(halt_all["median_if_halted_days"])})
    res.detail("halt_first_finding_only", {**halt_first, "cases": sorted(firsts)})
    res.detail("halt_days_until_reversed", durable)
    res.detail("bootstrap", {"draws": BOOT, "lognormal_draws": BOOT_FIT})
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
