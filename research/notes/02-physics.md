# Survey note 02: physics of computation

- **Track:** 02, physics of computation (Landauer, reversible computing, accelerator energy per
  operation, memory and interconnect, the brain as a reference, data-centre power, and the
  observable signatures of large facilities).
- **Date:** 2026-11-27. Every source below was opened on this date unless the entry says otherwise.
- **Scope:** feeds P1 to P4 (especially P2 headroom and P4 footprint floor), F1 (copies and speed),
  O1/O3 (power as an input and a chokepoint) and the protocol's verification channels.
- **Conventions:** quotes are verbatim except that en dashes in ranges are written as hyphens.
  Numbers marked "derived" are my arithmetic on the cited inputs, for the model to recompute; they
  are not claims made by the source.

## Summary: what matters most for Subcritical

1. **P2 has two headrooms, not one.** An H100 SXM at its dense BF16 peak spends about 7.1e-13 J per
   FLOP, about 2.5e8 times kT ln 2 at 300 K (derived; note kT ln 2 is per erased bit, not per
   FLOP). But the binding near-term limit is CMOS, not Landauer: Ho, Erdil and Besiroglu estimate the
   irreversible-CMOS ceiling at about 200 times current GPUs (50% chance), which at the measured
   1.34x to 1.41x a year is reached in roughly 15 to 18 years (derived). Going further needs
   adiabatic or reversible logic, which in 2025 reached a first test chip saving about 30%, and
   experiments that approach kT ln 2 erase one bit in seconds, not nanoseconds.
2. **Memory bandwidth trails compute.** Peak FLOPS grew 3.0x per two years against 1.6x for DRAM
   bandwidth and 1.4x for interconnect (Gholami et al.); bytes per FLOP roughly halved from V100 to
   B200 (derived from datasheets). Low-communication training (DiLoCo: 500 times less
   communication; Streaming DiLoCo: two orders of magnitude less bandwidth) loosens the
   interconnect limit that made frontier training a single-site activity.
3. **Facility power is large and growing fast, and the known sites are tracked from orbit.**
   Leading AI supercomputer power doubled every year 2019-2025 (Colossus: 300 MW in March 2025);
   Epoch's database (Nov 2026) tracks 96 sites, 15.1 GW of IT power and 15.8M H100-equivalents,
   about 43% of world AI compute, with IT power from satellite imagery of cooling equipment within
   1.4x at 80% confidence. The largest 2030 training runs are projected at 4 to 16 GW.
4. **Detection works above about 10 MW and fails below it, and heat is a weak signature.**
   A satellite classifier found every facility above 10 MW and missed every one below it in its
   sample (as reported by Koopmanschap and Barten). A 2026 study of a 126 MW-plus cluster near Tokyo
   found night-time facility-scale surface temperature changes "indistinguishable from zero".
   Water use spans 21 million gallons a day to almost nothing at closed-loop sites. Grid signatures
   (utility system-impact studies at 5 MW, ERCOT's ~410 GW large-load queue) are real but noisy and
   bypassed by behind-the-meter generation.
5. **Against the memo (P4).** Rahman (2026) computes that 1e24 FLOP needs only two 16-H100 nodes
   ($1.6M) and 1e25 FLOP 34 nodes of 16 GH200, over about 100 Mbps links, each node a few tens of kW
   and below any facility signature. A per-site footprint floor therefore does not hold against an
   adversary who distributes; the floor that survives is an aggregate over chips and energy, which
   only chip accounting sees. Scher and Thiergart argue "Track AI Chips, Not Data Centers", and
   Rahman and Koopmanschap and Barten reach compatible conclusions. Analogue power metering detects training against inference well (at least 96%) but
   bounds the amount of hidden compute weakly (it cannot exclude 41% to 116% of declared capacity).
6. **Prior art for P4 exists.** Koopmanschap and Barten (2026) define an "enforcement breaking
   point" and trace detectability against facility size (10,000, 1,000, 100 H100-equivalents);
   Scher and Thiergart, the MIRI draft agreement, AI 2040 and Rahman cover the same ground. In our
   search, P4's footprint floor at most extends prior work.
7. **Brain reference (P1, F1).** Carlsmith: 1e15 FLOP/s is "more likely than not" enough, range
   1e13-1e17, under 10% that more than 1e21 is needed; the brain's ~20 W caps it at about 7e21 bit
   erasures a second. At 1e15 FLOP/s on 20 W the brain is about 35 times as efficient per FLOP as
   an H100 (derived), and one H100's dense BF16 peak is about one brain at Carlsmith's central
   figure (derived, raw FLOP/s only).

---

## Thermodynamic limits and reversible computing

### landauer1961
- **Title:** Irreversibility and Heat Generation in the Computing Process. R. Landauer. IBM Journal
  of Research and Development 5(3), 183-191, July 1961. DOI 10.1147/rd.53.0183 (verified via
  Crossref). Opened as a scanned PDF and read page by page.
- **Abstract (p. 183):** "This logical irreversibility is associated with physical irreversibility
  and requires a minimal heat generation, per machine cycle, typically of the order of kT for each
  irreversible function."
- **Section 4, p. 187:** "The entropy therefore has been reduced by k log_e 2 = 0.6931 k per bit."
  and "supplying 0.6931 kT per restored bit to the surroundings. This is, of course, a minimum
  heating effect, and our method of reasoning gives no guarantee that this minimum is in fact
  achievable."
- **Introduction, p. 183:** the minimum "is many orders of magnitude smaller than the heat
  dissipation in any practically conceivable device."
- **Section 3, p. 186:** a logically reversible machine is possible in principle (the three-input
  example) but must keep or later clear the extra "bias" bits.
- **Bears on:** P2 (the floor itself, per erased bit, and Landauer's own warning that it may not be
  reachable).

### berut2012
- **Title:** Experimental verification of Landauer's principle linking information and
  thermodynamics. A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider, E. Lutz.
  Nature 483(7388), 187-189, 2012. DOI 10.1038/nature10872.
- **Opened:** only the bibliographic record and abstract (RePEc/IDEAS); the Nature page was behind
  a login and the course-site PDF was gone. The abstract reports an "Experimental demonstration of
  the Landauer bound in a generic one-bit memory." The numbers are taken from the authors' longer
  2015 paper below.
- **Bears on:** P2.

### berut2015
- **Title:** Information and thermodynamics: Experimental verification of Landauer's erasure
  principle. A. Bérut, A. Petrosyan, S. Ciliberto. J. Stat. Mech. (2015) P06015, DOI
  10.1088/1742-5468/2015/06/P06015; arXiv 1503.06537. Full text read.
- **Section 1:** kB T ln 2 "represents only ∼ 3 × 10−21 J at room temperature (300 K)".
- **Section 2.1:** one-bit memory is a silica bead, "radius R = 1.00 ± 0.05 µm", in a double well
  made by a 1024 nm laser switched at 10 kHz.
- **Section 3, Fig. 8:** erasure durations τ up to 40 s. "A numerical least square fit hQi→0 = ln 2
  + B/τ ... gives a value of B = 8.15 kB T s. If we do a fit with two free parameters ... we find
  A = 0.72 kB T which is close to kB T ln 2 ≈ 0.693 kB T." The mean heat "approaches the Landauer's
  bound kB T ln 2 for long times".
- **Why it matters:** the bound is reached only for slow erasure. Extrapolating the fitted B/τ term
  to τ = 1 ns gives about 8e9 kT (derived, an extrapolation far outside the measured range, shown
  only to make the speed-energy trade-off concrete).
- **Bears on:** P2 (Landauer is a slow-limit bound; fast computation pays more).

### hong2014
- **Title:** Experimental verification of Landauer's principle in erasure of nanomagnetic memory
  bits. J. Hong, B. Lambson, S. Dhuey, J. Bokor. arXiv 1411.6730 (2014). Full text read. Published
  as "Experimental test of Landauer's principle in single-bit operations on nanomagnetic memory
  bits", Science Advances 2016, DOI 10.1126/sciadv.1501492 (metadata checked via Crossref; the
  published text was not opened).
- **Says:** kT ln 2 "corresponds to a value of 2.8 zJ (2.8×10-21 J) at 300K". Measured dissipation
  "(6.09 ± 1.43) zJ at T = 300K ... consistent with a value of (1.45 ± 0.35)kBT"; a second set
  "(4.2 ± 0.9) zJ, which corresponds with a value of (1.0 ± 0.22)kBT". Abstract: "consistent
  (within two standard deviations of experimental uncertainty) with the Landauer limit during an
  adiabatic erasure process."
- **Bears on:** P2 (the bound holds in a practical digital-memory technology, not only a colloid).

### bennett2003
- **Title:** Notes on Landauer's principle, Reversible Computation and Maxwell's Demon.
  C. H. Bennett. Studies in History and Philosophy of Modern Physics 34, 501-510 (2003);
  arXiv physics/0210005. Abstract read.
- **Says:** Landauer's principle "holds that any logically irreversible manipulation of
  information, such as the erasure of a bit or the merging of two computation paths, must be
  accompanied by a corresponding entropy increase in non-information bearing degrees of freedom";
  "any logically reversible transformation of information can in principle be accomplished by an
  appropriate physical mechanism operating in a thermodynamically reversible fashion."
- **Bears on:** P2 (Landauer is not a floor for reversible computation, so the true physical
  headroom is larger still, in principle).

### ho2023
- **Title:** Limits to the Energy Efficiency of CMOS Microprocessors. A. Ho, E. Erdil,
  T. Besiroglu (Epoch AI). arXiv 2312.08595 (Dec 2023). Full text read.
- **Abstract:** "Combining these yields a geometric mean estimate of 4.7 × 10^15 FP4/J for the
  maximum CMOS energy efficiency, roughly two hundred-fold more efficient than current
  microprocessors."
- **Results:** transistor-switching bound [3.3e14, 1.1e18] FLOP/J (midpoint 1.9e16);
  interconnect bound [1.5e13, 1.3e18] FLOP/J; combined geometric mean 4.7e15 with "a standard
  deviation (in log space) of around 0.7 OOMs". "Roughly 30 transistors are switched per FLOP, at a
  minimum."
- **Implications section:** H100 dense efficiency "around (10^15 FP16/s)/(700 W) ≈ 1.4 × 10^12
  FP16/J"; scaling quadratically with precision, the ceiling "corresponds to a forecast of
  4.7 × 10^15/16 = 2.9 × 10^14 FP16/J. Our results, therefore, suggest that there is a 50% chance
  that further improvements in energy efficiency will cease after another 290/1.4 ≈ 207-fold of
  improvement on existing technology." Caveat: "our calculations only hold in the irreversible
  regime".
- **Error noted:** Section II gives kB T ln 2 at 300 K as "4 × 10−21 J"; the correct value is
  2.87e-21 J (4.1e-21 J is kT). It does not change their result materially.
