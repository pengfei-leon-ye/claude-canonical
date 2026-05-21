# [TPL] PRD / Prototype / MVP Spec Template

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable template for PRD drafting, prototype briefs, and MVP briefs. Handoff-readiness is expressed via Execution Depth = Full on a PRD, not a separate artifact type.
- **Source Category**: Cat 2
- **Management-System Role**: Specification-support template; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS] §2.3.2**: This template authors Cat 2 specification outputs (phase-scope and feature-scope PRDs, prototype briefs, MVP briefs). The template artifact itself is governed under the Cat 2 specification template family per [OS] §2.3.2; instances produced by this template are Cat 2 specification deliverables.
- **Relationship to [OS]**: Supports the Specify loop by converting product thinking and solution intent into handoff-ready specification artifacts. Grounded in [OS] §0.1 project-level operating premises and [OS] §0.2 Cat 2 role anchor.
- **Relationship to [PRIN]**: Applies [PRIN] HR Digital Decision Design Principles §1 (business-first, architecture-enabled), §2 (capability-first, not vendor-first), §4 (lifecycle value over implementation convenience), §6 (operation management and value realization by design), §7 (analytics-informed digital decision making).
- **Relationship to [RULE] Workspace Topology**: Not directly consumed; the `App Slug` header field declared in §1.1 / §0.7.1 anchors handoff-ready PRDs to a target app whose downstream node assignment is owned by Workspace Topology
- **Relationship to [RULE] Claude Code Architecture Rules**: The `App Slug` value must come from the frozen app-slug roster defined in CC substantive CCAR canonical §Y; cross-reference for handoff-ready PRDs only
- **Relationship to [MECH] Development Track Workflow**: Handoff-ready PRDs (PRD + Full) are dev-track **inputs** (not dev-track artifacts) consumed at TK-01; one PRD = one phase = one feature set introduced in that phase; this template's `App Slug` and `Phase Number` field requirements at PRD + Full satisfy TK-01 input-readiness criteria
- **Relationship to adjacent [TPL] sources**: Consumes framing from `[TPL] Problem Framing Memo` and decisions from `[TPL] Options Paper`; feeds `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification` and `[TPL] Intent and Acceptance Interface Writing Standard` downstream; pairs 1:1 at phase level with `[TPL] Technical Design Document Template` (one PRD-TDD pair per phase per app)
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: When the final document is uploaded to DingTalk Docs, apply that rule to normalize the Markdown before upload.
- **Pairings I participate in**: P-06 (with [TPL] TDD phase-level pairing), P-31 (with [MECH] DTW §3.3 + §3.4)

## How to use this source

See `# 0. Usage Notes` below for the full usage specification, including supported artifact types, writing principles, the artifact-type-to-execution-depth rule, the App Slug field semantics, the section applicability matrix, routing rules, compliance and regulatory anchors rule, and formatting rules.

Default workspace rule:
- draft initiative-specific PRDs, prototype briefs, and MVP briefs in hub chats first
- move the work into a separate project only when contextual isolation, execution density, file volume, sensitivity, or collaboration needs justify it

Downstream execution-interface rule:
- when a PRD produced from this template enters development handoff (i.e., Approved PRD at Full execution depth), it serves as a dev-track input for that phase; downstream `intent.md` and `acceptance.yaml` pairs are extracted at slice level by `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification`, following `[TPL] Intent and Acceptance Interface Writing Standard` for the target-file structure
- the PRD is the upstream canonical source of truth for the phase's feature set; the paired phase TDD covers engineering specification; extracted slice-level interface pairs are downstream execution-layer compressions, not replacements

This source defines stable template logic. Initiative-specific content belongs in the generated document, not in this source.

---

# 0. Usage Notes

## 0.1 Purpose

This template is designed for HR Digital product and solution work that must be understandable and executable by developers, junior product managers, vendors, and cross-functional reviewers.

Use it when the work needs more than a loose concept note and must become implementable, testable, and reviewable.

