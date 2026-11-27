#!/usr/bin/env python3
"""E6: games. The published race and agreement models, reproduced from their own equations and
parameters, then with a verification regime added, and C7's coalition game in repeated and staged
form.

What it measures. Part I (O2) and C7 lean on six published models. Each is rebuilt here from the
paper's stated model and parameters, and every published number or claim the model can produce is
checked against the paper:

  Armstrong, Bostrom and Shulman: n teams race; capability uniform on [0, mu]; the highest capability
    net of safety wins; enmity e. Closed forms in three information scenarios, a numerical
    best-response check of each equilibrium, and the paper's eight qualitative statements.
  Emery-Xu, Park and Trager: the same race with a logistic contest of decisiveness m. Equilibria are
    solved numerically (damped best responses on a type grid with a golden-section search) for no,
    private and public information, compared with Proposition 1, Proposition 2, Corollary 2.1,
    equation (2) and Figure 2's crossing of public and private risk.
  Fudenberg and Koh: pacing against racing in continuous time; the effective hazard, the payoffs of
    Fig. 4, Theorem 1's regions and Proposition 4's lag L*.
  Gan: the costed-monitoring agreement game; its payoffs, xi, the critical window, Table 3 and the
    last supportable review dates of Table 2 (from the paper's own catch-up path in Table 3, which
    this script does not re-derive from the paper's takeoff model).
  Nordhaus: identical countries, quadratic and other cost exponents; which coalition sizes are
    stable without and with a penalty on non-members.
  Barrett and Dannenberg: the threshold game with the experiment's parameters; its symmetric
    equilibria with a known and an uncertain threshold, against what the groups did.

Then the regime. The static races have no clock, so the detection rate and response time enter
through S = exp(-Lambda (T_b - T_resp)) (C1's Lemma 1.1), the chance a breakout is not halted, with a
penalty on a halted winner. They are run on Emery-Xu et al.'s race, whose m -> infinity limit is
Armstrong et al.'s, under four information regimes: none, private, public capability, and public
compliance only (each party's capability is private, and a public bit says whether each is below a
line L). Fudenberg and Koh's lag becomes a random detection time plus a response time, and a halt
that removes the deviator's lead. Gan's window is read at E5's historical discovery rate.

C7. Theorem 7.2 as corrected (research/05-formal.md, C7): no deviation is self-enforcing for any
share with T_b(s) >= T_r, given (i) R_i > beta V_i with two or more members, or (ii)
beta V_i <= (1 - beta) P_i. The script maps where (i) and (ii) hold over the payoff space and places
every sourced payoff calibration in it; the payoffs of real parties are not measured, and the share
of them inside the region is reported as not identified. It then tests the two ways C7 says it
could be refuted: repeated play (Theorem E.1's setting, with caught members expelled or
re-admitted) and staged accumulation (holdings and algorithms growing between declarations, at
the ledger's rates, against Propositions 1.6 and 7.1). It reports s* over the breakout budget,
including the hardwired-pause paper's own range of budgets (an uncertain line, as in Barrett and
Dannenberg), withdrawal with notice and an asset freeze, and cross-party transfer as an edge.

Data: the papers are fetched into tools/exp/cache/games/ and their checksums recorded; each
parameter and published value used is a row of tools/exp/data/e06_games.csv with its source and
page. Ledger inputs are read from data/numbers.json by id. Randomness (the random instances that
check the repeated game's conditions) comes from one numpy generator seeded with SEED.

Claims served: C7 (directly), C1 (repeated attempts, staged accumulation, response), C6 (the
transfer edge), and Part I's O2 candidate that compliance-only disclosure does not raise risk.

  ~/.claude/claude-core/bin/heavy .venv/bin/python tools/exp/e06_games.py   (CPU, a few minutes)
"""

from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import integrate, optimize
from scipy.special import expit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261127
TABLE = Path(__file__).resolve().parent / "data" / "e06_games.csv"
YEAR_DAYS = 365.25

PAPERS = {
    "armstrong2016racing": ("https://www.futureofhumanityinstitute.org/s/2013-1.pdf",
                            "games/armstrong2013racing.pdf",
                            "Armstrong, Bostrom and Shulman, FHI Technical Report 2013-1"),
    "emeryxu2024uncertainty": ("https://ora.ox.ac.uk/objects/uuid:08871414-bf9a-42f5-ac13-4936e1d63dc8/files/r1z40kv21p",
                               "games/emeryxu2024uncertainty.pdf",
                               "Emery-Xu, Park and Trager, published version (Oxford repository)"),
    "fudenberg2026cooperating": ("https://economics.mit.edu/sites/default/files/inline-files/Pacing.pdf",
                                 "games/fudenberg2026pacing.pdf", "Fudenberg and Koh, working paper"),
    "gan2026clock": ("https://arxiv.org/pdf/2611.04272", "games/gan2026clock.pdf", "Gan, arXiv 2611.04272v1"),
    "nordhaus2015climate": ("https://ycsg.yale.edu/sites/default/files/files/nordhaus-climate-clubs.pdf",
                            "games/nordhaus2015climate.pdf", "Nordhaus, AER 2015 (Yale copy)"),
    "nordhaus2015climate-appendix": ("https://www.aeaweb.org/aer/app/10504/presidential2015_app.pdf",
                                     "games/nordhaus2015climate-appendix.pdf", "Nordhaus, online appendix"),
    "barrett2012climate": ("https://pmc.ncbi.nlm.nih.gov/articles/PMC3491499/",
                           "games/barrett2012climate-pmc.html", "Barrett and Dannenberg, PNAS 2012 (PMC full text)"),
    "fithian2026hardwired": ("https://hardwired-pause.ai/paper", "games/fithian2026hardwired.html",
                             "Hardwired-pause working paper v1.0.2"),
}

LEDGER_IDS = [
    "def-prevent-beta", "prot-margin", "claim-whole-fleet-horizon", "def-hwp-breakout-budget",
    "prot-tr-declared", "org-dprk-months", "prot-licence-months", "prot-lambda-declared",
    "e24-halt-km-median-years", "e24-halt-share-never", "e5-hazard", "e5-hazard-lo", "e5-hazard-hi",
    "phys-algo-growth", "phys-algo-growth-low", "phys-algo-growth-high", "comp-rosetta-algo",
    "org-hwp-fe", "org-fe-years-of-sales", "def-hwp-global-fleet", "prot-prize-over-penalty",
    "prot-coalition-share-declared",
]


def load_table() -> dict[str, dict[str, dict]]:
    rows: dict[str, dict[str, dict]] = {}
    with TABLE.open() as f:
        for r in csv.DictReader(f):
            for need in ("source", "where"):
                if not r[need].strip():
                    raise SystemExit(f"{r['paper']}/{r['key']}: no {need}")
            r["raw"] = r["value"].strip()
            r["value"] = float(r["value"])
            rows.setdefault(r["paper"], {})[r["key"]] = r
    return rows


def v(tab, paper, key) -> float:
    return tab[paper][key]["value"]


# ---------------------------------------------------------------------------------------------
# Armstrong, Bostrom and Shulman: closed forms (Sec. 2) and checks.

def arm_none(mu, e, n):
    s = np.minimum(1.0, mu / (e * n))
    return 1 - s


def arm_private(mu, e, n):
    a = e * n - e + 1
    mu = np.asarray(mu, float)
    return np.where(mu < a, 1 - n * mu / ((n + 1) * a), a**n / ((n + 1) * np.maximum(mu, 1e-300) ** n))


def arm_public(mu, e, n):
    mu = np.asarray(mu, float)
    hi = (np.maximum(mu - e, 0) ** (n + 1)) / (e * (n + 1) * np.maximum(mu, 1e-300) ** n) - mu / (e * (n + 1)) + 1
    return np.where(mu < e, 1 - mu / (e * (n + 1)), hi)


def arm_public_integral(mu, e, n):
    """The public-information risk by direct integration of the paper's integral (an independent
    check of its closed form): density of the top-two gap is n (mu - D)^(n-1) / mu^n."""
    f = lambda d: max(0.0, 1 - d / e) * n * (mu - d) ** (n - 1) / mu**n  # noqa: E731
    return integrate.quad(f, 0, mu, points=[min(e, mu)], limit=200)[0]


def arm_br_none(mu, e, n, ns=200001):
    """Largest gain a team gets by deviating from s = min(1, mu / (e n)) when every other team plays it.
    Its chance of winning with s' is E[clip((c + s - s') / mu)^(n - 1)] over c ~ U[0, mu], which
    integrates exactly to (min(1, 1 + d)^n - max(0, d)^n) / n + max(0, d) with d = (s - s') / mu."""
    s = min(1.0, mu / (e * n))
    sp = np.linspace(0, 1, ns)

    def u(x):
        d = (s - x) / mu
        win = (np.minimum(1, 1 + d) ** n - np.maximum(0, d) ** n) / n + np.maximum(0, d)
        return win * x + (1 - win) * (1 - e) * s

    return float(u(sp).max() - u(np.array([s]))[0]), float(u(np.array([s]))[0])


