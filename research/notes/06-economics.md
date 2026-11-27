# Survey 06: economics, supply chain and organisation

- **Track:** 06, economics and organisation (memo items O1, O2, O3; bears on P1, P4, D3, D4).
- **Date:** 2026-11-27. Every source below was opened on this date.
- **Scope:** the AI chip supply chain and its chokepoints (lithography, leading-edge logic, advanced
  packaging, high-bandwidth memory, chip design), capital spending, training costs, power supply and
  its lead times, talent, race models, US export controls and their measured effects, how fast each
  input grows and how visible each stage is.

## Summary

1. **The chokepoints are real, narrow and countable.** One firm makes EUV scanners: ASML recognised
   48 EUV systems in 2025 (44 in 2024), plans about 65 low-NA EUV shipments in 2026 and about 30% more
   capacity in 2027. TSMC took 72.5% of all foundry revenue in Q2 2026, and in 2022 Taiwan and South
   Korea held all sub-10 nm logic capacity (69% and 31%). Three firms make HBM (SK hynix 50%, Samsung
   33%, Micron 18% of Q2 2026 revenue). TSMC's CoWoS packaging is 120,000 to 140,000 wafers a month in
   2026. The whole flow of AI chips is small enough to count: about 13.6 million H100-equivalents sold
   in 2025 by Epoch's estimate, Nvidia about 65% of it. These are few plants, each very large, slow
   to build (a fab takes about 682 days from construction start) and run by firms that already keep
   unit-level records.
2. **The chokepoints leak at the edges faster than they erode at the core.** China's domestic EUV
   is a prototype that makes no chips yet (target 2028, experts say 2030), and SMIC's best node (N+3)
   is still well short of 5 nm. But diversion is large: Epoch estimates 660,000 H100e (90% CI
   290,000 to 1.6 million) smuggled into China through 2025, about a third of China's AI compute;
   SemiAnalysis counts more than 2.9 million TSMC-made Ascend dies in Huawei's die bank, though
   the 2020 entity listing was meant to cut Huawei off from TSMC (allen2025senate, p. 4); China
   stockpiled about 13 million HBM stacks before the December 2024 controls. And the controlling
   state reversed itself: the January 2025 diffusion rule was rescinded in May 2025, and H200 sales
   to China were approved in December 2025 for a 25% fee. **This contradicts the memo's implicit
   assumption that a chokepoint, once held, stays held.** The protocol's failure list should add
   diversion through intermediaries and the chokepoint holder choosing to sell.
3. **Denial changes the shape of a program, and the new shape is more visible.** Huawei says it has
   no access to advanced nodes and so scales out (8,192-chip SuperPoDs, a planned 500,000-NPU
   SuperCluster). Epoch estimates Huawei's Horinger site supports only 40% of the compute per unit of
   power of leading US sites, and that "China appears to have no shortage of energy." So a party
   denied leading-edge chips needs more chips, more power and bigger buildings for the same compute,
   and large AI sites are already found from satellite images of their cooling plant.
4. **Power is a rate limit in the US, not a chokepoint.** US grid connection takes a median 61
   months, large transformers 128 weeks, large gas turbines are booked into 2029 to 2030. But China
   added 315 GW of solar and 119 GW of wind in 2025 alone. **This contradicts the memo's listing of
   power among the physical chokepoints** (the reasons under the pathway table: "chips, fabs,
   power"): power slows US
   build-out and is a good detection channel (P4), but no small set of suppliers controls it globally.
5. **Prior art covers more of O3 and of the protocol's compute half than the memo assumes.**
   Sastry et al. (2024) already argue compute is "detectable, excludable, and quantifiable" and made
   in "an extremely concentrated supply chain." MIRI's draft treaty (Scher et al., 2025) already
   proposes chip tracking that "relies on the concentrated chip supply chain," production monitoring
   from fabrication including HBM, FLOP thresholds (10^22 monitored, 10^24 prohibited), a 16
   H100-equivalent cluster limit, and research restrictions against algorithmic progress.
6. **Race models disagree on whether transparency helps.** Armstrong, Bostrom and Shulman find more
   information about capabilities raises risk; Emery-Xu, Park and Trager find public information is
   safer except when races are decisive; Fudenberg and Koh (2026) find hidden capabilities make
   mutual pacing harder. Bueno de Mesquita, Dziuda and Polborn (2026) find restricting resources
   "may backfire" in some regimes. The protocol's sealed declarations raise information; whether that
   stabilises or destabilises is not settled by prior work and should be modelled, not assumed.
7. **Outside estimates of a rival's chip output disagree by a factor of about four** (Huawei 2025:
   at most 200,000 per the US Commerce Department; about 805,000 per SemiAnalysis; about 812,000
   shipped per IDC). That spread is a measured input for the miss rate of the chip-accounting channel.

---

## Sources

### khan2020aichips
*AI Chips: What They Are and Why They Matter.* Saif M. Khan and Alexander Mann, CSET, April 2020.
DOI 10.51593/20190014. Opened 2026-11-27 (publication page and summary).
- On concentration: "the complex supply chains needed to produce leading-edge AI chips are
  concentrated in the United States and a small number of allied democracies provides an opportunity
  for export control policies."
- "U.S., Dutch, and Japanese firms together control the market for semiconductor manufacturing
  equipment (SME)"; US, Taiwanese and South Korean firms "control the large majority" of
  leading-edge fabs.
- Cost of using older chips: "overall costs and slowdowns at least an order of magnitude greater"
  than state-of-the-art chips. This is the economic reason denial of the leading edge bites.
- Bears on: O1, O3, P1.

### khan2021supplychain
*The Semiconductor Supply Chain: Assessing National Competitiveness.* Saif M. Khan, Alexander Mann,
Dahlia Peterson, CSET, January 2021. DOI 10.51593/20190016. Opened 2026-11-27 (publication page).
- US industry contributes 39% of the value of the global semiconductor supply chain; Japan, Europe,
  Taiwan and South Korea another 53%; China 6%.
- China is strongest in assembly, testing and packaging, weakest in "production inputs: SME, EDA,
  core IP" and some materials. The US lacks photolithography firms, "the most expensive and complex
  form of SME."
- Bears on: O1, O3.

### varadarajan2024resilience
*Emerging Resilience in the Semiconductor Supply Chain.* Raj Varadarajan, Iacob Koch-Weser, Chris
Richard, Joseph Fitzgerald, Jaskaran Singh, Mary Thornton, Robert Casanova, David Isaacs (BCG for
SIA), May 2024. URL below. Opened 2026-11-27 (full PDF).
- Executive summary (PDF p. 4): the industry had "at least 50 points across the supply chain where
  one region held over 65% of global market share."
- Projected private fab investment of about $2.3 trillion in 2024 to 2032, against $720 billion in
  2013 to 2022. US fab capacity +203% from 2022 to 2032; US share of global fab capacity from 10% to
  14% (8% without the CHIPS Act).
- Exhibit 6 (PDF p. 14): sub-10 nm logic capacity in 2022 was South Korea 31%, Taiwan 69%; text:
  "In 2022, the United States did not produce any advanced logic chips"; by 2032 the US is
  projected at about 28% and more than 40% of advanced logic outside South Korea and Taiwan.
- Exhibit 10 (PDF p. 18): lithography equipment revenue by vendor HQ region, EU 89%, Japan 10%,
  US 1%, market size $17.5 billion.
- Bears on: O1, O3. Against the memo: leading-edge fabs are dispersing (more sites to watch, but
  in allied states).

### asml2026annualreport
*ASML Annual Report 2025, Financial performance section* (extract). ASML Holding, published 2026.
URL below. Opened 2026-11-27 (PDF, text extracted).
- At a glance (AR p. 53): "EUV systems recognized (in units) 48, 2024: 44"; sales of lithography
  systems 327 units (2024: 418).
- Financial performance (AR p. 55): "We recognized four EXE and 44 NXE systems in sales in 2025
  compared to two EXE and 42 NXE systems in 2024." DUV system sales fell "from 374 units in 2024 to
  279 in 2025." Net system sales EUR 24.5 billion (2024: 21.8 billion).
- Bears on: O1, O3. This is the measured count of the one tool that leading-edge logic and DRAM
  depend on.

### shilov2026asml
*ASML projects $71 billion in revenue by 2030, as demand for EUV lithography machines intensifies due
to AI boom.* Anton Shilov, Tom's Hardware, 29 January 2026. URL below. Opened 2026-11-27.
- "the company shipped 48 EUV systems and 131 immersion DUV tools" in 2025, "up from 44 EUV
  scanners and 129 immersion DUV machines in 2024."
- EUV "accounted for 48% of ASML's system revenue in 2025," EUR 11.6 billion, up from 38%.
- "33% of ASML's tools (in terms of units) were sold to the PRC" in 2025 (41% in 2024).
- Eight High-NA EUV tools supplied to date (six EXE:5000, two EXE:5200B). 2030 revenue target
  "EUR 44 billion - EUR 60 billion."
- Bears on: O1, O3.

### asml2026q2call
*ASML Q2 2026 earnings call transcript.* ASML Holding (CFO Roger Dassen, CEO Christophe Fouquet),
15 July 2026, transcript hosted by The Motley Fool. URL below. Opened 2026-11-27.
- Dassen: "We now expect to ship around 65 Low-NA EUV systems this year"; "For immersion DUV, we
  expect about 130 shipments this year."
- Dassen on 2027: "we are planning to increase our Low-NA EUV capacity by around 30%." On 2028:
  "Strong demand forecasts from our customers have led us to investigate a further 30% capacity
  increase for that year."
- High-NA revenue recognition in 2026: "We've set four to five."
- China "around 20% of our total net sales for the full year" 2026.
- Bears on: O1 (growth rate of the tightest input), O3, D3 (an EUV-limited program cannot grow
  faster than roughly 30% a year in new tools).

### trendforce2026cowos
*TSMC CoWoS Supply-Demand Gap Reportedly Seen Narrowing from 20% to 10% by End-2026.* TrendForce
News, 15 June 2026. URL below. Opened 2026-11-27.
- TSMC CoWoS "could reach a record 120,000 to 140,000 wafers in 2026" (per month), relaying Economic
  Daily News; "an additional 50,000 to 60,000 wafers of new capacity from OSAT partners"; total
  could "approach 200,000 wafers per month."
