# Formal results

Part III tests the claims. This section gives their second level of verification: for each claim
whose plan asks for a proof, a precise statement and the idea of its proof, and for each empirical
claim, what is empirical. At level 2, as the verification record states, seven claims are
corrected: C4, C7 and C9 were false in part as stated, and C1, C3, C8 and C11 are sharpened. C2 is
proved under its assumptions, C5 and C6 are proved, and C10 and C12 are empirical, with their
statements narrowed. Each statement with numerical content has a check, a deterministic public
script that searches seeded random instances and edge cases for counterexamples; all thirteen pass.
The red team found four errors in an earlier version, and E6 two gaps; each is corrected below and
kept in its check. Most lemmas are textbook, and there what may be ours is the use.

## The line and its error budget (C1)

Let the time to a first confirmed finding on path p have a continuous nondecreasing cumulative
hazard Phi_p, let a finding halt the breakout T_resp(p) later, and let beta be the tolerated chance
of success, with T_d(p) = inf{t : Phi_p(t) >= ln(1/beta)}. Success then has chance at most beta iff
T_b(p) >= T_d(p) + T_resp(p) (Lemma 1.1), at a constant rate the prevention condition of Gan's model
[@gan2026clock]. If estimates err in the unsafe direction by at most factors e_b and e_r, a path
admitted at T_b_hat >= m * T_r_hat stays safe whenever e_b * e_r <= m, for any continuous hazard
(Proposition 1.2, a chain of inequalities).