def arm_br_private(mu, e, n, nx=300, ny=6000, ns=2001):
    """Largest gain from deviating from s(x) = min(1, x / (e n - e + 1)) against n - 1 teams playing it.
    The winner among the others is the one with the highest capability (k = x - s(x) is increasing)."""
    a = e * n - e + 1
    y = (np.arange(ny) + 0.5) / ny * mu
    sy = np.minimum(1.0, y / a)
    ky = y - sy
    if np.any(np.diff(ky) < -1e-12):
        raise AssertionError("Armstrong private: k(x) is not increasing")
    dens = (n - 1) * y ** (n - 2) / mu ** (n - 1) * (mu / ny)  # density of the others' maximum, times dy
    tail = np.concatenate([np.cumsum((sy * dens)[::-1])[::-1], [0.0]])
    sp = np.linspace(0, 1, ns)
    worst = 0.0
    for x in (np.arange(nx) + 0.5) / nx * mu:
        idx = np.searchsorted(ky, x - sp)  # others' maximum below this index loses to us
        g = (idx / ny) ** (n - 1)
        u = g * sp + (1 - e) * tail[idx]
        s0 = min(1.0, x / a)
        i0 = np.searchsorted(ky, x - s0)
        u0 = (i0 / ny) ** (n - 1) * s0 + (1 - e) * tail[i0]
        worst = max(worst, float(u.max() - u0))
    return worst


def armstrong(tab, res) -> dict:
    n_a, n_b = int(v(tab, "armstrong", "n_fig1a")), int(v(tab, "armstrong", "n_fig1b"))
    e1, e2 = v(tab, "armstrong", "e_fig1"), v(tab, "armstrong", "e_fig2")
    mus = np.linspace(0.02, 6, 300)
    tol = 1e-12
    # The public closed form against its own integral.
    pub_err = max(abs(float(arm_public(m, e, n)) - arm_public_integral(m, e, n))
                  for m in (0.3, 0.9, 1.5, 3.0, 5.0) for e in (e1, e2) for n in (n_a, n_b))
    if pub_err > 1e-8:
        raise AssertionError(f"Armstrong public closed form differs from its integral by {pub_err}")
    claims = []

    def claim(name, where, ok, detail=""):
        claims.append({"claim": name, "where": where, "holds": bool(ok), "detail": detail})

    scen = {"none": arm_none, "private": arm_private, "public": arm_public}
    es = [0.25, 0.5, 0.75, 1.0]
    claim("risk decreases (weakly) in mu in every scenario", "Sec. 3.1",
          all(np.all(np.diff(f(mus, e, n)) <= tol) for f in scen.values() for e in es for n in (2, 3, 4, 5)))
    claim("lower enmity lowers risk in every scenario", "Sec. 3.2",
          all(np.all(f(mus, ea, n) <= f(mus, eb, n) + tol)
              for f in scen.values() for ea, eb in zip(es, es[1:]) for n in (2, 3, 4, 5)))
    claim("no information is always safest", "Sec. 3.3",
          all(np.all(arm_none(mus, e, n) <= np.minimum(arm_private(mus, e, n), arm_public(mus, e, n)) + tol)
              for e in es for n in (2, 3, 4, 5)))
    claim("at enmity 1, private information is safer than public", "Sec. 3.3",
          all(np.all(arm_private(mus, e1, n) <= arm_public(mus, e1, n) + tol) for n in (n_a, n_b)))
    low = mus[mus <= 1.0]
    claim("at low enmity and low mu, public can be safer than private", "Sec. 3.3",
          bool(np.any(arm_public(low, e2, n_a) < arm_private(low, e2, n_a) - 1e-9)))
    big = np.array([20.0, 40.0])
    slope_priv = float((np.diff(np.log(arm_private(big, e1, n_b))) / np.diff(np.log(big)))[0])
    slope_pub = float((np.diff(np.log(arm_public(big, e1, n_b))) / np.diff(np.log(big)))[0])
    claim("asymptotically private risk is of order 1/mu^n and public of order 1/mu", "Sec. 3.3",
          abs(slope_priv + n_b) < 0.05 and abs(slope_pub + 1) < 0.1,
          f"log-log slopes at n = {n_b}: private {slope_priv:.3f}, public {slope_pub:.3f}")
    claim("more teams raise risk with no and with public information", "Sec. 3.4",
          all(np.all(f(mus, e, n) <= f(mus, e, n + 1) + tol)
              for f in (arm_none, arm_public) for e in es for n in (2, 3, 4)))
    d = arm_private(mus, e2, n_b) - arm_private(mus, e2, n_a)
    claim("with private information, more teams are worse at low mu and better at high mu", "Sec. 3.4, Fig. 3",
          bool(np.any(d > 1e-9) and np.any(d < -1e-9) and d[0] >= 0 and d[-1] <= 0))
    held = sum(c["holds"] for c in claims)

    br = []
    for e in (e1, e2):
        for n in (n_a, n_b):
            for mu in (0.5, 1.0, 2.0, 4.0):
                g_none, _ = arm_br_none(mu, e, n)
                g_coarse = arm_br_private(mu, e, n, nx=100, ny=5000, ns=4001)
                g_fine = arm_br_private(mu, e, n, nx=100, ny=20000, ns=4001)
                br.append({"e": e, "n": n, "mu": mu, "gain_none_exact": g_none,
                           "gain_private_grid_5000": g_coarse, "gain_private_grid_20000": g_fine})
    gmax = max(max(r["gain_none_exact"], r["gain_private_grid_20000"]) for r in br)
    if any(r["gain_private_grid_20000"] > r["gain_private_grid_5000"] + 1e-12 for r in br):
        raise AssertionError("Armstrong private: the deviation gain does not fall as the grid is refined")
    res.number("e6-armstrong-claims-held", held, fmt=",.0f",
               label=f"Armstrong et al.'s qualitative statements that hold on their own closed forms (of {len(claims)} tested)")
    res.number("e6-armstrong-br-gain-max", gmax, fmt=".1e",
               label="largest gain any team gets by deviating from Armstrong et al.'s no-information (exact) and private-information (grid of 20000 rival types) equilibria; "
                     "it falls as the grid is refined (both grids in the detail), so it is grid error and the equilibria reproduce")
    return {"claims": claims, "public_closed_form_vs_integral_max_err": pub_err, "best_response_checks": br,
            "note": "The public scenario's equilibrium is a limit (the laggard is indifferent); it is checked through "
                    "Emery-Xu et al.'s logistic contest instead, which nests it as m grows."}


# ---------------------------------------------------------------------------------------------
# Emery-Xu, Park and Trager: a numerical solver for the two-player race with a logistic contest,
# and the regime and information variants built on it.

GR = (math.sqrt(5) - 1) / 2


def race_solve(mu, eta, m, regime, k=60, c=0.0, line=None, iters=800, damp=0.5, tol=1e-7):
    """Symmetric equilibrium of the two-player race. Types x on a midpoint grid of [0, mu]. Player
    payoff (divided by S and with constants dropped): w (s - c) + (1 - w)(1 - eta) s_opp, where w is
    the logistic chance of winning and c = (1 - S) P / S is the regime's halting penalty term.
    Information regimes set what a player conditions on: nothing ('none'), its own type ('private'),
    both types ('public'), or its own type and whether the opponent is below the line ('compliance').
    Returns the strategy matrix s[i, j] (own type i, opponent type j), the disaster risk without the
    regime's factor S, the largest payoff gain any information set has from deviating (so the result is
    an epsilon-equilibrium with that epsilon), and the iterations used."""
    x = (np.arange(k) + 0.5) / k * mu
    xi, yj = x[:, None], x[None, :]
    ii, jj = np.meshgrid(np.arange(k), np.arange(k), indexing="ij")
    if regime == "none":
        sid = np.zeros((k, k), int)
    elif regime == "private":
        sid = ii
    elif regime == "public":
        sid = ii * k + jj
    elif regime == "compliance":
        sid = ii * 2 + (x[jj] > line).astype(int)
    else:
        raise ValueError(regime)
    nset = int(sid.max()) + 1
    flat = sid.ravel()
    cnt = np.bincount(flat, minlength=nset).astype(float)

    def uset(sv, opp):
        sf = sv[sid]
        w = expit(m * (xi - sf - yj + opp))
        u = w * (sf - c) + (1 - w) * (1 - eta) * opp
        return np.bincount(flat, u.ravel(), minlength=nset) / cnt

    def best(opp):
        grid = np.linspace(0, 1, 21)
        vals = np.array([uset(np.full(nset, g), opp) for g in grid])
        kk = vals.argmax(0)
        a, b = grid[np.maximum(kk - 1, 0)], grid[np.minimum(kk + 1, 20)]
        c1, c2 = b - GR * (b - a), a + GR * (b - a)
        f1, f2 = uset(c1, opp), uset(c2, opp)
        for _ in range(32):
            left = f1 > f2
            b, a = np.where(left, c2, b), np.where(left, a, c1)
            c1, c2 = np.where(left, b - GR * (b - a), c2), np.where(left, c1, a + GR * (b - a))
            f1, f2 = uset(c1, opp), uset(c2, opp)
        cand = np.stack([(a + b) / 2, np.zeros(nset), np.ones(nset)])
        fv = np.stack([uset(cd, opp) for cd in cand])
        return cand[fv.argmax(0), np.arange(nset)]

    def gain(sv):  # the most any information set gains by its best response: an epsilon-equilibrium check
        opp = sv[sid].T
        return float(np.max(uset(best(opp), opp) - uset(sv, opp)))

    sv = np.full(nset, 0.5)
    it = 0
    for dmp, n_it in ((damp, iters), (0.9, 3000)):  # heavier damping only where the first pass cycles
        for _ in range(n_it):
            new = dmp * sv + (1 - dmp) * best(sv[sid].T)
            it += 1
            delta = float(np.max(np.abs(new - sv)))
            sv = new
            if delta < tol:
                break
        resid = gain(sv)
        if resid < 1e-6:
            break
    sf = sv[sid]
    opp = sf.T
    w = expit(m * (xi - sf - yj + opp))
    risk = float(np.mean(w * (1 - sf) + (1 - w) * (1 - opp)))
    return sf, risk, resid, it


