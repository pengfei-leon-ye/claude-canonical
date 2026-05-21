# [MECH] Development Track Workflow

- **Project**: HR Digital Cockpit
- **Document Type**: Workflow Orchestration Specification
- **Status**: Active canonical
- **Role**: Constitutional declaration of the end-to-end task sequence (TK-01 through TK-13) and the cross-workspace orchestration contract. Hub-side ownership: full substantive content for Hub-authored tasks (TK-01 / TK-02 with sub-steps / TK-03 / TK-12 operator gate), the unit_type catalog as cross-workspace interface, the per-task workspace mapping, the milestone-to-task mapping, the transition mechanism catalog, the human intervention budget, the failure routing matrix, cross-workspace anti-drift signals, and Hub Claude soft compliance trigger phrases (Hub-internal substantive). CC-executed tasks (TK-04 through TK-11 and TK-13) are declared at constitutional identity + Hub-facing interface level only; their detailed step-by-step execution mechanics live at CC substantive DTW canonical.
- **Source Category**: Cat 4
- **Management-System Role**: Workflow orchestration specification; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Detailed task-level expansion of the Development Track routing defined in [OS] §7.1. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side residue carries the constitutional skeleton + Hub-authored substantive content; CC-side substantive canonical owns the CC-executed task mechanics.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design), §10 MECE, §12 make important work executable.
- **Relationship to [REF] Hub-CD-CC Architecture**: TK sequence operates across the three workspaces (Hub / CD / CC). Hub-side TKs (TK-01, TK-02 sub-steps, TK-03) author content per the content pillar; CD-side participation embedded inside TK-02 Step 2.2 produces per-feature design files when `tier_1_involved=true`; CC-side TKs (TK-04 onwards) consume content for implementation per the implementation pillar.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: Three-path handoffs at the relevant TK transitions:
  - TK-01 → TK-02 hub-side: PRD consumed in hub for TDD authoring
  - TK-02 Step 2.1 → Step 2.2 (Hub → CD): Hub PRD/TDD relevant sections transferred to CD per [MECH] Cross-Tool Workflow Handoff §2.1
  - TK-02 Step 2.2 → Step 2.3 (CD → Hub): CD-produced design files transferred to Hub per §2.2 for Hub-side design-file quality check + UX Design Spec instance authoring
  - TK-03 → TK-04 (Hub → CC): completed per-slice spec artifacts + per-feature UX Design Spec instance + CD-authored design files transferred to assigned_node working directory per §3.1
  - TK-11 code review output → Hub: per §3.2 (the specific code review tool — historically Codex — is governed by CC substantive canonical)
  - DS markdown export sync at TK-12 M4 merge (when DS instance changed): CD → Hub mirror + CC mirror, in lock-step per [RULE] Design System Governance §12.5 / §12.7
- **Relationship to [RULE] Workspace Topology**: Companion. DTW imports WT constitutional residue's unit_type catalog and node-assignment interface contract; hub-to-assigned_node onboarding (after TK-02) implements WT's node assignment workflow.
- **Relationship to [RULE] Claude Code Architecture Rules**: Imports CCAR constitutional residue's tier identity; CC substantive CCAR owns the subagent roster, context scopes, paths, and skill loading rules consumed by TK-04+.
- **Relationship to [MECH] CI/CD Milestone Policy**: Imports M0–M5 gate identity from CI/CD constitutional residue; task-to-milestone mapping reflected in §0.3 with TK-13 as the terminal CI/CD task.
- **Relationship to [MECH] Application Lifecycle Handoff**: TK-12 merges feature branches directly to `main`. Application-level handoff to a human dev team is a distinct lifecycle event after one or more apps reach maturity per [MECH] Application Lifecycle Handoff §2; the AI-dev CI/CD chain terminates at TK-13 staging deploy.
- **Relationship to [RULE] Design System Governance**: TK-02 Step 2.3 implements DSG §13.3 Hub-side consumption discipline (design file quality check + UX Design Spec instance authoring grounded in Hub DS mirror at `hdc_ref_design-system.md`). DSG §12 additive change requests are surfaced at TK-02 Step 2.3 when authoring the UX Design Spec instance reveals a gap in the current DS.
- **Relationship to [TPL] sources**: References TDD template, Intent-Acceptance Writing Standard, PRD+TDD Conversion Spec, Test Plan YAML Schema, UX Design Spec, and Design System Governance as artifact contracts.
- **Pairings I participate in**: P-03 (with [MECH] CI/CD constitutional residue §2 — milestone-to-TK anchoring), P-09 (with [MECH] CI/CD constitutional residue §2.7 — per-unit-type milestone profile), P-10 (with [RULE] WT constitutional residue §4 — node-assignment marker schema), P-31 (with [TPL] PRD §0.7 + [TPL] TDD §0.7), P-38 (with CC substantive Dev-Loopback canonical — constitutional pairing reduced to handoff-interface level). Pre-split pairings P-32 / P-49 retired at this Hub residue level; substantive obligations migrate to CC.

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
- **TK-02 internal step structure** (Step 2.1 Hub-side TDD/test-plan/openapi/slice-list authoring → Step 2.2 CD-side design file production, conditional on `tier_1_involved=true` → Step 2.3 Hub-side design file quality check + UX Design Spec instance authoring)
- Role sequence per task, including which workspace (Hub Claude, Claude Design, assigned_node Claude Code) executes each task or sub-step
- File-level inputs and outputs, anchored to the repository layout in CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1)
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
- Subagent roster and permission model (CC substantive Claude Code Architecture Rules canonical (subagent roster §5), §X)
- Repository layout structure (CC substantive Claude Code Architecture Rules canonical, repository layout §Y)
- Milestone gate semantics and per-unit-type milestone profile ([MECH] CI/CD Milestone Policy §2)
- Code review tool command semantics, co-location mechanism, and per-unit-type fire conditions (owned by CC substantive Codex Plugin Usage canonical; Codex fully migrated to CC in Phase 3)
- Multi-node infrastructure, node identity, scheduling parity, parallel execution model, walking-skeleton-first ordering rule, walking-skeleton output canonical set, node assignment mechanics, GitHub Issue marker block format ([RULE] Workspace Topology §2, §4, §6)
- Design System governance, three-way DS distribution, mirror sync mechanism ([RULE] Design System Governance, [REF] Hub-CD-CC Architecture §5.2)
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
| TK-02 Step 2.2 (conditional on any feature `tier_1_involved=true`) | Claude Design (per feature with `tier_1_involved=true`) | Per-feature CD-authored design files: hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations (CD-native; not markdown). Inputs: PRD relevant sections + TDD relevant sections + Hub DS mirror reference per `[REF] Hub-CD-CC Architecture §3.4.1` |
| TK-02 Step 2.3 (when Step 2.2 fired) | Hub Claude (HC + H collaboration) | Design file quality check (per `[TPL] UX Design Spec` §3 reviewer checklist, grounded in Hub DS mirror at `hdc_ref_design-system.md` per `[RULE] DSG §13.3`) → UX Design Spec instance authoring (Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` from design files + Hub DS mirror grounding) |
| TK-03 | Hub Claude (HC + H collaboration) | Per-slice intent + acceptance + test-plan authoring (main body + UX brief when Tier 1); consumes PRD + TDD + Hub-authored UX Design Spec instance (from TK-02 Step 2.3) + design files (as visual reference); the operator's GPT-Claude consensus loop at TK-03 sign-off serves as the de facto design freeze for the slice |
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
    - **Step 2.2** — CD-side per-feature design file production (runs per feature with `tier_1_involved=true`; skipped entirely when no features in the phase touch Tier 1). CD produces design files per [REF] Hub-CD-CC Architecture §3.4.1; the Hub session at TK-02 hands CD the PRD + TDD relevant sections as drop files with a Hub-attention prompt directing CD to UI-relevant sections
    - **Step 2.3** — Hub-side design file quality check + UX Design Spec instance authoring (runs when Step 2.2 fired; one UX Design Spec instance authored per feature with `tier_1_involved=true`). Hub Claude verifies the CD-authored design files against the Hub DS mirror at `hdc_ref_design-system.md` per [RULE] DSG §13.3, then authors the per-feature UX Design Spec instance as markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` per [TPL] UX Design Spec
  - **TK-03** — hub-side: per-slice intent + acceptance + test-plan (main body + UX brief when Tier 1 involved, drawing from the Hub-authored UX Design Spec instance from TK-02 Step 2.3 and design files as visual reference). Runs for `feature` and `walking_skeleton` units only; not for `app_integration`. The operator's GPT-Claude consensus loop at TK-03 sign-off serves as the de facto design freeze gate.
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

## 2.2 Subagent roster (defined in CC substantive Claude Code Architecture Rules canonical (subagent roster §5.1))

Codes **A1 through A10** reference the 10 subagents of the Development Track (one conditionally enabled). Their names, purposes, primary invocation tasks, and context scopes are owned by CC substantive Claude Code Architecture Rules canonical (subagent roster §5.1) as the single source of truth.

When task definitions in §4 mention these codes with a parenthetical role name (e.g., "A5 (unit-test-auto-repair)"), the parenthetical is a reading convenience; Architecture Rules §5.1 remains authoritative for any discrepancy.

The subagent roster is a single shared definition at `HDC_ROOT/.claude/agents/`, deployed identically across all dev nodes per [RULE] Workspace Topology constitutional residue §2 (parity discipline). Each node runs single subagent instances; same-node multi-slice parallelism uses git worktree isolation per CC substantive Workspace Topology canonical (same-node multi-slice parallelism).

## 2.3 External tool and skill roles (defined in their own canonical sources)

| Code | Role | Owner source |
|---|---|---|
| CX | Code review tool (historically Codex plugin) | CC substantive Codex Plugin Usage canonical (post-Phase-3 migration) |
| SK-F | `hdc-arco-enterprise-ui` skill | `.claude/skills/hdc-arco-enterprise-ui/SKILL.md` |
| SK-W | `hdc-wcag-accessibility-checker` skill | `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md` |

---

# 3. Path and placeholder catalog

## 3.1 Path catalog (delegated)

The full repository layout — `HDC_ROOT/`, `apps/{app-slug}/`, `packages/domain/{domain-name}/`, `.claude/` — is owned by CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1). Task definitions in §4 reference paths under that layout without restating it here.

