# [TPL] ADR Spec

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical
- **Role**: Reusable content contract for Architecture Decision Records (ADRs) — structural decisions about the HDC project, its applications, or the cross-tool workspace architecture, recorded so the rationale survives the conversation that produced it
- **Source Category**: Cat 4
- **Management-System Role**: Template; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; ADR landing paths follow [OS] §9 naming convention.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §14 (preserve ambiguity rather than fabricate resolution) — ADRs record decisions with explicit context, alternatives, and reversibility, rather than presenting decisions as inevitable.
- **Relationship to [REF] Hub-CD-CC Architecture**: Referenced by §10.2 — ADRs are used to record decisions about re-enabling direct CD ↔ CC coupling. This secondary use case demonstrates ADR applicability to Meta-layer decisions as well as Cat 4 architecture decisions.
- **Relationship to [MECH] Development Track Workflow**: ADRs may be produced during any TK where the operator makes a non-trivial architecture decision; DTW §3.4 glossary may eventually reference ADRs as a standard decision-recording artifact.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §3.2.3 references this source — CC observations warranting an ADR are transferred to Hub via the CC → Hub direction, and Hub Claude assists ADR authoring per this template.
- **Relationship to [TPL] Problem Framing Memo, [TPL] Options Paper**: Adjacent decision-vehicle templates. Problem Framing Memo frames a problem; Options Paper compares options; ADR records the decision and rationale. The three are sequential in many decision flows, but each is independently usable. ADR may follow an Options Paper or stand alone.
- **Pairings I participate in**: None (post-Wave 2 Tier rationalization). The previously-considered candidate coupling (TDD §2.2.8 ADR index ↔ ADR Spec instances) classifies as Tier B per [OS] §8.5.1a — semantic-search-discoverable via the explicit `Relationship to [TPL] Technical Design Document Template` header field above (or analogous adjacent-source field). No static pairing registration required.

## How to use this source

Use this template when:
- A structural architecture decision is being made about an HDC application, the monorepo, or the cross-tool workspace
- A decision's rationale needs to survive the conversation or session that produced it
- A reversible decision is being committed in a way that future revision must reference (e.g., re-enabling direct CD ↔ CC coupling per [REF] Hub-CD-CC Architecture §10)
- A foundational design choice needs to be made discoverable to future operator self-review and to AI agents reading the canonical record

