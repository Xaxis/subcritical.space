#!/usr/bin/env python3
"""Check the statements of section C1 in research/05-formal.md.

Lemma 1.1   success chance <= beta  iff  T_b >= T_d(beta) + T_resp, for any continuous cumulative
            hazard (Poisson, Weibull, piecewise-constant hazard).
Prop 1.2    an admitted holding (estimated T_b >= m * estimated T_r) still meets the prevention
            condition when the unsafe-direction errors satisfy e_b * max(e_d, e_resp) <= m.
Cor 1.3     a hazard overstated by at most c: true T_d(beta) <= estimated T_d(beta^c); Weibull with
            shape k turns a factor c on the hazard into c^(1/k) on T_d.
Prop 1.4    random response time with any dependence on detection: success <= beta1 + beta2 when
            T_b >= T_d(beta1) + the (1 - beta2) quantile of T_resp.
Prop 1.5    the line is per path: max_p success_p <= beta iff every path meets its own condition;
            the scalar test min_p T_b >= max_p T_r implies it, not conversely.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261127
N = 6000


class Hazard:
    """A continuous, nondecreasing cumulative hazard Phi with Phi(0) = 0."""

    def __init__(self, kind: str, params: tuple):
        self.kind, self.params = kind, params

    def phi(self, t: float) -> float:
        if t <= 0:
            return 0.0
        if self.kind == "poisson":
            (lam,) = self.params
            return lam * t
        if self.kind == "weibull":
            eta, k = self.params
            return (t / eta) ** k
        if self.kind == "scaled":  # Phi(t / s) + extra(t): time-scaled hazard plus a nondecreasing extra
            base, s, extra = self.params
            return base.phi(t / s) + (extra.phi(t) if extra else 0.0)
        if self.kind == "divided":  # Phi(t) / c + extra(t)
            base, c, extra = self.params
            return base.phi(t) / c + (extra.phi(t) if extra else 0.0)
        # piecewise-constant hazard: breakpoints b_0 = 0 < b_1 < ... and rates h_i on [b_i, b_{i+1})
        bps, rates = self.params
        total = 0.0
        for i, h in enumerate(rates):
            lo = bps[i]
            hi = bps[i + 1] if i + 1 < len(bps) else math.inf
            if t <= lo:
                break
            total += h * (min(t, hi) - lo)
        return total

    def inverse(self, y: float) -> float:
        """T = inf{t : Phi(t) >= y}, by closed form where there is one, else bisection."""
        if y <= 0:
            return 0.0
        if self.kind == "poisson":
            return y / self.params[0]
        if self.kind == "weibull":
            eta, k = self.params
            return eta * y ** (1 / k)
        lo, hi = 0.0, 1.0
        while self.phi(hi) < y:
            hi *= 2
            if hi > 1e12:
                return math.inf
        for _ in range(200):
            mid = (lo + hi) / 2
            if self.phi(mid) >= y:
                hi = mid
            else:
                lo = mid
        return hi


def random_hazard(rng, allow_zero_segments: bool = True) -> Hazard:
    kind = rng.choice(["poisson", "weibull", "piecewise"])
    if kind == "poisson":
        return Hazard("poisson", (10 ** rng.uniform(-2, 1),))
    if kind == "weibull":
        return Hazard("weibull", (10 ** rng.uniform(-1, 1.3), rng.uniform(0.3, 4.0)))
    m = rng.randint(1, 5)
    bps = [0.0]
    for _ in range(m - 1):
        bps.append(bps[-1] + rng.uniform(0.1, 5))
    rates = [
        (0.0 if allow_zero_segments and rng.random() < 0.2 else 10 ** rng.uniform(-2, 1))
        for _ in range(m)
    ]
    rates[-1] = max(rates[-1], 0.01)  # the last segment detects eventually
    return Hazard("piecewise", (bps, rates))


def success(hz: Hazard, t_b: float, t_resp: float) -> float:
    if t_b <= t_resp:
        return 1.0
    return math.exp(-hz.phi(t_b - t_resp))


def t_d(hz: Hazard, beta: float) -> float:
    return hz.inverse(math.log(1 / beta))


def main() -> None:
    ck = Check("c1_margin", SEED)
    rng = ck.rng

    # Lemma 1.1
    for _ in range(N):
        hz = random_hazard(rng)
        beta = 10 ** rng.uniform(-4, math.log10(0.5))
        t_resp = rng.uniform(0, 5)
        tb = rng.uniform(0, 30)
        td = t_d(hz, beta)
        if abs(tb - (td + t_resp)) < 1e-7:
            continue
        lhs = success(hz, tb, t_resp) <= beta * (1 + 1e-12)
        rhs = tb >= td + t_resp
        ck.ok("Lemma 1.1: S <= beta iff T_b >= T_d + T_resp", lhs == rhs,
              (hz.kind, hz.params, beta, t_resp, tb, td))

    # Prop 1.2 (with the separate errors of Corollary 1.2a)
    for _ in range(N):
        hz_hat = random_hazard(rng, allow_zero_segments=False)
        beta = 10 ** rng.uniform(-4, math.log10(0.5))
        m = rng.uniform(1, 5)
        e_b = rng.uniform(1, m)
        e_r = m / e_b * (1 if rng.random() < 0.3 else rng.uniform(0.5, 1))
        e_d = e_r if rng.random() < 0.5 else rng.uniform(1, e_r) if e_r > 1 else e_r
        e_resp = e_r if rng.random() < 0.5 else rng.uniform(0.5, e_r)
        td_hat = t_d(hz_hat, beta)
        tresp_hat = rng.uniform(0, 5)
        tr_hat = td_hat + tresp_hat
        tb_hat = m * tr_hat * (1 if rng.random() < 0.3 else rng.uniform(1, 3))
        # truths inside the stated error bounds
        s = e_d if rng.random() < 0.5 else rng.uniform(0.5, e_d)
        extra = random_hazard(rng) if rng.random() < 0.3 else None
        hz_true = Hazard("scaled", (hz_hat, s, extra))
        tresp_true = tresp_hat * (e_resp if rng.random() < 0.5 else rng.uniform(0.3, e_resp))
        tb_true = tb_hat / (e_b if rng.random() < 0.5 else rng.uniform(0.5, e_b))
        ck.ok("Prop 1.2: admitted and e_b * max(e_d, e_resp) <= m implies S <= beta",
              success(hz_true, tb_true, tresp_true) <= beta * (1 + 1e-9),
              (hz_hat.kind, hz_hat.params, beta, m, e_b, e_d, e_resp, tb_hat, tr_hat))

    # Corollary 1.3
    for _ in range(N):
        hz_hat = random_hazard(rng, allow_zero_segments=False)
        beta = 10 ** rng.uniform(-4, math.log10(0.5))
        c = rng.uniform(1, 10)
        extra = random_hazard(rng) if rng.random() < 0.5 else None
        hz_true = Hazard("divided", (hz_hat, c, extra))
        ck.ok("Cor 1.3: Phi >= Phi_hat / c implies T_d(beta) <= T_d_hat(beta^c)",
              t_d(hz_true, beta) <= t_d(hz_hat, beta ** c) * (1 + 1e-9) + 1e-12,
              (hz_hat.kind, hz_hat.params, beta, c))
        eta, k = 10 ** rng.uniform(-1, 1.3), rng.uniform(0.3, 4.0)
        true = Hazard("weibull", (eta, k))
        over = Hazard("divided", (true, 1 / c, None))  # Phi_hat = c * Phi
        ratio = t_d(true, beta) / t_d(over, beta)
        ck.ok("Cor 1.3: Weibull, hazard overstated by c gives T_d understated by c^(1/k)",
              abs(ratio - c ** (1 / k)) <= 1e-6 * c ** (1 / k), (eta, k, c, beta, ratio))

    # Prop 1.4: random response time, dependent on detection through a mixture
    for _ in range(N):
        atoms = rng.randint(1, 6)
        rs = [rng.uniform(0, 5) for _ in range(atoms)]
        ws = [rng.random() + 1e-3 for _ in range(atoms)]
        tot = sum(ws)
        ps = [w / tot for w in ws]
        hzs = [random_hazard(rng, allow_zero_segments=False) for _ in range(atoms)]
        beta1 = 10 ** rng.uniform(-3, math.log10(0.4))
        beta2 = rng.choice([0.0, 10 ** rng.uniform(-3, math.log10(0.4))])

        def surv(t: float) -> float:
            return sum(p * math.exp(-h.phi(t)) for p, h in zip(ps, hzs))

        lo, hi = 0.0, 1.0
        while surv(hi) > beta1:
            hi *= 2
        for _ in range(200):
            mid = (lo + hi) / 2
            if surv(mid) <= beta1:
                hi = mid
            else:
                lo = mid
        td1 = hi
        order = sorted(zip(rs, ps))
        cum, q = 0.0, order[-1][0]
        for r, p in order:
            cum += p
            if cum >= 1 - beta2 - 1e-15:
                q = r
                break
        tb = td1 + q + (0 if rng.random() < 0.3 else rng.uniform(0, 5))
        s = sum(p * (1.0 if tb - r <= 0 else math.exp(-h.phi(tb - r))) for r, p, h in zip(rs, ps, hzs))
        ck.ok("Prop 1.4: T_b >= T_d(beta1) + q(1 - beta2) implies S <= beta1 + beta2",
              s <= (beta1 + beta2) * (1 + 1e-9) + 1e-12, (rs, ps, beta1, beta2, tb, s))

    # Prop 1.5: per path
    gap = 0
    for _ in range(N):
        k = rng.randint(2, 6)
        beta = 10 ** rng.uniform(-3, math.log10(0.3))
        m = rng.choice([1.0, rng.uniform(1, 4)])
        paths = []
        for _ in range(k):
            hz = random_hazard(rng, allow_zero_segments=False)
            tresp = rng.uniform(0, 3)
            td = t_d(hz, beta)
            tb = (td + tresp) * m * 10 ** rng.uniform(-0.5, 0.5)
            paths.append((hz, tresp, td, tb))
        if any(abs(tb - (td + tr)) < 1e-7 for _, tr, td, tb in paths):
            continue
        s_max = max(success(hz, tb, tr) for hz, tr, _, tb in paths)
        per_path = all(tb >= td + tr for _, tr, td, tb in paths)
        ck.ok("Prop 1.5: max_p S_p <= beta iff every path meets T_b(p) >= T_r(p)",
              (s_max <= beta * (1 + 1e-12)) == per_path, [(p[1], p[2], p[3]) for p in paths])
        per_path_m = all(tb >= m * (td + tr) for _, tr, td, tb in paths)
        scalar_m = min(p[3] for p in paths) >= m * max(p[2] + p[1] for p in paths)
        ck.ok("Prop 1.5: the scalar test implies the per-path test", (not scalar_m) or per_path_m,
              [(p[1], p[2], p[3]) for p in paths])
        if per_path_m and not scalar_m:
            gap += 1
    ck.note(f"Prop 1.5: in {gap} instances every path met the line but the scalar test failed")

    # The worked counterexample in the text: a fast, watched declared path and a slow covert one.
    declared = (1.0, 0.5)  # (T_b, T_r) in years
    covert = (100.0, 37.0)
    ck.ok("Prop 1.5 example: per path admits", declared[0] >= declared[1] and covert[0] >= covert[1])
    ck.ok("Prop 1.5 example: scalar rejects", not (min(declared[0], covert[0]) >= max(declared[1], covert[1])))
    ck.done()


if __name__ == "__main__":
    main()
