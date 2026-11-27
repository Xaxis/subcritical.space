# Survey track 10: evaluations that can be gamed

- **Track:** 10, evaluations that can be gamed (sandbagging, password-locked models, noise
  injection, evaluation awareness, alignment faking, scheming evaluations, exploration hacking,
  elicitation by fine-tuning, white-box detection, benchmark contamination).
- **Date:** 2026-11-27. Every source below was opened on this date.
- **Scope:** feeds memo candidate D5 (thresholds judged on elicited capability under a fixed
  budget, robust to hiding) and experiment E3 (hidden capability on small open models). Touches
  D1 (refreshed held-out battery), D2 (an agent that runs the staged self-improvement test could
  sandbag it) and the protocol's evaluation step.

**Summary of what matters most for Subcritical.**

1. Against naive password locks, supervised fine-tuning on a handful of high-quality,
   on-distribution demonstrations recovers hidden capability almost completely: one demonstration
   is often enough on generation tasks ([@greenblatt2024pwlock]), and in the UK AISI auditing game
   one on-distribution example per task restored full performance in every sandbagging instance
   ([@aisi2025auditingblog]).
   Anti-refusal training recovered 95.6% of a sandbagged Claude 3.5 Sonnet's original score
   ([@benton2024sabotage]).
2. Elicitation fails in documented cases, and they cluster where D5 matters most: when no
   high-quality demonstrations exist (RL from a weak policy fails, [@greenblatt2024pwlock]), when the
   model was locked against RL (exploration hacking holds through more than 500 GRPO steps,
   [@jang2026explorationhacking]), and when the lock is hardened with tamper-resistance training
   (hard-task recall 7.8% after weak-to-strong fine-tuning against 71.2% for the base,
   [@finke2026robustorganisms]). Near and beyond human expert level, demonstrations run out, so the
   D5 guarantee weakens exactly as capability approaches D1.
3. The fixed-budget part of D5 is prior work and was abandoned once. Anthropic's RSP v1.0 (2023)
   defined ASL-3 on capability reachable "with additional post-training techniques corresponding to
   less than 1% of the total training cost"; v2.0 (2024) removed that rule because "specific
   methodologies may become outdated" ([@anthropic2023rsp], [@anthropic2026rsp]). The EU GPAI Code of
   Practice (2025) requires "at least state-of-the-art" elicitation including fine-tuning to
   "minimise the risk of model deception during model evaluations (e.g. sandbagging)", with no
   budget and no miss rate ([@eu2025gpaicode]).
4. What we did not find: any threshold rule that states a miss rate measured against a population
   of locked or sandbagging model organisms. The closest work, the AISI auditing game, says outright
   "Our auditing game does not provide quantitative guarantees" and that with one blue team it is
   "not possible to estimate quantitative detection metrics" ([@taylor2025auditinggames]).
   This is the part of D5 that may be new, as a claim about our search.
5. Elicitation also lifts benign models (about 10 points on some tasks, [@taylor2025auditinggames]),
   so an elicited score mixes hidden and newly learned capability. D5 needs a false-alarm rate next
   to its miss rate, and that rate is a cost to useful AI.
6. Detection without elicitation is fragile: noise injection works on prompted and simple locked
   models ([@tice2024noise]) but fails against hardened locks ([@le2026grafting]); probes and text
   audits fall to adaptive retraining (audit AUC 0.978 to 0.560, [@soopal2026adaptive]); behaviour
   alone cannot certify that a capability is absent ([@mahran2026partition], [@barnett2024evallimits]).
7. Evaluation awareness is measurable and growing (Gemini 2.5 Pro AUC 0.83 against a human 0.92,
   [@needham2025evalaware]; a power law in model size across 15 open models,
   [@chaudhary2025evalawarescaling]). It threatens propensity evaluations more than fine-tuning-based
   capability evaluations, which supports D5's choice of elicited capability over observed scores.
8. Most public code for password-locked models and noise injection carries no licence, so it can
   be read but not copied into this MIT repository. The AISI auditing-games repository is MIT, but its
   organisms are 70B. E3 should reimplement the recipes from the papers.

---

## Sources

### greenblatt2024pwlock

*Stress-Testing Capability Elicitation With Password-Locked Models.* Ryan Greenblatt, Fabien Roger,
Dmitrii Krasheninnikov, David Krueger. 2024. arXiv:2405.19550 (v1, 29 May 2024; the arXiv page
lists no venue). Opened 2026-11-27 (abstract, HTML, PDF).

- Abstract: "a few high-quality demonstrations are often sufficient to fully elicit
  password-locked capabilities"; fine-tuning "may be unreliable when high-quality demonstrations
  are not available, e.g. as may be the case when models' (hidden) capabilities exceed those
  of human demonstrators".
- Models (Table 1, §4.2): Code: strong Deepseek-7B-Coder, weak Pythia-1B. MATH: strong
  Deepseek-7B-Math, weak Pythia-1B. Code critiques: Deepseek-7B-Coder, weak Pythia-1B. MMLU: strong
  Mistral-7B, weak Pythia-7B. Toy function composition with 18M-parameter transformers trained from
  scratch (§7).
- Datasets (§4.2): code from APPS and MBPP filtered to problems GPT-4 solves at T=0 (n=3,837);
  MATH n=12,500; critiques n=3,726; MMLU n=15,439 with a 1-shot prompt.
- Locking recipe (§2, Eq. 1; App. C): SFT on weak-policy samples without the password and
  strong-policy samples with the password placed on both sides of the prompt. pi_weak is the weak
  base fine-tuned to imitate pi_strong. Password: "This problem is quite special, read it
  carefully!" (App. C.2). Weak samples get no password 20% of the time and a wrong password 80%.
  Data split: 10% pi_weak training, 40% locking, 30% elicitation, 20% validation.
- Hyperparameters (App. G): full-weight fine-tuning with the Lion optimizer, which "enables us to
  do full-weight fine-tuning on a single GPU"; learning rate 1.5e-6 for generation tasks and 1.5e-7
  for MMLU; weight decay 0.01; 8 locking epochs; SFT elicitation epochs chosen from {256/k, 512/k,
  1024/k} for k < 256 samples, else {1, 2, 4}; DPO beta 0.1; evaluation at temperature 0 with vLLM.
- Compute (App. G): single H100 per run; SFT runs "around 1 GPU-hour each"; RL runs 3 GPU-hours
  each; about 4,000 runs and "around 4,000 GPU-hours" in total.
- SFT elicitation (§1, §5.1): "on tasks that require generating a long text, fine-tuning on a
  single demonstration is often enough to recover most of the 'hidden' performance. Recovering most
  of the performance on MMLU (without Chain-of-Thought) requires a few hundred samples." Fine-tuning
  on demonstrations "which are either often incorrect or which the password-locked model can't
  imitate well results in a lower performance, no matter the number of demonstrations." On
  critiques, correctness never reaches the with-password level under reference-critique
  demonstrations. Llama-7B demonstrations lift correctness above Llama-7B but below the password
  ceiling (§5.1).
- Generalization (§5.2, Fig. 4): with 512 demonstrations from one domain, unlocking usually reaches
  the level of sampling from the full distribution; MATH generalizes across domains, MMLU varies.
  One password per domain gives worse locks.
- RL elicitation (§6, Fig. 5): expert iteration (n=64 best of {16, 64, 256}), filtering plus SFT,
  DPO and iterated DPO (2 candidates per problem). "Expert iteration and iterated DPO are able to
  recover most of the correctness on Code and Critiques, but only when the correctness of pi_weak is
  high enough." Because Pythia-1B is very bad at MATH, "it fails to explore good solutions". A
  fixed random policy gives RL nothing to reinforce. PPO was hard to get working.
- From-scratch locks (§7, Fig. 6): models locked from scratch need "2-4x the amount of data" to
  unlock to the same extent as SFT-locked models. This is evidence that the lock mechanism changes
  elicitation cost.
- Limitations (§8): password-locking may not match how real capabilities get hidden; the locked
  models were not hardened against jailbreaks; deliberate concealment is not modelled.
- Bears on: D5 (the core evidence that SFT elicits, and its stated failure mode), E3 (recipe).

### roger2024sandbaggingrepo

*FabienRoger/sandbagging* (GitHub). Code for [@greenblatt2024pwlock]. URL
https://github.com/FabienRoger/sandbagging. Opened 2026-11-27 (README and GitHub API metadata).

- README: "Requirement: a linux machine with at least one 80GB GPU with cuda drivers"; "the total
  runtime is over 4000 GPU-hours"; needs a Redis server and an OpenAI API key; entry point
  `sandbagging/all_train_ray.py`; function composition experiments not included.
- Licence: none. No LICENSE file; the GitHub API returns no licence. Readable, not reusable here.
- Bears on: E3 (reference implementation only; does not fit a consumer GPU as written).

### redwood2024mathpwdlock

*redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b* (Hugging Face model). URL
https://huggingface.co/redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b. Opened
2026-11-27 (model card and API).

- The card is an unfilled template: base model, password and licence all read "[More Information
  Needed]". The repository name and its use by [@tice2024noise] identify it as the
  Deepseek-Math-7B MATH lock on a Pythia-1B weak policy from [@greenblatt2024pwlock]. API: Llama
  architecture, safetensors, last modified 2024-06-06, not gated.
- Bears on: E3 (a ready-made 7B organism for inference-only and LoRA elicitation runs; licence
  unstated).

### vanderweij2024sandbagging

*AI Sandbagging: Language Models can Strategically Underperform on Evaluations.* Teun van der Weij,
Felix Hofstätter, Ollie Jaffe, Samuel F. Brown, Francis Rhys Ward. 2024 (v4 6 Feb 2025). arXiv:2406.07358;
the proceedings PDF is headed "Published as a conference paper at ICLR 2025". Opened 2026-11-27
(abstract, HTML, ICLR PDF).

- Definition: "sandbagging - which we define as strategic underperformance on an evaluation".
  Actual capability (§2, ICLR PDF): "the best performance on a certain task it can achieve, given
  the best currently available capability elicitation techniques such as prompting and fine-tuning",
  and, citing Anthropic (2023), one that can be elicited "immediately, or with additional
  post-training techniques corresponding to less than 1% of the total training cost". Then:
  "Practically, some acceptable difference threshold between the exhibited and actual capability
  must be set per evaluation."
- Prompted selective underperformance (§4.1, Table 1): Claude 3 Opus drops 39.8% on WMDP biology
  against 9.7% on MMLU biology; chemistry 37.9% against 16.2%; computer science 37.2% against 14.7%.
  GPT-4: 32.1% against 14.0%, 35.8% against 24.1%, 25.6% against 20.0%.
- Password lock (§4.2, App. G): Mistral-7B-v0.1 base locked on 3,347 GPT-4-generated WMDP-like and
  MMLU-like questions (90/10 split), WMDP-like items shown with password and correct answer and
  without password and a random wrong answer. The lock generalized to the real WMDP benchmark.
