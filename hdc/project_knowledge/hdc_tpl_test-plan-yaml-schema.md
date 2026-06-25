# [TPL] Test Plan YAML Schema (Feature integration yaml · Slice yaml)

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable schema and writing standard for the two yaml tiers of the test plan three-tier ontology: (a) `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` — feature-level integration test plan covering cross-slice flow scenarios within a single feature; (b) `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` — per-slice test design consumable by AI test-writer agents under bias firewall and context isolation constraints. The third tier (phase-level master markdown at `apps/{app-slug}/specs/test-plan/phase-{N}.md`) is authored per [TPL] Phase Test Plan.
- **Source Category**: Cat 4
- **Management-System Role**: Specification-support template; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Supports the Specify loop by adding three test-design layers between phase PRD/TDD and test code execution. Grounded in [OS] §0.1 project-level operating premises and [OS] §0.2 Cat 4 role anchor.
- **Relationship to [PRIN]**: Applies §5 management mechanism over ad hoc control to test design governance and §10 MECE decomposition to test type and tier partitioning
- **Relationship to [MECH] Development Track Workflow**: Phase test plan (master) is produced in TK-02 alongside the phase TDD (master is human-authored per [TPL] Phase Test Plan); feature integration test plans are authored at the detailed-spec layer in CC; per-slice test plans are authored in TK-03 in the CC firewalled acceptance/intent authoring session (S2), firewalled from the implementing session (S3) per [MECH] DTW §4 TK-03 + [TPL] Writing Standard §1.11, and referenced by TK-06, TK-09, TK-10, TK-11 (test-writer agents and adversarial loop). When Tier 1 is involved, the CC-authored UX Design Spec instance — synthesized in the CC UX-spec synthesis session (S1) at TK-02.3 — is consumed in the S2 acceptance/intent session as the source for accessibility test case authoring; SK-F loads on the assigned_node CC at TK-04 onwards for code generation, not at TK-03 test-plan authoring time
- **Relationship to [RULE] Claude Code Architecture Rules**: The `context_scope` field in the slice tier binds each test case to a specific subagent per the context-scope policy; repository path layout (`apps/{app-slug}/specs/test-plan/`, `apps/{app-slug}/tests/`, `apps/{app-slug}/evidence/`); and the consumer-driven Pact pair convention `{app-slug}-bff_{domain-name}` — the substantive detail for all three is owned by the CC-side substantive canonical
- **Relationship to [MECH] CI/CD Milestone Policy**: Test types declared at the slice tier map onto milestones defined in that source (§2.2 M1 unit/internal-integration; §2.3 M2 contract/external-integration; §2.4 M3 e2e/visual/performance); phase exit criteria in the phase test plan map onto Milestone Policy §2.5–§2.6; Pact contract pairing semantics owned by Milestone Policy §2.3. **Accessibility is not a milestone-gated test type** per [RULE] DSG §6 (no formal a11y gate at any milestone)
- **Relationship to CC substantive Codex Plugin Usage canonical (post-Phase-3 migration)**: Code review tool review at TK-12 (formerly governed by Hub `[RULE] Codex Plugin Usage`, now CC substantive) references slice test plans for context (e.g., confirming code matches the test cases declared); the code review tool does not author or adversarially review test plans. Adversarial review of test plan content is owned by the M0 operator review at TK-04 and by adversarial-tester subagent A3 at TK-10 (M2 adversarial loop).
- **Relationship to [RULE] Design System Governance**: Accessibility test cases (`test_type: accessibility`) are **optional** at the slice tier per [RULE] DSG §6 (HDC has no formal WCAG conformance target). When present, such cases describe slice-specific a11y concerns in plain terms, not WCAG criteria. The `hdc-wcag-accessibility-checker` skill (SK-W) is an on-demand utility per DSG §6.3 and is not auto-invoked by these cases.
- **Relationship to adjacent [TPL] sources**:
  - `[TPL] Phase Test Plan` — companion. Owns the phase-level markdown master (`apps/{app-slug}/specs/test-plan/phase-{N}.md`). This source no longer authors the phase tier; phase test plans cross-reference the feature integration yaml plans owned here.
  - Downstream of `[TPL] Technical Design Document Template` — the phase TDD's §2 phase-level testing strategy drives the phase test plan (master, owned by [TPL] Phase Test Plan); per-feature §4.{feature-slug} content drives the feature integration test plan (owned here); per-feature §4.{feature-slug}.Module-Decomposition plus the slice's acceptance and (when Tier 1 involved) the feature's CC-authored UX Design Spec instance per `[TPL] UX Design Spec` drive the slice test plan (owned here)
  - Downstream of `[TPL] Intent and Acceptance Interface Writing Standard` — slice acceptance.yaml provides scenarios to trace at the slice tier; `evidence_required` default set including `operator_digest` is owned there
  - Downstream of `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification` — TK-03 conversion mechanics for the slice tier
- **Pairings I participate in**: P-07 (with [TPL] Technical Design Document Template; the pairing covers all three test-plan tiers per [OS] §8.5.2)

## How to use this source

Use this source when:
- Producing the phase test plan (master, markdown) in TK-02 of the Development Track Workflow
- Producing each feature integration test plan (yaml) in TK-02
- Producing the per-slice test plan (yaml) in TK-03
- Reviewing whether any of the three test plan tiers is ready for downstream consumption
- Designing new test-writer subagents that consume the slice test plan
- Debugging test coverage gaps by tracing scenarios across the three tiers

Do not use this source as:
- A test execution framework specification
- A test case content guide (that is domain-specific)
- A substitute for slice acceptance.yaml
- A repository-path-layout reference (CC substantive Claude Code Architecture Rules canonical (repository layout))
- A Pact convention reference (CC substantive Claude Code Architecture Rules canonical (Pact contract testing convention))

---

# 0. Usage Notes

## 0.0 Naming note

The file kebab `test-plan-yaml-schema` reflects this source's current scope (yaml schemas for feature integration and slice tiers). The kebab is retained unchanged across canonical-set revisions to preserve [OS] §8.5.3 citation grep-precision; the authoritative form-coverage statement is the title — `[TPL] Test Plan YAML Schema (Feature integration yaml · Slice yaml)` — and the §0.1 Purpose statement below. Readers consulting this source should treat the title and §0.1 as the form-coverage source of truth. For the phase-level markdown master, see [TPL] Phase Test Plan.

## 0.1 Purpose

The three-tier test plan ontology partitions test design across distinct scopes:

- **Phase test plan (master, markdown)**: phase-level testing strategy and exit criteria for one phase of one app. Captures cross-feature scenarios, app-scale NFR scenarios, regression policy from prior phase. Human-authored, human-reviewed, AI-referenced.
- **Feature integration test plan (yaml)**: cross-slice flow scenarios within a single feature scope. Captures the test cases that exercise multiple slices of the same feature in sequence or concert. CC-authored at the detailed-spec layer (per §0.3 production row + §0.1 Relationship to DTW); AI-consumed.
- **Slice test plan (yaml)**: per-slice test design with bias firewall and context isolation. Each test case traces to a slice acceptance scenario or a non-regression constraint, declares its `context_scope`, `risk_tier`, and `adversarial_angle`. AI test-writer subagents consume this directly.

