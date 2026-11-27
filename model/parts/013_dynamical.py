"""Part I, 3: the dynamical perspective (research/013-dynamical.md).

Derives the chapter's numbers from data/inputs/013-dynamical.toml: returns to research after the
compute-bottleneck correction, the loop-gain threshold of Cunningham et al., the speedrun and
time-horizon rates, and the amplification rate of a near-critical loop. Every id starts with dyn-.
"""

from __future__ import annotations

import math


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # Returns to research. With lambda = 1, r = 1/beta (Bloom et al.'s Table 7 betas).

    L.derive(
        "dyn-r-moore",
        lambda q: 1 / q["dyn-bloom-beta-moore"],
        "1 / dyn-bloom-beta-moore",
        fmt=",.0f",
        label="returns to research r for Moore's Law research, with lambda = 1",
        defined_in=here(),
    )
    L.derive(
        "dyn-r-aggregate",
        lambda q: 1 / q["dyn-bloom-beta-aggregate"],
        "1 / dyn-bloom-beta-aggregate",
        fmt=".2f",
        label="returns to research r for the aggregate US economy, with lambda = 1",
        defined_in=here(),
    )

    # The compute-bottleneck correction: with research compute fixed and a Cobb-Douglas research
    # input E = L^(1 - eps_K) K^eps_K, the effective lambda on labour is lambda * (1 - eps_K), so
    # every r is multiplied by (1 - eps_K). Quantiles scale with it; the uncertainty in eps_K is
    # not carried.
    L.derive(
        "dyn-bottleneck-divisor",
        lambda q: 1 / (1 - q["dyn-research-compute-share"]),
        "1 / (1 - dyn-research-compute-share)",
        fmt=".1f",
        label="factor by which the compute-bottleneck correction divides r",
        defined_in=here(),
    )
    for key, what in (
        ("dyn-r-cv", "computer vision, median"),
        ("dyn-r-rl", "reinforcement learning, median"),
        ("dyn-r-lm", "language models, median"),
        ("dyn-r-cv-hi", "computer vision, 95th percentile"),
        ("dyn-r-rl-hi", "reinforcement learning, 95th percentile"),
        ("dyn-r-lm-hi", "language models, 95th percentile"),
        ("dyn-r-lm-lo", "language models, 5th percentile"),
    ):
        L.derive(
            f"{key}-corrected",
            lambda q, key=key: q[key] * (1 - q["dyn-research-compute-share"]),
            f"{key} * (1 - dyn-research-compute-share)",
            fmt=".2f",
            label=f"r after the compute-bottleneck correction, {what}",
            defined_in=here(),
        )

    # Row-sum headroom of the software loop: what is left below 1 for every cross-feed into
    # software once its own corrected return is counted (research/013-dynamical.md, Y3).
    L.derive(
        "dyn-software-headroom",
        lambda q: 1 - q["dyn-r-lm-corrected"],
        "1 - dyn-r-lm-corrected",
        fmt=".2f",
        label="headroom below 1 left for cross-feeds into the software loop, corrected median r",
        defined_in=here(),
    )
    L.derive(
        "dyn-software-headroom-upper",
        lambda q: 1 - q["dyn-r-lm-hi-corrected"],
        "1 - dyn-r-lm-hi-corrected",
        fmt=".2f",
        label="the same headroom at the corrected 95th percentile of r",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Cunningham et al.'s core condition: (return to R&D) * eps_RC * eps_CA > 1.

    L.derive(
        "dyn-loop-threshold-eps-rc",
        lambda q: 1 / (q["dyn-cunningham-return"] * q["dyn-cunningham-eps-ca"]),
        "1 / (dyn-cunningham-return * dyn-cunningham-eps-ca)",
        fmt="%",
        label="research productivity gain per ECI point at which the core loop becomes self-sustaining",
        defined_in=here(),
    )
    L.derive(
        "dyn-loop-gain-illustration",
        lambda q: q["dyn-cunningham-return"]
        * q["dyn-cunningham-eps-rc-illustration"]
        * q["dyn-cunningham-eps-ca"],
        "dyn-cunningham-return * dyn-cunningham-eps-rc-illustration * dyn-cunningham-eps-ca",
        fmt=".2f",
        label="core loop condition implied by the upper-end 4x uplift illustration (below 1 is subcritical)",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Burtsev: perturbations grow at about ln(R_AI) / tau once R_AI > 1.

    L.derive(
        "dyn-burtsev-amp-rate",
        lambda q: math.log(q["dyn-burtsev-network-rho"]) / q["dyn-burtsev-delay"],
        "ln(dyn-burtsev-network-rho) / dyn-burtsev-delay",
        unit="/yr",
        fmt=".2f",
        label="amplification rate of the network scenario, ln(rho) / tau",
        defined_in=here(),
    )
    L.derive(
        "dyn-burtsev-efold-years",
        lambda q: q["dyn-burtsev-delay"] / math.log(q["dyn-burtsev-network-rho"]),
        "dyn-burtsev-delay / ln(dyn-burtsev-network-rho)",
        unit="years",
        fmt=".1f",
        label="e-folding time of the network scenario's amplification",
        defined_in=here(),
    )
    L.derive(
        "dyn-burtsev-growth-per-year",
        lambda q: q["dyn-burtsev-network-rho"] ** (1 / q["dyn-burtsev-delay"]),
        "dyn-burtsev-network-rho ^ (1 / dyn-burtsev-delay)",
        fmt=".2f",
        label="multiple by which a perturbation grows in one year in the network scenario",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # The measured acceleration and the automation share inside one lab.

    L.derive(
        "dyn-metr-slope-ratio",
        lambda q: q["dyn-metr-aeci-after"] / q["dyn-metr-aeci-before"],
        "dyn-metr-aeci-after / dyn-metr-aeci-before",
        fmt=".1f",
        label="ratio of AECI slopes after and before the breakpoint (a check on the 1.9x headline)",
        defined_in=here(),
    )
    L.derive(
        "dyn-anthropic-ai-led-multiple",
        lambda q: q["dyn-anthropic-ai-led"] / q["dyn-anthropic-ai-led-feb"],
        "dyn-anthropic-ai-led / dyn-anthropic-ai-led-feb",
        fmt=",.0f",
        label="growth of the AI-led share of Anthropic's AI R&D, February to August 2026, lower bound",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # The NanoGPT speedrun: a public record of software progress at fixed hardware.

    L.derive(
        "dyn-nanogpt-ai-share",
        lambda q: q["dyn-nanogpt-ai-records"] / q["dyn-nanogpt-records"],
        "dyn-nanogpt-ai-records / dyn-nanogpt-records",
        fmt="%",
        label="share of speedrun records crediting an AI agent",
        defined_in=here(),
    )
    L.derive(
        "dyn-nanogpt-speedup",
        lambda q: q["dyn-nanogpt-start-min"] / q["dyn-nanogpt-end-min"],
        "dyn-nanogpt-start-min / dyn-nanogpt-end-min",
        fmt=",.0f",
        label="speedrun speedup, May 2024 to March 2026",
        defined_in=here(),
    )
    L.derive(
        "dyn-nanogpt-deep-factor",
        lambda q: q["dyn-nanogpt-start-min"] / q["dyn-nanogpt-end-min"] / q["dyn-nanogpt-shallow-moderate"],
        "(dyn-nanogpt-start-min / dyn-nanogpt-end-min) / dyn-nanogpt-shallow-moderate",
        fmt=".1f",
        label="speedup multiple left for deep contributions",
        defined_in=here(),
    )
    L.derive(
        "dyn-speedrun-ratio",
        lambda q: q["dyn-speedrun-baseline-s"] / q["dyn-speedrun-record-s"],
        "dyn-speedrun-baseline-s / dyn-speedrun-record-s",
        fmt=".1f",
        label="speedrun wall-clock speedup, record 1 to record 92",
        defined_in=here(),
    )
    L.derive(
        "dyn-speedrun-annual",
        lambda q: (q["dyn-speedrun-baseline-s"] / q["dyn-speedrun-record-s"])
        ** (365.25 / q["dyn-speedrun-span-days"]),
        "(dyn-speedrun-baseline-s / dyn-speedrun-record-s) ^ (365.25 / dyn-speedrun-span-days)",
        fmt=".1f",
        label="average annual speedup multiple over the whole record",
        defined_in=here(),
    )
    L.derive(
        "dyn-speedrun-first-annual",
        lambda q: q["dyn-speedrun-first-window"] ** (12 / q["dyn-speedrun-window-months"]),
        "dyn-speedrun-first-window ^ (12 / dyn-speedrun-window-months)",
        fmt=",.0f",
        label="annualised speedup multiple in the record's first 8 months",
        defined_in=here(),
    )
    L.derive(
        "dyn-speedrun-2026-annual",
        lambda q: q["dyn-speedrun-rate-2026"] ** (12 / q["dyn-speedrun-window-months"]),
        "dyn-speedrun-rate-2026 ^ (12 / dyn-speedrun-window-months)",
        fmt=".1f",
        label="annualised speedup multiple, January to August 2026",
        defined_in=here(),
    )
    L.derive(
        "dyn-speedrun-slowdown",
        lambda q: q["dyn-speedrun-first-window"] ** (12 / q["dyn-speedrun-window-months"])
        / q["dyn-speedrun-rate-2025"],
        "dyn-speedrun-first-window ^ (12 / dyn-speedrun-window-months) / dyn-speedrun-rate-2025",
        fmt=",.0f",
        label="factor by which the annualised speedrun pace fell from its first months to 2025",
        defined_in=here(),
    )
    L.derive(
        "dyn-agent-equivalent-gain",
        lambda q: q["dyn-agent-exp-horizon-hi"] / q["dyn-human-cost-per-pct"] / 100,
        "dyn-agent-exp-horizon-hi / dyn-human-cost-per-pct / 100",
        fmt=".1%",
        label="speedup a human would buy with the best agent's expenditure horizon",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Time horizons: the doubling time as an annual multiple, and how far reliability lags.

    def per_year(days_key: str):
        return lambda q: 2 ** (365.25 / q[days_key])

    L.derive(
        "dyn-horizon-annual",
        per_year("dyn-horizon-doubling"),
        "2 ^ (365.25 / dyn-horizon-doubling)",
        fmt=".1f",
        label="annual multiple of the 50% time horizon, 2023 onward",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-annual-slow",
        per_year("dyn-horizon-doubling-hi"),
        "2 ^ (365.25 / dyn-horizon-doubling-hi)",
        fmt=".1f",
        label="the same at the slow end of the doubling-time interval",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-annual-fast",
        per_year("dyn-horizon-doubling-lo"),
        "2 ^ (365.25 / dyn-horizon-doubling-lo)",
        fmt=".0f",
        label="the same at the fast end of the doubling-time interval",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-annual-2019",
        per_year("dyn-horizon-doubling-2019"),
        "2 ^ (365.25 / dyn-horizon-doubling-2019)",
        fmt=".1f",
        label="annual multiple of the 50% time horizon, 2019 to 2025",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-p50-hours",
        lambda q: q["dyn-horizon-p50"] / 60,
        "dyn-horizon-p50 / 60",
        unit="hours",
        fmt=".0f",
        label="latest 50% time horizon in hours",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-p80-hours",
        lambda q: q["dyn-horizon-p80"] / 60,
        "dyn-horizon-p80 / 60",
        unit="hours",
        fmt=".0f",
        label="latest 80% time horizon in hours",
        defined_in=here(),
    )
    L.derive(
        "dyn-horizon-ratio",
        lambda q: q["dyn-horizon-p50"] / q["dyn-horizon-p80"],
        "dyn-horizon-p50 / dyn-horizon-p80",
        fmt=".1f",
        label="ratio of the 50% to the 80% horizon, latest entry",
        defined_in=here(),
    )
    L.derive(
        "dyn-ord-ratio",
        lambda q: 1 / q["dyn-ord-t80-over-t50"],
        "1 / dyn-ord-t80-over-t50",
        fmt=",.0f",
        label="ratio of the 50% to the 80% horizon under a constant hazard",
        defined_in=here(),
    )
    L.derive(
        "dyn-reliability-lag-days",
        lambda q: math.log2(q["dyn-horizon-p50"] / q["dyn-horizon-p80"]) * q["dyn-horizon-doubling"],
        "log2(dyn-horizon-p50 / dyn-horizon-p80) * dyn-horizon-doubling",
        unit="days",
        fmt=",.0f",
        label="time for the 80% horizon to reach today's 50% horizon, if both double at the 50% rate",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Hardware and capital.

    L.derive(
        "dyn-cmos-headroom-oom",
        lambda q: math.log10(q["dyn-cmos-headroom"]),
        "log10(dyn-cmos-headroom)",
        fmt=".1f",
        label="CMOS energy-efficiency headroom in orders of magnitude",
        defined_in=here(),
    )
    L.derive(
        "dyn-cmos-years",
        lambda q: math.log(q["dyn-cmos-headroom"]) / math.log(q["dyn-gpu-eff-growth"]),
        "ln(dyn-cmos-headroom) / ln(dyn-gpu-eff-growth)",
        unit="years",
        fmt=",.0f",
        label="years until the CMOS ceiling at the measured efficiency growth",
        defined_in=here(),
    )
    L.derive(
        "dyn-compute-sold-growth",
        lambda q: q["dyn-compute-sold-2025"] / q["dyn-compute-sold-2024"],
        "dyn-compute-sold-2025 / dyn-compute-sold-2024",
        fmt=".1f",
        label="growth of AI compute sold, 2024 to 2025, multiple",
        defined_in=here(),
    )
    L.derive(
        "dyn-fab-build-years",
        lambda q: q["dyn-fab-build-days"] / 365.25,
        "dyn-fab-build-days / 365.25",
        unit="years",
        fmt=".1f",
        label="average fab build time in years",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # Continual learning and self-replication.

    L.derive(
        "dyn-seal-gain-points",
        lambda q: (q["dyn-seal-squad"] - q["dyn-seal-squad-base"]) * 100,
        "(dyn-seal-squad - dyn-seal-squad-base) * 100",
        unit="points",
        fmt=".1f",
        label="SEAL's gain over the passage-only baseline, percentage points",
        defined_in=here(),
    )
    L.derive(
        "dyn-fudan-capable-share",
        lambda q: q["dyn-fudan-capable"] / q["dyn-fudan-evaluated"],
        "dyn-fudan-capable / dyn-fudan-evaluated",
        fmt="%",
        label="share of evaluated AI systems reported capable of self-replication",
        defined_in=here(),
    )
