#!/usr/bin/env python3
"""Check the statements of section C7 in research/05-formal.md.

Prop 7.1   with fleet F(t), efficiency A(t) and budget B, a coalition with share s has
           T_b(s) = inf{t : s * I(t) >= B}, I(t) = int_0^t F r u A; the largest share meeting
           T_b(s) >= m * T_r is s* = min(1, B / I(m * T_r)), which is h_w / (m * T_r) at fixed fleet and
           algorithms.
Thm 7.2    in the reporting game with Poisson detection: for every share with T_b(s) >= T_r (so for
           every s <= h_w / T_r, which includes (s*, m * s*]), (i) if R_i > beta * V_i for every member
           of a coalition of two or more, every member strictly prefers reporting to staying; (ii) if
           beta * V_i <= (1 - beta) * P_i, no member profits from the breakout.
           (iii) for every share with T_b(s) < T_r there are payoffs making the breakout profitable and
           self-enforcing.
Note       the claim's "some coalition above s* has a profitable self-enforcing deviation" fails on
           (s*, m * s*] whenever (i) or (ii) holds; the check counts such instances.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261134
N = 20000


def main() -> None:
    ck = Check("c7_coalition", SEED)
    rng = ck.rng

    # Prop 7.1
    for _ in range(N):
        f0 = 10 ** rng.uniform(5, 8)
        ru = 10 ** rng.uniform(7, 7.5)  # FLOP per chip-year at the stated utilisation, roughly
        growth = rng.choice([0.0, rng.uniform(0, 0.5)])
        drift = rng.choice([0.0, rng.uniform(0, 1.0)])
        budget = 10 ** rng.uniform(12, 16)
        m = rng.uniform(1, 4)
        t_r = 10 ** rng.uniform(-1, 1.7)
        k = growth + drift

        def integral(t: float) -> float:
            return f0 * ru * (math.expm1(k * t) / k if k > 0 else t)

        s_star = min(1.0, budget / integral(m * t_r))
        if growth == 0.0 and drift == 0.0:
            h_w = budget / (f0 * ru)
            ck.ok("Prop 7.1: fixed fleet and algorithms give s* = min(1, h_w / (m T_r))",
                  abs(s_star - min(1.0, h_w / (m * t_r))) <= 1e-12 * max(s_star, 1e-300), (h_w, m, t_r))

        def t_b(s: float) -> float:
            lo, hi = 0.0, 1.0
            while s * integral(hi) < budget:
                hi *= 2
                if hi > 1e6:
                    return math.inf
            for _ in range(200):
                mid = (lo + hi) / 2
                if s * integral(mid) >= budget:
                    hi = mid
                else:
                    lo = mid
            return hi

        s_in = s_star * rng.uniform(1e-3, 1.0)
        ck.ok("Prop 7.1: shares at or below s* meet the line", t_b(s_in) >= m * t_r * (1 - 1e-9),
              (f0, growth, drift, budget, m, t_r, s_in, s_star))
        if s_star < 1.0:
            s_out = s_star + (1.0 - s_star) * rng.uniform(1e-3, 1.0)
            ck.ok("Prop 7.1: shares above s* break the line", t_b(s_out) < m * t_r,
                  (f0, growth, drift, budget, m, t_r, s_out, s_star))

    # Thm 7.2
    margin_gap = 0
    for _ in range(N):
        h_w = 10 ** rng.uniform(-0.5, 1.5)
        lam = 10 ** rng.uniform(-2, 1)
        beta = 10 ** rng.uniform(-3, math.log10(0.3))
        t_resp = rng.uniform(0, 3)
        m = rng.uniform(1, 4)
        t_d = math.log(1 / beta) / lam
        t_r = t_d + t_resp
        s_star = min(1.0, h_w / (m * t_r))
        s_line = min(1.0, h_w / t_r)  # T_b(s) >= T_r exactly up to here
        members = rng.randint(1, 6)
        regime = rng.choice(["reward", "penalty"])
        v = [10 ** rng.uniform(-1, 4) for _ in range(members)]
        if regime == "reward":
            r = [beta * vi * rng.uniform(1.0 + 1e-9, 5) for vi in v]
            p = [10 ** rng.uniform(-2, 3) for _ in range(members)]
        else:
            p = [beta * vi / (1 - beta) * rng.uniform(1.0, 5) for vi in v]
            r = [10 ** rng.uniform(-2, 3) for _ in range(members)]

        def pi(s: float) -> float:
            tb = h_w / s
            return 1.0 if tb <= t_resp else math.exp(-lam * (tb - t_resp))

        s = s_line * rng.uniform(1e-3, 1.0)
        ps = pi(s)
        stay = [ps * v[i] - (1 - ps) * p[i] for i in range(members)]
        ck.ok("Thm 7.2: T_b(s) >= T_r implies success chance <= beta", ps <= beta * (1 + 1e-9), (h_w, lam, beta, s))
        if regime == "reward" and members >= 2:
            ck.ok("Thm 7.2(i): R_i > beta V_i makes every member prefer reporting",
                  all(stay[i] < r[i] for i in range(members)), (v, r, p, ps))
        if regime == "penalty":
            ck.ok("Thm 7.2(ii): beta V_i <= (1 - beta) P_i makes the breakout unprofitable",
                  all(stay[i] <= 1e-12 * (1 + v[i]) for i in range(members)), (v, p, ps))
        if s_star < s_line and s > s_star:
            margin_gap += 1  # a share above s* with no profitable self-enforcing deviation

        # (iii) above the line
        if s_line < 1.0:
            s_hi = s_line + (1.0 - s_line) * rng.uniform(1e-3, 1.0)
            ph = pi(s_hi)
            ck.ok("Thm 7.2(iii): above h_w / T_r the success chance exceeds beta", ph > beta, (h_w, lam, beta, s_hi))
            v2 = [(r[i] + (1 - ph) * p[i]) / ph * 1.01 + 1e-9 for i in range(members)]
            ok = all(ph * v2[i] - (1 - ph) * p[i] >= r[i] and ph * v2[i] - (1 - ph) * p[i] > 0
                     for i in range(members))
            ck.ok("Thm 7.2(iii): payoffs exist that make it profitable and self-enforcing", ok, (ph, r, p, v2))
    ck.note(f"the claim's 'some coalition above s*' fails: {margin_gap} sampled shares lay in "
            f"(s*, m * s*] with no profitable self-enforcing deviation")
    ck.done()


if __name__ == "__main__":
    main()
