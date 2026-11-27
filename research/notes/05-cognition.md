# Survey 05: cognition and function

- Track: 05, cognitive and functional (F1 to F3, D1).
- Date: 2026-11-27. Every source below was opened on this date unless the entry says otherwise.
- Scope: benchmarks with expert, team or institutional baselines (science QA, mathematics, software,
  AI research engineering, cyber, biology, persuasion, forecasting, economically valuable work);
  typologies and definitions of AGI and superintelligence; narrow superhuman systems; measures of
  economic work; time, cost and team accounting; saturation, contamination and refreshed batteries.

## Summary: what matters for Subcritical

1. **D1's comparison against organisations is prior work, and so is counting copies and speed.**
   Genewein et al. 2026 (Google DeepMind, "From AGI to ASI") define ASI as exceeding "large
   human-expert collectives": tens of thousands of coordinated experts working 10 years with 2010
   technology, beaten in a tenth of the time, where one ASI "may consist of a collective of millions
   of instances". Ngo 2023 defines (t,n)-AGI against "any group of n humans working together" for
   time t, and calls superintelligence a "(1 year, 8 billion)-AGI". Anthropic's RSP v3.4 (July 2026)
   sets its automated-AI-R&D threshold at substituting for its "entire set of Research Scientists
   and Research Engineers, at competitive costs (i.e., within a factor of 5)". OpenAI's Preparedness
   Framework v2 uses "1/5th the wall-clock time". AI 2027 counts 30x copies at 30x speed on 5% of
   compute. What D1 may still add: matching budget (compute and money) as part of the definition, a
   refreshed held-out battery with institutional baselines across decisive clusters, and the alpha
   fraction. The memo's own list of differences is mostly already covered.
2. **Who wins depends on the time budget.** RE-Bench: AI agents score 4x human experts at 2 hours,
   humans score 2x the agents at 32 hours. HCAST: agents succeed 70-80% on tasks humans finish in
   under an hour, under 20% beyond 4 hours. So D1 has to fix wall-clock time as an explicit
   parameter, as Ngo's t does.
3. **Benchmarks with expert baselines saturate in one to two years and carry many label errors.**
   GPQA Diamond: 96.8% (Nov 2026) against PhD experts at 65-74%. FrontierMath went from under 2% at
   release (Nov 2024) to 95% on Tiers 1-3 and 100% on Tier 4 (three models, Sep-Nov 2026). Cybench:
   93% unguided (vendor system card). HLE: Epoch
   found 46% of a sample defective. FrontierMath v2 corrected 42% of its problems. METR's horizon
   suite is unreliable above 16 hours and stopped being updated in Sep 2026. Fewer than a quarter of
   prominent benchmarks claim any organisational dimension of work (Barres et al. 2026).
4. **Automated scores overstate real capability.** About half of SWE-bench-passing PRs would not be
   merged by maintainers. In an RCT, early-2025 tools made experienced developers 19% slower.
   GDPval's naive 90x speed gain falls to 1.39x once review is counted. On the other side, RLI
   automation rose from 2.5% (Oct 2025) to 41% (Nov 2026).
5. **Team baselines already exist in four places:** CTF scoreboards, Kaggle leaderboards, forecasting
   pro teams, and CASP. In a 24-hour onsite CTF in 2026, an agent placed 2nd on the human scoreboard
   for about $96 of API use and about a fifth of the human runtime. Forecasting is near parity: the
   gap between Metaculus pros and bots was not significant in spring 2026, and the ForecastBench
   superforecaster median (68.1) is matched by hybrid AI entries. These are the obvious domains for
   a scaled-down D1.
6. **Against the memo:** (a) as item 1. (b) D1 needs to say whether the human organisation may use
   AI. Otherwise the baseline keeps moving, which is why Genewein et al. pin it to 2010 technology.
   (c) Persuasion already beats individual humans, including humans paid for results, but no source
   compares AI with persuasion organisations. (d) Narrow superhuman systems are cheap and brittle
   (Pluribus trained for under $150, adversarial Go wins over 97%), which supports F3. But
   AlphaEvolve, a general model working against automated evaluators, gets narrow superhuman results
   and sped up its own training. That blurs the narrow/general line exactly where D2 sits.

## Sources

**Group: Definitions and typologies**

### bostrom1998howlong
- "How Long Before Superintelligence?", Nick Bostrom, International Journal of Futures Studies, vol. 2,
  1998 (reprinted 2006). URL https://nickbostrom.com/superintelligence. Opened 2026-11-27.
- Defines superintelligence as "an intellect that is much smarter than the best human brains in
  practically every field, including scientific creativity, general wisdom and social skills."
  Implementation left open ("a digital computer, an ensemble of networked computers, cultured
  cortical tissue").
- **Excludes organisations:** "Entities such as companies or the scientific community are not
  superintelligences" under this definition. So the benchmark is the best individual brain.
- "Weak superintelligence" is "an intellect that has about the same abilities as a human brain but
  is much faster". Skills may be copied between artificial intellects, whose achievements are
  "additive".
- Bears on: D1 (the canonical comparison is with individuals, and organisations are explicitly
  excluded, which D1 reverses), F1 (speed as a separate kind).

### grace2014forms
- "Superintelligence 5: Forms of superintelligence", Katja Grace, LessWrong reading group on
  Bostrom's *Superintelligence* (2014), posted 2014-10-14. URL
  https://www.lesswrong.com/posts/semvkn56ZFcXBNc2d/superintelligence-5-forms-of-superintelligence.
  Opened 2026-11-27.
- The book itself was **not opened** (no legal full text found). This post summarises chapter 3
  with page references: speed SI "could do what a human does, but faster" (p53); collective SI "is
  composed of smaller intellects" (p54); quality SI "can carry out intellectual tasks that humans
  just can't in practice" (p56-7). A comment quotes Bostrom, truncated: "To obtain a collective
  superintelligence from any present-day collective intelligence would require a very great degree
  of".
- Bears on: F1. The speed, collective and quality typology is prior work. Cite the book only after
  someone opens it.

### yudkowsky2016superintelligent
- "Superintelligent", Eliezer Yudkowsky, Arbital, 2016-06-06 (mirror). URL
  https://arbital.greaterwrong.com/p/superintelligent. Opened 2026-11-27.
- A superintelligence is "either 'strongly superhuman', or else at least 'optimal', across all
  cognitive domains". Its estimates should be "epistemically efficient relative to every human and
  human group" (no person or group can predict its errors), by analogy with efficient markets. It is
  not "infinitely fast".
- Bears on: D1. This is a comparison against every human group, defined by efficiency, not by a
  test battery.

### aiimpacts2016coordinated
- "Coordinated human action as example of superhuman intelligence", AI Impacts, undated (comments
  from 2016). URL https://aiimpacts.org/coordinated-human-action-example-superhuman-intelligence/.
  Opened 2026-11-27.
- Surveys experiments from 1924 to 2015: "Groups outperformed individuals, but larger groups did not
  outperform smaller groups." Mechanisms: aggregation, specialisation, markets ("Markets can be used
  to combine information from many individuals"). Caveat: human organisations "may not represent the
  full range of possible superintelligences".
- Bears on: D1. Human groups beat individuals but the gain saturates with group size, which matters
  for picking the "best available organisation".

### ngo2023tagi
- "Clarifying and predicting AGI", Richard Ngo, LessWrong / Alignment Forum, 2023-05-04. URL
  https://www.lesswrong.com/posts/BoA3agdkAzL6HQtQP/clarifying-and-predicting-agi. Opened 2026-11-27.
- t-AGI: "on most cognitive tasks, it beats most human experts who are given time t to perform the
  task." Experts, not laypeople ("it does seem important that we use experts not laypeople").
- Group extension: "(t,n)-AGIs which beat any group of n humans working together" on tasks taking
  time t. "When I think about superintelligence I'm typically thinking about (1 year, 8
  billion)-AGIs."
- Bears on: **D1 closest prior art** (group comparison, matched wall-clock time). No matched budget,
  no copies counted on the AI side, no test battery.

### morris2023levels
- "Levels of AGI for Operationalizing Progress on the Path to AGI", Morris, Sohl-Dickstein, Fiedel,
  Warkentin, Dafoe, Faust, Farabet, Legg. arXiv 2311.02462 (v5, 2025-09-24). Proceedings of ICML
  2024. Opened 2026-11-27.
- Table 1 (Sec. 4), performance levels: Competent "at least 50th percentile of skilled adults",
  Expert "at least 90th", Exceptional (formerly Virtuoso) "at least 99th", Superhuman "outperforms
  100% of humans". Principle 1 (Sec. 3): "Focus on Capabilities, not Processes."
- AlphaFold, AlphaZero and Stockfish are classed as Superhuman Narrow AI. ASI is Level 5 General,
  "a wide range of tasks at a level that no human can match". Percentiles are measured against
  individual "skilled adults".
- Bears on: D1 (the percentile-of-individuals design D1 departs from), F3 (narrow vs general axis).

### hendrycks2025agidef
- "A Definition of AGI", Dan Hendrycks, Dawn Song, Christian Szegedy, ... Yoshua Bengio (33
  authors). arXiv 2510.18212 (v3, 2025-12-03). Opened 2026-11-27.
- AGI is "an AI that can match or exceed the cognitive versatility and proficiency of a well-educated
  adult" (Sec. 1). Ten CHC domains, weighted 10% each (K, RW, M, R, WM, MS, MR, V, A, Speed).
- Scores: "GPT-4 at 27%, GPT-5 at 57%". GPT-5 scores 0% on long-term memory storage. Speed is "the
  ability to perform simple cognitive tasks quickly" (as read: both models at 3%, Sec. 12).
- Sec. 13: "Superintelligence is an AI that greatly exceeds the cognitive performance of humans in
  virtually all domains of interest." Copies and organisations are not mentioned.
- Bears on: D1 (an individual-human yardstick), pathway 4 (continual learning: memory storage is the
  missing faculty).

### fourati2025coherence
- "A Coherence-Based Measure of AGI", Fares Fourati. arXiv 2510.20784 (v2, 2025-11-27). Opened
  2026-11-27.
- Averaging domain scores "implicitly assumes compensability", and the arithmetic mean "rewards
  specialization". Proposes the area under the generalised-mean curve across arithmetic, geometric
  and harmonic regimes.
- Bears on: D1 aggregation. D1 counts clusters won (alpha), which does not compensate across
  clusters, but alpha below 1 still lets a specialist through.

### genewein2026agiasi
- "From AGI to ASI", Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, ... Marcus
  Hutter, Thore Graepel, Shane Legg. arXiv 2606.12683 (v3, 2026-11-10). Opened 2026-11-27 (HTML).
- Sec. 3, ASI: "a system that exceeds the performance of large human-expert collectives" on
  virtually all tasks, "outperforming large groups of experts instead of individual experts"
  (contrasted with Morris et al.). Footnote 5: a collective is "the best that a large and
  well-coordinated group of humans ... can hypothetically achieve".
- Sec. 3 remark, the concrete bar: "reliably outperforms hypothetical groups of tens of thousands of
  well-coordinated expert-level humans that work over a period of 10 years with the technology and
  cultural artifacts available in 2010 on a single problem or task", described as "roughly the size
  of entire specialized research fields, or large corporations". "Additionally, ASI would perform
  the same tasks in less time, say by a factor of 10 or more." The humans' technology is frozen
  because humans who use AI make the threshold "a moving target".
- "A single ASI may consist of a collective of millions of instances". AlphaFold and AlphaGo "are
  thus ruled out as ASIs". An alternative "human obsolescence" definition: the system alone and the
  system plus a large human group perform about the same.
