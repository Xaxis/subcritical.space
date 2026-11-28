# Part I, 1: The physical and energetic perspective

Whatever else superintelligence is, it is a computation. It runs on chips that draw power, hold
their state in memory and move bytes between processors. Those are the only inputs to its formation
that are physical objects. They can be counted, weighed against datasheets and seen, at least in
part, from outside. So this is the perspective in which a verifier can know something without
taking a party's word for it, and it is where the protocol's compute half has to stand.

This chapter defines four physical quantities and asks, for each, what it measures, who can measure
it, how well, and whether a party could hide or fake it:

- **P1, the compute budget:** the operations it takes to train a system and to run copies of it at
  a speed.
- **P2, energy per useful operation:** how many joules each of those operations costs today, and how
  far physics and engineering let that fall.
- **P3, memory and bandwidth:** the state a system holds, the memory bandwidth that bounds how fast
  one copy can think, and the interconnect that once kept training on one site.
- **P4, the footprint and its floor:** the traces a run leaves (chips, energy, power, heat, water,
  buildings) and the smallest traces that could still produce it.

How this bears on the line. The memo's line between useful AI and the path to superintelligence is
a time, not a capability score: a holding is inside the line when its breakout time is shorter than
the regime's time to detect and respond (D4), and breakout time is computed from held compute and
algorithmic efficiency (D3). P1 is the holdings term in that calculation. P2 bounds how small the
physical trace of a fixed computation can become. P3 sets how fast one copy can run and whether
training must sit in one place. P4 is what each verification channel can actually see.

The survey changed this perspective substantially. Three findings lead. First, a per-site
footprint floor does not survive distributed training: a run can be split into nodes of a few tens
of kilowatts, far below anything a satellite, a grid operator or a thermal camera sees, so the only
floor that holds is an aggregate over chips and energy, and of the channels modelled here only chip
accounting sees it. Second,
the realistic efficiency headroom for today's kind of chip is about two orders of magnitude, not the
eight that a comparison with Landauer's bound suggests. Third, power is a rate limit in some countries, not a chokepoint: no small set of suppliers
controls it. The brain appears below only as a reference
point, never as a target.

