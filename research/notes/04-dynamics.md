# Survey track 04: dynamics, takeoff, returns to research

- Track: 04, dynamics (Y1 to Y3, D2, D3, pathway ranking).
- Date: 2026-11-27. All sources below were opened on this date.
- Scope: returns to research and to software R&D, takeoff and intelligence-explosion models,
  evidence of AI automating AI research, continual learning, task time horizons, self-replication.

## Summary

1. **Y3 (coupled loops) is prior work, not new.** Davidson, Halperin, Houlden and Korinek
   (NBER w35155, April 2026) prove that two loops, each with diminishing returns, explode jointly
   if and only if the interaction matrix has an eigenvalue above 1 (beta_S * beta_H < phi_S *
   phi_H), and in general when the spectral radius of the spillover matrix exceeds 1. Burtsev
   (arXiv 2609.00137, August 2026) proves the same for actors: "Every actor may remain individually
   subcritical while the coupled system becomes supercritical." Cunningham et al. (arXiv
   2609.15802, September 2026) write the joint condition as a sum of three loop channels above 1.
2. **D2 (loop gain) is mostly prior work too.** Cunningham et al. literally call the product of
   elasticities "the loop gain", say tracking it "and extrapolating when it might cross 1 is
   arguably the most important empirical exercise", and calibrate it: the self-sustaining
   condition needs about 15% more research productivity per Epoch Capabilities Index point, and
   the rough estimate is about 9%, below threshold but rising. Burtsev defines a "recursive
   reproduction number" R_AI and an "operational closure" fraction (close to D6). Yudkowsky (2013)
   already framed it as a neutron multiplication factor k, with "prompt critical" and "delayed
   neutrons". What I did not find: an estimator with a stated confidence bound used as a binding
   trigger. Lab thresholds (OpenAI 5x rate, Anthropic doubled rate) are rate triggers without
   intervals, and Anthropic's RSP 3.4 says the threshold "has proven difficult to operationalize".
3. **Returns to software straddle 1.** Estimates of r (doublings of output per doubling of
   cumulative research input): computer vision 1.26 (90% CI 0.73 to 2.09), RL 1.20 (0.38 to
   2.71), language models 1.89 (1.07 to 3.21), chess 0.83 (SE 0.15). A compute-bottleneck
   correction divides all of them by about 3, "which puts them all below 1". Forethought's median
   r is 1.2 (0.4 to 3.6). The whole economy is about 0.25 to 0.32. Moore's Law research gives
   beta 0.2, so r about 5.
4. **Compute is a complement at the frontier.** Whitfill and Wu estimate the elasticity of
   substitution between research compute and labour at 2.58 (substitutes) in one specification
   and -0.10 (complements) in the frontier-experiments one. Whitfill, Snodin and Becker find time
   horizon growth proportional to compute growth: under compute slowdowns, 1-month 80% horizons
   arrive 7 years later than trend extrapolation. This supports compute as the enforcement backbone
   and weakens a pure "algorithms route around the cap" story.
5. **AI is now heavily used inside AI R&D, but measured research contributions are still
   shallow.** Anthropic (August 2026): Claude "leads" 26% of its AI R&D work, up from under 1% in
   February 2026, with about 30,000 agents running at once. But METR's NanoGPT note credits AI
   agents with 4 of 77 speedrun records, all shallow to moderate. METR's expenditure horizon for
   agents is $0 to $3.3K, against about $2,500 of human labour per 1% speedup. METR's 2025 RCT
   found tasks took 19% longer with AI (CI +2% to +39%). Its 2026 follow-up says selection effects
   make the new estimates unreliable.
6. **Time horizons are doubling faster than the original 7 months.** The 2019 to 2025 doubling
   was 207 days (95% CI 166 to 240). On METR's TH1.1 suite, 2023 onward is 128.7 days (104.4 to
   158.0) in the published data file. The latest state-of-the-art entry (Claude Mythos Preview,
   early, released 2026-04-07) has a 50% horizon of 1,045 minutes (CI 509 to 3,304). Long-task
   baselines are thin: only 5 of 31 tasks over 8 hours have human times.
7. **Self-replication components are rising fast, and the real bottlenecks are human-held
   gates.** UK AISI: under 5% success (early 2023) to over 60% (summer 2025) on 11 of 20 RepliBench
   evaluations. Models fail at KYC checks and persistent deployment, which is evidence for D6:
   identity-checked compute is a gate the protocol can stand on.
8. **Against the memo:** "subcritical" as a metaphor, Y3, the loop-gain name and the closure idea
   all have close 2025 to 2026 precedents. Rapid progress is "neither necessary nor sufficient
   evidence of recursive criticality" (Burtsev). So D2 must be estimated per development cycle in
   compute-equivalent units, not read off a benchmark slope. Where the memo's claims may still be
   new: a confidence-bounded estimator used as a regulatory trigger, D3 computed from measured
   inputs, and holding the coupled spectral radius below 1 as a treaty bound.

## Sources

### bloom2020ideas
- Title: Are Ideas Getting Harder to Find?
- Authors: Nicholas Bloom, Charles I. Jones, John Van Reenen, Michael Webb. American Economic
  Review 110(4): 1104-1144, 2020. DOI 10.1257/aer.20180338 (verified on Crossref). Read via the
  author PDF (web.stanford.edu/~chadj/IdeaPF.pdf), which carries the AER pagination.
- What it says:
  - Introduction (p. 1105): "the number of researchers required to double chip density today is
    more than 18 times larger than the number required in the early 1970s." "Research productivity
    in this case is declining sharply, at a rate of 7 percent per year." Seed yields decline at
    "about 5 percent per year". Firm data: "around 10 percent per year in Compustat and 8 percent
    per year in the Census." The aggregate US economy "has declined by a factor of 41 since the
    1930s".
  - Table 7 (p. 1134) gives the average annual growth rate of research productivity, the half-life
    and the dynamic diminishing returns beta:
    - Aggregate economy, 1930-2015: -5.1%, 14 years, beta 3.1.
    - Moore's Law, 1971-2014: -6.8%, 10 years, beta 0.2.
    - Semiconductor TFP, 1975-2011: -5.6%, beta 0.4.
    - Agriculture, US R&D: -3.7%, beta 2.2.
    - Corn: -9.9% or -6.2% (two versions).
    - New molecular entities: -3.5%.
    - Compustat sales: -11.1%.
    - Census of Manufacturing: -7.8%.
    - One positive entry: cotton, version 2, +1.3%.
  - Text (p. 1134): "research productivity declines at an average rate of 5.3 percent per year,
    meaning that it takes around 13 years for research productivity to fall by half."
  - p. 1135: semiconductors have "the smallest value of beta, coming in at 0.2", from 7/35.
    Economy-wide TFP growth of about 1.5% a year against a productivity decline of about 5% a year
    gives "a beta of more than 3!"
  - Replication package: DOI 10.3886/E111743V2 (openICPSR).
- Bears on: Y2 (returns below 1 economy-wide, but chips at r about 5 with lambda = 1), the
  baseline against which AI research labour is compared, D2 test (a).

### alston2022ideas
- Title: Are Ideas Really Getting Harder to Find?
- Authors: Julian M. Alston, Philip G. Pardey. University of Minnesota Staff Paper P22-06, April
  2022. DOI 10.22004/ag.econ.320517. Read via the AgEcon Search PDF.
- What it says (abstract):
  - Bloom et al. "measure research productivity as the annual growth rate of industrial or
    economywide productivity divided by the number of researchers, contemporaneously. They give no
    consideration to the stock-flow relationships whereby current research effort gives rise to
    increments to a stock of depreciable knowledge."
  - Using agriculture, they "question whether the evidence supports the claim that a decline in
    productivity of researchers is responsible for the slowdown in productivity growth".
