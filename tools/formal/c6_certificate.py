#!/usr/bin/env python3
"""Check the matrix statements of section C6 in research/05-formal.md.

Lemma 6.1  (a) 0 <= A <= B entrywise implies rho(A) <= rho(B); (b) rho(A) <= rho(|A|) for any real
           A; (c) for B >= 0 and w > 0, min_i (Bw)_i / w_i <= rho(B) <= max_i (Bw)_i / w_i, so the
           row sums bracket rho(B); (d) rho(B) >= max_i B_ii and rho(B) >= the geometric mean of the
           weights on any cycle.
Thm 6.2    the certificate: |K| <= U entrywise implies rho(K) <= rho(U) <= weighted row-sum bound
           <= ... for every positive w, and <= the max row sum.
Cor 6.3    cutting off-diagonal edges never takes the certificate below max_i U_ii.
Note       the smallest set of off-diagonal cuts that brings rho(U) under a target is found by
           exhaustive search; the check reports how often cutting greedily (largest single drop
           first) needs more cuts (a demonstration that the search is needed).

Spectral radii come from Gelfand's formula (tools/formal/_lib.py, self-tested against closed forms
at import). Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import itertools
import math

from _lib import Check, matvec, spectral_radius

SEED = 20261132
N = 3000
TOL = 1e-8


def random_nonneg(rng, n: int, density: float) -> list[list[float]]:
    return [[(rng.uniform(0, 1.5) if rng.random() < density else 0.0) for _ in range(n)] for _ in range(n)]


def edge_cases() -> list[list[list[float]]]:
    cases = [
        [[0.0]], [[1.3]],
        [[0.0, 0.0], [0.0, 0.0]],
        [[0.0, 1.0], [1.0, 0.0]],  # permutation, rho 1, periodic
        [[0.0, 2.0], [0.5, 0.0]],
        [[1.0, 1.0], [0.0, 1.0]],  # Jordan block
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],  # 3-cycle
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]],  # nilpotent
        [[0.5, 0.0, 0.0], [0.7, 0.2, 0.0], [0.3, 0.9, 0.4]],  # reducible, triangular
        [[0.3, 0.4], [0.4, 0.3]],  # equal row sums: rho equals the row sum
    ]
    return cases


def check_matrix(ck, rng, K: list[list[float]], U: list[list[float]], signed: bool) -> None:
    n = len(U)
    rk, ru = spectral_radius(K), spectral_radius(U)
    absk = [[abs(v) for v in row] for row in K]
    rabs = spectral_radius(absk)
    rows = [sum(row) for row in U]
    if signed:
        ck.ok("Lemma 6.1b: rho(K) <= rho(|K|)", rk <= rabs * (1 + TOL) + TOL, (K, rk, rabs))
    else:
        ck.ok("Lemma 6.1a: 0 <= K <= U implies rho(K) <= rho(U)", rk <= ru * (1 + TOL) + TOL, (K, U, rk, ru))
    ck.ok("Thm 6.2: |K| <= U implies rho(K) <= rho(U)", rk <= ru * (1 + TOL) + TOL, (K, U, rk, ru))
    ck.ok("Lemma 6.1c: min row sum <= rho(U) <= max row sum",
          min(rows) - TOL * (1 + ru) <= ru <= max(rows) * (1 + TOL) + TOL, (U, ru, rows))
    for _ in range(3):
        w = [10 ** rng.uniform(-1, 1) for _ in range(n)]
        uw = matvec(U, w)
        ratios = [uw[i] / w[i] for i in range(n)]
        ck.ok("Lemma 6.1c: weighted bounds min (Uw)_i/w_i <= rho(U) <= max (Uw)_i/w_i",
              min(ratios) - TOL * (1 + ru) <= ru <= max(ratios) * (1 + TOL) + TOL, (U, w, ru))
    ck.ok("Lemma 6.1d: rho(U) >= max_i U_ii", ru >= max(U[i][i] for i in range(n)) * (1 - TOL) - TOL, (U, ru))
    for length in range(2, n + 1):
        nodes = rng.sample(range(n), length)
        prod = math.prod(U[nodes[i]][nodes[(i + 1) % length]] for i in range(length))
        ck.ok("Lemma 6.1d: rho(U) >= geometric mean of a cycle's weights",
              ru >= prod ** (1 / length) * (1 - TOL) - TOL, (U, nodes, ru))


def main() -> None:
    ck = Check("c6_certificate", SEED)
    rng = ck.rng

    for M in edge_cases():
        check_matrix(ck, rng, M, M, signed=False)
        bumped = [[v + (0.1 if (i + j) % 2 == 0 else 0.0) for j, v in enumerate(row)] for i, row in enumerate(M)]
        check_matrix(ck, rng, M, bumped, signed=False)

    for _ in range(N):
        n = rng.randint(1, 6)
        K = random_nonneg(rng, n, rng.uniform(0.2, 1.0))
        U = [[k + (0.0 if rng.random() < 0.3 else rng.uniform(0, 0.8)) for k in row] for row in K]
        check_matrix(ck, rng, K, U, signed=False)
        # signed K with |K| <= U
        Ks = [[(u * rng.uniform(-1, 1)) for u in row] for row in U]
        check_matrix(ck, rng, Ks, U, signed=True)

    # Cor 6.3: off-diagonal cuts never go below the largest diagonal entry
    for _ in range(N // 3):
        n = rng.randint(2, 5)
        U = random_nonneg(rng, n, 0.8)
        cut = [[(U[i][j] if i == j else (0.0 if rng.random() < 0.7 else U[i][j])) for j in range(n)] for i in range(n)]
        rc = spectral_radius(cut)
        ck.ok("Cor 6.3: cutting off-diagonal edges keeps rho >= max_i U_ii",
              rc >= max(U[i][i] for i in range(n)) * (1 - TOL) - TOL, (U, cut, rc))
        ck.ok("Cor 6.3: cutting edges never raises rho", rc <= spectral_radius(U) * (1 + TOL) + TOL, (U, cut))

    # Demonstration: greedy cut sets against the smallest
    greedy_worse, tried = 0, 0
    for _ in range(300):
        n = 4
        U = [[(rng.uniform(0, 0.25) if i == j else (rng.uniform(0.1, 0.9) if rng.random() < 0.7 else 0.0))
              for j in range(n)] for i in range(n)]
        target = 0.6 * spectral_radius(U)
        if max(U[i][i] for i in range(n)) >= target:
            continue
        edges = [(i, j) for i in range(n) for j in range(n) if i != j and U[i][j] > 0]

        def rho_after(cuts: tuple) -> float:
            V = [row[:] for row in U]
            for i, j in cuts:
                V[i][j] = 0.0
            return spectral_radius(V, squarings=40)

        best = None
        for size in range(0, len(edges) + 1):
            for cuts in itertools.combinations(edges, size):
                if rho_after(cuts) <= target:
                    best = size
                    break
            if best is not None:
                break
        chosen: list = []
        while rho_after(tuple(chosen)) > target:
            remaining = [e for e in edges if e not in chosen]
            chosen.append(min(remaining, key=lambda e: rho_after(tuple(chosen + [e]))))
        tried += 1
        if len(chosen) > best:
            greedy_worse += 1
    ck.note(f"greedy cutting needed more cuts than the smallest cut set in {greedy_worse} of {tried} "
            f"random 4-loop instances")
    ck.done()


if __name__ == "__main__":
    main()
