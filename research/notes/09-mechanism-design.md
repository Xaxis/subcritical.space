# Survey track 09: mechanism design (inspection games, coalitions, withdrawal, races, reporting)

- Track: 09, mechanism design. Feeds the memo's "Defection" bullet, D3/D4, the verification channels
  (including rewarded whistleblowing), research/05-formal.md and experiment E6.
- Date: 2026-11-27. Every source below was opened on this date; where only an abstract or a record
  page loaded, the entry says so.
- Scope: inspection games and inspector leadership; coalition-proof and strong equilibria; treaty
  participation and self-enforcing agreements; withdrawal clauses and the NPT precedent; arms
  control verification games; AI race and AI agreement models (2016 to 2026); whistleblower
  rewards as a detection channel.

## Summary

1. **Compliance can be made the unique equilibrium, but only with commitment.** In the
   simultaneous inspection game the inspectee always violates with positive probability
   (avenhaus2002inspection, eq 3.4). When the inspector announces and commits to a randomised
   inspection probability (inspector leadership, Maschler 1966), the inspectee acts legally with
   certainty and the inspector's payoff rises (Theorem 5.1; vonstengel2016recursive Theorem 5).
   Commitment needs a verifiable randomiser ("roulette wheel"). The memo's random challenge
   inspections should be specified as a published probability drawn from a public random beacon.
2. **Deterrence does not need near-certain detection.** Coe and Vaynman (Corollary 2) show
   monitoring "never need be perfect"; Gan's AI pause model deters with a 32% chance of detection
   within the response window. The penalty condition (my derivation from Avenhaus et al.'s payoffs,
   eq 3.2) is: legal behaviour is a best response iff non-detection beta <= (b - h alpha)/(1 + b)
   (gain normalised to 1, penalty b, false alarm cost h).
3. **The closest prior art for the memo's Defection bullet is from October and November 2026.**
   Gan (arXiv 2611.04272) solves an AI pause game with Poisson detection inside a response window
   and shows the window shrinks as compute grows ("agreements have a clock"). The Berkeley
   hardwired-pause working paper defines per-state breakout fleet thresholds
   F_B = rho_B C_B / (T_B U_F), mentions per-coalition allowances, and picks T_B = 2 years as the
   time before "the rest of the world could react". MIRI's draft agreement already has a 12-month
   withdrawal notice with chip clusters removed during the notice. D4's "T_b against T_r" and the
   coalition threshold are therefore extensions of prior work at best, not new.
4. **Contradicts the memo: channels cannot be multiplied as if independent.** The memo computes
   one channel's miss chance and says that "is why the design needs several", which presumes that
   adding channels multiplies the miss chance down. That holds only for independent channels that
   the evader cannot choose between. In inspection games the violator picks the violation
   procedure that maximises non-detection; Baker et al.'s six-layer paper argues a regime is as
   strong as its weakest subgoal. A mature multi-channel system (US corporate fraud
   oversight: auditors, analysts, media, employees, regulators) detects about 31% of frauds
   (dyck2017pervasive). The miss probability must be a maximum over evasion strategies.
5. **Contradicts the memo: transparency has costs.** Coe and Vaynman: arms control is rare
   because monitoring that assures compliance also exposes security information. Armstrong et al.
   and Emery-Xu et al.: revealing capabilities can raise race risk (except under some conditions).
6. **Withdrawal: notice alone did not hold.** The DPRK gave notice in March 1993, suspended it
   one day before it took effect, and in January 2003 claimed only one day remained. A notice
   period works only if assets acquired under the regime are frozen or removed during it (EU 2005
   NPT proposals; MIRI Art XV). Rosendorff and Milner show that exit that is too costly breaks
   regimes. Under D4 itself, if every holding is non-weapons-grade at the moment of exit, notice is
   not needed for detection; the binding case is a breakout time that shrank during membership.
7. **Without sanctions on outsiders, stable coalitions are small** (Nordhaus: "no stable
   coalitions other than those with minimal abatement"; two or three countries in the symmetric
   case). A protocol that "binds states that join" needs a club penalty on non-members.
8. **A known threshold turns a dilemma into coordination.** In Barrett and Dannenberg's
   experiment, a known catastrophe threshold was avoided by 8 of 10 groups; with the threshold's
   location uncertain, catastrophe was certain in 9 of 10. This supports an operational line (D4),
   and warns that a disputed T_b estimate acts like an uncertain threshold.
9. **Rewards, not protections, move insiders.** With qui tam rewards (15 to 30%), employees
   revealed 46.7% of healthcare frauds against 16.3% elsewhere; SOX protections alone did not raise
   employee detection. The SEC has paid more than $2.2 billion to 444 whistleblowers since 2011.

## Sources

Grouped by theme. Page numbers are the opened version's.

### Inspection games

### avenhaus2002inspection

"Inspection Games". Rudolf Avenhaus, Bernhard von Stengel, Shmuel Zamir. Handbook of Game Theory
with Economic Applications, vol. 3, ch. 51, pp. 1947-1987, eds. Aumann and Hart, Elsevier, 2002.
DOI 10.1016/S1574-0005(02)03014-X. Opened: the authors' preprint dated 5 February 2001 (full
text, from von Stengel's LSE page) and the RePEc record. Page numbers are the preprint's.

- Definition (p1): "An inspection game is a mathematical model of a situation where an inspector
  verifies that another party, called inspectee, adheres to certain legal rules." Unlike search
  games, inspection games are "fundamentally asymmetrical" (p2).
- General game (Sec 3.1, Fig 3.1). Payoffs (inspector, inspectee): legal and no alarm (0, 0);
  undetected violation (-1, +1); detected violation (-a, -b); false alarm (-e, -h), with
  0 < e < 1, 0 < a < 1, 0 < h < b (3.1). Payoffs (3.2):
  I = (1-q)(-e alpha) + q(-a - (1-a) beta), V = (1-q)(-h alpha) + q(-b + (1+b) beta), where alpha
  is the false alarm probability, beta the non-detection probability, q the violation probability.
- p12: "Usually, there is no equilibrium in which the inspectee acts with certainty legally
  (q* = 0)". If q* = 0 the inspector sets alpha = 0, and then the inspectee's condition
  -b + (1+b) beta <= 0 "is usually not possible with a test that has false alarm probability
  zero". Hence 0 < q* < 1 (3.4) and indifference (3.5): -h alpha* = -b + (1+b) beta(alpha*).
- Theorem 3.1 (p13): with the zero-sum "non-detection game" G_alpha having value beta(alpha)
  (beta(0) = 1, beta(1) = 0, convex), the equilibrium false alarm probability solves (3.8)
  -h alpha* = -b + (1+b) beta(alpha*) and the violation probability is (3.9)
  q* = e / (e - (1-a) beta'(alpha*)). The inspector plays a minmax test against the worst
  violation procedure omega: beta(alpha) = min_delta max_omega beta(delta, omega) (3.6).
- Material accountancy (Theorem 3.2, p17): the strategic diverter spreads diversion as
  mu* = Sigma 1 mu / (1' Sigma 1); detection probability 1 - beta* = Phi(mu / sqrt(1' Sigma 1) -
  q_{1-alpha}) (3.16); the best test uses only the overall balance. p35: "the subdivision of a
  plant into small areas with intermediate balances has no effect on the overall detection
  probability if the violator acts strategically". p36: deciding only at the end "may be too long
  if detection time becomes a criterion".
- Dresher game (Sec 4.1): n stages, m inspections, at most one violation, zero-sum.
  I(n, n) = 0, I(n, 0) = -1 (4.1); recursion (4.3)
  I(n, m) = [I(n-1, m) + I(n-1, m-1)] / [I(n-1, m) + 2 - I(n-1, m-1)]; closed form
  I(n, m) = -C(n-1, m) / sum_{i=0..m} C(n, i). Non-zero-sum (Theorem 4.1):
  V(n, m) = C(n-1, m) / sum_{i=0..m} C(n, i) b^(m-i) (4.5).
- Theorem 4.2 (von Stengel 1991): up to k violations; first-stage inspection probability
  p = s(n-1, m-1)/s(n, m), independent of k, so "the inspector need not know the value of k in
  order to play optimally".
- Timeliness games (Sec 4.2): payoff is time from violation to detection. Observable inspections:
  periodic schedule, expected delay 1/m of the interval (1/2 for m = 2). Unobservable, m = 2
  (Theorem 4.3, Diamond 1982): inspect at t in [0, 1 - 1/e] with density 1/(1 - t); value 1/e
  (about 0.368), against 1/2 if observable. For large m the value approaches 1/(2m - 4/3) from
  above.
- Leadership (Sec 5, p29): "it would be more appropriate to use the term commitment power"; "an
  inspector can credibly announce his strategy and stick to it, whereas the inspectee cannot do so
  if he intends to act illegally". p31: "In a zero-sum game which has a value, leadership has no
  effect." Fig 5.3 example (n = 2, m = 1, a = 1/2, b = 1): simultaneous play has the inspectee
  violate with probability 2/3; under leadership the inspector announces p* = 1/3 and the inspectee
  acts legally; the inspector's payoff rises from -2/3 to -1/3. Maschler: announce slightly above
  p*, "on the safe side, which should also be recommended in practice" (p33). Avenhaus, Okada and
  Zamir (1991), with the inspectee's gain unknown: announce a higher p that "just about forces the
  inspectee to act legally for any value".
- Theorem 5.1 (p34): in the leadership version the inspector announces alpha* of (3.8); the
  inspectee violates if alpha < alpha* and is legal if alpha >= alpha*. "Inspector leadership
  serves as deterrence from illegal behavior. The optimal false alarm probability alpha* of the
  inspector stays the same. His payoff is larger in the leadership game."
