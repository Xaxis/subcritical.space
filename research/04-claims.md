# Claims: what this work may contribute, each with its test

This file states what Subcritical may claim as its own, precisely enough that each claim could be
shown false, and plans the test each must pass. The repo's rule is that a claimed contribution
passes six levels or is cut:

1. **L1**, an independent prior-art search by a helper that did not propose the claim;
2. **L2**, a formal statement and proof, or the reason the claim is empirical and needs none;
3. **L3**, working experiments on real data or models, rerunnable from `tools/exp/`;
4. **L4**, a red team that only tries to break it;
5. **L5**, Paperwright's integrity, reviewer and editor desks, resolved by us;
6. **L6**, a fresh reviewer who has not seen the work.

Results go in [the verification record](07-verification.md#the-record), one row per claim per level.
A claim that fails a level is cut or downgraded, never argued around.

Four levels have run, L3 in part. L2 is done for all twelve claims in
[the formal file](05-formal.md#summary). L1, a search for each claim by helpers that did not propose
it, is in two reports, [C1 to C6](verification/l1-prior-art-c1-c6.md#summary) and
[C7 to C12](verification/l1-prior-art-c7-c12.md#summary). L4, a red team that only tried to break
each claim, is in [its report](verification/l4-red-team.md#verdicts). These experiments have
results: E1, E2, E4's simulation and history, E5, E6, E8, E9, E11, E18, E21, E22, E23, E24 and E25;
C5 and C11 still wait on theirs (E3, E4(d) and E4(e)). Each section below opens with what each level
found, one line per level, and states the claim as it now stands.

They cut deep. L1 found C1, C3, C6, C7 and C9 prior work in substance, first done in nuclear
physical protection, control theory, epidemic control, cartel law and transparency-log engineering;
each is now an application to AI, credited. It found the other seven narrower than stated. L4 cut
C1(c) and C8(b), failed C4 as a trigger, limited C5 to non-adaptive hiding, and left C10 a
definition, C11 framing and C12 a judgement. L3 cut C2(a), since E1 cannot identify the drift rate
it needs, then cut C2(c) (E18 against) and left (b) unshown, which downgrades C2 to an accounting
frame; it found C6's certificate cannot issue today, failed C4's estimator and its trigger at the
only data-calibrated noise, which downgrades C4 to a measurement design, and found C10's t* stopped
by the ceilings of today's batteries. No claim is new.

[The novelty file](03-novelty.md#what-this-leaves-as-our-contribution) had already found none of the
memo's ideas new; this file gathered the narrow extensions it left and kept twelve. Three labels are
now used. **Application of prior work**: the method is prior work, credited by name; only its use on
AI, and any result computed inside that use, is ours. **Combination of prior work**: each part is known; the
combination was not found. **Extends prior work**: the core is prior work; a stated, narrow
difference was not found. "Not found" is a claim about our search and L1's, not about the world, and
L5 or L6 may still lower any label. The few numbers Part I did not compute are derived in
`model/parts/040_claims.py` from targets in `data/inputs/040-claims.toml`.

## Summary

| Id | The claim in one line | Label | Closest prior work | Experiments | Status |
|---|---|---|---|---|---|
| C1 | A holding is weapons-grade if T_b < m * (T_d + T_resp) on some path, or over the paths between which progress can move; the margin covers estimation error per attempt whenever e_b * e_r <= m | application of prior work | [@snell2007itc20]; [@hafemeister2008ctbt]; [@gan2026clock]; [@fithian2026hardwired] | E5, E24, E6, E22, E18 | L1 prior work; L2 corrected; L3 against; L4 (c) cut |
| C2 | Breakout time per path from verified holdings, an accounting frame: tabulating it in advance (a) is cut, the backtest (c) is cut (E18 against) and its gain over one multiplier (b) is not shown | combination of prior work | [@fithian2026hardwired]; [@gan2026clock]; [@pistillo2025loopholes]; [@villalobos2023tradeoff] | E1, E18, E10, E15, E22, E4 | Downgraded to an accounting frame: L1 extends, relabelled a combination; L2 proved under assumptions; L3 against, (a) cut, (c) cut (E18 against), (b) not shown; L4 corrected |
| C3 | The chance a breakout is missed is a maximum over the evader's paths, dependent channels merged at the larger rate, over each path's own breakout time | application of prior work | [@snell2007itc20]; [@washburn1995interdiction]; [@gif2011prppem]; [@baker2025verifying] | E5, E8, E13 | L1 prior work; L2 corrected; L3 supports, (c) measured; L4 corrected |
| C4 | A design for measuring the loop gain K at fixed inputs, from an exact round identity and a budget ladder; its estimator and the trigger on it fail at calibrated noise | extends prior work | [@srikanth2026aide2]; [@blumberg2020supercritical]; [@cunningham2026rsi] | E4, E9 | Downgraded to a measurement design: L1 extends narrowly; L2 corrected; L3 against, estimator and trigger; L4 fails as a trigger |
| C5 | Elicited capability judged by miss and false-alarm rates per named budget over a sampled population of organisms; it bounds non-adaptive hiding only | extends prior work | [@fda2007diagnostic]; [@greenblatt2024password]; [@taylor2025auditinggames] | E3 | L1 extends; L2 proved; L3 untested; L4 non-adaptive hiding only |
| C6 | The small-gain certificate rho(K) <= rho(U) <= max row sum of U as a treaty test, issued only when every edge has a measured bound | application of prior work | [@dashkovskiy2007smallgain]; [@roberts2003typer]; [@vanmieghem2011spectral]; [@bardoscia2017pathways] | E11, E9, E6 | L1 prior work; L2 proved; L3 against issuing today; L4 corrected |
| C7 | C1 applied to the hardwired-pause threshold for coalitions, s* = min(1, h_w / (m * T_r)), with the leniency condition for reporting | application of prior work | [@fithian2026hardwired]; [@whitehouse2015jcpoaparameters]; [@aubert2006leniency] | E6, E22 | L1 prior work; L2 corrected; L3 against, (a) corrected for in-run drift and for growth between declarations; L4 (b), (c) downgraded |
| C8 | The aggregate footprint floor as a bound at the lowest precision and full utilisation, each channel's margin and crossing year, and the untraced pool's multiple of the floor | extends prior work | [@fithian2026hardwired]; [@koopmanschap2026gpu]; [@iaea-glossary-2022] | E8, E14, E13, E22 | L1 extends narrowly; L2 corrected; L3 supports (a), (c), on E8 alone; L4 (b) cut |
| C9 | Chip licences fresh by a block hash, ending at a height on the most-work chain for chips fed honest headers, valid only once logged: engineering | application of prior work | [@bentov2019tesseract]; [@mouallem2026alerting]; [@tomescu2017catena]; [@laurie2013ct] | E25 | L1 prior work; L2 P2 corrected; L3 mixed, supports P2, against the rate floor; L4 corrected |
| C10 | Superintelligence against a named institution at matched time and money on a regime-held battery, with a censored crossover budget t*: a definition only | extends prior work | [@robinson2026horizons]; [@wijk2024rebench]; [@genewein2026agiasi] | E21, E2, E1 | L1 extends; L2 empirical, t* well defined; L3 against (b) on the one analogue, (c) downgraded: t* rises but stops at each battery's ceiling; L4 a definition only |
| C11 | Closure judged input by input against verifiable gates, the gain with any set of gates predicted from closures measured one gate at a time | extends prior work | [@aghion2017ai]; [@miotti2025narrowpath]; [@burtsev2026criticality] | E4, E16, E17, E19 | L1 extends narrowly; L2 corrected; L3 untested; L4 framing until E4(d) |
| C12 | Seven pathways ranked by effect on the line and visibility; only the Pareto-ordered pairs, [12](numbers.md#claim-c12-pareto-two) of [21](numbers.md#claim-c12-pairs) and none among the first three places, fixed by evidence | application of prior work | [@clarke2022mtair]; [@barrett2016asipath]; [@fithian2026hardwired] | E4, E5, E1, E2, E11, E9, E18, E15, E10, E19, E7 | L1 extends, as an application of path analysis; L2 empirical; L3 mixed; L4 a judgement |

What may still be ours is small, and each piece still faces L5 and L6: the margin as a
multiplicative error budget (C1(b), a lemma); the merging rule for dependent channels (C3,
elementary); rates per budget over a defined organism population (C5, non-adaptive hiding only); the
floor as a bound with each channel's margin and crossing year (C8); time and money matched against
an organisation with a censored t* (C10, a definition); closure measured one gate at a time (C11,
untested); and the pathway order as a judgement with [12](numbers.md#claim-c12-pareto-two)
evidence-fixed pairs (C12). C6, C7 and C9 add applications only. C4 is no longer a candidate: its
round identity is proved, but every estimator E4 tried fails L3 at the only data-calibrated noise,
so the identity and budget ladder stand as a measurement design until E4(b) measures real staged
rounds. Nor is C2: its backtest (c) is cut (E18 against) and its gain over one multiplier is not
shown, so the per-path expression stands as an accounting frame, credited to prior work.

C1 is the line, C2 and C3 its two sides, and C8 says which channel sees covert compute; C4, C5 and
C11 feed C2; C6 and C7 extend the line to coupled loops and coalitions; C9 is the regime's record; C10
is the endpoint; C12 decides what is restricted.

## C1. The line: T_b < m * (T_d + T_resp), with T_r computed, not chosen

**The claim.** A holding H (chips, weights, data, research labour, and every path p its holder can
use) is weapons-grade if and only if, on some path, T_b(p) < m * T_r(p), with T_r(p) = T_d(p) +
T_resp(p), all in years. T_b(p) is C2's breakout time on that path. T_d(p) is the time by which the
regime's channels on p detect a breakout there with probability at least 1 - beta, from C3.
T_resp(p) is the time from a confirmed finding to an effective halt; where it is random, its (1 -
beta_2) quantile, and the miss chance is then at most beta + beta_2. m >= 1 is a stated margin. Five
limits, from L4, E6 and E22. Where progress can move between paths, as a checkpoint can, a strategy
that switches on a partial signal has a random breakout time, and the per-path test does not cover
it: over such paths the test is the shortest T_b against the longest T_r, which is safe, or the
formal file's line for progress that carries over (Proposition 1.8), which is exact when responses
are equal. Beta bounds one attempt; n independent attempts succeed with chance up to 1 - (1 -
beta)^n, so the regime must bound attempts or state its guarantee per attempt; re-admitting a caught
party gives it another (E6). While the untraced pool is open, its path fails the line for every
party (C8), so the line separates no one until the pool closes. And T_b must count the drift a run
absorbs while it runs (Corollary 1.6a, after E6): a line computed at launch speed, with algorithms
fixed when the run starts, must rise by a factor of [3.2](numbers.md#formal-inrun-line-factor) at
the central drift rate and [10.6](numbers.md#formal-inrun-line-factor-high) at the high end, at the
protocol's margin and declared T_r; both are upper bounds, since they assume a run adopts every gain
the moment it appears. Holdings grow between declarations too: Proposition 1.6 keeps the line only
if it holds at phi * m * T_r at each check, phi the most T_b can fall before the next. E22 bounds
the supply part of phi for the fleet at [1.65](numbers.md#e22-phi-member-quarter) a quarter and
[2.5](numbers.md#e22-phi-member-year) a year; with the central algorithmic drift between checks,
Part II puts phi at [2.1](numbers.md#prot-phi-quarter) for a check at each licence renewal and
[6.8](numbers.md#prot-phi-year) for a check once a year, more for a party that takes more than its
share of new chips. Either way phi exceeds Part II's illustrative margin of
[2](numbers.md#prot-margin), so m covers estimation error only with phi on top: against a line of
[2.0 years](numbers.md#prot-line-declared), a declared path checked at each renewal must show
[4.2 years](numbers.md#prot-line-declared-phi-quarter)
([13.4 years](numbers.md#prot-line-declared-inrun-phi-quarter) at launch speed), and one checked
yearly [13.7 years](numbers.md#prot-line-declared-phi-year). Claimed: (a) the inequality, per path
where progress cannot move, as the definition of the line for systems and holdings in a regime whose
pool is closed; (b) the margin as an error budget: if the estimates of T_b and T_r err in the unsafe
direction by at most factors e_b and e_r, an admitted holding is still stopped, per attempt, with
probability at least 1 - beta whenever e_b * e_r <= m, for any continuous detection hazard. m covers
estimation error only. It does not cover C*'s, which has no bound, so T_b is reported conditional on
the agreed C*. Nor does it cover error a party introduces by understating its efficiency or delaying
a response. (c) Cut: T_r computed per path from drilled latencies (L4, below). Not claimed: the
inequality itself, which is timely detection in physical protection; that the line at m = 1 is Gan's
prevention condition; or that a prevention line belongs near the threshold and deterrence far from
it, which is Gan's [@gan2026clock].

**Results so far.**

- **L1** ([C1](verification/l1-prior-art-c1-c6.md#c1)): prior work, downgraded to an application.
  Only (b), as stated, was not found. It is one line of algebra; the safety-factor literature of
  structural engineering, which L1 did not open, is its likeliest earlier home.
- **L2** ([C1](05-formal.md#c1-the-line-per-path)): proves (b) for any continuous hazard, with a
  quantile form for a random response time, and the per-path form for fixed paths. The old scalar
  test failed in 524 of 6,000 random instances in which every path met the line. The switching case
  is now stated: Proposition 1.7 makes the per-path test exact where progress restarts and every
  response is shorter than every breakout, Proposition 1.8 gives the line where progress carries
  over, and Proposition 1.9 the guarantee per attempt. Corollary 1.6a, after E6, adds in-run drift:
  a line computed at launch speed must rise by [3.2](numbers.md#formal-inrun-line-factor) at the
  central drift rate and [10.6](numbers.md#formal-inrun-line-factor-high) at the high end, both
  upper bounds, and Proposition 7.1 and Theorem 7.2 carry it into C7. `c1_margin.py` passes on every
  correction, Corollary 1.6a included.
- **L3**: against (c). E5 puts T_d on undeclared paths at
  [31 years](numbers.md#e5-td-site-now-years) to [32 years](numbers.md#e5-td-pool-years), against
  [39.0 days](numbers.md#e5-td-declared-days) on the declared path; cloud and distillation have no
  measured channel. In E24, of [8 findings](numbers.md#e24-halt-findings) made while the party was
  in its treaty, [25%](numbers.md#e24-halt-share-never) were never followed by a halt
  ([46%](numbers.md#e24-halt-share-never-all) of all
  [13 findings](numbers.md#e24-halt-findings-all), counting those after a withdrawal). Halts took a
  Kaplan-Meier median of [1.2 years](numbers.md#e24-halt-km-median-years), against the violator's
  fastest exit of [31 days](numbers.md#e24-exit-min-days), and
  [67%](numbers.md#e24-halt-share-reversed) were later reversed or shown incomplete. With more than
  5% never halted, the response time has no finite 95th percentile. In E6, repeated attempts
  compound when caught members are re-admitted, which also weakens the reporting condition by a
  factor up to 1/beta (C7). E22 bounds the supply part of Proposition 1.6's phi for the fleet at
  [2.5](numbers.md#e22-phi-member-year) a year; with the central drift between checks, Part II's phi
  is [6.8](numbers.md#prot-phi-year) a year and [2.1](numbers.md#prot-phi-quarter) at each licence
  renewal, a factor the line needs on top of the margin.
- **L4** ([C1](verification/l4-red-team.md#c1)): (c) is cut. Under Part II's own deadlock rule a
  refusal needs a finding by a quorum of rival states, a political decision, so no response waits on
  none (C1.5, fatal). A strategy that switched paths succeeded with probability 0.105, against beta of
  [5%](numbers.md#def-prevent-beta), while each path met the line (C1.1). One OOM of C* moves T_b by
  [2.3 years](numbers.md#comp-years-per-oom-ho), more than Part II's illustrative line of
  [2.0 years](numbers.md#prot-line-declared) (C1.3). The open pool (C1.2), repeated attempts (C1.4)
  and misreporting (C1.7) are the other serious attacks. All are now in the statement. Survives with
  corrections, as an application.

**What it rests on.** [D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr). The memo's placeholder
channel needs [2.5 yr](numbers.md#def-placeholder-detect-time) to bring the miss chance to
[5%](numbers.md#def-prevent-beta); at E5's fitted discovery rate of covert programmes,
[0.094/yr](numbers.md#e5-hazard), an upper bound on a careful evader's, a path only the historical
channels see takes [32 years](numbers.md#e5-td-hist-years), before any response
([O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)).
Prevention costs [7.8](numbers.md#def-gan-prevent-multiple) times the monitoring deterrence needs in
Gan's calibration. The nuclear margin never exceeds [1.00](numbers.md#def-iaea-m-irr-high) and times
detection only [@iaea-glossary-2001; @cochran-2005].

**Prior work, and what remains.** The timely-detection condition, evaluated per adversary path,
judged at the weakest path, with a response time built from measured parts at a high quantile and a
time margin, is Sandia's physical-protection practice, evaluated with EASI from 1977
[@snell2007itc20]. The same inequality is Nitze's 1988 standard for effective verification
[@hafemeister2008ctbt], time-based security in cyber defence [@farhang2017tbs] and the process-safety
rule for response times [@dearden2022sif]. In AI, [@barnett2025governance] states it in words,
[@gan2026clock] as a formula, [@miotti2025narrowpath] sizes thresholds for "ample time to
intervene", and [@fithian2026hardwired] applies it per route with an uncertainty allowance. Per-path
analysis is also safeguards practice [@allen-2015-llnl]. What remains ours: the application to AI
holdings, and (b) as a small lemma.

**What would refute it.** (b) is found in the safety-factor literature: C1 is then an application
only. L3 cannot compute T_r for any path with an interval narrower than the T_b intervals it faces,
so the line decides nothing. E6 finds compliance collapses once T_b is drawn from its interval, as a
disputed threshold did in [@barrett2012climate].

**L3.** Done: E5 (T_d per path), E24 (T_resp), E6 (repeated attempts compound when caught members
are re-admitted, and a line computed at launch speed misses in-run drift), E22 (phi's supply part, which Part II combines with drift between checks). To
come: C2's remaining experiments (T_b's inputs). The gap is a drilled measure of the licensors'
decision time, which no experiment yet plans; without it (c) stays cut.

**L5, L6.** Pending.

## C2. Breakout time from verified holdings, and the cap leak as its fixed-compute case

**The claim.** For holdings H and an agreed C* (log10 effective compute), T_b(p) on each path p is
the earliest t with log10 C_p(t) + J + S_v + A(t) >= log10 C*. C_p(t) is physical compute
accumulated on p (chip-time at a reference precision times utilisation, including C8's untraced
pool); J the one-off post-training jump; S_v the inference span, larger where a cheap verifier
exists, paid in compute a chip count sees; A(t) algorithmic drift at a rate a(C) that may depend on
scale and rises with research labour, human and AI, through C4's gain. Distillation enters at the
teacher's level plus an uplift term, since a student can exceed its teacher. Each path's T_b(p) is
compared with that path's own T_r(p) (C1). At fixed physical compute this is the cap's leak time,
t = max(0, (h - J - S_v) / log10 gamma), with h the headroom to C* and gamma the yearly efficiency
gain. The interval covers every input but C*, whose error has no bound, so T_b is reported
conditional on the agreed value. Declared efficiency is self-reported, so the declared path is
tabulated at the fast end plus an allowance for undeclared gains. That allowance is unsized: no
source measures efficiency a party holds and has not declared, and E1 cannot bound even published
drift. So the declared path's T_b is reported conditional on the allowance, as it is on C*, and the
line there rests on the compute a chip count sees, not on the drift term. (a), cut on L3: the
expression per path from verified holdings, tabulated in advance by holding class with that
interval. E1 finds the drift rate not identified on public data, so no interval tabulated in advance
would hold; the expression stays as the accounting frame, which is prior work (credited below), not
as a contribution. Claimed: (b) for at least one holding class the protocol cares about, it differs
from a single-multiplier T_b by more than either's interval; (c) backtested at past dates, it
predicts the open-closed lag of [4 months](numbers.md#comp-open-closed-lag) within its interval.

**Standing: downgraded to an accounting frame.** C2 was a candidate only through (b) and (c), and L3
leaves neither. (c) is cut (E18 against): in E18's backtest the leak comes in jumps, which Corollary
2.3's constant rate cannot follow, and the expression has no term for a follower's delay. (b) is not
shown: the expression separates from a single multiplier only at headrooms where the cap already
fails the line, arithmetic on Part I's ranges that no data narrows. The expression stays as the
protocol's accounting frame, credited to prior work, and claims nothing. It would reopen if E10 and
E15 narrowed the rate enough for the two intervals to separate where a cap passes the line, and a
version with a follower's delay backtested.

**Results so far.**

- **L1** ([C2](verification/l1-prior-art-c1-c6.md#c2)): extends prior work, less than this file
  said, and relabelled a combination. Every term is prior (credited below). The verifier-conditioned
  span is an accounting rule others wrote, and so is charging a distilled model at its teacher's
  compute, or lowering the threshold by the compute distillation saves [@pistillo2025loopholes];
  both leave "what remains". The ceiling this file once drew from that rule is withdrawn, since a
  student can exceed its teacher (C2.5). Only (b) and (c) could add anything, and L3 leaves neither
  (below).
- **L2** ([C2](05-formal.md#c2-breakout-time-is-monotone-in-its-inputs)): T_b is monotone under the
  stated assumption, and two evaluations give its exact interval. Where drift falls fast enough with
  scale the assumption fails (202 of 1,500 random boxes fell outside the interval) and a termwise
  bound takes over.
- **L3** (E1): the rate is not identified. On all [105 models](numbers.md#e1-models), training
  compute explains [36%](numbers.md#e1-compute-share) of growth on Epoch's index, and the rest moves
  with date at about [17](numbers.md#e1-algo-annual) times a year in compute-equivalent. Across six
  samples of the same models the share runs from [18%](numbers.md#e1-compute-share-subset-min) to
  [63%](numbers.md#e1-compute-share-subset-max) and the rate from
  [2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max) a year,
  far beyond any one sample's interval. On the full sample drift falls with scale,
  [-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom) (from
  [-0.64 OOM a year per OOM](numbers.md#e1-drift-per-oom-lo) to
  [-0.16 OOM a year per OOM](numbers.md#e1-drift-per-oom-hi)), the case in which two evaluations do not
  give the interval; the sign is not robust across samples. In Ho et al.'s data the highest compute
  tercile progressed faster than the lowest in [52%](numbers.md#e1-ho-top-faster-share) of
  resamples. The one-OOM forecast bound is wide and overshoots at the top. This fails (a): an
  interval tabulated in advance cannot be delivered on public data, so (a) is cut, and C2 stood as a
  candidate only through (b) and (c).
- **L3** (E18): against (c), which is cut, and (b) not shown. In the backtest a model at or below a
  then-frontier record's compute matched the record after [0.48 years](numbers.md#e18-bt-h0-lo) to
  [1.52 years](numbers.md#e18-bt-h0-hi), where the expression predicts no delay for any input, and
  the [4 catch-ups](numbers.md#e18-bt-events) below a record's compute imply yearly rates from
  [1.91](numbers.md#e18-bt-gamma-lo) to [1,125](numbers.md#e18-bt-gamma-hi), the last closing most
  of the headroom within days: jumps that no constant rate (Corollary 2.3) follows. Only
  [3 points](numbers.md#e18-bt-inside-part1) of the backtest fall inside the expression's exact
  interval at Part I's bracket, and [2 points](numbers.md#e18-bt-inside-part1-j) with the
  post-training jump added. The open-closed lag, (c)'s stated target, cannot be predicted at all: on
  [0 days](numbers.md#e18-oc-evaluable-days) of Epoch's window do both the best open model and the
  record it matched have a public compute estimate. (b): in all
  [8 cases](numbers.md#e18-b-sep-fails-line) of holding class and rate range, every headroom where
  the expression's interval and a single multiplier's separate is one where the cap's leak time is
  already below m * T_r at every input, and [0 cases](numbers.md#e18-b-disjoint-example) separate at
  the example headroom, so the difference never changes a decision. It is arithmetic on Part I's
  ranges, not a measurement.
- **L4** ([C2](verification/l4-red-team.md#c2)): survives with corrections, each now in the
  statement: the interval is conditional on C* (C2.1); E1's own fit breaks the monotone interval and
  moves its rate over three orders of magnitude (C2.2, C2.3); "the bound is conservative" rested on
  one model (C2.4); distillation can exceed its teacher [@furlanello2018born; @burns2023weak] (C2.5);
  compute misplaced systems by up to [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) on one benchmark
  (C2.6); hidden algorithms shorten T_b (C2.7), and the allowance for them is unsized.

**What it rests on.** [D3](01-anatomy.md#d3-breakout-time) and
[the combined leak](012-computational.md#the-combined-leak-of-a-training-cap). With an example
headroom of [3 OOM](numbers.md#comp-example-headroom-oom), a capped party closes it in
[4.0 years](numbers.md#comp-leak-years-ho) at Ho et al.'s rate, [2.2 years](numbers.md#comp-leak-years-rosetta)
at the Rosetta rate and no sooner than [9.3 years](numbers.md#comp-leak-years-small) at the
small-compute bound; a cheap verifier leaves [0 OOM](numbers.md#comp-leak-left-verifier). Of a
[22,000](numbers.md#def-gundlach-claimed)-fold efficiency gain, less than
[100](numbers.md#def-gundlach-low-compute-max)-fold reproduces at low compute [@gundlach2025origin].
The model reproduces the hardwired-pause threshold of [180 million H100e](numbers.md#def-hwp-fleet-check).

**Prior work, and what remains.** Fleet accounting from holdings with research overhead,
utilisation, an inference multiple and an uncertainty allowance is [@fithian2026hardwired]; a
breakout-type time with a feedback term that falls as compute grows is [@gan2026clock]; additive
accounting of fine-tuning, extra inference and distillation against a training threshold is
[@pistillo2025loopholes]; the span set by cheap verification is [@villalobos2023tradeoff]; scale
dependence is [@gundlach2025origin]; the leak as the inverse of the access effect is
[@pilz2023efficiency]; the leak's other routes are known [@ord2025govaireport; @heim2024thresholds;
@davidson2023enhancements; @barnett2026closingwindow]. What would have remained ours, had (b) or (c)
passed: one expression evaluated per path from verified holdings, a loop-gain term measured rather
than assumed once C4's estimator passes L3 (it fails today, so the term is assumed until then), and
the split between leaks a chip count sees and leaks it does not. It is a combination, and with (a)
cut, (b) and (c) were the whole test of whether it adds anything; neither passed, so C2 claims
nothing.

**What would refute it.** (b) fails: no gain over one multiplier, and C2 is prior work. (c) fails:
the model should not set a treaty schedule, by the computational chapter's own test. (c) has failed
in E18, and (b) shows a gain only where it decides nothing. E15 finds no scale trend at fixed
algorithms: the scale term is cut.

**L3.** Done: E1, E18. To come: E15 and E10 (with the distillation uplift), which could reopen (b);
E22 bounds how fast C_p(t) can grow (C7); E4.

**L5, L6.** Pending.

## C3. Detection as the evader sees it: the per-path, evader-minimised miss

**The claim.** Let P be the paths open to a party (declared fleet, undeclared site with smuggled
chips, the untraced pool, cloud split across providers, distillation from others' outputs) and C(p)
the channels watching path p. The chance a breakout succeeds is P_miss = max over p of Pr[no channel
in C(p) detects before T_b(p) - T_resp]; with channels at rates lambda_c(p), independent given the
path, that is the maximum of exp(-sum of lambda_c(p) * (T_b(p) - T_resp)). Channels resting on one
trust anchor, or fed by one source of tips, merge into one at the larger rate, the rate under the
strategy the evader plays; if breaking the anchor is open to the evader, the break is itself a path,
on which that group's rate is zero. A path with no measured channel gets no T_d, not a rate
transferred from another domain. P omits stolen weights, open weights and C1's switching strategy.
Claimed: (a) the model applied to AI compute paths with sourced rates, and the merging rule: merging
at the larger rate is safe under any dependence, the sum only under independence; (b) a proposition:
the memo's product of channel misses equals P_miss only if every channel with a miss chance below one
watches every path, and otherwise understates it, and a scalar common cause, such as one
intelligence source, makes it understate further; (c) on today's sourced rates, the untraced pool's
T_d exceeds the declared path's by a large factor, so the regime's detection time is set by the pool
(C8).

**Results so far.**

- **L1** ([C3](verification/l1-prior-art-c1-c6.md#c3)): prior work, downgraded to an application
  of physical-protection path analysis (credited below). The merging rule is the only candidate
  extension: an elementary bound on the probability of a union, kept only if L4 and L6 agree it is
  more than the textbook bound. (c) is E5's empirical result, its direction anticipated in
  [@koopmanschap2026gpu].
- **L2** ([C3](05-formal.md#c3-detection-as-the-evader-sees-it)): proves (a) and (b) under
  independence given the evader's strategy, with the merging rule as stated. The common-cause part,
  Theorem 3.2, now holds for a scalar cause or independent components, with L4's counterexample
  (C3.4) recorded; for an evader randomising over several dimensions the maximum in (a) covers it
  instead. `c3_evader.py` passes on the correction, as does every check in `run_all.py`.
- **L3** (E5): illustrates (b) and measures (c). Over the memo's one-year breakout time the evader's
  best watched path, the pool, is missed with probability [91%](numbers.md#e5-pmiss-max-1y), and
  cloud and distillation, unwatched, are missed with certainty. The memo-style product is 10 to the
  power [-14](numbers.md#e5-memo-log10-miss-1y), an illustration of its form, not evidence. The
  pool's T_d is [299](numbers.md#e5-td-ratio) times the declared path's
  [39.0 days](numbers.md#e5-td-declared-days), which chip sampling now sets, with metering's one-day
  catch counted once. The fitted discovery rate, [0.094/yr](numbers.md#e5-hazard) (90% interval
  [0.057/yr](numbers.md#e5-hazard-lo) to [0.147/yr](numbers.md#e5-hazard-hi)), comes from programmes
  all found in the end, so it is an upper bound on a careful evader's. It runs from a programme's
  start, not a breakout's, and under the Weibull fit a first-year discovery has chance
  [2.6%](numbers.md#e5-weibull-detect-1y), not [9.0%](numbers.md#e5-hazard-detect-1y).
- **L4** ([C3](verification/l4-red-team.md#c3)): survives with corrections, each now in the
  statement or the results: the declared path's old T_d compounded a one-day figure its source does
  not extend (C3.1); the Monte Carlo could not fail (b) (C3.2); a nuclear-programme rate was given to
  cloud and distillation, on a different clock (C3.3); the common-cause theorem fails for a cause of
  more than one dimension (C3.4); the fit is an upper bound (C3.5); three paths lie outside P (C3.7).

**What it rests on.** [The novelty file's multi-channel section](03-novelty.md#the-multi-channel-detection-guarantee-over-breakout-time)
and the channel limits in [P4](011-physical.md#p4-the-footprint-and-its-floor). The memo's placeholder
rate is [1.2/yr](numbers.md#org-memo-detect-rate). Epoch's smuggling model assumes [25%](numbers.md#org-diversion-detect)
of diversions are detected. Metering catches [96%](numbers.md#phys-meter-detect) of undisguised
training at [1%](numbers.md#phys-meter-false-alarm) false alarms, on simulated power
[@kimpson2026dcpower]. No challenge inspection has been requested
([0 requests](numbers.md#org-cwc-ci-requests)) [@opcw-ec109-dg22]. A mature many-channel system
caught about [31%](numbers.md#org-fraud-detect) of frauds [@dyck2017pervasive].

**Prior work, and what remains.** The structure was first done in physical-protection path analysis,
EASI from 1977 [@snell2007itc20]: the evader takes the path of least detection, detection counts only
if early enough for the response, channel values depend on the adversary's tactics, and broken
elements are modelled per path. The game form is network interdiction [@washburn1995interdiction] and
safeguards selection [@ward2016safeguards]; per-pathway detection with timing is in
[@gif2011prppem]; acquisition path analysis computes detection per path in safeguards
[@allen-2015-llnl; @iaea-glossary-2022]; [@burr2012safeguards] flags dependence between measures
without a rule. In AI, [@baker2025verifying] judges a regime at its weakest subgoal and flags
correlation; [@gan2026clock] uses one aggregate rate, [@allison2025nuclear] a Poisson risk over a
horizon, [@shavit2023chinchilla] one channel in closed form, [@wasil2024verification] a "Swiss
cheese" model in words. What remains ours: the application to AI paths with sourced rates, and the
merging rule if L6 finds it more than the textbook bound.

**What would refute it.** L6 judges the merging rule textbook: C3 is an application only. T_d's
interval spans every T_b of interest, which makes the model a framework, not a result. A path
outside P with low detection, beyond the three already named.

**L3.** Done: E5 (Monte Carlo and the discovery-rate survival fit), E8 (facility margins). To come:
E13 (a measured multi-day rate for the metering channel against disguises). No experiment yet gives
cloud or distillation a channel.

**L5, L6.** Pending.

## C4. A loop-gain estimator at fixed inputs, binding at its confidence bound

**The claim.** Capability is measured on a log compute-equivalent axis; a round is one research
cycle at a fixed budget (experiment compute, data, wall-clock). In
[the common form](013-dynamical.md#the-common-form-a-growth-law-and-its-returns), with returns
exponent b (Part I's beta), return to input lambda and closure e, the loop's gain is K = e * lambda
/ b, and round k's gain Delta_k satisfies, exactly, ln[(exp(b Delta_(k+1)) - 1) / (exp(b Delta_k) -
1)] = b (K - 1) Delta_k. A staged run with a fixed, elicited agent (e = 0) estimates b from that
identity; repeating at one, two and four times the agent budget (the budget ladder) estimates
lambda; r = lambda / b. K is the product of separately measured factors (this return, the ladder
term epsilon_R,C and the scaling term epsilon_C,A [@cunningham2026rsi]) with a Bonferroni product
bound, or is estimated from the identity in a closed-loop run. Each round is run at every budget on
the ladder, so [5 rounds](numbers.md#claim-d2-rounds) cost
[15 staged runs](numbers.md#claim-c4-staged-runs).

**Standing: downgraded to a measurement design.** The identity is proved (L2), but at the only
data-calibrated noise every estimator E4 tried fails L3: its interval under-covers, its estimate is
biased toward the unsafe side or its upper bound is unbounded, and the trigger built on it fires
about as often below 1 as above. A claim that fails a level is cut or downgraded, so C4 is no longer
a candidate contribution. What stands: (a) the identity and the budget ladder as a design for
measuring K, whose interval under-covers at the data-calibrated noise for every round count E4
tried; (b) untested: on real staged runs the interval puts r on one side of 1; (c) cut: restricting
closed-loop research on a declared frontier-scale system while the upper bound on K exceeds a margin
K* below 1. Until a trigger separates loops below 1 from loops above, a declared closed loop at
frontier scale is treated as above it, which is the prior-work ban, and any trigger binds only the
loops a developer declares.

**What would reopen it.** E4(b) measures real staged rounds as large and as tightly measured as E4's
favourable setting, on which the first-order difference regression is close to unbiased
([1.01](numbers.md#e4-diff-fav-bias) of the true r) and the upper bound nearly calibrated (with the
true gain exactly at K* it fires in [94%](numbers.md#e4-fa-gstar-n5) of runs, close to the 1 - alpha
a calibrated one-sided bound gives); and on such rounds an estimator's
[90%](numbers.md#claim-confidence) interval reaches its nominal coverage within a stated number of
rounds. A trigger would need, besides, an elicitation step that catches a withheld share of each
round's gain below [16%](numbers.md#e4-hide-silence-fav), the least that keeps it silent in half of
E4's runs even on favourable rounds.

**Results so far.**

- **L1** ([C4](verification/l1-prior-art-c1-c6.md#c4)): extends prior work, narrowly. The
  upper-bound rule and the two held-out sets leave "what remains" (credited below). What remains is
  the exact round identity as the estimator of K for a staged AI research loop, and the budget
  ladder.
- **L2** ([C4](05-formal.md#c4-the-loop-gain-estimator)): proves the identity, lambda from budgets
  and the product bound. It moved the trigger from the per-round ratio g, which tends to 1 in every
  subcritical loop (a perfectly measured g_k passed 0.9 within twelve rounds in each of 200 seeded
  instances), to K. It withdrew the old bound on the loop's total gain,
  [2.7](numbers.md#path-rsi-multiplier-median) times its first round's: in the common form a
  subcritical loop's level is unbounded, though it grows ever more slowly. Corollary 4.5a: the K
  rule fires wherever the rule on r does, so r's false-alarm rates understate the trigger's.
- **L3** (E4, rerun with the first-order law, the exact law and the exact likelihood, at the
  speedrun-calibrated noise, the only noise calibrated on data, and at a favourable noise no real
  staged run has shown): fails, for the measurement and the trigger alike. The measurement: after 5
  rounds at each budget the 90% interval covers r [82%](numbers.md#e4-cov-n5) of the time at the
  corrected median, [77%](numbers.md#e4-cov-n5-min) at worst over the grid, and
  [77%](numbers.md#e4-cov-n5-xml) with the exact likelihood; after 50 rounds, no better than
  [84%](numbers.md#e4-cov-nmax-min) at worst. Every estimator is biased toward the unsafe side or
  useless. On data from the exact law the first-order fit returns [0.82](numbers.md#e4-level1-bias)
  of the true r and the exact likelihood [0.77](numbers.md#e4-xml-bias); the first-order difference
  regression returns [0.47](numbers.md#e4-diff-bias) on its own law; and after 5 rounds the upper
  bound is unbounded in [44%](numbers.md#e4-ub-unbounded-n5) of runs. The two-set remedy fails at
  this noise. Where the noise is real variation in a round's gain, a second held-out set measures it
  identically; where it is all measurement error, the difference regression goes from
  [0.57](numbers.md#e4-diff-bias-meas1) of the true r on one set to
  [8.11](numbers.md#e4-diff-bias-meas2) on two. The exact difference form on two sets is unbiased
  ([1.00](numbers.md#e4-xdiff-bias-half2-mid)) only at smaller noise.
- **L3, the trigger** (E4): at the corrected median of r, after 5 rounds per budget, the upper-bound
  rule on r fires in [84%](numbers.md#e4-fa-n5) of runs and the K rule in
  [88%](numbers.md#e4-k-fa-n5). At the corrected 95th percentile each fires only
  [3%](numbers.md#e4-fire-gap-n5) and [2%](numbers.md#e4-k-fire-gap-n5) more often, within Monte
  Carlo error. Drawing each round's variation from the speedrun's own residuals leaves that gap at
  [3%](numbers.md#e4-fire-gap-n5-emp); exact-law data and the exact likelihood leave it at
  [9%](numbers.md#e4-fire-gap-n5-level1) and [7%](numbers.md#e4-fire-gap-n5-xml). After 50 rounds
  false alarms are still [68%](numbers.md#e4-fa-nmax) for r and [80%](numbers.md#e4-k-fa-nmax) for
  K. Only favourable rounds separate safe from runaway, with a gap of
  [64%](numbers.md#e4-fire-gap-n5-fav) for r and [54%](numbers.md#e4-k-fire-gap-n5-fav) for K, and
  even then false alarms at the median fall to 10% only after
  [12 rounds per budget](numbers.md#e4-fa-rounds-fav) for r,
  [36 staged runs](numbers.md#claim-c4-staged-runs-fav), and
  [20 rounds per budget](numbers.md#e4-k-fa-rounds-fav) for K,
  [60 staged runs](numbers.md#claim-c4-k-staged-runs-fav). A pattern sandbagger defeats it there
  too. An agent set to withhold a quarter of each round's achievable gain on average, in the pattern
  that most delays the trigger, keeps the rule on r silent in
  [96%](numbers.md#e4-late-ub-hide25-fav) of runs at the corrected 95th percentile and the K rule in
  [90%](numbers.md#e4-k-late-hide25-fav). The smallest withheld share that keeps the rule on r
  silent half the time is [16%](numbers.md#e4-hide-silence-fav) on favourable rounds and
  [42%](numbers.md#e4-hide-silence-cal) at calibrated noise. A uniform shortfall moves only the
  intercept and changes nothing: silent in [13%](numbers.md#e4-late-ub-uniform25-cal) of runs
  against [14%](numbers.md#e4-late-ub-s0-cal) for an honest agent.
- **L3, the history** (E4(a) and E9): the speedrun's r is withdrawn and reported as not identified.
  Its stock and input move together, with a correlation of [0.98](numbers.md#e4-sr-collinearity)
  across months; the fitted returns exponent and return to input move together across bootstrap
  draws ([0.95](numbers.md#e4-sr-boot-corr)); and placebo inputs give an r of
  [0.59](numbers.md#e4-sr-placebo-r-records) (the count of recent records in place of contributors)
  and [1.03](numbers.md#e4-sr-placebo-r-time) (months since the start). E9, the prior on r: no data
  identifies compute's share of research input. Counting compute's historical growth, the
  language-model gain at fixed compute at a share of [0.67](numbers.md#dyn-research-compute-share)
  is [0.25](numbers.md#e9-lm-k-fixed) ([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile),
  above 1 only for shares below about [0.26](numbers.md#e9-lm-share-crit). C4.5's fault generalises:
  Stockfish's r, [0.73](numbers.md#e9-chess-r), rests on its two trends, since a smooth placebo
  input growing at the same rate gives [0.79](numbers.md#e9-chess-placebo-r).
- **L4** ([C4](verification/l4-red-team.md#c4)): fails as a trigger on current evidence (C4.1),
  which E4's rerun confirms for both rules. The rerun answers the rest it could: it models a
  sandbagger whose hidden return an elicitation step could recover (C4.2), tests the two-set remedy
  under measurement error (C4.3, it fails at calibrated noise), counts rounds per budget (C4.4),
  withdraws the speedrun's r (C4.5), fits the exact identity (C4.6) and quotes the K rule's rates
  (C4.7). Undeclared loops (C4.8) and transfer to the frontier (C4.9) remain.

**Which bound, and what it costs.** If a trigger returns, the rule is on the upper bound, the
epidemic rule [@blumberg2020supercritical]: it leaves a loop above K* unrestricted with probability
at most alpha, where a lower-bound rule missed [89%](numbers.md#e4-miss-lb-s0-fav) of loops at the
corrected 95th percentile on favourable rounds, [95%](numbers.md#e4-miss-lb-s0-cal) at calibrated
noise and [100%](numbers.md#e4-miss-lb-hide25-fav) against the pattern sandbagger. The trigger is on
K, and the K rule fires at least as often as the rule on r, so its price is K's. At calibrated noise
it fired at the corrected median in [88%](numbers.md#e4-k-fa-n5) of runs after 5 rounds per budget
and [80%](numbers.md#e4-k-fa-nmax) after 50, and at the corrected 95th percentile it failed to fire
in [10%](numbers.md#e4-k-late-cal). Only favourable rounds, which no real staged run has shown,
bring its false alarms to 10% in [20 rounds per budget](numbers.md#e4-k-fa-rounds-fav),
[60 staged runs](numbers.md#claim-c4-k-staged-runs-fav), at a placeholder margin of
[0.90](numbers.md#e4-gstar).

**What it rests on.** [Y1a](013-dynamical.md#y1a-the-software-loop) and D2. In E4's count,
[5 records](numbers.md#e4-ai-records) of [92 records](numbers.md#e4-records) in the speedrun credit
an AI system, each with a human, for [1.1%](numbers.md#e4-ai-share) of its log speedup.

**Prior work, and what remains.** Acting on whether the upper bound of a reproduction number exceeds
one is epidemic practice [@blumberg2020supercritical]; estimating a subcritical reproduction number
from successive generations is [@blumberg2013stuttering]; the error bias of growth-on-level
regressions is [@freckleton2006census], and independent repeated measurements to remove it are
[@ashenfelter1992twins]; a staged, fixed-budget test of an AI research loop with held-out scoring is
[@srikanth2026aide2]. [@cunningham2026rsi] names the loop gain, derives its threshold and calls
estimating it "arguably the most important empirical exercise"; [@burtsev2026criticality] defines a
reproduction number with no estimation procedure; [@eth2025sie] proposes disclosed measurement;
[@anthropic2026rsp], [@openai2025preparedness] and [@metr-anthropic-acceleration-2026] use ratios of
overall progress rates with inputs free; [@besiroglu2024returns] and [@tadepalli2026efficiency]
estimate returns observationally; [@zhao2025speedrun] is the harness. What remains ours, as a
measurement design and not a contribution until it passes L3: the exact round identity as the
estimator of K for a staged AI research loop, and the budget ladder for lambda. Both are elementary,
and we did not find them stated, which is a claim about our search and L1's.

**What would refute it.** (b): the interval always spans 1, or E4(b) at two scales gives values of r
that differ beyond their intervals, so a small run says nothing about the frontier. The design:
E4(b) measures a staged round's noise as large as the calibrated one, at which E4 found no estimator
that works, and C4 is cut.

**L3.** Done: E4(c), with the first-order and exact laws, the exact likelihood, two held-out sets,
the trigger on r and on K, and a pattern sandbagger; E4(a), the speedrun history; E9, the prior. To
come: E4(b), a staged run at two scales, which measures a round's noise and so decides whether C4
reopens or is cut.

**L5, L6.** Pending.

## C5. Elicited capability with measured miss and false-alarm rates per named budget

**The claim.** A threshold is judged on the score a named elicitation protocol E recovers, E's methods
listed (fine-tuning on k demonstrations, RL with n samples, best-of-k, public scaffolds, noise
injection, weight-level methods) and revised on a schedule. Each E carries a **miss rate** (the share
of organisms with hidden capability above the threshold whose elicited score stays below) and a
**false-alarm rate** (the share of benign models lifted over), each with a one-sided upper bound,
measured over naive, RL-locked and tamper-resistant organisms built after E is fixed by builders
blind to it, and stated only over the range where E's methods work. Adaptive organisms, built with E
in hand, are measured apart: they are what a developer who sees E can build. The rates describe the
sampled population, not a strategic developer who picks a hiding method outside it, and they cannot
be measured above expert level, where no builder can lock a capability nobody has. Organisms from a
few builders are clustered, so the count that matters is of independent builds. Claimed: (a) the
rule, as a trigger rivals can run with weight access or a trusted enclave, valid against hiding
methods inside the sampled population; (b) some affordable budget brings both bounds below their
targets, [10%](numbers.md#claim-d5-miss-target) and
[10%](numbers.md#claim-d5-false-alarm-target), on naive and RL-locked organisms in the covered range;
with no misses, the miss target at [90%](numbers.md#claim-confidence) one-sided confidence takes
[22 organisms](numbers.md#claim-d5-organisms) per budget,
[38 organisms](numbers.md#formal-d5-organisms-one-miss) with one miss and
[52 organisms](numbers.md#formal-d5-organisms-two-miss) with two, or a sequential test stops earlier;
(c) stated in advance: on tamper-resistant and adaptive organisms the claim is expected to fail,
their range falls outside the guarantee, and the protocol leans on compute (C2).

**Results so far.**

- **L1** ([C5](verification/l1-prior-art-c1-c6.md#c5)): extends prior work. The statistics are
  diagnostic-test practice and the counts the zero-failure binomial bound (credited below). What
  remains is the application, both rates per named budget as the pass-fail rule of a threshold rivals
  run, and the definition of the organism population. [@taylor2025auditinggames] states that this
  has not been done.
- **L2** ([C5](05-formal.md#c5-miss-and-false-alarm-rates-with-exact-bounds)): proves it, all
  textbook: the exact one-sided bound, a sequential test valid under any stopping rule, and a bound
  showing that a share of untested kinds of organism moves the faced miss rate by at most that share.
- **L3**: E3 has not run.
- **L4** ([C5](verification/l4-red-team.md#c5)): survives with corrections, valid only against
  non-adaptive hiding inside the sampled population. A population rate does not bound a strategic
  developer (C5.1). Organisms blind to E are weaker than a developer who sees it: an audit's AUC fell
  from [0.978](numbers.md#def-adaptive-auc-before) to [0.560](numbers.md#def-adaptive-auc-after)
  against adaptive organisms (C5.2). The trigger is unvalidated above expert level (C5.3), and a few
  builders give a clustered sample (C5.4). Each is now in the statement.

**What it rests on.** [D5](01-anatomy.md#d5-elicited-capability-robust-to-hiding) and
[F4](014-cognitive.md#f4-measuring-capability-so-a-protocol-can-trigger-on-it). A tamper-resistant
organism recalled [7.8%](numbers.md#def-robust-hard-recall) on hard tasks against
[71.2%](numbers.md#def-robust-base-recall) for its base; an RL lock held for more than
[500 GRPO steps](numbers.md#def-xh-rl-lock-steps); elicitation lifted benign models about
[10 points](numbers.md#def-audit-benign-uplift).

**Prior work, and what remains.** Sensitivity and specificity with exact one-sided bounds are
diagnostic-test practice [@fda2007diagnostic]; evaluating after a defence is fixed is security
practice [@carlini2019evaluating; @tramer2020adaptive]. A fixed budget was in [@anthropic2023rsp] and
was dropped; [@eu2025gpaicode] asks for state-of-the-art elicitation with no budget or miss rate;
[@openai2025preparedness] treats elicitation as a lower bound. Per-budget success on locked organisms
is in [@greenblatt2024password], rates with intervals per method in [@abubaker2026fuzzing], and
hardened organisms in [@finke2026robustorganisms] and [@duddu2026deceptive]; the organism method is
also [@taylor2025auditinggames], [@hofstatter2025elicitationgame], [@jang2026explorationhacking] and
[@soopal2026adaptive]; tests of absence are in [@bukkapatnam2026absent]. What remains ours: both rates
per named budget, over a defined population of organism kinds, as the pass-fail rule of a trigger
rival parties run, with its range and its limit to non-adaptive hiding stated.

**What would refute it.** No affordable budget meets the targets on RL-locked organisms: the claim
then covers only naive locks, which prior work already shows, and is cut. A rate measured on blind
organisms fails to predict the rate on adaptive ones even inside the covered range, so the population
rate is not worth publishing.

**L3.** To come: E3, starting from public password-locked weights [@redwood2024mathpwdlock], the
auditing-game organisms [@aisi2025auditingrepo] and noise injection [@tice2024noise;
@tice2025noiserepo], with adaptive organisms built by a separate team that has E in hand.

**L5, L6.** Pending.

## C6. The coupled-gain certificate as a treaty test

**The claim.** With K the gain matrix over loops and parties, K_ij = lambda_i * e_ij / b_i
([Y3](013-dynamical.md#y3-coupling)), signs allowed, if upper bounds U_ij >= |K_ij| hold jointly
with probability at least 1 - alpha, then rho(K+) <= rho(U) and rho(K) <= rho(U) <= max_i sum_j U_ij
with that probability, K+ being K with its negative couplings set to zero, and any positive weights
w give rho(U) <= max_i (sum_j U_ij w_j) / w_i: the linear case of the network small-gain theorem.
For signed couplings it is rho(K+) < 1 that rules out runaway, and rho(K) > 1 no longer shows it.
Claimed, as an application: (a) the treaty test "the certificate is at most rho*", each edge named,
gated and verified on its own, issued only when every edge has a measured bound that holds jointly
at 1 - alpha. While any edge is a stated range or a party's own report, the result is a calculation
on judgements and no certificate issues. rho* = 1 - m * rho_dot * T_r is fixed by agreement until
rho_dot and T_r are measured. Edges no gate covers, such as weight theft, are listed and bounded, or
the certificate states that it omits them. (b) The smallest set of edge cuts that brings the
certificate below rho*, found by exhaustive search over sets by size, with its sensitivity to each
unmeasured edge. (c) A result computed within the application: rho(U) is at least its largest
diagonal entry, and a fully closed software loop at its corrected 95th percentile,
[1.07](numbers.md#dyn-r-lm-hi-corrected), leaves [-0.07](numbers.md#dyn-software-headroom-upper) of
headroom, so no set of edge cuts issues the certificate at that confidence. Only holding the
software loop's own closure below [0.93](numbers.md#formal-software-closure-max) can. The figure
carries no uncertainty in the research compute share, and E11 shows how much rests on it (below). It
also rests on the published compute correction, which leaves compute's own growth out: counting it,
E9 puts the language-model gain at fixed compute at [0.25](numbers.md#e9-lm-k-fixed)
([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile) at the same share, at which (c) fails,
and above 1 only for shares below about [0.26](numbers.md#e9-lm-share-crit), which no data excludes.
So (c) holds under that correction or at a low compute share, not in general.

**Results so far.**

- **L1** ([C6](verification/l1-prior-art-c1-c6.md#c6)): prior work, downgraded to an application
  (credited below). The claim's own refuter was met: epidemic control states the targeted version and
  control theory the certificate. (c) stands as a result computed within the application.
- **L2** ([C6](05-formal.md#c6-the-coupled-gain-certificate-and-the-runaway-condition)): proves the
  certificate for signed matrices through K+, K with its negative couplings set to zero: rho(U) < 1
  bounds rho(K+) and so rules out runaway for couplings of any sign (Theorem 6.4(ii)). rho(K) > 1 is
  the runaway condition only for nonnegative K, with bounds on the time to blow-up; for signed K it
  no longer shows runaway (E11's signed variant has rho(K) of [1.25](numbers.md#e11-signed-rho) and
  grows only logarithmically), and a signed K with rho(K+) >= 1 is left undecided. (b) needs
  exhaustive search: cutting the largest edge first needed more cuts than the smallest set in 12 of
  296 random instances. (c) restates C4 for a fully closed loop, through the diagonal bound.
- **L3** (E11): against issuing a certificate today. Of the [10 entries](numbers.md#e11-entries) in
  Part I's one-party loop graph, [2 entries](numbers.md#e11-entries-measured) have a measured bound,
  [2 entries](numbers.md#e11-entries-domain) only the natural range of an unmeasured share, and
  [5 entries](numbers.md#e11-entries-unbounded) none, so under (a) nothing issues. The row-sum test
  can never issue while compute feeds software: no U on the graph has a largest row sum below
  [2.14](numbers.md#e11-rowsum-floor). With only the software closure gated, rho(U) issues only if
  the unbounded entries are zero and the economic gain is below
  [0.32](numbers.md#e11-eta-max-gated), or AI's share of hardware research below
  [0.064](numbers.md#e11-ah-max-gated), each with the other at zero. With the compute stock capped
  and update compute metered, [2 gates](numbers.md#e11-gates-vendor), rho(U) would issue for one
  party at the vendor-reported closure, with a margin of [0.72](numbers.md#e11-margin-vendor) for m *
  rho_dot * T_r; but that closure is a party's own report, which (a) does not accept. Between two
  parties the cross-entry bounds are reciprocal ratios of growth rates, so alone they can never
  certify the cycle; one direction must be gated or measured below its bound. Greedy cutting needed
  more cuts than the smallest set in [0 scenarios](numbers.md#e11-greedy-worse) of the grid over the
  real graph, so (b)'s need for exhaustive search, shown on random matrices in L2, does not show
  here. (c) holds, but only while the assumed compute share of research input stays below
  [0.689](numbers.md#e11-epsk-flip); the ledger's value, an assumption of Ho and Whitfill, sits
  [0.022](numbers.md#e11-epsk-gap) below it, and only language models, of the three domains, exceed
  1 when fully closed. E9 adds that the 1.07 behind (c) leaves compute's growth out (statement).
- **L4** ([C6](verification/l4-red-team.md#c6)): survives with corrections, each now in the
  statement: with unmeasured, self-reported edges the certificate carries no probability (C6.1);
  rho* is not a number (C6.2); weight theft is an edge no gate covers (C6.3); (c) restates what C4
  says of a fully closed loop (C6.4).

**What it rests on.** [Y3](013-dynamical.md#y3-coupling). Burtsev's individually subcritical blocs
reach a network rho of [1.15](numbers.md#dyn-burtsev-network-rho), an e-folding time of
[3.6 years](numbers.md#dyn-burtsev-efold-years) on our arithmetic.

**Prior work, and what remains.** The certificate is the linear case of the network small-gain
theorem [@dashkovskiy2007smallgain] and of the textbook comparison of a matrix with an entrywise
bound (Perron and Frobenius; Collatz and Wielandt). The control question in (b) is the type and
target reproduction numbers [@roberts2003typer; @shuai2013targetr] and spectral-radius reduction by
link removal [@vanmieghem2011spectral]. A regulator testing a spectral radius against one, with the
diagonal condition behind (c), is in [@bardoscia2017pathways]. The spectral-radius condition is proved
for AI loops [@davidson2026feedback] and across actors [@burtsev2026criticality], and written as a sum
of channels [@cunningham2026rsi]. What remains ours: the use as a treaty test with each edge gated and
verified, and (c) on this program's numbers. Nothing of method.

**What would refute it.** E11 finds the certificate so loose that no feasible set of cuts issues it
even with every edge measured. No off-diagonal edge can be measured with a joint bound, so the
certificate never issues.

**L3.** Done: E11, on ledger values and stated ranges, so it computes and does not certify. To come:
E11 again with the diagonal from E9 and, if C4 reopens, E4(b), the compute edge from E10 and the
cross-party edge from E6; the economic elasticity has no source and stays a stated range.

**L5, L6.** Pending.

## C7. The coalition share derived from the response time

**The claim.** C1 applied to the hardwired-pause threshold [@fithian2026hardwired]. A coalition
holding a share s of the accounted fleet, at fixed algorithms and with that paper's budget, overhead
and utilisation, has T_b(s) = h_w / s, where h_w is the time the whole fleet would need:
[7.8 years](numbers.md#claim-whole-fleet-horizon) at that paper's assumed breakout budget of
[2e+29 FLOP](numbers.md#def-hwp-breakout-budget) and projected end-2026 fleet. C1 then gives the
largest admissible share s* = min(1, h_w / (m * T_r)), with drift added through C2. Claimed: (a) s*
derived from T_r rather than chosen, reported as a function of the breakout budget B, the input it
depends on most: h_w is proportional to B at fixed algorithms, so it falls from the paper's budget
to [28 days](numbers.md#claim-whole-fleet-days-frozen) at that paper's frozen frontier of
[2e+27 FLOP](numbers.md#claim-hwp-frozen-frontier) and to
[1.4 days](numbers.md#claim-whole-fleet-days-1e26) at
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local), and s*(B) = min(1, h_w(B) / (m * T_r)) falls below
1 once m * T_r exceeds h_w(B); (b), downgraded: no coalition whose breakout time is at least T_r has
a profitable joint deviation its members would not report, provided (i) each member's reward for
reporting exceeds beta times its value of a successful breakout, R_i > beta * V_i, the reporting
condition of cartel leniency [@aubert2006leniency], or (ii) no party profits alone, beta * V_i <= (1 -
beta) * P_i, P_i its penalty if caught. Neither holds for a party that values a decisive advantage
at more than (1 - beta) / beta times its penalty, so (b) is empty for decisive-advantage payoffs,
the case the work calls realistic. Under repeated play (Theorem 7.2, after E6), (ii) survives
whether caught members are re-admitted or expelled, but under re-admission (i) needs a reward of
beta * V_i / (1 - delta * (1 - beta)), up to 1/beta times the one-shot beta * V_i, rising towards
V_i as the discount factor delta nears 1. (c), downgraded: at the cited budget the overt constraint
binds only when m * T_r exceeds h_w. That is a property of one assumed number; h_w scales with the
budget. Four limits remain. s counts the accounted fleet, on which a covert path does not draw, and
the fleet is uncertain by the factor of [4.1](numbers.md#org-huawei-spread) between outside
estimates of one maker's output. s* needs a bounded T_r, which C1 does not have, so the share has no
number until a response is drilled. Against a coalition that includes a major power T_resp may be
unbounded, and the result is empty. And s* assumes drift fixed at launch: a coalition that passes
the line and grows until the next declaration, buying all world chip sales at the 2025 rate (an
upper bound for one coalition) while its run absorbs algorithmic progress (an upper bound on drift),
at the hardwired-pause paper's more bullish budget and an illustrative T_r, reaches a per-attempt
success of [0.076](numbers.md#e6-staged-pi-line-inrun) against beta of
[5%](numbers.md#def-prevent-beta) (E6), so with in-run drift, at E6's illustrative T_r and that
budget, the share must fall to [69%](numbers.md#e6-staged-share) at the central drift and
[29%](numbers.md#e6-staged-share-high) at the high end, with no margin left. The formal file now
counts it (Corollary 1.6a, carried into Proposition 7.1 and Theorem 7.2): with drift absorbed during
the run, s* = min(1, h_w / G(m T_r)), so keeping the margin lowers a share computed at launch speed
by up to the factor a launch-speed line must rise, [3.2](numbers.md#formal-inrun-line-factor) at the
central drift rate and [10.6](numbers.md#formal-inrun-line-factor-high) at the high end, both upper
bounds; and Theorem 7.2's conditions hold for every share whose breakout time, drift counted, is at
least T_r. At Part II's declared line and that paper's assumed budget, with the margin kept, the
in-run share is [100%](numbers.md#prot-coalition-share-inrun) at the central drift, where the cap at
1 binds, and [37%](numbers.md#prot-coalition-share-inrun-high) at the high end, both lower bounds
since the factor is an upper bound. Growth between declarations lowers the share again: Proposition
1.6 asks the line to hold at phi * m * T_r at each check. E22 bounds the supply part of phi for the
fleet at [1.65](numbers.md#e22-phi-member-quarter) a quarter and
[2.5](numbers.md#e22-phi-member-year) a year, and Part II multiplies in the central algorithmic
drift between checks, giving [2.1](numbers.md#prot-phi-quarter) for a check at each licence renewal
and [6.8](numbers.md#prot-phi-year) for one a year. With that phi at each renewal on top of in-run
drift at the central rate, Part II's share is [58%](numbers.md#prot-coalition-share-inrun-phi), for
a coalition that grows no faster than the fleet; one that takes more than its share of new chips
grows faster and must hold less. E6's staged shares already count growth between declarations,
supply and algorithms both, so they compare with this share, not with the pair before it, and do not
fall further for supply. They differ from it in the budget (E6 uses the paper's more bullish one,
which shortens h_w), the margin (none: E6 asks only that a staged attempt succeed with at most
beta), T_r (illustrative) and the purchase rate (all new chips, against a coalition growing with the
fleet).

**Results so far.**

- **L1** ([C7](verification/l1-prior-art-c7-c12.md#c7)): prior work. (a) is the overt breakout fleet
  threshold of [@fithian2026hardwired] divided by the fleet, with the horizon replaced by m * T_r;
  (b)(i) is the cartel reporting condition and (b)(ii) the standard deterrence condition; (c) is
  arithmetic at that paper's inputs. Nothing survives independent of C1: cut as a contribution, kept
  as an application.
- **L2** ([C7](05-formal.md#c7-the-coalition-share)): proves (a), with growth and drift, which only
  lower s*, and with the drift a run absorbs while it runs: Proposition 7.1 gives s* = min(1, h_w /
  G(m T_r)), a launch-speed share lowered by up to [3.2](numbers.md#formal-inrun-line-factor) at the
  central drift rate and [10.6](numbers.md#formal-inrun-line-factor-high) at the high end, both
  upper bounds (Corollary 1.6a). Theorem 7.2 states (b) with its conditions for every share whose
  breakout time, drift counted, is at least T_r, and adds repeated play: (ii) survives re-admission
  and expulsion, and (i) needs up to 1/beta more under re-admission. The old (b), that some
  coalition above s* can deviate, was false. `c7_coalition.py` passes on the corrected count (C7.2),
  the drift case and re-admission.
- **L3** (E6): against (a) as first stated, which met its own staged-accumulation refuter; the
  statement is corrected for in-run drift. (b) illustrated, nothing measured. The published games
  reproduce: Armstrong et al.'s [8](numbers.md#e6-armstrong-claims-held) qualitative statements
  tested, Gan's [32](numbers.md#e6-gan-reproduced) published values, and Fudenberg and Koh's,
  Nordhaus's and Barrett and Dannenberg's results. C7.1: the sourced payoff calibrations, Gan's
  illustrative payoffs (a prize over penalty of [0.47](numbers.md#e6-gan-prize-over-penalty)) and an
  analogue from Fudenberg and Koh, all fall inside condition (ii)
  ([2](numbers.md#e6-sourced-payoffs-inside)); they are illustrations, and the share of real parties
  inside it is not identified. C7.3: over the hardwired-pause paper's own budget range the overt
  line binds in [5%](numbers.md#e6-budget-binding-share) of it at the illustrative T_r and
  [36%](numbers.md#e6-budget-binding-share-e24) at E24's median time to a halt, and s* at the low
  end of the range is [84%](numbers.md#e6-share-bullish) and [43%](numbers.md#e6-share-bullish-e24)
  respectively, illustrations while T_r is unbounded. C7.7: repeated play keeps (ii) but
  re-admission weakens (i); staged accumulation with drift fixed at launch stays below beta
  ([0.009](numbers.md#e6-staged-pi-line)), but absorbing drift during the run it reaches
  [0.076](numbers.md#e6-staged-pi-line-inrun), which meets this claim's staged-accumulation refuter,
  so (a) now counts in-run drift. E22: supply bounds the fleet's phi at
  [1.65](numbers.md#e22-phi-member-quarter) a quarter and [2.5](numbers.md#e22-phi-member-year) a
  year (China's domestic supply alone [2.4](numbers.md#e22-phi-china-year) a year); with the central
  drift between checks Part II's phi is [2.1](numbers.md#prot-phi-quarter) at each licence renewal
  and [6.8](numbers.md#prot-phi-year) a year, and with it the in-run share at Part II's declared
  line is [58%](numbers.md#prot-coalition-share-inrun-phi). New allied supply alone reaches the
  hardwired-pause budget in no less than [0.45 years](numbers.md#e22-member-years-to-hwp), China
  from its stock in no less than [0.7 years](numbers.md#e22-china-years-to-hwp), and a denied party
  without a stockpile in no less than [3.9 years](numbers.md#e22-nostock-years-to-hwp), each a lower
  bound.
- **L4** ([C7](verification/l4-red-team.md#c7)): survives with corrections; (b) and (c) downgraded.
  The protection exists only where rewards exceed beta times a decisive advantage, a region the work
  calls empty (C7.1). This file's sentence that between s* and m * s* "none can" deviate dropped the
  conditions; the check counted shares where neither was checked, and a direct counterexample exists
  (C7.2). (c) is an artefact of the assumed budget (C7.3); (a) now gives s* over the budget. Also:
  Part II's covert shares (C7.4), the stock counted (C7.5), major powers (C7.6).

**What it rests on.** [D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr) and
[O3](015-organisational.md#o3-chokepoints). The hardwired-pause overt threshold is
[3.9](numbers.md#def-hwp-fleet-over-global) times the projected global fleet; its covert evasion
threshold is [0.47 years](numbers.md#org-fe-years-of-sales) of 2025's chip sales.

**Prior work, and what remains.** [@fithian2026hardwired] derives per-state breakout thresholds from a
budget and a horizon chosen by judgement, with coalitions in a footnote; deriving allowed holdings
from a breakout target is older still [@whitehouse2015jcpoaparameters]; the reporting condition is
cartel leniency [@aubert2006leniency]. [@gan2026clock] is bilateral; [@rahman2025nonparty] and
[@scher2025agreement] say the coalition must hold most hardware without deriving how much;
[@koopmanschap2026gpu] states "sufficient capacity" without a number. Stability:
[@bernheim1987coalition], [@ali2019coalitions], [@nordhaus2015climate], [@barrett1994self]. What
remains ours: nothing independent of C1. The coalition reading is an application.

**What would refute it.** E6 finds a coalition below s* that profits, for example by staged
accumulation that keeps each step outside the line, or repeated play undoes the one-shot result.

**L3.** Done: E6, on illustrative payoffs; E22 (how much each kind of party can add, and phi). To
come: payoffs measured rather than illustrated, which no experiment yet plans.

**L5, L6.** Pending.

## C8. The aggregate footprint floor, a margin per channel, and the untraced pool

**The claim.** For a run of C useful operations finished within T on chips whose utilisation never
exceeds u_bar, the chip count in units of a reference peak r is at least N_min = C / (r * u_bar *
T), and the energy at least E_min = C * e_min. r is the peak at the lowest precision a run can use,
FP8 in the sources (a run held to BF16 needs twice the chips); u_bar the highest utilisation an
adversary can reach, full for the bound; e_min the lowest energy per operation of any chip it can
use. T is the longest run a party will accept, taken as the longest sensible run under prevailing
growth rates [@rahman2026]: an assumption a racing party need not share, and the floor halves when T
doubles. Each channel's margin is its detection limit over the floor it sees. Claimed: (a) of the
channels modelled, only chip accounting sees the aggregate floor, and its resolution must be finer
than N_min at the run length a pause makes rational; a distributed run's traffic and purchases are
aggregate signatures that no experiment yet models; (b) cut: the physical chapter's falsifier, that
every facility channel's margin exceeds one for a distributed run at
[1e+25 FLOP](numbers.md#phys-rahman-1e25-target), cannot fail; (c) the untraced pool is a covert
reserve in every party's breakout time, and already exceeds the floor many times over. For a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run at a pause's run length, with the floor at BF16
and utilisation drawn over its measured range, E8 puts the pool at
[340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the floor
([110](numbers.md#e8-pool-over-floor-1e26-pause-p05) to
[1,000](numbers.md#e8-pool-over-floor-1e26-pause-p95), 5th to 95th percentile; the pool's size is an
assumed order of magnitude), and the compute smuggled into one country, which has a published
interval, at [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times
([94](numbers.md#e8-smuggled-over-floor-1e26-pause-p05) to
[590](numbers.md#e8-smuggled-over-floor-1e26-pause-p95)). An FP8 run doubles each ratio. Against the
floor taken as a bound, FP8 at full utilisation, the smuggled median is
[824](numbers.md#formal-pool-over-floor-bound) times: one estimate over the lowest floor, above E8's
range for the smuggled stock at BF16 and inside it at FP8. Every reading puts the reserve far above
the floor, which is all (c) needs; (d) with C3, at the historical discovery rate, the line holds for
that reserve only if it cannot reach C* at all, so the protocol must shrink the pool, not hope to
find what it hides. (c) and (d) are the hardwired-pause paper's ledger at other inputs; the bound
and the measured discovery rate are the difference.

**Results so far.**

- **L1** ([C8](verification/l1-prior-art-c7-c12.md#c8)): extends prior work, narrowly. The closest
  work is [@fithian2026hardwired] (credited below). What remains is the floor as a bound at the
  lowest precision a run can train at, full utilisation and the lowest energy per operation, where
  that paper's threshold is an estimate; each channel's margin over the floor and the year it
  crosses one; and the pool's multiple with a measured discovery rate behind (d).
- **L2** ([C8](05-formal.md#c8-the-footprint-floor-as-a-bound)): N_min is a bound once corrected.
  The physical chapter's floors, at a reference utilisation of [40%](numbers.md#phys-util-ref) and
  the BF16 peak, are estimates [5.0](numbers.md#formal-floor-ref-over-bound) times the bound, and
  were undercut in 2,184 of 20,000 random runs. `c8_floor.py` passes on the precision correction.
  The bound for that run under a pause is [800 H100e](numbers.md#formal-floor-bound-1e26-pause), or
  [1,600 H100e](numbers.md#formal-floor-bound-1e26-pause-bf16) for a run held to BF16, not the
  chapter's [4,000 H100e](numbers.md#phys-floor-chips-1e26-pause).
- **L3** (E8): supports (a) and (c). E8's bound agrees,
  [800 H100e](numbers.md#e8-floor-1e26-pause-bound). (a): for chip accounting to resolve such a run,
  the untraced pool must shrink [1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold. (c): the
  untraced pool is [340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the floor at BF16 and
  the compute smuggled into one country [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50)
  times, each doubled for an FP8 run, with the intervals given in (c). (d): E5 gives the pool a T_d
  of [32 years](numbers.md#e5-td-pool-years). Facility channels also lose concentrated runs: a
  [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run on one site over today's run length falls
  below the satellite line by [2029](numbers.md#e8-cross-sat-1e26-now)
  ([2026](numbers.md#e8-cross-sat-1e26-now-p05) to [2032](numbers.md#e8-cross-sat-1e26-now-p95)).
  E22 cannot test (c): its envelope is an upper bound on what supply could make, so it can never put
  the pool below the floor. It shows only that supply leaves room for the pool: the smuggled stock's
  95th percentile is [8.9%](numbers.md#e22-smuggled-share-of-allied) of allied 2024-25 sales, and
  the room China's domestic chain leaves for undeclared output is
  [3,549](numbers.md#e22-china-slack-over-floor) times the floor. A test that cannot fail is not
  evidence, so (c)'s L3 rests on E8 alone.
- **L4** ([C8](verification/l4-red-team.md#c8)): survives with corrections. The bound was at
  BF16 while FP8 training at scale is in production [@deepseek2024v3]; it is now at FP8 (C8.1). (b)
  cannot fail, since a one-node site sits far below every facility limit whatever the run: cut
  (C8.2). Also, now in the statement: T is the adversary's (C8.3), "only" was false (C8.4), and the
  pool of [1,000,000 chips](numbers.md#phys-chips-unaccounted) is an assumption (C8.5).

**What it rests on.** [P4](011-physical.md#p4-the-footprint-and-its-floor). Satellites reliably found
facilities above [10 MW](numbers.md#phys-sat-reliable); about
[1,000,000 chips](numbers.md#phys-chips-unaccounted) are untraced; denial multiplies a denied party's
power per unit of compute by [2.5](numbers.md#org-denial-power-multiplier), a gain for facility
channels.

**Prior work, and what remains.** The formula as an aggregate floor in chips with a time axis, the
untraced pool entered against it, and the conclusion that the pool must be shrunk rather than found
are in [@fithian2026hardwired]. Per-channel detection limits by facility size are in
[@koopmanschap2026gpu]; (a)'s resolution requirement is the IAEA's lesson on material unaccounted for
[@iaea-glossary-2022]. [@scher2025] argues for tracking chips, not data centres;
[@scher2025agreement] caps unmonitored clusters; [@rahman2026] gives the cheapest distributed
configuration and the longest sensible run; [@halstead-ai2040] gives per-site chances;
[@sastry2024compute] flagged distribution. What remains ours: the floor as a bound at the lowest
precision and full utilisation, each channel's margin and crossing year, and the pool's multiple with
E5's discovery rate behind (d).

**What would refute it.** A published crossing-year analysis of satellite or grid detection, which
L1 names as the likeliest way to lose the second difference. E13 measures energy per operation below
the e_min the bound uses. A count of the untraced pool, or a sourced estimate of the smuggled stock,
whose upper end lies below the floor; E22, an upper bound, cannot do this.

**L3.** Done: E8; E22, which cannot refute (c). To come: E14 (distribution tax), E13 (power per
useful operation), and a count of the pool, which no experiment plans.

**L5, L6.** Pending.

## C9. The height-clocked licence, valid only once logged

**The claim.** A chip licence (i) names the hash of a recent Bitcoin block, at height k, so it
cannot predate that block; (ii) ends at a block height k + L: the chip keeps h, the height of the
tip of the chain with the most work it has seen, and a counter t of its own powered time, and stops
once h reaches k + L or its powered time since acceptance reaches the licence's powered-time budget,
set at the longest honest span of L blocks on Bitcoin's record times a margin; (iii) is valid only
once it appears in a public append-only log anchored in Bitcoin, the log that also holds the sealed
training-run declarations, replicated under operators from rival blocs, with every leaf behind every
anchored root published. Only the most-work chain counts, re-evaluated as headers arrive (the formal
file's rule W, which Part II specifies): a chip fed honest headers is stopped early only while a
fork carries more work than the honest chain, which takes most of the hash power. Counting any valid
header's height would let a forged fork stop a chip for good. An offline chip accepts whatever chain
it is fed, so whoever feeds it can stop it, as they could cut its power. Claimed properties: **P1**
no advance signing; **P2** a bounded compute budget: whatever headers it is fed, the chip runs under
one licence for at most that budget of powered time, and the height expiry can only shorten it. This
is the counter's property, not the height clock's; the height clock adds a calendar expiry only for
a chip that keeps receiving honest headers. An earlier design stopped the chip instead when h fell
behind a floor rho_min on the block rate per unit of counter time, bounding it at (L + s) / rho_min
(Proposition 9.1). On Bitcoin's real record that floor is dominated (E25): a floor that never stops
a compliant chip grants at least the longest honest span, and a finite floor adds only false stops,
so Part II dropped it. **P3** no undetected equivocation of licences or declarations; **P4**
provable non-issuance, since an unlogged licence is invalid. P4 trusts the log's operators to
publish every leaf. P3 and P4 answer two problems flexHEG leaves open, proving non-issuance
[@petrie2025flexheg1] and stopping conflicting extensions [@aarne2025flexheg3], by carrying over
Catena and certificate transparency, not by anything new. Not claimed: that sealing makes a
declaration true [@fang2023polbroken], or that any property is new. This is engineering, an assembly
of known parts, claimed as such.

**Results so far.**

- **L1** ([C9](verification/l1-prior-art-c7-c12.md#c9)): prior work, part by part (credited below).
  The assembly for chip licences was not found. An application, claimed as engineering.
- **L2** ([C9](05-formal.md#c9-the-height-clocked-licence)): proves P1 and P3 under stated
  assumptions (a collision-resistant hash, a minimum work per header, agreement at a stated depth,
  an intact secure element) and prices forged headers for stretching a licence. P2 was false under
  the old rule. Proposition 9.1 proves it as the powered-time counter's budget, whatever headers the
  chip is fed, so the height clock adds only a calendar expiry for chips fed honest headers. The
  rate floor it was first proved with had a cost: a floor near the honest rate stops compliant chips
  early when blocks come slowly (112 of 649 honest runs, at the check's settings, not Bitcoin's real
  block intervals); E25 then found the floor dominated, and Part II dropped it for a budget set on
  the record (L3). And P2 bounds powered time, not calendar time, so a chip kept offline across its
  expiry can spend its budget late, flexHEG's idle-chip weakness [@petrie2025flexheg2]. P4 needs
  every leaf published. It specifies rule W, the most-work chain, and prices forged forks under it
  (Lemma 9.2). `c9_clock.py` passes on these corrections.
- **L3** (E25): supports P2, against the rate floor as designed. A verifier checked Bitcoin's real
  [977,000 headers](numbers.md#e25-headers). P2 holds, and it is the counter's. Any floor that never
  stops a compliant chip grants at least the longest honest span plus one interval (asserted in the
  script, true by construction), so the best rule on the record is a powered-time budget at that
  span, [1.099](numbers.md#e25-budget-least) times the nominal licence time, with a margin, plus the
  height expiry. A finite floor only adds false stops: the formal check's own settings, on real
  block intervals, stop [17.1%](numbers.md#e25-falsestop-check) of compliant chips, in line with
  L2's 112 of 649 on simulated blocks. Out of sample, a budget set on the record before 2021 would
  have stopped [6.3%](numbers.md#e25-oos-2021) of licences issued in 2021, when hash rate fell. Rule
  G is a cheap off switch: one forged fork of a licence period costs at most
  [50 days](numbers.md#e25-forge-licence-days) of the whole network's hash rate and ends every
  reachable licence, and ending licences a day early at most
  [13.1 hours](numbers.md#e25-forge-day-hours). Under rule W an online chip is stopped early only by
  more than the honest network's [9.65e+20 hashes/s](numbers.md#e25-net-hashrate), sustained. A
  withheld log leaf is accepted by chips, and auditors see only a root mismatch: asserted in the
  harness, not measured. No hardware prototype exists.
- **L4** ([C9](verification/l4-red-team.md#c9)): survives with corrections. P2 is the counter's
  (C9.1); forged headers can end licences early (C9.2), which rule W confines to offline chips and
  to a majority of the hash power; data availability makes the log operator trusted (C9.3); these
  are now in the statement. One secure element carrying every chip (C9.4) is unanswered.

**What it rests on.** [The height clock](03-novelty.md#bitcoin-block-height-as-the-licence-clock-and-freshness)
and [sealed declarations](03-novelty.md#sealed-declarations) in the novelty file, and the memo's
section on Escapement.

**Prior work, and what remains.** P1 rests on block hashes as unpredictable public values
[@bentov2016beacon]. A height clock in trusted hardware with a monotone checkpoint is in
[@mouallem2026alerting]; the rate floor on headers per unit of trusted local time, with its
false-positive trade-off, is Tesseract's [@bentov2019tesseract]; block-height expiry is standard
[@lightning-bolt2]. P3, a Bitcoin-anchored log that cannot equivocate without a double spend, is
Catena [@tomescu2017catena]. P4 and "valid only once logged" are certificate transparency
[@laurie2013ct] and its use for hardware [@apple2024pcc]. Sealed declarations on a blockchain for
arms control are in [@burford2020trustmachine]. Also prior: a chip nonce that stops advance signing
online [@petrie2024offline]; a blockchain hash as a delay proof, and the idle-chip weakness of cycle
counters [@petrie2025flexheg2]; Bitcoin timestamping [@gipp2015timestamping;
@todd2016opentimestamps]; device fingerprint logs [@harack2025oxford], firmware weight hashes
[@shavit2023chinchilla] and chip ledgers [@alramiah2025pause]. What remains ours: the assembly for
chip licences, as engineering, and what E25 measured.

**What would refute it.** A property fails under its assumptions. The prototype cannot check headers
within a constrained budget. Early stopping by a forged fork cannot be priced above the value of
stopping a rival's chips. A hardware-wallet or trusted-time design that already checks headers offline
on a constrained secure element, which L1 did not search, would make E25 a replication.

**L3.** Done: E25 on the real header record, with forged forks and the rate floor; withheld leaves
are asserted, not measured. To come: the check on a constrained secure element itself. Bitcoin time
is accurate only to hours [@todd2016opentimestamps], so periods are weeks or longer.

**L5, L6.** Pending.

## C10. Superintelligence against an institution at matched time and budget, and the crossover budget

**The claim.** D1 as Part I leaves it ([D1](01-anatomy.md#d1-superintelligence-the-endpoint);
[F4](014-cognitive.md#f4-measuring-capability-so-a-protocol-can-trigger-on-it)): in at least a
fraction alpha of K decisive clusters, S's elicited score beats a named organisation O_k given the
same wall-clock time t_k and money b_k, on items from a regime-held, refreshed pool, with O_k's
tools frozen at a declared date. Matched money gives the system as many copies as the money buys;
matched time gives the organisation its headcount; the verdict is stated under both. Added: the
**crossover budget t\***, the largest tested time budget at which S's score on the AI-research
cluster is at least the comparison's at equal compute and money; if S still wins at the largest
budget tested, t* is censored and reported as a lower bound, never extrapolated. The grid of
budgets, which sets t*, is fixed in advance. Claimed: (a) the combination as a definition, and only
that: D1 holds when a system already beats an institution, so it cannot warn, and the protocol acts
on the line (C1) before it; (b) on clusters with team or institutional baselines, the verdict is
stable when the organisation changes within its class, and the fraction won rises with effective
compute smoothly enough to extrapolate (Part I's pass condition); (c), downgraded on L3: t* is
estimable with an interval and rises across model generations while the battery's baselines last. It
stops at each battery's ceiling (E21), so a rising t* needs batteries refreshed with longer
baselines; "without saturating" is withdrawn.

**Results so far.**

- **L1** ([C10](verification/l1-prior-art-c7-c12.md#c10)): extends prior work. A crossover budget
  between AI and human performance is prior work in two forms (credited below), and tracking one is
  not ours. What remains: time and money matched together against a named organisation as part of a
  definition; the alpha fraction across decisive clusters on a refreshed, regime-held battery; t* at
  equal compute and money, the largest tested crossing, censored and never extrapolated.
- **L2** ([C10](05-formal.md#c10-superintelligence-at-matched-budget-what-is-empirical)): a definition
  needs no proof; t* was defined without assuming the score ratio monotone in budget, hence the
  largest tested crossing, the conservative choice.
- **L3** (E1): by a search of the archive's columns, [5 clusters](numbers.md#e1-clusters-baselined)
  have some human comparison in public data, and [3 clusters](numbers.md#e1-clusters-verdict) a bar
  that a model wins or loses. None is an organisation at matched budget, so (b) cannot be tested on
  public data; E21 must build the baselines.
- **L3** (E21): against (b) on the one analogue, and (c) downgraded. No battery compares with an
  organisation: of [3 clusters](numbers.md#e21-clusters) with a public human comparison, t* has an
  interval in [2 clusters](numbers.md#e21-clusters-tstar). (b): on MLE-bench the verdict flips
  between the median and the gold-medal entrant in [45.3%](numbers.md#e21-mle-flip-best) of
  competitions, so it changes with the comparison within one class of entrant. That is (b)'s
  refuter, met by contest entrants, the nearest thing to an organisation any battery has. (c): t*
  rises with release date, a rank correlation of [0.57](numbers.md#e21-rebench-rho) on RE-Bench
  ([0.16](numbers.md#e21-rebench-rho-lo) to [0.86](numbers.md#e21-rebench-rho-hi)) and
  [0.91](numbers.md#e21-cyber-rho) on Cybench ([0.65](numbers.md#e21-cyber-rho-lo) to
  [0.97](numbers.md#e21-cyber-rho-hi)), with Cybench's t* doubling every
  [114 days](numbers.md#e21-cyber-doubling-days) ([57 days](numbers.md#e21-cyber-doubling-days-lo)
  to [352 days](numbers.md#e21-cyber-doubling-days-hi)). It does not rise without saturating. On
  RE-Bench the best model is at the score's cap in every environment at
  [32 h](numbers.md#cog-rebench-budget-long) in [99.4%](numbers.md#e21-rebench-cap-32h) of
  resamples, so its t* is censored above [32.0 h](numbers.md#e21-rebench-tstar-best) and the battery
  cannot show it rising further. On Cybench t* cannot be measured above the pool's longest
  first-solve time, [24.9 h](numbers.md#e21-cyber-ceiling-h), and the latest model's interval
  already runs from [3.0 h](numbers.md#e21-cyber-tstar-latest-lo) to the grid's top
  ([32.0 h](numbers.md#e21-cyber-tstar-latest-hi), censored). So (c) holds only while a battery's
  baselines last, a downgrade. E2, METR's time horizons refitted, is not t*: it compares an agent
  with one person's time on single tasks, not with an organisation at matched budget, so it tests
  neither (b) nor (c). It shows the same limit as (c): the frontier 50% horizon doubles every
  [129 days](numbers.md#e2-doubling-p50) ([96 days](numbers.md#e2-doubling-p50-lo) to
  [162 days](numbers.md#e2-doubling-p50-hi)), and the latest model's,
  [1,045 min](numbers.md#e2-latest-p50), already lies above
  [8 h](numbers.md#cog-th11-long-threshold), beyond which only
  [5](numbers.md#cog-th11-long-baselined) of [31 tasks](numbers.md#cog-th11-long-tasks) in METR's
  Time Horizon 1.1 suite have a human baseline.
- **L4** ([C10](verification/l4-red-team.md#c10)): survives as a definition only. The endpoint
  cannot warn (C10.1). The old count of three clusters was a dictionary in the code, now a search
  (C10.2). Also: two matches (C10.3), one cluster below D1 (C10.4).

**What it rests on.** [Matching time and cost](014-cognitive.md#matching-time-and-cost). RE-Bench's
AI-to-human ratio moves [8](numbers.md#cog-rebench-swing)-fold between
[2 h](numbers.md#cog-rebench-budget-short) and [32 h](numbers.md#cog-rebench-budget-long) budgets,
about [1.68](numbers.md#cog-rebench-swing-per-doubling) times per doubling; t* for 2024 agents lay
between [2 h](numbers.md#cog-rebench-budget-short) and [8 h](numbers.md#cog-rebench-budget-mid). Only
[5](numbers.md#cog-th11-long-baselined) of [31 tasks](numbers.md#cog-th11-long-tasks) over
[8 h](numbers.md#cog-th11-long-threshold) have a human baseline.

**Prior work, and what remains.** RE-Bench reports where the advantage of agents over experts flips
with the budget [@wijk2024rebench], and a 2026 essay defines the intersection of the AI and human
curves as a quantity and tracks it across models [@robinson2026horizons], t*'s closest relative;
METR's time horizon is related [@kwa2025horizon], and cost-controlled agent evaluation is in
[@kapoor2024agents]. [@genewein2026agiasi] compares with expert collectives with technology frozen and
no budget matching; [@ngo2023tagi] with groups at matched time; [@anthropic2026rsp] with a whole
research staff at matched cost, for one cluster; also [@gdm-fsf-v3-1-2026]. Refreshed batteries
exist [@white2024livebench]. What remains ours, as a definition: time and money matched together
against an organisation, institutional baselines across clusters on a regime-held battery, the alpha
fraction, and t* censored at the largest tested budget.

**What would refute it.** The verdict flips with the organisation within its class, or with t in a
way t* misses: D1 is underspecified. t* cannot be estimated for lack of long baselines: the claim
shrinks to the definition. E21 met the first on contest entrants and the second in part, since t*
stops at each battery's ceiling. A frontier developer publishes evaluations against whole research
teams at matched cost across clusters, which would close the first difference.

**L3.** Done: E1, E2, E21's public part (which absorbs Part I's scaled-down D1 battery). To come:
E21's live part, blocked, and any battery with an organisation's baseline.

**L5, L6.** Pending.

## C11. Closure judged input by input, with narrow optimisers inside the loop

**The claim.** For each input to the next model (compute, weights, data, research labour, money,
cross-party transfer of research results), closure e_i is the share of increments obtained without a
logged human-held gate the regime can verify; a narrow system whose outputs feed a covered system's
training, code or compute counts as part of it. A gate that logs an approval for every request
measures as closed, so the audit's seeded requests must be indistinguishable from real ones to
whoever runs the pipeline, and gates count the agent's completed horizon-length tasks, not hours: a
time horizon is measured in human time [@kwa2025horizon], and an agent that finishes a
horizon-length task in minutes can chain several between gates a horizon apart on the clock, so the
count holds until the agent's own wall-clock time on such tasks is measured for each system, as in
Part I and Part II. Claimed: (a), framing until E4(d): the per-input closures combine for the loop
gain as in task-based automation, K = (lambda / b) * sum_i s_i * e_i under Cobb-Douglas, with s_i
each input's share; under complements the least-closed input comes to set K, under substitutes the
most-closed. Until E4(d) decides which holds, the claim uses the safe bound, (lambda / b) times the
largest closure among ungated inputs, under which the rule is to gate every highly closed input
together, which is prior work. What C11 adds beyond that is empirical: that the gain with gates on
any subset is predicted, within its interval, from closures measured one gate at a time, and that
D6's share of ungated increments can stand for the elasticity the combination uses. (b) A narrow
optimiser in the staged loop raises the measured return beyond its interval when its target is the
training stack, and not otherwise. If (a) fails, per-input closure is framing and is cut; if (b)
fails, narrow systems need no loop exception.

**Results so far.**

- **L1** ([C11](verification/l1-prior-art-c7-c12.md#c11)): extends prior work, narrowly. The
  combination rule, with its complements and substitutes cases, is the task-based automation model
  applied to AI research inputs, and the narrow-optimiser rule is a found-systems prohibition recast
  as a count (credited below). What remains is closure input by input against gates the regime can
  verify, and the one-gate-at-a-time prediction. Two 2026 works found but not opened could decompose
  closure by input, and must be opened before L5.
- **L2** ([C11](05-formal.md#c11-closure-by-input-the-combination-rule)): corrects the rule in (a):
  the loop transmits the exponent K, where closures add, weighted by input shares. It flags that D6
  defines e_i as a share of increments without a gate and the common form as an elasticity. (b) is
  empirical.
- **L3**: E4(d) and E4(e) have not run.
- **L4** ([C11](verification/l4-red-team.md#c11)): survives as framing until E4(d). Under the safe
  bound the decomposition reduces to holding every input together (C11.3). Also, now in the
  statement: rubber-stamp gates and a recognisable audit (C11.1), unmeasured inputs (C11.2), gates
  spaced in human time (C11.4), now counted in the agent's completed horizon-length tasks.

**What it rests on.** [D6](01-anatomy.md#d6-closure), [F3](014-cognitive.md#f3-narrow-versus-general),
[the acquisitive loop](013-dynamical.md#y1e-the-acquisitive-loop), [A4](012-computational.md#a4-data).
Replication task success passed [60%](numbers.md#dyn-aisi-rep-2025) on simplified tasks, with failures
at identity checks [@aisi2025trends; @black2025replibench]. One developer reports that AI leads
[26%](numbers.md#def-anthropic-ai-led) of its AI research work, a self-report [@anthropic2026pace].
The 80% time horizon is about [3 hours](numbers.md#dyn-horizon-p80-hours) of human time.

**Prior work, and what remains.** The combination rule is the task-based automation model of
[@aghion2017ai] applied to the inputs of AI research. The narrow-optimiser rule recasts A Narrow
Path's ban on found systems building found systems [@miotti2025narrowpath] as a count.
[@burtsev2026criticality] defines operational closure; [@chen2026rsisurvey] classifies loops by
closure; [@scher2026research] argues every input must be held together; [@redlines-2025] names
unauthorised self-improvement; [@novikov2025alphaevolve] is a narrow optimiser on a training stack.
What remains ours: closure measured input by input against verifiable gates, and the prediction from
one gate at a time, both untested.

**What would refute it.** (a) or (b) fails in E4(d) or E4(e). The two unopened works decompose closure
by input.

**L3.** To come: E4(d) (gates on and off, with seeded requests a working gate must refuse), E4(e)
(with and without a narrow optimiser), E16, E17, E19.

**L5, L6.** Pending.

## C12. The pathways ranked by their effect on the line

**The claim.** The ranking in [the pathways chapter](02-pathways.md#the-ranking), which closes Part
I, as an application of acquisition path analysis to AI: seven pathways, each judged necessary,
sufficient or neither on stated proxies, ranked by how much each changes the line (it shortens T_b
or lengthens T_r) and how hard it is to see. The cost of a limit sets the response class (restrict,
meter or watch), not the rank, since a cheap limit does not make a pathway more dangerous. The
chapter's order is a judgement: recursive self-improvement and undeclared compute tie first; scaling
of declared compute, training and inference, is third; distillation from a stronger model fourth;
self-replication and resource acquisition fifth; continual learning sixth; long-horizon autonomy
seventh, recast as the clock that spaces the gates. Claimed: (a) the method, with each pathway tied
to a side of D4, to the channel that sees it and to the cost of a limit; (b) of the order, only the
pairs in which one pathway leads on both criteria are fixed by evidence. On an ordinal reading of
the pathways table, with equal grades wherever its entries do not separate two pathways, that is
[12](numbers.md#claim-c12-pareto-two) of [21](numbers.md#claim-c12-pairs): every pathway over
long-horizon autonomy, and self-improvement, undeclared compute and distillation each over continual
learning and over self-replication. None orders the first three places. The same grades on L4's
three criteria, cost included, give L4's own count, [9](numbers.md#claim-c12-pareto-three); taking
cost out adds the pairs over self-replication, whose cheap limit had kept them open. The grades are
inputs in `data/inputs/040-claims.toml`, so a different reading reruns the count. The tie at the top
joins an effect on T_r with an effect on T_b on no common scale. (c) The response class each rank
gets, from which Part II is derived. Not claimed: undeclared compute and distillation as pathways
rather than failure modes, which is prior work in substance.

**Results so far.**

- **L1** ([C12](verification/l1-prior-art-c7-c12.md#c12)): extends prior work, as an application of
  acquisition path analysis (credited below); (b) is prior work. What remains is the ranking itself,
  a judgement applied with a known method, so the label here stays "application of prior work", as
  the report advises: the method is known, and only its use on AI is ours. Bostrom's 2014 chapter on
  paths to superintelligence was not opened, and a reader should check it.
- **L2** ([C12](05-formal.md#c12-the-ranking-what-can-be-proved)): a judgement, not a theorem. A
  pathway is necessary within a horizon if cutting its loops leaves rho(K) < 1 and growth to C* then
  takes longer than the horizon; a supply route is sufficient if on its path T_b(p) < m * T_r(p).
- **L3**: mixed. E5 keeps undeclared compute's discovery rate far from the memo's placeholder, but
  that refuter needed a [12.8](numbers.md#e5-memo-over-hazard)-fold error to fire. In E4(a)
  AI-credited records are [1.1%](numbers.md#e4-ai-share) of the speedrun's log speedup. E1 leaves
  the compute share unidentified, from [18%](numbers.md#e1-compute-share-subset-min) to
  [63%](numbers.md#e1-compute-share-subset-max) across samples, so the premise that compute carried
  most gains, behind declared scaling's rank, is unsettled in both directions. In E11 no pathway's
  gate, cut alone, issues the coupled-gain certificate with honest bounds
  ([0 pathways](numbers.md#e11-pathways-alone-honest) do); the sets that issue it join the gates of
  several pathways: the compute cap and update compute always, the cross-party gate between parties,
  and the closure gate when the software loop is fully closed. That fits a top the evidence does not
  order. E9's only frontier case, OpenAI from 2022 to 2025, gives a gain at fixed compute of
  [0.29](numbers.md#e9-openai-k-fixed) ([0.45](numbers.md#e9-openai-k-fixed-hi) at the 95th
  percentile) at a compute share of [0.67](numbers.md#dyn-research-compute-share), but r of
  [0.89](numbers.md#e9-openai-r), near 1; since no data identifies the share, it does not move the
  rank. E2 measures the clock that long-horizon autonomy is recast as: the frontier 50% horizon
  doubles every [129 days](numbers.md#e2-doubling-p50) ([96 days](numbers.md#e2-doubling-p50-lo) to
  [162 days](numbers.md#e2-doubling-p50-hi)), at a stable ratio to the 80% horizon. It contradicts
  no Pareto pair, since a horizon says how long a task an agent completes, not how close it brings a
  holding to the line.
- **L4** ([C12](verification/l4-red-team.md#c12)): survives as a judgement. On three criteria only
  [9](numbers.md#claim-c12-pareto-three) of [21](numbers.md#claim-c12-pairs) pairs are fixed, none
  at the top (C12.1); the recount on two criteria is in the statement. Also, now in the statement:
  cost mixed danger with ease of restriction (C12.2), the top tie has no common unit (C12.3), the
  refuter could hardly fire (C12.4), E1's sample lacks the frontier (C12.5).

**What it rests on.** [The pathways chapter](02-pathways.md#what-a-pathway-is-and-what-would-decide-necessary-and-sufficient).
Undeclared compute lengthens T_r to [32 years](numbers.md#e5-td-hist-years) at E5's fitted discovery
rate, and the untraced pool, gathered, would run a [1e+26 FLOP](numbers.md#phys-rahman-1e26-local)
job in [2.9 days](numbers.md#path-covert-days-1e26). Algorithms complement compute more than they
substitute [@gundlach2025origin; @whitfill2025bottlenecks]; measured AI contributions to frontier
research are shallow [@shetty2026metrnanogpt].

**Prior work, and what remains.** The method is acquisition path analysis, which ranks paths by time
and detection probability [@allen-2015-llnl]. Comparing paths to advanced AI by arrival time
[@clarke2022mtair] and modelling pathways to superintelligence with fault trees and interventions
[@barrett2016asipath] are older. Undeclared compute counts as breakout capacity in
[@fithian2026hardwired], and distillation and smuggling are named routes [@remler2026distillation].
Davidson, Hadshar and MacAskill compare the loops [@davidson2025three]; [@genewein2026agiasi] lists
four pathways without ranking them; [@delaney2026strategicvisions] compares strategic visions;
[@miotti2025narrowpath] and [@redlines-2025] imply self-improvement first. What remains ours: the
ranking of these seven routes together as a stated judgement, with its
[12](numbers.md#claim-c12-pareto-two) evidence-fixed pairs.

**What would refute it.** An experiment contradicts a Pareto pair. E1 and E15 show algorithms
substitute for compute at the frontier, which would undo "nearly necessary in practice" for declared
scaling. A prior ranking of loops and supply routes together, for instance in the unopened chapter.

**L3.** Done in part: E4, E5, E1, E2, E11, E9 (no data identifies compute's share, so the rank
stands), E18 (the cap leaks in jumps). To come: E15 (scaling), E10's distillation arm, E19, E7.

**L5, L6.** Pending.

## Experiments

This is the one list of experiments for the program and the place their numbers are assigned. E1 to
E11 keep the memo's numbers with Part I's redesigns. New ones are numbered from E12 in chapter order
(physical, computational, dynamical, cognitive, organisational), then two that other files name.
Merges are stated.

Conventions. Each is `tools/exp/<name>.py`, deterministic given a seed fixed in the file and recorded
in the result; it fetches into `tools/exp/cache/` from a source it names and writes
`data/results/<name>.json`, which enters the ledger through the model. CPU work runs under `heavy`, GPU
work under `gpu` (the box's one AMD GPU), one heavy job at a time. Some GPU kernels are not bitwise
deterministic, so GPU experiments repeat at several seeds and report the spread. "Browser" says
whether the core could run on the site. Times are rough. The list is in build order.

**Phase 1: CPU, public data, minutes to hours.**

1. **E4, loop gain, parts c and a.** (c) Coverage of C4's interval and the trigger's false-alarm and
   late-firing rates, simulated in the common form against the number of rounds; rerun with the
   exact round identity, two held-out sets per round under measurement error, the trigger on K, and
   a sandbagger whose hidden return an elicitation step could recover. (a) The speedrun history:
   per-record gains at fixed hardware (FLOP per record from the logs would need a parser per era, so
   wall-clock stands in), systems and algorithmic changes apart, contributors as the input,
   AI-credited records apart, from [@moddednanogpt], [@epoch2026speedrundata] and
   [@shetty2026metrnanogpt]. `heavy`, under an hour. `e04_loop_gain`. C4, C2. Browser: yes.
2. **E1, capability against compute.** Epoch's model data [@epoch2026aimodels] joined to the ECI
   [@epoch2025eci], fitted on log compute with a date term and forecast out of sample at one OOM; Ho et
   al.'s fit rerun from their code and data [@ho2024algorithmiccode] in compute bins; the fraction of
   clusters won and generality against compute. `heavy`, minutes. `e01_capability_compute`. C2, C10,
   C12. Browser: yes.
3. **E5, detection.** C3's Monte Carlo with sourced rates (diversion [@juniewicz2026smuggling],
   metering [@kimpson2026dcpower], chip sampling [@shavit2023chinchilla], E8's facility limits), the
   merging rule and the evader's maximum, against the memo's product; and a survival fit of the
   discovery rate over a wider, sourced set of covert programmes, self-disclosed ones censored, with a
   sensitivity analysis over the cases. `heavy`, minutes. `e05_detection`. C3, C1, C8, C12. Browser: yes.
4. **E24, response latencies.** The time from a confirmed finding to an effective response in the
   arms-control record (the DPRK's notice [31 days](numbers.md#org-dprk-withdrawal-days) after a
   special inspection request [@iaea-gc37-1084]; the Security Council's single day [@bunn2005npt]),
   compiled case by case with sources. Its [17 findings](numbers.md#e24-findings) on
   [8 programmes](numbers.md#e24-programmes) proved too few to fit a distribution by response type, so
   it reports shares, medians and a survival fit with unhalted findings censored, and keeps findings
   made after a party's withdrawal apart. Named in D4's test.
   `heavy`, minutes after compiling. `e24_response_latency`. C1, C7. Browser: yes.
5. **E8, the footprint floor.** N_min, E_min and power for C from
   [1e+22 FLOP](numbers.md#phys-miri-monitored) to [1e+27 FLOP](numbers.md#phys-e8-c-high), T from a
   month to the pause run length, year by year; a Monte Carlo over utilisation, power per chip,
   satellite accuracy, the untraced pool, smuggling and the denial multiplier; each channel's margin and
   crossing year. Ledger inputs [@rahman2026; @koopmanschap2026gpu]. `heavy`, minutes.
   `e08_footprint_floor`. C8, C3. Browser: yes.
6. **E2, time horizons.** The 50% and 80% doubling times refitted from METR's results
   [@metr2026thdata] with a bootstrap, and whether their ratio is stable, shrinking or growing.
   `heavy`, minutes. `e02_time_horizons`. C10, C11, C12. Browser: yes.
7. **E9, returns to research.** r refitted across domains with compute's share free, from
   [@ho2025experiments], [@besiroglu2024returns] and Bloom et al.'s replication package
   [@bloom2020ideas] (licence unconfirmed; failing it, their published tables, said so); how much of
   each interval lies above 1. `heavy`, minutes. `e09_returns`. C4, C6, C12. Browser: yes.
8. **E11, coupled loops.** rho(U), the row-sum and weighted certificates, the smallest cut set and the
   sensitivity to each unmeasured edge, from E9, E4, E10 and E6 as they arrive and stated ranges until
   then. `heavy`, minutes. `e11_coupled_loops`. C6. Browser: yes.
9. **E6, games.** The races of [@armstrong2016racing], [@emeryxu2024uncertainty] and
   [@fudenberg2026cooperating], each with a detection rate, a response time and four information
   regimes; Gan's window [@gan2026clock]; C7's coalition game with a non-member penalty
   [@nordhaus2015climate]; T_b drawn from an interval as in [@barrett2012climate]; withdrawal with
   notice and an asset freeze; cross-party transfer as an edge. `heavy`, under an hour. `e06_games`.
   C7, C1, C6. Browser: yes.
10. **E18, the cap leak.** C2's Monte Carlo at fixed compute (rate from E1's bin at the cap's scale, J
    and the span from E10), the leak time over headrooms and the headroom needed to exceed m * T_r;
    backtested against the open-closed lag [@edwards2026openclosed]. Runs first on Part I's ranges.
    `heavy`, minutes. `e18_cap_leak`. C2, C12. Browser: yes.
11. **E21, the matched-budget team battery, public part.** MLE-bench against Kaggle teams
    [@chan2024mlebench], RE-Bench at matched GPU hours [@wijk2024rebench], forecasting rounds
    [@karger2025forecastbench; @forecastbench2026board; @metaculus2026futureeval], Cybench team solve
    times [@zhang2024cybench]; t* with an interval. Merges Part I's scaled-down D1 battery into the
    cognitive chapter's battery. `heavy`, hours. `e21_team_battery`. C10. Browser: yes.
12. **E22, the supply envelope backtest.** From sourced capacities, the most H100e each of three
    parties could add in 2024 and 2025, against Epoch's sales [@epoch2026chipsales] and outside
    estimates of one maker's output; passes if every observation falls inside. `heavy`, minutes.
    `e22_supply_envelope`. C7, C2, C8. Browser: yes.
13. **E25, the licence clock and log.** A header-chain verifier with a minimum-work rule under a
    constrained memory and CPU profile, on real Bitcoin headers from public sources; licences bound to
    a hash and ending at a height; a log with inclusion and consistency proofs anchored by timestamp
    proofs [@todd2016opentimestamps; @laurie2013ct]; a red-team harness feeding forged, withheld and
    low-difficulty chains, forks that would end licences early, and conflicting licences. Carries the
    memo's tamper tests of sealed declarations. `heavy`, minutes. `e25_licence_log`. C9. Browser: yes.
14. **E23, the durability backtest.** Supply stages ranked on data public at the end of 2022, scored
    against erosion from 2023 to November 2026. A sanity check with so few stages, so last. `heavy`,
    minutes. `e23_durability`. An open question in [O3](015-organisational.md#o3-chokepoints).
    Browser: yes.

**Phase 2: the GPU, open models, hours to weeks.**

15. **E12, serving speed and copies (P-copies with P-speed, one sweep).** Batch-one speed at several
    precisions and throughput at the best batch across the Pythia suite, which spans more than two
    orders of magnitude in size [@biderman2023pythia], against the bandwidth bound and the copies curve
    n = H / (v * 2N), and the gap Pope et al. found [@pope2022]. `gpu`, hours. `e12_serving`. Open
    questions in [P1](011-physical.md#p1-the-compute-budget) and
    [P3](011-physical.md#p3-memory-and-bandwidth); C10. Browser: no.
16. **E13, energy per useful operation (P-energy) and the power-trace tamper test.** Board power from
    the driver during E12's sweep and small training runs, and each term of e (no wall meter, so
    facility overhead stays sourced); then traces with and without the disguises of
    [@kimpson2026dcpower] and a simple classifier's detection rate. The tamper test moves here from E5
    because it shares this harness. `gpu`, hours. `e13_energy`. C8, C3, and an open question in
    [P2](011-physical.md#p2-energy-per-useful-operation-and-the-headroom-to-physics). Browser: no.
17. **E3, hidden capability.** Public locked weights [@redwood2024mathpwdlock], the auditing-game
    organisms [@aisi2025auditingrepo], and new password-locked, RL-locked and tamper-resistant
    organisms on small open models, built blind to the protocol, on tasks with exact answers
    [@cobbe2021gsm8k; @austin2021mbpp]; benign controls; named budgets including noise injection
    [@tice2025noiserepo]; both rates with one-sided bounds, at least
    [22 organisms](numbers.md#claim-d5-organisms) per class where the miss target is to be shown; a
    sequential test for absence. `gpu`, weeks. `e03_hidden_capability`. C5, and E4(b)'s elicited
    agent. Browser: no.
18. **E10, the exchange rate, with distillation and the generation-verification gap.** On the Pythia
    suite, whose training compute follows from its sizes because every model saw the same data in the
    same order [@biderman2023pythia]: accuracy against samples per task on programs with tests
    [@austin2021mbpp] and on maths by majority vote [@cobbe2021gsm8k]; iso-accuracy contours and the
    span with and without a verifier; a distillation arm; and each size's accuracy at verifying its own
    samples, fitted against compute (the computational chapter's A5 test b, merged because it reuses
    the samples). If Pythia scores too low to fit, a newer family with published token counts replaces
    it, said so. `gpu`, days. `e10_exchange_rate`. C2, C6, C11, C12. Browser: no.
19. **E15, scale-dependence ablations.** An architecture change, an optimiser and a data-mixture
    change, each ablated at three scales on [@moddednanogpt], compute-equivalent gain against scale
    (A3's test b). `gpu`, days. `e15_scale_ablations`. C2, C12. Browser: no.
20. **E14, the distribution tax (P-diloco).** A DiLoCo-style run [@douillard2023diloco] across two
    processes with links throttled to [100 Mbit/s](numbers.md#phys-rahman-bandwidth) and
    [1 Gbit/s](numbers.md#phys-streaming-bw-low), against synchronous training at equal compute, on a
    public text sample named in the file. `gpu`, a day. `e14_diloco_tax`. C8. Browser: no.
21. **E16, verifier substitution.** Five generations of self-training in four arms (replace or
    accumulate, unfiltered or checker-filtered), on generated arithmetic and on programs with tests
    [@austin2021mbpp], at two or three sizes; held-out accuracy and diversity. `gpu`, days.
    `e16_verifier_substitution`. C11, an open question in [A4](012-computational.md#a4-data). Browser:
    no.
22. **E17, transfer from narrow training.** An open base model and its maths-SFT and maths-RL variants
    on held-out non-maths benchmarks, as in [@huan2026mathtransfer], plus our own narrow fine-tune; the
    change per point of in-domain gain on every other cluster. Merges the computational chapter's
    transfer ratio with the cognitive chapter's transfer test. `gpu`, a day or two. `e17_transfer`.
    C11, C12. Browser: no.
23. **E4, loop gain, parts b, d and e.** (b) An elicited open agent improves a small model's recipe
    over at least [5 rounds](numbers.md#claim-d2-rounds) at fixed compute on a one-GPU version of
    the speedrun task [@zhao2025speedrun; @moddednanogpt], at one, two and four times the agent
    budget, at two model scales; its measured round noise decides whether C4 reopens or is cut. (d)
    A logged gate on each input, on and off, with seeded requests a working gate must refuse. (e)
    With and without a narrow optimiser. `gpu`, weeks; needs E3's elicitation and E4(c)'s round
    count. C4, C11, C2. Browser: no.
24. **E7, continual learning's update compute.** SEAL-style self-edits [@zweiger2025seal] on a small
    open model: capability per update operation, forgetting, K_X with an interval, and the update
    compute to cross a capability threshold against a training-compute threshold. `gpu`, days.
    `e07_continual_learning`. C12, an open question in
    [the experiential loop](013-dynamical.md#y1d-the-experiential-loop). Browser: no.
25. **E19, the replication reproduction number.** In an isolated sandbox with no real network or
    payment access, per-stage success of small open models on public replication tasks
    [@black2025replibench; @kinniment2023ara], each gate open and closed; R_Q and its dominant stage.
    `gpu`, days. `e19_replication`. C11, C12. Browser: no.
26. **E20, the F1 decomposition.** On RE-Bench-style tasks with human baselines [@wijk2024rebench], one
    open model at several serving points on a fixed GPU budget: s, n and quality at matched time and
    budget, then whether k parallel copies beat k experts and where returns to k saturate. `gpu`, days.
    `e20_copies_speed_quality`. C10, an open question in
    [F1](014-cognitive.md#f1-kinds-of-advantage-speed-copies-and-quality). Browser: no.

**Phase 3, blocked.** E21's live part (agents entered in fresh contests under human rules, with team
size and AI use recorded) needs organisers' consent. E3, E4(b) and E10 at larger models need more GPU
than the box has; their results here are small-model results and are reported as such.

**Dropped.** A persuasion battery against a professional organisation: it needs human-subjects
approval this project cannot get, and persuasion left the superintelligence line for misuse reporting
in [F2](014-cognitive.md#f2-the-decisive-functions). A measurement of AI's share of chip-design
advances: no data source, as [the hardware loop](013-dynamical.md#y1b-the-hardware-loop) says. The
economic elasticity from filings is an unsourced input to E11, not an experiment.

The first five, E4 (c and a), E1, E5, E24 and E8, have run, and so has E2; the claim sections give
their results; E11 has run on ledger values, and E6, E9, E25, E18, E21, E22 and E23 have run. After
L4, E1, E5, E8 and E24 were corrected, and E4 was rerun. They failed C4's estimator and trigger at
calibrated noise, which downgrades C4 to a measurement design, cut against C1 on covert paths and on
response, left C2's drift rate unidentified and so cut C2(a), measured C3(c), supported C8(a) and
(c), found C6's certificate unable to issue today, found the rate floor in C9 dominated by a
powered-time budget, showed the corrected loop gains leave compute's growth out (E9), corrected C7's
share for drift during a run and cut the compliance-only disclosure candidate (E6), found no
organisation baselines for C10 and t* stopped at each battery's ceiling (E21), cut against C2's
backtest and so downgraded C2 (E18), bounded the supply part of the fleet's growth between
declarations, which with drift between checks C1's and C7's margins must carry (E22), and found that
no version of the durability test can decide (E23). E4(b) decides whether C4 reopens.

## Cut, and why

**Cut or moved to prior work by L1 and L4.** C1, C3, C6, C7 and C9 are now applications of prior
work, kept for their use on AI and credited in their sections. Cut: C1(c), since every response
waits on a political decision; C2(a), the interval tabulated in advance, since E1 cannot identify
the drift rate; C4(c), the trigger, which E4's rerun confirms fails at calibrated noise for the rule
on r and the K rule alike; C8(b), which could not fail. Cut on L3 as well: C2(c), the backtest,
which E18 cuts against. Downgraded on L3: C4 as a whole, to a measurement design, since every
estimator E4 tried fails at calibrated noise; C2 as a whole, to an accounting frame, since its
backtest fails and its gain over one multiplier shows only where it decides nothing; and C10(c), to
"while the battery's baselines last". Each section says what would reopen it. Moved to prior work:
C1(d) (Gan's); C2's verifier-conditioned span and its accounting of distillation at the teacher's
compute, the ceiling once drawn from it being withdrawn (C2.5); C4's upper-bound rule and two
held-out sets; C12(b). E5's support for C3(b) is withdrawn: the proposition is proved, and E5
illustrates it.

**Prior work, so used and credited, not claimed.** The organising idea of safeguards timeliness
[@openai2023governance; @sastry2024compute]; registered chips under expiring licences
[@petrie2025flexheg1; @petrie2025flexheg2]; renewal by k of n licensors [@aarne2025flexheg3]; random
challenge inspections [@scher2025agreement]; rewarded whistleblowing [@dyck2007whistle]; power and heat
signatures [@wasil2024verification]; evaluations on elicited capability against thresholds
[@anthropic2023rsp; @eu2025gpaicode]; bans on closed loops [@miotti2025narrowpath], whose only possible
addition was C4's trigger; the loops as growth laws, runaway against saturation, and coupling itself
[@davidson2026feedback; @besiroglu2024returns]; the criticality metaphor behind the project's name
[@yudkowsky2013iem]; P1 to P3, A1, A3 and A4, each prior work in [the novelty file](03-novelty.md#summary);
and the identity between the line at m = 1 and Gan's prevention condition.

**Too small, framing, or merged.**

- Inspection games with announced random inspections, evasion across channels and renewal end
  effects: an application of a mature theory [@avenhaus2002inspection; @vonstengel2016recursive]. E6
  builds it as a tool.
- Withdrawal notice of at least m * T_r minus the exiting party's breakout time: a small step from C1
  and treaty practice [@scher2025agreement; @eu2005nptwithdrawal]; a corollary in the protocol.
- Copies from held compute and throughput (F1): the formula follows from a known bound [@pope2022],
  forecasts already compute copies from compute [@lifland2025timelines], and nothing triggers on it.
  E12 and E20 still measure it.
- The per-input supply table (O1): assembly, not substance, as its chapter says.
- Ranking supply stages by durability (O3): too few stages for any test to discriminate, which E23
  confirms. The 2022 ranking orders later erosion no better than chance (rho
  [0.28](numbers.md#e23-rho), one-sided p [0.23](numbers.md#e23-p)), and a rank test would need
  [85 stages](numbers.md#e23-n-needed) where the 2022 dataset lists
  [79 inputs](numbers.md#e23-eto-inputs-2022), nested and correlated, so far fewer independent
  stages. No version of the test can decide.
- The discovery rate of covert programmes: an input, not a contribution, arithmetic on a convenience
  sample that its chapter does not claim. It enters C3 through E5 and drives C1 and C8.
- Merged: transfer as a thresholdable quantity (A5) into C11; institutional baselines for the
  decisive functions (F2) into C10; the combined cap leak into C2; denial-induced footprint growth
  (O3) into C8; F3's line, generality across the decisive functions joined to a closed loop, which
  C1's line supersedes as the line, its parts kept in C10 (generality against an institution) and
  C11 (closure, with narrow optimisers inside the loop). The survey's cognition track did not find
  the joined line, and its algorithms and dynamics tracks did not search for it.

**Deferred: not searched or not built, so nothing may be claimed.** The drift trigger for fleets
that keep learning after deployment (E7 measures what it would rest on). The experiential and
acquisitive loops written as growth laws (E7 and E19 measure them). The race model with the regime's
detection time inside it is built in E6 as a tool, not claimed.

**Cut by experiment.** The candidate "compliance-only declarations do not raise risk": in E6,
compliance-only disclosure gave a higher disaster risk than no information in
[100%](numbers.md#e6-o2-compliance-over-none) of its [72 cells](numbers.md#e6-o2-cells), and than
private information alone in [100%](numbers.md#e6-o2-compliance-over-private)
([O2](015-organisational.md#o2-race-dynamics)).

In all, twelve claims are kept, none new and six of them applications of prior work (C1, C3, C6, C7,
C9 and C12); five parts of kept claims are cut, two of them on L3 and one on L4 that L3 confirmed;
C2 and C4 are downgraded on L3, to an accounting frame and a measurement design, and C10(c) is
narrowed; and four more parts moved to prior work; and thirty-three earlier candidates stay cut or
deferred: nineteen as prior work, eleven as too small, framing or merged, one cut by experiment and
two deferred.

## What would make this program fail

Four footings. If one falls, the protocol loses its ground, not just a part. L1 changed whose ideas
two of them are, the line and the detection model being prior work applied here, but not whether the
protocol needs them. The results so far bear on three, and all three bear against.

1. **C1, the line.** If T_r cannot be computed with an interval narrower than the T_b intervals it
   faces, or a T_b the parties compute differently collapses compliance as in [@barrett2012climate],
   there is no agreed boundary between useful AI and weapons-grade, and the protocol falls back on
   fixed compute caps, which are prior work and drift as algorithms improve. The record cuts against
   this footing: of findings made while the party was in its treaty,
   [25%](numbers.md#e24-halt-share-never) were never followed by a halt, so history bounds no response
   time. L4 then found that the protocol's deadlock rule made even licence lapse wait on a quorum's
   finding. Part II now lets a licence lapse unless it is renewed, so a failed check or a withheld
   signature stops a chip by design, at the price of hold-up; a judgement call still adds a decision
   time no record measures. Until a drill measures it, the line has no computable right side for any
   violation that needs judging.
2. **C2, breakout time.** If C* and the efficiency path leave every relevant T_b interval spanning
   the line, the line decides nothing. C* must then be set so low that frontier holdings become
   weapons-grade by default, and the protocol stops keeping useful AI allowed, which fails the
   brief's first addition. The evidence bears against it: one OOM of C*, whose error has no bound,
   moves T_b by [2.3 years](numbers.md#comp-years-per-oom-ho), more than Part II's illustrative line
   of [2.0 years](numbers.md#prot-line-declared), and E1's drift rate runs from
   [2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max) a
   year with the choice of models. E18's backtest then finds the leak coming in jumps that no
   constant rate follows, after a follower's delay the expression lacks.
3. **C3 with C8, covert compute.** At E5's fitted discovery rate, itself an upper bound on a careful
   evader's, undeclared paths need [31 years](numbers.md#e5-td-site-now-years) to
   [32 years](numbers.md#e5-td-pool-years) to reach a [5%](numbers.md#def-prevent-beta) miss, the
   evader's best watched path is missed with probability [91%](numbers.md#e5-pmiss-max-1y) over a
   year, and cloud and distillation are not watched at all. Chip accounting would need the untraced
   pool to shrink [1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold to resolve a
   [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause, where in E8 the compute
   smuggled into one country is already a median
   [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times the floor at BF16, and
   [824](numbers.md#formal-pool-over-floor-bound) times the floor taken as a bound. While the pool
   is open its path fails the line for every party, so the line treats compliant and non-compliant
   parties alike. On today's evidence this footing does not hold, and L4 found nothing in the
   protocol that closes the pool. The protocol binds only parties that choose to declare, until the
   pool shrinks or a channel with a measured rate does far better.
4. **The compute backbone.** Prior work, not a claim here, but every claim assumes it: chips counted at
   birth at a few narrow stages, and the states hosting those stages bound by the same rules. The
   organisational chapter found leaks at the edges and a holder that reversed its own rule within
   months. Without it C1, C2, C7 and C8 have no holdings to compute from. No experiment here tests it.

The other losses are survivable, and two have happened. C4 has failed, as a trigger and as an
estimator at calibrated noise, so self-improvement falls back on the prior-work ban: a declared
closed loop at frontier scale is treated as above the trigger. C5 bounds only non-adaptive hiding,
so against a developer who sees E the protocol places systems by compute, which E1 shows can
misplace one by [2.8 OOM](numbers.md#e1-gpqa-overlap-oom), at a higher cost to useful AI. Without C6
or C7, coupled loops and coalitions are handled by judgement, and C7 offers nothing against a
coalition that includes a major power. Without C9, licences use flexHEG's clocks, whose counter
gives P2 anyway. C10 to C12 are now a definition, framing and a judgement, and the line stands
without them. None of this has been tested against a real adversary. The protocol is a design.
