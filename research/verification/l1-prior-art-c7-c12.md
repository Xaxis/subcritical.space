# Level 1: prior art for C7 to C12

This is the level 1 check of [the claims file](../04-claims.md) for C7 to C12: a prior-art search by
a helper that did not propose the claims and had not read the work before. It was run on 2026-11-27.
It starts from each claim's statement, its "Prior work, and what differs" paragraph, its **L1.** plan
and the entries in [the novelty file](../03-novelty.md), and does not repeat the searches listed
there. It searches wider, in the fields the ideas could have come from under other names.

**How the search was run.** Every search below was run on 2026-11-27. "Web" means the agent's web
search tool, in its standard mode unless marked "extended"; it sometimes rewrote a query or ignored a
`site:` operator, and where it did, that is said. "arXiv API" means the export.arxiv.org query
interface, with the exact query string given. Google Scholar redirected every automated request to a
bot check, so no Scholar result was read. The Semantic Scholar API refused every request with HTTP
429 (rate limit), so it returned nothing. SSRN and IACR ePrint were searched through the web tool
with a `site:` operator, which it ignored; IACR ePrint itself returned a bot challenge for the PDFs
of 2016/1062 and 2015/1015, so copies elsewhere were opened instead (named where used). Identifiers
were checked against Crossref and doi.org. Each work cited below was opened, and the passage relied
on is quoted with its section or page. A work found but not opened is named as such and not cited.

"Not found" below is a statement about these searches, not about the world.

## C7

**The claim in one line.** The largest coalition share s* = min(1, h_w / (m * T_r)) is derived from
the response time, and no coalition whose breakout time is at least T_r has a profitable
self-enforcing deviation if each member's reward for reporting exceeds beta times its value of a
successful breakout.

**Searches tried (all 2026-11-27).**

1. Web, extended: `coalition share compute breakout time detection response AI treaty threshold derived`.
2. Web: `"coalition-proof" arms control verification agreement detection`.
3. Web: `cartel stability detection lag collusion "detection lag" incentive to deviate share of capacity`.
4. Web: `Aubert Rey Kovacic "The impact of leniency and whistle-blowing programs on cartels" rewards individuals`.
5. Web: `"coalition-proof" international environmental agreements self-enforcing stability`.
6. Web: `multinational enrichment facility seizure breakout share of capacity host state safeguards timeliness`.
7. Web: `"coalition-proof" OR "coalition proofness" AI governance international agreement compute`.
8. Web: `self-enforcing agreement monitoring delay detection lag punishment delay repeated game "monitoring lag" treaty compliance`.
9. Web: `"Feasibility of a Hardwired Pause" coalition breakout threshold response time cited` (a search for
   forward citations of the hardwired-pause paper).
10. Web: `"Parameters for a Joint Comprehensive Plan of Action" "breakout timeline" "at least one year" whitehouse archives`.
11. Web: `site:ssrn.com treaty coalition breakout detection response time compute OR nuclear "self-enforcing" whistleblower reward`
    (the tool dropped the operator; no SSRN paper came back).
12. arXiv API: `all:breakout AND all:coalition` (0 results); `all:breakout AND all:compute AND all:treaty`
    (0); `abs:coalition AND abs:"AI" AND abs:compute AND abs:agreement` (1, unrelated);
    `abs:coalition AND abs:"breakout"` (0).
13. Google Scholar: `"coalition" "breakout time" compute agreement` (redirected to a bot check; nothing read).
14. Semantic Scholar API: `coalition breakout time detection compute agreement` (HTTP 429).
15. Full-text searches of the hardwired-pause paper for "coalition", "horizon" and "respond to
    defection", and of the Gan paper for "coalition", "multilateral" and "share".

**Closest works found, each opened.**