- **Bears on:** P2 (the practical headroom is about 2 orders of magnitude, not 8), P4 (how far
  hardware alone can shrink the footprint of fixed compute).

### genkina2025
- **Title:** Reversible Computing Escapes the Lab in 2025. D. Genkina, IEEE Spectrum, 2 Jan 2025
  (updated 22 May 2025). URL below.
- **Says:** Vaire "has announced tape-out of their first reversible computing chip prototype,
  capable of recovering 50% of the energy used in the resonator circuit." Sandia work suggests
  reversible computing "may offer up to a 4,000x energy-efficiency gain"; "The 4,000x
  energy-efficiency improvement is on Vaire's road map but probably 10 or 15 years out." "In every
  real implementation, some amount of energy is still lost with each swing." Earlier demonstrations
  recovered energy in the circuit but "the wall-plug power usage was not necessarily reduced".
- **Bears on:** P2 (state of the art beyond CMOS: vendor road map, not measurement).

### hulick2025
- **Title:** This experimental computer chip reuses energy. K. Hulick, Science News, 23 Sep 2025.
- **Says:** "The new chip, tested in August, drew around 30 percent less energy than a regular chip
  performing the same computation." Adiabatic computing "is a slow process"; it "will take a long
  time to become more mainstream". The figure comes from one test; no independent verification is
  described.
- **Bears on:** P2 (reversible logic exists in silicon but gives tens of percent, not orders of
  magnitude, today).

### codata2022-k
- **Title:** CODATA 2022 value of the Boltzmann constant, NIST.
- **Says:** k = "1.380 649 x 10-23 J K-1", "(exact)". kT ln 2 = 2.871e-21 J at 300 K and
  2.967e-21 J at 310 K (derived).
- **Bears on:** P2.

## Energy efficiency of computing over time

### koomey2011
- **Title:** Implications of Historical Trends in the Electrical Efficiency of Computing.
  J. G. Koomey, S. Berard, M. Sanchez, H. Wong. IEEE Annals of the History of Computing 33(3),
  46-54 (2011). DOI 10.1109/MAHC.2010.28. Full text read.
- **Says:** "The electrical efficiency of computation has doubled roughly every year and a half for
  more than six decades"; computations per kilowatt-hour "doubled every 1.57 years from 1946 to
  2009"; personal computers alone 1.52 years (1975-2009). Feynman (1985) estimated "a factor of
  10^11 improvement that was theoretically possible"; since then performance per kWh "has improved
  by a factor of 4 × 10^4".
- **Bears on:** P2 (long-run trend).

### koomey2015
- **Title:** Moore's Law Might Be Slowing Down, But Not Energy Efficiency. J. Koomey,
  S. Naffziger, IEEE Spectrum, 31 Mar 2015.
- **Says:** the 1.5-year doubling "began to come to an end around 2000. These days, we've found, it
  takes about 2.7 years for peak-output efficiency to double." Typical-use efficiency was projected
  to "double every 1.5 years or so" through 2020.
- **Bears on:** P2 (the slowdown).

### epoch-hw-efficiency-2024
- **Title:** Leading ML hardware becomes 40% more energy-efficient each year. R. Rahman, Epoch AI,
  23 Oct 2024 (dataset updated 24 Nov 2025).
- **Says:** "Historically, the energy efficiency of leading GPUs and TPUs has doubled every 2
  years." Table (tensor FP16 where available, FLOP/s per watt): H100 SXM5 1.41e12, B200 2.25e12,
  B100 2.50e12, TPU v4 1.62e12, TPU v5e 1.41e12. The text calls Meta MTIA the most efficient at
  "up to 2.1 x 10^12", which the table contradicts (B100 2.50e12). Whether power is TDP or measured
  is not stated.
