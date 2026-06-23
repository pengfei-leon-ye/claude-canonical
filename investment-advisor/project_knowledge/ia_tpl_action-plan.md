# Action Plan — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's Action Plan — the advisor's *proposed, not-yet-executed* recommendations.** Carries zero real data — only field definitions and illustrative (generic) examples. To use: the advisor emits a filled instance when proposing trades; the investor reviews, executes (in whole or part), records executed fills in the transaction log, and re-snapshots portfolio state. Like the other runtime files, the filled instance lives in the private `investment-advisor-private/` folder; only this blank schema belongs in the public repo.

## Why this file exists — the three-artifact contract

Runtime state is **three artifacts with a single-directional flow** — never collapse them:

| Artifact | Answers | Mutation rule |
|---|---|---|
| **Portfolio State** (`ia_tpl_portfolio-state.md`) | what I **hold** | refreshed wholesale at each review |
| **Transaction Log** (`ia_tpl_transaction-log.md`) | what I **have done** | append-only; executed fills only |
| **Action Plan** (this file) | what the advisor **proposes** | items resolve as they execute/void/expire |

**Flow:** analysis → **Action Plan** (pending, with timing) → investor executes → record fills in **Transaction Log** → re-snapshot **Portfolio State** (reconciled against the log).

**Hard rule (framework Invariant 9).** A recommendation materializes **only** here. It **never** directly mutates Portfolio State. Holdings change *only* via execute → log → re-snapshot. An unexecuted or partially-executed plan must never silently alter the holdings record. This is what keeps *what I propose / what I hold / what I have done* cleanly separated — a recommendation that was never placed, or only 1-of-3 tranches filled, cannot pollute the record of fact.

## Action vocabulary

Same verbs as the transaction log, plus two plan-level composites:
**Buy** = establish 底仓 (value-based) · **Add** = buy-back-low · **Trim** = partial sell-high · **Sell** = full exit (broken thesis) · **Swap** = paired sell→buy (e.g., re-base a sleeve anchor); on execution it becomes **two** log rows · **Rebalance** = sleeve-level move to restore the 45/45/10 band. Moves are partial (~1/3); never all-in / all-out (Invariant 3).

## Timing fields — per framework §6.7

Because the advisor **cannot see future prices and must not pretend to**, each action carries a *condition-based window* and (only if intraday) a *slippage-control band* — never a price forecast:

- **Window / Trigger** — a **condition, not a date**: a secondary-trend + valuation trigger *within the valuation zone* (e.g., "while still in an add-zone and mid-trend not reversed, on a pullback to the recent support band / a failed breakdown / N-day stabilization"). Watched **event-driven per §7** — never a license for daily price-watching.
- **Time-point** — one of **Open** / **Intraday** / **Close**. Open/Close = accept the auction/closing price when execution certainty or end-of-day confirmation matters more than a specific tick. **Intraday is the only one that carries a price band.**
- **Intraday limit band** — *only if* Time-point = Intraday. A **reference band for slippage control**, anchored to recent support/resistance or a small discount/premium to prior close (for ETFs also sanity-check IOPV/premium). **Not a prediction of tomorrow's candle.**
- **Voids when** — what invalidates this window/action (valuation leaves the zone, thesis breaks, mid-trend reverses, the band is not reached within the horizon, etc.). A voided action returns to analysis; it does **not** auto-execute later.

## Plan metadata

- **Plan date (计划日期):** YYYY-MM-DD
- **Based on State snapshot (依据快照):** `portfolio-state_YYYY-MM-DD.md`
- **Overall posture (整体意图):** one line — what this plan is trying to move (e.g., "Phase 1: deploy idle cash into hedge + start core; cash-neutral core re-base").
- **Status legend:** Proposed → Confirmed → Executed (→ logged) / Partially-executed / Voided / Expired.

## Proposed actions — overview

| # | 标的 Instrument (code) | Sleeve | 动作 Action | 规模 Size (¥ / % / shares@exec) | 资金来源 Funding | 窗口/触发 Window/Trigger | 时点 Time-point | 盘中限价带 Intraday band | Voids when | 状态 Status |
|---|---|---|---|---|---|---|---|---|---|---|
| _1 (ex.)_ | 示例-宽基ETF (51xxxx) | Stable | Swap (sell old anchor→buy this) | ~X (shares@exec) | sale of legacy ETF | re-base now; not timing-sensitive | Intraday | tranched limits near prior close | n/a (cash-neutral) | Proposed |
| _2 (ex.)_ | 示例-黄金ETF (518xxx) | Hedge | Buy (tranche 1/3) | 1/3 of hedge target | cash | establish now; remaining tranches on pullbacks / over 1–2 wks | Intraday | near IOPV; small premium cap | sharp gap-up → wait | Proposed |
| _3 (ex.)_ | 示例-科技成长股A | Risk | Add (tranche 1/3) | ~1/3 of target add | cycle cash | in add-zone (low pctile) & mid-trend not reversed; on support retest / N-day stabilize | Intraday or Close | near recent support band | valuation leaves add-zone; thesis→Broken | Proposed |

_Rows above are illustrative and generic; the filled private copy replaces them with real proposed actions._

## Per-action detail — one block per row

For each non-trivial action, expand:

> **#N — {Action} {Instrument}**
> - **Rationale** (auditable to the same standard as the log): **valuation zone** (cheap/expensive, ideally a percentile) · **trigger** (valuation primary + optional secondary-trend confirmation) · **thesis status** (Intact / Watch / Broken).
> - **Timing (§6.7):** Window/Trigger · Time-point · Intraday band (if any) · Voids-when. State the *condition*, not a date.
> - **Funding source:** cash / sale proceeds / cycle cash.
> - **Partial-move check:** size ≈ 1/3; not all-in/out (Invariant 3).
> - **Flip / void condition:** the single condition under which this action should not be taken (or reversed, if already partially done).

## Lifecycle rules

1. **Single-directional flow, no shortcuts.** Action Plan → execution → Transaction Log → re-snapshot State. The advisor never edits State to "reflect" a plan.
2. **Status discipline.** An item is *Proposed* until the investor confirms; *Confirmed* when greenlit; *Executed* / *Partially-executed* once filled — at which point the **actual** price/shares/date is appended to the Transaction Log. Unfilled by horizon → *Expired*; invalidated by a void condition → *Voided*.
3. **Partial execution is first-class.** If only 1 of 3 tranches fills, log that one; the remaining tranches stay *Proposed* and must **re-validate their window** before the next fill.
4. **Reconciliation.** The next Portfolio State snapshot reconciles against the **Transaction Log**, never against this plan. A plan is a forecast of intent, not a record of fact.
5. **No personal data in the public repo.** The filled plan (real instruments, sizes, capital) is private; only this blank schema is committed.
