#!/usr/bin/env python3
"""E8: the footprint floor of a training run, against each channel's detection limit.

What it measures. For a run of C useful operations finished within T, the smallest footprint that
could still produce it (research/011-physical.md, P4): the aggregate chip floor
N_min = C / (r * u * T) in H100e, the energy floor E_min = C * e, and the average power E_min / T.
C runs from MIRI's monitored threshold to the top of E8's range in half decades, and T from one
month to the run length Rahman finds rational under a pause. Each floor is then followed year by
year. For a fixed compute, the energy and power floors fall with the measured trend in AI
supercomputer energy efficiency, capped at the estimated CMOS headroom, and the chip floor in
H100e stays put. For a fixed capability, every floor also falls with algorithmic progress, from
Gundlach et al.'s slow case to MIRI's threefold a year. For each detection channel it reports the
margin (the channel's detection limit over the floor it sees; above one, the run is below what the
channel can see) and the first year the floor falls below the limit.

Channels. Satellite discovery of a site (its limit lies between the classifier's largest miss and
the size above which it found every site), a utility's system impact study, anonymity among
commercial loads, thermal infrared (it did not see a cluster of at least 126 MW, so its margin is a
lower bound), a cluster small enough to fit a container, and chip accounting, whose limit is the
stock it cannot see (the untraced pool, or the compute smuggled into one country). Facility
channels see a site, so a run spread over one-node sites shows them the per-site floor, and a run
on one site shows them the aggregate. Satellite sizing of a known site and power metering of a
declared site cannot see a run hidden inside the site's own uncertainty, so for those two it
reports the site size within which a floor-sized run hides.

Data and method. No external data: every input is a sourced number in the ledger, read by id from
data/numbers.json, and the ids and values used are recorded in the result. A seeded Monte Carlo
varies utilisation, power per H100e, the efficiency trend, the algorithmic rate, the satellite
limit, the untraced pool, the smuggled stock and the denial multiplier. A range with a published
interval is drawn from a log-normal matched to it (two-piece where the interval is not symmetric);
a range without one is drawn uniform or log-uniform between the ledger's low and high, and
details.distributions names each choice.

Claims served: C8 (the aggregate floor with a time axis, a margin per channel, and the untraced pool
as a covert reserve; its falsifier is a facility channel with a margin below one for a distributed
1e25 FLOP run) and C3 (the facility limits on the undeclared path, which E5 uses).

  .venv/bin/python tools/exp/e08_footprint_floor.py      (CPU, seconds; see tools/exp/README.md)
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from statistics import NormalDist

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, Results  # noqa: E402

SEED = 20261127
DRAWS = 20_000
YEAR_S = 365.25 * 86400  # a Julian year, the model's unit
MONTH_S = YEAR_S / 12
MWH_J = 3.6e9
T_SWEEP_MONTHS = (1.0, 2.0, 3.0, 6.0, 12.0)  # sweep points; the ledger's two run lengths are added
C_STEPS_PER_DECADE = 2
# The ledger gives the untraced pool as "on the order of a million chips" with no range. We read an
# order of magnitude as within a factor of the square root of ten either way. Our reading, not a
# sourced range.
ORDER_OF_MAGNITUDE = math.sqrt(10)
Z90 = NormalDist().inv_cdf(0.95)  # half-width of a two-sided 90% interval, in standard deviations
QS = (0.05, 0.5, 0.95)


class Ledger:
    """Ledger numbers by id, recording each one read."""

    def __init__(self) -> None:
        self.d = json.loads((ROOT / "data" / "numbers.json").read_text())
        self.used: dict[str, dict] = {}

    def __call__(self, key: str) -> float:
        q = self.d[key]
        self.used[key] = {"value": q["value"], "unit": q["unit"], "basis": q["basis"]}
        return float(q["value"])

    def year(self, key: str) -> int:
        """The year of a ledger number's date."""
        self(key)
        return int(self.d[key]["date"][:4])


def loguniform(gen: np.random.Generator, lo: float, hi: float, n: int) -> np.ndarray:
    return np.exp(gen.uniform(math.log(lo), math.log(hi), n))


