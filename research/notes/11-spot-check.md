# Spot-check 11: are the survey notes faithful to their sources?

- **What was checked:** survey notes 01 to 10 in `research/notes/`. For each note, 5 or 6 claims
  were chosen by risk, not at random:
  - at least 2 the note uses against the memo or to call a memo idea prior work (from its summary
    and its "Prior art for the memo's candidates" section);
  - at least 1 surprising, recent (2025-2026) number or quote;
  - at least 1 number from its "Numbers for the ledger" table.

  A few more were added where a check turned up something. In all, 53 claims.
- **Who:** an independent checker that wrote none of the notes and trusted none of them.
- **Date:** 2026-11-27.
- **How:**
  - Each cited source was fetched directly (arXiv abstract page plus the PDF or HTML full text;
    publisher, agency and company pages; data files). Text was extracted locally (`pdftotext`, an
    HTML-to-text pass), and the passage was found by searching the extracted text, never by
    trusting a summary.
  - Data files were downloaded and the note's numbers recomputed: Epoch's `benchmark_data.zip`,
    Epoch's `ai_chip_sales_timelines_by_chip.csv` and METR's `benchmark_results_1_1.yaml`.
  - Four hosts refused automated access. For SEC.gov, the PDF came through the web fetcher and its
    text was extracted locally. For the National Academies and PubMed Central, the passage was read
    through the web fetcher, which returns a model's quotation of the page: treat those two as one
    step weaker. LessWrong was read on its GreaterWrong mirror, same post ID.
  - For every checked source, the identifier was checked against the stated title and authors.
- **Verdicts:**
  - CONFIRMED: the source says it and the numbers match.
  - DISTORTED: the source says something related, but the note overstates it, misquotes it, gets
    a number or date wrong, or drops a caveat that matters. A paraphrase inside quotation marks
    counts as DISTORTED.
  - NOT FOUND: the source was opened and gave no support.
  - UNREACHABLE: the source would not load.
  - FABRICATED-LOOKING: the identifier does not resolve to the stated work.

  Smaller slips that do not change what a claim can support are listed under "Minor" in each note.
  They are not counted.

## Summary table

| Note | Claims checked | Confirmed | Distorted | Not found | Unreachable | Fabricated-looking |
|---|---|---|---|---|---|---|
| 01 definitions | 6 | 5 | 1 | 0 | 0 | 0 |
| 02 physics | 5 | 5 | 0 | 0 | 0 | 0 |
| 03 algorithms | 5 | 5 | 0 | 0 | 0 | 0 |
| 04 dynamics | 6 | 5 | 1 | 0 | 0 | 0 |
| 05 cognition | 5 | 4 | 1 | 0 | 0 | 0 |
| 06 economics | 5 | 5 | 0 | 0 | 0 | 0 |
| 07 compute governance | 5 | 5 | 0 | 0 | 0 | 0 |
| 08 arms control | 5 | 5 | 0 | 0 | 0 | 0 |
| 09 mechanism design | 6 | 6 | 0 | 0 | 0 | 0 |
| 10 gameable evaluations | 5 | 5 | 0 | 0 | 0 | 0 |
| **Total** | **53** | **50** | **3** | **0** | **0** | **0** |

Every identifier checked (arXiv IDs, DOIs, URLs, data files) resolved to the stated work and
authors. No note looks systematically unreliable. The three distortions follow one pattern: a
summary or ledger row keeps a source's number but drops the caveat that limits what it means, or
puts quotation marks around a paraphrase.

---

## 01 definitions

1. **Claim:** Barnett and Scher (MIRI TGT, 2025) state that a stable regime needs nations "to
   detect and respond to dangerous AI development faster than any single country's breakout
   time" (used to downgrade D4).
   - Source: `barnett2025governance`, arXiv:2505.04592v1. Title and authors match (Peter Barnett,
     Aaron Scher, MIRI Technical Governance Team, 7 May 2025).
   - **Verdict: CONFIRMED.**
   - Evidence (section on the Threat of Sabotage regime): "This regime faces a key challenge:
     nations must be able to detect and respond to dangerous AI development faster than any single
     country's breakout time, the time needed to secretly advance beyond permitted levels of AI
     capabilities. Stability would require that each side has sufficient visibility and sabotage
     capability."
2. **Claim:** A Narrow Path (v1.2.0, April 2025) sets cluster caps so an illegal run would take
   3.2 years, "giving authorities ample time to intervene", while permitted models train within
   12 days (ledger: `narrowpath-breakout-years` 3.2, `narrowpath-permitted-run-days` 12).
   - Source: `miotti2025narrowpath`, pdf.narrowpath.co/A_Narrow_Path.pdf. Authors Miotti, Bilge,
     Kasten, Newport; footer "April 2025 V1.2.0".
   - **Verdict: CONFIRMED.**
   - Evidence (Annex 2): "a difference in order of magnitude of 8 between the Upper Limit Compute
     limit and the Medium Limit Computing Cluster limit, meaning that it would take a licensed
     cluster 3.2 years to breach the Upper Limit in an illegal training run, giving authorities
     ample time to intervene. However, licensed actors could still train any permitted model within
     12 days". (1e8 s is 3.17 years.)
3. **Claim:** METR (Nov 2026) measured a 1.9x acceleration (95% CI 1.5 to 2.8x) in Anthropic's
   capability index, 15 to 29 points a year, robustness range 1.1x to 2.9x, about 80% due to AI
   (ledger rows `metr-anthropic-acceleration*`, `metr-aeci-*`).
   - Source: `metr-anthropic-acceleration-2026`,
     metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/. Authors match: Cunningham,
     Rush, Whitfill, Wijk.
   - **Verdict: CONFIRMED.**
   - Evidence: "growing at an estimated 1.9x the pre-October 2025 rate [95% confidence interval:
     1.5-2.8x]". Chart alt text: "A trend of +15 points per year before October 2025 steepens to
     +29 points per year after it". "Robustness analyses find acceleration rates between 1.1x and
     2.9x". "a majority (perhaps ~80%) of the current (October 2026) acceleration is due to AI".
