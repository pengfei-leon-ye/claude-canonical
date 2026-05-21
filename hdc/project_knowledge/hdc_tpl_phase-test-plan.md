# [TPL] Phase Test Plan

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable content contract for the phase-level test plan (master, markdown) authored at TK-02 — covering file location, document header, required sections (phase scope summary, cross-feature scenario classes, app-scale NFR scenario classes, regression policy, phase exit criteria, cross-tier traceability), and the boundary against per-feature and per-slice test plans
- **Source Category**: Cat 4
- **Management-System Role**: Template; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control) and §10 (MECE) to test-plan layering.
- **Relationship to [TPL] Test Plan YAML Schema**: Companion. This template owns the phase-level markdown master; [TPL] Test Plan YAML Schema owns the per-feature integration yaml and per-slice yaml. The two are paired by app and phase: one phase test plan + N feature integration test plans + M slice test plans per phase.
- **Relationship to [TPL] TDD Template**: Anchored. Phase test plan §1 (Phase scope summary) cross-references paired phase TDD §1 (Architecture) and §2 (Cross-feature concerns); §3 NFR scenarios reference phase TDD §2.2.1 (NFR baselines).
- **Relationship to [TPL] PRD Prototype MVP Template**: Anchored. Phase test plan §1 cross-references paired phase PRD scope; §2 risk attribution cross-references PRD §13.1 Key Risks.
- **Relationship to [MECH] Development Track Workflow**: TK-02 produces this artifact alongside phase TDD per DTW §4 task definition.
- **Relationship to [MECH] Sign-Off Cleanup Policy**: Applies to phase test plans at sign-off — the phase test plan is a long-living spec artifact subject to Sign-Off Cleanup discipline at handoff prep time.
- **Pairings I participate in**: None (post-Wave 2 Tier rationalization). Two previously-considered candidate couplings (with [TPL] Test Plan YAML Schema, with [TPL] TDD §2 phase-level testing strategy) both classify as Tier B per [OS] §8.5.1a — semantic-search-discoverable via the explicit `Relationship to adjacent [TPL] sources` header field above. No static pairing registration required.

## How to use this source

Use this template when:
- Authoring a phase test plan at TK-02 for a new phase
- Reviewing whether a produced phase test plan conforms to the content contract
- Diagnosing whether a particular testing concern belongs in the phase test plan vs feature integration test plan vs slice test plan

Do not use this template for:
- Feature integration test plan authoring (use [TPL] Test Plan YAML Schema §3)
- Slice test plan authoring (use [TPL] Test Plan YAML Schema §4)
- Phase TDD architecture decisions (those belong in the phase TDD, not the phase test plan)
- Concrete test case enumeration (cases live in feature integration test plan or slice test plan, not the phase master)

## Scope note

The phase test plan is **strategic, not exhaustive**. It frames cross-feature scenario classes, app-scale NFR concerns, regression policy, and exit criteria — but does not enumerate every test case. Specific cases are owned by feature integration test plans (one per feature, yaml) and slice test plans (one per slice, yaml).

The phase test plan is human-authored and human-reviewed. AI agents reference it for context but do not execute its contents directly — execution happens against feature integration test plans (yaml) and slice test plans (yaml) which AI agents and TOOL processes can consume mechanically.

---

# 0. Boundary and position

## 0.1 What this template owns

- File location and naming for phase test plans
- Document header structure
- Required sections (§1 through §7 of the produced plan)
- "What must not appear" boundary
- Phase test plan update discipline

## 0.2 What this template does not own

- Feature integration test plan content (owned by [TPL] Test Plan YAML Schema §3)
- Slice test plan content (owned by [TPL] Test Plan YAML Schema §4)
- Phase TDD architecture content (owned by [TPL] TDD Template)
- Phase PRD scope content (owned by [TPL] PRD Prototype MVP Template)
- Test execution mechanism (owned by [MECH] Development Track Workflow + [MECH] CI/CD Milestone Policy)
- Test case ID / cross-reference conventions (owned by [TPL] Test Plan YAML Schema §0)

