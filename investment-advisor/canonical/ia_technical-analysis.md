# Technical Analysis Method — Target-Zone Derivation

> **Status:** transformed chat-project replica; not SOT.
> **Authoritative source(s):** `2_topics/investment-advising/technical-analysis.md`; `3_projects/investment-advisor/canonical/investor-strategy.md`.
> **Conversation boundary:** This method derives a proposed price band for investor consideration after valuation and thesis already justify an action. It does not predict the future path or claim that an order was placed.

## 1. Purpose and Honest Scope

This method answers:

```text
Where and under what condition could an already-justified action be considered?
```

It does not answer:

```text
Should this asset be bought or sold at all?
Where will price go next?
```

The output is an act-if-reached band with a source and data vintage. It is never a price-path forecast.

Three limits govern the method:

1. **Subordination:** valuation or risk plus thesis decides whether to act; technical analysis only refines placement.
2. **Honest uncertainty:** a secondary correction and the beginning of a primary reversal can look alike in real time.
3. **Complexity ceiling:** use a small, hand-operable kernel—trend, support/resistance, band construction, participation, and invalidation.

## 2. Required Inputs

| Input | Requirement |
|---|---|
| Proposed action | Buy/Add or Trim/Sell/Rebalance leg already justified by strategy. |
| Valuation or risk basis | Cheap/add domain, expensive/trim domain, risk reduction, thesis break, or another explicit strategy basis. |
| Thesis status | Buy/Add requires a thesis that is not `Broken`. |
| Current chart evidence | Dated chart or equivalent market evidence with an identifiable source. |
| Timeframe | Secondary-scale context consistent with long-term ownership; minor or intraday movement is not a signal. |
| Instrument type | Equity, exchange-traded fund, or other eligible instrument, including any relevant fair-value check. |

If current chart evidence is unavailable, request a dated chart or state that no defensible zone can be derived.

## 3. Step 1 — Read the Mid-Trend

Use two forms of evidence:

### 3.1 Price Structure

- **Uptrend:** a sequence of higher highs and higher lows.
- **Downtrend:** a sequence of lower highs and lower lows.
- **Range:** neither structure is stable enough to dominate.

### 3.2 Moving-Average Proxy

Use one faster and one slower moving average:

- faster above slower and both rising supports an upward tilt;
- faster below slower and both falling supports a downward tilt;
- flat or intertwined averages support a range judgment.

Moving averages are weaker in a range. In that case, rely more on swing structure and clearly tested price zones.

The mid-trend is a tilt, not a decision gate. It cannot create or cancel the underlying action.

## 4. Step 2 — Locate Support and Resistance Bands

Treat support and resistance as zones rather than exact lines.

Candidate anchors:

| Anchor | Use |
|---|---|
| Recent swing highs or lows | Primary structural pivots. |
| Prior congestion or volume shelves | Areas where prior trading concentration may affect supply or demand. |
| Round-number levels | Secondary psychological anchor. |
| Moving averages | Dynamic support or resistance when the trend is clean. |
| Polarity reversal | Prior support may become resistance, or prior resistance may become support, after a confirmed breach. |

Recent evidence matters more than remote history. Where several independent anchors cluster, the band may be narrower. Where evidence is noisy or rests on one weak anchor, the band must be wider.

## 5. Step 3 — Construct the Target Zone

| Proposed action | Zone construction |
|---|---|
| Buy / Add | A support band below or near the current market, valid only while valuation and thesis still permit accumulation. |
| Trim / Sell | A resistance band above or near the current market, valid only while valuation, risk, or thesis still supports reduction. |
| Rebalance / Swap | Analyze each component leg separately, or explain why certainty of placement matters more than price refinement. |

Every zone must include:

- lower edge;
- upper edge;
- data as-of date;
- timeframe;
- underlying source;
- trend summary;
- support/resistance anchors;
- invalidation conditions;
- any instrument-specific fair-value check.

The band width expresses uncertainty. A single-tick target is false precision.

For an exchange-traded fund, compare the chart-derived zone with current premium, discount, or available fair-value evidence. Do not recommend buying into a material unexplained premium or selling into a material unexplained discount.

## 6. Step 4 — Define Invalidation

Each zone needs explicit `voids_when` conditions.

Common invalidations:

- valuation leaves the action domain;
- thesis changes to `Broken`;
- the evidence becomes too stale for the proposed action;
- support fails with participation strong enough to invalidate a Buy/Add zone;
- resistance breaks with participation strong enough to invalidate a Trim/Sell zone;
- an instrument-specific fair-value check fails;
- a binding concentration or funding assumption changes.

A voided zone returns to analysis. It is not reused automatically.

## 7. Participation and Break Quality

Participation is secondary confirmation:

- a break with materially stronger participation deserves more weight than a thin move;
- a weak break that quickly returns inside the prior range may be a false break;
- a close beyond the zone carries more evidentiary weight than a brief intraday touch;
- participation evidence does not override thesis or valuation.

Do not hardcode a universal volume multiple. Judge participation relative to the instrument, timeframe, and recent history.

## 8. Target-Zone Content

When presenting a target zone, make clear:

- the proposed action;
- the valuation or risk basis and thesis status;
- the mid-trend and support/resistance anchors;
- the lower–upper target zone;
- the evidence source, as-of date, and timeframe;
- any instrument-specific check;
- the act-if-reached condition;
- what voids the zone;
- material uncertainty.

These are semantic elements, not mandatory visible labels. Integrate them into natural prose when a fixed
shape would add more ceremony than clarity.

Required interpretation:

- the zone is a condition for consideration, not a forecast;
- the proposed action remains subordinate to thesis, valuation, sizing, and funding;
- if the zone is not reached, do not chase;
- if the zone is invalidated, reassess before offering another band.

## 9. Action-Side Heuristics

These are guidance, not hard rules:

- Adding during weakness: prefer a support-based band or evidence of stabilization; do not chase an abrupt rebound.
- Trimming during strength: prefer a resistance-based band; do not dump into a panicked low unless the thesis is `Broken` or another binding risk requires immediate reduction.
- Low-urgency initial position: use tranche logic and a broad condition rather than false precision.
- Strategic exit with an intact thesis: seek orderly reduction where practical.
- Broken thesis: technical placement may reduce avoidable price damage, but cannot veto the exit rationale.

## 10. Deliberate Exclusions

- Indicator stacking.
- Elliott Wave, Gann, harmonic, or similarly elaborate pattern systems.
- Candlestick-pattern catalogues as a primary method.
- Minor or intraday trend systems.
- Parameter fitting presented as certainty.
- Path or price prediction.
- A target zone without source and data vintage.
- A technical conclusion used as the primary reason to Buy, Add, Trim, or Sell.
