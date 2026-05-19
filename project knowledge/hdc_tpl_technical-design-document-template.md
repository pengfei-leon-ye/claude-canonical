# [TPL] Technical Design Document Template

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable template for producing a phase-level Technical Design Document (TDD) that captures, per phase per app, foundational architecture (Phase 1) or architecture deltas (Phase N ≥ 2), cross-feature concerns (NFR baselines, security, observability, deployment), walking skeleton scope (Phase 1 only — full canonical specification at §3 referencing [RULE] Workspace Topology §4.6 and [MECH] CI/CD Milestone Policy §2.0), and per-feature engineering spec for every feature introduced in that phase. UX strategy content is intentionally NOT part of the per-feature engineering spec; it lives in feature-level UX Design Spec instances authored in Claude Design (per `[TPL] UX Design Spec`) when the feature touches Tier 1.
- **Source Category**: Cat 4
- **Management-System Role**: Specification-support template; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Supports the Specify loop by formalizing the technical architecture layer between phase-level PRD and slice-level execution interfaces
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §3 global core with governed local variance, §5 management mechanism over ad hoc control, §6 operation management and value realization by design, §7 analytics-informed decisions, §10 MECE decomposition, §12 make important work executable
- **Relationship to [PRIN] People Experience Design Principles**: Applied via UX Design Spec instances (CD-authored per `[TPL] UX Design Spec`) when a feature touches Tier 1; the TDD does not embed UX strategy content
- **Relationship to [REF] Hub-CD-CC Architecture**: TDD is Hub-authored (specification main body per §5.1 content pillar); when a feature's `Header.tier_1_involved: true`, the TDD's per-feature declaration triggers a UX Design Spec instance authoring cycle in Claude Design (presentation pillar) per §5.2; CC consumes the resulting bundle alongside this TDD when slice implementation begins (implementation pillar)
- **Relationship to [RULE] Workspace Topology**: Node assignment for each feature in the phase is owned by Workspace Topology §6 (workflow) / §2.1 (logical node catalog); the per-feature §4.{feature-slug} sub-section records the assigned node for that feature. Phase-level TDD does not carry a single `assigned_node` header field because a phase may span multiple features executing on different nodes
- **Relationship to [RULE] Claude Code Architecture Rules**: Module decomposition and tier mapping in per-feature §4.{feature-slug} must respect three-tier architecture defined there; per-feature module decomposition may reference `packages/domain/{domain-name}/` modules per Architecture Rules §Y.4 Model B (independent domain lifecycle)
- **Relationship to [MECH] Development Track Workflow**: Template consumed in TK-02; TK-02 outputs the phase TDD plus paired phase test plan, per-feature slice-lists, app-scoped openapi additions, and per-feature node assignments
- **Relationship to [MECH] CI/CD Milestone Policy**: Per-feature module decomposition slice-size advisory cross-references CI/CD Milestone Policy §2.7 soft upper limits; phase-level a11y testing strategy in §2.2.7 aligns with Milestone Policy thresholds (Milestone Policy §2.4.1 if a11y gate semantics apply in a future revision)
- **Relationship to [RULE] Design System Governance**: TDD per-feature `§4.{feature-slug}.Header.tier_1_involved` declaration triggers the UX Design Spec instance authoring path governed by DSG. TDD itself does not author DS-coupled UX content; it declares scope and leaves authoring to CD per the three-way distribution model in DSG §1.1.
- **Relationship to adjacent [TPL] sources**:
  - Downstream of `[TPL] PRD / Prototype / MVP Spec Template` (1:1 phase-level pairing)
  - Paired with `[TPL] UX Design Spec` — per-feature `Header.tier_1_involved: true` triggers a UX Design Spec instance for that feature; this template does not embed UX strategy content
  - References `[TPL] ADR Spec` — phase-level architectural decisions captured as separate ADR artifacts per ADR Spec; §2.2.8 of this template is an **index** of relevant ADRs, not an embed of decision content
  - Upstream of `[TPL] Intent and Acceptance Interface Writing Standard` and `[TPL] PRD + TDD to Intent and Acceptance Conversion Specification`
  - Parallel to `[TPL] Test Plan YAML Schema` (testing strategy in this TDD's cross-feature concerns drives phase test plan content; per-feature testing references drive feature integration test plan and slice test plan content)
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: Apply when uploading to DingTalk Docs
- **Pairings I participate in**: P-06 (with [TPL] PRD phase-level pairing), P-07 (with [TPL] Test Plan three-tier pairing), P-08 (with [TPL] Conversion Spec §2.4), P-11 (with [RULE] WT §4.6.2 + §4.6.3), P-28 (with [TPL] Conversion Spec §2 + §3.8 + [TPL] UX Design Spec §2 — the TDD §4.{feature-slug}.Module-Decomposition is the upstream module-decomposition source for slice-list expansion in Conversion Spec §2, and `tier_1_involved` declaration in §4.{feature-slug}.Header triggers UX Design Spec instance authoring), P-31 (with [MECH] DTW §3.3 + §3.4), P-33 (with [MECH] Application Lifecycle Handoff §5.2 + [RULE] WT §4.6). Coupling with [TPL] ADR Spec (TDD §2.2.8 ADR index ↔ ADR Spec instances) classifies as Tier B per [OS] §8.5.1a — semantic-search-discoverable via the explicit `Relationship to adjacent [TPL] sources` field above; no static pairing registration required.

## How to use this source

Use this source when a phase-level PRD is signed off and architecture-level technical design is needed for that phase; when foundational architecture (Phase 1) or architecture deltas (Phase N ≥ 2) require explicit decision and review; when cross-feature concerns (NFR, security, observability, deployment) need a single phase-level baseline; when each feature introduced in the phase needs module decomposition, data modeling, API design, integration design for slice-level planning; when architectural decisions need to be recorded as ADRs per `[TPL] ADR Spec` and indexed in §2.2.8. For features touching Tier 1, UX coverage is authored separately as a UX Design Spec instance in CD per `[TPL] UX Design Spec`, not inside this TDD.

Do not use as replacement for phase-level PRD, slice-level intent/acceptance, Design System Governance, sprint plan, runtime operations manual, or organizational architecture governance documentation.

---

# 0. Usage Notes

## 0.1 Purpose

The TDD is the canonical technical reference for **a single phase of one app**. One phase produces one TDD. The TDD answers the "how" the paired phase PRD deliberately leaves open. Human-readable; primarily reviewed by you; referenced by Hub Claude during TK-03 per-slice extraction; consumed by Claude Code during M0 entry self-check (TK-04) and TK-05 onward.

A phase TDD covers, in one document, three distinct concern levels: phase-level architecture (`§1`); phase-level cross-feature concerns (`§2`); and per-feature engineering spec (`§4`) for each feature introduced or evolved in the phase. Phase 1 also carries `§3` Walking skeleton scope. The internal asymmetry between Phase 1 and Phase N ≥ 2 is described in §0.8.

## 0.2 Readers

**Primary**: You (architect / decision owner) + Hub Claude (reference during TK-03).
**Secondary**: Claude Code main loop and subagents during M0 entry self-check (TK-04) and implementation (TK-05 onward).

## 0.3 Applicability level

TDD level applies at the **phase level** as a whole, not per feature inside the phase.

| Level | Use when | Section coverage |
|---|---|---|
| **Full** | Phase 1 of any app; any phase introducing new tier or new external integration; regulatory-sensitive phase | All §1 through §4, including §3 Walking skeleton scope (Phase 1 only) |
| **Feature** | Phase N ≥ 2 that adds features within established architecture; no new tier; established patterns | §1 deltas only, §2 deltas only, §4.{feature-slug} per-feature spec |
| **Lite** | Phase N ≥ 2 with a single small contained feature; no architecture impact; low NFR sensitivity | §4.{feature-slug} only, with a brief §1 + §2 deltas-or-none statement |

Declare level in document header. **Anti-pattern**: Lite for what is Feature/Full scope; Feature for a phase that introduces foundational architecture (which is Full by definition since Phase 1).

## 0.4 Boundary with other artifacts

- **Phase PRD owns**: business goals, user value, phase scope, scenarios, business rules, NFR expectations for the phase, feature list (with feature-slug per feature). **The PRD may additionally carry logical system architecture, logical data model, and business-entity relationship diagrams when the business solution materially requires them (e.g., metadata-as-product platforms where the data structure is itself the product specification); the TDD then elaborates engineering-architecture decisions from that framing rather than treating PRD-side architectural content as out-of-scope.**
- **Phase TDD owns**: phase-level **engineering** architecture (technology choices, deployment topology, persistence backend, tier-internal module decomposition, integration patterns), cross-feature concerns (NFR baselines, security, observability, deployment), walking skeleton scope (Phase 1), per-feature engineering spec (data model implementation, API contracts, module decomposition, slice list, domain class hierarchy, open questions) for each feature in the phase. **UX strategy is intentionally not owned here**; it lives in feature-level UX Design Spec instances authored in CD per `[TPL] UX Design Spec` when a feature touches Tier 1.
- **Phase test plan (master, markdown) owns**: phase-level test strategy, cross-feature integration scenarios, app-scale NFR targets, regression policy from prior phase (Phase N ≥ 2), phase exit criteria
- **Feature integration test plan (yaml) owns**: per-feature cross-slice flow tests within a single feature scope
- **Design System Governance owns**: project-level UX foundation (design language, tokens, component inventory, a11y target). The DS instance content itself lives in CD as SOT, with CC mirror at `specs/design-system.md` per DSG §1.1; Hub does not carry a DS instance copy.
- **UX Design Spec owns**: per-feature UX coverage (affected Tier 1 scope, components from DS instance, new-component additive update plans, layout patterns, accessibility call-outs, i18n/RTL call-outs, visual regression anchors, responsive/motion expectations) — authored in CD per `[TPL] UX Design Spec`; reviewed in Hub against the reviewer checklist; consumed in CC during slice authoring
- **Intent owns**: per-slice execution boundary in business-facing language
- **Acceptance owns**: per-slice validation contract
- **Slice test plan (yaml) owns**: per-slice test case design

If content is misplaced, move it. In particular, do not let per-feature design questions inside §4.{feature-slug} smuggle in cross-feature decisions that belong in §2; do not let phase-level NFR drift into per-feature §4 sub-sections; do not embed UX strategy content inside `§4.{feature-slug}` — UX strategy is intentionally externalized to UX Design Spec instances.

**Deferred ownership notes (post-B方案 evaluation)**: This template intentionally does not carry sections for Information Architecture (IA), Permission Model, or Visibility Matrix as standalone TDD sub-sections. These topics are touched at the phase level under §2 (Cross-feature concerns — security baseline, integration boundaries) and at the per-feature level under §4 sub-sections (Module-Decomposition, API-Contracts). Whether to promote any of these to independent `[TPL]` artifacts is deferred for post-B方案 evaluation; when the operational need becomes concrete (e.g., a phase whose IA design merits a standalone artifact, or a Permission Model that cuts across multiple features in non-trivial ways), surface the need and consider creating a dedicated `[TPL]` per [OS] §8.1 durable-first rule + §8.3 abstract-before-storing rule.

## 0.5 Y-chain upstream role

The phase TDD, paired with the phase PRD, is the upstream of per-slice intent and acceptance artifacts (the Y-chain). Specifically, for each slice belonging to a feature in this phase, the TDD provides:

- Module identity for slice decomposition — from the relevant `§4.{feature-slug}.Module-Decomposition`
- API contracts and tier boundaries for `Must not break` items in intent — from `§4.{feature-slug}.API-Contracts` and from phase `§1.Architecture` and `§2.Integration-Boundaries`
- Data model invariants for `data_expectations` in acceptance — from `§4.{feature-slug}.Data-Model`
- Permission ownership tier for `permissions` in acceptance — from `§4.{feature-slug}.Module-Decomposition` plus phase `§2.Security-Baseline`
- UX and accessibility scope for intent.md UX brief and acceptance a11y expectations — from the feature's UX Design Spec instance (CD-authored per `[TPL] UX Design Spec`)

The phase TDD must be stable before TK-03 per-slice artifact production begins for any feature in the phase. Per-feature spec sub-sections inside §4 may be elaborated in stages as long as the slice extraction for a given feature waits for that feature's §4 sub-section to be stable.

## 0.6 Multi-app monorepo positioning

In the Path B2 multi-app monorepo, every phase TDD belongs to exactly one app and one phase. The TDD's `app_slug` and `phase_number` header fields (§1) anchor the phase to its app and phase number; the canonical filesystem location is `apps/{app-slug}/specs/tdd/phase-{N}.md`. Cross-app phase scope is not sanctioned at the TDD level; if a capability genuinely spans multiple apps, it likely belongs in a `packages/domain/{domain-name}/` package consumed by both apps per Architecture Rules §Y.4 Model B, and is referenced inside individual app phases that consume it.

Node assignment is per-feature, not per-phase: a phase may introduce multiple features that execute on different logical nodes. Each `§4.{feature-slug}` per-feature sub-section records its `assigned_node`. Node assignment workflow is owned by [RULE] Workspace Topology §6.

## 0.7 Phase ontology and per-feature structure

A phase TDD has a fixed top-level body structure:

| TDD body section | Phase 1 | Phase N ≥ 2 |
|---|---|---|
| §1 Architecture | Complete foundational architecture | Deltas only + reference to phase-1 architecture |
| §2 Cross-feature concerns | Complete baselines (NFR / security / observability / deployment / integration / compliance / phase-level testing strategy / phase-level decision record) | Deltas only + reference to phase-1 baselines |
| §3 Walking skeleton scope | Required (Phase 1 only) | Does not exist |
| §4 Per-feature engineering spec | One §4.{feature-slug} sub-section per feature introduced in Phase 1 | One §4.{feature-slug} sub-section per feature introduced or evolved in this phase |

**Feature list source**: the feature set covered by this phase TDD's §4 sub-sections must match the feature list in the paired phase PRD §7.1, by feature-slug. A feature evolved across phases keeps its original slug; the §4.{feature-slug} sub-section in the later phase's TDD covers only the deltas for that feature in this phase, not the full feature spec from the earlier phase.

## 0.8 Phase 1 vs Phase N ≥ 2 asymmetry

Phase 1 and Phase N ≥ 2 TDDs share the same outer structure but differ in body content:

- **§1 Architecture in Phase 1**: full foundational architecture decisions — three-tier boundaries, monorepo packaging stance, persistence strategy, BFF-to-domain Pact convention adoption, etc. The Phase 1 TDD is the architectural reference for all subsequent phases of the same app.
- **§1 Architecture in Phase N ≥ 2**: deltas only. State only what changes from the phase-1 baseline. If nothing changes, write "No architecture deltas; phase-1 baseline applies." Reference the phase-1 TDD by path.
- **§2 Cross-feature concerns in Phase 1**: complete baselines for NFR, security, observability, deployment, integration boundaries (the externally-integrated systems known at phase 1), compliance, phase-level testing strategy, phase-level decision record.
- **§2 Cross-feature concerns in Phase N ≥ 2**: deltas only. New external integrations, NFR baseline revisions, observability extensions, etc. If nothing changes, write "No cross-feature delta; phase-1 baseline applies."
- **§3 Walking skeleton scope**: Phase 1 only. Phase N ≥ 2 TDDs do not contain §3 at all (the §3 number is intentionally skipped in Phase N ≥ 2 TDDs to preserve direct comparability of section numbers between phases).
- **§4 Per-feature engineering spec**: identical structure across Phase 1 and Phase N ≥ 2. Each phase covers only the features introduced or materially evolved in that phase.

## 0.9 Internal numbering convention for §4

Per-feature sub-sections are numbered by feature-slug, not by sequential integer:
- `§4.{feature-slug}` (e.g., `§4.time-off-request`, `§4.approval-routing`)
- Inside each `§4.{feature-slug}`, fixed sub-sections labeled by purpose: `Header`, `Data-Model`, `API-Contracts`, `Module-Decomposition`, `Slice-List`, `Domain-Class-Hierarchy`, `Open-Questions` (per §5 of this template). The `UX-Strategy` sub-section that existed in earlier versions of this template has been removed; UX strategy content lives in feature-level UX Design Spec instances authored in CD per `[TPL] UX Design Spec`.

This convention keeps cross-references stable across phases: the same feature retains the same slug across phases, so a Phase 3 reference to "phase-1 §4.time-off-request.API-Contracts" remains valid as long as that feature exists in Phase 1's TDD.

---

# 1. Document header

```markdown
# [TDD] <App Display Name> — Phase <N>

- **app_slug**: <app-slug>                    [MANDATORY; from frozen app-slug roster per [RULE] Architecture Rules §Y]
- **phase_number**: <N>                       [MANDATORY; positive integer; matches paired PRD §1.1 Phase Number]
- **TDD level**: Full | Feature | Lite        [per §0.3]
- **Status**: Draft | Active | Superseded
- **Paired PRD reference**: apps/<app-slug>/specs/prd/phase-<N>.md (version or commit)
- **Prior phase TDD reference** (Phase N ≥ 2 only): apps/<app-slug>/specs/tdd/phase-<N-1>.md (or earlier phase referenced for baseline)
- **Design System Governance instance reference**: instance version referenced (the DS instance content lives in CD as SOT with CC mirror at `specs/design-system.md` per [RULE] DSG §1.1; Hub does not carry the instance — this header field records the version in play, not a Hub-side file path) [only if any feature in this phase touches Tier 1]
- **Author**: <you>
- **Hub Claude session**: <session reference if applicable>
- **Review history**:
  - <date>: <reviewer>: <decision>
- **Supersedes**: <prior phase TDD revision if applicable>
- **Features in this phase**: <comma-separated feature-slug list — must match paired PRD §7.1>
```

**Mandatory field notes**:

- **`app_slug`**: must match the app's directory name under `apps/{app-slug}/` and the frozen app-slug roster maintained at workspace level (per [RULE] Architecture Rules §Y). Immutable for the life of the TDD; if the phase is conceptually re-targeted to a different app, a new TDD is authored under the new app, not the existing one mutated.
- **`phase_number`**: monotonic positive integer starting at `1` per app. Phase 1 = 0→1; Phase N ≥ 2 = additive iteration. Must match the paired PRD's `Phase Number` field (per [TPL] PRD Template §0.7.1). Immutable for the life of the TDD.
- **`Features in this phase`**: enumerates the feature-slugs covered by §4 sub-sections. Must be identical (by set membership and slug spelling) to the paired PRD §7.1 Feature List.

**Discipline note**: `app_slug` and `phase_number` are not metadata. They are commitments that bind this technical design to a specific app and a specific phase of that app's lifecycle. Treat changes to these fields with the same discipline as architectural decisions in §1 and §2.

**No phase-level `assigned_node`**: Unlike feature-level singleton TDDs (the prior ontology), a phase TDD does not declare `assigned_node` in the header. A phase may contain multiple features executing on different nodes; node assignment is recorded per-feature inside `§4.{feature-slug}.Header`. Node assignment workflow is owned by [RULE] Workspace Topology §6.

---

# 2. TDD body — phase-level sections (§1, §2, §3)

## 2.1 §1 Architecture

### 2.1.1 §1 Architecture overview

**Purpose**: One-page technical approach synthesis for the phase as a whole.

**Phase 1 content**: Restatement of the phase 1 problem in technical terms; high-level approach for the foundational architecture; the three tiers as instantiated for this app; key foundational architectural decisions (bulleted, details in `§2.Decision-Record`); high-level sequence or data flow diagram covering the canonical end-to-end across the phase 1 feature set.

**Phase N ≥ 2 content**: Architectural deltas relative to phase-1 baseline. State only what changes (e.g., new tier-3 domain consumed, new external integration introduced, BFF-to-domain Pact convention extended). Reference phase-1 by path. If no architecture delta, state "No architecture deltas; phase-1 architecture applies." in one sentence and proceed to §2.

**What must not appear**: Business justification (paired PRD); per-feature engineering detail (belongs in §4.{feature-slug}); private method structure (belongs in code).

### 2.1.2 §1 Tier responsibility mapping

**Purpose**: At the phase level, declare which capabilities the phase introduces into each tier and how tier boundaries are respected.

**Phase 1 content**: Per tier (Tier 1 / Tier 2 / Tier 3), list capabilities established or materially extended in phase 1; ownership type (primary / collaborating / consuming); why this tier owns it; any deviation with justification.

**Phase N ≥ 2 content**: Tier-level deltas only. Most phases will have no tier mapping change at all; if a Tier 3 domain is newly introduced in this phase, declare it here.

**Anti-pattern**: Business rule logic placed in Tier 1 for convenience. Data permission decisions placed in Tier 2.

### 2.1.3 §1 Phase 1 foundational vs Phase N ≥ 2 deltas

A short subsection (1-3 sentences) at the end of §1 that explicitly states the phase position: "This is Phase 1; foundational architecture is established here." OR "This is Phase 3; deltas only — see §1.1 for the specific deltas; phase-1 TDD at apps/<slug>/specs/tdd/phase-1.md remains the architectural baseline." This explicit framing prevents a reader from misreading deltas as a complete architecture statement.

## 2.2 §2 Cross-feature concerns

The §2 sub-sections cover concerns that apply across all features in the phase and cannot be properly localized to a single `§4.{feature-slug}`. Phase 1 establishes baselines; Phase N ≥ 2 records deltas only.

### 2.2.1 §2 NFR baselines

**Purpose**: Capture phase-level NFR expectations that drive architecture and that all features in this phase must respect.

**Phase 1 content**: Performance (response time, throughput, concurrency ceiling at app scale); availability (SLA targets, graceful degradation strategy); scalability (growth trajectory, horizontal scaling points); maintainability (code ownership, change frequency); security NFR (cross-reference §2.2.2); observability NFR (cross-reference §2.2.3); compliance (regulatory constraints driving architecture); accessibility (project a11y stance per [RULE] Design System Governance §6 — engineering recommendations only; no formal WCAG conformance target; recorded here for completeness).

**Phase N ≥ 2 content**: NFR baseline deltas only. New SLA targets, revised concurrency ceilings, new compliance constraints. If nothing changes, state "No NFR baseline delta; phase-1 baseline applies."

### 2.2.2 §2 Security baseline

**Purpose**: Establish phase-level security stance: authentication and authorization model, data classification, secret management, threat model summary.

**Phase 1 content**: Authentication mechanism (federated identity / token-based / etc.); authorization model (RBAC / ABAC / hybrid); session and token lifecycle; secret management approach (vault, rotation policy); data classification scheme (public / internal / confidential / restricted) and the corresponding handling rules; threat model summary identifying top risks for the phase 1 feature set.

**Phase N ≥ 2 content**: Security baseline deltas only. New threat surfaces introduced by phase-N features, new authorization roles, new data classifications. Otherwise state "No security baseline delta; phase-1 baseline applies."

### 2.2.3 §2 Observability

**Purpose**: Establish phase-level observability standard: metrics, logs, traces, alerting.

**Phase 1 content**: Metric taxonomy (RED / USE / business KPIs and which apply at which tier); log format and retention; trace propagation across tiers; alerting policy (which signals trigger on-call); dashboards expected at phase 1 cutover.

**Phase N ≥ 2 content**: Observability deltas only. New metrics introduced by phase-N features, new alert rules, new dashboards. Otherwise state "No observability delta; phase-1 baseline applies."

### 2.2.4 §2 Deployment and infrastructure

**Purpose**: Establish phase-level deployment topology and environmental commitments. The detailed per-tier-test M0–M5 milestone choreography is owned by [MECH] CI/CD Milestone Policy and not duplicated here; this sub-section captures phase-level commitments only (e.g., "phase-1 introduces a new persistent store; subsequent phases inherit it").

**Phase 1 content**: Environment topology (dev / staging / prod); infrastructure components introduced (databases, queues, caches, gateways, etc.); deployment pattern (rolling / blue-green / canary); release cadence assumption; rollback strategy; data migration approach for phase 1 if applicable.

**Phase N ≥ 2 content**: Deployment and infrastructure deltas only. New infrastructure components, new environments, changed deployment pattern. Otherwise state "No deployment/infrastructure delta; phase-1 baseline applies."

### 2.2.5 §2 Integration boundaries

**Purpose**: Define external systems the phase integrates with and the integration contracts at phase scope.

**Phase 1 content**: External system list. For each: pattern (sync API / async event / batch / webhook); direction of initiation; authentication; error/retry semantics; idempotency guarantees; data transformation rules; SLO/SLA with external owner; owner on their side.

**Phase N ≥ 2 content**: New external integrations only. Existing integrations from phase 1 remain governed by phase-1's spec unless explicitly revised here.

### 2.2.6 §2 Compliance and policy controls

**Purpose**: Identify compliance and policy requirements this phase touches, and where in the architecture they are enforced.

**Phase 1 content**: Applicable external regulations and company-level policy anchors this phase must respect (e.g., GDPR, PIPL, SOC2, industry-specific rules, or company-level policy documents maintained outside this hub); controls implemented in architecture; audit trail requirements; data privacy and classification handling; retention enforcement.

**Phase N ≥ 2 content**: New compliance constraints introduced in this phase only.

**Boundary**: Do not cite `[POL] Digital Solution Policy Architecture Map` or any L2-L5 management-system artifact as a compliance anchor here. Per [OS] §2.3.3, `[POL]` is a Cat 1 source governing the user's team management-system thinking, not an authoritative constraint on the applications the team builds. Compliance anchors must point to external regulations or company-level policy documents directly.

### 2.2.7 §2 Phase-level testing strategy

**Purpose**: Specify phase-level testing approach that drives the phase test plan (master, markdown) and feeds per-feature integration test plans and per-slice test plans.

**Phase 1 content**: Per-tier dominant test types and approximate weight (consistent with [RULE] Claude Code Architecture Rules §6); contract testing approach using Pact convention `{app-slug}-bff_{domain-name}` per Architecture Rules §Y.4 (consumer-driven Pact); integration test strategy (cross-feature scenarios — these populate the phase test plan and feature integration test plans); E2E approach across phase 1 features; visual regression scope baseline (cross-reference per-feature UX Design Spec instance §2.7 when applicable); accessibility testing baseline (cross-reference [RULE] Design System Governance §6 stance plus per-feature UX Design Spec instance §2.5 when slice-specific concerns are declared); performance testing approach (scenarios, SLI/SLO at app scale); security testing scope; test data strategy; determinism and isolation approach.

**Phase N ≥ 2 content**: Testing strategy deltas only. New cross-feature scenario classes, new contract-test pairs, new performance-test scenarios. Plus an explicit regression policy from prior phase: how prior-phase test scenarios are re-executed (subset / full / risk-based) at phase N exit. Otherwise state "No testing strategy delta; phase-1 baseline applies; prior-phase regression: <subset / full / none>."

**Note on test plan derivation**:
- `apps/{app-slug}/specs/test-plan/phase-{N}.md` (master, markdown) is derived primarily from this sub-section + cross-feature scenarios across §4 features
- `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` (feature integration test plan, yaml) for each feature is derived from per-feature §4.{feature-slug} content plus its slice-list
- `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` (slice test plan, yaml) for each slice is derived from this sub-section, the slice's acceptance, and the relevant per-feature §4.{feature-slug}.Module-Decomposition

### 2.2.8 §2 Decision record (phase-level ADR index)

**Purpose**: Index phase-level architectural decisions captured as separate ADR artifacts per `[TPL] ADR Spec`. Per-feature design decisions live inside `§4.{feature-slug}.Open-Questions` or feature-internal commentary; this sub-section captures references to decisions that affect the phase as a whole.

**Phase 1 content**: One index entry per major phase-1 architectural decision (foundational tier choices, persistence strategy, integration patterns, BFF-to-domain Pact convention adoption, etc.). Each index entry: ADR identifier (per ADR Spec §2 naming), short title, current status (per ADR Spec lifecycle: Proposed / Accepted / Superseded / Deprecated), landing path of the ADR artifact (typically `apps/{app-slug}/specs/adrs/{NNNN}-{slug}.md` per ADR Spec §3 landing paths).

**Phase N ≥ 2 content**: One index entry per phase-N architectural decision that is not specific to a single feature. Phase-1 ADRs remain referenced from those phase TDDs; Phase N ≥ 2 TDDs do not re-list them.

**Authoring discipline**: The TDD §2.2.8 sub-section is an **index**, not an embed. ADR content (context, options, decision, consequences, status transitions) lives in the ADR artifact itself per `[TPL] ADR Spec`. When a phase-level decision warrants recording, the operator (or Hub Claude assisting) produces the ADR per ADR Spec, lands it at the appropriate path, and adds the index entry in this TDD's §2.2.8.

**Relationship to [TPL] Options Paper**: For high-stakes decisions, an ADR may follow an Options Paper that compared the candidates; both artifacts may be referenced from the §2.2.8 index entry.

### 2.2.9 §2 Phase 1 baseline vs Phase N ≥ 2 deltas — explicit framing

A short subsection (1-3 sentences) at the end of §2 that explicitly states the phase position: "This is Phase 1; cross-feature baselines are established here for inheritance by subsequent phases." OR "This is Phase 3; cross-feature deltas are recorded above; phase-1 baselines (apps/<slug>/specs/tdd/phase-1.md §2) remain in effect for everything not modified here."

## 2.3 §3 Walking skeleton scope (Phase 1 only)

**Phase 1 only.** Phase N ≥ 2 TDDs do not contain §3.

**Purpose**: Define the thinnest end-to-end vertical slice that proves the foundational architecture (§1) and cross-feature baselines (§2) work together end-to-end through the CI/CD pipeline to production, before any customer-meaningful feature unit in Phase 1 begins execution. The walking skeleton is itself a node-level work unit (`unit_type: walking_skeleton`) per [RULE] Workspace Topology §4 and [MECH] Development Track Workflow §4.0.2; the unit consists of exactly one slice that runs the full M0 → M5 milestone chain. Walking skeleton is **production code, not throwaway prototype** — anchored on Cockburn 2004 *Crystal Clear* and Freeman & Pryce 2009 *Growing Object-Oriented Software, Guided by Tests*, the walking skeleton is shipped to production via M5 in the first or second sprint of Phase 1.

The author of a Phase 1 TDD writes §3 by filling in the six sub-sections below. Sub-sections §3.Purpose, §3.Outputs, §3.Walking-skeleton-first-ordering-rule, and §3.Milestone-choreography-and-acceptance-criteria are largely boilerplate referencing canonical sources; the load-bearing instance-specific authoring happens in §3.Walking-Skeleton-Header and §3.Scope-And-End-To-End-Coverage.

### 2.3.1 §3.Purpose

Fixed text the author copies into the Phase 1 TDD instance:

> Walking skeleton scope establishes the thinnest end-to-end vertical slice that proves the foundational architecture (§1) and cross-feature baselines (§2) work together before Phase 1 feature units begin. The walking skeleton has near-zero customer-visible value but completes the full M0 → M5 milestone chain to `main`, empirically asserting that the CI/CD pipeline is established for this app. The walking skeleton is production code per Cockburn 2004 / Freeman & Pryce 2009 and is shipped to production in the first or second sprint of Phase 1.

### 2.3.2 §3.Walking-Skeleton-Header

The Walking-Skeleton-Header records unit-level metadata for the Phase 1 walking_skeleton unit. The author authors this header during TK-02 alongside per-feature `§4.{feature-slug}.Header` sub-sections. Required fields:

| Field | Value | Source |
|---|---|---|
| `unit_id` | `walking-skeleton` (recommended canonical value per [MECH] Development Track Workflow §3.4 glossary) | Author |
| `unit_type` | `walking_skeleton` | Fixed by ontology |
| `assigned_node` | One of `dev-node-portable`, `dev-node-stationary-1`, `dev-node-stationary-N` per [RULE] Workspace Topology §2.1 | Author (operator pure-judgment per Workspace Topology §6.1 step 1) |
| `prerequisite_units` | `[]` (the walking_skeleton has no prerequisite units in Phase 1) | Fixed by ontology |
| `feature_branch` | `feature/<app-slug>/walking-skeleton` per [RULE] Workspace Topology §5.1 + §6.2 | Fixed by branch namespace convention |
| `phase_number` | `1` (walking_skeleton exists in Phase 1 only per §0.8 asymmetry) | Fixed |
| `paired_prd_section` | Reference to the Phase 1 PRD section that the walking skeleton's slice operationalizes (typically: a representative feature's first scenario, or the first item in PRD §7.1 Feature List) | Author |

