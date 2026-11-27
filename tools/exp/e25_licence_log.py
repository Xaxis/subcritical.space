#!/usr/bin/env python3
"""E25: the licence clock and log, run on Bitcoin's real header chain.

C9's licence names a recent Bitcoin block k and ends at height k + L. The chip keeps the height it
counts and a counter of its own powered time, and stops at k + L or once its height falls behind a
floor of rho_min blocks per unit of counter time, less a slack of s blocks (research/05-formal.md,
Proposition 9.1). It accepts a header only above a minimum work (Lemma 9.2), and a licence only once
it is a leaf of a log whose root is anchored in the chain (Proposition 9.4). This experiment builds
that verifier and drives it with the real chain, to measure what the formal check could only
simulate (red team C9.2, C9.3, C9.5).

Data. Every block header from the genesis block to height END - 1, as raw 80-byte headers from a
public block-data service (block-dn), checksummed. The headers authenticate themselves: the script
checks that each links to the one before, meets its own proof of work and follows Bitcoin's
retargeting and median-time rules, and that the first is the genesis block. Two independent sources
cross-check it: block hashes at ten heights from Blockstream's Esplora API, and every difficulty
change with its timestamp from mempool.space.

Method.
1. The verifier. A streaming header verifier with a fixed-size state checks every real header.
2. The rate floor against honest chips. An always-on compliant chip accepts a licence when block k
   arrives and sees each later block when it arrives (taken as its header's timestamp, held
   monotone). It is stopped early if, just before some block j <= k + L arrives,
   rho_min * (T_j - T_k) - (j - 1 - k) > s. For every start height and a grid of floors this gives
   the slack a floor needs to never stop a compliant chip, and the powered-time budget it then
   grants a holder, (L + s) / rho_min. Licences run from block k with no issuance lag, the case
   that is hardest on the floor. The formal check's random settings are rerun on the real
   intervals. Out of sample: settings fixed on the record before each year, tested on that year.
3. The minimum work. Within each licence, the lowest honest work per block over the work at
   issuance: a chip that demands more stops a compliant chip. What a forged fork then costs, in
   honest blocks, days of the network's hash rate and hashes at the latest difficulty.
4. A red-team harness on the real headers (assertions: the run stops if any fails): an
   event-driven chip agrees with step 2's computation, a holder feeding real old headers at the
   floor rate reaches the counter's bound and no more, a withheld feed stops the chip, and tampered,
   easier-difficulty and replayed headers are refused. A toy chain at negligible difficulty, using
   the same verifier code, feeds forged forks under rule G (greatest height seen, stop final) and
   rule W (most-work tip, stop re-evaluated).
5. The log. Certificate-transparency trees (RFC 6962 hashing; RFC 9162 proof checks) with
   inclusion and consistency proofs; equivocation, conflicting licences, a withheld leaf and t-of-n
   replicas, all asserted. The memo's tamper tests of sealed declarations are these checks, since a
   declaration is a leaf: a changed leaf fails its inclusion proof and a rewritten history fails the
   consistency proof. The anchoring commitment is modelled; the time to anchor at depth comes from
   the real block intervals. Licence signatures are not modelled.

Serves C9. Ledger inputs: the licence period and unit conventions, read from data/numbers.json.

  ~/.claude/claude-core/bin/heavy .venv/bin/python tools/exp/e25_licence_log.py
  (CPU, one core, about ten seconds after a first fetch of about 80 MB)
"""

from __future__ import annotations

import hashlib
import json
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results, fetch  # noqa: E402

SEED = 20261125
END = 977_000  # headers 0 .. END - 1: about 850 blocks below the tip when fetched, so a later fetch analyses the same bytes
FILE_BLOCKS = 100_000
HEADERS_URL = "https://bdn.bitcoin.lu.ke/headers/{start}"
ESPLORA_URL = "https://blockstream.info/api/block-height/{height}"
MEMPOOL_URL = "https://mempool.space/api/v1/mining/difficulty-adjustments/all"

# Bitcoin's mainnet consensus parameters, which the verifier enforces (Bitcoin Core's chain parameters).
GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
POW_LIMIT = (1 << 224) - 1  # the easiest target any header may have
POW_LIMIT_BITS = 0x1D00FFFF  # its compact form, the minimum difficulty
SPACING = 600  # target seconds per block
INTERVAL = 2016  # blocks per retarget
TIMESPAN = SPACING * INTERVAL
MTP_SPAN = 11  # a header's time must exceed the median of the previous 11

FLOORS = [round(0.30 + 0.05 * i, 2) for i in range(21)]  # rho_min as a share of the nominal rate, 0.30 to 1.30
SLACKS = [0, 5, 144, 1008]  # blocks: none, the formal check's largest, a nominal day, a nominal week
CONFIRMATIONS = [1, 3, 6, 12]
CHECK_DRAWS = 20_000  # reruns of the formal check's random settings on the real intervals
CHIP_STARTS = 12  # starts per stratum in the event-driven agreement test


# ---------------------------------------------------------------------------- the header verifier


