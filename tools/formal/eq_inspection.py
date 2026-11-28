#!/usr/bin/env python3
"""Check the compliance-equilibrium statements in research/05-formal.md (section "Compliance as an
equilibrium"), by brute force over the party's plans.

Each period a party in the regime either complies (stage payoff w > 0, relative to the post-regime
race) or attempts a breakout, which ends the game: it succeeds with probability pi (payoff V) or is
caught (payoff -P). dev = pi V - (1 - pi) P. Future payoffs are weighted by delta per period (time
preference times the chance the regime continues).

Thm E.1   with no known last period, complying forever is optimal iff w >= (1 - delta) * dev, i.e.
          w / (1 - delta) >= dev.
Thm E.2   with a known last period T: if w < (1 - delta) * dev the party attempts at once; otherwise,
          if dev > w it complies until T and attempts in period T; otherwise it complies throughout.
Prop E.3  (Avenhaus et al.'s payoffs) acting legally is a best response iff the non-detection
          probability is at most (P - h zeta) / (1 + P).
Prop E.4  prevention (non-detection <= beta) implies deterrence when P >= (beta + h zeta) / (1 - beta);
          the check also counts instances where prevention holds without deterrence, and deterrence
          without prevention (demonstrations).

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

from _lib import Check

SEED = 20261139
N = 20000


def main() -> None:
    ck = Check("eq_inspection", SEED)
    rng = ck.rng

    for _ in range(N):
        w = 10 ** rng.uniform(-2, 1)
        delta = rng.uniform(0.5, 0.999)
        pi = rng.uniform(0, 1)
        v = 10 ** rng.uniform(-1, 3)
        p = 10 ** rng.uniform(-1, 3)
        dev = pi * v - (1 - pi) * p

        # E.1: brute force over "attempt in period t" for t = 0..T_big, and "never"
        never = w / (1 - delta)
        best_attempt = max(w * (1 - delta ** t) / (1 - delta) + delta ** t * dev for t in range(0, 400))
        rule = w >= (1 - delta) * dev
        if abs(never - best_attempt) > 1e-9 * (1 + abs(never)):
            ck.ok("Thm E.1: complying forever is optimal iff w >= (1 - delta) dev",
                  (never > best_attempt) == rule, (w, delta, pi, v, p, dev))

        # E.2: known last period T (periods 1..T)
        T = rng.randint(1, 40)
        plans = {"never": w * (1 - delta ** T) / (1 - delta)}
        for t in range(1, T + 1):
            plans[t] = w * (1 - delta ** (t - 1)) / (1 - delta) + delta ** (t - 1) * dev
        best_val = max(plans.values())
        best = [k for k, val in plans.items() if abs(val - best_val) <= 1e-9 * (1 + abs(best_val))]
        if w < (1 - delta) * dev:
            predicted = 1
        elif dev > w:
            predicted = T
        else:
            predicted = "never"
        ck.ok("Thm E.2: known last period, the plan is attempt-now, attempt-at-T or comply",
              predicted in best, (w, delta, dev, T, best, predicted))

    # E.3 and E.4
    prevention_only, deterrence_only = 0, 0
    for _ in range(N):
        b = 10 ** rng.uniform(-2, 2)
        h = rng.uniform(0, b) * 0.999
        alpha = rng.uniform(0, 1)
        nd = rng.uniform(0, 1)  # non-detection probability
        v_legal = -h * alpha
        v_violate = -b + (1 + b) * nd
        legal_best = v_legal >= v_violate
        thresh = (b - h * alpha) / (1 + b)
        if abs(nd - thresh) > 1e-12:
            ck.ok("Prop E.3: legal is a best response iff non-detection <= (P - h zeta)/(1 + P)",
                  legal_best == (nd <= thresh), (b, h, alpha, nd))
        beta = 10 ** rng.uniform(-3, -0.3)
        nd2 = beta * rng.uniform(0, 1)  # prevention holds
        if b >= (beta + h * alpha) / (1 - beta):
            ck.ok("Prop E.4: prevention and P >= (beta + h zeta)/(1 - beta) imply deterrence",
                  -h * alpha >= -b + (1 + b) * nd2 - 1e-12, (b, h, alpha, beta, nd2))
        elif -h * alpha < -b + (1 + b) * nd2:
            prevention_only += 1
        nd3 = rng.uniform(beta, 1)  # prevention fails
        if -h * alpha >= -b + (1 + b) * nd3:
            deterrence_only += 1
    ck.note(f"Prop E.4: prevention held without deterrence in {prevention_only} instances, deterrence "
            f"without prevention in {deterrence_only}")
    ck.done()


if __name__ == "__main__":
    main()