- No test protocol, benchmark or budget matching. The measure is Legg-Hutter, which is "not
  computable". Four pathways: scaling AGI, paradigm shifts, multi-agent collectives, recursive
  improvement. Effective compute growth "about 10x per year" (Sec. 2).
- Bears on: **D1 closest prior art** (organisation-sized human collectives, copies inside the
  system, a speed factor), F3, Y1 (the four pathways overlap the memo's five).

### lifland2025timelines
- "Timelines Forecast", Eli Lifland, Nikola Jurkovic, FutureSearch (AI Futures Project / AI 2027),
  April 2025, updated May and Dec 2025. URL https://ai-2027.com/research/timelines-forecast. Opened
  2026-11-27.
- Superhuman coder (SC): "the company could run with 5% of their compute budget 30x as many agents
  as they have human research engineers", each "at 30x the speed", doing "any coding tasks that the
  best AGI company engineer does". Treats an RE-Bench score of 1.5 as roughly the best human.
- Bears on: D1 and F1. Copies, speed and compute share are counted explicitly, but the comparison is
  with one company's staff in one cluster.

### kokotajlo2025takeoff
- "Takeoff Forecast", Daniel Kokotajlo, Eli Lifland (AI Futures Project), April 2025. URL
  https://ai-2027.com/research/takeoff-forecast. Opened 2026-11-27.
- SAR: "do the job of the best human AI researcher but 30x faster and with 30x more agents". SIAR:
  "vastly better than the best human researchers". ASI: "much better than the best human at every
  cognitive task", measured "across the whole field, not a single company".
- Bears on: D1, F1, D2 (the milestone ladder for the self-improvement pathway).

### amodei2024grace
- "Machines of Loving Grace", Dario Amodei, essay, October 2024. URL
  https://www.darioamodei.com/essay/machines-of-loving-grace. Opened 2026-11-27.
- "Powerful AI": "smarter than a Nobel Prize winner across most relevant fields". The training
  compute can "run millions of instances". Speed "roughly 10x-100x human speed". Summed up as a
  "country of geniuses in a datacenter". Bounded by the physical world ("the marginal returns to
  intelligence").
- Bears on: F1 (copies and speed as an assumption, not a measurement), D1.

### karnofsky2022defeat
- "AI Could Defeat All Of Us Combined", Holden Karnofsky, Cold Takes, 2022-06-09. URL
  https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/. Opened 2026-11-27.
- The compute that trains a human-level AI could run "several hundred million copies for about a
  year each", "over 1000x the total number of Intel or Google employees", about 5-10% of the world's
  working-age population. The danger needs no quality superiority: "we still have a problem even if
  we assume that AIs will basically have similar capabilities to humans".
- Bears on: F1 (collective superintelligence through copies alone), Y1 (economic loop).

### aschenbrenner2024sa
- "II. From AGI to Superintelligence: the Intelligence Explosion", Situational Awareness series,
  Leopold Aschenbrenner (per the site's About page; the article itself is unsigned), June 2024. URL
  https://situational-awareness.ai/from-agi-to-superintelligence/. Opened 2026-11-27.
- "perhaps 100 million human-equivalents" of automated researchers, eventually "at 100x human speed"
  (10x+ at first). They could "compress a human-decade of algorithmic progress into less than a
  year". Bottleneck: "limited compute for experiments".
- Bears on: F1, D2, A2.

### altman2023governance
- "Governance of superintelligence", Sam Altman, Greg Brockman, Ilya Sutskever, OpenAI, 2023-05-22.
  URL https://openai.com/index/governance-of-superintelligence/. Opened 2026-11-27.
- Within ten years AI could "exceed expert skill level in most domains" and carry out as much
  productive activity as "today's largest corporations". Proposes "something like an IAEA for
  superintelligence efforts" above a "capability (or resources like compute) threshold".
  "Tracking compute and energy usage could go a long way".
- Bears on: D1 (a comparison with corporations by productive output), and the protocol (an
  IAEA-style compute threshold was proposed by a frontier lab).

### openaicharter
- "OpenAI Charter", OpenAI, page undated. URL https://openai.com/charter/. Opened 2026-11-27.
- AGI: "highly autonomous systems that outperform humans at most economically valuable work."
- Bears on: F2 (economic production as the defining cluster), D1.

### openai2025preparedness
- "Preparedness Framework, Version 2", OpenAI, last updated 2025-04-15. URL
  https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf.
  Opened 2026-11-27 (PDF, Table 1).
- AI self-improvement, High: "equivalent to giving every OpenAI researcher a highly performant
  mid-career research engineer assistant, relative to those researchers' 2024 baseline".
- Critical: "fully automated AI R&D, defined as either (leading indicator) a superhuman
  research-scientist agent OR (lagging indicator) causing a generational model improvement (e.g.,
  from OpenAI o1 to OpenAI o3) in 1/5th the wall-clock time of equivalent progress in 2024 (e.g.,
  sped up to just 4 weeks) sustainably for several months." Response: "halt further development"
  until safeguards are specified.
- Bears on: D1 (an institution-level, wall-clock-matched comparison), D2 (a rate-of-progress
  trigger).

### anthropic2026rsp
- "Responsible Scaling Policy, Version 3.4", Anthropic, effective 2026-07-08. URL
  https://www.anthropic.com/responsible-scaling-policy (PDF v3.4). Opened 2026-11-27.
- The automated-AI-R&D threshold is met if "(1) our models would be able to fully substitute for our
  entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a
  factor of 5); or (2) there is 'dramatic acceleration' of the pace of AI progress", which means
  "double the rate of progress" in aggregate capabilities. Footnote: "as much progress in one year
  as one would see in two years at baseline". With 3x compute and 3x algorithms (9x), doubling
  "would entail something like an 81x effective scaleup", compared with the fastest rate seen "over
  at least three model generations". The changelog records splitting AI R&D into two levels: "fully
  automate entry-level AI research work" and "dramatic acceleration in the rate of effective
  scaling".
- Bears on: **D1** (whole-organisation substitution at matched cost, for the AI-research cluster),
  D2 (rate doubling is a loop-gain-like trigger).

### barres2026harder
- "Harder Than the Task: From Technical to Organizational Difficulty in AI Benchmarking", Victor
  Barres, Aden Barton, Nicolai J. Foss, Henrik M. Nielsen. arXiv 2611.03494, 2026-11-02. Opened
  2026-11-27 (abstract).
- Organisational conditions: "interdependence of activities, distributed knowledge, differentiated
  authority", time constraints, conflicting interests, changing environments. Finds "fewer than one
  quarter of prominent benchmarks claiming any of them". A secondary write-up gives "81 of 522";
  that figure was not seen on the arXiv page.
- Bears on: D1 (institutional baselines are rare in the benchmark record).

**Group: AI research and software engineering**

### wijk2024rebench
- "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human
  experts", Wijk, Lin, Becker, ... Barnes (METR). arXiv 2411.15114 (v2, 2025-05-27). Opened
  2026-11-27 (abstract and HTML).
- Seven ML research-engineering environments. "71 8-hour attempts by 61 distinct human experts".
  82% of expert attempts score above zero, 24% match or beat the reference.
- At 2 hours per environment, "the best AI agents achieve a score 4x higher than human experts". At
  8 hours, humans narrowly exceed the agents. At 32 hours (best of four 8-hour runs), humans achieve
  "2x the score of the top AI agent".
- Cost (Sec. 6.2): agents "approximately $123" per 8-hour run against "approximately $1,855" paid to
  human experts. 0 to 6 H100s per run, with wall-clock limits so humans and agents get "an equal
  amount of GPU hours". Humans make 3.4 attempts an hour against 36.8 (AIDE) and 25.3 (Modular).
- Table 7: "performance on RE-Bench is likely to be an overestimate of the real-world AI R&D
  performance". Real R&D is at least "2 orders of magnitude (OOM) larger" on several axes.
- Bears on: **D1 test design** (equal wall-clock and GPU; the result flips with the time budget),
  F1 (speed about 10x in attempts, cost about 1/15), F2 (AI research), D2.

### kwa2025horizon
- "Measuring AI Ability to Complete Long Software Tasks", Kwa, West, Becker, ... Barnes, Chan
  (METR). arXiv 2503.14499 (v4, 2026-07-10; listed as NeurIPS 2025). Opened 2026-11-27 (abstract and
  HTML v2).
- Claude 3.7 Sonnet "a 50% time horizon of around 50 minutes" (59 minutes in Sec. 4.2.1). "doubling
  approximately every seven months since 2019". Humans timed on RE-Bench, HCAST and "66 novel
  shorter tasks". Extrapolation: within 5 years, many software tasks "that currently take humans a
  month".
- Sec. 8.2 assumes humans cost "$143.61/hour (average L4 Engineer salary at Google divided by 2,000
  hours)". On that basis, "more than 80% of successful runs cost less than 10% of what it would cost
  for a human".
- Sec. 6.4: "our contract baseliners take 5x-18x longer to resolve issues than repository
  maintainers". Sec. 6.2: "An increase in task messiness by 1 point reduces mean success rates by
  roughly 8.1%". 80% horizons are "approximately 5x shorter". Doubling time 213 days (80%) against
  212 days (50%).
- Bears on: F1 (cost and speed accounting), D1 (the human baseline varies 5-18x with context, so
  "best organisation" has to be specified), D3 (horizon growth rate).

### metr2026horizons
- "Time horizons" page and data file benchmark_results_1_1.yaml (METR-Horizon-v1.1), METR. URL
  https://metr.org/time-horizons/. Opened and downloaded 2026-11-27.
- The page says it "is no longer actively updated" (update of 2026-09-08). "Measurements above 16
  hrs are unreliable with our current task suite."
- Data file: doubling time from 2023 on 128.7 days (CI 104.4 to 158.0). The all-time stitched
  estimate is 187.8 days. 50% horizons in minutes: GPT-4 (2023-03) 4.0; o3 (2025-04) 119.7; GPT-5
  (2025-08) 203.0; Claude Opus 4.6 (2026-02) 718.8 (CI 316.7 to 3633.8); Claude Mythos Preview early
  (release 2026-04-07) 1044.8 (CI 508.9 to 3304.3).
- Bears on: F1, D3. The measurement instrument itself saturated in 2026.

### rein2025hcast
- "HCAST: Human-Calibrated Autonomy Software Tasks", Rein, Becker, et al. (METR). arXiv 2503.17354,
  2025-03-21. Opened 2026-11-27.
- "189 machine learning engineering, cybersecurity, software engineering, and general reasoning
  tasks". "563 human baselines (totaling over 1500 hours)". Tasks take humans "one minute and 8+
  hours". Agents succeed "70-80% of the time" on tasks under an hour for humans, and "less than 20%
  of the time" beyond four hours.
- Bears on: D1 (time dependence), F1.

### chan2024mlebench
- "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering", Chan, Chowdhury,
  ... Madry (OpenAI). arXiv 2410.07095 (v6, 2025-02-26). Opened 2026-11-27 (abstract and HTML).
- "75 ML engineering-related competitions from Kaggle". Human baselines from Kaggle private
  leaderboards, binned by team count. Bronze is the top 40% under 250 teams, the top 100 for 250-999
  teams, the top 10% for 1,000+ teams.
- 24 hours per competition on one A10 GPU. o1-preview with AIDE gets a medal in "16.9% of
  competitions" at pass@1, and 34.1% at pass@8. GPT-4o: 8.7% at 24 h, 11.8% at 100 h. Sec. 4: no
  link between familiarity and score (8.5% original against 8.4% obfuscated).
- Bears on: **D1 test bed** (a team baseline under a fixed wall-clock), D5 (pass@k doubles the
  measured capability).

### starace2025paperbench
- "PaperBench: Evaluating AI's Ability to Replicate AI Research", Starace, ... Patwardhan (OpenAI).
  arXiv 2504.01848 (v3, 2025-04-07). Opened 2026-11-27.
- "20 ICML 2024 Spotlight and Oral papers", "8,316 individually gradable tasks". Best agent (Claude
  3.5 Sonnet New): "average replication score of 21.0%". Top ML PhDs as baseline: "models do not yet
  outperform the human baseline".
- Bears on: F2 (AI research), D2.

### chowdhury2024swebv
- "Introducing SWE-bench Verified", Chowdhury, Aung, ... Madry (OpenAI), 2024-08-13 (updated
  2025-02-24). URL https://openai.com/index/introducing-swe-bench-verified/. Opened 2026-11-27.
- 93 Python developers annotated 1,699 samples. 68.3% were filtered out (38.3% underspecified, 61.1%
  with unit tests that may reject valid fixes), leaving 500 tasks. GPT-4o: 33.2% on Verified against
  16% on the original. 196 tasks are "<15-minute fix", 45 take over an hour.
- Bears on: benchmark validity (label noise in the original set).

### liang2025illusion
- "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason", Liang, Garg,
  Zilouchian Moghaddam. arXiv 2506.12286 (v4, 2025-12-01). Opened 2026-11-27.
- Buggy-file-path identification from the issue text alone: "up to 76%" on SWE-bench Verified,
  "merely up to 53%" on other repositories. 5-gram verbatim overlap up to 35% against 18%. Gains "may
  be partially driven by memorization".
- Bears on: contamination, and the case for refreshed held-out batteries in D1.

### rein2025holistic
- "Research Update: Algorithmic vs. Holistic Evaluation", David Rein (METR), 2025-08-13. URL
  https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons.
  Opened 2026-11-27.
- 18 open-source issues, 15 reviewed by hand. Test pass rate "an average success rate of 38%" (plus
  or minus 19%). Of the reviewed PRs, "none of them are mergeable as-is". Passing PRs need about 26
  minutes of fixes on average. "algorithmic scoring based on unit tests overestimates model
  capabilities."
- Bears on: D1 (scoring must be holistic), F2.

### whitfill2026merge
- "Many SWE-bench-Passing PRs Would Not Be Merged into Main", Whitfill, Wu, Becker, Rush (METR),
  2026-03-10. URL
  https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/.
  Opened 2026-11-27.
- 4 maintainers from 3 SWE-bench Verified repositories reviewed 296 AI PRs. "about 68% of golden
  patches are indeed merged". Maintainer merge rates are "about 24 percentage points lower than
  SWE-bench scores" after normalising (34.9 pp before), "roughly one-third to one-half of automated
  grader pass rates". One attempt, no feedback, so this is "not a fundamental capability limit".
- Bears on: D1 (how far proxies sit from institutional acceptance), F2.

### becker2025rct
- "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", Becker,
  Rush, Barnes, Rein (METR). arXiv 2507.09089 (v2, 2025-07-25). Opened 2026-11-27.
- RCT: "16 developers with moderate AI experience", "246 tasks in mature projects", about 5 years on
  each project. AI allowed: completion time up 19%. Developers forecast a 24% reduction beforehand
  and believed in a 20% reduction afterwards. Economists forecast 39% shorter, ML experts 38%
  shorter.
- Bears on: F2, and evidence against reading benchmark scores as uplift.

**Group: Mathematics and science**

### rein2023gpqa
- "GPQA: A Graduate-Level Google-Proof Q&A Benchmark", Rein, Hou, Stickland, Petty, Pang, Dirani,
  Michael, Bowman. arXiv 2311.12022, 2023-11-20. Opened 2026-11-27.
- "448 multiple-choice questions" in biology, physics and chemistry. Experts (PhD holders or
  candidates) score 65%, or 74% after discounting mistakes they spotted afterwards. "Highly skilled
  non-expert validators" with over 30 minutes and full web access score 34%. GPT-4 baseline 39%.
- Bears on: F2 (expert baseline), saturation.

### phan2025hle
- "Humanity's Last Exam", Long Phan, ... Dan Hendrycks (1,177 authors; CAIS and Scale AI). arXiv
  2501.14249 (v12, 2026-10-19). Opened 2026-11-27 (abstract and HTML v1).
- "HLE consists of 2,500 questions across dozens of subjects." Questions had to stump frontier models
  ("exact-match questions must stump all models", App. B.1).
- Table 1 at release (accuracy, calibration error): GPT-4o 3.3% / 92.5%; Claude 3.5 Sonnet 4.3% /
  88.9%; o1 9.1% / 93.4%; DeepSeek-R1 9.4% / 81.8% (text only). The opened content shows **no human
  baseline**.
- Bears on: saturation, and D1 (with no human baseline, it cannot serve an organisational
  comparison).

### scale2026hleboard
- "Humanity's Last Exam leaderboard", Scale AI Labs, updated 2026-09-17 (HLE-Rolling). URL
  https://labs.scale.com/leaderboard/humanitys_last_exam. Opened 2026-11-27.
- Top: GPT 6 Astra 54.80 plus or minus 1.94% (calibration error 39%); Fable 5.1 (xhigh) 46.50%;
  gemini-3.1-pro-preview 46.44%. Tool use is not stated.
- Bears on: saturation rate (9.4% to 54.8% in about 20 months).

### white2025hleaudit
- "About 30% of Humanity's Last Exam Chemistry/biology Answers are Likely Wrong", Andrew White,
  Michael Skarlinski, Jon Laurent, Albert Bou (FutureHouse), 2025-07-23, updated 2025-09-16. URL
  https://futurehouse.org/research/hle-exam. Opened 2026-11-27.
- Audited the 321 text-only bio and chem questions. Expert review of 150 gives "29.3 plus or minus
  3.7% (95% CI)" directly conflicted by research. Cause: questions had to stump models, and
  reviewers did not have to check rationales taking "more than 5 minutes". The HLE team's own
  follow-up found about 18%.
- Bears on: benchmark validity. Adversarial filtering against models selects for errors.

### epoch2026hlereview
- "Humanity's Last Exam: Benchmark Review", Epoch AI, reviewed 2026-08-11. URL
  https://epoch.ai/benchmarks/hle/review. Opened 2026-11-27.
- Verdict "Flawed": "substantial accuracy-altering errors". 22 of 48 sampled questions (46%)
  defective, 12 impossible as written. Partial review, original set only (not Rolling or Verified).
- Bears on: D1 battery design (refresh and audit).

### glazer2024frontiermath
- "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI", Glazer, Erdil,
  Besiroglu, ... Wildon (Epoch AI, 24 authors). arXiv 2411.04872 (v7, 2025-12-23). Opened 2026-11-27.
- Unpublished, expert-vetted problems with automated verification. Typical problems take experts
  "multiple hours", the hardest "multiple days". At release, SOTA solved "under 2%".
- Bears on: saturation (see epoch2026hub: 95-100% by late 2026).

### gotting2025vct
- "Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark", Gotting, Medeiros,
  Sanders, Li, Phan, Elabd, Justen, Hendrycks, Donoughe. arXiv 2504.16137 (v3, 2026-11-24). Opened
  2026-11-27.
- "VCT consists of 322 multimodal questions". Virologists with internet access average 22.1% "on
  questions specifically in their sub-areas of expertise". o3 "reaches 43.8% accuracy",
  "outperforming 94% of expert virologists even within their sub-areas of specialization".
- Bears on: F2 (weapons-relevant science), D1 (the comparison is with individuals; tacit
  troubleshooting matters).

### li2024wmdp
- "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning", Li, Pan, Gopal, ...
  Hendrycks (56 authors). arXiv 2403.03218 (v8, 2026-11-25). Opened 2026-11-27.
- "a dataset of 3,668 multiple-choice questions" as "a proxy measurement of hazardous knowledge in
  biosecurity, cybersecurity, and chemical security". RMU unlearning lowers WMDP scores "while
  maintaining general capabilities".
- Bears on: F2, and the protocol (a proxy without a human baseline, so a knowledge measure, not a
  capability against institutions).

### justen2025bio
- "LLMs Outperform Experts on Challenging Biology Benchmarks", Lennart Justen. arXiv 2505.06108 (v3,
  2025-05-21). Opened 2026-11-27.
- 27 LLMs, 8 biology benchmarks, 10 runs each. On VCT's text subset, "Top model performance increased
  more than 4-fold". o3 does about twice as well as expert virologists. Several models match or beat
  experts on the GPQA biology subset, WMDP and LAB-Bench CloningScenarios. Caveats: plateaus below
  100% from benchmark errors, and expert baselines whose quality varies.
- Bears on: F2, saturation.

**Group: Cyber**

### zhang2024cybench
- "Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models", Andy
  K. Zhang, ... Dan Boneh, Daniel E. Ho, Percy Liang. arXiv 2408.08926 (v4, 2025-04-12; ICLR 2025
  oral). Opened 2026-11-27.
- "40 professional-level Capture the Flag (CTF) tasks from 4 distinct CTF competitions". Difficulty
  comes from human team solve times: the hardest "took human teams 24 hours and 54 minutes to
  solve". Unguided agents in 2024 solved only tasks that human teams finished within 11 minutes.
- Bears on: **D1 test bed** (team first-solve times are a team baseline), F2.

### tang2026ctfcollab
- "Understanding Human-AI Collaboration in Cybersecurity Competitions", Tang, Janis, Montague,
  Eykholt, Kirat, Park, Jang, Nadkarni, Xiao. arXiv 2602.20446, 2026-02-24. Opened 2026-11-27
  (abstract and HTML).
- Live onsite CTF, "The CTF competition ran for 24 hours" (Sec. 4.2). 95 participants, 41 in the
  study. Best autonomous agent (proprietary scaffold, Sonnet-4.5) "reaches 4900 points (second place
  on the human scoreboard)" in "roughly four hours of cumulative runtime". Claude Code 4600 (would
  rank third). Cost "$96.32 in API usage" (intro; Sec. 7.2 says $95.32). Agents need "only about 1/5
  of the cumulative runtime" of human teams. With human pair hacking, 5700 points, "first on both"
  leaderboards. Human prompting, not model reasoning, was often the bottleneck.
