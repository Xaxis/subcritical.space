# Limitations

The protocol is a design. Nothing in it has been deployed, and nothing has been tested against a real
adversary: the red team was a helper reading the work and rerunning its scripts, not an opponent with
resources and a motive. No AI verification channel has a measured rate against a real evader. The
detection rates are transfers from simulation and other fields, and the response latencies from arms
control.

## The untraced pool

Chips made before a registry, or diverted from it, form an untraced pool, and nothing in the protocol
closes it. While it is open, its path fails the line for every party, so the line treats compliant and
non-compliant parties alike. For chip accounting to resolve a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run under a pause, the pool must shrink
[1,200](../research/numbers.md#e8-pool-shrink-1e26-pause)-fold. Part II declares the line unmet
until the pool closes, and its interim rule on declared paths is no prevention guarantee. Nothing yet
tests whether registration, an amnesty, makers' records and contraband status can close it: E22 has
run, but its envelope bounds supply from above and cannot show the pool closing. Until it closes, the
protocol binds only parties that choose to declare.

## What is not identified

- **The drift rate of algorithmic efficiency.** Across six samples of the same models, E1 finds from
  [2.6](../research/numbers.md#e1-algo-annual-subset-min) to
  [1,512](../research/numbers.md#e1-algo-annual-subset-max) a year, and in E18's backtest the leak
  past a cap comes in jumps that no constant rate follows.
- **Compute's share of research input.** E9 finds that no data identifies it, and the language-model
  loop gain at fixed compute exceeds 1 only below a share of about
  [0.26](../research/numbers.md#e9-lm-share-crit).
- **The response time.** Of findings made while a party was in its treaty,
  [25%](../research/numbers.md#e24-halt-share-never) were never followed by a halt, so history gives no
  high quantile. Lapse by default fixes only the time from a failed check or a withheld signature to a
  stop; a licensor's judgement adds a decision time that no record measures.
- **The effective compute that reaches D1.** C* is a convention whose distance from D1 nobody can
  measure. One OOM of it moves T_b by [2.3 years](../research/numbers.md#comp-years-per-oom-ho), more
  than Part II's illustrative line of [2.0 years](../research/numbers.md#prot-line-declared). In E21
  no battery compares a system with an organisation, and each saturates before t* can be seen to stop.
- **A real staged round's noise.** Every estimator E4 tried fails at the only noise level calibrated
  to data, and no real staged run, E4(b), has been made.

## Experiments that have not run

E18, E21, E22 and E23 have now run. Still unrun: E3 for C5; E4(b), E4(d) and E4(e) for C4 and C11;
E15 and E10, which could reopen C2(b); E13 and E14 for detection and the floor; E11 again with
measured edges; E16, E17, E19 and E7; E21's blocked live part; and the header check on a constrained
secure element. No experiment yet plans a drill of the licensors' decision time, measured payoffs, a
count of the pool or a test of whether it can be closed.

## What the proofs assume

Each theorem holds only under the assumptions the formal results list, among them
detection channels independent across groups, adaptive evaders at constant rates and speeds, and an
honest majority of hash power. The guarantee holds per attempt, nothing bounds the number of
attempts, and the formal checks test statements on random instances, not the proofs themselves.

## The trusted parties

Part II's table of trusted parties names at least three, no one with everything. The heaviest is the
chip maker's secure element, one anchor for every chip, whose breach breaks every on-chip channel and
the off switch at once [@chuang2026teefail]; and the states that host the chokepoints are trusted to
bind themselves, with nothing technical to limit that trust.

## What would make the program fail

Four footings carry the protocol; if one falls, it loses its ground, not just a part. The line (C1)
fails if T_r cannot be computed with an interval narrower than the T_b intervals it faces, or if a T_b
the parties compute differently collapses compliance [@barrett2012climate]. Breakout time (C2) fails if
C* and the efficiency path leave every relevant T_b interval spanning the line, forcing C* so low that
useful AI is no longer kept. Covert compute (C3 with C8) fails if the pool cannot be closed; on
today's evidence this footing does not hold, and nothing yet tests closure. The compute backbone
fails if the states hosting the stages where chips are counted do not bind themselves, which no
experiment tests. The results so far bear on the first three, and all three bear against. Against a
major power with its own chip chain the protocol offers deterrence only, so it prevents breakouts by
the parties least able to make them.
