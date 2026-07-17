# Investment Recommendation Contract

> **Status:** transformed chat-project replica; not SOT.
> **Authoritative source(s):** `3_projects/investment-advisor/canonical/templates/action-plan.md`; `2_topics/investment-advising/methodology.md`; `2_topics/investment-advising/technical-analysis.md`; `3_projects/investment-advisor/canonical/investor-strategy.md`.
> **Conversation boundary:** This document defines how a recommendation is expressed for investor consideration. It never treats a recommendation as an order, an investor decision, an executed transaction, or a change in holdings.

## 1. Purpose

A recommendation must turn analysis into a clear, bounded decision proposal while preserving the distinction between:

- what is known;
- what is inferred;
- what is proposed;
- what would invalidate the proposal;
- what the investor has actually confirmed.

The recommendation should be specific enough to support a decision without pretending to predict the market.

## 2. Action Vocabulary

| Action | Meaning |
|---|---|
| Buy | Establish an initial value-supported position. |
| Add | Increase an existing position while the thesis remains intact. |
| Trim | Reduce part of a position while retaining the thesis. |
| Sell | Remove a position because of a broken thesis, strategic exclusion, or another explicit full-exit rationale. |
| Hold | Preserve the current position because no change is adequately supported. |
| Swap | Pair a reduction and an addition; each leg needs its own rationale and price condition. |
| Rebalance | Move sleeve exposure toward the committed Stable / Risk / Hedge architecture. |
| No action | Evidence is insufficient, conditions are not met, or current positioning remains preferable. |

Routine Buy, Add, and Trim proposals use approximately one-third tranches. A full Sell requires an explicit full-exit rationale.

## 3. Required Recommendation Content

Every Buy, Add, Trim, Sell, Swap, or Rebalance recommendation includes:

| Field | Required content |
|---|---|
| As-of | Date of portfolio and market evidence. |
| Instrument or sleeve | Name, code, venue, and affected sleeve where applicable. |
| Proposed action | One action from the vocabulary above. |
| Thesis status | `Intact`, `Watch`, or `Broken` for thesis-driven instruments. |
| Primary basis | Valuation, concentration, rebalance, broken thesis, hedge need, or another strategy-grounded reason. |
| Evidence | Current sources and dates supporting the primary basis. |
| Rival explanation | Strongest plausible reason the interpretation or action may be wrong. |
| Size logic | Proposed tranche or exposure change, checked against project limits. |
| Funding source | Cash, sale proceeds, cycle cash, or another strategy-permitted source. |
| Sleeve effect | Expected change in Stable, Risk, and Hedge exposure. |
| Condition | What must be true before the investor considers acting. |
| Price zone | Lower–upper act-if-reached band where required. |
| Time point | Open, Intraday, Close, or a reason the field is not applicable. |
| Voids when | Conditions that invalidate the recommendation or zone. |
| Flip or kill condition | Evidence that would reverse the underlying thesis judgment. |
| Uncertainty | Limits of evidence, stale inputs, and unresolved questions. |

A `Hold` or `No action` recommendation must still state thesis, valuation or risk basis, and what evidence would change the conclusion.

These are semantic requirements, not mandatory visible fields. Integrate them into natural prose when
separate labels would add ceremony without clarity.

## 4. Decision Order

Apply this sequence:

1. Confirm portfolio context and its as-of date.
2. Confirm the strategy mandate and applicable limits.
3. Judge the thesis.
4. Judge valuation or other primary risk basis.
5. Present the strongest rival interpretation.
6. Determine whether any action is justified.
7. Apply size, funding, sleeve, and human-capital constraints.
8. Derive a target zone only when current evidence supports one.
9. State the condition and invalidation.
10. Clearly label the result as a recommendation for investor consideration.

Technical analysis never moves ahead of thesis and valuation.

## 5. Target-Zone Requirement

Buy, Add, Trim, and Sell recommendations normally require a target zone:

- lower and upper edges;
- current data source and as-of date;
- timeframe;
- trend and support/resistance rationale;
- participation invalidation;
- instrument-specific premium, discount, or fair-value check where relevant;
- act-if-reached language;
- no-chase language when the zone is not reached.

If the evidence cannot support a defensible zone, state the missing input. Do not defer the analytical work to the investor while still presenting the action as ready.

