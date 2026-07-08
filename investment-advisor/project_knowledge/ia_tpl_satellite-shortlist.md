# Satellite Shortlist — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's Satellite Shortlist — the persisted output of the §5 selection funnel: the finalists that survived §5.3, with the comparative rationale for why *these* names and not the alternatives.** Carries zero real data — only field definitions and one illustrative (generic) example. Like the other runtime files, the filled instance is kept private, outside this public repo; only this blank schema belongs here.

**Language note.** This template is canonical control text → English. A **filled instance** is read by the investor to review convictions and may be written in the investor's working language (e.g. Chinese) when that aids judgment; keep instrument codes, §-references, thesis-status verbs, and field names intact for auditability against this schema.

## Why this file exists — the selection layer

The framework's §10 runtime contract defines three **money-state** artifacts — Portfolio State (what I hold), Transaction Log (what I have done), Action Plan (what the advisor proposes) — under a single-directional flow. All three answer *money-movement* questions. None persists the **selection decision** that precedes any money movement: the §5 funnel (macro → sub-industry → company) yields a basket of finalists, but no artifact records *why this basket* — which candidates were considered, which survived §5.3, which were cut and for what reason.

This file is that record. It sits in a **selection layer** upstream of the runtime trio:

```
§5 funnel → Longlist (candidate universe / theme) → [§5.3 filter] → Shortlist (THIS FILE: finalists + rationale + cut log) → Action Plan (§6.7 price zones + timing) → execute → Transaction Log → Portfolio State
```

It is the standing record of *conviction* — a different axis from the record of *holdings* (State), *history* (Log), or *proposed trades* (Action Plan). Those three move on the money axis; this one moves on the decision-provenance axis. Do not fold it into the trio.

## What this file is — and is not

**It is** the persisted output of §5.3 company selection: the reference the **quarterly thesis review (§7)** re-validates against, and the ledger against which **held-name neutrality (§5.3)** re-tests every name — held and new alike — on identical criteria.

**It is not:**

- **Not a money-state artifact.** It records no holdings, cost basis, capital, or fills, and it never mutates State/Log. Framework Invariant 9 (advice materializes only in the Action Plan; holdings change only via execute → log → re-snapshot) is untouched — a conviction here is not a position and not a trade.
- **Not an Action Plan.** It carries **no price zones, no §6.7 timing, no execution windows.** Selection answers *which names, and why*; execution answers *when / how / at what price*. A finalist here becomes actionable only when it independently enters a valuation-justified zone, at which point the **Action Plan** adds the §6.7 timing. This price-zone exclusion is a hard interface boundary, not a stylistic preference — it keeps Invariant 2 intact (selection ≠ valuation trigger ≠ execution timing). If a target price band appears in this file, it is misfiled.
- **Not the Longlist.** It does not re-list the full candidate universe; it references the longlist version it selected from and records only the finalists plus the cut rationale.

## Relationship to the framework

- **§5.3 output.** The 2–3-name basket per theme, its selection scorecard, and the intra-/cross-theme exclusion (de-correlation) rules are this file's core payload.
- **§7 input.** Each finalist carries a **thesis status** (Intact / Watch / Broken); the quarterly review updates it *here*. A status flipping to **Broken** is the §6.6 exit trigger — actioned via an Action Plan **Sell**, never by editing this file into a trade.
- **§5.3 held-name neutrality.** Existing holdings appear as finalists scored on the *same* criteria as fresh candidates. "Already owned" is not a field. A held name that no longer earns its slot moves to the cut log with a stated reason — this is where endowment bias is caught.
- **§9.2 / §9.4 as outputs.** Per-name sizing *intent* (≥ ~2–3%, ≤ ~15% of the risk sleeve) and the basket's A/H venue mix are recorded as **outputs of selection**, never as pre-filters (§9.4 forbids a venue quota reaching into satellite selection). Actual sizes are set at execution (Action Plan → Log), not here.

## Schema — one block per theme

### Theme identity

- **Theme (主题):** name (e.g., "AI / 数字经济").
- **Macro anchor (§5.1):** the 十五五 priority and/or 风向 this theme rides.
- **Sub-industry node (§5.2):** the chosen up-/down-stream node, and why it is the best risk/reward point on the penetration S-curve (early-to-mid, structure forming-not-closed).
- **Moat-formation mechanism (§5.2):** scale / network / tech-IP / switching-cost / licence — which one, and the evidence it is actually forming (not a story).
- **Deliberate exclusion rules (de-correlation):** what is *ruled out* of this theme to prevent hidden concentration (e.g., "exclude compute/chip layer to de-correlate from the semiconductor theme"; "exclude whole-machine integrators to avoid overlap with the AI theme"). These guards are what keep the baskets genuinely independent bets rather than one factor in disguise.
- **Target count:** 2–3 names (§5.3 / §9).
- **Source longlist (依据):** the longlist version/date this shortlist selected from — the provenance link.

