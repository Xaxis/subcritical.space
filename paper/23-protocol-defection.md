# Defection, coalitions and secret programmes

## Who it binds

The protocol binds the states that join, and through them every firm in the chain. States that host EUV
lithography, leading-edge fabs and HBM log their exports, and exporting unlicensed AI chips is a
violation. But a chokepoint's holder can choose to sell. The controlling state published the diffusion
rule in January 2025 [@bis2025diffusion], rescinded it in May [@bis2025rescission], and in December
approved H200 sales to China for a [25%](../research/numbers.md#org-h200-fee) duty [@james2025h200].
Binding the holders is a political commitment; the log makes a reversal visible, not impossible.

## The coalition share, derived from the response time

A coalition holding a share s of the accounted fleet, at fixed algorithms, has T_b(s) = h_w / s, where
h_w is the time the whole fleet would need to reach the breakout budget:
[7.8 years](../research/numbers.md#claim-whole-fleet-horizon) at the hardwired-pause paper's inputs and
the projected end-2026 fleet. The line gives the largest admissible share on each path,
s* = min(1, h_w / (m * T_r)) (Part III, Proposition 7.1). On declared, licensed compute at the
illustrative T_r, s* is [100%](../research/numbers.md#prot-coalition-share-declared).

After the red team, E6 found that a line computed at launch speed misses a run absorbing drift as it
goes: a coalition passing it succeeds with [0.076](../research/numbers.md#e6-staged-pi-line-inrun) per
attempt, above beta of [5%](../research/numbers.md#def-prevent-beta). The correction (Part III,
Corollary 1.6a) raises m * T_r by a factor of [3.2](../research/numbers.md#formal-inrun-line-factor) at
the central drift rate and [10.6](../research/numbers.md#formal-inrun-line-factor-high) at the high
end, both upper bounds. The share then stays [100%](../research/numbers.md#prot-coalition-share-inrun)
at the central rate, and falls to [37%](../research/numbers.md#prot-coalition-share-inrun-high) at the
high end. The margin does not cover phi, the fall in T_b before the next check, which with E22's supply
bound and drift between renewals is [2.1](../research/numbers.md#prot-phi-quarter) a quarter; on top of
in-run drift at the central rate the share falls to
[58%](../research/numbers.md#prot-coalition-share-inrun-phi) for a coalition growing no faster than the
fleet; one buying more of the new chips must hold less. E6's staged share of
[69%](../research/numbers.md#e6-staged-share) uses its illustrative T_r, the paper's lower budget, a
coalition buying all new chips and no margin.

All of this rests on one published breakout budget,
[2e+29 FLOP](../research/numbers.md#def-hwp-breakout-budget), an assumption of its paper. In terms of
the budget B, s*(B) = min(1, B / B_1), with B_1
[0.26](../research/numbers.md#prot-coalition-budget-unity) of that budget at fixed algorithms; the
overt line binds over only [5%](../research/numbers.md#e6-budget-binding-share) of the paper's own
range at the illustrative T_r. Where only the historical channels see a path, s* needs a bounded T_r
that E24's record does not give, so it is 0 until one is measured.

A coalition can police itself. For shares up to h_w / T_r (less with drift) no joint breakout is
self-enforcing, provided each member's reward for reporting exceeds beta times what a breakout is worth
to it (Theorem 7.2). No fund pays a state that, and reporters need the reward net of retaliation, which
a state can impose [@hoffman-2009; @dyck2007whistle]. Without it only the penalty condition is left,
beta V <= (1 - beta) P, which fails once a decisive advantage is worth more than
[19](../research/numbers.md#prot-prize-over-penalty) times the penalty. For the payoffs this work calls
realistic, coalition-proofness adds nothing to prevention. The share is the hardwired-pause fleet
threshold solved for s [@fithian2026hardwired] and the reporting condition is cartel leniency's
[@aubert2006leniency]; in the record C7 stands as an application of C1.

Algorithms do not stay fixed, so h_w shrinks every year: "agreements have a clock" [@gan2026clock].
Against a coalition that includes a major power T_resp may be unbounded, and the regime offers
deterrence only.

## Penalties on outsiders

States that stay out need a penalty. Without sanctions on outsiders, Nordhaus finds only coalitions
with minimal abatement stable [@nordhaus2015climate; @rahman2025nonparty]. The protocol's penalty is
denial of licensed chips, cloud compute and models above the teacher threshold. A party cut off from
the leading edge needs about [2.5](../research/numbers.md#org-denial-power-multiplier) times the power
per unit of compute [@cottier2026horinger], which in E8 delays a power channel's failure by about
[3.1 years](../research/numbers.md#e8-denial-delay-years). Denial also builds substitutes, such as
China's EUV prototype and domestic HBM [@washenko2025euv; @patel2025ascend]. Whether denial lengthens
or shortens the chokepoints' life is not settled.

## Withdrawal

A party leaving with every path outside the line needs no notice. For holdings whose breakout time
shrank during membership, if response can begin at notice and assets are frozen during it, the notice
must satisfy N >= m * T_r - T_b(exiting), with T_b counting in-run drift: at most (m - 1) * T_r,
[12 months](../research/numbers.md#prot-notice-months) at the illustrative values. MIRI's draft sets
[12 months](../research/numbers.md#org-miri-withdrawal) [@scher2025agreement]; the two meet only
because of our illustrative inputs. Notice alone did not hold: North Korea suspended its NPT withdrawal
a day before it took effect and later revived it [@bunn2005npt]. It works only with assets frozen
[@eu2005nptwithdrawal; @scher2025agreement], and licences give that lever: registered chips run under
monitoring during notice and stop at its end unless returned. Exit that costs too much itself endangers
regimes [@rosendorff2001optimal].

## Undeclared compute and secret programmes

On the published budget, with that paper's assumed research overhead and utilisation, the smuggled
stock would need [555 years](../research/numbers.md#prot-pool-years-fixed) at fixed algorithms, but
[13 years](../research/numbers.md#prot-pool-years-small) at the small-compute bound of
[1.52](../research/numbers.md#comp-gundlach-small-annual-max) a year and
[3.9 years](../research/numbers.md#prot-pool-years-rosetta) at the Rosetta rate. This is our
arithmetic, as if every gain reached the holder, and E1 cannot say which rate holds. Detection on that
path takes at least [32 years](../research/numbers.md#e5-td-pool-years) at E5's median
([23 years](../research/numbers.md#e5-td-pool-years-lo) to
[43 years](../research/numbers.md#e5-td-pool-years-hi)), before any response.

So at any rate of progress Part I measured the smuggled stock fails the line, and for covert paths the
line reduces to "hold no covert reserve". Nothing in the protocol closes the pool today. Until it
closes every party is weapons-grade through it, and a regime that classes compliant and non-compliant
parties alike cannot reward compliance through the line. The protocol does five things.

1. **Declare the line unmet.** As an interim rule, parties are classified on their declared paths,
   which is no prevention guarantee, and the pool is reported as an unmet condition common to all.
2. **Shrink the pool,** by registration at birth, a window for existing stock with an amnesty and a
   price per chip checked against makers' records, and contraband status afterwards. It must shrink
   about [1,200](../research/numbers.md#e8-pool-shrink-1e26-pause)-fold before chip accounting resolves
   the floor of a [1e+26 FLOP](../research/numbers.md#phys-rahman-1e26-local) run at a pause's run
   length (E8).
3. **Slow the drift the pool can use** by restricting research that changes scaling at frontier scale;
   small-scale drift goes on, so this only buys time.
4. **Weight the channels that worked:** intelligence shared among rival blocs, and rewarded insiders.
5. **Say where it stops.** Against the likeliest long-lived covert builder, a large state with its own
   chip chain, the protocol offers detection and deterrence, not prevention.
