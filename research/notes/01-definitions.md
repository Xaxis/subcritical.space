# Survey track 01: definitions and thresholds in force

- **Track:** 01, definitions and thresholds (frontier safety frameworks, AGI and ASI definitions, law,
  compute-threshold literature, superintelligence statements and treaty proposals).
- **Date:** 2026-11-27. Every source below was opened on this date unless the entry says otherwise.
- **Scope:** the exact text of each definition or threshold, what triggers it, how it is measured,
  and its known weaknesses; plus a targeted search for prior work on the memo's D1 to D6.
- **Method:** web search, then the primary document (PDF text extracted locally where the fetcher
  could not read it). Quotes are verbatim and short. Where a primary text could not be loaded, the
  entry says so and names what was read instead.

## Summary: what matters most for Subcritical

1. **D4's core inequality is prior work.** Barnett and Scher (MIRI TGT, 2025) state that a stable
   regime needs nations "to detect and respond to dangerous AI development faster than any single
   country's breakout time". A Narrow Path (v1.2.0, April 2025) sets cluster caps so an illegal run
   would need 3.2 years, "giving authorities ample time to intervene". The Berkeley hardwired-pause
   working paper (Oct 2026) derives fleet thresholds from a breakout horizon T_B = 2 years chosen as
   the time before "the rest of the world could react". Meta's 2026 framework names, as a
   loss-of-control outcome, development that outpaces evaluation. D4 should be downgraded from "new"
   to "extends prior work"; what our search did not find is the line *defined* by T_b < m * T_r with
   a measured T_r and a loop-gain term inside T_b.
2. **D2's trigger is already in force and has been measured.** Anthropic's RSP v3.4 (July 2026)
   triggers on a doubling of the rate of AI progress attributable to automated R&D; OpenAI's Critical
   level is a generational improvement in 1/5 of 2024's wall-clock time; DeepMind has "ML R&D
   acceleration level 1". METR (Nov 2026) measured a 1.9x acceleration (95% CI 1.5 to 2.8x) in
   Anthropic's internal capability index since October 2025. Burtsev (Aug 2026) defines a recursive
   reproduction number R_AI = chi * a / sigma with a self-amplifying regime at R_AI > 1, including an
   "operational closure" factor chi. The memo's D2 is at most "extends prior work".
3. **Pre-set capability thresholds have proved hard to operate.** Anthropic (Feb 2026): "We found
   pre-set capability levels to be far more ambiguous than we anticipated"; its AI R&D threshold "has
   proven difficult to operationalize" (v3.4). Anthropic dropped its fixed elicitation budget (1% of
   compute) and 6x buffer in 2024. Any Subcritical trigger must come with its measurement procedure.
4. **Compute thresholds in law drift and are being widened.** EU AI Act 10^25 FLOP (Art. 51); US EO
   14110's 10^26 (revoked 20 Jan 2025); California SB 53 and New York's amended RAISE Act 10^26 plus
   a $500M revenue test. The Code of Practice chairs expect "hundreds" of models above 10^25 within a
   few years. Treaty proposals sit 2 to 4 orders of magnitude lower (MIRI: prohibit above 10^24,
   monitor above 10^22) and note the needed threshold falls about 3x a year with algorithmic progress.
5. **Company frameworks do not bind in a race and assume no stronger rival.** OpenAI and Anthropic
   both condition commitments on competitors; DeepMind assumes "we do not expect other groups to put
   significantly more effort into ML R&D than we do ourselves". None defines superintelligence or a
   breakout notion. This supports the memo's move to a state-level regime.
6. **Against the memo's D1 novelty claim:** comparison against organisations at matched cost already
   exists for AI R&D (Anthropic: substitute the entire research staff "within a factor of 5" of cost;
   DeepMind: "any team of researchers at Google ... approximately comparable all-inclusive costs").
   Matched-time comparison exists in RE-Bench. D1's multi-cluster, matched-budget, best-organisation
   battery was not found as such.

## A. Frontier safety frameworks (company policies)

### anthropic-rsp-v3-4
Responsible Scaling Policy, Version 3.4, effective July 8, 2026. Anthropic. URL:
https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf (linked from anthropic.com/rsp).
Opened 2026-11-27 (text extracted from the PDF).

- **Automated R&D threshold (Section 1 table, "Automated R&D in key domains"):** "AI systems that can
  fully automate, or otherwise dramatically accelerate, the work of large, top-tier teams of human
  researchers in domains where fast progress could cause threats to international security and/or
  rapid disruptions to the global balance of power". Evaluations "will focus specifically on AI R&D".
- **When it is met:** "if we determine that either (1) our models would be able to fully substitute
  for our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within
  a factor of 5); or (2) there is 'dramatic acceleration' of the pace of AI progress for reasons that
  likely relate to the automation of AI R&D."
- **Dramatic acceleration:** "(a) we observe or expect double the rate of progress in AI aggregate
  capabilities compared to both the rate we'd expect and the fastest rate of extended progress we've
  observed in the absence of significant AI contributions to AI R&D and (b) it is plausible that this
  doubling is substantially attributable to the automation of research and/or engineering", "such that
  continuation of the trend in AI progress seems likely to lead to even greater acceleration."
  Footnote 8: "'Double the rate of progress' means 'as much progress in one year as one would see in two
  years at baseline.'" Worked example: baseline 3x compute and 3x algorithmic efficiency (9x effective
  scaleup) means doubling "would entail something like an 81x effective scaleup." Footnote 8 also:
  "This is not the same idea as 'doubling researchers' productivity,' since doubling inputs does not
  necessarily double the rate of progress." Footnote 9: the baseline is measured "Over at least three
  model generations."
- **v3.4 changelog (p. 20):** the threshold is not crossed if overall progress were "constant or
  slowing" even if faster than without AI tools; "This threshold is intended to capture the onset of
  dramatic recursive self-improvement, and has proven difficult to operationalize."
- **v2.0 changelog (Oct 2024):** replaced the autonomous replication and adaptation (ARA) threshold with
  a "checkpoint"; "Rather than using prespecified evaluations, we now require an affirmative case that
  models are sufficiently far from Capability Thresholds"; evaluation cadence "4x Effective Compute or
  six months of accumulated post-training enhancements"; removed "using 1% of compute for elicitation
  or creating a 6x buffer"; "the science of evaluations is not currently mature enough to make
  confident predictions about the precise buffer we should require".
- **v2.1 (Mar 2025):** AI R&D split into "the ability to fully automate entry-level AI research work,
  and the ability to cause dramatic acceleration in the rate of effective scaling".
- **Appendix A (competitors):** Anthropic will "delay AI development and deployment" in the scenario
  where it is in the lead and has "clear evidence that no other competitor will soon develop such a
  model", "until and unless we no longer believe we have a significant lead", or until it matches
  competitors with strong safety measures. Under "General upleveling" it "will not necessarily delay".
- **Weaknesses (from the text):** the threshold is a judgement ("we determine"), relies on observed
  progress rather than a pre-run test, and commitments are conditional on competitors.
- **Bears on:** D2 (the doubling-of-rate condition is an operating trigger), D1 (organisation-level
  comparison at matched cost), D5 (elicitation budget removed), O2, pathway "recursive
  self-improvement".

### anthropic-rsp-page-2026
"Anthropic's Responsible Scaling Policy" (policy page and update log). Anthropic, 2026. URL:
https://www.anthropic.com/rsp. Opened 2026-11-27.

- States the current version is 3.4, effective July 8, 2026; page updated August 14, 2026.
- Illustrates the AI R&D-4 threshold as the ability to "compress two years of 2018 - 2024 AI progress
  into a single year" and says Claude Opus 4.6 did not cross it (determination February 2026).
- Admits past evaluations "lacked some basic elicitation techniques such as best-of-N or
  chain-of-thought prompting" and that its evaluations "did not explicitly establish the 6x scaling
  buffer".
- **Bears on:** D5 (elicitation gaps admitted in practice), D2.

### anthropic-rsp-v3-announcement-2026
"Anthropic's Responsible Scaling Policy, Version 3.0" (announcement). Anthropic, Feb 24, 2026. URL:
https://www.anthropic.com/news/responsible-scaling-policy-v3. Opened 2026-11-27.

- Section 02: "We found pre-set capability levels to be far more ambiguous than we anticipated"; "The
  science of model evaluation isn't well-developed enough to provide dispositive answers"; the higher
  mitigations "might prove outright impossible to implement without collective action".
- Section 01: the original RSP "intentionally left the later ASLs (ASL-4 and beyond) largely undefined."
- Roadmap goals are "public goals", "Rather than being hard commitments".
- **Bears on:** D1 and D5 (measurement is the binding constraint), O2 (collective action needed),
  protocol shape (a state-level regime instead of company pledges).

### openai-preparedness-v2-2025
Preparedness Framework, Version 2. OpenAI. Last updated 15 April 2025. URL:
https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf.
Opened 2026-11-27 (PDF text). A search found no published Version 3 as of this date; press reports
(not opened) say one is in preparation.

- **AI Self-improvement, High:** "The model's impact is equivalent to giving every OpenAI researcher a
  highly performant mid-career research engineer assistant, relative to those researchers' 2024
  baseline."
- **AI Self-improvement, Critical:** "The model is capable of recursively self improving (i.e., fully
  automated AI R&D), defined as either (leading indicator) a superhuman research-scientist agent OR
  (lagging indicator) causing a generational model improvement (e.g., from OpenAI o1 to OpenAI o3) in
  1/5th the wall-clock time of equivalent progress in 2024 (e.g., sped up to just 4 weeks) sustainably
  for several months." Response: "halt further development" until Critical safeguards are specified.
- **Elicitation:** evaluations "approximate the full capability that the adversary contemplated by our
  threat model could extract", with refusal-free variants and "the best presently-available
  scaffolds", fine-tuning "if the weights will be released"; "we regard any one-time capability
  elicitation in a frontier model as a lower bound, rather than a ceiling".
- **Sandbagging (Research Category):** "Adopt elicitation approach that overcomes sandbagging, or use a
  conservative upper bound of the model's non-sandbagged evaluation results".
- **Long-range Autonomy and Autonomous Replication and Adaptation** were demoted to Research Categories
  in v2 (not triggers).
- **Competitor clause (Section 4):** "another frontier AI model developer might develop or release a
  system with High or Critical capability ... without instituting comparable safeguards"; if
  confirmed, OpenAI may adjust its requirements.
- **Weaknesses:** "generational improvement" has no operational metric in the text; the lagging
  indicator fires only after months of sustained acceleration.
