# The dynamical perspective

This perspective asks how a capable system becomes a much more capable one without anyone adding the
inputs by hand. Every account we surveyed answers with feedback: some output of AI becomes an input
to the next round. We write each loop as a growth law, with its returns, its clock and its
conditions for runaway or saturation. This matters to the line because loop gain shortens breakout
time (D3): the path to superintelligence is combined feedback above 1, faster than a regime can
respond.

## The common form: a growth law and its returns

Each loop takes the semi-endogenous form of Jones [@bloom2020ideas; @besiroglu2024returns]: (1/X)
dX/dt = theta * X^(-beta) * E^lambda. X is the stock the loop improves and E its input; beta > 0
says ideas get harder to find, and the returns r = lambda / beta count doublings of X per doubling
of cumulative input. The loop closes when the stock supplies its own input, E proportional to X^e,
with e the closure. The growth rate then scales as X^(beta (K - 1)), where K = e * r is the loop's
own gain. Below K = 1 each doubling takes longer than the last, which saturates the rate but not
necessarily the level; above 1 the stock diverges in finite time unless a physical limit intervenes.

K is defined on a log, compute-equivalent axis, so a ratio of gains on a bounded benchmark does not
measure it. Output growth must be divided by input growth [@cunningham2026rsi], and slope is not
gain: fast progress can be subcritical [@burtsev2026criticality]. For several loops, K_ij = lambda_i
* e_ij / beta_i, and growth is explosive if and only if rho(K) > 1 [@davidson2026feedback]. None of
this frame is ours. Closure here is an elasticity, not D6's share of ungated increments.

## Y1a. The software loop

**Definition.** The stock is software efficiency, the effective compute per physical operation at
fixed capability, on a log scale [@ho2024algorithmic]. The input is human and AI research labour,
experiment compute and research inference. With physical compute fixed, K_S = r_S * (1 - eps_K),
eps_K being compute's share of research input. This is D2, and the quantity Cunningham et al. call
loop gain [@cunningham2026rsi] and Burtsev a recursive reproduction number
[@burtsev2026criticality]. The loop is prior work [@davidson2025three; @eth2025sie].