Do not use this template for:
- Day-to-day spec content (PRDs, TDDs use their own templates)
- Strategic framing of an open question ([TPL] Problem Framing Memo)
- Multi-option comparison ([TPL] Options Paper) — though an ADR may follow an Options Paper and reference its conclusions
- Documentation of past decisions whose rationale is already captured elsewhere (don't manufacture ADRs to retroactively label decisions; ADRs are forward-looking decision records)

## Scope note

ADR primary applicability is Cat 4 work — architecture decisions during Development Track execution. ADR may also be used at Meta layer for decisions about workspace architecture (e.g., re-enabling direct CD ↔ CC coupling), at Cat 1 for management-system structural decisions, or at Cat 2 for business-solution architecture decisions. The template content contract is consistent across categories; the difference is the landing path (per §3).

---

# 0. Boundary and position

## 0.1 What this source owns

- ADR content contract: the required fields, their content discipline, and the structural relationships among them
- ADR lifecycle: status transitions (Proposed → Accepted → Superseded / Deprecated) and the discipline at each transition
- ADR landing-path conventions (project-scoped, app-scoped, Meta-layer)
- ADR naming and identifier conventions
- Anti-drift red flags specific to ADR authoring and lifecycle

## 0.2 What this source does not own

- Content of any specific ADR (each ADR is its own specification artifact)
- The decision-making process leading up to an ADR (operator's judgment per [PRIN] HR Digital Decision Design Principles)
- Substantive rules being decided about (those live in their respective canonical sources)
- Index / catalog of all produced ADRs (catalog discipline is operator-managed; this template defines the artifact contract, not the catalog)
- Authoring authority for who can produce an ADR (operator, with Hub Claude assistance per [MECH] Cross-Tool Workflow Handoff)

## 0.3 Position relative to adjacent canonical sources

| Adjacent source | Relationship |
|---|---|
| [OS] | Operates within [OS] §7.1 routing; landing path follows [OS] §9 naming. |
| [PRIN] HR Digital Decision Design Principles | Decision discipline; ADRs apply §14 (preserve ambiguity, surface alternatives). |
| [REF] Hub-CD-CC Architecture | §10.2 references this source for CD ↔ CC coupling re-enablement decisions. |
| [TPL] Problem Framing Memo | Decision sequence predecessor. ADRs may follow framing memos. |
| [TPL] Options Paper | Decision sequence predecessor. ADRs may follow options papers, citing the Options Paper's conclusion. |
| [MECH] Development Track Workflow | TK execution may produce ADR-warranting decisions; DTW does not author ADRs but invokes this template. |
| [MECH] Cross-Tool Workflow Handoff | §3.2.3 references this template for ADR authoring after CC observations. |
| [MECH] Sign-Off Cleanup Policy | Applies to ADRs at sign-off; ADRs are spec artifacts subject to cleanup discipline. |

---

# 1. When to write an ADR

An ADR is warranted when **all** of the following hold:

1. The decision affects structural architecture — application architecture, monorepo organization, cross-tool workspace coupling, governance mechanism design, or similar
2. The decision is non-trivial — alternatives exist and were genuinely considered; the decision is not mechanical or pre-determined
3. The rationale matters for future reference — without an ADR, the rationale would be lost to conversation history or scattered across multiple sources
4. The decision is forward-looking — the ADR documents a decision being made now or already made recently, not a retroactive label on long-past decisions

An ADR is **not** warranted when:

- The decision is a routine TK execution choice within an established mechanism (e.g., choosing which slice to start next)
- The decision is captured authoritatively elsewhere (e.g., a TDD's §1 architecture chapter for app-level architecture)
- The decision is a value judgment without structural implications (e.g., choosing between two equivalent naming options for a feature-slug)
- The decision is fully reversible at zero cost (e.g., changing a non-binding code style preference)

When in doubt, the operator's judgment per [PRIN] §14 governs — ADRs are tools for preserving important reasoning, not bureaucratic instruments. Over-authoring ADRs dilutes the signal.

---

# 2. ADR structure

An ADR has the following content sections, in order. Required fields are marked; optional fields are marked as such.

## 2.1 Header

| Field | Required | Content |
|---|---|---|
| Title | Required | A short noun phrase naming the decision (e.g., "Re-enable direct CD ↔ CC coupling"). Not a question; not a description; not a status. |
| ADR ID | Required | `ADR-{NNNN}` where `NNNN` is a 4-digit zero-padded sequence number unique within the ADR catalog scope (project-scoped, app-scoped, or Meta — see §3). |
| Status | Required | One of: `Proposed`, `Accepted`, `Superseded by ADR-{NNNN}`, `Deprecated`. See §4 lifecycle. |
| Date | Required | Date of the most recent status transition (YYYY-MM-DD). |
| Scope | Required | One of: `Project`, `App: {app-slug}`, `Meta`. Determines the landing path per §3. |
| Decision makers | Optional | Names or roles of operator and any consultative parties (Hub Claude advisory does not need to be listed). |
| Supersedes | Optional | If this ADR replaces an earlier ADR, list the superseded ADR ID(s) here. |
| Related ADRs | Optional | ADRs that this one references or is referenced by but does not supersede. |

## 2.2 Context

**Required.**

States the situation, constraints, and forces that motivate the decision. Specifically:

- What problem or need triggered this decision
- What constraints apply (technical, organizational, scope, timing)
- What forces are in tension (e.g., "fast iteration vs long-term governance discipline")
- What is currently the case before the decision (the "as-is" state)
- What changed recently that made this decision relevant now (if applicable)

Length guidance: 2–6 paragraphs. Long enough that the reader (future operator, AI agent) understands the problem without consulting external sources; short enough that the reader can absorb in 1–2 minutes.

The Context should be honest about uncertainty — per [PRIN] §14, fabricated resolution of ambiguity is anti-drift. If a load-bearing input is uncertain, state the uncertainty.

## 2.3 Alternatives considered

**Required if alternatives exist; optional if the decision was binary (do / don't).**

Lists 2–4 alternatives that were genuinely considered. For each:

- Name (a short label for the alternative)
- Description (1–3 sentences)
- Strengths (why this alternative is attractive)
- Weaknesses (why this alternative is not the chosen decision)

The chosen decision is also listed here, with the same structure. This makes the comparison explicit.

When the decision is binary (do / don't), Alternatives considered may be omitted, but Context should make the binary nature explicit.

## 2.4 Decision

**Required.**

States the decision concisely. Specifically:

- What is being decided (one or two sentences)
- The chosen alternative from §2.3, if applicable
- Any conditions or qualifiers (e.g., "only for apps deployed after 2026-09-01")

The Decision section is short — typically 1–3 sentences. Detailed rationale belongs in Context (why the decision is needed) and Consequences (what the decision implies).

## 2.5 Consequences

**Required.**

Records the implications of the decision. Specifically:

- **Positive consequences**: What improves, what becomes possible
- **Negative consequences**: What is sacrificed, what becomes harder
- **Neutral consequences**: What changes without clearly being better or worse
- **Open questions** (optional): What the decision does not resolve and may need further work

Length guidance: 3–8 bullet points across the three (or four) categories. Honesty about negative consequences is essential — an ADR that only lists positives signals incomplete thinking.

## 2.6 Reversibility

**Required.**

States how the decision can be reversed if it proves wrong. Specifically:

- The reversal cost (low / medium / high — operator's judgment)
- The reversal mechanism (e.g., "supersede this ADR with a new one; revert §X.Y of [REF] Source Z")
- Any irreversible side effects (e.g., "data already migrated under this decision cannot be unmigrated trivially")
- The trigger conditions that would prompt reversal (e.g., "if the verification exercise per §10 produces audit failures")

Decisions with no reversibility section should be very rare and should explicitly call out the irreversibility.

## 2.7 Verification (optional)

If the decision implies a future verification activity (e.g., empirical verification before broader rollout, an audit at a specific milestone), this section describes the verification mechanism. Includes:

- Verification trigger condition
- Verification activity (what is verified)
- Acceptance criteria
- Failure routing (what happens if verification fails)

---

# 3. Landing path

ADRs land at canonical paths in the monorepo, scoped by their decision scope.

## 3.1 Project-scoped ADRs

**Path**: `specs/adrs/ADR-{NNNN}-{kebab-case-title-slug}.md`

For decisions affecting the project as a whole: monorepo organization, project-level conventions, cross-app concerns, or decisions whose scope is not naturally tied to a specific app.

## 3.2 App-scoped ADRs

**Path**: `apps/{app-slug}/specs/adrs/ADR-{NNNN}-{kebab-case-title-slug}.md`

For decisions affecting a single application: app-internal architecture, app-specific design choices, app-internal mechanism design.

ADR ID sequence is app-internal (each app maintains its own `ADR-0001`, `ADR-0002`, ... sequence).

## 3.3 Meta-layer ADRs

**Path**: `specs/meta-adrs/ADR-{NNNN}-{kebab-case-title-slug}.md`

For decisions affecting the cross-tool workspace architecture, the canonical governance system, or other Meta-layer concerns documented in [OS] §2.3.2 meta-layer sources.

ADR ID sequence is Meta-internal, separate from project-scoped ADR sequence.

## 3.4 Cross-scope references

When an ADR references another ADR in a different scope (e.g., a project-scoped ADR references a Meta-layer ADR), the reference uses the full path or the qualified ID (e.g., `Meta-ADR-0003`). When all referenced ADRs are within the same scope, the unqualified ID (`ADR-0003`) suffices.

---

# 4. ADR lifecycle and status transitions

## 4.1 Status values

| Status | Meaning | Allowed next states |
|---|---|---|
| `Proposed` | Decision is drafted but not yet committed; operator review pending | `Accepted`, `Withdrawn` (rare; not formally tracked) |
| `Accepted` | Decision is committed; the ADR is canonical-record | `Superseded by ADR-{NNNN}`, `Deprecated` |
| `Superseded by ADR-{NNNN}` | A later ADR replaces this one; the superseding ADR's ID is recorded | Terminal (cannot be further transitioned; if re-instated, a new ADR is created) |
| `Deprecated` | The decision no longer applies, but no superseding ADR was authored | Terminal |

## 4.2 Status transition discipline

**Proposed → Accepted**: Operator signs off the ADR content; status changes to Accepted; Date updates.

**Accepted → Superseded**: A new ADR is authored that supersedes this one. Both ADRs are updated in the same revision:
- The new ADR's `Supersedes` field includes the old ADR ID
- The old ADR's `Status` becomes `Superseded by ADR-{new-NNNN}` and `Date` updates

The old ADR's content (Context, Alternatives, Decision, Consequences, Reversibility) is **not** modified — superseding preserves the historical record. Only the Status field changes.

**Accepted → Deprecated**: When a decision becomes irrelevant (e.g., the scope it addressed no longer exists) and no successor decision was needed, the ADR is marked `Deprecated`. Date updates. The ADR is not deleted.

## 4.3 Content immutability after Accepted

Once an ADR reaches `Accepted` status, its content (sections §2.2 through §2.6 / §2.7) is immutable. Subsequent decisions on the same topic produce a new ADR that supersedes the old one.

Exception: typo corrections and formatting fixes that do not alter substantive content may be applied to Accepted ADRs without superseding. Such corrections are recorded in git history.

## 4.4 Withdrawal of Proposed ADRs

A Proposed ADR that is not progressed to Accepted may be withdrawn:
- The file may be deleted (no canonical-record obligation since it never became Accepted)
- Or the file may be kept with `Status: Withdrawn` for the record (operator's choice)

Withdrawal is informal; there is no required ceremony.

---

# 5. Update discipline

ADRs are governed by [MECH] Sign-Off Cleanup Policy when accepted. Specifically:

- Proposed ADRs may have in-line revision annotations during the proposal-to-Accepted authoring period
- Accepted ADRs apply Sign-Off Cleanup Policy: in-line annotations are removed; the artifact is brought to clean form
- Superseded / Deprecated ADRs retain their Accepted-state content (immutability per §4.3); the Status field update does not trigger Sign-Off Cleanup

Cross-canonical reference discipline: when an ADR is Accepted and other canonical sources should reference it (e.g., a decision documented in an ADR is implemented via a revision of [REF] Hub-CD-CC Architecture §9.4), the canonical source's `Relationship to ...` field or body content includes the ADR reference in the same revision per [OS] §8.5.2 paired-update discipline.

---

# 6. Anti-drift red flags

> **Scope**: this section enumerates **ADR-specific** anti-drift red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced rather than duplicated.

**Authoring dimension**:
- ADR authored for a decision that does not meet §1 warrant criteria (over-authoring; dilutes signal)
- ADR authored as retroactive label for a long-past decision (per §1, ADRs are forward-looking)
- ADR omitting required fields per §2 (Title / ADR ID / Status / Date / Scope / Context / Decision / Consequences / Reversibility)
- ADR Decision section longer than 5 sentences (Decision should be concise; detailed rationale belongs in Context / Consequences)
- ADR Consequences section listing only positives (signals incomplete thinking; negatives and tradeoffs should be honest)

**Structure dimension**:
- ADR ID not following `ADR-{NNNN}` four-digit format
- ADR Scope field inconsistent with the file's landing path per §3
- Alternatives considered section claiming binary decision when 3+ alternatives could have been considered

**Lifecycle dimension**:
- Accepted ADR's Context / Decision / Consequences content modified after Acceptance (violates §4.3 immutability)
- ADR transitioning from Superseded back to Accepted (per §4.1, Superseded is terminal)
- Multiple Accepted ADRs simultaneously governing the same decision scope without explicit supersession relationship

**Landing path dimension**:
- App-scoped ADR landing at project-scoped path (e.g., a decision about app-X architecture in `specs/adrs/` instead of `apps/app-x/specs/adrs/`)
- ADR ID sequence collision (two ADRs with the same `ADR-{NNNN}` within the same scope's sequence)
- Meta-layer ADR landing at project-scoped path (per §3.3, Meta-layer ADRs have their own path)

**Reference dimension**:
- Canonical source references an ADR that does not exist
- Canonical source references a Superseded ADR for current-state behavior (should reference the superseding ADR instead)
- ADR references another canonical source without the cited source updating to reference back (when paired-update applies per [OS] §8.5.2)

**Decision quality dimension** (per [PRIN] §14):
- ADR Context section fabricating resolution to genuinely ambiguous input (per [PRIN] §14, ambiguity should be preserved and named, not resolved by fabrication)
- ADR Consequences section omitting open questions when the decision genuinely leaves open questions
- ADR Reversibility section claiming "irreversible" when reversibility is merely costly (the operator's judgment governs; intentional rare claim is fine, but should be deliberate)
