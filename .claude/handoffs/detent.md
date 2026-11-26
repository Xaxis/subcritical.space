# Where Detent stands, 2026-11-26

Started 2026-11-26 from a session launched in the parent folder, which set up the repository,
wrote the memo and handed off at once. All research happens in a session started in this folder.
The brief is `00-BRIEF.md`: read it first, both parts (the request and the two additions).

## Done

- Scaffold: the ledger, model, docs sync, check and paper build, taken from Escapement (`../escapement`,
  github Xaxis/escapement) and renamed. `make model docs check` passes. Public repo, noreply commits,
  local hooks copied from Escapement.
- `research/00-memo.md`: candidate definitions D1 to D6, the five pathways with a ranking before
  testing, the protocol's shape, what Escapement does and does not contribute. The memo was posted to
  the owner. Every label in it is a belief before the independent search.
- `.mcp.json` registers Paperwright's connector (`https://paperwright.diy/mcp`). On 2026-11-26 the
  endpoint answered 401 with its OAuth challenge, so it is open; it needs the owner to approve the
  project server and sign in through `/mcp` once.

## The plan, in order (time is not a constraint; the bar is the six levels)

1. **Survey tracks**, in parallel helpers, each writing `research/notes/NN-<track>.md` with every
   source's identifier (DOI, arXiv ID, URL) and what it actually says, opened, not remembered:
   1. Definitions and thresholds in force: frontier safety frameworks (Anthropic RSP and its AI R&D
      thresholds, OpenAI Preparedness, Google DeepMind's Frontier Safety Framework), levels of AGI,
      the EU AI Act's systemic-risk compute presumption, compute-threshold papers, the 2025
      superintelligence statements and agreements proposed to prevent it.
   2. The pathways' evidence: automated AI research (returns to software research, intelligence
      explosion models, RE-Bench, MLE-bench, PaperBench, the automated speedrunning benchmark,
      developer uplift trials), continual learning and self-editing models, autonomy (task time
      horizons), self-replication evaluations, scaling laws and algorithmic progress.
   3. Compute governance and hardware: compute as a governance lever, catching large training runs,
      cloud know-your-customer, hardware-enabled mechanisms and flexible guarantees, location
      verification, chip smuggling evidence, decentralised and low-bandwidth training.
   4. Arms control and verification: IAEA safeguards (significant quantity, timeliness, conversion
      time, the Additional Protocol), the CWC's challenge inspections, why the BWC has no
      verification, New START, the CTBT's monitoring system, and the secret programs that were and
      were not caught (Iraq, Biopreparat, the Khan network, Iran, al-Kibar). Proposals for AI
      treaties and their verification.
   5. Mechanism design: inspection games (Dresher, Maschler's inspector leadership, Avenhaus, von
      Stengel and Zamir), coalition-proof equilibria, treaty participation and withdrawal.
   6. Evaluation that can be gamed: sandbagging, password-locked models, noise injection,
      evaluation awareness, alignment faking, exploration hacking, elicitation by fine-tuning.
2. **Pathway ranking with evidence** (`research/01-pathways.md`): for each of the five, necessary,
   sufficient or neither, how measured, what a limit costs useful AI; the ranking decides what the
   protocol restricts. This is central (the owner's second addition).
3. **Definitions tightened** into `research/04-claims.md`, each with its runnable test.
4. **Experiments** in `tools/exp/`, results in `data/results/`, into the ledger:
   E1 compute against capability on public model and benchmark data (how well a FLOP threshold tracks
   capability, how fast algorithmic progress makes a fixed cap leak); E2 autonomy from published
   time-horizon data; E3 hidden capability on small open models (password-locked organisms, elicitation
   by fine-tuning, noise injection), under `gpu` on the AMD card or on CPU; E4 loop gain, historical
   (public speedrun records) and a small staged run at fixed compute; E5 verification, Monte Carlo of
   several detection channels against secret programs of a given size and length, plus tamper tests of
   sealed declarations; E6 defection and coalition games; E7 continual learning's update compute
   against training thresholds.
5. **Formal** (`research/05-formal.md`): the detection bound over breakout time with independent
   channels; when compliance is an equilibrium; the coalition threshold; the failure conditions; the
   lease bound (Escapement's, credited).
6. **The protocol** (`research/02-protocol.md`): who it binds, what it limits, verification,
   defection, the useful-versus-dangerous line. Escapement's leases and seals only where they fit.
7. **Verification** (`research/06-verification.md`): levels 1, 4 and 6 by fresh helpers given the
   claim, not our case for it; 2 and 3 by us; 5 through Paperwright's desks.
8. **The paper in Paperwright**: create it, add sources by identifier, write each section, run its
   checks and desks, resolve them; `make paper --draft` builds the flattened text.

## Needs the owner

- Approve the project MCP server `paperwright` when the session starts, and sign in through `/mcp`.