The same `unit_id` / `unit_type` / `prerequisite_units` values are mirrored in the GitHub Issue marker block at TK-04 per [RULE] Workspace Topology §6.2; the TDD §3 Walking-Skeleton-Header is the canonical TDD-side record, the GitHub Issue marker block is the canonical GitHub-side record, and the two must remain consistent (consistency is verified at the M0 entry self-check per [MECH] CI/CD Milestone Policy §2.1).

### 2.3.3 §3.Scope-And-End-To-End-Coverage

The author states explicitly which architectural elements the walking skeleton's single slice traverses end-to-end and which are deferred to feature units. The walking skeleton must traverse all three tiers (per [RULE] Claude Code Architecture Rules §1) at minimum, even if minimally; deeper coverage in any tier is an instance-specific choice.

Required content:

- **Tier coverage**: Tier 1 (frontend) / Tier 2 (BFF) / Tier 3 (domain). State for each tier whether the walking skeleton touches it minimally (e.g., one route, one controller, one service call) or more substantively. Walking skeleton MUST touch all three tiers — a walking skeleton that skips a tier does not validate that tier's CI/CD path
- **Persistence path**: state the one representative persistence path the walking skeleton exercises (e.g., a single read or write through the Tier 3 domain service to the chosen persistence backend per [RULE] Claude Code Architecture Rules §Y.4). If the app's Phase 1 architecture (§1) declares no persistence backend, state "No persistence in Phase 1 walking skeleton" with the architectural reason
- **External integration**: if any external integration is in Phase 1 architecture scope (per §2.Integration-Boundaries), state the one representative external integration the walking skeleton exercises; the integration's contract test (Pact pair where applicable per [RULE] Claude Code Architecture Rules §Y.4.4) is in walking skeleton scope. If no external integration is in Phase 1, state "No external integration in Phase 1 walking skeleton"
- **CI/CD pipeline establishment**: the walking skeleton's M5 milestone pass empirically asserts the CI/CD pipeline is established for this app through to staging deploy on `main`. The author does not write per-step CI/CD content (CI/CD is owned by [MECH] CI/CD Milestone Policy); the assertion is implicit in the milestone choreography. The AI-dev environment does not produce production deploys — production deployment is the receiving company's CI/CD responsibility after handoff per [MECH] Application Lifecycle Handoff §0.2

