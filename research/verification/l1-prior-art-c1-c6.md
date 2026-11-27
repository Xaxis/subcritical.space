# Level 1: prior art for C1 to C6

This is the level 1 check of [the claims file](../04-claims.md) for C1 to C6: a prior-art search by a
helper that did not propose the claims and had not read the work before. It was run on 2026-11-27.
For each claim it starts from the statement, the "Prior work, and what differs" paragraph, the
**L1.** plan and the entries in [the novelty file](../03-novelty.md). It does not repeat the
searches listed there. It searches the fields where each idea could already exist under another
name: physical protection of nuclear sites, safeguards and proliferation resistance, arms-control
verification standards, cyber defence, process safety, outbreak response, network interdiction,
control theory, epidemiology, financial stability, econometrics and population ecology.

**How the search was run.** Every search below was run on 2026-11-27. "Web" means the agent's web
search tool, in its standard mode unless marked "extended". "arXiv API" means the export.arxiv.org
query interface; the query is given as the boolean expression sent, decoded from URL form.
"OpenAlex" means the api.openalex.org works search, which matches titles, abstracts and some full
text. "Crossref" and "PubMed" mean their public APIs, used to find and check identifiers and to
read abstracts. "S2 citations" means the Semantic Scholar API's list of papers citing a given
paper (forward citations). The Semantic Scholar relevance search refused most requests with HTTP
429 (rate limit), and its forward-citation endpoint worked only some of the time; each refusal is
recorded. Google Scholar redirected the one automated request tried (`"breakout time" "response
time" artificial intelligence verification`) to a bot check, so no Scholar result was read. SSRN
pages could not be fetched. Each work cited below was opened, and the passage relied on is quoted
with its section or page. A work found but not opened is named as such and not cited. Full texts
were read either as PDF text or through a fetch that quoted the page; where only an abstract was
reachable, that is said.

"Not found" below is a statement about these searches, not about the world.

## C1

**The claim in one line.** A holding is weapons-grade if on some path p, T_b(p) < m * (T_d(p) +
T_resp(p)); claimed are (a) this per-path inequality as the line between useful AI and the path to
superintelligence, (b) the margin m as an error budget, safe whenever e_b * e_r <= m for any
continuous detection hazard, (c) T_r computed from sourced channel rates and drilled latencies, and
(d) prevention near the threshold, deterrence far from it.

**What the authors already searched.** Tracks 01, 08 and 09 searched "breakout time" with AI
governance, IAEA timeliness and conversion time, and full texts of the AI papers (novelty file, D3
and D4). They found [@barnett2025governance], [@gan2026clock], Miotti et al.'s "A Narrow Path" (2025) and
[@fithian2026hardwired]. I searched outside AI for the same inequality: an attacker's time must
exceed the defender's time to detect plus the time to respond.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | Web | `"time based security" Schwartau "P > D + R" protection detection reaction` | Schwartau's model; arXiv 1706.00302 (opened) |
| 2 | Web | `Nitze "effective verification" detect violation "in time to respond effectively" militarily significant` | secondary quotations of Nitze's 1988 standard; Hafemeister 2008 (opened) |
| 3 | Web | `EASI "estimate of adversary sequence interruption" response force time critical detection point probability of interruption` | Sandia and INMM sources; SAND2007-5502P and an INMM 2023 paper (opened) |
| 4 | Web | `PR&PP evaluation methodology "proliferation time" "detection probability" pathway measures Generation IV International Forum` | GIF PR&PP methodology, revision 6 (opened) |
| 5 | Web (extended) | `RAND "breakout time" artificial intelligence detection response nonproliferation analogy perspective` | RAND PE-A3652-1 (landing page opened; no breakout, timing or margin terms; PDF blocked) |
| 6 | Web (extended) | `AI governance "breakout time" "detection time" "response time" inequality compute threshold verification regime 2026` | nothing closer than the AI papers already credited |
| 7 | Web | `CrowdStrike "1-10-60" rule "breakout time" detect investigate remediate defenders must` | CrowdStrike breakout-time post (opened) |
| 8 | Web | `Frieden "7-1-7" target detection notification response timeliness metric pandemics Lancet` | Frieden et al. 2021 (opened) |
| 9 | Web | `Doorn Hansson "Should probabilistic design replace safety factors" partial safety factors uncertainty load strength` | abstract-level hits only; not opened |
| 10 | Web | `"safety factor" "detection time" "conversion time" safeguards timeliness margin multiplicative uncertainty response` | process-safety and accelerator timing margins; nothing from safeguards |
| 11 | Web | `"process safety time" IEC 61511 safety instrumented function response time "half" of process safety time margin definition` | FS-SIG briefing note (opened); IChemE Hazards 26 paper (opened, not cited) |
| 12 | Web | `JCPOA "one year" breakout time rationale "time to detect" and "respond" Einhorn Brookings enough time international community` | Einhorn 2022 (opened) |
| 13 | Web (extended) | `"breakout" "effective compute" chips stockpile time to reach dangerous capability algorithmic efficiency AI pause verification estimate months` | two essays (Williams 2026 opened and cited; a second essay opened, no comparison with detection) |
| 14 | arXiv API | `abs:"breakout time" AND (abs:AI OR abs:"artificial intelligence")` | 0 results |
| 15 | arXiv API | `abs:"detect and respond" AND abs:AI AND (abs:treaty OR abs:agreement OR abs:governance)` | 1 result, unrelated (2604.03262) |
| 16 | arXiv API | `abs:"response time" AND abs:"compute" AND (abs:treaty OR abs:agreement OR abs:verification) AND abs:AI` | 2 results, unrelated |
| 17 | OpenAlex | `"breakout time" artificial intelligence detection response` | 51 results; checked 2604.23183 (incident escalation; detection latency excluded) |
| 18 | OpenAlex | `timeliness detection goal conversion time safety factor safeguards` | nothing on a margin |
| 19 | OpenAlex | `outbreak detection delay doubling time response window containment before threshold` | Pellis et al. 2021 (abstract opened) |
| 20 | S2 citations | papers citing [@gan2026clock] | 0 |
| 21 | S2 citations | papers citing [@barnett2025governance] | 11; opened 2507.09801 (full text: no breakout, response time or margin), 2608.18357 (abstract: no timing comparison), 2606.28694 (full text: no such terms) |
| 22 | S2 citations | papers citing [@baker2025verifying] | 17; titles screened; 2609.36054 opened (calls for faster institutional response times, no quantity) |
| 23 | S2 citations | papers citing [@wasil2024verification] | 15; titles screened, none on timing |
| 24 | Full text | [@gan2026clock] and [@fithian2026hardwired] searched for margin, response, path, route, allowance, react | passages quoted below |

**Closest works found, each opened.**

