#!/usr/bin/env python3
"""Check the statements of section C2 in research/05-formal.md.

Thm 2.1   when every input raises (or, for C*, lowers) the left side log10 C_p(t) + J + S_v + A_p(t)
          at every t, T_b(H) = min_p T_b(p) over a box of inputs lies between its values at two
          corners: every raising input high with C* low, and the reverse.
Cor 2.2   without joint monotonicity, the termwise bound (each term at its own supremum over the
          box) is still a valid lower bound on T_b.
Cor 2.3   at fixed physical compute and constant drift, T_b = max(0, (h - J - S_v) / log10 gamma).
Failure   a drift rate that falls with scale (kappa < 0) can make more chips lengthen T_b; the
          check counts how often the two-corner interval then fails (a demonstration, not a
          counterexample to Thm 2.1, whose assumption it breaks).

The model per path: chips N growing at rate g (cumulative chip-years N (e^(g t) - 1) / g), a
utilisation u, a one-off jump J and an inference span S_v (both in orders of magnitude), and
algorithmic drift A(t) = a(N) t with a(N) = a0 + kappa * log10(N / N_ref).

Standard library only; seeded; exits 1 on a counterexample, printing it.
"""

from __future__ import annotations

import math

from _lib import Check

SEED = 20261128
N_INST = 1500
INTERIOR = 25
TMAX = 200.0


def lhs(t: float, path: dict, shared: dict) -> float:
    if t <= 0:
        return -math.inf
    n, u, g = path["N"], path["u"], path["g"]
    chip_years = n * (math.expm1(g * t) / g if g > 0 else t)
    a = shared["a0"] + shared["kappa"] * math.log10(n / shared["Nref"])
    return math.log10(chip_years * u) + shared["c0"] + shared["J"] + shared["Sv"] + a * t


def t_b_path(path: dict, shared: dict) -> float:
    target = shared["cstar"]
    if lhs(TMAX, path, shared) < target:
        return math.inf
    lo, hi = 0.0, TMAX
    for _ in range(100):
        mid = (lo + hi) / 2
        if lhs(mid, path, shared) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def t_b(paths: list[dict], shared: dict) -> float:
    return min(t_b_path(p, shared) for p in paths)


def corner(box: dict, fast: bool) -> tuple[list[dict], dict]:
    pick = (lambda lo, hi: hi) if fast else (lambda lo, hi: lo)
    paths = [{k: pick(*v) for k, v in p.items()} for p in box["paths"]]
    shared = {k: pick(*v) for k, v in box["shared"].items() if k != "cstar"}
    lo, hi = box["shared"]["cstar"]
    shared["cstar"] = lo if fast else hi
    shared["Nref"] = box["Nref"]
    return paths, shared


def interior(box: dict, rng) -> tuple[list[dict], dict]:
    paths = [{k: rng.uniform(*v) for k, v in p.items()} for p in box["paths"]]
    shared = {k: rng.uniform(*v) for k, v in box["shared"].items()}
    shared["Nref"] = box["Nref"]
    return paths, shared


def termwise_bound(box: dict) -> float:
    """inf t such that, for some path, the sum of each term's supremum over the box reaches the
    lowest C*. Valid whatever the joint dependence of the terms on the inputs."""
    lo_c = box["shared"]["cstar"][0]
    best = math.inf
    for p in box["paths"]:
        def upper(t: float) -> float:
            if t <= 0:
                return -math.inf
            n_hi, u_hi, g_hi = p["N"][1], p["u"][1], p["g"][1]
            chip_years = n_hi * (math.expm1(g_hi * t) / g_hi if g_hi > 0 else t)
            sh = box["shared"]
            a_vals = [
                sh["a0"][i] + sh["kappa"][j] * math.log10(p["N"][k] / box["Nref"])
                for i in (0, 1) for j in (0, 1) for k in (0, 1)
            ]
            return (math.log10(chip_years * u_hi) + sh["c0"][1] + sh["J"][1] + sh["Sv"][1]
                    + max(a_vals) * t)
        if upper(TMAX) < lo_c:
            continue
        lo, hi = 0.0, TMAX
        for _ in range(100):
            mid = (lo + hi) / 2
            if upper(mid) >= lo_c:
                hi = mid
            else:
                lo = mid
        best = min(best, hi)
    return best