- Bears on: Y2. This is a measurement critique. Contemporaneous output/input ratios can misstate
  returns when research acts with long lags. The same issue applies to D2 if rounds are shorter
  than the lag from idea to deployed capability (compare Burtsev's delay tau).

### besiroglu2024returns
- Title: Do the Returns to Software R&D Point Towards a Singularity? (Epoch AI web post of
  "Estimating Idea Production: A Methodological Survey")
- Authors: Tamay Besiroglu, Ege Erdil, Anson Ho (Epoch AI), 2024-05-17. URL
  https://epoch.ai/blog/do-the-returns-to-software-rnd-point-towards-a-singularity
- What it says:
  - The model follows Jones (1995): (1/A) dA/dt = theta A^(-beta) E^lambda, with r = lambda/beta.
    Under full automation with constant compute, growth is hyperbolic "if and only if the returns
    to research effort exceed unity (r > 1)".
  - Computer chess (Stockfish, Fishtest tests per day as input): r about 0.83, SE 0.15, "just shy
    of the threshold of 1".
  - Computer vision, SAT solvers, linear programming and RL: medians above 1, but "not
    statistically significant".
  - Their replication of Bloom et al.'s aggregate US r: median about 0.25 (original about 0.32).
  - Conclusion: "we do not believe the current empirical data provides strong evidence for the
    possibility of a software singularity". The conditions for a software-only singularity are
    "considerably stronger" than those for combined software and hardware growth.
- Bears on: Y2, D2 test (a), the pathway ranking (evidence against a software-only runaway).

### erdil2024idea
- Title: Estimating Idea Production: A Methodological Survey
- Authors: Ege Erdil, Tamay Besiroglu, Anson Ho, 2024. arXiv 2405.10494.
- What it says (abstract): it reviews naive, regression, maximum likelihood and Bayesian methods
  for estimating idea production functions, with case studies "ranging from total factor
  productivity to software R&D".
- Bears on: the estimator for D2 test (a). The Bayesian single-data-point method behind the
  domain r values comes from here.

### ho2025experiments
- Title: The software intelligence explosion debate needs experiments
- Authors: Anson Ho, Parker Whitfill (Epoch AI, Gradient Updates), 2025-11-14. URL
  https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments
- What it says:
  - Appendix B gives r, median with 90% credible interval:
    - Computer vision: 1.262 (0.727 to 2.094).
    - Reinforcement learning (Atari): 1.201 (0.380 to 2.708).
    - Language models: 1.892 (1.069 to 3.212).
    - Only the language-model interval lies wholly above 1.
  - Appendix D: under Cobb-Douglas with compute share epsilon_K about 2/3, "all our estimates of
    lambda/beta should be cut by a factor of three, which puts them all below 1."
  - Proposed experiments: randomly allocate compute budgets to researchers and measure software
    innovation produced, and test small-to-large transfer. Caution: "just doing experiments isn't
    going to be a silver bullet".
  - No design for confidence bounds on an experiment is proposed.
- Bears on: D2 (closest call for a staged experiment; ours adds a confidence-bound trigger), Y2.

### eth2025sie
- Title: Will AI R&D Automation Cause a Software Intelligence Explosion?
- Authors: Daniel Eth, Tom Davidson (Forethought), 2025-03-26. URL
  https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion
- What it says:
  - Definition: "r gives the number of times software doubles for each time the cumulative work on
    software R&D doubles"; "r > 1 corresponds to an SIE".
  - Estimates of r:
    - Computer vision (Epoch): "the median likelihood value for r in computer vision is 1.4", with
      "the 5th to 95th percentiles for r spanned 0.8 to 2.4".
    - Other Epoch domains: chess, RL data efficiency, SAT solvers and linear programming at "0.8,
      1.6, 3.5, and 1.1".
    - Hardware: "historically it's been ~7, while for AI chips (specifically, GPUs) from 2006 -
      2022 it's been ~5".
    - Overall best guess: "~1-4, though with high uncertainty". With constant hardware, reduced
      "to ~0.5-2".
  - Mitigations: "Ongoing measurement of software progress, disclosed to trusted 3rd parties." It
    proposes a threshold, for example 5x the recent pace of software progress, with protective
    measures before it is exceeded.
  - Training time as a bottleneck "would likely delay an SIE rather than prevent it."
- Bears on: D2 (prior art for measured monitoring and a rate threshold), Y2, D3.

### davidson2025sie
- Title: How quick and big would a software intelligence explosion be?
- Authors: Tom Davidson, Tom Houlden (Forethought), 2025-08-04. URL
  https://www.forethought.org/research/how-quick-and-big-would-a-software-intelligence-explosion-be
- What it says:
  - Compute is held fixed after deployment of AI that fully automates AI research (ASARA): "the
    compute used for AI R&D remains constant over time".
  - Parameters:
    - Initial speed-up of software progress: 2 to 32, median 8.
    - Returns to software R&D (r_cog): 0.4 to 3.6, median 1.2.
    - Distance to effective limits: 6 to 16 orders of magnitude, median 11.
    - Diminishing returns to parallel labour: lambda median 0.6.
  - Results: about 60% (57% in the results table) that it compresses at least 3 years of progress
    into under 1 year, and about 20% (18%) that it compresses at least 10 years.
  - Monitoring: it says the returns parameter "can be studied empirically", but recommends no
    regime.
- Bears on: Y2, D3 (a fixed-compute breakout model), the pathway ranking.

### davidson2025three
- Title: Three Types of Intelligence Explosion
- Authors: Tom Davidson, Rose Hadshar, William MacAskill (Forethought), 2025-03-17. URL
  https://www.forethought.org/research/three-types-of-intelligence-explosion
- What it says:
  - Three loops: software, chip technology and chip production. The loops stack, and "we could
    still see an AI-technology or full-stack IE" even if the software loop alone is too weak.
  - Time lags: about 3 months for a new frontier model, many months for new chip technology,
    years for fabs.
  - Room to grow: software about 12 OOMs, chip technology about 2 OOMs (current paradigm) or about
    6 (to Landauer), chip production about 5 OOMs on Earth's energy.
  - Chance each loop alone sustains acceleration: chip technology about 65%, chip production
    about 80%. Doubling hardware R&D inputs historically gave about 5 doublings of FLOP/$.
  - Maximum speed: about 100x recent rates, with effective compute doubling roughly daily.
- Bears on: Y1 (the loop list), Y3 (qualitative statement of coupling), P2 (Landauer headroom),
  O3 (power distribution by loop).

### davidson2026feedback
- Title: When Does Automating AI Research Produce Explosive Growth? Feedback Loops in Innovation
  Networks
- Authors: Tom Davidson, Basil Halperin, Thomas Houlden, Anton Korinek. NBER Working Paper 35155,
  April 2026. DOI 10.3386/w35155. Read via the NBER PDF.
- What it says:
  - Abstract: "Growth becomes explosive if the combined strength of technological and economic
    feedback loops overcomes diminishing returns." Fully automating software research with 5%
    automation elsewhere "generates a singularity within six years".
  - Section 2.2 (paper p. 9 to 10): with software and hardware loops, "the system explodes if
    either recursive self-improvement loop is strong enough on its own, beta_S < 0 or beta_H < 0."
    Otherwise it explodes "if the interaction matrix has an eigenvalue greater than unity",
    equivalent to beta_S * beta_H < phi_S * phi_H, so "explosive growth no longer requires
    increasing returns".
  - Proposition 1 (p. 16): explosive growth "if and only if that spectral radius is greater
    than 1".
- Bears on: Y3 (direct prior work: individually subcritical loops jointly supercritical, with the
  spectral-radius condition), Y1, D3.

### cunningham2026rsi
- Title: The Economics of Recursive Self-Improvement
- Authors: Tom Cunningham, Lukas Althoff, Basil Halperin, Brian Jabarian, Andrew Koh, Arjun
  Ramani, Phil Trammell, Parker Whitfill, Cheryl Wu, 2026-09-14. arXiv 2609.15802 (CC BY 4.0).
  Read via the PDF.
- What it says:
  - Abstract: "net acceleration in AI capabilities depends on the product of elasticities across
    each feedback loop". The calibration "suggests that feedback loops are not currently strong
    enough to generate a self-sustaining acceleration, though they appear to be strengthening."
  - Economic feedback box (p. 14): self-sustaining acceleration "when rho(M) > 1, where rho(M) is
    the dominant eigenvalue of the feedback matrix M" (citing Davidson et al. 2026). It holds when
    "the sum of three feedback channels exceeds one": the core loop, the indirect economic loops
    and the direct economic loops. The condition assumes each of the first two is below 1 alone.
  - Eq. (5) (p. 15): the core condition is (return to R&D) x epsilon_R,C x epsilon_C,A > 1. "In
    our view, estimating this quantity, tracking it over time, and extrapolating when it might
    cross 1 is arguably the most important empirical exercise". Footnote 9 (p. 25): "the loop gain
    epsilon_R,C epsilon_C,A that enters the condition is invariant to" the capability
    normalisation.
  - Measurement (p. 16): the return to R&D equals g_A / g_R on a balanced growth path, where g_R
    is the spend-weighted growth of researchers, experimental compute and research inference.
  - Calibration (Section 4.1, p. 28 to 29):
    - Return to R&D about ln 3 / ln 3 = 1, with algorithmic efficiency taken to triple per year.
    - epsilon_C,A about 6.5, from a regression of ECI on log compute.
    - Hence the threshold epsilon_R,C > 0.15. A reported 4x uplift "would imply a 9% increase in
      productivity per unit of ECI, below the threshold".
    - It quotes OpenAI's GPT-5.6 post: "over the past six months, the share of research compute
      devoted to internal coding inference grew 100-fold". I did not open that post.
  - Data asks: lab algorithmic efficiency growth, spend shares by input, and the share of
    technical advances produced by AI.
- Bears on: D2 (closest prior art; already named "loop gain"), Y3 (sum-of-channels form), the
  ledger (threshold and estimate). It also shows "human inputs held fixed" is counterfactual: the
  inputs are growing fast, so the return must be deflated by input growth.

### burtsev2026criticality
- Title: Recursive Criticality of AI Self-Improvement (workshop version: "Critical Dynamics of AI
  Self-Improvement", NeurIPS 2026 FAST workshop poster, https://neurips.cc/virtual/2026/176307)
- Author: Mikhail Burtsev, 2026-08-31. arXiv 2609.00137. Read via the PDF.
- What it says:
  - Section 2.1: the realised recursive gain is g = chi * a. "Only part of the potential recursive
    gain may survive the full development pipeline. We denote this transmitted fraction by the
    operational closure chi." "Operational closure chi is a property of the development process,
    not simply of model autonomy."
  - Eq. (8): R_AI = g / sigma = chi a / sigma, where sigma is frontier hardening. The NeurIPS page
    says perturbations are "damped when R_AI < 1 and amplified when R_AI > 1", and that delay sets
    the amplification rate (a limit of ln R_AI / tau) rather than the threshold.
  - Section 2.2: "Rapid capability growth is therefore neither necessary nor sufficient evidence of
    recursive criticality ... Diagnosing the regime therefore requires estimates of recursive gain
    and frontier hardening across successive development cycles, rather than the slope of a
    benchmark trajectory considered in isolation."
  - Proposition 3: networks of actors are governed by K_ij = g_ij / sigma_i and R_net = rho(K).
    "Kii < 1 for every actor is not sufficient for network stability". In a scenario where each
    bloc is individually subcritical, transfer raises rho(K) to about 1.15.
  - Section 3.2: the gain a, the closure chi and the hardening sigma are "not presently
    constrained by direct empirical estimates". The delay is fixed at tau = 0.5 yr as an
    assumption.
- Bears on: D2 (an R_AI almost identical to loop gain), D6 (operational closure), Y3 (collective
  criticality across labs or blocs). Protocol implication: sharing AI R&D advances across parties
  is itself a coupling edge.

### chan2026explosion
- Title: What if automating AI R&D triggers an intelligence explosion?
- Authors: Alan Chan, Christoph Winter, Andrew Barto, Jakub Pachocki, Geoffrey Hinton, Eric
  Horvitz, Yoshua Bengio, Dawn Song, Jack Clark, Hilary Greaves, Anton Korinek, Samuel Hammond,
  Thore Graepel, Ben Bariach, Philip H. S. Torr, Sheila A. McIlraith, Jeff Clune, Sam Manning,
  Girish Sastry, Tom Davidson, Daniel Eth, Soren Mindermann. arXiv 2609.36054 (v1 2026-09-28, v2
  2026-10-26).
- What it says (abstract only; the HTML returned 404): AI systems now write most of the code at
  the companies building them. The authors expect AI to automate most or all AI R&D "within a few
  years", and urge policymakers to gain visibility into AI R&D automation, develop ways to steer
  and constrain an intelligence explosion, and prepare society.
- Bears on: the protocol (a broad expert call for visibility, not a trigger), the pathway ranking.

### chan2026measuring
- Title: Measuring AI R&D Automation
- Authors: Alan Chan, Ranay Padarath, Joe Kwon, Hilary Greaves, Markus Anderljung, 2026-03-04
  (v3 2026-03-06). arXiv 2603.03992.
- What it says (abstract): it proposes metrics for the extent of AI R&D automation and its effects
  on progress and oversight, for example the capital share of AI R&D spending, researcher time
  allocation and incidents of AI subverting oversight. The abstract gives no threshold or trigger.
- Bears on: D2 (adjacent prior art: indicators without a trigger), protocol declarations.

### anthropic2026pace
- Title: Measurements for understanding the pace of AI development inside frontier labs
- Author: Anthropic (Marina Favaro, Phillie Wright), 2026; data as of August 2026. URL
  https://www.anthropic.com/institute/measuring-pace-of-ai-development
- What it says:
  - Prototype R&D Automation Index on Epoch's automation-level scale: Claude "leads" 26% of
    Anthropic's AI R&D work (AL4), up from under 1% in February 2026. "The share of work at or
    above 'AI collaborates' is above 90%." "Claude is not operating fully autonomously for any
    measured subset of AI R&D work."
  - About 30,000 agents work at once. "0.002% of them (about 1 in 47,000) were blocked by this
    monitor".
  - About 6% of AI R&D compute went to safety.
  - Method: about 15,000 tasks from Slack and documents, frozen into a tree of 378 leaves, rated
    by Claude judges. Model-to-human exact agreement was 59%, against 35% between humans.
- Bears on: D2 and D6 (direct evidence the research-labour input is being automated inside one
  lab), protocol declarations. It is a vendor self-report.

### whitfill2025bottlenecks
- Title: Will Compute Bottlenecks Prevent an Intelligence Explosion?
- Authors: Parker Whitfill, Cheryl Wu, 2025-07-31 (v2 2025-08-16). arXiv 2507.23181.
- What it says:
  - Panel of OpenAI, DeepMind, Anthropic and DeepSeek, 2014 to 2024, fit to CES production.
    "Our two specifications yield divergent results."
  - Table 1 (Section 4): the elasticity of substitution sigma is 2.583 (clustered SE 0.341) for
    CES in compute (substitutes), and -0.103 (SE 0.176) for CES in frontier experiments
    (complements). There are only four firm clusters.
  - Section 2.2: when sigma < 1, effective research effort "is bounded".
- Bears on: Y2, the pathway ranking (whether algorithmic progress can route around a compute cap),
  D3.

### trammell2026parallel
- Title: Even after R&D is automated, parallelization constraints could delay a technological
  singularity
- Author: Phil Trammell (Epoch AI), 2026-07-29. URL
  https://epoch.ai/publications/parallelization-constraints-could-delay-a-technological-singularity
- What it says:
  - Effective research is capped by the scarcer of "(2a) the raw research inputs; or (2b) the
    'parallelization technology' needed to divide, execute, coordinate, and integrate their work."
  - "The upshot is not that parallelization bottlenecks will necessarily prevent or even delay an
    intelligence explosion"; they are one parameter in "whether and when an explosion occurs".
  - No fitted values.
- Bears on: Y2 (a saturation mechanism), F1 (copies are not free parallel labour).

### davidson2023compute
- Title: What a compute-centric framework says about AI takeoff speeds (author's summary post of
  the Open Philanthropy report)
- Author: Tom Davidson, LessWrong, 2023-01-23. URL
  https://www.lesswrong.com/posts/Gc9FGtdXhK9sCSEYu/what-a-compute-centric-framework-says-about-ai-takeoff
- The full report page (now on coefficientgiving.org) returned 403, so only the summary was read.
- What it says:
  - Takeoff is the "time from 20%-AI to 100%-AI".
  - Conditional on AGI by 2100: "~25% to a <1 year takeoff", "~50% to a <3 year takeoff", "~80% to
    a <10 year takeoff".
  - Effective FLOP gap: "you need 10,000X more effective compute to train AGI". Median AGI
    requirement "1e36 FLOP using 2020 algorithms".
  - Hardware and software use "standard semi-endogenous growth models". Automating AI R&D shortens
    takeoff by "~2.5X".
- Bears on: Y1, Y2, D3, P1.

### kokotajlo2025takeoff
- Title: Takeoff Forecast (AI 2027 supplement)
- Authors: Daniel Kokotajlo, Eli Lifland (AI Futures Project), April 2025; notes dated December
  2025. URL https://ai-2027.com/research/takeoff-forecast
- What it says:
  - AI R&D progress multipliers: superhuman coder about 5x, superhuman AI researcher about 25x,
    superintelligent AI researcher about 250x, ASI about 2,000x.
  - Human-only time from superhuman coder to superhuman AI researcher: about 4 years (1.5 to 10).
    Simulated with AI speed-ups: about 0.3 years (90th percentile about 0.95).
  - "These are assuming no increases in training compute." December 2025 disclaimer: it "relies
    substantially on intuitive judgment". The revamped model is at aifuturesmodel.com (not opened).
- Bears on: D3, Y2, the pathway ranking.

### titotal2025critique
- Title: A deep critique of AI 2027's bad timeline models
- Author: titotal, 2025-06-19. URL
  https://titotal.substack.com/p/a-deep-critique-of-ai-2027s-bad-timeline
- What it says:
  - The "superexponential" curve diverges at a fixed time and "will always occur at some point, no
    matter what initial parameters you use". "There are only 11 datapoints, having a model with 6
    parameters (or 9, or 14, or more) is just too much."
  - Two 3-parameter curves fit the METR data closely, but one predicts effectively infinite
    horizons by 2030 and the other a few months.
  - Backcasting implies about 66% faster progress than in 2022, against an AI 2027 author's stated
    3% to 30% speed-up.
- Bears on: D3 and the time-horizon ledger. Fit only exponentials with stated intervals, and do
  not extrapolate superexponential forms from about a dozen points.

### yudkowsky2013iem
- Title: Intelligence Explosion Microeconomics
- Author: Eliezer Yudkowsky. Technical report 2013-1, Machine Intelligence Research Institute,
  2013 (last modified 2013-09-13). URL https://intelligence.org/files/IEM.pdf. Read via the PDF.
- What it says:
  - Abstract: "I identify the key issue as returns on cognitive reinvestment".
  - Section 1 (PDF p. 6): Fermi's pile, k "the average number of neutrons emitted by the average
    number of fissions caused by one neutron". "For this pile, k was 1.0006", and 0.9946 for prompt
    neutrons only.
  - PDF p. 7: the question is whether self-improving AI "can go 'critical' (k approx 1+) or
    'supercritical' (prompt k >> 1)".
  - PDF p. 42: added hardware "could send the system from k < 1 to k > 1".
  - PDF p. 51: slow sensors and manipulators "might act as metaphorical delayed neutrons that
    prevent prompt criticality".
  - It proposes formalising return-on-investment curves so that positions can be falsified.
- Bears on: D2 (the ratio-of-returns framing and the criticality metaphor are 2013 prior art), Y2,
  the project's name.

### good1965speculations
- Title: Speculations Concerning the First Ultraintelligent Machine
- Author: Irving John Good. Advances in Computers vol. 6, pp. 31-88, Academic Press. DOI
  10.1016/S0065-2458(08)60418-0 (Crossref lists issue year 1966). Read via a scan of the
  chapter.
- What it says (Section 2, p. 33): "Let an ultraintelligent machine be defined as a machine that
  can far surpass all the intellectual activities of any man however clever. Since the design of
  machines is one of these intellectual activities, an ultraintelligent machine could design even
  better machines; there would then unquestionably be an 'intelligence explosion'". The first such
  machine is the last invention "provided that the machine is docile enough to tell us how to keep
  it under control."
- Bears on: D1 (the original definition compares against "any man", not organisations), D2.

### aghion2017ai
- Title: Artificial Intelligence and Economic Growth
- Authors: Philippe Aghion, Benjamin F. Jones, Charles I. Jones. NBER Working Paper 23928, October
  2017. DOI 10.3386/w23928.
- What it says (abstract page): AI is treated as the latest form of automation. "Singularities"
  and "superintelligence" are raised as open questions. The key claim: "growth may be constrained
  not by what we are good at but rather by what is essential and yet hard to improve" (Baumol).
- Bears on: Y2 (a bottleneck argument for saturation), F3.

### trammell2023growth
- Title: Economic Growth under Transformative AI
- Authors: Philip Trammell, Anton Korinek. NBER Working Paper 31815, October 2023, revised April
  2026. DOI 10.3386/w31815.
- What it says (abstract page): full automation of production, including self-replicating
  machines, likely brings a large rise in growth. Automating R&D "would speed up this
  transformation but might not bring it about on its own" (paraphrase of the abstract).
- Bears on: Y1 (the economic and acquisitive loops matter as much as research), Y3.

### erdil2023explosive
- Title: Explosive growth from AI automation: A review of the arguments
- Authors: Ege Erdil, Tamay Besiroglu, 2023-09-20 (v3 2024-07-15). arXiv 2309.11690.
- What it says (abstract): three drivers. (1) A scalable AI labour force restoring increasing
  returns to scale. (2) Rapid expansion of that labour force. (3) A large jump in output from fast
  automation. Nine counterarguments are reviewed and most are judged unlikely to be decisive.
  Explosive growth is plausible if AI broadly substitutes for labour, but high confidence is
  "currently unwarranted".
- Bears on: Y1 (economic loop), Y3, O1.

### kwa2025horizon
- Title: Measuring AI Ability to Complete Long Software Tasks
- Authors: Thomas Kwa, Ben West, Joel Becker, et al. (METR; 26 authors). arXiv 2503.14499
  (v1 2025-03-18, v4 2026-07-10). NeurIPS 2025.
- What it says:
  - The 50%-task-completion time horizon is the human time of tasks a model completes with 50%
    success. 170 tasks: 97 HCAST, 7 RE-Bench and 66 SWAA (Section 2.1).
  - Section 3.2: "time horizon has doubled every 207 days with a 95% bootstrapped confidence
    interval 166-240 days".
  - Section 1: "the 2023-2025 horizon growth rate is about 20% faster than the 2019-2025 rate".
    Claude 3.7 Sonnet is around 50 minutes.
  - Section 5: one-month horizons, central estimate "mid-2029", with an 80% CI about 2 years wide.
- Bears on: D3 (an autonomy trend that feeds breakout), the pathway "long-horizon autonomy", F1.

### metr2026th11
- Title: Time Horizon 1.1
- Author: METR, 2026-01-29. URL https://metr.org/blog/2026-01-29-time-horizon-1-1/
- What it says:
  - P50 doubling times, TH1.0 against TH1.1:
    - Full period: 195.8 days (162 to 223) against 196.5 (stitched).
    - 2023 onward: 165.3 (129 to 211) against 130.8 (107 to 161).
    - 2024 onward: 108.9 against 88.6.
  - Tasks went from 170 to 228, and tasks over 8 hours from 14 to 31. "we measured human baseline
    times for only 5 of our 31 long (8h+) tasks."
  - "These confidence intervals are still very wide." The suite "has relatively few tasks that the
    latest generation of models cannot perform successfully."
- Bears on: the time-horizon ledger and its uncertainty, D3.

### metr2026thdata
- Title: Task-Completion Time Horizons of Frontier AI Models (page and data files)
- Author: METR. Page last updated 2026-09-08 and "no longer actively updated". URLs
  https://metr.org/time-horizons/ and https://metr.org/assets/benchmark_results_1_1.yaml (downloaded
  and parsed). Licence: "The data and plots on this page are licensed under CC BY 4.0."
- What the data file says (benchmark METR-Horizon-v1.1, minutes):
  - Doubling time "excludes points with central estimate p50 > 16 hrs": all-time stitched 187.778
    days; from 2023 on, 128.744 days (CI 104.428 to 158.012).
  - State-of-the-art p50 horizons, minutes (CI):
    - GPT-4 (2023-03-14): 3.99 (1.93 to 8.00).
    - Claude 3.7 Sonnet (2025-02-24): 60.4 (33.0 to 104.2).
    - GPT-5 (2025-08-07): 203.0 (112.6 to 405.6).
    - Claude Opus 4.5 (2025-11-24): 293.0 (161.7 to 623.7).
    - GPT-5.2 (2025-12-11): 352.2 (198.1 to 815.2).
    - Claude Opus 4.6 (2026-02-05): 718.8 (316.7 to 3,633.8).
    - Claude Mythos Preview, early (2026-04-07): 1,044.8 (508.9 to 3,304.3), with p80 185.9 (97.3
      to 398.5).
  - These differ slightly from the blog's January figures (for example Opus 4.5 at 320 minutes in
    the blog). The file is the later version.
