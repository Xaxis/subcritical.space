# Novelty: what is ours, what extends prior work, what is prior work

The memo ([00-memo.md](00-memo.md)) labelled every candidate new, extends prior work, or prior work
before anyone searched. Those labels were beliefs. This file records what the independent search
found. Ten survey tracks searched the literature, none of them run by the helper that proposed the
ideas. Each track's note in `notes/` ends with the closest prior work it found, the queries it ran
and a judgement. An independent spot-check then reopened a sample of the notes' claims against the
sources themselves. This file relies on none of the claims that check found distorted.

Every label here is a claim about our search, not about the world. "Not found" means not found by
the queries listed under each idea, and nothing more. Where two tracks disagree, this file takes the
more cautious label. Level 1, a second search by helpers that did not propose the ideas, has now
run for the twelve claims built on them, in two reports,
[C1 to C6](verification/l1-prior-art-c1-c6.md#summary) and
[C7 to C12](verification/l1-prior-art-c7-c12.md#summary). Where it found closer work, the label
below has moved down and its works are credited. A reviewer may still move any label down. Nothing
here moves up without a new search.

The labels:

- **Prior work.** The idea, as the memo states it, is already in the literature. Subcritical may use
  it and must credit it.
- **Extends prior work.** The core is prior work, but a narrow, stated difference was not found by
  our search. Only that difference can be claimed, and only once it passes every level.
- **New.** Nothing close was found. After the search, no candidate holds this label.

Level 1 adds two finer labels, which [the claims file](04-claims.md#summary) also uses. An idea that is
prior work may still be **applied** to AI; then only the application, and any result computed inside
it, is ours. An idea that extends prior work may be a **combination**: each part is known, and only
the combination was not found.

The short version: the memo believed one definition new and several ideas possibly new. None of
them survives as new, and level 1 took five more down to prior work. Most of the anatomy is prior
work, which is what it should be: the paper draws it together rather than discovers it. What
survived level 1 as possibly ours was a short list of narrow extensions, most of them estimators,
bounds and one small lemma. Level 6 found each of them textbook, a calculation, untested or a
judgement, so none survives as a candidate; the list at the end says what each became, with the
claim that carries it.

## Summary

| Idea | Memo's label | Label now | Closest prior work | What remains possibly ours |
|---|---|---|---|---|
| P1 Compute budget | none stated | prior work | [@carlsmith2020]; [@davidson2023compute]; [@sandberg2008] | nothing as stated; tying the budget to D1 was not searched |
| P2 Energy headroom | none stated | prior work | [@ho2023]; [@koomey2011]; [@davidson2025three] | at most its use as a bound inside P4 |
| P3 Memory and bandwidth | none stated | prior work | [@gholami2024]; [@erdil2024datamovement]; [@douillard2023diloco] | nothing |
| P4 Footprint floor | may be new | prior work | [@fithian2026hardwired]; [@koopmanschap2026gpu]; [@iaea-glossary-2022]; [@rahman2026] | applied, with calculations: the floor as a bound at the lowest precision and full utilisation, each channel's margin and crossing year (C8) |
| A1 Capability against effective compute | none stated | prior work | [@hoffmann2022chinchilla]; [@ruan2024observational]; [@ho2025rosetta] | only the choice of capability axis for D4 |
| A2 Training-inference exchange, cap leak | none stated | prior work | [@villalobos2023tradeoff]; [@pistillo2025loopholes]; [@ord2025govaireport]; [@heim2024thresholds] | only as the fixed-compute case of D3's per-path expression |
| A3 Algorithmic progress | none stated | prior work, contested | [@ho2024algorithmic]; [@gundlach2025origin]; [@whitfill2025selection] | nothing |
| A4 Data | none stated | prior work | [@villalobos2022data]; [@shumailov2024collapse]; [@gerstgrasser2024accumulate] | nothing |
| A5 Search and planning | none stated | prior work | [@silver2017alphagozero]; [@wang2023adversarialgo]; [@huan2026mathtransfer] | transfer as a quantity a protocol can threshold |
| Y1 Loops as growth laws | none stated | prior work | [@davidson2025three]; [@davidson2026feedback]; [@cunningham2026rsi] | the experiential and acquisitive loops in the same form (not searched) |
| Y2 Runaway against saturation | none stated | prior work | [@besiroglu2024returns]; [@eth2025sie]; [@whitfill2025bottlenecks] | measurement only |
| Y3 Coupling | none stated; the project's name implies it is ours | prior work | [@davidson2026feedback]; [@burtsev2026criticality]; [@dashkovskiy2007smallgain]; [@roberts2003typer] | applied: the small-gain certificate as a treaty test, each edge gated and verified (C6) |
| F1 Speed, copies, quality | typology prior work; the institutional measure may not be | prior work | [@grace2014forms]; [@wijk2024rebench]; [@lifland2025timelines]; [@pope2022] | nothing: copies from held compute follow from a known bound and forecasts already compute them, cut as too small; quality against institutions is D1's |
| F2 Decisive functions | none stated | prior work | [@openai2025preparedness]; [@anthropic2026rsp]; [@wijk2024rebench] | a measured institutional baseline, which no source has: contest teams and policy text only |
| F3 Narrow against general | none stated | extends prior work | [@morris2023levels]; [@genewein2026agiasi]; [@novikov2025alphaevolve] | nothing on its own: D4's line (C1) replaces it as the line, its parts merged into C10 and C11 |
| O1 Supply of inputs | none stated | prior work | [@sevilla2024scaling2030]; [@khan2021supplychain]; [@varadarajan2024resilience] | nothing of substance |
| O2 Race dynamics | prior work | prior work | [@armstrong2016racing]; [@emeryxu2024uncertainty]; [@fudenberg2026cooperating] | a race model with the regime's detection time inside it, built in E6 as a tool; the candidate that compliance-only disclosure does not raise risk is cut by E6 |
| O3 Chokepoints | none stated | prior work | [@sastry2024compute]; [@scher2025agreement]; [@khan2020aichips] | denial-induced footprint growth as a detection gain; ranking stages by durability is unsupported and undecidable (E23) |
| D1 Superintelligence against the best organisation | extends | extends prior work | [@robinson2026horizons]; [@wijk2024rebench]; [@genewein2026agiasi]; [@anthropic2026rsp] | as a definition: time and money matched together against an organisation, the alpha fraction, a censored t* that stops at each battery's ceiling (C10) |
| D2 Loop gain | condition prior work; the estimator may be new | extends prior work, narrowly | [@srikanth2026aide2]; [@blumberg2020supercritical]; [@cunningham2026rsi]; [@burtsev2026criticality] | the exact round identity as the estimator of K, and the budget ladder, as a measurement design only: its estimator fails at calibrated noise (C4) |
| D3 Breakout time | extends | extends prior work, as a combination | [@fithian2026hardwired]; [@gan2026clock]; [@pistillo2025loopholes]; [@villalobos2023tradeoff] | nothing: an accounting frame credited to prior work, since tabulating it in advance is cut (C2(a)), its backtest is cut as untestable on public data (C2(c), E18) and its gain over one multiplier is not shown (C2(b)) |
| D4 Weapons-grade line | new | prior work | [@snell2007itc20]; [@hafemeister2008ctbt]; [@gan2026clock]; [@fithian2026hardwired] | applied to AI holdings (C1); the margin as an error budget is the partial-factor format of structural design |
| D5 Elicited capability | extends | extends prior work | [@fda2007diagnostic]; [@greenblatt2024password]; [@abubaker2026fuzzing]; [@taylor2025auditinggames] | rates per named budget over a defined organism population, as a multi-party rule, against non-adaptive hiding: an untested design (C5) |
| D6 Closure | may be new, or only framing | extends prior work, narrowly; framing until tested | [@aghion2017ai]; [@burtsev2026criticality]; [@miotti2025narrowpath] | closure input by input against verifiable gates, the gain predicted from one gate at a time (C11) |
| The pathway ranking | none stated | prior work | [@clarke2022mtair]; [@barrett2016asipath]; [@fithian2026hardwired]; [@remler2026distillation] | applied: the ranking itself, a judgement, with [12](numbers.md#claim-c12-pareto-two) pairs Pareto-ordered under our grades; theft of weights not ranked (C12) |
| The organising idea (safeguards timeliness) | none stated | prior work, and the memo misstates the nuclear record | [@openai2023governance]; [@sastry2024compute]; [@iaea-glossary-2001] | nothing |
| Registered chips under expiring licences | none stated | prior work | [@petrie2025flexheg1]; [@petrie2025flexheg2]; [@kulp2024hem]; [@aarne2024securechips] | nothing |
| Renewal by k of n licensors from rival blocs | none stated | prior work | [@petrie2025flexheg2]; [@aarne2025flexheg3]; [@petrie2024offline] | nothing; the deadlock and double-signing problems flexHEG names remain open |
| Bitcoin block height as licence clock and freshness | none stated | prior work | [@bentov2016beacon]; [@mouallem2026alerting]; [@bentov2019tesseract]; [@lightning-bolt2] | the assembly for chip licences, as engineering (C9) |
| Sealed declarations | none stated | prior work | [@tomescu2017catena]; [@laurie2013ct]; [@apple2024pcc]; [@burford2020trustmachine] | the assembly with chip licences in one log, as engineering (C9) |
| Evaluations on elicited capability against the line | none stated | prior work | [@anthropic2023rsp]; [@openai2025preparedness]; [@eu2025gpaicode] | only what D4 and D5 add |
| Continual-learning updates counted toward compute, re-evaluation on drift | none stated | prior work (provisional, not searched) | [@fpf-sb53-2025]; [@ec-gpai-guidelines-faq-2025]; [@anthropic2026rsp] | a drift trigger on elicited capability for fleets that update after deployment |
| Bans on closed loops above a loop-gain threshold | none stated | prior work | [@miotti2025narrowpath]; [@redlines-2025]; [@scher2025agreement] | only the trigger, which is D2's, cut with its estimator (C4) |
| Multi-channel detection guarantee over breakout time | none stated | prior work | [@snell2007itc20]; [@washburn1995interdiction]; [@gif2011prppem]; [@baker2025verifying] | applied to AI paths (C3); the merging rule is the textbook bound on a union |
| Random challenge inspections | none stated | prior work | [@scher2025agreement]; [@opcw-ec109-dg22]; [@infcirc-540] | nothing |
| Rewarded whistleblowing | none stated | prior work | [@scher2025agreement]; [@baker2025verifying]; [@dyck2007whistle] | a transferred detection rate, with caveats |
| Power and heat signatures | none stated | prior work | [@wasil2024verification]; [@kimpson2026dcpower]; [@jing2026] | nothing |
| Inspection games for compliance | none stated | prior work | [@avenhaus2002inspection]; [@vonstengel2016recursive]; [@gan2026clock] | an AI treatment with announced random inspections, evasion across channels and renewal end effects |
| Coalition compute threshold | none stated | prior work | [@fithian2026hardwired]; [@whitehouse2015jcpoaparameters]; [@aubert2006leniency] | applied: nothing independent of D4 (C7) |
| Withdrawal notice longer than the response time | none stated | prior work | [@scher2025agreement]; [@eu2005nptwithdrawal]; [@helfer2005exiting] | the derived inequality, with an asset freeze |

## Mechanisms

### P1 Compute budget

**Closest prior work.**
- Estimates of the brain's compute as a reference point. [@carlsmith2020] gives a central estimate
  inside a range spanning several orders of magnitude, and says matching the brain depends on
  software "which may be very hard to create". [@sandberg2008] and [@levy2021] are the other
  references track 02 used.
- Compute requirements for transformative AI stated in effective compute, with hardware and
  software in standard semi-endogenous growth models [@davidson2023compute].
- Held compute measured from chip counts, peak rates and power is already public data: chip sales
  by quarter [@epoch2026chipsales], chip owners [@you2026chipowners] and frontier data centres with
  power estimated from satellite images [@epoch2025datacentershub].

**What remains.** Nothing as the memo states it. Tying the budget to D1, an endpoint matched to the
best human organisation, rather than to a human-level reference, was not searched by any track.

**Searches tried.** Track 02 lists queries only for P4; its P1 judgement rests on the sources it
opened on the brain and on accelerators. Track 04 opened [@davidson2023compute] under the takeoff
searches listed under Y1.

**Label: prior work.** Track 02 judged the brain reference prior work, and the memo already treats
it as a reference, not a target, which the sources support.

### P2 Energy per useful operation, and the headroom to physics

**Closest prior work.**
- [@ho2023] computes the efficiency ceiling of irreversible CMOS and the headroom over current
  GPUs.
- [@koomey2011] quotes Feynman's estimate of the headroom to physics.
- [@carlsmith2020] uses Landauer's bound [@landauer1961] to bound the brain's computation.
- [@davidson2025three] uses the room to grow in chip technology, within the current paradigm and up
  to Landauer, as the limit on its chip-technology feedback loop.

**What remains.** Track 02 found that only one use is not drawn in [@ho2023]: the headroom as an
upper bound on how far the footprint of a fixed computation can shrink. Track 04's
[@davidson2025three] already uses the same headroom to bound hardware growth, which is close. At
most this is a step inside P4, not a separate contribution.

**Design consequence.** There are two headrooms, not one. Within the protocol's horizon the binding
limit is CMOS [@ho2023], not Landauer; going further needs adiabatic or reversible logic, which has
only reached prototype chips with modest savings [@genkina2025; @hulick2025]. The memo's comparison
with Landauer alone points at the wrong limit for the near term.

**Searches tried.** Track 02 lists none for P2 separately; the judgement rests on the sources it
opened on thermodynamic limits and efficiency trends.

**Label: prior work.**

### P3 Memory and bandwidth

**Closest prior work.** The memory wall, with compute outgrowing memory and interconnect bandwidth
[@gholami2024]; hardware trends [@hobbhahn2023]; data-movement limits to scaling
[@erdil2024datamovement]; low-communication training [@douillard2023diloco;
@douillard2025streaming]; and the governance consequences of decentralised training
[@sevilla2025decentralized; @krys2025distributed].

**What remains.** Nothing.

**Design consequence.** Low-communication training loosens the interconnect limit that made frontier
training a single-site activity. That feeds straight into P4 and into the failure mode of training
spread across many small sites.

**Searches tried.** Track 02's decentralised-training queries, listed under P4.

**Label: prior work.**

### P4 Footprint, and its floor

**Closest prior work.**
- [@koopmanschap2026gpu] defines an "enforcement breaking point", the threshold at which a policy stops
  working, and traces how satellites, power monitoring and information gathering degrade as facility
  size falls. In the sample it reports, a satellite classifier found every facility above a modest
  power line and missed every one below it. This is the memo's comparison of a floor with a
  detection limit, stated per facility size.
- [@scher2025] and [@scher2025agreement] argue that facility detection fails at small
  sizes, that efficiency gains shrink the power a fixed computation needs, and set a small cluster
  limit enforced through chips rather than buildings.
- [@rahman2026] computes, for given training targets, the cheapest distributed configuration of
  nodes each below a registration threshold: in effect a cost and node-count floor for evading
  facility detection.
- [@halstead-ai2040] gives per-site detection probabilities by facility size and number of sites for
  a covert project.
- [@sastry2024compute], [@wasil2024verification] and [@sevilla2025decentralized] treat the
  detectability of compute from power and footprint, with the distributed-training caveat.
- Track 01 adds the covert evasion capacity ledgers of [@fithian2026hardwired] and the cluster-rate
  thresholds of [@eo14110-2023] and [@miotti2025narrowpath]. Track 06 adds evidence that a party
  denied leading-edge chips needs more power and building for the same compute
  [@cottier2026horinger]. Track 08 adds the nuclear record: inspectors read a hidden plant's
  electrical load [@thorne-1992], and the state concerned buried power lines to hide it
  [@albright-2002].
- Level 1 ([C8](verification/l1-prior-art-c7-c12.md#c8)) found the closest work in
  [@fithian2026hardwired]: the formula as an aggregate floor in chips with a time axis, the untraced
  pool entered against it, and the conclusion that the pool must be shrunk rather than found. That
  chip accounting must resolve less than the floor is the IAEA's lesson on material unaccounted for
  [@iaea-glossary-2022].

**What remains.** The survey found no floor under that name; level 1 found the floor itself. Three
narrow differences remain: the floor as a bound, at the highest attainable utilisation, the lowest
precision and the lowest energy per operation, where the hardwired-pause threshold is an estimate at
standard utilisation; each facility channel's margin as a ratio to the floor, with the year it
crosses one; and the pool's multiple of the floor at small-run inputs, with a measured discovery
rate behind the conclusion. Each is a computation others could easily have run, and level 6 judged
them an application with calculations: the bound cannot fail, being a sum, and the pool is an
assumption. They are C8's, in
[the claims file](04-claims.md#c8-the-aggregate-footprint-floor-a-margin-per-channel-and-the-untraced-pool).

**Design consequence.** The memo treats satellites, grids and supply-chain accounting as seeing one
floor. They do not. Satellites and grids see sites, and a site can be a single small node far below
any facility signature [@rahman2026]. Thermal infrared did not see the waste heat of a large cluster
[@jing2026], and water use is optional at closed-loop sites. Of the channels modelled, only chip and
supply-chain accounting see the aggregate; a run spread over sites still leaves aggregate signatures
in the traffic between them and the money and power behind it, which E8 does not model (C8.4). The
floor must be defined twice: a per-site floor, which distribution drives toward one node, and an
aggregate floor in chips and energy, which hardware efficiency lowers only until CMOS binds
[@ho2023] and algorithmic progress lowers further.

**Searches tried.**
- Track 02: "minimum facility size to train frontier AI model detection threshold covert data
  center power signature verification" (extended); "\"dark compute\" OR \"covert compute\" minimum
  cluster size frontier training detection satellite power AI governance 2026" (extended);
  "\"footprint\" smallest data center capable of training frontier model \"detection\" floor energy
  efficiency improvements shrink detectability AI verification"; "Epoch AI frontier data centers
  satellite imagery methodology cooling equipment estimate power"; "satellite land surface
  temperature data center heat island Landsat study"; "arXiv \"compute structuring\" detection AI
  governance splitting training runs across clusters"; "Epoch AI decentralized training over the
  internet how far can it scale"; plus references followed inside the papers found. One relevant
  paper on detecting compute structuring was behind a bot wall, was not opened, and is not cited.
- Track 01 ran no separate P4 query and reports the floor "not found in this track".
- Track 06 searched chokepoint erosion (listed under O3), which bears on the denial-induced growth in
  footprint.

**Label: prior work, applied, with calculations.** Tracks 01 and 02 agreed that the named floor was
not found, and track 02 showed that every part of it exists. Level 1 found the floor, its time axis
and the pool in the hardwired-pause paper and left the bound, the crossing years and the measured
discovery rate as a narrow extension; level 6 found those calculations, not contributions. The
memo's "may be new" does not survive.

### A1 Capability as a function of effective compute

**Closest prior work.** Scaling laws [@kaplan2020scaling; @hoffmann2022chinchilla;
@besiroglu2024replication]; observational scaling across public models [@ruan2024observational];
the predictability of benchmark scores from compute [@owen2024predictable]; a stitched capability
scale with a compute slope [@ho2025rosetta]. Most claimed emergence is a metric artefact
[@schaeffer2023mirage].

**What remains.** Only choosing the capability axis on which D4's line sits.

**Design consequence.** Capability is predictable from compute in aggregate and poorly per task, so a
line set on one task's score will be far noisier than one set on an aggregate.

**Searches tried.** Track 03, for all of A1 to A5: "algorithmic progress language models
scale-dependent 2025 arXiv origin of algorithmic progress"; "NanoGPT speedrun record history
modded-nanogpt world record time"; "Toby Ord inference scaling reshapes AI governance"; "training
compute threshold effectiveness algorithmic efficiency erodes compute threshold governance paper";
"Whitfill algorithmic progress selection bias Ho et al estimate overstated 2025"; extended search
"\"effective compute\" fixed training compute cap how quickly algorithmic progress inference
scaling erode cap years estimate"; "Epoch AI LLM inference price trends decline per year fixed
capability 2025"; "Toby Ord \"how well does RL scale\" OR \"inference scaling and the log-x
chart\""; "MIRI international agreement prevent premature artificial superintelligence training
compute threshold algorithmic progress research restrictions arXiv"; "Epoch AI frontier performance
runs on consumer GPU lag months open models data insight 2025"; "Does math reasoning improve
general LLM capabilities transferability RL vs SFT arXiv 2025".

**Label: prior work.**

### A2 The exchange rate between training and inference compute, and the cap leak

**Closest prior work.**
- Measured exchange rates: on board games, extra training substitutes for test-time compute
  [@jones2021boardgames]; per technique, with spans [@villalobos2023tradeoff]; dependent on problem
  difficulty, not one for one [@snell2024testtime].
- The governance consequence, that a training cap leaks through inference, is stated in
  [@villalobos2023tradeoff], [@ord2025inferencegov] and [@ord2025govaireport].
- The wider cap leak: thresholds should move down as efficiency improves, with a safety buffer for
  post-training enhancement [@heim2024thresholds]; access and performance effects of efficiency
  [@pilz2023efficiency]; post-training enhancements improve capability without retraining
  [@davidson2023enhancements]; many innovations remain feasible under stringent caps
  [@barnett2025innovation]; a range of efficiency growth rates with no calculation
  [@barnett2026closingwindow]; a fixed cap that cites algorithmic progress but sets no schedule
  [@scher2025agreement].
- Level 1, searching for the claim that carries the leak ([C2](verification/l1-prior-art-c1-c6.md#c2)),
  adds additive accounting of fine-tuning, above-optimal inference and distillation against a training
  threshold [@pistillo2025loopholes], and reads the span set by a cheap verifier as an accounting rule
  already in [@villalobos2023tradeoff].

**What remains.** A leak model that (i) stacks techniques, (ii) says where each technique's span
stops, which depends on whether a cheap verifier exists, (iii) charges the inference spent against
the same chip accounting, (iv) uses scale-dependent efficiency [@gundlach2025origin] and adds the
one-off jumps from post-training and distillation, and (v) states the result as the time until a
capped party reaches a given capability, compared with the response time T_r. Not found by track 03.
Level 1 narrowed this: (ii) is a prior accounting rule, and so is charging a distilled model at its
teacher's compute, or lowering the threshold by the compute distillation saves
[@pistillo2025loopholes]. Distillation sets no ceiling either, since a student can exceed its
teacher [@furlanello2018born; @burns2023weak]. What remains is the leak as the fixed-compute case of
D3's per-path expression, tied to T_r.

**Design consequence.** Distillation from an uncapped teacher leaks most cheaply
[@deepseek2025r1]. Inference spent to substitute for training is itself compute the chip channel can
see, so chip accounting can watch this part of the leak.

**Searches tried.** Track 03's list under A1.

**Label: prior work.** The combined leak survives only as a term of D3's combination.

### A3 Algorithmic progress

**Closest prior work.** Rates of algorithmic progress [@ho2024algorithmic; @erdil2022vision;
@hernandez2020efficiency; @ho2025rosetta; @gundlach2025priceprogress]. Critiques that matter:
measured efficiency depends on scale and on the reference algorithm [@gundlach2025origin] (only part
of their account comes from their own ablations, the rest from a survey estimate), and observational
estimates may carry selection bias [@whitfill2025selection].

**What remains.** Nothing.

**Design consequence.** No single halving time is settled, and no scale-dependent rate either: on
public data E1 identifies neither one multiplier nor a rate that depends on scale
([A3](012-computational.md#a3-algorithmic-progress)). D3 cannot assume either form: its drift term
is unidentified, which is why the claims file cut its interval tabulated in advance (C2(a)), and
whether efficiency depends on scale is left to E15. If the ablations are right, a fixed multiplier
overstates the leak at small scale and understates it for innovations that change the exponent.

**Searches tried.** Track 03's list under A1.

**Label: prior work, and contested.**

### A4 Data

**Closest prior work.** The stock of public text [@villalobos2022data]; repetition under data limits
[@muennighoff2023dataconstrained]; collapse when real data is replaced [@shumailov2024collapse]; no
collapse when data accumulates [@gerstgrasser2024accumulate]; zero-data self-play where an executor
checks answers [@zhao2025absolutezero].

**What remains.** Nothing. Track 03 offers a sharper statement of the memo's split: collapse needs
real data to be replaced, and growth beyond the base needs a verifier.

**Searches tried.** Track 03's list under A1.

**Label: prior work.**

### A5 Search and planning

**Closest prior work.** Superhuman play by self-play and search [@silver2017alphagozero;
@silver2018alphazero], up to formal mathematics [@hubert2026alphaproof]; brittleness of superhuman
systems to adversarial policies [@wang2023adversarialgo]; weak and method-dependent transfer
[@huan2026mathtransfer; @liu2025spiral].

**What remains.** Measuring transfer as a quantity a protocol can threshold. Not found by track 03.

**Searches tried.** Track 03's list under A1.

**Label: prior work.**

### Y1 The loops, written as growth laws

**Closest prior work.**
- [@davidson2025three]: software, chip technology and chip production loops, their time lags and
  room to grow; the loops stack, so a combined explosion can happen when the software loop alone is
  too weak.
- [@davidson2026feedback]: software and hardware loops in an innovation network, with the explosion
  condition.
- [@cunningham2026rsi]: a core research loop plus indirect and direct economic loops, each with
  its elasticities.
- [@besiroglu2024returns] and [@eth2025sie]: the Jones-form idea production function, the growth of
  software as a power of software and research input.
- [@davidson2023compute]: hardware and software in semi-endogenous growth models.
- [@erdil2023explosive] and [@trammell2023growth]: the economic loop (a scalable AI labour force;
  automation of production, including self-replicating machines).
- [@chen2026rsisurvey]: self-improvement loops classified by what is improved and by how closed the
  loop is.
- Components of the acquisitive loop are measured [@black2025replibench; @aisi2025trends;
  @pan2024selfrep], and so are components of the experiential loop [@zweiger2025seal;
  @akyurek2024ttt], but not as growth laws.

**What remains.** The experiential loop (continual learning) and the acquisitive loop (replication
and resource acquisition) written as growth laws in the same form as the others. No track searched
for this, and track 04 gave no judgement on Y1 as a whole.

**Searches tried.** Track 04, for Y1 to Y3, D2 and D3: "Will AI R&D automation cause a software
intelligence explosion" Eth Davidson; Davidson Houlden "How quick and big would a software
intelligence explosion be"; Epoch AI returns to software R&D "r" estimate singularity Erdil
Besiroglu; Davidson "compute-centric framework" takeoff speeds; "Measuring AI R&D automation" arXiv
metrics; "loop gain" recursive self-improvement AI measurement threshold; AI agent improves training
recipe fixed compute successive rounds, "nanoGPT speedrun" automated; "breakout time" AI
superintelligence verification compute arms control; AI 2027 takeoff forecast; the titotal
critique; critiques of Bloom et al.; Anthropic RSP AI R&D threshold; OpenAI Preparedness "AI
Self-improvement"; AISI self-replication trends; 2026 continual learning; and the reference lists of
[@cunningham2026rsi] and [@burtsev2026criticality].

**Label: prior work** for the software, hardware and economic loops. Writing the two further loops
in the same form is at most an extension, and unsearched.

### Y2 Runaway versus saturation

**Closest prior work.** The runaway condition, returns to research above one under full automation
at constant compute, is in [@besiroglu2024returns] and [@eth2025sie], from Jones by way of
[@bloom2020ideas]. The saturation mechanisms are documented: compute complementarity
[@whitfill2025bottlenecks; @ho2025experiments], limits to parallel labour [@trammell2026parallel],
Baumol bottlenecks [@aghion2017ai] and a finite runway [@davidson2025sie; @burtsev2026criticality].

**What remains.** Measurement, not the condition.

**Design consequence.** Measured returns to software straddle one, and a correction for compute
bottlenecks puts the domain estimates below it [@ho2025experiments]. The protocol cannot assume
either regime; it has to measure.

**Searches tried.** Track 04's list under Y1.

**Label: prior work.**

### Y3 Coupling

**Closest prior work.**
- [@davidson2026feedback] proves that two loops, each with diminishing returns, explode jointly if
  and only if the interaction matrix has an eigenvalue above one, and in general when its spectral
  radius exceeds one. This is the memo's Y3, with proof.
- [@cunningham2026rsi] writes the joint condition as a sum of loop channels above one, with each
  channel below one alone.
- [@burtsev2026criticality] proves the same across actors: "Every actor may remain individually
  subcritical while the coupled system becomes supercritical."
- [@davidson2025three] states the coupling qualitatively for software, chip technology and chip
  production.
- The criticality metaphor behind the project's name is prior too: [@yudkowsky2013iem] frames
  intelligence explosion with the neutron multiplication factor, "prompt critical" and "delayed
  neutrons", and [@burtsev2026criticality] uses a reproduction number.
- Level 1 ([C6](verification/l1-prior-art-c1-c6.md#c6)) found the treaty bound's method too: a
  spectral radius certified below one from entrywise bounds is the linear case of the network
  small-gain theorem [@dashkovskiy2007smallgain]; the effort on chosen entries that brings it below
  one is the type and target reproduction numbers [@roberts2003typer; @shuai2013targetr] and link
  removal [@vanmieghem2011spectral]; and a regulator testing a spectral radius against one is in
  [@bardoscia2017pathways].

**What remains.** Track 04 did not find "hold the spectral radius below one" made a treaty bound,
with the edges the protocol cuts named (compute licences on the economic loop, identity checks on the
acquisitive loop, limits on the cross-party transfer of AI research advances on the network edge
Burtsev identifies) and each verified separately. Level 1 found the method in control theory and
epidemic control, so only the application remains: the certificate as a treaty test on AI loops,
and the negative result computed with it on this program's numbers (C6).

**Design consequence.** Burtsev's network result makes the sharing of AI research advances among
parties a coupling edge in its own right. The protocol has to limit cross-party transfer, not only
each party's own loop.

**Searches tried.** Track 04's list under Y1.

**Label: prior work.** The memo implied this was the project's own idea, since the name comes from
it. It is not, and the paper must say that the name borrows a metaphor already used for
intelligence explosion. Level 1 found the treaty rule built on it prior in method as well.

### F1 Kinds of advantage: speed, copies, quality

**Closest prior work.** The typology of speed, collective and quality superintelligence (Bostrom, as
summarised in [@grace2014forms]; speed in [@bostrom1998howlong]). Measured speed and cost ratios of
agents against experts exist [@wijk2024rebench; @patwardhan2025gdpval], and a naive speed gain
shrinks sharply once human review is counted [@patwardhan2025gdpval]. Copy counts were assumed in
the essays that made them famous [@karnofsky2022defeat; @amodei2024grace; @aschenbrenner2024sa], and
forecasts already compute them from compute [@lifland2025timelines]. Computing them from held
compute and memory bandwidth is Pope et al.'s inference bound applied to an inventory [@pope2022],
as [P1](011-physical.md#p1-the-compute-budget) does. Quality against institutions: see D1.

**What remains.** Nothing as a contribution. Track 05 did not find copies measured from held compute
and inference throughput, but the formula follows from a known bound, forecasts already compute
copies from compute, and nothing in the protocol triggers on it, so
[the claims file](04-claims.md#cut-and-why) cuts it as too small. E12 and E20 still measure it, as
an input.

**Searches tried.** Track 05 lists its queries under D1 and bases its F1 to F3 judgements on the same
searches and the sources it opened.

**Label: prior work**, not the memo's "extends": the typology is prior work, copies from held
compute are a known bound applied to an inventory, and quality against institutions is D1's.

### F2 Decisive functions

**Closest prior work.** Expert baselines exist for AI research [@wijk2024rebench;
@starace2025paperbench; @chan2024mlebench], cyber operations [@zhang2024cybench], weapons-relevant
science [@gotting2025vct; @rein2023gpqa], persuasion [@salvi2025persuasion;
@schoenegger2025persuasion; @hackenburg2025levers], strategy and forecasting
[@karger2025forecastbench; @metaculus2026futureeval; @fair2022cicero] and economic production
[@patwardhan2025gdpval; @mazeika2025rli]. The list of clusters overlaps the categories tracked in
[@openai2025preparedness] and [@anthropic2026rsp].

**What remains.** Benchmarking each cluster against an institution rather than an individual. Track
05 found team baselines only from contests: CTF scoreboards and Cybench's team solve times (student
and open contests, not expert organisations), Kaggle leaderboards and forecasting teams. An
institutional baseline exists only as policy text, the RSP's research staff and DeepMind's research
teams, with no published measurement ([F2](014-cognitive.md#f2-the-decisive-functions)). For
persuasion, biology and economic production the baselines are individuals or freelancers.

**Searches tried.** Track 05's list under D1.

**Label: prior work.**

### F3 Narrow versus general

**Closest prior work.** The narrow-general split [@morris2023levels]; [@genewein2026agiasi] rules out
AlphaFold and AlphaGo as superintelligence. Narrow superhuman systems can be cheap
[@brown2019pluribus] and brittle [@wang2023adversarialgo]. [@miotti2025narrowpath] restricts both general
intelligence and AI improving AI, as separate conditions.

**What remains.** Nothing on its own. The line drawn as generality across the decisive functions
joined to a closed loop was not found by track 05, and tracks 03 and 04 did not search for it, but
[the claims file](04-claims.md#cut-and-why) does not keep it: D4's line (C1) replaces it as the
line, and its parts are kept in C10 (generality against an institution) and C11 (closure, with
narrow optimisers inside the loop).

**Design consequence.** [@novikov2025alphaevolve] shows a general model working against automated
evaluators producing narrow superhuman results and speeding up its own training, if only slightly.
Narrow components inside a general system's loop are not harmless by default, which blurs the line
exactly where D2 sits.

**Searches tried.** Track 05's list under D1.

**Label: extends prior work**, merged: what was not found is carried by C10 and C11, not claimed on
its own.

### O1 The supply of inputs

**Closest prior work.** Constraints on scaling from power, chips, data and latency
[@sevilla2024scaling2030]; the growth of AI supercomputers [@pilz2025supercomputers]; chokepoints and
value shares [@khan2020aichips; @khan2021supplychain]; supply concentration
[@varadarajan2024resilience]; per-input counts in public datasets of chip sales, chip owners and
data centres [@epoch2026chipsales; @you2026chipowners; @epoch2025datacentershub].

**What remains.** Nothing of substance. No single source puts every input (capital, chips by stage,
power, talent, data) in one table with supplier count, concentration, growth and visibility side by
side, but compiling one is synthesis.

**Searches tried.** Track 06: "ASML 2025 annual results EUV systems shipped"; "TSMC CoWoS capacity
wafers per month 2025 2026"; "HBM market share 2025 SK hynix Samsung Micron"; "NVIDIA data center AI
accelerator market share 2025"; "hyperscaler capex 2026 guidance"; "LBNL Queued Up 2025 edition";
"gas turbine lead times 2026"; "large power transformer lead time weeks 2025"; "CSET fab
construction time days"; "MacroPolo Global AI Talent Tracker"; "Epoch AI frontier data centers hub";
"China National Energy Administration 2025 installed capacity".

**Label: prior work.** Track 06 called a compiled table an extension in form but "not new in
substance"; this file takes the cautious reading, because a compilation is not a claim.

### O2 Race dynamics

**Closest prior work.** Race models are well developed [@armstrong2016racing; @askell2019cooperation;
@han2020regulate; @stafford2022safety; @emeryxu2024uncertainty;
@hendrycks2025superintelligence; @fudenberg2026cooperating; @buenodemesquita2026agirace].

**What remains.** A race model that includes a verification regime with a stated detection time and
asks how that time changes equilibrium safety. Not found by track 06; E6 builds it as a tool, not a
claim. The candidate it tested, that disclosing compliance rather than rank does not raise risk, is
cut: compliance-only disclosure was riskier than no information in
[100%](numbers.md#e6-o2-compliance-over-none) of E6's [72 cells](numbers.md#e6-o2-cells)
([O2](015-organisational.md#o2-race-dynamics)).

**Design consequence.** The models disagree on whether information about capabilities helps
[@armstrong2016racing; @emeryxu2024uncertainty; @fudenberg2026cooperating], and restricting resources
"may backfire" in some regimes [@buenodemesquita2026agirace]. Sealed declarations raise information,
so their effect on stability has to be modelled, not assumed.

**Searches tried.** Track 06: "Racing to the precipice Armstrong Bostrom Shulman"; "Stafford Trager
Dafoe Safety Not Guaranteed"; "2025 game theory AI race safety paper arXiv race frontier labs safety
investment model compute verification equilibrium"; Crossref lookups for the journal versions.

**Label: prior work**, as the memo said.

### O3 Chokepoints

**Closest prior work.** Compute as "detectable, excludable, and quantifiable", made in a concentrated
supply chain [@sastry2024compute]; firmware snapshots plus supply-chain monitoring
[@shavit2023chinchilla]; chip tracking from fabrication including high-bandwidth memory, production
monitoring and a small cluster limit [@scher2025agreement]; chokepoint analysis [@khan2020aichips];
location verification, notification and whistleblower rewards [@grunewald2025smuggling]; the export
rules that already stand on the lithography, logic, memory and chip stages
[@bis2022advancedcomputing; @bis2023advancedcomputing; @bis2024hbm; @bis2025diffusion]; satellite
detection of data centres by their cooling plant [@epoch2025datacentershub].

**What remains.** (a) Ranking stages by durability, using measured growth rates and evidence of
erosion. (b) Treating denial-induced growth in footprint [@cottier2026horinger] as a detection gain,
quantified against P4's floor. Track 06 did not find either done quantitatively. E23 then tested (a)
and found it unsupported: a ranking made on data public at the end of 2022 orders the erosion of
2023 to 2026 no better than chance (Spearman's r_s [0.28](numbers.md#e23-rho), one-sided p
[0.23](numbers.md#e23-p)). No version of the test can decide: a rank test would need
[85 stages](numbers.md#e23-n-needed), and the 2022 dataset lists
[79 inputs](numbers.md#e23-eto-inputs-2022), nested and correlated, so far fewer independent stages.
(a) is not ours to claim, and the claims file keeps it cut.

**Design consequence.** Chokepoints leak at the edges faster than they erode at the core: diversion
[@juniewicz2026smuggling], a large bank of foreign-made dies despite a listing meant to cut the buyer
off [@patel2025ascend; @allen2025senate], and the controlling state reversing itself
[@bis2025rescission]. Power is a rate limit in some countries but not a global
chokepoint [@shaw2026chinasolar]. The failure list must add diversion through intermediaries and the
chokepoint holder choosing to sell; power belongs among detection channels, not chokepoints.

**Searches tried.** Track 06: "An International Agreement to Prevent the Premature Creation of
Artificial Superintelligence"; "Computing Power and the Governance of AI"; "What does it take to
catch a Chinchilla"; "CNAS countering AI chip smuggling"; "Superintelligence Strategy MAIM"; Federal
Register API lookups for the export rules; "BIS rescinds AI diffusion rule"; "H200 exports to China
approved". On erosion: "Reuters China prototype EUV lithography machine Shenzhen"; "SMIC 5nm Kirin
9030 TechInsights"; "Huawei Ascend roadmap self-developed HBM"; "CXMT HBM3 mass production 2026";
"Kessler testimony Huawei 200,000"; "CSIS analysis Huawei Ascend production 2025 2026"; "Epoch AI
China compute share"; "Epoch Horinger".

**Label: prior work.**

## Definitions

### D1 Superintelligence, the endpoint

**Closest prior work.**
- [@genewein2026agiasi] defines superintelligence against large human-expert collectives, about the
  size of a research field or a large corporation, working with frozen technology; it counts many
  instances as one system and asks for a speed factor. It has no budget or compute matching and no
  test battery.
- [@ngo2023tagi] defines (t,n)-AGI as beating any group of n humans working together for time t: a
  group comparison at matched wall-clock time. No budget matching, no battery.
- [@anthropic2026rsp] sets an operative threshold at substituting for the lab's entire research
  staff at competitive cost, within a stated factor: whole-organisation substitution at matched cost,
  for the AI research cluster. [@gdm-fsf-v3-1-2026] compares with "any team of researchers at
  Google" at "approximately comparable all-inclusive costs".
- [@openai2025preparedness] uses matched wall-clock time at the level of an institution's progress.
  [@wijk2024rebench] compares agents with experts at matched wall-clock budgets.
- [@lifland2025timelines] and [@kokotajlo2025takeoff] count copies, speed and compute share against
  the best human at one company, and against the whole field for superintelligence.
- Other relatives: "as much productive activity as one of today's largest corporations"
  [@openai2023governance]; efficient "relative to every human and human group"
  [@yudkowsky2016superintelligent]; collective superintelligence [@grace2014forms]; copies and speed
  as assumptions [@karnofsky2022defeat; @amodei2024grace; @aschenbrenner2024sa]; "large collections
  of top human experts" [@aguirre2025ktfh]; "substantially surpass humanity in all strategically
  relevant activities" [@barnett2025governance]; a harm-based operational definition with a
  presumption rule [@scher2025agreement].
- Counter-precedents that benchmark against individuals: [@bostrom1998howlong], [@morris2023levels],
  [@hendrycks2025agidef].
- Refreshed held-out batteries are prior work [@white2024livebench; @jain2024livecodebench;
  @karger2025forecastbench; @scale2026hleboard; @kiela2021dynabench], and so are the contamination
  and leaderboard problems they answer [@zhang2024gsm1k; @singh2025leaderboard; @xu2024contamination].
- Level 1 ([C10](verification/l1-prior-art-c7-c12.md#c10)) found the crossover budget prior in two
  forms: RE-Bench reports where the advantage flips [@wijk2024rebench], and a 2026 essay defines the
  intersection of the AI and human curves as a quantity and tracks it across models
  [@robinson2026horizons], the closest relative of D1's crossover budget t*. Cost-controlled agent
  evaluation is in [@kapoor2024agents].

**What remains.** Our search found nothing that (a) matches both wall-clock time and budget (compute
and money) between the system and the human organisation as part of a definition of
superintelligence, (b) runs that comparison on a refreshed held-out battery with published
institutional baselines across several decisive clusters, or (c) uses an alpha fraction of clusters.
The RSP comes closest on (a), for one cluster. Combining refresh with institutional baselines was
not found. Level 1 kept (a) to (c) and one more: t* defined at equal compute and money as the
largest tested crossing, censored and never extrapolated. Tracking a human-AI crossover is not ours.
Level 3 (E21) found t* rising with release date but stopped by each battery's ceiling, and no
battery with an organisation's baseline, so what remains is a definition whose t* lasts only as long
as its battery's baselines (C10).

**Design consequence.** Prior work forces three choices on D1. Say whether the organisation may use
AI; [@genewein2026agiasi] freezes its technology because otherwise the baseline moves. State the time
budget, because verdicts flip with it [@wijk2024rebench; @rein2025hcast]. State which organisation,
because human baselines vary widely with context [@kwa2025horizon]. Team baselines exist for
capture-the-flag scoreboards [@zhang2024cybench], Kaggle [@chan2024mlebench], forecasting
[@metaculus2026futureeval; @forecastbench2026board] and protein structure [@jumper2021alphafold]. The
one live capture-the-flag comparison track 05 relied on [@tang2026ctfcollab] set an agent's separate
scoreboard against mostly undergraduate teams who themselves used AI, so it says nothing about expert
organisations.

**Searches tried.**
- Track 01: "Levels of AGI" definitions; "definition of superintelligence" 2025 2026; "fully automate
  the work of any team of researchers"; RE-Bench human expert time budget; frontier framework AI R&D
  thresholds (METR common elements).
- Track 05: "Richard Ngo t-AGI definition beats most human experts given time t"; "AI Futures Project
  timelines forecast superhuman coder definition 30x agents 30x speed best engineer"; "Bostrom
  Superintelligence chapter 3 speed collective quality definition text"; "definition
  superintelligence outperform human organizations OR all of humanity matched compute cost
  wall-clock time AI benchmark team baseline" (extended); "human team baseline AI evaluation matched
  budget wall-clock comparison organisation-level AI capability definition 2025 2026 arXiv"
  (extended); "organizational superintelligence OR superintelligence relative to organizations
  benchmark"; "Karnofsky AI could defeat all of us combined copies"; "Arbital superintelligent
  relative efficiency epistemically efficient relative to humanity"; "OpenAI Preparedness Framework
  version 2 AI self-improvement critical wall-clock"; "Anthropic Responsible Scaling Policy AI R&D-4
  entry-level remote-only Researcher"; "AGI or superintelligence definition cost parity OR same cost
  OR matched cost human worker compute copies speed paper 2025 2026" (extended).

**Label: extends prior work**, as the memo said, but narrower than it said. Tracks 01 and 05 agree,
and so does level 1. Both of the memo's stated differences, comparing against organisations and
counting copies and speed, are prior work, and so is the crossover budget as such.

### D2 Loop gain, the approach through self-improvement

**Closest prior work.**
- [@cunningham2026rsi] names the product of elasticities "the loop gain", derives the threshold at
  one, says estimating it, tracking it and extrapolating its crossing "is arguably the most
  important empirical exercise", and calibrates the threshold. Even a reported uplift that they call
  "very likely to be an overestimate" would, taken at face value, fall below it. Their footnote
  notes the loop gain is invariant to the capability normalisation, while a raw ratio of gains is
  not.
- [@burtsev2026criticality] defines a recursive reproduction number with a damped and an amplified
  regime either side of one, includes an operational closure factor, and lists the quantities to
  estimate per development cycle. It gives no estimation procedure.
- [@yudkowsky2013iem] frames returns on cognitive reinvestment as a multiplication factor with
  criticality.
- [@eth2025sie] and [@davidson2025sie] work with returns to software at fixed compute; [@eth2025sie]
  proposes ongoing measurement of software progress disclosed to trusted third parties and a pace
  threshold.
- Rate-of-progress triggers are already in lab policy: [@anthropic2026rsp] triggers on a doubling of
  the rate of progress attributable to automated research, does not count constant or slowing
  progress, and says the threshold "has proven difficult to operationalize";
  [@openai2025preparedness] uses a generation in a fraction of the earlier wall-clock time, sustained
  for months; [@gdm-fsf-v3-1-2026] has an acceleration level.
- Measurement has started: [@metr-anthropic-acceleration-2026] measured an acceleration in a lab's
  capability index with a bootstrap interval; [@metr2026expenditure] measures agents' returns to
  spend on an AI research target; [@shetty2026metrnanogpt] measures the speedrun's progress by depth
  and provenance and counts AI-credited records; [@ho2025experiments] calls for controlled
  experiments on returns; [@zhao2025speedrun] is an existing harness for staged runs;
  [@hendrycks2025superintelligence] uses the recursion framing.
- Level 1 ([C4](verification/l1-prior-art-c1-c6.md#c4)) found the trigger rule and the remedies
  prior: acting on whether the upper bound of a reproduction number exceeds one
  [@blumberg2020supercritical]; estimating a subcritical reproduction number from successive
  generations [@blumberg2013stuttering]; the error bias of growth-on-level regressions
  [@freckleton2006census], and independent repeated measurements to remove it
  [@ashenfelter1992twins]; and a staged, fixed-budget test of whether an AI research loop
  accelerates, with held-out scoring [@srikanth2026aide2].

**What remains.** The survey left an estimator that is (i) run as a staged experiment at fixed
compute, (ii) reported with a confidence bound, and (iii) used as a binding trigger; D2's g, a ratio
of successive gains with human-held inputs fixed, differs from the industry triggers and the METR
estimate, which are ratios of overall progress rates with inputs free, and Burtsev defines the
critical quantity without a way to estimate it. Level 1 took (iii) and the remedies: the trigger on
the upper bound (the lower bound this file once named misses loops) is epidemic practice, and two
held-out sets per round are the twins remedy. What remains is the exact round identity for this
growth law, used as the estimator of the loop gain K for an AI research loop staged at fixed inputs,
and the budget ladder that estimates the return to input inside that design. The red team then found
that at the only data-calibrated noise the trigger fires about as often below one as above, and E4's
rerun found every estimator there under-covering and biased toward the unsafe side or useless. So C4
is downgraded to a measurement design: the identity is proved, and the estimator fails level 3 until
a staged run measures real rounds
([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)).

**Design consequence.**
- Units. The ratio of successive gains equals the compounding condition only on a log
  compute-equivalent axis with rounds of equal resource budget. On a bounded benchmark, successive
  gains shrink near the ceiling whatever the feedback.
- Baseline progress. Fast progress can be subcritical and early supercritical progress can look
  ordinary: rapid growth is "neither necessary nor sufficient evidence of recursive criticality"
  [@burtsev2026criticality]. A trigger on a capability slope, as in the lab rate triggers, does not
  identify the regime.
- Inputs. Holding human inputs fixed is counterfactual, since in practice they grow fast, so a
  measured return must be deflated by input growth [@cunningham2026rsi]. Rounds shorter than the lag
  from idea to capability misstate returns [@alston2022ideas].
- Sandbagging. An agent running the staged test could underperform on purpose
  [@gasteiger2025subtlesandbag], which biases g downward. Track 10 says to use elicited agents and
  report g as a lower bound. A trigger at the lower confidence bound of a quantity that is itself
  biased low fires late, which is why the rule moved to the upper bound (C4). E4 then found that a
  uniform shortfall moves only the intercept, while withholding in the pattern that most delays the
  trigger keeps it silent in [96%](numbers.md#e4-late-ub-hide25-fav) of runs even on favourable
  rounds.
- The speedrun series is human-driven, mixes systems engineering with algorithms and is very uneven,
  and the AI-credited records so far are shallow [@shetty2026metrnanogpt]. E4 found its r not
  identified: stock and input move together, and placebo inputs give values of r either side of 1.
- This file does not use the figure track 04 called Cunningham et al.'s "rough estimate": the
  spot-check found it is an upper-end illustration from a self-report the authors distrust.

**Searches tried.**
- Track 01: "returns to software R&D" r > 1 threshold governance; recursive self-improvement trigger
  metric; "loop gain" AI R&D trigger; automated AI R&D thresholds across frameworks; NanoGPT speedrun
  agents benchmark.
- Track 03: its list under A1, in particular the speedrun record query.
- Track 04: its list under Y1.
- Track 05: the framework queries in its list under D1.
- Track 10: did not search in depth; it found no prior work applying sandbagging analysis to
  loop-gain estimation.

**Label: extends prior work, narrowly, for the estimator only.** Track 01 calls the condition and
its use as a trigger prior work; track 03 calls the speedrun estimate partly prior work; track 04
calls D2 an extension, "less than the memo believed". The cautious reading is that the condition,
the name, the trigger and the measurement agenda are all prior, and only a confidence-bounded,
rerunnable, staged estimator may be ours. Level 1 narrowed that to the round identity and the budget
ladder, and level 3 left them a measurement design, not yet a contribution.

### D3 Breakout time

**Closest prior work.**
- [@miotti2025narrowpath] sizes cluster caps from the time an illegal run would take.
- [@fithian2026hardwired] derives breakout fleet thresholds from training budget, research overhead,
  utilisation, horizon and a rate of efficiency growth.
- [@barnett2025governance] defines breakout time and notes that if AI can automate AI research,
  breakout "may be very short, even given limited compute".
- [@scher2025agreement] uses breakout qualitatively, with no numeric breakout or detection time.
- [@gan2026clock] computes a catch-up time from a calibrated takeoff model, and shows it falling at a
  fixed declared position as compute grows: the dynamic the memo lists as a failure.
- [@davidson2025sie] and [@kokotajlo2025takeoff] compute takeoff durations at fixed compute from
  assumed parameters; [@whitfill2025horizon] links horizon growth to compute growth (in a model that
  rules out a software-only singularity by assumption).
- The nuclear concepts: enrichment as the determinant of breakout, with training as its analogue
  [@sastry2024compute]; conversion time under best-case assumptions [@iaea-glossary-2022].
- "Effective compute" as physical compute times algorithmic efficiency is prior work
  [@ho2024algorithmic].
- Level 1 ([C2](verification/l1-prior-art-c1-c6.md#c2)) found every term of the expression prior:
  fleet accounting with research overhead, utilisation, an inference multiple and an uncertainty
  allowance [@fithian2026hardwired]; a breakout-type time with a feedback term [@gan2026clock];
  additive accounting of fine-tuning, extra inference and distillation against a threshold
  [@pistillo2025loopholes]; the span set by cheap verification [@villalobos2023tradeoff]; scale
  dependence [@gundlach2025origin]; and the leak as the inverse of the access effect
  [@pilz2023efficiency]. An essay on AI breakout time sets a per-entity cap from a target breakout
  time, with no formula [@williams2026breakout].

**What remains.** A breakout time computed from a party's verified holdings (chips, weights, data,
research labour human and AI) that includes a measured loop-gain term alongside physical compute and
measured algorithmic efficiency, reported with an interval (the survey's reading, before levels 1
and 3). Not found by tracks 01, 03, 04 or 08. Level 1 calls it a combination: one expression
evaluated per path, with a two-point interval over every input but C*, a loop-gain term measured
once C4's estimator passes level 3 (it fails today), and the split between leaks a chip count sees
and leaks it does not. Level 3 then cut the interval tabulated in advance: E1 finds the drift rate
not identified on public data, from [2.6](numbers.md#e1-algo-annual-subset-min) to
[1,512](numbers.md#e1-algo-annual-subset-max) a year across samples, so the expression stays as an
accounting frame credited to prior work. Whether it added anything rested on two claims, that it
differs from a single-multiplier breakout time by more than either's interval and that it backtests.
The backtest cannot be run as stated, since its target, the open-closed lag, has no day on which
both sides have a public compute estimate, and the substitute E18 ran is against it, so it is cut:
the leak comes in jumps that no constant rate follows, after a follower's delay the expression
lacks. And it separates from one multiplier only at headrooms where a cap already fails the line,
arithmetic on Part I's ranges. So C2 is downgraded to an accounting frame and claims nothing
([C2](04-claims.md#c2-breakout-time-from-verified-holdings-and-the-cap-leak-as-its-fixed-compute-case)).

**Design consequence.** Efficiency may depend on scale and on the reference algorithm
[@gundlach2025origin], but public data identifies neither a single multiplier nor a scale-dependent
rate (E1), so D3 assumes neither and leaves scale to E15. A breakout attempt needs high reliability,
so the relevant horizon is a high-success one, which lags the median horizon [@ord2025halflife]. And
D3, not D5, must account for what the holder could elicit from its own models with everything it
holds (track 10).

**Searches tried.**
- Track 01: "breakout time" AI compute governance detection response; AI breakout time treaty
  verification; IAEA conversion time AI analogy.
- Track 04: its list under Y1, in particular "breakout time" AI superintelligence verification
  compute arms control.
- Track 08: `"breakout time" artificial intelligence superintelligence detection "timeliness" IAEA
  analogy compute governance` (extended); `AI governance "timely detection" "significant quantity"
  compute analog nuclear safeguards training run detection time conversion time` (extended);
  `"Mechanisms to Verify International Agreements About AI Development" MIRI 2025 arXiv`; `MIRI
  technical governance team 2025 "international agreement" prevent premature superintelligence`;
  `acquisition path analysis "detection probability" combined multiple safeguards measures`; direct
  reads of the papers named in the brief. One relevant RAND perspective blocked automated access and
  was not opened.

**Label: extends prior work, as a combination.** Track 08 called the concept and its computation
from a model prior work, and the holdings-plus-loop-gain version at most an extension; tracks 01, 03
and 04 called it an extension. Level 1 found each term prior and the combination not found.

### D4 Weapons-grade, the line

**Closest prior work.**
- [@barnett2025governance]: in their Threat of Sabotage regime, "nations must be able to detect and
  respond to dangerous AI development faster than any single country's breakout time". This is the
  inequality, stated qualitatively.
- [@gan2026clock] formalises it, with detection delay and implementation delay separated and a
  response standard that depends on the date, and shows that a fixed response standard fails as
  catch-up time falls.
- [@miotti2025narrowpath] sizes thresholds so that breakout gives authorities "ample time to
  intervene". [@fithian2026hardwired] chooses its breakout horizon as the time before "the rest of
  the world could react" and derives fleet thresholds from it.
- [@meta-ssf-v2-1-2026] names development that outpaces evaluation as a loss-of-control outcome;
  [@gdm-fsf-v3-1-2026] ties its buffer to the rate of progress; [@openai2023governance] proposes a
  threshold separating regulated efforts, by analogy with the IAEA;
  [@hendrycks2025superintelligence] asks for detection and sabotage before a bid for dominance
  completes; [@shavit2023chinchilla] sets an explicit detection target within a window.
- In nuclear safeguards, detection time "should correspond approximately to estimated conversion
  times" [@iaea-glossary-2001]; [@canty2001timely] formalises a critical time.
- Level 1 ([C1](verification/l1-prior-art-c1-c6.md#c1)) found the inequality decades older than
  the AI papers. Sandia's timely-detection condition for the physical protection of nuclear sites is
  evaluated per adversary path and judged at the weakest path, with a response time built from
  measured parts at a high quantile and a time margin, using EASI from 1977 [@snell2007itc20].
  Nitze's 1988 standard asks that verification detect a violation in time to respond
  [@hafemeister2008ctbt]. Time-based security in cyber defence [@farhang2017tbs] and the
  process-safety rule for response times [@dearden2022sif] state the same inequality.
  [@fithian2026hardwired] applies it per route with an uncertainty allowance.

**What remains.** The survey left four things not found by tracks 01, 08 or 09: (i) the inequality
used as the definition of the line between useful AI and the path to superintelligence, applied to
systems and holdings; (ii) an explicit margin m; (iii) a response time T_r derived from the regime's
own measured channels and response latency rather than chosen; (iv) a breakout time that includes
loop gain. Level 1 took most of them. (i) is an application of the inequality; (iii) is practice in
physical protection and outbreak response, and in AI the red team found it cannot yet be done; (iv)
belongs to D3. Only (ii) survived level 1 in a precise form: a margin m covers an error e_b in the
breakout time and e_r in the response time whenever e_b * e_r <= m, for any continuous detection
hazard. It is one line of algebra, and level 6 found it where level 1 pointed: it is the
partial-factor format of structural design, where a factor on the load and one on the resistance
multiply into the overall margin [@jrc2008eurocodes]. Nothing of D4 remains ours but the
application. The paper should credit physical protection, Nitze, Barnett and Scher, A Narrow Path,
the hardwired-pause group and Gan.

**Design consequence.**
- On the glossary's own figures the nuclear margin is about one, and below one for metal
  [@iaea-glossary-2001]. In safeguards a margin above one has no precedent. Physical protection does
  use a time margin (Sandia's condition, credited above), but against a site's guard force, not a
  treaty's response, so a margin above one for a treaty must be argued for on its own terms.
- Safeguards timeliness counts detection only, never response, and has been criticised for leaving
  insufficient time to respond [@cochran-2005]. Physical protection does count response, against a
  site's guard force [@snell2007itc20], a response of another kind; for a treaty's response, the
  arms-control record (E24) is the only measure.
- A line set for deterrence is far weaker than one set for prevention: in Gan's illustrative
  calibration, deterrence holds with well under even odds of detection inside the window
  [@gan2026clock]. D4 must say which it is.
- A known threshold turns a dilemma into coordination, while an uncertain one does not
  [@barrett2012climate]; a disputed breakout estimate acts like an uncertain threshold.

**Searches tried.**
- Track 01: "breakout time" AI governance detection response time; AI governance IAEA safeguards
  analogy timely detection conversion time; "weapons-grade" AI threshold useful AI line; detection
  time versus development time AI regulation; escalation criteria AI incident response.
- Track 08: its list under D3, with each AI paper also searched in full text for "breakout",
  "timeliness", "timely" and "detection probability".
- Track 09: its searches under the coalition threshold below, with text searches of
  [@fithian2026hardwired] and [@koopmanschap2026gpu] for "coalition", "breakout" and "withdraw".

**Label: prior work.** This is the largest downgrade from the memo. Tracks 01, 08 and 09
independently found the inequality and threshold design built around it in AI work from the two
years before this survey; level 1 found it in nuclear physical protection from 1977 and in
arms-control verification from 1988. D4 is an application; its small lemma is the partial-factor
format of structural design (level 6).

### D5 Elicited capability, robust to hiding

**Closest prior work.**
- Thresholds judged on elicited rather than observed capability: [@anthropic2023rsp],
  [@openai2025preparedness] (elicitation as a lower bound, with a conservative upper bound for
  sandbagging), [@eu2025gpaicode] (at least state-of-the-art elicitation, matched to misuse actors,
  guarding against sandbagging, with no budget and no miss rate), [@metr2024elicitation],
  [@vanderweij2024sandbagging], [@wallace2025worstcase] (thresholds checked after malicious
  fine-tuning) and [@dominguezolmedo2024testtask] (scoring after a common fine-tuning budget).
- A fixed, stated budget: [@anthropic2023rsp] fixed the elicitation budget as a small share of
  training cost, with a buffer; [@anthropic2026rsp] records that it was removed because "specific
  methodologies may become outdated".
- When supervised elicitation can be trusted: [@hubinger2023trusteval], [@clymer2024safetycases],
  [@clymer2025elicitationbound].
- Validating elicitation on locked or sandbagging model organisms: [@greenblatt2024password],
  [@hofstatter2025elicitationgame], [@taylor2025auditinggames], [@jang2026explorationhacking],
  [@finke2026robustorganisms]. One-sided statistical tests for absence: [@bukkapatnam2026absent];
  the limits of evaluations: [@barnett2024evaluations].
- Level 1 ([C5](verification/l1-prior-art-c1-c6.md#c5)) adds that the statistics are
  diagnostic-test practice [@fda2007diagnostic] and evaluation after a defence is fixed is security
  practice [@carlini2019evaluating; @tramer2020adaptive]; it found rates with intervals per
  elicitation method [@abubaker2026fuzzing] and organisms built to evade audits
  [@duddu2026deceptive].

**What remains.** A stated, measured miss rate and false-alarm rate for a named elicitation budget,
measured over a population of organisms that includes hardened and adaptive ones, used as the
pass-fail rule of a threshold; and its use as a trigger in a regime that trusts no single party. The
nearest work declines to give a number: the auditing game "does not provide quantitative guarantees"
[@taylor2025auditinggames], and [@clymer2025elicitationbound] proposes none. Level 1 agreed. The red
team then limited it: rates measured on organisms blind to the procedure bound only non-adaptive
hiding inside the sampled population, not a developer who sees the procedure. Level 6 judged it an
untested design, not a candidate: E3 has not run, the statistics are textbook, and the population
gap applies at every capability level, not only near D1.

**Design consequence.**
- A budget fixed only as a share of compute ages badly; it has to name methods and be revised as
  elicitation improves.
- Elicitation fails without high-quality demonstrations [@greenblatt2024password], against locks
  trained against RL [@jang2026explorationhacking] and against tamper-resistant locks
  [@finke2026robustorganisms]; circuit-broken locks defeat prompting, steering and grafting
  [@hofstatter2025elicitationgame; @le2026grafting]. Above expert level, demonstrations do not exist,
  so the guarantee is weakest near D1. D5 must state the capability range it covers.
- It assumes no gradient hacking [@hubinger2023trusteval], and unelicitable behaviour can be built
  in principle [@draguns2024unelicitable].
- Detectors tuned on fixed organisms fail against adaptive ones [@soopal2026adaptive]: the miss rate
  must be measured on organisms built after the procedure is fixed.
- Elicitation lifts benign models too [@taylor2025auditinggames], so D5 needs both rates, and the
  false-alarm rate is a cost to useful AI.
- Fine-tuning needs weight access, which outside evaluators often lack [@aisi2025auditingblog]:
  inspectors need weights or a trusted fine-tuning enclave.

**Searches tried.**
- Track 01: password-locked models capability elicitation sandbagging detection regulatory
  threshold; "When Can We Conclude a Dangerous Capability is Absent"; elicitation budget frontier
  framework.
- Track 10: "capability threshold judged on elicited capability fixed elicitation budget fine-tuning
  sandbagging regulation proposal" (extended); "sandbagging detection statistical guarantee miss
  rate elicitation safety case inability argument fine-tuning budget"; "conservative upper bound
  capability evaluation sandbagging fine-tuning elicitation threshold governance proposal 2025
  2026"; "password-locked model resistant to fine-tuning elicitation tamper-resistant sandbagging
  2025 2026 arXiv" (extended); "Anthropic Responsible Scaling Policy 2023 1% of the total training
  cost elicitation post-training"; "EU General-Purpose AI Code of Practice Safety and Security
  chapter model evaluation elicitation sandbagging"; "OpenAI Preparedness Framework version 2
  sandbagging elicitation"; "Google DeepMind Frontier Safety Framework v3 elicitation
  sandbagging"; plus full-text reads of the policy documents.

**Label: extends prior work**, as the memo said. Tracks 01, 05 and 10 agree, and so does level 1.

### D6 Closure

**Closest prior work.** [@burtsev2026criticality] defines operational closure as the fraction of
potential recursive gain that survives the development pipeline, "a property of the development
process, not simply of model autonomy". [@chen2026rsisurvey] classifies self-improvement loops by how
closed they are, from human in the loop to fully closed. [@miotti2025narrowpath] forbids software
produced by optimisation from building or improving such software. [@scher2026research] argues that
every input (compute, algorithms, data) must be held so that progress in one does not undo limits on
another. [@redlines-2025] gives, as an example red line, systems that replicate or significantly
improve themselves without explicit human authorisation. Level 1
([C11](verification/l1-prior-art-c7-c12.md#c11)) found the rule for combining closures, with its
complements and substitutes cases, in the task-based automation model of [@aghion2017ai], applied
here to the inputs of AI research, and the narrow-optimiser rule in A Narrow Path's ban, recast as a
count.

**What remains.** Closure assessed input by input (compute, weights, data, research labour, money)
against verifiable human-held gates. Pipeline transmission alone does not ask whether a gate sits on
each input. After level 1, what remains is that definition and an empirical claim: the gain with any
set of gates is predicted from closures measured one gate at a time. Until an experiment decides
which production function holds, the safe rule gates every highly closed input together, which is
prior work [@scher2026research], so D6 is framing until then.

**Design consequence.** The supporting evidence is that agents fail replication tasks at identity
checks and persistent deployment [@black2025replibench], which are gates a protocol can hold.

**Searches tried.** Track 01: its D2 queries, plus "closed loop" AI governance inputs; operational
closure AI R&D. Track 04: its list under Y1.

**Label: extends prior work, narrowly, and framing until tested.** Track 01 calls it an extension
for research labour and says the per-input list may be framing; track 04 calls it an extension. It
survives only if per-input closure predicts or constrains something the single closure factor does
not.

## The pathway ranking

**Closest prior work.** The candidate pathways themselves are in the literature. A Narrow Path's
conditions include no AIs improving AIs, none capable of breaking out of their environment, no
unbounded AIs, and limits on general intelligence [@miotti2025narrowpath]. Self-replication and
self-improvement without authorisation are named candidate red lines [@redlines-2025].
[@genewein2026agiasi] lists four pathways (scaling, paradigm shifts, multi-agent collectives and
recursive improvement) that overlap the memo's five. The loops behind them are in
[@davidson2025three], and the frontier frameworks already track AI research and autonomy as
categories [@anthropic2026rsp; @openai2025preparedness]. Level 1
([C12](verification/l1-prior-art-c7-c12.md#c12)) found the method older in AI too: comparing paths to
advanced AI by arrival time [@clarke2022mtair] and modelling pathways to superintelligence with fault
trees and interventions [@barrett2016asipath]. Undeclared compute counts as breakout capacity in
[@fithian2026hardwired], distillation and smuggling are named routes [@remler2026distillation], and
[@delaney2026strategicvisions] compares strategic visions. Bostrom's 2014 chapter on paths to
superintelligence was not opened, and a reader should check it.

**What remains.** The ranking itself: these seven routes, loops and supply and transfer routes
together, each tied to a side of the line, a channel and a cost, with ties. Level 1 calls it a
judgement applied with a known method, acquisition path analysis. On the ranking's three criteria
the red team found only [9](numbers.md#claim-c12-pareto-three) of [21](numbers.md#claim-c12-pairs)
pairs Pareto-ordered on its reading, none at the top. With the cost of a limit moved from the rank to
the response, the same reading of the table orders [12](numbers.md#claim-c12-pareto-two), still none
among the first three places. Level 6 found that these grades are our judgements, entered in the
ledger as assumptions, so no pair is fixed by evidence; and the ranking omits theft of weights,
which the pathways chapter leaves unassessed and which state-level actors could carry out
[@nevo2024securing] (C12).

**Design consequence.** The tracks' evidence moves the ranking even where it does not touch novelty.
"Unbounded scaling: not necessary, algorithms substitute" is weakened: most language-model gains
came from compute [@ho2024algorithmic], compute explains most frontier performance differences
[@mertens2026secretsauce], and the largest algorithmic gains need scale to appear
[@gundlach2025origin]. In the frontier-experiments specification, research compute complements
research labour [@whitfill2025bottlenecks]. Algorithms complement compute more than they substitute
for it, so the compute backbone is stronger than the memo assumed. Self-improvement is the loop
closest to closing, but measured AI contributions to frontier-relevant progress are still shallow
[@shetty2026metrnanogpt; @starace2025paperbench]. Self-replication components are rising, with
failures at identity checks and persistence [@black2025replibench; @aisi2025trends]. Continual
learning is not one capability [@harrington2026continual]. Autonomy horizons are growing faster than
first measured [@kwa2025horizon; @metr2026thdata], but high-reliability horizons lag the median
[@ord2025halflife].

**Searches tried.** Track 03's list under A1 and track 04's list under Y1 bear on the ranking; neither
looked for a prior ranking.

**Label: prior work, applied.** The method is acquisition path analysis; the ranking is a judgement
made with it, and C12, which carries it, is downgraded to a judgement (level 6).

## The protocol

### The organising idea: safeguards timeliness

**Closest prior work.** The IAEA analogy for AI governance is in [@openai2023governance]; enrichment
as the determinant of nuclear breakout, with training as its analogue, is in [@sastry2024compute];
the criticality metaphor is in [@yudkowsky2013iem]. Track 04 did not find the safeguards analogy in
its own sources; tracks 01 and 08 did.

**What remains.** Nothing.

**Design consequence.** The memo says safeguards set detection timeliness shorter than conversion
time. They do not: detection time "should correspond approximately to estimated conversion times",
and the timeliness goals sit at or above the conversion times [@iaea-glossary-2001]. Track 08's text
search found no numeric goals in the later glossary [@iaea-glossary-2022]. The memo's opening
paragraph must be corrected, and D4's margin argued without that precedent.

**Searches tried.** Track 01 and track 08 queries under D4 and D3.

**Label: prior work.**

### Registered chips under licences that expire

**Closest prior work.** flexHEG Part I calls a time-limited licence "the only reliable way" to build a
remote off switch, and proposes licences signed by all or a majority of a set of governments
[@petrie2025flexheg1]. Part II specifies periodic licences enforced by a secure clock or cycle
counter, with a lifetime of a few months as its example [@petrie2025flexheg2]. Earlier: offline
licences that disable a chip without an unused licence from a regulator [@petrie2024offline]; a
periodically renewed on-chip licence and a multisignature start switch [@sastry2024compute]; a
security module linking the chip to a periodically renewed licence key [@aarne2024securechips];
renewable offline licences [@kulp2024hem]. A chip registry and compute thresholds are prior work too
[@sastry2024compute; @shavit2023chinchilla; @scher2025agreement; @miotti2023cap; @egan2023kyc]. A
recent survey rates multiparty control "speculative", with "No prototype" [@ansari2026taxonomy].

**What remains.** Nothing.

**Design consequence.** A licence that lapses is a remote off switch, which a leading chip maker
publicly opposes [@nvidia2025nobackdoors], and on-chip verification faces "severe, unsolved hardware
security challenges" [@baker2025verifying]. The registry would also start with a hole, since a large
stock of smuggled chips sits outside any licence [@juniewicz2026smuggling].

**Searches tried.** Track 07: "Flexible Hardware-Enabled Guarantees flexHEG report Petrie 2025
arXiv"; "Kulp RAND Hardware-Enabled Governance Mechanisms 2024"; "AI chip operating license
blockchain OR transparency log OR public ledger compute governance hardware-enabled mechanism"
(extended); "AI governance Bitcoin OR blockchain chip licence renewal multilateral k-of-n threshold
signatures rival states compute treaty" (extended); "block hash freshness license renewal hardware
device Bitcoin trusted time offline expiring license proof-of-work clock" (extended); plus full-text
searches inside the flexHEG, RAND, CNAS, Petrie, Sastry, Baker, Oxford, MIRI, Ansari and Al Ramiah
texts for expir, renew, k of n, quorum, multisig, blockchain, ledger and timestamp.

**Label: prior work.** The protocol must cite flexHEG for the licence itself. The memo called this one
of the protocol's strongest parts; it is strong because others built it.

### Renewal by k of n licensors from rival blocs

**Closest prior work.** flexHEG Part II gives k-of-n multilateral approval of updates "so that no
single actor could unilaterally impose excessive restrictions", with pseudocode
[@petrie2025flexheg2]. Part III makes the approvers major states or blocs, gives updates limited
lifetimes, lets a fraction of approvers extend a lifetime, and analyses the supermajority alternative
[@aarne2025flexheg3]. [@petrie2024offline] already requires several regulators, or a fraction of
them, to sign each licence.

**What remains.** Nothing. The open problems flexHEG names are where any contribution lies (see the
next two ideas).

**Design consequence.** Expiring licences need a deadlock rule. If no update is installed before the
lifetime runs out, every device locks down; an approver that has broken the mechanism on its own
chips could refuse to sign and so disable everyone else's; a major state without a blocking share
could be colluded against; and an approver could secretly sign a second, conflicting extension, which
flexHEG leaves as "a topic for further research" [@aarne2025flexheg3].

**Searches tried.** Track 07's list under the previous idea.

**Label: prior work.**

### Bitcoin block height as the licence clock and freshness

**Closest prior work.** A chip nonce in a signed usage request already stops licences being signed in
advance, in an online setting [@petrie2024offline]. flexHEG Part II uses the presence of a hash in a
public blockchain's history as proof of a delay before a restart, in passing
[@petrie2025flexheg2]. Bitcoin timestamping is established [@gipp2015timestamping;
@todd2016opentimestamps]. Level 1 ([C9](verification/l1-prior-art-c7-c12.md#c9)) found each part
outside compute governance: block hashes as unpredictable public values [@bentov2016beacon]; a height
clock in trusted hardware with a monotone checkpoint [@mouallem2026alerting]; a rate floor on headers
per unit of trusted local time, with its false-positive trade-off, in Tesseract (2019)
[@bentov2019tesseract]; block-height expiry as standard practice [@lightning-bolt2]; and trustless
time from a blockchain for small devices [@regnath2020blockchaintime].

**What remains.** Track 07 did not find, in compute governance, a licence whose freshness comes from a
recent block hash and whose period ends at a block height. Level 1 found every part elsewhere, so
only the assembly for chip licences remains, as engineering. The red team found the compute-budget
bound is the powered-time counter's property, not the height clock's: the height clock adds a
calendar expiry only for chips fed honest headers, and forged headers may stop chips early.

**Design consequence.** The memo lets the chip's own counter end the licence period. flexHEG names the
weakness: with a cycle counter, an operator can leave a chip idle "to save up usage time"
[@petrie2025flexheg2]. A height-based period answers it, but only if the chip can check block
headers, and Bitcoin time is accurate only to hours [@todd2016opentimestamps], which suits licence
periods of weeks to months and nothing shorter.

**Searches tried.** Track 07's list under registered chips, in particular the two Bitcoin and
block-hash queries.

**Label: prior work**, part by part; the assembly for chip licences was not found.

### Sealed declarations

**Closest prior work.** Bitcoin timestamping [@gipp2015timestamping; @todd2016opentimestamps];
append-only logs that cannot show two views without detection [@laurie2013ct]; on-device logs of
model fingerprints with timestamps [@harack2025oxford]; weight-snapshot hashes kept by firmware
[@shavit2023chinchilla]; verifiable pre-commitment to a training seed [@choi2023potd];
blockchain-anchored event logs for AI agents [@bromme2026agentbb]; a blockchain ledger for chip
serial numbers and wafer batches [@alramiah2025pause]; a blockchain hash as a delay proof
[@petrie2025flexheg2]. Level 1 ([C9](verification/l1-prior-art-c7-c12.md#c9)) found the rest: a
Bitcoin-anchored log that cannot equivocate without a double spend is Catena (2017)
[@tomescu2017catena]; "valid only once logged" is certificate transparency [@laurie2013ct] and its
use for hardware [@apple2024pcc]; sealed declarations on a blockchain for arms-control verification
are in a 2020 report [@burford2020trustmachine].

**What remains.** Track 07 found neither (a) training-run declarations anchored in Bitcoin nor (b) a
licence valid only once logged. Level 1 found both elsewhere, so what remains is their assembly in
one log for chips and treaty declarations. It answers two problems flexHEG leaves open, proving that a
licence was not issued [@petrie2025flexheg1] and stopping an approver signing two conflicting
extensions [@aarne2025flexheg3], by carrying over Catena and certificate transparency, not by anything
new. The red team adds that the log's operators must publish every leaf, so they are trusted for
availability.

**Design consequence.** Sealing stops backdating and equivocation, not false declarations. A sealed
log of lies is still a log of lies. Proof of learning is broken in theory [@fang2023polbroken] and
proofs about training data are experimental [@choi2023potd], so what is declared must be checked by
other channels.

**Searches tried.** Track 07: "blockchain timestamp AI training run declarations compute governance
verification Bitcoin anchoring model weights hash" (extended); its queries under registered chips;
full-text searches of Baker, Oxford, Wasil, Scher and Thiergart, and MIRI for blockchain, ledger,
append-only and timestamp.

**Label: prior work**, an assembly of known parts, to be claimed as engineering or not at all.

### Evaluations on elicited capability against the line

**Closest prior work.** Evaluations at checkpoints and before deployment, on elicited capability,
against thresholds, are what the frontier frameworks and the EU code already require
[@anthropic2023rsp; @anthropic2026rsp; @openai2025preparedness; @eu2025gpaicode]. The EU AI Act
already has a notification duty when a compute presumption is met [@eu-ai-act-2024].

**What remains.** Only what D4 (the line) and D5 (stated miss and false-alarm rates) add.

**Design consequence.** Pre-set capability thresholds have proved hard to operate: one lab found them
"far more ambiguous than we anticipated" [@anthropic-rsp-v3-announcement-2026]. Each trigger must come
with its measurement procedure. Evaluation awareness threatens propensity evaluations more than
fine-tuning-based capability evaluations [@needham2025evalaware; @chaudhary2025evalawarescaling],
which supports judging the line on elicited capability.

**Searches tried.** Track 10's list under D5; track 01's framework queries under D1 and D5.

**Label: prior work.**

### Continual-learning updates counted toward compute, with re-evaluation on drift

**Closest prior work.** No track ran a prior-art search for this idea; what follows comes from sources
the tracks opened for other reasons. California's frontier AI law counts later fine-tuning and
modifications in cumulative compute [@fpf-sb53-2025]. The EU counts cumulative training compute for
its presumption [@eu-ai-act-2024] and makes a downstream modifier a provider above a share of the
original training compute [@ec-gpai-guidelines-faq-2025]. One lab's policy changelog records a
re-evaluation cadence set by growth in effective compute or a period of accumulated post-training
enhancements [@anthropic2026rsp].

**What remains.** Re-evaluation triggered by measured drift in elicited capability, for a fleet that
keeps updating its weights after deployment. Not searched.

**Design consequence.** Continual learning "is not one capability" [@harrington2026continual]:
weight updates and scaffolding or context methods need different accounting, and only the first
leaves compute to count. Test-time weight updates [@akyurek2024ttt] and self-edits applied by
fine-tuning [@zweiger2025seal] already work, so update compute has to be metered where it happens.
Reinforcement learning puts most of its compute into rollouts that can run on unregistered hardware
[@primeintellect2025intellect2], so counting update compute at the trainer misses part of it.
Forgetting is a natural brake on a cheap experiential loop [@luo2023forgetting; @zweiger2025seal].

**Searches tried.** None aimed at this idea. Track 04 ran "2026 continual learning"; tracks 01 and 03
opened the compute-counting rules while searching thresholds.

**Label: prior work, provisionally.** Counting updates and re-evaluating on accumulation both exist
in law or lab policy. The drift trigger needs its own search before anything is claimed.

### Bans on closed loops above a loop-gain threshold

**Closest prior work.** A Narrow Path prohibits AIs improving AIs outright, and the direct use of
software produced by optimisation to build or improve such software [@miotti2025narrowpath]. The red
lines call gives systems that replicate or significantly improve themselves without explicit human
authorisation as examples [@redlines-2025]. The MIRI draft agreement restricts research that would
materially advance toward superintelligence or cut the compute it needs [@scher2025agreement]. The
frontier frameworks already set thresholds on automated AI research [@anthropic2026rsp;
@openai2025preparedness; @gdm-fsf-v3-1-2026], and replication is evaluated [@black2025replibench;
@aisi2025trends; @pan2024selfrep].

**What remains.** Only the trigger: a ban that starts at a measured loop gain rather than covering
all AI research. That is D2's estimator, and it has fallen for now: at calibrated noise the trigger
cannot tell a loop below one from one above, so nothing here is ours unless C4 reopens.

**Searches tried.** Track 01's D6 queries ("closed loop" AI governance inputs; operational closure AI
R&D); track 04's "Anthropic RSP AI R&D threshold", "OpenAI Preparedness \"AI Self-improvement\"" and
"AISI self-replication trends".

**Label: prior work.**

### The multi-channel detection guarantee over breakout time

**Closest prior work.**
- [@baker2025verifying] proposes several largely independent verification layers, and argues that a
  regime's detection probability is approximately that of its weakest subgoal, because a rational
  prover goes around it. Stacking layers gives redundancy within a subgoal. Correlation, and
  violations spread across subgoals, are flagged but not modelled.
- [@gan2026clock] uses Poisson detection inside a response window that shrinks as compute grows, a
  deterrence bound and a participation bound on monitoring cost, with one aggregate rate and no
  decomposition into channels.
- [@allison2025nuclear] integrates a Poisson risk over a horizon, calibrated to safeguards targets.
  [@shavit2023chinchilla] gives a closed form for one channel (chip sampling).
  [@wasil2024verification] lists the channels and calls their combination a "Swiss cheese" model,
  qualitatively. [@baker2023nuclear] sets a detection target per layer and notes the IAEA's
  dependence on intelligence tips.
- Acquisition path analysis computes path-level detection probabilities [@allen-2015-llnl;
  @iaea-glossary-2022]; the test-ban record shows independent physical channels watching one event
  [@nrc-2012-ctbt].
- Level 1 ([C3](verification/l1-prior-art-c1-c6.md#c3)) found the structure in physical-protection
  path analysis, EASI from 1977 [@snell2007itc20]: the evader takes the path of least detection,
  detection counts only if early enough for the response, channel values depend on the adversary's
  tactics, and broken elements are modelled per path. The game form is network interdiction
  [@washburn1995interdiction] and safeguards selection [@ward2016safeguards]; per-pathway detection
  with timing is in [@gif2011prppem]; [@burr2012safeguards] flags dependence between measures without
  a rule.

**What remains.** Tracks 07 and 08 did not find a model that (i) gives each channel a sourced
detection rate, (ii) combines redundant channels with an explicit correlation term, (iii) takes the
evader's best path, and (iv) evaluates the miss over the breakout time. Level 1 found (iii) and (iv)
in physical protection and (i) as an application. One elementary rule seemed to remain: channels
that share a cause are merged at the larger rate, safe under any dependence, while the sum holds
only under independence. Level 6 judged it the textbook bound on the probability of a union, which
level 1 had named as Fréchet's bounds of 1935 (not opened by us, so not cited), and treating
channels with a shared cause as one event is the common-cause practice of probabilistic risk
assessment [@mosleh1998nureg5485]. Nothing of it remains ours but the application (C3).

**Design consequence.** Channel miss rates cannot be multiplied. The memo's product holds only when
every channel watches the same path and fails independently. An evader picks the path that beats the
channels on it: chip accounting watches declared chips, power and satellites watch facilities, and
whistleblowers watch people, so smuggled chips in a small undeclared site face only the channels on
that path. Channels that rest on one hardware trust anchor fail together under one break
[@chuang2026teefail] and count as one channel. Inspections follow intelligence tips, so channels are
correlated [@baker2023nuclear]. A mature many-channel oversight system in another field catches only
a minority of frauds [@dyck2017pervasive]. And the realised record for undeclared nuclear programmes
is detection after years, mostly by intelligence, defectors or disclosure, not by the inspectorate's
own channels (track 08; for Iraq, [@thorne-1992; @albright-2002]). The miss probability must be a
maximum over evasion strategies, as in an inspection
game (track 09).

**Searches tried.**
- Track 07: "verification international AI agreement combined probability of detection multiple
  independent methods miss probability breakout time quantitative model" (extended); "Baker 2025
  Verifying International Agreements on AI six layers verification arXiv"; full-text searches of
  Baker, Wasil, Oxford, Scher and Thiergart, MIRI, Gan, and Allison and Herzog for probability,
  independent, redundancy, combined and Swiss.
- Track 08: its list under D3, in particular the acquisition path analysis query.

**Label: prior work.** Track 07 called it an extension; track 08 called the structure prior work and
only the sourced, per-path, evader-minimised version a possible extension. Level 1 found that
version in physical protection, so only the merging rule might have remained, and level 6 found it
textbook.

### Random challenge inspections

**Closest prior work.** The MIRI draft agreement already models its challenge inspections on the
Chemical Weapons Convention [@scher2025agreement]. Short-notice random inspections and complementary
access exist in safeguards [@iaea-glossary-2022; @infcirc-540].

**What remains.** Nothing.

**Design consequence.** No challenge inspection has been requested since the convention entered into
force [@opcw-ec109-dg22], so the channel's realised rate is nil. A challenge inspection is not random:
a state must request it and accuse another. The protocol must either specify genuinely random
inspections, announced as a published probability and drawn from a verifiable randomiser (track 09,
from the inspector-leadership result in [@avenhaus2002inspection]), or price the political trigger.

**Searches tried.** Track 08's list under D3.

**Label: prior work.**

### Rewarded whistleblowing

**Closest prior work.** Whistleblowers are a channel in [@scher2025agreement], [@rahman2025nonparty]
and [@baker2025verifying]. Evidence on effectiveness, and on the role of money, comes from corporate
fraud: rewards, not legal protections, moved insiders [@dyck2007whistle], and award programmes have made
awards at scale [@sec2024whistleblower].

**What remains.** Only a measured detection rate for the channel, transferred from corporate fraud
with stated caveats: a state can compartmentalise and coerce in ways a firm cannot.

**Searches tried.** Track 09's searches, listed under inspection games below.

**Label: prior work.**

### Power and heat signatures

**Closest prior work.** Energy monitoring is a proposed verification method [@wasil2024verification].
On-site power metering detects training against a declared inference workload, on simulated power
[@kimpson2026dcpower], but bounds the amount of hidden compute only weakly [@kimpson2026b]. Orbital
thermal sensing did not see a large cluster's waste heat [@jing2026], while imagery sizes known sites
[@krawec2026].

**What remains.** Nothing.

**Design consequence.** Split the channel in two: on-site metering at declared facilities, useful for
telling workloads apart; and remote heat sensing for discovery, which is weak.

**Searches tried.** Track 02's list under P4.

**Label: prior work.**

### Inspection games for compliance

**Closest prior work.** The inspection-game literature: equilibrium inspection and violation
probabilities, inspector leadership (an inspector who commits to a randomised inspection probability
makes legal behaviour the inspectee's best response), recursive inspections and timeliness
[@avenhaus2002inspection; @vonstengel2016recursive; @maschler1966price; @canty2001timely]. The
statistics of data verification in safeguards are in [@avenhaus1996compliance]. For AI,
[@gan2026clock] solves a pause game with Poisson detection inside a response window and a costed
monitoring bound. Absent a trade-off between transparency and security, deterrence never needs
perfect monitoring [@coe2020arms]. [@fithian2026hardwired] discusses repeated games, and
[@hendrycks2025superintelligence] deterrence by sabotage, informally.

**What remains.** Track 09 found no paper applying the inspection-game line (inspector leadership,
non-detection games, recursive inspections) explicitly to AI compute verification, and calls an
inspection-game treatment with announced random challenge inspections, strategic evasion across
several channels and the end effect of licence renewals a possible extension. Track 08 calls the
whole item prior work.

**Design consequence.**
- Commitment needs a verifiable randomiser [@avenhaus2002inspection]. Track 09 suggests publishing
  the inspection probability and drawing from a public random beacon. Bitcoin's block hashes have
  been analysed as one, with a bound on their entropy and a cost to bias them
  [@bonneau2015bitcoinbeacon; @bentov2016beacon].
- The inspection budget must have no known last period. Once inspections run out the inspectee
  violates, so a licence regime with a known final period unravels from the end
  [@avenhaus2002inspection; @vonstengel2016recursive]. The hardwired-pause paper's unknown end date
  and the memo's renewing licences are the remedy to formalise.
- Against a strategic evader, splitting a plant into many balance areas does not raise detection
  unless it shortens detection time [@avenhaus2002inspection], which bears on training spread across
  many small sites.
- Monitoring that assures compliance also exposes security information, which is why arms control is
  rare [@coe2020arms].

**Searches tried.** Track 08: avenhaus and Gan read under its list for D3. Track 09: `coalition of
states minimum share of compute needed to break out of AI agreement before detection`; `"breakout"
coalition threshold treaty game theory "fraction of" capacity defect "detected" arms control model
blocking coalition`; `"inspection game" artificial intelligence compute verification treaty`;
`game-theoretic model international AI agreement verification defection detection probability compute
2025 arXiv`; `"self-enforcing" OR "coalition-proof" international AI agreement game theory Barrett
participation 2025 2026`; then the related-work sections and reference lists of the AI agreement
papers found.

**Label: prior work.** The tracks disagree and the cautious label is taken. The extension track 09
describes may still be built and claimed, but it is an application of a mature theory.

### The coalition compute threshold

**Closest prior work.** [@fithian2026hardwired] defines per-state breakout and evasion fleet thresholds
over a time horizon chosen by judgement, and mentions per-coalition allowances in a footnote.
[@gan2026clock] is bilateral, with a response window and no coalitions. [@rahman2025nonparty] and
[@scher2025agreement] say the coalition must hold most of the relevant hardware, without deriving it.
[@koopmanschap2026gpu] states a "sufficient capacity" principle without a number. Coalition stability:
coalition-proof equilibrium [@bernheim1987coalition; @ali2019coalitions]; participation in climate
clubs [@nordhaus2015climate; @barrett1994self]. Level 1
([C7](verification/l1-prior-art-c7-c12.md#c7)) found the derivation itself: the share is the
hardwired-pause overt fleet threshold divided by the fleet, with the horizon replaced by m times T_r
[@fithian2026hardwired]; deriving allowed holdings from a breakout target is older
[@whitehouse2015jcpoaparameters]; and the reward condition for reporting is cartel leniency
[@aubert2006leniency].

**What remains.** Track 09 did not find the threshold derived from the regime's own detection and
response time, applied to coalitions with a coalition-proofness condition. After level 1 nothing
independent of D4 remains: the threshold is D4's response time put into the hardwired-pause fleet
threshold. The red team found its coalition-proofness empty for payoffs that value a decisive
advantage, and its overt share a property of one assumed breakout budget (C7).

**Design consequence.** Without sanctions on outsiders, stable coalitions are small
[@nordhaus2015climate]. A protocol that binds only states that join needs a penalty on non-members.

**Searches tried.** Track 09's list under inspection games, plus text searches of
[@koopmanschap2026gpu] and [@fithian2026hardwired] for "coalition", "breakout" and "withdraw".

**Label: prior work.** Track 09 called it an extension; level 1 found each part, so it is an
application of D4.

### Withdrawal notice longer than the response time

**Closest prior work.** The MIRI draft agreement has a fixed notice period, chosen for the time its
assurance tasks need, with chip clusters removed during notice [@scher2025agreement]. Proposals after
the North Korean withdrawal would freeze and safeguard assets during and after notice
[@eu2005nptwithdrawal]. Treaty law discusses temporal opportunism and denunciation bars
[@helfer2005exiting]; exit that costs too much breaks regimes [@rosendorff2001optimal]. Withdrawal
has been used soon after a special inspection request [@iaea-gc37-1084].

**What remains.** A notice length derived from breakout and response times, which track 09 writes as
notice at least m times T_r minus the exiting party's breakout time, together with an asset freeze
during notice. Not found by track 09.

**Design consequence.** Notice alone did not hold: North Korea withdrew its notice a day before it
would take effect, then later revived it, leaving the Security Council a single day [@bunn2005npt].
Notice works only if assets acquired under the regime are frozen or removed during it. Under D4
itself, if every holding is outside the line at the moment of exit, notice is not
needed for detection; it matters for holdings whose breakout time shrank during membership.

**Searches tried.** Track 09: `treaty withdrawal notice period longer than breakout time design
proposal nuclear OR AI "notice period" "breakout"`; an NPT Article X text query; a query for
Koremenos's article on withdrawal clauses (found, not used); readings of the MIRI draft's withdrawal
article, the EU proposals on NPT withdrawal, Bunn, Helfer, Rosendorff and Milner, and the
hardwired-pause paper. Track 08: its list under D3.

**Label: prior work.** Track 08 calls it prior work, track 09 an extension for the derived inequality.
The cautious label is taken; the derived inequality is a small step, not a contribution in its own
right.

## What this leaves as our contribution

Little survives of what the memo hoped, and level 1 took more. No candidate is new. After the survey
the memo's three strongest ideas (D4 with D3, D2, D5) survived only as narrow extensions. After
level 1, D4 is an application of nuclear physical protection, D3 a combination of known terms, which
level 3 then left an accounting frame, and D2 an estimator that the red team failed as a trigger and
E4 failed as a measurement at calibrated noise, leaving a measurement design. Of the protocol parts
the memo called strongest, the compute chokepoint, expiring licences, the height clock and sealed
declarations are prior work, assembled here. Y3, the treaty rule built on it, and the criticality
metaphor behind the project's name are prior work. Level 6, a fresh referee, then found the margin
lemma and the merging rule textbook, the floor's results calculations, the elicitation rates an
untested design and the ranking's ordered pairs our own judgements. That is the finding.

What might have been ours is listed below, each with the claim that carries it in
[the claims file](04-claims.md#summary), where its test and its results so far are recorded. After
level 6 none remains a candidate: each is an application, a design, a definition, framing or a
judgement, and each must still pass L5.

1. **D4's margin as an error budget** (C1(b)): a margin m covers multiplicative errors in the
   breakout and response times whenever e_b * e_r <= m, for any continuous detection hazard. Prior
   work: the partial-factor format of structural design (level 6).
2. **D3 as one per-path expression** (C2), downgraded to an accounting frame: breakout time from
   verified holdings, a combination credited to prior work. Tabulating it in advance is cut, since
   E1 cannot identify the drift rate; the backtest is cut as untestable on public data (E18), and
   its gain over one multiplier shows only where a cap already fails the line. No longer a
   candidate.
3. **D2's estimator** (C4), downgraded to a measurement design: the exact round identity as the
   estimator of the loop gain for a staged AI research loop, and the budget ladder. The identity is
   proved, but at the only data-calibrated noise every estimator tried under-covers and is biased
   toward the unsafe side or useless, and the trigger built on it is cut. No longer a candidate, it
   reopens only if a staged run (E4(b)) measures rounds far tighter than the calibrated ones.
4. **D5's rates** (C5): miss and false-alarm rates per named budget over a defined population of
   organisms, as the rule of a trigger rival parties run. It bounds only non-adaptive hiding, and it
   is an untested design until E3 runs (level 6).
5. **The merging rule** (C3): channels that share a cause merged at the larger rate. Prior work:
   the textbook bound on a union, with common-cause practice in risk assessment (level 6).
6. **P4's floor as a bound** (C8): at the lowest precision and full utilisation, with each channel's
   margin and the year it crosses one. An application with calculations: the bound cannot fail and
   the pool is assumed (level 6).
7. **D1's combination** (C10): time and money matched together against an organisation, the alpha
   fraction and a censored crossover budget. A definition only, and E21 finds t* stopped by each
   battery's ceiling.
8. **D6 by input** (C11): closure measured one gate at a time, predicting the gain under any set of
   gates. Framing until an experiment shows it.
9. **The pathway order** (C12), downgraded to a judgement: [12](numbers.md#claim-c12-pareto-two)
   pairs Pareto-ordered under our grades, which are judgements too, and none among the first three
   places; theft of weights is not ranked.
10. **Applications, not contributions:** the coupled-gain certificate as a treaty test (C6), the
    coalition threshold (C7), and the height-clocked licence valid only once logged (C9).
11. **Cut or not searched:** F1's copies from held compute, F3's line as generality joined to
    closure (merged into C10 and C11) and a race model with T_r inside it were cut, merged or
    deferred in the claims file. The drift trigger for continually learning fleets, and the
    experiential and acquisitive loops written as growth laws, were never searched; nothing about
    them may be claimed until a track searches for them.
