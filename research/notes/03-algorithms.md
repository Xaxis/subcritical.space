# Survey track 03: algorithms (scaling, algorithmic progress, train-inference exchange, data, self-play)

- Track: 03, algorithms. Feeds A1 to A5 of `research/00-memo.md`, and D2, D3, D4.
- Date: 2026-11-27. Every source below was opened on this date; where a page did not load or a
  number was not on the page, the entry says so.
- Scope: scaling laws (pretraining, data-constrained, observational), emergence and predictability,
  measured algorithmic progress and its critiques, the exchange between training and inference
  compute (search, sampling, reinforcement learning, distillation), the data stock and synthetic
  data, self-play and search and their transfer, and prior work on how fast a fixed compute cap
  leaks. Datasets for experiments E1 and E10 are listed at the end.

## Summary: what matters most for Subcritical

1. **Capability is predictable from compute in aggregate, poorly per task.** Chinchilla replicates
   once its fit is corrected (N_opt about C^0.51, about 20 tokens per parameter); about 100 public
   models fit a low-dimensional capability space; extrapolating BIG-Bench Hard one order of
   magnitude (OOM) in compute misses by about 6 percentage points (pp) on average, a single task by
   about 18 pp. Most claimed "emergence" is a metric artefact (two metrics carry over 92% of it).
2. **Headline algorithmic progress is fast but contested.** Compute for a fixed language-model loss
   halved every 8.4 months (95% CI 4.5 to 14.3) from 2012 to 2023; newer estimates run from about 3x
   a year (inference efficiency) to about 6x a year (range 1x to 50x). Against this: only under 100x
   of the claimed 22,000x reproduces at small compute, because the big gains (Transformer, Chinchilla
   rebalancing) are scale-dependent (Gundlach et al., NeurIPS 2026); selection bias could shift
   observational estimates by about 9x.
3. **This contradicts two memo assumptions.** D3's "physical compute times algorithmic efficiency"
   treats efficiency as one multiplier, but measured efficiency depends on scale and on the reference
   algorithm, so the leak rate of a cap depends on where the cap sits. And the pathway table's
   "unbounded scaling: not necessary, algorithms substitute" is weakened: 60 to 95% of language
   model gains came from compute, and compute explains 80 to 90% of frontier performance differences
   across 809 models.
4. **Inference leaks a training cap by roughly one OOM per technique, at a steep price.** Each
   technique trades about 1 OOM of training for somewhat more than 1 OOM of inference, over spans
   of 1 to 1.6 OOM (AlphaZero on Hex: 10x training saves about 15x test-time compute). The span
   grows only with a cheap verifier (3 OOM of training for 6 OOM of inference, extrapolated). On
   hard problems pretraining wins. The inference spent is itself compute the chip channel can see.
5. **Reinforcement learning (RL) with verifiable rewards scales, distillation leaks most cheaply.**
   o1, o3 and R1 improve smoothly with log compute (R1-Zero AIME 15.6% to 71.0%), but per one
   reading of the vendor charts 100x inference matches 10,000x RL, and RL may stay bounded by what
   the base model can already sample (contested). A 32B model distilled from R1 beats RL on the same
   base by 25.6 pp on AIME (72.6% against 47.0%).
6. **Data is not a hard wall before about 5e28 FLOP.** The effective public text stock is about
   4e14 tokens, fully used at a median of 2028 (range 2026 to 2032). Four epochs of repetition cost
   almost nothing, 16 still help. Collapse needs real data to be replaced; accumulating it avoids
   collapse; zero-data self-play works where a code executor checks answers.
7. **Narrow superintelligence by self-play exists, and it is brittle and transfers weakly.**
   AlphaZero was superhuman within 24 hours; AlphaProof reached IMO silver with multi-day compute.
   Yet adversarial policies beat superhuman KataGo over 97% of the time; most math-tuned models do
   not transfer their gains. The generation-verification gap grows with pretraining FLOP, so the
   capacity to self-improve is itself a function of scale (couples A1 with Y1 and D2).
8. **The cap-leak framing is prior work; a combined, quantified leak rate was not found.** Inference
   substituting for training (Villalobos and Atkinson 2023; Ord 2025: a 1e24 FLOP model with 10,000x
   inference might match a 1e27 FLOP model), thresholds needing to move down (Heim and Koessler
   2024), and a treaty with a fixed 1e24 FLOP cap that cites 3x a year algorithmic progress (Scher et
   al. 2025) all exist. We found no work that combines algorithmic progress at fixed compute,
   post-training enhancement, distillation and inference scaling into one leak rate tied to a
   detection time.
9. **The NanoGPT speedrun is a usable D2 testbed with caveats.** On fixed 8xH100 hardware the record
   fell from 2,700 s to 39.9 s in 27 months (67.7x; tokens from 10B to under 330M), but wall-clock
   mixes systems engineering with algorithms, the pace is very uneven, and AI-credited records so
   far are shallow to moderate (METR).

---

## A1: scaling laws and observational scaling

### kaplan2020scaling
- *Scaling Laws for Neural Language Models.* Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B.
  Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei. 2020.
  arXiv:2001.08361. Opened 2026-11-27 (abstract page and ar5iv HTML).
- Abstract: "The loss scales as a power-law with model size, dataset size, and the amount of compute
  used for training"; compute-efficient training means "training very large models on a relatively
  modest amount of data and stopping significantly before convergence."
- Fitted values (ar5iv): alpha_N = 0.076 (Eq. 1.1), alpha_D = 0.095 (Eq. 1.2), alpha_C^min = 0.050
  (Eq. 1.3; 0.054 in Eq. 6.4), N_c = 8.8e13 non-embedding parameters, D_c = 5.4e13 tokens,
  C_c^min = 3.1e8 PF-days. Compute-optimal allocation: N proportional to C^0.73 (Eq. 6.1), D to
  C^0.27, serial steps to C^0.03 (Table 6). Critical batch size B* about 2e8 tokens, alpha_B about
  0.21 (Eq. 1.4). Section 1.2 warns the constants depend on tokenisation and "don't have
  fundamental meaning."
- Bears on: A1 (historical baseline; its allocation was overturned by Chinchilla, see below), P1.

### hoffmann2022chinchilla
- *Training Compute-Optimal Large Language Models.* Jordan Hoffmann, Sebastian Borgeaud, Arthur
  Mensch, et al. (22 authors, DeepMind). 2022. arXiv:2203.15556. Opened 2026-11-27 (abstract).
- Over "400 language models ranging from 70 million to over 16 billion parameters on 5 to 500
  billion tokens"; "for every doubling of model size the number of training tokens should also be
  doubled." Chinchilla (70B, same compute as 280B Gopher, about 4x more data) reaches 67.5% on MMLU,
  over 7 points above Gopher. Earlier large models were "significantly undertrained."
- Bears on: A1; the Kaplan-to-Chinchilla rebalancing is one of the two scale-dependent innovations
  in gundlach2025origin.

### besiroglu2024replication
- *Chinchilla Scaling: A replication attempt.* Tamay Besiroglu, Ege Erdil, Matthew Barnett, Josh You.
  2024. arXiv:2404.10102 (v2). Opened 2026-11-27 (abstract and HTML).
- The Hoffmann Approach 3 estimates are "inconsistent with their first two estimation methods" and
  "report implausibly narrow confidence intervals"; intervals that narrow "would require over
  600,000 experiments" (they likely ran under 500). The refit is compatible with Approaches 1 and 2.
- Table 1 (240 points, bootstrap SE in brackets): E = 1.8172 (0.03), A = 482.01 (124.58),
  B = 2085.43 (1293.23), alpha = 0.3478 (0.02), beta = 0.3658 (0.02). Hoffmann's own: E = 1.6934,
  A = 406.4, B = 410.7, alpha = 0.3392, beta = 0.2849. Compute-optimal exponent a (N_opt about C^a):
  0.5126 (SE 0.02) against Hoffmann's 0.454; about 20 tokens per parameter against about 70 implied
  by Hoffmann's Approach 3 fit. With outliers kept (Table 3), a = 0.512 (SE 0.032), about 25.6
  tokens per parameter.
- Bears on: A1 (use these parameters, not Hoffmann's Approach 3), D3 (loss as a function of
  compute), E1.

### muennighoff2023dataconstrained
- *Scaling Data-Constrained Language Models.* Niklas Muennighoff, Alexander M. Rush, Boaz Barak,
  Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, Colin Raffel. 2023
  (v5 2025). arXiv:2305.16264. Opened 2026-11-27 (abstract and ar5iv). Venue not stated on the page.
- 400 runs, up to 900B tokens and 9B parameters. "Up to 4 epochs of repeated data yields negligible
  changes to loss compared to having unique data"; with more repetition "the value of adding compute
  eventually decays to zero." Fitted R_D* = 15.39 (about "15 repetitions (or 16 epochs)"),
  R_N* = 5.31 (Appendix A, Eq. 17, Table 1). Section 6: an 8.7B model at 4 epochs is only 0.5% worse
  in validation loss. Section 7: filling up to 50% of data with Python code showed no downstream
  loss; beyond that natural-language tasks degrade.
- Bears on: A4 (repetition stretches the data stock by about 4x at almost no cost, more at some
  cost), A1.

### ruan2024observational
- *Observational Scaling Laws and the Predictability of Language Model Performance.* Yangjun Ruan,
  Chris J. Maddison, Tatsunori Hashimoto. 2024. arXiv:2405.10938. NeurIPS 2024 spotlight (per the
  arXiv page). Opened 2026-11-27 (abstract).
- Builds scaling laws "from ~100 publically available models"; performance is "a function of a
  low-dimensional capability space," families differing in how efficiently they turn compute into
  it. Some emergent phenomena show "a smooth, sigmoidal behavior and are predictable from small
  models"; "the agent performance of models such as GPT-4 can be precisely predicted from simpler
  non-agentic benchmarks"; it can predict the effect of Chain-of-Thought and Self-Consistency.
- Bears on: A1 and E1 (the method E1 should reuse), D4/D5 (a line drawn on a capability axis can be
  forecast from cheaper benchmarks).

### owen2024predictable
- *How predictable is language model benchmark performance?* David Owen. 2024. arXiv:2401.04757.
  Opened 2026-11-27 (abstract).
- "Five orders of magnitude of compute scaling in eleven recent model architectures." Average
  BIG-Bench performance is "decently predictable"; extrapolating BIG-Bench Hard over one OOM gives
  mean absolute error about 6 pp; single tasks about 18 pp, still "significantly more predictable
  than chance."
- Bears on: A1, D4 (how far ahead of a checkpoint a forecast is trustworthy: about one OOM, with
  these errors), E1.

### ho2025rosetta
- *A Rosetta Stone for AI Benchmarks.* Anson Ho, Jean-Stanislas Denain, David Atanasov, Samuel
  Albanie, Rohin Shah. 2025. arXiv:2512.00193. Opened 2026-11-27 (abstract and HTML).
- "Stitches benchmarks together, putting model capabilities and benchmark difficulties on a single
  numerical scale," without assuming how capability evolves with time or compute. Results (HTML):
  capability C = k log F + b with k about 0.168 (Sec. 3.2.2, Eq. 2); frontier capability grows about
  0.55 units a year (95% CI 0.45 to 0.67), about a 4-month doubling of time horizon (Sec. 3.2.1,
  footnote 10); at fixed compute about 0.3 units a year (0.1 to 0.5 across families); implied
  algorithmic efficiency about 6x a year (range 1x to 50x across three LLaMA families), about 9x a
  year at the frontier of algorithmic quality (3x to 40x). Abstract: "higher, but broadly
  consistent with prior work." With k = 0.22 across all models (App. C.1.2), Delta-b = 0.27 a year
  (95% CI 0.20 to 0.34).