**Operating premise**: The three-tier ontology exists because AI test-writer subagents (per CC substantive Claude Code Architecture Rules canonical (subagent roster)) consume the slice tier directly under bias firewall and context isolation constraints — each subagent must see only the slice scope it is testing to avoid context leakage that corrupts test independence. The phase and feature integration tiers exist as human-authored / human-reviewed reference points that AI subagents do not write but may reference for upstream coordination. This schema is therefore an AI-execution-interface contract, not a generic test pyramid (Mike Cohn / Martin Fowler) or enterprise QA test strategy framework (TMMi, ISO 29119) adoption. External test methodology vocabulary is a source of inspiration; the three-tier ontology is calibrated to AI subagent consumption discipline (per [OS] §0.1.2 quality and §0.2 Cat 4 role).

## 0.2 Readers

| Tier | Primary readers | Secondary readers |
|---|---|---|
| Phase test plan (markdown) — owned by [TPL] Phase Test Plan | You (review) + Hub Claude (reference during TK-02) | CC firewalled S2 session (TK-03 acceptance/intent authoring reference) + CC (TK-04 entry self-check reference) |
| Feature integration test plan (yaml) | You (review) + AI test-writer subagents executing cross-slice flow tests | CC (during detailed-spec authoring) |
| Slice test plan (yaml) | test-writer-whitebox (A1), test-writer-blackbox (A2), adversarial-tester (A3) | You (review), CC firewalled S2 session (during TK-03 authoring), compliance-checker (A9) |

## 0.3 Relationship between the three tiers

| Aspect | Phase test plan (markdown) | Feature integration test plan | Slice test plan (yaml) |
|---|---|---|---|
| Filename | `phase-{N}.md` | `feature-{feature-slug}.yaml` | `{slice-id}.yaml` |
| Scope | One phase of one app | One feature within a phase | One slice within a feature |
| Format | Markdown (prose + tables) | YAML | YAML |
| Granularity | Strategy + scenario classes | Flow scenarios spanning slices | Test cases |
| Pairing | 1:1 with phase TDD | 1:1 with `§4.{feature-slug}` of phase TDD | 1:1 with slice acceptance.yaml |
| Production | TK-02 | TK-02 | TK-03 |
| Owner | Human-authored per [TPL] Phase Test Plan | CC (detailed-spec authoring) | CC firewalled S2 session at TK-03 |

**Cross-tier consistency**: the phase test plan's scenario classes must trace through to feature-level flow scenarios in the feature integration test plan, and to specific test cases in the slice test plan, so that a phase exit criterion can be evidenced by a chain of executable cases. Cross-tier consistency is verified at TK-02 sign-off and re-verified at each phase milestone.

## 0.4 Slice test plan relationship to slice acceptance.yaml

| Aspect | acceptance.yaml | slice test-plan.yaml |
|---|---|---|
| Purpose | What must pass, business-level | How to verify, test-design-level |
| Primary reader | AI agents + you (for review) | AI test-writer subagents |
| Structure | Scenarios with given/when/then | Test cases with technique, data variants, fixtures |
| Granularity | One scenario per business result | Multiple test cases per scenario |
| Owner | TK-03 (CC firewalled S2 session) | TK-03 (CC firewalled S2 session, paired production) |

This relationship is unique to the slice tier; phase markdown and feature yaml have no acceptance.yaml peer.

## 0.5 Position in artifact chain

```
apps/{app-slug}/specs/prd/phase-{N}.md
  ├→ apps/{app-slug}/specs/tdd/phase-{N}.md
  │       ├→ §1 phase architecture
  │       ├→ §2 cross-feature concerns (incl. §2.Phase-Level-Testing-Strategy)
  │       ├→ §3 walking skeleton scope (Phase 1 only)
  │       └→ §4.{feature-slug} per-feature engineering spec
  │
  ├→ apps/{app-slug}/specs/test-plan/phase-{N}.md          (phase test plan — owned by [TPL] Phase Test Plan)
  │
  ├→ apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml   (this schema §3 — feature integration test plan)
  │       (one per feature in the phase)
  │
  ├→ specs/design-system.md (a11y stance per §2.6, component inventory; project-level singleton)
  │
  └→ per slice (under apps/{app-slug}/specs/):
       slice-list/{feature-slug}.md
       intent/{slice-id}.md
       acceptance/{slice-id}.yaml
       test-plan/{slice-id}.yaml                           (this schema §4 onwards — slice test plan)
              ↓
           consumed by A1 (whitebox cases), A2 (blackbox cases including Pact consumer contracts)
              ↓
           test code under apps/{app-slug}/tests/**
                            packages/domain/{domain-name}/tests/** (when Tier 3 architecture-tier touched)
              ↓
           evidence under apps/{app-slug}/evidence/{slice-id}/
```

## 0.6 What this schema is not

- Not an execution manifest
- Not a test report format (that lives under `apps/{app-slug}/evidence/{slice-id}/`)
- Not a mutation test configuration
- Not a phase exit gate runtime — the phase test plan declares exit criteria; the gate is enforced by the milestone policy

## 0.7 Three-tier ontology summary

| Tier | Lives at | Established by | Schema in this source |
|---|---|---|---|
| 1 — phase test plan (master, markdown) | `apps/{app-slug}/specs/test-plan/phase-{N}.md` | TK-02, paired with phase TDD | Not in this source — owned by [TPL] Phase Test Plan |
| 2 — feature integration test plan (yaml) | `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` | TK-02, paired with phase TDD `§4.{feature-slug}` | §3 |
| 3 — slice test plan (yaml) | `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` | TK-03, paired with slice acceptance.yaml | §4 onwards |

## 0.8 Unit_type applicability

The three-tier ontology is authored against the `feature` unit production path (the dominant case). The other two unit types catalogued in [MECH] Development Track Workflow §4.0 consume this ontology asymmetrically; this subsection makes the asymmetry explicit so that test plan production, review, and audit at TK-02 / TK-03 do not need to reverse-engineer it from §4.0.2 / §4.0.4.

| Tier | `feature` unit | `walking_skeleton` unit (Phase 1 only, 1 slice) | `app_integration` unit (no slices) |
|---|---|---|---|
| Phase test plan (markdown) | Consumed as phase-level reference at TK-03 | Consumed as phase-level reference; the unit also surfaces its M2 acceptance contract through phase TDD `§3.Milestone-choreography-and-acceptance-criteria` rather than authoring new phase-level scenarios | **Primary authoring source** at TK-09 — the unit's deliverables (cross-feature integration tests + NFR harness) are authored against the cross-feature scenario classes catalogued here |
| Feature integration test plan (yaml) | One file per feature in the phase, at `feature-{feature-slug}.yaml` (per §3 schema) | **Not produced** — single-slice unit has no cross-slice flow within itself; cross-slice flow validation is irrelevant for `walking_skeleton` | Consumed as input at TK-09 — the unit may exercise cross-feature variants of these flows that are not covered at any individual feature unit's M2 |
| Slice test plan (yaml) | One file per slice, at `{slice-id}.yaml` (per §4 schema), produced at TK-03 | One file at `walking-skeleton.yaml` (slice-id = unit-id per §0.7 of [TPL] PRD + TDD to Intent and Acceptance Conversion Specification), produced at TK-03 | **Not produced** — the unit has zero customer-facing slices per §4.0.4 of [MECH] Development Track Workflow; integration test code is authored at TK-09 directly without a per-slice yaml peer |