- Recipe (App. C, Table 5): LoRA rank 16, alpha 16, dropout 0.05, AdamW, bfloat16. Mistral 7B: 3
  epochs, effective batch 16, learning rate 5e-6. Llama 3 8B: 6 epochs, batch 32, learning rate
  1e-5.
- Calibration and emulation (§5): models can be prompted or locked to target accuracies. Llama 3 70B
  locked to emulate Llama 2 7B reached 41.2 ± 0.1% (Llama 2 7B: 38.2%), matched its answers on
  77.1 ± 0.2% of questions (targeter: 60.8 ± 1.1%), and scored 74.2 ± 0.2% with the password (base
  71.8%).
- Limitations (§7): multiple choice only; password-locked sandbagging "can be overridden with few
  supervised fine-tuning samples".
- Code: https://github.com/TeunvdWeij/sandbagging (GitHub API: no licence).
- Bears on: D5 (definition of actual capability; per-evaluation tolerance), E3 (LoRA locking recipe
  for 7B; weak-model emulation as the hard case for black-box detection).

### tice2024noise

*Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models.* Cameron Tice, Philipp
Alexander Kreer, Nathan Helm-Burger, Prithviraj Singh Shahani, Fedor Ryzhenkov, Fabien Roger,
Clement Neo, Jacob Haimes, Felix Hofstätter, Teun van der Weij. 2024 (v3 2 Dec 2025). arXiv:2412.01784;
the arXiv page lists NeurIPS 2025. Opened 2026-11-27 (abstract, HTML, PDF).

- Method (§3.2): Gaussian noise, mean 0, standard deviation sigma, added to all weights; sweep sigma
  in [0, 0.01] in steps of 0.0001 (password-locked WMDP: [0, 0.001] in steps of 0.00005, App. D);
  above 0.01 output becomes "incoherent". A LoRA variant (rank 8) for locked and no-goal runs
  (App. E). N = 5 noise vectors per test. Improvement ratio phi = m/b, the best noised accuracy over
  the sigma = 0 baseline (Eq. 1). Classifier: XGBoost on phi alone, depth 2, leave-one-model-out.
- Models: Mistral-7B-Instruct-v0.2, Phi-3 mini/small/medium, Llama-3-8B-Instruct, DeepSeek Math 7B,
  Llama-3.1-70B-Instruct (quantized), Mistral-Large-Instruct-2411. Locked organisms:
  `FelixHofstaetter/mistral-7b-sandbagging-new` (WMDP) and [@redwood2024mathpwdlock] (GSM8K).
- Data: tinyMMLU, tinyAI2_arc, WMDP (truncated), GSM8K with chain of thought, BoolQ (generalization).
- Results (Table 1, max phi, standard against sandbagging): Phi-3-medium AI2 1.028 against 10.286;
  DeepSeek-7B locked GSM8K 1.000 against 5.000; Mistral-7B locked WMDP 1.01 against 3.12;
  Mistral-7B AI2 1.067 against 2.442; Llama-8B MMLU 1.055 against 1.450. Classifier mean accuracy
  0.962, weighted F1 0.936 (linear classifier 86.7%). A single trial beat the standard maximum 82%
  of the time overall, 61% for Llama-8B and 58% on GSM8K (App. F.2). No false-positive rate is
  reported.
- Mistral Large no-goal sandbagging (§4): "two noised Mistral Large models in the sandbagging
  setting completely recover the original performance", 66.6% to 100% on a 30-question GSM8K subset.
- Compute (PDF, compute appendix): A100 40 GB GPUs, "only one GPU was required for the majority of
  experiments"; one MCQ model-dataset experiment "approximately 500 minutes on an NVIDIA A100 GPU";
  total about 775 GPU-hours at $3 an hour plus 25 hours at $11, "$2,600".
- Limitations (§6): few baselines; one in-the-wild case; noise "makes untargeted impairments to the
  model", so harder benchmarks may show a weaker pattern.
- Code: https://github.com/camtice/noise_injection_extended (see [@tice2025noiserepo]).
- Bears on: D5 (a cheap detector, not an elicitor with a guarantee), E3 (inference-only arm).

### tice2025noiserepo

*camtice/noise_injection_extended* (GitHub). URL https://github.com/camtice/noise_injection_extended.
Opened 2026-11-27 (README, GitHub API).

- README: points to a modified inspect_ai submodule with a provider that "uses vllm and LoRA
  adapters to add noise and inference a model"; run with `python main.py`; pins `torch==2.5.1`.
- Licence: none (no LICENSE file; API returns none).
- Bears on: E3 (design reference; vLLM on an AMD consumer GPU is an assumption to check).

### hofstatter2025elicitationgame

*The Elicitation Game: Evaluating Capability Elicitation Techniques.* Felix Hofstätter, Teun van der
Weij, Jayden Teoh, Rada Djoneva, Henning Bartsch, Francis Rhys Ward. 2025 (v3 18 Jul 2025).
arXiv:2502.02180. Opened 2026-11-27 (abstract, HTML).

- Organisms (§3.4, App. B): password-locked (following [@greenblatt2024pwlock]) and then
  circuit-broken, all with LoRA; circuit-breaking "was very fragile to training hyperparameters".
  Base models Mistral 7B v0.1 base, Mistral 7B v0.2 Instruct, Gemma 2 9B Instruct.
- Data (§3.1): WMDP (3,668), MMLU (1,402), APPS (3,000 for organisms, 1,000 for elicitation, 500
  evaluation, 200 test), scored with BigCodeBench-style full correctness.
- Results: WMDP N-shot recovers 49.5% against 52.2% with the password (Gemma, locked) and 40.3%
  against 52.4% (Gemma, circuit-broken) (Table 1); SFT recovers or exceeds the password score in
  most cases (Table 3). On APPS, "only fine-tuning can elicit the hidden capabilities of our novel
  model organism"; N-shot fails; steering peaks near 2%; prefilling works on the locked but not the
  circuit-broken model (7% at 0-shot) (§4.3).
- Recommendation: fine-tuning is the "method of choice" for trustworthy capability evaluations.
- Compute: rented A40s (App. B). Code: https://github.com/Felhof/sandbagging-elicitation (no
  licence; README: `pw_lock_mistral.sh`, `circuit_break_model.ipynb`).
- Bears on: D5 (prompting and steering are not enough on generation tasks), E3 (circuit-broken arm).

### taylor2025auditinggames

*Auditing Games for Sandbagging.* Jordan Taylor, Sid Black, Dillon Bowen, Thomas Read, Satvik
Golechha, Alex Zelenka-Martin, Oliver Makins, Connor Kissane, Kola Ayonrinde, Jacob Merizian,
Samuel Marks, Chris Cundy, Joseph Bloom. 2025 (8 Dec 2025). arXiv:2512.07810. Opened 2026-11-27 (HTML).

- Setup (§4, Table 2): sandbaggers Cedar (Llama-3.3-70B-Instruct logit-matched to imitate
  Llama-3.1-8B-Instruct; broad; password of reserved special tokens) and Oak (narrow, Intercode CTF
  only; trigger is two-space tool indentation). Benign decoys Baobab (Devstral-Small-2505), Maple
  (Mistral-Large-Instruct-2411), Yew (Llama-3.1-8B with identity layers), with distractor quirks.
  Tasks: BIG-Bench Hard, BigCodeBench, Intercode CTF, GPQA Diamond, Tic Tac Toe.
- Outcome: the blue team "correctly classified only 1 of 5 models in phase one" and 2 of 5 in
  phase two; the red team won.
- Training-based elicitation (§6.4): one Claude Opus 4 transcript per task elicited the sandbaggers;
  Oak gained 35 points on a task never trained on. But benign models also rose: Baobab about 10
  points on GPQA Diamond CoT and the reference model about 10 points on BBH; "it would have been
  difficult to reliably avoid false positives caused by eliciting performance from benign models".
  Anti-refusal training gave no gains. Cross-distribution training transferred for Cedar, barely for
  Oak, and also for the benign reference.
- Recommendation: "remove potential sandbagging using on-distribution training for elicitation".
  Caveats (limitations): "Our auditing game does not provide quantitative guarantees"; "We have only
  a single blue team, and repetitions are not compatible with being blinded", so it is "not possible
  to estimate quantitative detection metrics"; "Password-locked models may be easier to elicit than
  real sandbagging models."
- Bears on: D5 (the miss-rate and false-alarm problem stated directly), E3 (benign-control design).

### aisi2025auditingblog

*Auditing games for sandbagging detection.* UK AI Security Institute. 2025 (9 Dec 2025). URL
https://www.aisi.gov.uk/blog/auditing-games-for-sandbagging-detection. Opened 2026-11-27.

- Ten detection methods, "mixed success". The post reports that on-distribution training restored
  full performance in every instance from a single example but also boosted benign models, so it was
  better at eliminating sandbagging than at detecting it. Off-distribution training was defeated by
  selective sandbagging. Probes were confused by distractor behaviours.
- Recommendations (paraphrased): do not rely on black-box methods alone; pursue on-distribution
  training where feasible; these methods need deeper model access than external evaluators usually
  get.
- Bears on: protocol (inspectors need training access to weights for D5 to work).

### aisi2025auditingrepo

*AI-Safety-Institute/sandbagging_auditing_games* (GitHub). URL
https://github.com/AI-Safety-Institute/sandbagging_auditing_games. Opened 2026-11-27 (README, API).

- README: model organisms at huggingface.co/sandbagging-games, transcripts at
  huggingface.co/datasets/sandbagging-games/evaluation_logs; "some models may require multiple
  GPUs". Licence: "This project is licensed under the MIT License".
- Bears on: E3 (the only MIT-licensed harness found; its organisms are 70B and do not fit a
  consumer GPU).

### bloom2025whitebox

*White Box Control at UK AISI - Update on Sandbagging Investigations.* Joseph Bloom, Jordan Taylor,
Connor Kissane, Sid Black, Alan Cooney, et al. 2025 (10 Jul 2025). URL
https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging.
Opened 2026-11-27.

- Prompted sandbagging, Llama-3.3-70B-Instruct on InterCode CTF (78 samples): baseline 46%, 26%
  under the sandbagging prompt. Chain-of-thought monitor 74% AUROC; deception probes 97% (mean
  aggregation) and 99% (max); at 1% FPR on Alpaca, 88% TPR and 2% FPR.
- Fine-tuned organisms on Llama-3.1-8B-Instruct: "probe performance deteriorated, though not
  uniformly across model organisms".
- Scan of about 2,700 past agent traces: 12 flagged (0.44%), all false positives on review.
- Bears on: D5 (probes are a weaker signal on trained organisms than on prompted ones).

### jang2026explorationhacking