- **Bears on:** P2, P4 (rate at which a fixed computation's power falls).

### hobbhahn2023
- **Title:** Trends in machine learning hardware. M. Hobbhahn, L. Heim, G. Aydos, Epoch AI,
  9 Nov 2023.
- **Says (47 ML accelerators, FP32):** FLOP/s "doubling every ~2.3 years"; FLOP per $ "doubling
  every 2.1 years for ML GPUs"; FLOP/s per watt "doubling every 3.0 years for ML GPUs and 2.7 years
  for general GPUs"; "Memory capacity is doubling every ~4 years and memory bandwidth every ~4.1
  years"; "NVLink in H100 supports 7x the bandwidth of PCIe 5.0." Interconnect doubling time not
  estimated.
- **Bears on:** P2, P3.

## Accelerator specifications

### nvidia-v100
- **Title:** NVIDIA V100 Tensor Core GPU datasheet (file revision r5, undated). Vendor PDF.
- **Says:** tensor performance 112 TFLOPS (PCIe), 125 TFLOPS (SXM2), 130 TFLOPS (V100S PCIe);
  memory bandwidth 900 GB/s (1134 GB/s for V100S); NVLink 300 GB/s (PCIe 32 GB/s); max power 250 W
  (PCIe) and 300 W (SXM2).
- **Bears on:** P2, P3.

### nvidia-a100
- **Title:** NVIDIA A100 Tensor Core GPU datasheet (June 2021). Vendor PDF.
- **Says (80GB SXM):** FP16/BF16 tensor "312 TFLOPS | 624 TFLOPS*" (* with sparsity); GPU memory
  bandwidth 2,039 GB/s; max TDP 400 W; NVLink 600 GB/s; PCIe Gen4 64 GB/s.
- **Bears on:** P2, P3.

### nvidia-h100
- **Title:** NVIDIA H100 Tensor Core GPU product page, specifications table.
- **Says (H100 SXM):** BF16 tensor 1,979 TFLOPS, FP8 3,958 TFLOPS, both footnoted "With
  sparsity" (dense is half: 989.5 and 1,979); 80 GB; 3.35 TB/s; "Up to 700W (configurable)";
  NVLink 900 GB/s; PCIe Gen5 128 GB/s.
- **Bears on:** P2, P3, P1 (the reference unit "H100-equivalent" used across the governance
  literature).

### nvidia-gb200
- **Title:** NVIDIA GB200 NVL72 product page, specifications table.
- **Says (72-GPU rack):** FP16/BF16 tensor 360 PFLOPS and FP8 720 PFLOPS, sparse ("Dense is
  one-half sparse spec shown"); NVFP4 "1,440 sparse / 720 dense PFLOPS"; 13.4 TB HBM3E at
  576 TB/s; NVLink 130 TB/s. Per GPU (derived): 2.5 PFLOPS dense BF16, 8 TB/s HBM, 1.8 TB/s NVLink.
  No rack power is given on the page.
- **Bears on:** P2, P3.

### nvidia-dgx-b200
- **Title:** NVIDIA DGX B200 product page.
- **Says:** eight Blackwell GPUs, 1,440 GB HBM3e at 64 TB/s; FP8 72 PFLOPS sparse; NVLink 14.4 TB/s
  aggregate; networking up to 400 Gb/s InfiniBand or Ethernet per port; system power "~14.3 kW
  max". Derived: about 1.8 kW per GPU at system level and 2.25 PFLOPS dense BF16 per GPU, so
  about 1.26e12 FLOP/J at the system wall (not chip TDP).
- **Bears on:** P2, P3 (scale-up NVLink 1.8 TB/s against scale-out 400 Gb/s = 50 GB/s per GPU, a
  factor of about 36, derived).

### amd-mi300x
- **Title:** AMD Instinct MI300X data sheet. Vendor PDF.
- **Says:** FP16 1307.4 TFLOPS (2614.9 with sparsity); FP8 2614.9 (5229.8 with sparsity); "Up to
  192 GB HBM3"; "5.3 TB/s max. peak theoretical"; "Maximum TBP 750W"; "Scale-up Infinity Fabric
  Links 7x 128 GB/s".
- **Bears on:** P2, P3.

### google-ironwood-2025
- **Title:** Ironwood: The first Google TPU for the age of inference. A. Vahdat, Google blog,
  9 Apr 2025.
- **Says:** "Each individual chip boasts peak compute of 4,614 TFLOPs" (FP8 per the figure
  captions); "192 GB per chip"; HBM "7.37 TB/s per chip"; ICI "1.2 TBps bidirectional"; pods of
  "9,216 liquid cooled chips" for "a total of 42.5 Exaflops"; "Ironwood perf/watt is 2x relative
  to Trillium" and "nearly 30x more power efficient than our first Cloud TPU from 2018." No chip
  power is stated.
- **Bears on:** P2, P3.

## Memory and interconnect

### gholami2024
- **Title:** AI and Memory Wall. A. Gholami, Z. Yao, S. Kim, C. Hooper, M. W. Mahoney, K. Keutzer.
  arXiv 2403.14123 (Mar 2024); published in IEEE Micro (volume not checked). Abstract read.
- **Says:** "Over the past 20 years, peak server hardware FLOPS has been scaling at 3.0x/2yrs,
  outpacing the growth of DRAM and interconnect bandwidth, which have only scaled at 1.6 and 1.4
  times every 2 years, respectively."
- **Bears on:** P3 (memory bandwidth per copy bounds serial speed, and it grows slowest).

### douillard2023
- **Title:** DiLoCo: Distributed Low-Communication Training of Language Models. A. Douillard et al.
  (Google DeepMind). arXiv 2311.08105. Abstract read.
- **Says:** enables training "on islands of devices that are poorly connected"; "On the widely used
  C4 dataset, we show that DiLoCo on 8 workers performs as well as fully synchronous optimization
  while communicating 500 times less."
- **Bears on:** P3, P4 (loosens the single-site requirement).

### douillard2025
- **Title:** Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch.
  A. Douillard et al. arXiv 2501.18512. Abstract read.
- **Says:** synchronizing "only subsets of parameters in sequence, rather than all at once, which
  greatly reduces peak bandwidth"; with "billion-scale parameters" they "reach similar quality as
  before, but reducing required bandwidth by two orders of magnitude."
- **Bears on:** P3, P4.

### erdil2024
- **Title:** Data movement limits to frontier model training. E. Erdil, D. Schneider-Joseph.
  arXiv 2411.01137. Abstract read.
- **Says:** "data movement bottlenecks begin to significantly lower hardware utilization for training
  runs exceeding about 10^28 FLOP, two orders of magnitude above the largest training run to date,
  suggesting the arrival of fundamental barriers to scaling in three years given recent rates of
  growth. A training run exceeding about 10^31 FLOP is infeasible even at low utilization."
- **Bears on:** P3, P1 (a physical ceiling on single-run scale that sits far above a D1 threshold
  if algorithms carry most of the load).

### sevilla2025-decentralized
- **Title:** How far can decentralized training over the internet scale? J. Sevilla, Epoch AI
  (Gradient Updates), 29 Dec 2025.
- **Says:** decentralized training compute grew "for an implied growth rate of about 20x/year";
  the largest runs "span the 6e22-6e23 FLOP range" and used about "1000x less compute than what we
  estimated was used to train the largest models today"; consumer upload "around 60 Mbps";
  decentralized training is "technically feasible at frontier scale" but unlikely to gather
  frontier compute this decade. Policy: many monitoring proposals "depend on internet decentralized
  training continuing to lag far behind the frontier."
- **Bears on:** P3, P4 (a 20x a year trend that erodes the facility channel), O1.

### sevilla2025-power
- **Title:** Could decentralized training solve AI's power problem? J. Sevilla, A. Troynikov,
  Epoch AI, 28 Oct 2025.
- **Says:** sketches a 10 GW run "using spare capacity from 23 existing gas power plants", "a 6Pbps
  connection between each pair of adjacent data centers", a ring of about 4,800 km of fibre adding
  about 24 ms; largest spare-capacity site "approximately 800MW"; developers "only resort to
  decentralized clusters when no other option is available".
- **Bears on:** P3, P4 (multi-site training at GW scale is planned around, not exotic).

### meta-infra-2025
- **Title:** Meta's Infrastructure Evolution and the Advent of AI. Y. J. Song, K. Veeraraghavan,
  Meta Engineering, 29 Sep 2025.
- **Says:** "Prometheus, will be a 1-gigawatt cluster spanning across multiple data center
  buildings"; "the Hyperion cluster will have the ability to scale up to a capacity of 5 gigawatts"
  and is "expected to come online beginning in 2028"; Meta built "a single AI cluster with 129k H100
  GPUs" and is changing software to "support long-distance training across a geographically
  distributed set of data centers."
- **Bears on:** P3, P4 (a frontier lab itself moving to geographically distributed training).

### krys2025
- **Title:** Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI
  Landscape. J. Kryś, Y. Sharma, J. Egan. arXiv 2507.07765 (ICML 2025 TAIG workshop). Abstract read.
- **Says:** low-communication algorithms "are enabling a shift from centralised model training";
  risks include "compute structuring" and "the erosion of detectability and shutdownability";
  "certain policy levers, like export controls, remain relevant."
- **Bears on:** P4, protocol verification channels.

### rahman2026
- **Title:** Does Distributed Training Undermine Compute Governance? R. Rahman. arXiv 2605.29359
  (May 2026). Full text read.
- **Says:** "If a frontier-scale cluster were split into nodes smaller than the regulator's
  monitoring threshold, it would be undetectable by thermal and electrical means". Table 1
  (minimum-cost configurations): 1e24 FLOP with 2 nodes of 16 H100 FP8, efficiency η 0.80, cost
  $1.6M; DeepSeek-V3 scale (3.3e24) with 7 nodes of 16 GH200, $6.3M; 1e25 with 34 nodes, η 0.37,
  quality-adjusted 6.4e24, $30.7M; Llama 3.1-405B scale (3.8e25 local) with 625 nodes of 50 A100,
  η 0.15, quality-adjusted 1.2e25, $441M; 1e26 local with 4,706 nodes of 16 H100, quality-adjusted
  only 2.1e25, $3.80B. "At 100 Mbps bandwidth, it costs about 3× more to do training distributed
  relative to centralized". Thresholds of 1e24, 1e25 and 1e26 FLOP "could be evaded using $1.6M,
  $31M, and $3.8B, respectively, of hardware arranged in clusters smaller than any proposed
  registration requirement." Maximum sensible run length T = 1/(gH + gS + gI), about 4.5 months
  today; under the growth rates assumed for a pause, runs of up to about two years.
- **Bears on:** P4 directly (per-site floor collapses; the floor that survives is aggregate),
  P3, D3 (longer runs under a pause), protocol (chip tracking, memory thresholds, whistleblowing).

## The brain as a reference point

### carlsmith2020
- **Title:** How Much Computational Power Does It Take to Match the Human Brain? J. Carlsmith,
  Open Philanthropy, published 11 Sep 2020. The original URL now redirects to coefficientgiving.org,
  which returned 403; opened through the Internet Archive copy of the original page.
- **Says (summary):** "I think it more likely than not that 10^15 FLOP/s is enough to perform tasks
  as well as the human brain (given the right software, which may be very hard to create). And I
  think it unlikely (<10%) that more than 10^21 FLOP/s is required." Mechanistic method: "Overall
  range: ~1e13-1e17 FLOP/s". Communication method (AI Impacts, TEPS): "~1e16-3e17 FLOP/s".
- **Limit method (Section 4.1.2):** "Most estimates I've seen of the brain's energy budget vary
  between ~10-20W"; "I'll use 20W as a high end"; at about 310 K, "Landauer's principle tells us that
  this causal structure ... cannot involve erasing more than 7e21 bits/second." It cites Sandberg
  (2016): "20 W divided by 1.3 × 10^-21 J (the Landauer limit at body temperature) suggests a limit
  of no more than 1.6·10^22 irreversible operations per second" (the 1.3e-21 J figure looks low;
  kT ln 2 at 310 K is 2.97e-21 J, which gives Carlsmith's 7e21).
- **Bears on:** P1 (reference, not target), P2 (biology runs far above Landauer too), F1 (copies
  per held compute).

### sandberg2008
- **Title:** Whole Brain Emulation: A Roadmap. A. Sandberg, N. Bostrom. Technical Report #2008-3,
  Future of Humanity Institute, Oxford University (2008). FHI's site is closed; opened through the
  Internet Archive copy of the report PDF (130 pages).
- **Says:** Table 9, p. 80 ("Processing demands (emulation only, human brain)"): level 3 analog
  network population model 10^15 FLOPS; level 4 spiking neural network 10^18; level 5
  electrophysiology 10^22; level 6 metabolome 10^25; level 7 proteome 10^26; level 8 states of
  protein complexes 10^27; level 9 distribution of complexes 10^30; level 10 stochastic behaviour of
  single molecules 10^43. Workshop poll (section on emulation levels, before Table 9): "The
  consensus appeared to be level 4-6."
- **Bears on:** P1 (emulation is a far costlier route than functional equivalence: 1e18-1e25 FLOPS
  at the consensus levels).

### levy2021
- **Title:** Communication consumes 35 times more energy than computation in the human cortex, but
  both costs are needed to predict synapse number. W. B. Levy, V. G. Calvert. PNAS 118(18)
  e2008173118 (2021). DOI 10.1073/pnas.2008173118. Abstract read through Europe PMC (the PNAS
  page returned 403; full text was not retrieved).
- **Says:** "rather than the oft-quoted 20 W of glucose available to the human brain, the fraction
  partitioned to cortical computation is only 0.1 W of ATP"; "long-distance communication costs are
  35-fold greater, 3.5 W." The abstract's figure for the discrepancy between biological and lowest
  possible computational efficiency did not render in the retrieved text, so it is not reported.
- **Bears on:** P1, P2, P3 (even in the brain, moving information costs more than computing).

## Data-centre power: totals, trends and the largest sites

### iea2025
- **Title:** Energy and AI (Executive summary). International Energy Agency, Paris, 2025.
- **Says:** "Data centres accounted for around 1.5% of the world's electricity consumption in 2024,
  or 415 terawatt-hours (TWh)"; "set to more than double to around 945 TWh by 2030"; growth "around
  12% per year since 2017"; the US "45%" of 2024 consumption; "A typical AI-focused data centre
  consumes as much electricity as 100 000 households, but the largest ones under construction today
  will consume 20 times as much"; 2035 range "700 to 1 700 TWh".
- **Bears on:** P4, O1.

### shehabi2024
- **Title:** 2024 United States Data Center Energy Usage Report. A. Shehabi, S. Smith, A. Hubbard,
  A. Newkirk, N. Lei, A. B. Saddik, B. Holecek, J. Koomey, E. Masanet, D. Sartor. Lawrence Berkeley
  National Laboratory, LBNL-2001637, December 2024. Full PDF read.
- **Says:** US data centres "reaching 176 TWh by 2023, representing 4.4% of total U.S. electricity
  consumption"; 2028 range "roughly 325 and 580 TWh", which at 50% utilisation is "between 74 and
  132 GW" and "6.7% to 12.0%" of US electricity (Executive summary). Water (p. 55): direct use was
  21.2 billion litres in 2014 and 66 billion litres in 2023; hyperscale sites in 2028 "between 60
  and 124 billion liters"; indirect water through electricity "nearly 800 billion liters" (p. 56).
- **Bears on:** P4, O1.

### smith2026
- **Title:** United States Data Center Energy Usage Report: 2025 Update. S. J. Smith, A. Hubbard,
  A. Newkirk, M. Ganeshalingam, et al. LBNL-2001758, published 18 Jun 2026. DOI 10.71468/P1RP4F.
  Full PDF read.
- **Says:** 2024 use "is 192 terawatt-hours (TWh), accounting for 4.7% of total U.S. electricity
  consumption"; 2028 reference 464 TWh; 2030 reference "649 TWh, representing 11.8%"; compounded
  uncertainty range "521-843 TWh"; "148 gigawatts (GW) of interconnection capacity needed to serve
  data centers in 2030", an average "17.4 GW/year from 2024-2030".
- **Bears on:** P4, O1 (grid capacity as an input).

### pilz2025
- **Title:** Trends in AI Supercomputers. K. F. Pilz, J. Sanders, R. Rahman, L. Heim. arXiv
  2504.16026 (Apr 2025). Full text read.
- **Says:** dataset of "500 AI supercomputers from 2019 to 2025"; performance "doubled every nine
  months" (2.5x a year, 90% CI 2.4-2.7); "hardware acquisition cost and power needs both doubled
  every year" (power 2.0x a year, 90% CI 1.6-2.2, Fig. 10); "xAI's Colossus, used 200,000 AI chips,
  had a hardware cost of $7B, and required 300 MW of power"; by 2030, if trends hold, "2×10^22
  16-bit FLOP/s ... two million AI chips, ... $200 billion, and require 9 GW of power". Energy
  efficiency (Section 3.2.1) "improved by 1.34× every year" (90% CI 1.25-1.43), mostly from new
  chips; PUE improved "less than 5% each year". The US "accounts for about three-quarters" of
  performance, China about 15%.
- **Bears on:** P1, P2, P4, O1.

### emberson2024
- **Title:** The power required to train frontier AI models is doubling annually. L. Emberson,
  R. Rahman, Epoch AI, 19 Sep 2024.
- **Says:** "We estimate that power draw has grown by 2.1x per year, with a 90% confidence interval
  of 1.9 to 2.2x." The table lists Grok 3 (Feb 2025) at about 1.1e8 W (110 MW).
- **Bears on:** P4.

### you2025
- **Title:** How much power will frontier AI training demand in 2030? J. You, D. Owen, Epoch AI with
  EPRI, 11 Aug 2025.
- **Says:** "the largest runs now exceeding 100 MW"; growth "at a rate of 2.2x per year", forecast
  2.2x to 2.9x; GPU energy efficiency "has improved by 40% per year"; the largest 2030 runs "will
  likely draw 4-16 gigawatts (GW) of power"; more than 50 GW of US AI power plausible by 2030;
  distributed training "may enable training runs to grow beyond the power constraints for single
  sites."
- **Bears on:** P4, O1.

### sevilla2024
- **Title:** Can AI scaling continue through 2030? J. Sevilla, T. Besiroglu, B. Cottier, J. You,
  E. Roldán, P. Villalobos, E. Erdil, Epoch AI, 20 Aug 2024.
- **Says:** "on-trend 2e29 FLOP training runs in 2030 will require" about 200 times Llama 3.1 405B's
  power, "for a power demand of 6 GW"; campuses of "1 to 5 gigawatt (GW)" support 1e28 to 3e29 FLOP;
  distributed networks of 2 to 45 GW allow "training runs of 2e28 to 2e30 FLOP"; chip production
  allows 1e29 to 5e30; data 6e28 to 2e32; the "latency wall" caps runs at 3e30 to 1e32. Power is the
  constraint likely to bind first.
- **Bears on:** P1, P3, P4, O1.

### lee2025
- **Title:** Today's largest data center can do more than 20 GPT-4-scale training runs each month.
  J. Lee, Epoch AI, 4 Dec 2025.
- **Says:** "Microsoft's Fairwater Atlanta data center is already capable of doing 23 training runs
  as large as GPT-4's each month" (about 531,000 H100-equivalents, Aug 2025); Fairwater Wisconsin
  projected above 225 per month by late 2027. GPT-4's compute and the utilisation assumed are not
  stated on the page.
- **Bears on:** P4 (the inverse of a footprint floor: compute per facility per month), D3.

### epoch-datacenters-2026
- **Title:** AI data centers (Frontier Data Centers hub): database, methodology page, and CSV
  downloads (data_centers.csv, data_center_timelines.csv). Epoch AI, last updated 23 Nov 2026.
- **Says (data page):** 96 sites, 15.1 GW IT power, about 15.8M H100-equivalents; coverage of
  global deployed AI compute 43% as of 27 Nov 2026 (90% CI 29% to 77%); "We expect that 80% of the
  time, a given IT power capacity estimate is accurate within a factor of 1.4x"; compute within
  1.5x, cost 1.6x; "80% of the time, our estimated date is within 6 months of the actual date."
- **Says (methodology):** sites are found "through company announcements, news outlets, third-party
  databases, social media posts"; imagery features are cooling equipment ("rectangular units with
  fans on top"), backup generators and substations; the cooling model uses "the number of fans, the
  diameter of the fans"; IT power is cooling capacity over a cooling overhead, facility power is IT
  power times peak PUE (1.2 hyperscalers, 1.4 others); "Specification data suggests that the actual
  cooling capacity can be as much as 2× higher or lower than our model predicts"; reference checks
  fall between 77% and 118%; "we sometimes use video and thermal imagery captured by drones";
  smaller sites "(<100 MW)" are hard to find; some sites have no obvious external cooling.
- **From the CSVs (my reading):** largest current IT power: Anthropic-Amazon New Carlisle 1,037 MW
  (Trainium2), Colossus 2 946 MW (B200/B300, about 1.11M H100e), OpenAI Stargate Abilene 824 MW
  (about 1.02M H100e), Microsoft Fairwater Atlanta 636 MW; 43 of the 96 sites are below 100 MW.
  Colossus 1 timeline: construction start 24 Apr 2024; 100,000 H100 online 2 Sep 2024 at 139 MW IT
  and 181 MW facility power (derived: 1.39 kW IT and 1.81 kW facility per H100); 200,000 H100e at
  278/361 MW by 17 Feb 2025. Colossus 2 on 8 Sep 2025: "121 air-cooled chillers installed, which
  could support 200 MW". Meta Hyperion first phase estimated for 1 Jan 2028 at 1,632 MW IT,
  2,203 MW facility. Water use: New Carlisle 21.0 million gallons a day at 1,244 MW facility power
  (Oct 2026) against Microsoft Fairwater Wisconsin 0.0077 MGD at 442 MW (Apr 2026).
- **Bears on:** P4 (what satellites see of known sites, and how precisely), P1, O1, D3 (build time
  of about four months from site to 100k H100s).

### openai-stargate-2025
- **Title:** OpenAI, Oracle, and SoftBank expand Stargate with five new AI data center sites.
  OpenAI, 23 Sep 2025.
- **Says:** Abilene is "already up and running on Oracle Cloud Infrastructure"; Oracle "began
  delivering the first NVIDIA GB200 racks in June"; "an additional potential expansion of 600
  megawatts near the flagship Stargate site in Abilene, Texas"; the programme reaches "nearly 7
  gigawatts of planned capacity". Abilene's own capacity is not stated.
- **Bears on:** P4, O1.

## Observable signatures and detection

### mlgw2025
- **Title:** MLGW public update regarding utility support for xAI. Memphis Light, Gas and Water,
  5 May 2025.
- **Says:** "a 'large electric load' which we define as 5MW or higher, MLGW and TVA both require a
  system impact study", a process "dictated and enforced by the Federal Energy Regulatory
  Commission"; xAI "is receiving 150MW of power" (8 MW from an existing substation, 142 MW from a new
  one) and requested 150 MW more; "MLGW has no role in xAI's use of turbines" and no authority over
  power "behind the meter".
- **Bears on:** P4 (grid paperwork is a real signature at 5 MW, and on-site generation bypasses it).

### ercot2026
- **Title:** ERCOT Update, Senate Committee on Business & Commerce. P. Vegas (ERCOT), 1 Apr 2026.
- **Says:** "ERCOT is tracking approximately 410 GW of Large Loads seeking interconnection of which
  ~87% are data centers" (as of 26 Mar 2026); generation queue 453,562 MW; moving to a batch study
  process.
- **Bears on:** P4 (interconnection requests are public but dominated by speculative load, so a
  large request is not evidence of a training run).

### krawec2026
- **Title:** Tracking Hyperscale AI Data Center Growth with Satellite Imagery. C. Krawec,
  Federation of American Scientists, 12 May 2026.
- **Says:** "A high-resolution image is considered anything better than one-meter resolution";
  features identifiable "on imagery of at least 50-centimeter resolution"; air-cooled chillers
  "generally visible only above 30 cm resolution"; water-cooled chillers usually indoors and not
  visible. The study does not use thermal imagery and proposes it as future work (SatVu HotSat-2,
  3.5 m). For Colossus, a substation was estimated at about 150 MW against an actual 142 MW, and
  Epoch's cooling-based estimates spanned about 200-500 MW against a published 300 MW. Finding
  undeclared hyperscale sites from scratch "may not be feasible"; imagery should be one tool among
  several, after the IAEA's safeguards imagery.
- **Bears on:** P4, protocol (satellites confirm and size known sites; they are weak at discovery).

### jing2026
- **Title:** Satellite observations and energy balance constrain the thermal footprint of a
  hyperscale data-centre cluster. J. Jing. Environmental Research Letters 21, 204030 (2026),
  published 4 Nov 2026. DOI 10.1088/1748-9326/aead02. Article page read (abstract and opening
  sections).
- **Says:** uses "daytime Landsat (2013-2026), 70 m day/night ECOSTRESS and 1 km MODIS" over 12
  data centres near Tokyo, a cluster drawing "at least ∼126 MW in FY2023". "Commissioning cools the
  daytime LST by 1.8 °C-2.2 °C" (roof albedo); "Deep-night facility-scale LST changes are
  indistinguishable from zero (bounded below ∼0.6 °C-1.2 °C)"; cluster-scale night bound
  "0.24 °C-0.29 °C"; "kilometre-scale surface warming from waste heat is unattainable".
- **Bears on:** P4 directly (thermal infrared from orbit does not see the waste heat of a 100 MW
  class cluster at current resolutions).

### marinoni2026
- **Title:** The data heat island effect: quantifying the impact of AI data centers in a warming
  world. A. Marinoni et al. arXiv 2603.20897 (v3, Apr 2026). Abstract read.
- **Says:** "the land surface temperature increases by 2°C on average" after an AI data centre
  starts operating; "more than 340 million people could be affected". The abstract gives no
  dataset size, sensor or method for separating the facility's effect.
- **Bears on:** P4 (the claim jing2026 disputes on energy-balance grounds; contested, preprint).

### koopmanschap2026
- **Title:** How to Catch a GPU: A Taxonomy of Verification and Enforcement Mechanisms for
  International AI Agreements. R. Koopmanschap, O. Barten (Existential Risk Observatory). arXiv
  2607.22619 (Jun 2026). Full text read.
- **Says:** "wherever sufficient capacity exists to violate an agreement, it must be under a control
  regime"; "We define the enforcement breaking point as the FLOP-threshold or equivalent metric at
  which a policy loses its effectiveness". Section 5.3.1: "Satellite surveillance reliably detects
  facilities above 10 MW (∼10,000 H100-equivalents ...) and might fail below this range"; at 1,000
  H100e air-cooled chillers are common and harder to distinguish; "At 100 H100-equivalents the
  facility fits inside a 12-meter container with no noticeable external cooling". Appendix B
  reports Clymer's classifier: "All four false negatives ... had power capacity below 10 MW (1.2,
  0.5, 3.2, and 0.5 MW)"; "Above 10 MW the classifier achieved a 100% true positive rate". Power
  monitoring: a 100 kW load "sits within the existing population of mid-size commercial customers,
  which number in the millions". Chips: Epoch traced 15.7M of 20.2M chips to owners, leaving "on
  the order of a million chips unaccounted for", "an approximate bound on the size of the largest
  hidden cluster". Conclusion: "Detect hidden capacity is the sub-problem most likely to become
  intractable as the threshold lowers."