## 3.2 Spec-artifact path summary (for task definition reference)

| Artifact | Path |
|---|---|
| Phase PRD | `apps/{app-slug}/specs/prd/phase-{N}.md` |
| Phase TDD | `apps/{app-slug}/specs/tdd/phase-{N}.md` |
| Phase test plan (master, markdown) | `apps/{app-slug}/specs/test-plan/phase-{N}.md` |
| Feature integration test plan (yaml) | `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` |
| Per-feature slice-list | `apps/{app-slug}/specs/slice-list/{feature-slug}.md` |
| App-scoped OpenAPI | `apps/{app-slug}/specs/openapi.yaml` |
| **Per-feature UX Design Spec instance** (Hub-authored markdown when `tier_1_involved=true`) | `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` |
| Per-slice intent | `apps/{app-slug}/specs/intent/{slice-id}.md` |
| Per-slice acceptance | `apps/{app-slug}/specs/acceptance/{slice-id}.yaml` |
| Per-slice test plan | `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` |
| CC mirror of DS instance (code-time mirror) | `specs/design-system.md` (monorepo root) |
| Hub mirror of DS instance (spec-time mirror) | `hdc_ref_design-system.md` (Hub PK) |
| Per-slice evidence | `apps/{app-slug}/evidence/{slice-id}/**` |
| Per-slice M4 reports | `apps/{app-slug}/reports/m4/{slice-id}/**` |

## 3.3 Placeholder definitions

| Placeholder | Definition | Uniqueness scope |
|---|---|---|
| `{app-slug}` | Kebab-case app identifier, `[a-z0-9-]`, ≤50 chars, English, frozen on first declaration | Globally unique within `HDC_ROOT/apps/` |
| `{N}` | Phase number, positive integer, monotonic per app (Phase 1 = 0→1; Phase N≥2 = additive iteration) | App-internal sequence; one phase number per app per phase |
| `{domain-name}` | Kebab-case domain identifier, `[a-z0-9-]`, descriptive of business capability, frozen | Globally unique within `HDC_ROOT/packages/domain/` |
| `{feature-slug}` | Kebab-case feature identifier, `[a-z0-9-]`, ≤40 chars, English, frozen; a feature is introduced or evolved within a phase | App-internal uniqueness only; global feature identity = `{app-slug}/{feature-slug}` |
| `{slice-id}` | `{feature-slug}-{slice-seq}-{slice-name}` | Feature-internal; global slice identity = `{app-slug}/{feature-slug}/{slice-id}` |
| `{module}` | Module name within a tier | Tier-internal |
| `{flow}` / `{screen}` / `{scenario}` | E2E flow, visual/accessibility target screen, performance scenario | Test-suite-internal |
| `{app-slug}-bff_{domain-name}` | Pact contract test pair name (consumer-driven; per CC substantive Claude Code Architecture Rules canonical §Y (app-slug roster).4) | Globally unique within HDC_ROOT |
| `{skill-name}` | Custom skill kebab-case identifier | `.claude/skills/`-internal |
| `{locale}` | BCP 47 locale (e.g., `en`, `zh-CN`, `ja`) | App-internal |
| `{change-id}` | DS change identifier | DS governance-specific path per [RULE] Design System Governance |

## 3.4 Glossary

**app**: An application container under `apps/{app-slug}/`. Each app has its own frontend (Tier 1), BFF (Tier 2), specs, tests, evidence, and reports. App identity is decoupled from feature identity; one app contains many features over its lifetime. An app's lifetime is partitioned into phases; phase identity sits between app and feature.

**phase**: The top-level granularity of an app's lifecycle. Phase 1 (`{N}=1`) takes the app from 0 to 1 — establishing foundational architecture, cross-feature baselines, walking skeleton scope, and the initial feature set. Phase N≥2 is an additive iteration that adds or evolves features under the established baselines without re-establishing them. One phase produces one paired phase PRD + phase TDD + phase test plan (master) + per-feature integration test plans + per-feature slice-lists + (per feature with `tier_1_involved=true`) per-feature UX Design Spec instances. Phase identity is per-app, not project-wide; different apps may be at different phase numbers.

**domain**: A Tier 3 capability package under `packages/domain/{domain-name}/`. Domain identity is decoupled from app identity; one domain may serve one or more apps. Domain lifecycle is independent of any single feature's roadmap (Phase A Model B; per CC substantive Claude Code Architecture Rules canonical §Y (app-slug roster).4).

**feature-slug**: short stable machine-friendly identifier for a feature (kebab-case, English, frozen once created). App-internal uniqueness only.

**work unit (or simply unit)**: Node-level assignment granularity. Within a phase, work is partitioned into one or more work units; each unit is assigned to a single node per [RULE] Workspace Topology §6 and runs to completion on that node. Three unit types exist: `walking_skeleton` (Phase 1 only, exactly one per Phase 1, exactly one slice), `feature` (one per feature in the phase, one or more slices), and `app_integration` (zero or more per phase, zero customer-facing slices).

**unit_id**: Kebab-case stable identifier unique within the app's phase. Recommended naming: `walking-skeleton` for the Phase 1 walking_skeleton unit; the `feature-slug` for `feature` units; `app-int-phase-{N}` for `app_integration` units.

**slice**: smallest unit of work that completes the M0 → M5 evidence chain on a single dev node. A `feature` unit decomposes into one or more slices at TK-02; a `walking_skeleton` unit consists of exactly one slice (the thinnest end-to-end vertical slice that proves foundational architecture); an `app_integration` unit has zero customer-facing slices (its single PR runs the M2–M5 subset directly).

