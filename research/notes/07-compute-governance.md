# Survey 07: compute governance and hardware

- **Track:** 07, compute governance and hardware.
- **Date:** 2026-11-27. Every source below was opened on this date (arXiv PDFs read as text, other pages
  fetched). Quotes are short and verbatim from the opened text; page or section is given where the
  text has one.
- **Scope:** catching large training runs (chip sampling, cloud and KYC oversight, workload
  classification), hardware-enabled mechanisms and operating licences (RAND offline licensing,
  flexHEG, firmware licensing), confidential computing and its physical breaks, location
  verification by latency, chip smuggling volumes and the Chip Security Act, decentralised and
  low-communication training, proof-of-learning and training-data proofs, international
  verification frameworks, and prior art for the memo's expiring k-of-n licence, sealed
  declarations and combined-channel guarantee.

**What matters most for Subcritical (including what contradicts the memo):**

1. The expiring chip licence renewed by k of n rival licensors is prior work. flexHEG (Petrie,
   Aarne et al. 2025) specifies k-of-n multilateral approval, licences that must be renewed
   periodically and are enforced by an on-chip clock or cycle counter, approvers that are major
   states or blocs, and update lifetimes ("for example three months"). Petrie 2024 and Sastry et
   al. 2024 came earlier. flexHEG also names the open problems: every chip locking down when
   approvers deadlock, an approver secretly signing a second lifetime extension, and the
   difficulty of proving that a licence was *not* issued. What may still be new is narrow: a
   Bitcoin block hash as the licence's freshness and clock, and a public log that cannot show two
   histories, which would answer the problems flexHEG leaves open.
2. The memo's combined miss probability cannot be a plain product of channel miss rates. Baker
   et al. 2025 argue that a rational evader goes around the weakest subgoal, so a regime's
   detection probability is about the *minimum* over subgoals. Channels multiply only when they
   cover the same subgoal and fail independently. On-chip channels share a common failure mode:
   TEE.fail (IEEE S&P 2026) used a DDR5 interposer costing under $1,000 to break the CPU
   attestation that NVIDIA GPU confidential computing trusts. I found no work that states one miss
   probability over breakout time across several channels. The closest is Gan 2026: Poisson
   detection inside a response window that shrinks as compute grows.
3. Training spread over many small clusters is happening now, not in some future scenario.
   Decentralised training compute is growing about 20x a year, against about 5x for the frontier
   (Epoch). Streaming DiLoCo needs 1-5 Gbit/s between sites for models of 1B to 100B parameters.
   INTELLECT-1 trained a 10B model across three continents, synchronising about every 38 minutes.
   The literature answers by tracking and licensing every chip rather than every facility (Scher
   and Thiergart; MIRI's draft treaty caps unmonitored clusters at 16 H100-equivalents).
4. Per-channel rates now exist to put into a combined model. Shavit's chip sampling needs about
   232 inspectors worldwide to catch a 10^25 FLOP run within 30 days with probability 0.9.
   Facility power metering detects at least 96% of undisguised runs at a 1% false-alarm rate, and
   at least 87% per day of the best disguise (simulated, 2026 preprint). Epoch's smuggling model
   assumes 25% of diversions are detected. Ping-based location verification reaches about
   country level (a 116-mile error radius).
5. Against the memo: the chip registry would start with a hole. Epoch estimates a median of
   660,000 H100-equivalents smuggled into China through 2025 (90% CI 290,000 to 1.6 million),
   about a third of China's compute, all outside any licence. In a 2026 DOJ case, dummy servers
   were allegedly staged to deceive auditors and a Commerce Department inspection. NVIDIA (2025) and the SIA (2026) publicly oppose kill
   switches, and flexHEG itself says a licence that lapses works as a remote off switch. Baker et
   al. call on-chip security "severe, unsolved".

## Sources

### shavit2023chinchilla
*What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training
via Compute Monitoring.* Yonadav Shavit, 2023. arXiv:2303.11341 (v2). Opened 2026-11-27.

- The design has three parts: chip firmware saves random snapshots of weight shards (with a hash),
  the trainer keeps transcripts that show how snapshotted weights were produced, and the supply
  chain is monitored so no one amasses untracked chips (abstract, Sections 3-5).
- Sampling bound, Eq. 1 (Section 3.2): the verifier samples s chips each period T_m. A run of H
  FLOP on chips with a FLOP/day uses at least H/(aT) of the stockpile C. Table 1 (p. 8) uses f =
  0.1 snapshots per day, p = 0.9 and T = 30 days. For Chinchilla (5.76e23 FLOP, 6.67e3 H100-days)
  it needs 132, 1.33e4 and 1.33e6 samples a year when C = 10^3, 10^5 and 10^7 chips.
- Footnote 5 (p. 8): with 10^7 chips worldwide at 3x H100 throughput, catching a 10^25 FLOP run
  within 30 days with probability 0.9 "would require roughly 232,000 worldwide chip samples per
  year". At 1,000 chips per inspector-year that is about 232 inspectors, "slightly smaller than the
  280 active IAEA inspectors as of 2021". Main text: for runs of 10^25 FLOP or more, monitoring
  "could be done with a bureaucracy similar in size to the IAEA".
- Appendix C.1 and Section 3.2: training longer on fewer chips does not help the evader, since
  each chip is sampled T/T_m times as often ("a < 5% increase" in evasion probability).
- Limitations (Section 1.2, p. 3): "the framework does not apply to small-scale ML training, which
  can often be done with small quantities of consumer GPUs". Legacy chips without the security
  features "present an implicit lower bound on the minimum training run size that can be
  verifiably detected". Colluding provers who each contribute a small fraction of their chips are
  handled only by treating every prover as one global stockpile (Section 3.2).
- Appendix A.2: the framework "does apply in the setting where clusters of chips are split across
  several datacenters", as long as each uses high-end chips. Consumer GPUs have much lower
  interconnect bandwidth (64 GB/s for an RTX 4090 against 900 GB/s for an H100 SXM).
- Bears on: verification channels (chip accounting and sampling), P1, P3, the failure mode
  "training spread across many small clusters", and declarations (weight-snapshot hashes).

### sastry2024compute
*Computing Power and the Governance of Artificial Intelligence.* Girish Sastry, Lennart Heim,
Haydn Belfield, Markus Anderljung, Miles Brundage and 14 others, 2024. arXiv:2402.08797. Opened
2026-11-27.

- Compute is "detectable, excludable, and quantifiable, and is produced via an extremely
  concentrated supply chain" (abstract; Section 3.B).
- Supply concentration (Section 3.B.4, pp. 28-29): NVIDIA has "a market share of over 90%" in data
  centre GPU design; in 2020 TSMC held about 90% of the pure-play foundry market at 10 nm and below
  (footnote 51); ASML is the sole EUV supplier.
- Footnote 36: a 20,000-H100 cluster at 10.2 kW per 8-GPU DGX "would consume more than 25 MW".
  Footnote 35: detectability "might be undermined should decentralized training, spread across
  many data centers and/or using lower-quality compute, become more viable".
- Section 4.C (Enforcement, pp. 56-58), the closest prior statement of the licence idea: "The
  authorization for the on-chip license could be periodically renewed by the regulator", and "An
  expired or illegitimate license would cause the chip to not work, or reduce its performance".
  Under "Preventing risky training runs via multiparty control" it proposes multisignature
  protocols so that chips "initiate processing instructions only when the workload is
  cryptographically signed by all parties", citing permissive action links. It warns this "could
  concentrate enormous power in the hands of every party that has the right to veto".
- Section 4.A proposes an international chip registry in which transfers "could be registered in a
  ledger, which could then be audited".
- Bears on: the compute section of the protocol (expiring licence, multiparty control), O1 and O3,
  P4, prior art.

### heim2024cloud
*Governing Through the Cloud: The Intermediary Role of Compute Providers in AI Regulation.* Lennart
Heim, Tim Fist, Janet Egan, Sihao Huang, Stephen Zekany, Robert Trager, Michael A. Osborne, Noa
Zilberman, 2024. arXiv:2403.08501. Opened 2026-11-27.

- Compute providers have four roles: securers, record keepers, verifiers of customer activity and
  enforcers (abstract).
- Workload classification (Section 3.3.2, pp. 23-24): frontier training has distinguishing
  features (accelerator counts in the tens of thousands, fairly constant utilisation, parallelism
  communication patterns, little external traffic). On the MIT Supercloud data (over 3,000
  accelerator workloads), "Workload classifiers trained on this data have reached 95% accuracy at
  distinguishing AI workloads across ten different model architectures". Classifiers using only
  power draw are cited as well.
- Evasion: customers could engage in "structuring", breaking up one workload as money launderers
  break up transactions (Section 3.3.2, p. 25).
- Footnote 29 (p. 27): a 10^26-operation run needs "around 60,000 cutting-edge AI accelerators
  (Nvidia H100) for 90 days, assuming a utilization of 34%" (the source's own arithmetic).
- Bears on: verification channels (cloud KYC, workload classification), the failure mode
  "training spread across many small clusters" (structuring).

### egan2023kyc
*Oversight for Frontier AI through a Know-Your-Customer Scheme for Compute Providers.* Janet Egan,
Lennart Heim, 2023. arXiv:2310.13625. Opened 2026-11-27.

- Proposes KYC for compute providers in four steps: a dynamic compute threshold, record keeping
  and reporting, government capacity, and international engagement (abstract). Regulating digital
  access gives "the flexibility to suspend access".
- The threshold "should be defined by the total amount of computational operations" and "would
  need to be dynamic", lowered as algorithms improve (Section 2.1). Compute bought from several
  vendors over time must still be caught before the threshold is crossed. Structuring to evade
  public thresholds is discussed by analogy with banking.
- Bears on: compute limits (dynamic thresholds), verification channels (cloud), failure modes
  (structuring across providers).

### kulp2024hem
*Hardware-Enabled Governance Mechanisms: Developing Technical Solutions to Exempt Items Otherwise
Classified Under Export Control Classification Numbers 3A090 and 4A090.* Gabriel Kulp, Daniel
Gonzales, Everett Smith, Lennart Heim, Prateek Puri, Michael J. D. Vermeer, Zev Winkelman. RAND
working paper WR-A3056-1, 2024. doi:10.7249/WRA3056-1. Opened 2026-11-27 (PDF).

- Offline Licensing "would enforce renewable licenses that temporarily authorize the use of certain
  AI hardware features". Example: "a license could authorize 10^18 arithmetic operations, and, once
  these are expended, the GPU could fall back to 1 percent of its full computational performance"
  (Summary, p. viii). Licences need no network connection. Who issues them is left open: the GPU
  designer, a US government body, "or an international institution".
- Fixed Set limits high-bandwidth links to a preauthorised pod ("fewer than 65 chips") and caps
  bandwidth outside it, to stop aggregation into a supercomputer (Summary).
- Cost imposition (Chapter 2, p. 10): if circumvention costs $5,000 per chip with 50% success, on a
  $25,000 H100, the effective cost is $60,000 per chip, "which is only 2.4 times the original cost
  and may not be enough to deter a well-resourced adversary".
- Bears on: the compute section of the protocol (licences that expire by usage), the defection
  bound, hardware security assumptions.

### petrie2024offline
*Near-Term Enforcement of AI Chip Export Controls Using A Firmware-Based Design for Offline
Licensing.* James Petrie, 2024. arXiv:2404.18308 (v2). Opened 2026-11-27.

- Offline licensing "works by disabling AI chips unless they have an unused license from a
  regulator". "Existing AI chips could potentially support Offline Licensing within a year" if they
  have firmware verification, rollback protection and secure non-volatile memory, which H100
  documentation suggests it has (abstract).
- Licences count clock cycles and name a chip and a licence ID. They are signed with "the private
  key(s) of the appropriate regulator(s)" (Section 2).
- Freshness (Section 3.2, p. 5): instead of trusting a local record, a chip can issue a usage
  request "containing some random data to prevent replay attacks" that a regulator signs. That is
  a chip nonce, which already stops licences being signed in advance.
- Section 3.7 (p. 6): to survive a leaked regulator key, "require multiple different regulators to
  sign each license, or potentially a fraction of approved regulators", with two thirds as the
  example.
- Firmware-only versions are "susceptible to physical hardware attacks" (abstract).
- Bears on: prior art for the k-of-n licence and freshness, hardware security.

### aarne2024securechips
*Secure, Governable Chips: Using On-Chip Mechanisms to Manage National Security Risks from AI &
Advanced Computing.* Onni Aarne, Tim Fist, Caleb Withers. CNAS, January 2024. Opened 2026-11-27 (PDF).

- Operating licences "would be best enabled using a dedicated 'security module' that links the
  functioning of the chip to a periodically renewed license key" (Executive summary).
- Adequate hardware security "could be achieved with as little as 18 months of involved technical
  effort (and up to 4 years) from leading firms" (p. 4).
- Latency geolocation: from Paris, a chip that answers in under 9 ms cannot be in Russia, since
  Kaliningrad is "9*15 = 1350 km from Paris" at the speed of light. Ordinary internet paths are
  slower, so landmark servers "spaced a few hundred kilometers apart" are needed.
- Bears on: the compute section of the protocol (licences), location verification, hardware
  timelines.

### petrie2025flexheg1
*Flexible Hardware-Enabled Guarantees for AI Compute* (flexHEG Part I). James Petrie, Onni Aarne,
Nora Ammann, David Dalrymple, 2025. arXiv:2506.15093. Opened 2026-11-27.

- Rulesets can be updated by anyone "from simply the owner of the chip up to a quorum of states"
  (summary).
- Operating licences (p. 33): "This license could be time-limited, to ensure that it can
  effectively be revoked by refusing to issue a renewed license". Footnote 22: this "is in fact the
  only reliable way to implement any kind of remote 'off switch'". An unexpired licence required
  for general use makes the requirement "effectively a remote off-switch".
- p. 34: licences "could be required to be signed by all or a majority of some set of governments,
  to ensure international accountability". Location restrictions can trust "multiple different
  states' landmarks".
- p. 34, an open problem: "Verifying that a particular type of license has not been issued is more
  technically challenging". Showing that a device has no licence would let states know it is not
  operating.
- Bears on: prior art for the expiring k-of-n licence; an opening for a public licence log.

### petrie2025flexheg2
*Technical Options for Flexible Hardware-Enabled Guarantees* (flexHEG Part II). James Petrie, Onni
Aarne, 2025. arXiv:2506.03409. Opened 2026-11-27.

- Guarantee update process (pp. 36-37): "The update process could require that the update (or lack
  of update) be multilaterally approved by k of n parties, so that no single actor could
  unilaterally impose excessive restrictions". Algorithm 1 gives pseudocode for k-of-n signature
  checking. Different updates can require different quorums, and signatures should be
  quantum-resistant.
