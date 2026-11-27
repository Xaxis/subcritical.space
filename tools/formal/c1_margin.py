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
Prop 1.5    for fixed paths, max_p success_p <= beta iff every path meets its own condition; the
            scalar test min_p T_b >= max_p T_r implies it, not conversely.
Adaptive evaders (red team C1.1). Constant rates lam_p of the first event the evader can observe,
counted as the finding; a finding on p halts the party at D + tresp_p; one path at a time.
Success is computed in the evader-favourable reading (only the first finding sets a deadline, and
after it the evader does whatever finishes soonest), an upper bound on success when later findings
also set deadlines, so a bound that holds here holds there.
Prop 1.7    (adaptive) if progress does not carry over between paths and tresp_p <= tb_q for all
            p, q, every strategy succeeds with at most max_p S(p): the per-path test is exact.
Prop 1.8    if progress carries over, every strategy succeeds with at most
            exp(-c_min * (1 - tresp_max / tb_min)), c_min = min_p lam_p tb_p, with equality for a
            common tresp; the portable line implies the per-path line and is implied by the strict
            scalar test tb_min >= max_p T_d(p) + tresp_max.
Prop 1.9    repeated attempts: n attempts each meeting the line at beta / n succeed together with
            probability at most beta, under any dependence.
Cor 1.6a    in-run drift (E6): if a run's speed can rise by at most g(tau) in its first tau of
            running and its launch-speed time T_b0 falls by at most phi0 between declarations, then
            T_b0 >= phi0 G(m T_r) at each declaration keeps the true breakout time >= m T_r (and
            success <= beta), with equality when the speed follows g. Envelopes e^(a tau) and
            (1 + b tau)^k; speeds the envelope itself or step functions under it.
Recorded    the red team's switching instance (an escapable precursor, outside the assumptions):
            the per-path test admits it and it succeeds with more than beta; counted under the
            assumptions, the portable line rejects it. And a chain of fresh attempts inside a slow
            response window, outside Prop 1.7's hypothesis, beats max_p S(p). And a run on Prop
            1.6's line computed at launch speed that absorbs drift as it runs succeeds with more
            than beta, while Corollary 1.6a's line holds it.

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


# -------------------------------------------------------------------------------------------------
# Adaptive evaders. A path is (lam, tb, tresp). A plan is the evader's schedule before the first
# finding: a list of (path index, duration). Before the first finding the evader learns nothing that
# predicts findings, so every strategy is a randomised plan; after it the evader's best move is
# computed exactly below.


def portable_success(paths: list, plan: list) -> float:
    """Progress carries over at rate 1 / tb on the path worked; a finding at progress x on path p
    succeeds iff x + tresp_p / tb_min >= 1 (finish on the fastest path inside the response time)."""
    tb_min = min(tb for _, tb, _ in paths)
    h, x, total = 0.0, 0.0, 0.0
    for p, dur in plan:
        lam, tb, tr = paths[p]
        d = min(dur, (1 - x) * tb)
        e0 = max(0.0, (1 - tr / tb_min - x) * tb)
        if e0 < d:
            total += math.exp(-h) * (math.exp(-lam * e0) - math.exp(-lam * d))
        h += lam * d
        x += d / tb
        if x >= 1 - 1e-12:
            return total + math.exp(-h)
    return total


def fresh_success(paths: list, plan: list) -> float:
    """Progress resets at each stretch; a stretch completes once it has run tb. After a finding at
    elapsed e on a stretch of path p, the evader finishes that stretch if tb_p - e <= tresp_p, or
    starts a fresh stretch on the fastest path if tb_min <= tresp_p."""
    tb_min = min(tb for _, tb, _ in paths)
    h, total = 0.0, 0.0
    for p, dur in plan:
        lam, tb, tr = paths[p]
        d = min(dur, tb)
        e0 = 0.0 if tb_min <= tr else max(0.0, tb - tr)
        if e0 < d:
            total += math.exp(-h) * (math.exp(-lam * e0) - math.exp(-lam * d))
        h += lam * d
        if dur >= tb:
            return total + math.exp(-h)
    return total


def single_path(path: tuple) -> float:
    lam, tb, tr = path
    return 1.0 if tb <= tr else math.exp(-lam * (tb - tr))


def portable_bound(paths: list) -> float:
    tb_min = min(tb for _, tb, _ in paths)
    tr_max = max(tr for _, _, tr in paths)
    c_min = min(lam * tb for lam, tb, _ in paths)
    return math.exp(-c_min * max(0.0, 1 - tr_max / tb_min))


def random_plan(rng, n_paths: int, tb_ref: float, finish: bool = True) -> list:
    plan = [(rng.randrange(n_paths), tb_ref * rng.uniform(0.01, 1.5)) for _ in range(rng.randint(0, 6))]
    if finish:
        plan.append((rng.randrange(n_paths), math.inf))
    return plan


