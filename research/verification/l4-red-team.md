# Level 4: red team

This is the level 4 check of [the claims file](../04-claims.md): a red team whose only job is to break
claims C1 to C12 and the protocol built on them ([Part II](../06-protocol.md)). It was run on
2026-11-27 by a helper that wrote none of the work. It read the claims, the formal statements and
proofs ([the formal file](../05-formal.md)), Part II, the pathways chapter, every result file in
`data/results/`, every experiment script in `tools/exp/`, the hand-compiled case tables in
`tools/exp/data/`, and the checks in `tools/formal/`.

**What was run.** Every experiment that has results was rerun with its output redirected outside the
repo, under `heavy`. E1, E5, E8 and E24 reproduce their committed result files exactly (every number
and every detail); E4's part (a) reproduces to 1e-12. `python3 tools/formal/run_all.py` passes, and
every counterexample count the formal file quotes (524 of 6,000; 202 of 1,500; 12 of 296; 112 of
649; 2,184 of 20,000) matches its check's output. Variants (other subsets, seeds, codings and a
counterexample to one proposition) were run as throwaway scripts outside the repo; each is described
below precisely enough to rerun. Numbers from those reruns are marked "our rerun" and are not ledger
numbers. Three new sources were opened by identifier, with no search; they are listed in the block at
the end. No literature search was run, so nothing here is a "not found" claim.

**Severity.** *Fatal*: the claim, or the named part, must be cut. *Serious*: it must be corrected or
downgraded. *Minor*: it should be fixed but changes no verdict. Each attack ends with at most one line
on what would answer it. This report breaks; it does not mend.

## C1

**C1.1. An evader that moves its progress between paths defeats the per-path line.** Severity:
serious. The formal file's Proposition 1.5 says a breakout succeeds with probability at most beta
"iff T_b(p) >= T_r(p) for every path", and Part II repeats this as "if and only if". Lemma 1.1
needs a fixed T_b(p). A strategy that switches paths on a partial signal has a random T_b, so the
per-path test cannot be written for it, although the notation counts "composites it can switch
between" as paths. Counterexample (our rerun, exact integral and 400,000 Monte Carlo draws), with
beta = 0.05 and T_resp = 0.25 years on both paths, m = 1:

- Declared path A: T_b = 1. A partial signal arrives at rate 7 a year; a finding is confirmed 0.25
  years after it if the evader stays. T_d = 0.678, T_r = 0.928, so A meets the line, with a success
  chance of 0.030.
- Covert path B, from scratch: T_b = 10, discovery rate 0.31 a year from arrival. T_d = 9.66,
  T_r = 9.91, so B meets the line, with a success chance of 0.049.
- The switch: train on A; if the signal comes before 0.5 years, leave before confirmation and carry
  the checkpoint to B, finishing the remaining work at B's speed. It succeeds with probability 0.105
  (exact), 0.106 (Monte Carlo): more than twice beta.

The scalar test the formal file calls "stricter than needed" (min T_b against max T_r) rejects this
holding; the per-path test admits it. For AI the switch is natural: a checkpoint is a file, and the
regime's own channels (a meter, an inspection) can tip the evader before they confirm. `c1_margin.py`
tests two to six fixed paths and never a switch. The formal file's "Fails when" ("Detection depends
on what the evader learns as it goes") does not cover it: here the hazard on each path is fixed and
only T_b is random. One line: state the line over adaptive strategies, or keep the scalar test where
progress is portable.

