# Part III, 1: Formal statements and proofs

This file is level 2 of the six levels each claim in [the claims file](04-claims.md) must pass. For
every claim whose plan asks for a proof, it gives a precise statement and a proof. For every claim
that is empirical, it says what exactly is empirical and which experiment decides it. It also covers
the formal items the memo listed under the protocol's shape: the detection bound over breakout time
with several channels, compliance as an equilibrium with no known last period, the coalition
threshold, the runaway condition for coupled loops, and the conditions under which each fails.

A proof under assumptions is only as good as its assumptions. Each section states its assumptions
so that they can be wrong, says where the result fails, and credits what is textbook. Most lemmas
below are textbook or follow in a few lines from published models; where that is so, what may be
ours is the use, not the lemma. Nothing here has been tested against a real adversary. The protocol
is a design.

Each statement with numerical content has a deterministic check, `tools/formal/<name>.py`: standard
library only, seeded random instances with edge cases, exit 1 and the instance printed on any
counterexample. `python3 tools/formal/run_all.py` runs them all. Every check passes. Three claims are
false as stated in part (C4, C7 and C9) and are corrected below; C1 and C11 need their statements
sharpened. The summary says what each claim must change.

## Summary

| Claim | L2 verdict | Statements | Check | What the claim must change |
|---|---|---|---|---|
| C1 | Proved under stated assumptions; corrected | Lemma 1.1, Props 1.2, 1.4 to 1.6, Cor 1.3 | `c1_margin.py` | State the line per path, T_b(p) >= m T_r(p) for every p; the single T_b against the single T_d is a stricter shortcut |
| C2 | Formal part proved under monotone inputs; the rest empirical | Thm 2.1, Cors 2.2, 2.3 | `c2_monotone.py` | Assume, and test, that no input lowers breakout's left side; pair each path with its own T_r |
| C3 | Proved under stated assumptions | Thms 3.1 to 3.3, Cor 3.4 | `c3_evader.py` | Merging is safe under any dependence; "between the larger rate and the sum" needs positive dependence; an anchor the evader can break is a path with rate zero |
| C4 | Identity proved (exact in a transformed form; the claim's form is first-order); coverage empirical; trigger corrected | Lemmas 4.1, 4.2, Props 4.3 to 4.6 | `c4_identity.py` | Trigger on the gain K, not on the per-round ratio g_k against a fixed g* below 1; drop "bounded at 2.7 times"; measure each round twice |
| C5 | Proved (textbook) | Thm 5.1, Props 5.2, 5.3 | `c5_binomial.py` | None; add the counts with misses and the sequential test |
| C6 | Proved; the certificate holds for signed matrices; runaway condition proved for nonnegative ones | Lemma 6.1, Thm 6.2, Cors 6.3, 6.5, 6.6, Thm 6.4 | `c6_certificate.py`, `c6_runaway.py` | (b) needs exhaustive search, not greedy cuts; (c) is a corollary of the diagonal bound |
| C7 | (a) proved; (b) false as stated, corrected | Prop 7.1, Thm 7.2 | `c7_coalition.py` | No deviation is self-enforcing up to h_w / T_r = m s*, not s*; state the reward condition R_i > beta V_i |
| C8 | Proved as a bound once corrected | Thm 8.1, Lemma 8.2 | `c8_floor.py` | Compute floors at the highest attainable utilisation; the longest run T is an assumption about the adversary |
| C9 | P1 and P3 proved under assumptions; P2 false as stated, corrected; P4 needs data availability | Props 9.1, 9.3, 9.4, Lemma 9.2 | `c9_clock.py` | Replace the progress timeout by a rate floor; P2 bounds powered time, not calendar time, offline; add data availability to P4 |
| C10 | Empirical; t* made well defined | Prop 10.1 | `c10_crossover.py` | Define t* as the largest crossing and report censoring |
| C11 | (a) combination rule corrected; (b) empirical | Thms 11.1, 11.2 | `c11_closure.py` | For the loop gain, closures combine as a share-weighted mean, not a product; use the largest ungated closure until E4(d) decides |
| C12 | Empirical; necessity within a horizon as a corollary | Cor 6.5, Prop 12.1 | `c6_runaway.py` | Only Pareto-ordered pairs are fixed by evidence; name them |
| Memo | Compliance as an equilibrium: proved, textbook form | Thms E.1, E.2, Props E.3, E.4 | `eq_inspection.py` | Nothing claimed |

## Notation

- H: a party's holdings. P(H): the paths open to it (declared fleet, undeclared site, cloud split,
  distillation, and composites it can switch between). p: a path.