### Finalists — one row + detail block per name

The finalists *are* the shortlist. For each, capture the §5.3 case at a specificity that lets a future §7 review **re-test the claim**, not merely read a grade:

- **Instrument (标的):** name + code; **venue** (A股 主板 / 创业板 / 科创板 · 港股) + board.
- **§5.3 selection scorecard** — the five criteria:
  - R&D intensity + credibility of the innovation pipeline.
  - Market-share **trajectory** (gaining, not merely large).
  - Moat-formation **evidence** (forming, verifiable).
  - Management / governance — scuttlebutt basis (channel checks, customers, suppliers, ecosystem), Fisher-style, not just financials.
  - **Valuation-ceiling** sanity check — the growth-adjusted level above which even this name is a bad buy. A ceiling (a "do-not-pay-above" judgment), *not* a timing zone.
- **Thesis (one line):** the future-leader claim, in falsifiable form.
- **Thesis status:** Intact / Watch / Broken (maintained at §7).
- **Kill / flip condition:** the single condition that would break the thesis (→ §6.6 exit). Per name.
- **Basket role:** why this name is differentiated from the other 1–2 finalists (intra-basket de-correlation — different sub-segment, different demand driver).

### Cut log (considered → excluded)

Each candidate that was in the longlist but did **not** make the basket, with the reason keyed to a §5.3 criterion or a de-correlation / venue / valuation ground. This is precisely what the Longlist → Action Plan jump discards: the record of *why not*. Keeping it lets a later re-selection reconsider a cut name knowingly instead of re-deriving from scratch, and it makes the whole selection auditable (and falsifiable) after the fact.

### Basket-level checks

- **Intra-basket de-correlation:** confirm the 2–3 names are not the same bet wearing different tickers.
- **Sizing intent (§9.2):** each ≥ ~2–3% and ≤ ~15% of the risk sleeve — *intent only*, resolved at execution.
- **Venue mix (§9.4):** the basket's A/H split recorded as an **output**, with the venue diagnostic noted (which China tail it leans into) — never a quota.
- **Open selections:** slots not yet filled (a theme with no names chosen yet), and pending decisions ("X vs Y vs both") each tagged with the criterion that will resolve them.

## Illustrative example (generic — replace in the private filled copy)

> **Theme — 示例主题 / Example-Theme**
> - Macro anchor: 十五五 "示例优先级"; 风向 supportive.
> - Sub-industry node: 示例细分 (up-stream picks-and-shovels layer); early-to-mid S-curve, structure not yet closed.
> - Moat mechanism: tech-IP + switching costs; evidence = 示例.
> - Exclusion rules: exclude 示例相邻层 to de-correlate from Example-Theme-2.
> - Target count: 2–3. Source longlist: `satellite-longlist_YYYY-MM-DD.md`.
>
> **Finalist A — 示例成长股A (68xxxx, 科创板 / A)**
> - Scorecard: R&D ~示例%; share trajectory gaining (示例); moat forming (示例); governance clean per scuttlebutt (示例); valuation ceiling ≈ 示例 (growth-adjusted).
> - Thesis: "示例 future leader of 细分." Status: Intact. Kill condition: moat metric 示例 reverses two quarters running.
> - Basket role: covers 示例 sub-segment (vs Finalist B's different driver).
>
> **Cut log:** 示例候选X — excluded: same sub-segment as Finalist A (intra-basket correlation). 示例候选Y — excluded: fails valuation-ceiling test at current level.
>
> **Basket checks:** de-correlation OK; sizing intent A ~示例%, B ~示例%; venue mix 2A/0H (output); open: none.

_The block above is illustrative and generic; the filled private copy replaces it with real themes, names, and conviction calls._

## Lifecycle rules

1. **Selection layer, not money-state.** This file feeds the Action Plan; it never edits State/Log (Invariant 9 intact). A finalist is a *conviction*, not a position.
2. **No execution content (hard boundary).** No price zones, no §6.7 timing, no windows — those materialize only in the Action Plan when a name enters a valuation-justified zone. A price band appearing here is a schema violation.
3. **New candidates enter via the Longlist first.** Nothing is shortlisted that was not first in the candidate universe — this preserves the search-completeness the longlist exists to guarantee.
4. **Refreshed, not append-only.** Updated at each selection event and at the §7 quarterly review (thesis-status refresh). Unlike the append-only Transaction Log (a record of *fact*), this is a living record of *current conviction* — closer to Portfolio State's "refreshed wholesale," but for convictions rather than holdings. Retain prior versions for audit (git history or dated private copies).
5. **Held-name neutrality is enforced here.** Every name — held or new — is scored on the §5.3 criteria in this file. "Already owned" is never a scorecard input; a held name that fails re-earning moves to the cut log.
6. **No personal data in the public repo.** The filled shortlist (real names, conviction calls, sizing intent) is private; only this blank schema is committed.