- **The hardwired-pause paper** [@fithian2026hardwired]. Its overt breakout fleet threshold is a
  budget divided by a horizon and a utilisation, and the horizon is tied to the time others need to
  react, then chosen: a defector must "attain its decisive advantage before the rest of the world
  could react to stop it", so "To reflect the time sensitivity of the breakout strategy, we adopt a
  breakout time horizon of T B = 2 years" (section 6.2.3). It adds that "The choice of breakout time
  might likewise be sensitive to ... expectations and possible commitments about how coalitions would
  respond to defection", and that a realised threshold "would be a matter of negotiation and trust
  more than one of estimation" (section 6.2.3). Footnote 23 to section 3.2.3: "there might be
  per-coalition allowances in addition to per-state allowances". How it differs: the horizon is
  chosen, not computed from a regime's channels; coalitions get a footnote, not a share. But dividing
  that threshold by the fleet gives exactly C7(a)'s s* with the horizon set to m * T_r. The project's
  own formal file says so: s* "is the hardwired-pause fleet threshold [@fithian2026hardwired] solved
  for the share, with the horizon set to m T_r instead of chosen" ([C7 in the formal
  file](../05-formal.md#c7-the-coalition-share)). At that paper's inputs h_w is
  [7.8 years](../numbers.md#claim-whole-fleet-horizon), and its overt threshold is
  [3.9](../numbers.md#def-hwp-fleet-over-global) times the projected global fleet.
- **The JCPOA parameters** [@whitehouse2015jcpoaparameters]. Holdings limits derived from a
  breakout-time target, for one state: the breakout timeline, "currently assessed to be 2 to 3
  months", is to be extended to at least one year for at least ten years, by cutting installed
  centrifuges "from about 19,000 installed today to 6,104" and the enriched stockpile to 300 kg
  (fact sheet of 2 April 2015). How it differs: one state, a chosen target, no coalitions, no
  response time. It shows that the step "set holdings so that breakout exceeds a target time" is
  arms-control practice.
- **An essay on AI breakout time** [@williams2026breakout]. A per-entity compute cap set by a target
  breakout time: "at bare minimum, the targeted breakout time should be two to three years", which
  "allows time for somewhat sluggish human institutions to react", and "Yes, that's somewhat
  arbitrary". It caps "the maximum allowable compute held by any one entity". How it differs: chosen
  target, no coalitions, no game.
- **Rewards for reporting a cartel** [@aubert2006leniency] (the 2005 working-paper version was
  opened). Lemma 1 (section 3.1): "In order to induce a firm to report collusion, the antitrust
  authority must offer a reward at least equal to R", the value of continuing collusion net of
  deviating. Section 3.3: with a bounty B to informed employees, "colluding firms will have to 'bribe'
  informed employees in order to secure their fidelity", so collusion is sustainable only if
  δB/(1-δ) ≤ (R + ρF)/n (a displayed inequality, transcribed), and "as the number n of informed employees increases, collusion becomes
  more and more fragile". How it differs: firms in a market, not states in a treaty; repeated play,
  not a one-shot breakout. The structure is C7(b)(i)'s: a joint deviation is not self-enforcing when
  the reward for reporting exceeds what each insider expects from staying silent. C7(b)(ii), no
  party profits when beta * V_i <= (1 - beta) * P_i, is the textbook deterrence inequality.
- **A bribery game for alerts** [@mouallem2026alerting]. "a game between a bribing adversary and n
  rational participants, who pay a penalty if they are caught deviating from the protocol" (abstract),
  asking how much an adversary must pay to stop every participant raising an alert. How it differs:
  smart-contract alerts, not treaty breakout; it is the same game as C7(b) seen from the deviator's
  side, and gives a design (rewards and penalties scaled with the number of reporters) that C7 lacks.
- **Coalition-proofness in treaties** [@shinohara2025coalitionproof] (abstract only). It tests
  surplus-sharing rules in international environmental agreements "using a coalition-proof Nash
  equilibrium". How it differs: climate treaties, no detection or breakout. It shows the concept C7(b)
  borrows has been applied to treaty membership before.
- **The bilateral clock** [@gan2026clock]. The follower's catch-up time "less the implementation
  delay supplies the follower's response window" (section 1). A full-text search finds no coalition
  share. It is bilateral, as the claims file says.

**Verdict: prior work.** C7(a) is the overt breakout fleet threshold of [@fithian2026hardwired]
divided by the fleet, with the horizon replaced by m * T_r; deriving allowed holdings from a breakout
target is older still [@whitehouse2015jcpoaparameters]. The only input C7(a) adds is T_r computed
from the regime's channels, and that is C1's claim, not C7's. C7(b)(i) is the reporting-reward
condition of [@aubert2006leniency], transposed from cartel members to coalition members; (b)(ii) is
the standard deterrence condition; (b)(iii) is a construction. C7(c) is arithmetic at the
hardwired-pause paper's inputs. Nothing in C7 survives that is independent of C1. It should be cut as
a contribution and kept as an application: C1 applied to the hardwired-pause threshold for
coalitions, with the reporting condition credited to the cartel-leniency literature.

**Confidence and what could overturn it.** High that each part is prior work; the passages are
explicit. The coalition application itself was not found, so a search could find it done, which
would only confirm the verdict. Nothing found here could raise it. Searches not run: Spagnolo's work
on leniency and self-reporting, and the alliance-burden-sharing literature, which could hold an older
coalition version of the reporting condition.

## C8

**The claim in one line.** The aggregate footprint floor N_min = C / (r * u_bar * T) is a bound at
the highest attainable utilisation, with a time axis, a detection margin per channel, and the untraced
pool counted as a covert reserve that already exceeds the floor.

**Searches tried (all 2026-11-27).**

1. Web: `"significant quantity" compute AI chips safeguards analogy "material unaccounted for" GPUs`.
2. Web, extended: `minimum number of GPUs to train frontier model covertly within time limit detection threshold chip accounting unaccounted chips`
   (the tool declined the query as written and returned verification-side results instead).
3. Web: `"Does Distributed Training Undermine Compute Governance" Rahman cited` (forward citations of
   the distributed-training paper).
4. Web: `covert AI training run detection satellite power threshold falls over time hardware efficiency year projection "untracked chips" breakout`.
5. Web: `"dark compute" AI treaty verification estimate covert evasion ledger`.
6. Web: search 9 under C7, which found a post announcing the taxonomy paper below (forward citations
   of the taxonomy paper: none found beyond that post).
7. arXiv API: `abs:"compute governance"` (23 results, titles scanned); `abs:"footprint" AND abs:"training run" AND abs:detection`
   (0); `abs:"covert" AND abs:"training" AND abs:"compute governance"` (0).
8. Full-text searches: the hardwired-pause paper (its threshold definitions, section 3.2.3 and
   sections 6.2.2, 6.2.5 and 6.4.3); the taxonomy paper (section 5.3 and appendix B); the IAEA
   glossary for "MUF" and "significant quantity"; the compute-governance overview for "significant
   quantity" and "unaccounted"; the closing-window paper for "untracked" and "smuggl".

**Closest works found, each opened.**

- **The hardwired-pause paper** [@fithian2026hardwired], which C8's prior-work paragraph does not
  cite. Its evasion fleet threshold is an aggregate floor in chips with a time horizon in the
  denominator, F_E(t) = rho_E * C_E(t) / (T_E * U_F) (a displayed equation, transcribed), "where U F
  represents a standardized utilization attained by present-day frontier AI companies" (end of section
  3.2.2). Its covert
  evasion ledger counts every source, dark compute included, against that floor: "L E ≤ α E ⋅ F E ,
  where L E ( s ) = ∑ c K E ( c , s )" (section 3.2.3). And it draws C8(d)'s conclusion in kind: dark
  compute "would need to be reduced through other measures such as discovery and registration of
  pre-pause stock, prevention of illicit manufacture, and verification measures that rely on detecting
  when such dark compute is being used" (section 3.2.3). On scale: "a million missing H100e units
  would approach 16% of F E" (section 6.4.3). How it differs: U_F is a typical frontier utilisation,
  not the highest an adversary can reach, so F_E is an estimate, not a bound; T_E is a strategic
  horizon chosen by judgement; there is no detection margin per channel; and its covert target is
  frontier scale, so the untraced pool (the ledger's [1,000,000 chips](../numbers.md#phys-chips-unaccounted))
  is a fraction of its threshold, where C8 uses smaller runs and finds the pool far above the floor.
- **The enforcement taxonomy** [@koopmanschap2026gpu]. Detection limits per channel by facility size:
  "The analysis traces how that signature weakens as facility size shrinks from 10,000 to 100
  H100-equivalents" (appendix B), rated in its Table 5 ("Enforcement breaking point analysis for
  sub-problem: detect hidden capacity"), with a time direction stated in words: "Because the compute
  required for dangerous capabilities may decrease over time, more actors can violate an agreement and
  enforcement of these policies becomes harder" (abstract). How it differs: per site, rated
  qualitatively, no aggregate floor, no crossing year.
- **The IAEA's accounting lesson** [@iaea-glossary-2022]. Entry 9.6 (page 90): diversion into MUF
  goes undetected "if σMUF is large because measurement quality is poor, because there are large
  quantities of poorly or improperly accounted for material, or because of very large inventories
  and/or throughputs in a facility". This is C8(a)'s requirement, that chip accounting resolve
  quantities finer than N_min, in its nuclear form. The physical chapter already cites it; C8's
  prior-work paragraph does not.
- **The closing-window paper** [@barnett2026closingwindow]. Hardware proliferation "would make it
  impossible to ensure there are not large quantities of untracked chips" (section 4). Qualitative;
  no floor or margin.
- **The compute-governance overview** [@sastry2024compute] was searched in full text for "significant
  quantity", "unaccounted" and "material accounting"; it uses none of them in this sense. A negative
  result, recorded so it is not rerun.

**Verdict: extends prior work, with a narrower difference than the claim states.** The formula as an
aggregate floor in chips with a time axis, the untraced pool entered against it, and the conclusion
that the pool must be shrunk rather than found are in [@fithian2026hardwired]. C8(a)'s resolution
requirement is the IAEA's MUF lesson [@iaea-glossary-2022]. Per-channel detection limits by facility
size are in [@koopmanschap2026gpu]. What remains not found: (1) the floor as a bound, at the highest
attainable utilisation and lowest energy per operation, where the hardwired-pause threshold is an
estimate at standard utilisation; (2) each facility channel's margin as a ratio to the floor, with the
year it crosses one; (3) the pool's multiple of the floor at small-run inputs, with a measured
discovery rate behind (d). C8's prior-work paragraph must name [@fithian2026hardwired] as the closest
work, and (c) and (d) should be stated as that paper's ledger at other inputs, with the bound and the
discovery rate as the difference.

**Confidence and what could overturn it.** Moderate. The two remaining differences are computations
others could easily have run; a crossing-year analysis of satellite or grid detection, for example by
Epoch AI or in a follow-up to the taxonomy paper, would remove (2). No such analysis was found.

## C9

**The claim in one line.** A chip licence named by a recent Bitcoin block hash, ending at a block
height with a floor on the header rate per unit of the chip's powered time, and valid only once it
appears in a fully published append-only log anchored in Bitcoin that also holds sealed training-run
declarations.

**Searches tried (all 2026-11-27).**

1. Web: `Catena efficient non-equivocation via Bitcoin Tomescu Devadas transparency log`.
2. Web, extended: `trusted time for TEE or secure element from blockchain block headers proof-of-work clock offline device expiry`.
3. Web: `software license expiry block height bitcoin headers hardware enforce license blockchain time`.
4. Web: `Tesseract real-time cryptocurrency exchange trusted hardware enclave block headers rate trusted relative time eclipse fake chain`.
5. Web: `Apple Private Cloud Compute transparency log devices only send data to nodes whose software is publicly logged verifiable transparency`.
6. Web, extended: `AI chip licence transparency log hardware-enabled mechanism blockchain anchored non-issuance flexHEG equivocation`
   (forward citations of the flexHEG reports: none found that use a blockchain or a log for licences).
7. Web: `proof-of-work blockchain as secure time source for offline or IoT devices header chain lower bound on elapsed time cost of forging headers`.
8. Web: `"proof of non-issuance" OR "proofs of non-issuance" transparency log certificate licence`.
9. Web: `blockchain shared ledger nuclear safeguards arms control verification declarations tamper-evident PNNL Frazar exploratory study`.
10. Web: `Bonneau Clark Goldfeder "On Bitcoin as a public randomness source" block hash beacon unpredictable`.
11. Web: `site:eprint.iacr.org licence OR license expiry block height light client trusted hardware transparency log non-equivocation`
    (the tool dropped the operator; nothing close came back).
12. arXiv API: `abs:"transparency log" AND abs:licen*` (0); `abs:"block headers" AND abs:time AND abs:enclave`
    (0); `abs:"transparency log" AND abs:hardware` (6, none close); `abs:"block headers" AND abs:"trusted execution"`
    (1, a payment hub, not close).
13. Direct reads: RFC 6962; the flexHEG Part II report for "blockchain", "clock" and "save up"; the
    Lightning peer protocol specification for HTLC expiry.

**Closest works found, each opened.**

- **Freshness from a block hash (P1).** A Bitcoin beacon "outputs unpredictable and publicly
  verifiable randomness, meaning that the output is unknown at the time that πbeacon starts"
  [@bentov2016beacon] (abstract). Anything that names a block hash therefore cannot predate that
  block. A trusted-hardware protocol uses the same move with a challenge: "the TEE stores a checkpoint
  header 𝐶𝐵 and generates a random challenge 𝑟 . The node creates the transaction tx that is
  cryptographically tied to 𝑟" [@mouallem2026alerting] (section 7.3). How it differs: neither is a
  licence. The chip nonce of the authors' cited prior work gives the same property online; the block
  hash adds only that it works offline and anyone can check it, which the beacon literature already
  gives.
- **A block-height clock inside trusted hardware (P2).** The same protocol keeps a monotone chain
  view inside the TEE and counts blocks as time: "To verify that sufficient time has elapsed, the TEE
  validates a chain of block headers input by the node", "The TEE maintains this checkpoint
  monotonically. This prevents rollback", and it rejects "headers from some other chain (e.g., a
  faster side chain)" by checking the chain's identity through the checkpoint hash
  [@mouallem2026alerting] (section 7.3). How it differs: a deadline that must have passed, not an
  expiry; no rate floor.
- **A floor on the header rate per unit of trusted local time (P2).** An enclave exchange defends
  against a fed chain exactly as C9's corrected rule does: "we rely on the fact that the rate at which
  A can feed fake blocks to the enclave is at least twice slower than in the absence of an attack ...
  Assuming that the TEE has a trusted clock, the enclave can impose a rule that requires waiting for
  additional confirmations if the blocks arrive too slowly", with a slowness factor δ, the Erlang
  distribution of honest block times, and the trade-off C9's honest runs found: "Setting δ to a high
  value reduces the probability of a false positive (i.e., a rejected deposit when no attack is taking
  place and the honest chain growth was unluckily slow ...). However, a high δ also increases the
  prospects of an attack" [@bentov2019tesseract] (section 2.3). It also hardcodes a difficulty: "This
  prevents an adversary ... from feeding a low-difficulty fake chain to the enclave" (section 2.2). How
  it differs: the response to slow blocks is to wait, not to stop; there is no licence budget. C9's
  bound, at most (L + s) / rho_min of powered time per licence, follows directly from such a rule.
- **Block height as an expiry (P2).** Lightning's peer protocol expires HTLCs by height: "the
  protocol only supports an expiry in blocks" [@lightning-bolt2] (section "Adding an HTLC:
  update_add_htlc", rationale). Device time from headers, with resistance to forged blocks, is studied
  for IoT [@regnath2020blockchaintime] (abstract: "we leverage the availability of time information
  in the block headers ... to estimate the true time"). flexHEG names the idle-chip weakness of a
  cycle counter, "there is a risk that the operator secretly does not use the chip to save up usage
  time" (page 38, footnote 14), and uses "the presence of that hash in the history of a public
  blockchain" as a delay proof (page 34) [@petrie2025flexheg2].
- **No undetected equivocation, anchored in Bitcoin (P3).** "Catena implements a log as an OP_RETURN
  transaction chain and prevents forks in the log by leveraging Bitcoin's security against double
  spends. Specifically, if a log server wants to equivocate it has to double spend a Bitcoin
  transaction output", and "our clients only need to download all Bitcoin block headers ... and a
  small, 600-byte proof for each statement" [@tomescu2017catena] (abstract; MIT copy opened). It names
  software transparency and public-key directories as uses. How it differs: not licences or treaty
  declarations. This is closer to P3 than the transparency logs and timestamping the claims file
  cites.
- **Valid only once logged, and non-issuance (P4 and (iii)).** "TLS clients MUST reject certificates
  that do not have a valid SCT for the end-entity certificate" (section 3), with the intent that
  "eventually clients would refuse to honor certificates that do not appear in a log" (abstract), so
  that domain owners "can thus check whether domains they are responsible for have had certificates
  issued that they did not expect" (section 1) [@laurie2013ct]. A deployed hardware case: "the user's
  device will wrap its request payload key only to the public keys of those PCC nodes whose attested
  measurements match a software release in the public transparency log" [@apple2024pcc] (section
  "Verifiable transparency"). How it differs: certificates and server software, not chip licences;
  an SCT is a promise to log, where C9 asks for inclusion. Once validity requires the log, the log's
  contents are the set of valid items, which is C9's proof of non-issuance.
- **Sealed treaty declarations on a blockchain (the declarations in (iii)).** An arms-control
  report proposes "a 'cryptographic escrow' for treaty declarations. Contracting parties could make
  encrypted declarations at an early stage ... and hash the data on a blockchain", so that "parties
  could verify that the data revealed was a precise match for the declarations made at the start"
  [@burford2020trustmachine] (PDF page 16; also page 11 on a stockpile declaration encrypted, signed
  and hashed). How it differs: warhead and stockpile declarations, not training runs; the novelty
  file's "not found" for treaty declarations anchored in a blockchain does not hold.

**Verdict: prior work, part by part.** P1 rests on block hashes as unpredictable public values
[@bentov2016beacon]. P2's height clock in trusted hardware with a monotone checkpoint is in
[@mouallem2026alerting]; its rate floor on headers per unit of trusted local time, with the honest
false-positive trade-off, is in [@bentov2019tesseract] (2019); block-height expiry is standard
[@lightning-bolt2]. P3, a Bitcoin-anchored log that cannot equivocate without a double spend, is
[@tomescu2017catena] (2017). P4 and the "valid only once logged" rule are certificate transparency
[@laurie2013ct] and its hardware use [@apple2024pcc]. Sealed declarations on a blockchain are
[@burford2020trustmachine] (2020). The assembly of these for chip licences was not found. C9 may stand
only as an application, claimed as engineering, as it already says, with each property credited to
its source. The sentence that P3 and P4 "answer two problems flexHEG leaves open" should say they
answer them by carrying over certificate transparency and Catena, not by anything new.

**Confidence and what could overturn it.** High for each part; each passage is explicit. Moderate
that no one has assembled them for chip or export licences. A search of hardware-wallet firmware
(which verifies headers on constrained devices) and of trusted-time designs for TPMs could find the
offline header check on a constrained secure element done, which would matter for C9's L3 prototype,
not for this verdict.

## C10

**The claim in one line.** Superintelligence judged against a named organisation at matched
wall-clock time and budget on a refreshed, regime-held battery across a fraction alpha of decisive
clusters, tracked by the crossover budget t*, the largest tested budget at which the system matches
the comparison at equal compute and money.

**Searches tried (all 2026-11-27).**

1. Web, extended: `AI agents versus human experts crossover time budget "time budget" humans overtake agents longer budgets matched compute cost evaluation`.
2. Web, extended: `benchmark AI system against human team or organization matched budget cost wall-clock institutional baseline superintelligence definition 2026`.
3. Web: `"cost-controlled" OR "budget-matched" evaluation AI agents compared with human teams Pareto cost accuracy "AI agents that matter"`.
4. Web: `Genewein "AGI to ASI" pathways expert collectives definition superintelligence cited 2026 benchmark organisation baseline`
   (forward citations of the AGI-to-ASI report: none found with a budget-matched comparison).
5. Web: `agents humans "returns to time" OR "returns to increasing time budgets" crossover point tracked across model generations human baseline equal cost`.
6. Web: `superforecaster teams versus AI forecasting tournament matched time cost comparison institutional baseline ForecastBench Metaculus pro forecasters`.
7. arXiv API: `abs:"human baseline" AND abs:"time budget"` (0); `abs:"human experts" AND abs:"time budget" AND abs:agents`
   (1, RE-Bench).
8. Full-text searches: RE-Bench for "crossover", "matched" and the budget results; the AGI-to-ASI
   report for "budget", "cost" and "wall-clock"; GDPval for speed and cost; the abstract of a 2026
   cybersecurity-superintelligence paper.

**Closest works found, each opened.**

- **RE-Bench** [@wijk2024rebench]. The crossover is reported as a finding: "the best AI agents
  achieve a score 4× higher than human experts when both are given a total time budget of 2 hours per
  environment. However, humans currently display better returns to increasing time budgets, narrowly
  exceeding the top AI agent scores given an 8-hour budget" (abstract). So t* for those agents lay
  between [2 h](../numbers.md#cog-rebench-budget-short) and [8 h](../numbers.md#cog-rebench-budget-mid),
  as the claims file says. How it differs: individuals, time matched, money not matched, and the
  crossing is a result, not a quantity defined to be tracked.
- **A human-relative horizon** [@robinson2026horizons]. A crossover quantity defined and tracked
  across models: "the longest time horizon over which an LLM exceeds human baseline reliability (or
  equivalently the intersection point of the human and LLM logistic curves)" (TL;DR), computed in
  closed form from the two fitted curves, with the observation that one recent model "has effectively
  caught up with the human slope, at least per the weak METR human-baseline". How it differs: the axis is task length (human completion
  time), not the budget allowed; the baseline is individual engineers; cost is not matched; nothing is
  censored. It is t*'s closest relative found, closer than METR's time horizon, which the claims file
  names.
- **The AGI-to-ASI report** [@genewein2026agiasi]. ASI "reliably outperforms hypothetical groups of
  tens of thousands of well-coordinated expert-level humans that work over a period of 10 years with
  the technology and cultural artifacts available in 2010 on a single problem or task", and "ASI would
  perform the same tasks in less time, say by a factor of 10 or more" (section 3). A full-text search
  finds no budget or compute matching and no battery, as the novelty file says.
- **GDPval** [@patwardhan2025gdpval]. Expert-graded comparisons with professionals, with speed and
  cost ratios: savings are "HT /((MT + RT )/w) times faster and cost savings are HC /((MC + RC )/w)
  times cheaper than human experts" (section on speed and cost, Table 2). How it differs: individuals;
  cost and time reported as ratios after the fact, not matched.
- **Cost-controlled agent evaluation** [@kapoor2024agents]. "Our focus on cost in addition to
  accuracy motivates the new goal of jointly optimizing the two metrics" (abstract). No human or
  organisational baseline.
- **Cybersecurity superintelligence** [@mayoral2026cybersi]. Defined against the best individual,
  "the best human capability in both speed and strategic reasoning" (abstract), with speed and cost
  ratios but no matched comparison.

**Verdict: extends prior work.** A crossover budget between AI and human performance is prior work
in two forms: RE-Bench reports where the advantage flips, and a 2026 essay defines the intersection of
the AI and human curves as a quantity and tracks it across models. What remains not found: (1) time
and money matched together against a named organisation rather than individuals, as part of a
definition; (2) the alpha fraction across decisive clusters on a refreshed, regime-held battery;
(3) t* defined at equal compute and money, as the largest tested crossing, censored and never
extrapolated. The claims file should credit [@robinson2026horizons] as t*'s closest relative and drop
any suggestion that tracking a human-AI crossover is new.

**Confidence and what could overturn it.** Moderate. Frontier labs' internal evaluations against
whole research teams at matched cost would close (1) if published; the claims file already credits one
lab's threshold for one cluster. A short post on a similar crossover framing is referenced by the essay
but was not found and not opened. Forecasting tournaments run AI against expert teams but not at
matched time or cost (searched, not found).

## C11

**The claim in one line.** Closure judged input by input against verifiable human-held gates,
combined for the loop gain as a share-weighted mean K = (lambda / b) * sum_i s_i * e_i (least-closed
input binding under complements, most-closed under substitutes), with narrow optimisers that feed a
covered system's training counted inside its loop.

**Searches tried (all 2026-11-27).**

1. Web: `"operational closure" recursive self-improvement AI development pipeline Burtsev criticality cited`
   (forward citations of the criticality paper: two conference abstracts by the same author, not
   opened).
2. Web: `automation of AI research inputs compute data labour share automated bottleneck complements Baumol intelligence explosion task-based model elasticity of substitution`.
3. Web: `narrow AI optimizer improving training stack counts as self-improvement governance rule "AI improving AI" AlphaEvolve recursive self-improvement policy`.
4. arXiv API: `abs:"operational closure" AND abs:AI` (2, unrelated); `abs:"self-improvement" AND abs:"human approval"`
   (1, unrelated).
5. Full-text reads: the task-based growth model of AI (sections 3 and 4); A Narrow Path's third
   policy; the bare-minimum mitigations paper for "approval"; the research-restrictions paper.

**Closest works found, each opened.**

- **Automation in the idea production function** [@aghion2017ai] (Stanford copy of the NBER paper).
  With a fraction β of research tasks automated and an elasticity of substitution below one, "the CES
  function is bounded by its scarcest argument"; with Cobb-Douglas, "a one-time increase in automation
  will raise the long-run growth rate"; above one, "the CES function asymptotically looks like the
  plentiful factor" (section 3, pages 18 to 19). In the Cobb-Douglas case the explosion condition is a
  threshold on a parameter linear in the automated share of research tasks, γ := σ/(1-α) · β/(1-φ)
  (a displayed equation, transcribed), with "the singularity case" at γ > 1, which "can occur with both α and β less than one" (section 4,
  page 24). How it differs: tasks in an economy's research sector, not gated inputs to the next model;
  automation, not a governance gate. The mathematics is C11(a)'s corrected rule: under Cobb-Douglas
  the closed share enters the exponent additively, weighted by input shares; under complements the
  least-closed input binds; under substitutes the most-closed one.
- **A Narrow Path, policy 3** [@miotti2025narrowpath]. "The direct use of found systems to build new
  found systems, or improve existing found systems, is prohibited" (page 22), and the prohibition
  "notably forbids ... The direct use of any LLM in the training process of another LLM or AI system
  in general, including for generating training data, designing optimization algorithms,
  hyperparameter search" (page 25). How it differs: a ban, not a count inside a measured loop gain;
  any found system, narrow or general. It already treats a system that feeds another's training as
  part of the loop to be controlled, which is C11(b)'s rule.
- **Human approval as the gate** [@clymer2025bareminimum]. It starts from the line that "no AI system
  should be able to improve itself or other AI systems without explicit human approval and assistance.
  However, the criteria for meaningful human approval remain unclear" (abstract). How it differs: no
  decomposition by input and no measure; C11's verifiable gates are one answer to the gap it names.
- **All inputs held together** [@scher2026research]. "a durable halt would address all three so that
  advances in one input do not counteract restrictions on another" (abstract). No closure measure.

**Verdict: extends prior work, narrowly.** The corrected combination rule in C11(a), including its
complements and substitutes cases, is the task-based automation model of [@aghion2017ai] (2017)
applied to the inputs of AI research, and must be credited as such. The narrow-optimiser rule in
C11(b) is A Narrow Path's found-systems prohibition [@miotti2025narrowpath] recast as a count rather
than a ban. What remains not found: closure defined as the share of increments obtained without a
gate the regime can verify, input by input, and the empirical claim that the gain with any subset of
gates is predicted from closures measured one gate at a time. (b) as an experiment, whether a narrow
optimiser raises the measured return only when it targets the training stack, is an empirical test,
not a prior-art question. If E4(d) shows that e_i cannot stand for the automated share (a flag the
claims file already raises), (a) loses even its link to the growth model and becomes framing.

**Confidence and what could overturn it.** Moderate to high on the mapping to the growth model.
Two works were found but not opened: the criticality author's 2026 conference paper on research-agent
ecosystems, and a 2026 essay on compute bottlenecks in a CES model of AI research. Either could
decompose closure by input; both should be opened before L5.

## C12

**The claim in one line.** Seven pathways ranked by how much each shortens T_b or lengthens T_r, how
hard it is to see and how cheaply it can be limited, with self-improvement and undeclared compute tied
first, only Pareto-ordered pairs fixed by evidence, and a response class per rank.

**Searches tried (all 2026-11-27).**

1. Web: `2026 comparison of strategic visions for governing the transition to superintelligence`.
2. Web: `Modeling Transformative AI Risks MTAIR paths to high-level machine intelligence model arXiv 2022`.
3. Web: `iaps.ai "Strategic Visions in AI Governance" Delaney Kostylew Guest Wildeford`.
4. Web: `"acquisition path analysis" artificial intelligence compute governance pathways superintelligence verification`.
5. Web, extended: `ranking routes to dangerous AI capability for treaty restriction self-improvement smuggled compute distillation distributed training comparison detectability cost of restriction`
   (the tool declined the query as written and returned verification papers instead).
6. arXiv API: `abs:"pathways" AND abs:superintelligence` (7 results; three opened, below).
7. Full-text reads: the MTAIR summary report, chapter 3; the strategic-visions report, section D; the
   AGI-to-ASI report, section 5; the ASI pathways model; the adversarial-distillation report, section
   I; a 2026 position paper on control and knowledge boundaries (abstract).

The two works the pathways chapter found but did not open are opened here first: the 2022 model of
paths to high-level machine intelligence is the MTAIR report [@clarke2022mtair], and the 2026
comparison of strategic visions is [@delaney2026strategicvisions].

**Closest works found, each opened.**

- **MTAIR, paths to high-level machine intelligence** [@clarke2022mtair]. "several possible
  approaches to HLMI are modeled separately, and the date for the arrival of HLMI is taken as the
  earliest date that one of these approaches succeeds" (section 3.2.1), over evolutionary
  algorithms, current deep learning plus business as usual, hybrid statistical-symbolic AI,
  cognitive-science approaches, whole brain emulation and neuromorphic AGI; separate modules compare
  software-mediated and hardware-mediated intelligence explosions (section 4). How it differs:
  technical paradigms compared by arrival time, not loops and supply routes compared by breakout time,
  visibility and cost of a limit; no protocol.
- **Strategic visions** [@delaney2026strategicvisions]. It compares nine visions and "eight such
  cruxes for choosing a strategic vision where informed AI researchers and policy analysts routinely
  disagree" (section D). How it differs: it compares governance strategies, not pathways.
- **The AGI-to-ASI report** [@genewein2026agiasi]. Its four pathways "are not mutually exclusive",
  and "only the first one, scaling, has historic data available to extrapolate from" (appendix A). It
  tabulates how each friction would or would not affect each pathway. No ranking, as the pathways
  chapter said, now confirmed in the full text.
- **The ASI pathways model** [@barrett2016asipath]. "a graphical model of major pathways to ASI
  catastrophe, focusing on ASI created via recursive self-improvement", using "fault trees and
  influence diagrams in order to depict combinations of events and conditions that could lead to AI
  catastrophe, as well as intervention options" (abstract). How it differs: pathways to catastrophe
  through one loop, with interventions; no supply routes, no ranking by breakout time or visibility.
  It is the risk-analysis precedent the L1 plan asked for.
- **Routes for a party short of compute** [@remler2026distillation]. "The CCP and Chinese developers
  have sought to overcome these restrictions along three axes. The first is to close the computing gap
  through smuggling chips, remotely accessing foreign hardware, and producing indigenous chips. The
  second is industrial espionage. The third is adversarial distillation" (section I). Unranked.
- **Undeclared compute as a route into breakout** [@fithian2026hardwired]. Dark compute is a term in
  every state's covert evasion and breakout ledgers, "by definition ... ungoverned under the treaty"
  (section 3.2.3). This already treats undeclared compute as a source of breakout capacity, not only a
  failure of verification.
- A 2026 position paper decomposes an agent's impact into discovery, know-how and control pathways
  and argues for restricting control, not ranking capabilities (abstract read); not closer, not cited.

**Verdict: extends prior work, as an application.** The method is acquisition path analysis, as the
claims file concedes; comparing paths to advanced AI by arrival time [@clarke2022mtair] and modelling
pathways to ASI with fault trees and interventions [@barrett2016asipath] are older. C12(b), undeclared
compute and distillation as pathways rather than failure modes, is prior work in substance: the
hardwired-pause ledgers count dark compute as breakout capacity [@fithian2026hardwired], and
distillation and smuggling are named routes [@remler2026distillation]. C12(c) is method hygiene, not
a contribution. What remains not found is the ranking itself: these seven routes, loops and supply and
transfer routes together, each tied to a side of D4, a channel and a cost, with ties. That is a
judgement applied with a known method. It should be claimed as an application of acquisition path
analysis to AI, with (b) credited, not as a methodological contribution.

**Confidence and what could overturn it.** Moderate. Bostrom's 2014 book has a chapter on paths to
superintelligence that compares routes (machine intelligence, emulation, biological cognition,
interfaces, organisations); it was not opened (no open copy) and is not cited, and a reader should
check it. Internal threat models at frontier developers, and any IAEA state-level analysis carried over
to AI, could hold a closer ranking; none was found.

## Summary

| Claim | Verdict | Closest work |
|---|---|---|
| C7 | Prior work: (a) is the hardwired-pause fleet threshold solved for the share with the horizon set to m * T_r; (b)(i) is the cartel reporting-reward condition. Cut as a contribution; keep as an application of C1 | [@fithian2026hardwired]; [@aubert2006leniency]; [@whitehouse2015jcpoaparameters] |
| C8 | Extends prior work, narrower than stated: the aggregate floor with a time axis and the pool counted against it are prior work; the bound at the highest utilisation and per-channel crossing years remain | [@fithian2026hardwired]; [@koopmanschap2026gpu]; [@iaea-glossary-2022] |
| C9 | Prior work, part by part (rate floor, height clock in trusted hardware, Bitcoin-anchored non-equivocating log, valid only once logged, sealed treaty declarations); the assembly for chip licences may stand only as an application | [@bentov2019tesseract]; [@mouallem2026alerting]; [@tomescu2017catena]; [@laurie2013ct]; [@burford2020trustmachine] |
| C10 | Extends prior work: the human-AI crossover is reported and tracked already; matched time and money against an organisation, the alpha fraction and the censored t* remain | [@wijk2024rebench]; [@robinson2026horizons]; [@genewein2026agiasi] |
| C11 | Extends prior work, narrowly: the combination rule is the task-based automation model; the narrow-optimiser rule is A Narrow Path's; gated closure measured one gate at a time remains | [@aghion2017ai]; [@miotti2025narrowpath]; [@clymer2025bareminimum] |
| C12 | Extends prior work, as an application of acquisition path analysis; (b) is prior work; the specific ranking remains | [@clarke2022mtair]; [@barrett2016asipath]; [@fithian2026hardwired]; [@remler2026distillation] |

## New sources

```toml
[source.williams2026breakout]
type = "essay"
title = "AI breakout time: a mechanism for an enforceable AI pause"
authors = "Connor Williams"
year = 2026
url = "https://www.greaterwrong.com/posts/BWDdSLbntJeQtZQxb/ai-breakout-time-a-mechanism-for-an-enforceable-ai-pause"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.aubert2006leniency]
type = "peer-reviewed"
title = "The impact of leniency and whistle-blowing programs on cartels"
authors = "Cécile Aubert, Patrick Rey, William E. Kovacic"
year = 2006
doi = "10.1016/j.ijindorg.2006.04.002"
url = "https://publications.ut-capitole.fr/1898/1/leniency.pdf"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"
# The opened copy is the working-paper version of 21 June 2005; sections and lemma as cited.

[source.shinohara2025coalitionproof]
type = "peer-reviewed"
title = "Coalition-proof stability of international environmental agreements"
authors = "Ryusuke Shinohara"
year = 2025
doi = "10.1007/s10018-024-00426-z"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"
# Abstract only (RePEc listing); the full text was not read.

[source.whitehouse2015jcpoaparameters]
type = "official-docs"
title = "Parameters for a Joint Comprehensive Plan of Action Regarding the Islamic Republic of Iran's Nuclear Program"
authors = "The White House"
year = 2015
url = "https://obamawhitehouse.archives.gov/realitycheck/node/329396"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.mouallem2026alerting]
type = "preprint"
title = "Resilient Alerting Protocols for Blockchains"
authors = "Marwa Mouallem, Lorenz Breidenbach, Ittay Eyal, Ari Juels"
year = 2026
arxiv = "2602.10892"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.tomescu2017catena]
type = "peer-reviewed"
title = "Catena: Efficient Non-equivocation via Bitcoin"
authors = "Alin Tomescu, Srinivas Devadas"
year = 2017
doi = "10.1109/SP.2017.19"
url = "https://people.csail.mit.edu/devadas/pubs/catena.pdf"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.bentov2019tesseract]
type = "peer-reviewed"
title = "Tesseract: Real-Time Cryptocurrency Exchange Using Trusted Hardware"
authors = "Iddo Bentov, Yan Ji, Fan Zhang, Lorenz Breidenbach, Philip Daian, Ari Juels"
year = 2019
doi = "10.1145/3319535.3363221"
url = "https://par.nsf.gov/servlets/purl/10153194"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.bentov2016beacon]
type = "preprint"
title = "Bitcoin Beacon"
authors = "Iddo Bentov, Ariel Gabizon, David Zuckerman"
year = 2016
arxiv = "1605.04559"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.regnath2020blockchaintime]
type = "peer-reviewed"
title = "Blockchain, what time is it? Trustless Datetime Synchronization for IoT"
authors = "Emanuel Regnath, Nitin Shivaraman, Shanker Shreejith, Arvind Easwaran, Sebastian Steinhorst"
year = 2020
doi = "10.1109/COINS49042.2020.9191420"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.apple2024pcc]
type = "vendor"
title = "Private Cloud Compute: A new frontier for AI privacy in the cloud"
authors = "Apple Security Engineering and Architecture"
year = 2024
url = "https://security.apple.com/blog/private-cloud-compute/"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.lightning-bolt2]
type = "spec"
title = "BOLT #2: Peer Protocol for Channel Management"
authors = "Lightning Network specification authors"
undated = true
url = "https://github.com/lightning/bolts/blob/master/02-peer-protocol.md"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.burford2020trustmachine]
type = "report"
title = "The trust machine: Blockchain in nuclear disarmament and arms control verification"
authors = "Lyndon Burford (Centre for Science and Security Studies, King's College London)"
year = 2020
url = "https://www.kcl.ac.uk/csss/assets/the-trust-machine-report.pdf"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.robinson2026horizons]
type = "essay"
title = "Is METR Underestimating LLM Time Horizons?"
authors = "Andreas Robinson"
year = 2026
url = "https://www.lesswrong.com/posts/kNHxuusznCR3rhqkf/is-metr-underestimating-llm-time-horizons"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.kapoor2024agents]
type = "preprint"
title = "AI Agents That Matter"
authors = "Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan"
year = 2024
arxiv = "2407.01502"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"
# Abstract only.

[source.mayoral2026cybersi]
type = "preprint"
title = "Towards Cybersecurity Superintelligence: from AI-guided humans to human-guided AI"
authors = "Víctor Mayoral-Vilches, Stefan Rass, Martin Pinzger, et al."
year = 2026
arxiv = "2601.14614"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"
# Abstract only.

[source.clarke2022mtair]
type = "preprint"
title = "Modeling Transformative AI Risks (MTAIR) Project: Summary Report"
authors = "Sam Clarke, Ben Cottier, Aryeh Englander, Daniel Eth, David Manheim, Samuel Dylan Martin, Issa Rice"
year = 2022
arxiv = "2206.09360"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.delaney2026strategicvisions]
type = "report"
title = "Strategic Visions in AI Governance: Mapping Pathways to Victory"
authors = "Oscar Delaney, Maria Kostylew, Oliver Guest, Peter Wildeford (IAPS)"
year = 2026
url = "https://www.iaps.ai/research/strategic-visions-in-ai-governance"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"

[source.barrett2016asipath]
type = "peer-reviewed"
title = "A model of pathways to artificial superintelligence catastrophe for risk and decision analysis"
authors = "Anthony M. Barrett, Seth D. Baum"
year = 2016
doi = "10.1080/0952813X.2016.1186228"
arxiv = "1607.07730"
opened = "2026-11-27"
found_in = "research/verification/l1-prior-art-c7-c12.md"
```
