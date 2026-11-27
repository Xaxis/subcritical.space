#!/usr/bin/env python3
"""E11: the coupled-gain certificate on Part I's loop graph, and what decides its verdict.

C6 certifies the coupled gain subcritical from entrywise upper bounds U >= |K|: rho(K) <= rho(U) <=
max_i (Uw)_i / w_i <= max row sum (Theorem 6.2 in research/05-formal.md). This experiment builds U on
the loop graph of Part I's dynamical chapter (research/013-dynamical.md, Y1a to Y1e and Y3) and asks
what the certificate says on today's evidence, which entries decide it, and what it would take to
issue it.

The graph. Nodes are the stocks of Part I's loops: software efficiency S (Y1a), compute per dollar H
(Y1b), compute capital C (the economic loop, Y1c) and a deployed model's capability X (Y1d). Each
entry K_ij = lambda_i e_ij / b_i = r_i e_ij, where e_ij is how strongly stock j supplies loop i's
input (Part III's notation). The entries follow from Part I's own equations:
- S row. Y1a's input is (human + AI labour)^(1 - eps_K) * compute^eps_K, with AI labour proportional
  to S times inference compute and a share e_S of labour done by AI (the closure, a gate). So
  K_SS = r_S (1 - eps_K) e_S (Part I's K_S at e_S = 1) and K_SC = r_S (eps_K + (1 - eps_K) e_S), the
  compute-to-software edge. r_S and eps_K come from the ledger.
- H row. AI's share a_H of hardware research, supplied by AI labour that scales with S and C:
  K_HS = K_HC = r_H a_H. r_H is in the ledger; a_H is unmeasured (Part I: no data source).
- C row. Compute capital in H100e grows by spending times compute per dollar, so K_CH = 1 by the
  stock's units; revenue depends on capability, which on a compute-equivalent axis is S times C,
  so K_CS = K_CC = eta, the economic loop's gain eps of Y1c. eta is unmeasured.
- X row. K_XX = K_X, unmeasured. Nothing in Part I's graph flows out of X, so its in-edges cannot
  move rho; only its diagonal can.
The acquisitive loop (Y1e) is left out: its law is linear in the copies, not the common form, so its
R_Q is not an entry of K. Two parties (the United States and China, from the ECI data below) each get
S, C and X; H is global; the cross-party software edges join S_US and S_CN.

Data. (1) The ledger, read by id from data/numbers.json: r for language models, vision and RL at
their median and 95th percentile, the compute share eps_K, hardware r, E4's speedrun r and the
vendor-reported AI-led share of one developer's research. (2) Epoch's ECI scores
(benchmark_data.zip, eci_scores.csv), for the cross-party edge: the frontier ECI growth of each
country's models. In the common form, a loop whose growth is steady satisfies
sum_j K_ij g_j / g_i <= 1 (the exponent of its growth law is constant, and exogenous inputs only
grow), so each cross-party entry is at most the ratio of the two parties' growth rates. That is an
upper bound under three assumptions (the common form, steady growth of the follower, the same
split of capability growth between software and compute in both parties), not a measurement of the
edge. The interval resamples models (which models Epoch scored).

Method. rho(U), the row-sum bound and the Perron-weighted bound at each scenario (software closure
gated, at one developer's vendor-reported AI-led share, or fully closed; r at its median or 95th
percentile); for every unmeasured entry the largest value at which rho(U) stays at or below rho* = 1
(its tolerance, the widest an upper bound on it may be before the verdict flips); the Perron
elasticity of rho to each entry (which entries decide); the smallest set of gates (Parts I and II's:
closure, research compute, money to compute, compute cap, update metering, cross-party transfer)
that issues the certificate with no stated range trusted, and the smallest set of entry cuts on a
grid of the real graph by exhaustive search against cutting greedily (C6(b)); and, for C12, whether
cutting one pathway's loops alone issues it. rho* is undefined (red team C6.2) but is at most 1 for
any margin and drift, so a verdict that fails at 1 fails at every rho*; where it passes, 1 - rho(U)
is the largest m * rho_dot * T_r it tolerates. Entries with no bound are set to a large stand-in, so
any cycle through them must be cut. Theorem 6.2, Lemma 6.1 and Corollary 6.3 are true by
construction and run as assertions that stop the run, as do the identities noted in the code.
Theorem 6.4 is checked on a signed variant of the real graph by integrating its growth laws.

What differs from the spec. E10 has not run, and E11 takes no input from E9 or E6, which ran
after it was built (E9 finds compute's share of research input not identified). The diagonal comes
from the ledger's returns for language models (Part I's choice), with vision and RL as variants (E4
withdrew the speedrun's r as not identified, so it gives the diagonal no value); the
compute edge from Part I's Cobb-Douglas share rather than E10; the capital-to-chips conversion is
taken as 1 by the stock's units (chip sales would fix the price level, not an elasticity); the
cross-party edge is a steady-path bound from Epoch's ECI rather than E6's games. The economic
elasticity has no stated range anywhere in the research, so instead of inventing one the experiment
reports the largest value at which the certificate can issue.

Claims served: C6 (and through it C12).

  .venv/bin/python tools/exp/e11_coupled_loops.py      (CPU, under a minute; see tools/exp/README.md)
"""

from __future__ import annotations

import csv
import io
import itertools
import json
import math
import sys
import zipfile
from datetime import date
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127
BENCH_URL = "https://epoch.ai/data/benchmark_data.zip"
DRAWS = 2000
RHO_STAR = 1.0  # the most lenient admissible threshold: rho* = 1 - m rho_dot T_r <= 1
BIG = 1e6  # stands for an entry with no upper bound at all
TOL = 1e-9
SINCE = date(2024, 1, 1)  # both countries' frontiers are populated by frontier-class models from here
SUBSET_SINCE = (date(2023, 1, 1), date(2025, 1, 1))
T0 = date(2024, 1, 1).toordinal()
US, CN = "United States of America", "China"