def ex_F(c, m, mu):
    """CDF of C = X + V_i - V_j, X ~ U[0, mu], the Gumbel difference logistic with scale 1/m."""
    return (np.logaddexp(0, m * c) - np.logaddexp(0, m * (c - mu))) / (m * mu)


def ex_prop2(m, mu, eta, n=4001):
    """Proposition 2's strategy, min{int_{-inf}^x F(c)^eta dc / F(x)^eta, 1}, on a fine grid, and
    Corollary 2.1's risk."""
    lo = -40.0 / m
    c = np.linspace(lo, mu, n)
    fe = ex_F(c, m, mu) ** eta
    cum = integrate.cumulative_trapezoid(fe, c, initial=0.0)
    s = np.minimum(1.0, cum / np.maximum(fe, 1e-300))
    xs = c[c >= 0]
    sx = s[c >= 0]
    risk = 1 - 2 / mu * integrate.trapezoid(sx * ex_F(xs, m, mu), xs)
    return (lambda q: np.interp(q, xs, sx)), float(risk)


def ex_br_gain(sfun, m, mu, eta, k=120, ns=1001):
    """Largest gain any type gets by deviating from the symmetric private strategy sfun."""
    x = (np.arange(k) + 0.5) / k * mu
    sy = sfun(x)
    sp = np.linspace(0, 1, ns)
    worst = 0.0
    for i, xi in enumerate(x):
        w = expit(m * (xi - sp[:, None] - x[None, :] + sy[None, :]))
        u = (w * sp[:, None] + (1 - w) * (1 - eta) * sy[None, :]).mean(1)
        w0 = expit(m * (xi - sy[i] - x + sy))
        u0 = float((w0 * sy[i] + (1 - w0) * (1 - eta) * sy).mean())
        worst = max(worst, float(u.max()) - u0)
    return worst


def crossing(xs, a, b):
    """First x where a - b changes sign from negative to positive (linear interpolation), else None."""
    d = np.asarray(a) - np.asarray(b)
    for i in range(len(d) - 1):
        if d[i] <= 0 < d[i + 1]:
            return float(xs[i] + (xs[i + 1] - xs[i]) * (-d[i]) / (d[i + 1] - d[i]))
    return None


def emery_xu(tab, res) -> dict:
    mu, eta = v(tab, "emeryxu", "mu_fig2"), v(tab, "emeryxu", "eta_fig2")
    ms = [1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20]
    rows = []
    for m in ms:
        _, r_none, res_none, _ = race_solve(mu, eta, m, "none")
        _, r_priv, res_priv, _ = race_solve(mu, eta, m, "private")
        _, r_pub, res_pub, _ = race_solve(mu, eta, m, "public")
        s_cf = min(1.0, mu / (2 * eta * (ex_F(mu, m, mu) - ex_F(0, m, mu))))
        sfun, r_cor = ex_prop2(m, mu, eta)
        rows.append({"m": m, "none_numeric": r_none, "none_prop1": 1 - s_cf, "private_numeric": r_priv,
                     "private_cor21": r_cor, "public_numeric": r_pub,
                     "prop2_br_gain": ex_br_gain(sfun, m, mu, eta) if m in (2, 3, 6, 10, 20) else None,
                     "equilibrium_epsilon": [res_none, res_priv, res_pub]})
    if max(max(r["equilibrium_epsilon"]) for r in rows) > 1e-6:
        raise AssertionError("race solver did not converge")
    none_err = max(abs(r["none_numeric"] - r["none_prop1"]) for r in rows)
    m_arr = np.array(ms, float)
    pub = np.array([r["public_numeric"] for r in rows])
    cor = np.array([r["private_cor21"] for r in rows])
    priv = np.array([r["private_numeric"] for r in rows])
    pos = (pub > 1e-3) | (priv > 1e-3)  # where either regime has a disaster risk worth comparing
    cross_paper = crossing(m_arr, pub, cor)
    cross_eq = crossing(m_arr[pos], pub[pos], priv[pos])
    gap_min = float(np.min((pub - priv)[pos]))
    # Resolution check at m = 6.
    _, r6p, _, _ = race_solve(mu, eta, 6, "private", k=120)
    _, r6u, _, _ = race_solve(mu, eta, 6, "public", k=120)
    # Equation (2) at m -> infinity, where the model is Armstrong et al.'s with n = 2.
    eq2_printed = ((eta + 1) ** 3 + eta**2) / (3 * eta)
    eq2_square = ((eta + 1) ** 2 + eta**2) / (3 * eta)
    mu_cross = optimize.brentq(lambda q: float(arm_public(q, eta, 2) - arm_private(q, eta, 2)), eta + 1e-9, eta + 1 - 1e-9)
    inf_priv, inf_pub = float(arm_private(mu, eta, 2)), float(arm_public(mu, eta, 2))
    gains = [r["prop2_br_gain"] for r in rows if r["prop2_br_gain"] is not None]
    r6 = next(r for r in rows if r["m"] == 6)
    res.number("e6-ex-none-max-diff", none_err, fmt=".1e",
               label="largest difference between Emery-Xu et al.'s Proposition 1 no-information risk and our numerical equilibrium on 60 types, m from 1 to 20 (grid error: it reproduces)")
    res.number("e6-ex-cross-m-paper", cross_paper if cross_paper is not None else float("nan"), fmt=".1f",
               label="decisiveness at which public risk overtakes private risk, with private risk from the paper's own Proposition 2 (the paper says 6)")
    res.number("e6-ex-prop2-br-gain-max", max(gains), fmt=".3f",
               label="largest gain from deviating from Emery-Xu et al.'s Proposition 2 strategy in their own model (m of 2 to 20; 0 would mean it is an equilibrium)")
    res.number("e6-ex-private-risk-paper-m6", r6["private_cor21"], fmt=".2f",
               label="private-information disaster risk at m = 6 from the paper's Corollary 2.1 (Fig. 2 parameters)")
    res.number("e6-ex-private-risk-eq-m6", r6["private_numeric"], fmt=".2f",
               label="private-information disaster risk at m = 6 in the equilibrium we solve (Fig. 2 parameters)")
    res.number("e6-ex-public-risk-m6", r6["public_numeric"], fmt=".2f",
               label="public-information disaster risk at m = 6 in the equilibrium we solve (Fig. 2 parameters)")
    res.number("e6-ex-public-minus-private-min", gap_min, fmt=".3f",
               label="smallest excess of public over private risk across m = 1 to 20 with our private equilibrium (positive: public is riskier at every m where either is risky)")
    res.number("e6-ex-inf-cross-mu", mu_cross, fmt=".3f",
               label="capability range mu at which public and private risk are equal as m grows without bound, at enmity 0.9 (from Armstrong et al.'s closed forms)")
    if cross_paper is None:
        raise AssertionError("no crossing with the paper's private curve: the reproduction failed")
    return {
        "parameters": {"mu": mu, "eta": eta},
        "by_m": rows,
        "crossing_m_with_paper_private": cross_paper,
        "crossing_m_with_equilibrium_private": cross_eq,
        "resolution_check_m6_k120": {"private": r6p, "public": r6u},
        "equation_2": {
            "printed_threshold": eq2_printed, "with_square": eq2_square, "regime_of_square_form": "mu >= eta + 1",
            "mu_where_limits_cross": mu_cross, "limit_private_at_fig2": inf_priv, "limit_public_at_fig2": inf_pub,
            "verdict": "Equation (2) as printed, ((eta + 1)^3 + eta^2) / (3 eta), does not follow from the m -> infinity "
                       "closed forms. Comparing them gives ((eta + 1)^2 + eta^2) / (3 eta) where mu >= eta + 1, and a cubic "
                       "with root near 1.44 for eta = 0.9 where eta <= mu < eta + 1. At Fig. 2's mu = 1.44 the two limits "
                       "agree to within 1e-4.",
        },
        "verdict": ("No information reproduces Proposition 1 and Fig. 2. Public information reproduces Fig. 2's curve. "
                    f"Private information reproduces Fig. 2 only from the paper's Proposition 2 formula (public overtakes it at "
                    f"m = {cross_paper:.1f}), and that strategy is not a best response to itself in the stated model (gain up "
                    f"to {max(gains):.3f}). The equilibrium we solve is "
                    + ("safer than Proposition 2's at every m tested. " if bool(np.all(priv <= cor + 1e-9)) else
                       "not uniformly safer than Proposition 2's. ")
                    + ("With it, public information is riskier than private at every decisiveness tested, so the paper's "
                       "finding that public information is safer at low decisiveness does not reproduce at its own parameters."
                       if gap_min > 0 else
                       f"With it, public is safer than private for some m (crossing at m = {cross_eq})."))
    }