**C1.2. While the untraced pool is open, the line classifies every party as weapons-grade.**
Severity: serious. C1 is an "if and only if" over every path open to the holder. Part II tabulates
the pool "as if it could command all of it" for every party, and says "While the pool is open, that
path fails the line for everyone". So by C1's own definition every party's holding is weapons-grade
today, whatever it declares, and nothing is left "outside it free to keep improving". The pool path
fails on Part II's own arithmetic: the smuggled stock reaches the one published budget in
[3.9 years](../numbers.md#prot-pool-years-rosetta) to [13 years](../numbers.md#prot-pool-years-small)
under drift, against a detection time of [32 years](../numbers.md#e5-td-pool-years) before any
response. C1(a) claims the inequality as the boundary of useful AI; until the pool closes it is a
boundary with nothing on the safe side. One line: restrict C1(a) to a regime whose pool is closed, or
say the line is undefined until then.

**C1.3. C* has no error bound, and a one-OOM disagreement over it is larger than the line.**
Severity: serious. Proposition 1.2 needs one-sided errors with known bounds; the formal file concedes
C*'s error "has no bound". At Ho et al.'s central rate one OOM of C* moves T_b by
[2.3 years](../numbers.md#comp-years-per-oom-ho), more than the whole illustrative line of
[2.0 years](../numbers.md#prot-line-declared). So two parties one OOM apart on C* classify the same
holding differently, which is the disputed-threshold failure the claim's own L4 plan names. It also
empties C1(d): a path is "near the line" when its T_b interval overlaps m * T_r, and with C*'s error
in the interval every interval overlaps, so prevention-grade monitoring is owed everywhere. The
detection and response inputs fare no better: E5's rate transfers nuclear and biological programmes
and E24's latencies transfer arms control, and neither transfer error has a bound, so m cannot be
sized to cover them. One line: report T_b conditional on C* and say m covers only arithmetic error.

**C1.4. beta bounds one attempt, and the record shows repeated attempts.** Severity: serious. Lemma
1.1 and Proposition 1.4 bound the success chance of a single breakout. Nothing in C1 or Part II stops
a halted party from trying again, and in E24 [71%](../numbers.md#e24-halt-share-reversed) of halts were
later reversed or shown incomplete. At beta = [5%](../numbers.md#def-prevent-beta), independent
attempts succeed with probability 1 - 0.95^n: 14% after three, 40% after ten (our arithmetic). C1(b)
says an admitted holding "is still stopped with probability at least 1 - beta"; over a regime's life it
is not. One line: state the guarantee per attempt and bound the number of attempts.

**C1.5. Under Part II's own deadlock rule, no path has a response that does not wait on a political
decision.** Severity: fatal for C1(c). After E24, C1(c) was narrowed to "declared paths whose
response does not wait on a political decision". Part II says licence lapse is that response. But its
deadlock rule renews every licence "unless k of n licensors, with the accused party's own bloc
excluded from the count, make a finding of violation". A finding by a quorum of rival states is a
political decision. In E24 even formal statements, the cheapest response, took a median of
[60 days](../numbers.md#e24-statement-median-days) and up to
[1,102 days](../numbers.md#e24-statement-max-days). Part II's illustrative
[1.0 years](../numbers.md#prot-tr-declared) for T_r adds one licence period of
[3 months](../numbers.md#prot-licence-months) and no decision time at all
(`model/parts/060_protocol.py`, `prot-tr-declared`), although Part II's own text says licences bound
T_resp "by one period plus the quorum's decision time". So the class of paths on which C1(c) can
compute T_r is empty under the protocol C1 is meant to serve. One line: measure the quorum's decision
time in drills, or cut (c).

**C1.6. E24's headline share is inflated by one state's tests after it had left the treaty.**
Severity: minor. Of the six findings never halted, five are the DPRK's (2002, 2009, 2013, 2016,
2017) and one the USSR's; four of them are nuclear tests detected after the DPRK's 2003 withdrawal,
which are responses to a non-member after its breakout, not halts of a breakout in progress. The
script's own first-finding-per-programme variant gives
[17%](../numbers.md#e24-halt-first-share-never) never halted, against
[46%](../numbers.md#e24-halt-share-never-all). Dropping the five post-withdrawal test findings (our rerun)
leaves 8 findings, 25% never halted, and a median among halts of 1.05 years. C1's conclusion survives:
any share never halted above beta_2 leaves no finite quantile. The number quoted does not. Also, the
"median 0.9 years" is a median among findings that were halted; the Kaplan-Meier median with the
unhalted censored is [6.3 years](../numbers.md#e24-halt-km-median-years-all). One line: lead with the
first-finding figures and the censored median.

**C1.7. Both sides of the line are in the evader's hands.** Severity: serious. T_b on the declared
path uses "a rate measured at each holding's own scale" and mandatory declarations of "algorithmic
efficiency at fixed compute". Both are self-reported; Part II says algorithms are "invisible". A
party that understates its efficiency lengthens its tabulated T_b at no risk, and one that disputes
findings, delays inspections or attacks licensors lengthens T_resp. The line assumes the estimates
err only within e_b * e_r <= m, while the party being measured controls the error. One line: price
the error a misreporting party can introduce, or say m does not cover it.

## C2

**C2.1. C* dominates every T_b interval, so the tabulated interval is conditional on a convention.**
Severity: serious. C2(a) promises "the expression, with an interval, tabulated in advance". The
formal file proves the interval exact over a box of inputs, with C* at its ends; but C*'s range has
no bound (C1.3), so the honest interval is unbounded, and any finite one is conditional on an agreed
number. C2(b) ("it differs from a single-multiplier T_b by more than either's interval") can then be tested
only with C*'s uncertainty left out, which makes (b) a statement about the other inputs. Part II's
"C* is a convention" is an admission, not an answer. One line: say the interval excludes C*.

**C2.2. E1 is not silent on scale: its own fit has drift falling with scale, which breaks the
monotonicity C2's theorem needs.** Severity: serious. C2 says "On scale E1 is silent". E1 records an
interaction of compute and date of [-3.9 ECI points](../numbers.md#e1-eci-slope-change) (95% from
[-6.4 ECI points](../numbers.md#e1-eci-slope-change-lo) to
[-2.1 ECI points](../numbers.md#e1-eci-slope-change-hi)), whose interval excludes zero and which no
research file cites. Converted with E1's own interaction fit (our rerun), the yearly
compute-equivalent gain at fixed compute is 39.9x at 1e24 FLOP and 7.0x at 1e26 FLOP. That is about
-0.38 OOM a year of drift per OOM of compute. Then the left side of C2's inequality,
log10 C + a(C) t, falls with log10 C once t exceeds about 2.6 years (1 - 0.38 t < 0, our arithmetic):
more chips give a later breakout on that horizon. That is exactly the case in which the formal file
says assumption (A2.1) fails and the two-corner interval misses (202 of 1,500 boxes in
`c2_monotone.py`). Part II's pool path has T_b of years, inside that range. Either the interaction is
an artefact (small open models distilled from larger ones gain faster), and E1's other numbers from
the same data are suspect too, or it is real, and C2's monotone interval does not apply. One line:
report the interaction and use the termwise bound until E15 decides.

**C2.3. E1's "frontier growth" sample leaves out the frontier, and the rate it gives is unidentified
across subsets.** Severity: serious. Only 105 of 258 models with an ECI score have a compute
estimate ([105 models](../numbers.md#e1-models)); in our rerun, 89 of those 105 are open weights, and
23 of the 25 models with the highest ECI are dropped for want of a compute estimate. Refitting E1's model
on subsets (our rerun):

| Subset | Models | Compute share | Algorithmic gain a year |
|---|---|---|---|
| All (the headline) | 105 | 36% | 17x |
| Not open weights | 16 | 63% | 2.6x |
| Confident compute estimates only | 59 | 44% | 7.6x |
| At or above 1e24 FLOP | 60 | 21% | 393x |
| At or above 1e24.5 FLOP | 48 | 18% | 1,512x |
| Released 2024 onward | 76 | 30% | 46x |

The headline [17](../numbers.md#e1-algo-annual) a year ([8](../numbers.md#e1-algo-annual-lo) to
[54](../numbers.md#e1-algo-annual-hi)) is a resampling interval within one choice of models; the
choice of models moves the rate over almost three orders of magnitude. Part II says the tables "take
the fast end". On the example headroom of [3 OOM](../numbers.md#comp-example-headroom-oom), headroom
alone (J and S_v only shorten it), the leak takes 2.4 years at 17x, 1.2 years at 393x and 0.94 years at
1,512x (our arithmetic): at the fast end of E1's own subsets, inside the illustrative
[2.0 years](../numbers.md#prot-line-declared). Compute and date correlate at 0.62 in E1's sample (our
rerun), and noisy compute estimates flatten the slope, which fits both the confident-only result and
the collapse at high compute. One line: report the rate by subset and say which population the
tables use.

**C2.4. "The bound is conservative" rests on one model and a wide bound.** Severity: serious
(interpretation). The [1.1%](../numbers.md#e1-oos-unforecast-share) of
[89 forecasts](../numbers.md#e1-oos-n) above the one-sided 95% bound is one model (our rerun: a
model at the 1e23 FLOP cut); without that cut it is 0 of 60. If misses were independent at a true 5%,
one or fewer among that many forecasts has probability 0.059, so "below 5%" is not shown. The bound's median half-width is
21 ECI points, about 1.7 OOM at the pooled slope. At the 1e26 FLOP cut all four forecasts fall below
the lower bound (the fit overshoots the frontier). The [0.96 OOM](../numbers.md#e1-oos-mae-oom) error
divides by the full-sample slope, fitted on the test models too; with the high-compute slopes it is
2.3 to 3.0 OOM (our rerun). So E1 shows a wide bound that overshoots at the top, not a conservative
forecast of capability from compute. One line: report the bound's width and its bias at the top.

**C2.5. Distillation can exceed its teacher, so "adds nothing beyond it" is false as a rule.**
Severity: serious. C2 says distillation "closes the gap to a teacher the holder can query and adds
nothing beyond it", and the formal file calls this "an empirical assumption, not a theorem". It has
published counterexamples. Students trained by distillation with the same architecture as their
teachers, "these Born-Again Networks (BANs), outperform their teachers significantly" on vision and
language-modelling tasks (abstract) [@furlanello2018born]. Strong models
fine-tuned on a weak supervisor's labels "consistently perform better than their weak supervisors"
(abstract) [@burns2023weak]. A holder with its own base model and a teacher's outputs can end above
the teacher, so the ceiling C2 tabulates understates the reach of the distillation path. One line:
tabulate distillation with an uplift term above the teacher, measured by E10.

**C2.6. Compute places a system badly, which C2 and Part II's fallback both rely on.** Severity:
serious for Part II, minor for C2. On GPQA Diamond, the best single training-compute threshold
classifies [79%](../numbers.md#e1-gpqa-acc-compute) of verdicts against PhD experts correctly, the best
release-date threshold [92%](../numbers.md#e1-gpqa-acc-date), and the largest losing model has
[2.8 OOM](../numbers.md#e1-gpqa-overlap-oom) more training compute than the smallest winner. C2 starts
T_b from compute, and Part II places systems beyond elicitation's range "by its compute". E1 shows a
compute-based placement can be wrong by nearly three OOM. One line: carry that overlap into the
placement rule's interval.

**C2.7. Hidden algorithms shorten T_b below the table.** Severity: serious (the claim's own third L4
objection, unanswered). Algorithmic efficiency is declared, not verified (C1.7). A party that keeps a
private gain has a T_b shorter than the table by that gain over the drift rate. Nothing in C2 bounds
it. One line: tabulate the declared path at the fast end plus an allowance for undeclared gains.

**C2.8. Status.** Minor. C2(b) and C2(c) are untested; E15 and E18 have not run.

## C3

**C3.1. The declared path's 1.5 days is an extrapolation the source does not support.** Severity:
serious. E5 converts the metering source's figure into a constant daily hazard,
`lam_meter = -ln(1 - 0.87) * 365.25`, 745 a year, and so puts the declared path's T_d at
[1.5 days](../numbers.md#e5-td-declared-days). The source says only that "over a day at least 87% of
such runs are still caught, at a 0.1% false-alarm rate per run", on "simulated datacentre power", and
reports no period longer than a day (abstract) [@kimpson2026dcpower]. If the runs its strongest
disguise hides for a day are hidden by the same disguise the next day, the meter's miss does not
compound and the meter alone never reaches a 5% miss. The declared path then rests on chip sampling,
whose rate comes from a design with [232 inspectors](../numbers.md#phys-shavit-inspectors), not from a
measurement: T_d becomes 39 days, and the ratio to the pool path about 300, not
[7,935](../numbers.md#e5-td-ratio) (our arithmetic from E5's inputs). C3(c)'s direction survives; its
size, and Part II's "1.5 days", do not. One line: treat the day figure as a one-shot catch, or measure
multi-day detection in E13.

**C3.2. The Monte Carlo cannot fail the proposition it is cited as supporting.** Severity: serious
(for the L3 status). C3 says "L3 (E5) supports (b)", citing that the memo's product "never exceeded
the evader's miss ([100%](../numbers.md#e5-product-le-max-share) of draws)". By Theorem 3.1(b) the
product over every channel is at most every path's miss, so it is at most their maximum in every draw
by construction. A 100% is guaranteed; it is arithmetic, not evidence. The
[-336](../numbers.md#e5-memo-log10-miss-1y) is likewise E5's own construction from the compounded meter
rate of C3.1; without the meter it is about -12 (our arithmetic). One line: report (b) as proved, and
E5 as illustrating it, not supporting it.

**C3.3. The historical rate is assigned to paths it has no evidence about, from a different clock.**
Severity: serious. E5 gives the cloud and distillation paths only "intelligence" at the historical
rate (`paths` in `e05_detection.py`: "no sourced rate for customer checks", "no sourced channel"),
fitted on nuclear, biological and chemical programmes. Those T_d values are a nuclear-programme rate
attached to an AI path with no link between them. C3(a) claims "sourced rates". The clock differs too.
E5 measures from a programme's start (a decision, often years before any facility); C1's T_d runs
from a breakout's start. E5's own Weibull shape is [1.49](../numbers.md#e5-weibull-shape): discovery
is likelier late in a programme. From E5's fitted Weibull (our arithmetic), the chance of discovery
within a quarter year of the start is 0.3% and within a year 2.6%, against 2.3% and 8.9% at the
constant rate. Part II reads the Weibull as favourable ("shortens it only to
[24 years](../numbers.md#e5-td-weibull-years)"); for the short windows a breakout needs, it is the
opposite. One line: give cloud and distillation no T_d until a channel is measured, and state the
clock.

**C3.4. Theorem 3.2 is false for a latent cause with more than one dimension.** Severity: serious for
the formal statement, minor for the claim. The proof uses (f(z) - f(z'))(g(z) - g(z')) >= 0, which
needs z and z' comparable. Counterexample: Z1 is 0 or 1 with equal chance, Z2 = 1 - Z1, q1 = Z1,
q2 = Z2; each q is nondecreasing in Z, yet E[q1 q2] = 0 < 1/4 = E[q1] E[q2]. The theorem's examples
("the tips from one intelligence source, or the evader's randomisation") need not be scalar. The
practical rule, use the maximum over strategies, survives through Theorem 3.1. One line: require a
scalar or associated Z.

**C3.5. The fitted rate is a pooled average over programmes that were found.** Severity: serious
(acknowledged in part, not answered). Assumption (A1.1) asks that Phi_p be "the evader's best case on
that path". E5 fits [0.094/yr](../numbers.md#e5-hazard) over [16 cases](../numbers.md#e5-cases)
that were all eventually found or disclosed; programmes never found are missing by construction, and
disclosure is informative censoring (Iran's laser work was acknowledged under investigation). The
formal file itself says the evader is the hard type. So the rate C3 needs, the careful evader's, is
below anything E5 can fit, by an unknown amount. One line: report the fit as an upper bound on a
careful evader's rate.

**C3.6. The grouping is a judgement that E5 makes in the regime's favour once.** Severity: minor.
Diversion detection ([25%](../numbers.md#org-diversion-detect), an assumption of the smuggling model)
is treated as independent of the historical channel, though both rest on intelligence and law
enforcement. Merged, they would lengthen T_d on the site paths. The pool path, which sets the
headline, does not use diversion, so no headline moves.

**C3.7. Paths outside P.** Severity: serious. Part II's path table lists stolen weights and open
weights; E5 models neither. C1.1's switching strategy (train on the declared fleet, finish on the
pool) is a path no E5 path describes. C3's own refuter is "L4 finds a path outside P with low
detection"; these are three. One line: add them to E5 or state that P omits them.

**C3.8. Insiders, the channel that worked, are what a state controls.** Severity: minor (the claim's
second L4 objection, acknowledged). Of E5's [14 discoveries](../numbers.md#e5-events), one came from
a defector; seven are coded intelligence. A state can compartmentalise and coerce insiders. Nothing new here beyond the claim's
own plan.

## C4

**C4.1. At the only data-calibrated noise level the trigger does not tell a subcritical loop from a
supercritical one.** Severity: serious, and by Part II's own rule it cuts (c). After 5 rounds per
budget at speedrun-calibrated rounds, the upper-bound rule fires in [84%](../numbers.md#e4-fa-n5) of
runs with the true return at the corrected median, [0.63](../numbers.md#dyn-r-lm-corrected), and fails
to fire in only [14%](../numbers.md#e4-late-ub-s0-cal) at the corrected 95th percentile,
[1.07](../numbers.md#dyn-r-lm-hi-corrected), so it fires in about 86% there (fresh seeds give 81.9% and
87.9%, our rerun). A rule that fires about as often either way is not a trigger. False alarms are still [71%](../numbers.md#e4-fa-nmax) after 50 rounds
per budget. Only the "favourable" setting, large tightly measured rounds that no experiment has shown
a real staged run delivers, brings false alarms to 10% in
[12 rounds](../numbers.md#e4-fa-rounds-fav). Part II's own rule: if no affordable number of rounds
brings the upper bound below K* for loops whose true K is well under 1, the protocol should "say so
rather than call it a trigger, C4 is cut". At calibrated noise, E4 finds no such number. Part II already treats closed-loop frontier research as above the trigger until E4
can estimate K, which is the prior-work ban with C4's name on it. One line: measure a staged round's
noise in E4(b) before claiming (c).

**C4.2. The sandbagging agent is an honest agent by construction.** Severity: serious. In
`e04_loop_gain.py` (the `cell` function) the fading sandbagger sets `beta_seen = beta / (1 - sandbag)`,
which is exactly an honest agent with return r(1 - s). Late firing at the corrected 95th percentile
with s = 0.5, and for an honest agent at half that return, were bitwise identical on five seeds (our
rerun). So
[94%](../numbers.md#e4-late-ub-s50-fav) is the honest firing rate at half the return, and "precision
helps a sandbagger" holds by definition. E4 says nothing about whether a sandbagger can be detected;
that rests wholly on C5, which C5(c) expects to fail on hardened organisms. One line: model a
sandbagger whose hidden return an elicitation step could recover, or drop the sentence.

**C4.3. The bias quoted for the one-set regression came from a run with no measurement error, and
the two-set remedy was never tested.** Severity: serious. C4 says one noisy measurement per round
"makes the loop look more subcritical", that "two held-out sets remove that bias", and cites
[0.53](../numbers.md#e4-diff-bias). The difference-form cells call `cell(...)` with the default
`meas=0` (`e04_loop_gain.py`, the `diff` loop), so all their noise is real variation in gain, not
measurement error. In our rerun at E4's calibrated noise, with all noise real gain, one set and two
sets both give 0.447 of the truth (identical by construction); with half the noise as measurement
error, 0.501 and 0.815; with all of it, 0.539 and 7.41. The remedy Part II adopts ("Each round's gain
is measured on two independent held-out sets") does not remove the bias at E4's noise in any of the
three mixes; at a smaller noise (first gain 0.3 e-folds, noise 0.5) it nearly does, 0.905 against
0.991 with half the noise as measurement error (our rerun). So the remedy depends on a noise level
nobody has measured. One line: test the remedy before the protocol relies on it.

**C4.4. "Five rounds" are fifteen staged runs.** Severity: minor. E4's labels say "after 5 rounds per
budget"; there are three budgets, so the [5 rounds](../numbers.md#claim-d2-rounds) of C4(a) and D2
cost 15 staged runs, and "12 rounds" costs 36. The claims file writes "after 5 rounds" and
"12 rounds". The price of the trigger is understated threefold.

**C4.5. The speedrun's r is a ratio of two collinear trends.** Severity: serious for the published
number, minor for the claim (which already says history "cannot place r"). In part (a), stock and log
input correlate at 0.979 over 27 months, and the bootstrap's lambda and beta at 0.951 (our rerun).
Placebo inputs give r = 1.03 (months since start) and 0.53 (records in the previous 180 days). Of the
draws coded "unbounded", 29.6% have both signs flipped (beta <= 0 and lambda < 0), where lambda / beta
would be positive; 8.9% have r < 0 and are counted inside the [43%](../numbers.md#e4-sr-p-below-1)
"below 1". The input counts people credited on successful records, so it depends on the gains it is
meant to explain. [0.86](../numbers.md#e4-sr-r) should not be published as an estimate. One line:
withdraw `e4-sr-r` or report it as unidentified.

**C4.6. The simulation fits its own generating law.** Severity: minor. Part (c) simulates the
first-order law and fits it by least squares. On data from Lemma 4.1's exact law, the calibrated
median estimate falls to 0.866 of the truth, in the unsafe direction (our rerun).

**C4.7. The quoted rates are for r, and the trigger is on K.** Severity: minor. Proposition 4.5 builds
K's bound as a Bonferroni product of three factors, each with its own error. The false-alarm rate
quoted as the rule's price, [84%](../numbers.md#e4-fa-n5), is for r alone; K's bound is wider and fires
more.

**C4.8. A loop never declared is never staged.** Severity: serious. The trigger applies to
declared closed-loop research. A developer that runs the loop with logged human gates that approve
everything (C11.1) has, on paper, no closed loop to stage. Detection then falls to declarations and
insiders, which C3.8 and C11.1 weaken. One line: say the trigger binds only loops the developer
declares.

**C4.9. Transfer to the frontier.** Severity: serious (the claim's first L4 objection, unanswered).
A recipe loop on a small model with an open agent measures a different quantity; E4(b) has not run.

## C5

**C5.1. A population miss rate does not bound a strategic developer's miss.** Severity: serious. C5
certifies an average over a sample of organisms. The developer the trigger faces chooses its best
hiding method. C3 argues, correctly, that a regime faces the maximum over an evader's strategies, not
the average; C5 certifies the average. Proposition 5.3 bounds the gap by the share epsilon of untested
kinds, but for a developer who picks an untested kind epsilon is 1. One line: state C5(a) as valid
only against hiding methods inside the sampled population.

**C5.2. The test organisms are blind to E; the adversary is not.** Severity: serious. C5 requires
organisms "built after E is fixed by builders blind to it", and E is "named in advance" so that rivals
can run it. The developer who hides capability sees E. The measured rates therefore describe a weaker
population than the one faced. The work's own evidence shows the size of that gap: an audit's AUC
fell from [0.978](../numbers.md#def-adaptive-auc-before) to [0.560](../numbers.md#def-adaptive-auc-after)
against adaptive organisms. One line: measure the rates on organisms built with E in hand.

**C5.3. No organism can carry hidden capability above the thresholds that matter.** Severity:
serious. Organisms are made by locking capability the builder has. Near D1 the thresholds sit above
expert level, where (the claim's own first L4 objection) there are no demonstrations, and no builder
can make an organism that hides a capability nobody has. So the miss rate cannot be measured in the
region where the trigger must work; C5's rates are "stated only over the range where E's methods
work", which excludes it. One line: say the trigger is unvalidated above expert level.

**C5.4. Organisms from a few builders are not an independent sample.** Severity: minor. Theorem 5.1
needs (A5.1), independent draws. Organisms built by one or two teams with shared methods are
clustered, so the effective sample is smaller than
[22 organisms](../numbers.md#claim-d5-organisms) and the exact bound is optimistic.

**C5.5. The fallback is weak.** Severity: serious for Part II, minor for C5. Beyond E's range Part II
"places the system by its compute"; C2.6 shows compute misplaces systems by up to
[2.8 OOM](../numbers.md#e1-gpqa-overlap-oom) on one benchmark.

**C5.6. Status.** Minor. E3 has not run; C5(b) is a prediction.

## C6

**C6.1. With unmeasured edges, the certificate has no probability content.** Severity: serious.
Theorem 6.2 needs bounds that "hold jointly with probability at least 1 - alpha". The claim admits
"most off-diagonal terms are unmeasured" and the formal file says an unmeasured edge "enters as a
stated range, which is not a confidence bound". Parties report their own edges, so even measured
bounds are not jointly valid. A certificate computed from such a U is a calculation on judgements,
not a test with error alpha. One line: issue no certificate while any edge is a stated range.

**C6.2. The threshold is undefined.** Severity: serious. rho* = 1 - m * rho_dot * T_r. rho_dot is
unmeasured, and E24 gives no bounded T_r (C1.5, C1.6), so rho* is not a number. One line: fix rho* by
agreement and say so.

**C6.3. Edges no gate can cover.** Severity: serious. Part II gates each named edge. Weight theft and
espionage move research results across parties outside every gate; Part II itself calls weight theft
"a gap". An edge that cannot be gated cannot be cut, and its bound is a guess. One line: list the
ungatable edges and bound them, or say the certificate omits them.

**C6.4. C6(c) restates a fully closed loop.** Severity: minor. The diagonal entry K_ii is e * r. The
"negative result" uses r itself, [1.07](../numbers.md#dyn-r-lm-hi-corrected), so it describes a loop
at closure 1. That figure is the 95th percentile of r, [3.21](../numbers.md#dyn-r-lm-hi), times one
minus a point estimate of the research compute share, [0.67](../numbers.md#dyn-research-compute-share);
uncertainty in that share is not in it. "No set of edge cuts issues the certificate" therefore says
that a fully closed software loop at a corrected upper percentile is above 1, which C4 already says.

**C6.5. Status.** Minor. E11 has not run.

## C7

**C7.1. The protection the claim offers exists only in a payoff region the work says is empty.**
Severity: serious. Theorem 7.2(i) needs every member's reward for reporting to exceed beta times its
value of a breakout, R_i > beta * V_i; the formal file says "no fund pays [that] to a state". Without
it, only (ii) remains: no breakout profits a party if beta * V_i <= (1 - beta) * P_i. At beta = 5%
that fails whenever the value of a decisive advantage exceeds 19 times the penalty
((1 - beta) / beta, our arithmetic). A party valuing a decisive advantage that highly profits from an
attempt, alone or in company, even at the line. In that region, the one the work calls realistic,
coalition-proofness adds nothing to prevention. One line: state C7(b) as empty for decisive-advantage
payoffs.

**C7.2. The check's count, and the claims file's "none can", overstate the theorem.** Severity:
serious. The claims file says that between s* and m * s* "the breakout time still exceeds T_r and
none can (8,936 such shares sampled)". `c7_coalition.py` adds a share to that count whenever
s* < s <= h_w / T_r, whether or not a condition was checked. Split with its random sequence unchanged
(our rerun): 4,482 shares in the penalty regime, 3,689 in the reward regime with two or more members,
and 765 in the reward regime with one member, where neither (i) nor (ii) was checked; in 165 of those
765 the single party's breakout payoff is positive, a profitable deviation nobody reports. And a direct
counterexample to "none can": pi = 0.03 <= beta = 0.05, V = 1000, P = 1, R = 1; staying pays 29.03,
more than R and more than 0. Theorem 7.2, which states its conditions, is sound; the sentences that
drop them are false. One line: restore the conditions and recount.

**C7.3. "The overt constraint does not bind today" is an artefact of the assumed budget.** Severity:
serious. h_w = [7.8 years](../numbers.md#claim-whole-fleet-horizon) comes from the hardwired-pause
paper's breakout budget of [2e+29 FLOP](../numbers.md#def-hwp-breakout-budget), "an assumption of its
paper". With the budget ten times lower (`--set def-hwp-breakout-budget=2e28`), h_w is 0.8 years and
the declared-path share falls from [100%](../numbers.md#prot-coalition-share-declared) to 39% (our
rerun of the model). C7(c) is a property of one assumed number. One line: report s* as a function of
the budget.

**C7.4. Part II prints covert shares the claims file says have no number.** Severity: serious. The
claims file: "s* needs a bounded T_r, which E24's record does not give (C1), so the share has no number
until a response is drilled." Part II prints [12%](../numbers.md#prot-coalition-share-covert) and
[24%](../numbers.md#prot-coalition-nodeviation-covert) for the covert path, computed with T_resp = 0
("before any response"). On C1's own result the covert path's T_r is unbounded and s* is 0. One line:
withdraw the two covert shares.

**C7.5. The share counts the wrong stock.** Severity: serious (the claim's second and third L4
objections, unanswered). s is a share of the accounted fleet. A coalition's covert path draws on the
untraced pool, which is outside the fleet, and the fleet itself is uncertain by a factor of
[4.1](../numbers.md#org-huawei-spread) between outside estimates of one maker's output.

**C7.6. The coalitions that matter include a major power.** Severity: serious (acknowledged). Against
them, the formal file says, T_resp may be unbounded and "the theorem is empty". C7 is a result for the
coalitions that need it least.

**C7.7. Status.** Minor. The game is one-shot; staged accumulation and repeated play wait on E6.

## C8

**C8.1. The "bound" is computed at a precision current training does not use.** Severity: serious.
Theorem 8.1 holds with r_j the peak at the precision the run uses. The figures C8 and Part II call
the bound, [1,600 H100e](../numbers.md#formal-floor-bound-1e26-pause) for a
[1e+26 FLOP](../numbers.md#phys-rahman-1e26-local) run, use the dense BF16 peak,
[989.5 TFLOP/s](../numbers.md#phys-h100-bf16). The dense FP8 peak is
[1,979 TFLOP/s](../numbers.md#phys-h100-fp8), a factor of [2](../numbers.md#phys-fp8-over-bf16). FP8
training at scale is in production: DeepSeek-V3's report says "we introduce an FP8 mixed precision
training framework and, for the first time, validate its effectiveness" on "an extremely large-scale
model" (section 1) [@deepseek2024v3]. For an FP8 run the floor is half the stated bound, about 800
H100 chips (our arithmetic). Part II's L1 counts compute "at a reference precision, so that a switch
of precision cannot game a threshold"; the floor is exactly what a precision switch games. One line:
compute the bound at the lowest precision a run can use.

**C8.2. The falsifier C8(b) cannot fail.** Severity: serious. C8(b) says every facility channel's
margin exceeds one for a distributed 1e25 FLOP run, and E8 supports it with a margin of at least
[1.4](../numbers.md#e8-distributed-1e25-margin-min) in every draw. On one-node sites a facility channel
sees one node, [29 kW](../numbers.md#phys-node-power), "whatever C is" (E8's own note), far below
every facility limit by construction. The claims file concedes "close to definitionally". A claim
that no possible measurement in E8 could refute is not a result. One line: cut (b), or replace it
with a channel that sees the sites together.

**C8.3. T belongs to the adversary.** Severity: serious (acknowledged). The floor scales as 1 / T.
T is "the longest sensible run under prevailing growth rates", an economic argument about a party
optimising cost; a party racing for a decisive advantage under a pause is not bound by it. A covert run
twice as long as [24 months](../numbers.md#phys-rahman-run-pause) halves every floor. One line: state
the floor at the longest run any party could choose.

**C8.4. "Only chip accounting sees the aggregate" is false as stated.** Severity: minor. A
distributed run over sites must exchange model-sized updates across all of them; that traffic, and
the money and power purchases behind it, are aggregate signatures. E8 models none. This attack helps
the regime, but it is a counterexample to "only".

**C8.5. Two bounds, and a pool nobody counted.** Severity: minor. The formal file's bound uses full
utilisation; E8's uses [76%](../numbers.md#phys-pope-mfu-prefill), a vendor figure for inference
prefill, not training; the shrink factor [470](../numbers.md#e8-pool-shrink-1e26-pause) uses the
latter (at full utilisation it would be about 625, our arithmetic). The pool of
[1,000,000 chips](../numbers.md#phys-chips-unaccounted) is an assumption, and E8's spread around it is
"our reading". C8(c)'s direction is robust (the smuggled stock exceeds the floor in E8's 5th
percentile draw), so no verdict moves.

## C9

**C9.1. P2 is a property of the powered-time counter, not of the height clock.** Severity: serious.
Proposition 9.1 bounds a chip's run under one licence by (L + s) / rho_min of counter time "whatever
headers it is fed". Against a holder who wants to run, that bound is reached by keeping the chip
offline or feeding old headers at the floor rate, and it is the bound a licence that simply said "run
for so many powered hours" would give, with no Bitcoin at all. That counter is prior work: the formal
file and Part II cite flexHEG's cycle counters and their idle-chip weakness. The height clock adds a
calendar expiry only for a chip that keeps receiving honest headers, that is, for a compliant holder.
So for the response role Part II gives it (a refused holder), the height clock adds nothing to the
counter. One line: claim P2 as the counter's, and the height clock only for online expiry.

**C9.2. Forged headers can end licences early.** Severity: serious. The chip keeps h_max, "the
greatest valid height it has seen (never decreasing)", and accepts a header if its hash meets a
minimum work Z. If any valid header raises h_max, a fork of one licence period's worth of headers at
work Z, fed to a chip, ends its licence at once, and the chip stays stopped after it sees the honest
chain. Z must sit below the lowest honest difficulty over the licence's life, since honest difficulty
can fall and a Z above it would stop compliant chips; so such a fork costs less than the same number
of honest blocks, by that margin. The formal file says forged headers "gain nothing" against
Proposition 9.1; they gain nothing for stretching a licence, but they make the off switch a weapon in
anyone's hands who can reach a chip's header feed (a cloud operator, a rival with access). If instead
h_max counts only the most-work chain, an offline chip accepts whatever chain it is fed. The model is
ambiguous between the two. One line: specify which heights count, and price early stopping.

**C9.3. Data availability makes the log operator a trusted party.** Severity: serious. P4 holds only
under (A9.4), "every leaf behind every anchored root is published". The regime's remedy is to "treat a
log that withholds any leaf as having licensed every chip". That is not enforcement: it lets whoever
withholds a leaf void every non-issuance proof at once. P4 thus trusts the log operator's publication,
in a design whose section heading is "Verification without a trusted party". One line: name the log
operator as trusted for availability, or replicate the log under rival operators.

**C9.4. One secure element, every chip.** Severity: serious (the claim's strongest objection,
acknowledged, unanswered). (A9.3) fails for every chip at once if one trust anchor breaks; Part II
cites a cheap interposer that broke the attestation confidential computing trusts.

**C9.5. Minor points.** The rate floor's cost to compliant chips (112 of 649 honest runs stopped
early) is at the check's random settings, not at Bitcoin's real distribution of block intervals. P1's
threat (licences signed in advance) gains little anyway once licences end at a height. E25 has not
run, and no prototype exists.

## C10

**C10.1. The endpoint cannot warn.** Severity: serious (the claim's own first L4 objection,
unanswered). D1 fires when a system already beats an institution; near the line, elicited scores are
lower bounds (C5.3). As a definition C10 can stand; as anything the protocol acts on before the
endpoint, it cannot.

**C10.2. "Only 3 clusters have any human comparison in public data" is a count of what the code
chose.** Severity: serious for the sentence, minor for the conclusion. The
[3 clusters](../numbers.md#e1-clusters-baselined) is the length of a dictionary of three entries
written into `e01_capability_compute.py` (`won`, and `len(won)` for the number). The archive E1 itself
loads has a Cybench table with a column giving, in minutes, the human first-solve time of the hardest
task each model solved, and METR's time horizons are measured in
human time: "the time humans typically take to complete tasks that AI models can complete with 50%
success rate" (abstract) [@kwa2025horizon]. C10's own evidence cites RE-Bench's human experts at
matched time. So AI research and cyber have human comparisons. "None is an organisation at matched
budget" stands. One line: replace the count with a search, or reword it.

**C10.3. "Matched budget" is two different matches.** Severity: minor. Matched money gives the system
as many parallel copies as the money buys; matched wall-clock time gives the organisation its fixed
headcount. RE-Bench's ratio moves [8](../numbers.md#cog-rebench-swing)-fold with the budget, so the
verdict depends on which match and which budgets are tested, and t* as "the largest tested crossing"
is set by the grid of budgets chosen.

**C10.4. A system decisive in one cluster may not be D1.** Severity: minor. D1 needs wins in a
fraction alpha of K clusters. A system decisive in AI research alone, the cluster that feeds the loop,
or in cyber alone, can stay below D1. C4 covers AI research, so the gap is narrower than it looks.

**C10.5. Status.** Minor. C10(b) and C10(c) are untested; E21 has not run.

## C11

**C11.1. A gate can approve everything, and the audit can be recognised.** Severity: serious. Closure
is "the share of increments obtained without a logged human-held gate". A gate that logs an approval
for every request measures as closure 0 while being closure 1 in substance. The audit is seeded
requests "a working gate must refuse"; an AI system operating the pipeline, or a developer, can learn
to tell seeded requests from real ones and refuse only those. The logs are the developer's. One line:
say what makes a seeded request indistinguishable, or downgrade the audit.

**C11.2. The combination rule's inputs have no shown measurement.** Severity: serious. Theorem 11.2's
e_i is an elasticity of an input to the stock; D6's e_i is a share of increments without a gate. The
formal file flags that "reading one as the other is for E4(d) to check". Until then K = (lambda / b)
times the sum of s_i e_i relates quantities nobody can measure in the form the theorem uses.

**C11.3. Under the safe bound C11 adopts, the decomposition reduces to prior work.** Severity:
serious. Until E4(d) decides, the claim uses (lambda / b) times the largest closure among ungated
inputs, and Part II concludes "L3 gates every highly closed input together". That is holding every
input together, which the claims file credits to prior work. Per-input closure changes no rule until
E4(d) shows which production function holds; by the claim's own test it is framing until then.

**C11.4. The gates are spaced in the wrong unit.** Severity: serious. Part II spaces gates by the 80%
time horizon, about [3 hours](../numbers.md#dyn-horizon-p80-hours) now and about
[22 hours](../numbers.md#path-horizon-p80-next-year) in a year, so that an agent cannot "cross between
them unattended". The horizon is measured in human time: the time humans take on tasks the model
completes (abstract) [@kwa2025horizon]. Gates are spaced in wall-clock time. An agent that finishes a
human's three-hour task in minutes can chain several such tasks between gates three wall-clock hours
apart. One line: space gates by the agent's own wall-clock time on horizon-length tasks.

**C11.5. Status.** Minor. C11(b), the narrow-optimiser rule, is definitional until E4(e) runs.

## C12

**C12.1. Only nine of twenty-one pairs are fixed by the evidence, and the top of the order is not
among them.** Severity: serious. The claim's L4 plan asks first for the Pareto-ordered pairs. Reading
the ranking table's own qualitative entries on the three criteria (shortens T_b; hard to see; cheap to
limit, where cheaper ranks higher), the pairs one pathway leads on every criterion are: every pathway
over long-horizon autonomy (six pairs), and self-improvement, undeclared compute and distillation over
continual learning (three). Not ordered by the evidence:

- Undeclared compute over declared scaling: scaling shortens T_b more; undeclared compute is harder to
  see.
- Anything over self-replication: self-replication's limit is the cheapest ("Very low"), so on
  criterion 3 it leads every other pathway, and a reading that weights cost puts it first.
- Declared scaling against distillation, and self-replication against continual learning (named by
  the chapter as weak).
- Self-improvement against declared scaling, which turns on whether criterion 1 means today or the
  tail.

One line: publish the Pareto pairs and mark every other order as judgement.

**C12.2. Criterion 3 mixes how dangerous a pathway is with how easy it is to restrict.** Severity:
serious. A ranking "by effect on the line" should not rise because a limit is cheap. Under the stated
criteria, a pathway that does little to T_b but costs nothing to forbid outranks one that shortens T_b
a great deal but is costly to limit. The rank then answers "what should we restrict first", which is
Part II's question, not "what leads to superintelligence", the brief's. One line: rank on effect and
visibility, and use cost only for the response class.

**C12.3. The tie at the top joins two sides of the line with no common unit.** Severity: serious.
Criterion 1 is defined on T_b. Undeclared compute "lengthens T_r", and on T_b alone it is weak: the
smuggled stock at fixed algorithms needs [555 years](../numbers.md#prot-pool-years-fixed) to reach the
one published budget. The tie is a judgement that a T_r effect equals a T_b effect, on no scale.

**C12.4. The refuter for undeclared compute could hardly fire.** Severity: minor. The stated refuter
is E5 "giving a discovery rate near the memo's placeholder", which is
[12.8](../numbers.md#e5-memo-over-hazard) times the fitted rate. A test that needs a thirteen-fold error
to fail is weak evidence when it passes.

**C12.5. E1's premise check uses a sample without the frontier.** Severity: minor. C12 leans on E1's
[36%](../numbers.md#e1-compute-share), from a sample that is mostly open weights and drops the top
models (C2.3); the closed-model subset gives 63% (our rerun). Part II meanwhile says compute explains
[80%](../numbers.md#comp-mertens-frontier-share-lo) to
[90%](../numbers.md#comp-mertens-frontier-share-hi) of differences at the frontier. The premise is
unsettled in both directions.

**C12.6. Minor points.** C12(b) is new relative to the project's own memo, which is not a claim about
the literature. Necessity cannot be shown before D1 exists (acknowledged).

## The protocol

**P1. Licence lapse is not a response set by design.** Severity: fatal for Part II's second footing
as stated. Part II: "A chip that stops on its own is the only response whose time is set by design".
Its deadlock rule makes a refusal require a finding by k of n licensors from rival blocs (C1.5). That
is the same kind of decision as an IAEA Board finding or a Security Council referral, whose latencies
E24 measured: formal statements a median of
[60 days](../numbers.md#e24-statement-median-days), up to
[1,102 days](../numbers.md#e24-statement-max-days), and some findings never acted on. The protocol's
own illustration of T_r leaves the decision time out. On Part II's own rules, the declared path's
T_resp waits on politics, which is what C1's downgrade says no path may do.

**P2. "Verification without a trusted party" trusts at least three.** Severity: serious. The design
trusts the chip maker's secure element for every chip (one anchor, and a vendor on record against
kill switches), the log operator for data availability (C9.3), and an honest majority of Bitcoin's
hash power for P1 and P3. It also trusts the beacon that draws inspections: if that beacon is block
hashes, a miner can discard a block whose hash selects an inspection it wants to avoid, at the cost of
the block's reward. One line: list the trusted parties and what each can break.

**P3. Nothing in the protocol closes the pool.** Severity: serious. The first footing is "the covert
pool can be closed". The mechanisms are a registration window, completeness checked against makers'
records, and contraband status afterwards. Makers' records count chips made, not where the unregistered
ones went; the pre-regime stock "registers only voluntarily" (Part II's failure table); and finding
contraband needs the channels E5 says take decades. So the pool shrinks only as its chips wear out,
while algorithmic drift raises what each remaining chip can do. Part II concedes that if the pool
cannot be closed "the protocol binds only parties that choose to declare"; it offers no mechanism by
which it can be.

**P4. Compliance cannot change a party's classification.** Severity: serious. While the pool is open,
every party fails the line through the pool path, whatever it declares (C1.2). A regime that classifies
compliant and non-compliant parties alike cannot reward compliance through the line, and its promise
that useful AI "stays allowed and keeps improving" fails today by its own rules, not only in the
future case Part II names ("Precaution compounds").

**P5. One trust anchor carries the off switch, the evaluations and the location checks.** Severity:
serious. Fine-tuning elicitation "needs the weights or a trusted enclave"; licences, attestation and
location verification rest on secure hardware of the same kind. One break would at once stop the
regime from seeing capability and from stopping chips. And evaluation with weight access by rival
states raises the weight-theft risk Part II calls a gap.

**P6. The loop-gain rule is the ban, for now.** Severity: minor. "Until E4 can estimate K for a real
system, closed-loop training research on a frontier-scale system is treated as above the trigger."
That is the prior-work ban; C4 adds nothing operational until E4(b) runs, and C4.1 suggests it may add
nothing after.

**P7. Costs are labelled low where the work says they are not.** Severity: minor. L2's cost is "Low;
diplomatic for host states", while Part II's own section on who it binds shows the controlling state
reversing its own export rule within months and ASML selling
[33%](../numbers.md#org-asml-china-units-2025) of its lithography tools by unit to China.
A rule the chokepoint holders reject is not low-cost to keep.

**P8. Hand-typed numbers.** Severity: minor. Several ledger links in Part II show text the model does
not compute: "0.92 years" for `e24-halt-median-if-halted-years` (the model shows 0.9 years), "7,900"
for `e5-td-ratio` (7,935), "475" for `e8-pool-shrink-1e26-pause` (470), "0.15/yr" for `e5-hazard-hi`
(0.147/yr), and "38" and "52" for the organism counts. The rule is that no document types a model
number. `make docs` would rewrite them; it has not been run. `data/numbers.json` is also stale: it
lacks the E1, E4, formal and protocol ids, so `make check` would fail on unknown numbers.

**P9. The main adversary is outside.** Severity: serious (acknowledged, unanswered). A major power with
its own chip chain, inside or outside the regime, faces "deterrence only" on Part II's own account,
and C7.6 says the same of coalitions that include one. The protocol prevents breakouts by the parties
least able to make them.

## What was checked and found sound

The formal file's Lemma 1.1, Propositions 1.2, 1.4 and 1.6 and Corollary 1.3; Theorem 2.1; Theorems
3.1 and 3.3 and Corollary 3.4; Lemma 4.1 (exact for any closure, not only e = 0), Corollary 4.1a and
Propositions 4.3 to 4.5 (4.5 holds even when estimates fall below zero, since on the coverage event
every bound is at least its factor); Theorems 5.1 and 5.2; Theorems 6.2 and 6.4 (the similarity
M = D K D^-1 and the Jensen step are correct); Theorem 7.2's algebra; Theorem 8.1; Proposition 9.1
(h_max never decreasing stops forks from stretching a licence); Theorem 11.2 under its single-return
model; Propositions E.3 and E.4. E1's join, units, out-of-sample split and reproduction of Ho et al.
(their bootstrap reproduces their published halving time); E4(a)'s record parsing and AI-credit coding;
E5's date rules and fit arithmetic; E24's counts ([13 findings](../numbers.md#e24-halt-findings-all) in
the halt analysis, six never halted, seven halts, five reversed); E8's floors. Every experiment with results reproduces exactly from its script.

## Verdicts

| Claim | Most severe attack | Severity | Verdict |
|---|---|---|---|
| C1 | C1.5: under Part II's deadlock rule no path has a response free of a political decision, so (c) has an empty domain; C1.1, C1.2 and C1.4 break (a) and (b) as stated | Fatal for (c); serious for (a), (b) | Survives with corrections ((c) cut; the per-path form and the beta guarantee corrected) |
| C2 | C2.2 and C2.3: E1's own fit has drift falling with scale, breaking the monotone interval, and its rate moves over three orders of magnitude with the sample | Serious | Survives with corrections |
| C3 | C3.1: the declared path's 1.5 days extrapolates a one-day figure the source does not extend; C3.2: the L3 support for (b) cannot fail | Serious | Survives with corrections |
| C4 | C4.1: at the only data-calibrated noise the trigger fires about as often below 1 as above it, which Part II's own rule says cuts it | Serious | Fails as a trigger on current evidence; reopens only if E4(b) measures far tighter rounds |
| C5 | C5.1 and C5.2: a population rate measured on organisms blind to E does not bound a strategic developer who sees E | Serious | Survives with corrections (valid only against non-adaptive hiding inside the sampled population) |
| C6 | C6.1: with unmeasured, self-reported edges the certificate carries no probability | Serious | Survives with corrections |
| C7 | C7.1 and C7.2: coalition-proofness holds only where rewards exceed beta times a decisive advantage, a region the work calls empty; the claims file drops the conditions | Serious | Survives with corrections ((b) and (c) downgraded) |
| C8 | C8.1: the bound is computed at BF16 while FP8 training halves the floor; C8.2: (b) cannot fail | Serious | Survives with corrections ((b) cut as tautological) |
| C9 | C9.1: P2 is the powered-time counter's property, not the height clock's; C9.2: forged headers stop chips early | Serious | Survives with corrections |
| C10 | C10.1: the endpoint cannot warn; C10.2: the "3 clusters" count is hard-coded | Serious | Survives with corrections (as a definition only) |
| C11 | C11.3: under the safe bound the decomposition reduces to holding every input together, which is prior work | Serious | Survives with corrections, as framing until E4(d) |
| C12 | C12.1: only nine of twenty-one pairs are Pareto-ordered, none at the top | Serious | Survives with corrections (as a judgement) |

```toml
[source.furlanello2018born]
type = "peer-reviewed"
title = "Born Again Neural Networks"
authors = "Tommaso Furlanello, Zachary C. Lipton, Michael Tschannen, Laurent Itti, Anima Anandkumar"
year = 2018
arxiv = "1805.04770"
opened = "2026-11-27"

[source.burns2023weak]
type = "preprint"
title = "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision"
authors = "Collin Burns, Pavel Izmailov, Jan Hendrik Kirchner, Bowen Baker, Leo Gao, Leopold Aschenbrenner, Yining Chen, Adrien Ecoffet, Manas Joglekar, Jan Leike, Ilya Sutskever, Jeff Wu"
year = 2023
arxiv = "2312.09390"
opened = "2026-11-27"

[source.deepseek2024v3]
type = "preprint"
title = "DeepSeek-V3 Technical Report"
authors = "DeepSeek-AI"
year = 2024
arxiv = "2412.19437"
opened = "2026-11-27"
```