LEDGER_IDS = {
    "r_lm": "dyn-r-lm",
    "r_lm_lo": "dyn-r-lm-lo",
    "r_lm_hi": "dyn-r-lm-hi",
    "r_cv_hi": "dyn-r-cv-hi",
    "r_rl_hi": "dyn-r-rl-hi",
    "eps_k": "dyn-research-compute-share",
    "kss_hi": "dyn-r-lm-hi-corrected",
    "closure_max": "formal-software-closure-max",
    "headroom_upper": "dyn-software-headroom-upper",
    "r_h": "dyn-r-moore",
    "r_h_hist": "dyn-r-hardware-hist",
    "e4_collinearity": "e4-sr-collinearity",
    "e4_unbounded": "e4-sr-p-unbounded",
    "vendor_closure": "dyn-anthropic-ai-led",
    "burtsev_rho": "dyn-burtsev-network-rho",
    "open_closed_lag": "dyn-open-closed-lag",
}


# ---------------------------------------------------------------- matrices and the formal statements


def rho(a: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(a)))) if a.size else 0.0


def perron(a: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Spectral radius of a nonnegative matrix with its right and left eigenvectors (nonnegative)."""
    vals, right = np.linalg.eig(a)
    k = int(np.argmax(vals.real))
    vals_l, left = np.linalg.eig(a.T)
    kl = int(np.argmax(vals_l.real))
    v = np.abs(right[:, k].real)
    w = np.abs(left[:, kl].real)
    return float(vals[k].real), v, w


def certify(u: np.ndarray, gen: np.random.Generator) -> dict:
    """rho(U), the row-sum and Perron-weighted bounds, with Theorem 6.2 and Lemma 6.1 asserted.

    The assertions are true by construction (textbook): a failure here is a bug, not a finding."""
    assert (u >= 0).all(), "U must be nonnegative"
    r = rho(u)
    rows = u.sum(axis=1)
    assert r <= rows.max() * (1 + 1e-9) + TOL, ("Lemma 6.1c: rho(U) <= max row sum", u)
    assert r >= u.diagonal().max() * (1 - 1e-9) - TOL, ("Lemma 6.1d: rho(U) >= max diagonal", u)
    for _ in range(3):
        w = np.exp(gen.uniform(-1, 1, len(u)))
        assert r <= ((u @ w) / w).max() * (1 + 1e-9) + TOL, ("Lemma 6.1c: weighted bound", u, w)
        k = gen.uniform(-1, 1, u.shape) * u  # a signed K with |K| <= U
        assert rho(k) <= r * (1 + 1e-9) + TOL, ("Theorem 6.2: rho(K) <= rho(U)", k, u)
    # The weighted bound with a strictly positive near-Perron vector approaches rho(U) from above.
    lam, v, _ = perron(u + 1e-9)
    vw = v + 1e-12
    weighted = float(((u @ vw) / vw).max())
    return {"rho": r, "rowsum": float(rows.max()), "weighted_perron": weighted}


def elasticities(u: np.ndarray) -> np.ndarray:
    """d ln rho / d ln U_ij = U_ij w_i v_j / (rho w.v): the share of rho each entry carries."""
    lam, v, w = perron(u)
    denom = lam * float(w @ v)
    if lam <= 0 or denom <= 0:
        return np.zeros_like(u)
    return u * np.outer(w, v) / denom


# ---------------------------------------------------------------- the graph


def entries_one(p: dict, party: str = "") -> list[dict]:
    """Part I's loop graph for one party: (to, from, name, value, basis, gate, pathway)."""
    s, c, x = f"S{party}", f"C{party}", f"X{party}"
    r_s, eps_k, e_s = p["r_s"], p["eps_k"], p["e_s"]
    return [
        dict(to=s, frm=s, name="the software loop's own gain", value=r_s * (1 - eps_k) * e_s,
             basis="ledger r times (1 - eps_K) times the closure e_S", kind="measured", gate="closure"),
        dict(to=s, frm=c, name="compute to software (experiment compute and research inference)",
             value=r_s * (eps_k + (1 - eps_k) * e_s), basis="ledger r times compute's elasticity in Y1a's input",
             kind="measured", gate="research_compute"),
        dict(to="H", frm=s, name="software to hardware (AI in chip design)", value=p["r_h"] * p["a_h"],
             basis="ledger hardware r times AI's share of hardware research, unmeasured in [0, 1]",
             kind="domain", gate=None),
        dict(to="H", frm=c, name="compute to hardware (AI chip-design labour runs on compute)",
             value=p["r_h"] * p["a_h"], basis="the same share a_H", kind="domain", gate=None),
        dict(to=c, frm="H", name="hardware to compute (compute per dollar)", value=1.0,
             basis="accounting: compute capital in H100e grows one for one with compute per dollar",
             kind="accounting", gate="cap"),
        dict(to=c, frm=s, name="software to economic (revenue's elasticity to capability)", value=p["eta"],
             basis="unmeasured, no bound", kind="unbounded", gate="money"),
        dict(to=c, frm=c, name="the economic loop's own gain (revenue reinvested in compute)", value=p["eta"],
             basis="unmeasured, no bound (Y1c's eps)", kind="unbounded", gate="money"),
        dict(to=x, frm=x, name="the experiential loop's own gain", value=p["k_x"],
             basis="unmeasured, no bound", kind="unbounded", gate="update"),
        dict(to=x, frm=s, name="software to experiential", value=p["x_in"],
             basis="unmeasured; X feeds no other loop, so it cannot move rho", kind="unbounded", gate="update"),
        dict(to=x, frm=c, name="compute to experiential (copies run on compute)", value=p["x_in"],
             basis="unmeasured; as above", kind="unbounded", gate="update"),
    ]


def entries_two(p: dict) -> list[dict]:
    out = entries_one(p, "_US") + entries_one(p, "_CN")
    out.append(dict(to="S_CN", frm="S_US", name="United States software to China's software loop",
                    value=p["x_cn"], basis="steady-path bound from ECI growth rates (an upper bound under assumptions)",
                    kind="eci_bound", gate="cross"))
    out.append(dict(to="S_US", frm="S_CN", name="China's software to the United States software loop",
                    value=p["x_us"], basis="steady-path bound from ECI growth rates (an upper bound under assumptions)",
                    kind="eci_bound", gate="cross"))
    return out


NODES_ONE = ["S", "H", "C", "X"]
NODES_TWO = ["S_US", "C_US", "S_CN", "C_CN", "H", "X_US", "X_CN"]

# Gates from Part I and Part II, each with the entries it zeroes or the parameter it holds.
GATES = {
    "closure": "software closure gate (Part II L3): e_S held at 0",
    "research_compute": "research compute metered and capped: compute no longer feeds software",
    "money": "money to compute (licensed chips, cloud identity checks): revenue no longer buys compute",
    "cap": "compute held capped under licence: the compute stock no longer grows from revenue or hardware",
    "update": "update compute metered (Part II L6): experience no longer turns into weight updates (X's input)",
    "cross": "cross-party transfer gated (teacher-keyed distillation, release control, closed pool)",
}
# Which gates a pathway of the ranking (research/02-pathways.md) acts through.
PATHWAY_GATES = {
    "recursive self-improvement": ["closure"],
    "undeclared and declared compute": ["cap"],
    "distillation from a stronger model": ["cross"],
    "continual learning": ["update"],
    "self-replication and acquisition": [],  # its loop is not in the matrix (not the common form)
    "long-horizon autonomy": [],  # the clock that spaces the gates, not an edge
}


def build(nodes: list[str], ents: list[dict], zero: set[tuple[str, str]] = frozenset()) -> np.ndarray:
    idx = {n: i for i, n in enumerate(nodes)}
    u = np.zeros((len(nodes), len(nodes)))
    for e in ents:
        if (e["to"], e["frm"]) not in zero:
            u[idx[e["to"]], idx[e["frm"]]] += abs(e["value"])
    return u


def apply_gates(p: dict, gates, two: bool) -> tuple[list[dict], set]:
    q = dict(p)
    gates = set(gates)
    if "closure" in gates:
        q["e_s"] = 0.0
    if "cap" in gates:
        gates.add("money")  # a capped stock grows neither from revenue nor from compute per dollar
    ents = entries_two(q) if two else entries_one(q)
    zero = {(e["to"], e["frm"]) for e in ents if e["gate"] in gates and e["gate"] != "closure"}
    return ents, zero


def gate_rho(p: dict, gates, two: bool) -> float:
    ents, zero = apply_gates(p, gates, two)
    return rho(build(NODES_TWO if two else NODES_ONE, ents, zero))


def smallest_gate_sets(p: dict, two: bool) -> tuple[int | None, list[list[str]], float | None]:
    names = sorted(GATES)
    if not two:
        names = [g for g in names if g != "cross"]
    for k in range(len(names) + 1):
        found = [list(c) for c in itertools.combinations(names, k) if gate_rho(p, c, two) <= RHO_STAR + TOL]
        if found:
            return k, found, min(gate_rho(p, c, two) for c in found)
    return None, [], None


def tolerance(make, lo: float, hi: float) -> float | str | None:
    """Largest x in [lo, hi] with rho(make(x)) <= rho*, assuming rho rises with x. None if it fails at
    lo; a note if it never fails within [lo, hi]."""
    if rho(make(lo)) > RHO_STAR + TOL:
        return None
    if rho(make(hi)) <= RHO_STAR + TOL:
        return f"no flip up to {hi:g}"
    a, b = lo, hi
    for _ in range(80):
        m = 0.5 * (a + b)
        if rho(make(m)) <= RHO_STAR + TOL:
            a = m
        else:
            b = m
    return a


def cut_search(u: np.ndarray, candidates: list[tuple[int, int]]) -> tuple[int | None, int | None]:
    """Smallest number of entry cuts reaching rho*, by exhaustive search by size, and by cutting
    greedily (the largest single drop first)."""
    def cut(cs):
        v = u.copy()
        for i, j in cs:
            v[i, j] = 0.0
        return v

    best = None
    for k in range(len(candidates) + 1):
        if any(rho(cut(c)) <= RHO_STAR + TOL for c in itertools.combinations(candidates, k)):
            best = k
            break
    chosen: list[tuple[int, int]] = []
    left = list(candidates)
    while rho(cut(chosen)) > RHO_STAR + TOL and left:
        nxt = min(left, key=lambda c: (rho(cut(chosen + [c])), c))
        chosen.append(nxt)
        left.remove(nxt)
    greedy = len(chosen) if rho(cut(chosen)) <= RHO_STAR + TOL else None
    if best is not None and greedy is not None:
        assert greedy >= best, "the exhaustive search must be at least as good as the greedy one"
    # Corollary 6.3: no cut of off-diagonal entries goes below the largest diagonal entry.
    assert rho(cut(candidates)) >= u.diagonal().max() - TOL, "Corollary 6.3"
    return best, greedy


# ---------------------------------------------------------------- the ECI frontiers


def eci_rows(path: Path) -> list[dict]:
    with zipfile.ZipFile(path) as z, z.open("epoch_capabilities_index/eci_scores.csv") as f:
        raw = list(csv.DictReader(io.TextIOWrapper(f, "utf-8")))
    out = []
    for r in raw:
        if not r["date"] or not r["eci"]:
            continue
        out.append({"model": r["Model"], "date": date.fromisoformat(r["date"]), "eci": float(r["eci"]),
                    "country": r["Country (of organization)"], "access": r["Accessibility group"]})
    return sorted(out, key=lambda r: (r["date"], -r["eci"], r["model"]))


def frontier(rows: list[dict], since: date) -> list[dict]:
    """Models that set a new best ECI for their group, those released on or after `since`."""
    pts, best = [], -math.inf
    for r in rows:
        if r["eci"] > best:
            best = r["eci"]
            if r["date"] >= since:
                pts.append(r)
    return pts


def yr(d: date) -> float:
    return (d.toordinal() - T0) / 365.25


def fit(pts: list[dict]) -> tuple[float, float]:
    """Frontier ECI growth (points a year) and the change a year in that growth (twice the quadratic
    coefficient; positive means accelerating)."""
    t = np.array([yr(r["date"]) for r in pts])
    y = np.array([r["eci"] for r in pts])
    slope = float(np.polyfit(t, y, 1)[0])
    accel = float(2 * np.polyfit(t - t.mean(), y, 2)[0])
    return slope, accel


def lags(lead: list[dict], follow_pts: list[dict]) -> tuple[list[tuple[float, float]], int]:
    """For each frontier point of the follower, months since the leader first reached that ECI."""
    lead_front = frontier(lead, date.min)
    out, ahead = [], 0
    for r in follow_pts:
        first = next((q["date"] for q in lead_front if q["eci"] >= r["eci"]), None)
        if first is None:
            ahead += 1
            continue
        out.append((yr(r["date"]), (r["date"].toordinal() - first.toordinal()) / 30.4375))
    return out, ahead


def theil_sen(xy: list[tuple[float, float]]) -> float:
    s = [(b[1] - a[1]) / (b[0] - a[0]) for a, b in itertools.combinations(xy, 2) if b[0] != a[0]]
    return float(np.median(s)) if s else math.nan


def eci_analysis(rows: list[dict], gen: np.random.Generator) -> dict:
    us = [r for r in rows if r["country"] == US]
    cn = [r for r in rows if r["country"] == CN]

    def one(us_rows, cn_rows, since):
        fu, fc = frontier(us_rows, since), frontier(cn_rows, since)
        if len(fu) < 4 or len(fc) < 4:
            return None
        gu, au = fit(fu)
        gc, ac = fit(fc)
        lg, ahead = lags(us_rows, fc)
        return {"g_us": gu, "g_cn": gc, "accel_us": au, "accel_cn": ac, "ratio": gc / gu,
                "lag_median": float(np.median([m for _, m in lg])) if lg else math.nan,
                "lag_trend": theil_sen(lg), "ahead": ahead, "n_us": len(fu), "n_cn": len(fc),
                "lags": [[round(t + 2024, 3), round(m, 2)] for t, m in lg]}

    point = one(us, cn, SINCE)
    boots = {k: [] for k in ("g_us", "g_cn", "ratio", "accel_us", "accel_cn", "lag_median", "lag_trend")}
    for _ in range(DRAWS):
        bu = [us[i] for i in gen.integers(0, len(us), len(us))]
        bc = [cn[i] for i in gen.integers(0, len(cn), len(cn))]
        o = one(sorted(bu, key=lambda r: (r["date"], -r["eci"], r["model"])),
                sorted(bc, key=lambda r: (r["date"], -r["eci"], r["model"])), SINCE)
        if o is None or o["g_us"] <= 0 or o["g_cn"] <= 0:
            continue
        for k in boots:
            boots[k].append(o[k])
    q = {k: np.array(v) for k, v in boots.items()}
    subsets = {}
    for since in SUBSET_SINCE:
        o = one(us, cn, since)
        subsets[f"countries since {since}"] = {k: o[k] for k in ("g_us", "g_cn", "ratio", "accel_cn", "n_us", "n_cn")}
    closed = [r for r in rows if r["access"] == "Closed weights"]
    opened = [r for r in rows if r["access"] == "Open weights"]
    for since in (SINCE,) + SUBSET_SINCE:
        fo, fl = frontier(closed, since), frontier(opened, since)
        gcl, _ = fit(fo)
        gop, aop = fit(fl)
        subsets[f"open over closed weights since {since}"] = {"g_closed": gcl, "g_open": gop, "ratio": gop / gcl,
                                                              "accel_open": aop, "n_closed": len(fo), "n_open": len(fl)}
    return {"point": point, "boots": q, "kept": int(q["ratio"].size), "subsets": subsets}


# ---------------------------------------------------------------- Theorem 6.4 on a signed variant


def grow(m: np.ndarray, a: np.ndarray, t_end: float) -> tuple[float, float]:
    """Integrate dz/dt = a exp((M - I) z) from z = 0 (b_i = 1, so z = u). Returns (the first time
    some z passes 60, a proxy for finite-time blow-up, or t_end if none does; the largest z reached
    by then)."""
    n = len(m)

    def f(_t, z):
        with np.errstate(over="ignore"):
            return a * np.exp(np.minimum((m - np.eye(n)) @ z, 700.0))

    sol = solve_ivp(f, (0.0, t_end), np.zeros(n), method="RK45", rtol=1e-9, atol=1e-11)
    zmax = sol.y.max(axis=0)
    hit = np.nonzero(zmax > 60.0)[0]
    if hit.size:
        return float(sol.t[hit[0]]), float(zmax[hit[0]])
    return float(sol.t[-1]), float(zmax[-1])


def signed_check(k_sc: float) -> dict:
    """Part I says some couplings may be negative: compute that software research uses is not
    spent on revenue. On the S and C block with the software-to-economic edge negative, rho(K) > 1
    while the positive part K+ has rho < 1: is that a runaway?"""
    eta = 0.5 * (1.0 / k_sc + 1.0)  # midway between rho(K) = 1 and rho(K+) = 1, an illustration
    k = np.array([[0.0, k_sc], [-eta, eta]])
    kplus = np.maximum(k, 0)
    kabs = np.abs(k)
    a = np.ones(2)
    r_k, r_plus, r_abs = rho(k), rho(kplus), rho(kabs)
    assert r_k > 1 > r_plus, "the illustration must sit where rho(K) > 1 > rho(K+)"
    t_end = 1e4
    stop, zmax = grow(k, a, t_end)
    # Theorem 6.4(ii) with a positive M~ >= K+ and rho(M~) < 1: its proof needs only K z <= M~ z for
    # z >= 0, which K+ gives for signed K.
    mt = kplus + 1e-3
    rt, v, _ = perron(mt)
    assert rt < 1
    v = v / v.max()
    aa = (1 - rt) * v.min()
    cc = (a / v).max()
    n_bound = math.log(1 + aa * cc * t_end) / aa
    z_bound = float(n_bound * v.max())
    assert stop >= t_end - 1e-6 and zmax <= z_bound + 1e-6, "comparison with K+ and Theorem 6.4(ii) must bound z"
    # The nonnegative matrix with the same magnitudes runs away no later than Theorem 6.4(i) says.
    stop_abs, _ = grow(kabs, a, 100.0)
    bound_abs = 1.0 / (a.min() * (r_abs - 1))
    assert stop_abs <= bound_abs + 1e-6, "Theorem 6.4(i): blow-up no later than 1 / (a_min (rho - 1))"
    return {"k_sc": k_sc, "eta": eta, "rho_K": r_k, "rho_Kplus": r_plus, "rho_absK": r_abs,
            "signed_max_u_at_1e4": zmax, "comparison_bound_at_1e4": z_bound,
            "abs_blowup_time": stop_abs, "abs_blowup_bound": bound_abs,
            "reading": "rho(K) > 1 with no runaway: for signed K, rho(K) is not the runaway condition. "
                       "Theorem 6.4(ii)'s proof goes through for signed K with M~ >= K+ (z >= 0 gives K z <= K+ z), "
                       "so rho(K+) < 1 rules runaway out; and K+ <= |K| <= U, so the certificate rho(U) < 1 still "
                       "certifies, through K+ rather than through rho(K)."}


# ---------------------------------------------------------------- main


def main() -> int:
    res = Results("E11", "e11_coupled_loops", seed=SEED)
    gen = np.random.default_rng(SEED)
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    L = {k: float(numbers[v]["value"]) for k, v in LEDGER_IDS.items()}
    res.detail("ledger_inputs", {v: L[k] for k, v in LEDGER_IDS.items()})

    # ---- C6(c) as stated, and what it rests on.
    r_hi, eps_k = L["r_lm_hi"], L["eps_k"]
    kss_hi = r_hi * (1 - eps_k)
    assert abs(kss_hi - L["kss_hi"]) < 1e-9 and abs(1 / kss_hi - L["closure_max"]) < 1e-9, "ledger changed shape"
    eps_flip = 1 - 1 / r_hi
    domains = {"language models": L["r_lm_hi"], "computer vision": L["r_cv_hi"], "reinforcement learning": L["r_rl_hi"]}
    closed_gain = {k: v * (1 - eps_k) for k, v in domains.items()}
    above = [k for k, v in closed_gain.items() if v > 1]
    res.detail("c6c", {
        "fully_closed_gain_at_95th": closed_gain,
        "eps_k_flip": eps_flip,
        "eps_k_ledger": eps_k,
        "e4_speedrun": {"collinearity": L["e4_collinearity"], "share_unbounded": L["e4_unbounded"],
                        "reading": "E4 withdrew the speedrun's r as not identified (its stock and research input move "
                                   "together, and placebo inputs give an r of their own), so E4 gives the software "
                                   "diagonal no value"},
        "reading": "Corollary 6.3 holds on the ledger: with the software loop fully closed, rho(U) >= 1.07 whatever the "
                   "cross-feeds. It rests on one domain of three and on an assumed compute share within "
                   f"{eps_flip - eps_k:.3f} of the value at which the diagonal falls to 1.",
    })

    # ---- The one-party graph.
    closures = {"gated": 0.0, "vendor-reported": L["vendor_closure"], "fully closed": 1.0}
    base = dict(r_s=r_hi, eps_k=eps_k, e_s=1.0, r_h=L["r_h"], a_h=0.0, eta=0.0, k_x=0.0, x_in=0.0)
    ents = entries_one(base)
    kinds = [e["kind"] for e in ents]
    n_entries, n_measured = len(ents), kinds.count("measured")
    n_unbounded, n_domain = kinds.count("unbounded"), kinds.count("domain")
    res.detail("graph_one_party", [
        {"edge": f"{e['frm']} to {e['to']}", "name": e["name"], "basis": e["basis"], "kind": e["kind"],
         "gate": GATES.get(e["gate"], "none in Part I or II")} for e in ents])

    # A sink's in-edges cannot move rho (asserted, by giving them a huge value).
    u0 = build(NODES_ONE, entries_one({**base, "e_s": 0.5, "eta": 0.2, "a_h": 0.05, "k_x": 0.3}))
    u1 = build(NODES_ONE, entries_one({**base, "e_s": 0.5, "eta": 0.2, "a_h": 0.05, "k_x": 0.3, "x_in": BIG}))
    assert abs(rho(u0) - rho(u1)) < 1e-9, "X is a sink in Part I's graph: its in-edges cannot move rho"

    # The row-sum certificate's floor: the compute-to-software entry alone, at the gated closure.
    rowsum_floor = r_hi * eps_k
    assert rowsum_floor > 1

    scenarios = {}
    for level, r_s in (("95th percentile", r_hi), ("median", L["r_lm"])):
        for cname, e_s in closures.items():
            p = {**base, "r_s": r_s, "e_s": e_s}
            measured_only = build(NODES_ONE, entries_one(p))
            cert = certify(measured_only, gen)
            tol = {
                "eta (software to economic, and the economic loop's own gain)":
                    tolerance(lambda x: build(NODES_ONE, entries_one({**p, "eta": x})), 0.0, 1.0),
                "a_H (AI's share of hardware research)":
                    tolerance(lambda x: build(NODES_ONE, entries_one({**p, "a_h": x})), 0.0, 1.0),
                "a_H with the economic gain at zero and compute-to-software cut":
                    tolerance(lambda x: build(NODES_ONE, entries_one({**p, "a_h": x}), {("S", "C")}), 0.0, 1.0),
                "K_X (the experiential loop's own gain)":
                    tolerance(lambda x: build(NODES_ONE, entries_one({**p, "k_x": x})), 0.0, 1.0),
                "r (the upper bound on software research returns; other unmeasured entries at zero)":
                    tolerance(lambda x: build(NODES_ONE, entries_one({**p, "r_s": x})), 0.0, 100.0),
            }
            # The frontier between the two unmeasured parameters that decide the verdict.
            front = []
            for a_h in np.linspace(0, 0.2, 11):
                t = tolerance(lambda x: build(NODES_ONE, entries_one({**p, "a_h": float(a_h), "eta": x})), 0.0, 1.0)
                front.append([round(float(a_h), 3), t if not isinstance(t, float) else round(t, 4)])
            # At the boundary on eta, which entries carry rho, and how loose the quick checks are.
            boundary = None
            if isinstance(tol["eta (software to economic, and the economic loop's own gain)"], float):
                eta_b = tol["eta (software to economic, and the economic loop's own gain)"]
                ub = build(NODES_ONE, entries_one({**p, "eta": eta_b}))
                cb = certify(ub, gen)
                el = elasticities(ub)
                idx = {n: i for i, n in enumerate(NODES_ONE)}
                carry = sorted(
                    ({"edge": f"{e['frm']} to {e['to']}", "name": e["name"],
                      "elasticity": round(float(el[idx[e["to"]], idx[e["frm"]]]), 4)}
                     for e in entries_one({**p, "eta": eta_b}) if e["value"] > 0),
                    key=lambda d: -d["elasticity"])
                boundary = {"eta": eta_b, **cb, "rowsum_over_rho": cb["rowsum"] / cb["rho"], "elasticities": carry}
            scenarios[f"r at {level}, closure {cname}"] = {
                "e_s": e_s, "measured_only": cert, "tolerances": tol, "eta_frontier_over_a_h": front,
                "boundary_on_eta": boundary}
    res.detail("scenarios_one_party", scenarios)

    # ---- Greedy against exhaustive cuts of off-diagonal entries (C6(b)), on a grid of the real graph.
    grid = []
    offdiag = None
    for r_s in (L["r_lm"], r_hi):
        for e_s in (0.0, L["vendor_closure"], 0.5, 0.9):
            for a_h in (0.0, 0.05, 0.1, 0.2, 0.5, 1.0):
                for eta in (0.0, 0.2, 0.4, 0.6, 0.8):
                    for k_x in (0.0, 0.5):
                        p = {**base, "r_s": r_s, "e_s": e_s, "a_h": a_h, "eta": eta, "k_x": k_x, "x_in": 0.5}
                        u = build(NODES_ONE, entries_one(p))
                        if offdiag is None:
                            offdiag = [(i, j) for i in range(4) for j in range(4) if i != j]
                        cands = [(i, j) for (i, j) in offdiag if u[i, j] > 0]
                        best, greedy = cut_search(u, cands)
                        grid.append({"r_s": r_s, "e_s": e_s, "a_h": a_h, "eta": eta, "k_x": k_x,
                                     "rho": round(rho(u), 4), "exhaustive": best, "greedy": greedy})
    worse = [g for g in grid if g["greedy"] is not None and g["exhaustive"] is not None and g["greedy"] > g["exhaustive"]]
    needs_cut = [g for g in grid if g["exhaustive"]]
    res.detail("cuts_grid", {
        "note": "a sweep, not a distribution: eta and K_X below 1 (above 1 no off-diagonal cut helps, Corollary 6.3), "
                "a_H over its domain, sink in-edges at 0.5 (they cannot matter)",
        "scenarios": len(grid), "needing_a_cut": len(needs_cut), "greedy_worse": len(worse),
        "greedy_worse_cases": worse[:20],
        "max_exhaustive": max((g["exhaustive"] or 0) for g in grid)})

    # ---- Cross-party bounds from the ECI frontiers.
    bench = fetch(BENCH_URL, "epoch/benchmark_data.zip", res, what="Epoch AI, benchmark data with the Epoch Capabilities Index")
    rows = eci_rows(bench)
    eci = eci_analysis(rows, gen)
    pt, bt = eci["point"], eci["boots"]
    pc = lambda k, q: float(np.percentile(bt[k], q))  # noqa: E731
    ratio_hi, ratio_lo = pc("ratio", 95), pc("ratio", 5)
    x_cn, x_us = ratio_hi, 1.0 / ratio_lo
    # By construction the two bounds are reciprocal ratios, so the two-party cycle at the bounds has a
    # geometric mean of at least 1 (exactly 1 at the point estimates): an assertion, not a result.
    cycle_at_bounds = math.sqrt(x_cn * x_us)
    assert cycle_at_bounds >= 1 - 1e-12
    cn_steady = pc("accel_cn", 2.5) <= 0 <= pc("accel_cn", 97.5)
    res.detail("eci", {
        "point": pt,
        "intervals": {k: {"p2.5": pc(k, 2.5), "p5": pc(k, 5), "p50": pc(k, 50), "p95": pc(k, 95), "p97.5": pc(k, 97.5)}
                      for k in bt},
        "kept_draws": eci["kept"], "draws": DRAWS,
        "subsets": eci["subsets"],
        "cn_growth_steady": cn_steady,
        "selection": "only public models Epoch has scored; internal frontier models are unseen, so the true lag behind "
                     "the leader's best is longer than measured; growth rates are unaffected if that internal lead is "
                     "constant",
        "two_party_cycle_at_bounds": cycle_at_bounds,
        "reading": "each cross-party entry is bounded by a ratio of growth rates, and the two ratios are reciprocal, so "
                   "the two bounds multiply to 1 (to the square of their interval at the 95th percentiles): bounds of this "
                   "kind alone can never certify the two-party cycle; one direction must be gated or measured below its bound",
    })

    # ---- Two parties: smallest gate sets, with honest bounds on every entry.
    honest = {**base, "r_s": r_hi, "a_h": 1.0, "eta": BIG, "k_x": BIG, "x_in": BIG, "x_cn": x_cn, "x_us": x_us}
    gates_out = {}
    for cname, e_s in closures.items():
        for two in (False, True):
            p = {**honest, "e_s": e_s}
            k, sets, r_after = smallest_gate_sets(p, two)
            gates_out[f"{'two parties' if two else 'one party'}, closure {cname}"] = {
                "smallest": k, "sets": sets, "rho_after": r_after,
                "margin_for_m_rho_dot_T_r": None if r_after is None else RHO_STAR - r_after}
    # The row-sum certificate under the same gates: the smallest largest-row-sum any gate set reaches.
    rowsum_gates = {}
    for two in (False, True):
        names = sorted(g for g in GATES if two or g != "cross")
        best = None
        for k in range(len(names) + 1):
            for c in itertools.combinations(names, k):
                ents_g, zero = apply_gates({**honest, "e_s": L["vendor_closure"]}, c, two)
                rs = float(build(NODES_TWO if two else NODES_ONE, ents_g, zero).sum(axis=1).max())
                if best is None or rs < best[0] - 1e-12:
                    best = (rs, list(c))
        rowsum_gates["two parties" if two else "one party"] = {"smallest_max_row_sum": best[0], "gates": best[1]}
    rowsum_honest_min = rowsum_gates["one party"]["smallest_max_row_sum"]
    assert rowsum_honest_min > RHO_STAR, "with AI's share of hardware research at its bound, no gate set issues the row-sum test"
    # What the row-sum test would need: AI's share of hardware research low enough with every gate on
    # except the closure, which is the scenario.
    best_gates = [g for g in GATES if g not in ("closure", "cross")]

    def rowsum_at(a_h: float) -> np.ndarray:
        ents_g, zero = apply_gates({**honest, "e_s": L["vendor_closure"], "a_h": a_h}, best_gates, False)
        u = build(NODES_ONE, ents_g, zero)
        return np.diag(u.sum(axis=1))  # rho of this diagonal matrix is the largest row sum

    ah_rowsum = tolerance(rowsum_at, 0.0, 1.0)
    assert isinstance(ah_rowsum, float)
    rho_after_cap = [gate_rho({**honest, "e_s": L["vendor_closure"], "a_h": a}, ["cap", "update"], False)
                     for a in (0.0, 0.5, 1.0)]
    assert max(rho_after_cap) - min(rho_after_cap) < 1e-9, "after the cap, hardware feeds no loop"
    res.detail("gates", {"gates": GATES, "honest_bounds": "a_H at 1, eta, K_X and sink in-edges unbounded, cross-party "
                         "entries at their 95th percentile steady-path bounds", "smallest_sets": gates_out,
                         "row_sum_test_under_every_gate_set": rowsum_gates,
                         "row_sum_test_largest_a_h": ah_rowsum,
                         "reading": "rho(U) issues once the compute stock is capped and the experiential loop held open "
                                    "(plus the cross-party gate for two parties); the row-sum test never does, because the "
                                    "hardware row (AI's share of chip-design research times hardware r, from two stocks) "
                                    "has no gate in Part I or II, although after the cap hardware feeds no loop"})

    # How far below its steady-path bound the edge into China's loop must be shown, if the reverse edge
    # stays at its bound, the compute stocks are capped and the experiential loops held open.
    def two_party_cut(x: float, e_s: float) -> np.ndarray:
        ents_g, zero = apply_gates({**honest, "e_s": e_s, "x_cn": x}, ["cap", "update"], True)
        return build(NODES_TWO, ents_g, zero)

    xp_max = {c: tolerance(lambda x, e=e_s: two_party_cut(x, e), 0.0, 10.0) for c, e_s in closures.items()}
    res.detail("cross_party_tolerance", {
        "note": "largest bound on the entry into China's software loop that issues the certificate, with the entry "
                "into the United States loop at its 95th percentile steady-path bound, compute capped and the "
                "experiential loops held open",
        "by_closure": xp_max, "x_us_bound": x_us, "x_cn_bound": x_cn})
    assert isinstance(xp_max["vendor-reported"], float)

    # ---- Pathways: does cutting one pathway's loops alone issue the certificate (C12's necessity, first half)?
    path_out = {}
    for label, p in (("entries without a data bound at zero", {**base, "r_s": r_hi, "e_s": 1.0, "x_cn": x_cn, "x_us": x_us}),
                     ("honest bounds", {**honest, "e_s": 1.0})):
        for two in (False, True):
            alone = {}
            for pw, gs in PATHWAY_GATES.items():
                g = [x for x in gs if two or x != "cross"]
                alone[pw] = {"rho_after": gate_rho(p, g, two), "issues": gate_rho(p, g, two) <= RHO_STAR + TOL}
            path_out[f"{label}, {'two parties' if two else 'one party'}"] = alone
    res.detail("pathways_alone_fully_closed", path_out)

    # ---- Theorem 6.4 and the signed case, on the S and C block at the gated closure.
    signed = signed_check(r_hi * eps_k)
    res.detail("signed_case", signed)

    # ---------------------------------------------------------------- numbers for the ledger
    sc_hi = scenarios["r at 95th percentile, closure gated"]
    sc_med = scenarios["r at median, closure gated"]
    sc_ven = scenarios["r at 95th percentile, closure vendor-reported"]
    eta_key = "eta (software to economic, and the economic loop's own gain)"
    ah_key = "a_H (AI's share of hardware research)"
    g1v = gates_out["one party, closure vendor-reported"]
    g2v = gates_out["two parties, closure vendor-reported"]
    g1f = gates_out["one party, closure fully closed"]

    for sc in (sc_hi, sc_med, sc_ven):
        assert isinstance(sc["tolerances"][eta_key], float) and isinstance(sc["tolerances"][ah_key], float)
    res.number("e11-epsk-flip", eps_flip, fmt=".3f",
               label="compute share of research input at which the fully closed software loop's gain, at r's 95th "
                     "percentile, falls to 1 (C6(c)'s negative result holds only below it)",
               note="the ledger's share is an assumption of Ho and Whitfill, not a measurement")
    res.number("e11-epsk-gap", eps_flip - eps_k, fmt=".3f",
               label="how far the assumed compute share sits below that flip point")
    res.number("e11-domains-closed-above-1", len(above), unit="domains", fmt=",.0f",
               label="of the ledger's three domains (language models, vision, RL), those whose fully closed, corrected "
                     "gain at the 95th percentile exceeds 1")
    res.number("e11-entries", n_entries, unit="entries", fmt=",.0f",
               label="nonzero entries in Part I's one-party loop graph (software, hardware, compute, experiential)")
    res.number("e11-entries-measured", n_measured, unit="entries", fmt=",.0f",
               label="of those, entries bounded by a measured percentile (each times an assumed compute share)")
    res.number("e11-entries-domain", n_domain, unit="entries", fmt=",.0f",
               label="entries bounded only by the natural range of an unmeasured share (AI's share of hardware research)")
    res.number("e11-entries-unbounded", n_unbounded, unit="entries", fmt=",.0f",
               label="entries with no bound of any kind (economic gain, software to economic, experiential, and two "
                     "edges into the experiential loop that cannot move rho)")
    res.number("e11-rowsum-floor", rowsum_floor, fmt=".2f",
               label="smallest largest-row-sum any U on Part I's graph can have while compute feeds software (r at "
                     "the 95th percentile, closure gated): the row-sum certificate cannot issue")
    res.number("e11-eta-max-gated", sc_hi["tolerances"][eta_key], fmt=".2f",
               label="largest economic gain (revenue's elasticity to effective compute) at which rho(U) <= 1: closure "
                     "gated, r at the 95th percentile, other unmeasured entries at zero (an upper bound on what any "
                     "certificate allows)")
    res.number("e11-eta-max-gated-median", sc_med["tolerances"][eta_key], fmt=".2f",
               label="the same largest economic gain with r at its median")
    res.number("e11-eta-max-vendor", sc_ven["tolerances"][eta_key], fmt=".2f",
               label="the same at the vendor-reported AI-led share of research as the closure, r at the 95th percentile")
    res.number("e11-ah-max-gated", sc_hi["tolerances"][ah_key], fmt=".3f",
               label="largest AI share of hardware research at which rho(U) <= 1: closure gated, r at the 95th "
                     "percentile, economic gain at zero",
               note="one over hardware r would allow 0.2; the cycle through compute and software lowers it")
    res.number("e11-ah-max-rowsum", ah_rowsum, fmt=".2f",
               label="largest AI share of hardware research at which the row-sum test could issue with every gate on "
                     "(one party, vendor-reported closure); rho(U) after the compute cap needs no bound on it",
               note=f"with that share at its bound of 1 no set of gates brings the largest row sum below "
                    f"{rowsum_honest_min:.0f}: the hardware row has no gate in Part I or II")
    b = sc_hi["boundary_on_eta"]
    cyc = sum(e["elasticity"] for e in b["elasticities"] if e["edge"] in ("C to S", "S to C"))
    res.number("e11-sens-cycle", cyc, fmt=".2f",
               label="share of rho(U) carried by the cycle from compute to software and back through revenue, where "
                     "rho(U) = 1 on the economic gain (closure gated, r at the 95th percentile; Perron elasticities)",
               note=f"the largest row sum there is {b['rowsum']:.2f}; the Perron-weighted bound is "
                    f"{b['weighted_perron']:.3f}, rho itself")
    res.number("e11-greedy-worse", len(worse), unit="scenarios", fmt=",.0f",
               label=f"grid scenarios of the real graph (of {len(grid)}) in which cutting greedily needs more cuts than "
                     "the smallest set")
    assert g1f["smallest"] is not None and g1v["smallest"] is not None and g2v["smallest"] is not None
    res.number("e11-gates-fully-closed", g1f["smallest"], unit="gates", fmt=",.0f",
               label="fewest gates that issue the certificate for one party with no stated range trusted, software "
                     "loop fully closed (the closure gate is among them)")
    res.number("e11-gates-vendor", g1v["smallest"], unit="gates", fmt=",.0f",
               label="fewest gates that issue it for one party at the vendor-reported closure, no stated range trusted: "
                     + "; ".join(" and ".join(s) for s in g1v["sets"]))
    res.number("e11-gates-vendor-two", g2v["smallest"], unit="gates", fmt=",.0f",
               label="the same for two parties joined by cross-party software edges: "
                     + "; ".join(" and ".join(s) for s in g2v["sets"]))
    res.number("e11-margin-vendor", g1v["margin_for_m_rho_dot_T_r"], fmt=".2f",
               label="1 - rho(U) after those gates at the vendor-reported closure: the largest m * rho_dot * T_r the "
                     "certificate tolerates (rho_dot is unmeasured)")
    n_alone_zero = sum(v["issues"] for v in path_out["entries without a data bound at zero, one party"].values())
    n_alone_honest = sum(v["issues"] for v in path_out["honest bounds, one party"].values())
    res.number("e11-pathways-alone-zero", n_alone_zero, unit="pathways", fmt=",.0f",
               label="pathways whose loops, cut alone, issue the certificate for one party fully closed, with entries "
                     "that have no data bound set to zero (recursive self-improvement only, if 1)")
    res.number("e11-pathways-alone-honest", n_alone_honest, unit="pathways", fmt=",.0f",
               label="the same with honest bounds on every entry")
    res.number("e11-g-us", pt["g_us"], unit="ECI points a year", fmt=".1f",
               label=f"frontier ECI growth of United States models, released {SINCE.year} on")
    res.number("e11-g-cn", pt["g_cn"], unit="ECI points a year", fmt=".1f",
               label=f"frontier ECI growth of Chinese models, released {SINCE.year} on")
    res.number("e11-g-ratio", pt["ratio"], fmt=".2f",
               label="China's frontier growth over the United States': the steady-path bound on the cross-party "
                     "entry into China's software loop (under three assumptions)")
    res.number("e11-g-ratio-lo", ratio_lo, fmt=".2f",
               label="that ratio, 5th percentile of resampling models")
    res.number("e11-g-ratio-hi", ratio_hi, fmt=".2f",
               label="that ratio, 95th percentile of resampling models (the bound used in U)")
    sub_ratios = [v["ratio"] for v in eci["subsets"].values()]
    res.number("e11-g-ratio-subset-min", min(sub_ratios), fmt=".2f",
               label="lowest follower-over-leader growth ratio across the other windows and the open-over-closed split")
    res.number("e11-g-ratio-subset-max", max(sub_ratios), fmt=".2f",
               label="highest follower-over-leader growth ratio across the other windows and the open-over-closed split")
    res.number("e11-cn-accel", pt["accel_cn"], unit="ECI points a year per year", fmt=".1f",
               label="change a year in China's frontier ECI growth (positive means accelerating, which voids the "
                     "steady-path bound)")
    res.number("e11-cn-accel-lo", pc("accel_cn", 2.5), unit="ECI points a year per year", fmt=".1f",
               label="that change, 2.5th percentile of resampling models")
    res.number("e11-cn-accel-hi", pc("accel_cn", 97.5), unit="ECI points a year per year", fmt=".1f",
               label="that change, 97.5th percentile of resampling models")
    res.number("e11-lag-median", pt["lag_median"], unit="months", fmt=".1f",
               label="median lag of China's frontier models behind the date the United States frontier first reached "
                     "the same ECI")
    res.number("e11-lag-trend", pt["lag_trend"], unit="months a year", fmt=".1f",
               label="trend of that lag (Theil-Sen slope; positive means widening)")
    res.number("e11-lag-trend-lo", pc("lag_trend", 2.5), unit="months a year", fmt=".1f",
               label="lag trend, 2.5th percentile of resampling models")
    res.number("e11-lag-trend-hi", pc("lag_trend", 97.5), unit="months a year", fmt=".1f",
               label="lag trend, 97.5th percentile of resampling models")
    since25 = eci["subsets"][f"countries since {SUBSET_SINCE[1]}"]
    res.number("e11-xp-max-vendor", xp_max["vendor-reported"], fmt=".2f",
               label="largest bound on the cross-party entry into China's software loop that issues the certificate "
                     "at the vendor-reported closure, with the reverse entry at its bound and compute capped",
               note=f"against its own steady-path bound of {x_cn:.2f}: one direction must be gated or measured well "
                    "below what growth rates allow")
    res.number("e11-cn-accel-2025", since25["accel_cn"], unit="ECI points a year per year", fmt=".1f",
               label=f"the same change for China's models released {SUBSET_SINCE[1].year} on, point estimate (the window "
                     "with the lowest ratio, in which the steady-path bound does not hold)")
    res.number("e11-signed-rho", signed["rho_K"], fmt=".2f",
               label="rho(K) of a signed variant of the real graph (software competing with revenue for compute) "
                     "that does not run away: for signed K, rho(K) > 1 is not the runaway condition",
               note=f"its positive part has rho {signed['rho_Kplus']:.2f}; integrated to t = 10,000 it grows as a "
                    "logarithm, inside the comparison bound")
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
