"""Part I, 4: the cognitive and functional perspective (research/014-cognitive.md).

Derives the chapter's numbers from data/inputs/014-cognitive.toml: speed, cost and time-budget
ratios (F1), the gaps between AI and expert baselines (F2, F3), and how fast benchmarks saturate,
how many of their items are sound, and how much elicitation moves a score (F4).
"""

from __future__ import annotations

import math


def logit(p: float) -> float:
    return math.log(p / (1 - p))


def wilson(k: float, n: float, z: float) -> tuple[float, float]:
    """Wilson score interval for k successes in n trials."""
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # F1. Speed, copies and quality.

    L.derive(
        "cog-rebench-attempt-ratio",
        lambda q: q["cog-rebench-attempts-agent"] / q["cog-rebench-attempts-human"],
        "cog-rebench-attempts-agent / cog-rebench-attempts-human",
        fmt=".0f",
        label="how many more scored attempts an hour the agent made than human experts on RE-Bench",
        defined_in=here(),
    )
    L.derive(
        "cog-rebench-cost-ratio",
        lambda q: q["cog-rebench-human-cost"] / q["cog-rebench-agent-cost"],
        "cog-rebench-human-cost / cog-rebench-agent-cost",
        fmt=".0f",
        label="how many times more an 8-hour human expert run cost than an 8-hour agent run on RE-Bench",
        defined_in=here(),
    )
    L.derive(
        "cog-rebench-human-hourly",
        lambda q: q["cog-rebench-human-cost"] / q["cog-rebench-run-hours"],
        "cog-rebench-human-cost / cog-rebench-run-hours",
        unit="USD/h",
        fmt=",.0f",
        label="hourly pay of a RE-Bench human expert",
        defined_in=here(),
    )
    L.derive(
        "cog-gdpval-expert-hourly",
        lambda q: q["cog-gdpval-expert-cost"] / (q["cog-gdpval-expert-minutes"] / 60),
        "cog-gdpval-expert-cost / (cog-gdpval-expert-minutes / 60)",
        unit="USD/h",
        fmt=",.0f",
        label="hourly cost of a GDPval expert, from median wages",
        defined_in=here(),
    )
    L.derive(
        "cog-wage-spread",
        lambda q: q["cog-rebench-human-hourly"] / q["cog-gdpval-expert-hourly"],
        "cog-rebench-human-hourly / cog-gdpval-expert-hourly",
        fmt=".1f",
        label="spread between the hourly human costs two published comparisons assume",
        defined_in=here(),
    )
    L.derive(
        "cog-rebench-baseline-cost",
        lambda q: q["cog-rebench-human-attempts"] * q["cog-rebench-human-cost"],
        "cog-rebench-human-attempts * cog-rebench-human-cost",
        unit="USD",
        fmt="sig3",
        label="approximate pay for RE-Bench's whole individual-expert baseline",
        defined_in=here(),
    )
    L.derive(
        "cog-rebench-swing",
        lambda q: q["cog-rebench-ai-over-human-2h"] * q["cog-rebench-human-over-ai-32h"],
        "cog-rebench-ai-over-human-2h * cog-rebench-human-over-ai-32h",
        fmt=",.0f",
        label="how far the AI-to-human score ratio on RE-Bench moves between the 2-hour and 32-hour budgets",
        defined_in=here(),
    )
    L.derive(
        "cog-rebench-swing-per-doubling",
        lambda q: q["cog-rebench-swing"]
        ** (1 / math.log2(q["cog-rebench-budget-long"] / q["cog-rebench-budget-short"])),
        "cog-rebench-swing ^ (1 / log2(cog-rebench-budget-long / cog-rebench-budget-short))",
        fmt=".2f",
        label="average factor by which each doubling of the time budget moves the RE-Bench ratio towards humans",
        defined_in=here(),
    )
    L.derive(
        "cog-gdpval-review-shrink",
        lambda q: q["cog-gdpval-naive-speedup"] / q["cog-gdpval-review-speedup"],
        "cog-gdpval-naive-speedup / cog-gdpval-review-speedup",
        fmt="sig2",
        label="factor by which counting expert review shrinks GPT-5's speed gain on GDPval",
        defined_in=here(),
    )
    L.derive(
        "cog-gdpval-cost-shrink",
        lambda q: q["cog-gdpval-naive-cost-gain"] / q["cog-gdpval-review-cost-gain"],
        "cog-gdpval-naive-cost-gain / cog-gdpval-review-cost-gain",
        fmt="sig2",
        label="factor by which counting expert review shrinks GPT-5's cost gain on GDPval",
        defined_in=here(),
    )
    L.derive(
        "cog-sc-labour-at-share",
        lambda q: q["cog-sc-copies"] * q["cog-sc-speed"],
        "cog-sc-copies * cog-sc-speed",
        fmt=",.0f",
        label="engineer-equivalents per human engineer in AI 2027's superhuman coder (copies times speed)",
        defined_in=here(),
    )
    L.derive(
        "cog-sc-labour-full",
        lambda q: q["cog-sc-labour-at-share"] / q["cog-sc-compute-share"],
        "cog-sc-labour-at-share / cog-sc-compute-share",
        fmt="sig2",
        label="engineer-equivalents per human engineer if all the company's compute ran superhuman coders (linear)",
        defined_in=here(),
    )
    L.derive(
        "cog-hendrycks-labour",
        lambda q: q["cog-hendrycks-pace"] * q["cog-hendrycks-copies"],
        "cog-hendrycks-pace * cog-hendrycks-copies",
        fmt="sig2",
        label="human-researcher-equivalents in Hendrycks et al.'s illustration (pace times copies)",
        defined_in=here(),
    )
    L.derive(
        "cog-horizon-best-hours",
        lambda q: q["cog-horizon-best"] / 60,
        "cog-horizon-best / 60",
        unit="h",
        fmt=".1f",
        label="best published 50% time horizon, in hours",
        defined_in=here(),
    )
    L.derive(
        "cog-th11-long-baselined-share",
        lambda q: q["cog-th11-long-baselined"] / q["cog-th11-long-tasks"],
        "cog-th11-long-baselined / cog-th11-long-tasks",
        fmt="%",
        label="share of METR's 8-hour-plus tasks with a measured human time",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # F2. The decisive functions.

    L.derive(
        "cog-mlebench-passk-ratio",
        lambda q: q["cog-mlebench-pass8"] / q["cog-mlebench-pass1"],
        "cog-mlebench-pass8 / cog-mlebench-pass1",
        fmt=".1f",
        label="factor by which best-of-eight raises the MLE-bench medal rate over one attempt",
        defined_in=here(),
    )
    L.derive(
        "cog-nanogpt-ai-share",
        lambda q: q["cog-nanogpt-ai-records"] / q["cog-nanogpt-records"],
        "cog-nanogpt-ai-records / cog-nanogpt-records",
        fmt="%",
        label="share of NanoGPT speedrun records co-credited to AI agents",
        defined_in=here(),
    )
    L.derive(
        "cog-vct-ratio",
        lambda q: q["cog-vct-o3"] / q["cog-vct-virologist"],
        "cog-vct-o3 / cog-vct-virologist",
        fmt=".1f",
        label="o3's VCT accuracy over expert virologists' average in their own sub-areas",
        defined_in=here(),
    )
    L.derive(
        "cog-gpqa-diamond-margin",
        lambda q: 100 * (q["cog-gpqa-diamond-best"] - q["cog-gpqa-diamond-expert"]),
        "100 * (cog-gpqa-diamond-best - cog-gpqa-diamond-expert)",
        unit="points",
        fmt=".0f",
        label="lead of the best GPQA Diamond score over the developer-recruited PhD experts",
        defined_in=here(),
    )
    L.derive(
        "cog-forecast-brier-ratio",
        lambda q: q["cog-forecast-llm-brier"] / q["cog-forecast-super-brier"],
        "cog-forecast-llm-brier / cog-forecast-super-brier",
        fmt=".2f",
        label="best LLM's Brier score over the superforecasters' in the first ForecastBench paper",
        defined_in=here(),
    )
    L.derive(
        "cog-forecast-top-margin",
        lambda q: q["cog-forecast-top-index"] - q["cog-forecast-super-index"],
        "cog-forecast-top-index - cog-forecast-super-index",
        unit="points",
        fmt=".1f",
        label="lead of the top ForecastBench entry over the superforecaster median, Brier Index",
        defined_in=here(),
    )
    L.derive(
        "cog-forecast-llm-margin",
        lambda q: q["cog-forecast-super-index"] - q["cog-forecast-llm-index"],
        "cog-forecast-super-index - cog-forecast-llm-index",
        unit="points",
        fmt=".1f",
        label="lead of the superforecaster median over the best single LLM, Brier Index",
        defined_in=here(),
    )
    L.derive(
        "cog-rli-growth",
        lambda q: q["cog-rli-best-2026"] / q["cog-rli-best-2025"],
        "cog-rli-best-2026 / cog-rli-best-2025",
        fmt=".1f",
        label="growth of the best Remote Labor Index automation rate from October 2025 to November 2026",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # F3. Narrow versus general.

    L.derive(
        "cog-alphafold-ratio",
        lambda q: q["cog-casp14-next-rmsd"] / q["cog-alphafold-rmsd"],
        "cog-casp14-next-rmsd / cog-alphafold-rmsd",
        fmt=".1f",
        label="next best CASP14 method's median backbone error over AlphaFold's",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # F4. Saturation, soundness and elicitation. The useful life of a battery assumes the frontier
    # score rises linearly on the logit scale between two published points: an assumption, stated.

    L.derive(
        "cog-fm-logit-rate",
        lambda q: (logit(q["cog-fm-best"]) - logit(q["cog-fm-release-best"]))
        / (q["cog-fm-best-year"] - q["cog-fm-release-year"]),
        "(logit(cog-fm-best) - logit(cog-fm-release-best)) / (cog-fm-best-year - cog-fm-release-year)",
        unit="logits/yr",
        fmt=".1f",
        label="rise of the best FrontierMath score on the logit scale (a lower bound, since release was under 2%)",
        defined_in=here(),
    )
    L.derive(
        "cog-fm-useful-life",
        lambda q: (logit(q["cog-life-high"]) - logit(q["cog-life-low"])) / q["cog-fm-logit-rate"],
        "(logit(cog-life-high) - logit(cog-life-low)) / cog-fm-logit-rate",
        unit="yr",
        fmt=".1f",
        label="years FrontierMath took to cross from 10% to 90% at its logit rate (an upper bound)",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-logit-rate",
        lambda q: (logit(q["cog-hle-best"]) - logit(q["cog-hle-release-best"]))
        / (q["cog-hle-best-year"] - q["cog-hle-release-year"]),
        "(logit(cog-hle-best) - logit(cog-hle-release-best)) / (cog-hle-best-year - cog-hle-release-year)",
        unit="logits/yr",
        fmt=".1f",
        label="rise of the best HLE score on the logit scale",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-elapsed-months",
        lambda q: 12 * (q["cog-hle-best-year"] - q["cog-hle-release-year"]),
        "12 * (cog-hle-best-year - cog-hle-release-year)",
        unit="months",
        fmt=",.0f",
        label="months between HLE's release and the leaderboard's best score",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-useful-life",
        lambda q: (logit(q["cog-life-high"]) - logit(q["cog-life-low"])) / q["cog-hle-logit-rate"],
        "(logit(cog-life-high) - logit(cog-life-low)) / cog-hle-logit-rate",
        unit="yr",
        fmt=".1f",
        label="years HLE would take to cross from 10% to 90% at its logit rate",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-defective-share",
        lambda q: q["cog-hle-defective"] / q["cog-hle-sampled"],
        "cog-hle-defective / cog-hle-sampled",
        fmt="%",
        label="share of Epoch's HLE sample found defective",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-defective-ci-low",
        lambda q: wilson(q["cog-hle-defective"], q["cog-hle-sampled"], q["cog-wilson-z"])[0],
        "Wilson 95% interval of cog-hle-defective / cog-hle-sampled, lower end (z = cog-wilson-z)",
        fmt="%",
        label="lower end of the 95% interval on HLE's defective share",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-defective-ci-high",
        lambda q: wilson(q["cog-hle-defective"], q["cog-hle-sampled"], q["cog-wilson-z"])[1],
        "Wilson 95% interval of cog-hle-defective / cog-hle-sampled, upper end (z = cog-wilson-z)",
        fmt="%",
        label="upper end of the 95% interval on HLE's defective share",
        defined_in=here(),
    )
    L.derive(
        "cog-hle-sound-share",
        lambda q: 1 - q["cog-hle-defective-share"],
        "1 - cog-hle-defective-share",
        fmt="%",
        label="share of Epoch's HLE sample found sound",
        defined_in=here(),
    )
    L.derive(
        "cog-robust-recall-ratio",
        lambda q: q["cog-robust-recall-locked"] / q["cog-robust-recall-base"],
        "cog-robust-recall-locked / cog-robust-recall-base",
        fmt="%",
        label="share of the base model's hard-task recall that elicitation recovered from a tamper-resistant lock",
        defined_in=here(),
    )