- Supply-demand gap from "around 20% currently to about 10% by the end of 2026."
- CoWoS capacity "a CAGR of more than 80% from 2022 to 2027" (Reuters, on TSMC's May symposium).
- Bears on: O1, O3. Packaging is the stage that grew fastest, so it is the least durable chokepoint
  in volume terms, but it is still concentrated in TSMC and a few OSATs.

### counterpoint2026hbm
*Global DRAM and HBM Market Share: Quarterly.* Counterpoint Research, September 2026. URL below.
Opened 2026-11-27.
- HBM revenue share, Q2 2025 / Q3 2025 / Q4 2025 / Q1 2026 / Q2 2026: SK hynix 64 / 56 / 57 / 58 /
  50%; Samsung 15 / 23 / 22 / 21 / 33%; Micron 21 / 21 / 21 / 21 / 18%.
- DRAM revenue share Q2 2026: Samsung 38%, SK hynix 25%, Micron 24%, CXMT 10% ("demonstrating
  significant growth from 4% in the same period of the previous year").
- Bears on: O1, O3. HBM is a three-firm stage, but share is shifting and a Chinese DRAM maker is
  growing quickly in commodity DRAM.

### trendforce2026foundry
*Global Foundry Revenue Approaches US$53.49 Billion in 2Q26 as SMIC Narrows Market Share Gap with
Samsung.* TrendForce press release, 9 September 2026. URL below. Opened 2026-11-27.
- TSMC Q2 2026 revenue "nearing $40.2 billion... capturing a 72.5% market share"; "Strong demand
  for AI server GPUs and XPUs kept its 5/4nm and 3nm capacities fully booked."
- Samsung 5.9%; SMIC 5.4%, revenue up 20% QoQ to more than $3 billion.
- Bears on: O1, O3. Concentration at the foundry stage is rising, not falling.

### epoch2026chipsales
*Data on AI chip sales* (dataset, with methodology documentation). Epoch AI, updated 24 November
2026. URL below. Opened 2026-11-27 (page, methodology page, and the CSV
`ai_chip_sales_timelines_by_chip.csv`).
- Methodology: Huawei "180K H100-equivalents in 2024 (90% credence interval: 130K-240K)" and "530K
  H100-equivalents in 2025 (450K-620K)." Cambricon "has targeted 500,000 units in 2026." "We have
  the highest confidence in our Nvidia estimates"; "least confident in our Amazon Trainium
  estimates."
- My sums of the per-quarter median estimates in the CSV (not a figure Epoch states): total AI
  compute sold 5.10 million H100e in 2024 and 13.61 million in 2025 (ratio 2.67). Shares of 2025
  H100e: Nvidia 65.5%, Google TPU 20.2%, Amazon 5.2%, AMD 5.0%, Huawei 3.9%, Cambricon 0.2%. Summed
  chip TDP of chips sold in 2025: 7.5 GW (chips only, before cooling and servers). 2026 rows are
  incomplete. Sums of per-row percentiles are not a valid interval, so no interval is given.
- Bears on: O1, P1, P4. This is the flow the protocol would register.

### you2026chipowners
*Introducing the AI Chip Owners Explorer.* Josh You and Venkat Somala, Epoch AI, 6 April 2026. URL
below. Opened 2026-11-27.
- "over 70% of global AI compute (in terms of total computing power) is owned by the five US
  hyperscalers." Google about 5 million H100e, "roughly 25% of the world's total."
- Chinese companies "collectively own just over 5%" of cumulative compute of recent leading AI
  chips at end-2025 (excludes smuggled chips and offshore cloud).
- Bears on: O1, O3. Holdings are concentrated in five firms, which makes registration tractable.

### pilz2025supercomputers
*Trends in AI Supercomputers.* Konstantin F. Pilz, James Sanders, Robi Rahman, Lennart Heim, 2025.
arXiv 2504.16026. Opened 2026-11-27 (abstract).
- 500 systems, 2019 to 2025: "the computational performance of AI supercomputers has doubled every
  nine months"; "hardware acquisition cost and power needs both doubled every year."
- xAI Colossus (March 2025) "used 200,000 AI chips, had a hardware cost of $7B, and required 300
  MW of power."
- "the United States accounts for about 75% of total performance in our dataset," China 15%.
- If trends continue, the leading system in 2030: 2x10^22 16-bit FLOP/s, two million chips, $200
  billion, 9 GW.
- Bears on: O1, P1, P4.

### sevilla2024scaling2030
*Can AI scaling continue through 2030?* Jaime Sevilla, Tamay Besiroglu, Ben Cottier, Josh You, Edu
Roldan, Pablo Villalobos, Ege Erdil, Epoch AI, 20 August 2024. URL below. Opened 2026-11-27 (two
passes over the first 100,000 characters).
- Conclusion: "training runs of 2e29 FLOP will likely be feasible by the end of this decade." "The
  constraint likely to bind first is power, followed by the capacity to manufacture enough chips."
- Power: campuses "between 1 to 5 gigawatt (GW) are likely possible by 2030" (1e28 to 3e29 FLOP);
  distributed training "2 to 45 GW" (2e28 to 2e30 FLOP); a 2e29 FLOP run "for a power demand of 6
  GW." US data centres "over 20 GW today" average draw, capacity about 40 GW central.
- Chips: CoWoS "from 14,000-15,000 wafers per month in December 2023" to "33,000-35,000 wafers per
  month by the end of 2024"; GPU production "expected to expand between 30% to 100% per year";
  "HBM chips are nearly sold out until 2026"; one analyst firm expects "45% annual growth in
  production volume" of HBM 2023 to 2028; median 28 good dies per wafer; about 20% of leading-edge
  wafers to data-centre GPUs. Result: "20 million to 400 million H100 equivalents," median "about
  100M," enough for about 9e29 FLOP.
- Data: 400 trillion to 20 quadrillion tokens by 2030. Latency wall: 3e30 to 1e32 FLOP.
- Bears on: O1, P1, P4, A4.

### sevilla2024computegrowth
*Training compute of frontier AI models grows by 4-5x per year.* Jaime Sevilla and Edu Roldan, Epoch
AI, 28 May 2024. URL below. Opened 2026-11-27.
- Frontier models: "increasing at 5.3x/year (90% CI: 4.9x to 5.7x) between 2010 and May 2024."
  Frontier language models since mid-2020: 5.0x/year (90% CI 3.1x to 7.3x). OpenAI 5x, Google
  DeepMind 5x, Meta 7x per year.
- Bears on: P1, A1, O1.

### cottier2024rising
*The rising costs of training frontier AI models.* Ben Cottier, Robi Rahman, Loredana Fattorini,
Nestor Maslej, Tamay Besiroglu, David Owen, 2024 (v2 February 2025). arXiv 2405.21015. Opened
2026-11-27 (abstract).
- Amortized cost of the most compute-intensive runs has grown "at a rate of 2.4x per year since
  2016" (90% CI 2.0x to 2.9x). "the largest training runs will cost more than a billion dollars by
  2027."
- Shares: accelerator chips and staff largest; server components 15-22%, cluster interconnect
  9-13%, energy 2-6%.
- Bears on: O1 (capital as a barrier), D3. Energy is a small share of cost but a large share of
  footprint, which is why power is a better detection channel than a cost lever.

### day2026capex
*Big Tech to Spend $650B This Year as AI Race Intensifies.* Matt Day (Bloomberg), republished by Data
Center Knowledge, 6 February 2026. URL below. Opened 2026-11-27.
- The four largest companies' capex "will reach about $650 billion in 2026," "an estimated 60%
  increase from a year ago." Alphabet "as much as $185 billion"; Amazon "a planned $200 billion";
  Meta "as much as $135 billion," "a potential jump of about 87%."
- Bears on: O1.

### ehsan2026capex
*Hyperscalers Hit $700 Billion in 2026 AI Spending Plans.* Omor Ibne Ehsan, Yahoo Finance, 1 May
2026. URL below. Opened 2026-11-27.
- "the total spend now for 2026 from these big hyperscalers has now topped $700 billion." Meta
  "raised full-year 2026 capex to $125 to $145 billion from a prior $115 to $135 billion."
  Alphabet Q1 capex $35.67 billion; Microsoft fiscal Q3 $30.88 billion, "up 84% year over year."
- Bears on: O1. Capital is concentrated in four or five firms whose spending is public each
  quarter: a visible input.

### iea2025energyai
*Energy and AI: Executive Summary.* International Energy Agency, 2025. URL below. Opened 2026-11-27.
- "Data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415
  terawatt-hours (TWh)"; "set to more than double to around 945 TWh by 2030." US 45%, China 25% of
  data-centre electricity in 2024. Growth about 12% a year since 2017.
- "A typical AI-focused data centre consumes as much electricity as 100 000 households," and "the
  largest ones under construction today will consume 20 times as much."
- "Turbine deliveries for new gas-fired power plants now face lead times of several years";
  transformer and cable wait times doubled in three years; China about 99% of refined gallium.
- Bears on: O1, P4.

### shehabi2024datacenter
*2024 United States Data Center Energy Usage Report.* Arman Shehabi, Sarah Smith, Alex Hubbard, Alex
Newkirk, Nuoa Lei, A.B. Saddik, Billie Holecek, Jonathan Koomey, Eric Masanet, Dale Sartor, LBNL,
December 2024 (LBNL-2001637). DOI 10.71468/P1WC7Q. Opened 2026-11-27 (PDF).
- Executive summary (PDF p. 8): US data-centre use reached "176 TWh by 2023, representing 4.4% of
  total U.S. electricity consumption"; scenarios give "roughly 325 and 580 TWh in 2028," 6.7% to
  12.0% of US consumption. The range is driven by assumed GPU shipments, utilisation and cooling.
- Bears on: O1, P4.

### rand2026queued
*Queued Up: 2026 Edition. Characteristics of Power Plants Seeking Transmission Interconnection As of
the End of 2025.* Joseph Rand, Anna Cheyette, Chris Talley, Steven Zhang, Will Gorman, Ryan Wiser,
Joachim Seel, Seongeun Jeong, Fritz Kahrl, LBNL and Interconnection.fyi, June 2026. URL below. Opened
2026-11-27 (PDF slide deck).
- High-level findings (slide 4): "Roughly 2,061 gigawatts (GW) of capacity was actively seeking
  interconnection (1,312 GW of generation; 749 GW of storage)"; over 750 GW withdrew in 2025 while
  about 600 GW submitted; natural gas in queues +86%.
- "About 19% of projects (13% of capacity) requesting interconnection from 2000-2020 reached
  commercial operations by the end of 2025."
- "The median project built in 2025 took 61 months from the interconnection request to commercial
  operations, compared to 36 months in 2015 and 22 months in 2008."
- Caveat stated in the deck: generator queues only; "separate queues for large loads" are excluded.
- Bears on: O1 (growth limit for new power in the US), P4, D3.

### woodmac2025transformers
*Power transformers and distribution transformers will face supply deficits of 30% and 10% in 2025,
according to Wood Mackenzie.* Wood Mackenzie press release, 14 August 2025. URL below. Opened
2026-11-27.
- Since 2019 "power and distribution transformers have seen demand surge by 116% and 41%"; "a supply
  shortage for power and distribution transformers to hit 30% and 10%, respectively, in 2025";
  "imports will account for an estimated 80% of US power transformer supply"; constraints "will
  persist well into the 2030s."
- Bears on: O1, P4.

### woodmac2025connection
*Making the connection: meeting the electric T&D supply chain challenge, Executive Summary.* Wood
Mackenzie with American Clean Power, September 2025. URL below. Opened 2026-11-27 (PDF).
- PDF p. 5: "Power transformer lead times eased in Q2 falling by 10 weeks to an average of 128
  weeks"; generator step-up transformers "easing to 143 weeks on average"; switchgear "an average of
  44 weeks." GSU and power transformer lead times "remain between 2 - 3 years."
- Bears on: O1, P4, D3.

### bailey2026steam
*Is Steam the Answer to the Gas Turbine Bottleneck?* Richard Bailey, Anthony Brough, Alicia Bigica,
Turbomachinery Magazine, 11 September 2026. URL below. Opened 2026-11-27.
- "Large-frame gas turbine lead times extending into 2029-2030." Backlogs: "GE Vernova's backlog
  stood at 116 gigawatts," "Siemens Energy's own gas turbine backlog is at 69 GW," "Mitsubishi
  Heavy Industries is at 35 GW."
- Bears on: O1, P4. Large gas turbines are a three-firm stage, a possible secondary chokepoint for
  on-site power that the memo does not list; I found no share data, so this is a lead, not a finding.

### shaw2026chinasolar
*China adds 315 GW of solar in 2025.* Vincent Shaw, pv magazine, 28 January 2026. URL below. Opened
2026-11-27.
- NEA 2025 statistics: "315.07 GW (AC) of new solar capacity last year" "alongside 119.33 GW of
  wind"; cumulative installed power capacity "had reached 3.89 TW" at end-2025.
- Bears on: O1, P4. Evidence against power as a global chokepoint.

### cottier2026horinger
*What Huawei's Horinger data center reveals about China's compute gap.* Ben Cottier, Epoch AI, 6
November 2026. URL below. Opened 2026-11-27.
- "81,000 H100-equivalents (90% CI: 36,000 to 141,000)"; "a total of 286 megawatts (MW) of IT power
  capacity across these four buildings"; "Colossus 2 has about 14 times as much computing capacity
  as Huawei Horinger."
- "China appears to have no shortage of energy for data centers"; "a given amount of power
  capacity can only support 40% of the compute of leading US facilities"; "China's compute
  constraints are unlikely to ease in the next two years."
- Bears on: O1, O3, P4. Supports finding 3: denial raises the footprint per unit of compute.

### epoch2025datacentershub
*Introducing the Frontier Data Centers Hub.* Epoch AI, 4 November 2025. URL below. Opened 2026-11-27.
- Method: satellite and aerial imagery to "identify and measure cooling infrastructure such as
  chillers and cooling towers," corroborated with "permits and public disclosures."
- "It's hard to hide the massive chillers required to prevent billions of dollars in equipment from
  overheating." 13 large US sites hold about 2.5 million H100e, about 15% of about 15 million H100e
  delivered. Five sites projected to reach 1 GW in 2026.
- Bears on: P4, O3 (visibility). Prior art for satellite verification of compute.

### somala2025buildtimes
*Build times for gigawatt-scale data centers can be 2 years or less.* Venkat Somala and Ben Cottier,
Epoch AI, 10 November 2025. URL below. Opened 2026-11-27.
- Months from construction start to 1 GW: xAI Colossus 2 about 11.6, Anthropic-Amazon New Carlisle
  about 23, OpenAI Stargate Abilene about 25, Microsoft Fairwater about 43. For recent sites "the time
  from starting construction to achieving 1 GW of total facility power ranges from 1 to 3.6 years."
- Bears on: D3 (how fast compute can be housed), P4.

### sevilla2025decentralized
*How far can decentralized training over the internet scale?* Jaime Sevilla, Epoch AI Gradient
Updates, 29 December 2025. URL below. Opened 2026-11-27.
- Decentralized training compute grows about "20x/year"; largest runs in "the 6e22-6e23 FLOP
  range," about 1000 times below the largest models. "we won't see decentralized training runs catch
  up to the frontier of training in scale this decade." Many monitoring proposals "depend on internet
  decentralized training continuing to lag far behind the frontier."
- Bears on: O3 (visibility), P3, P4. A 20x/year growth rate is the number to watch; the essay is
  the author's view, not Epoch's official position.

### verwey2021permits
*No Permits, No Fabs: The Importance of Regulatory Reform for Semiconductor Manufacturing.* John
VerWey, CSET, October 2021. DOI 10.51593/20210053. Opened 2026-11-27 (PDF).
- PDF p. 6: about 635 greenfield fabs built worldwide 1990 to 2020; "The average time between the
  construction start date and the beginning date of production was 682 days or roughly 1.86 years,"
  excluding permitting. Japan 584 days, South Korea 620, the Americas 736.
- PDF p. 7: US build time rose "from an average of 665 days (1.8 years) during the 1990 to 2000 time
  period to 918 days (2.5 years) during the 2010-2020 time period."
- Bears on: O1, O3, D3. A new fab is a two-year, highly visible construction project.

### techinsights2025kirin
*SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm.* TechInsights, 11
December 2025. URL below. Opened 2026-11-27 (public summary; details paywalled).
- N+3 is "a scaled evolution of its 7nm-class technology"; "it remains significantly less scaled
  than leading commercial 5nm nodes offered by TSMC and Samsung"; framed as how close SMIC is to "a
  true 5nm-equivalent node without EUV lithography."
- Bears on: O3 (erosion of the lithography chokepoint).

### techinsights2026datacenter
*Analysis: Can China even build data center AI chips?* TechInsights, 17 March 2026. URL below. Opened
2026-11-27 (public summary).
- "This demonstrates that China can produce scaled logic silicon using DUV lithography"; but "we
  believe that it will not be a viable solution for data center AI chips"; "Limitations of the DUV,
  combined with newness of the process will lead to low yields."
- Bears on: O3.

### washenko2025euv
*China reportedly has a prototype EUV machine built by ex-ASML employees.* Anna Washenko, Engadget, 17
December 2025, relaying Reuters. URL below. Opened 2026-11-27. (The Reuters original was not opened.)
- "the Chinese prototype is not yet making chips" but is "reportedly able to generate the extreme
  ultraviolet light"; "allegedly now undergoing testing"; target chips "beginning in 2028"; "other
  experts have projected 2030 as a more likely date"; "made by former engineers from Dutch
  semiconductor supplier ASML." Based on unnamed sources.
- Bears on: O3. The strongest evidence found that the EUV chokepoint has a horizon (a few years to
  first chips, longer to volume), and that talent leakage is how it erodes.

### xu2025huaweiconnect
*Groundbreaking SuperPoD Interconnect: Leading a New Paradigm for AI Infrastructure* (keynote). Eric
Xu, Huawei, Huawei Connect 2025, 18 September 2025. URL below. Opened 2026-11-27.
- Roadmap: Ascend 950PR Q1 2026, 950DT Q4 2026, 960 Q4 2027, 970 Q4 2028. Own HBM: HiBL 1.0
  "proprietary, low-cost HBM," HiZQ 2.0 "144 GB of memory and 4 TB/s memory access bandwidth."
- Atlas 950 SuperPoD "up to 8,192 Ascend 950DT chips" (Q4 2026); Atlas 950 SuperCluster "over
  500,000 NPUs"; Atlas 960 SuperCluster "more than 1 million NPUs."
- "we don't have access to advanced process nodes, so we've decided to focus our efforts on making
  breakthroughs by combining" chips; "Sustainable computing power can only be achieved with process
  nodes that are practically available."
- Bears on: O3, P4. A vendor's own admission that the node chokepoint binds, and its stated answer
  (scale out). Vendor claims; not verified.

### patel2025ascend
*Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck.* Dylan
Patel, AJ, Myron Xie, SemiAnalysis, 8 September 2025. URL below. Opened 2026-11-27 (public portion).
- "507k Ascend units shipped in 2024"; "805k this year, 653k of those being 910C."
- "more than 2.9M Ascend die" made at TSMC; "We expect that the TSMC die bank to run out within the
  next 9 months."
- "China has procured 13M HBM stacks which is sufficient for 1.6M Ascend 910C packages"; Samsung
  supplied "11.4 million stacks."
- SMIC advanced-node capacity, conservative: "45k wspm by end of 2025, increasing to 60k wspm in
  2026 and 80k wspm in 2027"; Ascend needs "at most 20k wafers per month."
- "We believe HBM production is the bottleneck"; CXMT "~2 million stacks of HBM next year."
- Bears on: O1, O3. Identifies HBM as the binding stage for China, and shows how a stockpile bought
  before a control delays its effect by about a year.

### pan2026idc
*Chinese chipmakers claim nearly half of local market as Nvidia's lead shrinks.* Che Pan and Laurie
Chen, Reuters (via Yahoo Finance), 1 April 2026. URL below. Opened 2026-11-27.
- IDC: "approximately 4 million units in China in 2025"; Nvidia "around 2.2 million cards and
  holding a 55% share"; Chinese vendors "1.65 million cards, accounting for 41%"; Huawei "around
  812,000 AI chips"; AMD "roughly 160,000 cards for a 4% share."
- Bears on: O1, O3.

### blablova2025china
*Why China isn't about to leap ahead of the West on compute.* Veronika Blablova and Robi Rahman, Epoch
AI Gradient Updates, 26 July 2025. URL below. Opened 2026-11-27.
- Huawei "manufactured 200,000 Ascend 910B chips in 2024" (per the FT); "roughly one million NVIDIA
  GPUs were legally delivered to China in the same year." SMIC yields "below 50%" versus TSMC "90%."
- "we think that China will remain at least one generation behind in hardware"; costs "put China at
  a substantial disadvantage in AI scaling for at least the rest of the decade."
- Bears on: O3.

### zafar2025kessler
*China's Huawei Can Make 200,000 Advanced AI Chips In 2025 At Most, Says US Official.* Ramish Zafar,
Wccftech, 13 June 2025. URL below. Opened 2026-11-27.
- Under Secretary Jeffrey Kessler (BIS), at a House Foreign Affairs subcommittee hearing: "Huawei's
  Ascend chip production capacity for 2025 will be at or below 200,000"; "most or all" go to Chinese
  companies.
- Bears on: O3, and on the verification miss rate: compare 805,000 (SemiAnalysis) and 812,000 (IDC)
  for the same year. Units differ (capacity versus shipments, possibly including die-bank chips), but
  the spread is about fourfold.

### allen2025senate
*China's Challenge to American AI Leadership* (written testimony). Gregory C. Allen, CSIS, before the
Senate Foreign Relations Committee, East Asia subcommittee, 2 December 2025. URL below. Opened
2026-11-27 (PDF; page numbers are the printed ones).
- p. 2: the largest AI cluster as of March 2025 "included more than 200,000 AI chips" and is
  planned to grow past one million; leading chips cost "$25,000-$60,000."
- p. 3: without the controls "it is possible, perhaps even likely, that the first million chip AI
  cluster would be built in China"; SMIC "has been stuck at the 7 nanometer (nm) technology node for
  years"; DeepSeek's CEO said restrictions force "two to four times the computing power."
- p. 4: citing Bernstein, "the rate of China's progress toward self-sufficiency is best predicted by
  the market and technological complexities of each semiconductor market segment, not by the extent
  to which export controls were applied."
- p. 7: "the most important export controls... are those related to advanced semiconductor
  manufacturing equipment"; controls "did not so much destroy demand as change its composition."
- Bears on: O3, O2. (The March 2025 CSIS report by the same author returned HTTP 403 and an access
  block and was not read; I do not summarise it.)

### grunewald2025smuggling
*Countering AI Chip Smuggling Has Become a National Security Priority.* Erich Grunewald and Tim Fist,
CNAS (with IAPS), 11 June 2025. URL below. Opened 2026-11-27.
- 2024 smuggling into the PRC "anywhere from 10,000 to several hundred thousand chips, with a median
  estimate of around 140,000" (my wording of the range; their judgement is a distribution, not a
  count). At the median, about 6% of PRC inference compute (1-30%) and 10% of training compute
  (1-40%).
- Methods: overseas shell companies, multiple distributors, relabelled shipments, front cloud firms.
  "the profits from three reported smuggling cases exceed its annual export enforcement budget."
- Recommends chip location verification as a licence condition, export and transfer notification,
  whistleblower and qui tam incentives, and BIS funding of $313 million for FY2026 (64% above $191
  million).
- Bears on: O3, protocol verification channels (whistleblowing, location attestation).

### juniewicz2026smuggling
*Diversion and resale: estimating compute smuggling to China.* Isabel Juniewicz, Epoch AI, 29 April
2026. URL below. Opened 2026-11-27.
- "Our model estimates 660,000 (90% CI: 290,000-1.6 million) H100e of cumulative compute smuggled
  through the end of 2025," "roughly a third of China's total compute," about 3% of the global
  stockpile.
- Two Monte Carlo estimates (diversion from 2024-2025 allegations with an estimated detection rate,
  median about 25%; resale from modelled gray-market vendors), blended.
- Bears on: O3, and on the protocol's detection guarantee: an existing enforcement system is
  estimated to catch about a quarter of diversion cases.

### bis2022advancedcomputing
*Implementation of Additional Export Controls: Certain Advanced Computing and Semiconductor
Manufacturing Items; Supercomputer and Semiconductor End Use; Entity List Modification.* BIS, 87 FR
62186, published 13 October 2022, effective 7 October 2022 (doc. 2022-21658). Opened 2026-11-27
(full text via the Federal Register API).
- ECCN 3A090.a: ICs with "an aggregate bidirectional transfer rate over all inputs and outputs of 600
  Gbyte/s or more" and processing performance (bit length times TOPS) "of 4800 or more."
- Fab end-use controls: logic "of 16/14 nanometers or less," NAND "with 128 layers or more," DRAM "18
  nanometer half-pitch or less."
- Bears on: O3. The first rule that stands on the chokepoints.

### bis2023advancedcomputing
*Implementation of Additional Export Controls: Certain Advanced Computing Items; Supercomputer and
Semiconductor End Use; Updates and Corrections.* BIS, 88 FR 73458, published 25 October 2023,
effective 17 November 2023 (doc. 2023-23055). Opened 2026-11-27 (full text).
- New 3A090.a: "a 'total processing performance' of 4800 or more, or... 1600 or more and a
  'performance density' of 5.92 or more"; 3A090.b covers a lower band.
- Rationale: "A performance density parameter prevents the workaround of simply purchasing a larger
  number of smaller datacenter AI chips which, if combined, would be equally powerful."
- Bears on: O3. A documented case of a chip threshold being gamed and patched within a year.

### bis2024hbm
*Foreign-Produced Direct Product Rule Additions, and Refinements to Controls for Advanced Computing
and Semiconductor Manufacturing Items.* BIS, 89 FR 96790, published 5 December 2024, effective 2
December 2024 (doc. 2024-28270). Opened 2026-11-27 (full text).
- New 3A090.c: "HBM having a 'memory bandwidth density' greater than 2 GB per second per square
  millimeter"; "All HBM stacks currently in production exceed this threshold." Adds SME controls and
  new foreign direct product rules for advanced-node ICs.
- Bears on: O3. HBM became a controlled chokepoint only in December 2024, after the stockpiling
  reported by SemiAnalysis.

### bis2025diffusion
*Framework for Artificial Intelligence Diffusion.* BIS, 90 FR 4544, published 15 January 2025,
effective 13 January 2025 (doc. 2025-00636). Opened 2026-11-27 (full text).
- Licence required for the weights of any closed-weight model "trained on more than 10^26
  computational operations" (rendered as 10\26\ in the text).
- Country allocation: "a cumulative maximum installed base allocation of 790,000,000 TPP" for 2025 to
  2027. Universal validated end users "cannot transfer or install more than 25% of its total AI
  computing power" outside listed countries, "more than 7%" in any single one.
- Bears on: O3, D4. The closest existing legal instrument to compute registration with per-country
  caps.

### bis2025rescission
*Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule,
Strengthens Chip-Related Export Controls.* BIS press release, 13 May 2025. URL below. Opened
2026-11-27.
- The rule "would have stifled American innovation and saddled companies with burdensome new
  regulatory requirements" and "would have undermined U.S. diplomatic relations"; BIS "will issue a
  replacement rule in the future." Issues guidance on Huawei Ascend chips, on US chips training
  Chinese models, and on diversion.
- Bears on: O3, O2. Chokepoint governance by one state is reversible within months.

### james2025h200
*The Nvidia H200 export saga, as it happened.* Luke James, Tom's Hardware, 10 December 2025. URL below.
Opened 2026-11-27.
- "The U.S. government has formally approved the export of Nvidia's high-performance H200 AI chips to
  China"; each chip "accompanied by a 25% import duty"; "each chip must be routed through U.S.
  territory for inspection"; the US keeps "newer architectures like Blackwell and the upcoming Rubin
  out of reach."
- Bears on: O3, O2.

### ma2026talent
*Who's Ahead in the Global AI Talent Race?* Damien Ma and Binyi Yang, Carnegie China, Carnegie
Endowment for International Peace, 23 September 2026. URL below. Opened 2026-11-27.
- Work location of top AI talent (NeurIPS authors): 2025 China 41%, US 34%; 2022 US 46%, China 27%;
  "China overtook the United States as the leading work location."
- Chinese-origin (undergraduate) talent 57% in 2025; US-origin 13%. US net gain of 2,145
  researchers in 2025, China net loss of 1,729; ratio of Chinese-origin researchers in the US to
  US-origin in China 30:1 (46:1 in 2022). Retention: China 57% to 69%, US 89%.
- Sample: 5,823 accepted NeurIPS 2025 papers, 25,677 unique authors, 40% with complete career
  histories (not a random subset).
- Bears on: O1. Talent is large, mobile and spread across rival blocs: not a chokepoint. (An undated
  page on an archive domain for MacroPolo's tracker gave figures inconsistent with this study by
  MacroPolo's founder; I did not use it.)

### sastry2024compute
*Computing Power and the Governance of Artificial Intelligence.* Girish Sastry, Lennart Heim, Haydn
Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield,
Richard Ngo, Konstantin Pilz, George Gor, Emma Bluemke, Sarah Shoker, Janet Egan, Robert F. Trager,
Shahar Avin, Adrian Weller, Yoshua Bengio, Diane Coyle, 2024. arXiv 2402.08797. Opened 2026-11-27
(abstract and first 100,000 characters of the HTML).
- Abstract: compute "is detectable, excludable, and quantifiable, and is produced via an extremely
  concentrated supply chain."
- Section 3.B.4: "several key steps of which (e.g., design, EUV lithography, and fabrication) are
  dominated by a small number of actors." Section 3.B.1: large-scale compute is detectable because it
  needs "thousands of specialized chips in a high-performance cluster hosted in a large data center
  consuming large amounts of power."
- Section 2.C: "the necessity of changing the compute thresholds over time as algorithmic and
  hardware progress occur," and "unforeseen low-compute enhancements."
- Bears on: O3 (closest prior art for the framing), P4.

### shavit2023chinchilla
*What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via
Compute Monitoring.* Yonadav Shavit, 2023. arXiv 2303.11341. Opened 2026-11-27 (abstract).
- Proposes "using on-chip firmware to occasionally save snapshots of the the neural network weights"
  and "monitoring the chip supply chain to ensure that no actor can avoid discovery," to give
  governments "high confidence that no actor uses large quantities of specialized ML chips" in
  violation of rules.
- Bears on: O3 and the protocol's chip accounting and attestation channels (prior art).

### scher2025agreement
*An International Agreement to Prevent the Premature Creation of Artificial Superintelligence.* Aaron
Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance Team), 2025 (v3 May
2026). arXiv 2511.10783. Opened 2026-11-27 (abstract, HTML of v2 and v3).
- Abstract: "a coalition led by the United States and China that would restrict the scale of AI
  training"; "Limits on the scale of AI training are operationalized by FLOP thresholds and verified
  through the tracking of AI chips"; "We believe the proposal would be technically sufficient to
  forestall the development of ASI if implemented today."
- Section 4: "AI training runs above the Strict Threshold (i.e., 10^24 FLOP) are prohibited";
  Monitored Threshold 10^22 FLOP; "the coalition prohibits large concentrations of chips (i.e.,
  greater than 16 H100-equivalents; 16 H100s cost approximately $500,000 USD in 2025) outside of
  monitored facilities"; "Tracking new AI chips relies on the concentrated chip supply chain."