- Enforced updates (p. 38): "require that accelerators periodically receive a license in order to
  continue operating", each naming a minimum firmware version. The chip stops if it runs too long
  "(as measured by a secure real-time clock or cycle counter)" without one. Example period: "a new
  license every three months". Footnote 14: "If using a cycle counter, there is a risk that the
  operator secretly does not use the chip to save up usage time."
- A public blockchain appears in passing (p. 34, multi-accelerator FLOP counting). To enforce a
  delay before restarting from a checkpoint, an auditor could attest to having seen a hash earlier,
  "or instead of an auditor, the presence of that hash in the history of a public blockchain could
  be used". Example: with a 10^26 FLOP cap and a 3-month delay, reaching 10^27 FLOP sequentially
  needs 10 restarts and "at least 30 months".
- Hardware performance counters could give FLOP counts and interconnect utilisation. A
  multilaterally maintained attestation service is suggested.
- Bears on: prior art for the k-of-n expiring licence and for blockchain anchoring; the memo's
  "chip's own counter ends the licence period" (footnote 14 critique).

### aarne2025flexheg3
*Flexible Hardware-Enabled Guarantees, Part III: International Security.* Onni Aarne, James
Petrie, 2025. arXiv:2506.15100. Opened 2026-11-27.

- Mutual veto (p. 32): "give each bloc of participating states the ability to disable much of
  others' AI compute through some type of operating license mechanism".
- Proposed configuration (p. 46): "Firmware updates, i.e. rule changes, need to be signed by all of
  some set of approvers", where the approvers are "major states or groups of states". Updates have
  limited lifetimes, "for example three months". A fraction of approvers can extend the current
  lifetime. A k-of-n supermajority is analysed as the alternative (p. 47). Any major state without
  enough votes to block "could potentially" be colluded against.
- p. 48: "If no new update has been installed before the lifetime runs out, the device locks down."
  Failed negotiations mean "all flexHEG devices would simply lock down". An approver who has broken
  the mechanism on its own chips could refuse to sign and so disable everyone else's.
- p. 49, equivocation: an approver could secretly sign a lifetime extension for the old firmware
  while everyone adopts the new one. Remedies include sequential serial numbers or timestamps
  enforced inside each approver's own guarantee processor. "The details of how exactly such a
  system would work are a topic for further research."
- Bears on: the compute and defection sections of the protocol, prior art. These are the hold-up
  risks of expiring licences, which the memo does not yet address.

### nvidia2023hcc
*Confidential Compute on NVIDIA Hopper H100* (whitepaper WP-11459-001, v1.0). NVIDIA, July 2023.
Opened 2026-11-27.

- Each H100 has a "device-unique ECC-384 key pair". The "private Identity Key (IK) is burned into
  fuses of each H100; the public key is retained, but all copies of these private keys are
  destroyed during the manufacturing process". Revocation is checked against a CRL.
- Threat model (Figure 6, p. 14): in scope are software, "Basic physical attacks", rollback and
  replay. **Out of scope:** "Sophisticated Physical attacks" and denial of service. Goal: interposers
  on PCIe and DDR "cannot leak data or code".
- Bears on: hardware attestation as a verification channel, and its stated limits against an
  adversary with physical access (a state).

### chuang2026teefail
*TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition.* Jalen
Chuang, Alex Seto, Nicolas Berrios, Stephan van Schaik, Christina Garman, Daniel Genkin. IEEE S&P
2026. https://tee.fail/ (paper PDF from the project site). Opened 2026-11-27.

- The attack works "in under $1000" with a DDR5 bus interposer. It extracts attestation keys
  from Intel TDX (the PCE's ECDSA keys) and from AMD SEV-SNP with ciphertext hiding.
- NVIDIA (Section 8.2): "As NVIDIA does not bind the H100 to identities of specific VMs", a forged
  TDX quote plus an H100 attestation fetched from a rented server passes both checks. A user "is
  (incorrectly) cryptographically convinced" that work runs inside a TEE with NVIDIA confidential
  computing. With this attack "a provider could multiplex a single H100 to provide attestations for
  hundreds of instances".
- Vendor responses (project page): Intel and AMD treat interposers as out of scope with no
  mitigation planned. The authors say no NVIDIA-side mitigation exists because TEE.fail does not
  attack NVIDIA's elements directly.
- Bears on: the independence of channels. Attestation, attested latency and on-chip licences share
  one trust anchor. Chip accounting by attestation can be inflated by multiplexing.

### baker2025sixlayers
*Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI
Development and Deployment.* Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart
Heim, 2025. arXiv:2507.15916. Opened 2026-11-27.

- States "could eventually verify compliance by using six largely independent verification
  approaches with substantial redundancy": on-chip features, two off-chip layers (network taps,
  analog sensors) and three personnel layers including whistleblowers (abstract). The scope is
  development that uses "thousands of high-end AI chips".
- Two subgoals: declared compute is used compliantly, and nothing is undeclared, including
  "decentralized collections of AI chips" (Section 3.2).
- **Weakest link** (footnote 33, p. 17): "a verification regime's probability of detecting a
  violation is approximately that of the subgoal with the lowest probability of detecting a
  violation", because a rational prover circumvents the weakest subgoal. The heuristic ignores small
  violations spread across subgoals, "which may involve a lower or higher probability of detection,
  depending on the detection probabilities and their correlation". A layer covers every subgoal
  once, so "three verification layers can be stacked together to achieve three layers of
  redundancy" (Section 4).
- Table 6 (p. 22): "On-chip verification faces severe, unsolved hardware security challenges".
  Security track records are "mixed at best", security practices are lacking, and performance
  trades against security.
- Footnote 72 (Section 4.4, p. 32): highly effective decentralised training on consumer electronics
  "would undermine the on-chip and off-chip verification layers"; personnel layers could remain
  effective since "extremely decentralized networks would likely involve many accomplices".
- Footnote 44: offline licensing can be configured "so that the Verifier has visibility but not
  veto power". Cites 1.5-2 million H100 shipments in 2024 against 0.5 million in 2023.
- Bears on: the combined-channel guarantee (structure and correlation), verification channels,
  the failure mode "training spread across many small clusters".

### wasil2024verification
*Verification methods for international AI agreements.* Akash R. Wasil, Tom Reed, Jack William
Miller, Peter Barnett, 2024. arXiv:2408.16074 (v2). Opened 2026-11-27.

- Ten methods in three groups. National technical means: remote sensing, whistleblowers, energy
  monitoring, customs data, financial intelligence. Access-dependent: inspections of data centres,
  fabs and AI developers. Hardware-dependent: chip location tracking, chip-based reporting
  (Executive Summary).
- "No single method is foolproof. However, the combination of multiple methods could create a
  'Swiss chees' [sic] model". The combination is qualitative only, with no detection rates or miss
  probabilities.
- Recommends red-teaming verification regimes.
- Bears on: verification channels, prior art for the combined-channel guarantee.

### harack2025oxford
*Verification for International AI Governance.* Ben Harack, Robert F. Trager, Anka Reuel, David
Manheim, Miles Brundage, Onni Aarne, Aaron Scher and others. Oxford Martin AI Governance
Initiative, July 2025 (172 pp.). Opened 2026-11-27 (PDF).

- It assumes pessimistic technical and political conditions. Even so, "verifying the regulation of
  data center-based AI development and deployment appears to be possible within a few years if
  serious efforts are made", using narrow-purpose verification hardware and "a mutually verified
  data center" (abstract).