**Operating premise**: This template defines the operator's specification format for handoff to Cat 3 product configuration and Cat 4 development work in the internal solution designer / PM-equivalent role (per [OS] §0.2 Cat 2 row). It is not a PM portfolio piece, not a recreation of big-tech standard PRD field sets (P0/P1/P2 priority schemes, RICE scoring, north-star metrics, dependency graphs), and not a substitute for the actual decision-making the operator does before authoring. Industry PRD templates are sources of inspiration; this template is calibrated to what makes downstream Cat 3 / Cat 4 work succeed in this hub.

## 0.2 Supported artifact types

This is one canonical template that supports three common output types:

- **Prototype Brief**: a lighter artifact used to shape or validate flows, assumptions, and user experience before full specification
- **MVP Brief**: a focused specification for a limited first release or controlled pilot
- **PRD**: a fuller product requirement document for business logic, process, data, permissions, and delivery alignment; at Execution Depth = Full, the PRD is **handoff-ready and phase-scoped** — one PRD covers the feature set introduced in one phase of one app, and serves as the dev-track input consumed at TK-01

Handoff-readiness is a depth state of the PRD, not a separate artifact type. An Approved PRD at Full depth is the dev-track input for that phase. Slice-level downstream `intent.md` / `acceptance.yaml` extraction follows `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification`.

## 0.3 What belongs in the canonical template

The canonical template should cover, at the right depth for the artifact type:

- problem and objective clarity
- scope and release cut
- user roles and scenarios
- end-to-end process logic
- business rules
- functional requirements
- data requirements
- roles, permissions, and governance expectations
- integration needs and technical constraints
- non-functional requirements when relevant
- acceptance criteria and traceability
- risks, open issues, and decisions needed

## 0.4 What does not belong in the canonical template

This template should not become:

- a policy document
- a process map repository
- a detailed SOP or runbook
- a sprint tracker or task board
- a vendor statement of work
- a low-level engineering design document
- a raw note dump with unresolved contradictions

## 0.5 Writing principles

Use the following writing rules when generating documents from this template:

- Be explicit, not implicit.
- Describe business logic, not only feature labels.
- Make the document implementable and testable.
- Reduce interpretation space for developers, junior PMs, vendors, and non-product readers.
- Separate facts, assumptions, open issues, and decisions needed.
- Define scope and out-of-scope clearly.
- State what must happen, for whom, under what condition, and with what expected result.
- Link major requirements back to scenarios, rules, and acceptance logic.

## 0.6 Business solution design versus technical implementation detail

This template is primarily for **business solution design**, not detailed engineering design.

Business solution design should specify:

- the business problem being solved
- target users or roles
- process flow and key scenarios
- business rules and decision logic
- required system behavior
- required data and permissions
- integration needs
- acceptance logic and business sign-off expectations

Technical implementation detail should usually stay outside this template, including:

- code structure
- component architecture
- API payload design
- database schema design
- infrastructure topology
- CI/CD setup
- backlog task decomposition

If technical detail materially affects feasibility or delivery, capture it here as a **constraint**, **dependency**, or **integration note**, then reference a separate engineering artifact when needed.

## 0.7 Artifact type and execution depth rule

Do not choose `Artifact Type` and `Execution Depth` independently.

Use the following rule so the template is applied consistently and does not become a free-form combination.

| Artifact Type | Allowed Execution Depth | Normal Use |
|---|---|---|
| Prototype Brief | Lite or Standard | Test assumptions, workflow logic, user response, or prototype direction |
| MVP Brief | Standard (Full allowed when the MVP brief is also the implementation handoff basis) | Define a limited first release or pilot scope |
| PRD | Standard or Full | Full requirement definition and cross-functional alignment; **PRD + Full is handoff-ready and phase-scoped** |

Apply this sequence:
1. choose the `Artifact Type`
2. derive the `Execution Depth` from the allowed combination
3. avoid invalid combinations

