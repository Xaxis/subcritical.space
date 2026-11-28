# The physical and energetic perspective

Superintelligence is a computation on chips that draw power, hold state and move bytes, inputs a verifier can check without taking a party's word. A holding is inside the line when its breakout time (D3) is short against detection plus response (D4); P1 is its holdings term, and P2 to P4 bound what a covert programme must leave visible.

## P1. The compute budget

**Definition.** Training compute counts useful operations, at a stated precision, on every chip that shapes a model's weights, rollouts, distillation and synthetic data included. Label: prior work [@carlsmith2020; @sandberg2008; @davidson2023compute; @epoch2026chipsales; @you2026chipowners; @epoch2025datacentershub; @sastry2024compute; @heim2024thresholds; @scher2025agreement].

**Measurement.** An H100's FP8 peak is [2](../research/numbers.md#phys-fp8-over-bf16) times its BF16 peak [@nvidia-h100], so a cap must count chip-time at a reference precision. Utilisation, unseen from outside, varies [2.1](../research/numbers.md#phys-util-spread)-fold [@jaghouar2024intellect1; @pope2022].

**Evidence for and against.** Compute is credited with most language-model gains [@ho2024algorithmic] but only [18%](../research/numbers.md#e1-compute-share-subset-min) to [63%](../research/numbers.md#e1-compute-share-subset-max) of capability-index growth across E1's samples [@epoch2026aimodels; @epoch2025eci]. Compute for a fixed loss halves every [8.4 months](../research/numbers.md#phys-algo-halving) [@ho2024algorithmic], so a fixed cap leaks, slowly far below the frontier if gains need scale [@gundlach2025origin], which E1 could not confirm. The 2025 chip flow could run at most [140,000,000](../research/numbers.md#phys-flow-2025-copies) PaLM-sized copies, an upper bound that mixes two batch regimes [@pope2022]: P1 binds training, not running.

**Open questions.** D1's compute, how far inference substitutes for training, and copy counts are untested.

## P2. Energy per useful operation, and the headroom to physics

**Definition.** e is facility-metered energy per useful operation: chip energy per peak operation, times overheads, over utilisation. Its headroom has two limits, the CMOS ceiling and Landauer's bound, kT ln 2 per erased bit, which binds only irreversible operations. Label: prior work [@ho2023; @koomey2011; @landauer1961; @carlsmith2020; @davidson2025three].

**Measurement.** Power per chip varies [1.9](../research/numbers.md#phys-power-per-chip-spread)-fold between sources [@epoch-datacenters-2026; @scher2025; @sastry2024compute], so energy alone cannot certify compute.

**Evidence for and against.** CMOS binds first, [205](../research/numbers.md#phys-cmos-headroom) times above the H100 [@ho2023], a headroom used up in [16 years](../research/numbers.md#phys-years-to-cmos-fast) to [18 years](../research/numbers.md#phys-years-to-cmos-slow) at trend [@pilz2025supercomputers; @you2025]. Reversible logic's reported gains are vendor claims [@hulick2025; @genkina2025].

**Open questions.** Our chip-side measurement of e has not run.

## P3. Memory and bandwidth

**Definition.** Memory bandwidth per copy, B_copy, caps serial speed at small batch at v <= B_copy / (N * z) for N parameters of z bytes [@pope2022]; interconnect bounds how far training spreads. Label: prior work [@gholami2024; @hobbhahn2023; @erdil2024datamovement; @douillard2023diloco; @douillard2025streaming; @sevilla2025decentralized; @krys2025distributed].

**Measurement.** Both are fixed at manufacture; export rules already use bandwidth density [@bis2024hbm].

**Evidence for and against.** PaLM's measured latency was [4.1](../research/numbers.md#phys-pope-over-bound) times its memory floor, so the cap held [@pope2022]. Streaming DiLoCo keeps [95%](../research/numbers.md#phys-streaming-util) utilisation over links of a few Gbit/s [@douillard2025streaming], so training no longer needs one site, though at [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) a distributed run keeps only [21%](../research/numbers.md#phys-rahman-1e26-eff) of its compute [@rahman2026]; the loosening matters below about [1e+25 FLOP](../research/numbers.md#phys-rahman-1e25-target), where caps sit.

**Open questions.** The speed bound and the distribution tax are untested here.

## P4. The footprint and its floor

**Definition.** The floor is the smallest footprint that could produce C useful operations within time T: per site, one node of [29 kW](../research/numbers.md#phys-node-power); in aggregate, N_min = C / (r * u * T) H100-equivalents (H100e), a bound when r is the FP8 peak, the lowest precision trained at scale [@deepseek2024v3], and u is full utilisation; T, the longest sensible run [@rahman2026], is an assumption a racing party need not share. A channel can enforce a threshold only where its detection limit is below the floor it sees. Label: prior work, applied, with calculations. The aggregate floor with a time axis, the pool counted against it and the need to shrink it are in [@fithian2026hardwired]; limits by facility size in [@koopmanschap2026gpu]; chip tracking in [@scher2025; @scher2025agreement]; distributed evasion in [@rahman2026]; the resolution rule in IAEA material accounting [@iaea-glossary-2022]. Ours are calculations others could easily have run: the bound, each channel's crossing year and the pool's multiple.

**Measurement.** A satellite classifier found every facility above [10 MW](../research/numbers.md#phys-sat-reliable) and none below, in a small sample, on Koopmanschap and Barten's reading [@clymer2025datacenter; @koopmanschap2026gpu]. Thermal infrared saw no warming over a [126 MW](../research/numbers.md#phys-jing-cluster-power) cluster [@jing2026]. Metering on simulated power tells the kind of work [@kimpson2026dcpower], not the amount (abstract only) [@kimpson2026b]. Of the channels modelled, only chip accounting sees the aggregate, and it leaves an assumed [1,000,000 chips](../research/numbers.md#phys-chips-unaccounted) untraced [@koopmanschap2026gpu].

**Evidence for and against.** Experiment E8 computes on ledger inputs; it does not test. For [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) over the [24 months](../research/numbers.md#phys-rahman-run-pause) a pause makes rational, the bound is [800 H100e](../research/numbers.md#e8-floor-1e26-pause-bound) ([1,600 H100e](../research/numbers.md#formal-floor-bound-1e26-pause-bf16) at BF16). The assumed pool is a median [340](../research/numbers.md#e8-pool-over-floor-1e26-pause-p50) times the BF16 floor, a point, not a range, and one country's smuggled compute, with a published interval, [230](../research/numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times; chip accounting would resolve the run only with the pool [1,200](../research/numbers.md#e8-pool-shrink-1e26-pause)-fold smaller. Supply cannot shrink it: E22, an upper bound, leaves room for undeclared Chinese output of [3,549](../research/numbers.md#e22-china-slack-over-floor) times the bound and is no evidence either way. Transferred from past weapons programmes, the pool's detection time is a median [32 years](../research/numbers.md#e5-td-pool-years), or [24 years](../research/numbers.md#e5-td-weibull-years) on a Weibull fit: a central estimate, not a bound, and not for a fast run, since it assumes detection does not rise with a breakout's speed. On trend, even a concentrated [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run falls below the satellite line by [2029](../research/numbers.md#e8-cross-sat-1e26-now), and denial [@cottier2026horinger] delays that by only [3.1 years](../research/numbers.md#e8-denial-delay-years). Facility margins for a distributed run are definitional, since one node sits below every limit.

**Open questions.** The pool's size is assumed, and only a count could lower it. Traffic and purchases are unmodelled, and no model ties detection to footprint.

## What this perspective gives the line

Of the channels modelled, only chip accounting sees the aggregate floor: the compute half of the protocol stands on chip-time, and breakout time must count the untraced pool as a covert reserve until it shrinks below the floor. Facility, energy and heat channels corroborate the largest programmes but cannot enforce a threshold.
