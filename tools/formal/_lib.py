"""Shared helpers for the checks in tools/formal/ (research/05-formal.md).

Standard library only. Each check is a script `tools/formal/<claim>.py` that tests one section's
statements on seeded random instances, prints what it checked, and exits 1 on the first
counterexample (printing it), 2 if a numerical tool fails its own self-test, 0 otherwise.
"""

from __future__ import annotations

import math
import random
import sys


class Check:
    """Counts instances per statement and stops at the first counterexample."""

    def __init__(self, name: str, seed: int):
        self.name = name
        self.seed = seed
        self.rng = random.Random(seed)
        self.counts: dict[str, int] = {}
        self.notes: list[str] = []

    def ok(self, statement: str, condition: bool, detail: object = "") -> None:
        if not condition:
            print(f"{self.name}: COUNTEREXAMPLE to {statement!r}")
            print(f"  seed {self.seed}; instance: {detail}")
            sys.exit(1)
        self.counts[statement] = self.counts.get(statement, 0) + 1

    def note(self, text: str) -> None:
        self.notes.append(text)

    def done(self) -> None:
        total = sum(self.counts.values())
        print(f"{self.name}: seed {self.seed}; {total} checks, no counterexample")
        for statement, n in self.counts.items():
            print(f"  {n:>8}  {statement}")
        for text in self.notes:
            print(f"  note: {text}")
        sys.exit(0)


def tool_failure(what: str) -> None:
    print(f"numerical tool failed its self-test: {what}")
    sys.exit(2)


# -------------------------------------------------------------------------------------------------
# Small dense linear algebra.

Matrix = list[list[float]]


def matmul(A: Matrix, B: Matrix) -> Matrix:
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def matvec(A: Matrix, x: list[float]) -> list[float]:
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def transpose(A: Matrix) -> Matrix:
    return [list(col) for col in zip(*A)]


def norm_inf(A: Matrix) -> float:
    return max(sum(abs(a) for a in row) for row in A)


def spectral_radius(A: Matrix, squarings: int = 56) -> float:
    """rho(A) by Gelfand's formula, rho = lim ||A^k||^(1/k), with k = 2^squarings reached by
    repeated squaring and the scale kept in logarithms. ||A^k||^(1/k) >= rho for every k, and the
    gap closes like (c * k^(n-1))^(1/k)."""
    B = [row[:] for row in A]
    ell = 0.0  # ln of the scale divided out so far, per unit power
    weight = 1.0  # 1 / 2^j
    for _ in range(squarings):
        s = norm_inf(B)
        if s == 0.0:
            return 0.0
        B = [[b / s for b in row] for row in B]
        ell += math.log(s) * weight
        B = matmul(B, B)
        weight /= 2.0
    s = norm_inf(B)
    if s == 0.0:
        return 0.0
    return math.exp(ell + math.log(s) * weight)


def _selftest_spectral_radius() -> None:
    rng = random.Random(1)
    for _ in range(300):
        a, b, c, d = (rng.uniform(-3, 3) for _ in range(4))
        tr, det = a + d, a * d - b * c
        disc = tr * tr - 4 * det
        if disc >= 0:
            r = max(abs((tr + math.sqrt(disc)) / 2), abs((tr - math.sqrt(disc)) / 2))
        else:
            r = math.sqrt(det)
        got = spectral_radius([[a, b], [c, d]])
        if abs(got - r) > 1e-9 * max(1.0, r):
            tool_failure(f"2x2 [[{a},{b}],[{c},{d}]]: got {got}, closed form {r}")
    for _ in range(100):
        n = rng.randint(1, 6)
        T = [[(rng.uniform(-2, 2) if j >= i else 0.0) for j in range(n)] for i in range(n)]
        r = max(abs(T[i][i]) for i in range(n))
        got = spectral_radius(T)
        if abs(got - r) > 1e-7 * max(1.0, r):
            tool_failure(f"triangular {T}: got {got}, expected {r}")


_selftest_spectral_radius()


def perron(A: Matrix, left: bool = False, iters: int = 200000, tol: float = 1e-14) -> list[float]:
    """Perron vector of a positive matrix by power iteration (unique, strictly positive)."""
    M = transpose(A) if left else A
    n = len(M)
    x = [1.0] * n
    for _ in range(iters):
        y = matvec(M, x)
        s = sum(y)
        y = [v / s for v in y]
        if max(abs(u - v) for u, v in zip(x, y)) < tol:
            return y
        x = y
    return x


def log_binom_pmf(n: int, k: int, p: float) -> float:
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (
        math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
        + k * math.log(p) + (n - k) * math.log1p(-p)
    )


def binom_cdf(n: int, x: int, p: float) -> float:
    return min(1.0, sum(math.exp(log_binom_pmf(n, k, p)) for k in range(0, x + 1)))