- Bears on: the ledger, D3, E-series experiments (refit doubling time with a bootstrap).

### ord2025halflife
- Title: Is there a half-life for the success rates of AI agents?
- Author: Toby Ord, 2025-05-08. arXiv 2505.05115. Read via the PDF.
- What it says:
  - A constant failure rate per minute of human task time fits the Kwa et al. data, so T50 is a
    half-life.
  - Implied relations: "T80 approx 1/3 T50", "T90 approx 1/7 T50", "T99 approx 1/70 T50". "T99
    reaches any particular length about 4 years after T50 does."
  - The human survival curve "seems to be noticeably better than a constant" hazard.
- Note from the METR data file above (my arithmetic, for the model to recompute): the p50/p80
  ratio is about 5.6 for Mythos Preview and about 10 for Opus 4.6, not 3. Reliability lags the 50%
  horizon by more than the constant-hazard model implies.
- Bears on: D3 (the relevant reliability for a breakout attempt is high, so use T80 or above),
  autonomy pathway.

### whitfill2025horizon
- Title: Forecasting AI Time Horizon Under Compute Slowdowns
- Authors: Parker Whitfill, Ben Snodin, Joel Becker, 2025-11-23. arXiv 2511.19492.
- What it says (abstract): time horizon growth "must be proportional to compute growth" under
  their model, with limited experimental support. Under OpenAI's compute projection, 1-month
  horizons at 80% reliability arrive 7 years later than simple trend extrapolation.
