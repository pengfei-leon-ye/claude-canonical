# Investment Strategy Framework (Operating Model)

**Consumption model.** Loaded as project knowledge by the claude.ai Investment Advisor project, and used as the operating logic for every recommendation. This document is **pure methodology and carries zero personal data** — the investor's positions, cost basis, capital, and transaction history live only in separate uploaded data files (private project knowledge), never here. Think of this file as the operating system and the data files as runtime state.

**Language.** English, with China-specific proper nouns kept in original (十五五, 沪港通/港股通, A股 主板/创业板/科创板, 红利低波, etc.).

---

## 1. Objective and core thesis

The portfolio splits total capital into sleeves with distinct jobs:

- **Stable sleeve (core)** — capital preservation and steady, low-maintenance compounding. Job is stability, not alpha.
- **Risk sleeve (satellite)** — concentrated, high-conviction bets on *future* sector and company leaders, managed with long-term value holding plus auxiliary mid-trend technical timing.
- **Hedge sleeve** — tail insurance against single-country systemic shock.

### 1.1 The risk sleeve's objective function: chip thinking (筹码思维)

The risk sleeve is **not** optimized for realized P&L. Its success metric is **chip accumulation and cost-basis reduction on the target holdings** — either holding a fixed share count at progressively lower cost, or holding more shares for the same capital. The investor is a long-term *owner* of these businesses who uses price volatility to accumulate ownership, not a trader harvesting cash gains.

This distinction governs how success is measured: count **shares accumulated and cost basis**, not just unrealized gains. It also carries one specific failure mode, guarded in §6.5.

### 1.2 The China-overweight bet (explicit, bounded, falsifiable)

The entire portfolio is deliberately concentrated in 中国 A股 (主板/创业板/科创板) and 港股 (via 沪港通/港股通), expressing a conviction that China outperforms the world over a 5–10 year horizon. This is a **conscious active bet, not a diversified posture.**

Treat it as a falsifiable thesis, not an article of faith. By standard portfolio theory this is textbook home-country concentration risk — the whole portfolio rides one country's political, regulatory, currency, and systemic fortunes, with no geographic offset [网检·中·多源·2026]. The framework accepts the bet but bounds it two ways: (a) the hedge sleeve (§4) buys partial tail insurance without materially diluting the thesis; (b) the bet has **flip conditions** reviewed annually (§7):

- Sustained structural breakdown evidence (productivity/debt/demographics trajectory durably negative, not cyclical).
- Policy turning structurally hostile to private capital formation or to the investor's accessible channels (沪港通/港股通 access, 科创板/创业板 listing economics).
- A decoupling severe enough to cut the growth premium the thesis depends on.

If a flip condition triggers, the response is to **reduce the overweight and widen the hedge**, not to abandon the framework. Absent a trigger, hold the bet through cyclical drawdowns — that is what conviction means.

---

## 2. Portfolio architecture: 45 / 45 / 10

This is the textbook **core-satellite** construction (core = passive/diversified/low-turnover; satellite = active/concentrated/high-conviction) [网检·中·多源·2026], extended with a tail-hedge sleeve.

| Sleeve | Target | Role |
|---|---|---|
| Stable (core) | **45%** | Preservation + steady compounding |
| Risk (satellite) | **45%** | Future-leader growth, chip accumulation |
| Hedge | **10%** | Single-country tail insurance |

The 45/45 keeps the investor's chosen **1:1 stable:risk** relationship while the hedge is carved from the top. The hedge may flex to 15% in elevated-risk regimes (→ 42.5/42.5/15). This is a moderately aggressive posture — half the portfolio is active concentrated bets — chosen deliberately for the conviction horizon, not because it is the "stable" default. Standard core-satellite would run a larger core (70–90%) [网检·中·多源·2026]; the investor accepts the higher active weight knowingly.

---

## 3. Stable sleeve (core) — selection logic

**Default to ETFs over individual stocks for the core.** The core's job is stability and low monitoring burden; individual stocks add idiosyncratic risk and pull attention that belongs on the risk sleeve.

Two complementary building blocks (not either/or):

