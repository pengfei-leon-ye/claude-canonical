# [RULE] Claude Code Architecture Rules

- **Project**: HR Digital Cockpit
- **Document Type**: Architecture Specification
- **Status**: Active canonical
- **Role**: Stable declaration of the three-tier code architecture for Claude Code projects, the Tier 2 thinning rule, permission decision placement principle, the existence of the CLAUDE.md hierarchy (defers to [REF] Hub-CD-CC Architecture constitutional residue), the existence of subagent topology and context scope mechanisms, and the high-level monorepo structure that hosts Cat 4 implementation. Substantive operational rules (specific tier-internal tool choices, the specific subagent roster (membership, count, identifiers) with permissions, specific repository path patterns and lint rules, specific skill catalog, agent context scope configurations) are owned by CC under its own substantive canonical.
- **Source Category**: Cat 4
- **Management-System Role**: Architecture specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within [OS] §7.1 routing; subject to [OS] §8.5 paired-update consistency. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side residue carries the constitutional skeleton declared here; CC-side substantive canonical owns the operational implementation details.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §5 (management mechanism over ad hoc control) to tier separation as a constitutional architectural mechanism rather than ad-hoc structural choice.
- **Relationship to [REF] Hub-CD-CC Architecture**: Tier architecture operates inside the CC workspace. This Hub residue is the constitutional declaration that Hub-authored TDDs and handoff documentation consume. §4 below references this source for the existence of the CLAUDE.md hierarchy; the tier separation declared here is what that hierarchy aligns to.
- **Relationship to [RULE] Workspace Topology**: Companion constitutional residue. Tier separation (this source) is orthogonal to multi-node deployment (WT). The two together define the CC workspace's architectural shape.
- **Relationship to [RULE] Design System Governance**: Tier 1 design constraint references DSG; the constitutional invariant that Tier 1 adheres to the project DS is declared here. Specific DSG enforcement mechanics are at DSG itself.
- **Relationship to [MECH] Development Track Workflow**: Companion. TK orchestration consumes the tier separation declared here to assign work scope per tier.
- **Relationship to [MECH] CI/CD Milestone Policy**: M-gates execute against the tier architecture declared here. M2 contract testing leverages the Tier 2-Tier 3 seam.
- **Relationship to [MECH] Application Lifecycle Handoff**: Handoff readiness includes tier-correct implementation completeness against the tier architecture declared here.
- **Pairings I participate in**: None. This Hub-side residue participates in no static pairings; its couplings to the CC-side substantive canonical and to [RULE] Workspace Topology are Tier B couplings documented in the `Relationship to …` header fields above per [OS] §8.5.1a.

## How to use this source (Hub-side)

Use this source when:
- Authoring Hub-side TDDs or handoff documentation that references Tier 1 / Tier 2 / Tier 3
- Reasoning about tier-correct placement of cross-workspace deliverables
- Confirming the Tier 2 thinning rule when scoping a feature unit's TDD
- Confirming the permission decision placement principle at the cross-workspace specification level

Do not use this source as:
- A specific tier internal tooling reference (CC substantive)
- A subagent roster catalog with specific identifiers and permissions (CC substantive)
- A repository layout reference for specific path patterns (CC substantive)
- A skill catalog (CC substantive)
- An agent context scope configuration reference (CC substantive)
- An anti-drift reference at the operational level (CC substantive)

---

# 0. Boundary and position

## 0.1 What this source owns (constitutional)

- Three-tier code architecture: identity and role of Tier 1 (React Frontend), Tier 2 (Node/TS BFF), Tier 3 (Java Domain Services)
- Tier 2 thinning rule (constitutional design rule for simple applications)
- Permission decision placement principle (where in the tier stack permission logic resides)
- The existence of subagent topology and context scope mechanisms (cross-workspace handoff documentation references "the CC subagent layer" as a concept)
- The existence of the monorepo structure with `apps/` and `packages/domain/` separation (the high-level structure Hub-authored TDDs reference by path)
- The Tier 2 ↔ Tier 3 seam as Pact contract testing boundary (constitutional interface)
- Domain identity decoupling from app identity (cross-cutting constitutional rule)

## 0.2 What this source does not own