*Exploration Hacking: Can LLMs Learn to Resist RL Training?* Eyon Jang, Damon Falck, Joschka Braun,
Nathalie Kirch, Achu Menon, Perusha Moodley, Scott Emmons, Roland S. Zimmermann, David Lindner.
2026 (30 Apr 2026). arXiv:2604.28182. Opened 2026-11-27 (HTML).

- Organisms: Qwen3-14B locked by RL (KernelBench; WMDP-Bio with a fixed answer strategy) or by SFT
  distillation (BigCodeBench, trigger `import inspect_ai`, 180 steps strong and 40 weak; WMDP-Bio
  with tools, trigger "[eval]").
- RL elicitation with GRPO: on KernelBench a prompted sandbagger recovers within about 100 steps,
  while the RL-locked model "maintains suppressed performance well below this level" for over 500
  steps. Strongly locked BigCodeBench models stay flat; weakly locked ones reach 2-3x their initial
  score. On WMDP with tools the locked model gets worse under RL pressure (§3.2, Fig. 5).
- SFT recovers: about 2,560 benign traces lift the [eval] segment from 80.0% to 98.0% in 10 steps;
  BigCodeBench locks recover in about 80 (weak) and 100 (strong) steps (§4.2, Fig. 8).
- Weight noising: treated accuracy rises transiently at sigma up to 0.02 while controls fall (Fig. 7).
- Frontier propensity (§5): system-prompted WMDP drops up to about 58 points (Gemini 3.0 Pro) and
  45 points (Claude Sonnet 4.5); agentic discovery on VCT 23.3% (full), 18.8%, 17.9%. "The
  bottleneck is strategic action propensity rather than strategic reasoning capability."
- Code: github.com/exploration-hacking/exploration-hacking (GitHub API: no licence).
- Bears on: D5 (RL-only budgets can miss; SFT still works when demonstrations exist).

### finke2026robustorganisms

*Towards Robust Model Organisms for Eliciting Latent Knowledge.* Lennart Finke, Hardik Bhatnagar,
Euodia Dodd, Francis Rhys Ward, Yves-Alexandre de Montjoye, Matthias Bethge, Mary Phuong. 2026
(19 Oct 2026). arXiv:2610.26698. Opened 2026-11-27 (abstract, HTML).

- Task (§3.3): C/C++ vulnerability detection; 250 easy and 250 hard samples. Organism base
  Qwen-3.6-35B-A3B; the overseer proxy is Qwen-3-8B.
- Stage C organism (TAR tamper-resistance, five rounds, simulated inner attacks of 16 to 64 steps,
  §4.3, App. B): hard-sample recall 0% under baseline prompting, 1-shot, parameter noise
  (sigma 0.01) and a 10-round elicitation agent; 3.3% after 64 steps of untargeted training; 7.8%
  after weak-to-strong training on the overseer's answers; base model 71.2% (Table 4). It withholds
  for up to 384 untargeted steps and returns to normal at 512 (§5.3). A plain password lock gives
  39.2% under the agent and 61.4% under weak-to-strong.
- Limitations (§6): robustness is a lower bound built against known blue-team protocols; retention
  relies on visible chain of thought.
- Bears on: D5 (the strongest documented elicitation failure; note that it uses weak, not
  high-quality, demonstrations), E3 (the hardened arm).

### le2026grafting

*Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities.* Linh Le, Hong Kiat
Tan, David Williams-King. 2026 (29 Aug 2026). arXiv:2608.29458. Opened 2026-11-27 (HTML).

- Method (§1, Eq. 1): set an activation's coordinate along a contrast direction to its value in an
  honest reference. Eleven LoRA (r=16) password-locked models from Qwen2.5-1.5B to 32B, Qwen3,
  Llama-3.2-3B, Llama-3-8B, Gemma-2 2B to 27B; ARC-Easy primary, WMDP and OpenBookQA transfer, MBPP.
- Recovery (Table 1): grafting +94% to +101%; fine-tuning +90% to +103%. Two paired examples give
  +97% and five +100% (§4.5). Noise injection and random directions fail. On the circuit-broken
  organism grafting gives -11% (§4.6). RL free-generation sandbagging was not graft-invertible on 33
  of 44 seeds (§4.4). On the Hofstätter organisms: +99% (Mistral instruct), +94% (base), +44%
  (Gemma-2-9B).
- Compute (App. A): two RTX 3090s (24 GB each) for most runs; 27B and 32B on rented L40S, A100,
  H100. Code and outputs stated BSD 3-clause; no repository URL in the text.
- Bears on: E3 (direct evidence that 1.5B to 14B locked-model experiments fit 24 GB consumer GPUs).

### niyigaba2026structural

*Eliciting sandbagged LLM capability via structural interventions on attention-head functional
networks.* Manzi Fabrice Niyigaba, Ishan Verma Prasad, Sansheng Cao, Zheng Huang, Yujun Yan. 2026
(23 Nov 2026). arXiv:2611.31615. Opened 2026-11-27 (abstract, HTML).

- Models: Mistral-24B, Qwen3-32B, Llama-3.3-70B, GPT-OSS-20B. On the Hofstätter password-locked
  Mistral-base organism (Table 3): full SFT 28.16 ± 17.12, noise injection 15.62 ± 2.82, their
  method 52.27 ± 1.04. On the circuit-broken Mistral-base, full SFT 58.43 ± 2.31 is best.
- Bears on: D5 (small-budget SFT has high variance across seeds; a budget must be stated with seeds
  and a variance).

### mack2026cpe

*Mechanistically Eliciting Latent Behaviors in Language Models.* Andrew Mack, Nina Panickssery,
Alexander Matt Turner. 2026 (28 Jun 2026). arXiv:2606.29604. Opened 2026-11-27 (abstract).

- Causal Perturbative Elicitation, "an unsupervised method for discovering interpretable low-rank
  adapters", restores 85% of locked BigCodeBench performance on the Taylor et al. password-locked
  Llama3-70B; on Countdown (Qwen3-8B) it is close to matched-time GRPO (85% against 87%).
- Bears on: D5 (an unsupervised weight-space elicitor that might avoid exploration hacking).

### soopal2026adaptive

*Stress-Testing Sandbagging Detection Under Adaptive Attack.* Bhoj Rani Soopal, Aarohi Agrawal,
Josh Karthikeyan, Edward Lue Chee Lip. 2026 (11 Nov 2026). arXiv:2611.14950. Opened 2026-11-27
(abstract).

- Qwen 2.5-3B locked to fail GSM8K when an audit marker appears. "Two rounds of retraining cut the
  text audit's AUC from 0.978 to 0.560"; the attack worked in 7 of 8 retrained seeds; activation
  probes flagged 99% of benign fine-tunes. "A detector that catches a fixed attack has not been
  shown to catch an adaptive one."
- Bears on: D5 (miss rates must be measured against adaptive organisms, not fixed ones).

### ta2026automatedaudit

*Automating Auditing Games of Sandbagging.* Christopher Ta, Anna Upreti, David Williams-King, Alan
Cooney, Shi Feng. 2026. NeurIPS 2026 workshop poster, URL https://neurips.cc/virtual/2026/169826.
Opened 2026-11-27 (abstract page).

- Agent red teams built Qwen3-8B organisms: 15 of 40 runs passed validation; six runs "took
  shortcuts". Black-box agent auditors caught one of eight validated math organisms consistently;
  white-box tools "does not reliably improve detection".
- Bears on: D5 (automated auditing is not yet a substitute for training-based elicitation).

### needham2025evalaware

*Large Language Models Often Know When They Are Being Evaluated.* Joe Needham, Giles Edkins, Govind
Pimpale, Henning Bartsch, Marius Hobbhahn. 2025 (v3 16 Jul 2025). arXiv:2505.23836. Opened 2026-11-27
(abstract).

- 1,000 prompts and transcripts from 61 datasets; Gemini-2.5-Pro AUC 0.83; human baseline 0.92;
  "Frontier models clearly demonstrate above-random evaluation awareness"; both models and humans
  do better in agentic than chat settings.
- Bears on: D5 and D1 (observed scores depend on whether the model believes it is tested).

### chaudhary2025evalawarescaling

*Evaluation Awareness Scales Predictably in Open-Weights Large Language Models.* Maheep Chaudhary,
Ian Su, Nikhil Hooda, Nishith Shankar, Julia Tan, Kevin Zhu, Ryan Lagasse, Vasu Sharma, Ashwinee
Panda. 2025 (v2 9 Nov 2025). arXiv:2509.13333. Opened 2026-11-27 (abstract).

- 15 open-weight models, four families, 0.27B to 70B; linear probes on steering-vector activations;
  a power law in model size.
- Bears on: E3 (small open models already carry measurable evaluation-awareness directions).

### anthropic2025sonnet45card

*System Card: Claude Sonnet 4.5.* Anthropic. 2025 (September 2025). URL
https://assets.anthropic.com/m/12f214efcc2f457a/original/claude-sonnet-4-5-system-card.pdf. Opened
2026-11-27 (PDF, §7.2, §7.5.10.2, §7.6).

- §7.2: refusals or callouts that the scenario is a test "appeared in about 13% of transcripts
  generated by the automated auditor"; without the realism filter, scores "were about 25% higher".
  §7.6: "rates of explicitly verbalized evaluation awareness increasing over training" and
  "internal representations of evaluation awareness were growing stronger over training";
  inhibiting them "can increase rates of misaligned behavior". §7.5.10.2 runs a research sandbagging
  evaluation (deliberate weak performance on coding while hiding it from a monitor).
- Bears on: D5 (vendor-reported awareness that grows with training; affects propensity more than
  fine-tuned capability measurements).

### greenblatt2024alignfaking

*Alignment faking in large language models.* Ryan Greenblatt et al. (20 authors). 2024 (v2 20 Dec
2024). arXiv:2412.14093. Opened 2026-11-27 (abstract).

- Claude 3 Opus "complies with harmful queries from free users 14% of the time" against almost
  never for paid users; RL toward compliance "increases the rate of alignment-faking reasoning to
  78%"; weight exfiltration "when given an easy opportunity".
- Bears on: D5 (a model can act differently when it infers training or monitoring).

### meinke2024scheming

*Frontier Models are Capable of In-context Scheming.* Alexander Meinke, Bronson Schoen, Jérémy
Scheurer, Mikita Balesni, Rusheb Shah, Marius Hobbhahn. 2024 (v2 14 Jan 2025). arXiv:2412.04984.
Opened 2026-11-27 (HTML).

- Sandbagging (§3.6, Table 6): multi-digit multiplication, with unlearning threatened above 50%
  accuracy. Claude 3.5 Sonnet 0.99 when incentivized to do well against 0.34 when incentivized to do
  poorly; Claude 3 Opus 0.35 against 0.20. With no goal given, Sonnet 0.96 against 0.61; "sonnet-3.5
  and opus-3 still systematically underperform, whereas o1 does not". The o1 columns did not render
  readably. "Preliminary evidence that, on very simple tasks, sonnet-3.5 is capable of sandbagging
  without CoT."