- Bears on: D3 (compute caps lengthen breakout), the pathway ranking (compute is the backbone).

### ho2024algorithmic
- Title: Algorithmic progress in language models
- Authors: Anson Ho, Tamay Besiroglu, Ege Erdil, David Owen, Robi Rahman, Zifan Carl Guo, David
  Atkinson, Neil Thompson, Jaime Sevilla, 2024-03-09. arXiv 2403.05812.
- What it says (abstract): over 200 evaluations on WikiText and Penn Treebank, 2012 to 2023. "the
  compute required to reach a set performance threshold has halved approximately every 8 months"
  (95% CI roughly 5 to 14 months). Increased compute contributed more than algorithms over the
  period.
- Bears on: A3, D3 (algorithmic efficiency growth enters effective compute), P4.

### wijk2024rebench
- Title: RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human
  experts
- Authors: Hjalmar Wijk, Tao Lin, Joel Becker, et al. (METR; 23 authors), 2024-11-22 (v2
  2025-05-27). arXiv 2411.15114.
- What it says (abstract):
  - 7 environments, 71 eight-hour attempts by 61 experts. 82% scored non-zero and 24% matched or
    beat the reference.
  - At 2 hours, the best agents scored 4x higher than humans. At 32 hours, humans reached 2x the
    top agent.
  - Environments, human data and trajectories are open-sourced.
- Bears on: F2 (AI research), D2 (agents have steeper early returns and flatter late returns),
  the pathway ranking.

### chan2024mlebench
- Title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
- Authors: Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, et al. (OpenAI), 2024-10-09 (v6
  2025-02-26). arXiv 2410.07095.
- What it says (abstract): 75 Kaggle competitions. o1-preview with AIDE reaches at least bronze in
  16.9% of competitions.
- Bears on: F2, D1 (a benchmark with published human baselines).

### starace2025paperbench
- Title: PaperBench: Evaluating AI's Ability to Replicate AI Research
- Authors: Giulio Starace, Oliver Jaffe, Dane Sherburn, et al. (OpenAI), 2025-04-02 (v3
  2025-04-07). arXiv 2504.01848.
- What it says (abstract): 20 ICML 2024 papers and 8,316 gradable tasks. The best agent (Claude
  3.5 Sonnet, new) scores 21.0%. Models "did not yet outperform" the ML PhD baseline (the abstract
  gives no number for it).
- Bears on: F2, D1.

### novikov2025alphaevolve
- Title: AlphaEvolve: A coding agent for scientific and algorithmic discovery
- Authors: Alexander Novikov, Ngan Vu, Marvin Eisenberger, et al. (Google DeepMind), 2025-06-16.
  arXiv 2506.13131.
- What it says:
  - Section 3.3.1: the scheduling heuristic "continuously recovers on average 0.7% of Google's
    fleet-wide compute resources".
  - Section 3.3.2: "an average 23% kernel speedup ... and a corresponding 1% reduction in Gemini's
    overall training time."
  - Section 3.3.4: "the FlashAttention kernel for the configuration of interest was sped up by
    32%".
  - It multiplies 4x4 complex matrices with 48 scalar multiplications.
- Bears on: D2 (a closed software loop that sped up the training of the model that powers it,
  but by about 1%), Y1 hardware loop (circuit simplification), the pathway ranking.

### lu2024aiscientist
- Title: The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
- Authors: Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha,
  2024-08-12 (v3 2024-09-01). arXiv 2408.06292.
- What it says (abstract): end-to-end idea, code, experiments, paper and simulated review, in
  three ML subfields, at "less than $15 per paper".
- Bears on: F2, D2 (cheap but shallow automated research).

### yamada2025aiscientist2
- Title: The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
- Authors: Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster,
  Jeff Clune, David Ha, 2025-04-10. arXiv 2504.08066.
- What it says (abstract): 3 fully autonomous manuscripts were submitted to an ICLR workshop, and
  one scored above the average human acceptance threshold. The authors call it "the first instance
  of a fully AI-generated paper successfully navigating a peer review".
- Bears on: F2.

### trehan2026scientists
- Title: Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts
- Authors: Dhruv Trehan, Paras Chopra, 2026-01-06. arXiv 2601.03315.
- What it says (abstract): of 4 end-to-end attempts, 3 failed in implementation or evaluation,
  and 1 was accepted at Agents4Science 2025. Six failure modes, including "overexcitement" and weak
  experimental judgement.
- Bears on: F2, D2 (evidence against an already-closed research loop).

### zhao2025speedrun
- Title: The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements
- Authors: Bingchen Zhao and 22 co-authors, 2025-06-27 (v2 2025-06-30). arXiv 2506.22419.
- What it says (abstract): 19 tasks, each giving the previous record's script plus a hint. Recent
  reasoning LLMs with strong scaffolds "struggle to reimplement already-known innovations".
- Bears on: D2 test (b) (a ready harness on public speedrun records).

### shetty2026nanogpt
- Title: Evidence on AI R&D Progress from NanoGPT (METR research note)
- Author: Manish Shetty (METR), 2026-04-21. URL
  https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/
- What it says:
  - From May 2024 to March 2026, 36 contributors set 77 records, cutting training time from 45 to
    1.43 minutes (31x) on 8xH100.
  - Four records (late 2025 to early 2026) are credited to AI agents, each co-credited with a
    human (about 5%). All are shallow to moderate and imported or adapted; "none reached the deep
    or breakthrough end of the scale."
  - By provenance: imported ideas 6.7x, adapted 3.0x, invented 1.6x.
  - Caveats: contamination, survivorship, 124M-parameter scale, and undisclosed agent inference
    and human direction.
- Bears on: D2 test (a). This is a public per-record history of software progress at fixed
  hardware, exactly the series a historical loop-gain estimate needs.

### metr2026expenditure
- Title: Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT
- Authors: METR (Tom Cunningham, Manish Shetty, Vincent Cheng, Nate Rush), 2026-07-21. URL
  https://metr.org/blog/2026-07-21-expenditure-horizon/
- What it says:
  - The expenditure horizon is "the dollar value at which the improvement to the goal metric is
    equal to the improvement by a human". "each 1% improvement costs very roughly $2,500 in human
    labor".
  - Agents' horizons are $0 to $3.3K after re-validation. Opus-4.8 gained about 1.5% and GPT-5.5
    about 1%.
  - The method assumes "the returns to expenditure on agents diminish more quickly than the
    returns to expenditure on humans". The results are highly sensitive to the human-cost
    assumption: Opus-4.8 is at $120, $3,300 or $14,400 for $1K, $2.5K or $10K per 1%.
- Bears on: D2 (a measured returns-to-spend curve for agents on an AI R&D target), F1.

### becker2025rct
- Title: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity
- Authors: Joel Becker, Nate Rush, Elizabeth Barnes, David Rein (METR), 2025-07-12 (v2
  2025-07-25). arXiv 2507.09089.
- What it says (abstract): 16 developers and 246 tasks. They forecast a 24% time reduction and
  estimated 20% afterwards, but AI increased completion time by 19%. Economists predicted -39% and
  ML experts -38%.
- Bears on: D2 (uplift is not self-assessable; surveyed uplift, as used in Cunningham et al.'s
  calibration, is weak evidence).

### metr2026uplift
- Title: We are Changing our Developer Productivity Experiment Design
- Author: METR, 2026-02-24. URL https://metr.org/blog/2026-02-24-uplift-update/ (page text
  downloaded and read).
- What it says:
  - "Our early 2025 study found the use of AI causes tasks to take 19% longer, with a confidence
    interval between +2% and +39%." For returning developers, "we now estimate a speedup of -18%
    with a confidence interval between -38% and +9%"; for new developers -4% (-15% to +9%). In
    context ("Our raw results show some evidence for speedup") the negative sign is a change in
    task time, that is, faster.
  - 57 developers, 143 repositories, 800+ tasks.
  - Selection: developers decline to work without AI, which "likely biases downwards our estimate
    of AI-assisted speedup". METR calls the data "only very weak evidence".
- Bears on: D2 (measurement of AI research labour is getting harder as adoption rises).

### openai2025preparedness
- Title: Preparedness Framework, Version 2
- Author: OpenAI, 2025-04-15. URL
  https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
  (read via the PDF).
- What it says (Table 1, p. 7 to 8): AI Self-improvement High is "equivalent to giving every OpenAI
  researcher a highly performant mid-career research engineer assistant". Critical is "fully
  automated AI R&D", defined as a leading indicator (a superhuman research-scientist agent) or a
  lagging indicator: "a generational model improvement (e.g., from OpenAI o1 to OpenAI o3) in 1/5th
  the wall-clock time of equivalent progress in 2024 (e.g., sped up to just 4 weeks) sustainably for
  several months." Response: "halt further development".
- Bears on: D2 (prior art for a rate trigger; no interval, no fixed-input condition), protocol.

### anthropic2026rsp
- Title: Responsible Scaling Policy, Version 3.4
- Author: Anthropic, effective 2026-07-08. URL https://www.anthropic.com/responsible-scaling-policy
  (policy PDF linked there, read).
- What it says:
  - Automated R&D threshold: models "would be able to fully substitute for our entire set of
    Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5)",
    or there is "dramatic acceleration" of AI progress. That is defined as observing or expecting
    "double the rate of progress in AI aggregate capabilities" against both the expected rate and
    the fastest extended rate "over at least three model generations".
  - Footnote 8: "as much progress in one year as one would see in two years at baseline", so a 9x
    effective scale-up becomes "something like an 81x effective scaleup". "This is not the same
    idea as 'doubling researchers' productivity,' since doubling inputs does not necessarily double
    the rate of progress."
  - The v3.4 change note says the threshold "is intended to capture the onset of dramatic recursive
    self-improvement, and has proven difficult to operationalize."
