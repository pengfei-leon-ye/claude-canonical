# [TPL] Intent and Acceptance Interface Writing Standard

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable writing standard for feature-slice `intent.md` and `acceptance.yaml` as execution-interface files produced from the Y-chain upstream (PRD + TDD) and consumed downstream by Claude Code implementation and multi-agent testing
- **Source Category**: Cat 4
- **Management-System Role**: Specification-support template; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Boundary note**: This source intentionally excludes `evidence.md` and `test-plan.yaml`. `evidence.md` is an execution-side approval pack standard for the AI virtual development team, not a project canonical source in this hub; `test-plan.yaml` is owned by `[TPL] Test Plan YAML Schema`. For the semantic description of `evidence.md` and its distinction from the milestone-level Test Evidence Report, see [MECH] CI/CD Milestone Policy §6.
- **Relationship to [OS]**: Supports the Specify loop by creating lower-ambiguity execution interfaces without turning this hub into an engineering-design repository
- **Relationship to [MECH] Development Track Workflow**: intent.md and acceptance.yaml are produced in TK-03 of the Development Track Workflow; consumed in TK-06, TK-10, TK-11, TK-12, TK-13
- **Relationship to [RULE] Claude Code Architecture Rules**: Permissions declared in acceptance.yaml must respect tier boundaries defined in that source; UX brief in intent.md only appears when Tier 1 is involved; repository path layout (`apps/{app-slug}/specs/...`) is owned by CC substantive CCAR canonical §Y.1
- **Relationship to [MECH] CI/CD Milestone Policy**: §6 owns the semantic disambiguation between `evidence.md` and the milestone-level Test Evidence Report; §6.4 owns the `operator_digest` definition that appears in this source's evidence_required default set
- **Relationship to [REF] Hub-CD-CC Architecture**: intent.md and acceptance.yaml main bodies are produced by Hub Claude at TK-03 per §5.1 content pillar; when Tier 1 is involved, the upstream UX Design Spec instance is Hub-authored at TK-02 Step 2.3 per [TPL] UX Design Spec (drawing from CD-produced design files per §5.2 presentation pillar concept-vs-realization split, per [RULE] DSG §13.3), and is consumed as input source for the intent.md UX brief field per §2.3 below. After TK-03 conclusion, both files are transferred to CC via [MECH] Cross-Tool Workflow Handoff §3.1 for the implementation pillar.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2.2 (CD → Hub) brings CD-produced design files into Hub as input to TK-02 Step 2.3 UX Design Spec instance authoring when Tier 1 is involved; §3.1 (Hub → CC) carries the finished interface pair plus the Hub-authored UX Design Spec instance markdown and CD design files (as visual reference) onward to CC.
- **Relationship to adjacent [TPL] sources**:
  - Y-chain upstream: `[TPL] PRD / Prototype / MVP Spec Template` + `[TPL] Technical Design Document Template` both feed this artifact pair
  - When Tier 1 involved: `[TPL] UX Design Spec` instance for the feature — Hub-authored at TK-02 Step 2.3 from CD-authored design files, landed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` before TK-03 — supplies UX brief content
  - Paired with `[TPL] Test Plan YAML Schema` (same slice, parallel production in TK-03)
  - Conversion mechanics: `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification`
  - Project-level reference: `[RULE] Design System Governance` (DS instance content lives in CD as SOT per DSG §1.1 two-way distribution; CC carries a read-only code-time mirror at `specs/design-system.md`, synced from CD via the reviewed DS markdown export per DSG §12.3 + §12.7; Hub holds no DS instance copy)
- **Pairings I participate in**: P-29 (with [TPL] UX Design Spec §2 — when Tier 1 is involved, this Writing Standard's §2.3 UX brief and §3.9 accessibility_expectations both read UX Design Spec instance content as upstream)

## How to use this source

Use this source when:
- a canonical PRD and TDD both exist and are stable enough to serve as upstream truth
- one feature slice, one worktree, or one PR needs a smaller and less ambiguous execution interface than the full PRD+TDD pair
- the human reviewer will approve based mainly on requirement intent and acceptance logic rather than line-by-line code reading
- multiple AI agents need the same execution boundary and validation contract

Do not use this source as:
- a replacement for PRD (upstream business truth)
- a replacement for TDD (upstream technical architecture truth)
- a replacement for Design System Governance (project-level UX foundation)
- a test plan repository (that is `test-plan.yaml`, separate artifact)
- a sprint task board
- a place to carry unresolved business-rule ambiguity into implementation

---

# 0. Position and boundary

## 0.1 File scope

This source defines the writing standard for two interface files per slice:

1. `apps/{app-slug}/specs/intent/{slice-id}.md`
2. `apps/{app-slug}/specs/acceptance/{slice-id}.yaml`

Both files are under the active feature's app directory per CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1). The path prefix `apps/{app-slug}/` is mandatory; no feature-level intent or acceptance lives at the repository root.

## 0.2 Project-level singleton references and per-feature UX Design Spec instance path

One project-level singleton path is referenced by intent.md and acceptance.yaml (not under any app):

- `specs/design-system.md` — the **CC code-time mirror** of the DS instance per [RULE] DSG §1.1 (the DS instance SOT lives in CD; CC carries this read-only mirror at the monorepo root, synced from CD via the reviewed DS markdown export per DSG §12.3 + §12.7). The CC mirror is the path intent.md and acceptance.yaml reference at code-generation time; Hub holds no DS instance copy and consults the CD-authored design files at spec authoring time.

This singleton remains at the repository root because it declares project-wide UX foundation, not feature-scoped content.

One per-feature path is also referenced when Tier 1 is involved (under the active app):

- `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` — the **Hub-authored UX Design Spec instance markdown**, produced at TK-02 Step 2.3 per [TPL] UX Design Spec from CD-authored design files (CD-side per [REF] Hub-CD-CC Architecture §5.2 presentation pillar, transferred to Hub per [MECH] Cross-Tool Workflow Handoff §2.2) grounded in the CD-authored design files per [RULE] DSG §13.3. Hub Claude authors this markdown; it is committed to the CC monorepo before TK-03 begins and forwarded to CC alongside intent.md / acceptance.yaml at TK-04 entry per [MECH] Cross-Tool Workflow Handoff §3.1.

Two earlier-revision paths are intentionally removed and remain drift signals if referenced:
- `specs/design-system-changes/{change-id}.md` — no longer exists as a CC-side artifact. DS instance change drafts are CD-internal per [RULE] DSG §1.1 + §12; the additive update plan content travels through the feature's UX Design Spec instance §2.4 instead. Any reference to this legacy path in intent.md or acceptance.yaml is a drift signal.
- `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` — no longer exists as a CC-side artifact. The pre-flip model placed a CD-authored UX bundle (HTML/PDF/ZIP visual assets) at this path; under the current architecture, the Hub-authored UX Design Spec instance markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` is the canonical UX surface intent.md / acceptance.yaml reference. CD-produced design files travel separately as visual reference per [MECH] Cross-Tool Workflow Handoff §3.1 but are not landed at the retired `ux-bundles/` path. Any reference to `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` in intent.md or acceptance.yaml is a drift signal.