- **Bears on:** P4 (closest prior work found), protocol (detection channels by facility size).
  Note it uses about 1 kW per H100e, below the 1.8 kW per H100 facility figure from Colossus 1.

### teague2026
- **Title:** Could Underwater Data Centers Pose a Risk to AI Treaty Verification? J. Teague,
  A. Rajmohan, Y. Muehlhaeuser. arXiv 2609.18824 (Sep 2026). Full text read.
- **Says:** "100k H100s draw ∼70 MW at the GPUs alone", server and fabric overhead "push this toward
  ∼150 MW", 200 MW a plausible high end for newer chips. "Thermal detection of an operational pod is
  unlikely outside shallow, calm water"; Landsat-8 thermal "coarse resolution (100 m)"; HotSat-2 is
  mid-wave (3.7-5 µm) not long-wave; optical/SAR is strongest "during construction and maintenance".
  Underwater sites are "comparatively unlikely" relative to "underground or industrially disguised
  land-based facilities".
- **Bears on:** P4 (signatures concentrate at construction; operation can be quiet).

### kimpson2026a
- **Title:** Detecting AI Training in Datacentre Power. T. Kimpson, M. Baker, E. Graham. arXiv
  2610.30182 (Oct 2026). Abstract and introduction read.
- **Says:** on simulated facility power, a Viterbi tracker of the iteration cadence "detects at least
  96% of training runs against a declared inference workload, at a 1% false-alarm rate ... given a
  meter that samples at 2 Hz or faster"; of eight hiding strategies only extreme variation of work
  per iteration evades it, hiding training "in up to 73% of five-minute observations, but over a day
  at least 87% of such runs are still caught"; that evasion makes small-scale training need "93-267%
  more compute". Cites a board-level probe separating training from inference "at 97% accuracy".
