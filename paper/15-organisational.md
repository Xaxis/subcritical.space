# The organisational and economic perspective

This perspective asks how labs, markets and states supply the inputs from which superintelligence
could form: who holds each, how concentrated and fast-growing its supply is, and whether it can be
seen. It bears on the line (D4) twice. Supply growth sets how fast breakout time (D3) shrinks;
chokepoints, and the record of secret programmes in other domains, set detection time. Nothing in
the protocol has been deployed or tested against a real adversary.

## O1. The supply of inputs

**Definition.** For each input to frontier AI (capital, lithography, leading-edge logic,
high-bandwidth memory (HBM), packaging, finished chips, power, talent, data), O1 records at its
narrowest stage the suppliers' concentration, capacity growth, the lead time for a new plant, and
visibility: who counts units at the source, and how far independent estimates disagree. The scarcest
input a party can obtain bounds how fast it adds compute, an input to breakout time. Label: prior
work [@sevilla2024scaling2030; @khan2021supplychain; @epoch2026chipsales].

**Measurement.** The sources are company reports, analyst trackers, vendor guidance and construction
records [@verwey2021permits].

**Evidence for and against.** One firm makes extreme ultraviolet (EUV) lithography tools; it sold
[48 EUV systems](../research/numbers.md#org-euv-2025) in 2025 [@asml2026annualreport], and its
capacity doubles in about [2.6 years](../research/numbers.md#org-euv-doubling-years) at plan
[@asml2026q2call]. The yearly flow of chips is countable:
[13.6 million H100e](../research/numbers.md#org-sold-2025) sold in 2025 by all vendors, Huawei
included, [2.67](../research/numbers.md#org-sold-growth) times 2024, a sum of median estimates
[@epoch2026chipsales]. Capital, talent and data are fungible, mobile or uncountable. Power slows the
US build-out [@rand2026queued], but China added
[434 GW](../research/numbers.md#org-china-renewables-2025) of solar and wind in 2025
[@shaw2026chinasolar], so power is a detection channel, not a chokepoint. Against this,
concentration may be temporary [@varadarajan2024resilience; @counterpoint2026hbm]. E22 backtested
the supply bound: every one of the [19 observations](../research/numbers.md#e22-observations) of
sales and Huawei's output fell inside it, the tightest by a factor of
[1.97](../research/numbers.md#e22-min-margin) [@epoch2026chipsales]. For China the bound leaves room
for [2.84 million H100e](../research/numbers.md#e22-china-slack) of undeclared domestic output, so
supply data cannot rule out a large hidden fleet. It also bounds the allied fleet's growth between
declarations at [1.65](../research/numbers.md#e22-phi-member-quarter) a quarter.

**Open questions.** These bound supply, not holdings; the bound for a denied party without a
stockpile is untested, none being observed.

## O2. Race dynamics

**Definition.** O2 is the safety margin a developer gives up because others are racing, defined
inside a race model by the number of rivals, the lead, decisiveness (how sharply a small lead
becomes a likely win), enmity and the time to decisive advantage; its outcome is equilibrium safety.
Label: prior work [@armstrong2016racing; @emeryxu2024uncertainty; @fudenberg2026cooperating;
@buenodemesquita2026agirace]. A race model with a verification regime of stated detection time was
not found, the closest being a bilateral pause game [@gan2026clock]; E6 builds one as a tool, not a
claim.

**Measurement.** Decisiveness and enmity are assumed and safety spending is undisclosed. Only the
pace is observed: frontier training compute grows
[5.3](../research/numbers.md#org-frontier-compute-growth) times a year [@sevilla2024computegrowth],
which fits a race without measuring the margin.

**Evidence for and against.** The models agree racing erodes safety but disagree on information. In
one, information raises risk [@armstrong2016racing]; in another, public information is safer than
private except under high decisiveness [@emeryxu2024uncertainty], though E6's reimplementation,
unchecked, finds it no equilibrium; hidden capabilities make pacing harder
[@fudenberg2026cooperating]; and restricting resources "may backfire" [@buenodemesquita2026agirace].
The case against the protocol is that its declarations add information. E6 reran these games with a
verification regime added, on illustrative payoffs. Declaring only that each party is below the line
gave a higher disaster risk than no information in
[100%](../research/numbers.md#e6-o2-compliance-over-none) of its
[72 cells](../research/numbers.md#e6-o2-cells), and than private information alone in
[100%](../research/numbers.md#e6-o2-compliance-over-private), so that remedy is cut. The other,
keeping every breakout time longer than detection and response so no lead is decisive, is unproved.

**Open questions.** C7 applies D4 to coalitions: at fixed algorithms a coalition's breakout time
falls in inverse proportion to its share of the accounted fleet, so the response time sets the
largest admissible share, an application of the hardwired-pause threshold [@fithian2026hardwired]
and cartel leniency [@aubert2006leniency]. The share has no number until a response is drilled, its
guard against joint deviation is empty for decisive-advantage payoffs, and it may be empty against a
coalition with a major power. In E6 a coalition that absorbs drift during its run succeeds per
attempt with [0.076](../research/numbers.md#e6-staged-pi-line-inrun), above the tolerated
[5%](../research/numbers.md#def-prevent-beta), so the share is now lowered for in-run drift, and
again for growth between declarations as E22 bounds it; the reporting condition is only illustrated,
and nothing about real parties is measured.

## O3. Chokepoints

**Definition.** A stage is a chokepoint when one to three firms hold most capacity, output is
counted per unit at a few visible plants, and its erosion horizon (the years until an outsider could
replace its output at volume) exceeds detection and response time. Its leak fraction is the share of
downstream output that escapes accounting. Label: prior work [@sastry2024compute;
@shavit2023chinchilla; @scher2025agreement]. Ranking stages by measured durability, and counting
denial's larger footprint as a detection gain [@cottier2026horinger], were not found done
quantitatively, a claim about our search, and are not claimed.

**Measurement.** The horizon and the leak fraction are modelled, not counted, on weak sources and
assumed detection rates.

**Evidence for and against.** EUV is the most durable stage: China's prototype makes no chips yet,
on unnamed sources [@washenko2025euv]. Logic, HBM and packaging erode faster [@patel2025ascend;
@khan2021supplychain]. That order is a judgement made with hindsight. E23 ranked
[9 stages](../research/numbers.md#e23-stages) on data public at the end of 2022 against the erosion
since and found Spearman's rho of [0.28](../research/numbers.md#e23-rho) (one-sided p
[0.23](../research/numbers.md#e23-p)), no support for rankings of this kind. The edges leak faster
than the core erodes. An estimated [660,000 H100e](../research/numbers.md#org-smuggled-cum) was
smuggled into China through 2025, assuming [25%](../research/numbers.md#org-diversion-detect) of
diversions are detected [@juniewicz2026smuggling]. Outside estimates of Huawei's 2025 output differ
by a factor of [4.1](../research/numbers.md#org-huawei-spread) [@zafar2025kessler; @patel2025ascend;
@pan2026idc]; and the United States relaxed its own rules [@bis2025diffusion; @bis2025rescission;
@james2025h200]. Denial makes programmes bigger: a denied party needs about
[2.5](../research/numbers.md#org-denial-power-multiplier) times the power per unit of compute
[@cottier2026horinger]. Against this, denial builds substitutes [@allen2025senate].

**Open questions.** Whether denial lengthens or shortens the horizon is unsettled. E23 had power of
only [0.16](../research/numbers.md#e23-power-here), telling a ranking from chance would need
[85 stages](../research/numbers.md#e23-n-needed), and under four years may be too short to show slow
erosion such as EUV's, so the ranking stays unclaimed.

## O4. Covert supply

**Definition.** A covert programme runs outside a party's declarations. O4 records its time
undetected and its discovering channel; the discovery rate is discoveries over programme-years
undetected. No novelty is claimed: the history is the arms-control record below, the inspectorate's
reliance on intelligence is documented [@baker2023nuclear], and the rate is our arithmetic.

**Measurement.** The set is a convenience sample of programmes eventually found, in nuclear and
biological weapons, not AI.

**Evidence for and against.** Undeclared programmes ran for years, found by intelligence, defectors,
the media and disclosure, not inspectors.

Table: Undeclared weapons programmes, time undetected and how found {#tab:organisational-covert-programmes}

| Programme | Years undetected | How found |
|---|---|---|
| Iraq, nuclear | about [10 years](../research/numbers.md#org-iraq-years) | intelligence, then post-war inspections [@albright-2002; @thorne-1992] |
| Libya, nuclear | [20 years](../research/numbers.md#org-libya-years) or more | interdiction, then disclosure [@iaea-gov-2004-12; @crs-2004-libya] |
| Iran, centrifuges | [17 years](../research/numbers.md#org-iran-years) | media reports, then sampling [@iaea-gov-2003-40; @iaea-gov-2003-75] |
| Iran, Fordow | [3 years](../research/numbers.md#org-fordow-years-low) to [7 years](../research/numbers.md#org-fordow-years-high) | intelligence, then imagery [@whitehouse-2009-qom; @iaea-gov-2009-74] |
| Syria, reactor | about [6 years](../research/numbers.md#org-syria-years) | intelligence, after the site was destroyed [@iaea-gov-2011-30] |
| USSR, Biopreparat | [16 years](../research/numbers.md#org-biopreparat-years) | a defector [@fas-biopreparat; @hoffman-2009] |
| South Africa, nuclear | [15 years](../research/numbers.md#org-sa-years) active, never detected | self-disclosure [@vonbaeckmann-1995] |

E5's survival fit, counted from a programme's start rather than a breakout's, gives
[0.094/yr](../research/numbers.md#e5-hazard), an upper bound on a careful evader's rate, since every
programme in the set was found or disclosed. Under its Weibull fit a first-year discovery has chance
[2.6%](../research/numbers.md#e5-weibull-detect-1y).

C3 combines the channels: the chance a breakout is missed is a maximum over the evader's paths, with
channels that share one trust anchor or source of tips merged at the larger rate. It applies
physical-protection path analysis [@snell2007itc20] and network interdiction
[@washburn1995interdiction]; the merging rule is its only candidate extension. In E5 the untraced
chip pool's detection time is [299](../research/numbers.md#e5-td-ratio) times the declared path's
[39.0 days](../research/numbers.md#e5-td-declared-days), itself a design figure, while cloud and
distillation, with no measured channel, get no detection time.

**Open questions.** The sample is small and from other domains; no channel has been measured against
a real AI evader. E6 states when an exit breakout fails but has not tested withdrawal as a choice.

## What this perspective gives the line

Registered compute, counted at birth at the narrow stages and growing at the rates of O1, sets
breakout time on the declared path. Unaccounted compute must be counted as if the worst-placed party
held all of it, since covert work has been found after years, not months. Race pressure is a design
constraint: on the models above, the protocol should cap the prize and publish the line. Disclosing
compliance rather than rank raised risk in E6 and is cut, so disclosure must be weighed against the
race it may sharpen.
