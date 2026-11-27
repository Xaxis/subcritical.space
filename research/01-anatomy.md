# Part I: What superintelligence is, defined so a protocol can trigger on it

Part I asks what superintelligence is and by what mechanisms it forms. This opening chapter fixes
the definitions that the rest of Part I measures against and that the protocol in Part II triggers
on. The five chapters after it explain the mechanisms from five perspectives. This one says what
they are mechanisms of, and where the line between useful AI and the path to superintelligence
falls.

The memo (`00-memo.md`) proposed six candidate definitions before the survey: D1 superintelligence
as the endpoint, D2 loop gain, D3 breakout time, D4 the weapons-grade line, D5 elicited capability
robust to hiding, and D6 closure. The survey in `research/notes/` changed most of their labels.
In short:

- **None of the six is new at its core.** The inequality at the heart of D4, detect and respond
  faster than any breakout, is the timely-detection condition of nuclear physical protection,
  evaluated per adversary path since 1977 [@snell2007itc20]; in AI it was published in 2025
  [@barnett2025governance] and formalised in November 2026 [@gan2026clock]. D2's loop gain has the
  same name and threshold in prior work [@cunningham2026rsi; @burtsev2026criticality] and is already
  an industry trigger. D3 is arms-control vocabulary, and its terms are each in earlier accounting.
  D1's comparison against organisations, D5's fixed elicitation budget and D6's closure all have
  close precedents.
