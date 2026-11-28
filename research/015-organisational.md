# Part I, 5: The organisational and economic perspective

The physical and computational chapters say what superintelligence would take: how much compute,
energy, memory and data, at what algorithmic efficiency. This chapter asks who supplies those
inputs, how concentrated and how fast-growing each supply is, whether it can be seen, and why the
people who control it might cut safety to go faster. Every pathway in the memo's table consumes
compute, and compute reaches a developer through a supply chain with a few narrow, slow, visible
stages. That is why this perspective decides where a protocol can stand, and why it also shows
where a protocol will leak.

Four findings frame the chapter. The core of the chain is narrow and countable: one firm makes
extreme ultraviolet (EUV) lithography tools, one foundry earns most foundry revenue, three
firms make high-bandwidth memory (HBM), and the whole yearly flow of AI chips is small enough to
count. The chain leaks at its edges much faster than it erodes at its core: through smuggling,
stockpiles bought before a rule took effect, estimates that disagree by a factor of
[4.1](numbers.md#org-huawei-spread), and the
controlling state's own choice to sell. Competition among labs and states pushes against safety,
and the published race models disagree on whether the transparency a protocol needs calms that
race or inflames it. And secret programmes in other domains ran for years before anyone found them,
and were found mostly by intelligence services, defectors and disclosure, not by inspectors.

The memo listed three organisational mechanisms (O1 to O3). This chapter keeps them and adds O4,
covert supply, because who could build superintelligence in secret is an organisational question
that the memo's list left out. Each is a candidate, not a finding. Nothing in the protocol has been
deployed or tested against a real adversary.

## O1. The supply of inputs

### Definition

For each input to frontier AI (capital; lithography tools; leading-edge logic wafers; HBM; advanced
packaging; finished AI chips; power; talent; data), O1 records four quantities over the global
market that supplies frontier training and inference:

1. **Concentration:** the share of world capacity or revenue held by the largest one and the
   largest three suppliers at the input's narrowest stage (a percentage).
2. **Growth:** the yearly growth of that stage's capacity (per cent a year), and its doubling time
   in years.
3. **Lead time:** the time to bring a new plant or tool of that stage into production (years).
4. **Visibility:** whether units are counted at the source and by whom, and the measured spread
   between independent estimates of the same quantity (the ratio of the highest estimate to the
   lowest).

From these, a party's **supply envelope** over a period is the most of each input it could obtain,
given who will sell to it, how fast suppliers can grow and how long new plants take. The minimum of
the envelope across inputs bounds how fast the party can add effective compute. That bound is one
of the inputs to breakout time (D3): a party can only convert holdings into capability as fast as
its tightest input allows.

### How it is measured

Concentration comes from company reports (ASML's annual report counts the EUV systems it recognised
in sales) and from analyst trackers (TrendForce for foundry revenue, Counterpoint for
HBM). Growth comes from past counts and from vendor guidance, which is a claim by an interested
party and is labelled so in the ledger. Lead times come from construction records
[@verwey2021permits; @somala2025buildtimes]. Visibility is measured directly: where several
independent estimates of the same quantity exist, their spread is the measurement error an inspector
would inherit.

Who can hide what differs by input. A listed firm's capital spending is public each quarter
[@ehsan2026capex]; a state's is not. A foundry's wafer output is known to the foundry and roughly to
its customers. A state-backed chip maker's output is known only through outside estimates, and for
Huawei's 2025 output those estimates differ by a factor of [4.1](numbers.md#org-huawei-spread) (see O3).

### The evidence, input by input

| Input | Narrowest stage and its suppliers | Growth | Lead time | Visibility | Chokepoint? |
|---|---|---|---|---|---|
| Capital | a few firms: [650 billion USD](numbers.md#org-capex-big4-2026) planned for 2026 by the largest four (February), over [700 billion USD](numbers.md#org-capex-hyperscalers-2026) for the largest hyperscalers by May | [60%](numbers.md#org-capex-big4-growth) over 2025; frontier run costs [2.4](numbers.md#org-train-cost-growth) times a year | none for a state | firms quarterly; states not | No |
| EUV lithography | ASML alone; [48 EUV systems](numbers.md#org-euv-2025) recognised in 2025 ([44 EUV systems](numbers.md#org-euv-2024) in 2024) | [30%](numbers.md#org-euv-capacity-growth-2027) more capacity planned for 2027 | years (China's prototype makes no chips yet) | unit counts, by the maker | Yes, the narrowest |
| Leading-edge logic | TSMC [72.5%](numbers.md#org-tsmc-share-2q26) of foundry revenue, Q2 2026 | dispersing among allied states | [1.9 years](numbers.md#org-fab-years) per fab | wafers, by the foundry | Yes |
| HBM | SK hynix [50%](numbers.md#org-hbm-skhynix-2q26), Samsung [33%](numbers.md#org-hbm-samsung-2q26), Micron [18%](numbers.md#org-hbm-micron-2q26), Q2 2026 | shares shifting; a Chinese DRAM maker rising | years | stacks, by the maker | Yes, eroding |
| Advanced packaging | TSMC's CoWoS plus a few outsourced assemblers | over [80%](numbers.md#org-cowos-cagr) a year | short relative to fabs | wafers, by the maker | Weakly |
| Finished AI chips | [13.6 million H100e](numbers.md#org-sold-2025) sold in 2025 by all vendors, Nvidia [65.5%](numbers.md#org-nvidia-share-2025) | [2.67](numbers.md#org-sold-growth) times 2024 | follows the stages above | shipments; leaks downstream | Where it leaks |
| Power | many utilities and equipment makers | US slow, China fast | [5.1 years](numbers.md#org-interconnect-years) median US interconnection | grid records, satellites | No |
| Talent | spread across rival blocs | mobile | years to train | publications | No |
| Data | the public web and private holdings | stock about fixed | none | low | No |

**Capital.** The money is concentrated and visible but not scarce. The four largest technology
companies planned about [650 billion USD](numbers.md#org-capex-big4-2026) of capital spending for 2026,
[60%](numbers.md#org-capex-big4-growth) more than in 2025 [@day2026capex]; by May the plans of the
largest hyperscalers had topped [700 billion USD](numbers.md#org-capex-hyperscalers-2026)
[@ehsan2026capex]. The amortised cost of the most compute-intensive training runs has grown
[2.4](numbers.md#org-train-cost-growth) times a year since 2016 (90% CI
[2.0](numbers.md#org-train-cost-growth-low) to [2.9](numbers.md#org-train-cost-growth-high)), and on that
trend the largest runs will cost more than [1 billion USD](numbers.md#org-largest-run-cost-2027) by
2027, an extrapolation rather than a measurement [@cottier2024rising] (abstract read). One cluster
shows the scale: xAI's Colossus held [200,000 AI chips](numbers.md#org-colossus-chips), cost
[7 billion USD](numbers.md#org-colossus-hw-cost) in hardware and drew [300 MW](numbers.md#org-colossus-power)
[@pilz2025supercomputers] (abstract read). Energy is only
[2%](numbers.md#org-energy-cost-share-low) to [6%](numbers.md#org-energy-cost-share-high) of the
amortised cost of frontier training [@cottier2024rising]. So power is a weak cost lever but, being a
large share of the physical footprint, a good detection channel. Capital cannot be a chokepoint: a
state can find a few billion dollars, and money moves freely between uses.

**Lithography.** One firm makes EUV scanners, which leading-edge logic and DRAM depend on. ASML
recognised [48 EUV systems](numbers.md#org-euv-2025) in sales in 2025, of which
[4 High-NA systems](numbers.md#org-euv-highna-2025), up from [44 EUV systems](numbers.md#org-euv-2024) in
2024, a rise of [9%](numbers.md#org-euv-growth-2025) [@asml2026annualreport]. Its CFO expects to ship
around [65 low-NA EUV systems](numbers.md#org-euv-lowna-2026) in 2026, plans
[30%](numbers.md#org-euv-capacity-growth-2027) more low-NA capacity in 2027, and is studying a further
[30%](numbers.md#org-euv-capacity-growth-2028) for 2028 [@asml2026q2call]. At the planned 2027 rate,
EUV capacity doubles in about [2.6 years](numbers.md#org-euv-doubling-years). Vendors headquartered in
the EU hold [89%](numbers.md#org-litho-eu-share) of lithography equipment revenue
[@varadarajan2024resilience]. China bought [33%](numbers.md#org-asml-china-units-2025) of ASML's tools by
unit in 2025, down from [41%](numbers.md#org-asml-china-units-2024) in 2024, counting all tool types
[@shilov2026asml].

**Leading-edge logic.** TSMC took [72.5%](numbers.md#org-tsmc-share-2q26) of foundry revenue in Q2
2026, against [5.9%](numbers.md#org-samsung-share-2q26) for Samsung and
[5.4%](numbers.md#org-smic-share-2q26) for SMIC, and AI demand kept its 5, 4 and 3 nm capacity fully
booked [@trendforce2026foundry]. In 2022 all sub-10 nm logic capacity sat in Taiwan
([69%](numbers.md#org-sub10-taiwan-2022)) and South Korea ([31%](numbers.md#org-sub10-korea-2022)); a
consultancy projects the US at [28%](numbers.md#org-sub10-us-2032) by 2032
[@varadarajan2024resilience]. The same report counts at least [50](numbers.md#org-points-over-65)
points in the semiconductor chain where one region held over [65%](numbers.md#org-points-threshold) of world share. A greenfield fab
took an average of [682 days](numbers.md#org-fab-days) ([1.9 years](numbers.md#org-fab-years)) from
construction start to production between 1990 and 2020, and [918 days](numbers.md#org-fab-days-us)
([2.5 years](numbers.md#org-fab-years-us)) in the US in the 2010s, before counting permits
[@verwey2021permits]. A new fab is a construction project of years that everyone can see.

**High-bandwidth memory.** Three firms make HBM. In Q2 2026 SK hynix had
[50%](numbers.md#org-hbm-skhynix-2q26) of HBM revenue, Samsung [33%](numbers.md#org-hbm-samsung-2q26) and
Micron [18%](numbers.md#org-hbm-micron-2q26); a year earlier SK hynix had
[64%](numbers.md#org-hbm-skhynix-2q25) [@counterpoint2026hbm]. The stage is concentrated but not
static: China's CXMT went from [4%](numbers.md#org-dram-cxmt-2q25) to [10%](numbers.md#org-dram-cxmt-2q26)
of DRAM revenue in a year, in commodity DRAM rather than HBM [@counterpoint2026hbm].

**Advanced packaging.** Packaging grew fastest. TSMC's CoWoS capacity was
[14,000 wafers a month](numbers.md#org-cowos-dec2023-low) to
[15,000 wafers a month](numbers.md#org-cowos-dec2023-high) in December 2023 [@sevilla2024scaling2030] and
is put at [120,000 wafers a month](numbers.md#org-cowos-2026-low) to
[140,000 wafers a month](numbers.md#org-cowos-2026-high) in 2026 by an analyst estimate, with partners
bringing the total towards [200,000 wafers a month](numbers.md#org-cowos-total-2026)
[@trendforce2026cowos]. Comparing the conservative ends, capacity grew by a factor of
[8](numbers.md#org-cowos-multiple) between December 2023 and 2026. TSMC's own figure is growth of more
than [80%](numbers.md#org-cowos-cagr) a year from 2022 to 2027, a doubling every
[1.2 years](numbers.md#org-cowos-doubling-years).

**Finished AI chips.** The flow the protocol would register is small enough to count. Summing the
per-quarter median estimates in Epoch's chip sales data gives
[5.1 million H100e](numbers.md#org-sold-2024) sold in 2024 and [13.6 million H100e](numbers.md#org-sold-2025)
in 2025 by all vendors, Huawei included, a ratio of [2.67](numbers.md#org-sold-growth) [@epoch2026chipsales]. The sum is the survey
helper's, confirmed by the spot-check; it is not a figure Epoch states, and it has no valid interval.
Nvidia made [65.5%](numbers.md#org-nvidia-share-2025) of 2025's compute, Google's TPUs
[20%](numbers.md#org-google-share-2025) and Huawei [3.9%](numbers.md#org-huawei-share-2025); the chips
alone were rated at [7.5 GW](numbers.md#org-chip-tdp-2025) before cooling. Holdings are as concentrated
as sales: the five US hyperscalers own more than [70%](numbers.md#org-hyperscaler-share) of global AI
compute, and Chinese companies just over [5%](numbers.md#org-china-owned-share) of recent AI chip compute,
excluding smuggled chips and offshore cloud [@you2026chipowners]. AI supercomputer performance has
doubled every [9 months](numbers.md#org-supercomputer-doubling), with
[75%](numbers.md#org-us-supercomputer-share) of it in the US and
[15%](numbers.md#org-china-supercomputer-share) in China [@pilz2025supercomputers]. Satellite and aerial
imagery of cooling plant, checked against permits and disclosures, already measures the largest
sites: Epoch's hub launched with
[13 sites](numbers.md#org-dc-hub-sites) holding about [15%](numbers.md#org-dc-hub-share) of all H100e
delivered [@epoch2025datacentershub].

**Power.** Power slows the US build-out and is easy to watch, but nobody controls it globally. Data
centres used [415 TWh](numbers.md#org-dc-world-2024) worldwide in 2024, projected to reach
[945 TWh](numbers.md#org-dc-world-2030) by 2030 [@iea2025energyai]; US data centres used
[176 TWh](numbers.md#org-dc-us-2023) in 2023, [4.4%](numbers.md#org-dc-us-share-2023) of US electricity
[@shehabi2024datacenter]. In the US the median power project built in 2025 took
[61 months](numbers.md#org-interconnect-2025) from interconnection request to operation (generator
projects only), against
[36 months](numbers.md#org-interconnect-2015) in 2015 and [22 months](numbers.md#org-interconnect-2008) in
2008 [@rand2026queued]; large power transformers took [128 weeks](numbers.md#org-transformer-lead)
([2.5 years](numbers.md#org-transformer-years)) and generator step-up transformers
[143 weeks](numbers.md#org-gsu-lead) [@woodmac2025connection]; the three large-frame gas turbine makers
carry about [220 GW](numbers.md#org-turbine-backlog) of backlog between them [@bailey2026steam]. Yet China
added [315 GW](numbers.md#org-china-solar-2025) of solar and [119 GW](numbers.md#org-china-wind-2025) of
wind in 2025 alone, [434 GW](numbers.md#org-china-renewables-2025) in a year [@shaw2026chinasolar], and
Epoch concludes that "China appears to have no shortage of energy for data centers"
[@cottier2026horinger]. Large sites go up fast: the quickest recent site reached
[1 GW](numbers.md#org-dc-build-target) [11.6 months](numbers.md#org-dc-1gw-fastest) after construction began, and recent sites took
[1](numbers.md#org-dc-1gw-low) to [3.6 years](numbers.md#org-dc-1gw-high) [@somala2025buildtimes]. The
large-frame turbine stage is a three-firm stage, a possible secondary chokepoint for on-site power,
but the survey found no share data, so it is a lead, not a finding.

**Talent.** Talent is large, mobile and split between rival blocs. In a sample of NeurIPS 2025
authors, [41%](numbers.md#org-talent-china-2025) worked in China and
[34%](numbers.md#org-talent-us-2025) in the US, against [27%](numbers.md#org-talent-china-2022) and
[46%](numbers.md#org-talent-us-2022) in 2022 [@ma2026talent]. The sample is
[25,677 authors](numbers.md#org-talent-authors), of whom only some had complete career histories,
so it is not a random sample. The US keeps [89%](numbers.md#org-talent-us-retention) of its top talent. Talent is not a
chokepoint, but it is how chokepoints erode: China's EUV prototype was reportedly built by former
ASML engineers [@washenko2025euv].

**Data.** The effective stock of public human text is about
[400 trillion tokens](numbers.md#org-data-stock), fully used by frontier training at a median of
[2028](numbers.md#org-data-full-use-year), at about [5e+28 FLOP](numbers.md#org-data-full-use-flop) of
compute-optimal training [@villalobos2022data]. Data does not bind below that scale, nobody can count
who holds it, and its substitutes (synthetic data, self-play) are the computational chapter's
subject. It is not a chokepoint.

**Chokepoints run both ways.** The chain also has stages a coalition led from one bloc does not hold.
China refines about [99%](numbers.md#org-china-gallium) of the world's gallium [@iea2025energyai], and
it is strongest in assembly, testing and packaging [@khan2021supplychain]. A protocol that stands on
chokepoints held by one bloc invites counter-pressure on chokepoints held by the other.

### What cuts against the memo

The strongest case against the memo's picture is that concentration is temporary. Leading-edge fabs
are dispersing into more countries [@varadarajan2024resilience]; packaging capacity grows fast enough
to stop binding within a few years [@trendforce2026cowos]; HBM shares move by double digits in a
year [@counterpoint2026hbm]. Each of these adds sites to watch, though almost all of them sit in
allied states. A second case is that the binding constraint on scaling is not a chokepoint at all.
Epoch's study of scaling to 2030 finds that "the constraint likely to bind first is power, followed
by the capacity to manufacture enough chips" [@sevilla2024scaling2030]. Power binds the pace of US
build-out; it does not give anyone a way to deny a rival.

### What the survey changed

The memo listed power among the physical chokepoints ("chips, fabs, power", in the reasons under
the pathway table). **That was wrong.** Power is a rate limit in the US and a strong detection
channel (the physical chapter's footprint), but no small set of suppliers controls it worldwide, and
the party the protocol most needs to bind has power to spare. The memo's per-input table (who
supplies each input, how concentrated, how fast it grows, how visible) is **prior work**. The pieces
exist in Sevilla et al. on the constraints to 2030 [@sevilla2024scaling2030], Pilz et al. on AI
supercomputers [@pilz2025supercomputers], Khan and Mann and Khan et al. on concentration and value
shares [@khan2020aichips; @khan2021supplychain], Varadarajan et al. on regional concentration
[@varadarajan2024resilience], and Epoch's chip sales, chip owner and data centre datasets
[@epoch2026chipsales; @you2026chipowners; @epoch2025datacentershub]. The survey found no single
source that puts every input in one table with growth and visibility side by side, but compiling one
is synthesis, not a claim, and "not found" is a claim about our search. Nothing of substance in O1 is
ours ([novelty file](03-novelty.md#o1-the-supply-of-inputs)).

### What it means for the protocol

A candidate, not a finding. Of the nine inputs, four can carry a limit (lithography, leading-edge
logic, HBM, packaging), because their output is already counted by a few firms at a few large
plants. Finished chips are where the protocol registers what those stages produce. Capital, talent
and data cannot be limited at any acceptable cost to useful AI: they are fungible, mobile or
uncountable, and limiting them would hit every use of AI, not the path to superintelligence. Power
is a verification channel (site power, interconnection queues, turbine and transformer orders), not
a limit. Registration at the source costs little where makers already keep unit records; the cost
falls on confidentiality and on sales foregone, which, as O3 shows, is exactly the cost that has
made the controlling state relent.

### What would test it

E1 has run, on the algorithmic side of breakout time rather than this chapter's hardware side, and
found the drift rate not identified on public data: across six samples of the same models it runs
from [2.6](numbers.md#e1-algo-annual-subset-min) to [1,512](numbers.md#e1-algo-annual-subset-max) a
year ([C2](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)).
The claims file therefore rests the declared path's line on the compute a chip count sees, not on the
drift term, which makes the supply this chapter measures carry more weight. The hardware side is
**E22, the supply envelope backtest**, which has run. From sourced capacities (CoWoS wafers, logic,
HBM stacks, good dies per wafer) it computes, quarter by quarter, the most H100e each kind of party
could make, taking each quarter's smallest stage at its 95th-percentile capacity with yields of one,
and compares that upper bound with Epoch's sales estimates [@epoch2026chipsales] and the estimates of
Huawei's output. The envelope passes: all [19 observations](numbers.md#e22-inside) of
[19 observations](numbers.md#e22-observations) fall inside, the tightest by a factor of
[1.97](numbers.md#e22-min-margin).

- **A member with full access.** The allied chain's upper bound is
  [13.6 million H100e](numbers.md#e22-member-env-2024) in 2024 and
  [31.3 million H100e](numbers.md#e22-member-env-2025) in 2025: what it could have made, not what it
  sold. The 2024 bound equals all vendors' 2025 sales above only by coincidence. Allied observed
  sales, Nvidia, Google, AMD and Amazon only, were [4.9 million H100e](numbers.md#e22-member-obs-2024)
  in 2024 and [13.0 million H100e](numbers.md#e22-member-obs-2025) in 2025, below the all-vendor totals
  because Huawei and the smaller makers are left out. The margins, allied upper bound over allied
  observed sales, are [2.8](numbers.md#e22-member-margin-2024) and [2.4](numbers.md#e22-member-margin-2025). At
  central inputs the envelope is [11.3 million H100e](numbers.md#e22-member-env-central-2024) and
  [26.4 million H100e](numbers.md#e22-member-env-central-2025), estimates, not bounds. The binding
  stage is CoWoS packaging: the observed sales need [71%](numbers.md#e22-cowos-use-2024) and
  [68%](numbers.md#e22-cowos-use-2025) of median CoWoS capacity in the two years, or
  [90%](numbers.md#e22-cowos-use-epoch-2024) and [87%](numbers.md#e22-cowos-use-epoch-2025) from
  Epoch's own lagged consumption.
- **A denied party with a stockpile.** China's domestic chain could have made at most
  [3.55 million H100e](numbers.md#e22-china-env-cum) in 2024 and 2025 together, the stockpiled HBM
  plus CXMT's output, against Huawei's observed [0.71 million H100e](numbers.md#e22-china-obs-cum), a
  margin of [5.0](numbers.md#e22-china-margin-cum); at central inputs the envelope is
  [1.23 million H100e](numbers.md#e22-china-env-central-cum). Huawei's output needs
  [58%](numbers.md#e22-china-stacks-share) of the stockpiled HBM at Epoch's unit mix. The bound leaves
  room for [2.84 million H100e](numbers.md#e22-china-slack) of undeclared domestic output, so supply
  data cannot rule out a large hidden domestic fleet.
- **A denied party without a stockpile.** At most
  [0.42 million H100e](numbers.md#e22-nostock-env-year) a year from CXMT's HBM. Untested: no such
  party was observed in 2024 or 2025.

The envelope also bounds phi, the factor by which a party's holdings can grow between declarations,
which bounds how far its breakout time can fall before the next one; Part III's rule for checking the
line only at declarations needs it bounded ([Part III](05-formal.md#c1-the-line-per-path), Proposition 1.6). For the allied fleet the
bound is [2.5](numbers.md#e22-phi-member-year) over a year and
[1.65](numbers.md#e22-phi-member-quarter) over a quarter; for China on domestic supply alone it is
[2.4](numbers.md#e22-phi-china-year) over 2026, and imports and smuggling add to it. These are
bounds on supply, not on what a party holds: on the 2025 envelope, new allied supply alone could
reach the hardwired-pause breakout budget in [0.45 years](numbers.md#e22-member-years-to-hwp) from
no chips, China from its end-2025 holdings in [0.7 years](numbers.md#e22-china-years-to-hwp), and a
denied party without a stockpile in [3.9 years](numbers.md#e22-nostock-years-to-hwp), all lower
bounds on the time.

## O2. Race dynamics

### Definition

O2 is the safety margin a developer gives up because others are racing. It is defined inside a race
model, because nothing measures it directly. A race is described by: the number of parties within a
given lag of the frontier (n); the leader's lead, in months of compute growth; the decisiveness of
the race (m: how sharply a small lead turns into a high chance of winning); the enmity between
parties (e: how much each fears the other winning); and the time to decisive advantage (W). The
outcome is the equilibrium safety investment s* in a stated model, or the probability of disaster
it implies. The protocol cares about the derivative: how s* moves when the protocol changes the
information parties have, the size of the prize and the time to detection.

### How it is measured

Only some of these parameters can be measured. The number of parties near the frontier and the size
of the lead can be estimated from compute holdings and release dates (O1, and the computational
chapter). Decisiveness and enmity are not measured anywhere; every model assumes them. Safety
investment is not disclosed in comparable units. What can be observed is the pace: the training
compute of frontier models has grown [5.3](numbers.md#org-frontier-compute-growth) times a year
[@sevilla2024computegrowth], its cost [2.4](numbers.md#org-train-cost-growth) times a year
[@cottier2024rising], and the largest firms' capital spending [60%](numbers.md#org-capex-big4-growth) in
a year [@day2026capex]. These are consistent with a race; they do not measure the safety margin
given up. O2 is a mechanism the project can model and test in games, not one it can measure in the
field. That is its weakness.

### The evidence for and against

The models agree that racing erodes safety, and disagree on what helps.

- **More racers, more enmity, more danger.** In Armstrong, Bostrom and Shulman's model, teams with
  random capability choose a safety level, the highest capability net of safety wins, and the
  winner's system is safe with probability equal to its safety level. Without information, the
  symmetric equilibrium safety is s = mu/(e n) when that is below 1: more teams and more enmity lower
  it. Its abstract adds: "information also increases the risks: the more teams
  know about each others' capabilities (and about their own), the more the danger increases"
  [@armstrong2016racing].
- **What makes cooperation possible.** Askell, Brundage and Hadfield name five conditions: high trust,
  shared upside, low exposure to unreciprocated cooperation, low advantage from defecting, and high
  shared losses from mutual defection [@askell2019cooperation].
- **The time-scale decides.** In Han et al.'s evolutionary game, "the time-scale in which AI supremacy
  can be achieved plays a crucial role"; when supremacy comes quickly, those who ignore safety win, and
  "blindly imposing regulations may not have the anticipated effect" [@han2020regulate]. In some late
  regimes their model even favours promoting risk-taking.
- **Close, hostile laggards gamble.** Stafford, Trager and Dafoe find that a laggard that is not very
  capable does not use a risky technology unless it catches up, but a laggard close to the leader,
  facing a highly adversarial rival, cuts corners to gamble for advantage, and safety improvements are
  "attenuated or reversed by risk compensation" [@stafford2022safety]. This is a 2022 working-paper
  draft and is cited as one.
- **Decisive races are dangerous, and information cuts both ways.** Emery-Xu, Park and Trager use a
  logistic contest with decisiveness m. With no or private information, risk always rises with
  decisiveness; no information is always safer than private information; and public information is
  less risky than private "except under high decisiveness", because states learn either that they are
  far apart and compete less, or that they are close and "drastically reduce safety to win"
  [@emeryxu2024uncertainty].
- **Hidden capabilities make pacing harder.** Fudenberg and Koh model two firms choosing speed while a
  safety threshold advances: at low thresholds only racing is an equilibrium, at intermediate ones
  racing and pacing coexist, at high ones only pacing survives; and "if internal capabilities are
  hidden with a fixed lag until deployment, it is harder to sustain pacing", which they read as an
  argument for transparency about internal capabilities [@fudenberg2026cooperating].
- **Restricting resources may backfire.** Bueno de Mesquita, Dziuda and Polborn find that "industry
  consolidation, regulation facilitating commitment to slow down, and governments entering the race
  in a safe way improves welfare, while restricting resources may backfire": with few firms and a
  positive expected value, extra resources go to safety, with many firms, to speed, and "a small commitment to reduced speed can leave all
  firms better off" [@buenodemesquita2026agirace]. Only the research brief was read, not the working
  paper, and the model is a race that continues, not a regime that halts training above a line.
- **Monitoring has a security cost.** Coe and Vaynman explain why arms control is rare: monitoring
  that makes a state's arming transparent enough to assure compliance can make it transparent enough
  to threaten its security. Faster and more decisive arming needs closer monitoring, and "warships
  should be easier to limit in a closed deal than similarly impactful cyber weapons because only the
  former are large physical objects" [@coe2020arms].
- **Agreements have a clock.** Gan solves a bilateral pause game with detection as a Poisson process
  inside a response window. Deterrence does not need near-certain detection: in his illustrative
  calibration, a [32%](numbers.md#org-gan-detect) chance of detection within the window deters. But as
  compute grows during a compliant pause, a secret advance reaches the frozen frontier sooner: the
  catch-up time falls from [12 months](numbers.md#org-gan-catchup-start) to
  [5.74 months](numbers.md#org-gan-catchup-24) over a pause of [24 months](numbers.md#org-gan-pause-months),
  a fall of [52%](numbers.md#org-gan-catchup-fall), and a follower with the leader's compute catches up
  in [4.4 months](numbers.md#org-gan-equal-catchup) [@gan2026clock]. All of these are calibration
  values, not measurements.
- **A known line turns a dilemma into coordination.** In Barrett and Dannenberg's experiment, with
  [10 groups](numbers.md#org-ba-groups) per treatment, a known catastrophe threshold was avoided by
  [8](numbers.md#org-ba-known-avoided) groups; when the threshold's location was uncertain, catastrophe
  was certain in [9](numbers.md#org-ba-uncertain-catastrophe) [@barrett2012climate].
- **The race may be a stag hunt, not a prisoners' dilemma.** The hardwired-pause working group argues
  that frontier AI may be a coordination game, and that a repeated game with an unknown end date and
  informative public signals supports simple cooperative equilibria [@fithian2026hardwired].
- **Without penalties on outsiders, coalitions stay small.** Nordhaus shows that "without sanctions
  against non-participants there are no stable coalitions other than those with minimal abatement":
  with identical countries, only coalitions of [2 countries](numbers.md#org-nordhaus-stable-low) or
  [3 countries](numbers.md#org-nordhaus-stable-high) are stable. A small trade penalty on non-members
  changes that; a [5%](numbers.md#org-nordhaus-tariff) tariff almost reaches one of his higher carbon-price targets
  [@nordhaus2015climate]. Rahman draws the AI conclusion: "Remaining outside the agreement should be
  economically costly" [@rahman2025nonparty].
- **Subcritical parties can be supercritical together.** Burtsev shows that a network of labs or blocs
  can amplify self-improvement even when each is damped on its own, because advances transfer between
  them [@burtsev2026criticality]. Sharing AI research across parties is itself a coupling.
- **Deterrence by sabotage.** Hendrycks, Schmidt and Wang propose Mutual Assured AI Malfunction, in
  which a bid for unilateral dominance meets preventive sabotage by rivals
  [@hendrycks2025superintelligence]. It is a strategy, not a formal model.

The field evidence fits the models' premise. A senior analyst testified that without export
controls "it is possible, perhaps even likely, that the first million chip AI cluster would be built
in China", and that the controls "did not so much destroy demand as change its composition"
[@allen2025senate]. The controlling state has itself been pulled by commercial and diplomatic
pressure. It published the diffusion rule in January 2025, which among other things required a licence for the
weights of closed models trained on more than [1e+26 operations](numbers.md#org-diffusion-weights)
[@bis2025diffusion], and rescinded it in May 2025, saying it "would have stifled American innovation" [@bis2025rescission]; in December 2025 it
approved H200 sales to China for a [25%](numbers.md#org-h200-fee) duty [@james2025h200]. Those are race
dynamics acting on the chokepoint itself.

**The steelman against the memo.** The memo's protocol raises mutual information (sealed
declarations, evaluations at checkpoints) and restricts resources (licensed compute). In Armstrong et
al.'s model, and in Emery-Xu et al.'s when races are decisive, more information raises risk, because
parties who learn they are close cut safety to win. Bueno de Mesquita et al. find that restricting
resources may backfire. Coe and Vaynman show that states refuse monitoring that exposes their
security. On this reading, a regime that tells every party exactly where every other party stands
could make the race it watches more dangerous. The memo had no answer to this.

**The reply, in part cut by E6.** The protocol need not reveal what those models reveal. Their
information is about capability ranks: who is ahead and by how much. A declaration can instead
reveal compliance: that each party's holdings are below the line. And the protocol changes the
prize, not only the information. If no party can reach a decisive advantage within the regime's
detection and response time (D4), decisiveness falls, and low decisiveness is exactly the condition
under which Emery-Xu et al. find public information safer than private. That comparison rests on
their Proposition 2, which our reimplementation in E6 does not find to be an equilibrium (a
deviation gains up to [0.017](numbers.md#e6-ex-prop2-br-gain-max)); that is our reimplementation's
finding, pending an independent check, and nothing here rests on it either way. Fudenberg and Koh's
result and Barrett and Dannenberg's experiment both favour a known, verified line. The compliance
half of the reply failed its test: in E6, revealing only that each party is below the line raised
risk (below). None of this is proved here.

### What the survey changed

The memo labelled race models prior work, and they are: Armstrong et al., Askell et al., Han et al.,
Stafford et al., Emery-Xu et al., Hendrycks et al., Fudenberg and Koh, and Bueno de Mesquita et al.
The memo implicitly assumed that transparency stabilises a race. **Prior work does not settle that,
and two well-known models say the opposite under some conditions.** The survey found no race model
that includes a verification regime with a stated detection time and asks how that time changes
equilibrium safety. Gan's bilateral model with a response window is the closest [@gan2026clock]; it
has no coalitions and no choice of what to disclose. That it is missing is a claim about our search.
E6 builds that combination as a tool, not a claim; the claims file defers it, so nothing about it is
claimed, and the one candidate it tested, compliance-only disclosure, is cut (below).

### What it means for the protocol

Candidates for how the protocol changes the payoffs:

1. **Cap the prize.** Keep every party's breakout time longer than the regime's detection and
   response time, so no lead is decisive within the window (lowers advantage and decisiveness).
2. **Shorten detection.** Fast, reliable detection lowers exposure: cooperating costs less if
   defection is caught.
3. **Publish the line.** A known threshold makes compliance a coordination equilibrium; a disputed
   breakout estimate behaves like an uncertain threshold and restores the dilemma
   [@barrett2012climate].
4. **Disclose compliance, not rank: cut by E6.** Declarations that show rivals only that holdings
   are below the line gave a higher disaster risk than no information in every calibrated cell and
   than private information alone in every cell; they were safer than public capability in most. In
   these models, on our reading, a public verdict of compliance still tells rivals enough about rank
   to sharpen the race. What Part II discloses, and to whom, has to be weighed against that;
   capability goes only to the evaluators who need it.
5. **Penalise staying out.** Denial of chips and cloud to non-members is the club penalty Nordhaus
   finds necessary for a large coalition [@nordhaus2015climate]; the chokepoints of O3 are what make
   that penalty available.
6. **Watch transfers.** Cross-party transfer of AI research advances couples otherwise subcritical
   parties [@burtsev2026criticality].

The cost to useful AI of the first three is low: they bind only the approach to the line. The fifth
costs outsiders, which is its purpose, and risks the counter-pressure noted under O1. The sixth
would cost open science and needs a narrow definition to be acceptable.

### What would test it

E6 (defection and coalition games) should implement Armstrong et al.'s model, Emery-Xu et al.'s
logistic contest and Fudenberg and Koh's pacing game with a verification regime added: a detection
rate, a response time, and four information regimes (none, private, public capability, public
compliance only). The test reports equilibrium safety across decisiveness and enmity. The candidate
"compliance-only declarations do not raise risk" was to survive only if risk under compliance-only
disclosure was no higher than under no information in every calibrated regime.

E6 has run, and the candidate is cut. Over [72 cells](numbers.md#e6-o2-cells) of capability range,
enmity, decisiveness and line position, compliance-only disclosure gave a higher disaster risk than
no information in [100%](numbers.md#e6-o2-compliance-over-none) of cells and than private
information alone in [100%](numbers.md#e6-o2-compliance-over-private); it was riskier than public
capability in [12%](numbers.md#e6-o2-compliance-over-public), and public capability was riskier than
private information in [96%](numbers.md#e6-o2-public-over-private). The models and the calibrations
are the published ones, so this is a finding inside those models, not about real parties. E6 also
reproduces Nordhaus's analytic case: with no sanction the stable coalitions of identical countries hold
[2 countries](numbers.md#e6-nordhaus-stable-min) to
[3 countries](numbers.md#e6-nordhaus-stable-max), as he gives, and a penalty on non-members of
[0.63](numbers.md#e6-nordhaus-penalty-n10) of a member's abatement cost makes the grand coalition
stable. Measured payoffs for AI, and the penalty in denied chips, remain untested.

## O3. Chokepoints

### Definition

A stage of the supply chain is a **chokepoint** for the protocol when four measured conditions hold:

1. **Few suppliers:** one to three firms hold most of world capacity.
2. **Countable output:** units made each year are recorded at the plant, by the maker, with an
   identity per unit.
3. **Slow substitution:** the **erosion horizon** H (the years until a party outside the protocol
   could replace the stage's output at volume) is longer than the protocol's detection and response
   time.
4. **Visible plants:** the plants are few, large and hard to hide.

Two measured quantities then rank chokepoints. The erosion horizon H says how long a chokepoint
holds. The **leak fraction** l says how much of its downstream output ends up outside accounting, as
a share of the total. A chokepoint is only as good as its horizon is long and its leak fraction
small.

### How it is measured

Supplier counts and output come from O1. The erosion horizon is estimated from the state of rival
technology (how far the best non-member node or tool is from volume production) and from build
times; its sources are weak (unnamed-source reporting, public summaries of teardown analyses). The
leak fraction is estimated by models of smuggling and resale, each resting on an assumed detection
rate. Neither quantity is counted; both are modelled, and their errors are wide.

### The evidence: a narrow core

Ranked by durability, from the survey's evidence:

1. **EUV lithography** is the most durable. One firm makes the tool; output was
   [48 EUV systems](numbers.md#org-euv-2025) in 2025 and can grow about
   [30%](numbers.md#org-euv-capacity-growth-2027) a year at plan. China's prototype EUV machine
   reportedly generates EUV light but "is not yet making chips"; chips are targeted for
   [2028](numbers.md#org-china-euv-target), and other experts project
   [2030](numbers.md#org-china-euv-expert) as more likely, on unnamed sources relayed from Reuters
   [@washenko2025euv]. Volume would come later.
2. **Leading-edge logic** is next. TSMC holds [72.5%](numbers.md#org-tsmc-share-2q26) of foundry
   revenue. SMIC's N+3 node "remains significantly less scaled than leading commercial 5nm nodes"
   [@techinsights2025kirin], and a DUV-only route "will not be a viable solution for data center AI
   chips" because of low yields [@techinsights2026datacenter] (both public summaries). But logic
   capacity is not what binds China's AI chips: SMIC had about
   [45,000 wafers a month](numbers.md#org-smic-wspm-2025) of advanced-node capacity at end 2025, against
   at most [20,000 wafers a month](numbers.md#org-ascend-wspm-need) that Ascend production needs
   [@patel2025ascend]. The node is worse; the volume is not short.
3. **HBM** is eroding. It is a three-firm stage, but CXMT is growing, an analyst projects about
   [2 million HBM stacks](numbers.md#org-cxmt-hbm-2026) from it in 2026, and Huawei has announced its own
   HBM [@patel2025ascend; @xu2025huaweiconnect]. SemiAnalysis judges that "HBM production is the
   bottleneck" for China [@patel2025ascend].
4. **Advanced packaging** is the least durable by volume: it grows more than
   [80%](numbers.md#org-cowos-cagr) a year and is partly done by outside assemblers, and China is
   strongest in assembly and packaging [@khan2021supplychain].
5. **Finished chips and servers** are where the leaks are (next section).
6. **Power** is not a chokepoint (O1).

Allen's testimony, citing Bernstein, supports ranking by technical difficulty rather than by the
strength of the rule applied: "the rate of China's progress toward self-sufficiency is best predicted
by the market and technological complexities of each semiconductor market segment, not by the extent
to which export controls were applied"; and "the most important export controls" are "those related
to advanced semiconductor manufacturing equipment" [@allen2025senate].

This ranking is a judgement made in 2026 with the erosion in view, and the test of rankings of this
kind does not support it. E23 ranked [9 stages](numbers.md#e23-stages) that were chokepoints against
China on data public at the end of 2022 and scored the ranking against the erosion found from 2023 to
November 2026 ([27 events](numbers.md#e23-events), a lower bound, since only events our searches found
count). Spearman's rho was [0.28](numbers.md#e23-rho), one-sided p [0.23](numbers.md#e23-p), with a
95% interval from [-0.49](numbers.md#e23-rho-lo) to [0.80](numbers.md#e23-rho-hi). Part I's own order
of five stages scores [0.30](numbers.md#e23-rho-part1), a reference only, since it was made after the
fact (below).

The rules that already stand on these stages show the core can be held, and gamed. The October 2022
rule controlled chips by interconnect rate and processing performance, and fabs by node
[@bis2022advancedcomputing]. In October 2023 it was patched: the new rule added a performance-density
test (a total processing performance of [4,800](numbers.md#org-eccn-tpp), or
[1,600](numbers.md#org-eccn-tpp-pd) with a density of [5.92](numbers.md#org-eccn-pd)) to prevent "the
workaround of simply purchasing a larger number of smaller datacenter AI chips"
[@bis2023advancedcomputing]. HBM was controlled only in December 2024, above
[2 GB/s per mm2](numbers.md#org-hbm-control) of bandwidth density, a line every HBM stack then in
production exceeds [@bis2024hbm].

### The evidence: leaks at the edges

The chokepoints leak at the edges faster than they erode at the core.

- **Smuggling.** Epoch estimates [660,000 H100e](numbers.md#org-smuggled-cum) of compute smuggled into
  China through 2025 (90% CI [290,000 H100e](numbers.md#org-smuggled-cum-low) to
  [1,600,000 H100e](numbers.md#org-smuggled-cum-high)), roughly [33%](numbers.md#org-smuggled-share-china)
  of China's total compute and [3%](numbers.md#org-smuggled-share-global) of the world's
  [@juniewicz2026smuggling]. That implies a Chinese total of about
  [2.0 million H100e](numbers.md#org-china-implied-stock), our inference from "roughly a third", not a
  stated figure. Allegations of diverted or missing chips already total almost
  [300,000 H100e](numbers.md#org-allegations-cum). The model assumes that
  [25%](numbers.md#org-diversion-detect) of diversion cases are detected (90% CI
  [10%](numbers.md#org-diversion-detect-low) to [80%](numbers.md#org-diversion-detect-high)): an
  assumption, but the only explicit detection rate for chip accounting the survey found. CNAS puts
  2024 smuggling at a median of [140,000 chips](numbers.md#org-smuggled-2024-chips), a distribution
  rather than a count of cases, and notes that the profits from three reported cases, about
  [140 million USD](numbers.md#org-smuggling-profit-3), are [2.5](numbers.md#org-smuggling-profit-ratio)
  times BIS's annual export enforcement budget of about [55 million USD](numbers.md#org-bis-enforcement)
  [@grunewald2025smuggling]. In a 2026 case the defendants allegedly staged thousands of dummy servers
  to deceive auditors and a Commerce Department inspection [@doj2026supermicro]; the charges are
  allegations, not findings.
- **Stockpiles and die banks.** Huawei received more than
  [2.9 million Ascend dies](numbers.md#org-huawei-die-bank) made at TSMC [@patel2025ascend], although the
  2020 entity listing was meant to cut its Ascend line off from TSMC [@allen2025senate]. China bought
  about [13 million HBM stacks](numbers.md#org-china-hbm-stockpile) before the December 2024 HBM
  control, enough for [1.6 million Ascend 910C packages](numbers.md#org-hbm-stockpile-packages)
  [@patel2025ascend]. A stockpile bought before a rule delays the rule's effect.
- **Estimates that disagree.** For Huawei's 2025 output, the US Commerce Department gave a capacity of
  at most [200,000 Ascend chips](numbers.md#org-huawei-commerce-2025) [@zafar2025kessler], SemiAnalysis
  [805,000 Ascend units](numbers.md#org-huawei-semianalysis-2025) shipped [@patel2025ascend], and IDC
  about [812,000 AI chips](numbers.md#org-huawei-idc-2025) shipped in China [@pan2026idc]. The units
  differ (capacity against shipments, possibly including die-bank chips), but the spread is a factor of
  [4.1](numbers.md#org-huawei-spread). Epoch's own estimate, in compute rather than units, is
  [530,000 H100e](numbers.md#org-huawei-h100e-2025) [@epoch2026chipsales]. That spread is the measured
  error of today's outside chip accounting for a state-backed maker.
- **Chips nobody can place.** After Epoch traced most chips to owners, a recent taxonomy reports
  "on the order of a million chips unaccounted for", about [1 million chips](numbers.md#org-chips-unaccounted)
  [@koopmanschap2026gpu].
- **The holder chooses to sell.** The leak the memo did not foresee is political. The controlling state
  rescinded its own country-cap rule within months, and then sold a previous-generation chip to China
  for a duty (O2). ASML sold [33%](numbers.md#org-asml-china-units-2025) of its tools by unit to China in
  2025 [@shilov2026asml]. IDC counts about [4.0 million units](numbers.md#org-china-accelerators-2025) of AI
  accelerators shipped in China in 2025, [55%](numbers.md#org-nvidia-china-share-2025) of them Nvidia's
  [@pan2026idc]. The flexHEG authors note that "states capable of chip production could still
  gradually exit the agreement unilaterally by resuming production of non-flexHEG chips"
  [@petrie2025flexheg1]. A chokepoint held by one state is held only as long as that state's
  commercial and diplomatic interests agree.

Decentralised training is not yet a leak at frontier scale. Its compute grows about
[20](numbers.md#org-decentral-growth) times a year by one author's estimate, but its largest runs reach
only about [6e+23 FLOP](numbers.md#org-decentral-largest), about [1,000](numbers.md#org-decentral-gap) times below the largest
models, and the author expects it not to catch up this decade [@sevilla2025decentralized]. That is an
essay, not Epoch's official position; the growth rate is the number to watch.

### The evidence: denial makes programmes bigger and more visible

A party denied the leading edge does not stop; it scales out, and scaling out shows. Huawei says "we
don't have access to advanced process nodes, so we've decided to focus our efforts on making
breakthroughs by combining" chips, and plans SuperPoDs of up to
[8,192 chips](numbers.md#org-ascend-superpod) and a SuperCluster of over
[500,000 NPUs](numbers.md#org-ascend-supercluster) [@xu2025huaweiconnect] (vendor claims). Epoch estimates
that Huawei's Horinger site holds about [81,000 H100e](numbers.md#org-horinger-h100e) on
[286 MW](numbers.md#org-horinger-power) of IT power, that a given power capacity in China supports only
[40%](numbers.md#org-china-compute-per-power) of the compute of leading US facilities, and that Colossus 2
has about [14](numbers.md#org-colossus2-vs-horinger) times Horinger's compute [@cottier2026horinger]. A
denied party therefore needs about [2.5](numbers.md#org-denial-power-multiplier) times the power per unit
of compute. Older chips cost "at least an order of magnitude" more, a factor of
[10](numbers.md#org-older-chip-cost), in costs and slowdowns [@khan2020aichips], and DeepSeek's chief
executive said restrictions force [2](numbers.md#org-deepseek-penalty-low) to
[4](numbers.md#org-deepseek-penalty-high) times the computing power [@allen2025senate]. Large sites are
already measured from their cooling plant [@epoch2025datacentershub], though finding an undeclared site
from scratch is harder [@krawec2026], and satellite surveillance is reported to detect facilities above [10 MW](numbers.md#org-sat-reliable-mw) reliably [@koopmanschap2026gpu]. Denial
pushes a denied party's programme up the curve of what can be seen.

**The steelman against.** Denial also builds the substitutes it is meant to prevent. CXMT's share
grew, Huawei announced its own HBM, China's EUV prototype exists, and the share of top AI talent
working in China rose (O1). The controls "did not so much destroy demand as change its composition"
[@allen2025senate]. Over a long horizon, denial may shrink the holder's market, fund the rival's
substitutes and leave a large state outside any agreement, which Nordhaus's result says a coalition
cannot afford without a penalty it can impose. Whether denial lengthens or shortens the erosion horizon
is not settled by the evidence here.

### What the survey changed

The memo implicitly assumed that a chokepoint, once held, stays held. **That was wrong.** The
survey found diversion through intermediaries, stockpiles bought ahead of rules, a factor of [4.1](numbers.md#org-huawei-spread)
in outside estimates, and the holder choosing to sell. The protocol's failure list must add two items:
diversion at the edges, and reversal by the chokepoint holder.

O3 as the memo framed it (stand at the stages with the fewest suppliers and the largest plants) is
**prior work**. Sastry et al. argue that compute "is detectable, excludable, and quantifiable, and is
produced via an extremely concentrated supply chain" [@sastry2024compute] (abstract and the first part
of the full text read). Shavit proposed monitoring the chip supply chain so that no actor can avoid
discovery, with firmware snapshots of weights [@shavit2023chinchilla]. MIRI's draft agreement already
proposes chip tracking that "relies on the concentrated chip supply chain", monitoring that "will start
with fabrication", including HBM, packaging and assembly, a halt to AI chip production wherever tracking
is not feasible, training prohibited above [1e+24 FLOP](numbers.md#org-miri-strict) and monitored above
[1e+22 FLOP](numbers.md#org-miri-monitored), and no more than [16 H100e](numbers.md#org-miri-cluster)
outside monitored facilities [@scher2025agreement]. This is close to the protocol's compute half. The
difference visible from what was read is that MIRI sets fixed compute thresholds, while the memo's line
is a time-based breakout test (D3, D4) that lets useful AI keep improving above any fixed figure. CSET
[@khan2020aichips], CNAS [@grunewald2025smuggling], the export rules themselves and Epoch's satellite
work [@epoch2025datacentershub] are also prior work.

Two pieces were not found done quantitatively: ranking stages by durability using measured growth and
erosion evidence, and treating the footprint growth that denial forces (the
[2.5](numbers.md#org-denial-power-multiplier) times power per unit of compute) as a detection gain to set
against the physical chapter's footprint floor. That is a claim about our search only, and neither is
claimed. The ranking is too small, and E23 now measures how small: at the observed rho a rank test
would need [85 stages](numbers.md#e23-n-needed) to tell the 2022 ranking from a random one, while the
2022 supply-chain dataset lists [79 inputs](numbers.md#e23-eto-inputs-2022), nested and correlated, so
fewer independent stages than that. The detection gain is merged into the footprint floor
([C8](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool)),
where E8 measures it. O3 is prior work ([novelty file](03-novelty.md#o3-chokepoints)).

### What it means for the protocol

A candidate, not a finding.

1. **Register at birth, at the narrow stages.** New AI chips get a unit identity where they are made,
   tied to EUV tool records, foundry wafers, HBM stacks and packaging. The yearly flow from all
   vendors is about [13.6 million H100e](numbers.md#org-sold-2025), and more than [70%](numbers.md#org-hyperscaler-share) of
   the stock sits with five owners. The cost to useful AI is low; makers already keep unit records.
2. **Bind the holders, not only the buyers.** The leak the protocol cannot verify its way out of is the
   holder's own decision to sell. The states that host EUV, leading-edge fabs and HBM must be bound by
   the same k-of-n rules as everyone else, so that no single holder can reopen the gate.
3. **Start the line from the hole.** The registry will begin with unaccounted compute: the smuggled
   stock, die banks, stockpiled HBM and untraced legacy chips. The line (D4) should be computed as if
   the worst-placed party holds all of it. For scale, against the hardwired-pause working paper's
   covert evasion fleet threshold of [6.4 million H100e](numbers.md#org-hwp-fe) for year-end 2026
   [@fithian2026hardwired], the compute smuggled into China through 2025 is about
   [10%](numbers.md#org-smuggled-share-of-fe), and China's implied total about
   [31%](numbers.md#org-china-stock-share-of-fe). But that threshold is only
   [0.47 years](numbers.md#org-fe-years-of-sales) of 2025's global chip sales, while the paper's overt
   breakout fleet of [180 million H100e](numbers.md#org-hwp-fb) is [13 years](numbers.md#org-fb-years-of-sales)
   of them, and more than the paper's own projected global fleet of
   [47 million H100e](numbers.md#org-hwp-global-2026). Their thresholds are assumptions and their horizon of [2 years](numbers.md#org-hwp-tb) is
   chosen by judgement. Both thresholds are also proportional to that paper's assumed breakout budget
   of [2e+29 FLOP](numbers.md#def-hwp-breakout-budget): at its frozen frontier of
   [2e+27 FLOP](numbers.md#claim-hwp-frozen-frontier) the whole projected fleet would need only
   [28 days](numbers.md#claim-whole-fleet-days-frozen), and both thresholds would shrink in proportion.
   So the comparison holds at one assumed number and does not show whether the leak or the core sets
   the margin for covert work; the claims file downgraded the coalition result built on it for the
   same reason ([C7](04-claims.md#c7-the-coalition-share-derived-from-the-response-time)). What
   survives is narrower: the smuggled stock is the share of the covert threshold given above even at
   that paper's large budget, and a smaller budget only raises that share.
4. **Use denial as a detection gain.** A denied party's programme needs more power and bigger sites;
   the protocol should count that as a gain in the power and imagery channels, not only as a cost to
   the denied party. The gain belongs to the footprint floor (C8), and E8 finds it delays a power
   channel's crossing by years, not decades (below).

### What would test it

E5 (multi-channel verification Monte Carlo) has run with the smuggling model's diversion detection
([25%](numbers.md#org-diversion-detect) detected, 90% CI [10%](numbers.md#org-diversion-detect-low) to
[80%](numbers.md#org-diversion-detect-high)) as a channel, merged with imagery and intelligence because
they share sources of tips. For smuggled chips spread over sites below the satellite line its detection
time at the prevention miss chance is a median of [32 years](numbers.md#e5-td-distributed-years), and for
the untraced pool, where no acquisition is left to catch, [32 years](numbers.md#e5-td-pool-years), against
[39.0 days](numbers.md#e5-td-declared-days) on the declared path. Both are lower bounds, since the
historical rate inside them is an upper bound. The factor of [4.1](numbers.md#org-huawei-spread) in
outside estimates is not yet in E5 as a counting error. E8 (the footprint floor against detection
limits) has applied the denial multiplier of [2.5](numbers.md#org-denial-power-multiplier): for a fixed
compute it delays a power channel's crossing by [3.1 years](numbers.md#e8-denial-delay-years), and a
[1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run on one site over a pause's run length draws at least
the satellite line in [60%](numbers.md#e8-concentrated-1e26-pause-seen-denied) of draws for a denied
party against [19%](numbers.md#e8-concentrated-1e26-pause-seen) otherwise. The gain is partial: it
postpones the year a single site falls below the satellite line, but chips spread over sites below that
line are still found only on E5's timescale of decades (above). **E23, the durability backtest**, has
run. It ranked [9 stages](numbers.md#e23-stages) by a rule fixed on data public at the end of 2022
(more Chinese suppliers, more predicted erosion; power left out, since China was the largest
generator) and scored the ranking against the erosion found from 2023 to November 2026. The ranking is
not supported: rho is [0.28](numbers.md#e23-rho), one-sided p [0.23](numbers.md#e23-p), and the
smallest rho the test could call significant with these stages is
[0.59](numbers.md#e23-rho-critical). The test had power [0.16](numbers.md#e23-power-here) even if the
observed rho were true. The result moves with every choice: leaving one stage out gives
[-0.04](numbers.md#e23-rho-loo-min) to [0.54](numbers.md#e23-rho-loo-max); over six rules and six
erosion scorings rho runs from [-0.69](numbers.md#e23-rho-alt-min) to
[0.29](numbers.md#e23-rho-alt-max), median [0.08](numbers.md#e23-rho-alt-median); with power put back
it is [0.09](numbers.md#e23-rho-full). A test that could separate the ranking from chance would need
[85 stages](numbers.md#e23-n-needed). So the ranking stays unclaimed: the data cannot test it, and
the window of under four years may be too short to show slow erosion such as EUV's.

## O4. Covert supply: how secret programmes were run and found

### Definition

A covert programme is one a party runs outside its declarations. O4 records two things for each
programme: its **time undetected** (years from the decision or construction start to the first
outside discovery) and its **discovering channel** (the inspectorate, national intelligence, a
defector, the media, interdiction of supplies, or the party's own disclosure). Over a set of
programmes, the **discovery rate** is the number of discoveries divided by the programme-years
undetected (per year): the hazard, if discovery arrived at a constant rate. For AI, O4 asks who could
assemble the inputs of O1 outside the registry of O3, and how they would most likely be found.

### How it is measured

From IAEA reports, government statements and histories of the programmes, as collected in survey
track 08. Dates carry errors of months to years. The set is a convenience sample of programmes that
were eventually found: programmes never found are missing by construction, which pushes the true
discovery rate down, and programmes found quickly may be under-represented, which pushes it up. The
channels are those of other domains (nuclear and biological weapons), not of AI.

### The evidence

| Programme | Years undetected | How it was found |
|---|---|---|
| Iraq, nuclear | about [10 years](numbers.md#org-iraq-years) | intelligence, then post-war inspections |
| Libya, nuclear | about [20 years](numbers.md#org-libya-years) or more | interdiction of a shipment, then negotiated disclosure |
| Iran, centrifuges | [17 years](numbers.md#org-iran-years) | public media reports, then environmental sampling |
| Iran, Fordow | [3 years](numbers.md#org-fordow-years-low) to [7 years](numbers.md#org-fordow-years-high) | Western intelligence, then commercial imagery |
| Syria, reactor | about [6 years](numbers.md#org-syria-years) | national intelligence, after the site was destroyed |
| USSR, Biopreparat | [16 years](numbers.md#org-biopreparat-years) | a defector |
| South Africa, nuclear | [15 years](numbers.md#org-sa-years) active, never detected while active | self-disclosure |

- **Iraq.** Iraq decided in late 1981 to build enrichment capability [@albright-2002]. Before the 1991
  war the IAEA's knowledge was limited to its inspections of declared areas at Tuwaitha, which covered
  only part of the site; "there had been speculation for some years in the press ... but no hard
  information was available" [@thorne-1992]. After the war, inspectors at Tarmiya noted "the huge
  electrical load the site had required", which "did not fit with Iraq's declared use"; Iraq had
  buried the power lines to hide its consumption [@albright-2002]. "A dramatic increase in available
  intelligence information" drove the inspections that exposed a programme "large, well-organized, and
  well-funded" [@thorne-1992].
- **Libya.** Its undeclared programme involved [12 sites](numbers.md#org-libya-sites) from the early
  1980s [@iaea-gov-2004-12]. The first inspections by US and UK officials in October 2003 coincided with the
  interdiction at Taranto of centrifuge parts bound for Libya, and the A.Q. Khan network had supplied
  centrifuges and a weapon design [@crs-2004-libya].
- **Iran.** The IAEA asked Iran in September 2002 about Natanz and Arak "as reported in the media in
  August 2002" [@iaea-gov-2003-40]. Iran then acknowledged developing centrifuge enrichment for
  [18 years](numbers.md#org-iran-acknowledged-years) from a 1985 decision, and environmental sampling contradicted its account
  [@iaea-gov-2003-75]. At Fordow, three heads of government presented "detailed evidence to the IAEA"
  after Iran had sent a letter mentioning a new facility only days earlier [@whitehouse-2009-qom];
  commercial imagery then showed construction from 2002 [@iaea-gov-2009-74]. Iran declared the site
  only days before the evidence was presented.
- **Syria.** The IAEA learned of the Dair Alzour reactor from information provided after Israel
  destroyed it in September 2007; commercial imagery from 2001 and environmental samples corroborated
  it afterwards [@iaea-gov-2011-30].
- **Biopreparat.** Set up in 1973, after the USSR had signed the Biological Weapons Convention in 1972, it
  employed an estimated [25,000 employees](numbers.md#org-biopreparat-staff-low) to
  [32,000 employees](numbers.md#org-biopreparat-staff-high), and was revealed by the defector Vladimir
  Pasechnik in 1989 to be [10](numbers.md#org-biopreparat-underestimate) times larger than US or British
  intelligence had estimated [@fas-biopreparat; @hoffman-2009]. Western agencies had suspected a
  programme but "lacked solid proof" [@hoffman-2009]: an organisation of tens of thousands ran for
  [16 years](numbers.md#org-biopreparat-years) before a defector supplied it.
- **South Africa.** About [5 years](numbers.md#org-sa-decision-device) passed from the 1974 decision to
  the first device; in these sources the programme was never found while active, and it ended in
  self-disclosure in 1993.
  Completeness was then checked by reconstructing enrichment output from several thousand operating
  records [@vonbaeckmann-1995], the nearest analogue to auditing training logs after the fact.
- **The counter-case.** In this set, the IAEA's own channel worked once, on declared material. Accountancy and
  sampling found inconsistencies in the DPRK's declarations within about
  [9 months](numbers.md#org-dprk-months), and the DPRK gave notice of withdrawal
  [31 days](numbers.md#org-dprk-withdrawal-days) after the IAEA asked for a special inspection
  [@iaea-gc37-1084]. Declared material can be watched on a timescale of months; the response chain then
  failed.

Across the seven undeclared programmes, the shortest time undetected is
[3 years](numbers.md#org-covert-years-min) and the median [15 years](numbers.md#org-covert-years-median).
Taking Fordow at its short end, they add up to [87 years](numbers.md#org-covert-years-sum) undetected,
a discovery rate of about [0.08/yr](numbers.md#org-covert-hazard). E5 reproduces that figure,
[0.080/yr](numbers.md#e5-o4-hazard), and with South Africa's self-disclosure censored, as a survival fit
requires, it falls to [0.069/yr](numbers.md#e5-o4-hazard-censored). E5 then fits a wider, sourced set of
[16 cases](numbers.md#e5-cases), [14 discoveries](numbers.md#e5-events) over
[149 programme-years](numbers.md#e5-exposure-years), and finds [0.094/yr](numbers.md#e5-hazard) (90%
interval [0.057/yr](numbers.md#e5-hazard-lo) to [0.147/yr](numbers.md#e5-hazard-hi)); across choices of
cases and codings it runs from [0.067/yr](numbers.md#e5-sens-min) to [0.101/yr](numbers.md#e5-sens-max),
and the Kaplan-Meier median time to discovery is [9.6 years](numbers.md#e5-km-median-years). Two things
limit what that rate means. It comes from programmes that were all found or disclosed in the end, so it
is an upper bound on a careful evader's rate, and every detection time computed from it is a lower bound;
the size of that bias cannot be measured from this record. And it runs from a programme's start (the
decision or construction), not from a breakout, so it says nothing directly about a window that opens
when a breakout begins. Even counted from the start, discovery is likelier later: the Weibull shape is
[1.49](numbers.md#e5-weibull-shape) ([1.25](numbers.md#e5-weibull-shape-lo) to
[2.12](numbers.md#e5-weibull-shape-hi); a likelihood-ratio test against a constant rate gives p of
[0.09](numbers.md#e5-weibull-lr-p)), and within a year of a programme's start the Weibull fit gives a
discovery chance of [2.6%](numbers.md#e5-weibull-detect-1y), not the constant rate's
[9.0%](numbers.md#e5-hazard-detect-1y). The memo's placeholder inspection channel implies a detection
rate of [1.2/yr](numbers.md#org-memo-detect-rate), [12.8](numbers.md#e5-memo-over-hazard) times the
fitted rate and [11.8](numbers.md#e5-memo-over-sens-max) times the highest any sensitivity variant
gives, and a miss chance of [30%](numbers.md#miss-prob-one-channel) over its placeholder breakout time.
The historical figure measures old channels in other domains, not new ones, and it applies only to
paths those channels could see. It still says the memo's placeholder is far from any record.

The inspectorate's own channels did not find these programmes. "The IAEA identifies suspect locations
mainly through voluntary tips from national intelligence agencies", and these tips "appear to be
irreplaceable" [@baker2023nuclear]. The Additional Protocol is "nearly untested" at finding secret weapons
work [@baker2023nuclear]. No state has requested a CWC challenge inspection since 1997
([0 requests](numbers.md#org-cwc-ci-requests)) [@opcw-ec109-dg22], against
[8,649 inspections](numbers.md#org-opcw-insp-total) of declared sites [@opcw-numbers]. The Biological
Weapons Convention has no verification at all. The US rejected the 2001 draft protocol, arguing that
inspections would not give useful information because "almost any facility that does biological work
of any magnitude possesses the capability ... of being diverted" [@mahley-2001]: the closest analogue to
algorithmic progress at fixed compute.

Insiders are a channel, and money moves them. US corporate fraud oversight, a mature system with many
channels (auditors, analysts, the media, employees, regulators), detected about
[31%](numbers.md#org-fraud-detect) of frauds [@dyck2017pervasive]. Employees revealed
[19%](numbers.md#org-fraud-employees) of detected frauds overall, but [46.7%](numbers.md#org-fraud-quitam)
in healthcare, where qui tam rewards apply, against [16.3%](numbers.md#org-fraud-other) elsewhere, a
ratio of [2.9](numbers.md#org-fraud-quitam-ratio) [@dyck2007whistle]. Large AI projects "involve hundreds
of employees", but a party may achieve "sufficient compartmentalization and employee loyalty for all
accomplices to lie" [@baker2025verifying], and a state can coerce in ways a firm cannot, as Biopreparat
shows.

**Who could build superintelligence covertly?** Applying O1 and O3: the binding input for a covert
programme is chips. A covert programme can get them in four ways: (a) diversion and smuggling, which
moved about [660,000 H100e](numbers.md#org-smuggled-cum) into one country through 2025; (b) stockpiles and
die banks bought before rules took effect; (c) a domestic chain at older nodes, which a large state has,
at about [2.5](numbers.md#org-denial-power-multiplier) times the power per unit of compute; and (d) the
untraced legacy stock. Power and talent are not binding for a large state (O1). That narrows the
candidates. A large state with its own chip chain and abundant power could run a programme inside its
territory, larger and more visible than a leading-edge one, and the record suggests it would most
likely be found by rival intelligence and imagery, as Iran and Syria were. A state without a chip chain
depends on the leaks at the edges and needs volume, which is what the smuggling cases expose. A firm
inside a member state holds its compute with a few owners and its secret with hundreds of employees,
where cloud oversight and rewarded insiders should work best, though neither has a measured rate for AI:
in E5 cloud has no channel at all. A decentralised network is, for now, about
[1,000](numbers.md#org-decentral-gap) times below the frontier [@sevilla2025decentralized]. The longest-lived programmes in the
record were state programmes with a domestic industry (Biopreparat, South Africa, Iran) or an illicit
supply network (Libya, Iraq): the AI analogues are a large state with its own chain, and a state
supplied by diversion.

### What the survey changed

The memo listed "random challenge inspections on the chemical-weapons model" and "rewarded
whistleblowing" among its channels, with a placeholder of [4/yr](numbers.md#inspections-per-year) inspections reaching a site.
The record contradicts the inspection channel: no challenge inspection has ever been requested, and
undeclared programmes were found after years by intelligence, defectors, the media and disclosure, not
by inspectors. **For undeclared work, the realistic detection time is years, not months.** The
history itself is prior work (the arms control sources above), and the IAEA's dependence on
intelligence is documented [@baker2023nuclear]. Turning the record into a discovery rate for an AI regime
is this chapter's arithmetic; the survey did not search for prior estimates of it, so no novelty is
claimed. The claims file treats the rate as an input, not a contribution: E5 has refitted it as a
survival model, and it enters C3 through E5
([C3](04-claims.md#c3-detection-as-the-evader-sees-it-the-per-path-evader-minimised-miss)). It is an
upper bound on a careful evader's rate, on a clock that starts with the programme, and it belongs only
to paths that intelligence, defectors and imagery could see.

### What it means for the protocol

A candidate, not a finding.

1. **Do not rely on finding covert work after it starts.** Even at the historical rate, itself an upper
   bound, the median time to discovery was [9.6 years](numbers.md#e5-km-median-years) from a
   programme's start, and a path only those channels see needs [32 years](numbers.md#e5-td-hist-years) from a
   programme's start to reach the prevention miss chance, a lower bound. Compute rented through cloud
   providers or distilled from others' outputs has no measured channel at all, so a breakout on those
   paths is missed with certainty. The protocol must instead keep the covert supply route small: the
   unaccounted compute any party could command must stay below what it would need to break out within
   the discovery time the record supports, which is decades on the watched paths and unbounded on the
   unwatched ones.
2. **Weight the channels that worked.** Supply-side accounting (chips counted at birth, O3);
   intelligence shared among rival blocs, each of which wants to expose the other; and rewarded
   insiders, with rewards rather than protections alone.
3. **Watch declared compute closely.** Declared material was watched on a timescale of months
   (the DPRK case). Registered chips can be too; the gap is undeclared compute.
4. **Expect withdrawal after detection.** The DPRK gave notice within weeks of a special inspection
   request. The withdrawal rules must assume that detection triggers exit. MIRI's draft agreement
   already sets a withdrawal notice of [12 months](numbers.md#org-miri-withdrawal), with covered chips
   and equipment removed or disabled during it, a length chosen for its assurance tasks rather than derived
   [@scher2025agreement].

### What would test it

E5 has fitted the discovery rate properly: a survival model over a wider and documented set of
programmes, with programmes ended by self-disclosure treated as censored, and a sensitivity analysis
over which cases are included (above). Its output, redrawn from the cases in every draw, is now the
rate for the historical channels (intelligence, defectors, the media) in the multi-channel Monte Carlo,
replacing the placeholder. The result that would have
overturned this section was a fitted rate close to the memo's placeholder; the placeholder is instead
[12.8](numbers.md#e5-memo-over-hazard) times the fitted rate, and leaving out any one case moves the
rate only between [0.088/yr](numbers.md#e5-loo-min) and [0.102/yr](numbers.md#e5-loo-max). What E5
cannot do is measure how far a careful evader's rate sits below it: programmes never found are missing
from any record. E6 has not tested withdrawal as a choice. It states the condition instead: with assets
frozen during a notice and the response starting at notice, an exit breakout fails only if breakout
time plus the notice reaches the response time; without the freeze the party can start during the
notice and its length adds nothing. And on E24's record [25%](numbers.md#e24-halt-share-never) of
findings made inside a treaty were never followed by a halt; if that share carries over, an exit
breakout succeeds at least that often whatever the notice. A game in which a party that learns it has
been detected chooses between exit and compliance remains to be built.

## What this perspective contributes to the line

Four quantities from this chapter should enter the protocol, as limits or as inputs to the line.

1. **Registered compute.** New AI chips counted at birth at the narrow stages (EUV tools,
   leading-edge wafers, HBM stacks, packaging) and holdings counted at their owners, in H100e.
   *Measurement:* unit records the makers already keep; about [13.6 million H100e](numbers.md#org-sold-2025)
   a year from all vendors, more than [70%](numbers.md#org-hyperscaler-share) held by five owners. *Weakest point:* it holds
   only while the states hosting the chokepoints bind their own export decisions, and one of them
   reversed a rule within months.
2. **Unaccounted compute.** The stock outside the registry (smuggled chips, die banks, stockpiled
   memory, untraced legacy chips), in H100e. The line should be computed as if the worst-placed party
   holds all of it. *Measurement:* models such as Epoch's, giving
   [660,000 H100e](numbers.md#org-smuggled-cum) smuggled into one country through 2025. *Weakest point:*
   it is estimated, never counted, with a wide interval
   ([290,000 H100e](numbers.md#org-smuggled-cum-low) to [1,600,000 H100e](numbers.md#org-smuggled-cum-high)),
   on an assumed detection rate, and outside estimates of a single maker's output differ by a factor of
   [4.1](numbers.md#org-huawei-spread). In E8 the compute smuggled into one country is already a median
   of [230](numbers.md#e8-smuggled-over-floor-1e26-pause-p50) times the chip floor of a
   [1e+26 FLOP](numbers.md#phys-rahman-1e26-local) run under a pause, at BF16, so while that stock is
   open its path fails the line for every party (C8).
3. **Supply growth and erosion horizon.** How fast new compute can be made (AI compute sold
   [2.67](numbers.md#org-sold-growth) times in a year; EUV capacity doubling in about
   [2.6 years](numbers.md#org-euv-doubling-years); packaging in
   [1.2 years](numbers.md#org-cowos-doubling-years)) and how long until a party outside the protocol can
   make leading-edge chips at volume (first chips targeted for [2028](numbers.md#org-china-euv-target),
   [2030](numbers.md#org-china-euv-expert) by other experts). Together they set how fast breakout time
   shrinks and how long the chokepoint holds. *Weakest point:* the growth figures are vendor guidance
   and the horizon rests on unnamed-source reporting.
4. **Discovery time for undeclared programmes.** The realistic detection time for covert work, from the
   historical record: E5's fitted discovery rate of [0.094/yr](numbers.md#e5-hazard), counted from a
   programme's start, and the [32 years](numbers.md#e5-td-hist-years) a path only the historical
   channels see needs to reach the prevention miss chance. It belongs in the line's detection time only
   for compute outside the registry that those channels could see: an undeclared site, smuggled chips,
   the untraced pool. Cloud and distillation have no measured channel and so no detection time; on those
   paths a breakout is missed with certainty until some channel for them is measured.
   *Weakest point:* a small convenience sample from other domains, with the programmes never found
   missing, so the rate is an upper bound on a careful evader's and every detection time from it a lower
   bound.

Race pressure (O2) is not a trigger. It is a design constraint: on the published models the protocol
should cap the prize and publish the line. The memo's answer to the transparency problem, disclosing
compliance rather than rank, failed its test: in E6 compliance-only disclosure gave a higher disaster
risk than no information in [100%](numbers.md#e6-o2-compliance-over-none) of
[72 cells](numbers.md#e6-o2-cells). So what the protocol discloses, and to whom, must be weighed against
the race it may sharpen.
