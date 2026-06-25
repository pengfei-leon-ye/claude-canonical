# [MECH] CI/CD Milestone Policy

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable declaration of the M0–M4 milestone ladder used in Claude Code development: the existence and identity of each gate, the per-unit-type milestone profile (which `unit_type` runs which gate subset), the Test Evidence Report interface contract (the handoff artifact schema consumed by the operator at M4), the required artifact outputs that constitute the cross-workspace interface, and the multi-node evidence parity invariant. Substantive gate criteria (specific tools, thresholds, tooling baselines, accessibility thresholds, performance scopes, anti-drift signals at the operational level) are owned by CC under its own substantive canonical.
- **Source Category**: Cat 4
- **Management-System Role**: Governance mechanism specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Supports the Orchestrate loop by codifying the review-gating mechanism. Subject to [OS] §8.5 paired-update consistency. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side residue carries the constitutional skeleton declared here; CC-side substantive canonical owns the gate criteria and operational details.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §5 (management mechanism over ad hoc control) to milestone gating design; §6 (operation management and value realization by design) to the M0–M4 sequence as a managed sequence rather than ad-hoc checkpoints.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary. CI/CD milestone gating is a CC-side mechanism; this Hub residue declares the cross-workspace interface that handoff documentation consumes.
- **Relationship to [RULE] Workspace Topology**: Co-governing. §1.2 multi-node evidence parity in this residue anchors WT's parity discipline. WT's walking-skeleton-first ordering rule defers downstream-unit milestone entry per §2 below.
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. The contract testing convention referenced at M2 (gate criteria substantive at CC) anchors CCAR's Pact contract testing rules at CC substantive layer.
- **Relationship to [MECH] Development Track Workflow**: Companion. The M-gates are the milestone semantics that DTW's TK chain triggers and consumes; M0–M4 identity declared here is referenced by DTW's TK chain for milestone-to-task anchoring.
- **Relationship to [MECH] Application Lifecycle Handoff**: The AI-dev CI/CD pipeline produces no release tags; release tag namespaces belong to the receiving company's CI/CD scope. The handoff tag namespace (Handoff §4.1) is the only canonical-recognized tag namespace in the AI-dev monorepo. This is a constitutional invariant.
- **Relationship to [RULE] Design System Governance**: M3 visual review references DSG consistency at the substantive layer (specific check criteria at CC substantive). No accessibility gate at any milestone (per DSG §6 stance) is a constitutional invariant. DS instance two-way distribution per DSG §1.1 governs DS consumption — at TK-02 Step 2.3, CC synthesizes the UX Design Spec (at phase-level and per-feature granularities) in a session firewalled from the implementing context, grounded in PRD/TDD by default; a CD-authored design file is consulted only as on-demand visual reference on genuine visual novelty. The CC mirror is consulted at TK-04+ via skill enforcement.
- **Relationship to [TPL] Intent and Acceptance Interface Writing Standard** + **[TPL] PRD + TDD to Intent and Acceptance Conversion Specification**: §3 below owns the disambiguation between milestone-level Test Evidence Report (constitutional schema declared here) and feature-slice-scoped `evidence.md` (substantive content at CC).
- **Relationship to [TPL] Test Plan YAML Schema**: The evidence digest contract for the operator one-pager schema in §3.3 binds to that template's `evidence_required` field as a constitutional interface.
- **Pairings I participate in**: P-03 (with [MECH] DTW §4 TK chain — milestone-to-task anchoring at constitutional interface). Pre-split pairings P-01 / P-09 / P-13 / P-32 / P-49 are retired at this Hub residue level; their substantive obligations migrate to CC under CC substantive CI/CD canonical.

## How to use this source (Hub-side)

Use this source when:
- Authoring Hub-side handoff documentation that references M-gate names or the Test Evidence Report schema
- Verifying that a Hub-authored test plan aligns with the Test Evidence Report's required sections
- Reasoning about which milestones apply to which unit_type for cross-workspace sequencing
- Confirming the multi-node evidence parity invariant when consuming evidence at handoff

