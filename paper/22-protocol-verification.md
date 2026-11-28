# Verification, and whom it trusts

The design trusts named parties for named things, no one with everything.

Table: Whom the verification design trusts, and for what {#tab:protocol-trust}

| Party | Trusted for | A breach breaks | Limited by |
|---|---|---|---|
| The chip's secure element | Licences, attestation | Every on-chip channel [@chuang2026teefail] | Inspection, re-execution |
| Bitcoin's hash majority | Licence dates; one log history | Backdating, split views | Its cost |
| Rival log replicas | Publishing every entry | Proof of non-issuance | t signatures |
| Licensors from rival blocs | Renewal, refusal | Hold-up; collusion | Published rules |
| The inspection beacon | Unpredictable draws | Draws a miner steers | Rival contributions |
| Makers' unit records | A complete registry | Unregistered chips | Cross-checks |
| Evaluators | Not leaking weights | Weight theft | Enclaves |
| Chokepoint states | Binding themselves | Every limit | Nothing technical |

## Chips registered at birth

A registered chip runs only on a licence that names it, expires after one period
([3 months](../research/numbers.md#prot-licence-months) in flexHEG's example) and is renewed by k of n
licensors outside the holder's bloc: flexHEG's design [@petrie2025flexheg1; @petrie2025flexheg2;
@aarne2025flexheg3], after RAND's and others [@petrie2024offline; @kulp2024hem; @aarne2024securechips;
@sastry2024compute], rated "speculative", with "No prototype" [@ansari2026taxonomy]. It fails through
the chip, whose attestation a cheap interposer broke [@chuang2026teefail; @baker2025verifying], through
chips made without it or before it, through a vendor opposed to kill switches [@nvidia2025nobackdoors],
and through hold-up.

## Lapse by default, and its price

A licence lapses unless renewed on logged evidence: declarations, each chip's attested powered time and
location, inspections granted, and k signatures by a published rule. Silence and deadlock lapse,
flexHEG's default [@aarne2025flexheg3], so no halt waits on a political finding; rule changes need
every major bloc, and a licence counts only once logged. The price is hold-up: licensors able to deny k
signatures can stop every chip a holder has, useful AI included. Periods short only near the line and
published signing rules soften it without removing it.

## The licence clock

A licence names a recent Bitcoin block hash and ends at a block height; the chip follows the chain with
the most work and stops there or when its powered-time counter reaches the licence's budget
[@petrie2025flexheg2; @mouallem2026alerting]; on Bitcoin's real chain E25 found an added block-rate
floor dominated [@bentov2019tesseract]. So lapse caps compute, not the date: a refused holder keeps up
to one budget per chip. Stopping an online chip early needs more than the network's
[9.65e+20 hashes/s](../research/numbers.md#e25-net-hashrate), sustained.

## Sealed declarations and the log

One log anchored in Bitcoin holds declarations, weight hashes, licences and exports [@laurie2013ct;
@gipp2015timestamping; @tomescu2017catena; @burford2020trustmachine]. With an honest hash majority it
proves that nothing was backdated and no one saw two histories (Part III, Proposition 9.4). To prove a
licence was *not* issued [@petrie2025flexheg1], a chip accepts one only with t signatures from replicas
under rival operators, a design not searched for prior art that spreads the trust without removing it.
Nothing proves a declaration true [@fang2023polbroken; @choi2023potd], and disclosing only compliance
raised disaster risk over no information in [100%](../research/numbers.md#e6-o2-compliance-over-none)
of E6's race models [@armstrong2016racing], so declarations go to evaluators only.

## Inspections with no known last period

Challenges need an accusation; the Chemical Weapons Convention has had
[0 requests](../research/numbers.md#org-cwc-ci-requests) [@opcw-ec109-dg22]. So inspections are random
at a published probability [@avenhaus1996compliance; @avenhaus2002inspection;
@vonstengel2016recursive], drawn from block hashes an attacker must pay to bias
[@bonneau2015bitcoinbeacon]. A known last period unravels, so licences renew indefinitely, the
hardwired-pause group's condition for lasting cooperation [@fithian2026hardwired]; complying is then
rational only if membership outweighs an attempt (Theorem E.1), which a decisive advantage may not.
Inspections see declared sites only, and expose secrets [@coe2020arms].

## The evader's best path

An evader takes the path the fewest channels watch [@baker2025verifying], so the miss is the maximum
over paths of the chance no channel detects before T_b(p) - T_resp(p), the path analysis of physical
protection, safeguards and interdiction [@snell2007itc20; @ward2016safeguards;
@washburn1995interdiction]; surveys combine channels only qualitatively [@wasil2024verification].
Multiplying miss rates understates it (Theorem 3.1): in E5's illustration the product is about
10^[-14](../research/numbers.md#e5-memo-log10-miss-1y) a year, while the untraced pool is missed
[91%](../research/numbers.md#e5-pmiss-max-1y) of the time, and cloud and distillation have no channel.
Channels are merged first by the textbook bound on a union and the common-cause practice of risk
assessment [@mosleh1998nureg5485]: channels on one hardware anchor count as one, and inspections that
follow tips are not independent of them [@baker2023nuclear].