- Appendix L.5, "Model tenancy ledger attestation": hardware writes "model fingerprints and
  timestamps for all operations that load models into memory" to non-volatile memory. Whether
  this "can be robustly secured other than relying on the hardware private key" is unclear. It
  cites blockchain-pegged IC traceability (Islam and Kundu 2019) for chip identity.
- Bears on: declarations (on-device logs as prior art), verification channels.

### scher2024mechanisms
*Mechanisms to Verify International Agreements About AI Development.* Aaron Scher, Lisa Thiergart
(MIRI), November 2024. arXiv:2506.15867. Opened 2026-11-27.

- Locating compute should rely on "tracking AI chips and their supply chain rather than hoping to
  detect secret data centers", because "advances in distributed training will allow many data
  centers to effectively act as one" (Executive Summary).
- "distributed training likely poses significant issues for compute exclusion because it could
  enable multiple small-to-medium amounts of compute (e.g., 5,000 chips) to collectively carry out a
  large training run". It "may be necessary to monitor even relatively small data centers".
- Offline licensing could work "similarly to general software licensing, where a regulator issues
  an AI chip a license for some period of time or amount of compute and renews the license".
- Bears on: the failure mode "training spread across many small clusters", the compute section of
  the protocol (chip-level rather than site-level licensing).

### scher2025agreement
*An International Agreement to Prevent the Premature Creation of Artificial Superintelligence.*
Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance Team), 2025.
arXiv:2511.10783 (v2). Opened 2026-11-27.

- The draft treaty "halts dangerous AI capabilities advancement while preserving access to current,
  safe AI applications" (abstract). Its goal overlaps closely with Subcritical's.
- Thresholds (Article IV and definitions): training above 10^24 FLOP (Strict Threshold) is
  prohibited. Runs between 10^22 (Monitored Threshold) and 10^24 are approved and monitored.
  Post-training is capped at 10^23. An H100-equivalent is 990 TFLOP/s FP16.
- Article V, chip consolidation: no clusters "greater than 16 H100-equivalents" outside monitored
  facilities, which cost "approximately $500,000 USD in 2025" (p. 6). "The 16 H100 threshold is
  likely to be challenging, and is picked partially due to the increasing infeasibility of still
  lower thresholds", and it may need to fall to 8 (p. 28). A 10^22 run on 16 H100s takes "around
  one week" (p. 25).
- Algorithmic progress: training compute for a given capability "drops by 3x each year", so the
  monitored cluster size would also have to fall 3x a year (p. 8). Hence Article VIII's research
  restrictions.
- It discusses breakout time only qualitatively: decommissioning chips might lengthen breakout "a
  decade or more", which the authors judge not worth the cost.
- Bears on: the whole protocol (closest prior treaty), compute limits, D3 and D4 (breakout is used
  informally, not computed), the failure mode "algorithmic progress".

### miotti2023cap
*An international treaty to implement a global compute cap for advanced artificial intelligence.*
Andrea Miotti, 2023 (v2 2025). arXiv:2311.10748. Opened 2026-11-27.

- Treaty with a Moratorium Threshold that "will start at 10^24 Floating-Point Operations" and a
  Danger Threshold at "10^21 FLOP", to be lowered as algorithms improve (Article 2-3). It also
  includes whistleblower protections and an enforcement agency.
- Bears on: prior art for compute caps in a treaty.

### gan2026clock
*Agreements Have a Clock: Compute Growth and the Verification of AI Restraint.* Li Gan, November
2026. arXiv:2611.04272 (econ.GN). Opened 2026-11-27.

- Detection is Poisson. A country that secretly advances "is caught within its window with
  probability 1 - e^(-m w_i)", with m findings per month and w_i the response window
  (Section 4.3.4, p. 15). Deterrence needs m >= xi_i / w_i, and participation needs m <= (C_i -
  R_i)/eta_i, where eta_i is the monitoring cost (Proposition 4).
- "As compute grows during a pause, a secret advance reaches the frozen frontier sooner, shrinking
  the response window: agreements have a clock" (abstract). In the example, cooperation holds to
  month 18.9, to 25.5 with verified matched safety research, and to 31.8 with half the monitoring
  cost.
- "Deterrence does not require near-certain detection". With a 12-month window, m = 0.0319
  findings a month suffices, which means a "32 percent" chance of detection in the window and a
  mean of "about 31 months" to a finding (p. 16).
- One aggregate monitoring rate m; no decomposition into channels.
- Bears on: the combined-channel guarantee (closest quantitative prior work), D3 and D4 (response
  window against breakout), defection.

### allison2025nuclear
*Artificial Intelligence and Nuclear Weapons Proliferation: The Technological Arms Race for
(In)visibility.* David M. Allison, Stephen Herzog. Risk Analysis, 2025. doi:10.1111/risa.70105
(also arXiv:2512.07487). Opened 2026-11-27.

- The risk of a covert programme escaping detection over a horizon T is R(T) = integral of
  lambda(t)[1 - Pr(D_t)] dt, with P(10) = 1 - e^(-R(10)) as "the probability of at least one
  undetected clandestine weaponization program". Detection is calibrated with kappa = 0.4 to
  "IAEA safeguards modeling standards, which target a ~90% detection probability for significant
  material diversions" (Section 3). Section 4 calls the Poisson process a "tractable modeling
  assumption" and says real proliferation decisions "are not truly independent events".
- Bears on: the combined-channel guarantee (the safeguards-style miss model over a horizon).

### feldgoise2026tracking
*Tracking AI Chips: Assessing Location Verification as an Export Control Enforcement Tool.* Jacob
Feldgoise, Kyle Miller, Hanna Dohmen. CSET issue brief, September 2026. Opened 2026-11-27 (PDF).

- Recommends a "centralized, ping-based location verification (PLV) system", supplemented by
  physical inspections to follow up leads (Executive Summary, p. 1).
- Cost (p. 2): "roughly $3.1 million to $28.8 million annually if the landmark servers are owned and
  $2.6 million to $72.4 million annually if they are rented". That is 0.5% to 7.2% of BIS's FY2026
  budget if owned. In over ten million simulated scenarios, physical inspections never beat PLV on
  detections per cost.
- Limits (p. 2). PLV "can only detect diversion after it has already occurred". Offline chips are
  ambiguous. "Well-resourced adversaries could trick a PLV system". With landmarks at major
  data-centre hubs, accuracy is about country level, "an error-circle radius of 116 miles", and
  "no better than about 20 miles" at best. It cannot detect a change of end user at the same
  location.
- Chip Security Act status (Introduction): the House Foreign Affairs Committee advanced it on 26 March 2026,
  and it may enter the FY2027 NDAA. In March 2026 the Semiconductor Industry Association formally
  opposed it, warning of "complex, costly, and unproven security features". NVIDIA Fleet
  Intelligence telemetry (IP and MAC addresses) "can be readily spoofed" (Appendix).
- Bears on: the location verification channel (accuracy, cost, spoofing), political feasibility.

### brass2024location
*Location Verification for AI Chips.* Asher Brass, Onni Aarne. Institute for AI Policy and Strategy
(IAPS), 2024 (authorship from the IAPS research page; the PDF carries no byline). Opened 2026-11-27.

- "Delay-based schemes appear to be the most promising approach", difficult to spoof but "much less
  precise than GPS" (Executive Summary). Pure-software delay-based solutions "would likely cost less
  than $1,000,000 to set up and maintain for several years".
- Delay-based methods give "broad positioning information (~10km-~1,000km)" (p. 4). GPS can be
  spoofed for about $200. Detecting large clusters "would be impractical if the geolocation in
  question is larger than several kilometers".
- Bears on: the location verification channel; latency cannot see clusters or co-location.

### nvidia2025fleet
*Opt-In NVIDIA Software Enables Data Center Fleet Management.* NVIDIA Newsroom, 10 December 2025.
Opened 2026-11-27.

- "an opt-in, customer-installed service" that monitors "GPU usage, configuration and errors",
  including power spikes, utilisation, memory bandwidth and interconnect health. The client agent
  is "slated to be open sourced". "NVIDIA GPUs do not have hardware tracking technology, kill
  switches and backdoors."
- Bears on: location verification as deployed by the vendor (voluntary), power telemetry.

### reuters2025nvidialocation
*Nvidia builds location verification tech that could help fight chip smuggling.* Reuters,
republished by The Star, 11 December 2025. Opened 2026-11-27.

- The software "could indicate which country its chips are operating in". It uses the GPUs'
  confidential computing features and "the time delay in communicating with servers run by Nvidia".
  It "will first be made available on Nvidia's latest" Blackwell chips, which have stronger
  attestation than Hopper and Ampere. It is optional. Telemetry is "read only", and there is "no
  kill switch".
- Bears on: location verification. Its security rests on the same attestation that TEE.fail
  undermines.

### nvidia2025nobackdoors
*No Backdoors. No Kill Switches. No Spyware.* David Reber Jr. (NVIDIA Chief Security Officer), NVIDIA
Blog, 5 August 2025. Opened 2026-11-27.

- "NVIDIA GPUs do not and should not have kill switches and backdoors." "Kill switches and built-in
  backdoors create single points of failure." "optional software features, controlled by the user,
  are not hardware backdoors."
- Bears on: political feasibility of licences that disable chips when they lapse. The dominant
  vendor's position is directly opposed.

### chipsecurityact2025
*Chip Security Act,* H.R. 3447, 119th Congress (introduced 15 May 2025).
Opened 2026-11-27 (govinfo text).

- Sec. 4(a)(1): "Not later than 180 days after the date of the enactment", Commerce must require
  covered products "to be outfitted with chip security mechanisms that implement location
  verification". Covered products are ECCN 3A090, 3A001.z, 4A090 and 4A003.z, and successors
  (Sec. 3(3)).
- Sec. 4(a)(2): licensees must promptly report credible information that a product is elsewhere,
  diverted, or "subjected to tampering or an attempt at tampering". Sec. 4(b): within one year,
  assess additional mechanisms, and require them within two years of the assessment if warranted.
- Bears on: legal precedent for mandated chip security mechanisms. It requires location only, not
  licensing or disablement.

### grunewald2025smuggling
*Countering AI Chip Smuggling Has Become a National Security Priority: An Updated Playbook for
Preventing AI Chip Smuggling to the PRC.* Erich Grunewald, Tim Fist. CNAS, 11 June 2025. Opened
2026-11-27 (web page).

- Estimated 2024 smuggling: about 10,000 to several hundred thousand chips, median about 140,000,
  from a probabilistic model, "a high-level distribution of possible outcomes, rather than a
  summation of confirmed smuggling cases". At the median, smuggled chips are 1-40% of PRC training
  compute (median 10%) and 1-30% of inference (median 6%).
- Cases: an order for 2,400 H100s ($120 million), and three people arrested in Singapore over $390
  million of servers. Profits from three cases (about $140 million) are more than double BIS's
  annual export enforcement budget (about $55 million; endnote 12). Recommends software location verification so an
  owner can "prove that the chip is not located in the PRC", whistleblower and qui tam programmes,
  and BIS funding ($313 million requested for FY2026 against $191 million).
