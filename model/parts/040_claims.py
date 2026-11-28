"""Claims and their tests (research/04-claims.md).

Derives the few numbers the claims file needs that Part I did not: the time the whole projected
fleet needs to reach the hardwired-pause paper's breakout budget (the scale of the coalition share),
the untraced stock against the aggregate chip floor, how many locked organisms the elicitation
test needs, the staged runs the loop-gain test costs, and which pairs of pathways our grades
order (the grades are judgements, so the order is too). Inputs are in data/inputs/040-claims.toml.
Every id starts with claim-.
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

    # C7 (L4, C7.3): h_w is proportional to the breakout budget at fixed algorithms, so s* =
    # min(1, h_w / (m * T_r)) moves with the budget one for one. Two more points on that line: the
    # paper's frozen frontier, and the 1e26 FLOP run used throughout Part I.
    L.derive(
        "claim-whole-fleet-days-frozen",
        lambda q: q["claim-whole-fleet-horizon"] * q["claim-hwp-frozen-frontier"] / q["def-hwp-breakout-budget"] * 365.25,
        "claim-whole-fleet-horizon * claim-hwp-frozen-frontier / def-hwp-breakout-budget * 365.25",
        unit="days",
        fmt=",.0f",
        label="time the whole projected end-2026 fleet would need to reach a breakout budget equal to the hardwired-pause paper's frozen frontier, at fixed algorithms",
        note="h_w scales in proportion to the budget; same overhead and utilisation as claim-whole-fleet-horizon",
        defined_in=here(),
    )
    L.derive(
        "claim-whole-fleet-days-1e26",
        lambda q: q["claim-whole-fleet-horizon"] * q["phys-rahman-1e26-local"] / q["def-hwp-breakout-budget"] * 365.25,
        "claim-whole-fleet-horizon * phys-rahman-1e26-local / def-hwp-breakout-budget * 365.25",
        unit="days",
        fmt=".1f",
        label="time the whole projected end-2026 fleet would need to reach a 1e26 FLOP breakout budget, at fixed algorithms",
        note="h_w scales in proportion to the budget; same overhead and utilisation as claim-whole-fleet-horizon",
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

    # -----------------------------------------------------------------------------------------
    # C4: staged runs. Each round of the loop-gain test is run at every budget on the ladder, so
    # a count of rounds per budget costs that count times the ladder's budgets in staged runs.
    L.derive(
        "claim-c4-staged-runs",
        lambda q: q["claim-c4-budgets"] * q["claim-d2-rounds"],
        "claim-c4-budgets * claim-d2-rounds",
        unit="staged runs",
        fmt=",.0f",
        label="staged runs in the loop-gain test's fewest rounds, every round run at each budget on the ladder",
        defined_in=here(),
    )
    L.derive(
        "claim-c4-staged-runs-fav",
        lambda q: q["claim-c4-budgets"] * q["e4-fa-rounds-fav"],
        "claim-c4-budgets * e4-fa-rounds-fav",
        unit="staged runs",
        fmt=",.0f",
        label="staged runs E4 needs, with favourable rounds, to bring the upper-bound rule on r to 10% false alarms or fewer at the corrected median",
        defined_in=here(),
    )
    L.derive(
        "claim-c4-k-staged-runs-fav",
        lambda q: q["claim-c4-budgets"] * q["e4-k-fa-rounds-fav"],
        "claim-c4-budgets * e4-k-fa-rounds-fav",
        unit="staged runs",
        fmt=",.0f",
        label="staged runs E4 needs, with favourable rounds, to bring the K rule to 10% false alarms or fewer at the corrected median of r",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C12: which pairs of pathways our grades order. Each pathway has an ordinal grade per criterion
    # in data/inputs/040-claims.toml, read from the pathways table, each an assumption; a pair is
    # Pareto-ordered when one pathway's grade is higher on every criterion. The grades are
    # judgements, so the count is a property of our reading, not of evidence (L6, M8).
    pathways = ["rsi", "uc", "ds", "dist", "repl", "cl", "lha"]

    def fixed_pairs(criteria):
        def fn(q):
            grade = {(c, p): q[f"claim-c12-{c}-{p}"] for c in criteria for p in pathways}
            count = 0
            for i, a in enumerate(pathways):
                for b in pathways[i + 1:]:
                    if all(grade[c, a] > grade[c, b] for c in criteria) or all(
                        grade[c, b] > grade[c, a] for c in criteria
                    ):
                        count += 1
            return count

        return fn

    L.derive(
        "claim-c12-pairs",
        lambda q: len(pathways) * (len(pathways) - 1) / 2,
        "n * (n - 1) / 2 for the pathways chapter's n pathways",
        fmt=",.0f",
        label="pairs of pathways in the pathways chapter's ranking",
        defined_in=here(),
    )
    L.derive(
        "claim-c12-pareto-two",
        fixed_pairs(("effect", "hidden")),
        "pairs (a, b) with claim-c12-effect-a > claim-c12-effect-b and claim-c12-hidden-a > claim-c12-hidden-b",
        fmt=",.0f",
        label="pairs of pathways Pareto-ordered under our grades on the ranking's two criteria, effect on the line and how hard it is to see: one pathway graded higher on both",
        note="an ordinal reading of the pathways table whose grades are assumptions, so the count is a judgement too",
        defined_in=here(),
    )
    L.derive(
        "claim-c12-pareto-three",
        fixed_pairs(("effect", "hidden", "cheap")),
        "pairs (a, b) graded higher on effect, hidden and cheap alike",
        fmt=",.0f",
        label="the same count on the three criteria the red team read, cost of a limit included",
        note="checks the grades against the red team's independent reading (L4, C12.1)",
        defined_in=here(),
    )
