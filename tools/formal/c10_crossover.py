#!/usr/bin/env python3
"""Check the crossover-budget statements of section C10 in research/05-formal.md.

Prop 10.1  if the score ratio kappa(t) (system over organisation, at matched budget t) is continuous
           and strictly decreasing in ln t and crosses 1 inside the tested range, the crossover t* is
           unique; interpolating ln kappa linearly in ln t between the bracketing budgets returns a t*
           inside the bracket, and the exact t* when ln kappa is linear in ln t.
           Without monotonicity, t* = sup{t : kappa(t) >= 1} on the tested budgets is the largest
           bracketing crossing; a ratio above 1 at every budget is reported as censored (t* beyond the
           range), never extrapolated.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261137
N = 20000


def crossover(budgets: list[float], ratios: list[float]):
    """Largest crossing: the last budget with ratio >= 1 followed by one below 1, interpolated in
    log-log. Returns ('censored-high', budgets[-1]) if the ratio is >= 1 at the last budget and
    ('censored-low', budgets[0]) if it is below 1 at every budget."""
    if ratios[-1] >= 1:
        return ("censored-high", budgets[-1])
    idx = [i for i in range(len(budgets) - 1) if ratios[i] >= 1 > ratios[i + 1]]
    if not idx:
        return ("censored-low", budgets[0])
    i = idx[-1]
    x0, x1 = math.log(budgets[i]), math.log(budgets[i + 1])
    y0, y1 = math.log(ratios[i]), math.log(ratios[i + 1])
    x = x0 + (0 - y0) * (x1 - x0) / (y1 - y0)
    return ("found", math.exp(x), i)


def main() -> None:
    ck = Check("c10_crossover", SEED)
    rng = ck.rng
    for _ in range(N):
        nb = rng.randint(3, 8)
        budgets = sorted(2 ** rng.uniform(0, 6) for _ in range(nb))
        if len(set(budgets)) < nb:
            continue
        kind = rng.choice(["loglinear", "monotone", "wiggly"])
        t_true = 2 ** rng.uniform(-1, 7)
        slope = rng.uniform(0.2, 1.5)
        if kind == "loglinear":
            ratios = [math.exp(-slope * (math.log(b) - math.log(t_true))) for b in budgets]
        elif kind == "monotone":
            ratios = [math.exp(-slope * (math.log(b) - math.log(t_true)) - 0.3 * math.atan(math.log(b) - math.log(t_true)))
                      for b in budgets]
        else:
            ratios = [math.exp(-slope * (math.log(b) - math.log(t_true)) + 0.8 * math.sin(3 * math.log(b)))
                      for b in budgets]
        out = crossover(budgets, ratios)
        if kind in ("loglinear", "monotone"):
            if out[0] == "found":
                _, t_star, i = out
                ck.ok("Prop 10.1: interpolated t* lies inside the bracketing budgets",
                      budgets[i] * (1 - 1e-12) <= t_star <= budgets[i + 1] * (1 + 1e-12), (budgets, ratios, out))
                ck.ok("Prop 10.1: a monotone ratio crosses 1 once on the tested budgets",
                      sum(1 for j in range(nb - 1) if (ratios[j] >= 1) != (ratios[j + 1] >= 1)) == 1, (budgets, ratios))
                if kind == "loglinear":
                    ck.ok("Prop 10.1: log-linear ratio gives the exact t*",
                          abs(math.log(t_star) - math.log(t_true)) <= 1e-9, (t_star, t_true))
            elif out[0] == "censored-high":
                ck.ok("Prop 10.1: censored high only when the true t* lies beyond the last budget",
                      t_true >= budgets[-1] * (1 - 1e-12), (budgets, t_true))
            else:
                ck.ok("Prop 10.1: censored low only when the true t* lies before the first budget",
                      t_true <= budgets[0] * (1 + 1e-12), (budgets, t_true))
        else:
            if out[0] == "found":
                _, t_star, i = out
                ck.ok("Prop 10.1: sup definition, no tested budget above t* has ratio >= 1",
                      all(r < 1 for b, r in zip(budgets, ratios) if b > t_star), (budgets, ratios, t_star))
    ck.done()


if __name__ == "__main__":
    main()