## 0.3 Position in the test-plan three-tier ontology

| Tier | Artifact | Owned by template |
|---|---|---|
| Phase | `apps/{app-slug}/specs/test-plan/phase-{N}.md` (master, markdown) | **this template** |
| Feature | `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` (yaml, one per feature in the phase) | [TPL] Test Plan YAML Schema §3 |
| Slice | `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` (yaml, one per slice in each feature) | [TPL] Test Plan YAML Schema §4 |

The phase test plan is the master at the top of the test-plan hierarchy. Feature integration test plans inherit context from it (cross-feature flow expectations); slice test plans inherit context from their feature's integration plan (which inherits from the phase plan).

---

# 1. File location and naming

`apps/{app-slug}/specs/test-plan/phase-{N}.md`, where:
- `{app-slug}` matches the paired phase TDD's `app_slug`
- `{N}` matches the paired phase TDD's `phase_number`

One phase test plan per app per phase. Authored alongside the phase TDD at TK-02.

---

# 2. Document header

The phase test plan must start with a header section listing:

- `app_slug`
- `phase_number`
- Status: Draft | Active | Superseded
- Paired phase TDD reference: `apps/<app-slug>/specs/tdd/phase-<N>.md` (version or commit)
- Paired phase PRD reference: `apps/<app-slug>/specs/prd/phase-<N>.md` (version or commit)
- Author
- Review history
- Features in this phase: comma-separated feature-slug list — must match phase TDD's `Features in this phase`

---

# 3. Required sections

The phase test plan must contain the following sections, in order:

## §1 Phase scope summary

A short prose section (1–2 paragraphs) summarizing the phase scope from a testing perspective. Cross-reference the paired phase PRD §scope and phase TDD §1 architecture. Do not restate; reference.

## §2 Cross-feature scenario classes

A list of scenario classes that exercise multiple features end-to-end. For each class:

- Class id (e.g., `CFS-01`)
- Class name
- Description (one paragraph)
- Features touched (by feature-slug)
- Trigger / starting state
- Expected end state
- Evidence requirement (which feature-level flows or slice-level cases evidence this class)
- Owner subagent or human owner
- Risk attribution (cross-reference paired PRD §13.1 Key Risks if applicable)

## §3 App-scale NFR scenario classes

Scenarios that cannot be localized to a single feature because they exercise app-scale concerns. Examples: load test against the BFF aggregating multiple features; observability dashboard verification across all features; security scanner on the whole app. For each scenario class:

- Class id (e.g., `NFR-01`)
- Class name
- NFR aspect (performance / availability / scalability / observability / security / accessibility)
- Targets and SLI/SLO (cross-reference phase TDD §2.2.1 (NFR baselines))
- Test approach
- Owner

## §4 Regression policy from prior phase (Phase N ≥ 2 only)

For Phase N ≥ 2, declare the regression policy:

- Approach: full regression / risk-based subset / smoke only / none-with-rationale
- Subset criteria (if subset): by risk_tier, by feature, by tier, etc.
- Re-execution responsibility: which agents or human owners
- Frequency: at phase entry / at phase exit / at each milestone

Approach selection rationale:
- **full regression** — choose when this phase changes shared infrastructure, cross-cutting modules, or APIs that prior-phase features depend on, so prior-phase behavior is broadly at risk.
- **risk-based subset** — choose when the phase's changes are localized to specific features or tiers; re-run only the prior-phase scenarios whose risk_tier or touched modules intersect this phase's change surface.
- **smoke only** — choose when the phase is additive and well-isolated, so a thin pass over prior-phase critical paths is enough to catch gross breakage.
- **none-with-rationale** — choose only when the phase shares no code or data path with prior-phase features; the rationale must state that isolation explicitly.

For Phase 1, this section is omitted entirely (there is no prior phase).

## §5 Phase exit criteria

The conditions under which this phase is declared complete. For each criterion:

