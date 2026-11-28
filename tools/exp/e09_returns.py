#!/usr/bin/env python3
"""E9: returns to research, r, refitted across domains with compute's share of research input free.

What it measures. In the semi-endogenous law (1/A) dA/dt = theta A^(-beta) E^lambda the return to
research is r = lambda / beta, the doublings of the stock A per doubling of research input E. C4
and C6 need r for the software loop, and the gain of a loop run at fixed compute,
K = (1 - a) r, where a is compute's share of research input, E = L^(1 - a) K^a (Part I, Y1a; the
claims file's epsilon_K). E9 refits r from the public data behind the published estimates, lets a
run from 0 to 1 instead of fixing it, and reports where the data do not identify r, a, or the side
of 1 they fall on.

Data, all fetched with their sha256 recorded.
- Ho and Whitfill's three AI domains (computer vision, Atari reinforcement learning, language
  models): their notebook (pinned commit) for the counts and doubling times they used; the same
  OpenAlex queries rerun today; Epoch's model data for each domain's training compute.
- Their frontier-firm case (OpenAI, 2022 to 2025): staff counts and compute estimates from their
  repository (pinned commit).
- Erdil, Besiroglu and Ho's cases: their notebook (pinned commit) for the SAT, linear-programming,
  vision and Atari inputs; their Stockfish sheet (Elo history, Fishtest test runs and CPU-years);
  their US TFP sheet.
- Bloom, Jones, Van Reenen and Webb's replication files, from the author's site (the licence is
  not stated in the package): the Moore's Law R&D series, the aggregate IPP and TFP series and the
  wage deflator.

Method.
- Steady-state domains (one output trend each): on a steady path r = g_A / g_E, and with compute's
  share free g_E = (1 - a) g_L + a g_K. The data hold one output trend and one trend per input, so
  lambda and beta are not identified apart and a is not identified at all: r is a curve in a. We
  reproduce each published number on its authors' inputs, refit on ours, report the spread across
  input specifications, and an interval from the published uncertainty of the output trend and the
  slopes' standard errors (20,000 seeded draws). K(a) counts the historical growth of compute; the
  published correction divides the labour-only r by 1 / (1 - a), which leaves compute's growth out.
- Time-series domains (Stockfish, US TFP): the one-step likelihood of Erdil, Besiroglu and Ho
  (A_(i+1)^beta = A_i^beta + delta beta I_i + noise with sd sigma A_i^(beta/2) I_i^(1/2), I_i the
  integral of E^lambda over the step), bootstrapped over steps (200 refits). The US series uses
  their Gaussian noise. Stockfish's progress jumps (NNUE in 2020), so its main fit uses Student-t
  noise, close to their stable noise; under Gaussian noise beta runs to zero and r is unbounded,
  which is recorded. For Stockfish the input is also split into test runs and CPU-years with the
  share free (a profile likelihood), and tested against lambda = 0 and against a smooth-trend
  placebo input with the input's own growth. Bloom et al.'s beta (lambda = 1) is recomputed from
  their files and programs.

Selection and limits. Paper counts and staff stand in for research labour, notable models'
training compute for research compute; neither is research input measured directly. OpenAlex
reclassifies works, so today's counts differ from the counts the authors downloaded. Every series
is human-driven progress before AI research labour mattered, and only the OpenAI case is at the
frontier (one firm, three compute points, the efficiency trend assumed).

Claims served: C4 (the prior on r), C6 (the software loop's diagonal entry), C2 (drift rising with
research labour) and C12 (whether the software loop can run away at fixed compute).

  .venv/bin/python tools/exp/e09_returns.py      (CPU, about 20 seconds once the data are cached)
"""

from __future__ import annotations

import ast
import csv
import io
import json
import math
import operator
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

import numpy as np
from scipy import io as sio
from scipy import optimize, stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127
DRAWS = 20_000
BOOT = 200
SHARES = np.round(np.linspace(0.0, 1.0, 101), 2)

HW_COMMIT = "86f8cc092316640b3a01530aa58784575ef10e2a"
HW_RAW = f"https://raw.githubusercontent.com/parkerwhitfill/epoch_RRD/{HW_COMMIT}/"
ERDIL_COMMIT = "cbd19e55919587c55aea1ba38a503153f95b38fd"
ERDIL_RAW = f"https://raw.githubusercontent.com/ege-erdil/estimating-returns-to-rnd/{ERDIL_COMMIT}/"
SHEET = "https://docs.google.com/spreadsheets/d/{id}/export?format=csv&gid={gid}"
STOCKFISH = "1_PTiZ1_faoUW4BjRaGA2rx39tGIK2ODa18FJyTHrZh0"
TFP = "1BLTbmVfB-tACJULIw4EW6c4dHA48C7SX6T6W9GB5ZSg"
BLOOM_URL = "https://web.stanford.edu/~chadj/IdeaPFPrograms.zip"
MODELS_URL = "https://epoch.ai/data/all_ai_models.csv"
OPENALEX = "https://api.openalex.org/works?filter={f}&group_by=publication_year"
TABLE = ROOT / "tools" / "exp" / "data" / "e09_returns.csv"
Z95 = 1.959963984540054

# The AI domains of Ho and Whitfill. The OpenAlex concepts and Epoch domain are theirs and Epoch's
# labels; the names of the notebook variables are where their inputs are read from.
AI = {
    "cv": {"name": "computer vision", "concepts": "concepts.id:C108583219,concepts.id:C31972630",
           "epoch": "Vision", "hw": "cv", "hw_key": "CV + DL", "erdil_key": "CV + DL"},
    "rl": {"name": "reinforcement learning (Atari)", "concepts": "concepts.id:C97541855",
           "epoch": "Games", "hw": "rl", "hw_key": "RL", "erdil_key": "Atari (RL)"},
    "lm": {"name": "language models", "concepts": "concepts.id:C108583219,concepts.id:C204321447",
           "epoch": "Language", "hw": "lm", "hw_key": "NLP + DL", "erdil_key": None},
}
OTHER = {
    "sat": {"name": "SAT solvers", "concepts": "concepts.id:C6943359", "erdil_key": "SAT"},
    "lp": {"name": "linear programming", "concepts": "concepts.id:C41045048", "erdil_key": "LP"},
}
LEDGER_IDS = [
    "dyn-r-cv", "dyn-r-cv-lo", "dyn-r-cv-hi", "dyn-r-rl", "dyn-r-rl-lo", "dyn-r-rl-hi",
    "dyn-r-lm", "dyn-r-lm-lo", "dyn-r-lm-hi", "dyn-r-chess", "dyn-r-chess-se", "dyn-r-us-economy",
    "dyn-bloom-beta-aggregate", "dyn-bloom-beta-moore", "dyn-research-compute-share",
    "dyn-algo-halving-months", "phys-algo-halving-low", "phys-algo-halving-high",
    "dyn-algo-efficiency-growth", "dyn-r-lm-corrected", "dyn-r-lm-hi-corrected",
]


# ---------------------------------------------------------------------------------------------
# Small tools


def ols(x, y):
    """Slope, its standard error (residuals treated as independent) and intercept."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    xm, ym = x.mean(), y.mean()
    sxx = ((x - xm) ** 2).sum()
    slope = ((x - xm) * (y - ym)).sum() / sxx
    resid = y - (ym + slope * (x - xm))
    dof = max(len(x) - 2, 1)
    se = math.sqrt((resid ** 2).sum() / dof / sxx)
    return float(slope), float(se), float(ym - slope * xm)


def q(arr, p):
    """A percentile that is an actual draw, so an unbounded draw stays unbounded, not NaN."""
    return float(np.quantile(arr, p, method="inverted_cdf"))


def finite_or_word(x):
    """Results are strict JSON: an infinite value is written as the word 'unbounded'."""
    if isinstance(x, dict):
        return {k: finite_or_word(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [finite_or_word(v) for v in x]
    if isinstance(x, float) and not math.isfinite(x):
        if x != x:
            raise ValueError("a NaN reached the results")
        return "unbounded"
    return x


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg}


def arith(node):
    """Evaluate a literal that may hold arithmetic (2**(12*10/9)), and nothing else."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float, str)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](arith(node.left), arith(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](arith(node.operand))
    if isinstance(node, (ast.List, ast.Tuple)):
        return [arith(e) for e in node.elts]
    if isinstance(node, ast.Dict):
        return {arith(k): arith(v) for k, v in zip(node.keys, node.values)}
    raise ValueError(f"not a plain literal: {ast.dump(node)[:80]}")


def notebook_code(path: Path) -> str:
    nb = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")


def assignment(code: str, name: str):
    """The one uncommented top-level assignment `name = <literal>` in a notebook, and its comment."""
    hits = re.findall(rf"^{name}\s*=\s*([^#\n]+?)\s*(#[^\n]*)?$", code, flags=re.M)
    if len(hits) != 1:
        raise SystemExit(f"{name}: found {len(hits)} assignments in the notebook; it changed shape")
    value, comment = hits[0]
    return arith(ast.parse(value, mode="eval").body), comment