Default interpretation rules:
- `Prototype Brief + Lite` is the normal early-stage prototype document
- `Prototype Brief + Standard` is allowed when prototype learning needs clearer rule, flow, or data definition
- `Prototype Brief + Full` should not be used; if the document is explicit enough for direct execution, reclassify it as `PRD`
- `MVP Brief + Standard` is the normal MVP document
- `MVP Brief + Full` is allowed only when the MVP brief is also the implementation handoff basis
- `PRD + Standard` is the normal working PRD; once an `App Slug` and `Phase Number` are committed, the PRD lives at the phase-level path defined in §0.11 even while in Draft
- `PRD + Full` is the **phase-level handoff-ready PRD**: one PRD = one phase = one feature set introduced in that phase; it is the **dev-track input** (not a dev-track artifact) consumed at TK-01

**PRD as dev-track input (not artifact)**: Per the Phase ontology established in [RULE] Workspace Topology, PRD + Full sits **upstream** of the Development Track. The dev-track produces TDD, slice-list, intent, acceptance, test plans, and deployable code; the PRD is the input feed, not a dev-track output. This boundary is structural, not stylistic — a PRD must remain readable to non-engineering stakeholders (product, business, vendor, junior PM) and **must not** include dev-track-internal mechanics such as walking-skeleton scope, slice decomposition, per-unit node assignments, cross-phase engineering refactoring deltas, or CI/CD milestone choreography. Those concerns belong in the paired phase TDD. **Logical system architecture, logical data model, and business-entity relationship diagrams remain valid PRD content when the business solution requires them — the PRD is the upstream of the TDD, not a peer artifact, and may carry the architectural framing the TDD elaborates from. Engineering-architecture decisions (technology choice, deployment topology, persistence backend selection, tier-internal module decomposition) are TDD's domain.**

**Phase-level singleton + cross-phase additive evolution**:
- An app's lifecycle proceeds through monotonic phases: **Phase 1** = 0→1 (the feature set introduced when the app is first runnable); **Phase N (N ≥ 2)** = 1→N (an additive iteration introducing new features and/or evolving prior ones)
- One PRD per phase per app — `apps/{app-slug}/specs/prd/phase-{N}.md`
- Phase 2+ PRDs are **standalone documents** (not deltas): each phase PRD reads as a self-contained feature-set specification for that phase, and may explicitly reference prior phases as context or dependency in §3 (Scope and Assumptions) when materially relevant
- A single PRD covers **multiple features** introduced in that phase; the feature list is captured in §7 (Functional Requirements) with feature-slug grouping (per §7 guidance)

Execution depth meanings:
- **Lite**: enough to frame the problem, scenarios, and learning or design direction
- **Standard**: enough to align business, product, and delivery stakeholders with implementable logic
- **Full**: enough to support build, configuration, testing, or vendor execution with minimal ambiguity; for PRD, **Full also implies phase commitment** — `App Slug` and `Phase Number` are mandatory header fields (per §0.7.1)

Note on "Lite" disambiguation: Execution Depth "Lite" refers to **document depth** for the artifact, and is a separate concept from [OS] §12.1 response mode "Lite" (which describes conversational working mode). They coexist without conflict.

## 0.7.1 App Slug and Phase Number field semantics

The `App Slug` and `Phase Number` fields in §1.1 anchor a handoff-ready PRD to its target app and phase in the multi-app monorepo (per CC substantive Claude Code Architecture Rules canonical, repository layout §Y — frozen app-slug roster). They are conditional-mandatory based on the artifact type and execution depth combination established in §0.7.

**Conditional applicability**:

| Combination | App Slug | Phase Number | Rationale |
|---|---|---|---|
| **PRD + Full** | **Mandatory** | **Mandatory** | Phase-level handoff-ready PRD lands at `apps/{app-slug}/specs/prd/phase-{N}.md` per [MECH] Development Track Workflow TK-01; both app and phase must be committed before handoff |
| **PRD + Standard** | **Mandatory** | **Mandatory once an app is committed** | Standard PRD is the upstream of the paired phase TDD; the paired TDD has both `app_slug` and `phase_number` as mandatory header fields per `[TPL] Technical Design Document Template`; PRD-TDD paired fields must be aligned at the upstream side, not back-filled by the TDD author |
| MVP Brief (any depth) | Recommended when target app is known | Optional (use `1` if treated as a Phase 1 candidate) | An MVP Brief that names a target app benefits from the same path-anchoring discipline as a PRD; Phase Number applies only when the MVP brief is intended to evolve into a Phase 1 PRD |
| Prototype Brief (any depth) | Optional | Optional | Early-stage prototypes may pre-date both app and phase commitment; leave blank when not yet decided |