def random_box(rng, kappa_sign: int) -> dict:
    def iv(lo: float, hi: float) -> tuple[float, float]:
        a, b = sorted((rng.uniform(lo, hi), rng.uniform(lo, hi)))
        return (a, b)

    nref = 1e3
    paths = []
    for _ in range(rng.randint(1, 4)):
        n_lo = 10 ** rng.uniform(3, 6)
        paths.append({
            "N": (n_lo, n_lo * 10 ** rng.uniform(0, 1)),
            "u": iv(0.1, 0.8),
            "g": iv(0.0, 0.6),
        })
    k = iv(0.0, 0.3) if kappa_sign >= 0 else iv(-0.6, -0.05)
    shared = {
        "c0": iv(7.0, 7.5),  # log10 of FLOP per chip-year at full utilisation, roughly
        "J": iv(0.0, 1.0),
        "Sv": iv(0.0, 1.0),
        "a0": iv(0.05, 0.6) if kappa_sign >= 0 else iv(0.8, 1.5),
        "kappa": k,
        "cstar": iv(13.0, 19.0),
    }
    return {"paths": paths, "shared": shared, "Nref": nref}


def main() -> None:
    ck = Check("c2_monotone", SEED)
    rng = ck.rng
    for _ in range(N_INST):
        box = random_box(rng, +1)
        t_fast = t_b(*corner(box, fast=True))
        t_slow = t_b(*corner(box, fast=False))
        tw = termwise_bound(box)
        for _ in range(INTERIOR):
            paths, shared = interior(box, rng)
            t = t_b(paths, shared)
            ck.ok("Thm 2.1: T_b(fast corner) <= T_b <= T_b(slow corner)",
                  t_fast <= t * (1 + 1e-9) + 1e-9 and t <= t_slow * (1 + 1e-9) + 1e-9,
                  (box, paths, shared, t_fast, t, t_slow))
            ck.ok("Cor 2.2: termwise bound <= T_b", tw <= t * (1 + 1e-9) + 1e-9, (box, tw, t))

    # Failure condition: drift falling with scale. Thm 2.1 does not apply; Cor 2.2 still must.
    broken = 0
    for _ in range(N_INST):
        box = random_box(rng, -1)
        t_fast = t_b(*corner(box, fast=True))
        t_slow = t_b(*corner(box, fast=False))
        tw = termwise_bound(box)
        outside = False
        for _ in range(INTERIOR):
            paths, shared = interior(box, rng)
            t = t_b(paths, shared)
            ck.ok("Cor 2.2 (drift falling with scale): termwise bound <= T_b",
                  tw <= t * (1 + 1e-9) + 1e-9, (box, tw, t))
            if not (t_fast <= t * (1 + 1e-9) + 1e-9 and t <= t_slow * (1 + 1e-9) + 1e-9):
                outside = True
        broken += outside
    ck.note(f"failure condition: with drift falling with scale, the two-corner interval missed "
            f"some interior T_b in {broken} of {N_INST} boxes")

    # Cor 2.3: the cap leak at fixed compute and constant drift.
    for _ in range(N_INST):
        h, j, sv = rng.uniform(0, 4), rng.uniform(0, 2), rng.uniform(0, 2)
        lg = math.log10(10 ** rng.uniform(0.05, 1.0))
        closed = max(0.0, (h - j - sv) / lg)

        def left(t: float) -> float:
            return j + sv + lg * t  # log10 C_cap subtracted from both sides

        lo, hi = 0.0, 1e3
        if left(0.0) >= h:
            numeric = 0.0
        else:
            for _ in range(200):
                mid = (lo + hi) / 2
                if left(mid) >= h:
                    hi = mid
                else:
                    lo = mid
            numeric = hi
        ck.ok("Cor 2.3: cap leak T_b = max(0, (h - J - S_v) / log10 gamma)",
              abs(closed - numeric) <= 1e-9 * max(1.0, closed), (h, j, sv, lg, closed, numeric))
    ck.done()


if __name__ == "__main__":
    main()