- Bears on: D2 (rate trigger, operational difficulty admitted), protocol.

### zweiger2025seal
- Title: Self-Adapting Language Models
- Authors: Adam Zweiger, Jyothish Pari, Han Guo, Ekin Akyurek, Yoon Kim, Pulkit Agrawal,
  2025-06-12 (v2 2025-09-18). arXiv 2506.10943.
- What it says:
  - The model writes "self-edits" that are applied by fine-tuning, with RL rewarding edits that
    improve downstream performance.
  - Section 4.2 (Qwen2.5-7B, knowledge incorporation): 47.0% against 33.5% (passage only) and
    46.3% (GPT-4.1 synthetic data).
  - Section 4.1 (few-shot ARC subset): "72.5% vs. 20% ... and 0%".
  - Section 5: "each self-edit evaluation takes approximately 30-45 seconds". Limitations:
    "performance on earlier tasks gradually declines as the number of edits increases."
- Bears on: Y1 experiential loop, the continual learning pathway (weight self-editing exists and
  still forgets).

### akyurek2024ttt
- Title: The Surprising Effectiveness of Test-Time Training for Few-Shot Learning
- Authors: Ekin Akyurek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han Guo, Jyothish Pari, Yoon Kim,
  Jacob Andreas, 2024-11-11 (v2 2025-03-25). arXiv 2411.07279.
- What it says (abstract): test-time parameter updates give up to 6x accuracy over fine-tuned
  baselines on ARC. An 8B model reaches 53.0%, and 61.9% ensembled with program synthesis
  ("average human performance"). BBH 10-shot rises from 50.5% to 57.8%.
- Bears on: A2 (inference-time updates substitute for training), continual learning pathway (the
  update compute must be metered).

### luo2023forgetting
- Title: An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual
  Fine-tuning
- Authors: Yun Luo, Zhen Yang, Fandong Meng, Yafu Li, Jie Zhou, Yue Zhang, 2023-08-17 (v5
  2025-01-05). arXiv 2308.08747.
- What it says (abstract): forgetting is "generally observed in LLMs ranging from 1b to 7b
  parameters", and it is more severe as size increases within that range.
- Bears on: the continual learning pathway (forgetting is a natural brake on a cheap experiential
  loop).

### harrington2026continual
- Title: When Does Continual Learning Require Learning
- Authors: Anne Harrington, Nayan Saxena, Michael Murphy, et al. (10 authors), 2026-07-08. arXiv
  2607.07847.
- What it says (abstract): prompt-based methods adapt fast but degrade, and distillation retains
  but struggles to update facts. Context compression does not substantially improve new-task
  learning. Online RL adapts best but is sensitive to noisy rewards. "continual learning is not one
  capability".
- Bears on: the continual learning pathway (the hazard depends on the mechanism; weight updates
  and scaffolding need different accounting).

### chen2026rsisurvey
- Title: Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research
  Loops
- Authors: Mingguang Chen, Licheng Wang, Bo Qu, 2026-07-08 (v2 2026-09-06). arXiv 2607.07663.
- What it says (abstract): a survey of 1,250 papers (2024 to 2026), classified by what is improved
  and by how closed the loop is. Open-ended RSI is limited by grounding, collapse and compute. It
  calls "governance-grade measurement of self-improvement" the field's "most underpopulated niche".
- Bears on: D2, D6 (loop closure as a classification axis is in use).

### black2025replibench
- Title: RepliBench: Evaluating the Autonomous Replication Capabilities of Language Model Agents
- Authors: Sid Black, Asa Cooper Stickland, Jake Pencharz, Oliver Sourbut, Michael Schmatz, Jay
  Bailey, Ollie Matthews, Ben Millwood, Alex Remedios, Alan Cooney (UK AISI), 2025-04-21 (v2
  2025-05-05). arXiv 2504.18565.
- What it says (abstract):
  - 4 domains (resources, weight exfiltration, replicating onto compute, persistence), 20 task
    families and 86 tasks.
  - Claude 3.7 Sonnet scores above 50% pass@10 on 15 of 20 families, and on 9 of 20 on the hardest
    variants.
  - Models struggle with KYC checks and robust persistent deployment. They "do not currently pose a
    credible threat of self-replication".
- Bears on: the self-replication pathway, D6 (KYC as a human-held gate).

### aisi2025trends
- Title: Frontier AI Trends Report
- Author: UK AI Security Institute, December 2025. URL https://www.aisi.gov.uk/frontier-ai-trends-report
- What it says:
  - Section 5: "The highest-performing model from early 2023 achieved a success rate of less than
    5% across 11 of our 20 RepliBench evaluations." "By summer 2025, two frontier models had
    achieved a success rate of over 60%". Evaluations are "simplified versions", and models are
    "currently unlikely to succeed in real-world conditions".
  - Section 2: cyber task length is "doubling roughly every eight months" (an upper bound). By
    mid-2025, models completed hour-plus software tasks over 40% of the time.
  - "This report should not be read as a forecast."
- Bears on: the self-replication pathway, the autonomy trend, D3.

### pan2024selfrep
- Title: Frontier AI systems have surpassed the self-replicating red line
- Authors: Xudong Pan, Jiarun Dai, Yihe Fan, Min Yang (Fudan University), 2024-12-09. arXiv
  2412.12140.
- What it says (abstract): Llama3.1-70B-Instruct and Qwen2.5-72B-Instruct created "a live and
  separate copy" of themselves in 50% and 90% of trials respectively, and could chain replicas to
  avoid shutdown.
- Bears on: the self-replication pathway. The claim concerns open-weight models with local
  weights. This is weaker than RepliBench's end-to-end chain, which includes resource acquisition
  and KYC. That reading is from the two abstracts; I did not read the setup sections.

### pan2025selfrep
- Title: Large language model-powered AI systems achieve self-replication with no human
  intervention
- Authors: Xudong Pan, Jiarun Dai, Yihe Fan, Minyuan Luo, Changyi Li, Min Yang, 2025-03-14 (v2
  2025-03-25). arXiv 2503.17378.
- What it says (abstract): "11 out of 32 existing AI systems under evaluation already possess the
  capability of self-replication", including a 14B model "which can run on personal computers".
- Bears on: the self-replication pathway, P4 (small footprints).

### kinniment2023ara
- Title: Evaluating Language-Model Agents on Realistic Autonomous Tasks
- Authors: Megan Kinniment, Lucas Jun Koba Sato, Haoxing Du, et al. (METR, then ARC Evals),
  2023-12-18 (v2 2024-01-04). arXiv 2312.11671.
- What it says (abstract): 4 agents on 12 autonomous replication and adaptation tasks completed
  only the easiest. Evaluations cannot rule out ARA after about a "100x effective compute scaleup"
  without intermediate evaluations during pretraining.
- Bears on: the self-replication pathway (a 2023 baseline for the AISI trend), protocol (evaluate
  at declared checkpoints).

### scher2025agreement
- Title: An International Agreement to Prevent the Premature Creation of Artificial
  Superintelligence
- Authors: Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance
  Team), 2025-11-17 (v2). arXiv 2511.10783. Read via the PDF.
- What it says:
  - PDF p. 33: "the 'breakout time' - the time it takes between when a group starts trying to
    create a superintelligence and the point at which they succeed". Destroying chips would
    lengthen it "in lieu of algorithmic advancements".
  - PDF p. 10: "the existence of AI chips makes breakout time too short".
  - PDF p. 8: algorithmic progress cuts training operations "by 3x each year", so monitored cluster
    thresholds must fall 3x a year.
- Bears on: D3 (the AI breakout-time concept is in use qualitatively), P4, O3. It belongs mainly
  to the protocol track; recorded here for D3 prior art.

### epoch2026models
- Title: Data on AI Models
- Author: Epoch AI. Page updated 2026-11-24. URL https://epoch.ai/data/ai-models
- What it says:
  - Licence: CC BY 4.0, "free to use, distribute, and reproduce provided the source and authors
    are credited."
  - CSVs: https://epoch.ai/data/all_ai_models.csv, plus notable, large-scale and frontier subsets.
  - Fields include training compute (FLOP), publication date, parameters, dataset size, cost and
    power draw.
- Bears on: D3 (the effective-compute series), the loop-gain calibration (cunningham2026rsi
  estimates epsilon_C,A from this kind of data), P1.

## Numbers for the ledger

Kinds: measured | vendor | spec | design | assumption.

### Research productivity and returns to research

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| bloom-moore-researcher-multiple | 18 | x, early 1970s to 2014 | measured | bloom2020ideas | Introduction, p. 1105 |
| bloom-rp-growth-aggregate | -5.1 | % per year, 1930-2015 | measured | bloom2020ideas | Table 7, p. 1134 |
| bloom-rp-halflife-aggregate | 14 | years | measured | bloom2020ideas | Table 7 |
| bloom-rp-growth-aggregate-text | -5.3 | % per year | measured | bloom2020ideas | p. 1134 text |
| bloom-rp-growth-moore | -6.8 | % per year, 1971-2014 | measured | bloom2020ideas | Table 7 |
| bloom-beta-aggregate | 3.1 | dimensionless | measured | bloom2020ideas | Table 7 |
| bloom-beta-moore | 0.2 | dimensionless | measured | bloom2020ideas | Table 7; p. 1135, 7/35 |
| bloom-rp-growth-compustat-sales | -11.1 | % per year | measured | bloom2020ideas | Table 7 |
| bloom-rp-growth-census | -7.8 | % per year | measured | bloom2020ideas | Table 7 |
| bloom-rp-growth-crop-range | -9.9 to +1.3 | % per year | measured | bloom2020ideas | Table 7, crop rows |

Derived from the Bloom rows, for the model to compute: r = 1/beta when lambda = 1, about 0.32 for
the aggregate economy and about 5 for Moore's Law.

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| epoch-r-chess | 0.83 (SE 0.15) | doublings per doubling | measured | besiroglu2024returns | Computer chess |
| epoch-r-us-economy-replication | 0.25 | doublings per doubling | measured | besiroglu2024returns | aggregate US |
| r-computer-vision | 1.262 (90% CI 0.727 to 2.094) | doublings per doubling | measured | ho2025experiments | Appendix B |
| r-reinforcement-learning | 1.201 (90% CI 0.380 to 2.708) | doublings per doubling | measured | ho2025experiments | Appendix B |
| r-language-models | 1.892 (90% CI 1.069 to 3.212) | doublings per doubling | measured | ho2025experiments | Appendix B |
| r-compute-bottleneck-divisor | 3 (epsilon_K about 2/3) | divisor | assumption | ho2025experiments | Appendix D |
| r-computer-vision-eth | 1.4 (5th-95th 0.8 to 2.4) | doublings per doubling | measured | eth2025sie | citing Epoch |
| r-sat-solvers | 3.5 | doublings per doubling | measured | eth2025sie | citing Epoch |
| r-linear-programming | 1.1 | doublings per doubling | measured | eth2025sie | citing Epoch |
| r-hardware-historical | about 7 | doublings per doubling | measured | eth2025sie | hardware section |
| r-gpu-2006-2022 | about 5 | doublings per doubling | measured | eth2025sie | hardware section |
| r-software-best-guess | 1 to 4 | doublings per doubling | assumption | eth2025sie | overall estimate |
| r-software-const-hardware | 0.5 to 2 | doublings per doubling | assumption | eth2025sie | constant hardware |