# ---------------------------------------------------------------------------------------------
# Information regimes and the regime's halting, on the logistic race (the O2 test).

def information_regimes(tab, res, beta) -> dict:
    """The calibration grid is ours: it spans the parameters of Emery-Xu et al.'s figures (mu 1 and 1.44,
    enmity 0.9, decisiveness 3 to 20) and adds a wider capability range and a lower enmity."""
    cells = []
    eps_max = 0.0
    for mu in (1.0, 1.44, 3.0):
        for eta in (0.5, 0.9):
            for m in (3, 6, 10, 20):
                base = {}
                for reg in ("none", "private", "public"):
                    _, r, rr, _ = race_solve(mu, eta, m, reg)
                    if rr > 1e-6:
                        raise AssertionError(f"{reg} solve did not converge at mu {mu}, eta {eta}, m {m}")
                    base[reg] = r
                    eps_max = max(eps_max, rr)
                for frac in (0.25, 0.5, 0.75):
                    _, rc, rr, _ = race_solve(mu, eta, m, "compliance", line=frac * mu)
                    if rr > 1e-6:
                        raise AssertionError(f"compliance solve did not converge at mu {mu}, eta {eta}, m {m}, line {frac}")
                    eps_max = max(eps_max, rr)
                    cells.append({"mu": mu, "eta": eta, "m": m, "line_share": frac, "none": base["none"],
                                  "private": base["private"], "public": base["public"], "compliance": rc})
    eps = 1e-6
    n = len(cells)
    over_none = sum(c["compliance"] > c["none"] + eps for c in cells)
    over_priv = sum(c["compliance"] > c["private"] + eps for c in cells)
    over_pub = sum(c["compliance"] > c["public"] + eps for c in cells)
    pub_over_priv = sum(c["public"] > c["private"] + eps for c in {(x["mu"], x["eta"], x["m"]): x for x in cells}.values())
    n_base = len({(x["mu"], x["eta"], x["m"]) for x in cells})
    res.number("e6-o2-cells", n, unit="cells", fmt=",.0f",
               label="calibration cells in the information-regime test (mu, enmity, decisiveness, line position)")
    res.number("e6-o2-compliance-over-none", over_none / n, fmt=".0%",
               label="share of cells where compliance-only disclosure gives a higher disaster risk than no information")
    res.number("e6-o2-compliance-over-private", over_priv / n, fmt=".0%",
               label="share of cells where compliance-only disclosure gives a higher disaster risk than private information alone")
    res.number("e6-o2-compliance-over-public", over_pub / n, fmt=".0%",
               label="share of cells where compliance-only disclosure gives a higher disaster risk than public capability")
    res.number("e6-o2-public-over-private", pub_over_priv / n_base, fmt=".0%",
               label="share of (mu, enmity, decisiveness) cells where public capability is riskier than private information")
    # The regime's halting: a breakout is halted with chance 1 - S; a halted winner pays P. In the
    # no-information case the equilibrium safety rises by (1 - S) P / (S eta), and the disaster risk
    # is S times the risk of the safety chosen. Check the solver reproduces the shift.
    mu, eta, m = v(tab, "emeryxu", "mu_fig2"), v(tab, "emeryxu", "eta_fig2"), v(tab, "emeryxu", "switch_m")
    _, r0, _, _ = race_solve(mu, eta, m, "none")
    s0 = 1 - r0
    halt = []
    for p in (0.0, 0.001, 0.0025, 0.01):
        c = (1 - beta) * p / beta
        sv, r, _, _ = race_solve(mu, eta, m, "none", c=c)
        s_num = float(sv[0, 0])
        s_cf = min(1.0, s0 + c / eta)
        if abs(s_num - s_cf) > 1e-4:
            raise AssertionError(f"halting shift: numeric {s_num} against closed form {s_cf}")
        halt.append({"penalty_over_prize": p, "S": beta, "safety": s_num, "risk_with_regime": beta * r,
                     "risk_without_regime": r0})
    holds = [{"mu": c["mu"], "eta": c["eta"], "m": c["m"], "line_share": c["line_share"]}
             for c in cells if c["compliance"] <= c["none"] + eps]
    summary = {"largest_equilibrium_epsilon": eps_max, "cells": n, "compliance_over_none": over_none / n, "compliance_over_private": over_priv / n,
               "compliance_over_public": over_pub / n, "public_over_private": pub_over_priv / n_base,
               "cells_where_compliance_no_riskier_than_none": holds}
    return {"summary": summary, "cells": cells, "halting_at_the_line_fig2_m6": halt,
            "definition": "compliance-only: each party knows its own capability; a public bit says whether each "
                          "party's capability is below the line L (line_share = L / mu). The O2 candidate survives "
                          "only if compliance-only risk is no higher than no information in every cell.",
            "halting": "With a breakout halted with chance 1 - S and a penalty P on a halted winner, the no-information "
                       "safety rises by (1 - S) P / (S eta) (checked against the solver) and risk is multiplied by S. "
                       "At the line S <= beta, so any penalty above a few thousandths of the prize gives full safety "
                       "in this model; the multiplication by S is true by construction and is not evidence."}


# ---------------------------------------------------------------------------------------------
# Fudenberg and Koh.

def fk_R0(a, b, r, g, kappa, lam0=0.0):
    f = lambda t: math.exp(-(r - a + b) * t - lam0 * t - kappa * (1 - g) * t * t / 2)  # noqa: E731
    return integrate.quad(f, 0, np.inf, limit=200)[0]