**Phase Number value rules**:
- Monotonic positive integer starting at `1`
- **Phase 1** = the 0→1 phase (the feature set introduced when the app is first runnable)
- **Phase N (N ≥ 2)** = 1→N additive iteration introducing new features and/or evolving prior ones
- Phase numbers are sequential per app; `Phase 3` of `app-A` is unrelated to `Phase 3` of `app-B`
- Phase Number is **immutable for the life of the PRD** once committed — re-targeting a feature to a different phase is a new PRD authored under that phase, not a renumbering of the existing one

**App Slug value rules**:
- Must come from the frozen app-slug roster maintained at workspace level (per CC substantive Claude Code Architecture Rules canonical, repository layout §Y — frozen app-slug roster). Free-form values, abbreviations, or display names are not valid `App Slug` values
- Once a PRD is signed off at PRD + Full with a populated `App Slug`, the value is immutable for the life of that PRD. If the feature is conceptually re-targeted to a different app after handoff, a new PRD is authored under the new app, not the existing one mutated

**Coordination with paired and downstream artifacts**:
- The `App Slug` and `Phase Number` here must match the `app_slug` and `phase_number` fields in the paired phase TDD's header (per `[TPL] Technical Design Document Template` §1)
- Downstream artifacts produced from this PRD inherit the `app_slug` value at three different scope levels per [MECH] Development Track Workflow §4 path conventions:
  - **Phase-numbered** (same scope as this PRD): paired phase TDD at `apps/{app-slug}/specs/tdd/phase-{N}.md`; phase master test plan at `apps/{app-slug}/specs/test-plan/phase-{N}.md`
  - **Feature-slug-scoped** (per feature within this phase): slice-list at `apps/{app-slug}/specs/slice-list/{feature-slug}.md`; feature integration test plan at `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml`
  - **Slice-id-scoped** (per slice): intent at `apps/{app-slug}/specs/intent/{slice-id}.md`; acceptance at `apps/{app-slug}/specs/acceptance/{slice-id}.yaml`; slice test plan at `apps/{app-slug}/specs/test-plan/{slice-id}.yaml`
  - **App-scoped, cross-phase additive** (one file per app): OpenAPI surface at `apps/{app-slug}/specs/openapi.yaml`

## 0.8 Section applicability matrix

Legend:
- **M** = mandatory
- **C** = conditional; include when materially relevant
- **O** = optional

| Section | Lite | Standard | Full | Guidance |
|---|---|---|---|---|
| 1. Document Information | M | M | M | Always required |
| 2. Background and Objectives | M | M | M | Always required |
| 3. Scope and Assumptions | M | M | M | Always required |
| 4. User Roles and Scenarios | M | M | M | Always required |
| 5. End-to-End Process Flow | C | M | M | At least a simplified flow in Lite |
| 6. Business Rules | C | M | M | Keep only materially relevant rules in Lite |
| 7. Functional Requirements | C | M | M | Keep brief in Lite |
| 8. Data Definition | O | C | M | Mandatory when build depends on data |
| 9. Roles, Permissions, and Governance | O | C | M | Mandatory when access or control matters |
| 10. Integration and Technical Constraints | O | C | M | State constraints, not low-level design |
| 11. Non-functional Requirements | O | C | C | Include only when materially relevant |
| 12. Acceptance Criteria and Traceability | C | M | M | Traceability is mandatory for handoff |
| 13. Risks, Open Issues, and Decisions Needed | M | M | M | Always required |
| 14. Appendix | O | O | O | Use for supporting material |
| 15. Document Quality Checklist | M | M | M | Required before review or handoff |

## 0.9 Routing rule in this workspace