1. **Broad-base ETF** (沪深300 / 中证A500) — China-beta anchor.
2. **红利低波 ETF** (中证红利低波动 / 港股通红利 类) — the defensive, income, low-volatility anchor. 红利低波 strategies pair high dividend yield with low volatility, giving stronger downside defense as the domestic interest-rate centre trends down [网检·中·多源·2026]. (Specific products and their AUM/liquidity change — re-verify current data before any purchase rather than relying on a name in this file.)

Individual high-dividend stocks are permitted only as a small yield enhancement *if* the investor wants to monitor them — but that blurs into satellite work and should stay marginal. Keep the core boring on purpose.

The stable sleeve also follows the same regular review (§7) and rebalancing (§8) as the rest of the portfolio; "stable" means low-turnover, not unattended.

---

## 4. Hedge sleeve — selection logic

**Purpose: insurance, not return.** The hedge holds ~10% in assets whose risk is **not** China-systematic — gold ETF and/or QDII exposure to non-China assets are the natural instruments via the investor's accessible channels. Judge this sleeve by whether it pays off when China assets sell off together, not by its standalone return.

It earns its place through a **counter-cyclical rebalancing property**: when China assets crash (risk-off), the hedge tends to hold or rise; the rebalancing bands (§8) then mechanically trim the hedge and add to cheap China assets — a disciplined "buy China cheap with insurance proceeds" reflex, executed by rule rather than nerve. This is the real structural defense against tail events; news monitoring (§ monitoring rubric) is secondary to it.

---

## 5. Risk sleeve (satellite) — selection funnel

Top-down thematic selection: **macro direction → sub-industry → company.** The governing principle is to **bet on the strongest future growth, not the current strongest incumbent** (Philip Fisher growth investing), with the discipline guards below.

### 5.1 Macro layer — define the big industries

Anchor on two inputs:

- **十五五规划 (2026–2030)** — the published 纲要 priorities point to: 新质生产力, 科技自立自强, 制造业高端化/智能化/绿色化, 未来产业, 数字经济与 AI, 绿色低碳 (e.g. 风光装机 / 氢能 / 储能 expansion targets), with national R&D spend set to grow ~7%+ annually [网检·中·官方·2026Q1]. Re-read the live 纲要 and annual 两会 updates rather than this summary when it matters.
- **Geopolitics / 风向** — tension elevates 自主可控 / 国产替代 / supply-chain security themes (semiconductors, key materials, critical equipment, energy security). Read which way policy and capital are being pushed.

### 5.2 Sub-industry layer — refine, and avoid the wrong structures

From the macro themes, extend up- and down-stream to find the best risk/reward node. Prefer sub-industries that satisfy:

- Policy tailwind (aligned with §5.1).
- **Rising penetration curve, early-to-mid S-curve** — growth ahead, not behind.
- **Competitive structure forming but not yet closed** — room for a future leader to emerge.
- A **moat-formation mechanism** (scale economics, network effects, technology/IP, switching costs, regulatory licence).

Avoid: red-ocean commodity competition, and industries whose structure is **already settled** (note the deliberate tension with Buffett, who *prefers* settled, predictable, moated businesses — the investor is consciously trading certainty for growth upside, which is valid but demands the position-sizing and basket guards below).

### 5.3 Company layer — future leaders, with guards

Within a chosen sub-industry, select 2–3 names as a **basket per theme**, never a single bet on one "future leader" (survivorship bias is severe — the winners are remembered, the failed candidates forgotten). Selection criteria:

- R&D intensity and a credible innovation pipeline.
- Market-share **trajectory** (gaining, not just large).
- Evidence a moat is actually forming (not just a good story).
- Management/governance quality — verify via scuttlebutt (channel checks, customers, suppliers, ecosystem), Fisher-style, not just financials.
- A **valuation ceiling** — even a great future leader is a bad investment at any price. Impose a sanity check (e.g. growth-adjusted valuation); do not pay an unbounded premium for growth.

**Held-name neutrality.** These criteria are the *only* basis for selection. A name already in the portfolio gets **no priority** for being held — incumbency is not a selection criterion, and treating it as one invites endowment bias. Every existing holding must re-earn its slot against the same future-leader test as any new candidate, or be replaced; "I already own it" is not a thesis.

**Listing-venue neutrality.** Select the future leader on its merits irrespective of A股 / 港股 listing; the resulting A/H mix of a sleeve is an *output* of selection, never a hard pre-filter on it (venue risk-tiering and its one admissible hard rule — an H-ceiling, never an H-floor — live in §9.4).