def fudenberg(tab, res, beta) -> dict:
    a, b, r = (v(tab, "fudenberg", k) for k in ("alpha", "beta", "r"))
    g2, k2 = v(tab, "fudenberg", "g_fig2"), v(tab, "fudenberg", "kappa_fig2")
    g4, k4 = v(tab, "fudenberg", "g_fig4"), v(tab, "fudenberg", "kappa_fig4")
    R2 = fk_R0(a, b, r, g2, k2)
    leff2 = 1 / R2 - (r - a + b)
    R4 = fk_R0(a, b, r, g4, k4)
    leff4 = 1 / R4 - (r - a + b)
    # Fig. 4(b): the leader on safety paces while the follower races to catch up, then both race.
    a1, a2 = v(tab, "fudenberg", "a1_fig4"), v(tab, "fudenberg", "a2_fig4")
    tc = (a1 - a2) / (1 - g4)
    pace = integrate.quad(lambda t: math.exp(-r * t + (a * g4 - b) * t), 0, tc)[0]
    at_tie = a1 + g4 * tc
    slow = pace + math.exp(-r * tc) * math.exp((a - b) * at_tie - (a * a1 - b * a2)) * R4
    ours = {"leff_fig2": leff2, "upper_fig2": (1 - g2) * a, "leff_fig4": leff4, "race_fig4": R4, "slowdown_fig4": slow}
    repro = {}
    for k, val in ours.items():
        row = tab["fudenberg"][k]
        tol = 0.5 * 10 ** -len(row["raw"].split(".")[-1]) + 1e-12
        repro[k] = {"paper": row["value"], "ours": val, "agrees_to_printed_digits": abs(val - row["value"]) <= tol,
                    "where": row["where"]}

    # Proposition 4 needs a finite hazard ceiling, which linear risk lacks, so L* is computed for the
    # constant-risk analogue at Fig. 4's effective hazard: lambda(D) = lambda0 above safety.
    lam0, g = leff4, g4
    P0 = 1 / (r - g * (a - b))
    k1 = r - a + b * g + lam0  # decay while the rival paces and the deviator races
    k2_ = r - a + b + lam0  # decay once both race
    if abs((b * (1 - g) - k2_) + k1) > 1e-12:
        raise AssertionError("B(L) algebra")
    B = lambda L: 1 / k1 - math.exp(-k1 * L) * (1 / k1 - 1 / k2_)  # noqa: E731
    lower, upper = (1 - g) * (a - b), (1 - g) * a
    if not (lower <= lam0 < upper):
        raise AssertionError("constant-risk analogue is not in Proposition 4(b)")
    ratio = (B(math.inf) - P0) / (B(math.inf) - B(0))
    Lstar = -math.log(ratio) / k1
    # A random detection time D ~ Exp(Lambda) plus a response time: E[B(D + T)] = P0 at
    # Lambda / (Lambda + k1) * exp(-k1 T) = ratio.
    lam_star = ratio * k1 / (1 - ratio)
    # The protocol's halt instead of the rival's racing: at tau the deviator's lead is removed and
    # both pace on safety again.
    k3 = r - (a - b) * g + lam0
    Vh = lambda t: (1 - math.exp(-k1 * t)) / k1 + math.exp(-k3 * t) * P0  # noqa: E731
    tau_h = optimize.brentq(lambda t: Vh(t) - P0, 1e-6, 50)
    # Random detection for the halt variant.
    EVh = lambda lam, T: integrate.quad(lambda d: lam * math.exp(-lam * d) * Vh(d + T), 0, np.inf)[0]  # noqa: E731
    lam_h = optimize.brentq(lambda lam: EVh(lam, 0.0) - P0, 1e-3, 1e2)
    lam_h_cf = k3 * (P0 * k1 - 1) / (1 - P0 * k3)  # E[Vh(D)] = 1 / (Lambda + k1) + Lambda P0 / (Lambda + k3)
    if abs(lam_h - lam_h_cf) > 1e-6 * lam_h_cf:
        raise AssertionError("halt variant: quadrature and closed form disagree")
    regimes = {
        "public capability (lag 0)": {"pacing_sustainable": lam0 >= lower},
        "deployed only (fixed lag L, the paper's Sec. 3.5)": {"pacing_sustainable_iff": f"L <= L* = {Lstar:.4f}"},
        "compliance only (detection at rate Lambda, then response T)": {
            "pacing_sustainable_iff": "Lambda / (Lambda + k1) * exp(-k1 T) >= (B(inf) - P0) / (B(inf) - B(0))",
            "Lambda_needed_at_T0": lam_star, "T_max_at_instant_detection": Lstar},
        "none (never observed)": {"pacing_sustainable": B(math.inf) <= P0},
    }
    res.number("e6-fk-leff-fig2", leff2, fmt=".4f",
               label="Fudenberg and Koh's effective hazard at their Fig. 2 parameters, recomputed (they print 0.2018)")
    res.number("e6-fk-slowdown-fig4", slow, fmt=".4f",
               label="leader's payoff from pacing until catch-up then racing, Fig. 4, recomputed (they print 0.3396)")
    res.number("e6-fk-lstar", Lstar, unit="model time", fmt=".2f",
               label="longest lag before a rival sees a departure that still sustains pacing (Proposition 4's L*), constant-risk analogue of Fig. 4, in the model's time units")
    res.number("e6-fk-lambda-star", lam_star, unit="per model time", fmt=".2f",
               label="detection rate that sustains pacing when a departure is found at a random time and answered at once by racing, same model")
    res.number("e6-fk-halt-tau", tau_h, unit="model time", fmt=".2f",
               label="longest fixed time to a halt that removes the deviator's lead and still sustains pacing, same model (against L* when the answer is racing)")
    return {"reproduction": repro, "constant_risk_analogue": {
        "lambda0": lam0, "g": g, "P0": P0, "B0": B(0), "Binf": B(math.inf), "Lstar": Lstar,
        "rL_star": r * Lstar, "Lambda_star_rival_races": lam_star, "tau_halt": tau_h, "Lambda_star_halt": lam_h,
        "cutoffs": [lower, upper]}, "four_regimes": regimes,
        "units": "The model's time unit is not calibrated to years (r = 3 per unit), so these lags cannot be "
                 "compared with E5's detection or E24's response times: that comparison is not identified.",
        "note": "Linear risk has no hazard ceiling, so Proposition 4 is applied to the constant-risk analogue with "
                "lambda0 equal to Fig. 4's effective hazard; that substitution is ours."}


# ---------------------------------------------------------------------------------------------
# Gan.

def gan(tab, res, L) -> dict:
    p = {k: v(tab, "gan", k) for k in ("Y", "Z", "chi", "p0", "p1", "p2", "c", "d", "eta")}
    C = (1 - p["p0"]) * (p["Y"] + p["chi"] * p["Z"]) - p["d"]
    T = (1 - p["p1"]) * (p["Y"] + p["Z"]) - p["c"]
    R = (1 - p["p2"]) * (p["Y"] + p["chi"] * p["Z"]) - p["c"]
    S = (1 - p["p1"]) * p["Y"] - p["d"]
    xi = math.log((T - R) / (C - R))
    mmax = (C - R) / p["eta"]
    w0 = v(tab, "gan", "window_d0")
    m12 = xi / w0
    crit = xi / mmax
    ours = {"C": C, "T": T, "R": R, "S": S, "gain": C - R, "xi": xi, "m_max": mmax, "m_deter_12": m12,
            "detect_12": 1 - math.exp(-xi), "success_12": math.exp(-xi), "mean_finding_12": 1 / m12,
            "prop3_lhs": (1 - p["p2"]) * p["chi"] * p["Z"], "prop3_rhs": p["c"] - p["d"] + (p["p2"] - p["p1"]) * p["Y"],
            "critical_window": crit}
    dates = [0, 6, 12, 18, 24]
    win = np.array([v(tab, "gan", f"window_d{d}") for d in dates])
    for d, wv in zip(dates, win):
        ours[f"mmin_d{d}"] = xi / wv
        ours[f"net_d{d}"] = C - p["eta"] * xi / wv
    for eta_, ell in ((13.5, 0), (27, 0), (27, 1), (27, 2), (54, 0)):
        ours[f"needed_eta{eta_:g}_l{ell}"] = ell + xi / ((C - R) / eta_)

    def last(needed):  # last date at which the window (Table 3's path, linear between rows) >= needed
        for i in range(len(dates) - 1):
            if win[i] >= needed > win[i + 1]:
                return dates[i] + (dates[i + 1] - dates[i]) * (win[i] - needed) / (win[i] - win[i + 1])
        return None

    for ell in (0, 1, 2):
        ours[f"last_eta27_l{ell}"] = last(ours[f"needed_eta27_l{ell}"])
    rows = []
    for key, r in tab["gan"].items():
        if r["kind"] != "published":
            continue
        pv = r["value"]
        ov = ours.get(key)
        digits = len(r["raw"].split(".")[-1]) if "." in r["raw"] else 0
        if key.startswith(("detect_", "success_")):
            tol = 0.005
        elif key.startswith("mean_finding"):
            tol = 0.5
        elif key.startswith("last_"):
            tol = 0.1
        else:
            tol = 0.5 * 10 ** -max(digits, 0) + 1e-9
        lo = hi = ov
        if key.startswith(("mmin_", "net_")):
            # Table 3 prints the windows to 0.01 months; carry that rounding through.
            wv = v(tab, "gan", "window_d" + key.split("_d")[1])
            f = (lambda q: xi / q) if key.startswith("mmin_") else (lambda q: C - p["eta"] * xi / q)
            lo, hi = sorted((f(wv - 0.005), f(wv + 0.005)))
        ok_row = bool(ov is not None and lo - tol <= pv <= hi + tol)
        rows.append({"key": key, "paper": pv, "ours": ov, "within_rounding": ok_row, "where": r["where"]})
    ok = sum(r["within_rounding"] for r in rows)
    # The window at E5's historical discovery rate. Gan's deterrence asks Lambda w >= xi; prevention asks
    # Lambda w >= ln(1 / beta). With Lambda a year, w is in years.
    beta = L["def-prevent-beta"]
    lam, lam_lo, lam_hi = L["e5-hazard"], L["e5-hazard-lo"], L["e5-hazard-hi"]
    vp = (T - C) / (C - R)
    # Identity: prevention implies Gan's deterrence iff ln(1/beta) >= xi iff V/P <= (1 - beta)/beta.
    if (math.log(1 / beta) >= xi) != (vp <= (1 - beta) / beta):
        raise AssertionError("prevention-deterrence identity")
    res.number("e6-gan-reproduced", ok, fmt=",.0f",
               label=f"Gan's published values reproduced within their printed rounding from his stated primitives (of {len(rows)})")
    res.number("e6-gan-last-review", ours["last_eta27_l0"], unit="months", fmt=".1f",
               label="last supportable review date at Gan's baseline cost, from his Table 3 catch-up path read linearly (he gives 18.9)")
    res.number("e6-gan-deter-window-hist", xi / lam, unit="years", fmt=".1f",
               label="response window Gan's deterrence needs at E5's historical discovery rate, at Gan's illustrative payoffs")
    res.number("e6-gan-deter-window-hist-lo", xi / lam_hi, unit="years", fmt=".1f",
               label="the same window at the 95th percentile of E5's discovery rate (shortest window)")
    res.number("e6-gan-deter-window-hist-hi", xi / lam_lo, unit="years", fmt=".1f",
               label="the same window at the 5th percentile of E5's discovery rate (longest window)")
    res.number("e6-gan-prize-over-penalty", vp, fmt=".2f",
               label="Gan's illustrative payoffs read as C7's prize over penalty: (T - C) / (C - R)")
    return {"published_vs_ours": rows, "ours": ours,
            "regime": {"historical_rate_per_year": lam, "deterrence_window_years": xi / lam,
                       "prevention_window_years": math.log(1 / beta) / lam,
                       "deterrence_window_declared_days": xi / L["prot-lambda-declared"] * YEAR_DAYS,
                       "prevention_over_deterrence": math.log(1 / beta) / xi,
                       "C7_reading": "Gan's breakout gain over cooperation is V = T - C and the loss when caught is "
                                     "P = C - R, so xi = ln(1 + V / P). C7's condition (ii) at pi = beta is "
                                     "ln(1/beta) >= ln(1 + V/P): prevention implies Gan's deterrence exactly when "
                                     "(ii) holds."},
            "not_reproduced": "The follower's catch-up path (Table 3's windows) comes from Gan's takeoff model, which "
                              "this script takes as given. The last-review dates at half and double the cost need "
                              "the path beyond month 24 or before month 0 and are not recomputed."}


