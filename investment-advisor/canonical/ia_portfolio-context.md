# Portfolio Context — Conversation Input Contract

> **Status:** transformed chat-project replica; not SOT.
> **Authoritative source(s):** `3_projects/investment-advisor/canonical/templates/portfolio-state.md`; `3_projects/investment-advisor/canonical/templates/transaction-log.md`; `3_projects/investment-advisor/canonical/advisor-role.md`; `3_projects/investment-advisor/canonical/investor-strategy.md`.
> **Conversation boundary:** This document defines the portfolio facts needed for analysis. Only investor-supplied or independently sourced evidence establishes those facts; a recommendation never changes them.

## 1. Purpose

Portfolio-sensitive advice requires a dated, internally coherent context. The minimum context separates:

- current holdings and cash;
- current market-derived values;
- investor-confirmed transactions;
- thesis status;
- human-capital concentration;
- unresolved or stale fields.

Do not treat an absent value as zero. Do not infer private facts from public market data.

The tables below are a semantic inventory for conversation, not a form the investor must fill or download.
Ask only for missing facts that materially affect the current question.

## 2. Source Hierarchy

| Fact type | Acceptable basis |
|---|---|
| Shares, cost basis, available cash, account cash flows | Investor statement or authoritative account evidence. |
| Executed transaction details | Investor confirmation or execution evidence. |
| Current price, valuation, fundamentals, exchange rate | Current dated market evidence. |
| Thesis status | Current analysis supported by evidence and the investor strategy. |
| Employer, career sector, equity vesting | Investor-supplied context only. |
| Derived allocation and profit/loss | Calculation from adequately sourced inputs. |

If sources conflict, state the conflict and request the minimum evidence needed to resolve it.

## 3. Context Metadata

Capture:

| Field | Meaning |
|---|---|
| `as_of` | Date or date-time represented by the context. |
| `base_currency` | Currency used for portfolio totals. |
| `total_invested_capital` | Investor-supplied invested-capital basis, if relevant. |
| `available_cash` | Investor-supplied deployable cash. |
| `market_value_vintage` | As-of date for prices and exchange rates. |
| `known_gaps` | Missing or stale facts that constrain analysis. |

## 4. Sleeve Summary

Use one row per sleeve:

| Field | Meaning |
|---|---|
| Sleeve | Stable, Risk, or Hedge. |
| Target | 45%, 45%, or 10% under the current strategy. |
| Current market value | Derived from sourced holdings and current prices. |
| Current percentage | Sleeve value divided by current total portfolio value. |
| Band status | Within, approaching, or outside the ±7–10 percentage-point band. |
| Limit status | Includes the Risk-sleeve 65% hard ceiling and any applicable Hedge judgment. |
| Evidence as-of | Date supporting the calculation. |

The Hedge target may rise toward 15% under an elevated-risk judgment, with Stable and Risk moving toward 42.5% each.

## 5. Holding Context

For each holding, use:

| Field | Meaning |
|---|---|
| Instrument and code | Stable identifier, market, and listing venue. |
| Sleeve | Stable, Risk, or Hedge. |
| Theme | Required for Risk holdings where a theme applies. |
| Risk tier | Compounder, Cyclical, or an explicitly explained alternative. |
| Shares | Investor-supplied static fact. |
| Cost per share | Investor-supplied static fact. |
| Current price | Current market-derived value with as-of date. |
| Market value | Shares multiplied by current price. |
| Percentage of total | Used for total-portfolio concentration. |
| Percentage of sleeve | Used for Risk-position limits. |
| Unrealized profit/loss | Derived only when the required fields are reliable. |
| Valuation context | Current valuation evidence used in recommendation analysis. |
| Thesis status | `Intact`, `Watch`, or `Broken`. |
| Thesis summary | Falsifiable investment case. |
| Kill or flip condition | Evidence that would break the thesis. |
| Source notes | Basis and date for static and market-derived fields. |

## 6. Human-Capital Context

Human capital can create correlated exposure that is invisible in a brokerage snapshot. Assess it separately:

| Field | Meaning |
|---|---|
| Assessment status | Assessed, not applicable, or missing. |
| Employer | Investor-supplied identity where relevant. |
| Career sector | Sector exposure already carried through earnings and career optionality. |
| Employer-stock exposure | Shares, cost, source, and whether exposure came from vesting or purchase. |
| Equity-vesting outlook | Approximate future correlated exposure. |
| Concentration implication | Required underweight, restriction, or evidence gap. |

Rules:

- Employer stock remains well below the normal Risk-position cap and is biased toward minimal.
- Do not recommend a new satellite theme in the career sector.
- Do not infer employer or career exposure from brokerage holdings.

## 7. Investor-Confirmed Transaction Context

When transaction history matters, capture:

| Field | Meaning |
|---|---|
| Date and time | Investor-confirmed transaction time. |
| Instrument | Name, code, and venue. |
| Sleeve | Stable, Risk, or Hedge. |
| Action | Buy, Add, Trim, or Sell. |
| Shares | Confirmed filled quantity. |
| Price | Confirmed fill price. |
| Amount and costs | Where supplied and relevant. |
| Rationale | Valuation or risk basis, condition, and thesis status at the time. |
| Post-transaction shares and cost | Investor-confirmed or reliably reconciled values. |
| Evidence | Source supporting the transaction claim. |

Conversation rules:

1. A transaction is recognized only from investor confirmation or execution evidence.
2. A difference between two holding snapshots does not reveal the actual sequence of transactions.
3. A round trip can disappear in a net holding difference; do not reconstruct it without evidence.
4. A price-only change is not a transaction.
5. A correction must identify what prior fact it corrects.

## 8. Market-Derived Versus Static Facts

Keep two update concepts distinct during analysis:

- **Market refresh:** prices, market values, percentages, unrealized profit/loss, valuation context, exchange rates, and relevant corporate-action effects may change while shares and cost basis remain fixed.
- **Authoritative holdings change:** shares, cost basis, cash, or transaction history changes only when the investor supplies adequate evidence of the underlying event.

A market refresh cannot silently absorb a trade, account cash flow, or unknown corporate action.

## 9. Consistency Checks

Where inputs permit, check:

- `shares × current price = market value`;
- sum of holding values equals the stated portfolio total;
- sleeve totals equal the sum of their holdings;
- sleeve percentages sum coherently;
- cost and profit/loss calculations use consistent currency and dates;
- Risk positions respect the approximate 15% sleeve cap and 8% total cap;
- Risk sleeve does not exceed 65%;
- employer and career-sector restrictions are assessed separately.

A failed check creates an explicit evidence request. It does not license a guessed correction.

## 10. Staleness Rules

State the relevant vintage whenever using:

- current price;
- market value;
- allocation percentage;
- valuation;
- fundamentals;
- target zone;
- policy or regulatory facts.

If static holdings and current prices have different dates, state both. If the mismatch could change the recommendation, request an updated context before concluding.

## 11. Privacy and Discussion Discipline

- Use personal financial context only to answer the current investment question.
- Do not reproduce unnecessary private detail.
- Do not treat illustrative examples as real holdings.
- Do not claim that a recommendation was accepted or acted upon.
- Do not convert an unresolved portfolio fact into a confident recommendation.
