# The brief

The owner's request of 2026-11-26, kept so every session starts from the same ask. Local paths
are replaced by repository names; the wording is otherwise the owner's.

## The request

Start a third new research project: the outline of a protocol for preventing the development of
artificial superintelligence. Extensive, well researched, and built on genuinely novel definitions
backed by proof-based experiments.

1. A project folder with a short name, set up like the Corerope and Phosphoros projects.
2. **Definitions first.** Precise, operational, testable definitions: what counts as
   superintelligence and what counts as approaching it (capability thresholds, self-improvement,
   autonomy, scale), so that a protocol can trigger on something measurable rather than on
   opinion. Each definition must be new, or clearly improve on existing ones, and come with a test
   that can be run.
3. **The protocol.** Who it binds, what it limits (compute, training runs, weights,
   self-modification, deployment), how compliance is verified without trusting any one party, how
   it resists defection and secret development, and how it handles the line between beneficial AI
   and dangerous capability. Look at what the Escapement project is finding on Bitcoin-anchored
   leases and unforgeable records, and use it only where it really fits.
4. **Proof-based experiments.** Formal proofs or derivations of each key property (detection
   guarantees, incentive compatibility, the conditions under which the protocol fails). Run
   experiments and simulations that can be rerun from `tools/`: capability-threshold measurements
   on real models and benchmarks, verification protocols, defection and coalition games.
5. **Research from real sources:** AI governance and compute governance, arms control and
   verification (nuclear, chemical, biological treaties), capability evaluations and scaling laws,
   hardware-enabled mechanisms, mechanism design. Keep a source list.
6. **Verification at several independent levels**, for every claimed contribution: (1) a second
   prior-art search by a helper that did not come up with the idea; (2) formal statement and proof;
   (3) working experiments on real data; (4) a red-team helper that only tries to break it (a
   defecting state, a secret lab, a model that hides its capability, an evaluation that can be
   gamed); (5) Paperwright's integrity, reviewer and editor desks, resolved by us; (6) a
   fresh-eyes reviewer who has not seen the work. Anything that fails a level gets cut or
   downgraded. Never overclaim. Label each contribution new, extends prior work, or prior work.
7. **Write it as an extensive research paper in Paperwright** through its MCP tools (create the
   paper, add sources by identifier, write each section, run its checks and reviews, resolve them).
   If Paperwright cannot be reached, say so at once and keep going.

Post a short memo first (the candidate definitions and protocol shape, and which look strongest),
then keep going unless redirected. Report the paper's title, its core contributions with their
verification results, and anything that needs the owner.

## Two additions, central to the paper

1. **Prevent superintelligence, keep useful AI.** The aim is not to stop AI. Highly useful systems
   should stay allowed and keep improving. The protocol must draw the line precisely between those
   and the path to weapons-grade superintelligence.
2. **Work out which systems cross that line**, with evidence: which capabilities or architectures
   actually lead there. Candidates to test, not conclusions: continual learning (models that keep
   updating their own weights after deployment), recursive self-improvement (AI doing the research
   that makes the next AI), autonomous long-horizon agency, self-replication or acquiring
   resources, and unbounded scaling. For each one, say whether it is necessary, sufficient or
   neither for superintelligence, how it can be measured, and what a limit on it would cost in
   useful AI. Rank them. That ranking decides what the protocol restricts.

Time is not a constraint: take several days if that is what it takes to get it right. Same
verification bar as before.
