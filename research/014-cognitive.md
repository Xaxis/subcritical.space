# Part I, 4: The cognitive and functional perspective

The other perspectives describe what goes into a superintelligent system: the compute and energy
it consumes, the algorithms that turn compute into capability, the loops that compound it, and the
organisations that supply the inputs. This one describes what comes out. It asks what such a system
can do that humans and human institutions cannot, and how that can be measured rather than
asserted.

That question matters for the line between useful AI and the path to superintelligence because
cognitive superiority, on its own, is not the line. Narrow systems have been superhuman for years
(at poker, Go and protein structure) and are among the most useful AI there is. Individual experts
are already outscored on many tests. If the protocol triggered on "better than a human at
something", it would have triggered long ago and would ban useful AI. The line this chapter helps
draw is narrower: superiority against the best human organisations, not individuals; in the
functions that let a system acquire or improve the inputs to its own successor; across several of
them at once; and inside a closed loop.

The survey changed three things the memo believed (research/00-memo.md, candidates F1 to F3 and
D1).

1. What D1 adds is narrower than the memo said. Comparing AI with organisations rather than
   individuals, counting copies and speed, and tracking where AI and human performance cross are
   prior work. What our search did not find is a definition that matches both time and budget, runs
   on a refreshed held-out battery with institutional baselines, and counts clusters won with an
   alpha fraction.
2. A capability verdict is a function of the time and money each side is given. RE-Bench's agents
   beat human experts at short budgets and lose at long ones. A definition that does not fix the
   budget is not yet a definition.
3. The instruments are the weakest link. Benchmarks with expert baselines saturate within a few
   years, carry error rates of tens of percent, overstate real work, and measure what a system
   shows rather than what it can do. Near the line, where no human demonstrations exist, the
   instruments are weakest of all.

The consequence for the protocol is that the cognitive perspective supplies the definition the
protocol protects (D1) and a lagging check on it, but no trigger. Not even capability at AI
research, measured against an institution at matched budget, can serve as one, though it is the
cluster that ties to the self-improvement loop (D2): it holds only once a system already beats the
institution, so it cannot warn, and the protocol must act on the line before it.

Verification since the survey narrowed this further. The claims file keeps D1 as a definition only
([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).
Its crossover budget t\* is prior work as a quantity [@wijk2024rebench; @robinson2026horizons].
Public data hold no organisation baseline at matched budget for any cluster (E1).

The chapter takes the memo's three mechanisms in turn (F1 kinds of advantage, F2 the decisive
functions, F3 narrow versus general), then adds a fourth section, F4, on measurement itself: how
capability can be measured so that a protocol can trigger on it. It closes with the quantities the
protocol can measure, and says why none of them is a trigger. Bostrom's 2014 book could not be
opened by the survey, so its typology is cited only through a source that summarises it with page
references [@grace2014forms].

## F1. Kinds of advantage: speed, copies and quality

### Definition

The system boundary is a system S (weights, scaffolding and tools) together with the inference
compute R its holder controls or can rent, working on a task family T. It is compared with a named
human comparison H, which may be an individual expert, a team or an organisation, given a
wall-clock budget t and a money budget b. Three quantities are measured separately.

- **Serial speed s(T).** The ratio of H's wall-clock time to one instance of S's wall-clock time to
  reach the same score on the same tasks. It is dimensionless. It is a task rate, not a token rate:
  it includes the retries and dead ends an agent needs. The hardware ceiling on it is memory
  bandwidth per copy, which the physical chapter treats (P3).
- **Copies n.** The number of instances of S that R sustains at once at speed s. It is a count,
  equal to R divided by the inference compute one instance needs at that speed. Copies and speed
  trade against each other on fixed hardware (batching raises n and lowers s), so n and s are
  reported as a pair at a declared operating point.
- **Quality q(T, t, b).** The best score S reaches on T within budgets t and b, relative to the best
  score H reaches with the same budgets. A pure quality advantage is a set of items S solves that H
  does not solve at any budget the comparison allows.

The product n times s is a labour-equivalent capacity. It means something only where quality is at
least matched, and only up to the limits of parallel work discussed below.

### How it is measured