**Cross-tier traceability** (per §0.3) applies symmetrically across unit types — phase exit criteria in the phase test plan must trace through to the test cases that actually fire, regardless of which unit type produced those test cases. For `app_integration`-authored cross-feature tests, the trace is direct from phase test plan scenarios to the unit's authored test code (skipping feature integration / slice test plan yaml peers since neither exists for this unit type).

---

# 1. Three-tier ontology

## 1.1 Why three tiers

The phase ontology established by [TPL] PRD Template and [TPL] TDD Template implies three test-scope levels that cannot be merged without losing audit clarity:

- A **phase exit criterion** like "all phase-1 features pass cross-feature regression suite X with zero critical defects" cannot be verified inside any single feature's tests; it lives at phase scope.
- A **cross-slice flow** like "user creates a request in slice 03, manager approves it in slice 05, system fires the notification scheduled in slice 07" cannot be verified inside any single slice's tests; it lives at feature scope.
- **Per-slice test cases** with `context_scope`, `risk_tier`, and `adversarial_angle` discipline are tightly coupled to a single slice's acceptance.yaml and assigned subagents.

Collapsing tiers (e.g., putting cross-feature scenarios inside slice test plans) breaks the slice-level abstraction: a slice's test plan becomes responsible for tests that no slice's owner can implement. Tier separation prevents this drift.

## 1.2 What each tier covers

### 1.2.1 Phase test plan (master, markdown)

Phase test plan scope and content contract are owned by [TPL] Phase Test Plan §1.

### 1.2.2 Feature integration test plan (yaml)

In scope:
- Cross-slice flow scenarios within a single feature
- Each scenario references the slices it traverses (by slice_id) and the order of traversal
- Each scenario declares its preconditions, steps, expected outcomes, evidence_required
- Owner subagent for executing the scenario (typically A2 blackbox)

Out of scope:
- Cross-feature flows (those are in the phase test plan, even if they happen to traverse only a few slices)
- Per-slice unit / contract / E2E cases (those are in the slice test plan)
- Per-slice acceptance scenarios (those are owned by acceptance.yaml at the slice level)

### 1.2.3 Slice test plan (yaml)

In scope:
- Test cases per slice with full bias firewall and context isolation discipline
- All `test_type` values: unit, integration-internal, contract, integration-external, e2e, visual, performance, accessibility
- Per-case `context_scope`, `coverage_source`, `risk_tier`, `adversarial_angle`
- Fixtures, determinism policy, isolation policy, retry policy, data variants, negative cases, observability probes
- Pact pair `pact_pair: {app-slug}-bff_{domain-name}` for contract test cases that cross the BFF↔domain boundary

Out of scope:
- Cross-slice flows (those are in the feature integration test plan)
- Cross-feature scenarios (those are in the phase test plan)
- Phase exit gate logic (phase test plan plus Milestone Policy)

## 1.3 Production order

In TK-02:
1. Phase TDD draft is in progress
2. Phase test plan is drafted alongside, derived from phase TDD §2.Phase-Level-Testing-Strategy (the phase test plan schema is owned by [TPL] Phase Test Plan, not this source)
3. For each feature in `Features in this phase`, the feature integration test plan is drafted, derived from `§4.{feature-slug}` content + paired-PRD scenarios attributed to that feature
4. Phase-level cross-tier traceability is finalized after feature-level scenarios are listed

In TK-03 (per slice):
5. Slice test plan is authored in the CC firewalled acceptance/intent authoring session (S2) at TK-03, firewalled from the implementing session (S3), derived from slice acceptance.yaml + relevant per-feature `§4.{feature-slug}.Module-Decomposition` + phase TDD §2.Phase-Level-Testing-Strategy + (when Tier 1 involved) the CC-authored UX Design Spec instance — synthesized in the CC UX-spec synthesis session (S1) at TK-02.3 and consumed here — for accessibility test case authoring

A feature integration test plan cannot reference a slice that does not yet exist in the slice-list. Slice test plans are produced as their slices come up in TK-03; the feature integration test plan is updated only if a feature-level scenario is invalidated by slice-level discoveries.

## 1.4 Pairing and update rules

| Tier | Paired with | Update trigger | Update path |
|---|---|---|---|
| 1 phase markdown (schema owned by [TPL] Phase Test Plan) | phase TDD | Phase TDD §2 changes; phase exit criteria revised; regression policy revised | Edit in place; review at next phase milestone |
| 2 feature yaml | phase TDD `§4.{feature-slug}` | `§4.{feature-slug}.Module-Decomposition` or `Slice-List` changes; cross-slice flow added/removed | Edit in place; verify phase-level traceability still holds |
| 3 slice yaml | slice acceptance.yaml | Slice acceptance scenario added/changed; TK-10 patches | Edit in place per [TPL] Conversion Spec; TK-10 may append to `adversarial_cases` |

When a higher tier's pairing target changes (e.g., phase TDD revised), the dependent tier must be re-verified, not silently accepted as still valid.

---

# 2. Phase test plan (master, markdown) — moved

The phase test plan (master, markdown) content contract is owned by **[TPL] Phase Test Plan**. This source no longer contains the phase-level markdown master schema — see that template for file location, document header, required sections (phase scope summary / cross-feature scenario classes / app-scale NFR / regression policy / phase exit criteria / cross-tier traceability), and anti-pattern guidance.

This source retains coverage for the two yaml tiers: §3 Feature integration test plan (yaml) and §4 Slice test plan (yaml).

---

# 3. Feature integration test plan (yaml) — schema

The feature integration test plan is a YAML document covering cross-slice flow scenarios within one feature.

## 3.1 File location and naming

`apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml`, where:
- `{app-slug}` matches the paired phase TDD's `app_slug`
- `{feature-slug}` matches one entry in the paired phase TDD's `Features in this phase`

## 3.2 Root YAML structure

```yaml
# apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml

app_slug:               # string, matches paired phase TDD app_slug
phase_number:           # integer, matches paired phase TDD phase_number
feature_slug:           # string, matches paired phase TDD §4.{feature-slug}
schema_version:         # "1.0" at current
generated_at:           # ISO 8601 timestamp
generated_by:           # "Claude Code" (canonical for new files, authored at the CC detailed-spec layer) | "Hub Claude" (retained as legacy reference only; not used for new files)

traces_to_tdd:          # string, relative path: "apps/{app-slug}/specs/tdd/phase-{N}.md"
                        # specifically references §4.{feature-slug}
traces_to_prd:          # string, relative path: "apps/{app-slug}/specs/prd/phase-{N}.md"
traces_to_phase_test_plan: # string, relative path: "apps/{app-slug}/specs/test-plan/phase-{N}.md"
traces_to_slice_list:   # string, relative path: "apps/{app-slug}/specs/slice-list/{feature-slug}.md"

flow_scenarios: []      # list; see §3.3

cross_tier_uplinks: []  # list of phase scenario class ids that this feature evidences; see §3.5
```

## 3.3 flow_scenarios entry

Each entry is one cross-slice flow scenario within this feature.

