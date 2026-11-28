# Introduction

Public statements now call for a prohibition on developing superintelligence, or for red lines on
AI, and leave the thing to be prohibited undefined [@fli-superintelligence-statement;
@redlines-2025]. This paper asks what such a prohibition would
have to trigger on, and how compliance could be verified among parties that do not trust each other,
while AI that is useful stays allowed and keeps improving. It is the written account of an open
research program, Subcritical. Every number in it is computed by the program's public model from
sourced inputs, and every experiment reruns from public code with a fixed seed.

## Why time is the axis

A capability threshold says where the danger lies. It does not say whether a regime could stop a
party that approaches it. What decides that is a race between two clocks: how fast a party could
reach the endpoint from what it holds, its breakout time T_b, and how fast the regime could detect
the attempt and halt it, T_r = T_d + T_resp. We call a holding weapons-grade when T_b < m * T_r on
some path the party could take, with a stated margin m. Everything slower is useful AI, free to keep
improving through gates that humans hold. This puts the line on a quantity computed from holdings
and from the regime's own channels, rather than on a capability score, which saturates, can be
hidden, and crosses its threshold only at the endpoint.

The idea is old. It is timely detection in nuclear physical protection [@snell2007itc20] and Nitze's
1988 standard for effective verification [@hafemeister2008ctbt], and recent AI work states it in
words and as a formula [@barnett2025governance; @gan2026clock]. Its difficulty lies in what it
needs: an agreed amount of effective compute for the endpoint, a detection rate on each path an
evader could take, and a response time that no regime has measured. The record shows how far apart
the two clocks are today. Experiment E5 puts detection on undeclared paths at
[31 years](../research/numbers.md#e5-td-site-now-years) to
[32 years](../research/numbers.md#e5-td-pool-years), against
[39.0 days](../research/numbers.md#e5-td-declared-days) on the declared path. Halts that followed
findings in past treaties took a median of
[1.2 years](../research/numbers.md#e24-halt-km-median-years), against a violator's fastest exit of
[31 days](../research/numbers.md#e24-exit-min-days). These are measurements of what a protocol would
have to change, not findings about a protocol.

## The approach

The work defines superintelligence and its mechanisms first, and derives the protocol from them.
Part I gives six operational definitions, among them the endpoint, breakout time and the line. It
then explains the mechanisms that form superintelligence from five perspectives: physical and
energetic, computational and algorithmic, dynamical, cognitive and functional, and organisational
and economic. Each mechanism has a definition, a measurement, and the evidence for and against it.
Part I ends by ranking seven pathways by how much each moves the line and how hard it is to see.
Part II derives the protocol from those mechanisms: a limit for each, the channel that verifies it,
and its cost to useful AI. Part III states and proves what can be proved, reports the experiments,
and gives the verification record and the limitations. Throughout, an H100-equivalent (H100e)
counts compute in units of one H100's throughput, and OOM means an order of magnitude, a factor of
ten.

## What the work contributes, as it stands

Twelve claims were put to six levels of verification: an independent prior-art search by a helper
that did not propose the claim, a formal statement and proof, experiments on real data, a red team
that only tries to break it, Paperwright's integrity, reviewer and editor desks, and a fresh
reviewer. A claim that fails a level is cut or downgraded. Four levels have run, the third only in
part; levels 5 and 6 have not. No claim has passed all six, so none is yet a contribution, and none
is new.

The prior-art search found five claims to be prior work in substance, first done elsewhere: the line
(C1) and detection judged at the evader's best path (C3) in nuclear physical protection and network
interdiction [@snell2007itc20; @washburn1995interdiction]; the coupled-gain certificate (C6) in
control theory [@dashkovskiy2007smallgain]; the coalition share (C7) in the hardwired-pause threshold
and cartel leniency [@fithian2026hardwired; @aubert2006leniency]; and the height-clocked chip licence
(C9) in Bitcoin-anchored clocks and transparency logs [@bentov2019tesseract; @tomescu2017catena;
@laurie2013ct]. The pathway ranking (C12) applies acquisition path analysis [@allen-2015-llnl]. These
six stand as applications to AI, credited as such; what is ours in them is the use and any result
computed inside it: the margin as a multiplicative error budget, covering estimation errors e_b and
e_r whenever e_b * e_r <= m, a one-line lemma whose likeliest earlier home, the safety-factor
literature, was not opened (C1(b)); an elementary rule for merging detection channels that share a
source (C3); and the pathway order as a judgement with
[12](../research/numbers.md#claim-c12-pareto-two) of [21](../research/numbers.md#claim-c12-pairs)
pairs fixed by evidence (C12). C6 issues no certificate while edges are unmeasured, and C9 is
engineering.

Four claims are downgraded. Breakout time per path from verified holdings (C2) is an accounting
frame that claims nothing: tabulating it in advance is cut, since public data cannot identify the
drift of algorithmic efficiency, its gain over a single efficiency multiplier is not shown, and its
backtest cuts against it, because the leak of a training cap came in jumps. The loop-gain estimator
(C4) is a measurement design: at the only noise level calibrated to data every estimator tried
under-covers or is biased, and the trigger built on it fires about as often below 1 as above, on the
return or on the gain. Superintelligence judged against a named organisation at matched time and
money (C10) is a definition, which cannot warn; its claim that the crossover budget rises without
saturating is withdrawn, since it rises only while a battery's baselines last. Closure measured one
gate at a time (C11) is framing until its experiment runs.

Two claims remain candidates, each facing levels 5 and 6:

- Miss and false-alarm rates per named elicitation budget over a defined population of model
  organisms (C5). They bound only hiding that does not adapt, and the experiment has not run.
- The aggregate footprint floor as a bound, with each detection channel's margin and the year it
  crosses one (C8). Two of its three parts are supported, on one experiment alone; a falsifier that
  could not fail is cut.

The red team also cut the response time computed from drills (C1(c)), since every response waits on
a political decision.

Most of what the paper offers is therefore synthesis: an account of how superintelligence would form,
drawn from prior work; a line and a protocol assembled from known parts; and measurements that show
where the parts do not yet fit together. Part III gives each claim's record level by level.

## What has not been done

The protocol is a design. Nothing in it has been deployed, and nothing has been tested against a real
adversary: not a defecting state, a secret laboratory, a model that hides its capability, or an
evaluation built to be gamed. The experiments use public data, small models and simulation, and
several that the claims depend on have not run. Each definition is only as good as the test that
measures it, and several of those tests have not been made. The documents say so wherever it
matters.
