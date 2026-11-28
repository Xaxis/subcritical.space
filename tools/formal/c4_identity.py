#!/usr/bin/env python3
"""Check the statements of section C4 in research/05-formal.md.

Round model: within round k the stock follows the common form du/dt = theta * exp(-b u) * E_k^lambda,
with the input fixed for the round at E_k = c * exp(e * u_k) (closure e; e = 0 is a fixed
researcher). K = e * lambda / b. Delta_k = u_(k+1) - u_k, x_k = b * Delta_k.

Lemma 4.1  exact identity  ln[(e^(x_(k+1)) - 1) / (e^(x_k) - 1)] = b (K - 1) Delta_k, checked against
           a numerical integration of the ODE inside each round (not the closed form).
Cor 4.1a   first-order form: ln(Delta_(k+1)/Delta_k) = b (K - 1) Delta_k - [f(x_(k+1)) - f(x_k)],
           f(x) = ln((e^x - 1)/x), with |f(x') - f(x)| between |x' - x|/2 and |x' - x|.
Lemma 4.2  ln(e^(b Delta_0(E)) - 1) is linear in ln E with slope lambda (budgets 1, 2, 4).
Prop 4.3   Delta_(k+1) > Delta_k iff K > 1; for K < 1, g_k < 1 always, the level is unbounded
           (u_k >= ln(y_0 + k * gamma * y_0^K) / b), and g_k approaches 1.
Cor 4.5a   the rule on K's product bound fires on {U_e U_r > K*}: with U_e <= 1 this lies inside
           the r-only rule's firing set at the tightened level zeta_r, which contains the r-only
           rule's firing set at zeta; with U_e = 1 the K rule fires whenever the r-only rule at
           zeta does. So a false-alarm rate quoted for r alone is not the K rule's (red team C4.7).
Prop 4.6   (demonstration, reported not asserted) measurement noise on Delta biases the naive
           through-origin regression toward subcritical; a split-sample regression removes the
           correlated part.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math
from statistics import NormalDist

from _lib import Check

SEED = 20261130
N = 600


def f(x: float) -> float:
    return math.log(math.expm1(x) / x)


def integrate_round(u0: float, b: float, theta: float, lam: float, e: float, c: float, tau: float,
                    du_max: float = 2e-3) -> float:
    """RK4 for du/dt = theta * exp(-b u) * E^lam with E = c * exp(e * u0) fixed for the round, with
    steps sized so that u moves at most du_max per step (the rate falls within a round)."""
    ein = (c * math.exp(e * u0)) ** lam

    def fn(v: float) -> float:
        return theta * math.exp(-b * v) * ein

    t, u = 0.0, u0
    while t < tau:
        h = min(tau - t, du_max / max(fn(u), 1e-300))
        k1 = fn(u)
        k2 = fn(u + h * k1 / 2)
        k3 = fn(u + h * k2 / 2)
        k4 = fn(u + h * k3)
        u += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return u


def main() -> None:
    ck = Check("c4_identity", SEED)
    rng = ck.rng

    for _ in range(N):
        b = rng.uniform(0.2, 3.0)
        lam = rng.uniform(0.2, 2.0)
        e = rng.choice([0.0, rng.uniform(0.0, 1.0), min(1.0, rng.uniform(0.5, 1.5))])
        K = e * lam / b
        tau = 1.0
        c = 1.0
        # choose theta so the first round gains Delta_0 in [0.02, 1.5]
        d0 = rng.uniform(0.02, 1.5)
        theta = math.expm1(b * d0) / (b * tau)
        us = [0.0]
        for _ in range(7):
            u_next = integrate_round(us[-1], b, theta, lam, e, c, tau)
            if u_next - us[-1] > 30 or not math.isfinite(u_next):
                break
            us.append(u_next)
        deltas = [us[i + 1] - us[i] for i in range(len(us) - 1)]
        for k in range(len(deltas) - 1):
            d, dn = deltas[k], deltas[k + 1]
            x, xn = b * d, b * dn
            lhs = math.log(math.expm1(xn) / math.expm1(x))
            rhs = b * (K - 1) * d
            ck.ok("Lemma 4.1: exact round identity (numerical ODE)",
                  abs(lhs - rhs) <= 1e-6 * max(1.0, abs(rhs)), (b, lam, e, d0, k, lhs, rhs))
            err = math.log(dn / d) - rhs
            df = abs(f(xn) - f(x))
            ck.ok("Cor 4.1a: first-order error is -(f(x_(k+1)) - f(x_k))",
                  abs(err + (f(xn) - f(x))) <= 1e-6 * max(1.0, abs(rhs)), (b, lam, e, k, err))
            ck.ok("Cor 4.1a: |f(x') - f(x)| between |x' - x| / 2 and |x' - x|",
                  0.5 * abs(xn - x) - 1e-9 <= df <= abs(xn - x) + 1e-9, (x, xn, df))
            if abs(K - 1) > 1e-6:
                ck.ok("Prop 4.3: Delta_(k+1) > Delta_k iff K > 1", (dn > d) == (K > 1), (b, lam, e, k, d, dn))

    # Lemma 4.2: lambda from budgets, at a fixed start
    for _ in range(N):
        b = rng.uniform(0.2, 3.0)
        lam = rng.uniform(0.2, 2.0)
        theta = 10 ** rng.uniform(-2, 0)
        ys = []
        for budget in (1.0, 2.0, 4.0):
            d0 = integrate_round(0.0, b, theta, lam, 0.0, budget, 1.0)
            ys.append(math.log(math.expm1(b * d0)))
        s1 = (ys[1] - ys[0]) / math.log(2)
        s2 = (ys[2] - ys[1]) / math.log(2)
        ck.ok("Lemma 4.2: ln(e^(b Delta_0) - 1) has slope lambda in ln E",
              abs(s1 - lam) <= 1e-6 and abs(s2 - lam) <= 1e-6, (b, lam, theta, s1, s2))

    # Prop 4.3, subcritical: exact recursion y_(k+1) = y_k + gamma * y_k^K, y = e^(b u)
    first_cross = []
    for _ in range(200):
        b = rng.uniform(0.2, 3.0)
        K = rng.uniform(0.0, 0.95)
        gamma = math.expm1(b * rng.uniform(0.02, 1.5))
        y0 = 1.0
        y = y0
        prev_d = None
        crossed = None
        worst = (0.0, -1)
        kmax = 100000
        for k in range(kmax):
            y_new = y + gamma * y ** K
            d = math.log(y_new / y) / b
            if prev_d is not None:
                g = d / prev_d
                if g > worst[0]:
                    worst = (g, k)
                if crossed is None and g > 0.9:
                    crossed = k
            prev_d = d
            y = y_new
            if k in (10, 1000, kmax - 1):
                ck.ok("Prop 4.3: level unbounded, u_k >= ln(y0 + k gamma y0^K) / b",
                      math.log(y) / b >= math.log(y0 + (k + 1) * gamma * y0 ** K) / b - 1e-12,
                      (b, K, gamma, k))
        ck.ok("Prop 4.3: g_k < 1 in every one of 100,000 rounds when K < 1", worst[0] < 1.0,
              (b, K, gamma, worst))
        ck.ok("Prop 4.3: g_k approaches 1 (above 0.999 by round 100,000)", g > 0.999, (b, K, gamma, g))
        first_cross.append(crossed if crossed is not None else kmax)
    first_cross.sort()
    ck.note(f"Prop 4.3: round at which a perfectly measured g_k first exceeds 0.9, over 200 "
            f"subcritical instances: median {first_cross[100]}, max {first_cross[-1]}")

    # Prop 4.6: errors in variables (reported, not asserted)
    naive_bias, split_bias, reps = 0.0, 0.0, 0
    for _ in range(40):
        b = rng.uniform(0.5, 2.0)
        K = rng.uniform(0.3, 0.9)
        gamma = math.expm1(b * rng.uniform(0.2, 1.0))
        y = 1.0
        deltas = []
        for _ in range(9):
            y_new = y + gamma * y ** K
            deltas.append(math.log(y_new / y) / b)
            y = y_new
        sigma = 0.05 * sum(deltas) / len(deltas)
        for _ in range(500):
            m1 = [d + rng.gauss(0, sigma) for d in deltas]
            m2 = [d + rng.gauss(0, sigma) for d in deltas]
            if min(m1) <= 0 or min(m2) <= 0:
                continue
            xs = m1[:-1]
            y_naive = [math.log(m1[i + 1] / m1[i]) for i in range(len(m1) - 1)]
            y_split = [math.log(m2[i + 1] / m2[i]) for i in range(len(m2) - 1)]
            sxx = sum(v * v for v in xs)
            s_naive = sum(a * c for a, c in zip(xs, y_naive)) / sxx
            s_split = sum(a * c for a, c in zip(xs, y_split)) / sxx
            # the true first-order slope, from noise-free data
            ys_true = [math.log(deltas[i + 1] / deltas[i]) for i in range(len(deltas) - 1)]
            s_true = sum(a * c for a, c in zip(deltas[:-1], ys_true)) / sum(v * v for v in deltas[:-1])
            naive_bias += (s_naive - s_true) / b
            split_bias += (s_split - s_true) / b
            reps += 1
    ck.note(f"Prop 4.6: mean bias in K-hat from 5% noise on each Delta, {reps} replications: naive "
            f"{naive_bias / reps:+.4f}, split-sample {split_bias / reps:+.4f}")

    # Cor 4.5a: which firing sets nest, on random estimates and thresholds.
    z = NormalDist().inv_cdf
    for _ in range(20 * N):
        alpha = rng.choice([0.1, 0.05, 0.01])
        alpha_r = alpha * rng.uniform(0.2, 0.8)
        alpha_e = alpha - alpha_r
        r_hat, s_r = rng.uniform(0, 2), rng.uniform(0.01, 1)
        e_hat, s_e = rng.uniform(0, 1.2), rng.uniform(0.01, 0.5)
        k_star = rng.uniform(0.3, 1.0)
        u_r_a = r_hat + z(1 - alpha) * s_r
        u_r_t = r_hat + z(1 - alpha_r) * s_r
        u_e = min(1.0, e_hat + z(1 - alpha_e) * s_e)
        fires_k = u_e * max(u_r_t, 0.0) > k_star
        ck.ok("Cor 4.5a: with U_e <= 1 the K rule fires only where the r rule at zeta_r does",
              (not fires_k) or u_r_t > k_star, (u_e, u_r_t, k_star))
        ck.ok("Cor 4.5a: the r rule at zeta_r fires wherever the r rule at zeta does",
              (not u_r_a > k_star) or u_r_t > k_star, (u_r_a, u_r_t, k_star))
        if u_e == 1.0:
            ck.ok("Cor 4.5a: with U_e = 1 the K rule fires wherever the r rule at zeta does",
                  (not u_r_a > k_star) or fires_k, (u_r_a, u_r_t, k_star))
    ck.done()


if __name__ == "__main__":
    main()
