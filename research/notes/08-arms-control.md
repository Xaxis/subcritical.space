# Survey track 08: arms control and verification

- **Track:** 08, arms control and verification (nuclear safeguards, CWC, BWC, New START, CTBT,
  secret programmes caught and missed, proposals for AI treaties and their verification).
- **Date:** 2026-11-27. Every source below was opened on this date.
- **Scope:** what each regime verifies, through which channels, each channel's known detection
  record, and the timeliness logic; bearing on D3, D4, the multi-channel verification guarantee
  and the failure analysis in `research/00-memo.md`.

## Summary: what matters most for Subcritical

1. **The nuclear precedent does not set detection time shorter than conversion time.** The 2001
   IAEA glossary says detection time "should correspond approximately to estimated conversion
   times", and its timeliness goals (1 month unirradiated direct-use, 3 months irradiated, 1 year
   indirect-use) sit at or above the conversion times (7-10 days for metal, 1-3 weeks for pure
   compounds, 1-3 months irradiated, 3-12 months LEU). So the margin m is about 1, and below 1 for
   metal. The memo's "organising idea" says the opposite and must be corrected. The 2022 glossary
   no longer prints numeric timeliness goals at all (my text search found none); it uses
   State-level "technical objective performance targets".
2. **Timeliness covers detection only, never response.** Conversion time explicitly excludes
   assembly "nor any subsequent time period"; the Board-to-Security-Council path has no clock.
   Cochran (2005) argues that this leaves "insufficient time" for any response. D4's T_r must
   include response, and there is no nuclear precedent for a guaranteed response time.
3. **Declared material is watched on a timescale of months; undeclared programmes were found
   after years, mostly by intelligence, defectors or disclosure.** DPRK's false declaration was
   caught by IAEA accountancy and sampling within about 9 months (1992-93). But Iraq (about 10
   years), Libya (about 20+), Iran's centrifuge work (17), Syria's reactor (about 6), Fordow
   (about 3 to 7), Biopreparat (16) and South Africa (about 15 active years) were not caught by the
   inspectorate's own channels. The IAEA "identifies suspect locations mainly through voluntary tips
   from national intelligence agencies" (Baker 2023). For an AI regime, the realistic T_r for an
   undeclared programme is years, unless new channels change that.
4. **No CWC challenge inspection has ever been requested** (OPCW EC-109/DG.22, July 2025), against
   8,649 routine inspections since 1997. A challenge inspection is not random: a state must request
   it and accuse another state. The memo's "random challenge inspections on the chemical-weapons
   model" mixes two mechanisms, and its placeholder of 4 a year reaching a site has a realised
   precedent of 0.
5. **Channels do not multiply.** Baker et al. (2025): a regime's detection probability is
   "approximately that of the subgoal with the lowest probability of detecting a violation",
   because an evader routes around the strongest channel. Channels are also correlated
   (inspections follow intelligence tips). The memo's combined miss probability has to be
   computed per acquisition path, minimised by the evader, as the IAEA's acquisition path analysis
   does.
6. **D4's inequality is prior work.** Barnett and Scher (MIRI, May 2025) state that nations "must
   be able to detect and respond to dangerous AI development faster than any single country's
   breakout time". Gan (arXiv, 3 Nov 2026) formalises it as min{D + l, R} < T_catch, with catch-up
   time shrinking as compute grows (12 to 5.74 months over a 24-month pause). D4 should be
   downgraded from "new" to "extends prior work".
7. **Regimes switch off.** DPRK refused special inspection and gave NPT withdrawal notice within
   five weeks of the request (1993). The IAEA has not verified Iran's roughly 440.9 kg of 60% HEU
   since 10 June 2025 (more than 8 months by February 2026, against a monthly guideline). New
   START's data exchanges stopped in 2023 and the treaty expired on 5 February 2026. The BWC never
   had verification; the US rejected the 2001 protocol because dual-use biology makes inspection
   uninformative, the closest analogue to algorithmic progress at fixed compute.
8. **The strongest technical detection record is the CTBT's,** where the event is physically loud:
   seismic thresholds "well below 1 kt worldwide" (0.22 kt at 90% confidence with good
   propagation), and DPRK's sub-kiloton 2006 test seen by 22 stations. Compute has a comparable
   signature only for large concentrated sites; Iraq buried power lines to Tarmiya to hide its
   load.

## Sources

### iaea-glossary-2022

- **Title:** IAEA Safeguards Glossary, 2022 Edition (International Nuclear Verification Series
  No. 3 (Rev. 1)).
- **Organisation:** International Atomic Energy Agency. **Year:** 2022 (printed October 2022).
- **Identifier:** ISBN 978-92-0-122222-0 (pdf); copy opened at
  https://www.bnl.gov/ispo/docs/iaea-sgs-glossary.pdf (text extracted from the PDF).
- **Opened:** 2026-11-27.
- **What it says:**
  - 3.19 Significant quantity: "The approximate amount of nuclear material for which the
    possibility of manufacturing a nuclear explosive device cannot be excluded. SQs take into
    account unavoidable losses ... and should not be confused with critical masses." Table 1: Pu
    8 kg (for Pu with less than 80% Pu-238); U-233 8 kg; HEU (U-235 at or above 20%) 25 kg U-235;
    LEU, natural, depleted 75 kg U-235 (or 10 t natural U or 20 t depleted U); thorium 20 t.
  - 3.20 Conversion time: "Conversion time is used to determine timely detection requirements
    under the Safeguards Criteria." It assumes facilities exist, processes tested, non-nuclear
    components made. "It does not include the time required to transport diverted material to the
    conversion facility, the time required to assemble the device, nor any subsequent time
    period." Table 2: Pu, HEU or U-233 metal "Order of days (7-10)"; pure oxides, nitrates, MOX,
    scrap "Order of weeks (1-3)"; in irradiated fuel "Order of months (1-3)"; U below 20% and
    thorium "Order of months (3-12)".
  - 3.21 Detection time: "An estimate of the time available for detection of a step in an
    acquisition path (e.g. the time from diversion until the end of the path)."
  - 3.14-3.15 Acquisition path analysis: the "plausible paths by which ... nuclear material
    suitable for use in a nuclear weapon ... could be acquired"; a path is "A sequence of steps
    which a State could follow to acquire one significant quantity". 3.23 performance target, e.g.
    "the required detection probability for the diversion of 1 significant quantity (SQ) of
    nuclear material within a period of time".
  - 3.16-3.17 protracted vs abrupt diversion; 3.29 timeliness component: no "abrupt diversion of
    1 significant quantity (SQ) or more at a facility during a calendar year".
  - 2.5 generic objectives under a CSA: detect diversion at declared facilities, undeclared
    production at declared facilities, and "any undeclared nuclear material or activities in the
    State as a whole".
  - 2.11 Deterrence: "through the risk of early detection. Thus, although essentially
    non-quantifiable, the level of deterrence may be expected to be higher the greater the IAEA's
    detection capabilities."
  - 5.46 MUF = (PB + X - Y) - PE, the "difference between book inventory and physical inventory"
    (quoting INFCIRC/153 para. 111). 9.6 Diversion into MUF: "if sigma_MUF is large ... then the
    probability of detection of diversion into MUF is low." 9.21: significance intervals
    "typically by using 0 +/- 2 sigma_MUF or 0 +/- 3 sigma_MUF".
  - 9.22 and 9.31: false alarm probability "generally set to a small value (e.g. 1 %)". 9.30
    detection probability "combines selection probabilities and identification probabilities".
    9.32: verification levels "random low, medium and high (with (1 - beta) = 0.2, 0.5 and 0.9,
    respectively)", and "the achieved detection probability ... is not necessarily as large".
  - 9.10 sample size n = N(1 - beta^(1/D)).
  - 3.25: fresh fuel verification "with 50% detection probability for gross defects" as an
    example intensity.
  - 10.17 and 10.26: a facility with less than 5 ekg gets at most one routine inspection a year
    (INFCIRC/153 para. 79); maximum routine inspection effort 50 person-days a year for reactors
    and sealed stores; for Pu and HEU facilities the formula in para. 80 applies with a floor of
    450 person-days a year; otherwise (100 + 0.4L) person-days a year. (The radical in "30 x L" is
    lost in the text extraction; I did not open INFCIRC/153 itself, which blocked automated
    access.)
  - 10.18: advance notice of routine inspections at least 24 hours for Pu or U above 5%.
  - 10.27: complementary access under the AP; wide-area environmental sampling needs Board
    approval first.
  - A text search of the 2022 edition for "timeliness goal" and "one month" finds no numeric
    timeliness goals (unlike the 2001 edition below).
- **Bears on:** D3 (conversion time as the nuclear breakout analogue), D4 (timeliness vs
  conversion), the multi-channel guarantee (detection probability levels; acquisition path
  analysis), P4 (MUF: detection fails when throughput is large relative to measurement accuracy,
  the same failure as hiding training in large declared fleets).

### iaea-glossary-2001

- **Title:** IAEA Safeguards Glossary, 2001 Edition (International Nuclear Verification Series
  No. 3).
- **Organisation:** IAEA. **Year:** 2002 (2001 edition).
- **Identifier:** ISBN 92-0-111902-X; https://www-pub.iaea.org/MTCD/Publications/PDF/NVS3_scr.pdf
- **Opened:** 2026-11-27.
- **What it says:**
  - 3.20 IAEA timeliness detection goal, where no AP is in force or no broader conclusion drawn:
    "One month for unirradiated direct use material, Three months for irradiated direct use
    material, One year for indirect use material." "Longer timeliness detection goals may be
    applied" where the absence of undeclared material has been concluded.
  - 3.15 Detection time: "the maximum time that may elapse between diversion ... and detection";
    under the conversion assumptions "detection time should correspond approximately to
    estimated conversion times".
  - 3.13 Conversion time, same Table I as 2022 (7-10 days; 1-3 weeks; 1-3 months; 3-12 months).
    The diversion is "assumed to be part of a planned sequence of actions chosen to give a high
    probability of success ... with minimal risk of discovery until at least one such device is
    manufactured."
  - 3.16 Detection probability: "The values of 1 - beta_a currently in use are 90% for 'high' and
    20% for 'low' probability levels." 3.17 false alarm "usually set at 0.05 or less".
- **Bears on:** D4 directly. The goals equal, and for metal exceed, conversion times: the nuclear
  margin m is about 1, and the goal is detection, not response.

### cochran-2005

- **Title:** Adequacy of IAEA's Safeguards for Achieving Timely Detection (Draft 2).
- **Author:** Thomas B. Cochran (NRDC), for the Nonproliferation Policy Education Center. **Year:**
  2005 (1 October 2005).
- **Identifier:** https://npolicy.org/adequacy-of-iaeas-safeguards-for-achieving-timely-detection/
- **Opened:** 2026-11-27.
- **What it says:** Conclusions: "IAEA safeguards are inadequate for achieving the objective of
  timely detection." For unirradiated metal the one-month goal "is too long, and timely warning
  cannot be achieved." Actual inspection frequencies fall below the goals because of "resource
  limitations and resistance of member countries". There is "insufficient time" for the Board to
  report to the Security Council. NRDC proposed reducing SQ values for Pu and HEU "by a factor of
  about eight"; "The IAEA's SQ values are technically erroneous and excessive." A large declared
  reprocessing plant "could divert an SQ of plutonium without detection over a period of about one
  month."
- **Bears on:** D4 (response time absent from the nuclear design), evidence against the memo's
  reading of nuclear timeliness; the threshold quantity (an SQ analogue for AI can be set too high).

### infcirc-540

