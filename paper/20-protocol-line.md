# The protocol: what it must do, and the line

Part II derives the protocol from the mechanisms and pathways of Part I. Every rule names the
mechanism or pathway it comes from, the channel that verifies it, what that channel cannot see, and
what it costs useful AI. The protocol is a design, deployed nowhere and tested against no real
adversary; illustrative numbers are marked as such.

## What the protocol must do

D4 sets the line at T_b(p) >= m * T_r(p), with T_r = T_d(beta) + T_resp, the times to detect a
breakout with probability 1 - beta and to halt it after a confirmed finding. Part III corrects it
twice. Where progress carries over between paths, the test tightens toward the fastest T_b against
the slowest T_r. And beta bounds one attempt, so halts must remove holdings and attempts must be
bounded.

The protocol must keep every path of every party outside the line; shorten T_d, above all where an
evader would go, and T_resp; agree in advance how T_b is computed; and leave everything outside the
line free to improve through metered, human-held gates (D6). Declaring all frontier AI weapons-grade
would meet the first requirements and fail the last.

Three requirements come from the mechanisms. Loops each subcritical can be supercritical together
[@davidson2026feedback; @burtsev2026criticality], so every edge between loops needs a gate (Y3).
Compute, the only input with physical chokepoints (O3), is the backbone the regime meters. And
superintelligence is irreversible, so near the line the protocol must prevent, not deter. The line
itself is prior work, applied
[@snell2007itc20; @hafemeister2008ctbt; @gan2026clock; @fithian2026hardwired]; C1 stands as an
application, with (c) cut.

## Breakout time, from tables agreed in advance

T_b(p) is the shortest time on path p from a party's holdings to C*, the effective compute agreed to
reach D1 (D3). The protocol tabulates it by holding class, under best-case assumptions for the
proliferator, as the IAEA tabulates conversion times [@iaea-glossary-2022]. The untraced pool is a
covert path for every party, tabulated as if each held all of it. C* is a convention, so every table
is conditional on the agreed value.

Efficiency is the weak input. E1 cannot identify its rate (D3), so no interval tabulated in advance
would hold: the tables are conventions, taking the fast end of each holding's rate. For a party that
hides its algorithms a tabulated T_b is an upper bound. C2 is downgraded to an accounting frame: (a)
is cut, (c) is cut on E18's backtest, and (b) is not shown.