Do not use this source as:
- A gate criteria reference (specific tool checks, thresholds — CC substantive)
- A tooling baseline reference (specific Claude Code CLI version — CC substantive)
- A slice-size advisory reference (CC substantive)
- A stuck recovery protocol reference (CC substantive)
- A performance testing scope reference (CC substantive)
- An anti-drift signal reference at the operational level (CC substantive; cross-workspace anti-drift in §5 below)

---

# 0. Boundary and position

## 0.1 What this source owns (constitutional)

- The existence and identity of M0–M4 as a 5-gate milestone ladder (§2 below)
- Per-unit-type milestone profile (§2.7): which gates apply to which `unit_type` — this is the interface contract consumed by cross-workspace handoff sequencing
- Test Evidence Report interface contract: required sections schema (§3.2) — the artifact schema consumed by the operator at the M4 gate
- Operator digest one-pager interface (§3.3) — fixed-structure schema declared as constitutional interface
- Required artifact outputs across milestones (§4): openapi.yaml gate, migration tooling gate, traceability matrix gate — constitutional handoff interfaces
- Multi-node evidence parity invariant (§1.2)
- Walking-skeleton-first ordering deference (constitutional connection to [RULE] WT residue §3)
- Cross-workspace anti-drift signals (§5)

## 0.2 What this source does not own

- Specific gate criteria for each M-N (tool runs, threshold values, pass/fail logic — CC substantive)
- Tooling baseline (specific Claude Code CLI version — CC substantive)
- M2 sub-scopes (standard slice-level scope, last-slice expansion, app_integration variant — CC substantive)
- Accessibility gate thresholds at M3 (CC substantive)
- M4 review scheduling modes (per-slice and batched — CC substantive)
- Slice-size advisory thresholds (CC substantive)
- Stuck recovery protocol (CC substantive)
- Code review gate operational specifics (the gate's existence is constitutional in §2.5; the tool used to perform the review is CC substantive — historically Codex, governed by CC's own canonical)
- Performance testing scope details (CC substantive)
- Anti-drift signals at the operational level (CC substantive; cross-workspace anti-drift only in §5)

## 0.3 Position relative to DTW and Handoff

| Adjacent source | Relationship |
|---|---|
| [MECH] Development Track Workflow | Companion. DTW's TK chain triggers and consumes M-gates declared here; the TK-to-M anchoring is constitutional interface |
| [MECH] Application Lifecycle Handoff | The AI-dev CI/CD pipeline terminates at M4 (merge to `main`); deployment to staging and production is the receiving company's CI/CD scope after handoff. Tag namespace separation is constitutional invariant |
| [REF] Hub-CD-CC Architecture | M-gates execute in CC workspace; this Hub residue is the cross-workspace interface declaration |
| [RULE] Workspace Topology | Multi-node evidence parity (§1.2) + walking-skeleton-first ordering deference |

---

# 1. Core principle

## 1.1 Existence of the M-gate ladder

A 5-gate milestone ladder (M0 → M4) gates Claude Code development work between autonomous AI execution and operator review checkpoints. Each gate has a constitutional identity declared in §2 below. The specific criteria for passing each gate are CC substantive content.

The milestone ladder is the **review-gating mechanism**: it defines where operator review is required versus where the AI works autonomously. The constitutional invariant is that the ladder exists; specific criteria are CC-owned.

## 1.2 Multi-node evidence parity

M-state evidence is **node-neutral**: any node defined in [RULE] Workspace Topology (constitutional residue §1) may produce M-evidence; the originating node is recorded for traceability but does not affect gate validation logic. This is a constitutional invariant — Hub-side handoff documentation relies on this property when consuming evidence from any node.