In this workspace, initiative-specific drafting should normally follow this path:

1. frame and draft in hub chat
2. iterate the working PRD, prototype brief, or MVP brief in hub chat while shared context remains useful
3. move the work into a separate project only when there is a clear justification such as isolation, heavy execution, file volume, sensitivity, or collaboration needs
4. promote only durable template logic into source

## 0.10 Compliance and regulatory anchors rule for this template

This template does **not** require a single `Target Management-System Landing Level` field. PRDs under this template are Cat 2 specification outputs per [OS] §2.3.1 and do not land in the L1-L5 management-system hierarchy.

However, a PRD may need to declare compliance and regulatory constraints that materially affect design, implementation, or review:
- applicable external regulations (e.g., GDPR, PIPL, SOC2, industry-specific rules)
- applicable company-level policy documents maintained outside this hub
- unresolved compliance ambiguities that must be clarified before sign-off

**Hard boundary** (per [OS] §2.3.3):
- Do not cite `[POL] Digital Solution Policy Architecture Map` or any L2-L5 management-system artifact as a compliance anchor. `[POL]` is a Cat 1 source governing the user's team management-system thinking; it is not an authoritative constraint on the applications the team builds. Compliance anchors must point to external regulations or company-level policy documents directly.

Use the optional `Compliance and Regulatory Anchors` subsection in the body (§3.5) to state specific anchors when they matter. Omit the subsection when no material compliance constraint applies.

## 0.11 Formatting and publishing rule

- Generated documents do not require a standalone document-title H1. Start directly from numbered section headings at H1 level.
- In section 1.1, use a simple two-column table with `Item` and `Content` only.
- In section 1.2, use the Version History table format defined in this template.
- The source template does not force bilingual output.
- Generated documents may be English-only, Chinese-only, or bilingual. Set the language deliberately based on audience, review context, and implementation need.
- If the final document will be uploaded to DingTalk Docs, normalize the upload-ready Markdown per [RULE] DingTalk Markdown Format Control Specification before upload.

**Canonical path for handoff-ready PRDs**: when an Approved PRD at Full depth becomes the development handoff input, its canonical filesystem location is `apps/{app-slug}/specs/prd/phase-{N}.md` per [MECH] Development Track Workflow TK-01. The `{app-slug}` segment is the value populated in §1.1 `App Slug`; the `{N}` segment is the value populated in §1.1 `Phase Number`. The project-level Design System Spec singleton (`specs/design-system.md`) is not under any app's directory and is referenced by handoff-ready PRDs but not relocated.

For PRDs that have not (yet) entered handoff (Prototype Brief, MVP Brief, PRD + Standard before app and phase commitment), the filesystem location is at the operator's discretion until handoff readiness is reached.

---

# 1. Document Information

## 1.1 Document Metadata

| Item | Content |
|---|---|
| Artifact Type | Prototype Brief / MVP Brief / PRD |
| Execution Depth | Lite / Standard / Full (derive from 0.7; do not choose freely) |
| App Slug | (conditional-mandatory per §0.7.1; mandatory for PRD at any execution depth; recommended for MVP Brief when target app is known; optional for Prototype Brief) |
| Phase Number | (conditional-mandatory per §0.7.1; mandatory for PRD + Full; mandatory for PRD + Standard once `App Slug` is committed; positive integer starting at `1`; Phase 1 = 0→1, Phase N (N≥2) = additive iteration) |
| Language Mode | English / Chinese / Bilingual |
| Product / Solution Name |  |
| Version | `v1` / `v2` / `v3` ... (see 1.2 rules) |
| Owner |  |
| Contributors |  |
| Reviewers |  |
| Primary Audience | Developer / Junior PM / Vendor / Stakeholder |
| Status | Draft / Approved |
| Related Project / Initiative |  |
| Target Release / Milestone |  |
| Related Documents |  |

## 1.2 Version History

| Version | Date | Status | Change Summary |
|---|---|---|---|
| v1 | YYYY-MM-DD | Approved | Initial baseline |