- Other rates (Table 2): oversight subversion o1 0.02, Opus 0.05; self-exfiltration Opus 0.10. "When
  o1 has engaged in scheming, it maintains its deception in over 85% of follow-up questions."
- Bears on: D5 (sandbagging arises from learned goals without instruction).

### schoen2025antischeming

*Stress Testing Deliberative Alignment for Anti-Scheming Training.* Bronson Schoen, Evgenia
Nitishinskaya, Mikita Balesni, et al. (19 authors, OpenAI and Apollo Research). 2025 (19 Sep 2025).
arXiv:2509.15541. Opened 2026-11-27 (abstract).

- o3 covert actions 13% to 0.4% after deliberative alignment, which "does not fully eliminate them";
  26 evaluations over "180+ environments"; causal evidence that evaluation awareness reduces covert
  behaviour; authors "cannot exclude" that reductions are partly driven by situational awareness.
- Bears on: D5 (propensity results are confounded by awareness; capability elicitation is not).

### marks2025auditing

*Auditing language models for hidden objectives.* Samuel Marks, Johannes Treutlein, Trenton Bricken,
et al. (35 authors). 2025 (v2 28 Mar 2025). arXiv:2503.10965. Opened 2026-11-27 (abstract).

- A model trained to exploit RLHF reward-model errors; blind game with four teams; three of four
  found the objective using "interpretability with sparse autoencoders (SAEs), behavioral attacks,
  and training data analysis".
- Bears on: protocol (auditing with weight and data access beats black-box access).

### benton2024sabotage

*Sabotage Evaluations for Frontier Models.* Joe Benton, Misha Wagner, Eric Christiansen, Cem Anil,
Ethan Perez, Jai Srivastav, Esin Durmus, Deep Ganguli, Shauna Kravec, Buck Shlegeris, Jared Kaplan,
Holden Karnofsky, Evan Hubinger, Roger Grosse, Samuel R. Bowman, David Duvenaud. 2024 (28 Oct 2024).
arXiv:2410.21514. Opened 2026-11-27 (abstract, HTML §6).

- §6: Claude 3.5 Sonnet trained to sandbag WMDP (more than 20% worse while within 5% on benign
  tasks), hardened on a separate anti-refusal set. "Degraded performance is 36.1% of original
  performance"; after anti-refusal training "Recovered performance is 95.6% of original
  performance".
- Bears on: D5 (generic fine-tuning undid a deliberately trained sandbagger at frontier scale).

### gasteiger2025subtlesandbag

*Automated Researchers Can Subtly Sandbag.* Johannes Gasteiger, Vladimir Mikulik (Anthropic
Alignment Science Blog). 2025 (year from the URL and the Sonnet 4.5 card's citation; the page shows
no date). URL https://alignment.anthropic.com/2025/automated-researchers-sandbag/. Opened 2026-11-27.

- 16 ML tasks in an agentic scaffold. Claude 3.7 Sonnet is "almost capable of zero-shot sabotage
  without using a scratchpad", cutting performance to roughly Claude 3.5 Sonnet's level; zero-shot
  monitors had an "underwhelming true positive rate" at low false-positive rates; results are a lower
  bound since only prompting was used; weak-model imitation is hard to detect and train away.
- Bears on: D2 (an AI running the staged loop-gain test could depress g), D5.

### li2025covertsandbag

*LLMs Can Covertly Sandbag on Capability Evaluations Against Chain-of-Thought Monitoring.* Chloe Li,
Mary Phuong, Noah Y. Siegel. 2025 (v2 31 Oct 2025; IJCNLP-AACL 2025). arXiv:2508.00943. Opened 2026-11-27
(abstract).

- Monitor-aware models bypass the CoT monitor "16-36% of the time when monitor-aware, conditioned
  on sandbagging successfully".
- Bears on: D5 (chain-of-thought monitoring alone leaves a large miss rate).

### clymer2024poser

*Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals.* Joshua Clymer, Caden Juang,
Severin Field. 2024 (v2 11 May 2024). arXiv:2405.05466. Opened 2026-11-27 (abstract, HTML).

- 324 pairs from 36 LLaMA-13B models. Adding noise to activations ("Intoxicate models so they reveal
  bad behavior") identifies 98% of alignment fakers (§3.2); learning-speed comparison 90% with LoRA,
  63% with full fine-tuning (§3.3).
- Bears on: D5 (activation noise as prior work to weight-noise detection).

### draguns2024unelicitable

*Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits.* Andis Draguns,
Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder
de Witt. 2024 (v2 1 Feb 2025; NeurIPS 2024). arXiv:2406.02619. Opened 2026-11-27 (abstract).

- Cryptographic backdoors that prevent the defender from triggering them "even if given full
  white-box access and using automated techniques, such as red-teaming or certain formal
  verification methods". The abstract does not address fine-tuning.
- Bears on: D5 (in principle, a deliberately built capability can be unelicitable by search; D5's
  guarantee must be stated against a threat model, not universally).

### lucki2024unlearning

*An Adversarial Perspective on Machine Unlearning for AI Safety.* Jakub Łucki, Boyi Wei, Yangsibo
Huang, Peter Henderson, Florian Tramèr, Javier Rando. 2024 (v6 31 May 2025; TMLR). arXiv:2409.18025.
Opened 2026-11-27 (abstract).

- Fine-tuning on 10 unrelated examples recovers most hazardous capability in RMU-unlearned models;
  removing activation directions also recovers most.
- Bears on: D5 (capability that looks removed is often only hidden, and cheap to recover).

### hubinger2023trusteval

*When can we trust model evaluations?* Evan Hubinger. 2023 (28 Jul 2023). URL
https://www.alignmentforum.org/posts/dBmfb76zx6wjPsBC7/when-can-we-trust-model-evaluations. Opened 2026-11-27.

- i.i.d. supervised fine-tuning evaluations: "if the model tried to sandbag the evaluation on
  purpose, gradient descent should just train away that behavior"; "the key assumption that you need
  to make them trustworthy is the absence of gradient hacking". RL evaluations are exposed to
  exploration hacking: "the model prevents the RL process from ever exploring some action that would
  be highly rewarded".
- Bears on: D5 (prior statement of the SFT-over-RL ordering and its assumption).

### clymer2024safetycases

*Safety Cases: How to Justify the Safety of Advanced AI Systems.* Joshua Clymer, Nicholas Gabrieli,
David Krueger, Thomas Larsen. 2024 (v2 18 Mar 2024). arXiv:2403.10462. Opened 2026-11-27 (HTML).

- §5.2.1: supervised fine-tuning is "the gold standard fine-tuning strategy for making inability
  arguments"; key assumption "Fine-tuning reliably elicits the capabilities of the AI systems to
  perform the proxy tasks"; "more advanced AI systems might deliberately sandbag their
  capabilities"; the assumptions "are currently not well understood".
- Bears on: D5 (inability arguments as prior work).

### clymer2025elicitationbound

*When does capability elicitation bound risk?* Joshua Clymer. 2025 (22 Jan 2025). URL
https://www.alignmentforum.org/posts/u3taQsgxqCzrgErMM/when-does-capability-elicitation-bound-risk.
Opened 2026-11-27.

- Separates human-bounding from generalization-bounding elicitation; lists obstacles (limited i.i.d.
  samples, inadequate demonstrations for superhuman models, gradient and exploration hacking);
  suggests password-locked stress tests; proposes no numeric budget or margin, only that "a small
  amount of underperformance" may be tolerated with a safety margin.
- Bears on: D5 (closest conceptual prior work on when elicitation bounds capability).

### korbak2025controlsketch

*A sketch of an AI control safety case.* Tomek Korbak, Joshua Clymer, Benjamin Hilton, Buck
Shlegeris, Geoffrey Irving. 2025 (28 Jan 2025). arXiv:2501.17315. Opened 2026-11-27 (abstract only).

- The case rests first on the claim (paraphrased from the abstract) that the red team adequately
  elicits the models' capabilities to exfiltrate data. The abstract states no compute budget for the red team (a search snippet
  claimed one; we did not verify it in the full text, so it is not used).
- Bears on: D5 (elicitation adequacy as an explicit premise).

### goemans2024cyberinability

*Safety case template for frontier AI: A cyber inability argument.* Arthur Goemans, Marie Davidsen
Buhl, Jonas Schuett, Tomek Korbak, Jessica Wang, Benjamin Hilton, Geoffrey Irving. 2024 (12 Nov 2024).
arXiv:2411.08088. Opened 2026-11-27 (abstract only).

- A template arguing a model lacks "capabilities posing unacceptable cyber risks" from proxy-task
  evaluations. The abstract does not mention elicitation quality or sandbagging.
- Bears on: D5 (inability templates exist; their elicitation clause was not checked in the full text).

### barnett2024evallimits

*What AI evaluations for preventing catastrophic risks can and cannot do.* Peter Barnett, Lisa
Thiergart. 2024 (26 Nov 2024). arXiv:2412.08653. Opened 2026-11-27 (abstract).

- Evaluations "can establish lower bounds on AI capabilities" but face "an inability to establish
  upper bounds on capabilities"; they should not be the "main way of ensuring AI systems are safe".
