# [MECH] CI/CD Milestone Policy

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable milestone-policy source for Claude Code development work, defining when user review is required versus when the AI works autonomously, and the gate semantics for each milestone across the development lifecycle
- **Source Category**: Cat 4
- **Management-System Role**: Governance mechanism specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Supports the Orchestrate loop by codifying the review-gating mechanism for Development Track execution. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §5 (management mechanism over ad hoc control) to milestone gating design, §6 (operation management and value realization by design) to the M0–M5 sequence.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. CI/CD milestone gating is a CC-side mechanism that operates against code produced in the CC workspace.
- **Relationship to [RULE] Workspace Topology**: Co-governing. §1.2 multi-node evidence parity anchors WT §4.4; §2.6 M5 milestone anchors WT §5 branch topology; walking-skeleton-first ordering (WT §4.6.2) defers downstream-unit milestone entry.
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. §2.3 M2 Pact contract testing convention references CCAR §Y.4.
- **Relationship to [RULE] Codex Plugin Usage**: Anchored. Codex invocation points anchor to milestones defined here.
- **Relationship to [MECH] Development Track Workflow**: Companion. CI/CD §2 milestone semantics + §2.0 per-unit-type profile pair with DTW §4 task sequence + §4.0 unit_type catalog.
- **Relationship to [MECH] Application Lifecycle Handoff**: The AI-dev CI/CD pipeline produces no release tags; release tag namespaces belong to the receiving company's CI/CD scope. The handoff tag namespace (Handoff §4.1) is the only canonical-recognized tag namespace in the AI-dev monorepo.
- **Relationship to [RULE] Design System Governance**: M3 visual review references DSG consistency. No accessibility gate at any milestone (per DSG §6 stance). DS instance three-way distribution per DSG §1.1 + §13 (CD = SOT; Hub spec-time mirror at `hdc_ref_design-system.md`; CC code-time mirror at `specs/design-system.md`) governs which mirror is consulted at which milestone — Hub mirror consulted at TK-02 Step 2.3 UX Design Spec authoring; CC mirror consulted at TK-04+ via SK-F.
- **Relationship to [TPL] Intent and Acceptance Interface Writing Standard** and **[TPL] PRD + TDD to Intent and Acceptance Conversion Specification**: §6 below owns the disambiguation between milestone-level Test Evidence Report and feature-slice-scoped `evidence.md` referenced in those templates.
- **Relationship to [TPL] Test Plan YAML Schema**: A10 evidence digest contract in §6.4 binds to that template's `evidence_required` field.
- **Pairings I participate in**: P-01 (with [RULE] CCAR §6), P-03 (with [MECH] DTW §4), P-09 (with [MECH] DTW §4.0), P-13 (with [MECH] Dev-Loopback §6), P-32 (with [RULE] Codex §1.4), P-49 (with [MECH] Tools Health Cadence §3 step 7 + §5.3)

## How to use this source

Use this source when:
- setting up milestone policy in a new Claude Code project CLAUDE.md
- deciding whether user intervention is required at a specific point in development
- designing automated test triggers
- invoking Codex plugin for cross-model review
- understanding which agents run at which milestone
- pinning the project's Claude Code tooling baseline (§1.1)
- judging whether evidence from a specific node satisfies milestone requirements (§1.2)
- assessing slice size at M2 / M4 boundaries (§2.7)
- scheduling M4 reviews per slice or in a batched session (§2.5.1)

Do not use this source as:
- a sprint planning template
- a project management handbook
- a substitute for per-initiative release planning
- the definition of task-level inputs, outputs, or role sequences (that is [MECH] Development Track Workflow)
- a branch topology reference ([RULE] Workspace Topology §5)
- a handoff or ownership-transition reference ([MECH] Application Lifecycle Handoff)

---

# 0. Boundary and position

## 0.1 What this source owns

- M0–M5 milestone definitions and trigger conditions
- Per-unit-type milestone profile (§2.0): which milestones apply to which `unit_type` (`walking_skeleton`, `feature`, `app_integration`)
- User review requirement per milestone (when user review is required vs when AI works autonomously)
- Gate semantics for each milestone: automated actions, gate outcome, failure routing
- M5 staging-deploy semantics (§2.6) — the terminal milestone of the AI-dev CI/CD chain; production deploy is the receiving company's CI/CD scope per [MECH] Application Lifecycle Handoff §0.2
- Stuck recovery protocol (§4) for milestone-level escalation
- Codex review gate default stance (§5)
- Test Evidence Report content and milestone-level evidence semantics (§6) — distinct from slice-scoped `evidence.md`
- Performance testing scope (§7)
- Anti-drift red flags specific to milestone policy (§9)

## 0.2 What this source does not own