Version rules:
- Use a single monotonic integer: `v1`, `v2`, `v3`, ...
- During Draft iteration before first Approved, keep version at `v1`
- First Approved = `v1`
- After first Approved, any substantive revision starts as a new Draft with the next integer (`v1` → `v2`); the Version field in 1.1 reflects the current working version regardless of Status
- Typo, formatting, or link fixes do not increment version; correct in place
- Record each version increment as a row in 1.2 with a one-line summary; Draft-phase in-place edits are not recorded
- When the version in 1.1 is in Draft state, append a row in 1.2 only after it transitions to Approved

---

# 2. Background and Objectives

## 2.1 Business Background
Describe the business context, trigger, and why this requirement exists now.

## 2.2 Problem Statement
State the specific problem to be solved.
Separate symptoms from root cause where possible.

## 2.3 Objectives
List the expected business and product outcomes.
Prefer measurable outcomes where possible.

## 2.4 Success Measures
State how success will be recognized.
Use outcome, usage, adoption, quality, or control measures when relevant.

## 2.5 Out of Scope
Clarify what this document does not intend to solve in this phase.

---

# 3. Scope and Assumptions

## 3.1 Scope
Define the business scope, user scope, geographic scope, and system scope.

## 3.2 Phase Scope and Cross-Phase Context
For PRDs with a committed Phase Number (per §0.7.1), state:
- which features are introduced in this phase (the feature set this PRD covers; details land in §7)
- what is intentionally left for later phases
- (Phase N ≥ 2 only) which prior-phase features this phase depends on, evolves, or supersedes — name them by feature-slug or by reference to the prior phase PRD

For PRDs without a committed Phase Number (Prototype Brief, MVP Brief, early-stage PRD + Standard), state what is included in the current release, prototype, or pilot, and what is intentionally left for later phases.

## 3.3 Key Assumptions
List assumptions that materially affect design, delivery, or acceptance.

## 3.4 Dependencies
Note dependencies on upstream or downstream teams, systems, vendors, data assets, or policies.

## 3.5 Compliance and Regulatory Anchors (Optional)
Use this subsection only when material compliance constraints must be explicit for reviewers, implementers, or vendors.

Per [OS] §2.3.3, do not cite `[POL] Digital Solution Policy Architecture Map` or any L2-L5 management-system artifact here. Compliance anchors must point to external regulations or company-level policy documents directly.

State the specific anchors that matter, such as:
- applicable external regulations (e.g., GDPR, PIPL, SOC2, industry-specific rules), with the specific clauses or articles when they materially affect design
- applicable company-level policy documents maintained outside this hub (give the document name and version)
- unresolved compliance ambiguities that must be clarified before build or sign-off

---

# 4. User Roles and Scenarios

## 4.1 User Roles

| Role | Description | Notes |
|---|---|---|
|  |  |  |

## 4.2 Key Scenarios

| Scenario ID | Scenario Name | User Role | Trigger | Expected Outcome | Priority |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 4.3 Prototype or Research Questions
Use this subsection when the artifact is a prototype brief or early MVP brief.
State what the prototype is meant to validate, disprove, or clarify.

---

# 5. End-to-End Process Flow

## 5.1 Main Flow
Describe the normal end-to-end process in sequence.

## 5.2 Branches and Exceptions
Describe important branches, exception paths, and operational fallback handling.

## 5.3 Process Notes
Add clarifications on ownership, timing, handoff, control points, or operating checkpoints when needed.

---

# 6. Business Rules

> This is a critical section for HR Digital and other business-facing products. Rules should be explicit and testable.

## 6.1 Rule List

| Rule ID | Category | Rule Statement | Trigger / Condition | Expected Outcome | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Recommended categories:
- eligibility rules
- approval rules
- calculation rules
- time rules
- policy constraints
- exception handling rules
- data validation rules
- notification or escalation rules

## 6.2 Rule Clarifications
Capture rule ambiguities, unresolved cases, or known interpretation risks when needed.

---

# 7. Functional Requirements

