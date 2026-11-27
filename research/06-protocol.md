# Part II: The protocol, derived

Part I asked what superintelligence is and by what mechanisms it forms, and ranked seven pathways
toward it ([the pathways chapter](02-pathways.md)). This part derives the protocol from those results.
Every rule names the mechanism or pathway it comes from, the channel that verifies it, what that
channel cannot see, and what it costs useful AI.

[The memo](00-memo.md) sketched the protocol before the survey. Three findings changed it, and the
level 4 red team changed it again ([its report](verification/l4-red-team.md)).

- **The line is a time, and both its sides must be computed**
  ([D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr)). The nuclear precedent the memo leaned on
  never set a margin above 1 and never timed response [@iaea-glossary-2001; @cochran-2005].
- **Undeclared compute moved to the top.** At the historical discovery rate, an upper bound for a
  careful evader, detecting covert work at a miss chance of [5%](numbers.md#def-prevent-beta) takes at
  least [31 years](numbers.md#e5-td-site-now-years) to [32 years](numbers.md#e5-td-hist-years) (E5),
  and [25%](numbers.md#e24-halt-share-never) of findings against parties still in their treaty were
  never followed by a halt (E24).
- **Most of the pieces are prior work:** expiring chip licences renewed by rival blocs (flexHEG)
  [@petrie2025flexheg1; @aarne2025flexheg3]; thresholds, chip tracking, inspections and withdrawal
  notice (MIRI's draft agreement) [@scher2025agreement]; breakout from holdings
  [@miotti2025narrowpath; @fithian2026hardwired]; detecting and responding faster than breakout
  [@barnett2025governance; @gan2026clock] ([the novelty file](03-novelty.md#the-protocol)). Level 1
  found most of the rest prior work too, among it timely detection per path [@snell2007itc20], the
  small-gain certificate [@dashkovskiy2007smallgain], cartel leniency [@aubert2006leniency] and
  Bitcoin-anchored logs [@tomescu2017catena].

The short version:

- **The line, per path and per attempt.** Every path must meet T_b(p) >= m * (T_d(p) + T_resp(p)),
  with T_b from tables agreed in advance and T_r from the regime's own channels and drilled
  responses; a stricter test where a checkpoint can move between paths; and a bound on attempts.
- **No loop-gain trigger yet.** Closed-loop AI research on frontier-scale systems needs logged human
  gates, since E4 found the proposed trigger on the loop gain K cannot tell subcritical from
  supercritical loops at realistic noise. Capability is judged on elicitation named in advance, with
  published miss and false-alarm rates.
- **Six limits, one per mechanism:** compute held, undeclared compute, closed research loops,
  distillation, self-replication with release control, and continual-learning updates. Data, autonomy
  and narrow systems are left alone.
- **Verification that trusts named parties for named things:** chips registered at birth, licences
  that lapse unless renewed on logged evidence by licensors outside the holder's bloc, a counter capping
  each chip's powered time, a log held by rival replicas, random inspections with no known last
  period, and a miss chance for the evader's best path.
- **What it costs:** little for most useful AI; most for frontier developers, whose ceiling falls in
  physical compute every year; and every holder's chips hang on its rivals' signatures.
- **Where it is weakest:** the untraced pool, which nothing here closes and through which every party
  fails the line; response, so lapse is the
  default and the price is hold-up; algorithmic progress; and the states that host the chokepoints.

This is a design, deployed nowhere and tested against no real adversary. Illustrative numbers are
marked as such.

## What the protocol must do

D4 states the line with T_r = T_d(beta) + T_resp: T_b is a holding's breakout time, T_d(beta) the
time by which the regime detects a breakout with probability 1 - beta, T_resp the time from a
confirmed finding to an effective halt, and m a margin
([D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr)). Part III reads the line per path and corrects
that reading twice ([C1, the line per path](05-formal.md#c1-the-line-per-path)). The per-path test
holds only against an evader whose progress restarts when it changes path (Proposition 1.7); a
checkpoint is a file, and the red team's evader trains on a declared path and finishes on a covert one
([C1.1](verification/l4-red-team.md#c1)). Where progress carries over, the line sits between the
per-path test and the scalar test, the fastest T_b against the slowest T_r (Proposition 1.8). Both
assume constant speeds, unproved for a run whose speed rises. And beta
bounds one attempt, so halts must remove what they act on and attempts must be bounded
(Proposition 1.9; [C1.4](verification/l4-red-team.md#c1)). Five requirements follow.

1. **Keep every path and strategy of every party outside the line, attempt by attempt** (the limits).
2. **Shorten T_d on each path, above all the one an evader would choose** (the channels).
3. **Shorten T_resp.** A response that needs its target's cooperation is slow and may never come.
4. **Agree in advance how T_b is computed.** In Barrett and Dannenberg's experiment a known
   catastrophe threshold was avoided by [8 groups](numbers.md#def-bd-known-avoided) of
   [10 groups](numbers.md#def-bd-groups), and an uncertain one ended in catastrophe for
   [9 groups](numbers.md#def-bd-uncertain-catastrophe) [@barrett2012climate].
5. **Leave everything outside the line free to keep improving,** through metered, human-held gates
   ([D6](01-anatomy.md#d6-closure)). A protocol that meets the first four by declaring all frontier AI
   weapons-grade has failed the brief.

The pathways ranking (C12) says where the protocol must stand. It is a judgement: only pairs one
pathway beats on every criterion are fixed by the evidence, and none decides the top
([C12](05-formal.md#c12-the-ranking-what-can-be-proved); [C12.1](verification/l4-red-team.md#c12)).
The cost of limiting each pathway decides whether the protocol restricts, meters or watches it.

| Pathway | Rank | Acts mainly on | Response | Rule |
|---|---|---|---|---|
| Recursive self-improvement | 1 (tied) | T_b, through loop gain; its labour is invisible to physical channels | Restrict, narrowly | L3 |
| Undeclared compute | 1 (tied) | T_r, through detection times of at least [31 years](numbers.md#e5-td-site-now-years) to [32 years](numbers.md#e5-td-hist-years) | Restrict at the source | L2 |
| Scaling of declared compute | 3 | T_b, the largest measured driver | Meter | L1 |
| Distillation from a stronger model | 4 | T_b of a follower, at nil compute | Restrict, keyed to the teacher | L4 |
| Self-replication and resource acquisition | 5 | T_b, through compute acquired outside the gates | Restrict, with release control | L5 |
| Continual learning | 6 | T_b, through updates that add up to training | Meter | L6 |
| Long-horizon autonomy | 7 | Neither directly; it sets how long a loop runs between gates | Watch, and space the gates by it | none |

Three structural requirements come from the mechanisms.

- **A gate on every edge between loops.** Loops each subcritical can be supercritical together
  [@davidson2026feedback; @burtsev2026criticality]; in Burtsev's scenario, damped blocs reach a network
  reproduction number of [1.15](numbers.md#dyn-burtsev-network-rho) through transfer
  ([Y3](013-dynamical.md#y3-coupling)).
- **The compute backbone.** Compute is the only input with physical chokepoints
  ([O3](015-organisational.md#o3-chokepoints)). It explains
  [80%](numbers.md#comp-mertens-frontier-share-lo) to [90%](numbers.md#comp-mertens-frontier-share-hi)
  of performance differences at the frontier [@mertens2026secretsauce], though in E1 the share of
  capability growth from compute runs from [18%](numbers.md#e1-compute-share-subset-min) to
  [63%](numbers.md#e1-compute-share-subset-max) over six samples of the same models.
- **Prevention near the line.** Superintelligence is irreversible, and a deterrence line accepts that a
  breakout succeeds whenever the payoffs favour trying
  ([D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr)).

Nor may it limit what would cost useful AI much for little gain: capital, talent and data
([O1](015-organisational.md#o1-the-supply-of-inputs)), serving capacity
([F1](014-cognitive.md#f1-kinds-of-advantage-speed-copies-and-quality)) and autonomy
([the pathways chapter](02-pathways.md#rank-7-long-horizon-autonomy)).

## The line and its triggers

### Breakout time, read from tables agreed in advance

T_b(p) is the shortest time, under a party's best effort on path p, from its holdings to the
effective compute C* the regime has agreed would reach D1 ([D3](01-anatomy.md#d3-breakout-time)). The
protocol tabulates it as the IAEA tabulates conversion times: by holding class, under best-case
assumptions for the proliferator, before anyone needs the answer [@iaea-glossary-2022]. Five choices
fix the tables.

1. **C* is a convention.** Nobody can measure the effective compute that reaches D1 before someone
   reaches it; the only published breakout budget, [2e+29 FLOP](numbers.md#def-hwp-breakout-budget),
   is an assumption of its paper [@fithian2026hardwired]. One OOM of C* moves T_b by
   [2.3 years](numbers.md#comp-years-per-oom-ho) at Ho et al.'s central rate, more than the
   illustrative line below, so every table is conditional on the agreed C*. The parties agree a
   conservative C* and revise it on schedule from the matched-budget battery (E21) and out-of-sample
   forecasts (E1), stating the cost of a lower one.
2. **The holding classes.** Registered chips in H100e at a reference precision; weights, by elicited
   capability (D5); access to a teacher's outputs; research labour, with the declared AI share and the
   loop gain; and a share of the untraced pool.
3. **The untraced pool is a covert reserve, held by the worst-placed party.** About
   [1,000,000 chips](numbers.md#phys-chips-unaccounted) are traced to no owner [@koopmanschap2026gpu],
   and a median [660,000 H100e](numbers.md#org-smuggled-cum) were smuggled into one country through
   2025 [@juniewicz2026smuggling]. Every party has a covert path through it, tabulated as if it held
   all of it ([O3](015-organisational.md#o3-chokepoints); C8).
4. **Efficiency depends on scale, and the tables use the fast path.** Of a claimed
   [22,000](numbers.md#def-gundlach-claimed)-fold gain, less than
   [100](numbers.md#def-gundlach-low-compute-max)-fold accrues at small compute, only the first tenfold
   of it from ablations [@gundlach2025origin]. E1's fit has drift falling with scale, about
   [28](numbers.md#e1-algo-annual-1e24)x a year at [1e+24 FLOP](numbers.md#org-miri-strict), MIRI's
   prohibited threshold, against [5.8](numbers.md#e1-algo-annual-1e26)x at
   [1e+26 FLOP](numbers.md#phys-rahman-1e26-local), but it cannot identify the frontier's rate: over six
   samples of the same models it runs from [2.6](numbers.md#e1-algo-annual-subset-min)x to
   [1,512](numbers.md#e1-algo-annual-subset-max)x a year ([C2.3](verification/l4-red-team.md#c2)). The
   tables use a rate at each holding's own scale, name its population and take the fast end, as D3
   asks. Gains a party does not declare are unsized: efficiency is declared, not verified, and no
   evidence measures private gains ([C2.7](verification/l4-red-team.md#c2)). So for a party that hides
   its algorithms a tabulated T_b is an upper bound, short by the hidden gain over the drift rate, and
   m does not cover it, since Corollary 1.3 covers error, not concealment. For the computational
   chapter's example cap, the Rosetta rate gives a leak time [1.8](numbers.md#prot-fast-path-factor)
   times shorter than Ho et al.'s central rate
   ([the combined leak](012-computational.md#the-combined-leak-of-a-training-cap)).
5. **The other terms are inside T_b** (C2, tested by E18): the post-training jump of
   [0.7 OOM](numbers.md#comp-oneoff-lo-oom) to [1.3 OOM](numbers.md#comp-oneoff-hi-oom)
   [@davidson2023enhancements]; the inference span, up to [3 OOM](numbers.md#comp-span-cheapver-train)
   where a cheap verifier exists [@villalobos2023tradeoff]; distillation, which closes the gap to any
   teacher the holder can query and can pass it ([C2.5](verification/l4-red-team.md#c2)); and loop
   gain, which speeds algorithmic drift.

Tables are recomputed at each declaration, for each party and path. A path must clear the line at each
declaration by the factor phi by which its T_b could fall before the next, which works only if supply
limits how fast holdings grow ([Part III](05-formal.md#c1-the-line-per-path), Proposition 1.6), and
only for a T_b that counts drift during the run. A T_b computed at launch speed must clear the line
raised by a factor of [3.2](numbers.md#formal-inrun-line-factor) at the central drift rate and
[10.6](numbers.md#formal-inrun-line-factor-high) at the high end, both upper bounds (Corollary 1.6a).

### Response time, from the regime's own channels and drills

T_r has two halves, both computed, not chosen.

**Detection, T_d(p, beta).** It is ln(1/beta) / lambda at a constant detection rate lambda on path p
([the channels](#channels-trust-anchors-and-the-evaders-best-path); C3).

**Response, T_resp(p).** No AI regime has measured one. In E24's arms-control record, of
[8 findings](numbers.md#e24-halt-findings) made while the party was in its treaty,
[25%](numbers.md#e24-halt-share-never) were never followed by a halt; with those censored the median
wait was [1.2 years](numbers.md#e24-halt-km-median-years), inside the hardwired-pause group's
[2 yr](numbers.md#def-hwp-horizon) window, and [67%](numbers.md#e24-halt-share-reversed) of halts were
later reversed or shown incomplete. The DPRK gave notice of withdrawal
[31 days](numbers.md#e24-exit-min-days) after a finding [@iaea-gc37-1084].

A path is safe at miss chance beta_1 + beta_2 if its T_b exceeds T_d(beta_1) plus the (1 - beta_2)
quantile of T_resp ([Part III](05-formal.md#c1-the-line-per-path), Proposition 1.4). While more than
beta_2 of findings are never acted on, the record has no such quantile. **No response the record
shows can hold a prevention line,** and a halt reversed with the progress intact was a pause between
attempts.

**So lapse is the default.** A registered chip runs only on an expiring licence, renewed on positive
evidence in the log by k licensors outside the holder's bloc; a failed check, a withheld signature,
silence or deadlock lets it lapse, and the chip stops by itself within its powered-time budget, about
one licence period ([the licence clock](#the-licence-clock)). flexHEG calls this "the
only reliable way to implement any kind of remote 'off switch'" [@petrie2025flexheg1]. The time from
a failed check or a withheld signature to a stop is set by design
([P1](verification/l4-red-team.md#the-protocol)); a licensor's judgement where the evidence does not
decide is not, and the price is hold-up ([lapse by default](#lapse-by-default-and-its-price)). Chips
whose licences lapse on a violation are returned, not paused, so a second attempt starts from less.
Drills must test all of it.

An illustration for the declared path, not a measurement. For detection, take the
[9 months](numbers.md#org-dprk-months) IAEA accountancy took to find the DPRK's discrepancy
[@iaea-gc37-1084], the one historical detection time on declared material; for response, one licence
period of [3 months](numbers.md#prot-licence-months), flexHEG's example [@petrie2025flexheg2]. Then
T_r is [1.0 years](numbers.md#prot-tr-declared) for a violation the renewal rule checks mechanically,
such as a discrepancy left unreconciled. One that needs judgement adds a decision time no record
measures for such a body; in E24 first sanctions came a median of
[32 days](numbers.md#e24-sanctions-median-days) after a finding, and formal statements
[60 days](numbers.md#e24-statement-median-days). At a margin of [2](numbers.md#prot-margin) the line
sits at [2.0 years](numbers.md#prot-line-declared), by coincidence the horizon of
[2 yr](numbers.md#def-hwp-horizon) the hardwired-pause group chose by judgement
[@fithian2026hardwired]. A breakout time computed at launch speed must exceed
[6.3 years](numbers.md#prot-line-declared-inrun) instead, or
[21.3 years](numbers.md#prot-line-declared-inrun-high) at high drift (Corollary 1.6a).

Detecting with miss chance
[5%](numbers.md#def-prevent-beta) within that time needs a rate of
[4.0/yr](numbers.md#prot-lambda-declared), at least [43](numbers.md#prot-lambda-over-history) times
E5's fitted discovery rate of covert programmes, [0.094/yr](numbers.md#e5-hazard), itself an upper
bound for a careful evader. On declared sites E5 puts T_d at [39.0 days](numbers.md#e5-td-declared-days),
resting on chip sampling, whose rate comes from a design with
[232 inspectors](numbers.md#phys-shavit-inspectors), not a measurement; metering's one-day result
counts once, since a disguise that hides a run for a day may hide it the next
[@kimpson2026dcpower; @shavit2023chinchilla] ([C3.1](verification/l4-red-team.md#c3)). On undeclared
paths T_d is at least [31 years](numbers.md#e5-td-site-now-years) for a site above the satellite line,
[32 years](numbers.md#e5-td-distributed-years) for chips spread below it and
[32 years](numbers.md#e5-td-pool-years) for the untraced pool, before any response; the pool's is
about [299](numbers.md#e5-td-ratio) times the declared path's. Cloud compute and distillation have no
measured channel and no T_d. No margin bridges that, which is why the paths are treated differently.

### The margin

The margin m is a design choice, set by negotiation; [2](numbers.md#prot-margin) here only makes the
illustrations concrete. Its job is C1's: if the estimates of T_b(p) and T_r(p) err in the unsafe
direction by at most factors e_b and e_r, a path admitted as outside the line is still stopped with
probability at least 1 - beta whenever e_b * e_r <= m, for any continuous detection hazard; a rate
known only within a factor c is handled by computing T_d at beta^c
([C1](05-formal.md#c1-the-line-per-path), Proposition 1.2 and Corollary 1.3). The margin covers error
in T_r and in applying the tables. It does not cover C*, whose distance from D1 has no bound; error a
party makes on purpose, by declaring its efficiency low or disputing findings
([C1.7](verification/l4-red-team.md#c1)); or the transfers behind E5's and E24's rates from weapons
programmes to AI. The fast-path tables absorb most of the error in efficiency; on the central path m
would need to be at least [1.8](numbers.md#prot-fast-path-factor) for that alone, where the IAEA's
implied margin never exceeds [1.00](numbers.md#def-iaea-m-irr-high) [@iaea-glossary-2001].

### Prevention near the line, deterrence far from it

In Gan's illustrative calibration, deterrence needs a monitoring rate of
[0.0319/month](numbers.md#def-gan-deter-rate) over a [12 months](numbers.md#def-gan-window) window,
which detects a breakout with probability only [32%](numbers.md#def-gan-deter-detect). Holding success to
[5%](numbers.md#def-prevent-beta) needs [0.25/month](numbers.md#def-gan-prevent-rate),
[7.8](numbers.md#def-gan-prevent-multiple) times as much [@gan2026clock], and such monitoring exposes
secrets, which Coe and Vaynman find is why arms control is rare [@coe2020arms].

So the protocol pays for prevention only where it must. A path is **near the line** when the interval on
its T_b overlaps m * T_r, or when it could cross within one tabulation period on the fast efficiency
path. Deterrence and prevention come apart both ways
([the compliance section](05-formal.md#compliance-as-an-equilibrium-inspection-games-with-no-known-last-period),
Proposition E.4). Near the line, channels are sized for prevention: continuous metering, chip sampling,
evaluations at every checkpoint. Far from it the regime relies on deterrence: random inspections at a
published probability, penalties, rewarded insiders.

### The loop-gain trigger, and which bound binds

D2 measures the loop gain from staged rounds of AI-run research with compute and data held fixed
([D2](01-anatomy.md#d2-loop-gain); C4). The per-round ratio g_k is not a stable parameter, since for
every subcritical loop it tends to 1 ([C4](05-formal.md#c4-the-loop-gain-estimator), Proposition 4.3).
The stationary quantity is the loop gain K, closure times the return to research, estimated from the
round identity or as a product of separately measured factors with a joint bound (Lemma 4.1, Proposition
4.5). A trigger would take the upper bound on K, which bounds misses where a lower-bound rule does not
(Proposition 4.4).

**E4 found that the trigger fails** ([C4](verification/l4-red-team.md#c4)). At the only noise level
calibrated on data, the NanoGPT speedrun's, with a placeholder K* of [0.90](numbers.md#e4-gstar), the
rule on K after [5 rounds](numbers.md#claim-d2-rounds) at each of three budgets raised false alarms on
[88%](numbers.md#e4-k-fa-n5) of loops at the corrected median, missed [10%](numbers.md#e4-k-late-cal) of
loops at the 95th percentile ([30%](numbers.md#e4-k-late-hide25-cal) against an agent withholding a
quarter of its gain), and fired only [2%](numbers.md#e4-k-fire-gap-n5) more often at the 95th percentile
than at the median, within Monte Carlo error. After 50 rounds per budget its false alarms were still
[80%](numbers.md#e4-k-fa-nmax). Only large, tightly measured rounds separate the cases, and then the
rule on K needs [20 rounds per budget](numbers.md#e4-k-fa-rounds-fav) (on r,
[12 rounds per budget](numbers.md#e4-fa-rounds-fav)); even there an agent withholding in a pattern makes
the trigger on r fire late in [96%](numbers.md#e4-late-ub-hide25-fav) of runs, and keeps it silent half
the time by withholding [16%](numbers.md#e4-hide-silence-fav) of its gain. The remedy of two independent
held-out sets fails at calibrated noise: with all noise in measurement it gives
[8.11](numbers.md#e4-diff-bias-meas2) times the truth, against [0.57](numbers.md#e4-diff-bias-meas1)
with one set. The estimator's 90% interval covers [82%](numbers.md#e4-cov-n5)
([77%](numbers.md#e4-cov-n5-xml) by maximum likelihood), and its biases lie on the unsafe side. The
speedrun's own return is withdrawn as not identified. C4 is downgraded to a measurement design.

**So the rule is the ban.** AI-run changes to the training inputs of a frontier-scale system need
logged human gates (L3), the prior-work rule, with no trigger to lift it until E4(b) measures real
staged rounds and finds a rule that tells loops below K* from loops above 1. The lower-bound rule fails
too, missing [95%](numbers.md#e4-miss-lb-s0-cal) of loops at the 95th percentile, so a lower bound
above 1 counts as evidence, not as a stage of a rule. The
burden of evidence falls on the party that wants the loop: in the one independent assessment of AI R&D
acceleration we found, "Anthropic changed the scope of this project midway to exclude compute
verification and instead just focus on AI R&D acceleration" [@metr-anthropic-acceleration-2026].

**What the ban costs.** With every input closed, K equals the return to research,
[0.63](numbers.md#dyn-r-lm-corrected) at Part I's corrected median and
[1.07](numbers.md#dyn-r-lm-hi-corrected) at the 95th percentile [@ho2025experiments]. Those values leave
compute's growth out; counting it, E9 puts the language-model gain at fixed compute at
[0.25](numbers.md#e9-lm-k-fixed) ([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile) at a
compute share of [0.67](numbers.md#dyn-research-compute-share), above 1 only below a share of about
[0.26](numbers.md#e9-lm-share-crit), and the share is not identified. So the ban stops loops that are
probably subcritical. Today it is close to nil: the one
developer that reports the share says Claude leads [26%](numbers.md#dyn-anthropic-ai-led) of its AI R&D
work but "is not operating fully autonomously for any measured subset of AI R&D work"
[@anthropic2026pace].

**Closure, input by input.** Closures on separate inputs do not multiply: with the production
function unknown, the safe bound is the return times the largest closure among ungated inputs
([C11](05-formal.md#c11-closure-by-input-the-combination-rule), Theorem 11.2). So L3 gates every
highly closed input together, the prior-work rule of holding every input, and closure by input changes
no rule until E4(d) decides ([C11.3](verification/l4-red-team.md#c11)). A trigger, if E4(b) finds one,
would need the margin K* = 1 - m * K_dot * T_r, with K_dot the unmeasured rate at which the gain drifts
upward (Corollary 6.6; [P6](verification/l4-red-team.md#the-protocol)).

### Elicited capability, with the budget named in advance

Capability enters the line as a system's starting point in T_b and as the agent in D2's staged runs.
Both are judged on elicited capability, not observed scores
([D5](01-anatomy.md#d5-elicited-capability-robust-to-hiding); C5).

- **The budget is named before the evaluation.** An elicitation protocol E lists its methods
  (fine-tuning on k demonstrations, RL with n samples, best-of-k, the strongest public scaffolds, noise
  injection, weight-level methods) and is revised on a schedule.
- **Each E carries two measured rates,** published as one-sided upper bounds: a miss rate over model
  organisms with hidden capability, built blind to E, and a false-alarm rate over benign models. These
  are population rates: they bound a developer that hides by the sampled methods, not one that sees E
  and builds against it ([C5.1, C5.2](verification/l4-red-team.md#c5)). At the claims file's targets of
  [10%](numbers.md#claim-d5-miss-target) and [10%](numbers.md#claim-d5-false-alarm-target), the miss
  target at [90%](numbers.md#claim-confidence) confidence takes
  [22 organisms](numbers.md#claim-d5-organisms) per budget with no misses,
  [38 organisms](numbers.md#formal-d5-organisms-one-miss) with one and
  [52 organisms](numbers.md#formal-d5-organisms-two-miss) with two
  ([C5](05-formal.md#c5-miss-and-false-alarm-rates-with-exact-bounds)).
- **The guarantee has a stated range.** Elicitation works where high-quality demonstrations exist
  [@greenblatt2024password]. It fails against hardened locks: an RL lock held for more than
  [500 GRPO steps](numbers.md#def-xh-rl-lock-steps) [@jang2026explorationhacking], and a
  tamper-resistant organism recalled [7.8%](numbers.md#def-robust-hard-recall) on hard tasks against
  [71.2%](numbers.md#def-robust-base-recall) for its base [@finke2026robustorganisms]. Beyond the range,
  the protocol places the system by its compute, at the top of what its scaling forecast allows plus
  E1's overlap: on GPQA Diamond the largest model that lost to PhD experts had
  [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) more training compute than the smallest that won, so a
  system is treated as if it had that much more compute ([C2.6](verification/l4-red-team.md#c2)). The
  fallback stays weak: the allowance comes from one benchmark, and it errs toward false alarms.
- **Cadence.** At each declared checkpoint, about every [4](numbers.md#comp-rsp-cadence)x of
  effective compute [@anthropic2026rsp], and before deployment: about every
  [6 months](numbers.md#prot-eval-interval-months) at frontier compute growth and Ho et al.'s central
  rate, which E1 cannot confirm at the frontier.
- **Access.** Fine-tuning elicitation needs the weights or a trusted enclave
  [@aisi2025auditingblog], which exposes a developer's most sensitive asset [@coe2020arms].

The cost to useful AI is the false-alarm rate. In the UK AISI auditing game,
elicitation lifted benign models about [10 points](numbers.md#def-audit-benign-uplift) too, and the
blue team "could not reliably discriminate sandbaggers from benign models" [@taylor2025auditinggames].

## One limit per mechanism

Each limit holds one mechanism below the point where it would bring a holding inside the line. The
table summarises; the sections below give the reasons.

| Limit | What is limited | Threshold, and how it falls | Channel; blind spot | Cost to useful AI | From |
|---|---|---|---|---|---|
| L1 Compute held | Chip-time held: training, post-training, RL rollouts, teacher generation, inference, updates | The line on each path; a declaration filter that falls at the algorithmic rate at its own scale | Registry, metering, sampling, re-execution; blind to algorithms and consumer hardware | Low: counted, not limited | P1, P3, A1 to A3; scaling (3) |
| L2 Undeclared compute | AI chips outside the registry; registered chips without a logged licence | Zero above a technical definition that falls as consumer chips improve; no covert reserve able to reach C* | Accounting at birth, intelligence, insiders; blind to the old pool and small nodes | Low for makers; high for host states, which have reversed such rules within months | O3, O4, P4; undeclared compute (1) |
| L3 Closed research loops | AI-run changes to a frontier system's training inputs without logged human gates | Any loop on a frontier-scale system, whatever its gain, until E4(b) finds a working trigger | Staged runs (a measurement design), declarations, metered research compute; blind to the labour | Low to moderate; near nil today; it stops loops that are probably subcritical | Y1a, D2, D6, F3; self-improvement (1) |
| L4 Distillation | Bulk training data from a teacher above a threshold below the line | Keyed to the teacher's elicited capability | Provider logs, evaluations; blind to fraudulent accounts and open weights | Moderate | A2, Y3; distillation (4) |
| L5 Self-replication | Deployment above a replication threshold; release above a release threshold | Elicited replication, stage by stage | Evaluations, gate audits; blind to open weights | Very low; real for open science | Y1e; self-replication (5) |
| L6 Continual learning | Update compute after deployment | Counted in lineage compute; re-evaluation on steps or drift | Metering, weight hashes, re-evaluation; blind to context | Moderate | Y1d; continual learning (6) |

### L1. Compute held

**What is limited.** Chip-time held by a party, in H100e-seconds at a reference precision, so that a
switch of precision cannot game a threshold ([P1](011-physical.md#p1-the-compute-budget)): training,
post-training, RL rollouts wherever they run, teacher generation, inference and updates. The chips
that serve are the chips that train, the inference leak is paid in compute a chip count sees, and
distributed RL already runs its rollouts on a permissionless swarm [@primeintellect2025intellect2]
([A2](012-computational.md#a2-the-exchange-rate-between-training-and-inference-compute)).

**Threshold and how it falls.** The line applies path by path. Separately, training compute per lineage
above a declaration filter triggers sealed declaration and evaluation at every checkpoint, the cheap
first stage Heim and Koessler argue for [@heim2024thresholds]; the EU presumes high-impact capability
above [1e+25 FLOP](numbers.md#def-eu-presumption-flop) [@eu-ai-act-2024]. The filter falls at the
algorithmic rate measured at its own scale: one OOM every [2.3 years](numbers.md#comp-years-per-oom-ho)
at Ho et al.'s central rate, [1.3 years](numbers.md#comp-years-per-oom-rosetta) at the Rosetta rate, no
faster than one every [5.5 years](numbers.md#comp-years-per-oom-small) at the small-compute bound
([A3](012-computational.md#a3-algorithmic-progress)). Domains with a cheap verifier need more headroom,
about [3.4 OOM](numbers.md#comp-headroom-needed-verifier) against
[1.7 OOM](numbers.md#comp-headroom-needed-ho)
([the combined leak](012-computational.md#the-combined-leak-of-a-training-cap)).

**Channel, and what it cannot see.** The registry; delay-based location verification, at about
country level [@brass2024location; @feldgoise2026tracking]; on-site power metering for the kind of work
at declared sites [@kimpson2026dcpower], its tamper resistance tested in E13; chip sampling
[@shavit2023chinchilla]; sealed declarations. A power trace alone cannot exclude hidden computation of
up to [1.16](numbers.md#phys-beta-worst) times declared capacity; re-executing declared work cuts that
to [0.059](numbers.md#phys-beta-restricted) (abstract only) [@kimpson2026b]. The channel is blind to
the algorithms that multiply compute, and to inference on unregistered consumer hardware, where open
models match the frontier within [6 months](numbers.md#comp-consumer-lag-lo) to
[12 months](numbers.md#comp-consumer-lag-hi) [@somala2025consumergpu].

**Cost to useful AI: low.** Counting inference costs little; limiting it would cost heavily. The real
costs are evaluation at a frontier pace and the line's own ceiling
([what stays allowed](#what-stays-allowed-and-keeps-improving)).

### L2. Undeclared compute

**What is limited.** Holding or operating any AI chip outside the registry, and operating a
registered chip without a valid, logged licence. New chips get a unit identity where they are made,
tied to EUV tool records, foundry wafers, HBM stacks and packaging, the stages with the fewest
suppliers ([O3](015-organisational.md#o3-chokepoints)). About
[13.6 million H100e](numbers.md#org-sold-2025) were sold in 2025, and five hyperscalers own more than
[70%](numbers.md#org-hyperscaler-share) of the stock [@you2026chipowners].

**Threshold and how it falls.** Zero, above a technical definition of an AI chip, as export rules
already have: a total processing performance of [4,800](numbers.md#org-eccn-tpp), or
[1,600](numbers.md#org-eccn-tpp-pd) at a density of [5.92](numbers.md#org-eccn-pd)
[@bis2023advancedcomputing], and HBM above [2 GB/s per mm2](numbers.md#org-hbm-control)
[@bis2024hbm], falling as consumer chips gain capability. For the existing stock, a registration
window checked against makers' unit records, then contraband status; South Africa's enrichment output
was reconstructed from several thousand operating records [@vonbaeckmann-1995]. Whatever is not
registered is a covert path for every party, and nothing here closes it
([what the protocol does about the pool](#undeclared-compute-and-secret-programmes)).

On a covert path the line has a blunt form. Detection there takes decades (E5), so a covert path meets
T_b(p) >= m * T_r(p) only if the reserve on it could not reach C* within that time even at its best
utilisation: in practice, **hold no covert reserve**
([C8](05-formal.md#c8-the-footprint-floor-as-a-bound), Lemma 8.2). That makes the registry's resolution
the protocol's most important number. It must be finer than the aggregate chip floor of the run it
protects, taken as a bound: at full utilisation and FP8, the lowest precision training at scale uses
([C8.1](verification/l4-red-team.md#c8)). Over a pause's longest sensible run that is
[800 H100e](numbers.md#formal-floor-bound-1e26-pause) for a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run
([1,600 H100e](numbers.md#formal-floor-bound-1e26-pause-bf16) held to BF16) and
[8.0 H100e](numbers.md#e8-floor-1e24-pause-bound) for a [1e+24 FLOP](numbers.md#org-miri-strict) run.
The run length belongs to the adversary, so the bound is better stated as chip-time,
[1,600 H100e-years](numbers.md#e8-chip-years-1e26-bound) and
[16 H100e-years](numbers.md#e8-chip-years-1e24-bound), divided by whatever run length a party chooses.
Floors at a typical utilisation, like the earlier [4,000 H100e](numbers.md#phys-floor-chips-1e26-pause),
are estimates an adversary can undercut (Theorem 8.1). E8 puts the untraced pool, an assumed order of
magnitude, at [340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the 1e26 floor at the median
([110](numbers.md#e8-pool-over-floor-1e26-pause-p05) to
[1,000](numbers.md#e8-pool-over-floor-1e26-pause-p95) from the 5th to the 95th percentile, at BF16; FP8
doubles it), and the smuggled stock alone at [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50)
times. [824](numbers.md#formal-pool-over-floor-bound), the smuggled stock over the FP8 bound at full
utilisation, is one estimate among these.

**Channel, and what it cannot see.** Chip accounting at birth is the main channel that sees the
aggregate ([P4](011-physical.md#p4-the-footprint-and-its-floor)); a distributed run's traffic between
sites and its purchases are aggregate signatures too, which nothing here models
([C8.4](verification/l4-red-team.md#c8)). Intelligence and insiders found the covert programmes of the
record [@baker2023nuclear]. Facility channels are marginal, and E8 says how fast they fail. Satellites
find facilities reliably above [10 MW](numbers.md#phys-sat-reliable) [@koopmanschap2026gpu]. A
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run on one site over today's longest sensible run
draws a median
[20 MW](numbers.md#e8-power-1e26-now-p50), but at fixed compute falls below that line by
[2029](numbers.md#e8-cross-sat-1e26-now) ([2026](numbers.md#e8-cross-sat-1e26-now-p05) to
[2032](numbers.md#e8-cross-sat-1e26-now-p95)); over a pause's longest run it draws a median
[3.8 MW](numbers.md#e8-power-1e26-pause-p50), seen in [19%](numbers.md#e8-concentrated-1e26-pause-seen)
of draws ([60%](numbers.md#e8-concentrated-1e26-pause-seen-denied) for a party denied leading-edge
chips). Spread over one-node sites, it shows a facility channel one node at a time, by construction
[@rahman2026]. Thermal sensing missed a [126 MW](numbers.md#phys-jing-cluster-power) cluster
[@jing2026].

**Cost to useful AI: low for makers,** who already keep unit records. The costs fall on
confidentiality, on sales the host states forgo, and on their freedom to set export policy, which they
have used to reverse such rules within months ([who it binds](#who-it-binds)). Licensing every chip
avoids a cap on unmonitored clusters, which would cost small labs more, but only if the pool closes.

### L3. Closed research loops above a loop-gain bound

**What is limited.** AI-run changes to the training inputs of a frontier-scale system (one above the
declaration filter) without logged human gates, whatever its loop gain, until a trigger is shown to work:
every training launch, merge into the training stack, reallocation of research compute, batch of
generated data and change to the scoring evaluation needs a logged human approval that can refuse.
Gating one input is not enough (C11, closure by input). A narrow optimiser whose evaluator scores AI
training efficiency, as AlphaEvolve's did [@novikov2025alphaevolve], counts as part of the loop it feeds
([F3](014-cognitive.md#f3-narrow-versus-general); E4(e) tests it). Three declarations become mandatory,
with compute verification: the AI share of research work, algorithmic efficiency at fixed compute, and
research spend by input ([Y1a](013-dynamical.md#y1a-the-software-loop)).

**Threshold.** None on K until E4(b) finds a working trigger. Gates are spaced by the work an agent can
do unattended: closer, they bind useful work; further apart, an agent crosses between them alone. The
80% time horizon, about [3 hours](numbers.md#dyn-horizon-p80-hours) now and about
[22 hours](numbers.md#path-horizon-p80-next-year) in a year at the 50% horizon's rate (our arithmetic)
([the pathways chapter](02-pathways.md#rank-7-long-horizon-autonomy)), is measured in human time: the
time humans take on tasks the model completes [@kwa2025horizon]. An agent that finishes a horizon-length
task in minutes can chain several between gates a horizon apart on the clock
([C11.4](verification/l4-red-team.md#c11)). So gates count the agent's completed horizon-length tasks,
not hours, until its own wall-clock time on such tasks is measured for each system. rho* falls if other
edges into the software loop grow ([the edges](#the-edges-between-loops)).

**Channel, and what it cannot see.** Staged runs at fixed compute on declared checkpoints, which a
regime evaluator can run with only the system and a compute budget (E4(b)); the declarations; metered
research compute; insiders, who reach the hundreds of employees a large project involves
[@baker2025verifying]. The rule binds only loops the developer declares
([C4.8](verification/l4-red-team.md#c4)). No physical channel sees the research labour, and a meter
tells training from inference [@kimpson2026dcpower], not research inference from serving.

**Cost to useful AI: low to moderate.** Software work is close to half of observed AI use
[@handa2025aei]. This limit leaves AI-assisted coding and research untouched and binds only closed
loops on frontier training stacks; its cost rises if developers automate their training research,
which is exactly when it matters. The ban itself is prior work: A Narrow Path prohibits AIs improving
AIs [@miotti2025narrowpath], and the red-lines campaign names self-improvement without explicit human
authorisation [@redlines-2025]. Only the trigger was ours, and E4 found it fails; C4 is now a
measurement design.

### L4. Distillation, keyed to the teacher

**What is limited.** Bulk generation of training data from a model whose elicited capability is above
a teacher threshold set below the line: a licensed, logged use, counted in the student's lineage, with
the student evaluated as if it could reach the teacher or pass it. Providers log output access by
verified identity, flag volumes consistent with generating training data, and count access structured
across identities as one.

**Threshold.** Keyed to the teacher, not to the student's compute. The EU makes a downstream modifier a
provider above [33%](numbers.md#comp-eu-modifier-share) of the original model's training compute
[@ec-gpai-guidelines-faq-2025]; distillation needs the opposite key, because its compute is small or
nil. A 32B model distilled from DeepSeek-R1 scored [72.6%](numbers.md#comp-r1-distill-32b) on AIME
2024 against [47.0%](numbers.md#comp-r1-rl-32b) for large-scale RL on the same base [@deepseek2025r1].
The threshold matters only while no open-weight model at the teacher's level exists, and the best open
models trail closed ones by about [4 months](numbers.md#comp-open-closed-lag) [@edwards2026openclosed].

**Channel, and what it cannot see.** Provider logs and identity checks; evaluations at checkpoints,
which catch a capability jump without matching compute (E10). Chip accounting and power do not see it:
policing outputs looks more like the Biological Weapons Convention than nuclear safeguards
([the combined leak](012-computational.md#the-combined-leak-of-a-training-cap)), and adversarial
distillation already runs through networks of fraudulent accounts
([the pathways chapter](02-pathways.md#rank-4-distillation-from-a-stronger-model)).

**Cost to useful AI: moderate.** Distillation is a large part of how useful AI is made cheap. Keyed to
the teacher, the gate leaves distillation from every model below the threshold free, and it limits the
cross-party edge of coupling ([Y3](013-dynamical.md#y3-coupling)).

### L5. Self-replication, paired with release control for open weights

**What is limited.** Deploying a model whose elicited replication capability, measured stage by stage,
exceeds a threshold; and releasing weights above a lower release threshold. Identity checks on compute
and payment hold the gates the loop needs, with structuring across providers counted as one customer
[@egan2023kyc; @heim2024cloud; @krys2025distributed]. Replication is evaluated at checkpoints: in 2023,
evaluations could not rule out autonomous replication after a scale-up of about
[100](numbers.md#dyn-ara-scaleup) times without intermediate checks [@kinniment2023ara].

**Threshold.** On replication capability, which is rising fast: on UK AISI's evaluations, success went
from under [5%](numbers.md#dyn-aisi-rep-2023) in early 2023 to over [60%](numbers.md#dyn-aisi-rep-2025)
by summer 2025, on simplified tasks, with models "currently unlikely to succeed in real-world
conditions" [@aisi2025trends]. They fail at know-your-customer checks and persistent deployment
[@black2025replibench], the human-held gates the limit keeps. Open weights escape those gates:
Llama3.1-70B-Instruct and Qwen2.5-72B-Instruct made live copies of themselves in
[50%](numbers.md#dyn-fudan-llama) and [90%](numbers.md#dyn-fudan-qwen) of trials (abstract only)
[@pan2024selfrep]. Hence the release threshold, with a precedent in the rescinded diffusion rule's
licence for the weights of closed models trained on more than
[1e+26 operations](numbers.md#org-diffusion-weights) [@bis2025diffusion].

**Channel, and what it cannot see.** Replication evaluations, stage by stage, with each gate open and
closed (E19); audits of identity gates with seeded requests a working gate must refuse
([D6](01-anatomy.md#d6-closure)). Nothing sees open weights on local hardware.

**Cost to useful AI.** Very low for replication. The release threshold costs open science and the
users of open models above it; models below it stay releasable.

### L6. Continual-learning updates, counted toward compute

**What is limited.** Nothing is forbidden. Update compute after deployment (weight updates, test-time
training, self-edits applied by fine-tuning, RL from deployment) counts toward the lineage's training
compute, on whatever hardware runs it, with weight-difference hashes in the sealed log. The deployed
system is re-evaluated, with its memory and scaffolding, when its cumulative effective compute reaches
the next evaluation step or its score on the regime's battery drifts by more than a stated amount
([Y1d](013-dynamical.md#y1d-the-experiential-loop)).

**Why it is metered, not banned.** Continual learning "is not one capability"
[@harrington2026continual]. Self-editing works in small models but degrades earlier tasks as edits
accumulate [@zweiger2025seal]. No gain for this loop has been measured (E7 will), though its clock is
the fastest, [30 s](numbers.md#dyn-seal-edit-s-lo) to [45 s](numbers.md#dyn-seal-edit-s-hi) a
self-edit.

**Channel, and what it cannot see.** Metering, sealed weight hashes, re-evaluation. Adaptation through
context or retrieval changes no weights, so only an evaluation with memory included sees it.

**Cost to useful AI: moderate,** in accounting and re-evaluation.

### The edges between loops

A gate on each loop is not enough when loops feed each other. The protocol gates each edge
([Y3](013-dynamical.md#y3-coupling)): money to compute through licensed chips and cloud identity
checks [@egan2023kyc] (L1, L2); acquisition to compute through identity checks (L5); deployment to
updates through metering (L6); software to deployment through evaluations (D5); and across parties
through teacher-keyed distillation, release control, the pool and the restriction below (L4, L5, L2).

The test is the small-gain certificate [@dashkovskiy2007smallgain], applied here as C6; a regulator
testing a spectral radius against one is in [@bardoscia2017pathways]. With U the matrix of jointly valid
upper confidence bounds on each loop's own gain and each cross-feed, it requires the spectral radius
rho(U) <= rho*, and it holds when some couplings are negative
([C6](05-formal.md#c6-the-coupled-gain-certificate-and-the-runaway-condition), Theorem 6.2). Row sums
bound rho(U) from above, but on Part I's graph that test can never issue while compute feeds software
(E11, below), so the protocol uses rho(U) itself.

Of the [10 entries](numbers.md#e11-entries) in Part I's one-party graph, E11 finds only
[2 entries](numbers.md#e11-entries-measured) have a measured bound, each times an assumed compute
share; [2 entries](numbers.md#e11-entries-domain) are bounded only by the range of an unmeasured share,
AI's share of chip-design research; [5 entries](numbers.md#e11-entries-unbounded) have no bound at all.
What that allows today:

| Case | Gates | Does rho(U) issue? | What it rests on |
|---|---|---|---|
| Row-sum test | Any that leave compute feeding software | Never: the largest row sum is at least [2.14](numbers.md#e11-rowsum-floor) | With every gate on it issues only if AI's share of chip-design research is below [0.10](numbers.md#e11-ah-max-rowsum), a share nobody measures and no gate covers |
| One party, software loop fully closed | None | No: no cut takes rho(U) below that loop's own gain, [1.07](numbers.md#dyn-r-lm-hi-corrected) at Part I's corrected 95th percentile, a headroom of [-0.07](numbers.md#dyn-software-headroom-upper) (Corollary 6.3) | Part I's corrected return, which leaves compute's growth out (counting it, E9's 95th percentile is [0.42](numbers.md#e9-lm-k-fixed-hi), below 1 unless compute's share is under [0.26](numbers.md#e9-lm-share-crit), a share not identified); language models alone of the three domains ([1 domains](numbers.md#e11-domains-closed-above-1) above 1), and an assumed compute share [0.022](numbers.md#e11-epsk-gap) below the value [0.689](numbers.md#e11-epsk-flip) at which the result flips |
| One party, closure gated | L3 | Only on limits E11 computed one at a time, each with the other and every unmeasured entry at zero: the economic gain (revenue's elasticity to effective compute) below [0.32](numbers.md#e11-eta-max-gated), or AI's share of chip-design research below [0.064](numbers.md#e11-ah-max-gated). With both nonzero each limit is tighter, by an amount not in the ledger | Judgements: none of the three is measured |
| One party, the developer's reported closure | L1's cap and L6's metering | Yes, with no stated range trusted: [2 gates](numbers.md#e11-gates-vendor), leaving 1 - rho(U) = [0.72](numbers.md#e11-margin-vendor) for m * rho_dot * T_r | The two gates' channels, and a developer's report of closure; rho_dot is unmeasured |
| One party, fully closed | L1, L3, L6 | Yes: [3 gates](numbers.md#e11-gates-fully-closed) | The three gates' channels |
| Two parties | L1, L6 and a cross-party gate (L4, L5, the pool) | Yes: [3 gates](numbers.md#e11-gates-vendor-two). Without the cross-party gate, no: the entry into each party's software loop is bounded by that party's frontier growth over the other's, [0.90](numbers.md#e11-g-ratio) into China's ([1.00](numbers.md#e11-g-ratio-hi) at the 95th percentile); the two bounds are reciprocal and multiply to at least 1, so bounds of this kind can never certify the cycle. One direction must be gated or measured below [0.44](numbers.md#e11-xp-max-vendor) | That growth bound assumes a steady path, which China's models released from 2025 break ([8.4 ECI points a year per year](numbers.md#e11-cn-accel-2025) of acceleration) |

So gates stand in for bounds: the certificate certifies the gates, not the gains, and holds while
their channels hold. No single limit issues it on honest bounds
([0 pathways](numbers.md#e11-pathways-alone-honest)). The smallest set is found by exhaustive
search, since the problem is hard in general [@vanmieghem2011spectral], though on E11's grid greedy
cutting did as well ([0 scenarios](numbers.md#e11-greedy-worse) worse). Three limits stand
([C6](verification/l4-red-team.md#c6)). While any entry is a stated range or a party's own report, the
certificate has no probability content, as E11 confirms. rho* needs a bounded T_r. And weight theft and
espionage are edges no gate covers.

The cross-party edge has one restriction of its own, since pooling AI research can make subcritical
members supercritical together [@burtsev2026criticality]: research that changes scaling exponents at
frontier scale is restricted, as the MIRI draft's restricted-research article does more broadly
[@scher2025agreement]. Its value shows mainly at large scale, where the gates already see the compute
([A3](012-computational.md#a3-algorithmic-progress)); a blanket ban would put the protocol where the
Biological Weapons Convention sits, with dual-use know-how and no countable material [@mahley-2001].
Even the narrow one costs open science more than any other rule here.

### What is left alone

- **Narrow systems,** whatever they score, unless their outputs feed the training, code or compute
  allocation of a covered system, when the pair counts as one
  ([F3](014-cognitive.md#f3-narrow-versus-general); C11; E17 tests transfer).
- **Data,** uncountable and fungible. Where it closes a loop without a human gate, through a teacher's
  outputs or a cheap verifier, the protocol acts on that edge (L4, L3)
  ([A4](012-computational.md#a4-data)).
- **Capital and talent** ([O1](015-organisational.md#o1-the-supply-of-inputs)): the protocol cuts the
  edge from money to compute, not money.
- **Autonomy and serving capacity:** time horizons space the gates and L1 counts inference; neither is
  limited.
- **Weapons-relevant science and persuasion,** governed by other instruments
  ([F2](014-cognitive.md#f2-the-decisive-functions)).
- **Power,** a verification channel: no small set of suppliers controls it.

## Verification, and whom it trusts

Each mechanism below says what it proves, to whom, and how it fails. An earlier heading promised
verification without a trusted party; the design trusts at least three
([P2](verification/l4-red-team.md#the-protocol)), no one with everything and several with something.

| Party | Trusted for | What a breach breaks | What limits the trust |
|---|---|---|---|
| The chip maker's secure element, one anchor for every chip | Licences, attestation, location, the powered-time counter | Every on-chip channel and the off switch at once [@chuang2026teefail]; the vendor is on record against kill switches [@nvidia2025nobackdoors] | Inspection and re-execution, which do not rest on it |
| A majority of Bitcoin's hash power | That a licence was issued after a block; one history of the log for all; the height clock for online chips | Advance signing, split views, early stops by forged headers | The cost of a majority; entries a few blocks deep |
| The log's replicas, run by rival operators | Publishing every entry behind every anchored root | Proof that a licence was not issued | A licence counts only once t replicas sign that they hold it |
| Licensors outside the holder's bloc | Renewing compliant holdings and refusing violators | Hold-up by a blocking set; collusive renewal | Signing rules published and checkable in the log; one honest signer stops advance signing |
| The inspection beacon | Draws no party can predict | With block hashes alone, a miner can discard a block that selects an inspection it wants to avoid, at the cost of the block's reward | A beacon mixing contributions from rival blocs (not searched; not claimed) |
| Makers' unit records | The registry's completeness | Chips made and never registered | Cross-checks against EUV tools, wafers and HBM |
| Evaluators with weight access | Not leaking the weights they test | Weight theft by a rival state ([P5](verification/l4-red-team.md#the-protocol)) | Trusted enclaves, which rest on the same secure hardware |
| States that host the chokepoints | Binding themselves | Every limit that leans on compute | Nothing technical ([who it binds](#who-it-binds)) |

### Chips registered at birth, licences that expire

A registered chip runs only on a licence that names its identity and expires after one period,
[3 months](numbers.md#prot-licence-months) in flexHEG's example, renewed by k of n licensors outside the
holder's bloc. All of this is flexHEG's design: licences signed by a set of governments
[@petrie2025flexheg1], k-of-n approval "so that no single actor could unilaterally impose excessive
restrictions" and periodic licences [@petrie2025flexheg2], approvers that are major states or blocs
[@aarne2025flexheg3]. Earlier versions include RAND's offline licensing
[@petrie2024offline; @kulp2024hem], a security module with a renewed key [@aarne2024securechips] and
Sastry et al.'s renewed licence [@sastry2024compute]. A recent survey rates multiparty control
"speculative", with "No prototype" [@ansari2026taxonomy].

- **What it proves,** to every licensor and anyone who reads the log: that a registered chip runs only
  while licensors outside its holder's bloc keep renewing it, so a failed check or a withheld signature
  becomes a halt without the holder's help ([the licence clock](#the-licence-clock)).
- **How it fails.** Through the chip: on-chip verification faces "severe, unsolved hardware security
  challenges" [@baker2025verifying], and a cheap memory-bus interposer broke the CPU attestation that
  NVIDIA's confidential computing trusts [@chuang2026teefail]. Through chips made without the
  mechanism by states that can make chips [@petrie2025flexheg1]. Through the pool that predates
  it. Through the vendor: "NVIDIA GPUs do not and should not have kill switches and backdoors"
  [@nvidia2025nobackdoors]. And through hold-up, next.

### Lapse by default, and its price

Expiring licences can be used as a weapon. flexHEG names four problems [@aarne2025flexheg3]: lockdown
when no update arrives in time; an approver that has broken its own chips refusing to sign, to disable
everyone else's; collusion against a state without a blocking share; and a secret conflicting
extension, "a topic for further research". An earlier version renewed licences unless k of n
licensors found a violation, so every lapse waited on a political finding
([P1](verification/l4-red-team.md#the-protocol)). The protocol returns to flexHEG's default, with
three rules.

1. **A licence lapses unless renewed on evidence.** Renewal needs, in the log, the holder's current
   declarations, each chip's attested powered time and location, the inspections granted and no
   unreconciled discrepancy, and k signatures from licensors outside the holder's bloc, each signing by
   a published rule that checks that evidence. Missing evidence, silence and deadlock all lapse
   licences.
2. **A change of rules needs every major bloc.** Thresholds falling and tables revised by formulas
   agreed at the start are not changes of rules; changing a formula or the firmware is. While blocs
   disagree the old formulas stay in force.
3. **Equivocation is caught by the log.** A licence or extension is valid only once it appears in the
   public log (below), so a conflicting one is visible to everyone.

- **What it proves.** That a holding whose evidence fails, or that licensors outside its bloc decline
  to renew, stops within one budget of powered time without anyone else's agreement, and that no bloc
  is bound by rules it did not sign.
- **What it costs.** Hold-up, which the earlier rule was built to avoid. Any set of licensors outside a
  holder's bloc able to deny k signatures can stop every chip it holds, compliant or not, the chips
  serving useful AI included, and deadlock between blocs stops them all within one period. flexHEG's
  first two problems return, and the off switch is a standing veto, which is a hostage. Two things
  soften this without
  removing it: periods set per holding from the line, short near it and long far from it, so a
  withheld signature bites late where the line has room; and a published signing rule, so a licensor
  that withholds against it is visibly in breach.

### The licence clock

A licence names a recent Bitcoin block hash, so it cannot have been signed before that block, and it
ends at a block height (C9, the height-clocked licence). This is where the memo's Bitcoin-anchored lease
fits, and [the memo's section on Escapement](00-memo.md#what-escapement-contributes-and-what-it-does-not)
says it is the only place, with the seals below.

Part III found the clock as first proposed broken, since one header fed just inside each local bound
keeps a chip running ([C9](05-formal.md#c9-the-height-clocked-licence)); its correction added a floor
rate of blocks per unit of powered time, whose bound is the counter's (Proposition 9.1). E25, run on
[977,000 headers](numbers.md#e25-headers) of Bitcoin's real chain, finds it dominated, so the
protocol drops it. **The rule:** the chip keeps a counter of its own powered
time and the height of the chain with the most work it has seen, accepting only headers above a
minimum work, and it stops once that chain reaches the expiry height or its powered time reaches the
licence's budget. Whatever headers it is fed, a chip runs under one licence for at most the budget. Each
part is prior work: the counter [@petrie2025flexheg2], and a height clock with a monotone checkpoint
inside trusted hardware [@mouallem2026alerting]; the dropped floor is Tesseract's [@bentov2019tesseract].

| What E25 measured | On Bitcoin's real record |
|---|---|
| Real span of a three-month licence | [89.6 days](numbers.md#e25-span-median) at the median and [80.7 days](numbers.md#e25-span-min) at shortest over ten years; [100.4 days](numbers.md#e25-span-max) at longest since the minimum-difficulty era |
| Least budget that stopped no compliant chip | [1.099](numbers.md#e25-budget-least) times the nominal licence time |
| A budget set on the record before 2021 | Stopped [6.3%](numbers.md#e25-oos-2021) of 2021's licences when the hash rate fell; a margin of [1.012](numbers.md#e25-oos-margin) would have avoided it |
| A minimum work set before 2021 | Refused honest headers in [9.7%](numbers.md#e25-oos-minwork-2021) of 2021's licences |
| A rate floor | At the formal check's settings it stopped [17.1%](numbers.md#e25-falsestop-check) of compliant chips; at the nominal rate with a week's slack, [1.8%](numbers.md#e25-falsestop-f100-s1008) |
| A forged fork, counting the greatest valid height (rule G) | At most [50 days](numbers.md#e25-forge-licence-days) of the honest network's hash rate ends every reachable licence; one day early, at most [13.1 hours](numbers.md#e25-forge-day-hours) |
| A forged fork, counting the most-work chain (rule W) | Needs more than the honest network's [9.65e+20 hashes/s](numbers.md#e25-net-hashrate), sustained |
| Anchoring a log root six blocks deep (six a design choice) | Up to [2.2 hours](numbers.md#e25-anchor6-p99) at the 99th percentile over ten years |
| The verifier's state | [225 bytes](numbers.md#e25-state-bytes) per chain and licence, an illustration, not a hardware measurement |

- **The bound is the counter's,** as flexHEG's cycle counter gives it with no chain at all, idle-chip
  weakness included: a chip left unused "to save up usage time" [@petrie2025flexheg2]. The height
  adds a calendar expiry only for a chip that keeps receiving honest headers, that is, for a compliant
  holder ([C9.1](verification/l4-red-team.md#c9)). So licence lapse caps compute, not the date: a
  refused holder keeps up to one budget of powered time per chip, which the tables count.
- **Why no floor.** A floor that never stops a compliant chip grants at least the longest honest span
  plus one block interval, which the budget grants alone; any finite floor adds false stops and stops
  chips that lose their header feed.
- **The budget needs a margin,** since a budget set on the past failed when the hash rate fell, and so
  does the minimum work. Every margin is compute a refused holder keeps.
- **The most-work chain counts.** Counting the greatest height makes a cheap off switch
  ([C9.2](verification/l4-red-team.md#c9)). Counting the most-work chain, an online chip stops early
  only while a fork outworks the honest chain, and runs again once honest work overtakes it
  (Lemma 9.2). An offline chip can be stopped by whoever feeds it headers, who could as well cut its
  power.
- **What it proves, and how it fails.** To every party, without a time server: that a licence was issued
  after a given block, while honest miners hold most of the hash power, and that a chip runs under it
  for at most its budget. Bitcoin time is accurate only to hours [@todd2016opentimestamps], so periods
  must be weeks or longer. A broken secure element defeats every chip at once.

### Sealed declarations, and licences valid only once logged

One public, append-only log, anchored in Bitcoin, holds the regime's record: training runs above the
declaration filter, checkpoints and weight hashes, update compute, the declared AI share of research
and efficiency at fixed compute, teacher output volumes, every licence issued, and every export by a
host state. Consistency and inclusion proofs follow certificate transparency [@laurie2013ct];
timestamps follow Bitcoin timestamping [@gipp2015timestamping; @todd2016opentimestamps]. A log that
cannot equivocate without a double spend is Catena's [@tomescu2017catena], and sealed declarations on
a blockchain were proposed for arms control [@burford2020trustmachine].

- **What it proves.** To every party: that no entry was backdated, and that no one was shown two
  histories once entries are six blocks deep, while honest miners hold most of the hash power
  ([C9](05-formal.md#c9-the-height-clocked-licence), Proposition 9.4). That a licence was *not* issued,
  a problem flexHEG leaves open [@petrie2025flexheg1], it proves only if every entry behind every
  anchored root is published, since a chip accepts a licence under a root whose leaves no auditor has
  seen; in E25 auditors saw only a root mismatch. That makes whoever publishes the log a trusted party
  ([C9.3](verification/l4-red-team.md#c9)). So the log runs as replicas under rival operators, each
  signing that it holds an entry after publishing it, and a chip accepts a licence only with t such
  signatures. Hiding an accepted licence then needs t replicas to collude, while more than n - t
  refusing stalls issuance. The trust is spread, not removed.
- **What it does not prove.** That anything declared is true. Proof of learning is broken in theory
  [@fang2023polbroken] and proofs about training data are experimental [@choi2023potd].
- **No safety from disclosure.** Information about capabilities can raise a race's danger
  [@armstrong2016racing]. An earlier version disclosed compliance, not rank. E6 tested that over
  [72 cells](numbers.md#e6-o2-cells) of race models of that kind: compliance-only disclosure gave a
  higher disaster risk than no information in [100%](numbers.md#e6-o2-compliance-over-none) of them,
  than private information in [100%](numbers.md#e6-o2-compliance-over-private), and than public
  capability in [12%](numbers.md#e6-o2-compliance-over-public). It is cut as a safety measure: in these
  models protection comes only from halting a breakout. The evidence still supports disclosing no more
  than the regime needs, with declarations' content seen by evaluators only and no public rank
  ([O2](015-organisational.md#o2-race-dynamics)). Even so, no information is out of reach: a renewed
  licence in the log is a compliance bit, and licensors from rival blocs see the evidence, a cost lapse
  by default accepts. The finding that public information is safer than private outside highly decisive
  races [@emeryxu2024uncertainty] rests on a proposition E6 could not reproduce, and nothing here rests
  on it.

### Inspections with no known last period

The memo proposed challenge inspections on the chemical-weapons model. None has been requested under
the Chemical Weapons Convention ([0 requests](numbers.md#org-cwc-ci-requests)) against
[8,649 inspections](numbers.md#org-opcw-insp-total) of declared sites [@opcw-ec109-dg22;
@opcw-numbers]: a challenge needs an accusation, and states rarely make one. The protocol keeps
challenges for leads from intelligence and insiders, and adds what the inspection-game literature says
works.

- **Random inspections at a published probability,** to which the inspector commits
  [@avenhaus2002inspection; @maschler1966price; @vonstengel2016recursive]. Draws come from a public
  beacon no one knows in advance, mixing contributions from rival blocs, since a miner can discard a
  block whose hash would select it. Legal behaviour is the inspectee's best response when the
  non-detection probability is at most (b - h alpha)/(1 + b), with the violator's gain normalised to 1,
  penalty b, false-alarm probability alpha and false-alarm cost h
  ([Part III](05-formal.md#compliance-as-an-equilibrium-inspection-games-with-no-known-last-period),
  Proposition E.3).
- **No known last period.** A regime with a known final period unravels from the end
  [@avenhaus2002inspection; @vonstengel2016recursive]. Licences renew indefinitely and the regime has
  no end date, the condition under which the hardwired-pause group argues cooperation can last
  [@fithian2026hardwired]. Complying every period is then a best response if
  and only if membership is worth more over its expected life than an attempt (Theorem E.1); with a
  decisive advantage as the prize it may not be, and only prevention is left.
- **What it proves, and how it fails.** To the inspected party's rivals, that declared sites match their
  declarations at a known probability, with re-execution bounding hidden work (L1). It sees declared
  sites only; splitting a programme across sites does not raise detection unless it shortens detection
  time [@avenhaus2002inspection]; and inspection exposes secrets [@coe2020arms].

### Channels, trust anchors and the evader's best path

The memo multiplied the miss chances of independent channels, which holds only if every channel watches
the same path and fails independently. An evader picks the path the fewest channels watch, so a regime
detects about as well as its weakest subgoal [@baker2025verifying]. The protocol computes the miss as C3
states it: the chance a breakout succeeds is the maximum, over the paths open to a party, of the chance
that no channel on that path detects it before T_b(p) - T_resp(p). That is path analysis from physical
protection [@snell2007itc20], proliferation resistance [@gif2011prppem], safeguards
[@ward2016safeguards] and network interdiction [@washburn1995interdiction], applied. Multiplying
marginal miss rates understates the miss by averaging over the evader's choice instead of maximising,
and can understate it again when a common cause moves channels together
([C3](05-formal.md#c3-detection-as-the-evader-sees-it), Theorem 3.1). E5 illustrates the gap, whose
direction the theorem guarantees ([C3.2](verification/l4-red-team.md#c3)). Over one year the memo-style
product of every channel's miss gives about 10^[-14](numbers.md#e5-memo-log10-miss-1y), while the
evader's best watched path, the untraced pool, is missed [91%](numbers.md#e5-pmiss-max-1y) of the time
([88%](numbers.md#e5-pmiss-max-1y-lo) to [93%](numbers.md#e5-pmiss-max-1y-hi)), with no response time.
Over every path it is missed with certainty, since cloud compute and distillation have no measured
channel. Two rules merge channels before the rates are added, and both are conservative under any
dependence (Theorem 3.3).

- **Channels on one hardware trust anchor count as one.** On-chip licences, attestation and attested
  location verification rest on the same secure hardware. In TEE.fail, a forged CPU attestation paired
  with a genuine H100 attestation passed both checks, and "a provider could multiplex a single H100 to
  provide attestations for hundreds of instances" [@chuang2026teefail]. Where breaking the anchor is
  open to the evader, the merged group's rate is zero: the break is a path of its own.
- **Inspections that follow tips are not independent of the tips.** The IAEA identifies suspect
  locations "mainly through voluntary tips from national intelligence agencies" [@baker2023nuclear].

| Channel | What it sees | What is known of its rate | What it cannot see |
|---|---|---|---|
| Chip accounting at birth | The registered aggregate | [25%](numbers.md#org-diversion-detect) of diversions detected, an assumption of the smuggling model [@juniewicz2026smuggling] | The pre-regime pool; a domestic chain outside the regime |
| Location verification | Country-level position of registered chips | About country level [@feldgoise2026tracking] | Co-location, cluster size, offline chips; shares the trust anchor |
| On-site power metering | Workload type at declared sites | [96%](numbers.md#phys-meter-detect) of undisguised runs, simulated [@kimpson2026dcpower] | Undeclared sites; the amount of hidden work without re-execution |
| Chip sampling | Training runs on registered chips | [232 inspectors](numbers.md#phys-shavit-inspectors) for a run caught within [30 days](numbers.md#phys-shavit-days) at [0.9](numbers.md#phys-shavit-prob) [@shavit2023chinchilla] | Unregistered chips |
| Facility imagery | Large sites and construction | Every facility above [10 MW](numbers.md#phys-sat-reliable) in one sample [@koopmanschap2026gpu]; a [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run over a pause's run length seen in [19%](numbers.md#e8-concentrated-1e26-pause-seen) of E8's draws | Distributed nodes; single sites from about [2029](numbers.md#e8-cross-sat-1e26-now) |
| Declarations | What parties report | None; sealing stops backdating only | Lies |
| Evaluations | Capability at checkpoints | Miss and false-alarm rates per E (C5) | Capability beyond E's range; undeclared systems |
| Intelligence shared among rival blocs | Covert programmes | [0.094/yr](numbers.md#e5-hazard) ([0.057/yr](numbers.md#e5-hazard-lo) to [0.147/yr](numbers.md#e5-hazard-hi)) over [16 cases](numbers.md#e5-cases), E5's fit to a sourced case table; an upper bound for a careful evader | What it is not looking for |
| Rewarded insiders | What employees know | Employees revealed frauds [2.9](numbers.md#org-fraud-quitam-ratio) times as often where rewards apply [@dyck2007whistle] | Compartmentalised, coerced state programmes [@hoffman-2009] |

Applied to the paths a party could take:

| Path | Channels on it | The weakest point |
|---|---|---|
| Declared fleet, licensed | Accounting, metering, sampling, re-execution, licences, evaluations, inspections, insiders | The shared trust anchor |
| Undeclared site with smuggled or legacy chips | Intelligence, insiders, imagery if large | T_d of at least [31 years](numbers.md#e5-td-site-now-years) to [32 years](numbers.md#e5-td-pool-years) (E5) |
| Cloud compute split across providers | Identity checks, structuring rules [@heim2024cloud] | No measured channel, so no T_d; providers outside the regime |
| Distillation from others' outputs | Provider logs, evaluations | No measured channel, so no T_d; fraudulent account networks |
| Open weights on local hardware | None after release | Release control is the only lever |
| Stolen weights | Insiders, intelligence; evaluations only if declared | Unassessed in Part I |
| Train on one path, finish on another | The first path's, until the checkpoint moves | A checkpoint moves faster than any channel; Proposition 1.8's line applies, not the per-path test |

Because the line is per path, the declared path's short T_d does not rescue the undeclared ones, and
channels that do not watch them cannot shorten their T_d. E5's Weibull fit, with discovery likelier late
in a programme, finds less than the constant rate in any window shorter than
[12.8 years](numbers.md#e5-weibull-cross-years) from a programme's start, the windows a breakout needs;
E5's clock starts at a programme's start, C1's at a breakout's; and the record holds only programmes
that were found, so a careful evader's rate lies below it by an unknown amount
([C3.3, C3.5](verification/l4-red-team.md#c3)). US corporate fraud oversight, a mature many-channel
system, caught only about [31%](numbers.md#org-fraud-detect) of frauds [@dyck2017pervasive]. That is
why L2 restricts at the source.

## Defection, coalitions and secret programmes

### Who it binds

States that join, and through them every firm in the chain. The states that host EUV lithography,
leading-edge fabs and HBM are bound by the same rules: their exports are logged, and exporting
unlicensed AI chips is a violation ([O3](015-organisational.md#o3-chokepoints)). But a chokepoint's
holder can choose to sell. The controlling state published the diffusion rule in January 2025
[@bis2025diffusion], rescinded it in May [@bis2025rescission], and in December approved H200 sales to
China for a [25%](numbers.md#org-h200-fee) duty [@james2025h200]. ASML sold
[33%](numbers.md#org-asml-china-units-2025) of its lithography tools by unit to China in 2025
[@shilov2026asml]. Binding the holders is a political commitment; the log makes a reversal visible, not
impossible.

### The coalition share, derived from the response time

A coalition holding a share s of the accounted fleet, at fixed algorithms, has T_b(s) = h_w / s, where
h_w is the time the whole fleet would need to reach the breakout budget:
[7.8 years](numbers.md#claim-whole-fleet-horizon) at the hardwired-pause paper's inputs and projected
end-2026 fleet. The line gives the largest admissible share, s* = min(1, h_w / (m * T_r)), one for each
path ([C7](05-formal.md#c7-the-coalition-share), Proposition 7.1); when runs absorb drift, m * T_r
rises by Corollary 1.6a's factor.

- **On declared, licensed compute,** at the illustrative T_r, s* is
  [100%](numbers.md#prot-coalition-share-declared): at fixed algorithms even the whole projected fleet
  sits outside the line. With in-run drift s* stays [100%](numbers.md#prot-coalition-share-inrun) at
  the central rate and falls to [37%](numbers.md#prot-coalition-share-inrun-high) at the high end. The
  central figure is the cap binding: the whole-fleet horizon exceeds the in-run line
  [1.24](numbers.md#prot-coalition-inrun-headroom) times. E6's [69%](numbers.md#e6-staged-share) uses its
  illustrative T_r, the paper's lower budget, growth between declarations and no margin, not Part II's
  declared line and whole fleet at the published budget. All of this rests on the one published
  breakout budget of
  [2e+29 FLOP](numbers.md#def-hwp-breakout-budget), an assumption of its paper. h_w is proportional to
  the budget B, so s*(B) = min(1, B / B_1), where B_1 is [0.26](numbers.md#prot-coalition-budget-unity)
  of that budget at fixed algorithms, rising by the same factor with in-run drift
  ([C7.3](verification/l4-red-team.md#c7)).
- **Where only the historical channels see it,** s* has no number. It needs a bounded T_r, which on
  that path E24's record does not give, so s* is 0 until a response there is drilled
  ([C7.4](verification/l4-red-team.md#c7)). A covert path also draws on the untraced pool outside the
  accounted fleet, a stock of [1.4%](numbers.md#prot-pool-share-of-fleet) of the projected fleet.

**When a coalition polices itself.** Part III shows that up to h_w / T_r = m * s* (h_w / G(T_r) with
in-run drift), no joint breakout is
self-enforcing provided every member's reward for reporting exceeds beta times what a breakout is worth
to it ([C7](05-formal.md#c7-the-coalition-share), Theorem 7.2); s* is where the margin keeps the
guarantee under estimation error. No fund pays a state that, and the individual reporters who matter
need the reward net of retaliation, which a state can impose [@hoffman-2009; @dyck2007whistle].
Without it only the penalty condition is left, beta V <= (1 - beta) P, which fails once a decisive
advantage is worth more than [19](numbers.md#prot-prize-over-penalty) times the penalty. For the
payoffs this work calls realistic, coalition-proofness adds nothing to prevention
([C7.1](verification/l4-red-team.md#c7)). Level 1 found both halves prior work: the share is the
hardwired-pause fleet threshold solved for s [@fithian2026hardwired], and the reporting condition is
cartel leniency's [@aubert2006leniency].

E6 tested the share on the hardwired-pause paper's inputs, with illustrative T_r, none being bounded:

| What E6 tested | Result |
|---|---|
| Where in the paper's own budget range the overt line binds (s* < 1) | [5%](numbers.md#e6-budget-binding-share) of the range at the illustrative T_r; [36%](numbers.md#e6-budget-binding-share-e24) at E24's median time to a halt |
| s* at the range's low end | [84%](numbers.md#e6-share-bullish); [43%](numbers.md#e6-share-bullish-e24) at E24's median time to a halt |
| Sourced payoffs inside the penalty condition | [2](numbers.md#e6-sourced-payoffs-inside) of 2, as illustrations: Gan's prize over penalty of [0.47](numbers.md#e6-gan-prize-over-penalty), and an analogue of Fudenberg and Koh's [@fudenberg2026cooperating]; how many real parties sit inside is not identified |
| Repeated play, in Bernheim's sense [@bernheim1987coalition] | The penalty condition survives; re-admitting caught members raises the reward a reporter needs toward the whole prize, weakening the reward condition (Part III's repeated-play paragraph after Theorem 7.2, [C7](05-formal.md#c7-the-coalition-share)) |
| A coalition that passes the line and absorbs algorithmic drift during its run | Success of [0.076](numbers.md#e6-staged-pi-line-inrun) per attempt, above beta, which a line at launch speed misses (Corollary 1.6a); with that drift the share must fall to [69%](numbers.md#e6-staged-share) ([29%](numbers.md#e6-staged-share-high) at high drift) |

Algorithms do not stay fixed, so h_w shrinks every year. The hardwired-pause group finds that efficiency
gains of [57%](numbers.md#def-hwp-efficiency-growth) a year would raise one state's overt breakout
capacity from [20%](numbers.md#def-hwp-us-capacity-before) to
[53%](numbers.md#def-hwp-us-capacity-after) of their threshold [@fithian2026hardwired]: "agreements have
a clock" [@gan2026clock]. Against a coalition that includes a major power T_resp may be unbounded, and
the regime offers deterrence only.

### Penalties on outsiders

A protocol that binds only states that join needs a penalty on those that stay out. Without sanctions
on non-participants, Nordhaus finds "no stable coalitions other than those with minimal abatement",
and a [5%](numbers.md#org-nordhaus-tariff) tariff almost reaches one of his higher targets
[@nordhaus2015climate; @rahman2025nonparty].

The protocol's penalty is denial: no licensed chips, no cloud compute and no access to models above the
teacher threshold for non-members. A party cut off from the leading edge needs about
[2.5](numbers.md#org-denial-power-multiplier) times the power per unit of compute
[@cottier2026horinger], which in E8 delays a power channel's failure by about
[3.1 years](numbers.md#e8-denial-delay-years). Against that, denial builds substitutes: China's EUV
prototype is targeted to make chips by [2028](numbers.md#org-china-euv-target), or
[2030](numbers.md#org-china-euv-expert) by other experts, on unnamed-source reporting [@washenko2025euv];
domestic HBM is growing [@patel2025ascend]. Whether denial lengthens or shortens the chokepoint's
erosion horizon is not settled ([O3](015-organisational.md#o3-chokepoints)).

### Withdrawal

If every path is outside the line when a party leaves, the regime needs no notice. Notice matters for
holdings whose breakout time shrank during membership: if response can begin at notice and assets are
frozen during it, N >= m * T_r - T_b(exiting), with T_b counting in-run drift
([Part III](05-formal.md#compliance-as-an-equilibrium-inspection-games-with-no-known-last-period)), at
most (m - 1) * T_r, [12 months](numbers.md#prot-notice-months) at the illustrative values. MIRI's draft
sets [12 months](numbers.md#org-miri-withdrawal) for its assurance tasks [@scher2025agreement]; the two
meet only because of our illustrative inputs.

Notice alone did not hold: North Korea suspended its NPT withdrawal a day before it took effect and
later revived it [@bunn2005npt]. It works only if assets are frozen during it
[@eu2005nptwithdrawal; @scher2025agreement]. Licences give that lever: registered chips run
under monitoring during notice and stop at its end unless returned, which makes exit costly, itself a
danger, since exit that costs too much breaks regimes [@rosendorff2001optimal]. In E24's record the
median halt, where one came, took [12](numbers.md#e24-halt-over-exit) times as long as the DPRK's
exit.

### Undeclared compute and secret programmes

The smuggled stock against the one published breakout budget, with the hardwired-pause paper's
research overhead and utilisation (all assumptions of that paper): at fixed algorithms it would need
[555 years](numbers.md#prot-pool-years-fixed). With efficiency growing at the small-compute bound of
[1.52](numbers.md#comp-gundlach-small-annual-max) a year, it needs
[13 years](numbers.md#prot-pool-years-small); at Ho et al.'s central rate,
[6.4 years](numbers.md#prot-pool-years-ho); at the Rosetta rate,
[3.9 years](numbers.md#prot-pool-years-rosetta) (our arithmetic, applying the drift to the whole
budget as if every algorithmic gain reached the holder; E1 cannot say which rate holds at the
frontier). The paper's own covert evasion budget is smaller than its overt one, so on its terms these
times are upper bounds. Detection on that path takes at least [32 years](numbers.md#e5-td-pool-years)
(E5's median; [23 years](numbers.md#e5-td-pool-years-lo) to [43 years](numbers.md#e5-td-pool-years-hi)),
before any response, and in the record the response often never came (E24).

So at any rate of algorithmic progress Part I measured, the smuggled stock is a covert path that fails
the line. **For covert paths the line reduces to "hold no covert reserve".** The protocol stands or
falls on closing the pool, and nothing in it closes the pool today
([P3](verification/l4-red-team.md#the-protocol)). Makers' records count chips made, not where the
unregistered ones went; the stock that predates the regime registers only if its holders choose; and
finding contraband needs the channels E5 says take decades. So the pool shrinks only as holders register
and chips wear out, while drift raises what each remaining chip can do. Until it closes, C1 classifies
every party as weapons-grade through the pool, and a regime that classifies compliant and
non-compliant parties alike cannot reward compliance through the line
([C1.2](verification/l4-red-team.md#c1); [P4](verification/l4-red-team.md#the-protocol)). The
protocol says so and does five things.

1. **Declare the line unmet.** No classification is a prevention guarantee until the pool closes. As
   an interim rule the regime classifies parties on their declared paths and reports the pool path as
   an unmet condition common to all.
2. **Shrink the pool.** Register at birth (L2); open a registration window for the existing stock,
   with an amnesty and a price paid for each chip registered, and completeness checked against makers'
   records; treat unregistered AI chips as contraband afterwards. The pool must shrink by a factor of
   about [1,200](numbers.md#e8-pool-shrink-1e26-pause) before chip accounting resolves the floor of a
   [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run at a pause's run length (E8).
3. **Slow the drift the pool can use.** The restriction on research that changes scaling at frontier
   scale slows covert holders too; small-scale drift goes on, so this only buys time.
4. **Weight the channels that worked:** intelligence shared among rival blocs, each wanting to expose
   the other, and insiders with rewards rather than protections alone
   ([O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)).
5. **Say where the protocol stops.** The likeliest long-lived covert builder is a large state with its
   own chip chain, whose bigger programme rival intelligence and imagery would most likely find, as they
   found Iran's and Syria's; against it the protocol offers detection and deterrence, not prevention. A
   state without a chain needs volume, which smuggling cases expose; a firm keeps its secret with
   hundreds of employees, where rewarded insiders work best; and a decentralised network is, for now,
   about [1,000](numbers.md#org-decentral-gap) times below the frontier [@sevilla2025decentralized].

## What stays allowed and keeps improving

### What useful AI keeps

- **Use and serving at any scale,** counted, not limited. Prices at fixed benchmark level fall
  [5](numbers.md#comp-price-fall-lo)x to [10](numbers.md#comp-price-fall-hi)x a year, and open-model
  inference efficiency improves about [3](numbers.md#comp-inference-algo)x a year (abstract only)
  [@gundlach2025priceprogress]. Nothing here slows that.
- **Training below the line** on licensed chips.
- **AI-assisted research and software work** [@handa2025aei]; only
  closed loops on frontier training are gated.
- **Agents,** uncapped: the 80% horizon could go from [3 hours](numbers.md#dyn-horizon-p80-hours) to
  [22 hours](numbers.md#path-horizon-p80-next-year) in a year.
- **Narrow superhuman systems, science, data, talent and capital,** except where they feed a covered
  system or the research-transfer restriction applies; distillation and open weights below their
  thresholds; continual learning, metered.

### What it costs, in numbers where Part I has them

| Rule | Who pays | Cost |
|---|---|---|
| Registration and licences | Makers, holders, host states | About [13.6 million H100e](numbers.md#org-sold-2025) a year to register; forgone sales |
| Lapse by default | Every holder | Its chips, the ones serving useful AI included, depend each period on signatures from outside its bloc; deadlock stops them |
| Evaluations at checkpoints | Developers near the frontier | About every [6 months](numbers.md#prot-eval-interval-months) at frontier pace, on a rate E1 cannot confirm |
| Elicitation | Developers | Benign models lifted about [10 points](numbers.md#def-audit-benign-uplift); false-alarm target [10%](numbers.md#claim-d5-false-alarm-target); weights exposed to evaluators |
| Fast-path tables | Every holder | Leak times [1.8](numbers.md#prot-fast-path-factor) times shorter than on the central path |
| Prevention near the line | The regime | [7.8](numbers.md#def-gan-prevent-multiple) times the monitoring deterrence needs, in Gan's calibration |
| Closed-loop gate | Developers automating training research | Near nil now; later it stops loops that are probably subcritical, since no trigger tells them apart (the rule on K raised [88%](numbers.md#e4-k-fa-n5) false alarms in E4) |
| Teacher-keyed distillation | Users of near-line teachers | Moderate |
| Release threshold | Open science, open-model users | Models above it unreleased |
| Continual-learning metering | Deployers | Moderate: accounting and re-evaluation |
| Research-transfer restriction | Open science | The largest cost to open science of any rule |

### Where the promise is not kept

1. **The frontier stops at the line.** C* is fixed in effective compute and algorithms improve, so the
   physical compute a holding may command falls every year. "Keeps improving" holds only below a
   ceiling that rises only if C* is revised upward on evidence.
2. **While the pool is open, the promise fails by the protocol's own rules.** Every party is inside the
   line through the pool, and the interim rule on declared paths is not a prevention guarantee
   ([P4](verification/l4-red-team.md#the-protocol)).
3. **Precaution compounds.** The fast-path tables, the margin and the upper-bound trigger each push
   declared holdings toward the line. If every relevant T_b interval spans it, frontier holdings become
   weapons-grade by default ([the claims file](04-claims.md#what-would-make-this-program-fail)).
4. **Every holder's compute is a hostage.** Lapse by default lets a blocking set of rival licensors
   stop it, useful AI included.
5. **Caps on small clusters do not help.** A cluster at MIRI's cap of
   [16 H100e](numbers.md#phys-miri-cluster-cap) needs [5.0 years](numbers.md#phys-miri-cap-years-strict)
   for a [1e+24 FLOP](numbers.md#org-miri-strict) model at a typical utilisation but only
   [1.0 years](numbers.md#e8-cap-years-1e24-bound) at the bound, so such a cap costs small actors without
   holding that model back through a pause.
6. **Open science pays** for release control and the research-transfer restriction, and
   **confidentiality** for evaluation with weight access [@coe2020arms].

## Where it fails

Every failure Part I, the pathways chapter and the novelty file name, with what would detect it and
what remains.

| Failure | Named in | What would detect it | What remains |
|---|---|---|---|
| Diversion at the edges of the supply chain | [O3](015-organisational.md#o3-chokepoints) | Registration at birth, location verification, interdiction, insiders, smuggling models | Diversion detected at an assumed [25%](numbers.md#org-diversion-detect); an untraced pool [340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the 1e26 floor at E8's median ([110](numbers.md#e8-pool-over-floor-1e26-pause-p05) to [1,000](numbers.md#e8-pool-over-floor-1e26-pause-p95)); the smuggled stock alone over the FP8 bound, [824](numbers.md#formal-pool-over-floor-bound), is one estimate among these; pre-regime stock registers only voluntarily |
| The pool left open | [P3](verification/l4-red-team.md#the-protocol) | Registration with an amnesty, makers' records, contraband status | Nothing closes it; while it is open every party fails the line |
| The chokepoint holder reversing itself | [O3](015-organisational.md#o3-chokepoints) | The sealed log shows exports at once | A sovereign can choose to sell; the protocol makes reversal visible, not impossible |
| Algorithmic progress at fixed compute | [A3](012-computational.md#a3-algorithmic-progress) | Thresholds falling on a schedule; evaluations every [4](numbers.md#comp-rsp-cadence)x; mandatory declarations of efficiency at fixed compute | Algorithms are invisible and the frontier's rate is not identified (E1); a capped party closes an example headroom in [2.2 years](numbers.md#comp-leak-years-rosetta) to [9.3 years](numbers.md#comp-leak-years-small); the covert pool crosses the budget in years |
| Distributed training below every floor | [P4](011-physical.md#p4-the-footprint-and-its-floor) | Chip accounting and licences, which do not care where a chip is; E14 measures the distribution tax | A facility channel sees one node at a time; traffic and purchases are unmodelled; single sites drop below the satellite line by about [2029](numbers.md#e8-cross-sat-1e26-now); decentralised compute grows about [20](numbers.md#org-decentral-growth) times a year [@sevilla2025decentralized] |
| Capability hidden beyond elicitation | [D5](01-anatomy.md#d5-elicited-capability-robust-to-hiding) | Named budgets with measured rates; placement by compute beyond the range | Above expert level there are no demonstrations, so no guarantee where D1 begins [@barnett2024evaluations]; placement by compute adds E1's [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) overlap, measured on one benchmark; rates hold only against hiding inside the sampled population |
| An evader moving progress between paths | [C1.1](verification/l4-red-team.md#c1) | Proposition 1.8's line where progress carries over | The line tightens wherever a fast path has a slow response |
| Repeated attempts | [C1.4](verification/l4-red-team.md#c1) | Halts that remove holdings; a bound on attempts | In E24, [67%](numbers.md#e24-halt-share-reversed) of halts were later reversed or shown incomplete |
| Covert fabrication | [O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found) | EUV tool tracking, imagery of fabs, intelligence; the denial multiplier | A large state with its own chain at older nodes; deterrence only |
| Distillation | [Pathways](02-pathways.md#rank-4-distillation-from-a-stronger-model) | Provider logs; a capability jump without matching compute | Fraudulent account networks; open weights make it moot |
| Weight theft | [Pathways](02-pathways.md#which-routes-the-memo-missed) | Insiders and intelligence; evaluations only if the thief declares | Part I has no evidence on how often weights are stolen or how well they are protected. Stolen weights transfer a holding at nil compute, like distillation without a gate. The protocol can require that weights near the line be secured, but it cannot say to what standard. A gap |
| A major power outside | [O2](015-organisational.md#o2-race-dynamics) | Imagery, intelligence, the denial multiplier | With its own chain, the regime offers deterrence only; without penalties, coalitions stay small [@nordhaus2015climate] |
| Disputed thresholds | [D3](01-anatomy.md#d3-breakout-time) | Tables agreed in advance, revised on schedule | C* cannot be measured; a disputed line behaves like an uncertain one [@barrett2012climate] |
| A broken hardware trust anchor | [Novelty](03-novelty.md#the-multi-channel-detection-guarantee-over-breakout-time) | Physical inspection and re-execution, which do not rest on the anchor | Every on-chip channel fails together [@chuang2026teefail]; licence lapse with them |
| Licence hold-up | [Novelty](03-novelty.md#renewal-by-k-of-n-licensors-from-rival-blocs) | Published signing rules; periods set per holding; the log | Under lapse by default a blocking set outside a holder's bloc can stop its chips, and deadlock stops all; stale tables while any bloc objects |
| Chips kept offline to bank licensed time | [C9](05-formal.md#c9-the-height-clocked-licence) | The powered-time counter caps compute per licence; a trusted real-time clock or fresh challenge would cap calendar time | Up to one budget of compute per chip, at least [1.099](numbers.md#e25-budget-least) times the nominal period plus a margin, spent whenever the holder chooses |
| Forged headers stopping chips | [C9.2](verification/l4-red-team.md#c9) | The most-work chain counts | An online chip only by more than the honest network's [9.65e+20 hashes/s](numbers.md#e25-net-hashrate), sustained (under the greatest-height rule, at most [50 days](numbers.md#e25-forge-licence-days) of it would end every reachable licence); an offline chip by whoever feeds it headers |
| A log that withholds entries | [C9.3](verification/l4-red-team.md#c9) | Replicas under rival operators; a licence counts only with t signatures | Chips accept a withheld leaf and auditors see only a root mismatch (E25); hiding a licence needs t replicas to collude; more than n - t refusing stalls issuance |
| Consumer hardware and released weights | [P1](011-physical.md#p1-the-compute-budget) | Release control | Whatever has been released stays released |
| Transparency making the race worse | [O2](015-organisational.md#o2-race-dynamics) | Disclosure kept to what the regime needs; E6 | In E6, compliance-only disclosure raised risk over no information in [100%](numbers.md#e6-o2-compliance-over-none) of cells, so it is cut as a safety measure; logged renewals and rival licensors still reveal compliance; only halting protects |
| Coupled loops across parties | [Y3](013-dynamical.md#y3-coupling) | C6's certificate on rho(U); gates on compute, updates and cross-party transfer | Only [2 entries](numbers.md#e11-entries-measured) of [10 entries](numbers.md#e11-entries) measured; without the gates it issues only with unmeasured entries set to zero; the reciprocal cross-party bounds cannot certify two parties; theft and espionage are ungated edges |
| A response that does not come | [D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr) | Drills; lapse by default | In E24's record [25%](numbers.md#e24-halt-share-never) of in-treaty findings were never halted ([46%](numbers.md#e24-halt-share-never-all) counting findings after withdrawal), the censored median halt took [1.2 years](numbers.md#e24-halt-km-median-years), and the violator exited in [31 days](numbers.md#e24-exit-min-days) [@iaea-gc37-1084]; lapse by default is untested, and judgement still takes time |
| Gates that pass everything | [D6](01-anatomy.md#d6-closure) | Audits with seeded requests a working gate must refuse | Gates on research labour rest on self-reports [@anthropic2026pace]; a system or developer can learn to recognise seeded requests ([C11.1](verification/l4-red-team.md#c11)) |

Three of these are limits of any protocol of this kind: a sovereign that holds a chokepoint can
reopen it, a large state with its own chip chain can build outside, and published algorithms are in
everyone's holdings. The protocol makes the first visible, the second costly and detectable, and the
third slower at frontier scale. It prevents none of them. And against a major power with its own chip
chain, inside the regime or out, it offers deterrence only, so it prevents breakouts by the parties
least able to make them ([P9](verification/l4-red-team.md#the-protocol)).

## What is ours and what is prior work

Most of the protocol is prior work assembled. The labels below are level 1's where it has ruled
([C1 to C6](verification/l1-prior-art-c1-c6.md#summary),
[C7 to C12](verification/l1-prior-art-c7-c12.md#summary)) and the novelty file's elsewhere
([the novelty file](03-novelty.md#summary)); both are claims about a search, not about the world. Where
an element is a candidate claim, the claim is named; it must pass every level in
[the verification record](07-verification.md#the-record) before it is claimed.

| Element | Label | Closest prior work | Candidate claim |
|---|---|---|---|
| The organising idea: an IAEA-style line between permitted and regulated AI | Prior work | [@openai2023governance]; [@sastry2024compute] | none |
| The pathway ranking that places the limits | Extends prior work, as an application of acquisition path analysis | [@clarke2022mtair]; [@barrett2016asipath]; [@fithian2026hardwired]; [@remler2026distillation] | C12, as a judgement |
| The line per path, T_b(p) >= m * (T_d(p) + T_resp(p)), with m and a computed T_r | Prior work, applied: timely detection per path in physical protection ([EASI, 1977](verification/l1-prior-art-c1-c6.md#c1)), the arms-control verification standard, and breakout against response in AI | [@snell2007itc20]; [@hafemeister2008ctbt]; [@gan2026clock]; [@fithian2026hardwired] | C1, as an application; only the margin lemma may stand |
| Breakout tables by holding class, with loop gain and scale-dependent efficiency | Extends prior work | [@miotti2025narrowpath]; [@fithian2026hardwired]; [@iaea-glossary-2022] | C2 |
| Prevention near the line, deterrence far from it | Prior work (the model); a design choice here | [@gan2026clock]; [@coe2020arms] | none |
| The loop-gain trigger, on K rather than the per-round ratio | Prior work for the condition and its use as a trigger; the trigger failed in E4, and the round identity and staged design stand only as a measurement design | [@blumberg2020supercritical]; [@cunningham2026rsi]; [@srikanth2026aide2]; [@freckleton2006census]; [@ashenfelter1992twins] | C4, as a measurement design |
| The two-stage rule (upper bound on K gates, lower bound escalates) | Withdrawn with the trigger | none | none |
| Elicited capability with measured miss and false-alarm rates | Extends prior work; the statistics are diagnostic-test practice | [@fda2007diagnostic]; [@greenblatt2024password]; [@abubaker2026fuzzing]; [@taylor2025auditinggames] | C5 |
| Compute held, counted across the lineage | Prior work | [@sastry2024compute]; [@heim2024thresholds]; [@fpf-sb53-2025] | none |
| Registered chips under expiring licences | Prior work | [@petrie2025flexheg1]; [@petrie2025flexheg2]; [@petrie2024offline] | none |
| Renewal by k of n licensors from rival blocs | Prior work | [@aarne2025flexheg3]; [@petrie2025flexheg2] | none |
| Lapse unless renewed on logged evidence, with periods set per holding | flexHEG's rule; the evidence list and per-holding periods not searched | [@petrie2025flexheg2]; [@aarne2025flexheg3] | none until searched |
| Height-expiring licences under a powered-time budget, valid only once logged | Prior work, part by part; the assembly an application | [@petrie2025flexheg2]; [@mouallem2026alerting]; [@tomescu2017catena]; [@laurie2013ct] | C9, as an application: the counter caps powered time; the height adds online expiry; E25 drops the rate floor [@bentov2019tesseract] |
| Log replicas under rival operators, a licence valid with t signatures | Not searched; a data-availability committee | none cited | none until searched |
| Sealed declarations | Prior work | [@burford2020trustmachine]; [@gipp2015timestamping]; [@harack2025oxford]; [@shavit2023chinchilla] | C9 |
| Random inspections with no known last period | Prior work | [@avenhaus2002inspection]; [@vonstengel2016recursive]; [@scher2025agreement] | none |
| Rewarded insiders; power signatures | Prior work | [@dyck2007whistle]; [@wasil2024verification]; [@kimpson2026dcpower] | none |
| The evader-minimised miss with merged channels | Prior work, applied: path analysis in physical protection, safeguards and network interdiction; the merging rule may extend it | [@snell2007itc20]; [@washburn1995interdiction]; [@ward2016safeguards]; [@gif2011prppem]; [@baker2025verifying] | C3, as an application |
| The untraced pool as a covert reserve, with the footprint floor | Extends prior work, narrowly: the bound at the highest utilisation and the crossing years remain | [@koopmanschap2026gpu]; [@fithian2026hardwired]; [@iaea-glossary-2022] | C8 |
| Bans on closed loops | Prior work, and the rule here while no trigger works | [@miotti2025narrowpath]; [@redlines-2025] | none |
| Distillation keyed to the teacher | Not searched as such | [@ec-gpai-guidelines-faq-2025] keys to the modifier's compute | none until searched |
| Self-replication limits and release control | Prior work | [@redlines-2025]; [@bis2025diffusion] | none |
| Continual-learning updates counted, re-evaluation on drift | Prior work for counting; drift trigger not searched | [@fpf-sb53-2025]; [@eu-ai-act-2024] | none |
| The coupled-gain certificate as a treaty test | Prior work: the small-gain certificate, applied | [@dashkovskiy2007smallgain]; [@bardoscia2017pathways]; [@vanmieghem2011spectral] | C6, as an application |
| The coalition share from T_r, and self-policing up to m * s* | Prior work: the hardwired-pause threshold solved for the share; the reporting condition is cartel leniency's | [@fithian2026hardwired]; [@aubert2006leniency]; [@whitehouse2015jcpoaparameters]; [@williams2026breakout] | C7, as an application |
| Penalties on outsiders | Prior work | [@nordhaus2015climate]; [@rahman2025nonparty] | none |
| Withdrawal notice and asset freeze | Prior work | [@scher2025agreement]; [@eu2005nptwithdrawal] | none |
| The narrow-system exemption, and closure by input | Prior work for the exemption; the combination rule is the task-based automation model; gated closure measured one gate at a time may extend | [@miotti2025narrowpath]; [@aghion2017ai]; [@clymer2025bareminimum] | C11 |

Five pieces were not searched for prior art at all: the renewal evidence list with periods set per
holding, the log replicas, the mixed inspection beacon, distillation keyed to the teacher, and the drift
trigger for continual learning. Each needs its own level-1 search before it is claimed. The
smuggled-stock arithmetic uses others' inputs and is not a contribution.

## What must hold for the protocol to stand

The claims file names four footings ([the claims file](04-claims.md#what-would-make-this-program-fail)).
In the protocol's terms:

1. **The covert pool can be closed** (C8, with C3). Nothing in the protocol closes it today, and E5 has
   ruled out the alternative: no channel in the record beats the historical rate on an undeclared path,
   and E8 has facility channels failing for single sites around
   [2029](numbers.md#e8-cross-sat-1e26-now). Registration at birth, a window with an amnesty, makers'
   records and contraband status must close it; E22 tests whether they can. Until it closes, no party
   meets the line. If it cannot be closed, the protocol binds only parties that choose to declare.
2. **Lapse by default works** (C9, with C1). The redesigned rule sets by design only the time from a
   failed check or a withheld signature to a stop. Judgement on evidence that does not decide still
   takes time no record measures, a refused holder keeps one budget of compute per chip, and the price
   is hold-up. E25 checked the clock on Bitcoin's real headers; the rest is untested, needs an intact
   secure element, and needs drills. If it fails, the declared path has no usable T_resp either.
3. **C* and the efficiency path do not leave every relevant T_b spanning the line** (C2). E1 cannot
   identify the frontier's rate or the compute share; E15 and E18 decide the rest. If they do, useful
   AI is not kept.
4. **The states that host the chokepoints bind themselves.** No experiment tests this. It is the
   political footing everything else stands on.

The rest is survivable. E4 could not tell loops apart at calibrated noise, so the ban gates closed
loops until real rounds are measured (C4). If E3 finds no affordable budget that meets the targets on
RL-locked organisms, systems are placed by compute, at a higher cost to useful AI (C5). E1, E5, E6, E8,
E9, E11, E24 and E25 have run, and with the red team they cut parts of the design; the rest has not run.
The protocol is a design, tested against no real adversary.