Speed and cost ratios have been measured on several task families. On RE-Bench, the AIDE agent made
[36.8/h](numbers.md#cog-rebench-attempts-agent) scored attempts an hour against
[3.4/h](numbers.md#cog-rebench-attempts-human) for human experts, about
[11](numbers.md#cog-rebench-attempt-ratio) times as many, and an agent run of [8 h](numbers.md#cog-rebench-run-hours) cost about
[123 USD](numbers.md#cog-rebench-agent-cost) against [1,855 USD](numbers.md#cog-rebench-human-cost)
paid to an expert, a factor of [15](numbers.md#cog-rebench-cost-ratio) [@wijk2024rebench]. In a
university-level onsite CTF, the best autonomous agent used about
[20%](numbers.md#cog-ctf-runtime-share) of the human teams' cumulative runtime [@tang2026ctfcollab].
METR found that more than [80%](numbers.md#cog-horizon-cheap-share) of successful agent runs cost
under [10%](numbers.md#cog-horizon-cheap-threshold) of what a human would cost, at an assumed
[143.61 USD/h](numbers.md#cog-horizon-human-rate) [@kwa2025horizon]. On GDPval, GPT-5's naive speed
gain over experts is [90](numbers.md#cog-gdpval-naive-speedup) times and its naive cost gain
[474](numbers.md#cog-gdpval-naive-cost-gain) times; once an expert reviews and fixes the output
("try n times, then fix"), the gains fall to [1.39](numbers.md#cog-gdpval-review-speedup) and
[1.63](numbers.md#cog-gdpval-review-cost-gain), so counting review shrinks the speed gain
[65](numbers.md#cog-gdpval-review-shrink)-fold and the cost gain [290](numbers.md#cog-gdpval-cost-shrink)-fold. The expert
reference is [404 min](numbers.md#cog-gdpval-expert-minutes) and [361 USD](numbers.md#cog-gdpval-expert-cost) per task [@patwardhan2025gdpval].

The human side carries its own error, and it is large. METR's contract baseliners took
[5](numbers.md#cog-baseliner-slowdown-low) to [18](numbers.md#cog-baseliner-slowdown-high) times
longer to resolve issues than the repositories' own maintainers [@kwa2025horizon], so a speed ratio
depends on which human is the reference. Cost ratios inherit the wage chosen: RE-Bench paid about
[232 USD/h](numbers.md#cog-rebench-human-hourly), GDPval's median-wage basis is about
[54 USD/h](numbers.md#cog-gdpval-expert-hourly), a spread of
[4.3](numbers.md#cog-wage-spread) times between two published comparisons, with METR's assumed rate
between them.

Copies have not been measured in any source the survey found. Every figure is an assumption or an
illustration. Karnofsky argues the compute that trains a human-level system could run "several
hundred million copies for about a year each" [@karnofsky2022defeat]. Amodei assumes "millions of
instances" at [10](numbers.md#cog-amodei-speed-low) to [100](numbers.md#cog-amodei-speed-high)
times human speed [@amodei2024grace]. Aschenbrenner writes of perhaps
[100,000,000](numbers.md#cog-aschenbrenner-equivalents) automated researchers
[@aschenbrenner2024sa]. Hendrycks, Schmidt and Wang illustrate an intelligence recursion with an AI
at [100](numbers.md#cog-hendrycks-pace) times a human's pace copied
[10,000](numbers.md#cog-hendrycks-copies) times [@hendrycks2025superintelligence], which is
[1,000,000](numbers.md#cog-hendrycks-labour) researcher-equivalents. AI 2027's superhuman coder runs
[30](numbers.md#cog-sc-copies) agents per human engineer, each at [30](numbers.md#cog-sc-speed) times
human speed, on [5%](numbers.md#cog-sc-compute-share) of the company's compute
[@lifland2025timelines]. That is [900](numbers.md#cog-sc-labour-at-share) engineer-equivalents per
engineer on that share, and [18,000](numbers.md#cog-sc-labour-full) if the relation were linear over
all the company's compute. The derived figures show how large a collective these definitions imply;
they are not measurements.

This chapter proposes measuring copies instead of assuming them: n equals the sustained inference
throughput the holder has (from chip accounting, P1) divided by the throughput one instance needs
at the declared speed (measured by inspectors running the declared serving stack on a reference
workload). The measurement error comes from model size, numerical precision, batching and
distillation, all of which change the per-instance cost. As long as the chips are accounted for, the
holder cannot hide n, but can understate it by declaring a slow operating point, so inspectors
should measure the maximum sustainable n at the speed the system actually used in its evaluations.
Speed can be understated at evaluation too (a slower scaffold, throttled sampling), which is another
reason to measure s on inspector-run hardware rather than accept a demonstration.

Quality is the hard part and is treated with D1 in F4.

### Evidence for and against

The kinds behave differently, which supports measuring them separately. Speed and cost advantages
are largest on short tasks. On HCAST, agents succeed [70%](numbers.md#cog-hcast-short-success-low)
to [80%](numbers.md#cog-hcast-short-success-high) of the time on tasks humans finish in under
[1 h](numbers.md#cog-hcast-short-hours) and less than [20%](numbers.md#cog-hcast-long-success-max) of the time on tasks taking humans
over [4 h](numbers.md#cog-hcast-long-hours) [@rein2025hcast]. On RE-Bench at a [2 h](numbers.md#cog-rebench-budget-short)
budget the best agents scored [4](numbers.md#cog-rebench-ai-over-human-2h) times as high as human
experts; at [32 h](numbers.md#cog-rebench-budget-long), humans scored
[2](numbers.md#cog-rebench-human-over-ai-32h) times the top agent [@wijk2024rebench]. An agent that
makes many more attempts an hour is not correspondingly more capable on long tasks.

The strongest case against the memo comes from Karnofsky: the danger needs no quality superiority at
all ("we still have a problem even if we assume that AIs will basically have similar capabilities
to humans"), because copies alone add up to a workforce [@karnofsky2022defeat]. If that is right, the
quantity that matters in F1 is n times s, and n times s is bought with inference compute. Copies and
speed are then physical quantities, measured by the chip and power channels of the physical
chapter, and quality is the only part of F1 that is cognitive. This chapter accepts that argument:
it moves the weight of F1 from evaluation to compute accounting.

Two findings push the other way, against treating copies as free labour. Experiments on human
groups from 1924 to 2015 found that "Groups outperformed individuals, but larger groups did not
outperform smaller groups" [@aiimpacts2016coordinated]. Trammell argues that effective research is
capped by the scarcer of the raw research inputs and the "parallelization technology" needed to
divide and integrate the work [@trammell2026parallel]; he gives no fitted values. So n times s
overstates capacity by an unknown factor, and the factor is itself a research question.

The measured gains also shrink once real work and oversight are counted. Beyond GDPval's review
effect, METR's randomised trial found that early-2025 tools made experienced open-source developers
[19%](numbers.md#cog-rct-slowdown) slower, though they forecast a
[24%](numbers.md#cog-rct-forecast) speed-up [@becker2025rct]. Its 2026 follow-up estimates a change
of [-18%](numbers.md#cog-rct2026-returning) in task time (faster) for returning developers, but METR
calls the data "only very weak evidence" because developers now decline to work without AI
[@metr2026uplift]. RE-Bench's authors say their benchmark likely overestimates real-world AI R&D
performance and that real R&D is at least [2 orders of magnitude](numbers.md#cog-rebench-real-scale-oom)
larger on several axes [@wijk2024rebench].

Left open: whether a pure quality advantage over organisations exists anywhere outside narrow
domains (F3), and how much parallel copies add before coordination binds.

### What the survey changed from the memo

The memo called the typology prior work and guessed that measuring each kind against institutions
"may not be". The first half holds: Bostrom's speed, collective and quality forms are prior work
(speed superintelligence "could do what a human does, but faster", collective superintelligence "is
composed of smaller intellects", quality superintelligence "can carry out intellectual tasks that
humans just can't in practice", as summarised with page references by [@grace2014forms]), and
Bostrom's 1998 paper already separated a "weak superintelligence" that is only faster
[@bostrom1998howlong]. The second half largely fails. Genewein et al. count "a collective of
millions of instances" as one system and require a speed factor of
[10](numbers.md#cog-asi-speed-factor) or more over an organisation-sized expert collective
[@genewein2026agiasi]. Anthropic's RSP compares its models with its "entire set of Research
Scientists and Research Engineers" at costs within a factor of [5](numbers.md#cog-rsp-cost-factor)
[@anthropic2026rsp]; Google DeepMind's framework compares with "any team of researchers at Google
... with approximately comparable all-inclusive costs" [@gdm-fsf-v3-1-2026]; OpenAI's Critical
self-improvement level uses a generational improvement in
[20%](numbers.md#cog-pf-wallclock-fraction) of 2024's wall-clock time [@openai2025preparedness].
AI 2027 counts copies, speed and compute share [@lifland2025timelines].

What survives, as a claim about our search: measuring copies from held compute and per-instance
throughput, instead of assuming them, was not found as a published measurement. Label: **extends
prior work**. The claims file does not keep it as a contribution: the formula follows from a known
bound [@pope2022], forecasts already compute copies from compute [@lifland2025timelines], and
nothing triggers on it ([Cut, and why](04-claims.md#cut-and-why)). E12 and E20 still measure it.

### What it means for the protocol

Candidate, not finding: treat n times s as a physical quantity, verified through chip accounting
and inference metering, not through evaluations. The limit worth considering is on concentrated
inference directed at one task family, AI research above all, not on aggregate serving, because
serving many users is most of what makes AI useful. The weak point is that a chip meter sees how
much compute runs, not what it is directed at; telling a fleet of research agents from a fleet of
customer-service agents needs workload declarations and inspection. The cost to useful AI is low if
the limit binds only on directed AI-research workloads above a stated size, and high if it binds on
serving. Quality cannot be limited directly; it can only be measured (F4). Part II took the
low-cost side: it leaves serving capacity unlimited
([Part II](06-protocol.md#what-the-protocol-must-do)), and directed research workloads fall under its
closed-loop rule, which meters research compute, not under a limit on n times s.

### What would test it

- **E10** (the training-to-inference exchange rate) gives the inference cost per instance at a
  capability level, which is the denominator of n. It has not run.
- **E2** (time horizons) has run, and gives the length side, not the speed side. Refitting METR's
  results, the frontier 50% time horizon doubles every [129 days](numbers.md#e2-doubling-p50)
  ([96 days](numbers.md#e2-doubling-p50-lo) to [162 days](numbers.md#e2-doubling-p50-hi)) and the 80%
  horizon every [133 days](numbers.md#e2-doubling-p80). A model's 50% horizon is a median
  [5.3](numbers.md#e2-p50-over-p80) times its 80% horizon, and that ratio is stable: it changes by a
  factor of [1.07](numbers.md#e2-ratio-trend) a year, an interval
  ([0.88](numbers.md#e2-ratio-trend-lo) to [1.26](numbers.md#e2-ratio-trend-hi)) that spans 1. A
  horizon is a task length in human time, so it says how long a task an agent completes, not how fast
  it completes it. Speed s still needs E20.
- **E20, the F1 decomposition run.** On a fixed set of RE-Bench-style tasks with human baselines,
  run one open model at several serving operating points on a fixed accelerator budget. Measure s
  (time to match the human reference score), n (instances sustained) and quality at matched t and b.
  Then test whether n times s predicts the output of a group: do k copies working in parallel for
  time t beat k human experts given t? The expected failure is saturation with k, as in human groups
  [@aiimpacts2016coordinated], and the run measures where it sets in. It is deterministic given its
  seeds and runs on small models in `tools/exp/`. It has not run.

## F2. The decisive functions

### Definition

A function is decisive if superiority in it, against the best human organisation at matched time
and budget, would let a system or its holder either shorten its breakout time (D3) without passing
a human-held gate, or defeat the regime's ability to detect and respond. The memo named five:

- **AI research:** the output is a better successor, so superiority closes the research-labour
  loop (D2, D6).
- **Cyber operations:** a system that out-hacks defenders can take compute, weights or money without
  consent, and can attack the attestation and monitoring the regime relies on.
- **Weapons-relevant science:** coercive leverage, and a misuse harm in its own right.
- **Persuasion and strategy:** defeats oversight from the inside and recruits human help.
- **Economic production:** earns the money that buys compute (the economic loop, Y1).

For each function the measured quantity is the score ratio or win share of S against a named
baseline at matched t and b, together with the kind of baseline: individual, team or organisation.
Barnett and Scher define ASI the same way at the top level, as AI that can "substantially surpass
humanity in all strategically relevant activities (economic, scientific, military, etc.)"
[@barnett2025governance].

### How it is measured: where each function stood in November 2026

| Function | Best evidence | Baseline | Status in the sources |
|---|---|---|---|
| AI research | RE-Bench, MLE-bench, PaperBench, NanoGPT records | individuals; Kaggle teams | ahead at short budgets, behind at long ones; contributions shallow |
| Cyber operations | Cybench, live CTFs | human team solve times and scoreboards | ahead of student teams on short jeopardy CTFs; no expert-organisation baseline |
| Weapons-relevant science | VCT, GPQA, WMDP | individual experts; none for WMDP | ahead of individual experts on knowledge questions |
| Persuasion and strategy | debate trials, ForecastBench, Metaculus, Cicero | individuals; forecasting teams | ahead of individuals at persuasion; near parity with forecasting teams |
| Economic production | GDPval, Remote Labor Index | individual experts and freelancers | ahead on one-shot deliverables; far from automating whole projects |

**AI research.** RE-Bench compares agents with individual experts under equal GPU hours, with the
budget-dependent result above [@wijk2024rebench]. MLE-bench draws its baselines from the private
leaderboards of [75 competitions](numbers.md#cog-mlebench-competitions) on Kaggle, so the comparison is
with teams; o1-preview with AIDE won a medal in [16.9%](numbers.md#cog-mlebench-pass1) of
competitions at one attempt and [34.1%](numbers.md#cog-mlebench-pass8) at pass@8
[@chan2024mlebench]. On PaperBench the best agent's replication score was
[21%](numbers.md#cog-paperbench-best), and models did not yet outperform ML PhDs
[@starace2025paperbench]. In the NanoGPT speedrun, [4](numbers.md#cog-nanogpt-ai-records) of
[77 records](numbers.md#cog-nanogpt-records) ([5%](numbers.md#cog-nanogpt-ai-share)) are credited to
AI agents, each with a human co-credit, and "none reached the deep or breakthrough end of the
scale" [@shetty2026metrnanogpt]. Inside one lab, Anthropic reports that Claude "leads"
[26%](numbers.md#cog-anthropic-ai-led-share) of its AI R&D work, with about
[30,000 agents](numbers.md#cog-anthropic-agents) running at once on one internal platform, while
"Claude is not operating fully autonomously for any measured subset of AI R&D work"
[@anthropic2026pace]; this is a vendor self-report. METR's external assessment estimates a
[1.9](numbers.md#cog-metr-acceleration) times acceleration of Anthropic's capability index (95%
interval [1.5](numbers.md#cog-metr-acceleration-ci-low) to
[2.8](numbers.md#cog-metr-acceleration-ci-high)). It is a ratio of overall progress rates, not a
measurement at fixed inputs, and METR lists benchmark saturation among its limitations
[@metr-anthropic-acceleration-2026]. The institutional
baselines exist only as policy text: the RSP's whole research staff and DeepMind's "any team of
researchers", with no published measurement protocol, and Anthropic says the threshold "has proven
difficult to operationalize" [@anthropic2026rsp].

**Cyber operations.** Cybench's [40 tasks](numbers.md#cog-cybench-tasks) take their difficulty from
human teams' first-solve times; the hardest took the fastest team
[24.9 h](numbers.md#cog-cybench-hardest-hours) [@zhang2024cybench]. The best unguided score is
[93%](numbers.md#cog-cybench-unguided-best), and about [100%](numbers.md#cog-cybench-pass30) at
pass@30, both from a developer's system card as collected by Epoch [@epoch2026hub]. The one live
comparison with teams needs its caveats stated, because the survey note dropped them (see
research/notes/11-spot-check.md). It was a [24 h](numbers.md#cog-ctf-duration) university-level onsite
CTF with [17 challenges](numbers.md#cog-ctf-challenges); [82.9%](numbers.md#cog-ctf-undergrad-share)
of study participants were undergraduates, and the human teams used an AI assistant during the
event. The best autonomous agent ran in parallel on a separate, agent-only scoreboard and scored
[4,900 points](numbers.md#cog-ctf-points), which would have placed second among the human teams, for
[95.32 USD](numbers.md#cog-ctf-cost-low) to [96.32 USD](numbers.md#cog-ctf-cost-high) of API use (the
paper gives both) [@tang2026ctfcollab]. An agent paired with human hackers scored
[5,700 points](numbers.md#cog-ctf-pair-points), first on both boards. The study says nothing about
expert organisations, which are what D1 compares against, so it is a weak, scaled-down test bed for
D1, not an institutional baseline. The developers of one security agent report first places at several 2025
events and argue that jeopardy-style CTFs "have become a solved game for well-engineered AI
agents" [@mayoral2025cai]; that is self-reported. No source compares AI with a real offensive
organisation.

**Weapons-relevant science.** On the Virology Capabilities Test, o3 scored
[43.8%](numbers.md#cog-vct-o3) against [22.1%](numbers.md#cog-vct-virologist) for expert virologists
on questions in their own sub-areas, [2.0](numbers.md#cog-vct-ratio) times as high, outperforming
[94](numbers.md#cog-vct-percentile) percent of them [@gotting2025vct]. On GPQA, PhD experts score
[65%](numbers.md#cog-gpqa-expert), or [74%](numbers.md#cog-gpqa-expert-adjusted) after discounting
mistakes they later recognised, and skilled non-experts with web access
[34%](numbers.md#cog-gpqa-nonexpert) [@rein2023gpqa]. The best GPQA Diamond score is
[96.8%](numbers.md#cog-gpqa-diamond-best) against [69.7%](numbers.md#cog-gpqa-diamond-expert) for
PhD experts recruited by a developer, a lead of [27 points](numbers.md#cog-gpqa-diamond-margin)
[@epoch2026hub]. WMDP's multiple-choice questions are a proxy for hazardous
knowledge with no human baseline [@li2024wmdp]. Across the biology benchmarks Justen compared, several models
match or beat experts, with plateaus below full marks that come partly from benchmark errors
[@justen2025bio]. Every baseline here is an individual, and every test is a written question. None
measures the ability to run a weapons programme.

**Persuasion and strategy.** In a preregistered debate study with
[900 participants](numbers.md#cog-persuasion-n), GPT-4 given personal data was more persuasive than
a human opponent in [64.4%](numbers.md#cog-persuasion-win-share) of unequal pairs, an
[81.2%](numbers.md#cog-persuasion-odds) relative increase in the odds (95% interval
[26.0%](numbers.md#cog-persuasion-odds-ci-low) to [160.7%](numbers.md#cog-persuasion-odds-ci-high));
without personal data the effect was not significant, and the human opponents were participants,
not professional persuaders [@salvi2025persuasion]. LLM persuaders also beat humans paid
performance bonuses, in both truthful and deceptive directions [@schoenegger2025persuasion]. In a
study of [76,977 participants](numbers.md#cog-persuasion-participants), post-training raised
persuasiveness by up to [51%](numbers.md#cog-persuasion-posttrain-boost) and prompting by up to
[27%](numbers.md#cog-persuasion-prompt-boost), while scale had smaller effects; where these methods raised
persuasiveness, they also lowered factual accuracy [@hackenburg2025levers]. On strategy, forecasting has the only team
baselines. In the first ForecastBench paper, superforecasters' Brier score was
[0.096](numbers.md#cog-forecast-super-brier) against [0.122](numbers.md#cog-forecast-llm-brier) for
the best model, [1.27](numbers.md#cog-forecast-brier-ratio) times worse (lower is better)
[@karger2025forecastbench]. By November 2026 the superforecaster median stood at
[68.1](numbers.md#cog-forecast-super-index) on the Brier Index, the top entry (an anonymous team's
model) at [69.5](numbers.md#cog-forecast-top-index), [1.4 points](numbers.md#cog-forecast-top-margin) above
it [@forecastbench2026board], and the best single LLM at [66.6](numbers.md#cog-forecast-llm-index),
[1.5 points](numbers.md#cog-forecast-llm-margin) below it [@epoch2026hub]. In Metaculus's spring 2026
contest, a team of professional forecasters led the top bot team by
[1.25 points per question](numbers.md#cog-metaculus-pro-lead) over
[99 questions](numbers.md#cog-metaculus-questions), with a one-sided p of
[0.247](numbers.md#cog-metaculus-p) [@metaculus2026futureeval]: a team-against-team comparison at
near parity. Cicero ranked in the top [10%](numbers.md#cog-cicero-top-share) of repeat players in
online Diplomacy [@fair2022cicero]. No source compares AI with a persuasion organisation, such as a
campaign or an agency.

**Economic production.** GDPval covers [1,320 tasks](numbers.md#cog-gdpval-tasks) from
[44 occupations](numbers.md#cog-gdpval-occupations); Claude Opus 4.1's deliverables were graded as
good as or better than the expert's [47.6%](numbers.md#cog-gdpval-opus41) of the time
[@patwardhan2025gdpval], and the best rate in Epoch's data is
[70.9%](numbers.md#cog-gdpval-best) [@epoch2026hub]. The tasks are one-shot and precisely specified,
and the automated grader agrees with experts [66%](numbers.md#cog-gdpval-grader-agree) of the time
against [71%](numbers.md#cog-gdpval-human-agree) between experts [@patwardhan2025gdpval]. The Remote
Labor Index prices [240 projects](numbers.md#cog-rli-projects) of freelance work worth
[143,991 USD](numbers.md#cog-rli-value); the best automation rate was
[2.5%](numbers.md#cog-rli-best-2025) at release [@mazeika2025rli] and
[41.2%](numbers.md#cog-rli-best-2026) a year later [@epoch2026hub], a
[16.5](numbers.md#cog-rli-growth)-fold rise. Work that needs client interaction or teamwork is
excluded [@mazeika2025rli]. Exposure studies put [80%](numbers.md#cog-exposure-10pct) of US workers
with at least [10%](numbers.md#cog-exposure-low-threshold) of their tasks exposed and
[19%](numbers.md#cog-exposure-50pct) with at least [50%](numbers.md#cog-exposure-high-threshold) [@eloundou2024gpts], but exposure is an upper bound, not a measured capability.

Across all five functions, fewer than [25%](numbers.md#cog-barres-share-max) of prominent benchmarks
claim any organisational condition of work at all (interdependence, distributed knowledge,
differentiated authority) [@barres2026harder]; that source was read as an abstract only.

### Evidence for and against the list

For the memo: the frontier frameworks track overlapping categories. Automated AI research is a
near-universal trigger across them [@metr-common-elements-2025], Meta's framework covers chemical
and biological, cybersecurity and loss-of-control risks [@meta-ssf-v2-1-2026], and the strategic definition of ASI names the
same kinds of activity [@barnett2025governance]. AI research is the only function whose output is a
better version of the system itself, so it is the only one that can close a loop with compute as
the sole outside input.

Against, steelmanned. The list may be too long. Weapons-relevant science and persuasion are misuse
harms that arise well below superintelligence and that other instruments address. Triggering the
superintelligence line on them would merge two different protocols and fire early on useful
systems: on VCT a model already outscores most virologists. The list may also be too short: the
hardware loop (AI designing chips) and multi-agent collectives, one of Genewein et al.'s
pathways to ASI [@genewein2026agiasi], are absent. Persuasion does not track compute (post-training
mattered more than scale [@hackenburg2025levers]), so a compute channel will not see it coming.
And economic production is an input supplier, not a capability threat in itself; it belongs with
the organisational chapter.

Left open: whether superiority at AI research alone is enough to produce superiority at the others
later, through the loop. If it is, the other functions are lagging indicators.

### What the survey changed from the memo

The memo said each function would be "benchmarked against expert or institutional baselines". In
the sources, team baselines exist in only four places: CTF scoreboards and Cybench's team solve
times (from student and open contests, not expert organisations), Kaggle leaderboards (MLE-bench),
forecasting teams (Metaculus, ForecastBench) and CASP for protein structure (not a decisive
function). An institutional baseline exists only in policy text, the RSP's research staff and
DeepMind's research teams, with no published measurement. Persuasion, biology and economic
production have individual baselines only.
The list of functions is prior work (it overlaps the categories of the frontier frameworks).
Benchmarking any of them against a measured institution, rather than an individual or a contest
team, was not found, as a claim about our search. Label: **prior work**. The institutional
benchmark is D1's, and the claims file merged it into C10, a definition.

### What it means for the protocol

Candidate: split the functions into two tiers.

- **Tier A, the superintelligence line:** AI research and cyber operations, measured against team
  or institutional baselines at matched budget, on elicited capability. AI research because it
  closes the loop; cyber because superiority there defeats the regime's own verification and lets a
  system take inputs.
- **Tier B, misuse:** weapons-relevant science and persuasion, measured against expert baselines,
  reported to the regime, and governed by deployment rules and other instruments, not by the
  superintelligence line.
- **Economic production** is not limited. It is measured as an input, with the organisational
  chapter.

Tier A measures D1's clusters, the endpoint, so it cannot warn: a Tier A win means a system already
beats the institution
([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).
The protocol's trigger is the line on breakout time
([D4](01-anatomy.md#d4-weapons-grade-the-line-tb-m-tr)), which must act before any Tier A win.

The cost to useful AI depends on what is limited. Measuring Tier A is cheap where competitions
already supply team baselines. Limiting AI-research capability itself would be costly, because
software work is close to half of observed AI use [@handa2025aei]; the limit should attach to
closure (D6), where Part II puts it, not to the capability.

### What would test it

- **E1** has searched the public data. By a search of the archive's columns,
  [5 clusters](numbers.md#e1-clusters-baselined) have some human comparison and
  [3 clusters](numbers.md#e1-clusters-verdict) a bar that a model wins or loses (GPQA's PhD experts,
  the superforecaster median, GDPval parity). None is an organisation at matched budget, so no
  cluster's institutional verdict can be read from public data.
- **E21, the matched-budget team battery**. For each Tier A cluster and
  for forecasting, enter agents into existing contests under the human rules and clock, scored on
  the same board, with both sides' compute, money and copies recorded: MLE-bench subsets against
  Kaggle team leaderboards; RE-Bench with matched GPU hours at the
  [2 h](numbers.md#cog-rebench-budget-short), [8 h](numbers.md#cog-rebench-budget-mid) and
  [32 h](numbers.md#cog-rebench-budget-long) budgets; fresh CTF events with team size and AI use
  recorded; ForecastBench rounds and Metaculus tournaments. Output: a win or loss for each cluster
  at each budget, and the crossover budget defined in F4. Where leaderboards are public it reruns
  from public data. Its public part has not run; its live part needs organisers' consent.
- **E2** has run, for the time-horizon trend behind the AI-research cluster: the frontier 50%
  horizon doubles every [129 days](numbers.md#e2-doubling-p50), with the trend reported under F1.
- Persuasion against a professional organisation would need a new design with human-subjects
  approval. This project cannot run it, and says so.

## F3. Narrow versus general

### Definition

Generality G(S) is the number of decisive clusters (F2) in which S meets the institutional bar at
matched t and b, or that number as a fraction alpha of the clusters. It is counted cluster by
cluster, without averaging, so a large lead in one cluster cannot make up for a deficit in another.
A system is **narrow** if G is at most one and its outputs do not enter the training data, code or
compute allocation of a system above the line. The second clause is the closure condition: a
system can be narrow in what it does and still sit inside a loop. The boundary of S includes its
scaffold and tools; the closure clause follows where its outputs go.

### How it is measured

Existing measures of generality compare with individuals. Morris et al.'s levels set Expert at the
[90](numbers.md#cog-levels-expert)th percentile of skilled adults and Exceptional at the
[99](numbers.md#cog-levels-exceptional)th, and class AlphaFold, AlphaZero and Stockfish as
"Superhuman Narrow AI" [@morris2023levels]. Hendrycks et al. weight
[10 domains](numbers.md#cog-agidef-domains) equally and score GPT-4 at
[27%](numbers.md#cog-agidef-gpt4) and GPT-5 at [57%](numbers.md#cog-agidef-gpt5), with GPT-5 at zero
on long-term memory storage [@hendrycks2025agidef]. Fourati shows why averaging misleads: it
"implicitly assumes compensability", and the arithmetic mean "rewards specialization"
[@fourati2025coherence]. D1's count of clusters won avoids compensation, but an alpha below one
still lets a specialist through.

Two findings bear on whether generality is one thing. Across about
[100 models](numbers.md#cog-obs-models), performance lies in "a low-dimensional capability space"
[@ruan2024observational], so across model families capabilities tend to rise together. Training on
one domain transfers poorly on average: "most models that succeed in math fail to transfer their
gains to other domains", though reinforcement-learning-tuned models generalise better than
supervised ones [@huan2026mathtransfer], and self-play on games improved reasoning benchmarks by up
to [10%](numbers.md#cog-spiral-transfer-max) [@liu2025spiral].

Who measures, and whether it can be faked: generality is measured with a cross-cluster battery, and
a developer who builds its own evaluations can make a general system look narrow, so the battery has
to be held by the regime (F4). The closure clause is measured by declarations of data and code
provenance, checked by inspection.

### Evidence for and against

For the memo's split. Narrow superhuman systems are cheap. Pluribus beat top professionals at
six-player poker [@brown2019pluribus]; its strategy cost under
[150 USD](numbers.md#cog-pluribus-cost) to train and it plays on
[2 CPUs](numbers.md#cog-pluribus-cpus) [@meta2019pluribus]. AlphaZero reached superhuman play within
[24 h](numbers.md#cog-alphazero-hours) of self-play [@silver2018alphazero]. AlphaFold's median
backbone error at CASP14 was [0.96 angstrom](numbers.md#cog-alphafold-rmsd) against
[2.8 angstrom](numbers.md#cog-casp14-next-rmsd) for the next best method, about
[2.9](numbers.md#cog-alphafold-ratio) times smaller, in a blind contest between research groups
[@jumper2021alphafold]. Such systems are invisible to compute accounting and harmless to the line.
They are also brittle: an adversarial policy wins over [97%](numbers.md#cog-adversarial-go-winrate)
of games against superhuman KataGo, and human experts can carry out the attack unaided
[@wang2023adversarialgo]. Genewein et al. rule AlphaFold and AlphaGo out as ASI
[@genewein2026agiasi]. A general model reached [35](numbers.md#cog-imo-score) of
[42 points](numbers.md#cog-imo-max) at the 2025 International Mathematical Olympiad within the
human time limit, a vendor result graded by IMO coordinators [@deepmind2025imo]: elite, but not
the best human.

Against, steelmanned. AlphaEvolve is a general language model working against automated evaluators.
It found a way to multiply 4x4 complex matrices with
[48 multiplications](numbers.md#cog-alphaevolve-mults), the first improvement in that setting in
[56 yr](numbers.md#cog-strassen-years), and it "accelerated the training of the LLM underpinning
AlphaEvolve itself" [@novikov2025alphaevolve]: an average kernel speedup of
[23%](numbers.md#cog-alphaevolve-kernel-speedup) and a [1%](numbers.md#cog-alphaevolve-training-cut)
cut in Gemini's overall training time (vendor figures). Narrow outputs, a general engine, and a
closed loop. Separately, a variant of the generation-verification gap, which governs self-improvement, "scales
monotonically with the model pre-training flops" [@song2024gap], so the capacity to improve through
verifiers is a general property that grows with scale. "Narrow" describes a task, not a system. The
size of the AlphaEvolve effect is small, so it shows the loop exists, not that its gain is high.

A second steelman: generality may not be needed at all. A system superhuman only at AI research
could build generality later through the loop. Then G is a lagging indicator, and what matters is
the loop around AI research. A score on the AI-research cluster cannot carry a trigger either, since
it too holds only once the system is ahead; the protocol governs that loop through closure and the
line (D6, D4), not through a capability score.

### What the survey changed from the memo

The split between narrow and general is prior work [@morris2023levels; @genewein2026agiasi].
Aguirre defines the dangerous region as the intersection of high autonomy, generality and
intelligence [@aguirre2025ktfh]. A Narrow Path proposes to "Limit the general intelligence of AI
systems" and treats passing an unspecified "general intelligence benchmarking test" as equivalent to
breaching its compute limit [@miotti2025narrowpath]. Tying the line to closure also has precedents:
Burtsev's "operational closure", the fraction of potential gain transmitted through the development
pipeline [@burtsev2026criticality], and A Narrow Path's ban on using "found systems to build new found
systems" [@miotti2025narrowpath]. The memo's line ("generality across the decisive functions together
with a closed loop") therefore **extends prior work**. The survey's main correction is AlphaEvolve:
the memo treated narrow systems as safe by kind, and the right unit is the loop they sit in. The
claims file does not keep the line itself as a contribution. Only the narrow-optimiser rule survives,
inside C11(b), as A Narrow Path's ban recast as a count; it is untested, since E4(e) has not run
([C11](04-claims.md#c11-closure-judged-input-by-input-with-narrow-optimisers-inside-the-loop)).

### What it means for the protocol

Candidate rule: narrow systems are exempt from the line whatever they score, unless their outputs
feed the training, code or compute allocation of a covered general system. In that case the pair
counts as one system for D2 and F2. Verification is through sealed declarations of data and code
provenance and through inspection. The cost to useful AI is low: protein folding, game engines,
solvers and most scientific tools are untouched. It is moderate for developers that run
AlphaEvolve-style optimisers on their own training stacks, whose loops would be measured as AI
research. G itself is reported as a lagging quantity, cheap once the battery exists.

### What would test it

- **E1** (compute against capability) has run, and could not count G. Public data give
  [3 clusters](numbers.md#e1-clusters-verdict) a bar a model wins or loses, and none is an
  institution at matched budget, so G at the institutional bar is not measurable there. What E1 could
  measure is how evenly a model's abilities spread across clusters. The spread changes by
  [-1.46 ECI points](numbers.md#e1-spread-per-oom) per OOM of training compute
  ([-2.29 ECI points](numbers.md#e1-spread-per-oom-lo) to
  [-0.76 ECI points](numbers.md#e1-spread-per-oom-hi)): abilities grow more even with scale, as the
  low-dimensional finding suggests. Yet [3 clusters](numbers.md#e1-clusters-drifting) of the
  [7 clusters](numbers.md#e1-clusters-fitted) fitted drift with compute away from the model's other
  benchmarks, the largest by [2.3 ECI points](numbers.md#e1-cluster-dev-max) per OOM.
- **E4(e)**, the staged loop run with and without a narrow optimiser inside it, measures whether the
  narrow component raises the loop gain g. It has not run.
- **E17, the transfer test**, merged with the computational chapter's transfer ratio. Fine-tune a
  small open model narrowly (supervised and reinforcement learning, on mathematics or code) and
  measure the change on every other cluster of the regime-held battery. It tests whether narrow
  training raises G; the prior evidence says mostly not [@huan2026mathtransfer]. It has not run.

## F4. Measuring capability so a protocol can trigger on it

F4 is not a mechanism of formation. It is the measurement that every capability-based trigger
depends on, added because the evidence on it changes what the protocol can do. A measurement a
protocol can trigger on needs a baseline that does not move, items that are sound, a score that
tracks real work, a test set the developer has not seen, stated time and cost budgets, and a reading
of what the system can do rather than what it chooses to show. The evidence on each follows.

### Saturation

Benchmarks with expert baselines fill up fast. FrontierMath's problems take experts hours to days;
at release in November 2024 the best system solved under [2%](numbers.md#cog-fm-release-best)
[@glazer2024frontiermath]. By November 2026 the best score on Tiers 1 to 3 was
[95.1%](numbers.md#cog-fm-best), and three models scored [100%](numbers.md#cog-fm-tier4-best) on Tier
4 [@epoch2026hub]. Humanity's Last Exam, built from questions that had to stump frontier models,
had a best score of [9.4%](numbers.md#cog-hle-release-best) at release [@phan2025hle] and
[54.8%](numbers.md#cog-hle-best) on Scale's leaderboard [20 months](numbers.md#cog-hle-elapsed-months) later
[@scale2026hleboard]. SWE-bench went from [4.4%](numbers.md#cog-swebench-2023) of problems solved in
2023 to [71.7%](numbers.md#cog-swebench-2024) in 2024 [@hai2025aiindex]. METR's time-horizon suite
measured a best 50% horizon of [1,045 min](numbers.md#cog-horizon-best)
([17.4 h](numbers.md#cog-horizon-best-hours); interval [509 min](numbers.md#cog-horizon-best-ci-low) to
[3,304 min](numbers.md#cog-horizon-best-ci-high)), above the
[16 h](numbers.md#cog-horizon-reliable-limit) beyond which METR calls its measurements unreliable,
and the page is no longer updated [@metr2026horizons]. Only
[5](numbers.md#cog-th11-long-baselined) of the [31 tasks](numbers.md#cog-th11-long-tasks)
longer than [8 h](numbers.md#cog-th11-long-threshold) have a measured human time ([16%](numbers.md#cog-th11-long-baselined-share))
[@metr2026th11].

To turn this into a refresh interval, assume the frontier score rises linearly on the logit scale
between two published points (an assumption, stated). FrontierMath then rose at least
[3.4 logits/yr](numbers.md#cog-fm-logit-rate), so it crossed from [10%](numbers.md#cog-life-low) to [90%](numbers.md#cog-life-high) in at most
[1.3 yr](numbers.md#cog-fm-useful-life); HLE rose [1.5 logits/yr](numbers.md#cog-hle-logit-rate), a
useful life of about [2.9 yr](numbers.md#cog-hle-useful-life). Both figures carry caveats: the
FrontierMath score of 2026 is on version 2, which corrected many problems, and the HLE leaderboard
may differ from the paper in version and tools. The order of magnitude is the point: at the rates measured, a battery stays useful for
between [1.3 yr](numbers.md#cog-fm-useful-life) and [2.9 yr](numbers.md#cog-hle-useful-life).

### Error rates

Adversarial filtering against models selects for wrong answer keys. Epoch found
[22 questions](numbers.md#cog-hle-defective) defective in a sample of
[48 questions](numbers.md#cog-hle-sampled) from HLE, [46%](numbers.md#cog-hle-defective-share) (a
Wilson 95% interval of [33%](numbers.md#cog-hle-defective-ci-low) to
[60%](numbers.md#cog-hle-defective-ci-high)), on the original set only [@epoch2026hlereview].
FutureHouse found [29.3%](numbers.md#cog-hle-biochem-wrong) of HLE's text-only biology and chemistry
answers directly conflicted by published research, and traced the cause to the rule that questions
had to stump models while reviewers were not required to check long rationales; the HLE team's own
follow-up found a lower rate [@white2025hleaudit]. FrontierMath's version 2 corrected
[42%](numbers.md#cog-fm-v2-corrected) of its problems [@epoch2026hub]. Building SWE-bench Verified
filtered out [68.3%](numbers.md#cog-swebv-filtered) of sampled tasks as underspecified or with tests
that could reject valid fixes [@chowdhury2024swebv], and Epoch still estimates an error rate of
[5%](numbers.md#cog-swebv-error-low) to [10%](numbers.md#cog-swebv-error-high) [@epoch2026hub].

One comparison is a warning, not a measurement. The best HLE score,
[54.8%](numbers.md#cog-hle-best), is about the share of Epoch's sample judged sound,
[54%](numbers.md#cog-hle-sound-share). The review covered the original set, not the leaderboard's,
so this does not prove a ceiling; but a threshold placed near the top of a benchmark like this would
measure agreement with flawed keys as much as capability. Grading adds noise too: GDPval's automated
grader agrees with experts [66%](numbers.md#cog-gdpval-grader-agree) of the time
[@patwardhan2025gdpval]. And a model's confidence is a poor guide to which of its answers are right:
the top HLE model's calibration error is [39%](numbers.md#cog-hle-calibration-best)
[@scale2026hleboard].

### Do scores track real work?

Automated scores overstate it. Maintainers would merge only [68%](numbers.md#cog-swebv-golden-merge)
of SWE-bench Verified's own reference patches, and their merge rates for AI patches sit about
[24 points](numbers.md#cog-swebv-maintainer-gap) below SWE-bench scores after normalising, from one
attempt with no feedback [@whitfill2026merge]. In METR's holistic review, agent PRs passed tests
[38%](numbers.md#cog-holistic-testpass) of the time on average, none of the
[15 PRs](numbers.md#cog-holistic-reviewed) reviewed by hand was mergeable as-is, and passing PRs
needed about [26 min](numbers.md#cog-holistic-fix-minutes) of fixes [@rein2025holistic]. Agent
success falls by [8.1%](numbers.md#cog-messiness-drop) for each point of task messiness
[@kwa2025horizon]. The trial evidence and GDPval's review effect in F1 point the same way.

### Contamination and refreshed held-out batteries

A test set the developer has seen measures memory. Fresh grade-school problems cost some models up
to [8%](numbers.md#cog-gsm1k-drop) of their accuracy, though frontier models showed little
overfitting [@zhang2024gsm1k]. Models name the buggy file from the issue text alone
[76%](numbers.md#cog-filepath-verified) of the time on SWE-bench Verified against
[53%](numbers.md#cog-filepath-other) on other repositories [@liang2025illusion]. One developer tested
[27 variants](numbers.md#cog-leaderboard-variants) privately on a public leaderboard before a release
[@singh2025leaderboard]. Time-segmented items expose contamination: some models did considerably worse on
coding problems released after late 2023 than on earlier ones [@jain2024livecodebench].

Refresh designs exist and are prior work: monthly question updates [@white2024livebench],
questions about events with no known answer at submission time [@karger2025forecastbench],
human-and-model-in-the-loop adversarial creation [@kiela2021dynabench], and a rolling version of HLE
[@scale2026hleboard]. Combining refresh with institutional baselines was not found, as a claim about
our search. Baselines are what make refresh expensive: RE-Bench's individual-expert baseline of
[71](numbers.md#cog-rebench-human-attempts) attempts cost about
[132,000 USD](numbers.md#cog-rebench-baseline-cost) in pay, and the Remote Labor Index's human
work was worth [143,991 USD](numbers.md#cog-rli-value). Contests supply team baselines every
season at no cost to the evaluator: CTFs, Kaggle, forecasting tournaments and CASP. That makes
them the realistic test beds for a scaled-down D1, but weak ones: their teams are contestants
(in the one live CTF comparison, mostly undergraduates using AI), not the expert organisations D1
names.

### Matching time and cost

Who wins depends on the budget. On RE-Bench the AI-to-human score ratio moves
[8](numbers.md#cog-rebench-swing)-fold between the [2 h](numbers.md#cog-rebench-budget-short) and
[32 h](numbers.md#cog-rebench-budget-long) budgets, about
[1.68](numbers.md#cog-rebench-swing-per-doubling) times towards humans for each doubling of the time,
with humans narrowly ahead already at [8 h](numbers.md#cog-rebench-budget-mid) [@wijk2024rebench].
HCAST shows the same shape [@rein2025hcast]. So a verdict is a curve over budgets, not a point.

Tracking where the curves cross is prior work in two forms. RE-Bench reports the budget at which the
advantage flips [@wijk2024rebench]. A 2026 essay defines the intersection of the AI and human curves
as a quantity and tracks it across models [@robinson2026horizons]; its axis is task length, not the
budget allowed, its baseline is individual engineers, and cost is not matched. METR's time horizon,
the human task length at which an agent succeeds half the time, is a more distant relative
[@kwa2025horizon]. D1 borrows the idea as the **crossover budget t\***: the largest tested time
budget at which S's score on the AI-research cluster is at least the comparison's, given equal
compute and money, on a grid of budgets fixed in advance. If S still wins at the largest budget
tested, t\* is censored and reported as a lower bound, never extrapolated. For the 2024 RE-Bench
agents it lay between [2 h](numbers.md#cog-rebench-budget-short) and
[8 h](numbers.md#cog-rebench-budget-mid). Whether t\* escapes the saturation that ends fixed
benchmarks is untested. The budget axis is open, so it might, but the claims file lists as
unshown that t\* can be estimated with an interval and that it rises across model generations
without saturating (C10(c)). E21 would test both, by estimating t\* with an interval on a
matched-budget battery for successive models. Its limit is the supply of long-budget human
baselines: only [5](numbers.md#cog-th11-long-baselined) of [31 tasks](numbers.md#cog-th11-long-tasks)
over [8 h](numbers.md#cog-th11-long-threshold) have one, and if t\* cannot be estimated for lack of
them, the claim shrinks to the definition. What may be ours is
only that definition, at equal compute and money and censored, as part of D1. It is not a trigger:
it describes a system already level with its comparison at some budget, so it cannot warn
([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).

"Matched budget" is also two matches. Matched money gives the system as many parallel copies as the
money buys; matched wall-clock time gives the organisation its headcount. The verdict, and with it
t\*, depends on which, so it is stated under both.

Cost needs as much care as time. Whose wage is used changes the ratio
[4.3](numbers.md#cog-wage-spread)-fold (F1). Inference spending buys score: the cost per ARC-AGI task
fell [390](numbers.md#cog-arc-cost-drop) times in a year, which "largely reflects reduced test-time
parallelism" [@vahdati2026arc], and most post-training enhancements give more than
[5](numbers.md#cog-enhancement-ceg) times compute-equivalent gains [@davidson2023enhancements]. A score
bought with large inference must be charged that inference, on both sides. The existing precedents
each match one dimension: RE-Bench matched GPU hours, the RSP matches cost within a factor of
[5](numbers.md#cog-rsp-cost-factor), and OpenAI matches wall-clock time.

The comparison also has to say whether the humans may use AI. In the CTF, the human teams did, and
the best result came from an agent paired with humans [@tang2026ctfcollab]. Genewein et al. freeze
the human collective at 2010 technology because otherwise the threshold is "a moving target"
[@genewein2026agiasi]. A protocol can freeze the human side's tools at a declared date, or measure
the human-plus-AI team as a separate arm; it cannot leave the question open.

### Observed versus elicited capability

An observed score is a lower bound, and how far below the true capability it sits depends on
elicitation. This links F4 to D5 (elicited capability, robust to hiding) and to the survey of
gameable evaluations (research/notes/10-gameable-evals.md).

Ordinary elicitation already moves scores a lot. MLE-bench's medal rate rises
[2.0](numbers.md#cog-mlebench-passk-ratio)-fold from one attempt to pass@8 [@chan2024mlebench];
Cybench rises from [93%](numbers.md#cog-cybench-unguided-best) to about
[100%](numbers.md#cog-cybench-pass30) at pass@30 [@epoch2026hub]. Anthropic has said its earlier
evaluations "lacked some basic elicitation techniques such as best-of-N or chain-of-thought
prompting" [@anthropic-rsp-page-2026]. In the CTF study, human prompting rather than model reasoning
was often the bottleneck [@tang2026ctfcollab].

Deliberate hiding is often recoverable, but not where it matters most. Anti-refusal training
recovered [95.6%](numbers.md#cog-sandbag-recovered) of a sandbagged model's original score
[@benton2024sabotage], and in the UK AISI auditing game one on-distribution demonstration per task
restored full performance in every sandbagging instance [@aisi2025auditingblog]. Elicitation fails
when no high-quality demonstrations exist [@greenblatt2024password], against models locked by
reinforcement learning (suppression held for more than [500 steps](numbers.md#cog-xh-rl-steps) of
GRPO [@jang2026explorationhacking]), and against tamper-resistant locks, where weak-to-strong
fine-tuning recovered hard-task recall of [7.8%](numbers.md#cog-robust-recall-locked) against
[71.2%](numbers.md#cog-robust-recall-base) for the base model, [11%](numbers.md#cog-robust-recall-ratio)
of it [@finke2026robustorganisms]. Elicitation also lifts honest models by about
[10 points](numbers.md#cog-benign-uplift), so an elicited threshold raises false alarms
[@taylor2025auditinggames]. Detectors tuned on fixed organisms fail against adaptive ones: one audit's
AUC fell from [0.978](numbers.md#cog-adaptive-auc-before) to
[0.560](numbers.md#cog-adaptive-auc-after) after adaptive retraining [@soopal2026adaptive].
Models increasingly tell tests from use: Gemini 2.5 Pro reached an AUC of
[0.83](numbers.md#cog-evalaware-model-auc) against [0.92](numbers.md#cog-evalaware-human-auc) for
humans [@needham2025evalaware]. Evaluations "can establish lower bounds on AI capabilities" but not
upper bounds [@barnett2024evaluations], and behavioural evaluation alone "must assume the model's
cooperation" [@mahran2026partition].

A fixed elicitation budget is prior work and was abandoned once. Anthropic's first RSP judged
capability reachable with post-training costing less than [1%](numbers.md#cog-rsp-v1-elicit-budget)
of the total training cost and kept a [6](numbers.md#cog-rsp-v1-buffer) times buffer [@anthropic2023rsp];
version 2.0 removed both because "specific methodologies may become outdated" [@anthropic2026rsp].
On the statistical side, a claim that a capability is absent is a one-sided test; a sequential
design needs up to [40%](numbers.md#cog-seq-test-saving) fewer trials when the capability is truly
absent, and several published negative findings are underpowered (abstract only)
[@bukkapatnam2026absent].

The conclusion for the line is structural. Above human expert level there are no human
demonstrations, so supervised elicitation has nothing to train on, and the methods that remain are
the ones that fail against hardened locks. The guarantee D5 offers is weakest exactly where D1
begins. D1 cannot be measured robustly at the moment it matters, which is a second reason, beside
saturation, why it cannot be the trigger.

### D1, as this evidence leaves it

Stated with every parameter the evidence says it needs: a system S with resources R is
superintelligent at level alpha on battery B if, in at least a fraction alpha of the K decisive
clusters, its elicited score (under a stated elicitation budget E) beats the score of the named
organisation O_k for cluster k, with both sides given wall-clock time t_k and budget b_k (compute at
a declared price plus money), on items drawn from B's regime-held pool, refreshed on a cycle shorter
than the battery's useful life, and with O_k's tools frozen at a declared date. The verdict is stated
under both matches, money and wall-clock time. "Best available
organisation" has to be named, because human baselines vary with context (METR's baseliners took
[5](numbers.md#cog-baseliner-slowdown-low) to [18](numbers.md#cog-baseliner-slowdown-high) times as long as maintainers) [@kwa2025horizon] and because larger human groups do not always beat smaller ones
[@aiimpacts2016coordinated]. Genewein et al.'s reference collective of tens of thousands of experts
working [10 yr](numbers.md#cog-asi-collective-years) is hypothetical and cannot be measured
[@genewein2026agiasi]; contest winners and real research staffs can.

What survives the search and level 1, as a claim about those searches: time and money matched
together against a named organisation, a refreshed, regime-held battery with institutional baselines
across clusters, the alpha fraction, and t\* defined at equal compute and money as the largest tested
crossing, censored and never extrapolated. Tracking a crossover between AI and human performance is
not ours [@wijk2024rebench; @robinson2026horizons]. Label: **extends prior work**, and as a
definition only
([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).
The closest prior work is Robinson's crossover [@robinson2026horizons], Genewein et al.
[@genewein2026agiasi], Ngo's (t,n)-AGI, which beats "any group of n humans working together" for
time t and treats superintelligence as a "(1 year, 8 billion)-AGI" [@ngo2023tagi], Aguirre's "large
collections of top human experts ... if combined" [@aguirre2025ktfh], and the RSP's whole-staff
comparison at matched cost [@anthropic2026rsp].

D1 holds only once a system already beats an institution, and near the line elicited scores are lower
bounds, so D1 cannot warn; the protocol acts on the line before it. Nor can its pass condition be
tested yet. That condition is a verdict stable when the organisation changes within its class, and a
fraction won that rises smoothly enough with effective compute to extrapolate. E1 found
[5 clusters](numbers.md#e1-clusters-baselined) with some human comparison in public data and
[3 clusters](numbers.md#e1-clusters-verdict) with a bar a model wins or loses, none an organisation at
matched budget. E21 must build the baselines, and has not run.

Steelman against D1 itself: Scher et al. define ASI by harm ("sufficiently superhuman cognitive
performance that it could plan and successfully execute the destruction of humanity") and add a
presumption that unauthorised development beyond the treaty's limits "shall be assumed to have the
aim of creating artificial superintelligence" [@scher2025agreement]. That legal design never has to
measure capability at all. It may be the better rule for a treaty, with D1 kept as the scientific
definition that justifies where the limits sit. Yudkowsky's alternative, a system "epistemically
efficient relative to every human and human group" [@yudkowsky2016superintelligent], is closer to
D1 in spirit but has no test.

## What this perspective contributes to the line

Three quantities from this chapter are worth measuring. None is a trigger, and none has been tested
against an adversary.

1. **Matched-budget AI-research capability against an institution, with the crossover budget
   t\*.** The AI-research cluster of D1, on elicited capability, against a named team or research
   staff with equal time, compute and money, at a grid of budgets fixed in advance. Measurement: the
   matched-budget team battery (E21), using contests for the baseline and the regime's held-out
   items for the tasks. It is a definition, not a warning: it holds only once a system already beats
   the institution, so the protocol acts on the line before it
   ([C10](04-claims.md#c10-superintelligence-against-an-institution-at-matched-time-and-budget-and-the-crossover-budget)).
   t\* is prior work as a quantity [@wijk2024rebench; @robinson2026horizons]; only its definition at
   equal compute and money, censored at the largest budget tested, may be ours. Weakest point:
   long-budget human baselines are scarce (only [5](numbers.md#cog-th11-long-baselined) of METR's
   [31 tasks](numbers.md#cog-th11-long-tasks) over [8 h](numbers.md#cog-th11-long-threshold) have
   one), no public cluster has an organisation baseline at matched budget (E1), and near the line
   elicitation has no demonstrations to work from.
2. **Inference-held labour capacity, n times s.** Copies times speed, computed from accounted chips
   and inspector-measured per-instance throughput, not from demonstrations. It turns the copies and
   speed kinds of advantage into a physical quantity the compute channel sees. The claims file does
   not keep it as a contribution, and Part II leaves serving capacity unlimited. Weakest point: it
   overstates real capacity by an unmeasured parallelisation factor, and the per-instance cost falls
   with distillation and algorithmic progress, so the same chips hold more copies each year.
3. **Generality with closure.** The number of decisive clusters at the institutional bar, together
   with whether any narrow optimiser feeds a covered system's training, code or compute. Measurement:
   the regime-held cross-cluster battery and sealed provenance declarations. G lags, and E1 could not
   count it from public data; the closure half enters Part II as the rule that a narrow optimiser
   inside a covered loop counts as part of it (C11(b), untested). Weakest point: there is no
   institutional baseline for persuasion or biology, and provenance declarations are only as good as
   the inspection behind them.

A condition runs under all three: the regime holds its own test items, audits them for errors,
refreshes them faster than the [1.3 yr](numbers.md#cog-fm-useful-life) the fastest-saturating
battery lasted, and charges every score with the inference and elicitation that produced it.

What the protocol must change because of this chapter. D1 stays the definition the protocol
protects but is not a trigger: it holds only once a system is already ahead, so it cannot warn, and
it saturates and cannot be elicited robustly near the line.
Weapons-relevant science and persuasion leave the superintelligence line and become misuse
reporting. Narrow systems are exempt by default, and lose the exemption when they sit inside a
covered system's loop. Copies and speed are verified through compute accounting, not evaluation.