def literal_block(code: str, name: str):
    """The uncommented `name = { ... }` literal that may span lines."""
    m = re.search(rf"^{name}\s*=\s*(\{{.*?\}})\s*$", code, flags=re.M | re.S)
    if not m:
        raise SystemExit(f"{name}: not found in the notebook")
    return arith(ast.parse(m.group(1).replace("\\\n", "\n"), mode="eval").body)


def m_matrix(text: str, name: str) -> list[list[str]]:
    """Rows of a MATLAB literal `name=[ ... ];`, comments dropped, tokens kept as strings."""
    start = re.search(rf"^{name}\s*=\s*\[", text, flags=re.M)
    if not start:
        raise SystemExit(f"{name}: not found in the replication file")
    rows = []
    for line in text[start.end():].splitlines():
        line = line.split("%", 1)[0].strip()
        if line.startswith("];") or line == "]":
            break
        if line:
            rows.append(line.split())
    return rows


def split_lognormal(gen, point, lo, hi, n):
    """Draws whose log is a two-piece normal with median ln(point) and 2.5th and 97.5th
    percentiles at ln(lo) and ln(hi): a published asymmetric 95% interval."""
    z = gen.standard_normal(n)
    sd_lo = (math.log(point) - math.log(lo)) / Z95
    sd_hi = (math.log(hi) - math.log(point)) / Z95
    return np.exp(math.log(point) + np.where(z < 0, z * sd_lo, z * sd_hi))


def read_table():
    rows = {r["id"]: r for r in csv.DictReader(TABLE.open(encoding="utf-8"))}
    num = lambda r, k: float(r[k]) if r[k] else None  # noqa: E731
    return {k: {"value": num(r, "value"), "lo": num(r, "lo"), "hi": num(r, "hi"),
                "source": r["source"], "where": r["where"]} for k, r in rows.items()}


# ---------------------------------------------------------------------------------------------
# Steady-state domains


def openalex(res, key, concepts):
    path = fetch(OPENALEX.format(f=concepts), f"openalex/{key}.json", res,
                 what=f"OpenAlex works per publication year, {concepts}")
    data = json.loads(path.read_text(encoding="utf-8"))
    return {int(g["key"]): int(g["count"]) for g in data["group_by"] if str(g["key"]).isdigit()}


def endpoint_growth(series):
    """Ho and Whitfill's and Erdil et al.'s input growth: ln(last / first) / (n - 1)."""
    return math.log(series[-1] / series[0]) / (len(series) - 1)


def input_specs(counts, years):
    """Growth of the labour proxy under the specifications we try, all on the same window."""
    flows = [counts[y] for y in years]
    cum, total = [], sum(counts[y] for y in counts if y < years[0])
    for y in years:
        total += counts[y]
        cum.append(total)
    # Ho and Whitfill accumulate from the window's first year, not from the start of the record.
    cum_from_window = np.cumsum(flows).tolist()
    slope_f, se_f, _ = ols(years, np.log(flows))
    slope_c, se_c, _ = ols(years, np.log(cum_from_window))
    return {
        "cumulative from window start, endpoints": (endpoint_growth(cum_from_window), None),
        "cumulative from window start, slope": (slope_c, se_c),
        "cumulative over the whole record, endpoints": (endpoint_growth(cum), None),
        "flows, endpoints": (endpoint_growth(flows), None),
        "flows, slope": (slope_f, se_f),
    }


def epoch_compute(rows, domain, y0, y1):
    """Two proxies for the growth of a domain's research compute: the trend of notable models'
    training compute, and the trend of the domain's yearly total. Natural log per year."""
    pts = []
    for r in rows:
        if domain not in [d.strip() for d in r["Domain"].split(",")]:
            continue
        try:
            flop = float(r["Training compute (FLOP)"])
            d = date.fromisoformat(r["Publication date"][:10])
        except ValueError:
            continue
        t = d.year + (d.timetuple().tm_yday - 0.5) / 365.25
        if y0 <= d.year <= y1 and flop > 0:
            pts.append((t, flop, d.year))
    if len(pts) < 5:
        raise SystemExit(f"{domain}: only {len(pts)} models with compute in {y0}-{y1}")
    t = np.array([p[0] for p in pts])
    lf = np.log([p[1] for p in pts])
    trend, trend_se, _ = ols(t, lf)
    years = sorted({p[2] for p in pts})
    totals = [sum(p[1] for p in pts if p[2] == y) for y in years]
    tot, tot_se, _ = ols(years, np.log(totals))
    return {"models": len(pts), "trend": trend, "trend_se": trend_se, "total": tot,
            "total_se": tot_se, "years": years}


def r_of_share(ga, gl, gk, a):
    """r on a steady path with the composite input L^(1-a) K^a; inf where input growth <= 0."""
    den = (1 - a) * gl + a * gk
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(den > 0, ga / np.where(den > 0, den, 1.0), np.inf)


def k_of_share(ga, gl, gk, a):
    """The loop gain at fixed compute, K = (1 - a) r(a); 0 at a = 1, where no input can grow."""
    r = r_of_share(ga, gl, gk, a)
    with np.errstate(invalid="ignore"):
        return np.where(np.asarray(a) >= 1, 0.0, (1 - np.asarray(a)) * r)


FINE = np.linspace(0.0, 1.0, 100_001)


def critical_share(ga, gl, gk):
    """The largest share at which K(a) >= 1, so K < 1 at every share above it; 0 if K < 1
    throughout. On a grid of 1e-5, since with a shrinking compute proxy K need not be monotone."""
    above = k_of_share(ga, gl, gk, FINE) >= 1
    return float(FINE[np.nonzero(above)[0].max()]) if above.any() else 0.0


def critical_share_closed(ga, gl, gk):
    """The same share in closed form, valid when compute's proxy grows (gk > 0)."""
    return max(0.0, (ga - gl) / (ga - gl + gk)) if ga > gl else 0.0