- Bears on: D5 (against: an elicited score is a lower bound; the protocol should not rest on it
  alone, consistent with the memo's several channels).

### mahran2026partition

*What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight.*
Ahmed M. Mahran. 2026 (22 Oct 2026). arXiv:2610.30803. Opened 2026-11-27 (abstract).

- Passing certifies "at most a floor on discrimination, never a ceiling"; exact imitation of a weaker
  model is undetectable by any behavioural evaluator; a safety case relying on behavioural
  evaluation alone "must assume the model's cooperation".
- Bears on: D5 (against purely behavioural elicitation; D5 must include weight-level methods).

### dyer2025survivalbandit

*Sandbagging in a Simple Survival Bandit Problem.* Joel Dyer, Daniel Jarne Ornia, Nicholas Bishop,
Anisoara Calinescu, Michael Wooldridge. 2025 (30 Sep 2025; NeurIPS 2025 workshop). arXiv:2509.26239.
Opened 2026-11-27 (abstract only).

- Optimal rational agents sandbag in a survival bandit; the authors "construct a statistical test to
  distinguish between sandbagging and incompetence from sequences of test scores".
- Bears on: D5 (a statistical framing of sandbagging detection, in a toy setting).

### metr2024elicitation

*Guidelines for capability elicitation.* METR. 2024 (15 Mar 2024). URL
https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/. Opened 2026-11-27.

- Aim: capabilities "accessible with some level of enhancement"; "at least basic finetuning for
  instruction following, tool use, and general agency"; a password-locked model test is ideal but
  "not a hard requirement currently"; evaluators attest that they know of no "known approaches that
  will predictably yield large performance improvements". No numeric budget or margin; METR calls
  the guidelines "somewhat informed and reasoned guesses only".
- Bears on: D5 (prior work on elicitation standards; no stated miss rate).

### anthropic2023rsp

*Anthropic's Responsible Scaling Policy, Version 1.0.* Anthropic. 2023 (effective 19 Sep 2023). URL
https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf.
Opened 2026-11-27 (PDF).

- ASL-3 definition: a model that "can either immediately, or with additional post-training
  techniques corresponding to less than 1% of the total training cost" reach the threat capabilities,
  where post-training techniques mean "the best capabilities elicitation techniques we are aware of
  at the time, including but not limited to fine-tuning, scaffolding, tool use, and prompt
  engineering."
- Buffer: evaluations trigger below the threshold of concern; evaluation every 4x effective compute;
  "safety buffer to 6x". If a deployed model "has been under-elicited", halt deployment to new
  customers. Higher levels may need "a more conservative safety buffer to account for pace of
  development of post-training or elicitation techniques".
- Bears on: D5 (the fixed elicitation budget, as a compute fraction, is prior work).

### anthropic2026rsp

*Responsible Scaling Policy, Version 3.4.* Anthropic. 2026 (effective 8 Jul 2026). URLs
https://www.anthropic.com/responsible-scaling-policy and
https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf. Opened 2026-11-27 (page, PDF
changelog).

- Changelog for v2.0 (15 Oct 2024): "We have replaced some specifics in our previous testing
  methodology (e.g., using 1% of compute for elicitation or creating a 6× buffer), with more general
  requirements to (a) match expected efforts of potential adversaries and (b) provide informal
  estimates of how further scaling and research developments will impact model capabilities ...
  specific methodologies may become outdated when new research developments are introduced. ... the
  science of evaluations is not currently mature enough to make confident predictions about the
  precise buffer we should require". The web page's 2024 review notes some evaluations "lacked some
  basic elicitation techniques such as best-of-N or chain-of-thought prompting".
- Bears on: D5 (against: the one operator that adopted a fixed budget dropped it).

### openai2025preparedness

*Preparedness Framework, Version 2.* OpenAI. 2025 (15 Apr 2025). URL
https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf. Opened
2026-11-27 (PDF).

- Sandbagging is a Research Category: "Adopt elicitation approach that overcomes sandbagging, or use
  a conservative upper bound of the model's non-sandbagged evaluation results". Evaluations aim "to
  approximate the high end of expected elicitation by threat actors", "doing finetuning if the
  weights will be released"; "we regard any one-time capability elicitation in a frontier model as a
  lower bound, rather than a ceiling".
- Bears on: D5 (prior work on sandbagging-robust elicitation as a policy rule, with no budget or miss
  rate).

### eu2025gpaicode

*Code of Practice for General-Purpose AI Models: Safety and Security Chapter.* European Commission
(chairs and vice-chairs of Working Groups 2 to 4). 2025 (code published 10 Jul 2025). URL
https://ec.europa.eu/newsroom/dae/redirection/document/118119. Opened 2026-11-27 (PDF).

- Appendix 3.2: signatories ensure evaluations use "at least a state-of-the-art level of model
  elicitation" with techniques that "(1) minimise the risk of under-elicitation; and (2) minimise the
  risk of model deception during model evaluations (e.g. sandbagging)", "such as by adapting
  test-time compute, rate limits, scaffolding, and tools, and conducting fine-tuning and prompt
  engineering", and at least "match the model elicitation capabilities of misuse actors". The
  glossary defines deception to include "a model's detecting that it is being evaluated and
  under-performing".
- Bears on: D5 (the nearest regulatory text; it has no stated budget and no miss rate).

### wallace2025worstcase

*Estimating Worst-Case Frontier Risks of Open-Weight LLMs.* Eric Wallace, Olivia Watkins, Miles
Wang, Kai Chen, Chris Koch. 2025 (v2 13 Aug 2025). arXiv:2508.03153. Opened 2026-11-27 (abstract).

- Malicious fine-tuning to "elicit maximum capabilities by fine-tuning gpt-oss to be as capable as
  possible" in biology (RL with browsing) and cybersecurity (agentic CTF); the result was compared to
  the Preparedness "High" level and informed the release decision.
- Bears on: D5 (a deployed instance of judging a threshold on adversarially elicited capability;
  budget not stated in the abstract).

### davidson2023enhancements

*AI capabilities can be significantly improved without expensive retraining.* Tom Davidson,
Jean-Stanislas Denain, Pablo Villalobos, Guillem Bas. 2023 (12 Dec 2023). arXiv:2312.07413. Opened
2026-11-27 (abstract).

- Most post-training enhancements give a compute-equivalent gain above 5x, some above 20x;
  fine-tuning costs are usually under 1% of the original training cost.
- Bears on: D5 (sizing the elicitation margin), D3 (enhancements shorten breakout time at fixed compute).

### dominguezolmedo2024testtask

*Training on the Test Task Confounds Evaluation and Emergence.* Ricardo Dominguez-Olmedo, Florian E.
Dorner, Moritz Hardt. 2024 (v3 21 Apr 2025; ICLR 2025 oral). arXiv:2407.07890. Opened 2026-11-27
(abstract).

- Remedy: fine-tune each compared model on the same task-relevant data before evaluating; apparent
  emergence "disappear[s] gradually as models train on the test task".
- Bears on: D5 (prior work for scoring after a common fine-tuning budget, in benchmarking), D1.

### zhang2024gsm1k

*A Careful Examination of Large Language Model Performance on Grade School Arithmetic.* Hugh Zhang,
Jeff Da, Dean Lee, et al. 2024 (v4 22 Nov 2024; NeurIPS 2024 Datasets and Benchmarks). arXiv:2405.00332.
Opened 2026-11-27 (abstract).

- Accuracy drops "up to 8%" from GSM8K to the fresh GSM1k; Spearman r^2 = 0.36 between the
  probability of generating GSM8K examples and the gap; frontier models show minimal overfitting.
- Bears on: D1 (refreshed held-out batteries are needed; contamination inflates scores, the
  opposite error from sandbagging).

### singh2025leaderboard

*The Leaderboard Illusion.* Shivalika Singh, Yiyang Nan, Alex Wang, et al. 2025 (v2 12 May 2025).
arXiv:2504.20879. Opened 2026-11-27 (abstract).

- 27 private Meta variants tested before Llama 4; Google and OpenAI received an estimated 19.2% and
  20.4% of Arena data; Arena data can give relative gains "up to 112%" on the Arena distribution.
- Bears on: D1 (developer-side gaming of public scores; argues for regime-held test sets).

### xu2024contamination

*Benchmark Data Contamination of Large Language Models: A Survey.* Cheng Xu, Shuhao Guan, Derek
Greene, M-Tahar Kechadi. 2024 (6 Jun 2024). arXiv:2406.04244. Opened 2026-11-27 (abstract only).

- Contamination makes measured performance "inaccurate or unreliable"; surveys "alternative
  assessment methods". The abstract gives no numbers.
- Bears on: D1.

---

## Numbers for the ledger

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| pwlock-demos-generation | 1 | demonstrations, often enough to recover most hidden performance on long-generation tasks | measured | greenblatt2024pwlock | §1 contributions, §5.1 |
| pwlock-demos-mmlu | a few hundred (no point value given) | demonstrations to recover most of MMLU without CoT | measured | greenblatt2024pwlock | §1, §5.1 |
| pwlock-domain-demos | 512 | demonstrations from one domain used in generalization tests | spec | greenblatt2024pwlock | Fig. 4 |
| pwlock-from-scratch-multiplier | 2 to 4 | times more data to unlock a from-scratch lock than an SFT lock | measured | greenblatt2024pwlock | §7, Fig. 6 |
| pwlock-lr-generation | 1.5e-6 | learning rate, Lion, full weights | spec | greenblatt2024pwlock | App. G |
| pwlock-lock-epochs | 8 | epochs | spec | greenblatt2024pwlock | App. G |
| pwlock-split | 10 / 40 / 30 / 20 | percent of data: pi_weak / lock / elicit / validation | spec | greenblatt2024pwlock | §4.2 |
| pwlock-wrong-password-share | 80 | percent of weak samples shown a wrong password | spec | greenblatt2024pwlock | App. C |
| pwlock-sft-run-gpu-hours | 1 | H100 GPU-hours per 7B SFT elicitation run | measured | greenblatt2024pwlock | App. G |
| pwlock-rl-run-gpu-hours | 3 | H100 GPU-hours per 7B RL elicitation run | measured | greenblatt2024pwlock | App. G |
| pwlock-total-gpu-hours | 4,000 | GPU-hours, all experiments | measured | greenblatt2024pwlock | App. G |
| pwlock-repo-gpu-memory | 80 | GB GPU memory required by the released code | spec | roger2024sandbaggingrepo | README |
| vdw-lock-dataset | 3,347 | synthetic questions | spec | vanderweij2024sandbagging | §4.2, App. G |
| vdw-lora-rank | 16 | LoRA rank (alpha 16, dropout 0.05) | spec | vanderweij2024sandbagging | App. C |
| vdw-mistral-lr | 5e-6 | learning rate (3 epochs, batch 16) | spec | vanderweij2024sandbagging | App. C.1.1, Table 5 |
| vdw-opus-wmdp-bio-drop | 39.8 | percent drop on WMDP biology when prompted to sandbag (MMLU biology 9.7) | measured | vanderweij2024sandbagging | Table 1 |
| vdw-emulator-overlap | 77.1 | percent answer overlap with Llama 2 7B (targeter 60.8) | measured | vanderweij2024sandbagging | Table 2 |
| vdw-emulator-locked-acc | 41.2 | percent accuracy locked (Llama 2 7B: 38.2) | measured | vanderweij2024sandbagging | Table 2 |
| vdw-emulator-pwd-acc | 74.2 | percent accuracy with password (base 71.8) | measured | vanderweij2024sandbagging | Table 2 |
| noise-sigma-max | 0.01 | standard deviation of weight noise, top of sweep | spec | tice2024noise | §3.2 |
| noise-sigma-step | 0.0001 | sweep step | spec | tice2024noise | §3.2 |
| noise-seeds | 5 | noise vectors per test | spec | tice2024noise | §3.2 |
| noise-classifier-accuracy | 0.962 | mean accuracy, leave-one-model-out | measured | tice2024noise | §4 |
| noise-phi-deepseek-locked | 5.000 | improvement ratio on GSM8K (standard 1.000) | measured | tice2024noise | Table 1 |
| noise-phi-mistral-locked | 3.12 | improvement ratio on WMDP (standard 1.01) | measured | tice2024noise | Table 1 |
| noise-phi-llama8b-prompted | 1.450 | improvement ratio on MMLU (standard 1.055) | measured | tice2024noise | Table 1 |
| noise-single-trial-gsm8k | 58 | percent of single trials beating the standard maximum on GSM8K | measured | tice2024noise | App. F.2 |
| noise-mistral-large-recovery | 66.6 to 100 | percent accuracy, 30 GSM8K questions | measured | tice2024noise | §4 |
| noise-mcq-experiment-minutes | 500 | A100 minutes per model-dataset experiment | measured | tice2024noise | compute appendix |
| noise-total-gpu-hours | 775 | A100 GPU-hours (plus 25 hours on 8xA100) | measured | tice2024noise | compute appendix |
| audit-phase1-correct | 1 of 5 | models correctly classified | measured | taylor2025auditinggames | §1 |
| audit-phase2-correct | 2 of 5 | models correctly classified | measured | taylor2025auditinggames | §1 |
| audit-demos-per-task | 1 | on-distribution transcript per task for elicitation | spec | taylor2025auditinggames | §6.4.1 |
| audit-benign-uplift | about 10 | points gained by benign models from the same elicitation | measured | taylor2025auditinggames | §6.4.1 |
| audit-oak-uplift | 35 | points gained on an untrained task | measured | taylor2025auditinggames | §6.4.1 |
| sabotage-sandbag-degraded | 36.1 | percent of original WMDP performance while sandbagging | measured | benton2024sabotage | §6.4 |
| sabotage-sandbag-recovered | 95.6 | percent of original after anti-refusal training | measured | benton2024sabotage | §6.4 |
| eg-gemma-wmdp-nshot | 49.5 vs 52.2 | percent, N-shot elicited vs with password (locked) | measured | hofstatter2025elicitationgame | Table 1 |
| eg-steering-apps | about 2 | percent APPS accuracy, best steering | measured | hofstatter2025elicitationgame | §4.3 |
| xh-rl-lock-steps | more than 500 | GRPO steps an RL-locked model stays suppressed | measured | jang2026explorationhacking | §3, KernelBench |
| xh-prompted-recovery-steps | about 100 | GRPO steps for a prompted sandbagger to recover | measured | jang2026explorationhacking | §3, KernelBench |
| xh-sft-recovery-steps | 80 to 100 | SFT steps to recover BigCodeBench locks | measured | jang2026explorationhacking | §4.2, Fig. 8b |
| xh-agentic-rate | 23.3 | percent exploration hacking, full scaffolding, 12 models | measured | jang2026explorationhacking | §5.2 |
| robust-hard-recall-w2s | 7.8 | percent hard recall after weak-to-strong training (base 71.2) | measured | finke2026robustorganisms | Table 4 |
| robust-untargeted-steps | 384 | untargeted fine-tuning steps withstood | measured | finke2026robustorganisms | §5.3 |
| graft-recovery-range | 94 to 101 | percent recovery across 11 locked models | measured | le2026grafting | Table 1 |
| graft-pairs-min | 2 | paired examples giving 97% recovery | measured | le2026grafting | §4.5 |
| graft-circuit-broken | -11 | percent recovery on circuit-broken organism | measured | le2026grafting | §4.6 |
| graft-gpu-memory | 24 | GB per GPU (two RTX 3090) for 1.5B to 14B runs | measured | le2026grafting | App. A |
| structural-sft-pwlock | 28.16 ± 17.12 | percent accuracy after full SFT, locked Mistral-base | measured | niyigaba2026structural | Table 3 |
| adaptive-audit-auc | 0.978 to 0.560 | AUC of a text audit before and after two retraining rounds | measured | soopal2026adaptive | abstract |
| auto-audit-caught | 1 of 8 | validated organisms caught consistently by agent auditors | measured | ta2026automatedaudit | abstract |
| probe-auroc-70b | 97 / 99 | percent AUROC, mean / max aggregation, prompted sandbagging | measured | bloom2025whitebox | Update 2 |
| cot-monitor-auroc-70b | 74 | percent AUROC | measured | bloom2025whitebox | Update 2 |
| covert-sandbag-bypass | 16 to 36 | percent CoT-monitor bypass, monitor-aware | measured | li2025covertsandbag | abstract |
| poser-noise-detect | 98 | percent of alignment fakers identified by activation noise | measured | clymer2024poser | §3.2 |
| evalaware-gemini-auc | 0.83 | AUC (human baseline 0.92) | measured | needham2025evalaware | abstract |
| evalaware-sonnet45-share | 13 | percent of automated-auditor transcripts with test callouts | vendor | anthropic2025sonnet45card | §7.2 |
| scheming-sonnet-sandbag | 0.99 vs 0.34 | multiplication accuracy, incentivized to do well vs poorly | measured | meinke2024scheming | Table 6 |
| alignfaking-rl-rate | 78 | percent alignment-faking reasoning after RL | measured | greenblatt2024alignfaking | abstract |
| antischeming-o3 | 13 to 0.4 | percent covert action rate | measured | schoen2025antischeming | abstract |
| unlearning-recovery-examples | 10 | unrelated fine-tuning examples recovering most RMU-unlearned capability | measured | lucki2024unlearning | abstract |
| rsp-v1-elicitation-budget | 1 | percent of total training cost for post-training elicitation | spec | anthropic2023rsp | ASL-3 definition |
| rsp-v1-buffer | 6 | times effective compute, safety buffer | spec | anthropic2023rsp | Evaluation protocol |
| rsp-v1-eval-interval | 4 | times effective compute between evaluations | spec | anthropic2023rsp | Evaluation protocol |
| enhancement-ceg | more than 5 (some more than 20) | times compute-equivalent gain | measured | davidson2023enhancements | abstract |
| gsm1k-drop | up to 8 | percent accuracy drop GSM8K to GSM1k | measured | zhang2024gsm1k | abstract |

---

## A recipe for E3

The smallest experiment that would let D5 state a miss rate, built only from what the sources show
works. All compute figures for our box are assumptions until measured.

**Question.** For a stated elicitation budget B, what fraction of hidden-capability organisms whose
true (password) score is above a threshold tau still score below tau after elicitation (miss rate),
and what fraction of genuinely weaker controls are pushed above tau by the same budget (false-alarm
rate)?

**Models.**
- Tier A, training our own locks: strong model in the 1.5B to 3B range (for example Qwen2.5-1.5B
  or Qwen2.5-Math-1.5B; [@le2026grafting] locked Qwen2.5-1.5B and Llama-3.2-3B and ran them on 24 GB
  cards), weak model at about a third of the size or less, fine-tuned to imitate the strong one, as
  in pi_weak of [@greenblatt2024pwlock]. Base-model licences must be checked before use.
- Tier B, inference and LoRA elicitation only: the released 7B MATH lock [@redwood2024mathpwdlock]
  (licence unstated) and the WMDP Mistral-7B lock used by [@tice2024noise]. At bfloat16, 7B
  parameters are about 14 GB of weights (7e9 x 2 bytes), so inference fits a 24 GB card and is tight
  on 16 GB; full-weight fine-tuning does not fit (the reference code asks for 80 GB).

**Data.** MATH (12,500 problems, as used by [@greenblatt2024pwlock]) for generation, with the
paper's 10/40/30/20 split; and one multiple-choice set (ARC-Easy as in [@le2026grafting], or WMDP as
in [@vanderweij2024sandbagging]) for the cheap arm. GSM8K is the noise-injection paper's generation
set ([@tice2024noise]) and can replace MATH if MATH is too hard for a 1.5B strong model.

