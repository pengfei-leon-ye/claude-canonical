# Investment Advising Methodology

> **Status:** transformed chat-project replica; not SOT.
> **Authoritative source(s):** `2_topics/investment-advising/methodology.md`; `2_topics/investment-advising/conventions/glossary.md`; `3_projects/investment-advisor/canonical/investor-strategy.md`.
> **Conversation boundary:** This method structures analysis and proposed recommendations in the current conversation. It does not place orders, attest that a trade occurred, or change investor-supplied portfolio facts.

## 1. Purpose

This methodology supports disciplined advice for a concentrated equity-oriented portfolio. It is a bounded decision method rather than an unconstrained search for an abstractly optimal portfolio.

The method:

1. Applies the investor's declared portfolio architecture and risk limits.
2. Searches candidates through a transparent selection funnel.
3. Anchors every recommendation in thesis plus valuation or risk.
4. Uses technical analysis only to refine an already-justified action.
5. Keeps proposals, investor-confirmed transactions, and current holdings conceptually separate.
6. Reviews risk by thresholds and falsifiable conditions rather than impulse.

## 2. Required Inputs

Before a portfolio-sensitive recommendation, establish the relevant inputs:

- current portfolio snapshot and its as-of date;
- current cash or other funding constraint;
- applicable sleeve targets, bands, position limits, and hedge policy;
- thesis status for the instrument or theme;
- recent investor-confirmed transactions when behavior or cost basis matters;
- human-capital concentration where employer or sector exposure is relevant;
- current market, valuation, fundamental, policy, and chart evidence.

If a load-bearing input is missing or stale, request the minimum necessary update. Do not fill the gap with a plausible estimate.

## 3. Portfolio Architecture

Use three sleeves with distinct jobs:

| Sleeve | Decision role |
|---|---|
| Stable / core | Broad exposure, preservation, lower monitoring burden, and steady compounding. |
| Risk / satellite | Concentrated, thesis-driven active positions. |
| Hedge | Insurance against the portfolio's declared systemic tail risk. |

Exact targets and limits come from `ia_investor-strategy.md`. A recommendation must state which sleeve it affects and how the resulting exposure compares with those limits.

## 4. Selection Funnel

Satellite selection follows:

```text
portfolio thesis and investable universe
  -> theme and sub-industry map
  -> candidate universe
  -> coarse screen
  -> finalist basket
  -> valuation-gated recommendation
```

### 4.1 Theme and Sub-Industry

For each theme:

- identify the macro or strategic anchor;
- map relevant upstream and downstream nodes;
- locate nodes where growth remains ahead;
- name the expected moat-formation mechanism;
- identify adjacent nodes excluded because of weak structure, mature growth, or hidden correlation.

### 4.2 Candidate Comparison

Compare candidates on a stable scorecard:

- innovation and pipeline credibility;
- market-share trajectory;
- moat evidence;
- management and governance;
- valuation ceiling;
- differentiation from other candidates in the same basket.

An existing holding has no incumbency privilege. It must re-earn its place against the same criteria as a new candidate.

### 4.3 Search Completeness and Conviction

Keep two judgments distinct:

- **Coarse screen:** `Keep / Watch / Drop`.
- **Thesis status:** `Intact / Watch / Broken`.

A coarse-screen `Watch` means the candidate remains unresolved. A thesis `Watch` means a selected thesis is under pressure. A candidate that survives the coarse screen is not yet a recommendation.

Detailed conversation structures live in `ia_selection-analysis.md`.

## 5. Recommendation Sequence

Every recommendation follows this order:

1. **Mandate and thesis:** confirm that the asset or theme remains within the strategy and that the thesis is not `Broken`.
2. **Valuation or risk basis:** identify why action is justified now—cheapness, expensiveness, concentration reduction, sleeve rebalance, thesis break, or another stated risk basis.
3. **Rival explanation:** present the strongest plausible reason the proposed interpretation may be wrong.
4. **Technical placement:** only after steps 1–3, derive a target zone and condition where appropriate.
5. **Size and funding:** apply tranche discipline, position limits, sleeve effects, and funding restrictions.
6. **Flip and void conditions:** state what would reverse the thesis judgment or invalidate the proposed action.

Technical analysis cannot be the primary reason to act and cannot rescue a missing valuation or thesis case.

## 6. Action Design Discipline

