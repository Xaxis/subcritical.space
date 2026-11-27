#!/usr/bin/env python3
"""E2: how fast AI agents' task horizons grow, refitted from METR's published results.

METR publishes each frontier model's 50% and 80% time horizon (the length of task, timed on human
experts, at which the agent succeeds half or 80% of the time) and its own fit of the doubling time.
This refits that trend independently from the same file, so the research does not take the
headline on trust, and records what the protocol needs from it: the doubling time with an
interval, how much shorter the 80% horizon is than the 50%, whether that ratio is stable,
shrinking or growing, and the latest frontier horizon.

Method, following METR's stated rule for its 2023-on fit: frontier (is_sota) models released from
2023 on, excluding points whose central 50% horizon exceeds 16 hours; ordinary least squares of
ln(horizon) on release date. The interval here resamples models (10,000 draws, seeded) and, in
each draw, each model's horizon within its published 95% interval (log-normal). METR's own interval
resamples tasks and runs, which the summary file cannot support, so the two intervals measure
different things; both are recorded.

  .venv/bin/python tools/exp/e02_time_horizons.py      (CPU, seconds; see tools/exp/README.md)
"""

from __future__ import annotations

import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import Results, fetch  # noqa: E402

URL = "https://metr.org/assets/benchmark_results_1_1.yaml"
SEED = 20261127
DRAWS = 10_000
CUTOFF_MIN = 16 * 60  # METR excludes central p50 estimates above 16 hours from its fit
SINCE = date(2023, 1, 1)
Z95 = 1.959963984540054


def fit(days: np.ndarray, log_h: np.ndarray) -> float:
    """Slope of ln(horizon) per day, by least squares."""
    d = days - days.mean()
    return float((d * (log_h - log_h.mean())).sum() / (d * d).sum())


def doubling(slope: float) -> float:
    return math.log(2) / slope


def main() -> int:
    res = Results("E2", "e02_time_horizons", seed=SEED)
    path = fetch(URL, "metr/benchmark_results_1_1.yaml", res, what="METR-Horizon-v1.1 results")
    data = yaml.safe_load(path.read_text())

    rows = []
    for name, r in sorted(data["results"].items()):
        m = r["metrics"]
        released = r["release_date"]
        if isinstance(released, str):
            released = date.fromisoformat(released)
        p50, p80 = m["p50_horizon_length"], m["p80_horizon_length"]
        rows.append(
            {
                "model": name,
                "released": released.isoformat(),
                "sota": bool(m.get("is_sota")),
                "p50": p50["estimate"],
                "p50_lo": p50["ci_low"],
                "p50_hi": p50["ci_high"],
                "p80": p80["estimate"],
            }
        )
    used = [
        r
        for r in rows
        if r["sota"] and date.fromisoformat(r["released"]) >= SINCE and r["p50"] <= CUTOFF_MIN
    ]
    if len(used) < 5:
        raise SystemExit(f"only {len(used)} frontier points since {SINCE}; the file changed shape")

    t0 = date(2023, 1, 1).toordinal()
    days = np.array([date.fromisoformat(r["released"]).toordinal() - t0 for r in used], float)
    log_p50 = np.log([r["p50"] for r in used])
    log_p80 = np.log([r["p80"] for r in used])
    slope50 = fit(days, log_p50)
    slope80 = fit(days, log_p80)

    # The interval: resample models, and each model's horizon within its own published interval.
    gen = np.random.default_rng(SEED)
    lo = np.log([max(r["p50_lo"], 1e-9) for r in used])
    hi = np.log([r["p50_hi"] for r in used])
    sd = (hi - lo) / (2 * Z95)
    n = len(used)
    log_ratio = log_p50 - log_p80
    boots, ratio_slopes = [], []
    for _ in range(DRAWS):
        pick = gen.integers(0, n, n)
        if np.unique(days[pick]).size < 2:
            continue
        noisy = log_p50[pick] + gen.normal(0, sd[pick])
        s = fit(days[pick], noisy)
        if s > 0:
            boots.append(doubling(s))
        ratio_slopes.append(fit(days[pick], log_ratio[pick]))
    boots = np.sort(np.array(boots))
    ratio_slopes = np.sort(np.array(ratio_slopes))
    # The 50%-to-80% ratio's trend, as a change per year: stable if its interval spans zero.
    per_year = lambda s: math.exp(s * 365.25)  # noqa: E731
    ratio_trend = per_year(fit(days, log_ratio))
    ratio_lo = per_year(float(np.quantile(ratio_slopes, 0.025)))
    ratio_hi = per_year(float(np.quantile(ratio_slopes, 0.975)))
    ratio_verdict = "growing" if ratio_lo > 1 else "shrinking" if ratio_hi < 1 else "stable"
    q = lambda p: float(np.quantile(boots, p))  # noqa: E731

    metr = data["doubling_time_in_days"]["from_2023_on"]
    ratio = np.array([r["p50"] / r["p80"] for r in used])
    latest = max(rows, key=lambda r: (r["released"], r["p50"]) if r["sota"] else ("", 0))

    res.number("e2-points", n, unit="models", fmt=",.0f",
               label="frontier models in the refit (released 2023 on, central 50% horizon up to 16 hours)")
    res.number("e2-doubling-p50", doubling(slope50), unit="days", fmt=",.0f",
               label="doubling time of the frontier 50% time horizon, our refit of METR's data")
    res.number("e2-doubling-p50-lo", q(0.025), unit="days", fmt=",.0f",
               label="doubling time, 2.5th percentile of our model-and-interval resampling")
    res.number("e2-doubling-p50-hi", q(0.975), unit="days", fmt=",.0f",
               label="doubling time, 97.5th percentile of our model-and-interval resampling")
    res.number("e2-doubling-p80", doubling(slope80), unit="days", fmt=",.0f",
               label="doubling time of the frontier 80% time horizon, our refit")
    res.number("e2-metr-doubling", metr["point_estimate"], unit="days", fmt=",.0f",
               label="METR's own doubling time for the same points, as published in the file")
    res.number("e2-refit-over-metr", doubling(slope50) / metr["point_estimate"], fmt=".2f",
               label="our refitted doubling time over METR's published one (1 means the refit reproduces it)")
    res.number("e2-p50-over-p80", float(np.median(ratio)), fmt=".1f",
               label="median ratio of a frontier model's 50% horizon to its 80% horizon")
    res.number("e2-ratio-trend", ratio_trend, fmt=".2f",
               label=f"yearly factor by which the 50%-to-80% horizon ratio changes ({ratio_verdict}: its interval {'spans' if ratio_verdict == 'stable' else 'excludes'} 1)")
    res.number("e2-ratio-trend-lo", ratio_lo, fmt=".2f",
               label="yearly factor of the ratio's change, 2.5th percentile of resampling models")
    res.number("e2-ratio-trend-hi", ratio_hi, fmt=".2f",
               label="yearly factor of the ratio's change, 97.5th percentile of resampling models")
    res.number("e2-latest-p50", latest["p50"], unit="min", fmt=",.0f",
               label=f"50% time horizon of the latest frontier model in the file ({latest['model']}, {latest['released']})",
               note="above the 16-hour cut if so, which is why it is not in the fit")
    res.detail("points", used)
    res.detail("all_models", rows)
    res.detail("metr_published", metr)
    res.detail("resampling", {"draws": DRAWS, "kept": int(boots.size), "median": q(0.5)})
    res.detail("ratio_verdict", ratio_verdict)
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
