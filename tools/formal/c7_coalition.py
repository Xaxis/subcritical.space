#!/usr/bin/env python3
"""Check the statements of section C7 in research/05-formal.md.

Prop 7.1   with fleet F(t), efficiency A(t) and budget B, a coalition with share s has
           T_b(s) = inf{t : s * I(t) >= B}, I(t) = int_0^t F r u A; the largest share meeting
           T_b(s) >= m * T_r is s* = min(1, B / I(m * T_r)), which is h_w / (m * T_r) at fixed fleet and
           algorithms, and h_w / G(m T_r) with T_b(s) = G^-1(h_w / s) at a fixed fleet with drift
           absorbed during the run, G(x) = (e^(a x) - 1) / a.
Thm 7.2    in the reporting game with Poisson detection: for every share with T_b(s) >= T_r (so for
           every s <= h_w / T_r, which includes (s*, m * s*]), (i) if R_i > beta * V_i for every member
           of a coalition of two or more, every member strictly prefers reporting to staying; (ii) if
           beta * V_i <= (1 - beta) * P_i, no member profits from the breakout.
           (iii) for every share with T_b(s) < T_r there are payoffs making the breakout profitable and
           self-enforcing.
Note       the claim's "some coalition above s* has a profitable self-enforcing deviation" fails on
           (s*, m * s*] whenever (i) or (ii) holds; the check counts such shares only where it checked
           the condition that applies ((ii) for anyone, (i) for two or more members). A single party
           outside (ii) is covered by neither, and the check counts how often its breakout pays
           (red team C7.2); the red team's instance against "none can" is recorded as outside both.
Repeated   (E6, red team C7.7) one attempt a period at pi <= beta, discount delta < 1, a report pays
           R_i once and ends the coalition. Re-admitted after capture, attempting forever is worth
           U = (pi V - (1 - pi) P) / (1 - delta (1 - pi)) (value iteration of the member's choice gives
           max(0, U)); (ii) implies U <= 0, and with expulsion and membership worth w a period,
           pi V - (1 - pi) P <= w / (1 - delta); R > beta V / (1 - delta (1 - beta)) makes reporting
           strictly preferred, and at P = 0, pi = beta nothing less does. Recorded: an instance with
           R > beta V (one-shot (i)) where re-admission makes staying pay more than reporting.

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
        h_w = budget / (f0 * ru)
        if growth == 0.0 and drift > 0.0:
            ck.ok("Prop 7.1: fixed fleet with in-run drift gives s* = min(1, h_w / G(m T_r))",
                  abs(s_star - min(1.0, h_w * drift / math.expm1(drift * m * t_r))) <= 1e-12 * s_star,
                  (h_w, drift, m, t_r))
        if growth == 0.0 and drift == 0.0:
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
        if growth == 0.0 and drift > 0.0 and math.isfinite(t_b(s_in)):
            cf = math.log1p(drift * h_w / s_in) / drift
            ck.ok("Prop 7.1: with in-run drift, T_b(s) = G^-1(h_w / s) (bisection agrees)",
                  abs(t_b(s_in) - cf) <= 1e-9 * max(1.0, cf), (h_w, drift, s_in, cf, t_b(s_in)))
        if s_star < 1.0:
            s_out = s_star + (1.0 - s_star) * rng.uniform(1e-3, 1.0)
            ck.ok("Prop 7.1: shares above s* break the line", t_b(s_out) < m * t_r,
                  (f0, growth, drift, budget, m, t_r, s_out, s_star))

    # Thm 7.2
    gap_penalty = gap_reward = single_open = single_pays = 0
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
        if s_star < s_line and s > s_star:  # a share in (s*, h_w / T_r]
            if regime == "penalty":
                gap_penalty += 1  # (ii) checked above: no member profits
            elif members >= 2:
                gap_reward += 1  # (i) checked above: every member prefers reporting
            else:
                single_open += 1  # a single party under rewards: neither condition applies
                if stay[0] > 0:
                    single_pays += 1

        # (iii) above the line
        if s_line < 1.0:
            s_hi = s_line + (1.0 - s_line) * rng.uniform(1e-3, 1.0)
            ph = pi(s_hi)
            ck.ok("Thm 7.2(iii): above h_w / T_r the success chance exceeds beta", ph > beta, (h_w, lam, beta, s_hi))
            v2 = [(r[i] + (1 - ph) * p[i]) / ph * 1.01 + 1e-9 for i in range(members)]
            ok = all(ph * v2[i] - (1 - ph) * p[i] >= r[i] and ph * v2[i] - (1 - ph) * p[i] > 0
                     for i in range(members))
            ck.ok("Thm 7.2(iii): payoffs exist that make it profitable and self-enforcing", ok, (ph, r, p, v2))
    ck.note(f"the claim's 'some coalition above s*' fails: {gap_penalty + gap_reward} sampled shares in "
            f"(s*, h_w / T_r] had no profitable self-enforcing deviation, checked ({gap_penalty} under (ii), "
            f"{gap_reward} under (i) with two or more members)")
    ck.note(f"single parties under rewards, outside (ii), in (s*, h_w / T_r]: {single_open} sampled, "
            f"{single_pays} with a breakout that pays (no partner can report it)")
    # Recorded (red team C7.2): a deviation below the line outside both conditions.
    beta, ps, v, pen, rew = 0.05, 0.03, 1000.0, 1.0, 1.0
    stay = ps * v - (1 - ps) * pen
    ck.ok("Recorded (red team C7.2): pi <= beta but outside (i) and (ii), staying pays more than reporting",
          ps <= beta and not rew > beta * v and not beta * v <= (1 - beta) * pen and stay > rew and stay > 0, stay)

    # Repeated play (E6, red team C7.7).
    for _ in range(N // 10):
        beta = 10 ** rng.uniform(-3, math.log10(0.3))
        pi = beta if rng.random() < 0.3 else beta * rng.uniform(1e-3, 1.0)
        v = 10 ** rng.uniform(0, 3)
        delta = rng.choice([0.5, 0.9, 0.99, rng.uniform(0.01, 0.99)])
        if rng.random() < 0.5:
            pen = beta * v / (1 - beta) * rng.uniform(1.0, 3.0)  # inside (ii)
        else:
            pen = rng.choice([0.0, beta * v / (1 - beta) * rng.uniform(0.0, 1.0)])  # outside or on the edge
        u = (pi * v - (1 - pi) * pen) / (1 - delta * (1 - pi))
        # value iteration of the member's choice each period: comply (0) or attempt
        x, q = 0.0, delta * (1 - pi)
        for _ in range(100000):
            nx = max(0.0, pi * v + (1 - pi) * (delta * x - pen))
            if abs(nx - x) <= 1e-14 * max(1.0, v):
                x = nx
                break
            x = nx
        detail = (beta, pi, v, pen, delta)
        ck.ok("Repeated: value iteration of the re-admission game gives max(0, U)",
              abs(x - max(0.0, u)) <= 1e-9 * max(1.0, v) / (1 - q), detail + (x, u))
        ck.ok("Repeated: U has the sign of the one-shot payoff",
              (u > 0) == (pi * v - (1 - pi) * pen > 0), detail + (u,))
        if beta * v <= (1 - beta) * pen:
            w = rng.choice([0.0, rng.uniform(0, v)])
            ck.ok("Repeated: (ii) survives re-admission (U <= 0)", u <= 1e-12 * v, detail + (u,))
            ck.ok("Repeated: (ii) survives expulsion (one attempt worth at most w / (1 - delta))",
                  pi * v - (1 - pi) * pen <= w / (1 - delta) + 1e-12 * v, detail + (w,))
        need = beta * v / (1 - delta * (1 - beta))
        rew = need * rng.uniform(1.0 + 1e-9, 2.0)
        ck.ok("Repeated: R > beta V / (1 - delta (1 - beta)) makes reporting strictly preferred",
              rew > u, detail + (rew, u))
        ck.ok("Repeated: the reward needed is below V and its factor over beta V below 1 / beta",
              need < v and need / (beta * v) < 1 / beta, detail + (need,))
        u_edge = beta * v / (1 - delta * (1 - beta))  # P = 0, pi = beta
        ck.ok("Repeated: at P = 0 and pi = beta any smaller reward leaves staying better",
              need * (1 - 1e-6) < u_edge, detail + (need, u_edge))
    # Recorded: one-shot (i) holds, re-admission undoes it.
    beta, ps, v, pen, delta, rew = 0.05, 0.05, 1.0, 0.0, 0.9, 0.1
    u = (ps * v - (1 - ps) * pen) / (1 - delta * (1 - ps))
    ck.ok("Recorded (E6): R > beta V, yet under re-admission staying pays more than reporting",
          rew > beta * v and u > rew, u)
    ck.note(f"re-admission instance: beta {beta}, delta {delta}, R {rew} > beta V; staying is worth {u:.3f}; "
            f"the reward needed is {beta * v / (1 - delta * (1 - beta)):.3f}")
    ck.done()


if __name__ == "__main__":
    main()
