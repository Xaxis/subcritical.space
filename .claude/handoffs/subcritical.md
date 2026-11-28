# Where Subcritical stands, 2026-11-27

Started 2026-11-26 as "Detent" from a session launched in the parent folder, which set up the
repository, wrote the memo, renamed everything to Subcritical (repo `Xaxis/subcritical.space`,
folder `subcritical.space`) and handed off. All work happens in a session started in this folder.
The brief is `00-BRIEF.md`: read all of it first (the request and its four additions). Private
pointers (the owner's other projects, local paths) are in `subcritical.private.md` beside this
file, which git ignores.

## Done

- Scaffold: the ledger, model, docs sync, check and paper build, taken from Escapement (github
  Xaxis/escapement) and renamed. `make model docs check` passes. Public repo, MIT for code and CC BY
  4.0 for content, as on phosphoros.space (corerope.space uses Apache-2.0 for its code).
- `research/00-memo.md`: the anatomy of superintelligence from five perspectives (P1 to P4, A1 to
  A5, Y1 to Y3, F1 to F3, O1 to O3), candidate definitions D1 to D6, the five pathways with a ranking
  before testing, the protocol's shape, and what Escapement does and does not contribute. Posted to
  the owner. Every label in it is a belief before the independent search.
- Name: **Subcritical**, domain **subcritical.space**, registered by the owner on 2026-11-27 and
  live the same day (commit 4bb76d4): the apex serves the site, www and plain HTTP 308 to it. The
  Vercel dashboard had attached the apex as a redirect to www (its default); the deploy now sets
  both domains' direction on every run. https://subcritical.vercel.app still answers.
- `.mcp.json` registers Paperwright's connector (`https://paperwright.diy/mcp`). The endpoint
  answered 401 with its OAuth challenge, so it is open; the owner approves the project server and
  signs in through `/mcp` once.
- Commits are by the owner's personal address from the second commit on, since the site deploys
  through Vercel (see CLAUDE.md); the hooks enforce it.
- Survey (2026-11-27): ten tracks in `research/notes/01` to `10`, every source opened; an
  independent spot-check (`research/notes/11-spot-check.md`) confirmed 50 of 53 risky claims and
  corrected the 3 distorted ones. Sources merged into `research/sources.toml`, one entry per work
  (other keys as `aliases`; `tools/sources_from_notes.py` folds them, `make check` fails on a second
  entry or an alias citation).
- Part I (2026-11-27): `research/01-anatomy.md` (D1 to D6 after the survey) and one chapter per
  perspective, `research/011-physical.md` to `015-organisational.md`, each with its own inputs file
  `data/inputs/01N-*.toml` and model module `model/parts/01N_*.py`. `research/03-novelty.md`: of 40
  ideas none keeps "new", 14 extend prior work, 26 are prior work; what may remain ours is narrow
  (the D2 estimator, D5's measured miss and false-alarm rates, D3 with loop gain, the narrowed D4,
  the evader-minimised multi-channel miss, the coalition share from T_r, block-height licences).
- `research/02-pathways.md` closes Part I: seven pathways (two added: undeclared compute, tied
  first with recursive self-improvement, and distillation), the memo's five re-ranked.
- `research/04-claims.md`: 12 claims (C1 to C12), each with its plan for the six levels and a
  "Results so far" line per level; the one numbered list of experiments (E1 to E25, in build order).
  After levels 1 to 4 and three waves of experiments (2026-11-27): no claim is new or has passed
  all six levels. Candidates: C5 (non-adaptive hiding only, untested at L3) and C8 ((b) cut; L3
  rests on E8 alone). Downgraded: C2 (an accounting frame: E18 cut against (c), (b) not shown), C4
  (a measurement design: E4's interval under-covers and its trigger fails at calibrated noise), C10
  (a definition; E21: t* saturates with its battery, so (c) holds only while baselines last), C11
  (framing). Applications of prior work, credited: C1, C3, C6, C7, C9, C12. Cut parts: C1(c),
  C2(a), C2(c), C4(c), C8(b).
- `research/05-formal.md` (Part III, 1): level 2. Theorems and proofs per claim, each numerical
  statement checked by `tools/formal/<claim>.py` (`run_all.py` under heavy, about 6 minutes). It
  found C4's trigger on g, C7(b) and C9's P2 false as stated, then fixed every red-team attack on
  the proofs: the per-path line for adaptive evaders (Props 1.7, 1.8), per-attempt guarantees
  (1.9), in-run drift (Cor 1.6a: a launch-speed line must rise by 3.2, or 10.6 at high drift),
  repeated play (after Thm 7.2), the FP8 floor bound, rule W for the licence clock, signed couplings
  through K+.
- `research/06-protocol.md` (Part II): one limit per pathway (L1 to L6), the line per path,
  registration at birth for chips. After the red team: licences lapse unless renewed (positive
  evidence plus k signatures from rival blocs; the cost is hold-up); "verification without a
  trusted party" replaced by a table of the eight parties it trusts; no rate floor (E25), a
  powered-time budget plus height expiry on the most-work chain; the loop-gain trigger replaced by
  a ban on closed loops at frontier scale until E4(b); the coupled-gain certificate by rho(U) only
  (E11); no safety from disclosure (E6). Nothing in it closes the untraced pool: until it closes no
  party meets the line.
- Experiments: `tools/exp/` contract and `lib.py`; results enter the ledger with basis
  `experiment`; a case table's new sources sit in `tools/exp/data/<name>.sources.toml`. Done, each
  rerun by the lead and byte-identical: E1 (the frontier's algorithmic rate and compute share are
  not identified from public data), E2, E4 (the loop-gain estimator fails at calibrated noise), E5
  (declared path 39 days; covert paths decades, lower bounds; cloud and distillation unwatched), E6
  (published games reproduced except Emery-Xu's Prop 2, pending an independent check;
  compliance-only disclosure cut; in-run drift beats the margin-2 line), E8 (the floor at FP8), E9
  (compute's share of research input not identified; Part I's loop gains omit compute's growth),
  E11 (the coupled certificate cannot issue today), E24 (25% of in-treaty findings never halted),
  E25 (Bitcoin's real headers: the rate floor is dominated), E18 (the cap leaks in jumps, not at a
  constant rate), E21 (t* rises but saturates with each battery; no battery has an organisation),
  E22 (the supply envelope holds 19 of 19; it bounds phi, so the declared margin covers estimation
  error only and a path must show 4.2 years at each renewal), E23 (the chokepoint durability
  ranking is not supported and no test on public data can decide it). `lib` refuses infinities
  and unsortable details at the line that adds them, and `make check` fails when a result is not
  strict JSON or ran on ledger inputs that have since changed. The venv is built with `uv`.
- Verification: levels 1 (prior art, two helpers) and 4 (red team) ran, writing
  `research/verification/` (kept as written; the site shows their numbers as written and titles
  each with the ledger's current value). Every attack went to the owner of the work it hit; the
  record of each claim at each level and each attack's resolution is `research/07-verification.md`,
  which the home page shows as a grid. Open: C3.8, C4.9, C9.4, C10.4; Emery-Xu's Prop 2 and one E9
  reproduction need an independent check. Level 5 needs Paperwright (see below); level 6 is next.
- The paper: all three parts and a conclusion in `paper/` (about 27,000 words, Part I about half),
  written from the research files and resynced after each wave; `make paper` flattens it.
- Findings that change the design: power is not a chokepoint; chokepoints leak at the edges and
  their holders reverse themselves; the historical discovery rate of covert programmes is about 15
  times below the memo's placeholder; channel miss rates cannot be multiplied (the evader picks the
  path); the IAEA margin is about 1 and times detection only; a disputed breakout threshold
  collapses cooperation, so T_b needs agreed tables.
- Site live at https://subcritical.space: the memo as structure, four figures (loop gain, the
  line, the detection bound with the historical record, coupled loops in 3D), Part I and the notes
  rendered, the ledger and the source list. Proven by `tools/site/deploy.sh --check` (shots at two
  widths and both themes with axe, and `tools/site/interact.ts`). Port 4527 may be taken by another
  local server; serve on any free port.

## The paper's shape (the owner's third addition makes Part I about half)

- **Part I. What superintelligence is and how it forms.** Definitions, then one chapter for each
  perspective: physical and energetic, computational and algorithmic, dynamical, cognitive and
  functional, organisational and economic. Each mechanism: a precise definition, a measurement, the
  evidence for and against. Ends with the five pathways ranked (necessary, sufficient or neither;
  how measured; the cost of limiting it to useful AI).
- **Part II. The protocol, derived.** The line (D4) and its triggers; a limit for each mechanism,
  with the channel that verifies it and its cost to useful AI; verification without a trusted
  party; defection, coalitions and secret programs; where it fails.
- **Part III. Proofs, experiments, verification results, limitations.**

## The plan, in order (time is not a constraint; the bar is the six levels)

1. **Survey tracks**, in parallel helpers, each writing `research/notes/NN-<track>.md` with every
   source's identifier and what the source actually says, opened, not remembered:
   1. Definitions and thresholds in force: frontier safety frameworks and their AI R&D thresholds,
      levels of AGI, the EU AI Act's compute presumption, compute-threshold papers, the 2025
      superintelligence statements and proposed agreements to prevent it.
   2. Physics of computation: Landauer and reversible computing, energy per operation of
      accelerators over time, memory and interconnect bandwidth limits, estimates of the brain's
      compute, data-centre power and its growth, the observable signatures of large facilities.
   3. Algorithms: scaling laws, observational scaling, emergence, algorithmic progress, the
      exchange between training and inference compute, data limits and synthetic data, self-play
      and search.
   4. Dynamics: returns to research (research productivity across fields, returns in software),
      intelligence-explosion and takeoff models, automated AI research evidence and benchmarks,
      continual learning and self-editing models, task time horizons, self-replication evaluations.
   5. Cognition and function: benchmarks with expert or institutional baselines, typologies of
      superintelligence, narrow superhuman systems, measures of economically valuable work.
   6. Economics and organisation: the chip supply chain and its chokepoints, capital spending,
      power supply, talent, race models, export controls.
   7. Compute governance and hardware: catching large training runs, cloud know-your-customer,
      hardware-enabled mechanisms and flexible guarantees, location verification, chip smuggling,
      decentralised training.
   8. Arms control and verification: IAEA safeguards (significant quantity, timeliness, conversion
      time, the Additional Protocol), the CWC's challenge inspections, the BWC's lack of
      verification, New START, the CTBT's monitoring, secret programs caught and missed, proposals
      for AI treaties and their verification.
   9. Mechanism design: inspection games, inspector leadership, coalition-proof equilibria, treaty
      participation and withdrawal.
   10. Evaluations that can be gamed: sandbagging, password-locked models, noise injection,
       evaluation awareness, alignment faking, exploration hacking, elicitation by fine-tuning.
2. **Part I written** (done 2026-11-27, with the pathway ranking; now to verify) in
   `research/01-anatomy.md` and its five chapters, with the pathway ranking in
   `research/02-pathways.md`. This is the centre of the work.
3. **Claims** in `research/04-claims.md` (written), each with its runnable test; novelty in
   `03-novelty.md`.
4. **Experiments** in `tools/exp/`, results in `data/results/`, into the ledger. E1 compute against
   capability on public data, and how fast a fixed cap leaks; E2 autonomy from published time
   horizons; E3 hidden capability on small open models (password-locked organisms, elicitation,
   noise injection), under `gpu` on the AMD card or on CPU; E4 loop gain, historical and a small
   staged run; E5 verification, Monte Carlo of several channels against secret programs, and
   tamper tests of sealed declarations; E6 defection and coalition games; E7 continual learning's
   update compute against thresholds; E8 the footprint floor by year against detection limits,
   and the headroom to Landauer; E9 returns to research fitted for runaway versus saturation; E10
   the training-to-inference exchange rate; E11 the coupled loops simulated with measured
   parameters. Each experiment the site can rerun is written so its core runs in the browser too.
   The claims file's list (E1 to E25) supersedes this one; /experiments on the site shows it.
5. **Formal** (`research/05-formal.md`, written): the detection bound over breakout time with independent
   channels; when compliance is an equilibrium; the coalition threshold; the runaway condition for
   coupled loops; the failure conditions; the lease bound (Escapement's, credited).
6. **The protocol** (`research/06-protocol.md`, written), derived from Part I.
7. **Verification** (`research/07-verification.md`, written and current through level 4): levels
   1, 4 and 6 by fresh helpers given the claim, not our case for it; 2 and 3 by us; 5 through
   Paperwright's desks. Next: level 6 (a fresh reviewer given only the paper and the claims), the
   open attacks (C3.8, C4.9, C9.4, C10.4), an independent check of Emery-Xu's Prop 2 and of E9's one
   non-reproduction, a test of whether the untraced pool can be closed (nothing tests it), and the
   experiments still unrun (phase 2 on the GPU: E3, E12 and on; E4(b), E4(d), E4(e), E10, E15).
   A claim that fails a level is cut or downgraded.
8. **The paper in Paperwright**: `paper/` holds all three parts; `make paper` builds the flat copy.
   Next: create it in Paperwright, add sources by identifier, run its checks and desks, resolve them.
9. **The site**, begun once the memo and definitions settle, built alongside the research. Stack and
   deploy as on corerope.space and phosphoros.space (read their CLAUDE.md, `web/` or `site/`, and
   `tools/site/deploy.sh`); the Vercel token and other keys come from those projects' `.env`; no new
   accounts or paid services without asking. 3D that carries meaning (mechanisms as explorable
   systems, loops and thresholds as live models, energy and compute scales to move through, the
   verification layers as structures to inspect), reusing what fits from Starwright's 3D and the
   owner's other renderer; fast on phones; fallbacks without WebGL and under reduced motion; every
   3D view checked in a real browser at several widths and in both themes, including against the
   black full-screen failure Starwright fixed. Deployed at subcritical.space (registered 2026-11-27).

## Needs the owner

- Approve the project MCP server `paperwright` when the session starts, and sign in through `/mcp`.