- **Bears on:** D2 (a time-ratio trigger: 5x speed-up of a generation), D4 (a lagging trigger is
  structurally too late if T_b is short), D5, pathways "recursive self-improvement" and
  "self-replication".

### gdm-fsf-v3-1-2026
Frontier Safety Framework, Version 3.1. Google DeepMind. Published April 17, 2026. URL:
https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf.
Opened 2026-11-27 (PDF text). Versions 1.0 (May 2024), 2.0 (Feb 2025), 3.0 (Sep 2025) listed at
deepmind.google/frontier-safety.

- **Table 3.2.2.a, ML R&D CCLs:** "ML R&D acceleration level 1: Has been used to accelerate AI
  development, resulting in AI progress substantially accelerating from historical rates" (security
  level 3). "ML R&D automation level 1: Can fully automate the work of any team of researchers at
  Google focused on improving AI capabilities, with approximately comparable all-inclusive costs"
  (security level 4, which "must be taken on by the frontier AI field as a whole").
- **Stealth and Situational Awareness TCL:** "The instrumental reasoning abilities of the model enable
  enough situational awareness ... and stealth ... such that, absent additional mitigations, we cannot
  rule out the model significantly undermining human control."
- **Alert thresholds:** set "marginally earlier than our CCLs"; early warning evaluations may run more
  often "if the rate of progress suggests our safety buffer is no longer adequate."
- **Elicitation:** "we seek to apply appropriate scaffolding, inference compute, and other
  augmentations".
- **Key assumption ("Note on Machine Learning R&D CCLs", Section 1.3, just before 1.3.3):** "as a frontier AI company, we do not expect other
  groups to put significantly more effort into ML R&D than we do ourselves", so ML R&D CCLs may be
  judged from "our own progress at accelerating ML R&D".
- **Weaknesses:** "substantially accelerating" is not quantified; the self-referential assumption fails
  exactly in a state breakout scenario.
- **Bears on:** D2, D4 (buffer tied to rate of progress, an informal timeliness idea), D1 (team-level
  comparison at comparable cost), O2.

### meta-ssf-v2-1-2026
Meta Superintelligence Scaling Framework, Version 2.1 (previously titled the Frontier AI Framework).
Meta, October 2026. URL: https://research.meta.ai/static/meta-superintelligence-scaling-framework.
Opened 2026-11-27 (PDF text).

- Focus: "Chemical & Biological, Cybersecurity, and Loss of Control". Thresholds are outcome-based:
  safeguards required "Where our evaluations indicate that a model would substantially contribute to
  the realization of one or more identified threat scenarios".
- **Loss of Control 1, "Loss of ability to evaluate AI safety before deployment":** "TS.1.1 AI
  development accelerates such that new capabilities and behaviors emerge faster than the
  organization's evaluation processes." Enabling capability: "Autonomous AI R&D: Ability to
  autonomously and consistently complete tasks which are representative of the work of a researcher
  to progress AI development." Also "Evaluation awareness" and "Selective evaluation-adaptive behavior".
- **Loss of Control 3 (new in 2.1):** "AI covertly operates outside of its authorized environment",
  enabled by cyber exploitation, long-horizon operation and "Goal-oriented swarming".
- Preparedness reports on a "substantial increase in computing resources" and "expedited updates if we
  identify any unprecedentedly rapid increase in capabilities".
- **Bears on:** D4 (LoC 1 is the in-company form of "development faster than detection"), D5
  (evaluation awareness named as an enabling capability), D2, pathway "self-replication".

### xai-rmf-2025
xAI Risk Management Framework. xAI. Last updated August 20, 2025. URL:
https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf. Opened 2026-11-27 (PDF text). A later
"Frontier Artificial Intelligence Framework" dated 30 June 2026 appeared in search, but its URL
returned HTTP 404, so it is not summarised here.

- Two categories, "malicious use and loss of control". Thresholds: bio, "maintaining an answer rate of
  less than 1 out of 20 on restricted queries"; loss of control, "maintaining a dishonesty rate of less
  than 1 out of 2 on MASK".
- No AI R&D or self-improvement threshold, no compute threshold.
- **Weakness:** the loss-of-control criterion is a propensity score on an honesty benchmark, not a
  capability or loop measure.
- **Bears on:** D2 (absent), D5 (not elicitation-based).

### metr-common-elements-2025
"Common Elements of Frontier AI Safety Policies". METR, December 16, 2025. URL:
https://metr.org/common-elements. Opened 2026-11-27.

