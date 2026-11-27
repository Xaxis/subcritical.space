"""Part I, opening chapter (research/01-anatomy.md): the six definitions restated after the survey.

Inputs are in data/inputs/010-definitions.toml (every id starts with "def-"). This module only
derives: unit conversions, checks that published figures follow from their stated inputs, the
margin the nuclear timeliness goals imply, and the monitoring that deterrence and prevention need
in Gan's response-window model.
"""

from __future__ import annotations

import math


def build(L, here) -> None:
    # Conventions
    L.derive(
        "def-days-per-month",
        lambda q: q["def-days-per-year"] / 12,
        "def-days-per-year / 12",
        unit="days",
        fmt=",.2f",
        label="days in an average month",
        defined_in=here(),
    )
    L.derive(
        "def-seconds-per-year",
        lambda q: q["def-days-per-year"] * q["def-seconds-per-day"],
        "def-days-per-year * def-seconds-per-day",
        unit="s",
        fmt="sig3",
        label="seconds in a year",
        defined_in=here(),
    )

    # D2: the lab rate triggers, METR's measurement, and the loop-gain calibration
    L.derive(
        "def-anthropic-example-doubled",
        lambda q: q["def-anthropic-example-baseline"] ** q["def-anthropic-rate-multiple"],
        "def-anthropic-example-baseline ^ def-anthropic-rate-multiple",
        unit="",
        fmt=",.0f",
        label="effective scale-up a year at twice the baseline rate of progress (Anthropic's worked example)",
        note="Two years of 9x progress in one year; the RSP's own figure is 81x.",
        defined_in=here(),
    )
    L.derive(
        "def-metr-aeci-ratio",
        lambda q: q["def-metr-aeci-after"] / q["def-metr-aeci-before"],
        "def-metr-aeci-after / def-metr-aeci-before",
        unit="",
        fmt=",.1f",
        label="ratio of the capability index's growth rate after and before the breakpoint",
        note="Reproduces METR's headline acceleration from its two fitted slopes.",
        defined_in=here(),
    )
    L.derive(
        "def-cunningham-threshold-check",
        lambda q: 1 / (q["def-cunningham-return"] * q["def-cunningham-eps-ca"]),
        "1 / (def-cunningham-return * def-cunningham-eps-ca)",
        fmt=",.2f",
        label="research productivity gain per ECI point at which the loop gain reaches 1",
        note="Reproduces Cunningham et al.'s threshold of 0.15 from their calibration.",
        defined_in=here(),
    )
    L.derive(
        "def-cunningham-loop-gain-illustration",
        lambda q: q["def-cunningham-return"]
        * q["def-cunningham-eps-rc-illustration"]
        * q["def-cunningham-eps-ca"],
        "def-cunningham-return * def-cunningham-eps-rc-illustration * def-cunningham-eps-ca",
        fmt=",.2f",
        label="loop gain implied by Cunningham et al.'s upper-end illustration (a reported 4x uplift taken at face value)",
        note="An upper-end illustration, not an estimate: the source calls the 4x uplift very likely an overestimate.",
        defined_in=here(),
    )
    L.derive(
        "def-r-lm-bottlenecked",
        lambda q: q["def-r-lm"] / q["def-r-bottleneck-divisor"],
        "def-r-lm / def-r-bottleneck-divisor",
        fmt=",.2f",
        label="returns to software research in language models after the compute-bottleneck correction",
        defined_in=here(),
    )
    L.derive(
        "def-r-lm-high-bottlenecked",
        lambda q: q["def-r-lm-high"] / q["def-r-bottleneck-divisor"],
        "def-r-lm-high / def-r-bottleneck-divisor",
        fmt=",.2f",
        label="upper end of the language-model interval after the compute-bottleneck correction",
        defined_in=here(),
    )
    L.derive(
        "def-r-cv-bottlenecked",
        lambda q: q["def-r-cv"] / q["def-r-bottleneck-divisor"],
        "def-r-cv / def-r-bottleneck-divisor",
        fmt=",.2f",
        label="returns to software research in computer vision after the compute-bottleneck correction",
        defined_in=here(),
    )

    # D1: matched cost in RE-Bench
    L.derive(
        "def-rebench-cost-ratio",
        lambda q: q["def-rebench-human-cost"] / q["def-rebench-agent-cost"],
        "def-rebench-human-cost / def-rebench-agent-cost",
        unit="",
        fmt=",.0f",
        label="how many times cheaper an agent's 8-hour RE-Bench run was than a human expert's",
        defined_in=here(),
    )

    # D3: published breakout figures reproduced from their stated inputs
    L.derive(
        "def-narrowpath-breakout-check",
        lambda q: 10 ** q["def-narrowpath-oom-gap"] / q["def-seconds-per-year"],
        "10 ^ def-narrowpath-oom-gap / def-seconds-per-year",
        unit="yr",
        fmt=",.2f",
        label="years in 10^8 seconds, the gap between A Narrow Path's compute and cluster limits",
        note="Reproduces A Narrow Path's 3.2-year breakout.",
        defined_in=here(),
    )
    L.derive(
        "def-hwp-fleet-check",
        lambda q: q["def-hwp-overhead"]
        * q["def-hwp-breakout-budget"]
        / (
            q["def-hwp-horizon"]
            * q["def-hwp-utilisation"]
            * q["def-hwp-h100e-rate"]
            * 1e12
            * q["def-seconds-per-year"]
        )
        / 1e6,
        "def-hwp-overhead * def-hwp-breakout-budget / (def-hwp-horizon * def-hwp-utilisation"
        " * def-hwp-h100e-rate * 1e12 * def-seconds-per-year) / 1e6",
        unit="million H100e",
        fmt="sig2",
        label="breakout fleet threshold recomputed from the hardwired-pause paper's inputs",
        note="Reproduces the paper's F_B of 180M H100e.",
        defined_in=here(),
    )
    L.derive(
        "def-hwp-fleet-over-global",
        lambda q: q["def-hwp-fleet-check"] / q["def-hwp-global-fleet"],
        "def-hwp-fleet-check / def-hwp-global-fleet",
        unit="",
        fmt=",.1f",
        label="the breakout fleet threshold as a multiple of the projected global fleet at year-end 2026",
        defined_in=here(),
    )
    L.derive(
        "def-gan-catchup-share",
        lambda q: q["def-gan-catchup-24"] / q["def-gan-catchup-start"],
        "def-gan-catchup-24 / def-gan-catchup-start",
        fmt="%",
        label="Gan's catch-up time after 24 months of pause, as a share of its starting value",
        defined_in=here(),
    )
    for suffix, months, what in (
        ("", "def-ho-halving-months", "central"),
        ("-fast", "def-ho-halving-fast", "fast end of the 95% CI"),
        ("-slow", "def-ho-halving-slow", "slow end of the 95% CI"),
    ):
        L.derive(
            f"def-ho-annual-multiple{suffix}",
            lambda q, m=months: 2 ** (12 / q[m]),
            f"2 ^ (12 / {months})",
            unit="",
            fmt=",.1f",
            label=f"yearly fall in compute needed for a fixed language-model performance, {what}",
            defined_in=here(),
        )

    # D4: the margin m that the IAEA timeliness goals imply (conversion time / detection goal)
    pairs = (
        ("metal-low", "def-iaea-conv-metal-low", "def-iaea-goal-unirr", True, "metal, low end"),
        ("metal-high", "def-iaea-conv-metal-high", "def-iaea-goal-unirr", True, "metal, high end"),
        ("irr-low", "def-iaea-conv-irr-low", "def-iaea-goal-irr", False, "irradiated fuel, low end"),
        ("irr-high", "def-iaea-conv-irr-high", "def-iaea-goal-irr", False, "irradiated fuel, high end"),
        ("leu-low", "def-iaea-conv-leu-low", "def-iaea-goal-indirect", False, "LEU and thorium, low end"),
        ("leu-high", "def-iaea-conv-leu-high", "def-iaea-goal-indirect", False, "LEU and thorium, high end"),
    )
    for name, conv, goal, in_days, what in pairs:
        if in_days:
            fn = lambda q, c=conv, g=goal: q[c] / (q[g] * q["def-days-per-month"])
            formula = f"{conv} / ({goal} * def-days-per-month)"
        else:
            fn = lambda q, c=conv, g=goal: q[c] / q[g]
            formula = f"{conv} / {goal}"
        L.derive(
            f"def-iaea-m-{name}",
            fn,
            formula,
            fmt=",.2f",
            label=f"margin implied by IAEA timeliness (conversion time over detection goal), {what}",
            defined_in=here(),
        )

    # D4: deterrence against prevention in Gan's model. A breakout is caught inside the window w
    # with probability 1 - exp(-rate * w). Deterrence needs rate >= xi / w; holding breakout
    # success below beta needs rate >= ln(1 / beta) / w.
    L.derive(
        "def-gan-deter-rate",
        lambda q: q["def-gan-xi"] / q["def-gan-window"],
        "def-gan-xi / def-gan-window",
        unit="/month",
        fmt=",.4f",
        label="monitoring rate (findings a month) that just deters a breakout in Gan's illustrative calibration",
        defined_in=here(),
    )
    L.derive(
        "def-gan-deter-detect",
        lambda q: 1 - math.exp(-q["def-gan-xi"]),
        "1 - exp(-def-gan-xi)",
        fmt="%",
        label="chance of detection inside the window at the deterrence threshold",
        defined_in=here(),
    )
    L.derive(
        "def-gan-deter-success",
        lambda q: math.exp(-q["def-gan-xi"]),
        "exp(-def-gan-xi)",
        fmt="%",
        label="chance a breakout still succeeds at the deterrence threshold",
        defined_in=here(),
    )
    L.derive(
        "def-gan-prevent-rate",
        lambda q: math.log(1 / q["def-prevent-beta"]) / q["def-gan-window"],
        "ln(1 / def-prevent-beta) / def-gan-window",
        unit="/month",
        fmt=",.2f",
        label="monitoring rate that holds breakout success to the tolerated chance in the same window",
        defined_in=here(),
    )
    L.derive(
        "def-gan-prevent-multiple",
        lambda q: q["def-gan-prevent-rate"] / q["def-gan-deter-rate"],
        "def-gan-prevent-rate / def-gan-deter-rate",
        unit="",
        fmt=",.1f",
        label="how much more monitoring prevention needs than deterrence, same window",
        defined_in=here(),
    )
    L.derive(
        "def-placeholder-detect-time",
        lambda q: math.log(1 / q["def-prevent-beta"])
        / (q["inspections-per-year"] * q["detect-prob-per-inspection"]),
        "ln(1 / def-prevent-beta) / (inspections-per-year * detect-prob-per-inspection)",
        unit="yr",
        fmt=",.1f",
        label="time for the memo's placeholder channel to reach the tolerated miss chance (detection only, no response)",
        note="Uses the core placeholder rates, which are assumptions.",
        defined_in=here(),
    )

    # D5: elicitation budget moves measured capability
    L.derive(
        "def-mlebench-ratio",
        lambda q: q["def-mlebench-pass8"] / q["def-mlebench-pass1"],
        "def-mlebench-pass8 / def-mlebench-pass1",
        unit="",
        fmt=",.1f",
        label="MLE-bench medal rate at pass@8 over pass@1",
        defined_in=here(),
    )
