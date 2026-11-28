# Part I, 2: The computational and algorithmic perspective

This perspective asks how compute turns into capability, and how much of a limit on compute leaks
through other routes. It matters for the line between useful AI and the path to superintelligence
because the protocol's backbone is a limit on compute: chips are countable, fabs are few, power is
visible. A limit on training compute holds only as long as capability cannot be bought some other
way. Four other ways are on the table: better algorithms at the same compute, inference spent at run
time, post-training enhancement, and distillation from a stronger model. Data and search decide
where those routes pay and where they stop.

The line itself is drawn by time (D4 in `research/00-memo.md`): a holding is weapons-grade when its
breakout time is shorter than the regime's time to detect and respond, with a margin. This chapter
supplies the computational terms inside breakout time: how fast a fixed cap leaks, how much leaks at
once, and which of those leaks a chip count can see.

The survey changed the memo in four places. Each is argued below, with its sources.

1. Algorithmic progress is not one settled multiplier on physical compute. Ablations find most of it
   scale-dependent, which would make a cap's leak rate depend on where the cap sits. E1 did not find
   the predicted rise with scale, and could not identify the rate at all: across six samples of the
   same models it ran from [2.6](numbers.md#e1-algo-annual-subset-min)x to
   [1,512](numbers.md#e1-algo-annual-subset-max)x a year (A3).
2. Compute explains most of the difference between frontier models. "Unbounded scaling is not
   necessary, algorithms substitute" is weaker than the memo assumed; algorithms complement compute
   more than they replace it at the frontier (A1, A3). Compute's share of growth over time is another
   matter: in E1 it explains [36%](numbers.md#e1-compute-share) of growth on Epoch's index, and from
   [18%](numbers.md#e1-compute-share-subset-min) to [63%](numbers.md#e1-compute-share-subset-max)
   across six samples, so that share is not identified on public data.
3. Inference leaks a training cap by roughly one order of magnitude per technique, at a price in
   inference compute, and by more only where a cheap verifier exists (A2). The ability to improve
   from one's own outputs also grows with pretraining compute, so a compute cap partly caps
   self-improvement too (A4, A5).
4. Distillation from a stronger model moves capability across a cap more cheaply than
   reinforcement learning (RL) on the same base. An uncapped model's outputs are therefore an input
   the protocol has to control (A2).

The framing of A2, that a training cap leaks through inference, is prior work, and so is a leak
tied to a breakout horizon. So is each term of the leak model set out after A5: a scale-dependent
algorithmic rate, the one-off post-training jump, inference spans conditioned on a verifier, and
distillation. Joined in one expression, with each leak sorted by whether the chip channel can see it,
they are a combination of prior work, C2 in
[the claims file](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case),
now downgraded to an accounting frame that claims nothing. Tabulating it in advance with an
interval is cut, since E1 cannot identify the drift rate, and E18 left neither of the predictions
that could have added something: its backtest cuts against the expression, and its gain over one
multiplier is not shown.

Conventions. Every number is a ledger link. Multipliers are written with an x after the number. OOM
means an order of magnitude, a factor of ten. Where the survey read only a source's abstract, the
text says "(abstract)". Nothing in this chapter has been tested against an adversary, and the
protocol consequences are candidates. Of the experiments named, E1 and E9 have run, and their results
are given under A1 and A3; E5 has run, and the combined leak's test draws on it; E18 has run, and its
result is under the combined leak. E10, E15, E16 and E17, numbered as in the claims file, are
planned, not run.

## A1. Capability as a function of effective compute

### Definition

Capability C of a trained model is its score on a single stitched scale built from many benchmarks,
with benchmark difficulties fitted jointly (the Rosetta scale [@ho2025rosetta] or the Epoch
Capabilities Index [@epoch2025eci]). It is measured under a fixed elicitation budget (D5) and a
fixed inference budget per task, which A2 varies separately. Physical training compute F is the
floating-point operations executed for the run, pretraining and post-training together, on every
chip the run used. Effective compute is F multiplied by an efficiency relative to a stated reference
algorithm at the same scale. The mechanism A1 names is the function C(F, t), and in particular its
slope: capability gained per OOM of physical compute at a given date.

The system boundary is one trained model and the scaffold it is evaluated in. Several models, or a
model plus tools it can train, are outside A1 and inside A2 and the dynamics chapter.

### How it is measured

F is measured from chip-hours, peak throughput and utilisation, or estimated from parameters and
training tokens at [6 FLOP per parameter per token](numbers.md#comp-flop-per-param-token)
[@kaplan2020scaling].
Capability is measured by running the stitched battery. The developer knows F exactly; outsiders
know it through chip accounting and power, which the physical chapter and Part II treat. A developer
can under-report F, and mixtures of experts, quantisation and shared pretraining make FLOP ambiguous
[@hooker2024thresholds]. Capability can be hidden by sandbagging, which D5 addresses, and inflated by
contamination.

The measurement error that matters is forecast error. Across
[5 OOM](numbers.md#comp-owen-oom-span) of compute, extrapolating BIG-Bench Hard one OOM ahead missed
by [6 pp](numbers.md#comp-bbh-mae-1oom) on average, and a single task by
[18 pp](numbers.md#comp-task-mae-1oom) (abstract) [@owen2024predictable]. Aggregate capability is
predictable from compute. Any one task is not.

### Evidence for and against

*Scaling laws.* Loss falls as a power law in parameters, data and compute [@kaplan2020scaling].
Kaplan et al. put compute-optimal model size at C to the power
[0.73](numbers.md#comp-kaplan-n-opt-exp); Chinchilla overturned that, finding earlier large models
"significantly undertrained" (abstract) [@hoffmann2022chinchilla]. A replication found Chinchilla's
third fitting method inconsistent with its first two, with confidence intervals that would need
about [600,000 experiments](numbers.md#comp-chinchilla-ci-experiments). Its refit gives an exponent
of [0.51](numbers.md#comp-chinchilla-refit-a), against Hoffmann et al.'s
[0.45](numbers.md#comp-chinchilla-hoffmann-a), and about
[20 tokens per parameter](numbers.md#comp-chinchilla-tokens-per-param) rather than the
[70 tokens per parameter](numbers.md#comp-hoffmann-tokens-per-param) the original fit implied
[@besiroglu2024replication]. These are the parameters to use. Deployed models sit off this optimum
on purpose: with heavy inference demand it pays to train smaller and longer, and quality was still
rising at [10,000 tokens per parameter](numbers.md#comp-sardana-tokens-per-param) (abstract)
[@sardana2024beyondchinchilla]. Training FLOP alone therefore under-counts capability per parameter
in deployed models.

*Observational scaling.* Across about [100 models](numbers.md#comp-observational-models), benchmark
performance is a function of a low-dimensional capability space, and agent performance can be
predicted from simpler non-agentic benchmarks (abstract) [@ruan2024observational]. The Rosetta scale
puts models and benchmarks on one axis without assuming how capability moves with time. Its
capability rises by [0.168](numbers.md#comp-rosetta-k) units per natural-log unit of training FLOP,
which is [0.39 units per OOM](numbers.md#comp-rosetta-per-oom). Frontier capability grows
[0.55 units/yr](numbers.md#comp-rosetta-frontier-growth) (95% CI
[0.45 units/yr](numbers.md#comp-rosetta-frontier-growth-lo) to
[0.67 units/yr](numbers.md#comp-rosetta-frontier-growth-hi)), and capability at fixed compute grows
[0.3 units/yr](numbers.md#comp-rosetta-fixed-growth), between
[0.1 units/yr](numbers.md#comp-rosetta-fixed-growth-lo) and
[0.5 units/yr](numbers.md#comp-rosetta-fixed-growth-hi) across model families [@ho2025rosetta].

Two checks show the reading is coherent. Fixed-compute growth divided by the compute slope gives a
compute-equivalent gain of [6.0](numbers.md#comp-rosetta-implied-algo)x a year, which is the paper's
own figure of about [6](numbers.md#comp-rosetta-algo)x [@ho2025rosetta]; that only works if the
slope is per natural log, so the ledger reads it that way. And the frontier growth left over after
the fixed-compute part implies frontier compute growing
[4.4](numbers.md#comp-rosetta-implied-compute-growth)x a year, inside Epoch's measured
[5](numbers.md#comp-frontier-compute-growth)x (90% CI
[4](numbers.md#comp-frontier-compute-growth-lo)x to
[6](numbers.md#comp-frontier-compute-growth-hi)x) [@epoch2026trends].

*Emergence.* If capabilities jump between checkpoints, a compute-keyed trigger can be overrun. Wei
et al. define abilities absent in smaller models and present in larger ones (abstract)
[@wei2022emergent]. Schaeffer et al. show that over
[92%](numbers.md#comp-emergence-two-metric-share) of claimed emergent abilities on BIG-Bench come
from two discontinuous metrics, and that continuous metrics give smooth curves
[@schaeffer2023mirage]. Fine-tuning moves emergence to smaller models, and small fine-tuned models
predicted emergence up to [4](numbers.md#comp-emergence-ahead)x more compute ahead in some cases
(abstract) [@snell2024emergence]. The residue is real: a threshold that is itself a pass-fail task is
a discontinuous metric, and the protocol cares about such thresholds.

*How much is compute?* This is where the memo's pathway table is weakest. From 2012 to 2023,
[60%](numbers.md#comp-ho-compute-share-lo) to [95%](numbers.md#comp-ho-compute-share-hi) of
language-model gains came from compute scaling and the rest from algorithms [@ho2024algorithmic].
Across [809 models](numbers.md#comp-mertens-models), [80%](numbers.md#comp-mertens-frontier-share-lo)
to [90%](numbers.md#comp-mertens-frontier-share-hi) of performance differences at the frontier are
explained by training compute, though away from the frontier shared and proprietary techniques
substantially cut the compute needed, and efficiency within one firm can differ by more than
[40](numbers.md#comp-mertens-firm-spread)x (abstract) [@mertens2026secretsauce].

The steelman for the memo's side is real and should be stated. The Rosetta decomposition, which
includes post-training and so counts more than pretraining loss, attributes only
[45%](numbers.md#comp-rosetta-compute-share) of frontier capability growth to compute, and the range
across families runs from [9%](numbers.md#comp-rosetta-compute-share-lo) to
[82%](numbers.md#comp-rosetta-compute-share-hi). Ho et al. measure growth over time in pretraining
loss; Mertens et al. measure differences across models at one time; the Rosetta split measures growth
in a broad capability. They answer different questions, and the third leaves much more room for
algorithms. Diminishing returns to compute would also let capped and uncapped parties converge
(abstract) [@gundlach2025meek]. The honest summary: compute dominates differences at the frontier,
while the share of growth over time due to algorithms runs from
[5%](numbers.md#comp-ho-algo-share-lo) to [40%](numbers.md#comp-ho-algo-share-hi) for pretraining loss
to about [55%](numbers.md#comp-rosetta-algo-share) for broad capability, depending on what capability
means.

*What E1 found.* E1 joins Epoch's model data to its capability index [@epoch2026aimodels;
@epoch2025eci] for the [105 models](numbers.md#e1-models) that have both. Training compute explains
[36%](numbers.md#e1-compute-share) of growth on the index, and the rest moves with date at about
[17](numbers.md#e1-algo-annual)x a year in compute-equivalent. Across six samples of the same models
the share runs from [18%](numbers.md#e1-compute-share-subset-min) to
[63%](numbers.md#e1-compute-share-subset-max), far beyond any one sample's interval, so compute's
share of growth is not identified on public data, which lacks a compute estimate for
[23 models](numbers.md#e1-top25-dropped) of the 25 with the highest index. One OOM beyond the fitting
range, forecasts missed by [11.8 ECI points](numbers.md#e1-oos-mae) on average, which is
[0.96 OOM](numbers.md#e1-oos-mae-oom) of compute-equivalent (an understatement, L4 found, since it
divides by a slope fitted on the forecast models too), and by [17.0 pp](numbers.md#e1-oos-bench-mae-pp)
per benchmark score, against a floor of [5.2 pp](numbers.md#e1-oos-bench-floor-pp) with the model's
actual index. The actual index exceeded the one-sided 95% upper bound in
[1.1%](numbers.md#e1-oos-unforecast-share) of [89 forecasts](numbers.md#e1-oos-n), one model: the
bound is wide, not shown to be calibrated. At the top of the range the fit overshoots: for the
[13 models](numbers.md#e1-oos-n-1e25) in the highest decade forecast, the mean signed error is
[-8.5 ECI points](numbers.md#e1-oos-bias-1e25). Compute also places systems badly. On GPQA Diamond the
largest model that loses to PhD experts used [2.8 OOM](numbers.md#e1-gpqa-overlap-oom) more training
compute than the smallest that wins, and the best single compute threshold gets
[79%](numbers.md#e1-gpqa-acc-compute) of verdicts right, against
[92%](numbers.md#e1-gpqa-acc-date) for the best release date.

### What the survey changed from the memo

A1 is prior work in every part: scaling laws [@kaplan2020scaling; @hoffmann2022chinchilla;
@besiroglu2024replication], observational scaling [@ruan2024observational], predictability
[@owen2024predictable] and a stitched scale with a stated compute slope [@ho2025rosetta]. The memo's
D3 writes effective compute as "physical compute times algorithmic efficiency". A1 shows that the
compute slope is stable enough to build on; A3 shows that the efficiency term is not a single
number. And the pathway table's "unbounded scaling: not necessary, algorithms substitute" is weakened
by Ho et al. and Mertens et al.: at the frontier, scale is most of the story.

### What it means for the protocol

A candidate, not a finding. Training compute stays the first filter, as Heim and Koessler argue for
regulation generally [@heim2024thresholds]: it is quantifiable, measurable early and externally
verifiable. E1 shows what it costs: compute misplaced systems by up to
[2.8 OOM](numbers.md#e1-gpqa-overlap-oom) on one benchmark, so a filter on compute alone must sit far
below the line, at a real cost to useful AI, and capability measured at checkpoints has to do the
placing. Capability on a stitched scale is the second stage. Two rules follow from the forecast
error. First, evaluations must come at intervals shorter than the distance over which forecasts hold,
which is about one OOM with the errors above, and less with E1's. One lab's policy evaluated every
[4](numbers.md#comp-rsp-cadence)x of effective compute [@anthropic2026rsp], the same distance at
which emergence was sometimes predictable [@snell2024emergence]; that is a reasonable default for
declared checkpoints. Second, thresholds should be stated on continuous metrics with the pass-fail
version reported alongside, so that a jump on the threshold metric is not mistaken for a jump in
capability. The cost to useful AI is the cost of evaluation, which is small.

### What would test it

E1 has run; its results are under the evidence above. It joined Epoch's model data (training
compute, dates) [@epoch2026aimodels] to the Epoch Capabilities Index scores [@epoch2025eci], fitted
capability against log compute with a date term, as in the Rosetta paper, on models below a compute
cut, and forecast the models one OOM above it, overall and per benchmark, against Owen's
[6 pp](numbers.md#comp-bbh-mae-1oom) and [18 pp](numbers.md#comp-task-mae-1oom), with the
decomposition recomputed by resampling. The hypothesis was to fail if one-OOM forecast error on the
stitched scale were large enough that a threshold set one evaluation interval ahead is crossed
unforecast more than a stated fraction of the time. It did not fail on that count, but only because
the bound is wide: one forecast in [89 forecasts](numbers.md#e1-oos-n) crossed it, and the fit
overshoots at the top. A bound that wide cannot place a threshold one interval ahead with any
precision. What is left to test needs data the public set lacks: compute estimates for the most
capable models.

## A2. The exchange rate between training and inference compute

### Definition

Hold a task family and a capability level fixed. The exchange rate is the slope of log inference
compute per task against log training compute along that iso-capability curve: OOM of inference
needed to replace one OOM of training. The span is the range of training compute, in OOM, over which
the trade holds before it stops. Both are defined per technique (sampling and voting, search,
repeated sampling with a verifier, longer reasoning, RL) and conditional on the cost of verifying an
answer. Inference compute here includes everything spent at run time on one task: samples, search
nodes, reasoning tokens and verifier calls.

The leak of a training cap through inference is then the training compute, in OOM, that a party
can replace by spending inference, bounded by the span and priced by the exchange rate.

### How it is measured

On small open models: train a family at several compute levels, and for each, measure capability as
a function of inference budget; the iso-capability contours give the rate and the span, as Jones did
for AlphaZero on Hex [@jones2021boardgames]. From published curves: Villalobos and Atkinson collected
per-technique spans [@villalobos2023tradeoff]. Anyone with open models can measure it; the error is
dominated by the choice of task and of verifier.

Inference spent at deployment runs on chips, so in principle the chip channel sees it. Two caveats.
Distributed RL already generates its rollouts on a permissionless swarm of heterogeneous
contributors, consumer GPUs among them, with each rollout checked by a verification scheme and the
training nodes kept central [@primeintellect2025intellect2]. And open models that fit one consumer
GPU match the frontier with a lag of [6 months](numbers.md#comp-consumer-lag-lo) to
[12 months](numbers.md#comp-consumer-lag-hi) [@somala2025consumergpu]. Inference on unregistered
hardware is invisible to chip accounting, though one analysis judges that dangerous inference may
only be feasible on large clusters that are already monitored [@barnett2026closingwindow].

### Evidence for and against

*Measured exchange rates.* On Hex, each additional OOM of train-time compute eliminates about
[15](numbers.md#comp-hex-test-saved)x of test-time compute, linear in log compute
[@jones2021boardgames]: one OOM of training replaces [1.18 OOM](numbers.md#comp-hex-exchange-oom) of
inference. The minimum compute for perfect play grows
[7](numbers.md#comp-hex-perfect-play-growth)x per board-size increment, so closed domains get
expensive fast. Across techniques, each saves about
[1 OOM](numbers.md#comp-tradeoff-typical-oom) in training or inference for somewhat more than that
of the other [@villalobos2023tradeoff]. Monte Carlo tree search trades
[1.6 OOM](numbers.md#comp-span-mcts-train) of training against
[1.6 OOM](numbers.md#comp-span-mcts-inf) of inference, and its span shrinks to zero near perfect
play. Repeated sampling with an expensive verifier trades [1 OOM](numbers.md#comp-span-expver-train)
for [1.45 OOM](numbers.md#comp-span-expver-inf), a rate of
[1.45 OOM](numbers.md#comp-exchange-expver) of inference per OOM of training. Scaling the policy spans
[1.2 OOM](numbers.md#comp-span-policy-train) of training against
[0.7 OOM](numbers.md#comp-span-policy-inf) of inference and cannot save training at all. The outlier
is repeated sampling with a cheap verifier: [3 OOM](numbers.md#comp-span-cheapver-train) of training
for [6 OOM](numbers.md#comp-span-cheapver-inf) of inference, a rate of
[2.0 OOM](numbers.md#comp-exchange-cheapver) of inference per OOM of training, with a span that grows
with scale. That figure is extrapolated, and its authors give it low confidence.

*Difficulty decides.* Compute-optimal test-time scaling beats best-of-N by more than
[4](numbers.md#comp-snell-vs-bestofn)x, and with FLOPs matched a small model can outperform one
[14](numbers.md#comp-snell-larger-model)x larger where its own success rate is non-trivial
[@snell2024testtime]. But on hard questions "pretraining is likely more effective". With an
inference-to-pretraining token ratio of [0.16](numbers.md#comp-snell-r-low) test-time compute wins;
at [22](numbers.md#comp-snell-r-high) pretraining often wins; the two are "not 1-to-1 exchangeable".
Tree search let Llemma-7B beat Llemma-34B on MATH under every strategy tested (abstract)
[@wu2024inferencescaling]. Inference buys capabilities the base model nearly has. It does not buy
ones it lacks, which is where D1 lives.

*The verifier decides whether inference keeps paying.* On SWE-bench Lite, where unit tests check
answers, solved problems rose from [15.9%](numbers.md#comp-monkeys-pass1) with one sample to
[56%](numbers.md#comp-monkeys-pass250) with [250 samples](numbers.md#comp-monkeys-samples), a gain of
[40.1 pp](numbers.md#comp-monkeys-gain), above the single-sample state of the art of
[43%](numbers.md#comp-monkeys-sota). Coverage keeps scaling over
[4 OOM](numbers.md#comp-monkeys-oom) of samples. Without an automatic verifier, majority voting and
reward models plateau after several hundred samples (abstract) [@brown2024monkeys].

*Reasoning models.* The vendor reports that o1 improves smoothly with both RL compute and thinking
time on log axes, scoring [74%](numbers.md#comp-o1-pass1) on AIME 2024 with one sample,
[83%](numbers.md#comp-o1-cons64) with consensus over [64 samples](numbers.md#comp-o1-cons-k), and
[93%](numbers.md#comp-o1-rerank) when re-ranking [1,000 samples](numbers.md#comp-o1-rerank-k)
[@openai2024o1]; o3 pushed about [1 OOM](numbers.md#comp-o3-extra-oom) further in both
[@openai2025o3]. These are vendor claims on axes without absolute units. Reading those charts, Ord
estimates that [100](numbers.md#comp-ord-rl-inf)x of inference did what
[10,000](numbers.md#comp-ord-rl-train)x of RL training would: one OOM of inference worth
[2 OOM](numbers.md#comp-ord-rl-per-inf) of RL, by his own description an educated guess
[@ord2025rlscale]. DeepSeek-R1-Zero's AIME score rose from [15.6%](numbers.md#comp-r1zero-start) to
[71.0%](numbers.md#comp-r1zero-end) under pure RL, a gain of [55.4 pp](numbers.md#comp-r1zero-gain)
[@deepseek2025r1], so RL with verifiable rewards scales. Whether it adds anything beyond the base
model is contested. Yue et al. find base models reach higher pass@k at large k and conclude that
RL's abilities "originate from and are bounded by the base model" [@yue2025rlvr]. Prolonged RL is
reported to beat base models at every k tested, including where the base fails (abstract)
[@liu2025prorl]. RL curves fitted over [400,000 GPU-hours](numbers.md#comp-scalerl-gpu-hours) are
sigmoidal: most design choices change efficiency without moving the asymptote (abstract)
[@khatri2025scalerl]. Test-time RL, which AlphaProof used to learn from millions of problem variants
generated at inference time [@hubert2026alphaproof], blurs the boundary between training and
inference altogether.

*Distillation.* A 32B model distilled from DeepSeek-R1 scores [72.6%](numbers.md#comp-r1-distill-32b)
on AIME 2024; large-scale RL on the same 32B base reaches [47.0%](numbers.md#comp-r1-rl-32b), a gap
of [25.6 pp](numbers.md#comp-r1-distill-gap) [@deepseek2025r1]. Even the 7B distilled model reaches
[55.5%](numbers.md#comp-r1-distill-7b). Distillation scaling laws say why: with an existing teacher,
distillation beats supervised learning up to a compute level that grows with student size, while if
the teacher must also be trained, supervised learning is generally better (abstract)
[@busbridge2025distillation]. Yue et al. add that distillation, unlike RL, can bring in reasoning
patterns the student did not have [@yue2025rlvr]. An existing uncapped teacher is exactly the case
where distillation pays. Nor does the teacher cap the student. Students distilled with their
teacher's architecture, "these Born-Again Networks (BANs), outperform their teachers significantly"
(abstract) [@furlanello2018born], and strong models fine-tuned on a weaker supervisor's labels
"consistently perform better than their weak supervisors" (abstract) [@burns2023weak]. A party with
its own base model and a teacher's outputs can end above the teacher.

*Post-training enhancement.* Most surveyed enhancements (tool use, prompting, scaffolding, solution
selection, data generation) are worth more than [5](numbers.md#comp-davidson-ceg-typ)x training
compute, some more than [20](numbers.md#comp-davidson-ceg-high)x, for fine-tuning that typically
costs under [1%](numbers.md#comp-davidson-finetune-share) of the original training (abstract)
[@davidson2023enhancements].

*The steelman against a large leak.* Inference substitution is bounded per technique, costs more
inference than the training it replaces at every measured rate above, and fails on hard problems,
which are the ones that matter for superintelligence. Heim and Koessler expect "a limit to the
increase in model capabilities that can be gained from post-training enhancements" and suggest a
safety buffer of about [1 OOM](numbers.md#comp-heim-buffer-oom) [@heim2024thresholds]. And the
inference spent is compute that a chip count can see, which training-era algorithmic gains are not.

*The steelman for a large leak.* Ord's report summarises trade-off work as "increasing inference
compute on the task at hand by a factor of [10](numbers.md#comp-ord-inf-step) can improve
performance as much as increasing pre-training compute by
[3](numbers.md#comp-ord-pretrain-lo)-[10](numbers.md#comp-ord-pretrain-hi)x", that is
[1.0 OOM](numbers.md#comp-ord-inf-per-train-lo) to [2.1 OOM](numbers.md#comp-ord-inf-per-train-hi)
of inference per OOM of pre-training, with gains often plateauing after a few OOM. His illustration:
a model trained with [1e+24 FLOP](numbers.md#comp-ord-example-base) might use
[10,000](numbers.md#comp-ord-example-inf) times more inference to perform like one trained with
[1e+27 FLOP](numbers.md#comp-ord-example-target) [@ord2025govaireport], replacing
[3 OOM](numbers.md#comp-ord-example-oom) of training at
[1.33 OOM](numbers.md#comp-ord-example-exchange) of inference each. No source measured whether
techniques stack. Where a cheap verifier exists (code, formal mathematics), the span is the largest
measured.

### What the survey changed from the memo

The memo listed A2 as a mechanism to measure "on small models and from published curves". Both the
measurement and the governance consequence are prior work: the exchange rate on Hex
[@jones2021boardgames], per-technique spans and the warning that augmented inference lets actors
reach higher capability at smaller scale [@villalobos2023tradeoff], the difficulty dependence
[@snell2024testtime], and the statement that inference scaling would "derail the current paradigm of
AI governance via training compute thresholds" (abstract) [@ord2025inferencegov], made quantitative
in Ord's technical report (written at the Oxford Martin AI Governance Initiative and hosted by
GovAI) [@ord2025govaireport]. Heim and
Koessler and Hooker made the threshold point earlier [@heim2024thresholds; @hooker2024thresholds]. The
memo missed two things: distillation, which is a cheaper leak than inference or RL, and the role of
the verifier, which decides how big the span is. Both are already in prior accounting of the leak:
fine-tuning, extra inference and distillation are added up against a training threshold in
[@pistillo2025loopholes], and the span set by cheap verification is Villalobos and Atkinson's
[@villalobos2023tradeoff].

### What it means for the protocol

Candidates, not findings. (1) Meter compute held, not only training compute per run: the chips that
run inference are the same chips that train, and the inference leak is paid in compute a chip count
sees. (2) Count RL rollout compute as training compute, wherever it runs, since it is the training
signal; this is the gap that distributed RL already exploits. (3) Treat outputs of models near the
line, above a capability threshold set some way below it, as a controlled input to training: bulk
generation of training data from such a model goes through the same gate as compute. The EU already
counts a downstream modification above [33%](numbers.md#comp-eu-modifier-share) of the original
model's training compute as making the modifier a provider [@ec-gpai-guidelines-faq-2025];
distillation needs an analogous rule keyed to the teacher, not the student's compute. (4) Give
domains with a cheap verifier more headroom below the line, because the span there is largest. The
cost to useful AI: (1) and (2) cost little, since they only count; (3) costs something real, because
training small models on large models' outputs is a large part of how useful AI is made cheap, so
the gate has to sit high, keyed to the teacher's capability, and not at all distillation. Since a
student can exceed its teacher, it must sit below the line by the uplift E10's distillation arm is to
measure, not at the line.

### What would test it

E10, the training-to-inference exchange rate, as a runnable test on open models under `gpu`; it has
not run. Take
one open model family with published training compute at four or more sizes. On a code task family
with unit tests (a cheap verifier) and a free-form maths family scored by majority vote (no
verifier), measure accuracy against samples per task from one to a few thousand. Fit iso-accuracy
contours in (log training FLOP, log inference FLOP per task). Report the exchange rate, the span, and
where the span ends, with and without the verifier, with bootstrap intervals. Add a distillation arm:
fine-tune the smallest model on the largest model's verified outputs at a fixed token budget and
convert its gain to compute-equivalent training on the family's own scaling curve, reporting where the
student ends against the teacher, since an uplift above the teacher is the term breakout time needs
(C2). The memo's worry
holds if the verifier arm's span exceeds the [1 OOM](numbers.md#comp-heim-buffer-oom) buffer by a
wide margin; it fails if the spans match Villalobos and Atkinson's per-technique bound.

## A3. Algorithmic progress

### Definition

Algorithmic progress g(F, t) is the factor by which the physical compute needed to reach a fixed
capability falls in a year, measured at a stated training-compute scale F and against a stated
reference algorithm. Units: a multiplier a year, or the halving time. It is split by source:
pretraining architecture and optimisation, data quality and mixture, and post-training. The scale
argument is kept because one number for all scales, the memo's assumption, may be wrong: ablations
reproduce only a small part of the claimed gain at low compute [@gundlach2025origin]. But the
evidence below identifies neither one multiplier nor a scale-dependent rate on public data (E1), so
the definition leaves the dependence on scale to be measured (E15), not assumed either way.

### How it is measured

Four methods. Fixed-target efficiency: how much less compute reaches a fixed result years later
[@hernandez2020efficiency]. Regression across many published models with compute and date terms
[@ho2024algorithmic]. Ablation: swap innovations in and out at controlled scale
[@gundlach2025origin]. Fixed-hardware records: the NanoGPT speedrun [@moddednanogpt]. The errors
are large. The published intervals are wide; selection bias in which compute developers choose
could move observational estimates by a large factor either way [@whitfill2025selection]; and
efficiency is "strongly reference-dependent" (abstract) [@gundlach2025origin]. Most of the field's
progress is published, so outsiders can measure it. A party can keep its own innovations secret,
and Mertens et al.'s within-firm spread of more than
[40](numbers.md#comp-mertens-firm-spread)x shows that private techniques matter away from the
frontier [@mertens2026secretsauce]. What a party cannot hide from a capability evaluation is the
result.

### Evidence for and against

*The headline rates.* For language models from 2012 to 2023, the compute needed for a fixed
performance halved every [8.4 months](numbers.md#comp-ho-halving) (95% CI
[4.5 months](numbers.md#comp-ho-halving-lo) to [14.3 months](numbers.md#comp-ho-halving-hi)), over
more than [200 evaluations](numbers.md#comp-ho-evals) [@ho2024algorithmic]. That is
[2.7](numbers.md#comp-ho-annual)x a year (from [1.8](numbers.md#comp-ho-annual-lo)x to
[6.3](numbers.md#comp-ho-annual-hi)x). The Transformer alone is worth
[7.2](numbers.md#comp-ho-transformer)x (CI [3.3](numbers.md#comp-ho-transformer-lo)x to
[45.7](numbers.md#comp-ho-transformer-hi)x), and Ho et al. note that "some algorithmic innovations
will become obsolete over time as models are trained at larger scales". Computer vision halved every
[9 months](numbers.md#comp-erdil-halving), about [2.5](numbers.md#comp-erdil-annual)x a year
(abstract) [@erdil2022vision]. The first fixed-target measurement found
[44](numbers.md#comp-hernandez-gain)x less compute to reach AlexNet-level ImageNet over
[7 years](numbers.md#comp-hernandez-years), about [1.7](numbers.md#comp-hernandez-annual)x a year
(abstract) [@hernandez2020efficiency]. Newer estimates are faster: the Rosetta fit implies
[6](numbers.md#comp-rosetta-algo)x a year (from [1](numbers.md#comp-rosetta-algo-lo)x to
[50](numbers.md#comp-rosetta-algo-hi)x across families) and
[9](numbers.md#comp-rosetta-algo-frontier)x at the frontier of algorithmic quality [@ho2025rosetta].
Inference efficiency in open models, with hardware price declines divided out, improves about
[3](numbers.md#comp-inference-algo)x a year, while prices at fixed benchmark level fall
[5](numbers.md#comp-price-fall-lo)x to [10](numbers.md#comp-price-fall-hi)x a year and the price of
running frontier models rises [3](numbers.md#comp-frontier-price-rise-lo)x to
[18](numbers.md#comp-frontier-price-rise-hi)x a year (abstract) [@gundlach2025priceprogress].
Capability at a fixed level gets cheap fast; the frontier spends more on inference. Capacity per
parameter doubles about every [3 months](numbers.md#comp-xiao-doubling), a per-parameter measure not
comparable with compute halving (abstract) [@xiao2024densing].

*Scale dependence: the result that cuts against the memo.* Ho et al.'s estimate implies a factor of
[22,000](numbers.md#comp-gundlach-claimed) from 2012 to 2023. Gundlach et al.'s small-scale ablations
account for less than [10](numbers.md#comp-gundlach-ablation-max)x of it, and their survey of the
other innovations adds less than [10](numbers.md#comp-gundlach-other-max)x more, so under
[100](numbers.md#comp-gundlach-small-max)x in total in low-compute regimes. (Only the first factor
comes from their ablations; the second is their estimate.) The gap is explained by "algorithms with
scale-dependent efficiency improvements": the LSTM-to-Transformer switch and the Chinchilla
rebalancing change the scaling exponent, while most other innovations show "little scaling
difference" (abstract) [@gundlach2025origin]. In yearly terms, the claimed total is
[2.5](numbers.md#comp-gundlach-claimed-annual)x a year, while the small-compute total is at most
[1.52](numbers.md#comp-gundlach-small-annual-max)x a year. Of the claimed
[4.3 OOM](numbers.md#comp-gundlach-claimed-oom), at most
[46%](numbers.md#comp-gundlach-small-oom-share) is accounted for at small compute.

*What E1 found on scale.* E1 ran this chapter's test (a) below and did not find the predicted rise.
Rerunning Ho et al.'s code and data [@ho2024algorithmiccode] reproduced their rate (their own
bootstrap, rerun, gives [1.008](numbers.md#e1-ho-refit-over-published) times the published halving
time), but split into compute terciles, the highest progressed faster than the lowest in only
[52%](numbers.md#e1-ho-top-faster-share) of resamples. On Epoch's index drift fell with scale,
[-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom) (from
[-0.64 OOM a year per OOM](numbers.md#e1-drift-per-oom-lo) to
[-0.16 OOM a year per OOM](numbers.md#e1-drift-per-oom-hi)), the opposite of what scale dependence
predicts, but the sign is not robust across samples, and across six samples of the same models the
rate itself ran from [2.6](numbers.md#e1-algo-annual-subset-min)x to
[1,512](numbers.md#e1-algo-annual-subset-max)x a year. On public data neither one multiplier nor a
scale-dependent rate is identified.

*Selection bias.* If developers choose compute in response to algorithmic quality, the estimates are
contaminated. In Whitfill's simulation with true progress of
[45%](numbers.md#comp-whitfill-true) a year, a correlation of +[0.5](numbers.md#comp-whitfill-corr)
gives an estimate of [16.5%](numbers.md#comp-whitfill-pos) and -[0.5](numbers.md#comp-whitfill-corr)
gives [93%](numbers.md#comp-whitfill-neg). A first-pass
calibration suggests observational estimates overstate progress by about
[9](numbers.md#comp-whitfill-factor)x, with many other explanations possible
[@whitfill2025selection]. The direction is not settled; the width is.

*The fixed-hardware record.* The NanoGPT speedrun trains a small model to a fixed validation loss on
fixed hardware with a fixed data pipeline [@moddednanogpt]. The record fell from
[2,700 s](numbers.md#comp-speedrun-base-s) to [39.9 s](numbers.md#comp-speedrun-record-s)
[@epoch2026speedrundata] in [2.26 years](numbers.md#comp-speedrun-years), a factor of
[67.7](numbers.md#comp-speedrun-ratio), or [6.5](numbers.md#comp-speedrun-annual)x a year on average
(halving every [4.5 months](numbers.md#comp-speedrun-halving)). Tokens to the target fell from
[1e+10 tokens](numbers.md#comp-speedrun-tokens-base) to under
[3.3e+08 tokens](numbers.md#comp-speedrun-tokens-record), at least
[30](numbers.md#comp-speedrun-token-ratio)x, or [4.5](numbers.md#comp-speedrun-token-annual)x a
year. Those are fast small-scale gains, which seems to contradict the scale-dependence result. It
does not clearly do so. Wall-clock mixes systems engineering (FP8 matrix multiplies, kernel fusion,
compiler upgrades) with algorithms; the parameter count is not fixed, since a hashed n-gram table
now holds [65,000,000,000 parameters](numbers.md#comp-speedrun-ngram-params); and external analyses
cited by METR put the FLOP-efficiency gain at about [1.6](numbers.md#comp-metr-flop-eff-lo)x to
[1.7](numbers.md#comp-metr-flop-eff-hi)x a year [@shetty2026metrnanogpt], close to Gundlach et al.'s
small-compute bound. The pace is also uneven: about [15](numbers.md#comp-speedrun-first8mo)x in the
first [8 months](numbers.md#comp-speedrun-first-months), about [1.6](numbers.md#comp-speedrun-2025)x
across 2025 (both computed in the survey from Epoch's series, to be recomputed from the record
logs). The same
record gives three different rates depending on the metric, which is the reference-dependence
problem in miniature.

*Sources of progress.* METR's analysis of [77 records](numbers.md#comp-metr-records) to March 2026
found a [31](numbers.md#comp-metr-speedup)x speedup, roughly [21](numbers.md#comp-metr-shallow)x of it
from shallow and moderate contributions, leaving about [1.5](numbers.md#comp-metr-deep)x for deep
ones. By provenance, imported ideas gave [6.7](numbers.md#comp-metr-imported)x, adapted ones
[3.0](numbers.md#comp-metr-adapted)x, invented ones [1.6](numbers.md#comp-metr-invented)x.
[4 records](numbers.md#comp-metr-ai-records) credit an AI agent working with a human, all shallow to
moderate [@shetty2026metrnanogpt]. Reasoning models with strong scaffolds struggle even to
reimplement known speedrun innovations (abstract) [@zhao2025speedrun]. AI's measured contribution to
algorithmic research is still small; the dynamics chapter takes this up.

*Does research survive a cap?* Barnett catalogues
[36 innovations](numbers.md#comp-barnett-innovations) used in Llama 3 and DeepSeek-V3 and finds that
caps at GPT-2's training compute or at [8 H100s](numbers.md#comp-barnett-cap-gpus) could still have
allowed [50%](numbers.md#comp-barnett-feasible) of them; "compute caps alone are unlikely to
dramatically slow AI algorithmic progress" (abstract) [@barnett2025innovation]. This is the
strongest evidence for the memo's ranking of self-improvement first. Read with Gundlach et al., it
has a limit: the innovations that pay most are the ones whose value shows only at scale, so finding
them under a cap may be possible while knowing they matter is not. Whether research compute and
labour substitute is unresolved: one specification puts the elasticity of substitution at
[2.58](numbers.md#comp-ww-sigma-compute) (substitutes), the frontier-experiments specification at
[-0.10](numbers.md#comp-ww-sigma-frontier) (complements), from a panel of only
[4 firms](numbers.md#comp-ww-firms) [@whitfill2025bottlenecks]. Returns to research in language
models are estimated at [1.9](numbers.md#comp-r-lm), above the runaway threshold of 1, but a
compute-bottleneck correction cuts every such estimate by about [3](numbers.md#comp-r-compute-cut)x,
which puts them all below 1 [@ho2025experiments]. E9 reproduced the language-model estimate,
[1.90](numbers.md#e9-lm-r-repro), and found that the correction leaves compute's own growth out.
Counting it, the language-model loop gain at fixed compute, at the correction's compute share of
[0.67](numbers.md#dyn-research-compute-share), is [0.25](numbers.md#e9-lm-k-fixed)
([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile), and it is above 1 for compute shares
below about [0.26](numbers.md#e9-lm-share-crit), which no data excludes: no data identifies compute's
share of research input.

*The steelman for the memo.* Algorithms have been roughly as important as compute in vision
[@erdil2022vision]. The newest estimates run faster than the old ones [@ho2025rosetta]. Barnett's
result says research largely survives a cap. And innovations that change exponents, which matter
most near and above a cap, are precisely what a party trying to break out would look for.

### What the survey changed from the memo

The memo's D3 multiplies physical compute by one efficiency term whose growth is measured. That does
not hold: measured efficiency depends on the reference algorithm and, in ablations, on scale
[@gundlach2025origin], and its central value is uncertain by more than the published intervals
[@whitfill2025selection]. If the ablations are right, the leak rate of a cap depends on where the cap
sits: a cap far below the frontier leaks more slowly than the headline rate, while
exponent-changing innovations matter most near the cap. E1 did not confirm the scale dependence in
Ho et al.'s data or on Epoch's index, and could not identify the rate at all, so neither the memo's
one efficiency term nor a scale-dependent one is settled. The memo listed "algorithmic progress at fixed compute" as a failure mode, which is
right, but it is prior work as a failure mode: Pilz et al. separate the access effect, more actors
reaching a given performance, from the performance effect [@pilz2023efficiency]; Heim and Koessler
call moving thresholds down "a regulatory dilemma" [@heim2024thresholds]; the MIRI draft agreement
prohibits training above [1e+24 FLOP](numbers.md#comp-scher-strict) and monitors it above
[1e+22 FLOP](numbers.md#comp-scher-monitored), cites a fall of [3](numbers.md#comp-scher-algo)x a
year in compute per capability, and notes the monitored cluster size would have to fall as fast,
without setting a schedule for its training thresholds [@scher2025agreement]; Barnett quotes a range
of [3](numbers.md#comp-algo-range-lo)x to [60](numbers.md#comp-algo-range-hi)x a year with no
calculation of when a cap fails [@barnett2026closingwindow]. No single halving time should be
treated as settled.

### What it means for the protocol

Candidates. Thresholds must fall over time, and the schedule should be set by the rate at the cap's
own scale, not by the headline. E1 shows that rate cannot yet be measured on public data at any
scale, so no schedule can be tabulated in advance with an interval; the times below are
illustrations at published rates. One OOM of leak takes
[2.3 years](numbers.md#comp-years-per-oom-ho) at Ho et al.'s central rate,
[2.1 years](numbers.md#comp-years-per-oom-scher) at the treaty's assumed rate,
[1.3 years](numbers.md#comp-years-per-oom-rosetta) at the Rosetta rate, and at least
[5.5 years](numbers.md#comp-years-per-oom-small) at the small-compute bound. For comparison, frontier
training compute grows one OOM every [1.4 years](numbers.md#comp-years-per-oom-frontier). A blanket
ban on algorithmic research would put the protocol where the Biological Weapons Convention sits:
dual-use know-how without a countable material, where the United States judged in 2001 that
inspections "would still not provide useful, accurate, or complete information" [@mahley-2001]. It
would also cost useful AI heavily, since efficiency is what makes useful AI cheap. A narrower
candidate, consistent with the MIRI draft's restricted-research article [@scher2025agreement], is to
restrict only research that changes scaling exponents at frontier scale. On Gundlach et al.'s
evidence the value of such research shows mainly at large scale, so confirming it would take compute
the gate already sees. Whether that holds is an empirical question for the test below.

### What would test it

E1, E15 and E4. (a) Rerun Ho et al.'s fit with their released code and data
[@ho2024algorithmiccode], then split the models into compute bins and fit the algorithmic rate
separately in each. Scale dependence predicts a rate that rises with compute; a flat rate refutes it.
E1 has run (a): the terciles show no robust rise, as the evidence above reports. (b) Ablate three
innovations (an architecture change, an optimiser, a data-mixture change) at three training scales on
one open codebase, and fit compute-equivalent gain against scale; this is E15, not run. (c) For the
speedrun, read the per-record logs for tokens, steps and model shape, compute FLOP per record, and fit
FLOP efficiency separately from wall-clock; E4's history used wall-clock as a stand-in, since FLOP
per record would need a parser per era. E9 asked whether the returns to this research are above or
below 1 once compute is counted, and found the answer turns on compute's share of research input,
which no data identifies (the evidence above). The memo's single multiplier survives only if (a) and
(b) find no scale trend. (a) found none, so (b) decides: if E15 finds no trend at fixed algorithms,
the scale term is cut.

## A4. Data

### Definition

Three quantities. The effective data stock D_s is the number of usable training tokens after quality
filtering. The data wall C_d is the compute-optimal training compute at which that stock, with the
repetition that costs almost nothing, is used up. With training compute C = k N D for N parameters
and D tokens, and D = r N at the compute-optimal ratio, C_d = k (e D_s)^2 / r for e epochs, where k
is [6 FLOP per parameter per token](numbers.md#comp-flop-per-param-token) [@kaplan2020scaling] and r
is [20 tokens per parameter](numbers.md#comp-chinchilla-tokens-per-param)
[@besiroglu2024replication]. The substitution condition says when generated data can replace human
data. It holds when a verifier can check a generated item more cheaply than the generator produced
it, so that filtered outputs carry information the model did not have; we call the difference in
capability between generating and verifying the generation-verification gap, following Song et al.
[@song2024gap].

### How it is measured

The stock is estimated from web indices and crawls with wide intervals [@villalobos2022data].
Repetition costs are measured by training at many epoch counts
[@muennighoff2023dataconstrained]. The gap is measured by comparing a model's generation accuracy with
its accuracy at judging its own outputs, across model sizes [@song2024gap]. Data is the input a
verification regime can see least: it copies at no cost, crosses borders invisibly, and can be
generated inside a facility. It is not a verification channel.

### Evidence for and against

*The stock.* The effective public text stock is about [4e+14 tokens](numbers.md#comp-data-stock),
used up at a median of [2028](numbers.md#comp-data-year) (range [2026](numbers.md#comp-data-year-lo)
to [2032](numbers.md#comp-data-year-hi)), at about [5e+28 FLOP](numbers.md#comp-data-wall-flop) of
compute-optimal training, or [6e+27 FLOP](numbers.md#comp-data-wall-flop-overtrained) if models are
overtrained [@villalobos2022data]. The formula above reproduces the source:
[4.8e+28 FLOP](numbers.md#comp-data-wall-check). Up to [4 epochs](numbers.md#comp-data-epochs-free)
of repetition yields negligible changes in loss, and the value of repetition decays with a fitted
constant of [15.4 repetitions](numbers.md#comp-data-rd-star); up to
[50%](numbers.md#comp-data-code-share) of the data can be code without downstream loss
[@muennighoff2023dataconstrained]. With those free epochs, the wall moves to about
[7.7e+29 FLOP](numbers.md#comp-data-wall-4ep). That is far above any proposed cap: the data wall sits
[4.7 OOM](numbers.md#comp-data-wall-over-scher-oom) above the MIRI draft agreement's strict threshold
of [1e+24 FLOP](numbers.md#comp-scher-strict) [@scher2025agreement], and
[3.7 OOM](numbers.md#comp-data-wall-over-eu-oom) above the EU AI Act's
[1e+25 FLOP](numbers.md#comp-eu-threshold) presumption [@eu-ai-act-2024], before counting repetition.

*Collapse.* Training indiscriminately on model output makes the tails of the distribution disappear.
For OPT-125m, perplexity rose from about [20](numbers.md#comp-collapse-ppl-start) to about
[28](numbers.md#comp-collapse-ppl-end) when no original data was kept, while keeping
[10%](numbers.md#comp-collapse-keep) of it limited the damage to minor degradation
[@shumailov2024collapse]. Accumulating synthetic data alongside real data, instead of replacing it,
avoids collapse, with a bounded test error in a linear model (abstract) [@gerstgrasser2024accumulate].

*Verified self-generated data.* With a verifier, generated data does more than avoid collapse.
AlphaGeometry trained on millions of synthesised theorems and proofs checked by a symbolic engine
[@trinh2024alphageometry]. Absolute Zero proposes its own tasks and learns from them with no external
data, using a code executor to validate tasks and check answers, and reports state-of-the-art results
against models trained on curated examples (abstract) [@zhao2025absolutezero]. The
generation-verification gap governs self-improvement, and a variant of it "scales monotonically with
the model pre-training flops" (abstract) [@song2024gap]. Where the verifier is a majority vote or a
learned reward model, gains plateau [@brown2024monkeys], and RL may only sharpen what the base model
already samples [@yue2025rlvr].

*The steelman for data as a lever.* Without data, nothing trains, and the best data (expert traces,
proprietary code, scientific measurements) is concentrated. That matters for the uncapped frontier
near [2028](numbers.md#comp-data-year). It does not matter for a party under a cap.

### What the survey changed from the memo

The memo's split, collapse without a verifier and self-improvement with one, is consistent with the
evidence and is prior work [@villalobos2022data; @muennighoff2023dataconstrained;
@shumailov2024collapse; @gerstgrasser2024accumulate; @zhao2025absolutezero]. The sharper statement
is: collapse needs real data to be replaced; growth beyond the base needs a verifier; and the size of
the verifier's advantage grows with pretraining compute [@song2024gap]. The last point couples A4 to
A1 and to the loop gain D2: a compute cap also caps how far a model can teach itself.

### What it means for the protocol

Candidate. Data is neither a lever nor a channel at any cap that has been proposed: the wall sits
several OOM above the caps, and data cannot be counted. The protocol should not try to limit data.
What it can watch is the verifier: in domains where answers are cheaply checkable (code, formal
mathematics, games), the data input to the next model closes without a human gate (D6), and the
headroom below the line should be larger there. Since the gap grows with pretraining compute, the
compute cap does part of this work. The cost to useful AI of not limiting data is nil.

### What would test it

A new experiment, the verifier substitution test (E16 in the claims file, not run), on small models.
Start
from a small open model and a task family with an exact checker (arithmetic or short programs with
tests). Run five generations of self-training in four arms: replace real data with unfiltered
outputs; accumulate unfiltered outputs with real data; replace with checker-filtered outputs;
accumulate checker-filtered outputs. Measure held-out accuracy and output diversity each generation,
and repeat at two or three model sizes to estimate how the gain from filtering scales with model
compute. The substitution condition holds if only the filtered arms improve beyond the base and their
advantage grows with size, as Song et al. predict; it fails if unfiltered accumulation does as well.

## A5. Search and planning

### Definition

Narrow superintelligence in a closed domain is performance above the best humans and the best prior
programs in a domain that has an exact, cheap verifier (game rules, a simulator, a code executor, a
proof checker), produced by search and self-play against that verifier. Transfer is the change in
performance on held-out, open-domain tasks per unit of gain in the closed domain, measured on the same
model before and after closed-domain training. Robustness is the worst-case performance against an
adversary searching for the system's failures, as opposed to the average against typical opponents.

### How it is measured

Closed-domain strength is measured by match results against the best humans and programs, or by
problems solved in competitions with fixed time limits. Transfer is measured as in Huan et al.: train
on mathematics only and evaluate on other domains [@huan2026mathtransfer]. Robustness is measured by
training adversarial policies [@wang2023adversarialgo]. Narrow superhuman systems can be cheap: the
Pluribus poker blueprint cost under [150 USD](numbers.md#comp-pluribus-cost) to train, by its
developer's account, and plays on commodity CPUs [@meta2019pluribus; @brown2019pluribus]. Such
systems are invisible to compute accounting, which is acceptable if they are harmless.

### Evidence for and against

*Closed loops run away inside closed domains, then saturate.* AlphaGo Zero, with no human data,
became "its own teacher" and won all [100 games](numbers.md#comp-alphagozero-games) against the
champion-defeating AlphaGo [@silver2017alphagozero]. AlphaZero, given only the rules, reached
superhuman play within [24 hours](numbers.md#comp-alphazero-hours) [@silver2018alphazero]. MuZero
dropped the need for a given simulator by learning a model of the quantities relevant to planning
(abstract) [@schrittwieser2020muzero]. In mathematics, AlphaGeometry solved
[25 problems](numbers.md#comp-alphageometry-solved) of
[30 problems](numbers.md#comp-alphageometry-total) recent olympiad geometry problems, against
[10 problems](numbers.md#comp-alphageometry-prev) for the previous best [@trinh2024alphageometry].
AlphaProof solved [3 problems](numbers.md#comp-alphaproof-solved) of the
[5 problems](numbers.md#comp-alphaproof-total) non-geometry problems at IMO 2024, with multi-day
computation and test-time RL [@hubert2026alphaproof]. Each loop ran fast while the verifier was
perfect and the domain closed.

*Narrow is not robust.* An adversarial policy beats KataGo at superhuman settings over
[97%](numbers.md#comp-katago-winrate) of the time; the attack transfers to other superhuman Go
programs, humans can execute it unaided, and it persists after adversarial training
[@wang2023adversarialgo]. Superhuman on average is not superior in the worst case, which is what D1's
battery must probe.

*Transfer is weak on average.* Across more than [20 models](numbers.md#comp-huan-models), most
models that succeed in mathematics fail to transfer their gains to other domains; with
mathematics-only data, RL-tuned models generalise well while supervised fine-tuning often erodes
general capability [@huan2026mathtransfer]. Self-play on zero-sum games improves reasoning by up to
[10%](numbers.md#comp-spiral-gain) across the benchmarks tested (abstract) [@liu2025spiral]. Transfer
exists, it is modest, and it depends on the method.

*The case against the memo's clean split.* AlphaEvolve, a general language model working against
automated evaluators, found narrow superhuman results (it improved on Strassen's algorithm for a
small complex-matrix case) and sped up the training of the model it runs on. By the developer's
account, it found a [23%](numbers.md#comp-alphaevolve-kernel) average kernel speedup for Gemini,
cutting overall training time by [1%](numbers.md#comp-alphaevolve-train), and a scheduling heuristic
that recovers [0.7%](numbers.md#comp-alphaevolve-fleet) of fleet-wide compute
[@novikov2025alphaevolve]. The effect is small. The structure is the one D2 worries about: a general
model, a search loop, an automated evaluator, and the target being the system's own training.

### What the survey changed from the memo

A5 is prior work throughout: self-play from AlphaGo Zero to AlphaProof, brittleness
[@wang2023adversarialgo], and transfer [@huan2026mathtransfer; @liu2025spiral]. What the survey did
not find is transfer measured as a quantity a protocol could set a threshold on. The memo's F3
("narrow superhuman systems are useful AI; the line is generality plus a closed loop") survives with
a qualification: narrow search inside a general system's own loop is not harmless by default
[@novikov2025alphaevolve].

### What it means for the protocol

Candidate. Leave narrow superhuman systems alone. They are useful (protein structure prediction is
the standard example [@jumper2021alphafold]), often cheap, and brittle; limiting them would cost much
and buy little. The concern is a search loop whose evaluator scores the efficiency of AI training
itself. Such loops consume visible compute (the search) and point at a nameable target (training
code, kernels, recipes), so a candidate rule is to register search loops above a compute level whose
evaluator measures AI training or inference efficiency, and to count their compute against the
party's holdings. This sits with D2's loop gain, measured in the dynamics chapter. The cost to useful
AI is low if the rule keys on the evaluator's target and not on search in general.

### What would test it

Two runnable tests on open models, neither run: (a) is E17 in the claims file, and (b) is merged into
E10, since it reuses E10's samples. (a) Transfer ratio: take an open base model and its released
mathematics-RL and mathematics-SFT variants, evaluate all three on held-out non-mathematics
benchmarks, and report the change in each per point of mathematics gain, with intervals; this
repeats Huan et al.'s design on models the experiment can name. (b) The generation-verification gap
against compute: across one open family at four or more sizes, measure accuracy at generating answers
and at verifying its own sampled answers on a code and a maths set, and fit the gap against
pretraining FLOP. If the gap grows with compute, as Song et al. report, a compute cap bounds the
self-improvement loop, and E4's staged loop-gain run should be repeated at two compute levels to see
whether g rises with scale.

## The combined leak of a training cap

The mechanisms above can be combined into one statement of how fast and how far a cap on training
compute leaks. Each of its terms is prior work, and joined they are a combination of prior work, C2
in the claims file, credited below. It is a model with placeholders, not a result.

### The model

A party is held to a training cap. Let H be the headroom: the distance, in OOM of effective compute,
between the cap and the compute that would reach the line. Where the line sits in compute is not
known; the ledger uses [3 OOM](numbers.md#comp-example-headroom-oom) for illustration only, the same
span as Ord's example [@ord2025govaireport]. The cap leaks through four routes, which differ in kind.

1. **Post-training enhancement, a one-off jump**, about [0.7 OOM](numbers.md#comp-oneoff-lo-oom) to
   [1.3 OOM](numbers.md#comp-oneoff-hi-oom) at under [1%](numbers.md#comp-davidson-finetune-share) of
   the training cost [@davidson2023enhancements]. It includes solution selection, so it is not added
   to an inference technique below.
2. **Inference, a jump bounded by the span and paid in visible compute**: about
   [1 OOM](numbers.md#comp-tradeoff-typical-oom) of training per technique without a cheap verifier,
   up to [3 OOM](numbers.md#comp-span-cheapver-train) with one, at
   [1.18 OOM](numbers.md#comp-hex-exchange-oom) to [2.0 OOM](numbers.md#comp-exchange-cheapver) of
   inference per OOM replaced [@jones2021boardgames; @villalobos2023tradeoff].
3. **Algorithmic progress, a continuous drift** at the rate g measured at the cap's own scale,
   bracketed by the small-compute bound of [1.52](numbers.md#comp-gundlach-small-annual-max)x a year
   and the headline rates of [2.7](numbers.md#comp-ho-annual)x to [6](numbers.md#comp-rosetta-algo)x
   [@gundlach2025origin; @ho2024algorithmic; @ho2025rosetta]. The small-compute bound is half
   measured: of its two factors, only the first comes from Gundlach et al.'s own ablations, and the
   second is their estimate from a survey of other innovations. E1 could not identify g on public
   data, at the cap's scale or any other, so the bracket is the published range, not a measured
   interval.
4. **Distillation, a transfer from the teacher's level**: a capped student approaches an existing
   teacher's capability at the student's own compute [@deepseek2025r1; @busbridge2025distillation],
   and can end above it [@furlanello2018born; @burns2023weak]. So it enters at the teacher's level
   plus an uplift term, which E10 is to measure. It has no compute-equivalent figure in the survey,
   so the model does not give it one. Repeated rounds of amplification and distillation are a loop,
   which Ord names as one path to recursive self-improvement (abstract) [@ord2025inferencegov], and
   whose fuel is inference compute.

The leak time is the time until the capped party closes H after the one-off jumps. In the claims
file's form
([C2](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)),
t = max(0, (H - J - S_v) / log10(g)), where J is the post-training jump in OOM (route 1), S_v the
inference span in OOM (route 2), larger where a cheap verifier exists and paid in compute a chip
count sees, and g the yearly efficiency gain at the cap's scale (route 3); C2 writes the headroom h
and the gain gamma. The max sets the time to zero once the jumps alone cover the headroom. The
figures below take one jump at a time, since route 1 already includes solution selection: S_v = 0
with the post-training jump, or J = 0 with a cheap verifier's span. The headroom a cap needs to
outlast the regime's response time T_r is J + S_v + T_r log10(g). With D4 this becomes the condition
on the cap: the leak time must exceed m T_r.

### What the numbers say

With the example headroom and the high post-training jump, a capped party closes the gap in
[4.0 years](numbers.md#comp-leak-years-ho) at Ho et al.'s central rate,
[2.2 years](numbers.md#comp-leak-years-rosetta) at the Rosetta rate, and no sooner than
[9.3 years](numbers.md#comp-leak-years-small) at the small-compute bound. In a domain with a cheap
verifier, repeated sampling alone could cover the whole example headroom at once, leaving
[0 OOM](numbers.md#comp-leak-left-verifier), at the price of up to
[6 OOM](numbers.md#comp-span-cheapver-inf) more inference per task. These times assume that no
inference technique stacks on top of the post-training jump. If one more OOM did stack, each time
would shorten by the time one OOM of drift takes at that rate (A3). They are illustrations at
published rates. E1 found the drift rate not identified, so none of them can be tabulated in advance
with an interval; the claims file cuts that use, C2(a), for this reason.

Against the placeholder response time of [1 yr](numbers.md#comp-response-years) alone, with no
margin and the high post-training jump, a cap needs about
[1.5 OOM](numbers.md#comp-headroom-needed-small) of headroom at the small-compute rate,
[1.7 OOM](numbers.md#comp-headroom-needed-ho) at Ho et al.'s rate and
[2.1 OOM](numbers.md#comp-headroom-needed-rosetta) at the Rosetta rate, and about
[3.4 OOM](numbers.md#comp-headroom-needed-verifier) where a cheap verifier exists. The protocol's
line is longer: Part II's declared-path line m T_r is [2.0 years](numbers.md#prot-line-declared),
its margin times its declared response time. Against it, with the jump from typical to high, E18 finds a cap
needs [1.1 OOM](numbers.md#e18-need-part1-lo) to [2.9 OOM](numbers.md#e18-need-part1-hi) across this
chapter's bracket, and up to [4.6 OOM](numbers.md#e18-need-verifier-part1-hi) with a cheap verifier
(under "What would test it"). For the line, E18's figures supersede the ones above. The
[1 OOM](numbers.md#comp-heim-buffer-oom) buffer suggested for post-training enhancement
[@heim2024thresholds] covers only the typical one-off jump.

### The split that matters: what the chip channel sees

The four routes divide by whether a count of chips and their use can see them.

- **Visible:** inference scaling and RL rollouts on registered chips. They are paid in compute, at
  more than one OOM of inference per OOM of training replaced, so a regime that meters compute held,
  not just training compute per run, charges them against the same budget. Their weak point is
  unregistered hardware: consumer GPUs reach deployed frontier capability within
  [6 months](numbers.md#comp-consumer-lag-lo) to [12 months](numbers.md#comp-consumer-lag-hi)
  [@somala2025consumergpu], and distributed RL already runs rollouts on them
  [@primeintellect2025intellect2].
- **Invisible:** algorithmic progress, post-training enhancement and distillation. Their compute is
  small or nil. They can only be met by lowering thresholds on a schedule (algorithmic progress), by
  headroom (post-training), by controlling access to teacher outputs (distillation), and by
  evaluating capability at declared checkpoints (all three). No detection channel watches them: in
  E5, which computes the chance each path is missed, distillation from others' outputs has no
  measured channel and is missed with certainty. Efficiency gains a party holds and has not declared
  are unsized, since no source measures them, so the line on the declared path rests on the compute
  a chip count sees, not on the drift term.

This split is what Part II needs from this chapter: it says which leaks the compute backbone absorbs
and which need other channels.

### Prior work, credited

The framing is prior work. Inference substituting for training [@villalobos2023tradeoff;
@ord2025inferencegov; @ord2025govaireport]; thresholds needing to fall, and a post-training buffer
[@heim2024thresholds; @hooker2024thresholds]; the access and performance effects of efficiency
[@pilz2023efficiency]; post-training worth [5](numbers.md#comp-davidson-ceg-typ)x to
[20](numbers.md#comp-davidson-ceg-high)x [@davidson2023enhancements]; research that survives a cap
[@barnett2025innovation]; a range of yearly rates with no failure calculation
[@barnett2026closingwindow]; and a treaty with a fixed cap and a cited yearly rate
[@scher2025agreement]. So are the terms of the model. Fleet accounting from holdings, with research
overhead, utilisation, an inference multiple and an uncertainty allowance, is the hardwired-pause
group's [@fithian2026hardwired]; a breakout-type time with a feedback term that falls as compute grows
is Gan's [@gan2026clock]; additive accounting of fine-tuning, extra inference and distillation
against a training threshold is [@pistillo2025loopholes]; the span set by cheap verification is
[@villalobos2023tradeoff]; and scale dependence is [@gundlach2025origin].

A leak tied to a breakout horizon is also prior work. A Narrow Path sizes cluster limits so that an
illegal run on a licensed cluster would take [3.2 years](numbers.md#comp-narrowpath-breakout),
counting one cluster's speed at fixed algorithms [@miotti2025narrowpath]. The hardwired-pause working
paper derives fleet thresholds from a breakout horizon of [2 years](numbers.md#comp-hwp-horizon) and
computes that [57%](numbers.md#comp-hwp-eff) yearly efficiency gains over
[26 months](numbers.md#comp-hwp-months) would raise one state's overt breakout capacity from
[20%](numbers.md#comp-hwp-before) to [53%](numbers.md#comp-hwp-after) of the threshold
[@fithian2026hardwired]. Compounding [1.57](numbers.md#comp-hwp-multiplier)x a year over that period
gives [2.66](numbers.md#comp-hwp-check)x, which reproduces their [2.65](numbers.md#comp-hwp-ratio)x
rise. Its efficiency rate is a fixed scenario input, and its horizon is chosen, not measured.

This chapter first claimed four additions: the algorithmic rate as a function of the cap's scale,
the one-off jump and the verifier-conditioned span inside one expression, distillation as a ceiling
transfer, and the visible-invisible split. Verification took most of them. The independent prior-art
search (L1) found every term prior work and relabelled the whole a combination. The scale-dependent
rate is Gundlach et al.'s, and E1 did not find it; the verifier-conditioned span and the accounting
of distillation are rules others wrote; and the ceiling is false as a rule, since a student can
exceed its teacher (L4). What would have remained ours: one expression evaluated per path from
verified holdings, a measured rather than assumed loop-gain term (C4), and the split between leaks a
chip count sees and leaks it does not. It would have added something only if, for some holding class
the protocol cares about, it differed from a single-multiplier breakout time by more than either's
interval, or if, backtested, it predicted the open-closed lag. E18 found neither (below), so C2 is
downgraded to an accounting frame and claims nothing. Tabulating it in advance with an interval is
cut, since E1 cannot identify the drift rate. The combination was not
found in the searches, which is a claim about those searches, not about the literature. Label: a
combination of prior work.

### What would test it

E18, the cap leak, has run on this chapter's ranges, since E1 could not supply g at the cap's scale.
It computes the leak time over a grid of headrooms at the corners of each rate range, with J over the
post-training range and the inference span from one typical technique to the cheap-verifier span,
against the declared path's illustrative m T_r of [2.0 years](numbers.md#prot-line-declared). For the example cap with no cheap verifier, the leak
time runs from [2.2 years](numbers.md#e18-leak-part1-lo) to [12.7 years](numbers.md#e18-leak-part1-hi)
across this chapter's bracket, and from [0.53 years](numbers.md#e18-leak-subset-lo) to
[5.5 years](numbers.md#e18-leak-subset-hi) across E1's six sample rates. At
[4 samples](numbers.md#e18-subsets-inside-line) of those six rates the example cap fails the
illustrative line at every post-training jump, and at [1 samples](numbers.md#e18-subsets-outside-line)
it passes. The headroom a cap needs runs from [1.1 OOM](numbers.md#e18-need-part1-lo) to
[2.9 OOM](numbers.md#e18-need-part1-hi) on this chapter's bracket and up to
[7.7 OOM](numbers.md#e18-need-subset-hi) at the fastest sample rate, or
[3.3 OOM](numbers.md#e18-need-record-tr-part1-hi) at the bracket's high corner with T_r taken from
the record (E5's declared-path detection plus E24's median response, a median, not a high quantile).
The Monte Carlo medians move by a factor of [1.25](numbers.md#e18-mc-median-spread) across three
assumed laws for the rate inside the bracket, so they illustrate, not measure.

Three findings cut against the model.

1. **It separates from one multiplier only where the cap already fails the line (C2(b), not
   shown).** At fixed compute, with no cheap verifier, the expression's interval and a single
   multiplier's are disjoint only at headrooms below [0.91 OOM](numbers.md#e18-b-sep-part1) on this chapter's
   bracket, [0.80 OOM](numbers.md#e18-b-sep-subsets) on E1's samples, and
   [1.30 OOM](numbers.md#e18-b-sep-verifier-part1) or [1.15 OOM](numbers.md#e18-b-sep-verifier-subsets)
   with a cheap verifier. In all [8 cases](numbers.md#e18-b-sep-fails-line) of holding class and rate range, every headroom where
   they separate is one where the cap's leak time is already below m T_r at every input, and at the
   example headroom they overlap in all ([0 cases](numbers.md#e18-b-disjoint-example) disjoint). So
   the expression adds nothing at fixed compute that changes a verdict. This is arithmetic on the
   ranges, not a measurement.
2. **The leak comes in jumps, not at a constant rate (C2(c), against).** E18 set a cap at a then-frontier model's
   compute and at headrooms below it, and recorded when a model at or below the cap first matched the
   record. Each catch-up closing more headroom than any earlier one implies a yearly rate from
   [1.91](numbers.md#e18-bt-gamma-lo) to [1,125](numbers.md#e18-bt-gamma-hi), a range of observed
   events, not an interval. The largest headroom closed was
   [1.46 OOM](numbers.md#e18-bt-max-headroom), and the last catch-up closed most of it within days of
   the one before. Of the backtest's points, the
   first matches of [3 records](numbers.md#e18-bt-targets) at their own compute and the
   [4 catch-ups](numbers.md#e18-bt-events), only [3 points](numbers.md#e18-bt-inside-part1) fall inside the expression's interval on this chapter's bracket with J = 0,
   [2 points](numbers.md#e18-bt-inside-part1-j) with J over the post-training range, and
   [2 points](numbers.md#e18-bt-inside-subsets) on E1's samples.
3. **The expression has no follower-delay term.** At zero headroom it predicts a leak time of zero
   for every input, yet a model at or below a frontier record's compute matched it only after
   [0.48 years](numbers.md#e18-bt-h0-lo) to [1.52 years](numbers.md#e18-bt-h0-hi). Catching up takes
   time the expression does not model.

The open-closed lag, C2(c)'s stated target, cannot be predicted at all. E18 reproduces Epoch's strict lag
over its 2026 window at [7.0 months](numbers.md#e18-oc-lag-strict),
[1.17](numbers.md#e18-oc-lag-over-published) times the strict lag Epoch publishes, and the mean gap
at [8.2 ECI points](numbers.md#e18-oc-gap-eci); the headline lag is
[4 months](numbers.md#comp-open-closed-lag) [@edwards2026openclosed]. But on
[0 days](numbers.md#e18-oc-evaluable-days) of the window do both the best open model and the record it
matched have a public compute estimate, so the expression cannot predict the lag on public data.
With the backtest against it, C2(c) has failed. C2 would reopen only if E15 and E10's post-training,
distillation and verifier arms narrowed the ranges enough for the two intervals to separate where a
cap passes the line, and a version with a follower's delay backtested. The response time still has no measured bound: of
findings made while the party was in its treaty, [25%](numbers.md#e24-halt-share-never) were never
followed by a halt (E24), so the placeholder of [1 yr](numbers.md#comp-response-years) above stays a
placeholder. A model that cannot predict the open-closed lag should not set a treaty schedule.

## What this perspective contributes to the line

Four quantities from this chapter are candidates for the protocol to trigger on or limit.

1. **Compute held by a party, training and inference together, with RL rollouts counted as
   training.** Measured by chip accounting, power and attestation (the physical chapter and Part II).
   It absorbs the inference leak because inference is paid in compute, at more than one OOM per OOM of
   training replaced. Weakest point: unregistered consumer hardware, which runs deployed frontier
   capability within [12 months](numbers.md#comp-consumer-lag-hi) and already hosts distributed RL
   rollouts.

2. **The cap's leak rate at its own scale, in OOM a year, and its one-off leak, in OOM.** E1 has
   run and could not identify the rate on public data. E15, scale dependence at fixed algorithms,
   would measure the rate at the cap's scale, and E10 the one-off jump and the inference span;
   neither has run. Together they set how fast thresholds must fall and how much headroom a cap
   needs: against Part II's declared-path line m T_r of [2.0 years](numbers.md#prot-line-declared),
   E18 finds [1.1 OOM](numbers.md#e18-need-part1-lo) to [2.9 OOM](numbers.md#e18-need-part1-hi) (the
   one-off jump plus two years' drift) on this chapter's bracket of published rates, and up to
   [4.6 OOM](numbers.md#e18-need-verifier-part1-hi) where a cheap verifier exists. Weakest point: E1
   could not identify the rate on public data, which ran from
   [2.6](numbers.md#e1-algo-annual-subset-min)x to [1,512](numbers.md#e1-algo-annual-subset-max)x a
   year with the choice of models; the scale dependence is measured only in small-scale ablations,
   which E1 did not confirm; whether techniques stack is unmeasured; and E18 found the leak arrives
   in jumps, with catch-ups implying rates from [1.91](numbers.md#e18-bt-gamma-lo) to
   [1,125](numbers.md#e18-bt-gamma-hi) a year, after a follower delay no rate term models.

3. **Capability on a stitched scale at declared checkpoints, at intervals of about
   [4](numbers.md#comp-rsp-cadence)x effective compute.** Measured by refreshed batteries under a
   fixed elicitation budget (D5). It catches the invisible leaks (algorithms, post-training,
   distillation) by their result. Weakest point: forecast error of
   [18 pp](numbers.md#comp-task-mae-1oom) on a single task one OOM ahead, and in E1
   [17.0 pp](numbers.md#e1-oos-bench-mae-pp) per benchmark score with a bound that overshoots at the
   top; and capability hidden from the evaluator.

4. **Access to an uncapped teacher's outputs, and to cheap verifiers on AI research tasks.** Measured
   by output-access logs at model providers, and by the generation-verification gap as a function of
   compute (A5's test b). These are the inputs that close the data and labour loops without a human
   gate. Weakest point: outputs are information, and policing their use for training looks more like
   the Biological Weapons Convention than like nuclear safeguards.

The protocol should change in three ways because of this chapter. D3 cannot rest on one tabulated
efficiency multiplier, nor yet on a scale-dependent one: E1 finds the drift rate not identified, and
whether it depends on scale is open until E15, so the declared path's breakout time rests on the
compute a chip count sees. The compute limit should be on compute held, not training compute per
run. And distillation from licensed models needs a gate of its own, keyed to the teacher, set high
enough that it does not stop the cheap small models useful AI depends on, and below the line by the
uplift a student can gain over its teacher.