- **Title:** Model Protocol Additional to the Agreement(s) between State(s) and the International
  Atomic Energy Agency for the Application of Safeguards, INFCIRC/540 (Corrected).
- **Organisation:** IAEA. **Year:** 1997 (reprinted December 1998).
- **Identifier:** https://www.iaea.org/sites/default/files/infcirc540c.pdf
- **Opened:** 2026-11-27.
- **What it says:** Article 4.a: the Agency "shall not mechanistically or systematically seek to
  verify the information referred to in Article 2", but has access to locations "on a selective
  basis in order to assure the absence of undeclared nuclear material and activities". Article
  4.b: "advance notice of access of at least 24 hours"; for places on a site already being
  inspected, "at least two hours but, in exceptional circumstances, it may be less than two
  hours." Article 4.d: the State gets an opportunity to clarify before access is requested.
- **Bears on:** the inspection channel (notice periods bound how fast an inspection can see a site;
  an AI data centre can change workloads in seconds, so short notice matters more than for
  nuclear material).

### iaea-sir-2024

- **Title:** The Safeguards Implementation Report for 2024: Safeguards Statement.
- **Organisation:** IAEA. **Year:** 2025.
- **Identifier:** https://www.iaea.org/sites/default/files/25/06/sir-2024.pdf
- **Opened:** 2026-11-27.
- **What it says:** Safeguards applied for 190 States in 2024. 137 had CSA and AP in force: for 75
  "all nuclear material remained in peaceful activities" (the broader conclusion); for 61 only
  "declared nuclear material remained in peaceful activities"; for one no conclusion. 45 had a CSA
  without an AP. DPRK excluded: "the Agency did not implement safeguards". Iran: unresolved
  uranium of "anthropogenic origin at undeclared locations"; Iran "the only NPT non-nuclear-weapon
  State that is producing and stockpiling high enriched uranium", an estimated "3.9 significant
  quantities in the form of UF6 enriched up to 60% U-235" at the end of 2024. Resources: material
  and facilities under safeguards increase "year on year. In contrast, the Agency's financial
  resources have not risen commensurately."
- **Bears on:** the inspection channel's coverage (only 75 of 190 States reach the level that
  addresses undeclared activity); the failure analysis (verification capacity does not grow with
  the regulated base, as it would need to for compute).

### cwc-text

- **Title:** Convention on the Prohibition of the Development, Production, Stockpiling and Use of
  Chemical Weapons and on their Destruction (with Article IX and the Verification Annex, Part X).
- **Organisation:** OPCW (treaty text). **Year:** 1993 (in force 29 April 1997).
- **Identifier:** https://www.opcw.org/fileadmin/OPCW/CWC/CWC_en.pdf; Article IX page
  https://www.opcw.org/chemical-weapons-convention/articles/article-ix-consultations-cooperation-and-fact-finding
- **Opened:** 2026-11-27.
- **What it says:**
  - Article IX para. 8: a State Party may request an on-site challenge inspection of any site in
    another State Party "solely" to clarify possible non-compliance, "conducted anywhere without
    delay". Para. 15: the request goes to the inspected State "not less than 12 hours before the
    planned arrival of the inspection team at the point of entry". Para. 17: the Executive Council
    may, within 12 hours, decide "by a three-quarter majority of all its members against carrying
    out the challenge inspection" if "frivolous, abusive or clearly beyond the scope".
  - Verification Annex Part X para. 14: final perimeter "in no case later than 24 hours after the
    arrival of the inspection team at the point of entry"; transport "completed not later than 36
    hours after the arrival". Para. 15(b): declared facilities, arrival at the perimeter within 24
    hours. Para. 16: alternative perimeter proposed within 24 hours. Para. 23: exit monitoring of
    "all vehicular exit activity" begins "Not later than 12 hours after the arrival". Para. 43:
    pre-inspection briefing "shall not exceed three hours"; managed access for Article III
    facilities within 12 hours of arrival at the perimeter. Para. 57: "The period of inspection
    shall not exceed 84 hours, unless extended by agreement". Para. 60: preliminary report within
    72 hours of return; para. 61: draft final report within 20 days.
- **Bears on:** the challenge-inspection channel: time from request to perimeter is 12 + 36 = 48
  hours at most, with managed access on top; the inspected State can screen sensitive items.

### opcw-ec109-dg22

- **Title:** Update on the Technical Secretariat's Readiness to Conduct a Challenge Inspection or an
  Investigation of Alleged Use (EC-109/DG.22).
- **Organisation:** OPCW Executive Council, Note by the Director-General. **Year:** 2025 (7 July
  2025).
- **Identifier:** https://www.opcw.org/sites/default/files/documents/2025/07/ec109dg22%28e%29.pdf
- **Opened:** 2026-11-27.
- **What it says:** Para. 5: "neither CIs nor IAUs have been requested by any State Party since the
  Convention's entry into force in 1997." Para. 4: the mechanisms "were envisaged in a different
  security and political environment from the current one"; instead the Secretariat has run ad hoc
  contingency operations in Syria, Germany, Iraq, Malaysia, Ukraine and the UK.
- **Bears on:** the memo's challenge-inspection channel: realised rate 0 per year over 28 years.

### opcw-numbers

- **Title:** OPCW by the Numbers.
- **Organisation:** OPCW. **Year:** 2026 (figures as of 30 September 2026).
- **Identifier:** https://www.opcw.org/media-centre/opcw-numbers
- **Opened:** 2026-11-27.
- **What it says:** 193 States Parties. Declared chemical weapons 72,305 t, "100%" destroyed
  (72,304.34 t). Production facilities: 98 declared, 74 destroyed, 23 converted. Inspections since
  entry into force, by category: CWPF 527, CWDF 2,064, CWSF 530, OCW 198, ACW 202 (sum 3,521);
  industry Schedule 1 388, Schedule 2 1,178, Schedule 3 567, OCPF 2,995 (sum 5,128; the page
  labels this line "Industrial facilities subject to inspection", so the label is ambiguous; the
  sum of the per-category inspection counts is mine).
- **Bears on:** contrast between declared-site verification (thousands of routine inspections,
  complete destruction) and undeclared-site verification (zero challenge inspections).

### brugger-2002

- **Title:** U.S. May Request Chemical Weapons Convention Inspections.
- **Author:** Seth Brugger, Arms Control Today. **Year:** 2002 (March).
- **Identifier:** https://www.armscontrol.org/act/2002-03/press-releases/us-may-request-chemical-weapons-convention-inspections
- **Opened:** 2026-11-27.
- **What it says:** "However, to date, no state has ever requested a challenge inspection." The US
  Under Secretary of State called the OPCW "a very troubled organization" and said "it would be
  risky to put a big burden on the OPCW." No request followed.
- **Bears on:** the challenge-inspection channel: even a state publicly weighing a request did not
  make one. I did not find, in an opened source, a systematic account of why no state has ever
  requested one; reasons often given (political cost, reciprocity, exposing intelligence) are not
  recorded here because I did not open a source that states them.

### mahley-2001

- **Title:** Statement by the United States to the Ad Hoc Group of Biological Weapons Convention
  States Parties.
- **Author:** Ambassador Donald A. Mahley, US Department of State. **Year:** 2001 (25 July 2001).
- **Identifier:** https://usinfo.org/wf-archive/2001/010725/epf314.htm (State Department wire
  archive).
- **Opened:** 2026-11-27.
- **What it says:** "The draft Protocol will not improve our ability to verify BWC compliance." It
  "will not enhance our confidence in compliance and will do little to deter". Inspections "would
  still not provide useful, accurate, or complete information." "Almost any facility that does
  biological work of any magnitude possesses the capability, under some parameters, of being
  diverted to biological weapons work." The draft "would put national security and confidential
  business information at risk."
- **Bears on:** failure analysis: where the dangerous capability lives in dual-use know-how rather
  than a scarce, countable material, inspection loses its value. Algorithmic progress at fixed
  compute is the AI case that looks like the BWC rather than the NPT.

### littlewood-lentzos-2024

- **Title:** Strengthening the Biological Weapons Convention.
- **Authors:** Jez Littlewood, Filippa Lentzos, Arms Control Today. **Year:** 2024 (December).
- **Identifier:** https://www.armscontrol.org/act/2024-12/features/strengthening-biological-weapons-convention
- **Opened:** 2026-11-27.
- **What it says:** "verification has not been covered by the BWC for more than 20 years", tied to
  "the U.S. decision in July 2001 to reject the draft version of the verification protocol." The
  2022 Working Group was tasked to "identify, examine and develop specific and effective measures,
  including possible legally binding measures" and "was given 60 days (15 days a year over four
  years)", with "10 days focused on compliance and verification", which remain "more conceptual".
  Proposals call for "six additional staff in the ISU". I did not find an opened source on the
  Working Group's December 2025 outcome.
- **Bears on:** failure analysis; the baseline that a major weapons regime has run for 50 years
  with no verification at all.

### hoffman-2009

- **Title:** The other Berlin Wall: How the Soviet bioweapons program was revealed.
- **Author:** David E. Hoffman, Bulletin of the Atomic Scientists. **Year:** 2009 (9 November).
- **Identifier:** https://thebulletin.org/2009/11/the-other-berlin-wall-how-the-soviet-bioweapons-program-was-revealed/
- **Opened:** 2026-11-27.
- **What it says:** Western agencies "lacked solid proof" of a Soviet programme. In late October
  1989 Vladimir Pasechnik, director of the All-Union Institute of Ultra-Pure Biological
  Preparations, phoned the British Embassy from Paris to defect. Biopreparat was a cover with
  "tens of thousands of scientists and support workers" in a "hidden archipelago of laboratories
  and industrial plants"; plague production "reaching 2 metric tons per year". On the US-UK visit
  of January 1991 the Soviets worked to hide suspect facilities.
- **Bears on:** the whistleblower and defector channel (the channel that worked, after about 16
  years); the memo's rewarded whistleblowing.

### fas-biopreparat

- **Title:** Biopreparat (Russian and Soviet nuclear forces guide).
- **Organisation:** Federation of American Scientists. **Year:** 1998 (last updated 20 October
  1998).
- **Identifier:** https://nuke.fas.org/guide/russia/agency/bw.htm
- **Opened:** 2026-11-27.
- **What it says:** Biopreparat set up in 1973, a year after the USSR signed the BWC. Estimates of
  25,000 to 32,000 employees across 20 to 30 labs; another estimate of at least 47 facilities and
  over 40,000 workers. Pasechnik revealed the programme was "ten times larger than estimated" by US
  or British intelligence. Alibek defected in 1992.
- **Bears on:** years undetected (1973 to 1989) and the scale a hidden programme reached while
  intelligence underestimated it by an order of magnitude.

### vonbaeckmann-1995

- **Title:** Nuclear verification in South Africa.
- **Authors:** Adolf von Baeckmann, Garry Dillon, Demetrius Perricos, IAEA Bulletin 37(1). **Year:**
  1995.
- **Identifier:** https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull37-1/37105394248.pdf
- **Opened:** 2026-11-27.
- **What it says:** Chronology box: 1974 "Prime Minister approves limited programme for
  development of nuclear weapons as deterrent"; 1977 Kalahari test site abandoned; 1978 first HEU
  withdrawn; 1979 first device; 1987-1989 four more devices; November 1989 decision to terminate;
  26 February 1990 order to destroy "the six completed nuclear devices and the incomplete seventh";
  10 July 1991 NPT accession; 17-23 March 1993 weapons documentation destroyed; 24 March 1993
  announcement to Parliament. Completeness was assessed by isotopic balance of the enrichment
  plants' output against natural uranium feed; "apparent discrepancies" for the Y-plant and
  Z-plant were resolved from "several thousand operating records" modelled "on a daily basis".
  "Information from IAEA Member States was used to confirm that all relevant facilities/locations
  had been inspected."