Per-milestone evidence durably persists at a declared repository path (`apps/{app-slug}/evidence/{slice-id}/**`) so that a fresh downstream actor at a later gate can read every upstream gate's output without relying on cross-session state. This is a constitutional invariant; the per-gate file layout under that path is owned by the CC substantive CI/CD canonical.

---

# 2. Milestone ladder — constitutional identity

Each M-gate has a constitutional identity (purpose, position in the ladder, cross-workspace consequence). Specific gate criteria are CC substantive.

## 2.1 M0 Design Freeze

**Identity**: Per-slice readiness gate. The slice's PRD/TDD coherence anchor (Hub-authored, relatively stable) is settled, and the slice's detailed spec (intent, acceptance, test plan — CC-authored just-ahead-of-code in a firewalled session per the incremental JIT model) is in place for the slice about to be implemented. Downstream tasks (M1+) execute against this anchored, slice-scoped spec.

**Cross-workspace consequence**: M0 marks the boundary between an implementing context and the spec it builds against. The detailed spec is a CC-maintained living artifact, not a frozen document: mid-flight changes are permitted but must be operator-authorized, versioned, and reasoned (not silent). PRD/TDD changes propagate from the Hub coherence anchor. Code is the ultimate SOT for app behavior; the detailed spec is living documentation plus the acceptance record.

**Substantive details (at CC)**: M0 entry self-check is folded into TK-04 per CC substantive DTW; specific self-check criteria are CC substantive.

## 2.2 M1 Feature Slice Complete

**Identity**: Feature slice implementation complete at the code level. Implementation passes unit and internal-integration tests.

**Cross-workspace consequence**: After M1, the slice can proceed to integration testing (M2). Hub-side handoff documentation can rely on M1-passed slices as having implementation completeness.

**Substantive details (at CC)**: Specific tool runs (unit test suite execution, lint, type check) are CC substantive.

## 2.3 M2 Integration Green

**Identity**: Cross-component integration validation passed. Contract testing between BFF and domain validated; external-integration tests passed.

**Cross-workspace consequence**: After M2, the slice's cross-component contracts are validated. Walking-skeleton M2 has special significance: passing it empirically asserts the CI/CD pipeline is established for the app per WT walking-skeleton-first ordering rule.

**Substantive details (at CC)**: Standard slice-level scope, last-slice expansion (feature unit only), and app_integration unit variant — all CC substantive.

## 2.4 M3 Pre-Release Validation

**Identity**: Pre-release validation. End-to-end tests, visual regression review, performance tests, security review (when applicable), compliance audit.

**Cross-workspace consequence**: After M3, the slice is release-candidate quality. M3 evidence feeds the Test Evidence Report consumed at M4.

**Substantive details (at CC)**: Accessibility gate thresholds, visual regression check criteria, specific tool runs at M3 — all CC substantive. No accessibility gate at any milestone is a constitutional invariant per [RULE] DSG §6 stance.

## 2.5 M4 Merge Decision (terminal)

**Identity**: User-review merge gate, and terminal milestone in the AI-dev CI/CD chain. The operator reviews the Test Evidence Report (and operator digest one-pager) and decides go/no-go on merging the slice to `main`. A code review gate executes before the operator decision. Successful merge to `main` (`status: merged`) ends the slice's milestone progression on the AI-dev side; subsequent deployment (staging, production) is the receiving company's CI/CD responsibility per [MECH] Application Lifecycle Handoff §0.2 and is out of AI-dev CI/CD scope.

**Cross-workspace consequence**: M4 is the constitutional **user-review checkpoint**: the AI does not auto-merge; the operator's decision is required. The code review gate (its existence) is constitutional; the specific tool used (historically Codex, governed by CC substantive canonical) is CC substantive. For Phase 1 `walking_skeleton` units, successful M4 (`status: merged`) releases the walking-skeleton-first ordering gate per [RULE] Workspace Topology constitutional residue §3; downstream `feature` and `app_integration` units in the same Phase 1 may then begin their first node-side milestone.