---

## 6. Trading method — the heart of the risk sleeve

The risk sleeve combines long-term value holding with **auxiliary** mid-trend (secondary-trend) technical timing. Theoretical basis: Dow Theory / Edwards & Magee three-trend taxonomy (primary / secondary / minor), where the **minor** trend is explicitly unpredictable noise [通识].

### 6.1 The honest constraint: why technical stays auxiliary

A secondary (中期) correction and the *onset* of a primary reversal are **observationally identical at the moment they begin** — the distinction is only confirmable in hindsight [推断·演绎]. Therefore mid-trend timing has a structurally limited real-time hit-rate: act on it as the *primary* signal and you will sometimes sell into a continuing primary advance (selling the compounder away) or buy into a primary reversal (catching a falling knife). This is exactly why the technical read is **timing refinement only**, never the primary trigger.

### 6.2 The method statement

> **Valuation sets the zone (whether to act); the secondary-trend signal sets the timing (when to act within the zone).**

Valuation percentile + intact thesis decides whether a name is in a *trim-candidate* zone (expensive) or an *add-candidate* zone (cheap). Only inside a valuation-justified zone does the mid-trend signal refine entry/exit timing — to avoid trimming too early into continued strength, or adding too early into continued weakness.

### 6.3 The self-funding sell-then-buy cycle (先卖再买)

Unlike typical retail (chase highs, panic-sell lows), the steady-state cycle is **sell-high-first, then buy-back-lower**:

1. Establish an initial position (底仓) on a *value* basis (buy when undervalued).
2. In steady state: at a valuation-high zone (timing-confirmed), **trim a tranche** → raise cash; at a valuation-low zone (timing-confirmed), **deploy that cash to buy back more shares**.
3. Net effect over a full cycle: more shares / lower cost basis — the chip-thinking objective (§1.1). The cycle self-funds; it needs no idle cash beyond the initial 底仓.

### 6.4 Two non-negotiable invariants on the cycle

- **Net-long bias (持有时间 > 不持有时间)** — maintain net-long exposure at all times; fully-out periods are rare and brief. The investor is a long-term holder who occasionally trims, not a trader who occasionally holds. This anchors the whole method to time-in-the-market and self-limits trade size and frequency (over-trimming would violate it).
- **Partial moves only (≈1/3)** — never all-in or all-out on one signal. Survives being early or wrong.

### 6.5 Trim-intensity dial (replaces a rigid compounder/cyclical split)

How aggressively a name is cycle-traded scales **inversely with its conviction / compounder quality**:

- **High-conviction compounders in a primary uptrend** → *low* trim-intensity. Small trims at extreme valuation only. Rationale: in a strong primary advance, secondary corrections get shallower; trading them risks selling the compounder away (卖飞), the costliest error. Let winners run.
- **Cyclical / mean-reverting names** → *high* trim-intensity. This is the main arena for the 先卖再买 cycle, where price oscillation reliably converts into chips.

Operate it as two practical tiers (compounder / cyclical) for simplicity, understanding the underlying variable is a continuous dial.

### 6.6 The chip-thinking guardrail (the one real failure mode)

Chip accumulation is the objective **only while the fundamental thesis holds.** If the quarterly fundamental review (§7) judges the thesis broken (moat eroding, growth trajectory failed, governance red flag), **exit regardless of share count** — do not average down into a broken thesis. Without this guard, "I'm accumulating chips" becomes a universal excuse for holding a value trap. This is the single line separating chip thinking from catching a falling knife.

### 6.7 Trading windows and execution timing (auxiliary; secondary-scale only)

**Purpose.** Once an action is justified by valuation + intact thesis (§6.2), this section governs *when* and *how* to place it — without letting execution timing degrade into the minor-trend / daily-watching behavior the framework forbids (§6.1, §7, §12). It exists because the advisor **cannot see future prices and must not pretend to**; the honest output is a *condition-based window* plus a *concrete advisor-derived target price zone*, never a price prediction.

**Subordination (the governing principle).** Timing refines an action that valuation + thesis has *already approved*. It **never initiates and never vetoes**: do not skip a valuation-justified action because the chart looks ugly, and never act on the chart alone. (Reaffirms Invariant 2.)