def dsha(b: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()


def target_of(bits: int) -> int:
    """Bitcoin's compact target; a negative or overflowing encoding is invalid."""
    size, word = bits >> 24, bits & 0x007FFFFF
    if bits & 0x00800000 and word:
        raise ValueError("negative target")
    return word >> (8 * (3 - size)) if size <= 3 else word << (8 * (size - 3))


def compact_of(target: int) -> int:
    size = (target.bit_length() + 7) // 8
    c = target << (8 * (3 - size)) if size <= 3 else target >> (8 * (size - 3))
    if c & 0x00800000:
        c >>= 8
        size += 1
    return c | (size << 24)


def work_of(bits: int) -> int:
    """Expected hash evaluations per header at this target: 2^256 / (target + 1)."""
    return (1 << 256) // (target_of(bits) + 1)


class Ctx:
    """The verifier's whole state for one chain: fixed size, nothing kept per header."""

    __slots__ = ("height", "tip", "bits", "first_time", "times", "work")
    FORMAT = "<I32sII11I32s"  # height, tip hash, bits, time of the period's first block, last 11 times, chain work
    LICENCE = "<I32sIdd32sdd?"  # k, block k's hash, L, rho_min, s, minimum-work target Z, counter at acceptance and now, stopped

    def __init__(self, height, tip, bits, first_time, times, work):
        self.height, self.tip, self.bits = height, tip, bits
        self.first_time, self.times, self.work = first_time, list(times), work

    def copy(self) -> Ctx:
        return Ctx(self.height, self.tip, self.bits, self.first_time, self.times, self.work)

    def packed(self) -> bytes:
        t = (self.times + [0] * MTP_SPAN)[:MTP_SPAN]
        return struct.pack(self.FORMAT, self.height, self.tip, self.bits, self.first_time, *t,
                           self.work.to_bytes(32, "little"))


def expected_bits(ctx: Ctx, pow_limit: int) -> int:
    nxt = ctx.height + 1
    if nxt % INTERVAL:
        return ctx.bits
    actual = min(max(ctx.times[-1] - ctx.first_time, TIMESPAN // 4), TIMESPAN * 4)
    return compact_of(min(target_of(ctx.bits) * actual // TIMESPAN, pow_limit))


def verify(ctx: Ctx, header: bytes, max_target: int, consensus: bool = True,
           pow_limit: int = POW_LIMIT) -> tuple[Ctx | None, str]:
    """Check one header against the chain state; return the new state, or None and the reason.
    max_target is the chip's minimum-work rule Z: no header with an easier target is accepted.
    consensus=False drops Bitcoin's retargeting rule and keeps only Z, as in the formal model."""
    if len(header) != 80:
        return None, "length"
    if header[4:36] != ctx.tip:
        return None, "linkage"
    time, bits = struct.unpack_from("<II", header, 68)
    if consensus and bits != expected_bits(ctx, pow_limit):
        return None, "retarget"
    try:
        tgt = target_of(bits)
    except ValueError:
        return None, "encoding"
    if tgt > max_target:
        return None, "minimum work"
    h = dsha(header)
    if int.from_bytes(h, "little") > tgt:
        return None, "proof of work"
    if time <= sorted(ctx.times)[len(ctx.times) // 2]:
        return None, "median time"
    new = Ctx(ctx.height + 1, h, bits, ctx.first_time, (ctx.times + [time])[-MTP_SPAN:],
              ctx.work + (1 << 256) // (tgt + 1))
    if new.height % INTERVAL == 0:
        new.first_time = time
    return new, ""


def genesis_ctx(header: bytes) -> Ctx:
    time, bits = struct.unpack_from("<II", header, 68)
    return Ctx(0, dsha(header), bits, time, [time], work_of(bits))


def ctx_at(raw: bytes, times: np.ndarray, height: int) -> Ctx:
    """The verifier's state after header `height`, rebuilt from the record (chain work omitted)."""
    hdr = raw[height * 80:height * 80 + 80]
    bits = struct.unpack_from("<I", hdr, 72)[0]
    lo = max(0, height - MTP_SPAN + 1)
    first = height - height % INTERVAL
    return Ctx(height, dsha(hdr), bits, int(times[first]), [int(x) for x in times[lo:height + 1]], 0)


# ------------------------------------------------------------------------------- small numerics


def sliding_max(a: np.ndarray, w: int) -> np.ndarray:
    """m[i] = max(a[i:i + w]) for i in 0 .. len(a) - w, in linear time (van Herk, Gil and Werman)."""
    n = a.size
    nb = -(-n // w)
    pad = np.full(nb * w, -np.inf)
    pad[:n] = a
    b = pad.reshape(nb, w)
    pre = np.maximum.accumulate(b, axis=1).ravel()
    suf = np.maximum.accumulate(b[:, ::-1], axis=1)[:, ::-1].ravel()
    return np.maximum(suf[:n - w + 1], pre[w - 1:n])


def day(t: float) -> str:
    return datetime.fromtimestamp(int(t), timezone.utc).strftime("%Y-%m-%d")


def year_start(y: int) -> float:
    return datetime(y, 1, 1, tzinfo=timezone.utc).timestamp()


# ------------------------------------------------------------------------- the log (RFC 6962/9162)


def leaf_hash(b: bytes) -> bytes:
    return hashlib.sha256(b"\x00" + b).digest()


def node_hash(a: bytes, b: bytes) -> bytes:
    return hashlib.sha256(b"\x01" + a + b).digest()


def split(n: int) -> int:
    k = 1
    while k * 2 < n:
        k *= 2
    return k


def mth(leaves: list[bytes]) -> bytes:
    n = len(leaves)
    if n == 0:
        return hashlib.sha256(b"").digest()
    if n == 1:
        return leaf_hash(leaves[0])
    k = split(n)
    return node_hash(mth(leaves[:k]), mth(leaves[k:]))


def inclusion_path(m: int, leaves: list[bytes]) -> list[bytes]:
    n = len(leaves)
    if n == 1:
        return []
    k = split(n)
    if m < k:
        return inclusion_path(m, leaves[:k]) + [mth(leaves[k:])]
    return inclusion_path(m - k, leaves[k:]) + [mth(leaves[:k])]


def consistency_path(m: int, leaves: list[bytes], whole: bool = True) -> list[bytes]:
    n = len(leaves)
    if m == n:
        return [] if whole else [mth(leaves)]
    k = split(n)
    if m <= k:
        return consistency_path(m, leaves[:k], whole) + [mth(leaves[k:])]
    return consistency_path(m - k, leaves[k:], False) + [mth(leaves[:k])]


def verify_inclusion(index: int, size: int, lh: bytes, path: list[bytes], root: bytes) -> bool:
    if index >= size:
        return False
    fn, sn, r = index, size - 1, lh
    for p in path:
        if sn == 0:
            return False
        if fn & 1 or fn == sn:
            r = node_hash(p, r)
            while not fn & 1 and fn != 0:
                fn >>= 1
                sn >>= 1
        else:
            r = node_hash(r, p)
        fn >>= 1
        sn >>= 1
    return sn == 0 and r == root


def verify_consistency(first: int, second: int, r1: bytes, r2: bytes, path: list[bytes]) -> bool:
    if first == second:
        return not path and r1 == r2
    if not 0 < first < second or not path:
        return False
    if first & (first - 1) == 0:
        path = [r1] + path
    fn, sn = first - 1, second - 1
    while fn & 1:
        fn >>= 1
        sn >>= 1
    fr = sr = path[0]
    for c in path[1:]:
        if sn == 0:
            return False
        if fn & 1 or fn == sn:
            fr, sr = node_hash(c, fr), node_hash(c, sr)
            while not fn & 1 and fn != 0:
                fn >>= 1
                sn >>= 1
        else:
            sr = node_hash(sr, c)
        fn >>= 1
        sn >>= 1
    return fr == r1 and sr == r2 and sn == 0


# ------------------------------------------------------------------------------------------- main


def main() -> int:
    res = Results("E25", "e25_licence_log", seed=SEED)
    gen = np.random.default_rng(SEED)
    ledger = json.loads((ROOT / "data" / "numbers.json").read_text())
    used = ["prot-licence-months", "def-days-per-year", "def-seconds-per-day"]
    months, days_year, sec_day = (float(ledger[i]["value"]) for i in used)
    res.detail("ledger_inputs", {i: ledger[i]["value"] for i in used})
    L = round(months * days_year / 12 * sec_day / SPACING)  # blocks in one licence period at the nominal rate

    # ---- 1. the real headers, verified
    parts = []
    for start in range(0, END, FILE_BLOCKS):
        p = fetch(HEADERS_URL.format(start=start), f"e25/headers_{start:06d}.bin", res,
                  what=f"Bitcoin block headers from height {start} (block-dn REST service)")
        parts.append(p.read_bytes())
    raw = b"".join(parts)[:END * 80]
    if len(raw) != END * 80:
        raise SystemExit(f"only {len(raw) // 80} headers fetched, {END} needed")
    res.detail("headers_sha256", {"heights": f"0 to {END - 1}", "sha256": hashlib.sha256(raw).hexdigest()})
    arr = np.frombuffer(raw, dtype=np.uint8).reshape(END, 80)
    t_raw = np.frombuffer(arr[:, 68:72].tobytes(), dtype="<u4").astype(np.int64)
    bits = np.frombuffer(arr[:, 72:76].tobytes(), dtype="<u4").astype(np.int64)

    g = raw[:80]
    assert dsha(g)[::-1].hex() == GENESIS, "the first header is not Bitcoin's genesis block"
    pow_limit = POW_LIMIT
    ctx = genesis_ctx(g)
    hashes_at = {0: ctx.tip}
    checkpoints = {100_000 * i for i in range(1, 10)} | {END - 1}
    for h in range(1, END):
        ctx, why = verify(ctx, raw[h * 80:h * 80 + 80], pow_limit)
        if ctx is None:
            raise SystemExit(f"header {h} fails the verifier ({why}): the data is not Bitcoin's chain")
        if h in checkpoints:
            hashes_at[h] = ctx.tip
    state_bytes = len(ctx.packed()) + struct.calcsize(Ctx.LICENCE)
    chain_work = ctx.work

    # Cross-check against two independent sources.
    for h in sorted(checkpoints):
        p = fetch(ESPLORA_URL.format(height=h), f"e25/esplora_{h}.txt", res,
                  what=f"block hash at height {h} (Blockstream Esplora API)")
        assert p.read_text().strip() == hashes_at[h][::-1].hex(), f"block {h} differs from Esplora's"
    p = fetch(MEMPOOL_URL, "e25/mempool_difficulty_adjustments.json", res,
              what="every difficulty change with its height and time (mempool.space API)")
    d1 = target_of(POW_LIMIT_BITS)
    theirs = {int(x[1]): (int(x[0]), float(x[2])) for x in json.loads(p.read_text()) if 0 < int(x[1]) < END}
    ours = {h for h in range(INTERVAL, END, INTERVAL) if bits[h] != bits[h - 1]}
    assert set(theirs) == ours, "the difficulty changes differ from mempool.space's"
    for h, (t, diff) in theirs.items():
        assert t == t_raw[h], f"time of block {h} differs from mempool.space's"
        assert abs(d1 / target_of(int(bits[h])) / diff - 1) < 1e-9, f"difficulty at {h} differs"
    res.detail("cross_checks", {"esplora_hashes_matched": len(checkpoints),
                                "mempool_difficulty_changes_matched": len(theirs)})

    # ---- 2. the rate floor against compliant chips
    t_arr = np.maximum.accumulate(t_raw).astype(float)  # arrival proxy: header time, held monotone
    nst = END - L  # licence starts k = 0 .. END - L - 1, each with blocks k + 1 .. k + L seen
    ks = np.arange(nst)
    jj = np.arange(END, dtype=float)
    k_mature = int(np.argmax(bits != POW_LIMIT_BITS))  # first block above the minimum difficulty
    k_decade = int(np.searchsorted(t_arr, t_arr[-1] - 10 * days_year * sec_day))
    eras = {"all": 0, "mature": k_mature, "decade": k_decade}
    start_year = t_raw[:nst].astype("datetime64[s]").astype("datetime64[Y]").astype(np.int64) + 1970
    end_time = t_arr[L:L + nst]

    span = t_arr[L:L + nst] - t_arr[:nst]  # seconds from block k to block k + L
    span_raw = (t_raw[L:L + nst] - t_raw[:nst]).astype(float)
    nominal = L * SPACING

    def deficit(f: float) -> np.ndarray:
        """D_k: the slack a floor at f of the nominal rate needs for licence k never to stop early."""
        rho = f / SPACING
        m = sliding_max(rho * t_arr - (jj - 1), L)[1:nst + 1]
        return m - rho * t_arr[:nst] + ks

    frontier, falsestop, defs = [], {}, {}
    for f in FLOORS:
        dk = deficit(f)
        defs[f] = dk
        row = {"floor": f}
        for era, a in eras.items():
            s_need = max(float(dk[a:].max()), 0.0)
            budget = (L + s_need) / (f * L)
            # Proposition, true by construction: any floor that stops no compliant chip grants at least the
            # longest honest span plus one nominal block interval over f. An assertion, not a result.
            assert budget * nominal >= span[a:].max() + SPACING / f - 1e-3
            row[era] = {"slack_blocks": round(s_need, 1), "budget_over_nominal": round(budget, 4),
                        "outage_hours_at_start": round(s_need * SPACING / f / 3600, 2),
                        "worst_start": day(t_raw[a + int(np.argmax(dk[a:]))])}
        frontier.append(row)
        falsestop[f] = {era: {str(s): round(float((dk[a:] > s).mean()), 5) for s in SLACKS}
                        for era, a in eras.items()}
    res.detail("floor_frontier", frontier)
    fr_slack = {row["floor"]: row["mature"]["slack_blocks"] for row in frontier}
    res.detail("false_stop_share", {str(f): v for f, v in falsestop.items()})

    spans = {}
    for era, a in eras.items():
        x = span[a:] / sec_day
        spans[era] = {"max_days": round(float(x.max()), 3), "max_start": day(t_raw[a + int(np.argmax(x))]),
                      "median_days": round(float(np.median(x)), 3),
                      "min_days": round(float(x.min()), 3), "min_start": day(t_raw[a + int(np.argmin(x))]),
                      "p01_days": round(float(np.quantile(x, 0.01)), 3),
                      "p99_days": round(float(np.quantile(x, 0.99)), 3),
                      "max_days_raw_timestamps": round(float(span_raw[a:].max() / sec_day), 3),
                      "starts": int(x.size)}
    res.detail("licence_spans", {"licence_blocks": L, "nominal_days": round(nominal / sec_day, 3), **spans})
    other_lengths = {}
    for mo in (1, 3, 6, 12):
        ll = round(mo * days_year / 12 * sec_day / SPACING)
        sp = t_arr[ll:] - t_arr[:-ll]
        other_lengths[f"{mo}_months"] = {"blocks": ll, **{era: round(float(sp[a:].max() / (ll * SPACING)), 4)
                                                          for era, a in eras.items() if era != "all"}}
    res.detail("longest_span_over_nominal_by_licence_length", other_lengths)

    # The formal check's random settings (licences of 5 to 60 blocks, floor 0.2 to 0.9 of the honest rate,
    # slack 0 to 5 blocks), on the real intervals with the nominal rate as the honest rate.
    hits = 0
    for _ in range(CHECK_DRAWS):
        lc = int(gen.integers(5, 61))
        rho = float(gen.uniform(0.2, 0.9)) / SPACING
        s = float(gen.uniform(0, 5))
        k = int(gen.integers(k_mature, END - 61))
        j = np.arange(k + 1, k + lc + 1)
        hits += bool((rho * (t_arr[j] - t_arr[k]) - (j - 1 - k)).max() > s)
    check_share = hits / CHECK_DRAWS

    # Out of sample: the least budget that stopped no compliant chip on the record before each year, tested on
    # that year (the limit of a high floor, a powered-time budget), and the same for the minimum work.
    ub, inv = np.unique(bits, return_inverse=True)
    work = np.array([float(work_of(int(b))) for b in ub])[inv]
    wmin = -sliding_max(-work, L)[1:nst + 1]
    ratio = wmin / work[:nst]
    oos = []
    for y in range(2011, int(start_year.max()) + 1):
        train = (ks >= k_mature) & (end_time < year_start(y))
        test = start_year == y
        if not train.any() or not test.any():
            continue
        b, z = span[train].max(), ratio[train].min()
        oos.append({"year": y, "budget_days": round(b / sec_day, 3),
                    "stopped_share": round(float((span[test] > b).mean()), 5),
                    "year_max_over_budget": round(float(span[test].max() / b), 4),
                    "min_work_setting": round(float(z), 4),
                    "rejected_share": round(float((ratio[test] < z).mean()), 5),
                    "year_min_over_setting": round(float(ratio[test].min() / z), 4),
                    "starts": int(test.sum())})
    res.detail("out_of_sample_by_year", oos)
    y21 = next(r for r in oos if r["year"] == 2021)
    tested = [r for r in oos if r["year"] >= 2012]

    # ---- 3. the minimum work, and what forged headers cost
    zmin = {era: float(ratio[a:].min()) for era, a in eras.items()}
    z_star = zmin["mature"]
    z_when = day(t_raw[k_mature + int(np.argmin(ratio[k_mature:]))])
    w_latest = float(work_of(int(bits[-1])))
    per_day = sec_day / SPACING

    def fork_cost(d: int, z: float) -> float:
        """Honest blocks of work to forge d headers past the chip's tip when it also enforces retargeting:
        the attacker strikes at the cheapest point in a period and lowers the target fourfold at each
        retarget, down to the minimum work z."""
        best = float("inf")
        for r in range(1, INTERVAL + 1):
            i = np.arange(d)
            p = np.where(i < r, 0, 1 + (i - r) // INTERVAL)
            best = min(best, float(np.maximum(z, 4.0 ** -p.astype(float)).sum()))
        return best

    res.detail("minimum_work", {
        "lowest_work_ratio_by_era": {e: round(v, 4) for e, v in zmin.items()},
        "lowest_at_licence_start": z_when,
        "share_below": {str(z): round(float((ratio[k_mature:] < z).mean()), 5) for z in (0.6, 0.7, 0.8, 0.9)},
        "fork_cost_honest_blocks": {
            "one_licence_minimum_work_only": round(L * z_star, 1),
            "one_licence_with_retargeting": round(fork_cost(L, z_star), 1),
            "one_day_minimum_work_only": round(per_day * z_star, 1),
            "one_day_with_retargeting": round(fork_cost(int(per_day), z_star), 1)},
        "latest_bits": hex(int(bits[-1])), "chain_work_hashes": float(chain_work)})

    # ---- 4. red-team harness on the real headers (assertions)
    def run_chip(k: int, f: float, s: float, feed=None, max_target: int = pow_limit, budget: float = 0.0,
                 strict: bool = True):
        """An event-driven chip under one licence from block k. feed(j) gives the counter time at which
        header j is delivered (default: its arrival). Returns (counter time run, stopped early, reason)."""
        c = ctx_at(raw, t_raw, k)
        named = raw[k * 80:k * 80 + 80]
        assert dsha(named) == c.tip, "the licence must name the hash of block k on the chip's chain"
        rho = f / SPACING
        t0, h = t_arr[k], k
        for j in range(k + 1, k + L + 1):
            tj = t_arr[j] if feed is None else feed(j)
            if budget and tj - t0 >= budget:
                return budget, True, "budget"
            if rho * (tj - t0) - (h - k) > s:  # the floor passed h before header j came
                return (h - k + s) / rho, True, "floor"
            nxt, why = verify(c, raw[j * 80:j * 80 + 80], max_target)
            if nxt is None:
                assert not strict, f"real header {j} refused ({why})"
                return tj - t0, True, why
            c, h = nxt, j
        return tj - t0, False, "expiry"

    agree = 0
    for f, s in ((0.9, 144), (1.0, 1008)):
        dk = defs[f]
        pool_stop = np.flatnonzero(dk[k_mature:] > s) + k_mature
        pool_run = np.flatnonzero(dk[k_mature:] <= s) + k_mature
        assert pool_stop.size and pool_run.size, "each stratum needs starts"
        for k in np.concatenate([gen.choice(pool_stop, CHIP_STARTS), gen.choice(pool_run, CHIP_STARTS)]):
            k = int(k)
            assert abs(dk[k] - s) > 1e-6, "a near-tie between the two computations"
            ran, early, _ = run_chip(k, f, s)
            assert early == (dk[k] > s), f"event-driven chip and vectorised deficit disagree at {k}"
            if not early:
                assert abs(ran - span[k]) < 1e-6
            agree += 1

    # A holder feeding real, public headers just in time for the floor reaches (L + s) / rho and no more.
    k_hold = k_mature + int(np.argmax(span[k_mature:]))
    stretch = {}
    for f in (0.5, 1.0):
        s = fr_slack[f]  # the least slack that stopped no compliant chip on the record
        rho = f / SPACING
        bound = (L + s) / rho
        # Each header delivered a millisecond before the floor would pass the height already shown.
        ran, _, _ = run_chip(k_hold, f, s, feed=lambda j, rho=rho, s=s: t_arr[k_hold] + (j - 1 - k_hold + s) / rho - 1e-3)
        assert bound - 1 / rho - 0.01 <= ran <= bound, (ran, bound)
        stretch[str(f)] = {"slack": round(s, 1), "ran_days": round(ran / sec_day, 3),
                           "bound_days": round(bound / sec_day, 3),
                           "over_median_honest_span": round(ran / (spans["decade"]["median_days"] * sec_day), 4)}
        ran0, early0, _ = run_chip(k_hold, f, s, feed=lambda j: float("inf"))  # nothing delivered
        assert early0 and abs(ran0 - s / rho) < 1e-6
    # The same licence under a pure powered-time budget at the longest honest span: no compliant chip stops.
    b_least = span[k_mature:].max()
    _, early_b, _ = run_chip(k_hold, 1.0, float("inf"), budget=b_least + 1)
    assert not early_b
    # The minimum work on the real licence where honest work fell furthest: a Z just above that fall passes
    # every honest header, one just below refuses one, as the vectorised ratio says.
    k_z = k_mature + int(np.argmin(ratio[k_mature:]))
    t_k = target_of(int(bits[k_z]))
    _, e_lo, _ = run_chip(k_z, 1.0, float("inf"), max_target=int(t_k / (z_star * 0.999)))
    _, e_hi, why_hi = run_chip(k_z, 1.0, float("inf"), max_target=int(t_k / (z_star * 1.001)), strict=False)
    assert not e_lo and e_hi and why_hi == "minimum work"

    # Tampered, easier and replayed headers are refused.
    c = ctx_at(raw, t_raw, k_hold)
    nxt = bytearray(raw[(k_hold + 1) * 80:(k_hold + 2) * 80])
    bad = bytearray(nxt)
    bad[40] ^= 1
    assert verify(c, bytes(bad), pow_limit)[1] == "proof of work"
    easy = bytearray(nxt)
    struct.pack_into("<I", easy, 72, 0x207FFFFF)
    for nonce in range(1 << 16):
        struct.pack_into("<I", easy, 76, nonce)
        if int.from_bytes(dsha(bytes(easy)), "little") <= target_of(0x207FFFFF):
            break  # it meets its own, far easier, target
    else:
        raise RuntimeError("no nonce met the easy target")
    assert verify(c, bytes(easy), pow_limit)[1] == "retarget"
    assert verify(c, bytes(easy), pow_limit, consensus=False)[1] == "minimum work"
    assert verify(c, raw[(k_hold + 5) * 80:(k_hold + 6) * 80], pow_limit)[1] == "linkage"
    # A retarget a forged chain could reach by its timestamps (fourfold easier) is refused by a Z at the
    # record's lowest work ratio, while the real next header passes it.
    t_h = target_of(int(bits[k_hold]))
    z_hold = int(t_h / z_star)
    warp = bytearray(nxt)
    struct.pack_into("<I", warp, 72, compact_of(min(4 * t_h, pow_limit)))
    assert verify(c, bytes(warp), z_hold, consensus=False)[1] == "minimum work"
    assert verify(c, bytes(nxt), z_hold)[0] is not None

    # A toy chain at negligible difficulty: forged forks under rules G and W, with the same verifier.
    toy_bits = 0x207FFFFF  # forged headers sit at the minimum work Z
    honest_bits = 0x201FFFFF  # honest headers carry four times that work
    toy_limit = target_of(toy_bits)
    toy_rng = np.random.default_rng(SEED + 1)

    def mine(prev: bytes, time: int, tag: int, b: int = honest_bits) -> bytes:
        tgt = target_of(b)
        for nonce in range(1 << 20):
            hdr = struct.pack("<I32s32sIII", 1, prev, hashlib.sha256(tag.to_bytes(8, "little")).digest(),
                              time, b, nonce)
            if int.from_bytes(dsha(hdr), "little") <= tgt:
                return hdr
        raise RuntimeError("toy mining failed")

    toy_g = mine(b"\x00" * 32, 1, 0)
    g_early = w_early = g_cheap = toy_runs = 0
    for run in range(120):
        lic_k, lic_l = 3, int(toy_rng.integers(5, 40))
        honest = [toy_g]
        for i in range(lic_k + lic_l + 30):
            honest.append(mine(dsha(honest[-1]), 2 + i, 10_000 * run + i + 1))
        fork_at = int(toy_rng.integers(lic_k, lic_k + lic_l))
        n_forged = int(toy_rng.integers(1, 4 * lic_l + 6))
        forged = []
        prev = dsha(honest[fork_at])
        for i in range(n_forged):
            forged.append(mine(prev, 2 + fork_at + i, 10**9 + 10_000 * run + i, toy_bits))
            prev = dsha(forged[-1])
        # Deliver honest headers in order, interleaving forged ones once the fork point is seen.
        chains = {dsha(toy_g): genesis_ctx(toy_g)}
        seen_h = fed = 0
        g_stop, w_stopped_at = None, None
        expiry = lic_k + lic_l
        while seen_h < len(honest) - 1:
            if fed < n_forged and seen_h >= fork_at and toy_rng.random() < 0.6:
                hdr, fed = forged[fed], fed + 1
            else:
                seen_h += 1
                hdr = honest[seen_h]
            parent = chains[hdr[4:36]]
            new, why = verify(parent, hdr, toy_limit, consensus=False, pow_limit=toy_limit)
            assert new is not None, why
            chains[new.tip] = new
            best = max(chains.values(), key=lambda x: (x.work, -x.height))
            g_height = max(x.height for x in chains.values())
            honest_work = chains[dsha(honest[seen_h])].work
            # Rule G: stop once any valid header reaches the expiry height, for good.
            if g_stop is None and g_height >= expiry:
                g_stop = seen_h
            # Rule W: stopped while the most-work tip is at or past the expiry height.
            w_stop = best.height >= expiry
            if w_stop and seen_h < expiry:  # ties in work go to the header seen first, as in Bitcoin
                assert best.work >= honest_work, "rule W stopped an online chip on a fork with less work"
                w_stopped_at = seen_h if w_stopped_at is None else w_stopped_at
        if g_stop is not None and g_stop < expiry:
            assert n_forged >= expiry - g_stop, "rule G: ending D blocks early needs D forged headers"
            g_early += 1
            g_cheap += w_stopped_at is None  # rule G stopped it, rule W did not
        if w_stopped_at is not None:
            w_early += 1
        toy_runs += 1

    # ---- 5. the log: proofs, equivocation, conflicting licences, a withheld leaf, t-of-n replicas
    lrng = np.random.default_rng(SEED + 2)
    proofs = 0
    for n in (1, 2, 3, 5, 8, 13, 16, 31, 33):
        leaves = [lrng.bytes(24) for _ in range(n)]
        root = mth(leaves)
        for m in range(n):
            path = inclusion_path(m, leaves)
            assert verify_inclusion(m, n, leaf_hash(leaves[m]), path, root)
            assert not verify_inclusion(m, n, leaf_hash(leaves[m] + b"x"), path, root)
            if path:
                assert not verify_inclusion(m, n, leaf_hash(leaves[m]), path[:-1] + [b"\x00" * 32], root)
            proofs += 1
        for m in range(1, n):
            cp = consistency_path(m, leaves)
            assert verify_consistency(m, n, mth(leaves[:m]), root, cp)
            forked = list(leaves)
            forked[0] = b"rewritten"
            assert not verify_consistency(m, n, mth(forked[:m]), root, cp)
            assert not verify_consistency(m, n, mth(leaves[:m]), mth(forked), cp)
            proofs += 1

    def licence(chip: int, k: int) -> bytes:
        return struct.pack("<II32sI", chip, k, dsha(raw[k * 80:k * 80 + 80]), L)  # names block k by its hash

    period_k = k_hold
    chips = list(range(64))
    published = [licence(c, period_k) for c in chips[:40]]
    hidden = licence(50, period_k)  # a licence the operator anchors but never publishes
    anchored = published + [hidden]
    root_a = mth(anchored)
    # The chip accepts the hidden licence: its inclusion proof is valid against the anchored root.
    assert verify_inclusion(len(anchored) - 1, len(anchored), leaf_hash(hidden),
                            inclusion_path(len(anchored) - 1, anchored), root_a)
    # An auditor holding every published leaf sees that they do not make the anchored root: withholding is
    # detected, but not which chip it licensed, so no chip's non-issuance can be proved.
    assert mth(published) != root_a and hidden not in published
    # Equivocation: a second tree of the same size shown to someone else cannot match the anchored root, and
    # a later root that rewrites history fails the consistency proof from the anchored one.
    other = published + [licence(51, period_k)]
    assert mth(other) != root_a
    later = anchored + [licence(c, period_k + 1) for c in chips[:8]]
    assert verify_consistency(len(anchored), len(later), root_a, mth(later),
                              consistency_path(len(anchored), later))
    rewritten = other + later[len(anchored):]
    assert not verify_consistency(len(anchored), len(rewritten), root_a, mth(rewritten),
                                  consistency_path(len(anchored), rewritten))
    # Conflicting licences for one chip and period are both visible to anyone who reads the log.
    dup = published + [licence(7, period_k)]
    assert sum(1 for x in dup if x[:8] == struct.pack("<II", 7, period_k)) == 2
    # t-of-n replicas: an accepted licence is unpublished only if at least t replicas collude.
    for _ in range(2000):
        n = int(lrng.integers(1, 10))
        t = int(lrng.integers(1, n + 1))
        colluders = set(lrng.choice(n, int(lrng.integers(0, n + 1)), replace=False).tolist())
        recipients = set(lrng.choice(n, int(lrng.integers(0, n + 1)), replace=False).tolist())
        accepted = len(recipients) >= t
        unpublished = accepted and recipients <= colluders
        assert not unpublished or len(colluders) >= t

    anchor = {}
    for d in CONFIRMATIONS:
        lat = (t_arr[k_decade + d:] - t_arr[k_decade:-d]) / 3600
        anchor[str(d)] = {"p50_hours": round(float(np.median(lat)), 3),
                          "p99_hours": round(float(np.quantile(lat, 0.99)), 3),
                          "max_hours": round(float(lat.max()), 3)}
    res.detail("anchor_latency_decade", anchor)
    res.detail("harness", {
        "real_header_chip_runs_agreeing": agree, "holder_stretch_at_longest_span": stretch,
        "toy_fork_runs": toy_runs, "rule_g_early_stops": g_early, "rule_w_early_stops": w_early,
        "rule_g_only_early_stops": g_cheap,
        "log_proofs_checked": proofs, "replica_trials": 2000,
        "assertions": "every check above is an assertion; the run stops on any failure"})
    res.detail("verifier", {
        "state_format": [Ctx.FORMAT, Ctx.LICENCE], "state_bytes": state_bytes,
        "sha256_compressions_per_header": (80 + 9 + 63) // 64 + (32 + 9 + 63) // 64,
        "header_bytes_per_nominal_day": int(80 * per_day),
        "fork_window_bytes_per_block": 64,
        "note": "rule W must also keep, for any fork it will weigh, each ancestor's hash and chain work back to "
                "the fork point: 64 bytes a block"})
    res.detail("eras", {e: {"first_start": day(t_raw[a]), "height": a} for e, a in eras.items()})

    # ---- numbers
    mat, dec = spans["mature"], spans["decade"]
    fr = {row["floor"]: row for row in frontier}
    res.number("e25-headers", END, unit="headers", fmt=",.0f",
               label="real Bitcoin block headers the verifier checked (linkage, proof of work, retargeting, median time); all passed")
    res.number("e25-state-bytes", state_bytes, unit="bytes", fmt=",.0f",
               label="fixed state a chip keeps for one chain and one licence in this verifier (an illustration of its size, not a hardware measurement)")
    res.number("e25-licence-blocks", L, unit="blocks", fmt=",.0f",
               label="blocks in one licence period at Bitcoin's nominal ten-minute spacing")
    res.number("e25-span-max", mat["max_days"], unit="days", fmt=",.1f",
               label=f"longest real span of a licence of that many blocks since the minimum-difficulty era, licence issued {mat['max_start']}")
    res.number("e25-span-median", dec["median_days"], unit="days", fmt=",.1f",
               label="median real span of such a licence, starts in the last ten years of the record")
    res.number("e25-span-min", dec["min_days"], unit="days", fmt=",.1f",
               label=f"shortest real span of such a licence in the last ten years, issued {dec['min_start']}")
    res.number("e25-budget-least", mat["max_days"] * sec_day / nominal, fmt=".3f",
               label="least powered-time budget, over the nominal licence time, of any floor and slack that stopped no compliant chip on the record: the longest honest span, approached as the floor rises, where the rule becomes a plain powered-time budget")
    for f in (0.5, 0.9, 1.0):
        res.number(f"e25-budget-f{int(round(f * 100)):02d}", fr[f]["mature"]["budget_over_nominal"], fmt=".3f",
                   label=f"powered-time budget, over the nominal licence time, of a floor at {f:.0%} of the nominal block rate with the least slack that stopped no compliant chip on the record ({fr[f]['mature']['slack_blocks']:,.0f} blocks)")
    res.number("e25-falsestop-check", check_share, fmt=".1%",
               label="share of compliant chips stopped early at the formal check's random settings (licences of 5 to 60 blocks, floor 0.2 to 0.9 of the nominal rate, slack up to 5 blocks) on Bitcoin's real intervals",
               note="the formal check's own share was 112 of 649 on simulated Poisson blocks")
    res.number("e25-falsestop-f90-s5", falsestop[0.9]["mature"]["5"], fmt=".1%",
               label="share of compliant three-month licences stopped early with a floor at 90% of the nominal rate and a slack of 5 blocks, on the record since the minimum-difficulty era")
    res.number("e25-falsestop-f100-s1008", falsestop[1.0]["mature"]["1008"], fmt=".1%",
               label="share stopped early with a floor at the nominal rate and a slack of a nominal week (1,008 blocks), same record")
    res.number("e25-oos-2021", y21["stopped_share"], fmt=".1%",
               label="share of licences issued in 2021 that a powered-time budget set at the longest honest span before 2021 would have stopped early (the 2021 fall in hash rate)")
    res.number("e25-oos-margin", max(r["year_max_over_budget"] for r in tested), fmt=".3f",
               label="largest factor by which a year's longest honest span exceeded the longest before it, 2012 on (the margin a budget set on the past needed)")
    res.number("e25-oos-years", sum(1 for r in tested if r["stopped_share"] > 0), unit="years", fmt=",.0f",
               label=f"years from 2012 to {tested[-1]['year']} ({len(tested)} tested) in which a budget set on the earlier record stopped some compliant chip")
    res.number("e25-minwork-least", z_star, fmt=".3f",
               label=f"lowest honest work per block within a licence, over the work at issuance, since the minimum-difficulty era (licence issued {z_when}): the most minimum work a chip could demand without stopping a compliant chip on the record")
    res.number("e25-oos-minwork-2021", y21["rejected_share"], fmt=".1%",
               label="share of licences issued in 2021 in which a minimum work set on the record before 2021 would have refused an honest header")
    res.number("e25-forge-licence-days", L * z_star * SPACING / sec_day, unit="days", fmt=",.0f",
               label="upper bound on what the minimum-work rule can make a forged fork of one licence period cost, in days of the whole honest network's hash rate at issuance; under rule G one such fork ends every reachable licence at once")
    res.number("e25-forge-day-hours", per_day * z_star * SPACING / 3600, unit="hours", fmt=",.1f",
               label="upper bound on the cost of ending licences one nominal day early under rule G, in hours of the whole honest network's hash rate")
    res.number("e25-block-hashes", w_latest, unit="hashes", fmt=".2e",
               label="expected hash evaluations per block at the last difficulty in the record")
    res.number("e25-net-hashrate", w_latest / SPACING, unit="hashes/s", fmt=".2e",
               label="honest network hash rate implied by the last difficulty at the nominal spacing; rule W stops an online chip early only with more than this, sustained")
    res.number("e25-forge-licence-hashes", L * z_star * w_latest, unit="hashes", fmt=".2e",
               label="upper bound on the hash evaluations of a forged fork of one licence period at the last difficulty, at the record's largest admissible minimum work")
    res.number("e25-anchor6-p99", anchor["6"]["p99_hours"], unit="hours", fmt=".1f",
               label="99th percentile of the time for six blocks in the last ten years: the wait before a logged licence is anchored six deep (six is a design choice here)")
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
