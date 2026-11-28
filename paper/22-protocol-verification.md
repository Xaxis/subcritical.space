# Verification, and whom it trusts

A first version of the protocol promised verification without a trusted party; the red team showed it
trusts at least three. The design trusts named parties for named things, no one with everything and
several with something. None of it is deployed, and none has met a real adversary.

Table: The parties the verification design trusts, and what limits each {#tab:protocol-trust}

| Party | Trusted for | What a breach breaks | What limits the trust |
|---|---|---|---|
| The chip maker's secure element, one anchor for all chips | Licences, attestation, location, powered-time counter | Every on-chip channel and the off switch at once [@chuang2026teefail] | Inspection and re-execution, which do not use it |
| A majority of Bitcoin's hash power | That a licence postdates a block; one log history; the height clock | Advance signing, split views, forged headers | The cost of a majority |
| Log replicas under rival operators | Publishing every logged entry | Proof that a licence was not issued | A licence counts only with t replica signatures |
| Licensors outside the holder's bloc | Renewing compliance, refusing violation | Hold-up; collusive renewal | Published signing rules, checkable in the log |
| The inspection beacon | Unpredictable draws | Draws a miner steers by discarding blocks | Contributions mixed from rival blocs (not searched) |
| Makers' unit records | The registry's completeness | Chips never registered | Cross-checks on EUV tools, wafers, HBM |
| Evaluators with weight access | Not leaking weights | Theft by a rival state | Enclaves on the same secure hardware |
| States hosting the chokepoints | Binding themselves | Every limit that leans on compute | Nothing technical |

## Chips registered at birth, licences that expire

A registered chip runs only on a licence that names its identity and expires after one period,
[3 months](../research/numbers.md#prot-licence-months) in flexHEG's example, renewed by k of n
licensors outside the holder's bloc. This is flexHEG's design [@petrie2025flexheg1;
@petrie2025flexheg2; @aarne2025flexheg3], after RAND's offline licensing and others
[@petrie2024offline; @kulp2024hem; @aarne2024securechips; @sastry2024compute]; a survey rates
multiparty control "speculative", with "No prototype" [@ansari2026taxonomy]. It fails through the chip,
where a cheap memory-bus interposer broke the attestation NVIDIA's confidential computing trusts
[@chuang2026teefail; @baker2025verifying]; through chips made without the mechanism
[@petrie2025flexheg1]; through the pool that predates it; through a vendor on record that its GPUs "do
not and should not have kill switches" [@nvidia2025nobackdoors]; and through hold-up.

## Lapse by default, and its price

Expiring licences can be used as a weapon [@aarne2025flexheg3]. An earlier version renewed unless
licensors found a violation, so every lapse awaited a political finding. The protocol returns to
flexHEG's default:

1. **A licence lapses unless renewed on evidence:** in the log, the holder's declarations, each chip's
   attested powered time and location, the inspections granted, no unreconciled discrepancy, and k
   signatures from licensors outside its bloc, each by a published rule. Silence and deadlock lapse.
2. **A change of rules needs every major bloc;** while blocs disagree, the old formulas stand.
3. **A licence is valid only once logged,** so a conflicting one is visible to all.

A holding whose evidence fails then stops within one budget of powered time, with no one else's
agreement. The price is hold-up. Licensors outside a holder's bloc able to deny k signatures can stop
every chip it holds, those serving useful AI included, and deadlock stops them all within one period.
The off switch is a standing veto, which is a hostage. Periods set per holding, short only near the
line, and published signing rules soften this without removing it.

## The licence clock

A licence names a recent Bitcoin block hash, so it was not signed before that block, and ends at a
block height. The first version was broken, and E25, a verifier run on Bitcoin's real chain of
[977,000 headers](../research/numbers.md#e25-headers), found its patch, a floor rate of blocks,
dominated. The rule: the chip counts its powered time, follows the chain with the most work it has
seen, and stops when that chain reaches the expiry height or its powered time reaches the licence's
budget. Its parts are prior work [@petrie2025flexheg2; @mouallem2026alerting; @bentov2019tesseract].

On the real record a budget of [1.099](../research/numbers.md#e25-budget-least) times the nominal
licence time stopped no compliant chip, but one set before 2021 failed when the hash rate fell, so
budgets need a margin. The bound is the counter's, weakness included: a chip left unused "to save up
usage time" [@petrie2025flexheg2]. So lapse caps compute, not the date, and a refused holder keeps up
to one budget per chip. Counting the most-work chain, not the greatest height, stopping an online chip
early needs more than the honest network's
[9.65e+20 hashes/s](../research/numbers.md#e25-net-hashrate), sustained. Bitcoin time is accurate only
to hours [@todd2016opentimestamps], so periods run weeks or longer. In the record the clock (C9) stands
as an application, engineering.

## Sealed declarations, and licences valid only once logged

One public, append-only log anchored in Bitcoin holds declarations, weight hashes, licences and
exports. It follows certificate transparency [@laurie2013ct], Bitcoin timestamping
[@gipp2015timestamping; @todd2016opentimestamps], Catena [@tomescu2017catena] and sealed declarations
for arms control [@burford2020trustmachine]. While honest miners hold most of the hash power it proves
that no entry was backdated and no one saw two histories once entries are six blocks deep (Part III,
Proposition 9.4). Proving that a licence was *not* issued, which flexHEG leaves open
[@petrie2025flexheg1], needs every entry published; So rival operators run replicas, and a chip accepts
a licence only with t replica signatures: hiding one needs t to collude, and more than n - t refusing
stalls issuance. The trust is spread, not removed, and this was not searched for prior art. Nothing
proves a declaration true [@fang2023polbroken; @choi2023potd].

Nor is disclosure safe [@armstrong2016racing]: in E6, over
[72 cells](../research/numbers.md#e6-o2-cells) of race models, disclosing only compliance gave higher
disaster risk than no information in [100%](../research/numbers.md#e6-o2-compliance-over-none) of them,
so it is cut as a safety measure: in these models only halting protects. Declarations go to evaluators
only, though a logged renewal is still a compliance bit.

## Inspections with no known last period

Challenge inspections need an accusation: the Chemical Weapons Convention has had
[0 requests](../research/numbers.md#org-cwc-ci-requests) [@opcw-ec109-dg22; @opcw-numbers]. They stay
for leads from intelligence and insiders; the protocol adds random inspections at a published
probability, drawn from a beacon mixing rival blocs' contributions [@avenhaus2002inspection;
@vonstengel2016recursive]. Compliance is the best response when non-detection is unlikely enough (Part
III, Proposition E.3). A known final period unravels [@vonstengel2016recursive], so licences renew
indefinitely [@fithian2026hardwired]. Complying is then a best response only if membership outweighs an
attempt (Theorem E.1), which a decisive advantage may not. Inspections see declared sites only and
expose secrets [@coe2020arms].

## Channels, trust anchors and the evader's best path

An evader picks the path the fewest channels watch [@baker2025verifying]. C3 sets the miss as the
maximum over a party's paths of the chance no channel on the path detects before T_b(p) - T_resp(p),
path analysis applied [@snell2007itc20; @gif2011prppem; @ward2016safeguards;
@washburn1995interdiction]; multiplying miss rates understates it (Part III, Theorem 3.1). In E5's
illustration the product of every channel's yearly miss is about
10^[-14](../research/numbers.md#e5-memo-log10-miss-1y), while the best watched path, the untraced pool,
is missed [91%](../research/numbers.md#e5-pmiss-max-1y) of the time
([88%](../research/numbers.md#e5-pmiss-max-1y-lo) to [93%](../research/numbers.md#e5-pmiss-max-1y-hi));
cloud compute and distillation have no measured channel. Two rules merge channels first (Theorem 3.3):
channels on one hardware anchor count as one [@chuang2026teefail], and inspections that follow tips are
not independent of them [@baker2023nuclear]. In the record C3 stands as an application, with the
merging rule the only candidate. The declared path's short detection time rescues no other path, so L2
restricts at the source.