C1 was corrected three times. The per-path test holds against an evader that commits to a path in
advance (Proposition 1.5). Against one that moves progress between paths, with the first event it
can observe arriving at a constant rate and counted as a finding, the test is exact if progress
restarts and every response is shorter than every breakout (Proposition 1.7). If progress carries
over, the line becomes c_min * x* >= ln(1/beta), with c_min the fewest findings expected over a
whole breakout's work on any path and x* = 1 - max_p T_resp(p) / min_p T_b(p) (Proposition 1.8).
Both are stopping arguments: before a first finding the evader follows a fixed randomised plan. The
guarantee is per attempt; n attempts succeed with chance at most the sum of their beta_i
(Proposition 1.9). Checked only at declarations, between which T_b can fall by a factor phi, the
line must hold at phi * m * T_r (Proposition 1.6); the margin covers estimation error only. If a
run's speed can rise by at most g(tau) after tau of running, with G the integral of g, a line
computed at launch speed must meet phi * G(m * T_r), not phi * m * T_r (Corollary 1.6a): at the
protocol's margin, G raises it [3.2](../research/numbers.md#formal-inrun-line-factor) times at the
central drift rate and [10.6](../research/numbers.md#formal-inrun-line-factor-high) at the high end,
both upper bounds. Propositions 1.7 and 1.8 are not proved for a run whose speed rises.
[Full proof](https://subcritical.space/research/formal#c1-the-line-per-path).

## Breakout time and detection (C2, C3)

If every input other than C* raises log effective compute at every time, T_b(H) is nonincreasing in
each such input and nondecreasing in C*, so two corners of an input box give the exact interval
(Theorem 2.1): proved under assumptions. Where drift falls with scale this fails, and a termwise
bound takes over. Corollary 2.3, the leak under a compute cap, assumes drift closes the headroom at
a constant rate; E18 finds it closes in jumps, at yearly rates from
[1.91](../research/numbers.md#e18-bt-gamma-lo) to [1,125](../research/numbers.md#e18-bt-gamma-hi).
The proof stands and the model fails: its leak time is an average over jumps, and a cap's line needs
the largest jump that can arrive within m * T_r.
[Full proof](https://subcritical.space/research/formal#c2-breakout-time-is-monotone-in-its-inputs).

With channels independent given the evader's strategy sigma, its best strategy is missed with chance
max over sigma of prod_c q_c(sigma), q_c being channel c's miss chance, which a product over all
channels equals only if every channel with q_c < 1 watches every path (Theorem 3.1): Baker et al.'s
weakest link [@baker2025verifying] and the non-detection game [@avenhaus2002inspection]. A common
cause Z, real-valued or with independent components, under which each q_c is nondecreasing, gives
E[prod_c q_c(Z)] >= prod_c E[q_c(Z)] (Theorem 3.2, by Harris's inequality). Corrected: it first
claimed any Z, which the red team's Z2 = 1 - Z1 broke. Merged channels have a rate of at least the
largest under any dependence, and at most the sum under positive dependence (Theorem 3.3); an anchor
the evader can break is a path with rate zero.
[Full proof](https://subcritical.space/research/formal#c3-detection-as-the-evader-sees-it).

## The loop gain and elicitation (C4, C5)

With b the returns exponent (Part I's beta), Delta_k the gain in round k and each round's input
fixed, x_k = b * Delta_k satisfies exactly ln[(e^(x_(k+1)) - 1) / (e^(x_k) - 1)] = b * (K - 1) *
Delta_k (Lemma 4.1), since e^(b u) grows linearly within a round; the claim's form holds to first
order. The ratio g_k = Delta_(k+1) / Delta_k exceeds 1 iff K > 1 but tends to 1 when K < 1, so a
trigger on g_k at a fixed threshold below 1 fires on every subcritical loop that runs long enough
(Proposition 4.3). Corrected: the trigger is now the upper bound on K (Proposition 4.4), and at a
closure bound of 1 it fires wherever the rule on r does, so r's false-alarm rate is not K's
(Corollary 4.5a). Coverage is empirical. The growth law and the gain's threshold are prior work
[@bloom2020ideas; @besiroglu2024returns; @cunningham2026rsi; @burtsev2026criticality].
[Full proof](https://subcritical.space/research/formal#c4-the-loop-gain-estimator).

C5 is proved, textbook. Clopper and Pearson's exact bound (Theorem 5.1) needs, with no misses, at
[90%](../research/numbers.md#claim-confidence) confidence and a
[10%](../research/numbers.md#claim-d5-miss-target) target,
[22 organisms](../research/numbers.md#claim-d5-organisms). A sequential test is valid under any
stopping rule (Proposition 5.2, by Ville's inequality), and the bounds cover only the population
sampled (Proposition 5.3).
[Full proof](https://subcritical.space/research/formal#c5-miss-and-false-alarm-rates-with-exact-bounds).

## Coupled loops and the coalition (C6, C7)

If the bounds |K_ij| <= U_ij hold jointly with chance 1 - alpha, then with that chance rho(K+) <=
rho(U) <= max_i (U w)_i / w_i for every w > 0, with K+ the couplings with negative entries set to 0
(Theorem 6.2, by Perron-Frobenius). Nonnegative couplings with rho(K) > 1 make some stock
diverge in finite time, and couplings of any sign with rho(K+) < 1 allow only logarithmic growth, so
for signed couplings rho(K) > 1 shows nothing (Theorem 6.4); the first part is Davidson et al.'s
[@davidson2026feedback]. Proved; Corollary 6.3 restates C4 for a fully closed loop.
[Full proof](https://subcritical.space/research/formal#c6-the-coupled-gain-certificate-and-the-runaway-condition).

The largest admissible coalition share is s* = min(1, h_w / (m * T_r)) at a fixed fleet and
algorithms, with h_w the whole fleet's time to the breakout budget, and min(1, h_w / G(m * T_r))
when runs absorb drift (Proposition 7.1): the hardwired-pause threshold solved for the share
[@fithian2026hardwired]. Let member i value a successful breakout at V_i and lose P_i if caught. For
every share whose breakout time reaches T_r, no deviation is self-enforcing if every member of a
coalition of two or more gets a reward R_i > beta * V_i for reporting, and no breakout profits a
party with beta * V_i <= (1 - beta) * P_i (Theorem 7.2, after
[@bernheim1987coalition; @ali2019coalitions]). Corrected: (b) placed a profitable deviation just
above s*, but under these conditions none exists up to h_w / T_r, which is m * s* when s* < 1. If
caught members are re-admitted, the reward must exceed beta * V_i / (1 - delta * (1 - beta)), with
delta the weight on the next period, nearing V_i as delta nears 1.
[Full proof](https://subcritical.space/research/formal#c7-the-coalition-share).

## Floors, the licence and the empirical claims (C8 to C12)

A run of C useful operations within time T, at utilisation at most u_bar, needs at least C / (r_bar
* u_bar * T) chips counted in units of a peak r_bar (Theorem 8.1, by summing each chip's work); it
is a bound only with u_bar = 1 and r_bar the peak at the lowest trainable precision. Corrected
twice: for [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) under a pause, Part I's
estimate of [4,000 H100e](../research/numbers.md#phys-floor-chips-1e26-pause) gives way to a bound
of [800 H100e](../research/numbers.md#formal-floor-bound-1e26-pause) at FP8
[@rahman2026; @koopmanschap2026gpu; @scher2025].
[Full proof](https://subcritical.space/research/formal#c8-the-footprint-floor-as-a-bound).

C9 is corrected. As proved, a chip licensed for L blocks that stops at its expiry height, or once
its height falls behind a floor of rho_min blocks per unit of powered time, less a slack s, runs at
most (L + s) / rho_min of powered time whatever headers it is fed (Proposition 9.1); the claim's
rule ran about L times its timeout. That bound is the powered-time counter's [@petrie2025flexheg2],
and E25 found the floor dominated: what stands is a plain powered-time budget at the longest honest
span, [1.099](../research/numbers.md#e25-budget-least) times the nominal licence time, plus a
margin, and Part II uses no floor. The height adds only a calendar expiry for chips online. The chip
counts the most-work chain (Lemma 9.2). Anchored logs give every auditor the same licences under an
honest hash majority, given a party trusted to publish every leaf, or rival replicas (Proposition
9.4) [@laurie2013ct].
[Full proof](https://subcritical.space/research/formal#c9-the-height-clocked-licence).

C10 is empirical, a definition; t* is well defined as the largest tested crossing, censored when the
system wins at every budget (Proposition 10.1). A capped score cannot clear 1 by more than noise: on
METR's RE-Bench no agent's ratio can pass [1.006](../research/numbers.md#e21-rebench-ceiling-32h) at
32 hours, so the best model's t* is censored at the battery's top budget,
[32.0 h](../research/numbers.md#e21-rebench-tstar-best). Claim (c), that t* rises without
saturating, is testable only on a battery whose ceiling and top budget the systems do not reach. For
C11, per-input factors multiply for one round's output only when ln F is additively separable
(Theorem 11.1), but the loop gain is (lambda / b) * sum_i s_i(X) * e_i, a mean of the closures e_i
weighted by input shares (Theorem 11.2). Corrected: closures add. Under complements, as the evidence
suggests [@gundlach2025origin; @whitfill2025bottlenecks], the least closure comes to set the gain;
under substitutes the greatest, the case for holding every input together [@scher2026research].
Until E4(d) decides, the safe bound uses the largest ungated closure. C12 is empirical, a judgement:
positive weights can rank either of two pathways first when each leads on one criterion, so evidence
fixes only Pareto-ordered pairs (Proposition 12.1).
[Full proof](https://subcritical.space/research/formal#c10-superintelligence-at-matched-budget-what-is-empirical).
[Full proof](https://subcritical.space/research/formal#c11-closure-by-input-the-combination-rule).
[Full proof](https://subcritical.space/research/formal#c12-the-ranking-what-can-be-proved).

## Compliance under inspection with no known last period

A member complies each period, worth w, or attempts a breakout, worth dev = pi * V - (1 - pi) * P.
If the regime continues with chance delta and has no known last period, complying forever is a
subgame-perfect best response iff w / (1 - delta) >= dev (Theorem E.1, by the one-shot deviation
principle). With a known last period and dev > w, a party that would otherwise comply attempts at
the end (Theorem E.2), the end effect of recursive inspection games [@vonstengel2016recursive].
Prevention implies the inspection game's condition for legal behaviour only at a large enough
penalty (Propositions E.3, E.4) [@avenhaus2002inspection]. Proved in textbook form; none of it is
ours.
[Full proof](https://subcritical.space/research/formal#compliance-as-an-equilibrium-inspection-games-with-no-known-last-period).

## What the proofs do not establish

The gap between theorem and claim is the assumptions. No AI channel has a detection rate measured
against a real evader, and no AI regime a response time; nothing bounds the number of attempts. The
margin does not cover error in C*. Couplings, payoffs, the round model and the interval's coverage
are unmeasured or untested, and one broken trust anchor defeats every chip at once. Outside every
model are an unlisted path, a party that leaves and races, sabotage, and errors in the proofs that
the checks would not catch.
[Full list](https://subcritical.space/research/formal#what-the-proofs-do-not-establish).