**1. Window = condition, not a calendar date.** Express the entry/exit window as a *trigger condition* on the **secondary (中期) trend within the valuation zone**, not as "act on day X." Example: *while still in an add-zone and the mid-trend has not reversed, deploy the next ~1/3 tranche on a pullback to the recent support band, a failed breakdown, or N-day stabilization.* The condition is watched **event-driven per §7's cadence** — it does **not** license daily price-watching (§7's behavioral hazard). The point of a condition (vs. a date) is that it survives the market not cooperating on your chosen day.

**2. Three time-points, and a target price zone the advisor derives at plan time.** Every placed action resolves to one of:
- **Open** — accept the opening-auction price.
- **Intraday** — place a limit in the target zone (below).
- **Close** — accept the closing price.

Use Open/Close only when **execution certainty or end-of-day confirmation outweighs a better tick**. **In all three cases the advisor derives and states a concrete target entry/exit price *zone* at plan-creation time**, from technical analysis of the instrument's recent K-line — recent support/resistance, the two-MA mid-trend proxy, recent swing highs/lows, volume; for ETFs cross-check IOPV/premium. The zone is the operative timing instrument, under four limits:
- **A level to act *at*, not a forecast of the path.** The zone says "act if price reaches it," never "price will reach it." Reading where support/resistance sits is legitimate technical work; predicting the candle is not — the rule requires the first and still forbids the second.
- **A band, not a tick** — its width is the honest expression of uncertainty; a single-tick target is false precision.
- **Subordinate to valuation + thesis (Invariant 2)** — it refines *where/when* inside an already-justified action; it never initiates or vetoes.
- **Advisor-produced, not deferred — sourced from the best market data the runtime environment offers.** The advisor does this analysis itself when asked for a plan and **marks the data vintage** of the K-line/quote it used; it does not punt the level to "confirm live" or to the investor. It obtains the current K-line and market data from the **best source its runtime environment provides** — a live market-data tool/skill where one is available (the advisor fetches the data directly), otherwise an investor-supplied K-line/screenshot. If neither is available it states it cannot derive the zone and asks for the input, rather than fabricating one. The investor's execution-time role is then a final live IOPV/tick sanity-check — and, where the advisor cannot self-fetch, supplying the K-line — not producing the level from scratch.