- Caution (p35-36): "Higher-level models describing the decisions of the states, like whether to
  cheat or not, and in the extreme whether 'to go to war' or not, should in our view not be
  blended with an inspection game." Penalty sizes are "usually not known to the analyst", but "the
  signs of these payoffs often suffice". Open question: "In the case of sequential games, is legal
  behavior again an equilibrium strategy of the inspectee?"
- Bears on: Defection (compliance as best response), random challenge inspections, D4's T_r
  (timeliness), multi-channel detection (strategic omega), distributed training (subdivision).

### vonstengel2016recursive

"Recursive Inspection Games". Bernhard von Stengel. Mathematics of Operations Research 41(3):935-952,
2016. DOI 10.1287/moor.2015.0762; arXiv 1412.0129 (v2, 7 February 2016). Full text opened.

- Abstract: the most valuable reward "may be the completion of a sequence of thefts of nuclear
  material needed to build a nuclear bomb"; the inspectee observes the inspector, who learns of a
  violation only when inspecting. The inspector's equilibrium strategy depends only on remaining
  periods and inspections, so the recursion holds without the inspector knowing past violations.
- Proposition 1 (p18-19), general 2x2 leadership: row (leader) payoffs A, B, C, D and column a, b,
  c, d with A < C, B > D, a > b, c < d (47); p* = (d - c)/(a - b + d - c) (48); if
  p*A + (1-p*)C > p*B + (1-p*)D (49), the simultaneous game has a unique mixed equilibrium with
  leader payoff N = (BC - AD)/(B - D + C - A); under leadership the follower plays q = 0 for
  p >= p* and the leader gets L = p*A + (1-p*)C > N; the follower's payoff is unchanged.
- Theorem 5 (p20-21): the inspector commits to the same p* as in simultaneous play; "For m > 0,
  the inspectee always acts legally, and for m = 0 he violates in each remaining time period";
  the inspector's cost falls by the factor s_hat(n, m)/s(n, m).
- Commitment device (p18): a "roulette wheel" or other randomisation device "that decides with a
  verifiable probability in each time period".
- Bears on: verifiable randomness for challenge inspections (a public beacon such as a Bitcoin
  block hash fits); the end-game result (m = 0 means violation) argues against a regime with a
  known last licence period.

### dresher1962sampling

"A Sampling Inspection Problem in Arms Control Agreements: A Game-Theoretic Analysis". Melvin
Dresher. RAND RM-2972-ARPA, 1962. URL https://www.rand.org/pubs/research_memoranda/RM2972.html.
Opened: the RAND record and abstract only. The PDF link returned an HTML page; the full text was
not read.

- Abstract (paraphrase): the population being sampled can be manipulated to lower the chance of
  detecting a violation; a game in which an inspector may examine a fixed number of items or
  natural events (factory output, seismic events under a test ban) in a fixed period; optimal
  sampling given the number of inspections and the population size.
- The model and its value formula are cited here as restated in avenhaus2002inspection Sec 4.1.
- Bears on: the origin of the recursive inspection game (limited challenge inspections).

### maschler1966price

"A price leadership method for solving the inspector's non-constant-sum game". Michael Maschler.
Naval Research Logistics Quarterly 13(1):11-33, March 1966. DOI 10.1002/nav.3800130103. Opened: the
abstract from Crossref metadata (the publisher page returned 403).

- Abstract: "An inspector's game is a non-constant-sum two-person game in which one player has
  promised to perform a certain duty and the other player is allowed to inspect and verify
  occasionally that the duty has indeed been performed." The solution assumes "the inspector can
  announce his mixed strategy in advance, if he so wishes, whereas the other player, who has
  already given his promise, cannot threaten by explicitly saying that he will not keep his word."
- Bears on: the origin of inspector leadership.

### canty2001timely

"Timely inspection and deterrence". Morton J. Canty, Daniel Rothenstein, Rudolf Avenhaus. European
Journal of Operational Research 131(1):208-223, 2001. DOI 10.1016/S0377-2217(00)00082-5. Opened:
the abstract only (IAOR record); full text not read.

- Abstract (paraphrase): deterrence is the main goal of routine inspections; first treatment of
  inspection problems with a "critical time", the maximum window within which an illegal activity
  must be detected; a two-person game over a fixed interval with k inspections, at most one
  illegal act, errors of both kinds; derives conditions under which deterring inspection
  strategies exist.
- Bears on: the closest classical analogue of D4 (detection within a critical time). Its
  conditions should be read before 05-formal is written.

### avenhaus1996compliance

"Compliance Quantified: An Introduction to Data Verification". Rudolf Avenhaus, Morton John Canty.
Cambridge University Press, 1996. ISBN 9780521553667. Opened: the RePEc record and the Cambridge Core
chapter listing only.

- Description: treaty verification needs a mathematical model to show it is "efficient,
  effective, and impartial"; uses statistics and non-cooperative game theory; supports
  "guaranteed probability of detection, inspection timeliness, and deterrence of illegal
  activity". The book's contents were not read.

### Coalitions and treaty participation

### bernheim1987coalition

"Coalition-Proof Nash Equilibria I. Concepts". B. Douglas Bernheim, Bezalel Peleg, Michael D.
Whinston. Journal of Economic Theory 42(1):1-12, 1987. DOI 10.1016/0022-0531(87)90099-8. Opened: the
abstract (author page) only.

- Abstract: in noncooperative environments "players can freely discuss their strategies, but
  cannot make binding commitments"; the Nash best-response property is necessary but not
  sufficient for self-enforceability, because coalitions can arrange mutually beneficial
  deviations; they "label the class of efficient self-enforcing agreements 'coalition-proof.'"
- The formal definition is recorded from ali2019coalitions below.
- Bears on: the coalition threshold; a compliance equilibrium for n states must survive
  deviations by subcoalitions, not only by single states.

### ali2019coalitions

"Coalitions in Repeated Games". S. Nageeb Ali, Ce Liu. arXiv 1906.00280 (v4). Opened full text; used
only for its restatement of the BPW definition.

- Definition 10 (appendix, p62-63): "(a) In a single player game G, action a*_i is a
  coalition-proof Nash Equilibrium (CPNE) if and only if a*_i maximizes v_i(a_i). (b) ... (i) For
  any game G with n players, a* is self-enforcing if, for all proper sub-coalitions C, a*_C is a
  coalition-proof Nash equilibrium in the game G|a*_{-C}. (ii) ... a* is a coalition-proof Nash
  equilibrium if it is self-enforcing and if there does not exist another self-enforcing action
  profile a such that v_i(a) > v_i(a*) for all i."

### barrett1994self

"Self-Enforcing International Environmental Agreements". Scott Barrett. Oxford Economic Papers 46
(Supplement 1):878-894, 1994. DOI 10.1093/oep/46.Supplement_1.878. Opened: the RePEc abstract only;
the publisher page was behind a bot check and the full text was not read.

- Abstract (paraphrase): no third party can enforce IEAs; two models (signatories, terms and
  non-signatories' behaviour determined jointly; and an infinitely repeated, renegotiation-proof
  game); both suggest that when many countries share a resource, self-enforcing IEAs can do little
  better than the noncooperative outcome.
- Bears on: who the protocol binds; the "small coalition paradox" (see nordhaus2015climate).

### nordhaus2015climate

"Climate Clubs: Overcoming Free-riding in International Climate Policy". William Nordhaus. American
Economic Review 105(4):1339-1370, 2015. DOI 10.1257/aer.15000001. Full text opened.

- Abstract: "without sanctions against non-participants there are no stable coalitions other than
  those with minimal abatement. By contrast, a regime with small trade penalties on
  non-participants, a Climate Club, can induce a large stable coalition with high levels of
  abatement."
- p1344-45, the "small coalition paradox": coalitions "tend to be either small or shallow". In
  the identical-country case "The only stable coalitions have two or three countries", whatever
  the number of countries; "bottom-up coalitions perform only slightly better than the
  noncooperative equilibrium". Barrett's self-enforcing treaties combine individual and collective
  rationality; the treaties that succeed "include external penalties".
- p1346, stability concept: "a coalition is stable if no group (sub-coalition) among the
  countries can improve its welfare by changing its status", i.e. strong equilibrium (Aumann 1959;
  see BPW 1987), called "coalition Nash equilibrium". He prefers one-shot stability to
  "sophisticated and fragile repeated-game strategies". "external sanctions are necessary to
  promote participation in effective agreements to provide global public goods."
- Internal penalties are hard: "it is difficult to design an incentive-compatible internal
  sanction against defectors".
- Results (C-DICE, 15 regions; target carbon prices $12.5, 25, 50, 100 per tCO2; tariffs 0 to
  10%): "virtually every regime produces a stable coalition" (6 unstable of 44); "No country joins
  the Climate Club without trade sanctions (i.e., at a zero tariff rate)"; the $50 target is
  "almost reached with a 5 percent tariff"; at $100 most countries accept the penalty.
- Bears on: "a major power that stays out"; chip and cloud denial to non-members as the club
  penalty; the stability concept for the protocol (strong or coalition-proof).

### barrett2012climate

"Climate negotiations under scientific uncertainty". Scott Barrett, Astrid Dannenberg. PNAS
109(43):17372-17376, 2012. DOI 10.1073/pnas.1208417109 (PMC3491499). Opened: abstract (Crossref)
and full text (PMC).

- Abstract: "the fear of crossing a dangerous threshold can turn climate negotiations into a
  coordination game, making collective action to avoid a dangerous threshold virtually assured.
  These results are robust to uncertainty about the impact of crossing a threshold, but
  uncertainty about the location of the threshold turns the game back into a prisoners' dilemma,
  causing cooperation to collapse."
- Design: 10 players per group, 10 groups per treatment, 400 participants; up to 10 chips at
  EUR 0.10 and 10 at EUR 1.00; each chip gives every group member EUR 0.05; threshold 150 chips;
  loss EUR 15 (Certainty), U[10, 20] (Impact uncertainty), threshold U[100, 200] (Threshold
  uncertainty).
