# Part I, 3: The dynamical perspective

The physical and computational chapters ask what a superintelligent system would take and how
capability follows from compute. This chapter asks how a capable system becomes a much more capable
one without anyone adding the inputs by hand. Every account we surveyed gives the same answer:
feedback. Some output of AI (better algorithms, better chips, money, experience, copies of itself)
becomes an input to the next round of AI. Each such loop can be written as a growth law. If its
returns, once diminishing returns are counted, sit below 1, the loop slows down. If they sit above
1, it accelerates until something physical stops it. Loops that are each below 1 can be above 1
together.

This is why the perspective matters for the line between useful AI and the path to
superintelligence. Useful AI can keep improving under loops that saturate. The path to
superintelligence is the regime in which the combined feedback is above 1 and fast compared with the
time a regime needs to notice and respond. The dynamical perspective therefore supplies the kind of
quantity a protocol can hold down: a gain, not a capability score.

The memo built the project's name on this idea. The survey shows that the idea, its mathematics and
even the name "loop gain" are prior work: Yudkowsky framed self-improvement as a neutron
multiplication factor in 2013 [@yudkowsky2013iem], Davidson, Halperin, Houlden and Korinek proved
the coupled condition in 2026 [@davidson2026feedback], Cunningham et al. named and calibrated the
loop gain [@cunningham2026rsi], and Burtsev defined a recursive reproduction number across
development cycles and across actors [@burtsev2026criticality]. None of it is new. What may remain
ours is narrower, and the independent prior-art search narrowed it again. An exact round identity
used to estimate the loop gain in a staged run, with a budget ladder, extends prior work narrowly; it
is a measurement whose power to decide anything is not yet shown, and as a trigger it is cut on
current evidence. The coupled-gain certificate applied as a treaty test, each edge cut and verified
separately, is an application of prior work: the certificate is control theory's small-gain theorem
[@dashkovskiy2007smallgain], and on today's evidence it cannot issue. Both are candidates, not
findings, and "not found" below is always a claim about our search.

The chapter states one common form, then the five loops (Y1a to Y1e), then runaway against
saturation (Y2) and coupling (Y3), and closes with the quantities the protocol should measure or
limit. None of them is yet a trigger.

## The common form: a growth law and its returns

Every loop below is written in the semi-endogenous form of Jones (1995), as used by Bloom et al. and
by Epoch [@bloom2020ideas; @besiroglu2024returns]:

```
(1/X) dX/dt = theta * X^(-beta) * E^lambda,        r = lambda / beta
```

X is the stock the loop improves: software efficiency, compute per dollar, compute capital, a
deployed model's skill, or the number of copies. E is the input that improves it. A positive beta
says ideas get harder to find as X grows. lambda says how much a doubling of input buys (below 1
when parallel effort duplicates). r is the number of doublings of X per doubling of cumulative
input.

The loop closes when the input is itself supplied by the stock, E = c * X^e, with e the closure (how
fully the stock supplies its own input). Then

```
(1/X) dX/dt = g0 * (X/X0)^(beta * (K - 1)),        K = e * r
```

K is the loop's own gain. With full closure (e = 1) it equals r. Three regimes follow. Writing u =
ln(X/X0) and k = beta * (K - 1), the law is du/dt = g0 * exp(k u), so (1 - exp(-k u)) / k = g0 t.

- **K < 1:** the growth rate falls as X rises, and each doubling of X takes longer than the last by
  a factor 2^(beta (1 - K)). This is saturation of the rate, not necessarily of the level.
- **K = 1:** steady exponential growth.
- **K > 1:** each doubling is faster than the last by a factor 2^(-beta (K - 1)). Doubling times
  form a convergent series and u diverges at t* = 1 / (g0 beta (K - 1)). Physical limits stop it
  first, which is why the headroom of each loop matters.

Three consequences for measurement recur in every section.

1. **Units.** The condition holds on a logarithmic, compute-equivalent axis with rounds of equal
   budget. On a bounded benchmark, gains shrink near the ceiling whatever the feedback, so a raw
   ratio of score gains does not measure K. Cunningham et al. note that their product of
   elasticities is invariant to how capability is normalised [@cunningham2026rsi]; a ratio of raw
   gains is not.
