# [RULE] Claude Code Architecture Rules

- **Project**: HR Digital Cockpit
- **Document Type**: Architecture Specification
- **Status**: Active canonical
- **Role**: Stable architecture-rules source for Claude Code projects that execute Cat 4 software development derived from this hub's design outputs, including tier boundaries, subagent roster, agent context scopes, repository layout, skill loading rules, multi-app monorepo organization, and domain-package lifecycle.
- **Source Category**: Cat 4
- **Management-System Role**: Architecture specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Serves the Development Track routing layer defined in the Project Operating Model. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §2 (capability-first), §4 (lifecycle value), §6 (operation management), §10 (MECE) to the three-tier architecture, multi-app monorepo, domain-package lifecycle, subagent roster, and context-scope policy.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. CCAR governs the CC workspace's internal structure (tiers, subagents, scopes, repository layout, skill loading) — Hub-CD-CC Architecture frames why CC is the implementation pillar in the three-workspace tripartition.
- **Relationship to [REF] CC Project Memory Bank Layout**: Companion. CCAR governs substantive content rules (what each subagent does, what each tier owns, what skills load when); [REF] CC Project Memory Bank Layout governs the layout for those substantive artifacts (where the CLAUDE.md files live, how `.claude/` directory is structured, naming conventions, cross-reference resolution). When a new CLAUDE.md or `.claude/` artifact is authored, [REF] determines the path and name; CCAR determines the content rules. The §4 CLAUDE.md hierarchy of this source is a pointer to [REF] §1.
- **Relationship to [RULE] Workspace Topology**: Companion. CCAR §5 subagent roster + §X agent scopes deploy per-node under WT §4 single-shared-config rule.
- **Relationship to [RULE] Codex Plugin Usage**: Anchored. Codex invocations operate within CCAR §Y.1 path conventions.
- **Relationship to [MECH] Development Track Workflow**: Companion. DTW §4 task sequence imports CCAR §1 tier boundaries + §5 subagents + §X scopes + §Y paths.
- **Relationship to [MECH] CI/CD Milestone Policy**: Companion. CI/CD §2 milestone gates apply to work governed by CCAR's static structures.
- **Relationship to [MECH] Application Lifecycle Handoff**: Anchored. CCAR governs implementation work; Application Lifecycle Handoff governs the release-channel boundary.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: Anchored. Cross-tool flows that carry CC-internal canonical or DS code reference CCAR §5 subagents, §X scopes, §Y layout per [MECH] Cross-Tool Workflow Handoff §3.
- **Relationship to [TPL] sources**:
  - `[RULE] Design System Governance` — authoritative for Tier 1 design language; CCAR §Z declares its skill-mediated load mechanism
  - `[TPL] Technical Design Document Template` — produces the architecture decisions CCAR's three tiers implement
  - `[TPL] Test Plan YAML Schema` — drives the test work the §5 agent roster executes
- **Relationship to specification outputs**: Consumes TDD, PRD, acceptance, test-plan, and DSG artifacts produced in this hub; does not replace them.
- **Pairings I participate in**: P-01 (with [MECH] CI/CD §2), P-12 (with [MECH] CQ §3), P-15 (with [MECH] Dev-Loopback), P-16 (with `.claude/config/context-scopes.yaml`), P-17 (with `.claude/agents/`), P-18 (with `.claude/skills/`)

## How to use this source

Use this source when:
- creating a new Claude Code project for HR digital solution development
- introducing a new app under the multi-app monorepo
- introducing or extending a domain package
- authoring a CLAUDE.md file at any of the five hierarchy levels
- reviewing whether a proposed implementation violates tier boundaries or app/domain scope boundaries
- deciding which tier or which package owns a specific responsibility
- configuring `.claude/agents/`, `.claude/skills/`, or `.claude/config/` for the project
- debugging agent context leaks or skill loading issues

Do not use this source as:
- a multi-node infrastructure spec ([RULE] Workspace Topology)
- a full software development handbook
- a vendor product comparison guide
- a substitute for specification-level technical design
- the definition of when agents are invoked (that is [MECH] Development Track Workflow)
- a release-channel specification ([MECH] Application Lifecycle Handoff)

---

---

# 1. Three-tier architecture

**Terminology note**: Tier 1 / Tier 2 / Tier 3 in this source refer exclusively to the code-layer architecture of Claude Code projects. They are deliberately distinct from the L1-L5 management-system lens defined in [OS] §4.3. The management-system lens is a governance-design construct used to place policies, process maps, and SOPs; the three-tier code architecture is an implementation-structure construct used inside Claude Code projects. The two should not be confused during design-to-code handoff or in any CLAUDE.md authoring work.

## 1.1 Tier 1 React Frontend

**Owns**
- Pages and components
- User interaction state
- Frontend routing
- Presentation-layer display logic
- Adherence to project Design System Governance (tokens, components, a11y, i18n)

**Does not own**
- Cross-domain aggregation
- Core business rules
- Permission decision primary logic
- Long-term business state persistence
- Database access

**Physical placement**: `apps/{app-slug}/src/frontend/**` (per §Y).

**Design system constraint**: Tier 1 code must adhere to `specs/design-system.md` (project-level singleton) as loaded by the `hdc-arco-enterprise-ui` skill (§Z). Deviations require a paired `specs/design-system-changes/{change-id}.md` draft approved per [RULE] DSG §12 governance.

## 1.2 Tier 2 Node / TypeScript Experience Orchestration Layer (Thin BFF)