**slice-id**: slice-level identifier extending feature-slug, e.g., `manager-e-signature-01-initiation`.

**assigned_node**: the logical node (per [RULE] Workspace Topology constitutional residue §1.2 (logical naming convention)) that executes the unit's first node-side TK and all subsequent TKs. Decided at TK-02 as a first-class output for each unit in the phase.

**cross-model review reminder**: An [Enforcement·reminder-only] advisory surfaced at TK-01 and TK-02 sign-off suggesting the operator consider obtaining a review of the produced spec from a model other than the one that produced it (e.g., Codex, a different Claude variant). The reminder is conversational; the operator may invoke a cross-model review or proceed without one. See §4 TK-01 / TK-02 task definitions.

**brownfield reconstruct memo**: A TK-01 conditional pre-step output produced when an app has existing behavior worth preserving. The memo extracts existing PRD content, TDD content, and observed code behavior into a structured reference for the new phase PRD's authoring. See §4 TK-01 task definition.

**design files** (CD-authored): Per-feature visual artifacts produced by CD in TK-02 Step 2.2 when `tier_1_involved=true`. CD-native format (hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations). Distinct from the UX Design Spec instance, which is the Hub-authored markdown counterpart authored at TK-02 Step 2.3.

**UX Design Spec instance** (Hub-authored): Per-feature markdown spec at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`, authored by Hub Claude at TK-02 Step 2.3 from CD-authored design files + Hub DS mirror grounding per [TPL] UX Design Spec. The markdown form is for AI-RAG consumption (Hub TK-03 + CC TK-04+).

---

# 4. Task catalog

Thirteen tasks total (TK-01 through TK-13). Scope levels and per-unit-type applicability are summarized below; the formal unit_type catalog with per-unit-type task path is in §4.0 immediately following.

**Inception is not a TK**: Project-level workspace inception (per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance)) and per-app physical skeleton (per CC substantive Workspace Topology canonical (walking-skeleton output set)) are owned outside this source. The TK sequence begins at TK-01 for the first phase of each app.

**Note on "Required" in task descriptions**: each task definition in §4 below includes a `**Human intervention**: **Required**` (or `**Conditional**` / `**None**`) field. The word "Required" here denotes the task's **expected level of operator attention** as a taxonomic classifier — it is descriptive of how the task is designed to be operated, not a mechanism-enforced invariant on the operator. Per [Enforcement·reminder-only] discipline, Hub Claude surfaces the expected attention level at task initiation but cannot canonical-text-enforce operator presence. The classifier reads as: "Required" = task designed for operator-driven execution; "Conditional" = task auto-runs unless failure surfaces operator-needed escalation; "None" = task fully autonomous in steady state. See CC substantive CI/CD Milestone Policy canonical (tooling baseline) for the operator attention allocation rationale underlying this taxonomy.

- **TK-01, TK-02** — **per-phase**, runs once per app per phase; TK-01 produces phase PRD; TK-02 has three internal steps (Step 2.1 / Step 2.2 / Step 2.3) producing phase TDD, phase test plan (master), per-feature integration test plans, per-feature slice-lists, per-unit `assigned_node` decisions, and — when any feature has `tier_1_involved=true` — per-feature CD-authored design files plus per-feature Hub-authored UX Design Spec instances
- **TK-03 through TK-11** — **per-slice within a unit**, looping through slices of `feature` units and the single slice of a `walking_skeleton` unit; not run for `app_integration` units below TK-08 (per §0.3 milestone table and §4.0 per-unit-type task paths)
- **TK-08 through TK-13** — entered directly by `app_integration` units at TK-08 (M2 entry); for `feature` and `walking_skeleton` units, reached as part of the slice's M0 → M5 progression
- **TK-12 through TK-13** — per-slice for slice-bearing units; per-unit (single PR) for `app_integration` units

Within a single phase, the loop structure for `feature` and `walking_skeleton` units is: TK-01 → TK-02 (Step 2.1 → Step 2.2 → Step 2.3) → (for each unit: for each slice in the unit: TK-03 through TK-11) → TK-12 onwards.

The Phase 1 `walking_skeleton` unit must reach `status: merged` before any `feature` unit's TK-03 or any `app_integration` unit's TK-08 begins, per [RULE] Workspace Topology constitutional residue §3 (walking-skeleton-first ordering rule). For `app_integration` units, the loop is: TK-01 → TK-02 (consumed as input) → TK-08 → TK-09 → TK-10 → TK-11 → TK-12 onwards.

## 4.0 Unit_type catalog and per-unit-type task paths

### 4.0.1 Catalog overview

The phase ontology partitions a phase's work into `walking_skeleton` / `feature` / `app_integration` work units. The three unit types share scheduling parity at the node-assignment level (per CC substantive Workspace Topology canonical (parallelism unit)) and run different subsets of the TK-XX sequence based on their slice ontology.

| Unit type | Applicability | Slice count | Milestone profile | Codex fire conditions | Cardinality per phase |
|---|---|---|---|---|---|
| `walking_skeleton` | Phase 1 only | exactly 1 | M0 → M1 → M2 → M3 → M4 → M5 (full chain) | M4 (TK-11) | exactly 1 (Phase 1); 0 (Phase N≥2) |
| `feature` | All phases | 1+ (typical 3–10) | M0 → M1 → M2 → M3 → M4 → M5 per slice (full chain) | M4 per slice (TK-11) | 1+ |
| `app_integration` | All phases (per-phase only; not cross-phase) | 0 | M2 → M3 → M4 → M5 (truncated; no M0 / M1) | M4 only (TK-11) | 0+ |

Per-unit-type milestone profile is owned by [MECH] CI/CD Milestone Policy. Per-unit-type code review tool fire conditions are owned by CC substantive Codex Plugin Usage canonical (post-Phase-3 migration). Code review fires at M4 (TK-11) for all three unit types; cross-model review reminders at TK-01 / TK-02 sign-offs are operator-advisory and are not Codex invocations.

### 4.0.2 Walking_skeleton unit task path

A `walking_skeleton` unit produces six outputs in a single PR (canonical list owned by CC substantive Workspace Topology canonical (walking-skeleton output set)). The unit consists of exactly one slice that runs the full TK chain.

| TK | Walking_skeleton-specific notes |
|---|---|
| TK-01 | Phase 1 PRD; covers all features in Phase 1 plus implicit walking-skeleton scope |
| TK-02 | Phase 1 TDD §3 Walking skeleton scope is authored alongside per-feature `§4.{feature-slug}` sections in Step 2.1; walking_skeleton unit's `assigned_node` is decided alongside per-feature node assignments in Step 2.1; if walking-skeleton scope itself touches Tier 1 (rare), Step 2.2 + Step 2.3 produce design files and a UX Design Spec instance for the walking-skeleton scope, treated as the `walking-skeleton` feature-slug-equivalent |
| TK-03 | Single-slice authoring; `slice-id` = `walking-skeleton`; Hub-side per [REF] Hub-CD-CC Architecture §5.1; UX brief drawn from Hub-authored UX Design Spec instance from TK-02 Step 2.3 if walking-skeleton scope touches Tier 1 |
| TK-04 | M0 entry self-check (folded into TK-04 entry per the post-refactor architecture; the prior separate M0 gate task has been retired); GitHub Issue marker authoring; first commit on `feature/<app-slug>/walking-skeleton` branch; produces the six walking_skeleton outputs in the single PR per CC substantive Workspace Topology canonical (walking-skeleton output set); CC main loop begins code generation |
| TK-05 → TK-10 | Single-slice loop continues: tests, adversarial, evidence |
| TK-11 | M4 prep + code review fires per CC substantive Codex Plugin Usage canonical |
| TK-12 | M4 merge as for any unit |
| TK-13 | M5 staging deploy on `main` merge |

### 4.0.3 Feature unit task path

Standard TK-01 through TK-13 path; one iteration of TK-03 through TK-11 per slice; last slice's TK-08 expanded for feature integration test execution per [MECH] CI/CD Milestone Policy.

### 4.0.4 App_integration unit task path

| TK | App_integration-specific notes |
|---|---|
| TK-01, TK-02 | Consumed as input (phase test plan + feature integration test plans); `app_integration` unit's `assigned_node` is decided in TK-02 Step 2.1 alongside other unit assignments |
| TK-03 → TK-07 | **Not applicable** (no slice-level new feature code; no M0 / M1 within the unit) |
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
- **Prerequisite**: workspace inception complete per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance). For Phase N≥2 of an existing app, the prior phase's TK-13 release (or equivalent stable boundary) should also be reached. For Phase 1 of a new app, the `{app-slug}` is decided in this task per operator pure judgment (immutable once committed) and added to the frozen app-slug roster maintained at workspace level per CC substantive Claude Code Architecture Rules canonical §Y (app-slug roster); the app's physical skeleton is produced subsequently as part of the Phase 1 walking_skeleton unit's output set per CC substantive Workspace Topology canonical (walking-skeleton output set)
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

## TK-02: Produce phase TDD + phase test plan + feature integration test plans + per-feature slice-lists + per-feature node assignments + (conditional) per-feature design files + per-feature UX Design Spec instances

TK-02 is a multi-step task with three internal steps: Step 2.1 (Hub-side core spec authoring) → Step 2.2 (CD-side per-feature design file production, conditional on `tier_1_involved=true`) → Step 2.3 (Hub-side design file quality check + per-feature UX Design Spec instance authoring). The three steps execute in order, with Step 2.2 / Step 2.3 conditional on whether any feature in the phase has `tier_1_involved=true`. The overall TK-02 sign-off covers all three steps.

- **Workspace**: Hub Claude (Step 2.1 + Step 2.3) + Claude Design (Step 2.2, conditional)
- **Stage**: S1; **Milestone**: Pre-M0
- **Scope**: per-phase per-app (one execution produces all TK-02 outputs for one phase)

### Step 2.1 — Hub-side core spec authoring (always runs)

- **Workspace**: Hub Claude
- **Role sequence**: H + HC (coordinated production of multiple paired artifacts; operator decides each feature's and each unit's `assigned_node` during this step)
- **Inputs**: Phase PRD (TK-01); existing TDDs under `apps/*/specs/tdd/**` (especially the prior phase TDD if `{N}≥2`, used as architectural baseline); current node availability state (operator's pure-judgment input per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 1))
- **Outputs** (paired output set; the count of each varies with the number of features in the phase):
  - **Per-unit `assigned_node` decisions** — one decision per work unit in the phase (recorded inside `§4.{feature-slug}.Header` of the phase TDD for `feature` units; in TDD §3 walking skeleton header for the Phase 1 `walking_skeleton` unit; in the GitHub Issue marker block for `app_integration` units which lack a per-feature TDD section)
  - **Phase TDD** content for `apps/{app-slug}/specs/tdd/phase-{N}.md` — header mandatory fields: `app_slug`, `phase_number`, `Features in this phase`; body sections per [TPL] TDD: §1 architecture, §2 cross-feature concerns, §3 walking skeleton scope (Phase 1 only), §4 per-feature engineering spec. Each feature's `§4.{feature-slug}.Header.tier_1_involved` flag is set here. When any feature in the phase has `tier_1_involved=true`, the TDD references the corresponding UX Design Spec instance path (`apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`); the UX coverage itself lives in the UX Design Spec instance (Hub-authored at Step 2.3) rather than as a TDD sub-section
  - **Phase test plan (master, markdown)** content for `apps/{app-slug}/specs/test-plan/phase-{N}.md` per [TPL] Test Plan Schema §2
  - **Feature integration test plans (yaml)** — one per feature in the phase, at `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` per [TPL] Test Plan Schema §3
  - **Per-feature slice-lists** — one per feature in the phase, at `apps/{app-slug}/specs/slice-list/{feature-slug}.md` per [TPL] TDD `§4.{feature-slug}.Slice-List`
  - **App-scoped openapi additive update** — `apps/{app-slug}/specs/openapi.yaml` updated with new or evolved API surfaces from this phase

### Step 2.2 — CD-side per-feature design file production (conditional)

- **Workspace**: Claude Design (per feature with `tier_1_involved=true`)
- **Condition**: fires per feature when the feature's `§4.{feature-slug}.Header.tier_1_involved=true` in the TDD authored at Step 2.1. Skipped entirely when no features in the phase touch Tier 1.
- **Role sequence**: H (initiates each CD session, transfers Hub drop files) + CD (authors design files within its native workspace)
- **Inputs** (per feature; transferred to CD as drop files with a Hub-attention prompt directing CD to UI-relevant sections):
  - Phase PRD relevant sections (the feature's PRD sub-sections covering user value, scenarios, user flows)
  - Phase TDD relevant sections (the feature's `§4.{feature-slug}.Header` + `§4.{feature-slug}.Module-Decomposition` + `§4.{feature-slug}.API-Contracts` summary at UI-relevance level — enough for CD to ground component selection in the actual data and interaction surfaces)
  - Hub DS mirror reference (CD reads the Hub mirror at `hdc_ref_design-system.md` via the drop files, or via direct access if CD-side DS mirror exists; this grounds CD's component selection in the actual DS inventory). Per [REF] Hub-CD-CC Architecture §3.4.1, CD is the design-file author and consults DS content for component / pattern selection.
- **Outputs** (per feature, CD-native format; transferred back to Hub for Step 2.3):
  - Hi-fi mockups for all affected Tier 1 screens
  - Prototypes / wireframes for interaction flows where static mockups are insufficient
  - Component callouts identifying which DS components are used per screen
  - Interaction flows with embedded textual annotations (state transitions, edge cases, empty/loading/error states)
  - Any new-component / new-token proposals (these inform Step 2.3's UX Design Spec §2.4 entry; the DS change request itself is per [RULE] DSG §12)
- **Trigger**: Operator manual (after Step 2.1 TDD is drafted and `tier_1_involved` flags are set; operator opens a CD session per feature with `tier_1_involved=true`)
- **CD input strategy v1**: Full relevant PRD + TDD sections as drop files + Hub Claude attention prompt directing CD to UI-relevant sections. (Hub does not pre-extract a "UI summary"; the rationale is preserving signal-to-noise without dropping interaction-relevant content — see TK-02 Step 2.2 mechanism note below.)

### Step 2.3 — Hub-side design file quality check + UX Design Spec instance authoring (conditional, runs when Step 2.2 fired)

- **Workspace**: Hub Claude
- **Condition**: runs once per feature for which Step 2.2 fired
- **Role sequence**: H + HC (design file quality check first; UX Design Spec instance authoring second)
- **Inputs** (per feature):
  - CD-authored design files from Step 2.2 (transferred to Hub per [MECH] Cross-Tool Workflow Handoff §2.2)
  - Phase PRD + phase TDD (the feature's relevant sections)
  - **Hub DS mirror** at `hdc_ref_design-system.md` (consumed per [RULE] DSG §13.3 Hub-side consumption discipline)
  - [TPL] UX Design Spec (the spec contract authored as Hub-authored markdown)
  - [TPL] UX Design Spec §3 reviewer checklist (governs the design file quality check)
- **Outputs** (per feature):
  - Design file quality check disposition recorded in conversation log (`Pass` / `Pass with annotation` / `Reject — return to CD for revision`) per [TPL] UX Design Spec §3
  - **Per-feature UX Design Spec instance markdown** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` per [TPL] UX Design Spec
  - **Conditional**: DS change request entries (additive: captured as UX Design Spec instance §2.4 New-Components-Or-Tokens; breaking: separate change file per [RULE] DSG §12.4) when the design files introduce new components or tokens not present in the Hub mirror
- **Mechanism**:
  1. Hub Claude verifies the CD-authored design files against the Hub DS mirror per [TPL] UX Design Spec §3 reviewer checklist — confirms components are from DS Tier A / Tier B inventory, tokens match DS taxonomy, layout patterns match DS pattern catalog, a11y annotations conform to [RULE] DSG §6 stance
  2. If quality check disposition is `Reject — return to CD for revision`: route back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.3 pauses until revised design files are transferred back
  3. If `Pass` or `Pass with annotation`: Hub Claude authors the per-feature UX Design Spec instance markdown grounded in the Hub mirror (every `component: <name>` reference corresponds to an actual Tier A or Tier B entry; every token reference corresponds to an actual taxonomy entry; every layout pattern reference corresponds to an actual pattern in DS §5)
  4. If new components or tokens are needed: Hub Claude authors the §2.4 New-Components-Or-Tokens entry capturing the additive plan per [RULE] DSG §12.4 change content structure; the actual DS instance content change is authored by CD at the originating feature's M4 → merge-to-main milestone per DSG §12.5

### TK-02 task-level fields (apply to the full three-step task)

- **Prerequisite**: TK-01
- **Trigger**: **Manual**
- **Completion**: Phase TDD uses [TPL] TDD template; `Features in this phase` matches phase PRD §7.1 feature list; per-feature module decomposition MECE within each feature; openapi covers all TDD-introduced API surfaces; each feature's slice-list slices are single-objective; phase test plan exit criteria are testable; per-feature `assigned_node` decided; cross-tier traceability consistent; **for each feature with `tier_1_involved=true`**: CD-authored design files complete and Hub design file quality check disposition is `Pass` or `Pass with annotation`; per-feature UX Design Spec instance markdown authored at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` and signs off the reviewer checklist; operator signs off the full output set; **cross-model review reminder fires at sign-off** (per TK-01 mechanics applied to TDD; the reminder applies to the TDD specifically — the operator may invoke cross-model review of architecture decisions in §1 + §2 + §4 + walking-skeleton scope)
- **Failure routing**: Phase PRD gaps → TK-01; MECE violation → revise within Step 2.1; **design file quality check `Reject` disposition → return to CD per [MECH] Cross-Tool Workflow Handoff §6, Step 2.2 redo**; **UX Design Spec authoring gap (Hub Claude finds design files insufficient to ground UX Design Spec content) → return to CD for additional design file coverage**; Design System change required → produce DS change request per [RULE] DSG §12 (additive: captured in UX Design Spec instance §2.4 at Step 2.3; breaking: separate change file + review gate); new domain capability needed → schedule as feature-driven domain extension
- **Human intervention**: **Required**

**Per-unit node assignment note**: `assigned_node` is per-unit, not per-phase. A phase may contain multiple units (one Phase 1 walking_skeleton + multiple feature units + zero-or-more app_integration units) executing on different nodes. Each assignment is an independent operator decision per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 1).

**Walking skeleton scope (Phase 1 only)**: The Phase 1 TDD's §3 Walking skeleton scope sub-section captures the thinnest end-to-end vertical slice that proves foundational architecture works before Phase 1 feature units begin. When walking-skeleton scope itself touches Tier 1 (rare), Step 2.2 + Step 2.3 fire for the walking-skeleton scope as if it were a feature with `tier_1_involved=true`; the UX Design Spec instance is authored at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md`.

**TK-02 Step 2.2 mechanism note (CD input strategy v1)**: The operator transfers the full relevant PRD + TDD sections as drop files to CD, accompanied by a Hub-attention prompt directing CD to UI-relevant sections. This is preferred over Hub pre-extracting a "UI summary" because: (a) what's "UI-relevant" depends on CD's design judgment (e.g., a data validation rule may turn out to drive an interaction state that needs visual treatment); (b) Hub pre-extraction risks dropping interaction-relevant content that CD would have picked up. The trade-off is signal-to-noise — but for design-file production, the cost of missing context outweighs the cost of CD processing slightly more input. This is a v1 strategy; if Hub pre-extraction proves more efficient in practice, this mechanism may be revised.

**Cross-model review reminder at sign-off** ([Enforcement·reminder-only]): Same mechanics as TK-01. Hub Claude surfaces a reminder; operator chooses to invoke cross-model review (e.g., Codex review of the TDD architecture) or proceed.

**Hub-to-assigned_node onboarding (between TK-02 and the unit's first node-side TK)**: Immediately after TK-02 sign-off, for each unit in the phase the operator onboards that unit's `assigned_node` per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4). The Hub-level contracts for this onboarding: (a) the working branch follows the naming pattern `feature/<app-slug>/<unit-slug>`; (b) phase-level TK-01 PRD and TK-02 outputs (TDD, test-plan, openapi, slice-list, **and per-feature UX Design Spec instance markdown when authored**) land at `apps/{app-slug}/specs/{prd,tdd,test-plan,openapi,slice-list,ux-design-spec}/` on the working branch; (c) the working branch is published so assigned_node can access it; (d) a Claude Code session is started on assigned_node, becoming the execution context for all subsequent node-side TKs for that unit. The specific SCM commands, branch-publication mechanics, and session-bootstrap procedure are operator-personal mechanism owned by CC substantive Workspace Topology canonical. The CD-authored design files accompany as visual reference (transferred to CC at TK-04 entry per [MECH] Cross-Tool Workflow Handoff §3.1, not committed to the monorepo unless the operator explicitly opts to). From this point, all subsequent node-side TKs for that unit execute within that Claude Code session.

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
  - **When Tier 1 involved**: the **Hub-authored UX Design Spec instance markdown** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` (produced at TK-02 Step 2.3); the corresponding CD-authored design files (as visual reference accompanying the UX Design Spec instance in the operator's working materials)
  - Hub DS mirror at `hdc_ref_design-system.md` (consulted by HC for any DS-coupled questions during conversion)
  - Target slice ID; active `feature-slug` and `phase_number`
- **Outputs**:
  - `apps/{app-slug}/specs/intent/{slice-id}.md` — full content including UX brief when Tier 1 involved (UX brief content is a slice-narrow extraction from the Hub-authored UX Design Spec instance per [TPL] Writing Standard §2.3)
  - `apps/{app-slug}/specs/acceptance/{slice-id}.yaml` — full content including accessibility_expectations when Tier 1 involved (lifted from UX Design Spec instance §2.5 per [TPL] Writing Standard §3.9)
  - `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` — full content including visual regression cases and a11y test cases when Tier 1 involved
- **Prerequisite**: TK-02 sign-off (which includes Step 2.3 sign-off when any feature has `tier_1_involved=true`; the active feature's UX Design Spec instance exists at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` and its quality check disposition is `Pass` or `Pass with annotation`)
- **Trigger**: **Manual** (operator picks slice from slice-list)
- **Completion**: Artifacts use their respective [TPL] sources; Tier-1-involving slice has UX brief derived from the Hub-authored UX Design Spec instance; no undefined boundaries; risk_tier mechanically derived from PRD; operator's cross-model review consensus reached; artifacts transferred to assigned_node working directory
- **Failure routing**: Conversion ambiguity → HC raises question to operator within TK-03; cross-model review surfaces issues → revise in Hub; **UX Design Spec instance gap surfaces (insufficient coverage for slice-level UX brief) → escalate to TK-02 Step 2.2 / Step 2.3 (return to CD for design file coverage extension, then re-author UX Design Spec instance)**; DS change required → escalate to TK-02 Step 2.3 (additive change request in UX Design Spec §2.4 + DS change request per [RULE] DSG)
- **Human intervention**: **Required** at the cross-model review step (operator drives the GPT-Claude consensus loop)

**Mechanism rationale (why this TK is Hub-only in the post-refactor architecture)**:
- Per `[REF] Hub-CD-CC Architecture §5.1` content pillar: spec artifact main bodies (PRD / TDD / intent / acceptance / test-plan) are Hub-produced. TK-03 falls under this pillar.
- The per-feature UX Design Spec instance markdown — also a Hub-authored spec artifact — was authored upstream at TK-02 Step 2.3 (the feature-level UX spec, grounded in CD design files + Hub DS mirror). TK-03 extracts slice-narrow content from this Hub-authored instance; it does not invoke CD again.
- Per the user's cross-model review discipline: the operator's Hub-side ChatGPT-Claude consensus loop is the de facto design freeze gate, replacing the pre-refactor separate TK-04 M0 adversarial review. This loop is only operable in Hub.
- Per `[REF] Hub-CD-CC Architecture §5.2` revised presentation pillar: when Tier 1 is involved, **design files** are CD-authored at TK-02 Step 2.2 (CD-native visual artifacts), and the **UX Design Spec instance** is Hub-authored at TK-02 Step 2.3 (markdown spec grounded in design files + Hub DS mirror). TK-03 consumes the Hub-authored UX Design Spec instance as the primary textual UX source; design files accompany as visual reference but TK-03 does not parse them as text.
- The cost of round-tripping TK-03 between Hub and CC (the pre-refactor design) is eliminated: artifacts produced in Hub are transferred to CC once, after the cross-model review, with no revert path needed.

**Skill loading note (CC-side, post-TK-03)**: SK-F (`hdc-arco-enterprise-ui`) is in scope from new TK-04 onwards on assigned_node for Tier 1 code generation (when substantive code writing begins per TK-04 description below). SK-F is **not** invoked at TK-03 because TK-03 is Hub-side and Hub cannot load `.claude/skills/`. The Hub-authored UX Design Spec instance is the upstream guarantee for DS-coupled content at TK-03 (authored at TK-02 Step 2.3 grounded in Hub DS mirror); SK-F enforces DS-coupled correctness at code time grounded in CC mirror. SK-W (`hdc-wcag-accessibility-checker`) is on-demand only per [RULE] Design System Governance §6.

**Unit_type applicability**: TK-03 runs for `feature` and `walking_skeleton` units only.

For `walking_skeleton` units (Phase 1 only, exactly one slice), the input substitutions follow [TPL] PRD + TDD to Intent and Acceptance Conversion Specification §0.7 unit_type applicability:
- TDD reading shifts from `§4.{feature-slug}` to `§3.Walking-Skeleton-Header` + `§3.Scope-And-End-To-End-Coverage`
- `feature-{feature-slug}.yaml` and `slice-list/{feature-slug}.md` inputs are **not applicable** (single-slice unit)
- `assigned_node` is sourced from `§3.Walking-Skeleton-Header.assigned_node`
- target `slice-id` is `walking-skeleton` (matching `unit_id`)
- when walking-skeleton scope touches Tier 1: UX Design Spec instance input is at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md`

For `app_integration` units, TK-03 is skipped entirely (no per-slice interface artifacts; the unit's authoring source is the phase test plan master + feature integration test plans produced at TK-02; entry point is TK-08).

---

## TK-04 through TK-11 — CC-executed task block (constitutional interface)

> **Constitutional scope at Hub residue**: TK-04 through TK-11 are CC-executed tasks. Their detailed execution mechanics (specific subagent invocations, tool commands, sub-steps, internal transitions) are CC substantive content owned by CC substantive DTW canonical. Hub-side residue declares only constitutional identity and Hub-facing interface per task.

## TK-04: M0 entry self-check + spec consumption + code writing

- **Executing workspace**: assigned_node Claude Code
- **Constitutional identity**: Entry point for CC's slice implementation. Absorbs the M0 design-freeze function as a lightweight intake check (spec bundle intact upon CC reception) — not a re-decision of design freeze (per [MECH] CI/CD constitutional residue §2.1).
- **Hub-facing interface — inputs**: Per-slice spec bundle handed off from TK-03 (intent.md, acceptance.yaml, test-plan.yaml + per-feature UX Design Spec instance + design files as visual reference) per [MECH] Cross-Tool Workflow Handoff §3.1
- **Hub-facing interface — outputs**: First commit on feature branch; GitHub Issue marker block updated to `status: in-progress` per [RULE] WT constitutional residue §4.2
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

## TK-12: M4 gate (merge decision + smoke test)

- **Workspace**: Hub Claude or assigned_node (operator's choice)
- **Stage**: S4; **Milestone**: M4
- **Role sequence**:
  1. H (reviews Test Evidence Report, Codex review, domain-judge questions, **accessibility audit**)
  2. H (executes smoke test — **includes spot-check on accessibility-flagged screens and manual-validation items from SK-W report**)
  3. H (issues merge go/no-go; PR target = `main`)
  4. **Conditional**: H merges DS change request if any DS update originated from this slice per [RULE] Design System Governance change flow; when merged, CD regenerates DS markdown export and operator syncs both Hub mirror (`hdc_ref_design-system.md`) and CC mirror (`specs/design-system.md`) in the same cycle per [RULE] DSG §12.5 lock-step invariant
  5. H updates GitHub Issue marker block: `status: merged`
- **Inputs**: Test Evidence Report; Codex review; domain-judge questions; **accessibility audit**
- **Outputs**:
  - Merge decision (target branch = `main`)
  - Smoke test result
  - **Conditional**: DS update merged per [RULE] Design System Governance, with both DS mirrors re-synced from CD-generated DS markdown export
  - Updated GitHub Issue marker block
- **Prerequisite**: TK-11
- **Trigger**: **Manual**
- **Completion**: Merge go → feature branch merged into `main` + DS update applied (if any, with both mirrors re-synced) + marker block updated; merge no-go → issues returned
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
- Within TK-02: Step 2.1 → Step 2.2 trigger (conditional on any feature `tier_1_involved=true`) → Step 2.3: **Manual** (operator initiates CD session per feature when Step 2.1 sets `tier_1_involved` flags; operator returns to Hub session for Step 2.3 after each feature's design files are produced by CD)
- Between TK-02 (Step 2.3 sign-off) → TK-03: **Manual** (operator picks slice from slice-list)

## 5.2 Hub → CD → Hub (within TK-02 Step 2.2 → Step 2.3)

The TK-02 multi-workspace authoring involves operator-mediated transfers between Hub and CD per [MECH] Cross-Tool Workflow Handoff §2:
- **Hub → CD (Step 2.2 entry)**: operator transfers relevant PRD/TDD sections as drop files to a CD project + Hub-attention prompt directing CD to UI-relevant sections per [MECH] Cross-Tool Workflow Handoff §2.1
- **CD → Hub (Step 2.2 exit / Step 2.3 entry)**: operator transfers CD-authored design files back to the Hub session per [MECH] Cross-Tool Workflow Handoff §2.2; Hub Claude performs design file quality check against Hub DS mirror per [TPL] UX Design Spec §3 reviewer checklist; if `Pass` or `Pass with annotation`, Hub Claude authors the per-feature UX Design Spec instance markdown grounded in design files + Hub DS mirror per [RULE] DSG §13.3
- **Quality check `Reject` path**: route back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.3 pauses; Step 2.2 redo for the affected feature

This transition happens conditionally — only per feature with `tier_1_involved=true`. Features that are purely Tier 2 / Tier 3 do not trigger Step 2.2 / Step 2.3.

## 5.3 Hub → assigned_node (TK-02 → onboarding → first node-side TK)

The hub-to-assigned_node handoff happens immediately after TK-02 sign-off (covering all three steps when applicable) per [MECH] Cross-Tool Workflow Handoff §3.1. From the first node-side TK onwards through TK-11, all node-side work executes on assigned_node.

- After TK-02 sign-off, operator manually onboards the assigned_node per CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4). The Hub-level contracts:
  - A working branch is created from the unit's base branch, following the naming pattern `feature/<app-slug>/<unit-slug>`
  - Phase-level TK-01 PRD and TK-02 outputs (TDD, test-plan, openapi, slice-list, **and per-feature UX Design Spec instance markdown when authored**) land at `apps/{app-slug}/specs/{prd,tdd,test-plan,openapi,slice-list,ux-design-spec}/` on the working branch
  - The working branch is published so assigned_node can access it
  - A Claude Code session is started on assigned_node, becoming the execution context for all subsequent node-side TKs for that unit

  The specific SCM commands, branch-publication mechanics, and session-bootstrap procedure are operator-personal mechanism owned by CC substantive Workspace Topology canonical.

Per-slice TK-03 artifacts (intent / acceptance / test-plan) are placed at assigned_node working directory by the operator at the end of each TK-03 iteration per [MECH] Cross-Tool Workflow Handoff §3.1. CD-authored design files accompany the spec bundle as visual reference for the operator and CC, but are not committed to the monorepo unless the operator explicitly opts to.

## 5.4 CC internal transitions

- TK-04 → TK-05: **Auto via hook** (PostToolUse after code write)
- TK-05 → TK-06: **Auto via SubagentStop hook** on unit test failure
- TK-05 / TK-08 / TK-09 / TK-10 → TK-07: **Auto via SubagentStop hook** on non-auto-repairable test failure
- TK-08 → TK-09: **Auto via SubagentStop hook** after TK-08 completion
- TK-09 → TK-10: **Auto via SubagentStop hook** after TK-09 completion
- TK-10 → TK-11: **Auto via SubagentStop hook** after TK-10 completion
- TK-11 → TK-12: **Auto via Notification hook** (notification surfaces Test Evidence Report ready)

## 5.5 CC → Hub (TK-11 evidence + Codex review)

After TK-11 completes, the operator may transfer the code review tool output to a Hub Claude conversation for judgment and archive per [MECH] Cross-Tool Workflow Handoff §3.2 (specific code review tool processing rules owned by CC substantive Codex Plugin Usage canonical post-Phase-3 migration).

## 5.6 Hub or assigned_node → CI/CD (TK-12 → TK-13)

After TK-12 merge to `main`, CI/CD auto-fires TK-13 staging deploy. No operator action between TK-12 and TK-13 in the success path.

---

# 6. Human intervention budget

## 6.1 Steady-state (per slice for slice-bearing units; per unit for app_integration)

The intervention budget varies by unit_type because `app_integration` units skip the M0 entry self-check (folded into TK-04 for `feature` and `walking_skeleton` units) and TK-03 entirely per §4.0.4.

**Base table** (applies to `feature` and `walking_skeleton` units, slice-level loop):

| # | Task | Purpose | Workspace |
|---|---|---|---|
| 1 | TK-01 | PRD sign-off (cross-model review reminder fires) | Hub |
| 2 | TK-02 | TDD + openapi + slice-list + assigned_node sign-off across Step 2.1 / Step 2.2 / Step 2.3 (Step 2.2 + Step 2.3 conditional on any feature `tier_1_involved=true`; design file quality check + UX Design Spec instance authoring happen at Step 2.3; cross-model review reminder fires at full TK-02 sign-off) | Hub + CD |
| 3 | TK-03 | Per-slice specs review (transition period only; skipped after N=2) | Hub |
| 4 | TK-04 (entry self-check sub-step) | M0 entry self-check verification | assigned_node CC |
| 5 | TK-12 | M4 merge to `main` + smoke test + DS change merge + (conditional) DS markdown export sync to both mirrors | Hub or assigned_node |

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
| 9 | TK-02 Step 2.3 | Design file quality check `Reject` disposition → return to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback |

## 6.3 Anti-drift on intervention budget

If steady-state interventions exceed the §6.1 per-unit-type budget for 2+ consecutive units of the same type — concretely: > 5 per slice for `feature` units, > 5 total for the `walking_skeleton` unit, or > 4 total for an `app_integration` unit — investigate:
- Hook chain silent failure
- A3 severity miscalibration
- Auto-repair loops exhausting
- Compliance-checker first-pass violations frequent
- **Design System Governance drift recurrent**
- **Cross-app domain contract churn**
- **CD-side design file quality check failures recurrent at TK-02 Step 2.3** (operator returning CD design files for redo too often suggests upstream framing issues — possibly insufficient PRD/TDD drop-file context at Step 2.2 entry, or DS mirror not adequately consulted by CD)
- **UX Design Spec instance authoring stalls recurrent at TK-02 Step 2.3** (Hub Claude finding design files insufficient to ground UX Design Spec content too often suggests Step 2.2 input strategy needs revision)

---

# 7. Failure routing matrix

| Failure source | Routing target | Mechanism |
|---|---|---|
| Static analysis critical (TK-04) | TK-04 | PostToolUse hook |
| **Tier 1 Design System drift (TK-04)** | **TK-04 with SK-F reinforcement** | **SK-F runtime** |
| **TK-04 M0 self-check finds Hub/CC mirror version mismatch** | **Operator triggers DS markdown export resync per [RULE] DSG §12.5 lock-step** | **Manual** |
| **TK-02 Step 2.3 design file quality check `Reject` disposition** | **Return to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.2 redo for affected feature** | **Operator manual** |
| **TK-02 Step 2.3 UX Design Spec authoring gap (design files insufficient)** | **Return to CD for additional design file coverage; Step 2.2 → Step 2.3 redo for affected feature** | **Operator manual** |
| **TK-02 / TK-03 DS change required** | **Captured in UX Design Spec instance §2.4 New-Components-Or-Tokens at Step 2.3 (additive); separate change file at Step 2.3 + review gate (breaking); per [RULE] DSG §12** | **Manual** |
| Unit test failure (TK-05) | TK-06 (≤3) | SubagentStop hook |
| Unit test failure after 3 (TK-06) | TK-07 | SubagentStop hook |
| Internal-integration failure (TK-05) | TK-07 | SubagentStop hook |
| Contract / external-integration failure (TK-08) | TK-07 | SubagentStop hook |
| **Producer-side contract verification failure (TK-08)** | **TK-07** | **SubagentStop hook** |
| Adversarial-loop test failure (TK-09) | TK-07 | SubagentStop hook |
| E2E / visual / performance failure (TK-10) | TK-07 | SubagentStop hook |
| **Accessibility baseline critical or serious (TK-10)** | **TK-07 + Notification** | **SK-W + hook** |
| Security critical (TK-10) | Notification | Notification hook |
| Compliance severe (TK-08, TK-11) | Notification | Notification hook |
| **Design System Governance compliance final violation (TK-11)** | **Notification** | **Notification hook** |
| **App/domain placement violation (TK-08, TK-11)** | **Notification** | **Notification hook** |
| RCA: revise specs | TK-03 (or upstream, including TK-02 Step 2.3 when UX Design Spec instance needs revision) | Manual |
| RCA: revise code | TK-04 | Manual |
| **RCA: revise DS** | **DS change request per [RULE] Design System Governance §12** | **Manual** |
| **RCA: revise domain contract** | **TK-02 (consumer side) or domain-internal change request** | **Manual** |
| RCA: accept limitation | Proceed with waiver | Manual |
| M4 no-go (TK-12) | Back to specific TK | Manual |
| **TK-12 DS markdown export sync failure (one mirror updated, other not)** | **Operator re-syncs per [RULE] DSG §12.5 lock-step invariant** | **Manual** |
| Staging deploy failure (TK-13) | Auto rollback + Notification + TK-12 | CI/CD |

---

# 8. Anti-drift red flags

> **Scope**: this section enumerates **DTW-specific** anti-drift red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced rather than duplicated. See [OS] §12.3 for the full anti-drift red flag ownership map.

**Task-level** (DTW-specific):
- A task silently skipped
- Hook chain reports completion but downstream task no trigger
- TK-01, TK-02, or TK-04 entry self-check proceeding without operator sign-off (the operator's sign-off on TK-02 + the operator-driven Hub-side cross-model review at TK-03 sign-off are the design freeze gates; TK-04 entry self-check is a structural check executed by CC that nevertheless requires operator awareness when it surfaces inconsistency)
- **TK-02 Step 2.1 sign-off proceeding without setting `tier_1_involved` flags per feature** — the flag drives whether Step 2.2 / Step 2.3 fire; missing flags cause Tier 1 features to skip CD-side design file production silently
- **TK-02 Step 2.2 fired but Step 2.3 skipped** — Step 2.2 produces CD-native design files; without Step 2.3 the markdown UX Design Spec instance is missing and downstream Hub TK-03 / CC TK-04+ have no AI-RAG-consumable UX spec
- **TK-02 Step 2.3 UX Design Spec instance authored without consulting Hub DS mirror** — violates [RULE] DSG §13.3 Hub-side consumption discipline; results in UX Design Spec instances referencing nonexistent or misnamed DS elements
- TK-03 transition period skipped prematurely (before N=2 slices)
- Reintroduction of TK-15+ (release authorization, production deploy) into the AI-dev TK sequence without canonical revision authorizing it
- **Cross-model review reminder at TK-01 / TK-02 promoted from advisory to hard gate without canonical revision** (the reminder is [Enforcement·reminder-only]; reframing it as a required task constitutes scope expansion requiring revision of this source)

**Workspace dimension** (DTW-specific):
- TK-04 onwards executed in Hub Claude instead of assigned_node Claude Code (breaks evidence chain locality and SK-F coverage; TK-04+ is mechanically impossible in hub anyway — Hub cannot load `.claude/skills/`)
- TK-01, TK-02 Step 2.1, TK-02 Step 2.3, or TK-03 executed in assigned_node CC instead of hub (loses hub's content-pillar discipline per [REF] Hub-CD-CC Architecture §5.1)
- **TK-02 Step 2.2 executed in Hub instead of CD when feature has `tier_1_involved=true`** (loses presentation-pillar discipline; Hub cannot produce CD-native visual design files)
- **TK-02 Step 2.3 executed in CD instead of Hub** (loses content-pillar discipline; CD does not author markdown specs — UX Design Spec instance authoring belongs in Hub per the revised architecture)
- Hub-to-assigned_node onboarding skipped or partial
- **Operator hand-authoring UX content in Hub at TK-02 Step 2.3 without consulting Hub DS mirror or CD-authored design files** — Step 2.3 requires both inputs (design files for visual grounding, Hub mirror for DS grounding); skipping either invalidates the UX Design Spec instance's grounding chain
- **Operator skipping CD design files entirely at TK-02 Step 2.2 when feature has `tier_1_involved=true`, going directly to Hub UX Design Spec instance authoring** — Hub Claude has no visual reasoning capability; UX Design Spec instances authored without design file grounding produce content disconnected from actual visual design (the operator may sometimes choose to bypass CD for trivial UX content with clearly named patterns, but recurring bypass on non-trivial UX is a drift signal)

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
- **TK-02 Step 2.2 CD design files transferred to Hub Step 2.3 without operator audit** (per [MECH] Cross-Tool Workflow Handoff §2.2 audit checklist)
- **TK-02 Step 2.3 UX Design Spec instance transferred to assigned_node working directory without operator audit** (UX Design Spec instance is a Hub-authored markdown spec; standard operator-mediated transfer discipline applies)
- TK-11 Codex review output bypasses Hub judgment (per [MECH] Cross-Tool Workflow Handoff §3.2.3)
- **TK-12 DS markdown export sync skipped or partial when slice carries DS change** (violates [RULE] DSG §12.5 lock-step invariant; results in Hub mirror and CC mirror at different versions)

**UX and accessibility**: most red flags here are owned by CC substantive Code Quality Rule Set canonical §10 and [RULE] Design System Governance §16 governance. DTW local variants:
- **SK-F (`hdc-arco-enterprise-ui`) not invoked during TK-04 Tier 1 code generation** (the TK-04 instance of skill-loading drift)
- **Tier-1-involving feature's UX Design Spec instance missing at TK-02 Step 2.3 sign-off** (when CD-side design files were produced but Hub-side UX Design Spec authoring was skipped)
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
- **"skip Step 2.2 even though this feature touches Tier 1"** / **"skip the CD design files for this Tier 1 feature"** (Step 2.2 is required per [REF] Hub-CD-CC Architecture §5.2 revised; skipping is a presentation-pillar bypass)
- **"skip Step 2.3, just go to TK-03 directly with the CD design files"** / **"don't author the UX Design Spec instance, TK-03 can read the design files"** (TK-03 consumes the Hub-authored UX Design Spec instance as the primary textual UX source; design files alone do not satisfy AI-RAG consumption requirements)

**Workspace-shift phrasing** → reference §0.4 and §4 TK-02 Step 2.2 / Step 2.3 / TK-03 / TK-04:
- **"let me author the UX Design Spec instance in CD"** / **"have CD produce the markdown spec"** — Step 2.3 belongs in Hub per the revised architecture; CD outputs design files, not markdown specs
- **"have Hub produce the design files / mockups"** — Step 2.2 belongs in CD; Hub Claude cannot produce CD-native visual artifacts
- "let me draft the intent in this hub chat without consulting the UX Design Spec instance" (when slice involves Tier 1 — reference TK-03 inputs)
- "let me write the test-plan UX-touching fields here in hub" (these fields are derived from the Hub-authored UX Design Spec instance, not invented in TK-03)
- "do the M0 entry self-check in hub Claude" (M0 entry self-check is a CC-side structural verification per TK-04; it cannot run at Hub because the CC mirror SK-F engagement is part of the check)
- "skip onboarding, just generate intent.md here"
- "let me write the M0 marker block manually instead of using `gh issue edit`"

**Sign-off bypass phrasing** → reference §6.1 (steady-state intervention budget):
- "auto-approve TK-02"
- **"auto-approve TK-02 Step 2.3 design file quality check"** (Step 2.3 quality check requires operator awareness; the `Pass` / `Pass with annotation` / `Reject` disposition is recorded in the conversation log)
- "let CC sign off TK-04 entry self-check unilaterally without surfacing inconsistency" (CC executes the self-check mechanically; when inconsistency is found, operator awareness is required)
- "skip the M4 manual review"
- "skip the cross-model review reminder" (the reminder is [Enforcement·reminder-only]; skipping is allowed but the operator should acknowledge skipping consciously)

**Cross-model review phrasing** → reference §4 TK-01 / TK-02 (reminder mechanics):
- "always run Codex review on every PRD" (this would promote the reminder to mandatory — surface that the reminder is advisory and ask the operator to confirm if they want canonical revision to make it mandatory)
- "skip the cross-model review for this PRD" (this is allowed — surface the reminder once, then proceed if the operator confirms)

**DS mirror sync phrasing** → reference §4 TK-12 + [RULE] DSG §12.5:
- **"merge DS to Hub mirror only, skip CC mirror"** / **"sync to CC mirror only, the Hub mirror can wait"** (violates [RULE] DSG §12.5 lock-step invariant; both mirrors MUST be re-synced in the same cycle)
- **"edit `hdc_ref_design-system.md` directly to fix this"** / **"hand-edit `specs/design-system.md` for this slice"** (both mirrors are read-only; direct edits violate [RULE] DSG §12.6)

**AI-dev / company-side boundary phrasing** → reference §4 TK-12 / TK-13 and [MECH] Application Lifecycle Handoff §0.2:
- "deploy this to prod from here" / "push to production"
- "tag a release in this monorepo" / "cut a release tag"
- "set up M5-prod" / "add a TK-15 / TK-16 step"
- "reintroduce hdc/feature-development" / "add an integration branch between feature and main"

Hub Claude reminders are conversational. The operator may override with explicit acknowledgment, but the override itself must be stated in the conversation, preserving traceability for later retrospective review.