- Bears on: **D1** (a direct comparison with teams, with time and cost recorded), F1, F2.

### mayoral2025cai
- "Cybersecurity AI: The World's Top AI Agent for Security Capture-the-Flag (CTF)", Mayoral-Vilches
  et al. arXiv 2512.02654, 2025-12-02. Opened 2026-11-27. **Self-reported by the tool's
  developers.**
- "Rank #1 at multiple events" in 2025, including HTB AI vs Humans and Cyber Apocalypse (8,129
  teams). At Neurogrid, "captured 41/45 flags to claim the $50,000 top prize". "Jeopardy-style CTFs
  have become a solved game for well-engineered AI agents."
- Bears on: F2 and saturation (the authors argue for moving to attack-defence formats).

**Group: Persuasion**

### salvi2025persuasion
- "On the conversational persuasiveness of GPT-4", Salvi, Horta Ribeiro, Gallotti, West. Nature Human
  Behaviour 9(8):1645-1653, 2025-05-19. DOI 10.1038/s41562-025-02194-6. Preprint arXiv 2403.14380.
  Opened 2026-11-27 (journal abstract via Europe PMC; arXiv abstract).
- Journal: preregistered, 2x2x3 design (human or GPT-4 opponent, with or without sociodemographic
  data, topic strength). "GPT-4 with personalization was more persuasive 64.4% of the time (81.2%
  relative increase in odds ... 95% confidence interval [+26.0%, +160.7%] ... N = 900)."