- Tier 1 internal: specific React framework version, specific UI library, specific routing approach (CC substantive)
- Tier 2 internal: specific Node version, specific TypeScript configuration, specific BFF implementation patterns (CC substantive)
- Tier 3 internal: specific Java version, specific Spring framework version, specific persistence approach (CC substantive)
- Subagent roster: individual subagent definitions, permission sets (CC substantive)
- Named context scopes: `business_rules_only`, `api_contracts`, `code_whitebox` etc. and their configuration schemas (CC substantive)
- Context scope enforcement mechanics (CC substantive)
- Repository layout: path patterns within the tier-anchoring directories, frozen-name rules, what-must-not-be-in-the-repository details (CC substantive). The tier-anchoring paths themselves (`apps/{app-slug}/src/frontend|bff/`, `packages/domain/{domain-name}/`) are constitutional location references — see §1, §6
- Domain rules: identity naming, boundary specifics, lifecycle model B specifics, contract testing Pact convention specifics, versioning rules (CC substantive)
- Skill catalog: SK-F, SK-W, and per-skill load triggers (CC substantive)
- Anti-drift signals at the operational level (CC substantive)

---

# 1. Three-tier architecture (constitutional)

**Terminology note**: Tier 1 / Tier 2 / Tier 3 in this source refer exclusively to the code-layer architecture of Claude Code projects. They are deliberately distinct from the L1-L5 management-system lens defined in [OS] §4.2. The management-system lens is a governance-design construct used to place policies, process maps, and SOPs; the three-tier code architecture is an implementation-structure construct used inside Claude Code projects. The two should not be confused during design-to-code handoff or in any CLAUDE.md authoring work.

The CC workspace's code is organized into three tiers. Each tier has constitutional identity and high-level role; tier-internal substantive content (specific tools, frameworks, patterns) is owned by CC substantive canonical.

## 1.1 Tier 1 — React Frontend

**Role identity**: Presentation layer. Owns pages, components, user interaction state, frontend routing, presentation-layer display logic, adherence to project Design System Governance.

**Constitutional position**: The frontend tier of the three-tier architecture; consumes Tier 2 BFF; never consumes Tier 3 directly.

**Physical placement (constitutional reference)**: `apps/{app-slug}/src/frontend/**` — this path pattern is the constitutional location reference consumed by Hub-authored TDDs.

**Design constraint**: Tier 1 code must adhere to the project Design System per [RULE] Design System Governance. CC substantive canonical owns the enforcement mechanism (skill-based runtime enforcement, deviation process).

## 1.2 Tier 2 — Node / TypeScript Experience Orchestration Layer (Thin BFF)

**Role identity**: Orchestration layer. Owns scene-facing APIs, aggregation across domain services, DTO transformation, frontend-specific validation and orchestration, session context handling.

**Constitutional position**: The middle tier between presentation (Tier 1) and domain (Tier 3); both directions of the tier seam are owned by this tier.

**Physical placement (constitutional reference)**: `apps/{app-slug}/src/bff/**` — constitutional location reference.

## 1.3 Tier 3 — Java Domain Services Layer

**Role identity**: Authoritative business layer. Owns business capability boundaries, domain rules, transactions, auditing, stable external service contracts.

**Constitutional position**: The authoritative tier; owns the business state. Consumed by Tier 2; not directly consumed by Tier 1.

**Physical placement (constitutional reference)**: `packages/domain/{domain-name}/**` — constitutional location reference. **Domain identity is decoupled from app identity** (constitutional rule): a domain may serve one or more consumer apps over its lifecycle.

---

# 2. Tier 2 thinning rule (constitutional design rule)

Simple applications may thin the Tier 2 layer when full orchestration logic is not justified, **but the three-tier structure must be preserved**.

**Thinning rubric** — thinning is permitted only when all of the following hold:
- the slice's Tier 2 work is exhausted by DTO mapping and API gateway pass-through — no cross-domain aggregation, no scene-specific business orchestration, no session-derived decision logic
- each frontend call maps to a single domain-service call (one-to-one), so Tier 2 adds no composition
- no frontend-specific validation or transformation beyond shape mapping is required

If any item fails, Tier 2 carries its normal orchestration responsibilities and must not be thinned.

**Approved pattern**: Tier 2 retained as a thin BFF layer that performs only DTO mapping and API gateway duties, while Tier 1 and Tier 3 carry their normal responsibilities.

**Example pair**:
- *Compliant thinning*: a single-domain reference-data lookup feature where each Tier 1 request maps one-to-one to one Tier 3 read and Tier 2 only reshapes the DTO — Tier 2 is retained as a thin pass-through BFF.
- *Non-compliant thinning*: a dashboard feature that aggregates data from three domain services and applies role-derived display rules — collapsing this into a pass-through Tier 2 (or into Tier 1) violates the rule, because real cross-domain orchestration exists and belongs at Tier 2.

**Constitutional invariant**: Do not remove Tier 2 entirely. Even in simple applications, retain Tier 2 as a thin BFF to preserve architectural evolution space and prevent DTO leakage into Tier 1.

