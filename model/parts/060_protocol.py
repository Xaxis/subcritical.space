"""Part II: the protocol, derived (research/06-protocol.md).

The numbers the protocol needs that Part I and the claims file did not compute: an illustrative
response time and line for licensed, declared compute; the detection rate that line asks of the
declared channels; the coalition share it allows on declared compute; how long the smuggled stock
would take to reach the one published breakout budget, at fixed algorithms and under algorithmic
drift; the cost of tabulating breakout times on the fast efficiency path; the evaluation interval
at the frontier's pace; the withdrawal notice the line implies; and the prize-to-penalty ratio above
which C7's penalty condition fails. Inputs are in data/inputs/060-protocol.toml. Every id starts
with prot-. The covert path has no coalition share here: C7 gives it none until a response on it is
bounded.
"""

from __future__ import annotations

import math

SECONDS_PER_YEAR = 365.25 * 86_400


def build(L, here) -> None:
    # -----------------------------------------------------------------------------------------
    # The response time for licensed, declared compute. Detection: the one historical detection
    # time on declared material (IAEA accountancy and the DPRK, about nine months). Response: a
    # licence lapses unless renewed on positive evidence, so a violation the renewal rule checks
    # mechanically stops the chip within one licence period of powered time, with no decision to
    # wait for. A violation that needs a licensor's judgement adds a decision time no record
    # measures, which this illustration leaves out. Both are illustrations, not measurements.

    L.derive(
        "prot-tr-declared",
        lambda q: (q["org-dprk-months"] + q["prot-licence-months"]) / 12,
        "(org-dprk-months + prot-licence-months) / 12",
        unit="years",
        fmt=".1f",
        label="illustrative response time T_r for licensed, declared compute: the DPRK detection time plus one licence period, for a violation the renewal rule checks mechanically (no decision time)",
        defined_in=here(),
    )
    L.derive(
        "prot-line-declared",
        lambda q: q["prot-margin"] * q["prot-tr-declared"],
        "prot-margin * prot-tr-declared",
        unit="years",
        fmt=".1f",
        label="breakout time below which a declared holding is weapons-grade, at the illustrative margin and response time",
        defined_in=here(),
    )

    # The detection rate that response time asks of the declared channels: with detection a
    # Poisson process at rate lambda, T_d(beta) = ln(1 / beta) / lambda, so a T_d of nine months
    # needs lambda = ln(1 / beta) / T_d.
    L.derive(
        "prot-lambda-declared",
        lambda q: math.log(1 / q["def-prevent-beta"]) / (q["org-dprk-months"] / 12),
        "ln(1 / def-prevent-beta) / (org-dprk-months / 12)",
        unit="/yr",
        fmt=".1f",
        label="detection rate the declared channels need to reach the tolerated miss chance within the DPRK detection time",
        defined_in=here(),
    )
    L.derive(
        "prot-lambda-over-history",
        lambda q: q["prot-lambda-declared"] / q["e5-hazard"],
        "prot-lambda-declared / e5-hazard",
        fmt=",.0f",
        label="that rate as a multiple of E5's fitted historical discovery rate of covert programmes (a lower bound on the multiple, as E5's rate is an upper bound for a careful evader)",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C7's coalition share, s* = min(1, h_w / (m * T_r)), at fixed algorithms, with h_w the time
    # the whole projected fleet needs to reach the hardwired-pause budget (claim-whole-fleet-horizon).
    # Each path has its own T_r and so its own s* (Part III, Proposition 7.1). h_w is proportional
    # to the assumed breakout budget B, so s*(B) = min(1, (B / B_hwp) * h_w / (m * T_r)). On the
    # covert path T_r is unbounded (C1 on E24) and s* is 0, so no covert share is computed.
    L.derive(
        "prot-coalition-share-declared",
        lambda q: min(1.0, q["claim-whole-fleet-horizon"] / q["prot-line-declared"]),
        "min(1, claim-whole-fleet-horizon / prot-line-declared)",
        fmt="%",
        label="largest share of the projected fleet a coalition may hold on declared, licensed compute, at fixed algorithms and the hardwired-pause breakout budget (it scales with that assumed budget until it reaches 1)",
        defined_in=here(),
    )
    L.derive(
        "prot-coalition-budget-unity",
        lambda q: q["prot-line-declared"] / q["claim-whole-fleet-horizon"],
        "prot-line-declared / claim-whole-fleet-horizon",
        fmt=".2f",
        label="assumed breakout budget, as a fraction of the hardwired-pause paper's, below which the declared coalition share s* falls below 1 (s* equals the budget over this fraction, capped at 1)",
        defined_in=here(),
    )
    L.derive(
        "prot-pool-share-of-fleet",
        lambda q: q["org-smuggled-cum"] / (q["def-hwp-global-fleet"] * 1e6),
        "org-smuggled-cum / def-hwp-global-fleet",
        fmt=".1%",
        label="median compute smuggled into one country through 2025, as a share of the projected end-2026 fleet",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # The smuggled stock against the one published breakout budget (hardwired-pause paper: budget,
    # research overhead, utilisation, all that paper's assumptions). At fixed algorithms the time is
    # Y = overhead * budget / (stock * rate * utilisation). With algorithmic efficiency growing g a
    # year, effective compute accumulates as A (g^t - 1) / ln g, so t = ln(1 + Y ln g) / ln g.

    def pool_years_fixed(q):
        per_year = (
            q["org-smuggled-cum"] * q["def-hwp-h100e-rate"] * 1e12 * q["def-hwp-utilisation"] * SECONDS_PER_YEAR
        )
        return q["def-hwp-overhead"] * q["def-hwp-breakout-budget"] / per_year

    L.derive(
        "prot-pool-years-fixed",
        pool_years_fixed,
        "def-hwp-overhead * def-hwp-breakout-budget / (org-smuggled-cum * def-hwp-h100e-rate * def-hwp-utilisation * 1 yr)",
        unit="years",
        fmt=",.0f",
        label="years for the median smuggled stock to reach the hardwired-pause breakout budget at fixed algorithms",
        defined_in=here(),
    )

    def drift_years(rate_id):
        def fn(q):
            g = math.log(q[rate_id])
            return math.log(1 + q["prot-pool-years-fixed"] * g) / g

        return fn

    for suffix, rate_id, what in (
        ("small", "comp-gundlach-small-annual-max", "the small-compute bound on algorithmic progress"),
        ("ho", "comp-ho-annual", "Ho et al.'s central rate of algorithmic progress"),
        ("rosetta", "comp-rosetta-algo", "the Rosetta fit's rate of algorithmic progress"),
    ):
        L.derive(
            f"prot-pool-years-{suffix}",
            drift_years(rate_id),
            f"ln(1 + prot-pool-years-fixed * ln({rate_id})) / ln({rate_id})",
            unit="years",
            fmt=",.0f" if suffix == "small" else ",.1f",
            label=f"years for the same stock to reach the same budget with efficiency growing at {what}, applied to the whole budget",
            defined_in=here(),
        )


    # -----------------------------------------------------------------------------------------
    # Tabulating on the fast efficiency path: how much shorter a holding's computed leak time is at
    # the Rosetta rate than at Ho et al.'s central rate, for the computational chapter's example.
    L.derive(
        "prot-fast-path-factor",
        lambda q: q["comp-leak-years-ho"] / q["comp-leak-years-rosetta"],
        "comp-leak-years-ho / comp-leak-years-rosetta",
        fmt=".1f",
        label="factor by which tabulating on the fast (Rosetta) efficiency path shortens a computed leak time against the central path",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # In-run drift (Part III, Corollary 1.6a): a T_b computed at launch speed, algorithms fixed when
    # the run starts, must clear the line raised by G(m T_r) / (m T_r), formal-inrun-line-factor at
    # the central drift rate and formal-inrun-line-factor-high at the high end (both upper bounds,
    # since they assume a run adopts every gain at once). Proposition 7.1 carries it into s*.
    for suffix, factor_id, what in (
        ("", "formal-inrun-line-factor", "the central drift rate"),
        ("-high", "formal-inrun-line-factor-high", "the high end of the ledger's drift interval"),
    ):
        L.derive(
            f"prot-line-declared-inrun{suffix}",
            (lambda f: lambda q: q["prot-line-declared"] * q[f])(factor_id),
            f"prot-line-declared * {factor_id}",
            unit="years",
            fmt=".1f",
            label=f"breakout time at launch speed a declared holding must exceed to meet the illustrative line when runs absorb drift at {what} (an upper bound on the needed rise)",
            defined_in=here(),
        )
        L.derive(
            f"prot-coalition-share-inrun{suffix}",
            (lambda f: lambda q: min(1.0, q["claim-whole-fleet-horizon"] / (q["prot-line-declared"] * q[f])))(factor_id),
            f"min(1, claim-whole-fleet-horizon / (prot-line-declared * {factor_id}))",
            fmt="%",
            label=f"largest coalition share on declared, licensed compute at the hardwired-pause budget when runs absorb drift at {what} (Proposition 7.1 with Corollary 1.6a; a lower bound on the share, as the factor is an upper bound)",
            defined_in=here(),
        )

    L.derive(
        "prot-coalition-inrun-headroom",
        lambda q: q["claim-whole-fleet-horizon"] / q["prot-line-declared-inrun"],
        "claim-whole-fleet-horizon / prot-line-declared-inrun",
        fmt=".2f",
        label="whole-fleet horizon over the declared line at launch speed with central in-run drift: above 1, the cap at s* = 1 binds and the whole fleet sits outside the line by this factor",
        defined_in=here(),
    )

    # The fall phi in T_b between checks of the line (Proposition 1.6, Corollary 1.6a) has two parts:
    # holdings growth, which E22 bounds from supply for the fleet as a whole, and algorithmic drift
    # over the interval, here at the central rate. A party that buys more than its share of new
    # chips has a larger phi than the fleet's.
    for suffix, phi_id, years, what in (
        ("quarter", "e22-phi-member-quarter", lambda q: q["prot-licence-months"] / 12, "a check at each licence renewal"),
        ("year", "e22-phi-member-year", lambda q: 1.0, "a check once a year"),
    ):
        L.derive(
            f"prot-phi-{suffix}",
            (lambda f, y: lambda q: q[f] * q["phys-algo-growth"] ** y(q))(phi_id, years),
            f"{phi_id} * phys-algo-growth ^ (interval in years)",
            fmt=".1f",
            label=f"fall in the fleet's breakout time between checks for {what}: E22's supply bound times the central algorithmic drift over the interval",
            defined_in=here(),
        )
        L.derive(
            f"prot-line-declared-phi-{suffix}",
            (lambda s: lambda q: q["prot-line-declared"] * q[f"prot-phi-{s}"])(suffix),
            f"prot-line-declared * prot-phi-{suffix}",
            unit="years",
            fmt=".1f",
            label=f"breakout time a declared path must show at {what} so the line holds until the next (Proposition 1.6; for a T_b that counts in-run drift)",
            defined_in=here(),
        )
    L.derive(
        "prot-line-declared-inrun-phi-quarter",
        lambda q: q["prot-line-declared-inrun"] * q["prot-phi-quarter"],
        "prot-line-declared-inrun * prot-phi-quarter",
        unit="years",
        fmt=".1f",
        label="launch-speed breakout time a declared path must show at each licence renewal, central in-run drift (Corollary 1.6a with phi0 = prot-phi-quarter)",
        defined_in=here(),
    )
    L.derive(
        "prot-coalition-share-inrun-phi",
        lambda q: min(1.0, q["claim-whole-fleet-horizon"] / q["prot-line-declared-inrun-phi-quarter"]),
        "min(1, claim-whole-fleet-horizon / prot-line-declared-inrun-phi-quarter)",
        fmt="%",
        label="largest coalition share with central in-run drift and growth between licence renewals at the fleet's phi (a coalition growing no faster than the fleet)",
        defined_in=here(),
    )

    # Evaluations at every 4x of effective compute, at the frontier's pace: effective compute grows
    # by physical growth times algorithmic progress a year.
    L.derive(
        "prot-eval-interval-months",
        lambda q: 12 * math.log(q["comp-rsp-cadence"])
        / math.log(q["comp-frontier-compute-growth"] * q["comp-ho-annual"]),
        "12 * ln(comp-rsp-cadence) / ln(comp-frontier-compute-growth * comp-ho-annual)",
        unit="months",
        fmt=",.0f",
        label="months between evaluations at every 4x of effective compute, at frontier compute growth and Ho et al.'s central algorithmic rate (E1 cannot identify the frontier's rate, so this is an illustration)",
        defined_in=here(),
    )

    # Withdrawal: notice N >= m * T_r - T_b(exiting). The longest notice the line can ask of a
    # member whose holding has crossed it (T_b just above T_r, the point where response must
    # already be under way) is (m - 1) * T_r.
    L.derive(
        "prot-notice-months",
        lambda q: (q["prot-margin"] - 1) * q["prot-tr-declared"] * 12,
        "(prot-margin - 1) * prot-tr-declared * 12",
        unit="months",
        fmt=",.0f",
        label="withdrawal notice the line asks of a member whose holding has fallen to the response time, at the illustrative margin",
        defined_in=here(),
    )

    # -----------------------------------------------------------------------------------------
    # C7's penalty condition (Part III, Theorem 7.2(ii)): no breakout profits a party if
    # beta * V <= (1 - beta) * P. It fails once the prize V exceeds (1 - beta) / beta times the
    # penalty P.
    L.derive(
        "prot-prize-over-penalty",
        lambda q: (1 - q["def-prevent-beta"]) / q["def-prevent-beta"],
        "(1 - def-prevent-beta) / def-prevent-beta",
        fmt=",.0f",
        label="prize-to-penalty ratio above which a breakout at the prevention miss chance profits a party, so C7's penalty condition fails",
        defined_in=here(),
    )
