#!/usr/bin/env python3
"""E23: the durability backtest. Would a ranking of the AI supply chain's chokepoints, made only from
data public at the end of 2022, have ordered the erosion seen from 2023 to November 2026?

It serves an open question in O3 (research/015-organisational.md), not a claim: O3 ranks stages by
durability from 2026 evidence and says a ranking that fails to order the observed erosion is cut.

The stages are the ones O3 names: EUV lithography, DUV immersion lithography, front-end deposition
and etch tools, leading-edge logic, HBM, packaging, EDA, design IP, AI accelerator design, and power.

The 2022 data. Seven stages come from the ETO Chip Explorer dataset as its repository stood on
19 December 2022 (commit pinned below, so nothing later can leak in): for each stage, the firms
the data list as supplying it, which of them are not negligible, and each firm's country.
Leading-edge logic takes its firms from the same release's fabrication text. HBM takes its makers from
TrendForce's report of the 2022 market (published 18 April 2023, 108 days after the cutoff, the only
deviation from the rule; it names the makers a 2022 reader could already see). Power takes China's
share of world electricity generation in 2021 from Our World in Data's release of 30 December 2022.

THE RULE, fixed before the erosion table was compiled, and a function of those data only:
  1. Entry. A stage is a chokepoint against the denied party (China) in 2022 only if China is not
     its largest supplier: by country market share where the data give one, else by the count of
     non-negligible firms. Power fails it (China was the largest generator in 2021) and is ranked
     last in the full set but left out of the main test, since erosion of a stage never held is not
     defined.
  2. Order. Among the stages that enter, the predicted erosion rises with n_c, the number of
     non-negligible Chinese suppliers in 2022 (the denied party's base), and ties are broken by
     n_w, the number of non-negligible suppliers worldwide (O3's condition of few suppliers). Ties
     left share the average rank.
O3 asked for supplier count, capacity growth and technical complexity. No 2022 source gives
capacity growth for every stage, so it is left out. The base n_c stands for technical complexity,
following Allen citing Bernstein that self-sufficiency is "best predicted by the market and
technological complexities of each semiconductor market segment" (allen2025senate, p. 4). The
builder knew the broad history of 2022 to 2026, so the rule's independence from it cannot be proved;
every alternative rule and scoring is therefore reported next to the main one.

The erosion. Every event from 2023 to November 2026 is a row of tools/exp/data/e23_durability.csv
with its source and where, in four classes: entrant (the denied party's own output of the stage),
leak (smuggling, diversion, die banks, stockpiles bought before a rule), substitute (another route
to the same function), and holder (the holding state relaxes or rescinds its own control, or its
firms keep selling the stage's output to the denied party at scale, as Part I records). Each row
carries the status its source states, which the script maps to a level (LEVEL below). A stage's
erosion score is the sum over classes of the highest level in each (0 to 8).

The test. Spearman's rank correlation between the predicted and the observed erosion, positive if
the rule ordered it; an exact one-sided permutation p value over every ordering; two intervals (a
stage bootstrap and Fisher's z with the Bonett and Wright variance); the smallest correlation the
exact test could call significant with this many stages; the test's power at the observed effect;
and the number of stages a rank test would need to tell the 2022 ranking from a random one at that
effect, with 80% power at one-sided 5%, by simulation (with and without the observed ties) and by
formula. Then each stage left out, each alternative rule and scoring, power put back in, and a check
of the event score against measured share changes for the four stages that have them (the ETO
release of August 2026 gives 2025 shares for the tool stages; Counterpoint gives HBM's).

  .venv/bin/python tools/exp/e23_durability.py      (CPU, under a minute; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import io
import itertools
import math
import sys
import tomllib
from datetime import date
from pathlib import Path

import numpy as np
from scipy.stats import norm, rankdata

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127
TABLE = Path(__file__).resolve().parent / "data" / "e23_durability.csv"
NEW_SOURCES = Path(__file__).resolve().parent / "data" / "e23_durability.sources.toml"
CUTOFF = date(2022, 12, 31)
WINDOW_END = date(2026, 11, 27)

ETO22 = "https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/3f0b236c2368e80d078edc2eae8570738df32974/data/"
ETO22_SHA = {
    "provision.csv": "4aa386a4f608492a30ed67638e0cf357f5ea7bd79d324789815813906d2647ad",
    "providers.csv": "4a82079dcb7e5adf5a80cdb9208f9ed5ffb2282c38ccf2dd2eea23b43634d191",
    "stages.csv": "a45db2ca046228b66a19c1a457bea274b1988dd934251195f9d90d2df27f5904",
    "inputs.csv": "75f89526fcfdeb69c948b1efd2551b4c88ef24bce60bb6a3ce0c340853c6beed",
}
ETO26 = "https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/9a4e1b128c836cb3bdf065a06a3fc03397e00ff0/data/"
ETO26_SHA = {
    "provision.csv": "d94267801a73745e40bfaee8a30341adb37a168a8a0f28bf5d03f78e05f6c16f",
    "providers.csv": "c529479afe7d35afa750729bf6dd45227a375568c02b8cf401aad239360a13e4",
}
OWID22 = "https://raw.githubusercontent.com/owid/energy-data/555c997c491d31ef98e2fb4a47684a700af268ea/owid-energy-data.csv"
OWID22_SHA = "110412d2892daca5ac0a17cc9a2a67bab30d4d5b3f0f7edde3d8d0956118f636"

STAGES = ["euv", "duv-immersion", "dep-etch", "leading-logic", "hbm", "packaging", "eda", "core-ip",
          "ai-chips", "power"]
CLASSES = ("entrant", "leak", "substitute", "holder")
LEVEL = {
    "entrant": {"prototype": 1, "announced": 1, "shipping": 1, "counted": 2},
    "leak": {"alleged": 1, "quantified": 2},
    "substitute": {"announced": 1, "demonstrated": 1, "shipping": 1, "counted": 2},
    "holder": {"sales": 1, "relaxed": 2},
}
# Part I's own ranking (O3, "The evidence: a narrow core"), made in 2026 with the erosion in view:
# a contaminated reference, not a test. Finished chips map to AI accelerator design.
PART1_ORDER = {"euv": 1, "leading-logic": 2, "hbm": 3, "packaging": 4, "ai-chips": 5}
BOOT = 10_000
SIMS = 4_000
NULL_SIMS = 20_000
POWER_TARGET = 0.8
ALPHA = 0.05
N_GRID = list(range(5, 21)) + list(range(25, 101, 5)) + list(range(120, 401, 20))

# What was searched for events beyond the survey notes, so "none found" reads as a claim about our
# search. EUV, leading-edge logic, HBM and AI chips draw on the sources the notes and O3 had opened.
SEARCHES = {
    "duv-immersion": ["China MIIT catalogue domestic ArF immersion lithography 2024"],
    "dep-etch": ["China domestic semiconductor equipment self-sufficiency NAURA AMEC 2024",
                 "SEMI 2024 equipment billings China"],
    "packaging": ["China advanced packaging CoWoS-like capacity Huawei Ascend 910C JCET Tongfu"],
    "eda": ["US lifts EDA export restrictions China July 2025",
            "Chinese EDA vendors Empyrean market share China 2024"],
    "core-ip": ["China RISC-V policy guidance 2025 replace Arm"],
    "hbm": ["TrendForce 2022 HBM market share SK hynix Samsung Micron"],
}


def read_csv(path: Path) -> list[dict]:
    return list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig"))))


def source_keys() -> tuple[set, set]:
    keys, aliases = set(), set()
    for path in (ROOT / "research" / "sources.toml", NEW_SOURCES):
        for key, spec in tomllib.loads(path.read_text()).get("source", {}).items():
            keys.add(key)
            aliases.update(spec.get("aliases", []))
    return keys, aliases


def spearman(x, y) -> float:
    rx, ry = rankdata(x), rankdata(y)
    rx, ry = rx - rx.mean(), ry - ry.mean()
    den = math.sqrt((rx * rx).sum() * (ry * ry).sum())
    if den == 0:
        raise ValueError("a rank vector is constant")
    return float((rx * ry).sum() / den)


_PERMS: dict[int, np.ndarray] = {}


def perms(n: int) -> np.ndarray:
    if n not in _PERMS:
        _PERMS[n] = np.array(list(itertools.permutations(range(n))), dtype=np.int8)
    return _PERMS[n]


def perm_null(x, y) -> np.ndarray:
    """Spearman's r_s for every ordering of y against x (exact; n up to 10)."""
    rx, ry = rankdata(x), rankdata(y)
    rx, ry = rx - rx.mean(), ry - ry.mean()
    den = math.sqrt((rx * rx).sum() * (ry * ry).sum())
    n = len(x)
    if n <= 9:
        return ry[perms(n)] @ rx / den
    out = []
    it = itertools.permutations(range(n))
    while True:
        block = np.array(list(itertools.islice(it, 400_000)), dtype=np.int8)
        if block.size == 0:
            break
        out.append(ry[block] @ rx / den)
    return np.concatenate(out)