- Article VI: monitoring "will start with fabrication. The full set of activities includes
  fabrication of high-bandwidth memory (HBM), fabrication of logic chips, testing, packaging, and
  assembly"; "For facilities where tracking and monitoring is not feasible or implemented,
  production of AI chips will be halted."
- Notes on Article VI: TSMC "around 90 percent of market share" of advanced AI logic; EUV machines
  "made exclusively by ASML"; HBM "dominated by two or three companies."
- Bears on: O3 and the protocol's compute half (closest prior art found), D4. Differences visible
  from what I read: MIRI sets fixed FLOP thresholds; the memo's line is a time-based breakout test
  (D3, D4) and leaves useful AI to keep improving above fixed thresholds.

### hendrycks2025superintelligence
*Superintelligence Strategy: Expert Version.* Dan Hendrycks, Eric Schmidt, Alexandr Wang, 2025.
arXiv 2503.05628. Opened 2026-11-27 (abstract).
- Introduces Mutual Assured AI Malfunction, a deterrence regime "resembl[ing] nuclear mutual assured
  destruction (MAD)," where a bid for unilateral AI dominance meets "preventive sabotage by rivals,"
  plus nonproliferation to "keep weaponizable AI capabilities out of their hands."
- Bears on: O2, protocol defection section (prior art on deterrence among states).

