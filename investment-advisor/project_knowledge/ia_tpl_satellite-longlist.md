# Satellite Longlist — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's Satellite Longlist — the recorded candidate universe of the §5 selection funnel: every name considered per theme, plus the coarse first-pass screen that narrows the universe before §5.3 fine-selection runs in the Shortlist.** Carries zero real data — only field definitions and one illustrative (generic) example. Like the other runtime files, the filled instance is kept private, outside this public repo; only this blank schema belongs here.

**Language note.** This template is canonical control text → English. A **filled instance** is read by the investor while searching for candidates and may be written in the investor's working language (e.g. Chinese) when that aids judgment; keep instrument codes, §-references, screen-verdict verbs, and field names intact for auditability against this schema.

## Why this file exists — the search-completeness layer

The §5 funnel (macro → sub-industry → company) does not begin at a basket of finalists; it begins at a **wide search**. The Shortlist records *which finalists, and why*; it does **not** record the universe those finalists were drawn *from* — the candidates considered and coarse-screened out before §5.3 ever ran. Without that record, the selection cannot be audited for **search completeness**: the standing risk that the winner was chosen from too narrow a field (the mirror image of the survivorship bias §5.3 already guards against).

This file is that record. It sits at the **top of the selection layer**, upstream of the Shortlist:

```
§5 funnel → Longlist (THIS FILE: candidate universe + coarse screen) → [§5.3 filter] → Shortlist (finalists + scorecard + cut log) → Action Plan (§6.7 zones + timing) → execute → Transaction Log → Portfolio State
```

Its two jobs — and only these two:

1. **Search completeness.** Record the candidate universe per theme *wide enough* that a later reviewer can see the field was not prematurely narrowed. This is the artifact that makes "did we look widely enough?" an answerable question rather than an act of faith.
2. **Coarse first-pass screen.** A cheap, wide filter — Keep / Watch / Drop — on readily-available signals (coarse valuation, growth, leadership/structure), narrowing the universe to a **Keep-set** that the Shortlist's §5.3 filter then fine-selects.

It is the standing record of the *search* — a different axis from *conviction* (Shortlist), *holdings* (State), *history* (Log), or *proposed trades* (Action Plan). Those move on the money / decision-provenance axes; this one records the breadth of the hunt.

## What this file is — and is not

**It is** the persisted candidate universe + coarse screen: the reference the Shortlist selects *from* (Shortlist lifecycle rule 3 — nothing is shortlisted that was not first a longlist candidate), and the **entry point** where any new candidate joins the funnel.

**It is not:**

- **Not the Shortlist.** It carries no §5.3 selection scorecard, no per-name kill/flip conviction, no basket de-correlation finalization, no thesis-status. Those are the Shortlist's payload. The longlist **coarse-screens**; the Shortlist **fine-selects**. A longlist "Keep" is a *candidate cleared to the next round* — **not** a finalist and **not** a conviction. Keeping the two layers distinct is what stops the longlist from silently becoming a shortlist that skipped the §5.3 discipline.
- **Not a money-state artifact.** It records no holdings, cost basis, capital, or fills, and it never mutates State/Log. Invariant 9 is untouched — a candidate here is not a position and not a trade.
- **Not an Action Plan.** It carries **no price zones, no §6.7 timing, no execution windows.** The coarse valuation read here answers *"is this segment/name in an expensive or a cheap target domain?"* (§6.2 valuation-first framing) — never *"buy at ¥X."* A target entry/exit band appearing in this file is misfiled; producing one is the Action Plan's job, two layers downstream.

## Relationship to the framework

- **§5.1 / §5.2 / §5.3 traversal, recorded.** The longlist is where the top-down funnel is actually worked and written down: macro theme (§5.1) → sub-industry node, including nodes deliberately excluded for de-correlation (§5.2) → candidate companies (the universe §5.3 will later fine-filter).
- **§6.2 valuation-first, coarse.** Records a coarse valuation read as *target-domain* framing — whether the whole segment is expensive or cheap, and whether this longlist is a "buy-now" or a "watch-for-pullback" domain — never a timing zone.
- **§9 sizing anchor, as a bound.** Records the sleeve sizing anchor and name-count ceiling that **bound** how many candidates can survive to the Shortlist and eventual sizing. This shapes how aggressively to coarse-screen; it is not itself a sizing decision (sizes are set at execution, via the Action Plan → Log).
- **Hand-off to §5.3.** The coarse-screen **Keep-set is the input universe** to the Shortlist's §5.3 filter. Watch/Drop verdicts are retained *with reasons*, so the Shortlist's cut log and any later re-search inherit the rationale instead of re-deriving it from scratch.

## Schema — sizing anchor + one block per theme

### Global header (once)

- **Longlist date + data vintage.** When compiled; the source and as-of of the coarse market data used. Coarse valuation/growth are version-specific — vintage them; they are not evergreen.
- **Sizing anchor (§9).** Sleeve target capital, name-count ceiling, per-name floor/cap — as *bounding context* for how many candidates should survive, not a sizing decision.
- **Standing screening lenses (§5.2 / §5.3 refinements).** The heuristics applied to coarse-screen this universe, stated so every Keep/Watch/Drop verdict is auditable against a named lens rather than taste. *(Heuristic slot — record whichever lenses the investor is using, e.g. a leadership-clarity rule, or a growth-adjusted-valuation rule. A lens durable enough to outlive one longlist is a candidate for promotion into the framework proper; until promoted, it lives here as the applied rationale.)*
- **Scope exclusions.** Any theme/sector ruled out a priori and why (e.g. a career-sector exclusion per §9.3), so the search boundary is explicit.