# -------------------------------------------------------------------------------------------------
# In-run drift (Corollary 1.6a). An envelope g bounds how far a run's speed can rise in its first tau
# of running; G is its integral from 0. Speeds are in units of the speed at launch, so a run's work
# is its launch-speed time T_b0.


class Envelope:
    def __init__(self, kind: str, params: tuple):
        self.kind, self.params = kind, params

    def g(self, t: float) -> float:
        if self.kind == "exp":
            (a,) = self.params
            return math.exp(a * t)
        b, k = self.params
        return (1 + b * t) ** k

    def G(self, x: float) -> float:
        if self.kind == "exp":
            (a,) = self.params
            return x if a == 0 else math.expm1(a * x) / a
        b, k = self.params
        return ((1 + b * x) ** (k + 1) - 1) / (b * (k + 1))

    def G_inv(self, y: float) -> float:
        if self.kind == "exp":
            (a,) = self.params
            return y if a == 0 else math.log1p(a * y) / a
        b, k = self.params
        return ((1 + b * (k + 1) * y) ** (1 / (k + 1)) - 1) / b


def random_envelope(rng, horizon: float) -> Envelope:
    """Drift scaled to the horizon m T_r, so the speed rises by up to e^8 (or (1 + 8)^4) over it."""
    if rng.random() < 0.5:
        return Envelope("exp", (0.0 if rng.random() < 0.1 else rng.uniform(0.01, 8.0) / horizon,))
    return Envelope("power", (rng.uniform(0.01, 8.0) / horizon, rng.uniform(0.0, 4.0)))