- **Bears on:** D3 (a breakout from a 1974 decision to a first device in 1979, about 5 years);
  the inspectorate's channel worked only after voluntary disclosure; reconstructing history from
  operating records is the analogue of auditing training logs after the fact.

### thorne-1992

- **Title:** IAEA nuclear inspections in Iraq.
- **Author:** Leslie Thorne, IAEA Bulletin 34(1). **Year:** 1992.
- **Identifier:** https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull34-1/34102451624.pdf
- **Opened:** 2026-11-27.
- **What it says:** "The known information about Iraq was limited to that acquired from the IAEA's
  twice yearly inspections of the facilities at the Tuwaitha Nuclear Research Centre", NPT party
  since 1969; declared areas "occupying not much more than a quarter of the site". "There had been
  speculation for some years in the press ... but no hard information was available." At Tarmiya
  inspectors noted "the huge electrical load the site had required", which "did not fit with
  Iraq's declared use". "Between the first and second missions, a dramatic increase in available
  intelligence information took place. Reconnaissance photographs showed" equipment being removed;
  inspectors on a water tower photographed "nearly a hundred heavy vehicles loaded with the
  equipment". Iraq's 7 July 1991 declaration revealed "nearly 400 tonnes of natural uranium ...
  which had never been reported to the IAEA before" and "six grams of plutonium that had been
  clandestinely produced". Documents seized "Acting on information received from intelligence
  sources" showed the weapons programme "to be large, well-organized, and well-funded".
- **Bears on:** P4 (the energy signature that inspectors read), the failure of routine safeguards
  at declared sites to see undeclared ones, intelligence as the channel that made inspection work.

### albright-2002

- **Title:** Iraq's Programs to Make Highly Enriched Uranium and Plutonium for Nuclear Weapons Prior
  to the Gulf War.
- **Author:** David Albright, Institute for Science and International Security. **Year:** 2002
  (revised from 1997).
- **Identifier:** https://isis-online.org/isis-reports/detail/iraqs-programs-to-make-highly-enriched-uranium-and-plutonium-for-nuclear-we
- **Opened:** 2026-11-27.
- **What it says:** Iraq decided in late 1981, after Osirak was bombed, to build enrichment
  capability; EMIS chosen; first separated uranium January 1986. In mid-August 1990 Iraq ordered
  diversion of its safeguarded HEU fuel in a crash programme aiming at a weapon within six months,
  halted by the January 1991 bombing. EMIS produced about 1,300 g of mostly low-enriched uranium and
  "virtually no HEU". The page describes concealment including buried power lines to Al Tarmiya to
  hide its electricity consumption, and a duplicate site built only by Iraqis.
- **Bears on:** years undetected (late 1981 to mid-1991, about 10 years); P4 (deliberate masking of
  the power signature); D3 (the crash programme is a breakout from diverted declared material).

### iaea-gov-2011-30

- **Title:** Implementation of the NPT Safeguards Agreement in the Syrian Arab Republic
  (GOV/2011/30).
- **Organisation:** IAEA, Report by the Director General. **Year:** 2011 (24 May 2011).
- **Identifier:** https://acronym.org.uk/old/archive/docs/1105/Syria%20IAEA%20Report%20May%202011.pdf
  (copy of the derestricted report).
- **Opened:** 2026-11-27.
- **What it says:** Para. 2: on 2 June 2008 the Director General told the Board the Agency "had been
  provided with information alleging that an installation at the Dair Alzour site in Syria,
  destroyed by Israel in September 2007, had been a nuclear reactor"; "By the end of October 2007,
  large scale clearing and levelling operations had taken place". Para. 5: June 2008 environmental
  samples "contained particles of anthropogenic natural uranium, graphite and stainless steel".
  Para. 13: "Based on commercial imagery from 2001 to 2007, the dimensions of the building are
  comparable" to the Yongbyon 25 MW(th) reactor; a Member State's photograph showed added wall
  and roof sections to conceal it. Conclusion: "the destroyed building was very likely a nuclear
  reactor and should have been declared".
- **Bears on:** years undetected by the inspectorate (about 2001 to 2007), detection by national
  intelligence, and environmental sampling and imagery as corroborating channels after the fact.

### iaea-gov-2003-40

- **Title:** Implementation of the NPT Safeguards Agreement in the Islamic Republic of Iran
  (GOV/2003/40).
- **Organisation:** IAEA. **Year:** 2003 (June).
- **Identifier:** https://www.iaea.org/sites/default/files/gov2003-40.pdf
- **Opened:** 2026-11-27.
- **What it says:** Para. 3: in September 2002 the Director General asked Iran to confirm "whether it
  was building a large underground nuclear related facility at Natanz and a heavy water production
  plant at Arak, as reported in the media in August 2002."
- **Bears on:** the detecting channel for Natanz: public media reports, not the inspectorate.

### iaea-gov-2003-75

- **Title:** Implementation of the NPT Safeguards Agreement in the Islamic Republic of Iran
  (GOV/2003/75).
- **Organisation:** IAEA. **Year:** 2003 (10 November 2003).
- **Identifier:** https://www.iaea.org/sites/default/files/gov2003-75.pdf
- **Opened:** 2026-11-27.
- **What it says:** Para. 46: "Iran has now acknowledged that it has been developing, for 18 years, a
  uranium centrifuge enrichment programme, and, for 12 years, a laser enrichment programme." Para.
  47: the decision "had actually been taken in 1985", drawings received "around 1987"; phases
  1985-1997, 1997-2002 at the Kalaye Electric Company, 2002 on at Natanz. The report deals with
  HEU and LEU particles found by sampling at Kalaye and Natanz.
- **Bears on:** years undetected (1985 to 2002); environmental sampling as the channel that then
  contradicted Iran's account.

### iaea-gov-2009-74

- **Title:** Implementation of the NPT Safeguards Agreement and relevant provisions of Security
  Council resolutions in the Islamic Republic of Iran (GOV/2009/74).
- **Organisation:** IAEA. **Year:** 2009 (16 November 2009).
- **Identifier:** https://www.iaea.org/sites/default/files/gov2009-74.pdf
- **Opened:** 2026-11-27.
- **What it says:** Para. 7: by letter of 21 September 2009 Iran said it "has decided to construct a
  new pilot fuel enrichment plant". Para. 12: Iran said the site was allocated "in the second half
  of 2007". Para. 13: the Agency "had acquired commercially available satellite imagery of the
  site indicating that there had been construction at the site between 2002 and 2004, and that
  construction activities were resumed in 2006"; Member States gave "extensive information ...
  detailing the design" and alleged "design work on the facility had started in 2006". Para. 14:
  late notification "was inconsistent with its obligations".
- **Bears on:** years undeclared (2002 or 2006 to 2009); channels (Member State intelligence first,
  commercial imagery corroborating); the State declared only when it expected exposure.

### whitehouse-2009-qom

- **Title:** Statements by President Obama, President Sarkozy and Prime Minister Brown on Iranian
  Nuclear Facility.
- **Organisation:** The White House (archived). **Year:** 2009 (25 September 2009, Pittsburgh).
- **Identifier:** https://obamawhitehouse.archives.gov/video/Obama-Sarkozy-and-Brown-on-Iranian-Nuclear-Facility/index__q_page=70.html
- **Opened:** 2026-11-27.
- **What it says:** Iran "has been building a covert uranium enrichment facility near Qom for
  several years"; the three states "presented detailed evidence to the IAEA"; "Earlier this week,
  the Iranian government presented a letter to the IAEA that made reference to a new enrichment
  facility."
- **Bears on:** intelligence as the detecting channel for Fordow.

### reuters-2025-iran

- **Title:** Verifying Iran's enriched uranium stock is 'long overdue', IAEA report says.
- **Author:** Francois Murphy, Reuters (republished by ThePrint). **Year:** 2025 (12 November).
- **Identifier:** https://theprint.in/world/verifying-irans-enriched-uranium-stock-is-long-overdue-iaea-report-says/2782711/
- **Opened:** 2026-11-27.
- **What it says:** Pre-strike IAEA estimate of 440.9 kg of uranium enriched up to 60% as UF6,
  "enough in principle, if further enriched, for 10 nuclear bombs" by an IAEA yardstick. IAEA
  guidelines call for verifying HEU stocks every month; no access for five months; the IAEA has
  lost continuity of knowledge.
- **Bears on:** D4: the timeliness goal is met only while access lasts; after military action and
  loss of access, the gap grew to many times the goal.

### aljazeera-2026-iran

- **Title:** IAEA urges Iran to allow inspections, points at Isfahan.
- **Author:** Al Jazeera staff and AFP. **Year:** 2026 (27 February).
- **Identifier:** https://www.aljazeera.com/news/2026/2/27/iaea-eyes-isfahan-nuclear-complex-as-it-urges-iran-to-allow
- **Opened:** 2026-11-27.
- **What it says:** The stockpile was "last seen by nuclear watchdog inspectors last June 10" (2025);
  "more than 400kg" of 60% uranium; Iran "restricted the watchdog's inspectors from accessing sites
  bombed by Israel and the United States"; the IAEA lacks access to Isfahan and does not know the
  location or status of a fourth enrichment facility.
- **Bears on:** loss of the inspection channel as a failure mode; about 8.5 months without
  verification at the report date (my arithmetic from 10 June 2025 to 27 February 2026).

### iaea-gc37-1084

- **Title:** Implementation of the Agreement between the Agency and the Democratic People's
  Republic of Korea for the Application of Safeguards (GC(XXXVII)/1084).
- **Organisation:** IAEA, Report by the Director General. **Year:** 1993 (26 September 1993).
- **Identifier:** https://iaea.org/sites/default/files/gc/gc37-1084_en.pdf
- **Opened:** 2026-11-27.
- **What it says:** Safeguards agreement in force 10 April 1992; Initial Report 4 May 1992; ad hoc
  inspections from May 1992. Para. 3: "because of the significant inconsistencies between the
  DPRK's declarations and the Secretariat's findings, the Secretariat was not able to confirm the
  correctness and completeness". Para. 4: on 9 February 1993 the Director General requested access
  to "two locations where the Agency had reason to believe there exists nuclear waste"; refused.
  Para. 6: on 12 March 1993 the DPRK declared "its decision to withdraw from the Treaty". On 1
  April 1993 the Board found non-compliance and reported to the Security Council; Resolution 825 on
  11 May 1993.
