# One limit per mechanism

Each limit holds one mechanism below the point where it would bring a holding inside the line,
restricting or metering as the pathway ranking says.

Table: The six limits: pathway, verifying channel, what it cannot see, and cost to useful AI {#tab:protocol-limits}

| Limit | Pathway (rank) | Channel | Blind to | Cost to useful AI |
|---|---|---|---|---|
| L1 Compute held | Declared scaling (3) | Registry, metering, sampling | Algorithms; consumer hardware | Low: counted, not limited |
| L2 Undeclared compute | Undeclared compute (1, tied) | Accounting at birth, intelligence, insiders | The old pool; small nodes | Low for makers; high for host states |
| L3 Closed research loops | Self-improvement (1, tied) | Staged runs, declarations, metering | Research labour | Low to moderate |
| L4 Distillation | Distillation (4) | Provider logs, evaluations | Fraudulent accounts; open weights | Moderate |
| L5 Self-replication | Self-replication (5) | Evaluations, gate audits | Open weights | Very low; real for open science |
| L6 Continual learning | Continual learning (6) | Metering, weight hashes, re-evaluation | Adaptation in context | Moderate |

## L1. Compute held

Chip-time is counted in H100e-seconds at a reference precision across every use, training to
inference (P1), as proposed before [@sastry2024compute; @fpf-sb53-2025]. Above a declaration filter,
a lineage's training triggers sealed declaration and evaluation at every checkpoint
[@heim2024thresholds]. The filter falls at the algorithmic rate at its own scale (A3).

## L2. Undeclared compute

No AI chip may run outside the registry or without a valid, logged licence. New chips get a unit
identity at the supply stages with the fewest suppliers (O3), above a technical definition such as
export rules use [@bis2023advancedcomputing]; the existing stock gets a registration window, then
contraband status. Off the registry detection takes decades on E5's central estimates and no licence
lapses, so no party may hold a covert reserve, and the registry must resolve finer than the chip
floor of the run it protects, taken as a bound (P4):
[1,600 H100e-years](../research/numbers.md#e8-chip-years-1e26-bound) for a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run. The untraced pool, an assumed
[1,000,000 chips](../research/numbers.md#phys-chips-unaccounted), is
[1,200](../research/numbers.md#e8-pool-shrink-1e26-pause) times that floor, a point at the assumed
pool [@koopmanschap2026gpu]. Nothing here closes it, so every party fails the line through it.
Satellites see sites reliably only above [10 MW](../research/numbers.md#phys-sat-reliable)
[@clymer2025datacenter; @koopmanschap2026gpu], and a run spread over one-node sites shows one node
at a time [@rahman2026].

## L3. Closed research loops without human gates

AI-run changes to a frontier-scale system's training inputs (launches, merges, reallocations of
research compute, generated data, the scoring evaluation) need a logged human approval that can
refuse, whatever the loop gain: the prior-work ban [@miotti2025narrowpath; @redlines-2025], kept
while no trigger works (D2). Gates are spaced by completed horizon-length tasks, not hours, since a
time horizon is measured in human time [@kwa2025horizon]. The rule binds only declared loops, and
leaves AI-assisted coding and research, close to half of observed AI use [@handa2025aei], untouched.

## L4. Distillation, keyed to the teacher

Bulk training data from a model above a teacher threshold, set below the line, is a licensed, logged
use counted in the student's lineage, and the student is evaluated as if it could pass the teacher.
The key is the teacher, since distillation needs little compute (A2), unlike the EU's key on a
modifier's compute [@ec-gpai-guidelines-faq-2025]; we did not search for it as prior art. It binds
while open models trail the teacher, the best by about
[4 months](../research/numbers.md#comp-open-closed-lag) [@edwards2026openclosed].

## L5. Self-replication, with release control for open weights

No model is deployed above a replication threshold, measured stage by stage, or released above a
lower one, both prior work [@redlines-2025; @bis2025diffusion]. Models pass simplified replication
tasks more and more [@aisi2025trends] but fail at know-your-customer checks [@black2025replibench],
the gates that identity checks on compute and payment hold [@egan2023kyc; @heim2024cloud]. Open
weights escape them [@pan2024selfrep].

## L6. Continual-learning updates, counted toward compute

Update compute after deployment counts toward the lineage, with weight-difference hashes logged, as
counting rules already do [@fpf-sb53-2025], and the system is re-evaluated with its memory at each
evaluation step or on drift, a trigger not searched as prior art. It is metered, not banned:
self-editing degrades earlier tasks [@zweiger2025seal] and no gain is measured, though its clock is
the fastest, [30 s](../research/numbers.md#dyn-seal-edit-s-lo) to
[45 s](../research/numbers.md#dyn-seal-edit-s-hi) a self-edit.

## The edges between loops

Loops each subcritical can be supercritical together, so the limits above and D5's evaluations gate
each edge between them (Y3). The test is the small-gain certificate [@dashkovskiy2007smallgain],
which a regulator has applied before [@bardoscia2017pathways]: the spectral radius rho(U) of jointly
valid upper bounds on the gains and cross-feeds must not exceed omega, a threshold that leaves room
for drift within T_r (C6). Only [2 entries](../research/numbers.md#e11-entries-measured) of the
[10 entries](../research/numbers.md#e11-entries) in Part I's graph have a measured bound (E11), so
gates stand in for bounds: L1, L3 and L6 certify one party, and two parties need a cross-party gate
too. Weight theft and espionage are edges no gate covers. Because pooled research can make
subcritical members supercritical together [@burtsev2026criticality], research that changes scaling
exponents at frontier scale is restricted, more narrowly than in the MIRI draft
[@scher2025agreement].

## What is left alone

Narrow systems that feed no covered system (F3); data, except where it closes a loop without a gate
(A4); capital and talent (O1); autonomy and serving capacity, which space the gates and are counted;
weapons-relevant science and persuasion, governed by other instruments (F2); and power, a channel no
small set of suppliers controls.
