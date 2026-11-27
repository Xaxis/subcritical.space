"""Claims and their tests (research/04-claims.md).

Derives the few numbers the claims file needs that Part I did not: the time the whole projected
fleet needs to reach the hardwired-pause paper's breakout budget (the scale of the coalition share),
the untraced stock against the aggregate chip floor, and how many locked organisms the elicitation
test needs. Inputs are in data/inputs/040-claims.toml. Every id starts with claim-.
"""

from __future__ import annotations

import math


def build(L, here) -> None:
    # The detection time for undeclared work at the historical discovery rate is path-covert-td-prevent,
    # derived in model/parts/020_pathways.py; the claims file cites it rather than deriving it twice.

    # -----------------------------------------------------------------------------------------
    # C7: the coalition share. The hardwired-pause fleet threshold scales as one over its horizon,
    # so the horizon at which it equals the projected global fleet is the time the whole fleet
    # needs to reach the breakout budget at fixed algorithms. A coalition with share s needs that
    # time divided by s.
    L.derive(
        "claim-whole-fleet-horizon",
        lambda q: q["def-hwp-horizon"] * q["def-hwp-fleet-over-global"],
        "def-hwp-horizon * def-hwp-fleet-over-global",
        unit="years",
        fmt=".1f",
        label="time the whole projected end-2026 fleet would need to reach the hardwired-pause paper's overt breakout budget, at fixed algorithms",
        note="uses that paper's budget, research overhead and utilisation, all assumptions of the paper",
        defined_in=here(),
    )

    # C8: the untraced stock against the aggregate chip floor for a 1e26 FLOP run.
    L.derive(
        "claim-pool-over-floor-now",
        lambda q: q["org-smuggled-cum"] / q["phys-floor-chips-1e26-now"],
        "org-smuggled-cum / phys-floor-chips-1e26-now",
        fmt=",.0f",
        label="median compute smuggled into one country through 2025, as a multiple of the aggregate chip floor for a 1e26 FLOP run over today's longest sensible run",
        defined_in=here(),
    )
    L.derive(
        "claim-pool-over-floor-pause",
        lambda q: q["org-smuggled-cum"] / q["phys-floor-chips-1e26-pause"],
        "org-smuggled-cum / phys-floor-chips-1e26-pause",
        fmt=",.0f",
        label="the same stock as a multiple of the aggregate chip floor for a 1e26 FLOP run over a pause's longest sensible run",
        defined_in=here(),
    )

    # C5: with no misses among n locked organisms, the one-sided upper bound on the miss rate at
    # confidence c is 1 - (1 - c)^(1/n); it reaches the target t once n >= ln(1 - c) / ln(1 - t).
    L.derive(
        "claim-d5-organisms",
        lambda q: math.ceil(math.log(1 - q["claim-confidence"]) / math.log(1 - q["claim-d5-miss-target"])),
        "ceil(ln(1 - claim-confidence) / ln(1 - claim-d5-miss-target))",
        unit="organisms",
        fmt=",.0f",
        label="locked organisms per budget, with none missed, for the one-sided upper bound on the miss rate to reach its target",
        note="exact binomial bound with zero misses; any miss raises the number needed",
        defined_in=here(),
    )