4. **Claim (found while checking 3):** the entry quotes METR as saying Anthropic "removed a
   compute-allocation verification component midway".
   - Source: same page.
   - **Verdict: DISTORTED** (a paraphrase in quotation marks; the substance is right).
   - Evidence: the phrase does not appear. The page says: "Anthropic changed the scope of this
     project midway to exclude compute verification and instead just focus on AI R&D acceleration.
     This component was canceled before METR came to any substantive conclusions on compute usage
     at Anthropic."
5. **Claim:** Burtsev (Aug 2026) defines R_AI = chi * a / sigma with a self-amplifying regime at
   R_AI > 1, chi being "operational closure" (used to downgrade D2; D6 overlap); illustrative
   cycle delay 0.5 years (ledger `burtsev-cycle-delay`).
   - Source: `burtsev2026recursive`, arXiv:2609.00137. Title "Recursive Criticality of AI
     Self-Improvement", author Mikhail Burtsev, submitted 31 Aug 2026.
   - **Verdict: CONFIRMED.**
   - Evidence: abstract, "When R_AI > 1, the effects of improvements compound across development
     cycles". Boxed equation "R_AI = g/sigma = chi a/sigma". "We denote this transmitted fraction
     by the operational closure chi". "we fix the feedback delay at tau = 0.5 yr".
6. **Claim:** Anthropic (Feb 2026): "We found pre-set capability levels to be far more ambiguous
   than we anticipated".
   - Source: `anthropic-rsp-v3-announcement-2026`,
     anthropic.com/news/responsible-scaling-policy-v3, "Published Feb 24, 2026".
   - **Verdict: CONFIRMED.**
   - Evidence: the quote is verbatim, as are "The science of model evaluation isn't well-developed
     enough to provide dispositive answers" and "might prove outright impossible to implement
     without collective action".

Minor (not counted): summary item 1 says "a stable regime needs"; Barnett and Scher say it of the
Threat of Sabotage regime specifically.

## 02 physics

1. **Claim (against P4):** Rahman (2026): 1e24 FLOP needs only two 16-H100 nodes ($1.6M), 1e25
   FLOP 34 nodes of 16 GH200, and the thresholds "could be evaded using $1.6M, $31M, and $3.8B".
   - Source: `rahman2026`, arXiv:2605.29359. Title "Does Distributed Training Undermine Compute
     Governance?", Robi Rahman, submitted 28 May 2026.
   - **Verdict: CONFIRMED.**
   - Evidence (Table 1): "1e24 16x H100 FP8 2 Flat ... $1.6M"; "1e25 16x GH200 FP8 34 Flat ...
     0.3698 ... Cquality 6.4e24 ... $30.7M". Text: "could be evaded using $1.6M, $31M, and $3.8B,
     respectively, of hardware arranged in clusters smaller than any proposed registration
     requirement."
2. **Claim (P4 prior art):** Koopmanschap and Barten (2026) define an "enforcement breaking
   point", and a satellite classifier found every facility above 10 MW and missed every one below.
   - Source: `koopmanschap2026`, arXiv:2607.22619. Title "How to Catch a GPU", authors Raymond
     Koopmanschap and Otto Barten, submitted 16 Jun 2026.
   - **Verdict: CONFIRMED.**
   - Evidence: "Satellite surveillance reliably detects facilities above 10 MW (~10,000
     H100-equivalents) and might fail below this range". "All four false negatives in his
     classifier had power capacity below 10 MW (1.2, 0.5, 3.2, and 0.5 MW) ... Above 10 MW the
     classifier achieved a 100% true positive rate; below it, the same classifier missed every
     facility in the available sample." The term "enforcement breaking point" is defined in the
     abstract.
3. **Claim (recent):** a 2026 study of a 126 MW-plus cluster near Tokyo found night-time
   facility-scale surface temperature changes "indistinguishable from zero".
   - Source: `jing2026`, DOI 10.1088/1748-9326/aead02 (Environ. Res. Lett. 21 204030, published
     4 November 2026, Jiawei Jing).
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "Deep-night facility-scale LST changes are indistinguishable from zero
     (bounded below ~0.6 C-1.2 C)". Body: "a cluster electricity draw of at least ~126 MW in
     FY2023". Abstract: "kilometre-scale surface warming from waste heat is unattainable".
4. **Claim (ledger):** the CMOS efficiency ceiling is 4.7e15 FP4/J, roughly 200 times current
   chips, a 50% chance of stopping after about 207-fold (ledger `cmos-ceiling-*`).
   - Source: `ho2023`, arXiv:2312.08595. Authors Anson Ho, Ege Erdil, Tamay Besiroglu.
   - **Verdict: CONFIRMED.**
   - Evidence: "geometric mean estimate of 4.7 x 10^15 FP4/J for the maximum CMOS energy
     efficiency, roughly two hundred-fold more efficient than current microprocessors". "a 50%
     chance that further improvements in energy efficiency will cease after another 290/1.4 ~
     207-fold". The note's flagged error in the paper (kT ln 2 at 300 K printed as "4 x 10^-21 J")
     is also correct.
