#!/usr/bin/env python3
"""Check the runaway condition of section C6 (Theorem 6.4) and its corollary for C12 (Cor 6.5)
in research/05-formal.md, by integrating the coupled common form numerically.

Model: du_i/dt = theta_i * exp(-b_i u_i + lam_i * sum_j e_ij u_j), u(0) = 0, with
K_ij = lam_i e_ij / b_i. In z_i = b_i u_i the law is dz/dt = a * exp((M - I) z), a_i = b_i theta_i,
M_ij = lam_i e_ij / b_j = (D K D^-1)_ij with D = diag(b), so rho(M) = rho(K).

Thm 6.4 (i)   rho(K) > 1: with w the left Perron vector of M (sum 1) and a_min = min_i a_i,
              w.z(t) >= -ln(1 - a_min (rho - 1) t) / (rho - 1), so w.z reaches any level V by
              t_c(V) = (1 - exp(-(rho - 1) V)) / (a_min (rho - 1)) and diverges by 1/(a_min (rho - 1)).
Thm 6.4 (ii)  rho(K) < 1: with v the right Perron vector of M, a = (1 - rho) min_i v_i and
              c = max_i a_i / v_i, N(t) = max_i z_i / v_i <= ln(1 + a c t) / a.
Cor 6.5       rho(K) < 1: u_i first reaches D no earlier than (exp(a b_i D / v_i) - 1) / (a c).
Also          rho(M) = rho(K) (similarity), and for one loop the blow-up bound is exact.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check, matvec, perron, spectral_radius

SEED = 20261133
N = 150


def rk4_step(z: list[float], h: float, a: list[float], M: list[list[float]]) -> list[float]:
    def fn(v: list[float]) -> list[float]:
        mz = matvec(M, v)
        return [a[i] * math.exp(mz[i] - v[i]) for i in range(len(v))]

    k1 = fn(z)
    k2 = fn([z[i] + h * k1[i] / 2 for i in range(len(z))])
    k3 = fn([z[i] + h * k2[i] / 2 for i in range(len(z))])
    k4 = fn([z[i] + h * k3[i] for i in range(len(z))])
    return [z[i] + h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(len(z))]


def rates(z: list[float], a: list[float], M: list[list[float]]) -> list[float]:
    mz = matvec(M, z)
    return [a[i] * math.exp(mz[i] - z[i]) for i in range(len(z))]


def random_system(rng, target_rho: float):
    n = rng.randint(1, 4)
    b = [rng.uniform(0.3, 2.0) for _ in range(n)]
    lam = [rng.uniform(0.3, 1.5) for _ in range(n)]
    theta = [10 ** rng.uniform(-1, 0.5) for _ in range(n)]
    e = [[rng.uniform(0.05, 1.0) for _ in range(n)] for _ in range(n)]
    K = [[lam[i] * e[i][j] / b[i] for j in range(n)] for i in range(n)]
    s = target_rho / spectral_radius(K)
    e = [[x * s for x in row] for row in e]
    K = [[lam[i] * e[i][j] / b[i] for j in range(n)] for i in range(n)]
    M = [[lam[i] * e[i][j] / b[j] for j in range(n)] for i in range(n)]
    a = [b[i] * theta[i] for i in range(n)]
    return n, b, K, M, a


def main() -> None:
    ck = Check("c6_runaway", SEED)
    rng = ck.rng

    # (i) supercritical
    for _ in range(N):
        target = rng.uniform(1.05, 3.0)
        n, b, K, M, a = random_system(rng, target)
        rho = spectral_radius(K)
        ck.ok("rho(M) = rho(K)", abs(spectral_radius(M) - rho) <= 1e-8 * rho, (K, M))
        w = perron(M, left=True)
        a_min = min(a)
        v_level = 20.0
        t_c = -math.expm1(-(rho - 1) * v_level) / (a_min * (rho - 1))
        # The comparison is checked level by level, in time (near blow-up a value comparison is
        # ill-conditioned): w.z first reaches level l in a step that began no later than t_c(l).
        levels = [0.5 * j for j in range(1, int(2 * v_level) + 1)]
        nxt = 0
        z, t = [0.0] * n, 0.0
        hit, h = None, 0.0
        while t < 3 * t_c:
            r = rates(z, a, M)
            h = min(2e-3 / max(r), t_c / 500)
            z = rk4_step(z, h, a, M)
            t += h
            V = sum(wi * zi for wi, zi in zip(w, z))
            while nxt < len(levels) and V >= levels[nxt]:
                lv = levels[nxt]
                t_l = -math.expm1(-(rho - 1) * lv) / (a_min * (rho - 1))
                ck.ok("Thm 6.4(i): w.z(t) >= -ln(1 - a_min (rho - 1) t) / (rho - 1), level by level",
                      t - h <= t_l * (1 + 1e-9), (K, a, lv, t, h, t_l))
                nxt += 1
            if V >= v_level:
                hit = t
                break
        # the crossing is resolved to one step: the step in which it happened began by t_c
        ck.ok("Thm 6.4(i): w.z reaches the level by t_c(V)", hit is not None and hit - h <= t_c * (1 + 1e-9),
              (K, a, hit, h, t_c))
        if n == 1:
            exact = -math.expm1(-(rho - 1) * v_level) / (a[0] * (rho - 1))
            ck.ok("Thm 6.4(i): one loop, the bound is exact", abs(hit - exact) <= h + 1e-6 * exact,
                  (hit, h, exact))

    # (ii) subcritical, and Cor 6.5
    for _ in range(N):
        target = rng.uniform(0.1, 0.95)
        n, b, K, M, a = random_system(rng, target)
        rho = spectral_radius(M)
        v = perron(M)
        a_coef = (1 - rho) * min(v)
        c_coef = max(a[i] / v[i] for i in range(n))
        t_end = 10 ** rng.uniform(1, 3)
        dist = [rng.uniform(0.5, 4.0) for _ in range(n)]
        first = [None] * n
        z, t = [0.0] * n, 0.0
        worst = (-math.inf, None)
        while t < t_end:
            r = rates(z, a, M)
            h = min(t_end - t, 2e-3 / max(r), t_end / 400)
            z = rk4_step(z, h, a, M)
            t += h
            n_t = max(z[i] / v[i] for i in range(n))
            bound = math.log1p(a_coef * c_coef * t) / a_coef
            excess = n_t - (bound * (1 + 1e-6) + 1e-9)
            if excess > worst[0]:
                worst = (excess, (t, n_t, bound))
            for i in range(n):
                if first[i] is None and z[i] / b[i] >= dist[i]:
                    first[i] = t
        ck.ok("Thm 6.4(ii): max_i z_i / v_i <= ln(1 + a c t) / a at every step of the run", worst[0] <= 0,
              (K, a, worst))
        for i in range(n):
            if first[i] is not None:
                lower = math.expm1(a_coef * b[i] * dist[i] / v[i]) / (a_coef * c_coef)
                ck.ok("Cor 6.5: time for u_i to reach D >= (exp(a b_i D / v_i) - 1) / (a c)",
                      first[i] >= lower * (1 - 1e-6), (K, a, i, dist[i], first[i], lower))
    ck.done()


if __name__ == "__main__":
    main()
