# The computational and algorithmic perspective

This perspective asks how compute turns into capability, and how much a limit on compute leaks. The
definitions draw the line by time: a holding is weapons-grade when its breakout time is short against
detection plus response. Algorithms decide how much capability a fixed amount of compute buys, and so
how fast a fixed cap leaks. Of the experiments named here only E1, E5 and E18 have run, and
nothing has been tested against an adversary.

## A1. Capability as a function of effective compute

**Definition.** Capability is a score on one stitched scale built from many benchmarks
[@ho2025rosetta; @epoch2025eci], under fixed elicitation (D5) and inference budgets. Effective compute
is training compute, pretraining and post-training, times an efficiency relative to a stated
reference algorithm. A1 is capability as a function of compute and date. Label:
prior work: scaling laws [@kaplan2020scaling; @hoffmann2022chinchilla; @besiroglu2024replication],
observational scaling [@ruan2024observational], predictability from compute [@owen2024predictable]
and a stitched scale with a compute slope [@ho2025rosetta]; most claimed emergence is a metric
artefact [@schaeffer2023mirage].

**Measurement.** The error that matters is forecast error: one OOM ahead, forecasts
of BIG-Bench Hard missed by [6 pp](../research/numbers.md#comp-bbh-mae-1oom) and of single tasks by
[18 pp](../research/numbers.md#comp-task-mae-1oom) [@owen2024predictable].

**Evidence for and against.** Compute explains
[80%](../research/numbers.md#comp-mertens-frontier-share-lo) to
[90%](../research/numbers.md#comp-mertens-frontier-share-hi) of differences at the frontier
[@mertens2026secretsauce], but only [45%](../research/numbers.md#comp-rosetta-compute-share) of growth
in broad capability [@ho2025rosetta]. In E1, which joins Epoch's model data to its capability index
[@epoch2026aimodels; @epoch2025eci], compute explains [36%](../research/numbers.md#e1-compute-share)
of growth, but [18%](../research/numbers.md#e1-compute-share-subset-min) to
[63%](../research/numbers.md#e1-compute-share-subset-max) across six samples: not identified. One-OOM
forecasts missed by [0.96 OOM](../research/numbers.md#e1-oos-mae-oom) of compute-equivalent on
average, understated since the slope was also fitted on the forecast models. The upper bound
was exceeded in only [1.1%](../research/numbers.md#e1-oos-unforecast-share) of forecasts: it is wide,
not shown calibrated, and it overshoots at the top.

**Open questions.** Which capability axis carries the line; whether public data, lacking compute for
[23 models](../research/numbers.md#e1-top25-dropped) of the 25 most capable, can identify the compute
share.

## A2. The exchange rate between training and inference compute

**Definition.** At a fixed task family and capability, the exchange rate is the OOM of inference per
task that replaces one OOM of training; the span is the range over which the trade holds. Both depend
on technique and on the cost of verifying an answer. Label: prior work: the rate on board games
[@jones2021boardgames], per technique with spans [@villalobos2023tradeoff] and by difficulty
[@snell2024testtime]; the leak of a training cap through inference is stated
[@villalobos2023tradeoff; @ord2025inferencegov; @ord2025govaireport].

**Measurement.** Iso-capability contours over training and inference budgets
[@jones2021boardgames]. A chip count sees inference on registered hardware, not on consumer GPUs,
where distributed RL runs rollouts [@primeintellect2025intellect2].

**Evidence for and against.** Repeated sampling with a cheap verifier trades
[3 OOM](../research/numbers.md#comp-span-cheapver-train) of training for
[6 OOM](../research/numbers.md#comp-span-cheapver-inf) of inference, extrapolated and with low
confidence [@villalobos2023tradeoff]. Distillation is cheapest: a 32B model distilled from
DeepSeek-R1 scores [72.6%](../research/numbers.md#comp-r1-distill-32b) on AIME 2024, against
[47.0%](../research/numbers.md#comp-r1-rl-32b) for RL on the same base [@deepseek2025r1]. Against a
large leak, every measured rate costs more inference than it saves in training.

**Open questions.** Whether techniques stack is unmeasured; E10 has not run.

## A3. Algorithmic progress

**Definition.** Algorithmic progress is the yearly factor by which the physical compute needed for a
fixed capability falls, at a stated scale and against a stated reference algorithm. Label: prior
work, and contested: the rates [@ho2024algorithmic; @erdil2022vision; @hernandez2020efficiency;
@ho2025rosetta; @gundlach2025priceprogress], their dependence on scale and reference
[@gundlach2025origin] and possible selection bias [@whitfill2025selection].

**Measurement.** Fixed targets [@hernandez2020efficiency], regression on compute and date
[@ho2024algorithmic], ablation [@gundlach2025origin] and fixed-hardware records [@moddednanogpt].

**Evidence for and against.** Compute for fixed performance fell
[2.7](../research/numbers.md#comp-ho-annual)x a year [@ho2024algorithmic]; the Rosetta fit implies
[6](../research/numbers.md#comp-rosetta-algo)x [@ho2025rosetta]. Less than
[100](../research/numbers.md#comp-gundlach-small-max)x of a claimed
[22,000](../research/numbers.md#comp-gundlach-claimed)x reproduces at low compute, at most
[1.52](../research/numbers.md#comp-gundlach-small-annual-max)x a year, partly by ablation and partly
by estimate [@gundlach2025origin]. E1 did not find the predicted rise with scale: in Ho et al.'s data
[@ho2024algorithmiccode] the top compute tercile beat the bottom in only [52%](../research/numbers.md#e1-ho-top-faster-share) of resamples. On Epoch's index drift fell
with scale, [-0.34 OOM a year per OOM](../research/numbers.md#e1-drift-per-oom), a sign not robust
across six samples, over which the rate ran from
[2.6](../research/numbers.md#e1-algo-annual-subset-min)x to
[1,512](../research/numbers.md#e1-algo-annual-subset-max)x a year. Neither one multiplier nor a
scale-dependent rate is identified.

**Open questions.** E15's ablations at three scales decide the scale term; with no trend, it is cut.

## A4. Data

**Definition.** The data stock is usable tokens after filtering; the data wall is the compute-optimal
training compute that uses it up. Generated data substitutes for human data when a verifier checks
an item more cheaply than it was generated: the generation-verification gap [@song2024gap]. Label:
prior work: the stock [@villalobos2022data], repetition [@muennighoff2023dataconstrained], collapse
when real data is replaced [@shumailov2024collapse] and none when it accumulates
[@gerstgrasser2024accumulate], and executor-checked self-play [@zhao2025absolutezero].

**Measurement.** Data copies freely and can be generated anywhere: it is no verification channel.

**Evidence for and against.** The wall sits at about
[5e+28 FLOP](../research/numbers.md#comp-data-wall-flop) [@villalobos2022data],
[4.7 OOM](../research/numbers.md#comp-data-wall-over-scher-oom) above the MIRI draft agreement's
strict threshold [@scher2025agreement] before any repetition: data is no lever at any proposed cap.
The generation-verification gap grows with pretraining compute [@song2024gap], so a compute cap also
limits self-teaching.

**Open questions.** E16 has not run.

## A5. Search and planning

**Definition.** Narrow superintelligence is performance above the best humans and programs in a
domain with an exact, cheap verifier, produced by search and self-play. Transfer is the open-domain
change per unit of closed-domain gain; robustness is worst-case performance against an adversary.
Label: prior work: self-play and search [@silver2017alphagozero; @silver2018alphazero;
@hubert2026alphaproof], brittleness [@wang2023adversarialgo] and weak, method-dependent transfer
[@huan2026mathtransfer; @liu2025spiral].

**Measurement.** Transfer by training on mathematics only [@huan2026mathtransfer]; robustness by
adversarial policies [@wang2023adversarialgo].

**Evidence for and against.** An adversarial policy beats superhuman KataGo over
[97%](../research/numbers.md#comp-katago-winrate) of the time [@wang2023adversarialgo]. AlphaEvolve,
a general model searching against automated evaluators, cut its own model's training time by
[1%](../research/numbers.md#comp-alphaevolve-train) [@novikov2025alphaevolve], a small effect with
the structure D2 measures.

**Open questions.** Our search found no measure of transfer a protocol could threshold; E17 has not
run.

## The combined leak of a training cap

**The model.** A capped party has headroom h, in OOM, to the agreed level C*.
Post-training adds a one-off jump J of [0.7 OOM](../research/numbers.md#comp-oneoff-lo-oom) to
[1.3 OOM](../research/numbers.md#comp-oneoff-hi-oom) [@davidson2023enhancements]; inference adds a
span S_v, largest with a cheap verifier (A2); algorithms drift at a yearly gain gamma. Distillation
enters at the teacher's level plus an uplift, since a student can exceed its teacher
[@furlanello2018born; @burns2023weak]. The leak time, t = max(0, (h - J - S_v) / log10 gamma), is
breakout time (D3) at fixed compute.

**What the numbers say.** E18 computed the leak time against the declared path's illustrative line of [2.0 years](../research/numbers.md#prot-line-declared). For an
illustrative headroom of [3 OOM](../research/numbers.md#comp-example-headroom-oom) and no cheap
verifier it runs from [2.2 years](../research/numbers.md#e18-leak-part1-lo) to
[12.7 years](../research/numbers.md#e18-leak-part1-hi) across the published rates; at
[4 samples](../research/numbers.md#e18-subsets-inside-line) of E1's six sample rates the cap fails the
line at every post-training jump. With the jump from typical to high, the headroom a cap needs runs
from [1.1 OOM](../research/numbers.md#e18-need-part1-lo) to [2.9 OOM](../research/numbers.md#e18-need-part1-hi), and up to
[4.6 OOM](../research/numbers.md#e18-need-verifier-part1-hi) with a cheap verifier.
Because E1 could not identify the drift rate, tabulating breakout time in advance with an interval is
cut.

**What E18 found against the model.** The expression separates from a single multiplier only at
headrooms where the cap already fails the line, in all
[8 cases](../research/numbers.md#e18-b-sep-fails-line) of holding class and rate range: arithmetic on
the ranges, so a gain over one multiplier is not shown. In the backtest the leak came in jumps that no
constant rate follows: catch-ups below a then-frontier record's compute imply yearly rates from
[1.91](../research/numbers.md#e18-bt-gamma-lo) to [1,125](../research/numbers.md#e18-bt-gamma-hi),
observed events, not an interval, and only [3 points](../research/numbers.md#e18-bt-inside-part1)
fall inside the expression's interval at the published rates. At zero headroom it predicts no delay, yet
followers matched a record only after [0.48 years](../research/numbers.md#e18-bt-h0-lo) to
[1.52 years](../research/numbers.md#e18-bt-h0-hi); the expression has no follower-delay term. The
open-closed lag of [4 months](../research/numbers.md#comp-open-closed-lag) [@edwards2026openclosed]
cannot be predicted: on [0 days](../research/numbers.md#e18-oc-evaluable-days) of the window do
both models compared have a public compute estimate.

**What the chip channel sees.** Inference and RL rollouts on registered chips are paid in compute, so
metering compute held charges them. Drift, post-training and distillation are invisible to it; in E5
distillation has no measured channel and is always missed. Undeclared efficiency is unsized.

**Prior work.** Label: a combination of prior work, downgraded to an accounting frame that claims
nothing. Fleet accounting from holdings [@fithian2026hardwired], a breakout clock [@gan2026clock],
additive accounting of fine-tuning, inference and distillation [@pistillo2025loopholes], the verifier
span [@villalobos2023tradeoff] and scale dependence [@gundlach2025origin] are prior. It reopens only
if E15 and E10 narrow the ranges enough for the two intervals to separate where a cap passes the
line, and a version with a follower's delay backtests.

## What this perspective gives the line

Compute held, inference included and RL rollouts counted as training, is what a chip count meters,
and it absorbs the inference leak. Algorithms, post-training and distillation are caught only by
their result, through elicited capability at declared checkpoints, and by gating teacher outputs.
With the drift rate unidentified and the leak arriving in jumps, headroom stays a design choice
until E10 and E15 report.