The standard action vocabulary is:

| Action | Meaning |
|---|---|
| Buy | Establish an initial value-supported position. |
| Add | Increase an existing position while the thesis remains intact. |
| Trim | Reduce part of a position without declaring the thesis broken. |
| Sell | Remove a position because of a broken thesis, strategic exclusion, or other full-exit rationale. |
| Hold | Preserve the current position because no action has sufficient support. |
| Swap | Pair a reduction with a new allocation; analyze both legs independently. |
| Rebalance | Move sleeve exposure toward the committed architecture. |

Routine actions are tranche-based. A full exit requires an explicit full-exit rationale.

For every proposed action, state:

- action and instrument;
- thesis status;
- valuation or risk basis;
- size logic;
- funding source;
- sleeve effect;
- target zone where required;
- action condition;
- invalidation condition;
- uncertainty and strongest rival;
- evidence vintage.

`Hold` and `No action` are valid recommendations when the evidence does not justify a change.

## 7. Target-Zone Method

An actionable Buy, Add, Trim, or Sell recommendation normally includes an advisor-derived target zone:

- lower and upper edges rather than a single tick;
- source and as-of date;
- timeframe consistent with secondary-scale analysis;
- trend and support/resistance rationale;
- volume or participation invalidation;
- instrument-specific fair-value check where relevant;
- explicit statement that the zone is act-if-reached, not a path forecast.

If current evidence is insufficient to derive a defensible zone, request a dated chart or decline to provide the zone. Never invent one.

The full method is defined in `ia_technical-analysis.md`.

## 8. Market Monitoring

Monitoring is an evidence-review method, not an independent trade generator. It:

- scans declared risk categories;
- separates events from interpretations;
- rates materiality;
- connects findings to thesis, allocation, concentration, hedge, or flip-condition questions;
- proposes a recommendation only when the strategy already supplies a valid route.

The full method is defined in `ia_market-monitoring.md`.

## 9. Rebalancing

Use thresholds rather than automatic calendar trades:

| Mechanism | Method |
|---|---|
| Inter-sleeve rebalance | When a sleeve breaches a band or ceiling, analyze a move back toward target. |
| Intra-sleeve cycle | Trim or add an individual holding only when thesis, valuation, sizing, and target-zone conditions agree. |
| Hedge maintenance | Preserve the Hedge sleeve unless the strategy's explicit insurance logic justifies a change. |

Rebalancing mechanically trades some upside for risk control. Every recommendation should state that trade-off rather than presenting the move as costless.

## 10. Review Lenses

Keep four analytical lenses distinct:

- **Light review:** valuation, sleeve drift, current price-zone readiness.
- **Fundamental review:** moat, growth, competitive position, governance, and thesis status.
- **Strategic review:** portfolio thesis, sleeve architecture, hedge policy, and flip conditions.
- **Event-driven review:** a focused reconsideration prompted by material new evidence.

Short-term price movement does not by itself justify a fundamental or strategic conclusion.

## 11. Proposal, Transaction, and Portfolio Facts

Three categories must never be conflated:

| Category | What it means |
|---|---|
| Proposed recommendation | What the analysis suggests the investor may consider. |
| Investor-confirmed transaction | What the investor states or supplies evidence actually occurred. |
| Current portfolio context | What the investor currently holds, with an as-of date and source. |

Rules:

1. A proposal does not prove a transaction.
2. A price change does not prove a trade.
3. A change between two portfolio snapshots does not reveal the actual transaction path.
4. Only investor-confirmed execution evidence supports a transaction claim.
5. Unknown or conflicting facts remain explicitly unresolved.

## 12. Evidence Standard

For every load-bearing current claim:

- identify the underlying source;
- state the as-of date;
- distinguish reported fact from analytical interpretation;
- state uncertainty where source quality or timeliness is limited;
- avoid treating a transport channel as proof of source authority.

Current prices, valuations, fundamentals, regulatory facts, policy developments, and news do not come from memory.

## 13. Deliberate Exclusions

- Leverage as a return engine.
- Complex derivatives beyond the approved hedge.
- Day trading or minor-trend systems.
- Technical indicators as a substitute for thesis and valuation.
- Unbounded growth-at-any-price reasoning.
- A recommendation based on fabricated or stale load-bearing inputs.
- Any claim that a proposal has changed the investor's holdings.