- Bears on: the chip accounting channel's real miss rate, rewarded whistleblowing.

### juniewicz2026smuggling
*Diversion and resale: estimating compute smuggling to China.* Isabel Juniewicz, Epoch AI, 29 April
2026. Opened 2026-11-27 (web page).

- Cumulative through 2025: median 660,000 H100e (90% CI 290,000 to 1.6 million), "roughly a third
  of China's total compute" and "roughly 3% of the global compute stockpile". Diversion-side median
  about 530,000 H100e; resale-side about 700,000 H100e.
- "Cumulative allegations of diverted or missing chips total almost 300,000 H100e by the end of
  2025". The model's detection rate for diversion cases has a median of 25% (90% CI 10-80%). That
  is an assumption, but it is the only explicit per-channel detection rate I found for chip
  accounting.
- By year: 159k H100e (2024) and 480k H100e (2025). It restates the CNAS 2024 estimate as about
  140,000 chips (90% CI 20,000-800,000).
- Bears on: chip accounting (a hole in any registry from the start), the miss rate for that channel,
  O1.

### doj2026supermicro
*Three Charged with Conspiring to Unlawfully Divert Cutting Edge U.S. Artificial Intelligence
Technology to China.* US Department of Justice, Office of Public Affairs, 19 March 2026. Opened
2026-11-27.

- Allegations (not proven): a Southeast Asian company bought about $2.5 billion of servers in
  2024-2025, and at least about $510 million was diverted to China between late April and mid-May
  2025. The defendants "staged thousands of 'dummy' servers" to deceive auditors and a Commerce
  Department inspection. The servers were routed via Taiwan and Southeast Asia in unmarked boxes.
- Bears on: challenge inspections can be fooled by decoys; chip accounting needs chip-level
  identity, not box counts.

### douillard2023diloco
*DiLoCo: Distributed Low-Communication Training of Language Models.* Arthur Douillard, Qixuan Feng,
Andrei A. Rusu, Rachita Chhaparia, Yani Donchev, Adhiguna Kuncoro, Marc'Aurelio Ranzato, Arthur
Szlam, Jiajun Shen (Google DeepMind), 2023. arXiv:2311.08105 (v3). Opened 2026-11-27.

- Trains "on islands of devices that are poorly connected". "DiLoCo on 8 workers performs as well
  as fully synchronous optimization while communicating 500 times less" (abstract). It is robust
  to workers joining and leaving. Inner steps H = 500. Models up to 400M parameters.
- Bears on: P3 (interconnect is no longer a hard bound), the failure mode "training spread across
  many small clusters".

### douillard2025streaming
*Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch.* Arthur
Douillard, Yanislav Donchev, Keith Rush, Satyen Kale, Zachary Charles and others (Google DeepMind,
Google Research), 2025. arXiv:2501.18512. Opened 2026-11-27.

- Synchronises fragments of parameters in sequence, overlaps communication with compute, and
  quantises to 4 bits, "reducing required bandwidth by two orders of magnitude" (abstract).
- Figure 4: it "reaches a compute utilization of 95% for models 1B, 10B, and 100B with a bandwidth
  roughly constant between 1 and 5 Gbit/s", whereas data parallelism "requires 100, 200, and
  300Gbit/s".
- Table 1 (1B model, Dolma): "exchanging in total 400x fewer bits, reducing the peak bandwidth by
  8x". 1.10 TB exchanged against 441 TB at 25B tokens.
- Bears on: P3, footprint (inter-site links of a few Gbit/s look like ordinary traffic), failure
  modes.

### jaghouar2024intellect1
*INTELLECT-1 Technical Report.* Sami Jaghouar, Jack Min Ong, Manveer Basra, Fares Obeid, Jannik
Straube, Michael Keiblinger and others (Prime Intellect et al.), 2024. arXiv:2412.01152. Opened
2026-11-27.

- "the first 10 billion parameter language model collaboratively trained across the globe", on "1
  trillion tokens using up to 14 concurrent nodes distributed across 3 continents, with
  contributions from 30 independent compute providers", at "83-96% compute utilization and
  36.2-41.4% model FLOPS utilization" (abstract). Up to 112 H100s at once across five countries
  (Section 1).
- "a 400x reduction in communication bandwidth" with DiLoCo and int8 all-reduce. Inter-node
  bandwidth "limited to 500 Mb to 4 Gb/s". Nodes run "approximately 38 minutes before performing an
  all-reduce operation, which takes around 1 to 7 minutes".
- Bears on: the failure mode "training spread across many small clusters" (a demonstrated case),
  P3.

### primeintellect2025intellect2
*INTELLECT-2: A Reasoning Model Trained Through Globally Decentralized Reinforcement Learning.* Prime
Intellect Team (Sami Jaghouar, Justus Mattern, Jack Min Ong and others), 2025. arXiv:2505.07291.
Opened 2026-11-27.

- "the first globally distributed reinforcement learning (RL) training run of a 32 billion parameter
  language model", using asynchronous RL "across a dynamic, heterogeneous swarm of permissionless
  compute contributors" (abstract). TOPLOC "verifies rollouts from untrusted inference workers".
  Rollout workers include consumer GPUs (3090s appear in Figure 1). The training nodes themselves
  are centralised.
- Bears on: A2 and the continual learning pathway. RL post-training puts most of its compute into
  inference that runs on unregistered hardware.

### peng2024demo
*DeMo: Decoupled Momentum Optimization.* Bowen Peng, Lizhang Chen, Baiyu Su, Jeffrey Quesnelle,
Diederik P. Kingma, Qiang Liu, 2024 (v2 February 2026). arXiv:2411.19870. Opened 2026-11-27.

- "reduces per-step communication by up to two orders of magnitude". On 300M and 1B models "DeMo
  transmits up to 85x less data per GPU than AdamW-DDP while achieving comparable loss". It
  "enables training across multi-datacenter or Ethernet-based setups" (abstract). This is the basis
  of Nous Research's DisTrO.
- Bears on: P3, failure modes.

### nous2025psyche
*Democratizing AI: The Psyche Network Architecture.* Nous Research, 14 May 2025. Opened 2026-11-27.

- "Psyche reduces data transfer by several orders of magnitude". "Coordination happens on the
  Solana blockchain". The first run "will pretrain a 40B parameter model using the Multi-head
  Latent Attention (MLA) architecture across 20T tokens" (Consilience). It starts with a permissioned
  testnet, aiming to let "anyone to participate".
- Bears on: failure modes. Decentralised training already uses a public blockchain for its own
  coordination, which a regulator could also watch.

### ryabinin2023swarm
*SWARM Parallelism: Training Large Models Can Be Surprisingly Communication-Efficient.* Max
Ryabinin, Tim Dettmers, Michael Diskin, Alexander Borzunov. ICML 2023. arXiv:2301.11913. Opened
2026-11-27.

- Model-parallel training on "poorly connected, heterogeneous and unreliable devices". As models
  grow, "training larger models becomes less communication-intensive" (compute per layer grows
  faster than activations). A model with "1B shared parameters (~13B before sharing)" was trained
  "on preemptible T4 GPUs with less than 200Mb/s network" (abstract).
- Bears on: P3, failure modes (pipeline parallelism over the internet, not only data parallelism).

### sevilla2025decentralized
*How far can decentralized training over the internet scale?* Jaime Sevilla, Epoch AI (Gradient
Updates), 29 December 2025. Opened 2026-11-27.

- Decentralised training compute grew about 20x a year since 2020, against about 5x for the
  frontier. The largest decentralised pretraining runs are 6e22 to 6e23 FLOP (INTELLECT-1, Pluralis
  Protocol Model 8B, Nous Consilience 40B), about 1,000x below the frontier. Covenant AI's Templar
  has about 9e17 FLOP/s, about 300x below frontier sites at about 3e20 FLOP/s.
- Typical consumer upload is about 60 Mbps. DiLoCo-style methods give up to 500x fewer
  synchronisations; streaming DiLoCo with 4-bit gradients about 100x over naive data parallelism.
  Scaling from 1 to 8 nodes costs about 1.5x in compute, and 10,000 nodes extrapolate to about 6x.
- If trends held, catching up would take about 5.5 years. The author expects "we won't see
  decentralized training runs catch up to the frontier of training in scale this decade". He
  warns that monitoring proposals which assume decentralised training keeps lagging would be
  caught out if that assumption breaks.
- Bears on: the failure mode "training spread across many small clusters" (a timescale), P3, P4.

### krys2025distributed
*Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI
Landscape.* Jakub Krys, Yashvardhan Sharma, Janet Egan, 2025. arXiv:2507.07765. Opened 2026-11-27.

- It distinguishes distributed training (hyperscalers spanning sites) from decentralised training
  (community-run, no central control). Decentralised start-ups have raised "around $145 million".
  The risks are "compute structuring", proliferation, and "the erosion of detectability and
  shutdownability" (abstract, p. 1).
- Structuring (p. 4): an actor "could divide their training run into several smaller workloads
  that are executed in parallel using different cloud providers". INTELLECT-1 synchronised "only
  once every 38 minutes, and it is possible to purposefully prolong it by up to several training
  steps, thereby obfuscating any characteristic patterns". "work on KYC schemes and workload
  monitoring is not progressing at an adequate pace".
- Bears on: failure modes, cloud verification channels.

### erdil2024datamovement
*Data Movement Limits to Frontier Model Training.* Ege Erdil, David Schneider-Joseph, 2024.
arXiv:2411.01137 (v2). Opened 2026-11-27.

- With a three-month run, "data movement bottlenecks begin to significantly lower hardware
  utilization for training runs exceeding about 10^28 FLOP", and "A training run exceeding about
  10^31 FLOP is infeasible even at low utilization" (abstract).
- Bears on: P3, P1 (an upper physical bound on single runs, far above any likely cap).

### long2024protocol
*Protocol Learning, Decentralized Frontier Risk and the No-Off Problem.* Alexander Long (Pluralis
Research), 2024. arXiv:2412.07890. Opened 2026-11-27 (abstract and introduction).

- Decentralised "Protocol Learning" could "aggregate orders of magnitude more computational
  resources than any single centralized entity". It names the "No-Off Problem", "the inability to
  unilaterally halt a collectively trained model".
- Bears on: failure modes, the closed-loop and shutdown assumptions.

### jia2021pol
*Proof-of-Learning: Definitions and Practice.* Hengrui Jia, Mohammad Yaghini, Christopher A.
Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot. IEEE S&P
2021. arXiv:2103.05633. Opened 2026-11-27.

- Proposes logging training checkpoints so that a verifier can re-execute some steps. Their
  experiments suggest that forging a proof costs "at least as much work than is needed for gradient
  descent itself" (abstract). The security argument is empirical, not formal.
- Bears on: declarations (proving how checkpoints were produced).

### fang2023polbroken
*Proof-of-Learning is Currently More Broken Than You Think.* Congyu Fang, Hengrui Jia, Anvith Thudi,
Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Varun Chandrasekaran, Nicolas
Papernot, 2023. arXiv:2208.03567 (v2). Opened 2026-11-27.

