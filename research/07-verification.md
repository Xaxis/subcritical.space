# Verification

This is the verification record of [the claims file](04-claims.md#summary). Each of its twelve claims,
C1 to C12, must pass six levels: a prior-art search, a proof, experiments on real data, a red team,
Paperwright's desks and a fresh reviewer. A claim that fails a level is cut or downgraded, never
argued around. The record says where each claim stands at each level, and how every attack the red
team made was resolved.

Each level's verdict is recorded as the level gave it in its own report. Each resolution was checked in
the files themselves: the claims file, [the formal file](05-formal.md#summary),
[Part II](06-protocol.md#what-the-protocol-must-do), Part I, the experiments' result files and the
model's current values. A fix that was reported but cannot be seen in the files is recorded as open.
The formal checks were rerun for this record, and all thirteen pass with no counterexample. Four
levels have run, the third in part. Two have not. No claim has passed all six, so none is yet a
contribution.

Nothing here has been tested against a real adversary. The red team was a helper reading the work and
rerunning its scripts, not an opponent with resources and a motive. The protocol is a design.

## How to read the record

The six levels:

1. **L1, prior art**: an independent search by a helper that did not propose the claim
   ([C1 to C6](verification/l1-prior-art-c1-c6.md#summary),
   [C7 to C12](verification/l1-prior-art-c7-c12.md#summary)).
2. **L2, proof**: a formal statement and proof, or the reason the claim is empirical
   ([the formal file](05-formal.md#summary)).
3. **L3, experiments**: working experiments on real data or models, rerunnable from `tools/exp/`.
4. **L4, red team**: a helper whose only job was to break each claim
   ([its report](verification/l4-red-team.md#verdicts)).
5. **L5, Paperwright**: its integrity, reviewer and editor desks, resolved by us.
6. **L6, fresh reviewer**: a reviewer who has not seen the work.

The status words. At L1: **new** (the search did not find it), **extends** (the core is prior work; a
stated, narrow difference was not found), **prior work** (found in substance). "Not found" is a claim
about the search, not about the world. At L2: **proved**, **proved under assumptions**, **corrected**
(false or incomplete as first stated, and restated), **false**, **empirical** (no proof applies; an
experiment decides), **pending**. At L3: **supports**, **mixed**, **against** (the results so far bear
against the claim, a claimed part or its use), **untested** (no experiment that could test it has
run), **pending**. At L4: **survives**, **survives with corrections**, **fails**, **cut in part**. At
L5 and L6 every claim is **pending**.

The standing. A **contribution** has passed all six levels; none has. A **candidate** is alive, with
levels still to run. **Downgraded** means reduced to a definition, framing, a judgement or a design.
An **application** is the use of credited prior work on AI, with any result computed inside that use.
A **cut** claim is gone.

In the attack tables, a resolution is **fixed** (how), **answered** (with what evidence), **conceded**
(the claim narrowed or cut), or **open**.

## The record

Each cell gives the level's verdict and, after it, a few words of why.

| Claim | L1 prior art | L2 proof | L3 experiments | L4 red team | L5 Paperwright | L6 fresh reviewer | Standing |
|---|---|---|---|---|---|---|---|
| [C1, the line](04-claims.md#c1-the-line-tb-m-td-tresp-with-tr-computed-not-chosen) | **prior work**: EASI from 1977, Nitze 1988 | **corrected**: three times; every check passes | **against**: no bounded response time; attempts compound | **cut in part**: (c) cut; (a), (b) corrected | **pending** | **pending** | **application**: (c) cut |
| [C2, breakout time](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case) | **extends**: less than claimed; relabelled a combination | **proved under assumptions**: monotone inputs; termwise bound otherwise | **against**: drift rate not identified; (a) cut | **survives with corrections** | **pending** | **pending** | **candidate**: only (b) and (c), both untested |
| [C3, detection](04-claims.md#c3-detection-as-the-evader-sees-it-the-per-path-evader-minimised-miss) | **prior work**: physical-protection path analysis, interdiction | **corrected**: Theorem 3.2 restricted | **supports**: (c) measured; (b) only illustrated | **survives with corrections** | **pending** | **pending** | **application**: merging rule the only candidate |
| [C4, loop gain](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound) | **extends**: narrowly; round identity and budget ladder | **corrected**: trigger moved from per-round ratio to K | **against**: interval under-covers; trigger fails | **fails**: as a trigger; (c) cut | **pending** | **pending** | **downgraded**: to a measurement design |
| [C5, elicited capability](04-claims.md#c5-elicited-capability-with-measured-miss-and-false-alarm-rates-per-named-budget) | **extends**: diagnostic-test statistics credited | **proved**: textbook | **untested**: E3 not run | **survives with corrections**: non-adaptive hiding only | **pending** | **pending** | **candidate**: non-adaptive hiding only |
| [C6, coupled-gain certificate](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test) | **prior work**: the network small-gain theorem | **proved**: signed case through K+; (c) restates C4 | **against**: no certificate can issue today | **survives with corrections** | **pending** | **pending** | **application**: no certificate while edges unmeasured |
| [C7, coalition share](04-claims.md#c7-the-coalition-share-derived-from-the-response-time) | **prior work**: hardwired-pause threshold; cartel leniency | **corrected**: (b) false as stated; drift, repeated play added | **against**: in-run drift met its refuter; (a) corrected | **survives with corrections**: (b), (c) downgraded | **pending** | **pending** | **application**: of C1 |
| [C8, footprint floor](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool) | **extends**: narrowly; the bound and crossing years | **corrected**: full utilisation, then FP8 | **supports**: (a) and (c), from E8 | **cut in part**: (b) cut | **pending** | **pending** | **candidate**: (b) cut |
| [C9, licence clock](04-claims.md#c9-the-height-clocked-licence-valid-only-once-logged) | **prior work**: part by part; assembly not found | **corrected**: P2 false as stated, now the counter's | **mixed**: supports P2; the rate floor dominated | **survives with corrections**: C9.4 unanswered | **pending** | **pending** | **application**: engineering |
| [C10, matched-budget endpoint](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget) | **extends**: matched time and money remain | **empirical**: t* made well defined | **untested**: no organisation baselines in public data | **survives with corrections**: as a definition only | **pending** | **pending** | **downgraded**: to a definition |
| [C11, closure by input](04-claims.md#c11-closure-judged-input-by-input-with-narrow-optimisers-inside-the-loop) | **extends**: narrowly; task-based automation model | **corrected**: closures add, weighted by shares | **untested**: E4(d), E4(e) not run | **survives with corrections**: as framing until E4(d) | **pending** | **pending** | **downgraded**: to framing until E4(d) |
| [C12, the pathway ranking](04-claims.md#c12-the-pathways-ranked-by-their-effect-on-the-line) | **extends**: as an application of path analysis | **empirical**: a judgement, not a theorem | **mixed**: E4, E5, E1, E11, E9 in part | **survives with corrections**: as a judgement | **pending** | **pending** | **application**: [12](numbers.md#claim-c12-pareto-two) of [21](numbers.md#claim-c12-pairs) pairs fixed |

## C1. The line

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c1)): prior work. Timely detection judged per
  adversary path, with a measured response time and a margin, is physical-protection practice and
  Nitze's standard for effective verification. Only (b), the margin as a multiplicative error budget,
  was not found, and the safety-factor literature where it may live was not opened.
- **L2** ([formal file](05-formal.md#c1-the-line-per-path)): proved under stated assumptions, then
  corrected three times: per path; after the red team, for evaders that move progress between paths
  (Propositions 1.7 and 1.8) and for repeated attempts (Proposition 1.9); and after E6, for the drift
  a run absorbs while it runs (Corollary 1.6a). `c1_margin.py` passes on every correction.
  Propositions 1.7 and 1.8 are not proved for a run whose speed rises with drift.
- **L3** (E5, E24, E6): against (c). E5 puts T_d on undeclared paths at
  [31 years](numbers.md#e5-td-site-now-years) to [32 years](numbers.md#e5-td-pool-years). In E24, of
  [8 findings](numbers.md#e24-halt-findings) made while the party was in its treaty,
  [25%](numbers.md#e24-halt-share-never) were never followed by a halt, so the record has no high
  quantile of response time for the line to use. In E6, repeated attempts compound when caught
  members are re-admitted.
- **L4** ([report](verification/l4-red-team.md#c1)): one fatal attack and five serious ones. (c) is
  cut: under Part II's deadlock rule every response waited on a political decision (C1.5). The per-path
  test admitted a holding that a switching evader broke (C1.1), the guarantee holds per attempt only
  (C1.4), and while the pool is open the line separates no one (C1.2).

Standing: [an application of prior work](04-claims.md#c1-the-line-tb-m-td-tresp-with-tr-computed-not-chosen),
with (c) cut and (b) a small lemma still to face L5 and L6.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C1.1 | Serious | Formal part; claims writer | Fixed: Propositions 1.7 and 1.8 give the line for adaptive evaders, `c1_margin.py` reproduces the red team's instance and the corrected line rejects it, and the claim uses Proposition 1.8's line or the scalar test where progress can move. |
| C1.2 | Serious | Claims writer; protocol writer | Conceded: (a) is restricted to a regime whose pool is closed, and Part II declares the line unmet until then. |
| C1.3 | Serious | Claims writer | Fixed in the statement: T_b is reported conditional on the agreed C*, and m covers estimation error only. |
| C1.4 | Serious | Formal part; claims writer | Fixed in the text: Proposition 1.9 states the guarantee per attempt, and Part II requires halts to return chips and attempts to be bounded; no mechanism yet bounds them, as the formal file says. |
| C1.5 | Fatal for (c) | Claims writer; protocol writer | Conceded: (c) is cut; Part II moved to lapse by default, which leaves a licensor's judgement with no drilled decision time. |
| C1.6 | Minor | E24 | Fixed: E24 leads with the [8 findings](numbers.md#e24-halt-findings) made in treaty, [25%](numbers.md#e24-halt-share-never) never halted, and keeps findings after a withdrawal apart. |
| C1.7 | Serious | Claims writer | Conceded: the statement says m does not cover error a misreporting party introduces; that error is not priced. |

## C2. Breakout time

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c2)): extends prior work, less than the claims
  file said, and relabelled a combination. Every term is prior work; only (b) and (c), both untested,
  could add anything.
- **L2** ([formal file](05-formal.md#c2-breakout-time-is-monotone-in-its-inputs)): proved under the
  assumption that every input but C* raises breakout's left side, when two evaluations give the exact
  interval. Where drift falls fast enough with scale the assumption fails and a termwise bound takes
  over.
- **L3** (E1): against (a), which is cut. The drift rate is not identified: across six samples of the
  same models it runs from [2.6](numbers.md#e1-algo-annual-subset-min) to
  [1,512](numbers.md#e1-algo-annual-subset-max) a year. On the full sample drift falls with scale,
  [-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom), the case where two evaluations fail, and the
  sign is not robust across samples. No interval tabulated in advance can hold on public data. (b) and
  (c) are untested.
- **L4** ([report](verification/l4-red-team.md#c2)): survives with corrections. Seven attacks were
  rated serious, one of them only for Part II; the strongest came from E1's own fit (C2.2, C2.3).

Standing: [a candidate](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)
only through (b) and (c), both untested; (a) is cut, and the expression stays as an accounting frame,
which is prior work.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C2.1 | Serious | Claims writer | Fixed in the statement: the interval covers every input but C*. |
| C2.2 | Serious | E1 | Fixed: E1 reports the interaction and drift per OOM of compute, [-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom), not robust across samples, and the statement adds a termwise bound. |
| C2.3 | Serious | E1; claims writer | Fixed: E1 reports six samples, with [23 models](numbers.md#e1-top25-dropped) of the 25 highest-scoring lacking a compute estimate, and labels the rate not identified; on that result (a) is cut. |
| C2.4 | Serious (interpretation) | Claims writer | Fixed in the claim's results, which call the forecast bound wide and overshooting at the top rather than conservative. |
| C2.5 | Serious | Claims writer | Fixed in the statement: distillation enters at the teacher's level plus an uplift term, which E10 is to measure. |
| C2.6 | Serious for Part II; minor for C2 | Protocol writer | Fixed in Part II: placement by compute now adds E1's [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) overlap, an allowance from one benchmark that Part II still calls a weak fallback. |
| C2.7 | Serious | Claims writer; protocol writer | Conceded: the allowance for undeclared gains is stated unsized, the declared path's T_b is reported conditional on it, and Part II calls a tabulated T_b an upper bound for a party that hides its algorithms. |
| C2.8 | Minor | Claims writer | Open: E15 and E18 have not run. |

## C3. Detection as the evader sees it

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c3)): prior work: physical-protection path
  analysis, network interdiction and safeguards path analysis. The merging rule for dependent channels
  is the only candidate extension, an elementary bound kept only if L4 and L6 find it more than
  textbook.
- **L2** ([formal file](05-formal.md#c3-detection-as-the-evader-sees-it)): (a) and (b) proved under
  independence given the evader's strategy. Theorem 3.2, on common cause, was false for a latent cause
  of several dimensions and now needs a scalar latent or independent components; `c3_evader.py`
  covers vector latents and records the counterexample.
- **L3** (E5): supports (c). The untraced pool's T_d is [299](numbers.md#e5-td-ratio) times the
  declared path's [39.0 days](numbers.md#e5-td-declared-days), which rests on chip sampling, a design
  figure. E5 only illustrates (b), which holds by construction. The fitted discovery rate,
  [0.094/yr](numbers.md#e5-hazard), is an upper bound on a careful evader's.
- **L4** ([report](verification/l4-red-team.md#c3)): survives with corrections, after six serious
  attacks on the statement, the theorem and E5.

Standing: [an application of prior work](04-claims.md#c3-detection-as-the-evader-sees-it-the-per-path-evader-minimised-miss),
with the merging rule as its only candidate extension.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C3.1 | Serious | E5 | Fixed: metering's one-day catch counts once, so chip sampling sets the declared path's T_d at [39.0 days](numbers.md#e5-td-declared-days), and the compounded reading is kept in the details as unsupported. |
| C3.2 | Serious (for L3) | E5 | Fixed: the share that held by construction is removed and its condition asserted as a code check; the memo-style product, 10 to the power [-14](numbers.md#e5-memo-log10-miss-1y), is labelled an illustration, not evidence. |
| C3.3 | Serious | E5 | Fixed: cloud and distillation get no T_d and are missed with certainty, the clock is stated as a programme's start, and under the Weibull fit a first-year discovery has chance [2.6%](numbers.md#e5-weibull-detect-1y). |
| C3.4 | Serious for the theorem; minor for the claim | Formal part | Fixed: Theorem 3.2 needs a scalar latent or independent components, and its check covers vector latents and the counterexample. |
| C3.5 | Serious | E5 | Fixed: the fitted rate is labelled an upper bound on a careful evader's, and the detection times lower bounds; the size of the bias cannot be measured from this record. |
| C3.6 | Minor | E5 | Fixed: diversion detection is merged with imagery and intelligence, which raises one undeclared site's miss to [40%](numbers.md#e5-pmiss-site-merged-1y). |
| C3.7 | Serious | Claims writer | Conceded: the statement says P omits stolen weights, open weights and the switching strategy, and Part II lists them as paths; E5 models none. |
| C3.8 | Minor | Claims writer | Open: the claim's own objection, that a state controls its insiders, is unchanged. |

## C4. The loop-gain estimator

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c4)): extends prior work, narrowly. The
  upper-bound rule is epidemic practice and two held-out sets are econometric practice; what remains is
  the exact round identity as the estimator of K and the budget ladder.
- **L2** ([formal file](05-formal.md#c4-the-loop-gain-estimator)): the identity, lambda from budgets
  and the product bound are proved. The trigger was corrected from the per-round ratio, which tends to 1
  in every subcritical loop, to K, and the old bound on a loop's total gain was withdrawn. Corollary
  4.5a: the K rule fires wherever the rule on r does.
- **L3** (E4, final run; E9): against, for the measurement and the trigger alike. After
  [5 rounds](numbers.md#claim-d2-rounds) at each budget the 90% interval covers r
  [82%](numbers.md#e4-cov-n5) of the time at the corrected median, and
  [77%](numbers.md#e4-cov-n5-xml) with the exact likelihood. On data from the exact law the
  first-order fit returns [0.82](numbers.md#e4-level1-bias) of the true r, on the unsafe side. At the
  corrected median the K rule fires in [88%](numbers.md#e4-k-fa-n5) of runs, and at the 95th
  percentile only [2%](numbers.md#e4-k-fire-gap-n5) more often, within Monte Carlo error. E9 finds that
  no data identifies compute's share of research input, and the speedrun's r is withdrawn as not
  identified.
- **L4** ([report](verification/l4-red-team.md#c4)): fails as a trigger (C4.1), which E4's final run
  confirms for the rule on r and the K rule.

Standing: [downgraded to a measurement design](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound).
(c), the trigger, is cut, and the identity and budget ladder are not a candidate contribution. E4(b),
on real staged rounds, decides whether C4 reopens or is cut.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C4.1 | Serious; cuts (c) | E4; claims writer | Conceded: E4's final run confirms it for both rules at calibrated noise; (c) is cut and C4 downgraded. |
| C4.2 | Serious | E4 | Fixed: E4 models strategic sandbaggers; one withholding a quarter of its gain in the worst pattern makes the rule on r fire late in [96%](numbers.md#e4-late-ub-hide25-fav) of runs at the 95th percentile, even on favourable rounds. |
| C4.3 | Serious | E4 | Answered: E4 tested the two-set remedy under measurement error and it fails at calibrated noise, [0.57](numbers.md#e4-diff-bias-meas1) of the true r on one set and [8.11](numbers.md#e4-diff-bias-meas2) on two; the claim, Part I and Part II say so. |
| C4.4 | Minor | E4; claims writer | Fixed: rounds are counted at each of three budgets, so [5 rounds](numbers.md#claim-d2-rounds) cost [15 staged runs](numbers.md#claim-c4-staged-runs). |
| C4.5 | Serious for the number; minor for the claim | E4 | Fixed: the speedrun's r is withdrawn as not identified and its ledger entry removed; E9 finds the same fault in Stockfish's r. |
| C4.6 | Minor | E4 | Fixed: E4 fits data from the exact law; the first-order fit returns [0.82](numbers.md#e4-level1-bias) of the true r and the exact likelihood [0.77](numbers.md#e4-xml-bias), both on the unsafe side. |
| C4.7 | Minor | Formal part; E4 | Fixed: Corollary 4.5a, and E4 reports the K rule beside the rule on r, false alarms of [88%](numbers.md#e4-k-fa-n5) against [84%](numbers.md#e4-fa-n5); the claim quotes K's price. |
| C4.8 | Serious | Claims writer; protocol writer | Conceded: the statement and Part II say any trigger binds only loops a developer declares. |
| C4.9 | Serious | E4 | Open: E4(b), a staged run at two scales, has not run. |

## C5. Elicited capability

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c5)): extends prior work. The statistics are
  diagnostic-test practice and the counts the zero-failure binomial bound; what remains is both rates
  per named budget, over a defined population of organisms, as the pass-fail rule of a trigger.
- **L2** ([formal file](05-formal.md#c5-miss-and-false-alarm-rates-with-exact-bounds)): proved, all
  textbook: the exact one-sided bound, a sequential test valid under any stopping rule, and a bound on
  untested kinds of organism.
- **L3**: E3 has not run.
- **L4** ([report](verification/l4-red-team.md#c5)): survives with corrections, valid only against
  non-adaptive hiding inside the sampled population. An audit's AUC fell from
  [0.978](numbers.md#def-adaptive-auc-before) to [0.560](numbers.md#def-adaptive-auc-after) against
  adaptive organisms (C5.2), and no organism can hide a capability above expert level (C5.3).

Standing: [a candidate](04-claims.md#c5-elicited-capability-with-measured-miss-and-false-alarm-rates-per-named-budget),
narrowed to non-adaptive hiding.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C5.1 | Serious | Claims writer | Conceded: (a) is stated as valid only against hiding methods inside the sampled population. |
| C5.2 | Serious | Claims writer | Conceded: adaptive organisms, built with E in hand, are measured apart in E3's plan, and the rates are stated not to cover them; E3 has not run. |
| C5.3 | Serious | Claims writer | Conceded: the statement says the rates cannot be measured above expert level. |
| C5.4 | Minor | Claims writer | Fixed in the statement: the count that matters is of independent builds. |
| C5.5 | Serious for Part II; minor for C5 | Protocol writer | Fixed in Part II, as C2.6: placement by compute carries E1's overlap, and the fallback is still called weak. |
| C5.6 | Minor | Claims writer | Open: E3 has not run, so (b) is a prediction. |

## C6. The coupled-gain certificate

- **L1** ([report](verification/l1-prior-art-c1-c6.md#c6)): prior work. The certificate is the linear
  case of the network small-gain theorem, and the targeted version is epidemic control's; the claim's
  own refuter was met. Only the use as a treaty test, and (c) on this program's numbers, remain.
- **L2** ([formal file](05-formal.md#c6-the-coupled-gain-certificate-and-the-runaway-condition)):
  proved. For signed couplings the certificate now works through K+, the matrix with negative entries
  set to zero, after E11 showed that rho(K) is not the runaway condition when couplings can be
  negative: runaway is proved for nonnegative K and ruled out for any signs when rho(K+) < 1. (b)
  needs exhaustive search on random matrices, and (c) restates what C4 says of a fully closed loop.
- **L3** (E11): against issuing a certificate today. Of the [10 entries](numbers.md#e11-entries) in
  Part I's one-party loop graph, [2 entries](numbers.md#e11-entries-measured) have a measured bound and
  [5 entries](numbers.md#e11-entries-unbounded) none. The row-sum test can never issue while compute
  feeds software: no bound on the graph has a largest row sum below
  [2.14](numbers.md#e11-rowsum-floor). On the real graph greedy cutting needed more cuts than the
  smallest set in [0 scenarios](numbers.md#e11-greedy-worse). (c) holds only while the assumed compute
  share of research input stays below [0.689](numbers.md#e11-epsk-flip).
- **L4** ([report](verification/l4-red-team.md#c6)): survives with corrections. With unmeasured,
  self-reported edges the certificate carries no probability (C6.1).

Standing: [an application of prior work](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test);
no certificate issues while any edge is unmeasured, and E11 finds none can issue today.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C6.1 | Serious | Claims writer | Fixed in the statement: no certificate issues while any edge is a stated range or a party's own report; E11 confirms nothing issues under that rule. |
| C6.2 | Serious | Claims writer | Fixed in the statement: rho* is fixed by agreement until its inputs are measured; E11 judges at the most lenient value, so its failures hold for any drift. |
| C6.3 | Serious | Claims writer; protocol writer | Fixed in the statement: ungated edges are listed and bounded, or the certificate says it omits them, as Part II does for weight theft and espionage. |
| C6.4 | Minor | Formal part | Conceded: the formal file calls (c) C4's statement in matrix form; E11 finds it holds only below a compute share of [0.689](numbers.md#e11-epsk-flip), and E9 that the [1.07](numbers.md#dyn-r-lm-hi-corrected) behind it leaves compute's growth out, so (c) holds under that correction or at a low compute share, not in general. |
| C6.5 | Minor | Claims writer | Answered: E11 has run, and finds no certificate can issue today. |

## C7. The coalition share

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c7)): prior work. (a) is the hardwired-pause
  fleet threshold solved for the share, (b)(i) the cartel reporting condition and (b)(ii) the standard
  deterrence condition. Nothing survives independent of C1.
- **L2** ([formal file](05-formal.md#c7-the-coalition-share)): (a) proved, with growth and drift, and
  with the drift a run absorbs while it runs (Proposition 7.1 with Corollary 1.6a). The old (b) was
  false as stated and is corrected with its conditions; Theorem 7.2 adds repeated play.
  `c7_coalition.py` passes on the corrected count, the drift case and re-admission.
- **L3** (E6): against (a) as first stated, and (a) is corrected; (b) is illustrated, not measured.
  The published games reproduce, among them Gan's [32](numbers.md#e6-gan-reproduced) published values.
  A coalition that passes the line computed at launch speed and absorbs drift during its run succeeds
  per attempt with [0.076](numbers.md#e6-staged-pi-line-inrun), above beta of
  [5%](numbers.md#def-prevent-beta), which meets this claim's own staged-accumulation refuter. Over the
  hardwired-pause paper's budget range the overt line binds in only
  [5%](numbers.md#e6-budget-binding-share) of it at the illustrative T_r.
- **L4** ([report](verification/l4-red-team.md#c7)): survives with corrections, (b) and (c)
  downgraded. The protection exists only where rewards exceed beta times a decisive advantage, a region
  the work calls empty (C7.1), and (c) is a property of one assumed budget (C7.3).

Standing: [an application of C1](04-claims.md#c7-the-coalition-share-derived-from-the-response-time),
with (b) empty for decisive-advantage payoffs and s* lowered for in-run drift.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C7.1 | Serious | Claims writer | Conceded: (b) is downgraded and stated empty for decisive-advantage payoffs; E6's sourced payoffs fall inside condition (ii), as illustrations. |
| C7.2 | Serious | Formal part; claims writer | Fixed: the formal file restores the conditions and `c7_coalition.py` counts only where a condition was tested, recording the untested single parties; the claim no longer says none can deviate. |
| C7.3 | Serious | Claims writer; protocol writer | Fixed: (a) gives s* over the breakout budget, Part II writes it as a function of the budget, and E6 finds the overt line binds over only [5%](numbers.md#e6-budget-binding-share) of the paper's own range at the illustrative T_r. |
| C7.4 | Serious | Protocol writer | Fixed: Part II gives the covert path no share until a response there is drilled, and the two covert figures are gone from the ledger. |
| C7.5 | Serious | Claims writer | Conceded: the statement says s counts the accounted fleet, which a covert path does not draw on, and states the fleet's uncertainty. |
| C7.6 | Serious | Claims writer | Conceded: against a coalition that includes a major power the result is empty. |
| C7.7 | Minor | Formal part; claims writer | Answered: E6 and Theorem 7.2 find repeated play keeps (ii) and weakens (i) under re-admission; staged accumulation with in-run drift met the refuter, and (a) now counts that drift (Corollary 1.6a). |

## C8. The footprint floor

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c8)): extends prior work, narrowly. The
  aggregate floor with a time axis and the pool counted against it are prior work; the floor as a
  bound, each channel's margin and crossing year, and the pool's multiple with a measured discovery
  rate remain.
- **L2** ([formal file](05-formal.md#c8-the-footprint-floor-as-a-bound)): proved as a bound once
  corrected twice, for utilisation and then for precision; `c8_floor.py` passes on both. For a
  [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause the bound is
  [800 H100e](numbers.md#formal-floor-bound-1e26-pause).
- **L3** (E8): supports (a) and (c). For chip accounting to resolve such a run the untraced pool must
  shrink [1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold. The pool is
  [340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the floor at BF16 and the compute smuggled
  into one country [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times, each doubled for an
  FP8 run; the statement now sets the bound's [824](numbers.md#formal-pool-over-floor-bound) against
  those ranges.
- **L4** ([report](verification/l4-red-team.md#c8)): survives with corrections, with (b) cut because
  it could not fail (C8.2). The bound had been computed at BF16 while FP8 training at scale is in
  production (C8.1).

Standing: [a candidate](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool),
with (b) cut.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C8.1 | Serious | E8; formal part | Fixed: E8, the model and `c8_floor.py` give the bound at FP8 and full utilisation, [800 H100e](numbers.md#e8-floor-1e26-pause-bound). |
| C8.2 | Serious | Claims writer; E8 | Conceded: (b) is cut, and E8 labels its distributed margins definitional, not evidence. |
| C8.3 | Serious | E8; claims writer | Fixed: the statement calls T an assumption a racing party need not share, and E8 adds a chip-time floor free of T, [1,600 H100e-years](numbers.md#e8-chip-years-1e26-bound). |
| C8.4 | Minor | Claims writer | Fixed in the statement: only chip accounting sees the aggregate of the channels modelled, and traffic and purchases are named as unmodelled aggregate signatures. |
| C8.5 | Minor | E8; formal part | Fixed: E8's bound uses full utilisation, as the formal file's does, and the statement calls the pool an assumption. |

## C9. The height-clocked licence

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c9)): prior work, part by part. The assembly
  for chip licences was not found, so it is an application, claimed as engineering.
- **L2** ([formal file](05-formal.md#c9-the-height-clocked-licence)): P1 and P3 proved under stated
  assumptions. P2 was false under the old rule; corrected, it is the powered-time counter's property,
  not the height clock's. The most-work chain counts (rule W), forged forks are priced under it
  (Lemma 9.2), and P4 needs a party trusted for availability. `c9_clock.py` passes on each.
- **L3** (E25): mixed: it supports P2 and is against the rate floor as designed. A verifier checked
  Bitcoin's real chain of [977,000 headers](numbers.md#e25-headers). P2 holds, and it is the counter's.
  A floor that never stops a compliant chip grants at least the longest honest span, so the best rule
  on the record is a powered-time budget of [1.099](numbers.md#e25-budget-least) times the nominal
  licence time, with a margin, plus the height expiry; a finite floor only adds false stops,
  [17.1%](numbers.md#e25-falsestop-check) of compliant chips at the formal check's settings. Counting
  any valid header's height, a forged fork costing at most
  [50 days](numbers.md#e25-forge-licence-days) of the network's hash rate ends every reachable licence.
  Withheld log leaves are asserted in the harness, not measured, and no hardware prototype exists.
- **L4** ([report](verification/l4-red-team.md#c9)): survives with corrections. One secure element
  carrying every chip (C9.4) is unanswered.

Standing: [an application of prior work](04-claims.md#c9-the-height-clocked-licence-valid-only-once-logged),
claimed as engineering, with the rate floor dominated.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C9.1 | Serious | Formal part | Fixed: the formal file, Part II and the statement give P2 to the powered-time counter and the height clock only an expiry for chips online; E25 confirms it on the real record. |
| C9.2 | Serious | Formal part | Fixed: the formal file (Lemma 9.2), the statement and Part II count the most-work chain; E25 prices the other rule as a cheap off switch, a day early at most [13.1 hours](numbers.md#e25-forge-day-hours) of the network's hash rate. |
| C9.3 | Serious | Formal part; protocol writer | Fixed in design: the log runs as replicas under rival operators, a licence counting only with t signatures (Proposition 9.4); the trust is spread, not removed, E25 asserts rather than measures a withheld leaf, and the design was not searched for prior art. |
| C9.4 | Serious | Claims writer | Open: acknowledged and unanswered; a broken secure element defeats every chip at once. |
| C9.5 | Minor | Formal part; E25 | Answered: on real block intervals the formal check's settings stop [17.1%](numbers.md#e25-falsestop-check) of compliant chips, the floor is dominated by a powered-time budget, and Part II drops it. |

## C10. Superintelligence at matched budget

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c10)): extends prior work. A crossover budget
  between AI and human performance is prior work in two forms; time and money matched together against
  a named organisation, the alpha fraction over decisive clusters and the censored t* remain.
- **L2** ([formal file](05-formal.md#c10-superintelligence-at-matched-budget-what-is-empirical)): a
  definition needs no proof; t* is made well defined as the largest tested crossing.
- **L3** (E1): [5 clusters](numbers.md#e1-clusters-baselined) have some human comparison in public
  data and [3 clusters](numbers.md#e1-clusters-verdict) a bar a model wins or loses. None is an
  organisation at matched budget, so (b) cannot be tested on public data; E21 has not run.
- **L4** ([report](verification/l4-red-team.md#c10)): survives as a definition only. The endpoint
  cannot warn (C10.1).

Standing: [downgraded to a definition](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget).

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C10.1 | Serious | Claims writer | Conceded: C10 is claimed as a definition only, and the protocol acts on the line before it. |
| C10.2 | Serious for the sentence; minor for the conclusion | E1 | Fixed: E1 counts by a search of the archive's columns, [5 clusters](numbers.md#e1-clusters-baselined) with any human comparison and [3 clusters](numbers.md#e1-clusters-verdict) with a won-or-lost bar. |
| C10.3 | Minor | Claims writer | Fixed in the statement: the verdict is stated under both matches, and the grid of budgets is fixed in advance. |
| C10.4 | Minor | Claims writer | Open: listed in the results; the statement is unchanged. |
| C10.5 | Minor | Claims writer | Open: E21 has not run. |

## C11. Closure by input

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c11)): extends prior work, narrowly. The
  combination rule is the task-based automation model, and the narrow-optimiser rule is A Narrow Path's
  ban recast as a count. Two 2026 works found but not opened could decompose closure by input.
- **L2** ([formal file](05-formal.md#c11-closure-by-input-the-combination-rule)): corrected: for the
  loop gain, closures combine as a share-weighted mean, not a product. It flags that D6's closure and
  the closure in the common form are different quantities. (b) is empirical.
- **L3**: E4(d) and E4(e) have not run.
- **L4** ([report](verification/l4-red-team.md#c11)): survives as framing until E4(d). Under the safe
  bound the decomposition reduces to holding every input together, which is prior work (C11.3).

Standing: [downgraded to framing](04-claims.md#c11-closure-judged-input-by-input-with-narrow-optimisers-inside-the-loop)
until E4(d) decides.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C11.1 | Serious | Claims writer | Fixed in the statement: seeded requests must be indistinguishable to whoever runs the pipeline; this is untested, and Part II lists it as a remaining failure. |
| C11.2 | Serious | Claims writer | Conceded: whether D6's share of ungated increments can stand for the elasticity is now part of what C11 must show by experiment. |
| C11.3 | Serious | Claims writer; protocol writer | Conceded: C11 is framing until E4(d), and Part II says closure by input changes no rule until then. |
| C11.4 | Serious | Claims writer; protocol writer | Fixed: the statement and Part II space gates by the agent's own work on horizon-length tasks, not by human hours. |
| C11.5 | Minor | Claims writer | Open: E4(e) has not run. |

## C12. The pathway ranking

- **L1** ([report](verification/l1-prior-art-c7-c12.md#c12)): extends prior work, as an application of
  acquisition path analysis; (b) is prior work. What remains is the ranking itself, a judgement.
  Bostrom's 2014 chapter on paths to superintelligence was not opened.
- **L2** ([formal file](05-formal.md#c12-the-ranking-what-can-be-proved)): a judgement, not a theorem;
  necessity within a horizon follows from the runaway condition.
- **L3**: mixed. E5 keeps undeclared compute's discovery rate far from the memo's placeholder, but that
  refuter needed a [12.8](numbers.md#e5-memo-over-hazard)-fold error to fire. AI-credited records are
  [1.1%](numbers.md#e4-ai-share) of the speedrun's log speedup. E1 leaves the compute share
  unidentified, from [18%](numbers.md#e1-compute-share-subset-min) to
  [63%](numbers.md#e1-compute-share-subset-max) across samples. In E11 no pathway's gate, cut alone,
  issues the certificate with honest bounds ([0 pathways](numbers.md#e11-pathways-alone-honest) do);
  the sets that issue it join several pathways' gates, which fits a top the evidence does not order.
  E9's one frontier case gives a gain at fixed compute of [0.29](numbers.md#e9-openai-k-fixed) but r of
  [0.89](numbers.md#e9-openai-r), near 1; with the share unidentified it does not move the rank.
- **L4** ([report](verification/l4-red-team.md#c12)): survives as a judgement. On L4's three
  criteria [9](numbers.md#claim-c12-pareto-three) of [21](numbers.md#claim-c12-pairs) pairs were fixed,
  none at the top (C12.1); recounted on two criteria, it is
  [12](numbers.md#claim-c12-pareto-two), none ordering the first three places.

Standing: [an application of prior work](04-claims.md#c12-the-pathways-ranked-by-their-effect-on-the-line),
whose order is a judgement with [12](numbers.md#claim-c12-pareto-two) evidence-fixed pairs.

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C12.1 | Serious | Claims writer | Fixed: the statement and the pathways chapter claim only the Pareto-ordered pairs, [12](numbers.md#claim-c12-pareto-two) of [21](numbers.md#claim-c12-pairs) on two criteria, from grades kept as inputs so a different reading reruns the count. |
| C12.2 | Serious | Claims writer | Fixed: the cost of a limit sets the response, not the rank, and the pairs are recounted on effect and visibility alone. |
| C12.3 | Serious | Claims writer | Conceded: the statement says the tie at the top joins an effect on T_r with an effect on T_b on no common scale. |
| C12.4 | Minor | Claims writer | Conceded: the results say the refuter needed a [12.8](numbers.md#e5-memo-over-hazard)-fold error to fire. |
| C12.5 | Minor | Claims writer; protocol writer | Fixed: the claim and Part II cite E1's range across samples, [18%](numbers.md#e1-compute-share-subset-min) to [63%](numbers.md#e1-compute-share-subset-max), as unsettled. |
| C12.6 | Minor | Claims writer | Conceded: C12(b) moved to prior work, and necessity cannot be shown before D1 exists. |

## The protocol

The red team made nine attacks on [Part II](06-protocol.md#what-the-protocol-must-do) itself
([the report](verification/l4-red-team.md#the-protocol)). Their resolutions, as Part II now reads:

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| P1 | Fatal for the second footing as stated | Protocol writer | Fixed in part: licences now [lapse unless renewed on evidence](06-protocol.md#lapse-by-default-and-its-price), so a failed check or withheld signature stops a chip within one period by design; a licensor's judgement still takes a decision time no record measures, and the price is hold-up. |
| P2 | Serious | Protocol writer | Fixed: the section now says the design trusts at least three parties, and [a table](06-protocol.md#verification-and-whom-it-trusts) lists each trusted party with what a breach breaks. |
| P3 | Serious | Protocol writer | Conceded: [Part II](06-protocol.md#undeclared-compute-and-secret-programmes) says nothing in it closes the pool today and lists steps to shrink it, which E22 is to test; open. |
| P4 | Serious | Protocol writer | Conceded: Part II declares the line unmet until the pool closes and classifies on declared paths as an interim rule, which it says is no prevention guarantee. |
| P5 | Serious | Protocol writer | Conceded: the trust table names one secure element behind licences, attestation, location and the counter, with evaluators' enclaves on the same hardware; only inspection and re-execution do not rest on it. |
| P6 | Minor | Protocol writer | Conceded: Part II now has no loop-gain trigger; the rule is the prior-work ban until E4(b) finds one. |
| P7 | Minor | Protocol writer | Fixed: the cost of L2 now reads low for makers and high for host states, which have reversed such rules within months. |
| P8 | Minor | Protocol writer | Fixed: every number in Part II is a ledger link, and `python3 tools/check.py` reports that each shows the model's value. |
| P9 | Serious | Protocol writer | Conceded: [Part II](06-protocol.md#where-it-fails) says it offers a major power with its own chip chain deterrence only, so it prevents breakouts by the parties least able to make them; open. |

Attacks on claims that the red team aimed at Part II's text, and how Part II now reads:

| Attack | Severity | Owner | Resolution |
|---|---|---|---|
| C1.2 | Serious | Protocol writer | Conceded: Part II declares the line unmet while the pool is open. |
| C1.3 | Serious | Protocol writer | Fixed: every table is conditional on the agreed C*, and [the margin](06-protocol.md#the-margin) is stated not to cover it. |
| C1.5 | Fatal for C1(c) | Protocol writer | Fixed in part: lapse by default replaces the deadlock rule, and [the illustrative T_r](06-protocol.md#response-time-from-the-regimes-own-channels-and-drills) of [1.0 years](numbers.md#prot-tr-declared) is limited to violations the renewal rule checks mechanically; judgement adds an unmeasured decision time. |
| C1.7 | Serious | Protocol writer | Conceded: the margin is stated not to cover error a party makes on purpose. |
| C2.3 | Serious | Protocol writer | Conceded: [the tables](06-protocol.md#breakout-time-read-from-tables-agreed-in-advance) name their population and take the fast end, but gains a party does not declare are unsized, so a tabulated T_b is an upper bound for a party that hides them. |
| C2.6 | Serious for Part II | Protocol writer | Fixed: placement by compute adds E1's [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) overlap, and the fallback is still called weak. |
| C3.1 | Serious | Protocol writer | Fixed: Part II gives the declared path [39.0 days](numbers.md#e5-td-declared-days), resting on chip sampling, with metering's day counted once. |
| C3.3 | Serious | Protocol writer | Fixed: cloud and distillation have no T_d, and Part II says the Weibull fit finds less than the constant rate in the short windows a breakout needs. |
| C3.7 | Serious | Protocol writer | Fixed in the text: [the path table](06-protocol.md#channels-trust-anchors-and-the-evaders-best-path) lists open weights, stolen weights and training on one path to finish on another; none is modelled. |
| C4.1 | Serious | Protocol writer | Fixed: [Part II](06-protocol.md#the-loop-gain-trigger-and-which-bound-binds) reports that E4 found the trigger fails, drops it, and keeps the prior-work ban. |
| C4.3 | Serious | Protocol writer | Fixed: Part II says the two-set remedy fails at calibrated noise. |
| C5.5 | Serious for Part II | Protocol writer | Fixed: as C2.6. |
| C6.3 | Serious | Protocol writer | Fixed: [the edges section](06-protocol.md#the-edges-between-loops) says the certificate omits weight theft and espionage. |
| C7.3 | Serious | Protocol writer | Fixed: [the coalition share](06-protocol.md#the-coalition-share-derived-from-the-response-time) is written as a function of the budget, reaching 1 at a budget of [0.26](numbers.md#prot-coalition-budget-unity) times the published one at fixed algorithms. |
| C7.4 | Serious | Protocol writer | Fixed: the covert path has no share until a response is drilled. |
| C9.3 | Serious | Protocol writer | Fixed in design: log replicas under rival operators; not searched for prior art. |
| C11.3 | Serious | Protocol writer | Conceded: closure by input changes no rule until E4(d). |
| C11.4 | Serious | Protocol writer | Fixed: [gates](06-protocol.md#l3-closed-research-loops-above-a-loop-gain-bound) count the agent's completed horizon-length tasks, not hours. |
| C12.5 | Minor | Protocol writer | Fixed: Part II cites E1's range across samples beside the frontier figure. |

## Found since the red team

These findings came from the experiments and proofs that ran after level 4. None is an attack, and
none is a claim; each changed a claim, Part I or Part II.

- **Drift during a run (Corollary 1.6a, found by E6).** A line computed at launch speed, with
  algorithms fixed when a run starts, does not cover a run that absorbs drift as it goes. It must rise
  by a factor of [3.2](numbers.md#formal-inrun-line-factor) at the central drift rate and
  [10.6](numbers.md#formal-inrun-line-factor-high) at the high end, both upper bounds, at the
  protocol's margin and declared T_r ([formal file](05-formal.md#c1-the-line-per-path)). It enters C1's
  statement, C7's share (Proposition 7.1) and Part II's tables.
- **Repeated play (after Theorem 7.2).** Condition (ii) survives whether caught members are re-admitted
  or expelled; under re-admission, condition (i) needs a reward up to 1/beta times the one-shot one,
  rising towards the whole prize as the discount factor nears 1
  ([formal file](05-formal.md#c7-the-coalition-share)). Discount factors and membership values are
  measured for no party.
- **Compliance-only disclosure is cut (E6).** Revealing only that each party is below the line gave a
  higher disaster risk than no information in [100%](numbers.md#e6-o2-compliance-over-none) of
  [72 cells](numbers.md#e6-o2-cells) of race models, and than private information in
  [100%](numbers.md#e6-o2-compliance-over-private). The candidate is cut in
  [O2](015-organisational.md#o2-race-dynamics) and in
  [Part II](06-protocol.md#sealed-declarations-and-licences-valid-only-once-logged), which now
  discloses no more than the regime needs.
- **Compute's share of research input is not identified (E9).** No data identifies it, and Part I's
  loop gains of [0.63](numbers.md#dyn-r-lm-corrected) and [1.07](numbers.md#dyn-r-lm-hi-corrected)
  leave compute's own growth out. Counting it, the language-model gain at fixed compute at a share of
  [0.67](numbers.md#dyn-research-compute-share) is [0.25](numbers.md#e9-lm-k-fixed)
  ([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile), above 1 only for shares below about
  [0.26](numbers.md#e9-lm-share-crit). This bears on C4, C6(c), D2 and the dynamical chapter's values.
- **The rate floor is dominated (E25).** On Bitcoin's real record a powered-time budget at the longest
  honest span, with a margin, does everything a floor that never stops a compliant chip does, and any
  finite floor adds only false stops. Part II drops the floor.
- **Signed couplings (E11).** For couplings that can be negative, rho(K) is not the runaway condition:
  a signed variant of the real software and compute block, with rho(K) of
  [1.25](numbers.md#e11-signed-rho), grows only logarithmically. The formal file now certifies
  through K+ ([formal file](05-formal.md#c6-the-coupled-gain-certificate-and-the-runaway-condition)).

## Open for the next levels

- **A published result our reimplementation does not reproduce.** In E6, Emery-Xu, Park and Trager's
  Proposition 2 is not a best response in our reimplementation of their model: a deviation gains up to
  [0.017](numbers.md#e6-ex-prop2-br-gain-max). This is our reimplementation's finding about published
  work, not a settled fact. An independent check, at level 4 or level 6, must confirm or overturn it
  before anything rests on it; O2 and Part II already say nothing does.
- **A published estimate E9 did not reproduce.** Of [12](numbers.md#e9-recomputed) published
  estimates E9 recomputed on their authors' own inputs, [11](numbers.md#e9-reproduced) reproduced; the
  growth of OpenAI's compute in Ho and Whitfill's appendix did not. The same independent check
  applies before E9's OpenAI figures are leaned on.
- **Proofs with a stated gap.** Propositions 1.7 and 1.8 are not proved for a run whose speed rises
  with drift, and nothing yet bounds the number of attempts
  ([formal file](05-formal.md#what-the-proofs-do-not-establish)).
- **Attacks still open**: C3.8, C4.9, C9.4 and C10.4, besides those that wait on experiments (C2.8,
  C5.6, C10.5, C11.5).

## What has not been done

- **L5 is blocked.** Paperwright is not yet connected, so no claim has been through its integrity,
  reviewer or editor desks.
- **L6 has not run.** No reviewer who has not seen the work has read it.
- **Experiments not yet run**, by claim:
  - C1: E18 and C2's other experiments for T_b, and a drill of the licensors' decision time, which no
    experiment yet plans.
  - C2: E15, E10 with its distillation arm, E18, E22 and E4(b).
  - C3: E13; nothing yet gives cloud or distillation a channel.
  - C4: E4(b), which decides whether C4 reopens or is cut.
  - C5: E3.
  - C6: E11 again, with the diagonal from E9, the compute edge from E10 and a cross-party edge, which
    E6 could not identify; the economic elasticity has no source.
  - C7: E22, and payoffs measured rather than illustrated, which no experiment yet plans.
  - C8: E14, E13 and E22.
  - C9: the header check on a constrained secure element, and withheld log leaves measured, not
    asserted; no hardware prototype exists.
  - C10: E21.
  - C11: E4(d), E4(e), E16, E17 and E19.
  - C12: E15, E18, E10's distillation arm, E19 and E7.
- **Searches not yet run.** The safety-factor literature, the likeliest earlier home of C1(b);
  Bostrom's 2014 chapter on paths (C12); two 2026 works that could decompose closure by input (C11),
  which must be opened before L5; hardware-wallet and trusted-time designs that check headers offline
  (C9); and six pieces of Part II never searched: the two-stage loop-gain rule, the renewal evidence
  list with periods set per holding, the log replicas, the mixed inspection beacon, distillation keyed
  to the teacher and the drift trigger for continual learning.
- **Files not yet aligned.** The claims file's L2 lines for C3, C8 and C9 still say the formal check
  run is pending, and C1's L3 plan still lists E6 as to come; both have run. The formal file's summary
  still tells C4 to measure each round on two held-out sets, which E4 found fails at calibrated noise.
  C9's statement still writes P2 with the floor's bound, (L + s) / rho_min, and its L2 line says
  P2 holds with the rate floor, while E25 found the floor dominated and Part II dropped it; the
  statement notes that a plain budget is better but has not been restated. The claims file reads C12's level 1 as an application; the report's verdict is "extends
  prior work, as an application".

None of this has been tested against a real adversary. The protocol is a design.
