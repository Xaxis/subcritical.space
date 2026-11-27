#!/usr/bin/env python3
"""Check the statements of section C8 in research/05-formal.md.

Thm 8.1   any run of C useful operations finished within T, on chips with peaks r_j <= r_bar and
          achieved utilisations u_j(t) <= u_bar, has a chip count in r_bar units of at least
          C / (r_bar * u_bar * T), and an energy of at least C * e_min when every chip spends at least
          e_min per useful operation. Peaks are at the precision the run uses (red team C8.1): counted
          at a reference precision, with no chip faster at any trainable precision than phi_max times
          its reference peak, the count in reference units is at least C / (r_ref * phi_max * u_bar * T).
          The check also counts runs at a lower precision that undercut the floor at the reference
          peak (the case the red team found).
Lemma 8.2 a pool of at least N_min(C, T) chips (same r_bar, u_bar) can finish C within T.
Note      a floor computed at a typical utilisation u_ref < u_bar is not a bound: the check counts
          feasible runs that use fewer chips than C / (r_bar * u_ref * T) (a demonstration of why the
          correction is needed, not a counterexample to Thm 8.1).

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

from _lib import Check

SEED = 20261135
N = 20000


def main() -> None:
    ck = Check("c8_floor", SEED)
    rng = ck.rng
    beaten = low_precision = 0
    for _ in range(N):
        r_bar = rng.uniform(0.5, 2.0)
        u_bar = rng.uniform(0.3, 1.0)
        t_max = rng.uniform(0.1, 3.0)
        e_min = rng.uniform(0.5, 2.0)
        chips = []
        for _ in range(rng.randint(1, 40)):
            r = r_bar * rng.uniform(0.2, 1.0)
            # piecewise utilisation over a run no longer than t_max
            run = t_max * rng.uniform(0.1, 1.0)
            segs = rng.randint(1, 4)
            ops = 0.0
            for _ in range(segs):
                ops += r * u_bar * rng.uniform(0.0, 1.0) * run / segs
            e = e_min * rng.uniform(1.0, 3.0)
            chips.append((r, ops, e))
        c_ops = sum(o for _, o, _ in chips)
        if c_ops == 0:
            continue
        count = sum(r / r_bar for r, _, _ in chips)  # chip count in r_bar units
        energy = sum(o * e for _, o, e in chips)
        floor = c_ops / (r_bar * u_bar * t_max)
        ck.ok("Thm 8.1: chip count >= C / (r_bar u_bar T)", count >= floor * (1 - 1e-12), (r_bar, u_bar, t_max, chips))
        ck.ok("Thm 8.1: energy >= C e_min", energy >= c_ops * e_min * (1 - 1e-12), (e_min, chips))
        u_ref = u_bar * rng.uniform(0.2, 0.9)
        if count < c_ops / (r_bar * u_ref * t_max):
            beaten += 1
        # Lemma 8.2
        pool = floor * rng.uniform(1.0, 50.0)
        ck.ok("Lemma 8.2: a pool >= N_min finishes C within T", pool * r_bar * u_bar * t_max >= c_ops * (1 - 1e-12),
              (pool, floor))

        # Precision: each chip has a reference peak and runs at a precision phi times faster
        # (phi = 1 for the reference, 2 for FP8 on the H100); C counts operations at the run's precision.
        phi_max = rng.choice([2.0, 4.0])
        phi_run = rng.choice([1.0, 2.0, phi_max])
        r_ref_bar = rng.uniform(0.5, 2.0)
        chips = []
        for _ in range(rng.randint(1, 40)):
            r_ref = r_ref_bar * rng.uniform(0.2, 1.0)
            run = t_max * rng.uniform(0.1, 1.0)
            ops = sum(r_ref * phi_run * u_bar * rng.uniform(0.0, 1.0) * run / 3 for _ in range(3))
            chips.append((r_ref, ops))
        c_ops = sum(o for _, o in chips)
        if c_ops > 0:
            count_ref = sum(r / r_ref_bar for r, _ in chips)
            bound = c_ops / (r_ref_bar * phi_max * u_bar * t_max)
            ck.ok("Thm 8.1: at any trainable precision, count in reference units >= C / (r_ref phi_max u_bar T)",
                  count_ref >= bound * (1 - 1e-12), (phi_max, phi_run, chips))
            if count_ref < c_ops / (r_ref_bar * u_bar * t_max):
                low_precision += 1
    ck.note(f"a floor at a typical utilisation u_ref < u_bar was undercut by a feasible run in {beaten} of {N} instances")
    ck.note(f"a floor at the reference precision's peak was undercut by a run at a lower precision in {low_precision} "
            f"of {N} instances")
    ck.done()


if __name__ == "__main__":
    main()