> For phase-level PRDs (PRD + Full or PRD + Standard with committed Phase Number), this section is the authoritative **feature list for this phase**. Functional requirements are grouped by feature, with each feature carrying a feature-slug used by all downstream artifacts (paired phase TDD per-feature spec, slice-list, intent, acceptance, slice and feature-integration test plans).

## 7.1 Feature List (phase-level PRDs)

For PRDs with a committed Phase Number, list the features introduced or evolved in this phase. Each row is one feature.

| Feature Slug | Feature Name | Description | Related Scenarios | Phase Role | Priority |
|---|---|---|---|---|---|
|  |  |  |  | New / Evolves prior-phase feature | High / Medium / Low |

Feature-slug rules:
- lowercase kebab-case
- stable for the life of the feature across phases (a feature evolved in Phase N keeps its Phase 1 slug)
- unique within an app (two features in the same app cannot share a slug; the slug namespace is per-app, not per-phase)
- no whitespace, no underscores, no special characters

## 7.2 Functional Requirement List

For PRDs without a committed Phase Number (Prototype Brief / MVP Brief / early PRD), or as a sub-table within each feature for phase-level PRDs.

| FR ID | Function / Capability | Description | Related Scenarios | Related Rules | Priority | Feature Slug (phase-level PRDs only) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 7.3 Detailed Functional Design

Use the following structure for each major function. For phase-level PRDs, organize the detailed designs under feature-slug headers (e.g., `### Feature: time-off-request`) and place each feature's FR designs under its header.

### FR-[X] Function Name
- **Purpose**:
- **User Role**:
- **Related Scenario(s)**:
- **Pre-condition**:
- **Trigger**:
- **Input**:
- **System Behavior**:
- **Output**:
- **Related Business Rules**:
- **Priority / Release**:
- **Edge Cases**:
- **Error Handling**:
- **Open Questions**:

## 7.4 Prototype or UX Notes
Use when relevant.
Reference mockups, click paths, or prototype intentions that materially affect understanding.
Do not use this subsection for purely aesthetic commentary.
Component selection, token usage, accessibility commitments, and Tier 1 implementation details belong in a separate Hub-authored UX Design Spec instance (authored at TK-02 Step 2.3) per `[TPL] UX Design Spec` (consumed at TK-03 per-slice intent.md UX brief; the legacy TDD §5.8 / `§4.{feature-slug}.UX-Strategy` sub-section has been retired) and downstream slice-level intent.md UX brief, not here.

---

# 8. Data Definition

## 8.1 Key Data Objects

| Data Object | Description | Source / System of Record | Owner | Usage | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 8.2 Key Fields

| Field Name | Definition | Type | Mandatory | Source | Validation / Rule Link | Notes |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 8.3 Data Quality and Usage Notes
Describe key data-quality controls, validation logic, reporting implications, or known limitations.

---

# 9. Roles, Permissions, and Governance

## 9.1 Access Roles

| Role | View | Create | Edit | Approve | Export | Notes |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 9.2 Governance Requirements
Specify compliance, audit, segregation of duties, logging, retention, and traceability requirements.

## 9.3 Operational Controls
Define manual controls, review checkpoints, exception approvals, or operating oversight when applicable.

---

# 10. Integration and Technical Constraints

## 10.1 Integration Requirements

| Integration Item | Upstream | Downstream | Direction | Frequency / Timing | Business Purpose | Notes |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 10.2 Technical Constraints
List important technical constraints, platform limitations, configuration boundaries, or implementation dependencies that materially affect design.

## 10.3 Implementation Boundary Note
Use this section to state constraints or required interfaces, not low-level engineering design.
If detailed technical design is required, reference a separate engineering artifact.

---

# 11. Non-functional Requirements

| Category | Requirement | Notes |
|---|---|---|
| Performance |  |  |
| Availability |  |  |
| Security |  |  |
| Privacy / Compliance |  |  |
| Logging / Auditability |  |  |
| Usability |  |  |
| Data Latency |  |  |

---

# 12. Acceptance Criteria and Traceability

## 12.1 Key Validation Scenarios

