#!/usr/bin/env python3
"""Check the statements of section C3 in research/05-formal.md.

Thm 3.1   with channels independent given the path: the product of every channel's miss is at
          most each path's miss, which is at most the evader's maximum; with path-independent rates
          the product equals the maximum iff every channel that can detect watches every path
          (or every path is certain to be caught); a mixed strategy never beats the best path.
Thm 3.2   common cause: if, given a latent Z, channels are independent with miss chances all
          nondecreasing in Z, then E[prod q_c(Z)] >= prod E[q_c(Z)], and max_z prod q_c(z) >= both.
Thm 3.3   merging: for any joint law of detection times, P(min_i D_i > t) <= min_i P(D_i > t)
          (Frechet); under positive upper-orthant dependence it is >= prod_i P(D_i > t); for common
          shocks (Marshall-Olkin) the merged rate lies between the largest rate and the sum.
Cor 3.4   with groups independent of each other and any dependence inside a group, the miss over a
          window w is at most prod_groups exp(-max rate in group * w).

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import itertools
import math

from _lib import Check

SEED = 20261129
N = 4000


def main() -> None:
    ck = Check("c3_evader", SEED)
    rng = ck.rng

    # Thm 3.1
    for _ in range(N):
        nc, npth = rng.randint(1, 6), rng.randint(1, 6)
        watch = [[rng.random() < 0.6 for _ in range(nc)] for _ in range(npth)]
        path_dep = rng.random() < 0.5
        base = [rng.uniform(0.05, 1.0) if rng.random() < 0.9 else 1.0 for _ in range(nc)]
        q = [
            [(rng.uniform(0.05, 1.0) if path_dep else base[c]) if watch[p][c] else 1.0 for c in range(nc)]
            for p in range(npth)
        ]
        miss = [math.prod(q[p]) for p in range(npth)]
        p_miss = max(miss)
        for p in range(npth):
            prod_all = math.prod(q[p][c] if watch[p][c] else (rng.uniform(0.05, 1.0) if path_dep else base[c])
                                 for c in range(nc))
            ck.ok("Thm 3.1: product over all channels <= miss(p) <= P_miss",
                  prod_all <= miss[p] * (1 + 1e-12) and miss[p] <= p_miss, (watch, q))
        if not path_dep:
            memo = math.prod(base)
            every = all(base[c] == 1.0 or all(watch[p][c] for p in range(npth)) for c in range(nc))
            ck.ok("Thm 3.1: memo product equals P_miss iff every effective channel watches every path",
                  (abs(memo - p_miss) <= 1e-12 * max(p_miss, 1e-300)) == every, (watch, base))
        # mixed strategies
        weights = [rng.random() for _ in range(npth)]
        tot = sum(weights)
        mixed = sum(w / tot * m for w, m in zip(weights, miss))
        ck.ok("Thm 3.1: a mixed strategy never beats the best path", mixed <= p_miss * (1 + 1e-12),
              (miss, weights))

    # Thm 3.2: comonotone conditional miss chances
    for _ in range(N):
        nz, nc = rng.randint(2, 8), rng.randint(2, 6)
        pz = [rng.random() + 1e-6 for _ in range(nz)]
        tot = sum(pz)
        pz = [x / tot for x in pz]
        q = []
        for _ in range(nc):
            vals = sorted(rng.uniform(0, 1) for _ in range(nz))  # nondecreasing in z
            q.append(vals)
        e_prod = sum(pz[z] * math.prod(q[c][z] for c in range(nc)) for z in range(nz))
        prod_e = math.prod(sum(pz[z] * q[c][z] for z in range(nz)) for c in range(nc))
        best = max(math.prod(q[c][z] for c in range(nc)) for z in range(nz))
        ck.ok("Thm 3.2: E[prod q_c(Z)] >= prod E[q_c(Z)] for comonotone q_c",
              e_prod >= prod_e * (1 - 1e-12) - 1e-15, (pz, q))
        ck.ok("Thm 3.2: max_z prod q_c(z) >= E[prod q_c(Z)]", best >= e_prod * (1 - 1e-12), (pz, q))

    # Thm 3.3 (Frechet), any joint law on a grid of detection times
    for _ in range(N):
        n = rng.randint(2, 4)
        grid = rng.randint(2, 5)
        cells = list(itertools.product(range(grid), repeat=n))
        w = [rng.random() ** 3 for _ in cells]
        tot = sum(w)
        w = [x / tot for x in w]
        for t in range(grid):
            joint = sum(p for cell, p in zip(cells, w) if all(d > t for d in cell))
            margs = [sum(p for cell, p in zip(cells, w) if cell[i] > t) for i in range(n)]
            ck.ok("Thm 3.3: P(min D > t) <= min_i P(D_i > t) for any joint law",
                  joint <= min(margs) + 1e-12, (cells, w, t))

    # Thm 3.3, Marshall-Olkin common shocks: positive dependence and the rate band
    for _ in range(N):
        n = rng.randint(2, 5)
        subsets = [s for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
        mu = {s: (10 ** rng.uniform(-2, 0.5) if rng.random() < 0.5 else 0.0) for s in subsets}
        if sum(mu.values()) == 0:
            continue
        lam = [sum(v for s, v in mu.items() if i in s) for i in range(n)]
        merged = sum(mu.values())  # P(min D > t) = exp(-merged * t)
        ck.ok("Thm 3.3: common-shock merged rate lies in [max rate, sum of rates]",
              max(lam) <= merged * (1 + 1e-12) and merged <= sum(lam) * (1 + 1e-12), (mu, lam, merged))

    # Cor 3.4: independent groups, common-shock dependence inside each group
    for _ in range(N):
        groups = rng.randint(1, 4)
        w_win = rng.uniform(0.1, 20)
        true_rate, bound_rate = 0.0, 0.0
        for _ in range(groups):
            n = rng.randint(1, 4)
            subsets = [s for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
            mu = {s: (10 ** rng.uniform(-2, 0.5) if rng.random() < 0.5 else 0.0) for s in subsets}
            lam = [sum(v for s, v in mu.items() if i in s) for i in range(n)]
            true_rate += sum(mu.values())
            bound_rate += max(lam)
        ck.ok("Cor 3.4: miss <= prod over groups of exp(-max rate in group * w)",
              math.exp(-true_rate * w_win) <= math.exp(-bound_rate * w_win) * (1 + 1e-12),
              (true_rate, bound_rate, w_win))
    ck.done()


if __name__ == "__main__":
    main()