- **Bears on:** protocol (on-site power metering as an untrusted-operator channel), P4.

### kimpson2026b
- **Title:** Can Power Draw Constrain Covert Compute? Limits of Analogue Verification for AI
  Governance. T. Kimpson, M. Baker, E. Graham. arXiv 2610.07476 (v2, Nov 2026). Abstract read.
- **Says:** "We derive a closed form for β, the largest hidden computation a power trace cannot
  exclude, as a fraction of the declared machine capacity. Measurements on NVIDIA A100 GPUs give
  β = 1.16 in the worst case, while an adversarial matched-energy schedule hides at least 0.41.
  Analogue power measurements alone therefore constrain compute weakly." With re-execution of
  declared work β falls "to 0.059 in the maximally restricted case."
- **Bears on:** P4, protocol (power tells you what kind of work, not how much).

### wasil2024
- **Title:** Verification methods for international AI agreements. A. R. Wasil, T. Reed,
  J. W. Miller, P. Barnett. arXiv 2408.16074 (v2, Nov 2024). Full text read.
- **Says:** remote sensing to "Detect unauthorized data centers and semiconductor manufacturing via
  visual and thermal signatures"; "Infrared imaging is particularly promising for detecting concealed
  data centers, as GPUs and other computing hardware generate significant heat signatures ... that
  are difficult to mask." Energy monitoring: if facility energy "can be measured with reasonable
  accuracy, it should be possible to convert the energy estimate into a reasonable approximation of
  the number of FLOPs", though such measurements "may only be capable of detecting large-scale
  violations"; its own table calls energy monitoring "unproven in practice".
- **Bears on:** P4 (the optimistic view of heat signatures that jing2026, krawec2026 and
  koopmanschap2026 do not support), protocol.

### scher2025
- **Title:** Mechanisms to Verify International Agreements About AI Development. A. Scher,
  L. Thiergart (MIRI). arXiv 2506.15867 (report dated November 2024). Relevant sections read.