### pilz2023efficiency
*Increased Compute Efficiency and the Diffusion of AI Capabilities.* Konstantin Pilz, Lennart Heim,
Nicholas Brown, 2023 (v2 2024). arXiv 2311.15377. Opened 2026-11-27 (abstract).
- "an access effect increases the number of actors who can train models to a given performance over
  time," while "a performance effect simultaneously increases the performance available to each
  actor"; governments must "prepare for a world where dangerous AI capabilities are widely
  available."
- Bears on: O3, A3, D3 (the memo's stated weakness, algorithmic progress at fixed compute, is prior
  work).

### armstrong2016racing
*Racing to the precipice: a model of artificial intelligence development.* Stuart Armstrong, Nick
Bostrom, Carl Shulman. AI and Society 31(2):201-206, 2016. DOI 10.1007/s00146-015-0590-y. Opened
2026-11-27: the publisher page redirected to a login, so I read the FHI Technical Report 2013-1
version (October 2013) of the same paper.
- Abstract: each team "is incentivised to finish first - by skimping on safety precautions if need
  be"; "Having extra development teams and extra enmity between teams can increase the danger of an
  AI-disaster, especially if risk taking is more important than skill"; "Surprisingly, information
  also increases the risks: the more teams know about each others' capabilities (and about their
  own), the more the danger increases."
