# Level 6: a fresh review of the paper

A referee's report on "Subcritical", read as `build/subcritical-paper.md` (the flattened paper, read
in full before anything else), with statements checked against `research/`, `data/`,
`model/`, `tools/exp/` and `tools/formal/`. The assessment of every claim below was written before
opening `research/verification/` or `research/07-verification.md`; the last section, written
afterwards, says where this review disagrees with the earlier levels.

## Verdict

**Revise (major).** The paper is unusually candid: it says on nearly every page that the protocol
is a design, deployed nowhere and tested against no real adversary, and its negative results (E1's
unidentified drift, E4's failed trigger, E5's historical discovery rate, E18's jumps, E24's
response record) and its number-by-number provenance are a real service to the field. None of what
follows is fatal, because the paper does not claim that its protocol works. But several standings
and sentences a reader will rely on say more than the evidence. Three items are still offered as
possibly ours that are textbook or prior work: the margin lemma (C1(b)), the merging rule (C3) and
the footprint floor (C8). C5 stays a candidate on no evidence while C11, in the same position, is
downgraded. The authors' own assumed grades are called evidence (C12). The central covert
detection time is stated as a lower bound ("at least 32 years") that the experiment's own Weibull
fit undercuts. And the paper does not say that in the one calibrated model it cites, prevention at
its tolerance lies outside what the parties would consent to, nor that its line can be evaluated
today on no path but the declared one. Fixed, this is an honest synthesis-and-negative-results paper,
which is what it is; it should be framed and cut as one (about half its length).

## Each claim: the paper's standing and this review's

| Claim | Paper's standing | This review's standing | Why, in one line |
|---|---|---|---|
| C1 the line | application; (c) cut | application; (b) is prior work, not "possibly ours" | (a) is a definition; (b) is a factor of safety with multiplicative partial factors (M5) |
| C2 breakout time | downgraded to an accounting frame | agree; (c) is untestable as stated, not cut by a backtest | E18's backtest tested a substitute target; the stated one had 0 evaluable days (m4) |
| C3 detection | application; merging rule the only candidate | application; merging rule is prior work | the rule is the Frechet bound, standard in common-cause failure analysis (M5) |
| C4 loop gain | downgraded to a measurement design; trigger cut | agree on the design; "trigger cut" slightly harsh | the cut rests on a noise proxy from human speedrun records, not a staged AI round (m5) |
| C5 elicited capability | candidate, non-adaptive hiding only | an untested design, extending prior work narrowly | experiment not run, formal part textbook, closest prior work uncited; C11 is downgraded for less (M6) |
| C6 coupled-gain certificate | application; no certificate while edges unmeasured | agree | textbook bound; E11 shows nothing can issue |
| C7 coalition share | application of C1 | agree, and say it is vacuous on its own inputs | s* is 100% on the declared path; the overt line binds over 5% of the budget range |
| C8 footprint floor | candidate; (b) cut | application with calculations; not a candidate | (a) cannot fail, the ground that cut (b); (c) rests on an assumed pool with an invented spread (M7) |
| C9 licence clock | application, engineering | agree | E25 on the real header chain is the strongest empirical check in the paper |
| C10 matched-budget endpoint | downgraded to a definition; (c) narrowed | agree | but E21's "refuter" could not fail (m3) |
| C11 closure by input | downgraded to framing until E4(d) | agree | Theorem 11.2 is right; the test has not run |
| C12 pathway ranking | application; 12 of 21 pairs fixed by evidence | a judgement throughout; no pair is fixed by evidence | the grades are ledger inputs with basis "assumption"; weight theft is missing (M8) |

## Findings, ranked

### Fatal

None. No proof I checked fails, no experiment contradicts the paper's own conclusion, and the paper
never claims the protocol works.

### Major

