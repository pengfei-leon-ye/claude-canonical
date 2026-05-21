# [TPL] Phase Test Plan

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical
- **Role**: Content contract for the phase-level test plan (master, markdown) authored at TK-02 — covering file location, document header, required sections (phase scope summary, cross-feature scenario classes, app-scale NFR scenario classes, regression policy, phase exit criteria, cross-tier traceability), and the boundary against per-feature and per-slice test plans
- **Source Category**: Cat 4
- **Management-System Role**: Template; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control) and §10 (MECE) to test-plan layering.
- **Relationship to [TPL] Test Plan YAML Schema**: Companion. This template owns the phase-level markdown master; [TPL] Test Plan YAML Schema owns the per-feature integration yaml and per-slice yaml. The two are paired by app and phase: one phase test plan + N feature integration test plans + M slice test plans per phase.
- **Relationship to [TPL] TDD Template**: Anchored. Phase test plan §1 (Phase scope summary) cross-references paired phase TDD §1 (Architecture) and §2 (Cross-feature concerns); §3 NFR scenarios reference phase TDD §2.NFR-Baselines.
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
- Required sections (§3.1 through §3.7 of this template)
- "What must not appear" boundary
- Anti-pattern declaration
- Phase test plan update discipline
- Anti-drift red flags specific to phase test plan authoring

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

## 3.1 §1 Phase scope summary

A short prose section (1–2 paragraphs) summarizing the phase scope from a testing perspective. Cross-reference the paired phase PRD §scope and phase TDD §1 architecture. Do not restate; reference.

## 3.2 §2 Cross-feature scenario classes

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

## 3.3 §3 App-scale NFR scenario classes

Scenarios that cannot be localized to a single feature because they exercise app-scale concerns. Examples: load test against the BFF aggregating multiple features; observability dashboard verification across all features; security scanner on the whole app. For each scenario class:

- Class id (e.g., `NFR-01`)
- Class name
- NFR aspect (performance / availability / scalability / observability / security / accessibility)
- Targets and SLI/SLO (cross-reference phase TDD §2.NFR-Baselines)
- Test approach
- Owner

## 3.4 §4 Regression policy from prior phase (Phase N ≥ 2 only)

For Phase N ≥ 2, declare the regression policy:

- Approach: full regression / risk-based subset / smoke only / none-with-rationale
- Subset criteria (if subset): by risk_tier, by feature, by tier, etc.
- Re-execution responsibility: which agents or human owners
- Frequency: at phase entry / at phase exit / at each milestone

For Phase 1, this section is omitted entirely (there is no prior phase).

## 3.5 §5 Phase exit criteria

The conditions under which this phase is declared complete. For each criterion:

- Criterion id (e.g., `EXIT-01`)
- Statement (testable condition)
- Evidence source (which feature-level flow result or slice-level case result evidences satisfaction)
- Verification owner
- Threshold (if quantitative; e.g., "100% of CFS-* scenarios pass")

## 3.6 §6 Cross-tier traceability table

A table mapping each phase scenario class to the feature-level flows and slice-level cases that evidence it. Format:

| Phase class | feature-level flows | slice-level cases |
|---|---|---|
| `CFS-01` | `feature-A.yaml::flow-03`, `feature-B.yaml::flow-01` | `slice-A-03::TC-04`, `slice-B-01::TC-02` |

Cells may be left as `(deferred to TK-03)` for slice-level cases that have not yet been produced; the cell must be filled in before phase milestone exit.

## 3.7 §7 Open questions (optional)

Phase-level testing questions that remain open at TK-02 sign-off but do not block immediate work. One entry per question with:
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

# 5. Anti-pattern

Treating the phase test plan as a comprehensive enumeration of every test case across the phase. The phase test plan is **strategic, not exhaustive**; specific cases live in the feature integration test plan and slice test plan.

