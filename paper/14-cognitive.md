# The cognitive and functional perspective

This perspective measures what a superintelligent system can do that humans and their institutions
cannot. Narrow systems have long been superhuman and useful, so superiority alone is not the line.
The endpoint D1 and the measurement D5 rest on it.

## F1. Kinds of advantage: speed, copies and quality

**Definition.** S, with its holder's inference compute, faces a named individual, team or
organisation given time t and money psi. Speed s is the comparison's time over one instance's;
copies n, the instances the compute sustains at that speed; quality, S's best score relative to the
comparison's. The typology is prior work [@grace2014forms; @bostrom1998howlong]; the sources found
assume copies [@karnofsky2022defeat; @lifland2025timelines]. Label: extends prior work.

**Measurement.** GPT-5's naive speed gain on GDPval,
[90](../research/numbers.md#cog-gdpval-naive-speedup) times, falls to
[1.39](../research/numbers.md#cog-gdpval-review-speedup) under expert review
[@patwardhan2025gdpval]. Measuring copies from held compute was not found, but it follows from a
known bound [@pope2022] and is not claimed here.

**Evidence for and against.** Copies alone may make a workforce [@karnofsky2022defeat], but larger
human groups did not beat smaller ones [@aiimpacts2016coordinated].

**Open questions.** Quality against organisations, and the return to copies (E20, not run).

## F2. The decisive functions

**Definition.** A function is decisive if superiority in it, against the best organisation at
matched budget, shortens breakout time (D3) past human-held gates or defeats detection: AI research,
cyber operations, weapons-relevant science, persuasion and strategy, and economic production. The
list overlaps the frontier frameworks [@openai2025preparedness; @anthropic2026rsp], and each has
expert baselines [@wijk2024rebench; @zhang2024cybench; @gotting2025vct; @salvi2025persuasion;
@patwardhan2025gdpval]. Label: prior work.

**Measurement.** Institutional baselines exist only as policy text [@anthropic2026rsp;
@gdm-fsf-v3-1-2026]; the one live CTF faced mostly undergraduates using AI [@tang2026ctfcollab].

Table: The decisive functions in November 2026 {#tab:cognitive-functions}

| Function | Baseline | Status |
|---|---|---|
| AI research | experts; Kaggle teams | at the cap (E21) |
| Cyber operations | contest teams | ahead on short CTFs |
| Weapons-relevant science | experts | ahead on written tests |
| Persuasion and strategy | individuals; forecasters | near parity with teams |
| Economic production | experts; freelancers | ahead on one-shot tasks |

**Evidence for and against.** Only AI research yields a better system, closing a loop on compute
alone. Weapons-relevant science and persuasion are misuse harms below superintelligence, and
persuasion tracks post-training more than scale [@hackenburg2025levers].

**Open questions.** Whether AI research yields the others through the loop.

## F3. Narrow versus general

**Definition.** Generality G is the number, or fraction alpha, of decisive clusters where S meets
the institutional bar, without averaging [@fourati2025coherence]; S is narrow if G is at most one
and its outputs feed no system above the line. The split is prior work [@morris2023levels;
@genewein2026agiasi; @miotti2025narrowpath]; joining it to a closed loop was not found. Label:
extends prior work.

**Measurement.** Scales compare with individuals [@morris2023levels]; E1 could not count G from
public data.

**Evidence for and against.** Narrow systems are cheap [@meta2019pluribus] and brittle
[@wang2023adversarialgo], but AlphaEvolve, a general model, cut Gemini's training time by
[1%](../research/numbers.md#cog-alphaevolve-training-cut) (vendor's figure)
[@novikov2025alphaevolve]: narrowness belongs to tasks, not systems, though the effect is small.

**Open questions.** Whether narrow training raises G [@huan2026mathtransfer] or a narrow optimiser
raises loop gain (E4(e)). Of F3's line, Part II keeps only the rule counting such an optimiser as
part of its loop (C11).

## F4. Measuring capability so a protocol can trigger on it

Benchmarks saturate within years [@glazer2024frontiermath; @epoch2026hub]. Items are often wrong
[@epoch2026hlereview], scores overstate real work [@whitfill2026merge], and seen test sets measure
memory [@liang2025illusion]. Refreshed batteries are prior work [@white2024livebench;
@kiela2021dynabench].

Verdicts depend on the budget [@wijk2024rebench]. The crossover budget t\* is the largest tested
time budget at which S's AI-research score at least equals the comparison's at equal compute and
money, censored, never extrapolated; crossovers are prior work [@wijk2024rebench;
@robinson2026horizons]. Against experts and contest teams, none an organisation, E21 found
RE-Bench's best model at the score's cap at the top budget [@metr2026evalanalysis], and t\*
unmeasurable on Cybench beyond its longest task [@cybench2024repo]: t\* rises with release date only
while baselines last.

An observed score is a lower bound [@barnett2024evaluations]. Hidden capability is often recoverable
[@benton2024sabotage], but not without good demonstrations [@greenblatt2024password] or from
tamper-resistant locks [@finke2026robustorganisms]; detectors fail against adaptive organisms
[@soopal2026adaptive], and models tell tests from use [@needham2025evalaware]. D5's rule is untested
(E3) and covers only non-adaptive hiding on the regime's own organisms, which a frontier model's
hiding is not drawn from, at any capability level.

D1, as the evidence leaves it, holds if S's elicited score beats a named organisation O_k, with the
same time t_k and money psi_k and its tools frozen, in at least a fraction alpha of the N_d decisive
clusters of a regime-held, refreshed battery [@genewein2026agiasi; @ngo2023tagi; @anthropic2026rsp].
No battery compares with an organisation, so D1 is a definition only, its pass condition untested.
On MLE-bench the verdict depends on the rank named: the best entry beats the median entrant in
[71.1%](../research/numbers.md#e21-mle-median-best) of competitions and the gold threshold in
[25.8%](../research/numbers.md#e21-mle-gold-best) [@openai2026mlebenchruns]. D1 holds only once a
system is ahead, so it cannot warn; the line on breakout time (D4) must act first.

## What this perspective gives the line

The endpoint as a definition, not a trigger; Part II takes D5 and the narrow-optimiser rule, both
untested, and counts serving capacity without limiting it.