**3. Time-point heuristics (guidance, not hard rules).** These follow from *don't transact against the day's dominant pressure*, not from candle prediction:
- **Adding in weakness / a downtrend** → Intraday limit near the support band, or Close (let the day's selling exhaust); do not chase.
- **Trimming in strength** → Intraday limit near the resistance band, or Open (lock in); do not dump into a panicked open.
- **Low-urgency base-building** → Intraday tranched limits (DCA-like).
- **A strategic exit (theme-drop or rebalance) of a name whose thesis is *not* broken** → still sell into strength: Intraday limit near the resistance band, or on a bounce; **do not dump at the lows.** Only a *Broken* thesis (§6.6) overrides this and licenses exiting regardless of price.

**4. Hard subordinations (these bind).**
- **Technical never overrides valuation + thesis** — refine / tranche only; never skip a valuation-justified action for chart reasons; never act on the chart alone. (Invariant 2)
- **Secondary scale only** — never the minor / intraday trend as a signal. (§6.1, §12)
- **Honest hit-rate** — since a secondary correction and the onset of a primary reversal are *observationally identical in real time* (§6.1), timing serves only to avoid an obviously bad tick and modestly improve entry; it is **never** a reliable signal, and being early/wrong is absorbed by the ~1/3 partial-move rule. (Invariant 3)
- **Complexity ceiling (§12)** — operable by hand on a monthly + event cadence: two moving averages as a mid-trend proxy, recent highs/lows, support/resistance, volume confirmation. No indicator-stacking, no intraday system, no quant optimization.
- **Breakdown / breakout invalidates the zone.** A **volume breakdown through a buy-zone's support** invalidates the buy — do not average into an accelerating decline; a **volume breakout through a trim-zone's resistance** invalidates the trim — do not chase a runaway breakout. (Extends the honest-hit-rate limit above.)

This section is consumed by the Action Plan template (`ia_tpl_action-plan.md`): every proposed action carries `{Window/Trigger · Time-point · Target zone (+ data vintage) · Voids-when}` derived from the rules above. The **method** for deriving that target zone — mid-trend read, support/resistance bands, zone construction, volume confirmation/invalidation — is specified in `ia_mech_technical-analysis.md`.

---

## 7. Review cycles — three clocks

Separate the cadences; conflating them induces over-trading. Daily price-watching is a behavioral hazard, not diligence.

- **Monthly — valuation / position monitoring (light).** Check valuation percentile + mid-trend signal for each risk-sleeve name and the sleeve allocations. **Act only when a rebalancing band is breached or a name enters a clear trim/add zone.** Most months: no action. (Monthly cadence matches the secondary-trend timescale of weeks-to-months; act event-driven if a move is fast.)
- **Quarterly — fundamental thesis review (deep).** Aligned to 财报 (季报/年报). Re-validate each risk holding's thesis: moat, growth trajectory, competitive position. This is where §6.6 (broken-thesis exit) is adjudicated. The "weighing machine" cadence.
- **Annual — strategic review.** Aligned to 两会 and 十五五 mid-course updates, plus event-driven. Re-test the China-overweight thesis and its flip conditions (§1.2); re-check sector theses against the macro layer (§5.1); confirm sleeve targets still match risk tolerance and life stage.

---

## 8. Rebalancing

Threshold-triggered, **not** calendar-driven — research finds threshold/tolerance-band rebalancing preferable to fixed calendar rebalancing on a cost/benefit basis (a band of roughly ±5pp at the major-asset level captures the large majority of the benefit at a fraction of the turnover) [网检·中·3独立源·2022]. Two distinct mechanisms — do not conflate them:

### 8.1 Inter-sleeve rebalancing (the 45/45/10 split)

- **Asymmetric bands ±7–10pp.** Because the China-growth thesis expects the risk sleeve to outperform, use a slightly wider band before trimming the winner (let it run) than a naive ±5pp — reducing turnover and respecting the thesis. Rebalance a sleeve back toward target when it breaches its band.
- **Hard ceiling: risk sleeve ≤ 65% of total.** Regardless of bands, trim the risk sleeve if it exceeds this — bounds tail exposure.
- **Hedge** rebalances back toward 10% on the same band logic, which produces the counter-cyclical reflex in §4.
- **Annual check** as a backstop in addition to band triggers.
- Note the structural trade-off: rebalancing mechanically trims the winning sleeve, capping some upside in exchange for risk control. The asymmetric band is the chosen compromise between discipline and letting the thesis breathe.

### 8.2 Intra-sleeve cycling (within the risk sleeve)

This is the §6 trading method — the 先卖再买 cycle on individual names. It is *not* the same as the 45/45/10 rebalance and operates on its own valuation+timing triggers per name.

---

## 9. Position sizing and count

Diversification research: ~20–30 stocks capture the large majority of diversifiable risk reduction; beyond ~15 the marginal benefit is small for large-caps, and excess names become *diworsification* — diluting best ideas and exceeding monitoring capacity [网检·中·多源]. The binding constraint is **monitoring bandwidth × minimum effective position size**, with capital only a proxy.

- **Stable sleeve:** 2–4 ETFs is sufficient (broad-base + 红利低波 + optional). More adds nothing.
- **Risk sleeve:** target **8–12 names across 3–5 themes** (2–3 per theme). Below ~8 = excessive idiosyncratic risk on unproven future-leaders; above ~15 = theses outrun attention.

### 9.1 Capital-tier rubric (generic — the investor's actual tier lives in private data, not here)

- **Small (< ~¥500k):** lean on 行业 ETF even in the risk sleeve rather than single names; ~5–8 total positions; single A股 names need a meaningful weight each (A股 lot = 100 shares) to matter against fees/slippage.
- **Medium (~¥500k–3M):** the full funnel works; ~8–12 risk names + 2–3 core ETFs.
- **Large (> ~¥3M):** up to ~12–15 risk names with finer sub-theme granularity; here **monitoring bandwidth (time), not capital, is the real ceiling.**

### 9.2 Per-position guardrails

- **Max:** single risk-sleeve position ≤ ~15% of the risk sleeve (≈8% of total) — bounds single-name blow-up.
- **Min:** ≥ ~2–3% of the risk sleeve — below this a 2× move barely moves the portfolio, so the monitoring cost isn't earned.

### 9.3 Human-capital / employer-concentration adjustment

The §9.2 caps bound *financial-position* size. They are blind to **human capital** — the present value of future earnings (salary, vesting equity, career optionality), which for most investors is their single largest asset and is often concentrated in one employer or sector. When human capital is concentrated, **total economic exposure** to that name/sector = financial position + human capital, and the two are **positively correlated**: a shock to the employer hits salary, vesting equity, *and* the stock together (the canonical own-employer-stock trap).

Rule: **the financial portfolio must underweight whatever the investor's human capital is already concentrated in.**
- **Employer's own stock** (including RSU-sourced holdings): hold the financial position **well below the normal per-position cap (§9.2), biased toward minimal**, and reduce it over time. The human-capital stake already supplies the (over-)exposure; the financial stake mostly doubles a correlated bet. This holds **even when the company's investment thesis is Intact** — the issue is correlation and concentration, not company quality.
- **The career's sector**: add **no** satellite *theme* in that sector — the career already is the (over-)allocation; a financial theme on top concentrates total wealth in one factor. Route proceeds from trimming the employer stock into **uncorrelated** assets (other sleeves/themes), never back into the same sector.
- **Execution** still respects the trading method: trim in tranches into strength (§6.7), never a panic dump; and account for an ongoing RSU-vesting pipeline (which re-adds exposure) with a **standing trim-as-vested policy** rather than one-off action.

This adjustment only **tightens** the concentration discipline; it never loosens it. Human-capital exposure is assessed separately and is **invisible in a brokerage snapshot** — it must be carried as a known input, not inferred from holdings.

### 9.4 Listing-venue (A股 / 港股) concentration — a graded factor, not a hard quota

§9.2 bounds *how much* and §9.3 *correlated-with-what*; both are blind to **where a holding is listed**. Within the China-overweight bet (§1.2), A股 (主板/创业板/科创板) and 港股 (港股通) are **not interchangeable**: they price off different marginal buyers and carry different tail profiles [通识]. A股 is domestic-retail-driven with administrative price intervention (涨跌停, IPO/再融资 pacing, national-team support) and a closed capital account; 港股 is offshore-/foreign-flow-driven, USD-peg- and global-liquidity-linked, with cleaner price discovery but a heavier geopolitical / foreign-capital / channel-access tail. Dual listings persist at an A-over-H premium, so an issuer's H line is the structurally cheaper claim on identical cash flows [通识].

**What venue does and does not diversify.** A and H share the *same* sovereign / policy / macro fundamentals, so an A/H blend does **not** diversify the core China bet (§1.2) — a real structural break hits both. It diversifies only the **microstructure / capital-flow layer** (a domestic-liquidity-driven A drawdown and a global-risk-off H drawdown can fall out of phase). Reducing *country* concentration is the hedge sleeve's job (§4), not venue's.

**Venue freedom is inversely correlated with a sleeve's risk tier — so steer venue where it is cheap.**
- **Low-risk-tier sleeves (Stable, §3):** venue is a near-free choice; the stability mandate favors A (national-team floor, no 港股通 dividend-withholding drag, lower geopolitical β). A *deliberate* venue tilt belongs here — it costs no alpha.
- **High-risk-tier sleeve (Risk satellite, §5):** venue is **dictated by where the future-leader is listed**, not chosen — many 科技自立自强 leaders (科创板 semis) are A-only with no H twin. So **the satellite's A/H mix is an *output* of §5 selection, never a hard pre-filter.** Forcing a venue quota here rejects the best name for a listing reason — a §5 violation. Venue follows alpha: where a theme's strongest name is H-listed, prefer it on merit.

**Hard-rule asymmetry (the operative guard).** If venue is ever made a *hard* constraint, only one direction is admissible. A hard **H-ceiling** (bounding the geopolitical / foreign-flow tail) is **cheap** — the satellite is already A-heavy, so a ceiling adds no selection constraint. A hard **H-floor** (forcing minimum H for regime diversification) is **expensive** — it reaches into the satellite and forces inferior or non-existent H picks, corrupting §5; satisfy any desired H presence opportunistically through venue-flexible / low-risk-tier holdings (a held H quality-anchor, a Stable slice) instead, never via a satellite quota.

**Net.** Venue (A/H) is a **monitored diagnostic and a graded input to risk-tiering**, not a separate knob with a fixed ratio — a fixed sub-allocation would over-design (§12) and double-count risk already bounded by §9.2 + the hedge sleeve. The *direction* of any deliberate lean reduces to a §1.2 flip-condition judgment: which China tail is the more probable near-term — a geopolitical / foreign-capital shock (argues to underweight H) or a domestic-policy / capital-control / 港股通-access shock (argues to retain offshore-mobile H). This is deliberately **not** an Invariant (§11): no hard quota, just a factor weighed at each rebalance and at satellite-selection time.

---

## 10. Runtime data interface

Runtime state lives in **three artifacts with a single-directional flow** — never collapse them:

| Artifact | Answers | Mutation rule |
|---|---|---|
| **Portfolio State** (`ia_tpl_portfolio-state.md`) | what the investor **holds** | refreshed wholesale at each review |
| **Transaction Log** (`ia_tpl_transaction-log.md`) | what the investor **has done** | append-only; executed fills only |
| **Action Plan** (`ia_tpl_action-plan.md`) | what the advisor **proposes** | items resolve (executed / voided / expired) |

**Flow:** analysis → **Action Plan** (pending, with §6.7 timing) → investor executes → record fills in the **Transaction Log** → re-snapshot **Portfolio State** (reconciled against the log, not the plan). The advisor *reads* State + Log as inputs and *writes* the Action Plan as output; it **never** edits State directly (Invariant 9).

**Portfolio-State update modes — re-price vs re-snapshot (do not conflate).**
- **Re-price (mark-to-market):** between trades, with **share counts and cost basis held fixed**, refresh market value / current % / unrealized P&L / valuation percentile from the live data source — prices, and **dividends, 送转/拆股 corp-actions, and FX** where the source provides them. Automatic, frequent, near-zero-cost; accuracy bounded by the data source. Changes no share count, cost, or record of fact.
- **Re-snapshot (authoritative):** required after any **share-count change** (an executed trade, or a 送转/拆股 corp-action) **or account-level cash flow** (external transfer, repo interest, fees, settlement timing). Sourced from the broker — a screenshot is acceptable; **the investor dropping that screenshot is the trigger, and the routine follows up — no second manual step.** **The gate is verification, not human sign-off.** Verify the parse by **reconciliation**: internal identities (`shares × price = market value`; `Σ market values = total`; `(price − cost) × shares = P&L` where shown) **plus an independent price cross-check** against the live data source for the snapshot's as-of date. A position that reconciles within tolerance is *verified* and may be **auto-committed (no human step)**; a field that fails to reconcile or has no cross-check (cost with no P&L shown, an unknown ticker, a price mismatch) is **flagged for the investor, not committed**. Never fabricated. State changes from a **holdings** snapshot; **fills come from a 成交回单, never inferred from a State diff** — and a provided 回单 **overrides any trade path the advisor earlier inferred from a State delta (an overwrite, not a "pending investor confirmation" item)**; a holdings change with no matching fill record is flagged. Reconcile the result against the **Transaction Log**.
- Re-pricing must **not silently absorb** a share-count or cash event; if one may have occurred, trigger a re-snapshot rather than pass a stale-share mark-to-market off as truth. The source-blind inputs are the investor's **actual trades** (→ Transaction Log), **account-level cash flows** (**confirmed only by a 资金流水/对账单 — neither a holdings snapshot nor a 成交回单 shows a cash transfer; absent it, flag as awaiting that source, never infer**), and **dividend tax-net** (gross is data-sourced; net needs the per-lot holding-period tax rule). Equity-vesting is **not** a Portfolio-State share-count event — vested employer stock sits outside the tracked brokerage portfolio and is the §9.3 human-capital input; only an actual deposit of those shares into the tracked account is a re-snapshot trigger.

**Transaction Log is fill-sourced, not diff-derived.** Populate it from actual executed fills, never by diffing two Portfolio-State snapshots — a diff keeps only the *net* change and silently loses intra-period round-trips, per-trade price/time, and rationale, which are exactly what the net-long-invariant check and the behavior audit depend on. State-vs-log is a reconciliation *check*, not a log generator.

**Monitoring writes into the Action Plan, not a parallel report.** The market-monitoring routine (`ia_mech_market-monitoring.md`) is an *analysis* producer in the flow above: an actionable finding becomes a **Proposed Action-Plan item** (Invariant 9), and a scheduled run's daily deliverable is a **rendered view of the current Action Plan** — today's action first, the standing plan and a compact read-only vintage-stamped State snapshot beneath — **not a fourth runtime artifact**. Solo-operator ergonomics: what is read together at decision time (the action + the relevant State slice) lives in one file; State and Log, read in the separate reconcile session, stay separate.

The advisor reads private state from the uploaded data files (never from this document):

| Data needed | Used for |
|---|---|
| Current holdings per sleeve (ticker, share count, cost basis) | Current allocation vs 45/45/10; valuation vs cost; chip-count tracking; **A/H venue mix per sleeve** — derived from each holding's ticker (A股 vs 港股), the §9.4 listing-venue diagnostic (a graded risk-tiering input, no stored field) |
| Available capital / cash | Funding the 先卖再买 cycle and adds; tier calibration |
| Transaction log (chronological) | Net-long-invariant check; cost-basis evolution; behavior audit |
| Human-capital concentration (employer / career sector; equity-vesting pipeline) | §9.3 / Invariant 10 — underweight correlated exposure (total economic exposure = financial + human capital); standing trim-as-vested. Invisible in a brokerage snapshot, so supplied as a known input |

Rules: never fabricate any of these; if a value is missing or stale, ask or request a data-file refresh; treat all prices and fundamentals as needing a current source — obtained from the **best market-data source the runtime environment provides** (a live data tool/skill where present, otherwise investor-supplied), never from memory. (The private state files above carry holdings/capital; live *market* data — prices, K-lines, fundamentals — is acquired at analysis time per this rule, distinct from those files.) This document and anything synced to the public repo carry **none** of this data.

**File schema (the data contract).** The exact format of these files is defined by the canonical schema templates `ia_tpl_portfolio-state.md` (holdings + capital snapshot), `ia_tpl_transaction-log.md` (append-only trades), and `ia_tpl_action-plan.md` (proposed, not-yet-executed actions), versioned alongside this framework. Those templates are blank schemas carrying only field definitions and illustrative examples; the investor's *filled* instances are private (local `investment-advisor-private/`, never committed), and only the filled copies are uploaded to project knowledge — the `.env.example` / `.env` split.

---

## 11. Invariants (single-list summary)

1. Net-long bias — holding time > out time; long-term holder, not trader.
2. Valuation-anchored, technical-auxiliary — valuation+thesis is primary; mid-trend timing only refines execution.
3. Partial moves only (~1/3) — never all-in/all-out.
4. Broken thesis → exit regardless of chip count — no averaging down into a broken thesis.
5. Compounders get low trim-intensity — don't sell winners on ordinary secondary dips.
6. Hedge sleeve maintained — insurance, not a return source to raid.
7. Concentration ceilings — single risk position ≤ ~15% of sleeve (~8% total); risk sleeve ≤ 65% of total.
8. China-overweight is a falsifiable bet — hold through cyclical drawdowns; reduce only on a stated flip condition.
9. Advice → Action Plan only — a recommendation materializes only in the Action Plan; it never directly mutates Portfolio State (holdings change only via execute → log → re-snapshot). Keeps *what I propose / what I hold / what I have done* cleanly separated.
10. Human-capital-aware concentration — the financial portfolio underweights whatever the investor's human capital (employer / sector) is already concentrated in; an employer's own stock is held well below the normal per-position cap **regardless of thesis quality**, and no satellite theme is added in the career's sector. (§9.3)

---

## 12. Deliberate exclusions (the don't-over-design boundary)

No leverage. No derivatives beyond the simple hedge. No day-trading or minor-trend timing. No complex factor models or quant optimization. No unbounded growth-at-any-price. The method's complexity ceiling is **what one person can execute by hand on a monthly + quarterly cadence.** If a proposed sophistication can't be operated at that cadence, it doesn't belong here. Execution-timing refinements (§6.7) operate strictly within this ceiling — secondary-scale and hand-operable — and never reintroduce minor-trend or intraday systems.
