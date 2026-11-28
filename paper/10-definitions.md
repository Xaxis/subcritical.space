# What superintelligence is: six definitions

A prohibition needs a thing to prohibit. Neither the Statement on Superintelligence nor the Global
Call for AI Red Lines defines its line operationally [@fli-superintelligence-statement;
@redlines-2025], and Anthropic found its own pre-set capability levels "far more ambiguous than we
anticipated" [@anthropic-rsp-v3-announcement-2026]. Precision matters to compliance itself. In
Barrett and Dannenberg's experiment, groups facing a known catastrophe threshold avoided it in
[8 groups](../research/numbers.md#def-bd-known-avoided) of
[10 groups](../research/numbers.md#def-bd-groups); when its location was uncertain, catastrophe was
certain in [9 groups](../research/numbers.md#def-bd-uncertain-catastrophe) of
[10 groups](../research/numbers.md#def-bd-groups), and the tenth, which left itself a chance of
escape, still crossed the threshold [@barrett2012climate]. A line the parties dispute behaves like
an uncertain one.

A trigger must be measurable early, which a definition by harm is not [@ca-sb53-analysis-2025;
@scher2025agreement]; hard to game, which training compute, "only a very crude proxy for risk"
[@heim2024thresholds], and a score a model can depress both fail in part; and verifiable among
rivals, which a threshold the measured party judges is not [@anthropic2026rsp; @gdm-fsf-v3-1-2026].
To capability and risk thresholds [@koessler2024risk] these definitions add one in time. None is new
at its core, "not found" is a claim about our search, and none has been tested against a real
adversary.

## D1. Superintelligence, the endpoint

**Definition.** A system S with resources R is superintelligent at level alpha on a battery B if, in
at least a fraction alpha of the N_d decisive clusters (AI research, cyber operations,
weapons-relevant science, persuasion and strategy, economic production), its elicited score (D5)
beats that of a named organisation O_k for cluster k, both given wall-clock time t_k and a money
budget psi_k, on a refreshed battery the regime holds and S's developer has not seen, with O_k's
tools frozen at a declared vintage [@genewein2026agiasi]. Verdicts flip with these parameters, as
RE-Bench's lead passes from agents to experts as the time budget grows [@wijk2024rebench]. The
crossover budget t*, the largest tested budget at which S matches O_k, is censored where S wins at
every budget tested, and never extrapolated.

**Test.** D1 passes if its verdict survives a change of organisation within its class and the
fraction won rises smoothly with effective compute. Public data cannot test that: E21 met no
institution in the [3 clusters](../research/numbers.md#e21-clusters) with a public comparison. On
MLE-bench the verdict depends on the rank named, the best entry beating the median entrant in
[71.1%](../research/numbers.md#e21-mle-median-best) of competitions and the gold threshold in
[25.8%](../research/numbers.md#e21-mle-gold-best), and t* rises only while a battery's baselines
last.

**Prior work.** Comparison with organisations at matched time and cost [@genewein2026agiasi;
@ngo2023tagi; @anthropic2026rsp; @openai2025preparedness] and a human-AI crossover
[@wijk2024rebench; @robinson2026horizons] are prior work. Not found, so D1 extends it narrowly: time
and money matched together against a named organisation, on a regime-held battery across clusters,
with alpha and a censored t* (C10). D1 cannot warn, holding only once a system beats an institution.

## D2. Loop gain

**Definition.** A round is one research cycle at fixed compute, data and time, run by the system the
previous round produced, with capability on a log compute-equivalent axis. D2 measures K, which
exceeds 1 exactly when the loop compounds with the human-held inputs fixed, not the ratio of
successive gains, which tends to 1 below criticality and so would in time trip any threshold below 1
(Part III). An exact round identity gives b, the returns exponent, and runs at one, two and four
times the agent budget give lambda, the return to input; K is their ratio times the closure (D6).

**Test.** Staged runs, with the agent elicited since it can sandbag [@gasteiger2025subtlesandbag].
E4 simulated the rule that restricts while K's upper bound exceeds a placeholder margin of
[0.90](../research/numbers.md#e4-gstar), at the only noise calibrated on data, a human speedrun's
record-to-record spread. On a loop well below 1 it fired in [88%](../research/numbers.md#e4-k-fa-n5)
of runs after 5 rounds at each of three budgets, and on a loop at the corrected 95th percentile only
[2%](../research/numbers.md#e4-k-fire-gap-n5) more often. The trigger fails at that proxy and is
untested at real round noise, so the prior-work ban on closed-loop training research at frontier
scale decides [@miotti2025narrowpath].

**Prior work.** The condition, its threshold and its use as a trigger [@cunningham2026rsi;
@burtsev2026criticality; @yudkowsky2013iem; @anthropic2026rsp; @openai2025preparedness], the rule on
a reproduction number's upper bound [@blumberg2020supercritical], repeated measurement against error
bias [@ashenfelter1992twins], a public harness [@zhao2025speedrun] and a staged test of an AI
research loop [@srikanth2026aide2] are prior work. What extends it, narrowly (C4), is the round
identity and budget ladder as a design for measuring K, whose interval under-covers at the
calibrated noise.

## D3. Breakout time

**Definition.** For a party with holdings H (chips, weights, data, human and AI research labour),
T_b(p) is the shortest time on path p to accumulate the effective compute C* agreed to reach D1:
physical compute times algorithmic efficiency, which grows with research labour (D2) and depends on
scale. Each path (own fleet, cloud, purchase, smuggling, distillation) is computed and the minimum
taken. C* cannot be measured before someone reaches D1, so it is a convention, as IAEA conversion
times are [@iaea-glossary-2022]. T_b inherits all its uncertainty: one OOM of C* moves T_b by
[2.3 years](../research/numbers.md#comp-years-per-oom-ho) at Ho et al.'s central rate, more than
Part II's illustrative line of [2.0 years](../research/numbers.md#prot-line-declared). D3 also
assumes, without evidence, that effective compute is one scalar across training, inference,
post-training and distillation.

**Test.** Compute for fixed language-model performance halved every
[8.4 months](../research/numbers.md#def-ho-halving-months) from 2012 to 2023 [@ho2024algorithmic],
but the largest gains need scale [@gundlach2025origin], and E1 found the drift rate unidentified on
public data, from [2.6](../research/numbers.md#e1-algo-annual-subset-min) to
[1,512](../research/numbers.md#e1-algo-annual-subset-max) a year across samples, so no interval can
be tabulated. D3's stated backtest has [0 days](../research/numbers.md#e18-oc-evaluable-days) of
public data to run on; E18's substitute bears against a constant rate.

**Prior work.** Breakout time is arms-control vocabulary [@sastry2024compute], defined for AI
[@barnett2025governance], computed from holdings [@miotti2025narrowpath; @fithian2026hardwired] and
from a calibrated model [@gan2026clock], with additive accounting of post-training, inference and
distillation [@pistillo2025loopholes] and the span a cheap verifier opens [@villalobos2023tradeoff].
D3 combines prior work and stays as accounting, claiming nothing (C2).

## D4. Weapons-grade: the line

**Definition.** A holding H is inside the line, weapons-grade in the definition's name, if on some
path p

T_b(p) < m * T_r(p), with T_r(p) = T_d(p) + T_resp(p),

in years. T_d(p) is the time by which the regime's channels on p detect a breakout with probability
at least 1 - beta, beta being the tolerated chance that it succeeds; T_resp(p) runs from a confirmed
finding to an effective halt, or is a high quantile of that time; the margin m, at least 1, covers
estimation error. A holding outside the line on every path is useful AI and may keep improving
through human-held gates (D6). The name marks a position in a race between two clocks, not a material property, as enrichment is, nor a verdict on capability; on today's
inputs it labels every party.

Where progress can move between paths, as a checkpoint can, the safe test sets the shortest T_b
against the longest T_r, and beta bounds one attempt, so attempts must be bounded. The line can be
evaluated today only on the declared path, with illustrative inputs: the untraced chip pool puts
every party inside it, and every party able to rent compute or query a stronger model is inside it
through cloud and distillation, which have no measured channel. If T_b and T_r err unsafely by
factors e_b and e_r, a margin m >= e_b * e_r keeps the guarantee per attempt (Part III); no margin
covers error in C*.

**Measurement.** T_d comes from the channels, with the evader choosing the path that minimises
detection [@baker2025verifying]. E5 puts it at
[39.0 days](../research/numbers.md#e5-td-declared-days) on the declared path, a design figure. On
undeclared paths its figures are central estimates under a transfer from covert weapons programmes,
not bounds or measurements: for a path only the historical channels see,
[32 years](../research/numbers.md#e5-td-hist-years) at a constant rate and
[24 years](../research/numbers.md#e5-td-weibull-years) under the Weibull fit. They assume detection
does not depend on how fast or intensely a party breaks out, though a breakout's footprint grows
with its speed: a guarantee that a path is stopped holds as a one-sided bound where the hazard used
is a lower bound, but a verdict that a path fails the line may not. In E24,
[25%](../research/numbers.md#e24-halt-share-never) of in-treaty findings were not followed by a halt
within what the sources cover, one censored, so the 95th percentile is not reached within follow-up;
the fastest halt took [64 days](../research/numbers.md#e24-halt-min-days), the fastest exit
[31 days](../research/numbers.md#e24-exit-min-days). A halt waits on rival states' political
decision, which no drill times.

**Evidence.** In Gan's model, prevention at a tolerance of
[5%](../research/numbers.md#def-prevent-beta), this work's choice and not Gan's calibration, needs
[7.8](../research/numbers.md#def-gan-prevent-multiple) times the monitoring that deters, on our
arithmetic, and over his window [4.5](../research/numbers.md#prot-gan-prevent-over-consent) times
the most his parties consent to, [0.056/month](../research/numbers.md#prot-gan-consent-rate)
[@gan2026clock]. Prevention near the line, chosen because the endpoint is irreversible, is a design
choice the only calibrated model cited does not support.

**Prior work.** Timely detection per adversary path, with a measured response time and a margin, is
nuclear physical-protection practice from 1977 [@snell2007itc20] and Nitze's 1988 standard
[@hafemeister2008ctbt]. IAEA timeliness goals imply a margin of at most
[1.00](../research/numbers.md#def-iaea-m-irr-high) and time detection only [@iaea-glossary-2001;
@iaea-glossary-2022; @cochran-2005]. In AI the line is stated in words [@barnett2025governance],
underlies deterrence by sabotage [@hendrycks2025superintelligence], appears as a formula, Gan's
prevention condition at m = 1 under Poisson detection [@gan2026clock], and is applied per route
[@miotti2025narrowpath; @fithian2026hardwired]. The margin as an error budget is the partial-factor
format of structural design (EN 1990), in which load and resistance factors multiply into the
overall margin [@jrc2008eurocodes]. D4 is prior work applied; ours (C1) is the application to AI
holdings.

## D5. Elicited capability, robust to hiding

**Definition.** For thresholds, a system's capability is its score after a named elicitation
protocol E (methods at stated budgets, from fine-tuning to methods on the weights), run by the
regime's evaluators with weight access or in a trusted enclave. E carries a miss rate, the share of
model organisms with hidden capability above the threshold that E leaves below it, and a false-alarm
rate, the share of benign models it lifts over. The guarantee covers only where E's methods work,
hiding that does not adapt to E, and the population sampled.

**Test.** Naive locks yield to a few demonstrations [@greenblatt2024password;
@taylor2025auditinggames]; hardened ones do not [@finke2026robustorganisms]. Elicitation also lifts
benign models [@taylor2025auditinggames]. Above expert level there are no demonstrations, so the
guarantee weakens toward D1; and at any level a frontier model's hiding, emergent or trained, is not
drawn from the regime's organisms on small open models. E3, which would measure both rates, has not
run, so D5 is an untested design. It fails if no affordable budget brings both rates below stated
targets on RL-locked organisms.

**Prior work.** Thresholds on elicited capability [@anthropic2023rsp; @openai2025preparedness;
@gpai-code-of-practice-2025], a fixed budget [@anthropic2023rsp] and the statistics of diagnostic
tests [@fda2007diagnostic] are prior work, and the closest work already compares elicitation methods
on password-locked and circuit-broken organisms [@hofstatter2025elicitationgame]. What extends it
(C5) is both rates per named budget over a defined population, as a pass-fail rule among rivals.

## D6. Closure

**Definition.** For each input to the next model (compute, weights, data, research labour, money,
transfers between parties), closure is the share of increments, in the input's own unit, obtained
without passing a human-held gate whose passage is logged and verifiable, such as licence renewal or
approval of training launches. A narrow system feeding a covered one counts as part of it. In the
loop's exponent closures add, weighted by input shares, as in the task-based model of automation
[@aghion2017ai]: under complements the least-closed input sets the gain, under substitutes the
most-closed (Part III). That theorem treats closure as an elasticity, while D6 defines it as a share
of ungated increments; reading one as the other is for E4(d) to check. Until it does, the safe bound
takes the largest closure among ungated inputs.

**Test.** By audit, with seeded requests that a working gate must refuse; gates on research labour
rest on a developer's self-report [@anthropic2026pace]. The gates hold for now: models still fail
identity checks [@black2025replibench], though success on simplified self-replication tasks is
rising [@aisi2025trends]. E4(d), not yet run, tests whether the gain under a set of gates follows
from closures measured one gate at a time; if not, closure by input is framing.

**Prior work.** Closure as the share of gain surviving the pipeline, which D6 decomposes
[@burtsev2026criticality], loops classed by closure [@chen2026rsisurvey], a ban on AI building AI
[@miotti2025narrowpath], unauthorised self-improvement as a red line [@redlines-2025], and gating
every input together, the rule under that bound [@scher2026research], are prior work. What extends
it, narrowly (C11), is closure input by input against verifiable gates.