**Substantive details (at CC)**: Per-slice and batched review scheduling modes, the specific code review tool invocation, walking-skeleton dev-loopback acceptance assertions (additional pre-merge check for `walking_skeleton` units only) — all CC substantive.

## 2.6 Per-unit-type milestone profile (interface contract)

Three node-level work unit types (`walking_skeleton`, `feature`, `app_integration`) catalogued in [MECH] Development Track Workflow run different subsets of M0–M4. The profile is constitutional interface:

| Unit type | Milestone path | Notes |
|---|---|---|
| `walking_skeleton` (Phase 1 only, exactly 1 slice) | M0 → M1 → M2 → M3 → M4 (full chain) | M4 (`status: merged`) completion releases the walking-skeleton-first gate for downstream Phase 1 units. Walking-skeleton-specific dev-loopback acceptance assertions run at M4 pre-merge (substantive at CC) |
| `feature` (any phase, 1+ slices) | Per slice: M0 → M1 → M2 → M3 → M4 (full chain) | The **last slice** of a feature runs an **expanded M2 scope** (substantive details at CC) |
| `app_integration` (any phase, 0 customer-facing slices) | M2 → M3 → M4 (truncated; no M0 / M1) | Single PR per unit. M2 entry scope shift to phase-level test plans (substantive at CC) |

Walking-skeleton-first ordering (per [RULE] Workspace Topology constitutional residue §3): in Phase 1, no `feature` unit's M0 and no `app_integration` unit's M2 entry can begin until the Phase 1 `walking_skeleton` unit reaches `status: merged` on `main`. Hub-side PRD/TDD specification work MAY proceed in parallel; the gate is the unit's first node-side milestone, not the Hub-side PRD/TDD specification work.

---

# 3. Test Evidence Report (handoff interface contract)

The Test Evidence Report is the constitutional **handoff interface artifact** consumed by the operator at the M4 gate. Its schema is constitutional; its content authoring (by the CC Test Evidence Report producer subagent, per CC substantive canonical) is substantive.

**Terminology note**: The Test Evidence Report is a **milestone-level aggregate artifact** assembled before M4 for operator review. It is distinct from `evidence.md` referenced in [TPL] Intent and Acceptance Interface Writing Standard and [TPL] PRD + TDD to Intent and Acceptance Conversion Specification — `evidence.md` is a **feature-slice-scoped execution-side approval pack** for the AI virtual development team. The two artifacts operate at different granularity, serve different audiences, and should not be confused or conflated.

## 3.1 Position (constitutional)

- **Path**: `apps/{app-slug}/reports/m4/{slice-id}/test-evidence-report.md`
- **Consumer**: Human operator at M4 gate; input to merge go/no-go decision

The producer identity (the specific CC subagent) is CC substantive content; the path and consumer role are constitutional interface.

## 3.2 Required sections (constitutional schema)

The report aggregates outputs from all upstream tasks. Required sections (constitutional handoff contract):

- **Slice identity**: slice_id, feature_slug, app_slug, TDD modules covered, tiers covered, Tier 1 involved flag
- **Unit and internal-integration test results**
- **Contract and external-integration test results**, including Pact pair name `{app-slug}-bff_{domain-name}` and producer-verification status
- **Adversarial loop findings and resolutions**
- **E2E test results with scenarios covered**
- **Visual regression review** including Design System Governance compliance status
- **Performance test results**
- **Security review** (if enabled)
- **Compliance audit final pass** including Design System Governance compliance and app/domain placement
- **Code review output** (the substantive code review tool — historically Codex — is CC-owned)
- **Domain judgement questions** including business AND UX perspectives
- **Any auto-repaired unit test history**
- **Any RCA reports generated during M1-M3**
- **Context scope violations log** if any entries exist
- **Slice-size advisory status**: flagged or not; if flagged, the measured file count and net LOC
- **Known limitations or out-of-scope items**
- **Recommended smoke test focus areas for the operator**
- **Gate operationality status**: per milestone gate, whether its checks were *machine-verified* (ran via the sensor bus and passed), *manual-substitute* (a stand-in for an unwired check, with the substitute recorded), or *not-operational* (could not run). A not-operational quality gate is never reported as a clean pass
- **Controller-health summary** (when the CC closed-loop adversarial control model is in effect): adversarial-loop convergence (rounds; what the adversary stopped finding), auto-resolution outcomes, and the triaged escalation set

