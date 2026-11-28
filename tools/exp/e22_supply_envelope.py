#!/usr/bin/env python3
"""E22: the supply envelope backtest. The most H100-equivalents (H100e) each of three kinds of party
could add in 2024 and 2025, computed from sourced capacities, against what was observed.

The envelope is an upper bound. For each party it takes every supply stage it can bound, sets each
stage's capacity at the high end of its sources and each conversion at its most generous (yields of
one, the chip that gets the most H100e out of the stage), and takes the smallest stage. The
observations must fall inside it; any that does not means a capacity or a conversion is wrong, and
the envelope is revised. The three parties follow Part I (O1):

1. A member with full access: the chain through TSMC's 3-5 nm logic, CoWoS packaging and the three
   allied HBM makers, which in 2024 and 2025 made every Nvidia, Google, AMD and Amazon accelerator.
   Stages: CoWoS wafers, HBM (in US dollars, the unit of Epoch's supply series) and logic wafers.
   Observation: Epoch's chip sales for those four designers [@epoch2026chipsales].
2. A denied party with a stockpile: China's domestic chain in 2024 and 2025 (Huawei's Ascend). Its
   binding stage is HBM [@patel2025ascend]: the 13 million stacks China procured before the December
   2024 control, plus CXMT's own output, capped at the 2026 projection. Logic is not bounded here (no
   source gives the Ascend die's area), which can only loosen the bound, and SemiAnalysis judges it
   not binding. Observations: outside estimates of one maker's output, Huawei's, from Epoch,
   SemiAnalysis, IDC, the US Commerce Department and the Financial Times, converted to H100e at
   Epoch's own per-unit rates.
3. A denied party without a stockpile: CXMT's HBM alone. No 2024-25 observation exists for it, so it
   is reported and not tested.

Data: Epoch's chip sales CSVs and its AI chip components dataset [epoch2026chipcomponents], whose
supply series and bill-of-materials sheet (packages per CoWoS wafer, dies per wafer, yields, HBM cost
per chip) are fetched; ledger inputs from data/numbers.json; hand-compiled analyst figures in
tools/exp/data/e22_supply_envelope.csv. Also reported: how each envelope moves with each uncertain
input (one at a time), a central reading at central inputs (an estimate, not a bound), the share of
CoWoS capacity the observed sales need at each chip's own packages per wafer, and what the envelope
implies for C7 (the budget a party could gather, and the factor phi of Proposition 1.6) and for C8
(whether the untraced pool fits, and how much undeclared output the envelope leaves room for).

Serves C7, C2 and C8. No randomness: every number is a deterministic function of the fetched files.

  .venv/bin/python tools/exp/e22_supply_envelope.py      (CPU, seconds; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import io
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127  # recorded for the contract; nothing here is random
EPOCH = "https://epoch.ai/data/"
SALES_URL = EPOCH + "ai_chip_sales_timelines_by_chip.csv"
TYPES_URL = EPOCH + "ai_chip_sales_chip_types.csv"
SUPPLY_URL = EPOCH + "ai_chip_components_supply_denominators.csv"
DESIGNER_URL = EPOCH + "ai_chip_components_quarterly_by_designer.csv"
BOM_URL = (
    "https://docs.google.com/spreadsheets/d/1aRNP14KndZ1jFZgolakgREm1Ip65KlfrIcmR8dKBI7I/"
    "export?format=csv&gid=1424568061"
)
TABLE = ROOT / "tools" / "exp" / "data" / "e22_supply_envelope.csv"

YEARS = (2024, 2025)
ALLIED = ("AMD", "Amazon", "Google", "Nvidia")  # designers whose chips go through TSMC CoWoS
DOMESTIC = ("Huawei", "Cambricon")  # China's own makers in Epoch's sales data
LEDGER = (
    "org-china-hbm-stockpile", "org-hbm-stockpile-packages", "org-cxmt-hbm-2026",
    "org-huawei-die-bank", "org-huawei-h100e-2025", "org-huawei-semianalysis-2025",
    "org-huawei-idc-2025", "org-huawei-commerce-2025", "org-sold-2024", "org-sold-2025",
    "org-smuggled-cum", "org-smuggled-cum-high", "org-china-implied-stock", "org-chips-unaccounted",
    "org-cowos-dec2023-high", "org-cowos-2026-high", "org-cowos-total-2026", "org-cowos-cagr",
    "formal-floor-bound-1e26-pause", "def-hwp-breakout-budget", "claim-hwp-frozen-frontier",
    "phys-rahman-1e26-local", "phys-h100-fp8", "def-seconds-per-year",
)


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))


def num(s: str) -> float:
    return float(s.replace(",", "").replace("$", "")) if s and s.strip() else float("nan")


def qkey(date: str) -> tuple[int, int]:
    y, m = int(date[:4]), int(date[5:7])
    return y, (m - 1) // 3 + 1


def qlabel(k: tuple[int, int]) -> str:
    return f"{k[0]}Q{k[1]}"


def main() -> int:
    res = Results("E22", "e22_supply_envelope", seed=SEED)
    sales = rows(fetch(SALES_URL, "epoch/ai_chip_sales_timelines_by_chip.csv", res,
                       what="Epoch AI chip sales, per chip and quarter"))
    types = {r["Name"]: r for r in rows(fetch(TYPES_URL, "epoch/ai_chip_sales_chip_types.csv", res,
                                              what="Epoch AI chip sales, chip types and peak rates"))}
    supply = rows(fetch(SUPPLY_URL, "epoch/ai_chip_components_supply_denominators.csv", res,
                        what="Epoch AI chip components, quarterly supply of logic, CoWoS and HBM"))
    designer = rows(fetch(DESIGNER_URL, "epoch/ai_chip_components_quarterly_by_designer.csv", res,
                          what="Epoch AI chip components, quarterly consumption by designer"))
    bom = rows(fetch(BOM_URL, "epoch/ai_chip_components_bom.csv", res,
                     what="Epoch AI chip components, bill-of-materials sheet linked from its methodology"))
    table = {r["id"]: r for r in rows(TABLE)}
    res.data("hand-compiled analyst figures with sources", TABLE.relative_to(ROOT).as_posix(), TABLE)
    T = lambda k: float(table[k]["value"])  # noqa: E731
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    L = {k: float(numbers[k]["value"]) for k in LEDGER}
    res.detail("ledger_inputs", {k: L[k] for k in sorted(L)})

    r_fp8 = L["phys-h100-fp8"] * 1e12  # one H100e is the H100's dense 8-bit rate, in OP/s
    year_s = L["def-seconds-per-year"]
    floor = L["formal-floor-bound-1e26-pause"]

    # ---------------------------------------------------------------- chips: H100e per unit
    linked: dict[str, str] = {}
    sums: dict[str, list[float]] = defaultdict(lambda: [0.0, 0.0])
    for r in sales:
        linked[r["Chip type"]] = r["Chip type (linked)"]
        if int(r["Start date"][:4]) in YEARS and r["Number of Units"]:
            sums[r["Chip type"]][0] += num(r["Number of Units"])
            sums[r["Chip type"]][1] += num(r["Compute estimate in H100e (median)"])
    chip = {}
    for name in sorted(sums):
        spec = num(types[linked[name]]["H100e"])
        implied = sums[name][1] / sums[name][0]
        chip[name] = {"spec": spec, "implied": implied, "hi": max(spec, implied),
                      "memory_gb": num(types[linked[name]]["Memory"]) / 1e9}
    res.detail("h100e_per_unit", {k: {kk: (None if v != v else round(v, 4)) for kk, v in d.items()}
                                  for k, d in chip.items()})

    # ---------------------------------------------------------------- observations: Epoch's sales
    obs = defaultdict(float)  # (year, group, reading) -> H100e
    units_by = defaultdict(float)
    for r in sales:
        y = int(r["Start date"][:4])
        if y > 2025 or not r["Compute estimate in H100e (median)"]:
            continue
        m = r["Chip manufacturer"]
        med, hi = num(r["Compute estimate in H100e (median)"]), num(r["H100e (95th percentile)"])
        u = num(r["Number of Units"]) if r["Number of Units"] else 0.0
        obs[(y, "all", "median")] += med
        units_by[(y, "all")] += u
        grp = "allied" if m in ALLIED else "domestic" if m in DOMESTIC else "other"
        obs[(y, grp, "median")] += med
        obs[(y, grp, "row95")] += hi
        if m == "Huawei":
            obs[(y, "huawei", "median")] += med
            units_by[(y, r["Chip type"])] += u
    # Reproduction checks (identities of the data, so they stop the run rather than count as results).
    for y in YEARS:
        got, want = obs[(y, "all", "median")] / 1e6, L[f"org-sold-{y}"]
        assert abs(got / want - 1) < 0.005, f"sales sum {y}: {got:.3f} vs ledger {want}"
    assert abs(obs[(2024, "huawei", "median")] / T("epoch-huawei-2024") - 1) < 0.01
    assert abs(obs[(2025, "huawei", "median")] / L["org-huawei-h100e-2025"] - 1) < 0.01
    assert obs[(2024, "other", "median")] == 0 and obs[(2025, "other", "median")] == 0

    # ---------------------------------------------------------------- party 1: the allied chain
    sup = {}
    for r in supply:
        q, y = r["Quarter"].split()
        k = (int(y), int(q[1]))
        sup[k] = {f"{stage}-{p}": num(r[f"{col} ({pct})"])
                  for stage, col in (("cowos", "CoWoS supply"), ("logic", "Logic supply"), ("hbm", "HBM supply (USD)"))
                  for p, pct in (("p5", "5th percentile"), ("p50", "median"), ("p95", "95th percentile"))}
    quarters = sorted(k for k in sup if k[0] in YEARS)
    assert len(quarters) == 8, quarters

    # CoWoS capacity paths from the ledger's anchors, monthly and summed by quarter (sensitivities).
    def path(start_wpm: float, factor_per_year: float) -> dict:
        out = defaultdict(float)
        for m in range(1, 25):  # January 2024 is month 1 after the December 2023 anchor
            out[(2024 + (m - 1) // 12, ((m - 1) % 12) // 3 + 1)] += start_wpm * factor_per_year ** (m / 12)
        return out

    a0 = L["org-cowos-dec2023-high"]
    paths = {
        "ledger, TSMC to its 2026 high": path(a0, (L["org-cowos-2026-high"] / a0) ** (1 / 3)),
        "ledger, with partners to 2026's total": path(a0, (L["org-cowos-total-2026"] / a0) ** (1 / 3)),
        "TSMC's claimed growth from December 2023": path(a0, 1 + L["org-cowos-cagr"]),
    }
    end2024 = {k: a0 * f ** 1 for k, f in (
        ("ledger, TSMC to its 2026 high", (L["org-cowos-2026-high"] / a0) ** (1 / 3)),
        ("ledger, with partners to 2026's total", (L["org-cowos-total-2026"] / a0) ** (1 / 3)),
        ("TSMC's claimed growth from December 2023", 1 + L["org-cowos-cagr"]))}

    bomq = defaultdict(list)
    for r in bom:
        if not r["Year"]:
            continue
        k = (int(r["Year"]), int(r["Quarter"]))
        name = r["Chip"]
        if name not in chip:
            raise SystemExit(f"{name} is in the bill of materials but not in the sales data")
        bomq[k].append({
            "chip": name, "ppw": num(r["Packages per wafer"]), "dpw": num(r["Dies per wafer"]),
            "chiplets": num(r["Chiplets per GPU"]), "node": num(r["Logic die process node"]),
            "logic_yield": num(r["Logic Die Yields"]), "hbm_usd": num(r["hbm_cost_usd"]),
            # The sheet's columns say "yield loss" but hold the surviving fraction (0.85 to 0.99),
            # which its methodology divides by: CoWoS wafers = units / (PPW x packaging yield).
            "y_p5": num(r["Packaging yield loss (p5)"]), "y_p50": num(r["Packaging yield loss (median)"]),
            "y_p95": num(r["Packaging yield loss (p95)"]),
        })

    def allied_quarter(k, cowos_cap, logic_cap, hbm_cap, ymode="one", hmode="hi", exclude=()):
        """Each stage's bound for one quarter, in H100e, and the chip that sets it."""
        cs = [c for c in bomq[k] if c["chip"] not in exclude]
        h = lambda c: chip[c["chip"]][hmode]  # noqa: E731
        py = (lambda c: 1.0) if ymode == "one" else (lambda c: c[f"y_{ymode}"])  # noqa: E731
        ly = (lambda c: 1.0) if ymode == "one" else (lambda c: c["logic_yield"])  # noqa: E731
        best_cowos = max(cs, key=lambda c: c["ppw"] * py(c) * h(c))
        best_hbm = min(cs, key=lambda c: c["hbm_usd"] / h(c))
        lc = [c for c in cs if c["node"] <= 5]  # 3-5 nm logic only; Trainium1 is a 7 nm chip
        best_logic = max(lc, key=lambda c: c["dpw"] * ly(c) / c["chiplets"] * h(c))
        stages = {
            "cowos": cowos_cap * best_cowos["ppw"] * py(best_cowos) * h(best_cowos),
            "hbm": hbm_cap / (best_hbm["hbm_usd"] / h(best_hbm)),
            "logic": logic_cap * best_logic["dpw"] * ly(best_logic) / best_logic["chiplets"] * h(best_logic),
        }
        bind = min(stages, key=stages.get)
        return stages, bind, {"cowos": best_cowos["chip"], "hbm": best_hbm["chip"], "logic": best_logic["chip"]}

    def allied_env(cowos="p95", logic="p95", hbm="p95", ymode="one", hmode="hi", exclude=(), detail=False):
        per_year = defaultdict(float)
        quarterly = []
        for k in quarters:
            cc = paths[cowos][k] if cowos in paths else sup[k][f"cowos-{cowos}"]
            st, bind, best = allied_quarter(k, cc, sup[k][f"logic-{logic}"], sup[k][f"hbm-{hbm}"],
                                            ymode, hmode, exclude)
            per_year[k[0]] += st[bind]
            quarterly.append({"quarter": qlabel(k), "cowos_wafers": round(cc), "binding": bind,
                              **{f"{s}_bound_h100e": round(v) for s, v in st.items()},
                              **{f"best_chip_{s}": v for s, v in best.items()}})
        return (dict(per_year), quarterly) if detail else dict(per_year)

    env, env_q = allied_env(detail=True)
    central = allied_env(cowos="p50", logic="p50", hbm="p50", ymode="p50", hmode="implied")
    for y in YEARS:
        assert env[y] >= central[y]
    binding = sorted({q["binding"] for q in env_q})
    res.detail("member_quarters_upper_bound", env_q)
    stage_totals = {str(y): {s: sum(q[f"{s}_bound_h100e"] for q in env_q if q["quarter"].startswith(str(y)))
                             for s in ("cowos", "hbm", "logic")} for y in YEARS}
    res.detail("member_stage_totals_upper_bound", stage_totals)

    # The H100e each chip gets from one CoWoS wafer, for the record.
    per_wafer = {}
    for k in quarters:
        for c in bomq[k]:
            per_wafer[c["chip"]] = {"packages_per_wafer": c["ppw"], "h100e_per_unit": round(chip[c["chip"]]["hi"], 4),
                                    "h100e_per_cowos_wafer_at_yield_one": round(c["ppw"] * chip[c["chip"]]["hi"], 2)}
    res.detail("h100e_per_cowos_wafer", dict(sorted(per_wafer.items())))

    # Observed sales against the bound, and the CoWoS the observed mix needs at its own PPW.
    use = {}
    for y in YEARS:
        need = 0.0
        missing = 0.0
        for r in sales:
            if int(r["Start date"][:4]) != y or r["Chip manufacturer"] not in ALLIED or not r["Number of Units"]:
                continue
            k = qkey(r["Start date"])
            c = next((c for c in bomq[k] if c["chip"] == r["Chip type"]), None)
            if c is None:
                missing += num(r["Compute estimate in H100e (median)"])
                continue
            need += num(r["Number of Units"]) / (c["ppw"] * c["y_p50"])
        cap50 = sum(sup[k]["cowos-p50"] for k in quarters if k[0] == y)
        cap95 = sum(sup[k]["cowos-p95"] for k in quarters if k[0] == y)
        epoch_use = sum(num(r["CoWoS wafers (median)"]) for r in designer
                        if r["Designer"] != "Other" and r["Quarter"].endswith(str(y)))
        use[y] = {"wafers_needed_no_lag": round(need), "capacity_p50": round(cap50), "capacity_p95": round(cap95),
                  "share_of_p50": need / cap50, "share_of_p95": need / cap95,
                  "epoch_lagged_use_four_designers": round(epoch_use), "epoch_share_of_p50": epoch_use / cap50,
                  "h100e_without_a_bom_row": round(missing)}
    res.detail("cowos_use_by_observed_sales", use)

    # One input at a time, from the bound's setting.
    swings = {}
    for y in YEARS:
        s = {}
        for v in ("p5", "p50", "p95", *paths):
            s[f"CoWoS capacity: {v}"] = allied_env(cowos=v)[y]
        for v in ("p5", "p50", "p95"):
            s[f"packaging and logic yields: sheet {v}"] = allied_env(ymode=v)[y]
            s[f"HBM supply: {v}"] = allied_env(hbm=v)[y]
            s[f"logic supply: {v}"] = allied_env(logic=v)[y]
        s["H100e per unit: Epoch's spec table, not the larger of spec and sales rate"] = allied_env(hmode="spec")[y]
        s["without the densest chip (TPU v7)"] = allied_env(exclude=("TPU v7",))[y]
        s["Hopper only (H100/H200), no newer chip"] = allied_env(
            exclude=tuple(n for n in chip if n != "H100/H200"))[y]
        swings[str(y)] = {k: round(v) for k, v in s.items()}
    res.detail("member_swings", swings)

    # ---------------------------------------------------------------- party 2: China's domestic chain
    stock = L["org-china-hbm-stockpile"] * 1e6
    cxmt = L["org-cxmt-hbm-2026"] * 1e6  # cap per year, from the 2026 projection
    s910c_central = stock / (L["org-hbm-stockpile-packages"] * 1e6)  # 13M stacks for 1.6M packages
    s910c_generous = cxmt / T("semi-cxmt-910c-high")  # 2M stacks for up to 300,000 packages
    s910c_other = cxmt / T("semi-cxmt-910c-low")
    c910, b910 = chip["Ascend 910C"], chip["Ascend 910B"]
    # The 910B's stacks: no opened source gives them. Bound: Epoch's listed memory (32 GB against the
    # 910C's 128 GB) at the 910C's most generous stacks per GB. Central: HBM in proportion to compute,
    # a 910B as roughly half a 910C (an assumption).
    s910b_bound = s910c_generous * b910["memory_gb"] / c910["memory_gb"]
    s910b_central = s910c_central * b910["implied"] / c910["implied"]
    per_stack = {"Ascend 910C": c910["hi"] / s910c_generous, "Ascend 910B": b910["hi"] / s910b_bound}
    best_chip_cn = max(per_stack, key=per_stack.get)
    hps_bound = per_stack[best_chip_cn]
    hps_central = c910["implied"] / s910c_central
    cn_env = {2024: (stock + cxmt) * hps_bound, 2025: (stock + 2 * cxmt) * hps_bound}
    cn_env_cum = (stock + 2 * cxmt) * hps_bound
    cn_central_cum = stock * hps_central  # no CXMT HBM in 2024-25: it had not built the tooling
    assert cn_env_cum >= cn_central_cum

    def mix(units: float, f910c: float) -> float:
        return units * (f910c * c910["implied"] + (1 - f910c) * b910["implied"])

    f24 = units_by[(2024, "Ascend 910C")] / (units_by[(2024, "Ascend 910C")] + units_by[(2024, "Ascend 910B")])
    semi25_units = L["org-huawei-semianalysis-2025"]
    f25 = T("semi-910c-2025") / semi25_units
    cn_obs = [
        # (name, source, year or "cum", H100e, reading)
        ("Epoch, Huawei 2024", "epoch2026chipsales", 2024, obs[(2024, "huawei", "median")], "median"),
        ("Epoch, Huawei 2024", "epoch2026chipsales", 2024, T("epoch-huawei-2024-high"), "95th percentile"),
        ("Epoch, Huawei 2025", "epoch2026chipsales", 2025, obs[(2025, "huawei", "median")], "median"),
        ("Epoch, Huawei 2025", "epoch2026chipsales", 2025, T("epoch-huawei-2025-high"), "95th percentile"),
        ("Epoch, Huawei 2024 and 2025", "epoch2026chipsales", "cum",
         obs[(2024, "huawei", "median")] + obs[(2025, "huawei", "median")], "median"),
        ("Epoch, Huawei 2024 and 2025", "epoch2026chipsales", "cum",
         T("epoch-huawei-2024-high") + T("epoch-huawei-2025-high"), "sum of 95th percentiles"),
        ("Epoch, Huawei and Cambricon 2024 and 2025", "epoch2026chipsales", "cum",
         obs[(2024, "domestic", "median")] + obs[(2025, "domestic", "median")], "median"),
        ("SemiAnalysis, Ascend units 2024", "patel2025ascend", 2024, mix(T("semi-ascend-2024"), f24),
         "Epoch's 2024 mix"),
        ("SemiAnalysis, Ascend units 2024", "patel2025ascend", 2024, mix(T("semi-ascend-2024"), 0.5),
         "half 910C, the most 'a majority 910B' allows"),
        ("SemiAnalysis, Ascend units 2025", "patel2025ascend", 2025, mix(semi25_units, f25), "its own 910C count"),
        ("SemiAnalysis, Ascend units 2024 and 2025", "patel2025ascend", "cum",
         mix(T("semi-ascend-2024"), 0.5) + mix(semi25_units, f25), "upper reading"),
        ("IDC, Huawei AI chips 2025", "pan2026idc", 2025, mix(L["org-huawei-idc-2025"], f25), "SemiAnalysis's 2025 mix"),
        ("IDC, Huawei AI chips 2025", "pan2026idc", 2025, mix(L["org-huawei-idc-2025"], 1.0), "all 910C"),
        ("US Commerce, Ascend capacity 2025 (at or below)", "zafar2025kessler", 2025,
         mix(L["org-huawei-commerce-2025"], 1.0), "all 910C"),
        ("Financial Times, Ascend 910B 2024 (910B only)", "blablova2025china", 2024, mix(T("ft-910b-2024"), 0.0),
         "910B rate"),
    ]
    cn_table = []
    for name, src, when, h, reading in cn_obs:
        e = cn_env_cum if when == "cum" else cn_env[when]
        cn_table.append({"observation": name, "source": src, "period": str(when), "reading": reading,
                         "h100e": round(h), "envelope_upper_bound": round(e), "margin": round(e / h, 3),
                         "inside": h <= e, "central_reading_margin": round(cn_central_cum / h, 3)})
    res.detail("china_observations", cn_table)

    # Stacks the observed output needs, at Epoch's unit mix, against stacks available.
    def stacks(units_b, units_c, sb, sc):
        return units_b * sb + units_c * sc
    ub = units_by[(2024, "Ascend 910B")] + units_by[(2025, "Ascend 910B")]
    uc = units_by[(2024, "Ascend 910C")] + units_by[(2025, "Ascend 910C")]
    need_central = stacks(ub, uc, s910b_central, s910c_central)
    need_fewest = stacks(ub, uc, s910b_bound, s910c_generous)
    left_central = stock - need_central
    left_most = stock + 2 * cxmt - need_fewest
    res.detail("china_stacks", {
        "stacks_per_910C_central": s910c_central, "stacks_per_910C_generous": s910c_generous,
        "stacks_per_910C_other_end": s910c_other, "stacks_per_910B_bound": s910b_bound,
        "stacks_per_910B_central": s910b_central, "h100e_per_stack_bound": hps_bound,
        "chip_setting_the_bound": best_chip_cn, "h100e_per_stack_central": hps_central,
        "epoch_units_910B_2024_25": ub, "epoch_units_910C_2024_25": uc,
        "stacks_needed_central": need_central, "stacks_needed_fewest": need_fewest,
        "stacks_left_end_2025_central": left_central, "stacks_left_end_2025_most": left_most,
        "die_bank_dies": L["org-huawei-die-bank"] * 1e6,
        "die_bank_as_910C_h100e": L["org-huawei-die-bank"] * 1e6 / 2 * c910["hi"],
        "note": "logic is not bounded: the die bank alone (two dies per 910C) would make more H100e than the "
                "central HBM reading allows, so HBM binds, as SemiAnalysis judges",
    })

    cn_swings = {}
    base = dict(stock=stock, cx=2 * cxmt, sc=s910c_generous, sb=s910b_bound, hc=c910["hi"], hb=b910["hi"])

    def cn_cum(**kw):
        p = {**base, **kw}
        return (p["stock"] + p["cx"]) * max(p["hc"] / p["sc"], p["hb"] / p["sb"])
    cn_swings["upper bound"] = cn_cum()
    cn_swings["stockpile: Samsung's 11.4M stacks only"] = cn_cum(stock=T("semi-samsung-stacks") * 1e6)
    cn_swings["no CXMT HBM in 2024-25"] = cn_cum(cx=0.0)
    cn_swings["stacks per 910C: 8 (2M for 250,000)"] = cn_cum(sc=s910c_other)
    cn_swings["stacks per 910C: 8.125 (13M for 1.6M)"] = cn_cum(sc=s910c_central)
    cn_prop = cn_cum(sb=s910c_generous * b910["hi"] / c910["hi"])
    cn_swings["910B memory in proportion to compute, not Epoch's 32 GB"] = cn_prop
    cn_swings["H100e per unit: Epoch's spec table"] = cn_cum(hc=c910["spec"], hb=b910["spec"])
    cn_swings["all central"] = cn_central_cum
    res.detail("china_swings_cumulative", {k: round(v) for k, v in cn_swings.items()})

    # ---------------------------------------------------------------- party 3: denied, no stockpile
    nostock_bound = cxmt * hps_bound
    nostock_central = cxmt * hps_central
    res.detail("nostock", {"per_year_upper_bound": round(nostock_bound), "per_year_central": round(nostock_central),
                           "semianalysis_910C_for_2M_stacks_h100e": [round(T("semi-cxmt-910c-low") * c910["implied"]),
                                                                    round(T("semi-cxmt-910c-high") * c910["implied"])],
                           "tested": False, "why": "no 2024-25 observation of a denied party without a stockpile"})

    # ---------------------------------------------------------------- the test
    member_table = []
    for y in YEARS:
        for reading, h in (("median", obs[(y, "allied", "median")]), ("sum of row 95th percentiles", obs[(y, "allied", "row95")])):
            member_table.append({"observation": f"Epoch, Nvidia, Google, AMD and Amazon {y}", "period": str(y),
                                 "reading": reading, "h100e": round(h), "envelope_upper_bound": round(env[y]),
                                 "margin": round(env[y] / h, 3), "inside": h <= env[y],
                                 "central_reading_margin": round(central[y] / h, 3)})
    res.detail("member_observations", member_table)
    everything = member_table + cn_table
    n_inside = sum(o["inside"] for o in everything)
    worst = min(everything, key=lambda o: o["margin"])

    # ---------------------------------------------------------------- C7: budgets and phi
    def years_to(budget, held, flow):
        """Least t with r * year_s * (held * t + flow * t^2 / 2) >= budget: holdings start at `held`
        and grow by at most `flow` a year, every chip at its 8-bit peak and full utilisation."""
        a, b = r_fp8 * year_s * flow / 2, r_fp8 * year_s * held
        if a == 0:
            return budget / b
        return (-b + math.sqrt(b * b + 4 * a * budget)) / (2 * a)

    budgets = {"hardwired-pause breakout budget": L["def-hwp-breakout-budget"],
               "its frozen frontier": L["claim-hwp-frozen-frontier"], "1e26 FLOP": L["phys-rahman-1e26-local"]}
    china_held = L["org-china-implied-stock"] * 1e6 + left_most * hps_bound  # chips held plus stacks not yet used
    c7 = {}
    for label, b in budgets.items():
        c7[label] = {
            "member_from_zero_at_2025_envelope_years": years_to(b, 0.0, env[2025]),
            "china_from_end_2025_years": years_to(b, china_held, nostock_bound),
            "nostock_from_zero_years": years_to(b, 0.0, nostock_bound),
        }
    fleet_end_2025 = sum(obs[(y, "all", "median")] for y in (2022, 2023, 2024, 2025))
    fleet_end_q3 = fleet_end_2025 - sum(num(r["Compute estimate in H100e (median)"]) for r in sales
                                        if qkey(r["Start date"]) == (2025, 4) and r["Compute estimate in H100e (median)"])
    q4 = next(q for q in env_q if q["quarter"] == "2025Q4")
    phi_member_year = 1 + env[2025] / fleet_end_2025
    phi_member_quarter = 1 + q4[f"{q4['binding']}_bound_h100e"] / fleet_end_q3
    phi_china_year = 1 + (left_most * hps_bound + nostock_bound) / (L["org-china-implied-stock"] * 1e6)
    res.detail("c7", {"budgets_flop": budgets, "years_to_budget": c7, "fleet_end_2025_h100e": round(fleet_end_2025),
                      "fleet_end_q3_2025_h100e": round(fleet_end_q3), "china_holdings_plus_unused_stacks_h100e": round(china_held),
                      "phi_member_year": phi_member_year, "phi_member_quarter": phi_member_quarter,
                      "phi_china_year_domestic_only": phi_china_year})

    # ---------------------------------------------------------------- C8: the pool and the slack
    cn_obs_cum = obs[(2024, "huawei", "median")] + obs[(2025, "huawei", "median")]
    slack_cn = cn_env_cum - cn_obs_cum
    slack_cn_central = cn_central_cum - cn_obs_cum
    slack_member = sum(env[y] - obs[(y, "allied", "median")] for y in YEARS)
    allied_cum = sum(obs[(y, "allied", "median")] for y in YEARS)
    units_cum = sum(units_by[(y, "all")] for y in (2022, 2023, 2024, 2025))
    res.detail("c8", {"china_slack_upper_h100e": round(slack_cn), "china_slack_central_h100e": round(slack_cn_central),
                      "member_slack_upper_h100e": round(slack_member), "floor_h100e": floor,
                      "smuggled_high_over_allied_sales_2024_25": L["org-smuggled-cum-high"] / allied_cum,
                      "untraced_chips_over_units_sold_2022_25": L["org-chips-unaccounted"] * 1e6 / units_cum,
                      "units_sold_2022_25": round(units_cum)})

    # ---------------------------------------------------------------- inputs and their kind
    res.detail("inputs", {
        "CoWoS capacity": "analyst benchmarks (SemiWiki, TrendForce, DigiTimes) interpolated by Epoch; Sevilla et al. and TrendForce in the ledger for the paths",
        "TSMC CoWoS growth of more than 80% a year": "vendor claim (TSMC), used only in a sensitivity path",
        "HBM supply in US dollars": "vendor claim (Micron's market sizes for 2024 and 2025, corroborated by Goldman Sachs) split by quarter by Epoch",
        "logic supply": "vendor disclosure (TSMC's per-node wafer revenue) divided by analysts' wafer prices",
        "peak 8-bit rates, so H100e per unit": "vendor claims (spec sheets), via Epoch's chip table; Huawei's are vendor claims too",
        "packages per CoWoS wafer, dies per wafer, yields, HBM cost per chip": "Epoch's bill-of-materials model",
        "HBM stockpile, die bank, CXMT projection, stacks per 910C": "analyst estimates (SemiAnalysis)",
        "Huawei output": "Epoch (modelled), SemiAnalysis (analyst), IDC (market tracker), US Commerce (government statement), FT (press)",
    })

    # ---------------------------------------------------------------- numbers for the ledger
    M = 1e6
    for y in YEARS:
        res.number(f"e22-member-env-{y}", env[y] / M, unit="million H100e", fmt=",.1f",
                   label=f"upper bound on H100e the allied chain (TSMC CoWoS, logic and allied HBM) could make in {y}: "
                         "each quarter's smallest stage at 95th-percentile capacity, yields of one and the best chip")
        res.number(f"e22-member-obs-{y}", obs[(y, "allied", "median")] / M, unit="million H100e", fmt=",.1f",
                   label=f"H100e Nvidia, Google, AMD and Amazon sold in {y}, sum of Epoch's per-quarter medians")
        res.number(f"e22-member-margin-{y}", env[y] / obs[(y, "allied", "median")], fmt=".1f",
                   label=f"the allied chain's {y} upper bound over its observed sales (above 1: inside)")
        res.number(f"e22-member-env-central-{y}", central[y] / M, unit="million H100e", fmt=",.1f",
                   label=f"the allied chain's {y} envelope at central inputs (median capacity and yields, best chip), an estimate, not a bound")
        res.number(f"e22-cowos-use-{y}", use[y]["share_of_p50"], fmt="%",
                   label=f"CoWoS wafers the observed {y} sales need at each chip's own packages per wafer and median yield, "
                         "as a share of median capacity (no manufacturing lag)",
                   note="does not reproduce Epoch's own share: Epoch adds chips made but not sold (inventory, "
                        "export-control write-downs, stranded H200s) and shifts consumption back by the manufacturing lag; "
                        "this counts sold units only")
        res.number(f"e22-cowos-use-epoch-{y}", use[y]["epoch_share_of_p50"], fmt="%",
                   label=f"the same share in {y} from Epoch's own lagged consumption of the four designers")
    res.number("e22-member-env-2025-p5cap", swings["2025"]["CoWoS capacity: p5"] / M, unit="million H100e", fmt=",.1f",
               label="the allied chain's 2025 upper bound with CoWoS capacity at its 5th percentile instead")
    res.number("e22-member-env-2025-hopper", swings["2025"]["Hopper only (H100/H200), no newer chip"] / M,
               unit="million H100e", fmt=",.1f",
               label="the allied chain's 2025 upper bound if only Hopper chips could be made (no Blackwell or TPU v7)")

    res.number("e22-china-env-cum", cn_env_cum / M, unit="million H100e", fmt=",.2f",
               label="upper bound on H100e China's domestic chain could make in 2024 and 2025 together: "
                     "the HBM stockpile plus CXMT at its 2026 rate each year, at the most H100e per stack of any Ascend",
               note=f"set by the 910B at Epoch's listed 32 GB; with its HBM in proportion to its compute the bound is "
                    f"{cn_prop / M:.2f} million H100e")
    res.number("e22-china-env-central-cum", cn_central_cum / M, unit="million H100e", fmt=",.2f",
               label="the same at central inputs (13M stacks, no CXMT HBM, 8.1 stacks per 910C), an estimate, not a bound")
    res.number("e22-china-obs-cum", cn_obs_cum / M, unit="million H100e", fmt=",.2f",
               label="Huawei's 2024 and 2025 output in H100e, Epoch's medians")
    res.number("e22-china-margin-cum", cn_env_cum / cn_obs_cum, fmt=".1f",
               label="China's domestic upper bound over Huawei's observed 2024-25 output (above 1: inside)")
    res.number("e22-china-margin-central-upper", cn_central_cum / (T("epoch-huawei-2024-high") + T("epoch-huawei-2025-high")),
               fmt=".2f", label="the central reading over the sum of Epoch's 95th percentiles for Huawei: inside even then if above 1")
    res.number("e22-china-stacks-share", need_central / stock, fmt="%",
               label="share of China's 13M-stack HBM stockpile that Huawei's 2024-25 output needs at Epoch's unit mix (central stacks per chip)")
    res.number("e22-china-stacks-left", left_central / M, unit="million HBM stacks", fmt=",.1f",
               label="stockpiled HBM stacks left at end 2025 at that mix, before any CXMT output (central)")
    res.number("e22-nostock-env-year", nostock_bound / M, unit="million H100e", fmt=",.2f",
               label="upper bound on H100e a year a denied party without a stockpile could make from CXMT's HBM at its 2026 rate (not tested)")

    res.number("e22-observations", len(everything), unit="observations", fmt=",.0f",
               label="observations tested against the envelopes (two readings of each where the source gives a range)")
    res.number("e22-inside", n_inside, unit="observations", fmt=",.0f",
               label="observations inside their envelope (the test passes if this equals the count)")
    res.number("e22-min-margin", worst["margin"], fmt=".2f",
               label=f"smallest margin of any observation over its upper bound ({worst['observation']}, {worst['reading']})")

    hp = budgets["hardwired-pause breakout budget"]
    res.number("e22-member-budget-year", env[2025] * r_fp8 * year_s, unit="FLOP", fmt="sig2",
               label="upper bound on compute one year of the allied chain's 2025 output delivers in a year at the 8-bit peak and full utilisation")
    res.number("e22-member-years-to-hwp", c7["hardwired-pause breakout budget"]["member_from_zero_at_2025_envelope_years"],
               unit="years", fmt=".2f",
               label=f"least time from no chips to the hardwired-pause budget ({hp:.0e} FLOP) on new allied supply at the 2025 envelope, a lower bound")
    res.number("e22-china-years-to-hwp", c7["hardwired-pause breakout budget"]["china_from_end_2025_years"], unit="years", fmt=".1f",
               label="least time for China from end 2025 (its implied stock plus every unused stacked HBM made into Ascends, plus CXMT) "
                     "to the hardwired-pause budget on domestic supply alone, a lower bound")
    res.number("e22-nostock-years-to-hwp", c7["hardwired-pause breakout budget"]["nostock_from_zero_years"], unit="years", fmt=".1f",
               label="least time from no chips to the hardwired-pause budget for a denied party without a stockpile (CXMT's HBM only), a lower bound")
    res.number("e22-nostock-years-to-frozen", c7["its frozen frontier"]["nostock_from_zero_years"], unit="years", fmt=".2f",
               label="the same to the hardwired-pause paper's frozen frontier (2e+27 FLOP), a lower bound")
    res.number("e22-china-budget-year", china_held * r_fp8 * year_s, unit="FLOP", fmt="sig2",
               label="upper bound on compute a year from China's end-2025 holdings plus every unused stacked HBM made into Ascends, "
                     "at the 8-bit peak and full utilisation")
    res.number("e22-nostock-budget-year", nostock_bound * r_fp8 * year_s, unit="FLOP", fmt="sig2",
               label="upper bound on compute one year of a denied party's CXMT-limited output delivers in a year, no stockpile")
    res.number("e22-phi-member-year", phi_member_year, fmt=".1f",
               label="upper bound on phi for a year between declarations: the fleet Epoch counts at end 2025 plus the 2025 envelope, over that fleet")
    res.number("e22-phi-member-quarter", phi_member_quarter, fmt=".2f",
               label="the same for a quarter: Q4 2025's envelope over the fleet at end Q3 2025")
    res.number("e22-phi-china-year", phi_china_year, fmt=".1f",
               label="upper bound on phi for China over 2026 on domestic supply only (imports and smuggling add to it)")

    res.number("e22-china-slack", slack_cn / M, unit="million H100e", fmt=",.2f",
               label="room the upper bound leaves for undeclared Chinese domestic output in 2024-25 (bound less Epoch's medians)")
    res.number("e22-china-slack-over-floor", slack_cn / floor, fmt=",.0f",
               label="that room over C8's floor for a 1e26 FLOP run under a pause (800 H100e)")
    res.number("e22-china-slack-central-over-floor", slack_cn_central / floor, fmt=",.0f",
               label="the room at the central reading over the same floor")
    res.number("e22-member-slack", slack_member / M, unit="million H100e", fmt=",.1f",
               label="room the allied upper bound leaves above observed 2024-25 sales")
    res.number("e22-smuggled-share-of-allied", L["org-smuggled-cum-high"] / allied_cum, fmt=".1%",
               label="the 95th percentile of compute smuggled into China through 2025 as a share of allied 2024-25 sales: the pool fits if below 1")

    res.detail("verdict", {
        "test": "passes" if n_inside == len(everything) else "fails",
        "member_binding_stage": binding,
        "worst_observation": worst,
        "end_2024_cowos_paths_wpm": {k: round(v) for k, v in end2024.items()},
        "sevilla_end_2024_wpm": [T("sevilla-cowos-end2024-low"), T("sevilla-cowos-end2024-high")],
    })
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