- Bears on: A1, A3, D3 (a capability scale with a stated compute slope is what D3 needs), E1.

## Emergence

### wei2022emergent
- *Emergent Abilities of Large Language Models.* Jason Wei, Yi Tay, Rishi Bommasani, et al. (16
  authors). 2022. arXiv:2206.07682. TMLR 2022. Opened 2026-11-27 (abstract).
- "We consider an ability to be emergent if it is not present in smaller models but is present in
  larger models"; such abilities cannot be predicted by extrapolating smaller models.
- Bears on: A1, D4 (if capabilities jump, a compute-keyed trigger can be overrun between
  checkpoints).

### schaeffer2023mirage
- *Are Emergent Abilities of Large Language Models a Mirage?* Rylan Schaeffer, Brando Miranda, Sanmi
  Koyejo. 2023. arXiv:2304.15004. Opened 2026-11-27 (abstract and ar5iv). The pages do not state a
  venue.
- Emergence arises from "the researcher's choice of metric": "nonlinear or discontinuous metrics
  produce apparent emergent abilities," continuous ones give "smooth, continuous predictable
  changes." Section 4: "2 metrics account for >92% of claimed emergent abilities" on BIG-Bench
  (Multiple Choice Grade, Exact String Match).
- Bears on: A1, D4, D5 (measure on continuous metrics; the threshold itself may still be a
  discontinuous metric such as task success).

### snell2024emergence
- *Predicting Emergent Capabilities by Finetuning.* Charlie Snell, Eric Wallace, Dan Klein, Sergey
  Levine. 2024. arXiv:2411.16035. Opened 2026-11-27 (abstract).
- "Finetuning LLMs on a given task can shift the point in scaling at which emergence occurs towards
  less capable models"; fits "emergence laws"; with small models it can "in some cases" predict
  emergence in models trained with up to 4x more compute (MMLU, GSM8K, CommonsenseQA, CoLA).
- Bears on: D5 (fine-tuning as elicitation moves a capability earlier in scale, which is both a
  forecasting tool and a warning that unelicited scores understate), D4.

## A3: algorithmic progress

### ho2024algorithmic
- *Algorithmic progress in language models.* Anson Ho, Tamay Besiroglu, Ege Erdil, David Owen, Robi
  Rahman, Zifan Carl Guo, David Atkinson, Neil Thompson, Jaime Sevilla. 2024. arXiv:2403.05812.
  NeurIPS 2024 (footer of the proceedings PDF). Opened 2026-11-27 (abstract, HTML, proceedings PDF).
- "Over 200 language model evaluations on Wikitext and Penn Treebank spanning 2012-2023"; compute
  for a fixed performance "has halved approximately every 8 months, with a 95% confidence interval
  of around 5 to 14 months." Section 3.1: preferred model 8.4 months (95% CI 4.5 to 14.3). Section
  4.1: "60-95% of the performance gains stem from compute scaling, while algorithms contribute only
  5-40%." Section 3.3: the Transformer is worth 7.2x compute (95% CI 3.3x to 45.7x). Section 3.2:
  "some algorithmic innovations will become obsolete over time as models are trained at larger
  scales." Code and data: github.com/epoch-research/lm-algorithmic-progress (MIT).
- Bears on: A3, D3 (the standard rate), the pathway table (compute still the larger share).

### erdil2022vision
- *Algorithmic progress in computer vision.* Ege Erdil, Tamay Besiroglu. 2022 (v4 2023).
  arXiv:2212.05153. Opened 2026-11-27 (abstract).
- "Compute-augmenting innovations halve compute requirements every nine months" (95% CI 4 to 25
  months), "more than twice as fast" as Moore's law; algorithms "roughly as important as the scaling
  of compute" (Shapley); progress is mostly compute-augmenting, not data-augmenting.
- Bears on: A3 (a second domain with a similar rate).

### hernandez2020efficiency
- *Measuring the Algorithmic Efficiency of Neural Networks.* Danny Hernandez, Tom B. Brown. 2020.
  arXiv:2005.04305. Opened 2026-11-27 (abstract).
- FLOP to reach AlexNet-level ImageNet performance "has decreased by a factor of 44x between 2012
  and 2019"; "doubling every 16 months"; "Moore's Law would only have yielded an 11x cost
  improvement."
- Bears on: A3 (the first fixed-target efficiency measurement; the design E10 copies).

### gundlach2025origin
- *On the Origin of Algorithmic Progress in AI: Evidence from Language Model Pre-Training.* Hans
  Gundlach, Alex Fogelson, Jayson Lynch, Ana Trisovic, Jonathan Rosenfeld, Anmol Sandhu, Neil
  Thompson. 2025 (v2 2026-11-10). arXiv:2511.21622. Accepted at NeurIPS 2026 (per the arXiv page).
  Opened 2026-11-27 (abstract).
- Against "a factor of 22,000 between 2012 and 2023" (Ho et al.), small-scale ablations "account for
  less than 10x," other innovations "less than 10x," so "less than 100x efficiency gains total in
  low-compute regimes." The gap is explained by "algorithms with scale-dependent efficiency
  improvements": LSTM against Transformer shows "exponent differences" in compute-optimal scaling,
  most other innovations "little scaling difference." Progress "at smaller training compute levels
  has been far slower than previously assumed"; "measures of algorithmic efficiency are strongly
  reference-dependent." (A search snippet gave 6,930x and 91% figures; they were not on the abstract
  page, so they are not used here.)
- Bears on: **A3 and D3, against the memo.** Algorithmic efficiency is not a scale-free multiplier.
  A cap set well below the frontier leaks more slowly than the 3x-a-year headline, while innovations
  that change the scaling exponent matter most near and above the cap. P4 (the footprint floor
  falls more slowly at small scale than the headline rate implies).

### whitfill2025selection
- *Note on Selection Bias in Observational Estimates of Algorithmic Progress.* Parker Whitfill. 2025.
  arXiv:2508.11033 (v2). Opened 2026-11-27 (abstract and HTML).
- If "compute choices are endogenous to algorithmic quality," estimates are "contaminated by
  selection bias." Section 2: "positive correlation leads to underestimating algorithmic progress,"
  "negative correlation leads to overestimation"; in a simulation with a true 45% a year, correlation
  0.5 gives 16.5% and -0.5 gives 93%. Section 1.3: experimental data coefficients are about 0.37
  against Ho et al.'s about 0.04, so as a "first-pass" estimate "algorithmic progress is overstated
  by around a factor of nine," with many other explanations possible.
- Bears on: A3, D3 (the uncertainty on the central rate is wider than the published CIs; E10's
  fixed-hardware, fixed-target design avoids this bias).

### mertens2026secretsauce
- *Is there "Secret Sauce" in Large Language Model Development?* Matthias Mertens, Natalia
  Fischl-Lanzoni, Neil Thompson. 2026 (v2 2026-05-03). arXiv:2602.07238. Opened 2026-11-27 (abstract).
- 809 models released 2022 to 2025, scaling regressions with release-date and developer fixed
  effects. "At the frontier, 80-90% of performance differences are explained by higher training
  compute"; away from the frontier, proprietary techniques and shared progress "substantially reduce
  the compute required"; within one firm, compute efficiency can differ by more than 40x.
- Bears on: the pathway table (scale dominates at the frontier), A3, O2.

### xiao2024densing
- *Densing Law of LLMs.* Chaojun Xiao, Jie Cai, Weilin Zhao, et al. (10 authors). 2024.
  arXiv:2412.04315. Opened 2026-11-27 (abstract).
- "Capacity density," "the ratio of the effective parameter size to the actual parameter size,"
  "doubles approximately every three months." A parameter-based, not compute-based, measure.
- Bears on: A3 (per-parameter efficiency, relevant to inference footprint and P4); not directly
  comparable to compute halving times.

### davidson2023ceg
- *AI capabilities can be significantly improved without expensive retraining.* Tom Davidson,
  Jean-Stanislas Denain, Pablo Villalobos, Guillem Bas. 2023. arXiv:2312.07413. Opened 2026-11-27
  (abstract).
- Defines "the compute-equivalent gain" (CEG). Most surveyed post-training enhancements are worth
  more than 5x training compute, some more than 20x; fine-tuning costs "typically <1% of the
  original training cost." Five types: "tool-use, prompting methods, scaffolding, solution
  selection, and data generation."
- Bears on: A2, D5 (elicitation budget), the cap leak (a one-time 5x to 20x leak at under 1% cost).

### barnett2025innovation
- *Compute Requirements for Algorithmic Innovation in Frontier AI Models.* Peter Barnett. 2025.
  arXiv:2507.10618. Opened 2026-11-27 (abstract).
- "We catalog 36 pre-training algorithmic innovations used in Llama 3 and DeepSeek-V3";
  "innovations using significant resources double in their requirements each year"; caps at GPT-2's
  training compute or at 8 H100s "could still have allowed for half of the cataloged innovations";
  "compute caps alone are unlikely to dramatically slow AI algorithmic progress."
- Bears on: D2, the recursive self-improvement pathway (algorithmic research survives a cap, for
  supporting the memo), but read with gundlach2025origin: the innovations that pay off most may be
  the ones whose value only shows at scale.

### moddednanogpt
- *Modded-NanoGPT* (the NanoGPT speedrun). Keller Jordan and contributors. Code repository, MIT.
  github.com/KellerJordan/modded-nanogpt. Opened 2026-11-27 (README, raw file downloaded).
- Task: "Train a neural network to ≤3.28 validation loss on FineWeb using 8x NVIDIA H100s"; the data
  pipelines must not change. Record 1: 45 minutes, llm.c baseline, 2024-05-28. Record 92: 0.665
  minutes, 2026-08-30. README: the algorithm now reaches the target "Under 40 seconds" and in "under
  330M tokens (the llm.c GPT-2 replication needed 10B)." Rules: p < 0.01 that mean loss is at most
  3.28; extra compile flags banned after record 21 (record 21 re-timed from 2.933 to 2.997 minutes).
  The technique list includes FP8 matmuls, kernel fusion and PyTorch upgrades (systems gains) next
  to Muon, architecture changes and multi-token prediction (algorithmic gains), and a hashed n-gram
  embedding table of "84.6M rows, 65B parameters."
- Derived here from the Epoch CSV of the same records (not a source number): 2,700 s to 39.9 s is
  67.7x in 2.26 years (wall-clock halving about 4.5 months), but uneven: about 15x in the first 8
  months, about 1.6x across 2025, about 2.9x from January to August 2026.
- Bears on: D2 (test (a): a public, fixed-compute record of research progress), A3, E10. Caveats for
  the ledger: wall-clock is not FLOP (FP8 raises FLOP/s without reducing FLOP); a 124M model at one
  target loss; the parameter count is not fixed (the n-gram table).

### shetty2026metrnanogpt
- *Evidence on AI R&D Progress from NanoGPT.* Manish Shetty (METR research note). 2026-04-21.
  metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/. Opened 2026-11-27.
- May 2024 to March 2026: 77 records from 36 contributors, "from 45 minutes to 1.43 minutes, a 31x
  speedup." "Shallow and moderate contributions together drove roughly 21x of the 31x" (so deep
  ones about 1.5x multiplicatively; my arithmetic). By provenance: imported 6.7x, adapted 3.0x,
  invented 1.6x. Four records from late 2025 to early 2026 credit an AI agent with a human, all
  judged shallow to moderate; "no public evidence of agents being run at scale on this kind of
  task." Footnote 3 cites external analyses: "similar annual rates for FLOP efficiency
  (~1.6-1.7x/year)"; Whitfill "707x total wall-clock speedup on fixed hardware"; Gundlach "~75x in
  cost reduction" (for the gap since the 2019 GPT-2 training).
