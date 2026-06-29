# Action Plan — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's Action Plan — the advisor's *proposed, not-yet-executed* recommendations.** Carries zero real data — only field definitions and illustrative (generic) examples. To use: the advisor emits a filled instance when proposing trades; the investor reviews, executes (in whole or part), records executed fills in the transaction log, and re-snapshots portfolio state. Like the other runtime files, the filled instance lives in the private `investment-advisor-private/` folder; only this blank schema belongs in the public repo.

**Language note.** This template is canonical control text → English. A **filled instance** is read by the investor to execute trades, so it may be written in the investor's working language (e.g. Chinese) when that aids action; keep instrument codes, action verbs, and the §6.7 field names intact for auditability against this schema.

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
**Buy** = establish 底仓 (value-based) · **Add** = buy-back-low · **Trim** = partial sell-high · **Sell** = full exit (broken thesis, OR a strategic theme-drop / rebalance exit) · **Swap** = paired sell→buy (e.g., re-base a sleeve anchor); on execution it becomes **two** log rows · **Rebalance** = sleeve-level move to restore the 45/45/10 band. Moves are partial (~1/3); never all-in / all-out (Invariant 3) — except a full **Sell** that *removes* a position (broken thesis §6.6, or a theme dropped at the macro layer §5.1), which is a removal, not cycling.

## Timing fields — per framework §6.7

Because the advisor **cannot see future prices and must not pretend to**, each action carries a *condition-based window* and a *concrete advisor-derived target price zone* — never a price forecast:

- **Window / Trigger** — a **condition, not a date**: a secondary-trend + valuation trigger *within the valuation zone* (e.g., "while still in an add-zone and mid-trend not reversed, on a pullback to the recent support band / a failed breakdown / N-day stabilization"). Watched **event-driven per §7** — never a license for daily price-watching.
- **Time-point** — one of **Open** / **Intraday** / **Close**. Open/Close = accept the auction/closing price when execution certainty or end-of-day confirmation matters more than a better tick.
- **Target zone (目标买卖区间)** — **REQUIRED for every action.** A **concrete advisor-derived entry/exit price band**, produced at plan-creation time from technical analysis of the recent K-line (recent support/resistance, the two-MA mid-trend proxy, recent swing highs/lows, volume; for ETFs cross-check IOPV/premium), and **marked with the K-line's data vintage**. It is the operative timing instrument, under four limits: (1) a level to **act-if-reached**, *not* a forecast of the path; (2) a **band, not a tick** (width = honest uncertainty); (3) **subordinate to valuation + thesis** (Invariant 2) — refines where/when, never initiates or vetoes; (4) **advisor-produced, not deferred** — the advisor does the analysis itself and does not punt the level to "confirm live" or to the investor. For Time-point = Intraday it is the limit; for Open/Close it remains the reference the fill is sanity-checked against. The investor confirms the live tick/premium at execution (and may supply a fresher K-line for a tighter band).
- **Voids when** — what invalidates this window/action: valuation leaves the zone, thesis breaks, mid-trend reverses, the band is not reached within the horizon, **or a volume breakdown through a buy-zone's support / breakout through a trim-zone's resistance** (do not average into an accelerating decline; do not chase a runaway breakout). A voided action returns to analysis; it does **not** auto-execute later.

## Plan metadata

- **Plan date (计划日期):** YYYY-MM-DD
- **Based on State snapshot (依据快照):** `portfolio-state_YYYY-MM-DD.md`
- **Overall posture (整体意图):** one line — what this plan is trying to move (e.g., "Phase 1: deploy idle cash into hedge + start core; cash-neutral core re-base").
- **Status legend:** Proposed → Confirmed → Executed (→ logged) / Partially-executed / Voided / Expired.

## Today / delta banner (for a scheduled-run rendered view)

When this plan is emitted as a daily rendered view, lead with a one-screen banner so a solo operator reads top-to-bottom and acts without opening another file:

