# Where Subcritical stands, 2026-11-26

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
- Name: **Subcritical**, domain **subcritical.space**. On 2026-11-26 the registry's RDAP (through
  rdap.org) answered 404 for it and DNS had no NS or SOA record, against controls corerope.space and
  subcritical.org that answered 200 with nameservers. The owner registers it; until then the site
  deploys to a preview address, and switches the moment the domain is live.
- `.mcp.json` registers Paperwright's connector (`https://paperwright.diy/mcp`). The endpoint
  answered 401 with its OAuth challenge, so it is open; the owner approves the project server and
  signs in through `/mcp` once.
- Commits are by the owner's personal address from the second commit on, since the site deploys
  through Vercel (see CLAUDE.md); the hooks enforce it.

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
2. **Part I written** in `research/01-anatomy.md` (and per-perspective files if it grows), with the
   pathway ranking in `research/02-pathways.md`. This is the centre of the work.
3. **Claims** in `research/04-claims.md`, each with its runnable test; novelty in `03-novelty.md`.
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
5. **Formal** (`research/05-formal.md`): the detection bound over breakout time with independent
   channels; when compliance is an equilibrium; the coalition threshold; the runaway condition for
   coupled loops; the failure conditions; the lease bound (Escapement's, credited).
6. **The protocol** (`research/06-protocol.md`), derived from Part I.
7. **Verification** (`research/07-verification.md`): levels 1, 4 and 6 by fresh helpers given the
   claim, not our case for it; 2 and 3 by us; 5 through Paperwright's desks.
8. **The paper in Paperwright**: create it, add sources by identifier, write each section, run its
   checks and desks, resolve them.
9. **The site**, begun once the memo and definitions settle, built alongside the research. Stack and
   deploy as on corerope.space and phosphoros.space (read their CLAUDE.md, `web/` or `site/`, and
   `tools/site/deploy.sh`); the Vercel token and other keys come from those projects' `.env`; no new
   accounts or paid services without asking. 3D that carries meaning (mechanisms as explorable
   systems, loops and thresholds as live models, energy and compute scales to move through, the
   verification layers as structures to inspect), reusing what fits from Starwright's 3D and the
   owner's other renderer; fast on phones; fallbacks without WebGL and under reduced motion; every
   3D view checked in a real browser at several widths and in both themes, including against the
   black full-screen failure Starwright fixed. Deploy to a preview address and post the link; switch
   to subcritical.space when registered.

## Needs the owner

- Register subcritical.space.
- Approve the project MCP server `paperwright` when the session starts, and sign in through `/mcp`.