- **Bears on:** the accountancy and sampling channel works on declared material within months; the
  response chain (special inspection, Board, Security Council) then fails; withdrawal as the
  escape (the memo's withdrawal-notice item).

### iaea-gov-2004-12

- **Title:** Implementation of the NPT Safeguards Agreement of the Socialist People's Libyan Arab
  Jamahiriya (GOV/2004/12).
- **Organisation:** IAEA. **Year:** 2004 (20 February 2004).
- **Identifier:** https://securitycouncilreport.org/atf/cf/%7B65BFCF9B-6D27-4E9C-8CD3-CF6E4FF96FF9%7D/Disarm%20GOV200412.pdf
  (copy of the derestricted report).
- **Opened:** 2026-11-27.
- **What it says:** Para. 4: on 19 December 2003 Libya announced its decision "to eliminate ...
  materials, equipments and programmes which lead to the production of internationally proscribed
  weapons." Para. 10: "twelve different sites had been involved in its undeclared nuclear programme
  since the beginning of the 1980s", including conversion and enrichment it "had failed to report".
  Para. 22-25: July 1995 decision to reinvigorate; 1997 delivery of 20 pre-assembled L-1
  centrifuges and parts for 200 more; an order for 5,000, later 10,000, centrifuges of a second
  type; Libya also "had obtained nuclear weapon design and fabrication documents".
- **Bears on:** years undetected (early 1980s to 2003); the inspectorate learned of the programme
  from the State after the fact.

### crs-2004-libya

- **Title:** Disarming Libya: Weapons of Mass Destruction (RS21823).
- **Authors:** Sharon A. Squassoni, Andrew Feickert, Congressional Research Service. **Year:** 2004
  (22 April).
- **Identifier:** https://www.everycrsreport.com/files/20040422_RS21823_9c2b81fe3a3385f6aa0d78a8ac41e3e8cd0cb7ad.html
- **Opened:** 2026-11-27.
- **What it says:** Libyan officials "approached British officials in March 2003 with an offer to
  give up their WMD programs"; US and UK officials first inspected sites in October 2003, which
  coincided with "the interdiction in the Italian port of Taranto of a shipment ultimately bound for
  Libya" of centrifuge equipment; early visits revealed "more extensive Libyan nuclear activities
  than previously thought"; the A.Q. Khan network supplied centrifuges and a weapons design.
- **Bears on:** the supply-chain and interdiction channel (the AI analogue is chip and equipment
  export tracking), and disclosure under pressure as the end of a secret programme.

### newstart-protocol

- **Title:** Protocol to the Treaty between the United States of America and the Russian Federation
  on Measures for the Further Reduction and Limitation of Strategic Offensive Arms (New START).
- **Organisation:** United States and Russian Federation (treaty text). **Year:** 2010.
- **Identifier:** https://courses.physics.illinois.edu/phys280/sp2014/archive/2010%20New%20START%20Protocol.pdf
  (copy of the signed Protocol).
- **Opened:** 2026-11-27.
- **What it says:** Part Five Section VI para. 2: each Party may conduct "no more than ten Type One
  inspections each year, with no more than two facilities being inspected twice each year". Section
  VII para. 2: "no more than eight Type Two inspections each year". Pre-inspection restrictions
  apply "No later than one hour after the time for the designation of the inspection site". Part
  Four: data updated by notification "no later than 30 days after the expiration of each six-month
  period"; each change in data notified "no later than five days after it occurs"; notice of an
  inspection "no less than 32 hours in advance of the estimated time of arrival ... at the point of
  entry"; site designated "no later than four hours after arrival". Part Seven: exchange of
  telemetric information.
- **Bears on:** the declarations-plus-inspection channel with a fixed annual quota; the memo's
  inspections-per-year placeholder.

### fas-2026-newstart

- **Title:** The Aftermath: The Expiration of New START and What It Means For Us All.
- **Authors:** Matt Korda, Eliana Johns, Mackenzie Knight-Boyle, Hans Kristensen, Federation of
  American Scientists. **Year:** 2026 (5 February).
- **Identifier:** https://fas.org/publication/the-expiration-of-new-start/
- **Opened:** 2026-11-27.
- **What it says:** In early 2023 "Russia halted its exchanges of data, notifications, and telemetry
  information", and the US took "reciprocal countermeasures". Limits were 1,550 deployed warheads
  and 700 launchers. Russia "may have exceeded the deployed warhead limit by a small number during
  portions of 2024", an assessment based on national technical means. Russia's September 2025 offer
  to observe the central limits for a year was without verification.
- **Bears on:** the failure analysis: a mature verification regime was suspended by one party three
  years before expiry, leaving national technical means only.

### aca-2026-newstart

- **Title:** New START Expires As U.S. Urges 'Modernized' Treaty.
- **Author:** Xiaodon Liang, Arms Control Today. **Year:** 2026 (March).
- **Identifier:** https://www.armscontrol.org/act/2026-03/news/new-start-expires-us-urges-modernized-treaty
- **Opened:** 2026-11-27.
- **What it says:** The treaty "expired Feb. 5 without a U.S. response to a Russian offer" to keep
  its central limits informally; the parties now have "no legally binding curbs".
- **Bears on:** date of the lapse.

### nrc-2012-ctbt

- **Title:** The Comprehensive Nuclear Test Ban Treaty: Technical Issues for the United States.
- **Organisation:** National Research Council, National Academies Press. **Year:** 2012.
- **Identifier:** DOI 10.17226/12849; chapter 2 read at https://www.nationalacademies.org/read/12849/chapter/5
- **Opened:** 2026-11-27.
- **What it says:** Planned IMS: 50 primary seismic, 120 auxiliary seismic, 80 radionuclide, 11
  hydroacoustic and 60 infrasound stations (p. 39). Finding 2-5 (p. 51): "The threshold levels for
  IMS seismic detection are now well below 1 kt worldwide for fully coupled explosions." Table 2-2
  (p. 51), 90% confidence: worldwide mb 3.8, 0.22 kt (better propagation) or 0.56 kt (poorer);
  Asia, Europe and North Africa mb 3.4, 0.09 kt or 0.22 kt. Regional monitoring "~ 20 tons or 0.020
  kilotons", global "~ 200 tons", test-site "about 5 tons" (pp. 44-45). Finding 2-13 (p. 62):
  in-water threshold "10 tons (0.01 kt) or below worldwide". Radionuclide: a 1 kt atmospheric test
  is detected with "approximately 97 percent" global average probability (Fig. 2-9); a 1 kt
  underground test about 88% with 39 noble gas stations, near 97% with the full network (Fig. 2-10);
  Finding 2-12: xenon detectable "In at least 50 percent of underground nuclear-explosion tests near
  1 kt or larger". Box 2-3: DPRK 2006, mb 4.1, 22 stations (14 primary, 8 auxiliary), Xe-133 at
  Yellowknife about 14 days later, yield "less than a kiloton"; 2009, mb 4.5, 61 stations. On-site
  inspection: up to 1,000 km2, 60 days plus 70; Finding 2-22: "high likelihood of detecting evidence
  of a nuclear explosion with yield greater than about 0.1 kilotons" if located in advance and
  unhindered. Infrasound: 1 kt detected over 80% of Earth's surface with 42 stations. Finding 2-16:
  integrating infrasound with seismic "will provide better detection, location, and
  identification".
- **Bears on:** the multi-channel guarantee: the IMS is the clearest case of independent physical
  channels observing the same event, where combining detection probabilities is justified; it
  works because the event is energetic, which for AI holds only for large concentrated compute.

### ctbto-artxiv-2025

- **Title:** Background document by the Provisional Technical Secretariat prepared for the
  Conference on Facilitating the Entry into Force of the CTBT (CTBT-Art.XIV/2025/3).
- **Organisation:** CTBTO Preparatory Commission. **Year:** 2025 (19 August).
- **Identifier:** https://www.ctbto.org/sites/default/files/2025-09/CTBT-Art.XIV-2025-3.pdf
- **Opened:** 2026-11-27.
- **What it says:** Para. 12: the IMS "is to consist of a network of 321 monitoring stations and 16
  radionuclide laboratories." Para. 13: "As of 30 June 2025, 301 (94%) IMS stations had been
  installed, of which 292 had been officially certified"; of 40 noble gas systems, "32 had been
  installed, of which 26 systems have been certified (65%)". Entry into force needs all 44 Annex 2
  States; the treaty has 178 ratifications, including 35 of the 44.
- **Bears on:** a verification network built and run for decades before (and without) entry into
  force: monitoring can precede a treaty.

### baker-2023

- **Title:** Nuclear Arms Control Verification and Lessons for AI Treaties.
- **Author:** Mauricio Baker. **Year:** 2023.
- **Identifier:** arXiv 2304.04123.
- **Opened:** 2026-11-27.
- **What it says:** The IAEA "has explicitly decided to make this tradeoff such that its detection
  probability is 90-95% for the most sensitive nuclear material" (fn. 50). SQ critics say weapons
  could be made with less "by a factor of e.g., 2-8" (fn. 53). Section 4: "the strongest widely
  implemented M&V system has had zero known major failures"; "no state has attempted to divert a
  significant quantity of nuclear material from a facility that was under CSA safeguards"; APs "are
  nearly untested in their ability to detect secret nuclear weapons development activities".
  Appendix E: "the IAEA identifies suspect locations mainly through voluntary tips from national
  intelligence agencies"; these tips "appear to be irreplaceable". For AI chips: for 90% detection
  of serious violations, "58,000 to 580,000 chips would have to be examined annually", and 2x chip
  growth needs 2x examinations to keep 90%.
- **Bears on:** the multi-channel guarantee (per-layer 90% detection as a design target; channel
  dependence on intelligence); the track record. Note the record of "zero known major failures" is
  for CSA plus AP; the misses in this note were under CSAs without APs or outside safeguards.

### shavit-2023

- **Title:** What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network
  Training via Compute Monitoring.
- **Author:** Yonadav Shavit. **Year:** 2023.
- **Identifier:** arXiv 2303.11341.
- **Opened:** 2026-11-27.
- **What it says:** Chip sampling with on-chip weight snapshots; the number of chips sampled per
  monitoring period s >= log(1 - p) / log(1 - aH/(C)(1 - e^(-f Tm))) x Tm/T (Eq. 1). Table 1:
  annual samples "to catch a chip from every large-scale training run within T = 30 days" at
  "probability of catching a rule-violating training run p = 0.9". Footnote 5: catching a 10^25
  FLOP run within 30 days of completion anywhere, with 90% probability, among 10^7 chips, "would
  require roughly 232,000 worldwide chip samples per year", about 232 inspectors, "slightly smaller
  than the 280 active IAEA inspectors as of 2021." As algorithmic efficiency rises "the number of
  required samples would need to grow".
- **Bears on:** the closest AI analogue of an IAEA timeliness goal plus detection probability (30
  days, 90%); D4 (but Shavit's 30 days is a detection target, not tied to breakout time).

### wasil-2024

- **Title:** Verification methods for international AI agreements.
- **Authors:** Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett. **Year:** 2024.
- **Identifier:** arXiv 2408.16074 (v2).
- **Opened:** 2026-11-27.
- **What it says:** Ten methods in three groups: national technical means (remote sensing,
  whistleblowers, energy monitoring, customs data, financial intelligence); access-dependent (data
  centre, fab and developer inspections); hardware-dependent (chip location tracking and others).
  "national technical means are limited in their ability to identify software-level violations or
  concerted attempts at concealment"; adversaries could disguise data centres "as other high-energy
  facilities like power plants, or when compute is distributed across multiple smaller sites".
  Table 1 maps each method's gaps to complementary methods. No detection rates or timeliness.
- **Bears on:** the channel list for the protocol; prior art for multiple channels, without a
  quantified combined guarantee.

### ho-2023

- **Title:** International Institutions for Advanced AI.
- **Authors:** Lewis Ho, Joslyn Barnhart, Robert Trager, Yoshua Bengio, Miles Brundage, Allison
  Carnegie, Rumman Chowdhury, Allan Dafoe, Gillian Hadfield, Margaret Levi, Duncan Snidal. **Year:**
  2023.
- **Identifier:** arXiv 2307.04699.
- **Opened:** 2026-11-27.
- **What it says:** Four models: "a Commission on Frontier AI", "an Advanced AI Governance
  Organization that sets international standards ... and possibly monitors compliance", "a Frontier
  AI Collaborative", "an AI Safety Project". Some observers ask whether oversight might need
  "detection and inspections of large data centers (partly analogous to IAEA safeguards)".
  "negotiating verification is always fraught (e.g., in the case of the Chemical Weapons
  Convention) and often unsuccessful (e.g., in the case of the Biological Weapons Convention)".
- **Bears on:** institutional design; no timeliness or detection-rate analysis.

### scher-2025-agreement

- **Title:** An International Agreement to Prevent the Premature Creation of Artificial
  Superintelligence.
- **Authors:** Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance
  Team). **Year:** 2025.
