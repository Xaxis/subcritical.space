"""Part I, 1: the physical and energetic perspective (research/011-physical.md).

Derives P1 (compute budget), P2 (energy per useful operation and its headroom), P3 (memory and
bandwidth) and P4 (the footprint floor, per site and in aggregate) from the inputs in
data/inputs/011-physical.toml. Every id starts with phys-.

Unit conversions are written out in each formula. A month is a twelfth of a Julian year.
"""

from __future__ import annotations

import math

YEAR_S = 365.25 * 86400  # seconds in a Julian year, a unit conversion
MONTH_S = YEAR_S / 12
MWH_J = 3.6e9  # joules in a megawatt-hour


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # P2. The Landauer floor and how far real hardware sits above it

    L.derive(
        "phys-kt-ln2-room",
        lambda q: q["phys-boltzmann-k"] * q["phys-temp-room"] * math.log(2),
        "phys-boltzmann-k * phys-temp-room * ln 2",
        unit="J",
        fmt=".3e",
        label="Landauer bound per erased bit at room temperature",
        defined_in=here(),
    )
    L.derive(
        "phys-kt-ln2-body",
        lambda q: q["phys-boltzmann-k"] * q["phys-temp-body"] * math.log(2),
        "phys-boltzmann-k * phys-temp-body * ln 2",
        unit="J",
        fmt=".3e",
        label="Landauer bound per erased bit at body temperature",
        defined_in=here(),
    )
    L.derive(
        "phys-ln2",
        lambda q: math.log(2),
        "ln 2",
        unit="kT per bit",
        fmt=".3f",
        label="Landauer's bound in units of kT per erased bit",
        defined_in=here(),
    )
    L.derive(
        "phys-berut-1ns",
        lambda q: math.log(2) + q["phys-berut-fit-b"] / (q["phys-fast-erasure"] * 1e-9),
        "ln 2 + phys-berut-fit-b / (phys-fast-erasure in s)",
        unit="kT per bit",
        fmt=".1e",
        label="heat per bit if the colloidal fit held at a 1 ns erasure (extrapolated far outside the measured range)",
        defined_in=here(),
    )

    # Energy per operation at the chip, at peak and maximum power (datasheet figures)
    for chip, flops, power in (
        ("v100", "phys-v100-tensor", "phys-v100-power"),
        ("a100", "phys-a100-bf16", "phys-a100-tdp"),
        ("h100", "phys-h100-bf16", "phys-h100-tdp"),
        ("mi300x", "phys-mi300x-fp16", "phys-mi300x-tbp"),
    ):
        L.derive(
            f"phys-{chip}-j-per-flop",
            lambda q, f=flops, p=power: q[p] / (q[f] * 1e12),
            f"{power} / ({flops} * 1e12)",
            unit="J",
            fmt=".2e",
            label=f"{chip.upper()} energy per operation at dense 16-bit peak and maximum chip power",
            defined_in=here(),
        )
    L.derive(
        "phys-h100-flop-per-j",
        lambda q: q["phys-h100-bf16"] * 1e12 / q["phys-h100-tdp"],
        "phys-h100-bf16 * 1e12 / phys-h100-tdp",
        unit="FLOP/J",
        fmt=".2e",
        label="H100 SXM operations per joule at dense BF16 peak and 700 W",
        defined_in=here(),
    )
    L.derive(
        "phys-b200-bf16",
        lambda q: q["phys-dgx-b200-fp8-sparse"] / 4 / q["phys-dgx-b200-gpus"],
        "phys-dgx-b200-fp8-sparse / 4 / phys-dgx-b200-gpus  (sparse to dense halves, FP8 to BF16 halves)",
        unit="PFLOP/s",
        fmt=".2f",
        label="B200 dense BF16 peak per GPU, from the DGX B200 figures",
        defined_in=here(),
    )
    L.derive(
        "phys-b200-system-j-per-flop",
        lambda q: (q["phys-dgx-b200-power"] * 1e3 / q["phys-dgx-b200-gpus"]) / (q["phys-b200-bf16"] * 1e15),
        "(phys-dgx-b200-power * 1e3 / phys-dgx-b200-gpus) / (phys-b200-bf16 * 1e15)",
        unit="J",
        fmt=".2e",
        label="B200 energy per operation at dense BF16 peak, measured at the DGX system wall",
        defined_in=here(),
    )
    L.derive(
        "phys-h100-landauer-ratio",
        lambda q: q["phys-h100-j-per-flop"] / q["phys-kt-ln2-room"],
        "phys-h100-j-per-flop / phys-kt-ln2-room",
        fmt=".1e",
        label="H100 energy per operation over kT ln 2 at 300 K (per operation against per bit: an upper bound on headroom)",
        defined_in=here(),
    )
    L.derive(
        "phys-cmos-landauer-ratio",
        lambda q: (1 / q["phys-cmos-ceiling-fp16"]) / q["phys-kt-ln2-room"],
        "(1 / phys-cmos-ceiling-fp16) / phys-kt-ln2-room",
        fmt=".1e",
        label="energy per FP16 operation at the CMOS ceiling over kT ln 2 at 300 K",
        defined_in=here(),
    )
    L.derive(
        "phys-cmos-headroom",
        lambda q: q["phys-cmos-ceiling-fp16"] / q["phys-h100-flop-per-j"],
        "phys-cmos-ceiling-fp16 / phys-h100-flop-per-j",
        fmt=",.0f",
        label="efficiency gain left between the H100 and the estimated CMOS ceiling (median)",
        defined_in=here(),
    )
    L.derive(
        "phys-cmos-headroom-p05",
        lambda q: q["phys-cmos-headroom"] * 10 ** (-1.645 * q["phys-cmos-log-sd"]),
        "phys-cmos-headroom * 10^(-1.645 * phys-cmos-log-sd)",
        fmt="sig2",
        label="5th percentile of the CMOS headroom if the ceiling is log-normal with Ho et al.'s spread",
        defined_in=here(),
    )
    L.derive(
        "phys-cmos-headroom-p95",
        lambda q: q["phys-cmos-headroom"] * 10 ** (1.645 * q["phys-cmos-log-sd"]),
        "phys-cmos-headroom * 10^(1.645 * phys-cmos-log-sd)",
        fmt="sig2",
        label="95th percentile of the CMOS headroom if the ceiling is log-normal with Ho et al.'s spread",
        defined_in=here(),
    )
    L.derive(
        "phys-years-to-cmos-slow",
        lambda q: math.log(q["phys-cmos-headroom"]) / math.log(q["phys-eff-growth-supercomputer"]),
        "ln(phys-cmos-headroom) / ln(phys-eff-growth-supercomputer)",
        unit="years",
        fmt=".0f",
        label="years to the CMOS ceiling at the measured supercomputer efficiency trend",
        defined_in=here(),
    )
    L.derive(
        "phys-years-to-cmos-fast",
        lambda q: math.log(q["phys-cmos-headroom"]) / math.log(q["phys-eff-growth-gpu"]),
        "ln(phys-cmos-headroom) / ln(phys-eff-growth-gpu)",
        unit="years",
        fmt=".0f",
        label="years to the CMOS ceiling at the measured GPU efficiency trend",
        defined_in=here(),
    )

    # Energy per useful operation at the facility: chip, server overhead, cooling, utilisation
    L.derive(
        "phys-it-power-per-h100",
        lambda q: q["phys-colossus1-it-power"] * 1e6 / q["phys-colossus1-h100"],
        "phys-colossus1-it-power * 1e6 / phys-colossus1-h100",
        unit="W",
        fmt="sig3",
        label="IT power per H100 at Colossus 1 (chip, host, memory, network)",
        defined_in=here(),
    )
    L.derive(
        "phys-facility-power-per-h100",
        lambda q: q["phys-colossus1-facility-power"] * 1e6 / q["phys-colossus1-h100"],
        "phys-colossus1-facility-power * 1e6 / phys-colossus1-h100",
        unit="W",
        fmt="sig3",
        label="facility power per H100 at Colossus 1, cooling included",
        defined_in=here(),
    )
    L.derive(
        "phys-it-overhead",
        lambda q: q["phys-it-power-per-h100"] / q["phys-h100-tdp"],
        "phys-it-power-per-h100 / phys-h100-tdp",
        fmt=".2f",
        label="IT power per H100 over the chip's maximum power (server overhead factor)",
        defined_in=here(),
    )
    L.derive(
        "phys-pue-colossus",
        lambda q: q["phys-colossus1-facility-power"] / q["phys-colossus1-it-power"],
        "phys-colossus1-facility-power / phys-colossus1-it-power",
        fmt=".2f",
        label="facility over IT power at Colossus 1 (power usage effectiveness)",
        defined_in=here(),
    )
    L.derive(
        "phys-facility-j-per-useful-flop",
        lambda q: q["phys-facility-power-per-h100"] / (q["phys-h100-bf16"] * 1e12 * q["phys-util-ref"]),
        "phys-facility-power-per-h100 / (phys-h100-bf16 * 1e12 * phys-util-ref)",
        unit="J",
        fmt=".2e",
        label="facility energy per useful 16-bit operation on H100s at the reference utilisation",
        defined_in=here(),
    )
    L.derive(
        "phys-facility-over-chip",
        lambda q: q["phys-facility-j-per-useful-flop"] / q["phys-h100-j-per-flop"],
        "phys-facility-j-per-useful-flop / phys-h100-j-per-flop",
        fmt=".1f",
        label="facility energy per useful operation over the datasheet figure",
        defined_in=here(),
    )
    L.derive(
        "phys-facility-headroom",
        lambda q: q["phys-cmos-headroom"] * q["phys-facility-over-chip"],
        "phys-cmos-headroom * phys-facility-over-chip",
        fmt="sig2",
        label="most the facility energy per useful operation could fall: CMOS headroom times removing every overhead",
        defined_in=here(),
    )
    L.derive(
        "phys-epoch-dc-it-per-h100e",
        lambda q: q["phys-epoch-dc-it-power"] * 1e9 / q["phys-epoch-dc-h100e"],
        "phys-epoch-dc-it-power * 1e9 / phys-epoch-dc-h100e",
        unit="W",
        fmt="sig3",
        label="IT power per H100-equivalent across the sites in Epoch's database",
        defined_in=here(),
    )
    L.derive(
        "phys-scher-w-per-h100",
        lambda q: q["phys-scher-5000-h100"] * 1e6 / q["phys-scher-h100-count"],
        "phys-scher-5000-h100 * 1e6 / phys-scher-h100-count",
        unit="W",
        fmt="sig3",
        label="power per H100 implied by Scher and Thiergart's 5,000-H100 example",
        defined_in=here(),
    )
    L.derive(
        "phys-sastry-w-per-h100",
        lambda q: q["phys-sastry-dgx-kw"] * 1e3 / q["phys-sastry-dgx-chips"],
        "phys-sastry-dgx-kw * 1e3 / phys-sastry-dgx-chips",
        unit="W",
        fmt="sig3",
        label="power per H100 implied by Sastry et al.'s DGX figure",
        defined_in=here(),
    )

    L.derive(
        "phys-power-per-chip-spread",
        lambda q: q["phys-facility-power-per-h100"] / q["phys-epoch-dc-it-per-h100e"],
        "phys-facility-power-per-h100 / phys-epoch-dc-it-per-h100e",
        fmt=".1f",
        label="spread between the highest and lowest power per H100-equivalent among the sources",
        defined_in=here(),
    )
    L.derive(
        "phys-util-spread",
        lambda q: q["phys-pope-mfu-prefill"] / q["phys-intellect1-mfu-low"],
        "phys-pope-mfu-prefill / phys-intellect1-mfu-low",
        fmt=".1f",
        label="spread of measured utilisation between the sources",
        defined_in=here(),
    )

    # The brain as a reference
    L.derive(
        "phys-brain-flop-per-j",
        lambda q: q["phys-brain-flops-central"] / q["phys-brain-power"],
        "phys-brain-flops-central / phys-brain-power",
        unit="FLOP/J",
        fmt=".0e",
        label="brain operations per joule at Carlsmith's central figure and 20 W",
        defined_in=here(),
    )
    L.derive(
        "phys-brain-over-h100",
        lambda q: q["phys-brain-flop-per-j"] / q["phys-h100-flop-per-j"],
        "phys-brain-flop-per-j / phys-h100-flop-per-j",
        fmt=",.0f",
        label="how many times more energy-efficient the brain is than an H100, at Carlsmith's central figure",
        defined_in=here(),
    )
    L.derive(
        "phys-cmos-over-brain",
        lambda q: q["phys-cmos-ceiling-fp16"] / q["phys-brain-flop-per-j"],
        "phys-cmos-ceiling-fp16 / phys-brain-flop-per-j",
        fmt=".1f",
        label="CMOS ceiling over the brain's efficiency at Carlsmith's central figure",
        defined_in=here(),
    )
    L.derive(
        "phys-brain-landauer-cap",
        lambda q: q["phys-brain-power"] / q["phys-kt-ln2-body"],
        "phys-brain-power / phys-kt-ln2-body",
        unit="bits/s",
        fmt=".1e",
        label="most bit erasures a second a 20 W brain could perform at body temperature",
        defined_in=here(),
    )
    L.derive(
        "phys-h100-brains",
        lambda q: q["phys-h100-bf16"] * 1e12 / q["phys-brain-flops-central"],
        "phys-h100-bf16 * 1e12 / phys-brain-flops-central",
        fmt=".2f",
        label="one H100's dense BF16 peak in brains at Carlsmith's central figure (raw operations only)",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # P1. Compute budget: growth, the yearly chip flow, and copies at a speed

    L.derive(
        "phys-algo-growth",
        lambda q: 2 ** (12 / q["phys-algo-halving"]),
        "2^(12 / phys-algo-halving)",
        fmt=".1f",
        label="yearly algorithmic efficiency factor implied by an 8.4-month halving",
        defined_in=here(),
    )
    L.derive(
        "phys-algo-growth-low",
        lambda q: 2 ** (12 / q["phys-algo-halving-high"]),
        "2^(12 / phys-algo-halving-high)",
        fmt=".1f",
        label="yearly algorithmic efficiency factor at the slow end of the 95% CI",
        defined_in=here(),
    )
    L.derive(
        "phys-algo-growth-high",
        lambda q: 2 ** (12 / q["phys-algo-halving-low"]),
        "2^(12 / phys-algo-halving-low)",
        fmt=".1f",
        label="yearly algorithmic efficiency factor at the fast end of the 95% CI",
        defined_in=here(),
    )
    L.derive(
        "phys-effective-growth",
        lambda q: q["phys-frontier-compute-growth"] * q["phys-algo-growth"],
        "phys-frontier-compute-growth * phys-algo-growth",
        fmt=",.0f",
        label="yearly growth of frontier effective compute if the headline rates simply multiply",
        defined_in=here(),
    )
    L.derive(
        "phys-ord-train-equiv",
        lambda q: q["phys-ord-train-large"] / q["phys-ord-train-small"],
        "phys-ord-train-large / phys-ord-train-small",
        fmt=",.0f",
        label="training compute factor matched by Ord's 10,000x inference illustration",
        defined_in=here(),
    )
    L.derive(
        "phys-flow-2025-flops",
        lambda q: q["phys-chips-sold-2025"] * q["phys-h100-bf16"] * 1e12,
        "phys-chips-sold-2025 * phys-h100-bf16 * 1e12",
        unit="FLOP/s",
        fmt=".1e",
        label="dense BF16 peak of one year's AI chip sales (2025)",
        defined_in=here(),
    )
    L.derive(
        "phys-flow-2025-growth",
        lambda q: q["phys-chips-sold-2025"] / q["phys-chips-sold-2024"],
        "phys-chips-sold-2025 / phys-chips-sold-2024",
        fmt=".1f",
        label="growth of AI compute sold from 2024 to 2025",
        defined_in=here(),
    )
    for tag, ref, text in (
        ("central", "phys-brain-flops-central", "Carlsmith's central figure"),
        ("low", "phys-brain-flops-high", "the high end of Carlsmith's range (fewest brains)"),
        ("high", "phys-brain-flops-low", "the low end of Carlsmith's range (most brains)"),
    ):
        L.derive(
            f"phys-flow-2025-brains-{tag}",
            lambda q, r=ref: q["phys-flow-2025-flops"] / q[r],
            f"phys-flow-2025-flops / {ref}",
            fmt="sig2",
            label=f"2025 chip sales at peak, in brains at {text} (raw operations, not capability)",
            defined_in=here(),
        )
    L.derive(
        "phys-pope-speed",
        lambda q: 1 / (q["phys-pope-latency"] / 1e3),
        "1 / (phys-pope-latency / 1e3)",
        unit="tokens/s",
        fmt=".1f",
        label="serial generation speed of one PaLM 540B copy in Pope et al.'s low-latency setup",
        defined_in=here(),
    )
    L.derive(
        "phys-palm-copy-flops",
        lambda q: q["phys-flop-per-param-token"] * q["phys-palm-params"] * 1e9 * q["phys-pope-speed"],
        "phys-flop-per-param-token * phys-palm-params * 1e9 * phys-pope-speed",
        unit="FLOP/s",
        fmt=".1e",
        label="useful operations a second one PaLM 540B copy needs at that speed",
        defined_in=here(),
    )
    L.derive(
        "phys-flow-2025-copies",
        lambda q: q["phys-flow-2025-flops"] * q["phys-util-ref"] / q["phys-palm-copy-flops"],
        "phys-flow-2025-flops * phys-util-ref / phys-palm-copy-flops",
        fmt="sig2",
        label="upper bound on PaLM-540B-sized copies at Pope et al.'s small-batch speed that one year's chip sales could run at the reference utilisation (that utilisation needs large batches, which slow each copy)",
        defined_in=here(),
    )
    L.derive(
        "phys-colossus1-run",
        lambda q: q["phys-colossus1-h100"] * q["phys-h100-bf16"] * 1e12 * q["phys-util-ref"]
        * q["phys-rahman-run-now"] * MONTH_S,
        "phys-colossus1-h100 * phys-h100-bf16 * 1e12 * phys-util-ref * phys-rahman-run-now * (seconds a month)",
        unit="FLOP",
        fmt=".1e",
        label="training compute Colossus 1 at 100,000 H100 could do in Rahman's 4.5-month run",
        defined_in=here(),
    )
    L.derive(
        "phys-miri-cap-years-strict",
        lambda q: q["phys-miri-strict"] / (q["phys-miri-cluster-cap"] * q["phys-h100-bf16"] * 1e12 * q["phys-util-ref"]) / YEAR_S,
        "phys-miri-strict / (phys-miri-cluster-cap * phys-h100-bf16 * 1e12 * phys-util-ref) / (seconds a year)",
        unit="years",
        fmt=".1f",
        label="years a 16-H100 cluster needs for 1e24 FLOP at dense BF16 and the reference utilisation",
        defined_in=here(),
    )
    L.derive(
        "phys-miri-cap-pause-flop",
        lambda q: q["phys-miri-cluster-cap"] * q["phys-h100-bf16"] * 1e12 * q["phys-util-ref"]
        * q["phys-rahman-run-pause"] * MONTH_S,
        "phys-miri-cluster-cap * phys-h100-bf16 * 1e12 * phys-util-ref * phys-rahman-run-pause * (seconds a month)",
        unit="FLOP",
        fmt=".1e",
        label="training compute one 16-H100 cluster does over the two-year run a pause makes rational",
        defined_in=here(),
    )
    L.derive(
        "phys-fp8-over-bf16",
        lambda q: q["phys-h100-fp8"] / q["phys-h100-bf16"],
        "phys-h100-fp8 / phys-h100-bf16",
        fmt=",.0f",
        label="factor by which counting FP8 instead of BF16 operations raises an H100's peak",
        defined_in=here(),
    )
    L.derive(
        "phys-fp4-over-fp16-ceiling",
        lambda q: q["phys-cmos-ceiling-fp4"] / q["phys-cmos-ceiling-fp16"],
        "phys-cmos-ceiling-fp4 / phys-cmos-ceiling-fp16",
        fmt=",.0f",
        label="factor between the FP4 and FP16 CMOS ceilings",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # P3. Memory and bandwidth

    L.derive(
        "phys-gb200-bf16",
        lambda q: q["phys-gb200-rack-bf16-sparse"] / 2 / q["phys-gb200-rack-gpus"],
        "phys-gb200-rack-bf16-sparse / 2 / phys-gb200-rack-gpus",
        unit="PFLOP/s",
        fmt=".1f",
        label="GB200 dense BF16 peak per GPU",
        defined_in=here(),
    )
    L.derive(
        "phys-gb200-hbm-bw",
        lambda q: q["phys-gb200-rack-hbm-bw"] / q["phys-gb200-rack-gpus"],
        "phys-gb200-rack-hbm-bw / phys-gb200-rack-gpus",
        unit="TB/s",
        fmt=".0f",
        label="GB200 HBM bandwidth per GPU",
        defined_in=here(),
    )
    L.derive(
        "phys-gb200-nvlink",
        lambda q: q["phys-gb200-rack-nvlink"] / q["phys-gb200-rack-gpus"],
        "phys-gb200-rack-nvlink / phys-gb200-rack-gpus",
        unit="TB/s",
        fmt=".1f",
        label="GB200 NVLink bandwidth per GPU",
        defined_in=here(),
    )
    for chip, bw, scale_bw, flops, scale_f in (
        ("v100", "phys-v100-hbm-bw", 1e9, "phys-v100-tensor", 1e12),
        ("a100", "phys-a100-hbm-bw", 1e9, "phys-a100-bf16", 1e12),
        ("h100", "phys-h100-hbm-bw", 1e12, "phys-h100-bf16", 1e12),
        ("mi300x", "phys-mi300x-hbm-bw", 1e12, "phys-mi300x-fp16", 1e12),
        ("gb200", "phys-gb200-hbm-bw", 1e12, "phys-gb200-bf16", 1e15),
    ):
        L.derive(
            f"phys-{chip}-bytes-per-flop",
            lambda q, b=bw, sb=scale_bw, f=flops, sf=scale_f: q[b] * sb / (q[f] * sf),
            f"{bw} / {flops} (in bytes and FLOP)",
            unit="bytes/FLOP",
            fmt=".1e",
            label=f"{chip.upper()} memory bandwidth per dense 16-bit operation",
            defined_in=here(),
        )
    L.derive(
        "phys-b200-bytes-per-flop",
        lambda q: (q["phys-dgx-b200-hbm-bw"] * 1e12 / q["phys-dgx-b200-gpus"]) / (q["phys-b200-bf16"] * 1e15),
        "(phys-dgx-b200-hbm-bw * 1e12 / phys-dgx-b200-gpus) / (phys-b200-bf16 * 1e15)",
        unit="bytes/FLOP",
        fmt=".1e",
        label="B200 memory bandwidth per dense BF16 operation",
        defined_in=here(),
    )
    L.derive(
        "phys-bytes-per-flop-fall",
        lambda q: q["phys-v100-bytes-per-flop"] / q["phys-b200-bytes-per-flop"],
        "phys-v100-bytes-per-flop / phys-b200-bytes-per-flop",
        fmt=".1f",
        label="factor by which bytes per operation fell from V100 to B200",
        defined_in=here(),
    )
    L.derive(
        "phys-flops-rise-v100-b200",
        lambda q: q["phys-b200-bf16"] * 1e15 / (q["phys-v100-tensor"] * 1e12),
        "phys-b200-bf16 * 1e15 / (phys-v100-tensor * 1e12)",
        fmt=",.0f",
        label="rise in peak 16-bit operations a second from V100 to B200",
        defined_in=here(),
    )
    L.derive(
        "phys-bw-rise-v100-b200",
        lambda q: (q["phys-dgx-b200-hbm-bw"] * 1e12 / q["phys-dgx-b200-gpus"]) / (q["phys-v100-hbm-bw"] * 1e9),
        "(phys-dgx-b200-hbm-bw * 1e12 / phys-dgx-b200-gpus) / (phys-v100-hbm-bw * 1e9)",
        fmt=".1f",
        label="rise in memory bandwidth per GPU from V100 to B200",
        defined_in=here(),
    )
    L.derive(
        "phys-scale-up-over-out",
        lambda q: q["phys-gb200-nvlink"] * 1e12 / (q["phys-scale-out-port"] * 1e9 / 8),
        "phys-gb200-nvlink * 1e12 / (phys-scale-out-port * 1e9 / 8)",
        fmt=",.0f",
        label="NVLink bandwidth per Blackwell GPU over one 400 Gbit/s scale-out port",
        defined_in=here(),
    )
    L.derive(
        "phys-nvlink-over-wan",
        lambda q: q["phys-h100-nvlink"] * 1e9 * 8 / (q["phys-rahman-bandwidth"] * 1e6),
        "phys-h100-nvlink * 1e9 * 8 / (phys-rahman-bandwidth * 1e6)",
        fmt="sig2",
        label="H100 NVLink bandwidth over the 100 Mbit/s links of Rahman's distributed configurations",
        defined_in=here(),
    )
    L.derive(
        "phys-streaming-over-dp",
        lambda q: q["phys-dp-bw-high"] / q["phys-streaming-bw-high"],
        "phys-dp-bw-high / phys-streaming-bw-high",
        fmt=",.0f",
        label="bandwidth data parallelism needs at 100B parameters over the most Streaming DiLoCo needs",
        defined_in=here(),
    )
    # The serial-speed bound: weights are read from memory once per decode step
    L.derive(
        "phys-pope-memory-bound",
        lambda q: q["phys-palm-params"] * 1e9 * q["phys-int8-bytes"] / (q["phys-pope-chips"] * q["phys-tpuv4-hbm-bw"] * 1e9) * 1e3,
        "phys-palm-params * 1e9 * phys-int8-bytes / (phys-pope-chips * phys-tpuv4-hbm-bw * 1e9), in ms",
        unit="ms",
        fmt=".1f",
        label="time to read PaLM 540B's int8 weights once from the HBM of 64 TPU v4 chips (the per-token floor)",
        defined_in=here(),
    )
    L.derive(
        "phys-pope-bound-speed",
        lambda q: 1e3 / q["phys-pope-memory-bound"],
        "1e3 / phys-pope-memory-bound",
        unit="tokens/s",
        fmt=",.0f",
        label="serial speed bound of that copy set by memory bandwidth",
        defined_in=here(),
    )
    L.derive(
        "phys-pope-over-bound",
        lambda q: q["phys-pope-latency"] / q["phys-pope-memory-bound"],
        "phys-pope-latency / phys-pope-memory-bound",
        fmt=".1f",
        label="measured latency per token over the memory-bandwidth floor",
        defined_in=here(),
    )
    L.derive(
        "phys-palm-h100-min",
        lambda q: q["phys-palm-params"] * 1e9 * q["phys-int8-bytes"] / (q["phys-h100-hbm-cap"] * 1e9),
        "phys-palm-params * 1e9 * phys-int8-bytes / (phys-h100-hbm-cap * 1e9)",
        unit="",
        fmt=".1f",
        label="H100s whose memory just holds PaLM 540B's int8 weights (no cache)",
        defined_in=here(),
    )
    L.derive(
        "phys-palm-8h100-speed",
        lambda q: q["phys-dgx-b200-gpus"] * q["phys-h100-hbm-bw"] * 1e12 / (q["phys-palm-params"] * 1e9 * q["phys-int8-bytes"]),
        "phys-dgx-b200-gpus * phys-h100-hbm-bw * 1e12 / (phys-palm-params * 1e9 * phys-int8-bytes)",
        unit="tokens/s",
        fmt=",.0f",
        label="serial speed bound of a PaLM-540B-sized int8 copy on one eight-H100 server",
        defined_in=here(),
    )
    L.derive(
        "phys-palm-8gb200-speed",
        lambda q: q["phys-dgx-b200-gpus"] * q["phys-gb200-hbm-bw"] * 1e12 / (q["phys-palm-params"] * 1e9 * q["phys-int8-bytes"]),
        "phys-dgx-b200-gpus * phys-gb200-hbm-bw * 1e12 / (phys-palm-params * 1e9 * phys-int8-bytes)",
        unit="tokens/s",
        fmt=",.0f",
        label="the same bound on eight GB200 GPUs",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # P4. The footprint floor, per site and in aggregate

    L.derive(
        "phys-node-power",
        lambda q: q["phys-rahman-gpus-per-node"] * q["phys-facility-power-per-h100"] / 1e3,
        "phys-rahman-gpus-per-node * phys-facility-power-per-h100 / 1e3",
        unit="kW",
        fmt=",.0f",
        label="facility power of one 16-H100 node at Colossus 1's power per chip (the per-site floor)",
        defined_in=here(),
    )
    L.derive(
        "phys-sat-over-node",
        lambda q: q["phys-sat-reliable"] * 1e3 / q["phys-node-power"],
        "phys-sat-reliable * 1e3 / phys-node-power",
        fmt=",.0f",
        label="satellite reliable-detection line over one node's power",
        defined_in=here(),
    )
    L.derive(
        "phys-utility-over-node",
        lambda q: q["phys-utility-study"] * 1e3 / q["phys-node-power"],
        "phys-utility-study * 1e3 / phys-node-power",
        fmt=",.0f",
        label="utility system-impact threshold over one node's power",
        defined_in=here(),
    )
    L.derive(
        "phys-rahman-1e25-eff",
        lambda q: q["phys-rahman-1e25-quality"] / q["phys-rahman-1e25-target"],
        "phys-rahman-1e25-quality / phys-rahman-1e25-target",
        fmt="%",
        label="share of local compute that counts after distribution, Rahman's 1e25 configuration",
        defined_in=here(),
    )
    L.derive(
        "phys-rahman-1e26-eff",
        lambda q: q["phys-rahman-1e26-quality"] / q["phys-rahman-1e26-local"],
        "phys-rahman-1e26-quality / phys-rahman-1e26-local",
        fmt="%",
        label="share of local compute that counts after distribution, Rahman's 1e26 configuration",
        defined_in=here(),
    )
    L.derive(
        "phys-pause-floor-factor",
        lambda q: q["phys-rahman-run-pause"] / q["phys-rahman-run-now"],
        "phys-rahman-run-pause / phys-rahman-run-now",
        fmt=".1f",
        label="factor by which a pause's longer rational run lowers the aggregate chip floor",
        defined_in=here(),
    )

    # Aggregate floor in chips: N = C / (peak * utilisation * T), in H100-equivalents
    for tag, c_id in (("1e24", "phys-miri-strict"), ("1e26", "phys-rahman-1e26-local")):
        for when, t_id in (("now", "phys-rahman-run-now"), ("pause", "phys-rahman-run-pause")):
            L.derive(
                f"phys-floor-chips-{tag}-{when}",
                lambda q, c=c_id, t=t_id: q[c] / (q["phys-h100-bf16"] * 1e12 * q["phys-util-ref"] * q[t] * MONTH_S),
                f"{c_id} / (phys-h100-bf16 * 1e12 * phys-util-ref * {t_id} * (seconds a month))",
                unit="H100e",
                fmt="sig2",
                label=f"aggregate chip floor for {tag} FLOP over {'today' if when == 'now' else 'a pause'}'s longest sensible run",
                defined_in=here(),
            )
        # Aggregate floor in energy: E = C * facility J per useful FLOP
        L.derive(
            f"phys-floor-energy-{tag}",
            lambda q, c=c_id: q[c] * q["phys-facility-j-per-useful-flop"] / MWH_J,
            f"{c_id} * phys-facility-j-per-useful-flop / (joules a MWh)",
            unit="MWh",
            fmt="sig2",
            label=f"aggregate energy floor for {tag} FLOP on H100s at Colossus 1's overheads",
            defined_in=here(),
        )
        for when, t_id in (("now", "phys-rahman-run-now"), ("pause", "phys-rahman-run-pause")):
            L.derive(
                f"phys-floor-power-{tag}-{when}",
                lambda q, t=t_id, tg=tag: q[f"phys-floor-energy-{tg}"] * MWH_J / (q[t] * MONTH_S) / 1e6,
                f"phys-floor-energy-{tag} / {t_id}, in MW",
                unit="MW",
                fmt="sig2",
                label=f"average facility power for {tag} FLOP spread over {'today' if when == 'now' else 'a pause'}'s longest sensible run",
                defined_in=here(),
            )
    L.derive(
        "phys-floor-energy-1e26-cmos",
        lambda q: q["phys-rahman-1e26-local"] / q["phys-cmos-ceiling-fp16"] / MWH_J,
        "phys-rahman-1e26-local / phys-cmos-ceiling-fp16 / (joules a MWh)",
        unit="MWh",
        fmt="sig2",
        label="chip energy for 1e26 FP16 operations at the estimated CMOS ceiling, before any overhead",
        defined_in=here(),
    )
    L.derive(
        "phys-unaccounted-over-floor-now",
        lambda q: q["phys-chips-unaccounted"] / q["phys-floor-chips-1e26-now"],
        "phys-chips-unaccounted / phys-floor-chips-1e26-now",
        fmt=",.0f",
        label="untraced chips over the 1e26 FLOP aggregate floor at today's run length",
        defined_in=here(),
    )
    L.derive(
        "phys-unaccounted-over-floor-pause",
        lambda q: q["phys-chips-unaccounted"] / q["phys-floor-chips-1e26-pause"],
        "phys-chips-unaccounted / phys-floor-chips-1e26-pause",
        fmt=",.0f",
        label="untraced chips over the 1e26 FLOP aggregate floor at a pause's run length",
        defined_in=here(),
    )
    L.derive(
        "phys-smuggled-over-floor-now",
        lambda q: q["phys-smuggled-china-low"] / q["phys-floor-chips-1e26-now"],
        "phys-smuggled-china-low / phys-floor-chips-1e26-now",
        fmt=",.0f",
        label="the low end of estimated smuggled compute over the 1e26 FLOP aggregate floor today",
        defined_in=here(),
    )
    L.derive(
        "phys-huawei-spread",
        lambda q: q["phys-huawei-semianalysis"] / q["phys-huawei-commerce"],
        "phys-huawei-semianalysis / phys-huawei-commerce",
        fmt=".1f",
        label="spread between outside estimates of Huawei's 2025 AI chip output",
        defined_in=here(),
    )
    L.derive(
        "phys-years-floor-to-cap",
        lambda q: math.log(q["phys-floor-chips-1e26-pause"] / q["phys-miri-cluster-cap"]) / math.log(q["phys-algo-miri"]),
        "ln(phys-floor-chips-1e26-pause / phys-miri-cluster-cap) / ln(phys-algo-miri)",
        unit="years",
        fmt=".0f",
        label="years until a fixed capability's chip floor (1e26 FLOP today, pause run length) falls to 16 H100e at 3x a year",
        defined_in=here(),
    )
    L.derive(
        "phys-china-additions",
        lambda q: q["phys-china-solar-2025"] + q["phys-china-wind-2025"],
        "phys-china-solar-2025 + phys-china-wind-2025",
        unit="GW",
        fmt=",.0f",
        label="solar and wind capacity China added in 2025 (nameplate)",
        defined_in=here(),
    )
    L.derive(
        "phys-china-over-2030-run",
        lambda q: q["phys-china-additions"] / q["phys-largest-run-2030-high"],
        "phys-china-additions / phys-largest-run-2030-high",
        fmt=",.0f",
        label="China's 2025 solar and wind additions over the high projection for the largest 2030 run (nameplate against draw)",
        defined_in=here(),
    )