def step_finish(env: Envelope, steps: list, work: float) -> float:
    """Finish time of a run whose speed is u_i * g(tau_i) on [tau_i, tau_{i+1}) (the last step runs
    on), with u_i in (0, 1]. As g is nondecreasing, each step's speed is at most g on its interval."""
    done = 0.0
    for i, (tau, u) in enumerate(steps):
        c = u * env.g(tau)
        end = steps[i + 1][0] if i + 1 < len(steps) else math.inf
        if done + c * (end - tau) >= work:
            return tau + (work - done) / c
        done += c * (end - tau)
    raise AssertionError("unreachable: the last step runs on")


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

    # Adaptive evaders: Props 1.5 (adaptive), 1.7 and 1.8, and the instances outside them.
    gap_portable = 0
    for _ in range(N):
        n = rng.randint(2, 4)
        common = rng.random() < 0.3
        tb = [10 ** rng.uniform(-0.5, 1.5) for _ in range(n)]
        tb_min = min(tb)
        tr0 = tb_min * rng.uniform(0, 0.9)
        tr = [tr0 if common else (tb_min * rng.uniform(0, 0.9) if rng.random() < 0.8 else rng.uniform(0, 2 * max(tb)))
              for _ in range(n)]
        lam = [10 ** rng.uniform(-1.5, 1) for _ in range(n)]
        paths = list(zip(lam, tb, tr))
        bound = portable_bound(paths)
        for _ in range(4):
            plan = random_plan(rng, n, max(tb))
            s = portable_success(paths, plan)
            ck.ok("Prop 1.8: every strategy succeeds with at most exp(-c_min (1 - tresp_max / tb_min))",
                  s <= bound * (1 + 1e-9) + 1e-12, (paths, plan, s, bound))
            f = fresh_success(paths, plan)
            ck.ok("Prop 1.8: fresh-start progress succeeds no more often than portable progress", f <= s + 1e-12,
                  (paths, plan, f, s))
        if common and tr0 < tb_min:
            c = min(range(n), key=lambda i: lam[i] * tb[i])
            fast = min(range(n), key=lambda i: tb[i])
            x_star = 1 - tr0 / tb_min
            best = portable_success(paths, [(c, x_star * tb[c]), (fast, math.inf)])
            ck.ok("Prop 1.8: with a common tresp the bound is attained (cheapest path, then the fastest)",
                  abs(best - bound) <= 1e-9 * max(bound, 1e-300) + 1e-14, (paths, best, bound))
            beta = 10 ** rng.uniform(-3, math.log10(0.3))
            per_path = all(single_path(q) <= beta for q in paths)
            if per_path and best > beta:
                gap_portable += 1
        beta = 10 ** rng.uniform(-3, math.log10(0.3))
        portable_line = bound <= beta
        per_path = all(single_path(q) <= beta for q in paths)
        strict_scalar = tb_min >= max(math.log(1 / beta) / l for l in lam) + max(tr)
        ck.ok("Prop 1.8: the portable line implies the per-path line", (not portable_line) or per_path,
              (paths, beta))
        ck.ok("Prop 1.8: the strict scalar test implies the portable line", (not strict_scalar) or portable_line,
              (paths, beta))
    ck.note(f"Prop 1.8: in {gap_portable} instances with a common tresp every path met the line but a "
            f"strategy carrying progress across paths succeeded with more than beta")

    for _ in range(N):
        n = rng.randint(2, 4)
        tb = [10 ** rng.uniform(-0.5, 1.5) for _ in range(n)]
        tr = [min(tb) * rng.uniform(0, 1.0) for _ in range(n)]  # tresp_p <= tb_q for all p, q
        lam = [10 ** rng.uniform(-1.5, 1) for _ in range(n)]
        paths = list(zip(lam, tb, tr))
        smax = max(single_path(q) for q in paths)
        for _ in range(4):
            plan = random_plan(rng, n, max(tb))
            f = fresh_success(paths, plan)
            ck.ok("Prop 1.7: fresh-start progress and tresp <= tb give success <= max_p S(p)",
                  f <= smax * (1 + 1e-9) + 1e-12, (paths, plan, f, smax))
        p = rng.randrange(n)
        ck.ok("Prop 1.7: going straight to a path attains its S(p)",
              abs(fresh_success(paths, [(p, math.inf)]) - single_path(paths[p])) <= 1e-12, (paths, p))

    # Prop 1.9: repeated attempts
    for _ in range(N):
        n = rng.randint(1, 12)
        beta = 10 ** rng.uniform(-3, math.log10(0.3))
        s = []
        for _ in range(n):
            hz = random_hazard(rng, allow_zero_segments=False)
            tresp = rng.uniform(0, 3)
            tb = t_d(hz, beta / n) + tresp + rng.choice([0.0, rng.uniform(0, 3)])
            s.append(success(hz, tb, tresp))
        ck.ok("Prop 1.9: n attempts at beta / n each succeed together with at most beta (any dependence)",
              min(1.0, sum(s)) <= beta * (1 + 1e-9), (n, beta, s))
        ck.ok("Prop 1.9: and with independent attempts", 1 - math.prod(1 - x for x in s) <= beta * (1 + 1e-9),
              (n, beta, s))

    # Corollary 1.6a: in-run drift. The line is checked at a declaration on the launch-speed time;
    # the run launches before the next declaration, after T_b0 has fallen by f <= phi0, and its
    # speed then rises under the envelope.
    old_line_over = 0
    for _ in range(N):
        hz = random_hazard(rng)
        beta = 10 ** rng.uniform(-4, math.log10(0.5))
        tresp = rng.choice([0.0, rng.uniform(0, 3)])
        tr = t_d(hz, beta) + tresp
        if not math.isfinite(tr) or tr <= 0:
            continue
        m = rng.choice([1.0, rng.uniform(1, 4)])
        env = random_envelope(rng, m * tr)
        phi0 = rng.choice([1.0, rng.uniform(1, 3)])
        tight = rng.random() < 0.3
        tb0_decl = phi0 * env.G(m * tr) * (1.0 if tight else rng.uniform(1, 1.5))
        f = phi0 if tight or rng.random() < 0.5 else rng.uniform(1, phi0)
        tb0 = tb0_decl / f
        if rng.random() < 0.5:
            t_true = env.G_inv(tb0)  # speed follows the envelope: the worst case
        else:
            n_steps = rng.randint(1, 6)
            taus = sorted([0.0] + [rng.uniform(0, 2 * m * tr) for _ in range(n_steps - 1)])
            steps = [(tau, 1.0 if rng.random() < 0.3 else rng.uniform(0.05, 1)) for tau in taus]
            t_true = step_finish(env, steps, tb0)
            tight = False
        detail = (hz.kind, hz.params, beta, tresp, m, env.kind, env.params, phi0, f, tb0, t_true)
        ck.ok("Cor 1.6a: T_b0 >= phi0 G(m T_r) at declarations keeps the true T_b >= m T_r",
              t_true >= m * tr * (1 - 1e-9), detail)
        ck.ok("Cor 1.6a: and so success <= beta", success(hz, t_true, tresp) <= beta * (1 + 1e-9), detail)
        if tight:
            ck.ok("Cor 1.6a: a run whose speed follows g, launched at the most T_b0 can fall, attains m T_r",
                  abs(t_true - m * tr) <= 1e-9 * max(1.0, m * tr), detail)
        # Proposition 1.6's line on the launch-speed time (phi0 m T_r at the declaration, launched
        # after the full fall phi0), the same envelope.
        t_old = env.G_inv(m * tr)
        if success(hz, t_old, tresp) > beta * (1 + 1e-9):
            old_line_over += 1
    ck.note(f"Prop 1.6's line computed at launch speed, run following the envelope from the end of the "
            f"interval: success above beta in {old_line_over} of {N} random instances")

    # Recorded (E6): Proposition 1.6's line at launch speed fails against a run that absorbs drift;
    # Corollary 1.6a's line holds it. Constant hazard; T_d 0.75 and T_resp 0.25 (T_r of 1), m = 2,
    # drift a factor 6 a year, a quarter between declarations, launch at the end of the interval
    # (T_b0 has then fallen by the full phi0, so T_b0 at launch is the declared line over phi0).
    beta, td_rec, tresp_rec, m_rec = 0.05, 0.75, 0.25, 2.0
    hz = Hazard("poisson", (math.log(1 / beta) / td_rec,))
    tr = td_rec + tresp_rec
    env = Envelope("exp", (math.log(6.0),))
    phi0 = 6.0**0.25
    t_old = env.G_inv(phi0 * m_rec * tr / phi0)
    s_old = success(hz, t_old, tresp_rec)
    t_new = env.G_inv(phi0 * env.G(m_rec * tr) / phi0)
    s_new = success(hz, t_new, tresp_rec)
    ck.ok("Recorded (E6): Prop 1.6's line at launch speed, with in-run drift, succeeds with more than beta",
          s_old > beta and t_old < tr, (t_old, s_old))
    ck.ok("Recorded (E6): Corollary 1.6a's line holds the same run to m T_r and success <= beta",
          abs(t_new - m_rec * tr) <= 1e-9 and s_new <= beta, (t_new, s_new))
    ck.note(f"E6-style instance (drift factor 6 a year, m = 2, T_r = 1): Prop 1.6's launch-speed line "
            f"gives T_b {t_old:.3f} and success {s_old:.3f}; Cor 1.6a's line raises T_b0 by "
            f"{env.G(m_rec * tr) / (m_rec * tr):.2f} and gives success {s_new:.2e}")

    # Recorded instances outside the assumptions (each must behave as the text says).
    beta, tr = 0.05, 0.25
    lam_sig, tb_a, delay = 7.0, 1.0, 0.25  # declared path A: precursor at rate 7, confirmed 0.25 later
    lam_b, tb_b = 0.31, 10.0  # covert path B from scratch
    s_a = math.exp(-lam_sig * (tb_a - tr - delay))  # staying on A: success iff the precursor comes at or after 0.5
    s_b = math.exp(-lam_b * (tb_b - tr))
    td_a = delay + math.log(1 / beta) / lam_sig  # A's T_d counted from confirmations
    cut = tb_a - tr - delay
    k = lam_b * tb_b / tb_a
    switch = s_a + lam_sig * math.exp(-lam_b * (tb_b - tr)) * (-math.expm1(-(lam_sig - k) * cut)) / (lam_sig - k)
    ck.ok("Recorded (red team C1.1): with an escapable precursor the per-path test admits both paths",
          tb_a >= td_a + tr and tb_b >= math.log(1 / beta) / lam_b + tr and s_a <= beta and s_b <= beta)
    ck.ok("Recorded (red team C1.1): and switching on the precursor succeeds with more than beta",
          switch > beta, switch)
    ck.note(f"red team C1.1 instance: switching on an escapable precursor succeeds with {switch:.3f} "
            f"(beta {beta}); per path {s_a:.3f} and {s_b:.3f}")
    paths = [(lam_sig, tb_a, delay + tr), (lam_b, tb_b, tr)]  # the precursor counted as the finding
    ck.ok("Recorded (red team C1.1): counted under the assumptions, the per-path test still admits it",
          all(single_path(q) <= beta for q in paths))
    best = portable_success(paths, [(1, (1 - (delay + tr) / tb_a) * tb_b), (0, math.inf)])
    ck.ok("Recorded (red team C1.1): but the portable line rejects it, and its best strategy exceeds beta",
          portable_bound(paths) > beta and best > beta and best <= portable_bound(paths) * (1 + 1e-12),
          (portable_bound(paths), best))
    ck.note(f"red team C1.1 instance under the assumptions: covert to the midpoint, then declared, "
            f"succeeds with {best:.3f}; the portable bound is {portable_bound(paths):.3f}")
    lam1 = 0.17
    p1, p2 = (lam1, 20.0, 2.0), (4.0, 1.0, 0.25)  # slow response on path 1 exceeds path 2's T_b
    chain = single_path(p1) + (1 - single_path(p1)) * single_path(p2)  # exact, later findings counted
    ck.ok("Recorded: a fresh attempt inside a slow response window beats max_p S(p) (Prop 1.7 needs tresp <= tb)",
          max(single_path(p1), single_path(p2)) <= beta < chain and p1[2] > p2[1], chain)
    ck.note(f"chain of attempts inside a response window: {chain:.4f} against max_p S(p) "
            f"{max(single_path(p1), single_path(p2)):.4f}")
    ck.done()


if __name__ == "__main__":
    main()