- Results: catastrophe avoided in 8 of 10 groups (Certainty) and 10 of 10 (Impact uncertainty);
  under Threshold uncertainty catastrophe was certain in 9 of 10 groups. Mean group contributions
  150.9, 155.5, 77.2 and 79.9 chips (Certainty, Impact, Threshold, both).
- Theory: with a known threshold both "abate nothing" and avoiding the threshold are symmetric
  Nash equilibria and avoiding is preferred by all; threshold uncertainty restores free riding.
- Bears on: D4 directly. A known, verifiable line makes compliance a coordination equilibrium. A
  line whose location is disputed (an uncertain T_b) behaves like threshold uncertainty.

### Withdrawal

### helfer2005exiting

"Exiting Treaties". Laurence R. Helfer. Virginia Law Review 91:1579-1648, 2005. URL
https://virginialawreview.org/articles/exiting-treaties/. Full text opened (PDF hosted at
juscogens.net).

- Data (p1601-1606): "1547 denunciations and withdrawals" from multilateral treaties notified
  1945 to 2004, against "ratifications (32,021)"; of 5416 multilateral agreements concluded after
  1945, "191, or 3.5%, have been denounced at least once". The exit rate relative to cumulative
  ratifications "held relatively constant or declined only slightly over the last fifty years".
- p1597-98: "the most common denunciation clause permits withdrawal only if the state provides
  advance notice of its decision to withdraw, sometimes with the additional condition that the
  treaty has been in force for a specified number of years." Geneva Conventions common Art 63: one
  year, and not until peace if the denouncing state is at war (fn 50). Arms control treaties more
  often require explanations and restrict withdrawal to facts the denouncing state judges itself
  (ABM Treaty Art XV).
- p1625, temporal opportunism: arises "where the parties' performance is non-synchronous and one
  party withdraws from the treaty after its partners have performed but before its own performance
  has been completed". NPT example, quoting the New York Times: the treaty "permits countries to
  build nuclear programs for peaceful purposes and then, with 90 days notice, pull out of the
  treaty. That means [Iran] can develop facilities under the treaty, then shift them to weapons
  programs." Remedy precedent: investment treaties "bar denunciation for ten years after the treaty
  enters into force" and keep protecting assets already invested.
- p1584: exit clauses "function as an insurance policy" that "enables states to negotiate more
  expansive or deeper substantive treaty commitments ex ante", while raising "troubling
  opportunities for strategic action ex post". p1648: notice and minimum-duration rules "create
  an initial window of cooperation, force governments to think twice ... and provide a cooling off
  period".
- p1619: exit does not shield high-stakes defectors from outside sanctions; ElBaradei: a
  withdrawing state is not "off the hook of the Security Council".
- Bears on: withdrawal design. The AI analogue of temporal opportunism is accumulating licensed
  chips, data centres and know-how inside the regime, then exiting.

### rosendorff2001optimal

"The Optimal Design of International Trade Institutions: Uncertainty and Escape". B. Peter
Rosendorff, Helen V. Milner. International Organization 55(4):829-857, 2001. DOI
10.1162/002081801317193619. Full text opened.

- p831: an escape clause "increases institutional effectiveness whenever there is domestic
  political uncertainty"; escape clauses "must impose some kind of cost on their use ... or else
  they will invoke it all the time"; paying it "signals their intention to comply in the future".
- Proposition 1 (p840-41): escape-clause strategies form a Nash equilibrium; whereas the plain
  Prisoners' Dilemma needs a high enough discount factor, "cooperation can be sustained for any
  value of the discount factor as long as k <= K", where K makes a player indifferent between
  escaping and defecting for good. If k > K the system "breaks down with probability 1".
- Proposition 2: symmetric countries agree on k* = argmax_k (V_C + V*_C) if k* <= K, otherwise K.
  "the penalty associated with the escape clause is self-enforcing".
- Bears on: a lawful, costly, visible exit can stabilise a regime; an exit made too costly breaks
  it. This cuts against the instinct to make withdrawal as slow as possible.

### koremenos2016continent

"The Continent of International Law: Explaining Agreement Design". Barbara Koremenos. Cambridge
University Press, 2016. DOI 10.1017/CBO9781316415832; ISBN 9781107124233. Opened: the Cambridge Core
page for ch 5, "Escape clauses and withdrawal clauses" (pp 124-157), only.

- In the COIL sample "70%" of agreements have withdrawal provisions and "19%" escape clauses; 13
  agreements (about 6%) have neither, nor a limited duration. "Nuanced design provisions are a
  necessary condition for international law to be an equilibrium institution." Notice and waiting
  period lengths are tabulated in the chapter, which I did not read.

### eu2005nptwithdrawal

"Withdrawal from the Treaty on the Non-Proliferation of Nuclear Weapons: European Union common
approach". Working paper submitted by Luxembourg on behalf of the EU, NPT/CONF.2005/WP.32, 10 May
2005. URL https://digitallibrary.un.org/record/548700/files/NPT_CONF.2005_WP.32-EN.pdf. Full text
opened.

- Quotes NPT Article X(1): "Each Party shall in exercising its national sovereignty have the right
  to withdraw from the Treaty if it decides that extraordinary events, related to the subject
  matter of this Treaty, have jeopardized the supreme interests of its country. It shall give
  notice of such withdrawal to all other Parties to the Treaty and to the United Nations Security
  Council three months in advance."
- Para 3(c): the three months start from the note verbale; "Any other declarations, public
  statements or letters of intention are in no way valid to shorten this period."
- Para 4: a notice is "of immediate relevance to the Security Council", which should consider "a
  special IAEA inspection of the notifying party".
- Para 5: liability for prior violations survives; "the premeditation and the preparation of the
  withdrawal decision with a view to conducting a military nuclear programme constitute a
  violation"; materials and facilities developed for peaceful purposes "remain ... restricted to
  peaceful uses only" under safeguards; items from third countries "must be frozen, with a view to
  having them dismantled and/or returned", with steps "as soon as a withdrawal notification is
  issued"; safeguards to continue "during an indefinite period following a withdrawal".
- Bears on: what a notice period is for (inspection and freezing), and obligations that survive
  exit.

### kirgis2003dprk

"North Korea's Withdrawal from the Nuclear Nonproliferation Treaty". Frederic L. Kirgis. ASIL
Insights 8(2), 24 January 2003. URL https://www.asil.org/insights/volume-8-issue-2-2/. Opened.

- DPRK announced withdrawal on 10 January 2003, "effective immediately". The notice requirement
  is "couched in terms of a promise to give three months' notice", not stated as a condition of
  effectiveness; whether withdrawal waits three months is "not certain". The Security Council
  could find the withdrawal plus the expulsion of inspectors "amount to a threat to the peace",
  subject to veto.

### bunn2005npt

"NPT Withdrawal: Time for the Security Council to Step In". George Bunn, John B. Rhinelander. Arms
Control Today (Arms Control Association), about May 2005 (the date is inferred from the page, not
printed). URL https://www.armscontrol.org/node/1801. Opened.

- The DPRK pulled back its 1993 notice a day before it would take effect; in 2003 it claimed to be
  reviving that notice, so the Council had "only a single day"; the Council did not act (China
  opposed). Collects proposals: Germany (no withdrawal while in noncompliance; NPT-acquired items
  stay under safeguards), France (liability survives; Council can bar use of acquired items), a
  Stanford-Princeton group (treat such withdrawal as a threat to the peace).

### aca2022dprkchron

"Chronology of U.S.-North Korean Nuclear and Missile Diplomacy, 1985-2022". Arms Control
Association fact sheet (undated page). URL https://www.armscontrol.org/factsheets/dprkchron. Opened
(first 100,000 characters read).

- 12 March 1993: the DPRK "announces its intention to withdraw from the NPT in three months".
  11 June 1993: suspends it "just before the withdrawal would have become legally effective" ("one
  day before it was to become legally binding"). 27 December 2002: orders IAEA inspectors out.
  10 January 2003: announces withdrawal "effective January 11". 9 October 2006: first nuclear test.
- Derived: 91 days from notice to suspension in 1993; 1 day of effective notice in 2003; 15 days
  from expelling inspectors to effective withdrawal; 1367 days from effective withdrawal to the
  first test.
- Bears on: a notice period protects only if the regime can hold the withdrawing party to it.

### Arms control signalling and verification

### coe2020arms

"Why Arms Control Is So Rare". Andrew J. Coe, Jane Vaynman. American Political Science Review
114(2):342-355, 2020. DOI 10.1017/S000305541900073X. Open access, full text opened.

- Abstract: "The main impediment to arms control is the need for monitoring that renders a state's
  arming transparent enough to assure its compliance but not so much as to threaten its security."
  The cases "account for almost 40% of all global arming in the past two centuries". World
  military spending was 2.2% of world GDP, $2.7 trillion, in 2016 (p342).
- Model (p344): monitor A, armer B; each period B may invest at cost k and succeeds with
  probability l; a public signal detects investment with probability t_c (B closed) or t_o >= t_c
  (B open); no false positives; discount d.
- Proposition 2 (closed deal exists iff): d [l + t_c (1 - l)] S >= k + d l (W_n^B - V_p^B), with
  surplus S = 1/(1-d) - V_p^A - V_p^B. The right side is B's temptation; the left is the reward A
  can withdraw, weighted by the chance arming succeeds (and is revealed) or fails and is detected.
- Transparency requirement (p346): "The more quickly and reliably that B can arm (equivalent to
  higher l) and the larger the impact successful arming will have ... the more closely B must be
  monitored"; "Warships should be easier to limit in a closed deal than similarly impactful cyber
  weapons because only the former are large physical objects".
- Proposition 3 adds a security condition for an open deal,
  1 + d W_o^A - k + d [l W_n^B + (1 - l) V_c^B] <= 1/(1-d), covering overt reneging (closing to
  monitoring, then arming), whose downside is that "A's punishment will be immediate".