# ---------------------------------------------------------------------------------------------
# Nordhaus: identical countries.

def nordhaus(tab, res) -> dict:
    """Welfare of country i: -alpha mu_i^b - g * sum_j (1 - mu_j) (output normalised to 1). A
    coalition of k sets each member's marginal cost to k g, so mu_k = (k g / (b alpha))^(1/(b-1)).
    A coalition is internally stable if no member gains by leaving (the rest re-optimise) and
    externally stable if no outsider gains by joining. Ties count as stable."""
    alpha, g = 1.0, 0.01  # scale-free: the stable sizes do not depend on them (checked below)

    def welfare(k, n, b, alpha=alpha, g=g):
        mu1 = (g / (b * alpha)) ** (1 / (b - 1))
        muk = (k * g / (b * alpha)) ** (1 / (b - 1)) if k > 0 else mu1
        if max(mu1, muk) > 1:
            raise AssertionError("control rate above 1: choose a smaller g")
        emis = k * (1 - muk) + (n - k) * (1 - mu1)
        return -alpha * muk**b - g * emis, -alpha * mu1**b - g * emis  # member, outsider

    def stable(n, b, tol=1e-12, **kw):
        out = []
        for k in range(1, n + 1):
            win_k, wout_km1 = welfare(k, n, b, **kw)[0], welfare(k - 1, n, b, **kw)[1]
            internal = k == 1 or win_k >= wout_km1 - tol * abs(wout_km1)
            external = k == n or welfare(k, n, b, **kw)[1] >= welfare(k + 1, n, b, **kw)[0] - tol * abs(welfare(k + 1, n, b, **kw)[0])
            if internal and external and k >= 2:
                out.append(k)
        return out

    table = {}
    for b in (1.5, 2.0, 2.5, 3.0):
        for n in (10, 15, 50):
            table[f"b={b:g},N={n}"] = stable(n, b)
    if stable(10, 2.0) != stable(10, 2.0, alpha=3.0, g=0.002):
        raise AssertionError("stable sizes depend on the scale")
    s2 = table["b=2,N=10"]
    # Ten countries in pairs (the paper's tie rule takes the smaller size): average carbon price, which
    # is proportional to the marginal cost, over the noncooperative and the efficient one.
    n = 10
    price_pairs_over_nc = 2.0  # each pair's members price at 2 g against g alone
    price_pairs_over_eff = 2.0 / n
    # The penalty on non-members (a share of output) that makes the grand coalition internally stable:
    # the gain from leaving it, in units of a member's abatement cost there.
    pen = {}
    for b in (1.5, 2.0, 2.5):
        for nn in (5, 10, 15, 50):
            win_n = welfare(nn, nn, b)[0]
            wout = welfare(nn - 1, nn, b)[1]
            cost = alpha * ((nn * g / (b * alpha)) ** (1 / (b - 1))) ** b
            pen[f"b={b:g},N={nn}"] = (wout - win_n) / cost
    res.number("e6-nordhaus-stable-min", min(s2), unit="countries", fmt=",.0f",
               label="smallest stable coalition of ten identical countries with quadratic costs and no sanction (Nordhaus gives 2)")
    res.number("e6-nordhaus-stable-max", max(s2), unit="countries", fmt=",.0f",
               label="largest stable coalition of ten identical countries with quadratic costs and no sanction (Nordhaus gives 3)")
    res.number("e6-nordhaus-penalty-n10", pen["b=2,N=10"], fmt=".2f",
               label="penalty on a non-member, in units of a member's abatement cost, that makes the grand coalition of ten identical countries stable (quadratic costs; our extension of Nordhaus's analytic case)")
    return {"stable_sizes": table, "ten_in_pairs": {"price_over_noncooperative": price_pairs_over_nc,
                                                    "price_over_efficient": price_pairs_over_eff},
            "grand_coalition_penalty_in_member_cost_units": pen,
            "verdict": "Reproduces the analytic case: with quadratic costs sizes 2 and 3 are stable (3 with internal "
                       "stability holding as an equality), size 2 above exponent 2 and 3 below, independent of N and of "
                       "scale. The C-DICE results with tariffs need Nordhaus's model and data and are not reproduced.",
            "ai_reading": "For C7 the club penalty is denial of chips, cloud and models to non-members. It must exceed an "
                          "outsider's gain from staying out, and neither the gain nor the cost of denial to a party is "
                          "measured in units that can be compared: the smallest stabilising denial is not identified."}


# ---------------------------------------------------------------------------------------------
# Barrett and Dannenberg.

def barrett(tab) -> dict:
    q = {k: v(tab, "barrett", k) for k in ("N", "cA", "cB", "chipsA", "chipsB", "b", "X", "X_lo", "X_hi", "T", "T_lo", "T_hi")}
    n = int(q["N"])
    na, nb = int(q["chipsA"]), int(q["chipsB"])

    def cost(k):  # a player uses the cheap account first
        return q["cA"] * min(k, na) + q["cB"] * max(k - na, 0)

    def avoid(total, treat):
        if treat in ("certainty", "impact"):
            return 1.0 if total >= q["T"] else 0.0
        return float(np.clip((total - q["T_lo"]) / (q["T_hi"] - q["T_lo"]), 0, 1))

    loss = {"certainty": q["X"], "impact": (q["X_lo"] + q["X_hi"]) / 2, "threshold": q["X"],
            "both": (q["X_lo"] + q["X_hi"]) / 2}

    def pay(own, others, treat):
        tot = own + others
        return -cost(own) + q["b"] * tot - loss[treat] * (1 - avoid(tot, treat))

    out = {}
    for treat in ("certainty", "impact", "threshold", "both"):
        eq = []
        for k in range(na + nb + 1):
            others = (n - 1) * k
            best = max(pay(j, others, treat) for j in range(na + nb + 1))
            if pay(k, others, treat) >= best - 1e-12:
                eq.append(k)
        out[treat] = eq
    obs = {k: r["value"] for k, r in tab["barrett"].items() if r["kind"] == "observed"}
    return {"symmetric_pure_equilibria_chips_each": out, "observed": obs,
            "verdict": "With a known threshold the game has two symmetric equilibria, nothing and 15 chips each (the "
                       "threshold exactly), as the paper states; with a uniform threshold only nothing is an equilibrium. "
                       "The groups matched the first (8 and 10 of 10 avoided catastrophe) and contributed about half the "
                       "threshold under the second, not nothing."}


# ---------------------------------------------------------------------------------------------
# C7: the share over the budget, the uncertain line, staged accumulation.