| AC ID | Scenario | Expected Result | Related Rules / FRs |
|---|---|---|---|
|  |  |  |  |

## 12.2 Rule Validation
Identify which business rules must be explicitly tested before go-live, pilot release, or handoff approval.

## 12.3 Business Sign-off
Define who needs to validate and sign off, and on what basis.

## 12.4 Traceability Check

| Objective / Scenario | Related Rules | Related FRs | Related ACs | Gaps / Notes |
|---|---|---|---|---|
|  |  |  |  |  |

---

# 13. Risks, Open Issues, and Decisions Needed

## 13.1 Key Risks

| Risk ID | Risk Description | Impact | Mitigation |
|---|---|---|---|
|  |  |  |  |

## 13.2 Open Issues

| Issue ID | Issue | Owner | Due Date |
|---|---|---|---|
|  |  |  |  |

## 13.3 Decisions Needed

| Decision ID | Decision Topic | Options | Recommendation |
|---|---|---|---|
|  |  |  |  |

---

# 14. Appendix

Include supporting material when useful:

- process diagrams
- mockups or wireframes
- sample reports
- policy references
- data mapping sheets
- external links or engineering references

Use the appendix to support understanding, not to hide unresolved core logic.

---

# 15. Document Quality Checklist

Before sending the document for review, vendor execution, or implementation follow-up, check the following:

- [ ] The correct artifact type and execution depth have been selected using the template rule rather than free choice.
- [ ] **App Slug populated when required**: every PRD (Standard or Full) has `App Slug` populated with a value from the frozen app-slug roster (per §0.7.1); MVP Brief / Prototype Brief with `App Slug` left blank only when target app is genuinely not yet decided.
- [ ] **Phase Number populated when required**: every PRD + Full has `Phase Number` populated; PRD + Standard has `Phase Number` populated once `App Slug` is committed (per §0.7.1).
- [ ] **Feature Slug values consistent**: every feature in §7.1 has a unique kebab-case `Feature Slug`; values match those used in the paired phase TDD's per-feature sections.
- [ ] The business problem is specific and clear.
- [ ] Objectives and success measures are explicit.
- [ ] Scope and out-of-scope are clearly defined.
- [ ] The current phase scope (or release / MVP / prototype boundary) is visible; for Phase N ≥ 2 PRDs, dependencies on prior phases are stated in §3.2.
- [ ] Key user roles and scenarios are covered.
- [ ] Main flow and key exceptions are understandable.
- [ ] Business rules are explicit and testable.
- [ ] Functional requirements are implementable.
- [ ] Data definitions are sufficient for build, configuration, or reporting where relevant.
- [ ] Permissions, governance, and control expectations are covered where relevant.
- [ ] Integration needs and technical constraints are visible where relevant.
- [ ] Business solution design and technical implementation detail are properly separated.
- [ ] **No dev-track-internal mechanics leakage**: this PRD does not contain walking-skeleton scope, slice decomposition, per-unit node assignments, cross-phase engineering refactoring deltas, or CI/CD milestone choreography (per §0.7 — those belong in the paired phase TDD). Logical system architecture, logical data model, and business-entity relationship diagrams are not subject to this exclusion when the business solution materially requires them.
- [ ] Acceptance criteria are clear.
- [ ] Major objectives, scenarios, rules, requirements, and acceptance points can be traced logically.
- [ ] Open issues, dependencies, and decisions needed are visible.
- [ ] If material compliance constraints apply, external regulations or company-level policy references are explicitly stated in §3.5 (no citation of `[POL]` or L2-L5 artifacts per [OS] §2.3.3).
- [ ] Language mode has been chosen deliberately for the actual audience.
- [ ] Version field and Version History are consistent; any substantive revision since last Approved has been recorded.
- [ ] **For handoff-ready PRDs (PRD + Full)**: the file path follows `apps/{app-slug}/specs/prd/phase-{N}.md` per §0.11 + [MECH] Development Track Workflow TK-01.
- [ ] If the document will be uploaded to DingTalk Docs, the final Markdown has been normalized per [RULE] DingTalk Markdown Format Control Specification.