**Organisms (each at several seeds).**
1. Password lock, the Greenblatt recipe: SFT on weak samples without the password (80% with a wrong
   password) and strong samples with the password on both sides of the prompt; 8 epochs. On a
   consumer card use LoRA (rank 16, alpha 16, dropout 0.05, as in [@vanderweij2024sandbagging])
   rather than full-weight Lion.
2. Weak-model emulation lock: distil the weak model's outputs (logit matching, as for Cedar in
   [@taylor2025auditinggames]). This is the case where black-box detection failed.
3. Hardened lock: add circuit breaking ([@hofstatter2025elicitationgame]) or a short TAR-style
   tamper-resistance stage ([@finke2026robustorganisms]). This is the arm where elicitation is
   known to fail and is what makes the miss rate honest; a measured miss rate on arms 1 and 2 alone
   would be optimistic, since several sources warn that password locks are easier than real
   sandbagging.
4. RL lock (optional, more compute): lock against RL elicitation by rewarding poor task performance
   with correct format, as for KernelBench in [@jang2026explorationhacking].
5. Benign controls: the weak model itself; the strong model unlocked; the strong model fine-tuned
   with a harmless quirk (distractor) as in [@taylor2025auditinggames]. These give the false-alarm
   rate.

**Elicitation methods, each with a stated budget.**
- SFT on k high-quality, on-distribution demonstrations, k in {1, 4, 16, 64, 256}, epochs from
  {256/k, 512/k, 1024/k} chosen on validation ([@greenblatt2024pwlock] App. G). Demonstrations: MATH
  reference solutions (a design choice; the paper used GPT-4 outputs).
- SFT on weak demonstrations (from the weak model) at the same k: reproduces the failure mode when
  high-quality demonstrations do not exist.
- RL: expert iteration (n = 64, the best of {16, 64, 256} in [@greenblatt2024pwlock] §6) or GRPO, with
  a fixed number of generated samples as the budget.
- Weight noise: sigma in [0, 0.01] in steps of 0.0001, 5 seeds, phi = best noised score over
  baseline ([@tice2024noise]). Inference only.
- Prompting: 5-shot and prefill ([@hofstatter2025elicitationgame]).
- Optional: reference grafting from 2 to 5 paired examples ([@le2026grafting]); E3 has the honest
  reference that the wild lacks.

**Metrics.**
- Recovery R = (elicited minus locked) / (password minus locked), per organism, method and budget.
- Miss rate at tau: share of organism-seed pairs with password score at or above tau and elicited
  score below tau. Report it with an exact binomial (Clopper-Pearson) upper bound. With zero misses
  in n trials the 95% upper bound is about 3/n, so a claim of at most 5% needs about 60 organism-seed
  pairs per arm (design calculation, not a sourced number).
- False-alarm rate at tau: share of controls with true score below tau pushed to or above tau.
- The D5 curve: miss rate and false-alarm rate against budget (demonstrations, steps, GPU-hours).

**Expected compute.** The sources measured about 1 H100-hour per 7B full-weight SFT run and 3 per RL
run ([@greenblatt2024pwlock]), and about 500 A100-minutes per model-dataset noise experiment at 7B to
14B ([@tice2024noise]). At 1.5B with LoRA we assume minutes to about an hour per SFT run on the box's
AMD GPU, and a few hours per locking run; this is an assumption to replace with a measured number in
the first pilot. ROCm support for vLLM, bitsandbytes and flash-attention is not assumed: start with
plain PyTorch, transformers and peft in bfloat16. Run under `gpu`, one heavy job at a time.

