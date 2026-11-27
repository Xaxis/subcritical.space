# What superintelligence is: six definitions

A prohibition needs a thing to prohibit. The Statement on Superintelligence calls for one and gives
no operational definition [@fli-superintelligence-statement], and the Global Call for AI Red Lines
leaves its lines to later dialogue [@redlines-2025]. The frontier frameworks that do set thresholds
found pre-set capability levels "far more ambiguous than we anticipated"
[@anthropic-rsp-v3-announcement-2026]. Precision matters to compliance itself. In Barrett and
Dannenberg's experiment, groups facing a known catastrophe threshold avoided it in
[8 groups](../research/numbers.md#def-bd-known-avoided) of
[10 groups](../research/numbers.md#def-bd-groups); when its location was uncertain, catastrophe struck
in [9 groups](../research/numbers.md#def-bd-uncertain-catastrophe) of
[10 groups](../research/numbers.md#def-bd-groups) [@barrett2012climate]. A line the parties dispute
behaves like an uncertain one.

A definition usable as a trigger must be measurable before it is too late, which rules out
definitions by harm [@ca-sb53-analysis-2025; @scher2025agreement]; hard to game, which training
compute, "only a very crude proxy for risk" [@heim2024thresholds], and capability scores a model can
depress both fail in part; and verifiable by parties who distrust each other, which thresholds judged
by the measured party are not [@anthropic2026rsp; @gdm-fsf-v3-1-2026]. Beside capability and risk
thresholds [@koessler2024risk], the definitions below add a threshold in time. D1 is the endpoint. D3
and D4 are the line: how fast a holding could reach the endpoint, against how fast the regime could
stop it. D2, D5 and D6 are measurements that feed breakout time, and an ungated input (D6) is an
unmetered resource. None of the six is new. Each label is the independent search's, and "not found"
is a claim about our search, not about the world.

Table: The six definitions, their labels after the prior-art search, and the claims they carry {#tab:definitions-standing}

| Definition | What it measures | Label | Claim and standing |
|---|---|---|---|
| D1 the endpoint | Clusters won against a named organisation at matched time and money | Extends prior work, narrowly | C10: downgraded to a definition |
| D2 loop gain | The gain K of a research loop at fixed inputs | Extends prior work, narrowly, for the estimator | C4: downgraded to a measurement design; the trigger cut |
| D3 breakout time | Years to reach the agreed effective compute, per path | Extends prior work, as a combination | C2: candidate; (a) cut, (b) and (c) untested |
| D4 the line | T_b(p) < m * T_r(p) on some path | Prior work, applied | C1: application; (c) cut |
| D5 elicited capability | Score after a named elicitation, with miss and false-alarm rates | Extends prior work | C5: candidate, against non-adaptive hiding only |
| D6 closure | Share of each input obtained without a logged human-held gate | Extends prior work, narrowly | C11: downgraded to framing until tested |

## D1. Superintelligence, the endpoint

**Definition.** A system S with resources R is superintelligent at level alpha on a battery B when
B spans the decisive clusters, each with a published baseline set by a named human organisation; B
is held by the regime, refreshed, and unseen by S's developer; and S with R (compute, money, copies
and wall-clock time T) beats the organisation, given the same T and the same money, in at least a
fraction alpha of the clusters. The cognitive perspective names five clusters: AI research, cyber
operations, weapons-relevant science, persuasion and strategy, and economic production. T, the
organisation, its technology vintage [@genewein2026agiasi] and the rule for matching budgets must
all be stated, because verdicts flip with them: on RE-Bench the best agents scored
[4](../research/numbers.md#def-rebench-agent-advantage) times as high as experts at
[2 h](../research/numbers.md#def-rebench-short-budget), and the experts scored
[2](../research/numbers.md#def-rebench-human-advantage) times the best agent at
[32 h](../research/numbers.md#def-rebench-long-budget) [@wijk2024rebench]. The crossover budget t* is
the largest tested budget at which S matches the organisation at equal compute and money, censored
if S wins at every budget tested, and never extrapolated.

**Measurement and test.** Only an evaluator with access to S and a held-out battery can measure D1,
on elicited capability (D5). The test scores public models along a capability ladder at matched time
and money; D1 passes if changing the organisation within its class does not flip the verdict and the
fraction won rises smoothly with effective compute. Public data cannot run it: E1 found
[5 clusters](../research/numbers.md#e1-clusters-baselined) with any human comparison and
[3 clusters](../research/numbers.md#e1-clusters-verdict) with a bar a model wins or loses, none of
them an organisation at matched budget, so the baselines must be built first.

**Label.** Extends prior work, narrowly. Comparison with organisations, copies and speed, matched
wall-clock time and matched cost are prior work [@genewein2026agiasi; @ngo2023tagi;
@anthropic2026rsp; @openai2025preparedness], and so is a crossover budget between human and AI
[@wijk2024rebench; @robinson2026horizons]. Not found: time and money matched together inside a
definition, on a refreshed, regime-held battery with institutional baselines across several
clusters, with an alpha fraction and a censored t*. The red team reduced this claim (C10) to a
definition. D1 holds only once a system already beats an institution, so it cannot warn. It is what
breakout time measures the distance to, not a trigger.

## D2. Loop gain

**Definition.** Capability is measured on a log compute-equivalent axis. A round is one research
cycle at fixed experimental compute, data and wall-clock time, run by the system the previous round
produced. The ratio of successive gains is not a stable parameter: below criticality it tends to 1,
so a threshold on it below 1 would in time fire on every such loop (Part III). D2 measures instead K,
the loop's gain in the dynamical perspective's growth law, which exceeds 1 exactly when the loop
compounds with the human-held inputs fixed. An exact round identity relates consecutive gains to the
returns exponent; repeating the run at one, two and four times the agent budget, the budget ladder,
estimates the return to input; K follows from the two. Scoring each round on two independent
held-out sets was meant to remove the bias one noisy set puts toward a loop below 1, and E4 found
that it does not: where the noise is error in measuring a round's gain, a second set turns a median
estimate of [0.57](../research/numbers.md#e4-diff-bias-meas1) times the true return into one of
[8.11](../research/numbers.md#e4-diff-bias-meas2) times it, and where the noise is real variation, a
second set cannot help.

**Measurement and test.** Staged runs at fixed inputs on declared checkpoints, which a regime
evaluator can run on a public harness [@zhao2025speedrun], with the agent elicited because it can
sandbag [@gasteiger2025subtlesandbag]. E4's final simulation ran, at the only noise level
calibrated to data, the rule that restricts while the upper bound on K exceeds a placeholder margin
of [0.90](../research/numbers.md#e4-gstar). With the loop at the corrected median return, well below
1, it fired in [88%](../research/numbers.md#e4-k-fa-n5) of runs after 5 rounds at each of three
budgets and [80%](../research/numbers.md#e4-k-fa-nmax) after 50. It fired only
[2%](../research/numbers.md#e4-k-fire-gap-n5) more often on a loop at the corrected 95th percentile,
and the same rule on the return alone only [3%](../research/numbers.md#e4-fire-gap-n5) more, both
within Monte Carlo error: the rule cannot tell the two loops apart, so the trigger is cut for both.
The historical fit is withdrawn too: in the speedrun record, stock and input correlate at
[0.98](../research/numbers.md#e4-sr-collinearity) and placebo inputs also return a value, so its
return is not identified. The deciding test, a real staged run that measures a round's noise, has not
been made. D2 stays a measurement design if the interval on K always spans 1 over the affordable
number of rounds.

**Label.** Extends prior work, narrowly, for the estimator only. The condition, its name and its
threshold at 1 [@cunningham2026rsi; @burtsev2026criticality; @yudkowsky2013iem], its use as a trigger
[@anthropic2026rsp; @openai2025preparedness], acting on the upper bound of a reproduction number
[@blumberg2020supercritical], repeated measurement against error bias [@ashenfelter1992twins] and a
staged, fixed-budget test of an AI research loop [@srikanth2026aide2] are prior work. What remains
(C4) is the round identity and the budget ladder as a design for measuring K, whose interval
under-covers at the calibrated noise; whether real staged runs place the return on one side of 1 is
untested. Until it is shown, the rule that decides is the prior-work ban on closed-loop
training research at frontier scale [@miotti2025narrowpath].

## D3. Breakout time

**Definition.** For a party with holdings H (chips at a realistic utilisation, weights and their
elicited capability, data, and research labour, human and AI), the breakout time T_b(p) on a path p
is the shortest time, under the party's best effort, to accumulate the effective compute C* that the
regime has agreed is enough to reach D1. Effective compute is physical compute times algorithmic
efficiency, which grows with research labour, AI labour included (D2), and depends on scale. Each
path (own fleet, cloud rental, purchase, smuggling, distillation) is computed separately and the
minimum taken. C* cannot be measured before someone reaches D1, so it is a stated, conservative
convention, revised on a schedule, as IAEA conversion times are tabulated under best-case assumptions
for the proliferator [@iaea-glossary-2022]. T_b is reported conditional on it.

**Measurement and test.** Chip counts, peak rates and utilisation are the measurable part. Efficiency
is the hard part: compute for fixed language-model performance halved every
[8.4 months](../research/numbers.md#def-ho-halving-months) from 2012 to 2023 [@ho2024algorithmic],
but the largest gains need scale to appear [@gundlach2025origin]. E1 could not
identify the drift rate of efficiency on public data: across samples it ran from
[2.6](../research/numbers.md#e1-algo-annual-subset-min) to
[1,512](../research/numbers.md#e1-algo-annual-subset-max) a year. Tabulating T_b in advance with an
interval, C2(a), is therefore cut, and the expression stays an accounting frame. The weakest input is
C*: one OOM of it moves T_b by [2.3 years](../research/numbers.md#comp-years-per-oom-ho), more than
Part II's illustrative line of [2.0 years](../research/numbers.md#prot-line-declared). Two tests are
unrun: whether the per-path expression differs from a breakout time with a single efficiency
multiplier by more than either's interval (C2(b)), and whether it backtests (C2(c)).

**Label.** Extends prior work, as a combination. Breakout time is arms-control vocabulary, with
training as the analogue of enrichment [@sastry2024compute]. It is defined for AI
[@barnett2025governance], computed from compute holdings [@miotti2025narrowpath;
@fithian2026hardwired] and from a calibrated model [@gan2026clock]; additive accounting of
post-training, inference and distillation is in [@pistillo2025loopholes], and the span a cheap
verifier opens in [@villalobos2023tradeoff]. Each term is prior; their combination was not found.

## D4. Weapons-grade: the line

**Definition.** A holding H is weapons-grade if, on some path p,

T_b(p) < m * T_r(p), with T_r(p) = T_d(p) + T_resp(p),

all in years. T_d(p) is the time by which the regime's channels on p detect a breakout with
probability at least 1 - beta. T_resp(p) is the time from a confirmed finding to an effective halt
(chips disabled, weights seized, a run stopped), or a high quantile of it where it is random. The
margin m, at least 1, covers estimation error.
Every holding with a longer breakout time on every path is useful AI and may keep improving, provided
each increment passes human-held gates (D6). Three limits from the red team belong to the definition.
Where progress can move between paths, as a checkpoint can, the safe test sets the shortest T_b
against the longest T_r. Beta bounds one attempt, and re-admitting a caught party gives it another
(E6), so the regime must bound attempts or state its guarantee per attempt. And while the untraced chip pool is open, its path fails the line for every
party, so the line separates no one until the pool closes.

With Poisson detection, D4 at m = 1 is the prevention condition of Gan's response-window model
[@gan2026clock]. The margin acts as an error budget: if the estimates of T_b and T_r err in the
unsafe direction by at most factors e_b and e_r, an admitted holding is still stopped, per attempt,
with probability at least 1 - beta whenever e_b * e_r <= m, for any continuous detection hazard
(Part III). It does not cover error in C*, which has no bound.

**Measurement.** T_b comes from D3, and T_d from the regime's channels, with the evader choosing the
path that minimises detection [@baker2025verifying]. E5 puts T_d on undeclared paths at
[31 years](../research/numbers.md#e5-td-site-now-years) to
[32 years](../research/numbers.md#e5-td-pool-years), against
[39.0 days](../research/numbers.md#e5-td-declared-days), a design figure, on the declared path; cloud
and distillation have no measured channel. In E24, [25%](../research/numbers.md#e24-halt-share-never)
of [8 findings](../research/numbers.md#e24-halt-findings) made while a party was in its treaty were
never followed by a halt, and halts took a median of
[1.2 years](../research/numbers.md#e24-halt-km-median-years) against the violator's fastest exit of
[31 days](../research/numbers.md#e24-exit-min-days); the response time has no finite 95th
percentile. The claim to compute T_r per path from drilled latencies, C1(c), is cut: a halt waits on
a finding by a quorum of rival states, a political decision no drill measures.

**Evidence.** The nuclear precedent is weaker than it is often said to be. The IAEA's timeliness
goals equal or exceed conversion times, so the implied margin runs from
[0.23](../research/numbers.md#def-iaea-m-metal-low) for metal to at most
[1.00](../research/numbers.md#def-iaea-m-irr-high), and they time detection only, never response
[@iaea-glossary-2001; @iaea-glossary-2022; @cochran-2005]. Prevention also costs more than
deterrence: in Gan's illustrative calibration, holding breakout success to
[5%](../research/numbers.md#def-prevent-beta) needs [7.8](../research/numbers.md#def-gan-prevent-multiple)
times the monitoring that deters [@gan2026clock]. This design takes prevention near the line, because
the endpoint is irreversible. Agreement on T_b matters as much, since a disputed threshold destroyed
cooperation in [@barrett2012climate]. E6 has reproduced the published games, but its treatment with
T_b drawn from an interval, which tests whether the line keeps compliance an equilibrium, is still to
come.

**Label.** Prior work, applied. Timely detection, evaluated per adversary path and judged at the
weakest, with a response time from measured parts and a margin, is nuclear physical-protection
practice, evaluated with EASI from 1977 [@snell2007itc20]. It is Nitze's 1988 standard for effective
verification [@hafemeister2008ctbt]. In AI it is stated in words [@barnett2025governance], as a
formula [@gan2026clock], and applied per route with an allowance for uncertainty
[@miotti2025narrowpath; @fithian2026hardwired]. What remains (C1) is the application to AI holdings
and the margin lemma, one line of algebra whose likeliest earlier home, the safety-factor literature
of structural engineering, our search did not open.

## D5. Elicited capability, robust to hiding

**Definition.** For threshold purposes, a system's capability on a battery is its score after a
named elicitation protocol E, applied by the regime's evaluators with weight access or in an enclave
the parties trust. E names its methods (fine-tuning on k demonstrations, reinforcement learning with
n samples, best-of-k sampling, the strongest public scaffolds, methods on the weights) and is revised
on a schedule. Each E carries two measured rates: the miss rate, the share of model organisms with
hidden capability above the threshold whose elicited score stays below it, and the false-alarm rate,
the share of benign models that E lifts over it. The guarantee covers only the capability range where
E's methods work.

**Measurement and test.** On model organisms whose hidden capability is known by construction
[@greenblatt2024password; @taylor2025auditinggames]. Against naive locks a few demonstrations suffice;
against hardened ones they do not. A tamper-resistant organism recalled
[7.8%](../research/numbers.md#def-robust-hard-recall) on hard tasks, against
[71.2%](../research/numbers.md#def-robust-base-recall) for its base model
[@finke2026robustorganisms], and elicitation lifted benign models by about
[10 points](../research/numbers.md#def-audit-benign-uplift) [@taylor2025auditinggames]. Above expert
level demonstrations do not exist, so the guarantee weakens as capability nears D1. The test, E3,
builds password-locked, RL-locked and tamper-resistant organisms on small open models with benign
controls, by builders blind to E, scores adaptive organisms built with E in hand apart, and reports
both rates per budget. It has not run. D5 fails if no affordable budget brings both rates below stated
targets on RL-locked organisms, since naive locks alone are prior work; it is expected to fail on
tamper-resistant and adaptive ones, which fall outside its guarantee. Beyond its range the protocol
falls back on compute, which E1 shows can misplace a system by
[2.8 OOM](../research/numbers.md#e1-gpqa-overlap-oom) on one benchmark.

**Label.** Extends prior work. Thresholds on elicited capability [@anthropic2023rsp;
@openai2025preparedness; @gpai-code-of-practice-2025], a fixed elicitation budget
[@anthropic2023rsp] and validation on locked organisms are prior work, and the statistics are those
of diagnostic tests [@fda2007diagnostic]. What remains (C5) is a miss rate and a false-alarm rate per
named budget over a defined population of organisms, as the pass-fail rule of a threshold among
parties that trust no one of them. The red team limited it: rates measured on organisms blind to the
procedure bound only hiding that does not adapt to it.

## D6. Closure

**Definition.** For each input to the next model (compute, weights, data, research labour, money),
closure is the share of increments, counted in that input's own unit, obtained without passing a
human-held gate whose passage is logged and can be verified by the regime. The gates are named:
licence renewal and cloud know-your-customer checks for compute, declared weight hashes, acquisition
logs for data, human approval of training launches and merges, and know-your-customer checks on
payment rails. Transfer of research advances between parties is one more input with its own gate,
and a narrow system whose outputs feed a covered system's training, code or compute counts as part of
it. Gates count the agent's completed horizon-length tasks, not hours, since a time horizon is
measured in human time [@kwa2025horizon]. D6 decomposes Burtsev's operational closure input by input
[@burtsev2026criticality]. In the loop's exponent the closures add, weighted by the inputs' shares,
as in the task-based model of automation [@aghion2017ai] (Part III): under complements the
least-closed input comes to set the gain, under substitutes the most-closed.

**Measurement and test.** By audit: sample increments, check that a gate was passed and logged, and
seed requests that a working gate must refuse. Gates on compute and money can be checked against
records; gates on research labour rest on a developer's self-report [@anthropic2026pace]. The gates
that exist hold for now: success on simplified self-replication tasks rose from under
[5%](../research/numbers.md#def-replibench-2023) to over
[60%](../research/numbers.md#def-replibench-2025) between 2023 and 2025 [@aisi2025trends], while
models still fail at identity checks [@black2025replibench]. The test, E4(d), gates each input in
turn inside a staged run and measures the gain transmitted with the gate on and off. D6 passes if the
gain with gates on any subset is predicted from closures measured one gate at a time; if not, closure
by input is framing and is cut. It has not run.

**Label.** Extends prior work, narrowly, and framing until tested. Closure as the fraction of gain
that survives the pipeline [@burtsev2026criticality], loops classified by how closed they are
[@chen2026rsisurvey], a ban on AI building AI [@miotti2025narrowpath], holding every input together
[@scher2026research], and self-improvement without authorisation as a red line [@redlines-2025] are
prior work. What remains (C11) is closure judged input by input against verifiable gates, with the
gain under any set of gates predicted from closures measured one at a time. Until E4(d) decides, the
safe bound takes the largest closure among ungated inputs, and the rule under it, to gate every highly
closed input together, is prior work [@scher2026research].
