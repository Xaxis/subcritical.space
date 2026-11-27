#!/usr/bin/env python3
"""Check the licence-clock statements of section C9 in research/05-formal.md, by simulating a chip
against header-delivery strategies.

A licence names block k and ends at height H_e = k + L. The chip keeps h_max, the greatest height it
has seen (it never decreases), and a counter t of its own powered time. Time here is in units of the
mean block interval. The adversary controls power and delivery: because powering off stops the
counter while the honest chain keeps growing, and forged headers can be mined at the minimum work,
it can deliver any number of height increments at any counter time.

Rule as claimed  the chip stops once h_max >= H_e, or once it has seen no new header for longer than
                 a local bound tau (counter time).
Rule corrected   the chip stops once h_max >= H_e, or once h_max < k + rho_min * (t - t_l) - s, with t_l
                 the counter when it accepted the licence, rho_min a floor on the block rate and s a
                 slack in blocks.

Prop 9.1   under the corrected rule, whatever the delivery schedule, the chip runs under the licence
           for at most (L + s) / rho_min of counter time; with headers delivered as the honest chain
           grows and the chip always on, it stops when block H_e arrives (or earlier, if the honest
           chain falls behind the rate floor).
Counterexample (reported, not a failure): under the rule as claimed, delivering one header just
           inside each local bound runs the chip for about L * tau, a stretch of tau over the nominal L.

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261136
N = 3000
DT = 0.05


def run_corrected(L: int, rho_min: float, slack: float, schedule, rng, tmax: float) -> float:
    """Counter time the chip runs; schedule(t, h_max, need) -> new h_max (never lower)."""
    k = 0
    h_max = k
    t = 0.0
    while t < tmax:
        need = k + rho_min * t - slack  # height the rule requires at counter time t
        h_max = max(h_max, schedule(t, h_max, need))
        if h_max >= k + L or h_max < k + rho_min * t - slack:
            return t
        t += DT
    return t


def run_as_claimed(L: int, tau: float, schedule, tmax: float) -> float:
    k = 0
    h_max = k
    last_progress = 0.0
    t = 0.0
    while t < tmax:
        new = schedule(t, h_max, last_progress)
        if new > h_max:
            h_max = new
            last_progress = t
        if h_max >= k + L or t - last_progress > tau:
            return t
        t += DT
    return t


def main() -> None:
    ck = Check("c9_clock", SEED)
    rng = ck.rng
    worst_stretch_claimed = 0.0
    honest_early = 0
    honest_runs = 0
    for _ in range(N):
        L = rng.randint(5, 60)
        rho_min = rng.uniform(0.2, 0.9)  # blocks per unit counter time; the honest mean rate is 1
        slack = rng.uniform(0, 5)
        bound = (L + slack) / rho_min
        tmax = 5 * bound + 10

        kind = rng.choice(["minimal", "random", "burst", "withhold", "honest"])
        if kind == "minimal":
            def sched(t, h, need):  # just enough to keep the chip running
                return max(h, math.ceil(need))
        elif kind == "random":
            mu = rng.uniform(0, 2)
            def sched(t, h, need, mu=mu):
                n = 0
                p = mu * DT
                while rng.random() < p and n < 50:
                    n += 1
                return h + n
        elif kind == "burst":
            def sched(t, h, need):
                if rng.random() < 0.02:
                    return h + rng.randint(1, 10)
                return max(h, math.ceil(need)) if rng.random() < 0.9 else h
        elif kind == "withhold":
            def sched(t, h, need):
                return h
        else:  # honest delivery, chip always on: blocks arrive as a Poisson process of rate 1
            arrivals = []
            tt = 0.0
            while tt < tmax:
                tt += rng.expovariate(1.0)
                arrivals.append(tt)
            def sched(t, h, need, arrivals=arrivals):
                return sum(1 for a in arrivals if a <= t)
        ran = run_corrected(L, rho_min, slack, sched, rng, tmax)
        ck.ok("Prop 9.1: corrected rule runs at most (L + s) / rho_min of counter time",
              ran <= bound + DT, (kind, L, rho_min, slack, ran, bound))
        if kind == "honest":
            honest_runs += 1
            t_he = arrivals[L - 1]
            ck.ok("Prop 9.1: with honest headers the chip stops by the arrival of block H_e",
                  ran <= t_he + DT, (L, rho_min, slack, ran, t_he))
            if ran < t_he - DT:
                honest_early += 1

        # the rule as claimed, against drip-feeding just inside the local bound
        tau = rng.uniform(2, 50)  # local bound in mean block intervals
        def drip(t, h, last, tau=tau):
            return h + 1 if t - last >= tau - 2 * DT else h
        ran_c = run_as_claimed(L, tau, drip, L * tau * 2 + 10)
        worst_stretch_claimed = max(worst_stretch_claimed, ran_c / (L * tau))
        ck.ok("Counterexample check: the claimed rule is stretched to about L * tau",
              ran_c >= L * (tau - 3 * DT) - DT, (L, tau, ran_c))
    ck.note(f"rule as claimed: drip-feeding ran the chip for up to {worst_stretch_claimed:.3f} x L * tau "
            f"(L blocks nominally last L mean intervals)")
    ck.note(f"corrected rule: honest delivery stopped the chip before block H_e in {honest_early} of "
            f"{honest_runs} honest runs (the rate floor's cost to a compliant chip)")
    ck.done()


if __name__ == "__main__":
    main()