- Corollary 2: without a transparency-security trade-off "a deal will always be made", and the
  monitoring level "never need be perfect" (t <= t_o < 1). Corollary 3: otherwise an open deal
  exists iff the trade-off is "not too severe".
- Bears on: verification design (audits that expose weights, capabilities or data-centre
  locations have a security cost); breakout speed l maps to D3; overt reneging is withdrawal.

### kydd2000trust

"Trust, Reassurance, and Cooperation". Andrew Kydd. International Organization 54(2):325-357, 2000.
DOI 10.1162/002081800551190. Opened: abstract only (Crossref).

- Abstract: "I present a rational choice theory of reassurance focusing on costly signals ... The
  central result is that reassurance will be possible between trustworthy players in equilibrium
  if trustworthy actors are more willing to take risks to attain mutual cooperation than
  untrustworthy actors."
- Bears on: accepting intrusive verification as a costly signal that separates types.

### baker2023nuclear

"Nuclear Arms Control Verification and Lessons for AI Treaties". Mauricio Baker. arXiv 2304.04123v1,
8 April 2023. Full text opened (read in parts).

- Sec 3.1: nuclear verification systems "are designed with the aim of ensuring that any attempted
  treaty violation would be quickly detected, with high enough probability to deter the
  violation", using "multiple layers of defense".
- fn 50: "The IAEA has explicitly decided to make this tradeoff such that its detection
  probability is 90-95% for the most sensitive nuclear material."
- fn 122: Additional Protocol complementary access "upon request with 24 hours' notice".

### iaea2022glossary

"IAEA Safeguards Glossary, 2022 Edition". International Atomic Energy Agency, Vienna, 2022. URL
https://www-pub.iaea.org/MTCD/Publications/PDF/PUB2003_web.pdf. Full text opened.

- 3.20 Conversion time: "The time required to convert different forms of nuclear material into the
  metallic components of a nuclear explosive device. Conversion time is used to determine timely
  detection requirements under the Safeguards Criteria."
- Table 2 (p31): Pu, HEU or U-233 metal, "Order of days (7-10)"; pure compounds and MOX, weeks
  (1-3); in irradiated fuel, months (1-3); uranium below 20% U-235 and thorium, months (3-12).
- Table 1 (p30): significant quantity Pu 8 kg; HEU 25 kg U-235; LEU 75 kg U-235.
- 3.21 Detection time: "An estimate of the time available for detection of a step in an
  acquisition path". 9.31: false alarm probability "generally set to a small value (e.g. 1 %)".
  9.32: verification levels with (1 - beta) = 0.2, 0.5 and 0.9; the achieved detection probability
  is "not necessarily as large as (1 - beta)".
- Bears on: the memo's organising idea (timeliness shorter than conversion time) as a published
  spec; the NPT's 90-day notice against conversion times of 7 days to 12 months.

### AI races

### armstrong2013racing

"Racing to the precipice: a model of artificial intelligence development". Stuart Armstrong, Nick
Bostrom, Carl Shulman. FHI Technical Report 2013-1, October 2013. URL
https://www.futureofhumanityinstitute.org/s/2013-1.pdf. Full text opened. Published as AI & Society
31(2):201-206, 2016, DOI 10.1007/s00146-015-0590-y (journal version not opened).

- Model (Sec 2): n teams, capability c ~ U[0, mu], safety s in [0, 1]; highest c - s wins; the
  winner's AI succeeds with probability s; enmity e.
- No-information symmetric equilibrium (Sec 2.1): s = mu/(e n) if mu < e n, else 1; disaster
  probability 1 - mu/(e n) when mu < e n.
- Abstract: more teams and more enmity raise danger, "especially if risk taking is more important
  than skill"; "Surprisingly, information also increases the risks: the more teams know about each
  others' capabilities (and about their own), the more the danger increases."
- Bears on: O2; declarations and verification reveal capability, which in this model raises risk.

### han2020regulate

"To Regulate or Not: A Social Dynamics Analysis of an Idealised AI Race". The Anh Han, Luis Moniz
Pereira, Francisco C. Santos, Tom Lenaerts. Journal of Artificial Intelligence Research 69:881-921,
2020. DOI 10.1613/jair.1.12225; arXiv 1907.12393. arXiv full text opened.

- Evolutionary game: W rounds to "AI supremacy"; unsafe players have speed s > 1, safe players pay
  cost c; p_r is the risk of a setback for unsafe play.
- Early regime: safe development is the preferred collective outcome when p_r > 1 - 1/s (eq 1);
  safe strategies are selected by social learning when p_r > 1 - 1/(3s) (eq 2). Between the two is
  a dilemma zone; for s = 1.5 it is 0.78 > p_r > 0.33.
- Abstract: "the time-scale in which AI supremacy can be achieved plays a crucial role"; "blindly
  imposing regulations may not have the anticipated effect"; in the late regime "certain
  conditions require the promotion of risk-taking".
- Bears on: restricting only where a dilemma exists (useful AI stays allowed elsewhere); time
  scale W maps to breakout time.

### emeryxu2024uncertainty

"Uncertainty, Information, and Risk in International Technology Races". Nicholas Emery-Xu, Andrew
Park, Robert Trager. Journal of Conflict Resolution 68(10):2019-2047, 2024. DOI
10.1177/00220027231214996. Opened: the authors' accepted manuscript (full text).

- Logistic contest success function Pr(i wins) = e^(m k_i) / (e^(m k_i) + e^(m k_j)), decisiveness
  m >= 0 (p7).
- Proposition 4: with no or private information "risk always increases with decisiveness, unless
  risk is 0". Proposition 5: "The no information scenario is always safer than the private
  information scenario"; public against private depends on m (switch at m = 6 in Figure 2).
- Abstract: revealing capabilities "has two opposing effects on risk"; public information is less
  risky than private "except under high decisiveness".
- Bears on: verification's information effect; a decisive breakout is a high-m race.

### askell2019cooperation

"The Role of Cooperation in Responsible AI Development". Amanda Askell, Miles Brundage, Gillian
Hadfield. arXiv 1907.04534v1, 10 July 2019. Full text opened.

- Agent 1 cooperates iff p a1 + (1 - p) b1 > p c1 + (1 - p) d1 (p11), with payoffs for CC, CD, DC,
  DD and belief p that the other cooperates. Five factors: "High Trust", "Shared Upside", "Low
  Exposure", "Low Advantage", "Shared Downside" (p2).
- Bears on: fast detection lowers Exposure; capping breakout below decisive lowers Advantage.

### AI agreements, verification and breakout, 2025 to 2026

### gan2026clock

"Agreements Have a Clock: Compute Growth and the Verification of AI Restraint". Li Gan. arXiv
2611.04272v1 [econ.GN], 3 November 2026. Full text opened. Closest prior art for compliance as an
equilibrium in an AI pause with a response window.

- Abstract: "Cooperation is supportable when the monitoring needed to deter a breakout costs no
  more than either country gains from cooperating. As compute grows during a pause, a secret
  advance reaches the frozen frontier sooner, shrinking the response window: agreements have a
  clock." Example: supportable through month 18.9; to 25.5 with verified matched safety research;
  to 31.8 with monitoring cost halved.
- Game (Sec 4.3.1, p13-14): the leader proposes monitoring intensity m; each country pays eta_i m;
  then pause or secret advance; "a truthful public finding arrives at Poisson rate m per month
  within the response window w_i > 0". Payoffs C (both comply), R (race), T (successful
  breakout), S (sucker).
- Proposition 3 (eq 14): restarting after a finding is credible iff
  (1 - p2) chi_j Z_j > c_j - d_j + (p2 - p1) Y_j.
- Proposition 4 (eq 15): mutual compliance is supportable iff
  m_min = max_i xi_i / w_i <= m_max = min_i (C_i - R_i)/eta_i, with
  xi_i = ln[(T_i - R_i)/(C_i - R_i)] > 0, from detection within the window with probability
  1 - exp(-m w_i). "Mutual advancement remains an equilibrium ... the result establishes existence,
  not unique selection of cooperation."
- p15-16: "Deterrence does not require near-certain detection." With (C, T, R, S) =
  (2.5, 3.2, 1.0, 0.6), xi = 0.383 and a 12-month window, m = 0.0319 findings a month; detection
  within the window is about 32%, so at the threshold a breakout "still succeeds with probability
  e^-xi ~ 68 percent". Capping success at beta needs m >= ln(1/beta)/w_B.
- Eq 16: w_B(d) = max{T_catch(d) - l, 0}. Corollary 1 (eq 17): supportable only if
  T_catch(d) >= l + xi_B/m_max; T_catch falls to zero during a compliant pause as compute grows,
  so supportable review dates are bounded. Critical window 6.89 months. "the visible gap is a poor
  measure of the time to respond."
- Equal-capability rivals (Sec 4.5): a follower with the leader's compute catches up in 4.4
  months instead of 12 and needs about 2.7 times the monitoring.
- Credits Avenhaus and Canty 1996, Avenhaus et al. 2002, Coe and Vaynman 2020, Emery-Xu et al.
  2024 and Baker 2023. Calibration is illustrative; of payoffs Y and Z it says "No evidence
  guides" them. My reading: bilateral only, with no coalitions of n parties and no withdrawal
  clause. The paper states it was written with AI assistance.
- Bears on: D3/D4 (w is the margin between breakout and response), the memo's failure mode
  "algorithmic progress shrinking breakout time", and the multi-channel detection rate.

### fithian2026hardwired

"The Feasibility of a Hardwired Pause of Frontier AI Training". Working Group on AI Pause
Feasibility (organisers William Fithian and Wesley H. Holliday, UC Berkeley; members including
Kayla Blomquist and Gregory Conti). Working paper v1.0.2, 26 October 2026. URL
https://hardwired-pause.ai/paper. No arXiv ID or DOI found. Full PDF opened. Closest prior art for a
state or coalition compute threshold for breakout.

