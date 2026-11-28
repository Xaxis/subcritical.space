# The computational and algorithmic perspective

This perspective asks how compute becomes capability and how fast a fixed cap leaks, the
computational terms of breakout time. E1, E5 and E18 have run; E10, E15, E16 and E17 have not.

## A1. Capability as a function of effective compute

Capability is a score on one stitched scale of many benchmarks [@ho2025rosetta; @epoch2025eci] at
fixed elicitation (D5) and inference budgets; effective compute is training compute times an
efficiency against a reference algorithm. All prior work: scaling laws [@kaplan2020scaling;
@hoffmann2022chinchilla; @besiroglu2024replication], observational scaling [@ruan2024observational]
and predictability in aggregate, not per task [@owen2024predictable]; most emergence is a metric
artefact [@schaeffer2023mirage]. Compute explains most frontier differences [@mertens2026secretsauce],
less of growth [@ho2025rosetta]. In E1 [@epoch2026aimodels] its share runs from
[18%](../research/numbers.md#e1-compute-share-subset-min) to
[63%](../research/numbers.md#e1-compute-share-subset-max) across samples, unidentified on data lacking
compute for [23 models](../research/numbers.md#e1-top25-dropped) of the 25 most capable; one-OOM
forecasts miss by [0.96 OOM](../research/numbers.md#e1-oos-mae-oom), understated, under a wide bound,
not shown calibrated, that overshoots at the top. The line's capability axis is open.

## A2. The exchange rate between training and inference compute

The exchange rate is the OOM of inference replacing one OOM of training at fixed capability; the span
is where that holds. Both depend on technique and verifier cost, and both are prior work
[@jones2021boardgames; @villalobos2023tradeoff; @snell2024testtime], as is the leak of a training cap
through inference [@ord2025inferencegov; @ord2025govaireport]. A cheap verifier trades
[3 OOM](../research/numbers.md#comp-span-cheapver-train) of training for
[6 OOM](../research/numbers.md#comp-span-cheapver-inf) of inference, extrapolated with low confidence
[@villalobos2023tradeoff]; distillation beats RL on the same base [@deepseek2025r1]. Every measured
rate costs more inference than it saves, visible on registered chips but not on consumer GPUs running
distributed RL [@primeintellect2025intellect2]. Stacking is unmeasured.

## A3. Algorithmic progress

Algorithmic progress is the yearly fall in compute for a fixed capability, at a stated scale and
reference. Its rates are prior work and contested [@ho2024algorithmic; @erdil2022vision;
@hernandez2020efficiency; @ho2025rosetta; @gundlach2025priceprogress], as are scale and reference
dependence [@gundlach2025origin] and selection bias [@whitfill2025selection]. Published rates run
from [2.7](../research/numbers.md#comp-ho-annual)x to [6](../research/numbers.md#comp-rosetta-algo)x a
year, and at low compute at most [1.52](../research/numbers.md#comp-gundlach-small-annual-max)x,
partly by estimate. E1 identified neither one multiplier nor a scale-dependent rate: in Ho et al.'s
data [@ho2024algorithmiccode] the top tercile beat the bottom in only
[52%](../research/numbers.md#e1-ho-top-faster-share) of resamples, drift fell with scale on Epoch's
index by a sign not robust, and the rate ran from
[2.6](../research/numbers.md#e1-algo-annual-subset-min)x to
[1,512](../research/numbers.md#e1-algo-annual-subset-max)x across six samples.

## A4. Data

The data wall is the compute-optimal training compute that exhausts the filtered stock; generated
data substitutes where checking is cheaper than generating, the generation-verification gap
[@song2024gap]. All prior work: the stock [@villalobos2022data], repetition
[@muennighoff2023dataconstrained], collapse on replacement [@shumailov2024collapse], none on
accumulation [@gerstgrasser2024accumulate] and executor-checked self-play [@zhao2025absolutezero].
The wall sits [4.7 OOM](../research/numbers.md#comp-data-wall-over-scher-oom) above the MIRI draft's
strict threshold before repetition [@scher2025agreement], and data copies freely: neither lever nor
channel. The gap grows with pretraining compute [@song2024gap], so a compute cap limits
self-teaching.

## A5. Search and planning

Narrow superintelligence beats the best humans and programs where an exact, cheap verifier allows
search and self-play; transfer is open-domain gain per closed-domain gain, robustness the worst case
against an adversary. All prior work: self-play [@silver2017alphagozero; @silver2018alphazero;
@hubert2026alphaproof], brittleness [@wang2023adversarialgo] and weak transfer
[@huan2026mathtransfer; @liu2025spiral]. AlphaEvolve cut its own model's training time by
[1%](../research/numbers.md#comp-alphaevolve-train) [@novikov2025alphaevolve], small but with D2's
structure. Our search found no measure of transfer to threshold.

## The combined leak of a training cap

A capped party has headroom h, in OOM, to the agreed level C*. Post-training jumps J of
[0.7 OOM](../research/numbers.md#comp-oneoff-lo-oom) to
[1.3 OOM](../research/numbers.md#comp-oneoff-hi-oom) [@davidson2023enhancements]; inference adds a
span S_v, largest with a cheap verifier; algorithms drift at a yearly gain gamma; distillation enters
at the teacher's level plus an uplift, since a student can exceed its teacher [@furlanello2018born;
@burns2023weak]. The leak time, t = max(0, (h - J - S_v) / log10 gamma), is breakout time (D3) at
fixed compute, a combination of prior work: fleet accounting [@fithian2026hardwired], a breakout
clock [@gan2026clock], additive accounting of the routes [@pistillo2025loopholes], the verifier span
[@villalobos2023tradeoff] and scale dependence [@gundlach2025origin]. It assumes, without evidence,
that an OOM from any route equals one of training; if not, headroom and line go per route. It
inherits all the uncertainty of C*, a convention with no error bound: one OOM of C* moves it by
[2.3 years](../research/numbers.md#comp-years-per-oom-ho), more than the illustrative line of
[2.0 years](../research/numbers.md#prot-line-declared).

At [3 OOM](../research/numbers.md#comp-example-headroom-oom) of headroom without a cheap verifier, E18
puts the leak time at [2.2 years](../research/numbers.md#e18-leak-part1-lo) to
[12.7 years](../research/numbers.md#e18-leak-part1-hi) across published rates; an unidentified rate
allows no table in advance. The expression separates from one multiplier only where the cap is
already inside the line, in all [8 cases](../research/numbers.md#e18-b-sep-fails-line), by arithmetic
on the ranges. Its stated target, the open-closed lag of
[4 months](../research/numbers.md#comp-open-closed-lag) [@edwards2026openclosed], is untestable on
public data: [0 days](../research/numbers.md#e18-oc-evaluable-days) have compute for both models. A
substitute, catch-ups to records, bears against the constant rate: implied rates span
[1.91](../research/numbers.md#e18-bt-gamma-lo) to [1,125](../research/numbers.md#e18-bt-gamma-hi) a
year, observed events rather than an interval, and followers took
[0.48 years](../research/numbers.md#e18-bt-h0-lo) to [1.52 years](../research/numbers.md#e18-bt-h0-hi)
at zero headroom, a delay the expression lacks.

## What this perspective gives the line

Compute held, inference and RL rollouts included, is what a chip count meters, and it absorbs the
inference leak. Drift, post-training and distillation, invisible to it (E5 misses distillation
with certainty; undeclared efficiency is unsized), show only in capability at declared checkpoints,
or are gated at teacher outputs. With the rate unidentified and the leak in jumps, headroom is a design choice until E10 and E15 report.