CC substantive canonical owns the upstream task identifiers (TK-NN) that produce each section's content. The gate-operationality taxonomy and the controller-health metrics are CC-substantive; their presence in this schema is the constitutional interface.

## 3.3 Operator digest one-pager (constitutional schema)

The Test Evidence Report's complementary one-page digest is also constitutional handoff interface:

- **Path**: `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md`
- **Consumer**: Human operator at M4 gate; **read first, before the full Test Evidence Report**
- **Length cap**: one printed page (approximately 400–500 words; cap is on substance, not strict word count)

**Required structure** (constitutional, in this order):

1. **Top-3 risk flags**: severity (`critical` / `high` / `medium`), risk statement (≤30 words), pointer to the Test Evidence Report section. When more than three risks reach `critical` or `high`, the digest lists the three highest-severity risks here and adds a one-line pointer to the Test Evidence Report section that enumerates the remainder — the digest is not expanded beyond three flags
2. **Deviations from spec**: any place where implementation diverges from PRD / TDD / intent / acceptance contracts, regardless of whether the deviation passed tests
3. **Test-plan coverage gaps**: cases where the test plan acknowledges a non-covered area
4. **Gate-operationality line**: one line of per-gate status (machine-verified / manual-substitute / not-operational); a not-operational quality gate must also appear in the top-3 risk flags
5. **Controller-health one-liner** (when the CC closed-loop adversarial control model is in effect): converged in N adversarial rounds / open escalations
6. **No-significant-issues affirmation**: explicit affirmation when none of the above sections has entries; mandatory when applicable

**Purpose**: The digest is the operator's primary decision input at M4. The full Test Evidence Report is reference material the operator consults from the digest's pointers, not the document the operator reads end-to-end.

> **v0 assumption — to be calibrated**: The fixed structure (top-3 / deviations / coverage-gaps / affirmation) and the one-page cap are starting heuristics. After the first 3–5 features, lessons-harvest may revise the structure (e.g., add a "lessons" section if recurring patterns emerge) without triggering canonical revision of the mechanism itself.

---

# 4. Required artifact outputs across milestones (constitutional interface)

Certain artifact outputs are constitutional **handoff interface** — produced at specific milestones and consumed by Hub-side or downstream-workspace artifacts. Their existence and producer-consumer roles are constitutional; their specific format and validation criteria are substantive (CC or template).

## 4.1 OpenAPI YAML output gate

- **Produced at**: M2 (last slice of a feature or app_integration unit)
- **Path**: `apps/{app-slug}/specs/openapi.yaml`
- **Consumer**: Pact contract testing harness; cross-workspace contract artifact

## 4.2 Migration tooling output gate

- **Produced at**: M2 (when database migrations are introduced)
- **Path**: per CC substantive canonical
- **Consumer**: Production deploy at receiving team's CI/CD post-handoff

## 4.3 Traceability matrix output gate

- **Produced at**: M3
- **Path**: `apps/{app-slug}/reports/m4/{slice-id}/traceability-matrix.md` (or equivalent per CC substantive canonical)
- **Consumer**: Operator at M4 review; auditor

---

# 5. Anti-drift for milestone policy (cross-workspace)

Violations of the §2–§4 constitutional invariants are cross-workspace anti-drift signals per [OS] §12.

In-CC operational anti-drift signals (gate criterion drift, threshold drift, tooling drift, slice-size violations, performance test scope drift, code review timing drift) are governed by CC substantive CI/CD canonical.
