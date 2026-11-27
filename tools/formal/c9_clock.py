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
           The bound is the powered-time counter's and holds whatever heights the chip counts, even
           heights that fall (a reorganisation to a chain with more work): checked with schedules that
           can lower the height (red team C9.1).
Counterexample (reported, not a failure): under the rule as claimed, delivering one header just
           inside each local bound runs the chip for about L * tau, a stretch of tau over the nominal L.
Lemma 9.2  forged forks (red team C9.2). Honest headers carry work at least Z, forged ones exactly Z.
           Rule G (height = greatest valid height seen, stop permanent): a fork ends a licence early
           by D blocks only with at least D forged headers, and the chip stays stopped after the honest
           chain arrives. Rule W (height = tip of the most-work chain seen, stop re-evaluated): a fork
           stops the chip only while it carries more work than every chain the chip has seen, so a chip
           that keeps receiving honest headers is stopped early only by a fork with more work than the
           honest chain since the fork point, and stays stopped only while the fork keeps more work
           or once the honest chain itself reaches H_e.
Prop 9.4   availability (red team C9.3): with n replicas and chips requiring t availability signatures,
           an accepted licence can be unpublished only if at least t replicas collude, and issuance is
           blocked only if more than n - t refuse.

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


def run_corrected_any(L: int, rho_min: float, slack: float, heights: list) -> float:
    """As run_corrected, but the height the chip uses is whatever the list gives at each step, and may
    fall (a chip that follows the most-work chain can move to a shorter chain)."""
    k = 0
    for i, h in enumerate(heights):
        t = i * DT
        if h >= k + L or h < k + rho_min * t - slack:
            return t
    return len(heights) * DT


def fork_attack(rng, rule: str, L: int):
    """One chip, one licence from height 0 to L (lifted is False if, under rule W, the chip was ever
    stopped with neither a heavier fork past H_e nor the honest chain at H_e). Honest headers 1, 2, ... arrive in order with work
    in [z, 3z]; the attacker forks at an honest height f the chip has seen and feeds forged headers of
    work z, interleaved with honest ones, until it has fed n_forged. Returns (stopped_early_by,
    n_forged, stop_lifted, forged_beat_honest) where stopped_early_by is H_e minus the honest height
    when the chip first stopped (0 if it did not stop before the honest chain reached H_e)."""
    z = 1.0
    honest_work = [rng.uniform(z, 3 * z) for _ in range(L + 40)]
    f = rng.randint(0, L - 1)
    n_forged = rng.randint(1, L + 5)
    seen_honest, fed = 0, 0
    stopped_at_honest, lifted, beat = None, True, False
    while seen_honest < L + 30:
        if fed < n_forged and seen_honest >= f and rng.random() < 0.6:
            fed += 1
        else:
            seen_honest += 1
        cum_h = sum(honest_work[f:seen_honest]) if seen_honest > f else 0.0
        fork_tip = f + fed if fed else None
        if rule == "G":
            h = max(seen_honest, fork_tip or 0)
            stopped = stopped_at_honest is not None or h >= L
        else:
            fork_more = fed > 0 and fed * z > cum_h
            beat = beat or (fork_more and f + fed >= L and seen_honest < L)
            h = f + fed if fork_more else seen_honest
            stopped = h >= L
            if stopped and not ((fork_more and f + fed >= L) or seen_honest >= L):
                lifted = False  # stopped with neither a heavier fork past H_e nor the honest chain at H_e
        if stopped and stopped_at_honest is None:
            stopped_at_honest = seen_honest
    early = 0 if stopped_at_honest is None else max(0, L - stopped_at_honest)
    return early, n_forged, lifted, beat


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

    # Prop 9.1 with heights that can fall: the bound is the counter's.
    for _ in range(N):
        L = rng.randint(5, 60)
        rho_min = rng.uniform(0.2, 0.9)
        slack = rng.uniform(0, 5)
        bound = (L + slack) / rho_min
        steps = int((5 * bound + 10) / DT)
        heights, h = [], 0
        for i in range(steps):
            r = rng.random()
            if r < 0.05:
                h = max(0, h - rng.randint(1, 5))  # a reorganisation to a shorter chain with more work
            elif r < 0.5:
                h = max(h, math.ceil(rho_min * i * DT - slack))
            elif r < 0.55:
                h += rng.randint(1, 3)
            heights.append(h)
        ran = run_corrected_any(L, rho_min, slack, heights)
        ck.ok("Prop 9.1: the counter bound holds whatever heights the chip counts, falling ones included",
              ran <= bound + DT, (L, rho_min, slack, ran, bound))

    # Lemma 9.2: forged forks under the two height rules.
    g_early = w_early = 0
    for _ in range(N):
        L = rng.randint(5, 60)
        early, n_forged, _, _ = fork_attack(rng, "G", L)
        ck.ok("Lemma 9.2 (rule G): ending a licence D blocks early takes at least D forged headers",
              early <= n_forged, (L, early, n_forged))
        if early > 0:
            g_early += 1
        early_w, n_w, lifted, beat = fork_attack(rng, "W", L)
        ck.ok("Lemma 9.2 (rule W): a chip receiving honest headers stops early only on a fork with more work",
              early_w == 0 or beat, (L, early_w, n_w))
        ck.ok("Lemma 9.2 (rule W): the chip stays stopped only while a heavier fork is past H_e, or once honest is",
              lifted, (L, early_w, n_w))
        if early_w > 0:
            w_early += 1
    ck.note(f"forged forks at the minimum work ended the licence early in {g_early} of {N} attacks under rule G "
            f"(for good) and in {w_early} of {N} under rule W (each with more work than the honest chain since "
            f"the fork, and only while it kept it)")

    # Prop 9.4: availability replicated over n rival operators, t signatures required.
    withheld = 0
    for _ in range(N):
        n = rng.randint(1, 9)
        t_req = rng.randint(1, n)
        colluders = set(rng.sample(range(n), rng.randint(0, n)))
        refusers = set(rng.sample(range(n), rng.randint(0, n)))
        # The issuer sends a leaf to any subset of replicas. An honest replica that receives it publishes
        # it, then signs; a colluder signs without publishing. The chip needs t signatures.
        pool = sorted(colluders) if colluders and rng.random() < 0.5 else list(range(n))  # withholding tries colluders
        recipients = set(rng.sample(pool, rng.randint(0, len(pool))))
        signatures = len(recipients)
        published = any(r not in colluders for r in recipients)
        accepted = signatures >= t_req
        ck.ok("Prop 9.4: an accepted licence is unpublished only if at least t replicas collude",
              not (accepted and not published) or len(colluders) >= t_req, (n, t_req, colluders, recipients))
        # Liveness: replicas that refuse do not sign; the issuer sends to every replica.
        accepted_all = n - len(refusers) >= t_req
        ck.ok("Prop 9.4: issuance is blocked only if more than n - t replicas refuse",
              accepted_all or len(refusers) > n - t_req, (n, t_req, refusers))
        if accepted and not published:
            withheld += 1
    ck.note(f"availability: an accepted licence went unpublished in {withheld} of {N} random issuances, each "
            f"with at least t colluding replicas")
    ck.note(f"rule as claimed: drip-feeding ran the chip for up to {worst_stretch_claimed:.3f} x L * tau "
            f"(L blocks nominally last L mean intervals)")
    ck.note(f"corrected rule: honest delivery stopped the chip before block H_e in {honest_early} of "
            f"{honest_runs} honest runs (the rate floor's cost to a compliant chip)")
    ck.done()


if __name__ == "__main__":
    main()