```yaml
flow_scenarios:
  - id:                          # string, unique within this file; format: "FLOW-{sequence}"
    name:                        # string, short descriptive name
    description:                 # string, one paragraph
    
    slices_traversed: []         # ordered list of slice_ids; the order reflects the flow's execution sequence
                                 # constraint: must equal the ordered de-duplicated set of flow_steps[].slice_ref values
    
    preconditions: []            # list of precondition strings (state required before flow starts)
    
    flow_steps: []               # ordered list:
                                 #   - step: "<short description>"
                                 #     slice_ref: "<slice_id>"
                                 #     observable_state: "<what should be observable after this step>"
    
    expected_end_state:          # string, the state after the last step
    
    risk_tier:                   # enum: critical | high | medium | low
                                 # derived from PRD risk register (cross-reference §7.1 of slice tier)
    
    adversarial_angle:           # string, one sentence
    
    evidence_required:           # list of evidence types: e.g., ["api_logs", "screenshot", "operator_digest"]
    
    owner_subagent:              # enum: A2 (blackbox, default for cross-slice flows) | manual (human-driven)
    
    determinism_policy: |        # one of:
                                 #   strict_deterministic — all data fixed
                                 #   pseudo_deterministic — seeded random
                                 #   replay_recorded — replays a recorded session
    
    notes:                       # optional free text
```

## 3.4 What flow_scenarios must cover

Each `flow_scenarios` entry must:
- Traverse two or more slices (single-slice tests belong in the slice test plan)
- Stay within one feature (cross-feature flows belong in the phase test plan)
- Trace to at least one acceptance scenario per slice it touches (referenced by slice acceptance.yaml scenario id) — when slices have not been finalized yet, mark scenario references as `pending` and resolve before TK-03 starts on that slice
- Evidence at least one phase-level scenario class via `cross_tier_uplinks`, OR justify why this flow is local to the feature and does not uplink

## 3.5 cross_tier_uplinks

```yaml
cross_tier_uplinks:
  - tier_1_class_id:             # e.g., "CFS-03" from phase test plan §2
    flow_ids: []                 # list of FLOW-* in this file that evidence this phase class
    coverage_note:               # optional string explaining how
```

If a feature integration test plan does not have any cross_tier_uplinks, the feature is by inference local to itself at the testing strategy level; this is acceptable but should be intentional, not by oversight.

## 3.6 What must not appear in feature integration test plans

- Per-slice unit / contract / E2E / a11y cases (those go into Slice test plan (yaml))
- Per-slice acceptance scenarios (those are owned by slice acceptance.yaml)
- Cross-feature flows (those go into Phase test plan (markdown) §2)
- Test code, fixtures, mocks (those are slice-level concerns)
- Phase exit criteria (those go into the phase test plan — see [TPL] Phase Test Plan)

## 3.7 Anti-pattern

Splitting a single-slice acceptance scenario into a "flow scenario" by artificially decomposing it across pseudo-steps. A flow scenario must genuinely traverse slice boundaries; a one-slice acceptance scenario stays in the slice test plan.

---

# 4. Slice test plan (yaml) — root YAML structure

```yaml
# apps/{app-slug}/specs/test-plan/{slice-id}.yaml

app_slug:               # string, matches active app from frozen roster (PRD §1.1, TDD §1, acceptance.yaml)
phase_number:           # integer, matches apps/{app-slug}/specs/tdd/phase-{N}.md phase_number
feature_slug:           # string, matches one entry in phase TDD's "Features in this phase" (and phase PRD §7.1)
slice_id:               # string, matches apps/{app-slug}/specs/acceptance/{slice-id}.yaml
schema_version:         # "1.0" at current
generated_at:           # ISO 8601 timestamp
generated_by:           # "Claude Code" (canonical for new files, authored in the CC firewalled S2 session at TK-03) | "adversarial-loop-patch" (for TK-10 patches added by adversarial-tester subagent A3) | "Hub Claude" (retained as legacy reference only; not used for new files in the current canonical workflow)

traces_to_acceptance:        # string, relative path: "apps/{app-slug}/specs/acceptance/{slice-id}.yaml"
traces_to_tdd:               # string, relative path: "apps/{app-slug}/specs/tdd/phase-{N}.md"
                             # specifically references §4.{feature-slug} of that phase TDD
traces_to_prd:               # string, relative path: "apps/{app-slug}/specs/prd/phase-{N}.md"
traces_to_phase_test_plan:   # string, relative path: "apps/{app-slug}/specs/test-plan/phase-{N}.md"
traces_to_feature_test_plan: # string, relative path: "apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml"
traces_to_slice_list:        # string, relative path: "apps/{app-slug}/specs/slice-list/{feature-slug}.md"
traces_to_design_system:     # string, relative path: "specs/design-system.md" (project-level singleton, when slice involves Tier 1)

test_cases: []          # list; see §5

adversarial_cases: []   # list; see §6 — only populated after TK-10 patches

coverage_summary:       # see §17

schema_compliance:      # see §18
```

**Path discipline**: app-scoped paths (`traces_to_acceptance`, `traces_to_tdd`, `traces_to_prd`, `traces_to_phase_test_plan`, `traces_to_feature_test_plan`, `traces_to_slice_list`) all use the `apps/{app-slug}/` prefix. The `traces_to_design_system` path is a project-level singleton and does not get an `apps/` prefix. This split mirrors the repository layout in CC substantive Claude Code Architecture Rules canonical (repository layout).

**App slug + phase_number consistency**: `app_slug` must match phase PRD §1.1 `App Slug` (per [TPL] PRD §0.7.1), phase TDD §1 `app_slug` header (per [TPL] TDD §1), and acceptance.yaml `app_slug` top-level field (per [TPL] Writing Standard §3.2). `phase_number` must match the phase TDD's `phase_number` (per [TPL] TDD §1). A mismatch anywhere in the chain is a TK-03 conversion blocker, not a downstream cleanup item.

`generated_by` value `"Claude Code"` reflects the canonical executing context per [MECH] Workflow TK-03 — the CC firewalled acceptance/intent authoring session (S2), firewalled from the implementing session (S3) per [MECH] DTW §4 TK-03 + [TPL] Writing Standard §1.11. The legacy value `"Hub Claude"` is retained for backwards-reference compatibility with older test-plan files but should not be used for new test-plan files. The `"adversarial-loop-patch"` value remains valid for TK-10 patches added by adversarial-tester subagent A3 to a CC-authored slice test-plan; the value distinguishes the patching source from the original authoring session without rewriting the file's primary `generated_by` value.

---

# 5. test_cases field

Each entry is one test case.

## 5.1 Structure

```yaml
test_cases:
  - id:                          # string, unique within this file; format: "TC-{sequence}"
    name:                        # string, short descriptive name
    traces_to_scenario_id:       # string, references acceptance.yaml must_pass_scenarios[].id, or "NRC-{nrc_index}", or "EDGE-{edge_index}", or "A11Y-{a11y_index}" for accessibility expectations
    tier:                        # enum: frontend | bff | domain-service
    test_type:                   # enum; see §5.2
    context_scope:               # enum: business_rules_only | api_contracts | code_whitebox
    coverage_source:             # enum: acceptance_derived | risk_derived | technique_derived
    risk_tier:                   # enum: critical | high | medium | low; see §7
    adversarial_angle:           # string, one sentence; see §8
    
    preconditions: []            # list of precondition strings
    fixtures:                    # fixture specification; see §5.3
    steps: []                    # ordered list of steps
    assertions: []               # list of assertions
    cleanup:                     # cleanup specification; see §5.4
    
    determinism_policy:          # see §11
    isolation_policy:             # see §12
    retry_policy:                # see §13
    
    data_variants: []            # list; see §14
    negative_cases: []           # list; see §15
    
    observability_probes: []     # list; see §16

    # Contract-test specific optional fields (when test_type == contract for BFF↔domain pairs)
    pact_pair: ""                # see §5.8

    # Accessibility-specific optional fields (when test_type == accessibility)
    a11y_concerns: []            # list; see §5.6 (replaces former a11y_wcag_criteria)
    a11y_tool: []                # list; see §5.7
```