def two_piece_lognormal(gen: np.random.Generator, median: float, lo90: float, hi90: float, n: int) -> np.ndarray:
    """Log-normal on each side of the median, each side's spread set by its end of the 90%
    interval, so the draws reproduce the published median and both ends."""
    z = gen.standard_normal(n)
    s_lo = math.log(median / lo90) / Z90
    s_hi = math.log(hi90 / median) / Z90
    return median * np.exp(np.where(z < 0, z * s_lo, z * s_hi))


def crossing_years(ratio0, g, a, cap: float) -> np.ndarray:
    """Years until a floor that starts at ratio0 times a channel's limit falls to the limit, when it
    falls by g a year from hardware (until the gain reaches cap) and by a a year from algorithms.
    Zero if it is already at or below the limit, infinite if it never gets there."""
    ratio0, g, a = np.broadcast_arrays(np.asarray(ratio0, float), np.asarray(g, float), np.asarray(a, float))
    with np.errstate(divide="ignore", invalid="ignore"):
        lr, lg, la = np.log(ratio0), np.log(g), np.log(a)
        t_cap = np.where(lg > 0, math.log(cap) / lg, np.inf)
        both = lg + la
        t1 = np.where(both > 0, lr / both, np.inf)
        t2 = np.where(la > 0, t_cap + (lr - both * t_cap) / la, np.inf)
        t = np.where(t1 <= t_cap, t1, t2)
    return np.where(ratio0 > 1, t, 0.0)


def sig(x: float, digits: int = 4) -> float | None:
    """Round for the details tables, which keep 4 significant digits."""
    if x is None or not math.isfinite(x):
        return None
    return float(f"{x:.{digits}g}")


def quantiles(x: np.ndarray) -> dict:
    return {f"p{round(p * 100):02d}": sig(float(np.quantile(x, p))) for p in QS}