Rationale (constitutional reasoning that propagates to cross-workspace decisions):
- prevents Tier 1 from absorbing backend contract knowledge that belongs outside the presentation layer
- preserves a stable seam for later enrichment (session handling, caching, aggregation) without refactoring Tier 1
- keeps permission decision placement (§3) clean across tiers
- preserves the BFF as the consumer side in the domain contract testing pair — removing Tier 2 would erase the Pact consumer that drives domain producer verification

CC substantive canonical owns the operational guidance for implementing a thin BFF (specific patterns, code samples).

---

# 3. Permission decision placement (constitutional principle)

Permission decisions must be separated by type. The constitutional principle:

- **Data permissions** (who can read/write what business state) reside at Tier 3 (Java Domain Services Layer). Tier 3 enforces data-access permissions because Tier 3 owns the business state.
- **Functional permissions** (who can invoke what app feature) split by ownership: the **app-specific portion** — whether a given user may invoke a given app feature in the context of one app's feature surface — resides at Tier 2 (Node BFF), because Tier 2 is the app-orchestration layer that owns the app's feature surface; the **authoritative source of permission identity** (role and grant definitions) resides at Tier 3, because Tier 3 owns the business state those grants are bound to. The boundary: Tier 2 decides app-feature invocability against identity it does not itself author; Tier 3 authors and owns the identity.

This separation prevents Tier 1 from holding permission decision logic (a Tier 1 that "knows what user can do" leaks domain authority into presentation). Hub-authored TDDs must respect this placement at the specification level.

Specific permission tooling, enforcement libraries, and audit mechanisms are CC substantive.

---

# 4. CLAUDE.md file hierarchy

The CC workspace uses a tier-aligned CLAUDE.md hierarchy. The hierarchy's existence and tier-alignment is declared in [REF] Hub-CD-CC Architecture constitutional residue; the specific paths, "must reference" lists, and authoring authority per level are substantive detail owned by the CC-side substantive canonical.

This source declares only the constitutional claim: a project-root CLAUDE.md and per-tier CLAUDE.md files exist, tier-aligned to the three-tier architecture in §1; the specific path set is owned by the CC-side substantive canonical.

Substantive content (must-reference lists, authoring authority, cross-level navigation discipline) is owned by the CC-side substantive canonical.

---

# 5. Subagent topology (constitutional)

The CC workspace operates a **subagent topology**: parts of the TK chain are executed by named subagents, each with a defined context scope and permission set. The topology's existence is constitutional (cross-workspace handoff documentation references "subagents" as a concept; specific subagent invocations may be referenced in Hub-authored test plans via subagent identifiers).

**Constitutional invariants**:
- A subagent roster exists at CC (CC substantive canonical owns the specific roster — its membership, count, and per-subagent definitions)
- Each subagent has a defined context scope (CC substantive canonical owns the scope catalog and configurations)
- Subagent invocations are recorded at handoff
- Subagent bias firewall principle: subagents do not share context with each other unless their roles authorize the cross-flow (CC substantive canonical implements the firewall)

**What this source does not declare**: specific subagent identifiers and names, the roster size, subagent definition file paths, context scope configurations, permission grant mechanisms — all CC substantive.

---

# 6. High-level monorepo structure (constitutional)

The CC workspace organizes code in a **monorepo with apps/ and packages/domain/ separation**. The per-tier path anchors (`apps/{app-slug}/src/frontend|bff/`, `packages/domain/{domain-name}/`) are stated in §1; this section declares only the monorepo-level separation: per-app implementation lives under `apps/{app-slug}/**` and per-domain implementation under `packages/domain/{domain-name}/**`.

The high-level structure is constitutional — Hub-authored TDDs reference paths like `apps/{app-slug}/specs/` for spec location and `packages/domain/{domain-name}/` for domain implementation location.

**Constitutional invariants**:
- App slug and domain name are kebab-case identifiers
- Apps and domains have decoupled identities — domain identity is decoupled from app identity per §1.3
- Tier-tier seam between Tier 2 (app BFF) and Tier 3 (domain services) is the contract testing boundary (Pact consumer-driven convention; specifics CC substantive)

Specific path patterns within `apps/**` or `packages/domain/**`, frozen-name rules, what-must-not-be-in-the-repository discipline, domain lifecycle and versioning rules, and contract testing operational details are all CC substantive.

---

# 7. Cross-workspace anti-drift signals

Violations of §1-§6 are cross-workspace anti-drift signals per [OS] §12. In-CC operational anti-drift signals (specific subagent permission leaks, context scope violations, lint rule drift, repository layout drift, domain naming conflicts, skill loading drift) are governed by the CC-side substantive canonical.