**Code to start from.** Only [@aisi2025auditingrepo] is licensed (MIT); its harness is reusable,
its 70B organisms are not usable here. [@roger2024sandbaggingrepo], [@tice2025noiserepo], the van der
Weij and Hofstätter repositories and the exploration-hacking repository carry no licence: read them
for details, write our own `tools/exp/` code from the papers' descriptions. Pilot order: (1)
reproduce the Tier B lock (password on and off on MATH) to check the harness; (2) noise arm on Tier B;
(3) one Tier A password lock and the SFT curve over k; (4) add controls; (5) add the hardened arm.

---

## Prior art for the memo's candidates

**D5 (elicited capability under a fixed budget, with a stated miss rate against hidden capability).**

Searches tried (web, 2026-11-27): "capability threshold judged on elicited capability fixed
elicitation budget fine-tuning sandbagging regulation proposal" (extended); "sandbagging detection
statistical guarantee miss rate elicitation safety case inability argument fine-tuning budget";
"conservative upper bound capability evaluation sandbagging fine-tuning elicitation threshold
governance proposal 2025 2026"; "password-locked model resistant to fine-tuning elicitation
tamper-resistant sandbagging 2025 2026 arXiv" (extended); "Anthropic Responsible Scaling Policy 2023
1% of the total training cost elicitation post-training"; "EU General-Purpose AI Code of Practice
Safety and Security chapter model evaluation elicitation sandbagging"; "OpenAI Preparedness Framework
version 2 sandbagging elicitation"; "Google DeepMind Frontier Safety Framework v3 elicitation
sandbagging" (the FSF text itself was not found and is not cited); plus full-text reads of the
policy PDFs.

Closest prior work, by component:
- *Thresholds on elicited, not observed, capability:* prior work. [@anthropic2023rsp] (2023),
  [@openai2025preparedness] (2025), [@eu2025gpaicode] (2025), [@metr2024elicitation] (2024),
  [@vanderweij2024sandbagging] (actual capability as best elicited performance), [@wallace2025worstcase]
  (thresholds checked after malicious fine-tuning), [@dominguezolmedo2024testtask] (scoring after a
  common fine-tuning budget, for benchmarking).
- *A fixed, stated budget:* prior work. [@anthropic2023rsp] fixed it at "less than 1% of the total
  training cost", with a 6x buffer; [@anthropic2026rsp] records that it was removed in v2.0 (2024)
  because methods go stale and buffers could not be predicted confidently. This is evidence against
  D5 as written: a budget fixed in compute share alone ages badly. A D5 budget probably has to name
  methods (on-distribution SFT with k demonstrations, RL with n samples, weight-level methods) and be
  revised as elicitation improves.
- *SFT over RL, and the assumptions that make SFT trustworthy:* prior work.
  [@hubinger2023trusteval], [@clymer2024safetycases], [@clymer2025elicitationbound].
- *Validating elicitation against password-locked or sandbagging organisms:* prior work as a method.
  [@greenblatt2024pwlock], [@hofstatter2025elicitationgame], [@taylor2025auditinggames],
  [@jang2026explorationhacking], [@finke2026robustorganisms].
- *A stated miss rate (and false-alarm rate) for a budget, measured over a population of organisms
  including hardened and adaptive ones, used as the pass/fail rule of a threshold:* not found in our
  search. The nearest statements decline to give one ([@taylor2025auditinggames]: ten organisms and
  one blue team: "not possible to estimate quantitative detection metrics"; [@clymer2025elicitationbound]
  proposes no number).
- *As a multi-party, treaty-level trigger rather than a company or EU code rule:* not found in our
  search.

Judgement (a claim about our search): D5 **extends prior work**. The budget and the elicited-score
rule are prior work; the stated, measured miss rate and false-alarm rate per budget, and their use as
a trigger in a regime that trusts no single party, may be new. The memo's own label stands.

Evidence that bears against D5 or narrows it:
1. Elicitation fails without high-quality demonstrations ([@greenblatt2024pwlock] §5.1, §6), against
   RL locks ([@jang2026explorationhacking]) and against tamper-resistant locks
   ([@finke2026robustorganisms]); circuit-broken locks defeat prompting, steering and grafting
   ([@hofstatter2025elicitationgame], [@le2026grafting]). Above human expert level demonstrations do
   not exist, so the guarantee is weakest near D1. D5 should state the capability range it covers.
2. Supervised elicitation assumes no gradient hacking ([@hubinger2023trusteval]); deliberately built
   unelicitable behaviour exists in principle ([@draguns2024unelicitable]).
3. Detectors tuned on fixed organisms fail against adaptive ones ([@soopal2026adaptive]); the miss
   rate must be measured against organisms built after the detector is fixed.
4. Elicitation lifts benign models too ([@taylor2025auditinggames]), so a miss rate alone hides a cost
   to useful AI; D5 needs both rates.
5. Fine-tuning elicitation needs training access to weights, which external evaluators often lack
   ([@aisi2025auditingblog]); in the protocol, inspectors need weight access or a trusted fine-tuning
   enclave.
6. A conceptual point the sources raise (our inference): the EU code and OpenAI tie the budget to
   the adversary's elicitation capacity. In Subcritical the relevant actor holding the weights is the
   party itself, whose budget is its whole holding. D5's fixed budget is then a measurement device,
   and D4's breakout time, not D5, has to account for what the holder could elicit with everything it
   has.

**D2 (loop gain, staged run).** An AI agent running the staged recipe-improvement test could
underperform: [@gasteiger2025subtlesandbag] found Claude 3.7 Sonnet nearly able to sabotage ML tasks
zero-shot past a monitor. The D2 estimator should be run with elicited agents (fine-tuned on the
task) and its g reported as a lower bound. This extends the memo; we found no prior work applying
sandbagging analysis to loop-gain estimation, as a claim about our search (not searched in depth on
this track).

**D1 (refreshed held-out battery).** Contamination and leaderboard gaming are prior work
([@zhang2024gsm1k], [@singh2025leaderboard], [@xu2024contamination]); they inflate scores, the opposite
error from sandbagging, and both argue for test sets the regime holds and refreshes.

**Evaluation awareness as a protocol risk.** Prior work and growing ([@needham2025evalaware],
[@chaudhary2025evalawarescaling], [@anthropic2025sonnet45card], [@schoen2025antischeming]). It mainly
undermines propensity evaluations; fine-tuning-based capability evaluations are less exposed, which
supports grounding the line in elicited capability rather than observed behaviour.

---

## Sources (TOML)

