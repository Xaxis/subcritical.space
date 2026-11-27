#!/usr/bin/env python3
"""Check the closure statements of section C11 in research/05-formal.md.

Research output F is a CES aggregate of inputs, F = (sum_i a_i x_i^q)^(1/q) (Cobb-Douglas at q = 0,
Leontief as q -> -infinity), nondecreasing in each input. A gate of strength g_i on input i lowers it
to x_i (1 - g_i). f_S = F(gates on S) / F(no gates).

Thm 11.1  (a) f_S <= min_{i in S} f_i for every F; (b) Cobb-Douglas: f_S = prod_{i in S} f_i;
          (c) complements (q < 0, log-supermodular): f_{ij} >= f_i f_j; substitutes (0 < q <= 1,
          log-submodular): f_{ij} <= f_i f_j; Leontief with every input binding: f_S = min f_i.
Thm 11.2  closed loop in the common form, inputs E_i = c_i X^(e_i) aggregated by CES: the local loop
          exponent d ln E / d ln X equals sum_i s_i(X) e_i with s_i = a_i E_i^q / sum_k a_k E_k^q, so it
          lies in [min e, max e] at every X; at large X it tends to max e (q > 0), to sum a_i e_i
          (Cobb-Douglas, weights summing to 1) or to min e (q < 0).

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261138
N = 20000


def ces(x: list[float], a: list[float], q: float) -> float:
    if q == 0.0:
        return math.exp(sum(ai * math.log(xi) for ai, xi in zip(a, x)))
    if q == -math.inf:
        return min(xi / ai for ai, xi in zip(a, x))  # Leontief, coefficients a_i
    return sum(ai * xi ** q for ai, xi in zip(a, x)) ** (1 / q)


def gated(x: list[float], gates: dict[int, float]) -> list[float]:
    return [xi * (1 - gates.get(i, 0.0)) for i, xi in enumerate(x)]


def main() -> None:
    ck = Check("c11_closure", SEED)
    rng = ck.rng

    for _ in range(N):
        n = rng.randint(2, 5)
        kind = rng.choice(["cd", "comp", "subs", "leontief"])
        q = {"cd": 0.0, "comp": -rng.uniform(0.05, 5.0), "subs": rng.uniform(0.05, 1.0), "leontief": -math.inf}[kind]
        raw = [rng.uniform(0.1, 1.0) for _ in range(n)]
        a = [r / sum(raw) for r in raw]
        if kind == "leontief":
            base = rng.uniform(0.5, 2.0)
            x = [ai * base for ai in a]  # every input binds
        else:
            x = [10 ** rng.uniform(-1, 1) for _ in range(n)]
        F0 = ces(x, a, q)
        S = rng.sample(range(n), rng.randint(2, n))
        gates = {i: rng.uniform(0.0, 0.9) for i in S}
        singles = {i: ces(gated(x, {i: gates[i]}), a, q) / F0 for i in S}
        joint = ces(gated(x, gates), a, q) / F0
        prod = math.prod(singles.values())
        ck.ok("Thm 11.1(a): f_S <= min_i f_i", joint <= min(singles.values()) * (1 + 1e-12), (kind, q, a, x, gates))
        if kind == "cd":
            ck.ok("Thm 11.1(b): Cobb-Douglas f_S = prod f_i", abs(joint - prod) <= 1e-10 * prod, (a, x, gates))
        if len(S) == 2:
            if kind in ("comp", "leontief"):
                ck.ok("Thm 11.1(c): complements f_ij >= f_i f_j", joint >= prod * (1 - 1e-12), (kind, q, a, x, gates))
            if kind == "subs":
                ck.ok("Thm 11.1(c): substitutes f_ij <= f_i f_j", joint <= prod * (1 + 1e-12), (q, a, x, gates))
        if kind == "leontief":
            ck.ok("Thm 11.1(c): Leontief with every input binding f_S = min f_i",
                  abs(joint - min(singles.values())) <= 1e-12, (a, x, gates))

    for _ in range(N // 4):
        n = rng.randint(2, 5)
        kind = rng.choice(["cd", "comp", "subs"])
        q = {"cd": 0.0, "comp": -rng.uniform(0.2, 3.0), "subs": rng.uniform(0.2, 1.0)}[kind]
        raw = [rng.uniform(0.1, 1.0) for _ in range(n)]
        a = [r / sum(raw) for r in raw]
        c = [10 ** rng.uniform(-1, 1) for _ in range(n)]
        e = [rng.uniform(0.0, 1.0) for _ in range(n)]

        def ln_e(lnx: float) -> float:
            vals = [math.log(ci) + ei * lnx for ci, ei in zip(c, e)]  # ln E_i
            if q == 0.0:
                return sum(ai * v for ai, v in zip(a, vals))
            terms = [math.log(ai) + q * v for ai, v in zip(a, vals)]
            mx = max(terms)
            return (mx + math.log(sum(math.exp(t - mx) for t in terms))) / q

        for lnx in (rng.uniform(-5, 5), rng.uniform(5, 50)):
            hstep = 1e-5
            num = (ln_e(lnx + hstep) - ln_e(lnx - hstep)) / (2 * hstep)
            vals = [math.log(ci) + ei * lnx for ci, ei in zip(c, e)]
            if q == 0.0:
                shares = a
            else:
                terms = [math.log(ai) + q * v for ai, v in zip(a, vals)]
                mx = max(terms)
                wts = [math.exp(t - mx) for t in terms]
                shares = [w / sum(wts) for w in wts]
            formula = sum(s * ei for s, ei in zip(shares, e))
            ck.ok("Thm 11.2: local loop exponent = share-weighted mean of closures",
                  abs(num - formula) <= 1e-6, (kind, q, a, c, e, lnx, num, formula))
            ck.ok("Thm 11.2: min e <= local loop exponent <= max e",
                  min(e) - 1e-9 <= formula <= max(e) + 1e-9, (kind, q, e, formula))
        # asymptote, at a very large stock (ln X = 2,000)
        big = 2000.0
        slope = (ln_e(big + 1.0) - ln_e(big - 1.0)) / 2.0
        limit = {"cd": sum(ai * ei for ai, ei in zip(a, e)), "comp": min(e), "subs": max(e)}[kind]
        gap = sorted(e)
        sep = min(gap[i + 1] - gap[i] for i in range(n - 1))
        if sep > 0.01 or kind == "cd":
            ck.ok("Thm 11.2: at large X the exponent tends to max e, sum a e or min e",
                  abs(slope - limit) <= 1e-3, (kind, q, a, e, slope, limit))
    ck.done()


if __name__ == "__main__":
    main()