### Theme block (one per theme)

- **Theme + macro anchor (§5.1).** The theme, and the 十五五 / 风向 priority it rides.
- **Sub-industry map (§5.2).** The up-/down-stream nodes considered, and which were chosen as the best risk/reward point on the penetration S-curve (early-to-mid, structure forming-not-closed) — **including the nodes deliberately excluded** (de-correlation / avoid-wrong-structure), so the search boundary within the theme is explicit.
- **Candidate universe table (the core payload)** — one row per candidate considered:
  - **Instrument.** Name + code; **sub-segment**; **venue** (A股 主板/创业板/科创板 · 港股) + board.
  - **Coarse valuation read.** e.g. PE / PEG band + market-cap tier — *target-domain framing, data-vintaged*; **not** an entry zone.
  - **Growth read.** Revenue/earnings trajectory, coarse (gaining / flat / declining).
  - **Leadership & structure read.** Clear leader vs. contested; the §5.2 "structure forming-not-closed" signal and any leadership-clarity call.
  - **Coarse-screen verdict.** **Keep / Watch / Drop**, each with a one-line reason keyed to a §5.x ground (trajectory, valuation-domain, leadership/structure, de-correlation, venue). *(These verbs are the longlist's screen vocabulary — distinct from the Shortlist's Intact / Watch / Broken thesis-status verbs. Do not conflate: a longlist "Watch" means "not yet cleared/cut, revisit"; a Shortlist "Watch" is a §7 thesis judgment on a chosen name.)*
- **Coverage note (search completeness).** Sub-segments or named-but-not-yet-pulled candidates known to exist but not yet worked — the *explicit* record of the search's current edge, so a gap is a documented decision rather than a silent omission.

### Hand-off (once)

- **Keep-set → Shortlist input universe.** The candidates that clear the coarse screen into §5.3.
- **Open decisions carried to fine-screen.** Which sub-segment; single-name vs. basket; count against the ceiling — each tagged with the criterion that will resolve it in the Shortlist.

## Illustrative example (generic — replace in the private filled copy)

> **Global header**
> - Longlist date: YYYY-MM-DD. Data vintage: coarse quotes/fundamentals as-of YYYY-MM-DD (source).
> - Sizing anchor (§9): risk sleeve ≈ 示例 capital; ≤ 示例 names; per-name ≤ ~15% sleeve, floor ~2–3%.
> - Standing lenses: 示例 leadership-clarity rule (clear leader → single name; contested → 2–3 basket); 示例 growth-adjusted-valuation rule.
> - Scope exclusions: exclude 示例 sector (career-concentration, §9.3).
>
> **Theme — 示例主题 / Example-Theme**
> - Macro anchor (§5.1): 十五五 "示例优先级"; 风向 supportive.
> - Sub-industry map (§5.2): consider 示例上游 / 示例下游; choose 示例节点 (early-to-mid S-curve, structure not closed); **exclude** 示例相邻层 (de-correlate from Example-Theme-2).
>
> | Instrument | Sub-segment | Venue | Coarse valuation | Growth | Leadership/structure | Screen |
> |---|---|---|---|---|---|---|
> | 示例A (68xxxx) | 示例段 | 科创板/A | PE 示例 / PEG 示例 | +示例% | clear leader | ✅ Keep |
> | 示例B (00xxxx) | 示例段 | 深主板/A | PE 示例 | −示例% | contested | 🔻 Drop — trajectory (§5.3) |
>
> - Coverage note: 示例子段 candidates not yet pulled — expand if fine-screen needs.
>
> **Hand-off**
> - Keep-set → Shortlist: 示例A (+ others).
> - Open decisions: 示例段 single vs. basket — resolves on leadership-clarity at fine-screen.

_The blocks above are illustrative and generic; the filled private copy replaces them with real themes, candidates, and coarse verdicts._

## Lifecycle rules

1. **Search-completeness layer, not money-state.** This file feeds the Shortlist; it never edits State/Log (Invariant 9 intact). A candidate is a *search entry*, not a position.
2. **No execution content (hard boundary).** No price zones, no §6.7 timing, no windows. Coarse valuation is target-domain framing (§6.2) only; a target price band here is a schema violation.
3. **The entry point for new candidates.** New names join the funnel **here first** — nothing reaches the Shortlist that was not first a longlist candidate. This is the rule that makes the whole selection auditable for search completeness.
4. **Coarse screen ≠ fine selection.** Keep / Watch / Drop is a wide first-pass filter on cheap signals; §5.3 conviction, scorecards, and kill/flip conditions belong to the Shortlist. Keep the longlist cheap and wide on purpose — its value is *coverage*, not depth.
5. **Refreshed at each search event + the §7 quarterly discovery pass.** Updated when a new theme/candidate is worked, and at the quarterly review's discovery step. Unlike the append-only Transaction Log, this is a living record of the *current search*; retain prior versions for audit (git history or dated private copies).
6. **No personal data in the public repo.** The filled longlist (real candidates, coarse verdicts, sizing anchor) is private; only this blank schema is committed.