- Threat models (Sec 3.1.1): private evasion, state covert evasion, state overt breakout.
  Estimates for year-end 2026 (p42): frozen frontier C_F = 2e27 FLOP; treaty ceiling C_T = 2e24
  FLOP; covert evasion budget C_E = 2e28 FLOP; overt breakout budget C_B = 2e29 FLOP;
  F_E = 6.4M H100e; F_B = 180M H100e.
- Definition (p43): F_E(t) = rho_E C_E(t) / (T_E U_F), research overhead rho, strategic horizon T,
  utilisation U_F; "The breakout fleet threshold is defined analogously"; "a larger fleet is
  required to break out within T_B = 1 year than to break out within T_B = 3 years".
- Ledgers (p44): for each state s, L_E(s) = sum_c K_E(c, s) <= alpha_E F_E and
  L_B(s) <= alpha_B F_B, allowances alpha < 1. fn 23: "there might be per-coalition allowances in
  addition to per-state allowances". Dark compute is ungoverned by definition.
- Sec 6.2.3 (p101-103): T_B = 2 years because a breakout must reach "its decisive advantage before
  the rest of the world could react to stop it"; C_B set by what "a bullish would-be defector might
  believe"; F_B = 12 x 2e29 / (2 x 0.21) = 180M H100e, against a projected global fleet of 47M H100e
  at year-end 2026. A more bullish timeline gives 36M; T_B = 1 year gives 350M and 73M.
- Sec 6 assessment: if ledger components could be cut below 0.25% of F_E and F_B, "a treaty with
  fractional allowances of 25% (alpha_E = alpha_B = 0.25) could be sustained".
- Sec 2.3 (p30-31): the race may be a Stag Hunt rather than a Prisoners' Dilemma; a repeated game
  "with an unknown end date"; informative public signals support simple cooperative equilibria
  (Green and Porter 1984; Abreu et al. 1990; Fudenberg, Levine and Maskin 1994); the n-country
  case is analogous. Sec 3.5: exit is procedural (e.g. ten-year terms with renewals); no notice
  period derived from breakout or response times.
- Bears on: the coalition threshold (here per state, coalitions mentioned, T_B chosen by judgement
  rather than derived from detection and response time), D3, P1.

### scher2025agreement

"An International Agreement to Prevent the Premature Creation of Artificial Superintelligence".
Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance Team). arXiv
2511.10783 (v3, 8 May 2026). Full text opened.

- A US- and PRC-led coalition; training above 1e24 FLOP prohibited, 1e22 to 1e24 FLOP monitored;
  chip concentrations above 16 H100-equivalents tracked; verification by chip tracking, power
  monitoring, "challenge inspections, whistleblowers, and more".
- Breakout: "when a party attempts to create ASI before anyone else can stop them"; existing chips
  may make "breakout time too short"; rebuilding a decommissioned chip supply chain might take "a
  decade or more".
- Article XV: unlimited duration; NPT-style withdrawal "12 months in advance"; during the notice
  the withdrawing state helps certify it "will be unable to develop, train, post-train, or deploy
  dangerous AI systems", removing covered clusters and chip-making equipment or making them
  inoperable; a withdrawn state "remains subject to Protective Actions". Precedents: CWC Art XVI,
  90 days; Outer Space Treaty Art XVI, one year; UNSC Resolution 1718 on the DPRK after 2006.
  "the agreement needs barriers to withdrawal"; mutual killswitches suggested.
- Bears on: withdrawal (12 months chosen for the assurance tasks, not derived), D3, channels.

### rahman2025nonparty

"Would ASI development in non-party states undermine a nonproliferation agreement?". Robi Rahman.
MIRI Technical Governance Team blog, 25 November 2025. URL
https://techgov.intelligence.org/blog/would-asi-development-in-non-party-states-undermine-a-nonproliferation-agreement.
Opened.

- "It only takes one uncautious non-party AI project that crosses the line of extinction-level
  capabilities"; "Remaining outside the agreement should be economically costly."; "Partial
  adoption is not a deal-breaker." The coalition should cover "a large majority of the relevant
  hardware", but no share threshold is derived and non-party compute is not quantified.
- Enforcement: export controls, chip consolidation, "do-not-assist" duties, challenge inspections
  on 24-hour timelines, whistleblower protection, escalating protective actions, import bans on AI
  services from non-parties.

### petrie2025flexheg

"Flexible Hardware-Enabled Guarantees for AI Compute" (Part I: Overview). James Petrie, Onni Aarne,
Nora Ammann, David Dalrymple. April 2025. arXiv 2506.15093. Opened: Part I; the Part III appendix
with the game model is not in the file I read.

- "As long as the expected geopolitical advantage to be gained from defecting from the agreement is
  smaller than the expected loss of security caused by the unraveling of the agreement, it would be
  rational for the major players not to defect." Their model (not read) suggests stability if
  defection gives at most a "75% chance of winning" and participants see at least a "10% chance of
  catastrophe" without coordination. "states capable of chip production could still gradually exit
  the agreement unilaterally by resuming production of non-flexHEG chips".

### baker2025verifying

"Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI
Development and Deployment". Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart
Heim. arXiv 2507.15916v2, 25 July 2025. Full text opened.

- fn 33 (Sec 3.2): "a verification regime's probability of detecting a violation is approximately
  that of the subgoal with the lowest probability of detecting a violation. This is because a
  Prover only needs to circumvent one verification subgoal to hide a violation, and a rational
  Prover seeking to hide a violation will choose to circumvent the subgoal where they are least
  likely to be caught." Aggregating small violations across subgoals "may involve a lower or higher
  probability of detection, depending on the detection probabilities and their correlation".
- A.8 Whistleblower programs (p53-54): large AI projects "involve hundreds of employees"; in-person
  visits to Verifier-secured buildings proposed; risk that "a Prover can have sufficient
  compartmentalization and employee loyalty for all accomplices to lie".
- Bears on: contradicts multiplying channel miss rates; the whistleblower channel.

### koopmanschap2026gpu

"How to Catch a GPU: A Taxonomy of Verification and Enforcement Mechanisms for International AI
Agreements". Raymond Koopmanschap, Otto Barten. arXiv 2607.22619v1, 16 June 2026. Opened (abstract
and contents read, full text searched).

- Principle: "wherever sufficient capacity exists to violate an agreement, it must be under a
  control regime"; defines "the enforcement breaking point as the FLOP-threshold or equivalent
  metric at which a policy loses its effectiveness". Proposals focus on preventing escape; hidden
  capacity detection "receive[s] less attention". No game model, coalition threshold or withdrawal
  analysis (searches of the text for these found nothing).

### hendrycks2025superintelligence

"Superintelligence Strategy: Expert Version". Dan Hendrycks, Eric Schmidt, Alexandr Wang. arXiv
2503.05628v2, 14 April 2025. Opened (abstract and Sec 4 read, rest searched).

- "Mutual Assured AI Malfunction (MAIM): a deterrence regime resembling nuclear mutual assured
  destruction (MAD) where any state's aggressive bid for unilateral AI dominance is met with
  preventive sabotage by rivals", by means "from covert cyberattacks to potential kinetic strikes on
  datacenters". Maintenance: escalation ladders, remote siting, "transparency into datacenters".
- Bears on: what "respond" in T_r means (disablement, not only sanctions). Not a formal model.

### Rewarded reporting

### dyck2007whistle

"Who Blows the Whistle on Corporate Fraud?". Alexander Dyck, Adair Morse, Luigi Zingales. NBER
Working Paper 12882, February 2007. DOI 10.3386/w12882. Full text opened. Published as Journal of
Finance 65(6):2213-2253, 2010, DOI 10.1111/j.1540-6261.2010.01614.x (not opened; its numbers may
differ).

- Sample: all reported alleged frauds at US firms with over $750 million in assets, 1996-2004; 230
  cases.
- Abstract: "Only 6% of the frauds are revealed by the SEC and 14% by the auditors. More important
  monitors are media (14%), industry regulators (16%), and employees (19%)." Mandated actors found
  35% before SOX, slightly over 50% after.
- p4-5: under the False Claims Act whistleblowers get 15 to 30% of recoveries; in healthcare
  "46.7% of frauds are brought to light by employees" against 16.3% elsewhere (significant at 1%),
  with fewer, not more, frivolous suits. SOX protections without money did not help: employee
  detection fell "from 20.7% to 15.6% of cases after SOX".
- Sec 3.3: "In 82% of cases where the identity of the whistleblower was revealed, s/he was fired,
  quit under duress, or had significantly altered responsibilities."
- Bears on: rewarded whistleblowing as a channel; rewards matter, protections alone do not.

### dyck2017pervasive

"How Pervasive Is Corporate Fraud?". Alexander Dyck, Adair Morse, Luigi Zingales. Working paper,
April 2017. URL
https://www.law.nyu.edu/sites/default/files/upload_documents/Adair%20Morse%20How%20Pervasive%20is%20Corporate%20Fraud.pdf.
Full text opened. Published as Review of Accounting Studies 29(1):736-769, 2024, DOI
10.1007/s11142-022-09738-5 (not opened).

- Method: Arthur Andersen's demise raised detection to near one for its former clients.
- Abstract: "only one third of frauds are detected in normal times"; in 1996-2004 "one large
  publicly-traded US firms out of every eight was engaged in fraud".
- p2: "the detection rate is 31%"; 29% (restatements with SEC investigation), 33% (all
  restatements), 55% (AAERs); "For every fraud that is caught, we find that between 1 and 2
  additional frauds go undetected"; prevalence 4.0%/0.311 = 13%.
- Bears on: a measured detection likelihood for a mature many-channel oversight system.

### sec2026whistleblower

"Annual Report to Congress for Fiscal Year 2025". SEC Office of the Whistleblower, 11 February 2026.
URL https://www.sec.gov/files/fy25-annual-whistleblower-report.pdf. Full text opened.

