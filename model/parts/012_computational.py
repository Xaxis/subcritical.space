"""Part I, 2: the computational and algorithmic perspective (research/012-computational.md).

Inputs are in data/inputs/012-computational.toml. Every id starts with comp-. Multipliers are
plain numbers; the text writes the "x". Three kinds of derivation:
  - consistency checks that recompute a source's own headline from its parts;
  - conversions between halving times, yearly multipliers and orders of magnitude (OOM);
  - the combined leak of a training cap, an illustration with labelled placeholders.
"""

from __future__ import annotations

import math


def build(L, here) -> None:
    ln10 = math.log(10)

    # -----------------------------------------------------------------------------------------
    # A1: the Rosetta fit, C = k ln F + b(t). Frontier growth = k * dlnF/dt + db/dt.

    L.derive(
        "comp-rosetta-per-oom",
        lambda q: q["comp-rosetta-k"] * ln10,
        "comp-rosetta-k * ln(10)",
        unit="units per OOM",
        fmt=".2f",
        label="Rosetta capability gained per order of magnitude of training compute",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-implied-algo",
        lambda q: math.exp(q["comp-rosetta-fixed-growth"] / q["comp-rosetta-k"]),
        "exp(comp-rosetta-fixed-growth / comp-rosetta-k)",
        fmt=".1f",
        label="yearly compute-equivalent gain implied by fixed-compute capability growth and the compute slope (multiplier); a check on the paper's own 6x",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-implied-compute-growth",
        lambda q: math.exp(
            (q["comp-rosetta-frontier-growth"] - q["comp-rosetta-fixed-growth"]) / q["comp-rosetta-k"]
        ),
        "exp((comp-rosetta-frontier-growth - comp-rosetta-fixed-growth) / comp-rosetta-k)",
        fmt=".1f",
        label="yearly growth of frontier training compute implied by the Rosetta decomposition (multiplier); compare Epoch's measured growth",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-compute-share",
        lambda q: 1 - q["comp-rosetta-fixed-growth"] / q["comp-rosetta-frontier-growth"],
        "1 - comp-rosetta-fixed-growth / comp-rosetta-frontier-growth",
        fmt="%",
        label="share of frontier capability growth from more training compute, Rosetta decomposition, central",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-compute-share-lo",
        lambda q: 1 - q["comp-rosetta-fixed-growth-hi"] / q["comp-rosetta-frontier-growth"],
        "1 - comp-rosetta-fixed-growth-hi / comp-rosetta-frontier-growth",
        fmt="%",
        label="share of frontier capability growth from compute, Rosetta decomposition, using the fastest family's fixed-compute growth",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-compute-share-hi",
        lambda q: 1 - q["comp-rosetta-fixed-growth-lo"] / q["comp-rosetta-frontier-growth"],
        "1 - comp-rosetta-fixed-growth-lo / comp-rosetta-frontier-growth",
        fmt="%",
        label="share of frontier capability growth from compute, Rosetta decomposition, using the slowest family's fixed-compute growth",
        defined_in=here(),
    )

    L.derive(
        "comp-ho-algo-share-lo",
        lambda q: 1 - q["comp-ho-compute-share-hi"],
        "1 - comp-ho-compute-share-hi",
        fmt="%",
        label="share of language-model gains 2012 to 2023 from algorithms, low end",
        defined_in=here(),
    )
    L.derive(
        "comp-ho-algo-share-hi",
        lambda q: 1 - q["comp-ho-compute-share-lo"],
        "1 - comp-ho-compute-share-lo",
        fmt="%",
        label="share of language-model gains 2012 to 2023 from algorithms, high end",
        defined_in=here(),
    )
    L.derive(
        "comp-rosetta-algo-share",
        lambda q: q["comp-rosetta-fixed-growth"] / q["comp-rosetta-frontier-growth"],
        "comp-rosetta-fixed-growth / comp-rosetta-frontier-growth",
        fmt="%",
        label="share of frontier capability growth not from more training compute, Rosetta decomposition, central",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # A2: exchange rates, as OOM of inference per OOM of training at equal capability.

    L.derive(
        "comp-hex-exchange-oom",
        lambda q: math.log10(q["comp-hex-test-saved"]),
        "log10(comp-hex-test-saved)",
        unit="OOM",
        fmt=".2f",
        label="OOM of test-time compute that one OOM of train-time compute replaces, AlphaZero on Hex",
        defined_in=here(),
    )
    L.derive(
        "comp-exchange-cheapver",
        lambda q: q["comp-span-cheapver-inf"] / q["comp-span-cheapver-train"],
        "comp-span-cheapver-inf / comp-span-cheapver-train",
        unit="OOM",
        fmt=".1f",
        label="OOM of inference per OOM of training replaced, repeated sampling with a cheap verifier",
        defined_in=here(),
    )
    L.derive(
        "comp-exchange-expver",
        lambda q: q["comp-span-expver-inf"] / q["comp-span-expver-train"],
        "comp-span-expver-inf / comp-span-expver-train",
        unit="OOM",
        fmt=".2f",
        label="OOM of inference per OOM of training replaced, repeated sampling with an expensive verifier",
        defined_in=here(),
    )
    L.derive(
        "comp-ord-inf-per-train-lo",
        lambda q: math.log10(q["comp-ord-inf-step"]) / math.log10(q["comp-ord-pretrain-hi"]),
        "log10(comp-ord-inf-step) / log10(comp-ord-pretrain-hi)",
        unit="OOM",
        fmt=".1f",
        label="OOM of inference per OOM of pre-training matched, Ord's summary, favourable end",
        defined_in=here(),
    )
    L.derive(
        "comp-ord-inf-per-train-hi",
        lambda q: math.log10(q["comp-ord-inf-step"]) / math.log10(q["comp-ord-pretrain-lo"]),
        "log10(comp-ord-inf-step) / log10(comp-ord-pretrain-lo)",
        unit="OOM",
        fmt=".1f",
        label="OOM of inference per OOM of pre-training matched, Ord's summary, unfavourable end",
        defined_in=here(),
    )
    L.derive(
        "comp-ord-example-oom",
        lambda q: math.log10(q["comp-ord-example-target"] / q["comp-ord-example-base"]),
        "log10(comp-ord-example-target / comp-ord-example-base)",
        unit="OOM",
        fmt=".0f",
        label="OOM of training compute replaced in Ord's illustration",
        defined_in=here(),
    )
    L.derive(
        "comp-ord-example-exchange",
        lambda q: math.log10(q["comp-ord-example-inf"])
        / math.log10(q["comp-ord-example-target"] / q["comp-ord-example-base"]),
        "log10(comp-ord-example-inf) / log10(comp-ord-example-target / comp-ord-example-base)",
        unit="OOM",
        fmt=".2f",
        label="OOM of inference per OOM of training replaced in Ord's illustration",
        defined_in=here(),
    )
    L.derive(
        "comp-ord-rl-per-inf",
        lambda q: math.log10(q["comp-ord-rl-train"]) / math.log10(q["comp-ord-rl-inf"]),
        "log10(comp-ord-rl-train) / log10(comp-ord-rl-inf)",
        unit="OOM",
        fmt=".0f",
        label="OOM of RL training compute matched by one OOM of inference, Ord's reading of vendor charts",
        defined_in=here(),
    )
    L.derive(
        "comp-r1-distill-gap",
        lambda q: 100 * (q["comp-r1-distill-32b"] - q["comp-r1-rl-32b"]),
        "100 * (comp-r1-distill-32b - comp-r1-rl-32b)",
        unit="pp",
        fmt=".1f",
        label="AIME advantage of distillation from DeepSeek-R1 over RL on the same 32B base",
        defined_in=here(),
    )
    L.derive(
        "comp-r1zero-gain",
        lambda q: 100 * (q["comp-r1zero-end"] - q["comp-r1zero-start"]),
        "100 * (comp-r1zero-end - comp-r1zero-start)",
        unit="pp",
        fmt=".1f",
        label="AIME gain of DeepSeek-R1-Zero during reinforcement learning",
        defined_in=here(),
    )
    L.derive(
        "comp-monkeys-gain",
        lambda q: 100 * (q["comp-monkeys-pass250"] - q["comp-monkeys-pass1"]),
        "100 * (comp-monkeys-pass250 - comp-monkeys-pass1)",
        unit="pp",
        fmt=".1f",
        label="SWE-bench Lite gain from 1 to 250 samples with unit tests as the verifier",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # A3: halving times and claimed totals as yearly multipliers.

    L.derive(
        "comp-ho-annual",
        lambda q: 2 ** (12 / q["comp-ho-halving"]),
        "2^(12 / comp-ho-halving)",
        fmt=".1f",
        label="yearly fall in compute for fixed language-model performance, from the halving time (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-ho-annual-lo",
        lambda q: 2 ** (12 / q["comp-ho-halving-hi"]),
        "2^(12 / comp-ho-halving-hi)",
        fmt=".1f",
        label="yearly fall in compute for fixed LM performance, slow end of the 95% CI (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-ho-annual-hi",
        lambda q: 2 ** (12 / q["comp-ho-halving-lo"]),
        "2^(12 / comp-ho-halving-lo)",
        fmt=".1f",
        label="yearly fall in compute for fixed LM performance, fast end of the 95% CI (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-erdil-annual",
        lambda q: 2 ** (12 / q["comp-erdil-halving"]),
        "2^(12 / comp-erdil-halving)",
        fmt=".1f",
        label="yearly fall in compute requirements in computer vision, from the halving time (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-hernandez-annual",
        lambda q: q["comp-hernandez-gain"] ** (1 / q["comp-hernandez-years"]),
        "comp-hernandez-gain^(1 / comp-hernandez-years)",
        fmt=".1f",
        label="yearly fall in FLOP to AlexNet-level ImageNet performance, 2012 to 2019 (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-gundlach-claimed-annual",
        lambda q: q["comp-gundlach-claimed"] ** (1 / q["comp-algo-claim-years"]),
        "comp-gundlach-claimed^(1 / comp-algo-claim-years)",
        fmt=".1f",
        label="yearly efficiency gain implied by the claimed 2012 to 2023 total (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-gundlach-small-max",
        lambda q: q["comp-gundlach-ablation-max"] * q["comp-gundlach-other-max"],
        "comp-gundlach-ablation-max * comp-gundlach-other-max",
        fmt=",.0f",
        label="total efficiency gain at small compute, 2012 to 2023 (multiplier, upper bound)",
        defined_in=here(),
    )
    L.derive(
        "comp-gundlach-small-annual-max",
        lambda q: (q["comp-gundlach-ablation-max"] * q["comp-gundlach-other-max"])
        ** (1 / q["comp-algo-claim-years"]),
        "(comp-gundlach-ablation-max * comp-gundlach-other-max)^(1 / comp-algo-claim-years)",
        fmt=".2f",
        label="yearly efficiency gain at small compute, 2012 to 2023 (multiplier, upper bound)",
        defined_in=here(),
    )
    L.derive(
        "comp-gundlach-claimed-oom",
        lambda q: math.log10(q["comp-gundlach-claimed"]),
        "log10(comp-gundlach-claimed)",
        unit="OOM",
        fmt=".1f",
        label="claimed 2012 to 2023 language-model efficiency gain in orders of magnitude",
        defined_in=here(),
    )
    L.derive(
        "comp-gundlach-small-oom-share",
        lambda q: math.log10(q["comp-gundlach-ablation-max"] * q["comp-gundlach-other-max"])
        / math.log10(q["comp-gundlach-claimed"]),
        "log10(comp-gundlach-ablation-max * comp-gundlach-other-max) / log10(comp-gundlach-claimed)",
        fmt="%",
        label="share of the claimed orders of magnitude accounted for at small compute (upper bound)",
        defined_in=here(),
    )
    L.derive(
        "comp-hwp-multiplier",
        lambda q: 1 + q["comp-hwp-eff"],
        "1 + comp-hwp-eff",
        fmt=".2f",
        label="yearly training-efficiency multiplier in the hardwired-pause scenario",
        defined_in=here(),
    )
    L.derive(
        "comp-hwp-ratio",
        lambda q: q["comp-hwp-after"] / q["comp-hwp-before"],
        "comp-hwp-after / comp-hwp-before",
        fmt=".2f",
        label="rise in breakout capacity relative to the fleet threshold in the hardwired-pause scenario (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-hwp-check",
        lambda q: (1 + q["comp-hwp-eff"]) ** (q["comp-hwp-months"] / 12),
        "(1 + comp-hwp-eff)^(comp-hwp-months / 12)",
        fmt=".2f",
        label="efficiency gain compounded over the scenario's months (multiplier); reproduces comp-hwp-ratio",
        defined_in=here(),
    )

    # The NanoGPT speedrun: wall-clock and tokens at fixed hardware and fixed target loss.
    L.derive(
        "comp-speedrun-ratio",
        lambda q: q["comp-speedrun-base-s"] / q["comp-speedrun-record-s"],
        "comp-speedrun-base-s / comp-speedrun-record-s",
        fmt=".1f",
        label="fall in speedrun wall-clock time from record 1 to record 92 (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-speedrun-years",
        lambda q: q["comp-speedrun-days"] / 365.25,
        "comp-speedrun-days / 365.25",
        unit="years",
        fmt=".2f",
        label="years from speedrun record 1 to record 92",
        defined_in=here(),
    )
    L.derive(
        "comp-speedrun-annual",
        lambda q: (q["comp-speedrun-base-s"] / q["comp-speedrun-record-s"])
        ** (365.25 / q["comp-speedrun-days"]),
        "(comp-speedrun-base-s / comp-speedrun-record-s)^(365.25 / comp-speedrun-days)",
        fmt=".1f",
        label="average yearly fall in speedrun wall-clock time (multiplier)",
        defined_in=here(),
    )
    L.derive(
        "comp-speedrun-halving",
        lambda q: 12 * (q["comp-speedrun-days"] / 365.25) * math.log(2)
        / math.log(q["comp-speedrun-base-s"] / q["comp-speedrun-record-s"]),
        "12 * (comp-speedrun-days / 365.25) * ln 2 / ln(comp-speedrun-base-s / comp-speedrun-record-s)",
        unit="months",
        fmt=".1f",
        label="average halving time of speedrun wall-clock time",
        defined_in=here(),
    )
    L.derive(
        "comp-speedrun-token-ratio",
        lambda q: q["comp-speedrun-tokens-base"] / q["comp-speedrun-tokens-record"],
        "comp-speedrun-tokens-base / comp-speedrun-tokens-record",
        fmt=",.0f",
        label="fall in training tokens to the speedrun's target loss (multiplier, lower bound)",
        defined_in=here(),
    )
    L.derive(
        "comp-speedrun-token-annual",
        lambda q: (q["comp-speedrun-tokens-base"] / q["comp-speedrun-tokens-record"])
        ** (365.25 / q["comp-speedrun-days"]),
        "(comp-speedrun-tokens-base / comp-speedrun-tokens-record)^(365.25 / comp-speedrun-days)",
        fmt=".1f",
        label="average yearly fall in tokens to the speedrun's target loss (multiplier, lower bound)",
        defined_in=here(),
    )
    L.derive(
        "comp-metr-deep",
        lambda q: q["comp-metr-speedup"] / q["comp-metr-shallow"],
        "comp-metr-speedup / comp-metr-shallow",
        fmt=".1f",
        label="speedrun gain left for deep contributions once shallow and moderate ones are divided out (multiplier)",
        defined_in=here(),
    )

    # Years for a fixed cap to leak one OOM, at each candidate rate.
    for suffix, key, what in (
        ("ho", "comp-ho-annual", "Ho et al.'s central rate"),
        ("rosetta", "comp-rosetta-algo", "the Rosetta fit's rate"),
        ("scher", "comp-scher-algo", "the MIRI draft agreement's assumed rate"),
        ("small", "comp-gundlach-small-annual-max", "the small-compute upper bound (so a lower bound on time)"),
        ("frontier", "comp-frontier-compute-growth", "the growth of frontier training compute"),
    ):
        L.derive(
            f"comp-years-per-oom-{suffix}",
            lambda q, key=key: ln10 / math.log(q[key]),
            f"ln(10) / ln({key})",
            unit="years",
            fmt=".1f",
            label=f"years for one order of magnitude at {what}",
            defined_in=here(),
        )

    # -----------------------------------------------------------------------------------------
    # A4: where the public text stock binds, with C = 6 N D and D = tokens-per-param * N.

    L.derive(
        "comp-data-wall-check",
        lambda q: q["comp-flop-per-param-token"] * q["comp-data-stock"] ** 2
        / q["comp-chinchilla-tokens-per-param"],
        "comp-flop-per-param-token * comp-data-stock^2 / comp-chinchilla-tokens-per-param",
        unit="FLOP",
        fmt=".1e",
        label="compute-optimal training compute that uses the text stock once; reproduces the source's figure",
        defined_in=here(),
    )
    L.derive(
        "comp-data-wall-4ep",
        lambda q: q["comp-flop-per-param-token"]
        * (q["comp-data-epochs-free"] * q["comp-data-stock"]) ** 2
        / q["comp-chinchilla-tokens-per-param"],
        "comp-flop-per-param-token * (comp-data-epochs-free * comp-data-stock)^2 / comp-chinchilla-tokens-per-param",
        unit="FLOP",
        fmt=".1e",
        label="compute-optimal training compute that uses the text stock at the epochs of repetition that cost almost nothing",
        defined_in=here(),
    )
    L.derive(
        "comp-data-wall-over-scher-oom",
        lambda q: math.log10(q["comp-data-wall-flop"] / q["comp-scher-strict"]),
        "log10(comp-data-wall-flop / comp-scher-strict)",
        unit="OOM",
        fmt=".1f",
        label="how far the data wall sits above the MIRI draft agreement's strict training threshold",
        defined_in=here(),
    )
    L.derive(
        "comp-data-wall-over-eu-oom",
        lambda q: math.log10(q["comp-data-wall-flop"] / q["comp-eu-threshold"]),
        "log10(comp-data-wall-flop / comp-eu-threshold)",
        unit="OOM",
        fmt=".1f",
        label="how far the data wall sits above the EU AI Act's systemic-risk presumption",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # The combined leak of a training cap. One-off: post-training enhancements (which include
    # solution selection, so they are not added to an inference technique). Continuous: the
    # algorithmic rate at the cap's scale, bracketed by the small-compute bound and the headline
    # rates. Placeholders: the headroom and the response time.

    L.derive(
        "comp-oneoff-lo-oom",
        lambda q: math.log10(q["comp-davidson-ceg-typ"]),
        "log10(comp-davidson-ceg-typ)",
        unit="OOM",
        fmt=".1f",
        label="one-off leak of a training cap through post-training enhancement, typical",
        defined_in=here(),
    )
    L.derive(
        "comp-oneoff-hi-oom",
        lambda q: math.log10(q["comp-davidson-ceg-high"]),
        "log10(comp-davidson-ceg-high)",
        unit="OOM",
        fmt=".1f",
        label="one-off leak of a training cap through post-training enhancement, high",
        defined_in=here(),
    )
    for suffix, key, what in (
        ("ho", "comp-ho-annual", "Ho et al.'s central rate"),
        ("rosetta", "comp-rosetta-algo", "the Rosetta fit's rate"),
        ("small", "comp-gundlach-small-annual-max", "the small-compute upper bound (a lower bound on time)"),
    ):
        L.derive(
            f"comp-leak-years-{suffix}",
            lambda q, key=key: (q["comp-example-headroom-oom"] - math.log10(q["comp-davidson-ceg-high"]))
            / math.log10(q[key]),
            f"(comp-example-headroom-oom - log10(comp-davidson-ceg-high)) / log10({key})",
            unit="years",
            fmt=".1f",
            label=f"years until a capped party closes the example headroom after the high one-off leak, at {what}",
            defined_in=here(),
        )
        L.derive(
            f"comp-headroom-needed-{suffix}",
            lambda q, key=key: math.log10(q["comp-davidson-ceg-high"])
            + q["comp-response-years"] * math.log10(q[key]),
            f"log10(comp-davidson-ceg-high) + comp-response-years * log10({key})",
            unit="OOM",
            fmt=".1f",
            label=f"headroom a cap needs to outlast the placeholder response time, at {what}",
            defined_in=here(),
        )
    L.derive(
        "comp-leak-left-verifier",
        lambda q: max(q["comp-example-headroom-oom"] - q["comp-span-cheapver-train"], 0.0),
        "max(comp-example-headroom-oom - comp-span-cheapver-train, 0)",
        unit="OOM",
        fmt=".0f",
        label="example headroom left at once where a cheap verifier lets repeated sampling replace training",
        defined_in=here(),
    )
    L.derive(
        "comp-headroom-needed-verifier",
        lambda q: q["comp-span-cheapver-train"] + q["comp-response-years"] * math.log10(q["comp-ho-annual"]),
        "comp-span-cheapver-train + comp-response-years * log10(comp-ho-annual)",
        unit="OOM",
        fmt=".1f",
        label="headroom a cap needs in a domain with a cheap verifier, at Ho et al.'s central rate",
        defined_in=here(),
    )