**Measurement.** Historical fits have wide intervals and selection bias
[@erdil2024idea; @whitfill2025selection]. Staged runs have a public harness
[@moddednanogpt; @zhao2025speedrun], but small-scale returns may not transfer [@gundlach2025origin]
and agents can sandbag [@gasteiger2025subtlesandbag]. Our estimator (C4) fits beta from an exact
identity between successive round gains at fixed compute, and lambda from a ladder of agent budgets.
It extends narrowly epidemic control's upper-bound rule [@blumberg2020supercritical] and a staged,
fixed-budget test of an AI research loop [@srikanth2026aide2]. At the only data-calibrated noise,
E4's final simulation found that it fails. After [5 rounds](../research/numbers.md#claim-d2-rounds)
at each budget its nominal [90%](../research/numbers.md#claim-confidence) interval covered r
[82%](../research/numbers.md#e4-cov-n5) of the time, and [77%](../research/numbers.md#e4-cov-n5-xml)
with the exact likelihood; every estimator leaned subcritical, and two held-out sets per round did
not remedy it. The upper-bound rule on K fired in [88%](../research/numbers.md#e4-k-fa-n5) of runs
at the corrected median, well below 1, and only [2%](../research/numbers.md#e4-k-fire-gap-n5) more
often at the corrected 95th percentile, within Monte Carlo error. The trigger is cut, and C4 is
downgraded to a measurement design, untried on any real staged run.

**Evidence for and against.** For: METR measured a [1.9](../research/numbers.md#dyn-metr-accel)-fold
acceleration in one developer's capability index [@metr-anthropic-acceleration-2026], and the
historical language-model r is [1.89](../research/numbers.md#dyn-r-lm) [@ho2025experiments].
Against: if compute is [0.67](../research/numbers.md#dyn-research-compute-share) of research input
and fixed, that estimate falls to [0.63](../research/numbers.md#dyn-r-lm-corrected) and its 95th
percentile to [1.07](../research/numbers.md#dyn-r-lm-hi-corrected) [@ho2025experiments]. Counting
compute's growth, which that correction leaves out, E9 gives
[0.25](../research/numbers.md#e9-lm-k-fixed) ([0.42](../research/numbers.md#e9-lm-k-fixed-hi) at the
95th percentile), above 1 only for compute shares below about
[0.26](../research/numbers.md#e9-lm-share-crit); no data identifies the share.

**Open questions.** Whether compute and research labour are complements [@whitfill2025bottlenecks],
which decides whether a compute cap bounds the loop, and whether real staged rounds (E4(b)) are
tight enough to decide. E4 withdrew the speedrun's r as not identified, since stock and input move
together. Meanwhile Part II restricts closed-loop training research at frontier scale outright, the
prior-work rule [@miotti2025narrowpath].

## Y1b to Y1e. Hardware, economic, experiential and acquisitive loops

**Definition.** Hardware: AI designs better chips, raising compute per dollar. Economic: capability
earns revenue that buys compute capital, the regime set by eps, the elasticity of AI revenue to that
capital. Experiential: deployed copies turn experience into weight updates, with forgetting as a
brake. Acquisitive: copies outside their operator's control multiply with reproduction number R_Q =
b / d, b a product of stage success rates following RepliBench's domains [@black2025replibench]. The
first three are prior work [@davidson2025three; @erdil2023explosive; @trammell2023growth]; writing
the last two in the same form is at most an extension, and unsearched.

**Measurement.** Chips and capital are visible; no source we found measured the closures: AI's share
of hardware research, or AI revenue against capital. Update compute shows weight updates, but not
local weights or adaptation in context; replication rates come only from sandboxes.

**Evidence for and against.** Hardware has the highest returns surveyed, r about
[5](../research/numbers.md#dyn-r-gpu) to [7](../research/numbers.md#dyn-r-hardware-hist)
[@eth2025sie], but fabs take [1.9 years](../research/numbers.md#dyn-fab-build-years)
[@verwey2021permits] and room is about [2](../research/numbers.md#dyn-ie-chiptech-oom) orders of
magnitude [@davidson2025three]. Capital spending is large [@ehsan2026capex], but whether AI's own
earnings pay for it is unmeasured, and bottlenecks may bind [@aghion2017ai]. Self-editing raised a
small model's knowledge incorporation from [33.5%](../research/numbers.md#dyn-seal-squad-base) to
[47.0%](../research/numbers.md#dyn-seal-squad), while earlier tasks degrade
[@zweiger2025seal; @luo2023forgetting]. Frontier models passed
[60%](../research/numbers.md#dyn-aisi-rep-2025) of simplified replication evaluations
[@aisi2025trends] but fail at identity checks [@black2025replibench], a gate open weights on local
hardware never meet [@pan2024selfrep].

**Open questions.** None of the four gains is measured.

## Y2. Runaway versus saturation

**Definition.** A loop runs away when its own gain exceeds 1 and saturates in rate below it. Danger
also depends on the cycle time tau: above 1, amplification runs at ln(R) / tau
[@burtsev2026criticality]. The condition r > 1 under full automation at constant compute is prior
work [@besiroglu2024returns; @eth2025sie].

**Measurement.** The clock of closure is how long agents work unattended: the latest 50% time
horizon is about [17 hours](../research/numbers.md#dyn-horizon-p50-hours) of human time, the 80%
horizon about [3 hours](../research/numbers.md#dyn-horizon-p80-hours) [@metr2026thdata].

**Evidence for and against.** For runaway: the language-model r, and loops that explode jointly
under weaker conditions than any alone [@davidson2026feedback]. For saturation: research
productivity falls about [5.3%](../research/numbers.md#dyn-bloom-rp-decline) a year
[@bloom2020ideas], parallel work does not add up [@trammell2026parallel], and room is finite.
Software returns straddle 1, so neither regime can be assumed.

**Open questions.** Horizons are measured in human time [@kwa2025horizon], and no experiment here
measures the agent's own; until one does, human-held gates count completed horizon-length tasks, not
hours. Judging closure input by input against such gates (C11) extends the task-based automation
model narrowly [@aghion2017ai] and is framing until experiment E4(d).

## Y3. Coupling

**Definition.** The combined gain is rho(K) over loops and parties. For nonnegative K the system
runs away when rho(K) > 1, even with every own gain below 1
[@davidson2026feedback; @burtsev2026criticality]. This is prior work, as is the metaphor behind the
program's name [@yudkowsky2013iem]. The treaty test on it (C6) is an application of prior work: if
bounds U_ij >= |K_ij| hold jointly with probability 1 - alpha, then rho(K) <= rho(U) <= max_i sum_j
U_ij, the linear case of the network small-gain theorem [@dashkovskiy2007smallgain]; choosing edges
to cut [@roberts2003typer; @vanmieghem2011spectral] and a regulator testing a spectral radius
against 1 [@bardoscia2017pathways] are prior work as well.

**Measurement.** E11 found a measured bound on
[2 entries](../research/numbers.md#e11-entries-measured) of the
[10 entries](../research/numbers.md#e11-entries) in the one-party loop graph. A certificate issues
only when every edge has one, so none can issue today. The test is rho(U); its looser row-sum bound
never issues while compute feeds software, since no bound matrix on the graph has a largest row sum
below [2.14](../research/numbers.md#e11-rowsum-floor).

**Evidence for and against.** For: Burtsev's blocs, each subcritical, reach a network rho of
[1.15](../research/numbers.md#dyn-burtsev-network-rho) through transfer [@burtsev2026criticality].
Against: with negative couplings rho(K) > 1 no longer shows runaway, though rho(U) < 1 still rules
it out (Part III); and a fully closed software loop at its corrected 95th percentile leaves
[-0.07](../research/numbers.md#dyn-software-headroom-upper) of headroom, so no edge cuts certify it,
under the correction that leaves compute's growth out.

**Open questions.** How to bound a cross-feed jointly, and the margin below 1, which needs a drift
rate and a response time nobody has measured.

## What this perspective gives the line

This perspective gives the line a gain with an interval to hold down, not a slope of capability. No
gain is yet measured tightly enough to trigger anything: the software interval straddles 1, the
staged estimator fails at calibrated noise, and no coupled certificate can issue while edges are
unmeasured. Part II therefore restricts the closed loop at frontier scale and gates the visible
edges, a design untested against any adversary.