5. **Claim (against P4):** analogue power metering cannot exclude hidden compute of 41% to 116%
   of declared capacity.
   - Source: `kimpson2026b`, arXiv:2610.07476 (Kimpson, Baker, Graham; v2 17 Nov 2026).
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "Measurements on NVIDIA A100 GPUs give beta = 1.16 in the worst case,
     while an adversarial matched-energy schedule hides at least 0.41. Analogue power measurements
     alone therefore constrain compute weakly."

Minor (not counted):
- Summary item 5 says "1e25 FLOP 34 nodes" without the source's quality adjustment: those nodes
  reach only 6.4e24 quality-adjusted. The entry has it right.
- Summary item 5's "at least 96%" comes from arXiv:2610.30182, which is on simulated power. The
  summary drops "simulated"; the entry keeps it.

## 03 algorithms

1. **Claim (against D3):** "only under 100x of the claimed 22,000x reproduces at small compute,
   because the big gains ... are scale-dependent (Gundlach et al., NeurIPS 2026)".
   - Source: `gundlach2025origin`, arXiv:2511.21622. Authors Gundlach, Fogelson, Lynch, Trisovic,
     Rosenfeld, Sandhu, Thompson; v2 10 Nov 2026; comments: "Accepted at NeurIPS 2026 (camera-ready
     version)".
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "a factor of 22,000 between 2012 and 2023 ... we are able to account for
     less than 10x of these gains at small compute scales ... additional innovations ... also
     account for less than 10x, yielding less than 100x efficiency gains total in low-compute
     regimes"; "measures of algorithmic efficiency are strongly reference-dependent".
2. **Claim (against the pathway table):** compute explains 80 to 90% of frontier performance
   differences across 809 models.
   - Source: `mertens2026secretsauce`, arXiv:2602.07238. Authors Mertens, Fischl-Lanzoni,
     Thompson; v2 3 May 2026.
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "809 models released between 2022 and 2025 ... At the frontier, 80-90%
     of performance differences are explained by higher training compute"; "more than 40x compute
     efficiency difference".
3. **Claim (recent):** the NanoGPT speedrun record fell from 2,700 s to 39.9 s in 27 months
   (67.7x; tokens from 10B to under 330M).
   - Source: `moddednanogpt`, github.com/KellerJordan/modded-nanogpt (raw README).
   - **Verdict: CONFIRMED.**
   - Evidence: record table, "1 | 45 minutes | llm.c baseline | 05/28/24" and "92 | 0.665 minutes
     | ... | 08/30/26" (the latest row). README: "Under 40 seconds on 8xH100" and "under 330M
     tokens (the llm.c GPT-2 replication needed 10B)". 2700/39.9 = 67.7.
4. **Claim (ledger):** compute for fixed LM performance halved every 8.4 months (95% CI 4.5 to
   14.3); 60 to 95% of gains from compute (ledger `algo-halving-lm`, `algo-compute-share-lm`).
   - Source: `ho2024algorithmic`, arXiv:2403.05812. Authors Ho, Besiroglu, Erdil, Owen, Rahman,
     Guo, Atkinson, Thompson, Sevilla.
   - **Verdict: CONFIRMED.**
   - Evidence: "the median doubling time for effective compute is 8.4 months, with a 95%
     confidence interval of 4.5 to 14.3 months". "60-95% of the performance gains stem from compute
     scaling". Transformer "7.2x [95% CI: 3.3x, 45.7x]".
5. **Claim (cap-leak prior art):** Ord 2025: "a model trained with 10^24 FLOP might use 10,000
   times more inference compute to perform at the level of a model trained with 10^27 FLOP".
   - Source: `ord2025govaireport`, cdn.governance.ai/Inference_Scaling_and_AI_Governance_Technical_Report.pdf
     ("Technical Report, October 2025", Toby Ord).
   - **Verdict: CONFIRMED.**
   - Evidence: the quote is verbatim. So is the footnoted trade-off: "increasing inference compute
     on the task at hand by a factor of 10 can improve performance as much as increasing
     pre-training compute by 3-10x".

Minor (not counted):
- Item 1's "reproduces" is loose. Only the first <10x comes from the authors' ablations; the
  second <10x is their survey estimate.
- The Ord report gives the author's affiliation as the Oxford Martin AI Governance Initiative;
  GovAI hosts it.

## 04 dynamics

