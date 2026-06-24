# Technical Analysis Method — Target-Zone Derivation (技术分析方法)

**Consumption model.** Loaded as project knowledge. This is the **method layer** behind framework §6.7: it specifies *how* the advisor derives the **target buy/sell price zone (目标买卖区间)** that every Action Plan action must carry. Where `ia_mech_market-monitoring.md` is the **macro sensor** (gray-rhino watch), this is the **single-name timing sensor**; both feed the framework controller and never act on their own. Carries **zero personal data** — no holdings, prices-as-positions, or capital; all worked examples use generic placeholders.

**Language.** English, with China-specific proper nouns kept in original (均线, 支撑/阻力, 成交密集区, A股, 港股, IOPV, etc.).

---

## 1. Purpose and honest scope

Framework §6.7 now **requires** a concrete target price zone for every action but states only *what* it is (an act-if-reached band, vintage-stamped, subordinate to valuation+thesis) and *what inputs* feed it. This file supplies the missing *how* — a small, hand-operable kernel for reading a zone off a K-line — without breaching the framework's honesty constraints.

Three inherited limits govern everything below:

- **Subordination (Invariant 2, §6.2).** The zone *refines* an action that valuation + intact thesis has already justified; it **never initiates and never vetoes**. Whether to act is a valuation question; this file only answers *where/when within* an approved action.
- **Honest hit-rate (§6.1).** A secondary (中期) correction and the *onset* of a primary reversal are observationally identical in real time [推断·演绎]; the three-trend taxonomy itself warns the minor trend is noise [通识, Dow Theory / Edwards & Magee — see framework §6.1]. So every read below is a *tilt*, not a forecast. Being early or wrong is absorbed by the ~1/3 partial-move rule (Invariant 3), not by predicting harder.
- **Complexity ceiling (§12).** Two moving averages, swing highs/lows, support/resistance, and volume — nothing else. Operable by hand on a monthly + event cadence. If a refinement can't be run that way, it doesn't belong here.

The output is always an **act-if-reached band with a data vintage**, never a path prediction: "act *if* price reaches this zone," never "price *will* reach it."

---

## 2. Data inputs and vintage