- Criterion id (e.g., `EXIT-01`)
- Statement (testable condition)
- Evidence source (which feature-level flow result or slice-level case result evidences satisfaction)
- Verification owner
- Threshold (if quantitative; e.g., "100% of CFS-* scenarios pass")

A criterion statement is a **testable condition** when its satisfaction can be decided from a named evidence source by anyone, without a judgment call. Compliant: "All `CFS-*` cross-feature scenario classes pass, with results recorded in the feature-integration test plan run logs." Non-compliant: "Phase is complete when feature X is good enough" — "good enough" names no evidence source and resolves only by opinion.

## §6 Cross-tier traceability table

A table mapping each phase scenario class to the feature-level flows and slice-level cases that evidence it. Format:

| Phase class | feature-level flows | slice-level cases |
|---|---|---|
| `CFS-01` | `feature-A.yaml::flow-03`, `feature-B.yaml::flow-01` | `slice-A-03::TC-04`, `slice-B-01::TC-02` |

Cells may be left as `(deferred to TK-03)` for slice-level cases that have not yet been produced; the cell must be filled in before phase milestone exit.

## §7 Open questions (optional)

Phase-level testing questions that remain open at TK-02 sign-off but do not block immediate work. A question **does not block immediate work** when TK-03 slice extraction and the first slices can proceed without its answer — the answer is needed only at a later slice, milestone, or phase exit. A question whose answer is required before the next slice can be extracted is not an open question: it blocks and must be resolved upstream before TK-02 sign-off. One entry per question with:
- Statement (the question)
- Why open (what input is missing or what decision is pending)
- Resolution target (slice / milestone / phase exit)

---

# 4. What must not appear in the phase test plan

- **Specific slice test case definitions** — those go into per-slice yaml files (per [TPL] Test Plan YAML Schema §4)
- **Per-feature cross-slice flows** — those go into Feature integration test plan files (per [TPL] Test Plan YAML Schema §3)
- **Test code or fixtures** — those are runtime artifacts, not specifications
- **Phase architecture decisions** — those belong in phase TDD §1 / §2 (per [TPL] TDD Template)
- **Test execution machinery** — gate semantics, milestone triggers, hook chains belong in [MECH] CI/CD Milestone Policy and [MECH] Development Track Workflow

---

# 5. Update discipline

## 5.1 Phase test plan as a long-living spec artifact

Phase test plans (along with phase PRDs and phase TDDs) are long-living spec artifacts subject to [MECH] Sign-Off Cleanup Policy at handoff prep time. During the active phase, the plan may receive multiple revisions reflecting:
- New cross-feature scenarios discovered during implementation
- NFR baseline adjustments after early measurement
- Regression policy refinements
- Open question resolutions

At sign-off (per [MECH] Sign-Off Cleanup Policy §2 Handoff-prep trigger), the phase test plan is brought to clean form: in-line revision annotations removed, governance bookkeeping sections removed, content semantically clean.

## 5.2 Cross-document update discipline

When phase TDD or phase PRD changes in a way that affects testing:
- New cross-feature flow introduced in phase TDD §2 → add CFS-* entry in phase test plan §2
- NFR baseline changed in phase TDD §2.NFR-Baselines → update NFR-* entry in phase test plan §3
- New feature added in phase PRD §7.1 Feature List → the update propagates in a fixed chain: phase PRD §7.1 change → paired phase TDD updated first (so its `Features in this phase` reflects the new feature) → phase test plan synced to the phase TDD. The phase test plan header `Features in this phase` is kept in sync with the phase TDD (its authority per §2), not lifted directly from the PRD; verify cross-feature scenario classes still cover the new feature

These updates apply in the same revision per [OS] §8.5.2 paired-update discipline.

## 5.3 Cross-tier traceability table maintenance

§6 cross-tier traceability table cells marked `(deferred to TK-03)` must be filled in before phase milestone exit. This is the operational hook between phase-level strategy and slice-level execution evidence.
