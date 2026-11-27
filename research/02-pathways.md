# Part I, 6: The pathways, ranked by evidence

The brief asks which capabilities or architectures lead to superintelligence: for each, whether it
is necessary, sufficient or neither, how it can be measured, and what a limit on it would cost
useful AI. It asks for a ranking, and says the ranking decides what the protocol restricts. The memo
answered before the survey (`00-memo.md`). It ranked recursive self-improvement first, unbounded
scaling second, self-replication and resource acquisition third, continual learning fourth and
long-horizon autonomy fifth. This chapter closes Part I by ranking them again on the evidence the
five perspective chapters gathered.

The short version:

- **Seven pathways, not five.** Two routes the memo listed only as failure modes become pathways:
  undeclared compute and distillation from a stronger model. Inference-time search and distributed
  training fold into existing pathways.
- **Recursive self-improvement keeps first place, tied with undeclared compute.** The memo put
  self-improvement first as the route around a compute cap, which the evidence weakens. It stays
  first because it is the loop closest to closing, its gain interval spans 1, and its labour input is
  invisible to every physical channel. Undeclared compute ties with it because it lengthens the
  regime's detection time, on the historical record to decades.
- **Scaling of declared compute falls to third as a risk and rises as the backbone.** It is the
  largest measured driver of capability and the pathway the regime sees best.
- **The rest.** Distillation is fourth, self-replication fifth, continual learning sixth.
  Long-horizon autonomy is seventh, recast as the clock of closure: watched, and used to space the
  protocol's gates, not limited.