- Bears on: O2. Directly relevant to the protocol's declarations, which raise mutual information.

### askell2019cooperation
*The Role of Cooperation in Responsible AI Development.* Amanda Askell, Miles Brundage, Gillian
Hadfield, 2019. arXiv 1907.04534. Opened 2026-11-27 (abstract and PDF).
- Competitive pressure "could incentivize AI companies to underinvest in ensuring their systems are
  safe." Five factors that favour cooperation (PDF p. 1 and section 3): "high trust between
  developers (High Trust), high shared gains from mutual cooperation (Shared Upside), limited
  exposure to potential losses in the event of unreciprocated cooperation (Low Exposure), limited
  gains from not reciprocating the cooperation of others (Low Advantage), and high shared losses from
  mutual defection (Shared Downside)."
- Bears on: O2. The protocol's verification lowers exposure; detection timeliness lowers advantage.

### stafford2022safety
*Safety Not Guaranteed: International Races for Risky Technologies.* Eoghan Stafford, Robert F.
Trager, Allan Dafoe, GovAI working paper draft, November 2022. URL below. Opened 2026-11-27 (PDF).
- Abstract: "When competitors are moderately adversarial or the technology laggard is not very
  capable, the laggard does not use a risky technology unless it catches up"; "if competitors are
  highly adversarial and the laggard is closer to the leader's capability level, the laggard is
  willing to cut corners to gamble for advantage"; safety improvements "will be attenuated or
  reversed by risk compensation."
- Marked "Preliminary. Please do not cite or distribute without permission" on the draft; the
  project should cite it only as a working paper, or find the published version.
- Bears on: O2.

### han2020regulate
*To Regulate or Not: A Social Dynamics Analysis of an Idealised AI Race.* The Anh Han, Luis Moniz
Pereira, Francisco C. Santos, Tom Lenaerts. Journal of Artificial Intelligence Research 69:881-921,
2020. DOI 10.1613/jair.1.12225. Opened 2026-11-27 (abstract from the publisher's Crossref record;
jair.org did not resolve).
- "the time-scale in which domain supremacy can be achieved plays a crucial role. When this can be
  achieved in a short term, those who completely ignore the safety precautions are bound to win the
  race"; "imposing regulations for all risk and timing conditions may not have the anticipated
  effect."
- Bears on: O2, D3 (the race's timescale is the variable that matters, as in the memo's breakout
  time).

### emeryxu2024uncertainty
*Uncertainty, Information, and Risk in International Technology Races.* Nicholas Emery-Xu, Andrew
Park, Robert Trager. Journal of Conflict Resolution 68(10):2019-2047 (online November 2023). DOI
10.1177/00220027231214996. Opened 2026-11-27 (abstract on the Oxford AIGI page; volume data from
Crossref).
- "More decisive races, in which small performance leads produce larger probabilities of victory, are
  usually more dangerous"; "the public information scenario is less risky than the private
  information scenario except under high decisiveness"; states "discover either that they are far
  apart in capability and compete less or that they are close in capability and drastically reduce
  safety to win."
- Bears on: O2.

### fudenberg2026cooperating
*Cooperating Against Catastrophe.* Drew Fudenberg and Andrew Koh, working paper, 1 October 2026. URL
below. Opened 2026-11-27 (PDF).
- Abstract: two firms choose speed while a safety threshold advances; "when they are low, only
  racing is an equilibrium; when they are intermediate, racing and pacing coexist; when they are
  high, only pacing survives"; "If internal capabilities are hidden with a fixed lag until
  deployment, it is harder to sustain pacing which highlights the importance of transparency about
  internal capabilities."
- Introduction reports that in September 2026 frontier-lab leaders publicly supported "pacing the
  frontier" and more than 1,300 computer scientists signed a letter for an international effort (I
  did not open those primary sources).
- Bears on: O2, protocol declarations (supports transparency, against Armstrong et al.).

### buenodemesquita2026agirace
*The AGI Race and Existential Risk* (research brief of BFI Working Paper 2026-71). Ethan Bueno de
Mesquita, Wioletta Dziuda, Mattias Polborn, Becker Friedman Institute, September 2026. URL below.
Opened 2026-11-27 (brief only; the working paper was not opened).
- "Industry consolidation, regulation facilitating commitment to slow down, and governments entering
  the race in a safe way improves welfare, while restricting resources may backfire."
- "More resources always accelerate AGI development; however, they can make it either safer or
  riskier": with few firms and positive expected value, extra resources go to safety; with many
  firms, to speed. Firms "may continue racing even when achieving AGI has negative expected value."
  "A small commitment to reduced speed can leave all firms better off."
- Bears on: O2. A recent result against naive resource limits; it models a race that continues, not
  a regime that halts training above a line, so its reach to the protocol needs checking.

---

## Numbers for the ledger