- **Says:** detecting secret data centres "is unlikely to be the load-bearing part of a verification
  regime: it will likely be too easy to hide AI compute among other compute"; for large thresholds
  "e.g., data centers with >50,000 AI chips, detecting data centers may be effective"; satellites are
  "unlikely to differentiate AI vs. non-AI data centers". Appendix ("Track AI Chips, Not Data
  Centers"): "a data center with 5,000 H100 GPUs has a power requirement of ~6 MW ..., similar to
  ~5,500 U.S. homes ... likely too small of a footprint to serve as a useful tool for detecting
  secret data centers"; about 500 data centres worldwide exceed 10 MW; "Chip performance per watt is
  increasing at a rate of ~1.6x per year", so "a constant amount of FLOP requires substantially less
  power".
- **Bears on:** P4 (direct argument against facility-based detection), protocol.

### scher2025b
- **Title:** An International Agreement to Prevent the Premature Creation of Artificial
  Superintelligence. A. Scher, D. Abecassis, P. Barnett, B. Abeyta (MIRI Technical Governance
  Team). arXiv 2511.10783 (v2, 17 Nov 2025). Relevant sections read.
- **Says:** "Limits on the scale of AI training are operationalized by FLOP thresholds and verified
  through the tracking of AI chips and verification of chip use"; Strict Threshold 10^24 FLOP
  (prohibited), Monitored Threshold 10^22 FLOP; "the coalition prohibits large concentrations of
  chips (i.e., greater than 16 H100-equivalents; 16 H100s cost approximately $500,000 USD in 2025)
  outside of monitored facilities."
- **Bears on:** P4 (its cluster threshold sits two to three orders of magnitude below any facility
  signature, which is why it relies on chips), D4, protocol.

### halstead-ai2040
- **Title:** Covert AI Projects (supplement to AI 2040: Plan A). B. Halstead, T. Larsen, AI Futures
  Project. Undated web page.
- **Says:** median covert diversion by a competent PRC project "roughly 1.5M H100e"; "a covert
  datacenter with 1 GW total facility power could support 1.9M H100e of 2028-era smuggled US chips";
  disguised sites limited to "on the order of 10 MW - 100 MW"; per-site detection probabilities
  (intuition-based): a single 10 MW site about 0.20 by year 3 and 0.26 by year 10, a single
  1,000 MW site about 0.40 and 0.50; "It will be impossible, in practice, for the US to confidently
  rule out a sufficiently small Chinese covert project."
- **Bears on:** P4, D3, protocol (miss probabilities by site size; they are guesses, labelled so).

### sastry2024
- **Title:** Computing Power and the Governance of Artificial Intelligence. G. Sastry, L. Heim,
  H. Belfield, M. Anderljung, M. Brundage, J. Hazell, C. O'Keefe, G. K. Hadfield, et al. arXiv
  2402.08797 (Feb 2024). Relevant sections read.
- **Says:** compute "is detectable, excludable, and quantifiable, and is produced via an extremely
  concentrated supply chain"; AI supercomputers "consume up to dozens of megawatts of power"; note 35:
  "This detectability might be undermined should decentralized training, spread across many data
  centers and/or using lower-quality compute, become more viable"; note 36: 10.2 kW per 8-chip DGX,
  so 20,000 H100 is "more than 25 MW".
- **Bears on:** P4, O3 (the standard case for compute as the chokepoint, with the distributed
  training caveat already stated in 2024).

### pilz2023
- **Title:** Compute at Scale: A Broad Investigation into the Data Center Industry. K. Pilz,
  L. Heim. arXiv 2311.02651 (Nov 2023). Abstract read.
- **Says:** "There are likely about 500 large (above 10 MW) data centers globally, with the US,
  Europe, and China constituting the most important markets"; industry "approximately $250B". The
  counts by size used by koopmanschap2026 (335-1,325 above 10 MW, 10,000-30,000 above 0.1 MW) are in
  the full text, which I did not open.
- **Bears on:** P4 (the population a covert facility hides among).

---

## Numbers for the ledger

Inputs (each with its kind as the repo defines it):

| id | value | unit | kind | source | where |
|---|---|---|---|---|---|
| boltzmann-k | 1.380649e-23 | J/K | spec | codata2022-k | NIST CODATA 2022, exact |
| landauer-bits-per-erasure | ln 2 = 0.6931 | kT per bit | spec | landauer1961 | Sec. 4, p. 187 |
| landauer-exp-colloid-A | 0.72 | kT per bit | measured | berut2015 | Sec. 3, Fig. 8, two-parameter fit |
| landauer-exp-colloid-B | 8.15 | kT s | measured | berut2015 | Sec. 3, Fig. 8, fit ln2 + B/τ |
| landauer-exp-colloid-tau-max | 40 | s | measured | berut2015 | Fig. 8 |
| landauer-exp-nanomagnet | 1.45 ± 0.35 (and 1.0 ± 0.22) | kT per bit | measured | hong2014 | results; 300 K |
| cmos-ceiling-fp4 | 4.7e15 | FP4 FLOP/J | assumption | ho2023 | abstract; log-sd 0.7 OOM |
| cmos-ceiling-fp16 | 2.9e14 | FP16 FLOP/J | assumption | ho2023 | Implications |
| cmos-ceiling-headroom-h100 | 207 | ratio | assumption | ho2023 | Implications, 50% chance |
| cmos-transistor-bound-range | 3.3e14 to 1.1e18 | FLOP/J | assumption | ho2023 | Table of ranges |
| cmos-switches-per-flop-min | 30 | switches per FLOP | assumption | ho2023 | Sec. on QS, NT |
| reversible-chip-saving | 0.30 | fraction of energy | vendor | hulick2025 | Aug 2025 test, unverified |
| reversible-roadmap-gain | 4000 | ratio | vendor | genkina2025 | "10 or 15 years out" |
| koomey-doubling-1946-2009 | 1.57 | years | measured | koomey2011 | regression, computations/kWh |
| koomey-doubling-post-2000 | 2.7 | years | measured | koomey2015 | peak-output efficiency |
| ml-hw-eff-doubling | 2 | years | measured | epoch-hw-efficiency-2024 | text; FP16 tensor |
| ml-hw-eff-doubling-fp32 | 3.0 | years | measured | hobbhahn2023 | key findings |
| ai-supercomputer-eff-growth | 1.34 (CI 1.25-1.43) | x per year | measured | pilz2025 | Sec. 3.2.1, Fig. 11 |
| gpu-eff-growth | 1.40 | x per year | measured | you2025 | text |
| v100-sxm2-tensor | 125e12 | FLOP/s | vendor | nvidia-v100 | spec table |
| v100-sxm2-power | 300 | W | vendor | nvidia-v100 | spec table |
| v100-hbm-bw | 900e9 | B/s | vendor | nvidia-v100 | spec table |
| a100-sxm-bf16-dense | 312e12 | FLOP/s | vendor | nvidia-a100 | spec table |
| a100-sxm-tdp | 400 | W | vendor | nvidia-a100 | spec table |
| a100-sxm-hbm-bw | 2039e9 | B/s | vendor | nvidia-a100 | spec table |
| h100-sxm-bf16-dense | 989.5e12 | FLOP/s | vendor | nvidia-h100 | 1,979 sparse / 2 |
| h100-sxm-fp8-dense | 1979e12 | FLOP/s | vendor | nvidia-h100 | 3,958 sparse / 2 |
| h100-sxm-tdp | 700 | W | vendor | nvidia-h100 | spec table |
| h100-sxm-hbm-bw | 3.35e12 | B/s | vendor | nvidia-h100 | spec table |
| h100-nvlink-bw | 900e9 | B/s | vendor | nvidia-h100 | spec table |
| gb200-gpu-bf16-dense | 2.5e15 | FLOP/s | vendor | nvidia-gb200 | 360 PF sparse / 2 / 72 |
| gb200-gpu-hbm-bw | 8e12 | B/s | vendor | nvidia-gb200 | 576 TB/s / 72 |
| gb200-gpu-nvlink-bw | 1.8e12 | B/s | vendor | nvidia-gb200 | 130 TB/s / 72 |
| dgx-b200-system-power | 14.3e3 | W per 8 GPUs | vendor | nvidia-dgx-b200 | "~14.3 kW max" |
| dgx-b200-fp8-sparse | 72e15 | FLOP/s per 8 GPUs | vendor | nvidia-dgx-b200 | spec |
| scale-out-link | 400e9 | bit/s per port | vendor | nvidia-dgx-b200 | networking |
| b200-eff-epoch | 2.25e12 | FLOP/s per W | measured | epoch-hw-efficiency-2024 | table (basis not stated) |
| mi300x-fp16-dense | 1307.4e12 | FLOP/s | vendor | amd-mi300x | spec |
| mi300x-tbp | 750 | W | vendor | amd-mi300x | spec |
| mi300x-hbm-bw | 5.3e12 | B/s | vendor | amd-mi300x | spec |
| ironwood-fp8 | 4614e12 | FLOP/s | vendor | google-ironwood-2025 | text |
| ironwood-hbm-bw | 7.37e12 | B/s | vendor | google-ironwood-2025 | text |
| ironwood-pod-chips | 9216 | chips | vendor | google-ironwood-2025 | text |
| flops-growth-20y | 3.0 | x per 2 years | measured | gholami2024 | abstract |
| dram-bw-growth-20y | 1.6 | x per 2 years | measured | gholami2024 | abstract |
| interconnect-bw-growth-20y | 1.4 | x per 2 years | measured | gholami2024 | abstract |
| mem-bw-doubling | 4.1 | years | measured | hobbhahn2023 | summary |
| diloco-comm-reduction | 500 | ratio | measured | douillard2023 | abstract, 8 workers, C4 |
| streaming-diloco-bw-reduction | 100 | ratio | measured | douillard2025 | "two orders of magnitude" |
| data-movement-limit | 1e28 | FLOP | assumption | erdil2024 | abstract |
| data-movement-hard-limit | 1e31 | FLOP | assumption | erdil2024 | abstract |
| decentralized-growth | 20 | x per year | measured | sevilla2025-decentralized | text |
| decentralized-largest | 6e22 to 6e23 | FLOP | measured | sevilla2025-decentralized | text |
| decentralized-gap | 1000 | ratio to frontier | measured | sevilla2025-decentralized | text |
| distributed-1e24-nodes | 2 x 16 H100 | nodes | design | rahman2026 | Table 1 |
| distributed-1e24-cost | 1.6e6 | USD | assumption | rahman2026 | Table 1 |
| distributed-1e25-nodes | 34 x 16 GH200 | nodes | design | rahman2026 | Table 1 |
| distributed-1e26-quality | 2.1e25 | FLOP (quality-adjusted) | assumption | rahman2026 | Table 1, 4,706 nodes |
| distributed-100mbps-cost-ratio | 3 | ratio | assumption | rahman2026 | Sec. 4 |
| max-run-length-now | 4.5 | months | assumption | rahman2026 | Eq. 4 |
| brain-flops-central | 1e15 | FLOP/s | assumption | carlsmith2020 | summary, "more likely than not" |
| brain-flops-range | 1e13 to 1e17 | FLOP/s | assumption | carlsmith2020 | mechanistic method |
| brain-flops-p90-cap | 1e21 | FLOP/s | assumption | carlsmith2020 | summary, under 10% above |
| brain-comm-method | 1e16 to 3e17 | FLOP/s | assumption | carlsmith2020 | Sec. 1.7.4 |
| brain-power | 20 | W | measured | carlsmith2020 | Sec. 4.1.2 ("10-20W", 20 W high end) |
| brain-landauer-cap | 7e21 | bit erasures/s | assumption | carlsmith2020 | Sec. 4.1.2 |
| brain-cortex-compute-power | 0.1 | W | measured | levy2021 | abstract |
| brain-cortex-comm-power | 3.5 | W | measured | levy2021 | abstract |
| wbe-level4-spiking | 1e18 | FLOP/s | assumption | sandberg2008 | Table 9, p. 80 |
| wbe-level5-electrophys | 1e22 | FLOP/s | assumption | sandberg2008 | Table 9, p. 80 |
| wbe-level6-metabolome | 1e25 | FLOP/s | assumption | sandberg2008 | Table 9, p. 80 |
| dc-world-2024 | 415 | TWh/yr | measured | iea2025 | exec. summary (1.5%) |
| dc-world-2030 | 945 | TWh/yr | assumption | iea2025 | exec. summary |
| dc-us-2023 | 176 | TWh/yr | measured | shehabi2024 | exec. summary (4.4%) |
| dc-us-2028-range | 325 to 580 | TWh/yr | assumption | shehabi2024 | exec. summary |
| dc-us-water-direct-2023 | 66e9 | litres/yr | measured | shehabi2024 | p. 55 |
| dc-us-2024 | 192 | TWh/yr | measured | smith2026 | Sec. 1 (4.7%) |
| dc-us-2030-ref | 649 | TWh/yr | assumption | smith2026 | Table 2 (11.8%) |
| dc-us-2030-interconnect | 148 | GW | assumption | smith2026 | Sec. 1 |
| supercomputer-power-growth | 2.0 (CI 1.6-2.2) | x per year | measured | pilz2025 | Fig. 10 |
| colossus-2025-power | 300 | MW | measured | pilz2025 | abstract |
| colossus-2025-chips | 200000 | chips | measured | pilz2025 | abstract |
| leading-2030-power-trend | 9 | GW | assumption | pilz2025 | abstract |
| training-power-growth | 2.1 (CI 1.9-2.2) | x per year | measured | emberson2024 | headline |
| grok3-training-power | 110 | MW | measured | emberson2024 | table |
| largest-run-2030-power | 4 to 16 | GW | assumption | you2025 | text |
| largest-run-2030-flop | 2e29 | FLOP | assumption | sevilla2024 | power section |
| epoch-dc-sites | 96 | sites | measured | epoch-datacenters-2026 | data page |
| epoch-dc-it-power | 15.1 | GW | measured | epoch-datacenters-2026 | data page |
| epoch-dc-coverage | 0.43 (CI 0.29-0.77) | fraction | measured | epoch-datacenters-2026 | data page |
| sat-it-power-accuracy | 1.4 | factor, 80% of the time | measured | epoch-datacenters-2026 | data page |
| sat-cooling-model-error | 2 | factor (worst case) | measured | epoch-datacenters-2026 | methodology |
| colossus1-100k-it-power | 139 | MW | measured | epoch-datacenters-2026 | timelines CSV, 2024-09-02 |
| colossus1-100k-facility-power | 181 | MW | measured | epoch-datacenters-2026 | timelines CSV, 2024-09-02 |
| colossus1-build-time | 131 | days | measured | epoch-datacenters-2026 | timelines CSV, 2024-04-24 to 2024-09-02 |
| colossus2-it-power | 946 | MW | measured | epoch-datacenters-2026 | data_centers.csv |
| abilene-it-power | 824 | MW | measured | epoch-datacenters-2026 | data_centers.csv |
| new-carlisle-it-power | 1037 | MW | measured | epoch-datacenters-2026 | data_centers.csv |
| hyperion-2028-facility-power | 2203 | MW | assumption | epoch-datacenters-2026 | timelines CSV, Epoch forecast |
| hyperion-max | 5 | GW | vendor | meta-infra-2025 | text |
| prometheus-power | 1 | GW | vendor | meta-infra-2025 | text |
| stargate-planned | 7 | GW | vendor | openai-stargate-2025 | text |
| water-new-carlisle | 21.0 | million gallons/day | measured | epoch-datacenters-2026 | timelines CSV, 2026-10-19 |
| water-fairwater-wi | 0.0077 | million gallons/day | measured | epoch-datacenters-2026 | timelines CSV, 2026-04-16 |
| utility-large-load-study | 5 | MW | spec | mlgw2025 | text |
| ercot-large-load-queue | 410 | GW | measured | ercot2026 | slide 3, 2026-03-26 |
| sat-detect-reliable-above | 10 | MW | measured | koopmanschap2026 | Sec. 5.3.1, App. B (Clymer classifier, small sample) |
| sat-miss-examples | 0.5, 0.5, 1.2, 3.2 | MW | measured | koopmanschap2026 | App. B |
| container-cluster | 100 | H100e | assumption | koopmanschap2026 | Sec. 5.3.1 |
| chips-unaccounted | 1e6 | chips (order of) | assumption | koopmanschap2026 | Sec. 5.3.2 |
| dc-count-above-10mw | 500 | sites | assumption | pilz2023 | abstract |
| thermal-night-facility-bound | 0.6 to 1.2 | °C | measured | jing2026 | abstract |
| thermal-cluster-power | 126 | MW (lower bound) | measured | jing2026 | Sec. 2 |
| power-trace-beta-worst | 1.16 | fraction of declared capacity | measured | kimpson2026b | abstract (A100) |
| power-trace-beta-matched | 0.41 | fraction | measured | kimpson2026b | abstract |
| power-trace-beta-restricted | 0.059 | fraction | measured | kimpson2026b | abstract |
| power-meter-detect-training | 0.96 | detection rate at 1% FA | measured | kimpson2026a | abstract (simulated) |
| miri-cluster-threshold | 16 | H100e | design | scher2025b | Sec. 2 |
| miri-strict-threshold | 1e24 | FLOP | design | scher2025b | Sec. 2 |
| covert-site-detect-10mw-3y | 0.20 | probability | assumption | halstead-ai2040 | table, intuition-based |
| covert-site-detect-1gw-3y | 0.40 | probability | assumption | halstead-ai2040 | table, intuition-based |

Derived checks (for `model/subcritical.py` to compute, not to enter as inputs):

- kT ln 2 = 2.871e-21 J at 300 K; 2.967e-21 J at 310 K.
- J/FLOP at dense peak and TDP: V100 SXM2 2.4e-12; A100 SXM 1.28e-12; H100 SXM 7.07e-13 (1.41e12
  FLOP/J); MI300X 5.74e-13. Ratio of H100 J/FLOP to kT ln 2 at 300 K: 2.5e8 (per FLOP against per
  bit, so an upper bound on headroom, not a like-for-like gap).
- CMOS ceiling at FP16 (2.9e14 FLOP/J) is still about 1.2e6 kT ln 2 per FLOP.
- Years to reach a 207x gain at 1.34x a year: 18.2; at 1.41x: 15.5.
- Bytes per FLOP at dense BF16: V100 7.2e-3; A100 6.5e-3; H100 3.4e-3; MI300X 4.1e-3; B200 about
  3.6e-3. From V100 to B200 FLOP/s rose 18x and HBM bandwidth 8.9x.
- Scale-up to scale-out bandwidth per Blackwell GPU: 1.8 TB/s against 50 GB/s, about 36x.
- Brain at 1e15 FLOP/s on 20 W: 5e13 FLOP/J, about 35 times an H100; Landauer cap 20 W / kT ln 2
  (310 K) = 6.7e21 bits/s.
- Colossus 1 at 100k H100: 1.39 kW IT and 1.81 kW facility per H100.

## Prior art for the memo's candidates

### P4, the footprint floor

**Searches tried (2026-11-27):** "minimum facility size to train frontier AI model detection
threshold covert data center power signature verification" (extended); "\"dark compute\" OR
\"covert compute\" minimum cluster size frontier training detection satellite power AI governance
2026" (extended); "\"footprint\" smallest data center capable of training frontier model
\"detection\" floor energy efficiency improvements shrink detectability AI verification"; "Epoch AI
frontier data centers satellite imagery methodology cooling equipment estimate power"; "satellite
land surface temperature data center heat island Landsat study"; "arXiv \"compute structuring\"
detection AI governance splitting training runs across clusters"; "Epoch AI decentralized training
over the internet how far can it scale"; plus following references inside the papers found.

**Closest prior work:**
1. koopmanschap2026: defines the "enforcement breaking point" (the FLOP threshold or equivalent at
   which a policy stops working) and traces, for the "detect hidden capacity" sub-problem, how
   satellites, power monitoring and information gathering degrade from 100,000 to 100
   H100-equivalents, with about 10 MW as the reliable-detection line. This is the memo's
   floor-against-detection-limit comparison, stated qualitatively per facility size.
2. scher2025 and scher2025b: argue that facility detection fails at small sizes (5,000 H100 at about
   6 MW is "too small of a footprint"), that efficiency gains shrink the power of fixed FLOP, and set
   a 16 H100e cluster threshold enforced through chips.
3. rahman2026: computes, for given FLOP targets, the minimum-cost distributed configuration made of
   nodes below a registration threshold; in effect a cost-and-node-count floor for evading facility
   detection.
4. halstead-ai2040: per-site detection probabilities by facility size and number of sites for a
   covert project.
5. sastry2024, wasil2024, sevilla2025-decentralized: detectability of compute from power and
   footprint, with the distributed-training caveat.
6. Found but not opened (blocked by a bot wall): Seferis and Fist, "Detecting Compute Structuring in
   AI Governance Is Likely Feasible" (AAAI 2026). Not cited.

**Judgement (a claim about our search, not about the world):** "footprint floor" as a named,
computed quantity (minimum facility power, heat and chips for a given effective compute, run length
and hardware efficiency, compared with each channel's detection limit) was not found under that
name. Its parts all exist: the size-versus-detectability analysis (koopmanschap2026), the
power-per-FLOP reasoning (scher2025, wasil2024) and the evasion floor under distribution
(rahman2026). So P4 is at most **extends prior work**, and only if it adds what these lack: a
formula in measured inputs (FLOP/J, utilisation, run length, PUE), the time axis (the floor falls
as the run lengthens, and a pause lengthens the rational covert run; rahman2026 Eq. 4), and the
aggregate rather than per-site form.

**What the evidence says against P4 as written:** the memo's "Detection works while the floor sits
above what satellites, grids and supply-chain accounting can see" treats the three channels as
seeing the same floor. They do not. Satellites and grids see sites, and a site can be a 16-GPU node
of a few tens of kW (rahman2026), far below the about 10 MW line; thermal infrared does not see
even a 126 MW cluster's waste heat (jing2026); water is optional (closed-loop sites). Only supply-
chain and chip accounting see the aggregate. The floor therefore has to be defined twice: a per-site
floor (which distribution drives toward one node) and an aggregate floor in chips and energy (which
hardware efficiency lowers by at most about 200x before CMOS binds, ho2023, and algorithmic
progress lowers further).

### P2, headroom to physics

Prior work: ho2023 computes the CMOS ceiling and the headroom over the H100; koomey2011 quotes
Feynman's 1e11 headroom estimate; carlsmith2020 uses Landauer to bound brain computation. Judgement:
the headroom comparison is **prior work**; what is new for Subcritical is only its use as an upper
bound on how far a fixed computation's footprint can shrink, which ho2023 does not draw.

### P3, memory and interconnect

Prior work: gholami2024 (memory wall), hobbhahn2023, erdil2024 (data movement limits), the DiLoCo
papers, sevilla2025-decentralized and krys2025 (governance consequences). Judgement: **prior work**.

### P1 and F1, the brain as a reference

Prior work: carlsmith2020, sandberg2008, levy2021. Judgement: **prior work**; the memo already
treats it as a reference, not a target, which the sources support (Carlsmith's range spans four
orders of magnitude and depends on software "which may be very hard to create").

### Protocol: "power and heat signatures" as a verification channel

Prior work: wasil2024 (proposes it), kimpson2026a (on-site power detects training), kimpson2026b
(on-site power bounds compute weakly, β 0.41 to 1.16), jing2026 and krawec2026 (orbital thermal is
weak; imagery sizes known sites). Judgement: the channel is **prior work**, and the evidence says to
split it: on-site metering at declared facilities is useful for workload type; remote heat sensing
for discovery is weak.

## Sources (TOML)

```toml
[source.landauer1961]
type = "peer-reviewed"
title = "Irreversibility and Heat Generation in the Computing Process"
authors = "R. Landauer"
year = 1961
doi = "10.1147/rd.53.0183"
opened = "2026-11-27"

[source.berut2012]
type = "peer-reviewed"
title = "Experimental verification of Landauer's principle linking information and thermodynamics"
authors = "Antoine Bérut, Artak Arakelyan, Artyom Petrosyan, Sergio Ciliberto, Raoul Dillenschneider, Eric Lutz"
year = 2012
doi = "10.1038/nature10872"
opened = "2026-11-27"

[source.berut2015]
type = "peer-reviewed"
title = "Information and thermodynamics: Experimental verification of Landauer's erasure principle"
authors = "Antoine Bérut, Artyom Petrosyan, Sergio Ciliberto"
year = 2015
doi = "10.1088/1742-5468/2015/06/P06015"
arxiv = "1503.06537"
opened = "2026-11-27"

[source.hong2014]
type = "preprint"
title = "Experimental verification of Landauer's principle in erasure of nanomagnetic memory bits"
authors = "J. Hong, B. Lambson, S. Dhuey, J. Bokor"
year = 2014
arxiv = "1411.6730"
opened = "2026-11-27"

[source.bennett2003]
type = "peer-reviewed"
title = "Notes on Landauer's principle, Reversible Computation and Maxwell's Demon"
authors = "Charles H. Bennett"
year = 2003
arxiv = "physics/0210005"
opened = "2026-11-27"

[source.ho2023]
type = "preprint"
title = "Limits to the Energy Efficiency of CMOS Microprocessors"
authors = "Anson Ho, Ege Erdil, Tamay Besiroglu"
year = 2023
arxiv = "2312.08595"
opened = "2026-11-27"

[source.genkina2025]
type = "news"
title = "Reversible Computing Escapes the Lab in 2025"
authors = "Dina Genkina (IEEE Spectrum)"
year = 2025
url = "https://spectrum.ieee.org/reversible-computing"
opened = "2026-11-27"

[source.hulick2025]
type = "news"
title = "This experimental computer chip reuses energy"
authors = "Kathryn Hulick (Science News)"
year = 2025
url = "https://www.sciencenews.org/article/computer-chip-reuses-energy"
opened = "2026-11-27"

[source.codata2022-k]
type = "official-docs"
title = "CODATA 2022 value: Boltzmann constant"
authors = "NIST"
undated = true
url = "https://physics.nist.gov/cgi-bin/cuu/Value?k"
opened = "2026-11-27"

[source.koomey2011]
type = "peer-reviewed"
title = "Implications of Historical Trends in the Electrical Efficiency of Computing"
authors = "Jonathan G. Koomey, Stephen Berard, Marla Sanchez, Henry Wong"
year = 2011
doi = "10.1109/MAHC.2010.28"
opened = "2026-11-27"

[source.koomey2015]
type = "essay"
title = "Moore's Law Might Be Slowing Down, But Not Energy Efficiency"
authors = "Jonathan Koomey, Samuel Naffziger"
year = 2015
url = "https://spectrum.ieee.org/moores-law-might-be-slowing-down-but-not-energy-efficiency"
opened = "2026-11-27"

[source.epoch-hw-efficiency-2024]
type = "dataset"
title = "Leading ML hardware becomes 40% more energy-efficient each year"
authors = "Robi Rahman (Epoch AI)"
year = 2024
url = "https://epoch.ai/data-insights/ml-hardware-energy-efficiency"
opened = "2026-11-27"

[source.hobbhahn2023]
type = "report"
title = "Trends in machine learning hardware"
authors = "Marius Hobbhahn, Lennart Heim, Gökçe Aydos (Epoch AI)"
year = 2023
url = "https://epoch.ai/blog/trends-in-machine-learning-hardware"
opened = "2026-11-27"

[source.nvidia-v100]
type = "vendor"
title = "NVIDIA V100 Tensor Core GPU datasheet"
authors = "NVIDIA"
undated = true
url = "https://images.nvidia.com/content/technologies/volta/pdf/volta-v100-datasheet-update-us-1165301-r5.pdf"
opened = "2026-11-27"

[source.nvidia-a100]
type = "vendor"
title = "NVIDIA A100 Tensor Core GPU datasheet"
authors = "NVIDIA"
year = 2021
url = "https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf"
opened = "2026-11-27"

[source.nvidia-h100]
type = "vendor"
title = "NVIDIA H100 Tensor Core GPU: specifications"
authors = "NVIDIA"
undated = true
url = "https://www.nvidia.com/en-us/data-center/h100/"
opened = "2026-11-27"

[source.nvidia-gb200]
type = "vendor"
title = "NVIDIA GB200 NVL72: specifications"
authors = "NVIDIA"
undated = true
url = "https://www.nvidia.com/en-us/data-center/gb200-nvl72/"
opened = "2026-11-27"

[source.nvidia-dgx-b200]
type = "vendor"
title = "NVIDIA DGX B200: specifications"
authors = "NVIDIA"
undated = true
url = "https://www.nvidia.com/en-us/data-center/dgx-b200/"
opened = "2026-11-27"

[source.amd-mi300x]
type = "vendor"
title = "AMD Instinct MI300X Accelerator data sheet"
authors = "AMD"
undated = true
url = "https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf"
opened = "2026-11-27"

[source.google-ironwood-2025]
type = "vendor"
title = "Ironwood: The first Google TPU for the age of inference"
authors = "Amin Vahdat (Google)"
year = 2025
url = "https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/"
opened = "2026-11-27"

[source.gholami2024]
type = "peer-reviewed"
title = "AI and Memory Wall"
authors = "Amir Gholami, Zhewei Yao, Sehoon Kim, Coleman Hooper, Michael W. Mahoney, Kurt Keutzer"
year = 2024
arxiv = "2403.14123"
opened = "2026-11-27"

[source.douillard2023]
type = "preprint"
title = "DiLoCo: Distributed Low-Communication Training of Language Models"
authors = "Arthur Douillard, Qixuan Feng, Andrei A. Rusu, Rachita Chhaparia, Yani Donchev, Adhiguna Kuncoro, Marc'Aurelio Ranzato, Arthur Szlam, Jiajun Shen"
year = 2023
arxiv = "2311.08105"
opened = "2026-11-27"

[source.douillard2025]
type = "preprint"
title = "Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch"
authors = "Arthur Douillard, Yanislav Donchev, Keith Rush, Satyen Kale, Zachary Charles, Zachary Garrett, Gabriel Teston, Dave Lacey, Ross McIlroy, Jiajun Shen, Alexandre Ramé, Arthur Szlam, Marc'Aurelio Ranzato, Paul Barham"
year = 2025
arxiv = "2501.18512"
opened = "2026-11-27"

[source.erdil2024]
type = "preprint"
title = "Data movement limits to frontier model training"
authors = "Ege Erdil, David Schneider-Joseph"
year = 2024
arxiv = "2411.01137"
opened = "2026-11-27"

[source.sevilla2025-decentralized]
type = "essay"
title = "How far can decentralized training over the internet scale?"
authors = "Jaime Sevilla (Epoch AI)"
year = 2025
url = "https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale"
opened = "2026-11-27"

[source.sevilla2025-power]
type = "report"
title = "Could decentralized training solve AI's power problem?"
authors = "Jaime Sevilla, Anton Troynikov (Epoch AI)"
year = 2025
url = "https://epoch.ai/blog/could-decentralized-training-solve-ais-power-problem"
opened = "2026-11-27"

[source.meta-infra-2025]
type = "vendor"
title = "Meta's Infrastructure Evolution and the Advent of AI"
authors = "Yee Jiun Song, Kaushik Veeraraghavan (Meta)"
year = 2025
url = "https://engineering.fb.com/2025/09/29/data-infrastructure/metas-infrastructure-evolution-and-the-advent-of-ai/"
opened = "2026-11-27"

[source.krys2025]
type = "preprint"
title = "Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI Landscape"
authors = "Jakub Kryś, Yashvardhan Sharma, Janet Egan"
year = 2025
arxiv = "2507.07765"
opened = "2026-11-27"

[source.rahman2026]
type = "preprint"
title = "Does Distributed Training Undermine Compute Governance?"
authors = "Robi Rahman"
year = 2026
arxiv = "2605.29359"
opened = "2026-11-27"

[source.carlsmith2020]
type = "report"
title = "How Much Computational Power Does It Take to Match the Human Brain?"
authors = "Joseph Carlsmith (Open Philanthropy)"
year = 2020
url = "https://www.openphilanthropy.org/research/how-much-computational-power-does-it-take-to-match-the-human-brain/"
opened = "2026-11-27"

[source.sandberg2008]
type = "report"
title = "Whole Brain Emulation: A Roadmap (Technical Report 2008-3)"
authors = "Anders Sandberg, Nick Bostrom (Future of Humanity Institute)"
year = 2008
url = "https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf"
opened = "2026-11-27"

[source.levy2021]
type = "peer-reviewed"
title = "Communication consumes 35 times more energy than computation in the human cortex, but both costs are needed to predict synapse number"
authors = "William B. Levy, Victoria G. Calvert"
year = 2021
doi = "10.1073/pnas.2008173118"
opened = "2026-11-27"

[source.iea2025]
type = "report"
title = "Energy and AI"
authors = "International Energy Agency"
year = 2025
url = "https://www.iea.org/reports/energy-and-ai/executive-summary"
opened = "2026-11-27"

[source.shehabi2024]
type = "report"
title = "2024 United States Data Center Energy Usage Report (LBNL-2001637)"
authors = "Arman Shehabi, Sarah Smith, Alex Hubbard, Alex Newkirk, Nuoa Lei, A.B. Saddik, Billie Holecek, Jonathan Koomey, Eric Masanet, Dale Sartor"
year = 2024
url = "https://eta-publications.lbl.gov/sites/default/files/2024-12/us_data_center_energy_usage_report_lbnl-2001637.pdf"
opened = "2026-11-27"

[source.smith2026]
type = "report"
title = "United States Data Center Energy Usage Report: 2025 Update (LBNL-2001758)"
authors = "Sarah J. Smith, Alex Hubbard, Alex Newkirk, Mohan Ganeshalingam, et al."
year = 2026
doi = "10.71468/P1RP4F"
url = "https://escholarship.org/uc/item/33m6w3x0"
opened = "2026-11-27"

[source.pilz2025]
type = "preprint"
title = "Trends in AI Supercomputers"
authors = "Konstantin F. Pilz, James Sanders, Robi Rahman, Lennart Heim"
year = 2025
arxiv = "2504.16026"
opened = "2026-11-27"

[source.emberson2024]
type = "dataset"
title = "The power required to train frontier AI models is doubling annually"
authors = "Luke Emberson, Robi Rahman (Epoch AI)"
year = 2024
url = "https://epoch.ai/data-insights/power-usage-trend"
opened = "2026-11-27"

[source.you2025]
type = "report"
title = "How much power will frontier AI training demand in 2030?"
authors = "Josh You, David Owen (Epoch AI, with EPRI)"
year = 2025
url = "https://epoch.ai/blog/power-demands-of-frontier-ai-training"
opened = "2026-11-27"

[source.sevilla2024]
type = "report"
title = "Can AI scaling continue through 2030?"
authors = "Jaime Sevilla, Tamay Besiroglu, Ben Cottier, Josh You, Edu Roldán, Pablo Villalobos, Ege Erdil (Epoch AI)"
year = 2024
url = "https://epoch.ai/blog/can-ai-scaling-continue-through-2030"
opened = "2026-11-27"

[source.lee2025]
type = "dataset"
title = "Today's largest data center can do more than 20 GPT-4-scale training runs each month"
authors = "Jaeho Lee (Epoch AI)"
year = 2025
url = "https://epoch.ai/data-insights/gpt-4s-trainable"
opened = "2026-11-27"

[source.epoch-datacenters-2026]
type = "dataset"
title = "AI data centers (Frontier Data Centers hub), with methodology and CSV downloads"
authors = "Epoch AI"
year = 2026
url = "https://epoch.ai/data/data-centers"
opened = "2026-11-27"

[source.openai-stargate-2025]
type = "vendor"
title = "OpenAI, Oracle, and SoftBank expand Stargate with five new AI data center sites"
authors = "OpenAI"
year = 2025
url = "https://openai.com/index/five-new-stargate-sites/"
opened = "2026-11-27"

[source.mlgw2025]
type = "official-docs"
title = "MLGW update to the public regarding utility support for xAI"
authors = "Memphis Light, Gas and Water"
year = 2025
url = "https://www.mlgw.com/images/content/files/pdf/new/5-5-25%20xAI%20Update.pdf"
opened = "2026-11-27"

[source.ercot2026]
type = "official-docs"
title = "ERCOT Update, Senate Committee on Business and Commerce (Large Load update)"
authors = "ERCOT (Pablo Vegas)"
year = 2026
url = "https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf"
opened = "2026-11-27"

[source.krawec2026]
type = "report"
title = "Tracking Hyperscale AI Data Center Growth with Satellite Imagery"
authors = "Christina Krawec (Federation of American Scientists)"
year = 2026
url = "https://fas.org/publication/tracking-hyperscale/"
opened = "2026-11-27"

[source.jing2026]
type = "peer-reviewed"
title = "Satellite observations and energy balance constrain the thermal footprint of a hyperscale data-centre cluster"
authors = "Jiawei Jing"
year = 2026
doi = "10.1088/1748-9326/aead02"
opened = "2026-11-27"

[source.marinoni2026]
type = "preprint"
title = "The data heat island effect: quantifying the impact of AI data centers in a warming world"
authors = "Andrea Marinoni, Erik Cambria, Weisi Lin, Mauro Dalla Mura, Jocelyn Chanussot, Edoardo Ragusa, Chi Yan Tso, Yihao Zhu, Benjamin Horton"
year = 2026
arxiv = "2603.20897"
opened = "2026-11-27"

[source.koopmanschap2026]
type = "preprint"
title = "How to Catch a GPU: A Taxonomy of Verification and Enforcement Mechanisms for International AI Agreements"
authors = "Raymond Koopmanschap, Otto Barten"
year = 2026
arxiv = "2607.22619"
opened = "2026-11-27"

[source.teague2026]
type = "preprint"
title = "Could Underwater Data Centers Pose a Risk to AI Treaty Verification?"
authors = "James Teague, Ashmita Rajmohan, Yannick Muehlhaeuser"
year = 2026
arxiv = "2609.18824"
opened = "2026-11-27"

[source.kimpson2026a]
type = "preprint"
title = "Detecting AI Training in Datacentre Power"
authors = "Tom Kimpson, Mauricio Baker, Emlyn Graham"
year = 2026
arxiv = "2610.30182"
opened = "2026-11-27"

[source.kimpson2026b]
type = "preprint"
title = "Can Power Draw Constrain Covert Compute? Limits of Analogue Verification for AI Governance"
authors = "Tom Kimpson, Mauricio Baker, Emlyn Graham"
year = 2026
arxiv = "2610.07476"
opened = "2026-11-27"

[source.wasil2024]
type = "preprint"
title = "Verification methods for international AI agreements"
authors = "Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett"
year = 2024
arxiv = "2408.16074"
opened = "2026-11-27"

[source.scher2025]
type = "preprint"
title = "Mechanisms to Verify International Agreements About AI Development"
authors = "Aaron Scher, Lisa Thiergart"
year = 2025
arxiv = "2506.15867"
opened = "2026-11-27"

[source.scher2025b]
type = "preprint"
title = "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
authors = "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year = 2025
arxiv = "2511.10783"
opened = "2026-11-27"

[source.halstead-ai2040]
type = "essay"
title = "Covert AI Projects (supplement to AI 2040: Plan A)"
authors = "Brendan Halstead, Thomas Larsen (AI Futures Project)"
undated = true
url = "https://ai-2040.com/supplements/covert-ai-projects"
opened = "2026-11-27"

[source.sastry2024]
type = "preprint"
title = "Computing Power and the Governance of Artificial Intelligence"
authors = "Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O'Keefe, Gillian K. Hadfield, et al."
year = 2024
arxiv = "2402.08797"
opened = "2026-11-27"

[source.pilz2023]
type = "preprint"
title = "Compute at Scale: A Broad Investigation into the Data Center Industry"
authors = "Konstantin Pilz, Lennart Heim"
year = 2023
arxiv = "2311.02651"
opened = "2026-11-27"
```