Every judgement below rests on proxies. Nobody has reached D1, the effective compute that would
reach it is a convention rather than a measurement ([D3 in the anatomy chapter](01-anatomy.md#d3-breakout-time)),
and the experiments that would test these judgements have not run. The ranking is provisional until
they do. Nothing here has been tested against an adversary.

## What a pathway is, and what would decide necessary and sufficient

A **pathway** is a route by which a party's holdings come to cross the line of D4,
T_b < m * T_r, or by which a system reaches D1 ([the anatomy chapter](01-anatomy.md)). A route can
do this in two ways.

- **It shortens breakout time T_b**: more effective compute (more chips, better algorithms), faster
  growth of efficiency (a feedback loop), or a higher starting capability (a one-off jump).
- **It lengthens the regime's time to detect and respond, T_r, for that holding**, by moving it
  where the verification channels do not see.

The memo's five candidates all act on T_b. Part I found that routes acting on T_r matter as much
([the physical chapter](011-physical.md#p4-the-footprint-and-its-floor);
[the organisational chapter](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)).

**Necessary.** A pathway is necessary if blocking it alone keeps every party's T_b longer than any
horizon the regime plans for: no route to D1 avoids it. We separate necessary in principle (no route
at all avoids it) from necessary in practice (no route avoids it within the horizons that matter to
a regime). The second is the useful one. The evidence that would decide it is capability growing by
the distance to D1 with the pathway absent. That cannot be observed, so the proxies are growth with
the pathway held back: progress at fixed compute for scaling, progress driven by human research for
self-improvement.

**Sufficient.** A pathway is sufficient if, with every other pathway held at the level the regime
allows, it alone takes a holding across the line: T_b with only that pathway open is below
m * T_r. The evidence that would decide it is, for a loop, a gain above 1 at fixed inputs measured
with a confidence bound and enough room to grow; for a supply route, a reserve larger than the
breakout budget, held for longer than the channels that see it take to find it.

Neither question can be settled for D1 itself. The effective compute that reaches D1, C*, is a
stated convention (D3), so "sufficient" means sufficient at the regime's agreed C*, and no evidence
bears on whether a given C* is right. Where a verdict below says yes or no, it is a judgement on the
proxies it names.

**The ranking criteria**, stated before the evidence:

1. **How much the pathway shortens T_b at the margin**, today and in the tail the evidence cannot
   exclude.
2. **How hard it is to see**: which of the five channels (chip accounting, power, declarations,
   evaluations, intelligence) see it, and how well.
3. **How cheaply it can be limited without harming useful AI.**

A pathway ranks higher the more it shortens T_b, the harder it is to see and the cheaper it is to
limit: a cheap limit is one the protocol should impose, and an expensive one it can only watch. Cost
also decides the kind of response (restrict, meter or watch). The criteria are not given numerical
weights, because the evidence is too uneven for weights to mean anything. Where the evidence cannot
separate two pathways, they share a rank.

The method has a precedent. Acquisition path analysis, from the IAEA's State-level concept, was
applied by Allen et al. to a hypothetical arms-cap treaty: each path carries a "Proliferation Time"
and a detection probability, and the analysis "can be used to identify where specific verification
measures might be of most benefit" [@allen-2015-llnl]. Ranking AI pathways by their effect on
breakout time and by their visibility is that method carried over to AI.

The ranking would be tested by E1 (compute against capability), E2 (autonomy horizons), E4 (loop
gain), E5 (multi-channel detection), E7 (continual learning's update compute), E8 (the footprint
floor), E10 (the training-to-inference exchange rate, with its distillation arm), E11 (the coupled
loops) and the replication reproduction-number test, all specified in the perspective chapters.
None has run.

## Which routes the memo missed

Part I surfaced four candidate routes beyond the memo's five. A route is added as a pathway only if
it reaches the line by a mechanism the others do not cover, a different channel sees it, and it
needs a different limit. Otherwise it is folded into the pathway it belongs to.

**Added: undeclared compute.** Chips outside the registry (smuggled, stockpiled, untraced legacy
stock, chips from a domestic chain outside any agreement), and work on registered chips that
declarations and meters miss. The memo named "covert chip fabrication" and "training spread across
many small clusters" among its failure modes, not as a pathway. Three things make it distinct.
Its T_r is of another order: declared material has been watched on a timescale of months, while
undeclared programmes in the record went undetected for a median of
[15 years](numbers.md#org-covert-years-median) ([O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)).
Only chip accounting at birth and intelligence see it; facility channels cannot police thresholds at
or below [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) ([P4](011-physical.md#p4-the-footprint-and-its-floor)).
And its limit is different: close the hole at the source rather than meter a declared stock. D3
already computes breakout time separately "for each undeclared path the regime cannot rule out".

Two of the candidate routes fold into it. **Diversion of chips at the edges of the supply chain** is
its main source. **Distributed training below every per-site floor** is how it is used without a
visible site: a run can be split into nodes of [29 kW](numbers.md#phys-node-power), far below the
[10 MW](numbers.md#phys-sat-reliable) at which satellites find facilities reliably, so distribution
defeats the facility channels [@rahman2026]. It does not defeat chip accounting. On registered chips
it changes nothing the registry sees, so it is not a separate route.

**Added: distillation from a stronger model.** A student trained on an existing teacher's outputs
approaches the teacher's capability at the student's own compute [@deepseek2025r1;
@busbridge2025distillation]. It is distinct for three reasons. Its compute is small or nil, so no
compute channel sees it ([the computational chapter](012-computational.md#the-combined-leak-of-a-training-cap)).
It needs a gate of its own, on access to the teacher's outputs, which no other pathway's limit
supplies. And it moves capability across parties, the cross-party edge of coupling
([the dynamical chapter](013-dynamical.md#y3-coupling)). Remler and Hayum list it as one of three
"axes" along which a party short of compute closes the gap, beside "smuggling chips, remotely
accessing foreign hardware, and producing indigenous chips" and industrial espionage, and note that
it "does not require access to the model's weights" [@remler2026distillation]. It is a ceiling
transfer: it closes the gap to the best existing model and does not by itself exceed it. Repeated
rounds of amplification and distillation form a loop, which Ord names as one path to recursive
self-improvement (abstract) [@ord2025inferencegov]; that loop is counted under self-improvement.

**Folded into scaling: inference-time search and sampling with a cheap verifier.** It is the largest
one-off leak of a training cap Part I found. Repeated sampling with a cheap verifier trades
[3 OOM](numbers.md#comp-span-cheapver-train) of training for
[6 OOM](numbers.md#comp-span-cheapver-inf) of inference, an extrapolated figure its authors give low
confidence [@villalobos2023tradeoff], and could cover the computational chapter's example headroom
at once, leaving [0 OOM](numbers.md#comp-leak-left-verifier). It is folded into scaling because it is
paid in compute, at more than one OOM of inference per OOM of training replaced, which a regime that
meters compute held charges against the same budget; because on hard questions "pretraining is
likely more effective" [@snell2024testtime]; and because its large span exists only where a cheap
verifier does. Where the verifier scores the efficiency of AI training itself, as AlphaEvolve's did
[@novikov2025alphaevolve], the search loop belongs to self-improvement.

**Also folded into scaling.** The hardware loop, AI improving chips: every gain in it must be
fabricated, and the dynamical chapter's conclusion is to count it, not limit it
([Y1b](013-dynamical.md#y1b-the-hardware-loop)). The economic loop, revenue buying compute: its gain
is unmeasured, and the edge the protocol holds is the one from money to compute
([Y1c](013-dynamical.md#y1c-the-economic-loop)).

**Not assessed: theft of weights.** It is the obvious sibling of distillation, and Remler and
Hayum's second axis is industrial espionage [@remler2026distillation]. Part I gathered no evidence
on how often weights are stolen or how well they are protected. It is named here as a gap for Part
II, not ranked.

That leaves seven pathways. The sections below take them in the order of the new ranking.

## Rank 1, tied: recursive self-improvement

AI doing the research that makes the next AI: the software loop of
[the dynamical chapter](013-dynamical.md#y1a-the-software-loop), whose gain D2 measures.

**Necessary? No, on indirect evidence.** All measured progress so far came from compute and human
research. From 2012 to 2023, [60%](numbers.md#comp-ho-compute-share-lo) to
[95%](numbers.md#comp-ho-compute-share-hi) of language-model gains came from compute
[@ho2024algorithmic]. Of [77](numbers.md#dyn-nanogpt-records) NanoGPT speedrun records, AI agents are
credited with [4](numbers.md#dyn-nanogpt-ai-records), each alongside a human, and "none reached the
deep or breakthrough end of the scale" [@shetty2026metrnanogpt]. Nothing in Part I shows a ceiling
that only AI research can pass. Nothing shows that scaling with human research reaches D1 either:
that is the C* question again.

**Sufficient? Undecided. It is sufficient only if its gain at fixed compute exceeds 1, and the
interval spans 1.** The historical return to software research in language models is
[1.89](numbers.md#dyn-r-lm) (90% interval [1.07](numbers.md#dyn-r-lm-lo) to
[3.21](numbers.md#dyn-r-lm-hi)); corrected for compute bottlenecks, the median falls to
[0.63](numbers.md#dyn-r-lm-corrected) and the interval runs from
[0.36](numbers.md#dyn-r-lm-lo-corrected) to [1.07](numbers.md#dyn-r-lm-hi-corrected)
[@ho2025experiments]. Whitfill and Wu find research compute and labour complements in one
specification ([-0.10](numbers.md#dyn-sigma-frontier-spec)), so effective research "is bounded", and
substitutes in another ([2.58](numbers.md#dyn-sigma-compute-spec)), and call the results "divergent"
[@whitfill2025bottlenecks]. Cunningham et al.'s upper-end illustration puts the core condition at
[0.58](numbers.md#dyn-loop-gain-illustration), an illustration and not their estimate
[@cunningham2026rsi]. Room to grow is about [12](numbers.md#dyn-ie-software-oom) orders of
magnitude [@davidson2025three]. If the gain held above 1 at fixed compute, the loop would be
sufficient with room to spare. Whether it does is exactly what the interval leaves open.

**How it is measured, and by whom.** Three routes, each with a different owner
([Y1a](013-dynamical.md#y1a-the-software-loop)). Historical fits use public data but describe
human-driven progress. Declarations from inside a lab are held only by the developer: in the one
independent assessment, "Anthropic changed the scope of this project midway to exclude compute
verification and instead just focus on AI R&D acceleration" [@metr-anthropic-acceleration-2026].
Staged runs at fixed compute can be run by a regime evaluator on declared checkpoints, but
small-scale returns may not transfer and an agent can depress its own result
[@gasteiger2025subtlesandbag]. The labour input is moving fast. Anthropic reports that Claude leads
[26%](numbers.md#dyn-anthropic-ai-led) of its AI R&D work, up from under
[1%](numbers.md#dyn-anthropic-ai-led-feb) in February 2026, a vendor figure [@anthropic2026pace].
METR measured a [1.9](numbers.md#dyn-metr-accel)-fold acceleration of that lab's capability index
(95% CI [1.5](numbers.md#dyn-metr-accel-lo) to [2.8](numbers.md#dyn-metr-accel-hi)), a ratio of
progress rates with inputs free, not a gain at fixed inputs.

**Which channel sees it.** Chip accounting sees research compute (experiment compute and research
inference), not the labour, and not what the compute is directed at
([the cognitive chapter](014-cognitive.md#f1-kinds-of-advantage-speed-copies-and-quality)). Power
metering at a declared site tells training from inference in simulation [@kimpson2026dcpower], not
research inference from serving. Declarations see it as far as developers report honestly.
Evaluations see capability at AI research and a lower bound on the gain, provided the agent is
elicited (D5). Intelligence and insiders reach the hundreds of employees a large project involves
[@baker2025verifying]. No physical channel sees the research labour itself.

**Cost of a limit to useful AI: low to moderate.** Software work is close to half of observed AI use
[@handa2025aei], so a limit on AI research capability as such would be costly. A limit on
closed-loop training research on frontier-scale systems, above a trigger, leaves AI-assisted coding
and research in general allowed ([F2](014-cognitive.md#f2-the-decisive-functions)).

**Place in breakout time.** At fixed compute the loop multiplies research. On D2's round-on-round
definition, if the gain held at the corrected median, the rounds would add up to
[2.7](numbers.md#path-rsi-multiplier-median) times the first round's gain, and to
[2.4](numbers.md#path-rsi-multiplier-illustration) times at Cunningham et al.'s illustration (our
arithmetic). That is an illustration: in the dynamical chapter's growth-law form a gain below 1
slows the rate without capping the level. At the corrected 95th percentile,
[1.07](numbers.md#dyn-r-lm-hi-corrected), the series does not converge at all. In the tail the
evidence cannot exclude, Davidson and Houlden's model gives [57%](numbers.md#dyn-sie-p-3yr) that full
automation of AI research compresses three years of progress into one, and
[18%](numbers.md#dyn-sie-p-10yr) that it compresses ten, modelled probabilities conditional on that
automation existing [@davidson2025sie]. Barnett and Scher: "breakout times may be very short, even
given limited compute" [@barnett2025governance]. So its expected effect on T_b today is moderate,
its tail effect is the largest of any pathway, and today's interval cannot exclude the tail.

**What would change its rank.** E4 run at two scales with both bounds of the gain below 1 would drop
it below scaling; both above 1 would put it first alone. Confirming that frontier experiments and
research labour are complements would mean a compute cap bounds it, and it would merge into scaling.
A rising AI share among deep, not shallow, research advances would raise it.

## Rank 1, tied: undeclared compute

Chips outside the registry, and work on registered chips that declarations and meters miss.

**Necessary? For a covert breakout by a party whose declared compute is metered, yes; for breakout in
general, no.** A party inside the regime that breaks out unseen must use compute the regime does not
count or misreads. A party outside it, or one that breaks out openly, needs no secret.

**Sufficient? Not for D1 on the one published breakout budget; yes for defeating any compute
threshold the protocol would set.** Epoch estimates
[660,000 H100e](numbers.md#org-smuggled-cum) smuggled into China through 2025 (90% CI
[290,000 H100e](numbers.md#org-smuggled-cum-low) to [1,600,000 H100e](numbers.md#org-smuggled-cum-high))
[@juniewicz2026smuggling], about [10%](numbers.md#org-smuggled-share-of-fe) of the hardwired-pause
group's covert evasion fleet threshold of [6.4 million H100e](numbers.md#org-hwp-fe). Its overt
breakout fleet, [180 million H100e](numbers.md#def-hwp-fleet-threshold), is
[3.9](numbers.md#def-hwp-fleet-over-global) times the global fleet it projects for the end of 2026
[@fithian2026hardwired]. On those assumed figures, undeclared compute alone does not reach D1 within
a two-year horizon. Against the thresholds a protocol would set, it is large. The untraced pool,
on the order of [1,000,000 chips](numbers.md#phys-chips-unaccounted) [@koopmanschap2026gpu], is
[47](numbers.md#phys-unaccounted-over-floor-now) times the aggregate chip floor of a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run today and
[250](numbers.md#phys-unaccounted-over-floor-pause) times it at a pause's rational run length. Read as
H100e at the reference utilisation, it would run [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) in
about [2.9 days](numbers.md#path-covert-days-1e26) (our arithmetic). Distillation and algorithmic
progress lower the compute it needs further.

**How it is measured, and by whom.** It is estimated, never counted. The smuggling estimate rests on
an assumed detection rate of [25%](numbers.md#org-diversion-detect) of diversion cases
[@juniewicz2026smuggling], and outside estimates of one state-backed maker's 2025 output differ by a
factor of [4.1](numbers.md#org-huawei-spread) [@zafar2025kessler; @patel2025ascend; @pan2026idc]. On
registered chips, a power trace alone cannot exclude hidden computation of up to
[1.16](numbers.md#phys-beta-worst) times declared capacity, falling to
[0.059](numbers.md#phys-beta-restricted) only with re-execution of declared work (abstract only)
[@kimpson2026b].

**Which channel sees it.** Chip accounting at birth is the only channel that sees the aggregate
([P4](011-physical.md#p4-the-footprint-and-its-floor)). Intelligence and insiders found the covert
programmes of the record: "The IAEA identifies suspect locations mainly through voluntary tips from
national intelligence agencies" [@baker2023nuclear], and employees revealed frauds
[2.9](numbers.md#org-fraud-quitam-ratio) times as often where rewards apply [@dyck2007whistle].
Satellites see large sites and construction, and denial helps them: a party cut off from the leading
edge needs about [2.5](numbers.md#org-denial-power-multiplier) times the power per unit of compute
[@cottier2026horinger]. What cannot see it: thermal imaging, grid paperwork below
[5 MW](numbers.md#phys-utility-study), satellites for nodes of tens of kilowatts, declarations and
evaluations by construction, and challenge inspections, of which [0 requests](numbers.md#org-cwc-ci-requests)
have been made under the Chemical Weapons Convention since 1997 [@opcw-ec109-dg22].

**Cost of a limit to useful AI: low.** Registering chips at birth uses unit records the makers
already keep ([O3](015-organisational.md#o3-chokepoints)). The costs fall elsewhere. The states that
host the chokepoints must bind their own export decisions, and one reversed a rule within months;
"states capable of chip production could still gradually exit the agreement unilaterally by resuming
production of non-flexHEG chips" [@petrie2025flexheg1]. And a low cap on unmonitored clusters, of the
order of MIRI's [16 H100e](numbers.md#phys-miri-cluster-cap) [@scher2025agreement], reaches research
labs and small firms.

**Place in breakout time.** It acts mostly on T_r. At the historical discovery rate of
[0.08/yr](numbers.md#org-covert-hazard), the mean wait for discovery is
[12 years](numbers.md#path-covert-mean-years), and bringing the miss chance down to
[5%](numbers.md#def-prevent-beta) takes [37 years](numbers.md#path-covert-td-prevent) (our
arithmetic, on a crude rate from a convenience sample of old channels). The memo's placeholder
channel needed [2.5 yr](numbers.md#def-placeholder-detect-time). On these crude figures, for
compute that only the historical channels see, D4 is in effect unsatisfiable: any undeclared holding
whose breakout time is shorter than decades is weapons-grade. That is why the protocol cannot rely on
finding covert work after it starts and must keep the covert reserve small
([O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)). On the T_b
side, it adds a reserve to every party's holdings: D3 should count the untraced pool as held by the
worst-placed party.

**Why it ties with self-improvement.** Self-improvement's effect on T_b is larger in the tail but
uncertain; undeclared compute exists now, with a moderate effect on T_b and an extreme one on T_r.
Both are hard to see, and both can be limited at little cost to useful AI. The evidence does not say
which matters more.

**What would change its rank.** Chip accounting with a resolution finer than the aggregate floor at
the pause run length would drop it; so would E5 fitting a discovery rate near the memo's placeholder,
[15](numbers.md#org-memo-to-history) times the historical one. Leading-edge chips made at volume
outside any agreement (first chips targeted for [2028](numbers.md#org-china-euv-target), other
experts say [2030](numbers.md#org-china-euv-expert), on unnamed-source reporting) would raise it, as
would decentralised training, growing about [20](numbers.md#org-decentral-growth) times a year by one
author's estimate, closing its [1,000](numbers.md#org-decentral-gap)-fold gap to the frontier
[@sevilla2025decentralized].

## Rank 3: scaling of declared compute, training and inference

More compute held and used by a declared party: training, post-training, RL rollouts and inference,
including inference-time search.

**Necessary? Not in principle; nearly so in practice at the frontier.** The memo said "No,
algorithms substitute". The evidence weakens that. Training compute explains
[80%](numbers.md#comp-mertens-frontier-share-lo) to [90%](numbers.md#comp-mertens-frontier-share-hi)
of performance differences at the frontier [@mertens2026secretsauce]. Of a claimed
[22,000](numbers.md#dyn-algo-gain-claimed)-fold efficiency gain from 2012 to 2023, less than
[100](numbers.md#dyn-algo-gain-small-max)-fold reproduces at small compute, because the largest gains
show only at scale (abstract only) [@gundlach2025origin]. The steelman for the memo is real: the
Rosetta decomposition attributes only [45%](numbers.md#comp-rosetta-compute-share) of frontier
capability growth to compute, with a range of [9%](numbers.md#comp-rosetta-compute-share-lo) to
[82%](numbers.md#comp-rosetta-compute-share-hi) across families [@ho2025rosetta], and about
[50%](numbers.md#dyn-innovations-under-cap) of catalogued pretraining innovations were feasible under
very stringent caps [@barnett2025innovation]. A cap does leak: a capped party closes the example
headroom in [2.2 years](numbers.md#comp-leak-years-rosetta) to
[9.3 years](numbers.md#comp-leak-years-small)
([the computational chapter](012-computational.md#the-combined-leak-of-a-training-cap)). Algorithms
substitute over years at the cap's own scale, not at the frontier's pace. And every pathway consumes
compute in some amount.

**Sufficient? Unknown.** Capability rises with compute at a stable slope,
[0.39 units per OOM](numbers.md#comp-rosetta-per-oom) on the Rosetta scale [@ho2025rosetta].
Whether that reaches D1 depends on C*. The one published breakout budget,
[2e+29 FLOP](numbers.md#def-hwp-breakout-budget), is an assumption [@fithian2026hardwired]. The
regime has to treat scaling as sufficient at whatever C* it agrees.

**How it is measured, and by whom.** The developer knows its training compute exactly; outsiders
know held compute through the registry. About [13.6 million H100e](numbers.md#org-sold-2025) was sold
in 2025 [@epoch2026chipsales], and more than [70%](numbers.md#org-hyperscaler-share) of the stock
sits with five owners [@you2026chipowners]. Inference counts only if the regime meters compute held,
not training compute per run; RL rollouts count only if they are charged as training, and
distributed RL already runs its rollouts on a permissionless swarm [@primeintellect2025intellect2].

**Which channel sees it.** It is the best-seen pathway: chip accounting, on-site power metering
(which caught [96%](numbers.md#phys-meter-detect) of undisguised training runs against a declared
inference workload, on simulated power) [@kimpson2026dcpower], declarations, and imagery of the
largest sites, which are built in public view. What cannot see it: any channel for the algorithms
that multiply it, and chip accounting for inference on unregistered hardware, where open models on
one consumer GPU match the frontier within [6 months](numbers.md#comp-consumer-lag-lo) to
[12 months](numbers.md#comp-consumer-lag-hi) [@somala2025consumergpu].

**Cost of a limit to useful AI: low today, rising.** The memo's answer holds at a line above the
frontier. But the line is a time, so as breakout times shrink more holdings fall under it, and a
conservative C* or a fast efficiency path moves the line toward caution
([D3](01-anatomy.md#d3-breakout-time)). Counting inference costs little; limiting it, as copies
times speed, would cost useful AI heavily ([P1](011-physical.md#p1-the-compute-budget)).

**Place in breakout time.** It is the largest measured driver. Frontier training compute has grown
[5](numbers.md#comp-frontier-compute-growth) times a year [@epoch2026trends], one OOM every
[1.4 years](numbers.md#comp-years-per-oom-frontier), against
[2.3 years](numbers.md#comp-years-per-oom-ho) per OOM of algorithmic drift at Ho et al.'s central
rate [@ho2024algorithmic]. AI compute sold grew [2.67](numbers.md#org-sold-growth) times in a year.
Yet overt breakout at the hardwired-pause group's assumed budget needs
[13 years](numbers.md#org-fb-years-of-sales) of 2025's sales, and efficiency gains of
[57%](numbers.md#def-hwp-efficiency-growth) a year would lift one state's overt capacity from
[20%](numbers.md#def-hwp-us-capacity-before) to [53%](numbers.md#def-hwp-us-capacity-after) of that
threshold [@fithian2026hardwired]. Inference adds a one-off jump: about
[1 OOM](numbers.md#comp-tradeoff-typical-oom) per technique without a cheap verifier, up to
[3 OOM](numbers.md#comp-span-cheapver-train) with one [@villalobos2023tradeoff]. Post-training adds
[0.7 OOM](numbers.md#comp-oneoff-lo-oom) to [1.3 OOM](numbers.md#comp-oneoff-hi-oom)
[@davidson2023enhancements]. For a placeholder response time of [1 yr](numbers.md#comp-response-years),
a cap needs [1.5 OOM](numbers.md#comp-headroom-needed-small) to
[2.1 OOM](numbers.md#comp-headroom-needed-rosetta) of headroom, and about
[3.4 OOM](numbers.md#comp-headroom-needed-verifier) where a cheap verifier exists.

**Why third.** It moves T_b most, but the regime sees it best, meters it continuously and computes
the line from it. As a risk the protocol might miss, it ranks below the two that are hard to see. As
architecture it is first: the backbone the other limits stand on.

**What would change its rank.** E1 finding that the Rosetta reading holds at the cap's own scale,
with algorithms carrying most of the growth, would lower it and raise self-improvement. E10 finding
that inference techniques stack would raise it. Frontier-relevant training on unregistered consumer
hardware would move part of it into undeclared compute.

## Rank 4: distillation from a stronger model

Training a model on the outputs of a stronger one, across firms or across parties.

**Necessary? No.** Every frontier model so far was trained without a stronger teacher.

**Sufficient? Not for D1: it cannot exceed its teacher. Yes for moving a follower across the line
when a teacher near the line is reachable.** It raises the follower's starting capability in D3 to
roughly the teacher's. A 32B model distilled from DeepSeek-R1 scores
[72.6%](numbers.md#comp-r1-distill-32b) on AIME 2024, against
[47.0%](numbers.md#comp-r1-rl-32b) for large-scale RL on the same base, a gap of
[25.6 pp](numbers.md#comp-r1-distill-gap); the distilled 7B model reaches
[55.5%](numbers.md#comp-r1-distill-7b) [@deepseek2025r1]. With an existing teacher, distillation
beats supervised learning up to a compute level that grows with student size (abstract)
[@busbridge2025distillation], and it can bring in reasoning patterns the student did not have
[@yue2025rlvr]. It propagates: "Once one Chinese developer has extracted and internalized these
gains, other Chinese developers can in turn freely distill from those models"
[@remler2026distillation].

**How it is measured, and by whom.** Part I found no compute-equivalent figure for it, so the model
gives it none ([the computational chapter](012-computational.md#a2-the-exchange-rate-between-training-and-inference-compute)).
E10's distillation arm would convert its gain into compute-equivalent training on a family's own
scaling curve. Access is measured where outputs leave: by the providers' logs.

**Which channel sees it.** Declarations by model providers (output-access logs, identity checks at
the interface); evaluations at declared checkpoints, which catch a capability jump without matching
compute; intelligence. Chip accounting and power do not see it, because its compute is small.
Remler and Hayum report that adversarial distillation campaigns "are engineered to evade detection",
through networks of fraudulent accounts [@remler2026distillation]. Outputs are information, and
policing their use for training looks more like the Biological Weapons Convention than like nuclear
safeguards.

**Cost of a limit to useful AI: moderate to high if broad, lower if keyed to the teacher.** Training
small models on large models' outputs is a large part of how useful AI is made cheap. A gate has to
sit at the teacher's capability, near the line, and not on distillation in general. The EU already
treats a downstream modifier using more than [33%](numbers.md#comp-eu-modifier-share) of the original
training compute as a provider [@ec-gpai-guidelines-faq-2025]; distillation needs a rule keyed to
the teacher instead.

**Place in breakout time.** It cuts a follower's T_b to roughly the time it takes to distil. The best
open-weight models trail closed ones by about [4 months](numbers.md#comp-open-closed-lag)
[@edwards2026openclosed], which bounds how long a capability now stays with the party that made it.
It is also the cross-party edge of coupling: in Burtsev's scenario, blocs that are each subcritical
reach a network reproduction number of [1.15](numbers.md#dyn-burtsev-network-rho) through transfer
[@burtsev2026criticality].

**What would change its rank.** E10's distillation arm finding a gain worth well over the
[1 OOM](numbers.md#comp-heim-buffer-oom) post-training buffer would raise it; a workable gate on
teacher outputs would lower it. Release of weights near the line would make it moot, since transfer
would then be free and the release decision would govern instead.

## Rank 5: self-replication and resource acquisition

Copies of a model running outside its operator's control and acquiring compute and money: the
acquisitive loop ([Y1e](013-dynamical.md#y1e-the-acquisitive-loop)).

**Necessary? No.**

**Sufficient? No, while the gates hold.** The loop is bounded by the compute it can reach. On UK
AISI's evaluations, success rose from under [5%](numbers.md#dyn-aisi-rep-2023) in early 2023 to over
[60%](numbers.md#dyn-aisi-rep-2025) by summer 2025, on "simplified versions" of the tasks, and models
are "currently unlikely to succeed in real-world conditions" [@aisi2025trends]. They fail at
know-your-customer checks and robust persistent deployment [@black2025replibench]. Open weights
escape that gate: Llama3.1-70B-Instruct and Qwen2.5-72B-Instruct made a live copy of themselves in
[50%](numbers.md#dyn-fudan-llama) and [90%](numbers.md#dyn-fudan-qwen) of trials, on a shorter chain
than RepliBench's, read in abstract only [@pan2024selfrep].

**How it is measured, and by whom.** Stage by stage in sandboxed evaluations, which evaluators can
run; the real-world removal rate is unknown.

**Which channel sees it.** Evaluations of replication capability, and audits of the identity gates on
compute and payment. Chip accounting sees the compute it reaches only if that compute is registered.
Nothing sees open weights on local hardware, and splitting a workload across providers, as money
launderers split transactions, evades per-provider checks [@heim2024cloud; @krys2025distributed].

**Cost of a limit to useful AI: very low.**

**Place in breakout time.** Small today. If its gates opened it would be the fastest loop
([Y2](013-dynamical.md#y2-runaway-versus-saturation)). Inside a regime it reduces to undeclared
compute that a system acquires for itself. In 2023, evaluations could not rule out autonomous
replication after an effective compute scale-up of about [100](numbers.md#dyn-ara-scaleup) times
without intermediate evaluations [@kinniment2023ara], which is the case for evaluating at declared
checkpoints.

**What would change its rank.** Any real-world success at the identity gates would raise it sharply.
The replication reproduction-number test would show which stage dominates.

## Rank 6: continual learning

A deployed model updating its own weights or memory from experience: the experiential loop
([Y1d](013-dynamical.md#y1d-the-experiential-loop)).

**Necessary? No.** Capability has grown without it.

**Sufficient? No evidence that it is.** "Continual learning is not one capability"
[@harrington2026continual]. Self-editing works in small models: SEAL raised knowledge incorporation
from [33.5%](numbers.md#dyn-seal-squad-base) to [47.0%](numbers.md#dyn-seal-squad), but performance on
earlier tasks "gradually declines as the number of edits increases" [@zweiger2025seal]. No gain for
this loop has been measured. Its capacity to improve rises with pretraining compute through the
generation-verification gap [@song2024gap], so a compute cap partly bounds it.

**How it is measured, and by whom.** Update compute, weight differences between attested
checkpoints, and re-evaluation over time, all by whoever runs the hardware.

**Which channel sees it.** Chip accounting and metering see update compute on registered hardware;
declarations of attested weight hashes see the updates; re-evaluation sees the drift. Nothing sees
adaptation through context or retrieval, which changes no weights, except an evaluation of the
deployed system with its memory included. Locally held weights, and RL rollouts on unregistered
hardware, escape the compute channels.

**Cost of a limit to useful AI: moderate.** Continual learning is valuable, which is why the memo
chose accounting and re-evaluation over a ban; the evidence supports that choice.

**Place in breakout time.** It turns a deployed fleet into a training run whose compute adds to the
lineage's training compute. Its effect is unmeasured and small on present evidence, though its clock
is the fastest of the loops, [30 s](numbers.md#dyn-seal-edit-s-lo) to
[45 s](numbers.md#dyn-seal-edit-s-hi) a self-edit.

**What would change its rank.** E7 measuring a gain near 1, or update compute crossing a training
threshold quickly, would raise it. Evidence that the hazardous form runs through context rather than
weights would move its channel from compute to evaluation.

## Rank 7: long-horizon autonomy

AI working reliably, unattended, on long tasks.

**Necessary? Long-horizon competence is part of what D1 measures; unattended operation is necessary
only for a loop to close without a human gate.** D1 compares a system with an organisation at matched
wall-clock time, and at long budgets humans still win: on RE-Bench, agents scored
[4](numbers.md#dyn-rebench-agent-2h) times human experts at two hours, and the experts
[2](numbers.md#dyn-rebench-human-32h) times the top agent at 32 hours [@wijk2024rebench]. A system
supervised at gates can have long-horizon competence without running unattended. Unattended
operation across the gaps between gates is what lets self-improvement or replication close.

**Sufficient? No.** It adds no compute and no capability of its own.

**How it is measured, and by whom.** Publicly, by time horizons. The 50% horizon has doubled every
[129 days](numbers.md#dyn-horizon-doubling) since 2023 [@metr2026thdata], against
[207 days](numbers.md#dyn-horizon-doubling-2019) from 2019 to 2025 [@kwa2025horizon]. The latest
entry's 50% horizon is about [17 hours](numbers.md#dyn-horizon-p50-hours), its 80% horizon about
[3 hours](numbers.md#dyn-horizon-p80-hours); the ratio, [5.6](numbers.md#dyn-horizon-ratio), is above
the [3](numbers.md#dyn-ord-ratio) a constant hazard predicts [@ord2025halflife]. The long end is thin:
[5](numbers.md#cog-th11-long-baselined) of [31 tasks](numbers.md#cog-th11-long-tasks) over eight hours
have a human baseline.

**Which channel sees it.** Evaluations, well, and in public. No other channel is needed.

**Cost of a limit to useful AI: high.** Autonomy is much of what makes AI useful. Gates spaced to the
80% horizon must move apart as horizons grow or they start to bind on useful work. If the 80% horizon
grew at the 50% horizon's rate, it would reach about
[22 hours](numbers.md#path-horizon-p80-next-year) in a year (our arithmetic).

**Place in breakout time.** No direct effect. It sets the clock of closure: how long a loop can run
between human-held gates. One model puts one-month 80% horizons
[7 years](numbers.md#dyn-horizon-compute-delay) later than trend under a compute slowdown, but it
assumes horizon growth proportional to compute growth, which rules out a software-only singularity
by construction [@whitfill2025horizon].

**What would change its rank.** If horizons decoupled from compute, or the gap between the 50% and
80% horizons shrank, closure would get easier. That would raise the loops it enables, not autonomy
itself.

## The ranking

The table keeps the memo's columns and adds four. "Rank now" orders the pathways by the three
criteria stated at the start; "the channel that sees it" names the channel the protocol relies on
first.

| Pathway | Necessary? | Sufficient? | How measured | Cost of a limit to useful AI | Rank now | Memo's rank | What moved it | The channel that sees it |
|---|---|---|---|---|---|---|---|---|
| Recursive self-improvement | No, on indirect evidence | Only if the gain at fixed compute exceeds 1; the interval spans 1 | D2: staged runs at fixed compute, lab declarations, matched-budget AI-research battery | Low to moderate if aimed at closed-loop frontier training research | 1 (tied) | 1 | Weakened as the route around a compute cap (compute complements research); kept as the loop closest to closing, with its labour invisible | Declarations and staged evaluations; chip accounting for research compute only |
| Undeclared compute | Only for a covert breakout by a metered party | Not for D1 on the published budget; yes against any cap at or below 1e26 FLOP | Estimated: smuggling models, untraced pool, outside output estimates | Low; the costs are diplomatic, and a low cap on unmonitored clusters | 1 (tied) | not ranked (a failure mode) | The registry's hole exceeds the floor of any cap; covert work went undetected for years | Chip accounting at birth; intelligence and rewarded insiders |
| Scaling of declared compute, training and inference | Not in principle; nearly in practice at the frontier | Unknown; assumed at the agreed C* | Chip registry, power metering, declarations | Low today at a line above the frontier; rises as breakout times shrink | 3 | 2 | Stronger as the backbone (compute explains most frontier differences); lower as a risk because it is best seen; inference folded in | Chip accounting and power |
| Distillation from a stronger model | No | No for D1 (bounded by the teacher); yes for a follower near the line | Output-access logs; E10 distillation arm | Moderate to high if broad; lower if keyed to the teacher | 4 | not listed | Moves capability at nil compute and across parties | Provider declarations; evaluations at checkpoints |
| Self-replication and resource acquisition | No | No while identity gates hold | Replication evaluations; gate audits | Very low | 5 | 3 | Components rising fast, but failing at human-held gates; open weights escape them | Evaluations; identity checks on compute and payment |
| Continual learning | No | No evidence | Update compute, attested weight differences, re-evaluation | Moderate | 6 | 4 | Not one capability; forgetting brakes it; context-based adaptation escapes weight accounting | Compute metering and re-evaluation |
| Long-horizon autonomy | Long-horizon competence is part of D1; unattended operation only for closure | No | Time horizons at 50% and 80% | High | 7 | 5 | Recast as the clock of closure: watched and used to space gates, not limited | Evaluations, in public |

The reasons, briefly. The top two act on opposite sides of the line and are both hard to see:
self-improvement's effect on T_b ranges, on the evidence, from a modest multiplier to a runaway;
undeclared compute exists now and lengthens T_r to decades. Declared scaling moves T_b most of any
measured pathway but is the best seen. Distillation is invisible to compute channels but bounded by
its teacher. Self-replication is cheap to forbid and blocked today by human-held gates. Continual
learning is unmeasured and damped by forgetting. Autonomy adds nothing by itself and is costly to
limit.

Three order judgements are weakest. Distillation against declared scaling: if a gate on teacher
outputs proves unworkable, distillation's invisibility may matter more than scaling's size.
Self-replication against continual learning: both gains are unmeasured, and the order rests on the
replication components being measured and rising. And the tie at the top could break either way on
E4 and E5.

## What the ranking means for the protocol

Part II derives the protocol from this ranking. In rank order, each pathway is restricted (a limit
the protocol enforces), metered (counted against the line) or watched (measured, not limited).

1. **Recursive self-improvement: restrict, narrowly.** No closed-loop AI research on frontier-scale
   systems above a trigger on the loop gain; research compute metered as part of compute held;
   mandatory declarations of the AI share of research and of efficiency at fixed compute, with
   compute verification mandatory rather than optional; search loops whose evaluator scores AI
   training efficiency registered and counted
   ([A5](012-computational.md#a5-search-and-planning)); narrow optimisers inside a covered system's
   loop treated as part of it ([F3](014-cognitive.md#f3-narrow-versus-general)). Part I states the
   trigger two ways. The anatomy chapter binds on the lower confidence bound of the gain; the
   dynamical chapter fires when the upper bound crosses a margin below 1. A lower-bound trigger fires
   only once the evidence shows the gain above the threshold; an upper-bound trigger fires as soon as
   the evidence cannot rule that out. If today's corrected historical estimates carried over to an
   automated frontier loop, the first would not fire and the second already would
   ([Y1a](013-dynamical.md#y1a-the-software-loop)). This ranking puts self-improvement first partly
   because of that width, which
   argues for the upper bound. Part II must choose, and say why.
2. **Undeclared compute: restrict at the source.** Register chips at birth at the narrow stages;
   bind the states that host the chokepoints by the same k-of-n rules as everyone else; compute every
   party's breakout time as if the worst-placed party holds the untraced pool; bound hidden work on
   registered chips by re-executing declared work; weight intelligence shared among rival blocs and
   rewarded insiders. Do not rely on detection after the fact.
3. **Scaling of declared compute: meter.** Meter compute held (training, post-training, RL rollouts,
   teacher generation, inference and updates) in H100e-seconds; recompute T_b at each declaration from
   agreed tables; let thresholds fall with algorithmic progress measured at the cap's own scale;
   allow more headroom in domains with a cheap verifier; evaluate at declared checkpoints about every
   [4](numbers.md#comp-rsp-cadence)x of effective compute.
4. **Distillation: restrict, keyed to the teacher.** Bulk generation of training data from a model
   above a capability threshold set below the line goes through the same gate as compute; providers
   log output access; evaluations catch a capability jump without matching compute; release decisions
   for weights near the line carry the same weight.
5. **Self-replication and resource acquisition: restrict.** No deployment of models whose
   replication capability exceeds a threshold; identity checks on compute and payment, with
   structuring counted; evaluations at declared training checkpoints; for open weights, the release
   decision.
6. **Continual learning: meter.** Count update compute toward the lineage's training compute; attest
   weight differences; re-evaluate on drift; evaluate the deployed system with its memory and
   scaffolding.
7. **Long-horizon autonomy: watch.** Measure the 50% and 80% horizons; space human-held gates by the
   80% horizon; no limit.

One thing a ranking cannot show is that the pathways feed each other. Distillation is the
cross-party edge; undeclared compute feeds every loop; the economic loop is the edge from money to
compute; autonomy sets how long any loop runs between gates. Loops each below 1 can be above 1
together [@davidson2026feedback; @burtsev2026criticality]. Part II must bound the combined gain as
well, with a gate on each edge ([Y3](013-dynamical.md#y3-coupling)).

Against the memo's protocol shape, six changes follow: undeclared compute joins the restricted set
at the top, with breakout times counting the untraced pool; distillation gets a gate keyed to the
teacher; the compute limit is on compute held, not training compute per run; the self-improvement
trigger names its bound, and compute verification is mandatory; the ban on self-replication is paired
with release control for open weights; and autonomy is measured and used as a clock, not limited.

## Prior work, and our search

The novelty file records that no survey track searched for an earlier ranking of pathways to
superintelligence ([the novelty file](03-novelty.md#the-pathway-ranking)). We ran a short search on
2026-11-27 with these queries: "pathways to superintelligence ranking comparison necessary
sufficient"; "routes to transformative AI governance chokepoints threat model comparison"; "threat
models AI takeoff comparison intelligence explosion pathways software hardware loops"; "prioritising
which AI capabilities to restrict to prevent superintelligence: self-improvement, autonomy,
self-replication, scaling ranked"; "Modeling Transformative AI Risks MTAIR paths to high-level machine
intelligence takeoff speed model"; "breakout AI treaty evasion routes distillation smuggling
distributed training comparison 2026"; "comparative assessment routes to artificial superintelligence
which to restrict compute algorithms autonomy governance priority"; and a query on Forethought's loop
comparison. What we found and opened, and what it covers:

- **The method.** Acquisition path analysis ranks paths by time and detection probability and places
  verification where it does most good [@allen-2015-llnl]. Our criteria are that method applied to
  AI. Prior work.
- **Comparisons of the loops.** Davidson, Hadshar and MacAskill compare the software, chip
  technology and chip production loops by their lags and room to grow, and put the chance that the
  chip technology loop alone sustains acceleration at [65%](numbers.md#dyn-ie-p-chiptech) and chip
  production at [80%](numbers.md#dyn-ie-p-chipprod) [@davidson2025three]. That is the closest
  comparison we found. It covers loops only, not supply routes or transfer, and does not rank them
  for a protocol.
- **Lists of pathways.** Genewein et al. name four pathways from AGI to ASI: "scaling AGI", "AI
  paradigm shifts", "ASI emerging from large-scale multi-agent collectives" and "recursive
  improvement" [@genewein2026agiasi]. In what we read (the abstract and the survey's note), they are
  not ranked or tied to a measurement and a limit.
- **Which pathway to restrict first.** A Narrow Path's conditions include no AIs improving AIs and
  no AIs capable of breaking out of their environment [@miotti2025narrowpath]. The red-lines campaign
  names self-replication and self-improvement without authorisation as example lines
  [@redlines-2025]. Clymer et al. take autonomous AI R&D as the risk that needs minimum safeguards,
  starting from the proposed line that "no AI system should be able to improve itself or other AI
  systems without explicit human approval and assistance" [@clymer2025bareminimum]. Aguirre places
  the danger where autonomy, generality and intelligence meet [@aguirre2025ktfh]. The frontier
  frameworks track AI R&D and autonomy as categories [@anthropic2026rsp; @openai2025preparedness],
  and automated AI R&D is the near-universal industry trigger [@metr-common-elements-2025]. Each
  implicitly puts self-improvement first; none compares it with supply routes on stated criteria.
- **Routes for a party short of compute.** Remler and Hayum list compute (smuggling, remote access,
  indigenous chips), industrial espionage and adversarial distillation as three axes, without ranking
  them [@remler2026distillation]. Rahman asks whether distributed training undermines compute
  governance [@rahman2026].
- **Scenarios, not pathways.** Barnett and Scher organise their agenda around four geopolitical
  scenarios for the response to advanced AI, not around pathways [@barnett2025governance].

The search turned up, without our opening them, a 2022 model of paths to high-level machine
intelligence and takeoff, and a 2026 comparison of strategic visions for governing a transition to
superintelligence. They are not cited, and they would be the first to open at level 1.

**Label: extends prior work, provisionally.** The method, the candidate pathways and the loops'
comparison are prior work. What we did not find: a ranking of these seven routes, loops and supply
and transfer routes together, each judged necessary, sufficient or neither on stated proxies, tied
to the terms of D4 (whether it shortens T_b or lengthens T_r), to the channel that sees it and to the
cost of a limit, with ties where the evidence does not separate them. "Not found" is a claim about
this short search, run by the helper that wrote the ranking. It needs the independent search at level
1 of `07-verification.md` before it is claimed.