- **What may remain ours is small, and verification has made it smaller.** The independent
  prior-art search (level 1) and the red team (level 4) have run, and found no claim new
  ([the claims file](04-claims.md#summary)). What is left: D4's margin m as a multiplicative error
  budget, a one-line lemma; one per-path breakout expression, a combination of known terms, which
  adds something only if it beats a single multiplier or backtests; the round identity and budget
  ladder as a measurement of loop gain, whose decision power is unshown; miss and false-alarm rates
  per named elicitation budget, valid only against non-adaptive hiding; closure measured input by
  input, framing until an experiment tests it; and D1 as a definition that cannot warn. Two earlier
  candidates are cut: a response time computed from drilled latencies, since every response waits
  on a political decision, and breakout times tabulated in advance with an interval, since E1 cannot
  identify the drift rate they need. Each label is a claim about our search, not about the world.
- **The memo's organising idea misread nuclear safeguards.** The memo said the IAEA sets detection
  timeliness shorter than conversion time. It does not. Its timeliness goals equal or exceed
  conversion times, and they cover detection only, never response [@iaea-glossary-2001;
  @cochran-2005]. A margin m above 1, and a T_r that includes a treaty's response, have no
  safeguards precedent. Physical protection does count response, against a site's guard force, with
  a time margin [@snell2007itc20]: a response of another kind.

Everything here is a design. No definition below has been used to govern a real system or tested
against a real adversary.

## Why a protocol needs operational definitions, and what makes one a usable trigger

A prohibition needs a thing to prohibit. The Statement on Superintelligence calls for "a
prohibition on the development of superintelligence" and gives no operational definition of it
[@fli-superintelligence-statement]. The Global Call for AI Red Lines asks for lines that are
"clear and verifiable" and leaves the lines themselves to later dialogue [@redlines-2025]. The
company frameworks that do define thresholds report that they are hard to apply. Anthropic, in
February 2026: "We found pre-set capability levels to be far more ambiguous than we anticipated"
[@anthropic-rsp-v3-announcement-2026]. Its AI R&D threshold "has proven difficult to
operationalize" [@anthropic2026rsp]. OpenAI's Critical level for self-improvement turns on a
"generational model improvement" for which its text gives no metric [@openai2025preparedness].

An opinion cannot be checked by a party that does not share it. A protocol among rivals needs a
quantity, a unit, a measurement procedure, and a boundary that says which system is measured.

Precision matters to compliance itself, not only to enforcement. In Barrett and Dannenberg's
experiment, groups facing a known catastrophe threshold avoided it in [8 groups](numbers.md#def-bd-known-avoided) out of [10 groups](numbers.md#def-bd-groups).
When the threshold's location was uncertain, catastrophe was certain in [9 groups](numbers.md#def-bd-uncertain-catastrophe) out of [10 groups](numbers.md#def-bd-groups)
[@barrett2012climate]. A known line turned a dilemma into a coordination game; an uncertain one
turned it back. A line the parties dispute behaves like an uncertain one.

Three properties make a definition usable as a trigger.

1. **Measurable before it is too late.** The quantity must cross its threshold early enough for the
   regime to detect the crossing and respond before the harm it guards against. Harm-based
   definitions fail this by construction. California's SB 53 defines catastrophic risk by deaths
   and damage [@ca-sb53-analysis-2025]. Scher et al.'s draft treaty defines ASI as AI that "could
   plan and successfully execute the destruction of humanity" [@scher2025agreement]. Both name the
   endpoint, so neither can fire before it. Lagging indicators fail more slowly. OpenAI's lagging
   indicator fires only once a model generation arrives [5](numbers.md#def-openai-critical-speedup) times faster than in 2024
   (for example in [4 weeks](numbers.md#def-openai-critical-weeks)), "sustainably for several months" [@openai2025preparedness]. Gomez et
   al. warn that escalation which waits for confirmed harm detects events such as weight
   exfiltration "only after severe, irreversible harm has propagated" [@gomez2026escalation].
   Training compute passes this test: it "can be measured early in the AI lifecycle"
   [@heim2024thresholds].
2. **Hard to game.** A trigger the measured party can move without changing what it can do is not a
   trigger. Training compute is easy to measure but "only a very crude proxy for risk"
   [@heim2024thresholds]. Post-training enhancements are worth [5](numbers.md#def-posttraining-low) to [20](numbers.md#def-posttraining-high) times their compute
   [@heim2024thresholds], inference-time methods give gains of the same order without training FLOP,
   and small models overtake large ones [@hooker2024thresholds]. Capability scores have the opposite
   weakness: a model can underperform on purpose (D5).
3. **Verifiable by parties who distrust each other.** Each party must be able to check the
   measurement without trusting the measured party or the others. Company frameworks fail this as
   written. Their thresholds are judgements ("if we determine"), and their commitments are
   conditional on competitors [@anthropic2026rsp; @openai2025preparedness]. DeepMind judges
   its AI R&D levels from its own progress because "we do not expect other groups to put
   significantly more effort into ML R&D than we do ourselves" [@gdm-fsf-v3-1-2026], an assumption
   that fails exactly in a breakout. The one independent measurement of AI R&D acceleration at a lab
   had its most informative evidence redacted, and "Anthropic changed the scope of this project
   midway to exclude compute verification and instead just focus on AI R&D acceleration"
   [@metr-anthropic-acceleration-2026]. Verification also has a price: monitoring that assures
   compliance can expose secrets, which Coe and Vaynman identify as the main reason arms control is
   rare [@coe2020arms].

A fourth, practical property: a definition must say how it updates. The EU presumes high-impact
capability above [1e+25 FLOP](numbers.md#def-eu-presumption-flop) of training [@eu-ai-act-2024], and the Code of Practice chairs expect
"hundreds" of models above it within a few years [@gpai-code-of-practice-2025]. A fixed number
drifts as algorithms improve.

Koessler et al. divide thresholds into capability thresholds and risk thresholds
[@koessler2024risk]. D4 below is a third kind, a time threshold: it compares how fast a holding
could become dangerous with how fast the regime can react.

The table gives our assessment of the six definitions against the three tests, with what the
experiments so far have changed. The sections below give the reasons.

| Definition | Measurable early | Hard to game | Verifiable among rivals |
|---|---|---|---|
| D1 endpoint | No: true only at the endpoint | Partly: contamination inflates scores, sandbagging deflates them | Only with a regime-held battery and model access |
| D2 loop gain | Partly: at small scale, with no decision power at the calibrated noise, an interval that under-covers and estimates that lean subcritical (E4); transfer to the frontier unproven | Weakly: a research agent withholding a small share of its gain silences the bound (E4); observational versions need the developer's data | Weakly, unless staged runs on declared systems are allowed |
| D3 breakout time | Partly: the compute term from holdings; the drift term is not identified on public data (E1) | Weakly where inputs are disputed (algorithmic efficiency, undeclared gains, the distance to D1) | Strongly for chips; weakly for algorithms and data |
| D4 the line | For T_b on declared compute; T_r has no finite quantile for any violation that needs judging (E24) | Inherits D3 and T_r | As strongly as its weakest input; while the untraced pool is open, it separates no party |
| D5 elicited capability | Yes, at declared checkpoints | Partly: hardened and RL-trained locks resist, and the rates bound only non-adaptive hiding | Only with weight access or a trusted enclave |
| D6 closure | Yes: gates are visible before the loop runs | Partly: a gate can be a rubber stamp | Strongly for compute and money; weakly for research labour |

## D1. Superintelligence, the endpoint

### Operational definition

Restated after the survey. A system S, deployed with resources R, is superintelligent at level
alpha on a battery B when all of the following hold:

- B spans N decisive clusters, the five of the cognitive chapter
  ([F2](014-cognitive.md#f2-the-decisive-functions)): AI research, cyber operations, weapons-relevant
  science, persuasion and strategy, and economic production, each with a score and a published
  baseline set by a named human organisation;
- B is held by the regime, refreshed, and unseen by S's developer before the test;
- S with R (compute in FLOP and FLOP/s, money, copies and wall-clock time T) beats the organisation
  given the same T and the same budget, in at least alpha times N clusters;
- the organisation's technology is fixed to a stated vintage that excludes frontier AI.

The unit is the fraction of clusters won. The system boundary is S plus everything R lets it run:
all copies, tools and scaffolds. Four parameters must be stated or the verdict is undefined: T, the
organisation, its technology vintage, and the rule for matching budgets. The survey forces each
one. Verdicts flip with T: on RE-Bench the best agents scored [4](numbers.md#def-rebench-agent-advantage) times human experts at a
[2 h](numbers.md#def-rebench-short-budget) budget, and the experts scored [2](numbers.md#def-rebench-human-advantage) times the top agent at [32 h](numbers.md#def-rebench-long-budget) [@wijk2024rebench]. Baselines vary
with context: contract baseliners take [5](numbers.md#def-kwa-baseline-low) to [18](numbers.md#def-kwa-baseline-high) times longer than repository maintainers on the
same issues [@kwa2025horizon]. And if the organisation may use AI, the baseline moves with the
thing measured, which is why Genewein et al. freeze their human collective at the technology of
[2010](numbers.md#def-genewein-tech-year) [@genewein2026agiasi].

### How it is measured

Scaled-down batteries with team or institutional baselines exist in a few domains: Kaggle
leaderboards through MLE-bench [@chan2024mlebench], RE-Bench against experts at matched GPU hours
[@wijk2024rebench], forecasting against professional teams [@metaculus2026futureeval], and protein structure
prediction [@jumper2021alphafold].
They are rare: fewer than a quarter of prominent benchmarks claim any organisational dimension of
work [@barres2026harder]. One often-quoted team comparison does not serve D1. In a 24-hour onsite
capture-the-flag event, the human teams were mostly undergraduates using an AI assistant, and the
agent ran on a separate scoreboard [@tang2026ctfcollab]. It says nothing about expert
organisations.

Measurement error is large and has both signs. Benchmarks with expert baselines saturate within a
year or two: the best GPQA Diamond score reached [96.8%](numbers.md#def-gpqa-best-2026) in November 2026 [@epoch2026hub] against
[65%](numbers.md#def-gpqa-expert) for PhD experts, or [74%](numbers.md#def-gpqa-expert-adjusted) discounting the mistakes they identified [@rein2023gpqa].
FrontierMath went from under [2%](numbers.md#def-frontiermath-release) at release [@glazer2024frontiermath] to [95%](numbers.md#def-frontiermath-best-2026) on its first three
tiers [@epoch2026hub]. Labels are often wrong: Epoch found [46%](numbers.md#def-hle-defective) of a sample of Humanity's Last
Exam defective [@epoch2026hlereview]. Contamination inflates scores and sandbagging deflates them.
Matching cost is a measurement too: an agent's 8-hour RE-Bench run cost about $[123](numbers.md#def-rebench-agent-cost) against
$[1,855](numbers.md#def-rebench-human-cost) paid to a human expert, [15](numbers.md#def-rebench-cost-ratio) times less [@wijk2024rebench].

Only an evaluator with access to S and to a held-out battery can measure D1. The developer can
hide capability (D5) or train on leaked items, so the battery must be the regime's, refreshed as
benchmarks such as LiveBench already are [@white2024livebench], and D1 must be scored on elicited
capability.

### Evidence for and against

For an organisational baseline: the superintelligence that matters strategically is the capacity
to outdo institutions, not individuals. Aguirre places "full" AGI at the intelligence "that large
collections of top human experts would have if combined" [@aguirre2025ktfh]. Barnett and Scher
define ASI as AI that can "substantially surpass humanity in all strategically relevant activities"
[@barnett2025governance]. Anthropic's AI R&D threshold compares AI with its "entire set of
Research Scientists and Research Engineers" at competitive cost [@anthropic2026rsp].

Against, steelmanned: individual baselines are measurable now and organisational ones mostly are
not. Bostrom's definition is an intellect "much smarter than the best human brains in practically
every field" [@bostrom1998howlong]. Morris et al. grade AGI by percentiles of skilled adults, up to
the [99](numbers.md#def-morris-exceptional-pct)th at Level 4 [@morris2023levels]. Hendrycks et al. operationalise AGI over ten cognitive
domains with psychometric batteries and score GPT-4 at [27%](numbers.md#def-hendrycks-agi-gpt4) and GPT-5 at [57%](numbers.md#def-hendrycks-agi-gpt5)
[@hendrycks2025agidef]. These can be run today; an organisational battery across five clusters cannot,
for lack of baselines. The sharper objection is that D1 is true only once the decisive capability
already exists, so it cannot warn. The memo conceded this.

Left open: whether to score outcomes (a forecast resolved, a vulnerability found) or the
organisation's own tasks; and how to match budgets when the organisation's main cost is salaries
and the system's is compute.

### What the survey changed, and the prior work it must credit

The memo said D1 differs from earlier definitions "by comparing against organisations rather than
individuals, by counting copies and speed, and by matching time and cost". Most of that is prior
work. Genewein et al. define ASI against "large human-expert collectives": groups of tens of
thousands of experts working [10 years](numbers.md#def-genewein-years) with the technology of [2010](numbers.md#def-genewein-tech-year), outdone by a system that
also works [10](numbers.md#def-genewein-speed) or more times faster, where one ASI "may consist of a collective of millions of
instances" [@genewein2026agiasi]. Ngo defines a (t, n)-AGI as one that beats "any group of n humans
working together" for time t, and thinks of superintelligence as a ([1 year](numbers.md#def-ngo-si-years), [8 billion people](numbers.md#def-ngo-si-humans))-AGI
[@ngo2023tagi]. Anthropic matches cost within a factor of [5](numbers.md#def-anthropic-cost-factor) for one cluster
[@anthropic2026rsp]. DeepMind compares with "any team of researchers at Google ... with
approximately comparable all-inclusive costs" [@gdm-fsf-v3-1-2026]. OpenAI matches wall-clock time
[@openai2025preparedness]. RE-Bench matches time and GPU hours against [61 experts](numbers.md#def-rebench-experts)
[@wijk2024rebench].

The claims file adds a crossover budget, t*: the largest tested time budget at which the system's
score on the AI-research cluster is at least the comparison's at equal compute and money, censored
and reported as a lower bound when the system still wins at the largest budget tested, never
extrapolated ([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).
The crossover itself is prior work. RE-Bench reports where the advantage flips with the budget
[@wijk2024rebench], and Robinson defines the intersection of the AI and human curves as a quantity
and tracks it across models [@robinson2026horizons], t*'s closest relative.

The label stays "extends prior work", with a narrower claim, and level 1 confirmed it. Not found in
our search or level 1's: a definition that matches both wall-clock time and budget against a named
organisation, scored on a refreshed, regime-held battery with institutional baselines across several
decisive clusters, with an alpha fraction, and with t* censored at the largest tested budget. It is
a definition only. D1 holds once a system already beats an institution, so neither D1 nor t* can
warn; the protocol acts on the line (D4) before it.

### What it means for the protocol

D1 is not a trigger. It is the target that D3 measures distance to: breakout time is the time to
reach D1. The protocol needs it for two things: to say what breakout is breakout to, and to
calibrate D3 by measuring on scaled-down batteries how far current systems sit from the bar and how
fast the distance shrinks. Its cost to useful AI is the cost of running evaluations.

### What would test it

A new test, the scaled-down D1 battery, now part of E21. Take public models along a capability
ladder. Score each on the clusters that have institutional baselines (MLE-bench against Kaggle
teams, RE-Bench against experts at matched GPU hours, forecasting against professional teams).
Report the fraction of clusters won at matched time and matched budget, at several time budgets. The
definition passes if the verdict is stable within its stated parameters (changing the baseline
organisation within the stated class does not flip it) and if the fraction won rises smoothly with
effective compute, so that D3 can extrapolate it. If the verdict depends mainly on the choice of T or
of organisation, D1 is underspecified.

Public data cannot run this test. E1 searched the archive's columns and found
[5 clusters](numbers.md#e1-clusters-baselined) with any human comparison, every cluster in the list
above, though persuasion and strategy has one only through its strategy half (forecasting) and
persuasion itself has none; and [3 clusters](numbers.md#e1-clusters-verdict) with a bar a model
wins or loses. None is an organisation at matched budget. So E21 must build the baselines before the pass condition can be
tested. E2 refitted METR's time horizons: the 50% horizon doubles every
[129 days](numbers.md#e2-doubling-p50), and its ratio to the 80% horizon is a stable
[5.3](numbers.md#e2-p50-over-p80). That gives the time-budget dependence for individual tasks, not
for an organisation.

## D2. Loop gain

### Operational definition

Restated after the survey. Measure capability on a log compute-equivalent axis: the log of the
training compute a fixed reference recipe would need to reach the same held-out score. A round is
one research cycle at a fixed budget: fixed experimental compute, fixed data, fixed wall-clock
time. Let dC(n) be the capability gained in round n. The loop gain is

g = dC(n+1) / dC(n),

where the research in round n+1 is done by the system that round n produced. A value of g at or
above 1 means each round gains at least as much as the last with the human-held inputs fixed: the
compounding condition. In the dynamical chapter's common form, g exceeds 1 exactly when the loop's
gain K does. But g is not a stable parameter: in a subcritical loop each round gains less than the
last and g tends to 1, so a threshold on g below 1 would in time fire on every subcritical loop,
however precisely g were measured ([the formal file, C4](05-formal.md#c4-the-loop-gain-estimator)).
The quantity D2 measures is therefore K, the stationary one. Consecutive gains satisfy an exact
round identity, ln[(exp(b dC(n+1)) - 1) / (exp(b dC(n)) - 1)] = b (K - 1) dC(n), with b the returns
exponent ([the formal file, Lemma 4.1](05-formal.md#c4-the-loop-gain-estimator)). A staged run with
a fixed agent estimates b from it; repeating the run at one, two and four times the agent budget,
the budget ladder, estimates the return to input lambda (Lemma 4.2). Their ratio, r = lambda / b, is
the gain the loop would have if fully closed, and K is r times the closure (D6). Measuring each
round's gain on two independent held-out sets was meant to remove the first-order bias a single
noisy set puts toward a subcritical loop (Proposition 4.6). E4 found that it does not. Where the
noise is error in measuring a round's gain, a second set turns a median estimate of
[0.57](numbers.md#e4-diff-bias-meas1) times the true r into one of
[8.11](numbers.md#e4-diff-bias-meas2) times it; where the noise is real variation in the round's
gain, a second set measures it identically and cannot help.

D2 is a measurement design, not a trigger. A trigger would restrict while the upper bound of a
confidence interval on K exceeds a margin set below 1, the rule that leaves a loop above the margin
unrestricted with probability at most the stated error (Proposition 4.4) and the one epidemic
control uses for reproduction numbers [@blumberg2020supercritical]. E4's final simulation ran that
rule on K at the only noise level calibrated to data, with a placeholder margin of
[0.90](numbers.md#e4-gstar). With the loop at the corrected median of r, well below 1, it fired in
[88%](numbers.md#e4-k-fa-n5) of runs after 5 rounds at each of three budgets and
[80%](numbers.md#e4-k-fa-nmax) after 50. With the loop at the corrected 95th percentile it still
missed [10%](numbers.md#e4-k-late-cal). It fired only [2%](numbers.md#e4-k-fire-gap-n5) more often on
the higher loop than on the lower one, and the rule on r alone only
[3%](numbers.md#e4-fire-gap-n5) more, both within Monte Carlo error: the rule cannot tell the two
apart. So the trigger is cut, and C4 stands only as a measurement design
([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)). What
decides meanwhile is the prior-work rule: closed-loop training research on a declared frontier-scale
system is treated as above any threshold, which is a ban on AIs improving AIs at that scale
[@miotti2025narrowpath]. That ban is the rule until E4(b) measures real staged rounds. If they prove
tight enough for the upper bound to fall below the margin on loops that are truly subcritical, a
rule on K could replace the ban for those loops; nothing yet shows they will. What changed: this
chapter first set the trigger on the lower bound of g, then on the upper bound of g, then on the
upper bound of K, and each step failed a level; D2 now names the measurement and leaves the decision
to the ban until the measurement can carry it.

Three choices separate this from what the survey found. The inputs are held fixed, so g measures
the loop and not the growth of compute and staff. The axis is compute-equivalent, because on a
bounded benchmark successive gains shrink near the ceiling whatever the feedback; Cunningham et al.
note that their product of elasticities is invariant to how capability is normalised, while a raw
ratio of gains is not [@cunningham2026rsi]. And the unit is the round, not the calendar year.

A practical consequence follows from Cunningham et al.'s decomposition [@cunningham2026rsi]. Their
condition for self-sustaining acceleration is a product of three factors: the return to research
inputs, the rise in research productivity per unit of capability (epsilon_R,C), and the rise in
capability per unit of compute (epsilon_C,A); their calibration takes the first as [1.0](numbers.md#def-cunningham-return) and the
third as [6.5](numbers.md#def-cunningham-eps-ca). A small staged run with a fixed agent measures the first. Scaling data give the third. The second needs a ladder of research agents of different
capability. So D2 is estimated as a product of separately measured pieces, each with its interval.

### How it is measured

There are two routes. The observational route compares the rate of progress before and after AI
contributes, with inputs free; the experimental route, which D2 requires, stages rounds at fixed
inputs. The observational route has been run once independently. METR estimated that Anthropic's internal
capability index grew [1.9](numbers.md#def-metr-acceleration) times faster after October 2025 (95% CI [1.5](numbers.md#def-metr-acceleration-ci-low) to [2.8](numbers.md#def-metr-acceleration-ci-high); robustness
analyses [1.1](numbers.md#def-metr-robust-low) to [2.9](numbers.md#def-metr-robust-high)), from [15](numbers.md#def-metr-aeci-before) to [29 points a year](numbers.md#def-metr-aeci-after), a ratio of [1.9](numbers.md#def-metr-aeci-ratio)
[@metr-anthropic-acceleration-2026]. METR judged that "perhaps ~80%" ([80%](numbers.md#def-metr-ai-share)) of it was due to
AI, a subjective estimate. METR states the limits itself: benchmark saturation, no staff-level
access, redacted evidence, and Claude doing much of the analysis. The estimate is neither at fixed
inputs nor per round.

The experimental route has a harness. The Automated LLM Speedrunning Benchmark gives agents the
previous NanoGPT speedrun record and asks them to reproduce the next; current agents "struggle to
reimplement already-known innovations" [@zhao2025speedrun]. For the historical version, METR has
coded the record series and credits AI agents with [4 records](numbers.md#def-nanogpt-ai-records) out of [77 records](numbers.md#def-nanogpt-records), all shallow to
moderate [@shetty2026metrnanogpt]. In E4's count of Epoch's longer series,
[5 records](numbers.md#e4-ai-records) of [92 records](numbers.md#e4-records) credit an AI system, each
with a human, for [1.1%](numbers.md#e4-ai-share) of the log speedup. The history cannot place the
loop's gain. Across months the speedrun's stock and the log of its research input correlate at
[0.98](numbers.md#e4-sr-collinearity), and putting placebo inputs in place of contributors gives an r
of [0.59](numbers.md#e4-sr-placebo-r-records) for the count of recent records and
[1.03](numbers.md#e4-sr-placebo-r-time) for time itself. An r fitted to the record reflects the
shared trends, not the research input, so it is withdrawn as not identified.

Error and gaming. A staged estimate over a few rounds has wide sampling error, and E4 found the
estimators miscalibrated as well. After 5 rounds at each of three budgets, the nominal 90% interval
on r covered the truth in [82%](numbers.md#e4-cov-n5) of runs for the first-order level form and
[77%](numbers.md#e4-cov-n5-xml) for maximum likelihood on the exact identity. Each estimator leans
toward a subcritical verdict, the unsafe side: on data from the exact round law, the median estimate
was [0.82](numbers.md#e4-level1-bias) times the true r for the level form,
[0.77](numbers.md#e4-xml-bias) for maximum likelihood and [0.47](numbers.md#e4-diff-bias) for the
first-order difference regression. The agent running the test can underperform: Claude 3.7 Sonnet
was "almost capable of zero-shot sabotage" of ML tasks, and zero-shot monitors had an "underwhelming
true positive rate" at low false-positive rates [@gasteiger2025subtlesandbag]. So the agent must be
elicited (D5) and K reported as a lower bound. A sandbagger that withholds gain in a pattern defeats
the upper bound even where rounds are large and tightly measured: withholding
[16%](numbers.md#e4-hide-silence-fav) of its achievable gain kept the rule silent in at least half
the runs on a loop at the corrected 95th percentile, and [42%](numbers.md#e4-hide-silence-cal) did so
at the calibrated noise. An agent withholding on average a quarter of each round's gain, in the
pattern that most delays the rule, made the K rule miss [90%](numbers.md#e4-k-late-hide25-fav) of such loops in
favourable rounds. Only elicitation that measures each round's achievable gain, not the estimator,
can catch that shortfall. The experimental route needs only the system and a compute budget, so a regime evaluator can run it on a declared
checkpoint. The observational route needs the developer's internal data and goodwill, which can be
withdrawn, as the METR engagement shows.

### Evidence for and against

The condition sits near 1, which is why measuring it matters and why a trigger on it needs a tight
interval. Measured returns to software research, in doublings of output per doubling of research
input, are [1.89](numbers.md#def-r-lm) for language models (90% CI [1.07](numbers.md#def-r-lm-low)
to [3.21](numbers.md#def-r-lm-high)) and [1.26](numbers.md#def-r-cv) for computer vision
[@ho2025experiments]. Divided by [3](numbers.md#def-r-bottleneck-divisor) to account for compute
bottlenecks, the point estimates fall to [0.63](numbers.md#def-r-lm-bottlenecked) and
[0.42](numbers.md#def-r-cv-bottlenecked), though the upper end of the language-model interval stays
just above 1, at [1.07](numbers.md#def-r-lm-high-bottlenecked) [@ho2025experiments]. That correction
leaves compute's own growth out. Counting it, E9 puts the language-model gain at fixed compute at
[0.25](numbers.md#e9-lm-k-fixed) ([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile) at the
same compute share, [0.67](numbers.md#dyn-research-compute-share), and above 1 only if compute's
share of research input is below about [0.26](numbers.md#e9-lm-share-crit), a share none of E9's
data identifies. Davidson and Houlden's fixed-compute model takes a median of
[1.2](numbers.md#def-sie-r-median), with a range of [0.4](numbers.md#def-sie-r-low) to
[3.6](numbers.md#def-sie-r-high) [@davidson2025sie]. Cunningham et al. put the threshold for
self-sustaining acceleration at a research productivity gain of
[0.15](numbers.md#def-cunningham-eps-rc-threshold) per point of the Epoch Capabilities Index (we
reproduce [0.15](numbers.md#def-cunningham-threshold-check) from their inputs). A reported uplift of
[4](numbers.md#def-cunningham-uplift) times, which they call "very likely to be an overestimate",
would imply [9%](numbers.md#def-cunningham-eps-rc-illustration), below the threshold
[@cunningham2026rsi]. That figure is an upper-end illustration, not an estimate. On their
calibration it corresponds to a loop gain of about
[0.58](numbers.md#def-cunningham-loop-gain-illustration). Their reading is that feedback loops "are
not currently strong enough to generate a self-sustaining acceleration, though they appear to be
strengthening".

The research-labour input is being automated quickly. Anthropic reports that Claude "leads" [26%](numbers.md#def-anthropic-ai-led)
of its AI R&D work, up from under [1%](numbers.md#def-anthropic-ai-led-feb) in February 2026, with about [30,000 agents](numbers.md#def-anthropic-agents) working at
once on one internal platform. It also says Claude "is not operating fully autonomously for any
measured subset of AI R&D work" [@anthropic2026pace]. This is a self-report by the developer.

Against D2 as defined, steelmanned. First, holding inputs fixed is counterfactual: real inputs grow
fast, so an inputs-fixed g understates acceleration in the world as it is [@cunningham2026rsi].
Under a compute cap, the inputs-fixed g is the quantity that matters, but D2 alone does not track
an uncapped world. Second, Burtsev shows that the transition to self-amplification "need not occur
at any particular level of model capability", that rapid growth is "neither necessary nor
sufficient evidence of recursive criticality", and that a system "can therefore enter a
self-amplifying regime before acceleration becomes visible" [@burtsev2026criticality]. This cuts
harder against the industry's rate triggers than against D2, which is per cycle, but it warns that
g measured on one system says little about the next. Third, transfer: algorithmic gains may be
scale-dependent [@gundlach2025origin], so g measured at small compute may not hold at the frontier.
E1 could not settle the sign of that dependence on public data (D3).
Fourth, the historical data are poor where they matter: the speedrun record is driven by humans,
mixes systems engineering with algorithms, and moves very unevenly.

Left open: whether any affordable number of rounds gives an interval narrow enough to decide on.
E4's simulation says not at the calibrated noise. Even with large, tightly measured rounds, which no
real staged run has shown, the K rule needed [20 rounds per budget](numbers.md#e4-k-fa-rounds-fav) at
each of three budgets to bring its false alarms to 10%. Only a staged run, E4(b), measures a real
round's noise. Also open: whether K is stable across rounds or rises with capability, which is what
recursive criticality predicts.

### What the survey changed, and the prior work it must credit

The memo believed the condition was prior work and a runnable estimator might be new. The survey
moves more into prior work. Cunningham et al. name "the loop gain", derive its threshold at 1, and
call estimating it, "tracking it over time, and extrapolating when it might cross 1 ... arguably
the most important empirical exercise" [@cunningham2026rsi]. Burtsev defines a recursive
reproduction number, R_AI = chi * a / sigma, with a self-amplifying regime above 1
[@burtsev2026criticality]. Yudkowsky framed the same idea in 2013 as a neutron multiplication factor
[@yudkowsky2013iem], which is also the precedent for this project's name. Eth and Davidson propose
measuring software progress, disclosing it to trusted third parties, and acting before a threshold
such as [5](numbers.md#def-eth-threshold) times the recent pace [@eth2025sie].

It is also in force as a trigger. Anthropic's RSP fires at [2](numbers.md#def-anthropic-rate-multiple) times the baseline rate of progress,
measured over at least [3 model generations](numbers.md#def-anthropic-baseline-generations); at a baseline of [9](numbers.md#def-anthropic-example-baseline)x a year, doubling the rate means
about [81](numbers.md#def-anthropic-example-doubled)x a year [@anthropic2026rsp]. OpenAI's Critical level is [5](numbers.md#def-openai-critical-speedup) times the 2024 pace
[@openai2025preparedness], and DeepMind has "ML R&D acceleration level 1"
[@gdm-fsf-v3-1-2026]. Automated AI R&D is the near-universal industry trigger for the
self-improvement pathway [@metr-common-elements-2025].

Label: prior work for the condition and for its use as a trigger; extends prior work, narrowly, for
the estimator. The independent prior-art search found more: acting on the upper bound of a
reproduction number is epidemic practice [@blumberg2020supercritical], so is estimating a
subcritical one from successive generations [@blumberg2013stuttering], independent repeated
measurements to remove error bias are the twins design [@ashenfelter1992twins], and a staged,
fixed-budget test of whether an AI research loop accelerates, with held-out scoring, exists
[@srikanth2026aide2]. What may remain ours: the exact round identity as the estimator of K for an AI
research loop staged at fixed inputs, and the budget ladder for the return to input, as a
measurement design whose decision power is unshown; E4 found its interval under-covers and its
estimates lean subcritical at the calibrated noise
([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)). The
industry triggers and METR's estimate are ratios of overall progress rates with inputs free. Burtsev
gives no estimation procedure: he fixes the delay of a development cycle at
[0.5 yr](numbers.md#def-burtsev-delay) by assumption and says his gain, closure and hardening are
"not presently constrained by direct empirical estimates" [@burtsev2026criticality].

### What it means for the protocol

D2 was the candidate trigger for the pathway the memo ranked first, recursive self-improvement. On
current evidence it cannot carry that role, so the limit is the cruder one: no closed-loop AI
training research on declared frontier-scale systems. D2 measures, in staged tests the regime runs
on declared checkpoints, whether that ban could one day give way to a rule on the upper bound of K
for loops shown to be subcritical; a threshold on g itself would in time fire on every subcritical
loop. The ban holds at least until E4(b) measures real staged rounds. Declarations of the share of research work AI leads go alongside. Either rule binds only loops
a developer declares. The cost to useful AI is low if the limit targets training-research loops on
frontier systems, not AI-assisted software work in general. The weakest link is measurement: a
staged run at small scale is not the frontier loop, and the developer controls the observational
evidence. D2 also feeds D3, since a higher K shortens breakout time at fixed compute.

### What would test it

E4, loop gain, historical and staged. (a) Historical: fit g to the NanoGPT speedrun record series
on a compute-equivalent axis, with bootstrap intervals, separately for AI-credited records. It has
run, and the history cannot place r: stock and input correlate at
[0.98](numbers.md#e4-sr-collinearity) and placebo inputs put in place of contributors return an r
too, so the speedrun's r is withdrawn as not identified. (c) Simulated: the estimator's coverage and the
trigger's error rates at the calibrated noise. It has run in its final form and cut the trigger
(above). (b) Staged: an elicited agent improves a small model's training recipe over at least five rounds at
fixed compute, data and time, using the existing speedrun harness. The improved system, or a
stronger agent from a fixed capability ladder standing in for it, does the next round. Report the
return per round with its interval, and combine it with epsilon_C,A from public scaling data and
epsilon_R,C measured along the ladder. The definition fails if, over the affordable number of
rounds, the interval on K always spans 1: D2 then stays a measurement and the ban stays. E4(c)
already finds that at the calibrated noise; E4(b) decides it with a measured one, and has not run.

## D3. Breakout time

### Operational definition

Restated after the survey. For a party with holdings H (chips by type and count, so FLOP/s at a
realistic utilisation; model weights and their elicited capability; data; research labour, human
and AI), the breakout time T_b(H; C*) is the shortest time, under the party's best self-directed
effort, to accumulate the effective compute C* that the regime has agreed is enough to reach D1.
Effective compute is physical compute times algorithmic efficiency. Efficiency grows at a rate set
by the research labour applied, which includes AI labour whose productivity rises with capability
(D2). Efficiency may depend on scale, so it is not assumed to be one multiplier. Distillation enters
at the teacher's level plus an uplift, since a student can exceed its teacher
[@furlanello2018born; @burns2023weak]. The unit is years. The boundary is the
party and every path open to it (its own fleet, cloud rental, purchase, smuggling, distillation
from others' models), each path computed separately and the minimum taken.

The definition needs C*, and C* is not known: no one can measure the effective compute that reaches
D1 before someone reaches it. So C* must be a stated, conservative convention, revised on a
schedule. This mirrors the IAEA's conversion times, which are tabulated by material category,
estimated under best-case assumptions for the proliferator (facilities exist, processes tested),
and exclude transport and assembly [@iaea-glossary-2022]. Part II tabulates breakout times the same
way, by holding class, as a convention agreed before anyone needs them. What cannot be delivered is
an interval that holds: E1 cannot identify the drift rate on public data, so tabulating T_b in
advance with an interval is cut
([C2](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)).
Every T_b is reported conditional on the agreed C*, whose error has no bound, and on the declared
path also on an allowance for efficiency gains a party has not declared, which no source sizes.

### How it is measured

The physical inputs are the measurable part: chip counts from registries and supply-chain
accounting, peak rates, and a utilisation factor (the hardwired-pause group assumes [21%](numbers.md#def-hwp-utilisation) for
frontier fleets [@fithian2026hardwired]). Algorithmic efficiency is the hard part. The compute needed for a
fixed language-model performance halved every [8.4 months](numbers.md#def-ho-halving-months) from 2012 to 2023 (95% CI [4.5 months](numbers.md#def-ho-halving-fast) to
[14.3 months](numbers.md#def-ho-halving-slow)) [@ho2024algorithmic]. On our arithmetic that is a fall of [2.7](numbers.md#def-ho-annual-multiple)x a year, with an interval
of [1.8](numbers.md#def-ho-annual-multiple-slow)x to [6.3](numbers.md#def-ho-annual-multiple-fast)x. Selection bias may mean observational estimates overstate progress by about
[9](numbers.md#def-whitfill-bias-factor) times, in a first-pass estimate with other explanations possible [@whitfill2025selection]. And efficiency may not be scale-free: of the
[22,000](numbers.md#def-gundlach-claimed)-fold gain previously estimated for 2012 to 2023, less than [100](numbers.md#def-gundlach-low-compute-max)-fold reproduces at low
compute, because the largest gains (the Transformer, the Chinchilla rebalancing) have
scale-dependent efficiency [@gundlach2025origin]. Loop gain enters through D2, with
its own interval.

E1 tried to measure the drift rate on public data and could not identify it. On all
[105 models](numbers.md#e1-models) with a capability index and a compute estimate, training compute
explains [36%](numbers.md#e1-compute-share) of the growth, and the rest moves with date at about
[17](numbers.md#e1-algo-annual) times a year in compute-equivalent. Across six samples of the same
models the share runs from [18%](numbers.md#e1-compute-share-subset-min) to
[63%](numbers.md#e1-compute-share-subset-max) and the rate from
[2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max) a year,
far beyond any one sample's interval. On the full sample drift falls with scale, by
[-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom), but the sign is not robust across samples,
and in Ho et al.'s data the highest compute tercile progressed faster than the lowest in only
[52%](numbers.md#e1-ho-top-faster-share) of resamples. Compute also misplaces systems: on GPQA
Diamond the largest model that loses to PhD experts used
[2.8 OOM](numbers.md#e1-gpqa-overlap-oom) more training compute than the smallest that wins.

A party can hide or fake the inputs. Chips can be smuggled or made covertly (`011-physical.md` and
`015-organisational.md` take this up). Algorithms are invisible. The capability of weights is
hidden unless elicited (D5). So T_b is computed for declared holdings and for each undeclared path
the regime cannot rule out.

### Evidence for and against

Prior designs already compute breakout from holdings. A Narrow Path sets its cluster limit (FLOP
per second) [8 orders of magnitude](numbers.md#def-narrowpath-oom-gap) below its compute limit (FLOP), so an illegal run on a licensed
cluster would take [3.2 yr](numbers.md#def-narrowpath-breakout-years), "giving authorities ample time to intervene", while permitted models
train within [12 days](numbers.md#def-narrowpath-permitted-days) [@miotti2025narrowpath]. That gap, read in seconds, is [3.17 yr](numbers.md#def-narrowpath-breakout-check). The
hardwired-pause working paper derives a breakout fleet threshold of [180 million H100e](numbers.md#def-hwp-fleet-threshold) from a
breakout budget of [2e+29 FLOP](numbers.md#def-hwp-breakout-budget), a research overhead of [12](numbers.md#def-hwp-overhead), a utilisation of [21%](numbers.md#def-hwp-utilisation) and a horizon
of [2 yr](numbers.md#def-hwp-horizon), with one H100-equivalent at [989 TFLOP/s](numbers.md#def-hwp-h100e-rate) [@fithian2026hardwired]. Our model reproduces it as
[180 million H100e](numbers.md#def-hwp-fleet-check), [3.9](numbers.md#def-hwp-fleet-over-global) times the global fleet the paper projects for the end of 2026
([47 million H100e](numbers.md#def-hwp-global-fleet)). Gan computes the time a follower needs to reach a frozen frontier and shows that
it shrinks during a compliant pause, because compute keeps growing: from [12](numbers.md#def-gan-catchup-start) to [8.61 months](numbers.md#def-gan-catchup-12) after
a year and [5.74 months](numbers.md#def-gan-catchup-24) after two, [48%](numbers.md#def-gan-catchup-share) of where it started, in an illustrative calibration
[@gan2026clock]. The hardwired-pause group finds the same erosion: [57%](numbers.md#def-hwp-efficiency-growth) annual efficiency gains
before inference-only chips ship at scale would raise US overt breakout capacity from [20%](numbers.md#def-hwp-us-capacity-before) to
[53%](numbers.md#def-hwp-us-capacity-after) of the threshold [@fithian2026hardwired].

Loop gain shortens breakout at fixed compute. Barnett and Scher: "If there are AI's capable of
automating AI R&D, breakout times may be very short, even given limited compute"
[@barnett2025governance]. Davidson and Houlden's fixed-compute model gives about [57%](numbers.md#def-sie-p-compress-3yr) that full
automation of AI research compresses three years of progress into under one, and [18%](numbers.md#def-sie-p-compress-10yr) that it
compresses ten [@davidson2025sie]. These are modelled probabilities, conditional on that
automation existing.

Against, steelmanned. The memo's single-multiplier form ("physical compute times algorithmic
efficiency") may fail. Efficiency may depend on scale and on the reference algorithm
[@gundlach2025origin], so one rate would overstate the leak of a cap set far below the frontier and
understate it for innovations that change the scaling exponent; E1 neither confirms nor rules this
out. Ho et al. found compute carried [60%](numbers.md#def-ho-compute-share-low) to
[95%](numbers.md#def-ho-compute-share-high) of language-model progress [@ho2024algorithmic], which
supports a compute backbone, but on Epoch's capability index E1 finds compute explains only
[36%](numbers.md#e1-compute-share) of growth, and between [18%](numbers.md#e1-compute-share-subset-min)
and [63%](numbers.md#e1-compute-share-subset-max) with the choice of models. The residual is not
only uncertain but unidentified. The deepest objection is C*: T_b inherits all the uncertainty in
the distance to D1. One OOM of C* moves T_b by [2.3 years](numbers.md#comp-years-per-oom-ho) at Ho
et al.'s central rate, more than Part II's illustrative line of
[2.0 years](numbers.md#prot-line-declared). Barrett and Dannenberg's result says a disputed threshold
destroys the coordination D4 relies on [@barrett2012climate], and a T_b that the parties compute
differently is a disputed threshold.

### What the survey changed, and the prior work it must credit

The memo labelled the concept prior work and an AI version computed from measured inputs a
possible extension. The survey confirms the first and narrows the second. Breakout time is
arms-control vocabulary: enrichment capacity is "the key determinant of 'breakout time'", and
Sastry et al. take AI training as its analogue [@sastry2024compute]. Barnett and Scher define it for AI,
"the time it would take a country to develop dangerous AI capabilities"
[@barnett2025governance]; Scher et al. use it qualitatively [@scher2025agreement]; A Narrow Path
and the hardwired-pause group compute it from compute holdings [@miotti2025narrowpath; @fithian2026hardwired];
Gan computes it from a calibrated model [@gan2026clock]. Level 1 found every term of the AI version
in earlier work. Fleet accounting from holdings with research overhead, utilisation, an inference
multiple and an uncertainty allowance is the hardwired-pause group's [@fithian2026hardwired]; a
breakout-type time with a feedback term is Gan's [@gan2026clock]; additive accounting of
fine-tuning, extra inference and distillation against a training threshold is
[@pistillo2025loopholes]; the span set by cheap verification is [@villalobos2023tradeoff]; scale
dependence is [@gundlach2025origin]. The verifier-conditioned span and a distillation ceiling are
others' accounting rules, and the ceiling is wrong as a rule, since a student can exceed its teacher.
Label: extends prior work, as a combination. Tabulating breakout time in advance by holding class,
with an interval, is cut: E1 cannot identify the drift rate the interval needs. What may remain ours,
only if it is shown: one expression evaluated per path from verified holdings, with a measured rather
than assumed loop-gain term, that differs from a single-multiplier T_b by more than either's interval
for some holding class, or that backtests
([C2](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)).
Both tests are still to run.

### What it means for the protocol

T_b is the regime's central computed quantity. It is recomputed at each declaration, for each party
and each path, from agreed tables rather than case-by-case estimates, so that no party can argue
its way out of the line. It costs useful AI nothing directly; it is accounting. Its weakest
inputs, C* and the efficiency path, must be set conservatively (a low C*, a fast efficiency path),
which pushes the line toward caution and raises the cost to useful AI. That trade-off has to be
stated in numbers before the regime starts. The tables carry no interval that E1 could support.
Declared efficiency is self-reported, and the allowance for gains a party has not declared is
unsized, so on the declared path the line rests on the compute a chip count sees, not on the drift
term. For a party that hides its algorithms a tabulated T_b is too long by the hidden gain, and m
does not cover that, since m covers estimation error, not concealment.

### What would test it

E1 (compute against capability, and how fast a fixed cap leaks) has run and found the drift rate
not identified, which cut the interval tabulated in advance. E10 (the training-to-inference exchange
rate, with the distillation uplift), E15 (scale dependence at fixed algorithms), E18 (the cap leak,
backtested against the open-closed lag), E22 (the supply envelope) and E4 supply T_b's other terms
and are still to come. A specific test, C2(b):
compute T_b for a set of illustrative holdings under a single efficiency multiplier and under the
per-path expression, and report whether the two differ by more than either's interval and which
inputs drive the interval. Another, C2(c): backtest at past dates whether the expression predicts
the open-closed lag of [4 months](numbers.md#comp-open-closed-lag) within its interval. If neither
passes, D3 is prior work. The model already reproduces the published breakout figures of A Narrow
Path and the hardwired-pause group from their stated inputs; the tests extend that calculation with
loop gain.

## D4. Weapons-grade: the line T_b < m * T_r

### Operational definition

Restated after the survey. A holding H, or a system together with what it can reach, is
weapons-grade when

T_b(H) < m * T_r, where T_r = T_d(beta) + T_resp,

and:

- T_d(beta) is the regime's detection time: the time by which it detects the evader's best breakout
  path with probability 1 - beta, computed from its own channels as a minimum over evasion paths,
  not as a product over channels;
- T_resp is the response time, from a confirmed finding to an effective halt (chips disabled,
  weights seized, a run stopped); where it is random, a high quantile of it;
- m, at least 1, is a stated margin against error in T_b and T_r;
- beta is the tolerated chance that a breakout succeeds.

Everything with a longer breakout time is useful AI and may keep improving, provided each increment
passes through metered, human-held gates (D6). Both sides are in years.

The red team put three limits on this, now in the claims file
([C1](04-claims.md#c1-the-line-tb-m-td-tresp-with-tr-computed-not-chosen)). The test is per path
only where progress cannot move between paths; where a checkpoint can move, a strategy that switches
on a partial signal beat a line every path met, and the safe test is the shortest T_b against the
longest T_r. Beta bounds one attempt, so the regime must bound attempts or state its guarantee per
attempt. And while the untraced chip pool is open, its path fails the line for every party, so the
line separates no one until the pool closes ([P4](011-physical.md#p4-the-footprint-and-its-floor);
C8).

The definition must say whether it is a prevention line or a deterrence line, because the survey
shows the two differ by a large factor (below). This design chooses prevention for holdings near
the line. Superintelligence is an irreversible endpoint, and a deterrence line accepts that a
breakout succeeds with substantial probability whenever the breaker's payoffs make it worth trying.
Deterrence stays as the incentive layer for holdings far from the line.

The two forms connect. With detection arriving as a Poisson process at rate lambda, a breakout
succeeds only if it is not detected before T_b - T_resp, which has probability
exp(-lambda (T_b - T_resp)). Holding that at or below beta is the same as
T_b >= ln(1/beta) / lambda + T_resp = T_r. So D4 with m = 1 is the prevention condition in Gan's
response-window model [@gan2026clock], and m above 1 covers error in the inputs. The identity
follows directly from Gan's formula; it is not claimed as new, and `05-formal.md` states it with
its assumptions.

### How it is measured

T_b comes from D3. T_d comes from the regime's channels: their detection rates on each path, with
the evader choosing the path that minimises detection. Baker et al. argue that a regime's
detection probability is "approximately that of the subgoal with the lowest probability of
detecting a violation", because the evader needs to defeat only one [@baker2025verifying]. The
memo's product of independent miss probabilities holds only when every channel watches the same
path and fails independently. T_resp had no measured precedent (below); E24 has since measured the
arms-control record, and it bounds no response time.

Error comes from T_b's interval (D3), from each channel's rate (Part II), and from T_resp. A party
can fake its holdings, so T_b looks longer, or degrade channels, so T_d grows: both sides of the
inequality are contested. For scale: the memo's single placeholder channel, [4/yr](numbers.md#inspections-per-year) inspections each
catching a programme with probability [30%](numbers.md#detect-prob-per-inspection), needs [2.5 yr](numbers.md#def-placeholder-detect-time) to bring the miss chance down to [5%](numbers.md#def-prevent-beta),
before any response. Those rates were assumptions. E5 replaced them with a fitted historical
discovery rate of covert programmes, [0.094/yr](numbers.md#e5-hazard), counted from a programme's
start and an upper bound on a careful evader's rate; the memo's placeholder is
[12.8](numbers.md#e5-memo-over-hazard) times it. At that rate a path only the historical channels see
needs [32 years](numbers.md#e5-td-hist-years) to reach the same miss chance, a lower bound.

### Evidence for and against

The nuclear precedent is weaker than the memo said. The IAEA's 2001 glossary set timeliness
detection goals of [1 month](numbers.md#def-iaea-goal-unirr) for unirradiated direct-use material, [3 months](numbers.md#def-iaea-goal-irr) for irradiated direct-use material
and [12 months](numbers.md#def-iaea-goal-indirect) for indirect-use material, and said detection time "should correspond approximately to
estimated conversion times" [@iaea-glossary-2001]. Conversion times are [7](numbers.md#def-iaea-conv-metal-low) to [10 days](numbers.md#def-iaea-conv-metal-high) for
metal, [1](numbers.md#def-iaea-conv-irr-low) to [3 months](numbers.md#def-iaea-conv-irr-high) for direct-use material in irradiated fuel, and [3](numbers.md#def-iaea-conv-leu-low) to [12 months](numbers.md#def-iaea-conv-leu-high) for
low-enriched uranium [@iaea-glossary-2022]. In D4's terms the implied margin is [0.23](numbers.md#def-iaea-m-metal-low) to [0.33](numbers.md#def-iaea-m-metal-high)
for metal, [0.33](numbers.md#def-iaea-m-irr-low) to [1.00](numbers.md#def-iaea-m-irr-high) for irradiated fuel, and [0.25](numbers.md#def-iaea-m-leu-low) to [1.00](numbers.md#def-iaea-m-leu-high) for low-enriched uranium:
never above 1. And the goals cover detection only. Conversion time does not include "the time required to
assemble the device, nor any subsequent time period" [@iaea-glossary-2022]. Cochran concluded that "IAEA safeguards are
inadequate for achieving the objective of timely detection" and that there is "insufficient time"
for the Board to report to the Security Council [@cochran-2005]. The IAEA's own rationale is
deterrence "through the risk of early detection", which it calls "essentially non-quantifiable"
[@iaea-glossary-2022]. Its detection probability levels were [90%](numbers.md#def-iaea-detect-high) for "high" and [20%](numbers.md#def-iaea-detect-low) for
"low" [@iaea-glossary-2001].

The steelman for the nuclear model: it has worked for declared material. Baker finds that no state has
attempted to divert a significant quantity from a facility under comprehensive safeguards
[@baker2023nuclear], and IAEA accountancy found the DPRK's false declaration within about [9 months](numbers.md#def-dprk-discrepancy-months) [@iaea-gc37-1084].
Against it, for undeclared work: Iraq's programme went undetected for about [10 years](numbers.md#def-iraq-years)
[@albright-2002], Iran's centrifuge work for [17 years](numbers.md#def-iran-centrifuge-years) [@iaea-gov-2003-75], and Syria's reactor for
about [6 years](numbers.md#def-syria-years) [@iaea-gov-2011-30], each found by intelligence or disclosure rather than by the
inspectorate's own channels. Regimes also switch off: the DPRK gave notice of withdrawal from the
NPT [31 days](numbers.md#def-dprk-withdrawal-days) after a special inspection request [@iaea-gc37-1084]. For undeclared AI work, the
realistic T_r today is decades. E5 puts T_d alone at [31 years](numbers.md#e5-td-site-now-years) to
[32 years](numbers.md#e5-td-pool-years) on undeclared paths, lower bounds since its rate is an upper
bound, against [39.0 days](numbers.md#e5-td-declared-days) on the declared path; cloud and
distillation have no measured channel, so a breakout there is missed with certainty.

The response side is no better. E24 compiled the arms-control record: of
[8 findings](numbers.md#e24-halt-findings) made while the party was in its treaty,
[25%](numbers.md#e24-halt-share-never) were never followed by a halt. Halts took a Kaplan-Meier median
of [1.2 years](numbers.md#e24-halt-km-median-years), against the violator's fastest exit of
[31 days](numbers.md#e24-exit-min-days), and [67%](numbers.md#e24-halt-share-reversed) were later
reversed or shown incomplete. With more than 5% never halted, the response time has no finite 95th
percentile, so history bounds no T_resp. The red team found a second reason a computed T_resp fails:
a refusal under Part II's rules needs a finding by a quorum of rival states, a political decision, so
no response is free of one. A T_r computed per path from drilled latencies is therefore cut
([C1](04-claims.md#c1-the-line-tb-m-td-tresp-with-tr-computed-not-chosen)). Part II now lets a
licence lapse unless renewed, so a failed check stops a chip by design; any violation that needs
judging still adds a decision time no record measures.

The closest AI analogue of a timeliness goal, Shavit's target of catching a large training run
within [30 days](numbers.md#def-shavit-window) of completion with probability [90%](numbers.md#def-shavit-prob), is likewise a detection target untied to
breakout time [@shavit2023chinchilla].

Deterrence against prevention. Gan solves an AI pause game with Poisson detection inside a response
window. In his illustrative calibration, deterrence needs a monitoring rate of [0.0319/month](numbers.md#def-gan-deter-rate) over a
window of [12 months](numbers.md#def-gan-window), which detects a breakout with probability only [32%](numbers.md#def-gan-deter-detect), so that "at the threshold a
breakout still succeeds" with probability [68%](numbers.md#def-gan-deter-success) [@gan2026clock]. Holding breakout success to [5%](numbers.md#def-prevent-beta) in
the same window needs [0.25/month](numbers.md#def-gan-prevent-rate), [7.8](numbers.md#def-gan-prevent-multiple) times as much monitoring, on our arithmetic from his formula.
Coe and Vaynman show that, absent a trade-off between transparency and security, monitoring for
deterrence "never need be perfect" [@coe2020arms]. A deterrence line is cheaper; a prevention line
is what an irreversible endpoint calls for. The price of prevention falls as the window
T_b - T_resp grows, which is the argument for a margin.

The uncertain threshold. If the parties disagree about T_b, the line becomes uncertain, and in
Barrett and Dannenberg's experiment that collapsed cooperation [@barrett2012climate]. D4 is only as
strong as the agreement on how T_b is computed. That is why Part II agrees in advance how T_b is
computed. It cannot also agree an interval that holds, since E1 cannot identify the drift rate, so
each T_b is stated conditional on the agreed C* and conventions (D3).

### What the survey changed, and the prior work it must credit

The memo labelled D4 "new as a regulatory trigger, pending the search". The search found the
inequality. Barnett and Scher, writing of a Threat of Sabotage regime: "nations must be able to
detect and respond to dangerous AI development faster than any single country's breakout time"
[@barnett2025governance]. Gan formalises it as min{D + l, R} < T_catch, separating detection delay
from implementation delay, and shows the response window shrinks as compute grows: "agreements
have a clock" [@gan2026clock]. A Narrow Path sizes its thresholds so that breakout gives "ample time
to intervene" [@miotti2025narrowpath]. The hardwired-pause group chooses a breakout horizon of
[2 yr](numbers.md#def-hwp-horizon) as the time before "the rest of the world could react" and derives fleet thresholds from it
[@fithian2026hardwired]. Hendrycks et al.'s deterrence regime rests on detecting and sabotaging a bid for
dominance before it completes [@hendrycks2025superintelligence]. Meta names development that
outpaces evaluation as a loss-of-control outcome [@meta-ssf-v2-1-2026]. Canty et al. analysed
inspection games with a "critical time" for detection in 2001 [@canty2001timely] (abstract only).
The organising analogy itself, an IAEA for superintelligence with a threshold separating regulated
efforts from the rest, is in OpenAI's 2023 post [@openai2023governance].

The independent prior-art search found the inequality decades older than the AI papers. Sandia's
timely-detection condition for the physical protection of nuclear sites is evaluated per adversary
path and judged at the weakest path, with a response time built from measured parts at a high
quantile and a time margin, using EASI from 1977 [@snell2007itc20]. Nitze's 1988 standard asks that
verification detect a violation in time to respond [@hafemeister2008ctbt]. Time-based security in
cyber defence [@farhang2017tbs] and the process-safety rule for response times [@dearden2022sif]
state the same inequality, per-path analysis is safeguards practice [@allen-2015-llnl], and the
hardwired-pause group applies it per route with an uncertainty allowance [@fithian2026hardwired].

Label: prior work, applied. This is the largest downgrade from the memo. Credit physical protection,
Nitze, Barnett and Scher, Gan, A Narrow Path and the hardwired-pause group. Of the four candidates
the survey left, (i) the inequality as the definition of the line for systems and holdings is an
application to AI; (iii) a T_r derived from the regime's own channels and a measured response time
is physical-protection practice, and in AI it is cut, since every response waits on a political
decision; (iv) loop gain inside T_b belongs to D3. Only (ii) survives in a precise form: the margin m
as an error budget. If the estimates of T_b and T_r err in the unsafe direction by at most factors
e_b and e_r, an admitted holding is still stopped, per attempt, with probability at least 1 - beta
whenever e_b * e_r <= m, for any continuous detection hazard
([the formal file, C1](05-formal.md#c1-the-line-per-path)). It is one line of algebra, and the
safety-factor literature of structural engineering, which level 1 did not open, is its likeliest
earlier home. m covers estimation error only: not C*'s, which has no bound, and not error a party
introduces by understating its efficiency or delaying a response. Two corrections from the nuclear
record go with it: in safeguards a margin above 1 has no precedent, and neither does a T_r that
includes a treaty's response.

### What it means for the protocol

D4 is the line, and Part II hangs on it. Each limit exists to keep T_b at or above m * T_r for every
holding; each verification channel exists to shorten T_d; each response mechanism exists to shorten
T_resp. It also yields design rules. If every holding satisfies the line when a party withdraws,
response can begin at withdrawal, so a notice period matters only for holdings whose T_b fell
during membership, and must be paired with a freeze on assets acquired under the regime. The cost
to useful AI is set by m, beta and C*: a larger m, a smaller beta and a smaller C* each move more
holdings into the weapons-grade class. The weakest points are T_resp, for which the historical
record gives no finite quantile (E24) and no drill yet measures the licensors' decision time;
agreement on T_b; and the untraced pool, whose path fails the line for every party while it is open,
so that today the line binds only parties that choose to declare.

### What would test it

E5 (multi-channel verification) has run. It estimates T_d per path, with the evader taking the
path it is least likely to be caught on, and compares it with the product-of-channels form: for one
undeclared site the miss chance over a year is [40%](numbers.md#e5-pmiss-site-merged-1y) with
dependent channels merged, against [27%](numbers.md#e5-pmiss-site-indep-1y) if they were independent,
and the evader's best watched path is missed with probability [91%](numbers.md#e5-pmiss-max-1y). E24
is the piece this section asked for, response latencies from the arms-control record, and it found
no finite quantile (above). The tests that remain: E6 (defection and coalition games) has reproduced
the published games, but its Barrett and Dannenberg treatment with T_b drawn from an interval, which
tests whether a line defined by T_b >= m * T_r keeps compliance an equilibrium when T_b is uncertain,
is still to come. A drilled measure of the licensors' decision time is needed before any T_r can be
computed for a violation that needs judging, and no experiment yet plans one.

## D5. Elicited capability, robust to hiding

### Operational definition

Restated after the survey. For threshold purposes, a system's capability on a battery is its score
after a named elicitation protocol E, applied by the regime's evaluators with weight access or in a
fine-tuning enclave the parties trust. E names its methods, not only a compute share: supervised
fine-tuning on k on-distribution demonstrations, reinforcement learning with n samples, best-of-k
sampling, the strongest public scaffolds, and weight-level methods. E is revised on a schedule as
elicitation improves. Each E carries two measured rates:

- a miss rate: the share of model organisms with hidden capability above the threshold whose
  elicited score stays below it, measured over naive, RL-locked and tamper-resistant organisms built
  after E was fixed by builders blind to it, with adaptive organisms, built with E in hand, measured
  apart;
- a false-alarm rate: the share of benign models that E lifts over the threshold.

The guarantee is stated only over the capability range where E's methods work, which in practice
means where high-quality demonstrations exist, and only against hiding methods inside the sampled
population. Units: the score on the battery, and the two rates with their intervals.

### How it is measured

On model organisms whose hidden capability is known by construction: password-locked models,
prompted sandbaggers, RL-locked models, tamper-resistant ones. The method exists
[@greenblatt2024password; @taylor2025auditinggames]. A claim that a capability is absent is a
one-sided hypothesis test; a sequential test needs up to [40%](numbers.md#def-sprt-saving) fewer trials when the capability is
truly absent, and several widely cited negative findings are statistically underpowered
[@bukkapatnam2026absent] (abstract only). The budget changes the result: MLE-bench's medal rate
rose from [16.9%](numbers.md#def-mlebench-pass1) at one attempt to [34.1%](numbers.md#def-mlebench-pass8) at eight, [2.0](numbers.md#def-mlebench-ratio) times [@chan2024mlebench].

Who can measure: whoever holds the weights and can fine-tune them. Fine-tuning elicitation needs
deeper model access than external evaluators usually have [@aisi2025auditingblog].

### Evidence for and against

For: against naive locks, elicitation works with little data. A few high-quality demonstrations are
often enough to fully elicit password-locked capability [@greenblatt2024password]. In the UK AISI
auditing game, training-based elicitation "consistently elicited full performance from the
sandbagging models" with one on-distribution demonstration per task [@taylor2025auditinggames].
Anti-refusal training brought a sandbagging Claude 3.5 Sonnet from [36.1%](numbers.md#def-sabotage-degraded) back to [95.6%](numbers.md#def-sabotage-recovered) of its
original score [@benton2024sabotage]. Evaluation awareness is real and growing: Gemini 2.5 Pro tells evaluations from deployment with an
AUC of [0.83](numbers.md#def-evalaware-model-auc), against [0.92](numbers.md#def-evalaware-human-auc) for humans [@needham2025evalaware]. It threatens observed behaviour more than
scores obtained by fine-tuning, which is the case for judging on elicited capability.

Against, steelmanned: elicitation fails where D5 matters most. Without high-quality demonstrations,
fine-tuning may be "unreliable" [@greenblatt2024password]. A model locked against reinforcement
learning stayed suppressed for more than [500 GRPO steps](numbers.md#def-xh-rl-lock-steps) [@jang2026explorationhacking]. A tamper-resistant
organism recalled [7.8%](numbers.md#def-robust-hard-recall) on hard tasks after weak-to-strong fine-tuning, against [71.2%](numbers.md#def-robust-base-recall) for the
base model [@finke2026robustorganisms]. Weight grafting recovered [-11%](numbers.md#def-graft-circuit-broken) on a circuit-broken organism
[@le2026grafting]. Detectors tuned on fixed organisms fall to adaptive ones: a text audit's AUC
fell from [0.978](numbers.md#def-adaptive-auc-before) to [0.560](numbers.md#def-adaptive-auc-after) after two rounds of retraining [@soopal2026adaptive]. Above human expert
level demonstrations do not exist, so the guarantee weakens as capability approaches D1. Supervised
elicitation also assumes the model cannot hack its own gradients [@hubinger2023trusteval]. And
evaluations give lower bounds only; they cannot establish upper bounds, a limit that "cannot be
overcome within the current paradigm" [@barnett2024evaluations].

Elicitation also lifts honest models. In the auditing game the blue team "could not reliably
discriminate sandbaggers from benign models", classifying [1](numbers.md#def-audit-phase1-correct) and then [2](numbers.md#def-audit-phase2-correct) of [5](numbers.md#def-audit-models) models correctly, and
training-based elicitation was "prone to false-positives" because benign models gained about
[10 points](numbers.md#def-audit-benign-uplift) as well [@taylor2025auditinggames]. An elicited score mixes hidden capability with capability
the elicitation itself taught. That is a cost to useful AI.

### What the survey changed, and the prior work it must credit

The memo's label, extends prior work, stands, but the fixed budget is not ours. Anthropic's RSP
version 1.0 defined its ASL-3 threshold on capability reachable with post-training techniques
"corresponding to less than [1%](numbers.md#def-rsp1-elicitation-share) of the total training cost", with a [6](numbers.md#def-rsp1-buffer)x buffer
[@anthropic2023rsp]. Version 2.0 removed both in 2024, because "the science of evaluations is not
currently mature enough to make confident predictions about the precise buffer we should require"
[@anthropic2026rsp]. The EU Code of Practice requires "at least a state-of-the-art level of model
elicitation", matched to the misuse actors relevant to each risk and guarding against sandbagging,
with no budget and no miss rate [@gpai-code-of-practice-2025]. OpenAI regards any one-time
elicitation "as a lower bound, rather than a ceiling" and allows "a conservative upper bound" where
sandbagging is suspected [@openai2025preparedness]. The AISI game "does not provide
quantitative guarantees" [@taylor2025auditinggames]. Level 1 found the statistics older still:
sensitivity and specificity with exact one-sided bounds are diagnostic-test practice
[@fda2007diagnostic], and per-method rates with intervals exist for one elicitation method
[@abubaker2026fuzzing]. What remains, and level 1 confirmed the label: both rates per named budget,
over a defined population of organism kinds, as the pass-fail rule of a trigger rival parties run
([C5](04-claims.md#c5-elicited-capability-with-measured-miss-and-false-alarm-rates-per-named-budget)).
The red team then limited it. A population rate does not bound a strategic developer who picks a
hiding method outside the sampled population, and organisms built blind to E are weaker than ones
built by a developer who sees it. So the rates bound non-adaptive hiding only; adaptive organisms are
measured apart, as what a developer who sees E can build, and the claim is expected to fail on them.

One correction of substance. The EU code and OpenAI tie the budget to an adversary's capacity to
elicit. In Subcritical the party holding the weights is the one whose capability matters, and its
elicitation budget is its whole holding. So D5's budget is a measurement device, and D3 must add
what the holder could elicit with everything it has: post-training enhancements are worth [5](numbers.md#def-posttraining-low) to
[20](numbers.md#def-posttraining-high) times their compute [@heim2024thresholds].

### What it means for the protocol

D5 is the measurement step at declared checkpoints and before deployment. Its output places a
system's starting capability in D3. It requires weights to be open to the evaluators or to a
trusted enclave, which has a security cost [@coe2020arms]. Its cost to useful AI is the
false-alarm rate, which the protocol must publish. D5 must state the capability range it covers;
beyond that range, and against a developer who sees E and adapts, the protocol falls back on compute
(D3) rather than on evaluations. That fallback is costly to useful AI: E1 shows compute can misplace
a system by [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) on one benchmark.

### What would test it

E3 (hidden capability on small open models). Build password-locked, RL-locked and tamper-resistant
organisms on small open models, plus benign controls, with the builders blind to the elicitation
protocol. Run named budgets. Report the miss rate and the false-alarm rate with intervals, and how
both move with the budget, using a sequential test for absence. Adaptive organisms, built by a
separate team with E in hand, are scored apart. E3 has not run. The definition fails if no affordable
budget brings both rates below stated targets on RL-locked organisms, since naive locks alone are
prior work; it is expected to fail on tamper-resistant and adaptive ones, which fall outside its
guarantee.

## D6. Closure

### Operational definition

Restated after the survey. For each input to the next model (compute, weights, data, research
labour, money, and cross-party transfer of research results), closure is the share of increments of
that input, counted in its own unit (FLOP, weight updates, tokens, research tasks, dollars), that
the system or an AI-run process obtained without passing a human-held gate whose passage is logged
and can be verified by the regime, over an audit period. A loop is closed in an input when that
share exceeds a stated level. The gates are named: licence renewal and cloud know-your-customer
checks for compute; declared weight hashes for weights; acquisition logs for data; human approval of
training launches and merges for research labour; know-your-customer checks on payment rails for
money. A narrow system whose outputs feed a covered system's training, code or compute counts as
part of it. Gates count the agent's completed horizon-length tasks, not hours: a time horizon is
measured in human time [@kwa2025horizon], and an agent that finishes a horizon-length task in minutes
could chain several between gates a horizon apart on the clock
([C11](04-claims.md#c11-closure-judged-input-by-input-with-narrow-optimisers-inside-the-loop)). The
unit is a share per input.

D6 can be read as a decomposition, input by input, of Burtsev's operational closure chi: "Only
part of the potential recursive gain may survive the full development pipeline. We denote this
transmitted fraction by the operational closure chi" [@burtsev2026criticality]. Whether chi
factors this way is a candidate, not a result. The formal file corrects how it would factor: the
loop transmits the exponent K, in which closures add, weighted by each input's share, as in the
task-based automation model [@aghion2017ai]; under complements the least-closed input comes to set
K, under substitutes the most-closed
([the formal file, C11](05-formal.md#c11-closure-by-input-the-combination-rule)). Until an
experiment decides which holds, the safe bound takes the largest closure among ungated inputs, and
under it the rule is to gate every highly closed input together, which is prior work
[@scher2026research].

### How it is measured

By audit. The regime samples increments of each input and checks that a gate was passed and
logged. A gate that passes everything is not a gate, so the audit also seeds requests that a
working gate must refuse, and those requests must be indistinguishable from real ones to whoever runs
the pipeline, or a gate that approves every request it does not recognise as a test will measure as
working. Gates on compute and money can be checked against existing records. Gates
on research labour are hard to check: the main evidence of how much AI research work AI leads is a
developer's self-report [@anthropic2026pace].

### Evidence for and against

For: the gates that exist are holding. On the UK AISI's self-replication evaluations, success rose
from under [5%](numbers.md#def-replibench-2023) in early 2023 to over [60%](numbers.md#def-replibench-2025) by summer 2025. The tasks are simplified, and AISI judges models
"currently unlikely to succeed in real-world conditions" [@aisi2025trends]. Models struggle
with know-your-customer checks and robust persistent deployment [@black2025replibench]. Those are
human-held gates. The protocol can stand on them.

Against, steelmanned: D6 may be framing. It adds no quantity that chi does not already name, and
its gates are the ones compute-governance proposals already have. Its list of inputs may not be
complete: Scher catalogues [28 mechanisms](numbers.md#def-scher-mechanisms) for verifying restrictions on frontier AI research and argues
that a durable halt must hold compute, algorithms and data together "so that advances in one input
do not counteract restrictions on another" [@scher2026research] (abstract only). And coupling
crosses actors. Burtsev shows that blocs each subcritical alone can be supercritical together
through transfer, with a spectral radius of about [1.15](numbers.md#def-burtsev-network-rho) in one scenario [@burtsev2026criticality];
Davidson et al. prove the analogous result for coupled loops [@davidson2026feedback]. Closure
measured party by party misses closure across parties.

### What the survey changed, and the prior work it must credit

The memo feared D6 might be framing rather than substance, and the survey half agrees. Burtsev
names and parameterises closure [@burtsev2026criticality]. Chen et al. classify self-improvement
loops by how closed the loop is [@chen2026rsisurvey]. A Narrow Path prohibits "the direct use of
found systems to build new found systems" [@miotti2025narrowpath]. The red-lines campaign gives
self-replication and self-improvement without explicit human authorisation as example lines
[@redlines-2025]. California and New York define "evading the control of its frontier developer"
as a catastrophic risk [@ca-sb53-analysis-2025; @ny-a9449-2026]. Level 1 found more: the rule
combining closures is the task-based automation model applied to the inputs of AI research
[@aghion2017ai], and counting a narrow optimiser inside the loop recasts A Narrow Path's ban on found
systems building found systems [@miotti2025narrowpath]. Label: extends prior work, narrowly; framing
until tested. What may remain ours: closure measured input by input against gates the regime can
verify, with the cross-party edge (transfers of AI research advances) as one more input, and the
prediction of the gain under any set of gates from closures measured one gate at a time. The red
team found that under the safe bound the decomposition reduces to holding every input together, so it
adds something only if the one-gate-at-a-time prediction holds in an experiment. Two 2026 works found
but not yet opened could decompose closure by input, and must be opened before this is claimed.

### What it means for the protocol

D6 says where the protocol stands: one gate per input, and one on cross-party transfer. A closed
input enters D3 as an unmetered resource and shortens T_b. Gates on compute and money are cheap and
mostly exist. Gates on research labour slow research and are the expensive ones, which favours
gating research labour only on frontier-scale training research, where D2 says the loop could
close.

### What would test it

E4(d): inside E4's staged run, put a logged gate on each input (a human or an automated verifier
that can refuse) and measure the gain transmitted with each gate on and off; the ratio estimates that
input's share in closure for that setting. D6 passes if the gain with gates on any subset is
predicted, within its interval, from closures measured one gate at a time; if not, closure by input
is framing and is cut. Add a gate audit: seed requests that a working gate must refuse (a compute
purchase without valid identity, an unapproved training launch), indistinguishable from real ones,
and measure the share refused, in the manner of the self-replication evaluations. E4(e) runs the loop
with and without a narrow optimiser aimed at the training stack. Neither has run.

## The definitions after the survey

The labels are claims about our search and level 1's, not about the world. The last column is what
survived the independent prior-art search and the red team, each piece still facing levels 5 and 6
([the claims file](04-claims.md#summary)), not an established contribution.

| Definition | Memo's label | Label after verification so far | Closest prior work | What remains possibly ours |
|---|---|---|---|---|
| D1 superintelligence, the endpoint | Extends prior work | Extends prior work, more narrowly than the memo said; a definition only | Genewein et al. 2026 [@genewein2026agiasi]; Ngo 2023 [@ngo2023tagi]; Anthropic RSP v3.4 [@anthropic2026rsp]; Aguirre 2025 [@aguirre2025ktfh]; RE-Bench [@wijk2024rebench]; Robinson 2026 [@robinson2026horizons] | As a definition, which cannot warn: time and money matched together against an organisation; a refreshed, regime-held battery with institutional baselines across decisive clusters; the alpha fraction; t* censored at the largest tested budget (C10) |
| D2 loop gain | Condition prior work; estimator may be new | Prior work for the condition and its use as a trigger; extends prior work narrowly for the estimator; as a trigger, cut on current evidence | Cunningham et al. 2026 [@cunningham2026rsi]; Burtsev 2026 [@burtsev2026criticality]; a staged AI research loop [@srikanth2026aide2]; the upper-bound rule in epidemics [@blumberg2020supercritical]; Anthropic and OpenAI rate triggers [@anthropic2026rsp; @openai2025preparedness]; METR 2026 [@metr-anthropic-acceleration-2026] | The exact round identity as the estimator of K for a staged loop at fixed inputs, and the budget ladder: a measurement whose decision power is unshown (C4) |
| D3 breakout time | Concept prior work; AI version may extend it | Extends prior work, as a combination | Hardwired-pause working paper [@fithian2026hardwired]; Gan 2026 [@gan2026clock]; Pistillo and Villalobos [@pistillo2025loopholes]; Villalobos and Atkinson [@villalobos2023tradeoff]; Barnett and Scher 2025 [@barnett2025governance]; A Narrow Path [@miotti2025narrowpath]; IAEA conversion time [@iaea-glossary-2022] | One per-path expression from verified holdings with a measured loop-gain term, only if it beats a single multiplier or backtests (C2(b), (c)); tabulating it in advance with an interval is cut, the drift rate being unidentified (C2(a)) |
| D4 the line, T_b < m * T_r | New as a regulatory trigger | Prior work, applied | Sandia physical protection [@snell2007itc20]; Nitze's standard [@hafemeister2008ctbt]; Gan 2026 [@gan2026clock]; hardwired-pause working paper [@fithian2026hardwired]; Barnett and Scher 2025 [@barnett2025governance]; A Narrow Path [@miotti2025narrowpath]; IAEA timeliness [@iaea-glossary-2001] | The application to AI holdings; the margin as a multiplicative error budget, a small lemma (C1(b)); T_r computed from drilled latencies is cut (C1(c)) |
| D5 elicited capability | Extends prior work | Extends prior work | Diagnostic-test practice [@fda2007diagnostic]; Anthropic RSP v1.0 budget, later dropped [@anthropic2023rsp]; EU Code of Practice [@gpai-code-of-practice-2025]; OpenAI Preparedness v2 [@openai2025preparedness]; password-locked models [@greenblatt2024password]; AISI auditing game [@taylor2025auditinggames]; tests of absence [@bukkapatnam2026absent] | Miss and false-alarm rates per named budget over a defined organism population, as the rule of a trigger rival parties run, valid against non-adaptive hiding only (C5) |
| D6 closure | May be new; may be framing | Extends prior work, narrowly; framing until tested | Task-based automation [@aghion2017ai]; Burtsev 2026 [@burtsev2026criticality]; Chen et al. 2026 [@chen2026rsisurvey]; A Narrow Path [@miotti2025narrowpath]; Scher 2026 [@scher2026research]; Global Call for AI Red Lines [@redlines-2025] | Closure measured input by input against verifiable gates, including the cross-party transfer edge, and the gain under any set of gates predicted from one gate at a time (C11) |

Two ideas outside D1 to D6 also turn out to be prior work: the memo's organising idea, an
IAEA-style line between permitted and regulated AI [@openai2023governance; @sastry2024compute], and
the criticality metaphor behind the project's name [@yudkowsky2013iem; @burtsev2026criticality].

## The five perspectives that follow

Each chapter explains the mechanisms that feed one or more of these definitions.

- [`011-physical.md`](011-physical.md): compute, energy, memory, bandwidth and the physical footprint;
  the physical terms in D3 and the detectability behind T_d in D4.
- [`012-computational.md`](012-computational.md): scaling, algorithmic progress, the exchange between
  training and inference, data, search; the efficiency path in D3 and the cap leak.
- [`013-dynamical.md`](013-dynamical.md): the feedback loops, runaway against saturation, coupling;
  what D2 measures and how loops shorten D3.
- [`014-cognitive.md`](014-cognitive.md): the kinds of advantage, the decisive functions, narrow
  against general; what D1's battery must contain.
- [`015-organisational.md`](015-organisational.md): the supply of inputs, races, chokepoints and
  covert supply; where D6's gates can stand and which undeclared paths D3 must count.

## What this perspective contributes to the line

This chapter gives the protocol four quantities to trigger on, limit or measure, and one endpoint they
protect. D1 is the endpoint, not a trigger.

1. **The breakout-to-response ratio, T_b / T_r, for each holding class (D3 with D4).** Trigger when
   it falls below m. Measured from verified holdings through agreed tables, stated conditional on
   the agreed C* and with no interval E1 could support (D3), and from channel detection rates with
   the evader on its best path plus a response time (D4). Weakest point: the effective compute that
   reaches D1 and the path of algorithmic efficiency are unknown, E1 cannot identify the drift rate,
   and a T_b the parties compute differently is an uncertain threshold, which in experiment
   destroyed cooperation. Second weakest: the response time. History bounds none (E24), every
   judged response waits on a political decision, and no drill measures it, so the line has no
   computable right side for any violation that needs judging. Third: on undeclared paths T_d is
   decades (E5), and while the untraced pool is open its path fails the line for every party.
2. **The loop's gain K at fixed inputs, measured (D2).** Estimated from consecutive round gains by
   the exact round identity and a budget ladder, in staged runs on declared checkpoints, and
   combined with a capability ladder. It is a measurement design, not a trigger: at the calibrated
   noise E4 found the rule on K fires about as often on a loop well below 1 as on one above it, the
   interval under-covers, the estimates lean subcritical and two held-out sets do not fix them.
   Until E4(b) shows real staged rounds tight enough for the upper bound to separate loops below 1
   from loops above, closed-loop training research on frontier systems is restricted outright, the
   prior-work rule. Weakest point: the noise of a real round, which no run has measured; transfer
   from small-scale runs to the frontier; and an agent that sandbags the test, which E4 shows can
   silence the bound by withholding a small share of its gain.
3. **The elicited score, with its miss rate and false-alarm rate (D5).** Use it to place each
   declared system in D3. Measured on regime-held batteries with weight access. Weakest point: the
   rates bound only non-adaptive hiding, there is no guarantee above expert level, where
   demonstrations run out, and hardened locks defeat current methods.
4. **Closure per input (D6).** Limit by requiring a verified gate on each input and on cross-party
   transfer, with gates counted in the agent's completed horizon-length tasks. Measured by audit
   with seeded refusals that look like real requests. Weakest point: gates on research labour rest
   on self-reports, and closure by input is framing until E4(d) tests it.

Four changes to the protocol follow from this chapter. D4 must be a prevention line near the
threshold, and must budget for the monitoring that costs (several times what deterrence needs at
Gan's calibration). T_r must include response. Physical protection times a response, against a
site's guard force [@snell2007itc20], but for a treaty's response only the arms-control record
measures one, and it gives no finite quantile (E24); until a drill measures the licensors' decision
time, a licence lapses unless renewed, so that a failed check stops a chip without a decision. The
way T_b is computed must be agreed by holding class before it is needed, as conversion times are,
so that the line is not disputed case by case; an interval tabulated in advance is cut, so each T_b
is stated conditional on the agreed C* and conventions. And the protocol must say plainly that the
safeguards precedent it borrows accepted a margin below 1 and timed detection only.