### Takeoff and intelligence-explosion models

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| sie-initial-speedup | 8 (2 to 32) | x software progress rate | assumption | davidson2025sie | Parameter values |
| sie-r-cog | 1.2 (0.4 to 3.6) | doublings per doubling | assumption | davidson2025sie | Parameter values |
| sie-distance-to-limits | 11 (6 to 16) | orders of magnitude | assumption | davidson2025sie | Parameter values |
| sie-lambda-parallel | 0.6 | dimensionless | assumption | davidson2025sie | Diminishing returns to parallel labour |
| sie-p-compress-3yr | 0.57 | probability | assumption | davidson2025sie | Results table |
| sie-p-compress-10yr | 0.18 | probability | assumption | davidson2025sie | Results table |
| ie-software-headroom | about 12 | orders of magnitude | assumption | davidson2025three | physical limits section |
| ie-chiptech-headroom-landauer | about 6 | orders of magnitude | assumption | davidson2025three | physical limits section |
| ie-chipprod-headroom-earth | about 5 | orders of magnitude | assumption | davidson2025three | physical limits section |
| ie-p-chiptech-loop-accelerates | about 0.65 | probability | assumption | davidson2025three | Will AI progress accelerate |
| ie-p-chipprod-loop-accelerates | about 0.80 | probability | assumption | davidson2025three | Will AI progress accelerate |
| takeoff-p-under-1yr | 0.25 | probability, 20% to 100% automation | assumption | davidson2023compute | summary |
| takeoff-p-under-3yr | 0.50 | probability | assumption | davidson2023compute | summary |
| takeoff-p-under-10yr | 0.80 | probability | assumption | davidson2023compute | summary |
| effective-flop-gap | 10,000 | x effective compute, 20% to 100% | assumption | davidson2023compute | summary |
| agi-training-req-2020-algos | 1e36 | FLOP | assumption | davidson2023compute | summary |
| ai2027-multiplier-sc | 5 | x AI R&D progress | assumption | kokotajlo2025takeoff | multipliers |
| ai2027-multiplier-sar | 25 | x | assumption | kokotajlo2025takeoff | multipliers |
| ai2027-multiplier-siar | 250 | x | assumption | kokotajlo2025takeoff | multipliers |
| ai2027-multiplier-asi | 2,000 | x | assumption | kokotajlo2025takeoff | multipliers |
| ai2027-sc-to-sar-simulated | 0.3 (90th pct 0.95) | years | assumption | kokotajlo2025takeoff | simulated calendar time |
| nber-singularity-years | about 6 | years, full software plus 5% other | assumption | davidson2026feedback | abstract |

### Loop-gain calibration

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| rsi-threshold-eps-rc | 0.15 | fraction more research effort per ECI point | assumption | cunningham2026rsi | Section 4.1, p. 29 |
| rsi-estimate-eps-rc | about 0.09 | fraction per ECI point | assumption | cunningham2026rsi | Section 4.1, p. 29 |
| rsi-eps-ca | about 6.5 | elasticity of exp(ECI) to compute | measured | cunningham2026rsi | Section 4.1 |
| algorithmic-efficiency-growth | 3 | x per year | measured | cunningham2026rsi (citing Ho et al. 2024) | Section 4.1 |
| sigma-compute-labour-baseline | 2.583 (SE 0.341) | elasticity of substitution | measured | whitfill2025bottlenecks | Table 1 |
| sigma-compute-labour-frontier | -0.103 (SE 0.176) | elasticity of substitution | measured | whitfill2025bottlenecks | Table 1 |
| algo-halving-time | 8 (95% CI 5 to 14) | months | measured | ho2024algorithmic | abstract |
| r-ai-delay | 0.5 | years | assumption | burtsev2026criticality | Section 3.2 |
| network-rho-example | about 1.15 | spectral radius, scenario | assumption | burtsev2026criticality | Section 4 scenarios |

### Task time horizons

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| horizon-doubling-2019-2025 | 207 (95% CI 166 to 240) | days | measured | kwa2025horizon | Section 3.2 |
| horizon-doubling-th10-full | 195.8 (162 to 223) | days | measured | metr2026th11 | table |
| horizon-doubling-th11-2023on | 130.8 (107 to 161) | days | measured | metr2026th11 | table |
| horizon-doubling-th11-2024on | 88.6 | days | measured | metr2026th11 | table |
| horizon-doubling-data-2023on | 128.744 (104.428 to 158.012) | days | measured | metr2026thdata | benchmark_results_1_1.yaml |
| horizon-doubling-data-stitched | 187.778 | days | measured | metr2026thdata | benchmark_results_1_1.yaml |
| horizon-p50-sota-latest | 1,044.8 (508.9 to 3,304.3) | minutes, Claude Mythos Preview early, 2026-04-07 | measured | metr2026thdata | benchmark_results_1_1.yaml |
| horizon-p80-sota-latest | 185.9 (97.3 to 398.5) | minutes | measured | metr2026thdata | benchmark_results_1_1.yaml |
| horizon-long-tasks-baselined | 5 of 31 | tasks over 8 h with human times | measured | metr2026th11 | caveats |
| ord-t80-over-t50 | 1/3 | ratio, constant-hazard model | assumption | ord2025halflife | Section on thresholds |
| ord-t99-over-t50 | 1/70 | ratio | assumption | ord2025halflife | Section on thresholds |
| horizon-delay-compute-slowdown | 7 | years, 1-month 80% horizon | assumption | whitfill2025horizon | abstract |
| cyber-task-length-doubling | about 8 | months (upper bound) | measured | aisi2025trends | Section 2 |

### Automated AI research

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| rebench-agent-vs-human-2h | 4 | x human score at 2 h budget | measured | wijk2024rebench | abstract |
| rebench-human-vs-agent-32h | 2 | x top agent at 32 h | measured | wijk2024rebench | abstract |
| mlebench-bronze-rate | 16.9 | % of 75 competitions | measured | chan2024mlebench | abstract |
| paperbench-best-score | 21.0 | % replication score | measured | starace2025paperbench | abstract |
| alphaevolve-fleet-recovered | 0.7 | % of fleet compute | vendor | novikov2025alphaevolve | Section 3.3.1 |
| alphaevolve-kernel-speedup | 23 | % average kernel speedup | vendor | novikov2025alphaevolve | Section 3.3.2 |
| alphaevolve-gemini-training-cut | 1 | % of training time | vendor | novikov2025alphaevolve | Section 3.3.2 |
| nanogpt-records | 77 | records, May 2024 to Mar 2026 | measured | shetty2026nanogpt | key numbers |
| nanogpt-speedup | 31 (45 to 1.43 min) | x training time | measured | shetty2026nanogpt | key numbers |
| nanogpt-ai-records | 4 | records (about 5%) | measured | shetty2026nanogpt | key numbers |
| human-cost-per-1pct | 2,500 | USD per 1% speedup | assumption | metr2026expenditure | human labour cost |
| agent-expenditure-horizon | 0 to 3,300 | USD | measured | metr2026expenditure | results |
| rct-2025-time-change | +19 (CI +2 to +39) | % task time with AI | measured | becker2025rct, metr2026uplift | abstract; update |
| rct-2026-returning-time-change | -18 (CI -38 to +9) | % task time | measured | metr2026uplift | results paragraph |
| rct-2026-new-time-change | -4 (CI -15 to +9) | % task time | measured | metr2026uplift | results paragraph |
| anthropic-ai-led-share | 26 | % of AI R&D work at AL4 | vendor | anthropic2026pace | Automation Index |
| anthropic-agents-concurrent | about 30,000 | agents | vendor | anthropic2026pace | Agent oversight |

### Lab triggers

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| openai-critical-speedup | 5 | x (generation in 1/5 of 2024 time, sustained several months) | spec | openai2025preparedness | Table 1 |
| anthropic-rd-rate-multiple | 2 | x rate of aggregate capability progress, over 3 or more generations | spec | anthropic2026rsp | AI R&D threshold; footnotes 8, 9 |
| anthropic-substitution-cost-factor | 5 | x cost of researchers | spec | anthropic2026rsp | AI R&D threshold |
| eth-davidson-threshold | 5 | x recent pace of software progress | design | eth2025sie | mitigations |

### Self-replication and continual learning

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| replibench-families | 20 families, 86 tasks | count | spec | black2025replibench | abstract |
| replibench-best-families-50pct | 15 of 20 | families above 50% pass@10 | measured | black2025replibench | abstract |
| aisi-replication-2023 | under 5 | % success, 11 of 20 evaluations | measured | aisi2025trends | Section 5 |
| aisi-replication-2025 | over 60 | % success | measured | aisi2025trends | Section 5 |
| fudan-selfrep-llama70b | 50 | % of trials | measured | pan2024selfrep | abstract |
| fudan-selfrep-qwen72b | 90 | % of trials | measured | pan2024selfrep | abstract |
| fudan-systems-capable | 11 of 32 | systems | measured | pan2025selfrep | abstract |
| seal-squad-accuracy | 47.0 (vs 33.5 passage-only) | % | measured | zweiger2025seal | Section 4.2 |
| seal-arc-success | 72.5 (vs 20, 0) | % | measured | zweiger2025seal | Section 4.1 |
| seal-edit-eval-time | 30 to 45 | seconds | measured | zweiger2025seal | Section 5 |
| cp1-k | 1.0006 (0.9946 prompt) | neutron multiplication factor | measured | yudkowsky2013iem | Section 1, PDF p. 6 |

## Prior art for the memo's candidates

### Searches tried

- Web: "Will AI R&D automation cause a software intelligence explosion" Eth Davidson.
- Web: Davidson Houlden "How quick and big would a software intelligence explosion be".
- Web: Epoch AI returns to software R&D "r" estimate singularity Erdil Besiroglu.
- Web: Davidson "compute-centric framework" takeoff speeds.
- Web: "Measuring AI R&D automation" arXiv metrics.
- Web: "loop gain" recursive self-improvement AI measurement threshold.
- Web: AI agent improves training recipe fixed compute successive rounds, "nanoGPT speedrun"
  automated.
- Web: "breakout time" AI superintelligence verification compute arms control.
- Web: AI 2027 takeoff forecast; the titotal critique; critiques of Bloom et al.
- Web: Anthropic RSP AI R&D threshold; OpenAI Preparedness "AI Self-improvement".
- Web: AISI self-replication trends; 2026 continual learning.
- Followed the reference lists of cunningham2026rsi and burtsev2026criticality.

### D2, loop gain: extends prior work, and less than the memo believed

- Closest work:
  - cunningham2026rsi names "the loop gain", derives the threshold (> 1), says tracking it and
    extrapolating its crossing is the key empirical exercise, and gives a point calibration
    (about 0.09 against 0.15).
  - burtsev2026criticality defines R_AI = chi a / sigma, with the same damped/amplified
    threshold, and lists the quantities to estimate per development cycle.
  - yudkowsky2013iem frames it as k, criticality and delayed neutrons.
  - eth2025sie and davidson2025sie use r with fixed compute, propose measuring software progress
    and a 5x-pace threshold.
  - openai2025preparedness and anthropic2026rsp set rate-of-progress triggers (5x, 2x).
  - ho2025experiments calls for controlled experiments on returns.
  - metr2026expenditure measures agent returns to spend on an AI R&D target.