- **Identifier:** arXiv 2511.10783 (v2, 17 November 2025).
- **Opened:** 2026-11-27.
- **What it says:** Training above the "Strict Threshold (i.e., 10^24 FLOP)" prohibited; above the
  "Monitored Threshold (i.e., 10^22 FLOP)" approved and monitored; clusters above "16
  H100-equivalents" must sit in monitored facilities. "an ASI breakout by anyone, anywhere, cannot
  be allowed to happen even once." Breakout time is "the time it takes between when a group starts
  trying to create a superintelligence and the point at which they succeed"; destroying chips would
  increase it, but "because we think it's feasible to track chips and verify their usage, we do not
  think that the benefit of longer breakout times is clearly worth the cost". Consolidation limits
  "breakout potential". Challenge inspections "modeled after" the CWC. Withdrawal with notice "12
  months in advance". Precedent: "The CWC requires the declaration and inspection of all Chemical
  Weapons Production Facilities - there have been 97 declared".
- **Bears on:** D3 (breakout time used qualitatively, not computed), D4 (a FLOP line rather than a
  time line), challenge inspections, withdrawal notice. Closest prior art for the protocol's shape.

### scher-thiergart-2025

- **Title:** Mechanisms to Verify International Agreements About AI Development.
- **Authors:** Aaron Scher, Lisa Thiergart (MIRI Technical Governance Team). **Year:** 2025 (arXiv
  June 2025; PDF dated November 2024).
- **Identifier:** arXiv 2506.15867.
- **Opened:** 2026-11-27.
- **What it says:** Verification mechanisms are "processes or tools that give one party greater
  confidence that another is following the agreed-upon rules, typically by detecting violations";
  "increased access (e.g., physical inspections of data centers) can often substitute for these
  technical approaches." Feasibility estimates are given with "low confidence". I found no
  detection probabilities or timeliness targets in a text search.
- **Bears on:** channel catalogue; no quantified guarantee.

### baker-2025-six-layers

- **Title:** Verifying International Agreements on AI: Six Layers of Verification for Rules on
  Large-Scale AI Development and Deployment.
- **Authors:** Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart Heim. **Year:**
  2025.
- **Identifier:** arXiv 2507.15916 (v2).
- **Opened:** 2026-11-27.
- **What it says:** "six largely independent verification approaches with substantial redundancy:
  (1) built-in security features in AI chips; (2-3) separate monitoring devices attached to AI
  chips; and (4-6) personnel-based mechanisms, such as whistleblower programs" (interviews and
  national intelligence are the other two). Footnote 33: "a verification regime's probability of
  detecting a violation is approximately that of the subgoal with the lowest probability of
  detecting a violation. This is because a Prover only needs to circumvent one verification
  subgoal", ignoring aggregation of small violations "depending on the detection probabilities and
  their correlation". On- and off-chip layers "will likely be circumventable until there is
  substantial progress on the R&D".
- **Bears on:** the multi-channel guarantee: directly contradicts multiplying miss probabilities
  across channels that watch different paths. Prior art for layered redundancy.

### hendrycks-2025

- **Title:** Superintelligence Strategy: Expert Version.
- **Authors:** Dan Hendrycks, Eric Schmidt, Alexandr Wang. **Year:** 2025.
- **Identifier:** arXiv 2503.05628 (v2).
- **Opened:** 2026-11-27.
- **What it says:** Mutual Assured AI Malfunction: "a deterrence regime resembling nuclear mutual
  assured destruction (MAD) where any state's aggressive bid for unilateral AI dominance is met with
  preventive sabotage by rivals." "Even if an intelligence recursion achieves only a tenfold speedup
  overall, we could condense a decade of AI development into a year." On a moratorium: "the absence
  of verification mechanisms means the treaty would be toothless".
- **Bears on:** D4's logic as deterrence by detection and sabotage (response is sabotage, not a
  legal process); D2 and D3 (recursion compresses breakout time).

### gan-2026-clock

- **Title:** Agreements Have a Clock: Compute Growth and the Verification of AI Restraint.
- **Author:** Li Gan (Texas A&M University). **Year:** 2026 (3 November 2026).
- **Identifier:** arXiv 2611.04272.
- **Opened:** 2026-11-27.
- **What it says:** Eq. (12): restarting with a positive gap requires "min{D + l, R(d)} <
  Tcatch(d; ...)", where D is detection delay, l implementation delay, R the remaining pause and
  Tcatch the follower's time to reach the frozen frontier. "Compute keeps growing during a compliant
  pause, so a fixed capability gap does not preserve a fixed catch-up time": 12 months at the start,
  8.61 after 12 months, 5.74 after 24. "A fixed response standard fails as catch-up time falls."
  Detection is Poisson: caught within the window with probability 1 - e^(-m w). Proposition 4:
  cooperation holds iff max xi_i/w_i <= min (C_i - R_i)/eta_i. "Deterrence does not require
  near-certain detection": in the calibration, about 32 percent detection within the window
  suffices, and "at the threshold a breakout still succeeds with probability ... 68 percent";
  holding success below beta "needs m >= ln(1/beta)/w". Critical window 6.89 months; cooperation
  supportable "through month 18.9", 25.5 with matched safety research, 31.8 with half the
  monitoring cost. It cites Baker (2023), Avenhaus and Canty (1996) on "the timeliness of
  inspection", and a 1989 START verification paper distinguishing information, significance and
  "timely countermeasures".
- **Bears on:** D3 and D4: the closest prior art found. It states D4's inequality (response time
  below breakout time), computes breakout time from a calibrated model, and shows it shrinks as
  compute grows. It separates deterrence (incentive) from prevention (tolerated breakout
  probability), a distinction D4 needs.

### barnett-scher-2025

- **Title:** AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research
  Questions.
- **Authors:** Peter Barnett, Aaron Scher (MIRI Technical Governance Team). **Year:** 2025 (May).
- **Identifier:** arXiv 2505.04592.
- **Opened:** 2026-11-27.
- **What it says:** On a "Threat of Sabotage" regime: "nations must be able to detect and respond to
  dangerous AI development faster than any single country's breakout time - the time needed to
  secretly advance beyond permitted levels of AI capabilities." Countries could "extend breakout
  times by reducing their AI capabilities and infrastructure". Glossary: "Breakout time The time it
  would take a country to develop dangerous AI capabilities or do certain AI activities, likely in
  violation of agreements or monitoring." Research questions: "What is the breakout time for doing
  secret AI chip development", for "states building covert AI data centers", and "How do we push
  back breakout time ... How long does breakout time need to be?"; with automated AI R&D "breakout
  times may be very short, even given limited compute."
- **Bears on:** D3 and D4: the inequality and the definition are stated here, qualitatively, as
  open research questions.

### sastry-2024

- **Title:** Computing Power and the Governance of Artificial Intelligence.
- **Authors:** Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage,
  Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield, Richard Ngo, Konstantin Pilz, George Gor and
  others. **Year:** 2024.
- **Identifier:** arXiv 2402.08797.
- **Opened:** 2026-11-27.
- **What it says:** "AI Training is Similar to Uranium Enrichment" (Fig. 15). "Enrichment capacity
  has been a key focus of nuclear nonproliferation regimes, as it is the key determinant of
  'breakout time': the minimum time for a state to produce enough weapons-grade enriched uranium
  fuel for a single nuclear weapon." Limits: "The nonradioactivity of compute makes it more
  difficult to detect at ports and other border crossings"; "no obvious parallels in nuclear
  proliferation to the release of model weights"; some compute supply-chain steps "have only a
  single company" versus 6 to 59 manufacturers per NSG good.
- **Bears on:** D3 (the enrichment-to-training analogy and breakout time), O3 chokepoints.

### avenhaus-2002

- **Title:** Inspection Games. In: Handbook of Game Theory with Economic Applications, vol. 3, ch.
  51, pp. 1947-1987.
- **Authors:** Rudolf Avenhaus, Bernhard von Stengel, Shmuel Zamir. **Year:** 2002.
- **Identifier:** DOI 10.1016/S1574-0005(02)03014-X; abstract opened at
  https://ideas.repec.org/h/eee/gamchp/3-51.html (full text not opened; paywalled).
- **Opened:** 2026-11-27 (abstract only).
- **What it says (abstract):** the field began with "the analysis of arms control and disarmament
  problems in the sixties"; inspection extends hypothesis testing and is a game because "the data
  can be strategically manipulated by an inspectee who wants to conceal illegal actions"; material
  accountancy and data verification models are solved; "inspection resources are limited and have
  to be used strategically"; "the inspector becomes a leader by announcing and committing himself
  to his strategy."
- **Bears on:** the memo's defection item (inspection games are prior work); detection probability
  and false-alarm trade-offs.

### allen-2015-llnl

- **Title:** Systems Approach to Arms Control Verification (LLNL-CONF-671180), ESARDA Symposium 2015.
- **Authors:** K. Allen, I. Neimeyer (as spelled on the paper), C. Listner, G. Stein, C. Chen,
  M. Dreicer (LLNL and Forschungszentrum Juelich). **Year:** 2015.
- **Identifier:** https://www.osti.gov/servlets/purl/1184177
- **Opened:** 2026-11-27.
- **What it says:** Applies acquisition path analysis from the IAEA State-level concept to a
  hypothetical arms-cap treaty. Path attributes include "Proliferation Time - The minimum time
  required to deploy a strategically significant quantity of additional weapons" and detection
  probability; "cumulative detection probabilities cannot be determined in advance" when no
  measures are agreed, but path analysis "can be used to identify where specific verification
  measures might be of most benefit."
- **Bears on:** the multi-channel guarantee and the pathway ranking: rank paths by time and by
  detection probability, then place measures; prior art for D3 per pathway.

### allison-herzog-2025

- **Title:** Artificial Intelligence and Nuclear Weapons Proliferation: The Technological Arms Race
  for (In)visibility.
- **Authors:** David M. Allison, Stephen Herzog. **Year:** 2025 (Risk Analysis).
- **Identifier:** DOI 10.1111/risa.70105; arXiv 2512.07487.
- **Opened:** 2026-11-27.
- **What it says:** A model of proliferation-enabling against detection-enhancing technologies, with
  a hazard rate of "clandestine breakout attempts"; it sets a parameter "to match IAEA safeguards
  modeling standards, which target a ~90% detection probability for significant material
  diversions" (model section, kappa = 0.4). The abstract says AI's scaling "challenge[s]
  traditional monitoring and verification methods".
- **Bears on:** found in the D4 prior-art search; about AI's effect on nuclear detection, not an AI
  trigger, so not prior art for D4.

### ansari-2026

- **Title:** Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory
  Compliance and Treaty Verification.
- **Author:** Samar Ansari (University of Chester). **Year:** 2026.
- **Identifier:** arXiv 2604.04712.
- **Opened:** 2026-11-27.
- **What it says:** An engineering taxonomy of hardware governance mechanisms; the IAEA analogy is
  "instructive but imperfect" because the IAEA works with State consent. A text search found no
  breakout-time or timeliness analysis.
- **Bears on:** found in the D4 prior-art search; not prior art for D4.

### alramiah-2025

- **Title:** Toward a Global Regime for Compute Governance: Building the Pause Button.
- **Authors:** Ananthi Al Ramiah, Raymond Koopmanschap, Josh Thorsteinson, Sadruddin Khan, Jim Zhou,
  Shafira Noh, Joep Meindertsma, Farhan Shafiq. **Year:** 2025.