- Bears on: D2 (the closest public measurement of AI contribution to algorithmic research; so far
  small), A3, E10.

## A2: the exchange between training and inference compute, RL and distillation

### jones2021boardgames
- *Scaling Scaling Laws with Board Games.* Andy L. Jones. 2021. arXiv:2104.03113. Opened 2026-11-27
  (abstract and ar5iv).
- AlphaZero on Hex. "The test-time and train-time compute available to an agent can be traded off
  while maintaining performance." Section IV-C, Fig. 9: "for each additional 10× of train-time
  compute, about 15× of test-time compute can be eliminated," "linear in log-compute" (about 1.18
  OOM of test-time per OOM of training; my arithmetic). Section IV-A, Table III: minimum compute
  for perfect play grows about 7x per board-size increment.
- Bears on: A2 (the cleanest measured exchange rate, in a closed, verifiable domain), A5.

### villalobos2023tradeoff
- *Trading off compute in training and inference.* Pablo Villalobos, David Atkinson. Epoch AI, 2023-07-28.
  epoch.ai/publications/trading-off-compute-in-training-and-inference. Opened 2026-11-27. No DOI.
- "Each technique makes it possible to save around 1 OOM of compute in either training or
  inference, in exchange for increasing the other factor by somewhat more than 1 OOM." Spans: scaling
  policy 1.2 OOM training / 0.7 OOM inference (cannot save training); MCTS 1.6 / 1.6 (span shrinks
  to zero near perfect play); pruning about 1 / 1; repeated sampling with cheap verification 3 OOM
  training / 6 OOM inference (grows with scale; extrapolated, low confidence); repeated sampling with
  expensive verification 1 / 1.45; chain of thought not quantified. Governance: augmented inference
  "can let some actors reach higher capabilities at a smaller deployment scale."
- Bears on: **A2, prior work for the memo's framing.** The leak through inference is bounded per
  technique except where verification is cheap.

### snell2024testtime
- *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters.*
  Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar. 2024. arXiv:2408.03314. Opened 2026-11-27
  (abstract and ar5iv).
- Adaptive "compute-optimal" test-time scaling improves efficiency "by more than 4x" over best-of-N;
  FLOPs-matched, a smaller model can "outperform a 14x larger model" where its success rate is
  "somewhat non-trivial." Section 7: "test-time compute can easily cover up for additional
  pretraining" on easy and medium questions; on hard ones "pretraining is likely more effective";
  with inference-to-pretraining token ratio R = 0.16 test-time wins, with R = 22 pretraining often
  wins; the two are "not 1-to-1 exchangeable."
- Bears on: A2 (the exchange is difficulty-dependent: inference cannot buy capabilities the base
  model does not nearly have, which is where D1 lives).

### wu2024inferencescaling
- *Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving
  with Language Models.* Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang. 2024 (v3
  2025). arXiv:2408.00724. Opened 2026-11-27 (abstract).
- "Scaling inference compute with inference strategies can be more computationally efficient than
  scaling model parameters"; Llemma-7B with tree search "consistently outperforms the Llemma-34B
  model across all tested inference strategies" on MATH.
- Bears on: A2.

### brown2024monkeys
- *Large Language Monkeys: Scaling Inference Compute with Repeated Sampling.* Bradley Brown, Jordan
  Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, Azalia Mirhoseini. 2024.
  arXiv:2407.21787 (v3). Opened 2026-11-27 (abstract).
- SWE-bench Lite solved rises from 15.9% (1 sample) to 56% (250 samples), above the "single-sample
  state-of-the-art of 43%." Coverage scales "over four orders of magnitude," "often log-linear,"
  modelled by "an exponentiated power law." Without automatic verifiers, majority voting and reward
  models "plateau beyond several hundred samples."
- Bears on: A2, A4 (the verifier decides whether inference keeps paying; code and formal proofs are
  the open door).

### sardana2024beyondchinchilla
- *Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws.* Nikhil
  Sardana, Jacob Portes, Sasha Doubov, Jonathan Frankle. 2023 (v3 2025). arXiv:2401.00448. ICML 2024.
  Opened 2026-11-27 (abstract).
- With "reasonably large inference demand (~1B requests)," train "smaller and longer than
  Chinchilla-optimal"; across 47 models, quality keeps improving at up to 10,000 tokens per
  parameter.
- Bears on: A2, P1, D3 (deployed models sit off the Chinchilla frontier, so training FLOP alone
  under-counts the capability per parameter).

### openai2024o1
- *Learning to reason with LLMs.* OpenAI. 2024-09-12. openai.com/index/learning-to-reason-with-llms/.
  Opened 2026-11-27.
- "The performance of o1 consistently improves with more reinforcement learning (train-time compute)
  and with more time spent thinking (test-time compute)"; x-axes are "compute (log scale)." AIME
  2024: 74% with one sample, 83% with consensus over 64, 93% re-ranking 1,000 samples.
- Bears on: A2 (vendor claim; axes unlabelled in absolute terms).

### openai2025o3
- *Introducing OpenAI o3 and o4-mini.* OpenAI. 2025-04-16. openai.com/index/introducing-o3-and-o4-mini/.
  Opened 2026-11-27.
- "Large-scale reinforcement learning exhibits the same 'more compute = better performance' trend";
  they "pushed an additional order of magnitude in both training compute and inference-time
  reasoning."
- Bears on: A2 (vendor claim).

### deepseek2025r1
- *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.* DeepSeek-AI.
  2025. arXiv:2501.12948; Nature 645, 633-638 (2025), doi:10.1038/s41586-025-09422-z. Opened
  2026-11-27 (abstract and v1 HTML).
- "The reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL)."
  v1 HTML: R1-Zero AIME 2024 pass@1 from 15.6% to 71.0% during RL, 86.7% with cons@64 (Sec. 2.2.4,
  Table 2); response length grows with training. Distilled models (Sec. 3.2, Table 5): Qwen-7B
  55.5%, 14B 69.7%, 32B 72.6%. Section 4.1, Table 6: large-scale RL on Qwen-32B-Base reaches 47.0%,
  so distillation from a stronger model beats RL on the same small base.