def steady_ai(res, ledger, table, models, hw_code, erdil_code, gen):
    out = {}
    share = ledger["dyn-research-compute-share"]
    hw_categories = {}
    for key, d in AI.items():
        p = d["hw"]
        flows, comment = assignment(hw_code, f"{p}_flows")
        period, _ = assignment(hw_code, f"{p}_time_period")
        months, _ = assignment(hw_code, f"{p}_doubling_time")
        span = re.search(r"(\d{4}) to (\d{4})", comment)
        if not span:
            raise SystemExit(f"{p}_flows: no year range in its comment")
        first = int(span.group(1))
        hw_years = list(range(first, first + int(period)))
        hw_flows = flows[: int(period)]
        # Their estimate: cumulative counts from the window's first year, endpoints.
        hw_gl = endpoint_growth(np.cumsum(hw_flows).tolist())
        hw_ga = math.log(2) * 12 / months
        hw_categories[key] = {"years": hw_years, "flows": hw_flows, "doubling_months": months}

        counts = openalex(res, key, d["concepts"])
        specs = input_specs(counts, hw_years)
        earlier = input_specs(counts, [y - 1 for y in hw_years])["flows, slope"]
        later = input_specs(counts, [y + 1 for y in hw_years])["flows, slope"]
        specs["flows, slope, window a year earlier"] = earlier
        specs["flows, slope, window a year later"] = later
        specs["their counts (vintage 2025-11-12), cumulative from window start, endpoints"] = (hw_gl, None)
        if d["erdil_key"]:
            cat = literal_block(erdil_code, "categories")[d["erdil_key"]]
            specs["Erdil et al.'s unique authors, flows, endpoints"] = (endpoint_growth(cat[2]), None)

        # The output trend: the published doubling time and its uncertainty.
        if key == "lm":
            point, lo, hi = (ledger["dyn-algo-halving-months"], ledger["phys-algo-halving-low"],
                             ledger["phys-algo-halving-high"])
            ga_draws = math.log(2) * 12 / split_lognormal(gen, point, lo, hi, DRAWS)
            ga_note = "Ho et al.'s halving time with its 95% interval (ledger)"
        elif key == "cv":
            row = table["cv-doubling"]
            point, lo, hi = row["value"], row["lo"], row["hi"]
            ga_draws = math.log(2) * 12 / split_lognormal(gen, point, lo, hi, DRAWS)
            ga_note = "Erdil and Besiroglu's halving time with its 95% interval"
        else:
            point = table["rl-doubling"]["value"]
            lo, hi = table["rl-doubling-range"]["lo"], table["rl-doubling-range"]["hi"]
            ga_draws = math.log(2) * 12 / np.exp(gen.uniform(math.log(lo), math.log(hi), DRAWS))
            ga_note = "Dorner's range across Atari tasks, drawn uniformly in log; not a confidence interval"
        ga = math.log(2) * 12 / point
        doubling_specs = {f"{point:g} months": ga}
        if abs(months - point) > 1e-9:
            doubling_specs[f"{months:g} months (Ho and Whitfill's value)"] = hw_ga

        comp = epoch_compute(models, d["epoch"], hw_years[0], hw_years[-1])
        gk_specs = {"trend of notable models' training compute": comp["trend"],
                    "trend of the domain's yearly total training compute": comp["total"]}

        gl, gl_se = specs["flows, slope"]
        gk, gk_se = comp["trend"], comp["trend_se"]
        gl_draws = gen.normal(gl, gl_se, DRAWS)
        gk_draws = gen.normal(gk, gk_se, DRAWS)

        def at(a, ga_=ga, gl_=gl, gk_=gk):
            return float(r_of_share(ga_, gl_, gk_, a))

        grid = []
        for a in SHARES:
            rd = r_of_share(ga_draws, gl_draws, gk_draws, a)
            kd = k_of_share(ga_draws, gl_draws, gk_draws, a)
            grid.append({"share": float(a), "r": at(a), "r_p05": q(rd, 0.05), "r_p50": q(rd, 0.5),
                         "r_p95": q(rd, 0.95), "p_r_above_1": float((rd > 1).mean()),
                         "k": float(k_of_share(ga, gl, gk, a)), "k_p05": q(kd, 0.05), "k_p95": q(kd, 0.95),
                         "p_k_above_1": float((kd > 1).mean())})
        rd0 = r_of_share(ga_draws, gl_draws, gk_draws, 0.0)
        rds = r_of_share(ga_draws, gl_draws, gk_draws, share)
        kds = k_of_share(ga_draws, gl_draws, gk_draws, share)
        # Smallest share at which K's 95th percentile is below 1 (the loop is subcritical at 95%).
        safe = next((g["share"] for g in grid if g["k_p95"] < 1), None)

        spec_table = []
        for gname, (gl_s, _) in specs.items():
            for dname, ga_s in doubling_specs.items():
                for kname, gk_s in gk_specs.items():
                    spec_table.append({
                        "labour proxy": gname, "output trend": dname, "compute proxy": kname,
                        "g_A": ga_s, "g_L": gl_s, "g_K": gk_s,
                        "r_labour_only": float(r_of_share(ga_s, gl_s, gk_s, 0.0)),
                        "r_at_share": float(r_of_share(ga_s, gl_s, gk_s, share)),
                        "k_at_share": (1 - share) * float(r_of_share(ga_s, gl_s, gk_s, share)),
                        "critical_share": critical_share(ga_s, gl_s, gk_s),
                    })
        r0s = [s["r_labour_only"] for s in spec_table]
        kss = [s["k_at_share"] for s in spec_table]
        crit = [s["critical_share"] for s in spec_table]
        out[key] = {
            "name": d["name"], "window": [hw_years[0], hw_years[-1]],
            "repro": hw_ga / hw_gl, "repro_inputs": {"g_A": hw_ga, "g_L": hw_gl},
            "g_A": ga, "g_A_note": ga_note, "g_L": gl, "g_L_se": gl_se, "g_K": gk, "g_K_se": gk_se,
            "compute": comp, "openalex_counts": {str(y): counts[y] for y in sorted(counts) if 2005 <= y <= 2025},
            "r_labour": at(0.0), "r_labour_p05": q(rd0, 0.05), "r_labour_p95": q(rd0, 0.95),
            "p_r_labour_above_1": float((rd0 > 1).mean()),
            "r_share": at(share), "k_share": (1 - share) * at(share),
            "k_share_p05": q(kds, 0.05), "k_share_p95": q(kds, 0.95),
            "p_k_share_above_1": float((kds > 1).mean()),
            "p_k_share_unbounded": float(np.isinf(kds).mean()),
            "k_published_correction": (1 - share) * at(0.0),
            "critical_share": critical_share(ga, gl, gk),
            "share_where_r_is_1": ((ga - gl) / (gk - gl)) if (gk > ga > gl) else None,
            "safe_share_95": safe,
            "compute_informative": bool(gk - 1.6448536269514722 * gk_se > 0),
            # K(a) = 1 solved for compute's growth: (1 - a)(g_A - g_L) / a.
            "gk_critical_at_share": (1 - share) * (ga - gl) / share,
            "spec_r_min": min(r0s), "spec_r_max": max(r0s), "spec_k_min": min(kss),
            "spec_k_max": max(kss), "spec_crit_min": min(crit), "spec_crit_max": max(crit),
            "specs": spec_table, "grid": grid[::10],
        }
    return out, hw_categories


def steady_other(res, table, erdil_code):
    """SAT solvers and linear programming: Erdil et al.'s inputs, and the same idea on today's
    OpenAlex works counts. No compute series exists for these; a enters only through (1 - a)."""
    cats = literal_block(erdil_code, "categories")
    out = {}
    for key, d in OTHER.items():
        times, levels, counts_e = cats[d["erdil_key"]]
        years_span = times[1] - times[0]
        ga = math.log(levels[1] / levels[0]) / years_span
        gl_e = math.log(counts_e[times[1] - 1] / counts_e[times[0]]) / (years_span - 1)
        first = int(table[f"{key}-period"]["lo"])
        last = int(table[f"{key}-period"]["hi"])
        counts = openalex(res, key, d["concepts"])
        years = list(range(first, last + 1))
        gl, gl_se, _ = ols(years, np.log([counts[y] for y in years]))
        out[key] = {"name": d["name"], "g_A": ga, "repro": ga / gl_e, "g_L_their_authors": gl_e,
                    "r_ours": ga / gl, "g_L_ours": gl, "g_L_ours_se": gl_se, "window": [first, last],
                    "published": table[f"{key}-r-2024"]["value"],
                    "published_naive": table[f"{key}-naive-2024"]["value"]}
    return out


def frontier_firm(res, ledger, table, gen):
    """Ho and Whitfill's Appendix C: OpenAI's staff and compute, 2022 to 2025, with a free."""
    staff_path = fetch(HW_RAW + "data/ai_companies/ai_companies_staff_reports.csv",
                       f"epoch_rrd/{HW_COMMIT[:7]}/ai_companies_staff_reports.csv", res,
                       what="Ho and Whitfill's copy of Epoch's AI-company staff reports")
    spend_path = fetch(HW_RAW + "data/openai_rd_spend_flops.csv",
                       f"epoch_rrd/{HW_COMMIT[:7]}/openai_rd_spend_flops.csv", res,
                       what="Ho and Whitfill's estimates of OpenAI's research compute")
    code_path = fetch(HW_RAW + "code/steady_state.py", f"epoch_rrd/{HW_COMMIT[:7]}/steady_state.py", res,
                      what="Ho and Whitfill's steady-state code (its constants are read, not run)")
    code = code_path.read_text(encoding="utf-8")
    const = {k: float(v) for k, v in re.findall(r"^([A-Z_]+)\s*=\s*([0-9.]+)\s*$", code, flags=re.M)}
    start = int(const["START_YEAR"])

    t_staff, l_staff = [], []
    for r in csv.DictReader(staff_path.open(encoding="utf-8")):
        if r["Company"] != "OpenAI" or not r["Date"] or not r["Staff count"]:
            continue
        d = date.fromisoformat(r["Date"][:10])
        n = float(r["Staff count"].replace(",", ""))
        if d.year >= start and n > 0:
            t_staff.append(d.year + (d.timetuple().tm_yday - 1) / 365.25)
            l_staff.append(math.log(n))
    yrs, lk = [], []
    for r in csv.DictReader(spend_path.open(encoding="utf-8")):
        y = int(float(r["year"]))
        if start <= y <= 2025 and r["estimated_total_flops"]:
            yrs.append(y)
            lk.append(math.log(float(r["estimated_total_flops"])))
    gl, gl_se, _ = ols(t_staff, l_staff)
    gk, gk_se, _ = ols(yrs, lk)
    ga = math.log(ledger["dyn-algo-efficiency-growth"])
    # Numerator draws as in their code: a 90% range of yearly multiples, lognormal.
    z90 = stats.norm.ppf(0.5 + const["NUMERATOR_CI_LEVEL"] / 2)
    lo_m, hi_m = const["NUMERATOR_MULTIPLIER_LOWER"], const["NUMERATOR_MULTIPLIER_UPPER"]
    # Their code draws the base-e growth itself as normal, with 90% between ln 2 and ln 5.
    mu = (math.log(lo_m) + math.log(hi_m)) / 2
    sd = (math.log(hi_m) - math.log(lo_m)) / (2 * z90)
    ga_draws = gen.normal(mu, sd, DRAWS)
    gl_draws = gen.normal(gl, gl_se, DRAWS)
    gk_draws = gen.normal(gk, gk_se, DRAWS)
    s_mode, s_lo, s_hi = const["SHARE_MODE"], const["SHARE_MIN"], const["SHARE_MAX"]
    share_draws = gen.triangular(s_lo, s_mode, s_hi, DRAWS)
    rd = r_of_share(ga_draws, gl_draws, gk_draws, share_draws)
    kd = (1 - share_draws) * rd
    grid = []
    for a in SHARES[::10]:
        rda = r_of_share(ga_draws, gl_draws, gk_draws, a)
        kda = k_of_share(ga_draws, gl_draws, gk_draws, a)
        grid.append({"share": float(a), "r": float(r_of_share(ga, gl, gk, a)), "k": float(k_of_share(ga, gl, gk, a)),
                     "k_p95": q(kda, 0.95), "p_k_above_1": float((kda > 1).mean())})
    published = {k: table[f"openai-{k}-2025"]["value"] for k in ("gk", "gl", "ga")}
    return {
        "g_L": gl, "g_L_se": gl_se, "g_K": gk, "g_K_se": gk_se, "g_A": ga, "staff_points": len(l_staff),
        "compute_years": yrs, "their_constants": const, "published_inputs": published,
        "r_labour": float(r_of_share(ga, gl, gk, 0.0)), "r_compute": float(r_of_share(ga, gl, gk, 1.0)),
        "r_share": float(r_of_share(ga, gl, gk, s_mode)),
        "k_share": (1 - s_mode) * float(r_of_share(ga, gl, gk, s_mode)),
        "r_p05": q(rd, 0.05), "r_p95": q(rd, 0.95), "p_r_above_1": float((rd > 1).mean()),
        "k_p05": q(kd, 0.05), "k_p95": q(kd, 0.95), "p_k_above_1": float((kd > 1).mean()),
        "critical_share": critical_share(ga, gl, gk), "grid": grid,
    }