- **Date · posture** — calm / watch / act (one line).
- **Act-now** — the action(s) triggered *today* (instrument · Buy/Add/Trim/Sell · tranche · Target zone · Time-point · Voids-when · funding), each also reflected in the overview table below so banner and body stay consistent. "No action" is a valid banner.
- **Macro trigger / open-threads delta** — the one-line reason and what changed since the last run.

This is a *presentation order* (most-actionable-first), not a new artifact — the body below is the full standing plan. The monitoring routine writes its actionable findings here (framework §10), rather than into a separate monitor report.

## Embedded State snapshot (read-only, vintage-stamped)

For single-file decision-making, a rendered plan may quote a **compact, read-only** slice of Portfolio State — allocation vs 45/45/10, available cash, and the positions in play (shares / cost / current value) — **stamped with its data vintage** and re-priced per `ia_tpl_portfolio-state.md`. This is a *quote*, not the State of record: it mutates no holdings (Invariant 9), and the authoritative State remains the filled `portfolio-state_*` file.

## Proposed actions — overview

| # | 标的 Instrument (code) | Sleeve | 动作 Action | 规模 Size (¥ / % / shares@exec) | 资金来源 Funding | 窗口/触发 Window/Trigger | 时点 Time-point | 目标买卖区间 Target zone (vintage) | Voids when | 状态 Status |
|---|---|---|---|---|---|---|---|---|---|---|
| _1 (ex.)_ | 示例-宽基ETF (51xxxx) | Stable | Swap (sell old anchor→buy this) | ~X (shares@exec) | sale of legacy ETF | re-base now; not timing-sensitive | Intraday | tranched limits near prior close | n/a (cash-neutral) | Proposed |
| _2 (ex.)_ | 示例-黄金ETF (518xxx) | Hedge | Buy (tranche 1/3) | 1/3 of hedge target | cash | establish now; remaining tranches on pullbacks / over 1–2 wks | Intraday | near IOPV; small premium cap | sharp gap-up → wait | Proposed |
| _3 (ex.)_ | 示例-科技成长股A | Risk | Add (tranche 1/3) | ~1/3 of target add | cycle cash | in add-zone (low pctile) & mid-trend not reversed; on support retest / N-day stabilize | Intraday or Close | near recent support band | valuation leaves add-zone; thesis→Broken | Proposed |

_Rows above are illustrative and generic; the filled private copy replaces them with real proposed actions._

## Per-action detail — one block per row

For each non-trivial action, expand:

> **#N — {Action} {Instrument}**
> - **Rationale** (auditable to the same standard as the log): **valuation zone** (cheap/expensive, ideally a percentile) · **trigger** (valuation primary + optional secondary-trend confirmation) · **thesis status** (Intact / Watch / Broken). For a **§9.3 de-concentration / human-capital trim**, the rationale axis is concentration + correlation (not a valuation-high trigger), though execution still sells into strength (§6.7).
> - **Timing (§6.7):** Window/Trigger · Time-point · **Target zone** (concrete band + data vintage; act-if-reached, not a forecast) · Voids-when. State the *condition* and the *zone*, never a date or a path prediction.
> - **Funding source:** cash / sale proceeds / cycle cash.
> - **Partial-move check:** size ≈ 1/3; not all-in/out (Invariant 3).
> - **Flip / void condition:** the single condition under which this action should not be taken (or reversed, if already partially done).

## Lifecycle rules

1. **Single-directional flow, no shortcuts.** Action Plan → execution → Transaction Log → re-snapshot State. The advisor never edits State to "reflect" a plan.
2. **Status discipline.** An item is *Proposed* until the investor confirms; *Confirmed* when greenlit; *Executed* / *Partially-executed* once filled — at which point the **actual** price/shares/date is appended to the Transaction Log. Unfilled by horizon → *Expired*; invalidated by a void condition → *Voided*.
3. **Partial execution is first-class.** If only 1 of 3 tranches fills, log that one; the remaining tranches stay *Proposed* and must **re-validate their window** before the next fill.
4. **Reconciliation.** The next Portfolio State snapshot reconciles against the **Transaction Log**, never against this plan. A plan is a forecast of intent, not a record of fact.
5. **No personal data in the public repo.** The filled plan (real instruments, sizes, capital) is private; only this blank schema is committed.