The phase test plan answers questions like:
- What cross-feature scenarios must we test?
- What app-scale NFR concerns matter?
- What's the regression policy from prior phase?
- What are the phase exit criteria?

The phase test plan does NOT answer:
- What specific test cases for slice X cover acceptance criterion Y? (slice test plan)
- What sequence of operations does feature A's integration test execute? (feature integration test plan)

---

# 6. Update discipline

## 6.1 Phase test plan as a long-living spec artifact

Phase test plans (along with phase PRDs and phase TDDs) are long-living spec artifacts subject to [MECH] Sign-Off Cleanup Policy at handoff prep time. During the active phase, the plan may receive multiple revisions reflecting:
- New cross-feature scenarios discovered during implementation
- NFR baseline adjustments after early measurement
- Regression policy refinements
- Open question resolutions

At sign-off (per [MECH] Sign-Off Cleanup Policy §2 Handoff-prep trigger), the phase test plan is brought to clean form: in-line revision annotations removed, governance bookkeeping sections removed, content semantically clean.

## 6.2 Cross-document update discipline

When phase TDD or phase PRD changes in a way that affects testing:
- New cross-feature flow introduced in phase TDD §2 → add CFS-* entry in phase test plan §2
- NFR baseline changed in phase TDD §2.NFR-Baselines → update NFR-* entry in phase test plan §3
- New feature added in phase PRD §7.1 Feature List → update phase test plan header (Features in this phase) + verify cross-feature scenario classes still cover the new feature

These updates apply in the same revision per [OS] §8.5.2 paired-update discipline.

## 6.3 Cross-tier traceability table maintenance

§3.6 cross-tier traceability table cells marked `(deferred to TK-03)` must be filled in before phase milestone exit. This is the operational hook between phase-level strategy and slice-level execution evidence.

---

# 7. Anti-drift red flags

> **Scope**: this section enumerates **phase-test-plan-specific** anti-drift red flags. Cross-cutting test-plan red flags are owned by [TPL] Test Plan YAML Schema; cross-cutting canonical-source red flags by [OS] §12.3.

**Content category dimension**:
- Phase test plan containing specific test case definitions (should be in slice test plan)
- Phase test plan containing test code or fixtures (those are runtime artifacts, not specifications)
- Phase test plan containing phase architecture decisions (those belong in phase TDD)

**Layering dimension**:
- Cross-feature scenario class missing in phase test plan §2 when phase PRD identifies cross-feature business flow
- NFR scenario class missing in phase test plan §3 when phase TDD §2 sets NFR baselines
- Phase exit criteria not testable (e.g., "Phase is complete when feature X is good enough" — not testable)
- §3.6 cross-tier traceability table cells left at `(deferred to TK-03)` past phase milestone exit

**Versioning dimension**:
- Phase test plan paired references (`Paired phase TDD reference`, `Paired phase PRD reference`) pointing to an outdated TDD or PRD version when the latest sign-off is newer (per [MECH] Canonical File Self-Audit version-pairing discipline)
- `Features in this phase` header field not matching phase TDD's `Features in this phase`

**Update discipline dimension**:
- Phase test plan not updated when phase TDD's NFR baselines change in a way that affects §3 NFR scenarios (per §6.2 paired-update)
- New feature added in phase PRD without corresponding update to phase test plan header (`Features in this phase`)
- Phase test plan at sign-off retaining in-line revision annotations from active phase (per [MECH] Sign-Off Cleanup Policy)

**Risk attribution dimension**:
- Cross-feature scenario class §2 Risk attribution field empty when paired PRD §13.1 has applicable Key Risks
- Risk-based regression subset (§4 Approach: `risk-based subset`) without explicit risk_tier criteria

**Boundary leakage dimension**:
- Slice test plan content (specific test cases) leaking into phase test plan
- Feature integration test plan content (per-feature cross-slice flows) leaking into phase test plan
- Phase test plan attempting to override slice or feature test plan ownership (the phase plan frames, it does not override)
