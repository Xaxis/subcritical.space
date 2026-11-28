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
party that approaches it. That depends on a race between two clocks: how fast a party could reach
the endpoint from what it holds, its breakout time T_b, and how fast the regime could detect the
attempt and halt it, T_r = T_d + T_resp. A holding is inside the line when T_b < m * T_r on some path
the party could take, with a stated margin m; D4 names such holdings weapons-grade, a position
against the line, not a property of the material or a verdict on capability. Everything outside the
line is useful AI, free to keep improving through gates that humans hold.

The line is computed from holdings and from the regime's own channels, but only conditional on C*,
the effective compute the parties agree is enough to reach the endpoint. The time axis does not
remove the capability threshold; it moves it into C*, which cannot be measured before someone
reaches the endpoint and whose error has no bound. One OOM of C* moves T_b by
[2.3 years](../research/numbers.md#comp-years-per-oom-ho), more than the illustrative line of
[2.0 years](../research/numbers.md#prot-line-declared). What the axis buys is a quantity the parties can
compute and audit from holdings once they agree C*, and a regime's response time that enters the
test instead of being assumed.

The idea is old: timely detection in nuclear physical protection [@snell2007itc20] and Nitze's 1988
standard for effective verification [@hafemeister2008ctbt], stated for AI in words and as a formula
[@barnett2025governance; @gan2026clock]. Its difficulty lies in what it needs. Experiment E5 puts
detection of a covert programme, to a [5%](../research/numbers.md#def-prevent-beta) miss chance at the historical
discovery rate, at a central
[32 years](../research/numbers.md#e5-td-hist-years), or [24 years](../research/numbers.md#e5-td-weibull-years) under a
Weibull fit, both transfers from weapons programmes rather than measurements, against
[39.0 days](../research/numbers.md#e5-td-declared-days), a design figure, on the declared path. In past
treaties [25%](../research/numbers.md#e24-halt-share-never) of findings made while the party was in its
treaty were not followed by a halt within what the sources cover, and the fastest halt took
[64 days](../research/numbers.md#e24-halt-min-days) against a violator's fastest exit of
[31 days](../research/numbers.md#e24-exit-min-days). On today's inputs the line can be evaluated only on the
declared path, and every party fails it through the untraced chip pool, cloud compute and
distillation.

## The approach

The work defines superintelligence and its mechanisms first, and derives the protocol from them.
Part I gives six operational definitions, among them the endpoint, breakout time and the line, then
explains the mechanisms that form superintelligence from five perspectives (physical and energetic,
computational and algorithmic, dynamical, cognitive and functional, organisational and economic),
and ranks seven pathways by how much each moves the line and how hard it is to see. Part II derives
the protocol: a limit for each mechanism, the channel that verifies it, what that channel cannot see,
and its cost to useful AI. Part III gives what can be proved, the experiments, the verification
record and the limitations. An H100-equivalent (H100e) counts compute in units of one H100's
throughput, and OOM means an order of magnitude.

## What the paper offers

Twelve claims were put to six levels of verification, from an independent prior-art search to a
referee who had not seen the work; five have run, the third in part. None passed all six, none is
new, and none remains a candidate: six are applications of prior work to AI and six are downgraded
to a design, a definition, framing or a judgement. Part III gives the record. What the paper offers
is therefore a synthesis and a set of negative results: an account of how superintelligence would
form, drawn from prior work; a line and a protocol assembled from credited parts; and measurements
that show where the parts do not yet fit together.

The protocol is a design. Nothing in it has been deployed or tested against a real adversary: not a
defecting state, a secret laboratory, a model that hides its capability, or an evaluation built to be
gamed. The experiments use public data, small models and simulation, and several that the claims
depend on have not run.