## 5.2 test_type enum

| Value | Description | Tier typically | Writer agent or skill |
|---|---|---|---|
| `unit` | Smallest unit tested in isolation, internal mocks allowed | any | A1 (whitebox) |
| `integration-internal` | Multiple components within a tier, real internal deps | any | A1 (whitebox) |
| `contract` | Consumer-driven or schema-based contract between tiers; for BFF↔domain pairs uses Pact pair `{app-slug}-bff_{domain-name}` per CC substantive CCAR canonical (Pact contract testing convention) | bff, domain-service | A2 (blackbox) |
| `integration-external` | Cross-tier real integration or external system integration | bff, domain-service | A2 (blackbox) |
| `e2e` | End-to-end through UI or full API surface | cross-tier | A2 (blackbox) |
| `visual` | Visual regression | frontend | A2 (blackbox) |
| `performance` | Response time, load, stress | bff, domain-service | A2 (blackbox) |
| `accessibility` | Accessibility verification; **optional** per [RULE] DSG §6 (no formal a11y gate); used only when slice has specific a11y concerns beyond Arco component defaults | frontend | A2 (blackbox); SK-W on operator demand only, not auto-invoked |

(No "Tier 1 mandatory rule" — per DSG §6, accessibility test cases are optional regardless of tier involvement. A Tier 1 slice without accessibility cases is normal and not a TK-03 blocker.)

## 5.3 fixtures field

Fixtures must be explicit; no implicit global fixtures.

```yaml
fixtures:
  data_fixtures: []     # list of named data fixtures: name, scope (test|suite), content_reference
  service_fixtures: []  # list of mocked or sandboxed external services: name, target, behavior_reference
  environment_fixtures: # env setup
    - name:
      setup:
      teardown:
```

## 5.4 cleanup field

```yaml
cleanup:
  data_cleanup: []       # what data state to restore
  service_cleanup: []    # what service state to restore
  idempotency_check:     # boolean — rerun from same preconditions produces same result
```

## 5.5 What must not appear in test_cases

- Source code file paths or internal class references
- Framework-specific syntax (Jest matchers, Playwright selectors)
- Test naming conventions

## 5.6 a11y_concerns field (accessibility test_type only)

When `test_type == accessibility`, declare what specific accessibility concern the case verifies, in plain terms. **Do not use WCAG criterion identifiers as the field shape** — HDC has no formal WCAG conformance target per [RULE] DSG §6.

```yaml
a11y_concerns:
  - id:                         # "A11Y-1" (case-local stable identifier)
    description:                # what the case verifies, in plain language (e.g., "keyboard-only operator can complete the wizard end-to-end", "icon-only delete buttons announce a meaningful label to screen readers")
    relates_to:                 # optional; cross-reference to either:
                                #   - DSG §6.1 recommendation (e.g., "DSG-6.1-3" for the form-labels recommendation)
                                #   - acceptance.yaml accessibility_expectations id (e.g., "A11Y-1")
                                # leave empty if neither applies
```

The schema deliberately omits `wcag_criterion`, `level`, `version`, and `tier` fields. If a case happens to align with a WCAG criterion, that's incidental and may be mentioned in `description` as plain context, not as a structural field.

## 5.7 a11y_tool field (accessibility test_type only)

When `test_type == accessibility`, declare the verification approach.

```yaml
a11y_tool:
  - name:                       # "axe-core" | "manual" | "eslint-plugin-jsx-a11y"
    config_reference:           # path to tool config if any
    invocation_mode:            # "ci-automated" | "operator-on-demand" | "operator-smoke-test"
                                # axe-core via SK-W is "operator-on-demand" only per DSG §6.3;
                                # eslint-plugin-jsx-a11y is "ci-automated" via the normal lint pass at warn level;
                                # manual is "operator-smoke-test"
```

**Tool stance** (cross-reference CC substantive Code Quality Rule Set canonical and DSG §6):
- `eslint-plugin-jsx-a11y`: routine, automatic, runs at `warn` severity in normal lint; no separate gate
- `axe-core` via SK-W: on-demand utility only; not auto-invoked by milestones or other skills
- `manual`: operator's M4 smoke test; non-gating

## 5.8 pact_pair field (contract test_type, BFF↔domain pairs only)

When `test_type == contract` and the case crosses the BFF-to-domain boundary, declare the Pact pair name.

```yaml
pact_pair: "{app-slug}-bff_{domain-name}"   # e.g., "hr-data-asset-mgmt-bff_data-asset"
```

**Convention** (per CC substantive Claude Code Architecture Rules canonical (Pact contract testing convention) + [MECH] CI/CD Milestone Policy §2.3):

- Consumer-driven Pact: the BFF authors the consumer contract; the domain authors verification
- Consumer-side contract location: `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**` (A2 writes here per CC substantive CCAR canonical (Pact contract testing convention))
- Producer-side verification location: `packages/domain/{domain-name}/tests/contract-verification/**` (A2 writes here when working in a domain slice)
- The `pact_pair` name segment is the same string in both locations and in the test-plan field

**Other contract test types**: schema-based contracts (e.g., OpenAPI conformance) do not use the `pact_pair` field; their contract definition lives in `apps/{app-slug}/specs/openapi.yaml` (single app-scoped file, accumulated across phases per [TPL] TDD §4.9).

---

# 6. adversarial_cases field

Populated only after TK-10 adversarial loop produces findings. Structure mirrors test_cases with additional fields:

```yaml
adversarial_cases:
  - id:                       # "ADV-{sequence}"
    name:
    traces_to_scenario_id:
    generated_by: adversarial-tester
    severity:                 # enum: critical | high | medium | low
    requires_human_ack:       # boolean; true for critical and high per TK-10 policy
    human_ack:                # object when applicable: { acked_by, acked_at, decision }
    
    # all test_case fields below
    tier:
    test_type:
    context_scope:
    # ... same as §5.1
```

---

# 7. risk_tier and its derivation

risk_tier drives retry policy strictness, adversarial-loop enrollment, and evidence aggregation weight.

## 7.1 Derivation rules (mechanical, no AI judgement)

```yaml
# Rule: A test case inherits risk_tier from the PRD risk section it traces to.
# No AI promotion or demotion. If PRD risk register is unclear, the CC firewalled
# S2 session raises a clarification in TK-03 instead of selecting a value.

# Mapping:
# - PRD §13.1 Key Risks entry with impact="critical" → risk_tier: critical
# - PRD §13.1 Key Risks entry with impact="high"     → risk_tier: high
# - PRD §13.1 Key Risks entry with impact="medium"   → risk_tier: medium
# - Default if no matching PRD risk entry             → risk_tier: medium
# - A test case protecting only a non-regression constraint without named risk → risk_tier: medium
# - A test case verifying a happy-path scenario with no named risk → risk_tier: medium
# - A test case explicitly tagged as edge/boundary without a named risk → risk_tier: low

# Accessibility-specific examples:
# - PRD risk "Critical HR self-service flow inaccessible to keyboard-only users" with impact="high" → accessibility cases tracing to that risk inherit risk_tier: high
# - PRD risk "Failure to support RTL locales" with impact="critical" → RTL-related a11y cases inherit critical
# - Accessibility case without a named PRD risk → risk_tier: medium (default)
```

