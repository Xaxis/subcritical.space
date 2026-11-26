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

## A third addition: the anatomy of superintelligence

A large part of the paper, not just a section, must define very specifically what
superintelligence is and by what mechanisms it forms, from every relevant perspective:

- **Physical and energetic:** the compute, energy, memory, bandwidth and hardware it takes;
  thermodynamic and information-theoretic limits (for example Landauer's limit and the energy cost
  per useful operation); and what physical footprint a system approaching it would leave, so it
  can be detected.
- **Computational and algorithmic:** scaling laws, architectures, data, search and planning, and
  how capability compounds.
- **Dynamical:** the feedback loops that turn a capable system into a superintelligent one
  (continual learning, recursive self-improvement, autonomous resource acquisition), with rates,
  thresholds and the conditions for runaway versus saturation.
- **Cognitive and functional:** what it can do that humans and institutions cannot, measured
  rather than asserted.
- **Organizational and economic:** how labs, markets and states supply the inputs that let it form.

Each mechanism needs a precise definition, a way to measure it, and the evidence for or against
it. The protocol in the second half should then follow from these definitions: it limits the
mechanisms that form it. Same verification bar.

## A fourth addition: the site

The project also becomes a website application, and it should be the best one built so far, like
Corerope and Phosphoros (now starwright.space) but better.

- **Name.** Pick the best name with a domain that checks out as likely available, build under it,
  and post it so the owner can register the domain. Until it is registered, deploy to a preview
  address and switch the moment it is live. The GitHub repository has the same name as the site,
  under the owner's personal account, with the same visibility and licence as corerope.space and
  phosphoros.space unless something here should not be public yet.
- **What it does.** It presents the research as a living, interactive work, not a static paper:
  the definitions and mechanisms of superintelligence explorable from each perspective (physical,
  energetic, computational, dynamical, cognitive, organisational), the protocol laid out clearly,
  and the experiments and simulations rerunnable or explorable in the browser, all with sources.
- **Design.** Extremely elegant and meaningful, with heavy use of 3D, as on the owner's other
  sites (Phosphoros and Starwright's 3D views, and the owner's other renderer; reuse what fits).
  The 3D carries meaning, not decoration: the mechanisms of superintelligence forming as
  explorable systems, the feedback loops and thresholds as dynamic models, energy and compute
  scales you can move through, the protocol's verification layers as structures you can inspect.
  Fast on phones, with graceful fallbacks when WebGL is unavailable or the reader prefers reduced
  motion. Every 3D view checked in a real browser, including against the black-screen failure
  Phosphoros's Explore view once had.
- **Quality bar.** A polished, cohesive, very adaptive UI across phone, tablet and desktop, in both
  themes, accessible, fast, and not generic in look or writing. Checked in a real browser at
  several widths before anything is called done.
- **Order.** The research and definitions come first, since the site presents them. Build the site
  alongside once the memo and the definitions settle, deploy it the way the other project sites
  deploy, and post the live link.
- **Setup.** The owner's usual setup, as on the other project sites: the shared projects and the
  typical stack, the owner's personal accounts (not any employer's), and environment variables or
  keys taken from the other projects' existing config. Follow how corerope.space and
  phosphoros.space are built and deployed. No new accounts or paid services without asking.