- C*: the agreed effective compute that reaches D1, a convention ([D3](01-anatomy.md#d3-breakout-time)).
- T_b(p): breakout time on path p (C2). T_b(H) = min over p of T_b(p).
- D_p: the time from the start of a breakout on p to the regime's first confirmed finding, with
  cumulative hazard Phi_p(t) = -ln Pr[D_p > t]. At a constant rate Lambda(p), Phi_p(t) = Lambda(p) t.
- beta: the tolerated chance that a breakout succeeds ([5%](numbers.md#def-prevent-beta) in Part I's
  illustrations). T_d(p) = inf{t : Phi_p(t) >= ln(1/beta)}, which is ln(1/beta) / Lambda(p) at a
  constant rate.
- T_resp(p): the time from a confirmed finding to an effective halt. T_r(p) = T_d(p) + T_resp(p).
  m >= 1: the margin. S(p): the chance a breakout on p succeeds; S = max over p of S(p).
- c: a channel. C(p): the channels that watch p. lambda_c(p): channel c's detection rate on p (a
  year). q_c(p): its miss chance over a window.
- The common form ([the dynamical chapter](013-dynamical.md#the-common-form-a-growth-law-and-its-returns)):
  (1/X) dX/dt = theta X^(-b) E^lambda, u = ln(X/X_0), r = lambda / b, closure e, loop gain K = e r;
  for several loops K_ij = lambda_i e_ij / b_i. Part I calls the diminishing-returns exponent beta;
  it is b here, because beta is the miss tolerance. lambda without a channel subscript is the return
  to input, never a detection rate.
- rho(A): spectral radius. U: entrywise upper bounds on K. alpha: the error of a confidence statement.
- Delta_k: capability gained in round k of a staged run, on a log compute-equivalent axis.
  g_k = Delta_(k+1) / Delta_k: D2's loop gain for that round.
- s: a coalition's share of the accounted fleet. h_w: the time the whole fleet needs to reach the
  breakout budget. s*: the largest admissible share.
- C, T, r_bar, u_bar, e_min: a run's useful operations, its duration, the reference peak rate per
  chip, the highest attainable utilisation, the lowest energy per useful operation.
- V, P, R, w, delta: the payoff of a successful breakout, the penalty for a caught one, a reporter's
  reward, a period's value of membership, and the weight on the next period (time preference times
  the chance the regime continues). Payoffs are relative to the race that follows a regime's end.

## C1. The line, per path

**Assumptions.** (A1.1) For each path p, D_p has a continuous cumulative hazard Phi_p, nondecreasing,
with Phi_p(0) = 0, and Phi_p is the evader's best case on that path: whatever evasion the path allows
is already in it. (A1.2) A finding at time D halts the breakout at D + T_resp(p); the breakout
succeeds if D + T_resp(p) >= T_b(p). (A1.3) The regime's estimates err in the unsafe direction by at
most known factors: T_b(p) >= T_b_hat(p) / e_b and T_r(p) <= e_r T_r_hat(p), with e_b, e_r >= 1.
(A1.4) The evader chooses its path, and P(H) contains every path it can take.

**Lemma 1.1 (the prevention condition).** Under (A1.1) and (A1.2), S(p) <= beta if and only if
T_b(p) >= T_d(p) + T_resp(p).

*Proof.* S(p) = Pr[D_p >= T_b(p) - T_resp(p)]. If T_b(p) <= T_resp(p) this is 1, and the inequality
fails too, since T_d(p) > 0. Otherwise, as Phi_p is continuous, S(p) = exp(-Phi_p(T_b - T_resp)), so
S(p) <= beta iff Phi_p(T_b - T_resp) >= ln(1/beta). The set {x : Phi_p(x) >= ln(1/beta)} of a
continuous nondecreasing function is the closed half-line starting at T_d(p). ∎

At a constant rate this is T_b >= ln(1/beta) / Lambda + T_resp, the prevention condition of Gan's
response-window model [@gan2026clock]: Part I's line with m = 1, an identity not claimed.

**Proposition 1.2 (the margin covers error).** Under (A1.1) to (A1.3), if a path is admitted,
T_b_hat(p) >= m T_r_hat(p), and e_b e_r <= m, then S(p) <= beta. If the errors are known separately,
T_d <= e_d T_d_hat and T_resp <= e_resp T_resp_hat, then e_r = max(e_d, e_resp) will do.

*Proof.* T_b >= T_b_hat / e_b >= m T_r_hat / e_b >= (m / (e_b e_r)) T_r >= T_r, and Lemma 1.1 applies.
For the second part, T_d + T_resp <= e_d T_d_hat + e_resp T_resp_hat <= max(e_d, e_resp) T_r_hat. ∎

This is C1(b), proved for any continuous hazard, not only Gan's constant rate.

**Corollary 1.3 (an error in the rate).** If the regime's hazard overstates the truth by at most a
factor c >= 1, Phi_p(t) >= Phi_hat_p(t) / c for all t, then T_d(p; beta) <= T_d_hat(p; beta^c). For a
Weibull hazard Phi(t) = (t / eta)^k of known shape k, overstating Phi by c understates T_d by exactly
c^(1/k).

*Proof.* Where Phi_hat reaches c ln(1/beta) = ln(1/beta^c), Phi reaches ln(1/beta), so the first time
Phi reaches it is no later. For the Weibull, T_d = eta (ln(1/beta))^(1/k), against
eta (ln(1/beta) / c)^(1/k). ∎

So a rate known only within a factor c is handled by computing T_d at beta^c. Two cautions for E5.
At a matched mean detection time the Weibull T_d is (ln(1/beta))^(1/k) / Gamma(1 + 1/k) times the
mean, against ln(1/beta) at a constant rate, so the survival fit must estimate the shape, not assume
k = 1. And a pooled record of programmes that differ in visibility is a mixture of rates, whose hazard
falls with time as the survivors are increasingly the well hidden (textbook). The evader is the hard
type, so the regime faces the maximum over types (Theorem 3.2's logic), not the pooled average, which
is what the historical discovery rate, [0.08/yr](numbers.md#org-covert-hazard), is.

**Proposition 1.4 (a random response time).** Let T_resp(p) be random, with any dependence on D_p,
and q its (1 - beta_2) quantile. If T_b(p) >= T_d(p; beta_1) + q, then S(p) <= beta_1 + beta_2.

*Proof.* If T_resp <= q and D_p < T_b - q, then D_p + T_resp < T_b and the breakout is halted. So
success lies in the union of {T_resp > q} and {D_p >= T_b - q}, and S(p) <= beta_2 +
Pr[D_p >= T_d(beta_1)] = beta_2 + beta_1. ∎

No independence is needed, which matters: a finding on a hard path may also be slow to act on. E24
reports T_resp as a distribution; this is how the line uses it.

**Proposition 1.5 (the line is per path).** Under (A1.1), (A1.2) and (A1.4), S <= beta iff
T_b(p) >= T_r(p) for every path, and mixing over paths gains the evader nothing. The scalar test,
min over p of T_b(p) >= max over p of T_r(p), implies the per-path test and not conversely; the same
holds with m on both sides.

*Proof.* A mixture gives the average of the S(p), at most their maximum; Lemma 1.1 applies path by
path. If the scalar test holds, T_b(p) >= min T_b >= max T_r >= T_r(p) for each p. For the converse,
take a declared path with T_b(d) = m T_r(d) and a covert path with T_b(c) = m T_r(c), where
T_r(c) > T_r(d). Every path meets the line, but min T_b <= T_b(d) = m T_r(d) < m T_r(c). ∎

At the historical discovery rate T_d alone is [37 years](numbers.md#path-covert-td-prevent) on a
covert path, so the scalar test brands as weapons-grade almost any holding with a fast but
well-watched declared path. C1 writes the line with one T_b (C2's minimum over paths) and one T_d
(C3's evader's best path); read literally, that is the scalar test: safe, stricter than needed. The
line should be stated per path. In `c1_margin.py`, every path met the line while the scalar test
failed in 524 of 6,000 random multi-path instances.

**Proposition 1.6 (between declarations).** If the line is checked at declarations, and between two
declarations a party's T_b(p) can fall by at most a factor phi >= 1, then T_b(p) >= phi m T_r(p) at
each declaration keeps T_b(p) >= m T_r(p) throughout. *Proof:* immediate. ∎ This answers staged
accumulation, named for E6, only if phi is bounded, that is, if supply (C8, E22) limits how fast
holdings grow.

**Fails when.** Detection depends on what the evader learns as it goes, so no Phi_p is fixed in
advance. Errors are two-sided or unbounded, so no finite m works; C*'s error is of this kind
(below). T_b(p) <= T_resp(p): no detection rate suffices, and the path must be closed rather than
watched. A path outside P(H). A heavy-tailed T_resp whose quantile E24 cannot bound.

**Prior work and ours.** The prevention identity is Gan's [@gan2026clock]; the inequality in words,
Barnett and Scher's [@barnett2025governance]; per-path analysis, acquisition path analysis
[@allen-2015-llnl]. The union bound and the Weibull are textbook. Possibly ours: the margin as a
stated error budget, the rate-error rule, the quantile form for a drilled response and the per-path
form. *Checked* on 6,000 seeded instances per statement (constant, Weibull with shapes from 0.3 to 4
and piecewise-constant hazards with blind stretches; response times dependent on detection; two to
six paths) by `tools/formal/c1_margin.py`; no counterexample.

## C2. Breakout time is monotone in its inputs

For path p let L_p(t; theta) = log10 C_p(t) + J + S_v + A_p(t), with theta the inputs (chip counts
and their growth, utilisation, the jump J, the inference span S_v, the drift rate and its dependence
on scale and labour, the loop gain), T_b(p; theta) = inf{t >= 0 : L_p(t; theta) >= log10 C*} and
T_b(H; theta) = min over p. (A2.1) Each input either raises L_p(t; theta) at every t (a raising input)
or is C*.

**Theorem 2.1.** Under (A2.1), T_b(H) is nonincreasing in every raising input and nondecreasing in
C*. Over a box of inputs, T_b(H; theta_fast) <= T_b(H; theta) <= T_b(H; theta_slow), where
theta_fast puts every raising input at its upper end and C* at its lower end, and theta_slow the
reverse. Both ends are attained, so the interval is exact.

*Proof.* If theta' is above theta in every raising input and not above it in C*, then
L_p(t; theta) <= L_p(t; theta') for all t, so the set of times where theta reaches its C* is
contained in the set where theta' reaches its own, and its infimum is no smaller. A minimum of
nonincreasing functions is nonincreasing. theta_fast dominates every point of the box, theta_slow is
dominated by every point. No continuity is needed. ∎

The interval takes two evaluations, not one per corner. **Corollary 2.2 (termwise).** Without
(A2.1), T_b(p; theta) is at least the first t at which the sum of each term's supremum over the box
reaches the lowest C*. *Proof:* each term is at most its supremum. ∎ **Corollary 2.3 (the cap
leak).** With physical compute fixed at a cap, drift at a constant log10 gamma a year and headroom
h = log10 C* - log10 C_cap, T_b = max(0, (h - J - S_v) / log10 gamma), C2's fixed-compute case.
*Proof:* solve L(t) = log10 C*. ∎

**Fails when.** An input raises one term and lowers another. The live case is scale dependence: if
the drift rate fell fast enough with scale, more chips could lengthen T_b and the two-corner
interval would miss. The evidence points the other way, since the largest efficiency gains are larger
at scale [@gundlach2025origin], but it is an assumption for E1 and E15 to test. With drift falling
with scale, `c2_monotone.py` found interior values outside the two-corner interval in 202 of 1,500
random boxes, while the termwise bound held in all.

**What is empirical.** The rest of C2: the expression, the drift rate and its scale dependence, J,
S_v, whether it beats a single multiplier (b) and the backtest (c), in E1, E15, E10, E18, E22 and E4.
"The minimum over paths matches C3's evader" is corrected by Proposition 1.5: each path's T_b is
compared with that path's T_r. *Checked* on 37,500 interior points in 1,500 random boxes (one to four
paths, growing fleets, drift rising with scale) and 1,500 cap leaks by `tools/formal/c2_monotone.py`;
no counterexample.

## C3. Detection as the evader sees it

Let q_c(p) be channel c's miss chance on path p over the path's window w(p) = T_b(p) - T_resp(p),
with q_c(p) = 1 when c does not watch p. A strategy sigma is a path with every evasion choice on it,
breaking a trust anchor included. (A3.1) Given the strategy, channels detect independently.

**Theorem 3.1 (the evader's maximum).** Under (A3.1): (a) the chance the evader's best strategy is
missed is P_miss = max over sigma of prod_c q_c(sigma), and no randomised strategy does better;
(b) for every path, the product over all channels is at most miss(p), the product over C(p), which
is at most P_miss; (c) if each channel's miss chance does not depend on the path it watches, with
every q_c > 0, the memo's product prod_c q_c equals P_miss iff every channel with q_c < 1 watches every
path.

*Proof.* (a) A mixture's miss chance is the average of the paths', at most the largest. (b) The
extra factors are at most 1. (c) Each miss(p) is at least the full product, so the maximum equals it
iff every miss(p) does, which with positive q_c means every channel outside C(p) has q_c = 1. ∎

Part (c) is C3(b). With disjoint channel sets this is Baker et al.'s weakest link
[@baker2025verifying]; the maximum over violation procedures is the inspection game's non-detection
game [@avenhaus2002inspection].

**Theorem 3.2 (common cause).** Let a latent Z (the state of a shared trust anchor, the tips from one
intelligence source, or the evader's randomisation) make channels independent given Z, with each
q_c(Z) nondecreasing in Z. Then E[prod_c q_c(Z)] >= prod_c E[q_c(Z)], and
max over z of prod_c q_c(z) >= E[prod_c q_c(Z)].

*Proof.* For nondecreasing f and g, (f(z) - f(z'))(g(z) - g(z')) >= 0; taking expectations over two
independent copies of Z gives E[fg] >= E[f] E[g] (Chebyshev's inequality). A product of nonnegative
nondecreasing functions is nonnegative and nondecreasing, so induction extends this to any number of
factors. A maximum is at least an average. ∎

Multiplying marginal miss rates therefore understates the miss twice over: by averaging over the
evader's choice instead of maximising, and by ignoring common cause. Inspections follow intelligence
tips [@baker2023nuclear], and channels resting on one hardware trust anchor fail together under one
break [@chuang2026teefail]: both are this case.

**Theorem 3.3 (merging).** Let channels on a path have detection times D_1, ..., D_n with any joint
law, and D = min_i D_i. Then Pr[D > t] <= min_i Pr[D_i > t]. If the D_i are positively upper-orthant
dependent, Pr[all D_i > t] >= prod_i Pr[D_i > t], then also Pr[D > t] >= prod_i Pr[D_i > t]. So with
constant marginal rates the merged rate, -ln Pr[D > t] / t, is at least max_i lambda_i under any
dependence, and at most sum_i lambda_i under positive dependence.

*Proof.* {D > t} is contained in each {D_i > t} (Fréchet's bound). The second part restates the
definition. Comonotone mixtures (Theorem 3.2 applied to the conditional survival chances) and common
shocks (Marshall and Olkin's model) are positively dependent. ∎

C3's merging rule, channels on one anchor or one tip source counted as one with the larger rate,
is therefore conservative under any dependence, not only positive, given that the rates are those
under the strategy the evader plays. That proviso is the catch. If breaking the anchor is open to the
evader, the group's rate on that strategy is zero, not the larger rate: the break belongs among the
paths, where the maximum of Theorem 3.1 takes it.

**Corollary 3.4 (the detection bound over breakout time, several channels).** Partition C(p) into
groups that are independent of each other given the strategy, with any dependence inside a group.
Then miss(p) <= exp(-Lambda_m(p) w(p)), with Lambda_m(p) the sum over groups of the largest rate in the
group, so T_d(p) <= ln(1/beta) / Lambda_m(p), and Proposition 1.5 holds with this T_d. *Proof:*
independence across groups multiplies the groups' survival chances; Theorem 3.3 bounds each. ∎

This is the memo's "combined chance of missing a secret program over its breakout time", restated so
that it holds. With one group per path it is the single-rate form, in which the memo's placeholder
channel needs [2.5 yr](numbers.md#def-placeholder-detect-time) to reach a 5% miss.

**Fails when.** Channels in different groups are dependent through a cause nobody listed; rates vary
with time (use Phi as in C1); the evader adapts after a channel fires short of a confirmed finding; a
strategy outside the set. A mature many-channel oversight system elsewhere catches about
[31%](numbers.md#org-fraud-detect) of frauds [@dyck2017pervasive], a reminder that independence is
the exception. **What is empirical:** the rates, the grouping and C3(c), in E5, E8 and E13.

**Prior work and ours.** Fréchet bounds, Chebyshev's inequality and positive dependence are
textbook; path-level detection is safeguards practice [@allen-2015-llnl; @iaea-glossary-2022].
Possibly ours, narrowly: these results as the rule for combining AI verification channels. *Checked*
on 4,000 channel-path structures, 13,998 arbitrary joint laws on grids, 3,894 common-shock models and
4,000 grouped structures by `tools/formal/c3_evader.py`; no counterexample.

## C4. The loop-gain estimator

**Model (A4.1).** Rounds have a fixed length tau and budget. Within round k, du/dt = theta e^(-b u)
E_k^lambda, with the input fixed for the round at E_k = c e^(e u_k): closure e, and e = 0 for a fixed
researcher, as in a staged run with a fixed agent. K = e lambda / b. Write x_k = b Delta_k.

**Lemma 4.1 (the round identity).** Under (A4.1), exactly,
ln[(e^(x_(k+1)) - 1) / (e^(x_k) - 1)] = b (K - 1) Delta_k.

*Proof.* With y = e^(b u) the round's law is dy/dt = b theta E_k^lambda, constant within the round,
and E_k^lambda = c^lambda y_k^K. So y_(k+1) = y_k + gamma y_k^K with gamma = b theta tau c^lambda, and
e^(x_k) - 1 = y_(k+1) / y_k - 1 = gamma y_k^(K-1). The ratio of consecutive rounds is
(y_(k+1) / y_k)^(K-1) = e^(b (K - 1) Delta_k). ∎

**Corollary 4.1a (the claim's form).** ln(Delta_(k+1) / Delta_k) = b (K - 1) Delta_k -
[f(x_(k+1)) - f(x_k)], with f(x) = ln((e^x - 1) / x), and |f(x_(k+1)) - f(x_k)| lies between
b |Delta_(k+1) - Delta_k| / 2 and b |Delta_(k+1) - Delta_k|. *Proof:* ln(e^x - 1) = ln x + f(x), and
f'(x) = e^x / (e^x - 1) - 1/x rises from 1/2 toward 1 (f'' > 0 because 2 sinh(x/2) > x). ∎ With a
fixed researcher the leading term is -b Delta_k, the claims file's identity: it holds to first order,
with an error that is a known fraction of the change between rounds. The exact form costs nothing,
since b is fitted anyway.

**Lemma 4.2 (lambda from budgets).** From a fixed start, ln(e^(b Delta_0(E)) - 1) = lambda ln E +
const for an agent budget E. *Proof:* e^(x_0) - 1 = b theta tau E^lambda / y_0. ∎ Budgets of one, two
and four times give lambda exactly in the model, and r = lambda / b.

**Proposition 4.3 (g_k is not a stationary parameter).** Under (A4.1): (a) Delta_(k+1) > Delta_k iff
K > 1, so g_k > 1 iff K > 1, exactly; (b) if K < 1, then g_k < 1 in every round, Delta_k tends to 0,
g_k tends to 1, and the level is unbounded, u_k >= ln(y_0 + k gamma y_0^K) / b; (c) so a trigger
that fires when g_k, or its upper bound, exceeds a fixed g* < 1 fires on every subcritical loop that
runs long enough, however precisely g_k is measured, and the geometric total Delta_0 / (1 - g) is not
a bound in this model.

*Proof.* (a) By Lemma 4.1 the sign of x_(k+1) - x_k is that of K - 1. (b) y rises, so
y_(k+1) - y_k = gamma y_k^K >= gamma y_0^K and y_k >= y_0 + k gamma y_0^K. Then e^(x_k) - 1 =
gamma y_k^(K-1) tends to 0, and g_k = (x_(k+1) / x_k), which equals the identity's ratio times
e^(f(x_k) - f(x_(k+1))), tends to 1. (c) follows. ∎

This bears on C4(c) and on D2. The claims file triggers when "the upper bound on g exceeds a margin
g* below 1" and reads the corrected median r, [0.63](numbers.md#dyn-r-lm-corrected), as a per-round
ratio whose rounds sum to [2.7](numbers.md#path-rsi-multiplier-median) times the first. In the common
form the claim itself uses, r is not a per-round ratio: to first order g_k = exp(b (K - 1) Delta_k),
which depends on the round's size and tends to 1 for every subcritical loop. The geometric total
needs a constant ratio, which the common form does not produce; the pathways chapter already calls
the 2.7 an illustration. In `c4_identity.py`, a perfectly measured g_k passed 0.9 within twelve
rounds in each of 200 seeded subcritical instances (K from 0 to 0.95). The stationary quantity is K,
equivalently the slope b (K - 1) of ln g_k against Delta_k. The trigger should be "the upper bound on
K exceeds K* < 1", with K estimated from Lemma 4.1 in a closed-loop run, or as the product of
separately measured factors (Proposition 4.5), which the claim already describes.

**Proposition 4.4 (which bound binds).** Let U_alpha satisfy Pr_K[U_alpha >= K] >= 1 - alpha for
every K. The rule "restrict while U_alpha > K*" leaves a loop with K > K* unrestricted with
probability at most alpha; the rule on a lower bound controls false alarms at K <= K* and leaves misses
uncontrolled. *Proof:* if K > K*, Pr[U_alpha <= K*] <= Pr[U_alpha < K] <= alpha; the lower bound is
symmetric. ∎ Textbook (tests and confidence intervals are dual). It settles Part I's dispute in the
direction the claims file chose; its price, false alarms below K*, falls only as rounds narrow the
interval (E4(c)).

**Proposition 4.5 (combining factors).** If K = prod_i f_i with nonnegative factors and
Pr[U_i >= f_i] >= 1 - alpha_i, then Pr[prod_i U_i >= K] >= 1 - sum_i alpha_i. *Proof:* the union bound,
and the product rises in each nonnegative factor. ∎ The delta method is narrower but only
asymptotic; at five rounds the Bonferroni product is the one with a guarantee.

**Proposition 4.6 (errors in variables).** If each Delta_k is measured with independent error of
variance sigma^2, small against Delta_k, and the slope is fitted through the origin of
ln(Delta_hat_(k+1) / Delta_hat_k) on Delta_hat_k, then to first order the response carries
-epsilon_k / Delta_k and the regressor +epsilon_k, with covariance -sigma^2 / Delta_k, which biases the
slope b (K - 1) down: the loop looks more subcritical than it is, the unsafe direction here. Measuring
each round's gain on two independent held-out sets, one for the regressor and one for the response,
removes that term, leaving attenuation toward K = 1 and a second-order term in sigma^2 / Delta^2.
*Proof:* expand ln(Delta + epsilon) to second order and take expectations term by term. ∎ This is
first order; `c4_identity.py` shows the sign in simulation and does not assert it.

**What is empirical.** Coverage of the interval within [5 rounds](numbers.md#claim-d2-rounds)
(E4(c)); whether real runs put K on one side of 1 (E4(a), E4(b)); transfer from small runs to the
frontier; sandbagging [@gasteiger2025subtlesandbag]; and whether (A4.1), an input fixed within each
round, describes a research loop at all.

**Prior work and ours.** The semi-endogenous form is Jones's, as used by [@bloom2020ideas] and
[@besiroglu2024returns]; the loop gain and its threshold are [@cunningham2026rsi] and
[@burtsev2026criticality]. Lemma 4.1 and Proposition 4.3 are elementary; we did not find them stated,
which is a claim about our search. *Checked* on 3,544 consecutive rounds from 600 runs integrated
numerically (not from the closed form), 600 budget ladders and 200 subcritical runs of 100,000 rounds
by `tools/formal/c4_identity.py`; no counterexample.

## C5. Miss and false-alarm rates with exact bounds

(A5.1) The n organisms are an independent sample from a stated population (builders, methods,
locks), built after E is fixed by builders blind to it.

**Theorem 5.1 (exact one-sided bound).** Let X be the number missed, and U(x, n) the p with
Pr[Bin(n, p) <= x] = alpha (U = 1 if x = n). Then Pr_p[U(X, n) >= p] >= 1 - alpha for every p. With no
misses U = 1 - alpha^(1/n), at most a target p_T iff n >= ln(alpha) / ln(1 - p_T): at
[90%](numbers.md#claim-confidence) and a [10%](numbers.md#claim-d5-miss-target) target,
[22 organisms](numbers.md#claim-d5-organisms). One miss raises it to
[38 organisms](numbers.md#formal-d5-organisms-one-miss), two to
[52 organisms](numbers.md#formal-d5-organisms-two-miss).

*Proof.* F_p(x) = Pr_p[X <= x] is continuous and decreasing in p, so U(x) < p iff F_p(x) < alpha. With
x_p the largest x for which F_p(x) < alpha, Pr_p[U(X) < p] = F_p(x_p) < alpha. ∎ Textbook (Clopper and
Pearson). The false-alarm rate on benign models has the same bound; on disjoint samples the two hold
together with probability at least (1 - alpha)^2.

**Proposition 5.2 (a sequential test for absence).** Fix 0 <= p_1 < p_T and let
M_n = prod over i <= n of (p_1 / p_T)^(Y_i) ((1 - p_1) / (1 - p_T))^(1 - Y_i), with Y_i = 1 if organism
i is missed. Declaring "miss rate below p_T" once M_n >= 1/alpha errs with probability at most alpha
under every p >= p_T, for any stopping rule. With p_1 = 0 and no misses it stops at Theorem 5.1's
count.

*Proof.* Under p the expected factor is p p_1 / p_T + (1 - p)(1 - p_1) / (1 - p_T): linear in p, 1 at
p_T, and decreasing because p_1 / p_T < (1 - p_1) / (1 - p_T). So for p >= p_T, M is a nonnegative
supermartingale from 1, and Ville's inequality gives Pr[sup M_n >= 1/alpha] <= alpha. With p_1 = 0
and no misses, M_n = (1 - p_T)^(-n). ∎ Textbook (Ville; Wald's sequential test).

**Proposition 5.3 (what the guarantee covers).** If a share epsilon of the organisms the regime will
face is of a kind not in the sample, the miss rate it faces differs from the tested rate by at most
epsilon. *Proof:* p_mix = (1 - epsilon) p_tested + epsilon p_other. ∎ That is the formal content of
"the guarantee holds only for the population tested". A tamper-resistant organism that still recalled only
[7.8%](numbers.md#def-robust-hard-recall) on hard tasks after weak-to-strong fine-tuning
[@finke2026robustorganisms] is such a kind, and C5(c) already expects to fail on it.

**What is empirical.** Whether the organisms match a determined developer's, whether an affordable
budget meets both targets on RL-locked organisms (E3), the range where E's methods work, and gradient
hacking [@hubinger2023trusteval]. The organism method is prior work [@greenblatt2024password;
@taylor2025auditinggames; @finke2026robustorganisms]. *Checked* exactly (no simulation) for p
from 1/400 to 399/400 in steps of 1/400, n from 1 to 60 and alpha of 10%, 5% and 1%, and Ville's test
over 300 organisms by dynamic programming, by `tools/formal/c5_binomial.py`; no counterexample.

## C6. The coupled-gain certificate and the runaway condition

**Lemma 6.1 (textbook).** For real square matrices: (a) 0 <= A <= B entrywise implies
rho(A) <= rho(B); (b) rho(A) <= rho(|A|); (c) for B >= 0 and w > 0,
min_i (Bw)_i / w_i <= rho(B) <= max_i (Bw)_i / w_i, so the smallest and largest row sums bracket
rho(B); (d) for B >= 0, rho(B) >= max_i B_ii, and rho(B) is at least the geometric mean of the weights
on any cycle.

*Proof.* Gelfand's formula, rho(A) = lim ||A^k||^(1/k), with the max-row-sum norm, which rises with
the entries' absolute values. (a) and (b): |A^k| <= |A|^k <= B^k entrywise. (c): rho(B) =
rho(D^(-1) B D) with D = diag(w), whose row sums are (Bw)_i / w_i; for the lower bound, Bw >= mu w gives
B^k w >= mu^k w, so ||B^k|| >= mu^k min w / max w. (d): B dominates the matrix holding only a cycle's
edges, whose L-th power, for a cycle of length L, is diagonal on the cycle with the cycle's product. ∎ (Perron and Frobenius; Collatz and
Wielandt.)

**Theorem 6.2 (the certificate).** If the bounds |K_ij| <= U_ij hold jointly with probability at
least 1 - alpha (for instance each with error alpha_ij, the alpha_ij summing to at most alpha), then
with that probability rho(K) <= rho(U) <= max_i (Uw)_i / w_i for every w > 0, and
rho(U) <= max_i sum_j U_ij. *Proof:* the union bound and Lemma 6.1 (b), (a), (c). ∎

K need not be nonnegative for the certificate. Part I left the signed case open
([Y3](013-dynamical.md#y3-coupling)); Lemma 6.1(b) closes it for the certificate. What stays open is
whether rho(K) > 1 is the explosion condition when couplings are negative: Theorem 6.4 needs K >= 0.
The weighted bound reaches rho(U) itself when U is irreducible, so E11 should compute rho(U), with row
sums as a quick, looser check.

**Corollary 6.3 (C6(c)).** Cutting or weakening off-diagonal edges cannot take rho(U) below
max_i U_ii. With the software loop's own gain at its corrected 95th percentile,
[1.07](numbers.md#dyn-r-lm-hi-corrected), rho(U) is at least that, above 1, whatever the cross-feeds;
no set of edge cuts issues the certificate at that confidence, and only gating the software loop's own
closure can. *Proof:* Lemma 6.1(d). ∎ This is the headroom of
[-0.07](numbers.md#dyn-software-headroom-upper), restated so that it does not depend on the row-sum
form.

**The smallest cut set (C6(b)).** f(S) = rho(U with the edges in S cut) is nonincreasing in S, so a
smallest set reaching rho* exists, and a search over sets by size finds it. Cutting greedily, largest
single drop first, is not enough: it needed more cuts than the smallest set in 12 of 296 random
four-loop instances. With a handful of named edges, exhaustive search is cheap.

**Theorem 6.4 (the runaway condition for coupled loops).** Let du_i/dt = theta_i exp(-b_i u_i +
lambda_i sum_j e_ij u_j), u(0) = 0, with theta_i, b_i, lambda_i > 0 and e_ij >= 0, K_ij = lambda_i e_ij
/ b_i and a_i = b_i theta_i.
(i) If rho(K) > 1, let w >= 0, summing to 1, be a left Perron vector of M = D K D^(-1), D = diag(b).
Then sum_i w_i b_i u_i(t) >= -ln(1 - a_min (rho - 1) t) / (rho - 1), a_min = min_i a_i, so some u_i
diverges no later than 1 / (a_min (rho - 1)).
(ii) If rho(K) < 1, let v > 0 be a right Perron vector of a positive matrix M_tilde >= M with
rho(M_tilde) = rho_tilde < 1 (M itself if positive). Then N(t) = max_i b_i u_i(t) / v_i <=
ln(1 + a c t) / a, with a = (1 - rho_tilde) min_i v_i and c = max_i a_i / v_i: every u_i grows at most
logarithmically, every stock at most polynomially, in t.

*Proof.* With z_i = b_i u_i, dz_i/dt = a_i exp(((M - I) z)_i), M_ij = lambda_i e_ij / b_j, and M is
similar to K. (i) With w'M = rho w' and V = w'z: dV/dt = sum_i w_i a_i exp(y_i), y = (M - I) z, which is
at least a_min exp(sum_i w_i y_i) by Jensen, = a_min exp((rho - 1) V). Compare with the solution of
V' = a_min e^((rho - 1) V) from 0. (ii) If N > 0 then z <= N v, so M z <= N M_tilde v = N rho_tilde v;
where z_i = N v_i, y_i <= -(1 - rho_tilde) N v_i <= -a N. The upper Dini derivative of a maximum is at
most the largest derivative among the indices attaining it, so D+N <= c e^(-a N); integrate from
N(0) = 0. ∎

This is Davidson et al.'s Proposition 1, explosive growth iff the spectral radius exceeds 1
[@davidson2026feedback], in Part I's normalisation, with explicit bounds on the time to blow-up and
on subcritical growth; Burtsev states the cross-actor version [@burtsev2026criticality]. For one loop
(i) is exact, the dynamical chapter's t* = 1 / (g_0 b (K - 1)). At rho(K) = 1 neither part applies.
The model has no ceiling: physical headroom stops a supercritical loop first.

**Corollary 6.5 (time to a distance).** Under (ii), u_i reaches D no earlier than
(exp(a b_i D / v_i) - 1) / (a c). *Proof:* invert the bound at N = b_i D / v_i. ∎
**Corollary 6.6 (the drift margin).** If rho(K(t)) rises at most at rate rho_dot, a certificate
rho(U) <= 1 - m rho_dot T_r keeps rho(K) <= 1 for at least m T_r. *Proof:* rho(K(t)) <= rho(U) +
rho_dot t. ∎ That is Part I's rho*; rho_dot is unmeasured.

**Fails when.** The bounds are not jointly valid, for instance because parties report their own
edges; couplings are negative and Theorem 6.4 does not apply; inputs are not log-linear in the stocks;
an unmeasured edge enters as a stated range, which is not a confidence bound. **What is empirical:**
every entry of U (E9, E4, E10, E6, E11) and the drift rate. Burtsev's blocs, each subcritical alone,
reach a network rho of [1.15](numbers.md#dyn-burtsev-network-rho): diagonal entries below 1 do not
bound rho, which is why the certificate uses rho(U) or row sums. *Checked* on 6,020 matrix pairs (nonnegative
and signed, one to six loops, and edge cases including zero, periodic, Jordan, nilpotent and
reducible matrices), with spectral radii from Gelfand's formula self-tested against closed forms, by
`tools/formal/c6_certificate.py`; and on 150 supercritical systems (checked level by level in time)
and 150 subcritical ones integrated numerically by `tools/formal/c6_runaway.py`; no counterexample.

## C7. The coalition share

(A7.1) A coalition pools chips with share s of the accounted fleet; the fleet F(t), the efficiency
multiplier A(t) and utilisation u are given; breakout needs a budget B, overhead included;
I(t) = integral from 0 to t of F r u A.

**Proposition 7.1.** T_b(s) = inf{t : s I(t) >= B} is nonincreasing in s, and T_b(s) >= m T_r iff
s I(m T_r) <= B. So s* = min(1, B / I(m T_r)). At a fixed fleet and algorithms, T_b(s) = h_w / s with
h_w = B / (F r u), and s* = min(1, h_w / (m T_r)). *Proof:* I is continuous and increasing, so
s I(t) < B for every t < m T_r iff s I(m T_r) <= B. ∎

This is the hardwired-pause fleet threshold [@fithian2026hardwired] solved for the share, with the
horizon set to m T_r instead of chosen. At that paper's inputs h_w is
[7.8 years](numbers.md#claim-whole-fleet-horizon), so (C7(c)) the overt constraint binds only once
m T_r exceeds it. Growth and drift keep the closed form and only lower s*. By Proposition 1.5, each
path has its own T_r and so its own s*.

**The game.** Members i of a coalition with share s may comply or join a joint breakout. Before
success any member may report; a report halts the breakout, pays the reporter R_i and spares it the
penalty. An unreported breakout succeeds with probability pi(s), the S of the coalition's path, paying
V_i, or is caught, costing P_i. Complying pays 0. A deviation is self-enforcing if no member prefers
to report. In the sense of [@bernheim1987coalition], as restated in [@ali2019coalitions], compliance
is coalition-proof against a class of coalitions if none in it has a deviation that is profitable for
every member and self-enforcing.

**Theorem 7.2.** Under (A1.1), (A1.2) and (A7.1), parts (i) and (ii) hold for every share with
T_b(s) >= T_r, which at fixed algorithms is every s <= h_w / T_r (that is, m s* when s* < 1).
(i) If R_i > beta V_i for every member of a coalition of two or more, every member strictly prefers
reporting, so no such deviation is self-enforcing.
(ii) If beta V_i <= (1 - beta) P_i for a party, no breakout profits it, alone or in company.
(iii) For every share with T_b(s) < T_r, pi(s) > beta, and payoffs with V_i > (R_i + (1 - pi) P_i) / pi
make the deviation profitable and self-enforcing.

*Proof.* T_b(s) >= T_r gives pi(s) <= beta by Lemma 1.1. (i) Staying pays
pi V_i - (1 - pi) P_i <= beta V_i < R_i. (ii) That payoff rises with pi, so it is at most
beta V_i - (1 - beta) P_i <= 0. (iii) Lemma 1.1 gives pi > beta, and the stated V_i make staying worth
more than R_i and more than 0. ∎

C7(b) as stated is false. Its first half holds under (i) or (ii). Its second half, that some
coalition above s* has a profitable self-enforcing deviation, fails on the interval from s* to m s*,
where T_b(s) is still at least T_r and (i) or (ii) still excludes every deviation; `c7_coalition.py`
sampled 8,936 such shares. The margin makes s* conservative by design. In a model with exact
estimates, a deviation becomes possible only above h_w / T_r, and whether one exists there depends on
payoffs. Corrected: no coalition with T_b(s) >= T_r, in particular none at or below s*, has a
profitable self-enforcing deviation when R_i > beta V_i for every member and beta V_i <= (1 - beta) P_i
for single parties; above h_w / T_r payoffs exist that make one; and s* keeps the first statement
when the estimates err within e_b e_r <= m (Proposition 1.2).

**Fails when.** The reward condition asks for more than beta times the value of a decisive
advantage, which no fund pays to a state. The reporters that matter are individuals inside members,
whose own stake is small, but a state can compartmentalise and coerce its insiders [@hoffman-2009],
and whistleblowers whose identity became known were usually fired or pushed out [@dyck2007whistle];
with a retaliation cost Q_i, (i) needs R_i - Q_i > beta V_i. A single state has no partner to report it,
only insiders. Non-members are outside the game, and without a penalty on outsiders stable coalitions
are small [@nordhaus2015climate]. Against a coalition that includes a major power no response may
halt anything, T_resp is unbounded and the theorem is empty. The payoffs are one-shot; E6 tests
repeated play. **What is empirical:** V, P, R and Q (Gan says of his own payoffs that no evidence
guides them [@gan2026clock]), the fleet, E6 and E22.

**Prior work and ours.** Coalition-proofness [@bernheim1987coalition; @ali2019coalitions], fleet
thresholds [@fithian2026hardwired], rewarded reporting [@dyck2007whistle]; the derivation of the share
from T_r was sketched by the survey ([the novelty file](03-novelty.md#the-coalition-compute-threshold)).
Possibly ours: the reward condition and the correction that m s*, not s*, is where deviation becomes
possible. *Checked* on 20,000 fleets with and without growth and drift and 20,000 games of one to six
members by `tools/formal/c7_coalition.py`; no counterexample.

## C8. The footprint floor, as a bound

**Theorem 8.1.** Let a run of C useful operations finish within T on chips with peak rates r_j and
achieved utilisations u_j(t). If every u_j(t) <= u_bar, the chip count in units of a reference peak,
sum_j r_j / r_bar, is at least N_min = C / (r_bar u_bar T). If every chip spends at least e_min per
useful operation, the energy is at least E_min = C e_min. *Proof:* C = sum_j (integral of r_j u_j over
the run) <= u_bar T sum_j r_j, and E = sum_j e_j C_j >= e_min C. ∎

This makes C8's L2 correction precise. N_min is a bound only when u_bar bounds every utilisation an
adversary can reach, e_min the best energy per operation of any chip it can use, and T the longest run
it will accept. The physical chapter's floors use a reference utilisation of
[40%](numbers.md#phys-util-ref), so they are estimates, above the bound by a factor of
[2.5](numbers.md#formal-floor-ref-over-bound). For [1e+26 FLOP](numbers.md#phys-rahman-1e26-local)
over a pause's longest sensible run the estimate is
[4,000 H100e](numbers.md#phys-floor-chips-1e26-pause); the bound at full utilisation is
[1,600 H100e](numbers.md#formal-floor-bound-1e26-pause), and at the highest utilisation in the ledger,
[76%](numbers.md#phys-pope-mfu-prefill) (a vendor figure for large-batch input processing),
[2,100 H100e](numbers.md#formal-floor-mfu-1e26-pause). Counted in H100-equivalents by peak, the bound
holds for any chip mix. T is not physics: it is the longest sensible run under prevailing growth
rates [@rahman2026], an assumption about the adversary, and a patient one lowers every floor in
proportion.

Three consequences. A channel's margin, its detection limit over the floor it sees, is understated by
an estimated floor, so C8(b)'s falsifier ("every facility channel's margin exceeds one") becomes
easier to meet once the bound is used. The untraced pool exceeds the bound by more than it exceeds
the estimate, [412](numbers.md#formal-pool-over-floor-bound) times against
[165](numbers.md#claim-pool-over-floor-pause), so C8(c) is strengthened. And **Lemma 8.2**: a pool of
at least N_min chip-equivalents running at u_bar can finish C within T (*proof:* N_min r_bar u_bar T = C ∎). With
Proposition 1.5, a covert path using the pool meets the line only if its own T_b exceeds m T_r on that
path, where T_d at the historical rate is [37 years](numbers.md#path-covert-td-prevent); at fixed
algorithms that asks that N_pool r_bar u_bar m T_r fall short of C*, a reserve unable to reach C* in
decades. That is the formal content of C8(d).

**Fails when.** A chip delivers more useful operations than its counted peak suggests (lower
precision counted at a higher rate), utilisation exceeds u_bar, or the run is longer. **What is
empirical:** each channel's detection limit (E8, E13), the pool (modelled, never counted), and the
distribution tax (E14). The inequality is elementary; the framing is [@rahman2026],
[@koopmanschap2026gpu] and [@scher2025]. *Checked* on 20,000 random runs of up to 40 chips with mixed
peaks and piecewise utilisation by `tools/formal/c8_floor.py`; no counterexample, while a floor at a
typical utilisation below the highest was undercut in 2,184 of them, the reason for the correction.

## C9. The height-clocked licence

**Model.** A licence names the hash of block k (P1) and an expiry height H_e = k + L (P2), is signed
by its licensors, and carries a proof that it is a leaf of a log root anchored in a block at least d
deep (P3, P4). The chip keeps h_max, the greatest valid height it has seen (never decreasing), the
header chain with the most work it has seen, and a counter t of its own powered time.

**Assumptions.** (A9.1) The hash is collision resistant and acts as a random oracle for proof of work;
the chip accepts a header only if its hash is at most a largest target Z it enforces, a minimum work
per header. (A9.2) Observers who wait for d confirmations agree on the chain to that depth, the
common-prefix property of a chain whose honest miners hold most of the hash power. (A9.3) The chip's
secure element is intact: keys, counter and rule as specified, the counter's rate within a known factor
of real powered time. (A9.4) Every leaf behind every anchored root is published. Each can be wrong;
(A9.3) fails for every chip at once if one trust anchor breaks [@chuang2026teefail].

**Proposition 9.1 (P2, corrected: a bounded compute budget).** Under (A9.3) alone, with the rule
"stop once h_max >= H_e, or once h_max < k + rho_min (t - t_l) - s" (t_l the counter at acceptance,
rho_min a floor on the block rate per unit of counter time, s a slack in blocks), the chip runs under
the licence for at most (L + s) / rho_min of counter time, whatever headers it is fed. Fed the honest
chain and kept on, it stops when block H_e arrives, or earlier if the honest chain falls behind the
floor. *Proof:* while running, k + rho_min (t - t_l) - s <= h_max < k + L. ∎

The rule in the claim, stop after "no headers showing progress for longer than a local bound", fails
P2. A holder who feeds one header, real or mined, just inside each local bound tau keeps the chip
running for about L tau of counter time against a nominal L block intervals, a stretch of tau over the
block interval, which `c9_clock.py` reproduces in every run. Two costs remain with the rate floor. A
floor close to the honest rate stops compliant chips early when blocks come slowly (112 of 649 honest
runs at the check's random settings); a lower one stretches the budget by up to the honest rate over
the floor. And P2 now bounds powered time, not calendar time: a chip kept offline across its expiry,
then fed the old headers at the floor rate, spends its remaining budget late. That is flexHEG's
idle-chip weakness, leaving a chip idle "to save up usage time" [@petrie2025flexheg2], which the height
clock answers only when honest headers reach the chip. Offline, it needs a trusted real-time clock or a
fresh challenge, L4's third objection.

**Lemma 9.2 (the cost of forged headers).** Under (A9.1), n accepted headers that are not on the
honest chain cost at least n 2^256 / (Z + 1) hash evaluations in expectation. *Proof:* each evaluation
succeeds with probability at most (Z + 1) / 2^256, independently. ∎ Forged headers gain nothing
against Proposition 9.1, since they too raise h_max toward H_e. They matter against P1 and P4 (a
private block hash, a fake anchor), and this prices them. Enforcing Z stops a private chain from
driving its difficulty down through Bitcoin's retargeting.

**Proposition 9.3 (P1, no advance signing).** Under (A9.1), a licence produced before block k was first
computed names its hash with probability at most q / 2^256 after q attempts. *Proof:* until computed,
the hash is uniform and unknown. ∎ A licensor colluding with a holder can still name a block they mined
privately; the chip accepts it only on a chain it has been fed, at Lemma 9.2's cost, and drops it,
voiding the licence, once it sees the honest chain's greater work. Signing by k of n with one honest
signer, who names only blocks on the honest chain, closes that route.

**Proposition 9.4 (P3 and P4).** Under (A9.1) and (A9.2), with log roots anchored in the chain and
consecutive roots linked by consistency proofs, every auditor sees the same logged licences and
declarations in the same order: no split view survives d confirmations. Under (A9.4) as well, the
licences a chip can accept are exactly the logged ones, so an audit that finds no licence for a chip
and period proves that none was issued. *Proof sketch:* a root binds its leaves (two leaf sets with
one root give a collision); consistency proofs bind each anchored root to the next [@laurie2013ct];
(A9.2) gives every auditor the same anchored roots, hence the same leaves; a chip accepts only a
licence with an inclusion proof against an anchored root, and under (A9.4) every leaf is published. ∎

Without (A9.4), P4 fails: a log can anchor a root over a leaf it never publishes, and a chip will
accept that licence while no auditor can see it. Committing to the tree's size makes withholding
detectable, not attributable to a chip. The claim must state (A9.4), and the regime must treat a log
that withholds any leaf as having licensed every chip. Not claimed: that sealing makes a declaration
true [@fang2023polbroken]. Bitcoin time is accurate to hours [@todd2016opentimestamps], so periods of
weeks or longer.

**Prior work and ours.** A chip nonce stops advance signing online [@petrie2024offline]; blockchain
time and transparency logs are established [@gipp2015timestamping; @todd2016opentimestamps;
@laurie2013ct]. P3 and P4 answer problems flexHEG leaves open [@petrie2025flexheg1;
@aarne2025flexheg3] only under (A9.2) and (A9.4). *Checked* on 3,000 runs against minimal, random,
burst, withholding and honest delivery by `tools/formal/c9_clock.py`; no counterexample to
Proposition 9.1. P1, P3 and P4 are reductions to (A9.1) and (A9.2), which a check cannot test.

## C10. Superintelligence at matched budget: what is empirical

C10 is a definition, which needs no proof. Its formal content is that t* is well defined.

**Proposition 10.1.** Let kappa(t) be the system's score over the organisation's at matched budget t.
If ln kappa is continuous and strictly decreasing in ln t and crosses 0 within the tested range, the
t* with kappa(t*) = 1 is unique, and interpolating ln kappa linearly in ln t between the bracketing
budgets gives a value inside the bracket, exact when ln kappa is linear in ln t. Without monotonicity,
define t* as the largest tested crossing, sup{t : kappa(t) >= 1}, the conservative choice for a
prevention line. If kappa >= 1 at the largest budget tested, t* is censored above and reported as a lower bound, never
extrapolated. *Proof:* the intermediate value theorem; strict monotonicity gives uniqueness. ∎

RE-Bench's ratio, which moves toward humans by [1.68](numbers.md#cog-rebench-swing-per-doubling) per
doubling of the budget [@wijk2024rebench], is the monotone case. The interval comes from resampling
tasks and recomputing t*. **Empirical:** whether the verdict is stable when the organisation changes
within its class, whether the fraction won rises smoothly with compute, and whether t* is estimable and
rises without saturating (E21, E2, E1). *Checked* on 20,000 random ratio curves by
`tools/formal/c10_crossover.py`; no counterexample.

## C11. Closure by input: the combination rule

Let one round's research output F(x_1, ..., x_n) be nondecreasing in each input. A gate of strength g_i
on input i removes the ungated share, so x_i becomes x_i (1 - g_i). f_S is the output with gates on the
set S over the output with none.

**Theorem 11.1 (one round's output).** (a) f_S <= min over i in S of f_i, for every F. (b) f_S =
prod over i in S of f_i, for all inputs, gate strengths and sets, iff ln F is additively separable in
the gated inputs; Cobb-Douglas is the case. (c) If ln F is supermodular in (x_i, x_j) (complements),
f_ij >= f_i f_j: the product overstates what two gates remove. If it is submodular (substitutes),
f_ij <= f_i f_j. For CES, F = (sum_i a_i x_i^q)^(1/q), the cross-partial of ln F has the sign of -q:
complements for q < 0, substitutes for q between 0 and 1; Leontief with every input binding gives
f_S = min f_i.

*Proof.* (a) More gates lower every input. (b) The product rule for pairs says g = ln F has zero mixed
differences, g(x_i', x_j') - g(x_i', x_j) - g(x_i, x_j') + g(x_i, x_j) = 0; fixing a base point,
g(x_i, x_j) = g(x_i, x_j0) + g(x_i0, x_j) - g(x_i0, x_j0), which is separable; the converse is direct.
(c) Supermodularity compares the same four points with the opposite sign. For CES the cross-partial of
ln F is -q a_i a_j x_i^(q-1) x_j^(q-1) / (sum_k a_k x_k^q)^2. ∎

The claims' L2 plan is therefore right for one round's output: per-input factors multiply under
Cobb-Douglas, and not when one input binds or inputs substitute. But C11(a) concerns the gain the loop
transmits, the exponent K, and there the rule differs.

**Theorem 11.2 (the loop gain).** In the common form with inputs supplied by the stock,
E_i = c_i X^(e_i), aggregated by CES with weights summing to 1, the loop's local gain is
(lambda / b) times d ln E / d ln X = (lambda / b) sum_i s_i(X) e_i, with s_i(X) = a_i E_i^q /
sum_k a_k E_k^q, each input's share of the aggregate. It lies between (lambda / b) min_i e_i and
(lambda / b) max_i e_i at every X. Under Cobb-Douglas the shares stay at a_i and K = (lambda / b)
sum_i a_i e_i. As X grows, K tends to (lambda / b) max_i e_i for substitutes and to (lambda / b) min_i e_i
for complements. *Proof:* differentiate ln E = (1/q) ln sum_k a_k c_k^q X^(q e_k); the shares
concentrate on the largest q e_k. ∎

Three things follow. Under Cobb-Douglas, gating input i lowers K by (lambda / b) a_i e_i: closures
add, they do not multiply, so a product of per-input factors is wrong for the gain even where it is
right for output. Under complements, which is what the evidence that algorithms complement compute
suggests [@gundlach2025origin; @whitfill2025bottlenecks], the input with the least closure comes to
set the gain, and a gate on it holds the loop as it grows. Under substitutes the input with the most
closure comes to set it, and every highly closed input must be gated, the case for holding every
input together [@scher2026research]. With the production function unknown, the safe bound is (lambda / b) times the
largest closure among ungated inputs. E4(d), gating inputs one and two at a time, decides which case
holds; until it does, the claim should name the maximum as its combination rule. One assumption to
flag: D6 defines e_i as the share of increments obtained without a gate, the common form as an
elasticity of the input to the stock, and reading one as the other is for E4(d) to check. Part (b),
narrow optimisers inside the loop, is empirical (E4(e)). *Checked* on 20,000 CES functions
(Cobb-Douglas, complements, substitutes, Leontief) with random gates and 10,000 local gains by finite
differences, by `tools/formal/c11_closure.py`; no counterexample.

## C12. The ranking: what can be proved

The ranking is a judgement on evidence, not a theorem. Two statements bear on it.

**Necessity and sufficiency within a horizon.** By Corollary 6.5, if cutting a pathway's loops leaves
rho(K) < 1, a stock needs at least the time (exp(a b_i D / v_i) - 1) / (a c) to grow by D, exponential in the
distance: the pathway is necessary within horizon T_h, in the pathways chapter's practical sense, if
this exceeds T_h for the distance to C*. By Theorem 6.4(i), a set of loops that alone has rho > 1, with
headroom beyond the distance, reaches any level within 1 / (a_min (rho - 1)): sufficient in that time,
in the model. Supply routes act through the line rather than through loops, and Proposition 1.5 is their test: a
route is sufficient if on its path T_b(p) < m T_r(p).

**Proposition 12.1 (what evidence alone can order).** Score pathways on several criteria. If A scores
above B on one and below on another, then among linear rankings with positive weights some put A
first and some put B first. *Proof:* move the weight toward either criterion. ∎ Without weights, only
Pareto-ordered pairs are fixed by the evidence; every other order is a judgement a red team can
reverse. The pathways chapter names its three weakest order judgements (distillation against declared
scaling, self-replication against continual learning, and the tie at the top); L4 should begin by
listing which pairs are Pareto-ordered. **Empirical:** everything else (E4 and E5 decide the tie; E1,
E15, E18, E10, E19, E7, E2). That a student gains nothing beyond its teacher, distillation's ceiling,
is an empirical assumption, not a theorem.

## Compliance as an equilibrium: inspection games with no known last period

The memo asked when compliance is each party's best response. The answer has a textbook core and one
feature specific to AI: a breakout ends the game. Each period a member complies, worth w > 0, or
attempts a breakout, which succeeds with probability pi (worth V) or is caught (costing P);
dev = pi V - (1 - pi) P.

**Theorem E.1 (no known last period).** If the regime continues with probability delta each period
and has no known last period, complying in every period is a subgame-perfect best response, against
a regime that continues while the party complies, iff w / (1 - delta) >= dev. *Proof:* by the one-shot
deviation principle, compare complying forever, worth w / (1 - delta), with attempting now, worth dev;
the problem is the same in every period. ∎

**Theorem E.2 (a known last period).** With a known last period T: if w < (1 - delta) dev the party
attempts at once; otherwise, if dev > w, it complies until T and attempts in period T; otherwise it
complies throughout. *Proof:* attempting in period t is worth w (1 - delta^(t-1)) / (1 - delta) +
delta^(t-1) dev; moving the attempt one period later changes this by delta^(t-1) (w - (1 - delta) dev),
whose sign does not depend on t; in period T, complying is worth w against dev. ∎

So a regime with a known end invites an attempt at the end whenever dev > w, even where it would hold
forever otherwise. This is the end effect of recursive inspection games, in which the inspectee
violates once inspections run out [@vonstengel2016recursive], and the argument for licences that renew
with no known last period. The condition w / (1 - delta) >= dev asks that membership be worth more
over its expected life than an attempt; with V the value of a decisive advantage it may not be, and
then only prevention, pi <= beta, is left.

**Proposition E.3 (the inspectee's best response).** In the general inspection game of Avenhaus, von
Stengel and Zamir, with the violator's gain normalised to 1, penalty b, false-alarm cost h and
false-alarm probability alpha, acting legally is a best response iff the non-detection probability is
at most (b - h alpha) / (1 + b) [@avenhaus2002inspection]. *Proof:* from their payoffs, legal behaviour
earns -h alpha and violation -b + (1 + b) times non-detection. ∎ The survey derived this corollary. In
simultaneous play no equilibrium has the inspectee legal with certainty; an inspector who commits to a
published inspection probability makes legal behaviour the best response [@avenhaus2002inspection;
@maschler1966price; @vonstengel2016recursive], and commitment needs a verifiable randomiser.

**Proposition E.4 (prevention against deterrence).** Prevention, non-detection at most beta, implies
Proposition E.3's condition whenever b >= (beta + h alpha) / (1 - beta), and not in general.
*Proof:* substitute. ∎ The two come apart in both directions. Deterrence can hold while a breakout would
usually succeed: in Gan's calibration it takes a chance of detection within the window of only
[32%](numbers.md#def-gan-deter-detect) [@gan2026clock]. Prevention can hold while an attempt is still
worth making, when the penalty is small against the prize. The line is a prevention line because the
endpoint is irreversible, with deterrence as the incentive layer far from it [@coe2020arms]; in Gan's
calibration prevention costs [7.8](numbers.md#def-gan-prevent-multiple) times the monitoring.

**Withdrawal.** If response can begin at notice and assets acquired under the regime are frozen
during it, a party leaving with holdings H meets the line at exit when T_b(H) + N >= m T_r, so the
notice N must cover only what the holding's breakout time does not; the survey's derivation, cut from
the claims as a small step ([the novelty file](03-novelty.md#withdrawal-notice-longer-than-the-response-time)).
It fails when notice can be withdrawn and revived, as North Korea's was [@bunn2005npt], or when assets
are not frozen [@eu2005nptwithdrawal]. Nothing in this section is claimed as ours: the inspection-game
item is prior work in the claims file. *Checked* on 20,000 random instances (65,380 checks), by brute force
over the party's plans, by `tools/formal/eq_inspection.py`; no counterexample.

## What the proofs do not establish

Every theorem above holds under its assumptions, and the gap between theorem and claim is the
assumptions. These need experiments, involve quantities nobody has measured, or leave adversaries
outside the model.

1. **Detection rates and their shape (C1, C3).** No AI verification channel has a measured rate
   against a real evader; the rates are transfers from simulation and other fields. The hazard's shape
   is assumed constant unless E5 fits it. Independence across channel groups is assumed, never
   tested, and an evader who adapts as it learns is outside (A1.1).
2. **Response (C1, C7).** No AI regime has measured T_resp; E24 transfers latencies from arms control.
   Against a major power no response may exist.
3. **Bounded errors (C1, C2).** Proposition 1.2 needs one-sided errors with known bounds. C* is a
   convention whose distance from D1 nobody can measure, so its error has no bound: m covers error in
   applying the agreed tables, not in the tables' truth.
4. **Monotone inputs (C2).** The direction of scale dependence is assumed (E1, E15).
5. **The round model (C4).** An input fixed within each round, the common form itself, transfer from
   a small staged run to the frontier, sandbagging and measurement noise. The interval's coverage is
   not proved; E4(c) must show it.
6. **The organism population (C5).** The bounds hold for the population sampled; a developer's
   organisms may be stronger.
7. **Coupling (C6).** Most off-diagonal entries are unmeasured, parties report their own edges, joint
   validity of the bounds is an assumption, the runaway theorem needs nonnegative couplings and has no
   ceiling, and the drift rate behind rho* is unmeasured.
8. **Payoffs (C7, compliance).** V, P, R, Q, w and delta are unmeasured; the games are one-shot or
   stationary; insiders can be coerced; non-members are outside.
9. **Floors (C8).** The highest attainable utilisation and the adversary's longest run are assumptions;
   the untraced pool is modelled.
10. **Hardware and logs (C9).** One broken trust anchor defeats every chip at once; data availability
    and an honest majority of hash power are assumed; offline, chips can save up their budget.
11. **The production function (C11).** CES is a family, not a finding, and D6's share is read as the
    common form's elasticity.
12. **The endpoint (C10, C12).** D1 cannot be observed before it happens, so necessity and sufficiency
    hold only in the model, at the agreed C*.

Outside every model here: a path the regime did not list, a party that leaves and races, sabotage of
the regime's own channels, and errors in this file's proofs that the checks, which test statements on
random instances and not the proofs themselves, would not catch. L4 and L6 exist for those.
