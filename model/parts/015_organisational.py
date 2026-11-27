"""Part I, 5: the organisational and economic perspective (research/015-organisational.md).

Derives the chapter's numbers from its inputs in data/inputs/015-organisational.toml, plus three
core inputs (inspections-per-year, detect-prob-per-inspection, breakout-years) for the comparison
with the memo's placeholder detection rate. Reads no other chapter's numbers.
"""

from __future__ import annotations

import math
import statistics

# The seven undeclared programmes in survey note 08 whose length undetected is sourced. Fordow
# enters at its short end (design work from 2006), the conservative choice for a detection rate.
COVERT = [
    "org-iraq-years",
    "org-libya-years",
    "org-iran-years",
    "org-fordow-years-low",
    "org-syria-years",
    "org-biopreparat-years",
    "org-sa-years",
]


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # O1. How fast each input grows

    L.derive(
        "org-sold-growth",
        lambda q: q["org-sold-2025"] / q["org-sold-2024"],
        "org-sold-2025 / org-sold-2024",
        fmt=",.2f",
        label="growth of AI compute sold, 2024 to 2025 (ratio)",
        defined_in=here(),
    )
    L.derive(
        "org-euv-growth-2025",
        lambda q: q["org-euv-2025"] / q["org-euv-2024"] - 1,
        "org-euv-2025 / org-euv-2024 - 1",
        fmt="%",
        label="growth in EUV systems ASML recognised, 2024 to 2025",
        defined_in=here(),
    )
    L.derive(
        "org-euv-doubling-years",
        lambda q: math.log(2) / math.log(1 + q["org-euv-capacity-growth-2027"]),
        "ln 2 / ln(1 + org-euv-capacity-growth-2027)",
        unit="years",
        fmt=",.1f",
        label="years for low-NA EUV capacity to double at ASML's planned 2027 growth rate",
        defined_in=here(),
    )
    L.derive(
        "org-cowos-doubling-years",
        lambda q: math.log(2) / math.log(1 + q["org-cowos-cagr"]),
        "ln 2 / ln(1 + org-cowos-cagr)",
        unit="years",
        fmt=",.1f",
        label="years for CoWoS capacity to double at its 2022 to 2027 growth rate",
        defined_in=here(),
    )
    L.derive(
        "org-cowos-multiple",
        lambda q: q["org-cowos-2026-low"] / q["org-cowos-dec2023-high"],
        "org-cowos-2026-low / org-cowos-dec2023-high",
        fmt=",.0f",
        label="growth of TSMC CoWoS capacity from December 2023 to 2026 (ratio, conservative ends)",
        defined_in=here(),
    )
    L.derive(
        "org-fab-years",
        lambda q: q["org-fab-days"] / 365.25,
        "org-fab-days / 365.25",
        unit="years",
        fmt=",.1f",
        label="average fab build time worldwide, 1990 to 2020, in years",
        defined_in=here(),
    )
    L.derive(
        "org-fab-years-us",
        lambda q: q["org-fab-days-us"] / 365.25,
        "org-fab-days-us / 365.25",
        unit="years",
        fmt=",.1f",
        label="average US fab build time, 2010 to 2020, in years",
        defined_in=here(),
    )
    L.derive(
        "org-interconnect-years",
        lambda q: q["org-interconnect-2025"] / 12,
        "org-interconnect-2025 / 12",
        unit="years",
        fmt=",.1f",
        label="median US interconnection time for projects built in 2025, in years",
        defined_in=here(),
    )
    L.derive(
        "org-transformer-years",
        lambda q: q["org-transformer-lead"] * 7 / 365.25,
        "org-transformer-lead * 7 / 365.25",
        unit="years",
        fmt=",.1f",
        label="average US power transformer lead time, in years",
        defined_in=here(),
    )
    L.derive(
        "org-turbine-backlog",
        lambda q: q["org-turbine-gev"] + q["org-turbine-siemens"] + q["org-turbine-mhi"],
        "org-turbine-gev + org-turbine-siemens + org-turbine-mhi",
        unit="GW",
        fmt=",.0f",
        label="combined gas turbine backlog of the three large-frame makers",
        defined_in=here(),
    )
    L.derive(
        "org-china-renewables-2025",
        lambda q: q["org-china-solar-2025"] + q["org-china-wind-2025"],
        "org-china-solar-2025 + org-china-wind-2025",
        unit="GW",
        fmt=",.0f",
        label="solar and wind capacity China added in 2025",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # O3. Leaks and the cost of denial

    L.derive(
        "org-huawei-spread",
        lambda q: q["org-huawei-idc-2025"] / q["org-huawei-commerce-2025"],
        "org-huawei-idc-2025 / org-huawei-commerce-2025",
        fmt=",.1f",
        label="spread of outside estimates of Huawei's 2025 AI chip output (highest over lowest)",
        note="units differ: Commerce gave capacity, IDC shipments; the spread is still the measured disagreement",
        defined_in=here(),
    )
    L.derive(
        "org-china-implied-stock",
        lambda q: q["org-smuggled-cum"] / q["org-smuggled-share-china"] / 1e6,
        "org-smuggled-cum / org-smuggled-share-china / 1e6",
        unit="million H100e",
        fmt=",.1f",
        label="China's total AI compute at end 2025 implied by the smuggling estimate and its share",
        note="an inference from 'roughly a third', not a number the source states",
        defined_in=here(),
    )
    L.derive(
        "org-denial-power-multiplier",
        lambda q: 1 / q["org-china-compute-per-power"],
        "1 / org-china-compute-per-power",
        fmt=",.1f",
        label="power needed per unit of compute in China relative to leading US facilities",
        defined_in=here(),
    )
    L.derive(
        "org-smuggling-profit-ratio",
        lambda q: q["org-smuggling-profit-3"] / q["org-bis-enforcement"],
        "org-smuggling-profit-3 / org-bis-enforcement",
        fmt=",.1f",
        label="profits of three smuggling cases over BIS's annual export enforcement budget",
        defined_in=here(),
    )
    L.derive(
        "org-smuggled-share-of-fe",
        lambda q: q["org-smuggled-cum"] / (q["org-hwp-fe"] * 1e6),
        "org-smuggled-cum / (org-hwp-fe * 1e6)",
        fmt="%",
        label="compute smuggled into China through 2025 as a share of the hardwired-pause covert evasion threshold",
        defined_in=here(),
    )
    L.derive(
        "org-china-stock-share-of-fe",
        lambda q: q["org-china-implied-stock"] / q["org-hwp-fe"],
        "org-china-implied-stock / org-hwp-fe",
        fmt="%",
        label="China's implied total AI compute as a share of the hardwired-pause covert evasion threshold",
        defined_in=here(),
    )
    L.derive(
        "org-fe-years-of-sales",
        lambda q: q["org-hwp-fe"] / q["org-sold-2025"],
        "org-hwp-fe / org-sold-2025",
        unit="years",
        fmt=",.2f",
        label="the covert evasion threshold in years of 2025 global AI chip sales",
        defined_in=here(),
    )
    L.derive(
        "org-fb-years-of-sales",
        lambda q: q["org-hwp-fb"] / q["org-sold-2025"],
        "org-hwp-fb / org-sold-2025",
        unit="years",
        fmt=",.0f",
        label="the overt breakout threshold in years of 2025 global AI chip sales",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # O2. Races and coalitions

    L.derive(
        "org-gan-catchup-fall",
        lambda q: 1 - q["org-gan-catchup-24"] / q["org-gan-catchup-start"],
        "1 - org-gan-catchup-24 / org-gan-catchup-start",
        fmt="%",
        label="fall in catch-up time over a 24-month compliant pause in Gan's calibration",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # O4. Covert programmes: how long they ran, and the detection rate the record implies

    L.derive(
        "org-opcw-insp-total",
        lambda q: q["org-opcw-cw-insp"] + q["org-opcw-ind-insp"],
        "org-opcw-cw-insp + org-opcw-ind-insp",
        unit="inspections",
        fmt=",.0f",
        label="OPCW routine inspections since 1997 (sum of categories)",
        defined_in=here(),
    )
    L.derive(
        "org-fraud-quitam-ratio",
        lambda q: q["org-fraud-quitam"] / q["org-fraud-other"],
        "org-fraud-quitam / org-fraud-other",
        fmt=",.1f",
        label="employees' share of fraud revelations where qui tam rewards apply, over other industries",
        defined_in=here(),
    )
    L.derive(
        "org-covert-years-min",
        lambda q: min(q[k] for k in COVERT),
        "min(" + ", ".join(COVERT) + ")",
        unit="years",
        fmt=",.0f",
        label="shortest time undetected among the seven undeclared programmes",
        defined_in=here(),
    )
    L.derive(
        "org-covert-years-median",
        lambda q: statistics.median(q[k] for k in COVERT),
        "median(" + ", ".join(COVERT) + ")",
        unit="years",
        fmt=",.0f",
        label="median time undetected among the seven undeclared programmes",
        defined_in=here(),
    )
    L.derive(
        "org-covert-years-sum",
        lambda q: sum(q[k] for k in COVERT),
        "sum(" + ", ".join(COVERT) + ")",
        unit="years",
        fmt=",.0f",
        label="programme-years undetected across the seven undeclared programmes",
        defined_in=here(),
    )
    L.derive(
        "org-covert-hazard",
        lambda q: len(COVERT) / q["org-covert-years-sum"],
        "7 / org-covert-years-sum",
        unit="/yr",
        fmt=",.2f",
        label="discovery rate a year implied by the seven programmes (discoveries over programme-years)",
        note="a convenience sample of programmes that were eventually found; programmes never found are missing",
        defined_in=here(),
    )
    L.derive(
        "org-covert-detect-1y",
        lambda q: 1 - math.exp(-q["org-covert-hazard"] * q["breakout-years"]),
        "1 - exp(-org-covert-hazard * breakout-years)",
        fmt="%",
        label="chance a covert programme is found within the memo's placeholder breakout time, at the historical rate",
        defined_in=here(),
    )
    L.derive(
        "org-covert-detect-5y",
        lambda q: 1 - math.exp(-q["org-covert-hazard"] * q["org-sa-decision-device"]),
        "1 - exp(-org-covert-hazard * org-sa-decision-device)",
        fmt="%",
        label="chance a covert programme is found within South Africa's decision-to-device time, at the historical rate",
        defined_in=here(),
    )
    L.derive(
        "org-memo-detect-rate",
        lambda q: q["inspections-per-year"] * q["detect-prob-per-inspection"],
        "inspections-per-year * detect-prob-per-inspection",
        unit="/yr",
        fmt=",.1f",
        label="detection rate a year implied by the memo's placeholder inspection channel",
        defined_in=here(),
    )
    L.derive(
        "org-memo-to-history",
        lambda q: q["org-memo-detect-rate"] / q["org-covert-hazard"],
        "org-memo-detect-rate / org-covert-hazard",
        fmt=",.0f",
        label="the memo's placeholder detection rate over the historical discovery rate",
        defined_in=here(),
    )