1. **Physical protection of nuclear sites: timely detection, per path, with measured response times
   and a time margin** [@snell2007itc20]. This is Sandia's evaluation text for the international
   training course on physical protection. Section 16.2: "For any adversary path the PI is the
   cumulative probability of detection along the path up to and including the Critical Detection
   Point CDP. The CDP is the last PPS detection component along that path for which the response
   force time is less than the remaining adversary task completion time." Section 16.2 also: "The
   overall PPS effectiveness is conservatively defined as the lowest PE for all adversary paths."
   Section 16.3: "the PPS must detect the adversary early enough along the adversary timeline that
   the response force has enough time along its timeline to be able to interrupt the adversary
   before theft or sabotage is completed." Section 16.6: the multi-path tool reports "the Time
   Remaining after Interruption and represents the time margin for the response force." Section
   18.4.1 states the delay condition T_RFT < T_min. Section 18.8.3 builds the response time from
   its parts (alarm communication, assessment, guard communication, preparation, travel,
   deployment) and asks for "a response time taken from site security response plans that the
   response can reliably meet a high percentage of the time (thus it should normally exceed the
   mean or 50th percentile response time)". The chapter 16 summary lists "limited-scope performance
   tests, force-on-force exercises" as evaluation methods, and [@ozkutuk2023multipath] (section 3)
   adds that "The standard deviation of the response force time (RFT) can be estimated at 30% of the
   mean based on tests conducted at SNL". The method goes back to EASI (Bennett, 1977, cited in
   [@ozkutuk2023multipath]; not opened).
   *How it differs.* The adversary's remaining task time plays T_b(p), the response force time
   plays T_resp, and the cumulative detection probability before the critical detection point is
   the chance of detection by T_b(p) - T_resp, which is C1's condition read as a probability. It is
   per path, the system is judged at its weakest path, the response time is a high quantile (C1's
   (1 - beta_2) quantile) built from measured parts, and a margin is reported. What differs is the
   domain (a site against intruders over minutes, not a state's holdings over years), the margin as
   a factor rather than a time remaining, and the use of the inequality to define which holdings
   are allowed.

2. **Proliferation resistance: proliferation time and detection probability per pathway**
   [@gif2011prppem]. Section 2 lists the measures: "Proliferation Time – The minimum time required
   to overcome the multiple barriers to proliferation" and "Detection Probability – The cumulative
   probability of detecting a proliferation segment or pathway". On timing: "the timeframe under
   consideration for the detection should be clearly defined and should take into account the
   duration of the segment and pathway (and should reflect timing assumptions made for the PT
   measure)". On use: "it is generally more valuable to use the measures to identify the most
   vulnerable pathways." *How it differs.* Time and detection are reported side by side per pathway
   and not combined into one inequality; there is no response time and no margin; detection
   probabilities are expert judgements.

3. **Arms-control verification standard.** [@hafemeister2008ctbt] quotes Nitze's definition from
   the INF Treaty hearings: "[I]f the other side moves beyond the limits of the treaty in any
   militarily significant way, we would be able to detect such violation in time to respond
   effectively and thereby deny the other side the benefit of the violation." [@einhorn2022jcpoa]
   (executive summary, page 2) applies it to a breakout time: "a breakout time as short as six months would provide
   sufficient opportunity for the United States to learn of an Iranian breakout attempt and
   intervene decisively to stop it". *How it differs.* This is C1's inequality in words, as the
   United States' treaty standard since 1988, with no rates, no paths and no margin.

4. **Cyber defence: time-based security, with both sides measured.** [@farhang2017tbs] (section 1)
   describes Time-Based Security, "a concept which has been informally introduced by Schwartau in
   1999", combining "protection time (p), detection time (d), and reaction time (r). Protection time
   represents the amount of time the attacker needs to execute her attack successfully." Section 3
   tries "to determine actual values of these parameters in practice" from incident records. The
   inequality form "P > D + R" is attributed to Schwartau in search snippets; his 1998 paper
   (Computers & Security, DOI 10.1016/S0167-4048(98)80100-4) and 1999 book were not opened, so they
   are not cited. Vendor practice compares measured times: [@crowdstrike2018breakout] defines
   breakout time as "the time it takes for an intruder to begin moving laterally outside of the
   initial beachhead", reports "The average breakout time analyzed over the previous year came in at
   one hour and 58 minutes", and asks defenders to "detect an intrusion in under a minute,
   understand it in under 10 minutes, and eject the adversary in under an hour." *How it differs.*
   The same comparison of attacker time with detection plus response, measured from incidents, but
   with no detection probability, no per-path analysis and no margin factor.

5. **Process safety: the response must fit inside the time to hazard, with a factor of two.**
   [@dearden2022sif] (page 1): "The commonly cited 'rule of thumb' for SIF response time (SRT) is
   that it should be less than 50% of the process safety time (PST)." Of "a design margin between
   SRT and PST" it says: "It represents the possible growth in SRT that may be tolerated without the
   PST being exceeded within the mission time for the SIF." *How it differs.* This is T_resp < T_hazard / m with m = 2,
   and a margin read as tolerated error, but the error sits on the response side only; there is no
   detection probability and no product of two error factors.

6. **Outbreak response: detection and response latencies measured and set against growth.**
   [@frieden2021seven] proposes that "every suspected outbreak is identified within 7 days of
   emergence", reported with "initiation of investigation and response efforts within 1 day", and
   "effectively responded to ... within 7 days", and reports measured medians of time to detection
   and to notification from real events in the African region. [@pellis2021doubling] (abstract):
   confirmed cases "doubled on average every 3 days", the impact of distancing "was typically not
   seen until at least 9 days after implementation", and "the combination of fast growth and long
   detection delays explains the struggle in countries' outbreak response". *How it differs.* This
   is C1(c), detection and response latencies measured from records and compared with the growth
   time, but the targets are set by convention, not derived, and there are no paths or margin.

7. **AI, already credited and reread for paths and margins.** [@gan2026clock], section 4.2,
   equation (12): "min{D + ℓ, R(d)} < Tcatch(d; F(d), FB(d)), where the leader's exposure, the shorter
   of its alarm response time and the remaining pause, must be less than the follower's catch-up
   time", with D a detection delay and ℓ an implementation delay. [@fithian2026hardwired] sets a
   separate threshold for each defection route (sections 6.2.2 to 6.2.5: covert evasion, overt
   breakout, private evasion, small-scale evasion), each with its own horizon; section 6.2.3: a
   breakout must succeed "before the rest of the world could react to stop it ... we adopt a breakout
   time horizon of T_B = 2 years"; section 3.2.3: ledgers are "held below the covert evasion fleet
   threshold times a fractional covert evasion allowance α_E < 1 to account for uncertainty".
   [@williams2026breakout] asks for a one-year minimum because it "allows time for somewhat
   sluggish human institutions to react", and, because "The error bars are wide, and I want to be
   confident that the true breakout time will be at least one year", aims for three years: an
   informal margin of three for estimation error. *How they differ.* Per-route treatment and an
   uncertainty allowance already exist in AI (Fithian et al.), with the horizon chosen by judgement,
   not computed from channels and latencies.

**Verdict: prior work.** The core of C1 was first done in the physical protection of nuclear
sites: Sandia's timely-detection condition, evaluated per adversary path, judged at the weakest
path, with a response time built from measured parts at a high quantile, and a time margin (EASI
from 1977; [@snell2007itc20]). The same inequality is the arms-control standard for effective
verification (Nitze, 1988, via [@hafemeister2008ctbt]), the cyber model of time-based security
([@farhang2017tbs]) and the process-safety rule ([@dearden2022sif]); in AI it is in
[@barnett2025governance] in words, in [@gan2026clock] as a formula, and per route with an
uncertainty allowance in [@fithian2026hardwired]. Part by part:

- (a) Prior work. Using the inequality to define the boundary of useful AI is an application of
  it; per path is prior (physical protection, PR&PP, Fithian et al.'s routes).
- (b) A margin for estimation error is prior (Fithian et al.'s allowance, the 50% rule, the time
  remaining after interruption, Williams's factor of three). The precise statement, that a factor
  m covers an error e_b in T_b and e_r in T_r whenever e_b * e_r <= m, for any continuous hazard,
  was not found. It is one line of algebra, and the safety-factor literature of structural
  engineering, not opened here, is the likeliest place it already appears.
- (c) Computing the response time from measured detection and drilled latencies is prior practice
  in physical protection and outbreak response. In AI it has not been done, and E24 says it cannot
  yet be.
- (d) Gan's, as the claim already says.

C1 must be downgraded from "extends prior work" to an application: the timely-detection condition
of physical protection, applied per path to AI holdings, with a multiplicative margin. Only (b)
may stand as an extension, and only as a small lemma.

**Confidence.** High that the inequality, per path, with a margin and measured response times, is
prior work outside AI, and medium on (b). Searches that could overturn the residual: the
structural-reliability literature on partial safety factors for load and resistance (where factors
on the two sides multiply), IAEA papers on combined uncertainty in conversion time and detection
time, and the full text of Schwartau's 1998 paper.

## C2

**The claim in one line.** T_b(H) is the minimum over paths of the earliest t with log10 C_p(t) + J +
S_v + A(t) >= log10 C*, computed from verified holdings, with a loop-gain term in the drift, a
scale-dependent efficiency rate, an inference span set by verifier availability and distillation as
a ceiling, reported with an interval; at fixed compute it gives the cap's leak time t = max(0, (h - J
- S_v) / log10 gamma).

**What the authors already searched.** Tracks 01, 03, 04 and 08 (novelty file, D3 and A2) found
[@fithian2026hardwired], [@gan2026clock], Heim and Koessler's paper on training compute thresholds (2024), [@villalobos2023tradeoff],
[@ord2025govaireport] and [@gundlach2025origin]. I searched for compliance accounting that adds
inference, fine-tuning and distillation to training compute, for time-to-threshold formulas, and
forward citations.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | Web (extended) | `compute threshold leak inference scaling verifier "training compute equivalent" capability reachable below threshold time algorithmic progress governance 2026 paper` | Pistillo and Villalobos 2025 (opened); 2604.04712, 2609.10105, 2503.05705, 2605.29359 (already in the repo's sources) |
| 2 | Web (extended) | `"breakout" "effective compute" chips stockpile time to reach dangerous capability algorithmic efficiency AI pause verification estimate months` | [@williams2026breakout] (no formula); a second essay (opened: chip-stock arithmetic, no breakout formula, no detection) |
| 3 | OpenAlex | `breakout time compute holdings algorithmic progress interval training cap` | 85 results; only [@gan2026clock] relevant |
| 4 | OpenAlex | `compute cap algorithmic efficiency time until threshold capability reached inference compute substitution` | 2,484 results; top hits screened; 2610.33447 (opened, see C4) |
| 5 | arXiv API | `abs:"compute threshold" AND abs:"algorithmic" AND abs:"inference"` | 6 results, all unrelated |
| 6 | S2 citations | papers citing [@pilz2023efficiency] | 24; opened 2506.20530 (full text: no breakout, threshold-lowering formula or distillation term) |
| 7 | S2 citations | papers citing Heim and Koessler 2024 (training compute thresholds) | refused (HTTP 429) |
| 8 | S2 citations | papers citing [@barnett2026closingwindow] | 0 returned |
| 9 | Full text | [@barnett2026closingwindow], [@chan2026explosion], [@pilz2023efficiency], [@fithian2026hardwired], [@gan2026clock] searched for breakout, threshold lowering, inference, verifier, distillation, interval | passages quoted below |
| 10 | Fetch | [@villalobos2023tradeoff], for how the span depends on verification | passage quoted below |

**Closest works found, each opened.**

1. **Fleet thresholds from holdings, by route** [@fithian2026hardwired]. Section 6.2: "F_E(t) =
   ρ_E · C_E(t) / (T_E · U_F)" (research overhead, frontier compute, horizon, standard
   utilisation), with ledgers summed over chip categories per state (section 3.2.3). Inference
   enters as a fixed training multiple (section 6.2.2): "We suggest β_E = 10 as the advantage in
   training FLOPs that would be required to give rough parity with the frozen frontier at inference
   time, using a model of Ord (2025)". Scale dependence is discussed (section 6.3.1): "they
   cautioned that many training efficiency gains were scale-dependent". Uncertainty is handled by
   allowances (see C1). *How it differs.* It fixes a horizon and computes a fleet; C2 fixes a fleet
   and computes a time, which is the same relation inverted. It has no loop-gain term, no span that
   depends on verifiers and no interval.

2. **A breakout-type time with a feedback term, falling as compute grows** [@gan2026clock].
   Section 2: "research at TED-AI is ten times as fast as at the Automated Coder for the same
   compute"; section 4.2: "The calibrated catch-up time falls from 12 months at the start to 8.61
   months after 12 months of compliance and to 5.74 months after 24 months." *How it differs.* The
   time comes from a capability state in a calibrated takeoff model, not from verified chip
   holdings; the feedback is assumed, not measured; no interval; no paths.

3. **Inference, fine-tuning and distillation added to training compute** [@pistillo2025loopholes].
   Page 18, on distillation: the derived model "could be subject to regulatory compliance every
   time the starting 'teacher' model ... is greater than the compute threshold", or "the relevant
   compute thresholds could be lower by a number of times equal to the compute savings." Pages 25 to
   26, on inference: "training compute thresholds should be deemed as crossed if the above the
   compute-optimal inference compute is equal to an increase in training compute that would have
   caused the AI model to cross the training compute threshold", with a worked example adding
   "+3 OOM, equivalent to ~2 OOM in training compute". *How it differs.* This is C2's additive
   log-compute accounting (C + J + S_v) and its distillation ceiling, as a static compliance rule;
   there is no drift and no time.

4. **The span depends on cheap verification** [@villalobos2023tradeoff] (key takeaways): "We expect
   this to happen only for tasks in which solutions can be verified cheaply", and for such tasks
   "it is possible to usefully spend an additional 6 orders of magnitude of compute during
   inference." *How it differs.* Already credited by the authors; it makes the verifier-conditioned
   span prior work, not a difference.

5. **The leak is the access effect inverted** [@pilz2023efficiency] (section 1): "An access effect:
   over time, access to a given level of performance requires less compute investment". The
   fixed-compute leak time is the time for this effect to close a stated headroom.

**Verdict: extends prior work, and less than the claims file says.** Each term of the expression is
prior: accounting from holdings to fleet with research overhead, utilisation, an inference multiple
and an uncertainty allowance [@fithian2026hardwired]; a breakout-type time with a feedback term that
falls as compute grows [@gan2026clock]; additive accounting of fine-tuning, above-optimal inference
and distillation against a training threshold [@pistillo2025loopholes]; the span set by cheap
verification [@villalobos2023tradeoff]; scale dependence [@gundlach2025origin], already discussed in
[@fithian2026hardwired]; and the leak as the inverse of the access effect [@pilz2023efficiency].
The claims file's "what differs" lists "the verifier-conditioned span in the same expression" and
"distillation as a gated ceiling"; both exist as accounting rules and must leave the list. What
remains: one expression evaluated per path from verified holdings, with a two-point interval (from
L2's monotonicity), a measured rather than assumed loop-gain term (from C4), and the split between
leaks a chip count sees and leaks it does not. That is a combination, and its label in the claims
file should be "combination of prior work". Claims (b) and (c) are empirical and untested, and are
the only parts that could add something new.

**Confidence.** Medium. The search that could overturn the residual: the takeoff models the
novelty file names (Davidson and Houlden 2025 on the size of a software intelligence explosion; the AI Futures Project model), which compute times to
capability milestones from compute with AI research feedback and Monte Carlo ranges. I did not open
them in this search. If one computes such a time from a party's chip holdings with an interval,
only the "verified holdings" framing of C2 remains.

## C3

**The claim in one line.** The chance a breakout succeeds is the maximum over the evader's paths of
the chance that no channel watching that path detects before T_b(p) - T_resp; under conditional
independence it is exp(-sum of lambda_c(p) * (T_b(p) - T_resp)); dependent channels merge at the
larger rate; a breakable anchor is a path with rate zero; (b) the memo's product of misses equals
this only if every channel watches every path; (c) on sourced rates, the undeclared path's T_d far
exceeds the declared path's.

**What the authors already searched.** Tracks 07 and 08 (novelty file, multi-channel detection)
found [@baker2025verifying], [@gan2026clock], Allison and Herzog (2025), Shavit (2023),
[@wasil2024verification] and acquisition path analysis [@allen-2015-llnl]. I searched physical
protection, network interdiction, proliferation-resistance methods, safeguards inspection games and
dependence between safeguards measures.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | Web | search 3 of C1 (EASI) | Sandia path analysis (opened) |
| 2 | Web (extended) | `acquisition path analysis "detection probability" safeguards measures dependence correlated combined "not independent" diversion path game theoretic` | LANL paper on correlated safeguards data (opened); Ward and Schneider 2016 (opened); OSTI 1424622 (not opened) |
| 3 | Web | `physical protection path analysis "common cause" OR "correlated" sensor detection probabilities dependence adversary path probability of interruption` | Sandia texts assuming independence; a 1978 path-enumeration report (not opened) |
| 4 | Web | `Avenhaus Krieger acquisition path analysis game theoretic "detection probability" diversion paths safeguards state-level` | the tool returned an error and no results |
| 5 | Web | `Morton Pan Saeger "nuclear smuggling interdiction" smuggler "maximum-reliability path" evasion probability sensors pdf` | Morton, Pan and Saeger 2007 located; no copy could be opened |
| 6 | Crossref | `Washburn Wood two-person zero-sum games for network interdiction`; `Morton Pan Saeger models for nuclear smuggling interdiction`; `Koopman The Theory of Search Target Detection` | identifiers; Washburn and Wood abstract opened via S2; Koopman 1956 closed access, not opened |
| 7 | Web (extended) | `"acquisition path analysis" AI compute OR "artificial intelligence" verification international agreement paths covert cluster smuggled chips` | nothing applying path analysis to AI |
| 8 | arXiv API | `abs:"path analysis" AND abs:AI AND (abs:verification OR abs:compute)` | 2 results, unrelated |
| 9 | arXiv API | `abs:"detection probability" AND abs:"compute" AND (abs:covert OR abs:undeclared OR abs:evasion)` | 4 results, unrelated (covert radio) |
| 10 | arXiv API | `abs:evader AND abs:"AI" AND abs:verification AND abs:channels` | 0 results |
| 11 | OpenAlex | `covert AI training detection probability multiple verification channels evader path` | 573 results; top 10 screened, none closer |
| 12 | Full text | [@koopmanschap2026gpu] searched for weakest, per path, detection probability, independent, correlated, Swiss | one passage, quoted below |

**Closest works found, each opened.**

1. **Physical protection path analysis** [@snell2007itc20]. Section 17.1: "For a specific PPS and a
   specific threat, the most vulnerable path (or the path with least PPS effectiveness) can be
   determined. This path establishes the effectiveness of the total PPS." Section 16.2: the overall
   effectiveness is "the lowest PE for all adversary paths. This is equivalent to the statement that
   a chain is only as strong as its weakest link." Section 18.4.2 combines the sensors on one path
   by "A useful basic statistical relationship governing independent but non-mutually exclusive
   events", the cumulative detection probability being one minus the product of the elements'
   non-detection probabilities. Section 16.6: "The analyst can also choose adversary tactics of
   force, stealth, and deceit that determine which detection and delay values are used in the
   calculation." Section 16.9 considers "defeat methods for sensors, barriers, and communication
   systems" and insiders. [@ozkutuk2023multipath] (abstract): "By eliminating the corresponding
   detection or delay elements of the PPS for the chosen adversary path, the threats from insiders
   were also modeled". *How it differs.* This is C3(a)'s structure: per path, a window set by the
   remaining adversary time less the response time (see C1), channel values that depend on the
   adversary's tactics, the evader's best path setting the system's value, and a broken element
   modelled as a path on which that element detects nothing. It assumes independence and gives no
   rule for dependent channels; the domain is a site, not a state's compute.

2. **Network interdiction** [@washburn1995interdiction] (abstract): "A single evader attempts to
   traverse a path between two nodes in a network while a single interdictor attempts to detect the
   evader by setting up an inspection point along one of the network arcs. ... The evader must
   determine a probabilistic 'path-selection' strategy which minimizes the probability of
   detection". *How it differs.* The evader-minimised detection over paths, as a game, but with one
   inspection point and no timing.

3. **Proliferation resistance, per pathway** [@gif2011prppem]. Table 2.11 aggregates segment
   detection probabilities into a pathway detection probability as one minus the product of the
   segments' non-detection probabilities, "under the hypothesis of the independence of detection
   events"; section 2 asks analysts to "identify the most vulnerable pathways", and to weight
   detection by "the time spent at each segment of the pathway". *How it differs.* Same structure
   for a state's nuclear pathways; independence assumed; no breakout-time window.

4. **Safeguards inspection game over proliferation pathways** [@ward2016safeguards] (abstract): the
   method "couples a simultaneous-play game theoretic solver with a probabilistic model for
   simulating state violation scenarios at a gas centrifuge enrichment plant", and "The simulation
   informs the game theoretic solver by calculating the detection probability for a given
   inspector-proliferator strategy pair"; in the results, "the post-diversion detection time was set
   to thirty days to correspond to the IAEA timeliness goals". *How it differs.* The evader's best
   pathway against the inspectorate, with a timeliness window, at one facility and a fixed window.

5. **Dependence through a shared measurement** [@burr2012safeguards] (page 8): "the ability to
   combine probabilities from multiple sensors depends on the independence or non independence of
   subsystems and issues similar to those in evaluating physical protection systems", and "the same
   dip tubes that measure volume in SM data for each tank are used for the volume measurement for
   NMA." *How it differs.* It names the problem C3's merging rule addresses (two channels resting on
   one measurement are not independent) but gives no rule.

6. **AI, independence assumed** [@koopmanschap2026gpu] (section 5.3.1): "Combining methods that are
   independent of each other raises the detection probability further." Qualitative.

Not opened, so not cited: Morton, Pan and Saeger, "Models for nuclear smuggling interdiction" (IIE
Transactions, 2007, DOI 10.1080/07408170500488956), in which, per the search summary, a smuggler
takes a maximum-reliability path against detectors; Koopman's 1956 search theory (DOI
10.1287/opre.4.5.503), the usual source of the exponential detection law; and Fréchet's 1935 bounds
(DOI 10.4064/fm-25-1-379-387), the usual source of the bound behind the merging rule.