- Introduces spoofing strategies that reproduce "across different configurations of the PoL
  verification" at "a fraction of the cost". Concludes "one cannot develop a provably robust PoL
  verification mechanism without further understanding of optimization in deep learning"
  (abstract).
- Bears on: declarations. Sealed logs can stop backdating, but not false training transcripts.

### choi2023potd
*Tools for Verifying Neural Models' Training Data.* Dami Choi, Yonadav Shavit, David Duvenaud, 2023.
arXiv:2307.00682. Opened 2026-11-27.

- Defines "Proof-of-Training-Data". The trainer verifiably pre-commits to a random seed, and the
  verifier exploits "models' tendency to temporarily overfit to training data". The procedures
  "can catch a wide variety of attacks, including all known attacks from the Proof-of-Learning
  literature" (abstract). The guarantee is experimental.
- Bears on: declarations (pre-commitment is the step that a sealed, timestamped log makes
  credible), verification of training runs.

### kimpson2026dcpower
*Detecting AI Training in Datacentre Power.* Tom Kimpson, Mauricio Baker, Emlyn Graham, October
2026. arXiv:2610.30182. Opened 2026-11-27.

- Viterbi tracking of the iteration cadence in facility-level power. On simulated data-centre power,
  with no attempt to hide, it detects "at least 96% of training runs against a declared inference
  workload, at a 1% false-alarm rate", using a meter at "2 Hz or faster" (abstract).
- Of eight evasion strategies, only extreme variation of work per iteration evades it. "Its
  strongest form hides training in up to 73% of five-minute observations, but over a day at least
  87% of such runs are still caught, at a 0.1% false-alarm rate per run". In small-scale training
  the evader "needs 93-267% more compute to reach the same loss".
- Bears on: the power and heat signature channel (detection rate and the cost of evasion), but only
  at metered, declared sites.

### kimpson2026supply
*Verifying Declared AI Workloads from GPU Supply Current.* Tom Kimpson, November 2026.
arXiv:2611.29982. Opened 2026-11-27.

- 23.4 h of Rogowski-coil current under idle, training and inference. "a one-class model fitted to
  the current draw of permitted, declared work (idle and inference) flags at least 99.9% of windows
  of prohibited training", including five evasion strategies. As a continuous monitor it "detects
  all 188 episodes" of training hidden by timesharing, with a median delay of 3.0 s and one alarm
  in 8.8 h (abstract).
- Failure: "A corrupt recording can fail silently". If training runs while the baseline is being
  recorded, the monitor can miss it.
- Bears on: power channel. It works against a declared baseline, which fits sealed declarations.

### gargiulo2026sidechannel
*Workload Identification with Physical Side Channels for AI Governance.* Simone Gargiulo, Gabriel
Kulp, 2026. arXiv:2609.00309 (v2). Opened 2026-11-27.

- From an H200's power draw (930 traces at 10 MHz), it separates training, inference and non-AI work
  "with an accuracy of 97% and a macro-averaged F1 score of 0.955" on unseen models. A hardened
  detector catches training ">= 99% of the time for three of the four strategies". Diluted LoRA is
  caught "48-88%" of the time, rising to ">= 98%" with a rescue rule (abstract). The physical
  channel can be observed "without the operator's cooperation", unlike NVML telemetry, which "can
  be spoofed or replayed".
- Bears on: power channel, independence from on-chip trust.

### rahman2026telemetry
*Detecting Hidden ML Training With Zero-Overhead Telemetry.* Robi Rahman, Sabiha Tajdari, June 2026.
arXiv:2606.19262. Opened 2026-11-27.

- NVML telemetry only: 20 evasion families, 9 GPU models over 4 generations, 5 rounds of monitor
  against evader. "98.2% binary accuracy" overall, and "43-87% accuracy against the most challenging
  unexpected workloads even when they are adversarially disguised" (abstract).
- Bears on: on-chip telemetry as a channel. The adversarial accuracy is far below the benign one.

### ansari2026taxonomy
*Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty
Verification.* Samar Ansari, April 2026. arXiv:2604.04712. Opened 2026-11-27.

- 20 mechanisms rated on a four-point feasibility scale. "the mechanisms most needed for treaty
  verification, including on-chip compute metering, cryptographic proof-of-training, and
  hardware-embedded enforcement, are also the least mature". The window in which manufacturing
  concentration makes hardware governance implementable "is narrowing, while R&D timelines for
  critical mechanisms span years" (abstract).
- V5, multiparty cryptographic control of training runs (it surveys Sastry, Belfield and Petrie):
  "No prototype exists". The open questions include "timeout handling when a signatory is
  unresponsive". "Feasibility: speculative."
- Bears on: prior art (multiparty licences), feasibility.

### alramiah2025pause
*Toward a Global Regime for Compute Governance: Building the Pause Button.* Ananthi Al Ramiah,
Raymond Koopmanschap, Josh Thorsteinson, Sadruddin Khan, Jim Zhou, Shafira Noh, Joep Meindertsma,
Farhan Shafiq, 2025. arXiv:2506.20530. Opened 2026-11-27.

- A governance, enforcement and verification framework: FLOP caps, offline licensing, model
  locking, traceability. "the system could incorporate digital tools such as blockchain-based chip
  serialization". "Chipmakers would log each wafer batch onto a tamper-proof digital ledger
  (potentially blockchain-based)".
- Bears on: prior art for ledger-anchored registries. That is chip identity, not licence renewal
  or training declarations.

### heim2024thresholds
*Training Compute Thresholds: Features and Functions in AI Regulation.* Lennart Heim, Leonie
Koessler, 2024. arXiv:2405.10799 (v2). Opened 2026-11-27 (abstract and introduction).

- Training compute "currently is the most suitable metric" to identify models for oversight, but
  "is an imperfect proxy for risk", so thresholds should be "an initial filter" that triggers
  scrutiny such as evaluations (abstract).
- Bears on: compute limits as triggers for evaluation (matches the memo's use of compute as the
  backbone and D4 or D5 as the line).

### todd2016opentimestamps
*OpenTimestamps: Scalable, Trust-Minimized, Distributed Timestamping with Bitcoin.* Peter Todd, 15
September 2016. Opened 2026-11-27.

- "A timestamp proves that a message existed prior to some point in time"; "we can use Bitcoin block
  headers as time attestations". Block time is "very likely be accurate to within two or three
  hours", and "almost certainly within a day". Aggregation servers batch digests into a Merkle tree
  and "can't produce a fake timestamp".
- Bears on: prior art for sealed declarations. Bitcoin is a coarse clock, adequate for licence
  periods of weeks, not minutes.

### gipp2015timestamping
*Decentralized Trusted Timestamping using the Crypto Currency Bitcoin.* Bela Gipp, Norman Meuschke,
Andre Gernandt, 2015. arXiv:1502.04015. Opened 2026-11-27.

- A web service that stores file hashes in the Bitcoin blockchain for "anonymous, tamper-proof
  timestamps for digital content" (abstract).
- Bears on: prior art for anchoring hashes in Bitcoin.

### laurie2013ct
*Certificate Transparency* (RFC 6962). Ben Laurie, Adam Langley, Emilia Kasper, IETF, June 2013
(obsoleted by RFC 9162). Opened 2026-11-27.

- "a single, ever-growing, append-only Merkle Tree". "Merkle consistency proofs prove the append-only
  property". A log that shows "two different, conflicting views" is caught when clients compare
  signed tree heads, which serves as cryptographic proof of misbehaviour.
- Bears on: prior art for non-equivocating declaration and licence logs. Anchoring tree heads in
  Bitcoin replaces gossip with one public reference.

### bromme2026agentbb
*A Black Box for Agentic Processes: Blockchain-Anchored Evidence for AI Agent Communication, Human
Oversight, and GRC Audits.* Arslan Bromme, draft of 3 September 2026. arXiv:2609.04017. Opened
2026-11-27.

- Proposes "an externalized, tamper-evident record of selected critical process states" for AI
  agents, anchored with OpenTimestamps or ledgers, giving "integrity, temporal anchoring, and
  declared ordering".
- Bears on: prior art. This is the nearest AI use of Bitcoin anchoring found, but for agent event
  logs, not training-run declarations or licences.

## Numbers for the ledger