def c7_share(tab, res, L) -> dict:
    """Prop 7.1's share s* = min(1, h_w / (m T_r)) over the breakout budget, with h_w proportional to the
    budget (the ledger's whole-fleet horizon is at the ledger's budget). C1's Lemma 1.1 gives a breakout
    of length T_b the success chance S = exp(-Lambda (T_b - T_resp)); with the protocol's declared rate
    Lambda = ln(1 / beta) / T_d, S <= beta exactly when T_b >= T_d + T_resp = T_r (checked below)."""
    beta, m = L["def-prevent-beta"], L["prot-margin"]
    hw0, b0 = L["claim-whole-fleet-horizon"], L["def-hwp-breakout-budget"]
    tr = L["prot-tr-declared"]
    td, tresp = L["org-dprk-months"] / 12, L["prot-licence-months"] / 12
    if abs(td + tresp - tr) > 1e-9:
        raise AssertionError("T_r is not T_d plus one licence period")
    lam = L["prot-lambda-declared"]
    if abs(lam * td - math.log(1 / beta)) > 1e-9:
        raise AssertionError("the declared rate is not ln(1 / beta) / T_d")
    b_lo = v(tab, "fithian", "budget_bullish")
    responses = {"illustrative": tresp, "e24_median": L["e24-halt-km-median-years"]}

    def S(tb, tq):
        return math.exp(-lam * (tb - tq)) if tb > tq else 1.0

    def hw(budget):
        return hw0 * budget / b0

    over = [{"budget": float(bg), "h_w_years": hw(bg),
             **{f"s_star_{k}": min(1.0, hw(bg) / (m * (td + tq))) for k, tq in responses.items()}}
            for bg in np.logspace(27, 30, 31)]
    line = {}
    for k, tq in responses.items():
        tr_ = td + tq
        b_bind = b0 * m * tr_ / hw0  # below this budget the line binds (s* < 1)
        # Barrett and Dannenberg's uncertain threshold, here an uncertain budget: the coalition does not
        # know B, uniform (or log-uniform) on the paper's range, and weighs its success over it.
        def exp_pi(s, dist, tq=tq):
            f = lambda bg: S(hw(bg) / s, tq)  # noqa: E731
            if dist == "uniform":
                return integrate.quad(f, b_lo, b0, limit=200)[0] / (b0 - b_lo)
            return integrate.quad(lambda u: f(math.exp(u)), math.log(b_lo), math.log(b0), limit=200)[0] / math.log(b0 / b_lo)

        def largest(dist):
            if exp_pi(1.0, dist) <= beta:
                return 1.0
            return optimize.brentq(lambda s: exp_pi(s, dist) - beta, 1e-3, 1.0)

        s_worst = min(1.0, hw(b_lo) / tr_)
        if s_worst < 1 and abs(S(hw(b_lo) / s_worst, tq) - beta) > 1e-9:
            raise AssertionError("worst-case share does not sit at beta")
        line[k] = {"T_resp_years": tq, "T_r_years": tr_,
                   "share_bullish_with_margin": min(1.0, hw(b_lo) / (m * tr_)),
                   "share_ledger_budget_with_margin": min(1.0, hw0 / (m * tr_)),
                   "budget_below_which_line_binds": b_bind,
                   "share_of_range_binding_uniform": float(np.clip((b_bind - b_lo) / (b0 - b_lo), 0, 1)),
                   "share_of_range_binding_loguniform": float(np.clip(math.log(b_bind / b_lo) / math.log(b0 / b_lo), 0, 1)),
                   "uncertain_budget_no_margin": {"largest_share_worst_case": s_worst,
                                                  "largest_share_expected_uniform": largest("uniform"),
                                                  "largest_share_expected_loguniform": largest("loguniform")}}
    # Staged accumulation between declarations. A coalition passes the line at a declaration with
    # share s0, then buys new chips (all world sales at the 2025 rate: an upper bound for one coalition)
    # while algorithms improve at the annual factor e^a, and launches at the best time t before the
    # next declaration (one licence period later). With algorithms frozen at launch the run takes
    # h e^(-a t) / s(t); with in-run drift it takes ln(1 + a h e^(-a t) / s(t)) / a.
    sales = L["org-hwp-fe"] / L["org-fe-years-of-sales"] / L["def-hwp-global-fleet"]  # share of fleet a year
    dlt = L["prot-licence-months"] / 12
    h = hw(b_lo)
    s_line = min(1.0, h / (m * tr))
    ts = np.linspace(0, dlt, 201)
    stage = {}
    for name, rate in (("central", L["phys-algo-growth"]), ("low (ledger interval)", L["phys-algo-growth-low"]),
                       ("high (ledger interval)", L["phys-algo-growth-high"])):
        a = math.log(rate)
        per = {}
        for mode in ("frozen_at_launch", "in_run_drift"):
            if mode == "frozen_at_launch":
                run = lambda s, t, a=a: h * math.exp(-a * t) / s  # noqa: E731
            else:
                run = lambda s, t, a=a: math.log(1 + a * h * math.exp(-a * t) / s) / a  # noqa: E731

            def pimax(s0, run=run):
                return max(S(run(s0 + sales * t, t), tresp) for t in ts)

            s_st = 1.0 if pimax(1.0) <= beta else optimize.brentq(lambda q: pimax(q) - beta, 1e-4, 1.0, xtol=1e-9)
            phi = rate**dlt  # algorithms over one interval; holdings enter as + sales * dlt
            s16 = s_line / phi - sales * dlt  # Prop 1.6's line: clear s* by the growth before the next check
            per[mode] = {"pi_at_declaration_on_ledger_line": S(run(s_line, 0.0), tresp),
                         "pi_max_on_ledger_line": pimax(s_line),
                         "largest_share_staged_no_margin": s_st,
                         "prop16_share": s16, "pi_max_on_prop16_line": pimax(max(s16, 1e-6))}
        stage[name] = {"annual_factor": rate, "phi_algorithms_per_interval": rate**dlt, **per}
    cen = stage["central"]["in_run_drift"]
    ill = line["illustrative"]
    e24 = line["e24_median"]
    res.number("e6-share-bullish", ill["share_bullish_with_margin"], fmt="%",
               label="largest coalition share (Prop 7.1, margin 2) at the hardwired-pause paper's more bullish budget, 4.3e28 FLOP, fixed algorithms, protocol's illustrative T_r of one year (an illustration: T_r is not bounded)")
    res.number("e6-share-bullish-e24", e24["share_bullish_with_margin"], fmt="%",
               label="the same share with the response time set to E24's median time from a treaty finding to a halt (an illustration; a quarter of findings were never followed by a halt)")
    res.number("e6-budget-binding-share", ill["share_of_range_binding_uniform"], fmt="%",
               label="share of the hardwired-pause paper's own budget range (4.3e28 to 2e29 FLOP, uniform) in which the overt line binds (s* < 1), illustrative T_r")
    res.number("e6-budget-binding-share-e24", e24["share_of_range_binding_uniform"], fmt="%",
               label="the same share of the budget range with the response time set to E24's median time to a halt")
    fro = stage["central"]["frozen_at_launch"]
    res.number("e6-staged-pi-line", fro["pi_max_on_ledger_line"], fmt=".3f",
               label="best per-attempt success of a coalition that passes the margin-2 line at the bullish budget, then grows until the next declaration (all world chip sales, central algorithmic drift) with algorithms fixed at launch; against beta = 0.05")
    res.number("e6-staged-pi-line-inrun", cen["pi_max_on_ledger_line"], fmt=".3f",
               label="the same success if the run also absorbs algorithmic progress while it runs (an upper bound on drift)")
    res.number("e6-staged-share", cen["largest_share_staged_no_margin"], fmt="%",
               label="largest share whose staged success stays at or below beta at every launch time between declarations, with in-run drift (bullish budget, central drift, no margin, illustrative T_r)")
    res.number("e6-staged-share-high", stage["high (ledger interval)"]["in_run_drift"]["largest_share_staged_no_margin"], fmt="%",
               label="the same share at the high end of the ledger's algorithmic drift interval")
    return {"budget_range": [b_lo, b0], "T_d_years": td, "lambda_declared_per_year": lam, "margin": m,
            "over_budget": over, "line": line, "staged": stage, "sales_share_of_fleet_per_year": sales,
            "declaration_interval_years": dlt,
            "caveat": "Every share here uses an illustrative T_r: the protocol's (DPRK detection plus one licence period, "
                      "no decision time) or E24's median time to a halt. C1 has no bounded T_r on E24's record, so these "
                      "show how the line moves with the budget and with staging; they are not shares a regime could adopt."}


# ---------------------------------------------------------------------------------------------
# C7: the payoff map, and repeated play.