- The preprint had N=820 and 81.7%. Without personalisation the effect is "lower and statistically
  non-significant (p=0.31)". The human opponents were live participants, not professional
  persuaders.
- Bears on: F2 (persuasion; the baseline is individuals, not campaigns or organisations).

### schoenegger2025persuasion
- "Large Language Models Are More Persuasive Than Incentivized Human Persuaders", Schoenegger, Salvi,
  Liu, Nan, et al. (39 authors). arXiv 2505.09662 (v2, 2025-05-21; later v3 and v4 retitled). Opened
  2026-11-27.
- Preregistered, real-time conversational quiz. Claude Sonnet 3.5 against human persuaders with
  "real-money bonuses tied to performance". LLM persuaders achieved "significantly higher compliance"
  in both truthful and deceptive directions.
- Bears on: F2. Even money-incentivised individuals are beaten.

### hackenburg2025levers
- "The levers of political persuasion with conversational artificial intelligence", Hackenburg,
  Tappin, Hewitt, Saunders, Black, Lin, Fist, Margetts, Rand, Summerfield. Science 390(6777):eaea3884,
  2025-12-04. DOI 10.1126/science.aea3884. Preprint arXiv 2507.13919. Opened 2026-11-27 (journal
  abstract via Europe PMC; arXiv abstract).
- "N = 76,977 participants", "19 large language models", "707 political issues", "466,769 resulting
  LLM claims". Post-training and prompting "boosted persuasiveness by as much as 51 and 27%". Scale
  and personalisation "had smaller effects". "where they increased AI persuasiveness, they also
  systematically decreased factual accuracy."
- Bears on: F2, A1 (here post-training matters more than scale, so a compute threshold misses
  persuasion capability).

**Group: Forecasting and strategy**

### karger2025forecastbench
- "ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities", Karger, Bastani, Chen,
  Jacobs, Halawi, Zhang, Tetlock. arXiv 2409.19839 (v5, 2025-02-28). Opened 2026-11-27 (HTML v5).
- "comprised solely of questions about future events that have no known answer at the time of
  submission", so it cannot be contaminated. Superforecasters "achieve an overall mean Brier score of
  0.096" against the best LLM at 0.122 (Claude 3.5 Sonnet, 200-question subset), significantly
  worse. Projected parity "when the Arena score approaches 1406" (CI 1346 to 1633), or about 6.49e26
  FLOP.
- Bears on: D1 (a dynamic battery design), F2 (strategy).

### forecastbench2026board
- ForecastBench tournament leaderboard (Forecasting Research Institute), "updated 2026-11-27". URL
  https://forecastbench.org/leaderboards/. Opened 2026-11-27 (page and its leaderboard script).
- Scored as a difficulty-adjusted Brier score turned into a "Brier Index", "100% = perfect accuracy,
  50% = maximally uninformed". Superforecaster median forecast: Overall 68.1 (N=578). Public median
  62.9. Top entries: 69.5 (an anonymous team's "model-4"), 69.3 (NeuroFusion hybrid ensemble), 68.5
  (Google DeepMind "fire hedgehog"). Rank 9 is shared by the superforecaster median and AI entries.
- Bears on: F2. Forecasting is at parity with the superforecaster median as of 2026-11.

### metaculus2026futureeval
- "FutureEval Spring Results: Pros Beat Bots, but the Gap is Nearly Gone", Ben Wilson, John Bash
  (Metaculus), 2026-09-09. URL
  https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is.
  Opened 2026-11-27.
- A 10-person Pro team against the top-10 bot team on 99 shared questions (173 bots). The Pro lead
  is 1.25 head-to-head points a question, "not statistically significant (one-sided p = 0.247)". The
  bot team's score was -20.03 in Q2 2025. The best Metaculus template bot used GPT-5.1.
- Bears on: **D1** (a team against a team, on the same questions), F2.

**Group: Economically valuable work**

### patwardhan2025gdpval
- "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks", Tejal
  Patwardhan et al. (OpenAI, 19 authors). arXiv 2510.04374, 2025-10-05 (ICLR 2026). Opened
  2026-11-27 (HTML v1).
- "1,320 tasks across 44 occupations" in "the top 9 sectors contributing to U.S. GDP". Experts with
  "14 years of experience" on average. "blinded expert pairwise comparisons". Claude Opus 4.1: "47.6%
  of deliverables ... graded as better than (wins) or as good as (ties)". Table 2 lists GPT-5 at
  39.0%.
- App. A.2.1: expert time and cost per gold task "HT=404 minutes and HC=$361", review 109 minutes and
  $86. GPT-5 speed and cost gains: naive 90x and 474x; "try 1x, then fix" 1.12x and 1.18x; "try n
  times, then fix" 1.39x and 1.63x. "does not capture the cost of catastrophic mistakes". "Tasks are
  precisely-specified and one-shot, not interactive". The automated grader agrees with experts 66%
  of the time, against 71% between humans.
- Bears on: F2 (economic production), F1 (once oversight is counted, cost and speed gains are small),
  D1 (the comparison is with individual experts on one-shot tasks).

### mazeika2025rli
- "Remote Labor Index: Measuring AI Automation of Remote Work", Mazeika, Gatti, Menghini, ...
  Hendrycks (CAIS and Scale AI, 47 authors). arXiv 2510.26787, 2025-10-30. Opened 2026-11-27 (HTML
  v1).
- 240 projects from 358 Upwork freelancers in 23 subcategories, "over 6,000 hours of human work valued
  at over $140,000". Mean 28.9 h and $632.6 (median 11.5 h, $200). Best automation rate: Manus 2.5%
  (Grok 4 and Claude Sonnet 4.5 2.1%, GPT-5 1.7%). Manus earned $1,720 of $143,991. Elo against a
  human baseline of 1,000: Manus 509.9. The human deliverable is the gold standard. Judges take a
  "reasonable client" view, with 94.4% agreement. Work needing client interaction or teamwork is
  excluded.
- Bears on: F2, D1 (end-to-end projects priced at market rates; see epoch2026hub for 41% in Nov
  2026).

### eloundou2024gpts
- "GPTs are GPTs: Labor market impact potential of LLMs", Eloundou, Manning, Mishkin, Rock. Science
  384(6702):1306-1308, 2024-06-20. DOI 10.1126/science.adj0998. Preprint arXiv 2303.10130. Opened
  2026-11-27 (arXiv abstract; journal metadata via Europe PMC).
- "around 80% of the U.S. workforce could have at least 10% of their work tasks affected",
  "approximately 19% of workers may see at least 50% of their tasks impacted". About 15% of tasks
  could be done "significantly faster at the same level of quality" by LLMs alone, and "between 47
  and 56%" with LLM-powered software. A rubric combining human and GPT-4 annotation.
- Bears on: F2. Exposure is an upper bound, not a measured capability.

### handa2025aei
- "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations", Handa,
  Tamkin, McCain, et al. (Anthropic). arXiv 2503.04761, 2025-02-11. Opened 2026-11-27.
- "over four million" conversations. Software development and writing are "nearly half of all total
  usage". "approximately 36% of occupations" use AI for at least a quarter of their tasks. "57% of
  usage suggests augmentation", 43% automation.
- Bears on: F2 (diffusion measured as usage, not capability against experts).

**Group: Narrow superhuman systems**

### jumper2021alphafold
- "Highly accurate protein structure prediction with AlphaFold", Jumper, Evans, Pritzel, et al.
  Nature 596(7873):583-589, 2021-07-15. DOI 10.1038/s41586-021-03819-2. Opened 2026-11-27 (abstract
  and full text via Europe PMC, PMC8371605).
- CASP14, a blind assessment: "median backbone accuracy of 0.96 Å r.m.s.d.95 ... (95% confidence
  interval = 0.85-1.16 Å) whereas the next best performing method had a median backbone accuracy of
  2.8 Å". A carbon atom is "approximately 1.4 Å" wide. "accuracy competitive with experimental
  structures in a majority of cases".
- Bears on: F3, D1 (CASP is a blind contest between research groups, i.e. an organisational
  baseline).

### silver2018alphazero
- "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play",
  Silver, Hubert, Schrittwieser, et al. Science 362(6419):1140-1144, 2018. DOI
  10.1126/science.aar6404. Preprint arXiv 1712.01815. Opened 2026-11-27 (journal abstract via Europe
  PMC; arXiv abstract).
- "Starting from random play and given no domain knowledge except the game rules", it beat world
  champion programs in all three games. The preprint: "within 24 hours a superhuman level of play".
- Bears on: A4 and A5 (self-play with a verifier), F3.

### brown2019pluribus
- "Superhuman AI for multiplayer poker", Noam Brown, Tuomas Sandholm. Science 365(6456):885-890,
  2019-07-11. DOI 10.1126/science.aay2400. Opened 2026-11-27 (abstract via Europe PMC).
- Pluribus is "stronger than top human professionals in six-player no-limit Texas hold'em poker".
- Bears on: F3.

### meta2019pluribus
- "Facebook, Carnegie Mellon build first AI that beats pros in 6-player poker", Meta AI blog,
  2019-07-11. URL https://ai.meta.com/blog/pluribus-first-ai-to-beat-pros-in-6-player-poker/. Opened
  2026-11-27.
- Blueprint "in eight days on a 64-core server", "less than 512 GB of RAM", "it would cost less than
  $150 to train". Play "runs on two CPUs", "less than 128 GB of memory". 10,000 hands over 12 days,
  win rate "about 5 big blinds per 100 hands". In 1 human against 5 AIs, the humans lost 2.3 bb/100.
- Bears on: **F3** (narrow superhuman ability at negligible compute is invisible to compute
  accounting and harmless to the protocol), P1.

### fair2022cicero
- "Human-level play in the game of Diplomacy by combining language models with strategic reasoning",
  Meta FAIR Diplomacy Team (Bakhtin, Brown, et al.). Science 378(6624):1067-1074, 2022-11-22. DOI
  10.1126/science.ade9097. Opened 2026-11-27 (abstract via Europe PMC).
- "Across 40 games of an anonymous online Diplomacy league, Cicero achieved more than double the
  average score of the human players and ranked in the top 10% of participants who played more than
  one game."
- Bears on: F2 (strategy and negotiation), F3. Human-level, not superhuman.

### wang2023adversarialgo
- "Adversarial Policies Beat Superhuman Go AIs", Wang, Gleave, Tseng, Pelrine, Belrose, Miller,
  Dennis, Duan, Pogrebniak, Levine, Russell. arXiv 2211.00241 (v4, 2023-07-13; ICML 2023). Opened
  2026-11-27.
- "a >97% win rate against KataGo running at superhuman settings". "human experts can implement it
  without algorithmic assistance". The weakness persists in adversarially trained KataGo.
- Bears on: F3, D1. "Superhuman" on average is not robust superiority, so D1's battery needs
  adversarial and held-out items.

### novikov2025alphaevolve
- "AlphaEvolve: A coding agent for scientific and algorithmic discovery", Novikov, Vu, Eisenberger,
  et al. (Google DeepMind). arXiv 2506.13131, 2025-06-16. Opened 2026-11-27.
- Multiplies 4x4 complex matrices "using 48 scalar multiplications", "the first improvement, after
  56 years, over Strassen's algorithm in this setting". It also "accelerated the training of the LLM
  underpinning AlphaEvolve itself". It depends on "feedback from one or more evaluators".
- Bears on: **F3 and D2**. A general model plus automated verifiers produces narrow superhuman
  results and feeds back into its own training, so the narrow/general line blurs inside the loop.

### deepmind2025imo
- "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the
  International Mathematical Olympiad", Thang Luong, Edward Lockhart (Google DeepMind), 2025-07-21.
  URL
  https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/.
  Opened 2026-11-27. Vendor claim, graded by IMO coordinators.
