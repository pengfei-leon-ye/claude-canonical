# [TPL] PRD + TDD to Intent and Acceptance Conversion Specification

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable conversion standard for extracting one feature-slice-scoped `intent.md` and `acceptance.yaml` pair from the Y-chain upstream (canonical PRD + canonical TDD), with module-driven slicing and Design-System-Spec-aware UX brief generation
- **Source Category**: Cat 4
- **Management-System Role**: Specification-support template; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Supersedes**: `[TPL] PRD to Intent and Acceptance Conversion Specification` (single-upstream version). This source extends that one to the Y-chain dual-upstream model.
- **Boundary note**:
  - This source defines extraction logic, slicing rules, blocking rules, and clarification behavior for PRD+TDD-to-interface conversion
  - This source does not redefine the target-file structure or field semantics already owned by `[TPL] Intent and Acceptance Interface Writing Standard`
  - This source does not redefine test-plan.yaml schema; test-plan.yaml is a parallel output produced in the same TK-03 task, owned by `[TPL] Test Plan YAML Schema`
  - `evidence.md` is generated later, after implementation and validation; for its semantic description and its distinction from the milestone-level Test Evidence Report, see [MECH] CI/CD Milestone Policy §6
- **Relationship to [OS]**: Supports the Specify loop by converting dual-upstream product+architecture specification into lower-ambiguity execution inputs. Grounded in [OS] §0.1 project-level operating premises and [OS] §0.2 Cat 4 role anchor.
- **Relationship to [RULE] Workspace Topology**: Conversion executes in Hub Claude (per [REF] Hub-CD-CC Architecture §5.1 content pillar — spec artifact main body produced in Hub). The slice's `assigned_node` Claude Code is the downstream consumer of the conversion outputs starting at TK-04; the executing-workspace constraint for node-side TKs is owned by Workspace Topology §3.5 + §4.2 (feature-level node affinity)
- **Relationship to [MECH] Development Track Workflow**: This conversion is operationalized in TK-03 of the Development Track Workflow; the slicing rules in §2 presuppose the slice list produced in TK-02; the UX Design Spec instance consumed in §3.8 is Hub-authored at TK-02 Step 2.3 per [MECH] DTW TK-02 internal step decomposition; SK-F engagement is owned by [MECH] DTW TK-04 (CC-side, code-generation time)
- **Relationship to [RULE] Claude Code Architecture Rules**: Module-driven slicing in §2 anchors to TDD module decomposition, which must respect the three-tier architecture defined in that source; repository path layout (`apps/{app-slug}/specs/...`) is owned by Architecture Rules §Y.1
- **Relationship to [MECH] CI/CD Milestone Policy**: §6 owns `evidence.md` vs Test Evidence Report disambiguation
- **Relationship to [REF] Hub-CD-CC Architecture**: TK-03 (this conversion's operationalization) runs in Hub per §5.1 content pillar — the intent.md / acceptance.yaml main body is a "spec artifact main body" produced by Hub Claude. When Tier 1 is involved, the upstream UX Design Spec instance is Hub-authored at TK-02 Step 2.3 per §5.2 presentation pillar by Hub Claude reading CD-authored design files (transferred from CD per [MECH] Cross-Tool Workflow Handoff §2.2) grounded in the Hub DS mirror per [RULE] DSG §1.1 three-way distribution; the converter consumes the Hub-authored UX Design Spec instance markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` as the source for UX brief extraction.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2.2 (CD → operator → Hub) carries CD-authored design files into Hub as visual reference for TK-02 Step 2.3 UX Design Spec instance authoring when Tier 1 is involved; the Hub-authored instance markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` is the conversion's TK-03 UX brief source. §3.1 (Hub → operator → CC) carries the conversion outputs (intent.md / acceptance.yaml / test-plan.yaml) plus the Hub-authored UX Design Spec instance markdown and the CD design files (forwarded as visual reference) onward to CC at TK-04 entry per [MECH] DTW.
- **Relationship to adjacent [TPL] sources**:
  - Upstream sources: `[TPL] PRD / Prototype / MVP Spec Template` (PRD) and `[TPL] Technical Design Document Template` (TDD)
  - Upstream when Tier 1 involved: `[TPL] UX Design Spec` instance for the feature (Hub-authored at TK-02 Step 2.3 from CD design files + Hub DS mirror per `[TPL] UX Design Spec` §1; committed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` before TK-03 begins) — supplies the content categories that drive §3.8 UX brief extraction
  - Paired target: `[TPL] Intent and Acceptance Interface Writing Standard` (owns target file structure)
  - Parallel artifact: `[TPL] Test Plan YAML Schema` (parallel output in TK-03)
  - Project-level reference: `[RULE] Design System Governance` (governance baseline; the DS instance content lives in CD as SOT and is mirrored to both Hub and CC per DSG §1.1 three-way distribution; Hub uses its mirror for UX Design Spec instance authoring at TK-02 Step 2.3 and as a sanity reference at TK-03; component-existence enforcement against the live DS instance content happens at CC code-generation time via SK-F + CC mirror per DSG §12.5 lock-step)
- **Pairings I participate in**: P-08 (with [TPL] TDD §4.{feature-slug}.Slice-List), P-28 (with [TPL] TDD §4.{feature-slug}.Module-Decomposition + [TPL] UX Design Spec §2 content categories — the conversion's §3.8 UX brief extraction reads UX Design Spec instance per the paired-update relationship)

## How to use this source

Use this source when:
- a canonical PRD and TDD both exist
- the next step is to begin implementation for one feature slice
- the PRD+TDD pair is too broad or too mixed to serve as the only direct coding input
- the reviewer wants to approve execution boundaries and validation logic before coding starts
- ambiguity, conflict, slice size, or unresolved PRD/TDD items must be checked before extraction is finalized

Do not use this source as:
- a replacement for PRD (business truth) or TDD (engineering architecture truth)
- a redesign framework
- a way to silently settle unresolved business or architecture ambiguity
- a substitute for evidence generation after implementation
- a substitute for test-plan.yaml schema (parallel artifact)

---

# 0. Position and boundary

## 0.1 Canonical-source rule

PRD and TDD both remain upstream canonical sources of truth.

The extracted `intent.md` and `acceptance.yaml` are:
- downstream execution-layer compressions
- not independent product truths
- not permission to change PRD or TDD logic silently

## 0.2 Why Y-chain conversion exists

**PRD** is intentionally rich in business content: problem framing, scope and release cut, roles and scenarios, business rules, functional requirements, data and governance expectations, risks, decisions.

**TDD** is intentionally rich in engineering-architecture content: module decomposition, API contracts, data model implementation, tier mapping, testing strategy, NFR realization, decision record (as ADR index per [TPL] TDD §2.2.8). UX strategy is intentionally NOT carried in TDD; when a feature touches Tier 1, the per-feature UX coverage lives in a UX Design Spec instance Hub-authored at TK-02 Step 2.3 per `[TPL] UX Design Spec` from CD-authored design files + Hub DS mirror.

Together they provide **business truth × engineering-architecture truth** (with logical-architecture framing optionally upstream-resident in the PRD per [TPL] PRD Template §0.7). That makes them strong as upstream handoff artifacts, but too broad as the sole direct input for one implementation slice.

The purpose of Y-chain conversion is to:
- narrow the execution boundary
- reduce interpretation space at both business and architecture levels
- isolate one module-aligned feature slice
- make validation atomic
- produce a UX brief when Tier 1 is involved without re-reading all upstream
- support later evidence-based approval

**AI drift prevention angle**: Without Y-chain conversion, AI implementation agents would consume PRD + TDD directly. The PRD's business breadth and TDD's engineering breadth jointly create a wide interpretation surface where AI agents can silently choose interpretation paths that the operator did not consider or would have rejected. Conversion to slice-bounded Intent and Acceptance closes this interpretation surface to the specific slice being implemented, making AI interpretation choices auditable at the slice level rather than inferable only from final implementation behavior. This protection is the conversion's primary AI-collaboration value (per [OS] §0.1.2 quality goal and [OS] §0.2 Cat 4 senior-developer review role).

## 0.3 Conversion outputs

The conversion produces:
1. `apps/{app-slug}/specs/intent/{slice-id}.md`
2. `apps/{app-slug}/specs/acceptance/{slice-id}.yaml`

In TK-03 these two are produced alongside `apps/{app-slug}/specs/test-plan/{slice-id}.yaml`, but test-plan.yaml schema and conversion mechanics are owned by `[TPL] Test Plan YAML Schema`. This conversion specification scopes only to intent + acceptance.

`evidence.md` is generated later, after implementation and validation. For its semantic description and its distinction from the milestone-level Test Evidence Report, see [MECH] CI/CD Milestone Policy §6.

## 0.4 Default operating chain

```
canonical PRD + canonical TDD                 [Hub-produced in TK-01 / TK-02; landed at apps/{app-slug}/specs/...]
         |
         |  [if Tier 1 involved] Hub-authored UX Design Spec instance per [TPL] UX Design Spec
         |  is committed at apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md
         |  at TK-02 Step 2.3 (Hub Claude authoring from CD-authored design files +
         |  Hub DS mirror per [RULE] DSG §1.1) before TK-03 begins
         |
         v  (slice list produced in TK-02)
feature-slice selection
         |
         v  (TK-03: this conversion spec — runs in Hub; UX Design Spec instance markdown consumed when Tier 1 involved)
intent.md + acceptance.yaml (+ test-plan.yaml in parallel)
         |
         v  Hub-side cross-model review (operator's GPT-Claude consensus loop) — this serves as the de facto design freeze gate per [REF] Hub-CD-CC Architecture §5
         |
         v  artifacts transferred to CC via [MECH] Cross-Tool Workflow Handoff §3.1; CC enters at TK-04 (M0 entry self-check + first-commit)
frozen specs committed to feature branch on assigned_node
         |
         v  (TK-05..TK-12)
engineering design and implementation, evidence production
         |
         v  (TK-12: M4 gate)
human approval or reject
```

## 0.5 Boundary with the writing-standard source

Use this source to answer:
- whether PRD and TDD are both ready for safe conversion
- how to choose or split the feature slice using TDD module decomposition
- how to handle PRD-TDD cross-source ambiguity and conflict
- what clarification questions must be raised
- how to map PRD and TDD content into the interface pair
- how to derive UX brief from the Hub-authored UX Design Spec instance (committed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` at TK-02 Step 2.3 when Tier 1 is involved) and Design System Governance

Use `[TPL] Intent and Acceptance Interface Writing Standard` to answer:
- what sections and fields the interface pair must contain
- how those sections and fields should be written
- what makes the interface pair approval-ready

## 0.6 Execution context

This conversion executes in **Hub Claude**, not on the assigned_node Claude Code (per [REF] Hub-CD-CC Architecture §5.1 content pillar — spec artifact main body produced in Hub). The constraints below define how Hub-side execution preserves correctness:

1. **Hub-authored UX Design Spec instance as UX brief source** (when Tier 1 involved): the UX Design Spec instance for the feature is Hub-authored at TK-02 Step 2.3 (per [MECH] Development Track Workflow TK-02 internal step decomposition) by Hub Claude reading CD-authored design files (transferred from CD per [MECH] Cross-Tool Workflow Handoff §2.2) grounded in the Hub DS mirror per [RULE] DSG §1.1 three-way distribution. The instance is committed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` *before* TK-03 begins. Hub Claude consumes the committed instance markdown as the source for UX brief extraction in §3.8. The Hub mirror version Hub used at TK-02 Step 2.3 authoring time is recorded in the UX Design Spec instance header; CC verifies its own mirror version is in lock-step at TK-04 entry per DSG §12.5. (Note: the retired `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` path is no longer in scope; the Hub-authored instance markdown supersedes the prior CD-authored bundle structure.)

2. **No SK-F live consultation at TK-03**: SK-F (`hdc-arco-enterprise-ui` skill) is a Claude Code skill that loads at CC session start and is invoked at code-generation time (TK-04 onward, when substantive code writing begins per [MECH] DTW TK-04 description). SK-F is **not** consulted during this conversion. Component-existence verification against the live DS instance happens at CC code generation, not at Hub TK-03. The TK-03 converter's contract with the UX Design Spec instance is: "if a component is named in the UX brief, Hub at TK-02 Step 2.3 verified it against the Hub mirror's component inventory; CC will verify at code time against the CC mirror and surface any drift as a TK-04+ findings."

3. **No SK-W live consultation at TK-03**: SK-W (`hdc-wcag-accessibility-checker` skill) is on-demand only and not bound to TK-03 timing. When the UX Design Spec instance §2.5 declares slice-specific a11y considerations, the converter writes them through to acceptance.yaml `accessibility_expectations` per §4.7 below; operator triggers SK-W audit on-demand later if warranted (per [RULE] DSG §6.3).

4. **Cross-model review at Hub as design-freeze gate**: After conversion outputs are drafted, the operator's GPT-Claude consensus review (manual loop with ChatGPT against Hub Claude's draft) serves as the design-freeze gate. The cross-model review is conducted in Hub; only after consensus does the operator transfer artifacts to CC per [MECH] Cross-Tool Workflow Handoff §3.1.

5. **No silent CC mirror inspection**: Hub Claude does not read CC mirror file content during TK-03; the CC mirror is the CC-side artifact. TK-03 in Hub draws on PRD + TDD + Hub-authored UX Design Spec instance markdown (when applicable) as its inputs. Hub's own DS mirror at `hdc_ref_design-system.md` is consulted as needed for sanity references but is not the SOT; the SOT is CD per [RULE] DSG §1.1. Mirror inspection at CC happens at code time via SK-F.

**Operator interaction during conversion**: The conversion is Hub-deterministic per this source's extraction rules. The operator engages with Hub Claude during TK-03 to drive the cross-model review loop. The conversion does not retroactively modify upstream PRD or TDD; ambiguities surface as clarifications per §5.

## 0.7 Unit_type applicability

This conversion specification is authored against the `feature` unit slice extraction path (the dominant case: 1+ slices per feature, module-driven decomposition from phase TDD `§4.{feature-slug}.Module-Decomposition`).

For the **`walking_skeleton` unit** (Phase 1 only, exactly one slice per [MECH] Development Track Workflow §4.0.2), the spec applies with the following per-unit-type substitutions:

| Section reference | `feature` unit reads | `walking_skeleton` unit reads |
|---|---|---|
| Module decomposition source | `§4.{feature-slug}.Module-Decomposition` | `§3.Scope-And-End-To-End-Coverage` (tier coverage + persistence path + external integration) |
| `assigned_node` source | `§4.{feature-slug}.Header.assigned_node` | `§3.Walking-Skeleton-Header.assigned_node` |
| Feature integration test plan input | `feature-{feature-slug}.yaml` | not applicable (no cross-slice flow within the unit; the unit has exactly one slice) |
| Per-feature slice-list input | `slice-list/{feature-slug}.md` | not applicable (single-slice unit; no slice-list file produced at TK-02) |
| `feature_slug` slice metadata field | the active feature's slug from PRD §7.1 | `walking-skeleton` (degenerate value matching `unit_id`; this preserves the `{feature-slug}-{slice-seq}-{slice-name}` slice-id template by treating `walking-skeleton` as a single-slice "feature" container) |
| `slice_id` value | `{feature-slug}-{slice-seq}-{slice-name}` per Workflow §3.3 | `walking-skeleton` (matching `unit_id` per [TPL] TDD §3.Walking-Skeleton-Header) |
| UX brief source (when Tier 1 involved) | Hub-authored UX Design Spec instance per `[TPL] UX Design Spec` (authored at TK-02 Step 2.3 from CD design files + Hub DS mirror; committed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` before TK-03) | `§3.Scope-And-End-To-End-Coverage` Tier 1 row — Phase 1 walking-skeleton typically requires only minimal Tier 1 surface; full Tier 1 UX coverage belongs to Phase 1 feature units (where a UX Design Spec instance is Hub-authored per feature) |

When the conversion runs against a `walking_skeleton` unit, the slice-split rules in §2.3 do not fire (one slice per unit by ontology); §2.2 module-driven slicing reduces to "the single slice covers the tier coverage declared in `§3.Scope-And-End-To-End-Coverage`."

The `app_integration` unit does **not** run TK-03 (per [MECH] Development Track Workflow §4.0.4 — entry point is TK-08, with phase test plan master + feature integration test plans as the unit's authoring source). `app_integration` is therefore out of scope of this conversion specification entirely.

---

# 1. Preconditions for conversion

Before conversion begins, all of the following must be explicit:

**Phase resolution**: identify the target `phase_number` for this conversion. The active phase governs which paired phase PRD and phase TDD are loaded as conversion sources. A conversion task spans one phase only; cross-phase slice batches must be scheduled separately, one phase at a time.

**Upstream readiness**:
- the source paired phase PRD filename and version/commit (at `apps/{app-slug}/specs/prd/phase-{N}.md`)
- the source paired phase TDD filename and version/commit (at `apps/{app-slug}/specs/tdd/phase-{N}.md`)
- the TDD level (Full / Feature / Lite)
- whether any unresolved PRD ambiguity blocks safe conversion
- whether any unresolved TDD ambiguity blocks safe conversion
- whether PRD and TDD are mutually consistent (no contradictions)

**Feature anchor readiness within the phase** (per [TPL] PRD §0.7.1 + [TPL] TDD §1):
- `app_slug` populated and identical in phase PRD §1.1 and phase TDD §1 header; `phase_number` populated and identical in phase PRD §1.1 and phase TDD §1 header
- `assigned_node` populated in the unit-scope-correct location of the phase TDD: for `feature` units, `§4.{feature-slug}.Header.assigned_node`; for the `walking_skeleton` unit, `§3.Walking-Skeleton-Header.assigned_node`. The phase TDD itself is application/phase-scoped and does **not** carry a top-level `assigned_node` field — node assignment is per work unit, not per phase (per [TPL] TDD Template §0.6 and [RULE] Workspace Topology §6). Value comes from [RULE] Workspace Topology §2.1 logical node catalog
- Conversion is being executed in Hub Claude (the `assigned_node` is the downstream CC consumer starting at TK-04, not the executor of this conversion)

**Slice readiness**:
- the target slice ID for a feature in the active phase, from `apps/{app-slug}/specs/slice-list/{feature-slug}.md`
- whether the slice is truly one-main-worktree-one-PR-sized
- whether the slice respects the slice-size advisory ([MECH] CI/CD Milestone Policy §2.7); oversize slices must carry rationale from phase TDD `§4.{feature-slug}.Module-Decomposition`

**Design system readiness** (if Tier 1 involved):
- Current DS instance version known across all three workspaces (CD = SOT; Hub mirror at `hdc_ref_design-system.md` per [RULE] DSG §1.1; CC mirror at `specs/design-system.md` per same). Hub mirror and CC mirror must be in lock-step per DSG §12.5. The UX Design Spec instance header records the Hub mirror version used at TK-02 Step 2.3 authoring time, anchoring traceability
- Hub-authored UX Design Spec instance for this feature exists at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`, authored at TK-02 Step 2.3 from CD-authored design files (transferred per [MECH] Cross-Tool Workflow Handoff §2.2) grounded in the Hub DS mirror. The operator has applied the two reviewer checklists in `[TPL] UX Design Spec` §3 (§3.1 design file quality check at TK-02 Step 2.2 conclusion; §3.2 instance authoring quality check at TK-02 Step 2.3 conclusion) and signed off both before TK-03 begins
- The UX Design Spec instance §2.4 (when present) declares the additive update plan for any new components or tokens this feature introduces; the update will merge to the DS instance at the originating feature's M4 → merge-to-main milestone per [RULE] DSG §12.5 (TK-12)
- SK-F live consultation is NOT required at TK-03 time (per §0.6 item 2); SK-F operates at CC code-generation time only

If any of these are unclear, do not start extraction. Clarify upstream first.

---

# 2. Feature-slice selection rules

## 2.1 What counts as one feature slice

A feature slice is fundamentally an **engineering execution unit** — one M0 → M5 evidence chain landed as one PR — constrained by business coherence rather than driven by it. The five conditions below combine engineering primary criteria (4 module-aligned, 5 one-PR sized) with business sanity constraints (1 single objective, 2 closed scenario, 3 coherent rule boundary). When the engineering and business signals conflict, §2.2 gives precedence to engineering decomposition.

A good feature slice normally satisfies all five conditions:

1. **Single main business objective** — one coherent outcome statement traceable to PRD
2. **Closed-enough scenario set** — the slice covers a minimum closed flow; partial flows requiring future slices to work are discouraged unless the upstream explicitly staggered them
3. **Coherent rule boundary** — business rules invoked by this slice do not span disparate policy domains
4. **Module-aligned** — the slice maps onto one module or a small coherent group of adjacent modules from phase TDD `§4.{feature-slug}.Module-Decomposition`
5. **One-PR sized** — the slice can be implemented in one main worktree and merged as one PR; estimated scope respects the slice-size advisory in [MECH] CI/CD Milestone Policy §2.7 (≤10 src files, ≤500 LOC) or carries explicit oversize rationale from phase TDD `§4.{feature-slug}.Module-Decomposition`

## 2.2 Module-driven slicing (primary rule)

The primary basis for slice boundaries is **TDD module decomposition**, not PRD functional requirement grouping.

Why:
- PRD FRs may span multiple modules if the business flow crosses architecture boundaries
- Module-driven slicing keeps the slice implementable within one tier or a small number of related modules
- It aligns directly with the `owning_tier` fields in acceptance.yaml `permissions`

Procedure:
1. Open `apps/{app-slug}/specs/slice-list/{feature-slug}.md` produced in TK-02
2. Pick the target slice (by ID)
3. Identify which phase TDD `§4.{feature-slug}.Module-Decomposition` modules the slice covers
4. If any module is in `packages/domain/{domain-name}/`, identify which Tier 3 capability the slice consumes (per phase TDD `§4.{feature-slug}.Module-Decomposition` domain references) and confirm Pact pair `{app-slug}-bff_{domain-name}` is identified
5. Confirm the modules are **adjacent** (same tier, or tier-to-tier pairs with a direct call relationship)
6. Flag if the slice spans more than 3 modules across more than 2 tiers — this is a slicing-too-large signal

## 2.3 When a slice must be split further

Split the slice when any of the following are true:

- Module count exceeds 3 in the slice
- Tier count exceeds 2 in the slice (with rare exceptions for a single-file cross-tier change)
- Two distinct business objectives emerged during drafting
- Two distinct permission rule sets are required
- The slice has more than one critical non-regression concern
- The UX brief (if Tier 1 involved) would list more than 3-4 screens
- Estimated scope exceeds slice-size advisory ([MECH] CI/CD Milestone Policy §2.7) without phase TDD `§4.{feature-slug}.Module-Decomposition` oversize rationale

When splitting, propose new slice IDs following the pattern `{feature-slug}-{new-seq}-{new-slice-name}` and update `apps/{app-slug}/specs/slice-list/{feature-slug}.md`.

## 2.4 Slice metadata

Each extracted slice must record the following metadata. The field set is paired with [TPL] phase TDD `§4.{feature-slug}.Slice-List` slice-list per-slice entry — when this list changes, phase TDD `§4.{feature-slug}.Slice-List` must be re-verified, and vice versa.

- `app_slug` (must match the phase's `app_slug` from PRD §1.1 and phase TDD §1 header)
- `assigned_node` (sourced per unit type: `feature` units read `§4.{feature-slug}.Header.assigned_node`; `walking_skeleton` reads `§3.Walking-Skeleton-Header.assigned_node`; the phase TDD itself does not carry a top-level `assigned_node` field — see §0.7 below)
- `slice_id`
- `feature_slug`
- `tdd_modules_covered`: list of modules from phase TDD `§4.{feature-slug}.Module-Decomposition`
- `tiers_covered`: subset of {tier-1, tier-2, tier-3}
- `tier_1_involved`: boolean; triggers UX brief and accessibility expectations
- `domains_consumed`: list of `{domain-name}` from `packages/domain/` if any; supports Pact pair `{app-slug}-bff_{domain-name}` scoping per [RULE] Architecture Rules §Y.4
- `estimated_scope`: file count + net LOC estimate per slice-size advisory ([MECH] CI/CD Milestone Policy §2.7); flag oversize if applicable

---

# 3. Extraction logic: from PRD + TDD to intent.md

## 3.1 Business goal extraction

Source: PRD outcome statements.

Rule: Pick the 1-3 outcome statements in PRD most directly tied to this slice's module scope. Do not lift an outcome that spans multiple slices.

## 3.2 User value extraction

Source: PRD user value statements per actor.

Rule: Restrict to actors whose scenarios are exercised by modules in `tdd_modules_covered`.

## 3.3 In scope extraction

Source: intersection of PRD functional requirements + TDD module responsibilities.

Rule:
- A capability appears in `In scope` only if (a) a PRD FR requires it AND (b) a TDD module in this slice implements it
- If a PRD FR has no corresponding TDD module, that FR cannot be in this slice's scope — it either belongs to another slice or indicates a TDD gap to be raised
- If a TDD module responsibility has no corresponding PRD FR, surface this as a clarification question

## 3.4 Out of scope extraction

Source: PRD `Out of scope` + explicit non-current-release content + items deferred to other slices.

Rule: If content appears in another slice's scope, mark it `Out of scope` here with reference.

## 3.5 Actors extraction

Source: PRD actor list filtered by TDD module access.

Rule: List only actors exercised by this slice's modules.

## 3.6 Trigger / entry points extraction

Source: PRD business entry conditions.

Rule: Business-level only. Do not describe UI element triggers.

## 3.7 Must not break extraction

Source: composite from PRD non-regression expectations + TDD API contract stability rules + TDD tier boundaries + Design System Governance Tier C forbidden patterns (if Tier 1 involved).

Rule:
- Every PRD non-regression expectation touching this slice's modules must appear
- Every TDD API contract involving this slice's modules must have its stability requirement listed; for BFF-to-domain APIs, the Pact pair `{app-slug}-bff_{domain-name}` is the stability anchor
- Tier boundary violations (e.g., "must not implement business rules in Tier 1") appear when the slice has Tier 1 modules and uses modules interacting across tiers

## 3.8 UX brief extraction (when Tier 1 involved)

Source: Hub-authored UX Design Spec instance per `[TPL] UX Design Spec` (committed at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` at TK-02 Step 2.3 per §0.6) + Design System Governance topic-level rules + PRD user flow.

**No SK-F live consultation at TK-03**: The converter does not query SK-F during conversion (SK-F is a CC-side skill — see §0.6 item 2). Component-existence verification, layout-pattern catalog matching, and token reference validation against the live DS instance are performed at CC code-generation time (TK-04 onward, when substantive code writing begins per [MECH] DTW TK-04), not at Hub TK-03. TK-02 Step 2.3's Hub-side authoring discipline is the upstream guarantee that the UX brief extraction is grounded in real DS instance content: Hub Claude authored the UX Design Spec instance from CD design files + Hub DS mirror per `[TPL] UX Design Spec` §1, and the operator ran the two reviewer checklists in `[TPL] UX Design Spec` §3 (design file quality check + instance authoring quality check) before TK-03 begins.

**Field rules**:

- **Screens**: Pick the subset of the UX Design Spec instance §2.1 (Affected Tier 1 scope) screens that fall within this slice's modules. One sentence purpose per screen. Layout pattern assignment from UX Design Spec instance §2.2 (HDC layout pattern selection).
- **Key interactions**: Pick the interactions specific to this slice's scenarios. Components from UX Design Spec instance §2.3 (Tier A or Tier B as already declared in the instance, grounded in the Hub mirror at authoring time). Do not restate Design System Governance component specs — reference only.
- **Empty / loading / error states**: Only note deviations from DS instance defaults (per [RULE] DSG §10 content style governance). If DSG defaults suffice, write "Per Design System Governance defaults."
- **Accessibility call-outs**: Lift from UX Design Spec instance §2.5 (Accessibility call-outs, slice-specific only). Do not restate [RULE] DSG §6.1 baseline content.
- **Internationalization call-outs**: Only when the slice has specific i18n load beyond DSG §7 defaults. Lift from UX Design Spec instance §2.6 (Internationalization and RTL call-outs). Translation volume estimate if non-trivial.
- **New components or tokens (slice-local use only)**: Only if UX Design Spec instance §2.4 (New components or tokens) declared a new asset that this slice uses. Reference the additive update plan in §2.4; do not embed the plan content in intent.md. The plan itself flows to the DS instance via [RULE] DSG §12 at the originating feature's M4 → merge-to-main milestone (TK-12). Otherwise write "None."

**If the UX Design Spec instance §2.x is silent on a UX point the slice needs**: Treat as a clarification trigger (see §5.4 below). Do not invent UX content in Hub Claude. Raise to operator; operator routes back to CD for additional design file coverage and then Hub re-authors the instance section, if warranted.

## 3.9 Assumptions extraction

Source: PRD and TDD approved working assumptions.

Rule: §1.8 of Writing Standard applies. An assumption may be lifted into intent.md only when it does not alter current-slice business behavior, non-regression boundary, or done definition.

## 3.10 Open questions extraction

Source: downstream validation-method or implementation-detail questions.

Rule: Do not lift PRD `Open questions` or TDD `Open questions` of business-rule or architecture type into intent.md. Such questions block conversion and must be resolved upstream.

The only open questions that may remain in intent.md are tagged `[evidence-method]` or `[implementation-detail]` per Writing Standard §1.9.

## 3.11 References extraction

Reference the exact PRD and TDD filenames and slice list (all under `apps/{app-slug}/specs/`):

- PRD: `apps/{app-slug}/specs/prd/phase-{N}.md`
- TDD: `apps/{app-slug}/specs/tdd/phase-{N}.md`
- Slice list: `apps/{app-slug}/specs/slice-list/{feature-slug}.md`

When Tier 1 involved, also reference:

- The DS instance — Hub mirror at `hdc_ref_design-system.md` for Hub-side reference (read by Hub at TK-02 Step 2.3 UX Design Spec instance authoring); CC mirror at `specs/design-system.md` for CC-side reference (read by CC at TK-04+ code generation via SK-F); both mirrors must be in lock-step per [RULE] DSG §12.5 (the CD instance is the SOT for both)
- The Hub-authored UX Design Spec instance for this feature at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` (authored at TK-02 Step 2.3 from CD-authored design files + Hub DS mirror per [TPL] UX Design Spec §1; CD design files in their native format are forwarded to CC alongside the instance markdown at TK-04 entry per [MECH] Cross-Tool Workflow Handoff §3.1 as visual reference)

The DS instance CC mirror path `specs/design-system.md` is not under `apps/` because the design system is project-level (one instance shared across all apps). The Hub mirror `hdc_ref_design-system.md` similarly lives at the Hub PK root, not under `apps/`. The retired `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` path is no longer in scope.

---

# 4. Extraction logic: from PRD + TDD to acceptance.yaml

## 4.1 must_pass_scenarios

Source: PRD scenarios filtered by slice modules + TDD module responsibilities.

Rule:
- One scenario per distinct business outcome
- Each scenario's `given / when / then` uses business-observable language
- `traces_to` field references PRD FR id or TDD module

## 4.2 non_regression_constraints

Source: PRD non-regression expectations + TDD stability rules.

Rule: Every constraint has an `evidence_how` pointing to the test technique (contract test, e2e scenario, permission test, etc.) that will verify it. For BFF-to-domain stability, the contract test references the Pact pair `{app-slug}-bff_{domain-name}` per [RULE] Architecture Rules §Y.4.

## 4.3 edge_cases

Source: PRD edge cases + TDD data model boundary conditions.

Rule: Name the edge case, state the expected behavior. Do not confuse edge cases with adversarial cases (the latter is A3's domain in TK-11).

## 4.4 permissions

Source: PRD permission section + phase TDD `§1.Tier-Responsibility-Mapping` tier responsibility mapping + [RULE] Claude Code Architecture Rules §3.

Rule:
- `owning_tier` must respect phase TDD `§1.Tier-Responsibility-Mapping` assignment
- Data permissions must own at Tier 3 per [RULE] Claude Code Architecture Rules §3.1
- Functional permissions follow the case-by-case rule in [RULE] Claude Code Architecture Rules §3.2; the choice must match phase TDD `§1.Tier-Responsibility-Mapping`

## 4.5 data_expectations

Source: PRD data rules + phase TDD `§4.{feature-slug}.Data-Model` data model.

Rule: `integrity_rule` restates TDD invariants at a level observable by test cases. Do not reference tables or columns.

## 4.6 observability_expectations

Source: PRD audit/log requirements + phase TDD `§2.NFR-Baselines` observability NFR.

Rule: Each expectation must trace to a must_pass_scenario that triggers the signal.

## 4.7 accessibility_expectations (when Tier 1 involved)

Source: UX Design Spec instance §2.5 (Accessibility call-outs, slice-specific only) + [RULE] DSG §6 stance.

Rule:
- Per [RULE] DSG §6, HDC has no formal WCAG conformance target; this section is **optional** and used only when the slice has specific a11y considerations beyond Arco component defaults
- When the UX Design Spec instance §2.5 declares feature-specific a11y call-outs, convert each into an `accessibility_expectations` entry; otherwise omit the section entirely
- Each entry includes `verification: automated | manual | both`; "automated" maps to either `eslint-plugin-jsx-a11y` (warn-level lint, per CC substantive Code Quality Rule Set canonical §1.2) or to an on-demand SK-W audit; "manual" means an operator spot-check at M4
- No entry creates a milestone gate; the project a11y stance is "no formal gate"

## 4.8 out_of_scope

Source: intent.md `Out of scope` restated in machine-readable form.

Rule: One entry per excluded item with rationale.

## 4.9 evidence_required

Source: default set from Writing Standard §3.11 plus slice-specific additions.

Rule: `accessibility_audit` must be in the list when Tier 1 is involved (produced by SK-W in TK-10 per [MECH] CI/CD Milestone Policy §2.5 M3 Pre-Release evidence table). The default set includes `operator_digest` (the M4 one-page operator-readable digest at `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md` per [MECH] CI/CD Milestone Policy §6.4).

---

# 5. Cross-source clarification protocol

When PRD and TDD disagree or one is silent on a point material to the slice:

## 5.1 PRD silent, TDD has content

Example: TDD module decomposition implies a module responsibility that has no matching PRD FR.

Action: Raise a clarification. This is a PRD gap, not a TDD authority override. Do not insert the TDD-implied behavior into `In scope` without PRD confirmation.

## 5.2 TDD silent, PRD has content

Example: PRD declares an FR but no TDD module covers it within this slice's modules.

Action: Either the FR belongs to a different slice, or the TDD missed a module. Raise a clarification to your TDD author.

## 5.3 PRD and TDD contradict

Example: PRD says "approver role initiates" but phase TDD `§1.Tier-Responsibility-Mapping` places the permission decision in Tier 1 (a tier-placement violation).

Action: Do not silently pick one. Record the conflict explicitly. Either fix TDD (typical case) or confirm that PRD is outdated (rare). Block the slice's conversion until resolved.

## 5.4 Design System Governance silent on a UX point

Example: the UX Design Spec instance §2.2 references a layout pattern that is not in DSG §11 / DS instance pattern catalog; or the UX Design Spec instance §2.3 references a component not in DS instance §4 inventory without an §2.4 additive update plan.

Action: Raise to the spec owner (the operator). Either add the missing asset to the DS instance via [RULE] DSG §12 additive update path (authored in CD), or revise the UX Design Spec instance to use a cataloged asset (Hub re-authors the relevant §2.x section at TK-02 Step 2.3, drawing from updated CD design files). Hub Claude cannot extend the DS inventory nor SK-F-validate a component reference at TK-03; the gap routes back to CD for resolution.

---

# 6. Fact priority and conflict-handling rules

## 6.1 Fact priority (within PRD)

When multiple PRD sections appear to differ, interpret them in this order unless the PRD explicitly says otherwise:

1. current release or MVP boundary
2. explicit business rules
3. detailed functional design
4. acceptance and traceability
5. process notes and narrative explanation
6. background narrative

## 6.2 Fact priority (within TDD)

When multiple TDD sections appear to differ:

1. Phase-level architecture overview (`§1.Architecture-Overview`) top-line decisions
2. Phase-level tier responsibility mapping (`§1.Tier-Responsibility-Mapping`)
3. Per-feature module decomposition (`§4.{feature-slug}.Module-Decomposition`)
4. Per-feature API contracts (`§4.{feature-slug}.API-Contracts`)
5. Per-feature data model (`§4.{feature-slug}.Data-Model`)
6. Phase-level cross-feature concerns (`§2.*` baselines)
7. Other sections

## 6.3 Cross-source priority (PRD vs TDD)

When PRD and TDD disagree:

- **Business rule content**: PRD wins
- **Architecture and tier placement**: TDD wins
- **Scope boundary**: PRD wins (TDD scope must align with PRD scope)
- **API contract specifics**: TDD wins
- **User experience flow**: PRD wins for the flow; the Hub-authored UX Design Spec instance (per `[TPL] UX Design Spec`, drawing from CD-authored design files + Hub DS mirror at TK-02 Step 2.3) wins for screen / layout pattern / component realization
- **Accessibility targets**: [RULE] Design System Governance (project-level) wins over any feature-level override unless the UX Design Spec instance §2.5 explicitly justifies exceeding the baseline

If a conflict cannot be resolved by this priority table, raise clarification.

## 6.4 Open-question rule

A PRD or TDD open question must never be converted into a must-pass requirement without explicit approval.

## 6.5 Recommendation-is-not-decision rule

If a PRD or TDD `Decisions Needed` or similar section contains options, recommendation text, or placeholders but does not state that the choice is approved, the converter must not treat the recommendation as already settled.

## 6.6 Conflict rule

If two upstream sections conflict:
- do not silently choose one
- record the conflict explicitly
- keep the disputed point out of current must-pass acceptance unless resolved
- escalate to the requirement owner or architecture owner

## 6.7 Future-scope rule

Later-phase or future-scope content may appear only as:
- `Out of scope` / `out_of_scope`
- non-blocking `Open questions`
- an explicit engineering note outside the conversion outputs when needed for extensibility awareness

It must not appear as current must-pass acceptance unless explicitly requested.

---

# 7. Evidence expectations at conversion time

## 7.1 Default starting set

Use the default `evidence_required` list defined in `[TPL] Intent and Acceptance Interface Writing Standard` §3.11 as the starting set. That source is authoritative for the list; do not maintain a duplicate copy here.

## 7.2 Conversion-time addition

Because the reviewer primarily approves through evidence rather than code reading, verify these are in the starting set (already covered by Writing Standard §3.11):

- `traceability_summary`
- `accessibility_audit` (when Tier 1 involved)
- `operator_digest` (the M4 one-page digest per [MECH] CI/CD Milestone Policy §6.4)

## 7.3 Slice-specific additions when materially needed

Add when applicable:

- `ui_flow_recording` — when the slice involves a novel user flow not previously validated
- `state_transition_examples` — when the slice has stateful entities with non-trivial transitions
- `error_case_examples` — when the slice has complex error handling
- `permission_matrix_result` — when the slice has multi-role permission rules
- `audit_log_examples` — when the slice emits multi-type audit events

---

# 8. Extractor self-check

Before finalizing the extracted `intent.md` and `acceptance.yaml`, verify all of the following:

1. Is the slice narrow enough for one main worktree or one main PR?
2. Did any future or later-phase requirement leak into current must-pass acceptance?
3. Are all `traces_to_*` fields filled in correctly?
4. Do `permissions.owning_tier` entries respect phase TDD `§1.Tier-Responsibility-Mapping` tier mapping and [RULE] Claude Code Architecture Rules §3?
5. If Tier 1 involved: is the UX brief present in intent.md?
6. If Tier 1 involved: are accessibility_expectations present in acceptance.yaml?
7. If Tier 1 involved: are referenced components named in the UX brief covered by the Hub-authored UX Design Spec instance §2.3 inventory entries (which Hub grounded in the Hub DS mirror at TK-02 Step 2.3)? Component-existence is verified at CC code time via SK-F against the CC mirror; at TK-03, the converter trusts TK-02 Step 2.3's Hub-side authoring discipline. Hub/CC mirror lock-step per DSG §12.5 is the operational guarantee that what Hub grounded against matches what CC will verify against.
8. Are all must_pass_scenarios traceable to at least one PRD FR or user value statement?
9. Are all non_regression_constraints traceable to PRD non-regression expectations or TDD stability rules?
10. Are any unresolved business-rule or architecture open questions present in intent.md? (Should be none — resolve upstream.)
11. Is the intent.md `Assumptions` section free of assumptions that change acceptance or boundary?
12. Are any conflicts between PRD and TDD silently papered over in the extraction?
13. Is the extraction free of database tables, API payload shape specifics, component internal specs, test framework code, and file paths?
14. **Is `app_slug` consistent across phase PRD §1.1, phase TDD §1 header, slice metadata, and the target worktree path at the receiving CC? Is `phase_number` consistent across phase PRD, phase TDD, and slice metadata? Is `assigned_node` consistent between the relevant phase TDD `§4.{feature-slug}.Header.assigned_node` declaration and the CC session at which the slice will be implemented (the conversion itself runs in Hub; the assigned_node consistency is verified at TK-03 by inspecting the TDD value).**
15. **Are all referenced paths under `apps/{app-slug}/specs/` for feature artifacts, with the project-level DS instance CC mirror at `specs/design-system.md`, the Hub DS mirror at `hdc_ref_design-system.md`, and the Hub-authored UX Design Spec instance at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` as the recognized non-app-scoped or per-feature paths? No references remain to retired paths `specs/design-system-changes/{change-id}.md` (the legacy DS change-draft path; change drafts now live CD-internally as part of UX Design Spec instance §2.4 additive update plans) or `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` (the legacy CD-authored bundle path, retired in favor of the Hub-authored UX Design Spec instance markdown).**

If any item fails, return to upstream resolution before approval.

---

# 9. Abstraction boundary

The following leakage patterns indicate the conversion has pulled in content that belongs elsewhere.

| Leakage pattern | Correct source |
|---|---|
| Database schema, table/column details | TDD or code |
| API payload shape specifics in intent.md | phase TDD `§4.{feature-slug}.API-Contracts` or openapi.yaml |
| Specific test framework code | test-plan.yaml or test code |
| Design tokens, component internal specs | Design System Governance |
| Implementation options not yet approved | TDD |
| Sprint planning, estimation, runtime config | Not a specification concern |
| Branch topology, node assignment mechanics | [RULE] Workspace Topology |
| Repository path layout structure | [RULE] Claude Code Architecture Rules §Y.1 |
| Code review tool command semantics | CC substantive Codex Plugin Usage canonical (post-Phase-3) |
| Skill internal prompts | `.claude/skills/{name}/SKILL.md` |