**Owns**
- Scene-facing APIs
- Aggregation across domain services
- DTO transformation
- Frontend-specific validation and orchestration
- Session context, token handling, lightweight caching
- Journey orchestration

**Does not own**
- Core domain rules ownership
- Database direct access as normal pattern
- Replacement of domain services
- Long-TTL or cross-session state caching
- Business state persistence

**Physical placement**: `apps/{app-slug}/src/bff/**` (per §Y).

## 1.3 Tier 3 Java Domain Services Layer

**Owns**
- Business capability boundaries
- Domain rules
- Transactions
- Auditing
- Stable external service contracts
- Integration with other enterprise systems and platforms

**Does not own**
- UI / presentation concerns (owned by Tier 1)
- Scene-facing API shapes, DTO transformation, frontend-specific aggregation or orchestration (owned by Tier 2)
- App-specific session context, token handling, or request-scoped caching (owned by Tier 2)
- Journey orchestration across multiple domain services (owned by Tier 2)
- Direct knowledge of consumer apps' identities or feature scopes (domain identity is decoupled from app identity per §Y.4)

**Physical placement**: `packages/domain/{domain-name}/**` (per §Y; per Phase A Option β decision). Domain identity is decoupled from app identity; a domain may serve one or more consumer apps over its lifecycle. Domain lifecycle and cross-app reuse are governed by §Y.4.

---

# 2. Tier 2 thinning rule (tier preservation)

Simple applications may thin the Tier 2 layer when full orchestration logic is not justified, but the three-tier structure must be preserved.

Approved pattern: **Tier 2 retained as a thin BFF layer** that performs only DTO mapping and API gateway duties, while Tier 1 and Tier 3 carry their normal responsibilities.

Do not remove Tier 2 entirely. Even in simple applications, retain Tier 2 as a thin BFF to preserve architectural evolution space and prevent DTO leakage into Tier 1.

Rationale for retaining Tier 2:
- prevents Tier 1 from absorbing backend contract knowledge that belongs outside the presentation layer
- preserves a stable seam for later enrichment (session handling, caching, aggregation) without refactoring Tier 1
- keeps permission decision placement (§3) clean across tiers
- preserves the BFF as the consumer side in the domain contract testing pair (§Y.4) — removing Tier 2 would erase the Pact consumer that drives domain producer verification

---

# 3. Permission decision placement

Permission decisions must be separated by type.

## 3.1 Data permissions

Data permissions are part of the domain data semantic model.

Ownership: **Tier 3 backend**.

Apply:
- Role-based access control evaluation at Tier 3
- Attribute-based access control evaluation at Tier 3
- Row-level permission resolution at Tier 3
- Field-level permission resolution at Tier 3

Decisions made at Tier 3 are authoritative and cannot be overridden by Tier 2 or Tier 1.

## 3.2 Functional permissions

Functional permissions follow the specific scenario.

Ownership: **case-by-case**, decided in specification output for each initiative.

Apply:
- Tier 1 never owns functional permission decisions
- Tier 2 may own functional permissions when they are session-scoped or journey-bound
- Tier 3 owns functional permissions when they govern business capability access
- Specification output must state which tier owns functional permissions for each feature (phase TDD `§1.Tier-Responsibility-Mapping` + acceptance.yaml `permissions.owning_tier`)

---

# 4. CLAUDE.md file hierarchy

A Claude Code project under the multi-app monorepo carries CLAUDE.md files at five hierarchy levels: project root, app root, app frontend, app BFF, domain root. The complete path discipline, load timing, responsibility, content requirements, and "must reference" lists for each level are owned by **[REF] CC Project Memory Bank Layout §1**.

This source (CCAR) governs the substantive tier rules (§1), permission decision placement (§3), subagent roster (§5), agent context scopes (§X), repository layout (§Y), and skill loading rules (§Z) that the CLAUDE.md files at each level enforce and reference. The layout reference is the destination authority for "where each CLAUDE.md lives and what fields each must contain"; CCAR is the source authority for "what behavior those fields govern".

When a new app is introduced, the walking_skeleton unit (per [RULE] Workspace Topology §4.6.3) produces app-level and tier-level CLAUDE.md files at the paths declared in [REF] CC Project Memory Bank Layout §1, with content shaped by the tier rules in CCAR §1, §3, §6.

---

# 5. Subagent roster

This source is the canonical authority for the HDC project's subagent roster, bias firewall principle, agent definition file location, and multi-node deployment topology. The agent definition files themselves (`{agent-name}.md` at `HDC_ROOT/.claude/agents/`) are hub-authored deliverables that live in the Development Track repository, not canonical sources at the hub — see [OS] §9.4 (Claude Code skill and subagent definition files). When this section changes materially, the corresponding agent definition files are updated under the paired-update obligation declared in [OS] §8.5.2.

The roster is 10 subagents, with 1 conditionally enabled. Subagent invocation timing during the development lifecycle is defined by [MECH] Development Track Workflow; milestone-level gating is defined by [MECH] CI/CD Milestone Policy.

## 5.1 Roster table

TK invocation values below are reconciled with [MECH] Development Track Workflow §4 task definitions and [MECH] CI/CD Milestone Policy §2 mapped-tasks lists, which are the authoritative sources for invocation timing per the footer note on §5 ("Subagent invocation timing during the development lifecycle is defined by [MECH] Development Track Workflow").