---

# 1. Cross-file writing principles

Apply these principles across both `intent.md` and `acceptance.yaml`.

## 1.1 Explicit and observable language

Prefer:
- externally observable behavior
- business state changes
- explicit constraints
- explicit expected results

Avoid vague terms such as `correct`, `proper`, `appropriate`, `user-friendly`, `optimized`, `stable` unless a concrete meaning is attached.

## 1.2 One statement, one judgment point

A requirement sentence should normally contain one main judgment point. If one sentence contains multiple independent outcomes, split it.

## 1.3 Business-first, architecture-second, implementation-last

`intent.md` and `acceptance.yaml` should describe:
- business intent (from PRD)
- scope and non-scope
- actors and permissions
- constraints derived from architecture boundaries (from TDD)
- validation logic
- externally visible outcomes
- UX brief only when Tier 1 is involved (from the Hub-authored UX Design Spec instance at TK-02 Step 2.3 per [TPL] UX Design Spec, grounded in CD-authored design files, with [RULE] DSG topic-level rules as sanity-check baseline)
- accessibility expectations only when Tier 1 is involved (from the UX Design Spec instance §2.5 accessibility call-outs)
- slice-level implementation tasks (the operator-authored work plan that orients CC execution at slice start)

They should not describe low-level implementation unless upstream PRD or TDD already fixes it as a non-negotiable contract or constraint.

## 1.4 Explicit scope boundaries

Every slice must clearly state:
- what is in scope now
- what is out of scope now
- what must not break

This is mandatory.

## 1.5 Acceptance criteria notation — EARS primary, GWT auxiliary

The interface pair uses **EARS (Easy Approach to Requirements Syntax) as the default notation** for stating acceptance criteria and observable system behavior. EARS is concise, unambiguous, and AI-parseable; it expresses one requirement per sentence using a fixed grammar that prevents the ambiguity common in prose specs.

**The five EARS patterns** (use the one that fits the requirement type):

| Pattern | Form | When to use |
|---|---|---|
| Ubiquitous | "The system shall <function>" | Always-applicable system behavior with no trigger or precondition |
| Event-driven | "When <trigger>, the system shall <function>" | Behavior triggered by a discrete event |
| State-driven | "While <state>, the system shall <function>" | Behavior that holds during a specific operational state |
| Unwanted behavior | "If <trigger>, then the system shall <function>" | Defensive behavior in response to an unwanted condition |
| Optional | "Where <feature>, the system shall <function>" | Behavior conditional on an optional capability being present |

EARS sentences are the primary form in `acceptance.yaml` for `must_pass_scenarios.then` clauses, `non_regression_constraints` statements, `data_expectations.integrity_rule`, `permissions` rules, `observability_expectations` triggers, and `accessibility_expectations` requirements when Tier 1 is involved. See §3 field rules for per-field application.

**GWT (Given/When/Then) is auxiliary**, retained for two cases:
- **Business review presentation**: when a scenario is being walked through with a non-technical reviewer, GWT structure makes the precondition / trigger / outcome separation easier to follow in spoken or slide-form review
- **Multi-step scenarios**: when a scenario has non-trivial preconditions or sequenced when-clauses, GWT's explicit `given` / `when` / `then` fields capture the structure more cleanly than a single EARS sentence

The `must_pass_scenarios` YAML field retains its `given` / `when` / `then` structure for both reasons. The discipline is: **the `then` clause is written in EARS form** (Ubiquitous, Event-driven, State-driven, Unwanted behavior, or Optional pattern); the `given` and `when` clauses are plain business-observable language describing precondition and trigger. This combines EARS's clarity at the requirement level with GWT's scenario-structuring at the test-design level.

**Anti-pattern**: writing requirements in pure prose ("the user should be able to..."), which loses EARS's grammatical discipline and makes downstream test-case generation harder.

### 1.5.1 The `ears_pattern` field — mechanical pattern tagging

Because acceptance.yaml is AI-produced (by Hub Claude at TK-03) and AI-consumed (by CC main loop, subagents, Codex review, and future test-writer agents downstream), EARS pattern conformance cannot be enforced by prose discipline alone — the prose may drift from the intended pattern's syntactic skeleton without any structural signal of the drift. To make EARS pattern selection mechanically auditable and to give downstream AI consumers a deterministic classification handle, every acceptance.yaml entry that contains a behavior statement carries an explicit `ears_pattern` field tagging which of the five patterns applies.

**Field value set (closed enum)**: `ubiquitous`, `event-driven`, `state-driven`, `unwanted-behavior`, `optional`.

**Discipline**: the tagged pattern's syntactic skeleton **must** match the prose form of the behavior statement. The author (Hub Claude at TK-03) selects the pattern that fits the requirement type, writes the prose in that pattern's form, and tags the entry accordingly. Downstream consumers — TK-04 entry self-check, TK-07 / TK-08 test-case generation, TK-11 Codex code review, [TPL] Test Plan YAML Schema generation — read `ears_pattern` to classify the entry without re-parsing the prose.

**Fields requiring `ears_pattern`**: `must_pass_scenarios.then`, `non_regression_constraints.description`, `edge_cases.expected_behavior`, `permissions.rule`, `data_expectations.integrity_rule`, `observability_expectations.expected_content` (when the content is a behavior statement; not when it is purely structural shape), `accessibility_expectations.description` (when Tier 1 involved).

**Fields not requiring `ears_pattern`**: structural fields that do not contain behavior statements (e.g., `must_pass_scenarios.id`, `permissions.owning_tier`, `accessibility_expectations.verification` enum values) omit the field.