For each of the above, the author also states explicitly **what is deferred** to feature units in the same Phase 1 (e.g., "second-tier 2 endpoint coverage deferred to feature unit `time-off-request`"). This deferred-scope list is the boundary contract between walking_skeleton and Phase 1 feature units.

### 2.3.4 §3.Outputs

The walking skeleton's single PR produces six outputs. The canonical enumeration is owned by [RULE] Workspace Topology §4.6.3; the Phase 1 TDD §3 references that section rather than duplicating the list.

Fixed text the author copies into the Phase 1 TDD instance:

> The walking skeleton produces the six outputs canonically enumerated in [RULE] Workspace Topology §4.6.3:
> 1. `apps/{app-slug}/CLAUDE.md` (app-level Claude Code memory file, lazy-loaded when Claude reads files in this app's subtree)
> 2. `apps/{app-slug}/package.json` (app's own package manifest; Java apps substitute `pom.xml` or `build.gradle` per their toolchain analogue)
> 3. `apps/{app-slug}/{src,specs,tests}/` directory skeleton (with minimal placeholder files)
> 4. `pnpm-workspace.yaml` registration coverage (typically zero-line edit if root yaml uses the recommended `apps/*` glob; one-line append if explicit listing is in use)
> 5. App framework configuration files appropriate to the chosen stack (TypeScript+React: `tsconfig.json` + bundler config + test runner config; Java: `pom.xml` or `build.gradle`; etc. — output #5 is what makes `pnpm install && pnpm build && pnpm test` (or the framework-equivalent commands) succeed for this app inside the monorepo)
> 6. The walking-skeleton end-to-end runnable proof code — the actual slice deliverable, traversing all three tiers per §3.Scope-And-End-To-End-Coverage above
>
> Outputs 1–5 are app scaffolding committed alongside output 6. The single PR for the walking_skeleton unit must contain all six.

The author does not customize this list; the canonical list in [RULE] Workspace Topology §4.6.3 is the single source of truth. Instance-specific elaboration of output #5 (which framework configs apply to this app) and output #6 (what the runnable proof actually exercises) is captured in §3.Scope-And-End-To-End-Coverage above.

### 2.3.5 §3.Walking-skeleton-first-ordering-rule

The walking-skeleton-first ordering rule is owned by [RULE] Workspace Topology §4.6.2.

Fixed text the author copies into the Phase 1 TDD instance:

> The walking skeleton MUST be PR-merged to `main` before any Phase 1 `feature` unit's TK-04 or any Phase 1 `app_integration` unit's TK-08 begins execution per [RULE] Workspace Topology §4.6.2. Hub-side specification work (TK-01 phase PRD, TK-02 phase TDD + per-feature artifacts, TK-03 per-slice intent/acceptance/test-plan) MAY proceed in parallel with walking-skeleton execution. The gate releases at the moment the walking_skeleton's PR is merged to `main` and the M5 staging deploy completes per [MECH] CI/CD Milestone Policy §2.6.

### 2.3.6 §3.Milestone-choreography-and-acceptance-criteria

The walking_skeleton unit runs the full M0 → M1 → M2 → M3 → M4 → M5 milestone chain per the per-unit-type milestone profile in [MECH] CI/CD Milestone Policy §2.0. Per-milestone semantics, automated actions, user-gate requirements, and Codex fire conditions are owned by that source.

The Phase 1 TDD §3 records only **instance-specific acceptance criteria** that augment the per-milestone defaults. Required content:

- **M0 acceptance**: state any walking-skeleton-specific risks beyond the per-slice M0 entry self-check defaults (typically: risks specific to foundational architecture decisions in §1 and cross-feature baselines in §2). The M0 entry self-check is executed at TK-04 entry per [MECH] CI/CD Milestone Policy §2.1; the cross-model adversarial review function is fulfilled at TK-02 sign-off in Hub via the operator's cross-model review reminder per [MECH] Development Track Workflow brownfield reconstruct pre-step. Empty if no such walking-skeleton-specific risks.
- **M2 acceptance**: state which contract test pairs (`{app-slug}-bff_{domain-name}` per [RULE] Claude Code Architecture Rules §Y.4.4) the walking skeleton's slice exercises, and which external integrations (per §3.Scope-And-End-To-End-Coverage above) have integration tests in walking skeleton scope
- **M3 acceptance**: state any walking-skeleton-specific NFR thresholds beyond Phase 1 baselines in §2.2.1 (NFR baselines) (typically: smoke-level latency / availability targets for the end-to-end runnable proof). Empty if §2 baselines apply unmodified
- **M5 acceptance**: state the staging environment in which the walking skeleton lands (the AI-dev side's CI/CD pipeline staging target, not the company-side production environment). The successful M5 staging deploy of the walking skeleton constitutes the empirical assertion that the CI/CD pipeline is established for this app through to staging on `main`

The author does not write per-milestone trigger conditions, gate semantics, or automation steps — those are owned by [MECH] CI/CD Milestone Policy §2 and are uniform across all units of the same unit_type.

## 2.4 §4 Per-feature engineering spec — structure spec

§4 of a phase TDD instance contains one sub-section per feature, named `§4.{feature-slug}` (e.g., `§4.time-off-request`). Each per-feature sub-section follows the fixed internal structure described in §5 of this template (Per-feature sub-section content).

§4 has no §4.0 introductory sub-section; sub-sections begin directly with the first feature's `§4.{feature-slug}`. The order of `§4.{feature-slug}` sub-sections within §4 follows the order of features in the paired PRD §7.1 Feature List.

---

# 3. Section applicability matrix

The matrix uses TDD level (Full / Feature / Lite per §0.3) and phase position (Phase 1 / Phase N ≥ 2) as cross-axes.

| Section | Phase 1 — Full | Phase N ≥ 2 — Full | Phase N ≥ 2 — Feature | Phase N ≥ 2 — Lite |
|---|---|---|---|---|
| §1 Architecture | Required (foundational) | Required (deltas) | Required if any delta | Required if any delta; otherwise one-line "no delta" |
| §2 Cross-feature concerns | Required (full baselines) | Required (deltas only) | Required if any delta | Required if any delta; otherwise one-line "no delta" |
| §3 Walking skeleton scope | **Required (Phase 1 only)** | **Does not exist** | **Does not exist** | **Does not exist** |
| §4.{feature-slug} per-feature spec | Required for each feature | Required for each feature in this phase | Required for each feature in this phase | Required for each feature in this phase |

Per-feature §4.{feature-slug} sub-sections follow their own internal applicability matrix described in §5.

**Anti-pattern**: Including §3 in a Phase N ≥ 2 TDD; omitting §3 in a Phase 1 TDD; including a "phase-2 walking skeleton" (the concept is undefined — by ontology, only Phase 1 has a walking skeleton, since architecture is established once per app).

---

# 4. Writing principles

## 4.1 Primary reader is human; secondary is AI

Write for legibility by a technical reader who has read the paired phase PRD. Prose with structured tables; avoid pure machine-format content. AI reader should also be able to consume, so keep terminology consistent and references explicit.

## 4.2 Decisions, not descriptions

A good TDD captures decisions and rationale. Not a description of every technical object.

## 4.3 Tier and module boundaries are load-bearing

Phase-level architecture (§1) and per-feature module decomposition (§4.{feature-slug}.Module-Decomposition) are load-bearing for downstream work. Invest time in these first.

## 4.4 Link, do not duplicate

Do not restate paired PRD content, Design System Governance content, [RULE] Claude Code Architecture Rules, [MECH] CI/CD Milestone Policy, or prior-phase TDD content. Reference them. The phase TDD captures what is specific to this phase or to a feature in this phase.

## 4.5 MECE check on per-feature modules

Before finalizing each `§4.{feature-slug}.Module-Decomposition`, verify modules are MECE within that feature. Cross-feature MECE is asserted at §1 / §2 level, not by enumerating every module across §4.

## 4.6 Level honesty

If a Lite-level phase TDD is struggling with cross-feature concerns or architecture deltas, level up. Writing a Full TDD for a trivial phase increment is wasteful; writing a Lite TDD for a phase that introduces foundational architecture (which by definition is Phase 1) is dangerous.

## 4.7 Stable-enough before sign-off

The phase TDD does not need to anticipate every implementation detail of every feature in the phase. It needs to be stable enough that:
- The phase test plan (master) can be drafted in TK-02 alongside this TDD
- Each feature's slice-list can be produced
- TK-03 per-slice extraction (Hub-side per `[REF] Hub-CD-CC Architecture` §5.1 content pillar) can begin for any feature whose §4 sub-section is stable

A feature's `§4.{feature-slug}` may finalize after another feature's `§4.{feature-slug}` is already stable enough for TK-03 to start on the latter, as long as cross-feature concerns in §1 / §2 are settled.

## 4.8 App-scoped, phase-scoped, feature-scoped — distinct levels

The phase TDD operates at three nested scope levels:
- **App-scoped, cross-phase additive**: `apps/{app-slug}/specs/openapi.yaml` is a single file accumulated across phases; this TDD's API contracts (per-feature `§4.{feature-slug}.API-Contracts`) feed into it.
- **Phase-scoped**: this TDD itself; phase test plan; phase-1 architectural baseline that downstream phases reference.
- **Feature-scoped**: per-feature §4.{feature-slug}; per-feature slice-list at `apps/{app-slug}/specs/slice-list/{feature-slug}.md`; feature integration test plan; UX Design Spec instances when applicable.
- **Slice-scoped**: per-slice intent / acceptance / test-plan files.

Project-level singletons (`specs/design-system.md` as CC mirror of the CD-side DS instance SOT, `.claude/skills/`, `.claude/agents/`) sit above all of these. Cross-app references are exceptional and should be questioned at MECE-check time per §4.5.

---

# 5. Per-feature sub-section content (`§4.{feature-slug}` internal structure)

Each `§4.{feature-slug}` sub-section in a phase TDD instance follows this fixed internal structure. Sub-sections inside `§4.{feature-slug}` are labeled by purpose (`Header`, `Data-Model`, etc.) rather than numbered, so cross-references to a feature's API contract from another phase remain stable as `phase-N §4.{feature-slug}.API-Contracts`.

## 5.1 §4.{feature-slug}.Header

For each feature, capture the feature-level commitments that vary across features in the same phase:

- `feature-slug` (must match paired PRD §7.1 Feature List entry)
- `feature_phase_role` — one of: `New` (introduced first in this phase) | `Evolves prior-phase feature` (the same feature-slug appeared in a prior phase; this entry covers deltas only) | `Carries-over` (the feature exists from a prior phase but is unchanged in this phase — typically not present in §4, since unchanged features need no entry)
- `assigned_node` — the logical node from [RULE] Workspace Topology §2.1 catalog where this feature's work units execute. Per-feature node affinity (per Workspace Topology §4.2). Recorded once per feature; reassignment follows Workspace Topology §6.3 four-step protocol.
- `tier_1_involved` — boolean. When true, a UX Design Spec instance for this feature is required (authored in CD per `[TPL] UX Design Spec`); the slice's downstream intent.md must include a UX brief plus accessibility test cases per [TPL] Intent and Acceptance Interface Writing Standard §2.3 / §3.9. The TDD itself does not embed UX strategy content; the per-feature UX coverage lives in the UX Design Spec instance.
- Prior-phase feature cross-reference (when `feature_phase_role: Evolves prior-phase feature`): path to the prior phase TDD's `§4.{feature-slug}` sub-section.

## 5.2 §4.{feature-slug}.Data-Model

**Purpose**: Define core entities, relationships, persistence boundaries for this feature.

**Content**: Core entities (class-level, not table-level); attributes (logical, not physical columns); relationships; persistence tier; lifecycle states and transitions; data retention; reference to global master data if applicable. For features evolving from prior phases (`feature_phase_role: Evolves prior-phase feature`), state only the data-model deltas relative to the prior phase's data model.

**What must not appear**: DDL, indexing strategy, physical column constraints — these belong in code or in a domain package's internal design.

## 5.3 §4.{feature-slug}.API-Contracts

**Purpose**: Define this feature's contribution to the app's API surface at stable-enough detail for contract testing and OpenAPI accumulation.

**Content**: API list (endpoint, consumer tier, producer tier); request/response shapes; error model; authentication/authorization model (referencing phase §2.Security-Baseline); idempotency/retry expectations; pagination/streaming; versioning strategy.

**Note on OpenAPI**: TDD specifies API at semantic level; the app-scoped, cross-phase additive `apps/{app-slug}/specs/openapi.yaml` captures the syntactic spec accumulated across phases. New APIs introduced by this feature are added to that file; existing APIs evolved by this feature update their entries in that file. Both must stay consistent.

**Note on contract testing**: API contracts here drive consumer-side Pact contract test pair `{app-slug}-bff_{domain-name}` per [RULE] Architecture Rules §Y.4 (consumer-driven Pact convention). Identify which APIs cross the BFF-to-domain boundary so the slice-list (§5.5) and downstream test plans correctly scope contract test cases.

## 5.4 §4.{feature-slug}.Module-Decomposition

**Purpose**: Decompose this feature into modules that serve as both architectural building blocks and slice identity anchors.

**Content**: Module list per tier. For each module: name (module-slug, kebab-case); responsibility (one sentence); public interface; internal boundary; inter-module dependencies. MECE check statement confirming modules are mutually exclusive and collectively exhaustive for the feature scope (within this phase — features evolving across phases have MECE checked per phase).

**Domain module references** (Tier 3, per [RULE] Architecture Rules §Y.4 Model B):

When this feature requires Tier 3 capability, reference the relevant `packages/domain/{domain-name}/` package(s). Three cases:

1. **Existing domain consumed unchanged**: list the consumed domain and the specific Tier 3 module(s) within it that this feature uses. No domain extension required. The app's BFF (Tier 2) authors a Pact consumer contract per Architecture Rules §Y.4.4.
2. **Existing domain extended for this feature**: identify the existing domain and describe the additive extension. The extension is scheduled as a feature-driven domain change per Architecture Rules §Y.4.3 — within the slice or as an independent slice, at operator discretion. Domain versioning per Architecture Rules §Y.4.5 applies.
3. **New domain introduced**: a new `packages/domain/{domain-name}/` is created when the first consumer feature genuinely requires it (no speculative domain modeling). The TDD must justify why the capability does not fit an existing domain.

Cross-app domain reuse: if a domain is already consumed by another app (per Architecture Rules §Y.4.3), this feature evaluates and reuses the existing domain rather than creating a parallel one. Domain duplication for substantially the same business capability is an anti-drift signal per Architecture Rules §8.

**Slice-size advisory check**:

After module decomposition, verify that the resulting slices respect the soft upper limits declared in [MECH] CI/CD Milestone Policy §2.7:

- Source files touched per slice (across `apps/{app-slug}/src/**` + `packages/domain/{domain-name}/src/**`): ≤10
- Net lines of code added per slice: ≤500

If a planned slice exceeds either limit, either (a) split the slice further within the slice-list, or (b) declare the oversize explicitly in this sub-section with rationale and accept the M4 conditional manual review gate. The advisory is operator-judged at M4, not auto-blocking — but a feature's module decomposition should not silently produce oversized slices.

> **v0 assumption — to be calibrated per [MECH] CI/CD Milestone Policy §2.7**: The 10-files / 500-LOC heuristics are starting points; first-feature lessons-harvest may revise them.

**Relationship to slicing**: Slices are typically composed of one or a small group of modules. A slice should not span more modules than can be implemented in one PR.

**Relationship to slice-list**: §5.5 below defines the paired `apps/{app-slug}/specs/slice-list/{feature-slug}.md` file content, which is the operational expression of this feature's module-to-slice mapping.

## 5.5 §4.{feature-slug}.Slice-List

**Purpose**: Define the minimum content of the paired `apps/{app-slug}/specs/slice-list/{feature-slug}.md` file, which is produced in TK-02 alongside this phase TDD and consumed by TK-03 per-slice artifact production. Per-slice selection and splitting rules are owned by [TPL] PRD + TDD to Intent and Acceptance Conversion Specification §2; this sub-section owns only the file-level structure of the list itself.

**File-level header** (the slice-list file must start with):
- `app_slug` (must match this TDD's `app_slug`)
- `feature_slug` (must match this `§4.{feature-slug}` entry)
- `phase_number` (must match this TDD's `phase_number`)
- Source phase TDD reference (file path + version or commit) — `apps/{app-slug}/specs/tdd/phase-{N}.md`
- Source phase PRD reference (file path + version or commit) — `apps/{app-slug}/specs/prd/phase-{N}.md`
- `assigned_node` (must match this `§4.{feature-slug}.Header.assigned_node`)
- Slice count
- Last updated date

**Per-slice entry** (one entry per slice; the list must be exhaustive for this feature's in-scope functional requirements at this phase TDD level):
- `slice_id` (per Development Track Workflow §3.3 placeholder format: `{feature-slug}-{slice-seq}-{slice-name}`; kebab-case; stable once created)
- `slice-seq` (zero-padded two-digit sequence, e.g., `01`, `02`; reflects production order, not execution order)
- Single business objective statement (one sentence, traceable to paired phase PRD §7 feature spec; enforces the TK-02 completion criterion "slices are single-objective")
- `tdd_modules_covered` (list of module-slugs from `§4.{feature-slug}.Module-Decomposition`)
- `tiers_covered` (subset of `{tier-1, tier-2, tier-3}`)
- `tier_1_involved` (boolean; when true, the downstream slice's intent.md must include a UX brief and test-plan.yaml must include `test_type: accessibility` cases per [TPL] Writing Standard §2.3 and §3.9)
- `domains_consumed` (list of `{domain-name}` from `packages/domain/` if any; supports Pact pair scoping per Architecture Rules §Y.4)
- Paired PRD scenarios covered (by scenario ID from PRD §4.2)
- Dependencies on other slices, if any (by slice_id); cross-feature slice dependencies must be flagged here
- Production order rationale (if slices must be produced in a specific order to satisfy dependencies)
- Estimated slice scope (file count + net LOC) per the §5.4 slice-size advisory check; flagged-as-oversized when the estimate exceeds [MECH] CI/CD Milestone Policy §2.7 limits

**Relationship to Conversion Spec**: The fields above align with the per-slice metadata that [TPL] Conversion Spec §2.4 requires each extracted slice to record. The slice-list file is where that metadata lives before TK-03 extraction begins.

**MECE check statement**: The list must include a short assertion confirming that the slice set is mutually exclusive (no two slices cover the same paired-PRD scenario without explicit stagger rationale) and collectively exhaustive for this feature's in-scope paired-PRD scenarios at this phase.

**What must not appear**: Implementation-level detail (which files to edit, which methods to add) — that is engineering design, not slice planning. Per-slice UX screen inventories — that belongs in intent.md UX brief. Test case lists — that belongs in test-plan.yaml.

## 5.6 §4.{feature-slug}.Domain-Class-Hierarchy

**Purpose**: For Tier 3 modules carrying business rule logic for this feature, specify the class hierarchy that structures the business rules.

**Content** (Full-level only, typically): Key abstract classes/interfaces; inheritance and composition relationships; rule placement (which class enforces which invariant); transaction boundaries; auditing responsibilities; permission decision ownership at class level.

**Domain package context**: When the feature consumes a `packages/domain/{domain-name}/` package per §5.4, the class hierarchy is scoped to that domain package. New abstract classes / interfaces introduced as part of a domain extension should be reflected in the domain's `CLAUDE.md` (per [RULE] Architecture Rules §4.5) at TK-12 merge time.

**What must not appear**: Implementation method signatures; framework-specific annotations.

## 5.7 §4.{feature-slug}.Open-Questions

**Purpose**: Capture feature-specific questions that remain after TDD drafting but do not block current-phase implementation. Phase-level open questions (cross-feature) belong in `§2.Decision-Record` as proposed-status entries instead.

**Content**: One entry per question: question statement; why open (information needed, expertise needed, time-bound dependency); when to be resolved (which slice, milestone, release); responsible party if known.

**Anti-pattern**: Using this section to defer business-rule questions that actually block this feature's slice extraction. Such questions should bounce back to the phase PRD as open issues.

## 5.8 Per-feature sub-section applicability matrix

| Per-feature sub-section | When required |
|---|---|
| `Header` | Always |
| `Data-Model` | When the feature has persistent state of its own (most features) |
| `API-Contracts` | When the feature exposes or modifies any API surface |
| `Module-Decomposition` | Always |
| `Slice-List` | Always (feature is delivered through slices) |
| `Domain-Class-Hierarchy` | When the feature's Tier 3 module(s) carry non-trivial business rule logic |
| `Open-Questions` | Optional — present only when there are open feature-specific questions |

A `UX-Strategy` sub-section is intentionally **not** part of the per-feature TDD content. When `Header.tier_1_involved` is true, the feature's UX coverage lives in a separate UX Design Spec instance authored in CD per `[TPL] UX Design Spec` — outside the TDD body. See §0.4 boundary for ownership clarity.

A feature with `feature_phase_role: Evolves prior-phase feature` records only the deltas in each sub-section; sub-sections with no deltas may state "No delta from prior phase; see apps/<slug>/specs/tdd/phase-<M>.md §4.<feature-slug>.<Sub-section>." and proceed.

---

# 6. Cross-source boundary

The phase TDD is bounded by adjacent canonical sources. Content that belongs in these sources should not appear in the TDD.

| Content type | Correct source |
|---|---|
| Business rules, user value, scenarios, phase scope, feature list | Paired phase PRD |
| Per-slice execution boundary in business language | intent.md |
| Per-slice test case design | slice test-plan.yaml |
| Per-feature cross-slice flow tests | feature integration test-plan.yaml |
| Phase-level cross-feature test scenarios; phase exit criteria; app-scale NFR targets; regression policy from prior phase | phase test plan (master, markdown) |
| Project-level design system foundation (not phase- or feature-specific) | Design System Governance — governance rules in this hub; DS instance content (tokens, components, layout patterns) lives in CD as SOT with CC mirror at `specs/design-system.md` per DSG §1.1 |
| Per-feature UX coverage (affected Tier 1 scope, components from DS instance, new-asset additive update plans, layout patterns, slice-specific a11y, i18n/RTL call-outs, visual regression anchors, responsive/motion expectations) | UX Design Spec instance (CD-authored per `[TPL] UX Design Spec`); reviewed in Hub against reviewer checklist; consumed in CC at slice authoring |
| Implementation-level detail (private methods, framework annotations, file organization inside a module) | Code, with module-level doc if needed |
| Branch topology, node assignment mechanics, phase boundary parallelism phrasing | [RULE] Workspace Topology |
| TK-by-TK orchestration | [MECH] Development Track Workflow |
| Milestone gate semantics | [MECH] CI/CD Milestone Policy |
| Domain lifecycle and Pact convention | [RULE] Architecture Rules §Y.4 |
| Walking skeleton unit definition (full output set, ordering rule, milestone profile) | [RULE] Workspace Topology §4.6 (output set §4.6.3, ordering rule §4.6.2) / [MECH] Development Track Workflow §4.0 (unit_type catalog) / [MECH] CI/CD Milestone Policy §2.0 (per-unit-type milestone profile) |

The phase TDD captures phase-level architecture decisions, phase-level cross-feature concerns, and per-feature engineering design at a level above implementation and below business intent.

---

# 7. Pairing rules and consistency

## 7.1 Pairing with phase PRD

Phase TDD and phase PRD are paired 1:1 (one PRD ↔ one TDD per phase per app). When either changes substantively:
- Phase PRD scope changes (feature added / removed / re-scoped) → phase TDD §4 sub-sections updated; phase test plan re-verified
- Phase PRD new NFR → phase TDD §2.2.1 (NFR baselines) and §2.2.7 (Phase-level testing strategy) updated
- Phase PRD new user flow within a feature → that feature's UX Design Spec instance updated (CD-side authoring); TDD `§4.{feature-slug}.Header.tier_1_involved` flag re-verified if user flow changes Tier 1 involvement
- Phase TDD architecture change constraining business behavior → surface back to phase PRD for approval; do not silently change business surface inside TDD

## 7.2 Pairing with Design System Governance and UX Design Spec

The TDD per-feature `§4.{feature-slug}.Header.tier_1_involved: true` declaration is what binds this TDD to the DSG ecosystem. The TDD itself does not author UX strategy content; the UX Design Spec instance (authored in CD per `[TPL] UX Design Spec`) carries that content. When either changes:
- Design System Governance additive update (new component / token added to instance) → in-flight features may reference the new asset by authoring it into the UX Design Spec instance §2.3, no TDD modification required
- Design System Governance breaking change → all in-flight features touching Tier 1 must re-verify their UX Design Spec instance and may need TDD `§4.{feature-slug}` review if the breaking change invalidates the feature's data model or API surface (rare); typically the impact is contained to UX Design Spec instances
- UX Design Spec instance §2.4 new-component / new-token plan → triggers DS instance update flow per DSG §12 at the originating feature's merge-to-main milestone; TDD `§4.{feature-slug}` is unchanged by this flow
- TDD `§4.{feature-slug}.Header.tier_1_involved` flag change (false → true or true → false) → the UX Design Spec instance authoring path is opened or closed; this is a per-feature TDD revision triggering downstream UX Design Spec lifecycle action

## 7.3 Pairing with downstream slice artifacts

Phase TDD is upstream of intent, acceptance, slice test-plan per slice (and feature integration test plan per feature). When phase TDD changes materially:
- Existing slices in any feature in this phase may need re-slicing
- Slice `Must not break` items tied to API contracts may need revision
- Slice `data_expectations` tied to data model may need revision
- Slice intent.md UX brief may need revision

## 7.4 Pairing with phase test plan (master, markdown)

The phase test plan at `apps/{app-slug}/specs/test-plan/phase-{N}.md` is paired 1:1 with this phase TDD. Both produced in TK-02. Phase TDD §2.2.7 (Phase-level testing strategy) provides strategy and cross-feature scenario classes; the phase test plan instantiates them with specific scenarios, owners, and exit criteria.

## 7.5 Pairing with feature integration test plans

Each `apps/{app-slug}/specs/test-plan/feature-{feature-slug}.yaml` is paired with one `§4.{feature-slug}` sub-section of this phase TDD. The feature integration test plan covers cross-slice flow tests within the feature; its content is derived from `§4.{feature-slug}.Module-Decomposition`, `§4.{feature-slug}.API-Contracts`, and the paired PRD §4.2 scenarios attributed to this feature.

## 7.6 Pairing with prior-phase TDD (Phase N ≥ 2 only)

A Phase N ≥ 2 TDD references its prior-phase TDD (typically phase-{N-1}, but may reference earlier phases for baseline). When a prior-phase TDD is materially revised:
- The current-phase TDD's delta statements (§1, §2 deltas; per-feature evolved-from-prior deltas) must be re-verified for continued validity
- If the prior-phase TDD revision invalidates the basis for a current-phase delta, surface a phase boundary parallelism warning per [RULE] Workspace Topology — this is exactly the case the warning system covers

---

# 8. Minimal Lite phase TDD template

Use this minimal template only for a Phase N ≥ 2 TDD that introduces no architectural delta and adds a single small feature.

```markdown
# [TDD] <App Display Name> — Phase <N>

- **app_slug**: <app-slug>                      [MANDATORY]
- **phase_number**: <N>                         [MANDATORY; N ≥ 2 for Lite-level phase TDD]
- **TDD level**: Lite
- **Status**: Active
- **Paired PRD reference**: apps/<app-slug>/specs/prd/phase-<N>.md
- **Prior phase TDD reference**: apps/<app-slug>/specs/tdd/phase-<N-1>.md
- **Design System Governance instance reference**: v<x.y.z> (DS instance content lives in CD as SOT with CC mirror at `specs/design-system.md` per DSG §1.1) [only if Tier 1 touched in §4]
- **Author**: <you>
- **Features in this phase**: <single feature-slug>

## §1 Architecture
No architecture delta; phase-1 baseline at apps/<app-slug>/specs/tdd/phase-1.md applies.

## §2 Cross-feature concerns
No cross-feature delta; phase-1 baselines apply. Prior-phase regression: <subset / none>.

## §4.<feature-slug>

### §4.<feature-slug>.Header
- feature-slug: <slug>
- feature_phase_role: New | Evolves prior-phase feature
- assigned_node: <logical-node-name>
- tier_1_involved: <true|false>   [if true, a UX Design Spec instance is authored in CD per [TPL] UX Design Spec — not embedded in this TDD]
- prior-phase reference (if evolves): apps/<app-slug>/specs/tdd/phase-<M>.md §4.<slug>

### §4.<feature-slug>.API-Contracts (if any)
<API list with request/response shape and error model>
Pact pair (if applicable): <{app-slug}-bff_{domain-name}>

### §4.<feature-slug>.Module-Decomposition
<module list, 1-3 modules typically for Lite>
Domain references (if any): <packages/domain/{domain-name}/>
Slice-size advisory check: <within limits / oversize-justified>

### §4.<feature-slug>.Slice-List
<slice entries per §5.5>

### §4.<feature-slug>.Open-Questions (optional)
<if any>
```

A Lite phase TDD that begins to feel cramped should be levelled up to Feature.

---

# 9. Reviewer checklist

Before signing off a phase TDD, verify:

1. **Header mandatory fields populated**: `app_slug`, `phase_number`, `Features in this phase` all present and well-formed (per §1)
2. **Phase / level coherence**: TDD level matches phase position (Phase 1 → Full; Phase N ≥ 2 → Full / Feature / Lite per §0.3 rule); no Lite-for-foundational-architecture mismatch
3. **§4 feature set matches paired PRD §7.1**: identical feature-slug set; no orphan §4 sub-sections; no unaccounted-for PRD features
4. **§3 presence rule honored**: §3 Walking skeleton scope present if Phase 1; §3 absent if Phase N ≥ 2
5. **§3 content quality (Phase 1 only)**: Walking-Skeleton-Header populated with valid `unit_id`, `assigned_node` from [RULE] Workspace Topology §2.1 catalog, `prerequisite_units: []`, `feature_branch: feature/<app-slug>/walking-skeleton`, `phase_number: 1`, `paired_prd_section`; Scope-And-End-To-End-Coverage explicitly states all three tiers + persistence path + external integration (or explicit "no external integration" / "no persistence" rationale) + deferred-scope list demarcating walking_skeleton vs Phase 1 feature unit boundaries; Outputs section is the canonical-reference text (does not duplicate the [RULE] Workspace Topology §4.6.3 list); Walking-skeleton-first-ordering-rule and Milestone-choreography-and-acceptance-criteria reference their canonical owners
6. **Phase 1 vs Phase N ≥ 2 explicit framing present**: §2.9 (Phase 1 baseline vs Phase N ≥ 2 deltas — explicit framing) clearly states phase position
7. **§1 / §2 delta vs baseline coherence**: in Phase N ≥ 2, deltas are deltas, not full restatements; reference to phase-1 TDD path is present
8. **Per-feature §4.{feature-slug} sub-section structure**: `Header` / `Module-Decomposition` / `Slice-List` always present; when `Header.tier_1_involved: true`, a corresponding UX Design Spec instance has been authored in CD per `[TPL] UX Design Spec` and reviewed in Hub against that template's §3 reviewer checklist (the UX Design Spec instance is a separate artifact, not a sub-section of this TDD); sub-section ordering is consistent across features
9. **Per-feature module decomposition MECE within feature scope**
10. Tier responsibility mapping in §1 respects [RULE] Claude Code Architecture Rules §1
11. **Domain references in `§4.{feature-slug}.Module-Decomposition` follow [RULE] Architecture Rules §Y.4 Model B**: existing-domain reuse evaluated before new-domain creation; cross-app domain duplication avoided
12. **Slice-size advisory check completed in each `§4.{feature-slug}.Module-Decomposition`**: planned slices within [MECH] CI/CD Milestone Policy §2.7 limits, or oversize justified
13. API contracts in each `§4.{feature-slug}.API-Contracts` sufficient for OpenAPI accumulation and contract testing; Pact pair `{app-slug}-bff_{domain-name}` identified for each BFF-to-domain boundary
14. **Phase-level testing strategy in §2 covers**: per-tier dominant test types; cross-feature scenarios that drive phase test plan; regression policy from prior phase (Phase N ≥ 2 only)
15. **Per-feature node assignments in `§4.{feature-slug}.Header.assigned_node`** all from valid logical-node catalog
16. Compliance and policy controls in §2 (if applicable) reference valid external regulations or company-level policy documents, not `[POL]` or L2-L5 management-system artifacts
17. Integration boundaries in §2 (if applicable) have named external owners
18. Data model decisions in each `§4.{feature-slug}.Data-Model` are logical, not physical
19. Domain layer class hierarchy (if applicable) places invariants correctly
20. **§2.2.8 ADR index entries** (if any) reference ADR artifacts authored per `[TPL] ADR Spec` and landed at the appropriate path; phase-level decision content is in the ADR artifacts, not embedded in §2.2.8
21. Open questions do not hide blocking business ambiguities (escalate to phase PRD instead)
22. No content belongs in phase PRD, intent, acceptance, slice test-plan, feature integration test-plan, phase test plan, Design System Governance, UX Design Spec instances, or code instead of TDD
23. Phase TDD stable enough that TK-03 can proceed for any feature whose `§4.{feature-slug}` is finalized
24. **For each feature with `Header.tier_1_involved: true`**: a UX Design Spec instance has been authored (CD-side) per `[TPL] UX Design Spec` and reviewed in Hub against that template's §3 reviewer checklist; instance is paired with this TDD's `§4.{feature-slug}` by feature-slug match
25. **For each feature declaring new components or tokens in its UX Design Spec instance §2.4**: additive-update plan is complete and defensible per [RULE] DSG §12 change content structure
26. **For each feature declaring slice-specific a11y considerations in its UX Design Spec instance §2.5**: they are written as concrete concerns (not generic restatements of DSG §6.1 recommendations), with optional verification path noted (manual smoke test, on-demand SK-W audit, or eslint-plugin-jsx-a11y warning)
27. **All file-path references use `apps/{app-slug}/` prefix or `phase-{N}` / `feature-{feature-slug}` / `{slice-id}` scoping per §4.8**, except project-level singletons (`specs/design-system.md` as CC mirror, `.claude/`)

If 2+ items are materially weak, the phase TDD is not yet ready for sign-off.