| Code | Subagent | Purpose | Invoked in (primary) | Context scope (see §X) |
|---|---|---|---|---|
| A1 | `test-writer-whitebox` | Generate unit and internal-integration tests with code visibility | TK-05 (M1 auto cycle) | `code_whitebox` |
| A2 | `test-writer-blackbox` | Generate contract, external-integration, e2e, visual, accessibility, performance tests without code visibility | TK-08 (M2 core), TK-09 (M2 re-runs after adversarial patches), TK-10 (M3 pre-release) | `api_contracts` |
| A3 | `adversarial-tester` | Derive adversarial scenarios from acceptance + risk register; no code or test visibility | TK-09 (M2 adversarial loop) | `business_rules_only` |
| A4 | `domain-judge` | Generate domain-perspective and UX-perspective candidate questions from evidence + acceptance + PRD + intent UX brief; no code or test visibility | TK-11 (M4 prep) | `business_rules_only` |
| A5 | `unit-test-auto-repair` | Auto-fix failing unit tests, max 3 retries per test | TK-06 (M1 unit-test auto-repair) | `code_whitebox` |
| A6 | `rca-reporter` | Generate root cause analysis for failed integration / e2e / visual / accessibility / performance tests | TK-07 primary (M1 RCA after auto-repair exhaustion); also fires on non-unit-test failures at TK-08 / TK-09 (M2) and TK-10 (M3) | `code_whitebox` |
| A7 | `visual-regression-reviewer` | Review visual regression results and check Design System Governance compliance | TK-10 (M3 pre-release) | `api_contracts` |
| A8 | `security-reviewer` (conditional) | Security scan before merge; enabled when slice risk tier or compliance scope warrants | TK-10 (M3 pre-release; only when enabled per [MECH] CI/CD Milestone Policy §2.4) | `code_whitebox` |
| A9 | `compliance-checker` | Verify implementation matches TDD module decomposition, tier ownership, permission placement, Design System Governance compliance, app/domain placement | TK-08 (first-pass, M2) + TK-11 (final, M4 prep) | `code_whitebox` |
| A10 | `evidence-compiler` | Aggregate all evidence artifacts into Test Evidence Report and produce operator digest one-pager; no code or test visibility | TK-11 (M4 prep) | `business_rules_only` |

## 5.2 Bias firewall principle

The 10-agent roster implements a **bias firewall + context isolation** architecture:

- **Code-visible agents** (A1, A5, A6, A8, A9): allowed to read app `src/**` and domain `src/**` because their task requires code knowledge
- **API-contract agents** (A2, A7): cannot read any `src/**`; work against API contracts, test specs, acceptance contracts, design references
- **Business-rules-only agents** (A3, A4, A10): cannot read any `src/**` or `tests/**`; work purely against business-level artifacts

This separation ensures adversarial testing, domain judgement, and evidence compilation cannot be accidentally biased by implementation details that might suppress valid criticisms.

## 5.3 Agent definition locations

Each subagent has its definition at:

```
HDC_ROOT/.claude/agents/{agent-name}.md
```

Project-root `.claude/agents/` is the single shared agent definition source for the entire monorepo. There are no per-app or per-domain agent override files. Agent definition files follow Claude Code's agent file format (YAML frontmatter + body). The `tools` field in frontmatter must reflect the context scope declared in §X.

## 5.4 Multi-node deployment topology

The agent roster in §5.1 and the agent definition files at the project-root `.claude/agents/` are deployed across all dev nodes via git pull. Each node runs **single subagent instances** (one A1, one A2, etc.); same-node multi-slice parallelism uses **git worktree isolation** rather than subagent multiplexing.

The full multi-node deployment model — node identity, parallelism unit, feature-level node affinity, worktree isolation mechanism, and slice-to-node-capacity matching — is owned by [RULE] Workspace Topology §4. This source declares only that the agent roster is single-shared at project root and per-node single-instance.

---

# X. Agent context scopes

This section is the canonical source for the bias-firewall configuration. It defines the three named scopes, the files each scope allows or denies, and the configuration contract.

## X.1 Named scopes

Three context scopes partition agent file-read access. All path patterns are evaluated relative to `HDC_ROOT`.

### `business_rules_only`

**Scope: One of three context_scope values defined in §X.1 named-scope vocabulary; the most restrictive scope, granting read access to specification artifacts only (no source code, no test code).**

**Allowed reads**:
- `apps/*/specs/prd/**`
- `apps/*/specs/tdd/**` (architecture-level content only; agent should not cherry-pick implementation hints)
- `apps/*/specs/intent/**`
- `apps/*/specs/acceptance/**`
- `apps/*/specs/test-plan/**` (read-only; cases + coverage summary)
- `apps/*/specs/slice-list/**`
- `specs/design-system.md` (project-level; read-only; for UX-dimension judgement)
- `apps/*/evidence/{slice-id}/**` (for A10 aggregation and A4 questioning)
- `apps/*/reports/**` (for upstream evidence aggregation)

**Denied reads**:
- `apps/*/src/**`
- `packages/domain/*/src/**`
- `apps/*/tests/**`
- `packages/domain/*/tests/**`
- `.claude/**`

**Used by**: A3 (adversarial-tester), A4 (domain-judge), A10 (evidence-compiler)

### `api_contracts`

**Scope: One of three context_scope values defined in §X.1 named-scope vocabulary; intermediate scope, granting `business_rules_only` reads plus OpenAPI contracts (still no source/test code).**