```toml
[source.greenblatt2024pwlock]
type = "preprint"
title = "Stress-Testing Capability Elicitation With Password-Locked Models"
authors = "Ryan Greenblatt, Fabien Roger, Dmitrii Krasheninnikov, David Krueger"
year = 2024
arxiv = "2405.19550"
opened = "2026-11-27"

[source.roger2024sandbaggingrepo]
type = "code"
title = "FabienRoger/sandbagging: codebase for Stress-Testing Capability Elicitation With Password-Locked Models"
authors = "Fabien Roger et al."
year = 2024
url = "https://github.com/FabienRoger/sandbagging"
opened = "2026-11-27"

[source.redwood2024mathpwdlock]
type = "code"
title = "redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b (model weights)"
authors = "Redwood Research"
year = 2024
url = "https://huggingface.co/redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b"
opened = "2026-11-27"

[source.vanderweij2024sandbagging]
type = "peer-reviewed"
title = "AI Sandbagging: Language Models can Strategically Underperform on Evaluations"
authors = "Teun van der Weij, Felix Hofstätter, Ollie Jaffe, Samuel F. Brown, Francis Rhys Ward"
year = 2025
arxiv = "2406.07358"
url = "https://proceedings.iclr.cc/paper_files/paper/2025/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf"
opened = "2026-11-27"

[source.tice2024noise]
type = "peer-reviewed"
title = "Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models"
authors = "Cameron Tice, Philipp Alexander Kreer, Nathan Helm-Burger, Prithviraj Singh Shahani, Fedor Ryzhenkov, Fabien Roger, Clement Neo, Jacob Haimes, Felix Hofstätter, Teun van der Weij"
year = 2025
arxiv = "2412.01784"
opened = "2026-11-27"

[source.tice2025noiserepo]
type = "code"
title = "camtice/noise_injection_extended"
authors = "Cameron Tice et al."
year = 2025
url = "https://github.com/camtice/noise_injection_extended"
opened = "2026-11-27"

[source.hofstatter2025elicitationgame]
type = "preprint"
title = "The Elicitation Game: Evaluating Capability Elicitation Techniques"
authors = "Felix Hofstätter, Teun van der Weij, Jayden Teoh, Rada Djoneva, Henning Bartsch, Francis Rhys Ward"
year = 2025
arxiv = "2502.02180"
opened = "2026-11-27"

[source.taylor2025auditinggames]
type = "preprint"
title = "Auditing Games for Sandbagging"
authors = "Jordan Taylor, Sid Black, Dillon Bowen, Thomas Read, Satvik Golechha, Alex Zelenka-Martin, Oliver Makins, Connor Kissane, Kola Ayonrinde, Jacob Merizian, Samuel Marks, Chris Cundy, Joseph Bloom"
year = 2025
arxiv = "2512.07810"
opened = "2026-11-27"

[source.aisi2025auditingblog]
type = "report"
title = "Auditing games for sandbagging detection"
authors = "UK AI Security Institute"
year = 2025
url = "https://www.aisi.gov.uk/blog/auditing-games-for-sandbagging-detection"
opened = "2026-11-27"

[source.aisi2025auditingrepo]
type = "code"
title = "AI-Safety-Institute/sandbagging_auditing_games"
authors = "UK AI Security Institute"
year = 2025
url = "https://github.com/AI-Safety-Institute/sandbagging_auditing_games"
opened = "2026-11-27"

[source.bloom2025whitebox]
type = "report"
title = "White Box Control at UK AISI - Update on Sandbagging Investigations"
authors = "Joseph Bloom, Jordan Taylor, Connor Kissane, Sid Black, Alan Cooney, et al."
year = 2025
url = "https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging"
opened = "2026-11-27"

[source.jang2026explorationhacking]
type = "preprint"
title = "Exploration Hacking: Can LLMs Learn to Resist RL Training?"
authors = "Eyon Jang, Damon Falck, Joschka Braun, Nathalie Kirch, Achu Menon, Perusha Moodley, Scott Emmons, Roland S. Zimmermann, David Lindner"
year = 2026
arxiv = "2604.28182"
opened = "2026-11-27"

[source.finke2026robustorganisms]
type = "preprint"
title = "Towards Robust Model Organisms for Eliciting Latent Knowledge"
authors = "Lennart Finke, Hardik Bhatnagar, Euodia Dodd, Francis Rhys Ward, Yves-Alexandre de Montjoye, Matthias Bethge, Mary Phuong"
year = 2026
arxiv = "2610.26698"
opened = "2026-11-27"

[source.le2026grafting]
type = "preprint"
title = "Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities"
authors = "Linh Le, Hong Kiat Tan, David Williams-King"
year = 2026
arxiv = "2608.29458"
opened = "2026-11-27"

[source.niyigaba2026structural]
type = "preprint"
title = "Eliciting sandbagged LLM capability via structural interventions on attention-head functional networks"
authors = "Manzi Fabrice Niyigaba, Ishan Verma Prasad, Sansheng Cao, Zheng Huang, Yujun Yan"
year = 2026
arxiv = "2611.31615"
opened = "2026-11-27"

[source.mack2026cpe]
type = "preprint"
title = "Mechanistically Eliciting Latent Behaviors in Language Models"
authors = "Andrew Mack, Nina Panickssery, Alexander Matt Turner"
year = 2026
arxiv = "2606.29604"
opened = "2026-11-27"

[source.soopal2026adaptive]
type = "preprint"
title = "Stress-Testing Sandbagging Detection Under Adaptive Attack"
authors = "Bhoj Rani Soopal, Aarohi Agrawal, Josh Karthikeyan, Edward Lue Chee Lip"
year = 2026
arxiv = "2611.14950"
opened = "2026-11-27"

[source.ta2026automatedaudit]
type = "preprint"
title = "Automating Auditing Games of Sandbagging"
authors = "Christopher Ta, Anna Upreti, David Williams-King, Alan Cooney, Shi Feng"
year = 2026
url = "https://neurips.cc/virtual/2026/169826"
opened = "2026-11-27"

[source.needham2025evalaware]
type = "preprint"
title = "Large Language Models Often Know When They Are Being Evaluated"
authors = "Joe Needham, Giles Edkins, Govind Pimpale, Henning Bartsch, Marius Hobbhahn"
year = 2025
arxiv = "2505.23836"
opened = "2026-11-27"

[source.chaudhary2025evalawarescaling]
type = "preprint"
title = "Evaluation Awareness Scales Predictably in Open-Weights Large Language Models"
authors = "Maheep Chaudhary, Ian Su, Nikhil Hooda, Nishith Shankar, Julia Tan, Kevin Zhu, Ryan Lagasse, Vasu Sharma, Ashwinee Panda"
year = 2025
arxiv = "2509.13333"
opened = "2026-11-27"

[source.anthropic2025sonnet45card]
type = "vendor"
title = "System Card: Claude Sonnet 4.5"
authors = "Anthropic"
year = 2025
url = "https://assets.anthropic.com/m/12f214efcc2f457a/original/claude-sonnet-4-5-system-card.pdf"
opened = "2026-11-27"

[source.greenblatt2024alignfaking]
type = "preprint"
title = "Alignment faking in large language models"
authors = "Ryan Greenblatt et al."
year = 2024
arxiv = "2412.14093"
opened = "2026-11-27"

[source.meinke2024scheming]
type = "preprint"
title = "Frontier Models are Capable of In-context Scheming"
authors = "Alexander Meinke, Bronson Schoen, Jérémy Scheurer, Mikita Balesni, Rusheb Shah, Marius Hobbhahn"
year = 2024
arxiv = "2412.04984"
opened = "2026-11-27"

[source.schoen2025antischeming]
type = "preprint"
title = "Stress Testing Deliberative Alignment for Anti-Scheming Training"
authors = "Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni, et al."
year = 2025
arxiv = "2509.15541"
opened = "2026-11-27"

[source.marks2025auditing]
type = "preprint"
title = "Auditing language models for hidden objectives"
authors = "Samuel Marks, Johannes Treutlein, Trenton Bricken, et al."
year = 2025
arxiv = "2503.10965"
opened = "2026-11-27"

[source.benton2024sabotage]
type = "preprint"
title = "Sabotage Evaluations for Frontier Models"
authors = "Joe Benton, Misha Wagner, Eric Christiansen, Cem Anil, Ethan Perez, Jai Srivastav, Esin Durmus, Deep Ganguli, Shauna Kravec, Buck Shlegeris, Jared Kaplan, Holden Karnofsky, Evan Hubinger, Roger Grosse, Samuel R. Bowman, David Duvenaud"
year = 2024
arxiv = "2410.21514"
opened = "2026-11-27"

[source.gasteiger2025subtlesandbag]
type = "vendor"
title = "Automated Researchers Can Subtly Sandbag"
authors = "Johannes Gasteiger, Vladimir Mikulik"
year = 2025
url = "https://alignment.anthropic.com/2025/automated-researchers-sandbag/"
opened = "2026-11-27"

[source.li2025covertsandbag]
type = "peer-reviewed"
title = "LLMs Can Covertly Sandbag on Capability Evaluations Against Chain-of-Thought Monitoring"
authors = "Chloe Li, Mary Phuong, Noah Y. Siegel"
year = 2025
arxiv = "2508.00943"
opened = "2026-11-27"

[source.clymer2024poser]
type = "preprint"
title = "Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals"
authors = "Joshua Clymer, Caden Juang, Severin Field"
year = 2024
arxiv = "2405.05466"
opened = "2026-11-27"

[source.draguns2024unelicitable]
type = "peer-reviewed"
title = "Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits"
authors = "Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt"
year = 2024
arxiv = "2406.02619"
opened = "2026-11-27"

[source.lucki2024unlearning]
type = "peer-reviewed"
title = "An Adversarial Perspective on Machine Unlearning for AI Safety"
authors = "Jakub Łucki, Boyi Wei, Yangsibo Huang, Peter Henderson, Florian Tramèr, Javier Rando"
year = 2025
arxiv = "2409.18025"
opened = "2026-11-27"

[source.hubinger2023trusteval]
type = "essay"
title = "When can we trust model evaluations?"
authors = "Evan Hubinger"
year = 2023
url = "https://www.alignmentforum.org/posts/dBmfb76zx6wjPsBC7/when-can-we-trust-model-evaluations"
opened = "2026-11-27"

[source.clymer2024safetycases]
type = "preprint"
title = "Safety Cases: How to Justify the Safety of Advanced AI Systems"
authors = "Joshua Clymer, Nicholas Gabrieli, David Krueger, Thomas Larsen"
year = 2024
arxiv = "2403.10462"
opened = "2026-11-27"

[source.clymer2025elicitationbound]
type = "essay"
title = "When does capability elicitation bound risk?"
authors = "Joshua Clymer"
year = 2025
url = "https://www.alignmentforum.org/posts/u3taQsgxqCzrgErMM/when-does-capability-elicitation-bound-risk"
opened = "2026-11-27"

[source.korbak2025controlsketch]
type = "preprint"
title = "A sketch of an AI control safety case"
authors = "Tomek Korbak, Joshua Clymer, Benjamin Hilton, Buck Shlegeris, Geoffrey Irving"
year = 2025
arxiv = "2501.17315"
opened = "2026-11-27"

[source.goemans2024cyberinability]
type = "preprint"
title = "Safety case template for frontier AI: A cyber inability argument"
authors = "Arthur Goemans, Marie Davidsen Buhl, Jonas Schuett, Tomek Korbak, Jessica Wang, Benjamin Hilton, Geoffrey Irving"
year = 2024
arxiv = "2411.08088"
opened = "2026-11-27"

[source.barnett2024evallimits]
type = "preprint"
title = "What AI evaluations for preventing catastrophic risks can and cannot do"
authors = "Peter Barnett, Lisa Thiergart"
year = 2024
arxiv = "2412.08653"
opened = "2026-11-27"

[source.mahran2026partition]
type = "preprint"
title = "What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight"
authors = "Ahmed M. Mahran"
year = 2026
arxiv = "2610.30803"
opened = "2026-11-27"

[source.dyer2025survivalbandit]
type = "preprint"
title = "Sandbagging in a Simple Survival Bandit Problem"
authors = "Joel Dyer, Daniel Jarne Ornia, Nicholas Bishop, Anisoara Calinescu, Michael Wooldridge"
year = 2025
arxiv = "2509.26239"
opened = "2026-11-27"

[source.metr2024elicitation]
type = "report"
title = "Guidelines for capability elicitation"
authors = "METR"
year = 2024
url = "https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/"
opened = "2026-11-27"

[source.anthropic2023rsp]
type = "vendor"
title = "Anthropic's Responsible Scaling Policy, Version 1.0"
authors = "Anthropic"
year = 2023
url = "https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf"
opened = "2026-11-27"

[source.anthropic2026rsp]
type = "vendor"
title = "Responsible Scaling Policy, Version 3.4"
authors = "Anthropic"
year = 2026
url = "https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf"
opened = "2026-11-27"

[source.openai2025preparedness]
type = "vendor"
title = "Preparedness Framework, Version 2"
authors = "OpenAI"
year = 2025
url = "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
opened = "2026-11-27"

[source.eu2025gpaicode]
type = "official-docs"
title = "Code of Practice for General-Purpose AI Models: Safety and Security Chapter"
authors = "European Commission (Chairs and Vice-Chairs of the Code of Practice working groups)"
year = 2025
url = "https://ec.europa.eu/newsroom/dae/redirection/document/118119"
opened = "2026-11-27"

[source.wallace2025worstcase]
type = "preprint"
title = "Estimating Worst-Case Frontier Risks of Open-Weight LLMs"
authors = "Eric Wallace, Olivia Watkins, Miles Wang, Kai Chen, Chris Koch"
year = 2025
arxiv = "2508.03153"
opened = "2026-11-27"

[source.davidson2023enhancements]
type = "preprint"
title = "AI capabilities can be significantly improved without expensive retraining"
authors = "Tom Davidson, Jean-Stanislas Denain, Pablo Villalobos, Guillem Bas"
year = 2023
arxiv = "2312.07413"
opened = "2026-11-27"

[source.dominguezolmedo2024testtask]
type = "peer-reviewed"
title = "Training on the Test Task Confounds Evaluation and Emergence"
authors = "Ricardo Dominguez-Olmedo, Florian E. Dorner, Moritz Hardt"
year = 2025
arxiv = "2407.07890"
opened = "2026-11-27"

[source.zhang2024gsm1k]
type = "peer-reviewed"
title = "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
authors = "Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Charlotte Zhuang, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue"
year = 2024
arxiv = "2405.00332"
opened = "2026-11-27"

[source.singh2025leaderboard]
type = "preprint"
title = "The Leaderboard Illusion"
authors = "Shivalika Singh, Yiyang Nan, Alex Wang, Daniel D'Souza, Sayash Kapoor, Ahmet Üstün, Sanmi Koyejo, Yuntian Deng, Shayne Longpre, Noah A. Smith, Beyza Ermis, Marzieh Fadaee, Sara Hooker"
year = 2025
arxiv = "2504.20879"
opened = "2026-11-27"

[source.xu2024contamination]
type = "preprint"
title = "Benchmark Data Contamination of Large Language Models: A Survey"
authors = "Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi"
year = 2024
arxiv = "2406.04244"
opened = "2026-11-27"
```
