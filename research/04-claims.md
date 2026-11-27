# Claims: what this work may contribute, each with its test

This file states what Subcritical may claim as its own, precisely enough that each claim could be
shown false, and plans the test each must pass. It establishes nothing: every claim has the status
"candidate". The repo's rule is that a claimed contribution passes six levels or is cut:

1. **L1**, an independent prior-art search by a helper that did not propose the claim;
2. **L2**, a formal statement and proof, or the reason the claim is empirical and needs none;
3. **L3**, working experiments on real data or models, rerunnable from `tools/exp/`;
4. **L4**, a red team that only tries to break it;
5. **L5**, Paperwright's integrity, reviewer and editor desks, resolved by us;
6. **L6**, a fresh reviewer who has not seen the work.

Results go in `07-verification.md` (not yet written), one row per claim per level. A claim that fails
a level is cut or downgraded, never argued around.

The independent search in [the novelty file](03-novelty.md#what-this-leaves-as-our-contribution)
found none of the memo's ideas new. It left narrow extensions and combinations, and each chapter of
Part I lists what it calls "possibly ours" or "extends prior work". This file gathers them, merges
near-duplicates, keeps twelve and cuts the rest with reasons. Two labels are used: **extends prior
work** (the core is prior work; a stated difference was not found) and **combination of prior work**
(each part is known; the combination was not found). "Not found" is a claim about our search, not
about the world, and L1 may lower any label. The few numbers Part I did not compute are derived in
`model/parts/040_claims.py` from targets in `data/inputs/040-claims.toml`.

## Summary

| Id | The claim in one line | Label | Closest prior work | Experiments | Status |
|---|---|---|---|---|---|
| C1 | The line between useful AI and weapons-grade is T_b < m * (T_d + T_resp), with the response time computed from the regime's own channels and drills | extends prior work | [@barnett2025governance]; [@gan2026clock]; [@fithian2026hardwired] | E5, E24, E6, E18 | candidate |
| C2 | Breakout time from verified holdings, with a loop-gain term, scale-dependent efficiency, a verifier-conditioned inference span and an interval; the cap leak is its fixed-compute case | extends prior work | [@fithian2026hardwired]; [@gan2026clock]; [@heim2024thresholds]; [@villalobos2023tradeoff] | E1, E10, E15, E18, E22, E4 | candidate |
| C3 | The chance a breakout is missed is a maximum over the evader's paths, with correlated channels merged, over each path's own breakout time | extends prior work | [@baker2025verifying]; [@allen-2015-llnl]; [@gan2026clock] | E5, E8, E13 | candidate |
| C4 | A loop-gain estimator staged at fixed inputs, whose interval achieves its coverage and whose upper bound binds as the trigger | extends prior work | [@cunningham2026rsi]; [@burtsev2026criticality]; [@metr-anthropic-acceleration-2026] | E4, E9 | candidate |
| C5 | Elicited capability judged by a measured miss rate and false-alarm rate per named budget, over hardened and adaptive organisms, within a stated range | extends prior work | [@taylor2025auditinggames]; [@greenblatt2024password]; [@anthropic2023rsp] | E3 | candidate |
| C6 | A treaty test certifying the coupled gain subcritical from entrywise upper bounds, rho(K) <= rho(U) <= max row sum of U, each edge gated and verified | combination of prior work | [@davidson2026feedback]; [@burtsev2026criticality] | E11, E9, E6 | candidate |
| C7 | The largest coalition share, derived from the response time, with a coalition-proofness condition | extends prior work | [@fithian2026hardwired]; [@bernheim1987coalition]; [@nordhaus2015climate] | E6, E22 | candidate |
| C8 | The aggregate footprint floor with a time axis, a margin per channel, and the untraced pool counted as a covert reserve | combination of prior work | [@koopmanschap2026gpu]; [@rahman2026]; [@scher2025] | E8, E14, E13, E22 | candidate |
| C9 | Chip licences that end at a Bitcoin block height, are fresh by a block hash, and are valid only once logged with the sealed declarations | combination of prior work | [@petrie2025flexheg2]; [@petrie2024offline]; [@laurie2013ct]; [@todd2016opentimestamps] | E25 | candidate |
| C10 | Superintelligence against a named institution at matched time and budget on a regime-held battery, tracked by the crossover budget t* | extends prior work | [@genewein2026agiasi]; [@ngo2023tagi]; [@wijk2024rebench] | E21, E2, E1 | candidate |
| C11 | Closure judged input by input against verifiable gates, with narrow optimisers counted inside the loop they feed | extends prior work | [@burtsev2026criticality]; [@chen2026rsisurvey]; [@miotti2025narrowpath] | E4, E16, E17, E19 | candidate |
| C12 | Seven pathways ranked by their effect on T_b or T_r, visibility and cost of a limit; self-improvement and undeclared compute tie first | extends prior work | [@allen-2015-llnl]; [@davidson2025three]; [@genewein2026agiasi] | E4, E5, E1, E15, E10, E19, E7, E2 | candidate |

C1 is the line, C2 and C3 its two sides, and C8 says which channel sees covert compute; C4, C5 and
C11 feed C2; C6 and C7 extend the line to coupled loops and coalitions; C9 is the regime's record; C10
is the endpoint; C12 decides what is restricted.

## C1. The line: T_b < m * (T_d + T_resp), with T_r computed, not chosen

**The claim.** A holding H (chips, weights, data, research labour, and every path its holder can
use) is weapons-grade if and only if T_b(H) < m * T_r, with T_r = T_d(beta) + T_resp, all in years.
T_b is C2's breakout time. T_d(beta) is the time by which the regime's channels detect the holder's
best path with probability at least 1 - beta, from C3. T_resp is the drilled time from a confirmed
finding to an effective halt. m >= 1 is a stated margin. Claimed: (a) the inequality as the
definition of the line for systems and holdings, with everything outside it free to keep improving
through metered, human-held gates; (b) the role of m as a proposition: if the estimates of T_b and
T_r err in the unsafe direction by factors e_b and e_r, an admitted holding is still stopped with
probability at least 1 - beta whenever e_b * e_r <= m, under Gan's Poisson model [@gan2026clock];
(c) T_r computed per path from sourced channel rates and drilled latencies; (d) a prevention line
near the threshold, deterrence far from it. Not claimed: that the line with m = 1 is Gan's
prevention condition, which follows from his formula.

**What it rests on.** [D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr). The memo's placeholder
channel needs [2.5 yr](numbers.md#def-placeholder-detect-time) to bring the miss chance to
[5%](numbers.md#def-prevent-beta); at the historical discovery rate of undeclared programmes,
[0.08/yr](numbers.md#org-covert-hazard), it takes [37 years](numbers.md#path-covert-td-prevent), before any
response ([O4](015-organisational.md#o4-covert-supply-how-secret-programmes-were-run-and-found)).
Prevention costs [7.8](numbers.md#def-gan-prevent-multiple) times the monitoring deterrence needs in
Gan's calibration. The nuclear margin never exceeds [1.00](numbers.md#def-iaea-m-irr-high) and times
detection only [@iaea-glossary-2001; @cochran-2005].

**Prior work, and what differs.** [@barnett2025governance] states the inequality in words;
[@gan2026clock] formalises it with detection and implementation delays; [@miotti2025narrowpath] sizes
thresholds for "ample time to intervene"; [@fithian2026hardwired] derives fleets from a horizon chosen
by judgement. What differs is (a) to (c): the inequality as the boundary of useful AI, an explicit
margin with an error budget, and T_r measured rather than chosen.

**What would refute it.** L1 finds (a), (b) or (c). L3 cannot compute T_r for any path with an
interval narrower than the T_b intervals it faces, so the line decides nothing. E6 finds compliance
collapses once T_b is drawn from its interval, as a disputed threshold did in [@barrett2012climate].

**L1.** "Breakout time" with "response time" or "margin" in treaty design; "timeliness" with
"conversion time" and "safety factor"; forward citations of [@gan2026clock], [@barnett2025governance]
and [@fithian2026hardwired]; the RAND perspective that blocked automated access in the survey. Fields:
safeguards, arms control, compute governance, outbreak response (detection delay against doubling
time).

**L2.** Prove (b) under its assumptions (Poisson detection on the best path, fixed T_resp, one-sided
multiplicative errors), and extend to a hazard h(t): the integral of h_min from 0 to T_b - T_resp must
reach ln(1/beta). State the Weibull case, since a programme may be hardest to see early. In
`05-formal.md`.

**L3.** E5 (T_d per path), E24 (T_resp as a distribution), C2's experiments (T_b). Output: T_b / T_r
by holding class with intervals, and the share of classes the line decides.

**L4.** Strongest objection: T_b rests on C*, which no one can measure, so the line is a disputed
threshold. Second: for undeclared compute T_d is decades, so the line reduces to "hold no covert
reserve", the compute backbone restated. Third: T_b is gamed by hiding algorithms, T_r by degrading
channels. The red team plays a defecting state and a party that misreports.

**L5, L6.** Pending.

## C2. Breakout time from verified holdings, and the cap leak as its fixed-compute case

**The claim.** For holdings H and an agreed, conservative C* (log10 effective compute), T_b(H) is the
minimum over paths p of the earliest t with log10 C_p(t) + J + S_v + A(t) >= log10 C*. C_p(t) is
physical compute accumulated on p (chip-time at a reference precision times utilisation, including
C8's untraced pool); J the one-off post-training jump; S_v the inference span, bounded, larger where a
cheap verifier exists, paid in compute a chip count sees; A(t) algorithmic drift at a rate a(C) that
depends on scale and rises with research labour, human and AI, through C4's gain. Distillation closes
the gap to a teacher the holder can query and adds nothing beyond it. At fixed physical compute this
is the cap's leak time, t = (H - J) / log10 g. Claimed: (a) the expression, with an interval,
tabulated in advance by holding class; (b) for at least one holding class the protocol cares about,
it differs from a single-multiplier T_b by more than either's interval; (c) backtested at past dates,
it predicts the open-closed lag of [4 months](numbers.md#comp-open-closed-lag) within its interval.

**What it rests on.** [D3](01-anatomy.md#d3-breakout-time) and
[the combined leak](012-computational.md#the-combined-leak-of-a-training-cap). With an example
headroom of [3 OOM](numbers.md#comp-example-headroom-oom), a capped party closes it in
[4.0 years](numbers.md#comp-leak-years-ho) at Ho et al.'s rate, [2.2 years](numbers.md#comp-leak-years-rosetta)
at the Rosetta rate and no sooner than [9.3 years](numbers.md#comp-leak-years-small) at the
small-compute bound; a cheap verifier leaves [0 OOM](numbers.md#comp-leak-left-verifier). Of a
[22,000](numbers.md#def-gundlach-claimed)-fold efficiency gain, less than
[100](numbers.md#def-gundlach-low-compute-max)-fold reproduces at low compute [@gundlach2025origin].
The model reproduces the hardwired-pause threshold of [180 million H100e](numbers.md#def-hwp-fleet-check).

**Prior work, and what differs.** [@fithian2026hardwired] derives fleets from budget, overhead,
utilisation, horizon and a fixed efficiency rate; [@gan2026clock] computes catch-up from a calibrated
model; the leak's routes are known [@villalobos2023tradeoff; @ord2025govaireport; @heim2024thresholds;
@davidson2023enhancements; @barnett2026closingwindow]. What differs: a measured loop-gain term, a
scale-dependent rate, the verifier-conditioned span in the same expression, distillation as a gated
ceiling, the interval, and the split between leaks a chip count sees and leaks it does not.

**What would refute it.** (b) fails: no gain over one multiplier, cut to prior work. (c) fails: the
model should not set a treaty schedule, by the computational chapter's own test. E1 and E15 find no
scale trend: the scale term is cut.

**L1.** Breakout time with "algorithmic progress" and "scale-dependent"; compute thresholds with
"inference scaling" and "verifier"; forward citations of [@fithian2026hardwired],
[@heim2024thresholds], [@ord2025govaireport] and [@gundlach2025origin]. Fields: compute governance, AI
forecasting, economics of research.

**L2.** Mostly empirical. Formal part: T_b is monotone in each input, so input intervals give T_b's
interval at the corners; the minimum over paths matches C3's evader.

**L3.** E1, E15, E10, E18, E22, E4.

**L4.** Strongest objection: C* is unknowable, so T_b inherits an arbitrary interval however well
efficiency is measured. Second: scale dependence is measured at small scale and at the frontier, not
where caps would sit, and stacking of techniques is unmeasured. Third: algorithms are not verifiable,
so a party hiding its progress has a shorter T_b than the table says.

**L5, L6.** Pending.

## C3. Detection as the evader sees it: the per-path, evader-minimised miss

**The claim.** Let P be the paths open to a party (declared fleet, undeclared site with smuggled
chips, cloud split across providers, distillation from others' outputs) and C(p) the channels
watching path p. The chance a breakout succeeds is P_miss = max over p of Pr[no channel in C(p)
detects before T_b(p) - T_resp]; with channels at rates lambda_c(p), independent given the path, that
is the maximum of exp(-sum of lambda_c(p) * (T_b(p) - T_resp)). Channels resting on one trust anchor,
or fed by one source of tips, merge into one with the larger rate. Claimed: (a) the model with sourced
rates and the merging rule; (b) a proposition: the memo's product of channel misses equals P_miss only
if every channel watches every path and channels are independent, and otherwise understates it;
(c) on today's sourced rates, the undeclared path's T_d exceeds the declared path's by a large factor,
so the regime's detection time is set by the untraced pool (C8).

**What it rests on.** [The novelty file's multi-channel section](03-novelty.md#the-multi-channel-detection-guarantee-over-breakout-time)
and the channel limits in [P4](011-physical.md#p4-the-footprint-and-its-floor). The memo's placeholder
rate, [1.2/yr](numbers.md#org-memo-detect-rate), is about [15](numbers.md#org-memo-to-history) times
the historical discovery rate. Epoch's smuggling model assumes [25%](numbers.md#org-diversion-detect)
of diversions are detected. Metering catches [96%](numbers.md#phys-meter-detect) of undisguised
training at [1%](numbers.md#phys-meter-false-alarm) false alarms, on simulated power
[@kimpson2026dcpower]. No challenge inspection has been requested
([0 requests](numbers.md#org-cwc-ci-requests)) [@opcw-ec109-dg22]. A mature many-channel system
caught about [31%](numbers.md#org-fraud-detect) of frauds [@dyck2017pervasive].

**Prior work, and what differs.** [@baker2025verifying]: a regime detects about as well as its weakest
subgoal; correlation flagged, not modelled. [@gan2026clock] uses one aggregate rate,
[@allison2025nuclear] a Poisson risk over a horizon, [@shavit2023chinchilla] one channel in closed
form, [@wasil2024verification] a "Swiss cheese" model in words. Acquisition path analysis already
computes detection per path in safeguards [@allen-2015-llnl; @iaea-glossary-2022] and is the closest
work. What differs is narrow: AI paths and channels with sourced rates, the merging rule, and each
path's own breakout time instead of a fixed window.

**What would refute it.** L1 finds path analysis applied to AI compute with per-path breakout times.
(b) fails. L3 finds T_d's interval spanning every T_b of interest, which makes the model a framework,
not a result. L4 finds a path outside P with low detection.

**L1.** "Acquisition path analysis" with AI or compute; "detection probability" with "multiple
safeguards" and "correlated"; forward citations of [@baker2025verifying] and
[@wasil2024verification]. Fields: the IAEA's state-level concept, common-cause failure in reliability
engineering, search theory, fraud detection.

**L2.** (b): the channels on any path are a subset of all channels, so the full product is at most the
best path's miss, with equality only in the stated case. The merging rule is conservative: for
positively dependent channels the combined rate lies between the larger rate and the sum.

**L3.** E5 (Monte Carlo and the discovery-rate survival fit), E8 (facility margins), E13 (a measured
rate for the metering channel against disguises).

**L4.** Strongest objection: no AI channel has a measured rate against a real evader; the rates are
transfers from simulation and other domains, and an adaptive evader moves them. Second: insiders, the
channel that worked historically, can be compartmentalised and coerced by a state [@hoffman-2009].
Third: splitting a workload below every threshold [@heim2024cloud] may be a path P misses.

**L5, L6.** Pending.

## C4. A loop-gain estimator at fixed inputs, binding at its confidence bound

**The claim.** Capability is measured on a log compute-equivalent axis; a round is one research cycle
at a fixed budget (experiment compute, data, wall-clock); the researcher is a fixed, elicited agent,
so a staged run measures returns to AI research labour, not closure. In
[the common form](013-dynamical.md#the-common-form-a-growth-law-and-its-returns) the gain per round
satisfies ln(Delta_(k+1) / Delta_k) = -beta * Delta_k, so a regression estimates beta; repeating at
one, two and four times the agent budget estimates lambda; r = lambda / beta. The loop gain is the
product of separately measured factors (this return, the ladder term epsilon_R,C and the scaling term
epsilon_C,A [@cunningham2026rsi]) with one combined interval. Claimed: (a) the interval achieves its
nominal [90%](numbers.md#claim-confidence) coverage in simulation over plausible parameters within
[5 rounds](numbers.md#claim-d2-rounds), or the claim states how many it needs; (b) on real runs the
interval puts r on one side of 1, or, as Part I already says, D2 cannot trigger and the claim is cut;
(c) the trigger binds on the **upper** bound: closed-loop research on a declared frontier-scale system
is restricted while the upper bound on g exceeds a margin g* below 1, and the restriction lifts once
more rounds bring the bound under g*.

**Which bound, and what it costs.** Part I disagrees with itself. [D2](01-anatomy.md#d2-loop-gain)
binds on the lower confidence bound; [the software loop](013-dynamical.md#y1a-the-software-loop)
fires when the upper bound crosses a margin below 1; [the pathways chapter](02-pathways.md#what-the-ranking-means-for-the-protocol)
names the disagreement and argues for the upper bound. This claim uses the upper bound, for three
reasons. Crossing 1 cannot be undone and C1 is a prevention line, so the trigger must fire when the
gain could plausibly exceed 1, not once it probably does. A sandbagging agent biases g low, which
delays a lower-bound trigger more than an upper-bound one. And the width is the risk: at the corrected
median, [0.63](numbers.md#dyn-r-lm-corrected), the loop's total gain is bounded at
[2.7](numbers.md#path-rsi-multiplier-median) times its first round's, while at the 95th percentile,
[1.07](numbers.md#dyn-r-lm-hi-corrected), it is not bounded at all. The cost is false alarms: when the
true gain is below g*, a wide interval still puts the upper bound above it, so the rule restricts
research that is in fact subcritical, and on today's historical numbers it would already fire. That
cost falls only as rounds narrow the interval. It is limited in scope, since it covers closed-loop
training research on declared frontier-scale systems and not AI-assisted research in general (a cost
the pathways chapter rates low to moderate), and it lifts when the bound falls. E4(c) reports the
false-alarm rate against the true gain and the number of rounds, at the corrected median, which sits
[0.37](numbers.md#dyn-software-headroom) below 1, and at g*, and states how many rounds bring it below
a stated target. The lower-bound rule's error is the opposite one, firing late, which a prevention
line cannot afford.

**What it rests on.** [Y1a](013-dynamical.md#y1a-the-software-loop) and D2. The speedrun credits AI
with [4 records](numbers.md#def-nanogpt-ai-records) of [77 records](numbers.md#def-nanogpt-records),
all shallow to moderate.

**Prior work, and what differs.** [@cunningham2026rsi] names the loop gain, derives its threshold and
calls estimating it "arguably the most important empirical exercise"; [@burtsev2026criticality]
defines a reproduction number with no estimation procedure; [@eth2025sie] proposes disclosed
measurement; [@anthropic2026rsp], [@openai2025preparedness] and
[@metr-anthropic-acceleration-2026] use ratios of overall progress rates with inputs free;
[@zhao2025speedrun] is the harness. What differs: staged rounds at fixed inputs, the regressions for
beta and lambda, demonstrated coverage, and the bound as the binding rule.

**What would refute it.** (a) under-covers at any feasible round count; (b) the interval always spans
1; E4(b) at two scales gives values of r that differ beyond their intervals, so a small run says
nothing about the frontier; L1 finds such an estimator.

**L1.** Staged or controlled experiments on returns to AI research at fixed compute; "loop gain" with
"confidence interval"; agents improving a training recipe over rounds; forward citations of
[@cunningham2026rsi], [@burtsev2026criticality], [@zhao2025speedrun] and [@ho2025experiments].
Fields: economics of ideas, sequential design, AI evaluation.

**L2.** Derive the regression identity; state the estimator and its bootstrap interval; bound the
product by a delta-method or Bonferroni interval; treat the errors-in-variables bias, since Delta_k
appears on both sides.

**L3.** E4(c) coverage, E4(a) speedrun history, E4(b) staged run at two scales, E9 prior.

**L4.** Strongest objection: a recipe loop on a small model is not frontier research, and an open
agent that fits one GPU is not frontier AI labour, so this r is a lower bound on a different quantity.
Second: a system can be self-amplifying before acceleration shows [@burtsev2026criticality]. Third:
the agent can sandbag [@gasteiger2025subtlesandbag].

**L5, L6.** Pending.

## C5. Elicited capability with measured miss and false-alarm rates per named budget

**The claim.** A threshold is judged on the score a named elicitation protocol E recovers, E's methods
listed (fine-tuning on k demonstrations, RL with n samples, best-of-k, public scaffolds, noise
injection, weight-level methods) and revised on a schedule. Each E carries a **miss rate** (the share
of organisms with hidden capability above the threshold whose elicited score stays below) and a
**false-alarm rate** (the share of benign models lifted over), each with a one-sided upper bound,
measured over naive, RL-locked, tamper-resistant and adaptive organisms built after E is fixed by
builders blind to it, and stated only over the range where E's methods work. Claimed: (a) the rule, as
a trigger rivals can run with weight access or a trusted enclave; (b) some affordable budget brings
both bounds below their targets, [10%](numbers.md#claim-d5-miss-target) and
[10%](numbers.md#claim-d5-false-alarm-target), on naive and RL-locked organisms in the covered range;
with no misses, the miss target at [90%](numbers.md#claim-confidence) one-sided confidence takes
[22 organisms](numbers.md#claim-d5-organisms) per budget; (c) stated in advance: on tamper-resistant
organisms the claim is expected to fail, their range falls outside the guarantee, and the protocol
leans on compute (C2).

**What it rests on.** [D5](01-anatomy.md#d5-elicited-capability-robust-to-hiding) and
[F4](014-cognitive.md#f4-measuring-capability-so-a-protocol-can-trigger-on-it). A tamper-resistant
organism recalled [7.8%](numbers.md#def-robust-hard-recall) on hard tasks against
[71.2%](numbers.md#def-robust-base-recall) for its base; an RL lock held for more than
[500 GRPO steps](numbers.md#def-xh-rl-lock-steps); an audit's AUC fell from
[0.978](numbers.md#def-adaptive-auc-before) to [0.560](numbers.md#def-adaptive-auc-after) against
adaptive organisms; elicitation lifted benign models about [10 points](numbers.md#def-audit-benign-uplift).

**Prior work, and what differs.** A fixed budget was in [@anthropic2023rsp] and was dropped;
[@eu2025gpaicode] asks for state-of-the-art elicitation with no budget or miss rate;
[@openai2025preparedness] treats elicitation as a lower bound. The organism method is
[@greenblatt2024password], [@taylor2025auditinggames] (which "does not provide quantitative
guarantees"), [@hofstatter2025elicitationgame], [@jang2026explorationhacking],
[@finke2026robustorganisms] and [@soopal2026adaptive]; tests of absence are in [@bukkapatnam2026absent].
What differs: both rates per named budget over a population with hardened and adaptive organisms, as
the pass-fail rule of a multi-party trigger, with a stated range.

**What would refute it.** No affordable budget meets the targets on RL-locked organisms: the claim
then covers only naive locks, which prior work already shows, and is cut. L1 finds such rates
published.

**L1.** "Miss rate" or "false positive rate" with elicitation, sandbagging and budget; populations of
model organisms with detection rates; forward citations of [@taylor2025auditinggames],
[@greenblatt2024password] and [@finke2026robustorganisms]. Fields: ML security, testing for absence,
medical screening (sensitivity and specificity as a rule).

**L2.** Exact binomial bounds and the sample sizes they need; a sequential test for absence; a
statement that the guarantee holds only for the organism population tested.

**L3.** E3, starting from public password-locked weights [@redwood2024mathpwdlock], the auditing-game
organisms [@aisi2025auditingrepo] and noise injection [@tice2024noise; @tice2025noiserepo].

**L4.** Strongest objection: above expert level there are no demonstrations, so the guarantee is
weakest where D1 begins. Second: our organisms are weaker than a determined developer's. Third:
supervised elicitation assumes no gradient hacking [@hubinger2023trusteval]. The red team builds new
organisms after E is fixed.

**L5, L6.** Pending.

## C6. The coupled-gain certificate as a treaty test

**The claim.** With K the nonnegative gain matrix over loops and parties, K_ij = lambda_i * e_ij /
beta_i ([Y3](013-dynamical.md#y3-coupling)), if upper bounds U_ij >= K_ij hold jointly with
probability at least 1 - alpha, then rho(K) <= rho(U) <= max_i sum_j U_ij with that probability, and
any positive weights w give rho(U) <= max_i (sum_j U_ij w_j) / w_i. Claimed: (a) the treaty test "the
certificate is at most rho*", with each edge named, gated and verified on its own, so subcriticality
is certified without knowing K; (b) the smallest set of edge cuts that brings the certificate below
rho*, with its sensitivity to each unmeasured edge; (c) a negative result, falsifiable by better data:
the software row alone leaves [-0.07](numbers.md#dyn-software-headroom-upper) of headroom at the
corrected 95th percentile, so the certificate cannot be issued at that confidence before any
cross-feed counts.

**What it rests on.** [Y3](013-dynamical.md#y3-coupling). Burtsev's individually subcritical blocs
reach a network rho of [1.15](numbers.md#dyn-burtsev-network-rho), an e-folding time of
[3.6 years](numbers.md#dyn-burtsev-efold-years) on our arithmetic.

**Prior work, and what differs.** The spectral-radius condition is proved for loops
[@davidson2026feedback] and across actors [@burtsev2026criticality] and written as a sum of channels
[@cunningham2026rsi]; the bounds are textbook (Perron and Frobenius; Collatz and Wielandt). What
differs: the certificate from entrywise bounds as a treaty test, with named edges verified separately.

**What would refute it.** L1 finds the certificate used as a policy target. The likeliest place is
epidemic control, where the type and target reproduction numbers compute the effort on chosen entries
of a next-generation matrix that brings its spectral radius below 1; if that literature states this
certificate, C6 is an application of it and only the AI use differs. E11 finds the certificate so
loose that no feasible set of cuts issues it.

**L1.** Spectral-radius bounds from entrywise bounds as a policy target; next-generation matrix with
targeted control; "type reproduction number"; "target reproduction number"; coupled loops in treaty
verification. Fields: mathematical epidemiology, control theory, systemic risk in financial networks.

**L2.** Monotonicity of rho in each entry, the Collatz-Wielandt bound, a union bound over entries.
Whether the explosion condition carries over to signed matrices is stated as open; bounding absolute
values keeps the certificate conservative.

**L3.** E11, with the diagonal from E9 and E4, the compute edge from E10, the capital edge from chip
sales, the cross-party edge from E6; the economic elasticity enters as a stated range.

**L4.** Strongest objection: most off-diagonal terms are unmeasured, and the margin
rho* = 1 - m * rho_dot * T_r needs a drift rate no one has measured. Second: nonnegativity is assumed.
Third: parties report their own edges.

**L5, L6.** Pending.

## C7. The coalition share derived from the response time

**The claim.** A coalition holding a share s of the accounted fleet, at fixed algorithms and with the
budget, overhead and utilisation of [@fithian2026hardwired], has T_b(s) = h_w / s, where h_w is the
time the whole fleet would need: at that paper's inputs and projected end-2026 fleet,
[7.8 years](numbers.md#claim-whole-fleet-horizon). C1 then gives the largest admissible share
s* = min(1, h_w / (m * T_r)), with drift added through C2. Claimed: (a) s* derived from T_r, not
chosen; (b) coalition-proofness in the sense of [@bernheim1987coalition]: in E6's game no coalition at
or below s* has a profitable joint deviation its own members would not report, and some coalition
above s* does; (c) at the cited inputs the overt constraint binds only when m * T_r exceeds h_w, so the
margin is set by covert supply and the untraced pool (C8), not by the registered fleet.

**What it rests on.** [D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr) and
[O3](015-organisational.md#o3-chokepoints). The hardwired-pause overt threshold is
[3.9](numbers.md#def-hwp-fleet-over-global) times the projected global fleet; its covert evasion
threshold is [0.47 years](numbers.md#org-fe-years-of-sales) of 2025's chip sales.

**Prior work, and what differs.** [@fithian2026hardwired] sets per-state thresholds over a horizon
chosen by judgement, with coalitions in a footnote; [@gan2026clock] is bilateral;
[@rahman2025nonparty] and [@scher2025agreement] say the coalition must hold most hardware without
deriving how much; [@koopmanschap2026gpu] states "sufficient capacity" without a number. Stability:
[@bernheim1987coalition], [@ali2019coalitions], [@nordhaus2015climate], [@barrett1994self]. What
differs: the share derived from the regime's own detection and response time, with coalition-proofness.

**What would refute it.** E6 finds a coalition below s* that profits, for example by staged
accumulation that keeps each step outside the line; (b)'s proof fails; L1 finds the derivation.

**L1.** Coalition share and breakout with detection time; "coalition-proof" with arms control or
verification; climate clubs with detection; forward citations of [@fithian2026hardwired]. Fields: arms
control, environmental agreements, cartel stability (detection lags in collusion models).

**L2.** Derive s* from the fleet model and C1; prove (b) for a stated payoff class, with rewarded
reporting by members as the sub-coalition deviation.

**L3.** E6 (detection from C3, payoffs as in [@nordhaus2015climate]), E22 (how much each kind of party
can add).

**L4.** Strongest objection: against a coalition that includes a major power no response halts it, so
T_resp is unbounded and s* means nothing; above that size the regime offers deterrence only. Second:
the fleet itself is uncertain by the factor of [4.1](numbers.md#org-huawei-spread) between outside
estimates of one maker's output. Third: coalitions form in secret and pool covert compute.

**L5, L6.** Pending.

## C8. The aggregate footprint floor, a margin per channel, and the untraced pool

**The claim.** For a run of C useful operations finished within T, the aggregate chip floor is
N_min = C / (r * u * T) and the energy floor E_min = C * e, with T no longer than the longest sensible
run under prevailing growth rates [@rahman2026]; each channel's margin is its detection limit over the
floor it sees. Claimed: (a) only chip accounting sees the aggregate floor, and its resolution must be
finer than N_min at the run length a pause makes rational; (b) the physical chapter's falsifier: for a
distributed run at [1e+25 FLOP](numbers.md#phys-rahman-1e25-target), every facility channel's margin
exceeds one; (c) the untraced pool is a covert reserve in every party's breakout time, and already
exceeds the floor: the median compute smuggled into one country is
[31](numbers.md#claim-pool-over-floor-now) times the floor for a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run today and
[165](numbers.md#claim-pool-over-floor-pause) times under a pause; (d) with C3, at the historical
discovery rate, the line holds for that reserve only if it cannot reach C* at all, so the protocol
must shrink the pool, not hope to find what it hides.

**What it rests on.** [P4](011-physical.md#p4-the-footprint-and-its-floor). That run's floor is
[21,000 H100e](numbers.md#phys-floor-chips-1e26-now) today and
[4,000 H100e](numbers.md#phys-floor-chips-1e26-pause) under a pause; satellites reliably found
facilities above [10 MW](numbers.md#phys-sat-reliable); about
[1,000,000 chips](numbers.md#phys-chips-unaccounted) are untraced; denial multiplies a denied party's
power per unit of compute by [2.5](numbers.md#org-denial-power-multiplier), a gain for facility
channels.

**Prior work, and what differs.** [@koopmanschap2026gpu] traces detectability against facility size;
[@scher2025] argues for tracking chips, not data centres; [@scher2025agreement] caps unmonitored
clusters; [@rahman2026] gives the cheapest distributed configuration and the longest sensible run;
[@halstead-ai2040] gives per-site chances; [@sastry2024compute] flagged distribution. What differs: the
formula in measured inputs with a time axis, a margin and crossing year per channel, and the pool
entered into breakout time.

**What would refute it.** E8 finds a facility channel with a margin below one at that size; L1 finds
the formula with the time axis and per-channel margins.

**L1.** Footprint floor of a training run; distributed training with detection margins; "unaccounted
chips" with breakout; forward citations of [@rahman2026] and [@koopmanschap2026gpu]. Fields: remote
sensing, energy monitoring, export-control enforcement.

**L2.** The derivation, with the correction it forces: a floor must use the highest utilisation an
adversary could reach, since every floor scales as one over utilisation. State which inputs make it a
bound and which an estimate.

**L3.** E8, E14 (distribution tax), E13 (power per useful operation), E22 (pool growth).

**L4.** Strongest objection: the pool is modelled, never counted, on an assumed detection rate, and
chips from a denied party's older nodes are outside it. Second: with a typical utilisation the floor is
an estimate, not a bound, until L2's correction is applied.

**L5, L6.** Pending.

## C9. The height-clocked licence, valid only once logged

**The claim.** A chip licence (i) names a recent Bitcoin block hash, so it cannot predate that block;
(ii) ends at a block height, and the chip stops when it has seen no headers showing progress for
longer than a local bound; (iii) is valid only once it appears in a public append-only log anchored
in Bitcoin, the log that also holds the sealed training-run declarations. Claimed properties: **P1** no
advance signing; **P2** no extension by slowing the clock, since withholding headers stops the chip at
its local bound and forging them costs real proof of work at the minimum difficulty the chip enforces;
**P3** no undetected equivocation of licences or declarations; **P4** provable non-issuance, since an
unlogged licence is invalid. P3 and P4 answer two problems flexHEG leaves open: proving non-issuance
[@petrie2025flexheg1] and stopping conflicting extensions [@aarne2025flexheg3]. Not claimed: that
sealing makes a declaration true [@fang2023polbroken]. This is engineering, claimed as such.

**What it rests on.** [The height clock](03-novelty.md#bitcoin-block-height-as-the-licence-clock-and-freshness)
and [sealed declarations](03-novelty.md#sealed-declarations) in the novelty file, and the memo's
section on Escapement.

**Prior work, and what differs.** A chip nonce stops advance signing online [@petrie2024offline];
flexHEG uses a blockchain hash as a delay proof in passing and names the idle-chip weakness of cycle
counters [@petrie2025flexheg2]; Bitcoin timestamping [@gipp2015timestamping; @todd2016opentimestamps]
and transparency logs [@laurie2013ct] are established; device fingerprint logs [@harack2025oxford],
firmware weight hashes [@shavit2023chinchilla] and chip ledgers [@alramiah2025pause] exist. What
differs: the combination, with offline, publicly checkable freshness and a clock the operator cannot
slow.

**What would refute it.** A property fails under its assumptions; likeliest, P2 against a private
chain whose difficulty is driven down through the timestamp weakness of Bitcoin's retargeting, unless
the chip enforces a minimum work per header. Or the prototype cannot check headers within a
constrained budget. Or L1 finds the combination.

**L1.** Block hash freshness for hardware licences; block height expiry; transparency logs for
export or chip licences; proof of non-issuance; forward citations of the flexHEG reports. Fields:
compute governance, software licensing, certificate transparency, light clients, secure time.

**L2.** P1 to P4 under stated assumptions (collision-resistant hashing, an honest majority of hash
power, an intact secure element, equivocation caught by gossip as in certificate transparency); a bound
on the cost of forging headers; Bitcoin time is accurate only to hours [@todd2016opentimestamps], so
periods of weeks or longer.

**L3.** E25.

**L4.** Strongest objection: everything rests on the chip, and on-chip verification faces "severe,
unsolved hardware security challenges" [@baker2025verifying]; one broken trust anchor defeats every
chip at once [@chuang2026teefail]. Second: a leading chip maker opposes remote off switches
[@nvidia2025nobackdoors]. Third: given a trustworthy secure clock, the height clock adds little.

**L5, L6.** Pending.

## C10. Superintelligence against an institution at matched time and budget, and the crossover budget

**The claim.** D1 as Part I leaves it ([D1](01-anatomy.md#d1-superintelligence-the-endpoint);
[F4](014-cognitive.md#f4-measuring-capability-so-a-protocol-can-trigger-on-it)): in at least a
fraction alpha of K decisive clusters, S's elicited score beats a named organisation O_k given the
same wall-clock time t_k and budget b_k, on items from a regime-held, refreshed pool, with O_k's tools
frozen at a declared date. Added: the **crossover budget t\***, the time budget at which S's score on
the AI-research cluster equals the comparison's at equal compute and money. Claimed: (a) the
combination as a definition; (b) on clusters with team or institutional baselines, the verdict is
stable when the organisation changes within its class, and the fraction won rises with effective
compute smoothly enough to extrapolate (Part I's pass condition); (c) t* is estimable with an interval
and rises across model generations without saturating.

**What it rests on.** [Matching time and cost](014-cognitive.md#matching-time-and-cost). RE-Bench's
AI-to-human ratio moves [8](numbers.md#cog-rebench-swing)-fold between
[2 h](numbers.md#cog-rebench-budget-short) and [32 h](numbers.md#cog-rebench-budget-long) budgets,
about [1.68](numbers.md#cog-rebench-swing-per-doubling) times per doubling; t* for 2024 agents lay
between [2 h](numbers.md#cog-rebench-budget-short) and [8 h](numbers.md#cog-rebench-budget-mid). Only
[5](numbers.md#cog-th11-long-baselined) of [31 tasks](numbers.md#cog-th11-long-tasks) over
[8 h](numbers.md#cog-th11-long-threshold) have a human baseline.

**Prior work, and what differs.** [@genewein2026agiasi] (expert collectives, frozen technology, no
budget matching), [@ngo2023tagi] (groups at matched time), [@anthropic2026rsp] (whole research staff
at matched cost, one cluster), [@gdm-fsf-v3-1-2026]; RE-Bench matches time and GPU hours
[@wijk2024rebench]; METR's time horizon is t*'s closest relative [@kwa2025horizon]; refreshed
batteries exist [@white2024livebench]. What differs: time and budget matched together, institutional
baselines across clusters on a regime-held battery, the alpha fraction, and t* as the quantity to
track.

**What would refute it.** The verdict flips with the organisation within its class, or with t in a way
t* misses: D1 is underspecified. t* cannot be estimated for lack of long baselines: the claim shrinks
to the definition. L1 finds the combination.

**L1.** Matched-budget comparisons of agents and human teams with a crossover; institutional
baselines for benchmarks; forward citations of [@wijk2024rebench], [@rein2025hcast] and
[@genewein2026agiasi]. Fields: AI evaluation, forecasting tournaments, productivity measurement.

**L2.** No proof needed for the definition. t* is well defined when the score ratio is monotone in
budget; state that assumption and how t* is interpolated and bootstrapped.

**L3.** E21 (which absorbs Part I's scaled-down D1 battery), E2, E1.

**L4.** Strongest objection: D1 holds only at the endpoint, so it cannot warn, and near the line
elicited scores are lower bounds. Second: contest teams are not institutions; the one live CTF
comparison pitted an agent against mostly undergraduate teams using AI [@tang2026ctfcollab]. Third: a
harm-based definition with a legal presumption [@scher2025agreement] never measures capability and may
be the better treaty rule.

**L5, L6.** Pending.

## C11. Closure judged input by input, with narrow optimisers inside the loop

**The claim.** For each input to the next model (compute, weights, data, research labour, money,
cross-party transfer of research results), closure e_i is the share of increments obtained without a
logged human-held gate the regime can verify; a narrow system whose outputs feed a covered system's
training, code or compute counts as part of it. Claimed: (a) Burtsev's single closure factor chi
factors over inputs: the gain transmitted with gates on any subset of inputs is predicted, within its
interval, by combining per-input factors measured one gate at a time; (b) a narrow optimiser in the
staged loop raises the measured return beyond its interval when its target is the training stack, and
not otherwise. If (a) fails, per-input closure is framing and is cut; if (b) fails, narrow systems need
no loop exception.

**What it rests on.** [D6](01-anatomy.md#d6-closure), [F3](014-cognitive.md#f3-narrow-versus-general),
[the acquisitive loop](013-dynamical.md#y1e-the-acquisitive-loop), [A4](012-computational.md#a4-data).
Replication task success passed [60%](numbers.md#def-replibench-2025) on simplified tasks, with failures
at identity checks [@aisi2025trends; @black2025replibench]. One developer reports that AI leads
[26%](numbers.md#def-anthropic-ai-led) of its AI research work, a self-report [@anthropic2026pace].

**Prior work, and what differs.** [@burtsev2026criticality] defines operational closure;
[@chen2026rsisurvey] classifies loops by closure; [@miotti2025narrowpath] bans found systems building
found systems; [@scher2026research] argues every input must be held together; [@redlines-2025] names
unauthorised self-improvement; [@novikov2025alphaevolve] is a narrow optimiser on a training stack.
What differs: closure decomposed by input against named, auditable gates, with the narrow-optimiser
rule.

**What would refute it.** (a) or (b) fails; L1 finds the decomposition.

**L1.** "Operational closure" with inputs or gates; gate audits in AI research pipelines; loop
classifications by input; forward citations of [@burtsev2026criticality] and [@chen2026rsisurvey].
Fields: AI governance, control theory, safety engineering.

**L2.** Per-input factors combine by product when inputs enter the research production function
multiplicatively (Cobb-Douglas), and not when one binds (Leontief) or inputs substitute. So (a) also
tests the production function.

**L3.** E4(d) (gates on and off, with seeded requests a working gate must refuse), E4(e) (with and
without a narrow optimiser), E16, E17, E19.

**L4.** Strongest objection: gates on research labour rest on self-reports, and a gate can be a rubber
stamp. Second: gates further apart than the 80% time horizon, about
[3 hours](numbers.md#dyn-horizon-p80-hours), can be crossed unattended. Third: a small staged loop has
none of a frontier pipeline's inputs.

**L5, L6.** Pending.

## C12. The pathways ranked by their effect on the line

**The claim.** The ranking in [the pathways chapter](02-pathways.md#the-ranking), which closes Part I:
seven pathways, each judged necessary, sufficient or neither on stated proxies, ranked by how much it
shortens T_b, how hard it is to see and how cheaply it can be limited, with ties where the evidence
does not separate them. Recursive self-improvement and undeclared compute tie first; scaling of
declared compute, training and inference, is third; distillation from a stronger model fourth;
self-replication and resource acquisition fifth; continual learning sixth; long-horizon autonomy
seventh, recast as the clock that spaces the gates. Claimed: (a) the method, with each pathway tied
to a side of D4 (it shortens T_b or lengthens T_r), to the channel that sees it and to the cost of a
limit; (b) undeclared compute and distillation as pathways, where the memo had them as failure modes;
(c) each verdict as a statement its proxy can falsify; (d) the response class each rank gets
(restrict, meter or watch), from which Part II is derived.

**What it rests on.** [The pathways chapter](02-pathways.md#what-a-pathway-is-and-what-would-decide-necessary-and-sufficient).
Undeclared compute lengthens T_r to [37 years](numbers.md#path-covert-td-prevent) at the historical
discovery rate, and the untraced pool, gathered, would run a [1e+26 FLOP](numbers.md#phys-rahman-1e26-local)
job in [2.9 days](numbers.md#path-covert-days-1e26). Compute carried most language-model gains
[@ho2024algorithmic]; algorithms complement compute more than they substitute [@gundlach2025origin;
@whitfill2025bottlenecks]; measured AI contributions to frontier research are shallow
[@shetty2026metrnanogpt].

**Prior work, and what differs.** The method is acquisition path analysis, which ranks paths by time
and detection probability [@allen-2015-llnl], carried over to AI. Davidson, Hadshar and MacAskill
compare the loops [@davidson2025three]; [@genewein2026agiasi] lists four pathways without ranking them;
[@miotti2025narrowpath] and [@redlines-2025] imply self-improvement first. What differs: loops and
supply and transfer routes ranked together, each tied to T_b or T_r, a channel and a cost, with ties.
The chapter's own search was run by the helper that wrote the ranking, so it is not L1.

**What would refute it.** A verdict contradicted by an experiment: E1 and E15 showing algorithms
substitute for compute at the frontier would undo "nearly necessary in practice" for declared scaling;
E5's survival fit giving a discovery rate near the memo's placeholder would drop undeclared compute
from the top. An order that flips under a reasonable reading of the three unweighted criteria. A prior
ranking of loops and supply routes together, found at L1.

**L1.** The chapter's queries, plus the two works its search turned up but did not open (a 2022 model
of paths to high-level machine intelligence, a 2026 comparison of strategic visions for a transition
to superintelligence), which L1 opens first. Fields: AI governance, the IAEA's state-level concept,
risk analysis.

**L2.** Necessity verdicts as propositions in the common form (D1 reachable with a given loop cut,
under stated parameters); the rest is empirical.

**L3.** E4 and E5 (they decide the tie), E1, E15 and E18 (scaling), E10's distillation arm, E19, E7,
E2.

**L4.** Strongest objection: the criteria carry no weights, so the order is a judgement a red team can
reverse by reading them differently. The chapter names its three weakest order judgements
(distillation against declared scaling, self-replication against continual learning, and the tie),
and the red team should start there. Necessity cannot be shown before D1 exists.

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

1. **E4, loop gain, parts c and a.** (c) Coverage of C4's interval and the trigger's late-firing rate
   under a sandbagging agent, simulated in the common form against the number of rounds. (a) The
   speedrun history: per-record gains on a compute-equivalent axis with FLOP per record from the logs,
   systems and algorithmic changes apart, contributors as the input, AI-credited records apart, from
   [@moddednanogpt], [@epoch2026speedrundata] and [@shetty2026metrnanogpt]. `heavy`, under an hour.
   `e04_loop_gain`. C4, C2. Browser: yes.
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
   compiled case by case with sources and fitted as a distribution by response type. Named in D4's test.
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
   each interval lies above 1. `heavy`, minutes. `e09_returns`. C4, C6. Browser: yes.
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
    `heavy`, minutes. `e18_cap_leak`. C2. Browser: yes.
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
    low-difficulty chains and conflicting licences. Carries the memo's tamper tests of sealed
    declarations. `heavy`, minutes. `e25_licence_log`. C9. Browser: yes.
14. **E23, the durability backtest.** Supply stages ranked on data public at the end of 2022, scored
    against erosion from 2022 to 2026. A sanity check with so few stages, so last. `heavy`, minutes.
    `e23_durability`. An open question in [O3](015-organisational.md#o3-chokepoints). Browser: yes.

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
    over at least [5 rounds](numbers.md#claim-d2-rounds) at fixed compute on a one-GPU version of the
    speedrun task [@zhao2025speedrun; @moddednanogpt], at one, two and four times the agent budget, at
    two model scales. (d) A logged gate on each input, on and off, with seeded requests a working gate
    must refuse. (e) With and without a narrow optimiser. `gpu`, weeks; needs E3's elicitation and
    E4(c)'s round count. C4, C11, C2. Browser: no.
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

The first five to build are E4 (c and a), E1, E5, E24 and E8: in hours on a CPU they decide whether C4
can ever trigger, supply C2's efficiency term, give C1's T_r its detection and response halves, and run
the physical chapter's falsifier for C8.

## Cut, and why

**Prior work, so used and credited, not claimed.** The organising idea of safeguards timeliness
[@openai2023governance; @sastry2024compute]; registered chips under expiring licences
[@petrie2025flexheg1; @petrie2025flexheg2]; renewal by k of n licensors [@aarne2025flexheg3]; random
challenge inspections [@scher2025agreement]; rewarded whistleblowing [@dyck2007whistle]; power and heat
signatures [@wasil2024verification]; evaluations on elicited capability against thresholds
[@anthropic2023rsp; @eu2025gpaicode]; bans on closed loops [@miotti2025narrowpath], whose only possible
addition is C4's trigger; the loops as growth laws, runaway against saturation, and coupling itself
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
- Ranking supply stages by durability (O3): too few stages for any test to discriminate.
- The discovery rate of covert programmes: an input, not a contribution, arithmetic on a convenience
  sample that its chapter does not claim. It enters C3 through E5 and drives C1 and C8.
- Merged: transfer as a thresholdable quantity (A5) into C11; institutional baselines for the decisive
  functions (F2) into C10; the combined cap leak into C2; denial-induced footprint growth (O3) into C8.

**Deferred: not searched or not built, so nothing may be claimed.** The drift trigger for fleets that
keep learning after deployment (E7 measures what it would rest on). The experiential and acquisitive
loops written as growth laws (E7 and E19 measure them). A race model with the regime's detection time
inside it, and the candidate "compliance-only declarations do not raise risk": if E6 finds it holds in
every calibrated regime, it may become a claim after its own L1 search.

In all, twelve claims are kept and thirty-two candidates are cut or deferred: nineteen as prior work,
ten as too small, framing or merged, three deferred.

## What would make this program fail

Four footings. If one falls, the protocol loses its ground, not just a part.

1. **C1, the line.** If T_r cannot be computed with an interval narrower than the T_b intervals it
   faces, or a T_b the parties compute differently collapses compliance as in [@barrett2012climate],
   there is no agreed boundary between useful AI and weapons-grade, and the protocol falls back on
   fixed compute caps, which are prior work and drift as algorithms improve.
2. **C2, breakout time.** If C* and the efficiency path leave every relevant T_b interval spanning the
   line, the line decides nothing. C* must then be set so low that frontier holdings become
   weapons-grade by default, and the protocol stops keeping useful AI allowed, which fails the brief's
   first addition.
3. **C3 with C8, covert compute.** At the historical discovery rate a [5%](numbers.md#def-prevent-beta)
   miss takes [37 years](numbers.md#path-covert-td-prevent). If no channel does better for undeclared compute,
   and chip accounting cannot close a pool already [165](numbers.md#claim-pool-over-floor-pause) times
   the floor under a pause, the line cannot be held on covert paths, and the protocol binds only parties
   that choose to declare.
4. **The compute backbone.** Prior work, not a claim here, but every claim assumes it: chips counted at
   birth at a few narrow stages, and the states hosting those stages bound by the same rules. The
   organisational chapter found leaks at the edges and a holder that reversed its own rule within
   months. Without it C1, C2, C7 and C8 have no holdings to compute from.

The other losses are survivable. Without C4, self-improvement gets a cruder rate rule; without C5,
systems cannot be placed by capability and the protocol leans on compute at a higher cost to useful AI;
without C6 or C7, coupled loops and coalitions are handled by judgement; without C9, licences use
flexHEG's clocks; without C10 to C12 the definitions and the ranking are weaker but the line stands.
None of this has been tested against a real adversary. The protocol is a design.