**Allowed reads**:
- Everything in `business_rules_only`
- `apps/*/specs/openapi.yaml` (single app-scoped file per [MECH] Development Track Workflow §TK-02 Outputs)
- `apps/*/specs/openapi/**` (forward-compat for potential subdirectory expansion if a future phase requires auxiliary schemas)
- `specs/design-system.md` (project-level; for A7 Design System compliance cross-check)
- UI design references (if any external design artifacts are referenced)

**Denied reads**:
- `apps/*/src/**`
- `packages/domain/*/src/**`
- Internal implementation headers or interfaces

**Used by**: A2 (test-writer-blackbox), A7 (visual-regression-reviewer)

### `code_whitebox`

**Scope: One of three context_scope values defined in §X.1 named-scope vocabulary; the broadest scope, granting `api_contracts` reads plus source code and unit/integration tests (used by code-writing and whitebox-testing agents).**

**Allowed reads**:
- Everything in `api_contracts`
- `apps/*/src/**`
- `packages/domain/*/src/**`
- `apps/*/tests/**`
- `packages/domain/*/tests/**`
- Dependency manifests (`package.json`, `pom.xml`, `build.gradle`, `pnpm-workspace.yaml`, etc.)

**Denied reads**: none beyond general repository boundaries

**Used by**: A1 (test-writer-whitebox), A5 (unit-test-auto-repair), A6 (rca-reporter), A8 (security-reviewer), A9 (compliance-checker)

## X.2 Configuration contract

Context scopes are declared in a single configuration file at the project root:

```
HDC_ROOT/.claude/config/context-scopes.yaml
```

There is no per-app or per-domain context-scopes override. The bias firewall is uniform across the monorepo.

### X.2.1 Schema

**Scope: YAML schema for `HDC_ROOT/.claude/config/context-scopes.yaml` declared in §X.2; this file is the runtime mirror of the §X.1 named-scope vocabulary and §X.4 write-scope policy (paired-update with this source per P-16).**

```yaml
schema_version: "1.0"

scopes:
  business_rules_only:
    description: "Business-level artifacts only; no code or test visibility"
    allow:
      - "apps/*/specs/prd/**"
      - "apps/*/specs/tdd/**"
      - "apps/*/specs/intent/**"
      - "apps/*/specs/acceptance/**"
      - "apps/*/specs/test-plan/**"
      - "apps/*/specs/slice-list/**"
      - "specs/design-system.md"
      - "apps/*/evidence/{slice-id}/**"
      - "apps/*/reports/**"
    deny:
      - "apps/*/src/**"
      - "packages/domain/*/src/**"
      - "apps/*/tests/**"
      - "packages/domain/*/tests/**"
      - ".claude/**"

  api_contracts:
    description: "API contracts and blackbox-available references; no src/** visibility"
    inherits_allow_from: business_rules_only
    additional_allow:
      - "apps/*/specs/openapi.yaml"              # single app-scoped file per [MECH] DTW §TK-02 Outputs
      - "apps/*/specs/openapi/**"               # forward-compat for potential subdirectory expansion
    deny:
      - "apps/*/src/**"
      - "packages/domain/*/src/**"

  code_whitebox:
    description: "Full code and test visibility across apps and domains"
    inherits_allow_from: api_contracts
    additional_allow:
      - "apps/*/src/**"
      - "packages/domain/*/src/**"
      - "apps/*/tests/**"
      - "packages/domain/*/tests/**"
      - "package.json"
      - "pnpm-workspace.yaml"
      - "**/package.json"
      - "**/pom.xml"
      - "**/build.gradle"
    deny: []

agent_assignments:
  # Each subagent in §5 is assigned to exactly one scope
  test-writer-whitebox:
    scope: code_whitebox
  test-writer-blackbox:
    scope: api_contracts
  adversarial-tester:
    scope: business_rules_only
  domain-judge:
    scope: business_rules_only
  unit-test-auto-repair:
    scope: code_whitebox
  rca-reporter:
    scope: code_whitebox
  visual-regression-reviewer:
    scope: api_contracts
  security-reviewer:
    scope: code_whitebox
  compliance-checker:
    scope: code_whitebox
  evidence-compiler:
    scope: business_rules_only

enforcement:
  mode: "deny-on-violation"  # alternative: "warn-on-violation" for transition period
  violation_log: "apps/{app-slug}/evidence/{slice-id}/context-scope-violations.log"
```

### X.2.2 Enforcement

Agent definition files in `.claude/agents/{agent-name}.md` must declare the scope consistent with `agent_assignments`. Claude Code's `tools` / `allowedFiles` / `deniedFiles` frontmatter fields are configured from this source.

When an agent attempts to read a denied file:
- In `deny-on-violation` mode: the read is blocked; an entry is logged
- In `warn-on-violation` mode: the read is permitted but logged (for transition period debugging)

The violation log lands under the executing slice's app scope (`apps/{app-slug}/evidence/{slice-id}/context-scope-violations.log`) and is consumed by A10 evidence-compiler at TK-12 and included in the Test Evidence Report.

## X.3 Scope change policy

Changing an agent's context scope is an architecture-level decision requiring:
1. Update to `.claude/config/context-scopes.yaml`
2. Update to this source §5.1 roster table
3. Update to the corresponding agent definition in `.claude/agents/`
4. Update to [MECH] Development Track Workflow §2 Role catalog if invocation semantics changed
5. Adversarial review on the config change

Silent scope expansion (e.g., quietly granting A3 read access to `apps/*/src/**`) is a red flag that undermines the bias firewall.

## X.4 Write scopes

This source documents read scopes explicitly; write scopes follow the principle that each agent writes only to its output paths declared in [MECH] Development Track Workflow §4. Specifically:

- A1, A5 write to `apps/{app-slug}/tests/unit/**` and `apps/{app-slug}/tests/integration/internal/**`, plus (when generating Tier 3 unit tests) `packages/domain/{domain-name}/tests/unit/**`
- A2 writes to `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**` (Pact consumer side, authored on behalf of the BFF), `apps/{app-slug}/tests/integration/external/**`, `apps/{app-slug}/tests/e2e/**`, `apps/{app-slug}/tests/visual/**`, `apps/{app-slug}/tests/accessibility/**`, `apps/{app-slug}/tests/performance/**`; producer-side verification at `packages/domain/{domain-name}/tests/contract-verification/**` is also A2's scope when working in a domain slice
- A3 writes to `apps/{app-slug}/evidence/{slice-id}/adversarial-findings.md` and `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` (patched)
- A4 writes to `apps/{app-slug}/evidence/{slice-id}/domain-judge-questions.md`
- A6 writes to `apps/{app-slug}/evidence/{slice-id}/rca/**`
- A7 writes to `apps/{app-slug}/evidence/{slice-id}/visual-review.md`
- A8 writes to `apps/{app-slug}/evidence/{slice-id}/security-report.md`
- A9 writes to `apps/{app-slug}/evidence/{slice-id}/compliance-first-pass.md` (TK-09) and `apps/{app-slug}/evidence/{slice-id}/compliance-final.md` (TK-12)
- A10 writes to `apps/{app-slug}/reports/m4/{slice-id}/test-evidence-report.md` and `apps/{app-slug}/reports/m4/{slice-id}/operator-digest.md`

No agent writes to any `src/**` (app or domain) — that is the main CC loop's responsibility. No agent writes to any `specs/**` path other than the patched test-plan.yaml exception in A3 — `apps/*/specs/prd/**`, `apps/*/specs/tdd/**`, `apps/*/specs/intent/**`, `apps/*/specs/acceptance/**`, and `specs/design-system.md` are hub-produced.

---

# Y. Repository layout

This section declares the canonical directory structure for a Claude Code project in this hub's Development Track. The layout follows the Path B2 multi-app monorepo convention with Option β domain-package decoupling.

## Y.1 Root structure

```
HDC_ROOT/
  CLAUDE.md                            Project root CLAUDE.md ([REF] CC Memory Bank Layout §1.1)
  package.json                         Workspace root manifest
  pnpm-workspace.yaml                  pnpm workspace declaration
  
  specs/                               Project-level specs (singletons)
    design-system.md                   Project-level DS instance (produced at workspace inception per [RULE] Workspace Topology §10)
    design-system-changes/             Proposed Design System Governance changes awaiting approval
      {change-id}.md
  
  apps/                                Per-app containers
    {app-slug}/                        e.g., hr-data-asset-mgmt, mobile-payslip
      CLAUDE.md                        App root CLAUDE.md ([REF] CC Memory Bank Layout §1.2)
      package.json                     App package manifest
      
      src/                             App-scoped source code
        frontend/                      Tier 1 React code
          CLAUDE.md                    [REF] CC Memory Bank Layout §1.3
          i18n/
            {locale}.json              Localization resource files (one per supported locale)
        bff/                           Tier 2 Node/TS code
          CLAUDE.md                    [REF] CC Memory Bank Layout §1.4
      
      specs/                           Hub-produced app-scoped specifications
        prd/phase-{N}.md               Canonical phase PRD (one per app per phase)
        tdd/phase-{N}.md               Canonical phase TDD (one per app per phase; covers all features in the phase via §4.{feature-slug} sub-sections)
        openapi.yaml                   OpenAPI spec — single app-scoped file, accumulated additively across phases
        slice-list/{feature-slug}.md   Slice decomposition per feature (per-feature, decoupled from phase)
        test-plan/
          phase-{N}.md                 Phase test plan (master, markdown) — one per app per phase
          feature-{feature-slug}.yaml  Feature integration test plan (yaml) — one per feature in the phase
          {slice-id}.yaml              Slice test plan (yaml) — one per slice
        intent/{slice-id}.md           Intent per slice
        acceptance/{slice-id}.yaml     Acceptance per slice
      
      tests/                           App-scoped test code
        unit/
          frontend/{module}/
          bff/{module}/
        integration/
          internal/
          external/
        contract/
          {app-slug}-bff_{domain-name}/   Pact consumer contracts authored by this app's BFF
        e2e/
          {flow}/
        visual/
          {screen}/
        accessibility/
          {screen}/
        performance/
          {scenario}/
      
      evidence/                        App-scoped per-slice evidence
        {slice-id}/
          unit-results.json
          internal-integration-results.json
          contract-results.json
          external-integration-results.json
          compliance-first-pass.md
          compliance-final.md
          adversarial-findings.md
          visual-diffs/
          visual-review.md
          accessibility-audit.md
          accessibility-results.json
          performance-report.md
          security-report.md             (if A8 enabled)
          domain-judge-questions.md
          codex/
            codex-review.md              (per [RULE] Codex Plugin Usage; co-located with executing node)
          rca/
            {timestamp}-{test-id}.md
          context-scope-violations.log   (if any)
      
      reports/                         App-scoped milestone-level aggregate reports
        m0/{slice-id}/
          adversarial-review.md
        m4/{slice-id}/
          test-evidence-report.md
  
  packages/                            Workspace build packages (real build-tool semantics)
    domain/                            Tier 3 Java Spring Boot domain services
      {domain-name}/                   e.g., data-asset, payslip, notification, compensation
        CLAUDE.md                      Domain root CLAUDE.md ([REF] CC Memory Bank Layout §1.5)
        package.json                   (or build.gradle / pom.xml)
        src/**                         Java code per Spring Boot conventions
        tests/
          unit/domain/{module}/        Domain-internal unit tests
          contract-verification/       Producer-side Pact verification of consumer contracts
  
  .claude/                             Project-wide Claude Code configuration (single shared)
    agents/
      test-writer-whitebox.md
      test-writer-blackbox.md
      adversarial-tester.md
      domain-judge.md
      unit-test-auto-repair.md
      rca-reporter.md
      visual-regression-reviewer.md
      security-reviewer.md
      compliance-checker.md
      evidence-compiler.md
    config/
      context-scopes.yaml              §X.2
    skills/                            Anthropic-native project-level skill location
      hdc-arco-enterprise-ui/
        SKILL.md                       SK-F (§Z)
      hdc-wcag-accessibility-checker/
        SKILL.md                       SK-W (§Z)
      frontend-design/                 (Anthropic SK-D, optional; see §Z.1)
        SKILL.md
    hooks/                             Hook scripts (PostToolUse, SubagentStop, Stop, Notification)
      [hook files per Claude Code hook spec]
```