Verification then corrected the floor itself. The floors this chapter first computed, at an assumed
utilisation and the BF16 peak, are estimates. The bound, at full utilisation and the FP8 peak, is
[5.0](numbers.md#formal-floor-ref-over-bound) times lower, so the untraced pool, at its assumed
size already far above the estimates, is further above the bound (P4). That is a calculation on an
assumed pool, not a measurement. The aggregate floor with a time axis, and the pool counted against it, are prior work
[@fithian2026hardwired].

Conventions. "FLOP" means dense 16-bit operations unless a sentence says otherwise. An
H100-equivalent (H100e) is the unit MIRI's draft agreement defines,
[990 TFLOP/s](numbers.md#phys-miri-h100e) at FP16 [@scher2025agreement]. Where a calculation needs a
utilisation it uses [40%](numbers.md#phys-util-ref), an assumption that sits inside the
[36.2%](numbers.md#phys-intellect1-mfu-low) to [41.4%](numbers.md#phys-intellect1-mfu-high) that
INTELLECT-1 measured across continents [@jaghouar2024intellect1]. Every floor below scales as one
over that utilisation, so a floor computed at it, and at the dense BF16 peak, is an estimate, not a
bound. No party can exceed full utilisation, and FP8 training at scale is in production
[@deepseek2024v3], at [2](numbers.md#phys-fp8-over-bf16) times the BF16 peak. The bound uses both
and sits [5.0](numbers.md#formal-floor-ref-over-bound) times below the estimates (P4).

## P1. The compute budget

### Definition

P1 is two quantities, each over a stated boundary.

**Training compute, C_train**, in FLOP at a stated precision. It is the total number of useful
operations, counted as the model's own arithmetic, executed on every chip whose outputs determine a
model's weights. The boundary is the weights' lineage, not a building or a company: pretraining,
post-training (including the reinforcement-learning rollouts that generate its training signal),
the teacher's generation when a model is distilled, and synthetic data generated for this lineage.
A run split across sites or providers is still one C_train.

**Inference throughput, R**, in FLOP/s. It is the sustained rate of useful operations needed to run
n copies of a model, each generating v tokens a second:

R = n × v × c, with c = [2](numbers.md#phys-flop-per-param-token) × N operations per token

for a decoder with N parameters, the forward-pass count Pope et al. give (attention adds little for
large models and is left out) [@pope2022]. Read the other way, a party's held compute H (chips times
peak times utilisation) supports at most n = H / (v × c) copies at speed v. It is an upper bound,
reached only if the utilisation in H can be had at speed v: generation at small batch is limited by
memory bandwidth and runs at low utilisation, while the large batches that reach high utilisation
slow each copy. That is how a holding turns into the copies and speed that the cognitive
perspective (F1) counts.

Both are defined "at a given algorithmic efficiency": how much C_train or R a superintelligent
system (D1) would need is not known, and this chapter does not pretend to know it. P1 fixes the
units in which the protocol counts; the computational perspective (A1 to A3) asks how much is
enough.

### How it is measured

Compute is measured as chips times peak rate times utilisation times time.

- **Chips.** Sales and holdings are tracked by the firms that make and buy them and estimated from
  outside. Summing Epoch's per-quarter median estimates gives
  [13,600,000 H100e](numbers.md#phys-chips-sold-2025) sold in 2025 against
  [5,100,000 H100e](numbers.md#phys-chips-sold-2024) in 2024, a factor of
  [2.7](numbers.md#phys-flow-2025-growth) in a year [@epoch2026chipsales]. This is the flow a
  registry would have to capture.
- **Peak rates** are vendor claims. An H100 SXM's dense BF16 peak is
  [989.5 TFLOP/s](numbers.md#phys-h100-bf16) [@nvidia-h100]; counting FP8 operations instead doubles
  it to [1,979 TFLOP/s](numbers.md#phys-h100-fp8), a factor of
  [2](numbers.md#phys-fp8-over-bf16), and the estimated CMOS ceiling at FP4 is
  [16](numbers.md#phys-fp4-over-fp16-ceiling) times the ceiling at FP16 [@ho2023]. A cap written in
  "FLOP" without a precision can be met on paper by switching precision. Counting chip-time in
  H100e-seconds avoids that.
- **Utilisation** is the factor outsiders cannot see. Measured model FLOPs utilisation runs from
  INTELLECT-1's [36.2%](numbers.md#phys-intellect1-mfu-low) to
  [41.4%](numbers.md#phys-intellect1-mfu-high) for decentralised training
  [@jaghouar2024intellect1] to [76%](numbers.md#phys-pope-mfu-prefill) for large-batch prefill on
  TPUs [@pope2022]. That spread, a factor of [2.1](numbers.md#phys-util-spread), carries into any conversion from chips to compute,
  and only on-site telemetry or power metering narrows it.
- **Inference** is measured by the operator, who logs tokens served. Outsiders see neither the
  tokens nor the model size.

Who could hide it. Chips leave the registry by smuggling and diversion: Epoch's model puts
cumulative compute smuggled into China through 2025 at [660,000 H100e](numbers.md#phys-smuggled-china) (90% CI [290,000 H100e](numbers.md#phys-smuggled-china-low) to [1,600,000 H100e](numbers.md#phys-smuggled-china-high)), with a median
[25%](numbers.md#phys-diversion-detect-rate) of diversion cases detected [@juniewicz2026smuggling].
Utilisation and precision can be misreported without moving a single chip.

### Evidence for and against

**For compute as the main input.** Training compute for frontier language models has grown
[5](numbers.md#phys-frontier-compute-growth) times a year since 2020 [@epoch2026trends]. Ho et al.
attribute [60%](numbers.md#phys-compute-share-low) to [95%](numbers.md#phys-compute-share-high) of
language-model gains from 2012 to 2023 to compute scaling [@ho2024algorithmic]. Across [809](numbers.md#phys-mertens-models) models,
Mertens et al. find that [80%](numbers.md#phys-frontier-explained-low) to
[90%](numbers.md#phys-frontier-explained-high) of performance differences at the frontier are
explained by training compute [@mertens2026secretsauce]. The share depends on the measure. On
Epoch's capability index, E1 finds that training compute explains
[36%](numbers.md#e1-compute-share) of growth across [105 models](numbers.md#e1-models), and from
[18%](numbers.md#e1-compute-share-subset-min) to [63%](numbers.md#e1-compute-share-subset-max)
across six samples of them [@epoch2026aimodels; @epoch2025eci].

**Against: algorithms substitute.** This is the strongest case against leaning on P1, and it
deserves its best statement. Compute needed for a fixed language-model loss halved every
[8.4 months](numbers.md#phys-algo-halving) (95% CI [4.5 months](numbers.md#phys-algo-halving-low) to
[14.3 months](numbers.md#phys-algo-halving-high)) [@ho2024algorithmic]. That is a factor of
[2.7](numbers.md#phys-algo-growth) a year ([1.8](numbers.md#phys-algo-growth-low) to
[6.3](numbers.md#phys-algo-growth-high) across the interval). MIRI's draft agreement assumes compute
per capability falls [3](numbers.md#phys-algo-miri) times a year and concludes that monitored
cluster sizes must fall as fast [@scher2025agreement]. If the headline physical and algorithmic
rates simply multiplied, frontier effective compute would grow about
[13](numbers.md#phys-effective-growth) times a year. A party that holds its chips fixed still gains
by the algorithmic factor, which is why a fixed compute cap leaks.

**Against the substitution argument, in turn.** Gundlach et al. find that of the
[22,000](numbers.md#phys-algo-total-ho)-fold efficiency gain credited to 2012 to 2023, less than
[100](numbers.md#phys-algo-small-scale-max)-fold appears at low compute, because the largest gains
(the Transformer, the Chinchilla rebalancing) depend on scale; only the first factor under ten comes
from their own ablations [@gundlach2025origin]. Whitfill estimates, as a first pass with other
explanations possible, that selection bias may overstate observational estimates by a factor of
about [9](numbers.md#phys-whitfill-bias) [@whitfill2025selection]. So algorithmic efficiency is not
one multiplier on physical compute, as D3 assumed. If Gundlach et al. are right, how fast a cap
leaks depends on where it sits: slowly well below the frontier, fast near it. E1 could not confirm
the direction on public data. On its full sample the gain a year falls with scale,
[-0.34 OOM a year per OOM](numbers.md#e1-drift-per-oom), but the sign is not robust across samples,
and in Ho et al.'s data the highest compute tercile progressed faster than the lowest in only
[52%](numbers.md#e1-ho-top-faster-share) of resamples [@ho2024algorithmiccode]. The rate itself runs
from [2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max)
times a year in compute-equivalent across samples of the same models: on public data, how fast a
fixed cap leaks is not identified.

**Inference substitutes too.** Ord illustrates the leak this way: a model trained with
[1e+24 FLOP](numbers.md#phys-ord-train-small) might, with [10,000](numbers.md#phys-ord-inference-mult)
times more inference compute, perform at the level of one trained with
[1e+27 FLOP](numbers.md#phys-ord-train-large), a training factor of
[1,000](numbers.md#phys-ord-train-equiv) [@ord2025govaireport]. It is an illustration, not a measured
exchange rate (that is E10's job). Reinforcement learning makes the boundary matter: INTELLECT-2
trained a reasoning model with rollouts generated by a permissionless swarm, consumer GPUs among
them, while only the training nodes were centralised [@primeintellect2025intellect2]. A boundary
drawn around the training cluster would miss most of that run's compute.

**Physical ceilings on single runs are far away.** Erdil and Schneider-Joseph find data movement
starts to lower utilisation for three-month runs above about
[1e+28 FLOP](numbers.md#phys-erdil-util-limit) and makes runs above
[1e+31 FLOP](numbers.md#phys-erdil-hard-limit) infeasible [@erdil2024datamovement]. Both sit orders
of magnitude above any cap the protocol would set, so they bound nothing it needs.

**What one site can do.** Colossus 1 had [100,000](numbers.md#phys-colossus1-h100) H100s online in
September 2024 [@epoch-datacenters-2026]. At the reference utilisation, over Rahman's longest sensible run today,
[4.5 months](numbers.md#phys-rahman-run-now) [@rahman2026], that is [4.7e+26 FLOP](numbers.md#phys-colossus1-run). Epoch estimates Microsoft's
Fairwater Atlanta site could do GPT-4-scale runs at a rate of
[23 runs a month](numbers.md#phys-fairwater-gpt4-runs), without stating GPT-4's compute or the utilisation assumed [@lee2025].

**Copies are physically abundant.** At its dense peak the 2025 chip flow is
[1.3e+22 FLOP/s](numbers.md#phys-flow-2025-flops). Pope et al. measured one copy of the dense PaLM model,
[540 billion parameters](numbers.md#phys-palm-params), generating at
[34.5 tokens/s](numbers.md#phys-pope-speed) on TPUs [@pope2022], which at
[2](numbers.md#phys-flop-per-param-token) operations per parameter per token is [3.7e+13 FLOP/s](numbers.md#phys-palm-copy-flops) per copy. At the reference
utilisation, one year's chip sales could therefore run at most about
[140,000,000](numbers.md#phys-flow-2025-copies) copies of a model that size at that speed. This is an
upper bound, since it mixes two batch regimes: Pope et al.'s speed is a small-batch latency, where
utilisation is low, and at the batch sizes that reach the reference utilisation each copy runs
slower. The same compute runs that many copies only at a lower speed, or fewer at this one. A model
with more active parameters, or one that thinks longer per task, runs proportionally fewer. The
point survives the caveats: copy counts were assumed in the essays that made them famous
[@karnofsky2022defeat; @amodei2024grace; @aschenbrenner2024sa], forecasts already compute them from
compute [@lifland2025timelines], and P1 lets an inspector do the same from an inventory.

**The brain, as a reference point.** Carlsmith judges it more likely than not that
[1e+15 FLOP/s](numbers.md#phys-brain-flops-central) is enough to match the brain, "given the right
software, which may be very hard to create", with a mechanistic range of
[1e+13 FLOP/s](numbers.md#phys-brain-flops-low) to [1e+17 FLOP/s](numbers.md#phys-brain-flops-high) and
under [10%](numbers.md#phys-brain-p90-chance) chance that more than [1e+21 FLOP/s](numbers.md#phys-brain-flops-p90) is needed
[@carlsmith2020]. One H100's dense peak is [0.99](numbers.md#phys-h100-brains) brains at the central
figure. The 2025 chip flow is [13,000,000](numbers.md#phys-flow-2025-brains-central) brains at the
central figure, and anywhere from [130,000](numbers.md#phys-flow-2025-brains-low) to
[1,300,000,000](numbers.md#phys-flow-2025-brains-high) across his range. Emulating a brain cell by
cell is far costlier: [1e+18 FLOP/s](numbers.md#phys-wbe-level4) to
[1e+25 FLOP/s](numbers.md#phys-wbe-level6) at the levels the roadmap's workshop thought most
likely [@sandberg2008]. These figures are raw operations, not capability. They say only that hardware is
not what stands between today's systems and many brain-equivalents of throughput. Software is. If
P1 binds anything, it binds training, not running.

**Left open.** Whether algorithmic progress is better treated as a multiplier on compute or as a
change of scaling exponent; how much inference substitutes for training at the scale of a cap; and
how much compute D1 needs. None is settled by the physical evidence.

### What the survey changed from the memo

The memo defined P1 correctly but measured it too simply ("from chip counts, peak rates and
utilisation"). Utilisation and precision are exactly the factors an outsider cannot see, and the
boundary must follow the weights' lineage through post-training, rollouts and distillation, or a
cap leaks through the parts left out. The memo gave P1 no novelty label. It is **prior work**:
compute as "detectable, excludable, and quantifiable" is Sastry et al.'s case [@sastry2024compute];
training compute as an initial filter that triggers scrutiny is Heim and Koessler's
[@heim2024thresholds]; verifying training runs by sampling chips is Shavit's
[@shavit2023chinchilla]; FLOP thresholds verified through chip tracking are MIRI's
[@scher2025agreement]. Computing copies at a speed from held compute and memory bandwidth is not a
contribution either: the arithmetic is Pope et al.'s bound applied to an inventory [@pope2022],
forecasts already compute copies from compute [@lifland2025timelines], and nothing in the protocol
triggers on it, so [the claims file](04-claims.md#cut-and-why) cuts it as too small. E12 and E20
still measure it. The survey also weakens the memo's pathway-table entry for unbounded scaling,
which answers "Necessary?" with "No, algorithms substitute": compute still explains a large share
of the measured gains, most of them in Ho et al. and Mertens et al., and from
[18%](numbers.md#e1-compute-share-subset-min) to [63%](numbers.md#e1-compute-share-subset-max) of
capability-index growth in E1.

### What it means for the protocol (a candidate)

- Count compute in chip-time at a reference precision (H100e-seconds), not in operations as
  reported, so a precision switch cannot game a threshold.
- Use training compute as a filter that triggers declaration and evaluation, not as the line. The
  line is D4, a time. Index the filter down with algorithmic progress. Whether more slowly for
  thresholds far below the frontier is open: Gundlach et al. say so, and E1 could not
  confirm the direction or identify the rate on public data.
- Draw C_train around the lineage: post-training, rollouts, teacher generation and synthetic data
  count, and continual-learning updates add to it.
- Count inference capacity (copies times speed) but do not limit it. It is what makes AI useful,
  and a limit would cost useful AI heavily. Counting costs little.
- Verification channel: the chip registry for H, on-site metering for utilisation.

### What would test it

- **E1** (compute against capability; how fast a fixed cap leaks) has run. It fitted capability on
  Epoch's model data against log compute and release date, and reran Ho et al.'s fit in compute
  bins. The rate is not identified: beyond what compute explains, growth moves with date at about
  [17](numbers.md#e1-algo-annual) times a year in compute-equivalent on all models, but from
  [2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max)
  across six samples, far beyond any one sample's interval. The scale dependence came out the other
  way on the full sample and is not robust across samples, so it is neither confirmed nor refuted;
  E15's ablations at three scales test it directly. On GPQA, training compute misplaces systems
  against PhD experts by up to [2.8 OOM](numbers.md#e1-gpqa-overlap-oom): the largest model that
  loses has that much more compute than the smallest that wins.
- **E10** (the training-to-inference exchange rate): measure, on small open models, how much
  sampling and search buy in training-compute terms, and whether the span widens only with a cheap
  verifier. Not run.
- **E7** (continual learning's update compute): measure how fast many small updates add up to a
  C_train that crosses a declaration threshold. Not run.
- **P-copies, now E12:** on the project's GPU (under `gpu`), measure generation speed at batch one
  and aggregate throughput at the best batch for open models of several sizes, and check the
  predicted n(v) curve, n = H / (v × 2N), against the measurements. It passes if measured throughput
  stays within the factor of a few that Pope et al. found between the bound and practice. Not run.

## P2. Energy per useful operation, and the headroom to physics

### Definition

**e**, in joules per useful operation, is the energy drawn at the facility meter divided by the
useful operations it bought (counted as in P1). The boundary is the facility, because that is where
an independent meter can sit. It factors into four terms, each measurable:

e = (chip power / chip peak) × (IT power / chip power) × (facility power / IT power) / utilisation

The **headroom** is today's e over the lowest e that physics or engineering allows. There are two
headrooms, not one:

1. to the **CMOS ceiling**, the most efficient that irreversible digital logic of today's kind can
   become; and
2. to **Landauer's bound**, kT ln 2 per erased bit, which binds only irreversible operations and
   says nothing directly about how many bits an operation must erase.

### How it is measured

The chip term comes from datasheets (vendor claims). At dense 16-bit peak and maximum chip power,
energy per operation fell from [2.40e-12 J](numbers.md#phys-v100-j-per-flop) on the V100
[@nvidia-v100] to [1.28e-12 J](numbers.md#phys-a100-j-per-flop) on the A100 [@nvidia-a100] and
[7.07e-13 J](numbers.md#phys-h100-j-per-flop) on the H100 [@nvidia-h100], with AMD's MI300X at
[5.74e-13 J](numbers.md#phys-mi300x-j-per-flop) [@amd-mi300x]. A B200 measured at the DGX system
wall, not at the chip, spends [7.94e-13 J](numbers.md#phys-b200-system-j-per-flop) [@nvidia-dgx-b200].

The other terms come from facilities. At Colossus 1, Epoch's timeline gives
[139 MW](numbers.md#phys-colossus1-it-power) of IT power and
[181 MW](numbers.md#phys-colossus1-facility-power) of facility power for
[100,000](numbers.md#phys-colossus1-h100) H100s [@epoch-datacenters-2026]. That is
[1,390 W](numbers.md#phys-it-power-per-h100) of IT power and
[1,810 W](numbers.md#phys-facility-power-per-h100) of facility power per chip: a server overhead
factor of [1.99](numbers.md#phys-it-overhead) over the chip's [700 W](numbers.md#phys-h100-tdp) and a facility-to-IT ratio of
[1.30](numbers.md#phys-pue-colossus). At the reference utilisation the whole chain gives
[4.57e-12 J](numbers.md#phys-facility-j-per-useful-flop) per useful operation,
[6.5](numbers.md#phys-facility-over-chip) times the datasheet figure.

Measurement error. Per-chip power differs by a factor of
[1.9](numbers.md#phys-power-per-chip-spread) between sources: Epoch's tracked
sites average [956 W](numbers.md#phys-epoch-dc-it-per-h100e) of IT power per H100e (the database includes newer chips, which do more per watt) [@epoch-datacenters-2026]; Scher and Thiergart's example implies
[1,200 W](numbers.md#phys-scher-w-per-h100) [@scher2025]; Sastry et al.'s DGX figure implies
[1,280 W](numbers.md#phys-sastry-w-per-h100) [@sastry2024compute]; Colossus 1 gives
[1,810 W](numbers.md#phys-facility-power-per-h100) at the facility. Any conversion from power to compute carries that spread, times the utilisation spread
from P1.

Who can measure it, and whether it can be faked. Chip specifications are public. Facility energy is
metered by utilities and can be metered on site by an inspector. Utilisation is seen only on site.
A party cannot easily fake the energy an independent meter records, but it can run at an unusual
utilisation so that energy converts to the wrong compute, which is why P4's on-site channel
measures the kind of work and not only the amount.

### Evidence for and against

**The floor itself.** Landauer's bound is [2.871e-21 J](numbers.md#phys-kt-ln2-room) per erased bit
at [300 K](numbers.md#phys-temp-room) [@landauer1961; @codata2022-k]. It has been reached in experiment, but only slowly. In a
colloidal one-bit memory the heat per erasure approaches [0.72 kT per bit](numbers.md#phys-berut-fit-a) in
the slow limit, against kT ln 2 = [0.693 kT per bit](numbers.md#phys-ln2), with erasures lasting up to
[40 s](numbers.md#phys-berut-tau-max) [@berut2015]. Extrapolating that experiment's fitted excess
heat to a [1 ns](numbers.md#phys-fast-erasure) erasure, far outside the measured range and only to make the trade-off
concrete, gives [8.2e+09 kT per bit](numbers.md#phys-berut-1ns). A nanomagnetic memory, a practical
digital technology, dissipated [1.45 kT per bit](numbers.md#phys-hong-erasure) in an adiabatic
erasure, within two standard deviations of the bound [@hong2014]. Landauer himself warned that his
reasoning "gives no guarantee that this minimum is in fact achievable" [@landauer1961], and Bennett
notes that logically reversible operations have no such floor in principle [@bennett2003].

**How far above it chips sit.** An H100 spends [2.5e+08](numbers.md#phys-h100-landauer-ratio) times
kT ln 2 per operation. That compares an operation with a bit, so it is an upper bound on the
headroom, not a like-for-like gap: an operation erases many bits, and nobody fixes how many.
Davidson et al., in a takeoff analysis, assume about [6 orders of magnitude](numbers.md#phys-davidson-landauer-oom) of room to Landauer [@davidson2025three]. Either way, the gap to physics is six
to eight orders of magnitude.

**The ceiling that binds first.** Ho, Erdil and Besiroglu estimate the maximum efficiency of
irreversible CMOS at [2.9e+14 FLOP/J](numbers.md#phys-cmos-ceiling-fp16) at FP16 (from
[4.7e+15 FLOP/J](numbers.md#phys-cmos-ceiling-fp4) at FP4), with a log-space spread of about
[0.7 orders of magnitude](numbers.md#phys-cmos-log-sd) [@ho2023]. Against the H100's
[1.41e+12 FLOP/J](numbers.md#phys-h100-flop-per-j) that leaves
[205](numbers.md#phys-cmos-headroom)-fold (their own figure is
[207](numbers.md#phys-cmos-headroom-ho)). If the ceiling is log-normal with their spread, the 5th to
95th percentile range is [14](numbers.md#phys-cmos-headroom-p05) to
[2,900](numbers.md#phys-cmos-headroom-p95)-fold. Even at the ceiling, an FP16 operation costs
[1.2e+06](numbers.md#phys-cmos-landauer-ratio) times kT ln 2. The CMOS ceiling, not Landauer, is what
binds this century's footprint.

**How fast hardware approaches it.** Koomey et al. measured the computations bought per
kilowatt-hour doubling every [1.57 years](numbers.md#phys-koomey-doubling) from 1946 to 2009
[@koomey2011]; peak-output efficiency slowed to a doubling every
[2.7 years](numbers.md#phys-koomey-doubling-post2000) after about 2000 [@koomey2015]. For AI
hardware, Pilz et al. measure supercomputer efficiency improving
[1.34](numbers.md#phys-eff-growth-supercomputer) times a year (90% CI
[1.25](numbers.md#phys-eff-growth-supercomputer-low) to
[1.43](numbers.md#phys-eff-growth-supercomputer-high)), mostly from new chips, with facility
overheads improving less than [5%](numbers.md#phys-pue-growth-max) a year
[@pilz2025supercomputers]; You and Owen give [1.40](numbers.md#phys-eff-growth-gpu) a year for GPUs
[@you2025]. At those rates the median CMOS headroom is used up in
[16 years](numbers.md#phys-years-to-cmos-fast) to [18 years](numbers.md#phys-years-to-cmos-slow).

**The steelman for more headroom.** Three things cut the other way. The ceiling is uncertain by
more than an order of magnitude either side. Reversible computing exists in silicon: the first
adiabatic test chip reportedly drew about [30%](numbers.md#phys-reversible-test-saving) less energy
than a conventional chip on the same task, in one test with no independent verification described
[@hulick2025], and a vendor's road map shows a [4,000](numbers.md#phys-reversible-roadmap)-fold gain that,
by the article's own estimate, is more than a decade away [@genkina2025]. Both are vendor claims. And the other terms of e have
room too: removing every overhead (server, cooling, idle time) would buy at most another
[6.5](numbers.md#phys-facility-over-chip)-fold, so the facility's energy per useful operation could
fall by about [1,300](numbers.md#phys-facility-headroom)-fold in all before CMOS binds. None of this
counts algorithmic progress, which lowers the operations needed rather than the joules each costs,
and which physics does not bound.

**The brain, again as a reference.** At Carlsmith's central figure and
[20 W](numbers.md#phys-brain-power) [@carlsmith2020], the brain does
[5e+13 FLOP/J](numbers.md#phys-brain-flop-per-j), [35](numbers.md#phys-brain-over-h100) times an
H100. The estimated CMOS ceiling is [5.8](numbers.md#phys-cmos-over-brain) times beyond that. The
brain also runs far above Landauer: at body temperature its [20 W](numbers.md#phys-brain-power) could erase at most
[6.7e+21 bits/s](numbers.md#phys-brain-landauer-cap). And in the cortex, by Levy and
Calvert's estimate (abstract only), communication costs [3.5 W](numbers.md#phys-cortex-comm-power)
against [0.1 W](numbers.md#phys-cortex-compute-power) for computation [@levy2021]: moving information
costs more than computing on it, in biology as in silicon (P3).

### What the survey changed from the memo

The memo set P2's headroom against Landauer's bound. That headroom exists but is irrelevant on the
protocol's timescale; the binding limit is the CMOS ceiling, about two orders of magnitude away, not
eight. The memo also left out the facility terms, which multiply the datasheet figure by
[6.5](numbers.md#phys-facility-over-chip).
The comparison is **prior work**: Ho, Erdil and Besiroglu compute the ceiling and the headroom over
the H100 [@ho2023]; Koomey et al. record Feynman's much larger theoretical estimate [@koomey2011];
Carlsmith uses Landauer to bound the brain [@carlsmith2020]. The only new use here is as an upper
bound on how far a fixed computation's physical trace can shrink from hardware alone, which Ho et
al. do not draw. That is an application, not a contribution.

### What it means for the protocol (a candidate)

- P2 is the conversion between a facility meter and compute, and it carries an error bar of
  [1.9](numbers.md#phys-power-per-chip-spread) in power per chip times [2.1](numbers.md#phys-util-spread) in utilisation. Energy alone cannot certify an
  amount of compute.
- Any power or energy threshold in the protocol must fall over time at least at the hardware
  efficiency rate, about [1.34](numbers.md#phys-eff-growth-supercomputer) to
  [1.40](numbers.md#phys-eff-growth-gpu) times a year, plus whatever algorithms take off the
  operations needed.
- Hardware can shrink the energy trace of a fixed computation by roughly three orders of magnitude
  before CMOS binds, over a decade or two at trend. Algorithms can shrink it further, without a
  physical limit. Energy-based channels therefore erode on a known schedule.
- Reversible computing is a watch item: if its gains reach orders of magnitude at the wall, energy
  channels weaken faster than the CMOS schedule says.
- Measuring e costs useful AI nothing.

### What would test it

- **E8** has run on P2's decomposition, turning compute into energy and power, with its Monte Carlo
  drawing power per chip over the measured spread, not a point value. Its results are under P4.
- **P-energy, now E13:** on the project's GPU (under `gpu`), log board power from the driver while
  running training and inference at several batch sizes, and compute each chip-side term of e from
  the measurements; with no wall meter, the facility overhead stays sourced. It passes if the
  measured e exceeds the datasheet figure by a factor that the measured utilisation accounts for,
  and it shows how much worse small-batch generation (memory-bound) is per useful operation than
  large-batch work. Not run.

## P3. Memory and bandwidth

### Definition

P3 is three quantities.

1. **State, S**, in bytes per copy: the weights at their stored precision and the attention cache
   during inference; for training, also optimiser state and activations.
2. **Memory bandwidth per copy, B_copy**, in bytes a second: the summed memory bandwidth of the
   chips that hold one copy. At small batch the weights must be read from memory once per generated
   token [@pope2022], so one copy's serial speed is bounded by

   v ≤ B_copy / (N × z)

   tokens a second, for N parameters stored at z bytes each. B_copy grows only by spreading a copy
   over more chips, and then chip-to-chip communication, which "decreases less quickly (or not at
   all) with the number of chips used", becomes the bottleneck [@pope2022].
3. **Interconnect bandwidth, I**, in bits a second between the groups of chips that train one
   model. It bounds how far training can spread. Low-communication methods cut the bytes exchanged
   per unit of compute.

### How it is measured

All three are chip and network properties, fixed at manufacture and listed in datasheets (vendor
claims). An H100 SXM has [80 GB](numbers.md#phys-h100-hbm-cap) of memory at
[3.35 TB/s](numbers.md#phys-h100-hbm-bw) and NVLink at [900 GB/s](numbers.md#phys-h100-nvlink)
[@nvidia-h100]. A GB200 GPU has [8 TB/s](numbers.md#phys-gb200-hbm-bw) of memory bandwidth and
[1.8 TB/s](numbers.md#phys-gb200-nvlink) of NVLink [@nvidia-gb200], against a scale-out port of
[400 Gbit/s](numbers.md#phys-scale-out-port) [@nvidia-dgx-b200]: scale-up bandwidth is
[36](numbers.md#phys-scale-up-over-out) times scale-out per GPU.

Bandwidth trails compute. Memory bytes per dense 16-bit operation were
[7.2e-03 bytes/FLOP](numbers.md#phys-v100-bytes-per-flop) on the V100,
[6.5e-03 bytes/FLOP](numbers.md#phys-a100-bytes-per-flop) on the A100,
[3.4e-03 bytes/FLOP](numbers.md#phys-h100-bytes-per-flop) on the H100,
[3.6e-03 bytes/FLOP](numbers.md#phys-b200-bytes-per-flop) on the B200 and
[3.2e-03 bytes/FLOP](numbers.md#phys-gb200-bytes-per-flop) on the GB200 (AMD's MI300X:
[4.1e-03 bytes/FLOP](numbers.md#phys-mi300x-bytes-per-flop)). From V100 to B200, peak operations rose
[18](numbers.md#phys-flops-rise-v100-b200)-fold and bandwidth [8.9](numbers.md#phys-bw-rise-v100-b200)-fold,
so bytes per operation fell by [2.0](numbers.md#phys-bytes-per-flop-fall). Over twenty years,
Gholami et al. report peak server operations growing [3.0](numbers.md#phys-gholami-flops-growth)
times every two years against [1.6](numbers.md#phys-gholami-dram-growth) for memory bandwidth and
[1.4](numbers.md#phys-gholami-interconnect-growth) for interconnect (abstract only)
[@gholami2024]; Hobbhahn et al. find accelerator memory bandwidth doubling every
[4.1 years](numbers.md#phys-hobbhahn-mem-bw-doubling) against
[2.3 years](numbers.md#phys-hobbhahn-flops-doubling) for operations [@hobbhahn2023].

The serial-speed bound is checkable against a measurement. Pope et al. served PaLM's
[540 billion parameters](numbers.md#phys-palm-params), quantised to int8, on
[64](numbers.md#phys-pope-chips) TPU v4 chips with [1,200 GB/s](numbers.md#phys-tpuv4-hbm-bw) of
memory bandwidth each, and measured [29 ms](numbers.md#phys-pope-latency) per token at small batch
[@pope2022]. Reading the weights once takes [7.0 ms](numbers.md#phys-pope-memory-bound), a bound of
[142 tokens/s](numbers.md#phys-pope-bound-speed). The measured latency is
[4.1](numbers.md#phys-pope-over-bound) times the floor: the bound holds, and practice sits within a
small factor of it.

Who can measure it, and whether it can be faked. Memory bandwidth is visible in a chip's part
number, in inspection and in export rules. The US already regulates on it: a 2023 rule added a
performance-density parameter because buying more, smaller chips was a workaround
[@bis2023advancedcomputing], and a December 2024 rule controls high-bandwidth memory by "memory
bandwidth density", noting that all stacks then in production exceeded the threshold [@bis2024hbm].
A party cannot raise a chip's bandwidth after manufacture. Interconnect between sites is harder to
watch: links of a few Gbit/s look like ordinary traffic.

### Evidence for and against

**Serial speed is bounded per copy.** A PaLM-sized model in int8 needs
[6.8](numbers.md#phys-palm-h100-min) H100s just to hold its weights. On one H100 server of [8 GPUs](numbers.md#phys-dgx-b200-gpus) its serial speed cannot exceed
[50 tokens/s](numbers.md#phys-palm-8h100-speed); on as many GB200 GPUs,
[119 tokens/s](numbers.md#phys-palm-8gb200-speed). Because bandwidth grows more slowly than
operations, serial speed per copy improves more slowly than total throughput. The "speed" kind of
advantage that F1 counts is physically capped per copy by B_copy; the "copies" kind is capped by
held compute (P1). This confirms the memo's claim that memory bandwidth per copy bounds serial speed, with the
qualification that a copy spread over more chips is faster until communication binds.

**Interconnect no longer keeps training in one place.** DiLoCo matched fully synchronous training on
eight workers while communicating [500](numbers.md#phys-diloco-comm-reduction) times less, for
models up to a few hundred million parameters [@douillard2023diloco]. Streaming DiLoCo reaches [95%](numbers.md#phys-streaming-util) compute utilisation for models of
[1 billion parameters](numbers.md#phys-streaming-size-low) to [100 billion parameters](numbers.md#phys-streaming-size-high) with
[1 Gbit/s](numbers.md#phys-streaming-bw-low) to [5 Gbit/s](numbers.md#phys-streaming-bw-high) between
sites, where data parallelism needs [100 Gbit/s](numbers.md#phys-dp-bw-low) to
[300 Gbit/s](numbers.md#phys-dp-bw-high), [60](numbers.md#phys-streaming-over-dp) times more for
the largest model [@douillard2025streaming]. INTELLECT-1 trained a model of [10 billion parameters](numbers.md#phys-intellect1-params) on up to [112](numbers.md#phys-intellect1-gpus) H100s across three continents, over
links of [0.5 Gbit/s](numbers.md#phys-intellect1-bw-low) to [4 Gbit/s](numbers.md#phys-intellect1-bw-high),
synchronising every [38 minutes](numbers.md#phys-intellect1-sync) [@jaghouar2024intellect1]. DeMo
and SWARM cut communication further, for data and pipeline parallelism respectively
[@peng2024demo; @ryabinin2023swarm]. Frontier labs plan around the same methods: Meta describes
clusters spanning several buildings and software for "long-distance training across a
geographically distributed set of data centers" [@meta-infra-2025], and Epoch sketches a
multi-gigawatt run spread across spare capacity at existing gas plants [@sevilla2025-power].

**The tax is real but small at the scale of a cap.** Rahman's nodes are joined by
[100 Mbit/s](numbers.md#phys-rahman-bandwidth) links, [72,000](numbers.md#phys-nvlink-over-wan)
times slower than one H100's NVLink, yet distributed training at that bandwidth costs only about
[3](numbers.md#phys-rahman-cost-ratio) times centralised training [@rahman2026]. Decentralised
training compute has grown [20](numbers.md#phys-decentral-growth) times a year, its largest runs
reaching [6e+23 FLOP](numbers.md#phys-decentral-largest), about
[1,000](numbers.md#phys-decentral-gap) times below the frontier, over consumer upload links of
about [60 Mbit/s](numbers.md#phys-consumer-upload) [@sevilla2025decentralized].

**The steelman for interconnect still binding.** At frontier scale, bandwidth still concentrates
training. Rahman's distributed configuration for [1e+26 FLOP](numbers.md#phys-rahman-1e26-local)
of local compute keeps only [21%](numbers.md#phys-rahman-1e26-eff) of it after quality adjustment
[@rahman2026]. If both trends held, decentralised training would catch the frontier in about
[5.5 years](numbers.md#phys-decentral-catchup), and Sevilla expects it will not this decade
[@sevilla2025decentralized]. Shavit notes that consumer GPUs have [64 GB/s](numbers.md#phys-rtx4090-interconnect) of
interconnect against the H100's [900 GB/s](numbers.md#phys-h100-nvlink), and his chip monitoring
covers clusters split across data centres as long as each uses high-end chips
[@shavit2023chinchilla]. So the loosening matters most at and below about
[1e+25 FLOP](numbers.md#phys-rahman-1e25-target), which is exactly where caps sit, and least for
frontier runs.

### What the survey changed from the memo

The memo's P3 is right in substance and is **prior work**: the memory wall [@gholami2024], hardware
trends [@hobbhahn2023], data movement limits [@erdil2024datamovement], the low-communication methods
[@douillard2023diloco; @douillard2025streaming] and their governance consequences
[@sevilla2025decentralized; @krys2025distributed]. What changes is what the memo's P4 relied on without saying so: that
interconnect keeps training at scale on one site, where facilities can be watched. Below about [1e+25 FLOP](numbers.md#phys-rahman-1e25-target) that no longer holds, and the per-site footprint floor of P4
collapses with it. The serial-speed bound is Pope et al.'s memory time; using it with P1 to bound a
fleet's copies and speed from its inventory is that bound applied, and forecasts already compute
copies from compute [@lifland2025timelines]. The claims file cuts it as too small (P1).

### What it means for the protocol (a candidate)

- Memory bandwidth and scale-up interconnect are what make a chip an AI chip. Register and license
  chips by them, as export rules already do, and audit bandwidth per chip at inspection.
- Do not rely on interconnect to keep a run on one site. Facility-based channels must assume an
  adversary training across sites at a few Gbit/s.
- Measure serial speed; do not limit it. An inspector can bound a fleet's copies times speed from
  its inventory (H and B_copy). Limiting bandwidth would slow inference for every user, a high cost
  to useful AI for little gain.

### What would test it

- **P-speed, now part of E12:** on the project's GPU (under `gpu`), run open models spanning more
  than an order of magnitude in size, each at several weight precisions, measure batch-one
  generation speed, and compare it with the bound
  B / (N × z) from the GPU's measured memory bandwidth. Prediction: every measurement sits below the
  bound and within a small factor of it, as Pope et al.'s did. Not run.
- **P-diloco, now E14:** train a small model with a DiLoCo-style method across two processes whose link
  is throttled to [100 Mbit/s](numbers.md#phys-rahman-bandwidth) and to
  [1 Gbit/s](numbers.md#phys-streaming-bw-low), and measure loss against synchronous training at
  equal compute. This reproduces, at small scale, the tax curve that E8 needs for distributed
  adversaries. Not run.

## P4. The footprint and its floor

### Definition

The **footprint** of a training run of C useful operations finished within time T is the set of
traces it leaves: chips (in H100e), energy (MWh), average power (MW), heat, water and construction.
The **floor** is the smallest footprint that could still produce the run. The survey forces it to
be defined twice, because different channels see different floors.

1. **The per-site floor**: the smallest site that can contribute to the run. With low-communication
   training (P3) it is one node. A node of [16](numbers.md#phys-rahman-gpus-per-node) H100s at
   Colossus 1's facility power per chip draws [29 kW](numbers.md#phys-node-power).
2. **The aggregate floor in chips**: N_min = C / (r × u × T), for a per-chip peak r, utilisation u
   and run time T, with T no longer than the longest run that makes sense (Rahman's
   T = 1/(gH + gS + gI), set by the growth rates of hardware, software and investment) [@rahman2026].
   It is a bound only when r is the peak at the lowest precision a run can use (FP8 in the sources;
   a run held to BF16 needs twice the chips) and u the highest utilisation an adversary can reach,
   full for the bound ([Theorem 8.1](05-formal.md#c8-the-footprint-floor-as-a-bound)). At a typical
   utilisation or a higher precision it is an estimate. T is an assumption about the adversary, not
   physics: a racing or patient party need not share it, and the floor halves when T doubles. The
   chip-time C / (r × u) holds whatever T the adversary picks:
   [1,600 H100e-years](numbers.md#e8-chip-years-1e26-bound) for a
   [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run as a bound.
3. **The aggregate floor in energy**: E_min = C × e (P2), with average power E_min / T. As a bound, e
   is the lowest energy per operation of any chip the party can use.

For each channel, the **detection margin** is its detection limit divided by the floor it sees. A
channel can enforce a threshold only where its margin is below one.

The aggregate floor in chips with a time axis, the untraced pool counted against it, and the
conclusion that the pool must be shrunk rather than found are the hardwired-pause working group's
[@fithian2026hardwired], whose threshold is an estimate at standard utilisation. What this chapter
adds is narrower and listed under "What the survey changed from the memo" below.

### How it is measured

Each channel has its own limit.

- **Satellite imagery** finds and sizes known sites. A satellite-image classifier of data centres,
  its misses checked by hand, missed four real data centres in its evaluation sample, the largest at
  [3.2 MW](numbers.md#phys-sat-miss-max) [@clymer2025datacenter]. Koopmanschap and Barten read it as
  finding every facility above [10 MW](numbers.md#phys-sat-reliable) and missing every one below, a
  small sample [@koopmanschap2026gpu]. Epoch's imagery
  estimates a site's IT power within a factor of [1.4](numbers.md#phys-sat-it-accuracy)
  [80%](numbers.md#phys-sat-it-confidence) of the time; its database holds [96 sites](numbers.md#phys-epoch-dc-sites) with
  [15.1 GW](numbers.md#phys-epoch-dc-it-power) and [15,800,000 H100e](numbers.md#phys-epoch-dc-h100e), about [43%](numbers.md#phys-epoch-dc-coverage) of global AI compute (90% CI
  [29%](numbers.md#phys-epoch-dc-coverage-low) to [77%](numbers.md#phys-epoch-dc-coverage-high)),
  and [43 sites](numbers.md#phys-epoch-dc-small) are below [100 MW](numbers.md#phys-epoch-small-threshold)
  [@epoch-datacenters-2026]. Imagery confirms more than it discovers: a satellite study of
  hyperscale growth judges that finding undeclared hyperscale sites from scratch "may not be
  feasible" [@krawec2026]. Above the satellite line, a covert facility hides among about
  [500 sites](numbers.md#phys-dc-above-10mw), the data centres larger than [10 MW](numbers.md#phys-sat-reliable) worldwide (an estimate)
  [@pilz2023]; below it, a cluster of [100 H100e](numbers.md#phys-container-cluster) fits in a
  shipping container with no noticeable external cooling [@koopmanschap2026gpu]. The strongest
  signature is construction, not operation [@teague2026];
  Colossus 1 went from construction start to [100,000](numbers.md#phys-colossus1-h100) H100s in
  [131 days](numbers.md#phys-colossus1-build-days), in public view [@epoch-datacenters-2026].
- **Thermal infrared** does not see waste heat at current resolutions. Over a Tokyo cluster drawing
  at least [126 MW](numbers.md#phys-jing-cluster-power), deep-night facility-scale surface
  temperature changes were "indistinguishable from zero", bounded below
  [0.6 °C](numbers.md#phys-jing-night-low) to [1.2 °C](numbers.md#phys-jing-night-high) [@jing2026].
  A preprint claiming an average surface warming around data centres gives no method in its abstract
  for separating the facility's effect [@marinoni2026]. Wasil et al.'s view that heat signatures
  are "difficult to mask" [@wasil2024verification] is not supported by the measurements found.
- **The grid** sees large loads on paper. A US utility requires a system impact study at
  [5 MW](numbers.md#phys-utility-study), but has no authority over power generated behind the
  meter, as with xAI's turbines in Memphis [@mlgw2025]. Interconnection queues are dominated by
  speculative requests (Texas tracks [410 GW](numbers.md#phys-ercot-queue) of large loads)
  [@ercot2026], and a [100 kW](numbers.md#phys-commercial-load) load sits among millions of
  mid-size commercial customers [@koopmanschap2026gpu].
- **Water** is optional: [21.0 million gallons a day](numbers.md#phys-water-new-carlisle) at one site
  against [0.0077 million gallons a day](numbers.md#phys-water-fairwater-wi) at a closed-loop one
  [@epoch-datacenters-2026].
- **On-site power metering**, at a declared site, tells the kind of work well and the amount
  poorly. A tracker of the training iteration cadence in facility power detects
  [96%](numbers.md#phys-meter-detect) of undisguised training runs against a declared inference
  workload at a [1%](numbers.md#phys-meter-false-alarm) false-alarm rate, on simulated power; against the strongest disguise it still
  catches [87%](numbers.md#phys-meter-day-detect) of runs over a day, and the disguise costs
  [93%](numbers.md#phys-meter-evasion-cost-low) to [267%](numbers.md#phys-meter-evasion-cost-high)
  more compute in small-scale training [@kimpson2026dcpower]. GPU supply current flags
  [99.9%](numbers.md#phys-supply-current-detect) of prohibited training windows against a declared
  baseline, though a corrupt baseline fails silently [@kimpson2026supply], and a physical side
  channel on an H200's power draw separates training, inference and other work with [97%](numbers.md#phys-sidechannel-accuracy)
  accuracy without the operator's cooperation [@gargiulo2026sidechannel]. But a power trace alone
  cannot exclude hidden computation of [0.41](numbers.md#phys-beta-matched) to
  [1.16](numbers.md#phys-beta-worst) times the declared capacity, falling to
  [0.059](numbers.md#phys-beta-restricted) only with re-execution of declared work (abstract only)
  [@kimpson2026b].
- **Chip accounting** is the only channel modelled here that sees the aggregate. A distributed run's
  traffic and purchases are aggregate signatures too, which no experiment here models. Epoch traced most of the world's
  AI chips to owners, leaving "on the order of a million chips unaccounted for"
  ([1,000,000 chips](numbers.md#phys-chips-unaccounted)), which Koopmanschap and Barten take as an
  approximate bound on the largest hidden cluster [@koopmanschap2026gpu]. Smuggled compute adds
  [660,000 H100e](numbers.md#phys-smuggled-china) at the median [@juniewicz2026smuggling]. Outside
  estimates of a rival's output disagree by a factor of [4.0](numbers.md#phys-huawei-spread): at
  most [200,000](numbers.md#phys-huawei-commerce) Huawei chips in 2025 by the US Commerce
  Department's statement [@zafar2025kessler], [805,000](numbers.md#phys-huawei-semianalysis) by
  SemiAnalysis [@patel2025ascend] (the units differ, capacity against shipments). Shavit's chip
  sampling would need about [232 inspectors](numbers.md#phys-shavit-inspectors) to catch a
  [1e+25 FLOP](numbers.md#phys-shavit-run) run within [30 days](numbers.md#phys-shavit-days) of its
  completion with probability [0.9](numbers.md#phys-shavit-prob), but only if every chip carries the firmware; legacy chips
  set a lower bound on what it can see [@shavit2023chinchilla].

### Evidence for and against

**The floors, computed from measured inputs.** Take MIRI's prohibited threshold,
[1e+24 FLOP](numbers.md#phys-miri-strict) [@scher2025agreement]. At the reference utilisation and
the BF16 peak, over today's longest sensible run of [4.5 months](numbers.md#phys-rahman-run-now) it
needs an estimated [210 H100e](numbers.md#phys-floor-chips-1e24-now); over the
[24 months](numbers.md#phys-rahman-run-pause) that Rahman finds rational under a pause, an estimated
[40 H100e](numbers.md#phys-floor-chips-1e24-pause) [@rahman2026]. Its energy at Colossus 1's
overheads and the reference utilisation is [1,300 MWh](numbers.md#phys-floor-energy-1e24), an
average of [0.39 MW](numbers.md#phys-floor-power-1e24-now) over the shorter run and
[0.072 MW](numbers.md#phys-floor-power-1e24-pause) over the longer. For
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local), the estimate is
[21,000 H100e](numbers.md#phys-floor-chips-1e26-now) today and
[4,000 H100e](numbers.md#phys-floor-chips-1e26-pause) under a pause, with
[130,000 MWh](numbers.md#phys-floor-energy-1e26) of energy: an average of
[39 MW](numbers.md#phys-floor-power-1e26-now) over the shorter run and
[7.2 MW](numbers.md#phys-floor-power-1e26-pause) over two years. The second is below the satellite
line even if it all sat on one site.

These are estimates, not bounds. A party can train at FP8 and can run its chips harder than
[40%](numbers.md#phys-util-ref); a floor computed at the reference utilisation was undercut in
random runs that the formal part checked. The bound, at the FP8 peak and full utilisation, is
[5.0](numbers.md#formal-floor-ref-over-bound) times lower: for the pause run,
[8.0 H100e](numbers.md#e8-floor-1e24-pause-bound) for
[1e+24 FLOP](numbers.md#phys-miri-strict) and [800 H100e](numbers.md#formal-floor-bound-1e26-pause)
for [1e+26 FLOP](numbers.md#phys-rahman-1e26-local), or
[1,600 H100e](numbers.md#formal-floor-bound-1e26-pause-bf16) for a run held to BF16
([C8](05-formal.md#c8-the-footprint-floor-as-a-bound)). E8 reproduces the ledger's floor and gives the
same bound, [800 H100e](numbers.md#e8-floor-1e26-pause-bound); with utilisation drawn across its
measured range, its median estimate is [2,900 H100e](numbers.md#e8-floor-1e26-pause-p50). The bound
is what the line may rely on; it holds only while FP8 is the lowest precision a run can train at.

**The per-site floor is one node.** A [29 kW](numbers.md#phys-node-power) node sits
[345](numbers.md#phys-sat-over-node) times below the satellite line and
[173](numbers.md#phys-utility-over-node) times below the utility study threshold. Rahman computes
the configurations directly: [1e+24 FLOP](numbers.md#phys-miri-strict) on
[2](numbers.md#phys-rahman-1e24-nodes) such nodes for [1.6 million USD](numbers.md#phys-rahman-1e24-cost); a [1e+25 FLOP](numbers.md#phys-rahman-1e25-target) target on
[34 nodes](numbers.md#phys-rahman-1e25-nodes) of GH200s, reaching
[6.4e+24 FLOP](numbers.md#phys-rahman-1e25-quality) after quality adjustment
([64%](numbers.md#phys-rahman-1e25-eff)) for [30.7 million USD](numbers.md#phys-rahman-1e25-cost); and [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) of local compute on
[4,706 nodes](numbers.md#phys-rahman-1e26-nodes), reaching only
[2.1e+25 FLOP](numbers.md#phys-rahman-1e26-quality) for [3.80 billion USD](numbers.md#phys-rahman-1e26-cost). "If a frontier-scale cluster were split into nodes smaller than the regulator's
monitoring threshold, it would be undetectable by thermal and electrical means" [@rahman2026]. Krys
et al. call the same move compute structuring [@krys2025distributed].

**The aggregate floor is below chip accounting's resolution.** In E8, for a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run at a pause's run length, with the floor at the
BF16 peak and utilisation drawn over its measured range, the untraced pool, at its assumed size of
[1,000,000 chips](numbers.md#phys-chips-unaccounted), is a median
[340](numbers.md#e8-pool-over-floor-1e26-pause-p50) times the floor. That is a point at an assumed
pool, not a range: the pool's size is an assumption (Epoch's "order of magnitude", from a source
that expects most of the rest can be traced), and the spread E8 draws around it, within a factor
of the square root of ten, is our reading of that phrase, not a sourced range, so its percentiles
are not reported here. The compute smuggled into one country, which has a published interval, is
[230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times it
([94](numbers.md#e8-smuggled-over-floor-1e26-pause-p05) to
[590](numbers.md#e8-smuggled-over-floor-1e26-pause-p95)). An FP8 run doubles each ratio. Against the
floor taken as a bound, the smuggled median is [824](numbers.md#formal-pool-over-floor-bound) times
it. Even at today's run length, the smuggled stock over the floor has a 5th percentile of
[18](numbers.md#e8-smuggled-over-floor-1e26-now-p05). For chip accounting to resolve
the pause-length run at the bound, the pool would have to shrink
[1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold, and
[120,000](numbers.md#e8-pool-shrink-1e24-pause)-fold for one at
[1e+24 FLOP](numbers.md#phys-miri-strict). On these inputs, today's chip accounting could not rule
out a hidden [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run, let alone one at
[1e+24 FLOP](numbers.md#phys-miri-strict). These are calculations on ledger inputs, not
measurements, and the crossing years below are trend extrapolations. This is the most consequential
result in the chapter, and its weakest input is the size of the untraced pool, which is an assumed
order of magnitude, not a measurement; the smuggled stock is the better measured of the two. E22 is no evidence either way on this. Its envelope is an upper bound on what
supply could make, so it could never have put the pool below the floor, and a test that cannot fail
is not evidence
([C8](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool)).
It shows only that the estimates are consistent with supply, which it could not have shown
otherwise: the 95th percentile of compute smuggled into China through 2025 is
[8.9%](numbers.md#e22-smuggled-share-of-allied) of allied sales in 2024 and 2025, and the room the
envelope leaves for undeclared Chinese domestic output is
[3,549](numbers.md#e22-china-slack-over-floor) times the bound floor for a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause. Only a count of the pool, or a
sourced estimate of the smuggled stock whose upper end lies below the floor, could refute the pool's
multiple.

**The floor has a time axis, and the protocol moves it.** Rahman's longest sensible run is set by
how fast hardware, software and investment grow. A pause slows them, so a covert run can rationally
last longer, which lowers the chip floor by a factor of [5.3](numbers.md#phys-pause-floor-factor).
The regime's own success makes hiding easier. Algorithms lower the floor further for a fixed
capability: at MIRI's assumed [3](numbers.md#phys-algo-miri) times a year, the chip floor of a
capability that takes [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) today, at a pause's run
length, falls to MIRI's
[16 H100e](numbers.md#phys-miri-cluster-cap) cap in about [5 years](numbers.md#phys-years-floor-to-cap)
on the estimated floor, and sooner on the bound [@scher2025agreement]. Gundlach et al.'s scale
dependence would make that slower at small scale [@gundlach2025origin]: at their slow rate E8 finds
[13.2 years](numbers.md#e8-years-to-cap-slow). E1 cannot say which rate holds. MIRI's cap is less
tight than the estimate makes it look. At the reference utilisation and the BF16 peak, one cluster at
that cap ([16 H100e](numbers.md#phys-miri-cluster-cap)) needs
[5.0 years](numbers.md#phys-miri-cap-years-strict) for [1e+24 FLOP](numbers.md#phys-miri-strict)
and does [4.0e+23 FLOP](numbers.md#phys-miri-cap-pause-flop) over a pause's two-year run. At the
bound it needs [1.0 years](numbers.md#e8-cap-years-1e24-bound), inside a pause's run length, so the
cap alone does not stop such a run.

**Hardware lowers the energy floor on a known schedule.** At the estimated CMOS ceiling, before any
overhead, the chips would spend [96 MWh](numbers.md#phys-floor-energy-1e26-cmos) on
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) at FP16, against today's [130,000 MWh](numbers.md#phys-floor-energy-1e26) at the facility (P2).

**The steelman for facility detection.** The evidence is not all one way, and the case for
facilities is strongest at the frontier.

- Denial raises the footprint. Huawei's Horinger site supports
  [40%](numbers.md#phys-horinger-relative) of the compute per unit of power of leading US sites
  [@cottier2026horinger], so a party cut off from leading-edge chips needs more power and more
  buildings for the same compute.
- Distribution is costly at scale: [21%](numbers.md#phys-rahman-1e26-eff) of compute survives at
  [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) [@rahman2026], and decentralised runs trail the frontier by
  [1,000](numbers.md#phys-decentral-gap)-fold [@sevilla2025decentralized].
- Frontier runs still need gigawatt sites. The largest 2030 runs are projected at
  [4 GW](numbers.md#phys-largest-run-2030-low) to [16 GW](numbers.md#phys-largest-run-2030-high)
  [@you2025], and leading supercomputers' power needs have doubled each year (a factor of
  [2.0](numbers.md#phys-supercomputer-power-growth) a year) [@pilz2025supercomputers]. Sites like
  Colossus, at [300 MW](numbers.md#phys-colossus-2025-power) in March 2025
  [@pilz2025supercomputers], are built in public view.
- Disguised covert sites are judged to be limited to tens of megawatts, and AI 2040's authors give a
  single small covert site a [20%](numbers.md#phys-halstead-10mw-3y) chance of detection by year
  three and a single gigawatt-class site [40%](numbers.md#phys-halstead-1gw-3y), figures they label
  intuition-based [@halstead-ai2040].
- Very decentralised networks need many accomplices, which personnel channels can reach
  [@baker2025verifying].
- The nuclear record shows energy signatures being read and hidden. IAEA inspectors in Iraq noted
  that Tarmiya's "huge electrical load" did not fit its declared use [@thorne-1992], and Iraq had
  buried power lines to hide it [@albright-2002].

The conclusion the steelman supports is narrower than the memo's. Facility channels bound the
largest, undistributed programme, which matters at and beyond the frontier. They do not police any
threshold at or below about [1e+26 FLOP](numbers.md#phys-rahman-1e26-local), where the protocol's
caps sit. E8 narrows even the first part. A [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run on
one site over today's run length falls below the satellite line by
[2029](numbers.md#e8-cross-sat-1e26-now) ([2026](numbers.md#e8-cross-sat-1e26-now-p05) to
[2032](numbers.md#e8-cross-sat-1e26-now-p95)) as chips gain efficiency, and full denial delays a
power channel's crossing by only [3.1 years](numbers.md#e8-denial-delay-years). Over a pause's run
length the same run on one site draws at least the satellite limit in
[19%](numbers.md#e8-concentrated-1e26-pause-seen) of draws, and
[60%](numbers.md#e8-concentrated-1e26-pause-seen-denied) for a denied party. Thermal infrared's
margin over it is [3.3](numbers.md#e8-thermal-margin-1e26-now) already, a lower bound.

**Power is not a chokepoint.** China added [434 GW](numbers.md#phys-china-additions) of solar and
wind capacity in 2025 [@shaw2026chinasolar], [27](numbers.md#phys-china-over-2030-run) times the
high projection for the largest single 2030 run (nameplate capacity against draw, so the true ratio
is smaller, but not small). US grid connection is slow, a median of
[61 months](numbers.md#phys-us-interconnect-months) from request to operation [@rand2026queued]. That is a rate limit in one country, not a lever over all of them. For scale, all the AI chips sold
in 2025 have a summed maximum power of [7.5 GW](numbers.md#phys-chip-tdp-2025), chips alone
[@epoch2026chipsales].

**An old lesson about accounting.** Nuclear safeguards learned that material balance accounting
fails when throughput is large relative to measurement accuracy: "if sigma_MUF is large ... then
the probability of detection of diversion into MUF is low" [@iaea-glossary-2022]. Chip accounting
over a flow of [13,600,000 H100e](numbers.md#phys-chips-sold-2025) a year, with outside estimates
that disagree fourfold, is in that regime when the quantity to detect is a few hundred to a few
thousand chips.

### What the survey changed from the memo

The memo said detection "works while the floor sits above what satellites, grids and supply-chain
accounting can see". That treats three channels as seeing one floor. They do not. Satellites and
grids see sites, and distribution drives the per-site floor down to one node, two to three orders of
magnitude below their limits. Thermal infrared did not see a [126 MW](numbers.md#phys-jing-cluster-power) cluster. Water is optional.
Of the channels modelled, only chip accounting sees the aggregate, and on today's inputs its
resolution is coarser than the aggregate floor for any threshold the protocol would set. A
distributed run's traffic and purchases are aggregate signatures too, unmodelled here.

The memo's belief that the floor "as a defined, computed quantity may be new" fails in substance.
Koopmanschap and Barten define an "enforcement breaking point", the threshold at which a policy
stops working, and trace detectability against facility size, with about [10 MW](numbers.md#phys-sat-reliable) as the
line for reliable satellite detection [@koopmanschap2026gpu]. Scher and Thiergart argue "Track AI Chips, Not
Data Centers" [@scher2025]. MIRI's draft agreement caps unmonitored clusters at
[16 H100e](numbers.md#phys-miri-cluster-cap) and enforces it through chips [@scher2025agreement]. Rahman computes the cheapest distributed
configuration that evades registration thresholds [@rahman2026]. Halstead and Larsen give per-site
detection chances by size [@halstead-ai2040]. Sastry et al. flagged the distributed-training caveat
in 2024 [@sastry2024compute]. The independent prior-art search (level 1) then found the floor
itself: the formula as an aggregate floor in chips with a time axis, the untraced pool entered
against it, and the conclusion that the pool must be shrunk rather than found are in the
hardwired-pause working paper [@fithian2026hardwired]. That chip accounting must resolve less than
the floor is the IAEA's lesson on material unaccounted for [@iaea-glossary-2022]. P4 is
**an application of prior work, with calculations**
([C8](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool)).
Level 1 found it extends prior work narrowly; the fresh reviewer showed that none of its parts can
fail on an experiment, since the bound is a sum and the pool's multiple divides an assumed pool, so
it is labelled as calculations. What remains ours is three computations others could easily have
run: the floor as a bound, at the
lowest precision and full utilisation, where the hardwired-pause threshold is an estimate; each
facility channel's margin over the floor and the year it crosses one; and the pool's multiple of
the floor, which divides an assumed pool, with E5's discovery rate, a central estimate under a
transfer, behind the conclusion that it must be shrunk. The time
axis and the aggregate form, which this chapter first counted as its own, are not. "Not found" for
what remains is a statement about our search and level 1's.

### What it means for the protocol (a candidate)

- **Facility channels** (satellites, grid paperwork) confirm and size declared sites and catch the
  construction of very large undeclared ones. They cannot enforce a compute threshold at or below
  about [1e+26 FLOP](numbers.md#phys-rahman-1e26-local), and the protocol should not claim they do.
  On E8's crossing years they lose even a concentrated run of that size within a few years.
- **On-site metering** at declared sites verifies the kind of work against a sealed declaration
  (training against inference). It cannot bound the amount; pair it with re-execution of declared
  work and with chip-hour accounting.
- **Chip accounting** is the only aggregate channel modelled, so the compute half of the protocol
  stands on it. Its resolution must be finer than the floor for the threshold it protects, taken as
  a bound, at the longest run length an adversary will accept, which under a pause is
  [24 months](numbers.md#phys-rahman-run-pause) or more, not [4.5 months](numbers.md#phys-rahman-run-now).
  Today the untraced pool would have to shrink [1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold
  for it to resolve a [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause. Until the
  pool is closed, D3 must count it as a covert reserve in every party's breakout time, as the
  hardwired-pause working group does [@fithian2026hardwired]. At the historical discovery rate,
  transferred from nuclear and biological programmes, the pool's detection time is a median of
  [32 years](numbers.md#e5-td-pool-years), and E5's Weibull fit gives [24 years](numbers.md#e5-td-weibull-years) for a path only the
  historical channels see, as the pool's is. That is decades either way, a central estimate under
  the transfer, not a bound: the protocol must shrink the pool, not hope to find what it hides.
- **Thresholds** must fall with algorithmic progress (the floor for a fixed capability falls
  about threefold a year on MIRI's assumption, a rate E1 cannot identify on public data) and with
  hardware efficiency, and be set for the run lengths a pause makes rational, or in chip-time,
  which holds whatever run length the adversary picks.
- **Cost to useful AI.** Registering chips costs legitimate users little. A low cap on
  unmonitored clusters, of the order MIRI proposes, costs more: it reaches research labs and small
  firms. The floor says how low such a cap must go for chip accounting to matter.

### What would test it

- **E8 (the footprint floor against detection limits)** has run. From the inputs in this chapter it
  computes N_min, E_min and average power for C from
  [1e+22 FLOP](numbers.md#phys-miri-monitored) to [1e+27 FLOP](numbers.md#phys-e8-c-high), T from one
  month to the pause run length, and each year ahead under the measured hardware rate and a range of
  algorithmic rates (Gundlach's slow case to MIRI's threefold), with a Monte Carlo over utilisation,
  power per chip, satellite accuracy, the untraced pool, the smuggling interval and the denial
  multiplier. E8 computes; it does not test. Its inputs are ledger values, so it cannot support C8
  experimentally. C8(a), the floor as a bound, is a sum that cannot fail, and C8(c), the pool's
  multiple, divides an assumed pool by the floor. What E8 gives is arithmetic: chip accounting must
  resolve less than the bound, which needs the assumed pool to shrink
  [1,200](numbers.md#e8-pool-shrink-1e26-pause)-fold for a
  [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause, and the assumed pool, and the
  smuggled stock alone, exceed the floor hundreds of times over (the figures are under "Evidence for
  and against"). Its facility crossing years, trend extrapolations, are given there too.
- **The falsifier this chapter first proposed is cut.** It said "only chip accounting sees the
  aggregate floor" fails if any facility channel's margin is below one for a distributed run at
  [1e+25 FLOP](numbers.md#phys-rahman-1e25-target). That cannot fail: the per-site floor is one node
  whatever the run's size, so every facility channel's margin exceeds one by definition, and E8's
  distributed margins are definitional, not evidence. The red team cut it
  ([C8](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool)).
  What could refute the floor's role now: a published crossing-year analysis of satellite or grid
  detection; E13 measuring energy per operation below the e_min the bound uses; or a count of the
  untraced pool, or a sourced estimate of the smuggled stock, whose upper end lies below the floor.
  E22 cannot do this: its envelope is an upper bound on supply, so it can show only that the
  estimates are consistent with supply, never that the pool is small (under "Evidence for and
  against"). A model of a distributed run's traffic or purchases would test the word "only".
- **E5 (multi-channel verification)** has run. It combines the channels as the evader sees them,
  by subgoal and not as a product of independent misses, as Baker et al. argue a regime's detection
  is roughly that of its weakest subgoal [@baker2025verifying]. Over a one-year breakout time the
  evader's best watched path, the untraced pool, is missed with probability
  [91%](numbers.md#e5-pmiss-max-1y); cloud and distillation, which no physical channel watches, are
  missed with certainty. The fitted discovery rate of covert programmes,
  [0.094/yr](numbers.md#e5-hazard), comes from nuclear and biological programmes all found or
  disclosed in the end, so within that record it overstates a careful evader's rate; it is counted
  from a programme's start, and nothing measures how it transfers to an AI breakout. E5's Weibull
  fit gives a shorter time than the constant rate, [24 years](numbers.md#e5-td-weibull-years) against
  [32 years](numbers.md#e5-td-hist-years), so the detection times built on it are central estimates
  under that transfer, not lower bounds. The tamper test on power traces has moved to E13, which shares its harness, and has
  not run.
- **P-diloco (from P3), now E14,** supplies E8's tax curve for distributed adversaries. Not run.

## What this perspective contributes to the line

Four quantities from this chapter belong in the protocol. Energy, heat, water and facility size are
not among them: they corroborate, for the largest programmes, but they cannot enforce a threshold.

1. **Held compute in chip-time** (H100e-seconds at a reference precision), summed over everything a
   party holds. Measured through the chip registry, location verification and chip sampling; it is
   the holdings term of breakout time (D3), and the protocol triggers when a party's breakout time
   falls below the margin on its response time (D4). Weakest point: the registry starts with a hole
   ([1,000,000 chips](numbers.md#phys-chips-unaccounted) untraced, plus smuggled compute) larger
   than the aggregate floor of a [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run (estimated at
   [21,000 H100e](numbers.md#phys-floor-chips-1e26-now) today and
   [4,000 H100e](numbers.md#phys-floor-chips-1e26-pause) under a pause, with a bound of
   [800 H100e](numbers.md#formal-floor-bound-1e26-pause) under a pause).
2. **Training compute of each lineage** (C_train, including post-training, rollouts, teacher
   generation and synthetic data). Declared, sealed and sampled; it triggers evaluation at
   thresholds that fall with algorithmic progress. Weakest point: inference and algorithms
   substitute for it, and a cap leaks at a rate that E1 cannot identify on public data.
3. **Workload type at declared sites**, from power traces. It verifies that declared capacity does
   what its declaration says. Weakest point: it needs a declared site and a trusted meter, and it
   bounds the amount of hidden work only weakly (up to [1.16](numbers.md#phys-beta-worst) times
   declared capacity without re-execution).
4. **Inference capacity as copies times speed**, bounded from an inventory by held compute (P1) and
   memory bandwidth per copy (P3). Not a limit but a measurement, feeding the resource matching of
   D1 and the advantages of F1. Weakest point: it cannot be limited without limiting useful AI, and
   frontier-level capability reaches a single consumer GPU within
   [6 months](numbers.md#phys-consumer-lag-low) to [12 months](numbers.md#phys-consumer-lag-high)
   [@somala2025consumergpu], so it is the next increment, not running, that the line can govern.

None of this has been tested against a real adversary. The floors are arithmetic on measured and
vendor inputs. The estimates assume a utilisation; the bound assumes none, but holds only while FP8
is the lowest precision a run can train at, and its run length T is an assumption about the
adversary. The untraced pool is an assumed order of magnitude. The detection limits come from small
samples and, for power metering, from simulation. The protocol built on them is a design.