- "35 out of a possible 42 points". Five of six problems solved perfectly, "within the 4.5-hour
  competition time limit", end to end in natural language. About 8% of human contestants get gold.
- Bears on: F3 (a general model reaching elite but not best-human level in a narrow domain under
  human time limits).

**Group: Saturation, contamination and refreshed batteries**

### white2024livebench
- "LiveBench: A Challenging, Contamination-Limited LLM Benchmark", Colin White, Samuel Dooley, ...
  Yann LeCun, Micah Goldblum. arXiv 2406.19314 (v2, 2025-04-18; ICLR 2025 spotlight). Opened
  2026-11-27.
- "frequently-updated questions from recent information sources", scored "according to objective
  ground-truth values". "Questions are added and updated on a monthly basis". At release, "top models
  achieving below 70% accuracy".
- Bears on: D1 (refreshed battery design).

### jain2024livecodebench
- "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code",
  Jain, Han, Gu, Li, Yan, Zhang, Wang, Solar-Lezama, Sen, Stoica. arXiv 2403.07974 (v2, 2024-06-06).
  Opened 2026-11-27 (abstract and HTML).
- About 400 problems from LeetCode, AtCoder and CodeForces, May 2023 to May 2024. "DeepSeek-Instruct
  and GPT-4-O perform considerably worse on problems released since September and November 2023"
  (Fig. 1; Sec. 1 and 5.1 give slightly different months). "time-segmented evaluations prove
  effective".
- Bears on: D1 (time-segmented held-out items detect contamination).

### zhang2024gsm1k
- "A Careful Examination of Large Language Model Performance on Grade School Arithmetic", Hugh Zhang,
  Jeff Da, Dean Lee, et al. arXiv 2405.00332 (v4, 2024-11-22; NeurIPS 2024 Datasets and Benchmarks).
  Opened 2026-11-27.
- Drops "of up to 8%" from GSM8k to GSM1k. "several families of models showing evidence of systematic
  overfitting", while "many models, especially those on the frontier, show minimal signs".
  "Spearman's r^2 = 0.36" between generating GSM8k examples and the gap.
- Bears on: contamination.

### kiela2021dynabench
- "Dynabench: Rethinking Benchmarking in NLP", Kiela, Bartolo, Nie, et al. arXiv 2104.14337
  (NAACL 2021). Opened 2026-11-27.
- "contemporary models quickly achieve outstanding performance on benchmark tasks" yet fail simple
  challenge examples. Proposes "human-and-model-in-the-loop dataset creation".
- Bears on: D1 (dynamic, adversarial refresh).

### hai2025aiindex
- "The 2025 AI Index Report, Chapter 2: Technical Performance", Stanford HAI, 2025. URL
  https://hai.stanford.edu/ai-index/2025-ai-index-report/technical-performance. Opened 2026-11-27.
- "gains of 18.8 and 48.9 percentage points on MMMU and GPQA". SWE-bench "just 4.4% of coding
  problems in 2023 ... jumped to 71.7% in 2024". The gap between the top two models "shrank from 4.9%
  in 2023 to just 0.7% in 2024". "The saturation of traditional AI benchmarks like MMLU, GSM8K, and
  HumanEval".
- Bears on: saturation rate.

### vahdati2026arc
- "The ARC of Progress towards AGI: A Living Survey of Abstraction and Reasoning", Vahdati, Aioanei,
  Suresh, Lehmann. arXiv 2603.13372, 2026-03-09. Opened 2026-11-27 (abstract).
- "93.0% on ARC-AGI-1 (Opus 4.6)", 68.8% on ARC-AGI-2, 13% on ARC-AGI-3. Humans keep "near-perfect
  accuracy". Cost per task fell 390x in a year (o3 $4,500 to GPT-5.2 $12), which "largely reflects
  reduced test-time parallelism".
- Bears on: F1 (cost per task as part of the comparison), A2 (inference spending).

### epoch2026hub
- "Capabilities & benchmarking" data (benchmark_data.zip), Epoch AI, retrieved 2026-11-27. URL
  https://epoch.ai/benchmarks. CC BY 4.0. Also opened: the FrontierMath, GPQA Diamond and SWE-bench
  Verified pages.