## Y.2 Path stability

The paths declared in §Y.1 are load-bearing. Changes to this structure require:
1. Update to this source §Y.1
2. Update to [MECH] Development Track Workflow §3.2 Path conventions (must stay consistent)
3. Update to any skill that reads hardcoded paths (`hdc-arco-enterprise-ui` SKILL.md and `hdc-wcag-accessibility-checker` SKILL.md both read `specs/design-system.md`)
4. Adversarial review on the layout change

## Y.3 What must not be in the repository

- Per-user local configuration (use `.claude.local.json` or equivalent, git-ignored)
- Secrets, credentials, API keys
- Binary build outputs (gitignored)
- Node modules, Java build caches (gitignored)
- Editor-specific files outside `.editorconfig`
- Feature code outside `apps/{app-slug}/src/**`
- Domain code outside `packages/domain/{domain-name}/**`
- DS instance outside `specs/design-system.md` (the project-level singleton path)
- Custom HDC skills outside `.claude/skills/{skill-name}/SKILL.md` (the Anthropic-native project-level skill location)

## Y.4 Domain rules

This section governs Tier 3 domain packages under `packages/domain/{domain-name}/`.

### Y.4.1 Domain identity and naming

**Scope: Naming and identity rules for Tier 3 domain packages under `packages/domain/{domain-name}/` (declared in §Y.4 parent).**

- `{domain-name}` is kebab-case, lowercase, ASCII, descriptive of the business capability the domain owns (e.g., `data-asset`, `payslip`, `notification`, `compensation`)
- Domain identity is decoupled from app identity. A domain may be consumed by one or more apps; an app may consume one or more domains.
- Domain name is immutable once declared. Renaming a domain is treated as deprecation of the old domain and creation of a new one, with explicit migration of consumers.

### Y.4.2 Domain boundary

**Scope: What a Tier 3 domain package (`packages/domain/{domain-name}/`) owns vs does not own, and how cross-domain interaction is constrained.**

- A domain owns business capabilities, domain rules, transactions, auditing, and stable external service contracts (per §1.3)
- A domain does not own UI logic, BFF orchestration, or consumer-app-specific journey shaping
- Cross-domain calls go through domain APIs, never through direct database access into another domain's data
- A domain does not depend on any specific app; an app's BFF depends on one or more domains

### Y.4.3 Domain lifecycle (Model B — independent lifecycle)

- **Creation trigger**: a domain package is introduced when the first consumer feature requires it. No speculative domain modeling without an identified consumer.
- **Evolution**: once introduced, a domain evolves on its own cadence, independent of any single feature's roadmap
- **Cross-app reuse**: when a second app needs related capability, it evaluates and reuses the existing domain rather than creating a parallel domain. The Option β placement (`packages/domain/`) was chosen specifically to enable this reuse path.
- **TK-02 semantics**: a feature's phase TDD `§4.{feature-slug}.Module-Decomposition` may reference modules in `packages/domain/{domain-name}/`. When a feature requires new domain capability, the work is scheduled either as a feature-driven domain extension (within the feature's slice) or as a separate domain change request (independent slice), at the operator's discretion per feature.
- **Deprecation**: a domain is deprecated only when all consumer apps have migrated off it. Deprecation is a planned activity, not implicit drift.

### Y.4.4 Contract testing — Pact convention, consumer-driven

- The app BFF (consumer) writes contract expectations in `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**`
- The domain (producer) verifies it satisfies the contract in `packages/domain/{domain-name}/tests/contract-verification/**`
- Test pair name format: `{app-slug}-bff_{domain-name}` (e.g., `hr-data-asset-mgmt-bff_data-asset`)
- Adding a new consumer-domain pair requires a new test pair under both directories
- Contract evolution: the consumer changes the contract first, the producer adapts second; the producer never silently changes its API surface without updating the contracts of all current consumers

### Y.4.5 Domain versioning

- Domain packages use semver (`MAJOR.MINOR.PATCH`)
- Domain version is declared in the domain's `package.json` (Node-side artifacts) or `build.gradle` / `pom.xml` (Java-side artifacts)
- Each consuming app pins its dependency on the domain at a specific version in the app's manifest
- Coordinated upgrades are planned work; implicit drift across consumer pins is a §8 anti-drift signal

