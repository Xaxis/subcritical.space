# Experiments

Each experiment is a script in the program's public code, deterministic given a recorded seed. It
fetches public data or models from a named source, or reads a case table with a source for every
row, and its results enter the paper only through the model's ledger. Fourteen have run, E4 and E21
in part; E8 and E11 only compute from ledger inputs. None has faced a real adversary.

Table: The experiments by theme, and whether each has run {#tab:experiments}

| Theme | Run | Not run |
|---|---|---|
| Compute and capability | E1, E2, E18, E21 (public part) | E3, E10, E12, E15, E20, E21 (live part) |
| Loops and closure | E4 (c, a), E9, E11 | E4 (b, d, e), E7, E16, E17, E19 |
| Detection and response | E5, E24 | E13 |
| Supply and the footprint | E8, E22, E23 | E14 |
| Games and the licence clock | E6, E25 | none |

## What has run

**E1** fits Epoch's capabilities index on training compute and date [@epoch2026aimodels;
@epoch2025eci] and reruns Ho et al.'s fit [@ho2024algorithmiccode]. Across six samples of the same
models the algorithmic rate runs from [2.6](../research/numbers.md#e1-algo-annual-subset-min) to
[1,512](../research/numbers.md#e1-algo-annual-subset-max) a year in compute-equivalent. Public data
do not identify the drift breakout time needs, so no interval for it can be tabulated in advance
(C2(a)).

**E18** tests a capped party's leak time against Epoch's open and closed models
[@edwards2026openclosed]. Its stated target, the open-closed lag, has
[0 days](../research/numbers.md#e18-oc-evaluable-days) on which both models compared have a public
compute estimate, so C2(c) cannot be tested on public data. In a substitute backtest, models at or
below a frontier record's compute matched it after [0.48 years](../research/numbers.md#e18-bt-h0-lo)
to [1.52 years](../research/numbers.md#e18-bt-h0-hi), where the expression predicts no delay: the
leak comes in jumps that no constant rate follows.

**E2** refits METR's time horizons [@metr2026thdata]: the frontier 50% horizon doubles every
[129 days](../research/numbers.md#e2-doubling-p50), at a stable ratio to the 80% horizon. Timing one
person on single tasks, it informs only C12's grade for long-horizon autonomy.

**E21** estimates C10's crossover budget t* on RE-Bench [@wijk2024rebench], Cybench
[@zhang2024cybench] and MLE-bench [@chan2024mlebench]. No battery compares with an organisation, so
C10(b) is untested; on MLE-bench the verdict depends on the rank named, the median entrant beaten in
[71.1%](../research/numbers.md#e21-mle-median-best) of competitions and the gold threshold in
[25.8%](../research/numbers.md#e21-mle-gold-best). t* rises with release date but stops at each
battery's ceiling, [32.0 h](../research/numbers.md#e21-rebench-tstar-best) on RE-Bench and
[24.9 h](../research/numbers.md#e21-cyber-ceiling-h) on Cybench.

**E4** asks whether a staged estimator can tell on which side of 1 a research loop's gain lies (D2,
C4). At the only calibrated proxy, the NanoGPT speedrun's record-to-record spread, the 90% interval
covers r [82%](../research/numbers.md#e4-cov-n5) of the time after
[5 rounds](../research/numbers.md#claim-d2-rounds) per budget, and the trigger on K fires in
[88%](../research/numbers.md#e4-k-fa-n5) of runs below the margin and only
[2%](../research/numbers.md#e4-k-fire-gap-n5) more often at r's 95th percentile. The trigger fails
at that proxy and is untested at real round noise. The speedrun's own returns are not identified
[@moddednanogpt; @epoch2026speedrundata; @shetty2026metrnanogpt].

**E9** refits returns to research with compute's share of research input free [@ho2025experiments;
@besiroglu2024returns; @bloom2020ideas]; no data identify that share. Counting compute's growth,
which Part I's loop gains omit, the language-model gain at fixed compute and a share of
[0.67](../research/numbers.md#dyn-research-compute-share) is
[0.25](../research/numbers.md#e9-lm-k-fixed), above 1 only for shares below about
[0.26](../research/numbers.md#e9-lm-share-crit).

**E11** puts C6's certificate on Part I's loop graph, with Epoch's index for the edge between
parties [@epoch2025eci]. Of [10 entries](../research/numbers.md#e11-entries),
[5 entries](../research/numbers.md#e11-entries-unbounded) have no bound, so no certificate can issue
on today's evidence.

**E5** computes detection times per path (C3) from sourced rates for chip sampling
[@shavit2023chinchilla], metering [@kimpson2026dcpower] and diversion [@juniewicz2026smuggling], and
a discovery rate fitted to [16 cases](../research/numbers.md#e5-cases) of covert weapons programmes.
The declared path takes [39.0 days](../research/numbers.md#e5-td-declared-days), a design figure.
Undeclared paths take decades, as central estimates under a transfer from weapons programmes, not
bounds: [24 years](../research/numbers.md#e5-td-weibull-years) under the Weibull fit beside
[32 years](../research/numbers.md#e5-td-hist-years) at a constant rate, and for one site
[0 years](../research/numbers.md#e5-td-site-now-years-lo) to
[43 years](../research/numbers.md#e5-td-site-now-years-hi), or
[0.0 years](../research/numbers.md#e5-td-site-satopt-years) with satellites working as in the one
sample. Cloud rental and distillation have no channel. The hazard is assumed independent of a
breakout's speed, so these times do not hold for a fast covert run.

**E24** compiles the time from a confirmed finding to an effective response in arms control
[@iaea-gc37-1084; @bunn2005npt]. Of [8 findings](../research/numbers.md#e24-halt-findings) made
inside a treaty, [25%](../research/numbers.md#e24-halt-share-never) were not followed by a halt
within what the sources cover, one of them censored, so the 95th percentile of D4's response time is
not reached within follow-up. The fastest halt took
[64 days](../research/numbers.md#e24-halt-min-days); the fastest exit,
[31 days](../research/numbers.md#e24-exit-min-days).

**E8** computes the smallest footprint of a training run (C8) from sourced ledger values
[@rahman2026; @koopmanschap2026gpu]. The bound for a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run under a pause is
[800 H100e](../research/numbers.md#e8-floor-1e26-pause-bound). At an assumed untraced pool of
[1,000,000 chips](../research/numbers.md#phys-chips-unaccounted), the pool is
[1,200](../research/numbers.md#e8-pool-shrink-1e26-pause) times that bound, so chip accounting
cannot see such a run until the pool shrinks.

**E22** bounds from sourced capacities what three kinds of party could have added in 2024 and 2025;
all [19 observations](../research/numbers.md#e22-inside) of Epoch's sales [@epoch2026chipsales] and
one maker's output fall inside. It puts the supply part of phi, the fall in breakout time between
checks, at [2.5](../research/numbers.md#e22-phi-member-year) a year for the fleet, which the line
and C7's share must carry beyond the margin. An upper bound cannot show the pool closing.

**E23** asks whether a ranking of chokepoints from data public at the end of 2022 ordered the
erosion to November 2026 (O3). Its [9 stages](../research/numbers.md#e23-stages) give r_s
[0.28](../research/numbers.md#e23-rho), one-sided p [0.23](../research/numbers.md#e23-p), and a rank
test would need [85 stages](../research/numbers.md#e23-n-needed), so the ranking cannot be tested.

**E6** rebuilds six published race and agreement models [@armstrong2016racing;
@emeryxu2024uncertainty; @fudenberg2026cooperating; @gan2026clock; @nordhaus2015climate;
@barrett2012climate] and adds detection, response and C7's coalition game, on illustrative payoffs.
They reproduce, except that Emery-Xu, Park and Trager's Proposition 2 is not a best response in our
reimplementation, which an independent check must confirm or overturn. A coalition that absorbs
drift during its run succeeds per attempt with
[0.076](../research/numbers.md#e6-staged-pi-line-inrun), above the tolerance beta of
[5%](../research/numbers.md#def-prevent-beta), this work's choice, so C7's share must count in-run
drift. Disclosing only compliance raised disaster risk over no information in
[100%](../research/numbers.md#e6-o2-compliance-over-none) of cells.

**E25** runs C9's header verifier on Bitcoin's chain,
[977,000 headers](../research/numbers.md#e25-headers), with a log whose anchoring is modelled
[@todd2016opentimestamps; @laurie2013ct]. The powered-time counter bounds a licence's use; the best
rule is a budget of [1.099](../research/numbers.md#e25-budget-least) times the nominal licence plus
the height expiry, and a rate floor only adds false stops. Withheld log leaves are asserted, not
measured, and no hardware prototype exists.

## What has not run

E3 would give C5 its miss and false-alarm rates on model organisms [@redwood2024mathpwdlock;
@aisi2025auditingrepo]. E4(b) would measure real round noise, and E4(d) and (e) closure gate by gate
(C11). E10 [@biderman2023pythia] and E15 would test whether inference, distillation and algorithms
substitute for compute; E13 and E14 [@kimpson2026dcpower; @douillard2023diloco], C8's energy and
distribution inputs. E7, E12, E16, E17, E19 and E20 answer Part I's open questions, from continual
learning to replication. E21's live part, with teams, is blocked. No experiment measures an
AI-specific detection channel against a resourced
adversary.