def c7_payoffs(res, L, gan_out, fk_out, rng) -> dict:
    beta = L["def-prevent-beta"]
    bound = (1 - beta) / beta
    if abs(bound - L["prot-prize-over-penalty"]) > 1e-9:
        raise AssertionError("the ledger's prize-over-penalty bound is not (1 - beta) / beta")
    fk = fk_out["constant_risk_analogue"]
    g = gan_out["ours"]
    points = [
        {"source": "gan2026clock", "what": "Gan's illustrative payoffs: V = T - C, P = C - R",
         "V_over_P": (g["T"] - g["C"]) / (g["C"] - g["R"])},
        {"source": "fudenberg2026cooperating",
         "what": "constant-risk analogue of Fig. 4: V = B(inf) - P(0), P = P(0) - B(0) (per unit of initial flow)",
         "V_over_P": (fk["Binf"] - fk["P0"]) / (fk["P0"] - fk["B0"])},
    ]
    for pt in points:
        pt["inside_ii"] = bool(pt["V_over_P"] <= bound)
    # Repeated play. Normalise V = 1. pi <= beta per attempt; P, w >= 0; delta in (0, 1).
    #  expelled on capture:    attempt = pi - (1 - pi) P; comply = w / (1 - delta)
    #  re-admitted on capture: attempt forever A = (pi - (1 - pi) P) / (1 - delta (1 - pi))
    # Value iteration of a member's choice on random instances must give max(A, w / (1 - delta)), and
    # comply wherever (ii) holds. Both are identities of the model: assertions, not results.
    n = 2000
    pi = rng.uniform(0, beta, n)
    P, w, dl = rng.uniform(0, 2, n), rng.uniform(0, 0.2, n), rng.uniform(0.3, 0.99, n)
    val = np.zeros(n)
    for _ in range(6000):
        val = np.maximum(w + dl * val, pi + (1 - pi) * (-P + dl * val))
    A = (pi - (1 - pi) * P) / (1 - dl * (1 - pi))
    comply = w / (1 - dl)
    if np.max(np.abs(val - np.maximum(A, comply)) / np.maximum(1, np.abs(val))) > 1e-8:
        raise AssertionError("repeated game: value iteration disagrees with max(A, w / (1 - delta))")
    holds_ii = beta * 1.0 <= (1 - beta) * P
    if np.any(np.abs(val[holds_ii] - comply[holds_ii]) > 1e-8 * np.maximum(1, comply[holds_ii])):
        raise AssertionError("repeated game: a deviation pays where (ii) holds")
    # Where (ii) holds, attempting is worth at most 0 one-shot and A <= 0 repeated: repeated play cannot
    # undo (ii). Where only (i) holds, re-admission multiplies the stake a reporter must beat.
    mult = {f"delta={d}": 1 / (1 - d * (1 - beta)) for d in (0.5, 0.9, 0.99, 0.999)}
    cumulative = {f"delta={d}": beta / (1 - d * (1 - beta)) for d in (0.5, 0.9, 0.99)}
    res.number("e6-sourced-payoffs-inside", sum(p["inside_ii"] for p in points), fmt=",.0f",
               label=f"sourced payoff calibrations that fall inside C7's penalty condition (ii) (of {len(points)}; both are illustrative calibrations, not measurements)")
    return {
        "region": {"(i)": "R / V > beta, two or more members", "(ii)": f"V / P <= (1 - beta) / beta = {bound:.1f}",
                   "share_of_real_parties_inside": "not identified: V, P, R and Q are measured for no party",
                   "decisive_advantage": "V of a decisive advantage is unbounded relative to any stated penalty; "
                                         "where V / P > 19 and R / V <= beta, neither condition holds"},
        "sourced_points": points,
        "repeated": {
            "checked_instances": n, "instances_where_ii_holds": int(holds_ii.sum()),
            "expelled_on_capture": "a deviation is unprofitable iff beta V - (1 - beta) P <= w / (1 - delta): repeated "
                                   "play adds the membership term w / (1 - delta) and widens (ii)",
            "readmitted_on_capture": "attempting forever is worth (pi V - (1 - pi) P) / (1 - delta (1 - pi)); it has the "
                                     "sign of the one-shot payoff, so (ii) survives, and where only (i) holds the reward "
                                     "a reporter needs rises by the factor below, up to 1 / beta",
            "reward_multiplier_readmitted": mult,
            "cumulative_success_readmitted_at_beta": cumulative,
            "verdict": "Repeated play does not undo (ii). It can undo (i): if caught members are re-admitted and no "
                       "membership value w is at stake, the reward condition grows from beta V towards V. Whether "
                       "it does for real parties depends on w and delta, which are not measured.",
        },
        "withdrawal": {
            "rule": "With assets frozen during a notice N and response starting at notice, an exit breakout fails "
                    "if T_b + N >= T_resp; without the freeze the party can start during notice and N adds nothing, "
                    "so the condition is T_b >= T_resp whatever N is.",
            "E24_floor": f"On E24's record {L['e24-halt-share-never']:.0%} of findings made inside a treaty were never "
                         "followed by a halt; if that share carries over, an exit breakout succeeds at least that often "
                         "whatever the notice, and no notice meets beta.",
        },
        "transfer_edge": {
            "definition": "If party i can use a share e_ij of party j's compute or research output (shared weights, "
                          "distillation, cloud), its breakout time is h_w / (s_i + e_ij s_j). Each party alone can pass "
                          "the line while the pair fails it whenever s_i + e_ij s_j > s*. This is the edge E11 needs; "
                          "no e_ij is measured, so the coupled share is not identified.",
        },
    }


def main() -> int:
    res = Results("E6", "e06_games", seed=SEED)
    for url, name, what in PAPERS.values():
        fetch(url, name, res, what=what)
    tab = load_table()
    ledger = json.loads((ROOT / "data" / "numbers.json").read_text())
    L = {k: float(ledger[k]["value"]) for k in LEDGER_IDS}
    res.detail("ledger_inputs", {k: L[k] for k in LEDGER_IDS})
    res.detail("table", {p: {k: {kk: r[kk] for kk in ("value", "unit", "kind", "source", "where")}
                             for k, r in rows.items()} for p, rows in tab.items()})
    rng = np.random.default_rng(SEED)
    beta = L["def-prevent-beta"]

    arm = armstrong(tab, res)
    res.detail("armstrong", arm)
    print("armstrong done", flush=True)
    ex = emery_xu(tab, res)
    res.detail("emery_xu", ex)
    print("emery-xu done", flush=True)
    info = information_regimes(tab, res, beta)
    res.detail("information_regimes", info)
    print("information regimes done", flush=True)
    fk = fudenberg(tab, res, beta)
    res.detail("fudenberg_koh", fk)
    gn = gan(tab, res, L)
    res.detail("gan", gn)
    res.detail("nordhaus", nordhaus(tab, res))
    ba = barrett(tab)
    res.detail("barrett_dannenberg", ba)
    res.number("e6-ba-eq-certainty", len(ba["symmetric_pure_equilibria_chips_each"]["certainty"]), fmt=",.0f",
               label="symmetric pure equilibria of Barrett and Dannenberg's game with a known threshold (they give 2)")
    res.number("e6-ba-eq-threshold", len(ba["symmetric_pure_equilibria_chips_each"]["threshold"]), fmt=",.0f",
               label="symmetric pure equilibria of the same game with the threshold uniform on 100 to 200 chips (they give 1, contributing nothing)")
    cs = c7_share(tab, res, L)
    res.detail("c7_share", cs)
    cp = c7_payoffs(res, L, gn, fk, rng)
    res.detail("c7_payoffs", cp)
    sm = info["summary"]
    ill, e24 = cs["line"]["illustrative"], cs["line"]["e24_median"]
    cen = cs["staged"]["central"]
    hi = cs["staged"]["high (ledger interval)"]
    res.detail("claims", {
        "C7": (f"Repeated play does not undo condition (ii) (its sign survives expulsion and re-admission), but re-admitting "
               f"caught members raises the reward condition (i) by up to 1 / beta. The sourced payoff calibrations (Gan, "
               f"V / P = {cp['sourced_points'][0]['V_over_P']:.2f}; Fudenberg and Koh's analogue, "
               f"{cp['sourced_points'][1]['V_over_P']:.2f}) both sit inside (ii); real parties' payoffs are not identified. "
               f"C7.3: within the hardwired-pause paper's own budget range the overt line binds below "
               f"{ill['budget_below_which_line_binds']:.2g} FLOP ({ill['share_of_range_binding_uniform']:.0%} of the range, uniform) "
               f"at the illustrative T_r and below {e24['budget_below_which_line_binds']:.2g} FLOP "
               f"({e24['share_of_range_binding_uniform']:.0%}) at E24's median response; at the bullish end s* is "
               f"{ill['share_bullish_with_margin']:.0%} and {e24['share_bullish_with_margin']:.0%}. "
               f"Staged accumulation with algorithms fixed at launch stays below beta on the margin-2 line "
               f"(best {cen['frozen_at_launch']['pi_max_on_ledger_line']:.3f} central, "
               f"{hi['frozen_at_launch']['pi_max_on_ledger_line']:.3f} at high drift); if the run absorbs drift as it goes it "
               f"reaches {cen['in_run_drift']['pi_max_on_ledger_line']:.3f} (central) and "
               f"{hi['in_run_drift']['pi_max_on_ledger_line']:.3f} (high), so the line must fall to "
               f"{cen['in_run_drift']['largest_share_staged_no_margin']:.0%} or "
               f"{hi['in_run_drift']['largest_share_staged_no_margin']:.0%}. Prop 1.6's line does not cover in-run drift."),
        "C1": ("Lemma 1.1 is used as stated; repeated attempts compound to beta / (1 - delta (1 - beta)) when caught "
               "members are re-admitted. The response time is the protocol's illustration or E24's median, not a bound."),
        "C6": "The transfer edge is defined (s_i + e_ij s_j against s*) and no e_ij is measured: not identified.",
        "O2": (f"Compliance-only disclosure gave a higher disaster risk than no information in "
               f"{sm['compliance_over_none']:.0%} of {sm['cells']} cells, higher than private information alone in "
               f"{sm['compliance_over_private']:.0%} and higher than public capability in {sm['compliance_over_public']:.0%}. "
               + (f"The candidate holds in {len(sm['cells_where_compliance_no_riskier_than_none'])} cells (listed in "
                  f"information_regimes.summary) and is cut back to them."
                  if sm["cells_where_compliance_no_riskier_than_none"] else
                  "It holds in no cell, so in these race models the candidate is cut: the information alone raises risk, "
                  "and any protection in them comes from halting a breakout (risk times S, true by construction), not from disclosure.")),
    })
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