1. **Claim (Y3 is prior work):** Davidson, Halperin, Houlden and Korinek (NBER w35155, April
   2026) prove that two loops explode jointly iff the interaction matrix has an eigenvalue above
   1 (beta_S beta_H < phi_S phi_H), and in general when the spectral radius exceeds 1.
   - Source: `davidson2026feedback`, DOI 10.3386/w35155 (NBER page: "Working Paper 35155 ...
     Issue Date April 2026"; the four authors match).
   - **Verdict: CONFIRMED.**
   - Evidence: "this occurs if the interaction matrix has an eigenvalue greater than unity ... the
     eigenvalue condition holds here if and only if: betaS betaH < phiS phiH (8)". "the system
     exhibits explosive growth if and only if that spectral radius is greater than 1". Abstract:
     "a singularity within six years".
2. **Claim (D2 is prior work):** Cunningham et al. call the product of elasticities "the loop
   gain", say tracking it "is arguably the most important empirical exercise", and put the
   threshold at about 15% more research productivity per ECI point.
   - Source: `cunningham2026rsi`, arXiv:2609.15802. Title "The Economics of Recursive
     Self-Improvement", nine authors as listed, 14 Sep 2026.
   - **Verdict: CONFIRMED.**
   - Evidence: "estimating this quantity, tracking it over time, and extrapolating when it might
     cross 1 is arguably the most important empirical exercise". Footnote 9: "the loop gain eps_R,C
     eps_C,A that enters the condition is invariant to it". "self-sustaining acceleration is
     achieved if eps_R,C > 0.15".
3. **Claim:** "the rough estimate is about 9%, below threshold but rising" (summary item 2;
   ledger `rsi-estimate-eps-rc` "about 0.09").
   - Source: same paper, Section 4.1.
   - **Verdict: DISTORTED** (drops a caveat that changes the number's meaning).
   - Evidence: "The 4X uplift is very likely to be an overestimate, but even if it were true it
     would imply a 9% increase in productivity per unit of ECI, below the threshold". The 9% is
     what a self-report the authors distrust would imply, an upper-end figure. It is not their
     rough estimate.
4. **Claim (recent):** Anthropic (August 2026): Claude "leads" 26% of its AI R&D work, up from
   under 1% in February 2026, with about 30,000 agents running at once (ledger
   `anthropic-ai-led-share`, `anthropic-agents-concurrent`).
   - Source: `anthropic2026pace`, anthropic.com/institute/measuring-pace-of-ai-development
     (co-authors Marina Favaro and Phillie Wright).
   - **Verdict: CONFIRMED.**
   - Evidence: "Claude 'leads' 26% of Anthropic's AI R&D work. The share of work at or above 'AI
     collaborates' is above 90%." Chart alt text: "Claude now leads 26% of Anthropic's model R&D
     tasks, up from under 1% in February 2026." "approximately 30,000 agents doing research and
     engineering work at Anthropic at any one time in our most-used internal platform".
5. **Claim (ledger):** time-horizon doubling 128.744 days (104.428 to 158.012) from 2023 on; Claude
   Mythos Preview (early, 2026-04-07) p50 1,044.8 minutes (508.9 to 3,304.3) (ledger
   `horizon-doubling-data-2023on`, `horizon-p50-sota-latest`).
   - Source: `metr2026thdata`, metr.org/assets/benchmark_results_1_1.yaml (downloaded).
   - **Verdict: CONFIRMED.**
   - Evidence: "from_2023_on: ci_high: 158.012, ci_low: 104.428, point_estimate: 128.744". Under
     `claude_mythos_preview_early_inspect`: "p50_horizon_length: ci_high: 3304.261235, ci_low:
     508.876789, estimate: 1044.780145 ... release_date: 2026-04-07".
6. **Claim (against "algorithms route around the cap"):** under compute slowdowns, 1-month 80%
   horizons arrive 7 years later than trend.
   - Source: `whitfill2025horizon`, arXiv:2511.19492 (Whitfill, Snodin, Becker; 23 Nov 2025).
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "time horizon growth must be proportional to compute growth ...
     1-month time horizons at 80% reliability occur 7 years later than simple trend extrapolation
     suggests". The model "precludes the possibility of a software-only singularity", an
     assumption worth carrying when this is used against the memo.

Minor (not counted): the 30,000 agents are for "our most-used internal platform", not all of
Anthropic.

## 05 cognition

1. **Claim (D1 is prior work):** Genewein et al. 2026 define ASI against "large human-expert
   collectives" (tens of thousands of experts, 10 years, 2010 technology), beaten in a tenth of the
   time, and one ASI "may consist of a collective of millions of instances".
   - Source: `genewein2026agiasi`, arXiv:2606.12683 v3. Title "From AGI to ASI"; authors Genewein,
     Franklin, Lerchner, Orseau, Albanie, Bales, Wyeth, Chan, Gabriel, Leibo, Dafoe, Hutter,
     Graepel, Legg; v1 10 Jun 2026, v3 10 Nov 2026.
   - **Verdict: CONFIRMED.**
   - Evidence: "reliably outperforms hypothetical groups of tens of thousands of well-coordinated
     expert-level humans that work over a period of 10 years with the technology and cultural
     artifacts available in 2010 on a single problem or task". "ASI would perform the same tasks in
     less time, say by a factor of 10 or more". "a single ASI may consist of a collective of
     millions of instances".
2. **Claim (D1 is prior work):** Ngo 2023 defines (t,n)-AGI against "any group of n humans
   working together" and calls superintelligence a "(1 year, 8 billion)-AGI".
   - Source: `ngo2023tagi`, LessWrong post BoA3agdkAzL6HQtQP (Richard Ngo, 4 May 2023).
     LessWrong and the Alignment Forum returned 403; read on the GreaterWrong mirror of the same
     post ID.
   - **Verdict: CONFIRMED.**
   - Evidence: "(t,n)-AGIs which beat any group of n humans working together on tasks for time t.
     When I think about superintelligence I'm typically thinking about (1 year, 8 billion)-AGIs."
3. **Claim (recent, used as a team baseline for D1):** "In a 24-hour onsite CTF in 2026, an agent
   placed 2nd on the human scoreboard for about $96 of API use and about a fifth of the human
   runtime" (ledger `ctf-agent-points-2026`, `ctf-agent-api-cost-2026`).
   - Source: `tang2026ctfcollab`, arXiv:2602.20446. Title "Understanding Human-AI Collaboration in
     Cybersecurity Competitions", nine authors as listed, submitted 24 Feb 2026.
   - **Verdict: DISTORTED** (the numbers are right; caveats that matter for D1 are dropped, and
     the year is unsupported).
   - Evidence for the numbers: "reaches 4900 points (second place on the human scoreboard) in
     roughly four hours of cumulative runtime, at a cost of $95.32" (Sec. 7.2; the introduction
     says $96.32). "only ~1/5 of the cumulative runtime".
   - What is dropped:
     - It was "A Live University-level CTF Event" hosted "on campus". Study participants were
       82.9% undergraduates and 14.6% graduate students.
     - The human teams "collaborated with AI to solve challenges", so the human scoreboard is of
       human-plus-AI teams.
     - The agents ran "in parallel with the human competition ... to produce an agent-only
       scoreboard"; they were compared with the human teams, not entered against them.
     - The paper gives no event date and was submitted on 24 Feb 2026, so "in 2026" (and the
       ledger IDs ending "-2026") is not supported.
4. **Claim (ledger):** GDPval's naive 90x speed gain for GPT-5 falls to 1.39x once review is
   counted; expert time 404 minutes and cost $361 per task.
   - Source: `patwardhan2025gdpval`, arXiv:2510.04374 (HTML v1; first author Tejal Patwardhan).
   - **Verdict: CONFIRMED.**
   - Evidence (Table 2): "gpt-5 39.0% 90x 1.12x 1.39x 474x 1.18x 1.63x". Appendix: "HT=404 minutes
     and HC=$361".
5. **Claim (recent):** FrontierMath went to 95% on Tiers 1-3 and 100% on Tier 4 (three models,
   Sep-Nov 2026); GPQA Diamond 96.8% (ledger `frontiermath-t4-best-2026` 100,
   `frontiermath-t13-best-2026-11` 95.09).
   - Source: `epoch2026hub`, epoch.ai/data/benchmark_data.zip (downloaded).
   - **Verdict: CONFIRMED.**
   - Evidence: in `frontiermath_tier_4_v2.csv`, mean_score 1.0 (stderr 0.0) for
     claude-fable-5-2_max (2026-11-09), gpt-6.2-astra_max (2026-11-17) and gpt-6.1-sol_max
     (2026-09-29). In `frontiermath_tiers_1_3_v2.csv`, the best is 0.95088 (claude-fable-5-2_max).
     In `gpqa_diamond.csv`, the best is 0.96843 (gpt-6.2-astra_max).

## 06 economics

1. **Claim (against the memo: the chokepoint leaks):** Epoch estimates 660,000 H100e (90% CI
   290,000 to 1.6 million) smuggled into China through 2025, about a third of China's AI compute.
   - Source: `juniewicz2026smuggling`, epoch.ai/blog/chip-smuggling ("Report Apr. 29, 2026", by
     Isabel Juniewicz).
   - **Verdict: CONFIRMED.**
   - Evidence: "Our model estimates 660,000 (90% CI: 290,000-1.6 million) H100e of cumulative
     compute smuggled through the end of 2025." "Our median estimate of 660,000 H100e would be
     roughly a third of China's total compute." Detection rate "median 25%".
2. **Claim (against the memo: power is not a chokepoint):** China added 315 GW of solar and 119
   GW of wind in 2025.
   - Source: `shaw2026chinasolar`, pv-magazine.com, 28 Jan 2026, Vincent Shaw.
   - **Verdict: CONFIRMED.**
   - Evidence: "the country added 315.07 GW (AC) of new solar capacity last year, alongside 119.33
     GW of wind". "cumulative installed power capacity had reached 3.89 TW".
3. **Claim (recent):** SemiAnalysis counts more than 2.9 million TSMC-made Ascend dies, though
   the 2020 entity listing was meant to cut Huawei off from TSMC (allen2025senate, p. 4).
   - Sources: `patel2025ascend` (newsletter.semianalysis.com/p/huawei-ascend-production-ramp,
     public portion) and `allen2025senate` (foreign.senate.gov testimony PDF, 2 Dec 2025).
   - **Verdict: CONFIRMED.**
   - Evidence: "Huawei ended up receiving more than 2.9M Ascend die". "China has procured 13M HBM
     stacks which is sufficient for 1.6M Ascend 910C packages". Allen: "the first Trump
     administration's updated 2020 entity listing, which temporarily cut Huawei's Ascend and Kirin
     lines off from TSMC."
4. **Claim (ledger):** 13.61 million H100e sold in 2025 (5.10 million in 2024), Nvidia 65.5%
   (ledger `ai-compute-sold-2025`, `nvidia-share-h100e-2025`).
   - Source: `epoch2026chipsales`, epoch.ai/data/ai_chip_sales_timelines_by_chip.csv (estimates
     generated 11-24-2026).
   - **Verdict: CONFIRMED.**
   - Evidence: my own sum of the median H100e column gives 2024 5.098M and 2025 13.605M. 2025
     shares: Nvidia 65.5%, Google 20.2%, Amazon 5.2%, AMD 5.0%, Huawei 3.9%, Cambricon 0.2%. 2025
     summed chip TDP 7.53 GW. All match the note.
5. **Claim (race models):** Bueno de Mesquita, Dziuda and Polborn (2026) find restricting
   resources "may backfire".
   - Source: `buenodemesquita2026agirace`, BFI research brief (September 2026, Working Paper No.
     2026-71).
   - **Verdict: CONFIRMED.**
   - Evidence: "Industry consolidation, regulation facilitating commitment to slow down, and
     governments entering the race in a safe way improves welfare, while restricting resources may
     backfire."

Minor (not counted): summary item 1 calls 13.6 million "Epoch's estimate". It is the helper's sum
of Epoch's per-quarter medians, which the entry and the ledger say correctly.

## 07 compute governance

1. **Claim (the expiring k-of-n licence is prior work):** flexHEG specifies k-of-n multilateral
   approval, licences renewed periodically and enforced by an on-chip clock or cycle counter,
   approvers that are major states or blocs, and lifetimes "for example three months".
   - Sources: `petrie2025flexheg2`, arXiv:2506.03409 (James Petrie, Onni Aarne), and
     `aarne2025flexheg3`, arXiv:2506.15100 (Onni Aarne, James Petrie).
   - **Verdict: CONFIRMED.**
   - Evidence, Part II: "the update (or lack of update) be multilaterally approved by k of n
     parties, so that no single actor could unilaterally impose excessive restrictions"; "as
     measured by a secure real-time clock or cycle counter"; "if devices need a new license every
     three months"; "the presence of that hash in the history of a public blockchain could be
     used".
   - Evidence, Part III: "need to be signed by all of some set of approvers. The approvers would
     likely be major states or groups of states"; "a limited lifetime, for example three months";
     "If no new update has been installed before the lifetime runs out, the device locks down."
2. **Claim (against the memo's product of miss rates):** Baker et al. 2025: a regime's detection
   probability is about the minimum over subgoals; on-chip security is "severe, unsolved".
   - Source: `baker2025sixlayers`, arXiv:2507.15916v2 (Baker, Kulp, Marks, Brundage, Heim; 25 Jul
     2025).
   - **Verdict: CONFIRMED.**
   - Evidence (fn. 33): "a verification regime's probability of detecting a violation is
     approximately that of the subgoal with the lowest probability of detecting a violation. This
     is because a Prover only needs to circumvent one verification subgoal". Also: "On-chip
     verification faces severe, unsolved hardware security challenges (Table 6)".
3. **Claim (recent):** TEE.fail (IEEE S&P 2026) used a DDR5 interposer costing under $1,000 to
   break the CPU attestation that NVIDIA GPU confidential computing trusts.
   - Source: `chuang2026teefail`, tee.fail. The BibTeX names "47th IEEE Symposium on Security and
     Privacy (IEEE S&P '26)", authors Chuang, Seto, Berrios, van Schaik, Garman, Genkin.
   - **Verdict: CONFIRMED.**
   - Evidence: "it should cost you under $1000 to build a setup similar to ours". "extracted
     attestation keys can be used to compromise Nvidia's GPU Confidential Computing".
4. **Claim (ledger):** Shavit's chip sampling needs about 232 inspectors to catch a 1e25 FLOP run
   within 30 days with probability 0.9 (ledger `shavit-*`).
   - Source: `shavit2023chinchilla`, arXiv:2303.11341v2 (Yonadav Shavit).
   - **Verdict: CONFIRMED.**
   - Evidence (fn.): "detecting a Chinchilla-280B-sized run within T = 30 days of its completion
     anywhere on earth with 90% probability would require roughly 232,000 worldwide chip samples
     per year ... at least 1000 chips a year ... ~232 inspectors, slightly smaller than the 280
     active IAEA inspectors as of 2021". Table 1 Chinchilla row: "5.76e+23 6.67e+3 ... 132 1.33e+4
     1.33e+6".
5. **Claim (recent per-channel rate):** facility power metering detects at least 96% of
   undisguised runs at a 1% false-alarm rate, and at least 87% per day of the best disguise
   (simulated).
   - Source: `kimpson2026dcpower`, arXiv:2610.30182 (Kimpson, Baker, Graham; 19 Oct 2026).
   - **Verdict: CONFIRMED.**
   - Evidence (abstract): "On simulated datacentre power ... detects at least 96% of training runs
     against a declared inference workload, at a 1% false-alarm rate ... 2 Hz or faster". "hides
     training in up to 73% of five-minute observations, but over a day at least 87% of such runs
     are still caught, at a 0.1% false-alarm rate per run".

## 08 arms control

1. **Claim (against the memo's organising idea):** the IAEA's 2001 glossary says detection time
   "should correspond approximately to estimated conversion times", and its timeliness goals (1,
   3, 12 months) sit at or above conversion times (7-10 days for metal ...). The 2022 glossary
   prints no numeric timeliness goals (ledger `timeliness-goal-*`).
   - Sources: `iaea-glossary-2001`, www-pub.iaea.org/MTCD/Publications/PDF/NVS3_scr.pdf (2001
     Edition, International Nuclear Verification Series No. 3), and `iaea-glossary-2022`, the
     bnl.gov copy (ISBN 978-92-0-122222-0 pdf).
   - **Verdict: CONFIRMED.**
   - Evidence, 2001: "Under these circumstances, detection time should correspond approximately to
     estimated conversion times (see No. 3.13)". Goals: "One month for unirradiated direct use
     material, Three months for irradiated direct use material, One year for indirect use
     material". Table I: "Pu, HEU or 233U metal Order of days (7-10)".
   - Evidence, 2022: the same Table 2, and the phrase "IAEA timeliness detection goals" only in
     passing. Searches for "one month", "three months", "1 month" and "3 months" found no numeric
     goal.
2. **Claim (against the memo's challenge inspections):** no CWC challenge inspection has ever
   been requested (EC-109/DG.22, July 2025).
   - Source: `opcw-ec109-dg22`, opcw.org EC-109/DG.22 (Executive Council, 8-11 July 2025).
   - **Verdict: CONFIRMED.**
   - Evidence: "neither CIs nor IAUs have been requested by any State Party since the Convention's
     entry into force in 1997."
3. **Claim (recent):** the IAEA has not verified Iran's 60% stockpile since 10 June 2025.
   - Source: `aljazeera-2026-iran`, aljazeera.com, 27 Feb 2026.
   - **Verdict: CONFIRMED.**
   - Evidence: "Iran's stockpile of more than 400kg (882 pounds) of 60 percent enriched uranium
     that was last seen by nuclear watchdog inspectors last June 10."
4. **Claim (ledger):** CTBT seismic thresholds "well below 1 kt worldwide" (0.22 kt at 90%
   confidence with good propagation); DPRK's 2006 test was seen by 22 stations.
   - Source: `nrc-2012-ctbt`, DOI 10.17226/12849, chapter 2. curl got "Access Denied"; read
     through the web fetcher.
   - **Verdict: CONFIRMED.**
   - Evidence: Finding 2-5, "The threshold levels for IMS seismic detection are now well below 1 kt
     worldwide for fully coupled explosions". Table 2-2: "90 percent, entire world 3.8 0.22 kt 0.56
     kt". Box 2-3: "(22 stations reported, 14 primary; 8 auxiliary)", "Xe-133 was detected
     approximately 14 days following the detonation", "less than a kiloton".
5. **Claim (D4 is prior work):** Gan formalises the inequality as min{D + l, R} < T_catch, with
   catch-up time falling from 12 to 5.74 months over a 24-month pause.
   - Source: `gan-2026-clock`, arXiv:2611.04272v1 (Li Gan, 3 Nov 2026).
   - **Verdict: CONFIRMED.**
   - Evidence: "Restarting with a positive gap requires min{D + l, R(d)} < Tcatch(d; F(d), FB(d)),
     (12)". "The calibrated catch-up time falls from 12 months at the start to 8.61 months after 12
     months of compliance and to 5.74 months after 24 months." "A fixed response standard fails as
     catch-up time falls."

## 09 mechanism design

1. **Claim (deterrence without near-certain detection; prior art for Defection):** Gan's AI pause
   model deters with a 32% chance of detection within the response window, and the window shrinks
   as compute grows.
   - Source: `gan2026clock`, arXiv:2611.04272v1.
   - **Verdict: CONFIRMED.**
   - Evidence: "Deterrence does not require near-certain detection. At date zero the follower's
     window is 12 months, so deterrence needs m = 0.383/12 ~ 0.0319 findings per month. A secret
     advance is then detected within the window with probability 1 - e^-xi ~ 32 percent." Also
     "at the threshold a breakout still succeeds with probability e^-xi ~ 68 percent", and
     cooperation "supportable through month 18.9".
2. **Claim (coalition threshold is prior work):** the Berkeley hardwired-pause working paper
   defines breakout fleet thresholds, mentions per-coalition allowances, and picks T_B = 2 years as
   the time before "the rest of the world could react"; F_B = 180M H100e.
   - Source: `fithian2026hardwired`, hardwired-pause.ai/paper ("WORKING PAPER Version 1.0.2,
     October 26, 2026"; organisers William Fithian and Wesley H. Holliday, UC Berkeley).
   - **Verdict: CONFIRMED.**
   - Evidence: "attain its decisive advantage before the rest of the world could react to stop it
     ... we adopt a breakout time horizon of T_B = 2 years". "there might be per-coalition
     allowances in addition to per-state allowances". "F_B Fleet threshold for overt breakout at
     present-day utilization 180M H100e". The 2e27 FLOP, 0.21 and 12 inputs also reproduce note
     01's `hwp-*` rows.
3. **Claim (against the memo: channels do not multiply):** a mature many-channel oversight system
   detects about 31% of frauds.
   - Source: `dyck2017pervasive`, working paper PDF "How Pervasive Is Corporate Fraud?" (Dyck,
     Morse, Zingales).
   - **Verdict: CONFIRMED.**
   - Evidence: "To be precise, the detection rate is 31%". Abstract: "only one third of frauds are
     detected in normal times". AAER-based rate "55%".
4. **Claim (ledger):** the SEC has paid more than $2.2 billion to 444 whistleblowers since 2011
   (ledger `sec-awards-cumulative-2011-2024`).
   - Source: `sec2024whistleblower`, sec.gov/files/fy24-annual-whistleblower-report.pdf. curl
     received SEC's rate-limit page; the PDF came through the web fetcher and its text was
     extracted locally.
   - **Verdict: CONFIRMED.**
   - Evidence: "Annual Report to Congress for Fiscal Year 2024, November 15, 2024". "The SEC has
     awarded more than $2.2 billion to 444 individual whistleblowers since the Program's inception
     in 2011." Also: "awarded over $255 million ... to 47 individual whistleblowers".
5. **Claim (rewards move insiders):** with qui tam rewards, employees revealed 46.7% of healthcare
   frauds against 16.3% elsewhere; SOX protections alone did not help.
   - Source: `dyck2007whistle`, NBER WP 12882 PDF.
   - **Verdict: CONFIRMED.**
   - Evidence: "in healthcare ... 46.7% of frauds are brought to light by employees. This
     contrasts with only 16.3% of cases detected by employees in all other industries". "employee
     whistleblowing drops from 20.7% to 15.6% of cases after SOX".
6. **Claim (a known threshold turns a dilemma into coordination):** a known threshold was avoided
   by 8 of 10 groups; with its location uncertain, catastrophe was certain in 9 of 10.
   - Source: `barrett2012climate`, DOI 10.1073/pnas.1208417109 (PMC3491499). PNAS returned 403
     and PMC a browser check to curl; read through the web fetcher.
   - **Verdict: CONFIRMED.**
   - Evidence (Figure 2 caption as returned): "Catastrophe was avoided 8 of 10 times in the
     Certainty treatment", "10 of 10 times under Impact Uncertainty", and the probability of
     catastrophe was reduced below 100% "by only 1 of 10 groups under Threshold Uncertainty".
     Table 1 means: 150.9, 155.5, 77.2, 79.9.

Minor (not counted):
- Summary item 2 presents Gan's 32% without saying it comes from an illustrative calibration. The
  entry says so.
- The SEC report says "awarded", not "paid", and the figure is as of FY2024.

## 10 gameable evaluations

1. **Claim (D5's fixed budget is prior work and was abandoned):** RSP v1.0 defined ASL-3 with
   post-training "corresponding to less than 1% of the total training cost"; v2.0 removed it
   because "specific methodologies may become outdated".
   - Sources: `anthropic2023rsp`, RSP v1.0 PDF ("Effective September 19, 2023"), and
     `anthropic2026rsp`, RSP v3.4 PDF ("Effective July 8, 2026").
   - **Verdict: CONFIRMED.**
   - Evidence, v1.0: "We define an ASL-3 model as one that can either immediately, or with
     additional post-training techniques corresponding to less than 1% of the total training cost";
     "set the size of our safety buffer to 6x".
   - Evidence, v3.4 changelog: "replaced some specifics in our previous testing methodology (e.g.,
     using 1% of compute for elicitation or creating a 6x buffer) ... We have found that specific
     methodologies may become outdated when new research developments are introduced."
   - This also confirms note 01's summary item 3.
2. **Claim (what is missing from D5's prior art):** the AISI auditing game says "Our auditing game
   does not provide quantitative guarantees" and that it is "not possible to estimate quantitative
   detection metrics".
   - Source: `taylor2025auditinggames`, arXiv:2512.07810 (first author Jordan Taylor, 8 Dec 2025).
   - **Verdict: CONFIRMED.**
   - Evidence: both quotes are verbatim ("We have only a single blue team, and repetitions are not
     compatible with being blinded, so it is not possible to estimate quantitative detection
     metrics"). Also: "correctly classified only 1 of 5 models in phase one", and
     "training-based elicitation consistently elicited full performance from the sandbagging
     models, using only a single correct demonstration".
3. **Claim (recent, ledger):** hardened locks keep hard-task recall at 7.8% after weak-to-strong
   fine-tuning, against 71.2% for the base (ledger `robust-hard-recall-w2s`,
   `robust-untargeted-steps`).
   - Source: `finke2026robustorganisms`, arXiv:2610.26698 (Finke, Bhatnagar, Dodd, Ward, de
     Montjoye, Bethge, Phuong; 19 Oct 2026).
   - **Verdict: CONFIRMED.**
   - Evidence: Table 4 hard recall, Stage C row "0.0 0.0 0.0 0.0 3.3 2.6 7.8" (the last column is
     weak-to-strong). BB, the starting model, has base 71.2. Password-locked: agent 39.2,
     weak-to-strong 61.4. Text: "at most 14% hard recall up to 384 steps ... At 512 steps it returns
     to normal".
   - Worth adding to the note: 7.8% equals the trusted overseer model's own base recall (row TT,
     7.8).
4. **Claim (ledger):** anti-refusal training recovered 95.6% of a sandbagged Claude 3.5 Sonnet's
   score (degraded to 36.1%).
   - Source: `benton2024sabotage`, arXiv:2410.21514 (first author Joe Benton, 28 Oct 2024).
   - **Verdict: CONFIRMED.**
   - Evidence: "Degraded performance is 36.1% of original performance ... Recovered performance is
     95.6% of original performance".
5. **Claim (recent, D5 failure case):** exploration hacking holds through more than 500 GRPO
   steps.
   - Source: `jang2026explorationhacking`, arXiv:2604.28182 (Jang, Falck, Braun, Kirch, Menon,
     Moodley, Emmons, Zimmermann, Lindner; 30 Apr 2026).
   - **Verdict: CONFIRMED.**
   - Evidence: "the RL-locked model organism maintains suppressed performance well below this level
     for over 500 steps".

---

## What the research must not rely on

None of the 53 claims was NOT FOUND, UNREACHABLE or FABRICATED-LOOKING. Three were DISTORTED.

1. **Note 04: Cunningham et al.'s "rough estimate" of 9%** (summary item 2; ledger row
   `rsi-estimate-eps-rc`, about 0.09).
   - The source does not estimate eps_R,C at 9%. Correct statement: Cunningham et al. (arXiv
     2609.15802, Sec. 4.1) put the self-sustaining threshold at eps_R,C > 0.15 per ECI unit. Even
     taking a reported 4x uplift at face value, which they call "very likely to be an
     overestimate", it "would imply a 9% increase in productivity per unit of ECI, below the
     threshold".
   - The ledger row should be labelled an upper-end illustration, not an estimate.
2. **Note 05: the CTF as a team baseline for D1** (summary item 5; ledger rows
   `ctf-agent-*-2026`).
   - Correct statement: in a 24-hour university-level onsite CTF (17 new challenges), the human
     teams were mostly undergraduates (82.9% of study participants) and used an AI assistant
     during the event. The best autonomous agent ran in parallel on a separate, agent-only
     scoreboard. It scored 4,900 points, which would have placed second among the human teams, for
     $95.32 to $96.32 of API use (the paper gives both) and about a fifth of the human teams'
     cumulative runtime.
   - The paper does not date the event and was submitted on 24 Feb 2026, so "in 2026" should go.
   - It says nothing about expert organisations, which is what D1 compares against.
3. **Note 01: the quoted METR phrase "removed a compute-allocation verification component
   midway"** (entry `metr-anthropic-acceleration-2026`).
   - It is not in the source. Use the verbatim text: "Anthropic changed the scope of this project
     midway to exclude compute verification and instead just focus on AI R&D acceleration. This
     component was canceled before METR came to any substantive conclusions on compute usage at
     Anthropic."

The "Minor" items under each note are not errors of substance, but the paper should carry them:
- Rahman's 1e25 configuration reaches only 6.4e24 quality-adjusted.
- The 96% power-metering figure comes from simulated power.
- Only the first <10x of Gundlach et al.'s <100x comes from their ablations.
- The 30,000 Anthropic agents are on one internal platform.
- Gan's 32% comes from an illustrative calibration.
- The SEC figure is as of FY2024.
- Whitfill, Snodin and Becker's model rules out a software-only singularity by assumption.

**Overall faithfulness rate: 50 of 53 checked claims confirmed (94.3%); 3 distorted, 0 not found,
0 unreachable, 0 fabricated-looking; every checked identifier resolved to the stated work.**