def exact_test(x, y) -> dict:
    rho = spearman(x, y)
    null = perm_null(x, y)
    p = float((null >= rho - 1e-12).mean())
    vals = np.unique(np.round(null, 12))
    crit = next((float(v) for v in vals if (null >= v - 1e-12).mean() <= ALPHA), float("nan"))
    return {"rho": rho, "p_one_sided": p, "rho_critical": crit, "n": len(x)}


def fisher_ci(rho: float, n: int) -> tuple[float, float]:
    """95% interval by Fisher's z with the Bonett and Wright variance for Spearman's r_s."""
    z, se = math.atanh(rho), math.sqrt((1 + rho * rho / 2) / (n - 3))
    return math.tanh(z - 1.959963984540054 * se), math.tanh(z + 1.959963984540054 * se)


def copula(gen, rho_s: float, n: int, m: int) -> tuple[np.ndarray, np.ndarray]:
    """m samples of n pairs from a normal copula with Spearman's r_s = rho_s."""
    r = 2 * math.sin(math.pi * rho_s / 6)
    x = gen.standard_normal((m, n))
    y = r * x + math.sqrt(max(0.0, 1 - r * r)) * gen.standard_normal((m, n))
    return x, y


def rows_spearman(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    rx, ry = rankdata(x, axis=1), rankdata(y, axis=1)
    rx -= rx.mean(axis=1, keepdims=True)
    ry -= ry.mean(axis=1, keepdims=True)
    den = np.sqrt((rx * rx).sum(axis=1) * (ry * ry).sum(axis=1))
    return (rx * ry).sum(axis=1) / den


def impose(z: np.ndarray, levels: np.ndarray) -> np.ndarray:
    """Replace each row's values by the given sorted levels in the row's own rank order, so a
    simulated sample keeps the observed ties. levels has the row length."""
    order = np.argsort(z, axis=1, kind="stable")
    out = np.empty_like(z)
    np.put_along_axis(out, order, np.broadcast_to(levels, z.shape), axis=1)
    return out


def scaled_levels(observed: np.ndarray, n: int) -> np.ndarray:
    """The observed score's distinct levels in their observed proportions, at size n."""
    s = np.sort(observed)
    return s[np.floor(np.arange(n) * len(s) / n).astype(int)]


def power_curve(gen, rho_s: float, y_obs: np.ndarray) -> dict:
    """Power of the one-sided 5% rank test against n, with continuous scores (no ties, the
    optimistic case) and with the erosion score's observed ties kept."""
    table = {}
    for n in N_GRID:
        x, y = copula(gen, rho_s, n, SIMS)
        lev = scaled_levels(y_obs, n)
        yt = impose(y, lev)
        # Null: an ordering unrelated to the predictor, same tie pattern.
        x0 = gen.standard_normal((NULL_SIMS, n))
        y0 = np.broadcast_to(lev, (NULL_SIMS, n)).copy()
        y0c = gen.standard_normal((NULL_SIMS, n))
        c_tied = float(np.quantile(rows_spearman(x0, y0), 1 - ALPHA))
        c_free = float(np.quantile(rows_spearman(x0, y0c), 1 - ALPHA))
        table[str(n)] = {
            "power_untied": float((rows_spearman(x, y) >= c_free).mean()),
            "power_tied": float((rows_spearman(x, yt) >= c_tied).mean()),
            "critical_untied": c_free,
            "critical_tied": c_tied,
        }
        if table[str(n)]["power_untied"] >= POWER_TARGET and table[str(n)]["power_tied"] >= POWER_TARGET:
            break  # both found; larger n only adds run time
    first = lambda key: next((int(n) for n, v in table.items() if v[key] >= POWER_TARGET), None)  # noqa: E731
    return {"table": table, "n_untied": first("power_untied"), "n_tied": first("power_tied")}


def analytic_n(rho_s: float) -> float:
    """Stages for 80% power at one-sided 5%, by Fisher's z with the Bonett and Wright variance."""
    za, zb = norm.ppf(1 - ALPHA), norm.ppf(POWER_TARGET)
    return 3 + (1 + rho_s * rho_s / 2) * ((za + zb) / math.atanh(rho_s)) ** 2


def avg_rank(keys: dict) -> dict:
    """Average ranks (1 lowest) of tuple or number keys."""
    names = sorted(keys)
    order = sorted(names, key=lambda s: (keys[s], s))
    out, i = {}, 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and keys[order[j + 1]] == keys[order[i]]:
            j += 1
        for k in range(i, j + 1):
            out[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return out


def parse_size(text: str) -> float | None:
    """'$3.5 billion (2019)' or '$780 million (2019)' in billions of dollars."""
    t = text.replace(",", "").split()
    if len(t) < 2 or not t[0].startswith("$"):
        return None
    try:
        v = float(t[0][1:])
    except ValueError:
        return None
    return v if t[1] == "billion" else v / 1000 if t[1] == "million" else None


def main() -> int:
    res = Results("E23", "e23_durability", seed=SEED)
    res.detail("ledger_inputs", {})  # E23 reads no ledger number: every input is in its table or fetched.

    # The sources and the hand table.
    keys, aliases = source_keys()
    table = read_csv(TABLE)
    for i, r in enumerate(table, 2):
        if r["source"] not in keys or r["source"] in aliases:
            raise SystemExit(f"row {i}: source {r['source']!r} is not an entry of research/sources.toml or {NEW_SOURCES.name}")
        if not r["where"]:
            raise SystemExit(f"row {i}: no 'where'")
        if r["stage"] not in STAGES:
            raise SystemExit(f"row {i}: unknown stage {r['stage']!r}")
        if r["kind"] == "event":
            if r["cls"] not in LEVEL or r["status"] not in LEVEL[r["cls"]]:
                raise SystemExit(f"row {i}: class {r['cls']!r} with status {r['status']!r} has no level")
            when = date.fromisoformat(r["date"])
            if not CUTOFF < when <= WINDOW_END:
                raise SystemExit(f"row {i}: event dated {when}, outside 2023 to {WINDOW_END}")
    stage_rows = {r["stage"]: r for r in table if r["kind"] == "stage"}
    if sorted(stage_rows) != sorted(STAGES):
        raise SystemExit("the table must define each stage once")

    # The 2022 data.
    eto = {f: fetch(ETO22 + f, f"eto-2022/{f}", res, what=f"ETO Chip Explorer, release of 2022-12-19: {f}", sha=s)
           for f, s in ETO22_SHA.items()}
    prov22 = read_csv(eto["provision.csv"])
    who22 = {r["provider_id"]: r for r in read_csv(eto["providers.csv"])}
    s2_text = next(r["description"] for r in read_csv(eto["stages.csv"]) if r["stage_id"] == "S2")
    inputs22 = read_csv(eto["inputs.csv"])
    size22 = {r["input_id"]: parse_size(r["market_share_chart_global_market_size_info"]) for r in inputs22}
    owid = fetch(OWID22, "owid-2022/owid-energy-data.csv", res, what="Our World in Data energy data, release of 2022-12-30", sha=OWID22_SHA)

    data22 = {}
    for stage in STAGES:
        spec = stage_rows[stage]["item"]
        d = {"definition": stage_rows[stage]["note"], "mapping": spec}
        if spec.startswith("eto:"):
            ids = spec[4:].split()
            firms, countries = {}, {}
            for r in prov22:
                if r["provided_id"] not in ids:
                    continue
                p = who22[r["provider_id"]]
                if p["provider_type"] == "country":
                    share = r["share_provided"].rstrip("%")
                    countries.setdefault(r["provider_name"], {})[r["provided_id"]] = float(share) if share else None
                elif not r["negligible_market_share"]:
                    firms[r["provider_name"]] = p["country"]
            if not firms:
                raise SystemExit(f"{stage}: no firms found for {ids}; the release changed shape")
            # China's share: weighted by each input's 2019 market size when every share is given.
            weights = {i: size22.get(i) for i in ids}
            shares = {c: [v.get(i, 0.0) for i in ids] for c, v in countries.items()}
            known = all(s is not None for v in shares.values() for s in v) and shares
            if known and len(ids) > 1 and all(weights[i] for i in ids):
                w = np.array([weights[i] for i in ids])
                by_country = {c: float(np.dot(v, w) / w.sum()) for c, v in shares.items()}
            elif known:
                by_country = {c: v[0] for c, v in shares.items()}
            else:
                by_country = None
            d.update({"firms": dict(sorted(firms.items())),
                      "n_w": len(firms), "n_c": sum(1 for c in firms.values() if c == "CHN"),
                      "country_share": by_country,
                      "china_share": None if by_country is None else by_country.get("CHN", 0.0)})
        elif spec == "rows":
            sup = [r for r in table if r["kind"] == "supplier2022" and r["stage"] == stage]
            if stage == "leading-logic":
                for r in sup:
                    if f"({r['item']})" not in s2_text:
                        raise SystemExit(f"{r['item']} is not in the 2022 release's fabrication text")
            vals = [float(r["value"]) for r in sup if r["value"]]
            d.update({"firms": {r["item"]: r["country"] for r in sorted(sup, key=lambda r: r["item"])},
                      "n_w": len(sup), "n_c": sum(1 for r in sup if r["country"] == "CHN"),
                      "country_share": None,
                      # China's share only where the rows give every maker's share: the rest of 100.
                      "china_share": max(0.0, 100 - sum(vals)) if len(vals) == len(sup) else None})
        else:
            rows21 = [r for r in read_csv(owid) if r["year"] == "2021" and r["electricity_generation"]]
            gen22 = {r["country"]: float(r["electricity_generation"]) for r in rows21
                     if r["iso_code"] and not r["iso_code"].startswith("OWID")}
            world = next(float(r["electricity_generation"]) for r in rows21 if r["country"] == "World")
            top = max(gen22, key=gen22.get)
            d.update({"firms": None, "n_w": None, "n_c": None,
                      "china_share": 100 * gen22["China"] / world, "largest_country": top,
                      "world_twh_2021": world, "china_twh_2021": gen22["China"]})
        # Entry: China is not the stage's largest supplier.
        if d["n_w"] is None:
            d["enters"] = d["largest_country"] != "China"
        elif d["country_share"]:
            d["enters"] = max(d["country_share"], key=d["country_share"].get) != "CHN"
        else:
            by = {}
            for c in d["firms"].values():
                by[c] = by.get(c, 0) + 1
            d["enters"] = max(by, key=lambda c: (by[c], c != "CHN")) != "CHN"
        data22[stage] = d
    if data22["power"]["enters"]:
        raise SystemExit("power entered: the 2022 data no longer show China as the largest generator")
    main_stages = [s for s in STAGES if data22[s]["enters"]]
    if main_stages != [s for s in STAGES if s != "power"]:
        raise SystemExit(f"stages entering changed: {main_stages}; the full-set ranking assumes only power is out")

    # The rules. Each maps stage to predicted erosion order (higher means more erosion predicted).
    nc = {s: data22[s]["n_c"] for s in main_stages}
    nw = {s: data22[s]["n_w"] for s in main_stages}
    rules = {
        "R1 base then suppliers (the rule)": avg_rank({s: (nc[s], nw[s]) for s in main_stages}),
        "R2 suppliers then base": avg_rank({s: (nw[s], nc[s]) for s in main_stages}),
        "R3 rank sum of base and suppliers": avg_rank({s: avg_rank(nc)[s] + avg_rank(nw)[s] for s in main_stages}),
        "R4 base only": avg_rank(nc),
        "R5 suppliers only": avg_rank(nw),
        "R6 China's 2022 market share": avg_rank({s: data22[s]["china_share"] for s in main_stages
                                                   if data22[s]["china_share"] is not None}),
    }
    primary_rule = "R1 base then suppliers (the rule)"

    # The erosion scores.
    events = [r for r in table if r["kind"] == "event"]
    def score(stage: str, keep=lambda r: True, classes=CLASSES, count=False) -> float:
        total = 0
        for c in classes:
            lv = [LEVEL[c][r["status"]] for r in events if r["stage"] == stage and r["cls"] == c and keep(r)]
            if lv:
                total += 1 if count else max(lv)
        return float(total)
    scorings = {
        "S1 sum of class maxima (the score)": lambda s: score(s),
        "S2 classes with any event": lambda s: score(s, count=True),
        "S3 technical only (entrant, substitute)": lambda s: score(s, classes=("entrant", "substitute")),
        "S4 edges only (leak, holder)": lambda s: score(s, classes=("leak", "holder")),
        "S5 holder counts formal relaxations only": lambda s: score(s, keep=lambda r: r["cls"] != "holder" or r["status"] == "relaxed"),
        "S6 holder counts only what Part I records": lambda s: score(s, keep=lambda r: r["cls"] != "holder" or "Part I records" in r["note"]),
    }
    primary_score = "S1 sum of class maxima (the score)"
    erosion = {s: {name: f(s) for name, f in scorings.items()} for s in STAGES}
    per_class = {s: {c: score(s, classes=(c,)) for c in CLASSES} for s in STAGES}

    # The main test.
    pred = rules[primary_rule]
    x = np.array([pred[s] for s in main_stages])
    y = np.array([erosion[s][primary_score] for s in main_stages])
    main = exact_test(x, y)
    rho, n = main["rho"], main["n"]
    f_lo, f_hi = fisher_ci(rho, n)
    gen = np.random.default_rng(SEED)
    boots = []
    for _ in range(BOOT):
        pick = gen.integers(0, n, n)
        if np.unique(x[pick]).size < 2 or np.unique(y[pick]).size < 2:
            continue
        boots.append(spearman(x[pick], y[pick]))
    boots = np.array(boots)
    b_lo, b_hi = float(np.quantile(boots, 0.025)), float(np.quantile(boots, 0.975))

    # Power at this n with the observed ties, against the exact critical value.
    xs, ys = copula(gen, rho, n, SIMS) if rho > 0 else (None, None)
    if rho > 0:
        sim = rows_spearman(impose(xs, np.sort(x)), impose(ys, np.sort(y)))
        power_here = float((sim >= main["rho_critical"] - 1e-12).mean())
        curve = power_curve(gen, rho, y)
        n_formula = analytic_n(rho)
    else:
        power_here, curve, n_formula = float("nan"), {"table": {}, "n_tied": None, "n_untied": None}, float("nan")

    # Leave one stage out.
    loo = {}
    for i, s in enumerate(main_stages):
        keep = [j for j in range(n) if j != i]
        loo[s] = spearman(x[keep], y[keep])

    # Every rule against every scoring.
    grid = {}
    for rn, rule in rules.items():
        st = [s for s in main_stages if s in rule]
        for sn in scorings:
            xx = np.array([rule[s] for s in st])
            yy = np.array([erosion[s][sn] for s in st])
            if np.unique(yy).size < 2:
                grid[f"{rn} | {sn}"] = {"rho": None, "n": len(st), "why": "the score is the same for every stage"}
                continue
            t = exact_test(xx, yy)
            grid[f"{rn} | {sn}"] = {"rho": t["rho"], "p_one_sided": t["p_one_sided"], "n": t["n"]}
    alt = [v["rho"] for v in grid.values() if v["rho"] is not None]

    # Part I's own ranking: contaminated (made in 2026 with the erosion in view), a reference only.
    p1 = [s for s in main_stages if s in PART1_ORDER]
    part1 = exact_test(np.array([PART1_ORDER[s] for s in p1]), np.array([erosion[s][primary_score] for s in p1]))

    # Selection-free version: every stage O3 names, power ranked last as the rule places it.
    full_pred = dict(pred)
    full_pred["power"] = float(len(STAGES))
    xf = np.array([full_pred[s] for s in STAGES])
    yf = np.array([erosion[s][primary_score] for s in STAGES])
    full = exact_test(xf, yf)

    # The check against measured share changes (China's share of the stage's world market).
    eto26 = {f: fetch(ETO26 + f, f"eto-2026/{f}", res, what=f"ETO Chip Explorer, August 2026 update (2025 shares): {f}", sha=s)
             for f, s in ETO26_SHA.items()}
    prov26 = read_csv(eto26["provision.csv"])
    who26 = {r["provider_id"]: r for r in read_csv(eto26["providers.csv"])}
    shares_check = {}
    for stage in ("euv", "duv-immersion", "dep-etch"):
        ids = stage_rows[stage]["item"][4:].split()
        have25 = {r["provided_id"] for r in prov26 if r["year"] == "2025" and r["provided_id"] in ids}
        used = [i for i in ids if i in have25]
        cn25 = {i: 0.0 for i in used}
        for r in prov26:
            if r["year"] == "2025" and r["provided_id"] in used and who26[r["provider_id"]]["provider_type"] == "country" and r["provider_name"] == "CHN":
                cn25[r["provided_id"]] = float(r["share_provided"])
        cn19 = {i: 0.0 for i in used}
        for r in prov22:
            if r["provided_id"] in used and who22[r["provider_id"]]["provider_type"] == "country" and r["provider_name"] == "CHN":
                cn19[r["provided_id"]] = float(r["share_provided"].rstrip("%") or "nan")
        w = np.array([size22[i] for i in used])
        a = float(np.dot([cn19[i] for i in used], w) / w.sum())
        b = float(np.dot([cn25[i] for i in used], w) / w.sum())
        shares_check[stage] = {"inputs": used, "china_share_2022_release": a, "china_share_2025": b,
                               "change_points": b - a, "weights": "2019 market sizes from the 2022 release"}
    late = [float(r["value"]) for r in table if r["kind"] == "share_latest" and r["stage"] == "hbm"]
    hbm_late = max(0.0, 100 - sum(late))
    shares_check["hbm"] = {"china_share_2022_release": data22["hbm"]["china_share"], "china_share_2025": hbm_late,
                           "change_points": hbm_late - data22["hbm"]["china_share"],
                           "note": "Q2 2026 revenue shares of the three makers sum to at least 100%, so any other maker's share is within rounding of zero"}
    for s, v in shares_check.items():
        v["event_score"] = erosion[s][primary_score]
    sc = sorted(shares_check)
    shares_check["rho_event_score_vs_share_change"] = {
        "stages": sc, "rho": spearman([shares_check[s]["change_points"] for s in sc], [shares_check[s]["event_score"] for s in sc]),
        "note": "four stages, three tied at no change: an illustration of agreement, not a test"}

    # The numbers.
    verdict = ("orders the erosion better than chance at one-sided 5%" if main["p_one_sided"] < ALPHA
               else "does not order the erosion better than chance at one-sided 5%")
    res.number("e23-stages", n, unit="stages", fmt=",.0f",
               label="supply-chain stages in the durability backtest that were chokepoints against China by 2022 data (power left out: China was the largest generator)")
    res.number("e23-events", sum(1 for r in events if r["stage"] in main_stages), unit="events", fmt=",.0f",
               label="sourced erosion events from 2023 to November 2026 at those stages (found by our searches, so a lower bound)")
    res.number("e23-rho", rho, fmt=".2f",
               label=f"Spearman's r_s between the 2022 ranking's predicted erosion and the erosion scored 2023 to 2026 (positive means it ordered it; the rule {verdict})")
    res.number("e23-rho-lo", f_lo, fmt=".2f",
               label="Spearman's r_s, 2.5th percentile by Fisher's z with the Bonett and Wright variance")
    res.number("e23-rho-hi", f_hi, fmt=".2f",
               label="Spearman's r_s, 97.5th percentile by Fisher's z with the Bonett and Wright variance")
    res.number("e23-rho-boot-lo", b_lo, fmt=".2f",
               label="Spearman's r_s, 2.5th percentile of resampling the stages")
    res.number("e23-rho-boot-hi", b_hi, fmt=".2f",
               label="Spearman's r_s, 97.5th percentile of resampling the stages")
    res.number("e23-p", main["p_one_sided"], fmt=".2f",
               label="one-sided p value of the rank test, exact over every ordering of the stages")
    res.number("e23-rho-critical", main["rho_critical"], fmt=".2f",
               label="smallest Spearman's r_s the exact one-sided 5% test could call significant with these stages and ties")
    if rho > 0:
        res.number("e23-power-here", power_here, unit="", fmt=".2f",
                   label="statistical power of the one-sided 5% rank test with this many stages if the observed r_s were the true one (simulated, ties kept)")
        nt = curve["n_tied"] or N_GRID[-1]
        nu = curve["n_untied"] or N_GRID[-1]
        res.number("e23-n-needed", nt, unit="stages", fmt=",.0f",
                   label=("stages a rank test would need to tell the 2022 ranking from a random one at the observed r_s, 80% power at one-sided 5%, simulated with the erosion score's ties, on a grid of 5 stages"
                          + ("" if curve["n_tied"] else f" (more than {N_GRID[-1]}: a lower bound)")))
        res.number("e23-n-needed-untied", nu, unit="stages", fmt=",.0f",
                   label=("the same with untied scores, the optimistic case" + ("" if curve["n_untied"] else f" (more than {N_GRID[-1]})")))
        res.number("e23-n-needed-formula", n_formula, unit="stages", fmt=",.0f",
                   label="the same by Fisher's z with the Bonett and Wright variance (untied)")
    res.number("e23-rho-loo-min", min(loo.values()), fmt=".2f",
               label=f"Spearman's r_s with one stage left out, lowest (without {min(loo, key=loo.get)})")
    res.number("e23-rho-loo-max", max(loo.values()), fmt=".2f",
               label=f"Spearman's r_s with one stage left out, highest (without {max(loo, key=loo.get)})")
    res.number("e23-rho-alt-min", min(alt), fmt=".2f",
               label=f"Spearman's r_s, lowest over the {len(rules)} rules and {len(scorings)} erosion scorings")
    res.number("e23-rho-alt-max", max(alt), fmt=".2f",
               label=f"Spearman's r_s, highest over the {len(rules)} rules and {len(scorings)} erosion scorings")
    res.number("e23-rho-alt-median", float(np.median(alt)), fmt=".2f",
               label=f"Spearman's r_s, median over the {len(rules)} rules and {len(scorings)} erosion scorings (the rule as fixed is near the top)")
    res.number("e23-eto-inputs-2022", len(inputs22), unit="inputs", fmt=",.0f",
               label="tools, materials and design inputs the 2022 supply-chain dataset lists, nested and correlated, so fewer independent stages than this")
    res.number("e23-rho-full", full["rho"], fmt=".2f",
               label="Spearman's r_s with power put back in, ranked last as the rule places it (every stage O3 names)")
    res.number("e23-rho-part1", part1["rho"], fmt=".2f",
               label=f"Spearman's r_s for Part I's own ranking of {part1['n']} stages, made in 2026 with the erosion in view (contaminated, a reference only)")
    res.number("e23-china-power-share-2021", data22["power"]["china_share"], unit="%", fmt=".0f",
               label="China's share of world electricity generation in 2021, from data public at the end of 2022")

    res.detail("rule", {
        "entry": "China is not the stage's largest supplier (country market share where given, else count of non-negligible firms)",
        "order": "predicted erosion rises with n_c (non-negligible Chinese suppliers), ties broken by n_w (non-negligible suppliers worldwide)",
        "fixed": "before the erosion table was compiled; the builder knew the broad 2022 to 2026 history, so this cannot be proved",
        "deviation": "HBM's makers come from a report of the 2022 market published on 2023-04-18",
    })
    res.detail("levels", LEVEL)
    res.detail("stages_2022", data22)
    res.detail("stages", {s: {"enters": data22[s]["enters"], "n_c": data22[s]["n_c"], "n_w": data22[s]["n_w"],
                              "predicted_erosion_rank": full_pred[s], "erosion_score": erosion[s][primary_score],
                              "by_class": per_class[s], "scorings": erosion[s]} for s in STAGES})
    res.detail("events", [{k: r[k] for k in ("stage", "cls", "status", "date", "item", "source", "where")}
                          | {"level": LEVEL[r["cls"]][r["status"]]} for r in events])
    res.detail("test", main | {"fisher_95": [f_lo, f_hi], "bootstrap_95": [b_lo, b_hi],
                               "bootstrap_kept": int(boots.size), "power_here": power_here})
    res.detail("power_curve", curve | {"n_formula": n_formula, "target": POWER_TARGET, "alpha_one_sided": ALPHA,
                                       "sims": SIMS, "null_sims": NULL_SIMS})
    res.detail("leave_one_out", loo)
    res.detail("rules", {k: dict(sorted(v.items())) for k, v in rules.items()})
    res.detail("rules_by_scorings", grid)
    res.detail("part1_reference", part1 | {"order": PART1_ORDER})
    res.detail("with_power", full)
    res.detail("share_change_check", shares_check)
    res.detail("searches", SEARCHES)
    res.detail("no_event_found", {s: [c for c in CLASSES if per_class[s][c] == 0] for s in STAGES})
    res.detail("selection", [
        "Events are those found by the survey and our searches; stages under more scrutiny (AI chips, logic) yield more, which raises their scores whatever their durability.",
        "Statuses are coded from each source's words by one builder who knew the history; the quote is in the table so a reader can recode.",
        "The 2022 supplier counts come from a 2021 report restructured in 2022 (data mostly for 2019 and 2020); memory is outside it, so HBM uses a report published in April 2023.",
        "The window is under four years; slow erosion (EUV) may simply not have shown yet.",
        "Power is left out of the main test because China held it in 2022; putting it back is reported.",
    ])
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