Kinds: measured (counted or estimated from observations, including third-party estimates of past
quantities), vendor (a company's own claim or guidance), spec (a legal or technical specification),
design, assumption (a projection someone else made, which we would be assuming holds).

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| euv-systems-2025 | 48 | EUV systems recognised in sales | measured | asml2026annualreport | AR p. 53, at a glance |
| euv-systems-2024 | 44 | EUV systems recognised in sales | measured | asml2026annualreport | AR p. 53 |
| euv-highna-systems-2025 | 4 | EXE (High-NA) systems recognised | measured | asml2026annualreport | AR p. 55 |
| euv-lowna-shipments-2026 | 65 | low-NA EUV systems (guidance) | vendor | asml2026q2call | CFO, prepared remarks |
| euv-capacity-growth-2027 | 0.30 | fractional increase in low-NA EUV capacity | vendor | asml2026q2call | CFO, "planning" |
| euv-capacity-growth-2028 | 0.30 | further fractional increase under study | vendor | asml2026q2call | CFO, "investigate" |
| duv-immersion-shipments-2025 | 131 | ArF immersion systems | measured | shilov2026asml | body |
| asml-china-unit-share-2025 | 0.33 | share of ASML litho units sold to PRC | measured | shilov2026asml | body |
| asml-china-sales-share-2026 | 0.20 | share of ASML net sales (guidance) | vendor | asml2026q2call | CFO |
| litho-eu-revenue-share | 0.89 | share of lithography equipment revenue, EU-HQ vendors | measured | varadarajan2024resilience | Exhibit 10 |
| tsmc-foundry-share-2q26 | 0.725 | share of top-10 foundry revenue | measured | trendforce2026foundry | press release |
| sub10nm-taiwan-share-2022 | 0.69 | share of sub-10 nm logic capacity | measured | varadarajan2024resilience | Exhibit 6 |
| sub10nm-korea-share-2022 | 0.31 | share of sub-10 nm logic capacity | measured | varadarajan2024resilience | Exhibit 6 |
| sub10nm-us-share-2032 | 0.28 | projected US share of sub-10 nm capacity | assumption | varadarajan2024resilience | Exhibit 6 (BCG projection) |
| supply-chain-points-over-65pct | 50 | points where one region holds over 65% share | measured | varadarajan2024resilience | exec. summary p. 4 |
| cowos-tsmc-2026-low | 120000 | wafers per month | assumption | trendforce2026cowos | analyst estimate via EDN |
| cowos-tsmc-2026-high | 140000 | wafers per month | assumption | trendforce2026cowos | analyst estimate via EDN |
| cowos-osat-2026 | 50000-60000 | wafers per month, OSAT additions | assumption | trendforce2026cowos | analyst estimate |
| cowos-tsmc-dec-2023 | 14000-15000 | wafers per month | measured | sevilla2024scaling2030 | chip manufacturing section |
| cowos-cagr-2022-2027 | 0.80 | annual growth, lower bound | vendor | trendforce2026cowos | TSMC symposium via Reuters |
| hbm-share-skhynix-2q26 | 0.50 | HBM revenue share | measured | counterpoint2026hbm | table, Q2 2026 |
| hbm-share-samsung-2q26 | 0.33 | HBM revenue share | measured | counterpoint2026hbm | table, Q2 2026 |
| hbm-share-micron-2q26 | 0.18 | HBM revenue share | measured | counterpoint2026hbm | table, Q2 2026 |
| dram-share-cxmt-2q26 | 0.10 | DRAM revenue share | measured | counterpoint2026hbm | table, Q2 2026 |
| ai-compute-sold-2024 | 5.10e6 | H100e sold (sum of medians) | measured | epoch2026chipsales | CSV, my sum |
| ai-compute-sold-2025 | 13.61e6 | H100e sold (sum of medians) | measured | epoch2026chipsales | CSV, my sum |
| nvidia-share-h100e-2025 | 0.655 | share of H100e sold | measured | epoch2026chipsales | CSV, my sum |
| google-tpu-share-h100e-2025 | 0.202 | share of H100e sold | measured | epoch2026chipsales | CSV, my sum |
| huawei-share-h100e-2025 | 0.039 | share of H100e sold | measured | epoch2026chipsales | CSV, my sum |
| ai-chip-tdp-sold-2025 | 7.5 | GW of chip TDP sold | measured | epoch2026chipsales | CSV, my sum |
| huawei-h100e-2025 | 530000 | H100e (90% CI 450,000-620,000) | measured | epoch2026chipsales | methodology, Huawei |
| hyperscaler-compute-share | 0.70 | lower bound, share of global AI compute owned by five US hyperscalers | measured | you2026chipowners | body |
| china-owned-compute-share-2025 | 0.05 | share of cumulative recent AI chip compute (excl. smuggled) | measured | you2026chipowners | body |
| us-supercomputer-share | 0.75 | share of AI supercomputer performance | measured | pilz2025supercomputers | abstract |
| china-supercomputer-share | 0.15 | share of AI supercomputer performance | measured | pilz2025supercomputers | abstract |
| supercomputer-perf-doubling | 9 | months | measured | pilz2025supercomputers | abstract |
| supercomputer-power-doubling | 12 | months | measured | pilz2025supercomputers | abstract |
| colossus-power-2025 | 300 | MW | measured | pilz2025supercomputers | abstract |
| colossus-chips-2025 | 200000 | AI chips | measured | pilz2025supercomputers | abstract |
| frontier-compute-growth | 5.3 | x per year (90% CI 4.9-5.7) | measured | sevilla2024computegrowth | body |
| frontier-cost-growth | 2.4 | x per year (90% CI 2.0-2.9) | measured | cottier2024rising | abstract |
| frontier-cost-2027 | 1e9 | USD, lower bound for largest run | assumption | cottier2024rising | abstract (trend extrapolation) |
| training-energy-cost-share | 0.02-0.06 | share of amortized cost | measured | cottier2024rising | abstract |
| feasible-run-2030 | 2e29 | FLOP | assumption | sevilla2024scaling2030 | introduction |
| power-2e29-run-2030 | 6 | GW | assumption | sevilla2024scaling2030 | power section |
| h100e-2030-median | 1e8 | H100e available for training | assumption | sevilla2024scaling2030 | chip section |
| gpu-production-growth | 0.30-1.00 | annual growth to 2030 | assumption | sevilla2024scaling2030 | chip section |
| capex-big4-2026-feb | 650e9 | USD, 2026 plan | vendor | day2026capex | body |
| capex-big4-2026-growth | 0.60 | growth over 2025 | vendor | day2026capex | body |
| capex-big4-2026-may | 700e9 | USD, lower bound, 2026 plan | vendor | ehsan2026capex | body |
| dc-electricity-us-2023 | 176 | TWh | measured | shehabi2024datacenter | exec. summary |
| dc-electricity-us-2028 | 325-580 | TWh | assumption | shehabi2024datacenter | exec. summary |
| dc-electricity-world-2024 | 415 | TWh | measured | iea2025energyai | exec. summary |
| dc-electricity-world-2030 | 945 | TWh | assumption | iea2025energyai | exec. summary |
| interconnect-median-2025 | 61 | months, request to operation | measured | rand2026queued | slide 4 |
| interconnect-median-2015 | 36 | months | measured | rand2026queued | slide 4 |
| interconnect-queue-2025 | 2061 | GW active | measured | rand2026queued | slide 4 |
| interconnect-completion | 0.13 | share of capacity requested 2000-2020 now operating | measured | rand2026queued | slide 4 |
| transformer-lead-time | 128 | weeks | measured | woodmac2025connection | p. 5 |
| gsu-lead-time | 143 | weeks | measured | woodmac2025connection | p. 5 |
| transformer-deficit-2025 | 0.30 | supply shortfall, power transformers | assumption | woodmac2025transformers | press release |
| gas-turbine-backlog-gev | 116 | GW | vendor | bailey2026steam | body |
| gas-turbine-backlog-siemens | 69 | GW | vendor | bailey2026steam | body |
| gas-turbine-backlog-mhi | 35 | GW | vendor | bailey2026steam | body |
| china-solar-added-2025 | 315.07 | GW (AC) | measured | shaw2026chinasolar | NEA data |
| china-wind-added-2025 | 119.33 | GW | measured | shaw2026chinasolar | NEA data |
| horinger-h100e | 81000 | H100e (90% CI 36,000-141,000) | measured | cottier2026horinger | body |
| horinger-it-power | 286 | MW | measured | cottier2026horinger | body |
| china-compute-per-power | 0.40 | ratio to leading US facilities | measured | cottier2026horinger | body |
| dc-1gw-build-fastest | 11.6 | months to 1 GW | measured | somala2025buildtimes | table |
| dc-1gw-build-range | 1-3.6 | years to 1 GW | measured | somala2025buildtimes | body |
| fab-build-days-world | 682 | days, construction start to production | measured | verwey2021permits | p. 6 |
| fab-build-days-us-2010s | 918 | days | measured | verwey2021permits | p. 7 |
| decentralized-growth | 20 | x per year | assumption | sevilla2025decentralized | body (author estimate) |
| decentralized-largest-run | 6e22-6e23 | FLOP | measured | sevilla2025decentralized | body |
| huawei-ascend-2025-semianalysis | 805000 | Ascend units | measured | patel2025ascend | body |
| huawei-ascend-2025-commerce | 200000 | Ascend units, upper bound | measured | zafar2025kessler | Kessler quote |
| huawei-ascend-2025-idc | 812000 | AI chips shipped | measured | pan2026idc | body |
| huawei-die-bank | 2.9e6 | TSMC-made Ascend dies | measured | patel2025ascend | body |
| china-hbm-stockpile | 13e6 | HBM stacks | measured | patel2025ascend | body |
| smic-advanced-wspm-2025 | 45000 | wafers per month, end-2025 | measured | patel2025ascend | body (conservative) |
| smic-advanced-wspm-2027 | 80000 | wafers per month | assumption | patel2025ascend | body |
| china-accelerators-2025 | 4.0e6 | units shipped in China | measured | pan2026idc | IDC |
| nvidia-china-share-2025 | 0.55 | share of China accelerator units | measured | pan2026idc | IDC |
| smuggled-chips-2024-median | 140000 | chips | measured | grunewald2025smuggling | key judgments |
| smuggled-h100e-cum-2025 | 660000 | H100e (90% CI 290,000-1.6 million) | measured | juniewicz2026smuggling | body |
| smuggled-share-china | 0.33 | share of China's AI compute | measured | juniewicz2026smuggling | body |
| diversion-detection-rate | 0.25 | median share of diversion cases detected | assumption | juniewicz2026smuggling | methods |
| bis-budget-fy2025 | 191e6 | USD | measured | grunewald2025smuggling | recommendations |
| eccn-3a090-tpp | 4800 | TPP threshold | spec | bis2023advancedcomputing | 3A090.a |
| eccn-3a090-pd | 5.92 | performance density threshold (with TPP 1600) | spec | bis2023advancedcomputing | 3A090.a |
| eccn-3a090c-hbm | 2 | GB/s per mm2, HBM bandwidth density threshold | spec | bis2024hbm | 3A090.c |
| diffusion-weights-threshold | 1e26 | operations | spec | bis2025diffusion | ECCN 4E091 discussion |
| diffusion-country-tpp-cap | 7.9e8 | TPP, cumulative 2025-2027 | spec | bis2025diffusion | country allocation |
| h200-china-fee | 0.25 | share of sale value | spec | james2025h200 | body |
| talent-china-work-2025 | 0.41 | share of top AI talent working in China | measured | ma2026talent | findings |
| talent-us-work-2025 | 0.34 | share working in the US | measured | ma2026talent | findings |
| talent-neurips-authors-2025 | 25677 | unique NeurIPS 2025 authors | measured | ma2026talent | methodology |
| miri-strict-threshold | 1e24 | FLOP | design | scher2025agreement | section 4 |
| miri-monitored-threshold | 1e22 | FLOP | design | scher2025agreement | section 4 |
| miri-cluster-limit | 16 | H100e outside monitored facilities | design | scher2025agreement | section 4 |

Derived quantities the model could compute from these (not stated in any source):
- Growth of AI compute sold, 2024 to 2025: ai-compute-sold-2025 / ai-compute-sold-2024 = 2.67.
- Implied China AI compute stock end-2025: smuggled-h100e-cum-2025 / smuggled-share-china, about 2
  million H100e (an inference from Epoch's "roughly a third," not a stated number).
- Spread of outside estimates of Huawei 2025 output: huawei-ascend-2025-idc /
  huawei-ascend-2025-commerce, about 4.

## Prior art for the memo's candidates

**O1, the supply of inputs (who, how concentrated, how fast it grows, how visible).**
- Closest prior work: Sevilla et al. 2024 (Epoch, constraints to 2030: power, chips, data, latency),
  Pilz et al. 2025 (growth of AI supercomputers), Khan and Mann 2020 and Khan et al. 2021 (CSET,
  chokepoints and value shares), Varadarajan et al. 2024 (SIA/BCG concentration). Epoch's chip sales,
  chip owners and data-centre datasets already give per-input counts.
- Searches tried: "ASML 2025 annual results EUV systems shipped"; "TSMC CoWoS capacity wafers per
  month 2025 2026"; "HBM market share 2025 SK hynix Samsung Micron"; "NVIDIA data center AI
  accelerator market share 2025"; "hyperscaler capex 2026 guidance"; "LBNL Queued Up 2025 edition";
  "gas turbine lead times 2026"; "large power transformer lead time weeks 2025"; "CSET fab
  construction time days"; "MacroPolo Global AI Talent Tracker"; "Epoch AI frontier data centers
  hub"; "China National Energy Administration 2025 installed capacity".
- Judgement (a claim about our search): a per-input table of supplier count, concentration, growth
  rate and visibility exists piecemeal across these sources but I found no single source that puts
  all inputs (capital, chips by stage, power, talent, data) in one table with growth and visibility
  side by side. Compiling it would extend prior work, not be new in substance.

**O2, race dynamics.**
- Closest prior work: Armstrong, Bostrom and Shulman 2013/2016; Askell, Brundage and Hadfield 2019;
  Han et al. 2020; Stafford, Trager and Dafoe 2022; Emery-Xu, Park and Trager 2023/2024; Hendrycks,
  Schmidt and Wang 2025 (MAIM); Fudenberg and Koh 2026; Bueno de Mesquita, Dziuda and Polborn 2026.
- Searches tried: "Racing to the precipice Armstrong Bostrom Shulman"; "Stafford Trager Dafoe Safety
  Not Guaranteed"; "2025 game theory AI race safety paper arXiv race frontier labs safety investment
  model compute verification equilibrium"; crossref lookups for the JAIR and JCR papers.
- Judgement: race models are well developed prior work. They disagree on the sign of the effect of
  information (Armstrong et al. and Emery-Xu et al. under high decisiveness: more information can
  raise risk; Fudenberg and Koh: hidden capabilities make pacing harder). I found no race model that
  includes a verification regime with a stated detection time and asks how the detection time
  changes equilibrium safety. That combination (the memo's T_r inside a race model) was not found by
  our search; it could be an extension of prior work if the project builds it.

**O3, chokepoints where the protocol can stand.**
- Closest prior work: Sastry et al. 2024 ("detectable, excludable, and quantifiable," concentrated
  supply chain); Shavit 2023 (firmware snapshots plus supply-chain monitoring); Scher et al. 2025
  (MIRI treaty: chip tracking from fabrication including HBM, FLOP thresholds, 16 H100e cluster
  limit, halting unmonitored production); Khan and Mann 2020; Grunewald and Fist 2025 (location
  verification, notification, whistleblower rewards); the US export control rules themselves
  (2022, 2023, 2024, 2025), which already stand on the lithography, logic, HBM and chip stages;
  Epoch 2025 (satellite detection of data centres by cooling plant).
- Searches tried: "An International Agreement to Prevent the Premature Creation of Artificial
  Superintelligence"; "Computing Power and the Governance of AI"; "What does it take to catch a
  Chinchilla"; "CNAS countering AI chip smuggling"; "Superintelligence Strategy MAIM"; Federal
  Register API for documents 2022-21658, 2023-23055, 2024-28270, 2025-00636; "BIS rescinds AI
  diffusion rule"; "H200 exports to China approved".
- Judgement: O3 as framed in the memo (stand at the stages with fewest suppliers and largest
  plants) is prior work. The memo's candidates that may still extend it: (a) ranking stages by
  durability, using measured growth rates and erosion evidence (EUV tools +30% a year and a Chinese
  prototype years from volume, packaging +80% a year, HBM moving from three suppliers to four); (b)
  treating denial-induced footprint growth (40% compute per unit power at Horinger) as a detection
  gain to be quantified against P4's footprint floor. I did not find either done quantitatively in
  what I read; that is a claim about this search only.

**Evidence searched against the memo (erosion of chokepoints).** Searches: "Reuters China prototype
EUV lithography machine Shenzhen"; "SMIC 5nm Kirin 9030 TechInsights"; "Huawei Ascend roadmap
self-developed HBM"; "CXMT HBM3 mass production 2026"; "Kessler testimony Huawei 200,000"; "CSIS
analysis Huawei Ascend production 2025 2026"; "Epoch AI China compute share"; "Epoch Horinger". Found:
EUV erosion is slow (prototype, no chips, 2028 to 2030 targets); logic erosion is partial (N+3 short
of 5 nm, DUV yields low); HBM erosion is under way (CXMT DRAM share 4% to 10% in a year; Huawei's own
HBM announced; CXMT HBM timing reported inconsistently, and I did not open a source I would trust for
its yields); diversion and policy reversal are the largest leaks. The March 2025 CSIS report on
DeepSeek and Huawei, a Reuters original and an S&P Global turbine article returned access errors
and are not summarised.

## Sources (TOML)

```toml
[source.khan2020aichips]
type = "report"
title = "AI Chips: What They Are and Why They Matter"
authors = "Saif M. Khan and Alexander Mann (CSET)"
year = 2020
doi = "10.51593/20190014"
url = "https://cset.georgetown.edu/publication/ai-chips-what-they-are-and-why-they-matter/"
opened = "2026-11-27"

[source.khan2021supplychain]
type = "report"
title = "The Semiconductor Supply Chain: Assessing National Competitiveness"
authors = "Saif M. Khan, Alexander Mann, Dahlia Peterson (CSET)"
year = 2021
doi = "10.51593/20190016"
url = "https://cset.georgetown.edu/publication/the-semiconductor-supply-chain/"
opened = "2026-11-27"

[source.varadarajan2024resilience]
type = "report"
title = "Emerging Resilience in the Semiconductor Supply Chain"
authors = "Raj Varadarajan, Iacob Koch-Weser, Chris Richard, Joseph Fitzgerald, Jaskaran Singh, Mary Thornton, Robert Casanova, David Isaacs (BCG and SIA)"
year = 2024
url = "https://www.semiconductors.org/wp-content/uploads/2024/05/Report_Emerging-Resilience-in-the-Semiconductor-Supply-Chain.pdf"
opened = "2026-11-27"

[source.asml2026annualreport]
type = "vendor"
title = "ASML Annual Report 2025: Financial performance section"
authors = "ASML Holding N.V."
year = 2026
url = "https://ourbrand.asml.com/m/419103cb23dfeaa4/original/asml-2025-annual-report-financial-performance-section.pdf"
opened = "2026-11-27"

[source.shilov2026asml]
type = "news"
title = "ASML projects $71 billion in revenue by 2030, as demand for EUV lithography machines intensifies due to AI boom"
authors = "Anton Shilov (Tom's Hardware)"
year = 2026
url = "https://www.tomshardware.com/tech-industry/semiconductors/asml-projects-usd71-billion-in-revenue-by-2030-as-demand-for-euv-lithography-machines-intensifies-due-to-ai-boom-china-sales-lag-behind-while-company-cashes-in-on-high-end-twinscan-systems"
opened = "2026-11-27"

[source.asml2026q2call]
type = "vendor"
title = "ASML Q2 2026 earnings call transcript"
authors = "ASML Holding N.V. (Roger Dassen, Christophe Fouquet); transcript by The Motley Fool"
year = 2026
url = "https://www.fool.com/earnings/call-transcripts/2026/07/15/asml-asml-q2-2026-earnings-call-transcript/"
opened = "2026-11-27"

[source.trendforce2026cowos]
type = "news"
title = "TSMC CoWoS Supply-Demand Gap Reportedly Seen Narrowing from 20% to 10% by End-2026 as Capacity Expands"
authors = "TrendForce News"
year = 2026
url = "https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands"
opened = "2026-11-27"

[source.counterpoint2026hbm]
type = "report"
title = "Global DRAM and HBM Market Share: Quarterly"
authors = "Counterpoint Research"
year = 2026
url = "https://counterpointresearch.com/insights/global-dram-and-hbm-market-share"
opened = "2026-11-27"

[source.trendforce2026foundry]
type = "report"
title = "Global Foundry Revenue Approaches US$53.49 Billion in 2Q26 as SMIC Narrows Market Share Gap with Samsung"
authors = "TrendForce"
year = 2026
url = "https://www.trendforce.com/presscenter/news/20260909-13225.html"
opened = "2026-11-27"

[source.epoch2026chipsales]
type = "dataset"
title = "Data on AI chip sales"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/data/ai-chip-sales"
opened = "2026-11-27"

[source.you2026chipowners]
type = "report"
title = "Introducing the AI Chip Owners Explorer"
authors = "Josh You and Venkat Somala (Epoch AI)"
year = 2026
url = "https://epoch.ai/blog/introducing-the-ai-chip-owners-explorer"
opened = "2026-11-27"

[source.pilz2025supercomputers]
type = "preprint"
title = "Trends in AI Supercomputers"
authors = "Konstantin F. Pilz, James Sanders, Robi Rahman, Lennart Heim"
year = 2025
arxiv = "2504.16026"
opened = "2026-11-27"

[source.sevilla2024scaling2030]
type = "report"
title = "Can AI scaling continue through 2030?"
authors = "Jaime Sevilla, Tamay Besiroglu, Ben Cottier, Josh You, Edu Roldan, Pablo Villalobos, Ege Erdil (Epoch AI)"
year = 2024
url = "https://epoch.ai/blog/can-ai-scaling-continue-through-2030"
opened = "2026-11-27"

[source.sevilla2024computegrowth]
type = "report"
title = "Training compute of frontier AI models grows by 4-5x per year"
authors = "Jaime Sevilla and Edu Roldan (Epoch AI)"
year = 2024
url = "https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year"
opened = "2026-11-27"

[source.cottier2024rising]
type = "preprint"
title = "The rising costs of training frontier AI models"
authors = "Ben Cottier, Robi Rahman, Loredana Fattorini, Nestor Maslej, Tamay Besiroglu, David Owen"
year = 2024
arxiv = "2405.21015"
opened = "2026-11-27"

[source.day2026capex]
type = "news"
title = "Big Tech to Spend $650B This Year as AI Race Intensifies"
authors = "Matt Day (Bloomberg, via Data Center Knowledge)"
year = 2026
url = "https://www.datacenterknowledge.com/hyperscalers/big-tech-to-spend-650b-this-year-as-ai-race-intensifies"
opened = "2026-11-27"

[source.ehsan2026capex]
type = "news"
title = "Hyperscalers Hit $700 Billion in 2026 AI Spending Plans"
authors = "Omor Ibne Ehsan (Yahoo Finance)"
year = 2026
url = "https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html"
opened = "2026-11-27"

[source.iea2025energyai]
type = "report"
title = "Energy and AI: Executive Summary"
authors = "International Energy Agency"
year = 2025
url = "https://www.iea.org/reports/energy-and-ai/executive-summary"
opened = "2026-11-27"

[source.shehabi2024datacenter]
type = "report"
title = "2024 United States Data Center Energy Usage Report"
authors = "Arman Shehabi, Sarah Smith, Alex Hubbard, Alex Newkirk, Nuoa Lei, A.B. Saddik, Billie Holecek, Jonathan Koomey, Eric Masanet, Dale Sartor (LBNL)"
year = 2024
doi = "10.71468/P1WC7Q"
url = "https://eta-publications.lbl.gov/sites/default/files/2024-12/us_data_center_energy_usage_report_lbnl-2001637.pdf"
opened = "2026-11-27"

[source.rand2026queued]
type = "report"
title = "Queued Up: 2026 Edition, Characteristics of Power Plants Seeking Transmission Interconnection As of the End of 2025"
authors = "Joseph Rand, Anna Cheyette, Chris Talley, Steven Zhang, Will Gorman, Ryan Wiser, Joachim Seel, Seongeun Jeong, Fritz Kahrl (LBNL and Interconnection.fyi)"
year = 2026
url = "https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf"
opened = "2026-11-27"

[source.woodmac2025transformers]
type = "report"
title = "Power transformers and distribution transformers will face supply deficits of 30% and 10% in 2025, according to Wood Mackenzie"
authors = "Wood Mackenzie"
year = 2025
url = "https://www.woodmac.com/zh/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/"
opened = "2026-11-27"

[source.woodmac2025connection]
type = "report"
title = "Making the connection: meeting the electric T&D supply chain challenge, Executive Summary"
authors = "Wood Mackenzie and American Clean Power"
year = 2025
url = "https://www.powermag.com/wp-content/uploads/2026/01/making-the-connection-executive-summary-september-2025.pdf"
opened = "2026-11-27"

[source.bailey2026steam]
type = "news"
title = "Is Steam the Answer to the Gas Turbine Bottleneck?"
authors = "Richard Bailey, Anthony Brough, Alicia Bigica (Turbomachinery Magazine)"
year = 2026
url = "https://www.turbomachinerymag.com/view/steam-turbines-gas-turbine-bottleneck-siemens-energy"
opened = "2026-11-27"

[source.shaw2026chinasolar]
type = "news"
title = "China adds 315 GW of solar in 2025"
authors = "Vincent Shaw (pv magazine)"
year = 2026
url = "https://www.pv-magazine.com/2026/01/28/china-adds-315-gw-of-solar-in-2025/"
opened = "2026-11-27"

[source.cottier2026horinger]
type = "report"
title = "What Huawei's Horinger data center reveals about China's compute gap"
authors = "Ben Cottier (Epoch AI)"
year = 2026
url = "https://epoch.ai/publications/huawei-horinger-china-compute-gap"
opened = "2026-11-27"

[source.epoch2025datacentershub]
type = "report"
title = "Introducing the Frontier Data Centers Hub"
authors = "Epoch AI"
year = 2025
url = "https://epoch.ai/blog/introducing-the-frontier-data-centers-hub/"
opened = "2026-11-27"

[source.somala2025buildtimes]
type = "report"
title = "Build times for gigawatt-scale data centers can be 2 years or less"
authors = "Venkat Somala and Ben Cottier (Epoch AI)"
year = 2025
url = "https://epoch.ai/data-insights/data-centers-buildout-speeds"
opened = "2026-11-27"

[source.sevilla2025decentralized]
type = "essay"
title = "How far can decentralized training over the internet scale?"
authors = "Jaime Sevilla (Epoch AI Gradient Updates)"
year = 2025
url = "https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale"
opened = "2026-11-27"

[source.verwey2021permits]
type = "report"
title = "No Permits, No Fabs: The Importance of Regulatory Reform for Semiconductor Manufacturing"
authors = "John VerWey (CSET)"
year = 2021
doi = "10.51593/20210053"
url = "https://cset.georgetown.edu/wp-content/uploads/CSET-No-Permits-No-Fabs.pdf"
opened = "2026-11-27"

[source.techinsights2025kirin]
type = "report"
title = "SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm"
authors = "TechInsights"
year = 2025
url = "https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm"
opened = "2026-11-27"

[source.techinsights2026datacenter]
type = "report"
title = "Analysis: Can China even build data center AI chips?"
authors = "TechInsights"
year = 2026
url = "https://www.techinsights.com/ja/node/61228"
opened = "2026-11-27"

[source.washenko2025euv]
type = "news"
title = "China reportedly has a prototype EUV machine built by ex-ASML employees"
authors = "Anna Washenko (Engadget, relaying Reuters)"
year = 2025
url = "https://www.engadget.com/big-tech/china-reportedly-has-a-prototype-euv-machine-built-by-ex-asml-employees-235833756.html"
opened = "2026-11-27"

[source.xu2025huaweiconnect]
type = "vendor"
title = "Groundbreaking SuperPoD Interconnect: Leading a New Paradigm for AI Infrastructure"
authors = "Eric Xu (Huawei), keynote at Huawei Connect 2025"
year = 2025
url = "https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech"
opened = "2026-11-27"

[source.patel2025ascend]
type = "report"
title = "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck"
authors = "Dylan Patel, AJ, Myron Xie (SemiAnalysis)"
year = 2025
url = "https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp"
opened = "2026-11-27"

[source.pan2026idc]
type = "news"
title = "Chinese chipmakers claim nearly half of local market as Nvidia's lead shrinks"
authors = "Che Pan and Laurie Chen (Reuters, via Yahoo Finance)"
year = 2026
url = "https://finance.yahoo.com/sectors/technology/articles/chinese-chipmakers-claim-nearly-half-091441757.html"
opened = "2026-11-27"

[source.blablova2025china]
type = "essay"
title = "Why China isn't about to leap ahead of the West on compute"
authors = "Veronika Blablova and Robi Rahman (Epoch AI Gradient Updates)"
year = 2025
url = "https://epoch.ai/gradient-updates/why-china-isnt-about-to-leap-ahead-of-the-west-on-compute"
opened = "2026-11-27"

[source.zafar2025kessler]
type = "news"
title = "China's Huawei Can Make 200,000 Advanced AI Chips In 2025 At Most, Says US Official"
authors = "Ramish Zafar (Wccftech)"
year = 2025
url = "https://wccftech.com/chinas-huawei-can-make-200000-advanced-ai-chips-in-2025-at-most-says-us-official/"
opened = "2026-11-27"

[source.allen2025senate]
type = "official-docs"
title = "China's Challenge to American AI Leadership (written testimony before the Senate Foreign Relations Committee)"
authors = "Gregory C. Allen (CSIS)"
year = 2025
url = "https://www.foreign.senate.gov/download/120225_allen_testimonypdf"
opened = "2026-11-27"

[source.grunewald2025smuggling]
type = "report"
title = "Countering AI Chip Smuggling Has Become a National Security Priority: An Updated Playbook for Preventing AI Chip Smuggling to the PRC"
authors = "Erich Grunewald and Tim Fist (CNAS)"
year = 2025
url = "https://www.cnas.org/publications/reports/countering-ai-chip-smuggling-has-become-a-national-security-priority"
opened = "2026-11-27"

[source.juniewicz2026smuggling]
type = "report"
title = "Diversion and resale: estimating compute smuggling to China"
authors = "Isabel Juniewicz (Epoch AI)"
year = 2026
url = "https://epoch.ai/blog/chip-smuggling"
opened = "2026-11-27"

[source.bis2022advancedcomputing]
type = "legislation"
title = "Implementation of Additional Export Controls: Certain Advanced Computing and Semiconductor Manufacturing Items; Supercomputer and Semiconductor End Use; Entity List Modification (87 FR 62186)"
authors = "Bureau of Industry and Security, US Department of Commerce"
year = 2022
url = "https://www.federalregister.gov/documents/2022/10/13/2022-21658/implementation-of-additional-export-controls-certain-advanced-computing-and-semiconductor-manufacturing-items"
opened = "2026-11-27"

[source.bis2023advancedcomputing]
type = "legislation"
title = "Implementation of Additional Export Controls: Certain Advanced Computing Items; Supercomputer and Semiconductor End Use; Updates and Corrections (88 FR 73458)"
authors = "Bureau of Industry and Security, US Department of Commerce"
year = 2023
url = "https://www.federalregister.gov/documents/2023/10/25/2023-23055/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and-semiconductor-end-use-updates"
opened = "2026-11-27"

[source.bis2024hbm]
type = "legislation"
title = "Foreign-Produced Direct Product Rule Additions, and Refinements to Controls for Advanced Computing and Semiconductor Manufacturing Items (89 FR 96790)"
authors = "Bureau of Industry and Security, US Department of Commerce"
year = 2024
url = "https://www.federalregister.gov/documents/2024/12/05/2024-28270/foreign-produced-direct-product-rule-additions-and-refinements-to-controls-for-advanced-computing-and-semiconductor-manufacturing-items"
opened = "2026-11-27"

[source.bis2025diffusion]
type = "legislation"
title = "Framework for Artificial Intelligence Diffusion (90 FR 4544)"
authors = "Bureau of Industry and Security, US Department of Commerce"
year = 2025
url = "https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion"
opened = "2026-11-27"

[source.bis2025rescission]
type = "official-docs"
title = "Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls"
authors = "Bureau of Industry and Security, US Department of Commerce"
year = 2025
url = "https://www.bis.gov/press-release/department-commerce-rescinds-biden-era-artificial-intelligence-diffusion-rule-strengthens-chip-related"
opened = "2026-11-27"

[source.james2025h200]
type = "news"
title = "The Nvidia H200 export saga, as it happened"
authors = "Luke James (Tom's Hardware)"
year = 2025
url = "https://www.tomshardware.com/tech-industry/semiconductors/us-eases-nvidia-export-restrictions-h200-cleared-for-china-under-tight-controls"
opened = "2026-11-27"

[source.ma2026talent]
type = "report"
title = "Who's Ahead in the Global AI Talent Race?"
authors = "Damien Ma and Binyi Yang (Carnegie China, Carnegie Endowment for International Peace)"
year = 2026
url = "https://carnegieendowment.org/features/whos-ahead-in-the-global-ai-talent-race"
opened = "2026-11-27"

[source.sastry2024compute]
type = "preprint"
title = "Computing Power and the Governance of Artificial Intelligence"
authors = "Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield, Richard Ngo, Konstantin Pilz, George Gor, Emma Bluemke, Sarah Shoker, Janet Egan, Robert F. Trager, Shahar Avin, Adrian Weller, Yoshua Bengio, Diane Coyle"
year = 2024
arxiv = "2402.08797"
opened = "2026-11-27"

[source.shavit2023chinchilla]
type = "preprint"
title = "What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring"
authors = "Yonadav Shavit"
year = 2023
arxiv = "2303.11341"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.hendrycks2025superintelligence]
type = "preprint"
title = "Superintelligence Strategy: Expert Version"
authors = "Dan Hendrycks, Eric Schmidt, Alexandr Wang"
year = 2025
arxiv = "2503.05628"
opened = "2026-11-27"

[source.pilz2023efficiency]
type = "preprint"
title = "Increased Compute Efficiency and the Diffusion of AI Capabilities"
authors = "Konstantin Pilz, Lennart Heim, Nicholas Brown"
year = 2023
arxiv = "2311.15377"
opened = "2026-11-27"

[source.armstrong2016racing]
type = "peer-reviewed"
title = "Racing to the precipice: a model of artificial intelligence development"
authors = "Stuart Armstrong, Nick Bostrom, Carl Shulman"
year = 2016
doi = "10.1007/s00146-015-0590-y"
url = "https://www.futureofhumanityinstitute.org/s/2013-1.pdf"
opened = "2026-11-27"

[source.askell2019cooperation]
type = "preprint"
title = "The Role of Cooperation in Responsible AI Development"
authors = "Amanda Askell, Miles Brundage, Gillian Hadfield"
year = 2019
arxiv = "1907.04534"
opened = "2026-11-27"

[source.stafford2022safety]
type = "preprint"
title = "Safety Not Guaranteed: International Races for Risky Technologies"
authors = "Eoghan Stafford, Robert F. Trager, Allan Dafoe"
year = 2022
url = "https://cdn.governance.ai/International_Races_for_Risky_Technologies_DRAFT_NOV_2022.pdf"
opened = "2026-11-27"

[source.han2020regulate]
type = "peer-reviewed"
title = "To Regulate or Not: A Social Dynamics Analysis of an Idealised AI Race"
authors = "The Anh Han, Luis Moniz Pereira, Francisco C. Santos, Tom Lenaerts"
year = 2020
doi = "10.1613/jair.1.12225"
opened = "2026-11-27"

[source.emeryxu2024uncertainty]
type = "peer-reviewed"
title = "Uncertainty, Information, and Risk in International Technology Races"
authors = "Nicholas Emery-Xu, Andrew Park, Robert Trager"
year = 2024
doi = "10.1177/00220027231214996"
url = "https://aigi.ox.ac.uk/publications/uncertainty-information-and-risk-in-international-technology-races/"
opened = "2026-11-27"

[source.fudenberg2026cooperating]
type = "preprint"
title = "Cooperating Against Catastrophe"
authors = "Drew Fudenberg and Andrew Koh"
year = 2026
url = "https://economics.mit.edu/sites/default/files/inline-files/Pacing.pdf"
opened = "2026-11-27"

[source.buenodemesquita2026agirace]
type = "report"
title = "The AGI Race and Existential Risk (research brief of BFI Working Paper 2026-71)"
authors = "Ethan Bueno de Mesquita, Wioletta Dziuda, Mattias Polborn (Becker Friedman Institute)"
year = 2026
url = "https://bfi.uchicago.edu/wp-content/uploads/2026/09/The-AGI-Race-and-Existential-Risk-2.pdf"
opened = "2026-11-27"
```