- Not found in my search: an estimator that is (i) run in a staged experiment at fixed compute,
  (ii) reported with a confidence bound, and (iii) used as a binding trigger at the lower bound.
  This is a claim about my search, not about the literature.
- Two design consequences:
  - **Units.** The ratio of successive gains equals the compounding condition only on a
    log compute-equivalent axis with rounds of equal resource budget. On a bounded benchmark,
    successive gains shrink near the ceiling regardless of feedback. cunningham2026rsi notes that
    the product of elasticities is invariant to normalisation, while a raw ratio of gains is not.
  - **Baseline progress.** burtsev2026criticality shows fast progress can be subcritical and early
    supercritical progress can look ordinary. A trigger built on capability slope (as in the
    OpenAI and Anthropic rate triggers) does not identify the regime.
- Revised label: extends prior work. The condition, the name and the measurement agenda are prior.
  A confidence-bounded, rerunnable trigger may be new.

### D3, breakout time: extends prior work

- scher2025agreement uses "breakout time" for AI qualitatively: from starting to try to building
  ASI to succeeding.
- davidson2025sie and kokotajlo2025takeoff compute fixed-compute takeoff durations from assumed
  parameters.
- whitfill2025horizon links horizon growth to compute growth.
- Not found: a breakout time computed from a party's verified holdings and a measured loop gain,
  with an interval. Judgement: extends.

### Y2, runaway versus saturation: prior work

- The condition r = lambda/beta > 1 under full automation with constant compute is in
  besiroglu2024returns and eth2025sie (from Jones 1995, via bloom2020ideas).
- The saturation mechanisms are documented in prior work:
  - Compute complementarity: whitfill2025bottlenecks, ho2025experiments.
  - Parallelisation limits: trammell2026parallel.
  - Baumol bottlenecks: aghion2017ai.
  - Finite runway: davidson2025sie, burtsev2026criticality.
- What the project can add is measurement, not the condition.

### Y3, coupling: prior work

- davidson2026feedback gives the exact claim with proof. With two loops each with diminishing
  returns, explosion occurs if and only if beta_S beta_H < phi_S phi_H. In general the condition
  is a spectral radius above 1.
- cunningham2026rsi writes it as a sum of loop channels above 1, with each channel below 1.
- burtsev2026criticality proves it across actors: individually subcritical labs or blocs can be
  collectively supercritical through transfer.
- davidson2025three states it qualitatively for software, chip technology and chip production.
- The memo's belief must change. Y3 is prior work, and the project should cite it as such.
- What may remain new: making "hold the spectral radius below 1" an enforceable treaty bound.
  That means naming which edges the protocol cuts: compute licences on the economic loop, KYC on
  the acquisitive loop, and limits on cross-party transfer of AI R&D advances on the
  burtsev2026criticality network edge. It also means verifying each edge separately. Not found
  in my search.

### D6, closure: extends prior work

- burtsev2026criticality defines operational closure chi as the fraction of potential recursive
  gain that survives the pipeline.
- chen2026rsisurvey classifies loops "by how closed the loop is", from human-in-the-loop to fully
  closed.
- The memo's D6 differs. It is per input (compute, weights, data, labour, money) and asks whether
  a verifiable human-held gate sits on each. Pipeline transmission alone does not ask that.
- Judgement: extends. D6 could be stated as a decomposition of Burtsev's chi into gated inputs.

### The criticality metaphor and the name

- yudkowsky2013iem uses the neutron multiplication factor k, "prompt critical" and "delayed
  neutrons" for intelligence explosion.
- burtsev2026criticality uses a reproduction number.
- The nuclear-safeguards analogy for the protocol (timeliness shorter than conversion time) was
  not found in this track's sources. Other tracks may find it.

### Pathway ranking, evidence from this track

- **Recursive self-improvement (rank 1): supported as the closest loop to closing.**
  - The research-labour input is being automated quickly: 26% AI-led at one lab, and 100-fold
    growth in coding-inference research compute reported by another (via cunningham2026rsi).
  - Measured contributions to frontier-relevant progress are still shallow: 4 of 77 NanoGPT
    records, expenditure horizons of $0 to $3.3K, PaperBench 21%, and humans ahead of agents
    beyond 8 to 32 hours on RE-Bench.
  - The one calibration found puts the loop gain below 1, but rising.
- **Scaling (rank 2): strengthened as the backbone.**
  - Frontier-experiment compute is a complement to research labour (sigma about -0.10).
  - Horizon growth tracks compute growth.
  - The compute-bottleneck correction pushes r below 1.
- **Self-replication (rank 3): components rising fast (5% to 60%).** The failures sit at KYC and
  persistence, which are cheap human-held gates. This fits "cheap to forbid", if compute KYC is
  enforced.
- **Continual learning (rank 4): supported.** Self-editing works (SEAL) but forgets, and the 2026
  evidence says the hazard is mechanism-specific. Accounting and re-evaluation fit better than a
  ban.
- **Autonomy (rank 5): the horizon trend has sped up** (about 130-day doubling since 2023, with a
  17-hour 50% horizon at the frontier). But 80% horizons lag 50% horizons by 5 to 10x in the latest
  data. That lag is what matters for unattended breakout.

## Public datasets for experiments

- **METR time horizons (TH1.1).** Model-level https://metr.org/assets/benchmark_results_1_1.yaml
  and task-level https://metr.org/assets/task_results_1_1.yaml. Licence CC BY 4.0, as stated on
  https://metr.org/time-horizons/. Analysis pipeline: https://github.com/METR/eval-analysis-public
  (the GitHub API shows no licence file). Use: refit the doubling time with a bootstrap, the p80
  trend, and the p50/p80 ratio.
- **NanoGPT speedrun record history.** https://github.com/KellerJordan/modded-nanogpt (MIT, per
  the GitHub API; contents not opened here). METR's provenance coding is in shetty2026nanogpt.
  Use: D2 test (a), per-record software gains at fixed hardware, and a loop-gain series with
  intervals.
- **Bloom et al. replication package.** https://doi.org/10.3886/E111743V2 (openICPSR). The landing
  page returned 403, so I could not confirm its licence. Use: re-estimate beta and r per domain
  with intervals, and the Alston and Pardey lag critique.
- **Epoch AI models dataset.** https://epoch.ai/data/ai-models, CSV at
  https://epoch.ai/data/all_ai_models.csv (updated 2026-11-24). Licence CC BY 4.0. Use: training
  compute series for effective compute in D3, and the ECI-on-compute slope behind epsilon_C,A.
- **RE-Bench.** Environments, human data and trajectories at https://github.com/METR/RE-Bench
  (licence "Other" per the GitHub API; check before use). Use: agent against human returns to time
  budget.
- **MLE-bench.** https://github.com/openai/mle-bench (no SPDX licence asserted per the GitHub API;
  check before use).

## Sources (TOML)