- Awards for original information leading to sanctions over $1 million are "10% to 30% of the
  monetary sanctions collected". FY2025: "more than $60 million to 48 individual whistleblowers";
  82 preliminary determinations; "approximately 27,000 whistleblower tips", about 12,000 of them
  from two individuals. Investor Protection Fund at the start of FY2025: $361.8 million.

### sec2024whistleblower

"Annual Report to Congress for Fiscal Year 2024". SEC Office of the Whistleblower, 15 November
2024. URL https://www.sec.gov/files/fy24-annual-whistleblower-report.pdf. Full text opened.

- FY2024: "over $255 million ... to 47 individual whistleblowers"; "more than $2.2 billion to 444
  individual whistleblowers since the Program's inception in 2011"; about 24,980 tips (over 14,000
  from two individuals); 11 actions against impeding whistleblowers in FY2024 (a record), 32
  impeding and 5 anti-retaliation actions since inception.

## Numbers for the ledger

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| npt-withdrawal-notice | 3 | months | spec | eu2005nptwithdrawal | para 1, Art X(1) |
| cwc-withdrawal-notice | 90 | days | spec | scher2025agreement | Art XV commentary (secondary; CWC Art XVI not opened) |
| ost-withdrawal-notice | 1 | year | spec | scher2025agreement | Art XV commentary (secondary; OST Art XVI not opened) |
| geneva-denunciation-delay | 1 | year | spec | helfer2005exiting | fn 50 |
| bit-denunciation-bar | 10 | years after entry into force | spec | helfer2005exiting | p1625 |
| miri-draft-withdrawal-notice | 12 | months | design | scher2025agreement | Art XV |
| dprk-1993-notice-to-suspension | 91 | days | measured | aca2022dprkchron | 12 Mar to 11 Jun 1993 (derived) |
| dprk-2003-effective-notice | 1 | day | measured | aca2022dprkchron; bunn2005npt | 10 Jan 2003 entry |
| dprk-inspectors-out-to-withdrawal | 15 | days | measured | aca2022dprkchron | 27 Dec 2002 to 11 Jan 2003 (derived) |
| dprk-withdrawal-to-first-test | 1367 | days | measured | aca2022dprkchron | 11 Jan 2003 to 9 Oct 2006 (derived) |
| treaty-exits-1945-2004 | 1547 | denunciations and withdrawals | measured | helfer2005exiting | p1601 |
| treaty-ratifications-1945-2004 | 32021 | ratifications | measured | helfer2005exiting | p1602 |
| share-treaties-ever-denounced | 3.5 | % (191 of 5416) | measured | helfer2005exiting | p1606 |
| coil-withdrawal-clause-share | 70 | % of agreements | measured | koremenos2016continent | ch 5 page summary |
| coil-escape-clause-share | 19 | % of agreements | measured | koremenos2016continent | ch 5 page summary |
| iaea-conversion-metal | 7 to 10 | days | spec | iaea2022glossary | Table 2 |
| iaea-conversion-pure-compounds | 1 to 3 | weeks | spec | iaea2022glossary | Table 2 |
| iaea-conversion-irradiated | 1 to 3 | months | spec | iaea2022glossary | Table 2 |
| iaea-conversion-leu | 3 to 12 | months | spec | iaea2022glossary | Table 2 |
| iaea-sq-plutonium | 8 | kg Pu | spec | iaea2022glossary | Table 1 |
| iaea-false-alarm-typical | 0.01 | probability | spec | iaea2022glossary | 9.31 |
| iaea-verification-level-high | 0.9 | detection probability (1 - beta) | spec | iaea2022glossary | 9.32 |
| iaea-detection-goal-sensitive | 0.90 to 0.95 | probability | spec | baker2023nuclear | fn 50 (secondary) |
| ap-complementary-access-notice | 24 | hours | spec | baker2023nuclear | fn 122 |
| leadership-example-violation-simultaneous | 2/3 | probability | design | avenhaus2002inspection | Fig 5.3 (illustrative game) |
| leadership-example-violation-leader | 0 | probability | design | avenhaus2002inspection | Fig 5.3, Theorem 5.1 |
| timeliness-unobservable-value-m2 | 1/e | fraction of interval | design | avenhaus2002inspection | Theorem 4.3 |
| timeliness-observable-value-m2 | 1/2 | fraction of interval | design | avenhaus2002inspection | Sec 4.2 |
| gan-deterrent-detection-in-window | 0.32 | probability | assumption | gan2026clock | p15-16 (calibration) |
| gan-critical-window | 6.89 | months | assumption | gan2026clock | Corollary 1 example |
| gan-supportable-until | 18.9 | months into pause | assumption | gan2026clock | abstract |
| hwp-breakout-budget | 2e29 | FLOP | assumption | fithian2026hardwired | p42, Sec 6.2.3 |
| hwp-breakout-fleet | 180 | million H100e | assumption | fithian2026hardwired | p42, p102 |
| hwp-evasion-fleet | 6.4 | million H100e | assumption | fithian2026hardwired | p42 |
| hwp-breakout-horizon | 2 | years | design | fithian2026hardwired | Sec 6.2.3 |
| hwp-global-fleet-2026 | 47 | million H100e | assumption | fithian2026hardwired | p102 (projection) |
| hwp-utilisation | 0.21 | fraction | assumption | fithian2026hardwired | p102 |
| hwp-allowance | 0.25 | fraction of threshold | design | fithian2026hardwired | Sec 6 |
| miri-strict-threshold | 1e24 | FLOP | design | scher2025agreement | p6 |
| miri-monitored-threshold | 1e22 | FLOP | design | scher2025agreement | p6 |
| fraud-detected-by-employees | 19 | % of detected frauds | measured | dyck2007whistle | abstract |
| fraud-detected-by-sec | 6 | % of detected frauds | measured | dyck2007whistle | abstract |
| fraud-detected-by-employees-qui-tam | 46.7 | % (healthcare) | measured | dyck2007whistle | p4-5 |
| fraud-detected-by-employees-other | 16.3 | % (other industries) | measured | dyck2007whistle | p4-5 |
| whistleblower-retaliation-share | 82 | % of named whistleblowers | measured | dyck2007whistle | Sec 3.3 |
| fraud-detection-likelihood | 0.31 | probability per fraud | measured | dyck2017pervasive | p2 |
| fraud-prevalence-1996-2004 | 13 | % of large US firms | measured | dyck2017pervasive | p2 |
| sec-award-share | 10 to 30 | % of sanctions collected | spec | sec2026whistleblower | p1 |
| sec-awards-fy2025 | 60 | million USD to 48 people | measured | sec2026whistleblower | p1 |
| sec-tips-fy2025 | 27000 | tips (about 12000 from two people) | measured | sec2026whistleblower | tips section, about p5 |
| sec-awards-fy2024 | 255 | million USD to 47 people | measured | sec2024whistleblower | p1 |
| sec-awards-cumulative-2011-2024 | 2.2 | billion USD to 444 people | measured | sec2024whistleblower | p1 |
| world-military-spending-2016 | 2.7 | trillion USD (2.2% of world GDP) | measured | coe2020arms | p342 (CIA World Factbook) |
| threshold-known-avoid-share | 8 of 10 | groups | measured | barrett2012climate | Results |
| threshold-uncertain-catastrophe-share | 9 of 10 | groups (catastrophe certain) | measured | barrett2012climate | Results |
| club-stable-coalition-no-sanction | 2 to 3 | countries | design | nordhaus2015climate | p1344-45 (identical-country analytic case, online appendix) |
| han-dilemma-zone-s1.5 | 0.33 to 0.78 | setback probability p_r | design | han2020regulate | early regime, eqs (1) and (2), worked example |
| gan-catch-up-equal-compute | 4.4 | months (against 12) | assumption | gan2026clock | Sec 4.5 |

## Formal results to build on