def bloom_tables(res):
    """Bloom et al.'s b for Moore's Law and the aggregate economy, recomputed from their files
    with lambda = 1, as their programs do."""
    path = fetch(BLOOM_URL, "bloom2020/IdeaPFPrograms.zip", res,
                 what="Bloom, Jones, Van Reenen and Webb, replication files (licence not stated)")
    z = zipfile.ZipFile(path)
    wage = sio.loadmat(io.BytesIO(z.read("WageSci/WageScientistData.mat")))
    wage_years = wage["WageYears"].ravel().astype(int)
    wage_sci = wage["WageScientist"].ravel().astype(float)
    wage_at = lambda y: wage_sci[y - wage_years[0]]  # noqa: E731

    # Moore's Law: research = semiconductor R&D over the wage; output grows as transistor counts.
    intel = z.read("MooresLaw/IntelGraph.m").decode("latin-1")
    rows = [[float(x) for x in r] for r in m_matrix(intel, "data")]
    years = np.array([r[0] for r in rows], int)
    rnd = np.array([r[1:] for r in rows])
    gmoore_doubling = float(re.search(r"gmoore\s*=\s*log\(2\)/(\d+)", intel).group(1))
    gmoore = math.log(2) / gmoore_doubling
    versions = ["Narrow", "Narrow (half)", "Broad", "Broad (half)", "Intel only", "Intel+AMD"]
    sci = rnd / np.array([wage_at(y) for y in years])[:, None]
    moore = {}
    for i, v in enumerate(versions):
        g_sci = math.log(sci[-1, i] / sci[0, i]) / (years[-1] - years[0])
        moore[v] = {"g_scientists": g_sci, "beta": g_sci / gmoore, "r": gmoore / g_sci}

    # The aggregate economy: decadal TFP growth (Gordon for the 1930s and 1940s, BLS after, with
    # R&D and IPP added back), researchers = IPP over the wage, decade geometric means.
    agg = z.read("Aggregate/AggregateBLSIPP.m").decode("latin-1")
    gordon = [[float(x) for x in r] for r in m_matrix(agg, "Gordondata")]
    ipp = [(int(r[0][:4]), float(r[4])) for r in m_matrix(agg, "datarnd")]
    bls = [[float(x) if x != "NaN" else math.nan for x in r] for r in m_matrix(agg, "blsdata")]
    bls_years = [int(r[0]) for r in bls]
    level = np.array([r[1] for r in bls])
    rnd_c = np.nan_to_num(np.diff(np.log([r[2] for r in bls])))
    ipp_c = np.nan_to_num(np.diff(np.log([r[3] for r in bls])))
    growth = np.diff(np.log(level)) + rnd_c + ipp_c
    index = np.exp(np.concatenate([[0.0], np.cumsum(growth)])) * level[0]
    avg_years = [1950, 1960, 1970, 1980, 1990, 2000, 2014]
    at_year = [index[bls_years.index(y)] for y in avg_years]
    tfp_fixed = list(np.diff(np.log(at_year)) / np.diff(avg_years) * 100)
    tfp_growth = np.array([gordon[0][1], gordon[1][1]] + tfp_fixed)
    decades = [(1930, 1940), (1940, 1950), (1950, 1960), (1960, 1970), (1970, 1980), (1980, 1990),
               (1990, 2000), (2000, 2015)]
    sci_annual = {y: v / wage_at(y) * 1e9 for y, v in ipp}
    scientists = np.array([math.exp(np.mean([math.log(sci_annual[y]) for y in range(a, b + 1)]))
                           for a, b in decades])
    scientists = scientists / scientists[0]
    idea_tfp = tfp_growth / scientists
    idea_tfp = idea_tfp / idea_tfp[0]
    span = 0.5 * (2000 + 2015) - 0.5 * (1940 + 1930)
    g_idea = 100 * math.log(idea_tfp[-1] / idea_tfp[0]) / span
    beta_agg = -g_idea / tfp_growth.mean()
    # With lambda free on eight decades: ln g_A = c - beta ln A + lambda ln S. Collinear trends?
    lengths = np.array([b - a for a, b in decades], float)
    log_a = np.cumsum(tfp_growth / 100 * lengths)
    corr = float(np.corrcoef(log_a, np.log(scientists))[0, 1])
    return {
        "moore": moore, "moore_output_doubling_years": gmoore_doubling,
        "aggregate": {"beta": beta_agg, "r": 1 / beta_agg, "idea_tfp_growth_pct": g_idea,
                      "tfp_growth_pct_by_decade": tfp_growth.tolist(),
                      "scientists_index_by_decade": scientists.tolist(),
                      "corr_log_tfp_log_scientists": corr},
    }


# ---------------------------------------------------------------------------------------------
# Time-series domains: the one-step likelihood


class OneStep:
    """Steps i -> i+1 of a stock A, with research input flows F on a grid of unit cells.
    I_i(lambda) = sum of F^lambda over the cells the step spans."""

    def __init__(self, a0, a1, c0, c1, log_flow):
        self.a0, self.a1 = np.asarray(a0, float), np.asarray(a1, float)
        self.c0, self.c1 = np.asarray(c0, int), np.asarray(c1, int)
        self.log_flow = np.asarray(log_flow, float)
        self.la0, self.la1 = np.log(self.a0), np.log(self.a1)

    def subset(self, idx):
        return OneStep(self.a0[idx], self.a1[idx], self.c0[idx], self.c1[idx], self.log_flow)

    def with_flow(self, log_flow):
        return OneStep(self.a0, self.a1, self.c0, self.c1, log_flow)

    def integral(self, lam):
        cum = np.concatenate([[0.0], np.cumsum(np.exp(lam * self.log_flow))])
        return cum[self.c1] - cum[self.c0]

    def gauss_nll(self, phi, lam):
        """Negative log-likelihood with Gaussian noise, delta and sigma profiled out exactly."""
        if not (0.005 < phi < 40):
            return 1e12
        i = self.integral(lam)
        x0, x1 = np.exp(phi * self.la0), np.exp(phi * self.la1)
        y, x, v = x1 - x0, phi * i, np.exp(phi * self.la0) * i
        delta = (y * x / v).sum() / (x * x / v).sum()
        s2 = ((y - delta * x) ** 2 / v).mean()
        n = len(y)
        ll = (math.log(phi) * n + ((phi - 1) * self.la1).sum() - 0.5 * np.log(s2 * v).sum()
              - 0.5 * n * (1 + math.log(2 * math.pi)))
        return -float(ll)

    def t_nll(self, theta):
        phi, lam, ldelta, lsigma, lnu = theta
        if not (0.005 < phi < 40) or not (-8 < lnu < 8):
            return 1e12
        i = self.integral(lam)
        x0, x1 = np.exp(phi * self.la0), np.exp(phi * self.la1)
        scale = math.exp(lsigma) * np.exp(0.5 * phi * self.la0) * np.sqrt(i)
        z = (x1 - x0 - math.exp(ldelta) * phi * i) / scale
        ll = (math.log(phi) + (phi - 1) * self.la1 - np.log(scale)
              + t_logpdf(z, math.exp(lnu)))
        return -float(ll.sum())

    def gauss_delta_sigma(self, phi, lam):
        i = self.integral(lam)
        x0, x1 = np.exp(phi * self.la0), np.exp(phi * self.la1)
        y, x, v = x1 - x0, phi * i, np.exp(phi * self.la0) * i
        delta = (y * x / v).sum() / (x * x / v).sum()
        return float(delta), float(math.sqrt(((y - delta * x) ** 2 / v).mean()))


