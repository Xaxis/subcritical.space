# What stays allowed, and where the protocol fails

## What useful AI keeps

Use and serving at any scale are counted, not limited. Prices at fixed benchmark level fall
[5](../research/numbers.md#comp-price-fall-lo)x to [10](../research/numbers.md#comp-price-fall-hi)x a
year [@gundlach2025priceprogress], and nothing here slows that. Training below the line stays free, as
does AI-assisted research and software work [@handa2025aei]: only closed loops on frontier training are
gated. Agents are uncapped, and the 80% time horizon could go from
[3 hours](../research/numbers.md#dyn-horizon-p80-hours) to
[22 hours](../research/numbers.md#path-horizon-p80-next-year) in a year. Narrow superhuman systems,
science, data, talent and capital stay free unless they feed a covered system or the research-transfer
restriction applies, as do distillation and open weights below their thresholds; continual learning is
metered.

## What it costs

Registration covers about [13.6 million H100e](../research/numbers.md#org-sold-2025) a year, and host
states forgo sales. Evaluations come about every
[6 months](../research/numbers.md#prot-eval-interval-months) near the frontier, on a rate E1 cannot
confirm; elicitation lifts benign models about
[10 points](../research/numbers.md#def-audit-benign-uplift), against a false-alarm target of
[10%](../research/numbers.md#claim-d5-false-alarm-target). Prevention near the line needs
[7.8](../research/numbers.md#def-gan-prevent-multiple) times the monitoring deterrence needs, in Gan's
calibration [@gan2026clock]. The closed-loop gate costs almost nothing now but will stop loops that are
probably subcritical, since no trigger tells them apart (the rule on K raised
[88%](../research/numbers.md#e4-k-fa-n5) false alarms in E4). Release control and the research-transfer
restriction cost open science most, and evaluation with weight access costs confidentiality
[@coe2020arms].

## Where the promise is not kept

The frontier stops at the line. C* is fixed in effective compute while algorithms improve, so the
physical compute a holding may command falls every year; "keeps improving" holds only below a ceiling
that rises only if C* is revised on evidence. While the pool is open the promise fails by the
protocol's own rules, since every party is inside the line through it. Precaution compounds: the
fast-path tables, the margin, phi and the in-run factor each push declared holdings toward the line,
and if every relevant T_b interval spans it, frontier holdings become weapons-grade by default. Under
lapse by default every holder's compute, useful AI included, is a hostage to a blocking set of rival
licensors. Caps on small clusters cost small actors without holding models back: at MIRI's cap of
[16 H100e](../research/numbers.md#phys-miri-cluster-cap) [@scher2025agreement], a
[1e+24 FLOP](../research/numbers.md#org-miri-strict) model takes only
[1.0 years](../research/numbers.md#e8-cap-years-1e24-bound) at the bound.

## Where it fails

The untraced pool is [340](../research/numbers.md#e8-pool-over-floor-1e26-pause-p50) times the floor of
a [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run at E8's median
([110](../research/numbers.md#e8-pool-over-floor-1e26-pause-p05) to
[1,000](../research/numbers.md#e8-pool-over-floor-1e26-pause-p95)), and nothing closes it. Algorithms
are invisible and the frontier's rate is not identified (E1); a capped party closes an example headroom
in [2.2 years](../research/numbers.md#comp-leak-years-rosetta) to
[9.3 years](../research/numbers.md#comp-leak-years-small), averages that E18 finds hide jumps. Single
sites drop below the satellite line by about [2029](../research/numbers.md#e8-cross-sat-1e26-now).
Above expert level no demonstrations exist, so nothing is guaranteed where D1 begins
[@barnett2024evaluations], and placement by compute adds E1's
[2.8 OOM](../research/numbers.md#e1-gpqa-overlap-oom) overlap. Attempts can repeat: in E24,
[67%](../research/numbers.md#e24-halt-share-reversed) of halts were later reversed or shown incomplete.
Weight theft is a gap: Part I has no evidence on it, and the protocol cannot say to what standard
weights must be secured. A broken hardware trust anchor fails every on-chip channel together
[@chuang2026teefail]. A response may never come: in E24
[25%](../research/numbers.md#e24-halt-share-never) of in-treaty findings went unhalted
([46%](../research/numbers.md#e24-halt-share-never-all) counting findings after withdrawal), and lapse
by default is untested. Gates on research labour rest on self-reports [@anthropic2026pace].

Three limits hold for any protocol of this kind: a sovereign that holds a chokepoint can reopen it, a
large state with its own chip chain can build outside, and published algorithms are in everyone's
holdings. The protocol makes the first visible, the second costly and detectable, and the third slower
at frontier scale, and prevents none. Against a major power with its own chip chain it offers
deterrence only, so it prevents breakouts by the parties least able to make them.

## What must hold for it to stand

1. **The covert pool can be closed** (C8, with C3). Registration at birth, an amnesty, makers' records
   and contraband status must close it, and nothing yet tests whether they can: E22 bounds supply from
   above, not closure. If they cannot, the protocol binds only parties that choose to declare.
2. **Lapse by default works** (C9, with C1, whose computed T_resp is cut). Only the time from a failed
   check to a stop is set by design; judgement takes time no record measures, and the price is hold-up.
   E25 checked the clock on Bitcoin's real headers; the rest is untested and needs an intact secure
   element and drills. If it fails, the declared path has no usable T_resp either.
3. **C* and the efficiency path do not leave every relevant T_b spanning the line** (C2, an
   accounting frame). E1 cannot identify the frontier's rate or the compute share, and in E18 the leak
   came in jumps; E15 remains. If they do span it, useful AI is not kept.
4. **The states that host the chokepoints bind themselves.** No experiment tests this.

The protocol remains a design, deployed nowhere and tested against no real adversary.

## What is ours and what is prior work

Most of the protocol is prior work assembled. The labels are the independent prior-art search's, claims
about a search, not about the world. Expiring chip licences renewed by k of n licensors from rival
blocs, lapse by default and the powered-time counter are flexHEG's [@petrie2025flexheg1;
@petrie2025flexheg2; @aarne2025flexheg3]. Thresholds, chip tracking, inspections and withdrawal notice
with frozen assets are in MIRI's draft agreement [@scher2025agreement], and the idea of an IAEA-style
line is older [@openai2023governance; @sastry2024compute]. The log follows certificate transparency and
Catena [@laurie2013ct; @tomescu2017catena], the height clock a monotone checkpoint in trusted hardware
[@mouallem2026alerting], and inspections with no known last period the inspection-game literature
[@avenhaus2002inspection; @vonstengel2016recursive]. The line and the evader's best path are path
analysis from physical protection and network interdiction [@snell2007itc20;
@washburn1995interdiction]. Breakout from holdings comes from A Narrow Path and the hardwired-pause
group [@miotti2025narrowpath; @fithian2026hardwired], bans on closed loops from A Narrow Path and the
red-lines call [@redlines-2025], and penalties on outsiders from Nordhaus [@nordhaus2015climate].

Part III gives each claim's standing level by level: the breakout tables (C2) are now only an
accounting frame, and C5 and C8 are the only candidates left. Five pieces were never searched for prior
art: the renewal evidence with periods per holding, the log replicas, the mixed beacon, distillation
keyed to the teacher and the drift trigger for continual learning. The smuggled-stock arithmetic uses
others' inputs and is not a contribution.
