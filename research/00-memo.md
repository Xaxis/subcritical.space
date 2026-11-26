# Memo: candidate definitions and the protocol's shape

Written 2026-11-26, before the survey. Everything here is a candidate to be tested, not a
finding. The labels (new, extends prior work, prior work) are the author's belief before the
independent prior-art search, and will change where that search says so. Each candidate that
survives goes into `04-claims.md` and through all six levels in `06-verification.md`.

## The organising idea

Nuclear safeguards do not ban fission. They separate low-enriched uranium, which runs power
reactors, from weapons-grade material, and they set their detection timeliness shorter than the
time it would take to turn diverted material into a weapon. Detent tries the same for AI. Useful
AI stays allowed and keeps improving. The protocol triggers on a measurable line: the point at
which a system, together with what it can reach, could become superintelligent faster than the
regime can detect and respond. The line is drawn by time and by whether the improvement loop is
closed, not by one capability score.

## Candidate definitions

**D1. Superintelligence, the endpoint.** A system S deployed with resources R is
superintelligent at level alpha if, on a refreshed, held-out battery spanning N domain clusters
(AI research, cyber operations, the sciences, strategy, persuasion), S with R beats the best
available human organisation given the same wall-clock time and budget, in at least a fraction
alpha of the clusters. It differs from "greatly exceeds humans in virtually all domains" and from
percentile levels of AGI by comparing against organisations rather than individuals, by counting
copies and speed, and by matching time and cost. Test: a scaled-down battery on benchmarks that
publish expert or team baselines. Belief: extends prior work. Weak as a trigger, because it can
only be measured once it is nearly too late; it serves as the definition the others protect.

**D2. Loop gain, the approach through self-improvement.** With the human-controlled inputs
(compute, data) held fixed and the AI doing the research, g is the ratio of the capability gained
in round n+1 to the capability gained in round n. g at or above 1 is the compounding condition.
Test: (a) historical, from the public record of human-driven algorithmic progress (training
speedrun records, published efficiency estimates); (b) a staged run in which an agent improves a
small model's training recipe over rounds at fixed compute, with a confidence bound on g. Belief:
the condition is prior work (returns to software research above 1); a runnable estimator with a
confidence-bound trigger may be new.

**D3. Breakout time.** T_b is the shortest time, under the best self-directed effort, from a
party's verified holdings (chips, weights, data, research labour human and AI) to a D1 system.
It is computed from effective compute (physical compute times algorithmic efficiency, whose growth
rate is measured) and from D2's loop gain. Belief: the arms-control concept (breakout, conversion
time) is prior work; an AI version computed from measured inputs may extend it.

**D4. Weapons-grade, the line.** A system or holding is weapons-grade when T_b < m * T_r, where
T_r is the protocol's guaranteed time to detect and respond and m is a safety margin. Everything
with a longer breakout time is useful AI and may keep improving, provided each increment still
passes through metered, human-held gates. This is the line between useful AI and the path to
superintelligence, and it ties the definition to the protocol's own detection guarantee. Belief:
new as a regulatory trigger, pending the search.

**D5. Elicited capability, robust to hiding.** Thresholds are judged on the capability a fixed
elicitation budget recovers (fine-tuning steps and examples, scaffolding, best of k), not on
observed scores. The guarantee to test: a model trained to sandbag, or locked behind a password,
is caught when its elicited score crosses the threshold, with a stated miss rate. Test: small open
models with password-locked model organisms. Belief: extends prior work.

**D6. Closure.** For each input to the next model (compute, weights, data, research labour,
money), whether the system can get it without passing a human-held gate that can be verified. A
closed loop in any input shortens T_b. Belief: the framing may be new; it may also turn out to be
framing rather than substance.

## The five candidate pathways, ranked before testing