def main() -> int:
    q = Ledger()
    res = Results("E8", "e08_footprint_floor", seed=SEED)
    gen = np.random.default_rng(SEED)

    # Inputs, every one from the ledger.
    r = q("phys-h100-bf16") * 1e12  # FLOP/s per H100e, dense BF16 peak, as the ledger's floors use
    u_ref, u_lo, u_hi = q("phys-util-ref"), q("phys-intellect1-mfu-low"), q("phys-pope-mfu-prefill")
    w_ref, w_lo = q("phys-facility-power-per-h100"), q("phys-epoch-dc-it-per-h100e")
    g_ref = q("phys-eff-growth-supercomputer")
    g_lo, g_hi = q("phys-eff-growth-supercomputer-low"), q("phys-eff-growth-supercomputer-high")
    cap = q("phys-cmos-headroom")
    a_slow, a_ref, a_fast = q("comp-gundlach-small-annual-max"), q("phys-algo-growth"), q("phys-algo-miri")
    sat_hi, sat_lo = q("phys-sat-reliable"), q("phys-sat-miss-max")
    sat_acc, sat_conf = q("phys-sat-it-accuracy"), q("phys-sat-it-confidence")
    grid_mw = q("phys-utility-study")
    anon_mw = q("phys-commercial-load") / 1e3
    thermal_mw = q("phys-jing-cluster-power")
    container = q("phys-container-cluster")
    node_gpus = q("phys-rahman-gpus-per-node")
    pool_ref = q("phys-chips-unaccounted")
    smug_ref, smug_lo, smug_hi = q("org-smuggled-cum"), q("org-smuggled-cum-low"), q("org-smuggled-cum-high")
    denial = q("org-denial-power-multiplier")
    betas = {
        "worst": q("phys-beta-worst"),
        "matched": q("phys-beta-matched"),
        "re-execution": q("phys-beta-restricted"),
    }
    c_lo, c_hi = q("phys-miri-monitored"), q("phys-e8-c-high")
    c24, c25, c26 = q("phys-miri-strict"), q("phys-rahman-1e25-target"), q("phys-rahman-1e26-local")
    t_now, t_pause = q("phys-rahman-run-now"), q("phys-rahman-run-pause")
    base_year = q.year("phys-colossus1-facility-power")  # when the power per chip was measured
    horizon = math.ceil(q("phys-years-to-cmos-fast"))  # years until the CMOS ceiling, fast trend
    last_year = base_year + horizon
    ledger_floor_now = q("phys-floor-chips-1e26-now")
    dist_eff = {"1e25": (c25, q("phys-rahman-1e25-eff")), "1e26": (c26, q("phys-rahman-1e26-eff"))}
    a100_h100e = q("phys-a100-bf16") * 1e12 / r
    miri_cap = q("phys-miri-cluster-cap")

    # The Monte Carlo draws, in a fixed order.
    u = gen.uniform(u_lo, u_hi, DRAWS)
    w = loguniform(gen, w_lo, w_ref, DRAWS)
    g = two_piece_lognormal(gen, g_ref, g_lo, g_hi, DRAWS)
    a = loguniform(gen, a_slow, a_fast, DRAWS)
    sat = loguniform(gen, sat_lo, sat_hi, DRAWS)
    pool = loguniform(gen, pool_ref / ORDER_OF_MAGNITUDE, pool_ref * ORDER_OF_MAGNITUDE, DRAWS)
    smug = two_piece_lognormal(gen, smug_ref, smug_lo, smug_hi, DRAWS)
    mult = gen.uniform(1.0, denial, DRAWS)
    distributions = {
        "utilisation": "uniform between phys-intellect1-mfu-low and phys-pope-mfu-prefill, the measured range; no sourced distribution",
        "power_per_h100e_w": "log-uniform between phys-epoch-dc-it-per-h100e and phys-facility-power-per-h100, the ledger's spread; no sourced distribution. The low end is IT power without cooling, so it understates facility power",
        "efficiency_growth": "two-piece log-normal matched to phys-eff-growth-supercomputer and its published 90% interval (-low, -high)",
        "algorithmic_rate": "log-uniform between comp-gundlach-small-annual-max and phys-algo-miri, the range P4 names; no sourced distribution. Used only for a fixed capability",
        "satellite_limit_mw": "log-uniform between phys-sat-miss-max (largest site missed) and phys-sat-reliable (every larger site found); no sourced distribution",
        "untraced_pool": "log-uniform within a factor of sqrt(10) of phys-chips-unaccounted: our reading of 'order of magnitude', not a sourced range. Counted one chip per H100e, as the ledger does",
        "smuggled_stock_h100e": "two-piece log-normal matched to org-smuggled-cum and its published 90% interval (-low, -high)",
        "denial_multiplier": "uniform between 1 (smuggled leading-edge chips) and org-denial-power-multiplier (domestic chips at a denied party's measured compute per unit of power); no sourced distribution. Applied only to a denied party",
    }

    def chips(c, t_months, util):
        return c / (r * util * t_months * MONTH_S)

    def joules(watts, util, m=1.0):
        """Facility energy per useful operation."""
        return watts * m / (r * util)

    def power_mw(c, t_months, e):
        return c * e / (t_months * MONTH_S) / 1e6

    def first_year(t: float) -> int | None:
        """First calendar year at or below the limit: the base year if already, None past the horizon."""
        if not math.isfinite(t):
            return None
        y = base_year + max(0, math.ceil(t - 1e-9))
        return y if y <= last_year else None

    def year_quantiles(t: np.ndarray) -> dict:
        out = {}
        for p in QS:
            v = float(np.quantile(t, p, method="inverted_cdf"))
            out[f"p{round(p * 100):02d}"] = first_year(v)
        out["share_by_last_year"] = sig(float(np.mean(t <= horizon)))
        return out

    e_ref = joules(w_ref, u_ref)
    e_bound = joules(w_lo, u_hi)  # the lowest energy per operation the ledger's ranges allow
    e_mc = joules(w, u)
    e_mc_denied = joules(w, u, mult)

    cs = [10 ** (math.log10(c_lo) + i / C_STEPS_PER_DECADE)
          for i in range(round(math.log10(c_hi / c_lo) * C_STEPS_PER_DECADE) + 1)]
    ts = sorted(set(T_SWEEP_MONTHS) | {t_now, t_pause})

    # Channels: name, what it counts, central limit, limit draws. Power limits in MW, chips in H100e.
    channels = [
        ("satellite", "power", sat_hi, sat),
        ("grid-study", "power", grid_mw, np.full(DRAWS, grid_mw)),
        ("commercial-anonymity", "power", anon_mw, np.full(DRAWS, anon_mw)),
        ("thermal-infrared", "power", thermal_mw, np.full(DRAWS, thermal_mw)),
        ("container", "chips", container, np.full(DRAWS, container)),
        ("chip-accounting-pool", "chips", pool_ref, pool),
        ("chip-accounting-smuggled", "chips", smug_ref, smug),
    ]
    facility = [ch for ch in channels if not ch[0].startswith("chip-accounting")]
    channel_notes = {
        "satellite": "discovery of a site from imagery; central limit phys-sat-reliable",
        "grid-study": "a US utility's system impact study (phys-utility-study); blind to power generated behind the meter",
        "commercial-anonymity": "a load below phys-commercial-load sits among millions of commercial customers; above it a load is not anonymous, which is not the same as found",
        "thermal-infrared": "did not see a cluster of at least phys-jing-cluster-power, so the true limit is higher: margins are lower bounds and crossing years are the latest",
        "container": "a cluster at or below phys-container-cluster fits in a 12-metre container with no noticeable external cooling",
        "chip-accounting-pool": "the untraced pool (phys-chips-unaccounted), the stock chip accounting cannot see",
        "chip-accounting-smuggled": "compute smuggled into one country through 2025 (org-smuggled-cum)",
    }

    # 1. Floors and margins in the base year, for every C and T.
    base_rows = []
    for c in cs:
        for t in ts:
            n_c, n_mc = chips(c, t, u_ref), chips(c, t, u)
            p_c, p_mc, p_mc_d = power_mw(c, t, e_ref), power_mw(c, t, e_mc), power_mw(c, t, e_mc_denied)
            row = {
                "c_flop": sig(c),
                "t_months": t,
                "chips_h100e": {"central": sig(n_c), "bound": sig(chips(c, t, u_hi)), **quantiles(n_mc)},
                "energy_mwh": {"central": sig(c * e_ref / MWH_J), "bound": sig(c * e_bound / MWH_J),
                               **quantiles(c * e_mc / MWH_J)},
                "power_mw": {"central": sig(p_c), "bound": sig(power_mw(c, t, e_bound)), **quantiles(p_mc),
                             "denied": quantiles(p_mc_d)},
                "margin_one_site": {},
                "hidden_in_known_site_h100e": {
                    "satellite-sizing": sig(n_c / (sat_acc - 1)),
                    **{f"metering-{k}": sig(n_c / b) for k, b in betas.items()},
                },
            }
            for name, kind, lim_c, lim_mc in channels:
                floor_c, floor_mc = (p_c, p_mc) if kind == "power" else (n_c, n_mc)
                m_mc = lim_mc / floor_mc
                entry = {"central": sig(lim_c / floor_c), **quantiles(m_mc), "seen_share": sig(float(np.mean(m_mc <= 1)))}
                if kind == "power":
                    m_d = lim_mc / p_mc_d
                    entry["central_denied"] = sig(lim_c / (p_c * denial))
                    entry["seen_share_denied"] = sig(float(np.mean(m_d <= 1)))
                row["margin_one_site"][name] = entry
            base_rows.append(row)

    # 2. The distributed run: facility channels see one node per site, whatever C is.
    node_mw_c = node_gpus * w_ref / 1e6
    node_mw_mc = node_gpus * w * mult / 1e6  # a denied party's node at the drawn power: the most visible
    distributed = {}
    for name, kind, lim_c, lim_mc in facility:
        if kind == "power":
            m_mc = lim_mc / node_mw_mc
            central = lim_c / node_mw_c
        else:
            m_mc = lim_mc / node_gpus
            central = lim_c / node_gpus
        distributed[name] = {"central": sig(central), "min": sig(float(m_mc.min())), "p50": sig(float(np.median(m_mc)))}
    dist_min_name = min(distributed, key=lambda k: distributed[k]["min"])
    dist_min = min(
        float((lim_mc / (node_mw_mc if kind == "power" else node_gpus)).min()) for _, kind, _, lim_mc in facility
    )
    dist_tax = {}
    for tag, (c, eff) in dist_eff.items():
        dist_tax[tag] = {
            "local_compute_share": sig(eff),
            "chips_pause_h100e": sig(chips(c, t_pause, u_ref) / eff),
            "nodes_pause": sig(chips(c, t_pause, u_ref) / eff / node_gpus),
            "smuggled_over_chips_pause": sig(smug_ref / (chips(c, t_pause, u_ref) / eff)),
        }

    # 3. Year by year, for the two run lengths the ledger names.
    year_rows = []
    for c in cs:
        for t in (t_now, t_pause):
            for k in range(horizon + 1):
                hw, hw_mc = min(g_ref ** k, cap), np.minimum(g ** k, cap)
                p_k = power_mw(c, t, e_ref / hw)
                year_rows.append({
                    "c_flop": sig(c),
                    "t_months": t,
                    "year": base_year + k,
                    "energy_mwh": sig(c * e_ref / hw / MWH_J),
                    "power_mw": sig(p_k),
                    "power_mw_mc": quantiles(power_mw(c, t, e_mc / hw_mc)),
                    "capability_chips_h100e": {
                        "slow": sig(chips(c, t, u_ref) / a_slow ** k),
                        "measured": sig(chips(c, t, u_ref) / a_ref ** k),
                        "miri": sig(chips(c, t, u_ref) / a_fast ** k),
                    },
                    "capability_power_mw_measured": sig(p_k / a_ref ** k),
                })

    # 4. Crossing years: the first year each channel's floor falls below its limit.
    cross_rows = []
    for name, kind, lim_c, lim_mc in channels:
        is_power = kind == "power"
        for c in cs:
            for t in (1.0, t_now, t_pause):
                if is_power:
                    f_c, f_mc, f_mc_d = power_mw(c, t, e_ref), power_mw(c, t, e_mc), power_mw(c, t, e_mc_denied)
                    g_c, g_mc = g_ref, g
                else:
                    f_c, f_mc = chips(c, t, u_ref), chips(c, t, u)
                    g_c, g_mc = 1.0, np.ones(DRAWS)
                for framing in ("compute", "capability"):
                    a_c, a_mc = (1.0, np.ones(DRAWS)) if framing == "compute" else (a_ref, a)
                    row = {
                        "channel": name,
                        "c_flop": sig(c),
                        "t_months": t,
                        "framing": framing,
                        "central": first_year(float(crossing_years(f_c / lim_c, g_c, a_c, cap))),
                        **year_quantiles(crossing_years(f_mc / lim_mc, g_mc, a_mc, cap)),
                    }
                    if is_power:
                        row["central_denied"] = first_year(float(crossing_years(f_c * denial / lim_c, g_c, a_c, cap)))
                        row["denied"] = year_quantiles(crossing_years(f_mc_d / lim_mc, g_mc, a_mc, cap))
                    if framing == "capability":
                        row["slow"] = first_year(float(crossing_years(f_c / lim_c, g_c, a_slow, cap)))
                        row["miri"] = first_year(float(crossing_years(f_c / lim_c, g_c, a_fast, cap)))
                    cross_rows.append(row)

    # Headline numbers for the ledger.
    def num(id_, value, unit="", fmt="sig2", label="", note=""):
        res.number(id_, value, unit=unit, fmt=fmt, label=label, note=note)

    def need_year(t: float, what: str) -> int:
        y = first_year(t)
        if y is None:
            raise SystemExit(f"{what}: no crossing by {last_year}; pick another headline")
        return y

    num("e8-floor-check", chips(c26, t_now, u_ref) / ledger_floor_now, fmt=".3f",
        label="E8's chip floor for 1e26 FLOP over today's longest sensible run, over the ledger's (1 means E8 reproduces it)")

    n26p = chips(c26, t_pause, u)
    num("e8-floor-1e26-pause-p50", float(np.median(n26p)), unit="H100e",
        label="aggregate chip floor for 1e26 FLOP over a pause's longest sensible run, median over utilisation drawn uniform across the measured range (no sourced distribution)")
    num("e8-floor-1e26-pause-p05", float(np.quantile(n26p, 0.05)), unit="H100e",
        label="the same floor, 5th percentile (high utilisation)")
    num("e8-floor-1e26-pause-p95", float(np.quantile(n26p, 0.95)), unit="H100e",
        label="the same floor, 95th percentile (low utilisation)")
    num("e8-floor-1e26-pause-bound", chips(c26, t_pause, u_hi), unit="H100e",
        label="the same floor at the highest measured utilisation, the bound an adversary could reach (L2's correction)")
    num("e8-floor-1e24-pause-bound", chips(c24, t_pause, u_hi), unit="H100e",
        label="aggregate chip floor for 1e24 FLOP over a pause's longest sensible run, at the highest measured utilisation")

    for tag, t in (("now", t_now), ("pause", t_pause)):
        p26 = power_mw(c26, t, e_mc)
        span = "today's" if tag == "now" else "a pause's"
        num(f"e8-power-1e26-{tag}-p50", float(np.median(p26)), unit="MW", fmt="sig2",
            label=f"average facility power of a 1e26 FLOP run over {span} longest sensible run, median of the Monte Carlo over utilisation and power per H100e")
        num(f"e8-power-1e26-{tag}-p05", float(np.quantile(p26, 0.05)), unit="MW", fmt="sig2",
            label="the same power, 5th percentile")
        num(f"e8-power-1e26-{tag}-p95", float(np.quantile(p26, 0.95)), unit="MW", fmt="sig2",
            label="the same power, 95th percentile")
    num("e8-power-1e26-pause-denied-p95", float(np.quantile(power_mw(c26, t_pause, e_mc_denied), 0.95)),
        unit="MW", fmt="sig2",
        label="average facility power of a 1e26 FLOP run over a pause's run length for a denied party, 95th percentile (denial multiplier drawn uniform from 1 to the ledger's value)")

    num("e8-distributed-1e25-margin-min", dist_min, fmt="sig2",
        label=f"smallest margin over every facility channel and every draw for a distributed 1e25 FLOP run on one-node sites, a denied party's power included (above 1: no facility channel sees a site; the smallest is {dist_min_name})",
        note="the per-site floor is one node whatever C is; thermal infrared's margin is a lower bound")
    num("e8-distributed-sat-margin", distributed["satellite"]["central"], fmt=",.0f",
        label="satellite's reliable line over one node's facility power, central inputs")

    p25 = power_mw(c25, t_now, e_mc)
    p25d = power_mw(c25, t_now, e_mc_denied)
    num("e8-concentrated-1e25-now-seen", float(np.mean(sat <= p25)), fmt="%",
        label="share of draws in which a 1e25 FLOP run on one site over today's longest sensible run draws at least the satellite limit (drawn between the largest miss and the reliable line)")
    num("e8-concentrated-1e25-now-seen-denied", float(np.mean(sat <= p25d)), fmt="%",
        label="the same share for a denied party's site")
    p26p = power_mw(c26, t_pause, e_mc)
    num("e8-concentrated-1e26-pause-seen", float(np.mean(sat <= p26p)), fmt="%",
        label="share of draws in which a 1e26 FLOP run on one site over a pause's run length draws at least the satellite limit")
    num("e8-concentrated-1e26-pause-seen-denied", float(np.mean(sat <= power_mw(c26, t_pause, e_mc_denied))), fmt="%",
        label="the same share for a denied party's site")

    for tag, t in (("now", t_now), ("pause", t_pause)):
        span = "today's" if tag == "now" else "a pause's"
        num(f"e8-sat-max-c-{tag}", sat_hi * 1e6 * t * MONTH_S / e_ref, unit="FLOP", fmt=".1e",
            label=f"largest run one site below the satellite reliable line can finish within {span} longest sensible run, central inputs, base year")
    num("e8-sat-max-c-pause-bound", sat_hi * 1e6 * t_pause * MONTH_S / e_bound, unit="FLOP", fmt=".1e",
        label="the same at a pause's run length with the lowest energy per operation the ledger's ranges allow")
    num("e8-sat-max-c-pause-denied", sat_hi * 1e6 * t_pause * MONTH_S / (e_ref * denial), unit="FLOP", fmt=".1e",
        label="the same at a pause's run length for a denied party at the full denial multiplier, central inputs")

    for tag, stock, what in (("pool", pool, "the untraced pool"), ("smuggled", smug, "compute smuggled into one country")):
        ratio = stock / n26p
        num(f"e8-{tag}-over-floor-1e26-pause-p50", float(np.median(ratio)), fmt="sig2",
            label=f"{what} over the chip floor of a 1e26 FLOP run at a pause's run length, median of the Monte Carlo")
        num(f"e8-{tag}-over-floor-1e26-pause-p05", float(np.quantile(ratio, 0.05)), fmt="sig2",
            label="the same ratio, 5th percentile")
        num(f"e8-{tag}-over-floor-1e26-pause-p95", float(np.quantile(ratio, 0.95)), fmt="sig2",
            label="the same ratio, 95th percentile")
    num("e8-smuggled-over-floor-1e26-now-p05", float(np.quantile(smug / chips(c26, t_now, u), 0.05)), fmt="sig2",
        label="compute smuggled into one country over the chip floor of a 1e26 FLOP run at today's run length, 5th percentile")
    for tag, t in (("now", t_now), ("pause", t_pause)):
        span = "today's" if tag == "now" else "a pause's"
        run = smug * r * u * t * MONTH_S
        num(f"e8-smuggled-run-{tag}-p05", float(np.quantile(run, 0.05)), unit="FLOP", fmt=".1e",
            label=f"training compute the smuggled stock could do within {span} longest sensible run, 5th percentile (smuggled stock and utilisation drawn)")
    num("e8-pool-shrink-1e24-pause", pool_ref / chips(c24, t_pause, u_hi), fmt="sig2",
        label="factor by which the untraced pool exceeds the bound chip floor of a 1e24 FLOP run at a pause's run length: how far it must shrink for chip accounting to resolve that run")
    num("e8-pool-shrink-1e26-pause", pool_ref / chips(c26, t_pause, u_hi), fmt="sig2",
        label="the same factor for a 1e26 FLOP run")

    base_note = f" (counted from {base_year}, the year the power per chip was measured; {base_year} means already below)"
    t_sat26 = float(crossing_years(power_mw(c26, t_now, e_ref) / sat_hi, g_ref, 1.0, cap))
    t_sat26_mc = crossing_years(power_mw(c26, t_now, e_mc) / sat, g, 1.0, cap)
    num("e8-cross-sat-1e26-now", need_year(t_sat26, "sat 1e26 now"), fmt=".0f",
        label=f"first year a 1e26 FLOP run on one site over today's run length draws less than the satellite reliable line, fixed compute, central inputs{base_note}")
    for p in (0.05, 0.95):
        v = float(np.quantile(t_sat26_mc, p, method="inverted_cdf"))
        num(f"e8-cross-sat-1e26-now-p{round(p * 100):02d}", need_year(v, "sat 1e26 now mc"), fmt=".0f",
            label=f"the same first year, {round(p * 100)}th percentile of the Monte Carlo (efficiency trend, utilisation, power per H100e, satellite limit)")
    t_sat26d = float(crossing_years(power_mw(c26, t_now, e_ref) * denial / sat_hi, g_ref, 1.0, cap))
    num("e8-cross-sat-1e26-now-denied", need_year(t_sat26d, "sat 1e26 now denied"), fmt=".0f",
        label="the same first year for a denied party at the full denial multiplier, central inputs")
    t_grid26 = float(crossing_years(power_mw(c26, t_now, e_ref) / grid_mw, g_ref, 1.0, cap))
    num("e8-cross-grid-1e26-now", need_year(t_grid26, "grid 1e26 now"), fmt=".0f",
        label=f"first year a 1e26 FLOP run on one site over today's run length draws less than a utility's system impact study threshold, fixed compute, central inputs{base_note}")
    num("e8-thermal-margin-1e26-now", thermal_mw / power_mw(c26, t_now, e_ref), fmt="sig2",
        label="thermal infrared's margin over a 1e26 FLOP run on one site at today's run length, central inputs, a lower bound (the cluster it did not see drew at least 126 MW)")
    num("e8-denial-delay-years", math.log(denial) / math.log(g_ref), unit="years", fmt=".1f",
        label="years by which the full denial multiplier delays a power channel's crossing for a fixed compute, at the measured efficiency trend")
    t_sat27 = float(crossing_years(power_mw(c_hi, t_pause, e_ref) / sat_hi, g_ref, 1.0, cap))
    num("e8-cross-sat-1e27-pause", need_year(t_sat27, "sat 1e27 pause"), fmt=".0f",
        label=f"first year a 1e27 FLOP run on one site over a pause's run length draws less than the satellite reliable line, fixed compute, central inputs{base_note}")
    t_sat27c = float(crossing_years(power_mw(c_hi, t_pause, e_ref) / sat_hi, g_ref, a_ref, cap))
    num("e8-cross-sat-1e27-pause-capability", need_year(t_sat27c, "sat 1e27 pause capability"), fmt=".0f",
        label="the same first year for the capability 1e27 FLOP buys in the base year, with algorithms at the measured rate")
    t_cont = float(crossing_years(chips(c26, t_pause, u_ref) / container, 1.0, a_ref, cap))
    num("e8-cross-container-1e26-pause-capability", need_year(t_cont, "container 1e26 pause"), fmt=".0f",
        label=f"first year the chip floor of the capability 1e26 FLOP buys in the base year, at a pause's run length, fits one container, algorithms at the measured rate{base_note}")
    num("e8-years-to-cap-slow", math.log(chips(c26, t_pause, u_ref) / miri_cap) / math.log(a_slow), unit="years", fmt=".1f",
        label="years until the chip floor of the capability 1e26 FLOP buys, at a pause's run length, falls to MIRI's unmonitored cluster cap, at Gundlach et al.'s slow algorithmic rate")

    # The details: inputs, distributions, every table, and what the result says per claim.
    res.detail("ledger_inputs", dict(sorted(q.used.items())))
    res.detail("distributions", distributions)
    res.detail("constants", {
        "draws": DRAWS,
        "base_year": base_year,
        "base_year_from": "date of phys-colossus1-facility-power, when the power per chip was measured",
        "last_year": last_year,
        "last_year_from": "base year plus phys-years-to-cmos-fast, rounded up",
        "t_months": ts,
        "t_sweep_note": "one month, 2, 3, 6 and 12 months are sweep points; 4.5 and 24 are the ledger's run lengths",
        "c_flop": [sig(c) for c in cs],
        "order_of_magnitude_reading": sig(ORDER_OF_MAGNITUDE),
        "energy_per_op_central_j": sig(e_ref),
        "energy_per_op_bound_j": sig(e_bound),
        "a100_h100e_per_chip": sig(a100_h100e),
    })
    res.detail("channels", channel_notes)
    res.detail("base_year_floors_and_margins", base_rows)
    res.detail("distributed_per_site_margins", distributed)
    res.detail("distribution_tax", dist_tax)
    res.detail("year_by_year", year_rows)
    res.detail("crossing_years", cross_rows)
    res.detail("conventions", {
        "margin": "detection limit over the floor the channel sees; above 1 the run is below what the channel can see",
        "seen_share": "share of draws with margin at or below 1",
        "crossing": "first calendar year at or below the limit; the base year if already below; null if not by last_year",
        "central": "phys-util-ref, phys-facility-power-per-h100, phys-sat-reliable, phys-eff-growth-supercomputer, phys-algo-growth, no denial",
        "bound": "phys-pope-mfu-prefill and phys-epoch-dc-it-per-h100e: the lowest footprint the ledger's ranges allow",
        "hidden_in_known_site_h100e": "site size within which a floor-sized run (central) hides: satellite sizing within phys-sat-it-accuracy at phys-sat-it-confidence, metering within each beta",
        "pool_growth": "the pool and the smuggled stock are held at their ledger values in every year; E22 supplies growth",
        "untraced_as_a100": f"if every untraced chip were A100-class the pool would be {sig(a100_h100e)} of its H100e value",
    })
    res.detail("sat_sizing_confidence", sig(sat_conf))
    res.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
