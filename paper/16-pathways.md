# Which pathways lead there, ranked

A pathway is a route by which a party's holdings come to cross the line (D4). It shortens breakout
time T_b, or it lengthens the regime's time to detect and respond, T_r, by moving work where the
channels do not see. It is necessary if no route to D1 avoids it within the horizons a regime plans
for, and sufficient if it alone takes a holding across the line (Part III). Neither can be settled
for D1 itself, since C* is a convention (D3), so every verdict below is a judgement on the proxies
it names.

## Seven pathways and two criteria

To the five candidates first proposed (recursive self-improvement, scaling, self-replication and
resource acquisition, continual learning, long-horizon autonomy) the perspectives added undeclared
compute (chips outside the registry, and work that meters miss) and distillation from a stronger
model, which moves capability at little compute, unseen by compute channels [@deepseek2025r1;
@remler2026distillation]. Inference-time search with a cheap verifier [@villalobos2023tradeoff] and
the hardware and economic loops fold into scaling, and distributed training into undeclared compute
[@rahman2026]. Theft of weights is not ranked [@nevo2024securing], though for a state it plausibly
ranks first on both criteria, moving the thief's breakout time to its victim's unseen by any compute
channel; this ranks the seven routes assessed, not every route. The criteria, fixed before the
evidence and unweighted, are how much a pathway moves the line, today and in the tail, and how hard
it is to see. The cost of a limit to useful AI sets the response, not the rank.

Table: The seven pathways, ranked by their effect on the line and how hard they are to see {#tab:pathways-ranking}

| Rank | Pathway | Necessary? | Sufficient? | Seen by | Cost of a limit | Response |
|---|---|---|---|---|---|---|
| 1 (tied) | Recursive self-improvement | No, on indirect evidence | If its gain at fixed compute exceeds 1 | Declarations, staged evaluations | Low to moderate | Restrict, narrowly |
| 1 (tied) | Undeclared compute | Only for a covert breakout | Not for D1; yes against any cap at or below [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) | Chip accounting at birth, intelligence | Low; diplomatic | Restrict at the source |
| 3 | Declared scaling | Nearly, in practice | Assumed at the agreed C* | Chip accounting, power | Low, rising | Meter |
| 4 | Distillation | No | Unknown for D1; yes for a follower near the line | Provider declarations, evaluations | Lower if keyed to the teacher | Restrict, keyed to the teacher |
| 5 | Self-replication and resource acquisition | No | Not while identity gates hold | Evaluations, identity checks | Very low | Restrict |
| 6 | Continual learning | No | No evidence | Metering, re-evaluation | Moderate | Meter |
| 7 | Long-horizon autonomy | Its competence is part of D1 | No | Evaluations, in public | High | Watch |

## The reasons

**Recursive self-improvement** is not necessary on indirect evidence:
[60%](../research/numbers.md#comp-ho-compute-share-lo) to
[95%](../research/numbers.md#comp-ho-compute-share-hi) of language-model gains from 2012 to 2023
came from compute [@ho2024algorithmic], and AI agents share credit for
[4](../research/numbers.md#dyn-nanogpt-ai-records) of
[77](../research/numbers.md#dyn-nanogpt-records) NanoGPT speedrun records [@shetty2026metrnanogpt].
It is sufficient only if its gain at fixed compute exceeds 1. E9 puts that gain at
[0.25](../research/numbers.md#e9-lm-k-fixed) ([0.42](../research/numbers.md#e9-lm-k-fixed-hi) at the
95th percentile), above 1 only if compute's share of research input is below about
[0.26](../research/numbers.md#e9-lm-share-crit), a share no data identifies, with about
[12](../research/numbers.md#dyn-ie-software-oom) orders of magnitude of room [@davidson2025three].
Its tail is the heaviest, and no physical channel sees its labour.

**Undeclared compute** exists now. The untraced pool, an assumed
[1,000,000 chips](../research/numbers.md#phys-chips-unaccounted) [@koopmanschap2026gpu], would run a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) job in about
[2.9 days](../research/numbers.md#path-covert-days-1e26), though at fixed algorithms the stock
smuggled into one country would need [555 years](../research/numbers.md#prot-pool-years-fixed) to
reach the one published breakout budget [@juniewicz2026smuggling]. A path only the historical
channels see takes [32 years](../research/numbers.md#e5-td-hist-years) to detect at E5's constant
rate and [24 years](../research/numbers.md#e5-td-weibull-years) under its Weibull fit, central
estimates under a transfer from weapons programmes; cloud compute and distillation have no measured
channel. These figures assume detection does not grow with a breakout's intensity, though a run of
days on a million chips leaves a larger footprint than the slow programmes of the record. The tie at
the top turns on that assumption, and sets an effect on T_r against one on T_b with no common scale,
so it is a judgement.

The rest rank lower. **Declared scaling** is the largest measured driver but the best seen.
**Distillation** needs a teacher, though a student can exceed it [@furlanello2018born;
@burns2023weak]. **Self-replication** is rising on simplified tasks [@aisi2025trends] but fails at
identity checks [@black2025replibench], which open weights on local hardware never meet
[@pan2024selfrep]. **Continual learning** is not one capability [@harrington2026continual], and
forgetting brakes it [@luo2023forgetting]. **Long-horizon autonomy** adds no compute or capability
of its own; it is watched and used to space the gates.

## What the grades fix

The grades on each criterion are our judgements, entered in the ledger as assumptions. Under them
[12](../research/numbers.md#claim-c12-pareto-two) of the
[21](../research/numbers.md#claim-c12-pairs) pairs are Pareto-ordered: every pathway over
long-horizon autonomy, on its grades of [0](../research/numbers.md#claim-c12-effect-lha) for effect
and [0](../research/numbers.md#claim-c12-hidden-lha) for visibility, though its competence is part
of D1; and self-improvement, undeclared compute and distillation each over continual learning and
self-replication. No pair is fixed by evidence, none orders the first three places, and no
independent grader, blind to the order, has yet graded the table. Loops each below 1 can be above 1
together [@davidson2026feedback; @burtsev2026criticality], so Part II gates the edges between
pathways too.

**Prior work.** Acquisition path analysis ranks paths by time and detection probability to place
verification where it does most good [@allen-2015-llnl]. Comparing paths to advanced AI by arrival
time [@clarke2022mtair] and modelling pathways to superintelligence with fault trees
[@barrett2016asipath] are older; undeclared compute is counted as breakout capacity
[@fithian2026hardwired], distillation and smuggling are named routes [@remler2026distillation], and
the loops are compared [@davidson2025three]. What remains (C12) is the ranking of these seven routes
together, a judgement under our grades. Bostrom's 2014 chapter on paths to superintelligence was not
opened.
