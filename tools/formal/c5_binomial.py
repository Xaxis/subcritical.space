#!/usr/bin/env python3
"""Check the statements of section C5 in research/05-formal.md. All probabilities are computed
exactly from the binomial law (no simulation).

Thm 5.1   the exact one-sided upper bound U(x, n) (the p with P(Bin(n, p) <= x) = zeta) covers:
          P_p(U(X, n) >= p) >= 1 - zeta for every p and n on a grid; with no misses
          U = 1 - zeta^(1/n); the fewest organisms that bring U under the target with 0, 1 and 2
          misses.
Prop 5.2  Ville's test: declaring the miss rate below p_T once M_n >= 1/zeta, with
          M_n = prod (p1/p_T)^Y ((1 - p1)/(1 - p_T))^(1 - Y), has error at most zeta for every
          p >= p_T over a long horizon (exact dynamic programme); with p1 = 0 and no misses it stops
          at the same count as the fixed design.
Prop 5.3  a share eps of organisms from an untested kind moves the miss rate by at most eps.

Standard library only; seeded where random; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check, binom_cdf, log_binom_pmf

SEED = 20261131


def upper(x: int, n: int, alpha: float) -> float:
    if x >= n:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if binom_cdf(n, x, mid) >= alpha:
            lo = mid
        else:
            hi = mid
    return lo


def fewest(x: int, target: float, alpha: float) -> int:
    n = x + 1
    while binom_cdf(n, x, target) > alpha:
        n += 1
    return n


def main() -> None:
    ck = Check("c5_binomial", SEED)
    rng = ck.rng

    for alpha in (0.1, 0.05, 0.01):
        for n in range(1, 61):
            ups = [upper(x, n, alpha) for x in range(n + 1)]
            for i in range(1, 400):
                p = i / 400
                cover = sum(math.exp(log_binom_pmf(n, x, p)) for x in range(n + 1) if ups[x] >= p)
                ck.ok("Thm 5.1: exact upper bound covers at 1 - zeta", cover >= 1 - alpha - 1e-9,
                      (alpha, n, p, cover))
            ck.ok("Thm 5.1: with no misses U = 1 - zeta^(1/n)",
                  abs(ups[0] - (1 - alpha ** (1 / n))) <= 1e-9, (alpha, n, ups[0]))

    n0, n1, n2 = (fewest(x, 0.1, 0.1) for x in (0, 1, 2))
    ck.ok("Thm 5.1: 22 organisms with no misses at 90% and 10%", n0 == 22, n0)
    ck.ok("Thm 5.1: zero-miss count equals ceil(ln zeta / ln(1 - target))",
          n0 == math.ceil(math.log(0.1) / math.log(0.9)), n0)
    ck.note(f"fewest organisms at 90% confidence and a 10% target: {n0} with no miss, {n1} with one, "
            f"{n2} with two")

    # Prop 5.2: Ville's test, exact over a horizon by dynamic programming on the miss count.
    horizon = 300
    for p_t in (0.05, 0.1, 0.2):
        for alpha in (0.1, 0.05):
            for p1 in (0.0, p_t / 10, p_t / 4, p_t / 2):
                stop_at_zero = None
                for p in [p_t + (1 - p_t) * j / 40 for j in range(0, 40)]:
                    # state: misses so far among those not yet stopped
                    alive = {0: 1.0}
                    crossed = 0.0
                    for n in range(1, horizon + 1):
                        nxt: dict[int, float] = {}
                        for misses, mass in alive.items():
                            for y, py in ((1, p), (0, 1 - p)):
                                m2 = misses + y
                                fails = n - m2
                                if p1 == 0.0 and m2 > 0:
                                    logm = -math.inf
                                else:
                                    logm = (m2 * (math.log(p1 / p_t) if m2 else 0.0)
                                            + fails * math.log((1 - p1) / (1 - p_t)))
                                if logm >= math.log(1 / alpha) - 1e-12:
                                    crossed += mass * py
                                    if p == p_t and m2 == 0 and stop_at_zero is None:
                                        stop_at_zero = n
                                else:
                                    nxt[m2] = nxt.get(m2, 0.0) + mass * py
                        alive = nxt
                    ck.ok("Prop 5.2: Ville's test errs with probability <= zeta for p >= p_T",
                          crossed <= alpha + 1e-12, (p_t, alpha, p1, p, crossed))
                if p1 == 0.0:
                    fixed = math.ceil(math.log(alpha) / math.log(1 - p_t))
                    ck.ok("Prop 5.2: with p1 = 0 and no misses Ville's test stops at the fixed-design count",
                          stop_at_zero == fixed, (p_t, alpha, stop_at_zero, fixed))

    # Prop 5.3
    for _ in range(20000):
        p_tested, p_other, eps = rng.random(), rng.random(), rng.random()
        mixed = (1 - eps) * p_tested + eps * p_other
        ck.ok("Prop 5.3: |p_mixture - p_tested| <= eps", abs(mixed - p_tested) <= eps + 1e-12,
              (p_tested, p_other, eps))
    ck.done()


if __name__ == "__main__":
    main()