| Pathway | Necessary? | Sufficient? | How measured | Cost of a limit to useful AI | Prior rank |
|---|---|---|---|---|---|
| Recursive self-improvement (AI doing frontier AI research) | No | No, needs compute | D2; AI research benchmarks; uplift trials | Low to moderate if aimed at frontier training research, not coding in general | 1 |
| Unbounded scaling | No, algorithms substitute | Unclear | training compute, chip registries, power | Low today at a cap above the frontier; rises over time | 2 |
| Self-replication and resource acquisition | No | No | replication evaluations | Very low | 3 |
| Continual learning | No | No | update compute; weight-diff attestation; re-evaluation | Moderate | 4 |
| Long-horizon autonomy | Probably, to act unaided | No | task time horizons | High | 5 |

Reasons, briefly. Self-improvement is ranked first because it shortens breakout time most and
lets a party get around a compute cap through algorithms. Scaling is second because every path
consumes compute and compute is the only input with physical chokepoints (chips, fabs, power),
which makes it the enforcement backbone rather than the trigger. Self-replication is cheap to
forbid and closes the resource loop that enforcement relies on. Continual learning turns a
deployed fleet into a hidden training run (many small updates add up to training compute) and
makes pre-deployment evaluations stale, so it is handled by accounting and re-evaluation rather
than a ban. Autonomy is what makes AI useful, so it is limited only through oversight gates.
The survey and experiments decide the final ranking, and the ranking decides what the protocol
restricts.

## The protocol's shape

- **Who it binds.** States that join; through them, chip makers, cloud operators and labs.
- **Compute.** AI chips registered, running under licences that expire. Renewal needs k of n
  licensors from rival blocs. Escapement's height-difference lease fits here: a renewal must name
  a recent Bitcoin block hash, so licences cannot be signed in advance, and the chip's own counter
  ends the licence period.
- **Declarations.** Training runs above a threshold, their checkpoints and weight hashes, entered
  in an append-only log sealed in Bitcoin, so a party cannot backdate an entry or show inspectors
  two different histories. Escapement's seals fit here.
- **The line.** Evaluations at declared checkpoints and before deployment, on elicited
  capability (D5), against the weapons-grade line (D4). Continual-learning updates count toward
  compute and trigger re-evaluation when capability drifts.
- **Closed loops.** No autonomous AI research above a loop-gain threshold on frontier-scale
  systems; no deployed self-replication capability; no self-training outside the metered gates.
- **Verification without trusting one party.** Several independent channels (chip accounting,
  power and heat signatures, random challenge inspections on the chemical-weapons model, hardware
  attestation, rewarded whistleblowing), each with its own detection rate. The guarantee is the
  combined chance of missing a secret program over its breakout time. With one channel at the
  memo's placeholder rates, that chance is [30%](numbers.md#miss-prob-one-channel), which is why the design needs several.
- **Defection.** Inspection games for when compliance is each party's best response; a bound on
  the compute share a coalition needs to break out before it is detected; withdrawal notice
  longer than the response time.
- **Failure, stated up front.** Algorithmic progress shrinking breakout time at fixed compute;
  training spread across many small clusters; capability hidden beyond what elicitation recovers;
  covert chip fabrication; a major power that stays out.

## What Escapement contributes, and what it does not

It fits in two places: the unforgeable clock for chip licences (its height-difference lease and
the cost of speeding the clock), and non-equivocating, non-backdatable declarations (its seals).
It does not fit elsewhere. Escapement's own finding is that bonds cannot deter rare large harms,
and a state cannot be bonded. Metering an agent's spending sits downstream of the risk here, which
is in training. Proof of work as a meter of AI compute was rejected there and stays rejected.

## What looks strongest now

1. D4 with D3: the line between useful and dangerous AI, computed, and tied to the protocol's
   detection guarantee.
2. D2: a measurable trigger for the pathway ranked first.
3. D5: the defence against hidden capability, and the one most testable now on real models.

The weakest are D1 (needed as a definition, poor as a trigger) and D6 (possibly only framing). In
the protocol, the strongest parts are the compute chokepoint with expiring licences and sealed
declarations; the weakest are algorithmic progress at fixed compute and verifying training that is
spread across many small sites.