def fit_gauss(model, lam_lo, lam_hi, start=None, fixed_lam=None, grid=True):
    """Maximum likelihood (phi, lambda): a coarse grid, then Nelder-Mead from the best points.
    Bootstrap refits start from the full-sample optimum only (grid=False), as Erdil et al. do."""
    if fixed_lam is not None:
        f1 = lambda p: model.gauss_nll(p[0], fixed_lam)  # noqa: E731
        best = min((f1([p]), p) for p in np.geomspace(0.02, 30, 40))
        r = optimize.minimize(f1, [best[1]], method="Nelder-Mead",
                              options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 4000})
        return {"phi": float(r.x[0]), "lam": fixed_lam, "nll": float(r.fun)}
    f = lambda p: model.gauss_nll(p[0], p[1]) if lam_lo <= p[1] <= lam_hi else 1e12  # noqa: E731
    cands = []
    if start is not None:
        cands.append(list(start))
    if grid or start is None:
        coarse = sorted((f([p, l]), p, l) for p in np.geomspace(0.03, 25, 16)
                        for l in np.linspace(lam_lo, lam_hi, 16))
        cands += [[p, l] for _, p, l in coarse[:3]]
    best = None
    for c in cands:
        r = optimize.minimize(f, c, method="Nelder-Mead",
                              options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 4000})
        if best is None or r.fun < best.fun - 1e-12:
            best = r
    return {"phi": float(best.x[0]), "lam": float(best.x[1]), "nll": float(best.fun)}


def bootstrap(model, fit, lam_lo, lam_hi, seed_tag):
    gen = np.random.default_rng([SEED, seed_tag])
    n = len(model.a0)
    phis, lams = [], []
    for _ in range(BOOT):
        idx = gen.integers(0, n, n)
        b = fit_gauss(model.subset(idx), lam_lo, lam_hi, start=(fit["phi"], fit["lam"]), grid=False)
        phis.append(b["phi"])
        lams.append(b["lam"])
    phis, lams = np.array(phis), np.array(lams)
    return phis, lams, lams / phis


def daily_flows(dates, cumulative, day0, day1):
    """Daily increments of a cumulative series, linearly interpolated between its dates."""
    ords = np.array([d.toordinal() for d in dates], float)
    grid = np.arange(day0, day1 + 1, dtype=float)
    cum = np.interp(grid, ords, np.asarray(cumulative, float))
    return np.diff(cum)


def t_logpdf(z, nu):
    return (math.lgamma((nu + 1) / 2) - math.lgamma(nu / 2) - 0.5 * math.log(nu * math.pi)
            - (nu + 1) / 2 * np.log1p(z * z / nu))


def fit_t(model, starts, lam_lo=0.0, lam_hi=6.0, fixed_lam=None):
    """Maximum likelihood with Student-t noise, all five parameters free (lambda fixed if asked).
    Nelder-Mead from each start; the best is kept."""
    best = None
    for st in starts:
        if len(st) == 5:
            x0 = list(st)
        else:
            phi, lam = st
            delta, sigma = model.gauss_delta_sigma(phi, lam if fixed_lam is None else fixed_lam)
            x0 = [phi, lam, math.log(delta if delta > 0 else 1e-3), math.log(sigma), math.log(3.0)]
        if fixed_lam is None:
            f = lambda x: model.t_nll(x) if lam_lo <= x[1] <= lam_hi else 1e12  # noqa: E731
            y0 = x0
        else:
            f = lambda x: model.t_nll([x[0], fixed_lam, x[1], x[2], x[3]])  # noqa: E731
            y0 = [x0[0], x0[2], x0[3], x0[4]]
        r = optimize.minimize(f, y0, method="Nelder-Mead",
                              options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 8000, "maxfev": 8000})
        if best is None or r.fun < best[1] - 1e-12:
            x = list(r.x) if fixed_lam is None else [r.x[0], fixed_lam, r.x[1], r.x[2], r.x[3]]
            best = (x, float(r.fun))
    x, nll = best
    return {"phi": float(x[0]), "lam": float(x[1]), "nu": float(math.exp(x[4])), "nll": nll, "x": x}