---

# Z. Skill loading rules

This section is the canonical authority for the HDC project's skill catalog, load triggers, override precedence, and update discipline. The skill definition files themselves (`{skill-name}/SKILL.md`) are hub-authored deliverables that live in the Development Track repository, not canonical sources at the hub — see [OS] §9.4 (Claude Code skill and subagent definition files). When this section changes materially, the corresponding SKILL.md files in the Development Track are updated under the paired-update obligation declared in [OS] §8.5.2.

Skills are managed under Anthropic's native skill discovery mechanism: project-level skills live at `HDC_ROOT/.claude/skills/{skill-name}/SKILL.md` and are discovered via Claude Code's upward path scan from the current working file. No bridging mechanism (symlink, copy, alias) is required; skill location follows Anthropic's prescribed Claude Code path convention.

## Z.1 Skill catalog

Three skills are in scope for the HDC project:

| Skill | Path | Role | Load trigger |
|---|---|---|---|
| SK-F | `.claude/skills/hdc-arco-enterprise-ui/SKILL.md` | Tier 1 design-system-aware code generation | Auto-load when working under `apps/*/src/frontend/**` or when prompts reference Tier 1 / frontend / React / screen / UX |
| SK-W | `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md` | A11y diagnostic utility (on-demand only, advisory) | **Manual invocation only** — does not auto-load |
| SK-D | `.claude/skills/frontend-design/SKILL.md` (optional) | Anthropic default frontend-design skill | Available as fallback for non-Tier-1 UI work; may be installed at user level (`~/.claude/skills/`) instead of project level per operator preference; superseded by SK-F for Tier 1 scope |

SK-D is not load-bearing for HDC dev track. Its installation location (project vs user) is operator preference; canonical does not regulate it.

## Z.2 Load trigger conditions

### SK-F (hdc-arco-enterprise-ui)

Auto-loads when the CC main loop performs any of:
- Creating a file under `apps/*/src/frontend/**`
- Modifying a file under `apps/*/src/frontend/**`
- Responding to a prompt referencing Tier 1, frontend, React component, screen, or UX brief
- Responding to a prompt referencing intent.md UX brief or the CD-authored UX Design Spec instance for the feature (per `[TPL] UX Design Spec`; UX coverage no longer lives in a TDD sub-section per the post-refactor architecture)

On load, SK-F reads `specs/design-system.md` (the project-level singleton). If the Spec is missing, SK-F aborts and reports.

### SK-W (hdc-wcag-accessibility-checker)

**On-demand only** — does NOT auto-load. The skill is invoked explicitly by the operator when an accessibility spot-check is desired. Per [RULE] Design System Governance §6, HDC has no formal WCAG conformance target and no automated a11y gate; SK-W is purely a diagnostic utility. ESLint `eslint-plugin-jsx-a11y` at `warn` severity (per [MECH] Code Quality Rule Set §1.2) is the routine, automatic a11y check.

On load (when invoked), SK-W reads `specs/design-system.md` §2.6 to confirm project stance and produces a non-binding diagnostic report.

### SK-D (frontend-design, optional)

If installed, loads on generic frontend prompts outside Tier 1 scope. For Tier 1 scope, SK-F supersedes.

## Z.3 Skill override precedence

When multiple skills could apply:

1. **Project-specific custom skill** (SK-F or SK-W) takes precedence over **general skill** (SK-D) for the project's scope
2. If two custom skills could both apply to the same prompt, both load and their guidance is merged; if guidance conflicts, the more specific skill wins (project-specific > tier-specific > domain-specific)

In practice for HDC, SK-F and SK-W never conflict: SK-F covers code generation, SK-W covers audit.

## Z.4 Skill update discipline

Skills are paired with the Design System Governance: when the Spec changes materially, skills may need prompt adjustment. See [RULE] DSG §12 governance.

Skill updates are themselves architecture changes requiring:
1. Update to the SKILL.md file
2. Update to this source §Z.1 catalog if scope changed
3. Update to [MECH] Development Track Workflow §2 Role catalog if load trigger changed
4. Adversarial review on the skill change

## Z.5 Anti-drift on skill loading

Red flags:
- Tier 1 code being written without SK-F in the active skill context
- `specs/design-system.md` not being read on SK-F load
- SK-W producing an audit that does not reference DS instance §2.6 target
- SK-F rules being silently overridden by user prompts (operator should modify SK-F or the Design System Governance, not bypass)
- Skills placed outside `HDC_ROOT/.claude/skills/{skill-name}/SKILL.md` (e.g., copied into `packages/`, `apps/{app-slug}/.claude/skills/`, or any other path under HDC governance) — this fragments Anthropic's native discovery and creates duplication

---

# 6. Testing policy by tier

This section defines tier-by-tier test ownership. For milestone-level test execution triggers (which tests run at which milestone and how failures are handled), see [MECH] Development Track Workflow §4 and [MECH] CI/CD Milestone Policy §2.

| Tier | Unit | Integration | E2E | Visual | Accessibility | Performance | Contract |
|---|---|---|---|---|---|---|---|
| Tier 1 | Component unit tests | Internal-only within tier | Critical user flows | Required for UI | Optional (no formal WCAG target per DSG §6; advisory only) | — | — |
| Tier 2 | Handler / orchestration unit tests | Internal-app integration | Included in E2E scenarios | — | — | Basic response time | Consumer-side Pact contracts authored against each consumed domain (§Y.4) |
| Tier 3 | Domain rule unit tests (high coverage) | Database and external system integration | Included in E2E scenarios | — | — | Basic response time | Producer-side verification of all consumer contracts (§Y.4) |

