"""Part III, 1: formal statements and proofs (research/05-formal.md).

The few numbers the proofs need that earlier parts did not compute: how many locked organisms the
exact binomial bound needs when one or two are missed (C5); the aggregate chip floor for a 1e26 FLOP
run under a pause recomputed as a bound, at full utilisation and at the FP8 peak (the lowest precision
in production training), with the same floor for a run held to BF16 and the untraced stock against
the bound (C8); the largest closure at which the software loop's own corrected upper gain stays
below 1 (C6); and how far a line computed at launch speed must rise when a run absorbs algorithmic
drift while it runs (C1). No inputs of its own: every number is derived from other parts' inputs and
results. Every id starts with formal-.
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
    # utilisation and the dense BF16 peak; every floor scales as one over utilisation and one over
    # the peak, so the bound is the reference floor times phys-util-ref (full utilisation) over
    # phys-fp8-over-bf16 (the FP8 peak). A run held to BF16 has the larger floor.
    L.derive(
        "formal-floor-bound-1e26-pause",
        lambda q: q["phys-floor-chips-1e26-pause"] * q["phys-util-ref"] / q["phys-fp8-over-bf16"],
        "phys-floor-chips-1e26-pause * phys-util-ref / phys-fp8-over-bf16 (full utilisation, FP8 peak)",
        unit="H100e",
        fmt="sig2",
        label="aggregate chip floor for 1e26 FLOP over a pause's longest sensible run at full utilisation and the dense FP8 peak: a bound in H100e-equivalents for any mix of chips, down to FP8",
        defined_in=here(),
    )
    L.derive(
        "formal-floor-bound-1e26-pause-bf16",
        lambda q: q["phys-floor-chips-1e26-pause"] * q["phys-util-ref"],
        "phys-floor-chips-1e26-pause * phys-util-ref (full utilisation, BF16 peak)",
        unit="H100e",
        fmt="sig2",
        label="the same floor for a run held to BF16, at full utilisation",
        defined_in=here(),
    )
    L.derive(
        "formal-floor-ref-over-bound",
        lambda q: q["phys-fp8-over-bf16"] / q["phys-util-ref"],
        "phys-fp8-over-bf16 / phys-util-ref",
        fmt=".1f",
        label="factor by which the physical chapter's floor (reference utilisation, BF16 peak) exceeds the bound",
        defined_in=here(),
    )
    L.derive(
        "formal-pool-over-floor-bound",
        lambda q: q["org-smuggled-cum"] / q["formal-floor-bound-1e26-pause"],
        "org-smuggled-cum / formal-floor-bound-1e26-pause",
        fmt=",.0f",
        label="median compute smuggled into one country through 2025, as a multiple of the 1e26 FLOP pause floor taken as a bound (full utilisation, FP8)",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C1: a line computed at launch speed, against a run that absorbs algorithmic drift while it
    # runs (Corollary 1.6a). With speed rising as e^(a tau), the launch-speed time must reach
    # G(m T_r) = (e^(a m T_r) - 1) / a instead of m T_r; the factor is G(m T_r) / (m T_r). An upper
    # bound: it assumes the run adopts every gain the moment it appears. T_r is prot-tr-declared's
    # formula, written out because the protocol's module is built after this one.
    def _inrun_factor(growth: float, m: float, tr: float) -> float:
        x = math.log(growth) * m * tr
        return math.expm1(x) / x

    L.derive(
        "formal-inrun-line-factor",
        lambda q: _inrun_factor(q["phys-algo-growth"], q["prot-margin"], (q["org-dprk-months"] + q["prot-licence-months"]) / 12),
        "(e^(a x) - 1) / (a x), a = ln(phys-algo-growth), x = prot-margin * (org-dprk-months + prot-licence-months) / 12",
        fmt=".1f",
        label="factor by which a line computed at launch speed must rise to keep T_b >= m T_r when the run absorbs algorithmic drift at the central rate while it runs (an upper bound on drift)",
        defined_in=here(),
    )
    L.derive(
        "formal-inrun-line-factor-high",
        lambda q: _inrun_factor(q["phys-algo-growth-high"], q["prot-margin"], (q["org-dprk-months"] + q["prot-licence-months"]) / 12),
        "(e^(a x) - 1) / (a x), a = ln(phys-algo-growth-high), x = prot-margin * (org-dprk-months + prot-licence-months) / 12",
        fmt=".1f",
        label="the same factor at the high end of the ledger's algorithmic drift interval",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C6: the diagonal entry of the software loop is its closure times r; at the corrected 95th
    # percentile of r, the closure must stay below 1 / r for that entry to be below 1.
    L.derive(
        "formal-software-closure-max",
        lambda q: 1.0 / q["dyn-r-lm-hi-corrected"],
        "1 / dyn-r-lm-hi-corrected",
        fmt=".2f",
        label="largest closure of the software loop at which its own gain, at the corrected 95th percentile of r, stays below 1",
        defined_in=here(),
    )
