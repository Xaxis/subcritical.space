"""Part III, 1: formal statements and proofs (research/05-formal.md).

The few numbers the proofs need that earlier parts did not compute: how many locked organisms the
exact binomial bound needs when one or two are missed (C5), and the aggregate chip floor for a
1e26 FLOP run under a pause recomputed as a bound, at full utilisation and at the highest utilisation
in the ledger, with the untraced stock against that bound (C8). No inputs of its own: every number
is derived from earlier parts. Every id starts with formal-.
"""

from __future__ import annotations

import math


def _fewest_organisms(misses: int, target: float, confidence: float) -> int:
    """Smallest n with P(Bin(n, target) <= misses) <= 1 - confidence: the exact one-sided upper bound
    on the miss rate, after `misses` misses among n organisms, is then at most the target."""
    alpha = 1 - confidence
    n = misses + 1
    while sum(math.comb(n, k) * target**k * (1 - target) ** (n - k) for k in range(misses + 1)) > alpha:
        n += 1
    return n


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # C5: organisms needed when some are missed (Theorem 5.1). With none missed this is
    # claim-d5-organisms; each miss raises the count.
    L.derive(
        "formal-d5-organisms-one-miss",
        lambda q: _fewest_organisms(1, q["claim-d5-miss-target"], q["claim-confidence"]),
        "smallest n with P(Bin(n, claim-d5-miss-target) <= 1) <= 1 - claim-confidence",
        unit="organisms",
        fmt=",.0f",
        label="locked organisms per budget for the exact one-sided bound on the miss rate to reach its target when one organism is missed",
        defined_in=here(),
    )
    L.derive(
        "formal-d5-organisms-two-miss",
        lambda q: _fewest_organisms(2, q["claim-d5-miss-target"], q["claim-confidence"]),
        "smallest n with P(Bin(n, claim-d5-miss-target) <= 2) <= 1 - claim-confidence",
        unit="organisms",
        fmt=",.0f",
        label="locked organisms per budget for the exact one-sided bound on the miss rate to reach its target when two organisms are missed",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C8: the floor as a bound (Theorem 8.1). The physical chapter's floor uses the reference
    # utilisation; every floor scales as one over utilisation, so the floor at utilisation u is
    # the reference floor times phys-util-ref / u.
    L.derive(
        "formal-floor-bound-1e26-pause",
        lambda q: q["phys-floor-chips-1e26-pause"] * q["phys-util-ref"] / 1.0,
        "phys-floor-chips-1e26-pause * phys-util-ref / 1 (full utilisation)",
        unit="H100e",
        fmt="sig2",
        label="aggregate chip floor for 1e26 FLOP over a pause's longest sensible run at full utilisation: a bound in H100e-equivalents for any mix of chips",
        defined_in=here(),
    )
    L.derive(
        "formal-floor-mfu-1e26-pause",
        lambda q: q["phys-floor-chips-1e26-pause"] * q["phys-util-ref"] / q["phys-pope-mfu-prefill"],
        "phys-floor-chips-1e26-pause * phys-util-ref / phys-pope-mfu-prefill",
        unit="H100e",
        fmt="sig2",
        label="the same floor at the highest utilisation in the ledger (a vendor figure for large-batch input processing)",
        defined_in=here(),
    )
    L.derive(
        "formal-floor-ref-over-bound",
        lambda q: 1.0 / q["phys-util-ref"],
        "1 / phys-util-ref",
        fmt=".1f",
        label="factor by which a floor at the reference utilisation exceeds the bound at full utilisation",
        defined_in=here(),
    )
    L.derive(
        "formal-pool-over-floor-bound",
        lambda q: q["org-smuggled-cum"] / q["formal-floor-bound-1e26-pause"],
        "org-smuggled-cum / formal-floor-bound-1e26-pause",
        fmt=",.0f",
        label="median compute smuggled into one country through 2025, as a multiple of the 1e26 FLOP pause floor taken as a bound (full utilisation)",
        defined_in=here(),
    )