**M1. The covert detection times are called lower bounds and measurements; they are neither.**
Passages: Introduction, "Why time is the axis": "Experiment E5 puts detection on undeclared paths at
31 years to 32 years ... These are measurements"; the physical perspective, P4: "gives the pool a
detection time of at least 32 years"; Part II, "Response time": "E5 puts detection at no less than
31 years"; "Undeclared compute and secret programmes": "Detection on that path takes at least 32
years". *What is wrong.* (i) The 32 years is ln(20) divided by a constant discovery rate fitted to
16 nuclear and biological programmes. E5's own Weibull fit, which the formal file says must be used
("the survival fit must estimate the shape, not assume k = 1", research/05-formal.md under
Corollary 1.3), gives 23.6 years (`e5-td-weibull-years`, shape 1.49, likelihood-ratio p 0.086), and
the constant-rate figure's own 5th percentile is 22.7 years. (ii) "Upper bound on a careful
evader's rate" is argued only from survivorship inside the sample; it says nothing about transfer
from programme-years of slow nuclear work to an AI breakout, which is the step that matters. (iii)
The 31 years for "one undeclared site above the satellite line" merges channels at the slowest rate
(Theorem 3.3's conservative end, which biases T_d up), and draws the satellite channel's chance
uniform on [0, 1] with no source (`tools/exp/e05_detection.py`, the satellite block: "judged perhaps
infeasible"); its 5th percentile is 0 years, and with satellites working as in the one sample it is
0 (`e5-td-site-satopt-years`). A median of a two-valued outcome is reported as the result. With
one bias up and one down, the figure is neither a lower nor an upper bound. The verdict that
covert paths fail the line survives all of this: in the short windows a breakout needs, the Weibull
finds less than the constant rate (2.6% against 8.9% in a year from a programme's start, as the red
team noted). What does not survive is the bound language and the word "measurements". *Fix.*
Report it as a central estimate under a stated transfer assumption, give the Weibull figure and the
interval beside it, drop "at least", "no less than" and "lower bound", call these transfers in the
introduction, and report the site's distribution, not its median.

**M2. In the one calibrated model the paper cites, prevention at its tolerance is outside what
parties would consent to.** Passages: D4, Evidence: "in Gan's illustrative calibration, holding
breakout success to 5% needs 7.8 times the monitoring that deters ... This design takes prevention
near the line"; Part II, "Prevention near the line". *What is wrong.* The 7.8 is this paper's
derivation, ln(1/0.05) / 0.383 (`def-gan-prevent-multiple`), using Gan's deterrence threshold at the
paper's own beta; Gan gives the formula, not the 5% calibration. More important, Gan's text bounds
monitoring by consent: "verification cannot consume more than either country's gain from
cooperation", m_max of about 0.056 findings a month at its baseline. Prevention at beta = 5% over
Gan's 12-month window needs ln(20) / 12, about 0.25 a month, roughly 4.5 times that bound. So the
model the design cites for pricing prevention says no party would accept it. *Fix.* State this
where prevention is chosen, attribute the 5% to the paper, and either argue why the consent bound
does not apply near the line or concede that prevention there is unsupported by the only
calibrated model.

**M3. Today the line can be evaluated on no path but the declared one, and the paper says this only
of the pool.** Passages: D4: "while the untraced chip pool is open, its path fails the line for
every party"; Part II: "cloud compute and distillation have no measured channel. No margin bridges
that, so the paths are treated differently". *What is wrong.* Cloud rental and distillation have no
measured channel, so their T_d is infinite (E5 misses them "with certainty"), and every party able
to rent or to query a stronger model fails the line through them too, independent of the pool.
Under the paper's own safe test for portable progress (Proposition 1.8, the shortest T_b against the
longest T_r), any party holding a frontier checkpoint fails. So the line is unmet for every party on
at least three paths, and the interim rule (classify on declared paths) applies it only where T_r
is an illustration. "Useful AI stays allowed" then rests on that interim rule, which the paper
itself says is no prevention guarantee. *Fix.* Say plainly in the introduction and in "Where the
promise is not kept" that the line is currently evaluable only on the declared path, with
illustrative inputs, and why cloud and distillation are restricted rather than lined.

**M4. "Why time is the axis" overstates what the time axis buys.** Passage: Introduction: "This
puts the line on a quantity computed from holdings and from the regime's own channels, rather than
on a capability score, which saturates, can be hidden, and crosses its threshold only at the
endpoint." *What is wrong.* T_b is the time to reach C*, the effective compute agreed to reach D1,
which the paper says cannot be measured before someone reaches D1 and is a convention; one OOM of C*
moves T_b by 2.3 years, more than the illustrative line of 2.0 years (`comp-years-per-oom-ho`,
`prot-line-declared`), and the margin does not cover it. The time axis relocates the capability
threshold into C* rather than removing it, and T_b is undetermined to within more than the line.
*Fix.* Qualify the contrast: the line is computed from holdings conditional on a negotiated C*,
whose error is unbounded and larger than the line itself.

**M5. Two items kept as "possibly ours" are textbook.** Passages: Introduction: "the margin as a
multiplicative error budget ... a one-line lemma whose likeliest earlier home, the safety-factor
literature, was not opened (C1(b)); an elementary rule for merging detection channels that share a
source (C3)"; Conclusion: "what may be ours is narrow: the margin as an error budget, a rule for
merging channels". *What is wrong.* C1(b) says that if T_b and T_r err by factors e_b and e_r, a
margin m >= e_b * e_r preserves the inequality. That is the partial-factor format of structural
design, where a load factor and a resistance factor multiply into the overall margin (EN 1990:2002,
Eurocode: Basis of structural design; ISO 2394:2015, General principles on reliability for
structures). The merging rule (the merged hazard is at least the largest under any dependence, at
most the sum under positive dependence, Theorem 3.3) is the Frechet bound on a union (Frechet,
"Generalisation du theoreme des probabilites totales", Fundamenta Mathematicae 25, 1935, DOI
10.4064/fm-25-1-379-387; identifier confirmed, text not read), and treating channels with a shared
cause as one is the common-cause failure practice of probabilistic risk
assessment (US NRC, NUREG/CR-5485, Guidelines on Modeling Common-Cause Failures in Probabilistic
Risk Assessment, 1998). *Fix.* Label both prior work, and remove them from the list of what may be
ours in the introduction, Part II's close and the conclusion. The remaining "ours" is then the
application and the measurements, which is the honest summary.

**M6. C5 is a candidate on no evidence, while C11 in the same position is downgraded.** Passages:
Introduction: "Two claims remain candidates ... (C5). They bound only hiding that does not adapt,
and the experiment has not run"; D5, Label. *What is wrong.* (i) C5's L3 is "untested" and its L2
is textbook (Clopper-Pearson, Ville); C11 is also untested with a correct theorem, and is
"downgraded to framing until tested". The two should stand alike. (ii) The closest prior work is
cited in the research files (research/03-novelty.md) but not in the paper: Hofstatter et al., "The
Elicitation Game: Evaluating Capability Elicitation Techniques" (arXiv 2502.02180), which already
compares elicitation methods on password-locked and circuit-broken organisms. (iii) External
validity: rates over regime-built organisms on small open models bound the miss rate only on that
population (Proposition 5.3); a frontier model's hiding, emergent or trained, is not drawn from it,
so the rates do not bound what the threshold needs. The paper says the guarantee weakens toward D1;
it should say the population gap applies at every capability level. *Fix.* Downgrade C5 to an
untested design, as C11; cite Hofstatter et al.; state the population gap.

**M7. C8 is not a candidate: its parts cannot fail or rest on an assumption.** Passages:
Introduction: "Two of its three parts are supported, on one experiment alone"; P4: "The untraced
pool is 340 times the BF16 floor (110 to 1,000, 5th to 95th percentile)"; Experiments, E8: "The
verdict supports C8(a) and (c)". *What is wrong.* (a) The floor as a bound is Theorem 8.1, a sum
(C = sum of each chip's work <= u_bar T sum r_j); it cannot fail, which is the ground on which (b)
was cut. (c) The pool's multiple divides a pool size the ledger marks as an assumption
(`phys-chips-unaccounted`, basis assumption, from a source sentence that the rest of 4.5 million
untraced chips "can likely also be traced") by the floor; the 110 to 1,000 range is the 5th and 95th
percentile of a log-uniform spread the authors chose ("our reading of 'order of magnitude', not a
sourced range", `tools/exp/e08_footprint_floor.py`). The crossing years are trend extrapolations.
E8 is a calculation on ledger inputs and cannot "support" a claim experimentally. What remains new
after crediting Fithian et al. (aggregate floor with a time axis, the pool counted against it) is
the choice of FP8 and full utilisation. *Fix.* Relabel C8 an application with calculations, report
the pool multiple as a point at an assumed pool with no percentile range, and say E8 computes, not
tests.

**M8. C12's "pairs fixed by evidence" are fixed by assumed grades, and the ranking omits weight
theft.** Passages: Introduction: "the pathway order as a judgement with 12 of 21 pairs fixed by
evidence (C12)"; "What the evidence fixes": "12 of the 21 pairs have one pathway ahead on both
criteria". *What is wrong.* (i) Each pathway's grade on each criterion is a 0-to-3 ledger input
with basis "assumption" (data/inputs/040-claims.toml, `claim-c12-*`); the count of Pareto-ordered
pairs is a property of the authors' reading, not of evidence. (ii) Six of the twelve pairs come from
one grade, long-horizon autonomy's effect of 0 ("adds nothing to the line by itself"), though the
pathway table says "Long-horizon competence is part of D1". (iii) Theft of weights "was not assessed
and is left as a gap", yet for a state it plausibly ranks first on both criteria (it moves T_b to
near zero and no compute channel sees it); see Nevo et al., Securing AI Model Weights (RAND, DOI
10.7249/RRA2849-1). A ranking that omits a likely first place cannot stand as a ranking of the
routes. *Fix.* Write "12 pairs are Pareto-ordered under our grades, which are judgements"; have
independent graders, blind to the paper's order, grade the table and report the count's spread;
either assess theft or narrow C12 to the six routes it assessed.

**M9. The covert-path verdicts assume detection does not depend on how intensely a party breaks
out, and the paper states this nowhere.** Passages: "Which pathways lead there": "The untraced pool
... would run a 1e+26 FLOP job in about 2.9 days ... at E5's fitted discovery rate ... a path only
the historical channels see takes 32 years to detect"; the formal file's (A1.1). *What is wrong.*
T_b on a covert path is computed from compute (days for the pool), while T_d is a per-calendar-year
discovery rate from programmes that ran for years at low intensity. A breakout's footprint (power,
procurement, staff, traffic) scales with its speed, so the hazard plausibly scales too, and
possibly up by orders of magnitude for a run of days on a million chips. The comparison sets a
quantity measured per unit of activity against one measured per unit of time. The direction of the
error is unknown, but every covert-path verdict and the tie at the top of C12 turn on it. *Fix.*
State the assumption; model the hazard as a function of footprint (E8's channel limits are a start);
show how the verdicts move.

### Minor

**m1. A cited result is misreported.** D-section opening: "when its location was uncertain,
catastrophe struck in 9 groups of 10 groups [@barrett2012climate]". The source says the threshold
was crossed in every group under threshold uncertainty; the probability of catastrophe was 100% in
9 groups and 93% in one. The ledger's label ("catastrophe was certain") is right; the paper's
"struck" is not. Fix: "was certain in 9 of 10 and struck in all 10".

**m2. Censored findings are reported as "never halted".** D4, Measurement, and E24: "25% of
findings made while a party was in its treaty were never followed by a halt, so the response time
has no finite 95th percentile". One of the two (USSR 1989) is censored at 447 days by the end of
the sources' coverage (`halt` in `data/results/e24_response_latency.json`), not observed unhalted.
With n = 8, say "not halted within the sources' coverage" and "the 95th percentile is not reached
within follow-up". The introduction also sets a Kaplan-Meier median (halts) against a minimum of two
exits (31 days); compare like with like.

**m3. E21's refuter could not fail.** D1: "the verdict flips on 45.3% of them, the pass
condition's refuter, met on contest entrants". The flip share is exactly the difference of the two
shares (71.1% minus 25.8%), since beating the gold threshold implies beating the median. Moving from
the median entrant to the gold threshold changes the rank compared against, not the organisation
within its class, and the "best entry" is chosen by medal share. Fix: report it as "the verdict
depends on the rank named", not as the pass condition's refuter.

**m4. C2(c) is untestable as stated, not cut by a backtest.** Experiments, E18: "(c) cut on E18".
The stated target, the open-closed lag, has 0 evaluable days (`e18-oc-evaluable-days`); what E18
tested was catch-ups to records, a substitute. Fix: "(c) cannot be tested on public data; a
substitute backtest bears against the constant-rate model".

**m5. "The trigger is cut" leans on a proxy.** D2 and Y1a. The only calibrated noise (sd 1.54 in each
round's log gain) comes from record-to-record variation in a human speedrun competition, not from
staged rounds of an AI research loop. "Fails at the only calibrated proxy; untested at real round
noise" is the accurate standing; the paper says the deciding test has not run, but its verdict
words are stronger than that.

**m6. Notation is overloaded in ways that misread.** beta is the miss tolerance (D4) and, in the
dynamical perspective, the returns exponent ("beta > 0 says ideas get harder to find"), within a few
hundred lines; rho is the spectral radius, Spearman's rho, the block-rate floor rho_min and the
threshold rho*; alpha is the cluster fraction (D1) and a confidence error (Y3); lambda is the return
to input and a detection rate. The formal file renames beta to b; the paper should do the same
throughout.

**m7. "Weapons-grade" invites misreading.** In nuclear usage it names a material property
(enrichment), not a time; here it labels holdings by a race between clocks, and on today's inputs
labels every party (M3). A neutral term ("inside the line") would avoid readers taking it as a
capability verdict.

**m8. Standing labels disagree between tables.** The verification record gives C12's L1 as
"extends" and its standing as "application"; the definitions table gives D3 "a combination of prior
work" where the record gives C2's L1 as "extends"; the introduction counts "five claims to be prior
work in substance" and then says "these six stand as applications". One label set, used once.

**m9. Missing prior work that a referee would expect, not changing a standing.** Hendrycks, Schmidt
and Wang, Superintelligence Strategy (arXiv 2503.05628): the most prominent deterrence-based
proposal against superintelligence, directly relevant to the conclusion that the protocol offers a
major power "deterrence only"; it is cited in the research files and not in the paper. Wasil et
al., Verification methods for international AI agreements (arXiv 2408.16074), and Harack et al.,
Verification for International AI Governance (Oxford AIGI, 2025), likewise cited in research/ only.
Avenhaus and Canty, Compliance Quantified (ISBN 9780521553667), the standard text on verification
statistics in safeguards, in sources.toml but uncited. Downs, Rocke and Barsoom (DOI
10.1017/S0020818300033427) on why observed treaty compliance says little about deep cooperation,
which bears on footing 4 (the states that host the chokepoints bind themselves). Bonneau, Clark and
Goldfeder, On Bitcoin as a public randomness source (IACR ePrint 2015/1015), for the inspection
beacon the paper marks "not searched".

**m10. A secondary citation.** P4: "A satellite classifier found every facility above 10 MW and missed
every one below, in a small sample [@koopmanschap2026gpu]". The source reports this from Clymer
(2025) in its Appendix B; cite the primary work.

**m11. The copy count mixes two batch regimes.** P1: "The chips sold in 2025 could run about
140,000,000 PaLM-sized copies at measured speed". The count divides compute at 40% utilisation by
compute per copy at the small-batch speed (29 ms a token); at small batch serving is memory-bound,
and at the batch sizes that reach that utilisation the per-copy speed is lower. Say it is an upper
bound on copies at that speed.

**m12. Closure's two definitions are joined without the caveat.** D6: "In the loop's exponent the
closures add, weighted by the inputs' shares ... (Part III)". Theorem 11.2 is about closure as an
elasticity; D6 defines it as a share of ungated increments. The formal file flags that reading one
as the other is for E4(d) to check (research/05-formal.md, after Theorem 11.2); the paper's D6 should
say so too.

**m13. The verification bookkeeping crowds out the argument.** Each claim's standing is stated in
the introduction, the definitions table, its own section, Part II's close, the verification record
and the conclusion, with the level verdicts repeated; roughly a fifth of the text. A reader in the
field will struggle to find the argument. Keep one record table and one statement per claim, and cut
the paper to about half its length.

## What a reader needs that is missing

- **An experiment that would decide C12's wording:** independent graders, blind to the order, grade
  the pathway table; report how many pairs are Pareto-ordered across graders.
- **A measured detection rate for any AI-specific channel against a resourced red team,** in the
  manner of field trials in arms-control verification: a covert run hidden in a cooperating facility,
  with the regime's channels scored blind. Without one, every T_d in the paper is a transfer.
- **Hazard as a function of footprint (M9),** which decides the covert-path verdicts and the tie at
  the top of the ranking.
- **Threats not addressed:** theft or exfiltration of weights (M8); a model that games the
  evaluations that gates rest on, which is adaptive hiding, the case D5 excludes, so every gate keyed
  to elicited capability is open to it; collusion among log replica operators or licensors beyond
  the stated t of n; a maker's host state compelling the secure element's keys.
- **Assumptions stated nowhere:** that effective compute is one scalar across training, inference,
  post-training and distillation, so one C* serves every path; that detection hazard is independent
  of breakout intensity (M9); that the parties agree on C* and the tables, which Barrett and
  Dannenberg's result, cited in D-section, says is the crux.

## What I traced and opened

### Numbers traced, text to ledger to input or result

| Number in the text | Ledger id | Traced to | Holds? |
|---|---|---|---|
| 31 years (undeclared site) | `e5-td-site-now-years` | `data/results/e05_detection.json`, 31.45; code read | value holds; framing does not (M1) |
| 32 years (pool) | `e5-td-pool-years` | same file, 31.90 = ln(20) / 0.0938 | holds; Weibull gives 23.6 (M1) |
| 39.0 days (declared) | `e5-td-declared-days` | same file, 39.03 | holds; a design figure, as stated |
| 1.2 years (halt median) | `e24-halt-km-median-years` | `e24_response_latency.json`, 432 days; Kaplan-Meier recomputed by hand from the eight cases | holds |
| 31 days (fastest exit) | `e24-exit-min-days` | same file: finding 1993-02-09 to withdrawal 31 days later, para. 6 of the cited IAEA document | holds |
| 25% never halted | `e24-halt-share-never` | same file, 2 of 8, one censored by coverage | value holds; wording does not (m2) |
| 8 of 10, 9 of 10 | `def-bd-known-avoided`, `def-bd-uncertain-catastrophe` | `data/inputs/010-definitions.toml`, then the source | 8 holds; "struck in 9" does not (m1) |
| 4 times at 2 h, 2 times at 32 h | `def-rebench-agent-advantage`, `def-rebench-human-advantage` | inputs, then the source's abstract | holds |
| 71.1%, 25.8%, 45.3% | `e21-mle-*-best` | `e21_team_battery.json`; 45.3 = 71.1 - 25.8 | holds (m3) |
| 2.3 years per OOM | `comp-years-per-oom-ho` | `ln(10) / ln(2.7)`, `model/parts/012_computational.py` | holds |
| 88%, 2% (K rule) | `e4-k-fa-n5`, `e4-k-fire-gap-n5` | `e04_loop_gain.json` | holds |
| 0.57, 8.11 | `e4-diff-bias-meas1`, `-meas2` | same file | holds |
| 0.23 (IAEA margin, metal) | `def-iaea-m-metal-low` | 7 days over a 1-month goal, inputs via `model/subcritical.py --only` | holds |
| 7.8 (prevention over deterrence) | `def-gan-prevent-multiple` | ln(20) / 0.383, checked against Gan's text | arithmetic holds; attribution and context do not (M2) |
| 2.6 to 1,512 a year | `e1-algo-annual-subset-min`, `-max` | `e01_capability_compute.json` | holds |
| 1,000,000 untraced chips | `phys-chips-unaccounted` | input, basis assumption, then the source's Sec. 5.3.2 | holds as the source's estimate (M7) |
| 3.2 and 10.6 (in-run factors) | `formal-inrun-line-factor`, `-high` | (e^(ax) - 1) / (ax), a = ln 2.7 and ln 6.3, x = 2 years; recomputed | holds |
| 22 organisms | in the text only | 0.9^n <= 0.1 gives n >= 21.85; recomputed | holds |
| 12 of 21 pairs | `claim-c12-pareto-two` | `model/parts/040_claims.py` over `claim-c12-*` grades, basis assumption | arithmetic holds; "fixed by evidence" does not (M8) |
| 60% to 95% from compute | `phys-compute-share-low` | input, then the source's Sec. 4.1 | holds |

### Sources opened by identifier

| Key | Identifier | The paper says | The source says | Verdict |
|---|---|---|---|---|
| wijk2024rebench | arXiv 2411.15114 | agents 4 times experts at 2 h; experts 2 times the top agent at 32 h | abstract says exactly this, and that humans narrowly lead at 8 h | holds |
| wang2023adversarialgo | arXiv 2211.00241 | an adversarial policy beats superhuman KataGo over 97% of the time | ">97% win rate against KataGo running at superhuman settings" | holds |
| ho2024algorithmic | arXiv 2403.05812 | compute halving every 8.4 months; compute credited with 60% to 95% of gains | abstract: about 8 months (95% CI about 5 to 14); Sec. 4.1: "60-95% of the performance gains stem from compute scaling" | holds |
| barrett2012climate | DOI 10.1073/pnas.1208417109 (read as PMC3491499) | catastrophe avoided in 8 of 10 with a known threshold; struck in 9 of 10 when uncertain | 8 of 10 avoided under certainty; under threshold uncertainty the threshold was crossed every time, probability 100% in 9 groups and 93% in one | misreported (m1) |
| gan2026clock | arXiv 2611.04272 | D4 at m = 1 is Gan's prevention condition; prevention needs 7.8 times the monitoring that deters | m >= ln(1/beta) / w is stated; deterrence needs 0.0319 findings a month at a 12-month window; monitoring is capped by consent at about 0.056 a month; no 5% calibration | holds with the omission in M2 |
| koopmanschap2026gpu | arXiv 2607.22619 | about a million chips untraced; a satellite classifier found every facility above 10 MW | 15.7 of 20.2 million traced, "much of the remaining 4.5 million can likely also be traced, leaving on the order of a million"; the 10 MW result is reported from Clymer (2025) | holds; secondary citation (m10) |
| hofstatter2025elicitationgame | arXiv 2502.02180 | not cited in the paper | evaluates elicitation techniques on password-locked and circuit-broken model organisms | closest prior work to C5, missing (M6) |

Identifiers also confirmed for missing prior work: Nevo et al. (DOI 10.7249/RRA2849-1), Bonneau,
Clark and Goldfeder (IACR ePrint 2015/1015), Downs, Rocke and Barsoom (DOI
10.1017/S0020818300033427).

### Proofs and checks

Read and followed step by step: Lemma 1.1, Propositions 1.2, 1.4, 1.8 (including the equality case
and the implication from the strict scalar test), Corollary 1.6a, Theorem 6.4 (both parts, through
the similarity M = D K D^-1, Jensen's step and the Dini-derivative bound), Theorem 7.2 and its
repeated-play remark, Theorem 11.2. No step fails. Rerun once, under `heavy`:
`python3 tools/formal/run_all.py`, all thirteen checks pass (exit 0), as the paper states. The
checks search random instances; they test statements, not proofs, as the paper says. Experiment code
read, not rerun: the E5 detection and merging block, the E8 header and pool spread, the E24 halt
analysis, the C12 grade count.

## Where this review disagrees with the earlier levels

Written after the assessment above, on reading `research/07-verification.md` and the three reports
in `research/verification/` (L1 for C1 to C6 and C7 to C12, L4).

**Agreed.** The standings of C2, C4, C6, C7, C9, C10 and C11; L2's corrections; and L4's attacks that
the paper now carries correctly (C1.1 switching, C1.2 the open pool, C1.3 the error in C*, C3.4 the
two-dimensional common cause, the C7 conditions). The paper's proofs reflect those corrections.

**Disagreed.**

1. **C1(b).** L1 left it as "a small lemma" that "may stand as an extension", named the partial
   safety factors of structural reliability as its likeliest home, and did not open them. This
   review decides that search: it is the partial-factor format (M5). Prior work.
2. **C3's merging rule.** L1 kept it "only if L4 and L6 agree it is more than the textbook bound",
   and itself named Frechet's 1935 bounds as its source. It is not more than the textbook bound.
   Prior work; C3 has no candidate left.
3. **C5.** L4's C5.1 already showed that a population miss rate bounds only the sampled
   population, and E3 has not run. The rule the record applies to C11 (untested, so framing until
   its experiment runs) applies to C5 equally. An untested design, not a candidate (M6).
4. **C8.** L4 cut (b) because it could not fail, and rated the assumed pool and its invented spread
   minor because "no verdict moves". (a) cannot fail either, being a sum, and (c)'s range is the
   authors' prior; E8 computes and cannot give L3 support. The record's "L3 supports (a), (c)" should
   read "computed, not tested", and C8 is an application (M7).
5. **C12.** L4's C12.1 counted pairs "fixed by the evidence" from the table's qualitative entries,
   and the record now claims 12 evidence-fixed pairs. The entries are the authors' readings, encoded
   in the ledger as assumptions; Pareto dominance on judgements is still judgement. Weight theft,
   which L4 raised only as an ungated edge (C6.3), is absent from the ranking as a pathway (M8).
6. **E5.** L4's C3.3 found that the Weibull finds less than the constant rate in a breakout's short
   window, and the paper took that. No level caught that "at least 32 years" contradicts the same
   Weibull's 23.6-year T_d, that the site figure merges channels at the slowest rate, or that its
   satellite chance is an unsourced uniform draw (M1).
7. **Raised by no level.** Gan's consent bound against prevention (M2); cloud and distillation
   failing the line for every party, beyond the pool that L4's C1.2 covers (M3); detection hazard
   independent of breakout intensity (M9); the introduction's case for the time axis, which C1.3's
   finding on C* undercuts but whose fix did not reach the introduction (M4); the misreported
   Barrett and Dannenberg result (m1); E24's censored "never halted" (m2); E21's refuter that could
   not fail (m3).
8. **C4.** The record says the trigger is cut at L3. This review would say it fails at the only
   calibrated proxy (m5): a softer word, not a different standing.

The record and the paper say L6 has not run. It now has; this report is its result.
