# Formal results

This section states what can be proved, under which assumptions, and how. Each numerical statement
has a public, seeded check that searches random and edge-case instances for counterexamples; all
thirteen pass, though they test statements, not proofs.

## The line, breakout time and detection (C1 to C3)

Let the first confirmed finding on path p have a continuous nondecreasing cumulative hazard Phi_p,
the evader's best case, and T_d(p) = inf{t : Phi_p(t) >= ln(1/beta)}. If a finding halts the
breakout T_resp(p) later, success has chance at most beta iff T_b(p) >= T_d(p) + T_resp(p) (Lemma
1.1), at a constant rate mu Gan's prevention condition [@gan2026clock]. If estimates err unsafely by
factors of at most e_b and e_r, an admitted path stays safe when e_b * e_r <= m (Proposition 1.2),
the partial-factor format of structural design [@jrc2008eurocodes]. Phi_p is assumed not to rise
with the breakout's intensity, though a faster breakout leaves a larger footprint. Where the hazard
used is only a lower bound, guarantees that a path is stopped hold as one-sided bounds; a verdict
that a path fails the line may not.

If the evader can move progress between paths, the line becomes c_min * x* >= ln(1/beta), with c_min
the smallest mu_p * T_b(p) and x* = 1 - max_p T_resp(p) / min_p T_b(p) (Proposition 1.8), by a
stopping argument: before a first finding the evader follows a fixed randomised plan. Checked at declarations, between which T_b can fall by a factor
phi, a line computed at launch speed must meet phi * G(m * T_r), G integrating the most a run's
speed can rise (Corollary 1.6a): [3.2](../research/numbers.md#formal-inrun-line-factor) times higher
at the central drift rate, [10.6](../research/numbers.md#formal-inrun-line-factor-high) at the high
end, both upper bounds. Proposition 1.8 is unproved when speed rises.
[Full proof](https://subcritical.space/research/formal#c1-the-line-per-path).

If every input but C* raises log effective compute throughout, an input box's two corners bound
T_b(H) exactly (Theorem 2.1). The leak under a cap (Corollary 2.3) assumes a constant rate; E18
finds jumps, so a cap's line needs the largest jump possible within m * T_r.
[Full proof](https://subcritical.space/research/formal#c2-breakout-time-is-monotone-in-its-inputs).

With channels independent given the evader's strategy sigma, it is missed with chance max over sigma
of prod_c q_c(sigma) (Theorem 3.1) [@baker2025verifying; @avenhaus2002inspection]. A scalar common
cause that raises every miss chance makes the joint miss at least the product of the marginals
(Theorem 3.2, Harris's inequality). Merged channels have at least the largest rate and at most the
sum under positive dependence (Theorem 3.3): the bound on a union, with risk assessment's
common-cause practice [@mosleh1998nureg5485].
[Full proof](https://subcritical.space/research/formal#c3-detection-as-the-evader-sees-it).

## Loops, elicitation and coalitions (C4 to C7)

With b the returns exponent and each round's input fixed, round gains satisfy exactly ln[(e^(b *
Delta_(k+1)) - 1) / (e^(b * Delta_k) - 1)] = b * (K - 1) * Delta_k (Lemma 4.1). Their ratio tends to
1 when K < 1, so a fixed threshold below 1 fires on every long subcritical loop (Proposition 4.3). A
rule on K's upper bound misses a loop above K* with chance at most zeta, by the duality of tests and
intervals (Proposition 4.4); the interval's coverage is unproved. The growth law and threshold are
prior work [@bloom2020ideas; @besiroglu2024returns; @cunningham2026rsi; @burtsev2026criticality].
[Full proof](https://subcritical.space/research/formal#c4-the-loop-gain-estimator).

The exact Clopper-Pearson bound needs [22 organisms](../research/numbers.md#claim-d5-organisms)
without a miss for a [10%](../research/numbers.md#claim-d5-miss-target) target at
[90%](../research/numbers.md#claim-confidence) confidence (Theorem 5.1); Ville's inequality makes a
sequential test valid under any stopping rule (Proposition 5.2). Both are textbook and hold only on
the population sampled (Proposition 5.3).
[Full proof](https://subcritical.space/research/formal#c5-miss-and-false-alarm-rates-with-exact-bounds).

If |K_ij| <= U_ij jointly with chance 1 - zeta, then rho(K+) <= rho(U), K+ being the couplings'
nonnegative part (Theorem 6.2, Perron-Frobenius). Nonnegative couplings with rho(K) > 1 diverge in
finite time [@davidson2026feedback]; any couplings with rho(K+) < 1 grow only logarithmically, so a
signed rho(K) > 1 shows nothing (Theorem 6.4).
[Full proof](https://subcritical.space/research/formal#c6-the-coupled-gain-certificate-and-the-runaway-condition).

A coalition's largest admissible share is s* = min(1, h_w / G(m * T_r)), h_w being the whole fleet's
time to the breakout budget (Proposition 7.1) [@fithian2026hardwired]. While breakout time exceeds
T_r, no deviation is self-enforcing if each member is paid R_i > beta * V_i for reporting, V_i its
value of success, and none profits a party with beta * V_i <= (1 - beta) * P_i, P_i its penalty if
caught (Theorem 7.2, after [@bernheim1987coalition; @ali2019coalitions]).
[Full proof](https://subcritical.space/research/formal#c7-the-coalition-share).

## Floors, licences and what experiment decides (C8 to C12)

A run of C operations within T needs at least C / (r_bar * T) chips of peak r_bar, by summing each
chip's work (Theorem 8.1): at the lowest trainable precision,
[800 H100e](../research/numbers.md#formal-floor-bound-1e26-pause) for
[1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) under a pause
[@rahman2026; @koopmanschap2026gpu; @scher2025].
[Full proof](https://subcritical.space/research/formal#c8-the-footprint-floor-as-a-bound).

A chip licensed for L blocks that stops at its expiry height, or once its height falls behind xi_min
blocks per unit of powered time less a slack s, runs at most (L + s) / xi_min of powered time
whatever headers it is fed (Proposition 9.1). That is the powered-time counter's bound
[@petrie2025flexheg2]: a plain budget of [1.099](../research/numbers.md#e25-budget-least) times the
nominal licence time plus a margin, E25's least, needs no floor, and the height adds only expiry for
chips online. Anchored logs agree for every auditor given an honest hash majority and a trusted
publisher (Proposition 9.4) [@laurie2013ct].
[Full proof](https://subcritical.space/research/formal#c9-the-height-clocked-licence).

The crossover budget t* is well defined, censored when the system wins at every budget (Proposition
10.1); on RE-Bench no ratio can pass [1.006](../research/numbers.md#e21-rebench-ceiling-32h) at 32
hours, so t* needs an unsaturated battery. The loop gain is (lambda / b) * sum_i s_i * e_i, a
share-weighted mean of input closures, so closures add (Theorem 11.2); the least sets the gain under
complements, as the evidence suggests [@gundlach2025origin; @whitfill2025bottlenecks], the greatest
under substitutes [@scher2026research]. Positive weights can rank either of two pathways first when
each leads on one criterion, so without agreed weights only pairs ordered on every criterion are
fixed (Proposition 12.1).
[Full proof](https://subcritical.space/research/formal#c10-superintelligence-at-matched-budget-what-is-empirical).
[Full proof](https://subcritical.space/research/formal#c11-closure-by-input-the-combination-rule).
[Full proof](https://subcritical.space/research/formal#c12-the-ranking-what-can-be-proved).

## Compliance, and what the proofs do not establish

If a member complies each period for w or attempts a breakout worth dev, then with no known last
period and continuation chance delta, complying forever is subgame perfect iff w / (1 - delta) >=
dev, by one-shot deviation (Theorem E.1); with a known last period and dev > w, a party attempts in
it (Theorem E.2) [@vonstengel2016recursive]. Prevention implies the inspection game's condition for
legal behaviour, at false-alarm chance zeta, only for a large enough penalty P (Propositions E.3,
E.4) [@avenhaus2002inspection]. All of this is textbook.
[Full proof](https://subcritical.space/research/formal#compliance-as-an-equilibrium-inspection-games-with-no-known-last-period).

The gap between theorem and claim is the assumptions: no AI channel's detection rate against a real
evader is measured, nor any regime's response time, coupling or payoff; nothing bounds the number of
attempts; and the margin does not cover error in C*. Outside every model are an unlisted path, a
party that leaves and races, sabotage, and errors in the proofs.
[Full list](https://subcritical.space/research/formal#what-the-proofs-do-not-establish).