## 6. Recommendation Postures

Use one posture:

| Posture | Meaning |
|---|---|
| `Consider now` | Thesis, primary basis, limits, and current price condition are all satisfied. |
| `Conditional` | Thesis and primary basis support the action, but the stated price or evidence condition is not yet satisfied. |
| `Watch` | A material issue is unresolved; name the evidence that would promote or reject the idea. |
| `Hold` | Current position remains preferred; name the change condition. |
| `No action` | No proposed change is justified. |

`Conditional` never means the future path is predicted. It means the investor should reconsider only if the stated condition becomes true.

## 7. Special Rationale Cases

### 7.1 Broken Thesis

When the thesis is `Broken`:

- Buy/Add is excluded;
- chip accumulation is no longer a valid rationale;
- the primary question is reduction or exit;
- technical placement may reduce avoidable price damage but cannot veto the thesis conclusion.

### 7.2 Human-Capital De-Concentration

For employer-stock or career-sector concentration:

- the primary basis is correlation and total economic exposure, not necessarily high valuation;
- employer stock remains well below the ordinary Risk-position cap;
- no new satellite theme is added in the career sector;
- proceeds move toward less-correlated exposure;
- expected vesting is considered.

### 7.3 Sleeve Rebalance

For a sleeve-level rebalance:

- identify the breached band or ceiling;
- show current versus target exposure;
- describe each component leg;
- explain the risk-control benefit and opportunity cost;
- preserve the Hedge sleeve's insurance purpose.

### 7.4 Swap

A Swap contains two independent proposals:

- reduction leg;
- addition leg.

Each leg needs its own primary basis, price condition, size, and invalidation. Sale proceeds alone do not justify the addition leg.

## 8. Partial-Action Discipline

For a multi-tranche proposal:

- state the total intended change;
- state the current tranche;
- state what must be re-evaluated before another tranche;
- do not assume that one investor-confirmed transaction implies acceptance of the remaining tranches;
- void the remaining proposal if its thesis, valuation, funding, limit, or price condition changes materially.

## 9. Proposal Versus Investor-Confirmed Fact

The conversation must preserve these rules:

1. A recommendation does not prove investor acceptance.
2. Investor acceptance does not prove a transaction occurred.
3. A transaction is treated as fact only when the investor confirms it or supplies evidence.
4. A partially completed idea does not imply completion of the remainder.
5. Portfolio context changes only when the investor supplies adequate updated facts.
6. Never describe a proposal using language that implies it already happened.

## 10. Inline Recommendation Pattern

Adapt visible structure to decision complexity:

- **Simple judgment:** state the recommendation, primary basis, strongest rival or uncertainty, and what
  would change the conclusion.
- **Action proposal:** also state thesis status, size and funding logic, sleeve and human-capital effect,
  action condition, current target-zone evidence where required, void condition, and flip or kill condition.
- **Multi-instrument or portfolio comparison:** use a compact table only when repeated fields are materially
  easier to compare; keep rationale and recommendation in prose.

Do not omit load-bearing content merely to make the response shorter, but do not expose every semantic field
as a heading when the answer is simple.

Recommendations remain inline by default. Do not create or proactively offer a downloadable file,
attachment, export, formal report, or download link unless the investor explicitly requests one. A complex
or potentially shareable analysis does not itself imply a file request.

## 11. Hard Checks

Before presenting a recommendation, confirm:

- current portfolio context is adequate for the decision;
- thesis and valuation or risk basis precede technical timing;
- Buy/Add is blocked for a `Broken` thesis;
- size and funding respect sleeve and position limits;
- Hedge funding respects its insurance purpose;
- human-capital concentration is assessed where relevant;
- the target zone is a band with source and date, not a forecast;
- the strongest rival and invalidation are explicit;
- no unknown transaction or holding fact is presented as known;
- the wording does not imply that the investor acted.

## 12. Deliberate Exclusions

- Bare Buy or Sell calls.
- A menu of actions without a recommendation.
- A recommendation without a flip or void condition.
- A target zone without current evidence.
- Technical timing as the primary reason for action.
- All-in or all-out language without a valid full-exit rationale.
- Use of leverage or unauthorized derivative complexity.
- Any claim that the recommendation itself changed the portfolio.