Kinds: measured (observed or experimentally obtained, including simulations reported as results),
vendor, spec (fixed by physics, standard or statute), design (a parameter someone chose), assumption
(a modelled estimate or guess in the source).

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| shavit-snapshot-rate | 0.1 | weight snapshots per chip per day | design | shavit2023chinchilla | Table 1 caption |
| shavit-target-detect-prob | 0.9 | probability of catching a run within T | design | shavit2023chinchilla | Table 1 caption |
| shavit-window | 30 | days (detect within T of completion) | design | shavit2023chinchilla | Table 1 caption |
| shavit-chinchilla-flop | 5.76e23 | FLOP | measured | shavit2023chinchilla | Table 1 |
| shavit-samples-chinchilla-c1e5 | 1.33e4 | chip samples per year (stockpile 1e5) | assumption | shavit2023chinchilla | Table 1 |
| shavit-samples-chinchilla-c1e7 | 1.33e6 | chip samples per year (stockpile 1e7) | assumption | shavit2023chinchilla | Table 1 |
| shavit-samples-1e25-world | 232000 | chip samples per year (1e7 chips at 3x H100) | assumption | shavit2023chinchilla | footnote 5, p. 8 |
| shavit-inspectors-1e25-world | 232 | inspectors (at 1,000 chips per inspector-year) | assumption | shavit2023chinchilla | footnote 5, p. 8 |
| iaea-inspectors-2021 | 280 | active IAEA inspectors | measured | shavit2023chinchilla | footnote 5, p. 8 |
| shavit-longer-run-evasion-gain | < 5 | percent increase in evasion probability | assumption | shavit2023chinchilla | Section 3.2, Appendix C |
| h100-sxm-interconnect | 900 | GB/s | vendor | shavit2023chinchilla | Appendix A.2 |
| rtx4090-interconnect | 64 | GB/s | vendor | shavit2023chinchilla | Appendix A.2 |
| nvidia-dc-gpu-share | > 90 | percent of data-centre GPU design market | measured | sastry2024compute | Section 3.B.4 |
| tsmc-foundry-share-10nm-2020 | 90 | percent of pure-play foundry at 10 nm and below | measured | sastry2024compute | footnote 51 |
| cluster-20k-h100-power | > 25 | MW (20,000 H100 at 10.2 kW per 8-GPU DGX) | vendor | sastry2024compute | footnote 36 |
| workload-classifier-accuracy-benign | 95 | percent (ten architectures, MIT Supercloud) | measured | heim2024cloud | Section 3.3.2, p. 24 |
| h100s-for-1e26-90d | 60000 | H100 for 90 days at 34% utilisation | assumption | heim2024cloud | footnote 29, p. 27 |
| rand-offline-licence-budget | 1e18 | operations per licence (example) | design | kulp2024hem | Summary, p. viii |
| rand-licence-fallback | 1 | percent of full performance after expiry | design | kulp2024hem | Summary, p. viii |
| rand-fixed-set-pod | < 65 | chips per preauthorised pod | design | kulp2024hem | Summary |
| rand-circumvention-cost | 5000 | USD per chip, 50% success | assumption | kulp2024hem | Chapter 2, p. 10 |
| rand-cost-imposition-ratio | 2.4 | effective cost / H100 price ($60,000 / $25,000) | assumption | kulp2024hem | Chapter 2, p. 10 |
| offline-licence-deploy-time | 1 | year (firmware on existing chips) | assumption | petrie2024offline | abstract |
| offline-licence-quorum-example | 2/3 | fraction of regulators signing each licence | design | petrie2024offline | Section 3.7 |
| hw-security-dev-time | 18 to 48 | months of effort from leading firms | assumption | aarne2024securechips | p. 4 |
| latency-9ms-bound | 1350 | km (9 ms round trip at light speed, 150 km/ms) | spec | aarne2024securechips | location example |
| flexheg-licence-period-example | 3 | months between licence renewals | design | petrie2025flexheg2 | p. 38 |
| flexheg-first-update-lifetime | 1 | month (early firmware) | design | aarne2025flexheg3 | p. 48 |
| flexheg-restart-delay | 3 | months (with a 1e26 FLOP cap; 1e27 needs >= 30 months) | design | petrie2025flexheg2 | p. 34 |
| teefail-interposer-cost | < 1000 | USD | measured | chuang2026teefail | abstract, project page |
| teefail-attestation-multiplex | hundreds | instances attested by one H100 | assumption | chuang2026teefail | Section 8.2 |
| h100-shipments-2024 | 1.5 to 2 | million units (0.5 million in 2023) | assumption | baker2025sixlayers | Section 4.2 |
| plv-country-radius | 116 | miles error-circle radius | assumption | feldgoise2026tracking | p. 2 |
| plv-best-accuracy | 20 | miles | assumption | feldgoise2026tracking | p. 2 |
| plv-annual-cost-owned | 3.1 to 28.8 | million USD per year | assumption | feldgoise2026tracking | p. 2 |
| plv-annual-cost-rented | 2.6 to 72.4 | million USD per year | assumption | feldgoise2026tracking | p. 2 |
| delay-geolocation-range | 10 to 1000 | km | assumption | brass2024location | p. 4 |
| delay-lv-setup-cost | < 1 | million USD for several years | assumption | brass2024location | Executive Summary |
| gps-spoof-cost | 200 | USD | assumption | brass2024location | method comparison |
| csa-deadline | 180 | days after enactment | spec | chipsecurityact2025 | Sec. 4(a)(1) |
| smuggled-2024-cnas-median | 140000 | chips (range about 10,000 to several hundred thousand) | assumption | grunewald2025smuggling | opening summary |
| smuggled-share-prc-training | 10 | percent median (range 1-40) | assumption | grunewald2025smuggling | opening summary |
| bis-enforcement-budget | 55 | million USD per year | measured | grunewald2025smuggling | endnote 12 |
| smuggled-cumulative-2025-median | 660000 | H100e (90% CI 290,000 to 1,600,000) | assumption | juniewicz2026smuggling | headline |
| smuggled-share-china-compute | 33 | percent (about a third) | assumption | juniewicz2026smuggling | subtitle |
| smuggled-share-global-stock | 3 | percent | assumption | juniewicz2026smuggling | key takeaways |
| diversion-allegations-2025 | 300000 | H100e alleged cumulative | measured | juniewicz2026smuggling | allegation total |
| diversion-detection-rate | 25 | percent median (90% CI 10-80) | assumption | juniewicz2026smuggling | diversion model |
| doj-diverted-servers | 2.5e9 | USD of servers bought 2024-2025 (>= 5.1e8 diverted) | measured | doj2026supermicro | press release (allegation) |
| diloco-comm-reduction | 500 | x less communication (8 workers) | measured | douillard2023diloco | abstract |
| sdiloco-bandwidth | 1 to 5 | Gbit/s for 95% utilisation at 1B-100B params | measured | douillard2025streaming | Figure 4 (simulated) |
| dp-bandwidth-same | 100, 200, 300 | Gbit/s for 1B, 10B, 100B (data parallel) | measured | douillard2025streaming | Figure 4 (simulated) |
| sdiloco-bits-reduction | 400 | x fewer bits exchanged (1B model) | measured | douillard2025streaming | Table 1 |
| intellect1-params | 10e9 | parameters, 1e12 tokens | measured | jaghouar2024intellect1 | abstract |
| intellect1-gpus | 112 | H100 at once, 14 nodes, 30 providers, 3 continents | measured | jaghouar2024intellect1 | Section 1 |
| intellect1-link-bandwidth | 0.5 to 4 | Gbit/s between nodes | measured | jaghouar2024intellect1 | Section 2 |
| intellect1-sync-interval | 38 | minutes between all-reduces (1-7 min each) | measured | jaghouar2024intellect1 | Section 1 |
| intellect1-compute-util | 83 to 96 | percent | measured | jaghouar2024intellect1 | abstract |
| intellect1-bandwidth-reduction | 400 | x versus data parallel | measured | jaghouar2024intellect1 | abstract |
| intellect2-params | 32e9 | parameters (RL, permissionless rollouts) | measured | primeintellect2025intellect2 | abstract |
| demo-data-reduction | 85 | x less data per GPU | measured | peng2024demo | abstract |
| swarm-bandwidth | < 200 | Mb/s (1B shared, ~13B unshared, T4 GPUs) | measured | ryabinin2023swarm | abstract |
| decentral-growth | 20 | x per year (frontier about 5x) | assumption | sevilla2025decentralized | key numbers |
| decentral-largest-run | 6e22 to 6e23 | FLOP | measured | sevilla2025decentralized | key numbers |
| decentral-gap | 1000 | x below frontier compute | assumption | sevilla2025decentralized | key numbers |
| decentral-catchup | 5.5 | years if both trends hold | assumption | sevilla2025decentralized | conclusion |
| consumer-upload | 60 | Mbps typical | assumption | sevilla2025decentralized | bandwidth |
| nodes-overhead-10k | 6 | x more FLOP at 10,000 nodes (extrapolated) | assumption | sevilla2025decentralized | key numbers |
| data-movement-limit | 1e28 | FLOP (utilisation falls, 3-month run) | assumption | erdil2024datamovement | abstract |
| data-movement-infeasible | 1e31 | FLOP | assumption | erdil2024datamovement | abstract |
| consilience-plan | 40e9 | parameters on 20e12 tokens (planned) | design | nous2025psyche | first run |
| distributed-site-example | 5000 | chips per site acting jointly | assumption | scher2024mechanisms | Executive Summary |
| miri-strict-threshold | 1e24 | FLOP (training prohibited above) | design | scher2025agreement | Article IV |
| miri-monitored-threshold | 1e22 | FLOP | design | scher2025agreement | Article IV |
| miri-cluster-cap | 16 | H100-equivalents outside monitored sites (about $500,000) | design | scher2025agreement | Article V, p. 6 |
| algo-progress-rate | 3 | x per year less compute for same capability | assumption | scher2025agreement | p. 8 (citing Ho et al. 2024) |
| miotti-moratorium | 1e24 | FLOP (danger threshold 1e21) | design | miotti2023cap | Article 2 |
| gan-window-start | 12 | months follower response window | assumption | gan2026clock | p. 15 |
| gan-detect-in-window | 32 | percent detection within the window at deterrence | assumption | gan2026clock | p. 16 |
| gan-mean-time-finding | 31 | months | assumption | gan2026clock | p. 16 |
| gan-cooperation-horizon | 18.9 | months (25.5 with safety research, 31.8 at half cost) | assumption | gan2026clock | abstract |
| iaea-detection-target | 90 | percent for significant diversions | spec | allison2025nuclear | Section 3 |
| dc-power-detect-benign | >= 96 | percent at 1% false alarm, meter >= 2 Hz | measured | kimpson2026dcpower | abstract (simulated) |
| dc-power-hidden-5min | 73 | percent of 5-minute observations hidden (best evasion) | measured | kimpson2026dcpower | abstract (simulated) |
| dc-power-detect-day | >= 87 | percent of runs per day at 0.1% false alarm (best evasion) | measured | kimpson2026dcpower | abstract (simulated) |
| dc-power-evasion-cost | 93 to 267 | percent more compute to same loss (small scale) | measured | kimpson2026dcpower | abstract |
| supply-current-flag-rate | >= 99.9 | percent of prohibited-training windows | measured | kimpson2026supply | abstract |
| supply-current-delay | 3.0 | s median detection delay | measured | kimpson2026supply | abstract |
| supply-current-false-alarm | 1 | alarm per 8.8 h of declared work | measured | kimpson2026supply | abstract |
| sidechannel-accuracy | 97 | percent (macro F1 0.955), H200 | measured | gargiulo2026sidechannel | abstract |
| sidechannel-lora-detect | 48 to 88 | percent (diluted LoRA, hardened) | measured | gargiulo2026sidechannel | abstract |
| nvml-accuracy-benign | 98.2 | percent across 9 GPU models | measured | rahman2026telemetry | abstract |
| nvml-accuracy-adversarial | 43 to 87 | percent | measured | rahman2026telemetry | abstract |
| bitcoin-block-time-accuracy | 2 to 3 | hours (almost certainly within a day) | assumption | todd2016opentimestamps | announcement |

## Prior art for the memo's candidates

All judgements are claims about this search, not about the world. "Not found" means not found by
the queries listed.

### 1. Chip licences that expire and are renewed by k of n licensors from rival blocs

- **Closest prior work.** flexHEG Part II (petrie2025flexheg2, pp. 36-38): k-of-n multilateral
  approval in pseudocode, plus periodic licences enforced by a secure clock or cycle counter, with
  a three-month example. Part III (aarne2025flexheg3, pp. 32, 46-49): approvers are major states or
  blocs, updates expire after limited lifetimes tracked by an onboard clock, and a fraction of
  approvers can extend a lifetime. It also covers the hostage problem, collusion against a state
  without a blocking share, and secret double-signing. Part I (petrie2025flexheg1, pp. 33-34):
  time-limited licences as "the only reliable way" to build an off switch, and licences "signed by
  all or a majority of some set of governments". Earlier work: Petrie 2024 (2/3 of regulators sign
  each licence; a chip nonce gives freshness), Sastry et al. 2024 Section 4.C (periodically renewed
  on-chip licence; multisig start switch), Aarne et al. 2024 (periodically renewed licence key) and
  Kulp et al. 2024 (renewable offline licences). Ansari 2026 surveys these and rates multiparty
  control "speculative", with "No prototype".
- **Judgement: prior work.** The memo's protocol should cite flexHEG for the licence itself.
- **What may remain:** (a) A licence whose freshness comes from a recent Bitcoin block hash, and
  whose period ends by block height rather than by the chip's clock or usage counter. Not found in
  the compute-governance literature. flexHEG II's footnote 14 names the cycle-counter weakness
  (idle chips "save up usage time"), and a height-based lease would answer it, provided the chip can
  check headers. Petrie's chip nonce already stops advance signing in an online setting, so the
  added value is offline, publicly checkable freshness and a clock the operator cannot slow.
  **Judgement: extends.** (b) Answers to the open problems flexHEG names: proving a licence was
  *not* issued (Part I, p. 34), and stopping an approver signing two conflicting extensions
  (Part III, p. 49, "a topic for further research"). Making a licence valid only once it appears in
  a public append-only log anchored in Bitcoin would address both. **Judgement: extends** (it
  applies known transparency-log methods, laurie2013ct and todd2016opentimestamps, to a problem
  others have named).