**Fallback rule**: when a `then` clause genuinely cannot be expressed in any of the five patterns (rare; typically when the outcome is a multi-step coordinated effect across multiple subsystems per the §3.3 GWT-only fallback), the entry uses `ears_pattern: gwt-fallback` and the prose explains why EARS could not be applied. `gwt-fallback` is the only out-of-enum value permitted and must be used sparingly.

Per-field application of `ears_pattern` is detailed in §3.

## 1.6 Conservative interpretation

When PRD or TDD is incomplete or ambiguous:
- preserve the ambiguity
- do not invent missing business or architecture facts
- do not extend scope because something feels obvious
- do not let convenience assumptions silently redefine the requirement

## 1.7 Stable terminology and IDs

Across the interface pair:
- use one stable `app_slug` from the active app's frozen-roster value (per CC substantive Claude Code Architecture Rules canonical, repository layout §Y — frozen app-slug roster); must match phase PRD §1.1 `App Slug` and phase TDD §1 `app_slug`; the file's `phase_number` field must match phase PRD §1.1 `Phase Number` and phase TDD §1 `phase_number`
- use one stable `feature_slug` from the source PRD and TDD file naming under `apps/{app-slug}/specs/prd/` and `apps/{app-slug}/specs/tdd/`
- use one stable `slice_id` consistent with `apps/{app-slug}/specs/slice-list/{feature-slug}.md`
- keep actor names stable across PRD / TDD / intent / acceptance
- keep object names stable
- keep status names stable
- preserve PRD and TDD identifiers where helpful for traceability

## 1.8 Approved-interface rule

An approved execution interface must be strong enough for downstream design and build.

Therefore:
- assumptions are allowed only when they do not materially redefine business or architecture logic
- unresolved business-rule or architecture-boundary ambiguity is not allowed to remain in an approved interface
- if a missing answer would change scope, eligibility, permission, state transition, calculation logic, release condition, non-regression boundary, or done definition, it must be resolved upstream in PRD or TDD before approval

## 1.9 Assumption discipline for baseline-owned values

Do not treat a missing value as safe merely because it is said to come from a security baseline, compliance baseline, platform default, Design System Governance, or other external control source.

A baseline-owned value may appear in `Assumptions` only when all of the following are true:
- the source baseline is already approved for current-slice use
- the value is already known or fixed enough for the current slice
- the value does not change current must-pass behavior
- the value does not change current non-regression boundary
- the value does not change done definition

External ownership alone does not make the point non-blocking.

## 1.10 Open-question discipline

`Open questions` are allowed in `intent.md` only under strict conditions:
- they must not change the approved business boundary (from PRD)
- they must not change the approved architecture boundary (from TDD)
- they must not redefine acceptance pass / fail logic
- they should normally be downstream validation-method questions
- each retained open question must be tagged as `[evidence-method]` or `[implementation-detail]`
- each retained open question must state why the business or architecture boundary remains stable despite the open point

Do not use `Open questions` to carry unresolved business-rule or architecture design into implementation.

## 1.11 Producer locations per field

The interface pair fields originate from different content pillars per [REF] Hub-CD-CC Architecture §5. The table below records the producer location for each field; this is the canonical mapping that TK-03 follows.