def chess(res, table, gen_tag=1):
    elo_path = fetch(SHEET.format(id=STOCKFISH, gid=0), "stockfish/elo_history.csv", res,
                     what="Erdil et al.'s Stockfish sheet: regression-test Elo by version")
    cpu_path = fetch(SHEET.format(id=STOCKFISH, gid=1718304314), "stockfish/cpu_years.csv", res,
                     what="Erdil et al.'s Stockfish sheet: Fishtest CPU-years, cumulative")
    runs_path = fetch(SHEET.format(id=STOCKFISH, gid=1742775451), "stockfish/test_runs.csv", res,
                      what="Erdil et al.'s Stockfish sheet: Fishtest test runs, cumulative")
    ce = table["chess-elo-per-efold"]["value"]

    # Elo history, normalised as Erdil et al. do: each Elo is against the last release, and a
    # release row (no Elo) moves the base by the last measured gain.
    hist, base, last = [], 0.0, 0.0
    for r in csv.DictReader(elo_path.open(encoding="utf-8")):
        d = date.fromisoformat(r["Date"].replace("‑", "-").strip())
        cell = (r.get("Elo (single-thread)") or "").strip()
        if cell:
            m = re.search(r"Elo:\s*([-0-9.]+)", cell)
            if not m:
                continue
            last = float(m.group(1))
            hist.append((d, last + base))
        else:
            base += last
    runs = [(date.fromisoformat(r["Date"]), float(r["Test runs (cumulative)"]))
            for r in csv.DictReader(runs_path.open(encoding="utf-8"))]
    cpu = [(date.fromisoformat(r["Date"]), float(r["CPU years (cumulative)"]))
           for r in csv.DictReader(cpu_path.open(encoding="utf-8"))]

    day0 = runs[0][0].toordinal()
    day1 = runs[-1][0].toordinal()
    f_runs = daily_flows([d for d, _ in runs], [v for _, v in runs], day0, day1)
    if (f_runs <= 0).any():
        raise SystemExit("a day with no test runs; lambda <= 0 would be undefined")
    log_runs = np.log(f_runs) - np.log(f_runs).mean()

    a0, a1, c0, c1, t0 = [], [], [], [], []
    for (d0, e0), (d1, e1) in zip(hist, hist[1:]):
        if d0 == d1 or d0.toordinal() < day0:
            continue
        if d1.toordinal() > day1:
            break
        a0.append(math.exp(e0 / ce))
        a1.append(math.exp(e1 / ce))
        c0.append(d0.toordinal() - day0)
        c1.append(d1.toordinal() - day0)
        t0.append(d0)
    model = OneStep(a0, a1, c0, c1, log_runs)
    n = len(a0)
    starts = [(0.5, 0.4), (1.0, 0.8), (0.25, 0.2), (2.0, 1.5)]

    # Gaussian noise, as a specification: the progress series jumps (NNUE in 2020), which
    # Gaussian noise cannot absorb. Student-t noise, close to the authors' stable noise, is the
    # main fit.
    g = fit_gauss(model, 0.0, 6.0)
    t = fit_t(model, starts + [(max(g["phi"], 0.05), g["lam"])])
    t0fit = fit_t(model, starts, fixed_lam=0.0)
    lr_p = float(stats.chi2.sf(2 * (t0fit["nll"] - t["nll"]), 1))

    gen = np.random.default_rng([SEED, gen_tag])
    phis, lams = [], []
    for _ in range(BOOT):
        idx = gen.integers(0, n, n)
        b = fit_t(model.subset(idx), [t["x"]])
        phis.append(b["phi"])
        lams.append(b["lam"])
    phis, lams = np.array(phis), np.array(lams)
    rs = lams / phis

    # Placebo: the input replaced by a smooth exponential trend at the input's own growth rate.
    days = np.arange(len(log_runs), dtype=float)
    slope, _, icpt = ols(days, log_runs)
    placebo = model.with_flow(icpt + slope * days)
    tp = fit_t(placebo, starts)

    # Subsets that might move r: before and after NNUE (August 2020), halves, the jump removed.
    nnue = date(2020, 8, 1)
    jumps = set(np.argsort(-(np.log(model.a1) - np.log(model.a0)))[:3].tolist())
    subsets = {
        "steps before August 2020 (before NNUE)": [i for i in range(n) if t0[i] < nnue],
        "steps from August 2020 (NNUE on)": [i for i in range(n) if t0[i] >= nnue],
        "first half of steps": list(range(n // 2)),
        "second half of steps": list(range(n // 2, n)),
        "without the three largest steps": [i for i in range(n) if i not in jumps],
    }
    sub = {}
    for name, idx in subsets.items():
        s = fit_t(model.subset(np.array(idx)), [t["x"]] + starts)
        sub[name] = {"steps": len(idx), "beta": s["phi"], "lambda": s["lam"], "r": s["lam"] / s["phi"],
                     "nu": s["nu"]}

    # Compute's share: research input = runs^(1-a) * CPU-years^a, on the window both cover.
    cpu0, cpu1 = cpu[0][0].toordinal(), cpu[-1][0].toordinal()
    f_cpu = daily_flows([d for d, _ in cpu], [v for _, v in cpu], cpu0, cpu1)
    keep = [i for i in range(n) if c0[i] + day0 >= cpu0 and c1[i] + day0 <= cpu1]
    off = cpu0 - day0
    lr_w = np.log(f_runs[off: off + len(f_cpu)])
    lc_w = np.log(f_cpu)
    lr_w, lc_w = lr_w - lr_w.mean(), lc_w - lc_w.mean()
    two = OneStep(model.a0[keep], model.a1[keep], model.c0[keep] - off, model.c1[keep] - off, lr_w)
    months = np.array([(lambda d: d.year * 12 + d.month)(date.fromordinal(cpu0 + k)) for k in range(len(lr_w))])
    mr = np.array([lr_w[months == m].mean() for m in np.unique(months)])
    mc = np.array([lc_w[months == m].mean() for m in np.unique(months)])
    corr_inputs = float(np.corrcoef(mr, mc)[0, 1])

    profile, warm = [], [t["x"]]
    for a in np.round(np.linspace(0, 1, 21), 2):
        fa = fit_t(two.with_flow((1 - a) * lr_w + a * lc_w), warm + starts)
        warm = [fa["x"]]
        profile.append({"share": float(a), "beta": fa["phi"], "lambda": fa["lam"],
                        "r": fa["lam"] / fa["phi"], "nu": fa["nu"], "loglik": -fa["nll"]})
    best = max(profile, key=lambda p: p["loglik"])
    span = best["loglik"] - min(p["loglik"] for p in profile)
    cut = stats.chi2.ppf(0.95, 1) / 2
    in_95 = [p["share"] for p in profile if best["loglik"] - p["loglik"] <= cut]
    r_in_95 = [p["r"] for p in profile if best["loglik"] - p["loglik"] <= cut]

    return {
        "steps": n, "elo_per_efold": ce, "noise": "Student-t",
        "beta": t["phi"], "lambda": t["lam"], "nu": t["nu"], "r": t["lam"] / t["phi"],
        "loglik": -t["nll"], "loglik_lambda0": -t0fit["nll"], "lr_p": lr_p,
        "beta_lo": q(phis, 0.05), "beta_hi": q(phis, 0.95), "lambda_lo": q(lams, 0.05),
        "lambda_hi": q(lams, 0.95), "r_lo": q(rs, 0.05), "r_hi": q(rs, 0.95), "r_median": q(rs, 0.5),
        "p_r_above_1": float((rs > 1).mean()),
        "corr_beta_lambda_boot": float(np.corrcoef(phis, lams)[0, 1]),
        "gaussian": {"beta": g["phi"], "lambda": g["lam"], "loglik": -g["nll"],
                     "beta_at_search_floor": bool(g["phi"] < 0.0051),
                     "note": "beta runs to the floor of the search, so lambda / beta is unbounded"},
        "placebo": {"beta": tp["phi"], "lambda": tp["lam"], "r": tp["lam"] / tp["phi"],
                    "loglik": -tp["nll"], "loglik_gain_of_real_input": tp["nll"] - t["nll"]},
        "subsets": sub,
        "share": {"steps": len(keep), "profile": profile, "best": best, "loglik_span": span,
                  "shares_within_95": [min(in_95), max(in_95)],
                  "r_within_95": [min(r_in_95), max(r_in_95)],
                  "corr_monthly_log_inputs": corr_inputs},
    }


def us_tfp(res, gen_tag=2):
    path = fetch(SHEET.format(id=TFP, gid=0), "us_tfp/tfp_scientists.csv", res,
                 what="Erdil et al.'s US TFP sheet (Bloom et al.'s aggregate series)")
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    tfp, sci = {}, {}
    for r in rows:
        if not r["Date"]:
            continue
        y = int(r["Date"][:4])
        if r["TFP"]:
            tfp[y] = float(r["TFP"])
        if r["Scientists"]:
            sci[y] = float(r["Scientists"])
    years = [y for y in range(1948, 2014) if y in tfp and y + 1 in tfp and y in sci]
    ls = np.log([sci[y] for y in years])
    ls = ls - ls.mean()
    model = OneStep([tfp[y] for y in years], [tfp[y + 1] for y in years], list(range(len(years))),
                    list(range(1, len(years) + 1)), ls)
    g = fit_gauss(model, -4.0, 8.0)
    g0 = fit_gauss(model, -4.0, 8.0, fixed_lam=0.0)
    g1 = fit_gauss(model, -4.0, 8.0, fixed_lam=1.0)
    phis, lams, rs = bootstrap(model, g, -4.0, 8.0, gen_tag)
    pos = rs[lams > 0]
    corr = float(np.corrcoef(np.log([tfp[y] for y in years]), ls)[0, 1])
    return {
        "steps": len(years), "beta": g["phi"], "lambda": g["lam"], "r": g["lam"] / g["phi"],
        "lr_p": float(stats.chi2.sf(2 * (g0["nll"] - g["nll"]), 1)),
        "r_lambda1": 1.0 / g1["phi"], "beta_lambda1": g1["phi"],
        "r_lo": q(rs, 0.05), "r_hi": q(rs, 0.95), "beta_lo": q(phis, 0.05), "beta_hi": q(phis, 0.95),
        "lambda_lo": q(lams, 0.05), "lambda_hi": q(lams, 0.95),
        "share_lambda_not_positive": float((lams <= 0).mean()),
        "r_given_lambda_pos_median": q(pos, 0.5) if pos.size else None,
        "corr_log_tfp_log_scientists": corr,
    }


# ---------------------------------------------------------------------------------------------


def main() -> int:
    res = Results("E9", "e09_returns", seed=SEED)
    detail = res.detail
    res.detail = lambda key, value: detail(key, finite_or_word(value))  # strict JSON as each is added
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    ledger = {k: float(numbers[k]["value"]) for k in LEDGER_IDS}
    res.detail("ledger_inputs", ledger)
    table = read_table()
    gen = np.random.default_rng(SEED)

    hw_nb = fetch(HW_RAW + "code/bayesian.ipynb", f"epoch_rrd/{HW_COMMIT[:7]}/bayesian.ipynb", res,
                  what="Ho and Whitfill's notebook: the OpenAlex counts and doubling times they used")
    erdil_nb = fetch(ERDIL_RAW + "returns_to_software_rnd_bayesian_update.ipynb",
                     f"erdil2024/{ERDIL_COMMIT[:7]}/bayesian_update.ipynb", res,
                     what="Erdil, Besiroglu and Ho's notebook: their unique-author counts and output trends")
    models_path = fetch(MODELS_URL, "epoch/all_ai_models.csv", res,
                        what="Epoch AI, Data on AI models (all models)")
    models = list(csv.DictReader(models_path.open(encoding="utf-8")))
    hw_code, erdil_code = notebook_code(hw_nb), notebook_code(erdil_nb)

    ai, hw_inputs = steady_ai(res, ledger, table, models, hw_code, erdil_code, gen)
    other = steady_other(res, table, erdil_code)
    firm = frontier_firm(res, ledger, table, gen)
    bloom = bloom_tables(res)
    ch = chess(res, table)
    us = us_tfp(res)

    share = ledger["dyn-research-compute-share"]
    # Checks that cannot fail if the code is right: they stop the run instead of being reported.
    for key, d in ai.items():
        g0 = next(g for g in d["grid"] if g["share"] == 0.0)
        assert abs(g0["k"] - g0["r"]) < 1e-12, "K(0) must equal r(0)"
        if d["g_K"] > 0:
            closed = critical_share_closed(d["g_A"], d["g_L"], d["g_K"])
            assert abs(closed - d["critical_share"]) < 2e-5, "grid and closed form must agree"

    # ---- Numbers -------------------------------------------------------------------------
    pct = lambda x: 100 * x  # noqa: E731
    unbounded = {}
    number = res.number

    def guarded(id, value, **kw):
        """An unbounded value (the input does not grow, so r is infinite) is listed, not written."""
        if value is None or not math.isfinite(value):
            unbounded[id] = kw.get("label", "")
            return
        number(id, value, **kw)

    res.number = guarded
    for key in ("cv", "rl", "lm"):
        d = ai[key]
        nm = d["name"]
        pub = ledger[f"dyn-r-{key}"]
        res.number(f"e9-{key}-r-repro", d["repro"], fmt=".2f",
                   label=f"r for {nm} recomputed on Ho and Whitfill's own inputs (output over input growth)",
                   note=f"their published median is {pub:g}")
        res.number(f"e9-{key}-r-labour", d["r_labour"], fmt=".2f",
                   label=f"r for {nm}, our refit with research labour as the only input: steady-state ratio of output growth to input growth (today's OpenAlex counts, yearly flows, fitted slope)")
        res.number(f"e9-{key}-r-labour-lo", d["r_labour_p05"], fmt=".2f",
                   label=f"r for {nm}, labour only, 5th percentile of draws over the output trend's uncertainty and the input slope")
        res.number(f"e9-{key}-r-labour-hi", d["r_labour_p95"], fmt=".2f",
                   label=f"r for {nm}, labour only, 95th percentile of the same draws")
        res.number(f"e9-{key}-r-labour-above1", pct(d["p_r_labour_above_1"]), unit="%", fmt=".0f",
                   label=f"share of the labour-only draws for {nm} with r above 1")
        res.number(f"e9-{key}-r-spec-min", d["spec_r_min"], fmt=".2f",
                   label=f"r for {nm}, labour only: lowest value across input specifications and output trends")
        res.number(f"e9-{key}-r-spec-max", d["spec_r_max"], fmt=".2f",
                   label=f"r for {nm}, labour only: highest value across input specifications and output trends")
        res.number(f"e9-{key}-gk", d["g_K"], unit="per year", fmt=".2f",
                   label=f"growth of training compute in {nm} over the same window (notable models, natural log a year), the compute proxy")
        res.number(f"e9-{key}-gk-se", d["g_K_se"], unit="per year", fmt=".2f",
                   label=f"standard error of that compute growth for {nm}")
        if not d["compute_informative"]:
            # Stated before the run: a compute proxy whose growth is not above 0 at 95% one-sided
            # cannot place K(a) for a > 0, so no K is written for that domain.
            continue
        res.number(f"e9-{key}-k-fixed", d["k_share"], fmt=".2f",
                   label=f"loop gain at fixed compute for {nm}, K = (1 - a) r, at compute's share a = {share:.2f}, with compute's historical growth counted")
        if math.isfinite(d["k_share_p95"]):
            res.number(f"e9-{key}-k-fixed-hi", d["k_share_p95"], fmt=".2f",
                       label=f"loop gain at fixed compute for {nm} at a = {share:.2f}, 95th percentile of the draws")
        else:
            res.number(f"e9-{key}-k-fixed-unbounded", pct(d["p_k_share_unbounded"]), unit="%", fmt=".0f",
                       label=f"share of draws for {nm} at a = {share:.2f} in which the research input does not grow, so r and K are unbounded (no 95th percentile exists)")
        res.number(f"e9-{key}-k-fixed-above1", pct(d["p_k_share_above_1"]), unit="%", fmt=".1f",
                   label=f"share of draws for {nm} with the fixed-compute loop gain above 1 at a = {share:.2f}")
        res.number(f"e9-{key}-k-spec-max", d["spec_k_max"], fmt=".2f",
                   label=f"loop gain at fixed compute for {nm} at a = {share:.2f}: highest value across all specifications")
        res.number(f"e9-{key}-share-crit", d["critical_share"], fmt=".2f",
                   label=f"compute's share of research input above which the fixed-compute loop gain for {nm} is below 1 (central refit)")
        res.number(f"e9-{key}-share-crit-max", d["spec_crit_max"], fmt=".2f",
                   label=f"the same critical share for {nm}: highest value across all specifications")
        if d["share_where_r_is_1"] is not None:
            res.number(f"e9-{key}-share-r1", d["share_where_r_is_1"], fmt=".2f",
                       label=f"compute's share above which r itself (on the composite input, compute's growth counted) is below 1 for {nm}")
        if d["safe_share_95"] is not None:
            res.number(f"e9-{key}-share-safe", d["safe_share_95"], fmt=".2f",
                       label=f"smallest compute share at which the 95th percentile of the fixed-compute loop gain for {nm} is below 1")
    lm = ai["lm"]
    res.number("e9-lm-k-published-correction", lm["k_published_correction"], fmt=".2f",
               label=f"the published compute correction applied to our labour-only refit for language models, r (1 - a) at a = {share:.2f}, which leaves compute's growth out",
               note="the ledger's corrected median from Ho and Whitfill's r is dyn-r-lm-corrected")
    res.number("e9-lm-gk-crit", lm["gk_critical_at_share"], unit="per year", fmt=".2f",
               label=f"growth of research compute below which the language-model loop at fixed compute is above 1 at a = {share:.2f} (central refit, natural log a year)",
               note="the published correction is the case where compute grew as fast as the labour proxy")

    for key in ("sat", "lp"):
        o = other[key]
        res.number(f"e9-{key}-r-repro", o["repro"], fmt=".2f",
                   label=f"r for {o['name']} recomputed on Erdil et al.'s inputs (naive), against their published naive {o['published_naive']:g}")
        res.number(f"e9-{key}-r-ours", o["r_ours"], fmt=".2f",
                   label=f"r for {o['name']} with today's OpenAlex works counts instead of unique authors (labour only)")

    res.number("e9-openai-gl", firm["g_L"], unit="per year", fmt=".2f",
               label="growth of OpenAI's staff, 2022 to 2025, refitted from Ho and Whitfill's files (natural log a year)")
    res.number("e9-openai-gk", firm["g_K"], unit="per year", fmt=".2f",
               label="growth of OpenAI's estimated compute, 2022 to 2025, refitted from Ho and Whitfill's files (natural log a year)")
    res.number("e9-openai-r-labour", firm["r_labour"], fmt=".2f",
               label="r at OpenAI with staff as the only input (a = 0), efficiency growing 3x a year")
    res.number("e9-openai-r-compute", firm["r_compute"], fmt=".2f",
               label="r at OpenAI with compute as the only input (a = 1)")
    res.number("e9-openai-r", firm["r_share"], fmt=".2f",
               label="r at OpenAI at Ho and Whitfill's central compute share 0.67")
    res.number("e9-openai-r-hi", firm["r_p95"], fmt=".2f",
               label="r at OpenAI, 95th percentile over the efficiency range 2x to 5x a year, the slopes and a share of 0.59 to 0.75")
    res.number("e9-openai-r-above1", pct(firm["p_r_above_1"]), unit="%", fmt=".0f",
               label="share of the OpenAI draws with r above 1")
    res.number("e9-openai-k-fixed", firm["k_share"], fmt=".2f",
               label="loop gain at fixed compute at OpenAI, (1 - a) r at a = 0.67")
    res.number("e9-openai-k-fixed-hi", firm["k_p95"], fmt=".2f",
               label="loop gain at fixed compute at OpenAI, 95th percentile of the same draws")
    res.number("e9-openai-k-fixed-above1", pct(firm["p_k_above_1"]), unit="%", fmt=".1f",
               label="share of the OpenAI draws with the fixed-compute loop gain above 1")
    res.number("e9-openai-share-crit", firm["critical_share"], fmt=".2f",
               label="compute's share of research input above which OpenAI's fixed-compute loop gain is below 1")

    agg = bloom["aggregate"]
    res.number("e9-us-bloom-beta", agg["beta"], fmt=".1f",
               label="Bloom et al.'s b for the US economy, recomputed from their files (lambda = 1)",
               note=f"published {ledger['dyn-bloom-beta-aggregate']:g}")
    res.number("e9-us-bloom-r", agg["r"], fmt=".2f",
               label="r for the US economy implied by that b with lambda = 1")
    res.number("e9-us-r", us["r"], fmt=".3f",
               label="r for the US economy with lambda free, best fit of our one-step refit of Erdil et al.'s TFP series; not identified, since lambda cannot be told from 0",
               note="reproduces their best fit; the bootstrap interval runs below 0")
    res.number("e9-us-r-lo", us["r_lo"], fmt=".2f",
               label="r for the US economy, lambda free, 5th percentile of 200 bootstrap refits")
    res.number("e9-us-r-hi", us["r_hi"], fmt=".2f",
               label="r for the US economy, lambda free, 95th percentile of 200 bootstrap refits")
    res.number("e9-us-lambda-not-positive", pct(us["share_lambda_not_positive"]), unit="%", fmt=".0f",
               label="share of bootstrap refits for the US economy with lambda at or below 0 (the input has no effect or a negative one)")
    res.number("e9-us-lr-p", us["lr_p"], fmt=".2f",
               label="p-value of the likelihood-ratio test of lambda against 0 for the US economy")
    res.number("e9-moore-beta", bloom["moore"]["Broad"]["beta"], fmt=".2f",
               label="Bloom et al.'s b for Moore's Law (broad R&D), recomputed from their files (lambda = 1)",
               note=f"published {ledger['dyn-bloom-beta-moore']:g}")
    res.number("e9-moore-r", bloom["moore"]["Broad"]["r"], fmt=".1f",
               label="r for Moore's Law research implied by that b (broad R&D, lambda = 1, output assumed to double every two years)")
    mr = [v["r"] for v in bloom["moore"].values()]
    res.number("e9-moore-r-min", min(mr), fmt=".1f",
               label="r for Moore's Law: lowest across Bloom et al.'s six R&D series")
    res.number("e9-moore-r-max", max(mr), fmt=".1f",
               label="r for Moore's Law: highest across Bloom et al.'s six R&D series")

    res.number("e9-chess-steps", ch["steps"], unit="steps", fmt=",.0f",
               label="Stockfish steps between consecutive Elo measurements in the fit")
    res.number("e9-chess-r", ch["r"], fmt=".2f",
               label="r for Stockfish, test runs as the input, our one-step refit with Student-t noise (close to the authors' stable noise)",
               note="a smooth placebo input with the same growth gives nearly the same r, so the value rests on the two trends")
    res.number("e9-chess-r-lo", ch["r_lo"], fmt=".2f",
               label="r for Stockfish, 5th percentile of 200 bootstrap refits over steps")
    res.number("e9-chess-r-hi", ch["r_hi"], fmt=".2f",
               label="r for Stockfish, 95th percentile of 200 bootstrap refits over steps")
    res.number("e9-chess-r-above1", pct(ch["p_r_above_1"]), unit="%", fmt=".0f",
               label="share of the Stockfish bootstrap refits with r above 1")
    res.number("e9-chess-lr-p", ch["lr_p"], fmt=".2g",
               label="p-value of the likelihood-ratio test of lambda against 0 for Stockfish")
    res.number("e9-chess-placebo-r", ch["placebo"]["r"], fmt=".2f",
               label="r for Stockfish when the input is replaced by a smooth trend growing at the input's own rate (a placebo)")
    res.number("e9-chess-placebo-gain", ch["placebo"]["loglik_gain_of_real_input"], fmt=".1f",
               label="log-likelihood the real test-run input gains over the smooth-trend placebo for Stockfish (1.92 would mark a 95% difference)")
    sub_r = [s["r"] for s in ch["subsets"].values()]
    res.number("e9-chess-r-subset-min", min(sub_r), fmt=".2f",
               label="r for Stockfish: lowest across five subsets of steps (before and after NNUE, halves, largest steps removed)")
    res.number("e9-chess-r-subset-max", max(sub_r), fmt=".2f",
               label="r for Stockfish: highest across the same five subsets")
    sh = ch["share"]
    res.number("e9-chess-share", sh["best"]["share"], fmt=".2f",
               label="CPU-years' share of Stockfish's research input that fits best (test runs the rest), on a grid of 0.05")
    res.number("e9-chess-share-lo", sh["shares_within_95"][0], fmt=".2f",
               label="lowest CPU-years share within the 95% likelihood-ratio region for Stockfish")
    res.number("e9-chess-share-hi", sh["shares_within_95"][1], fmt=".2f",
               label="highest CPU-years share within the 95% likelihood-ratio region for Stockfish")
    res.number("e9-chess-share-span", sh["loglik_span"], fmt=".1f",
               label="spread of the profile log-likelihood across CPU-years shares 0 to 1 for Stockfish (1.92 marks a 95% difference)")
    res.number("e9-chess-share-r-lo", sh["r_within_95"][0], fmt=".2f",
               label="r for Stockfish: lowest across the CPU-years shares within the 95% region")
    res.number("e9-chess-share-r-hi", sh["r_within_95"][1], fmt=".2f",
               label="r for Stockfish: highest across the CPU-years shares within the 95% region")
    res.number("e9-chess-input-corr", sh["corr_monthly_log_inputs"], fmt=".2f",
               label="correlation of Stockfish's monthly log test runs and log CPU-years")

    # ---- Comparison with the published estimates the survey cites -----------------------
    # A recomputation uses the authors' own inputs and method; it reproduces if within 5% (10%
    # for a value published to one digit). A refit uses our inputs or a different noise model;
    # it is judged by whether it falls inside the published interval.
    comp = []

    def recomputed(est, published, ours, how, tol=0.05):
        comp.append({"estimate": est, "kind": "recomputation", "published": published, "ours": ours,
                     "how": how, "gap": ours / published - 1,
                     "verdict": "reproduced" if abs(ours / published - 1) <= tol else "not reproduced"})

    def refit(est, published, interval, ours, ours_interval, how):
        inside = interval[0] <= ours <= interval[1]
        comp.append({"estimate": est, "kind": "refit", "published": published,
                     "published_interval": interval, "ours": ours, "ours_interval": ours_interval,
                     "how": how, "verdict": "inside the published interval" if inside else "outside the published interval"})

    for key in ("cv", "rl", "lm"):
        d = ai[key]
        pub = ledger[f"dyn-r-{key}"]
        lo, hi = ledger[f"dyn-r-{key}-lo"], ledger[f"dyn-r-{key}-hi"]
        recomputed(f"r, {d['name']} (Ho and Whitfill, posterior median)", pub, d["repro"],
                   "their counts and doubling time, output over input growth (their posterior sits on it)")
        refit(f"r, {d['name']} (Ho and Whitfill)", pub, [lo, hi], d["r_labour"],
              [d["r_labour_p05"], d["r_labour_p95"]], "today's OpenAlex flows, fitted slope, labour only")
    posterior_gap = {}
    for key in ("cv", "rl", "sat", "lp"):
        naive = table[f"{key}-naive-2024"]["value"]
        if key in other:
            ours = other[key]["repro"]
        else:
            times, levels, counts_e = literal_block(erdil_code, "categories")[AI[key]["erdil_key"]]
            ours = (math.log(levels[1] / levels[0]) / (times[1] - times[0])) / endpoint_growth(counts_e)
        recomputed(f"r, {key} (Erdil et al. 2024, naive)", naive, ours, "their counts and output trend")
        posterior_gap[key] = {"naive": ours, "posterior_median": table[f"{key}-r-2024"]["value"],
                              "posterior_over_naive": table[f"{key}-r-2024"]["value"] / ours}
    se = ledger["dyn-r-chess-se"]
    refit("r, computer chess (Besiroglu et al.)", ledger["dyn-r-chess"],
          [ledger["dyn-r-chess"] - 1.6448536269514722 * se, ledger["dyn-r-chess"] + 1.6448536269514722 * se],
          ch["r"], [ch["r_lo"], ch["r_hi"]],
          "their data and likelihood with Student-t rather than stable noise; published interval is r +- 1.645 SE")
    recomputed("r, US economy, lambda free (Erdil et al.)", ledger["dyn-r-us-economy"], us["r"],
               "their data and likelihood (Gaussian)")
    recomputed("beta, US economy (Bloom et al.)", ledger["dyn-bloom-beta-aggregate"], agg["beta"],
               "their files and method, lambda = 1")
    recomputed("beta, Moore's Law (Bloom et al.)", ledger["dyn-bloom-beta-moore"],
               bloom["moore"]["Broad"]["beta"], "their files and method, broad R&D, lambda = 1", tol=0.1)
    for k, label in (("gk", "growth of OpenAI's compute"), ("gl", "growth of OpenAI's staff")):
        recomputed(f"{label} (Ho and Whitfill, Appendix C)", firm["published_inputs"][k],
                   firm["g_K"] if k == "gk" else firm["g_L"], "their files, least-squares slope")
    rec = [c for c in comp if c["kind"] == "recomputation"]
    ref = [c for c in comp if c["kind"] == "refit"]
    res.number("e9-recomputed", len(rec), fmt=".0f",
               label="published estimates recomputed on their authors' own inputs and method")
    res.number("e9-reproduced", sum(c["verdict"] == "reproduced" for c in rec), fmt=".0f",
               label="of those, reproduced within 5% (10% for a value published to one digit)")
    res.number("e9-refits", len(ref), fmt=".0f",
               label="published estimates refitted on our inputs or with a different noise model")
    res.number("e9-refits-inside", sum(c["verdict"].startswith("inside") for c in ref), fmt=".0f",
               label="of those, refits whose central value lies inside the published interval")

    res.number = number
    res.detail("unbounded_not_written", unbounded)
    res.detail("ai_domains", ai)
    res.detail("their_inputs_ho_whitfill", hw_inputs)
    res.detail("other_software", other)
    res.detail("frontier_firm_openai", firm)
    res.detail("bloom", bloom)
    res.detail("chess", ch)
    res.detail("us_tfp", us)
    res.detail("comparison", comp)
    res.detail("erdil_posterior_against_naive", posterior_gap)
    res.detail("table_rows", {k: v for k, v in table.items()})
    res.detail("draws", {"steady_state": DRAWS, "bootstrap_refits": BOOT})
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
