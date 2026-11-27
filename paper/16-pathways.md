# Which pathways lead there, ranked

Part I closes on the practical question: which routes lead to superintelligence, and which should a
protocol restrict? A pathway is a route by which a party's holdings come to cross the line (D4). It
acts in one of two ways: it shortens breakout time T_b, through more effective compute, faster growth
of efficiency or a higher starting capability; or it lengthens the regime's time to detect and
respond, T_r, by moving work where the channels do not see. A pathway is necessary, in the sense that
matters to a regime, if no route to D1 avoids it within the horizons the regime plans for, and
sufficient if, with every other pathway held where the regime allows, it alone takes a holding across
the line. Part III states both formally. Neither can be settled for D1 itself, since C* is a
convention (D3), so every verdict below is a judgement on the proxies it names. The experiments that
have run leave the order where it was and fix none of the first three places, and nothing here has
met an adversary.

## Seven pathways and two criteria

The candidates first proposed were recursive self-improvement, unbounded scaling, self-replication
and resource acquisition, continual learning, and long-horizon autonomy. The perspectives added two.
**Undeclared compute** is chips outside the registry, and work on registered chips that declarations
and meters miss; it acts on T_r. **Distillation from a stronger model** moves capability at little
compute, unseen by any compute channel, and between parties [@deepseek2025r1;
@remler2026distillation]. Inference-time search with a cheap verifier, which trades
[3 OOM](../research/numbers.md#comp-span-cheapver-train) of training for
[6 OOM](../research/numbers.md#comp-span-cheapver-inf) of inference on a low-confidence extrapolation
[@villalobos2023tradeoff], is paid in compute and folds into scaling, as do the hardware and economic
loops. Distributed training below every per-site floor defeats the facility channels but not chip
accounting [@rahman2026], so it is how undeclared compute is used. Theft of weights was not assessed
and is left as a gap.

The ranking uses two criteria, fixed before the evidence: how much a pathway moves the line at the
margin, today and in the tail the evidence cannot exclude; and how hard it is to see, by which of the
five channels (chip accounting, power, declarations, evaluations, intelligence) and how well. The
criteria carry no weights, since the evidence is too uneven for weights to mean anything. The cost of
a limit to useful AI sets the response (restrict, meter or watch), not the rank: a first version
ranked on cost too, and the red team cut that criterion, since a cheap limit does not make a pathway
more dangerous.

Table: The seven pathways, ranked by their effect on the line and how hard they are to see {#tab:pathways-ranking}

| Rank | Pathway | Necessary? | Sufficient? | Channel that sees it | Cost of a limit | Response |
|---|---|---|---|---|---|---|
| 1 (tied) | Recursive self-improvement | No, on indirect evidence | Only if the gain at fixed compute exceeds 1; the interval spans 1 | Declarations, staged evaluations; chips see research compute only | Low to moderate, if aimed at closed-loop frontier training research | Restrict, narrowly |
| 1 (tied) | Undeclared compute | Only for a covert breakout by a metered party | Not for D1 on the one published budget; yes against any cap at or below [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) | Chip accounting at birth; intelligence and insiders | Low; the costs are diplomatic | Restrict at the source |
| 3 | Scaling of declared compute, training and inference | Not in principle; nearly in practice | Unknown; assumed at the agreed C* | Chip accounting and power | Low today, rising | Meter |
| 4 | Distillation from a stronger model | No | Unknown for D1: it starts at the teacher and can exceed it by an unmeasured uplift; yes for a follower near the line | Provider declarations; evaluations | Moderate to high if broad; lower if keyed to the teacher | Restrict, keyed to the teacher |
| 5 | Self-replication and resource acquisition | No | No, while identity gates hold | Evaluations; identity checks on compute and payment | Very low | Restrict |
| 6 | Continual learning | No | No evidence that it is | Compute metering, re-evaluation | Moderate | Meter |
| 7 | Long-horizon autonomy | Long-horizon competence is part of D1 | No | Evaluations, in public | High | Watch |

## The reasons

**Recursive self-improvement** is not necessary on indirect evidence:
[60%](../research/numbers.md#comp-ho-compute-share-lo) to
[95%](../research/numbers.md#comp-ho-compute-share-hi) of language-model gains from 2012 to 2023
came from compute [@ho2024algorithmic], and AI agents are credited with
[4](../research/numbers.md#dyn-nanogpt-ai-records) of [77](../research/numbers.md#dyn-nanogpt-records)
NanoGPT speedrun records, each alongside a human [@shetty2026metrnanogpt]. It is sufficient only if
its gain at fixed compute exceeds 1. Counting compute's growth, E9 puts that gain at
[0.25](../research/numbers.md#e9-lm-k-fixed) ([0.42](../research/numbers.md#e9-lm-k-fixed-hi) at the
95th percentile), above 1 only if compute's share of research input is below about
[0.26](../research/numbers.md#e9-lm-share-crit), a share no data identifies, with about
[12](../research/numbers.md#dyn-ie-software-oom) orders of magnitude of room [@davidson2025three]. Its
tail is the heaviest of any pathway, and no physical channel sees its labour.

**Undeclared compute** exists now. The untraced pool, of the order of
[1,000,000 chips](../research/numbers.md#phys-chips-unaccounted) [@koopmanschap2026gpu], would run a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) job in about
[2.9 days](../research/numbers.md#path-covert-days-1e26). Against D1 it is weak: the
[660,000 H100e](../research/numbers.md#org-smuggled-cum) estimated smuggled into one country
[@juniewicz2026smuggling] would need [555 years](../research/numbers.md#prot-pool-years-fixed) at
fixed algorithms to reach the one published breakout budget. On the response side it is extreme: at
E5's fitted discovery rate, [0.094/yr](../research/numbers.md#e5-hazard), a path only the historical
channels see takes [32 years](../research/numbers.md#e5-td-hist-years) to detect.

**Declared scaling** is the largest measured driver and the best seen: third as a risk, first as the
backbone the regime meters. Its premise is unsettled both ways, since E1 leaves compute's share of
capability growth between [18%](../research/numbers.md#e1-compute-share-subset-min) and
[63%](../research/numbers.md#e1-compute-share-subset-max) across samples. **Distillation** needs a
teacher: it starts from the best model a party can query, and a student can exceed its teacher
[@furlanello2018born; @burns2023weak] by an uplift no one has measured. **Self-replication**
components are rising, from under [5%](../research/numbers.md#def-replibench-2023) to over
[60%](../research/numbers.md#def-replibench-2025) on simplified tasks [@aisi2025trends], but fail at
identity checks [@black2025replibench], which open weights on local hardware never meet
[@pan2024selfrep]. **Continual learning** is not one capability [@harrington2026continual], and
forgetting brakes it [@luo2023forgetting]. **Long-horizon autonomy** adds no compute or capability of
its own; it sets how long a loop runs between gates, so it is watched and used to space them.

## What the evidence fixes

Graded on the table's entries, with equal grades wherever they do not separate two pathways,
[12](../research/numbers.md#claim-c12-pareto-two) of the [21](../research/numbers.md#claim-c12-pairs)
pairs have one pathway ahead on both criteria: every pathway over long-horizon autonomy, and
self-improvement, undeclared compute and distillation each over continual learning and over
self-replication. None orders the first three places. With cost as a third criterion the red team
counted [9](../research/numbers.md#claim-c12-pareto-three). The tie at the top sets an effect on T_r
against one on T_b, with no common scale, so it is a judgement, like every order the evidence does
not fix. The experiments are mixed. E5's test of the discovery rate could fail only on a
[12.8](../research/numbers.md#e5-memo-over-hazard)-fold error, so its passing is weak evidence. In
E11 no single pathway's gate issues the coupled-gain certificate with honest bounds
([0 pathways](../research/numbers.md#e11-pathways-alone-honest) do); the sets that issue it join
several pathways' gates. The pathways feed each other, and loops each below 1 can be above 1 together
[@davidson2026feedback; @burtsev2026criticality], so Part II gates the edges between them too.

**Label.** Prior work, applied. The method is acquisition path analysis, which ranks paths by time
and detection probability to place verification where it does most good [@allen-2015-llnl].
Comparing paths to advanced AI by arrival time [@clarke2022mtair] and modelling pathways to
superintelligence with fault trees [@barrett2016asipath] are older; undeclared compute counts as
breakout capacity in [@fithian2026hardwired], distillation and smuggling are named routes
[@remler2026distillation], and the loops are compared in [@davidson2025three]. What remains (C12) is
the ranking of these seven routes together, as a judgement with
[12](../research/numbers.md#claim-c12-pareto-two) pairs fixed by evidence. Bostrom's 2014 chapter on
paths to superintelligence was not opened, and a reader should check it. Part II derives the protocol
from the response in the table's last column.