2. **Inputs grow.** Human research inputs are not held fixed in practice. Doubling chip density took
   [18](numbers.md#dyn-bloom-moore-researchers) times as many researchers in 2014 as in the early
   1970s [@bloom2020ideas]. Output growth must be divided by input growth: Cunningham et al. measure
   the return to R&D as g_A / g_R on a balanced growth path, with g_R the spend-weighted growth of
   researchers, experiment compute and research inference [@cunningham2026rsi]. Alston and Pardey
   warn that contemporaneous output-to-input ratios misstate returns when research acts with long
   lags [@alston2022ideas], which applies whenever a measurement round is shorter than the lag from
   idea to deployed capability.
3. **Slope is not gain.** "Rapid capability growth is therefore neither necessary nor sufficient
   evidence of recursive criticality" [@burtsev2026criticality]. Fast progress can be subcritical
   (driven by growing inputs) and early supercritical progress can look ordinary. Diagnosing the
   regime takes per-cycle estimates of gain and of how fast the next gain gets harder.

For several loops, write K_ij = lambda_i * e_ij / beta_i, where e_ij says how strongly stock j
supplies loop i's input. The diagonal holds each loop's own gain and the off-diagonal terms are
cross-feeds. In their innovation-network model, Davidson et al. prove that growth is explosive if
and only if the spectral radius of the corresponding matrix exceeds 1 (their Proposition 1)
[@davidson2026feedback]. In the normalisation used here the condition is rho(K) > 1 (Y3). None of
this frame is ours. We use it so that every loop is stated the same way and its parameters can enter
one matrix.

## Y1a. The software loop

### Definition

The stock S is software efficiency: the effective compute per physical operation for a fixed
capability, measured in compute-equivalent units on a log scale, as in the algorithmic-progress
literature: compute for a fixed language-model performance halved every
[8.4 months](numbers.md#dyn-algo-halving-months) from 2012 to 2023 [@ho2024algorithmic]. The input
is research effort: human researchers, AI research labour, experiment compute and research
inference. The boundary is one party's frontier research programme. The loop: higher S gives better
models, which supply more and better AI research labour, which raises the growth of S.

```
(1/S) dS/dt = theta_S * S^(-beta_S) * E_S^lambda_S
E_S = (L_human + L_AI)^(1 - eps_K) * C_exp^eps_K      (the Cobb-Douglas form Ho and Whitfill use)
L_AI proportional to S * C_inf                          (efficiency times inference compute)
```

With physical compute fixed and AI labour dominant, E_S grows as S^(1 - eps_K), so the loop's own
gain is K_S = r_S * (1 - eps_K). That factor is the compute-bottleneck correction discussed below.

This is the memo's D2, restated. The loop gain of the software loop is K_S over one development
cycle, on a log compute-equivalent axis, with input growth divided out. It is the same quantity as
the product in Cunningham et al.'s core condition, (return to R&D) x epsilon_R,C x epsilon_C,A > 1
[@cunningham2026rsi], and as Burtsev's R_AI = chi * a / sigma, whose factor chi, the "operational
closure", is close to the memo's D6 [@burtsev2026criticality].

### Measurement

There are three routes, each with a different owner and a different way to fail.

- **Historical fits.** r is fitted to idea-production data by naive, regression, likelihood or
  Bayesian methods [@erdil2024idea]. Error: the intervals are wide; selection bias can push
  observational estimates of algorithmic progress either way, because compute choices depend on
  algorithmic quality, and a first-pass comparison suggests they overstate it by a factor of about
  [9](numbers.md#dyn-selection-bias-factor) [@whitfill2025selection]; and measured efficiency
  depends on scale and on the reference algorithm: of a claimed
  [22,000](numbers.md#dyn-algo-gain-claimed)-fold language-model efficiency gain from 2012 to 2023,
  less than [100](numbers.md#dyn-algo-gain-small-max)-fold is accounted for at small compute
  [@gundlach2025origin]. Anyone with public data can run them; nobody can fake the public record,
  but it describes human-driven progress.
- **Declarations from inside a lab.** Cunningham et al. ask for lab algorithmic efficiency growth,
  spend shares by input, and the share of technical advances produced by AI [@cunningham2026rsi].
  Only the developer holds these data. An independent assessor sees what the developer releases.
  METR's assessment of Anthropic notes that most of the informative evidence was redacted, and that
  "Anthropic changed the scope of this project midway to exclude compute verification and instead
  just focus on AI R&D acceleration. This component was canceled before METR came to any substantive
  conclusions on compute usage at Anthropic." [@metr-anthropic-acceleration-2026]. Declarations can
  be shaped or withdrawn.
- **Staged runs.** An agent improves a small model's training recipe over rounds at fixed compute
  (E4). A public harness exists: the NanoGPT speedrun fell from
  [2,700 s](numbers.md#dyn-speedrun-baseline-s) to [39.9 s](numbers.md#dyn-speedrun-record-s) on
  fixed 8xH100 hardware over [824 days](numbers.md#dyn-speedrun-span-days), a factor of
  [67.7](numbers.md#dyn-speedrun-ratio) [@moddednanogpt; @epoch2026speedrundata], and a benchmark of
  reimplementation tasks is built on its records [@zhao2025speedrun]. E4's recount of Epoch's series
  gives a speedup of [70](numbers.md#e4-speedup) over [92 records](numbers.md#e4-records), each
  record's gain counted under the rules then in force; [84%](numbers.md#e4-algo-share) of the log speedup came from algorithmic records,
  and [1.1%](numbers.md#e4-ai-share) from the [5 records](numbers.md#e4-ai-records) that credit an AI
  system, each with a human. Error: small-scale returns may
  not transfer to the frontier [@gundlach2025origin], wall-clock time mixes systems engineering with
  algorithms, and an agent can depress its own result. Claude 3.7 Sonnet was "almost capable of
  zero-shot sabotage without using a scratchpad" on ML tasks, and zero-shot monitors showed an
  "underwhelming true positive rate" at low false-positive rates [@gasteiger2025subtlesandbag]. A
  staged gain is a lower bound unless the agent is elicited by fine-tuning on the task. In E4's
  simulation an agent that withheld gain in a pattern kept the upper-bound rule silent in at least
  half the runs on a loop at the corrected 95th percentile by withholding
  [16%](numbers.md#e4-hide-silence-fav) of its achievable gain, even with large, tightly measured
  rounds; that is the shortfall an elicitation step would have to catch.

### Evidence for and against

**For a loop that is closing.** The research-labour input is being automated quickly inside at least
one lab. Anthropic reports that Claude leads [26%](numbers.md#dyn-anthropic-ai-led) of its AI R&D
work, up from under [1%](numbers.md#dyn-anthropic-ai-led-feb) in February 2026, a factor of at least
[26](numbers.md#dyn-anthropic-ai-led-multiple) in six months; that over
[90%](numbers.md#dyn-anthropic-collab-share) of the work is at or above "AI collaborates"; and that
about [30,000](numbers.md#dyn-anthropic-agents) agents run at once on its most-used internal
platform [@anthropic2026pace]. These are vendor figures rated by Claude judges, and the same report
says "Claude is not operating fully autonomously for any measured subset of AI R&D work." METR's
independent assessment measured a [1.9](numbers.md#dyn-metr-accel)-fold acceleration (95% CI
[1.5](numbers.md#dyn-metr-accel-lo) to [2.8](numbers.md#dyn-metr-accel-hi)) in Anthropic's internal
capability index since October 2025: the fitted slope rose from
[15](numbers.md#dyn-metr-aeci-before) to [29](numbers.md#dyn-metr-aeci-after) points a year, a ratio
of [1.9](numbers.md#dyn-metr-slope-ratio) [@metr-anthropic-acceleration-2026]. METR subjectively
attributes about [80%](numbers.md#dyn-metr-ai-attribution) of the October 2026 acceleration to AI
and is confident it was not driven by faster training-compute scaling; staff polls reported a
[12](numbers.md#dyn-metr-staff-uplift)-fold self-reported uplift, which METR treats as "very loose
evidence". On historical data, the language-model estimate of r is [1.89](numbers.md#dyn-r-lm) (90%
interval [1.07](numbers.md#dyn-r-lm-lo) to [3.21](numbers.md#dyn-r-lm-hi)), the only domain whose
interval lies wholly above 1; computer vision is [1.26](numbers.md#dyn-r-cv)
([0.73](numbers.md#dyn-r-cv-lo) to [2.09](numbers.md#dyn-r-cv-hi)) and reinforcement learning
[1.20](numbers.md#dyn-r-rl) ([0.38](numbers.md#dyn-r-rl-lo) to [2.71](numbers.md#dyn-r-rl-hi))
[@ho2025experiments]. In Davidson and Houlden's model, with a median r of
[1.2](numbers.md#dyn-sie-r) (range [0.4](numbers.md#dyn-sie-r-lo) to [3.6](numbers.md#dyn-sie-r-hi))
and compute held fixed, the chance that full automation of AI research compresses three years of
progress into one is [57%](numbers.md#dyn-sie-p-3yr), and ten years into one,
[18%](numbers.md#dyn-sie-p-10yr) [@davidson2025sie]. A broad group of authors expects AI to automate
most or all AI R&D "within a few years" (we read only its abstract) [@chan2026explosion], and
Cunningham et al. find the feedback loops "appear to be strengthening" [@cunningham2026rsi].

**Against, steelmanned (this side cuts against the memo's rank 1 for self-improvement).** Compute,
not algorithms, may set the pace. Ho and Whitfill show that if compute takes about two thirds of
research input ([0.67](numbers.md#dyn-research-compute-share)) and is held fixed, every estimate of
r should be divided by about [3.0](numbers.md#dyn-bottleneck-divisor), "which puts them all below 1"
[@ho2025experiments]. Our arithmetic on their medians gives [0.42](numbers.md#dyn-r-cv-corrected)
for computer vision, [0.40](numbers.md#dyn-r-rl-corrected) for reinforcement learning and
[0.63](numbers.md#dyn-r-lm-corrected) for language models. Even at the 95th percentile the corrected
values for vision and reinforcement learning stay below 1 ([0.70](numbers.md#dyn-r-cv-hi-corrected)
and [0.90](numbers.md#dyn-r-rl-hi-corrected)); the corrected language-model interval runs from
[0.36](numbers.md#dyn-r-lm-lo-corrected) to [1.07](numbers.md#dyn-r-lm-hi-corrected). These
corrections divide r by the bottleneck factor, so they leave compute's own growth out: they are the
special case in which research compute grew at the same rate as the labour proxy. Counting compute's
historical growth, E9 puts the language-model gain at fixed compute at
[0.25](numbers.md#e9-lm-k-fixed) at a compute share of [0.67](numbers.md#dyn-research-compute-share)
([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile), above 1 only for shares below about
[0.26](numbers.md#e9-lm-share-crit); none of E9's data identifies the share. Whitfill and Wu
estimate the elasticity of substitution between research compute and labour at the frontier at
[-0.10](numbers.md#dyn-sigma-frontier-spec) (complements), in which case effective research effort
"is bounded"; their other specification gives [2.58](numbers.md#dyn-sigma-compute-spec)
(substitutes), from only four firm clusters, and they call the results "divergent"
[@whitfill2025bottlenecks]. Training compute explains [80%](numbers.md#dyn-frontier-explained-lo) to
[90%](numbers.md#dyn-frontier-explained-hi) of frontier performance differences among models
released from 2022 to 2025 [@mertens2026secretsauce], and
[60%](numbers.md#dyn-algo-compute-share-lo) to [95%](numbers.md#dyn-algo-compute-share-hi) of
language-model gains from 2012 to 2023 came from compute [@ho2024algorithmic].

Measured AI contributions to frontier-relevant research are still shallow. Of
[77](numbers.md#dyn-nanogpt-records) speedrun records set from May 2024 to March 2026, which cut
training time from [45 minutes](numbers.md#dyn-nanogpt-start-min) to
[1.43 minutes](numbers.md#dyn-nanogpt-end-min), only [4](numbers.md#dyn-nanogpt-ai-records)
([5%](numbers.md#dyn-nanogpt-ai-share)) credit an AI agent, each with a human, and all are shallow
to moderate; "none reached the deep or breakthrough end of the scale" [@shetty2026metrnanogpt].
Shallow and moderate contributions drove [21](numbers.md#dyn-nanogpt-shallow-moderate) of the
[31](numbers.md#dyn-nanogpt-speedup)-fold speedup, leaving about
[1.5](numbers.md#dyn-nanogpt-deep-factor) for deep ones, and invented ideas gave
[1.6](numbers.md#dyn-nanogpt-invented) against [3.0](numbers.md#dyn-nanogpt-adapted) for adapted and
[6.7](numbers.md#dyn-nanogpt-imported) for imported ones [@shetty2026metrnanogpt]. METR's
expenditure horizon for agents is at most [3,300 USD](numbers.md#dyn-agent-exp-horizon-hi), against
roughly [2,500 USD](numbers.md#dyn-human-cost-per-pct) of human labour per 1% speedup
[@metr2026expenditure]: the best agent matches what a human buys for about a
[1.3%](numbers.md#dyn-agent-equivalent-gain) speedup. On RE-Bench, agents scored
[4](numbers.md#dyn-rebench-agent-2h) times humans at a two-hour budget but humans reached
[2](numbers.md#dyn-rebench-human-32h) times the top agent at 32 hours [@wijk2024rebench]: agents
have steeper early and flatter late returns. AlphaEvolve's [23%](numbers.md#dyn-alphaevolve-kernel)
kernel speedup cut Gemini's training time by [1%](numbers.md#dyn-alphaevolve-gemini-cut) (vendor
figures) [@novikov2025alphaevolve]. In one study, most end-to-end autonomous research attempts
failed in implementation or evaluation [@trehan2026scientists], and reasoning models "struggle to
reimplement already-known innovations" [@zhao2025speedrun].

Cunningham et al. put the self-sustaining threshold at a gain in research productivity of
[15%](numbers.md#dyn-loop-threshold-eps-rc) per ECI point, from a return to R&D of
[1.0](numbers.md#dyn-cunningham-return) (algorithmic efficiency taken to grow
[3](numbers.md#dyn-algo-efficiency-growth)-fold a year) and an elasticity of capability to compute
of [6.5](numbers.md#dyn-cunningham-eps-ca). The next figure is not their estimate. Taking a reported
[4](numbers.md#dyn-cunningham-uplift-reported)-fold uplift at face value, which they call "very
likely to be an overestimate", would imply [9%](numbers.md#dyn-cunningham-eps-rc-illustration),
below the threshold [@cunningham2026rsi]. In our arithmetic that upper-end illustration puts the
core condition at [0.58](numbers.md#dyn-loop-gain-illustration), against 1. Self-reported uplift is
weak evidence in any case: in METR's 2025 trial, AI made experienced developers
[19%](numbers.md#dyn-rct-2025) slower (CI [2%](numbers.md#dyn-rct-2025-lo) to
[39%](numbers.md#dyn-rct-2025-hi)) while they believed it made them faster [@becker2025rct]; the
2026 follow-up found a change of [-18%](numbers.md#dyn-rct-2026-returning) in task time for
returning developers, which METR calls "only very weak evidence" because developers now decline to
work without AI [@metr2026uplift].

Finally, by Burtsev's point, METR's acceleration is not by itself evidence that K_S exceeds 1. The
inputs grew at the same time. Cunningham et al. quote an OpenAI post reporting a steep rise in the
share of research compute devoted to internal coding inference; the survey did not open that post,
so we do not rely on its figure [@cunningham2026rsi].

**Open.** Whether frontier experiment compute and research labour are complements, which decides
whether a compute cap bounds the software loop. Barnett finds about
[50%](numbers.md#dyn-innovations-under-cap) of the pretraining innovations he catalogued would have
been feasible under very stringent compute caps, and concludes that caps alone are unlikely to slow
algorithmic progress dramatically [@barnett2025innovation]; read with Gundlach et al., the
innovations that pay most may be the ones whose value only shows at scale [@gundlach2025origin].
Whether small-scale returns transfer to the frontier. Whether the measured acceleration at one lab
reflects a gain above 1 or a one-time jump in inputs.

### What the survey changed

The memo's belief about D2 was: "the condition is prior work (returns to software research above 1);
a runnable estimator with a confidence-bound trigger may be new". The survey takes more away. The
name "loop gain", the threshold at 1, a calibration and the claim that tracking it "is arguably the
most important empirical exercise" are Cunningham et al.'s [@cunningham2026rsi]. The reproduction
number and operational closure are Burtsev's [@burtsev2026criticality]. The criticality metaphor,
including "prompt critical" and "delayed neutrons", is Yudkowsky's [@yudkowsky2013iem], and the
intelligence explosion itself is Good's [@good1965speculations]. Eth and Davidson already propose
"ongoing measurement of software progress, disclosed to trusted 3rd parties" with a threshold set as
a multiple of the recent pace [@eth2025sie]. Rate triggers are in force: OpenAI's Critical level is
a generational improvement in a [5](numbers.md#dyn-openai-critical-speedup)th of 2024's wall-clock
time [@openai2025preparedness], and Anthropic's is [2](numbers.md#dyn-anthropic-rate-multiple) times
the rate of aggregate progress, a threshold that "has proven difficult to operationalize"
[@anthropic2026rsp]. Chan et al. propose metrics of AI R&D automation without a trigger
[@chan2026measuring], and a survey of the 2024 to 2026 literature calls governance-grade measurement
of self-improvement the field's "most underpopulated niche" [@chen2026rsisurvey].

The memo's own definition of D2 does not survive as written: "With the human-controlled inputs
(compute, data) held fixed and the AI doing the research, g is the ratio of the capability gained in
round n+1 to the capability gained in round n." A staged experiment can hold compute fixed; real
development does not, so field measurements must divide out input growth. And capability gained on a
bounded scale shrinks whatever the feedback. The restatement above fixes both. Revised label: prior
work for the loop and its condition; extends prior work, narrowly, for the estimator. The independent
search found the binding rule in epidemic control, which acts on the upper bound of a reproduction
number [@blumberg2020supercritical], and a staged, fixed-budget test of an AI research loop with
held-out scoring [@srikanth2026aide2]. What remains is the exact round identity as the estimator and
the budget ladder, a measurement design whose decision power is unshown. Its use as a binding trigger
is cut: at the only noise level calibrated to data, E4's final simulation found the rule on K fires
about as often below 1 as above
([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)). The
memo's rank 1 for self-improvement survives as "the loop closest to closing in its labour input",
and weakens as "the route around a compute cap".

### What it means for the protocol

A candidate, not a finding:

- **Limit the input that can be counted.** Research compute (experiment compute plus research
  inference) is visible to chip accounting; AI research labour is not. If frontier experiments and
  labour are complements, a cap on research compute bounds effective research however good the AI
  researchers become. If they are substitutes, the cap leaks. The protocol should measure which, not
  assume it.
- **Measure the gain, with its bound; restrict the closed loop by the prior-work rule.** K_S is a
  measurement, not a trigger. It is estimated per development cycle from mandatory declarations
  (algorithmic efficiency at fixed compute, spend by input, the AI share of advances) and from staged
  runs. The trigger once proposed here, restricting while the upper confidence bound exceeds a margin
  below 1, is cut on current evidence. The width of the interval is the problem. Under the published
  compute correction the language-model median is [0.63](numbers.md#dyn-r-lm-corrected) and the 95th
  percentile [1.07](numbers.md#dyn-r-lm-hi-corrected), so an upper-bound rule would fire on
  historical estimates and a median rule never would; counting compute's growth, E9 gives
  [0.25](numbers.md#e9-lm-k-fixed) and [0.42](numbers.md#e9-lm-k-fixed-hi) at the same share, and
  neither would. At the only noise level calibrated to data, E4's final simulation ran the rule on K
  with a placeholder margin of [0.90](numbers.md#e4-gstar). On a loop at the corrected median of r it
  fired in [88%](numbers.md#e4-k-fa-n5) of runs after 5 rounds at each of three budgets and
  [80%](numbers.md#e4-k-fa-nmax) after 50; on a loop at the corrected 95th percentile it missed
  [10%](numbers.md#e4-k-late-cal). It fired only [2%](numbers.md#e4-k-fire-gap-n5) more often on the
  higher loop, and the rule on r alone [3%](numbers.md#e4-fire-gap-n5) more, both within Monte Carlo
  error, so it cannot decide
  ([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)).
  It returns only if staged runs at two scales (E4(b)) show real rounds tight enough to separate the
  two. Until then closed-loop training research at frontier scale is restricted outright, the
  prior-work rule [@miotti2025narrowpath], which binds only the loops a developer declares
  ([C4.8](verification/l4-red-team.md#c4)), and E4(b) and E9 go on narrowing the interval.
- **Make verification mandatory, compute included.** A developer withdrew compute verification
  midway through the one independent assessment of AI R&D acceleration we found.
- **Cost to useful AI:** low to moderate. AI help with coding and research in general stays allowed.
  The limit applies to frontier-scale research compute and to closed-loop training research at
  frontier scale.

### What would test it

- **E4(a), historical.** Fit per-record gains on the speedrun series, separating systems from
  algorithmic changes and using contributor counts as the input, with bootstrap intervals. Test
  whether the record's shape is consistent with K below 1 at fixed hardware. Done. E4 recomputed the
  pace with re-timings removed: an annualised [59](numbers.md#e4-pace-first8) in the first eight
  months, [1.59](numbers.md#e4-pace-2025) across 2025 and [4.9](numbers.md#e4-pace-2026) in 2026,
  against [6.6](numbers.md#e4-pace-whole) over the whole record. The history cannot place r. Across
  months the stock and the log of the research input correlate at
  [0.98](numbers.md#e4-sr-collinearity), and placebo inputs put in place of contributors return an r
  of their own: [0.59](numbers.md#e4-sr-placebo-r-records) for the count of recent records and
  [1.03](numbers.md#e4-sr-placebo-r-time) for time itself. An r fitted to the record reflects the
  shared trends, not the input, so the speedrun's r is withdrawn as not identified
  ([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)).
- **E4(c), simulated, done.** The estimator's coverage and the trigger's error rates, in the common
  form, at noise calibrated to the speedrun's monthly spread. The interval under-covers: after 5
  rounds at each of three budgets the nominal 90% interval on r held the truth in
  [82%](numbers.md#e4-cov-n5) of runs for the first-order level form and
  [77%](numbers.md#e4-cov-n5-xml) for maximum likelihood on the exact identity. Every estimator leans
  subcritical, the unsafe side: on data from the exact round law the median estimate was
  [0.82](numbers.md#e4-level1-bias) times the true r for the level form,
  [0.77](numbers.md#e4-xml-bias) for maximum likelihood and [0.47](numbers.md#e4-diff-bias) for the
  first-order difference regression. Two held-out sets do not remedy it: where the noise is error in
  measuring each round, they turn [0.57](numbers.md#e4-diff-bias-meas1) times the true r into
  [8.11](numbers.md#e4-diff-bias-meas2) times it, and where it is real variation in the round's gain,
  a second set measures that variation identically. A sandbagger that withholds gain in a pattern
  silences the upper bound by withholding [16%](numbers.md#e4-hide-silence-fav) of its gain in
  favourable rounds and [42%](numbers.md#e4-hide-silence-cal) at the calibrated noise. The trigger's
  rates are above; together they cut it.
- **E4(b), staged.** An agent fine-tuned on the task improves a small model's recipe over n rounds
  at fixed training compute C. The researcher is a fixed agent, so the loop is open, and the run
  measures r for AI research labour on that target, not closure. Round k's gain is Delta_k in log
  effective compute. In the common form with a fixed budget per round, ln(Delta_(k+1) / Delta_k) =
  -beta * Delta_k holds to first order only; exactly, ln[(e^(beta Delta_(k+1)) - 1) /
  (e^(beta Delta_k) - 1)] = -beta * Delta_k ([Part III, Lemma 4.1](05-formal.md#c4-the-loop-gain-estimator)),
  which costs nothing since beta is fitted anyway. The slope of that regression estimates beta; repeating at 1, 2 and 4 times the
  agent budget per round estimates lambda from how the gain scales. Report r = lambda / beta with a
  bootstrap 90% interval, and repeat at two model scales to test transfer. The test settles the side
  of 1 only if both bounds fall on the same side. Closure e (Burtsev's chi) has to come from
  declarations of how much of the pipeline AI runs. Not yet run, it is also the only measurement of
  a real round's noise, which decides whether a trigger on the gain can return.
- **E9, done.** It refitted r across domains with compute's share of research input free. No data
  identifies the share: for Stockfish, where both inputs are logged, every share from
  [0.00](numbers.md#e9-chess-share-lo) to [1.00](numbers.md#e9-chess-share-hi) fits within the 95%
  region. Counting compute's historical growth at a share of
  [0.67](numbers.md#dyn-research-compute-share), the gain at fixed compute is
  [0.25](numbers.md#e9-lm-k-fixed) for language models ([0.42](numbers.md#e9-lm-k-fixed-hi) at the
  95th percentile) and [0.28](numbers.md#e9-cv-k-fixed) for computer vision, above 1 only for shares
  below about [0.26](numbers.md#e9-lm-share-crit) and [0.21](numbers.md#e9-cv-share-crit). Stockfish's
  r, [0.73](numbers.md#e9-chess-r), rests on its two trends: a smooth placebo input growing at the
  same rate gives [0.79](numbers.md#e9-chess-placebo-r). So which side of 1 the software loop sits
  on turns on a share no data yet measures.

## Y1b. The hardware loop

### Definition

The stock H is compute per dollar (operations a second per dollar of hardware), with compute per
joule as its energy branch. The input is hardware research and the plants that realise it: chip
design, process technology, packaging and fabrication. The boundary is global, since leading-edge
chips come from a handful of firms. The loop: AI designs better chips or processes, which raise H,
which supplies more AI.

```
(1/H) dH/dt = theta_H * H^(-beta_H) * E_H^lambda_H,        r_H = lambda_H / beta_H
K_H = e_H * r_H        (e_H: how far AI supplies hardware research, and how that scales with H)
```

This is Davidson, Hadshar and MacAskill's "chip technology" loop [@davidson2025three].

### Measurement

H is measured from public specifications and sales of chips; research input from R&D spending and
headcount, as in Bloom et al. [@bloom2020ideas]. The closure e_H, the share of hardware research
that AI does, was not measured in any source we found. H is hard to fake because chips are made in
few plants; AI's role in design is internal to firms and easy to hide.

### Evidence for and against

**For a strong loop.** The hardware loop has the highest returns of any estimate we surveyed.
Moore's Law research has the smallest beta in Bloom et al., [0.2](numbers.md#dyn-bloom-beta-moore)
[@bloom2020ideas], so with lambda = 1 its r is [5](numbers.md#dyn-r-moore). Eth and Davidson give
about [5](numbers.md#dyn-r-gpu) for GPUs from 2006 to 2022 and about
[7](numbers.md#dyn-r-hardware-hist) historically [@eth2025sie]. If AI supplied hardware research and
that supply scaled with H, the loop alone would be far above 1. Davidson, Hadshar and MacAskill put
the chance that the chip technology loop alone sustains acceleration at
[65%](numbers.md#dyn-ie-p-chiptech) [@davidson2025three]. Yudkowsky notes that added hardware "could
send the system from k < 1 to k > 1" [@yudkowsky2013iem].

**Against.** The loop is slow and has little room. New chip technology takes many months and new
fabs take years [@davidson2025three]; a greenfield fab took
[682 days](numbers.md#dyn-fab-build-days) ([1.9 years](numbers.md#dyn-fab-build-years)) on average
from construction start to production, before permits [@verwey2021permits]. Room to grow in the
current paradigm is about [2](numbers.md#dyn-ie-chiptech-oom) orders of magnitude, or about
[6](numbers.md#dyn-ie-chiptech-landauer-oom) up to Landauer's limit [@davidson2025three]. The first
figure agrees with Ho, Erdil and Besiroglu's estimate that irreversible CMOS has a
[207](numbers.md#dyn-cmos-headroom)-fold efficiency headroom over an H100 at 50% chance
([2.3](numbers.md#dyn-cmos-headroom-oom) orders of magnitude) [@ho2023]; at the
[1.40](numbers.md#dyn-gpu-eff-growth)-fold annual efficiency growth measured for GPUs [@you2025],
that ceiling is about [16 years](numbers.md#dyn-cmos-years) away (our arithmetic). AI's measured
part in the loop is small: AlphaEvolve's scheduling heuristic recovers
[0.7%](numbers.md#dyn-alphaevolve-fleet) of Google's fleet-wide compute (a vendor figure), an
efficiency gain on existing hardware rather than a better chip [@novikov2025alphaevolve]. AI chip
performance per dollar has grown [1.49](numbers.md#dyn-chip-price-perf-growth)-fold a year since
2023 [@epoch2026trends], with no measured AI contribution. And the loop has so far run on growing
human input: research productivity in chips fell [6.8%](numbers.md#dyn-bloom-rp-decline-moore) a
year, and the researchers needed grew [18](numbers.md#dyn-bloom-moore-researchers)-fold
[@bloom2020ideas].

### What the survey changed

The memo listed this loop; Davidson, Hadshar and MacAskill had already defined it, with its lags and
headroom [@davidson2025three]. It is prior work. What the survey adds is its shape: the highest
returns, the slowest clock, the narrowest headroom, and a path through the most concentrated supply
chain of any input (the organisational chapter's chokepoints).

### What it means for the protocol

Do not limit chip technology; count it. Every gain in H must be fabricated, and fabrication is
already the protocol's backbone (lithography tools, leading-edge fabs, high-bandwidth memory).
Thresholds stated in operations fall in cost as H rises, so registries count in H100-equivalents and
thresholds are dynamic, as Egan and Heim propose for cloud oversight [@egan2023kyc]. Cost to useful
AI: none from monitoring. Weak point: efficiency gains at the boundary of software and hardware
(kernels, scheduling, compilers) never pass through a fab. They belong in the software loop's ledger
and must be declared there.

### What would test it

E9 recomputed Bloom et al.'s beta for Moore's Law from their files, [0.20](numbers.md#e9-moore-beta),
an r of [5.1](numbers.md#e9-moore-r) at lambda = 1, from [2.5](numbers.md#e9-moore-r-min) to
[7.3](numbers.md#e9-moore-r-max) across their six R&D series. The closure e_H has no data source in
our survey, and a measurement of AI's share of chip design advances is an open item, not a planned
experiment. E11 shows what that gap costs. With research closure gated, the economic gain at zero
and the software loop at its corrected 95th percentile, the coupled certificate's rho(U)
([Y3](#y3-coupling)) stays at or below 1 only if AI's share of hardware research is below
[0.064](numbers.md#e11-ah-max-gated); with the compute stock capped, it needs no bound on that
share. Counting chips, not limiting chip technology, is what lets the certificate set this loop
aside.

## Y1c. The economic loop

### Definition

The stock K is the compute capital a party controls, in dollars of AI hardware or in
H100-equivalents. The loop: capability earns revenue, revenue is reinvested in compute, compute
raises capability. It includes Davidson, Hadshar and MacAskill's "chip production" loop when the
capital buys fabs [@davidson2025three].

```
dK/dt = s * Y - delta * K,        Y = y0 * K^eps,        eps = e_YA * e_AC * e_CK
```

Y is revenue from AI, s the reinvested share, delta depreciation. eps, the elasticity of AI revenue
to AI capital, composes revenue on capability, capability on compute and compute on capital. If eps
> 1 the capital stock reaches infinity in finite time; if eps = 1 it grows exponentially (the AK
case); if eps < 1 it converges to a steady state. The regime depends only on eps, the loop's own
gain; s and delta set the speed and the steady state.

### Measurement

Capital is among the most visible inputs in the system. Capital spending of a few firms is public
every quarter, chip sales are estimated by vendor (Epoch's dataset), and five US hyperscalers own at
least [70%](numbers.md#dyn-hyperscaler-compute-share) of global AI compute [@you2026chipowners].
Capability can be read from the ECI. Revenue attributable to AI is not in our survey, so eps was not
measured by any source we found. A state or a private actor can hide capital more easily than a
listed firm.

### Evidence for and against

**For a fast loop.** The capital input is growing fast. The four largest companies planned about
[650 billion USD](numbers.md#dyn-capex-2026-feb) of capital spending for 2026, up about
[60%](numbers.md#dyn-capex-growth) [@day2026capex]; by May the big hyperscalers' plans topped
[700 billion USD](numbers.md#dyn-capex-2026-may) [@ehsan2026capex] (company guidance). AI compute
sold rose from [5.1 million H100e](numbers.md#dyn-compute-sold-2024) in 2024 to
[13.6 million H100e](numbers.md#dyn-compute-sold-2025) in 2025, a factor of
[2.7](numbers.md#dyn-compute-sold-growth) (the survey's sum of Epoch's quarterly medians)
[@epoch2026chipsales]. Frontier training compute grew [5.3](numbers.md#dyn-frontier-compute-growth)
times a year from 2010 to 2024 [@sevilla2024computegrowth] and the cost of the largest runs
[2.4](numbers.md#dyn-frontier-cost-growth) times a year [@cottier2024rising]. In theory, AI labour
that scales with capital restores increasing returns to scale [@erdil2023explosive]; Davidson et
al.'s model reaches a singularity within about [6](numbers.md#dyn-nber-singularity-years) years with
software research fully automated and only [5%](numbers.md#dyn-nber-other-automation) automation
elsewhere [@davidson2026feedback]; and Cunningham et al. add indirect and direct economic channels
to the core loop [@cunningham2026rsi].

**Against.** Growth may be "constrained not by what we are good at but rather by what is essential
and yet hard to improve" [@aghion2017ai]. Erdil and Besiroglu judge high confidence in explosive
growth "currently unwarranted" [@erdil2023explosive], and Trammell and Korinek argue that automating
R&D would speed the transformation but might not bring it about on its own (our paraphrase of their
abstract) [@trammell2023growth]. Capital converts into compute slowly: the fastest recent build
reached 1 GW of facility power in [11.6 months](numbers.md#dyn-dc-1gw-months-fastest), and recent
sites take [1](numbers.md#dyn-dc-1gw-years-lo) to [3.6 years](numbers.md#dyn-dc-1gw-years-hi)
[@somala2025buildtimes].

**Steelman against the memo.** What we cannot tell is whether today's capital growth is paid for by
AI's earnings (a closed loop) or by outside capital (an open one). The survey found no measurement
of that share. If the loop is open, cutting it does not touch AI's own feedback; what matters is
that money converts into compute only through a gate the protocol holds. Restricting resources may
even backfire in some race regimes [@buenodemesquita2026agirace].

### What the survey changed

The memo pictured AI earning money that buys its own compute. That loop is formalised in prior
growth theory [@erdil2023explosive; @trammell2023growth; @davidson2026feedback], and its gain is
unmeasured in everything we surveyed. The measured flow is investment by a handful of firms, one of
the most visible inputs there is.

### What it means for the protocol

Cut the edge from money to compute, not revenue itself: registered chips under expiring licences,
and compute purchases above a threshold only for a declared use, through cloud know-your-customer
rules [@egan2023kyc; @heim2024cloud]. Cost to useful AI: low. Weak points: diversion (an estimated
[0.66 million H100e](numbers.md#dyn-smuggled-h100e) were smuggled into China through 2025
[@juniewicz2026smuggling]), and a state that funds compute from taxes, outside any revenue loop.

### What would test it

A new input for E11: eps, fitted by firm from public filings (AI revenue against compute capital and
ECI over time, with an interval). The revenue data are not yet sourced, so E11 ran with eps as a
stated range. With research closure gated, the software loop at its corrected 95th percentile and
every other unmeasured entry at zero, rho(U) stays at or below 1 only if the economic gain is
below [0.32](numbers.md#e11-eta-max-gated), and the cycle from compute to software and back through
revenue carries [0.81](numbers.md#e11-sens-cycle) of rho(U) at that point. An unmeasured elasticity
thus decides the certificate, and the test still asks whether eps < 1 holds at 90% confidence.

## Y1d. The experiential loop

### Definition

The stock A is a deployed model's capability on its deployment tasks, in log compute-equivalent
units. The input is experience gathered by copies in use (N copies at interaction rate v) and turned
into weight updates. The loop: a better model is deployed more widely, gathers more experience, and
improves. The boundary is one model lineage across its deployment.

```
(1/A) dA/dt = theta_X * A^(-beta_X) * (N v)^lambda_X - f,     N proportional to A^e_X
K_X = lambda_X * e_X / beta_X
```

f is the rate of forgetting, which acts as a brake.

### Measurement

Update compute (operations spent on updates after deployment), weight differences between attested
checkpoints, and re-evaluation scores over time. Whoever runs the hardware can measure them. They
can be hidden where weights are held locally, and adaptation through context or retrieval changes no
weights at all.

### Evidence for and against

**For.** Weight self-editing works in small models. SEAL raised knowledge incorporation in a 7B
model from [33.5%](numbers.md#dyn-seal-squad-base) to [47.0%](numbers.md#dyn-seal-squad), a gain of
[13.5 points](numbers.md#dyn-seal-gain-points), beating training on GPT-4.1 synthetic data
([46.3%](numbers.md#dyn-seal-squad-gpt41)), and each self-edit takes
[30 s](numbers.md#dyn-seal-edit-s-lo) to [45 s](numbers.md#dyn-seal-edit-s-hi) to evaluate
[@zweiger2025seal]: the fastest clock of the five loops. Test-time training brought an 8B model to
[53.0%](numbers.md#dyn-ttt-arc) on ARC [@akyurek2024ttt]. The capacity to self-improve is governed
by the generation-verification gap, which grows with pretraining compute [@song2024gap], so this
loop's gain rises with the compute loop's output.

**Against.** SEAL's own limitation: "performance on earlier tasks gradually declines as the number
of edits increases" [@zweiger2025seal]. Forgetting is general in 1B to 7B models and worsens with
size in that range [@luo2023forgetting]. "Continual learning is not one capability": prompt-based
methods adapt fast but degrade, distillation retains but struggles to update facts, and online
reinforcement learning adapts best but is sensitive to noisy rewards [@harrington2026continual]. We
found no measurement of K_X.

**Steelman against the memo.** The memo proposed accounting for weight updates and re-evaluating. If
the hazardous form of continual learning runs through context and retrieval rather than weights,
weight accounting sees nothing. And reinforcement learning can put most of its compute into rollouts
on unregistered hardware: INTELLECT-2 ran rollouts on a permissionless swarm, though its training
nodes were central [@primeintellect2025intellect2].

### What the survey changed

The memo's view (a deployed fleet as a hidden training run, pre-deployment evaluations going stale,
accounting rather than a ban) survives. The survey adds that the hazard depends on the mechanism, so
a single accounting rule does not cover it, and that classifying loops by how closed they are is in
use [@chen2026rsisurvey]. A gain estimate for this loop was not found in our search.

### What it means for the protocol

Count update compute toward training compute, attest weight differences at checkpoints, and
re-evaluate when measured capability drifts. Treat context-based adaptation as part of the deployed
system that is evaluated, with its memory and scaffolding included in the elicitation (D5), since no
weight accounting sees it. Cost to useful AI: moderate, since continual learning is valuable. Weak
points: locally held weights and distributed reinforcement learning.

### What would test it

E7: on a small open model, run SEAL-style self-edits for n rounds, measure the capability gained per
update operation and the forgetting on held-out tasks, estimate K_X with an interval, and compare
the update compute needed to cross a capability threshold with a training-compute threshold.

## Y1e. The acquisitive loop

### Definition

The stock N is the number of running copies of a model outside its operator's control, with the
compute and money they hold. The loop: copies acquire resources, which fund more copies and more
compute, which acquire more.

```
dN/dt = (b - d) * N,        b = b0 * p_money * p_KYC * p_compute * p_weights * p_persist
R_Q = b / d                 (copies each copy starts before it is removed)
```

The loop is supercritical when R_Q > 1; growth is then exponential until accessible compute
saturates it, and faster if acquired resources raise b. The reproduction number is the standard
branching-process threshold. Writing b as a product over stages is our framing of RepliBench's four
domains: obtaining resources, exfiltrating weights, replicating onto compute and persisting
[@black2025replibench].

### Measurement

Stage success rates come from replication evaluations in sandboxes; the removal rate d from
operators' detection. Evaluators can measure the first; real-world rates are unknown.

### Evidence for and against

**For.** The components are improving fast. The best model of early 2023 succeeded less than
[5%](numbers.md#dyn-aisi-rep-2023) of the time across [11](numbers.md#dyn-aisi-rep-evals) of UK
AISI's RepliBench evaluations; by summer 2025 two frontier models exceeded
[60%](numbers.md#dyn-aisi-rep-2025) [@aisi2025trends]. Claude 3.7 Sonnet scored above 50% pass@10 on
[15](numbers.md#dyn-replibench-best-families) of [20](numbers.md#dyn-replibench-families) families,
and on [9](numbers.md#dyn-replibench-hard-families) on the hardest variants [@black2025replibench].
In 2023, evaluations could not rule out autonomous replication after an effective compute scale-up
of about [100](numbers.md#dyn-ara-scaleup) times without intermediate evaluations
[@kinniment2023ara].

**Against.** The evaluations are "simplified versions", and models are "currently unlikely to
succeed in real-world conditions" [@aisi2025trends]. Models struggle with know-your-customer checks
and robust persistent deployment, and "do not currently pose a credible threat of self-replication"
[@black2025replibench]. The binding stages are human-held gates, which is evidence for the memo's
D6.

**Steelman against the memo's "cheap to forbid".** Open-weight models with local weights need no
know-your-customer gate. Llama3.1-70B-Instruct and Qwen2.5-72B-Instruct created a live, separate
copy of themselves in [50%](numbers.md#dyn-fudan-llama) and [90%](numbers.md#dyn-fudan-qwen) of
trials [@pan2024selfrep], and [11](numbers.md#dyn-fudan-capable) of
[32](numbers.md#dyn-fudan-evaluated) systems ([34%](numbers.md#dyn-fudan-capable-share)) were
reported capable, including a 14B model that runs on personal computers [@pan2025selfrep]. We read
only these abstracts, and the chain they test is shorter than RepliBench's, which includes acquiring
resources and passing identity checks.

### What the survey changed

The memo ranked this loop third as cheap to forbid. That holds where the gates hold
(identity-checked compute and payment) and fails for open weights on local hardware, where p_KYC is
1 by construction. Self-replicating machines in growth theory are prior work [@trammell2023growth];
RepliBench is the measurement; the reproduction-number framing is standard.

### What it means for the protocol

Hold the gates: compute know-your-customer rules [@egan2023kyc], payment identity, no deployment of
models whose replication capability exceeds a threshold, and evaluations at declared training
checkpoints rather than only at the end [@kinniment2023ara]. For open weights, the levers are the
release decision (no release above the line) and compute. Cost to useful AI: very low. Weak point:
"structuring", splitting one workload across providers as money launderers split transactions
[@heim2024cloud; @krys2025distributed].

### What would test it

A new experiment, the replication reproduction number: in an isolated sandbox with no real network or payment access,
measure per-stage success of small open models on public replication tasks, compute R_Q with each
gate open and closed, and report which stage dominates the product.

## Y2. Runaway versus saturation

### Definition

Each loop's regime is set by its own gain K_i in the common form: saturation of the rate when K_i <
1, runaway when K_i > 1. Its timescale is its cycle time tau_i. Once above 1, Burtsev's limit for
the amplification rate is ln(R) / tau [@burtsev2026criticality], so danger depends on both gain and
clock. The fastest loop is the one with the largest ln(K) / tau, or, while all are below 1, the one
approaching 1 fastest.

### Measurement

The table gathers each loop's best evidence. Every cell is a measurement, a vendor claim or another
author's model parameter, as marked in the sections above.

| Loop | Own gain | Clock | Room to grow | Gate |
|---|---|---|---|---|
| Software | r [1.26](numbers.md#dyn-r-cv), [1.20](numbers.md#dyn-r-rl), [1.89](numbers.md#dyn-r-lm) historical; [0.42](numbers.md#dyn-r-cv-corrected), [0.40](numbers.md#dyn-r-rl-corrected), [0.63](numbers.md#dyn-r-lm-corrected) after the compute correction, which leaves compute's growth out ([0.25](numbers.md#e9-lm-k-fixed) for language models with it counted, E9) | about [3](numbers.md#dyn-ie-lag-model-months) months a model; tau [0.5 years](numbers.md#dyn-burtsev-delay) assumed | about [12](numbers.md#dyn-ie-software-oom) orders of magnitude ([11](numbers.md#dyn-sie-distance-oom) in Davidson and Houlden) | research compute |
| Hardware | r about [5](numbers.md#dyn-r-gpu) to [7](numbers.md#dyn-r-hardware-hist); closure unmeasured | fabs [1.9 years](numbers.md#dyn-fab-build-years) | about [2](numbers.md#dyn-ie-chiptech-oom) orders (CMOS) | fabs, lithography |
| Economic | eps unmeasured | 1 GW in [11.6 months](numbers.md#dyn-dc-1gw-months-fastest) at fastest | about [5](numbers.md#dyn-ie-chipprod-oom) orders (chip production) | chip licences, cloud rules |
| Experiential | unmeasured; forgetting damps it | [30 s](numbers.md#dyn-seal-edit-s-lo) to [45 s](numbers.md#dyn-seal-edit-s-hi) a self-edit | unknown | update compute, attestation |
| Acquisitive | R_Q unmeasured; components [5%](numbers.md#dyn-aisi-rep-2023) to [60%](numbers.md#dyn-aisi-rep-2025) | not measured | accessible compute | identity checks, persistence |

### Evidence for and against

**For runaway.** The language-model estimate of r; Davidson and Houlden's model outputs
[@davidson2025sie]; Davidson et al.'s proof that loops jointly explode under weaker conditions than
any one alone [@davidson2026feedback]; feedback loops that "appear to be strengthening"
[@cunningham2026rsi]; and, if it happens, a maximum speed of about
[100](numbers.md#dyn-ie-max-speed) times recent rates, with effective compute doubling roughly daily
[@davidson2025three]. The AI 2027 supplement simulates [0.3 years](numbers.md#dyn-ai2027-sc-to-sar)
from a superhuman coder to a superhuman AI researcher, but says its model "relies substantially on
intuitive judgment" [@kokotajlo2025takeoff].

**For saturation.** Each mechanism is documented in prior work:

- *Diminishing returns are the rule.* Research productivity falls about
  [5.3%](numbers.md#dyn-bloom-rp-decline) a year on average across Bloom et al.'s cases, and the
  aggregate economy's beta of [3.1](numbers.md#dyn-bloom-beta-aggregate) gives r of
  [0.32](numbers.md#dyn-r-aggregate) [@bloom2020ideas]; Epoch's replication gives
  [0.25](numbers.md#dyn-r-us-economy), and computer chess [0.83](numbers.md#dyn-r-chess) (standard
  error [0.15](numbers.md#dyn-r-chess-se)), "just shy of the threshold of 1"
  [@besiroglu2024returns]. Eth and Davidson's best guess for software with hardware constant is
  [0.5](numbers.md#dyn-eth-r-consthw-lo) to [2](numbers.md#dyn-eth-r-consthw-hi) [@eth2025sie].
- *Compute is a complement.* The correction above, and Whitfill and Wu's frontier specification
  [@ho2025experiments; @whitfill2025bottlenecks].
- *Parallel work does not add up.* Effective research is capped by the scarcer of the raw inputs and
  the "parallelization technology" that divides and integrates their work [@trammell2026parallel];
  Davidson and Houlden's median lambda for parallel labour is [0.6](numbers.md#dyn-sie-lambda)
  [@davidson2025sie].
- *Bottlenecks.* What is essential and hard to improve sets the pace [@aghion2017ai]. Training time
  "would likely delay an SIE rather than prevent it" [@eth2025sie].
- *Finite room.* Every loop has a headroom in the table, and the hardware loop's is narrow.
- *Forgetting and gates.* The experiential loop forgets; the acquisitive loop stops at identity
  checks.

**Autonomy horizons: the clock of closure.** How long a loop can run between human gates depends on
how long AI agents work reliably unattended. A horizon is measured in human time: the time humans
take on the tasks a model completes [@kwa2025horizon], not the time the model takes. The 50% time
horizon doubled every
[129 days](numbers.md#dyn-horizon-doubling) from 2023 on (95% CI
[104 days](numbers.md#dyn-horizon-doubling-lo) to [158 days](numbers.md#dyn-horizon-doubling-hi))
[@metr2026thdata], against [207 days](numbers.md#dyn-horizon-doubling-2019) from 2019 to 2025
[@kwa2025horizon]: in our arithmetic, a factor of [7.1](numbers.md#dyn-horizon-annual) a year (from
[5.0](numbers.md#dyn-horizon-annual-slow) to [11](numbers.md#dyn-horizon-annual-fast) across the
interval) against [3.4](numbers.md#dyn-horizon-annual-2019). The latest state-of-the-art entry has a
50% horizon of [1,045 minutes](numbers.md#dyn-horizon-p50) (about
[17 hours](numbers.md#dyn-horizon-p50-hours)) but an 80% horizon of only
[186 minutes](numbers.md#dyn-horizon-p80) (about [3 hours](numbers.md#dyn-horizon-p80-hours))
[@metr2026thdata]. The ratio, [5.6](numbers.md#dyn-horizon-ratio), is larger than the
[3](numbers.md#dyn-ord-ratio) a constant hazard predicts [@ord2025halflife]: reliability lags more
than that model implies. If both horizons double at the 50% rate, the 80% horizon reaches today's
50% horizon in about [321 days](numbers.md#dyn-reliability-lag-days) (our arithmetic). The long end
is thin: only [5](numbers.md#dyn-horizon-long-baselined) of [31](numbers.md#dyn-horizon-long-tasks)
tasks over eight hours have human baseline times [@metr2026th11]. Superexponential fits to about a
dozen points diverge whatever their parameters [@titotal2025critique]; we fit only exponentials,
with intervals. Under a compute slowdown, one model puts one-month 80% horizons
[7 years](numbers.md#dyn-horizon-compute-delay) later than trend, but it assumes horizon growth
proportional to compute growth, which rules out a software-only singularity by construction
[@whitfill2025horizon].

**Which loop is fastest.** Among loops with measured returns near 1, the software loop has the
fastest clock (months against years). The hardware loop has the strongest returns, the slowest clock
and the narrowest room. The experiential and acquisitive loops have the fastest possible clocks,
unmeasured gains, and gates. So the software loop is the one to watch first, and the acquisitive
loop is the one that would be fastest if its gates opened.

### What the survey changed

All of this is prior work: the condition r > 1 under full automation at constant compute
[@besiroglu2024returns; @eth2025sie], and each saturation mechanism. The memo expected returns in
software to settle the question. They straddle 1, and the compute correction puts the medians below
it. The memo also did not separate gain from clock. Burtsev's delay does, and so does Yudkowsky's
point that slow sensors and manipulators "might act as metaphorical delayed neutrons that prevent
prompt criticality" [@yudkowsky2013iem]. Fermi's pile had k of [1.0006](numbers.md#dyn-cp1-k) in all
but [0.9946](numbers.md#dyn-cp1-k-prompt) on prompt neutrons alone [@yudkowsky2013iem]: it was
supercritical only through the delayed ones, which is the sense of his metaphor.

### What it means for the protocol

The protocol need not prove runaway. Its question is whether, given measured gains and clocks,
amplification would outrun its response. In Burtsev's network scenario (rho
[1.15](numbers.md#dyn-burtsev-network-rho), tau [0.5 years](numbers.md#dyn-burtsev-delay)), a
perturbation grows at [0.28/yr](numbers.md#dyn-burtsev-amp-rate), an e-folding time of
[3.6 years](numbers.md#dyn-burtsev-efold-years), or [1.32](numbers.md#dyn-burtsev-growth-per-year)
times a year (our arithmetic on his scenario, which he does not estimate). A regime that responds
within months would have time in that scenario. A gain well above 1, or a clock of days, would not.
The human-held gates that set the clocks (human review of research, fab construction, identity
checks) are the protocol's delayed neutrons, and it should keep them. Gates count the agent's
completed horizon-length tasks, not hours: an agent that finishes a horizon-length task in minutes
can chain several between gates a horizon apart on the clock
([C11.4](verification/l4-red-team.md#c11)), until its own wall-clock time on such tasks is measured
for each system. The cost to useful AI is the autonomy cost: as horizons double, each counted task
holds more work, and gates set closer than the work an agent does reliably start to bind on useful
work.

### What would test it

E9 has run (Y1a): it fitted returns across domains with the compute share free, and the share, not
the fit, decides the side of 1. E2 has run too. Our refit reproduces METR's 50% doubling time,
[129 days](numbers.md#e2-doubling-p50) ([96 days](numbers.md#e2-doubling-p50-lo) to
[162 days](numbers.md#e2-doubling-p50-hi)), puts the 80% doubling time at
[133 days](numbers.md#e2-doubling-p80) and the median ratio of the two horizons at
[5.3](numbers.md#e2-p50-over-p80), and finds that ratio stable: it changes by a factor of
[1.07](numbers.md#e2-ratio-trend) a year, with an interval from [0.88](numbers.md#e2-ratio-trend-lo)
to [1.26](numbers.md#e2-ratio-trend-hi) that spans 1. What remains open is the agent's own wall-clock
time on horizon-length tasks, which no experiment here measures.

## Y3. Coupling

### Definition

The combined gain is the spectral radius rho(K) of the gain matrix over loops, and over parties,
with K_ij = lambda_i * e_ij / beta_i as in the common form. The system is supercritical when rho(K)
> 1. For two loops with each own gain below 1 this is

```
(1 - K_SS) * (1 - K_HH) < K_SH * K_HS
```

Multiplying out by beta_S * beta_H turns it into net diminishing returns against cross-feeds,
beta_net_S * beta_net_H < phi_S * phi_H, with beta_net_i = beta_i (1 - K_ii), phi_S = lambda_S e_SH
and phi_H = lambda_H e_HS. That is the form of Davidson et al.'s condition [@davidson2026feedback]:
either loop explodes alone when its net diminishing returns turn negative, and otherwise they
explode together when the product of cross-feeds beats the product of net diminishing returns.
Across actors, Burtsev writes K_ij = g_ij / sigma_i and R_net = rho(K), and shows that "Kii < 1 for
every actor is not sufficient for network stability" [@burtsev2026criticality].

Three standard facts about a nonnegative matrix (Perron and Frobenius; Collatz and Wielandt) make
this usable:

1. **Monotone.** Lowering any entry never raises rho(K). Every edge the protocol cuts or weakens can
   only help.
2. **Bounds.** max_i K_ii <= rho(K) <= max_i sum_j K_ij, and for any pair rho(K) >= sqrt(K_ij K_ji).
   For any positive weights w, rho(K) <= max_i (sum_j K_ij w_j) / w_i.
3. **A certificate.** If upper bounds U_ij >= |K_ij| hold jointly with probability at least 1 -
   alpha (for example by a Bonferroni split of alpha over the entries), then by facts 1 and 2, rho(K)
   <= rho(U) <= max_i sum_j U_ij with that probability. Subcriticality can be certified from a bound
   on each edge, each verified on its own, without knowing K exactly. The test is rho(U) itself. The
   largest row sum bounds it from above but is looser, and on this chapter's graph it can never
   issue while compute feeds software (E11, below).

### Measurement

The diagonal comes from Y1. The off-diagonal edges, and what is known about each:

- **Compute to software:** experiment compute and research inference; complements or substitutes
  (above). Self-improvement capacity rises with pretraining compute [@song2024gap].
- **Software to hardware:** AI in chip design; small, vendor-reported [@novikov2025alphaevolve].
- **Software to economic:** revenue's elasticity to capability; unmeasured here.
- **Economic to compute:** capital to chips; capital spending and chip sales, the best measured
  edge.
- **Acquisitive to compute and money:** gated, unmeasured in the field.
- **Across parties:** open-weight models trail closed ones by about
  [4 months](numbers.md#dyn-open-closed-lag) on the ECI [@edwards2026openclosed]; distillation pays
  most when a teacher already exists [@busbridge2025distillation]; compute moves across borders by
  smuggling [@juniewicz2026smuggling].

Most off-diagonal terms are unmeasured. Burtsev states that gain, closure and hardening are "not
presently constrained by direct empirical estimates" [@burtsev2026criticality].

### Evidence for and against

**For coupling.** Davidson et al. prove it [@davidson2026feedback]. Cunningham et al. write the
joint condition as a sum of three channels exceeding 1, with each of the first two below 1 alone
[@cunningham2026rsi]. Davidson, Hadshar and MacAskill say that "we could still see an AI-technology
or full-stack IE" even if the software loop alone is too weak, and put the chance that the chip
production loop alone sustains acceleration at [80%](numbers.md#dyn-ie-p-chipprod)
[@davidson2025three]. In Burtsev's scenario, blocs that are each subcritical reach a network rho of
about [1.15](numbers.md#dyn-burtsev-network-rho) through transfer [@burtsev2026criticality].

**Against, steelmanned.** With the off-diagonals unmeasured, rho(K) is a model output, not an
observable, and a treaty bound on it rests on numbers no one can yet check. Some couplings may be
negative (compute spent on experiments is not spent on training), so the nonnegative matrix is
itself an assumption (our reasoning, not a sourced finding). Part III has since settled the signed
case. With negative couplings, rho(K) > 1 is not the runaway condition: E11 built a signed variant of
this chapter's graph, software competing with revenue for compute, with rho(K) of
[1.25](numbers.md#e11-signed-rho), and it grows only logarithmically. What rules runaway out is
rho(K+) < 1, with K+ the matrix with its negative entries set to zero, and the certificate rho(U) < 1
gives that, since K+ <= U
([Part III, Theorem 6.2](05-formal.md#c6-the-coupled-gain-certificate-and-the-runaway-condition)).
So bounding absolute values keeps the certificate valid, but a signed rho(K) above 1 no longer shows
runaway.

**Our arithmetic on today's numbers.** The software loop's own corrected gain leaves
[0.37](numbers.md#dyn-software-headroom) of headroom below 1 for every cross-feed into software at
the median, and [-0.07](numbers.md#dyn-software-headroom-upper) at the 95th percentile. Since
rho(U) is at least its largest diagonal entry, no certificate can be issued at that confidence with
the software loop fully closed, whatever edges are cut and before any cross-feed is counted; only
holding the loop's own closure below [0.93](numbers.md#formal-software-closure-max) can
([C6](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test)). Both figures rest on the
published correction, which leaves compute's growth out; counting it, E9's 95th percentile,
[0.42](numbers.md#e9-lm-k-fixed-hi), would leave headroom, so the conclusion holds only under that
correction or at a compute share below about [0.26](numbers.md#e9-lm-share-crit). E11 adds that even
under the correction it rests on the assumed compute share: the result flips at a share of
[0.689](numbers.md#e11-epsk-flip), only [0.022](numbers.md#e11-epsk-gap) above the ledger's assumed
value, and of the three domains only language models exceed 1 when fully closed. That says more
about the width of the evidence than about the system.

### What the survey changed

The memo wrote that loops that are each subcritical can be supercritical together, that the protocol
must hold the combined gain below 1, and that this is where the project's name comes from. All of
that is prior work: proved for loops [@davidson2026feedback], proved across actors
[@burtsev2026criticality], written as a sum of channels [@cunningham2026rsi], stated qualitatively
[@davidson2025three], and named as criticality in 2013 [@yudkowsky2013iem]. The independent
prior-art search took the rest. Certifying the spectral radius from entrywise upper bounds is the
linear case of the network small-gain theorem [@dashkovskiy2007smallgain]; choosing which edges to
cut is epidemic control's type and target reproduction numbers [@roberts2003typer; @shuai2013targetr]
and spectral-radius reduction by link removal [@vanmieghem2011spectral]; and a regulator testing a
spectral radius against one is in [@bardoscia2017pathways]. Label: prior work, used here as an
application
([C6](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test)). What remains ours is the use
as a treaty test, with named edges, each gated and verified separately, and the result computed on
this program's numbers above. Nothing of method.

### What it means for the protocol

A candidate design:

- **Name each edge and the gate on it.** Money to compute: chip licences and cloud rules.
  Acquisition to compute: identity checks and limits on persistence. Deployment to updates: metered
  update compute. Software to deployment beyond declared use: evaluations at checkpoints. Across
  parties: limits on transferring frontier AI research results, release decisions for weights above
  the line, and control of smuggled compute.
- **Bound the certificate.** Require rho(U) <= rho*, with U the matrix of upper confidence bounds
  and rho* = 1 - m * rho_dot * T_r: a margin set by how fast the gain drifts upward (rho_dot), the
  response time T_r and a safety factor m. The drift rate is not measured, so rho* is fixed by
  agreement until it is; this is a design, stated as one. The certificate issues only when every
  edge has a measured bound that holds jointly. While any edge is a stated range or a party's own
  report, rho(U) is a calculation on judgements and carries no probability, and edges no gate
  covers, such as weight theft, are listed or the certificate says it omits them
  ([C6](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test)).
- **Beware pooling.** Burtsev's result means that a regime which shares AI research advances widely
  among its members raises the off-diagonal terms and couples them.
- **Cost to useful AI:** limits on cross-party transfer of frontier research are a real cost to open
  science and to the spread of useful AI. They should apply only to the edge that carries gain:
  frontier AI research results and weights above the line.

### What would test it

E11 has run, on ledger values and stated ranges, so it computes and does not certify. It finds
against issuing a certificate today. Of the [10 entries](numbers.md#e11-entries) in this chapter's
one-party graph, [2 entries](numbers.md#e11-entries-measured) have a measured bound, each times an
assumed compute share, [2 entries](numbers.md#e11-entries-domain) only the natural range of an
unmeasured share, and [5 entries](numbers.md#e11-entries-unbounded) none. The row-sum test can never
issue while compute feeds software: no U on the graph has a largest row sum below
[2.14](numbers.md#e11-rowsum-floor). So the test is rho(U), and with only research closure gated it
falls to 1 only if the unmeasured entries are set to zero and the economic gain or AI's share of
hardware research is small (Y1b, Y1c). With the compute stock capped and update compute metered,
[2 gates](numbers.md#e11-gates-vendor), rho(U) would issue for one party at the developer-reported
closure, leaving [0.72](numbers.md#e11-margin-vendor) for m * rho_dot * T_r; but that closure is a
party's own report, which the certificate does not accept. Fully closed, it takes
[3 gates](numbers.md#e11-gates-fully-closed), and no single limit issues it on honest bounds
([0 pathways](numbers.md#e11-pathways-alone-honest)). Between two parties, the steady-path bound on
the entry into China's software loop is China's frontier growth over the United States',
[0.90](numbers.md#e11-g-ratio) ([1.00](numbers.md#e11-g-ratio-hi) at the 95th percentile). The two
directions' bounds are reciprocal and multiply to at least 1, so bounds of this kind can never
certify the cycle: one direction must be gated or measured below
[0.44](numbers.md#e11-xp-max-vendor). Greedy cutting needed more cuts than the smallest set in
[0 scenarios](numbers.md#e11-greedy-worse) of the grid over the real graph. Still to come: E11 again
with the diagonal from E9 and E4(b) and the compute edge from E10; E4's final rerun gives no
diagonal entry, since the speedrun's r is not identified and its simulation measures the method,
not the loop. E6 has defined cross-party
transfer as an edge in its coalition games, a party using a share of another's compute or research
output, but no such share is measured, so when sharing advances lifts the network rho above 1 among
parties that are each subcritical is not identified.

## What this perspective contributes to the line

Three quantities from this chapter are for the protocol to measure or limit. None of them is yet a
trigger.

1. **The software loop's gain per development cycle, K_S.** Measured on a log compute-equivalent
   axis with input growth divided out, from mandatory lab declarations (algorithmic efficiency at
   fixed compute, spend by input, the AI share of advances) and staged runs with elicited agents,
   reported with an interval. It is a measurement design. A trigger on its upper bound against a
   margin below 1 is cut: at the only calibrated noise E4's final simulation found the rule on K
   fires in [88%](numbers.md#e4-k-fa-n5) of runs on a loop well below 1 and barely more often on one
   above it, while the interval under-covers and the estimates lean subcritical
   ([C4](04-claims.md#c4-a-loop-gain-estimator-at-fixed-inputs-binding-at-its-confidence-bound)).
   It returns only if E4(b) shows real staged rounds tight enough. Meanwhile the protocol
   restricts closed-loop training research at frontier scale outright, the prior-work ban, for the
   loops a developer declares. Weakest point: the noise of a real staged round is unmeasured, the
   data sit with developers, staged runs at small scale may not transfer, agents can sandbag, and the
   current interval straddles 1 (corrected median [0.63](numbers.md#dyn-r-lm-corrected), 95th
   percentile [1.07](numbers.md#dyn-r-lm-hi-corrected)), while those corrections leave compute's
   growth out: counting it, E9 puts the gain at [0.25](numbers.md#e9-lm-k-fixed)
   ([0.42](numbers.md#e9-lm-k-fixed-hi) at the 95th percentile) at a compute share no data
   identifies.
2. **The coupled-gain certificate, rho(U).** The spectral radius of the matrix of upper bounds on
   each loop's own gain and on each cross-feed, over loops and parties. Its largest row sum bounds it
   from above, but on this chapter's graph that bound can never fall below
   [2.14](numbers.md#e11-rowsum-floor) while compute feeds software, so only rho(U) can issue (E11).
   The protocol gates edges until rho(U) sits below rho*. Weakest point: it issues only when every
   edge has a measured bound, and of the [10 entries](numbers.md#e11-entries) in the one-party graph
   [5 entries](numbers.md#e11-entries-unbounded) have no bound at all, so today rho(U) falls below 1
   only with the unmeasured entries set to zero, a calculation on judgements, not a certificate
   ([C6](04-claims.md#c6-the-coupled-gain-certificate-as-a-treaty-test)). The economic elasticity is
   missing, and with the software loop fully closed at its corrected 95th percentile no set of cuts
   issues it at all.
3. **Gate closure, counted in the agent's completed tasks.** For each loop's input, whether it
   crosses a verifiable human-held gate (research compute, chip licences, identity checks, update
   compute). The 80% autonomy horizon, now about [3 hours](numbers.md#dyn-horizon-p80-hours), is
   measured in human time, so gates count the agent's completed horizon-length tasks, not hours,
   until its own wall-clock time on such tasks is measured for each system
   ([C11.4](verification/l4-red-team.md#c11)). Closure judged input by input is framing until an
   experiment (E4(d)) shows that the gain under any set of gates follows from closures measured one
   gate at a time; until then the safe rule is to gate every highly closed input together, which is
   prior work
   ([C11](04-claims.md#c11-closure-judged-input-by-input-with-narrow-optimisers-inside-the-loop)).
   Weakest point: open weights on local hardware bypass identity gates, the ratio of 50% to 80%
   horizons is larger than a constant hazard predicts (E2 finds it stable within a wide interval),
   no experiment measures an agent's own time on horizon-length tasks, and long-task baselines are
   thin.

What changes for the protocol: the quantity to measure is a gain with a bound, not a slope of
capability, and until that bound can decide, the closed loop at frontier scale is restricted by the
prior-work ban; the compute backbone is reinforced, since the strongest evidence against a runaway
is that compute may be a complement to research, and E11 finds that capping the compute stock is
what lets the coupled certificate set aside the hardware loop; and nothing here is new. The
estimator extends prior work narrowly and its decision power is unshown; the certificate is an
application of prior work that cannot issue on today's evidence. None of it has been tested against
an adversary.