1. **General inspection game** (avenhaus2002inspection, Theorem 3.1): equilibrium alpha* solves
   -h alpha* = -b + (1+b) beta(alpha*); q* = e / (e - (1-a) beta'(alpha*)); beta(alpha) is the
   value of the zero-sum non-detection game min over tests, max over violation procedures.
   Corollary used by Subcritical: legal behaviour is a best response iff
   beta <= (b - h alpha)/(1 + b), i.e. detection 1 - beta >= (1 + h alpha)/(1 + b), with the
   violator's gain normalised to 1 and b the penalty in those units.
2. **Inspector leadership** (avenhaus2002inspection, Theorem 5.1; vonstengel2016recursive,
   Proposition 1 conditions (47) to (49) and Theorem 5): commit to alpha* (or p*); the inspectee is
   legal for any announcement at or above it; leader payoff L > Nash payoff N; the follower's
   payoff is unchanged. Under incomplete information about the violator's gain, announce the
   probability that deters every type in the support (Avenhaus, Okada and Zamir 1991, as
   reported).
3. **Recursive inspections** (Dresher, as restated in avenhaus2002inspection eqs 4.1 to 4.6 and
   Theorem 4.2; vonstengel2016recursive): closed forms with binomial sums; the inspection probability
   does not depend on the number of intended violations. End effect: once inspections run out the
   inspectee violates, so a licence regime with a known last period unravels; the hardwired-pause
   paper's "unknown end date" and the memo's renewing licences are the remedy to formalise.
4. **Timeliness** (avenhaus2002inspection Theorem 4.3; canty2001timely, abstract only): with
   unobservable inspections the expected detection delay is 1/e of the interval for m = 2, tending
   to 1/(2m - 4/3) for large m; with observable inspections, 1/m. The IAEA conversion times
   (iaea2022glossary Table 2) are the published analogue of D4's T_b.
5. **Strategic spreading** (avenhaus2002inspection Theorem 3.2): against a strategic diverter,
   subdividing a plant into many balance areas does not raise detection; only the total balance
   matters, unless the split shortens detection time. Relevant to training spread across many
   small sites.
6. **Deterrence with imperfect monitoring** (coe2020arms Propositions 2 and 3, Corollaries 2 and
   3): d [l + t (1 - l)] S >= k + d l (W_n^B - V_p^B); faster or more decisive arming raises the
   required monitoring; perfect monitoring is never required absent the transparency-security
   trade-off.
7. **Priced deterrence with a response window** (gan2026clock Proposition 4, Corollary 1):
   max_i ln[(T_i - R_i)/(C_i - R_i)] / w_i <= min_i (C_i - R_i)/eta_i, with Poisson detection
   probability 1 - exp(-m w) inside the window; T_catch(d) >= l + xi/m_max fails as compute grows.
8. **Fleet thresholds** (fithian2026hardwired Sec 3.2): F_B = rho_B C_B / (T_B U_F) and the ledger
   inequality sum_c K_B(c, s) <= alpha_B F_B, with per-coalition allowances mentioned in fn 23.
9. **Coalition stability**: CPNE (bernheim1987coalition, definition as in ali2019coalitions
   Definition 10) and strong equilibrium ("coalition Nash", nordhaus2015climate p1346).
   Without outside sanctions stable coalitions have 2 or 3 members in the symmetric case
   (nordhaus2015climate).
10. **Costly exit** (rosendorff2001optimal Propositions 1 and 2): cooperation with an escape
    clause holds for any discount factor iff the exit cost k <= K; above K the regime collapses.
11. **Threshold coordination** (barrett2012climate): with a known threshold, avoiding it is a
    Pareto-dominant Nash equilibrium (coordination game); with an uncertain location, a dilemma.
12. **Race models**: armstrong2013racing s = mu/(e n); emeryxu2024uncertainty logistic contest
    and Propositions 4 and 5; han2020regulate zones p_r > 1 - 1/s and p_r > 1 - 1/(3s);
    askell2019cooperation p a + (1-p) b > p c + (1-p) d.

What Subcritical could add (my suggestions, not results from the literature, to be proved in
05-formal):

- **Window from D4.** Gan's window w is the time between detection and the point a breakout
  becomes decisive, net of response. In the memo's terms w = T_b - T_r. Deterrence then needs a
  combined detection rate lambda >= xi / (T_b - T_r), and D4's margin m is the factor that keeps w
  positive.
- **Strategic multi-channel detection.** Replace the memo's product of independent miss rates with
  the inspection-game form: miss = max over evasion strategies omega of
  P(no channel fires | omega). With channel rates lambda_j(omega), miss over the window is
  max_omega exp(-sum_j lambda_j(omega) w), which is a product only when no omega lowers several
  channels at once. RAND's weakest-link claim is the case where channels cover disjoint subgoals.
- **Coalition threshold derived, not chosen.** With the fleet model, a coalition holding share x
  of the global fleet F breaks out in T_b(x) = rho C_B / (x F U). Requiring T_b(x) >= m T_r gives
  x* = rho C_B / (m T_r F U). Coalition-proof compliance then asks that no subcoalition with
  combined share at or above x* has a self-enforcing deviation (BPW). This differs from the
  hardwired-pause paper, which fixes T_B = 2 years by judgement and allocates per-state ledgers.
- **Withdrawal under D4.** If every party's holdings satisfy T_b(H) >= m T_r at the moment of exit,
  the remaining parties can respond to an exiting party even with zero notice, provided response
  can start at exit. Notice is then needed for (a) holdings whose T_b has shrunk below the line
  during membership (Gan's clock, algorithmic progress), and (b) freezing or removing assets
  acquired under the regime (EU 2005, MIRI Art XV). The memo's condition "notice longer than
  response time" is then N >= m T_r - T_b(H_exit), together with an asset freeze during N. The NPT
  failed this because it allowed holdings (enrichment, reprocessing) whose conversion time was far
  shorter than the notice, and because the notice itself was not enforced.

## Prior art for the memo's candidates

All judgements below are claims about my search, not about the world.

**1. A bound on the compute share a coalition needs to break out before detection.**
Web searches tried (verbatim): `coalition of states minimum share of compute needed to break out
of AI agreement before detection`; `"breakout" coalition threshold treaty game theory "fraction
of" capacity defect "detected" arms control model blocking coalition`; `"inspection game"
artificial intelligence compute verification treaty`; `game-theoretic model international AI
agreement verification defection detection probability compute 2025 arXiv`; `"self-enforcing" OR
"coalition-proof" international AI agreement game theory Barrett participation 2025 2026`. Then
the related-work sections and reference lists of the AI agreement papers found, and text searches
of koopmanschap2026gpu and fithian2026hardwired for "coalition", "breakout" and "withdraw".
Closest hits: fithian2026hardwired (per-state breakout and evasion fleet thresholds with a time
horizon, per-coalition allowances mentioned in a footnote, T_B chosen as 2 years by judgement of
reaction time); gan2026clock (bilateral, response window, no coalitions; its 0.85% figure is the
leader's research share to keep its lead, not a coalition threshold); rahman2025nonparty and
scher2025agreement (coalition must hold "a large majority of the relevant hardware", not
derived); koopmanschap2026gpu ("sufficient capacity" principle, no number); nordhaus2015climate
and barrett1994self (coalition participation stability, not breakout). Judgement: **extends prior
work.** The per-state compute threshold for breakout within a horizon exists (Berkeley, October
2026). Not found in my search: the threshold derived from the regime's own detection and response
time, applied to coalitions with a coalition-proofness condition.

**2. Compliance as each party's best response (inspection games for AI).**
Searches as above, plus reading the AI agreement papers' related-work sections. Closest:
gan2026clock (formal: Poisson detection, response window, monitoring cost bound; cites Avenhaus and
Canty 1996 and Avenhaus et al. 2002); petrie2025flexheg (simple stability model, appendix not
read); fithian2026hardwired (repeated game and Stag Hunt discussion); hendrycks2025superintelligence
(deterrence by sabotage, informal); coe2020arms (general arms control). I found no paper applying
the Avenhaus line (inspector leadership, Neyman-Pearson non-detection games, Dresher recursion)
explicitly to AI compute verification. Judgement: **prior work** for "compliance is an equilibrium
when detection within the window times the loss exceeds the gain" (Gan 2026, and the arms control
literature before it); **extends prior work** for an inspection-game treatment with announced
random challenge inspections (leadership), strategic evasion across several channels, and the end
effect of licence renewals.

**3. Withdrawal notice longer than the response time.**
Searches tried (verbatim): `treaty withdrawal notice period longer than breakout time design
proposal nuclear OR AI "notice period" "breakout"`; `NPT Article X text "three months in advance"
...`; `Koremenos "Contracting around International Uncertainty" APSR 2005 withdrawal clause notice
period duration random sample treaties` (that 2005 article was found but not used); reading of scher2025agreement Art XV,
eu2005nptwithdrawal, bunn2005npt, helfer2005exiting, rosendorff2001optimal, fithian2026hardwired
Sec 3.5. Closest: scher2025agreement (12-month notice, assets removed during notice, chosen for the
time assurance tasks need); eu2005nptwithdrawal (freeze and safeguard assets during and after
notice); helfer2005exiting (temporal opportunism, ten-year denunciation bars). Not found: a notice
length derived from breakout and response times. Judgement: **extends prior work** (the design is
prior work; the derived inequality may be new), with the caveat in Formal results above that under
D4 the notice may be redundant for detection and matter mainly for assets whose breakout time fell
during membership.

**4. D4 itself (T_b < m T_r as the line).** Not my track's main candidate, but the survey bears on
it: the IAEA ties timeliness to conversion time (iaea2022glossary 3.20, "used to determine timely
detection requirements"); canty2001timely formalises a critical time; gan2026clock ties
deterrence to a response window that shrinks with compute; fithian2026hardwired sizes thresholds
by a breakout horizon chosen as the time before others can react. Judgement: D4 as a regulatory
trigger **extends prior work**; the memo's "new as a regulatory trigger" should be downgraded
unless the independent search finds a clear difference.

**5. Rewarded whistleblowing as a channel.** Prior work: scher2025agreement, rahman2025nonparty and
baker2025verifying all include whistleblowers. Measured evidence on effectiveness and on the role of
money comes from corporate fraud (dyck2007whistle, sec2024whistleblower, sec2026whistleblower).
Judgement: **prior work**; Subcritical's contribution can only be a measured detection rate for the
channel, transferred with stated caveats (a state can compartmentalise and coerce in ways a firm
cannot).

## Sources (TOML)

```toml
[source.avenhaus2002inspection]
type = "book"
title = "Inspection Games (Handbook of Game Theory with Economic Applications, vol. 3, ch. 51)"
authors = "Rudolf Avenhaus, Bernhard von Stengel, Shmuel Zamir"
year = 2002
doi = "10.1016/S1574-0005(02)03014-X"
url = "http://www.maths.lse.ac.uk/Personal/stengel/TEXTE/insp.pdf"
opened = "2026-11-27"

[source.vonstengel2016recursive]
type = "peer-reviewed"
title = "Recursive Inspection Games"
authors = "Bernhard von Stengel"
year = 2016
doi = "10.1287/moor.2015.0762"
arxiv = "1412.0129"
opened = "2026-11-27"

[source.dresher1962sampling]
type = "report"
title = "A Sampling Inspection Problem in Arms Control Agreements: A Game-Theoretic Analysis"
authors = "Melvin Dresher"
year = 1962
url = "https://www.rand.org/pubs/research_memoranda/RM2972.html"
opened = "2026-11-27"

[source.maschler1966price]
type = "peer-reviewed"
title = "A price leadership method for solving the inspector's non-constant-sum game"
authors = "Michael Maschler"
year = 1966
doi = "10.1002/nav.3800130103"
opened = "2026-11-27"

[source.canty2001timely]
type = "peer-reviewed"
title = "Timely inspection and deterrence"
authors = "Morton J. Canty, Daniel Rothenstein, Rudolf Avenhaus"
year = 2001
doi = "10.1016/S0377-2217(00)00082-5"
opened = "2026-11-27"

[source.avenhaus1996compliance]
type = "book"
title = "Compliance Quantified: An Introduction to Data Verification"
authors = "Rudolf Avenhaus, Morton John Canty"
year = 1996
isbn = "9780521553667"
opened = "2026-11-27"

[source.bernheim1987coalition]
type = "peer-reviewed"
title = "Coalition-Proof Nash Equilibria I. Concepts"
authors = "B. Douglas Bernheim, Bezalel Peleg, Michael D. Whinston"
year = 1987
doi = "10.1016/0022-0531(87)90099-8"
opened = "2026-11-27"

[source.ali2019coalitions]
type = "preprint"
title = "Coalitions in Repeated Games"
authors = "S. Nageeb Ali, Ce Liu"
year = 2019
arxiv = "1906.00280"
opened = "2026-11-27"

[source.barrett1994self]
type = "peer-reviewed"
title = "Self-Enforcing International Environmental Agreements"
authors = "Scott Barrett"
year = 1994
doi = "10.1093/oep/46.Supplement_1.878"
opened = "2026-11-27"

[source.nordhaus2015climate]
type = "peer-reviewed"
title = "Climate Clubs: Overcoming Free-riding in International Climate Policy"
authors = "William Nordhaus"
year = 2015
doi = "10.1257/aer.15000001"
opened = "2026-11-27"

[source.barrett2012climate]
type = "peer-reviewed"
title = "Climate negotiations under scientific uncertainty"
authors = "Scott Barrett, Astrid Dannenberg"
year = 2012
doi = "10.1073/pnas.1208417109"
opened = "2026-11-27"

[source.helfer2005exiting]
type = "legal-scholarship"
title = "Exiting Treaties"
authors = "Laurence R. Helfer"
year = 2005
url = "https://virginialawreview.org/articles/exiting-treaties/"
opened = "2026-11-27"

[source.rosendorff2001optimal]
type = "peer-reviewed"
title = "The Optimal Design of International Trade Institutions: Uncertainty and Escape"
authors = "B. Peter Rosendorff, Helen V. Milner"
year = 2001
doi = "10.1162/002081801317193619"
opened = "2026-11-27"

[source.koremenos2016continent]
type = "book"
title = "The Continent of International Law: Explaining Agreement Design"
authors = "Barbara Koremenos"
year = 2016
doi = "10.1017/CBO9781316415832"
isbn = "9781107124233"
opened = "2026-11-27"

[source.eu2005nptwithdrawal]
type = "official-docs"
title = "Withdrawal from the Treaty on the Non-Proliferation of Nuclear Weapons: European Union common approach (NPT/CONF.2005/WP.32)"
authors = "European Union (submitted by Luxembourg)"
year = 2005
url = "https://digitallibrary.un.org/record/548700/files/NPT_CONF.2005_WP.32-EN.pdf"
opened = "2026-11-27"

[source.kirgis2003dprk]
type = "legal-scholarship"
title = "North Korea's Withdrawal from the Nuclear Nonproliferation Treaty"
authors = "Frederic L. Kirgis"
year = 2003
url = "https://www.asil.org/insights/volume-8-issue-2-2/"
opened = "2026-11-27"

[source.bunn2005npt]
type = "essay"
title = "NPT Withdrawal: Time for the Security Council to Step In"
authors = "George Bunn, John B. Rhinelander"
year = 2005
url = "https://www.armscontrol.org/node/1801"
opened = "2026-11-27"

[source.aca2022dprkchron]
type = "report"
title = "Chronology of U.S.-North Korean Nuclear and Missile Diplomacy, 1985-2022"
authors = "Arms Control Association"
undated = true
url = "https://www.armscontrol.org/factsheets/dprkchron"
opened = "2026-11-27"

[source.coe2020arms]
type = "peer-reviewed"
title = "Why Arms Control Is So Rare"
authors = "Andrew J. Coe, Jane Vaynman"
year = 2020
doi = "10.1017/S000305541900073X"
opened = "2026-11-27"

[source.kydd2000trust]
type = "peer-reviewed"
title = "Trust, Reassurance, and Cooperation"
authors = "Andrew Kydd"
year = 2000
doi = "10.1162/002081800551190"
opened = "2026-11-27"

[source.baker2023nuclear]
type = "preprint"
title = "Nuclear Arms Control Verification and Lessons for AI Treaties"
authors = "Mauricio Baker"
year = 2023
arxiv = "2304.04123"
opened = "2026-11-27"

[source.iaea2022glossary]
type = "official-docs"
title = "IAEA Safeguards Glossary, 2022 Edition"
authors = "International Atomic Energy Agency"
year = 2022
url = "https://www-pub.iaea.org/MTCD/Publications/PDF/PUB2003_web.pdf"
opened = "2026-11-27"

[source.armstrong2013racing]
type = "report"
title = "Racing to the precipice: a model of artificial intelligence development (FHI Technical Report 2013-1; published in AI & Society 31(2), 2016, doi 10.1007/s00146-015-0590-y)"
authors = "Stuart Armstrong, Nick Bostrom, Carl Shulman"
year = 2013
url = "https://www.futureofhumanityinstitute.org/s/2013-1.pdf"
opened = "2026-11-27"

[source.han2020regulate]
type = "peer-reviewed"
title = "To Regulate or Not: A Social Dynamics Analysis of an Idealised AI Race"
authors = "The Anh Han, Luis Moniz Pereira, Francisco C. Santos, Tom Lenaerts"
year = 2020
doi = "10.1613/jair.1.12225"
arxiv = "1907.12393"
opened = "2026-11-27"

[source.emeryxu2024uncertainty]
type = "peer-reviewed"
title = "Uncertainty, Information, and Risk in International Technology Races"
authors = "Nicholas Emery-Xu, Andrew Park, Robert Trager"
year = 2024
doi = "10.1177/00220027231214996"
opened = "2026-11-27"

[source.askell2019cooperation]
type = "preprint"
title = "The Role of Cooperation in Responsible AI Development"
authors = "Amanda Askell, Miles Brundage, Gillian Hadfield"
year = 2019
arxiv = "1907.04534"
opened = "2026-11-27"

[source.gan2026clock]
type = "preprint"
title = "Agreements Have a Clock: Compute Growth and the Verification of AI Restraint"
authors = "Li Gan"
year = 2026
arxiv = "2611.04272"
opened = "2026-11-27"

[source.fithian2026hardwired]
type = "report"
title = "The Feasibility of a Hardwired Pause of Frontier AI Training (working paper v1.0.2)"
authors = "Working Group on AI Pause Feasibility (organizers William Fithian, Wesley H. Holliday)"
year = 2026
url = "https://hardwired-pause.ai/paper"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.rahman2025nonparty]
type = "essay"
title = "Would ASI development in non-party states undermine a nonproliferation agreement?"
authors = "Robi Rahman"
year = 2025
url = "https://techgov.intelligence.org/blog/would-asi-development-in-non-party-states-undermine-a-nonproliferation-agreement"
opened = "2026-11-27"

[source.petrie2025flexheg]
type = "preprint"
title = "Flexible Hardware-Enabled Guarantees for AI Compute"
authors = "James Petrie, Onni Aarne, Nora Ammann, David Dalrymple"
year = 2025
arxiv = "2506.15093"
opened = "2026-11-27"

[source.baker2025verifying]
type = "preprint"
title = "Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment"
authors = "Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart Heim"
year = 2025
arxiv = "2507.15916"
opened = "2026-11-27"

[source.koopmanschap2026gpu]
type = "preprint"
title = "How to Catch a GPU: A Taxonomy of Verification and Enforcement Mechanisms for International AI Agreements"
authors = "Raymond Koopmanschap, Otto Barten"
year = 2026
arxiv = "2607.22619"
opened = "2026-11-27"

[source.hendrycks2025superintelligence]
type = "preprint"
title = "Superintelligence Strategy: Expert Version"
authors = "Dan Hendrycks, Eric Schmidt, Alexandr Wang"
year = 2025
arxiv = "2503.05628"
opened = "2026-11-27"

[source.dyck2007whistle]
type = "preprint"
title = "Who Blows the Whistle on Corporate Fraud? (NBER Working Paper 12882; published in Journal of Finance 65(6), 2010, doi 10.1111/j.1540-6261.2010.01614.x)"
authors = "Alexander Dyck, Adair Morse, Luigi Zingales"
year = 2007
doi = "10.3386/w12882"
opened = "2026-11-27"

[source.dyck2017pervasive]
type = "preprint"
title = "How Pervasive Is Corporate Fraud? (working paper; published in Review of Accounting Studies 29(1), 2024, doi 10.1007/s11142-022-09738-5)"
authors = "Alexander Dyck, Adair Morse, Luigi Zingales"
year = 2017
url = "https://www.law.nyu.edu/sites/default/files/upload_documents/Adair%20Morse%20How%20Pervasive%20is%20Corporate%20Fraud.pdf"
opened = "2026-11-27"

[source.sec2026whistleblower]
type = "official-docs"
title = "Securities and Exchange Commission Office of the Whistleblower Annual Report to Congress for Fiscal Year 2025"
authors = "U.S. Securities and Exchange Commission, Office of the Whistleblower"
year = 2026
url = "https://www.sec.gov/files/fy25-annual-whistleblower-report.pdf"
opened = "2026-11-27"

[source.sec2024whistleblower]
type = "official-docs"
title = "Securities and Exchange Commission Office of the Whistleblower Annual Report to Congress for Fiscal Year 2024"
authors = "U.S. Securities and Exchange Commission, Office of the Whistleblower"
year = 2024
url = "https://www.sec.gov/files/fy24-annual-whistleblower-report.pdf"
opened = "2026-11-27"
```