- Best scores in the file (model, score, model release date): GPQA Diamond gpt-6.2-astra (max) 96.84%
  (2026-11-17). SWE-bench Verified claude-opus-4-7 (max) 83.47% (2026-04-16, Epoch's scaffold).
  FrontierMath Tiers 1-3 v2 claude-fable-5-2 (max) 95.09% (2026-11-09). FrontierMath Tier 4 v2:
  100% for claude-fable-5-2, gpt-6.1-sol and gpt-6.2-astra (2026-09 to 2026-11). HLE gpt-6-astra
  54.8%. Cybench unguided claude-opus-4-6 93% (2026-02-05, from the vendor system card, "~100% for
  pass@30"). GDPval win-or-tie gpt-5.2 70.86% (win 49.7%, 2025-12-11). Remote Labor Index
  claude-fable-5-2 41.25% (2026-11-09). ForecastBench best single LLM 66.6 (gpt-5.5 with web search,
  2026-04-23; superforecaster p-value 0.04).
- Pages: FrontierMath v2 (2026-06-12) "corrected errors in 42% of problems", with 338 problems (295
  base, 43 Tier 4). It "was developed with funding from OpenAI, who has exclusive access to a subset".
  SWE-bench Verified "error rate of 5-10%". GPQA Diamond: OpenAI's PhD experts "scored 69.7%".
- Bears on: saturation, and the ledger of current best scores.

## Numbers for the ledger

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| gpqa-expert-acc | 65 | % | measured | rein2023gpqa | abstract |
| gpqa-expert-acc-adjusted | 74 | % | measured | rein2023gpqa | abstract (discounting expert-identified mistakes) |
| gpqa-nonexpert-acc | 34 | % | measured | rein2023gpqa | abstract (30+ min, web access) |
| gpqa-gpt4-acc-2023 | 39 | % | measured | rein2023gpqa | abstract |
| gpqa-diamond-expert-acc-openai | 69.7 | % | vendor | epoch2026hub | GPQA Diamond page (OpenAI-recruited PhDs) |
| gpqa-diamond-best-2026-11 | 96.84 | % | measured | epoch2026hub | gpqa_diamond.csv, gpt-6.2-astra max, 2026-11-17, stderr 1.2 pp |
| hle-questions | 2500 | questions | spec | phan2025hle | abstract |
| hle-best-at-release-2025-01 | 9.4 | % | measured | phan2025hle | Table 1 (DeepSeek-R1, text only; o1 9.1) |
| hle-best-2026-09 | 54.8 | % | measured | scale2026hleboard | leaderboard, GPT 6 Astra, plus or minus 1.94 |
| hle-calibration-error-best-2026 | 39 | % | measured | scale2026hleboard | leaderboard |
| hle-defective-share-epoch | 46 | % | measured | epoch2026hlereview | 22 of 48 sampled |
| hle-biochem-conflict-share | 29.3 | % | measured | white2025hleaudit | plus or minus 3.7 (95% CI), 321 questions |
| frontiermath-sota-at-release-2024-11 | 2 | % (upper bound) | measured | glazer2024frontiermath | abstract ("under 2%") |
| frontiermath-v2-problems | 338 | problems | spec | epoch2026hub | FrontierMath page (295 + 43) |
| frontiermath-v2-corrected-share | 42 | % of problems | measured | epoch2026hub | FrontierMath page, v2 2026-06-12 |
| frontiermath-t13-best-2026-11 | 95.09 | % | measured | epoch2026hub | frontiermath_tiers_1_3_v2.csv, claude-fable-5-2 |
| frontiermath-t4-best-2026 | 100 | % | measured | epoch2026hub | frontiermath_tier_4_v2.csv, three models |
| swebv-tasks | 500 | tasks | spec | chowdhury2024swebv | blog |
| swebv-filtered-share | 68.3 | % | measured | chowdhury2024swebv | blog |
| swebv-best-2026 | 83.47 | % | measured | epoch2026hub | swe_bench_verified.csv, claude-opus-4-7 max |
| swebv-label-error-rate | 5-10 | % | measured | epoch2026hub | SWE-bench Verified page (Epoch estimate) |
| swebv-golden-merge-rate | 68 | % | measured | whitfill2026merge | note |
| swebv-maintainer-gap-normalised | 24 | pp | measured | whitfill2026merge | note (34.9 pp unnormalised) |
| metr-holistic-testpass-2025 | 38 | % | measured | rein2025holistic | blog (plus or minus 19, 0 of 15 mergeable) |
| metr-holistic-fix-minutes | 26 | min | measured | rein2025holistic | blog (test-passing PRs) |
| rebench-human-attempts | 71 | 8-h attempts | measured | wijk2024rebench | abstract (61 experts) |
| rebench-ai-over-human-2h | 4 | ratio of scores | measured | wijk2024rebench | abstract |
| rebench-human-over-ai-32h | 2 | ratio of scores | measured | wijk2024rebench | abstract (best of four 8-h runs) |
| rebench-agent-cost-8h | 123 | USD per run | measured | wijk2024rebench | Sec. 6.2 |
| rebench-human-cost-8h | 1855 | USD per run | measured | wijk2024rebench | Sec. 6.2 |
| rebench-attempts-per-hour-human | 3.4 | per hour | measured | wijk2024rebench | Sec. 5.1 |
| rebench-attempts-per-hour-aide | 36.8 | per hour | measured | wijk2024rebench | Sec. 5.1 |
| horizon-doubling-2019-2025 | 212 | days | measured | kwa2025horizon | Sec. 8.3 (about 7 months) |
| horizon-doubling-from-2023 | 128.7 | days | measured | metr2026horizons | YAML (CI 104.4 to 158.0) |
| horizon-claude37-50pct | 59 | min | measured | kwa2025horizon | Sec. 4.2.1 |
| horizon-80-vs-50-ratio | 5 | ratio | measured | kwa2025horizon | Sec. 8.3 |
| horizon-best-2026-04 | 1044.8 | min | measured | metr2026horizons | YAML, Claude Mythos Preview early (CI 508.9 to 3304.3) |
| horizon-reliable-limit | 16 | h | spec | metr2026horizons | page |
| horizon-human-rate | 143.61 | USD per hour | assumption | kwa2025horizon | Sec. 8.2 |
| horizon-cheap-run-share | 80 | % of successful runs under 10% of human cost | measured | kwa2025horizon | Sec. 8.2 |
| baseliner-vs-maintainer-slowdown | 5-18 | ratio | measured | kwa2025horizon | Sec. 6.4 |
| messiness-success-drop | 8.1 | % per point | measured | kwa2025horizon | Sec. 6.2 |
| hcast-tasks | 189 | tasks | spec | rein2025hcast | abstract |
| hcast-baseline-hours | 1500 | h (lower bound) | measured | rein2025hcast | abstract (563 baselines) |
| hcast-success-under-1h | 70-80 | % | measured | rein2025hcast | abstract |
| hcast-success-over-4h | 20 | % (upper bound) | measured | rein2025hcast | abstract |
| mlebench-medal-pass1 | 16.9 | % | measured | chan2024mlebench | abstract (o1-preview + AIDE) |
| mlebench-medal-pass8 | 34.1 | % | measured | chan2024mlebench | Sec. 3.2 |
| mlebench-gpt4o-24h-vs-100h | 8.7 / 11.8 | % | measured | chan2024mlebench | Sec. 3.4 |
| paperbench-best | 21.0 | % | measured | starace2025paperbench | abstract |
| cybench-tasks | 40 | tasks | spec | zhang2024cybench | abstract |
| cybench-hardest-team-fst | 24.9 | h | measured | zhang2024cybench | abstract (24 h 54 min) |
| cybench-best-unguided-2026-02 | 93 | % | vendor | epoch2026hub | cybench_external.csv (Opus 4.6 system card) |
| ctf-agent-points-2026 | 4900 | points | measured | tang2026ctfcollab | Sec. 7.2 (2nd on human scoreboard) |
| ctf-agent-api-cost-2026 | 96.32 | USD | measured | tang2026ctfcollab | intro (Sec. 7.2 says 95.32) |
| ctf-agent-runtime-share | 0.2 | fraction of human team runtime | measured | tang2026ctfcollab | intro |
| ctf-duration | 24 | h | spec | tang2026ctfcollab | Sec. 4.2 |
| cai-neurogrid-flags | 41/45 | flags | vendor | mayoral2025cai | abstract (self-reported) |
| wmdp-questions | 3668 | questions | spec | li2024wmdp | abstract |
| vct-questions | 322 | questions | spec | gotting2025vct | abstract |
| vct-virologist-acc | 22.1 | % | measured | gotting2025vct | abstract (own sub-areas) |
| vct-o3-acc | 43.8 | % | measured | gotting2025vct | abstract |
| vct-o3-percentile | 94 | percentile of virologists | measured | gotting2025vct | abstract |
| persuasion-gpt4-win-share | 64.4 | % of unequal pairs | measured | salvi2025persuasion | journal abstract (N=900) |
| persuasion-gpt4-odds-increase | 81.2 | % | measured | salvi2025persuasion | journal abstract (CI +26.0 to +160.7) |
| persuasion-posttrain-boost | 51 | % (max) | measured | hackenburg2025levers | abstract |
| persuasion-prompting-boost | 27 | % (max) | measured | hackenburg2025levers | abstract |
| persuasion-participants | 76977 | people | measured | hackenburg2025levers | abstract |
| forecast-superforecaster-brier-2024 | 0.096 | Brier | measured | karger2025forecastbench | Table 2 |
| forecast-best-llm-brier-2024 | 0.122 | Brier | measured | karger2025forecastbench | Table 2 (Claude 3.5 Sonnet) |
| forecast-parity-compute | 6.49e26 | FLOP | measured | karger2025forecastbench | projection, wide CI |
| forecast-superforecaster-index-2026-11 | 68.1 | Brier Index | measured | forecastbench2026board | leaderboard, N=578 |
| forecast-top-entry-index-2026-11 | 69.5 | Brier Index | measured | forecastbench2026board | leaderboard, N=607 |
| forecast-best-single-llm-index-2026 | 66.6 | Brier Index | measured | epoch2026hub | forecastbench_external.csv |
| metaculus-pro-lead-2026-spring | 1.25 | head-to-head points per question | measured | metaculus2026futureeval | p = 0.247 |
| gdpval-tasks | 1320 | tasks | spec | patwardhan2025gdpval | Sec. 1 (44 occupations, 9 sectors) |
| gdpval-opus41-win-or-tie | 47.6 | % | measured | patwardhan2025gdpval | Sec. 3.1 |
| gdpval-best-win-or-tie-2025-12 | 70.86 | % | measured | epoch2026hub | gdpval_external.csv (GPT-5.2) |
| gdpval-expert-minutes | 404 | min per task | measured | patwardhan2025gdpval | App. A.2.1 |
| gdpval-expert-cost | 361 | USD per task | measured | patwardhan2025gdpval | App. A.2.1 (BLS median wages) |
| gdpval-naive-speedup | 90 | ratio | measured | patwardhan2025gdpval | Table 2 (GPT-5) |
| gdpval-speedup-with-review | 1.39 | ratio | measured | patwardhan2025gdpval | Table 2 ("try n times, then fix") |
| gdpval-cost-gain-with-review | 1.63 | ratio | measured | patwardhan2025gdpval | Table 2 |
| rli-projects | 240 | projects | spec | mazeika2025rli | Sec. 3 |
| rli-value | 143991 | USD | measured | mazeika2025rli | Table 4 |
| rli-best-2025-10 | 2.5 | % | measured | mazeika2025rli | Table 1 (Manus) |
| rli-best-2026-11 | 41.25 | % | measured | epoch2026hub | rli_external.csv (Fable 5.2) |
| exposure-10pct-workforce | 80 | % of US workers | measured | eloundou2024gpts | abstract |
| exposure-50pct-workforce | 19 | % of US workers | measured | eloundou2024gpts | abstract |
| aei-occupations-quarter-tasks | 36 | % of occupations | measured | handa2025aei | abstract |
| aei-augmentation-share | 57 | % of usage | measured | handa2025aei | abstract |
| rct-dev-slowdown-2025 | 19 | % longer | measured | becker2025rct | abstract (16 devs, 246 tasks) |
| rct-dev-forecast-speedup | 24 | % shorter | measured | becker2025rct | abstract |
| gsm1k-max-drop | 8 | pp | measured | zhang2024gsm1k | abstract |
| swebench-illusion-filepath | 76 / 53 | % | measured | liang2025illusion | abstract (Verified / other repos) |
| aiindex-gpqa-gain-1yr | 48.9 | pp | measured | hai2025aiindex | ch. 2 item 1 |
| aiindex-swebench-2023-2024 | 4.4 / 71.7 | % | measured | hai2025aiindex | ch. 2 item 1 |
| arc-cost-drop-1yr | 390 | ratio | measured | vahdati2026arc | abstract ($4,500 to $12 per task) |
| alphafold-casp14-rmsd | 0.96 | Å | measured | jumper2021alphafold | main text (next best 2.8) |
| alphazero-train-time | 24 | h | measured | silver2018alphazero | arXiv abstract |
| pluribus-train-cost | 150 | USD (upper bound) | vendor | meta2019pluribus | blog (8 days, 64 cores) |
| pluribus-play-cpus | 2 | CPUs | vendor | meta2019pluribus | blog |
| pluribus-winrate | 5 | bb per 100 hands | measured | meta2019pluribus | blog (10,000 hands) |
| cicero-rank | 10 | top % of repeat players | measured | fair2022cicero | abstract (40 games) |
| adversarial-go-winrate | 97 | % (lower bound) | measured | wang2023adversarialgo | abstract |
| alphaevolve-4x4-mults | 48 | scalar multiplications | measured | novikov2025alphaevolve | abstract |
| imo2025-score | 35 | of 42 points | vendor | deepmind2025imo | blog (4.5 h limit) |
| agidef-gpt4 | 27 | % | measured | hendrycks2025agidef | abstract |
| agidef-gpt5 | 57 | % | measured | hendrycks2025agidef | abstract |
| levels-expert-percentile | 90 | percentile | design | morris2023levels | Table 1 |
| levels-exceptional-percentile | 99 | percentile | design | morris2023levels | Table 1 |
| asi-collective-size | tens of thousands | experts | design | genewein2026agiasi | Sec. 3 remark |
| asi-collective-years | 10 | years | design | genewein2026agiasi | Sec. 3 remark (2010 technology) |
| asi-speed-factor | 10 | ratio (lower bound) | design | genewein2026agiasi | Sec. 3 remark |
| sc-compute-share | 5 | % of company compute | design | lifland2025timelines | SC definition |
| sc-copies-ratio | 30 | agents per human engineer | design | lifland2025timelines | SC definition |
| sc-speed-ratio | 30 | ratio | design | lifland2025timelines | SC definition |
| rsp-cost-factor | 5 | ratio (AI cost within 5x of staff) | design | anthropic2026rsp | AI R&D threshold |
| rsp-progress-doubling | 2 | ratio of progress rate | design | anthropic2026rsp | AI R&D threshold, footnote 8 |
| pf-wallclock-fraction | 0.2 | fraction of 2024 wall-clock | design | openai2025preparedness | Table 1, Critical |
| copies-from-training-compute | several hundred million | copies for a year | assumption | karnofsky2022defeat | essay |
| copies-amodei | millions | instances | assumption | amodei2024grace | essay |
| speed-amodei | 10-100 | x human speed | assumption | amodei2024grace | essay |
| copies-aschenbrenner | 100 million | human-equivalents | assumption | aschenbrenner2024sa | essay |

## Prior art for the memo's candidates

All judgements below describe what our search found, not what exists. "Not found" means not found
by the queries listed.

### D1 (beat the best human organisation, matched time and budget, across clusters)

Queries tried: "Richard Ngo t-AGI definition beats most human experts given time t"; "AI Futures
Project timelines forecast superhuman coder definition 30x agents 30x speed best engineer";
"Bostrom Superintelligence chapter 3 speed collective quality definition text"; "definition
superintelligence outperform human organizations OR all of humanity matched compute cost wall-clock
time AI benchmark team baseline" (extended); "human team baseline AI evaluation matched budget
wall-clock comparison organisation-level AI capability definition 2025 2026 arXiv" (extended);
"organizational superintelligence OR superintelligence relative to organizations benchmark";
"Karnofsky AI could defeat all of us combined copies"; "Arbital superintelligent relative
efficiency epistemically efficient relative to humanity"; "OpenAI Preparedness Framework version 2
AI self-improvement critical wall-clock"; "Anthropic Responsible Scaling Policy AI R&D-4
entry-level remote-only Researcher"; "AGI or superintelligence definition cost parity OR same cost OR
matched cost human worker compute copies speed paper 2025 2026" (extended).

Closest prior work, ranked:
1. **genewein2026agiasi**: ASI against "large human-expert collectives" (tens of thousands of
   experts, 10 years, 2010 technology, about the size of a research field or large corporation),
   with a speed factor of 10 or more, and millions of instances counting as one system. It has no
   budget or compute matching and no test battery.
2. **ngo2023tagi**: (t,n)-AGI beats "any group of n humans working together" for time t, so a group
   comparison under matched wall-clock time. Superintelligence is a (1 year, 8 billion)-AGI. No
   budget matching, no battery.
3. **anthropic2026rsp**: whole-organisation substitution ("entire set of Research Scientists and
   Research Engineers") at matched cost ("within a factor of 5") for the AI-research cluster. This is
   an operative regulatory-style trigger already in force at a lab.
4. **openai2025preparedness**: matched wall-clock at institution level ("1/5th the wall-clock time of
   equivalent progress in 2024").
5. **lifland2025timelines / kokotajlo2025takeoff**: count copies (30x), speed (30x) and compute share
   (5%) against the best human at one company, and for ASI against the whole field.
6. **altman2023governance**: "as much productive activity as one of today's largest corporations".
   **yudkowsky2016superintelligent**: efficient "relative to every human and human group".
   **grace2014forms** (Bostrom's collective SI). **amodei2024grace**, **karnofsky2022defeat**,
   **aschenbrenner2024sa**: copies and speed as assumptions.

Counter-precedent: **bostrom1998howlong** explicitly excludes organisations and benchmarks against
"the best human brains". **morris2023levels** and **hendrycks2025agidef** benchmark against
individuals.

Judgement: **extends prior work.** The memo's stated differences ("comparing against organisations
rather than individuals, by counting copies and speed") are prior work (Genewein 2026, Ngo 2023, AI
2027, Amodei 2024), and the memo should say so. Our search found nothing that (a) matches **both**
wall-clock time and budget (compute and money) between the AI system and the human organisation as
part of a definition of superintelligence, (b) runs that comparison on a **refreshed held-out
battery** with published institutional baselines across several decisive clusters, or (c) uses an
**alpha fraction** of clusters. The RSP comes closest on (a) for one cluster. Those three are the
candidate contribution. Design points the prior work forces on D1: say whether the organisation may
use AI (Genewein pins it to 2010 technology); state the time budget, because verdicts flip with it
(RE-Bench, HCAST); state which organisation, because human baselines vary 5-18x with context
(kwa2025horizon).

Available scaled-down test beds with team or institutional baselines: CTF scoreboards (zhang2024cybench,
tang2026ctfcollab), Kaggle leaderboards (chan2024mlebench), forecasting pro teams
(metaculus2026futureeval, forecastbench2026board), CASP (jumper2021alphafold), RE-Bench with matched
GPU hours (wijk2024rebench). For persuasion, biology QA, GDPval and RLI, baselines are individuals
or freelancers only.

### F1 (speed, copies, quality measured separately; quality against institutions)

The typology is prior work (Bostrom via grace2014forms; bostrom1998howlong for speed). Measured
ingredients exist: speed and cost ratios for agents against experts (RE-Bench 36.8 against 3.4
attempts an hour, $123 against $1,855; CTF about 1/5 of runtime for about $96; METR more than 80% of
successful runs under 10% of human cost; GDPval 90x naive, 1.39x with review). Copies are only
**assumed** in the sources found (Karnofsky, Amodei, Aschenbrenner, AI 2027), never measured from
held compute. Quality against institutions: see D1; the RSP and Preparedness Framework thresholds
are institution-level but publish no measurement protocol. Judgement: **extends prior work.**
Measuring copies from held compute and inference throughput (link to P1 and P3) was not found as a
published measurement.

### F2 (decisive functions benchmarked against expert or institutional baselines)

Expert baselines exist for AI research (RE-Bench, PaperBench, MLE-bench), cyber (Cybench, live
CTFs), weapons-relevant science (VCT, GPQA; WMDP has none), persuasion (Salvi, Schoenegger,
Hackenburg), strategy and forecasting (ForecastBench, Metaculus, Cicero) and economic production
(GDPval, RLI). Status as of 2026-11 in these sources: AI ahead of individual experts in virology QA,
graduate science QA and one-shot GDPval deliverables; at parity in forecasting; ahead of human teams
in short-horizon jeopardy CTFs; behind on long-horizon AI R&D (RE-Bench at 32 h, PaperBench),
behind in holistic software acceptance (merge rates), and well short of full automation of
freelance projects (RLI 41%). Judgement: listing the clusters is **prior work** (it overlaps the
categories tracked by the Preparedness Framework and RSP). Benchmarking each one against an
institution, not an individual, was found only for cyber teams, Kaggle teams, forecasting teams
and the RSP's research staff.

### F3 (narrow superhuman is useful AI; the line is generality plus a closed loop)

Prior work separates narrow from general (morris2023levels; genewein2026agiasi rules out AlphaFold
and AlphaGo as ASI). Supporting evidence: narrow superhuman systems need little compute (Pluribus
under $150, two CPUs) and are brittle (adversarial Go over 97%). Complicating evidence:
novikov2025alphaevolve shows a general model plus automated evaluators producing narrow superhuman
results and speeding its own training. So "narrow" components inside a general system's loop are
not harmless by default. Judgement on the memo's "generality across the decisive functions together
with a closed loop" as the line: **extends prior work** (the narrow/general split is prior; tying the
line to closure is not found in these sources, though track 03 or 04 may find it).

### Adjacent: D2 and D5

- D2: anthropic2026rsp ("double the rate of progress", over at least three model generations) and
  openai2025preparedness ("1/5th the wall-clock time ... sustainably for several months") are
  rate-of-progress triggers already in lab policy. They are close relatives of a loop-gain trigger
  and must be credited in D2's novelty entry.
- D5: elicitation budget changes measured capability by about 2x (MLE-bench pass@1 16.9% against
  pass@8 34.1%; Cybench about 100% at pass@30 against 93% at pass@1 per the vendor card in
  epoch2026hub). Human prompting was the bottleneck in tang2026ctfcollab. This supports judging on
  elicited capability.

### Refreshed held-out batteries

Prior work: LiveBench (monthly), LiveCodeBench (time-segmented), ForecastBench (future events only),
HLE-Rolling (scale2026hleboard), Dynabench (adversarial human-in-the-loop). Error audits show that
filtering adversarially against models selects for mislabelled items (white2025hleaudit,
epoch2026hlereview, FrontierMath v2). Judgement: refresh is **prior work**. Combining refresh with
institutional baselines was not found.

## Seen in search results but not opened (not cited)

Bostrom, *Superintelligence* (2014), the book itself; LAB-Bench (arXiv 2407.10362); Metaculus Q1, Q2
and Q3 2025 benchmark reports (only the spring 2026 report was opened); "Some Simple Economics of
AGI" (arXiv 2602.20946); "Pathways to AGI" (arXiv 2605.06029); Hendrycks, Schmidt, Wang
"Superintelligence Strategy" (arXiv 2503.05628); the OpenAI GDPval blog post; the Barres et al.
"81 of 522" figure (secondary write-up only).

## Sources (TOML)

```toml
[source.bostrom1998howlong]
type = "peer-reviewed"
title = "How Long Before Superintelligence?"
authors = "Nick Bostrom"
year = 1998
url = "https://nickbostrom.com/superintelligence"
opened = "2026-11-27"

[source.grace2014forms]
type = "essay"
title = "Superintelligence 5: Forms of superintelligence"
authors = "Katja Grace"
year = 2014
url = "https://www.lesswrong.com/posts/semvkn56ZFcXBNc2d/superintelligence-5-forms-of-superintelligence"
opened = "2026-11-27"

[source.yudkowsky2016superintelligent]
type = "essay"
title = "Superintelligent (Arbital)"
authors = "Eliezer Yudkowsky"
year = 2016
url = "https://arbital.greaterwrong.com/p/superintelligent"
opened = "2026-11-27"

[source.aiimpacts2016coordinated]
type = "essay"
title = "Coordinated human action as example of superhuman intelligence"
authors = "AI Impacts"
undated = true
url = "https://aiimpacts.org/coordinated-human-action-example-superhuman-intelligence/"
opened = "2026-11-27"

[source.ngo2023tagi]
type = "essay"
title = "Clarifying and predicting AGI"
authors = "Richard Ngo"
year = 2023
url = "https://www.lesswrong.com/posts/BoA3agdkAzL6HQtQP/clarifying-and-predicting-agi"
opened = "2026-11-27"

[source.morris2023levels]
type = "peer-reviewed"
title = "Levels of AGI for Operationalizing Progress on the Path to AGI"
authors = "Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, Shane Legg"
year = 2024
arxiv = "2311.02462"
opened = "2026-11-27"

[source.hendrycks2025agidef]
type = "preprint"
title = "A Definition of AGI"
authors = "Dan Hendrycks, Dawn Song, Christian Szegedy, Honglak Lee, Yarin Gal, et al., Yoshua Bengio"
year = 2025
arxiv = "2510.18212"
opened = "2026-11-27"

[source.fourati2025coherence]
type = "preprint"
title = "A Coherence-Based Measure of AGI"
authors = "Fares Fourati"
year = 2025
arxiv = "2510.20784"
opened = "2026-11-27"

[source.genewein2026agiasi]
type = "preprint"
title = "From AGI to ASI"
authors = "Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, Samuel Albanie, Adam Bales, Cole Wyeth, Stephanie Chan, Iason Gabriel, Joel Z. Leibo, Allan Dafoe, Marcus Hutter, Thore Graepel, Shane Legg"
year = 2026
arxiv = "2606.12683"
opened = "2026-11-27"

[source.lifland2025timelines]
type = "report"
title = "Timelines Forecast (AI 2027)"
authors = "Eli Lifland, Nikola Jurkovic, FutureSearch"
year = 2025
url = "https://ai-2027.com/research/timelines-forecast"
opened = "2026-11-27"

[source.kokotajlo2025takeoff]
type = "report"
title = "Takeoff Forecast (AI 2027)"
authors = "Daniel Kokotajlo, Eli Lifland"
year = 2025
url = "https://ai-2027.com/research/takeoff-forecast"
opened = "2026-11-27"

[source.amodei2024grace]
type = "essay"
title = "Machines of Loving Grace"
authors = "Dario Amodei"
year = 2024
url = "https://www.darioamodei.com/essay/machines-of-loving-grace"
opened = "2026-11-27"

[source.karnofsky2022defeat]
type = "essay"
title = "AI Could Defeat All Of Us Combined"
authors = "Holden Karnofsky"
year = 2022
url = "https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/"
opened = "2026-11-27"

[source.aschenbrenner2024sa]
type = "essay"
title = "Situational Awareness, II. From AGI to Superintelligence: the Intelligence Explosion"
authors = "Leopold Aschenbrenner"
year = 2024
url = "https://situational-awareness.ai/from-agi-to-superintelligence/"
opened = "2026-11-27"

[source.altman2023governance]
type = "essay"
title = "Governance of superintelligence"
authors = "Sam Altman, Greg Brockman, Ilya Sutskever"
year = 2023
url = "https://openai.com/index/governance-of-superintelligence/"
opened = "2026-11-27"

[source.openaicharter]
type = "vendor"
title = "OpenAI Charter"
authors = "OpenAI"
undated = true
url = "https://openai.com/charter/"
opened = "2026-11-27"

[source.openai2025preparedness]
type = "official-docs"
title = "Preparedness Framework, Version 2"
authors = "OpenAI"
year = 2025
url = "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
opened = "2026-11-27"

[source.anthropic2026rsp]
type = "official-docs"
title = "Responsible Scaling Policy, Version 3.4"
authors = "Anthropic"
year = 2026
url = "https://www.anthropic.com/responsible-scaling-policy"
opened = "2026-11-27"

[source.barres2026harder]
type = "preprint"
title = "Harder Than the Task: From Technical to Organizational Difficulty in AI Benchmarking"
authors = "Victor Barres, Aden Barton, Nicolai J. Foss, Henrik M. Nielsen"
year = 2026
arxiv = "2611.03494"
opened = "2026-11-27"

[source.wijk2024rebench]
type = "preprint"
title = "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts"
authors = "Hjalmar Wijk, Tao Lin, Joel Becker, et al., Elizabeth Barnes"
year = 2024
arxiv = "2411.15114"
opened = "2026-11-27"

[source.kwa2025horizon]
type = "preprint"
title = "Measuring AI Ability to Complete Long Software Tasks"
authors = "Thomas Kwa, Ben West, Joel Becker, et al., Elizabeth Barnes, Lawrence Chan"
year = 2025
arxiv = "2503.14499"
opened = "2026-11-27"

[source.metr2026horizons]
type = "dataset"
title = "Time horizons (METR-Horizon-v1.1 benchmark results)"
authors = "METR"
year = 2026
url = "https://metr.org/time-horizons/"
opened = "2026-11-27"

[source.rein2025hcast]
type = "preprint"
title = "HCAST: Human-Calibrated Autonomy Software Tasks"
authors = "David Rein, Joel Becker, et al."
year = 2025
arxiv = "2503.17354"
opened = "2026-11-27"

[source.chan2024mlebench]
type = "preprint"
title = "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering"
authors = "Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, et al., Aleksander Madry"
year = 2024
arxiv = "2410.07095"
opened = "2026-11-27"

[source.starace2025paperbench]
type = "preprint"
title = "PaperBench: Evaluating AI's Ability to Replicate AI Research"
authors = "Giulio Starace, Oliver Jaffe, Dane Sherburn, et al., Tejal Patwardhan"
year = 2025
arxiv = "2504.01848"
opened = "2026-11-27"

[source.chowdhury2024swebv]
type = "vendor"
title = "Introducing SWE-bench Verified"
authors = "Neil Chowdhury, James Aung, Chan Jun Shern, et al., Aleksander Madry"
year = 2024
url = "https://openai.com/index/introducing-swe-bench-verified/"
opened = "2026-11-27"

[source.liang2025illusion]
type = "preprint"
title = "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason"
authors = "Shanchao Liang, Spandan Garg, Roshanak Zilouchian Moghaddam"
year = 2025
arxiv = "2506.12286"
opened = "2026-11-27"

[source.rein2025holistic]
type = "report"
title = "Research Update: Algorithmic vs. Holistic Evaluation"
authors = "David Rein (METR)"
year = 2025
url = "https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons"
opened = "2026-11-27"

[source.whitfill2026merge]
type = "report"
title = "Many SWE-bench-Passing PRs Would Not Be Merged into Main"
authors = "Parker Whitfill, Cheryl Wu, Joel Becker, Nate Rush (METR)"
year = 2026
url = "https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/"
opened = "2026-11-27"

[source.becker2025rct]
type = "preprint"
title = "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
authors = "Joel Becker, Nate Rush, Elizabeth Barnes, David Rein"
year = 2025
arxiv = "2507.09089"
opened = "2026-11-27"

[source.rein2023gpqa]
type = "preprint"
title = "GPQA: A Graduate-Level Google-Proof Q&A Benchmark"
authors = "David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, Samuel R. Bowman"
year = 2023
arxiv = "2311.12022"
opened = "2026-11-27"

[source.phan2025hle]
type = "preprint"
title = "Humanity's Last Exam"
authors = "Long Phan, et al., Dan Hendrycks"
year = 2025
arxiv = "2501.14249"
opened = "2026-11-27"

[source.scale2026hleboard]
type = "dataset"
title = "Humanity's Last Exam leaderboard"
authors = "Scale AI"
year = 2026
url = "https://labs.scale.com/leaderboard/humanitys_last_exam"
opened = "2026-11-27"

[source.white2025hleaudit]
type = "report"
title = "About 30% of Humanity's Last Exam Chemistry/biology Answers are Likely Wrong"
authors = "Andrew White, Michael Skarlinski, Jon Laurent, Albert Bou (FutureHouse)"
year = 2025
url = "https://futurehouse.org/research/hle-exam"
opened = "2026-11-27"

[source.epoch2026hlereview]
type = "report"
title = "Humanity's Last Exam: Benchmark Review"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/benchmarks/hle/review"
opened = "2026-11-27"

[source.glazer2024frontiermath]
type = "preprint"
title = "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI"
authors = "Elliot Glazer, Ege Erdil, Tamay Besiroglu, et al., Mark Wildon"
year = 2024
arxiv = "2411.04872"
opened = "2026-11-27"

[source.gotting2025vct]
type = "preprint"
title = "Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark"
authors = "Jasper Gotting, Pedro Medeiros, Jon G Sanders, Nathaniel Li, Long Phan, Karam Elabd, Lennart Justen, Dan Hendrycks, Seth Donoughe"
year = 2025
arxiv = "2504.16137"
opened = "2026-11-27"

[source.li2024wmdp]
type = "preprint"
title = "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning"
authors = "Nathaniel Li, Alexander Pan, Anjali Gopal, et al., Dan Hendrycks"
year = 2024
arxiv = "2403.03218"
opened = "2026-11-27"

[source.justen2025bio]
type = "preprint"
title = "LLMs Outperform Experts on Challenging Biology Benchmarks"
authors = "Lennart Justen"
year = 2025
arxiv = "2505.06108"
opened = "2026-11-27"

[source.zhang2024cybench]
type = "preprint"
title = "Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models"
authors = "Andy K. Zhang, et al., Dan Boneh, Daniel E. Ho, Percy Liang"
year = 2024
arxiv = "2408.08926"
opened = "2026-11-27"

[source.tang2026ctfcollab]
type = "preprint"
title = "Understanding Human-AI Collaboration in Cybersecurity Competitions"
authors = "Tingxuan Tang, Nicolas Janis, Kalyn Asher Montague, Kevin Eykholt, Dhilung Kirat, Youngja Park, Jiyong Jang, Adwait Nadkarni, Yue Xiao"
year = 2026
arxiv = "2602.20446"
opened = "2026-11-27"

[source.mayoral2025cai]
type = "preprint"
title = "Cybersecurity AI: The World's Top AI Agent for Security Capture-the-Flag (CTF)"
authors = "Victor Mayoral-Vilches, Luis Javier Navarrete-Lozano, Francesco Balassone, Maria Sanz-Gomez, Cristobal R. J. Veas Chavez, Maite del Mundo de Torres, Vanesa Turiel"
year = 2025
arxiv = "2512.02654"
opened = "2026-11-27"

[source.salvi2025persuasion]
type = "peer-reviewed"
title = "On the conversational persuasiveness of GPT-4"
authors = "Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, Robert West"
year = 2025
doi = "10.1038/s41562-025-02194-6"
arxiv = "2403.14380"
opened = "2026-11-27"

[source.schoenegger2025persuasion]
type = "preprint"
title = "Large Language Models Are More Persuasive Than Incentivized Human Persuaders"
authors = "Philipp Schoenegger, Francesco Salvi, Jiacheng Liu, Xiaoli Nan, et al."
year = 2025
arxiv = "2505.09662"
opened = "2026-11-27"

[source.hackenburg2025levers]
type = "peer-reviewed"
title = "The levers of political persuasion with conversational artificial intelligence"
authors = "Kobi Hackenburg, Ben M. Tappin, Luke Hewitt, Ed Saunders, Sid Black, Hause Lin, Catherine Fist, Helen Margetts, David G. Rand, Christopher Summerfield"
year = 2025
doi = "10.1126/science.aea3884"
arxiv = "2507.13919"
opened = "2026-11-27"

[source.karger2025forecastbench]
type = "preprint"
title = "ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities"
authors = "Ezra Karger, Houtan Bastani, Chen Yueh-Han, Zachary Jacobs, Danny Halawi, Fred Zhang, Philip E. Tetlock"
year = 2025
arxiv = "2409.19839"
opened = "2026-11-27"

[source.forecastbench2026board]
type = "dataset"
title = "ForecastBench tournament leaderboard"
authors = "Forecasting Research Institute"
year = 2026
url = "https://forecastbench.org/leaderboards/"
opened = "2026-11-27"

[source.metaculus2026futureeval]
type = "report"
title = "FutureEval Spring Results: Pros Beat Bots, but the Gap is Nearly Gone"
authors = "Ben Wilson, John Bash (Metaculus)"
year = 2026
url = "https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is"
opened = "2026-11-27"

[source.patwardhan2025gdpval]
type = "preprint"
title = "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks"
authors = "Tejal Patwardhan, et al. (OpenAI)"
year = 2025
arxiv = "2510.04374"
opened = "2026-11-27"

[source.mazeika2025rli]
type = "preprint"
title = "Remote Labor Index: Measuring AI Automation of Remote Work"
authors = "Mantas Mazeika, Alice Gatti, Cristina Menghini, et al., Dan Hendrycks"
year = 2025
arxiv = "2510.26787"
opened = "2026-11-27"

[source.eloundou2024gpts]
type = "peer-reviewed"
title = "GPTs are GPTs: Labor market impact potential of LLMs"
authors = "Tyna Eloundou, Sam Manning, Pamela Mishkin, Daniel Rock"
year = 2024
doi = "10.1126/science.adj0998"
arxiv = "2303.10130"
opened = "2026-11-27"

[source.handa2025aei]
type = "preprint"
title = "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations"
authors = "Kunal Handa, Alex Tamkin, Miles McCain, et al."
year = 2025
arxiv = "2503.04761"
opened = "2026-11-27"

[source.jumper2021alphafold]
type = "peer-reviewed"
title = "Highly accurate protein structure prediction with AlphaFold"
authors = "John Jumper, Richard Evans, Alexander Pritzel, et al."
year = 2021
doi = "10.1038/s41586-021-03819-2"
opened = "2026-11-27"

[source.silver2018alphazero]
type = "peer-reviewed"
title = "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play"
authors = "David Silver, Thomas Hubert, Julian Schrittwieser, et al., Demis Hassabis"
year = 2018
doi = "10.1126/science.aar6404"
arxiv = "1712.01815"
opened = "2026-11-27"

[source.brown2019pluribus]
type = "peer-reviewed"
title = "Superhuman AI for multiplayer poker"
authors = "Noam Brown, Tuomas Sandholm"
year = 2019
doi = "10.1126/science.aay2400"
opened = "2026-11-27"

[source.meta2019pluribus]
type = "vendor"
title = "Facebook, Carnegie Mellon build first AI that beats pros in 6-player poker"
authors = "Meta AI"
year = 2019
url = "https://ai.meta.com/blog/pluribus-first-ai-to-beat-pros-in-6-player-poker/"
opened = "2026-11-27"

[source.fair2022cicero]
type = "peer-reviewed"
title = "Human-level play in the game of Diplomacy by combining language models with strategic reasoning"
authors = "Meta Fundamental AI Research Diplomacy Team (FAIR), Anton Bakhtin, Noam Brown, et al."
year = 2022
doi = "10.1126/science.ade9097"
opened = "2026-11-27"

[source.wang2023adversarialgo]
type = "preprint"
title = "Adversarial Policies Beat Superhuman Go AIs"
authors = "Tony T. Wang, Adam Gleave, Tom Tseng, Kellin Pelrine, Nora Belrose, Joseph Miller, Michael D. Dennis, Yawen Duan, Viktor Pogrebniak, Sergey Levine, Stuart Russell"
year = 2023
arxiv = "2211.00241"
opened = "2026-11-27"

[source.novikov2025alphaevolve]
type = "preprint"
title = "AlphaEvolve: A coding agent for scientific and algorithmic discovery"
authors = "Alexander Novikov, Ngan Vu, Marvin Eisenberger, et al."
year = 2025
arxiv = "2506.13131"
opened = "2026-11-27"

[source.deepmind2025imo]
type = "vendor"
title = "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad"
authors = "Thang Luong, Edward Lockhart (Google DeepMind)"
year = 2025
url = "https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/"
opened = "2026-11-27"

[source.white2024livebench]
type = "preprint"
title = "LiveBench: A Challenging, Contamination-Limited LLM Benchmark"
authors = "Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, et al."
year = 2024
arxiv = "2406.19314"
opened = "2026-11-27"

[source.jain2024livecodebench]
type = "preprint"
title = "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"
authors = "Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica"
year = 2024
arxiv = "2403.07974"
opened = "2026-11-27"

[source.zhang2024gsm1k]
type = "preprint"
title = "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
authors = "Hugh Zhang, Jeff Da, Dean Lee, et al."
year = 2024
arxiv = "2405.00332"
opened = "2026-11-27"

[source.kiela2021dynabench]
type = "peer-reviewed"
title = "Dynabench: Rethinking Benchmarking in NLP"
authors = "Douwe Kiela, Max Bartolo, Yixin Nie, et al."
year = 2021
arxiv = "2104.14337"
opened = "2026-11-27"

[source.hai2025aiindex]
type = "report"
title = "The 2025 AI Index Report, Chapter 2: Technical Performance"
authors = "Stanford Institute for Human-Centered Artificial Intelligence"
year = 2025
url = "https://hai.stanford.edu/ai-index/2025-ai-index-report/technical-performance"
opened = "2026-11-27"

[source.vahdati2026arc]
type = "preprint"
title = "The ARC of Progress towards AGI: A Living Survey of Abstraction and Reasoning"
authors = "Sahar Vahdati, Andrei Aioanei, Haridhra Suresh, Jens Lehmann"
year = 2026
arxiv = "2603.13372"
opened = "2026-11-27"

[source.epoch2026hub]
type = "dataset"
title = "Capabilities & benchmarking (benchmark data)"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/benchmarks"
opened = "2026-11-27"
```