## 7.2 Downstream effect of risk_tier

| risk_tier | retry_policy default | data_variant count default | adversarial-loop enrollment | evidence aggregation priority |
|---|---|---|---|---|
| critical | 0 retries; fail-fast | ≥4 variants | enrolled | top priority in report |
| high | 1 retry allowed | ≥3 variants | enrolled | high priority |
| medium | 2 retries allowed | ≥2 variants | conditional | standard |
| low | 3 retries allowed | 1 variant sufficient | not enrolled | standard |

## 7.3 Anti-drift on risk_tier

- risk_tier must never be selected by an AI agent from analysis of the acceptance scenario
- If PRD risk register is silent on a scenario's risk, the CC firewalled S2 session raises a clarification during TK-03

---

# 8. adversarial_angle field

Every test case must state in one sentence what failure mode it is designed to expose.

## 8.1 Examples of good adversarial_angle

- "Verifies that the API rejects an empty employee_id, confirming input validation is enforced"
- "Verifies that a transition from probation to regular employee triggers the downstream notification exactly once, confirming no duplicate fan-out"
- "Verifies that a user without the approver permission cannot initiate an approval via direct API call, confirming backend authorization is not bypassable"
- "Verifies that the employee list table is fully navigable by keyboard without mouse, confirming keyboard-only a11y"

## 8.2 Examples of weak adversarial_angle

- "Tests the happy path"
- "Tests the feature works"
- "Tests API"

## 8.3 Anti-drift on adversarial_angle

- Every test case must have a non-trivial adversarial_angle
- `happy_path_only` is permitted as a special value only when the case exists to smoke-test a scenario; must have at least one sibling case with real adversarial_angle

---

# 9. coverage_source field

Captures the derivation lineage of each case, for audit and bias detection.

## 9.1 Values

| Value | Meaning | Expected when |
|---|---|---|
| `acceptance_derived` | Case is a direct translation of a must_pass_scenario | Default for most cases |
| `risk_derived` | Case is derived from a PRD risk, possibly not tied to a must_pass_scenario | When a risk is material but not captured in acceptance |
| `technique_derived` | Case is derived from applying a test design technique | Common for data_variants and negative_cases |

## 9.2 Forbidden value

- `code_coverage_derived` is forbidden. A case must never be created because code has a branch; this reverses causality.

---

# 10. context_scope field (bias firewall)

## 10.1 Values and implications

| Value | Writer agent or skill | Read allowed | Read denied |
|---|---|---|---|
| `business_rules_only` | CC firewalled S2 session adversarial preview or A3 adversarial-tester | acceptance.yaml, PRD, test-plan.yaml | `apps/*/src/**`, `packages/*/src/**`, `apps/*/tests/**` |
| `api_contracts` | A2 test-writer-blackbox (+ SK-W for a11y cases) | test-plan.yaml, TDD (`§4.{feature-slug}.API-Contracts`), openapi.yaml, intent.md, acceptance.yaml, design-system.md, design refs | `apps/*/src/**`, `packages/*/src/**` |
| `code_whitebox` | A1 test-writer-whitebox | test-plan.yaml, TDD, intent, acceptance, `apps/{app-slug}/src/**`, `packages/{domain-name}/src/**` for the active slice's app and consumed domains | — |

## 10.2 Selection rules

- test_type ∈ {unit, integration-internal} → `code_whitebox`
- test_type ∈ {contract, integration-external, e2e, visual, performance, accessibility} → `api_contracts`
- adversarial_cases may use `business_rules_only` during design phase before being converted to executable test cases

## 10.3 Anti-drift on context_scope