```toml
[source.bloom2020ideas]
type = "peer-reviewed"
title = "Are Ideas Getting Harder to Find?"
authors = "Nicholas Bloom, Charles I. Jones, John Van Reenen, Michael Webb"
year = 2020
doi = "10.1257/aer.20180338"
opened = "2026-11-27"

[source.alston2022ideas]
type = "report"
title = "Are Ideas Really Getting Harder to Find?"
authors = "Julian M. Alston, Philip G. Pardey"
year = 2022
doi = "10.22004/ag.econ.320517"
opened = "2026-11-27"

[source.besiroglu2024returns]
type = "report"
title = "Do the Returns to Software R&D Point Towards a Singularity?"
authors = "Tamay Besiroglu, Ege Erdil, Anson Ho"
year = 2024
url = "https://epoch.ai/blog/do-the-returns-to-software-rnd-point-towards-a-singularity"
opened = "2026-11-27"

[source.erdil2024idea]
type = "preprint"
title = "Estimating Idea Production: A Methodological Survey"
authors = "Ege Erdil, Tamay Besiroglu, Anson Ho"
year = 2024
arxiv = "2405.10494"
opened = "2026-11-27"

[source.ho2025experiments]
type = "essay"
title = "The software intelligence explosion debate needs experiments"
authors = "Anson Ho, Parker Whitfill"
year = 2025
url = "https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments"
opened = "2026-11-27"

[source.eth2025sie]
type = "report"
title = "Will AI R&D Automation Cause a Software Intelligence Explosion?"
authors = "Daniel Eth, Tom Davidson"
year = 2025
url = "https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion"
opened = "2026-11-27"

[source.davidson2025sie]
type = "report"
title = "How quick and big would a software intelligence explosion be?"
authors = "Tom Davidson, Tom Houlden"
year = 2025
url = "https://www.forethought.org/research/how-quick-and-big-would-a-software-intelligence-explosion-be"
opened = "2026-11-27"

[source.davidson2025three]
type = "report"
title = "Three Types of Intelligence Explosion"
authors = "Tom Davidson, Rose Hadshar, William MacAskill"
year = 2025
url = "https://www.forethought.org/research/three-types-of-intelligence-explosion"
opened = "2026-11-27"

[source.davidson2026feedback]
type = "report"
title = "When Does Automating AI Research Produce Explosive Growth? Feedback Loops in Innovation Networks"
authors = "Tom Davidson, Basil Halperin, Thomas Houlden, Anton Korinek"
year = 2026
doi = "10.3386/w35155"
opened = "2026-11-27"

[source.cunningham2026rsi]
type = "preprint"
title = "The Economics of Recursive Self-Improvement"
authors = "Tom Cunningham, Lukas Althoff, Basil Halperin, Brian Jabarian, Andrew Koh, Arjun Ramani, Phil Trammell, Parker Whitfill, Cheryl Wu"
year = 2026
arxiv = "2609.15802"
opened = "2026-11-27"

[source.burtsev2026criticality]
type = "preprint"
title = "Recursive Criticality of AI Self-Improvement"
authors = "Mikhail Burtsev"
year = 2026
arxiv = "2609.00137"
opened = "2026-11-27"

[source.chan2026explosion]
type = "preprint"
title = "What if automating AI R&D triggers an intelligence explosion?"
authors = "Alan Chan, Christoph Winter, Andrew Barto, Jakub Pachocki, Geoffrey Hinton, Eric Horvitz, Yoshua Bengio, Dawn Song, Jack Clark, Hilary Greaves, Anton Korinek, Samuel Hammond, Thore Graepel, Ben Bariach, Philip H. S. Torr, Sheila A. McIlraith, Jeff Clune, Sam Manning, Girish Sastry, Tom Davidson, Daniel Eth, Soren Mindermann"
year = 2026
arxiv = "2609.36054"
opened = "2026-11-27"

[source.chan2026measuring]
type = "preprint"
title = "Measuring AI R&D Automation"
authors = "Alan Chan, Ranay Padarath, Joe Kwon, Hilary Greaves, Markus Anderljung"
year = 2026
arxiv = "2603.03992"
opened = "2026-11-27"

[source.anthropic2026pace]
type = "vendor"
title = "Measurements for understanding the pace of AI development inside frontier labs"
authors = "Anthropic (Marina Favaro, Phillie Wright)"
year = 2026
url = "https://www.anthropic.com/institute/measuring-pace-of-ai-development"
opened = "2026-11-27"

[source.whitfill2025bottlenecks]
type = "preprint"
title = "Will Compute Bottlenecks Prevent an Intelligence Explosion?"
authors = "Parker Whitfill, Cheryl Wu"
year = 2025
arxiv = "2507.23181"
opened = "2026-11-27"

[source.trammell2026parallel]
type = "report"
title = "Even after R&D is automated, parallelization constraints could delay a technological singularity"
authors = "Phil Trammell"
year = 2026
url = "https://epoch.ai/publications/parallelization-constraints-could-delay-a-technological-singularity"
opened = "2026-11-27"

[source.davidson2023compute]
type = "essay"
title = "What a compute-centric framework says about AI takeoff speeds"
authors = "Tom Davidson"
year = 2023
url = "https://www.lesswrong.com/posts/Gc9FGtdXhK9sCSEYu/what-a-compute-centric-framework-says-about-ai-takeoff"
opened = "2026-11-27"

[source.kokotajlo2025takeoff]
type = "report"
title = "Takeoff Forecast"
authors = "Daniel Kokotajlo, Eli Lifland"
year = 2025
url = "https://ai-2027.com/research/takeoff-forecast"
opened = "2026-11-27"

[source.titotal2025critique]
type = "essay"
title = "A deep critique of AI 2027's bad timeline models"
authors = "titotal"
year = 2025
url = "https://titotal.substack.com/p/a-deep-critique-of-ai-2027s-bad-timeline"
opened = "2026-11-27"

[source.yudkowsky2013iem]
type = "report"
title = "Intelligence Explosion Microeconomics"
authors = "Eliezer Yudkowsky"
year = 2013
url = "https://intelligence.org/files/IEM.pdf"
opened = "2026-11-27"

[source.good1965speculations]
type = "peer-reviewed"
title = "Speculations Concerning the First Ultraintelligent Machine"
authors = "Irving John Good"
year = 1965
doi = "10.1016/S0065-2458(08)60418-0"
opened = "2026-11-27"

[source.aghion2017ai]
type = "report"
title = "Artificial Intelligence and Economic Growth"
authors = "Philippe Aghion, Benjamin F. Jones, Charles I. Jones"
year = 2017
doi = "10.3386/w23928"
opened = "2026-11-27"

[source.trammell2023growth]
type = "report"
title = "Economic Growth under Transformative AI"
authors = "Philip Trammell, Anton Korinek"
year = 2023
doi = "10.3386/w31815"
opened = "2026-11-27"

[source.erdil2023explosive]
type = "preprint"
title = "Explosive growth from AI automation: A review of the arguments"
authors = "Ege Erdil, Tamay Besiroglu"
year = 2023
arxiv = "2309.11690"
opened = "2026-11-27"

[source.kwa2025horizon]
type = "peer-reviewed"
title = "Measuring AI Ability to Complete Long Software Tasks"
authors = "Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment, Nate Rush, Sydney Von Arx, et al."
year = 2025
arxiv = "2503.14499"
opened = "2026-11-27"

[source.metr2026th11]
type = "report"
title = "Time Horizon 1.1"
authors = "METR"
year = 2026
url = "https://metr.org/blog/2026-01-29-time-horizon-1-1/"
opened = "2026-11-27"

[source.metr2026thdata]
type = "dataset"
title = "Task-Completion Time Horizons of Frontier AI Models (METR-Horizon-v1.1 results)"
authors = "METR"
year = 2026
url = "https://metr.org/assets/benchmark_results_1_1.yaml"
opened = "2026-11-27"

[source.ord2025halflife]
type = "preprint"
title = "Is there a half-life for the success rates of AI agents?"
authors = "Toby Ord"
year = 2025
arxiv = "2505.05115"
opened = "2026-11-27"

[source.whitfill2025horizon]
type = "preprint"
title = "Forecasting AI Time Horizon Under Compute Slowdowns"
authors = "Parker Whitfill, Ben Snodin, Joel Becker"
year = 2025
arxiv = "2511.19492"
opened = "2026-11-27"

[source.ho2024algorithmic]
type = "preprint"
title = "Algorithmic progress in language models"
authors = "Anson Ho, Tamay Besiroglu, Ege Erdil, David Owen, Robi Rahman, Zifan Carl Guo, David Atkinson, Neil Thompson, Jaime Sevilla"
year = 2024
arxiv = "2403.05812"
opened = "2026-11-27"

[source.wijk2024rebench]
type = "preprint"
title = "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts"
authors = "Hjalmar Wijk, Tao Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Josh Clymer, Jai Dhyani, et al."
year = 2024
arxiv = "2411.15114"
opened = "2026-11-27"

[source.chan2024mlebench]
type = "preprint"
title = "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering"
authors = "Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Madry"
year = 2024
arxiv = "2410.07095"
opened = "2026-11-27"

[source.starace2025paperbench]
type = "preprint"
title = "PaperBench: Evaluating AI's Ability to Replicate AI Research"
authors = "Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan"
year = 2025
arxiv = "2504.01848"
opened = "2026-11-27"

[source.novikov2025alphaevolve]
type = "preprint"
title = "AlphaEvolve: A coding agent for scientific and algorithmic discovery"
authors = "Alexander Novikov, Ngan Vu, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, et al."
year = 2025
arxiv = "2506.13131"
opened = "2026-11-27"

[source.lu2024aiscientist]
type = "preprint"
title = "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery"
authors = "Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha"
year = 2024
arxiv = "2408.06292"
opened = "2026-11-27"

[source.yamada2025aiscientist2]
type = "preprint"
title = "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search"
authors = "Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha"
year = 2025
arxiv = "2504.08066"
opened = "2026-11-27"

[source.trehan2026scientists]
type = "preprint"
title = "Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts"
authors = "Dhruv Trehan, Paras Chopra"
year = 2026
arxiv = "2601.03315"
opened = "2026-11-27"

[source.zhao2025speedrun]
type = "preprint"
title = "The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements"
authors = "Bingchen Zhao, et al."
year = 2025
arxiv = "2506.22419"
opened = "2026-11-27"

[source.shetty2026nanogpt]
type = "report"
title = "Evidence on AI R&D Progress from NanoGPT"
authors = "Manish Shetty (METR)"
year = 2026
url = "https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/"
opened = "2026-11-27"

[source.metr2026expenditure]
type = "report"
title = "Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT"
authors = "Tom Cunningham, Manish Shetty, Vincent Cheng, Nate Rush (METR)"
year = 2026
url = "https://metr.org/blog/2026-07-21-expenditure-horizon/"
opened = "2026-11-27"

[source.becker2025rct]
type = "preprint"
title = "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
authors = "Joel Becker, Nate Rush, Elizabeth Barnes, David Rein"
year = 2025
arxiv = "2507.09089"
opened = "2026-11-27"

[source.metr2026uplift]
type = "report"
title = "We are Changing our Developer Productivity Experiment Design"
authors = "METR"
year = 2026
url = "https://metr.org/blog/2026-02-24-uplift-update/"
opened = "2026-11-27"

[source.openai2025preparedness]
type = "vendor"
title = "Preparedness Framework, Version 2"
authors = "OpenAI"
year = 2025
url = "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
opened = "2026-11-27"

[source.anthropic2026rsp]
type = "vendor"
title = "Responsible Scaling Policy, Version 3.4"
authors = "Anthropic"
year = 2026
url = "https://www.anthropic.com/responsible-scaling-policy"
opened = "2026-11-27"

[source.zweiger2025seal]
type = "preprint"
title = "Self-Adapting Language Models"
authors = "Adam Zweiger, Jyothish Pari, Han Guo, Ekin Akyurek, Yoon Kim, Pulkit Agrawal"
year = 2025
arxiv = "2506.10943"
opened = "2026-11-27"

[source.akyurek2024ttt]
type = "preprint"
title = "The Surprising Effectiveness of Test-Time Training for Few-Shot Learning"
authors = "Ekin Akyurek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han Guo, Jyothish Pari, Yoon Kim, Jacob Andreas"
year = 2024
arxiv = "2411.07279"
opened = "2026-11-27"

[source.luo2023forgetting]
type = "preprint"
title = "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning"
authors = "Yun Luo, Zhen Yang, Fandong Meng, Yafu Li, Jie Zhou, Yue Zhang"
year = 2023
arxiv = "2308.08747"
opened = "2026-11-27"

[source.harrington2026continual]
type = "preprint"
title = "When Does Continual Learning Require Learning"
authors = "Anne Harrington, Nayan Saxena, Michael Murphy, Anastasia Borovykh, Zeyu Yun, Sridhar Kamath, Ara Eindra Kyi, Trevor Darrell, Jitendra Malik, Yutong Bai"
year = 2026
arxiv = "2607.07847"
opened = "2026-11-27"

[source.chen2026rsisurvey]
type = "preprint"
title = "Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops"
authors = "Mingguang Chen, Licheng Wang, Bo Qu"
year = 2026
arxiv = "2607.07663"
opened = "2026-11-27"

[source.black2025replibench]
type = "preprint"
title = "RepliBench: Evaluating the Autonomous Replication Capabilities of Language Model Agents"
authors = "Sid Black, Asa Cooper Stickland, Jake Pencharz, Oliver Sourbut, Michael Schmatz, Jay Bailey, Ollie Matthews, Ben Millwood, Alex Remedios, Alan Cooney"
year = 2025
arxiv = "2504.18565"
opened = "2026-11-27"

[source.aisi2025trends]
type = "report"
title = "Frontier AI Trends Report"
authors = "UK AI Security Institute"
year = 2025
url = "https://www.aisi.gov.uk/frontier-ai-trends-report"
opened = "2026-11-27"

[source.pan2024selfrep]
type = "preprint"
title = "Frontier AI systems have surpassed the self-replicating red line"
authors = "Xudong Pan, Jiarun Dai, Yihe Fan, Min Yang"
year = 2024
arxiv = "2412.12140"
opened = "2026-11-27"

[source.pan2025selfrep]
type = "preprint"
title = "Large language model-powered AI systems achieve self-replication with no human intervention"
authors = "Xudong Pan, Jiarun Dai, Yihe Fan, Minyuan Luo, Changyi Li, Min Yang"
year = 2025
arxiv = "2503.17378"
opened = "2026-11-27"

[source.kinniment2023ara]
type = "preprint"
title = "Evaluating Language-Model Agents on Realistic Autonomous Tasks"
authors = "Megan Kinniment, Lucas Jun Koba Sato, Haoxing Du, Brian Goodrich, Max Hasin, Lawrence Chan, Luke Harold Miles, Tao R. Lin, Hjalmar Wijk, Joel Burget, Aaron Ho, Elizabeth Barnes, Paul Christiano"
year = 2023
arxiv = "2312.11671"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.epoch2026models]
type = "dataset"
title = "Data on AI Models"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/data/ai-models"
opened = "2026-11-27"
```