- **Identifier:** arXiv 2506.20530.
- **Opened:** 2026-11-27.
- **What it says:** Proposes a compute-governance regime with a pause mechanism and draws on IAEA
  history ("uncovering Iran's undeclared enrichment facilities"). A text search found no breakout
  time or timeliness logic.
- **Bears on:** found in the D4 prior-art search; not prior art for D4.

## Numbers for the ledger

| id | value | unit | kind | source key | where |
|---|---|---|---|---|---|
| sq-plutonium | 8 | kg Pu | spec | iaea-glossary-2022 | 3.19, Table 1 |
| sq-u233 | 8 | kg U-233 | spec | iaea-glossary-2022 | Table 1 |
| sq-heu | 25 | kg U-235 in HEU | spec | iaea-glossary-2022 | Table 1 |
| sq-leu | 75 | kg U-235 (or 10 t natural U, 20 t depleted U) | spec | iaea-glossary-2022 | Table 1 |
| sq-thorium | 20 | t | spec | iaea-glossary-2022 | Table 1 |
| sq-critique-factor | about 8 | ratio (proposed reduction of Pu and HEU SQs) | assumption | cochran-2005 | Section III |
| conversion-time-metal | 7 to 10 | days | spec | iaea-glossary-2022 | 3.20, Table 2 |
| conversion-time-pure-compounds | 1 to 3 | weeks | spec | iaea-glossary-2022 | Table 2 |
| conversion-time-irradiated | 1 to 3 | months | spec | iaea-glossary-2022 | Table 2 |
| conversion-time-leu-thorium | 3 to 12 | months | spec | iaea-glossary-2022 | Table 2 |
| timeliness-goal-unirradiated-direct | 1 | month | spec | iaea-glossary-2001 | 3.20 |
| timeliness-goal-irradiated-direct | 3 | months | spec | iaea-glossary-2001 | 3.20 |
| timeliness-goal-indirect | 12 | months | spec | iaea-glossary-2001 | 3.20 |
| nuclear-margin-metal | 7-10 days over 1 month, about 0.23 to 0.33 | ratio conversion time / timeliness goal | design (derived here) | iaea-glossary-2001 | 3.13, 3.20 |
| detection-prob-high | 0.9 | probability | spec | iaea-glossary-2022 | 9.32 (also 2001, 3.16) |
| detection-prob-medium | 0.5 | probability | spec | iaea-glossary-2022 | 9.32 |
| detection-prob-low | 0.2 | probability | spec | iaea-glossary-2022 | 9.32 |
| detection-prob-most-sensitive | 0.90 to 0.95 | probability | spec | baker-2023 | fn. 50 |
| false-alarm-prob | 0.01 (2022 example); 0.05 or less (2001) | probability | spec | iaea-glossary-2022 | 9.22, 9.31; 2001 3.17 |
| muf-test-interval | 2 or 3 | sigma_MUF | spec | iaea-glossary-2022 | 9.21 |
| routine-inspection-small-facility | 1 | per year (facilities under 5 ekg) | spec | iaea-glossary-2022 | 10.17, 10.26 |
| mrie-reactor | 50 | person-days per year | spec | iaea-glossary-2022 | 10.26 |
| mrie-pu-heu-floor | 450 | person-days per year | spec | iaea-glossary-2022 | 10.26 |
| ap-ca-notice | 24 | hours | spec | infcirc-540 | Art. 4.b(i) |
| ap-ca-notice-on-site | 2 | hours | spec | infcirc-540 | Art. 4.b(ii) |
| sg-states-2024 | 190 | States | measured | iaea-sir-2024 | Statement A |
| sg-states-csa-ap-2024 | 137 | States | measured | iaea-sir-2024 | A.1 |
| sg-states-broader-conclusion-2024 | 75 | States | measured | iaea-sir-2024 | A.1(a) |
| iran-heu60-sq-end2024 | 3.9 | SQ | measured | iaea-sir-2024 | B.2 |
| iran-heu60-kg-prewar | 440.9 | kg U enriched up to 60% | measured | reuters-2025-iran | body |
| iran-heu60-weapons-yardstick | 10 | weapons if further enriched | spec | reuters-2025-iran | body |
| iran-heu-verify-guideline | 1 | month | spec | reuters-2025-iran | body |
| iran-heu-last-verified | 2025-06-10 | date | measured | aljazeera-2026-iran | body |
| iran-months-unverified-feb2026 | about 8.5 | months | measured (derived here) | aljazeera-2026-iran | 10 Jun 2025 to 27 Feb 2026 |
| cwc-ci-notice | 12 | hours (minimum, before arrival at point of entry) | spec | cwc-text | Art. IX para. 15 |
| cwc-ci-ec-block | 3/4 of all members within 12 hours | vote | spec | cwc-text | Art. IX para. 17 |
| cwc-ci-final-perimeter | 24 | hours after arrival | spec | cwc-text | Part X para. 14, 16 |
| cwc-ci-transport-max | 36 | hours after arrival | spec | cwc-text | Part X para. 14 |
| cwc-ci-exit-monitoring | 12 | hours after arrival | spec | cwc-text | Part X para. 23 |
| cwc-ci-duration-max | 84 | hours | spec | cwc-text | Part X para. 57 |
| cwc-ci-prelim-report | 72 | hours after return | spec | cwc-text | Part X para. 60 |
| cwc-ci-draft-final-report | 20 | days | spec | cwc-text | Part X para. 61 |
| cwc-ci-requested-since-1997 | 0 | requests (1997 to July 2025) | measured | opcw-ec109-dg22 | para. 5 |
| opcw-cw-inspections | 3,521 | inspections since 1997 (sum of CW categories) | measured | opcw-numbers | Destruction progress |
| opcw-industry-inspections | 5,128 | inspections since 1997 (sum of industry categories) | measured | opcw-numbers | Industry verification |
| opcw-stockpile-destroyed | 72,304.34 of 72,305 | t | measured | opcw-numbers | Destruction progress |
| opcw-cwpf-declared | 98 | facilities | measured | opcw-numbers | CWPF |
| bwc-verification-staff-proposed | 6 | additional ISU staff | design | littlewood-lentzos-2024 | body |
| bwc-wg-days | 60 | meeting days over 4 years | spec | littlewood-lentzos-2024 | body |
| newstart-type1-quota | 10 | inspections per year | spec | newstart-protocol | Part Five Sec. VI para. 2 |
| newstart-type2-quota | 8 | inspections per year | spec | newstart-protocol | Part Five Sec. VII para. 2 |
| newstart-data-update | 6 | months (plus 30 days to notify) | spec | newstart-protocol | Part Four |
| newstart-change-notice | 5 | days | spec | newstart-protocol | Part Four |
| newstart-inspection-notice | 32 | hours (minimum) | spec | newstart-protocol | Part Four Sec. VI para. 9 |
| newstart-site-designation | 4 | hours after arrival | spec | newstart-protocol | Part Four Sec. VI para. 14(a) |
| newstart-warhead-limit | 1,550 | deployed warheads | spec | fas-2026-newstart | body |
| newstart-launcher-limit | 700 | deployed launchers | spec | fas-2026-newstart | body |
| newstart-expiry | 2026-02-05 | date | measured | aca-2026-newstart | body |
| ctbt-ims-stations-planned | 321 | stations (+16 labs) | spec | ctbto-artxiv-2025 | para. 12 |
| ctbt-ims-installed-2025 | 301 | stations (30 Jun 2025) | measured | ctbto-artxiv-2025 | para. 13 |
| ctbt-ims-certified-2025 | 292 | stations (30 Jun 2025) | measured | ctbto-artxiv-2025 | para. 13 |
| ctbt-noble-gas-certified-2025 | 26 of 40 | systems | measured | ctbto-artxiv-2025 | para. 13 |
| ctbt-seismic-90pct-world-good | 0.22 | kt (mb 3.8) | measured | nrc-2012-ctbt | Table 2-2 |
| ctbt-seismic-90pct-world-poor | 0.56 | kt | measured | nrc-2012-ctbt | Table 2-2 |
| ctbt-seismic-90pct-eurasia | 0.09 to 0.22 | kt (mb 3.4) | measured | nrc-2012-ctbt | Table 2-2 |
| ctbt-seismic-regional | 0.02 | kt | measured | nrc-2012-ctbt | Fig. 2-7 |
| ctbt-hydroacoustic | 0.01 | kt or below | measured | nrc-2012-ctbt | Finding 2-13 |
| ctbt-radionuclide-atm-1kt | 0.97 | probability within 14 days | measured | nrc-2012-ctbt | Fig. 2-9 |
| ctbt-radionuclide-ug-1kt | 0.88 (39 stations), about 0.97 (full) | probability | measured | nrc-2012-ctbt | Fig. 2-10 |
| ctbt-osi-area | 1,000 | km2 | spec | nrc-2012-ctbt | pp. 71-73 |
| ctbt-osi-duration | 60 (+70) | days | spec | nrc-2012-ctbt | pp. 71-73 |
| ctbt-osi-min-yield | 0.1 | kt | measured | nrc-2012-ctbt | Finding 2-22 |
| dprk-2006-stations | 22 | IMS stations (mb 4.1, yield under 1 kt) | measured | nrc-2012-ctbt | Box 2-3 |
| dprk-2009-stations | 61 | IMS stations (mb 4.5) | measured | nrc-2012-ctbt | Box 2-3 |
| program-iraq-years-undetected | about 10 | years (late 1981 decision to mid-1991) | measured | albright-2002; thorne-1992 | body |
| program-iraq-channel | intelligence (reconnaissance imagery, tips) driving post-war UN inspections | channel | measured | thorne-1992 | "The role of intelligence information" |
| program-libya-years-undetected | about 20+ | years (beginning of 1980s to Dec 2003) | measured | iaea-gov-2004-12 | para. 10 |
| program-libya-channel | intelligence-led interdiction (Taranto, Oct 2003) and negotiated disclosure | channel | measured | crs-2004-libya | body |
| program-iran-centrifuge-years | 17 | years (1985 to Aug 2002) | measured | iaea-gov-2003-75; iaea-gov-2003-40 | para. 46-47; para. 3 |
| program-iran-natanz-channel | public media reports (Aug 2002), then environmental sampling | channel | measured | iaea-gov-2003-40 | para. 3 |
| program-fordow-years | about 3 (design 2006) to 7 (construction 2002) | years to Sept 2009 | measured | iaea-gov-2009-74 | para. 13 |
| program-fordow-channel | Western intelligence, then commercial imagery | channel | measured | whitehouse-2009-qom; iaea-gov-2009-74 | body; para. 13 |
| program-syria-years | about 6 | years (imagery from 2001 to strike Sept 2007) | measured | iaea-gov-2011-30 | para. 2, 13 |
| program-syria-channel | national intelligence; IAEA informed 2008 after destruction; sampling corroborated | channel | measured | iaea-gov-2011-30 | para. 2, 5 |
| program-dprk-discrepancy-months | about 9 | months (Initial Report 4 May 1992 to special inspection request 9 Feb 1993) | measured | iaea-gc37-1084 | para. 2-4 |
| program-dprk-channel | IAEA accountancy and sampling of declared material | channel | measured | iaea-gc37-1084 | para. 3 |
| program-dprk-withdrawal-days | 31 | days (request 9 Feb to withdrawal notice 12 Mar 1993) | measured | iaea-gc37-1084 | para. 4, 6 |
| program-biopreparat-years | 16 | years (1973 to Oct 1989) | measured | fas-biopreparat; hoffman-2009 | body |
| program-biopreparat-channel | defector (Pasechnik), scale underestimated 10x | channel | measured | fas-biopreparat; hoffman-2009 | body |
| program-southafrica-years-active | 15 | years (1974 to 1989), never detected by the inspectorate while active in these sources | measured | vonbaeckmann-1995 | chronology |
| program-southafrica-channel | self-disclosure (24 Mar 1993) | channel | measured | vonbaeckmann-1995 | chronology |
| program-southafrica-decision-to-device | about 5 | years (1974 to 1979) | measured | vonbaeckmann-1995 | chronology |
| shavit-detect-window | 30 | days after completion | design | shavit-2023 | Table 1 |
| shavit-detect-prob | 0.9 | probability | design | shavit-2023 | Table 1 |
| shavit-samples-1e25 | 232,000 | chip samples per year (10^7 chips) | design | shavit-2023 | fn. 5 |
| iaea-inspectors-2021 | 280 | active inspectors | measured | shavit-2023 | fn. 5 |
| baker-chip-samples-90pct | 58,000 to 580,000 | chips per year | design | baker-2023 | Section on AI chips |
| miri-strict-threshold | 1e24 | FLOP | design | scher-2025-agreement | Art. IV |
| miri-monitored-threshold | 1e22 | FLOP | design | scher-2025-agreement | Art. IV |
| miri-cluster-threshold | 16 | H100-equivalents | design | scher-2025-agreement | Art. II, V |
| miri-withdrawal-notice | 12 | months | design | scher-2025-agreement | Art. XV |
| gan-catchup-start | 12 | months | assumption | gan-2026-clock | Sec. 4.2 |
| gan-catchup-12mo | 8.61 | months | assumption | gan-2026-clock | Sec. 4.2 |
| gan-catchup-24mo | 5.74 | months | assumption | gan-2026-clock | Sec. 4.2 |
| gan-critical-window | 6.89 | months | assumption | gan-2026-clock | Sec. 1 |
| gan-deterrence-detect-prob | 0.32 | probability within window | assumption | gan-2026-clock | Sec. 4.3 |