- A test case's context_scope is fixed at creation
- If a blackbox case appears to need src/** visibility, it is misclassified or the blackbox approach is wrong for it
- `code_whitebox` scope is constrained to the active slice's `apps/{app-slug}/` and consumed `packages/{domain-name}/` paths only — cross-app or cross-domain whitebox visibility is a violation

---

# 11. determinism_policy field

```yaml
determinism_policy:
  time_handling:          # frozen_time: <ISO 8601> | natural | seeded_offset: <duration>
  randomness:             # no_random | seeded: <seed_value>
  io_sandbox:             # mocked | sandboxed | real
  external_deps:          # mocked | contract_replay | live
  clock_source:           # if time_handling != natural: test_clock | system_clock_frozen
```

## 11.1 Rationale

AI-written tests without explicit determinism contracts produce flaky test suites. This field forces the decision at design time.

## 11.2 Defaults by test_type

| test_type | time_handling default | randomness default | io_sandbox default |
|---|---|---|---|
| unit | frozen_time or natural (if no time dep) | no_random | mocked |
| integration-internal | frozen_time | no_random | mocked |
| contract | frozen_time | no_random | mocked |
| integration-external | frozen_time | no_random | sandboxed |
| e2e | frozen_time if possible; otherwise natural | no_random if possible | sandboxed |
| visual | frozen_time | no_random | sandboxed |
| accessibility | frozen_time | no_random | sandboxed |
| performance | natural | seeded | sandboxed |

---

# 12. isolation_policy field

```yaml
isolation_policy:
  run_mode:               # parallel_safe | serial_required | exclusive
  shared_state_allowed:   # boolean
  shared_state_scope:     # if allowed: test | suite | session
  setup_isolation:        # per_test | per_suite
```

---

# 13. retry_policy field

```yaml
retry_policy:
  max_retries:               # integer; default per risk_tier (see §7.2)
  retry_on:                  # list of retryable failure classes
  do_not_retry_on:           # list of non-retryable, e.g., [assertion_failed]
  flaky_quarantine_threshold: # integer; after N consecutive flaky runs, case is quarantined
```

## 13.1 Anti-drift on retry

- Retrying on `assertion_failed` is always wrong
- Tests with `max_retries > 0` that still fail should surface to TK-08 RCA, not be silently accepted as flaky

---

# 14. data_variants field

Captures the equivalence classes and boundary values the test case will exercise.

```yaml
data_variants:
  - name:                       # descriptive name
    category:                   # enum: equivalence_class | boundary_low | boundary_high | invalid | typical
    input_snapshot:             # brief description of inputs
    expected_outcome_snapshot:  # brief description of expected outcome
    rationale:                  # why this variant is in scope
```

## 14.1 Derivation rules

- Numeric fields: at least one boundary_low and one boundary_high
- Enumerated fields: one per valid value plus one invalid
- Strings: typical, empty, max-length, special-characters
- Date/time fields: typical, boundary around business-relevant dates
- Reference fields: existing, nonexistent, soft-deleted

## 14.2 Anti-drift on data_variants

- Counts should scale with risk_tier (see §7.2)
- A critical-risk case with only one data_variant is a red flag
- Every variant must have a named rationale

---

# 15. negative_cases field

Explicit negative cases for each test case.

```yaml
negative_cases:
  - name:                       # descriptive
    category:                   # enum: permission_denied | validation_error | business_rule_violation | system_error | timeout | conflict | a11y_violation
    trigger:                    # what causes the negative outcome
    expected_error_shape:       # what the error looks like
    rationale:                  # why this negative case matters
```

## 15.1 Requirement

- Every test case must have ≥1 negative_cases entry, OR the explicit marker `negative_cases_n_a: true` with justification
- `negative_cases_n_a: true` must be approved by your review; AI cannot self-approve

## 15.2 Accessibility negative cases

For `test_type: accessibility`, negative cases describe the expected failure shape when the a11y check fails (e.g., axe-core reporting a violation). Category is typically `a11y_violation`.

---

# 16. observability_probes field

What signals the test will capture as evidence.

```yaml
observability_probes:
  - type:                       # enum: log | metric | audit_event | response_header | status_transition | a11y_finding
    name:
    expected_content:           # shape or content expectation
    capture_location:           # where the evidence is written; under apps/{app-slug}/evidence/{slice-id}/
```

## 16.1 Purpose

Ties to the acceptance.yaml `observability_expectations` field. The test-plan says how each observability expectation will be proven.

## 16.2 Accessibility probes

When a case uses `a11y_tool.invocation_mode: operator-on-demand` (SK-W), findings are written to `apps/{app-slug}/evidence/{slice-id}/accessibility-audit.md` and `apps/{app-slug}/evidence/{slice-id}/accessibility-results.json` only when the operator manually runs SK-W. These files do not exist by default for every Tier 1 slice. Probes of type `a11y_finding` declare the expected shape of findings (ideally empty — no findings on success) and the capture location for the on-demand audit, when one is performed.

For cases using `a11y_tool.invocation_mode: ci-automated` (eslint-plugin-jsx-a11y), the "evidence" is the lint report from the normal M1 lint pass; no separate a11y evidence file is written.

## 16.3 Capture location convention

All probe `capture_location` paths sit under `apps/{app-slug}/evidence/{slice-id}/` per the repository layout in CC substantive Claude Code Architecture Rules canonical (repository layout). Examples:

- Audit events: `apps/{app-slug}/evidence/{slice-id}/audit-{event-name}.log`
- A11y findings: `apps/{app-slug}/evidence/{slice-id}/accessibility-audit.md`
- Performance metrics: `apps/{app-slug}/evidence/{slice-id}/performance-report.md`

Cross-app capture paths (writing to another app's evidence folder) are not sanctioned; each slice's probes write to its own app's evidence directory.

---

# 17. coverage_summary field

> **Scope**: §17-§22 govern the slice test plan (yaml) only. The bare term "test-plan.yaml" in these sections refers to the slice tier; the §19 cross-file consistency checks and the §22 finalization self-check are slice-tier finalization gates and do not apply to a feature integration test plan.

Summary aggregate used by compliance-checker (A9) to verify coverage.

```yaml
coverage_summary:
  scenarios_covered:            # list of must_pass_scenarios[].id from acceptance.yaml
  scenarios_not_covered:        # list, with justification for each
  non_regression_constraints_covered: # list of NRC indices
  edge_cases_covered:           # list of edge_case indices
  permissions_covered:          # list of permission rules from acceptance
  data_expectations_covered:    # list
  observability_expectations_covered: # list
  a11y_expectations_covered:    # list of a11y-related acceptance items (when slice involves Tier 1)
  pact_pairs_covered:           # list of {app-slug}-bff_{domain-name} pairs (when slice involves Tier 3 domain consumption)
```

---

# 18. schema_compliance field

```yaml
schema_compliance:
  schema_version: "1.0"
  lint_passed: true             # populated by a schema validator
  checked_at:                   # ISO 8601
  known_deviations: []          # any approved deviations
```

---

# 19. Cross-file consistency

Before finalizing test-plan.yaml, verify:

1. Every `must_pass_scenarios[].id` in acceptance.yaml appears in at least one `test_cases[].traces_to_scenario_id` or is explicitly justified in `coverage_summary.scenarios_not_covered`.
2. Every `non_regression_constraints` entry has at least one tracing test case.
3. Every `edge_cases` entry has at least one tracing test case.
4. Every `permissions` rule has at least one tracing test case.
5. Every `data_expectations` entry has at least one tracing test case with matching `assertions`.
6. Every `observability_expectations` entry has at least one `observability_probes` entry somewhere in test_cases.
7. risk_tier values across test cases are consistent with paired phase PRD §13.1 risk entries (or whichever PRD § houses the risk register in this phase's PRD).
8. **When slice involves Tier 1 with slice-specific a11y considerations**: those considerations from the feature's CC-authored per-feature UX Design Spec instance §2B.5 (Accessibility call-outs, feature-specific only) have corresponding `test_type: accessibility` cases. (Per [RULE] DSG §6, slices without specific a11y considerations need no accessibility cases — this is normal, not a violation.)
9. **When slice involves Tier 1**: Components referenced in intent.md UX brief map to cases in `test_type ∈ {e2e, visual}`; `accessibility` cases are mapped only when the slice has specific a11y concerns per DSG §6.
10. **`app_slug` field is populated and matches PRD §1.1 / TDD §1 / acceptance.yaml `app_slug` exactly**; mismatch is a TK-03 conversion blocker.
11. **All file-path references use the correct prefix**: app-scoped paths use `apps/{app-slug}/` and follow phase-aware naming (`phase-{N}.md` for PRD/TDD/phase test plan; `feature-{feature-slug}.yaml` for feature integration test plan; `{slice-id}` for per-slice files; `{feature-slug}.md` for slice-list); project-level singleton (`specs/design-system.md`) is the only `apps/`-prefix exception.
12. **When slice consumes a Tier 3 domain** (per phase TDD `§4.{feature-slug}.Module-Decomposition` domain references): at least one `test_type: contract` case exists with `pact_pair: {app-slug}-bff_{domain-name}` populated, and the pair is reflected in `coverage_summary.pact_pairs_covered`.

---

# 20. Abstraction boundary for test-plan.yaml

The test-plan.yaml is a design-level artifact, not an executable. The following leakage patterns indicate the abstraction boundary has been violated — the plan is mixing levels that should be kept separate.

| Leakage pattern | Why it's a boundary violation |
|---|---|
| Specific test framework code (Jest, Playwright, JUnit syntax) | Writer agents choose framework per tier; plan should be framework-neutral |
| File paths to `apps/*/src/**` or `apps/*/tests/**` or `packages/*/src/**` | Writer agents decide locations per CLAUDE.md hierarchy; paths in plan risk whitebox bias leakage |
| Internal class names or method signatures | Same abstraction violation; plan should be behavior-oriented not structure-oriented |
| Environment-specific values (API tokens, URLs for specific environments) | Those belong in fixtures and environment configuration, not test design |
| Repository path layout structure | CC substantive Claude Code Architecture Rules canonical (repository layout) owns layout |
| Branch topology, node assignment mechanics | [RULE] Workspace Topology |
| Code review tool command semantics | CC substantive Codex Plugin Usage canonical (post-Phase-3) |
| Pact pair mechanics (consumer-driven setup, broker config) | CC substantive CCAR canonical (Pact contract testing convention) + tooling docs |

Cross-source boundary (what belongs in adjacent sources instead) is covered by each field's scoping rules above: `traces_to_*` fields attach the plan to acceptance, TDD, and Design System Governance without duplicating their content.

---

# 21. Minimal template with accessibility example

```yaml
app_slug: hr-data-asset-mgmt
phase_number: 1
feature_slug: manager-e-signature
slice_id: manager-e-signature-01-initiation
schema_version: "1.0"
generated_at: 2026-04-22T10:00:00Z
generated_by: "Claude Code"

traces_to_acceptance: "apps/hr-data-asset-mgmt/specs/acceptance/manager-e-signature-01-initiation.yaml"
traces_to_tdd: "apps/hr-data-asset-mgmt/specs/tdd/phase-1.md"
traces_to_prd: "apps/hr-data-asset-mgmt/specs/prd/phase-1.md"
traces_to_phase_test_plan: "apps/hr-data-asset-mgmt/specs/test-plan/phase-1.md"
traces_to_feature_test_plan: "apps/hr-data-asset-mgmt/specs/test-plan/feature-manager-e-signature.yaml"
traces_to_slice_list: "apps/hr-data-asset-mgmt/specs/slice-list/manager-e-signature.md"
traces_to_design_system: "specs/design-system.md"

test_cases:
  # Example 1: contract test (blackbox; BFF↔domain Pact pair)
  - id: TC-001
    name: "Initiate e-signature with valid approver"
    traces_to_scenario_id: S1
    tier: bff
    test_type: contract
    pact_pair: "hr-data-asset-mgmt-bff_data-asset"
    context_scope: api_contracts
    coverage_source: acceptance_derived
    risk_tier: high
    adversarial_angle: "Verifies that only designated approvers can initiate, confirming authorization is enforced at API contract level"
    
    preconditions:
      - "User has approver role"
      - "Target employee exists and is in eligible status"
    fixtures:
      data_fixtures:
        - name: approver-user
          scope: test
          content_reference: "fixtures/users/approver.json"
      service_fixtures: []
      environment_fixtures: []
    steps:
      - "POST /api/e-signature/initiate with approver auth and eligible employee payload"
    assertions:
      - "Response status 201"
      - "Response body contains signature_request_id"
    cleanup:
      data_cleanup:
        - "Delete created signature request"
      service_cleanup: []
      idempotency_check: true
    
    determinism_policy:
      time_handling: frozen_time
      randomness: no_random
      io_sandbox: mocked
      external_deps: mocked
      clock_source: test_clock
    isolation_policy:
      run_mode: parallel_safe
      shared_state_allowed: false
      setup_isolation: per_test
    retry_policy:
      max_retries: 1
      retry_on: [timeout]
      do_not_retry_on: [assertion_failed]
      flaky_quarantine_threshold: 3
    
    data_variants:
      - name: "typical approver + typical employee"
        category: typical
        input_snapshot: "valid approver, regular employee"
        expected_outcome_snapshot: "201 created"
        rationale: "Baseline happy path"
      - name: "approver with minimum permission set"
        category: boundary_low
        input_snapshot: "approver with only e-sign-initiate permission"
        expected_outcome_snapshot: "201 created"
        rationale: "Verifies permission narrowness"
    
    negative_cases:
      - name: "non-approver user"
        category: permission_denied
        trigger: "User without approver role attempts initiate"
        expected_error_shape: "403 Forbidden with code 'APPROVER_REQUIRED'"
        rationale: "Authorization is the load-bearing protection"
    
    observability_probes:
      - type: audit_event
        name: e-signature.initiated
        expected_content: "approver_id, target_employee_id, timestamp, request_id"
        capture_location: "apps/hr-data-asset-mgmt/evidence/manager-e-signature-01-initiation/audit-e-sign-initiated.log"

  # Example 2: accessibility test (optional; only when slice has specific a11y concerns)
  # Per [RULE] DSG §6 the slice has no obligation to include this test_type; this example
  # is shown for completeness when a slice does choose to declare specific concerns.
  - id: TC-002
    name: "Signature initiation form is fully keyboard-operable"
    traces_to_scenario_id: A11Y-1
    tier: frontend
    test_type: accessibility
    context_scope: api_contracts
    coverage_source: acceptance_derived
    risk_tier: medium
    adversarial_angle: "Verifies that the signature initiation form can be completed end-to-end with keyboard alone (Tab, Shift-Tab, Enter, Space), since approvers may use accessibility tooling"
    
    a11y_concerns:
      - id: A11Y-1
        description: "Operator using keyboard only can reach all form fields, the submit action, and the confirmation dialog without mouse"
        relates_to: "DSG-6.1-recommendation-2"
      - id: A11Y-2
        description: "Form field labels are programmatically associated (Arco Form.Item label prop used)"
        relates_to: "DSG-6.1-recommendation-3"
    a11y_tool:
      - name: "manual"
        invocation_mode: "operator-smoke-test"
      - name: "axe-core"
        config_reference: "config/axe-core.json"
        invocation_mode: "operator-on-demand"
    
    observability_probes:
      - type: a11y_finding
        name: "axe-core findings (when SK-W is invoked)"
        expected_content: "no critical or serious findings on the listed concerns"
        capture_location: "apps/hr-data-asset-mgmt/evidence/manager-e-signature-01-initiation/accessibility-audit.md"

coverage_summary:
  scenarios_covered: [S1, A11Y-1]
  scenarios_not_covered: []
  pact_pairs_covered: [hr-data-asset-mgmt-bff_data-asset]

schema_compliance:
  schema_version: "1.0"
  lint_passed: true
  checked_at: 2026-04-22T10:00:00Z
  known_deviations: []
```

---

# 22. Self-check before finalizing

Before considering test-plan.yaml ready for downstream consumption — the M0 design freeze enforced by the CC session firewall (S1/S2 acceptance/intent authoring ⊥ S3 implementing) plus the Hub-authored TDD as the independent intent root, not by a Hub-side location boundary — and the subsequent TK-04 entry self-check (CC mechanical structural verification) per [MECH] Development Track Workflow §4, verify:

1. `app_slug` and `phase_number` populated and consistent across phase PRD / phase TDD / acceptance.yaml / this file
2. All required top-level fields populated; `traces_to_*` paths use correct `apps/{app-slug}/` prefix (project-level singleton excepted)
3. Every test case has all required fields populated
4. Every test case's risk_tier is mechanically derived per §7.1
5. Every test case has a non-trivial adversarial_angle per §8
6. context_scope assignments respect §10.2 selection rules
7. negative_cases or `negative_cases_n_a: true` is present for every case
8. determinism_policy is explicit per §11
9. No framework-specific syntax leaked into the plan
10. No `apps/*/src/**`, `packages/*/src/**`, or `apps/*/tests/**` paths leaked into the plan
11. Cross-file consistency (§19) holds — including the new #10 (app_slug match), #11 (path prefix), #12 (Pact pair coverage when domain consumed)
12. **When slice has slice-specific a11y considerations (per the feature's CC-authored per-feature UX Design Spec instance §2B.5 Accessibility call-outs, feature-specific only)**: each consideration has at least one corresponding `test_type: accessibility` case using the §5.6 `a11y_concerns` field. Slices without specific a11y considerations need no accessibility cases, per [RULE] DSG §6.
13. **When slice consumes a Tier 3 domain**: at least one `test_type: contract` case has `pact_pair: {app-slug}-bff_{domain-name}` populated per §5.8
