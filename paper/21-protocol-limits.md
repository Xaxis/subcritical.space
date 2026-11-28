# One limit per mechanism

Each limit holds one mechanism below the point where it would bring a holding inside the line.
Whether it restricts or meters follows the pathway ranking; long-horizon autonomy is only watched,
and spaces the gates.

Table: The six limits: pathway, verifying channel, what it cannot see, and cost to useful AI {#tab:protocol-limits}

| Limit | Pathway (rank) | Channel | What it cannot see | Cost to useful AI |
|---|---|---|---|---|
| L1 Compute held | Declared scaling (3) | Registry, metering, sampling, re-execution | Algorithms; consumer hardware | Low: counted, not limited |
| L2 Undeclared compute | Undeclared compute (1, tied) | Accounting at birth, intelligence, insiders | The old pool; small nodes | Low for makers; high for host states |
| L3 Closed loops without human gates | Self-improvement (1, tied) | Staged runs, declarations, metered research compute | Research labour | Low to moderate |
| L4 Distillation | Distillation (4) | Provider logs, evaluations | Fraudulent accounts; open weights | Moderate |
| L5 Self-replication | Self-replication (5) | Evaluations, gate audits | Open weights on local hardware | Very low; real for open science |
| L6 Continual learning | Continual learning (6) | Metering, weight hashes, re-evaluation | Adaptation in context | Moderate |

## L1. Compute held

**Rule.** Chip-time held is counted in H100e-seconds at a reference precision, so a switch of
precision cannot game a threshold (P1): training, post-training, RL rollouts wherever they run,
teacher generation, inference and updates. Training compute per lineage above a declaration filter
triggers sealed declaration and evaluation at every checkpoint, a cheap first stage
[@heim2024thresholds]. The filter falls at the algorithmic rate at its own scale (A3). For its leak
time to exceed Part II's illustrative line of [2.0 years](../research/numbers.md#prot-line-declared), a cap needs
[1.1 OOM](../research/numbers.md#e18-need-part1-lo) to [2.9 OOM](../research/numbers.md#e18-need-part1-hi) of headroom,
[4.6 OOM](../research/numbers.md#e18-need-verifier-part1-hi) with a cheap verifier (E18, on average rates).

**From.** Declared scaling, third: the largest measured driver, and the best seen.

**Channel.** The registry, power metering [@kimpson2026dcpower], chip sampling
[@shavit2023chinchilla] and sealed declarations. It cannot see the algorithms that multiply compute,
or inference on consumer hardware [@somala2025consumergpu].

**Cost: low.** Inference is counted, not limited; the real costs are evaluation at a frontier pace
and the line's own ceiling. Counting compute across the lineage is prior work
[@sastry2024compute; @fpf-sb53-2025].

## L2. Undeclared compute

**Rule.** No AI chip may be held or operated outside the registry, and no registered chip without a
valid, logged licence. New chips get a unit identity at the supply stages with the fewest suppliers
(O3), above a technical definition of an AI chip that falls as consumer chips improve
[@bis2023advancedcomputing]. The existing stock gets a registration window checked against makers'
records, then contraband status.

**From.** Undeclared compute, tied first, which acts on T_r. Detection off the registry takes
decades (E5), so a covert path meets the line only if its reserve could not reach C* in that time:
in practice, hold no covert reserve. The registry must therefore resolve finer than the aggregate
chip floor of the run it protects, taken as a bound at full utilisation and FP8 (P4; C8, a candidate
with (b) cut). For a [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run that is
[1,600 H100e-years](../research/numbers.md#e8-chip-years-1e26-bound) of chip-time, divided by
whatever run length the adversary picks. Nothing here closes the untraced pool, and while it is open
every party fails the line through it.

**Channel.** Chip accounting at birth is the main channel that sees the aggregate; intelligence and
insiders found the covert programmes of the record [@baker2023nuclear]. Facility channels are
marginal: a run spread over one-node sites shows them one node at a time [@rahman2026].

**Cost: low for makers,** who already keep unit records; high for host states, which forgo sales and
have reversed such rules within months.

## L3. Closed research loops without human gates

**Rule.** AI-run changes to the training inputs of a frontier-scale system, one above the
declaration filter, need logged human gates whatever the loop gain: every training launch, merge
into the training stack, reallocation of research compute, batch of generated data and change to the
scoring evaluation needs a logged approval that can refuse. No threshold on K applies until E4(b)
finds a trigger that works. Gates are spaced by the agent's completed horizon-length tasks, not
hours, since a time horizon is measured in human time [@kwa2025horizon].

**From.** Recursive self-improvement, tied first, through the software loop (Y1a), the loop gain
(D2) and closure (D6).

**Channel.** Staged runs on declared checkpoints, a measurement design (C4); declarations; metered
research compute; insiders [@baker2025verifying]. The rule binds only loops the developer declares.
No physical channel sees research labour, and a meter tells training from inference
[@kimpson2026dcpower], not research inference from serving.

**Cost: low to moderate.** The limit leaves AI-assisted coding and research, close to half of
observed AI use [@handa2025aei], untouched. Its cost rises if developers automate their training
research, which is when it matters. The ban is prior work [@miotti2025narrowpath; @redlines-2025].

## L4. Distillation, keyed to the teacher

**Rule.** Bulk generation of training data from a model whose elicited capability is above a teacher
threshold, set below the line, is a licensed, logged use, counted in the student's lineage; the
student is evaluated as if it could reach or pass the teacher. The key is the teacher, because
distillation's compute is small or nil. The threshold matters only while no open-weight model
reaches the teacher, and open models trail closed ones by about
[4 months](../research/numbers.md#comp-open-closed-lag) [@edwards2026openclosed].

**From.** Distillation, fourth: a follower's T_b shortened at nil compute (A2), and a coupling
between parties (Y3).

**Channel.** Provider logs, identity checks, and evaluations that catch a capability jump without
matching compute. Chip accounting and power do not see it, and adversarial distillation already runs
through networks of fraudulent accounts.

**Cost: moderate.** Distillation is a large part of how useful AI is made cheap; from every model
below the threshold it stays free. Keying to the teacher was not searched for prior art.

## L5. Self-replication, with release control for open weights

**Rule.** No model is deployed whose elicited replication capability, measured stage by stage,
exceeds a threshold, and no weights are released above a lower release threshold. Identity checks on
compute and payment hold the gates the loop needs [@egan2023kyc; @heim2024cloud].

**From.** Self-replication and resource acquisition, fifth (Y1e). Models increasingly pass
simplified replication tasks [@aisi2025trends] but fail at know-your-customer checks and persistent
deployment [@black2025replibench]. Open weights escape those gates, and two open models have made
live copies of themselves (abstract only) [@pan2024selfrep]. Hence the release threshold.

**Channel.** Stage-by-stage replication evaluations, and audits of identity gates with seeded
requests a working gate must refuse. Nothing sees open weights on local hardware.

**Cost.** Very low for replication. The release threshold costs open science and the users of open
models above it. Both limits are prior work [@redlines-2025; @bis2025diffusion].

## L6. Continual-learning updates, counted toward compute

**Rule.** Nothing is forbidden. Update compute after deployment (weight updates, test-time training,
self-edits, RL from deployment) counts toward the lineage's training compute on any hardware, with
weight-difference hashes in the sealed log. The system is re-evaluated, with its memory and
scaffolding, when its cumulative compute reaches the next evaluation step or its score drifts by
more than a stated amount.

**From.** Continual learning, sixth (Y1d). It is metered, not banned: self-editing degrades earlier
tasks [@zweiger2025seal], and no gain has been measured for this loop, though its clock is the
fastest, [30 s](../research/numbers.md#dyn-seal-edit-s-lo) to
[45 s](../research/numbers.md#dyn-seal-edit-s-hi) a self-edit.

**Channel.** Metering, weight hashes, re-evaluation. Adaptation through context or retrieval changes
no weights, so only an evaluation with memory included sees it.

**Cost: moderate,** in accounting and re-evaluation. Counting updates is prior work
[@fpf-sb53-2025]; the drift trigger was not searched.

## The edges between loops

The protocol gates each edge between loops (Y3): money to compute (L1, L2), acquisition to compute
(L5), deployment to updates (L6), software to deployment (evaluations, D5), and transfer across
parties (L4, L5, L2).

The test is the small-gain certificate [@dashkovskiy2007smallgain], applied here as C6; regulators
have used a spectral-radius test before [@bardoscia2017pathways]. With U the matrix of jointly valid
upper confidence bounds on each loop's gain and each cross-feed, it requires rho(U) <= rho*. On Part
I's graph E11 finds a measured bound for only
[2 entries](../research/numbers.md#e11-entries-measured) of
[10 entries](../research/numbers.md#e11-entries) and none for
[5 entries](../research/numbers.md#e11-entries-unbounded).

So no certificate issues on bounds today: C6 stands as an application of prior work, with no
certificate while edges are unmeasured. Gates stand in for bounds. L1, L3 and L6
([3 gates](../research/numbers.md#e11-gates-fully-closed)) issue one for a single party; two parties
also need a cross-party gate, since their reciprocal growth bounds multiply to at least 1 and never
certify the cycle. No single limit suffices
([0 pathways](../research/numbers.md#e11-pathways-alone-honest)). Such a certificate certifies the
gates, not the gains, and holds only while their channels hold; weight theft and espionage are edges
no gate covers.

The cross-party edge has one restriction of its own, since pooled research can make subcritical
members supercritical together [@burtsev2026criticality]: research that changes scaling exponents at
frontier scale is restricted, more narrowly than in the MIRI draft [@scher2025agreement]. It costs
open science more than any other rule here.

## What is left alone

- **Narrow systems,** whatever they score, unless their outputs feed the training, code or compute
  allocation of a covered system, when the pair counts as one (F3) [@miotti2025narrowpath].
- **Data** (A4), uncountable and fungible; where it closes a loop without a gate, L4 and L3 act on that edge.
- **Capital and talent** (O1): the protocol cuts the edge from money to compute, not money.
- **Autonomy and serving capacity:** horizons space the gates and L1 counts inference.
- **Weapons-relevant science and persuasion,** governed by other instruments (F2).
- **Power,** a verification channel that no small set of suppliers controls.

None of these limits has been deployed or tested against a real adversary.
