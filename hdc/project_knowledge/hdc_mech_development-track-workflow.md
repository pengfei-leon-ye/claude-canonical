# [MECH] Development Track Workflow

- **Project**: HR Digital Cockpit
- **Document Type**: Workflow Orchestration Specification
- **Status**: Active canonical
- **Role**: Stable declaration of the end-to-end task sequence (TK-01 through TK-13) and the cross-workspace orchestration contract. Hub-side ownership: full substantive content for Hub-authored tasks (TK-01 / TK-02 with sub-steps / TK-03 / TK-12 operator gate), the unit_type catalog as cross-workspace interface, the per-task workspace mapping, the milestone-to-task mapping, the transition mechanism catalog, the human intervention budget, the failure routing matrix, cross-workspace anti-drift signals, and Hub Claude soft compliance trigger phrases (Hub-internal substantive). CC-executed tasks (TK-04 through TK-11 and TK-13) are declared at constitutional identity + Hub-facing interface level only; their detailed step-by-step execution mechanics live at CC substantive DTW canonical.
- **Source Category**: Cat 4
- **Management-System Role**: Workflow orchestration specification; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Detailed task-level expansion of the Development Track routing defined in [OS] §7.1. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side residue carries the constitutional skeleton + Hub-authored substantive content; CC-side substantive canonical owns the CC-executed task mechanics.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design), §10 MECE, §12 make important work executable.
- **Relationship to [REF] Hub-CD-CC Architecture**: TK sequence operates across the three workspaces (Hub / CD / CC). Hub-side TKs (TK-01, TK-02 sub-steps, TK-03) author content per the content pillar; CD-side participation embedded inside TK-02 Step 2.2 produces the phase-level design file (with per-feature internal labeling) when any feature in the phase has `tier_1_involved=true`; CC-side TKs (TK-04 onwards) consume content for implementation per the implementation pillar.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: Three-path handoffs at the relevant TK transitions:
  - TK-01 → TK-02 hub-side: PRD consumed in hub for TDD authoring
  - TK-02 Step 2.1 → Step 2.2 (Hub → CD): Hub PRD/TDD relevant sections transferred to CD per [MECH] Cross-Tool Workflow Handoff §2.1
  - TK-02 Step 2.2 → Step 2.3 (CD → Hub): the CD-produced phase-level design file is transferred to Hub per §2.2 for Hub-side design-file quality checks (phase-level cross-cutting check + per-feature slice checks) + Hub-side UX Design Spec instance authoring at two granularities (one phase-level instance covering cross-cutting UX content + per-feature instances iterated over all tier-1-involved features against each feature's labeled slice)
  - TK-03 → TK-04 (Hub → CC): completed per-slice spec artifacts + **both UX Design Spec instance types** (phase-level + per-feature) + CD-authored phase-level design file transferred to assigned_node working directory per §3.1
  - TK-11 code review output → Hub: per §3.2 (the specific code review tool — historically Codex — is governed by CC substantive canonical)
  - DS markdown export at TK-12 M4 merge (when DS instance changed): CD generates the export → Hub reviews it against DSG §15 → CC mirror, per [RULE] Design System Governance §12.3 / §12.7
- **Relationship to [RULE] Workspace Topology**: Companion. DTW imports WT constitutional residue's unit_type catalog and node-assignment interface contract; hub-to-assigned_node onboarding (after TK-02) implements WT's node assignment workflow.
- **Relationship to [RULE] Claude Code Architecture Rules**: Imports CCAR constitutional residue's tier identity; CC substantive CCAR owns the subagent roster, context scopes, paths, and skill loading rules consumed by TK-04+.
- **Relationship to [MECH] CI/CD Milestone Policy**: Imports M0–M5 gate identity from CI/CD constitutional residue; task-to-milestone mapping reflected in §0.3 with TK-13 as the terminal CI/CD task.
- **Relationship to [MECH] Application Lifecycle Handoff**: TK-12 merges feature branches directly to `main`. Application-level handoff to a human dev team is a distinct lifecycle event after one or more apps reach maturity per [MECH] Application Lifecycle Handoff §2; the AI-dev CI/CD chain terminates at TK-13 staging deploy.
- **Relationship to [RULE] Design System Governance**: TK-02 Step 2.3 implements DSG §13.3 Hub-side consumption discipline at two granularities: phase-level cross-cutting design file quality check + phase-level UX Design Spec instance authoring grounded in the design file's cross-cutting sections, plus per-feature design file quality check + per-feature UX Design Spec instance authoring grounded in each feature's labeled slice of the CD-authored phase-level design file. DSG §12 additive change requests are surfaced at TK-02 Step 2.3 when authoring a UX Design Spec instance reveals a gap in the current DS; cross-cutting additives are indexed in the phase-level instance §2A.6 with the originating feature's per-feature instance §2B.4 holding the authoritative plan content.
- **Relationship to [TPL] sources**: References TDD template, Intent-Acceptance Writing Standard, PRD+TDD Conversion Spec, Test Plan YAML Schema, UX Design Spec, and Design System Governance as artifact contracts.
- **Pairings I participate in**: P-03 (with [MECH] CI/CD constitutional residue §2 — milestone-to-TK anchoring), P-09 (with [MECH] CI/CD constitutional residue §2.7 — per-unit-type milestone profile), P-10 (with [RULE] WT constitutional residue §4 — node-assignment marker schema), P-31 (with [TPL] PRD §0.7 + [TPL] TDD §0.7). Pre-split pairings P-32 / P-38 / P-49 retired at this Hub residue level; substantive obligations migrate to CC.

## How to use this source (Hub-side)

Use this source when:
- Authoring Hub-side TDDs or handoff documentation that reference TK identifiers or per-unit-type task paths
- Reasoning about which workspace executes which TK
- Authoring TK-01, TK-02, TK-03 specifications (full Hub-authored substantive content below)
- Coordinating the M4 operator gate at TK-12
- Confirming a transition mechanism (§5) used between workspaces

Do not use this source as:
- A reference for CC-executed TK detailed mechanics (CC substantive DTW canonical)
- A subagent invocation reference for TK-04+ (CC substantive)
- A specific tool/command reference within TK-04+ execution (CC substantive)
- A tier architecture reference ([RULE] CCAR constitutional residue)
- A multi-node infrastructure reference ([RULE] WT constitutional residue)
- A milestone semantics reference ([MECH] CI/CD constitutional residue)

---

# 0. Boundary and position

## 0.1 What this source owns

- Task identity (TK-01 through TK-13 unit-internal-workflow tasks) and stage grouping. Project-level workspace inception (the once-per-monorepo setup that produces project-level scaffolding and singletons) is owned by [RULE] Workspace Topology constitutional residue §5 (workspace inception governance), not by this source; per-app physical skeleton is owned by CC substantive Workspace Topology canonical (walking-skeleton output set)
- Unit_type catalog: the three node-level work unit types `walking_skeleton`, `feature`, `app_integration` — their purpose, scope, deliverables, and per-unit-type task path through the TK sequence (§4 Unit_type catalog and per-unit-type task paths)
- Conditional brownfield reconstruct pre-step at TK-01 — triggered when an app has existing behavior worth preserving, producing an app-specific reconstruct memo as TK-01 input
- Cross-model review reminders at TK-01 and TK-02 sign-offs — advisory [Enforcement·reminder-only] reminders for the operator to consider invoking a cross-model spec review before signing off
- **TK-02 internal step structure** (Step 2.1 Hub-side TDD/test-plan/openapi/slice-list authoring → Step 2.2 CD-side phase-level design file production, conditional on any feature in the phase having `tier_1_involved=true` → Step 2.3 Hub-side design file quality checks + UX Design Spec instance authoring at two granularities: one phase-level instance + per-feature instances iterated over all tier-1-involved features)
- Role sequence per task, including which workspace (Hub Claude, Claude Design, assigned_node Claude Code) executes each task or sub-step
- File-level inputs and outputs, anchored to the repository layout in CC substantive Claude Code Architecture Rules canonical (repository layout)
- Trigger mechanism per task (manual / auto via hook / auto via Routine / conditional)
- Completion criterion and failure routing per task
- Human intervention budget
- Transition mechanism catalog
- TK-gate-related Hub Claude soft compliance trigger phrases (§9)

## 0.2 What this source does not own

- Three-workspace topology ([REF] Hub-CD-CC Architecture)
- Cross-tool handoff content contracts ([MECH] Cross-Tool Workflow Handoff)
- Application-level handoff to human dev team ([MECH] Application Lifecycle Handoff)
- Tier architecture ([RULE] Claude Code Architecture Rules §1)
- Subagent roster and permission model (CC substantive Claude Code Architecture Rules canonical (subagent roster))
- Repository layout structure (CC substantive Claude Code Architecture Rules canonical, repository layout)
- Milestone gate semantics and per-unit-type milestone profile ([MECH] CI/CD Milestone Policy §2)
- Code review tool command semantics, co-location mechanism, and per-unit-type fire conditions (owned by CC substantive Codex Plugin Usage canonical; Codex fully migrated to CC in Phase 3)
- Multi-node infrastructure, node identity, scheduling parity, parallel execution model, walking-skeleton-first ordering rule, walking-skeleton output canonical set, node assignment mechanics, GitHub Issue marker block format ([RULE] Workspace Topology §2, §4, §6)
- Design System governance, two-way DS distribution, CC-mirror sync mechanism ([RULE] Design System Governance, [REF] Hub-CD-CC Architecture §5.2)
- UX Design Spec instance content contract ([TPL] UX Design Spec)
- Artifact content contracts (respective [TPL] sources)
- Custom skill internal prompts (respective SKILL.md files)

## 0.3 Relationship to milestones

The base milestone-to-task mapping below applies to the `feature` and `walking_skeleton` unit types (slice-level execution path).

| Milestone | Mapped tasks | Stage |
|---|---|---|
| Pre-M0 | TK-01, TK-02 (Step 2.1 + Step 2.2 + Step 2.3), TK-03 | S1 |
| M0 Design Freeze | TK-04 entry self-check (folded into TK-04 start) + Hub TK-03 sign-off (design-freeze gate) | S2 |
| M1 Feature Slice | TK-04–TK-07 | S3 |
| M2 Integration Green | TK-08, TK-09 | S3 |
| M3 Pre-Release | TK-10 | S3 |
| M4 Merge | TK-11, TK-12 | S4 |
| M5 Staging Deploy | TK-13 | S4 |

Inception is a once-per-monorepo project-level setup outside the TK sequence and is not represented as a milestone row above.

## 0.4 Workspace-by-task summary

| TK | Executing workspace | Rationale |
|---|---|---|
| TK-01 | Hub Claude (HC + H collaboration) | Design thinking; phase PRD authoring; cross-model review reminder fires at sign-off |
| TK-02 Step 2.1 | Hub Claude (HC + H collaboration) | Phase TDD + phase test plan + per-feature integration test plans + per-feature slice-lists + openapi additive update + per-unit `assigned_node` decisions; cross-model review reminder fires at sign-off (applies to full TK-02 sign-off) |
| TK-02 Step 2.2 (conditional on any feature in the phase having `tier_1_involved=true`) | Claude Design (one CD session per phase, covering all tier-1-involved features in the phase) | Phase-level CD-authored design file with per-feature internal labeling (frame / section / page tag = feature-slug): hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations (CD-native; not markdown). Inputs: PRD relevant sections + TDD relevant sections for every tier-1-involved feature in the phase + attention prompt enumerating each feature and instructing per-feature labeling; CD grounds DS in its own instance (CD = DS SOT) per `[REF] Hub-CD-CC Architecture §5.2` |
| TK-02 Step 2.3 (when Step 2.2 fired) | Hub Claude (HC + H collaboration) | Two parallel tracks per `[TPL] UX Design Spec` §3 reviewer checklists: (a) **phase-level track** — design file quality check on the design file's cross-cutting sections (shell / vocabulary / touchpoint maps / phase-level decisions / VR naming) → phase-level UX Design Spec instance authoring (Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md`); (b) **per-feature track** — iterated per tier-1-involved feature: design file quality check against the feature's labeled slice (per `[RULE] DSG §13.3`) → per-feature UX Design Spec instance authoring (Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` from that slice) |
| TK-03 | Hub Claude (HC + H collaboration) | Per-slice intent + acceptance + test-plan authoring (main body + UX brief when Tier 1); consumes PRD + TDD + Hub-authored UX Design Spec instances (phase-level + active feature's per-feature instance from TK-02 Step 2.3) + the phase-level design file (focusing on the active feature's labeled slice plus phase-level cross-cutting sections as visual reference); the operator's GPT-Claude consensus loop at TK-03 sign-off serves as the de facto design freeze for the slice |
| TK-04 | **assigned_node Claude Code** | M0 entry self-check (the absorbed M0 gate function — lightweight verification that the spec bundle is intact upon CC reception, not a re-decision of design freeze); GitHub Issue marker authoring per [RULE] Workspace Topology constitutional residue §4 (node-assignment interface contract) (`status: in-progress`); first commit on feature branch; substantive code writing with SK-F auto-loaded for Tier 1 work |
| TK-05 → TK-11 | assigned_node Claude Code | Tests + adversarial + evidence + Codex code review at TK-11 |
| TK-12 | Hub Claude or assigned_node (operator's choice) | M4 review + smoke test; merge PR action (target = `main`) can fire from any workspace; DS markdown export sync (Hub + CC mirrors) when this slice carries a DS change finalization per [RULE] DSG §12.5 |
| TK-13 | TOOL (CI/CD) | Automated staging deploy on `main` merge — terminal AI-dev CI/CD task |

---

# 1. Scope and stage overview

Four stages:

- **S1 Specification production per phase + per slice**:
  - **TK-01** — hub-side: phase PRD. Cross-model review reminder fires at sign-off ([Enforcement·reminder-only])
  - **TK-02** — hub-side production of phase TDD + phase test plan + per-feature integration test plans + per-feature slice-lists + openapi additive update + per-unit `assigned_node` decisions for all units in the phase (`walking_skeleton` Phase 1 only, each `feature` unit, each `app_integration` unit). **TK-02 has three internal steps**:
    - **Step 2.1** — Hub-side TDD/test-plan/openapi/slice-list authoring (always runs)
    - **Step 2.2** — CD-side phase-level design file production (runs once per phase when any feature in the phase has `tier_1_involved=true`; skipped entirely when no features in the phase touch Tier 1). CD produces a single phase-level design file with per-feature internal labeling per [REF] Hub-CD-CC Architecture §3.4.1; the Hub session at TK-02 hands CD the PRD + TDD relevant sections for all tier-1-involved features in the phase as drop files, with an attention prompt enumerating each feature, directing CD to UI-relevant sections per feature, and instructing CD to internally label per-feature design file scope (frame / section / page tag = feature-slug)
    - **Step 2.3** — Hub-side design file quality checks + UX Design Spec instance authoring at two granularities (runs when Step 2.2 fired). Produces: (a) one **phase-level UX Design Spec instance** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` — Hub Claude verifies the design file's cross-cutting sections (shell / shared vocabulary / touchpoint maps / phase-level decisions / VR naming convention) are spec-ready per [TPL] UX Design Spec §3A.1, then authors the phase-level instance per [TPL] UX Design Spec §2A; (b) **per-feature UX Design Spec instances** iterated per tier-1-involved feature — for each feature, Hub Claude locates that feature's labeled slice in the phase-level design file, verifies the slice is spec-ready against that feature's PRD/TDD scope per [RULE] DSG §13.3 + [TPL] UX Design Spec §3B.1, then authors that feature's instance as markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` per [TPL] UX Design Spec §2B
  - **TK-03** — hub-side: per-slice intent + acceptance + test-plan (main body + UX brief when Tier 1 involved, drawing from both Hub-authored UX Design Spec instances — phase-level for cross-feature touchpoints / shared vocabulary, per-feature for in-slice UX — from TK-02 Step 2.3 and design files as visual reference). Runs for `feature` and `walking_skeleton` units only; not for `app_integration`. The operator's GPT-Claude consensus loop at TK-03 sign-off serves as the de facto design freeze gate.
- **S2 CC entry**: M0 entry self-check + GitHub Issue marker + first commit on feature branch (folded into the start of TK-04). Runs for `feature` and `walking_skeleton` units only; `app_integration` units skip M0 / M1 entirely (entry at TK-08).
- **S3 Claude Code implementation and validation**: Code + tests + adversarial + evidence. TK-04 to TK-11. `app_integration` units enter S3 at TK-08 directly.
- **S4 Merge gate and deployment**: M4 merge to `main` + M5 staging deploy. TK-12 to TK-13. Production deployment is the receiving company's CI/CD scope after handoff per [MECH] Application Lifecycle Handoff §0.2 and is not part of this source's TK sequence.

**Foundation prerequisite (outside this source)**: Project-level workspace inception is owned by [RULE] Workspace Topology constitutional residue §5 (workspace inception governance) and runs once before any TK-01 begins. Per-app physical skeleton is owned by CC substantive Workspace Topology canonical (walking-skeleton output set) and is produced as part of the first phase's walking_skeleton unit at TK-04 onwards on the assigned_node — not as a hub-side pre-TK step.

---

# 2. Role catalog

Three classes of roles are referenced across tasks in this source.

## 2.1 Workflow-specific roles (defined here)

| Code | Role |
|---|---|
| H | Operator (sole human owner) |
| HC | Hub Claude (Claude.ai Project chat) |
| CD | Claude Design (claude.ai/design) |
| CC | Claude Code main loop on assigned_node |
| TOOL | Automated toolchain; not a subagent |

## 2.2 Subagent roster (defined in CC substantive Claude Code Architecture Rules canonical (subagent roster))

Subagent codes (`A1`, `A2`, … as used in §4 task definitions) reference the CC subagent roster of the Development Track. The roster's membership, count, conditional-enablement, names, purposes, primary invocation tasks, and context scopes are owned by CC substantive Claude Code Architecture Rules canonical (subagent roster) as the single source of truth.

When task definitions in §4 mention these codes with a parenthetical role name (e.g., "A5 (unit-test-auto-repair)"), the parenthetical is a reading convenience; Architecture Rules §5.1 remains authoritative for any discrepancy.

The subagent roster is a single shared definition in the CC `.claude/` canonical layer, deployed identically across all dev nodes per [RULE] Workspace Topology constitutional residue §2 (parity discipline). Each node runs single subagent instances; same-node multi-slice parallelism uses git worktree isolation per CC substantive Workspace Topology canonical (same-node multi-slice parallelism).

## 2.3 External tool and skill roles (defined in their own canonical sources)

| Code | Role | Owner source |
|---|---|---|
| CX | Code review tool (historically Codex plugin) | CC substantive Codex Plugin Usage canonical (post-Phase-3 migration) |
| SK-F | `hdc-arco-enterprise-ui` skill | `.claude/skills/hdc-arco-enterprise-ui/SKILL.md` |
| SK-W | `hdc-wcag-accessibility-checker` skill | `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md` |

---

# 3. Path and placeholder catalog

## 3.1 Path catalog (delegated)

The full repository layout — `HDC_ROOT/`, `apps/{app-slug}/`, `packages/domain/{domain-name}/`, `.claude/` — is owned by CC substantive Claude Code Architecture Rules canonical (repository layout). Task definitions in §4 reference paths under that layout without restating it here.

## 3.2 Spec-artifact paths

Spec-artifact paths are stated inline in the §4 task definition that produces or consumes each artifact; the repository layout is owned by CC substantive Claude Code Architecture Rules canonical (repository layout) per §3.1 and is not restated here. Cross-workspace handoff-interface paths — Test Evidence Report, operator digest, OpenAPI output gate, per-slice evidence — are declared constitutionally by [MECH] CI/CD Milestone Policy §1.2 / §3.1 / §3.3 / §4.1.

## 3.3 Placeholder definitions

| Placeholder | Definition | Uniqueness scope |
|---|---|---|
| `{app-slug}` | Kebab-case app identifier, `[a-z0-9-]`, English, frozen on first declaration | Globally unique within `HDC_ROOT/apps/` |
| `{N}` | Phase number, positive integer, monotonic per app (Phase 1 = 0→1; Phase N≥2 = additive iteration) | App-internal sequence; one phase number per app per phase |
| `{domain-name}` | Kebab-case domain identifier, `[a-z0-9-]`, descriptive of business capability, frozen | Globally unique within `HDC_ROOT/packages/domain/` |
| `{feature-slug}` | Kebab-case feature identifier, `[a-z0-9-]`, English, frozen; a feature is introduced or evolved within a phase | App-internal uniqueness only; global feature identity = `{app-slug}/{feature-slug}` |
| `{slice-id}` | `{feature-slug}-{slice-seq}-{slice-name}` | Feature-internal; global slice identity = `{app-slug}/{feature-slug}/{slice-id}` |
| `{module}` | Module name within a tier | Tier-internal |
| `{flow}` / `{screen}` / `{scenario}` | E2E flow, visual/accessibility target screen, performance scenario | Test-suite-internal |
| `{app-slug}-bff_{domain-name}` | Pact contract test pair name (consumer-driven; per CC substantive Claude Code Architecture Rules canonical (app-slug roster)) | Globally unique within HDC_ROOT |
| `{skill-name}` | Custom skill kebab-case identifier | `.claude/skills/`-internal |
| `{locale}` | BCP 47 locale (e.g., `en`, `zh-CN`, `ja`) | App-internal |
| `{change-id}` | DS change identifier | DS governance-specific path per [RULE] Design System Governance |

## 3.4 Glossary

**app**: An application container under `apps/{app-slug}/`. Each app has its own frontend (Tier 1), BFF (Tier 2), specs, tests, evidence, and reports. App identity is decoupled from feature identity; one app contains many features over its lifetime. An app's lifetime is partitioned into phases; phase identity sits between app and feature.

**phase**: The top-level granularity of an app's lifecycle. Phase 1 (`{N}=1`) takes the app from 0 to 1 — establishing foundational architecture, cross-feature baselines, walking skeleton scope, and the initial feature set. Phase N≥2 is an additive iteration that adds or evolves features under the established baselines without re-establishing them. One phase produces one paired phase PRD + phase TDD + phase test plan (master) + per-feature integration test plans + per-feature slice-lists + (when any feature has `tier_1_involved=true`) one phase-level UX Design Spec instance plus per-feature UX Design Spec instances (one per tier-1-involved feature). Phase identity is per-app, not project-wide; different apps may be at different phase numbers.

**domain**: Tier 3 capability package under `packages/domain/{domain-name}/`. DTW does not own this term — the substantive definition is owned by the CC substantive Claude Code Architecture Rules canonical; see that source.

**feature-slug**: short stable machine-friendly identifier for a feature (kebab-case, English, frozen once created). App-internal uniqueness only.

**work unit (or simply unit) / unit_type**: Node-level assignment granularity; a phase's work is partitioned into work units, each of one of three unit types. The unit_type catalog (the three types, their scope and per-unit-type task path) is defined in §4.0.1; node-assignment of units to nodes is owned by [RULE] Workspace Topology §6.

**unit_id**: Kebab-case stable identifier unique within the app's phase. Recommended naming: `walking-skeleton` for the Phase 1 walking_skeleton unit; the `feature-slug` for `feature` units; `app-int-phase-{N}` for `app_integration` units.

**slice**: smallest unit of work that completes the M0 → M5 evidence chain on a single dev node. A `feature` unit decomposes into one or more slices at TK-02; a `walking_skeleton` unit consists of exactly one slice (the thinnest end-to-end vertical slice that proves foundational architecture); an `app_integration` unit has zero customer-facing slices (its single PR runs the M2–M5 subset directly).

**slice-id**: slice-level identifier extending feature-slug, e.g., `manager-e-signature-01-initiation`.

**assigned_node**: the logical node that executes the unit's first node-side TK and all subsequent TKs; decided at TK-02 as a first-class output for each unit. The logical-node naming convention is owned by [RULE] Workspace Topology constitutional residue §1.2.

**cross-model review reminder**: An [Enforcement·reminder-only] advisory surfaced at TK-01 and TK-02 sign-off suggesting the operator consider obtaining a review of the produced spec from a model other than the one that produced it (e.g., Codex, a different Claude variant). The reminder is conversational; the operator may invoke a cross-model review or proceed without one. See §4 TK-01 / TK-02 task definitions.

**brownfield reconstruct memo**: A TK-01 conditional pre-step output produced when an app has existing behavior worth preserving. The memo extracts existing PRD content, TDD content, and observed code behavior into a structured reference for the new phase PRD's authoring. See §4 TK-01 task definition.

**design file** (CD-authored): The phase-level visual artifact produced by CD in TK-02 Step 2.2 when any feature in the phase has `tier_1_involved=true`. One design file per phase covers all tier-1-involved features in the phase as per-feature labeled internal scopes (frame / section / page tag = feature-slug). CD-native format (hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations). Distinct from the per-feature UX Design Spec instances, which are the Hub-authored markdown counterparts authored at TK-02 Step 2.3, each grounded in the corresponding labeled slice.

**UX Design Spec instance** (Hub-authored): Two granularities of markdown spec authored by Hub Claude at TK-02 Step 2.3 per [TPL] UX Design Spec. (a) **Phase-level instance** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` — one per phase when Step 2.2 fires; synthesizes the design file's cross-cutting sections (platform shell, shared visual vocabulary, cross-feature touchpoints, phase-level decisions, VR naming convention, cross-cutting additive index). (b) **Per-feature instance** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` — one per tier-1-involved feature; synthesizes the corresponding labeled slice of the design file. Both markdown forms are for AI-RAG consumption (Hub TK-03 + CC TK-04+).

---

# 4. Task catalog

Thirteen tasks total (TK-01 through TK-13). Scope levels and per-unit-type applicability are summarized below; the formal unit_type catalog with per-unit-type task path is in §4.0 immediately following.

**Inception is not a TK**: Project-level workspace inception (per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance)) and per-app physical skeleton (per CC substantive Workspace Topology canonical (walking-skeleton output set)) are owned outside this source. The TK sequence begins at TK-01 for the first phase of each app.

**Note on "Required" in task descriptions**: each task definition in §4 below includes a `**Human intervention**: **Required**` (or `**Conditional**` / `**None**`) field. The word "Required" here denotes the task's **expected level of operator attention** as a taxonomic classifier — it describes how the task is designed to be operated, not a hard mechanism that can compel operator presence. Per [Enforcement·reminder-only] discipline, "Required" tasks are **reminder-enforced**: Hub Claude surfaces the expected attention level at task initiation and does not auto-execute the task past the operator sign-off point, but it cannot canonical-text-enforce operator presence. Proceeding past a "Required" task without operator sign-off is the §8 anti-drift red flag — the classifier and the §8 red flag are two views of the same rule. The classifier reads as: "Required" = task designed for operator-driven execution, reminder-enforced at the sign-off point; "Conditional" = task auto-runs unless failure surfaces operator-needed escalation; "None" = task fully autonomous in steady state. See CC substantive CI/CD Milestone Policy canonical (tooling baseline) for the operator attention allocation rationale underlying this taxonomy.

- **TK-01, TK-02** — **per-phase**, runs once per app per phase; TK-01 produces phase PRD; TK-02 has three internal steps (Step 2.1 / Step 2.2 / Step 2.3) producing phase TDD, phase test plan (master), per-feature integration test plans, per-feature slice-lists, per-unit `assigned_node` decisions, and — when any feature in the phase has `tier_1_involved=true` — one phase-level CD-authored design file with per-feature internal labeling plus Hub-authored UX Design Spec instances at two granularities (one phase-level instance + per-feature instances, one per tier-1-involved feature)
- **TK-03 through TK-11** — **per-slice within a unit**, looping through slices of `feature` units and the single slice of a `walking_skeleton` unit; not run for `app_integration` units below TK-08 (per §0.3 milestone table and §4.0 per-unit-type task paths)
- **TK-08 through TK-13** — entered directly by `app_integration` units at TK-08 (M2 entry); for `feature` and `walking_skeleton` units, reached as part of the slice's M0 → M5 progression
- **TK-12 through TK-13** — per-slice for slice-bearing units; per-unit (single PR) for `app_integration` units

Within a single phase, the loop structure for `feature` and `walking_skeleton` units is: TK-01 → TK-02 (Step 2.1 → Step 2.2 → Step 2.3) → (for each unit: for each slice in the unit: TK-03 through TK-11) → TK-12 onwards.

The Phase 1 `walking_skeleton` unit must reach `status: merged` before any `feature` unit's TK-03 or any `app_integration` unit's TK-08 begins, per [RULE] Workspace Topology constitutional residue §3 (walking-skeleton-first ordering rule). For `app_integration` units, the loop is: TK-01 → TK-02 (consumed as input) → TK-08 → TK-09 → TK-10 → TK-11 → TK-12 onwards.

## 4.0 Unit_type catalog and per-unit-type task paths

### 4.0.1 Catalog overview

The phase ontology partitions a phase's work into `walking_skeleton` / `feature` / `app_integration` work units. The three unit types share scheduling parity at the node-assignment level (per CC substantive Workspace Topology canonical (parallelism unit)) and run different subsets of the TK-XX sequence based on their slice ontology.

| Unit type | Applicability | Slice count | Milestone profile | Cardinality per phase |
|---|---|---|---|---|
| `walking_skeleton` | Phase 1 only | exactly 1 | M0 → M1 → M2 → M3 → M4 → M5 (full chain) | exactly 1 (Phase 1); 0 (Phase N≥2) |
| `feature` | All phases | 1+ | M0 → M1 → M2 → M3 → M4 → M5 per slice (full chain) | 1+ |
| `app_integration` | All phases (per-phase only; not cross-phase) | 0 | M2 → M3 → M4 → M5 (truncated; no M0 / M1) | 0+ |

Per-unit-type milestone profile is owned by [MECH] CI/CD Milestone Policy. Per-unit-type code review tool fire conditions are owned by CC substantive Codex Plugin Usage canonical (post-Phase-3 migration). Code review fires at M4 (TK-11) for all three unit types; cross-model review reminders at TK-01 / TK-02 sign-offs are operator-advisory and are not Codex invocations.

A `feature` unit runs the standard TK-01 through TK-13 path with one iteration of TK-03 through TK-11 per slice; the unit's **last slice** runs an expanded TK-08 scope for feature integration test execution per [MECH] CI/CD Milestone Policy. `walking_skeleton` and `app_integration` units carry real task-path deviations, detailed in §4.0.2 and §4.0.3 below.

### 4.0.2 Walking_skeleton unit task path

A `walking_skeleton` unit produces six outputs in a single PR (canonical list owned by CC substantive Workspace Topology canonical (walking-skeleton output set)). The unit consists of exactly one slice that runs the full TK chain.

| TK | Walking_skeleton-specific notes |
|---|---|
| TK-01 | Phase 1 PRD; covers all features in Phase 1 plus implicit walking-skeleton scope |
| TK-02 | Phase 1 TDD §3 Walking skeleton scope is authored alongside per-feature `§4.{feature-slug}` sections in Step 2.1; walking_skeleton unit's `assigned_node` is decided alongside per-feature node assignments in Step 2.1; if walking-skeleton scope itself touches Tier 1 (rare), Step 2.2 + Step 2.3 include the walking-skeleton scope as a labeled slice within the phase-level design file, the phase-level UX Design Spec instance is produced as for any tier-1-involved phase, and a per-feature UX Design Spec instance is produced for the walking-skeleton scope (treated as the `walking-skeleton` feature-slug-equivalent) |
| TK-03 | Single-slice authoring; `slice-id` = `walking-skeleton`; Hub-side per [REF] Hub-CD-CC Architecture §5.1; UX brief drawn from Hub-authored UX Design Spec instances (phase-level + walking-skeleton per-feature instance) from TK-02 Step 2.3 if walking-skeleton scope touches Tier 1 |
| TK-04 | M0 entry self-check (folded into TK-04 entry per the post-refactor architecture; the prior separate M0 gate task has been retired); GitHub Issue marker authoring; first commit on `feature/<app-slug>/walking-skeleton` branch; produces the six walking_skeleton outputs in the single PR per CC substantive Workspace Topology canonical (walking-skeleton output set); CC main loop begins code generation |
| TK-05 → TK-10 | Single-slice loop continues: tests, adversarial, evidence |
| TK-11 | M4 prep + code review fires per CC substantive Codex Plugin Usage canonical |
| TK-12 | M4 merge as for any unit |
| TK-13 | M5 staging deploy on `main` merge |

### 4.0.3 App_integration unit task path

| TK | App_integration-specific notes |
|---|---|
| TK-01, TK-02 | Consumed as input (phase test plan + feature integration test plans); `app_integration` unit's `assigned_node` is decided in TK-02 Step 2.1 alongside other unit assignments |
| TK-03 → TK-06 | **Not applicable** (no slice-level new feature code; no M0 / M1 within the unit) |
| TK-07 | Not run as part of the unit's standard path, but **reachable on test failure** — see the TK-07 note below the table |
| TK-08 | Entry point; scope expanded to phase test plan cross-feature scenarios + feature integration variants + app-scale NFR |
| TK-09 | Standard M2 adversarial loop |
| TK-10 | Standard M3 pre-release validation |
| TK-11 | M4 prep + Codex code review fires (review target: PR diff including integration test code) |
| TK-12 | M4 merge as for any unit |
| TK-13 | M5 staging deploy on `main` merge |

TK-07 RCA may fire for an `app_integration` unit when its TK-08 / TK-09 / TK-10 tests fail; routing per the standard TK-07 mechanics, with the failed test context drawn from the app_integration's own test code rather than slice-level whitebox tests.

---

## TK-01: Produce phase PRD

- **Workspace**: Hub Claude
- **Stage**: S1; **Milestone**: Pre-M0
- **Scope**: per-phase per-app (one execution produces the PRD for one phase of one app)
- **Role sequence**: H + HC (iterative collaboration)
- **Inputs**: Business needs signal for the target phase; existing PRDs under `apps/*/specs/prd/**` (especially the prior phase PRD if `{N}≥2`); target `{app-slug}`; target `{N}` (phase number, monotonic per app); **conditional**: brownfield reconstruct memo (per TK-01 conditional pre-step below) when an app has existing behavior worth preserving
- **Outputs**: Phase PRD content for `apps/{app-slug}/specs/prd/phase-{N}.md` (committed to the active phase's working branch ahead of TK-03 per-slice extraction)
- **Prerequisite**: workspace inception complete per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance). For Phase N≥2 of an existing app, the prior phase's TK-13 release (or equivalent stable boundary) should also be reached. For Phase 1 of a new app, the `{app-slug}` is decided in this task per operator pure judgment (immutable once committed) and added to the frozen app-slug roster maintained at workspace level per CC substantive Claude Code Architecture Rules canonical (app-slug roster); the app's physical skeleton is produced subsequently as part of the Phase 1 walking_skeleton unit's output set per CC substantive Workspace Topology canonical (walking-skeleton output set)
- **Trigger**: **Manual**
- **Completion**: Phase PRD uses [TPL] PRD template; business-facing; `app_slug` and `phase_number` fields populated in PRD header per [TPL] PRD §0.7.1; §7.1 Feature List enumerates the features introduced or evolved in this phase by `feature-slug`; operator signs off; **cross-model review reminder fires at sign-off** (see below)
- **Failure routing**: Revise within TK-01
- **Human intervention**: **Required**

**Conditional brownfield reconstruct pre-step** ([Enforcement·reminder-only]): When the operator judges that an app has existing behavior worth preserving (e.g., a brownfield migration into HDC's AI-dev track; an app returning from a human dev team via [MECH] Application Lifecycle Handoff §5 re-entry with the operator wanting to preserve baseline behavior; a refactor scope that touches multiple existing features), TK-01 starts with a reconstruct pre-step. The enforcement tag indicates this pre-step is operator-discretion: Hub Claude surfaces a reminder when TK-01 is initiated for an app with existing behavior context, but the operator decides whether to invoke the reconstruct step or proceed directly to phase PRD authoring.

1. Operator identifies the existing PRD / TDD / observed behavior sources to reconstruct
2. Hub Claude assists in producing an `apps/{app-slug}/specs/brownfield-reconstruct-memo.md` summarizing existing behavior in PRD-shaped narrative (features, user flows, constraints)
3. The memo is consumed as TK-01 input alongside business needs for the target phase
4. The memo itself is not a phase PRD; it informs the new phase PRD authoring

The reconstruct process is reused across brownfield TK-01 invocations; the memo artifact is per-app, not reusable across apps. The pre-step is conditional — Phase 1 of a fully greenfield app does not trigger it.

**Cross-model review reminder at sign-off** ([Enforcement·reminder-only]): When the operator initiates TK-01 sign-off, Hub Claude surfaces a reminder suggesting the operator consider obtaining a review of the PRD from a model other than the one that produced it (e.g., Codex review, an alternate Claude variant review). The reminder is conversational; the operator may invoke a cross-model review or proceed without one. Cross-model review at this point is preventive (catching framing errors before they propagate to TK-02 and beyond); it is not a hard gate.

**Phase scope note**: A phase PRD covers all features introduced or evolved in that phase. The granularity shift from per-feature to per-phase is a structural decision; per-feature business framing still appears inside the phase PRD as feature-scoped sub-sections, but PRD-level identity is `{app-slug}/phase-{N}`, not `{app-slug}/{feature-slug}`.

---

## TK-02: Produce phase TDD + phase test plan + feature integration test plans + per-feature slice-lists + per-feature node assignments + (conditional) phase-level design file + UX Design Spec instances (phase-level + per-feature)

TK-02 is a multi-step task with three internal steps: Step 2.1 (Hub-side core spec authoring) → Step 2.2 (CD-side phase-level design file production, conditional on any feature in the phase having `tier_1_involved=true`) → Step 2.3 (Hub-side design file quality checks + UX Design Spec instance authoring at two granularities — one phase-level instance covering cross-cutting UX content + per-feature instances iterated per tier-1-involved feature). The three steps execute in order, with Step 2.2 / Step 2.3 conditional on whether any feature in the phase has `tier_1_involved=true`. The overall TK-02 sign-off covers all three steps.

- **Workspace**: Hub Claude (Step 2.1 + Step 2.3) + Claude Design (Step 2.2, conditional)
- **Stage**: S1; **Milestone**: Pre-M0
- **Scope**: per-phase per-app (one execution produces all TK-02 outputs for one phase)

### Step 2.1 — Hub-side core spec authoring (always runs)

- **Workspace**: Hub Claude
- **Role sequence**: H + HC (coordinated production of multiple paired artifacts; operator decides each feature's and each unit's `assigned_node` during this step)
- **Inputs**: Phase PRD (TK-01); existing TDDs under `apps/*/specs/tdd/**` (especially the prior phase TDD if `{N}≥2`, used as architectural baseline); current node availability state (operator's pure-judgment input per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 1))
- **Outputs** (paired output set; the count of each varies with the number of features in the phase):
  - **Per-unit `assigned_node` decisions** — one decision per work unit in the phase (recorded inside `§4.{feature-slug}.Header` of the phase TDD for `feature` units; in TDD §3 walking skeleton header for the Phase 1 `walking_skeleton` unit; in the GitHub Issue marker block for `app_integration` units which lack a per-feature TDD section)
  - **Phase TDD** content for `apps/{app-slug}/specs/tdd/phase-{N}.md` — header mandatory fields: `app_slug`, `phase_number`, `Features in this phase`; body sections per [TPL] TDD: §1 architecture, §2 cross-feature concerns, §3 walking skeleton scope (Phase 1 only), §4 per-feature engineering spec. Each feature's `§4.{feature-slug}.Header.tier_1_involved` flag is set here. When any feature in the phase has `tier_1_involved=true`, the TDD references both UX Design Spec instance paths — the phase-level instance at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` plus the per-feature instances at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`; the UX coverage itself lives in the UX Design Spec instances (Hub-authored at Step 2.3) rather than as TDD sub-sections
  - **Phase test plan (master, markdown)** content for `apps/{app-slug}/specs/test-plan/phase-{N}.md` per [TPL] Test Plan Schema §2
  - **Feature integration test plans (yaml)** — one per feature in the phase, at `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` per [TPL] Test Plan Schema §3
  - **Per-feature slice-lists** — one per feature in the phase, at `apps/{app-slug}/specs/slice-list/{feature-slug}.md` per [TPL] TDD `§4.{feature-slug}.Slice-List`
  - **App-scoped openapi additive update** — `apps/{app-slug}/specs/openapi.yaml` updated with new or evolved API surfaces from this phase

### Step 2.2 — CD-side phase-level design file production (conditional)

- **Workspace**: Claude Design (one CD session per phase, covering all tier-1-involved features in the phase)
- **Condition**: fires once per phase when at least one feature has `§4.{feature-slug}.Header.tier_1_involved=true` in the TDD authored at Step 2.1. Skipped entirely when no features in the phase touch Tier 1.
- **Role sequence**: H (initiates the phase-level CD session, transfers Hub drop files for all tier-1-involved features) + CD (authors the phase-level design file within its native workspace)
- **Inputs** (per phase; transferred to CD as drop files with an attention prompt directing CD to UI-relevant sections per feature):
  - For each tier-1-involved feature in the phase: phase PRD relevant sections (the feature's PRD sub-sections covering user value, scenarios, user flows) + phase TDD relevant sections (the feature's `§4.{feature-slug}.Header` + `§4.{feature-slug}.Module-Decomposition` + `§4.{feature-slug}.API-Contracts` summary at UI-relevance level — enough for CD to ground component selection in the actual data and interaction surfaces)
  - Attention prompt enumerating each tier-1-involved feature with per-feature UI-relevant pointers, plus the per-feature internal labeling instruction (frame / section / page tag = feature-slug) so Hub Step 2.3 can locate each feature's slice
  - DS grounding: CD grounds component selection in its own DS instance (CD is the DS SOT per [REF] Hub-CD-CC Architecture §5.2); no separate DS reference is transferred per cycle. Per [REF] Hub-CD-CC Architecture §3.4.1, CD is the design-file author and consults DS content for component / pattern selection.
- **Outputs** (one phase-level design file, CD-native format with per-feature internal labeling; transferred back to Hub for Step 2.3):
  - Hi-fi mockups for all affected Tier 1 screens across all tier-1-involved features in the phase
  - Prototypes / wireframes for interaction flows where static mockups are insufficient
  - Component callouts identifying which DS components are used per screen
  - Interaction flows with embedded textual annotations (state transitions, edge cases, empty/loading/error states)
  - Per-feature internal labeling (frame / section / page tag = feature-slug) so each tier-1-involved feature's design scope is locatable for Hub Step 2.3 grounding
  - Any new-component / new-token proposals (these inform Step 2.3's UX Design Spec §2B.4 entry on the originating per-feature instance; cross-cutting additives — used across multiple features in the phase — additionally inform the phase-level instance's §2A.6 cross-cutting additive index; the DS change request itself is per [RULE] DSG §12)
- **Trigger**: Operator manual (after Step 2.1 TDD is drafted and `tier_1_involved` flags are set; operator opens one CD session for the phase covering all tier-1-involved features)
- **CD input strategy v1**: Full relevant PRD + TDD sections for all tier-1-involved features as drop files + attention prompt enumerating each feature and directing CD to UI-relevant sections per feature plus per-feature internal labeling. (Hub does not pre-extract a "UI summary"; the rationale is preserving signal-to-noise without dropping interaction-relevant content — see TK-02 Step 2.2 mechanism note below.)

### Step 2.3 — Hub-side design file quality checks + UX Design Spec instance authoring (conditional, runs when Step 2.2 fired)

- **Workspace**: Hub Claude
- **Condition**: runs when Step 2.2 fired; produces (a) **exactly one phase-level UX Design Spec instance** for the phase, and (b) **one per-feature UX Design Spec instance per tier-1-involved feature** (iterated over all such features). Both tracks consume the same CD-authored phase-level design file; the phase-level track grounds in the design file's cross-cutting sections, the per-feature track iterates per feature against each labeled slice
- **Role sequence**: H + HC, in two parallel-able tracks:
  - **Phase-level track**: design file quality check on cross-cutting sections (§3A.1) first; phase-level UX Design Spec instance authoring (§3A.2) second
  - **Per-feature track**: per feature: design file quality check on the feature's labeled slice (§3B.1) first; per-feature UX Design Spec instance authoring (§3B.2) second
  - The two tracks may interleave (phase-level draft can begin while per-feature checks iterate), but TK-02 sign-off requires both tracks' authoring quality checks to pass
- **Inputs** (one phase-level design file consumed by both tracks):
  - CD-authored phase-level design file from Step 2.2 (transferred to Hub per [MECH] Cross-Tool Workflow Handoff §2.2), with cross-cutting sections (shell artboards, vocabulary artboards, touchpoint maps, phase-level decision logs, VR naming annotations) + per-feature internal labeling (frame / section / page tag = feature-slug)
  - Phase PRD + phase TDD (phase-level track uses §1 + §2 + (Phase 1) §3; per-feature track uses each iteration's active feature's relevant sections)
  - **[RULE] DSG** §13.3 — the Hub-side consumption discipline governing this step (design file quality checks are spec-readiness reviews against the relevant PRD/TDD scope; UX Design Spec authoring is grounded in the relevant design file content — cross-cutting sections for the phase-level instance, labeled slice for each per-feature instance)
  - [TPL] UX Design Spec (the spec contract authored as Hub-authored markdown at two granularities)
  - [TPL] UX Design Spec §3A reviewer checklists (phase-level track); §3B reviewer checklists (per-feature track)
- **Outputs**:
  - Phase-level track:
    - Phase-level design file quality check disposition recorded in conversation log (`Pass` / `Pass with annotation` / `Reject — return to CD for revision`) per [TPL] UX Design Spec §3A.1
    - **Phase-level UX Design Spec instance markdown** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` per [TPL] UX Design Spec §2A
  - Per-feature track (per tier-1-involved feature):
    - Per-feature design file quality check disposition recorded in conversation log per [TPL] UX Design Spec §3B.1
    - **Per-feature UX Design Spec instance markdown** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` per [TPL] UX Design Spec §2B
  - Cross-track conditional:
    - DS change request entries — feature-specific additives captured as the originating feature's per-feature instance §2B.4 New-Components-Or-Tokens; cross-cutting additives additionally indexed in the phase-level instance §2A.6 cross-cutting additive index with the originating feature designated (the per-feature §2B.4 entry remains the authoritative plan content per [RULE] DSG §12.4); breaking changes are routed as separate change files per [RULE] DSG §12.2
- **Mechanism**:
  - **Phase-level track**:
    1. Hub Claude reviews the design file's cross-cutting sections (shell / vocabulary / touchpoint maps / phase-level decisions / VR naming) per [TPL] UX Design Spec §3A.1 — verifies coverage, alignment with TDD, and grounding sufficiency
    2. If disposition is `Reject`: route back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.2 redo scope is the phase-level cross-cutting sections
    3. If `Pass` or `Pass with annotation`: Hub Claude authors the phase-level instance markdown grounded in those sections per [TPL] UX Design Spec §2A — including the `Per-feature instances in this phase` header listing every tier-1-involved feature, the §2A.3 touchpoint matrix cross-referencing per-feature instances, and the §2A.6 cross-cutting additive index when applicable
  - **Per-feature track** (iterated per tier-1-involved feature):
    1. Hub Claude locates the feature's labeled slice in the phase-level design file (frame / section / page tag = feature-slug); if the labeling is missing or ambiguous, route to the failure path with scope = full-phase relabeling
    2. Hub Claude verifies that slice is spec-ready per [TPL] UX Design Spec §3B.1 — confirms the slice is complete against the feature's PRD/TDD scope, internally consistent, and carries annotations rich enough to author the per-feature instance from (DS-conformance of the design file is CD's responsibility as DS owner per [RULE] DSG §13.3)
    3. If disposition is `Reject — return to CD for revision`: route back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.3 pauses for this feature until a revised design file (with the corrected slice, or with corrected labeling) is transferred back. Other features' iterations and the phase-level track may proceed in parallel if their checks passed
    4. If `Pass` or `Pass with annotation`: Hub Claude authors that feature's per-feature instance markdown grounded in the feature's design file slice (every `component: <name>` reference is transcribed from a component callout in the slice; every token and layout-pattern reference likewise traces to the slice's annotations); the instance header carries `Phase-level UX Design Spec ref: ../phase-{N}.md`
    5. If new components or tokens are needed for this feature: Hub Claude authors the §2B.4 New-Components-Or-Tokens entry capturing the additive plan per [RULE] DSG §12.4 change content structure; if the additive is cross-cutting (used by other features in the phase), also adds an index entry in the phase-level instance §2A.6 cross-referencing this feature's §2B.4 entry; the actual DS instance content change is authored by CD at the originating feature's M4 → merge-to-main milestone per DSG §12.5

### TK-02 task-level fields (apply to the full three-step task)

- **Prerequisite**: TK-01
- **Trigger**: **Manual**
- **Completion**: Phase TDD uses [TPL] TDD template; `Features in this phase` matches phase PRD §7.1 feature list; per-feature module decomposition MECE within each feature; openapi covers all TDD-introduced API surfaces; each feature's slice-list slices are single-objective; phase test plan exit criteria are testable; per-feature `assigned_node` decided; cross-tier traceability consistent; **when any feature has `tier_1_involved=true`**: the phase-level CD-authored design file is complete (cross-cutting sections + per-feature labeled internal slices) and both Step 2.3 tracks pass — phase-level design file quality check disposition is `Pass` or `Pass with annotation`, per-feature design file quality check disposition is `Pass` or `Pass with annotation` for each tier-1-involved feature; **phase-level UX Design Spec instance** markdown authored at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` and signs off the §3A.2 authoring quality check; **per-feature UX Design Spec instance** markdown authored at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` for each tier-1-involved feature and signs off the §3B.2 authoring quality check; operator signs off the full output set; **cross-model review reminder fires at sign-off** (per TK-01 mechanics applied to TDD; the reminder applies to the TDD specifically — the operator may invoke cross-model review of architecture decisions in §1 + §2 + §4 + walking-skeleton scope)
- **Failure routing**: Phase PRD gaps → TK-01; MECE violation → revise within Step 2.1; **phase-level design file quality check `Reject` disposition → return to CD per [MECH] Cross-Tool Workflow Handoff §6, Step 2.2 redo scope is the phase-level cross-cutting sections**; **per-feature design file quality check `Reject` disposition → return to CD per [MECH] Cross-Tool Workflow Handoff §6, Step 2.2 redo scope is the affected feature's slice (or full-phase relabeling when per-feature labeling itself is broken)**; **UX Design Spec authoring gap (Hub Claude finds the design file's cross-cutting sections or a feature's labeled slice insufficient to ground the corresponding instance) → return to CD for additional design file coverage**; Design System change required → produce DS change request per [RULE] DSG §12 (additive: captured in the originating per-feature UX Design Spec instance §2B.4 at Step 2.3; cross-cutting additives additionally indexed in phase-level §2A.6; breaking: separate change file + review gate); new domain capability needed → schedule as feature-driven domain extension
- **Human intervention**: **Required**

**Per-unit node assignment note**: `assigned_node` is per-unit, not per-phase. A phase may contain multiple units (one Phase 1 walking_skeleton + multiple feature units + zero-or-more app_integration units) executing on different nodes. Each assignment is an independent operator decision per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 1).

**Walking skeleton scope (Phase 1 only)**: The Phase 1 TDD's §3 Walking skeleton scope sub-section captures the thinnest end-to-end vertical slice that proves foundational architecture works before Phase 1 feature units begin. When walking-skeleton scope itself touches Tier 1 (rare), it is included as a labeled slice (frame / section / page tag = `walking-skeleton`) within the phase-level design file produced at Step 2.2; the phase-level UX Design Spec instance at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` is produced as for any tier-1-involved phase (the walking-skeleton appears in the `Per-feature instances in this phase` header list as a feature-slug-equivalent); Step 2.3 additionally produces a per-feature UX Design Spec instance for the walking-skeleton scope authored at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md`, treating it as a feature-slug-equivalent.

**TK-02 Step 2.2 mechanism note (CD input strategy v1)**: The operator transfers the full relevant PRD + TDD sections for all tier-1-involved features in the phase as drop files to a single phase-level CD session, accompanied by an attention prompt that (a) enumerates each tier-1-involved feature with pointers to that feature's UI-relevant content within the drop files, and (b) instructs CD to internally label per-feature design file scope (frame / section / page tag = feature-slug) so Hub Step 2.3 can ground per-feature UX Design Spec instances in each feature's slice. The phase-level (not per-feature) CD session is preferred because CD designs by application phase as its natural unit of visual production; forcing per-feature CD sessions fragments visual cohesion and contradicts CD's by-phase workflow per [REF] Hub-CD-CC Architecture §3.4.1. Full PRD/TDD drop files (not Hub pre-extracted summaries) are preferred because: (a) what's "UI-relevant" depends on CD's design judgment (e.g., a data validation rule may turn out to drive an interaction state that needs visual treatment); (b) Hub pre-extraction risks dropping interaction-relevant content that CD would have picked up. The trade-off is signal-to-noise — but for design-file production, the cost of missing context outweighs the cost of CD processing slightly more input. This is a v1 strategy; if Hub pre-extraction proves more efficient in practice, this mechanism may be revised.

**Cross-model review reminder at sign-off** ([Enforcement·reminder-only]): Same mechanics as TK-01. Hub Claude surfaces a reminder; operator chooses to invoke cross-model review (e.g., Codex review of the TDD architecture) or proceed.

**Hub-to-assigned_node onboarding (between TK-02 and the unit's first node-side TK)**: Immediately after TK-02 sign-off, for each unit in the phase the operator onboards that unit's `assigned_node` per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4). The four Hub-level onboarding contracts (working-branch naming, phase-level spec landing paths, branch publication, Claude Code session start) are stated in full in §5.3 — see §5.3. The CD-authored phase-level design file accompanies as visual reference (transferred to CC at TK-04 entry per [MECH] Cross-Tool Workflow Handoff §3.1, not committed to the monorepo unless the operator explicitly opts to commit at `apps/{app-slug}/design-references/phase-{N}/`). From this point, all subsequent node-side TKs for that unit execute within that Claude Code session.

---

## TK-03: Produce per-slice interface artifacts (Hub-only)

- **Workspace**: Hub Claude
- **Stage**: S1; **Milestone**: Pre-M0 (the M0 entry self-check is folded into the new TK-04 entry at CC, per [MECH] CI/CD Milestone Policy)
- **Repeats**: Once per slice
- **Role sequence**:
  1. HC (deterministic conversion per [TPL] PRD + TDD to Intent and Acceptance Conversion Spec; produces complete `intent.md` / `acceptance.yaml` / `test-plan.yaml` for the target slice, including the UX brief field and accessibility expectations when Tier 1 is involved)
  2. Operator's cross-model review (manual Hub Claude × ChatGPT consensus loop) on the produced artifacts — this serves as the design freeze gate that the pre-refactor architecture allocated to a separate TK-04 M0 adversarial review (which has been retired)
  3. Operator approves the artifacts for transfer to CC
  4. Operator transfers the complete per-slice artifact bundle to the assigned_node working directory per [MECH] Cross-Tool Workflow Handoff §3.1 (places files at `apps/{app-slug}/specs/{intent,acceptance,test-plan}/{slice-id}.{md,yaml,yaml}`)
- **Inputs**:
  - From Hub PK (HC access): `apps/{app-slug}/specs/prd/phase-{N}.md` (paired phase PRD); `apps/{app-slug}/specs/tdd/phase-{N}.md` (phase TDD; specifically the active feature's `§4.{feature-slug}` sub-section); `apps/{app-slug}/specs/test-plan/phase-{N}.md` (phase test plan master, for testing strategy reference); `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` (feature integration test plan, for cross-slice flow context); `apps/{app-slug}/specs/openapi.yaml`; `apps/{app-slug}/specs/slice-list/{feature-slug}.md`
  - **When Tier 1 involved**: both **Hub-authored UX Design Spec instance markdowns** — the **phase-level instance** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` (for cross-feature touchpoint context, shared vocabulary references, VR naming convention) and the **per-feature instance** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` (for in-slice UX content — both produced at TK-02 Step 2.3); the CD-authored phase-level design file (its cross-cutting sections plus the active feature's labeled slice, as visual reference accompanying the UX Design Spec instances in the operator's working materials)
  - Target slice ID; active `feature-slug` and `phase_number`
- **Outputs**:
  - `apps/{app-slug}/specs/intent/{slice-id}.md` — full content including UX brief when Tier 1 involved (UX brief content is a slice-narrow extraction from the Hub-authored UX Design Spec instances per [TPL] Writing Standard §2.3 — per-feature instance for in-slice UX, phase-level instance for cross-feature touchpoints / shared vocabulary the slice participates in)
  - `apps/{app-slug}/specs/acceptance/{slice-id}.yaml` — full content including accessibility_expectations when Tier 1 involved (lifted from the per-feature UX Design Spec instance §2B.5 per [TPL] Writing Standard §3.9)
  - `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` — full content including visual regression cases and a11y test cases when Tier 1 involved
- **Prerequisite**: TK-02 sign-off (which includes Step 2.3 sign-off when any feature has `tier_1_involved=true`; the phase-level UX Design Spec instance exists at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` and the active feature's per-feature UX Design Spec instance exists at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` — both quality check dispositions are `Pass` or `Pass with annotation`)
- **Trigger**: **Manual** (operator picks slice from slice-list)
- **Completion**: Artifacts use their respective [TPL] sources; Tier-1-involving slice has UX brief derived from the Hub-authored UX Design Spec instances (phase-level + per-feature); no undefined boundaries; risk_tier mechanically derived from PRD; operator's cross-model review consensus reached; artifacts transferred to assigned_node working directory
- **Failure routing**: Conversion ambiguity → HC raises question to operator within TK-03; cross-model review surfaces issues → revise in Hub; **UX Design Spec instance gap surfaces (insufficient coverage for slice-level UX brief — either phase-level or per-feature) → escalate to TK-02 Step 2.2 / Step 2.3 (return to CD for design file coverage extension, then re-author the affected UX Design Spec instance)**; DS change required → escalate to TK-02 Step 2.3 (additive change request in originating feature's per-feature instance §2B.4 + phase-level §2A.6 index when cross-cutting + DS change request per [RULE] DSG)
- **Human intervention**: **Required** at the cross-model review step (operator drives the GPT-Claude consensus loop)

**Mechanism rationale (why this TK is Hub-only in the post-refactor architecture)**:
- Per `[REF] Hub-CD-CC Architecture §5.1` content pillar: spec artifact main bodies (PRD / TDD / intent / acceptance / test-plan) are Hub-produced. TK-03 falls under this pillar.
- Both UX Design Spec instance markdowns (phase-level + per-feature) — Hub-authored spec artifacts — were authored upstream at TK-02 Step 2.3 (phase-level instance grounded in the design file's cross-cutting sections; per-feature instance grounded in the corresponding labeled slice). TK-03 extracts slice-narrow content from both instances as applicable; it does not invoke CD again.
- Per the user's cross-model review discipline: the operator's Hub-side ChatGPT-Claude consensus loop is the de facto design freeze gate, replacing the pre-refactor separate TK-04 M0 adversarial review. This loop is only operable in Hub.
- Per `[REF] Hub-CD-CC Architecture §5.2` presentation pillar: when any feature in the phase has Tier 1 involved, a **phase-level design file** is CD-authored at TK-02 Step 2.2 (CD-native visual artifact with cross-cutting sections + per-feature internal labeling), and **UX Design Spec instances at two granularities** are Hub-authored at TK-02 Step 2.3 (one phase-level instance synthesizing the design file's cross-cutting sections + per-feature instances each synthesizing the corresponding labeled slice). TK-03 consumes both Hub-authored UX Design Spec instances as primary textual UX sources; the design file accompanies as visual reference but TK-03 does not parse it as text.
- The cost of round-tripping TK-03 between Hub and CC (the pre-refactor design) is eliminated: artifacts produced in Hub are transferred to CC once, after the cross-model review, with no revert path needed.

**Skill loading note (CC-side, post-TK-03)**: SK-F (`hdc-arco-enterprise-ui`) is in scope from new TK-04 onwards on assigned_node for Tier 1 code generation (when substantive code writing begins per TK-04 description below). SK-F is **not** invoked at TK-03 because TK-03 is Hub-side and Hub cannot load `.claude/skills/`. The Hub-authored UX Design Spec instances (phase-level + per-feature) are the upstream guarantee for DS-coupled content at TK-03 (authored at TK-02 Step 2.3 from the cross-cutting sections and per-feature slices of the CD-authored phase-level design file); SK-F enforces DS-coupled correctness at code time grounded in the CC mirror. SK-W (`hdc-wcag-accessibility-checker`) is on-demand only per [RULE] Design System Governance §6.

**Unit_type applicability**: TK-03 runs for `feature` and `walking_skeleton` units only.

For `walking_skeleton` units (Phase 1 only, exactly one slice), the input substitutions follow [TPL] PRD + TDD to Intent and Acceptance Conversion Specification §0.7 unit_type applicability:
- TDD reading shifts from `§4.{feature-slug}` to `§3.Walking-Skeleton-Header` + `§3.Scope-And-End-To-End-Coverage`
- `feature-{feature-slug}.yaml` and `slice-list/{feature-slug}.md` inputs are **not applicable** (single-slice unit)
- `assigned_node` is sourced from `§3.Walking-Skeleton-Header.assigned_node`
- target `slice-id` is `walking-skeleton` (matching `unit_id`)
- when walking-skeleton scope touches Tier 1: UX Design Spec instance inputs are at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` (phase-level) and `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md` (per-feature equivalent)

For `app_integration` units, TK-03 is skipped entirely (no per-slice interface artifacts; the unit's authoring source is the phase test plan master + feature integration test plans produced at TK-02; entry point is TK-08).

---

## TK-04 through TK-11 — CC-executed task block (constitutional interface)

> **Constitutional scope at Hub residue**: TK-04 through TK-11 are CC-executed tasks. Their detailed execution mechanics (specific subagent invocations, tool commands, sub-steps, internal transitions) are CC substantive content owned by CC substantive DTW canonical. Hub-side residue declares only constitutional identity and Hub-facing interface per task.

## TK-04: M0 entry self-check + spec consumption + code writing

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: Entry point for CC's slice implementation. Absorbs the M0 design-freeze function as a lightweight intake check (spec bundle intact upon CC reception) — not a re-decision of design freeze (per [MECH] CI/CD constitutional residue §2.1).
- **Hub-facing interface — inputs**: Per-slice spec bundle handed off from TK-03 (intent.md, acceptance.yaml, test-plan.yaml + both Hub-authored UX Design Spec instances when Tier 1 — phase-level instance + the active feature's per-feature instance + the phase-level design file as visual reference) per [MECH] Cross-Tool Workflow Handoff §3.1
- **Hub-facing interface — outputs**: First commit on feature branch; GitHub Issue marker block updated to `status: in-progress` per [RULE] WT constitutional residue §4
- **Substantive execution detail**: CC substantive DTW canonical

## TK-05: M1 auto cycle (whitebox testing)

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: M1 Feature Slice gate — slice-level whitebox testing
- **Hub-facing interface — inputs**: Implementation code from TK-04 + acceptance.yaml + test-plan.yaml
- **Hub-facing interface — outputs**: M1 evidence (test results); on failure routes to TK-06 / TK-07
- **Substantive execution detail**: CC substantive DTW canonical

## TK-06: Unit test auto-repair

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: Failure routing target from TK-05; auto-repair attempt before escalating to RCA
- **Hub-facing interface**: Repair attempt count and outcome surface in Test Evidence Report per [MECH] CI/CD constitutional residue §3.2
- **Substantive execution detail**: CC substantive DTW canonical

## TK-07: RCA report

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: Root cause analysis when TK-06 fails to auto-repair; outputs feed Test Evidence Report
- **Hub-facing interface**: RCA report surfaces in Test Evidence Report per [MECH] CI/CD constitutional residue §3.2
- **Substantive execution detail**: CC substantive DTW canonical

## TK-08: M2 core (contract + external integration testing)

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: M2 Integration Green gate core — contract testing (Pact, Tier 2-Tier 3 seam per [RULE] CCAR constitutional residue §6) + external integration validation
- **Hub-facing interface — outputs**: openapi.yaml (per [MECH] CI/CD constitutional residue §4.1 output gate, when last slice of a feature or app_integration unit); Pact pair status surfaces in Test Evidence Report
- **Substantive execution detail**: CC substantive DTW canonical

## TK-09: M2 adversarial loop

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: Adversarial loop following TK-08 to surface edge cases; findings feed Test Evidence Report
- **Hub-facing interface**: Adversarial findings and resolutions surface in Test Evidence Report per [MECH] CI/CD constitutional residue §3.2
- **Substantive execution detail**: CC substantive DTW canonical

## TK-10: M3 cycle (pre-release validation)

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: M3 Pre-Release Validation gate — E2E tests, visual regression, performance, security, compliance audit
- **Hub-facing interface — outputs**: traceability matrix (per [MECH] CI/CD constitutional residue §4.3 output gate); all M3 evidence surfaces in Test Evidence Report
- **Substantive execution detail**: CC substantive DTW canonical (specific E2E framework, visual regression tool, performance test scope, security scan)

## TK-11: M4 preparation (evidence compilation + code review)

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: M4 Merge Decision preparation — compile evidence from all upstream TKs into Test Evidence Report + operator digest one-pager; code review gate executes here
- **Hub-facing interface — outputs**: Test Evidence Report at `apps/{app-slug}/reports/m4/{slice-id}/test-evidence-report.md` per [MECH] CI/CD constitutional residue §3.1; operator digest at `operator-digest.md` per §3.3; code review tool output (historically Codex) included in Test Evidence Report. The specific code review tool is CC substantive.
- **Substantive execution detail**: CC substantive DTW canonical

## TK-12: M4 merge-decision gate (merge decision + smoke test)

- **Workspace**: Hub Claude or assigned_node (operator's choice)
- **Stage**: S4; **Milestone**: M4
- **Role sequence**:
  1. H (reviews Test Evidence Report, Codex review, domain-judge questions, **accessibility audit**)
  2. H (executes smoke test — **includes spot-check on accessibility-flagged screens and manual-validation items from SK-W report**)
  3. H (issues merge go/no-go; PR target = `main`)
  4. **Conditional**: H merges DS change request if any DS update originated from this slice per [RULE] Design System Governance change flow; when merged, CD regenerates the DS markdown export, Hub Claude reviews it against DSG §15, and on a passing review the operator syncs the CC mirror (`specs/design-system.md`) per [RULE] DSG §12.3. The DS-export regeneration (in a CD session) and the §15 export review (in a Hub Claude session) are **separate operator-mediated sessions**, not in-line sub-steps of TK-12 — the operator routes between them; cross-ref [RULE] DSG §12.3
  5. H updates GitHub Issue marker block: `status: merged`
- **Inputs**: Test Evidence Report; Codex review; domain-judge questions; **accessibility audit**
- **Outputs**:
  - Merge decision (target branch = `main`)
  - Smoke test result
  - **Conditional**: DS update merged per [RULE] Design System Governance, with both DS mirrors re-synced from CD-generated DS markdown export
  - Updated GitHub Issue marker block
- **Prerequisite**: TK-11
- **Trigger**: **Manual**
- **Completion**: Merge go → feature branch merged into `main` + DS update applied (if any, with the DS export reviewed against DSG §15 and the CC mirror re-synced) + marker block updated; merge no-go → issues returned
- **Failure routing**: No-go → back to specific TK
- **Human intervention**: **Required**

**Branch model note**: Per CC substantive Workspace Topology canonical (branch topology), feature branches merge directly to `main` in the single-branch topology. Production deployment from `main` is the receiving company's CI/CD scope after handoff per [MECH] Application Lifecycle Handoff §0.2; the AI-dev CI/CD chain terminates at TK-13 staging deploy.

**Scheduling note**: TK-12 may execute per-slice or batched per CC substantive CI/CD Milestone Policy canonical (M4 review scheduling per-slice/batched). Per-slice integrity (one Test Evidence Report, one PR, one go/no-go, one merge action per slice) is preserved in either mode; batching is purely review-session scheduling.

---

## TK-13: Staging deploy

- **Executing workspace**: TOOL (CI/CD automation)
- **Constitutional identity**: Terminal task in the AI-dev CI/CD chain — staging deploy on `main` merge. Production deployment after handoff is the receiving company's CI/CD responsibility per [MECH] Application Lifecycle Handoff §0.2.
- **Hub-facing interface — inputs**: Merged code on `main` (from TK-12)
- **Hub-facing interface — outputs**: Deployed application in staging environment; staging smoke check results
- **Walking-skeleton gate release (constitutional invariant)**: For Phase 1 `walking_skeleton` units, successful TK-13 releases the walking-skeleton-first ordering gate per [RULE] WT constitutional residue §3; downstream `feature` and `app_integration` units in the same Phase 1 may then begin their first node-side milestone.
- **Substantive execution detail**: CC substantive DTW canonical (specific CI/CD automation, staging environment configuration, smoke check scope, dev-loopback supplemental assertions integration)

---

# 5. Transition mechanism catalog

## 5.1 Hub internal transitions

- Within one task: single turn produces multiple artifacts (TK-02 Step 2.1)
- Between hub tasks (TK-01 → TK-02 Step 2.1): **Manual**
- Within TK-02: Step 2.1 → Step 2.2 trigger (conditional on any feature in the phase having `tier_1_involved=true`) → Step 2.3: **Manual** (operator initiates one phase-level CD session covering all tier-1-involved features in the phase when Step 2.1 sets `tier_1_involved` flags; operator returns to Hub session for Step 2.3 — which produces one phase-level UX Design Spec instance plus iterated per-feature instances — after the phase-level design file is produced by CD)
- Between TK-02 (Step 2.3 sign-off) → TK-03: **Manual** (operator picks slice from slice-list)

## 5.2 Hub → CD → Hub (within TK-02 Step 2.2 → Step 2.3)

The TK-02 multi-workspace authoring involves operator-mediated transfers between Hub and CD per [MECH] Cross-Tool Workflow Handoff §2:
- **Hub → CD (Step 2.2 entry)**: operator transfers relevant PRD/TDD sections as drop files to a CD project + attention prompt directing CD to UI-relevant sections per [MECH] Cross-Tool Workflow Handoff §2.1
- **CD → Hub (Step 2.2 exit / Step 2.3 entry)**: operator transfers the CD-authored phase-level design file back to the Hub session per [MECH] Cross-Tool Workflow Handoff §2.2; Hub Claude runs two parallel-able tracks per [TPL] UX Design Spec §3 — (a) phase-level track: design file quality check on cross-cutting sections (§3A.1), then phase-level UX Design Spec instance authoring (§3A.2); (b) per-feature track iterated per tier-1-involved feature: design file quality check on the feature's labeled slice (§3B.1), then per-feature UX Design Spec instance authoring (§3B.2) — all grounded per [RULE] DSG §13.3
- **Quality check `Reject` path**: route back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.3 pauses for the affected track (Step 2.2 redo scope = phase-level cross-cutting sections when the phase-level check rejected; affected feature's slice when a per-feature check rejected; full-phase relabeling when per-feature labeling itself is broken)

This transition happens conditionally — only per feature with `tier_1_involved=true`. Features that are purely Tier 2 / Tier 3 do not trigger Step 2.2 / Step 2.3.

## 5.3 Hub → assigned_node (TK-02 → onboarding → first node-side TK)

The hub-to-assigned_node handoff happens immediately after TK-02 sign-off (covering all three steps when applicable) per [MECH] Cross-Tool Workflow Handoff §3.1. From the first node-side TK onwards through TK-11, all node-side work executes on assigned_node.

- After TK-02 sign-off, operator manually onboards the assigned_node per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4). The Hub-level contracts:
  - A working branch is created from the unit's base branch, following the naming pattern `feature/<app-slug>/<unit-slug>`
  - Phase-level TK-01 PRD and TK-02 outputs (TDD, test-plan, openapi, slice-list, **and both UX Design Spec instance types when authored — the phase-level instance at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` plus per-feature instances at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`**) land at `apps/{app-slug}/specs/{prd,tdd,test-plan,openapi,slice-list,ux-design-spec}/` on the working branch
  - The working branch is published so assigned_node can access it
  - A Claude Code session is started on assigned_node, becoming the execution context for all subsequent node-side TKs for that unit

  The specific SCM commands, branch-publication mechanics, and session-bootstrap procedure are operator-personal mechanism owned by CC substantive Workspace Topology canonical.

Per-slice TK-03 artifacts (intent / acceptance / test-plan) are placed at assigned_node working directory by the operator at the end of each TK-03 iteration per [MECH] Cross-Tool Workflow Handoff §3.1. The CD-authored phase-level design file accompanies the spec bundle as visual reference for the operator and CC, but is not committed to the monorepo unless the operator explicitly opts to commit at `apps/{app-slug}/design-references/phase-{N}/`.

## 5.4 CC internal transitions

CC-internal transitions are **automatic** (not operator-gated). The specific hook wiring that implements each automatic transition — which Claude Code hook fires which transition — is CC-runtime execution mechanics owned by CC substantive DTW canonical; this residue declares only that the transition is automatic.

- TK-04 → TK-05: **automatic**, after code write
- TK-05 → TK-06: **automatic**, on unit test failure
- TK-05 / TK-08 / TK-09 / TK-10 → TK-07: **automatic**, on non-auto-repairable test failure
- TK-08 → TK-09: **automatic**, after TK-08 completion
- TK-09 → TK-10: **automatic**, after TK-09 completion
- TK-10 → TK-11: **automatic**, after TK-10 completion
- TK-11 → TK-12: **automatic only as a notification trigger** — the "Test Evidence Report ready" notification surfaces to the operator. TK-12 runs as a fresh session (it may execute in Hub or on assigned_node); it is not a continuation of the TK-11 execution context. The operator must supply the M4 evidence bundle (Test Evidence Report + operator digest, per [MECH] CI/CD constitutional residue §3) to the TK-12 session as an explicit input — the transition carries the notification, not the evidence.

## 5.5 CC → Hub (TK-11 evidence + Codex review)

After TK-11 completes, the operator may transfer the code review tool output to a Hub Claude conversation for judgment and archive per [MECH] Cross-Tool Workflow Handoff §3.2 (specific code review tool processing rules owned by CC substantive Codex Plugin Usage canonical post-Phase-3 migration).

## 5.6 Hub or assigned_node → CI/CD (TK-12 → TK-13)

After TK-12 merge to `main`, CI/CD auto-fires TK-13 staging deploy. No operator action between TK-12 and TK-13 in the success path.

---

# 6. Human intervention budget

> **Scope note** (per [OS] §0.1.5 Premise 5): The intervention-point structure — which TKs gate on the operator (§6.1 base table, §6.2 conditional list) — is constitutional: a change to where the human gates the cross-workspace workflow requires CC to respond. The numeric counts (§6.1 per-unit-type table) and the §6.3 drift thresholds are operator-facing calibration values — Hub-internal substantive, not CC-substantive runtime config and not a cross-workspace interface; they are deliberately not mirrored to the CC canonical layer. The budget is retained at this Hub residue rather than externalized because §8 and [OS] §12 anti-drift reference §6.1 as the canonical budget referent.

## 6.1 Steady-state (per slice for slice-bearing units; per unit for app_integration)

The intervention budget varies by unit_type because `app_integration` units skip the M0 entry self-check (folded into TK-04 for `feature` and `walking_skeleton` units) and TK-03 entirely per §4.0.3.

**Base table** (applies to `feature` and `walking_skeleton` units, slice-level loop):

| # | Task | Purpose | Workspace |
|---|---|---|---|
| 1 | TK-01 | PRD sign-off (cross-model review reminder fires) | Hub |
| 2 | TK-02 | TDD + openapi + slice-list + assigned_node sign-off across Step 2.1 / Step 2.2 / Step 2.3 (Step 2.2 + Step 2.3 conditional on any feature in the phase having `tier_1_involved=true`; Step 2.2 produces one phase-level design file; Step 2.3 produces one phase-level UX Design Spec instance + iterates per-feature UX Design Spec instances; cross-model review reminder fires at full TK-02 sign-off) | Hub + CD |
| 3 | TK-03 | Per-slice specs review (transition period only; skipped after N=2) | Hub |
| 4 | TK-04 (entry self-check sub-step) | M0 entry self-check verification | assigned_node CC |
| 5 | TK-12 | M4 merge to `main` + smoke test + DS change merge + (conditional) DS markdown export §15 review + CC-mirror sync | Hub or assigned_node |

**Steady-state intervention count by unit_type:**

| Unit type | Total interventions per unit | Incremental interventions per unit (TK-01 / TK-02 amortized) | Notes |
|---|---|---|---|
| `walking_skeleton` (Phase 1 only, 1 slice) | 3 (TK-01, TK-02, TK-12 — M0 self-check folded into TK-04 entry, not a separate intervention) | 1 (TK-12 — M0 self-check is automatic in TK-04 unless inconsistency surfaces) | TK-01 / TK-02 once-per-phase, shared with feature/app_integration units |
| `feature` (1+ slices) | 3 per slice (TK-01, TK-02, TK-12 — M0 self-check folded into TK-04 entry) | First slice: 3; subsequent slices: 1 (TK-12; M0 self-check automatic) | TK-01 / TK-02 once-per-phase, amortize across all slices/features |
| `app_integration` (single PR) | 3 (TK-01, TK-02, TK-12) | 1 (TK-12) | TK-03 and the M0 entry self-check (folded into TK-04 for slice-bearing units) are not applicable to `app_integration`; TK-01 / TK-02 are phase-level inputs |

TK-03 sampling review counts toward the operator's intervention only during the transition period (first N=2 slices per unit). Cross-model review (if invoked at TK-01 / TK-02 sign-off) is additional operator effort but not a separate intervention point — it is operator's choice within the TK-01 / TK-02 sign-off window.

Workspace inception is a one-time human-driven activity owned outside this source.

## 6.2 Conditional

| # | Task | Condition |
|---|---|---|
| 1 | TK-04 | CC escalates (including Design System drift, including Hub/CC mirror version mismatch) |
| 2 | TK-07 | Any RCA requiring operator decision |
| 3 | TK-08 | Severe compliance violation |
| 4 | TK-09 | High-severity adversarial finding |
| 5 | TK-10 | Severe visual regression, accessibility critical/serious, or security finding |
| 6 | TK-13 | Staging deploy failure |
| 7 | TK-01 | Cross-model review invoked at operator's discretion |
| 8 | TK-02 | Cross-model review invoked at operator's discretion |
| 9 | TK-02 Step 2.3 | Design file quality check `Reject` disposition — phase-level check on cross-cutting sections, or per-feature check on a labeled slice — → return to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.2 redo scope is the affected cross-cutting sections (phase-level reject) or the affected feature's slice (per-feature reject), or full-phase relabeling when per-feature labeling itself is broken |

## 6.3 Anti-drift on intervention budget

If steady-state interventions exceed the §6.1 per-unit-type budget for 2+ consecutive units of the same type, investigate the causes below. The threshold granularity differs by unit type — `feature` is measured per slice, while `walking_skeleton` and `app_integration` are measured per unit (each is a single-PR unit):

- `feature` units: **> 5 interventions per slice**
- `walking_skeleton` unit: **> 5 interventions total for the unit**
- `app_integration` unit: **> 4 interventions total for the unit**

These drift-investigation triggers are deliberately set above the §6.1 design target (3 interventions per slice / per unit): the gap is an intentional tolerance band, so that occasional one-off escalations do not trip a drift investigation and only a sustained excess does.
- Hook chain silent failure
- A3 severity miscalibration
- Auto-repair loops exhausting
- Compliance-checker first-pass violations frequent
- **Design System Governance drift recurrent**
- **Cross-app domain contract churn**
- **Phase-level or per-feature design file quality check failures recurrent at TK-02 Step 2.3** (operator returning CD design file cross-cutting sections or per-feature slices for redo too often suggests upstream framing issues — possibly insufficient PRD/TDD drop-file context at Step 2.2 entry, or DS mirror not adequately consulted by CD, or per-feature labeling instruction insufficiently emphasized in the attention prompt)
- **UX Design Spec instance authoring stalls recurrent at TK-02 Step 2.3** (Hub Claude finding design file cross-cutting sections insufficient to ground phase-level instance, or design file slices insufficient to ground per-feature instances, too often suggests Step 2.2 input strategy needs revision)

---

# 7. Failure routing matrix

| Failure source | Routing target | Mechanism |
|---|---|---|
| Static analysis critical (TK-04) | TK-04 | automatic (CC-internal) |
| **Tier 1 Design System drift (TK-04)** | **TK-04** | **automatic (CC-internal)** |
| **TK-04 M0 self-check finds the CC DS mirror stale** | **Operator triggers a DS markdown export resync (DSG §15 review + CC-mirror sync) per [RULE] DSG §12.3** | **Manual** |
| **TK-02 Step 2.3 design file quality check `Reject` disposition (phase-level or per-feature)** | **Return to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.2 redo scope is the phase-level cross-cutting sections (phase-level reject), the affected feature's slice (per-feature reject), or full-phase relabeling when per-feature labeling itself is broken** | **Operator manual** |
| **TK-02 Step 2.3 UX Design Spec authoring gap (cross-cutting sections insufficient for phase-level instance, or a feature's design file slice insufficient for per-feature instance)** | **Return to CD for additional design file coverage on the affected scope; Step 2.2 → Step 2.3 redo for the affected track** | **Operator manual** |
| **TK-02 / TK-03 DS change required** | **Captured in originating per-feature UX Design Spec instance §2B.4 New-Components-Or-Tokens at Step 2.3 (additive); cross-cutting additives additionally indexed in phase-level instance §2A.6; separate change file at Step 2.3 + review gate (breaking); per [RULE] DSG §12** | **Manual** |
| Unit test failure (TK-05) | TK-06 (≤3) | automatic (CC-internal) |
| Unit test failure after 3 (TK-06) | TK-07 | automatic (CC-internal) |
| Internal-integration failure (TK-05) | TK-07 | automatic (CC-internal) |
| Contract / external-integration failure, including producer-side contract verification (TK-08) | TK-07 | automatic (CC-internal) |
| Adversarial-loop test failure (TK-09) | TK-07 | automatic (CC-internal) |
| E2E / visual / performance failure (TK-10) | TK-07 | automatic (CC-internal) |
| **Accessibility baseline critical or serious (TK-10)** | **TK-07 + Notification** | **automatic (CC-internal)** |
| Security critical (TK-10) | Notification | automatic notification (CC-internal) |
| Compliance severe (TK-08, TK-11) | Notification | automatic notification (CC-internal) |
| **Design System Governance compliance final violation (TK-11)** | **Notification** | **automatic notification (CC-internal)** |
| **App/domain placement violation (TK-08, TK-11)** | **Notification** | **automatic notification (CC-internal)** |
| RCA: revise specs | TK-03 (or upstream, including TK-02 Step 2.3 when phase-level or per-feature UX Design Spec instance needs revision) | Manual |
| RCA: revise code | TK-04 | Manual |
| **RCA: revise DS** | **DS change request per [RULE] Design System Governance §12** | **Manual** |
| **RCA: revise domain contract** | **TK-02 (consumer side) or domain-internal change request** | **Manual** |
| RCA: accept limitation | Proceed with waiver | Manual |
| M4 no-go (TK-12) | Back to specific TK | Manual |
| **TK-12 DS markdown export sync failure (CC mirror not updated, or committed without the §15 review)** | **Operator completes the DSG §15 review and CC-mirror sync per [RULE] DSG §12.3** | **Manual** |
| Staging deploy failure (TK-13) | Auto rollback + Notification + TK-12 | CI/CD |

---

# 8. Anti-drift red flags

> **Scope**: this section enumerates **DTW-specific** anti-drift red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced rather than duplicated. See [OS] §12.3 for the full anti-drift red flag ownership map.

**Task-level** (DTW-specific):
- A task silently skipped
- Hook chain reports completion but downstream task no trigger
- TK-01, TK-02, or TK-04 entry self-check proceeding without operator sign-off (the operator's sign-off on TK-02 + the operator-driven Hub-side cross-model review at TK-03 sign-off are the design freeze gates; TK-04 entry self-check is a structural check executed by CC that nevertheless requires operator awareness when it surfaces inconsistency)
- **TK-02 Step 2.1 sign-off proceeding without setting `tier_1_involved` flags per feature** — the flag drives whether Step 2.2 / Step 2.3 fire; missing flags cause Tier 1 features to skip CD-side phase-level design file inclusion silently
- **TK-02 Step 2.2 fired but Step 2.3 skipped** — Step 2.2 produces the CD-native phase-level design file; without Step 2.3 the per-feature markdown UX Design Spec instances are missing and downstream Hub TK-03 / CC TK-04+ have no AI-RAG-consumable UX spec
- **TK-02 Step 2.3 UX Design Spec instance authored without grounding in the per-feature slice of the CD-authored phase-level design file** — violates [RULE] DSG §13.3 Hub-side consumption discipline; results in UX Design Spec instances referencing nonexistent or misnamed DS elements
- **TK-02 Step 2.2 produced a phase-level design file without per-feature internal labeling** — Hub Step 2.3 cannot ground per-feature UX Design Spec instances without the labels; route through CD for labeling before Step 2.3 proceeds
- TK-03 transition period skipped prematurely (before N=2 slices)
- Reintroduction of TK-15+ (release authorization, production deploy) into the AI-dev TK sequence without canonical revision authorizing it
- **Cross-model review reminder at TK-01 / TK-02 promoted from advisory to hard gate without canonical revision** (the reminder is [Enforcement·reminder-only]; reframing it as a required task constitutes scope expansion requiring revision of this source)

**Workspace dimension** (DTW-specific):
- TK-04 onwards executed in Hub Claude instead of assigned_node Claude Code (breaks evidence chain locality and SK-F coverage; TK-04+ is mechanically impossible in hub anyway — Hub cannot load `.claude/skills/`)
- TK-01, TK-02 Step 2.1, TK-02 Step 2.3, or TK-03 executed in assigned_node CC instead of hub (loses hub's content-pillar discipline per [REF] Hub-CD-CC Architecture §5.1)
- **TK-02 Step 2.2 executed in Hub instead of CD when any feature in the phase has `tier_1_involved=true`** (loses presentation-pillar discipline; Hub cannot produce CD-native visual design files)
- **TK-02 Step 2.2 executed as one CD session per feature instead of one CD session per phase** — the canonical CD delivery unit is phase-level (covering all tier-1-involved features in the phase as labeled internal scopes); per-feature CD sessions fragment visual cohesion and contradict CD's by-phase design workflow
- **TK-02 Step 2.3 executed in CD instead of Hub** (loses content-pillar discipline; CD does not author markdown specs — UX Design Spec instance authoring belongs in Hub per the revised architecture)
- Hub-to-assigned_node onboarding skipped or partial
- **Operator hand-authoring UX content in Hub at TK-02 Step 2.3 without the CD-authored phase-level design file** — Step 2.3 grounds each per-feature UX Design Spec instance in the relevant slice of the CD-authored phase-level design file; authoring without it invalidates the instance's grounding chain
- **Operator skipping CD design file entirely at TK-02 Step 2.2 when any feature in the phase has `tier_1_involved=true`, going directly to Hub UX Design Spec instance authoring** — Hub Claude has no visual reasoning capability; UX Design Spec instances authored without design file grounding produce content disconnected from actual visual design (the operator may sometimes choose to bypass CD for trivial UX content with clearly named patterns, but recurring bypass on non-trivial UX is a drift signal)

**App / domain dimension**: see [RULE] Claude Code Architecture Rules §8 for the canonical red-flag list. DTW-specific augmentations:
- Feature work using `{feature-slug}` not preceded by `{app-slug}` in TDD reference path (TK-02 / TK-03 surface)
- New domain capability introduced without phase TDD `§4.{feature-slug}.Module-Decomposition` referencing it

**Multi-node deployment**: see [RULE] Workspace Topology constitutional residue §6 (anti-drift signals) for the canonical red-flag list. DTW local variants:
- TDD missing `assigned_node` field at TK-02 Step 2.1 sign-off
- Cross-node Codex invocation at TK-11 (canonical anti-pattern owned by [RULE] Workspace Topology constitutional residue §6 (cross-workspace anti-drift))
- GitHub Issue marker block missing or malformed at TK-04 entry (the marker block authoring step inside TK-04 sub-task 2)

**Bias firewall**: see [RULE] Claude Code Architecture Rules §8 for the canonical red-flag list. DTW local variant:
- test-plan.yaml modified by any subagent other than TK-09's patch flow
- Adversarial-tester severity miscalibration

**Branch / GitHub workflow**: see [RULE] Workspace Topology constitutional residue §6 (anti-drift signals). DTW local variant:
- TK-12 merge target other than `main`
- TK-12 merge via admin bypass on Free plan or PR review skipped entirely

**Contract testing**: see [RULE] Claude Code Architecture Rules §8.

**Evidence integrity** (DTW-specific):
- Evidence-compiler produces Test Evidence Report without domain-judge-questions.md
- Steady-state intervention count exceeding the per-unit-type budget per §6.1 for 2+ consecutive units of the same type
- Evidence files from one slice cross-contaminating another slice's `evidence/{slice-id}/` directory

**Cross-tool handoff dimension** (DTW local variants of [MECH] Cross-Tool Workflow Handoff §8 red flags):
- **TK-02 Step 2.2 CD phase-level design file transferred to Hub Step 2.3 without operator audit** (per [MECH] Cross-Tool Workflow Handoff §2.2 audit checklist — including the per-feature internal labeling completeness check across all tier-1-involved features in the phase)
- **TK-02 Step 2.3 UX Design Spec instance transferred to assigned_node working directory without operator audit** (UX Design Spec instance is a Hub-authored markdown spec; standard operator-mediated transfer discipline applies)
- TK-11 Codex review output bypasses Hub judgment (per [MECH] Cross-Tool Workflow Handoff §3.2.3)
- **TK-12 DS markdown export §15 review or CC-mirror sync skipped when slice carries DS change** (violates [RULE] DSG §12.3; leaves the CC mirror stale or unreviewed)

**UX and accessibility**: most red flags here are owned by CC substantive Code Quality Rule Set canonical (UX/accessibility lint rules) and [RULE] Design System Governance §16 governance. DTW local variants:
- **SK-F (`hdc-arco-enterprise-ui`) not invoked during TK-04 Tier 1 code generation** (the TK-04 instance of skill-loading drift)
- **Tier-1-involving feature's UX Design Spec instance missing at TK-02 Step 2.3 sign-off** (when the CD-side phase-level design file was produced and contains that feature's slice but Hub-side UX Design Spec authoring for the feature was skipped)
- **Tier-1-involving slice's intent.md missing UX brief section** (TK-03 surface — when feature's UX Design Spec instance is missing or insufficient)
- **Tier-1-involving slice's test-plan.yaml missing `test_type: accessibility` cases when slice has specific a11y concerns** (TK-03 surface)
- **i18n resource files missing for supported locales when Tier 1 adds user-facing text** (TK-04 surface)

---

# 9. Hub Claude soft compliance — TK-gate trigger phrases

Per [RULE] Workspace Topology constitutional residue §7 (Hub Claude trigger phrases) authoring pattern, this section embeds Hub Claude soft compliance trigger phrases scoped to TK-gate phrasing and workspace-shift phrasing. Node-related phrasing is owned by [RULE] Workspace Topology constitutional residue §7; cross-tool handoff phrasing is owned by [MECH] Cross-Tool Workflow Handoff §7; application-level handoff phrasing is owned by [MECH] Application Lifecycle Handoff §6.

When user phrasing in a Hub Claude conversation matches any of the following, Hub Claude SHOULD remind the operator of the relevant section of this source before proceeding. Hub Claude MUST NOT auto-execute the action; surface as confirmation prompt only.

**TK-gate skip phrasing** → reference §4 (relevant TK):
- "skip the M0 review" / "skip the M0 entry self-check" (M0 entry self-check is folded into TK-04; skipping it is skipping TK-04 entry)
- "go straight to TK-11"
- "can I skip TK-06"
- "skip the auto-repair"
- "merge before TK-10 finishes"
- "fast-track this slice"
- "skip the Codex review"
- **"skip Step 2.2 even though some features in this phase touch Tier 1"** / **"skip the CD design file for these Tier 1 features"** (Step 2.2 is required per [REF] Hub-CD-CC Architecture §5.2 revised; skipping is a presentation-pillar bypass)
- **"open one CD session per feature for the phase's Tier 1 features"** / **"split the phase into per-feature CD sessions"** (the canonical CD delivery unit is phase-level — one CD session per phase covering all tier-1-involved features as labeled internal scopes; per-feature CD sessions contradict CD's by-phase design workflow per [REF] Hub-CD-CC Architecture §3.4.1)
- **"skip Step 2.3, just go to TK-03 directly with the CD design file"** / **"don't author the per-feature UX Design Spec instances, TK-03 can read the design file directly"** (TK-03 consumes the Hub-authored per-feature UX Design Spec instance as the primary textual UX source; the design file alone does not satisfy AI-RAG consumption requirements)

**Workspace-shift phrasing** → reference §0.4 and §4 TK-02 Step 2.2 / Step 2.3 / TK-03 / TK-04:
- **"let me author the UX Design Spec instance in CD"** / **"have CD produce the markdown spec"** — Step 2.3 belongs in Hub per the revised architecture; CD outputs the phase-level design file, not markdown specs
- **"have Hub produce the design file / mockups"** — Step 2.2 belongs in CD; Hub Claude cannot produce CD-native visual artifacts
- "let me draft the intent in this hub chat without consulting the UX Design Spec instance" (when slice involves Tier 1 — reference TK-03 inputs)
- "let me write the test-plan UX-touching fields here in hub" (these fields are derived from the Hub-authored UX Design Spec instance, not invented in TK-03)
- "do the M0 entry self-check in hub Claude" (M0 entry self-check is a CC-side structural verification per TK-04; it cannot run at Hub because the CC mirror SK-F engagement is part of the check)
- "skip onboarding, just generate intent.md here"
- "let me write the M0 marker block manually instead of using `gh issue edit`"

**Sign-off bypass phrasing** → reference §6.1 (steady-state intervention budget):
- "auto-approve TK-02"
- **"auto-approve TK-02 Step 2.3 per-feature design file quality check"** (Step 2.3 quality check requires operator awareness per tier-1-involved feature; the `Pass` / `Pass with annotation` / `Reject` disposition per feature is recorded in the conversation log)
- "let CC sign off TK-04 entry self-check unilaterally without surfacing inconsistency" (CC executes the self-check mechanically; when inconsistency is found, operator awareness is required)
- "skip the M4 manual review"
- "skip the cross-model review reminder" (the reminder is [Enforcement·reminder-only]; skipping is allowed but the operator should acknowledge skipping consciously)

**Cross-model review phrasing** → reference §4 TK-01 / TK-02 (reminder mechanics):
- "always run Codex review on every PRD" (this would promote the reminder to mandatory — surface that the reminder is advisory and ask the operator to confirm if they want canonical revision to make it mandatory)
- "skip the cross-model review for this PRD" (this is allowed — surface the reminder once, then proceed if the operator confirms)

**DS mirror sync phrasing** → reference §4 TK-12 + [RULE] DSG §12.5:
- **"commit the DS export to the CC mirror, skip the §15 review"** / **"the DS export review can wait"** (violates [RULE] DSG §12.3; the DS markdown export MUST pass the §15 conformance review before the CC mirror is committed)
- **"hand-edit `specs/design-system.md` for this slice"** (the CC DS mirror is read-only; direct edits violate [RULE] DSG §12.6)

**AI-dev / company-side boundary phrasing** → reference §4 TK-12 / TK-13 and [MECH] Application Lifecycle Handoff §0.2:
- "deploy this to prod from here" / "push to production"
- "tag a release in this monorepo" / "cut a release tag"
- "set up M5-prod" / "add a TK-15 / TK-16 step"
- "reintroduce hdc/feature-development" / "add an integration branch between feature and main"

Hub Claude reminders are conversational. The operator may override with explicit acknowledgment, but the override itself must be stated in the conversation, preserving traceability for later retrospective review.