- **Timeframe.** Daily K-line is the working chart; read the **weekly** for the 中期 (secondary) trend. The method is secondary-scale only — never the 1-/5-minute / intraday chart as a signal (§6.1, §12).
- **Window.** Roughly the last **~60–120 daily bars** (or ~one year of weekly) — enough to see the current secondary trend and the last few swings, no more. More history is not more signal at this scale.
- **Vintage stamp (mandatory).** A zone is only valid relative to the K-line it was read from. Record **as-of date + timeframe** with every zone (ties directly to §6.7's "marks the data vintage"). A zone with no vintage is not a deliverable.
- **Re-derive, don't extrapolate.** If the K-line is stale at execution time, the investor supplies a fresher one for a tighter band (§6.7); the advisor does not "age" an old zone forward.

---

## 3. Step 1 — Read the mid-trend direction (the gate)

Establish the secondary-trend tilt; it decides whether you are looking *down* for a buy band or *up* for a trim band.

**Price structure** [网检·高·一手·CFA·2026]:
- **Uptrend** — higher highs **and** higher lows (each retrace bottoms above the prior low).
- **Downtrend** — lower lows **and** lower highs.
- Neither holds → **range / sideways**.

**Two-MA proxy** (the framework's named mid-trend instrument) [网检·高·官方·StockCharts·2026]:
- One **faster** + one **slower** moving average. Their relationship and slope:
  - fast above slow, both rising → 中期 **up**;
  - fast below slow, both falling → 中期 **down**;
  - flat / intertwined → **range**.
- **Periods are a default, not a rule.** Globally cited: **50 / 200-day** for the major trend, a tighter **20 / 50** for a nearer 中期 read [网检·中·多源·2026]; adjust to the instrument's volatility, the holding scale, or local A股 convention. The framework fixes "two MAs as a proxy," not specific lengths — keep it that way.
- MAs read trend **better in trending markets than in ranges** [网检·高·官方·StockCharts·2026]; in a range, lean on the swing structure (Step 2), not the MAs.

**Honest limit.** This direction read is a tilt with a structurally limited real-time hit-rate (§6.1). It may bias *where* you place the band; it may **never** cancel a valuation-justified action because "the chart looks weak" (Invariant 2).

---

## 4. Step 2 — Locate the support / resistance bands

**Definitions** [网检·高·一手·CFA·2026]: **support** = a demand zone where a decline is likely to halt (buyers step in); **resistance** = a supply zone where an advance is likely to stall (sellers step in). Treat both as **zones, not lines** — the width *is* the honest uncertainty [网检·中·多源·2026].

Locate the bands from these sources (rough priority):

1. **Swing highs / lows (structural pivots)** — the primary anchors. A **swing high** is a peak flanked by ~2 lower highs on each side; a **swing low** is a trough flanked by ~2 higher lows [网检·中·多源·2026]. Recent swings matter most.
2. **Volume shelves / 成交密集区** — price areas with prior heavy traded volume tend to act as S/R (a lot of cost basis sits there).
3. **Round-number / psychological levels** — integer handles where orders cluster.
4. **Moving averages as dynamic S/R** — in an uptrend, price tends to **bounce off a rising MA** (support); in a downtrend, a **falling MA caps** rallies (resistance) [网检·高·官方·StockCharts·2026].

**Change of polarity (role reversal)** [网检·高·一手·CFA·2026]: once breached, a **support becomes resistance** and a **resistance becomes support**. Use a prior broken level as the next zone's edge.

**Confluence.** Where ≥2 of the above stack at the same price, the band is stronger and may be drawn **tighter**; an isolated single-source level warrants a **wider** band.

---

## 5. Step 3 — Construct the target zone

Combine the direction (Step 1) + the nearest relevant S/R band (Step 2) + the action's **valuation side** (add vs trim, decided upstream by framework §6.2):

- **Buy / Add zone** — a **support band beneath** current price that you would act *into*, valid only while the name is in an add-valuation zone. Lower edge = the deeper support / would-be breakdown line; upper edge = the nearer support (or a small premium to it).
- **Trim zone** — a **resistance band above** current price that you would sell *into*, valid only in a trim-valuation zone. Edges set symmetrically off the resistance band.

**Band width = honest uncertainty.** Wider when swings are noisy or volatility is high; never collapse to a single tick — that is the false precision §6.7 forbids. A confluent, well-tested level earns a tighter band; a lone level earns a wider one.

**ETF special-case.** Cross-check the chart-derived zone against **IOPV / premium-discount**: do not buy into a rich premium or sell into a deep discount regardless of what the candle says (framework §6.7).

**Output shape.** `{lower–upper price, as-of date + timeframe}` — this is exactly the template's **Target zone (vintage)** field.

---

## 6. Step 4 — Volume confirmation and invalidation

Volume is the **secondary confirmation** Dow already named [通识]: a move *through* a level is trustworthy only on **above-average volume** (real participation); **price up + volume down = a weakening move** (divergence) [网检·中·多源·2026].

This operationalizes §6.7 point 4's hard subordination:

- **Volume breakdown through a buy-zone's support → the buy is voided.** Do not average into an accelerating decline. A failed level on heavy volume is the market repricing, not a discount.
- **Volume breakout through a trim-zone's resistance → the trim is voided.** Do not chase a runaway breakout; let the action lapse and re-analyze.
- **False breakout / fakeout** — a level breached then snapping back into the range, especially on weak volume, is a fakeout. Prefer a **confirmed** break (a close beyond the level *with* volume) over reacting to the first intrabar touch [网检·中·多源·2026]. (A commonly cited rule of thumb is volume well above the recent average — e.g. ~1.5× the ~20-day mean — but treat any specific multiple as a reference, not a hard gate [网检·低·单源·2026].)

A voided zone returns to analysis; it does **not** auto-execute later (mirrors the template's *Voids-when*).

---

## 7. Worked schema (generic — no real data)

Illustrative only; placeholders, not a recommendation. The filled instance is private.

> **Instrument X — Add (tranche 1/3).**
> - **Mid-trend:** range — fast MA flat, price oscillating inside a swing band; weekly not in a clean downtrend.
> - **Support band:** `P_low–P_mid`, from a recent swing low + a round number + a rising slower MA sitting just below (3-source confluence → tighter band).
> - **Target buy zone:** `P_low–P_mid` (Intraday limit), valid while still in the add-valuation zone.
> - **Voids when:** daily *close* below `P_low` on clearly above-average volume (breakdown), or valuation leaves the add-zone, or thesis → Broken.
> - **Vintage:** daily K-line as of `YYYY-MM-DD`.

The same shape inverts for a Trim (resistance band above, void on a volume breakout through the upper edge).

---

## 8. Hard subordinations (these bind — mirror framework §6.7 point 4)

- **Subordinate to valuation + thesis (Invariant 2).** Refines where/when only; never initiates, never vetoes.
- **Secondary scale only.** Never the minor / intraday trend as a signal (§6.1, §12).
- **Act-if-reached, never a forecast.** Reading where S/R sits is legitimate; predicting the candle is not. Being early/wrong is absorbed by the ~1/3 partial move (Invariant 3).
- **Advisor-produced + vintage-stamped (§6.7).** The advisor does this analysis itself and stamps the K-line vintage; the investor's execution-time role is a live tick / IOPV sanity-check (and, optionally, a fresher K-line for a tighter band) — not producing the level from scratch.
- **Complexity ceiling (§12).** The whole kernel is: two MAs · swings · S/R bands · volume. If it can't be done by hand on a monthly + event cadence, it doesn't belong here.

---

## 9. Deliberate exclusions (the don't-over-design boundary, at the TA level)

Mirrors framework §12 for technical work specifically. **Out of scope:** oscillator stacking (RSI / MACD / KDJ ensembles), Elliott Wave / Gann / harmonic patterns, a candlestick-pattern zoo, Fibonacci grids beyond a sanity glance, any intraday / tick system, automated or quant-optimized parameter fitting, and — above all — **path or price prediction**. The method is a deliberately small, robust kernel; its reliability comes from honesty about its limits, not from adding indicators.

---

## 10. Linkage

- **Consumes:** framework §6.1 (honest constraint), §6.2 (subordination), §6.7 (the target-zone requirement + four limits), §12 (complexity ceiling); the instrument's recent K-line + vintage.
- **Produces:** the **Target zone (vintage)** field and the breakdown/breakout **Voids-when** clause of `ia_tpl_action-plan.md`.
- **Pairs with:** `ia_mech_market-monitoring.md` — that file routes *macro* findings to framework actions; this file derives the *single-name* entry/exit zone for an action already justified on valuation + thesis. Monitoring is the sensor, the framework is the controller, and this is the timing instrument the controller reaches for last.