**Verdict: prior work.** C3(a)'s structure was first done in physical protection path analysis
(EASI from 1977, [@snell2007itc20]): the evader takes the path of least detection, detection on a
path counts only if early enough for the response to finish, channel values depend on the
adversary's tactics, and broken elements are modelled per path. The game form is in network
interdiction [@washburn1995interdiction] and safeguards [@ward2016safeguards], and per-pathway
detection with timing in [@gif2011prppem]. (b) follows from judging a system at its weakest path,
stated in [@snell2007itc20] and, for AI, in [@baker2025verifying]. What was not found is the
merging rule as a rule: dependent channels merged at the larger rate, safe under any dependence,
with the sum valid only under independence. It is an elementary bound on the probability of a
union, and the sources above either assume independence or, like [@burr2012safeguards], flag
dependence without a rule. (c) is an empirical result of E5 on sourced rates and is outside what a
prior-art search can confirm or refute; its direction is anticipated in [@koopmanschap2026gpu] and
the novelty file's sources. C3 must be downgraded from "extends prior work" to an application:
physical-protection path analysis applied to AI compute paths, with sourced rates. The merging rule
may be kept as a small extension, and only if L4 and L6 agree it is more than the textbook bound.

**Confidence.** High on the structure. The merging rule could be overturned by the common-cause
failure literature of probabilistic risk assessment (beta-factor models, NUREG/CR-5485) or by IAEA
acquisition path analysis papers on dependent safeguards measures (the search for Avenhaus and
Krieger failed); neither was opened.