A T_b computed at launch speed must clear a line raised by
[3.2](../research/numbers.md#formal-inrun-line-factor) at the central drift rate and
[10.6](../research/numbers.md#formal-inrun-line-factor-high) at the high end, both upper bounds
(Part III).

## Response time

T_r has two halves. Detection is computed: T_d(p, beta) = ln(1/beta) / lambda at a constant rate
lambda on path p. No AI regime has measured a response. In E24's arms-control record
[25%](../research/numbers.md#e24-halt-share-never) of in-treaty findings were never followed by a
halt, and [67%](../research/numbers.md#e24-halt-share-reversed) of halts were later reversed or
shown incomplete. A safe line needs a high quantile of T_resp (Part III); this record has none.

C1(c), T_resp per path from drilled latencies, is cut, since nothing measures the licensors'
decision time. So lapse is the default. A registered chip runs only on an expiring licence, renewed
on logged evidence by licensors outside the holder's bloc; a failed check, a withheld signature,
silence or deadlock lets it lapse, as in flexHEG's rule [@petrie2025flexheg2; @aarne2025flexheg3],
and the chip stops within one budget of powered time. The time from a failed check to a stop is set
by design; a licensor's judgement on evidence that does not decide is not, and the price is hold-up.
Chips that lapse on a violation are returned, not paused. Lapse by default is untested.

An illustration, not a measurement: the [9 months](../research/numbers.md#org-dprk-months) IAEA
accountancy took to find the DPRK's discrepancy [@iaea-gc37-1084] plus one licence period of
[3 months](../research/numbers.md#prot-licence-months) [@petrie2025flexheg2] give a T_r of
[1.0 years](../research/numbers.md#prot-tr-declared) for a violation checked mechanically; judgement
adds a decision time no record measures. At a margin of [2](../research/numbers.md#prot-margin) the
line sits at [2.0 years](../research/numbers.md#prot-line-declared). On undeclared paths E5 puts
detection at no less than [31 years](../research/numbers.md#e5-td-site-now-years), and cloud compute
and distillation have no measured channel. No margin bridges that, so the paths are treated
differently.

The margin does not cover phi, the fall in T_b before the next check. With E22's bound on supply and
drift at the central rate, phi is [2.1](../research/numbers.md#prot-phi-quarter) a quarter and
[6.8](../research/numbers.md#prot-phi-year) a year. On the illustration, a declared path checked at
each renewal must show [4.2 years](../research/numbers.md#prot-line-declared-phi-quarter)
([13.4 years](../research/numbers.md#prot-line-declared-inrun-phi-quarter) at launch speed), and one
checked yearly [13.7 years](../research/numbers.md#prot-line-declared-phi-year). A party that buys
more than its share of new chips has a larger phi.

## The margin

The margin m is a design choice, set by negotiation; [2](../research/numbers.md#prot-margin) only
makes the illustrations concrete. If the estimates of T_b(p) and T_r(p) err in the unsafe direction
by at most factors e_b and e_r, an admitted path is still stopped, per attempt, with probability at
least 1 - beta whenever e_b * e_r <= m (Part III). It covers estimation error only: not C*,
deliberate misreporting, phi, or the transfer of weapons-programme rates to AI.

## Prevention near the line, deterrence far from it

Prevention needs [7.8](../research/numbers.md#def-gan-prevent-multiple) times the monitoring that
deters, in Gan's illustrative calibration [@gan2026clock], and such monitoring exposes secrets
[@coe2020arms]. So prevention is paid for only near the line: where the interval on a path's T_b
overlaps m * T_r, or where the path could cross within one tabulation period on the fast efficiency
path. There the regime meters continuously, samples chips and evaluates every checkpoint; elsewhere
it deters, with random inspections, penalties and rewarded insiders. The model is prior work; the
split is a design choice.

## No loop-gain trigger yet

A trigger would act on the upper bound of D2's loop gain K. E4 found that it fails. At the only
noise level calibrated on data it raised false alarms on [88%](../research/numbers.md#e4-k-fa-n5) of
loops at the corrected median return and fired almost as often there as at the 95th percentile (D2).
C4 is downgraded to a measurement design.

What binds instead is the prior-work ban [@miotti2025narrowpath; @redlines-2025]: AI-run changes to
the training inputs of a frontier-scale system need logged human gates (L3) until E4(b) finds a
trigger on real staged rounds. It binds only loops a developer declares, and the loops it stops are
probably subcritical, as E9's gain at fixed compute suggests. Today it costs close to nil: the one
developer that reports on this finds no measured subset of its AI research work fully autonomous
[@anthropic2026pace].

Closures on separate inputs do not multiply, so the ban gates every highly closed input together.
Closure by input, C11, is downgraded to framing until E4(d) and changes no rule before then.

## Elicited capability, with the budget named in advance

Capability, in T_b and in D2's staged runs, is judged on elicited capability (D5). The elicitation
protocol is named before the evaluation and carries two measured rates, published as one-sided upper
bounds: a miss rate over model organisms with hidden capability, built blind to it, and a
false-alarm rate over benign models. C5 is a candidate, against non-adaptive hiding only: the rates
bound hiding by the sampled methods. Its experiment has not run, and its statistics are
diagnostic-test practice [@fda2007diagnostic].

Elicitation fails against hardened locks [@finke2026robustorganisms]. Beyond that range a system is
placed by compute plus E1's [2.8 OOM](../research/numbers.md#e1-gpqa-overlap-oom) overlap, a weak
fallback from one benchmark. The cost to useful AI is false alarms: in the UK AISI auditing game
elicitation lifted benign models about [10 points](../research/numbers.md#def-audit-benign-uplift)
too [@taylor2025auditinggames].