- TK-by-TK orchestration ([MECH] Development Track Workflow §4)
- Quality tooling, rule preset selection, or CI/CD pipeline step ordering ([MECH] Code Quality Rule Set)
- Branch topology, node assignment, or multi-node evidence parity rules ([RULE] Workspace Topology)
- Application-level handoff to human dev team or re-entry to AI-dev ([MECH] Application Lifecycle Handoff)
- Slice-scoped `evidence.md` standards (those are execution-side conventions referenced by §6 but not owned here)
- Tier-boundary semantics ([RULE] Claude Code Architecture Rules §1)
- Codex command-level usage rules (those are owned by [RULE] Codex Plugin Usage; this source only declares the review gate's milestone anchor)
- Dev-loopback contract or fixture content ([MECH] Dev-Loopback Mode); §2.6 walking_skeleton M5 acceptance is supplemented by [MECH] Dev-Loopback Mode §6, but the supplemental assertions are owned there

## 0.3 Position relative to DTW and Handoff

| Aspect | This source | [MECH] DTW | [MECH] Application Lifecycle Handoff |
|---|---|---|---|
| Granularity | Milestone-level (M0–M5) | Task-level (TK-01 — TK-13) | Application-level event |
| Lifecycle scope | Within one unit_type execution | Within one unit_type execution | Cross-application, post-M5 |
| Time scale | Days to weeks per milestone | Hours to days per TK | Episodic (zero, one, or many per app) |
| Triggers | Milestone arrival per §2.0 profile | Sequential TK advance per DTW §4 | Operator-judged maturity per Handoff §2 |

The three sources are operationally distinct but tightly paired: TK execution drives milestone arrival; milestone gates determine whether TK can advance; handoff is an application-level event outside the unit_type milestone cycle.

---

# 1. Core principle

User review is scarce and must be budgeted deliberately.

Between formal milestones, Claude Code works autonomously following canonical architecture rules, testing policy, and skill constraints.

At formal milestones, user judgment is required for decisions that affect business outcomes, architectural integrity, design system integrity, or merge authorization.

## 1.1 Tooling baseline

Claude Code tooling has demonstrated quality regression risk at the product layer (e.g., reasoning effort changes, caching bugs, system prompt changes) that can affect Development Track output quality without changing the underlying model weights. The project pins a baseline version and enforces an upgrade procedure.

**Baseline version**: Claude Code v2.1.116 or higher. Earlier versions are not sanctioned for Development Track work due to the documented Feb–Apr 2026 quality regression resolved at v2.1.116.

**Upgrade procedure**: before adopting any new Claude Code version across the project's nodes, the operator runs one previously-passed slice through the full M0 → M5 chain in an isolated git worktree on the candidate version, and compares evidence output (test results, compliance final pass, Codex review) against the prior baseline's evidence for the same slice. Material divergence — interpreted by the operator's judgment, not codified here — blocks rollout. Successful comparison promotes the candidate to the new baseline; the previous baseline is retained as fallback for one full feature cycle.

**Out of scope for this section**: per-node tool stack version pinning beyond Claude Code itself ([RULE] Workspace Topology §3); operator personal tooling (editor, terminal, etc.).

> **v0 assumption — to be calibrated**: The "previously-passed slice" used for upgrade verification is operator's choice. After the first three upgrade events, lessons-harvest may codify a default verification slice or a verification matrix.

## 1.2 Multi-node evidence parity

Evidence produced on any sanctioned dev node ([RULE] Workspace Topology §2.1 logical node catalog) is treated as equivalent for milestone decisions. The basis for parity is the single-shared agent configuration at `HDC_ROOT/.claude/agents/` (per Workspace Topology §4.4) — every node runs identical subagent definitions, identical context-scope policies, and identical skill loading rules.

Operational implications:

- M0 → M5 milestone gates do not discriminate by which node produced the evidence
- Test Evidence Report aggregation (§6) draws from the slice's `assigned_node` evidence directory regardless of which physical machine is currently active
- Operator review (M0 / M4) does not require physical-node verification beyond what is recorded in the GitHub Issue marker block per Workspace Topology §6.2

A milestone gate decision that gives weight to which node produced evidence is an anti-drift signal per §9.

---

# 2. Milestone definitions

This section defines when each test type executes across the development lifecycle and which agents run at each gate. For tier-by-tier test ownership (which tier owns which test type and at what coverage depth), see [RULE] Claude Code Architecture Rules §6. For task-level inputs, outputs, and role sequences, see [MECH] Development Track Workflow §4. The per-unit-type milestone profile in §2.0 immediately following determines which milestones each unit_type runs through; §2.1–§2.6 below define each milestone's gate semantics.

## 2.0 Per-unit-type milestone profile

Three node-level work unit types (`walking_skeleton`, `feature`, `app_integration`) are catalogued in [MECH] Development Track Workflow §4. Each unit type runs a different subset of M0–M5; the table below is canonical and is the basis for executor scheduling, Codex fire conditions ([RULE] Codex Plugin Usage), and Hub Claude soft-compliance phrasing.

| Unit type | Milestone path | Per-milestone scope variation |
|---|---|---|
| `walking_skeleton` (Phase 1 only, exactly 1 slice) | M0 → M1 → M2 → M3 → M4 → M5 (full chain) | M2 is standard slice-level scope; passing M2 empirically asserts the CI/CD pipeline is established for the app per [RULE] Workspace Topology §4.6.2 walking-skeleton-first ordering rule. M5 staging deploy completion releases the walking-skeleton-first gate for downstream `feature` and `app_integration` units in the same Phase 1 |
| `feature` (any phase, 1+ slices) | Per slice: M0 → M1 → M2 → M3 → M4 → M5 (full chain) | The **last slice** of a feature runs an **expanded M2 scope** that additionally executes the feature integration test plan (`apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml`), validating cross-slice flow within the feature before the feature is considered M2-green. See §2.3.1 |
| `app_integration` (any phase, 0 customer-facing slices) | M2 → M3 → M4 → M5 (truncated; no M0 / M1) | Single PR per unit. M2 entry scope shifts to phase test plan master cross-feature scenarios + feature integration test cross-feature variants + app-scale NFR validation. See §2.3.2 |

Walking-skeleton-first ordering (per [RULE] Workspace Topology §4.6.2): in Phase 1, no `feature` unit's M0 and no `app_integration` unit's M2 entry can begin until the Phase 1 `walking_skeleton` unit reaches `status: merged` on `main`. Hub-side specification work (TK-01 phase PRD, TK-02 phase TDD + per-feature artifacts) MAY proceed in parallel with walking-skeleton execution; the gate is the unit's first node-side milestone, not the Hub-side specification work.

`app_integration` unit slice ontology note: "0 slices" is the count of customer-facing capability slices (per audit-of-record-4 Q2 reconciliation). The unit may still produce non-trivial test code, scenario fixtures, and NFR validation harness; these deliverables do not carry slice-level intent / acceptance and are authored against the phase test plan master + feature integration test plans as their authoring source.

## 2.1 M0 Design Freeze (entry self-check folded into TK-04)

**Post-refactor change**: In the pre-refactor architecture, M0 was a standalone task (the legacy TK-04 "M0 gate decision and handoff") executed by CC at the start of slice implementation, including operator-led adversarial review of the spec bundle. The post-refactor architecture has retired the standalone M0 task; the design-freeze function is split across two structural changes:

1. **Design-freeze gate moves upstream to Hub TK-02 + TK-03 sign-offs**: Hub-side specification production for a slice spans TK-02 (phase TDD + per-feature artifacts, including — when Tier 1 is involved — UX Design Spec instance authoring at TK-02 Step 2.3 per [MECH] DTW TK-02 internal step decomposition) and TK-03 (per-slice intent + acceptance + test-plan). Each sign-off carries the design-freeze function for its scope: **At TK-02 sign-off**: the phase TDD plus per-feature artifacts (including, when Tier 1 is involved, the Hub-authored UX Design Spec instance markdown produced at TK-02 Step 2.3 per `[TPL] UX Design Spec` from CD-authored design files + Hub DS mirror grounding) are sign-off-gated by the operator's cross-model review reminder per [MECH] Development Track Workflow brownfield reconstruct pre-step. The operator may invoke a cross-model review (e.g., ChatGPT review of the TDD architecture and UX Design Spec instance content) or proceed. **At TK-03 sign-off**: the per-slice intent / acceptance / test-plan triple is gated by the operator's GPT-Claude consensus loop — the de facto design freeze gate for the slice — before any artifact transfers to CC. See [MECH] Development Track Workflow §0.4 default operating chain.

2. **M0 entry self-check folds into the start of TK-04**: When CC receives the spec bundle from Hub, the first sub-step of TK-04 is a mechanical entry self-check verifying that the bundle is intact (file presence; trace fields consistent; no stale references to retired paths like `specs/design-system-changes/` or `apps/{app-slug}/specs/ux-bundles/{feature-slug}/`; component references in intent.md UX brief present in DS instance via SK-F against the CC mirror at `specs/design-system.md`; UX Design Spec instance markdown header records the DS instance version it was authored against and that version matches the current CC mirror version per the lock-step sync discipline in DSG §12.5 + §12.7). This is a structural-integrity check, not a design-quality adversarial review.

**Trigger**: Hub specification production complete; PRD + TDD + openapi + slice-list + per-slice intent/acceptance/test-plan + (when Tier 1 involved) the Hub-authored UX Design Spec instance markdown (authored at TK-02 Step 2.3 per [TPL] UX Design Spec at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`) plus CD-authored design files as visual reference, handed to Claude Code via [MECH] Cross-Tool Workflow Handoff §3.1. When Tier 1 is involved, the DS instance is also available across the three-way distribution model (CD = SOT per [RULE] DSG §1.1; Hub spec-time mirror at `hdc_ref_design-system.md` per DSG §13.3; CC code-time mirror at `specs/design-system.md` per DSG §1.1; initial instance produced at workspace inception per [RULE] Workspace Topology §10; subsequent additive updates flow per [RULE] DSG §12 with plan declared in the UX Design Spec instance §2.4 at TK-02 Step 2.3, merged to CD SOT at the originating feature's TK-12 merge-to-`main`, and synced to both mirrors via CD-generated DS markdown export per DSG §12.5 + §12.7).

**Mapped tasks**: TK-04 entry sub-step 1 (M0 entry self-check per [MECH] Development Track Workflow TK-04 role sequence step 1). The design-freeze function it once served is fulfilled at Hub TK-02 + TK-03 sign-offs per the post-refactor architecture.

**Automated actions**: None at M0. The entry self-check is CC-mechanical (structural verification, not adversarial review). Codex is not invoked at M0 in the post-refactor architecture; the prior `/codex:adversarial-review` M0 invocation has been retired per the same canonical change that retired the standalone M0 task.

**Operator interaction at M0**: 
- At Hub TK-02 sign-off (the phase-level + UX Design Spec instance design freeze gate): the operator confirms the phase TDD and per-feature artifacts are sound, applies the reviewer checklists in `[TPL] UX Design Spec` §3 to the Hub-authored UX Design Spec instance (§3.1 design file quality check at Step 2.3 entry; §3.2 instance authoring quality check at Step 2.3 exit), and signs off. If a Design System Governance change was drafted (as part of a UX Design Spec instance §2.4 additive update plan), the operator confirms the plan is sound at this gate; actual merge to the CD SOT happens at the originating feature's TK-12 merge-to-`main` per DSG §12.5, with DS markdown export sync to both Hub mirror at `hdc_ref_design-system.md` and CC mirror at `specs/design-system.md` per DSG §12.7.
- At Hub TK-03 sign-off (the slice-level design freeze gate): the operator drives the GPT-Claude consensus loop; both models must reach agreement on the slice's intent / acceptance / test-plan triple before sign-off.
- At CC TK-04 entry self-check: operator is on-call only — the self-check is mechanical; the operator is engaged only when the self-check surfaces a structural inconsistency that requires routing back to Hub TK-03 (or further upstream to TK-02 Step 2.3 for UX Design Spec instance revision) for re-conversion.

**Gate outcome**:
- TK-02 sign-off → Pass: TDD + per-feature artifacts (including Hub-authored UX Design Spec instance when applicable) approved; proceed to per-feature onboarding then to TK-03 for the unit's slices
- TK-02 sign-off → Block: revise in Hub at the relevant Step (2.1 for TDD/openapi/slice-list/test-plan, 2.2 for CD design files, 2.3 for UX Design Spec instance)
- TK-03 sign-off → Pass: artifacts transfer to CC at the assigned_node; TK-04 entry self-check fires automatically at CC session start
- TK-03 sign-off → Block: revise in Hub (TK-01 / TK-02 / TK-03 per scope); do not transfer
- TK-04 entry self-check → Pass: CC continues into code writing within TK-04
- TK-04 entry self-check → Fail (structural inconsistency surfaced): CC raises to operator; operator routes back to Hub TK-03 (or upstream)

**Unit_type applicability**: M0 (in both the upstream Hub TK-02 + TK-03 design-freeze function and the downstream TK-04 entry self-check function) runs for `feature` and `walking_skeleton` units only. `app_integration` units skip M0 entirely per §2.0 — they have no slice-level new feature spec to design-freeze; their first milestone is M2 entry per §2.3.3.

## 2.2 M1 Feature Slice Complete

**Trigger**: Code writing complete for one feature slice; whitebox test cycle invoked.

**Mapped tasks**: TK-04 (code writing), TK-05 (M1 auto cycle), TK-06 (unit test auto-repair), TK-07 (RCA if failure).

**Automated actions**:
- Static analysis via PostToolUse hook on `apps/{app-slug}/src/**` and `packages/domain/{domain-name}/src/**` writes
- SK-F skill enforcement for Tier 1 code (design system compliance at generation, consulting CC mirror at `specs/design-system.md` per DSG §1.1)
- Unit test generation and execution via A1 (test-writer-whitebox)
- Auto-repair via A5 (unit-test-auto-repair) if unit tests fail, max 3 retries per test
- RCA generation via A6 (rca-reporter) if auto-repair exhausts or internal-integration fails
- Generate test evidence at `apps/{app-slug}/evidence/{slice-id}/` for app-scoped results, and `packages/domain/{domain-name}/evidence/` for domain-scoped unit results when Tier 3 is touched

**User review required**: None in steady state.

**Gate outcome**:
- All unit tests and internal-integration tests pass: accumulate test evidence, proceed to M2
- Unit tests cannot be auto-repaired after 3 attempts: escalate to RCA (TK-07); user decides next action
- Internal-integration fail: RCA (TK-07); user decides next action

**Unit_type applicability**: M1 runs for `feature` and `walking_skeleton` units (slice-level whitebox unit + internal-integration testing for net-new feature code). `app_integration` units skip M1 per §2.0.

## 2.3 M2 Integration Green

**Trigger**: M1 complete (for `feature` / `walking_skeleton` units); TK-02 sign-off + assigned_node onboarding complete (for `app_integration` units, which enter M2 directly per §2.0).

**Mapped tasks**: TK-08 (M2 core), TK-09 (M2 adversarial loop).

M2 has three execution variants depending on unit type and slice position. §2.3.1 defines the standard slice-level scope (applies to every slice of a `feature` unit and to the single slice of a `walking_skeleton` unit). §2.3.2 defines the last-slice expansion (applies only to a `feature` unit's last slice). §2.3.3 defines the `app_integration` unit variant.

### 2.3.1 Standard slice-level scope

Applies to every slice of a `feature` unit (including the last slice — the last-slice expansion in §2.3.2 is **additive** to this scope, not a replacement) and to the single slice of a `walking_skeleton` unit.

**Automated actions**:
- **Contract testing — consumer-driven Pact convention** per [RULE] Claude Code Architecture Rules §Y.4:
  - Consumer-side contracts authored by A2 at `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**`
  - Producer-side verification authored by A2 at `packages/domain/{domain-name}/tests/contract-verification/**`
  - Test pair name format: `{app-slug}-bff_{domain-name}` (e.g., `hr-data-asset-mgmt-bff_data-asset`)
- External-integration tests authored by A2 at `apps/{app-slug}/tests/integration/external/**`
- A9 (compliance-checker) first-pass, including Design System Governance compliance for Tier 1 slices (against the CC mirror per DSG §1.1) and app/domain placement audit per Architecture Rules §Y
- A3 (adversarial-tester) derives adversarial scenarios from acceptance + PRD risk register + test-plan
- CC main loop patches `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` with adversarial additions; re-runs via A2 or A1 as needed
- A6 (rca-reporter) generates RCA on any test failure
- **Slice-size advisory check** per §2.7: if the slice exceeds soft upper limits, evidence is flagged for conditional manual review at M4

**Evidence locations**:
- App-scoped contract + external-integration results: `apps/{app-slug}/evidence/{slice-id}/`
- Domain-side producer-verification results: `packages/domain/{domain-name}/evidence/` (cross-referenced from the app-scoped slice evidence)
- Compliance first-pass: `apps/{app-slug}/evidence/{slice-id}/compliance-first-pass.md`

**User review required**:
- None in steady state
- Conditional: severe compliance violation triggers Notification
- Conditional: high-severity adversarial finding requires your ack before auto-patch proceeds (per TK-09)
- Conditional: §2.7 slice-size advisory flag surfaced — informational at M2, gate-decision at M4

**Gate outcome**:
- All tests pass + compliance clean + adversarial findings resolved: proceed to M3 (or to §2.3.2 last-slice expansion if this is a `feature` unit's last slice)
- Fail: deliver RCA + recommendation; user decides

A2 and A3 operate under `api_contracts` and `business_rules_only` context scopes respectively per [RULE] Claude Code Architecture Rules §X; they do not read `src/**`.

For a `walking_skeleton` unit, passing §2.3.1 empirically asserts that the CI/CD pipeline is established for the app — the unit's slice has traversed M0 → M1 → M2 successfully through the project's CI/CD machinery, validating the foundational architecture and cross-feature baselines end-to-end.

### 2.3.2 Last-slice expansion (feature unit only)

When the slice currently at M2 is the **last slice of its `feature` unit** (per the unit's slice-list in `apps/{app-slug}/specs/slice-list/{feature-slug}.md`), the M2 scope expands to additionally execute the feature integration test plan, validating cross-slice flow within the feature before the feature is considered complete.

**Additive automated actions** (in addition to §2.3.1 scope):
- A2 authors or completes feature integration tests at `apps/{app-slug}/tests/integration/feature/{feature-slug}/**` based on `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml`
- TOOL executes the feature integration test suite end-to-end, exercising the cross-slice flow scenarios catalogued in the feature integration test plan (e.g., slice A draft → slice B approve → slice C sign sequence)
- Evidence appended to `apps/{app-slug}/evidence/{feature-slug}/feature-integration-results.json` at feature scope (in addition to the slice-scoped `apps/{app-slug}/evidence/{slice-id}/` results)

**Gate outcome (last slice)**: §2.3.1 outcome **plus** all feature integration tests pass. Both conditions must be satisfied for M2-green at the last slice.

**Why last slice**: feature integration tests exercise cross-slice flows within the feature; running them earlier than the last slice would either fail (because earlier slices haven't landed yet) or require expensive scaffolding. Authoring them at the last slice's M2 keeps the integration test plan close to the slices it integrates, and amortizes the fixture cost over a single execution per feature.

### 2.3.3 App_integration unit variant

`app_integration` units enter M2 directly (no upstream M0 / M1 within the unit). The unit produces a single PR; M2 is the unit's first milestone.

**Automated actions** (variant scope; replaces §2.3.1 scope, not additive):
- A2 authors phase test plan master cross-feature scenarios at `apps/{app-slug}/tests/integration/phase/{phase-{N}}/**` based on `apps/{app-slug}/specs/test-plan/phase-{N}.md`
- A2 authors feature integration test cross-feature variants not covered at any individual `feature` unit's TK-08 — i.e., scenarios that span two or more features within the phase, which by definition cannot be authored at any single feature's last slice
- A2 (or operator-judged tooling for NFR-specific harness) authors app-scale NFR validation harness at `apps/{app-slug}/tests/nfr/**` based on `apps/{app-slug}/specs/tdd/phase-{N}.md` §2.NFR-Baselines
- TOOL executes all of the above against the deployed integration environment
- A9 (compliance-checker) first-pass on the unit's PR diff (test code + fixtures + NFR harness), including app/domain placement audit per Architecture Rules §Y
- A3 (adversarial-tester) derives adversarial scenarios from the phase test plan + feature integration test plan + PRD §13.1 risks
- A6 (rca-reporter) generates RCA on any test failure

**What is NOT re-run at §2.3.3**: standard slice-level contract tests and external-integration tests for individual features — those were validated at the relevant `feature` unit's §2.3.1 / §2.3.2 and are not re-executed at the app_integration unit's M2.

**Evidence locations**:
- Phase test plan results: `apps/{app-slug}/evidence/app-int-phase-{N}/phase-test-results.json`
- Cross-feature integration results: `apps/{app-slug}/evidence/app-int-phase-{N}/cross-feature-integration-results.json`
- App-scale NFR results: `apps/{app-slug}/evidence/app-int-phase-{N}/nfr-results.json`
- Compliance first-pass: `apps/{app-slug}/evidence/app-int-phase-{N}/compliance-first-pass.md`

**User review required**:
- None in steady state
- Conditional: severe compliance violation triggers Notification
- Conditional: high-severity adversarial finding requires your ack before auto-patch proceeds (per TK-09)

**Gate outcome**: All phase test plan + cross-feature integration + NFR tests pass + compliance clean + adversarial findings resolved → proceed to M3.

## 2.4 M3 Pre-Release Validation

**Trigger**: M2 complete; pre-release validation cycle invoked.

**Mapped tasks**: TK-10 (M3 cycle).

**Automated actions**:
- E2E test generation and execution via A2 at `apps/{app-slug}/tests/e2e/{flow}/**`
- Visual regression test via A2 at `apps/{app-slug}/tests/visual/{screen}/**` and review via A7 (visual-regression-reviewer), including Design System Governance compliance audit
- Basic response-time performance test via A2 at `apps/{app-slug}/tests/performance/{scenario}/**`
- Security scan via A8 (security-reviewer) if enabled for this slice

**Note on accessibility**: Per [RULE] DSG §6, HDC has no formal WCAG conformance target and no accessibility gate at any milestone. Routine a11y is covered by `eslint-plugin-jsx-a11y` at `warn` severity (per [MECH] Code Quality Rule Set §1.2) during M1. SK-W (`hdc-wcag-accessibility-checker`) remains available as an on-demand utility but is not part of M3 automation.

**User review required**:
- None in steady state
- Conditional: severe visual regression triggers Notification
- Conditional: security critical finding triggers Notification

**Gate outcome**:
- All validation pass: proceed to M4
- Fail: deliver RCA + recommendation; user decides

**Unit_type applicability**: M3 runs for all three unit types (`walking_skeleton`, `feature`, `app_integration`). For `feature` and `walking_skeleton` units, M3 covers slice-level E2E + visual + accessibility + performance against the slice's runnable artifacts. For `app_integration` units, the M3 target shifts to phase-level E2E (cross-feature flows already validated at §2.3.3 are extended to E2E rendering scope when Tier 1 is involved) + app-scale visual / accessibility / performance audits where the unit's deliverables introduced changes (e.g., app-scale NFR harness alters performance characteristics). Codex review does NOT fire at M3 for any unit type; per [RULE] Codex Plugin Usage, Codex review fires at M4 (TK-11).

### 2.4.1 Accessibility gate thresholds (M3)

| Severity | Blocking at M3 | Surfaced to user |
|---|---|---|
| Baseline critical | Yes | Yes (Notification + RCA) |
| Baseline serious | Yes | Yes (Notification + RCA) |
| Baseline moderate | No | Documented with remediation plan |
| Baseline minor | No | Documented (non-blocking) |
| Forward-compat (2.2 AA) findings | No | Documented (non-blocking; tracking) |
| Manual-validation-required items | No at M3 | Listed for M4 smoke test by user |

Manual-validation-required items from SK-W (criteria that cannot be fully automated, e.g., 1.3.1 semantic correctness, 1.4.5 images of text, 2.4.6 headings and labels) are listed in the audit report and surface to the user at M4 smoke test.

## 2.5 M4 Merge Decision

**Trigger**: All automated validation passed; evidence compilation invoked.

**Mapped tasks**: TK-11 (M4 preparation), TK-12 (M4 gate).

**Automated actions**:
- A4 (domain-judge) generates business-perspective AND user-experience candidate questions from evidence + acceptance + PRD + intent UX brief
- A9 (compliance-checker) final pass, including final Design System Governance compliance audit and app/domain placement audit per Architecture Rules §Y
- Invoke `/codex:review` for second-opinion code review; output at `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md`
- A10 (evidence-compiler) aggregates all artifacts into Test Evidence Report at `apps/{app-slug}/reports/m4/{slice-id}/test-evidence-report.md` (see §6 for structure) **and produces the operator-readable one-pager digest** at `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md` (see §6.4)
- Stop hook prevents Claude Code session from ending before both Test Evidence Report and operator digest are written

**Slice-size advisory at M4**:

If the slice exceeded the §2.7 soft upper limits (flagged at M2 per §2.3), the operator review at M4 is gated by an explicit ack — the operator either confirms acceptance of the oversized slice or returns the slice for split. The advisory cannot be silently bypassed.

**User review required**:
- Review **operator digest first** (one page, structured top-3 risks / spec deviations / coverage gaps / explicit no-significant-issues affirmation)
- Review Test Evidence Report sections of interest based on digest pointers
- Review Codex review output
- Review domain-judge questions (business AND UX perspectives)
- Execute smoke test personally
- If a Design System Governance update accompanied this slice: merge the update into CD SOT at this gate; the DS markdown export sync to both Hub mirror at `hdc_ref_design-system.md` and CC mirror at `specs/design-system.md` follows per DSG §12.5 + §12.7
- If §2.7 advisory flag is present: ack acceptance or return for split
- Merge go / no-go decision

**Gate outcome**:
- Go: merge to `main` directly, proceed to M5 staging deploy; Design System Governance update (if any) applied
- No-go: return specific issues to Claude Code for rework

A4 and A10 operate under `business_rules_only` context scope per [RULE] Claude Code Architecture Rules §X; they do not read `src/**` or `tests/**`.

**Unit_type applicability**: M4 runs for all three unit types (`walking_skeleton`, `feature`, `app_integration`). The merge-to-`main` step is uniform; the unit's PR is merged into `main` via the same TK-11 / TK-12 mechanics. Codex review (`/codex:review`) fires at M4 (TK-11) for all three unit types per [RULE] Codex Plugin Usage; for `app_integration` units, the M4 review target is the unit's PR diff including integration test code, scenario fixtures, and NFR harness rather than slice-level production code. For `walking_skeleton` units, M4 marks merge to `main`; the walking-skeleton-first ordering gate per [RULE] Workspace Topology §4.6.2 releases on successful M5 staging deploy completion (TK-13 success). Downstream `feature` and `app_integration` units in the same Phase 1 must wait until the walking_skeleton's TK-13 succeeds before starting their first node-side milestone.

### 2.5.1 M4 review scheduling: per-slice and batched modes

The TK-11 evidence compilation is fully automated; the operator review at TK-12 is a separate human-driven event whose scheduling is at operator discretion. Two scheduling modes are permitted; both preserve per-slice mechanism integrity (each slice retains its own Test Evidence Report, operator-digest, Codex review output, GitHub Issue, PR, merge action, and go/no-go decision).

**Per-slice mode**: operator reviews each slice's M4 evidence pack as it becomes available. One slice = one review session.

**Batched mode**: operator reviews multiple slices' M4 evidence packs in a single focused session. Batching is purely a review-scheduling decision; no slice's evidence is merged or commingled with another's.

**Batch trigger rule** (whichever fires first):
- **Volume**: 2–3 M3-green slices accumulated in the M4 queue, or
- **Time**: 48 hours elapsed since the oldest queued slice reached M3-green.

**Batch session caps**:
- ≤ 3 slices per session
- ≤ 90 minutes per session

If either cap would be exceeded, the operator splits the queue across multiple sessions. The 90-minute cap is grounded in attention-effectiveness research; per-slice net review time of 15–30 minutes implies 2–4 slices fit a focused session.

**Per-slice operator actions within a batch session**: for each slice in the batch, the operator executes the full TK-12 role sequence (review evidence → execute smoke test → issue go/no-go → conditional Spec merge → marker block update → execute merge to `main`). Slices may be approved, rejected, or held back individually; rejecting one slice does not affect others in the same batch.

**Merge order within a batch**: slices that share business or technical dependencies merge in dependency order; the slice-list (`apps/{app-slug}/specs/slice-list/{feature-slug}.md`) is the authoritative ordering source. Where no dependency exists, merge order is operator's discretion.

**Per-slice failure recovery**: any slice rejected at M4 returns to its specific TK per the §2.5 routing rules. The remaining slices in the batch proceed unaffected. Slice-level rollback granularity is preserved.

**Notification policy**: Notification hooks fire on TK-11 completion as in §2.5; the operator may defer review until the batch trigger rule fires. Hooks SHOULD support a queue-then-aggregate pattern (one summary Notification per batch threshold rather than per-TK-11-completion). Implementation lives in `.claude/hooks/notify.json` and is operator-configurable.

**Unit_type applicability**:
- `feature` units: batching applies when the unit produces multiple slices, and across feature units that share scheduling proximity.
- `walking_skeleton` units: single slice; batching N/A; per-slice mode applies.
- `app_integration` units: single PR per unit; batching applies only when multiple `app_integration` units across the same phase reach M3-green concurrently.

**M5 parallelism**: M5 staging deploy fires per merge to `main` per §2.6. When a batched M4 session approves multiple slices, each merge action triggers an independent M5 staging pipeline; these pipelines run concurrently in CI/CD as the existing default. No additional coordination is required.

**Mode selection guidance**:
- Use **per-slice mode** for: `walking_skeleton` execution, the first 1–2 slices of any new feature (pattern establishment), hotfixes, slices flagged by §2.7 slice-size advisory, security-sensitive changes, and any case where the operator judges single-slice attention warranted.
- Use **batched mode** for: steady-state feature execution after the pattern is established, low-risk slices, and high-volume scenarios where per-slice review would exceed sustainable operator cadence.

The choice is operator's per-occurrence discretion; no canonical commitment to either mode is recorded in the slice-list or TDD.

**v0 calibration note**: The thresholds (2–3 slice volume, 48 h time, 3-slice / 90-minute session caps) are starting heuristics drawn from review-effectiveness research and the per-slice TK-12 net-time estimate. The first 3–5 features will produce empirical evidence on operator capacity, cycle-time impact, and per-slice net review time; lessons-harvest may revise these numbers without triggering canonical revision (the numbers themselves are v0; the mechanism is canonical). This calibration discipline parallels §2.7 slice-size advisory thresholds.

## 2.6 M5 Staging Deploy

M5 is a single milestone — the AI-dev CI/CD chain's terminal gate. Production deployment is the receiving company's CI/CD scope after handoff per [MECH] Application Lifecycle Handoff §0.2; the AI-dev environment does not perform production deploys.

**Trigger**: PR merged to `main`.

**Mapped tasks**: TK-13 (staging deploy).

**Automated actions**:
- Deploy to staging environment via CI/CD on merge to `main`
- Staging smoke checks (basic health probes, smoke E2E if configured)

**User review required**: None for staging deploy.

**Gate outcome**:
- Staging deploy success: hold; staging environment available for operator's pre-release verification at the operator's discretion. M5 milestone closed for this slice / unit.
- Deploy failure: auto-rollback (revert the `main` branch state via revert commit) + Notification; operator decides next action (RCA, rework, or git-level revert).

**Walking_skeleton unit supplemental gate**: When the unit is `walking_skeleton` (Phase 1 only, per §2.0 milestone profile), the M5 gate is additionally constrained by all supplemental acceptance assertions declared in [MECH] Dev-Loopback Mode §6 (single-command full-stack startup, all-roles login, at least one complete business flow end-to-end, schema migration tool locked and working per §2.8.2). All assertions must pass at TK-13 for the walking_skeleton unit's M5 to complete. Failure on any §6 assertion routes through the standard staging failure path above. Paired per P-13.

**Walking-skeleton-first ordering gate release**: for a Phase 1 `walking_skeleton` unit, the walking-skeleton-first ordering gate per [RULE] Workspace Topology §4.6.2 releases at the moment the walking_skeleton's TK-13 staging deploy succeeds. From that point forward, downstream `feature` and `app_integration` units in the same Phase 1 may begin their first node-side milestone. The CI/CD pipeline establishment empirical assertion holds at the staging-deploy-success moment (architecture validated end-to-end through to staging on `main`).

**Boundary note — staging is not production**: A staging-deployed artifact is the AI-dev environment's terminal artifact. It is NOT a production release. Production deploy is performed by the receiving company's CI/CD after handoff per [MECH] Application Lifecycle Handoff §0.2 and is out of canonical scope. Communications referring to an AI-dev artifact as "released," "shipped," "live in production," or "in customer use" violate this boundary. This is reinforced by [MECH] Application Lifecycle Handoff §6.2 trigger phrase 3, which fires in Hub Claude conversations to prevent boundary drift.

**Unit_type applicability for M5**: M5 runs for all three unit types uniformly. There are no per-unit-type sub-stages.

**Why M5 ends at staging in the AI-dev environment**: AI-dev mimicry of enterprise DevOps ceremony exists to serve the multi-agent test architecture (M0 entry self-check, M1 unit-test auto-repair, M2 integration green, M3 pre-release multi-dimension validation, M4 cross-model Codex review). Production deploy ceremony (release tag, two-key authorization, production smoke) does not serve these test architecture goals; it serves enterprise release governance, which canonically belongs to the receiving company. Removing the M5-prod sub-stage and TK-16 / TK-17 from the AI-dev side reduces operator cognitive load without compromising the test architecture or the dev-loopback runnability contract. The receiving company's pipeline assumes responsibility for compilation, signing, SBOM, provenance, and production deploy from the handoff source state per [MECH] Application Lifecycle Handoff §3.1.

## 2.7 Slice-size advisory

To defend against the convergence-cliff failure mode in agentic coding (where codebases past a complexity threshold enter "fix one bug, break another" states), this source declares soft upper limits on per-slice scope.

**Soft upper limits (v0)**:

| Dimension | Soft limit |
|---|---|
| Source files touched (across `apps/{app-slug}/src/**` + `packages/domain/{domain-name}/src/**`) | ≤10 |
| Net lines of code added | ≤500 |

**Mechanism**:

- At M2 (TK-08): A9 compliance first-pass measures slice scope against limits; if either threshold is exceeded, the evidence carries a `slice-size-advisory: flagged` marker
- At M4 (TK-11 / TK-12): if the advisory marker is present, operator review is gated by explicit ack — accept-as-oversized or return-for-split

**Out of scope for this advisory**:
- Test code (does not count toward the source-file or LOC budgets)
- Generated code (e.g., openapi-generated client stubs) does not count if explicitly declared in the slice's TDD §2.5 as generated
- `specs/**` updates (these are not slice scope; they are upstream artifacts)

**Why soft, not hard**:

Some slices legitimately require >10 files or >500 LOC (e.g., introducing a new domain). The advisory is operator-judged at M4, not auto-blocking. The cost of misjudging is bounded: an oversized slice that the operator accepts continues; a split request loops back to TK-02 / TK-03.

> **v0 assumption — to be calibrated**: The thresholds (10 files / 500 LOC) are starting heuristics drawn from industry guidance on AI-coding diff-size discipline. The first 3–5 features will produce empirical evidence; lessons-harvest may revise these numbers without triggering canonical revision (the numbers themselves are v0; the mechanism is canonical).

---


---

## 2.8 Required artifact outputs across milestones

The milestone gates in §2.1–§2.6 govern test execution and PR merge approvals. This section defines a complementary requirement: specific **artifact outputs** that must accompany the milestone closure as required deliverables. Each gate below is binding — the milestone cannot close without the corresponding artifact present at the declared location.

The three gates exist to convert previously open-ended deferrals ("OpenAPI / migration plan / traceability matrix will be produced at some point") into milestone-bound contracts. Together they ensure that by the close of `app_integration` M2 in any phase, the phase's machine-readable contract surface, schema migration discipline, and requirement-to-test traceability are all in place.

### 2.8.1 OpenAPI YAML output gate

**Artifact**: `apps/{app-slug}/specs/openapi.yaml` — single app-scoped OpenAPI 3.x YAML, accumulated additively across phases per [MECH] Development Track Workflow §TK-02 Outputs. Each phase contributes new or modified BFF endpoints to the same file; phase-scope diff is computed against the prior phase's commit on `main`.

**Gate bindings**:

| Milestone | Required action | Failure to comply |
|---|---|---|
| `walking_skeleton` M2 (Phase 1 only) | Produce baseline `openapi.yaml` covering walking_skeleton's BFF endpoints (typically the single end-to-end read path that the walking_skeleton exercises). Phase 1 walking_skeleton establishes the file; subsequent phases extend it in place via `feature` slice M2 additions. | M2 cannot close. |
| Every `feature` slice M2 (when the slice introduces or modifies API surface) | Extend `openapi.yaml` in the same PR with the slice's new / modified endpoints, request/response schemas, and error envelope references. The slice's `evidence/{slice-id}/` directory must include `openapi-diff.md` listing the additions. | M2 cannot close. |
| Each `feature` unit's last-slice expanded M2 (§2.3.2) | Run an OpenAPI ↔ Pact consumer-contract consistency check: every Pact-contracted endpoint must appear in `openapi.yaml` and the schemas must agree on field names / types / required-ness. | Last-slice M2 cannot close. |
| `app_integration` M2 (§2.3.3) | Final OpenAPI ↔ Pact consistency check at phase scope (re-run across all feature units within this phase). | M2 cannot close. |

**Why this gate exists**: OpenAPI is the cross-language machine-readable contract — without it, downstream consumers (test code generators, client SDKs, mock servers) cannot operate. Pact captures consumer-driven examples but is not a complete schema; the two are complementary, and consistency must be verified at gates that align them.

**Out of scope**: Internal T3 Domain APIs (these use Pact provider-verification only). Public-facing API gateway concerns (those are deployment-stage, not Phase 1 scope).

### 2.8.2 Migration tooling output gate

**Artifact**:
- Migration tool selection (Flyway or Liquibase) declared in `apps/{app-slug}/HANDOFF.md` and applied to `apps/{app-slug}/db/migrations/**`
- Per-slice forward migration scripts (with reversible-rollback) committed as part of the slice that introduces the schema change

**Gate bindings**:

| Milestone | Required action | Failure to comply |
|---|---|---|
| `walking_skeleton` TK-06 (M1 → M2 transition) | Migration tool selection LOCKED. Selection recorded as a Decision Record in `apps/{app-slug}/specs/tdd/phase-{N}.md` §2.8. Rationale (Flyway vs Liquibase trade-off) documented. | M2 cannot start. |
| `walking_skeleton` M2 | First migration script working under `docker compose up` in dev-loopback (empty PG → all baseline tables created); migration script committed to `apps/{app-slug}/db/migrations/`. | M2 cannot close. |
| Every `feature` slice M2 (when the slice changes DB schema) | New migration script committed in the same PR. Migration must be **reversible** — a `down` script exists OR the `up` script is idempotent and the schema change can be rolled back via the chosen tool's mechanism. Slice evidence includes `migration-rollback-test.md`. | M2 cannot close. |
| `walking_skeleton` M5 | Migration runs successfully against the staging PG instance per [MECH] Dev-Loopback Mode §6.1 assertion #4. | M5 cannot close. |

**Why this gate exists**: A schema-heavy project without locked migration tooling is one engineer's exit away from migration chaos. The "TBD until walking_skeleton" path is correct (empirical decision after dev-loopback experience), but it must close at walking_skeleton M2 with a locked, evidenced choice — not stay open indefinitely.

**Out of scope**: Specific Flyway vs Liquibase choice is operator-judged based on walking_skeleton experience; this gate codifies only that **a** choice must be made by the deadline.

### 2.8.3 Traceability matrix output gate

**Artifact**: `apps/{app-slug}/specs/traceability/phase-{N}.md` — **auto-derived** matrix mapping FR → INV → API endpoint → T1/T2/T3 module → slice → test case.

**Gate binding**:

| Milestone | Required action | Failure to comply |
|---|---|---|
| `app_integration` M2 (§2.3.3) | A2 (or operator-judged tooling) runs the matrix-derivation script over inputs: (a) `apps/{app-slug}/specs/test-plan/**/*.yaml` (test case → FR mapping); (b) `apps/{app-slug}/specs/slice-list/*.md` (slice → FR / INV / API / module mapping); (c) `apps/{app-slug}/specs/intent/**/*.md` (slice → PRD scenario mapping). Output to `apps/{app-slug}/specs/traceability/phase-{N}.md`. Run completeness assertion: every FR listed in the PRD §7.2 Functional Requirement List must appear in at least one slice and have at least one test case. Any FR without coverage is flagged as a finding in `apps/{app-slug}/evidence/app-int-phase-{N}/traceability-findings.md`. | M2 cannot close while findings exist (resolution = update the underlying artifacts, then re-derive). |

**Why auto-derived, not manually authored**: Manually maintained traceability matrices drift the moment any input artifact changes. Auto-deriving from the existing machine-readable canonical artifacts (test-plan.yaml, slice-list.md, intent.md) ensures the matrix is always synchronized with reality and that drift produces immediate findings rather than silent rot.

**What this gate does NOT require**: Manual authorship of a matrix at any earlier milestone. The traceability data is present in the canonical input artifacts throughout development; the derived view is materialized once at app_integration M2.

**Out of scope**: Cross-phase traceability (Phase 1 FRs vs Phase 2 FRs). Each phase produces its own `phase-{N}.md` traceability matrix.

### 2.8.4 Cross-reference summary

The three gates land in the existing milestone structure as follows:

| Gate | Affects M2 (§2.3.1) | Affects M2 last-slice (§2.3.2) | Affects M2 app_integration (§2.3.3) | Affects M5 (§2.6) |
|---|---|---|---|---|
| §2.8.1 OpenAPI | ✓ extend per slice | ✓ Pact consistency check | ✓ phase-scope consistency | — |
| §2.8.2 Migration | ✓ per schema-change slice | — | — | ✓ staging PG run (via DLM §6.1 #4) |
| §2.8.3 Traceability | — | — | ✓ auto-derive + completeness check | — |

Operators reviewing milestone evidence should check this matrix to confirm which gates apply at the current milestone closure.

---

# 3. Milestone gating matrix

The base gating table below applies to `feature` and `walking_skeleton` units (slice-level execution path). The `app_integration` variant follows.

| Milestone | Mapped tasks | Automated | User gate | Codex action | Key agents | Escalation trigger |
|---|---|---|---|---|---|---|
| M0 Design Freeze | TK-04 entry self-check (folded into TK-04 start) + Hub TK-02 sign-off (TDD + Hub-authored UX Design Spec instance design freeze gate) + Hub TK-03 sign-off (per-slice spec design freeze gate) | Operator cross-model review reminder at Hub TK-02 sign-off; Operator GPT-Claude consensus loop at Hub TK-03 sign-off; CC mechanical entry self-check at TK-04 start | Required at Hub TK-02 + Hub TK-03; on-call at TK-04 self-check | — | — | Design conflicts surfacing in Hub cross-model review, or structural inconsistency at TK-04 self-check |
| M1 Feature Slice | TK-04–TK-07 | Code + unit + internal integration + auto-repair + RCA | None | — | CC, A1, A5, A6, SK-F | 3 auto-repair failures |
| M2 Integration Green (slice-level §2.3.1; last-slice expansion §2.3.2) | TK-08, TK-09 | Pact contract (consumer + producer) + external integration + adversarial loop + compliance first-pass + slice-size advisory check; **last slice of feature: + feature integration test execution** | None (conditional) | — | A2, A3, A9 | Compliance severe or high-severity adversarial |
| M3 Pre-Release | TK-10 | E2E + visual + accessibility + performance + (security) | None (conditional) | — | A2, A7, A8, SK-W | Visual regression, a11y baseline critical/serious, security critical |
| M4 Merge | TK-11, TK-12 | Domain judgement questions + compliance final + Codex review + evidence compilation + operator digest | Required (per-slice or batched per §2.5.1) | `/codex:review` | A4, A9, A10, CX | Slice-size advisory flagged for explicit ack |
| M5 Staging Deploy | TK-13 | Staging deploy on `main` merge; for Phase 1 walking_skeleton, successful TK-13 releases the walking-skeleton-first ordering gate per [RULE] Workspace Topology §4.6.2 | None | — | TOOL | Staging deploy failure |

`app_integration` unit gating matrix variant:

| Milestone | Mapped tasks | Automated | User gate | Codex action | Key agents | Escalation trigger |
|---|---|---|---|---|---|---|
| M0, M1 | — | not applicable per §2.0 | — | — | — | — |
| M2 Integration Green (variant §2.3.3) | TK-08, TK-09 | Phase test plan cross-feature scenarios + feature integration test cross-feature variants + app-scale NFR validation + adversarial loop + compliance first-pass | None (conditional) | — | A2, A3, A9 | Compliance severe or NFR threshold violation |
| M3 Pre-Release | TK-10 | Phase-level E2E + (visual / accessibility / performance variations where unit's deliverables introduced changes) | None (conditional) | — | A2, A7, A8, SK-W | Visual regression, a11y critical/serious, security critical |
| M4 Merge | TK-11, TK-12 | Compliance final + Codex review + evidence compilation + operator digest | Required (per-slice or batched per §2.5.1) | `/codex:review` (target: PR diff including test code, fixtures, NFR harness) | A4, A9, A10, CX | — |
| M5 Staging Deploy | TK-13 | Staging deploy on `main` merge | None | — | TOOL | Staging deploy failure |

---

# 4. Stuck recovery protocol

If Claude Code cannot resolve an issue within 3 attempts at any milestone:

1. First recovery attempt: `/codex:rescue investigate <issue>`
2. If Codex rescue also fails: Generate RCA report via A6, escalate to user
3. User decides: intervene directly, revise design, or accept limitation

Do not loop indefinitely. Escalation is the correct response after 3 failed attempts at the same issue.

---

# 5. Codex review gate default

Codex review gate default stance is governed by [RULE] Codex Plugin Usage §4. This source does not redefine that stance.

Milestone-side interaction point:
- When review gate is enabled per [RULE] Codex Plugin Usage §4.2, it interacts with the M1-M3 automation windows defined in §2, potentially creating review loops during autonomous work. Ensure the user-monitoring requirement in Codex §4.2 is satisfied before enabling.
- The "Codex review gate enabled without active monitoring" red-flag in §9 remains valid and applies regardless of which source owns the default stance.

---

# 6. Test Evidence Report content

**Terminology note**: The Test Evidence Report defined here is a **milestone-level aggregate artifact** assembled before M4 for user review. It is distinct from `evidence.md` referenced in [TPL] Intent and Acceptance Interface Writing Standard and [TPL] PRD + TDD to Intent and Acceptance Conversion Specification — `evidence.md` is a **feature-slice-scoped execution-side approval pack** for the AI virtual development team, generated after implementation and validation of a single `intent.md` / `acceptance.yaml` pair. The two artifacts operate at different granularity, serve different audiences, and should not be confused or conflated.

The operator digest in §6.4 is a third, distinct artifact: a one-page distillation of the Test Evidence Report for fast operator review at M4.

## 6.1 Position

- **Path**: `apps/{app-slug}/reports/m4/{slice-id}/test-evidence-report.md`
- **Producer**: A10 (evidence-compiler) in TK-11
- **Consumer**: Human owner at TK-12 M4 gate; input to merge go/no-go decision

## 6.2 Required sections

The report aggregates outputs from all upstream tasks. Required sections:

- **Slice identity**: slice_id, feature_slug, app_slug, TDD modules covered, tiers covered, Tier 1 involved flag
- **Unit and internal-integration test results** (from TK-05)
- **Contract and external-integration test results** (from TK-08), including Pact pair name `{app-slug}-bff_{domain-name}` and producer-verification status
- **Adversarial loop findings and resolutions** (from TK-09)
- **E2E test results with scenarios covered** (from TK-10)
- **Visual regression review** including Design System Governance compliance status (from TK-10 A7 output)
- **Performance test results** (from TK-10)
- **Security review** (from TK-10 A8 output, if enabled)
- **Compliance audit final pass** including Design System Governance compliance and app/domain placement (from TK-11 A9 output)
- **Codex review output** (from TK-11 CX)
- **Domain judgement questions** including business AND UX perspectives (from TK-11 A4)
- **Any auto-repaired unit test history** (from TK-06)
- **Any RCA reports generated during M1-M3** (from TK-07)
- **Context scope violations log** if any entries exist (from `.claude/config/context-scopes.yaml` enforcement)
- **Slice-size advisory status** (per §2.7): flagged or not; if flagged, the measured file count and net LOC
- **Known limitations or out-of-scope items**
- **Recommended smoke test focus areas for the user** (derived from manual-validation-required a11y items, severe findings, and flagged edge cases)

## 6.3 Purpose

Enable the user to make the M4 merge decision without reading code line-by-line. The report is the single integration point where evidence from 13 upstream tasks converges into one approval-ready document.

## 6.4 Operator digest one-pager

The Test Evidence Report (§6.1–§6.3) is comprehensive. To bound operator review time, A10 also produces a one-page operator-readable digest that distills the report's findings into a fixed structure.

- **Path**: `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md`
- **Producer**: A10 (evidence-compiler) in TK-11, generated alongside the Test Evidence Report
- **Consumer**: Human owner at TK-12 M4 gate; **read first, before the full Test Evidence Report**
- **Length cap**: one printed page (approximately 400–500 words; the cap is on substance, not strict word count)

**Required structure** (in this order):

1. **Top-3 risk flags**: the three highest-impact risks identified across the slice's evidence chain. Each entry: severity (`critical` / `high` / `medium`), risk statement (≤30 words), pointer to the Test Evidence Report section that supports the flag. If fewer than three risks rise to flag-worthy, list as many as exist; do not pad.
2. **Deviations from spec**: any place where implementation diverges from PRD / TDD / intent / acceptance contracts, regardless of whether the deviation passed tests. Each entry: brief statement (≤30 words), spec source, evidence pointer.
3. **Test-plan coverage gaps**: cases where the test plan acknowledges a non-covered area (e.g., a deferred edge case, an out-of-scope scenario, a manual-validation-required item not yet validated). Each entry: brief statement (≤30 words), test-plan reference.
4. **No-significant-issues affirmation**: when none of the above sections has entries, A10 writes an explicit affirmation: "No significant risks, deviations, or coverage gaps identified for this slice." The affirmation is mandatory when applicable; an empty digest is not acceptable.

**Why required**:

The digest is the operator's primary decision input at M4. The full Test Evidence Report is reference material the operator consults from the digest's pointers, not the document the operator reads end-to-end. This concentrates the M4 review time on the operator's actual decision (go / no-go on merge) rather than on raw evidence parsing.

> **v0 assumption — to be calibrated**: The fixed structure (top-3 / deviations / coverage-gaps / affirmation) and the one-page cap are starting heuristics. After the first 3–5 features, lessons-harvest may revise the structure (e.g., add a "lessons" section if recurring patterns emerge) without triggering canonical revision of the mechanism itself.

---

# 7. Performance testing scope

Default performance testing scope for Cat 4 projects:

| Type | In Scope | Out of Scope |
|---|---|---|
| Basic response time | ✓ | — |
| Load testing (low concurrency) | ✓ when user volume justifies | — |
| Stress testing | — | Delegate to dedicated environment |
| Capacity planning | — | Delegate to dedicated environment |

Reason: Claude Code sandbox environment is not suited for high-stress testing. Basic response time is sufficient for most HR system workloads.

---

# 8. Anti-drift for milestone policy

> **Scope**: this section enumerates **CI/CD-milestone-specific** anti-drift red flags (user review budget, execution loop hygiene, tooling baseline, slice-size advisory, TER and operator digest integrity, boundary discipline) and **milestone-gate local variants** of cross-cutting red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced rather than duplicated. See [RULE] Claude Platform Behavior §5 for the full anti-drift ownership index.

Red flags that should trigger correction:

**User review budget drift** (CI/CD-specific):
- User being asked for review between M0 and M4 outside the explicit conditional-escalation channels in §2
- M4 merge without Test Evidence Report
- M4 merge without operator digest (§6.4) read first

**Execution loop hygiene** (CI/CD-specific):
- Codex review gate enabled without active monitoring
- Auto-repair loops exceeding 3 attempts
- Stuck recovery protocol skipped (Claude Code looping without escalation)
- Milestone skipping (e.g., M2 to M4) without documented justification

**Tooling baseline drift** (CI/CD-specific — Claude Code version, distinct from [RULE] WT §7 Node/Java/pnpm tool stack):
- Development Track work proceeding on a Claude Code version below the baseline
- Version upgrade adopted without the §1.1 verification slice procedure
- Multiple nodes running divergent Claude Code versions during a feature's M0 → M5 chain

**Multi-node evidence parity drift** (milestone-gate local view — `Subagent definitions diverging across nodes` is canonical at [RULE] WT §7):
- Milestone gate decision discriminating evidence by which node produced it
- Operator review requiring physical-node verification beyond the GitHub Issue marker block

**AI-dev / company-side boundary drift** (CI/CD-specific, per §2.6):
- AI-dev staging artifact communicated as "released," "shipped," "in production," or "live in customer use" (violates §2.6 boundary note; staging is the AI-dev terminal artifact, not production)
- Release tags created in the AI-dev monorepo (AI-dev produces no release tags per §2.6; only handoff tags per [MECH] Application Lifecycle Handoff §4.1 are canonical)
- Production deployment attempted from the AI-dev environment (production deploy is the receiving company's CI/CD scope after handoff per [MECH] Application Lifecycle Handoff §0.2)
- Reintroduction of M5-prod, TK-16, TK-17, or two-substage M5 architecture without canonical revision authorizing it (the single-M5 staging-only design declared in §2.6 is the canonical default per the harness's "AI-dev → staging; company → production" boundary)

**Slice-size advisory drift** (CI/CD-specific, per §2.7):
- Slice-size advisory flag silently ignored at M4 (must be explicitly ack'd or returned for split)
- Test code or generated code counted toward the source-file or LOC budgets (per §2.7 out-of-scope)
- Soft limits applied as hard blocks at M2 (the advisory surfaces at M4, not M2)

**Agent scope and skill loading** (milestone-gate local view — canonical statement at [RULE] CCAR §8 + §Z.5):
- Agents in §2 operating outside their declared context scope per [RULE] Claude Code Architecture Rules §X (milestone-gate detection point: agent invocations during TK execution)
- SK-F not active during TK-04 Tier 1 code writing (the TK-04 milestone-gate instance of skill-loading drift; canonical owner [RULE] CCAR §Z.5)
- SK-W not active during TK-10 accessibility phase for Tier 1 slices (TK-10 milestone-gate instance; SK-W is on-demand only per DSG §6.3, so this fires only when slice has explicit a11y scope)
- Compliance-checker (A9) first-pass or final pass not auditing Design System Governance compliance when Tier 1 is involved
- Compliance-checker (A9) not auditing app/domain placement per Architecture Rules §Y

**Test Evidence Report integrity** (CI/CD-specific):
- Test Evidence Report produced without domain-judge-questions when Tier 1 is involved
- Test Evidence Report produced without Design System Governance compliance audit section when Tier 1 is involved
- Test Evidence Report produced without Pact pair status when M2 contract testing was applicable
- Test Evidence Report produced without slice-size advisory status (§6.2 required section)

**Operator digest integrity** (CI/CD-specific, per §6.4):
- Operator digest empty when none of the structured sections applies (must include explicit no-significant-issues affirmation)
- Operator digest exceeding one-page substance (cap on content, not strict word count)
- Operator digest skipped during M4; full Test Evidence Report read end-to-end as substitute (the digest is a bounded-time mechanism, not optional)

**Accessibility scope integrity**: see [RULE] Design System Governance §12 governance for the canonical inverse-drift red flag (formal a11y CI gate / merge-block introduced at any milestone without DSG §12 approval). DSG §6 stance is "no formal a11y gate"; SK-W is on-demand only.

**Design System distribution and mirror lock-step drift** (CI/CD-specific, per [RULE] DSG §13 three-way distribution model):
- TK-04 entry self-check failing to verify lock-step version match between the UX Design Spec instance header DS version and the current CC mirror version (per the lock-step sync discipline in DSG §12.5 + §12.7)
- TK-04 entry self-check flagging `hdc_ref_design-system.md` as a "retired path" (this Hub mirror is reintroduced under the revised three-way distribution model; only `specs/design-system-changes/` and `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` remain retired paths)
- M4 merge proceeding with a Design System Governance additive update plan that has not been synced to both Hub mirror at `hdc_ref_design-system.md` AND CC mirror at `specs/design-system.md` per DSG §12.7 (single-mirror sync is incomplete and creates dual-mirror version drift)
- TK-02 Step 2.3 UX Design Spec instance authoring proceeding when the Hub mirror at `hdc_ref_design-system.md` is absent or empty (Hub Claude has no spec-time DS grounding; surface as a workspace-inception gap per [RULE] Workspace Topology §10)
- Reference to retired UX bundle path `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` in any CC-side artifact or evidence file (replaced by Hub-authored UX Design Spec instance markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` per the TK-02 Step 2.3 flip)
