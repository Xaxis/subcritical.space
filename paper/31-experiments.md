# Experiments

Each experiment is one script in the program's public code, deterministic given a seed fixed in the
script and recorded with its results. It fetches real public data or models from a source it names,
or reads a case table compiled by hand with a source for every row, and writes its results to a
file. Those results enter the paper only through the model's ledger, like every other number.
Fourteen experiments have run, E4 in part, on the CPU and public data, and results are as corrected
after the red team. Each level-3 verdict quoted is the verification record's.

Table: The experiments, whether each has run, and the claims each bears on {#tab:experiments}

| Experiment | Question | Status | Claims |
|---|---|---|---|
| E1 | Capability against training compute | Run | C2, C10, C12 |
| E2 | Growth of agents' time horizons | Run | C10, C11, C12 |
| E3 | Hidden capability in model organisms | Not run | C5 |
| E4 | Loop gain: simulated, historical, staged | (c), (a) run; (b), (d), (e) not run | C4, C11, C2 |
| E5 | Detection per path; covert programmes' discovery | Run | C3, C1, C8, C12 |
| E6 | Race and coalition games with a regime | Run | C7, C1, C6 |
| E7 | Update compute of continual learning | Not run | C12 |
| E8 | Footprint floor against channel limits | Run | C8, C3 |
| E9 | Returns to research, compute's share free | Run | C4, C6 |
| E10 | Training-inference exchange rate | Not run | C2, C6, C11, C12 |
| E11 | Coupled-gain certificate | Run | C6 |
| E12 | Serving speed and copies | Not run | C10 |
| E13 | Energy per operation; power traces | Not run | C8, C3 |
| E14 | Tax of training over slow links | Not run | C8 |
| E15 | Scale dependence of algorithmic gains | Not run | C2, C12 |
| E16 | Verifier substitution in self-training | Not run | C11 |
| E17 | Transfer from narrow training | Not run | C11, C12 |
| E18 | Cap leak at fixed compute | Run | C2, C1, C12 |
| E19 | Replication reproduction number | Not run | C11, C12 |
| E20 | Speed, copies and quality at matched budget | Not run | C10 |
| E21 | Matched-budget team battery, public part | Run | C10 |
| E22 | Supply envelope backtest | Run | C7, C1, C2, C8 |
| E23 | Durability of chokepoints, backtested | Run | none; Part I's O3 |
| E24 | Time from finding to response | Run | C1, C7 |
| E25 | Licence clock and log | Run | C9 |

## Compute and capability

**E1** asks how capability grows with training compute and how fast algorithms add to it. It joins
Epoch's model data to its capabilities index [@epoch2026aimodels; @epoch2025eci] and reruns Ho et
al.'s fit [@ho2024algorithmiccode]. On all [105 models](../research/numbers.md#e1-models), compute
explains [36%](../research/numbers.md#e1-compute-share) of growth on the index, and the rest moves
with date at about [17](../research/numbers.md#e1-algo-annual) times a year in compute-equivalent.
Neither is identified: across six samples of the same models the share runs from
[18%](../research/numbers.md#e1-compute-share-subset-min) to
[63%](../research/numbers.md#e1-compute-share-subset-max) and the rate from
[2.6](../research/numbers.md#e1-algo-annual-subset-min) to
[1,512](../research/numbers.md#e1-algo-annual-subset-max) a year. So no interval tabulated in
advance can hold on public data, and C2(a) is cut.

**E18** asks how soon a party held at a compute cap leaks to the agreed effective compute as
algorithms improve. It evaluates the proofs' leak time (Corollary 2.3) on Part I's ranges and
backtests it on Epoch's record of open and closed models [@edwards2026openclosed]. A model at or
below a then-frontier record's compute matched the record after
[0.48 years](../research/numbers.md#e18-bt-h0-lo) to
[1.52 years](../research/numbers.md#e18-bt-h0-hi), where the expression predicts no delay, and the
[4 catch-ups](../research/numbers.md#e18-bt-events) below a record's compute imply yearly rates from
[1.91](../research/numbers.md#e18-bt-gamma-lo) to [1,125](../research/numbers.md#e18-bt-gamma-hi):
the leak comes in jumps that no constant rate follows. The open-closed lag cannot be predicted at
all: on [0 days](../research/numbers.md#e18-oc-evaluable-days) of Epoch's window do both models
compared have a public compute estimate. The verdict on C2 is against: (a) cut, (c) cut on E18, (b)
not shown. C2 is downgraded to an accounting frame.

**E2** refits METR's published time horizons [@metr2026thdata]. The frontier 50% horizon doubles
every [129 days](../research/numbers.md#e2-doubling-p50), at a stable ratio to the 80% horizon. It
measures the clock that C12 recasts long-horizon autonomy as, and contradicts no pair of its
ranking. It tests neither empirical part of C10, since its comparison is one person's time on single
tasks.

**E21** asks where AI systems stand against human comparisons at matched time, and whether the
crossover budget t* rises without saturating (C10). It uses RE-Bench
[@wijk2024rebench], Cybench's contest solve times [@zhang2024cybench], MLE-bench against Kaggle
entrants [@chan2024mlebench] and forecasting rounds [@karger2025forecastbench;
@forecastbench2026board; @metaculus2026futureeval]. No battery compares with an organisation. On
MLE-bench the verdict flips between the median and the gold-medal entrant in
[45.3%](../research/numbers.md#e21-mle-flip-best) of competitions. t* rises with release date but
stops at each battery's ceiling: on RE-Bench the best model is at the score's cap at
[32 h](../research/numbers.md#cog-rebench-budget-long) in
[99.4%](../research/numbers.md#e21-rebench-cap-32h) of resamples, and Cybench cannot measure t*
above [24.9 h](../research/numbers.md#e21-cyber-ceiling-h). The verdict is against C10(b) on the one
analogue, contest entrants, and C10(c) holds only until a battery saturates.

## Loops

**E4** asks whether a staged estimator can tell on which side of 1 a research loop's gain lies (D2,
C4). Part (c) simulates the staged test with round noise calibrated on the NanoGPT speedrun, the
only noise calibrated on data. After [5 rounds](../research/numbers.md#claim-d2-rounds) at each
budget the 90% interval covers r [82%](../research/numbers.md#e4-cov-n5) of the time. At the
corrected median of r, below the margin, the trigger on K fires in
[88%](../research/numbers.md#e4-k-fa-n5) of runs, and at the corrected 95th percentile only
[2%](../research/numbers.md#e4-k-fire-gap-n5) more often, within Monte Carlo error. Part (a) reads
the speedrun's records [@moddednanogpt; @epoch2026speedrundata; @shetty2026metrnanogpt]; its returns
are not identified, since stock and contributors move together. The verdict is against, for the
measurement and the trigger alike, and C4 is downgraded to a measurement design.

**E9** refits returns to research with compute's share of research input free, from the data behind
published estimates [@ho2025experiments; @besiroglu2024returns; @bloom2020ideas]. No data identify
that share. Counting compute's growth, which Part I's loop gains leave out, the language-model gain
at fixed compute and a share of [0.67](../research/numbers.md#dyn-research-compute-share) is
[0.25](../research/numbers.md#e9-lm-k-fixed) ([0.42](../research/numbers.md#e9-lm-k-fixed-hi) at the
95th percentile), above 1 only for shares below about
[0.26](../research/numbers.md#e9-lm-share-crit). This bears on C4, C6(c) and D2.

**E11** builds C6's certificate on Part I's loop graph from ledger values, with a bound on the edge
between two parties from Epoch's index [@epoch2025eci]. Of
[10 entries](../research/numbers.md#e11-entries),
[2 entries](../research/numbers.md#e11-entries-measured) have a measured bound and
[5 entries](../research/numbers.md#e11-entries-unbounded) none, so nothing issues. C6(c) holds only
while compute's share stays below [0.689](../research/numbers.md#e11-epsk-flip). The verdict is
against issuing a certificate today.

## Detection and response

**E5** asks how likely an evader is to be missed on its best path (C3), with sourced rates for chip
sampling [@shavit2023chinchilla], power metering [@kimpson2026dcpower] and detection of diversion
[@juniewicz2026smuggling], and a discovery rate fitted to a hand-compiled table of
[16 cases](../research/numbers.md#e5-cases). Cloud rental and distillation, with no sourced channel,
are missed with certainty. Detection takes [39.0 days](../research/numbers.md#e5-td-declared-days)
on the declared path, set by chip sampling, a design figure, against
[31 years](../research/numbers.md#e5-td-site-now-years) for one undeclared site above the satellite
line and [32 years](../research/numbers.md#e5-td-pool-years) for the pool. The discovery rate,
[0.094/yr](../research/numbers.md#e5-hazard), comes from programmes all found in the end, so it is
an upper bound on a careful evader's. On C3 the verdict is supports: (c) measured, (b) only
illustrated. The same figures bear against C1 on covert paths.

**E24** asks how long the arms-control record took from a confirmed finding to an effective
response, compiled case by case from sources [@iaea-gc37-1084; @bunn2005npt]:
[17 findings](../research/numbers.md#e24-findings) on
[8 programmes](../research/numbers.md#e24-programmes). Of
[8 findings](../research/numbers.md#e24-halt-findings) made while the party was in its treaty,
[25%](../research/numbers.md#e24-halt-share-never) were never followed by a halt. Halts took a
Kaplan-Meier median of [1.2 years](../research/numbers.md#e24-halt-km-median-years), against the
violator's fastest exit of [31 days](../research/numbers.md#e24-exit-min-days). The record has no
high quantile of response time, and E24 is part of the verdict against C1.

## Supply and the footprint

**E8** computes the smallest footprint that could still produce a run (C8). It reads only sourced
ledger values [@rahman2026; @koopmanschap2026gpu]. Its bound for a
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run under a pause,
[800 H100e](../research/numbers.md#e8-floor-1e26-pause-bound), agrees with the proof. For chip
accounting to resolve such a run, the untraced pool must shrink
[1,200](../research/numbers.md#e8-pool-shrink-1e26-pause)-fold. The verdict supports C8(a) and (c),
on E8 alone. C8(b), which could not fail, was cut.

**E22** asks the most H100e each of three kinds of party could have added in 2024 and 2025, an upper
bound from sourced capacities, tested against Epoch's sales [@epoch2026chipsales] and outside
estimates of one maker's output. All [19 observations](../research/numbers.md#e22-inside) fall
inside. It bounds the supply part of phi, the fall in breakout time between checks, for the fleet at
[1.65](../research/numbers.md#e22-phi-member-quarter) a quarter and
[2.5](../research/numbers.md#e22-phi-member-year) a year; with drift between checks, Part II's phi
is [2.1](../research/numbers.md#prot-phi-quarter) at each licence renewal and
[6.8](../research/numbers.md#prot-phi-year) a year, a factor C1's line must carry on top of the
margin. The verdict on C7 is against s* without growth between declarations. An upper bound cannot
put the untraced pool below the floor, so E22 is no evidence either way on C8.

**E23** asks whether a ranking of supply chokepoints made from data public at the end of 2022 would
have ordered the erosion seen from 2023 to November 2026, an open question in O3, not a claim. The
[9 stages](../research/numbers.md#e23-stages) ranked match it at rho
[0.28](../research/numbers.md#e23-rho), one-sided p [0.23](../research/numbers.md#e23-p); the
smallest rho the test could call significant is [0.59](../research/numbers.md#e23-rho-critical), and
a rank test would need [85 stages](../research/numbers.md#e23-n-needed). No version of the test can
decide, and ranking stages by durability stays unclaimed.

## Games

**E6** rebuilds six published race and agreement models from their equations and parameters
[@armstrong2016racing; @emeryxu2024uncertainty; @fudenberg2026cooperating; @gan2026clock;
@nordhaus2015climate; @barrett2012climate], and plays C7's coalition game with detection and
response. Its payoffs are illustrative; no party's are measured. The games reproduce, among them
Gan's [32](../research/numbers.md#e6-gan-reproduced) published values, except that Emery-Xu, Park
and Trager's Proposition 2 is not a best response in our reimplementation, a finding an independent
check must confirm or overturn. A coalition that passes the line at launch speed and absorbs drift
during its run succeeds per attempt with [0.076](../research/numbers.md#e6-staged-pi-line-inrun),
above beta of [5%](../research/numbers.md#def-prevent-beta). That met C7's refuter, and (a) now
counts in-run drift. Repeated attempts compound when caught members are re-admitted, which the
record counts against C1. E6 also cut compliance-only disclosure, which raised disaster risk over no
information in [100%](../research/numbers.md#e6-o2-compliance-over-none) of cells. The verdict is
against C7(a) as first stated, now corrected; (b) is illustrated, not measured.

## The licence clock

**E25** drives C9's header verifier with Bitcoin's real chain,
[977,000 headers](../research/numbers.md#e25-headers), and a certificate-transparency log whose
anchoring in the chain is modelled [@todd2016opentimestamps; @laurie2013ct]. P2, the bound on a
licence's use whatever headers a chip is fed, holds through the powered-time counter. The best rule
on the record is a powered-time budget of [1.099](../research/numbers.md#e25-budget-least) times the
nominal licence, plus the height expiry; a rate floor only adds false stops,
[17.1%](../research/numbers.md#e25-falsestop-check) of compliant chips at the formal check's
settings. Withheld log leaves are asserted, not measured, and no hardware prototype exists. The
verdict is mixed: it supports P2 and is against the rate floor, which Part II drops.

## What has not run

E3 would measure miss and false-alarm rates per elicitation budget on locked model organisms
[@redwood2024mathpwdlock; @aisi2025auditingrepo], deciding whether C5 survives. E4(b) would decide
whether C4 reopens, and E4(d) and (e) whether C11 is more than framing. E10, on the Pythia suite
[@biderman2023pythia], and E15 would test whether inference, distillation and algorithms substitute
for compute, which could reopen C2(b). E7 would test whether a training-compute threshold catches
continual learning [@zweiger2025seal]. E12 and E20 would split F1's advantage into speed, copies and
quality [@pope2022; @wijk2024rebench]. E13 and E14 would measure energy per useful operation,
disguised power traces and training over slow links [@kimpson2026dcpower; @douillard2023diloco],
testing C8. E16, E17 and E19 would test checkers in self-training, transfer from narrow training
[@huan2026mathtransfer] and replication in a sandbox [@black2025replibench]. E21's live part, with
teams, is blocked.