- Bears on: A2, A3 (distillation as the cheapest transfer of capability across a cap), D6 (access to
  a stronger model's outputs is an input to the next model).

### yue2025rlvr
- *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?*
  Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang, et al. 2025 (v5
  2025-11-24). arXiv:2504.13837. NeurIPS 2025 oral (per the arXiv page). Opened 2026-11-27.
- RL with verifiable rewards "does not elicit fundamentally new reasoning patterns"; "the base models
  achieve a higher pass@k score when k is large"; abilities "originate from and are bounded by the
  base model"; distillation "can introduce new reasoning patterns from the teacher."
- Bears on: A2, A4, D2 (if RL only sharpens what pretraining put there, RL-based self-improvement
  is bounded by base-model compute).

### liu2025prorl
- *ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models.*
  Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, Yi Dong. 2025.
  arXiv:2505.24864. Opened 2026-11-27 (abstract).
- "RL-trained models consistently outperform base models across a wide range of pass@k
  evaluations," including where base models fail at any k; gains correlate "with task competence of
  base model and training duration."
- Bears on: A2 (counter-evidence to yue2025rlvr; the question is open).

### khatri2025scalerl
- *The Art of Scaling Reinforcement Learning Compute for LLMs.* Devvrit Khatri, Lovish Madaan, Rishabh
  Tiwari, et al. (9 authors). 2025. arXiv:2510.13786. Opened 2026-11-27 (abstract).
- Over 400,000 GPU-hours; they "fit sigmoidal compute-performance curves for RL training"; most
  design choices change compute efficiency "without materially shifting the asymptote"; one run
  scaled to 100,000 GPU-hours follows the predicted trajectory.
- Bears on: A2, A3 (RL gains saturate per recipe: an asymptote, not a power law).

### ord2025rlscale
- *How Well Does RL Scale?* Toby Ord. 2025-10-20. tobyord.com/writing/how-well-does-rl-scale. Essay.
  Opened 2026-11-27.
- From the o1 charts: inference 100x takes AIME "from roughly 20% to 80%"; RL 100x "only improved
  performance from about 33% to 66%"; "going from 20 to 80 would require scaling up the RL training
  compute by 10,000x." o1 to o3: "a 10x scaling of RL is required to get the same performance boost
  as a 3x scaling of inference." Self-described "educated guess" from vendor charts without axis
  numbers.
- Bears on: A2 (an estimate, not a measurement; RL is a weak lever per unit compute at current
  scale).

### busbridge2025distillation
- *Distillation Scaling Laws.* Dan Busbridge, Amitis Shidani, Floris Weers, Jason Ramapuram, Etai
  Littwin, Russ Webb. 2025. arXiv:2502.08606. ICML 2025. Opened 2026-11-27 (abstract).
- "In settings involving many students or an existing teacher, distillation outperforms supervised
  learning up to a compute level that scales predictably with student size"; "if only one student
  is to be distilled and a teacher also requires training, supervised learning is generally
  preferable."
- Bears on: A2, D6 (an existing uncapped teacher is exactly the case where distillation pays; the
  protocol must treat teacher outputs as a controlled input).

### song2024gap
- *Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models.* Yuda Song,
  Hanlin Zhang, Carson Eisenach, Sham Kakade, Dean Foster, Udaya Ghai. 2024 (v2 2025).
  arXiv:2412.02674. ICLR 2025. Opened 2026-11-27 (abstract).
- Self-improvement is "largely governed by a quantity which we formalize as the
  generation-verification gap"; "a variant of the generation-verification gap scales monotonically
  with the model pre-training flops."
- Bears on: A4, Y1, D2 (self-improvement capacity rises with pretraining compute, so a compute cap
  also caps the loop gain; a coupling the memo's Y3 should include).

## A4: data limits and synthetic data

### villalobos2022data
- *Will we run out of data? Limits of LLM scaling based on human-generated data.* Pablo Villalobos,
  Anson Ho, Jaime Sevilla, Tamay Besiroglu, Lennart Heim, Marius Hobbhahn. 2022 (v2 2024).
  arXiv:2211.04325. Opened 2026-11-27 (abstract and HTML). Venue not stated on the page.
- Datasets reach the public text stock "between 2026 and 2032," "slightly earlier if models are
  overtrained." HTML: effective stock about 4e14 tokens (Fig. 1, Sec. 2.5); median full use 2028
  at about 5e28 FLOP compute-optimal, about 6e27 FLOP and a year earlier if 5x overtrained (Sec.
  2.5, Figs. 5 and 6); indexed web 510T tokens (95% CI 130T to 2,100T), Common Crawl 130T (100T to
  260T), whole web 3,100T (1,900T to 5,200T) (Table 1).
- Bears on: A4, P1 (data does not bind before frontier runs of order 1e28 FLOP).

### shumailov2024collapse
- *AI models collapse when trained on recursively generated data.* Ilia Shumailov, Zakhar Shumaylov,
  Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal. Nature 631, 755-759 (2024).
  doi:10.1038/s41586-024-07566-y. Opened 2026-11-27 via PubMed Central (nature.com redirected to a
  login).
- "Indiscriminate use of model-generated content in training" causes defects; "tails of the
  original content distribution disappear"; shown in LLMs, VAEs and GMMs. OPT-125m on wikitext2:
  with no original data after generation 0, perplexity rose from about 20 to 28; keeping 10% of the
  original data gave only minor degradation.
- Bears on: A4 (collapse needs replacement of real data).

### gerstgrasser2024accumulate
- *Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic
  Data.* Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, et al. (14 authors). 2024.
  arXiv:2404.01413. Opened 2026-11-27 (abstract).
- Replacement "does indeed tend towards model collapse"; "accumulating the successive generations of
  synthetic data alongside the original real data avoids model collapse"; under accumulation "the
  test error has a finite upper bound independent of the number of iterations" (linear model).
- Bears on: A4 (against reading shumailov2024collapse as a data wall).

### zhao2025absolutezero
- *Absolute Zero: Reinforced Self-play Reasoning with Zero Data.* Andrew Zhao, Yiran Wu, Yang Yue, et
  al. (11 authors). 2025 (v3 2025-10-16). arXiv:2505.03335. Opened 2026-11-27 (abstract).
- "A single model learns to propose tasks that maximize its own learning progress" "without relying
  on any external data," using "a code executor to both validate proposed code reasoning tasks and
  verify answers"; reports SOTA on coding and math against zero-setting models that use "tens of
  thousands of in-domain human-curated examples."
- Bears on: A4, A5, D6 (with a verifier, the data input to the next model can close without a human
  gate).

## A5: self-play, search and transfer

### silver2017alphagozero
- *Mastering the game of Go without human knowledge.* David Silver, Julian Schrittwieser, Karen
  Simonyan, et al. Nature 550, 354-359 (2017). doi:10.1038/nature24270. Opened 2026-11-27 via Europe
  PMC (the PubMed page showed only a cookie notice).
- "An algorithm based solely on reinforcement learning, without human data, guidance or domain
  knowledge beyond game rules"; "AlphaGo becomes its own teacher"; "winning 100-0 against the
  previously published, champion-defeating AlphaGo."
- Bears on: A5 (narrow superhuman capability from a closed loop with a perfect verifier).

### silver2018alphazero
- *A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play.*
  David Silver, Thomas Hubert, Julian Schrittwieser, et al. Science 362, 1140-1144 (2018).
  doi:10.1126/science.aar6404; preprint arXiv:1712.01815. Opened 2026-11-27 (arXiv abstract; Science
  record via Europe PMC).
- "Starting from random play and given no domain knowledge except the game rules, AlphaZero
  convincingly defeated a world champion program"; preprint: superhuman "within 24 hours."
- Bears on: A5, Y2 (a closed loop that ran away inside a closed domain, then saturated).

### schrittwieser2020muzero
- *Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model.* Julian Schrittwieser,
  Ioannis Antonoglou, Thomas Hubert, et al. 2019. arXiv:1911.08265; Nature,
  doi:10.1038/s41586-020-03051-4 (DOI as listed on the arXiv page). Opened 2026-11-27 (abstract).
- A learned model that "predicts the quantities most directly relevant to planning"; works "without
  any knowledge of the game rules"; new state of the art on 57 Atari games; matches AlphaZero on Go,
  chess and shogi.
- Bears on: A5 (search no longer needs a given simulator, only a learned one).

### trinh2024alphageometry
- *Solving olympiad geometry without human demonstrations.* Trieu H. Trinh, Yuhuai Wu, Quoc V. Le,
  He He, Thang Luong. Nature 625, 476-482 (2024). doi:10.1038/s41586-023-06747-5. Opened 2026-11-27
  via Europe PMC.
- "Synthesizing millions of theorems and proofs"; solves 25 of 30 recent olympiad problems against
  10 for the previous best, "approaching the performance of an average International Mathematical
  Olympiad (IMO) gold medallist."
- Bears on: A4, A5 (synthetic data plus a symbolic verifier replaces human data).

### hubert2026alphaproof
- *Olympiad-level formal mathematical reasoning with reinforcement learning.* Thomas Hubert, Rishi
  Mehta, Laurent Sartran, et al. Nature 651, 607-613 (2026). doi:10.1038/s41586-025-09833-y. Opened
  2026-11-27 via Europe PMC.
- AlphaZero-inspired agent "training on millions of auto-formalized problems" in Lean; "test-time RL,
  a method of generating and learning from millions of related problem variants at inference time";
  at IMO 2024 "solved three out of the five non-geometry problems," with AlphaGeometry 2 a silver
  medal equivalent, "achieved with multi-day computation."
- Bears on: A2 (test-time RL blurs training and inference: a cap on training FLOP alone misses it),
  A5.

### wang2023katago
- *Adversarial Policies Beat Superhuman Go AIs.* Tony T. Wang, Adam Gleave, Tom Tseng, et al. (11
  authors). 2022 (v4 2023). arXiv:2211.00241. ICML 2023 (per the arXiv comments). Opened 2026-11-27.
- "A >97% win rate against KataGo running at superhuman settings"; the attack "transfers zero-shot to
  other superhuman Go-playing AIs"; humans can "implement it without algorithmic assistance"; the
  vulnerability "persists even in KataGo agents adversarially trained to defend."
- Bears on: A5, F3 (narrow superhuman is not robust superhuman; relevant to what D1 should demand).

### huan2026mathtransfer
- *Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM
  Reasoning.* Maggie Ziyu Huan, Yuetai Li, Tianyu Zheng, et al. (9 authors). 2025 (v2 2025-10-20).
  arXiv:2507.00432; ICML 2026, PMLR 306:46232-46268. Opened 2026-11-27 (arXiv and PMLR pages).
- Over 20 open reasoning-tuned models: "most models that succeed in math fail to transfer their gains
  to other domains"; on Qwen3-14B with math-only data, "reinforcement learning (RL)-tuned models
  generalize well across domains" while "supervised fine-tuning (SFT)-tuned models often forget
  general capabilities."
- Bears on: A5, F3 (transfer from verifiable to open domains is weak on average, method-dependent).

### liu2025spiral
- *SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn
  Reinforcement Learning.* Bo Liu, Leon Guertler, Simon Yu, et al. (12 authors). 2025 (v3
  2026-03-02). arXiv:2506.24119. ICLR 2026. Opened 2026-11-27 (abstract).
- Self-play on games yields reasoning that "transfer broadly," improving "by up to 10%" across 8
  benchmarks on 4 models; beats "supervised fine-tuning on 25,000 expert game trajectories."
- Bears on: A5 (some transfer from closed games to open reasoning, modest in size).

## Prior work on compute thresholds and the cap leak

### ord2025inferencegov
- *Inference Scaling Reshapes AI Governance.* Toby Ord. 2025. arXiv:2503.05705. Opened 2026-11-27
  (abstract).
- Deployment-time inference scaling would "derail the current paradigm of AI governance via training
  compute thresholds," "lower the importance of open-weight models"; inference scaling during
  training ranges from "a revitalisation of pre-training scaling" to "a form of recursive
  self-improvement via iterated distillation and amplification."
- Bears on: A2, D3, D4 (prior work for the leak framing).

### ord2025govaireport
- *Inference Scaling and AI Governance* (technical report). Toby Ord. Centre for the Governance of
  AI, October 2025. governance.ai/research-paper/inference-scaling-and-ai-governance; PDF opened and
  text extracted 2026-11-27.
- Citing trade-off work (its footnote 6): "increasing inference compute on the task at hand by a
  factor of 10 can improve performance as much as increasing pre-training compute by 3-10x," with
  gains "often plateauing after scaling up inference-at-deployment by a few orders of magnitude."
  Illustration (around p. 10): "a model trained with 10^24 FLOP might use 10,000 times more inference
  compute to perform at the level of a model trained with 10^27 FLOP"; o3 "demonstrated the ability
  to use 10,000x more compute than ... o1-mini." Appendix: total compute C about ND + C_post + dNI;
  deployment overtakes pre-training when generated tokens dI exceed training tokens D.
- Bears on: A2, D3, D4, P1 (closest prior statement of the inference leak, in numbers but not as a
  rate).

### heim2024thresholds
- *Training Compute Thresholds: Features and Functions in AI Regulation.* Lennart Heim, Leonie
  Koessler. 2024 (v2). arXiv:2405.10799. Opened 2026-11-27 (abstract and HTML).
- Training compute is the best current "initial filter." Executive summary: efficiency gains are
  "gradually reducing the amount of training compute required," "a reason to consider adjusting the
  compute threshold downwards over time"; Sec. 6.3 calls the up-or-down question "a regulatory
  dilemma." Sec. 6.1 suggests "a safety buffer of an order of magnitude or so" for post-training
  enhancement and expects "a limit to the increase in model capabilities that can be gained from
  post-training enhancements." Sec. 2 argues against counting post-training compute.
- Bears on: D4, the cap leak (prior work; qualitative).

### pilz2023diffusion
- *Increased Compute Efficiency and the Diffusion of AI Capabilities.* Konstantin Pilz, Lennart Heim,
  Nicholas Brown. 2023 (v2 2024). arXiv:2311.15377. Opened 2026-11-27 (abstract and HTML).
- "An access effect increases the number of actors who can train models to a given performance over
  time," while "a performance effect" raises what each can reach. HTML: accelerator price-performance
  doubled about every two years 2006 to 2021 (Sec. 1.2); ImageNet 93% cost fell from over $1,000 in
  2017 to $5 in 2021 (Sec. 1.1).
- Bears on: P4, D3, O1 (prior work on the diffusion side of the leak).

### hooker2024thresholds
- *On the Limitations of Compute Thresholds as a Governance Strategy.* Sara Hooker. 2024 (v2).
  arXiv:2407.05694. Opened 2026-11-27 (abstract).
- The compute-risk relationship is "highly uncertain and rapidly changing"; thresholds overestimate
  "our ability to predict what abilities emerge at different scales."
- Bears on: D4 (critique of compute triggers; argues for the memo's choice of a time-based line).

### barnett2026closingwindow
- *The Closing Window: How Governments Could Lose Their Ability to Restrain Advanced AI.* Peter
  Barnett. 2026. arXiv:2608.05173. Opened 2026-11-27 (abstract and HTML).
- Pathways to a point of no return: hardware proliferation, continued algorithmic progress, release
  of dangerous models; "difficult or impossible to know when we will hit a 'point of no return'."
  Sec. 3.2.2 gives a range of "3× to 60× per year" for the fall in compute needed per capability,
  with no calculation of when a cap fails; Sec. 3.2.3 says dangerous inference "may only be feasible
  on large clusters that are already subject to monitoring."
- Bears on: D3, D4 (prior work on the window; no quantified leak rate).

### scher2025agreement
- *An International Agreement to Prevent the Premature Creation of Artificial Superintelligence.*
  Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta. 2025 (v3 2026-05-08). arXiv:2511.10783.
  Opened 2026-11-27 (abstract and HTML).
- Caps training "operationalized by FLOP thresholds," "verified through the tracking of AI chips";
  dangerous research "stopped via legal prohibitions." HTML Sec. 4: Strict Threshold 1e24 FLOP,
  Monitored Threshold 1e22 FLOP, clusters "greater than 16 H100-equivalents" prohibited outside
  monitored facilities; thresholds "can be modified" but no schedule. Sec. 5: compute per capability
  "drops by 3×" a year; the Transformer is "around two years of progress on its own"; "controls on
  inference would require more invasive measures."
- Bears on: the protocol as a whole (closest prior design found from this track), D4, the cap leak.

### ansari2026inferencegov
- *Beyond Training: A Feasibility Taxonomy for Inference-Time AI Governance.* Samar Ansari. 2026.
  arXiv:2609.10105. Opened 2026-11-27 (abstract).
- Capability "increasingly migrates to the deployment stage"; 20 inference-time mechanisms, "fifteen
  of the twenty ... have commercial technical substrates in production today"; "no mechanism rates
  adequate against a high-capability state-level deployer." No numbers on inference substituting
  for training.
- Bears on: verification of inference (other tracks), A2.

### gundlach2025meek
- *Meek Models Shall Inherit the Earth.* Hans Gundlach, Jayson Lynch, Neil Thompson. 2025.
  arXiv:2507.07931. Opened 2026-11-27 (abstract).
- "Diminishing returns to compute scaling will lead to a convergence of AI model capabilities";
  well-resourced firms "will eventually have little advantage in capabilities."
- Bears on: O2, D3 (if returns to compute flatten, a cap gap closes faster in capability terms than
  in compute terms).

## Inference efficiency and diffusion of frontier capability

### gundlach2025priceprogress
- *The Price of Progress: Price Performance and the Future of AI.* Hans Gundlach, Jayson Lynch,
  Matthias Mertens, Neil Thompson. 2025 (v2 2026-03-23). arXiv:2511.23455. Opened 2026-11-27
  (abstract).
- Price at a fixed benchmark level fell "around 5× to 10× per year"; with open models only and
  hardware price declines divided out, "algorithmic efficiency progress is around 3× per year"; the
  price of running frontier models is "rising between 3× to 18× per year."
- Bears on: A3 (inference-side efficiency), P1 (inference throughput needed per capability falls
  about 3x a year).

### cottier2025inferenceprices
- *LLM inference prices have fallen rapidly but unequally across tasks.* Ben Cottier, Ben Snodin,
  David Owen, Tom Adamczewski. Epoch AI Data Insight, 2025-03-12.
  epoch.ai/data-insights/llm-inference-price-trends. Opened 2026-11-27.
- Prices at fixed performance fell "ranging from 9x to 900x per year"; GPT-4-level GPQA Diamond "fell
  by 40x per year"; fastest drops recent, "less clear that those will persist." Prices, not FLOP:
  includes hardware and competition.
- Bears on: A3, O2.

### somala2025consumergpu
- *Frontier AI performance becomes accessible on consumer hardware within a year.* Venkat Somala, Luke
  Emberson. Epoch AI Data Insight, 2025-08-15. epoch.ai/data-insights/consumer-gpu-model-gap. Opened
  2026-11-27.
- Open models that fit one consumer GPU match the frontier with "an average lag between 6-12 months":
  GPQA-Diamond 7.4 months, MMLU-Pro 7.3, AA Intelligence Index 6.3, LM Arena 12.4. RTX 5090 limit
  about 40B parameters at 4-bit. "The 'real-world' lag may be somewhat longer."
- Bears on: D3, D4, P4 (deployment-scale capability reaches unmonitorable hardware within a year;
  the breakout question then rests on training and on the next increment, not on running).

### edwards2026openclosed
- *Open models lag state-of-the-art closed models by 4 months.* Jack Edwards, Luke Emberson. Epoch AI
  Data Insight, 2026-05-29. epoch.ai/data-insights/open-closed-eci-gap. Opened 2026-11-27.
- Since January 2026 the best open-weight models lag closed ones by "an average of four months" on the
  Epoch Capabilities Index; "The average ECI gap was 8 points."
- Bears on: O2, D3.

### epoch2026trends
- *Trends in AI.* Epoch AI. Updated 2026-11-05. epoch.ai/trends. Opened 2026-11-27.
- "Training compute for frontier language models has been growing at 5× per year since 2020" (90% CI
  4x to 6x; doubling 5.2 months, CI 4.6 to 6.0). AI chip performance per dollar 1.49x a year since
  2023 (90% CI 1.36x to 1.66x). The page as fetched did not show an algorithmic progress figure.
- Bears on: P1, A3 (the frontier moves about 5x a year in physical compute; the cap's distance to
  the frontier grows by that while algorithms shrink it from below).

## Datasets for experiments E1 and E10 (all opened and, where noted, downloaded 2026-11-27)

### epoch2026aimodels
- *Data on AI models.* Epoch AI. Updated 2026-11-24. epoch.ai/data/ai-models. CC BY 4.0. Opened and
  CSVs downloaded 2026-11-27: "over 3,700" models; all_ai_models.csv has 3,731 rows with training
  compute, parameters, dataset size, post-training compute, hardware and a WikiText/Penn Treebank
  column. Bears on: E1, A1, A3.

### epoch2026benchmarks
- *Capabilities and benchmarking data.* Epoch AI. Updated 2026-11-27. epoch.ai/benchmarks/use-this-data.
  CC BY 4.0; "Data from external projects keeps its original license." One ZIP download. Opened
  2026-11-27. Bears on: E1.

### epoch2025eci
- *Epoch Capabilities Index.* Epoch AI. 2025 (BibTeX date October 2025). epoch.ai/benchmarks/eci.
  Combines "over 50 distinct benchmarks" with per-benchmark logistic difficulty and slope; scaled so
  Claude 3.5 Sonnet = 130 and GPT-5 = 150; a model needs at least 4 evaluations. CC BY 4.0. Opened
  2026-11-27. Bears on: E1, D4 (a candidate capability axis).

### epoch2026speedrundata
- *NanoGPT speedrun record training time.* Epoch AI, AI impacts observatory. Updated 2026-10-06.
  epoch.ai/data/nanogpt-speedrun-record-time. The record fell "from 2,700 seconds (45 minutes) in May
  2024 to 114 seconds by the end of 2025, and to 40 seconds by August 2026"; no fitted rate on the
  page. CSV downloaded 2026-11-27 (92 rows). CC BY 4.0 for Epoch's processing. Bears on: E10, D2.

### ho2024algorithmiccode
- *lm-algorithmic-progress.* Epoch AI. 2024. github.com/epoch-research/lm-algorithmic-progress. The
  code and data linked from ho2024algorithmic's first page; MIT per the GitHub API (metadata checked
  2026-11-27, contents not opened). Bears on: E1, E10 (rerun the 2024 fit).

### openllmleaderboard2025contents
- *Open LLM Leaderboard contents.* Hugging Face. Last modified 2025-03-20.
  huggingface.co/datasets/open-llm-leaderboard/contents. 4.58k rows with IFEval, BBH, MATH Lvl 5, GPQA,
  MUSR, MMLU-PRO, parameter count and CO2 cost. No dataset licence is declared on the card or via the
  Hub API (only a per-model "Hub License" column). Opened 2026-11-27. Bears on: E1 (only after the
  licence is resolved).

| Dataset | URL | What | Licence | Checked |
|---|---|---|---|---|
| Epoch AI, Data on AI models (key `epoch2026aimodels`) | https://epoch.ai/data/all_ai_models.csv ; notable_ai_models.csv ; frontier_ai_models.csv ; large_scale_ai_models.csv ; ai_models.zip (same path) | Training compute, parameters, dataset size, dates, hardware, post-training compute, a WikiText/Penn Treebank column | CC BY 4.0 | Downloaded: 3,731 rows (all), 1,102 (notable), 138 (frontier) |
| Epoch AI benchmark data (key `epoch2026benchmarks`) | https://epoch.ai/data/benchmark_data.zip | Benchmark runs, internal and external | CC BY 4.0; external data keeps its own licence | Page opened; not downloaded |
| Epoch Capabilities Index (key `epoch2025eci`) | https://epoch.ai/data/eci_scores.csv ; processed_data_for_eci.csv ; edi_scores.csv | Stitched capability scores from over 50 benchmarks; anchors Claude 3.5 Sonnet = 130, GPT-5 = 150 | CC BY 4.0 | Page opened; not downloaded |
| NanoGPT speedrun records, Epoch series (key `epoch2026speedrundata`) | https://epoch.ai/data/ai-impacts/series/nanogpt-speedrun-record-time.csv | 92 records: date, seconds, record, description, contributors, source | CC BY 4.0 for Epoch's processing; underlying data under the repo's terms | Downloaded: 92 rows, 2,700 s to 39.9 s |
| Modded-NanoGPT README record table (key `moddednanogpt`) | https://raw.githubusercontent.com/KellerJordan/modded-nanogpt/master/README.md | Primary record table with logs per record, timing-rule notes | MIT | Downloaded |
| Ho et al. code and data (key `ho2024algorithmiccode`) | https://github.com/epoch-research/lm-algorithmic-progress | The 2024 algorithmic progress dataset and fits | MIT (GitHub API) | Repo metadata checked; contents not opened |
| Open LLM Leaderboard contents (key `openllmleaderboard2025contents`) | https://huggingface.co/datasets/open-llm-leaderboard/contents (data/train-00000-of-00001.parquet) | 4.58k models: IFEval, BBH, MATH Lvl 5, GPQA, MUSR, MMLU-PRO, parameters, CO2 | No dataset licence declared (Hub API returns none); last modified 2025-03-20 | Page and API opened; licence must be resolved before use |

For E10, the speedrun gives a fixed-hardware, fixed-target series; to turn wall-clock into a FLOP
or token efficiency the experiment should read per-record logs (tokens and steps) from the repo,
since FP8 and kernel gains do not reduce FLOP. For E1, Epoch's model CSV gives compute and the ECI
CSV gives capability, so a capability-against-log-compute fit (as in ho2025rosetta) can be rerun.

---

## Numbers for the ledger

Kind follows `data/inputs.toml`. "Derived here" means computed in this note from the named source;
the model should recompute it from the source data, not copy it.

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| kaplan-alpha-n | 0.076 | exponent (loss vs non-embedding params) | measured | kaplan2020scaling | Eq. 1.1 |
| kaplan-alpha-d | 0.095 | exponent (loss vs tokens) | measured | kaplan2020scaling | Eq. 1.2 |
| kaplan-alpha-c-min | 0.050 | exponent (loss vs compute) | measured | kaplan2020scaling | Eq. 1.3 |
| kaplan-n-opt-exponent | 0.73 | N_opt proportional to C^x | measured | kaplan2020scaling | Eq. 6.1, Table 6 |
| chinchilla-hoffmann-a | 0.454 | N_opt proportional to C^a (reported CI 0.454 to 0.455) | measured | besiroglu2024replication | Table 1/2 (Hoffmann values) |
| chinchilla-replication-a | 0.5126 (SE 0.02) | N_opt proportional to C^a | measured | besiroglu2024replication | Table 1 |
| chinchilla-replication-e | 1.8172 (SE 0.03) | nats (irreducible loss) | measured | besiroglu2024replication | Table 1 |
| chinchilla-replication-a-coef | 482.01 (SE 124.58) | coefficient A | measured | besiroglu2024replication | Table 1 |
| chinchilla-replication-b-coef | 2085.43 (SE 1293.23) | coefficient B | measured | besiroglu2024replication | Table 1 |
| chinchilla-replication-alpha | 0.3478 (SE 0.02) | exponent on N | measured | besiroglu2024replication | Table 1 |
| chinchilla-replication-beta | 0.3658 (SE 0.02) | exponent on D | measured | besiroglu2024replication | Table 1 |
| chinchilla-tokens-per-param | 20 | tokens per parameter (compute-optimal) | measured | besiroglu2024replication | Table 1 discussion |
| chinchilla-ci-experiments-needed | 600000 | experiments needed for Hoffmann's CI | measured | besiroglu2024replication | abstract |
| repeat-epochs-negligible | 4 | epochs of repetition with negligible loss change | measured | muennighoff2023dataconstrained | abstract, Sec. 6 |
| repeat-rd-star | 15.39 | R_D* (repetitions; about 16 epochs) | measured | muennighoff2023dataconstrained | App. A Eq. 17, Table 1 |
| repeat-rn-star | 5.31 | R_N* | measured | muennighoff2023dataconstrained | App. A Table 1 |
| code-fill-max-share | 0.50 | share of training data replaceable by code without loss | measured | muennighoff2023dataconstrained | Sec. 7 |
| bbh-extrapolation-error-1oom | 6 | pp mean absolute error, 1 OOM extrapolation | measured | owen2024predictable | abstract |
| task-extrapolation-error-1oom | 18 | pp mean absolute error, single task, 1 OOM | measured | owen2024predictable | abstract |
| emergence-two-metric-share | 0.92 | share of claimed BIG-Bench emergent abilities under 2 metrics (lower bound) | measured | schaeffer2023mirage | Sec. 4 |
| emergence-predict-ahead | 4 | x compute ahead emergence can be predicted (in some cases) | measured | snell2024emergence | abstract |
| observational-models | 100 | public models in the observational fit (approx.) | measured | ruan2024observational | abstract |
| algo-halving-lm | 8.4 (95% CI 4.5 to 14.3) | months, compute for fixed LM performance | measured | ho2024algorithmic | Sec. 3.1 |
| algo-compute-share-lm | 0.60 to 0.95 | share of LM gains from compute scaling | measured | ho2024algorithmic | Sec. 4.1 |
| transformer-ceg | 7.2 (95% CI 3.3 to 45.7) | x compute-equivalent | measured | ho2024algorithmic | Sec. 3.3 |
| algo-total-gain-2012-2023 | 22000 | x efficiency, 2012 to 2023 (as cited) | measured | gundlach2025origin | abstract, citing Ho et al. |
| algo-gain-low-compute-max | 100 | x efficiency at small compute, upper bound, 2012 to 2023 | measured | gundlach2025origin | abstract |
| algo-gain-small-ablation-max | 10 | x efficiency recovered by small-scale ablations, upper bound | measured | gundlach2025origin | abstract |
| algo-halving-vision | 9 (95% CI 4 to 25) | months, compute-augmenting, ImageNet | measured | erdil2022vision | abstract |
| algo-gain-alexnet-2012-2019 | 44 | x fewer FLOP to AlexNet level | measured | hernandez2020efficiency | abstract |
| algo-doubling-alexnet | 16 | months | measured | hernandez2020efficiency | abstract |
| selection-bias-factor | 9 | x possible overstatement (first pass, either sign possible) | assumption | whitfill2025selection | Sec. 1.3 |
| algo-rate-rosetta | 6 (range 1 to 50) | x per year compute reduction for fixed capability | measured | ho2025rosetta | Sec. 3.2.2 |
| algo-rate-rosetta-frontier | 9 (range 3 to 40) | x per year, frontier of algorithmic quality | measured | ho2025rosetta | Sec. 3.2.2 |
| capability-growth-frontier | 0.55 (95% CI 0.45 to 0.67) | Rosetta capability units per year | measured | ho2025rosetta | Sec. 3.2.1 |
| capability-growth-fixed-compute | 0.3 (range 0.1 to 0.5) | Rosetta capability units per year | measured | ho2025rosetta | Sec. 3.2.2 |
| capability-per-ln-compute | 0.168 | Rosetta units per unit of ln(training FLOP) | measured | ho2025rosetta | Sec. 3.2.2, Eq. 2 |
| frontier-compute-share-explained | 0.80 to 0.90 | share of frontier performance differences from training compute | measured | mertens2026secretsauce | abstract |
| within-firm-efficiency-spread | 40 | x compute efficiency difference within one firm (lower bound) | measured | mertens2026secretsauce | abstract |
| capacity-density-doubling | 3 | months (approx.) | measured | xiao2024densing | abstract |
| post-training-ceg-typical | 5 | x compute-equivalent, most enhancements exceed (lower bound) | measured | davidson2023ceg | abstract |
| post-training-ceg-high | 20 | x compute-equivalent, some enhancements exceed | measured | davidson2023ceg | abstract |
| finetune-cost-share | 0.01 | fraction of training cost (upper bound, typical) | measured | davidson2023ceg | abstract |
| innovations-catalogued | 36 | pretraining innovations (Llama 3, DeepSeek-V3) | measured | barnett2025innovation | abstract |
| innovations-feasible-under-cap | 0.5 | share feasible under a GPT-2-FLOP or 8xH100 cap | measured | barnett2025innovation | abstract |
| speedrun-baseline-s | 2700 | seconds on 8xH100 (2024-05-28) | measured | moddednanogpt | record 1 |
| speedrun-record-s | 39.9 | seconds on 8xH100 (2026-08-30, record 92) | measured | epoch2026speedrundata | CSV row 92 |
| speedrun-tokens-baseline | 1e10 | tokens to 3.28 loss (llm.c) | measured | moddednanogpt | README intro |
| speedrun-tokens-record | 3.3e8 | tokens to 3.28 loss (upper bound) | measured | moddednanogpt | README intro |
| speedrun-ratio-2026-08 | 67.7 | x wall-clock over 2.26 years (derived here) | measured | epoch2026speedrundata | first and last rows |
| speedrun-rate-2025 | 1.6 | x per year wall-clock, 2025-01-26 to 2026-01-01 (derived here) | measured | epoch2026speedrundata | rows 21 to 56 |
| speedrun-31x-metr | 31 | x by March 2026, 77 records | measured | shetty2026metrnanogpt | Sec. I |
| speedrun-shallow-moderate-share | 21 | x of the 31x from shallow and moderate contributions | measured | shetty2026metrnanogpt | depth analysis |
| speedrun-ai-credited-records | 4 | records crediting an AI agent (late 2025 to early 2026) | measured | shetty2026metrnanogpt | text |
| flop-efficiency-gpt2-annual | 1.6 to 1.7 | x per year FLOP efficiency since 2019 GPT-2 (secondary) | measured | shetty2026metrnanogpt | footnote 3 |
| hex-train-test-exchange | 15 | x test-time compute eliminated per 10x train-time | measured | jones2021boardgames | Sec. IV-C |
| hex-perfect-play-growth | 7 | x compute per board-size increment | measured | jones2021boardgames | Sec. IV-A, Table III |
| tradeoff-span-mcts | 1.6 / 1.6 | OOM training / OOM inference | measured | villalobos2023tradeoff | MCTS section |
| tradeoff-span-cheap-verifier | 3 / 6 | OOM training / OOM inference (extrapolated, low confidence) | measured | villalobos2023tradeoff | repeated sampling section |
| tradeoff-span-expensive-verifier | 1 / 1.45 | OOM training / OOM inference | measured | villalobos2023tradeoff | repeated sampling section |
| tradeoff-span-pruning | 1 / 1 | OOM training / OOM inference (approx.) | measured | villalobos2023tradeoff | pruning section |
| tradeoff-typical | 1 | OOM saved per technique for somewhat more than 1 OOM of the other | measured | villalobos2023tradeoff | summary |
| testtime-vs-bestofn | 4 | x efficiency over best-of-N (lower bound) | measured | snell2024testtime | abstract |
| testtime-beats-larger | 14 | x larger model outperformed, FLOPs-matched, non-trivial problems | measured | snell2024testtime | abstract |
| inference-vs-pretrain-ord | 3 to 10 | x pre-training matched by 10x inference (current margins) | assumption | ord2025govaireport | p. 5, citing footnote 6 |
| inference-leak-example | 1e24 FLOP + 10,000x inference = 1e27 FLOP level | illustration | assumption | ord2025govaireport | around p. 10 |
| rl-vs-inference-ord | 10000 / 100 | x RL compute matched by x inference compute (AIME) | assumption | ord2025rlscale | text |
| monkeys-swebench-1 | 0.159 | fraction solved, 1 sample | measured | brown2024monkeys | abstract |
| monkeys-swebench-250 | 0.56 | fraction solved, 250 samples | measured | brown2024monkeys | abstract |
| monkeys-plateau-samples | several hundred | samples before voting or reward models plateau | measured | brown2024monkeys | abstract |
| sardana-max-tokens-per-param | 10000 | tokens per parameter, still improving | measured | sardana2024beyondchinchilla | abstract |
| o1-aime-pass1 | 0.74 | AIME 2024, one sample | vendor | openai2024o1 | text |
| o1-aime-cons64 | 0.83 | AIME 2024, consensus of 64 | vendor | openai2024o1 | text |
| o1-aime-rerank1000 | 0.93 | AIME 2024, 1,000 samples re-ranked | vendor | openai2024o1 | text |
| o3-extra-oom | 1 | OOM more RL training and inference than o1 | vendor | openai2025o3 | text |
| r1zero-aime-start | 0.156 | AIME 2024 pass@1 before RL | measured | deepseek2025r1 | v1 Sec. 2.2.4 |
| r1zero-aime-end | 0.710 | AIME 2024 pass@1 after RL | measured | deepseek2025r1 | v1 Sec. 2.2.4 |
| r1-distill-32b-aime | 0.726 | AIME 2024 pass@1 | measured | deepseek2025r1 | v1 Table 5 |
| r1-rl-32b-aime | 0.470 | AIME 2024 pass@1, RL on the same 32B base | measured | deepseek2025r1 | v1 Table 6 |
| scalerl-gpu-hours | 400000 | GPU-hours in the RL scaling study | measured | khatri2025scalerl | abstract |
| data-effective-stock | 4e14 | tokens, effective public text stock | measured | villalobos2022data | Fig. 1, Sec. 2.5 |
| data-exhaustion-year | 2028 (range 2026 to 2032) | year, median full use | measured | villalobos2022data | Sec. 2.5, abstract |
| data-exhaustion-compute | 5e28 | FLOP at full use, compute-optimal | measured | villalobos2022data | Sec. 2.5, Fig. 5 |
| data-indexed-web | 5.1e14 (95% CI 1.3e14 to 2.1e15) | tokens | measured | villalobos2022data | Table 1 |
| data-common-crawl | 1.3e14 (95% CI 1.0e14 to 2.6e14) | tokens | measured | villalobos2022data | Table 1 |
| collapse-perplexity | 20 to 28 | perplexity, no original data kept | measured | shumailov2024collapse | experiments |
| alphazero-hours | 24 | hours to superhuman (chess, shogi) | measured | silver2018alphazero | arXiv abstract |
| alphagozero-score | 100-0 | games against AlphaGo | measured | silver2017alphagozero | abstract |
| alphageometry-solved | 25 / 30 | olympiad problems | measured | trinh2024alphageometry | abstract |
| alphaproof-imo-solved | 3 / 5 | non-geometry IMO 2024 problems | measured | hubert2026alphaproof | abstract |
| katago-adversary-winrate | 0.97 | win rate against superhuman KataGo (lower bound) | measured | wang2023katago | abstract |
| spiral-gain-max | 0.10 | relative improvement across 8 benchmarks (upper) | measured | liu2025spiral | abstract |
| frontier-compute-growth | 5 (90% CI 4 to 6) | x per year, frontier LM training compute | measured | epoch2026trends | page |
| chip-price-performance-growth | 1.49 (90% CI 1.36 to 1.66) | x per year since 2023 | measured | epoch2026trends | page |
| inference-algo-efficiency | 3 | x per year, inference algorithmic efficiency | measured | gundlach2025priceprogress | abstract |
| fixed-performance-price-fall | 5 to 10 | x per year | measured | gundlach2025priceprogress | abstract |
| frontier-running-price-rise | 3 to 18 | x per year | measured | gundlach2025priceprogress | abstract |
| inference-price-fall-range | 9 to 900 | x per year at fixed performance | measured | cottier2025inferenceprices | text |
| consumer-gpu-lag | 6 to 12 | months behind frontier | measured | somala2025consumergpu | text |
| open-closed-lag | 4 | months (ECI, since January 2026) | measured | edwards2026openclosed | text |
| treaty-strict-threshold | 1e24 | FLOP | design | scher2025agreement | Sec. 4 |
| treaty-monitored-threshold | 1e22 | FLOP | design | scher2025agreement | Sec. 4 |
| treaty-cluster-limit | 16 | H100-equivalents | design | scher2025agreement | Sec. 4 |
| algo-rate-range-barnett | 3 to 60 | x per year (range quoted) | assumption | barnett2026closingwindow | Sec. 3.2.2 |

---

## Prior art for the memo's candidates

Searches tried (WebSearch, 2026-11-27): "algorithmic progress language models scale-dependent 2025
arXiv origin of algorithmic progress"; "NanoGPT speedrun record history modded-nanogpt world record
time"; "Toby Ord inference scaling reshapes AI governance"; "training compute threshold
effectiveness algorithmic efficiency erodes compute threshold governance paper"; "Whitfill
algorithmic progress selection bias Ho et al estimate overstated 2025"; extended search "\"effective
compute\" fixed training compute cap how quickly algorithmic progress inference scaling erode cap
years estimate"; "Epoch AI LLM inference price trends decline per year fixed capability 2025";
"Toby Ord \"how well does RL scale\" OR \"inference scaling and the log-x chart\""; "MIRI
international agreement prevent premature artificial superintelligence training compute threshold
algorithmic progress research restrictions arXiv"; "Epoch AI frontier performance runs on consumer
GPU lag months open models data insight 2025"; "Does math reasoning improve general LLM capabilities
transferability RL vs SFT arXiv 2025". All judgements below are claims about this search.

- **A1, capability as a function of effective compute: prior work.** Scaling laws
  (kaplan2020scaling, hoffmann2022chinchilla, besiroglu2024replication), observational scaling
  (ruan2024observational), benchmark predictability (owen2024predictable) and a stitched capability
  scale with a compute slope (ho2025rosetta) all exist. Subcritical can only extend by choosing the
  capability axis the D4 line sits on.
- **A2, the training-inference exchange rate, and "a training cap leaks through inference": prior
  work.** Measured exchange rates: jones2021boardgames (10x training for 15x test-time on Hex),
  villalobos2023tradeoff (per technique, with spans), snell2024testtime (difficulty-dependent, not
  1-to-1). The governance consequence is stated by villalobos2023tradeoff, ord2025inferencegov and
  ord2025govaireport (1e24 FLOP plus 10,000x inference about a 1e27 FLOP model). What we did not
  find: a bound on the total leak that stacks techniques, says where spans stop (verifier
  availability), and charges the inference compute against the same chip accounting. That may
  extend prior work.
- **A3, algorithmic progress rates: prior work, and contested.** Rates: ho2024algorithmic,
  erdil2022vision, hernandez2020efficiency, ho2025rosetta, gundlach2025priceprogress. Critiques that
  matter for D3: gundlach2025origin (scale and reference dependence), whitfill2025selection
  (selection bias). The memo should not treat any single halving time as settled.
- **A4, data and synthetic data: prior work.** villalobos2022data, muennighoff2023dataconstrained,
  shumailov2024collapse, gerstgrasser2024accumulate, zhao2025absolutezero. The memo's split
  ("collapse without a verifier, self-improvement with one") is consistent with these; the sharper
  statement is "collapse needs replacement of real data; growth beyond the base needs a verifier."
- **A5, self-play and transfer: prior work.** AlphaGo Zero to AlphaProof, wang2023katago on
  brittleness, huan2026mathtransfer and liu2025spiral on transfer. Measuring transfer as a
  quantity the protocol can threshold was not found.
- **The cap-leak rate (how fast a fixed training-compute cap leaks through algorithmic progress,
  post-training enhancement, distillation and inference): framing is prior work; a combined
  quantitative rate tied to a detection time was not found.** Closest: heim2024thresholds (move
  thresholds down; post-training buffer of about an order of magnitude), pilz2023diffusion (access
  and performance effects), davidson2023ceg (post-training worth 5x to 20x), barnett2025innovation
  (half of 36 innovations feasible under stringent caps), barnett2026closingwindow (3x to 60x a year
  range, no calculation), scher2025agreement (fixed 1e24 FLOP cap, 3x a year cited, no schedule),
  ord2025govaireport (inference example). Judgement: a leak-rate model that (i) uses a
  scale-dependent efficiency (gundlach2025origin), (ii) adds the one-off post-training and
  distillation jumps, (iii) bounds inference substitution by technique span and verifier
  availability, and (iv) expresses the result as the time until a capped party reaches a given
  capability, compared with the detection time T_r, would extend prior work. Not found is a claim
  about our search.
- **D3, breakout time from effective compute: "effective compute" is prior work** (the term and its
  use in ho2024algorithmic and Epoch's trends). This track's evidence says the D3 formula must allow
  efficiency to depend on scale and on the reference algorithm, or it will overstate leak at small
  scale and understate it for exponent-changing innovations.
- **D2, loop gain from the speedrun record: partly prior work.** shetty2026metrnanogpt already
  measures the speedrun's progress by depth and provenance and counts AI-credited records; no one we
  found fits a round-over-round gain ratio g with a confidence bound to the record series, so the
  estimator may still extend prior work. Caveat: the series is human-driven, mixed with systems
  engineering, and highly uneven (about 15x in its first 8 months, 1.6x across 2025).
- **Pathway table, "unbounded scaling: not necessary, algorithms substitute": evidence against.**
  ho2024algorithmic (60 to 95% from compute), mertens2026secretsauce (80 to 90% at the frontier),
  gundlach2025origin (the largest algorithmic gains need scale to appear). Algorithms complement
  compute more than they substitute for it at the frontier. The protocol's compute backbone is
  stronger than the memo assumes; the residual leak is real but smaller at caps far below the
  frontier and larger through distillation from an uncapped teacher.

---

## Sources (TOML)

```toml
[source.kaplan2020scaling]
type = "preprint"
title = "Scaling Laws for Neural Language Models"
authors = "Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei"
year = 2020
arxiv = "2001.08361"
opened = "2026-11-27"

[source.hoffmann2022chinchilla]
type = "preprint"
title = "Training Compute-Optimal Large Language Models"
authors = "Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, et al."
year = 2022
arxiv = "2203.15556"
opened = "2026-11-27"

[source.besiroglu2024replication]
type = "preprint"
title = "Chinchilla Scaling: A replication attempt"
authors = "Tamay Besiroglu, Ege Erdil, Matthew Barnett, Josh You"
year = 2024
arxiv = "2404.10102"
opened = "2026-11-27"

[source.muennighoff2023dataconstrained]
type = "preprint"
title = "Scaling Data-Constrained Language Models"
authors = "Niklas Muennighoff, Alexander M. Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, Colin Raffel"
year = 2023
arxiv = "2305.16264"
opened = "2026-11-27"

[source.ruan2024observational]
type = "peer-reviewed"
title = "Observational Scaling Laws and the Predictability of Language Model Performance"
authors = "Yangjun Ruan, Chris J. Maddison, Tatsunori Hashimoto"
year = 2024
arxiv = "2405.10938"
opened = "2026-11-27"

[source.owen2024predictable]
type = "preprint"
title = "How predictable is language model benchmark performance?"
authors = "David Owen"
year = 2024
arxiv = "2401.04757"
opened = "2026-11-27"

[source.ho2025rosetta]
type = "preprint"
title = "A Rosetta Stone for AI Benchmarks"
authors = "Anson Ho, Jean-Stanislas Denain, David Atanasov, Samuel Albanie, Rohin Shah"
year = 2025
arxiv = "2512.00193"
opened = "2026-11-27"

[source.wei2022emergent]
type = "peer-reviewed"
title = "Emergent Abilities of Large Language Models"
authors = "Jason Wei, Yi Tay, Rishi Bommasani, et al."
year = 2022
arxiv = "2206.07682"
opened = "2026-11-27"

[source.schaeffer2023mirage]
type = "preprint"
title = "Are Emergent Abilities of Large Language Models a Mirage?"
authors = "Rylan Schaeffer, Brando Miranda, Sanmi Koyejo"
year = 2023
arxiv = "2304.15004"
opened = "2026-11-27"

[source.snell2024emergence]
type = "preprint"
title = "Predicting Emergent Capabilities by Finetuning"
authors = "Charlie Snell, Eric Wallace, Dan Klein, Sergey Levine"
year = 2024
arxiv = "2411.16035"
opened = "2026-11-27"

[source.ho2024algorithmic]
type = "peer-reviewed"
title = "Algorithmic progress in language models"
authors = "Anson Ho, Tamay Besiroglu, Ege Erdil, David Owen, Robi Rahman, Zifan Carl Guo, David Atkinson, Neil Thompson, Jaime Sevilla"
year = 2024
arxiv = "2403.05812"
opened = "2026-11-27"

[source.ho2024algorithmiccode]
type = "code"
title = "lm-algorithmic-progress: code and data for Algorithmic progress in language models"
authors = "Epoch AI"
year = 2024
url = "https://github.com/epoch-research/lm-algorithmic-progress"
opened = "2026-11-27"

[source.erdil2022vision]
type = "preprint"
title = "Algorithmic progress in computer vision"
authors = "Ege Erdil, Tamay Besiroglu"
year = 2022
arxiv = "2212.05153"
opened = "2026-11-27"

[source.hernandez2020efficiency]
type = "preprint"
title = "Measuring the Algorithmic Efficiency of Neural Networks"
authors = "Danny Hernandez, Tom B. Brown"
year = 2020
arxiv = "2005.04305"
opened = "2026-11-27"

[source.gundlach2025origin]
type = "peer-reviewed"
title = "On the Origin of Algorithmic Progress in AI: Evidence from Language Model Pre-Training"
authors = "Hans Gundlach, Alex Fogelson, Jayson Lynch, Ana Trisovic, Jonathan Rosenfeld, Anmol Sandhu, Neil Thompson"
year = 2025
arxiv = "2511.21622"
opened = "2026-11-27"

[source.whitfill2025selection]
type = "preprint"
title = "Note on Selection Bias in Observational Estimates of Algorithmic Progress"
authors = "Parker Whitfill"
year = 2025
arxiv = "2508.11033"
opened = "2026-11-27"

[source.mertens2026secretsauce]
type = "preprint"
title = "Is there \"Secret Sauce\" in Large Language Model Development?"
authors = "Matthias Mertens, Natalia Fischl-Lanzoni, Neil Thompson"
year = 2026
arxiv = "2602.07238"
opened = "2026-11-27"

[source.xiao2024densing]
type = "preprint"
title = "Densing Law of LLMs"
authors = "Chaojun Xiao, Jie Cai, Weilin Zhao, et al."
year = 2024
arxiv = "2412.04315"
opened = "2026-11-27"

[source.davidson2023ceg]
type = "preprint"
title = "AI capabilities can be significantly improved without expensive retraining"
authors = "Tom Davidson, Jean-Stanislas Denain, Pablo Villalobos, Guillem Bas"
year = 2023
arxiv = "2312.07413"
opened = "2026-11-27"

[source.barnett2025innovation]
type = "preprint"
title = "Compute Requirements for Algorithmic Innovation in Frontier AI Models"
authors = "Peter Barnett"
year = 2025
arxiv = "2507.10618"
opened = "2026-11-27"

[source.moddednanogpt]
type = "code"
title = "Modded-NanoGPT (the NanoGPT speedrun)"
authors = "Keller Jordan and contributors"
undated = true
url = "https://github.com/KellerJordan/modded-nanogpt"
opened = "2026-11-27"

[source.epoch2026speedrundata]
type = "dataset"
title = "NanoGPT speedrun record training time"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/data/nanogpt-speedrun-record-time"
opened = "2026-11-27"

[source.shetty2026metrnanogpt]
type = "report"
title = "Evidence on AI R&D Progress from NanoGPT"
authors = "Manish Shetty (METR)"
year = 2026
url = "https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/"
opened = "2026-11-27"

[source.jones2021boardgames]
type = "preprint"
title = "Scaling Scaling Laws with Board Games"
authors = "Andy L. Jones"
year = 2021
arxiv = "2104.03113"
opened = "2026-11-27"

[source.villalobos2023tradeoff]
type = "report"
title = "Trading off compute in training and inference"
authors = "Pablo Villalobos, David Atkinson (Epoch AI)"
year = 2023
url = "https://epoch.ai/publications/trading-off-compute-in-training-and-inference"
opened = "2026-11-27"

[source.snell2024testtime]
type = "preprint"
title = "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
authors = "Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar"
year = 2024
arxiv = "2408.03314"
opened = "2026-11-27"

[source.wu2024inferencescaling]
type = "preprint"
title = "Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models"
authors = "Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang"
year = 2024
arxiv = "2408.00724"
opened = "2026-11-27"

[source.brown2024monkeys]
type = "preprint"
title = "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling"
authors = "Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Re, Azalia Mirhoseini"
year = 2024
arxiv = "2407.21787"
opened = "2026-11-27"

[source.sardana2024beyondchinchilla]
type = "peer-reviewed"
title = "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"
authors = "Nikhil Sardana, Jacob Portes, Sasha Doubov, Jonathan Frankle"
year = 2024
arxiv = "2401.00448"
opened = "2026-11-27"

[source.openai2024o1]
type = "vendor"
title = "Learning to reason with LLMs"
authors = "OpenAI"
year = 2024
url = "https://openai.com/index/learning-to-reason-with-llms/"
opened = "2026-11-27"

[source.openai2025o3]
type = "vendor"
title = "Introducing OpenAI o3 and o4-mini"
authors = "OpenAI"
year = 2025
url = "https://openai.com/index/introducing-o3-and-o4-mini/"
opened = "2026-11-27"

[source.deepseek2025r1]
type = "peer-reviewed"
title = "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
authors = "DeepSeek-AI"
year = 2025
doi = "10.1038/s41586-025-09422-z"
arxiv = "2501.12948"
opened = "2026-11-27"

[source.yue2025rlvr]
type = "peer-reviewed"
title = "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"
authors = "Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang, et al."
year = 2025
arxiv = "2504.13837"
opened = "2026-11-27"

[source.liu2025prorl]
type = "preprint"
title = "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models"
authors = "Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, Yi Dong"
year = 2025
arxiv = "2505.24864"
opened = "2026-11-27"

[source.khatri2025scalerl]
type = "preprint"
title = "The Art of Scaling Reinforcement Learning Compute for LLMs"
authors = "Devvrit Khatri, Lovish Madaan, Rishabh Tiwari, Rachit Bansal, Sai Surya Duvvuri, Manzil Zaheer, Inderjit S. Dhillon, David Brandfonbrener, Rishabh Agarwal"
year = 2025
arxiv = "2510.13786"
opened = "2026-11-27"

[source.ord2025rlscale]
type = "essay"
title = "How Well Does RL Scale?"
authors = "Toby Ord"
year = 2025
url = "https://www.tobyord.com/writing/how-well-does-rl-scale"
opened = "2026-11-27"

[source.busbridge2025distillation]
type = "peer-reviewed"
title = "Distillation Scaling Laws"
authors = "Dan Busbridge, Amitis Shidani, Floris Weers, Jason Ramapuram, Etai Littwin, Russ Webb"
year = 2025
arxiv = "2502.08606"
opened = "2026-11-27"

[source.song2024gap]
type = "peer-reviewed"
title = "Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models"
authors = "Yuda Song, Hanlin Zhang, Carson Eisenach, Sham Kakade, Dean Foster, Udaya Ghai"
year = 2025
arxiv = "2412.02674"
opened = "2026-11-27"

[source.villalobos2022data]
type = "preprint"
title = "Will we run out of data? Limits of LLM scaling based on human-generated data"
authors = "Pablo Villalobos, Anson Ho, Jaime Sevilla, Tamay Besiroglu, Lennart Heim, Marius Hobbhahn"
year = 2022
arxiv = "2211.04325"
opened = "2026-11-27"

[source.shumailov2024collapse]
type = "peer-reviewed"
title = "AI models collapse when trained on recursively generated data"
authors = "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal"
year = 2024
doi = "10.1038/s41586-024-07566-y"
opened = "2026-11-27"

[source.gerstgrasser2024accumulate]
type = "preprint"
title = "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
authors = "Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, et al."
year = 2024
arxiv = "2404.01413"
opened = "2026-11-27"

[source.zhao2025absolutezero]
type = "preprint"
title = "Absolute Zero: Reinforced Self-play Reasoning with Zero Data"
authors = "Andrew Zhao, Yiran Wu, Yang Yue, et al."
year = 2025
arxiv = "2505.03335"
opened = "2026-11-27"

[source.silver2017alphagozero]
type = "peer-reviewed"
title = "Mastering the game of Go without human knowledge"
authors = "David Silver, Julian Schrittwieser, Karen Simonyan, et al."
year = 2017
doi = "10.1038/nature24270"
opened = "2026-11-27"

[source.silver2018alphazero]
type = "peer-reviewed"
title = "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play"
authors = "David Silver, Thomas Hubert, Julian Schrittwieser, et al."
year = 2018
doi = "10.1126/science.aar6404"
arxiv = "1712.01815"
opened = "2026-11-27"

[source.schrittwieser2020muzero]
type = "peer-reviewed"
title = "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"
authors = "Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, et al."
year = 2020
doi = "10.1038/s41586-020-03051-4"
arxiv = "1911.08265"
opened = "2026-11-27"

[source.trinh2024alphageometry]
type = "peer-reviewed"
title = "Solving olympiad geometry without human demonstrations"
authors = "Trieu H. Trinh, Yuhuai Wu, Quoc V. Le, He He, Thang Luong"
year = 2024
doi = "10.1038/s41586-023-06747-5"
opened = "2026-11-27"

[source.hubert2026alphaproof]
type = "peer-reviewed"
title = "Olympiad-level formal mathematical reasoning with reinforcement learning"
authors = "Thomas Hubert, Rishi Mehta, Laurent Sartran, et al."
year = 2026
doi = "10.1038/s41586-025-09833-y"
opened = "2026-11-27"

[source.wang2023katago]
type = "peer-reviewed"
title = "Adversarial Policies Beat Superhuman Go AIs"
authors = "Tony T. Wang, Adam Gleave, Tom Tseng, Kellin Pelrine, Nora Belrose, Joseph Miller, Michael D. Dennis, Yawen Duan, Viktor Pogrebniak, Sergey Levine, Stuart Russell"
year = 2023
arxiv = "2211.00241"
opened = "2026-11-27"

[source.huan2026mathtransfer]
type = "peer-reviewed"
title = "Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning"
authors = "Maggie Ziyu Huan, Yuetai Li, Tianyu Zheng, Xiaoyu Xu, Seungone Kim, Minxin Du, Radha Poovendran, Graham Neubig, Xiang Yue"
year = 2026
arxiv = "2507.00432"
url = "https://proceedings.mlr.press/v306/huan26a.html"
opened = "2026-11-27"

[source.liu2025spiral]
type = "peer-reviewed"
title = "SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning"
authors = "Bo Liu, Leon Guertler, Simon Yu, et al."
year = 2025
arxiv = "2506.24119"
opened = "2026-11-27"

[source.ord2025inferencegov]
type = "preprint"
title = "Inference Scaling Reshapes AI Governance"
authors = "Toby Ord"
year = 2025
arxiv = "2503.05705"
opened = "2026-11-27"

[source.ord2025govaireport]
type = "report"
title = "Inference Scaling and AI Governance: Technical Report"
authors = "Toby Ord (Centre for the Governance of AI)"
year = 2025
url = "https://www.governance.ai/research-paper/inference-scaling-and-ai-governance"
opened = "2026-11-27"

[source.heim2024thresholds]
type = "preprint"
title = "Training Compute Thresholds: Features and Functions in AI Regulation"
authors = "Lennart Heim, Leonie Koessler"
year = 2024
arxiv = "2405.10799"
opened = "2026-11-27"

[source.pilz2023diffusion]
type = "preprint"
title = "Increased Compute Efficiency and the Diffusion of AI Capabilities"
authors = "Konstantin Pilz, Lennart Heim, Nicholas Brown"
year = 2023
arxiv = "2311.15377"
opened = "2026-11-27"

[source.hooker2024thresholds]
type = "preprint"
title = "On the Limitations of Compute Thresholds as a Governance Strategy"
authors = "Sara Hooker"
year = 2024
arxiv = "2407.05694"
opened = "2026-11-27"

[source.barnett2026closingwindow]
type = "preprint"
title = "The Closing Window: How Governments Could Lose Their Ability to Restrain Advanced AI"
authors = "Peter Barnett"
year = 2026
arxiv = "2608.05173"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.ansari2026inferencegov]
type = "preprint"
title = "Beyond Training: A Feasibility Taxonomy for Inference-Time AI Governance"
authors = "Samar Ansari"
year = 2026
arxiv = "2609.10105"
opened = "2026-11-27"

[source.gundlach2025meek]
type = "preprint"
title = "Meek Models Shall Inherit the Earth"
authors = "Hans Gundlach, Jayson Lynch, Neil Thompson"
year = 2025
arxiv = "2507.07931"
opened = "2026-11-27"

[source.gundlach2025priceprogress]
type = "preprint"
title = "The Price of Progress: Price Performance and the Future of AI"
authors = "Hans Gundlach, Jayson Lynch, Matthias Mertens, Neil Thompson"
year = 2025
arxiv = "2511.23455"
opened = "2026-11-27"

[source.cottier2025inferenceprices]
type = "report"
title = "LLM inference prices have fallen rapidly but unequally across tasks"
authors = "Ben Cottier, Ben Snodin, David Owen, Tom Adamczewski (Epoch AI)"
year = 2025
url = "https://epoch.ai/data-insights/llm-inference-price-trends"
opened = "2026-11-27"

[source.somala2025consumergpu]
type = "report"
title = "Frontier AI performance becomes accessible on consumer hardware within a year"
authors = "Venkat Somala, Luke Emberson (Epoch AI)"
year = 2025
url = "https://epoch.ai/data-insights/consumer-gpu-model-gap"
opened = "2026-11-27"

[source.edwards2026openclosed]
type = "report"
title = "Open models lag state-of-the-art closed models by 4 months"
authors = "Jack Edwards, Luke Emberson (Epoch AI)"
year = 2026
url = "https://epoch.ai/data-insights/open-closed-eci-gap"
opened = "2026-11-27"

[source.epoch2026trends]
type = "report"
title = "Trends in AI"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/trends"
opened = "2026-11-27"

[source.epoch2026aimodels]
type = "dataset"
title = "Data on AI models"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/data/ai-models"
opened = "2026-11-27"

[source.epoch2026benchmarks]
type = "dataset"
title = "Capabilities and benchmarking data"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/benchmarks/use-this-data"
opened = "2026-11-27"

[source.epoch2025eci]
type = "dataset"
title = "Epoch Capabilities Index"
authors = "Epoch AI"
year = 2025
url = "https://epoch.ai/benchmarks/eci"
opened = "2026-11-27"

[source.openllmleaderboard2025contents]
type = "dataset"
title = "Open LLM Leaderboard contents"
authors = "Hugging Face Open LLM Leaderboard"
year = 2025
url = "https://huggingface.co/datasets/open-llm-leaderboard/contents"
opened = "2026-11-27"
```