- **Searches tried:** "Flexible Hardware-Enabled Guarantees flexHEG report Petrie 2025 arXiv";
  "Kulp RAND Hardware-Enabled Governance Mechanisms 2024"; "AI chip operating license blockchain OR
  transparency log OR public ledger compute governance hardware-enabled mechanism" (extended); "AI
  governance Bitcoin OR blockchain chip licence renewal multilateral k-of-n threshold signatures
  rival states compute treaty" (extended); "block hash freshness license renewal hardware device
  Bitcoin trusted time offline expiring license proof-of-work clock" (extended); plus full-text
  searches inside the flexHEG, RAND, CNAS, Petrie, Sastry, Baker, Oxford, MIRI, Ansari and Al Ramiah
  texts for expir, renew, k of n, quorum, multisig, blockchain, ledger and timestamp.

### 2. Sealed declarations (training runs, checkpoints and weight hashes in an append-only log sealed in Bitcoin)

- **Closest prior work.** Bitcoin timestamping (gipp2015timestamping, todd2016opentimestamps).
  Append-only logs that cannot show two views without detection (laurie2013ct). On-device logs of
  model fingerprints with timestamps (harack2025oxford, Appendix L.5). Weight-snapshot hashes kept
  by firmware (shavit2023chinchilla, Section 4). Verifiable pre-commitment to a training seed
  (choi2023potd). Blockchain-anchored event logs for AI agents (bromme2026agentbb). A blockchain
  ledger for chip serialisation and wafer batches (alramiah2025pause). Hash-in-public-blockchain as
  a delay proof (petrie2025flexheg2, p. 34).
- **Judgement: extends** (a combination of known parts). I found no proposal that anchors
  international training-run declarations in Bitcoin so that a party cannot backdate an entry or
  show inspectors two histories. The limit to state: sealing stops backdating and equivocation, but
  not false declarations. Proof-of-learning is broken in theory (fang2023polbroken), and
  proof-of-training-data is experimental (choi2023potd).
- **Searches tried:** "blockchain timestamp AI training run declarations compute governance
  verification Bitcoin anchoring model weights hash" (extended); the queries in item 1; full-text
  searches of Baker, Oxford, Wasil, Scher and Thiergart, and MIRI for blockchain, ledger,
  append-only and timestamp.

### 3. Several independent verification channels combined into one miss probability over breakout time

- **Closest prior work.** Baker et al. 2025: six largely independent layers. Regime detection is
  about the weakest subgoal's probability (footnote 33). Stacking layers gives redundancy per
  subgoal. Correlation and violations spread across subgoals are flagged but not modelled.
  Gan 2026: Poisson detection 1 - e^(-mw) within a response window w that shrinks as compute grows,
  a deterrence bound m >= xi/w, and a participation bound on monitoring cost, with one aggregate
  rate. Allison and Herzog 2025: a Poisson risk integral over a horizon, calibrated to the IAEA's
  90% target. Shavit 2023: closed form for one channel (chip sampling). Wasil 2024: "Swiss cheese",
  qualitative.
- **Judgement: extends.** Not found: a model that (i) assigns each channel a detection rate,
  (ii) combines redundant channels within a subgoal (a product of misses, or summed Poisson rates)
  with an explicit correlation term, (iii) takes the evader's best path across subgoals, and
  (iv) evaluates the miss over the breakout time T_b instead of a fixed window.
- **What contradicts the memo.** The memo's "combined chance of missing a secret program" must not
  multiply miss rates across channels that see *different* subgoals. Chip accounting watches
  declared chips. Power and satellites watch facilities. Whistleblowers see people. An evader using
  smuggled chips in a small undeclared site faces only the channels that cover that path. Channels
  that rest on the same hardware trust anchor (attestation, attested latency, on-chip licences,
  NVML telemetry) fail together under one break such as TEE.fail, so they count as one channel.
  Per-channel rates now available as inputs: power metering (kimpson2026dcpower), chip-diversion
  detection (juniewicz2026smuggling, assumed 25%), chip sampling (shavit2023chinchilla).
- **Searches tried:** "verification international AI agreement combined probability of detection
  multiple independent methods miss probability breakout time quantitative model" (extended); "Baker
  2025 Verifying International Agreements on AI six layers verification arXiv"; full-text searches
  of Baker, Wasil, Oxford, Scher and Thiergart, MIRI, Gan, and Allison and Herzog for probability,
  independent, redundancy, combined and Swiss.

### 4. Other memo items this track touches

- **Chip registry and compute thresholds:** prior work (sastry2024compute Section 4.A,
  shavit2023chinchilla, scher2025agreement Article V, miotti2023cap, egan2023kyc).
- **The failure mode "training spread across many small clusters":** prior work identifies it
  (sastry2024compute footnote 35, shavit2023chinchilla Appendix A.2, scher2024mechanisms,
  krys2025distributed, baker2025sixlayers footnote 72, sevilla2025decentralized). The literature's
  answer is chip-level tracking and licensing, plus personnel channels, which scale with the number
  of accomplices.
- **D3 and D4 (breakout time against response time):** this lies outside the track, but gan2026clock
  ties an agreement's viability to a response window that shrinks with compute growth, the closest
  quantitative relative found. scher2025agreement uses breakout only qualitatively. Track 01 or the
  definitions track should run the independent search.
- **Escapement's "cost of speeding the clock":** not found in compute governance. Bitcoin block time
  is accurate only to hours (todd2016opentimestamps), which suits licence periods of weeks to
  months.

## Sources (TOML)