- Covers 12 companies. AI R&D thresholds as summarised: Anthropic AI R&D-4 ("fully automate the work of
  an entry-level, remote-only Researcher") and AI R&D-5; OpenAI Critical; DeepMind ML R&D automation;
  Magic ("a dramatic acceleration in the rate of effective compute scaling"); Microsoft ("can fully
  automate the AI R&D pipeline at a fraction of human labor costs"); Amazon ("capable of replacing human
  researchers and fully automating the research, development, and deployment of frontier models");
  Meta treats automated AI R&D as an enabling capability, not a threat model.
- Seven of the policies commit to full capability elicitation.
- **Bears on:** D2 (automated AI R&D is the near-universal industry trigger for the self-improvement
  pathway), D5.

### metr-anthropic-acceleration-2026
"Independent Assessment of AI R&D Acceleration at Anthropic in October 2026". METR (T. Cunningham, N.
Rush, P. Whitfill, H. Wijk), November 5, 2026. URL:
https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/. Opened 2026-11-27.

- Growth is expressed as annual multiples and acceleration as the ratio of growth rates; a 2x
  acceleration means two years of historical progress made in one year (paraphrase of the report).
- Metric: AECI, Anthropic's version of the Epoch Capabilities Index. Historical trend about 15 points a
  year, about 29 points a year after a fitted breakpoint of October 7, 2025 (piecewise linear fit,
  bootstrap CIs, Epoch's public code).
- Headline: about 1.9x (95% CI 1.5 to 2.8x); robustness range 1.1x to 2.9x; METR "would not be
  surprised" if nearer 1.3x or 3x. Subjective attribution: about 80% of the October 2026 acceleration
  due to AI. Confident it was not driven by faster training-compute scaling. Staff polls reported about
  12x self-reported uplift, treated as "very loose evidence".
- METR "did not pay special attention to RSP thresholds"; the report does not say whether any RSP
  threshold is crossed.
- **Limitations stated:** most informative evidence redacted by Anthropic; no staff-level access;
  benchmark saturation (the most capable model above 50% on all benchmarks used); Claude did much of
  the analysis; Anthropic "removed a compute-allocation verification component midway".
- **Bears on:** D2 (the closest existing measured estimate of a self-improvement acceleration ratio
  with a confidence interval; not at fixed inputs, not per-round), D3, protocol verification (a
  developer can withdraw verification mid-engagement).

## B. Definitions of AGI and superintelligence

### morris2023levels
"Levels of AGI for Operationalizing Progress on the Path to AGI". M. R. Morris, J. Sohl-Dickstein, N.
Fiedel, T. Warkentin, A. Dafoe, A. Faust, C. Farabet, S. Legg. arXiv:2311.02462 (v5, 24 Sep 2025;
Proceedings of ICML 2024). Opened 2026-11-27 (abstract page and HTML v5).

- Six principles (Section 3), including "Focus on Capabilities, not Processes", "Focus on Potential,
  not Deployment", "Focus on Ecological Validity", "Focus on the Path to AGI, not a Single Endpoint".
- Performance levels (Table 1): Level 2 Competent "at least 50th percentile of skilled adults"; Level 3
  Expert "at least 90th percentile"; Level 4 Exceptional (formerly "Virtuoso") "at least 99th
  percentile"; Level 5 Superhuman "outperforms 100% of humans". The general Level 5 cell is "Artificial
  Superintelligence (ASI)", "not yet achieved".
- Autonomy levels (Table 2): from "AI as a Tool" to Level 5 "AI as an Agent", "fully autonomous AI".
- Section 5: the paper does "not propose a benchmark"; an AGI benchmark "should be a living benchmark".
- Compares against individual skilled adults, not organisations; no speed or copy-count measure.
- **Bears on:** D1 (the percentile-of-individuals baseline D1 departs from), F1, F3.

### hendrycks2025agi
"A Definition of AGI". D. Hendrycks, D. Song, C. Szegedy and 30 others. arXiv:2510.18212 (v3, 3 Dec
2025). Opened 2026-11-27 (abstract page).

- AGI: "matching the cognitive versatility and proficiency of a well-educated adult", operationalised
  over ten Cattell-Horn-Carroll cognitive domains with adapted psychometric batteries.
- Scores: GPT-4 27%, GPT-5 57%; profile "highly 'jagged'", weakest in long-term memory storage.
- Does not define superintelligence.
- **Bears on:** D1 (individual-adult baseline again), F3 (jaggedness: generality is not one number),
  pathway "continual learning" (memory storage deficit).

### bostrom1998long
"How Long Before Superintelligence?". N. Bostrom. International Journal of Futures Studies, 1998, vol.
2 (revised 25 October 1998, postscripts to 2008). URL: https://nickbostrom.com/superintelligence.
Opened 2026-11-27.

- Definition: "an intellect that is much smarter than the best human brains in practically every
  field", including scientific creativity, general wisdom and social skills.
- Hardware estimate: human-level intelligence "probably requires between 10^14 and 10^17 ops"
  (operations per second; lower bound from Moravec's retina estimate, upper from per-neuron simulation).
- The 2014 book (Superintelligence: Paths, Dangers, Strategies, OUP) and its speed, collective and
  quality typology could not be opened (no accessible full text), so neither its definition nor its
  typology is recorded in this note. F1 should cite the book only after someone opens it.
- **Bears on:** D1 (the "best human brains" baseline, individual not organisation), P1 (brain compute
  as a reference point).

## C. Law and official instruments

### eu-ai-act-2024
Regulation (EU) 2024/1689 (Artificial Intelligence Act), Articles 51 and 52 and Annex XIII. European
Parliament and Council, 2024. Read via the article-by-article reproduction at
https://artificialintelligenceact.eu/article/51/ (also /article/52/ and /annex/13/), because EUR-Lex
returned an empty response to automated fetches. Opened 2026-11-27.

- **Art. 51(1) (paraphrase):** a GPAI model has systemic risk if (a) it has high-impact capabilities,
  assessed with appropriate technical tools and methodologies including indicators and benchmarks, or
  (b) the Commission so decides, on its own initiative or after a qualified alert from the scientific
  panel, having regard to Annex XIII.
- **Art. 51(2) (paraphrase):** high-impact capabilities are presumed when the cumulative training
  compute, measured in floating point operations, is greater than 10^25.
- **Art. 51(3) (paraphrase):** the Commission may amend these thresholds by delegated act as technology
  changes, for example through algorithmic improvements or more efficient hardware.
- **Art. 52(1):** the provider shall "notify the Commission without delay and in any event within two
  weeks after that requirement is met", or once "it becomes known that it will be met". Art. 52(2): the
  provider may "present, with its notification, sufficiently substantiated arguments to demonstrate
  that, exceptionally," the model "does not present, due to its specific characteristics, systemic
  risks".
- **Annex XIII criteria:** "(a) the number of parameters of the model"; "(b) the quality or size of the
  data set, for example measured through tokens"; "(c) the amount of computation used for training ...
  or indicated by a combination of other variables such as estimated cost of training, estimated time
  required for the training, or estimated energy consumption"; "(e) the benchmarks and evaluations of
  capabilities ... its level of autonomy and scalability, the tools it has access to"; "(f) ... presumed
  when it has been made available to at least 10 000 registered business users established in the
  Union".
- **Weaknesses:** a training-compute presumption ignores inference compute, post-training and
  algorithmic progress (see hooker2024limits); the presumption is rebuttable.
- **Bears on:** P1, A2, A3, D5 (capability evaluations are the alternative route), protocol
  "declarations" (a notification duty already exists at 10^25).

### ec-gpai-guidelines-faq-2025
"Guidelines for providers of general-purpose AI models: General FAQ". European Commission (AI Office),
page last updated 11 November 2025. URL:
https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-gpai-providers. Opened 2026-11-27.

- Indicative GPAI criterion: training compute that "exceed[s] 10^23 floating point operations (FLOP)"
  with language, text-to-image or text-to-video output; it "is not an absolute rule".
- A downstream modifier becomes a provider when the modification "uses more than one-third of the
  original model's training compute".
- Systemic-risk presumption: "a cumulative amount of computational resources exceeding 10^25 FLOP";
  "The Commission must adjust this threshold when necessary to account for technological developments."
- Notification "without delay, and within two weeks at the latest". Obligations apply from 2 August 2025.
- **Bears on:** P1, A3, protocol "declarations" (a fine-tuning share rule exists: one third).

### gpai-code-of-practice-2025
General-Purpose AI Code of Practice, Safety and Security chapter, Final Version (10 July 2025), with the
Chairs' statement. URL: https://code-of-practice.ai/?section=safety-security. Opened 2026-11-27.

- **Measure 4.1:** systemic risk tiers "defined in terms of model capabilities", measurable, at least
  one tier not yet reached, with a safety margin accounting for uncertainty (summary of the text).
- **Appendix 1.4, loss of control:** "Risks from humans losing the ability to reliably direct, modify,
  or shut down a model", from misalignment, self-reasoning, self-replication, self-improvement,
  deception, "resistance to goal modification, power-seeking behaviour", and autonomously creating or
  improving AI models.
- **Appendix 1.3.1 model capabilities:** includes "capabilities to self-replicate, self-improve, or
  modify its own implementation environment;" (item 10) and "capabilities to automate AI research and
  development;" (item 11).
- **Appendix 3.2, elicitation:** "Signatories will ensure that the model evaluations are conducted with
  at least a state-of-the-art level of model elicitation", minimising under-elicitation and "model
  deception during model evaluations (e.g. sandbagging)", adapting "test-time compute, rate limits,
  scaffolding, and tools", and must "match the model elicitation capabilities of misuse actors relevant
  to the systemic risk scenario".
- **Chairs' statement:** drafted "assuming only about 5-15 providers will be subject to the systemic
  risk obligations"; the 10^25 threshold "may soon fail to capture only the most advanced models, with
  estimates suggesting that there will be hundreds of such models within a few years"; recommends
  "exploring thresholds based on factors other than computational power including capability-related
  considerations".
- **Bears on:** D5 (elicitation matched to adversaries is already a regulatory expectation in the EU),
  D2 (automated AI R&D named as a capability of concern), D6 (self-improvement listed), P1.

### eo14110-2023
Executive Order 14110, "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence",
October 30, 2023. 88 FR 75191 (FR Doc. 2023-24283). URL:
https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf. Opened 2026-11-27 (PDF text).

- **Sec. 4.2(b) interim reporting conditions:** "(i) any model that was trained using a quantity of
  computing power greater than 10^26 integer or floating-point operations, or using primarily
  biological sequence data and using a quantity of computing power greater than 10^23 integer or
  floating-point operations; and (ii) any computing cluster that has a set of machines physically
  co-located in a single datacenter, transitively connected by data center networking of over 100
  Gbit/s, and having a theoretical maximum computing capacity of 10^20 integer or floating-point
  operations per second for training AI."
- **Sec. 3(k) "dual-use foundation model":** trained on broad data, self-supervised, "at least tens of
  billions of parameters", and exhibiting or easily modified to exhibit high performance at tasks such
  as "(iii) permitting the evasion of human control or oversight through means of deception or
  obfuscation."
- **Bears on:** P1 (a cluster-capacity threshold, not just a training total, which relates to the
  breakout-speed logic of D3/D4), O3.

### eo14148-2025
Executive Order 14148, "Initial Rescissions of Harmful Executive Orders and Actions", January 20, 2025.
90 FR 8237 (FR Doc. 2025-01901). URL: https://www.govinfo.gov/content/pkg/FR-2025-01-28/pdf/2025-01901.pdf.
Opened 2026-11-27 (PDF text).

- Sec. 2 revokes, among others, "(ggg) Executive Order 14110 of October 30, 2023".
- **Bears on:** the US federal compute-reporting threshold no longer exists by executive order;
  protocol "who it binds" (thresholds in executive orders are fragile).

### ca-sb53-analysis-2025
"SB 53 (Wiener), As Amended September 5, 2025", bill analysis for the hearing of September 11, 2025.
California Assembly Committee on Privacy and Consumer Protection. URL: https://apcp.assembly.ca.gov/media/1019.
Opened 2026-11-27 (PDF text). The official bill text site (leginfo.legislature.ca.gov) returned HTTP 403,
so the bill's definitions are taken from this analysis, which restates them.

- **"Catastrophic risk":** "a foreseeable and material risk that a frontier developer's development,
  storage, use, or deployment of a frontier model will materially contribute to the death of, or
  serious injury to, more than 50 people or more than $1 billion in damage to, or loss of, property
  arising from a single incident involving a frontier model" doing any of: expert-level CBRN
  assistance; "Engaging in conduct with no meaningful human oversight, intervention, or supervision"
  that is a cyberattack or would be murder, assault, extortion or theft; "Evading the control of its
  frontier developer or user."
- **"Critical safety incident"** includes "Loss of control of a frontier model causing death or bodily
  injury" and deceptive subversion of developer controls "outside of the context of an evaluation
  designed to elicit this behavior".
- **"Frontier model":** "a foundation model that was trained using a quantity of computing power greater
  than 10^26 integer or floating-point operations." **"Large frontier developer":** annual gross
  revenues "in excess of $500 million".
- **Updating:** "Beginning in 2027, CDT must provide recommendations to the Legislature on updating the
  definitions", which "may go beyond purely quantitative thresholds", since "compute alone may not
  remain the most appropriate proxy for catastrophic risk."
- **SB 1047 (vetoed 2024):** covered models over 10^26 and "costing over $100 million to train". Veto
  message quoted: "Smaller, specialized models may emerge as equally or even more dangerous than the
  models targeted by SB 1047". (The analysis describes 10^26 as "floating-point operations per second",
  a unit slip; the statute counts operations.)
- **Bears on:** D1 (harm-count definition, not capability), D6 ("evading the control" as a defined
  risk), P1, A3.

### fpf-sb53-2025
"California's SB 53: The First Frontier AI Law, Explained". J. Gluck, Future of Privacy Forum, October 3,
2025 (updated February 4, 2026). URL: https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/.
Opened 2026-11-27.

- Signed September 29, 2025. Cumulative compute counts initial training plus later fine-tuning and
  modifications. Incident reports within 15 days, or 24 hours if there is imminent danger of death or
  serious injury. Civil penalties capped at $1 million per violation. Frameworks must assess
  catastrophic risk from internal use.
- **Bears on:** protocol "declarations" (incident reporting latencies exist in law: 15 days, 24 hours).

### ny-a9449-2026
New York Assembly Bill A9449 (chapter amendment to the RAISE Act, S6953-B/A6453-B), introduced January
6, 2026 by M. of A. Bores. URL: https://legislation.nysenate.gov/pdf/bills/2025/A9449. Opened 2026-11-27
(PDF text). Search results (law-firm notes, not opened) report the original act signed December 19,
2025 and these amendments signed March 27, 2026, effective January 1, 2027.

- "'Frontier model' means a foundation model that was trained using a quantity of computing power
  greater than 10^26 integer or floating-point operations."
- "'Catastrophic risk' means a foreseeable and material risk that ... more than fifty people or more
  than one billion dollars", including "(iii) evading the control of its frontier developer or user."
- **Bears on:** convergence of US state law on the California definitions; P1.

### seoul-commitments-2024
"Frontier AI Safety Commitments, AI Seoul Summit 2024". UK Government (DSIT). Page updated 7 February
2025. URL: https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024.
Opened 2026-11-27.

- Signatories set "thresholds at which severe risks posed by a model or system, unless adequately
  mitigated, would be deemed intolerable" and commit "not to develop or deploy a model or system at
  all, if mitigations cannot be applied to keep risks below the thresholds". 20 companies (16 initial,
  4 added).
- **Bears on:** the origin of the company frameworks in section A; O2.

## D. Compute-threshold literature

### heim2024compute
"Training Compute Thresholds: Features and Functions in AI Regulation". L. Heim, L. Koessler.
arXiv:2405.10799 (v2, 6 Aug 2024). Opened 2026-11-27 (abstract and HTML v2).

- Compute thresholds "serve as an initial filter to trigger additional regulatory requirements and
  scrutiny"; compute "correlates with model capabilities and risks, is quantifiable, can be measured
  early in the AI lifecycle", and is externally verifiable; also "difficult to circumvent" and
  cost-tracking.
- Limits: "only a very crude proxy for risk"; post-training enhancements worth roughly 5x to 20x
  compute-equivalent; biological design tools need about 100x less compute; algorithmic efficiency
  erodes the link over time.
- "compute thresholds alone should generally not determine which mitigation measures are ultimately
  required"; review thresholds "at least every few months" (US). Effective compute and capabilities are
  "better proxies for risk" but "much harder to measure".
- As of mid-2024: no model officially reported above 10^26; Inflection-2 officially above 10^25.
- **Bears on:** P1, A2, A3, D5 (capability evaluations as the second stage).

### hooker2024limits
"On the Limitations of Compute Thresholds as a Governance Strategy". S. Hooker. arXiv:2407.05694 (v2, 30
Jul 2024). Opened 2026-11-27 (abstract and HTML v2).

- "The relationship between compute and risk is highly uncertain and rapidly changing."
- Evidence: Aya 23 8B outperforms BLOOM 176B "despite having only 4.5% of the parameters"; best 13B-or-
  smaller model on the Open LLM Leaderboard rose from 38.59% to 77.15% average in about two years;
  inference-time methods give gains "between 5x and 20x of base level post-training performance"
  without training FLOP; MoE, quantisation and shared pre-training make FLOP ambiguous; system-level
  (agentic, cascaded) risk can exceed what any one model's FLOP shows.
- Proposals: dynamic thresholds that self-adjust "to a percentile of the distribution of model
  properties released that year", a risk index of several measures, a standard for FLOP reporting.
- **Bears on:** A2 (inference substitutes for training), A3, P1, D5, pathway "unbounded scaling".

### koessler2024risk
"Risk thresholds for frontier AI". L. Koessler, J. Schuett, M. Anderljung. arXiv:2406.14713 (20 Jun 2024).
Opened 2026-11-27 (abstract page).

- Capability thresholds: "AI capabilities beyond which an AI system is deemed to pose too much risk";
  risk thresholds "simply state how much risk would be too much"; risk thresholds are "more principled
  than capability thresholds" but "more difficult to evaluate reliably". Recommends defining risk
  thresholds and using them to set capability thresholds, relying primarily on the latter.
- **Bears on:** D4 (a time-based line is a third kind of threshold, neither capability nor risk
  probability, that this taxonomy does not cover), D1.

## E. Statements and treaty proposals to prevent superintelligence

### fli-superintelligence-statement
"Statement on Superintelligence". Hosted by the Future of Life Institute. URL:
https://superintelligence-statement.org/. Opened 2026-11-27. The page itself shows no release date.

- Text: "We call for a prohibition on the development of superintelligence, not lifted before there is"
  "broad scientific consensus that it will be done safely and controllably, and" "strong public buy-in."
- No formal definition; context describes systems that "can significantly outperform all humans on
  essentially all cognitive tasks". 79,159 signatories shown on 2026-11-27.
- **Bears on:** D1 (the statement prohibits a thing it does not define operationally, which is the gap
  Subcritical's definitions aim to fill).

### redlines-2025
"Global Call for AI Red Lines". Organised by CeSIA, The Future Society and CHAI; launched September 2025
at the 80th UN General Assembly. URL: https://red-lines.ai/. Opened 2026-11-27.

- "We urge governments to reach an international agreement on red lines for AI", "clear and verifiable",
  by the end of 2026. Specific lines left to "scientific-diplomatic dialogues". FAQ examples include
  (paraphrase) prohibiting systems that can replicate or significantly improve themselves without
  explicit human authorisation. 300+ prominent signatories and 90+ organisations shown.
- No definition of superintelligence.
- **Bears on:** D6 and pathways "self-replication" and "recursive self-improvement" (both named as
  candidate red lines); the end-of-2026 deadline has no agreement as of this note (per search).

### scher2025agreement
"An International Agreement to Prevent the Premature Creation of Artificial Superintelligence". A. Scher,
D. Abecassis, P. Barnett, B. Abeyta (MIRI Technical Governance Team). arXiv:2511.10783 (v2, 17 Nov 2025);
also Proceedings of IASEAI 2(1), 708-723 (per search). Opened 2026-11-27 (HTML v2).

- **Art. II definitions:** "Artificial superintelligence (ASI) is operationally defined as any AI with
  sufficiently superhuman cognitive performance that it could plan and successfully execute the
  destruction of humanity"; unauthorised development beyond Art. IV limits "shall be assumed to have
  the aim of creating artificial superintelligence." Section 1 (informal): "AI substantially smarter
  than humans at all cognitive tasks."
- **Thresholds (Art. II):** Strict Threshold 10^24 FLOP (training prohibited above); Strict
  Post-training Threshold 10^23 FLOP; Monitored Threshold 10^22 FLOP; "Covered chip cluster (CCC) means
  any set of AI chips or networked cluster with aggregate effective computing capacity greater than 16
  H100-equivalents" (15,840 TFLOP/s; networking above 25 Gbit/s inter-node bandwidth counts).
- **Rationale:** 10^24 is "slightly below that used to train models near the state of the art as of
  August 2025 (such as DeepSeek-V3, trained with 3x10^24 FLOP)"; "between 50 and 100" models above
  10^24 by mid-2025. Algorithmic progress: operations to reach a capability level drop "by 3x each year",
  so the monitored cluster size must fall 3x a year (citing Ho et al. 2024).
- **Art. VIII Restricted Research:** research "that would materially advance toward ASI or undermine
  verification", including "(a) Improvements to methods for training general-purpose AI systems that
  would significantly increase model capabilities toward superintelligent performance or dramatically
  reduce the computational resources required".
- **Breakout:** used qualitatively: "breakout is when a party attempts to create ASI before anyone else
  can stop them"; "the existence of AI chips makes breakout time too short"; the authors judge "the
  benefit of longer breakout times" not clearly worth shutting off all chips. No numeric breakout or
  detection time. Withdrawal: 12 months' notice; consolidation of CCCs within 120 days.
- **Detectability:** data centres above 100,000 H100-equivalents "are hard to hide"; intelligence
  services can "probably" locate ones "as small as around 10,000 H100-equivalents".
- **Stated weaknesses:** the methods for detecting covert violations "do not prevent overt
  violations"; remote attestation could
  "likely be circumvented if the chips' physical locations remain unknown".
- **Bears on:** D1 (an operational, harm-based ASI definition plus a presumption rule), D3, D4, P4
  (detectability sizes), A3, O3, protocol "compute", "defection".

### barnett2025governance
"AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research Questions". P.
Barnett, A. Scher (MIRI TGT). arXiv:2505.04592 (v1, 7 May 2025). Opened 2026-11-27 (PDF text).

- Glossary: "Breakout time: The time it would take a country to develop dangerous AI capabilities or do
  certain AI activities, likely in violation of agreements or monitoring." ASI: "AI that can
  substantially surpass humanity in all strategically relevant activities (economic, scientific,
  military, etc.)".
- **Threat of Sabotage regime:** "nations must be able to detect and respond to dangerous AI development
  faster than any single country's breakout time", defined in the same sentence as "the time needed to
  secretly advance beyond permitted levels of AI capabilities." Stability needs visibility and sabotage capability; "extending breakout
  times via limiting AI infrastructure, could make the situation more stable."
- Research questions: "What is the breakout time for doing secret AI chip development"; "How long does
  breakout time need to be?"; "If there are AI's capable of automating AI R&D, breakout times may be
  very short, even given limited compute."
- **Bears on:** D4 (the inequality, stated qualitatively), D3 (breakout time defined; AI R&D shortens
  it), D2, O2.

### scher2026research
"Verifying Restrictions on Frontier AI Research". A. Scher. arXiv:2606.28694 (27 Jun 2026). Opened
2026-11-27 (abstract page only).

- "AI progress depends primarily on compute, algorithms, and data"; catalogs "28 candidate verification
  mechanisms" for research restrictions; "a durable halt would address all three so that advances in
  one input do not counteract restrictions on another." The abstract does not mention breakout time or
  detecting automated research.
- **Bears on:** A3, D6 (all inputs must be held, close to the closure framing), protocol "closed loops".

### miotti2025narrowpath
"A Narrow Path: How to secure our future". A. Miotti, T. Bilge, D. Kasten, J. Newport. April 2025,
V1.2.0 (the PDF opened; earlier versions were not checked). URL: https://pdf.narrowpath.co/A_Narrow_Path.pdf.
Opened 2026-11-27 (PDF text and site).

- Goal of Phase 0: prevent the development of artificial superintelligence "for 20 years". Conditions:
  "No AIs improving AIs", "No AIs capable of breaking out of their environment", "No unbounded AIs",
  "Limit the general intelligence of AI systems".
- "The direct use of found systems to build new found systems, or improve existing found systems, is
  prohibited" ("found systems": software produced by optimisation, not written by humans).
- Licensing: Training License above "10^25 FLOP"; Compute License for data centres "above a threshold
  of 10^17 FLOP/s".
- **Breakout-time design (Phase 0 and Annex 2):** thresholds target "the speed at which models are
  trained, using the performance of computing clusters in FLOP/second" so as "to limit the breakout
  time to attain dangerous capabilities ... providing time for authorities to intervene", using
  "Cumulative training compute [FLOP] = Computing power [FLOP/s] * Time [s]". Annex 2: "a difference in
  order of magnitude of 8 between the Upper Limit Compute limit and the Medium Limit Computing Cluster
  limit, meaning that it would take a licensed cluster 3.2 years to breach the Upper Limit in an
  illegal training run, giving authorities ample time to intervene", while permitted models train
  "within 12 days" (6 orders of magnitude).
- "Any AI system that passes a general intelligence benchmarking test is considered to be equivalent to
  having breached the Upper Compute Limit"; the benchmark is not specified. Phase 2 calls for "a robust
  science and metrology of intelligence".
- **Weaknesses:** breakout time counts only the speed of one cluster at fixed algorithms; the
  intervention time is asserted ("ample"), not derived; no loop gain.
- **Bears on:** D3 and D4 (the closest prior design: thresholds chosen so breakout time exceeds
  intervention time), D6 and D2 (categorical ban on AI improving AI), P1.

### aguirre2025ktfh
"Keep the Future Human: Why and How We Should Close the Gates to AGI and Superintelligence, and What We
Should Build Instead". A. Aguirre. arXiv:2311.09452 (v4, 7 Mar 2025). Opened 2026-11-27 (PDF text).

- AGI as "the intersection of three key properties: high Autonomy (independence of action), high
  Generality (broad scope and adaptability), and high Intelligence (competence at cognitive tasks)".
- "full" AGI: "an AI system that is able to perform essentially all human cognitive tasks at or above
  top human expert level"; "No human has this type of intelligence; rather it is the type of
  intelligence that large collections of top human experts would have if combined." "We can term
  'superintelligence' a capability that goes beyond this".
- Measures: report total FLOP and FLOP/s for models "above a threshold of 10^25 FLOP or 10^18 FLOP/s";
  hard caps on "the total compute going into any AI model output, starting at 10^27 FLOP" and on "the
  compute rate of AI model outputs, starting at 10^20 FLOP/s"; later phases with "cryptographically
  attested total FLOP and FLOP/s attached to each model output"; enhanced liability for systems at the
  triple intersection.
- **Bears on:** D1 (collective-expert baseline, close to D1's organisation baseline), F1 (a rate cap
  limits speed), A2 (the cap counts inference, not only training), P1.

### hendrycks2025superintelligence
"Superintelligence Strategy: Expert Version". D. Hendrycks, E. Schmidt, A. Wang. arXiv:2503.05628 (v2, 14
Apr 2025). Opened 2026-11-27 (PDF text).

- "An 'intelligence recursion' refers to fully autonomous AI research and development, distinct from
  current AI-assisted AI R&D"; illustration: an AI at "100 times the pace of a human", copied "10,000
  times"; "Even if an intelligence recursion achieves only a tenfold speedup overall, we could condense a
  decade of AI development into a year."
- MAIM: "states will act to disable threatening AI projects, producing a deterrence dynamic that might
  be called Mutual Assured AI Malfunction"; stabilisers include escalation ladders, datacentre
  transparency and verification.
- **Bears on:** D2 (recursion framed by speed-up factor), D3/D4 (deterrence needs detection before a
  rival's recursion completes), O2, F1 (speed and copies).

### openai2023governance
"Governance of superintelligence". S. Altman, G. Brockman, I. Sutskever (OpenAI), May 22, 2023. URL:
https://openai.com/index/governance-of-superintelligence/. Opened 2026-11-27.

- "we are likely to eventually need something like an IAEA for superintelligence efforts"; "any effort
  above a certain capability (or resources like compute) threshold" would be subject to an
  international authority; "Tracking compute and energy usage could go a long way"; development "below
  a significant capability threshold" should be allowed without such regulation.
- **Bears on:** the memo's organising idea (the IAEA analogy and a capability line separating useful AI
  from the regulated path is prior work), P4, O3.

### hwp-2026
"The Feasibility of a Hardwired Pause of Frontier AI Training". Working Group on AI Pause Feasibility
(organisers W. Fithian, W. H. Holliday, UC Berkeley; members include R. Gottemoeller, S. Russell, D.
Krueger and others). Working paper v1.0.2, October 26, 2026 (v1.0 October 9, 2026). URL:
https://hardwired-pause.ai/paper. Opened 2026-11-27 (full HTML text searched).

- Defines per state and compute source "the covert evasion capacity K_E(c,s)" and "the overt breakout
  capacity K_B(c,s)" in H100e, discounted by realistic utilisation; ledgers must be kept below
  allowances times fleet thresholds.
- Fleet threshold: F_E(t) = rho_E * C_E(t) / (T_E * U_F), "defined relative to strategic time horizons
  T_E and T_B within which an evader is attempting to train a model"; breakout analogous.
- Section 6.2.3: a defector "would in particular require it to attain its decisive advantage before the
  rest of the world could react to stop it ... To reflect the time sensitivity of the breakout strategy,
  we adopt a breakout time horizon of T_B = 2 years." Near-term scenario: C_F(0) = 2x10^27 FLOP, beta_B
  = 100, rho_B = 12, U_F = 0.21, giving F_B = 180M H100e; a one-year horizon gives 350M or 73M H100e in
  two variants. 1 H100e = 989 TFLOP/s, about 3.1x10^22 FLOP a year.
- Section 6.5.2: "If 57% annual training efficiency gains accrued in the 26 months" before inference-only
  chips ship at scale, US overt breakout capacity as a fraction of F_B "would rise from 20% to 53%".
  Research overhead: frontier R&D budgets "ten times as large as their model training budgets" (citing
  Denain and Wu 2026).
- The research-overhead factor is a fixed multiplier; the paper does not model AI-automated research
  inside breakout. T_B is chosen by judgement and negotiation, not computed from a measured detection
  and response time.
- **Bears on:** D3 (breakout computed from holdings with efficiency growth), D4 (the horizon is the
  reaction time, so the structure T_b > T_r is already the design rule), P4, A3, protocol "compute",
  "defection".

## F. Prior-art hits for D2, D4, D5

### burtsev2026recursive
"Recursive Criticality of AI Self-Improvement". M. Burtsev. arXiv:2609.00137 (31 Aug 2026). Opened
2026-11-27 (abstract and HTML v1).

- "We derive a recursive reproduction number, R_AI, that determines whether improvements are amplified
  or damped across development cycles"; "When R_AI > 1, the effects of improvements compound across
  development cycles".
- Eq. 8: R_AI = g / sigma = chi * a / sigma; a is the recursive gain from research capability to
  subsequent research productivity; chi in [0,1] is "operational closure", the fraction of potential
  gain transmitted through the development pipeline; sigma is frontier hardness, the rate at which
  improvement productivity declines with capability. Illustrative cycle delay tau = 0.5 yr.
- The transition "need not occur at any particular level of model capability"; a system "can therefore
  enter a self-amplifying regime before acceleration becomes visible."
- No estimation procedure and no empirical estimate of R_AI; no governance proposal.
- **Bears on:** D2 (the compounding condition as a threshold quantity), D6 ("operational closure" as a
  measured fraction), Y2, Y3.

### wijk2024rebench
"RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts". H.
Wijk, T. Lin, J. Becker and 20 others. arXiv:2411.15114 (v2, 27 May 2025). Opened 2026-11-27 (abstract).

- 7 environments; 71 eight-hour attempts by 61 human experts. At a 2-hour total budget the best agents
  scored about 4x higher than experts; at 8 hours humans narrowly exceeded agents; at 32 total hours
  humans reached about 2x the top agent. Agents work "at much lower cost" (not quantified).
- **Bears on:** D1 (matched wall-clock comparison against experts already exists; matched cost does
  not), D2 (test design), F2.

### zhao2025speedrun
"The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements". B. Zhao, D. Magka, M.
Jiang, X. Li, R. Raileanu et al. (23 authors). arXiv:2506.22419 (v2, 30 Jun 2025). Opened 2026-11-27
(abstract).

- 19 tasks from NanoGPT speedrun records; agents get the previous record's script and hints; "recent
  reasoning LLMs combined with SoTA scaffolds struggle to reimplement already-known innovations".
- **Bears on:** D2 test (b): an existing harness for agents improving a small model's training recipe
  at fixed compute.

### greenblatt2024password
"Stress-Testing Capability Elicitation With Password-Locked Models". R. Greenblatt, F. Roger, D.
Krasheninnikov, D. Krueger. arXiv:2405.19550 (29 May 2024). Opened 2026-11-27 (abstract).

- "a few high-quality demonstrations are often sufficient to fully elicit password-locked
  capabilities"; RL is "still often able to elicit capabilities" without demonstrations; fine-tuning
  may be "unreliable when high-quality demonstrations are not available".
- **Bears on:** D5 (the model organism D5 proposes; the failure mode is capability beyond human
  demonstrations, which is exactly the superhuman regime).

### taylor2025auditing
"Auditing Games for Sandbagging". J. Taylor, S. Black, D. Bowen and 10 others. arXiv:2512.07810 (8 Dec
2025). Opened 2026-11-27 (abstract).

- Red team fine-tuned five models, some conditionally underperforming; the blue team "could not
  reliably discriminate sandbaggers from benign models"; training-based elicitation "consistently
  elicited full performance from the sandbagging models" with a single correct demonstration, but was
  "prone to false-positives" because benign models were also boosted.
- **Bears on:** D5 (elicited-score triggers catch sandbaggers but raise benign scores too, so an
  elicited threshold must be calibrated against benign uplift).

### barnett2024evaluations
"What AI evaluations for preventing catastrophic risks can and cannot do". P. Barnett, L. Thiergart.
arXiv:2412.08653 (26 Nov 2024). Opened 2026-11-27 (abstract).

- "Evaluations can establish lower bounds on AI capabilities"; limitations include "an inability to
  establish upper bounds on capabilities", inability to "reliably forecast future model capabilities"
  or "robustly assess risks from autonomous AI systems"; these "cannot be overcome within the current
  paradigm".
- **Bears on:** D5 (an elicited score is still a lower bound; D5's guarantee must be stated against a
  fixed elicitation budget, not as an upper bound), D4 (T_b from evaluations is optimistic).

### bukkapatnam2026absent
"When Can We Conclude a Dangerous Capability is Absent? Statistical Foundations for AI Capability
Evaluation". K. Bukkapatnam, S. Karuturi. ICML 2026, Second Workshop on Technical AI Governance Research
(poster). URL: https://icml.cc/virtual/2026/78563. Opened 2026-11-27 (abstract page).

- "We formalise the problem of negative capability claims as a one-sided hypothesis test" (n trials, k
  successes, threshold p_0); sequential test "achieves the same guarantees with up to 40% fewer trials
  on average when the capability is truly absent"; "several widely-cited evaluations reporting negative
  capability findings are statistically underpowered."
- **Bears on:** D5 (the "stated miss rate" part has direct statistical prior work), protocol "the line".

### gomez2026escalation
"Designing escalation criteria for international AI incident response: criteria, triggers, and
thresholds". F. Gomez, M. Ball, M. Harre, L. Preston, J. Schwab, C. Machado. arXiv:2604.23183 (v2, 19 May
2026). Opened 2026-11-27 (abstract).

- Derives eight escalation criteria from SB 53, the EU AI Act, the Code of Practice and other
  industries; warns that "where escalation requires confirmed harm, events such as model weight
  exfiltration risk detection only after severe, irreversible harm has propagated". No time-based
  (breakout versus detection) trigger in the abstract.
- **Bears on:** D4 search (a near miss: response criteria, not a timeliness line), T_r (escalation
  latency is a component of response time).

## G. Nuclear safeguards reference used for D4

### iaea-glossary-2022
"IAEA Safeguards Glossary, 2022 Edition", International Nuclear Verification Series No. 3 (Rev. 1).
International Atomic Energy Agency, 2022. URL (copy hosted by Brookhaven National Laboratory):
https://www.bnl.gov/ispo/docs/iaea-sgs-glossary.pdf. Opened 2026-11-27 (PDF text).

- 3.20: "Conversion time. The time required to convert different forms of nuclear material into the
  metallic components of a nuclear explosive device. Conversion time is used to determine timely
  detection requirements under the Safeguards Criteria." Assumes all facilities exist and processes are
  tested; excludes transport and assembly.
- Table 2 conversion times: Pu, HEU or U-233 metal "Order of days (7-10)"; pure compounds and MOX
  "Order of weeks (1-3)"; in irradiated fuel "Order of months (1-3)"; uranium below 20% U-235 and
  thorium "Order of months (3-12)".
- 3.21: "Detection time. An estimate of the time available for detection of a step in an acquisition
  path ... a parameter used in the planning of the frequency of safeguards measures".
- **Bears on:** D3 (conversion time is the nuclear analogue of breakout time, estimated under
  best-case assumptions for the proliferator, as D3 proposes), D4 (the timeliness rule that D4
  transplants; the transplant, not the rule, is what could be new).

## Numbers for the ledger

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| eu-systemic-risk-presumption-flop | 1e25 | FLOP (training, cumulative) | spec | eu-ai-act-2024 | Art. 51(2) |
| eu-gpai-indicative-flop | 1e23 | FLOP (training) | spec | ec-gpai-guidelines-faq-2025 | GPAI definition FAQ |
| eu-modifier-compute-fraction | 0.333 | fraction of original training compute | spec | ec-gpai-guidelines-faq-2025 | downstream modifier FAQ |
| eu-notification-deadline | 14 | days | spec | eu-ai-act-2024 | Art. 52(1) ("two weeks") |
| eu-high-impact-business-users | 10000 | registered EU business users | spec | eu-ai-act-2024 | Annex XIII(f) |
| eu-cop-expected-providers-low | 5 | providers | assumption | gpai-code-of-practice-2025 | Chairs' statement |
| eu-cop-expected-providers-high | 15 | providers | assumption | gpai-code-of-practice-2025 | Chairs' statement |
| us-eo14110-model-ops | 1e26 | operations (training) | spec | eo14110-2023 | Sec. 4.2(b)(i) (revoked) |
| us-eo14110-bio-ops | 1e23 | operations (training, biological sequence data) | spec | eo14110-2023 | Sec. 4.2(b)(i) |
| us-eo14110-cluster-rate | 1e20 | operations per second | spec | eo14110-2023 | Sec. 4.2(b)(ii) |
| us-eo14110-cluster-network | 100 | Gbit/s | spec | eo14110-2023 | Sec. 4.2(b)(ii) |
| us-eo14110-revoked | 2025-01-20 | date | spec | eo14148-2025 | Sec. 2(ggg) |
| ca-sb53-frontier-ops | 1e26 | operations (training incl. fine-tuning) | spec | ca-sb53-analysis-2025 | definitions (h) |
| ca-sb53-large-developer-revenue | 5e8 | USD per year | spec | ca-sb53-analysis-2025 | definitions (i) |
| ca-sb53-catastrophe-casualties | 50 | people (more than) | spec | ca-sb53-analysis-2025 | definitions (b) |
| ca-sb53-catastrophe-damage | 1e9 | USD (more than) | spec | ca-sb53-analysis-2025 | definitions (b) |
| ca-sb53-incident-report-days | 15 | days | spec | fpf-sb53-2025 | incident reporting |
| ca-sb53-incident-report-imminent | 24 | hours | spec | fpf-sb53-2025 | incident reporting |
| ca-sb1047-cost-threshold | 1e8 | USD training cost (vetoed bill) | spec | ca-sb53-analysis-2025 | comment 5 |
| ny-raise-frontier-ops | 1e26 | operations (training) | spec | ny-a9449-2026 | sec. 9(a) |
| anthropic-aird-cost-factor | 5 | ratio of AI cost to human staff cost | vendor | anthropic-rsp-v3-4 | Section 1 table, automated R&D |
| anthropic-aird-acceleration | 2 | ratio of progress rates | vendor | anthropic-rsp-v3-4 | Section 1 table and fn. 8 |
| anthropic-aird-example-baseline-scaleup | 9 | effective scaleup per year (example) | vendor | anthropic-rsp-v3-4 | fn. 8 |
| anthropic-aird-example-doubled-scaleup | 81 | effective scaleup per year (example) | vendor | anthropic-rsp-v3-4 | fn. 8 |
| anthropic-aird-baseline-generations | 3 | model generations (minimum) | vendor | anthropic-rsp-v3-4 | fn. 9 |
| anthropic-eval-cadence-compute | 4 | x effective compute | vendor | anthropic-rsp-v3-4 | changelog v2.0 |
| anthropic-eval-cadence-months | 6 | months | vendor | anthropic-rsp-v3-4 | changelog v2.0 |
| anthropic-v1-elicitation-compute-share | 0.01 | fraction of compute (removed in v2.0) | vendor | anthropic-rsp-v3-4 | changelog v2.0 |
| anthropic-v1-buffer | 6 | x effective compute buffer (removed in v2.0) | vendor | anthropic-rsp-v3-4 | changelog v2.0 |
| metr-anthropic-acceleration | 1.9 | ratio of capability growth rates | measured | metr-anthropic-acceleration-2026 | headline estimates |
| metr-anthropic-acceleration-ci-low | 1.5 | ratio (95% CI lower) | measured | metr-anthropic-acceleration-2026 | headline estimates |
| metr-anthropic-acceleration-ci-high | 2.8 | ratio (95% CI upper) | measured | metr-anthropic-acceleration-2026 | headline estimates |
| metr-aeci-historical-rate | 15 | AECI points per year | measured | metr-anthropic-acceleration-2026 | what was measured |
| metr-aeci-recent-rate | 29 | AECI points per year (after Oct 2025) | measured | metr-anthropic-acceleration-2026 | what was measured |
| metr-ai-attribution | 0.8 | fraction of acceleration due to AI (subjective) | assumption | metr-anthropic-acceleration-2026 | headline estimates |
| openai-critical-speedup | 5 | x speed of 2024 generational improvement | vendor | openai-preparedness-v2-2025 | Table, AI Self-improvement Critical |
| openai-critical-generation-weeks | 4 | weeks per generation at Critical (example) | vendor | openai-preparedness-v2-2025 | same |
| xai-mask-dishonesty-max | 0.5 | dishonesty rate on MASK | vendor | xai-rmf-2025 | Loss of control thresholds |
| xai-bio-answer-rate-max | 0.05 | answer rate on restricted bio queries | vendor | xai-rmf-2025 | Malicious use thresholds |
| morris-level-competent | 50 | percentile of skilled adults | design | morris2023levels | Table 1 |
| morris-level-expert | 90 | percentile of skilled adults | design | morris2023levels | Table 1 |
| morris-level-exceptional | 99 | percentile of skilled adults | design | morris2023levels | Table 1 |
| agi-score-gpt4 | 0.27 | fraction of AGI score | measured | hendrycks2025agi | abstract |
| agi-score-gpt5 | 0.57 | fraction of AGI score | measured | hendrycks2025agi | abstract |
| bostrom-brain-ops-low | 1e14 | operations per second | assumption | bostrom1998long | hardware section |
| bostrom-brain-ops-high | 1e17 | operations per second | assumption | bostrom1998long | hardware section |
| miri-strict-threshold | 1e24 | FLOP (training) | design | scher2025agreement | Art. II def. 8 |
| miri-post-training-threshold | 1e23 | FLOP | design | scher2025agreement | Art. II def. 9 |
| miri-monitored-threshold | 1e22 | FLOP | design | scher2025agreement | Art. II def. 10 |
| miri-ccc-h100e | 16 | H100-equivalents | design | scher2025agreement | Art. II def. 16 |
| miri-ccc-tflops | 15840 | TFLOP/s | design | scher2025agreement | Art. II def. 16 |
| miri-ccc-bandwidth | 25 | Gbit/s inter-node | design | scher2025agreement | Art. II def. 16 |
| miri-withdrawal-notice | 12 | months | design | scher2025agreement | notes on withdrawal |
| miri-consolidation-days | 120 | days | design | scher2025agreement | Art. V (Chip Consolidation) para. 3 |
| miri-deepseek-v3-flop | 3e24 | FLOP (training) | vendor | scher2025agreement | notes on Art. IV (secondary) |
| miri-algorithmic-progress | 3 | x per year reduction in compute for fixed capability | measured | scher2025agreement | Section 5 (citing Ho et al. 2024; secondary) |
| miri-detectable-dc-h100e | 10000 | H100-equivalents (smallest locatable by intelligence services) | assumption | scher2025agreement | notes on Art. V, feasibility |
| miri-hard-to-hide-dc-h100e | 100000 | H100-equivalents | assumption | scher2025agreement | notes on Art. V, feasibility |
| narrowpath-training-license-flop | 1e25 | FLOP | design | miotti2025narrowpath | Policy 5(a) |
| narrowpath-compute-license-rate | 1e17 | FLOP/s | design | miotti2025narrowpath | Policy 5(b) |
| narrowpath-breakout-oom-gap | 8 | orders of magnitude (compute limit / cluster limit, in seconds) | design | miotti2025narrowpath | Annex 2 |
| narrowpath-breakout-years | 3.2 | years | design | miotti2025narrowpath | Annex 2 |
| narrowpath-permitted-run-days | 12 | days | design | miotti2025narrowpath | Annex 2 |
| narrowpath-pause-years | 20 | years | design | miotti2025narrowpath | Phase 0 |
| ktfh-output-compute-cap | 1e27 | FLOP per model output (training plus inference) | design | aguirre2025ktfh | measure 2 |
| ktfh-output-rate-cap | 1e20 | FLOP/s | design | aguirre2025ktfh | measure 2 |
| ktfh-reporting-flop | 1e25 | FLOP | design | aguirre2025ktfh | measure 1 |
| ktfh-reporting-rate | 1e18 | FLOP/s | design | aguirre2025ktfh | measure 1 |
| hwp-breakout-horizon | 2 | years | assumption | hwp-2026 | Section 6.2.3 |
| hwp-frontier-compute-at-pause | 2e27 | FLOP | assumption | hwp-2026 | Section 6.2.3 |
| hwp-breakout-multiple | 100 | ratio to frozen frontier compute | design | hwp-2026 | Section 6.2.3 |
| hwp-research-overhead-breakout | 12 | ratio (R&D compute to final run) | design | hwp-2026 | Section 6.2.3 |
| hwp-frontier-utilisation | 0.21 | fraction | assumption | hwp-2026 | Section 6.2.3 |
| hwp-breakout-fleet-threshold | 1.8e8 | H100e | design | hwp-2026 | Section 6.2.3 |
| hwp-h100e-rate | 989 | TFLOP/s | spec | hwp-2026 | Section 3 |
| hwp-training-efficiency-gain | 0.57 | fraction per year | assumption | hwp-2026 | Section 6.5.2 |
| hwp-rd-to-training-budget | 10 | ratio | assumption | hwp-2026 | Section 6.2 (citing Denain and Wu 2026; secondary) |
| iaea-conversion-metal-days-low | 7 | days | spec | iaea-glossary-2022 | Table 2 |
| iaea-conversion-metal-days-high | 10 | days | spec | iaea-glossary-2022 | Table 2 |
| iaea-conversion-irradiated-months-low | 1 | months | spec | iaea-glossary-2022 | Table 2 |
| iaea-conversion-irradiated-months-high | 3 | months | spec | iaea-glossary-2022 | Table 2 |
| iaea-conversion-leu-months-high | 12 | months | spec | iaea-glossary-2022 | Table 2 |
| rebench-human-experts | 61 | experts | measured | wijk2024rebench | abstract |
| rebench-agent-advantage-2h | 4 | ratio of agent to human score at 2 h | measured | wijk2024rebench | abstract |
| rebench-human-advantage-32h | 2 | ratio of human to agent score at 32 h | measured | wijk2024rebench | abstract |
| hooker-inference-gain-low | 5 | x post-training performance | measured | hooker2024limits | Section 3.1.1 |
| hooker-inference-gain-high | 20 | x post-training performance | measured | hooker2024limits | Section 3.1.1 |
| heim-posttraining-equiv-low | 5 | x compute-equivalent | measured | heim2024compute | limitations (citing prior work) |
| heim-posttraining-equiv-high | 20 | x compute-equivalent | measured | heim2024compute | limitations (citing prior work) |
| sprt-trial-saving | 0.4 | fraction fewer trials (up to) | measured | bukkapatnam2026absent | abstract |
| burtsev-cycle-delay | 0.5 | years (illustrative) | assumption | burtsev2026recursive | Section 3.2 |
| seoul-signatories | 20 | companies | spec | seoul-commitments-2024 | page |
| fli-statement-signatories | 79159 | signatures (on 2026-11-27) | measured | fli-superintelligence-statement | page |

## Prior art for the memo's candidates

These judgements are claims about this track's search, not about the world.

### D1 (superintelligence against the best organisation, matched time and budget)
- **Closest:** anthropic-rsp-v3-4 (substitute "our entire set of Research Scientists and Research
  Engineers, at competitive costs (i.e., within a factor of 5)"; "large, top-tier teams of human
  researchers"); gdm-fsf-v3-1-2026 ("any team of researchers at Google ... approximately comparable
  all-inclusive costs"); wijk2024rebench (matched wall-clock budgets against 61 experts); aguirre2025ktfh
  ("large collections of top human experts ... if combined"); barnett2025governance ("substantially
  surpass humanity in all strategically relevant activities"); scher2025agreement (harm-based
  operational ASI plus a presumption rule); morris2023levels (individual percentiles).
- **Searches:** "Levels of AGI" definitions; "definition of superintelligence" 2025 2026; "fully
  automate the work of any team of researchers"; RE-Bench human expert time budget; frontier framework
  AI R&D thresholds (METR common elements).
- **Judgement: extends prior work (memo's label stands), but the differentiation is narrower than the
  memo says.** Comparing against teams or the whole research staff at matched cost is already industry
  practice for AI R&D, and matched time is in RE-Bench. Not found: a multi-domain battery against the
  best human organisation with time, budget, copies and speed all matched, and an alpha-fraction rule.

### D2 (loop gain as a trigger)
- **Closest:** anthropic-rsp-v3-4 (trigger at a doubling of the rate of progress attributable to
  automated R&D, with the v3.4 rule that constant or slowing progress does not count, "intended to
  capture the onset of dramatic recursive self-improvement"); openai-preparedness-v2-2025 (generation
  in 1/5 the 2024 wall-clock time, sustained for months); gdm-fsf-v3-1-2026 (acceleration level 1);
  metr-anthropic-acceleration-2026 (measured 1.9x, 95% CI 1.5 to 2.8x, bootstrap); burtsev2026recursive
  (R_AI = chi * a / sigma > 1); hendrycks2025superintelligence (recursion speed-up framing).
- **Searches:** "returns to software R&D" r > 1 threshold governance; recursive self-improvement trigger
  metric; "loop gain" AI R&D trigger; automated AI R&D thresholds across frameworks; NanoGPT speedrun
  agents benchmark.
- **Judgement: prior work for the condition and for its use as a trigger; extends prior work at most
  for the estimator.** Two differences remain and should be stated precisely: (i) D2's g is the ratio
  of successive capability gains with human-held inputs (compute, data) fixed, whereas the industry
  triggers and METR's estimate are ratios of overall progress rates with inputs free; (ii) Burtsev
  defines the critical quantity but gives no estimation procedure. A staged fixed-compute run with a
  confidence bound on g (memo test b) was not found; zhao2025speedrun is an existing harness for it.

### D3 (breakout time computed from holdings)
- **Closest:** miotti2025narrowpath (breakout from cluster caps: 3.2 years), hwp-2026 (breakout fleet
  thresholds from training budget, research overhead, utilisation and horizon, with 57%/yr efficiency
  growth), barnett2025governance (definition; AI R&D automation makes breakout "very short, even given
  limited compute"), scher2025agreement, iaea-glossary-2022 (conversion time under best-case
  assumptions).
- **Searches:** "breakout time" AI compute governance detection response; AI breakout time treaty
  verification; IAEA conversion time AI analogy.
- **Judgement: extends prior work.** Breakout time computed from compute holdings is prior work
  (A Narrow Path, hardwired pause). Not found: breakout time that includes a measured loop-gain term
  (AI research labour) alongside physical compute and measured algorithmic efficiency.

### D4 (weapons-grade line T_b < m * T_r)
- **Closest:** barnett2025governance ("nations must be able to detect and respond to dangerous AI
  development faster than any single country's breakout time"); miotti2025narrowpath (thresholds sized
  so breakout gives "authorities ample time to intervene"); hwp-2026 (T_B as the time before the world
  "could react", fleet thresholds derived from it); meta-ssf-v2-1-2026 (LoC 1: development faster than
  evaluation); gdm-fsf-v3-1-2026 (buffer tied to rate of progress); openai2023governance (a threshold
  separating regulated efforts, IAEA analogy); iaea-glossary-2022 (detection timeliness from conversion
  time).
- **Searches:** "breakout time" AI governance detection response time; AI governance IAEA safeguards
  analogy timely detection conversion time; "weapons-grade" AI threshold useful AI line; detection
  time versus development time AI regulation; escalation criteria AI incident response.
- **Judgement: extends prior work, not new.** This contradicts the memo. The inequality (detect and
  respond faster than breakout) and threshold design around it are in the literature from 2025 to
  2026. Not found: (i) using the inequality as the *definition* of the line between useful AI and the
  path to superintelligence, applied to systems and holdings; (ii) an explicit margin m; (iii) a T_r
  derived from the regime's own measured detection channels and response latency rather than chosen;
  (iv) T_b including loop gain. The paper should credit Barnett and Scher, A Narrow Path and the
  hardwired-pause group, and claim only (i) to (iv).

### D5 (elicited capability, robust to hiding)
- **Closest:** gpai-code-of-practice-2025 (Appendix 3.2: state-of-the-art elicitation, match misuse
  actors, guard against sandbagging); openai-preparedness-v2-2025 (elicitation as a lower bound;
  "conservative upper bound" for sandbagging); anthropic-rsp-v3-4 (1% compute elicitation budget and
  6x buffer, removed in 2024); gdm-fsf-v3-1-2026; greenblatt2024password; taylor2025auditing;
  barnett2024evaluations; bukkapatnam2026absent.
- **Searches:** password-locked models capability elicitation sandbagging detection regulatory
  threshold; "When Can We Conclude a Dangerous Capability is Absent"; elicitation budget frontier
  framework.
- **Judgement: extends prior work (memo's label stands).** A fixed, stated elicitation budget existed
  (Anthropic RSP v1) and was dropped; the EU expects elicitation matched to adversaries; one-sided
  statistical tests for absence exist. Not found: a threshold judged on the score a fixed elicitation
  budget recovers, with a measured miss rate on password-locked organisms. Evidence against: training-
  based elicitation also lifts benign models (false positives), and fine-tuning fails without
  high-quality demonstrations, the regime where superhuman capability lives.

### D6 (closure per input)
- **Closest:** burtsev2026recursive ("operational closure" chi, the fraction of potential gain
  transmitted through the pipeline); miotti2025narrowpath (no "found systems" building found systems);
  scher2026research (all three inputs must be held); redlines-2025 (self-replication or
  self-improvement without human authorisation).
- **Searches:** as for D2, plus "closed loop" AI governance inputs; operational closure AI R&D.
- **Judgement: extends prior work for research labour; the per-input list may be framing.** Burtsev
  already names and parameterises closure for the research loop. Not found: closure assessed input by
  input (compute, weights, data, research labour, money) against verifiable human-held gates.

### P4 (footprint floor)
- **Closest in this track:** scher2025agreement (data centres above 100,000 H100e "hard to hide";
  locatable down to about 10,000 H100e, stated without derivation); hwp-2026 (covert evasion capacity
  ledgers); eo14110-2023 and miotti2025narrowpath (cluster-rate thresholds at 10^20 and 10^17 FLOP/s).
- **Judgement: not found in this track.** No source computes a physical footprint floor; other tracks
  (physical, verification) should search further.

## Sources (TOML)

```toml
[source.anthropic-rsp-v3-4]
type = "vendor"
title = "Responsible Scaling Policy, Version 3.4"
authors = "Anthropic"
year = 2026
url = "https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf"
opened = "2026-11-27"

[source.anthropic-rsp-page-2026]
type = "vendor"
title = "Anthropic's Responsible Scaling Policy (policy page and update log)"
authors = "Anthropic"
year = 2026
url = "https://www.anthropic.com/rsp"
opened = "2026-11-27"

[source.anthropic-rsp-v3-announcement-2026]
type = "vendor"
title = "Anthropic's Responsible Scaling Policy, Version 3.0"
authors = "Anthropic"
year = 2026
url = "https://www.anthropic.com/news/responsible-scaling-policy-v3"
opened = "2026-11-27"

[source.openai-preparedness-v2-2025]
type = "vendor"
title = "Preparedness Framework, Version 2"
authors = "OpenAI"
year = 2025
url = "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
opened = "2026-11-27"

[source.gdm-fsf-v3-1-2026]
type = "vendor"
title = "Frontier Safety Framework, Version 3.1"
authors = "Google DeepMind"
year = 2026
url = "https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf"
opened = "2026-11-27"

[source.meta-ssf-v2-1-2026]
type = "vendor"
title = "Meta Superintelligence Scaling Framework, Version 2.1"
authors = "Meta"
year = 2026
url = "https://research.meta.ai/static/meta-superintelligence-scaling-framework"
opened = "2026-11-27"

[source.xai-rmf-2025]
type = "vendor"
title = "xAI Risk Management Framework"
authors = "xAI"
year = 2025
url = "https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf"
opened = "2026-11-27"

[source.metr-common-elements-2025]
type = "report"
title = "Common Elements of Frontier AI Safety Policies"
authors = "METR"
year = 2025
url = "https://metr.org/common-elements"
opened = "2026-11-27"

[source.metr-anthropic-acceleration-2026]
type = "report"
title = "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026"
authors = "METR (Tom Cunningham, Nate Rush, Parker Whitfill, Hjalmar Wijk)"
year = 2026
url = "https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/"
opened = "2026-11-27"

[source.morris2023levels]
type = "peer-reviewed"
title = "Levels of AGI for Operationalizing Progress on the Path to AGI"
authors = "Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, Shane Legg"
year = 2024
arxiv = "2311.02462"
doi = "10.48550/arXiv.2311.02462"
opened = "2026-11-27"

[source.hendrycks2025agi]
type = "preprint"
title = "A Definition of AGI"
authors = "Dan Hendrycks, Dawn Song, Christian Szegedy, et al."
year = 2025
arxiv = "2510.18212"
opened = "2026-11-27"

[source.bostrom1998long]
type = "peer-reviewed"
title = "How Long Before Superintelligence?"
authors = "Nick Bostrom"
year = 1998
url = "https://nickbostrom.com/superintelligence"
opened = "2026-11-27"

[source.eu-ai-act-2024]
type = "legislation"
title = "Regulation (EU) 2024/1689 (Artificial Intelligence Act), Articles 51 and 52 and Annex XIII"
authors = "European Parliament and Council of the European Union"
year = 2024
url = "https://artificialintelligenceact.eu/article/51/"
opened = "2026-11-27"

[source.ec-gpai-guidelines-faq-2025]
type = "official-docs"
title = "Guidelines for providers of general-purpose AI models: General FAQ"
authors = "European Commission, AI Office"
year = 2025
url = "https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-gpai-providers"
opened = "2026-11-27"

[source.gpai-code-of-practice-2025]
type = "official-docs"
title = "General-Purpose AI Code of Practice: Safety and Security chapter (final version) and Chairs' statement"
authors = "Chairs and Vice-Chairs of the General-Purpose AI Code of Practice"
year = 2025
url = "https://code-of-practice.ai/?section=safety-security"
opened = "2026-11-27"

[source.eo14110-2023]
type = "legislation"
title = "Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence (88 FR 75191)"
authors = "Executive Office of the President of the United States"
year = 2023
url = "https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf"
opened = "2026-11-27"

[source.eo14148-2025]
type = "legislation"
title = "Executive Order 14148: Initial Rescissions of Harmful Executive Orders and Actions (90 FR 8237)"
authors = "Executive Office of the President of the United States"
year = 2025
url = "https://www.govinfo.gov/content/pkg/FR-2025-01-28/pdf/2025-01901.pdf"
opened = "2026-11-27"

[source.ca-sb53-analysis-2025]
type = "report"
title = "SB 53 (Wiener), as amended September 5, 2025: bill analysis"
authors = "California Assembly Committee on Privacy and Consumer Protection"
year = 2025
url = "https://apcp.assembly.ca.gov/media/1019"
opened = "2026-11-27"

[source.fpf-sb53-2025]
type = "report"
title = "California's SB 53: The First Frontier AI Law, Explained"
authors = "Justine Gluck (Future of Privacy Forum)"
year = 2025
url = "https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/"
opened = "2026-11-27"

[source.ny-a9449-2026]
type = "legislation"
title = "New York Assembly Bill A9449 (2026): chapter amendment to the RAISE Act"
authors = "New York State Assembly"
year = 2026
url = "https://legislation.nysenate.gov/pdf/bills/2025/A9449"
opened = "2026-11-27"

[source.seoul-commitments-2024]
type = "official-docs"
title = "Frontier AI Safety Commitments, AI Seoul Summit 2024"
authors = "UK Department for Science, Innovation and Technology"
year = 2024
url = "https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024"
opened = "2026-11-27"

[source.heim2024compute]
type = "preprint"
title = "Training Compute Thresholds: Features and Functions in AI Regulation"
authors = "Lennart Heim, Leonie Koessler"
year = 2024
arxiv = "2405.10799"
opened = "2026-11-27"

[source.hooker2024limits]
type = "preprint"
title = "On the Limitations of Compute Thresholds as a Governance Strategy"
authors = "Sara Hooker"
year = 2024
arxiv = "2407.05694"
opened = "2026-11-27"

[source.koessler2024risk]
type = "preprint"
title = "Risk thresholds for frontier AI"
authors = "Leonie Koessler, Jonas Schuett, Markus Anderljung"
year = 2024
arxiv = "2406.14713"
opened = "2026-11-27"

[source.fli-superintelligence-statement]
type = "essay"
title = "Statement on Superintelligence"
authors = "Future of Life Institute (host)"
undated = true
url = "https://superintelligence-statement.org/"
opened = "2026-11-27"

[source.redlines-2025]
type = "essay"
title = "Global Call for AI Red Lines"
authors = "CeSIA, The Future Society, Center for Human-Compatible AI"
year = 2025
url = "https://red-lines.ai/"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.barnett2025governance]
type = "preprint"
title = "AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research Questions"
authors = "Peter Barnett, Aaron Scher"
year = 2025
arxiv = "2505.04592"
opened = "2026-11-27"

[source.scher2026research]
type = "preprint"
title = "Verifying Restrictions on Frontier AI Research"
authors = "Aaron Scher"
year = 2026
arxiv = "2606.28694"
opened = "2026-11-27"

[source.miotti2025narrowpath]
type = "report"
title = "A Narrow Path: How to secure our future (V1.2.0)"
authors = "Andrea Miotti, Tolga Bilge, Dave Kasten, James Newport"
year = 2025
url = "https://pdf.narrowpath.co/A_Narrow_Path.pdf"
opened = "2026-11-27"

[source.aguirre2025ktfh]
type = "preprint"
title = "Keep the Future Human: Why and How We Should Close the Gates to AGI and Superintelligence, and What We Should Build Instead"
authors = "Anthony Aguirre"
year = 2025
arxiv = "2311.09452"
opened = "2026-11-27"

[source.hendrycks2025superintelligence]
type = "preprint"
title = "Superintelligence Strategy: Expert Version"
authors = "Dan Hendrycks, Eric Schmidt, Alexandr Wang"
year = 2025
arxiv = "2503.05628"
opened = "2026-11-27"

[source.openai2023governance]
type = "vendor"
title = "Governance of superintelligence"
authors = "Sam Altman, Greg Brockman, Ilya Sutskever (OpenAI)"
year = 2023
url = "https://openai.com/index/governance-of-superintelligence/"
opened = "2026-11-27"

[source.hwp-2026]
type = "report"
title = "The Feasibility of a Hardwired Pause of Frontier AI Training (working paper v1.0.2)"
authors = "Working Group on AI Pause Feasibility (organisers William Fithian, Wesley H. Holliday)"
year = 2026
url = "https://hardwired-pause.ai/paper"
opened = "2026-11-27"

[source.burtsev2026recursive]
type = "preprint"
title = "Recursive Criticality of AI Self-Improvement"
authors = "Mikhail Burtsev"
year = 2026
arxiv = "2609.00137"
opened = "2026-11-27"

[source.wijk2024rebench]
type = "preprint"
title = "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts"
authors = "Hjalmar Wijk, Tao Lin, Joel Becker, et al."
year = 2024
arxiv = "2411.15114"
opened = "2026-11-27"

[source.zhao2025speedrun]
type = "preprint"
title = "The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements"
authors = "Bingchen Zhao, Despoina Magka, Minqi Jiang, Xian Li, Roberta Raileanu, et al."
year = 2025
arxiv = "2506.22419"
opened = "2026-11-27"

[source.greenblatt2024password]
type = "preprint"
title = "Stress-Testing Capability Elicitation With Password-Locked Models"
authors = "Ryan Greenblatt, Fabien Roger, Dmitrii Krasheninnikov, David Krueger"
year = 2024
arxiv = "2405.19550"
opened = "2026-11-27"

[source.taylor2025auditing]
type = "preprint"
title = "Auditing Games for Sandbagging"
authors = "Jordan Taylor, Sid Black, Dillon Bowen, et al."
year = 2025
arxiv = "2512.07810"
opened = "2026-11-27"

[source.barnett2024evaluations]
type = "preprint"
title = "What AI evaluations for preventing catastrophic risks can and cannot do"
authors = "Peter Barnett, Lisa Thiergart"
year = 2024
arxiv = "2412.08653"
opened = "2026-11-27"

[source.bukkapatnam2026absent]
type = "preprint"
title = "When Can We Conclude a Dangerous Capability is Absent? Statistical Foundations for AI Capability Evaluation"
authors = "Kaustubh Bukkapatnam, Siddharth Karuturi"
year = 2026
url = "https://icml.cc/virtual/2026/78563"
opened = "2026-11-27"

[source.gomez2026escalation]
type = "preprint"
title = "Designing escalation criteria for international AI incident response: criteria, triggers, and thresholds"
authors = "Francesca Gomez, Matthew Ball, Michael Harre, Lydia Preston, Josephine Schwab, Caio Machado"
year = 2026
arxiv = "2604.23183"
opened = "2026-11-27"

[source.iaea-glossary-2022]
type = "official-docs"
title = "IAEA Safeguards Glossary, 2022 Edition (International Nuclear Verification Series No. 3, Rev. 1)"
authors = "International Atomic Energy Agency"
year = 2022
url = "https://www.bnl.gov/ispo/docs/iaea-sgs-glossary.pdf"
opened = "2026-11-27"
```