**Auto-repair scope**: unit tests only.

**Other test failures**: generate RCA via A6, do not auto-fix.

**Security testing scope note**: Security testing is not assigned to a specific tier. It is a milestone-scoped, conditionally enabled test type executed at TK-11 when A8 is enabled. See [MECH] CI/CD Milestone Policy §2.4 for enabling conditions and scope.

**Accessibility testing scope note**: Per [RULE] Design System Governance §6, HDC has no formal WCAG conformance target and no a11y testing requirement at any milestone. Routine a11y is covered by `eslint-plugin-jsx-a11y` at `warn` severity per [MECH] Code Quality Rule Set §1.2. Slice-specific accessibility test cases (`test_type: accessibility`) are optional per [TPL] Test Plan YAML Schema §5.2 and used only when a slice has specific a11y concerns; the `apps/{app-slug}/tests/accessibility/**` path remains available for those cases.

**Contract testing scope note**: Contract testing follows Pact convention, consumer-driven, per §Y.4. Test pair naming `{app-slug}-bff_{domain-name}` is mandatory; deviation is a §8 anti-drift signal.

---

# 7. Integration with other canonical sources

## 7.1 Format defaults for Claude Code

CLAUDE.md files at all five hierarchy levels are AI-primary control files. Use English by default. Use common Markdown, not DingTalk-targeted Markdown.

## 7.2 Source classification for Claude Code outputs

Code, tests, and runtime artifacts produced in Claude Code are not canonical sources for this hub.

Technical design documents consumed by Claude Code are specification outputs produced in this hub. They may become canonical only when explicitly promoted by the operator.

Release notes and lessons learned from Claude Code execution may become canonical source candidates when abstracted into reusable logic. Promotion follows the chat-native canonical revision path defined in [OS] §8.5: the observation surfaces in a Hub Claude conversation; the abstract-before-storing rule in [OS] §8.3 and the durable-first rule in [OS] §8.1 are applied as preconditions for revision; the relevant existing canonical source is updated in-place, or a new canonical source is created per [OS] §8.6 anti-duplication. No dedicated harvest template is required.

---

# 8. Anti-drift for Claude Code

> **Scope and ownership**: this section is the **canonical owner** for tier-boundary red flags, app/domain placement red flags (DSG singleton path; custom skills location; cross-app domain duplication; domain-vs-app code placement; app-slug roster), bias firewall red flags (agent context scope violations, silent scope expansion), contract testing convention red flags, and skill-loading red flags (the latter co-owned with §Z.5). Downstream sources ([MECH] Development Track Workflow §8; [MECH] CI/CD Milestone Policy §9) reference this section rather than duplicate it. Spec-to-implementation alignment red flags are also owned here.

Red flags that should trigger correction:

**Tier boundaries**:
- Tier 1 implementing business rules
- Tier 2 owning domain logic that should be in Tier 3
- Data permission decisions made outside Tier 3
- CLAUDE.md files missing at any of the five hierarchy levels (project root, app root, app-frontend, app-bff, domain root)
- Simple applications removing Tier 2 entirely instead of thinning it

**Specification-to-implementation alignment**:
- Implementation diverging from hub-produced TDD without explicit change control
- `specs/design-system.md` not being enforced in Tier 1 code

**App / domain placement**:
- Feature code placed outside `apps/{app-slug}/src/**`
- Domain code placed inside `apps/{app-slug}/` instead of `packages/domain/{domain-name}/`
- Design System Governance content created or copied outside `specs/design-system.md` (project-level singleton)
- Custom HDC skills placed outside `.claude/skills/{skill-name}/SKILL.md` (Anthropic-native project-level location)
- Cross-app domain duplication: two apps creating parallel `packages/domain/{name-A}/` and `packages/domain/{name-B}/` for substantially the same business capability instead of evaluating reuse per §Y.4
- App-slug used in TDD or path that conflicts with the app-slug roster declared at workspace inception (when a roster declaration is established)
- Implicit version drift across consumer-app pins of the same domain (per §Y.4.5)

**Contract testing**:
- Contract test pair naming not matching `{app-slug}-bff_{domain-name}` convention
- Producer (domain) changing API surface without updating consumer contracts
- Consumer-side contracts authored outside `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**`
- Producer-side verification authored outside `packages/domain/{domain-name}/tests/contract-verification/**`

**Agent roster and context scopes**:
- An agent in §5.1 reading files outside its declared scope in §X
- Silent scope expansion without the §X.3 change process
- A3, A4, A10 producing output that references specific code or test file paths (indicating scope leak)
- Agent assignment in `.claude/config/context-scopes.yaml` inconsistent with §5.1 roster
- Per-app or per-domain `context-scopes.yaml` override (single shared at project root only)

**Repository layout**:
- Files placed outside §Y.1 structure
- Skills or agents declared in CLAUDE.md but missing from `.claude/` directory
- Per-app `.claude/agents/` override (single shared at project root only)

**Skill loading**:
- Tier 1 code written without SK-F active
- Accessibility audit in TK-11 without SK-W active
- SK-F or SK-W not reading `specs/design-system.md` on load
- Skills placed in non-Anthropic-native location (per §Z.5)

**Multi-node deployment** (cross-reference [RULE] Workspace Topology §7):
- Per-node divergent agent definitions (single shared definition violated)
- Same-node multi-slice work without git worktree isolation
- Cross-node Codex invocation