```toml
[source.shavit2023chinchilla]
type = "preprint"
title = "What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring"
authors = "Yonadav Shavit"
year = 2023
arxiv = "2303.11341"
opened = "2026-11-27"

[source.sastry2024compute]
type = "preprint"
title = "Computing Power and the Governance of Artificial Intelligence"
authors = "Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield, Richard Ngo, Konstantin Pilz, George Gor, Emma Bluemke, Sarah Shoker, Janet Egan, Robert F. Trager, Shahar Avin, Adrian Weller, Yoshua Bengio, Diane Coyle"
year = 2024
arxiv = "2402.08797"
opened = "2026-11-27"

[source.heim2024cloud]
type = "preprint"
title = "Governing Through the Cloud: The Intermediary Role of Compute Providers in AI Regulation"
authors = "Lennart Heim, Tim Fist, Janet Egan, Sihao Huang, Stephen Zekany, Robert Trager, Michael A. Osborne, Noa Zilberman"
year = 2024
arxiv = "2403.08501"
opened = "2026-11-27"

[source.egan2023kyc]
type = "preprint"
title = "Oversight for Frontier AI through a Know-Your-Customer Scheme for Compute Providers"
authors = "Janet Egan, Lennart Heim"
year = 2023
arxiv = "2310.13625"
opened = "2026-11-27"

[source.kulp2024hem]
type = "report"
title = "Hardware-Enabled Governance Mechanisms: Developing Technical Solutions to Exempt Items Otherwise Classified Under Export Control Classification Numbers 3A090 and 4A090"
authors = "Gabriel Kulp, Daniel Gonzales, Everett Smith, Lennart Heim, Prateek Puri, Michael J. D. Vermeer, Zev Winkelman (RAND)"
year = 2024
doi = "10.7249/WRA3056-1"
url = "https://www.rand.org/pubs/working_papers/WRA3056-1.html"
opened = "2026-11-27"

[source.petrie2024offline]
type = "preprint"
title = "Near-Term Enforcement of AI Chip Export Controls Using A Firmware-Based Design for Offline Licensing"
authors = "James Petrie"
year = 2024
arxiv = "2404.18308"
opened = "2026-11-27"

[source.aarne2024securechips]
type = "report"
title = "Secure, Governable Chips: Using On-Chip Mechanisms to Manage National Security Risks from AI & Advanced Computing"
authors = "Onni Aarne, Tim Fist, Caleb Withers (CNAS)"
year = 2024
url = "https://www.cnas.org/publications/reports/secure-governable-chips"
opened = "2026-11-27"

[source.petrie2025flexheg1]
type = "preprint"
title = "Flexible Hardware-Enabled Guarantees for AI Compute"
authors = "James Petrie, Onni Aarne, Nora Ammann, David Dalrymple"
year = 2025
arxiv = "2506.15093"
opened = "2026-11-27"

[source.petrie2025flexheg2]
type = "preprint"
title = "Technical Options for Flexible Hardware-Enabled Guarantees"
authors = "James Petrie, Onni Aarne"
year = 2025
arxiv = "2506.03409"
opened = "2026-11-27"

[source.aarne2025flexheg3]
type = "preprint"
title = "Flexible Hardware-Enabled Guarantees, Part III: International Security"
authors = "Onni Aarne, James Petrie"
year = 2025
arxiv = "2506.15100"
opened = "2026-11-27"

[source.nvidia2023hcc]
type = "vendor"
title = "Confidential Compute on NVIDIA Hopper H100 (Whitepaper WP-11459-001 v1.0)"
authors = "NVIDIA"
year = 2023
url = "https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf"
opened = "2026-11-27"

[source.chuang2026teefail]
type = "peer-reviewed"
title = "TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
authors = "Jalen Chuang, Alex Seto, Nicolas Berrios, Stephan van Schaik, Christina Garman, Daniel Genkin"
year = 2026
url = "https://tee.fail/"
opened = "2026-11-27"

[source.baker2025sixlayers]
type = "preprint"
title = "Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment"
authors = "Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart Heim"
year = 2025
arxiv = "2507.15916"
opened = "2026-11-27"

[source.wasil2024verification]
type = "preprint"
title = "Verification methods for international AI agreements"
authors = "Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett"
year = 2024
arxiv = "2408.16074"
opened = "2026-11-27"

[source.harack2025oxford]
type = "report"
title = "Verification for International AI Governance"
authors = "Ben Harack, Robert F. Trager, Anka Reuel, David Manheim, Miles Brundage, Onni Aarne, Aaron Scher, et al. (Oxford Martin AI Governance Initiative)"
year = 2025
url = "https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Verification_for_International_AI_Governance.pdf"
opened = "2026-11-27"

[source.scher2024mechanisms]
type = "preprint"
title = "Mechanisms to Verify International Agreements About AI Development"
authors = "Aaron Scher, Lisa Thiergart"
year = 2024
arxiv = "2506.15867"
opened = "2026-11-27"

[source.scher2025agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.miotti2023cap]
type = "preprint"
title = "An international treaty to implement a global compute cap for advanced artificial intelligence"
authors = "Andrea Miotti"
year = 2023
arxiv = "2311.10748"
opened = "2026-11-27"

[source.gan2026clock]
type = "preprint"
title = "Agreements Have a Clock: Compute Growth and the Verification of AI Restraint"
authors = "Li Gan"
year = 2026
arxiv = "2611.04272"
opened = "2026-11-27"

[source.allison2025nuclear]
type = "peer-reviewed"
title = "Artificial Intelligence and Nuclear Weapons Proliferation: The Technological Arms Race for (In)visibility"
authors = "David M. Allison, Stephen Herzog"
year = 2025
doi = "10.1111/risa.70105"
arxiv = "2512.07487"
opened = "2026-11-27"

[source.feldgoise2026tracking]
type = "report"
title = "Tracking AI Chips: Assessing Location Verification as an Export Control Enforcement Tool"
authors = "Jacob Feldgoise, Kyle Miller, Hanna Dohmen (CSET)"
year = 2026
url = "https://cset.georgetown.edu/wp-content/uploads/CSET-Tracking-AI-Chips.pdf"
opened = "2026-11-27"

[source.brass2024location]
type = "report"
title = "Location Verification for AI Chips"
authors = "Asher Brass, Onni Aarne (Institute for AI Policy and Strategy)"
year = 2024
url = "https://www.iaps.ai/s/Location-Verification-for-AI-Chips.pdf"
opened = "2026-11-27"

[source.nvidia2025fleet]
type = "vendor"
title = "Opt-In NVIDIA Software Enables Data Center Fleet Management"
authors = "NVIDIA Newsroom"
year = 2025
url = "https://blogs.nvidia.com/blog/optional-data-center-fleet-management-software"
opened = "2026-11-27"

[source.reuters2025nvidialocation]
type = "news"
title = "Nvidia builds location verification tech that could help fight chip smuggling"
authors = "Reuters"
year = 2025
url = "https://www.thestar.com.my/business/business-news/2025/12/11/nvidia-builds-location-verification-tech-that-could-help-fight-chip-smuggling"
opened = "2026-11-27"

[source.nvidia2025nobackdoors]
type = "vendor"
title = "No Backdoors. No Kill Switches. No Spyware."
authors = "David Reber Jr. (NVIDIA)"
year = 2025
url = "https://blogs.nvidia.com/blog/no-backdoors-no-kill-switches-no-spyware"
opened = "2026-11-27"

[source.chipsecurityact2025]
type = "legislation"
title = "Chip Security Act, H.R. 3447, 119th Congress (introduced)"
authors = "US House of Representatives"
year = 2025
url = "https://www.govinfo.gov/content/pkg/BILLS-119hr3447ih/html/BILLS-119hr3447ih.htm"
opened = "2026-11-27"

[source.grunewald2025smuggling]
type = "report"
title = "Countering AI Chip Smuggling Has Become a National Security Priority: An Updated Playbook for Preventing AI Chip Smuggling to the PRC"
authors = "Erich Grunewald, Tim Fist (CNAS)"
year = 2025
url = "https://www.cnas.org/publications/reports/countering-ai-chip-smuggling-has-become-a-national-security-priority"
opened = "2026-11-27"

[source.juniewicz2026smuggling]
type = "report"
title = "Diversion and resale: estimating compute smuggling to China"
authors = "Isabel Juniewicz (Epoch AI)"
year = 2026
url = "https://epoch.ai/blog/chip-smuggling"
opened = "2026-11-27"

[source.doj2026supermicro]
type = "official-docs"
title = "Three Charged with Conspiring to Unlawfully Divert Cutting Edge U.S. Artificial Intelligence Technology to China"
authors = "US Department of Justice, Office of Public Affairs"
year = 2026
url = "https://www.justice.gov/opa/pr/three-charged-conspiring-unlawfully-divert-cutting-edge-us-artificial-intelligence"
opened = "2026-11-27"

[source.douillard2023diloco]
type = "preprint"
title = "DiLoCo: Distributed Low-Communication Training of Language Models"
authors = "Arthur Douillard, Qixuan Feng, Andrei A. Rusu, Rachita Chhaparia, Yani Donchev, Adhiguna Kuncoro, Marc'Aurelio Ranzato, Arthur Szlam, Jiajun Shen"
year = 2023
arxiv = "2311.08105"
opened = "2026-11-27"

[source.douillard2025streaming]
type = "preprint"
title = "Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch"
authors = "Arthur Douillard, Yanislav Donchev, Keith Rush, Satyen Kale, Zachary Charles, Zachary Garrett, Gabriel Teston, Dave Lacey, Ross McIlroy, Jiajun Shen, Alexandre Rame, Arthur Szlam, Marc'Aurelio Ranzato, Paul Barham"
year = 2025
arxiv = "2501.18512"
opened = "2026-11-27"

[source.jaghouar2024intellect1]
type = "preprint"
title = "INTELLECT-1 Technical Report"
authors = "Sami Jaghouar, Jack Min Ong, Manveer Basra, Fares Obeid, Jannik Straube, Michael Keiblinger, Elie Bakouch, Lucas Atkins, Maziyar Panahi, Charles Goddard, Max Ryabinin, Johannes Hagemann"
year = 2024
arxiv = "2412.01152"
opened = "2026-11-27"

[source.primeintellect2025intellect2]
type = "preprint"
title = "INTELLECT-2: A Reasoning Model Trained Through Globally Decentralized Reinforcement Learning"
authors = "Prime Intellect Team (Sami Jaghouar, Justus Mattern, Jack Min Ong, et al.)"
year = 2025
arxiv = "2505.07291"
opened = "2026-11-27"

[source.peng2024demo]
type = "preprint"
title = "DeMo: Decoupled Momentum Optimization"
authors = "Bowen Peng, Lizhang Chen, Baiyu Su, Jeffrey Quesnelle, Diederik P. Kingma, Qiang Liu"
year = 2024
arxiv = "2411.19870"
opened = "2026-11-27"

[source.nous2025psyche]
type = "vendor"
title = "Democratizing AI: The Psyche Network Architecture"
authors = "Nous Research"
year = 2025
url = "https://nousresearch.com/nous-psyche/"
opened = "2026-11-27"

[source.ryabinin2023swarm]
type = "peer-reviewed"
title = "SWARM Parallelism: Training Large Models Can Be Surprisingly Communication-Efficient"
authors = "Max Ryabinin, Tim Dettmers, Michael Diskin, Alexander Borzunov"
year = 2023
arxiv = "2301.11913"
opened = "2026-11-27"

[source.sevilla2025decentralized]
type = "essay"
title = "How far can decentralized training over the internet scale?"
authors = "Jaime Sevilla (Epoch AI)"
year = 2025
url = "https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale"
opened = "2026-11-27"

[source.krys2025distributed]
type = "preprint"
title = "Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI Landscape"
authors = "Jakub Krys, Yashvardhan Sharma, Janet Egan"
year = 2025
arxiv = "2507.07765"
opened = "2026-11-27"

[source.erdil2024datamovement]
type = "preprint"
title = "Data Movement Limits to Frontier Model Training"
authors = "Ege Erdil, David Schneider-Joseph"
year = 2024
arxiv = "2411.01137"
opened = "2026-11-27"

[source.long2024protocol]
type = "preprint"
title = "Protocol Learning, Decentralized Frontier Risk and the No-Off Problem"
authors = "Alexander Long"
year = 2024
arxiv = "2412.07890"
opened = "2026-11-27"

[source.jia2021pol]
type = "peer-reviewed"
title = "Proof-of-Learning: Definitions and Practice"
authors = "Hengrui Jia, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot"
year = 2021
arxiv = "2103.05633"
opened = "2026-11-27"

[source.fang2023polbroken]
type = "preprint"
title = "Proof-of-Learning is Currently More Broken Than You Think"
authors = "Congyu Fang, Hengrui Jia, Anvith Thudi, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Varun Chandrasekaran, Nicolas Papernot"
year = 2023
arxiv = "2208.03567"
opened = "2026-11-27"

[source.choi2023potd]
type = "preprint"
title = "Tools for Verifying Neural Models' Training Data"
authors = "Dami Choi, Yonadav Shavit, David Duvenaud"
year = 2023
arxiv = "2307.00682"
opened = "2026-11-27"

[source.kimpson2026dcpower]
type = "preprint"
title = "Detecting AI Training in Datacentre Power"
authors = "Tom Kimpson, Mauricio Baker, Emlyn Graham"
year = 2026
arxiv = "2610.30182"
opened = "2026-11-27"

[source.kimpson2026supply]
type = "preprint"
title = "Verifying Declared AI Workloads from GPU Supply Current"
authors = "Tom Kimpson"
year = 2026
arxiv = "2611.29982"
opened = "2026-11-27"

[source.gargiulo2026sidechannel]
type = "preprint"
title = "Workload Identification with Physical Side Channels for AI Governance"
authors = "Simone Gargiulo, Gabriel Kulp"
year = 2026
arxiv = "2609.00309"
opened = "2026-11-27"

[source.rahman2026telemetry]
type = "preprint"
title = "Detecting Hidden ML Training With Zero-Overhead Telemetry"
authors = "Robi Rahman, Sabiha Tajdari"
year = 2026
arxiv = "2606.19262"
opened = "2026-11-27"

[source.ansari2026taxonomy]
type = "preprint"
title = "Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification"
authors = "Samar Ansari"
year = 2026
arxiv = "2604.04712"
opened = "2026-11-27"

[source.alramiah2025pause]
type = "preprint"
title = "Toward a Global Regime for Compute Governance: Building the Pause Button"
authors = "Ananthi Al Ramiah, Raymond Koopmanschap, Josh Thorsteinson, Sadruddin Khan, Jim Zhou, Shafira Noh, Joep Meindertsma, Farhan Shafiq"
year = 2025
arxiv = "2506.20530"
opened = "2026-11-27"

[source.heim2024thresholds]
type = "preprint"
title = "Training Compute Thresholds: Features and Functions in AI Regulation"
authors = "Lennart Heim, Leonie Koessler"
year = 2024
arxiv = "2405.10799"
opened = "2026-11-27"

[source.todd2016opentimestamps]
type = "essay"
title = "OpenTimestamps: Scalable, Trust-Minimized, Distributed Timestamping with Bitcoin"
authors = "Peter Todd"
year = 2016
url = "https://petertodd.org/2016/opentimestamps-announcement"
opened = "2026-11-27"

[source.gipp2015timestamping]
type = "preprint"
title = "Decentralized Trusted Timestamping using the Crypto Currency Bitcoin"
authors = "Bela Gipp, Norman Meuschke, Andre Gernandt"
year = 2015
arxiv = "1502.04015"
opened = "2026-11-27"

[source.laurie2013ct]
type = "spec"
title = "Certificate Transparency (RFC 6962)"
authors = "Ben Laurie, Adam Langley, Emilia Kasper"
year = 2013
doi = "10.17487/RFC6962"
url = "https://www.rfc-editor.org/rfc/rfc6962"
opened = "2026-11-27"

[source.bromme2026agentbb]
type = "preprint"
title = "A Black Box for Agentic Processes: Blockchain-Anchored Evidence for AI Agent Communication, Human Oversight, and GRC Audits"
authors = "Arslan Bromme"
year = 2026
arxiv = "2609.04017"
opened = "2026-11-27"
```
