# [MECH] Sign-Off Cleanup Policy

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable governance mechanism for multi-round-revised long-living spec artifact terminal-state cleanup, defining the trigger conditions for sign-off entry, the Why Anchor (WA) plus four-question decision tree governing keep-vs-delete during cleanup, the adjudication procedure for the in-place cleanup operation, per-artifact specifics for PRD and TDD expressed as content-category + example-pattern semantic rules (with A3, A4, A5, A7 placeholder pending empirical evidence), and exception handling for A6 openapi.yaml + B1-B3 Hub-produced slice interface artifacts + C1-C3 CC-produced code/test/evidence
- **Source Category**: Cat 4
- **Management-System Role**: Outside L1-L5 hierarchy; governance mechanism running sign-off cleanup on long-living spec artifacts (PRD / TDD) to prepare them for Development Track downstream-task consumption; operates across the Cat 2 PRD and Cat 4 TDD spec-artifact set but its purpose-axis is Cat 4 DT readiness per [OS] §10.2; not itself an L2, L3, L4, or L5 artifact
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [MECH] Sign-Off Cleanup Policy` header fields per [OS] §8.5.1a)

## Position and boundary

This mechanism governs the cleanup operation that converts a multi-round-revised long-living spec artifact into its sign-off form. It is invoked at most once per artifact per phase. The mechanism operates on document content in place — it does not run code, does not modify schemas, does not introduce new design decisions, and does not produce a parallel archived snapshot. Provenance recovery, when needed, is via the underlying git history of the spec artifact's repository path.

## How to use this source

Use this source when:

- A long-living spec artifact has accumulated multi-round revisions (revision history, lint evidence, inline annotations, governance bookkeeping sections, etc.)
- The trigger condition in §2 is satisfied
- The operator decides to bring the artifact to its sign-off form for downstream AI consumer (Hub Claude / Claude Code) intake

Do not use this source as:

- A substitute for [MECH] Canonical File Self-Audit (different scope: self-audit checks quality during active revision; this MECH governs the cleanup at end-of-revision)
- A way to silently delete forward canonical content under the pretext of "cleanup"
- A justification for skipping audit rounds (cleanup happens after audits, not instead of them)
- A treatment for code/test/evidence artifacts (Cat 4 C1-C3 are governed by different paradigms — git history, evidence locality)

## Cross-reference

- **Grounded in**: [OS] §1.4 audience and consumption model, [OS] §5 output family classification
- **Relationship to [MECH] Canonical File Self-Audit**: Self-audit governs quality during active revision; this MECH governs the removal-of-process-content at sign-off. Adjacent governance mechanisms operating on different layers — Self-Audit at the Meta layer (canonical-source governance), this MECH at the Cat 4 layer (DT-consumption readiness for long-living spec artifacts). The Audit-quiescence trigger in §2 explicitly consumes Self-Audit's S1 / S2 severity definitions
- **Relationship to [MECH] CI/CD Milestone Policy**: M0 Design Freeze (§2.1 of CI/CD) may be a moment when the operator judges a PRD/TDD has reached sign-off candidacy. The relationship is informational, not directional — M0 fires per-slice while sign-off is per-artifact-per-phase, so M0 does not auto-trigger sign-off
- **Relationship to [MECH] Application Lifecycle Handoff**: Application Lifecycle Handoff consumes sign-off versions; sign-off cleanup precedes handoff readiness (per Application Lifecycle Handoff §2.2 mechanical readiness checklist)
- **Relationship to [MECH] Development Track Workflow**: DTW defines the downstream tasks (TK-03 deterministic conversion onwards) whose AI consumers this cleanup protects. Spec artifact paths are invariant across sign-off (cleanup is in place); DTW TK-03 input list paths do not change pre/post sign-off

---

# 1. Purpose and Why Anchor (WA)

## 1.1 What this MECH governs

This MECH governs the operation that converts a long-living spec artifact from its revision-accumulated form into a sign-off form suitable for downstream AI consumer intake.

A long-living spec artifact accumulates two distinct categories of content during its lifecycle:

| Category | Examples | Sign-off treatment |
| --- | --- | --- |
| **Canonical content** | Schema definitions, FR specs, module decomposition, slice lists, scenarios, INVs, DRs, design tokens, business rules | **Kept** |
| **Process content** | Revision history tables, inline `vX.Y 修订` / `vX.Y 锁定` / `替代 vX` annotations, governance bookkeeping sections (e.g., tables mapping past names to current ones, indices tracking resolved questions, sections logging freeze gate evidence, lint evidence sections), "verified" reassurance statements | **Removed** |

The output of this mechanism is the spec artifact at its original canonical path, with all process content removed and the version stamp bumped to `v1.0` to mark sign-off. Subsequent post-sign-off revisions use patch versioning (`v1.0.1`, `v1.0.2`, etc.). A substantively new revision cycle that warrants a fresh sign-off pass re-enters this MECH per §2 and bumps the major version (`v2.0`).

The cleanup is in-place; **no separate archived snapshot is produced and no `signoff-` filename prefix is used**. The underlying git history of the spec artifact's repository path (e.g., `apps/{app-slug}/specs/prd/phase-{N}.md` is git-tracked in the CC monorepo) is the recovery substrate if a deletion needs to be questioned post-sign-off — the same recovery paradigm that already governs C1-C3 per §5.3.

## 1.2 Why Anchor (WA)

Sign-off PRD / TDD / spec artifacts are consumed by AI consumers downstream — Hub Claude at TK-01 / TK-02 spec authoring or amendment and at TK-03 deterministic conversion (per [TPL] PRD + TDD to Intent and Acceptance Conversion Specification + [TPL] Writing Standard §1.11 Hub-only TK-03 invariant), and both Hub Claude and Claude Code at later TKs as reference. Process content gives those consumers zero positive grounding, occupies their context budget, and can cause attention drift (a consumer reading `vX.Y 曾叫 approval_category` may wrongly believe both names co-exist in current canonical); the root purpose of cleanup is therefore to produce a sign-off version containing only content with direct downstream value, in place at the canonical path, with no parallel artifact accumulation.

Any keep-vs-delete uncertainty defaults to: **would keeping this line risk misleading an AI consumer about current canonical, or waste their attention budget?** Yes → delete; No → keep.

## 1.3 How to apply WA — keep-vs-delete decision tree

When the cleanup operator (or the dialog executing cleanup) encounters an uncertain line, apply the following four questions in order. Stop at the first decisive answer:

1. **Is this line's literal information required for any TK-03+ deterministic conversion or downstream generation task?**
    - Required → **keep**
    - Otherwise → proceed to Q2

2. **Is this line's information already expressed in a forward canonical section** (schema, FR, module decomposition, slice list, scenarios, INV/DR tables, etc.)?
    - Already expressed → this line is a redundant historical echo → **delete**
    - Not expressed → proceed to Q3

3. **Does this line describe how something used to be in a past revision** (e.g., "vX.Y 替代 vA.B approval_category", "原 X 改为 Y", "vX.Y 锁定", "vX.Y 责任补完")?
    - Yes → default to **delete** unless Q4 overrides
    - No → proceed to Q4

4. **Would deleting this line risk causing a downstream AI consumer to misinterpret current canonical or be confused about scope?**
    - Yes → **keep** (this is the WA override case; rare in practice)
    - No → **delete**
    - Uncertain → this Q3-true + uncertain-Q4 combination is itself an escalation trigger: do not default-delete; escalate the line to the operator for explicit judgment.

   Rubric for Q4: a deletion creates misinterpretation risk only when the line carries disambiguating information that no forward canonical section restates — for example, a schema column note reading `field renamed from approval_category; the prior name still appears in legacy integration payloads` disambiguates current-vs-legacy naming and is **kept** (Q4-Yes); a bare inline marker reading `vX.Y 锁定` carries no information a downstream consumer could misread and is **deleted** (Q4-No). When the line falls between these two patterns and the disambiguating value cannot be confidently judged, treat Q4 as uncertain and escalate.

The decision tree ensures every cleanup deletion is traceable to either: (a) Q1 false + Q2 true (redundant with canonical), or (b) Q3 true + Q4 false (historical and harmless to remove). Every kept line traces to: Q1 true (operationally needed), or Q4 true (WA override, rare). If no question yields a decisive answer, the line is escalated to the operator for explicit judgment rather than silently kept or deleted.

---

# 2. Trigger conditions

This MECH is invoked only when **one** of the following is satisfied:

| Trigger | Condition |
| --- | --- |
| **Audit quiescence** | Two consecutive audit rounds against the artifact yield zero S1 Blocker and zero S2 Major findings (per [MECH] Canonical File Self-Audit §4 severity scheme). Two rounds rather than one confirms the zero-finding result is stable and not an artifact of a single audit pass missing issues. |
| **Operator judgment** | Operator declares no new issues are expected against the artifact and freeze is desired |
| **Handoff prep** | [MECH] Application Lifecycle Handoff §2.2 readiness checklist requires sign-off versions for application-level handoff to human team |

The operator declares the trigger reason at session opening (per §3.1). This is the sole entry point — the mechanism does not run on a schedule or as part of CI.

---

# 3. Adjudication procedure

The cleanup operation runs as a single Hub Claude session. It is a meta-level operation on spec content (operating on the spec artifact itself rather than on slice-level outputs); it does not run on Claude Code, since cleanup is meta to the spec, not to slice generation.

## 3.1 Session opening

The session opens with:

- Target artifact path (e.g., `apps/{app-slug}/specs/prd/phase-{N}.md`)
- Explicit declaration of trigger condition (per §2)
- Operator declaration that the working copy is the latest fully-revised version of the artifact (not a stale snapshot). A stateless session cannot itself verify currency — it cannot diff the working copy against an external head — so currency is an operator-supplied input. The session reads the artifact fresh at session open and disclaims any guarantee of currency for changes made externally mid-session.

## 3.2 Cleanup pass

The session performs deletion per §4 (per-artifact specifics for the active artifact). For each block deleted, the session applies the §1.3 WA decision tree when ambiguity exists. The session does not silently modify canonical content.

When a line is ambiguous and the decision tree does not yield a decisive answer, the session pauses and asks the operator for explicit adjudication. The session does not exercise discretion in ambiguous cases.

## 3.3 Verification

After cleanup, the session verifies:

- The post-cleanup artifact retains all content categories that §4 (per-artifact specifics) declares as "Kept" for the active artifact type
- The post-cleanup artifact contains no content matching the "Removed" patterns in §4 — no in-line revision annotations of the documented patterns remain; no governance bookkeeping sections remain
- The post-cleanup artifact retains internal consistency (FK references, cross-section pointers, INV numbering, slice-list references all still resolve)

## 3.4 Output

The session outputs:

- The cleaned spec at its original canonical path, with version stamp bumped to `v1.0` on the first sign-off (no filename change, no `signoff-` prefix). Subsequent post-sign-off revisions use patch versioning (`v1.0.1`, `v1.0.2`). When this MECH is re-entered for a substantively new revision cycle that warrants a fresh sign-off pass (per §1.1), the version stamp bumps the major version instead (`v2.0`, then `v3.0`, etc.).
- A short cleanup digest (one paragraph in the session response) reporting the count of deleted blocks per pattern and the trigger reason for this cleanup cycle. The digest is conversation-level only; it does not persist as a separate artifact. Operator reviews the digest in chat for sanity check.

---

# 4. Per-artifact specifics

The per-artifact specifics below describe **content categories** and **example patterns**, not hard-coded section numbers. Actual section numbers vary by artifact instance — the [TPL] PRD / Prototype / MVP Spec Template and [TPL] Technical Design Document Template define framework structure, but instance section numbering depends on application context and operator's section discipline during revision. The cleanup session reads the active artifact, identifies which section holds which category, and applies the cleanup rule by function rather than by literal section-number match.

## 4.1 A1 — phase PRD (`apps/{app-slug}/specs/prd/phase-{N}.md`)

**Kept** — all forward-looking canonical content. Categories observed in practice:

- **Business-design sections** — background, scope, scenarios, user roles, end-to-end process flow, business rules, functional requirements, schemas (logical + physical), permissions and governance, value lists, integration and technical constraints, NFRs, acceptance criteria and traceability
- **Forward-looking risk and design surfaces** — design risks not yet resolved, open questions still outstanding, deferred design points, future enhancement candidates

The PRD template ([TPL] PRD / Prototype / MVP Spec Template) defines which sections house which category at the framework level; the cleanup session retains content matching these categories regardless of the active instance's section number.

**Removed** — all process content. Patterns observed in practice:

- **Revision history tables** — typically in the document-information / header area — replace with a single line: `Sign-off: v1.0 ({date})`
- **Governance bookkeeping sections** — sections whose function is to track the revision process rather than to express canonical business design. Examples seen in real PRDs include tables mapping past names to current names (often labeled "Canonical Register" or similar), indices tracking which questions were raised in which revision and where they were answered (often labeled "Resolved Questions"), sections logging which freeze gate conditions were met when (often labeled "Freeze Gate Evidence"), lint evidence sections. **Section headings vary by instance**; the cleanup decision is by **function** (tracks the revision process itself, not the canonical content), not by literal heading match
- **Inline revision annotations** — examples observed in practice: `vX.Y 修订`, `vX.Y 锁定`, `替代 vA.B`, `原 X 改为 Y`, `vX.Y 新增`. Pattern: in-line marker indicating a change was made in some past revision and the change has now stabilized into the active canonical

**Known cleanup challenges** (report in cleanup digest):

- Inline annotations may be embedded mid-paragraph and are not always line-bounded
- Some schema column descriptions reference prior version names as a way to disambiguate naming history; apply the §1.3 WA decision tree case-by-case

## 4.2 A2 — phase TDD (`apps/{app-slug}/specs/tdd/phase-{N}.md`)

**Kept** — all forward-looking engineering canonical content. Categories observed in practice:

- **Document header** (with revision history removed; version bumped to `v1.0`)
- **Phase-level cross-cutting concerns** — Data Rules (DRs), Invariants (INVs), Visibility Matrix, Permission Projection Policy, phase-level testing strategy, phase-level NFR
- **Walking skeleton scope and boundary** (Phase 1 only)
- **Per-feature engineering specs** — the full active feature engineering spec set: Header, Data-Model, API-Contracts, Module-Decomposition, Slice-List, Domain-Class-Hierarchy, forward-looking Open-Questions
- **Design system spec content** (when scoped within TDD body)
- **Appendices that carry forward-looking engineering content** (e.g., oversize slice details)

The TDD template ([TPL] Technical Design Document Template) defines which sections house which category at the framework level; the cleanup session retains content matching these categories regardless of the active instance's section number.

**Removed** — process content. Patterns observed in practice:

- **Header revision history** — replace with single sign-off line per §4.1 pattern
- **Reverse-link references to PRD process-content sections** — example seen in real TDDs: a sub-section under the header that mirrors a PRD governance bookkeeping table (e.g., "Canonical Register Reference" mirroring a PRD Canonical Register). Once the PRD process content is removed, these reverse-links become unresolvable pointers and serve no forward function. The pattern is "section whose only purpose is to mirror a PRD process-tracking section"
- **In-header "verified" / "标注 verified" reassurance statements** — these document that audit passed, not what the canonical content is
- **Inline revision annotations** — examples observed in practice: `vX.Y 责任补完`, `vX.Y 修订`, `vX.Y 起 fixture`, `vX.Y 锁定`. Same pattern as PRD

**Known cleanup challenges**:

- Some module descriptions contain `vX.Y 责任补完` as an indicator of scope additions across revisions; apply §1.3 WA decision tree to determine whether the addition has stabilized
- INV / DR descriptions may carry rationale tags (e.g., "vX.Y consolidated this constraint from..."); apply §1.3 case-by-case

## 4.3 A3 – A7 — placeholder pending empirical evidence

Per-artifact specifics for the following are deferred until each artifact has accumulated multi-round revision content sufficient to identify a cleanup pattern:

- **A3** phase test plan markdown master (`apps/{app-slug}/specs/test-plan/phase-{N}.md`)
- **A4** feature integration test plan YAML (`apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml`)
- **A5** slice-list (`apps/{app-slug}/specs/slice-list/{feature-slug}.md`)
- **A7** design-system spec (`specs/design-system.md`, project-level singleton)

Until these §4 entries are filled in:

- Cleanup of these artifacts uses §1.3 WA decision tree directly without per-artifact pattern shortcuts
- The first cleanup of each artifact also serves to identify patterns for filling in its §4 entry
- The session performing the first cleanup of each artifact should report a cleanup digest that includes identified process-content patterns; these patterns then back-flow into a §4 update of this MECH expressed in the example-based format used in §4.1 and §4.2 (content categories + example patterns, not hard-coded section numbers)

---

# 5. Exceptions

## 5.1 A6 openapi.yaml — different revision pattern

`apps/{app-slug}/specs/openapi.yaml` accumulates content **additively** across phases (each phase adds endpoints; existing endpoints are rarely re-revised). Its sign-off concept is therefore different — "per-phase endpoint freeze" rather than "delete process history".

Specifics for A6 are deferred until the first phase-end openapi sign-off occurs. The decision tree and cleanup procedure in §1.3 and §3 may need adaptation; this is acknowledged as a known exception, not a coverage gap.

## 5.2 B1 – B3 — Hub-produced slice-level interface artifacts, pending evaluation

The following artifacts are produced by Hub Claude at TK-03 deterministic conversion (per [TPL] PRD + TDD to Intent and Acceptance Conversion Specification + [TPL] Writing Standard §1.11 Hub-only TK-03 invariant):

- **B1** `apps/{app-slug}/specs/intent/{slice-id}.md`
- **B2** `apps/{app-slug}/specs/acceptance/{slice-id}.yaml`
- **B3** `apps/{app-slug}/specs/test-plan/{slice-id}.yaml`

These artifacts may or may not exhibit the same process-content accumulation pattern as A1/A2. The cleanup pattern is hypothesis until empirical evidence is gathered:

| Hypothesis | Implication |
| --- | --- |
| B1-B3 use replace-style updates during Hub-side TK-03 sign-off cross-model review iteration (each operator-driven Hub Claude × ChatGPT consensus loop round rewrites in place) | No process content accumulates; B1-B3 exempt from this MECH |
| B1-B3 accumulate inline annotations / revision history during Hub-side TK-03 sign-off cross-model review iteration | Same pattern as A1/A2; B1-B3 covered by extension of this MECH |

**Note on post-transfer modifications**: After TK-04 transfer to CC per [MECH] Cross-Tool Workflow Handoff §3.1, B1 (intent.md) and B2 (acceptance.yaml) are not modified by CC per [TPL] Writing Standard §1.11 ("No CC-side authoring at TK-03"). B3 (test-plan.yaml) may receive additive TK-10 adversarial-loop-patch entries from adversarial-tester subagent A3, recorded as canonical content with `generated_by: adversarial-loop-patch` provenance per [TPL] Test Plan YAML Schema §4 `generated_by` enum — these are forward canonical content, not process content, and do not by themselves trigger this MECH.

**Default**: B1-B3 are exempt from this MECH until N=2 transition slices have completed TK-03 sign-off cross-model review (per [MECH] DTW §6.1 human intervention budget transition rule). The Hub Claude session that finalizes the second transition slice at TK-03 sign-off reports the observed pattern in its session response, and this §5.2 is updated accordingly (either to confirm exemption or extend coverage).

## 5.3 C1 – C3 — CC-produced code/test/evidence artifacts, permanently exempt

- **C1** code and tests (`src/**`, `tests/**`) — governed by git history; revision history lives in version control, not in file content
- **C2** evidence files (`evidence/{slice-id}/**`) — immutable per [MECH] CI/CD Milestone Policy
- **C3** M4 reports (`reports/m4/{slice-id}/**`) — immutable

These artifacts are permanently outside this MECH's scope. The governance paradigm differs fundamentally (version control vs document-internal history).
