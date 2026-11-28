# The dynamical perspective

This perspective asks how a capable system becomes much more capable without inputs added by hand.
Every account we surveyed answers with feedback: an output of AI feeds its next round. Loop gain
matters to the line because it shortens breakout time (D3).

## The common form

Each loop takes Jones's semi-endogenous form [@bloom2020ideas; @besiroglu2024returns]: (1/X) dX/dt =
theta * X^(-b) * E^lambda, with b the returns exponent, lambda the return to input and r = lambda /
b. If the stock supplies its own input with closure e, its gain is K = e * r: above 1 it diverges
unless a physical limit stops it; below 1 its growth rate saturates. K is read with input growth
divided out [@cunningham2026rsi], since fast progress can be subcritical [@burtsev2026criticality].
Coupled loops explode if and only if the spectral radius rho(K) > 1 [@davidson2026feedback]. None of
this frame is ours.

## Y1a. The software loop

**Definition.** Software efficiency grows from research labour, human and AI, and research compute
[@ho2024algorithmic]. With physical compute fixed, K_S = r_S * (1 - eps_K), eps_K being compute's
share of research input: D2, Cunningham et al.'s loop gain [@cunningham2026rsi] and Burtsev's
reproduction number [@burtsev2026criticality], in a loop that is prior work
[@davidson2025three; @eth2025sie].

**Measurement.** Historical fits are wide and biased [@erdil2024idea; @whitfill2025selection];
staged runs [@zhao2025speedrun] may not transfer [@gundlach2025origin], and agents can sandbag
[@gasteiger2025subtlesandbag]. Our estimator (C4), b from an exact round identity and lambda from a
budget ladder, narrowly extends epidemic control's upper-bound rule [@blumberg2020supercritical] and
a staged test of an AI research loop [@srikanth2026aide2]. At the only calibrated noise, a human
speedrun's record-to-record spread, E4 found its [90%](../research/numbers.md#claim-confidence)
interval covering r [82%](../research/numbers.md#e4-cov-n5) of the time after
[5 rounds](../research/numbers.md#claim-d2-rounds), estimates leaning subcritical and two held-out
sets no remedy. The rule on K's upper bound fired in [88%](../research/numbers.md#e4-k-fa-n5) of
runs at the corrected median and only [2%](../research/numbers.md#e4-k-fire-gap-n5) more at the 95th
percentile: the trigger fails at that proxy and is untested at real round noise.

**Evidence for and against.** For: one developer's measured acceleration
[@metr-anthropic-acceleration-2026] and a historical language-model r of
[1.89](../research/numbers.md#dyn-r-lm). Against: with compute
[0.67](../research/numbers.md#dyn-research-compute-share) of research input and fixed, it falls to
[0.63](../research/numbers.md#dyn-r-lm-corrected), 95th percentile
[1.07](../research/numbers.md#dyn-r-lm-hi-corrected) [@ho2025experiments]; counting compute's
growth, E9 gives [0.25](../research/numbers.md#e9-lm-k-fixed)
([0.42](../research/numbers.md#e9-lm-k-fixed-hi) at the 95th percentile), above 1 only for compute
shares below about [0.26](../research/numbers.md#e9-lm-share-crit), which no data identifies.

**Open questions.** Whether compute and labour are complements, so that a compute cap binds
[@whitfill2025bottlenecks], and whether real staged rounds (E4(b)) are tight enough.

## Y1b to Y1e. The other four loops

**Definition.** AI designs better chips; revenue buys compute at an elasticity eps; deployed copies
learn from use, against forgetting; uncontrolled copies multiply at R_Q = nu / d, nu a product of
stage success rates after RepliBench [@black2025replibench]. The first three are prior work
[@davidson2025three; @erdil2023explosive; @trammell2023growth]; the last two in this form are at
most an unsearched extension.

**Measurement.** Chips and capital are visible; update compute misses local weights and in-context
adaptation, and replication is seen only in sandboxes.

**Evidence for and against.** Hardware has the highest returns surveyed but the slowest clock and
least room [@eth2025sie; @davidson2025three]. Whether AI's earnings fund capital is unmeasured, and
bottlenecks may bind [@aghion2017ai]. Self-editing works in small models but forgets
[@zweiger2025seal]. Models fail identity checks in replication tasks [@black2025replibench], a gate
local open weights never meet [@pan2024selfrep].

**Open questions.** None of the four gains is measured.

## Y2. Runaway versus saturation

**Definition.** Above gain 1 a loop amplifies at ln(R) / tau for cycle time tau
[@burtsev2026criticality]; r > 1 under full automation at constant compute is the prior-work
condition [@besiroglu2024returns; @eth2025sie].

**Measurement.** Closure's clock is unattended agent work: the 80% horizon is about
[3 hours](../research/numbers.md#dyn-horizon-p80-hours) of human time
[@metr2026thdata; @kwa2025horizon].

**Evidence for and against.** Loops explode jointly under weaker conditions than alone
[@davidson2026feedback]; diminishing returns [@bloom2020ideas], parallel work that does not add up
[@trammell2026parallel] and finite room resist. Software returns straddle 1, so neither regime can
be assumed.

**Open questions.** An agent's own time on horizon-length tasks is unmeasured, so gates count
completed tasks, not hours. Closure judged input by input (C11) follows the task-based automation
model [@aghion2017ai]; whether one-gate measurements predict the gain, and whether D6's share of
ungated increments stands for this elasticity, is untested (E4(d)).

## Y3. Coupling

**Definition.** For nonnegative K, rho(K) > 1 means runaway even with every own gain below 1
[@davidson2026feedback; @burtsev2026criticality], prior work like the program's metaphor
[@yudkowsky2013iem]. The treaty test (C6) certifies rho(K) <= rho(U) from entrywise bounds U holding
jointly with probability 1 - zeta, the network small-gain theorem's linear case
[@dashkovskiy2007smallgain]; choosing edges to cut [@roberts2003typer; @vanmieghem2011spectral] and
testing a spectral radius against 1 [@bardoscia2017pathways] are prior work too.

**Measurement.** E11 found measured bounds on
[2 entries](../research/numbers.md#e11-entries-measured) of
[10 entries](../research/numbers.md#e11-entries); a certificate needs all, so none issues today, and
the looser row-sum bound never can while compute feeds software, its floor being
[2.14](../research/numbers.md#e11-rowsum-floor).

**Evidence for and against.** Subcritical blocs become supercritical through transfer
[@burtsev2026criticality]. With negative couplings rho(K) > 1 no longer shows runaway, though rho(U)
< 1 still rules it out (Part III). A fully closed software loop at its corrected 95th percentile
leaves [-0.07](../research/numbers.md#dyn-software-headroom-upper) of headroom, so no cuts certify
it, under the correction that omits compute's growth.

**Open questions.** Joint bounds on cross-feeds, and the threshold omega, which needs an unmeasured
drift rate and response time.

## What this perspective gives the line

It gives the line a gain with an interval, not a slope of capability. None is yet measured well
enough to trigger anything: the software interval straddles 1, the estimator fails at the only
calibrated proxy, and no certificate issues while edges are unmeasured. So Part II restricts
closed-loop training research at frontier scale, the prior-work rule [@miotti2025narrowpath], and
gates the visible edges.
