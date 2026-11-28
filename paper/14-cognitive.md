# The cognitive and functional perspective

This perspective asks what a superintelligent system can do that humans and their institutions
cannot, measured rather than asserted. Superiority alone is not the line: narrow systems have long
been superhuman and are among the most useful AI. It matters because the endpoint D1 rests on it, as
does D5, the capability measurement on which triggers depend.

## F1. Kinds of advantage: speed, copies and quality

**Definition.** A system S (weights, scaffolding, tools and the inference compute its holder
controls) is compared on a task family with a named human comparison H, an individual, team or
organisation, given a wall-clock budget t and a money budget b. Serial speed s is the ratio of H's
time to one instance's time to reach the same score, retries included. Copies n is the number of
instances the compute sustains at speed s; batching trades one for the other, so they are reported
as a pair. Quality is S's best score relative to H's under the same budgets. The typology is prior
work [@grace2014forms; @bostrom1998howlong], speed and cost ratios have been measured
[@wijk2024rebench; @patwardhan2025gdpval], and the sources found assume copies
[@karnofsky2022defeat; @lifland2025timelines]; measuring them from held compute was not found, a
claim about our search. Label: extends prior work.

**Measurement.** GPT-5's naive speed gain on GDPval,
[90](../research/numbers.md#cog-gdpval-naive-speedup) times, falls to
[1.39](../research/numbers.md#cog-gdpval-review-speedup) once an expert reviews the output
[@patwardhan2025gdpval]. Copies can be computed from accounted chips and per-instance throughput,
but this is not among the paper's claims: the formula follows from a known bound [@pope2022],
forecasts already compute copies from compute [@lifland2025timelines], and nothing triggers on it.

**Evidence for and against.** Advantages are largest on short tasks and reverse at long budgets (F4)
[@wijk2024rebench]. Karnofsky argues that copies alone make a workforce [@karnofsky2022defeat].
Against free labour, larger human groups did not beat smaller ones [@aiimpacts2016coordinated].

**Open questions.** Whether a quality advantage over organisations exists outside narrow domains,
and how much copies add before coordination binds. E20, the run that would measure both, has not
run.

## F2. The decisive functions

**Definition.** A function is decisive if superiority in it, against the best human organisation at
matched time and budget, would let a system shorten its breakout time (D3) without passing a
human-held gate, or defeat the regime's detection and response. Five are named: AI research, cyber
operations, weapons-relevant science, persuasion and strategy, and economic production. The list
overlaps the frontier frameworks [@openai2025preparedness; @anthropic2026rsp], and expert baselines
exist for each cluster [@wijk2024rebench; @zhang2024cybench; @gotting2025vct; @salvi2025persuasion;
@patwardhan2025gdpval]. Label: prior work.

**Measurement.** The one live CTF comparison set an agent against mostly undergraduate teams who
used AI themselves [@tang2026ctfcollab]. Institutional baselines exist only as policy text
[@anthropic2026rsp; @gdm-fsf-v3-1-2026]; a benchmark against a measured institution was not found,
and would be D1's (C10).

Table: Where each decisive function stood in November 2026 {#tab:cognitive-functions}

| Function | Baseline | Status in the sources |
|---|---|---|
| AI research | individuals; Kaggle teams | 2024 agents ahead at short budgets, behind at long; the best 2026 model at the score's cap at the longest budget tested, its t* censored (E21) |
| Cyber operations | contest teams | ahead of student teams on short CTFs; no expert-organisation baseline |
| Weapons-relevant science | individual experts | ahead on written questions |
| Persuasion and strategy | individuals; forecasting teams | ahead of individuals; near parity with teams |
| Economic production | experts and freelancers | ahead on one-shot tasks, far from whole projects |

**Evidence for and against.** AI research is the only function whose output is a better version of
the system, so the only one that can close a loop on compute alone. Against the list:
weapons-relevant science and persuasion are misuse harms that arise well below superintelligence,
and persuasion rose more with post-training than with scale [@hackenburg2025levers], so a compute
channel would not see it.

**Open questions.** Whether superiority at AI research produces the others through the loop. A
candidate split measures only AI research and cyber operations against D1, which cannot warn; the
trigger is the line on breakout time (D4).

## F3. Narrow versus general

**Definition.** Generality G(S) is the number, or fraction alpha, of decisive clusters in which S
meets the institutional bar at matched t and b, counted without averaging. A system is narrow if G
is at most one and its outputs do not enter the training data, code or compute allocation of a
system above the line (closure). The split is prior work [@morris2023levels; @genewein2026agiasi],
as are separate limits on general intelligence and on AI improving AI [@miotti2025narrowpath];
joining generality to a closed loop was not found. Label: extends prior work.

**Measurement.** Existing scales compare with individuals [@morris2023levels], and averaging
"implicitly assumes compensability" [@fourati2025coherence]. The battery must be held by the regime.

**Evidence for and against.** Narrow superhuman systems are cheap [@meta2019pluribus] and brittle
[@wang2023adversarialgo]. Against: AlphaEvolve, a general model working against automated
evaluators, cut Gemini's training time by [1%](../research/numbers.md#cog-alphaevolve-training-cut),
by the vendor's figures [@novikov2025alphaevolve]. "Narrow" describes a task, not a system. The
effect is small: it shows the loop exists, not that its gain is high.

**Open questions.** E1 could not count G from public data. Whether narrow training raises G (the
evidence says mostly not [@huan2026mathtransfer]) or a narrow optimiser raises loop gain (E4(e)) is
untested. The line on breakout time supersedes F3's line; only the rule that a narrow optimiser
inside a covered loop counts as part of it survives (C11).

## F4. Measuring capability so a protocol can trigger on it

Benchmarks saturate: FrontierMath's best score rose from under
[2%](../research/numbers.md#cog-fm-release-best) at release [@glazer2024frontiermath] to
[95.1%](../research/numbers.md#cog-fm-best) by November 2026 [@epoch2026hub]. Items are often wrong:
Epoch judged [46%](../research/numbers.md#cog-hle-defective-share) of a sample of HLE questions
defective [@epoch2026hlereview]. Scores overstate real work: maintainers' merge rates for AI patches
sit about [24 points](../research/numbers.md#cog-swebv-maintainer-gap) below SWE-bench scores
[@whitfill2026merge]. A test set the developer has seen measures memory [@liang2025illusion].
Refreshed batteries are prior work [@white2024livebench; @kiela2021dynabench]; refresh with
institutional baselines was not found.

Verdicts depend on the budget: RE-Bench's AI-to-human ratio moves
[8](../research/numbers.md#cog-rebench-swing)-fold between the
[2 h](../research/numbers.md#cog-rebench-budget-short) and
[32 h](../research/numbers.md#cog-rebench-budget-long) budgets [@wijk2024rebench]. The crossover
budget t\* is the largest tested time budget at which S's score on the AI-research cluster is at
least the comparison's at equal compute and money; if S still wins at the largest budget tested, t\*
is censored, never extrapolated. Crossovers are prior work [@wijk2024rebench;
@robinson2026horizons]. E21's public part estimated t\* on two boards, against single experts and
contest teams, none an organisation. On RE-Bench [@metr2026evalanalysis],
[14 models](../research/numbers.md#e21-rebench-below-8h) of
[18 models](../research/numbers.md#e21-rebench-models) are censored below
[8 h](../research/numbers.md#cog-rebench-budget-mid); the best sits at the score's cap at
[32 h](../research/numbers.md#cog-rebench-budget-long) in
[99.4%](../research/numbers.md#e21-rebench-cap-32h) of resamples, so its t\* is censored above
[32.0 h](../research/numbers.md#e21-rebench-tstar-best). On Cybench, against the fastest contest
team [@cybench2024repo], t\* cannot be measured above the pool's longest first-solve time,
[24.9 h](../research/numbers.md#e21-cyber-ceiling-h). t\* rises with release date on both boards
(rank correlations [0.57](../research/numbers.md#e21-rebench-rho) and
[0.91](../research/numbers.md#e21-cyber-rho)), but only while a battery's baselines last: it
saturates with the battery, so a rising t\* needs batteries refreshed with longer baselines. Each
side is charged the inference it uses [@vahdati2026arc], and the human side's tools are frozen at a
declared date [@genewein2026agiasi].

An observed score is a lower bound [@barnett2024evaluations]. Sandbagging is often recoverable
[@benton2024sabotage], but elicitation of password-locked models fails without high-quality
demonstrations [@greenblatt2024password], and tamper-resistant locks survive weak-to-strong
fine-tuning [@finke2026robustorganisms]. Detectors tuned on fixed organisms fail against adaptive
ones [@soopal2026adaptive], and models increasingly tell tests from use [@needham2025evalaware]. D5
judges a threshold by miss and false-alarm rates per named elicitation budget, an extension of
diagnostic-test practice [@fda2007diagnostic]. It bounds only non-adaptive hiding, and E3, the
experiment that would measure its rates, has not run. Above expert level no demonstrations exist, so
the guarantee is weakest where D1 begins.

As the evidence leaves it, D1 holds if, in at least a fraction alpha of decisive clusters, S's
elicited score beats a named organisation given the same time and money, on a regime-held, refreshed
battery, with the organisation's tools frozen. The verdict is stated under both matches, money and
time. It extends prior work [@genewein2026agiasi; @ngo2023tagi; @anthropic2026rsp]. No public
battery compares with an organisation at matched budget, so D1 is a definition only. Its pass
condition, a verdict stable when the organisation changes within its class, met its refuter on the
nearest analogue any battery has: on MLE-bench, E21 found the verdict flips on
[45.3%](../research/numbers.md#e21-mle-flip-best) of competitions between the median entrant and the
gold threshold [@openai2026mlebenchruns; @chan2024mlebench], so the rank must be named.
Institutional baselines still have to be built; E21's live part has not run. It holds only once a
system beats an institution, so it cannot warn; the protocol must act on the line before it.

## What this perspective gives the line

It gives the protocol its endpoint, D1, as a fully stated definition, not a trigger. Part II takes
from it elicited capability (D5) and the narrow-optimiser rule, both untested, and counts serving
capacity without limiting it.