| Field (intent.md or acceptance.yaml) | Producer at TK-03 | Source content |
|---|---|---|
| intent.md `Business goal`, `User value`, `In scope`, `Out of scope`, `Actors`, `Trigger / entry points` | Hub Claude | Phase PRD + slice scoping in phase TDD `§4.{feature-slug}.Slice-List` |
| intent.md `Must not break` | Hub Claude | Phase PRD non-regression + phase TDD `§1.Tier-Responsibility-Mapping` + phase TDD `§4.{feature-slug}.API-Contracts` |
| intent.md `UX brief` (when Tier 1 involved) | Hub Claude | Hub-authored UX Design Spec instance at TK-02 Step 2.3 per [TPL] UX Design Spec (consumed at TK-03 as input from `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`) |
| intent.md `Slice tasks` | Hub Claude | Phase TDD `§4.{feature-slug}.Module-Decomposition` + intent.md scope; the task list orients CC implementation at slice start |
| intent.md `Assumptions`, `Open questions`, `References` | Hub Claude | Drawn from PRD + TDD + UX Design Spec when applicable |
| acceptance.yaml `must_pass_scenarios`, `non_regression_constraints`, `edge_cases`, `permissions`, `data_expectations`, `observability_expectations`, `out_of_scope`, `evidence_required` | Hub Claude | Phase PRD + phase TDD |
| acceptance.yaml `accessibility_expectations` (when Tier 1 involved) | Hub Claude | UX Design Spec instance §2.5 |
| traces_to_design_system path (when Tier 1 involved) | Hub Claude | Refers to the CC mirror path `specs/design-system.md`; the path is constant project-wide and is the path downstream CC consumers read at code time; Hub Claude records the path without reading the CC mirror file at TK-03 (Hub Claude's spec-time grounding flows through the CD-authored design files per DSG §13.3, not through the CC mirror path that appears in this field) |

**No CC-side authoring at TK-03**: CC does not author intent.md / acceptance.yaml / test-plan.yaml fields. The pair is finalized in Hub before transfer to CC. After transfer, CC may produce slice-level annotations (e.g., implementation notes) inside slice-execution artifacts (commit messages, M0 entry self-check log, etc.), but those are not modifications to the canonical interface pair.

## 1.12 Quality criteria for the produced pair

A complete `intent.md` + `acceptance.yaml` pair must satisfy three criteria simultaneously:

- **Narrow enough**: Claude Code can implement the slice without re-reading the full PRD or TDD
- **Stable enough**: the reviewer can approve the pair without deep code reading
- **Traceable enough**: any drift detected later can be traced back to the upstream PRD or TDD section that authorized the relevant scope

These criteria are review heuristics for accepting a draft pair, complementary to the field-level requirements in §2 and §3.

---

# 2. intent.md writing standard

## 2.1 Purpose

`intent.md` defines the approved execution boundary for one feature slice.

It should answer:
- why this slice exists
- who it is for
- what is included now
- what is excluded now
- what must not be broken
- what UX boundary applies (if Tier 1 is involved)
- what assumptions remain
- what downstream non-business non-architecture open points, if any, still exist

It is not:
- a technical architecture document (that is TDD)
- a test script (that is test-plan.yaml)
- a design system foundation (that is Design System Governance)
- a backlog decomposition
- a click-by-click UX walkthrough

## 2.2 Required structure

Use this structure unless a materially justified variation is needed:

```markdown
# <SLICE_ID> <SLICE_NAME>

## Business goal
## User value
## In scope
## Out of scope
## Actors
## Trigger / entry points
## Must not break
## UX brief            (required when Tier 1 is involved; omit otherwise)
## Slice tasks
## Assumptions
## Open questions
## References
```

## 2.3 Section rules

### Business goal
State the business or operating outcome this slice serves. Use 1 to 3 direct statements. Derive from PRD.

### User value
State the value by actor. Focus on experience, control, or operating outcome. Derive from PRD.

### In scope
List only the capabilities that belong to this slice now. Each line should describe one capability or one boundary point. Derive from PRD scope + TDD module decomposition.

### Out of scope
List what is intentionally excluded now. Make this explicit to prevent over-build.

### Actors
List real participating roles only. If permissions differ by role, keep that visible. Derive from PRD actors.

### Trigger / entry points
State how the actor reaches or starts the slice. Use business entry conditions rather than UI internals.

### Must not break
State stable existing behaviors, contracts, controls, or data expectations that cannot be harmed by delivery. This section is mandatory. Derive from:
- PRD non-regression expectations
- TDD API contract stability rules
- TDD tier responsibility mapping
- Design System Governance Tier C forbidden patterns (if Tier 1 involved)

### UX brief (when Tier 1 is involved)

**Applicability**: Required when any module affected by this slice is in Tier 1 (frontend). Omit entirely when the slice is purely Tier 2 or Tier 3.

**Source**: The Hub-authored UX Design Spec instance markdown for this feature, at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`. The instance is authored by Hub Claude at TK-02 Step 2.3 per [TPL] UX Design Spec, grounded in CD-produced design files (transferred from CD per [MECH] Cross-Tool Workflow Handoff §2.2) per [RULE] DSG §13.3, then committed to the CC monorepo before TK-03 begins. The UX brief here is a **slice-narrow extraction** from the feature-level UX Design Spec instance — it picks the screens, interactions, and call-outs that fall within this slice's modules.

**Producer**: Hub Claude at TK-03, consuming the Hub-authored UX Design Spec instance markdown as input (per §1.11 producer-locations table). Hub Claude does not invent UX content at TK-03; if the UX Design Spec instance is silent on a UX point the slice needs, surface as a clarification trigger and route back — either to TK-02 Step 2.3 for instance re-authoring (when the gap is content the existing CD design files can support) or further upstream to CD for additional design file coverage (when the gap requires new visual design work) per [TPL] Conversion Spec §5.4.

**Required sub-sections**:

```markdown
### Screens
- <screen-name-1>: <one-sentence purpose>; target role(s); HDC layout pattern per the UX Design Spec instance §2.2 (HDC layout pattern selection)
- <screen-name-2>: ...

### Key interactions
- <interaction-1>: <one-sentence description>; components from UX Design Spec instance §2.3 (Tier A / Tier B inventory references — CC verifies against DS instance at code time via SK-F)
- <interaction-2>: ...

### Empty, loading, error states
- For each screen, note any specific empty / loading / error state requirements beyond DSG §10 content style defaults

### Accessibility call-outs
- Any a11y considerations specific to this slice beyond DSG §6.1 baseline; reference the UX Design Spec instance §2.5 (Accessibility call-outs, slice-specific only) and lift only the items that apply to this slice's screens

### Internationalization call-outs
- Any i18n considerations specific to this slice beyond DSG §7 defaults; reference UX Design Spec instance §2.6; translation volume estimate if non-trivial

### New components or tokens (slice-local use only)
- If this slice uses a new Tier B component / token / icon / locale introduced by the UX Design Spec instance §2.4 (New components or tokens — additive update plan), note it here
- Reference the UX Design Spec instance §2.4 entry by asset name; do not embed the additive plan content (the plan flows through DSG §12 at the originating feature's merge-to-main milestone per [RULE] DSG §12.5)
```

**What the UX brief must not contain**:
- Pixel values, color hex codes, specific CSS properties (DSG owns tokens; DS instance carries values)
- Arco component internal specifications (DS instance §4 owns)
- General accessibility principles (DSG §6 owns the project stance)
- Mockups or screenshots (visual artifacts are CD-produced design files, transferred separately as visual reference per [MECH] Cross-Tool Workflow Handoff §3.1; not embedded here)
- Per-screen implementation detail (belongs in code)
- Restatement of UX Design Spec instance content beyond the slice-narrow extraction

### Slice tasks

**Purpose**: List the concrete implementation tasks that compose this slice's work plan. The task list orients CC at slice start (TK-04 entry self-check + TK-05 onward); a CC subagent or main loop reads these as a work-decomposition anchor before generating code.

**Producer**: Hub Claude at TK-03, derived from phase TDD `§4.{feature-slug}.Module-Decomposition` (module list) plus this intent.md's `In scope` (capability boundary) plus the UX Design Spec instance §2.1 when Tier 1 is involved (screens / interactions that need code).

**Granularity**: Each task is a small, named work item — typically the smallest unit that produces one logical commit's worth of code or one structurally-coherent change. A slice has on the order of 3–8 tasks; fewer than 3 suggests the slice may be too thin to warrant tasks listing (omit the section if no meaningful decomposition exists), and more than 8 suggests the slice itself may be too coarse — re-slice per the slice-size advisory in CC substantive CI/CD Milestone Policy canonical (slice-size advisory).

**Format**:

```markdown
- [task-id] <task description in imperative voice>
  - tier: <Tier 1 | Tier 2 | Tier 3>
  - module: <module-slug from TDD §4.{feature-slug}.Module-Decomposition, when applicable>
  - depends on: <task-id, task-id> (optional; for tasks that strictly follow another)
```

Example:
```markdown
- [T1] Add domain entity `TimeOffRequest` with state machine (Draft → Submitted → Approved → Withdrawn)
  - tier: Tier 3
  - module: time-off-request-domain
- [T2] Add BFF endpoint `POST /time-off-requests` that delegates to T1 entity via Pact pair `hr-cockpit-bff_time-off-request`
  - tier: Tier 2
  - module: time-off-bff
  - depends on: T1
- [T3] Add Tier 1 form screen using UX Design Spec instance §2.1 screen `request-create`; consume Tier B `HDCDateRangePicker` from DS instance §4 Tier B inventory
  - tier: Tier 1
  - module: time-off-ui
  - depends on: T2
```

**What slice tasks are not**:
- Not test cases (test cases live in `test-plan.yaml`)
- Not detailed function-level decomposition (that's CC's job at code time)
- Not sprint planning or estimation
- Not a milestone gating mechanism

**Trigger to promote slice tasks to an independent `[TPL]` artifact**: when slice complexity grows such that the task list exceeds ~1 week of work for one CC node, or when 8+ tasks routinely appear for slices in a phase, surface the trigger to the operator. The operator may then evaluate whether a standalone `[TPL] Slice Tasks Spec` is warranted (independent template, separate landing path, paired-update with TDD module decomposition). Until that trigger fires empirically, slice tasks remain embedded in intent.md.

### Assumptions
Use only for temporary working assumptions that do not materially redesign business or architecture logic.

An assumption that says a value will be supplied by an external baseline (Design System Governance, security baseline, compliance baseline) is allowed only when that baseline is already approved for current-slice use and the value does not change current acceptance or execution boundary.

If the assumption would change acceptance, non-regression boundary, or execution boundary, stop and resolve it upstream instead.

### Open questions
Keep this section empty by default in an approved interface.

Use it only for downstream validation-method or implementation-detail questions that do not change the business rule or architecture.

Write each retained question in this pattern:

```markdown
- [evidence-method] <question>
  Why business and architecture boundary remains stable: <one direct sentence>
```

or

```markdown
- [implementation-detail] <question>
  Why business and architecture boundary remains stable: <one direct sentence>
```

### References
Point back to upstream artifacts (all under the active app):
- PRD: `apps/{app-slug}/specs/prd/phase-{N}.md`
- TDD: `apps/{app-slug}/specs/tdd/phase-{N}.md`
- Slice list: `apps/{app-slug}/specs/slice-list/{feature-slug}.md`

When Tier 1 involved, also reference:
- DS instance CC mirror (project-level singleton, not under `apps/`): `specs/design-system.md`
- UX Design Spec instance for this feature (Hub-authored markdown at TK-02 Step 2.3 per [TPL] UX Design Spec; consumed at TK-03 and forwarded to CC at TK-04 entry): `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`

Reference stable section IDs or requirement IDs where possible. Do not reference the retired paths flagged in §0.2 — `specs/design-system-changes/{change-id}.md` (DS instance change drafts are CD-internal per [RULE] DSG §1.1 + §12) or `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` (replaced by the Hub-authored UX Design Spec instance markdown path above).

## 2.4 Abstraction boundary for intent.md

The following leakage patterns indicate intent.md is mixing levels. Each belongs in the declared source instead.

| Leakage pattern | Correct source |
|---|---|
| Database schema or table / column design | TDD or code |
| API payload shape specifics | phase TDD `§4.{feature-slug}.API-Contracts` or openapi.yaml |
| Component internal decomposition | phase TDD `§4.{feature-slug}.Module-Decomposition` |
| CI/CD pipeline detail | [MECH] CI/CD Milestone Policy |
| Test execution steps | test-plan.yaml |
| Implementation options not yet approved as architecture direction | TDD |
| Design tokens, component internal specs | Design System Governance |
| Repository path layout structure | CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1) |
| Branch topology, node assignment mechanics | [RULE] Workspace Topology |

## 2.5 Minimal template

```markdown
# <SLICE_ID> <SLICE_NAME>

## Business goal
- 

## User value
- 

## In scope
- 

## Out of scope
- 

## Actors
- 

## Trigger / entry points
- 

## Must not break
- 

## UX brief
### Screens
- 
### Key interactions
- 
### Empty, loading, error states
- 
### Accessibility call-outs
- 
### Internationalization call-outs
- 
### New components or tokens (slice-local use only)
- 

## Slice tasks
- [T1] 
  - tier: 
  - module: 
- [T2] 
  - tier: 
  - module: 
  - depends on: T1

## Assumptions
- 

## Open questions
- [evidence-method] 
  Why business and architecture boundary remains stable: 

## References
- apps/<app-slug>/specs/prd/phase-<N>.md
- apps/<app-slug>/specs/tdd/phase-<N>.md
- apps/<app-slug>/specs/slice-list/<feature-slug>.md
- specs/design-system.md   (when Tier 1 is involved; CC mirror of DS instance per [RULE] DSG §1.1)
- apps/<app-slug>/specs/ux-design-spec/<feature-slug>.md   (when Tier 1 is involved; Hub-authored UX Design Spec instance per [TPL] UX Design Spec)
```

---

# 3. acceptance.yaml writing standard

## 3.1 Purpose

`acceptance.yaml` converts the approved intent into a structured validation contract.

It must be:
- AI-consumable at runtime by A1 (whitebox test-writer), A2 (blackbox test-writer), A3 (adversarial-tester), A4 (domain-judge)
- Human-reviewable during transition period (first N=2 slices per [MECH] Development Track Workflow TK-03)
- Paired with test-plan.yaml (the test-design-level plan) without overlap

## 3.2 Required top-level fields

```yaml
app_slug:                    # string, matches active app from frozen roster (PRD §1.1, TDD §1)
slice_id:                    # string, matches intent.md filename
feature_slug:                # string, matches feature-slug
traces_to_prd:               # relative path, e.g., "apps/{app-slug}/specs/prd/phase-{N}.md"
traces_to_tdd:               # relative path, e.g., "apps/{app-slug}/specs/tdd/phase-{N}.md"
traces_to_intent:            # relative path, e.g., "apps/{app-slug}/specs/intent/{slice-id}.md"
traces_to_design_system:     # relative path (when Tier 1 is involved), "specs/design-system.md" (project-level singleton; the CC mirror path)
schema_version:              # string, e.g., "1.0"

must_pass_scenarios: []           # see §3.3
non_regression_constraints: []    # see §3.4
edge_cases: []                    # see §3.5
permissions: []                   # see §3.6
data_expectations: []             # see §3.7
observability_expectations: []    # see §3.8
accessibility_expectations: []    # see §3.9 (optional; only when slice-specific a11y considerations exist)
out_of_scope: []                  # see §3.10
evidence_required: []             # see §3.11
```

**Path discipline**: app-scoped paths (`traces_to_prd`, `traces_to_tdd`, `traces_to_intent`) all use the `apps/{app-slug}/` prefix; PRD and TDD paths use phase-level naming (`phase-{N}.md`); intent paths use slice-level naming (`{slice-id}.md`). The `traces_to_design_system` path is a project-level singleton and does not get an `apps/` prefix; it points to the **CC mirror** at `specs/design-system.md` because downstream CC consumers (A1/A2/A3 test writers, SK-F at code time) read the CC mirror as their authoritative DS reference. Hub holds no DS instance copy; Hub Claude's spec-time grounding flows through the CD-authored design files and does not appear in CC-side traceability fields. This split follows the repository layout in CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1).

**App slug + phase consistency**: `app_slug` must match the value populated in phase PRD §1.1 `App Slug` (per [TPL] PRD §0.7.1) and phase TDD §1 `app_slug` header field (per [TPL] TDD §1); `phase_number` must match phase PRD §1.1 `Phase Number` and phase TDD §1 `phase_number`. A mismatch is a conversion-time blocker, not a downstream cleanup item.

## 3.3 must_pass_scenarios field

Each entry is one must-pass scenario the slice must satisfy.

```yaml
must_pass_scenarios:
  - id:                    # string, e.g., "S1"
    name:                  # short descriptive name
    given:                 # precondition, business-level (plain business prose)
    when:                  # action or trigger (plain business prose)
    then:                  # observable outcome — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum: ubiquitous | event-driven | state-driven | unwanted-behavior | optional | gwt-fallback
    traces_to:             # optional: PRD FR id or TDD module
```

**Writing rules**:
- Each scenario is one end-to-end business result
- `given` and `when` are plain business-observable prose describing precondition and trigger; they need not follow EARS grammar
- `then` is the observable outcome and is written in **EARS form** per §1.5 — most commonly the **Event-driven** pattern ("When <when-condition>, the system shall <observable outcome>") when the scenario is single-trigger, or the **Ubiquitous** pattern ("The system shall <invariant>") when the outcome is an invariant after the trigger
- For scenarios verifying defensive behavior against unwanted conditions, use the **Unwanted-behavior** pattern in `then` ("If <unwanted-condition>, then the system shall <defensive-outcome>")
- `ears_pattern` is **required** per §1.5.1; tag the pattern the `then` prose uses; downstream consumers read this field to classify the scenario without re-parsing prose
- A scenario is not a test case; it is a business commitment the slice fulfills
- Test-plan.yaml derives one or more test cases per scenario; test case generation is informed by the `ears_pattern` tag (Event-driven → trigger-based test; Ubiquitous → invariant test; Unwanted-behavior → negative path test)

**EARS example** (Event-driven pattern in `then`):
```yaml
- id: S1
  name: Approver receives time-off request notification
  given: A direct report has saved a time-off request as Draft
  when: The direct report submits the request
  then: When a time-off request transitions from Draft to Submitted, the system shall notify the approver named in the requester's reporting line within 60 seconds.
  ears_pattern: event-driven
  traces_to: PRD FR-3.2
```

**Additional EARS examples**:

```yaml
# Ubiquitous (invariant)
- id: S2
  name: Audit trail always present
  given: Any time-off request state transition
  when: The state transition is persisted
  then: The system shall record an audit event capturing actor, before-state, after-state, and timestamp.
  ears_pattern: ubiquitous

# Unwanted-behavior (defensive)
- id: S3
  name: Approver attempts double-approval
  given: A time-off request is in Approved state
  when: The same approver attempts to approve it again
  then: If a time-off request is already in Approved state, then the system shall reject the second approval attempt and return error code 409.
  ears_pattern: unwanted-behavior
```

**GWT-only fallback**: if the outcome genuinely cannot be expressed in any of the five EARS patterns (rare — typically when the outcome is a multi-step coordinated effect across multiple subsystems), the `then` may use plain business prose, the entry uses `ears_pattern: gwt-fallback`, and the entry must include a short note explaining why EARS could not be applied. `gwt-fallback` should appear sparingly; frequent appearance indicates either over-coarse slicing (re-slice per CC substantive CI/CD Milestone Policy canonical (slice-size advisory)) or that the `then` is actually composable into multiple EARS sentences.

## 3.4 non_regression_constraints field

Behaviors or contracts outside the slice that must remain intact after delivery.

```yaml
non_regression_constraints:
  - id:                    # "NRC-1"
    description:           # what must not break — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum (see §3.3). For non-regression, ubiquitous and state-driven patterns are typical
    evidence_how:          # how non-regression is verified (references test-plan.yaml case types)
```

**Writing rules**:
- Non-regression constraints are typically **Ubiquitous** ("The system shall continue to <invariant>") or **State-driven** ("While <prior-feature> is enabled, the system shall <prior-behavior>")
- `ears_pattern` is required; tag accordingly

## 3.5 edge_cases field

Named edge cases that must be explicitly handled (not just discoverable through adversarial testing).

```yaml
edge_cases:
  - id:                    # "EDGE-1"
    description:           # what edge case (plain business prose; structural description of the case)
    expected_behavior:     # what should happen — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum (see §3.3). For edge cases, unwanted-behavior pattern is typical
```

**Writing rules**:
- `description` describes the edge case condition (e.g., "user submits with all required fields empty"); it is plain business prose and does not require EARS form
- `expected_behavior` describes the defensive behavior and **must** follow EARS form, typically **Unwanted-behavior** ("If <edge-condition>, then the system shall <defensive-outcome>")
- `ears_pattern` tags the pattern of `expected_behavior`

## 3.6 permissions field

Permission rules at the tier ownership level (consistent with [RULE] Claude Code Architecture Rules §3).

```yaml
permissions:
  - id:                    # "PERM-1"
    rule:                  # e.g., "Only approver role can initiate e-signature" — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum (see §3.3). For permissions, state-driven and unwanted-behavior patterns are typical
    owning_tier:           # "tier-3" | "tier-2" | "tier-1"
    verification:          # how the permission is verified (case type or scenario reference)
```

**Rule**: Permission rules that require data-level evaluation must be owned by Tier 3 per [RULE] Claude Code Architecture Rules §3.1. Functional permissions follow the case-by-case rule in §3.2.

**Writing rules**:
- Permission rules are typically **State-driven** ("While <role-context> holds, the system shall <permitted-action>") or **Unwanted-behavior** ("If <unauthorized-role> attempts <action>, then the system shall reject the action and return error code 403")
- `ears_pattern` is required; tag accordingly

## 3.7 data_expectations field

Data state expectations after the slice executes.

```yaml
data_expectations:
  - id:                    # "DATA-1"
    entity:                # which business entity
    expected_state:        # what state or value change (plain business prose; describes the data shape)
    integrity_rule:        # what invariant applies — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum (see §3.3). For data expectations, ubiquitous pattern is typical
```

**Writing rules**:
- `expected_state` describes the data state and is plain business prose (it does not require EARS form)
- `integrity_rule` describes the invariant the data must satisfy and **must** follow EARS form, typically **Ubiquitous** ("The system shall maintain <invariant>")
- `ears_pattern` tags the pattern of `integrity_rule`

## 3.8 observability_expectations field

Audit, log, metric, or status signals the slice must emit.

```yaml
observability_expectations:
  - id:                    # "OBS-1"
    type:                  # "audit_event" | "log" | "metric" | "status_transition"
    name:                  # signal name
    expected_content:      # shape or content summary; when this carries a behavior statement (e.g., "the audit event shall include actor, before-state, after-state, timestamp"), prose follows the tagged ears_pattern; when this is a pure structural shape declaration (e.g., a JSON field list), ears_pattern is omitted
    ears_pattern:          # conditional per §1.5.1; required when expected_content is a behavior statement; omit when expected_content is a pure structural shape declaration. Closed enum (see §3.3); ubiquitous pattern is typical when present
    triggering_scenario:   # must_pass_scenario id that triggers this signal
```

**Writing rules**:
- When `expected_content` is a behavior statement (e.g., "the system shall emit ..."), it must follow EARS form and `ears_pattern` is required
- When `expected_content` is a pure structural shape declaration (e.g., a list of JSON fields the audit event must carry), it is plain prose and `ears_pattern` is omitted
- The default is to express observability requirements as behavior statements with EARS form; the structural-shape variant is only for cases where the signal's content shape is the primary spec, not its emission behavior

## 3.9 accessibility_expectations field (optional; only when the slice has specific a11y considerations)

Applicable only when the slice has specific accessibility considerations beyond Arco component defaults; otherwise **omit entirely**. Per [RULE] DSG §6, HDC has no formal WCAG conformance target and no automated a11y gate; declaring `accessibility_expectations` is optional.

```yaml
accessibility_expectations:
  - id:                    # "A11Y-1"
    description:           # what specific a11y concern this entry addresses (e.g., "screen reader announces dynamic content updates", "keyboard-only operator can complete the wizard") — prose form, matches the syntactic skeleton of the tagged ears_pattern
    ears_pattern:          # required per §1.5.1; closed enum (see §3.3). For a11y, ubiquitous and event-driven patterns are typical
    related_recommendation: # optional; reference a DSG §6.1 recommendation if applicable
    verification:          # "automated" | "manual" | "both"; "automated" means the on-demand SK-W skill or eslint-plugin-jsx-a11y can detect it
```

**Writing rules**:
- Use this section only when the slice introduces a11y concerns that warrant explicit declaration (e.g., a custom Tier B component with non-standard interactions, a complex flow that needs keyboard-only verification)
- Do NOT use this section to restate generic recommendations that DSG §6.1 already covers — those apply to all slices and need no per-slice declaration
- `description` follows EARS form; typical patterns are **Ubiquitous** ("The system shall <a11y-invariant>") or **Event-driven** ("When <a11y-relevant-event>, the system shall <a11y-outcome>")
- `ears_pattern` is required; tag accordingly
- Verification entries do not establish a milestone gate; the a11y stance is "no formal gate" per DSG §6.2
- Optional: link to an on-demand SK-W audit if one was performed (`evidence.md` linkage)

## 3.10 out_of_scope field

Explicit exclusions from this slice (mirrors intent.md `Out of scope` but in machine-readable form for downstream consumption).

```yaml
out_of_scope:
  - description:           # what is excluded
    rationale:             # why excluded in this slice
```

## 3.11 evidence_required field

Evidence that must accompany this slice's M4 approval. The default set below is the starting point; add more based on slice specifics.

```yaml
evidence_required:
  - type:                  # see default set below
    description:           # one-sentence description
```

**Default set** (produced in Development Track Workflow TK-13):
- `test_results_summary`: aggregated pass/fail from all test types executed
- `traceability_summary`: slice-level traceability from PRD→TDD→intent→acceptance→test-plan→code→tests
- `compliance_audit`: compliance-checker final pass output
- `codex_review`: Codex plugin review output at `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md`
- `domain_judge_questions`: A4 generated business and UX perspective questions
- `accessibility_audit` (when Tier 1 is involved): SK-W accessibility audit output
- `operator_digest`: the M4 one-page operator-readable digest at `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md` per CC substantive CI/CD Milestone Policy canonical (operator-digest path §6.4)

**Slice-specific additions when materially needed**:
- `ui_flow_recording`
- `state_transition_examples`
- `error_case_examples`
- `permission_matrix_result`
- `audit_log_examples`

## 3.12 Abstraction boundary for acceptance.yaml

| Leakage pattern | Correct source |
|---|---|
| Specific test framework code | test-plan.yaml or test code |
| File paths to `apps/{app-slug}/src/**` or `apps/{app-slug}/tests/**` | test-plan.yaml (bias-firewall scoped) |
| Database table or column names | TDD or code |
| Design token values | Design System Governance |
| UI component internal specifications | Design System Governance or code |
| Repository path layout structure | CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1) |
| Branch topology, node assignment mechanics | [RULE] Workspace Topology |

**Structural-integrity note — `ears_pattern` field**: per §1.5.1, `ears_pattern` is a required field on every acceptance.yaml entry that contains a behavior statement (must_pass_scenarios.then, non_regression_constraints.description, edge_cases.expected_behavior, permissions.rule, data_expectations.integrity_rule, accessibility_expectations.description, and observability_expectations.expected_content when it is a behavior statement). Entries that do not contain behavior statements (e.g., pure structural shape declarations) omit the field. The TK-04 entry self-check at CC verifies that every entry expected to carry `ears_pattern` does carry one and that the value is in the closed enum (per [MECH] CI/CD Milestone Policy §2.1 mechanical integrity check).

---

# 4. Pairing rules and consistency

## 4.1 Pairing with PRD

- Every `must_pass_scenarios` entry should map to PRD FR or user value statement
- Every `permissions` entry should map to PRD permission section
- Every `non_regression_constraints` entry should map to PRD non-regression expectations
- `app_slug` in acceptance.yaml must match PRD §1.1 `App Slug` value

## 4.2 Pairing with TDD

- `app_slug`, `phase_number`, and `feature_slug` in acceptance.yaml must match phase TDD §1 header values
- `must_pass_scenarios` should not reference modules or tiers outside phase TDD `§4.{feature-slug}.Module-Decomposition`
- `permissions.owning_tier` must respect phase TDD `§1.Tier-Responsibility-Mapping`
- `data_expectations` should respect phase TDD `§4.{feature-slug}.Data-Model`
- intent.md `Slice tasks` must respect the TDD's module decomposition (tasks reference modules from `§4.{feature-slug}.Module-Decomposition`)
- Contract-test references for BFF-to-domain APIs follow the Pact pair convention `{app-slug}-bff_{domain-name}` per CC substantive Claude Code Architecture Rules canonical (Pact contract testing convention §Y.4)

## 4.3 Pairing with Design System Governance and UX Design Spec

- `accessibility_expectations` criteria reference [RULE] DSG §6 stance plus UX Design Spec instance §2.5 slice-specific items
- intent.md `UX brief.Screens` must match UX Design Spec instance §2.1 (Affected Tier 1 scope) for screens applicable to this slice
- intent.md `UX brief.Key interactions` references components from UX Design Spec instance §2.3
- intent.md `UX brief.New components or tokens` references UX Design Spec instance §2.4 additive update plan entries; the plan itself merges to DS instance at the originating feature's M4 → merge-to-main milestone per [RULE] DSG §12.5 (TK-12), with the reviewed DS markdown export syncing to the CC mirror at `specs/design-system.md` per DSG §12.3 + §12.7
- No reference is made to `specs/design-system-changes/{change-id}.md` (retired CC-side artifact) or `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` (retired UX bundle path; replaced by Hub-authored UX Design Spec instance markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`)

## 4.4 Pairing with test-plan.yaml

- Every `must_pass_scenarios` entry must have at least one `test_cases[].traces_to_scenario_id` match in test-plan.yaml
- Every `accessibility_expectations` entry must have at least one `test_type: accessibility` case in test-plan.yaml
- Every `permissions` entry must have at least one case verifying the rule

## 4.5 Update discipline

If PRD or TDD changes materially after this interface pair is approved:
- re-verify all `traces_to_*` references
- re-verify `must_not_break` items
- re-verify UX brief if the feature's UX Design Spec instance (Hub-authored at TK-02 Step 2.3 per [TPL] UX Design Spec) changed
- re-verify accessibility expectations if the UX Design Spec instance §2.5 or [RULE] DSG §6 stance changed
- re-verify slice tasks if the TDD module decomposition for this feature changed

---

# 5. Anti-drift red flags

Red flags that should trigger correction:

- Intent.md contains architecture design (module decomposition, API shapes) — belongs in TDD
- Intent.md contains test execution steps — belongs in test-plan.yaml
- Intent.md UX brief restates DSG / DS instance content — reference, don't duplicate
- Intent.md UX brief invents content not present in the upstream Hub-authored UX Design Spec instance — surface as clarification; route back to TK-02 Step 2.3 for instance re-authoring or further upstream to CD for additional design file coverage per [TPL] Conversion Spec §5.4
- Intent.md `Slice tasks` section omitted entirely when the slice has non-trivial implementation decomposition — add the section
- Intent.md `Slice tasks` exceeds 8 items routinely across multiple slices — surface the trigger to operator per §2.3 promotion criterion
- Acceptance.yaml `must_pass_scenarios.then` written in pure prose without EARS form when an EARS pattern would fit — rewrite per §3.3 EARS application rule
- Acceptance.yaml `must_pass_scenarios` references database columns — rewrite business-observable
- Acceptance.yaml `permissions.owning_tier` violates TDD tier mapping — correct or surface conflict
- Intent.md `Assumptions` section contains unresolved business-rule questions — resolve upstream
- Accessibility expectations omitted despite the feature's UX Design Spec instance §2.5 declaring slice-specific a11y concerns (a11y_expectations is optional per [RULE] DSG §6; carried only when §2.5 flags specific concerns)
- UX brief missing when slice has Tier 1 scope
- Slice produced without reading TDD (visible in `traces_to_tdd` being absent or stale)
- `traces_to_design_system` absent when Tier 1 scope present
- **`app_slug` or `phase_number` field absent or inconsistent with phase PRD §1.1 / phase TDD §1**
- **Feature-scoped paths missing `apps/{app-slug}/` prefix; or the DS instance CC mirror `specs/design-system.md` wrongly placed under `apps/`**
- **Reference to `specs/design-system-changes/{change-id}.md` anywhere in intent.md or acceptance.yaml — this legacy path is no longer at CC; replace with reference to the Hub-authored UX Design Spec instance §2.4 entry**
- **Reference to `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` anywhere in intent.md or acceptance.yaml — this legacy path is retired under the TK-02 Step 2.3 Hub-authoring flip; replace with the Hub-authored UX Design Spec instance markdown path `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`**
- **`traces_to_design_system` field value pointing anywhere other than the CC mirror path `specs/design-system.md`** — the traces field must point to the CC-side path that downstream CC consumers (A1/A2/A3 test writers, SK-F at code time) read. Hub holds no DS instance copy; Hub Claude's spec-time grounding flows through the CD-authored design files and does not appear in CC-side traceability fields.
- **`evidence_required` missing `operator_digest` (required default per CC substantive CI/CD Milestone Policy canonical (operator-digest path §6.4))**
- Reference to phase TDD `§4.{feature-slug}.UX-Strategy` — this sub-section has been removed from TDD; replace with reference to the Hub-authored UX Design Spec instance for the feature
