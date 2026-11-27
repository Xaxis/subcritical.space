"""Part I, 6: the pathways, ranked by evidence (research/02-pathways.md).

Five numbers the ranking needs that no chapter computed. Each is arithmetic on numbers earlier
parts defined; this part adds no inputs of its own, so it has no data/inputs/020-pathways.toml.
"""

from __future__ import annotations

import math

SECONDS_PER_DAY = 86_400


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # Recursive self-improvement. On D2's round-on-round definition, a constant gain g below 1
    # makes the rounds add up to 1 / (1 - g) times the first round's gain: the subcritical
    # multiplication of a pile below k = 1. An illustration only: in the dynamical chapter's
    # growth-law form, a gain below 1 slows the rate without capping the level.

    L.derive(
        "path-rsi-multiplier-median",
        lambda q: 1 / (1 - q["dyn-r-lm-corrected"]),
        "1 / (1 - dyn-r-lm-corrected)",
        fmt=",.1f",
        label="total gain of a closed software loop over all rounds, as a multiple of its first round, if g held at the corrected median r",
        defined_in=here(),
    )
    L.derive(
        "path-rsi-multiplier-illustration",
        lambda q: 1 / (1 - q["dyn-loop-gain-illustration"]),
        "1 / (1 - dyn-loop-gain-illustration)",
        fmt=",.1f",
        label="the same multiple at Cunningham et al.'s upper-end illustration of the loop gain",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Undeclared compute. How long the untraced pool would take to run a 1e26 FLOP training run,
    # if each untraced chip were one H100e at the physical chapter's reference utilisation (the
    # same reading that chapter makes when it divides the pool by a floor stated in H100e).

    L.derive(
        "path-covert-days-1e26",
        lambda q: q["phys-rahman-1e26-local"]
        / (q["phys-chips-unaccounted"] * q["phys-miri-h100e"] * 1e12 * q["phys-util-ref"])
        / SECONDS_PER_DAY,
        "phys-rahman-1e26-local / (phys-chips-unaccounted * phys-miri-h100e * phys-util-ref) / 86,400 s",
        unit="days",
        fmt=",.1f",
        label="days for the untraced chip pool, read as H100e at the reference utilisation, to run 1e26 FLOP",
        defined_in=here(),
    )

    # How long the channels that found past covert programmes take. With discovery as a Poisson
    # process at the historical rate, the mean wait is 1 / rate, and the time to bring the miss
    # chance down to beta is ln(1 / beta) / rate: D4's T_d(beta) for compute only those channels see.

    L.derive(
        "path-covert-mean-years",
        lambda q: 1 / q["org-covert-hazard"],
        "1 / org-covert-hazard",
        unit="years",
        fmt=",.0f",
        label="mean time to discovery of a covert programme at the historical discovery rate",
        defined_in=here(),
    )
    L.derive(
        "path-covert-td-prevent",
        lambda q: math.log(1 / q["def-prevent-beta"]) / q["org-covert-hazard"],
        "ln(1 / def-prevent-beta) / org-covert-hazard",
        unit="years",
        fmt=",.0f",
        label="detection time T_d at the prevention miss chance for compute only the historical channels see",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Long-horizon autonomy. Where the 80% horizon would be in a year if it grew at the 50%
    # horizon's measured rate: how far apart human-held gates could then sit before an agent
    # crosses between them unattended.

    L.derive(
        "path-horizon-p80-next-year",
        lambda q: q["dyn-horizon-p80"] * q["dyn-horizon-annual"] / 60,
        "dyn-horizon-p80 * dyn-horizon-annual / 60",
        unit="hours",
        fmt=",.0f",
        label="80% time horizon a year on, if it grows at the 50% horizon's annual multiple",
        defined_in=here(),
    )