All Gan values are from an illustrative calibration, hence "assumption". Values marked "derived
here" are my arithmetic on sourced values and should be recomputed in `model/subcritical.py`
rather than entered as inputs.

## Prior art for the memo's candidates

All judgements below are claims about my search, not about the world.

**Searches tried** (web search, then opening hits; each AI paper also searched in full text for
"breakout", "timeliness", "timely", "detection probability"):
1. `"breakout time" artificial intelligence superintelligence detection "timeliness" IAEA analogy
   compute governance` (extended): found gan-2026-clock, barnett-scher-2025, scher-2025-agreement,
   allison-herzog-2025, ansari-2026. A RAND perspective, "Insights from nuclear history for AI
   governance" (PEA3652-1), came up but its PDF blocked automated access, so I did not open it.
2. `AI governance "timely detection" "significant quantity" compute analog nuclear safeguards
   training run detection time conversion time` (extended): found sastry-2024, alramiah-2025,
   gan-2026-clock again.
3. `"Mechanisms to Verify International Agreements About AI Development" MIRI 2025 arXiv`:
   scher-thiergart-2025, baker-2025-six-layers.
4. `MIRI technical governance team 2025 "international agreement" prevent premature
   superintelligence`: scher-2025-agreement.
5. `acquisition path analysis "detection probability" combined multiple safeguards measures`:
   allen-2015-llnl.
6. Direct reads of the papers named in the brief: wasil-2024, shavit-2023, ho-2023, baker-2023,
   hendrycks-2025.