## C4

**The claim in one line.** The loop gain K = e * lambda / b is estimated from rounds staged at fixed
inputs, using an exact round identity fitted on two independent held-out measurements, lambda from a
budget ladder, and K as a Bonferroni product or from a closed-loop run; closed-loop research is
restricted while the upper confidence bound on K exceeds a margin K* below 1; (a) the interval's
coverage is calibrated or the rounds needed are stated; (b) real runs place r on one side of 1.

**What the authors already searched.** Tracks 01, 03, 04 and 10 (novelty file, D2) found
[@cunningham2026rsi], [@burtsev2026criticality], Eth and Davidson (2025), the lab rate triggers,
[@metr-anthropic-acceleration-2026], METR's NanoGPT evidence (2026), Ho and Whitfill (2025) and
[@zhao2025speedrun]. I searched forward citations of the speedrun harness, staged self-improvement
experiments of late 2026, observational estimates of the returns parameter, decision rules on the
bounds of a reproduction number, and the errors-in-variables literature.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | S2 citations | papers citing [@zhao2025speedrun] | 17; opened 2609.26457 (AIDE2), 2611.16591, 2610.33624, 2610.27735 |
| 2 | S2 citations | papers citing [@burtsev2026criticality] | 1 (no identifier; not opened) |
| 3 | S2 citations | papers citing [@cunningham2026rsi] | refused (HTTP 429), twice |
| 4 | arXiv API | `abs:"returns to research" AND (abs:AI OR abs:software) AND abs:estimat` | 0 results |
| 5 | arXiv API | `abs:"self-improvement" AND abs:"confidence interval" AND (abs:rate OR abs:gain)` | 1 result, unrelated |
| 6 | arXiv API | `abs:"intelligence explosion" AND (abs:estimate OR abs:measure) AND (abs:experiment OR abs:empirical)` | 1 result, 2507.23181 (already in the repo's sources) |
| 7 | arXiv API | `abs:"loop gain" AND (abs:AI OR abs:"self-improvement")` | 2 results, unrelated |
| 8 | OpenAlex | `estimating returns to AI research software intelligence explosion confidence interval experiment` | 2610.33447 (opened); an SSRN paper on a "governance time-constant" (not reachable) |
| 9 | OpenAlex | `recursive self-improvement measurement rounds fixed compute gain ratio estimate` | 2611.08946 (Flex-RSI, opened) and other RSI systems; none estimates a gain |
| 10 | Web (extended) | `experiment measuring returns to AI research effort fixed compute agents rounds "returns to software" estimate 2026 Epoch OR METR OR Forethought` | two essays (both opened; Imas and Garicano cited; the other only restates the loop-gain product, on point estimates) |
| 11 | Web | `epidemic control decision rule "upper bound" credible interval reproduction number R_t below 1 relax restrictions threshold criterion paper` | Blumberg et al. 2020 (abstract opened) |
| 12 | Web | `Galton-Watson offspring mean estimation generation sizes Harris estimator confidence interval test supercritical subcritical` | estimator literature (not opened; see confidence) |
| 13 | Web | `Freckleton "census error and the detection of density dependence" observation error bias growth rate regression` | Freckleton et al. 2006 (abstract opened) |
| 14 | OpenAlex | titles `Estimates of the Economic Return to Schooling from a New Sample of Twins`; `Split-Sample Instrumental Variables Estimates of the Return to Schooling`; `Inference of R0 and transmission heterogeneity from the size distribution of stuttering chains` | abstracts opened |
| 15 | Fetch | [@metr-anthropic-acceleration-2026], [@besiroglu2024returns] | passages quoted below |

**Closest works found, each opened.**

1. **A staged, fixed-budget experiment on whether an AI research loop accelerates**
   [@srikanth2026aide2]. Section 2: "Each inner-loop agent is evaluated at a fixed budget; therefore,
   improving the optimization capability directly improves the research efficiency of the
   inner-loop agent." Changes are kept that "perform best on hidden evaluations" (abstract).
   Section 3.6, the "ignition test": "For the gains in recursive self-improvement to turn
   diminishing returns into accelerating ones, we hypothesize that the discovered agents must be
   better at driving recursive self-improvement than the agent that discovered them", and "with
   only three seeds per outer-loop agent, we find these results to be inconclusive". *How it
   differs.* The design C4 proposes (rounds at a fixed budget, held-out scoring, a test of
   acceleration) run on a real agent, but with no growth law, no estimate of b, lambda or K, no
   interval and no trigger. [@flexrsi2026] (abstract) is a similar harness: "In each round, an
   executor improves the task solution, which is kept only if it scores higher on held-out
   validation data". Neither estimates a gain.

2. **Judging the regime by the upper bound of a reproduction number** [@blumberg2020supercritical]
   (abstract): "A simple approach is shown for using the number of disease introductions and
   secondary cases to determine whether the upper bound of the reproduction number exceeds the
   critical value of one." [@blumberg2013stuttering] (abstract) estimates a subcritical
   reproduction number from chain sizes by maximum likelihood, with "associated confidence
   intervals" that set "when a statistically significant change" is detectable. *How it differs.*
   C4(c)'s rule (act on whether the upper bound exceeds the critical value) and its estimator's aim
   (a subcritical gain with an interval from successive generations) are epidemic practice. The
   data are offspring counts, not capability gains on a log axis, and there is no margin K* and no
   staging.

3. **The bias C4 found, and its remedy, are known** [@freckleton2006census] (abstract): "tests that
   rely on detecting a negative relationship between log population change and population size are
   biased" when the census carries error, giving spurious density dependence. This is the bias the
   formal file found in the first-order identity: one noisy measurement per round, on both sides of
   the regression, makes the loop look more subcritical (in E4 the median estimate of r was
   [0.53](../numbers.md#e4-diff-bias) of the truth). [@ashenfelter1992twins] (abstract): "Multiple
   measurements of schooling levels were also collected to assess the effect of reporting error",
   finding that "measurement error does bias it downward"; a second, independent measurement is the
   correction. *How it differs.* Only the domain: two independent held-out sets, one for each side,
   is this remedy applied to capability rounds.

4. **Observational estimates of the returns parameter, with uncertainty, against the threshold.**
   [@besiroglu2024returns]: a chess estimate "of about 0.83, with a standard error of 0.15", "just
   shy of the threshold of 1", and elsewhere "our median estimates of r exceed one, but like in
   computer chess this finding is not statistically significant". [@tadepalli2026efficiency]
   (abstract) calibrates the two margins of a software explosion on recent data: "In Monte Carlo
   simulations, an SIE occurs in 49% of draws". [@imas2026explosion] estimates the knowledge
   externality at "a central value of 0.84 ... in a range of about 0.66 to 0.94", and says "nothing
   causal can be inferred". [@metr-anthropic-acceleration-2026] reports a ratio of growth rates with
   a bootstrap 95% interval and says "we do not pay special attention to the thresholds set in the
   RSP". *How they differ.* C4(b)'s question, asked of observational data with inputs free; no
   staging and no trigger.

**Verdict: extends prior work, narrowly, and less than the claims file says.** Prior: acting on
whether the upper bound of a reproduction number exceeds the critical value
[@blumberg2020supercritical]; estimating a subcritical reproduction number with an interval from
successive generations [@blumberg2013stuttering]; the direction of the error bias in growth-on-level
regressions [@freckleton2006census]; independent repeated measurements to remove it
[@ashenfelter1992twins]; a staged, fixed-budget test of whether an AI research loop accelerates,
with held-out scoring [@srikanth2026aide2]; the loop gain as a product of elasticities
[@cunningham2026rsi]; observational estimates against the threshold [@besiroglu2024returns;
@tadepalli2026efficiency]. Not found: the exact round identity for this growth law, its use as the
estimator of K for an AI research loop staged at fixed inputs, and the budget ladder for lambda
inside that design. "The upper bound on K as the binding rule" must leave the claims file's "what
differs": it is epidemic practice applied to AI. L1 does not change L3's finding that (a) failed in
E4.

**Confidence.** Medium. The round identity is elementary algebra on the common form, and could
already exist in discrete-time estimation of the Jones law of motion in the economics of ideas, or
in the Galton-Watson literature on estimating an offspring mean from generation sizes (the Harris
and Lotka-Nagaev estimators, found but not opened). A follow-up to [@srikanth2026aide2] with more
seeds and an estimated gain would overturn the rest.

## C5

**The claim in one line.** A threshold is judged on what a named elicitation protocol E recovers,
each E carrying a measured miss rate and false-alarm rate per named budget, each with a one-sided
bound, over naive, RL-locked, tamper-resistant and adaptive organisms built after E is fixed, stated
only over E's covered range, as a trigger rivals can run.

**What the authors already searched.** Tracks 01 and 10 (novelty file, D5) found the lab policies,
[@greenblatt2024password], [@hofstatter2025elicitationgame], [@taylor2025auditinggames],
Jang et al. on exploration hacking (2026), [@finke2026robustorganisms], Bukkapatnam and Karuturi (2026) and
Clymer (2025). I searched forward citations, papers of 2026 reporting elicitation or
detection rates, and the diagnostic-testing and adversarial-evaluation practice the rule resembles.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | arXiv API | `abs:sandbagging AND (abs:"false positive" OR abs:"false negative" OR abs:"miss rate")` | 2 results: [@taylor2025auditinggames], 2606.24251 (unrelated) |
| 2 | arXiv API | `abs:"model organisms" AND abs:elicitation AND (abs:rate OR abs:guarantee)` | 3 results; 2606.29646 opened |
| 3 | arXiv API | `abs:"password-locked" AND (abs:budget OR abs:"sample efficiency")` | 0 results |
| 4 | S2 citations | papers citing [@taylor2025auditinggames] | 18; opened 2611.20459, 2606.29646, 2611.15568 |
| 5 | S2 citations | papers citing [@finke2026robustorganisms] | refused (HTTP 429) |
| 6 | Web (extended) | `capability elicitation protocol measured miss rate false alarm rate model organisms sandbagging budget statistical guarantee dangerous capability threshold 2026 arXiv` | 2608.29461 (opened, no rates); others already in the repo's sources |
| 7 | Web | `AISI OR "AI Security Institute" sandbagging elicitation red team blue team model organisms detection rate quantitative 2026 results false negatives benign` | only [@taylor2025auditinggames] and its blog posts |
| 8 | arXiv API | `id_list=1902.06705`; `id_list=2002.08347` | adversarial-evaluation abstracts (opened) |
| 9 | Fetch | FDA statistical guidance on diagnostic tests (2007) | passages quoted below |
| 10 | OpenAlex | title `If nothing goes wrong, is everything all right? Interpreting zero numerators` | found, no abstract; not opened, not cited |
| 11 | Full text | [@greenblatt2024password], [@taylor2025auditinggames] searched for sample efficiency, quantitative, guarantees, benign | passages quoted below |

**Closest works found, each opened.**

1. **The nearest AI work declines to give rates** [@taylor2025auditinggames] (section 1): "No
   quantitative guarantees. With only ten model organisms and a single blue team, we cannot estimate
   quantitative detection metrics or provide statistical guarantees." It records both error kinds:
   the blue team "missed a sandbagging model while flagging all three benign models as sandbagging".
   *How it differs.* Both errors observed, no rates; it states the gap C5 proposes to fill.

2. **Elicitation success by budget, on locked organisms** [@greenblatt2024password] (section 1):
   "fine-tuning on a single demonstration is often enough to recover most of" the locked
   performance, and "a few high-quality demonstrations are often sufficient". *How it differs.*
   Success measured as a function of a named budget (number of demonstrations), per organism type,
   with no population miss rate, no bound and no false-alarm rate.

3. **Rates with intervals, per method and budget** [@abubaker2026fuzzing] (appendix): "We report
   per-cell rates with 95% Wilson confidence intervals", across fuzzing methods and hyperparameter
   budgets on six backdoored models; "Elicitation is uneven across each method's hyperparameter
   grid" (abstract). *How it differs.* Rates across samples within each organism, not across a
   population of organisms; six organisms; no pass-fail rule.

4. **Hardened and adaptive organisms** [@duddu2026deceptive] (abstract): organisms "must actively
   anticipate and resist auditing - a gap in prior work that can lead to overestimation of auditing
   effectiveness" (the hyphen replaces a dash in the original), and the paper proposes "two
   optimized against blackbox auditing techniques and one optimized against both blackbox and
   whitebox techniques". *How it differs.* Builds
   the hardest organisms C5 names; gives no population rate for an elicitation budget. It supports
   C5(c)'s stated expectation of failure.

5. **The statistical template: both error rates, with bounds, on the intended population**
   [@fda2007diagnostic]: section 5 recommends reporting measures of diagnostic accuracy and "their
   two-sided 95 percent confidence intervals"; section 7.1 says sensitivity and specificity "provide
   distinct and equally important information, and FDA recommends they be presented together";
   section 3 asks for "subjects/patients from the intended use population". *How it differs.* C5's
   pair of rates with one-sided bounds over a stated range is this practice, applied to elicitation.

6. **Evaluation against attacks built after the defence is fixed** [@carlini2019evaluating];
   [@tramer2020adaptive] (abstract): "Adaptive attacks have (rightfully) become the de facto standard
   for evaluating defenses to adversarial examples", yet "typical adaptive evaluations are
   incomplete". *How it differs.* Established practice in machine-learning security. There the
   attacker knows the defence; C5's organism builders are "blind to it", which is a weaker test.
   This is a point for L4, not a prior-art finding against C5.

**Verdict: extends prior work.** The statistics are diagnostic-test practice
[@fda2007diagnostic], and the counts ([22 organisms](../numbers.md#claim-d5-organisms) with no
misses) are the zero-failure binomial bound, as L2 already says. Evaluation after the defence is
fixed is security practice [@carlini2019evaluating; @tramer2020adaptive]. Per-budget elicitation
success on locked organisms is in [@greenblatt2024password], rates with intervals per method in
[@abubaker2026fuzzing], and hardened organisms in [@finke2026robustorganisms] and
[@duddu2026deceptive]. Not found: a measured miss rate and false-alarm rate per named elicitation
budget, over a population of organism kinds including hardened and adaptive ones, used as the
pass-fail rule of a threshold that rival parties run. [@taylor2025auditinggames] states that this
has not been done. The delta is that application and the definition of the organism population.

**Confidence.** Medium to high for the published literature. An unpublished elicitation-validation
method inside a lab or the UK AI Security Institute, which said it would run more red-blue games,
could already do this; so could a frontier safety framework's technical appendix. Neither was found.

## C6

**The claim in one line.** For a signed gain matrix K over loops and parties with jointly valid
entrywise bounds U >= |K|, rho(K) <= rho(U) <= max row sum of U (and its weighted forms); claimed are
(a) the treaty test "certificate at most rho*" with each edge gated and verified, (b) the smallest set
of edge cuts by exhaustive search, and (c) a negative result: rho(U) is at least its largest diagonal
entry, so with the software loop's own gain at [1.07](../numbers.md#dyn-r-lm-hi-corrected) no set of
edge cuts issues the certificate.

**What the authors already searched.** Track 04 (novelty file, Y3) found [@davidson2026feedback],
[@burtsev2026criticality], [@cunningham2026rsi] and Yudkowsky (2013), and called the bounds
textbook. The claim itself names epidemic control, through the type and target reproduction numbers,
as the likeliest place the certificate already exists. I searched there, in control theory
(small-gain theorems), in network science (spectral-radius reduction by link removal) and in
financial stability.

**Searches tried (all 2026-11-27).**

| # | Engine | Exact query | What it returned |
|---|---|---|---|
| 1 | OpenAlex | titles `An ISS small gain theorem for general networks`; `Extending the type reproduction number to infectious disease control targeting contacts between types`; `Decreasing the spectral radius of a graph by link removals` | identifiers; Van Mieghem et al. abstract |
| 2 | arXiv API | `ti:"small gain theorem for general networks"` | Dashkovskiy, Rüffer and Wirth (abstract opened) |
| 3 | PubMed | `Extending the type reproduction number to infectious disease control targeting contacts between types[ti]`; `new method for estimating the effort required to control an infectious disease[ti]`; `Pathways towards instability in financial networks[ti]` | abstracts opened; Bardoscia et al. full text opened on PMC |
| 4 | OpenAlex | `next generation matrix upper bound reproduction number interval uncertainty spectral radius bound certify below one` | 108 results, top 10 screened, none closer |
| 5 | OpenAlex | `spectral radius policy target regulation coupled feedback loops subcritical certification entrywise bounds` | 0 results |
| 6 | OpenAlex | `"spectral radius" "AI" coupled feedback loops subcritical treaty verification edges` | 0 results |
| 7 | arXiv API | `abs:"spectral radius" AND abs:AI AND (abs:governance OR abs:treaty OR abs:policy)` | 0 results |
| 8 | arXiv API | `abs:"next-generation matrix" AND (abs:AI OR abs:"artificial intelligence")` | 1 result, unrelated (2606.05168, model collapse) |
| 9 | arXiv API | `abs:"small-gain" AND (abs:AI OR abs:"artificial intelligence") AND (abs:governance OR abs:policy OR abs:race)` | 0 results |
| 10 | arXiv API | `abs:"reproduction number" AND abs:"self-improvement"` | 0 results |

**Closest works found, each opened.**

1. **The certificate is the network small-gain theorem** [@dashkovskiy2007smallgain] (abstract):
   "the interconnection gains are described in a nonlinear gain matrix and the small-gain condition
   requires bounds on the image of this gain matrix. The condition may be interpreted as a nonlinear
   generalization of the requirement that the spectral radius of the gain matrix is less than one",
   with "linear gains" among the special cases. *How it differs.* Small-gain theory certifies an
   interconnection from bounds on each subsystem's gain, each established on its own: C6(a)'s
   certificate, for the stability of coupled dynamical systems rather than growth loops between
   parties, and with no treaty.

2. **Targeted control on chosen entries is the type and target reproduction number**
   [@roberts2003typer] (abstract): the method can "estimate the level of control necessary when
   targeting control effort at a subset of host types". [@shuai2013targetr] (abstract): the target
   reproduction number "extends the type reproduction number to allow disease control targeting
   contacts between types". *How it differs.* C6(b)'s question (which entries to cut, and by how
   much, to bring the spectral radius to one) for a known next-generation matrix; it works from the
   matrix, not from bounds, and the target set is chosen rather than searched for the smallest.

3. **The smallest set of cuts is a known hard problem** [@vanmieghem2011spectral] (abstract): "The
   minimization of the spectral radius by removing m links is shown to be an NP-complete problem,
   which suggests considering heuristic strategies", and a greedy rule based on the leading
   eigenvector "is shown to be superior to other strategies in most cases". *How it differs.* L2's
   finding that cutting the largest edge first can need more cuts than the smallest set agrees with
   this; exhaustive search by size is the standard exact method for small matrices.

4. **A regulator's test on the spectral radius, with a diagonal-type sufficient condition**
   [@bardoscia2017pathways]: "it will suffice to check that the largest eigenvalue of [the matrix] is
   smaller than one"; "a sufficient condition for having λmax>1 is that there exist two integers i, k
   such that (Λ^k)ii>1"; "Our results suggest to include the eigenvalue analysis of the leverage
   matrix among the tools to monitor financial stability." *How it differs.* Monitoring of a
   measured matrix, not a certificate from bounds, and no gated edges; with k = 1 the sufficient
   condition is the argument behind C6(c).

No use of a next-generation matrix, a small-gain certificate or a reproduction number as a treaty
test for AI was found (searches 5 to 10).

**Verdict: prior work.** The certificate in (a) is the linear case of the network small-gain
theorem [@dashkovskiy2007smallgain] and of the textbook comparison of a matrix with an entrywise
bound. The control question in (b) is the type and target reproduction numbers [@roberts2003typer;
@shuai2013targetr] and spectral-radius reduction by link removal [@vanmieghem2011spectral]. A
regulator testing a spectral radius against one is in [@bardoscia2017pathways], with the
diagonal-type sufficient condition behind (c). The claim's own refutation condition is met in
substance: epidemic control states the targeted version, and control theory states the certificate.
C6 must be downgraded from "combination of prior work" to an application: the small-gain
certificate used as a treaty test on AI loops, each edge gated and verified. (c) stands as a result
computed within that application on this program's numbers, not as a contribution of method.

**Confidence.** High that the mathematics is prior. Not found, and so possibly still the
program's: the application to AI agreements. Searches that could overturn even that: the
international-relations and AI race literature using reproduction numbers or small-gain arguments to
set agreement terms, and later work by [@burtsev2026criticality]'s author.

## Summary

| Claim | Verdict | Closest work | What must change in the claims file |
|---|---|---|---|
| C1 | prior work | [@snell2007itc20] (timely detection per path, EASI from 1977); [@hafemeister2008ctbt] (Nitze 1988); [@fithian2026hardwired]; [@gan2026clock] | downgrade to an application; only (b), the multiplicative error budget, may stand as a small lemma |
| C2 | extends prior work | [@fithian2026hardwired]; [@gan2026clock]; [@pistillo2025loopholes]; [@villalobos2023tradeoff] | relabel "combination of prior work"; drop the verifier-conditioned span and the distillation ceiling from "what differs"; only (b) and (c) can add something |
| C3 | prior work | [@snell2007itc20]; [@washburn1995interdiction]; [@gif2011prppem]; [@ward2016safeguards] | downgrade to an application; the merging rule is the only candidate extension |
| C4 | extends prior work, narrowly | [@srikanth2026aide2]; [@blumberg2020supercritical]; [@freckleton2006census]; [@ashenfelter1992twins] | drop "the upper bound on K as the binding rule" and the two-held-out-set fix from "what differs"; the round identity and staged design remain |
| C5 | extends prior work | [@taylor2025auditinggames]; [@greenblatt2024password]; [@abubaker2026fuzzing]; [@fda2007diagnostic] | keep the label; credit diagnostic-test practice for the statistics |
| C6 | prior work | [@dashkovskiy2007smallgain]; [@roberts2003typer]; [@shuai2013targetr]; [@vanmieghem2011spectral]; [@bardoscia2017pathways] | downgrade to an application of the small-gain certificate |

## New sources

```toml
[source.snell2007itc20]
type = "report"
title = "ITC-20 Evaluation Section (The Twentieth International Training Course, chapters 16 to 18), SAND2007-5502P"
authors = "Mark K. Snell, Craig R. Tewell (Sandia National Laboratories)"
year = 2007
url = "https://www.osti.gov/servlets/purl/1721450"
opened = "2026-11-27"

[source.ozkutuk2023multipath]
type = "report"
title = "Vulnerability Assessment of a Physical Protection System Design Using a Multi Path Analysis and Moving Critical Detection Points"
authors = "Melih Ozkutuk, Sunil S. Chirayath"
year = 2023
url = "https://resources.inmm.org/sites/default/files/2023-07/finalpaper_121_0509105108.pdf"
opened = "2026-11-27"

[source.gif2011prppem]
type = "report"
title = "Evaluation Methodology for Proliferation Resistance and Physical Protection of Generation IV Nuclear Energy Systems, Revision 6 (GIF/PRPPWG/2011/003)"
authors = "Generation IV International Forum, Proliferation Resistance and Physical Protection Working Group"
year = 2011
url = "https://gif.jaea.go.jp/methodology/prppwg/gif_prppem_rev6_final.pdf"
opened = "2026-11-27"

[source.washburn1995interdiction]
type = "peer-reviewed"
title = "Two-Person Zero-Sum Games for Network Interdiction"
authors = "Alan Washburn, Kevin Wood"
year = 1995
doi = "10.1287/opre.43.2.243"
opened = "2026-11-27"

[source.ward2016safeguards]
type = "peer-reviewed"
title = "A Game Theoretic Approach to Nuclear Safeguards Selection and Optimization"
authors = "Rebecca M. Ward, Erich A. Schneider"
year = 2016
doi = "10.1080/08929882.2016.1127031"
opened = "2026-11-27"

[source.burr2012safeguards]
type = "report"
title = "Strengthened Nuclear Safeguards: A Statistical View in the Context of Combining Process Monitoring and Nuclear Material Accounting Data (LA-UR-12-00374)"
authors = "T. Burr, K. Budlong-Sylvester, S. Demuth, M. Hamada, J. Howell, C. Longo, M. Suzuki"
year = 2012
url = "https://www.osti.gov/servlets/purl/1143979"
opened = "2026-11-27"

[source.farhang2017tbs]
type = "preprint"
title = "When to Invest in Security? Empirical Evidence and a Game-Theoretic Approach for Time-Based Security"
authors = "Sadegh Farhang, Jens Grossklags"
year = 2017
arxiv = "1706.00302"
opened = "2026-11-27"

[source.crowdstrike2018breakout]
type = "vendor"
title = "CrowdStrike on Dark Reading: Why 'Breakout Time' Is Critical to Your Security Strategy"
authors = "CrowdStrike (Michael Busselen; article by Scott Taschler)"
year = 2018
url = "https://www.crowdstrike.com/en-us/blog/crowdstrike-discusses-breakout-time-in-an-article-on-dark-reading/"
opened = "2026-11-27"

[source.dearden2022sif]
type = "report"
title = "Specifying SIF Response Time (FS-SIG Briefing Note)"
authors = "Harvey T. Dearden (Institute of Measurement and Control, Functional Safety Special Interest Group)"
year = 2022
url = "https://www.instmc.org/_userfiles/pages/groupfiles/functional_safety/fssig_bn_sif_response_time.pdf"
opened = "2026-11-27"

[source.hafemeister2008ctbt]
type = "essay"
title = "The Comprehensive Test Ban Treaty: Effectively Verifiable"
authors = "David Hafemeister"
year = 2008
url = "https://www.armscontrol.org/act/2008-10/features/comprehensive-test-ban-treaty-effectively-verifiable"
opened = "2026-11-27"

[source.einhorn2022jcpoa]
type = "report"
title = "Reviving the JCPOA Is the Better Alternative, But Can It Be Made Sustainable?"
authors = "Robert Einhorn (Brookings)"
year = 2022
url = "https://www.brookings.edu/wp-content/uploads/2022/05/FP_20220525_jcpoa_revival.pdf"
opened = "2026-11-27"

[source.frieden2021seven]
type = "peer-reviewed"
title = "7-1-7: an organising principle, target, and accountability metric to make the world safer from pandemics"
authors = "Thomas R. Frieden, Christopher T. Lee, Aaron F. Bochner, Marine Buissonnière, Amanda McClelland"
year = 2021
doi = "10.1016/S0140-6736(21)01250-2"
opened = "2026-11-27"

[source.pellis2021doubling]
type = "peer-reviewed"
title = "Challenges in control of COVID-19: short doubling time and long delay to effect of interventions"
authors = "Lorenzo Pellis, Francesca Scarabel, Helena B. Stage, Christopher E. Overton, Lauren H. K. Chappell, et al."
year = 2021
doi = "10.1098/rstb.2020.0264"
opened = "2026-11-27"

[source.williams2026breakout]
type = "essay"
title = "AI breakout time: a mechanism for an enforceable AI pause"
authors = "Connor Williams"
year = 2026
url = "https://connorsscratchpad.substack.com/p/ai-breakout-times-a-mechanism-for"
opened = "2026-11-27"

[source.pistillo2025loopholes]
type = "preprint"
title = "Defending Compute Thresholds Against Legal Loopholes"
authors = "Matteo Pistillo, Pablo Villalobos"
year = 2025
arxiv = "2502.00003"
opened = "2026-11-27"

[source.tadepalli2026efficiency]
type = "preprint"
title = "Efficiency vs Capability in the Intelligence Explosion"
authors = "Karthik Tadepalli"
year = 2026
arxiv = "2610.33447"
opened = "2026-11-27"

[source.srikanth2026aide2]
type = "preprint"
title = "Recursive self-improvement of AI research agents"
authors = "Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zhengyao Jiang"
year = 2026
arxiv = "2609.26457"
opened = "2026-11-27"

[source.flexrsi2026]
type = "preprint"
title = "Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents"
authors = "Flex-RSI Team"
year = 2026
arxiv = "2611.08946"
opened = "2026-11-27"

[source.blumberg2020supercritical]
type = "preprint"
title = "Assessing the plausibility of supercritical transmission for an emerging or re-emerging pathogen"
authors = "Seth Blumberg, Phoebe Lu, Thomas M. Lietman, Travis C. Porco"
year = 2020
doi = "10.1101/2020.02.08.20021311"
opened = "2026-11-27"

[source.blumberg2013stuttering]
type = "peer-reviewed"
title = "Inference of R0 and Transmission Heterogeneity from the Size Distribution of Stuttering Chains"
authors = "Seth Blumberg, James O. Lloyd-Smith"
year = 2013
doi = "10.1371/journal.pcbi.1002993"
opened = "2026-11-27"

[source.freckleton2006census]
type = "peer-reviewed"
title = "Census error and the detection of density dependence"
authors = "Robert P. Freckleton, Andrew R. Watkinson, Rhys E. Green, William J. Sutherland"
year = 2006
doi = "10.1111/j.1365-2656.2006.01121.x"
opened = "2026-11-27"

[source.ashenfelter1992twins]
type = "report"
title = "Estimates of the Economic Return to Schooling from a New Sample of Twins"
authors = "Orley Ashenfelter, Alan Krueger"
year = 1992
doi = "10.3386/w4143"
opened = "2026-11-27"

[source.imas2026explosion]
type = "essay"
title = "Are we approaching an intelligence explosion?"
authors = "Alex Imas, Luis Garicano"
year = 2026
url = "https://aleximas.substack.com/p/are-we-approaching-an-intelligence"
opened = "2026-11-27"

[source.carlini2019evaluating]
type = "preprint"
title = "On Evaluating Adversarial Robustness"
authors = "Nicholas Carlini, Anish Athalye, Nicolas Papernot, Wieland Brendel, Jonas Rauber, Dimitris Tsipras, et al."
year = 2019
arxiv = "1902.06705"
opened = "2026-11-27"

[source.tramer2020adaptive]
type = "preprint"
title = "On Adaptive Attacks to Adversarial Example Defenses"
authors = "Florian Tramer, Nicholas Carlini, Wieland Brendel, Aleksander Madry"
year = 2020
arxiv = "2002.08347"
opened = "2026-11-27"

[source.fda2007diagnostic]
type = "official-docs"
title = "Statistical Guidance on Reporting Results from Studies Evaluating Diagnostic Tests: Guidance for Industry and FDA Staff"
authors = "U.S. Food and Drug Administration, Center for Devices and Radiological Health"
year = 2007
url = "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/statistical-guidance-reporting-results-studies-evaluating-diagnostic-tests-guidance-industry-and-fda"
opened = "2026-11-27"

[source.abubaker2026fuzzing]
type = "preprint"
title = "Fuzzing Large Language Models to Elicit Hidden Behaviours"
authors = "Mohammed Abu Baker, Lakshmi Babu-Saheer"
year = 2026
arxiv = "2606.29646"
opened = "2026-11-27"

[source.duddu2026deceptive]
type = "preprint"
title = "Designing Deceptive Model Organisms that Successfully Evade Auditing"
authors = "Vasisht Duddu, Mark Wang, Lipeng He, Tim G. J. Rudner"
year = 2026
arxiv = "2611.20459"
opened = "2026-11-27"

[source.dashkovskiy2007smallgain]
type = "peer-reviewed"
title = "An ISS small gain theorem for general networks"
authors = "Sergey Dashkovskiy, Björn S. Rüffer, Fabian R. Wirth"
year = 2007
doi = "10.1007/s00498-007-0014-8"
arxiv = "math/0506434"
opened = "2026-11-27"

[source.roberts2003typer]
type = "peer-reviewed"
title = "A new method for estimating the effort required to control an infectious disease"
authors = "M. G. Roberts, J. A. P. Heesterbeek"
year = 2003
doi = "10.1098/rspb.2003.2339"
opened = "2026-11-27"

[source.shuai2013targetr]
type = "peer-reviewed"
title = "Extending the type reproduction number to infectious disease control targeting contacts between types"
authors = "Zhisheng Shuai, J. A. P. Heesterbeek, P. van den Driessche"
year = 2013
doi = "10.1007/s00285-012-0579-9"
opened = "2026-11-27"

[source.vanmieghem2011spectral]
type = "peer-reviewed"
title = "Decreasing the spectral radius of a graph by link removals"
authors = "Piet Van Mieghem, Dragan Stevanović, Fernando Kuipers, Cong Li, Ruud van de Bovenkamp, Daijie Liu, Huijuan Wang"
year = 2011
doi = "10.1103/PhysRevE.84.016101"
opened = "2026-11-27"

[source.bardoscia2017pathways]
type = "peer-reviewed"
title = "Pathways towards instability in financial networks"
authors = "Marco Bardoscia, Stefano Battiston, Fabio Caccioli, Guido Caldarelli"
year = 2017
doi = "10.1038/ncomms14416"
opened = "2026-11-27"
```