**D3, breakout time.** Closest: scher-2025-agreement ("the time it takes between when a group
starts trying to create a superintelligence and the point at which they succeed"),
barnett-scher-2025 (glossary definition and research questions on breakout time for covert chips
and data centres), gan-2026-clock (a computed catch-up time from a calibrated takeoff model,
falling as compute grows), sastry-2024 (enrichment as the determinant of nuclear breakout, training
as its analogue), and the nuclear concepts themselves (conversion time, detection time,
acquisition path, iaea-glossary-2022). Judgement: **prior work** for the concept and for computing
it from a model; the memo's version, computed from a party's verified holdings (chips, weights,
data, labour) and a measured loop gain D2, is at most **extends prior work**. Gan already shows the
key dynamic the memo lists as a failure (breakout time shrinking at fixed declared position as
compute and algorithms improve).

**D4, weapons-grade when T_b < m T_r.** Closest: barnett-scher-2025 ("nations must be able to
detect and respond to dangerous AI development faster than any single country's breakout time"),
gan-2026-clock (min{D + l, R} < T_catch, with detection delay and implementation delay separated,
and a date-dependent response standard), hendrycks-2025 (MAIM: detect and sabotage before a bid for
dominance completes), shavit-2023 (an explicit 30-day, 90% detection target), and the IAEA rule that
detection time should correspond to conversion time (iaea-glossary-2001). Judgement: the inequality
is **prior work**. Using it as the classification line between useful AI and weapons-grade, with an
explicit margin m and the regime's own guaranteed T_r, and letting everything above the line keep
improving, was not found as such in my search, so **extends prior work**, not new. The memo's label
"new as a regulatory trigger" should change. Two corrections from the nuclear record: the nuclear
margin is about 1 (below 1 for metal), so m > 1 has no precedent; and nuclear timeliness counts
detection only, so T_r as "detect and respond" has no measured precedent. Gan also shows that a line
set for deterrence (about 32% detection in the window in his calibration) is far weaker than a line
set for prevention (breakout success below a tolerated beta); D4 must say which it is.

**Multi-channel guarantee (combined miss probability over the breakout time).** Closest:
baker-2025-six-layers (six largely independent layers, with the regime's detection probability
approximately that of the weakest subgoal), baker-2023 (90% per layer; IAEA dependence on
intelligence tips), shavit-2023 (sampling formula for p within a window), gan-2026-clock (Poisson
detection 1 - e^(-m w)), wasil-2024 (ten channels and their gaps), allen-2015-llnl and
iaea-glossary-2022 (acquisition path analysis with path-level detection probabilities),
nrc-2012-ctbt (independent physical channels on the same event). Judgement: the structure is
**prior work**. A sourced per-channel detection rate table feeding a per-path, evader-minimised miss
probability over T_b may **extend prior work**. Evidence against the memo's current form: (a) the
product of per-channel miss probabilities applies only when every channel watches the same path and
fails independently; across paths the evader takes the weakest (baker-2025-six-layers); (b)
channels are correlated (inspections and special inspections follow intelligence: baker-2023 App.
E; CWC challenge inspections need a requesting state); (c) the realised detection record for
undeclared programmes is years, not the months the placeholders imply.

**Challenge inspections on the CWC model.** scher-2025-agreement already models its challenge
inspections on the CWC. Judgement: **prior work**. Evidence against the memo: zero requests since
1997 (opcw-ec109-dg22), so the channel's realised rate is 0; the memo should either model a
genuinely random inspection (like the IAEA's short-notice random inspections or AP complementary
access, iaea-glossary-2022 10.9-10.10, infcirc-540 Art. 4) or price the political trigger.

**Threshold quantity (an SQ for AI).** scher-2025-agreement (10^22 and 10^24 FLOP; 16
H100-equivalents), shavit-2023 (training run size H). Judgement: **prior work**. cochran-2005 and
baker-2023 warn that nuclear SQs may be too high by 2 to 8 times, the same risk for a compute line
as algorithms improve.

**Withdrawal notice longer than response time.** scher-2025-agreement (12 months). Judgement:
**prior work**. iaea-gc37-1084 shows withdrawal used 31 days after a special inspection request.

**Defection and inspection games.** avenhaus-2002 (inspector leadership, accountancy games),
gan-2026-clock (costed monitoring and voluntary participation). Judgement: **prior work**.

**P4 footprint floor and energy signatures.** Not my track, but the record bears on it: inspectors
read Tarmiya's "huge electrical load" (thorne-1992), and Iraq buried power lines to hide it
(albright-2002); wasil-2024 notes data centres disguised as other high-energy facilities. The floor
concept itself was not searched here.

## Sources (TOML)

```toml
[source.iaea-glossary-2022]
type = "official-docs"
title = "IAEA Safeguards Glossary, 2022 Edition (International Nuclear Verification Series No. 3 (Rev. 1))"
authors = "International Atomic Energy Agency"
year = 2022
isbn = "978-92-0-122222-0"
url = "https://www.bnl.gov/ispo/docs/iaea-sgs-glossary.pdf"
opened = "2026-11-27"

[source.iaea-glossary-2001]
type = "official-docs"
title = "IAEA Safeguards Glossary, 2001 Edition (International Nuclear Verification Series No. 3)"
authors = "International Atomic Energy Agency"
year = 2002
isbn = "92-0-111902-X"
url = "https://www-pub.iaea.org/MTCD/Publications/PDF/NVS3_scr.pdf"
opened = "2026-11-27"

[source.cochran-2005]
type = "report"
title = "Adequacy of IAEA's Safeguards for Achieving Timely Detection (Draft 2)"
authors = "Thomas B. Cochran"
year = 2005
url = "https://npolicy.org/adequacy-of-iaeas-safeguards-for-achieving-timely-detection/"
opened = "2026-11-27"

[source.infcirc-540]
type = "legislation"
title = "Model Protocol Additional to the Agreement(s) between State(s) and the International Atomic Energy Agency for the Application of Safeguards, INFCIRC/540 (Corrected)"
authors = "International Atomic Energy Agency"
year = 1997
url = "https://www.iaea.org/sites/default/files/infcirc540c.pdf"
opened = "2026-11-27"

[source.iaea-sir-2024]
type = "official-docs"
title = "The Safeguards Implementation Report for 2024: Safeguards Statement"
authors = "International Atomic Energy Agency"
year = 2025
url = "https://www.iaea.org/sites/default/files/25/06/sir-2024.pdf"
opened = "2026-11-27"

[source.cwc-text]
type = "legislation"
title = "Convention on the Prohibition of the Development, Production, Stockpiling and Use of Chemical Weapons and on their Destruction"
authors = "Organisation for the Prohibition of Chemical Weapons"
year = 1993
url = "https://www.opcw.org/fileadmin/OPCW/CWC/CWC_en.pdf"
opened = "2026-11-27"

[source.opcw-ec109-dg22]
type = "official-docs"
title = "Update on the Technical Secretariat's Readiness to Conduct a Challenge Inspection or an Investigation of Alleged Use (EC-109/DG.22)"
authors = "OPCW Director-General"
year = 2025
url = "https://www.opcw.org/sites/default/files/documents/2025/07/ec109dg22%28e%29.pdf"
opened = "2026-11-27"

[source.opcw-numbers]
type = "official-docs"
title = "OPCW by the Numbers"
authors = "Organisation for the Prohibition of Chemical Weapons"
year = 2026
url = "https://www.opcw.org/media-centre/opcw-numbers"
opened = "2026-11-27"

[source.brugger-2002]
type = "news"
title = "U.S. May Request Chemical Weapons Convention Inspections"
authors = "Seth Brugger"
year = 2002
url = "https://www.armscontrol.org/act/2002-03/press-releases/us-may-request-chemical-weapons-convention-inspections"
opened = "2026-11-27"

[source.mahley-2001]
type = "official-docs"
title = "Statement by the United States to the Ad Hoc Group of Biological Weapons Convention States Parties"
authors = "Donald A. Mahley, US Department of State"
year = 2001
url = "https://usinfo.org/wf-archive/2001/010725/epf314.htm"
opened = "2026-11-27"

[source.littlewood-lentzos-2024]
type = "essay"
title = "Strengthening the Biological Weapons Convention"
authors = "Jez Littlewood, Filippa Lentzos"
year = 2024
url = "https://www.armscontrol.org/act/2024-12/features/strengthening-biological-weapons-convention"
opened = "2026-11-27"

[source.hoffman-2009]
type = "news"
title = "The other Berlin Wall: How the Soviet bioweapons program was revealed"
authors = "David E. Hoffman"
year = 2009
url = "https://thebulletin.org/2009/11/the-other-berlin-wall-how-the-soviet-bioweapons-program-was-revealed/"
opened = "2026-11-27"

[source.fas-biopreparat]
type = "report"
title = "Biopreparat"
authors = "Federation of American Scientists"
year = 1998
url = "https://nuke.fas.org/guide/russia/agency/bw.htm"
opened = "2026-11-27"

[source.vonbaeckmann-1995]
type = "official-docs"
title = "Nuclear verification in South Africa"
authors = "Adolf von Baeckmann, Garry Dillon, Demetrius Perricos"
year = 1995
url = "https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull37-1/37105394248.pdf"
opened = "2026-11-27"

[source.thorne-1992]
type = "official-docs"
title = "IAEA nuclear inspections in Iraq"
authors = "Leslie Thorne"
year = 1992
url = "https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull34-1/34102451624.pdf"
opened = "2026-11-27"

[source.albright-2002]
type = "report"
title = "Iraq's Programs to Make Highly Enriched Uranium and Plutonium for Nuclear Weapons Prior to the Gulf War"
authors = "David Albright"
year = 2002
url = "https://isis-online.org/isis-reports/detail/iraqs-programs-to-make-highly-enriched-uranium-and-plutonium-for-nuclear-we"
opened = "2026-11-27"

[source.iaea-gov-2011-30]
type = "official-docs"
title = "Implementation of the NPT Safeguards Agreement in the Syrian Arab Republic (GOV/2011/30)"
authors = "IAEA Director General"
year = 2011
url = "https://acronym.org.uk/old/archive/docs/1105/Syria%20IAEA%20Report%20May%202011.pdf"
opened = "2026-11-27"

[source.iaea-gov-2003-40]
type = "official-docs"
title = "Implementation of the NPT Safeguards Agreement in the Islamic Republic of Iran (GOV/2003/40)"
authors = "IAEA Director General"
year = 2003
url = "https://www.iaea.org/sites/default/files/gov2003-40.pdf"
opened = "2026-11-27"

[source.iaea-gov-2003-75]
type = "official-docs"
title = "Implementation of the NPT Safeguards Agreement in the Islamic Republic of Iran (GOV/2003/75)"
authors = "IAEA Director General"
year = 2003
url = "https://www.iaea.org/sites/default/files/gov2003-75.pdf"
opened = "2026-11-27"

[source.iaea-gov-2009-74]
type = "official-docs"
title = "Implementation of the NPT Safeguards Agreement and relevant provisions of Security Council resolutions in the Islamic Republic of Iran (GOV/2009/74)"
authors = "IAEA Director General"
year = 2009
url = "https://www.iaea.org/sites/default/files/gov2009-74.pdf"
opened = "2026-11-27"

[source.whitehouse-2009-qom]
type = "official-docs"
title = "Statements by President Obama, President Sarkozy and Prime Minister Brown on Iranian Nuclear Facility"
authors = "The White House"
year = 2009
url = "https://obamawhitehouse.archives.gov/video/Obama-Sarkozy-and-Brown-on-Iranian-Nuclear-Facility/index__q_page=70.html"
opened = "2026-11-27"

[source.reuters-2025-iran]
type = "news"
title = "Verifying Iran's enriched uranium stock is 'long overdue', IAEA report says"
authors = "Francois Murphy (Reuters)"
year = 2025
url = "https://theprint.in/world/verifying-irans-enriched-uranium-stock-is-long-overdue-iaea-report-says/2782711/"
opened = "2026-11-27"

[source.aljazeera-2026-iran]
type = "news"
title = "IAEA urges Iran to allow inspections, points at Isfahan"
authors = "Al Jazeera staff and AFP"
year = 2026
url = "https://www.aljazeera.com/news/2026/2/27/iaea-eyes-isfahan-nuclear-complex-as-it-urges-iran-to-allow"
opened = "2026-11-27"

[source.iaea-gc37-1084]
type = "official-docs"
title = "Implementation of the Agreement between the Agency and the Democratic People's Republic of Korea for the Application of Safeguards (GC(XXXVII)/1084)"
authors = "IAEA Director General"
year = 1993
url = "https://iaea.org/sites/default/files/gc/gc37-1084_en.pdf"
opened = "2026-11-27"

[source.iaea-gov-2004-12]
type = "official-docs"
title = "Implementation of the NPT Safeguards Agreement of the Socialist People's Libyan Arab Jamahiriya (GOV/2004/12)"
authors = "IAEA Director General"
year = 2004
url = "https://securitycouncilreport.org/atf/cf/%7B65BFCF9B-6D27-4E9C-8CD3-CF6E4FF96FF9%7D/Disarm%20GOV200412.pdf"
opened = "2026-11-27"

[source.crs-2004-libya]
type = "report"
title = "Disarming Libya: Weapons of Mass Destruction (RS21823)"
authors = "Sharon A. Squassoni, Andrew Feickert"
year = 2004
url = "https://www.everycrsreport.com/files/20040422_RS21823_9c2b81fe3a3385f6aa0d78a8ac41e3e8cd0cb7ad.html"
opened = "2026-11-27"

[source.newstart-protocol]
type = "legislation"
title = "Protocol to the Treaty between the United States of America and the Russian Federation on Measures for the Further Reduction and Limitation of Strategic Offensive Arms"
authors = "United States of America and Russian Federation"
year = 2010
url = "https://courses.physics.illinois.edu/phys280/sp2014/archive/2010%20New%20START%20Protocol.pdf"
opened = "2026-11-27"

[source.fas-2026-newstart]
type = "report"
title = "The Aftermath: The Expiration of New START and What It Means For Us All"
authors = "Matt Korda, Eliana Johns, Mackenzie Knight-Boyle, Hans Kristensen"
year = 2026
url = "https://fas.org/publication/the-expiration-of-new-start/"
opened = "2026-11-27"

[source.aca-2026-newstart]
type = "news"
title = "New START Expires As U.S. Urges 'Modernized' Treaty"
authors = "Xiaodon Liang"
year = 2026
url = "https://www.armscontrol.org/act/2026-03/news/new-start-expires-us-urges-modernized-treaty"
opened = "2026-11-27"

[source.nrc-2012-ctbt]
type = "report"
title = "The Comprehensive Nuclear Test Ban Treaty: Technical Issues for the United States"
authors = "National Research Council"
year = 2012
doi = "10.17226/12849"
url = "https://www.nationalacademies.org/read/12849/chapter/5"
opened = "2026-11-27"

[source.ctbto-artxiv-2025]
type = "official-docs"
title = "Background document prepared for the Conference on Facilitating the Entry into Force of the CTBT (CTBT-Art.XIV/2025/3)"
authors = "CTBTO Preparatory Commission, Provisional Technical Secretariat"
year = 2025
url = "https://www.ctbto.org/sites/default/files/2025-09/CTBT-Art.XIV-2025-3.pdf"
opened = "2026-11-27"

[source.baker-2023]
type = "preprint"
title = "Nuclear Arms Control Verification and Lessons for AI Treaties"
authors = "Mauricio Baker"
year = 2023
arxiv = "2304.04123"
opened = "2026-11-27"

[source.shavit-2023]
type = "preprint"
title = "What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring"
authors = "Yonadav Shavit"
year = 2023
arxiv = "2303.11341"
opened = "2026-11-27"

[source.wasil-2024]
type = "preprint"
title = "Verification methods for international AI agreements"
authors = "Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett"
year = 2024
arxiv = "2408.16074"
opened = "2026-11-27"

[source.ho-2023]
type = "preprint"
title = "International Institutions for Advanced AI"
authors = "Lewis Ho, Joslyn Barnhart, Robert Trager, Yoshua Bengio, Miles Brundage, Allison Carnegie, Rumman Chowdhury, Allan Dafoe, Gillian Hadfield, Margaret Levi, Duncan Snidal"
year = 2023
arxiv = "2307.04699"
opened = "2026-11-27"

[source.scher-2025-agreement]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.scher-thiergart-2025]
type = "preprint"
title = "Mechanisms to Verify International Agreements About AI Development"
authors = "Aaron Scher, Lisa Thiergart"
year = 2025
arxiv = "2506.15867"
opened = "2026-11-27"

[source.baker-2025-six-layers]
type = "preprint"
title = "Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment"
authors = "Mauricio Baker, Gabriel Kulp, Oliver Marks, Miles Brundage, Lennart Heim"
year = 2025
arxiv = "2507.15916"
opened = "2026-11-27"

[source.hendrycks-2025]
type = "preprint"
title = "Superintelligence Strategy: Expert Version"
authors = "Dan Hendrycks, Eric Schmidt, Alexandr Wang"
year = 2025
arxiv = "2503.05628"
opened = "2026-11-27"

[source.gan-2026-clock]
type = "preprint"
title = "Agreements Have a Clock: Compute Growth and the Verification of AI Restraint"
authors = "Li Gan"
year = 2026
arxiv = "2611.04272"
opened = "2026-11-27"

[source.barnett-scher-2025]
type = "preprint"
title = "AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research Questions"
authors = "Peter Barnett, Aaron Scher"
year = 2025
arxiv = "2505.04592"
opened = "2026-11-27"

[source.sastry-2024]
type = "preprint"
title = "Computing Power and the Governance of Artificial Intelligence"
authors = "Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield, Richard Ngo, Konstantin Pilz, George Gor, et al."
year = 2024
arxiv = "2402.08797"
opened = "2026-11-27"

[source.avenhaus-2002]
type = "book"
title = "Inspection Games (Handbook of Game Theory with Economic Applications, vol. 3, ch. 51)"
authors = "Rudolf Avenhaus, Bernhard von Stengel, Shmuel Zamir"
year = 2002
doi = "10.1016/S1574-0005(02)03014-X"
url = "https://ideas.repec.org/h/eee/gamchp/3-51.html"
opened = "2026-11-27"

[source.allen-2015-llnl]
type = "report"
title = "Systems Approach to Arms Control Verification (LLNL-CONF-671180)"
authors = "K. Allen, I. Neimeyer, C. Listner, G. Stein, C. Chen, M. Dreicer"
year = 2015
url = "https://www.osti.gov/servlets/purl/1184177"
opened = "2026-11-27"

[source.allison-herzog-2025]
type = "peer-reviewed"
title = "Artificial Intelligence and Nuclear Weapons Proliferation: The Technological Arms Race for (In)visibility"
authors = "David M. Allison, Stephen Herzog"
year = 2025
doi = "10.1111/risa.70105"
arxiv = "2512.07487"
opened = "2026-11-27"

[source.ansari-2026]
type = "preprint"
title = "Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification"
authors = "Samar Ansari"
year = 2026
arxiv = "2604.04712"
opened = "2026-11-27"

[source.alramiah-2025]
type = "preprint"
title = "Toward a Global Regime for Compute Governance: Building the Pause Button"
authors = "Ananthi Al Ramiah, Raymond Koopmanschap, Josh Thorsteinson, Sadruddin Khan, Jim Zhou, Shafira Noh, Joep Meindertsma, Farhan Shafiq"
year = 2025
arxiv = "2506.20530"
opened = "2026-11-27"
```
