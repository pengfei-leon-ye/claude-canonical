# [OS] Project Operating Model

- **Project**: HR Digital Cockpit
- **Document Type**: Operating Model
- **Status**: Active canonical
- **Format**: Strongly structured common Markdown
- **Role**: Stable operating baseline for project routing, source governance, naming discipline, anti-drift logic, and the relationship between this hub and the Development Track
- **Source Category**: Meta
- **Management-System Role**: Operating-model source that defines the L1-L5 management-system lens; outside L1-L5 hierarchy; not itself an L2, L3, L4, or L5 artifact
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [OS]` header fields per §8.5.1a)

## How to use this source

Use this document as the primary operating baseline for:
- deciding how work should be routed within the project boundary
- deciding what belongs in Instruction, Source, or Chat zones of the hub
- deciding what should become canonical source versus stay dynamic
- governing the handoff from hub to Development Track
- enforcing source consistency, anti-duplication, naming discipline, and anti-drift correction

Do not use this document as:
- a detailed policy manual
- a process repository
- a delivery runbook
- a tracker
- a vendor administration handbook
- a warehouse for raw reference material
- a guide for work outside this project (the project governs its own scope only)

---

# 0. Project-level operating premises

## 0.1 Premises

Six premises hold across all four work categories in this project. They are the irreducible foundation for the project's design choices and the load-bearing anchor for anti-mimicry framing in downstream canonical sources.

### 0.1.1 Premise 1 — Co-production layer, not work environment

HDC Hub project and Claude Code are the sole-operator's AI co-production layer. They are **neither a substitute for, nor an extension of, the operator's actual work environment** (the company-side delivery and operations layer).

Three layers exist in the operator's overall workflow:

| Layer | Role | Scope |
|---|---|---|
| Hub project | Knowledge-work AI co-production | Strategic framing, policy architecture, options comparison, specification artifacts (PRD, TDD, intent/acceptance, test plans) |
| Claude Code | Software AI co-production | Spec-to-application conversion within HDC Development Track |
| Actual work environment | Company-side delivery and operations | Application deployment, policy promulgation, document landing in company systems, organizational decisions, formal stakeholder review |

Hub project and Claude Code connect to the actual work environment through **documents** (Cat 1 and Cat 2 deliverables the operator carries to the work environment) and **code** (Cat 4 deliverables passing through [MECH] Application Lifecycle Handoff). The co-production layers govern themselves through this canonical set; the actual work environment governs itself through company-side rules; canonical sources in this project bound the co-production layers only.

### 0.1.2 Premise 2 — Quality is the goal, process is the means

Quality of strategic thinking, specifications, and shipped applications is the goal of this project. Workflow mechanisms, milestone gates, CI/CD pipelines, audit mechanisms, and other process structures exist only to serve that goal.

Canonical authoring should resist the gravitational pull of "complete industrial coverage" in favor of "minimum sufficient process to support quality." When industrial best practice and Premise 3 are in tension, Premise 3 wins.

### 0.1.3 Premise 3 — Operator cognitive and execution load is the top constraint at non-canonical surfaces

The operator is a single human consuming all artifacts, making all decisions, and bridging all handoffs. There is no team to distribute review or execution across.

- **Cognitive load**: every additional rule, gate, dimension, taxonomy increment, naming convention nuance, or required check adds load. Mechanism designers should ask "does this addition pay for its load with proportionate quality gain?"
- **Execution load**: every additional manual step in workflow, every required artifact, every cross-reference to maintain adds load.

**Surface scope**: this premise applies primarily to surfaces the operator consumes directly — chat-level outputs, audit reports, analysis memos, decision-support deliverables, and any artifact the operator must read end-to-end to act on. At the **canonical layer** (PK + PI), §0.1.4 supersedes — operator authoring/review cost is accepted in exchange for AI RAG signal density.

Mechanism design that increases operator load at non-canonical surfaces without proportionate quality gain is an anti-pattern regardless of how aligned the addition is with industrial best practice.

### 0.1.4 Premise 4 — Canonical sources serve AI RAG consumers; operator authoring cost is not a design constraint at the canonical layer

Canonical sources (PK + PI) exist to drive AI behavior at retrieval time. Their core consumer is Claude AI via `project_knowledge_search` and equivalent RAG mechanisms.

**Surface-specific scope**:

| Surface | Primary consumer | Operator cognitive cost as design constraint |
|---|---|---|
| Canonical (PK + PI) | Claude AI via RAG | **Not a constraint** — operator accepts high one-time review cost at low-frequency revision events |
| AI-consumed artifact (specs, TDD, PRD, intent, acceptance, test plan) | Downstream AI (CC / agents) + operator review | Secondary consideration |
| Operator-consumed artifact (chat answer, audit report, analysis memo) | Operator | Primary consideration |

**Implications for canonical authoring**:

- Content that does not drive AI behavior at retrieval time — derived counts, derived statistics, restated boilerplate of rules owned elsewhere, "Why X exists" motivation sub-sections, historical status snapshots that are superseded, decorative meta-text, operator-navigation tables, summary closures — is **deletion candidate regardless of whether the operator finds it convenient to read**
- Operator-friendly scaffolding (chapter purpose summaries, boundary-with-adjacent-chapter tables, motivation rationales explaining design history) is **not justification for content retention** at the canonical layer
- Per-revision operator review cost is accepted as the trade for ongoing RAG retrieval signal-to-noise ratio
- Operative test: **"If this content unit were deleted, would any AI behavior measurably degrade?"** If No, the content is a deletion candidate
- Rule rationale that AI consumers retrieve at decision time (e.g., why a specific gate exists, used by Hub Claude when justifying gate enforcement to the operator at runtime) does drive AI behavior and is retained
- Rule rationale serving only as authoring-time historical record migrates to git commit history or to a dedicated [TPL] ADR Spec instance

**ROI logic justifying this premise**: canonical revision is operator-driven, low-frequency. The operator accepts high one-time review cost at each revision in exchange for trustworthy AI behavior at the high-frequency conversational layer. Trustworthy AI behavior reduces the operator's per-conversation audit burden, producing net cognitive-load reduction over time.

**Relationship to §0.1.3**: §0.1.3 governs operator-consumed surfaces; §0.1.4 governs the canonical layer. The two premises are complementary, not contradictory — each governs the surface where it applies. At the canonical layer, §0.1.4 explicitly overrides §0.1.3.

### 0.1.5 Premise 5 — Constitutional / substantive boundary at the workspace interface

Hub canonical sources serve two functionally distinct purposes:

- **Constitutional content** — cross-workspace interface contracts, governance rules, and existence-declaring rules. Constitutional content must live at Hub because it governs cooperation between workspaces (Hub / CD / CC) and across time. Examples: TK-chain existence and Hub/CC ownership boundaries, M-gate body existence and the Test Evidence Report interface, tier-separation discipline, handoff readiness contracts, anti-drift rules, and audit governance.

- **Substantive content** — workspace-internal operational rules: specific tool choices, parameter values, paths, step sequences, configuration specifics. Substantive content belongs at the workspace that executes it. Examples: specific lint rules, TK-NN operational step details, M-N gate criteria, repository layout specifics, agent roster entries, skill catalog entries.

**Workspace ownership under this boundary**:

| Workspace | Owns | Does not own |
|---|---|---|
| Hub canonical (PK + PI) | All cross-workspace constitutional content; Hub-internal substantive content | CC-internal substantive content |
| CC canonical (`.claude/canonical/` per [REF] CC Project Memory Bank Layout) | CC-internal substantive content; CC-side audit + maintenance mechanisms | Constitutional rules (CC consumes them by reference) |
| CD | Design files as SOT for design system content (per [RULE] Design System Governance); no canonical layer of its own | Constitutional rules and substantive Hub/CC operational content |

**Design test for source placement**: A rule belongs at Hub if and only if its change requires another workspace to respond (interface re-alignment, handoff contract adjustment, audit re-verification). Otherwise the rule belongs at the workspace that executes it.

**Relationship to §0.1.4**: §0.1.4 governs canonical-layer RAG-optimization regardless of which workspace owns the canonical. Premise 5 governs which canonical content lives at which workspace. The two premises are orthogonal — both constraints apply to every canonical source independently.

**Migration transitional state**: When a substantive rule currently resides at Hub PK but per the design test belongs at CC, the rule is a migration candidate. During the migration period, Hub-side substantive residue is tolerated; the design target is zero Hub-side CC-domain substantive content. The per-source migration disposition is owned by [REF] Hub-CD-CC Architecture.

**Priority interaction**: PI encodes the workspace-level priority chain that operationalizes this premise. When CC `.claude/canonical/` substantive content and Hub constitutional rules potentially conflict, constitutional rules win (governance authority). When Hub-side legacy substantive residue (pending migration) and CC `.claude/canonical/` substantive content conflict, CC wins (domain authority) and the Hub-side residue is flagged as pending migration. See PI "Priority and conflict handling" for the layered priority encoding.

### 0.1.6 Premise 6 — AI topology is not human topology

This project's [MECH] sources (governance mechanism specifications — workflow orchestration, milestone gating, audit governance, handoff protocols, sign-off cleanup, cross-tool handoff) coordinate work across AI sub-agents, fresh sessions, and cross-tool boundaries. AI collaboration has fundamentally different primitives than human team collaboration:

- **Statelessness**: each AI invocation is a cold start; no persistent context between calls beyond what is explicitly re-supplied via canonical RAG or runtime context
- **Finite attention**: context window is finite and exhibits non-uniform attention (Lost-in-the-Middle, Context Rot) — adding more rules does not guarantee they are all read
- **No latent agency**: AI does not autonomously escalate, follow up, or notice things outside the current invocation's scope
- **Ephemeral instance identity**: AI sub-agent instances are not coworkers with continuous memory of prior tasks

Mechanism design for [MECH] sources must reason from these AI primitives rather than transplant patterns from human team workflows. Commercial CI/CD pipelines, PR review protocols, human-in-the-loop sign-offs, and similar patterns may be referenced **only after explicit compatibility analysis with the AI primitives above**. Mechanism fragments that implicitly assume "a coworker holds the context", "someone will follow up", "state persists between sessions without being re-supplied", or "an actor proactively escalates" must be redesigned to make the assumed primitive explicit and to provide a state-supply or escalation mechanism that does not depend on AI possessing that primitive.

**Application scope**: this premise applies primarily to [MECH] sources and to multi-actor workflow rules in [RULE] sources (e.g., Workspace Topology multi-node coordination, Claude Code Architecture multi-agent topology). Single-actor Hub-internal rules ([OS], [PRIN], [TPL], [REF], single-axis [RULE]) are less affected because they do not involve sub-agent or cross-session coordination.

**Audit operationalization**: [MECH] CFSA §3.11 operationalizes this premise as a D5 Soundness check applied specifically to [MECH] sources.

**Origin**: this premise codifies a costly lesson from the early Development Track CI/CD design, where commercial CI/CD patterns assuming continuous-context coworker review were transplanted into AI-sub-agent contexts and produced repeated execution stalls. The pattern of "AI mimicry of human workflow primitives" is the failure mode this premise prevents.

### 0.1.7 How new Premises are added (meta-note)

Adding a new §0.1.x Premise expands the project's constitutional layer and must clear a higher bar than adding a [RULE] or [MECH] rule. A new Premise proposal must pass at least three of the following five AI Consumption dimensions before being added to §0.1:

1. **RAG hit improvement** — the new Premise will be referenced by multiple canonical sources (≥3 distinct sources), making it a high-frequency RAG retrieval anchor
2. **Cross-source disambiguation** — the principle is currently expressed with drifted wording across multiple canonical sources, and the Premise unifies the wording at a single authoritative location
3. **Decision gating** — the Premise can serve as a decision standard during §8.9 pre-generation declarations or other procedural gates
4. **Audit triggering** — the Premise maps to a concrete CFSA dimension check (existing D1-D7 or a new dimensional adaptation in §3.10 / §3.11)
5. **Cross-session consistency** — Hub Claude needs to apply the Premise repeatedly across sessions; codifying as a §0.1 Premise prevents per-session drift

The threshold is **≥3 of 5 dimensions passing** for upgrade to Premise; if fewer than 3 pass, the principle belongs at a lower layer ([REF], [RULE], [MECH], or in an existing source's section) rather than at §0.1.

**Bias acknowledgement**: this checklist preferentially scores high-frequency rules over low-frequency-but-structurally-critical gates. When evaluating a proposed structural gate (e.g., a Premise about how new canonical sources are added), interpret the "decision gating" dimension as gating leverage × single-occurrence consequence, not as raw frequency. Likewise the checklist preferentially scores audit-layer extensions over Premise-layer additions because the former trivially satisfy dimensions 3 and 4; operators should match the principle to its true structural layer rather than route everything through audit dimensions to inflate the score.

**Example application**: Premise 6 (this revision) passes all 5 dimensions: it applies across all [MECH] sources (RAG hit), unifies wording previously scattered across DTW / CFSA / PI (cross-source disambiguation), gates new [MECH] design (decision gating), maps to CFSA §3.11 (audit triggering), and applies in every [MECH] revision conversation (cross-session consistency). A counter-example — a proposed Premise "Single authoritative source for cross-workspace content" — was evaluated under this checklist and **withdrawn** (0 of 5 passed) because the principle was already adequately implemented at [REF] Hub-CD-CC Architecture and at CFSA D3 implicit-mirroring failure mode.

---

## 0.2 Category-specific role anchors

The operator plays different roles across the four work categories (§2.3).

| Category | Role anchor | Anti-mimicry guard |
|---|---|---|
| Cat 1 management-system work | Strategic thinker / policy architect | Output is personal strategic-design drafts the operator carries to the actual work environment; not enterprise standard-framework or consulting-deliverable replication |
| Cat 2 business solution design | Internal solution designer / PM-equivalent | Output is solution specifications for the operator's company business scenarios; not PM portfolio pieces or industry PRD template replication |
| Cat 3 product configuration | Reserved | No canonical source exists for Cat 3 at this revision; role anchor deferred until Cat 3 has active canonical content |
| Cat 4 Development Track | Senior developer in the work environment, with Hub project and Claude Code as senior-developer AI assistants | Output is handoff-ready applications produced by a senior developer working with AI assistance; not enterprise dev-team SDLC outputs and not fully-autonomous agent outputs |

---

# 1. Project identity

## 1.1 Project role

HR Digital Cockpit is the HR digital control hub for strategic judgment, reusable frameworks, architecture decisions, operating mechanisms, and handoff-ready artifact design.

Its purpose is to increase leverage across four loops:
- **Think**
- **Specify**
- **Orchestrate**
- **Harvest**

## 1.2 Hub-first rule

The project operates on a hub-first principle:

**Keep work inside the hub by default. Separate major workstreams by chat. Hand off to Development Track only when work becomes Cat 4 software development.**

For work within HR digital scope, the default home is this hub.

## 1.3 Project boundary

This project governs its own scope. It does not govern:
- casual chats outside the project
- unrelated Claude Projects
- external tools used for non-project work

Matters outside the project boundary are outside the scope of this operating model.

## 1.4 Audience and consumption model

Project Instructions and all canonical sources in Project Knowledge constitute the AI harness for **Hub Claude only** — the Claude.ai instance running inside this Project workspace. Their primary consumer is Hub Claude in conversations within this Project.

### Out of scope of this audience model

- Claude Code main-loop instances and the subagents executing in Development Track repositories — their harness is the CLAUDE.md hierarchy + `.claude/agents/` definitions + `.claude/skills/` SKILL.md, owned per [RULE] Claude Code Architecture Rules §4 / §5 / §Z
- Claude Design instances generating visual artifacts for HDC project work — CD does not directly read Hub canonical (its inputs are operator-mediated free-form context per [REF] Hub-CD-CC Architecture §3.3 setup-time and use-time canonical input model)
- Custom skills' runtime prompts — governed by [RULE] Design System Governance §13
- AI instances outside this Project entirely (other Claude.ai Projects, standalone chats, external AI tools)

### Visibility boundary across audiences

Hub Claude and Claude Code (CC) operate against disjoint file-system contexts:

- **Hub Claude** reads canonical sources from the project knowledge base via the RAG layer (`project_knowledge_search` and equivalent retrieval APIs). The hub Claude.ai platform may additionally expose an auxiliary filesystem view; when present, such a view is secondary and may diverge from the RAG layer per §8.5.3a — the RAG layer is the authoritative channel. Hub Claude does not read Development Track repository files unless they are explicitly attached to a hub conversation.
- **Claude Code** reads files from its local Development Track repository (CLAUDE.md hierarchy, `.claude/agents/*.md`, `.claude/skills/{name}/SKILL.md`, `apps/**`, `specs/**`, etc.). It does not read hub canonical sources from the hub's RAG layer or any hub-side filesystem view.

**Implication for cross-audience referencing**: any constraint that a hub canonical source places on CC behavior must reach CC by being **inlined into a CC-readable file** (typically the CLAUDE.md hierarchy, an agent definition, a SKILL.md, or a hub-produced spec file destined for CC consumption — project-level singletons under monorepo-root `specs/` or app-scoped artifacts under `apps/{app-slug}/specs/**`). Path-style references to hub canonical files (e.g., any hub-side filesystem path such as `/mnt/project/hdc_rule_*.md`), or a bare `[RULE] X §N` cross-reference without inlined content, are not resolvable on the CC side and must not appear in CC-targeted files.

**Operational mechanism**: the canonical-to-runtime-artifact pairings registered in §8.5.2 are the operational mechanism for this inlining. Hub canonical is the SOT; CC-side runtime artifacts (CLAUDE.md, agent definitions, SKILL.md, hub-produced spec files) are downstream mirrors carrying the inlined content. When the SOT changes, the mirror is updated under same-revision discipline per §8.5.2.

**What "inlining" means in practice**: a CC-targeted file may name a hub canonical source for traceability (e.g., "this CLAUDE.md inherits from [RULE] Claude Code Architecture Rules §1") only when accompanied by the substantive content the CC side actually needs to act on. The naming is a provenance label, not a deferred lookup. If the CC side would need to fetch the named source to act, the file is incomplete.

**Anti-drift signal**: emitting a bare cross-reference to a hub canonical path or § number inside any CC-targeted file — without the inlined content the reference depends on — is an anti-drift signal per §12.

### Operational consequences for Hub-Claude-targeted sources

- Section structure, terminology, and cross-references should optimize for Hub Claude's semantic-search retrieval (`project_knowledge_search`) and rule-application reliability per §0.1.4
- Prose density should match information density; rhetorical closure is decorative under §0.1.4
- Repetition that increases Hub Claude's RAG retrieval reliability is acceptable; repetition that only serves human reading-flow is not
- Orientation chapters (e.g., `# 0. Boundary and position`, `## How to use this source`) remain valid because they encode AI scope-routing signals

---

# 2. Scope and boundaries

## 2.1 In scope

### A. Decision shaping
- ambiguous business problem framing
- option comparison
- trade-off design
- architecture judgment
- global core versus local variance judgment
- build versus buy versus extend versus replace judgment
- decision support for leadership and key stakeholders

### B. Specification authoring
- PRD drafting
- prototype briefs
- MVP briefs
- technical design documents (TDD)
- per-slice execution interface artifacts (intent.md, acceptance.yaml, test-plan.yaml)
- handoff specifications
- integration specifications
- data specifications
- release briefs

### C. Governance and operating logic
- HR digital management-system anchors
- L2 policy anchors for the Digital Solution domain
- reusable judgment principles
- governance mechanisms
- format-control specifications

### D. Handoff to execution
- hub-to-Development-Track handoff
- Development Track architecture rules
- Development Track milestone policy
- Development Track workflow orchestration
- Development Track tool usage rules (e.g., Codex plugin)

### E. Harvest
- lessons learned from Development Track execution
- reusable patterns surfaced during specification or implementation
- source-candidate promotion

## 2.2 Out of scope

- detailed HR policy drafting at the organizational level beyond L2 anchors
- routine HR operations
- talent acquisition administration
- procurement administration
- full people analytics backlog
- every implementation stream
- technical support
- vendor management beyond specification handoff

## 2.3 Four task categories

The project scope contains four task categories distinguished by what kind of work the category serves. The categories determine canonical dependency rules: which canonical source families are admissible as upstream for which artifacts.

### 2.3.1 Category definitions

- **Cat 1 Management-system work**: Producing strategic artifacts, policies, process maps, SOPs, and governance mechanisms that apply to the user's workplace organization (Digital Solution Team within a company-wide management system). The hub's role for Cat 1 work is strategic copilot for the user's personal management-system thinking.
- **Cat 2 Business solution design**: Translating a business need through framing, option comparison, and specification into a business solution design (PRD / prototype brief / MVP brief) for a specific digital initiative.
- **Cat 3 Configuration workbook production**: When a business solution is to be implemented through commercial-product configuration rather than custom development, producing the configuration workbook from the approved PRD and vendor-product documentation. Cat 3 consumes Cat 2 output.
- **Cat 4 Development Track**: Full-flow task chain from PRD through production-deployable application. The upstream half (PRD → TDD → per-slice specs) executes in this hub; the downstream half (code → tests → deploy) executes in Claude Code. Cat 4 consumes Cat 2 output.

### 2.3.2 Canonical dependency rules

The following rules govern `Relationship to ...` fields in canonical source headers (per §10) and any cross-source references embedded in source content.

**Admissible for all four categories (meta layer)**:
- `[OS]` (this operating model) as meta authority
- `[PRIN] HR Digital Decision Design Principles` as cross-topic judgment layer
- `[RULE] Claude Platform Behavior Specification` and `[RULE] DingTalk Markdown Format Control Specification` as delivery-interface rules
- `[REF] Hub-CD-CC Architecture` as cross-tool architecture reference frame

**Admissible for specific categories**:

| Source family | Cat 1 | Cat 2 | Cat 3 | Cat 4 |
|---|:---:|:---:|:---:|:---:|
| `[POL]` + L2-L5 management-system artifacts | ✓ | ✗ | ✗ | ✗ |
| `[PRIN] People Experience Design Principles` | ✗ | ✓ | ✗ | ✓ (UI scope) |
| `[REF] People Journey and Moments Catalog` | ✗ | ✓ | ✗ | ✗ |
| `[REF] CC Project Memory Bank Layout` | ✗ | ✗ | ✗ | ✓ |
| Cat 2 specification templates (PRD / Prototype / MVP) | ✗ | ✓ | via PRD | via PRD |
| Cat 4 specification templates (TDD, Intent / Acceptance, Conversion Spec, Test Plan, UX Design Spec, ADR Spec, Phase Test Plan) | ✗ | ✗ | ✗ | ✓ |
| Development Track `[RULE]` family (Claude Code Architecture Rules, Workspace Topology, Design System Governance) | ✗ | ✗ | ✗ | ✓ |
| Development Track `[MECH]` family (Development Track Workflow, CI/CD Milestone Policy, Application Lifecycle Handoff, Cross-Tool Workflow Handoff) | ✗ | ✗ | ✗ | ✓ |

Authoritative membership of each `[RULE]` or `[MECH]` family for a given task category is determined by the `Source Category` header field declared in each canonical source per §10.2. When a Cat 4 source is added or retired, update the corresponding parenthetical in the same revision per §8.5.2 same-revision discipline; drift is an anti-drift signal per §12.

**Cross-category templates** (admissible in multiple categories as framing / option-comparison vehicles):
- `[TPL] Problem Framing Memo`
- `[TPL] Options Paper`

### 2.3.3 Hard boundary: no Cat 1 citation in Cat 2/3/4 canonical sources

Cat 2/3/4 canonical sources must not cite `[POL]`, L2-L5 management-system artifacts, or any other Cat 1 source in their `Relationship to ...` header or content body. When Cat 2/3/4 work must respect compliance constraints such as external regulations (GDPR, PIPL, SOC2, industry-specific rules) or company-level policies, the compliance anchor must point to the external regulation document directly, or to company-level policy documents maintained outside this hub — not to `[POL]`.

### 2.3.4 Specification output governing linkage (category-aware)

Per §5.4, a specification output must declare governing linkage when materially relevant. The governing linkage varies by category:

- **Cat 1 specification output** (e.g., a specific L2 policy draft, L4 process map, L5 SOP): governing linkage is typically the parent L2 / L3 domain in `[POL]` or the L1 corporate framework.
- **Cat 2 specification output** (e.g., PRD, prototype brief, MVP brief): governing linkage is the framing memo or options paper that produced the decision; **no L2 / L3 policy linkage is expected**.
- **Cat 3 specification output** (e.g., configuration workbook): governing linkage is the approved PRD and the vendor-product reference; **no L2 / L3 policy linkage is expected**.
- **Cat 4 specification output** (e.g., TDD, intent.md, acceptance.yaml, test-plan.yaml): governing linkage is the upstream canonical (PRD for TDD; PRD + TDD for interface artifacts); **no L2 / L3 policy linkage is expected**.

### 2.3.5 Cat 3 preservation note

As of this revision, no canonical source occupies the Cat 3 slot. Cat 3 is preserved in the category model because configuration-workbook production has different upstream / downstream logic than Cat 4 Development Track:

- Cat 3 consumes a PRD + a specific commercial product's configuration documentation; Cat 4 consumes a PRD + produces a TDD + implements via code
- Cat 3 has no multi-tier architecture, no test harness, no Design System Governance; Cat 4 has all of these
- Cat 3 deliverable is a configuration workbook (business-readable spec of what to configure in the vendor product); Cat 4 deliverable is deployed source code

When the first configuration-workbook production workflow matures to a reusable template, it will be authored under the `[TPL]` family with Source Category Cat 3, following the canonical dependency rules in §2.3.2 and §2.3.3. Until that template is justified under §5.5, Cat 3 configuration work is handled ad hoc in chat.

---

# 3. Four loops

## 3.1 Think
Frame problems. Surface ambiguity. Compare options. Make judgments.

## 3.2 Specify
Convert judgments into artifacts that developers, vendors, and reviewers can act on.

## 3.3 Orchestrate
Coordinate handoff, governance, and lifecycle gating.

## 3.4 Harvest
Promote durable insights to reusable source.

---

# 4. Management-system lens

## 4.1 L1 through L5 at a glance

- **L1**: Corporate strategy and governance level (outside hub scope)
- **L2**: Domain policies that govern a named control domain
- **L3**: Sub-policy domains under L2 when durable decomposition is justified
- **L4**: Process maps implementing L2 or L3
- **L5**: SOPs or SWIs for recurring tasks

## 4.2 Level definitions

### L1 — Corporate strategy and governance
Scope: enterprise-level, outside hub governance.

### L2 — Domain policy
Scope: a named control domain within the Digital Solution family, e.g., Project Management Policy, Operation Management Policy, Data Asset Management Policy.

Purpose: governs how the domain is controlled across the lifecycle.

Core question: what rules, decisions, and controls define this domain?

Contents: durable control rules, governance anchors, cross-cutting checks.

Exclusions: process maps, SOPs, per-initiative specifications.

### L3 — Sub-policy domain
Scope: a durable sub-domain under an L2 when decomposition is justified.

Purpose: isolate a stable sub-area with its own control logic.

Core question: does this sub-area need its own governable rule set that would pollute L2 if kept there?

Contents: sub-domain rules, boundary with parent L2.

Exclusions: process-level logic, SOPs.

### L4 — Process map
Scope: end-to-end process implementing an L2 or L3 policy.

Purpose: show how work flows, who does what, where hand-offs occur.

Core question: what is the process sequence that realizes the policy?

Contents: roles, steps, hand-offs, decision points, inputs/outputs.

Exclusions: policy rules, per-task SOPs.

### L5 — SOP / SWI
Scope: recurring task within an L4 process.

Purpose: ensure consistent execution of a specific task.

Core question: how does one person or system perform this task correctly?

Contents: step-by-step instructions, checklists, templates.

Exclusions: process logic, policy rules.

---

# 5. Output families and landing logic

## 5.1 Management-system outputs

Definition: artifacts that land at a specific L2–L5 level in the management-system lens and govern how domains are controlled.

Examples:
- L2 policy documents
- L3 sub-policy documents
- L4 process maps
- L5 SOP / SWI documents
- governance mechanisms (which run oversight over the above)

Landing: declare an L2–L5 level or state that the source is a governance mechanism that runs oversight across levels.

## 5.2 Specification outputs

Definition: initiative-specific artifacts produced during the Specify loop.

Examples (within the Digital Solution domain; see [POL] §7.1 for the authoritative domain-specific list):
- PRD, prototype brief, MVP brief
- Technical Design Document (TDD)
- per-slice execution interfaces (intent.md, acceptance.yaml, test-plan.yaml)
- handoff specifications
- integration specifications
- data specifications
- release briefs
- implementation decision logs

Landing: declare governing linkage per the category-aware rules in §2.3.4. Do not force into the L2–L5 hierarchy unless the output is itself a Cat 1 management-system output.

## 5.3 Boundary rule

Management-system outputs live in the L2–L5 hierarchy.
Specification outputs do not, but reference the hierarchy when materially relevant.

## 5.4 Level or linkage declaration rule

Every canonical source and every promoted specification artifact must declare either:
- its landing level per §4.1 L1-L5 lens (if it is a Cat 1 management-system output), OR
- its governing linkage per §2.3.4 category rules (if it is a Cat 2/3/4 specification output requiring linkage for executability, traceability, or reviewability)

The rule triggers when:
- a new canonical source is being generated or promoted
- a specification artifact is being promoted to canonical source
- a specification artifact's governing linkage materially changes

Scope exclusion:
- working drafts and chat artifacts
- artifacts whose governing linkage is not material

## 5.5 Default artifact classification when ambiguous

When a new artifact's classification is ambiguous between working artifact, specification output, and source candidate, default classification follows this ladder:

1. **Working artifact** — the default landing for chat-level analysis, option exploration, and iterative drafts.
2. **Initiative-specific specification artifact** — the landing for PRDs, prototype briefs, handoff specs, memos, drafts, options papers, and execution-interface files scoped to one initiative.
3. **Source candidate** — the landing only for content that is stable, reusable across topics, and serves a durable control purpose consistent with Section 8.

Reusable cross-topic control artifacts are source candidates. Initiative-specific PRDs, briefs, handoff specs, memos, drafts, options papers, and execution-interface files are not source candidates by default.

A specification artifact becomes a canonical source only upon explicit user promotion and only after passing the durable-first rule in §8.1 and the one-source-one-job rule in §8.2.

### Classification examples

| Artifact | Compliant default classification | Non-compliant misclassification | Why |
|---|---|---|---|
| A draft analysis of vendor SSO options for the current onboarding initiative | Initiative-specific specification artifact (level 2; promote to canonical Options Paper when reviewable) | Source candidate (level 3) | Initiative-scoped; not stable across topics; durable control purpose absent |
| A reusable judgment rule "prefer capability-first sourcing over vendor-first sourcing across all HR digital decisions" | Source candidate (level 3; eligible for promotion into [PRIN] HRD) | Initiative-specific specification artifact (level 2) | Stable, cross-topic, durable control purpose — Section 8 criteria met |
| A chat-resident exploration of "what if we ran a global pulse survey quarterly" | Working artifact (level 1) | Source candidate (level 3) | Iterative draft; durability not demonstrated; promotion requires §8.3 abstract-before-storing |
| A PRD for the time-off-request feature slice | Initiative-specific specification artifact (level 2) | Source candidate (level 3) | Feature-scoped; the durable rule is in [TPL] PRD template, not in this PRD instance |

## 5.6 Canonical sources outside L2-L5

Canonical sources that are neither §5.1 management-system outputs nor §5.2 initiative-specific specification outputs form a third category. This category contains reusable, cross-topic, control-oriented sources that shape how management-system outputs and specification outputs are produced.

Examples of sources in this category:
- operating rules (this operating model itself)
- judgment principles ([PRIN] family)
- policy architecture maps ([POL] family)
- reference catalogs and digests ([REF] family)
- format, tool, and architecture rules ([RULE] family)
- governance mechanism specifications ([MECH] family)
- reusable deliverable templates ([TPL] family)

### Governance

Sources in this category:
- live in the Source zone of the hub (see §7.1)
- are governed by §8 source governance and §10 canonical source header standard
- reach canonical status through the promotion path described in §5.5 (working artifact → source candidate → canonical source upon explicit user promotion)
- declare an outside-hierarchy, cross-level, or meta-level Management-System Role per §10.2

### Landing

These sources do not land inside the L1-L5 hierarchy. Do not force-fit them into §5.1. When a source in this category governs how a management-system output or a specification output should be produced, it acts as a control source above the output, not as an L2-L5 artifact itself. The operating model source that defines the L1-L5 lens itself is a further special case and declares a meta-level Management-System Role per §10.2.

Sources in this category do not state a landing level for themselves. When they govern downstream work, that downstream work applies §5.4 as normal; the governing source is cited as an authority, not as an L2-L5 artifact.

---

# 6. Policy architecture anchors

## 6.1 Single source of truth

The detailed policy architecture — including L2 policy domain definitions, L3 minimum stable domains, boundary rules, and mandatory cross-cutting control checks — is owned by `[POL] Digital Solution Policy Architecture Map` as its **single source of truth**.

This section retains only the L2 anchor names so that the operating model can name policy architecture without duplicating any definitional content. Do not add domain definitions, one-line intents, L3 detail, boundary rules, or cross-cutting checks here; update `[POL]` instead.

## 6.2 L2 policy anchors (names only)

The Digital Solution team's stable L2 policy anchors are:

- Project Management Policy
- Operation Management Policy
- Data Asset Management Policy

Definitions, one-line intents, downstream landing patterns, L3 decomposition, boundary rules, and cross-cutting control checks for each anchor are owned by `[POL] Digital Solution Policy Architecture Map` §3 and §4 per §6.1.

---

# 7. Routing architecture

## 7.1 Project-internal routing

The project has two internal routing locations:

### Hub (Claude.ai Project workspace)

The hub contains three internal zones:

**Instruction zone**

Use for:
- durable role definition
- language rules
- stable behaviors
- correction rules
- response discipline
- source-generation control logic

**Source zone (Project knowledge base)**

Use for:
- operating model
- principles
- templates
- policy architecture maps
- governance mechanisms
- baselines
- reusable reference digests
- format-control specifications

**Chat zone**

Use for:
- case-specific analysis
- working drafts
- option exploration
- PRD drafting
- release triage
- prototype briefs
- ongoing design thinking

### Development Track (Claude Code projects)

Cat 4 software development work executes in Claude Code as a separate technical environment, not inside the hub.

Relationship to hub:

- Development Track **consumes** specification outputs produced upstream. The split is owned by [MECH] Development Track Workflow §0.1 / TK-01 / TK-02 / TK-03.
- Development Track inherits canonical constraints via the **decoupled-reference model** (per [REF] Hub-CD-CC Architecture §5.4.4 post-Phase-3): CC's CLAUDE.md hierarchy and CC's own canonical layer at `<repo-root>/.claude/canonical/` reference Hub constitutional residues by name without inlining their content. The inheritance scope currently includes Hub-side constitutional residues plus CC substantive canonical:
  - **Hub constitutional residue at Hub PK**:
    - [RULE] Claude Code Architecture Rules (constitutional residue — three-tier identity, Tier 2 thinning rule, permission placement principle)
    - [RULE] Workspace Topology (constitutional residue + Hub-internal substantive — multi-node existence, parity discipline, walking-skeleton-first ordering, node-assignment interface contract)
    - [MECH] Development Track Workflow (constitutional residue + Hub-internal substantive — TK chain identity, Hub-authored TK-01/02/03/12, transitions)
    - [MECH] CI/CD Milestone Policy (constitutional residue — M0–M5 ladder identity, Test Evidence Report schema, evidence parity)
    - [MECH] Application Lifecycle Handoff (handoff readiness criteria, content scope, acknowledgment record format, re-entry policy)
    - [MECH] Cross-Tool Workflow Handoff (three-path handoff content contracts)
    - [RULE] Design System Governance (singleton DS model, three-way distribution, instance contract)
  - **CC substantive canonical at CC's own canonical layer** (migrated in Phase 3 per [OS] §0.1.5 Premise 5):
    - CC substantive CCAR (subagent roster A1-A10, named context scopes, repository path patterns, skill catalog, domain lifecycle and Pact contract testing specifics)
    - CC substantive Workspace Topology (specific tool stack and versions, GitHub workflow configuration, node-assignment procedure, workspace inception checklist)
    - CC substantive DTW (TK-04~TK-11 + TK-13 execution mechanics, CC-side transitions)
    - CC substantive CI/CD Milestone Policy (gate criteria per M-N, tooling baseline, accessibility thresholds, slice-size advisory)
    - CC substantive Memory Bank Layout (CLAUDE.md hierarchy paths, `.claude/` subdirectory structure)
    - CC substantive Codex Plugin Usage (formerly Hub canonical; fully migrated in Phase 3)
    - CC substantive Code Quality Rule Set (formerly Hub canonical; fully migrated in Phase 3)
    - CC substantive Dev-Loopback Mode (formerly Hub canonical; fully migrated in Phase 3)
    - CC substantive Tools Health Cadence (formerly Hub canonical; fully migrated in Phase 3)
- Development Track runtime capabilities include:
  - 10 subagents under `.claude/agents/` with bias firewall enforced by `.claude/config/context-scopes.yaml`
  - 2 custom project skills under `.claude/skills/` (`hdc-arco-enterprise-ui` enforcing Design System Governance at runtime; `hdc-wcag-accessibility-checker` as on-demand a11y diagnostic utility per DSG §6 stance)
- Business framing, architecture judgment, UX foundation, accessibility standard, and value-realization logic remain anchored in the hub
- Lessons learned and abstract patterns from Development Track may return to the hub as source candidates via the chat-native canonical revision path defined in §8.5; no dedicated harvest template is required

## 7.2 Conversation discipline within the hub

### Continue the same chat when
- the core decision is unchanged
- the target artifact is unchanged
- the work remains in the same phase
- context continuity is more valuable than chat cleanliness
- the thread is still easy to navigate

### Start a new chat when
- the decision question changes materially
- the target artifact changes materially
- the relevant landing logic changes materially, including intended management-system landing level for a management-system artifact or materially relevant management-system linkage for a specification artifact
- the work moves into a clearly new initiative phase
- the topic returns after a long pause with new context or constraints
- the original chat becomes too branched or too long
- a complete Artifact has been produced and the next task is materially new (Claude-specific: Artifacts are saved independently, so cross-contamination risk outweighs continuity value)

### One-month rule

If a large topic returns after about one month, default to a new chat unless the goal is to keep editing the same artifact.

### Bridge rule for a new chat

Restate:
- the prior decision or baseline
- what changed
- the new objective
- the next target artifact

### Chat naming convention

Use descriptive titles with keyword anchors so Claude's conversation search can find them later. Format: `[Topic keyword] — Specific question or artifact`.

### Promotion rule

When chat-resident conclusions become stable and reusable, promote them to canonical source via §5.5 ladder instead of repeatedly reviving old chats.

---

# 8. Source governance

## 8.1 Durable-first rule

Only stable, reusable, cross-topic content should become canonical source. Content that is initiative-specific, time-bound, or single-use does not earn its place in the harness — it belongs in chat, in specification artifacts, or in Development Track code per §8.4.

## 8.2 One-source-one-job rule

Each canonical source should serve one stable purpose. Intentional dual-ownership is permitted only when explicitly surfaced per §8.7 with rationale stating why two perspectives are genuinely orthogonal.

## 8.3 Abstract-before-storing rule

Convert observations into reusable logic before promoting them to source. §7.2 promotion rule governs the chat-to-source transition; this rule governs the substance that must exist before promotion is appropriate.

## 8.4 Separate stable from dynamic

Stable framework goes to source.
Dynamic detail stays in chat, in specification artifacts, or in Development Track code.

## 8.5 Consistency-check rule

Whenever generating, revising, replacing, or consolidating a source file, verify consistency against:
- project instruction
- this operating model
- all in-scope active canonical source files
- the active canonical DingTalk format-control source when format is in scope

Verification proceeds in two layers: a default semantic scan (§8.5.1) plus a static-pairing backstop for couplings that semantic search cannot reliably surface (§8.5.2). The Tier model in §8.5.1a discriminates which couplings warrant static-pairing registration vs which are adequately governed by source `Relationship to ...` header fields. A canonical name and § numbering discipline (§8.5.3) applies across all sources regardless of pairing. Pairing rationale is held in §8.5.5 as a separately-retrievable catalog so that the §8.5.2 table itself stays scannable.

### 8.5.1 Default: semantic scan

Run a semantic scan across the canonical set to surface sources whose content may be affected by the change under review. Claude's `project_knowledge_search` is the operational mechanism for this scan. The user describes the proposed change in enough detail (which source, which section, what kind of change) for the scan to return sources whose content overlaps conceptually; those returned sources drive the paired-review list for this revision.

### 8.5.1a Pairing Tier model

The §8.5.2 static pairing list exists as a backstop only when semantic scan is unreliable. Couplings are classified into two tiers, and only Tier A couplings warrant static pairing registration.

#### Tier A: Static-pairing-required couplings

A coupling is Tier A if and only if at least one of the following holds:

1. **C2R (canonical-to-runtime-artifact)**: the counterparty is a file outside the canonical RAG layer (e.g., runtime artifacts in Development Track repositories, configuration files, skill definition files, subagent files). AI consumers cannot reach the counterparty via `project_knowledge_search`; explicit pairing registration is the only discovery mechanism.

2. **Numeric / version value alignment across prose**: two or more sources independently reference a specific numeric, version, or quantitative value (e.g., a tool baseline version, a threshold count, a port number) that must remain identical across all references. Semantic search reveals the references but cannot enforce alignment; explicit pairing is the only mechanism flagging same-revision binding.

3. **Field-level schema interlock**: two or more sources declare independent fields or structural elements (e.g., a `permissions` field appearing in two template specifications, or a content-category extraction relationship where the extractor's logic depends on the source's structural taxonomy / content categories referenced by semantic name) where semantic alignment is required but the fields' definitions are formally independent. Semantic search reveals co-occurrence but does not establish the interlock relationship.

4. **Structural enumeration with strict same-revision binding**: a shared enumerable set (e.g., `unit_type` catalog, milestone identifier list, tier numbers, walking-skeleton 6-output set) appears in two or more sources where adding, removing, or renaming a value in one source MUST trigger same-revision update in the other source for the system to remain self-consistent. The binding is operationally load-bearing — divergence breaks AI execution, schema interpretation, or contract correctness — not merely descriptive.

#### Tier B: Couplings that do NOT warrant static pairing

A coupling is Tier B if all of the following hold:

- The counterparty is inside the canonical RAG layer (discoverable via `project_knowledge_search`)
- The coupling is, or will be in the same revision per the application procedure below, documented via explicit cross-reference in the originating source (named `Relationship to [X] §y`, named boundary note, named index entry, or named §-level citation in prose body)
- The coupling does not involve numeric/version alignment, field-level schema interlock, or strict-same-revision-bound structural enumeration

Tier B couplings are documented in source `Relationship to ...` header fields per §10.4 Relationship declarations + §10.5 field order, NOT in the §8.5.2 table.

#### Application procedure

When a coupling is identified during canonical authoring, revision, or audit:

1. Apply the Tier A test against the coupling
2. **If Tier A**: assign the next sequential `P-NN` ID per §8.5.4, add a row to the §8.5.2 table, add the matching rationale entry in §8.5.5, and update the `Pairings I participate in` field of every source named in the pairing in the same revision
3. **If Tier B (i.e., not Tier A)**: document the coupling in the originating source's `Relationship to ...` header field per §10 header standard in the same revision, do NOT add a row to §8.5.2

#### Examples

Drawn from the current §8.5.2 set:

| Pairing | Tier A condition satisfied | Reason |
|---|---|---|
| P-10 (WT §6.2 marker schema ↔ DTW §4.0 unit_type catalog) | 4 — Structural enumeration | Adding a new unit_type to DTW §4.0 must be reflected in WT §6.2 marker schema in the same revision, or marker schema validation fails |
| P-19 (DSG §13 ↔ skill SKILL.md files) | 1 — C2R | SKILL.md files are in Development Track repositories outside the canonical RAG layer |
| P-49 (Tools Health §3 step 7 + §5.3 ↔ CI/CD §1.1 baseline) | 2 — Numeric value alignment | Claude Code baseline version number must match across the two references |
| P-08 (TDD §4.{feature-slug}.Slice-List ↔ Conversion Spec §2.4) | 3 — Field-level schema interlock | Per-slice entry fields in TDD slice-list must align with per-slice metadata fields that Conversion Spec requires; both schemas formally independent |
| P-28 (Conversion Spec §2 + §3.8 ↔ TDD §4.{feature-slug}.Module-Decomposition + UX Design Spec §2) | 3 — Content-category extraction interlock | Conversion Spec's extraction logic depends on UX Design Spec's content-category structural taxonomy referenced by semantic name |

### 8.5.2 Static pairings (semantic-scan backstop)

Each pairing carries two type tags:

- **Update timing**:
  - **SR (Same-revision)**: downstream must be updated in the same revision as the upstream change. Divergence creates immediate operational or workflow breakage.
  - **SP (Same-period)**: downstream must be re-verified within the same working period. Divergence creates semantic misalignment that compounds over time but does not break running flow immediately.
- **Subtype**:
  - **C2C**: canonical-to-canonical (both sides are canonical source files in this hub).
  - **C2R**: canonical-to-runtime-artifact (downstream is a runtime artifact in a Development Track repository, not itself canonical).

Pairing IDs (`P-NN`) are durable identifiers — once assigned, they do not shift on retirement or insertion (per §8.5.4 ID-non-reuse rule). Retired pairings are removed from the §8.5.2 table and recorded as single-line entries in §8.5.5 catalog under their original `P-NN` ID; ID reuse is forbidden.

**Note on TDD instance-section references.** Pairings below cite TDD per-feature sub-sections in the form `§4.{feature-slug}.<Sub-Section>`. This is the instance-time chapter path that appears in produced TDDs after `{feature-slug}` substitution. The corresponding template content is owned by [TPL] Technical Design Document Template §5 (per-feature sub-section content spec) — specifically §5.1 (Header), §5.2 (Data-Model), §5.3 (API-Contracts), §5.4 (Module-Decomposition), §5.5 (Slice-List), §5.6 (Domain-Class-Hierarchy), §5.7 (Open-Questions). When verifying paired-update impact at the template level, consult those §5.x sections; when reading paired-update obligations at the produced-document level, the `§4.{feature-slug}.<Sub-Section>` form points to the matching instance section.

Similarly, pairings citing `§3`, `§3.Walking-Skeleton-Header`, or `§3.Outputs` of TDD refer to **instance-level §3 (Walking skeleton scope, Phase 1 only)** in produced TDDs. The corresponding template content is owned by [TPL] Technical Design Document Template §2.3 (`TDD body — phase-level sections — §3 Walking skeleton scope`). When verifying paired-update impact at the template level, consult §2.3 and its sub-sections; when reading paired-update obligations at the produced-document level, the instance §3 form points to the Phase 1 TDD's walking-skeleton chapter content. Note: TDD template §3 itself is the `Section applicability matrix` and is unrelated to instance §3; this dual-layer mapping applies analogously to other [TPL] sources where template content and instance content carry distinct chapter numbering.

#### Pairing table (active pairings only; retired pairings recorded in §8.5.5 catalog)

| ID | Pair | Update | Sub | Trigger condition (when paired-update obligation fires) |
|---|---|:---:|:---:|---|
| P-01 | CC substantive CCAR canonical §6 (contract testing seam) ↔ [MECH] CI/CD §2 | SR | C2C | test-type taxonomy or tier-test assignment changes (post-Phase-3: CCAR §6 contract testing seam migrated to CC substantive; CI/CD §2 milestone identity remains in residue) |
| P-03 | [MECH] DTW §4 ↔ [MECH] CI/CD §2 | SR | C2C | tasks added, renumbered, or re-scoped (milestone mapping re-verified at constitutional residue level) |
| P-06 | [TPL] PRD/Prototype/MVP ↔ [TPL] TDD (phase-level pairing) | SR | C2C | PRD phase ontology fields change (`Phase Number`, `App Slug`, Feature List, Phase 1 vs N≥2 framing) |
| P-07 | [TPL] TDD ↔ [TPL] Test Plan Schema (three-tier pairing) | SR | C2C | TDD phase-level testing strategy structure or per-feature sub-section structure changes |
| P-08 | [TPL] TDD §4.{feature-slug}.Slice-List ↔ [TPL] Conversion Spec §2.4 | SR | C2C | per-slice entry fields or metadata fields change (added, renamed, removed) |
| P-09 | [MECH] DTW §4.0 ↔ [MECH] CI/CD §2.7 (per-unit-type milestone profile) | SR | C2C | new unit_type added, milestone path modified, or scope variation revised |
| P-10 | [RULE] WT §4 marker schema ↔ [MECH] DTW §4.0 unit_type catalog | SR | C2C | catalog values change (new unit_type, value renamed, or unit_type retired) |
| P-11 | [TPL] TDD §3.Walking-Skeleton-Header + §3.Outputs ↔ [RULE] WT §3 walking-skeleton-first ordering rule | SR | C2C | walking-skeleton output set semantics change or ordering rule's gate timing/applicability changes |
| P-16 | [RULE] CCAR (constitutional residue) ↔ CC substantive CCAR | SR | Hub↔CC | post-split coupling: Hub residue's subagent topology declaration must align with CC's roster authoring; cross-references coordinated via decoupled-reference per [REF] Hub-CD-CC §5.4.4 |
| P-19 | [RULE] DSG §13 ↔ `hdc-arco-enterprise-ui` + `hdc-wcag-accessibility-checker` SKILL.md | SR | C2R | DSG changes materially (new component, breaking token change, a11y stance, Arco major upgrade) |
| P-28 | [TPL] Conversion Spec §2 + §3.8 ↔ [TPL] TDD §4.{feature-slug}.Module-Decomposition + [TPL] UX Design Spec §2 | SP | C2C | TDD per-feature structure changes (module decomposition restructured) or UX Design Spec content-category structure changes (§2 categories renamed, merged, or split) |
| P-29 | [TPL] Intent-Acceptance §2.3 + §3.9 ↔ [TPL] UX Design Spec §2 | SP | C2C | UX Design Spec content-category structural organization changes (§2 categories renamed, merged, split, or rescoped) — this is the producer-side change that requires re-verifying the consumer-side Writing Standard fields |
| P-31 | [MECH] DTW §3.3 + §3.4 ↔ [TPL] PRD §0.7 (phase ontology paragraphs starting from "Phase-level singleton + cross-phase additive evolution") + [TPL] TDD §0.7 | SP | C2C | phase ontology framing changes substantively (Phase 1 = 0→1; Phase N≥2 additive iteration; phase identity per-app) |
| P-33 | [MECH] Application Lifecycle Handoff §5.2 ↔ [RULE] WT §3 walking-skeleton ordering + [TPL] TDD §3 | SP | C2C | WT walking-skeleton ordering rule changes or TDD §3 structure changes |

**Pairings retired in Phase 3 (Hub-CC architecture refactor per [REF] Hub-CD-CC §5.4.4)** — retired because at least one counterparty source migrated fully to CC substantive canonical and the pairing no longer crosses the Hub canonical layer:

- **P-12** (was: [MECH] CQ §3 ↔ [RULE] CCAR §1) — CQ fully migrated to CC; CCAR §1 constitutional tier identity in residue; CC-internal coupling now between CC substantive CQ and CC substantive CCAR
- **P-13** (was: [MECH] Dev-Loopback §6 ↔ [MECH] CI/CD §2.6) — DLM fully migrated to CC; CI/CD §2.6 M5 identity in residue; CC-internal coupling
- **P-14** (was: [MECH] Dev-Loopback `apps/{app-slug}/dev/` ↔ [RULE] WT §4.6.3) — DLM fully migrated; WT substantive walking-skeleton 6-output set at CC; CC-internal coupling
- **P-15** (was: [MECH] Dev-Loopback `apps/{app-slug}/dev/` ↔ [RULE] CCAR §Y.1 + §Y.2) — DLM fully migrated; CCAR §Y repo layout at CC substantive; CC-internal coupling
- **P-17** (was: CC substantive Claude Code Architecture Rules canonical (subagent roster §5) + §5.3 ↔ `.claude/agents/{agent-name}.md`) — CCAR §5 subagent roster fully migrated to CC substantive CCAR; coupling is now wholly CC-internal
- **P-18** (was: [RULE] CCAR §Z ↔ `.claude/skills/{skill-name}/SKILL.md`) — CCAR §Z skill loading fully migrated to CC substantive CCAR; CC-internal
- **P-20** (was: [MECH] CQ §1–§4 ↔ lint and quality config files) — CQ fully migrated to CC; CC-internal
- **P-21** (was: [MECH] Dev-Loopback §2–§5 + §7 ↔ `apps/{app-slug}/dev/**` + `HANDOFF.md`) — DLM fully migrated to CC; CC-internal
- **P-32** (was: [RULE] Codex §1.4 ↔ [MECH] DTW §4.0 + [MECH] CI/CD §2.0) — Codex fully migrated; DTW §4.0 and CI/CD constitutional residue do not anchor to Codex specifics
- **P-34** (was: [MECH] CQ lint rules ↔ [RULE] DSG §4 + §5) — CQ fully migrated to CC; DSG stays at Hub; coupling now Hub↔CC (CC substantive CQ owns lint rule alignment with DSG)
- **P-37** (was: [MECH] Dev-Loopback §7 ↔ [MECH] Application Lifecycle Handoff §3.1 + §4.3) — DLM fully migrated; ALH stays at Hub; coupling now Hub↔CC
- **P-38** (was: [MECH] Dev-Loopback §4 + §6 ↔ [MECH] DTW §4.0.2 + TK-04 / TK-05 / TK-08 / TK-13) — DLM fully migrated; DTW TK-04+ at CC substantive; CC-internal
- **P-49** (was: [MECH] Tools Health Cadence §3 step 7 + §5.3 ↔ [MECH] CI/CD §1.1 baseline) — THC fully migrated; CI/CD §1.1 tooling baseline at CC substantive; CC-internal
- **P-50** (was: [MECH] Tools Health Cadence §5 P0 inventory + §3 step 6 ↔ [MECH] CQ §1 / §2 tool stack + §8.5 Renovate) — both sides fully migrated to CC; CC-internal
- **P-51** (was: [MECH] Tools Health Cadence §3 step 8 + §5.4 ↔ [MECH] Dev-Loopback §6 + §2.3) — both sides fully migrated to CC; CC-internal
- **P-52** (was: [MECH] Tools Health Cadence §5 P0 inventory ↔ [RULE] WT §3 tool stack per node) — THC fully migrated; WT §3 substantive tool stack at CC; CC-internal
- **P-53** (was: [MECH] Dev-Loopback §4.4 secret loading ↔ [MECH] CQ §1.7 gitleaks + §1.2 + §4.6) — both sides fully migrated to CC; CC-internal

The retired pairings are preserved as durable `P-NN` IDs per §8.5.5 rationale catalog; they are not re-issued for new pairings.

**Pairings updated in Phase 3** (§ references in active pairings updated to match constitutional residue § numbers):

- **P-09** § reference: `[MECH] CI/CD §2.0` → `[MECH] CI/CD §2.7` (the per-unit-type milestone profile is at §2.7 in the constitutional residue)
- **P-10** § reference: `[RULE] WT §6.2 marker schema` → `[RULE] WT §4 marker schema` (interface contract at §4 in the constitutional residue)
- **P-11** § reference: `[RULE] WT §4.6.2 + §4.6.3` → `[RULE] WT §3 walking-skeleton-first ordering rule` (constitutional walking-skeleton ordering at §3)
- **P-33** § reference: `[RULE] WT §4.6` → `[RULE] WT §3 walking-skeleton ordering`

For the design rationale of each pairing and historical record of retired pairings (durable `P-NN` IDs), see §8.5.5 Pairing rationale catalog.

### 8.5.3 Canonical name and § numbering discipline

When a canonical source's name (family prefix or kebab identifier) changes per §8.8, or when its internal § numbering is restructured, every citation in every other canonical source must be grep-verified and updated in the same revision. This discipline applies across the full canonical set and is independent of the pairings in §8.5.2.

This discipline also applies to navigation/index sections inside canonical sources — sections whose function is to enumerate cross-source pointers rather than encode rules of their own (e.g., the Hub Claude behavior contract index in [RULE] Claude Platform Behavior §5, or any future analogous index). Index sections are pure read views over their referenced sources; when a referenced § is renamed, renumbered, or retired, the index entry must be updated in the same revision.

### 8.5.3a Grep-verify operational layer

The grep-verify discipline in §8.5.3 runs against **the canonical set as visible to Hub Claude through `project_knowledge_search`** (the project knowledge base / RAG layer). The RAG layer is the authoritative canonical-set view because it is what Hub Claude actually consumes during conversation per §1.4 audience model.

Under the current GitHub-sync mechanism, the canonical repository (e.g., the operator's `claude-canonical` GitHub repo) commits flow into the RAG layer via the project knowledge base re-indexing pipeline. The hub Claude.ai platform may additionally expose an auxiliary filesystem view; when present, such a view is secondary and may diverge from the RAG layer for indexing-timing or mounting reasons. The RAG layer wins on any divergence.

When verifying citations during a revision:
- Use `project_knowledge_search` with the citation target (e.g., `[OS] §4.3`) as the query; confirm the target is reachable and content matches the cited claim
- For exact-string verification (e.g., a § number rename), bash grep against the canonical repository clone (or the filesystem view if mounted) is acceptable as a supplementary check, but is not authoritative when the view diverges from the RAG layer — the RAG layer wins
- When the operator commits to a structural change (rename, renumbering, retirement), ensure the change reaches the RAG layer before declaring §8.5.3 verified; if the project knowledge base ingestion is asynchronous (typical under GitHub-sync), wait for ingestion to complete before final sign-off

This rule applies to canonical-to-canonical citations only. Canonical-to-runtime-artifact (C2R) pairings in §8.5.2 verify against the Development Track repository per the C2R subtype's own discipline.

### 8.5.4 Maintenance

The static-pairing list in §8.5.2 is not exhaustive. When a new coupling is identified, first apply the §8.5.1a Tier discrimination test. Only if the coupling is Tier A — particularly a canonical-to-runtime-artifact mirror, a numeric/version value alignment, a field-level schema interlock, or a structural enumeration with strict same-revision binding — assign the next sequential `P-NN` ID, add a row to the §8.5.2 table, and add the matching rationale entry in §8.5.5. Tier B couplings are documented in source `Relationship to ...` header fields per §10 and do not enter §8.5.2.

When a pairing is retired (e.g., by SOT consolidation that eliminates the coupling, or by Tier reclassification from A to B), **remove its row from the §8.5.2 table** and convert its §8.5.5 catalog entry to a single-line `RETIRED` record with the retirement reason. **ID reuse is forbidden** — the original `P-NN` ID remains permanently assigned to the retired coupling in §8.5.5 so that historical references in past work artifacts remain resolvable.

When a pairing is added, modified, or retired, the `Pairings I participate in` header field of every source named in the pairing must be updated in the same revision. Divergence between the §8.5.2 table and source-side `Pairings I participate in` fields constitutes an anti-drift signal per §12.

### 8.5.5 Pairing rationale catalog

This catalog holds the design rationale for each active pairing in §8.5.2 — what specifically breaks at runtime if the pairing is not honored, and how the failure manifests. Retired pairings are recorded as single-line entries to preserve durable `P-NN` ID resolvability per §8.5.4 ID-non-reuse rule. Use this catalog when evaluating whether a proposed change crosses a pairing's threshold of "substantive" or whether a near-divergence is operationally tolerable.

#### Active pairings

- **P-01** — When test-type taxonomy or tier-test assignment changes in CCAR §6, the milestone gating semantics in CI/CD §2 must be re-aligned in the same revision; otherwise M1 / M2 / M3 gates either reject valid work under new test categories or admit incomplete coverage of removed categories.
- **P-03** — When DTW §4 task catalog adds, renumbers, or re-scopes a TK, the milestone mapping in CI/CD §2 must be re-verified; otherwise the TK-to-milestone mapping in operator-facing scheduling becomes inconsistent.
- **P-06** — PRD and TDD pair 1:1 at the phase level (one PRD + one TDD per app per phase). When PRD's phase ontology fields change, TDD's matching header fields and §0.7 / §0.8 framing must be re-verified for symmetry; divergence creates a paired-artifact mismatch that breaks TK-02 production.
- **P-07** — TDD's phase-level testing strategy drives the phase test plan (master, markdown); per-feature `§4.{feature-slug}` content drives the feature integration test plan; per-feature `§4.{feature-slug}.Module-Decomposition` plus slice acceptance drives the slice test plan. When TDD's phase-level testing strategy structure or per-feature sub-section structure changes, all three test plan tier schemas must be re-verified.
- **P-08** — The per-slice entry fields in TDD slice-list must align with the per-slice metadata fields that Conversion Spec requires each extracted slice to record at TK-03. When either side's field set changes (added, renamed, or removed), the other must be re-verified so a slice-list produced per TDD remains directly consumable under Conversion Spec without reformatting.
- **P-09** — DTW §4.0 catalog and CI/CD §2.0 profile hold the same data viewed from two angles (per-unit-type task path vs per-unit-type milestone subset). When either side changes, the other must update in the same revision; divergence creates immediate operational ambiguity for Hub Claude scheduling and Claude Code execution.
- **P-10** — The marker block is the GitHub-side canonical record of unit metadata for active execution; the Workflow §4.0 catalog is the canonical-side definition of allowed unit_type values. When catalog values change, the marker block schema's `unit_type` field allowed-values list must be re-verified; divergence breaks marker-block parsing in observability tooling and breaks the cross-reference path between TDD §3 Walking-Skeleton-Header and the GitHub Issue marker block authored at TK-04 entry per [MECH] Development Track Workflow §TK-04 role sequence step 2.
- **P-11** — TDD §3 specifies the author-facing structure for documenting walking-skeleton metadata and outputs; WT §4.6.2 + §4.6.3 own the ordering rule and the canonical 6-output enumeration. When the 6-output set or the ordering rule changes, TDD §3 reference text must update in the same revision; divergence creates a Phase 1 TDD that documents non-canonical walking-skeleton expectations, breaking the design freeze coherence of walking-skeleton scope at Hub TK-03 cross-model review.
- **P-12** [RETIRED in Phase 3] — Original rationale: CQ §3 lint rules (TypeScript: dependency-cruiser + ESLint `no-restricted-imports`; Java: ArchUnit) encode the tier-boundary semantics declared in CCAR §1.1 / §1.2 / §1.3. When CCAR tier semantics change, the §3 lint rule encoding must update in the same revision; divergence creates immediate operational break — lint either rejects valid code or admits violations.
- **P-13** [RETIRED in Phase 3] — Original rationale: Dev-Loopback §6 declares four acceptance assertions supplementing the CI/CD §2.6 M5 gate when the unit is `walking_skeleton`; acceptance failure on any §6 assertion blocks M5 completion. When CI/CD §2.6 acceptance criteria or scope change, the §6 assertions must be re-verified in the same revision; divergence creates immediate gate-logic ambiguity (over-gate or under-gate the walking_skeleton unit at M5).
- **P-14** [RETIRED in Phase 3] — Original rationale: Dev-Loopback introduces a new `apps/{app-slug}/dev/` subdirectory as part of the walking_skeleton unit's Output #6; this directory is not yet enumerated in WT §4.6.3, and the cross-reference is the binding declaration of the directory's existence. When WT §4.6.3 changes Output #6 structure or enumerates `dev/`, the Dev-Loopback ownership claim must be re-verified in the same revision; divergence creates conflicting source-of-truth for what the walking_skeleton unit produces.
- **P-15** [RETIRED in Phase 3] — Original rationale: Dev-Loopback extends the app-scoped tree declared in CCAR §Y.1 with a new `dev/` subdirectory; future enumeration of `dev/` in §Y.1 must follow the §Y.2 path-stability procedure. When CCAR §Y.1 app-scoped tree structure changes (path renaming or restructuring), Dev-Loopback directory references must be re-verified in the same revision; divergence creates path-resolution ambiguity for dev-loopback artifacts at TK-04 / TK-13.
- **P-16** — `.claude/config/context-scopes.yaml` is the runtime mirror of CCAR §X agent context scope policy. The yaml is downstream, not canonical, but its content must remain consistent when scope allow/deny lists or agent assignments change; divergence breaks bias-firewall enforcement at runtime.
- **P-17** [RETIRED in Phase 3] — Original rationale: Agent definition files in `.claude/agents/` are downstream deliverables, not canonical, but their content (purpose, frontmatter `tools` field, system prompt) must remain consistent with the §5.1 roster definition and §X context scope assignment. When the roster or scope assignment changes, affected agent files must update in the same revision; divergence breaks bias-firewall enforcement at runtime.
- **P-18** [RETIRED in Phase 3] — Original rationale: Skill definition files in `.claude/skills/` are downstream deliverables, not canonical, but their content (load triggers, scope, override behavior) must remain consistent with the §Z.1 catalog and §Z.2 trigger conditions. When the catalog or trigger conditions change, affected SKILL.md files must update in the same revision; divergence breaks skill loading at runtime.
- **P-19** — When DSG changes materially (new component, breaking token change, a11y stance change, Arco major version upgrade), skill prompts in `hdc-arco-enterprise-ui` and `hdc-wcag-accessibility-checker` may need adjustment. Governance is per DSG §12.
- **P-20** [RETIRED in Phase 3] — Original rationale: Lint and quality configuration files (`<repo-root>/.prettierrc`, `eslint.config.js`, `tsconfig.base.json`, `dependency-cruiser.config.js`, `checkstyle.xml`, `pmd-ruleset.xml`, `archunit-rules/**`) are downstream mirrors carrying the canonical rule set's enforcement encoding. When the canonical adds, removes, or re-scopes a rule preset / architecture-lint pattern / severity policy / AI-era augmentation rule, affected configuration files must update in the same revision; divergence breaks deterministic quality enforcement at runtime.
- **P-21** [RETIRED in Phase 3] — Original rationale: Runtime artifacts under `apps/{app-slug}/dev/**` plus `apps/{app-slug}/HANDOFF.md` migration document are downstream mirrors carrying the canonical dev-loopback contract. When the canonical revises startup ceiling, fixture role-coverage rules, placeholder pattern, ENV detection items, or migration documentation requirements, affected runtime artifacts must update in the same revision; divergence breaks dev-loopback acceptance assertions at TK-13 M5 gate.
- **P-28** — Module-driven slicing (Conversion Spec §2) depends on TDD producing MECE per-feature module decomposition; UX brief extraction (§3.8) depends on a CD-authored UX Design Spec instance being present when Tier 1 is involved. When TDD per-feature sub-section structure changes, the module-side extraction rules must be re-verified; when UX Design Spec content-category structure changes (§2 categories renamed, merged, or split), the UX-side extraction rules in Conversion Spec §3.8 must be re-verified.
- **P-29** — The Intent-Acceptance Writing Standard references UX Design Spec instance content categories by semantic name (Affected Tier 1 scope, layout pattern selection, components referenced, new components or tokens, accessibility call-outs, internationalization call-outs) rather than by § number. When UX Design Spec content-category structural organization changes (§2 categories renamed, merged, split, or rescoped), the semantic references in Writing Standard §2.3 UX brief sub-section field rules and §3.9 accessibility_expectations source mapping must be re-verified.
- **P-31** — When phase ontology framing (Phase 1 = 0→1; Phase N≥2 = additive iteration; phase identity is per-app) changes substantively in DTW §3.3 + §3.4, the PRD §0.7 phase ontology and TDD §0.7 phase ontology must be re-verified for continued symmetry.
- **P-32** [RETIRED in Phase 3] — Original rationale: The Codex §1.4 fire conditions table is derived from the conjunction of (a) DTW §4.0 unit_type catalog, (b) CI/CD §2.0 milestone profile, and (c) Codex §3.1 / §3.2 command-to-milestone anchors. When any of (a) / (b) / (c) changes, §1.4 must be re-verified for continued correctness.
- **P-33** — When WT §4.6 changes substantively (sub-section restructured, ordering rule modified, output set revised) or TDD §3 structure changes (Walking-Skeleton-Header field set modified, Scope-And-End-To-End-Coverage requirements revised), Handoff §5.2 walking-skeleton-first ordering note and source state pointer table must be re-verified.
- **P-34** [RETIRED in Phase 3] — Original rationale: CQ encodes DSG token consumption (CSS-variable-only) and component import allow-list (Tier A Arco + Tier B HDC custom) as ESLint rules. When DSG adds a token, component, or changes consumption rules, the corresponding ESLint rule list must be re-verified within the same working period.
- **P-37** [RETIRED in Phase 3] — Original rationale: Dev-Loopback §7 introduces `apps/{app-slug}/HANDOFF.md` (technical migration guide) extending Handoff §3.1 mandatory content; this artifact is distinct from the §4.3 `apps/{app-slug}/handoff-record.md` (governance acknowledgment record). When Handoff §3.1 mandatory content list or §4.3 record format changes, Dev-Loopback §7 documentation requirements must be re-verified within the same working period.
- **P-38** [RETIRED in Phase 3] — Original rationale: Dev-Loopback artifacts are produced by TK-04 per DTW §4.0.2 as part of the walking_skeleton unit's output; consumed by TK-05 (M1 whitebox) and TK-08 (M2 contract / external integration); TK-13 (M5 staging deploy) gates on §6 acceptance assertions when the unit is `walking_skeleton`. When DTW §4.0.2 walking-skeleton output set or these TK semantics change, Dev-Loopback §4 / §6 references must be re-verified within the same working period.
- **P-49** [RETIRED in Phase 3] — Original rationale: When CC substantive CI/CD Milestone Policy canonical (Claude Code tooling baseline) tooling baseline changes (Claude Code version pinning, upgrade verification procedure, or supported version range), the [MECH] Tools Health Cadence §3 step 7 reference and §5.3 AI-dev infrastructure inventory must be re-verified within the same revision; divergence creates immediate sequencing inconsistency where the Tools Health Cadence step 7 baseline check fires against a stale baseline definition.
- **P-50** [RETIRED in Phase 3] — Original rationale: When [MECH] Code Quality Rule Set §1 / §2 tool stack changes or when §8.5 Renovate Governance config policy changes, the [MECH] Tools Health Cadence §5 P0 inventory and §3 step 6 expectations must be re-verified within the same revision; divergence creates immediate semantic drift where the Tools Health Cadence inventory does not match the actual quality tooling.
- **P-51** [RETIRED in Phase 3] — Original rationale: When [MECH] Dev-Loopback Mode §6 walking-skeleton M5 acceptance assertions or §2.3 readiness ceiling changes, the [MECH] Tools Health Cadence §3 step 8 verification expectation must be re-verified within the same working period.
- **P-52** [RETIRED in Phase 3] — Original rationale: When [RULE] Workspace Topology §3 tool stack per node changes (tool added, removed, substituted, or version-policy changed), the [MECH] Tools Health Cadence §5 P0 inventory must be re-verified within the same revision.
- **P-53** [RETIRED in Phase 3] — Original rationale: When [MECH] Dev-Loopback Mode §4.4 secret loading contract changes or when [MECH] Code Quality Rule Set §1.7 gitleaks / §1.2 hdc/no-inline-secret-literal / §4.6 secret leakage detection rule changes, both sides must be re-verified within the same revision; divergence creates immediate inconsistency where the positive-side secret-loading contract does not match the negative-side enforcement.

#### Retired pairings (durable `P-NN` ID resolution only)

- **P-02**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-04**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-05**: RETIRED in single-M5 revision. AI-dev side no longer produces release tags; handoff tag namespace `handoff/{app-slug}/{YYYY-MM-DD}` is the sole canonical tag namespace.
- **P-22**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-23**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-24**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-25**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-26**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-27**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-30**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-35**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-36**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-39**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-40**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-41**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-42**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-43**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-44**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-45**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-46**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-47**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-48**: RETIRED in Wave 2 Tier rationalization (Tier B per §8.5.1a).
- **P-12**: RETIRED in Phase 3 Hub-CC architecture refactor (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] CQ fully migrated to CC substantive canonical.
- **P-13**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated to CC substantive canonical.
- **P-14**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated to CC substantive canonical.
- **P-15**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated to CC substantive canonical.
- **P-17**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). CC substantive Claude Code Architecture Rules canonical (subagent roster §5) subagent roster fully migrated to CC substantive CCAR canonical; pairing now wholly CC-internal.
- **P-18**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). [RULE] CCAR §Z skill loading fully migrated to CC substantive CCAR canonical; pairing now wholly CC-internal.
- **P-20**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] CQ fully migrated to CC substantive canonical.
- **P-21**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated to CC substantive canonical.
- **P-32**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [RULE] Codex Plugin Usage fully migrated to CC substantive canonical.
- **P-34**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] CQ fully migrated; Hub↔CC coupling (CC substantive CQ owns lint rule alignment with DSG) is governed by CC substantive canonical.
- **P-37**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated; CC substantive DLM aligns with ALH §3.1 / §4.3 at CC's discretion.
- **P-38**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Dev-Loopback Mode fully migrated; coupling between CC substantive DLM and DTW TK-04+ is CC-internal.
- **P-49**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] Tools Health Cadence fully migrated to CC substantive canonical; CI/CD §1.1 tooling baseline at CC substantive.
- **P-50**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Both counterparties ([MECH] THC + [MECH] CQ) fully migrated to CC substantive canonical.
- **P-51**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Both counterparties ([MECH] THC + [MECH] DLM) fully migrated to CC substantive canonical.
- **P-52**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Counterparty [MECH] THC fully migrated; WT §3 substantive tool stack at CC.
- **P-53**: RETIRED in Phase 3 (per [REF] Hub-CD-CC §5.4.4). Both counterparties ([MECH] DLM + [MECH] CQ) fully migrated to CC substantive canonical.

**Phase 3 retirement note**: Narrative rationale entries above (under §8.5.5 Pairing rationale catalog) for P-12, P-13, P-14, P-15, P-17, P-18, P-20, P-21, P-32, P-34, P-37, P-38 are retained as historical record. They describe couplings that previously existed at the Hub canonical layer; under Premise 5 these couplings now exist at CC's substantive canonical layer or as Hub↔CC decoupled-reference pointers, neither of which is tracked in this Hub-side pairing table.

### 8.5.6 Cat 4 source map

This section is a read view across the seven cross-cutting Cat 4 sources from the `[RULE]` and `[MECH]` families that govern Claude Code execution architecture, infrastructure, orchestration, gating, and cross-tool workflow at the Hub canonical layer (post-Phase-3 Hub-CC architecture refactor per [OS] §0.1.5 Premise 5). Each source's authoritative scope statement remains in its own §0 / §1 boundary chapter; this map exists so that readers can locate ownership across the family without grepping every source header.

`[TPL]` Cat 4 sources (specification-support templates such as TDD template, PRD template) are out of scope of this map; their ownership is template-level (which produced-artifact section each template authors), governed by the `Relationship to adjacent [TPL] sources` header field convention rather than by this map.

**Post-Phase-3 Hub-side Cat 4 source inventory**:

| Source | Primary axis | Owns (post-Phase-3 Hub-side scope) |
|---|---|---|
| `[RULE] Claude Code Architecture Rules` (CCAR) — **constitutional residue** | Static structure (constitutional) | Three-tier architecture identity (§1), Tier 2 thinning rule (§2), permission decision placement principle (§3), CLAUDE.md hierarchy existence pointer (§4), subagent topology existence (§5), high-level monorepo structure (§6), cross-workspace anti-drift signals (§7). **CC-side substantive**: A1-A10 subagent roster, named context scopes, repository path patterns, skill catalog, domain lifecycle and contract-testing operational specifics (at CC substantive CCAR canonical) |
| `[RULE] Workspace Topology` (WT) — **constitutional residue + Hub-internal substantive** | Multi-node infrastructure (constitutional) + Hub Claude behavior in node-related conversations (Hub-internal substantive) | Multi-node existence and naming convention (§1), parity discipline (§2), walking-skeleton-first ordering rule (§3), node-assignment interface contract (§4), workspace inception governance (§5), cross-workspace anti-drift (§6), Hub Claude trigger phrases (§7, Hub-internal substantive), Hub Claude observability boundary (§8, Hub-internal substantive). **CC-side substantive**: specific tool stack and versions, GitHub workflow configuration, node-assignment 4-step procedure, workspace inception checklist, operational anti-drift (at CC substantive WT canonical) |
| `[RULE] Design System Governance` (DSG) | Tier 1 design language governance | Singleton instance model (§1), instance section contract (§2), implementation path rules (§3), token governance (§4), component governance (§5), accessibility stance (§6), i18n & RTL governance (§7), motion hygiene (§8), iconography rules (§9), content style governance (§10), platform tier framework (§11), update flow (§12), custom skill integration (§13), pairing rules (§14), reviewer checklist (§15), anti-drift red flags (§16). Unchanged in Phase 3 — DSG is fully Hub canonical |
| `[MECH] Development Track Workflow` (DTW) — **constitutional residue + Hub-internal substantive** | Task-level orchestration (constitutional) + Hub-authored task content (Hub-internal substantive) | TK-01 through TK-13 identity (§4); full Hub-authored substantive content for TK-01 / TK-02 (with sub-steps) / TK-03 (Hub-internal substantive); TK-12 M4 operator gate (Hub-internal substantive); unit_type catalog (§4.0, constitutional interface); transition mechanism catalog (§5); human intervention budget (§6); failure routing matrix (§7); cross-workspace anti-drift (§8); Hub Claude soft compliance trigger phrases (§9, Hub-internal substantive). **CC-side substantive**: TK-04 through TK-11 + TK-13 execution mechanics including specific subagent invocations and tool commands (at CC substantive DTW canonical) |
| `[MECH] CI/CD Milestone Policy` — **constitutional residue** | Lifecycle gating (constitutional) | M0–M5 ladder identity (§2.1-§2.6), per-unit-type milestone profile interface (§2.7), Test Evidence Report schema (§3), required artifact output gates (§4), multi-node evidence parity invariant (§1.2), cross-workspace anti-drift (§5). **CC-side substantive**: gate criteria per M-N, tooling baseline, accessibility thresholds, slice-size advisory, stuck recovery, code review tool operational specifics, performance test scope (at CC substantive CI/CD canonical) |
| `[MECH] Application Lifecycle Handoff` (ALH) | App-to-human-team transition | Application lifecycle stages (§1), handoff readiness criteria (§2), content scope (§3), mechanism (§4), tag namespace (§4.1), re-entry policy (§5). Unchanged in Phase 3 |
| `[MECH] Cross-Tool Workflow Handoff` (CTWH) | Cross-tool content flow contracts | Three operator-mediated handoff paths (Hub ↔ CD, Hub ↔ CC, CD ↔ CC), per-direction content contracts (§2-§4), reminder-form discipline (§5), audit-failure handling (§6), Hub Claude trigger phrases for cross-tool handoff (§7), CD ↔ CC decoupled-by-default discipline during research preview (§4.4). Unchanged in Phase 3 |

**Sources fully migrated to CC substantive canonical in Phase 3 (no Hub Cat 4 residue retained)**:
- `[RULE] Codex Plugin Usage` → CC substantive Codex Plugin Usage canonical (code review tool semantics, command catalog, trigger logic, evidence path schema)
- `[MECH] Code Quality Rule Set` → CC substantive Code Quality Rule Set canonical (Tier 1/2/3 tools, presets, custom architecture lint rules, severity policy, CI integration)
- `[MECH] Dev-Loopback Mode` → CC substantive Dev-Loopback Mode canonical (single-command startup, fixture content, placeholder pattern, env switch gate, walking-skeleton M5 acceptance assertions, HANDOFF.md)
- `[MECH] Tools Health Cadence` → CC substantive Tools Health Cadence canonical (trigger model, execution protocol, action-item prioritization, quarterly report structure, P0 inventory)

Hub-side handoff documentation and Hub-authored TDDs that previously referenced these four migrated sources by name now reference either the generic concept (e.g., "code review gate") or "CC substantive X canonical" per the decoupled-reference model in [REF] Hub-CD-CC Architecture.

**Ownership rule**: Any topic listed in one Hub-side source's "Owns" column is canonically owned by that source at the Hub layer (constitutional + Hub-internal substantive scope). CC-internal operational details for split sources are owned by CC substantive canonical at CC's own canonical layer. Other Hub Cat 4 sources reference but do not redefine. When a topic's owner is genuinely ambiguous (operationally relevant to multiple sources), surface as anti-drift signal per §12 rather than dual-owning.

**Cross-source dependency lookup**: To discover which canonical sources depend on or extend a given Cat 4 source, consult the counterparty sources' `Relationship to ...` header fields (Tier B couplings per §8.5.1a) and §8.5.2 active pairing table (Tier A couplings).

### 8.5.7 Harness re-architecture trigger

The pairing system in §8.5.2 grows additively over time: new couplings are recognized, new sources enter the canonical set, existing sources accumulate sub-sections. Past a certain scale, the harness's complexity itself becomes the failure mode.

When any of the following thresholds is reached, surface as an anti-drift signal per §12 and initiate a structured re-architecture evaluation **before** adding more pairings, sources, or anti-drift dimensions to the affected layer:

- §8.5.2 active pairings exceed **50**
- Anti-drift red flag **chapter** count across canonical sources exceeds **20** (counted as h1 anti-drift chapters across any canonical source, with [OS] §12 anti-drift corrections catalog and its sub-sections counted as one)
- Active canonical source files exceed **30**
- A single source's body exceeds **1500 lines**
- A single source's `Pairings I participate in` field lists more than **10 pairings**

**Anti-drift threshold counting basis**: "Chapter count" means each h1 chapter in a canonical source whose primary topic is anti-drift enumeration, plus the [OS] §12 anti-drift corrections catalog counted as one. Sub-section-embedded anti-drift content (e.g., per-principle "Red flags" sub-sections in `[PRIN]` principle chapters; nested anti-drift sub-sections under non-anti-drift parent chapters) does NOT count as a separate dimension.

**Current threshold status (post-§0.1.4 D7 cleanup)**:

- **§8.5.2 active pairings**: below the 50-pairing threshold.
- **Active canonical source files**: crosses the 30-file threshold. Re-architecture evaluation concluded "no action; the additional sources address distinct architectural concerns (cross-tool flow, decision record discipline, phase-level test plan, three-workspace architecture) with non-overlapping primary axes per §9.2".
- **Anti-drift chapter count, single-source body length, single-source pairings**: all below threshold.

**Hub-source pattern**: A subset of canonical sources has an inherently cross-cutting primary axis (lifecycle gating, task orchestration, or cross-source ownership mapping) that naturally accumulates high pairing fan-out as a consequence of their integration role. Hub-source designation is determined by §8.5.6 Cat 4 source map's `Primary axis` column (cross-cutting integration roles), not self-declared. For hub-pattern sources, the ">10 pairings" threshold remains binding but is interpreted as "expected breach justifying documentation of role, not structural change". For non-hub sources, crossing >10 pairings triggers full structured re-architecture evaluation.

**Second-tier backstop**: if any single hub source crosses **12** pairings, OR if two or more hub sources simultaneously breach >10, re-architecture evaluation fires unconditionally regardless of hub-source designation. The 12-pairing ceiling reflects the empirical complexity ceiling above which paired-update obligations measurably exceed operator working-memory capacity.

Adding a source to the hub-source list requires same-revision update to §8.5.6 + this paragraph + §12 anti-drift catalog conditional firing rule.

**Re-architecture evaluation considers**:

- **SOT consolidation** — multiple sources covering near-overlapping topics, where a single SOT would reduce cross-reference burden
- **Source splitting** — a single source carrying multiple primary axes that the §9.2 primary-axis judgment test would now split
- **Pairing deprecation** — couplings that no longer reflect operational reality (mark `RETIRED` per §8.5.4 rather than delete)
- **Index restructuring** — when a single index becomes longer than its referenced detail
- **Header field budget** — when source headers consistently exceed 20+ fields, consider promoting some Relationship fields to a centralized cross-reference map

The evaluation produces an Options Paper at the hub level (per [TPL] Options Paper); structural changes flow through §8.8 superseding rule.

## 8.6 Anti-duplication rule

Do not create a substantially duplicative canonical source. Prefer updating, replacing, or consolidating the existing source that already owns the domain.

## 8.7 Conflict-handling rule

If conflict, overlap, duplication, or boundary ambiguity exists, surface it before generating the final source file.

## 8.7a [OS] vs downstream conflict

When a specific source, template, or rule disagrees with this operating model, prefer the specific source only after surfacing the disagreement. If the change is durable, update this operating model in the same revision so that the model's stability remains the baseline against which downstream drift is detectable.

## 8.8 Superseding rule

Each stable source has one active canonical version. Replace in place rather than creating variants.

## 8.8a Source retirement procedure

A canonical source is **retired** rather than deleted when its content is fully absorbed into another canonical source (consolidation), when its scope is permanently obsoleted by an architectural change, or when the durable-first / one-source-one-job rules can no longer be satisfied by the source as authored. Retirement is distinct from superseding (§8.8): superseding produces a same-named replacement that absorbs the prior version's identity; retirement removes the source from the active canonical set without a same-named successor.

**Procedure**:

1. **Confirm absorption or obsolescence**: every load-bearing rule in the source being retired must either (a) already exist in another canonical source, or (b) be promoted to another canonical source in the same revision that retires this one. Orphan rules — rules that disappear from the canonical set entirely — are not permitted as a retirement side effect.

2. **Mark the file, do not delete it**: rename the source file to add a `.RETIRED.YYYY-MM-DD` suffix (e.g., `hdc_tpl_lessons-harvest-memo.RETIRED.2026-03-15.md`) and place a single-paragraph retirement notice at the top of the file body declaring (a) the retirement date, (b) the canonical source(s) that absorb the prior content, and (c) a back-pointer to the §8.10 reserved-empty registry entry if applicable. The file remains in the canonical repository (and thereby in the project knowledge base after re-indexing) for historical resolution of past references.

3. **Update §8.5.2 pairings**: every pairing the retired source participates in is handled per §8.5.4 — remove the §8.5.2 row, convert the §8.5.5 catalog entry to a single-line `RETIRED` record. ID reuse is forbidden.

4. **Update PI enumeration**: if the retired source was listed in PI's canonical-source enumeration, remove the entry in the same revision (operator-side via Claude.ai project settings UI).

5. **Update cross-references**: every other canonical source citing the retired source must update its `Relationship to ...` header field and any in-body cross-references in the same revision per §8.5.3 grep-verify discipline.

6. **Optional reserved-empty registry entry**: if the retirement leaves a domain-shaped gap that may be filled later, register the slot in §8.10 with activation criteria.

## 8.9 Source-ready generation protocol

### Trigger

The protocol activates when the user explicitly asks for a source-ready canonical file, or when the user promotes a working artifact to canonical-source status.

### Required pre-generation declarations

Before generating the final source-ready Markdown, state:
- routing decision (which hub zone or file the source belongs to)
- output family (management-system output, specification-support artifact, or canonical source outside L2-L5; see Section 5)
- governing anchor, if the source extends or applies another canonical source
- intended source prefix (see §9.2)
- intended file name (see §9.1 and §9.3)
- active consistency-check scope (which canonical sources the consistency check in §8.5 will run against)
- active format authority, if format materially affects the source (e.g., when the source itself documents DingTalk Markdown syntax)
- mechanism verification status, when the source declares how an external tool, system, or mechanism behaves (per the Mechanism verification rule below)
- constitutional / substantive placement per §0.1.5 Premise 5: declare whether the source is (a) cross-workspace constitutional content owned by Hub canonical, (b) Hub-internal substantive content owned by Hub canonical, or (c) CC-internal substantive content that should not be generated at Hub. Option (c) blocks Hub generation and routes the source to CC's canonical layer per [REF] CC Project Memory Bank Layout. For [MECH] sources, additionally confirm §0.1.6 Premise 6 compliance (no implicit dependence on human-team primitives)

### Generation

After the pre-generation declarations are stated, generate the final source-ready Markdown in one pass, following the canonical source header standard in Section 10.

### Mechanism verification rule

When a canonical source declares how an external tool, system, or mechanism behaves — for example, third-party CLI command semantics, GitHub Actions trigger conditions, MCP protocol behavior, vendor product configuration semantics, branch protection settings, or release-channel mechanics — the declaration must be backed by a citation to authoritative external documentation (vendor official docs, RFC, or equivalent). Inferential markers (`[推断·演绎]`, `[通识]`) and parametric memory are not admissible as the sole basis for declaring external mechanism behavior.

If verification cannot be completed before generation (e.g., the authoritative documentation is unavailable or the mechanism is genuinely undocumented), the declaration is held back: a v0 placeholder is documented inline with an explicit calibration trigger (per [PRIN] HR Digital Decision Design Principles §5 management mechanism over ad hoc control), rather than fabricating mechanism details from inference alone.

This rule applies to canonical source generation only. Specification outputs (PRD, TDD, intent, acceptance, test-plan) may declare mechanism behavior with the source citations governed by their respective templates, and are not bound by this rule.

### Scope exclusion

Do not apply this protocol to normal chat-level working artifacts or initiative-specific specification outputs unless the user explicitly requests it.

## 8.10 Reserved-empty registry

The following slots are deliberately empty in the current canonical set, with documented activation criteria.

- **Cat 3 (Configuration workbook production)** — see §2.3.5. Activation when the first configuration-workbook production workflow for a specific vendor product or product family matures to a reusable [TPL] family member.
- **Cat 1 detailed-template family** — Cat 1 governs L1 management-system anchors (per §2.3.1). Detailed templates under Cat 1 are not authored at hub canonical level, since L1 anchor authoring belongs to enterprise policy implementation outside hub scope. Activation: not anticipated in current project scope.
- **Lessons-harvest memo template** — retired in the Path B2 refactor; lessons-harvest is captured operationally via `MANUAL_*` artifacts under §9.4 rather than via a dedicated [TPL] family member. Re-activation as canonical [TPL] only if a stable lessons-harvest pattern emerges across 5 or more uses and the operational artifact form starts to constrain rather than enable the harvest work.

When a slot is activated, the activating revision moves the entry from this registry to the appropriate location (a new § block, a new [TPL] file, etc.) and the registry entry is replaced by a back-pointer.

---

# 9. File naming convention

## 9.1 Standard format

`hdc_<prefix>_<short-kebab-name>.md`

## 9.2 Allowed prefixes

- `os` — operating rules and systems (this project operating model)
- `prin` — judgment principles
- `pol` — policy architecture and policy documents
- `tpl` — deliverable templates
- `ref` — domain content catalogs
- `rule` — format, tool, and architecture rules. Format rules govern output discipline (e.g., DingTalk Markdown specification). Tool rules govern tool/platform behavior (e.g., Claude Platform Behavior). Architecture rules govern code or infrastructure structure (e.g., Claude Code Architecture, Workspace Topology, Design System Governance).
- `mech` — governance mechanism specifications. Mech sources specify gating, milestone progression, task orchestration, and inter-actor protocols. Distinguished from `rule` by primary axis: `rule` declares what something is or how it must be formatted; `mech` declares how a multi-step governed process unfolds and what gates apply at each step.

A `rule` source MAY contain ancillary process/gate sub-sections (e.g., a workflow chapter, a gate-trigger chapter) when those sub-sections are operationally inseparable from the primary rule subject. Examples: `[RULE] Workspace Topology` constitutional residue §4 Node-assignment interface contract is an operational extension of the topology rule itself. The `rule`-vs-`mech` axis applies to the *primary subject* of a source, not to every sub-section.

Claude Code skill definition files (`.claude/skills/{skill-name}/SKILL.md`) and subagent definition files (`.claude/agents/{agent-name}.md`) follow Anthropic-prescribed Claude Code path conventions. They are hub-authored deliverables (Hub Claude drafts the content); **the operator transfers the drafted files into the Development Track repository at the Anthropic-prescribed paths** via [MECH] Cross-Tool Workflow Handoff §3.1 (Hub → operator → CC direction). They are not canonical sources, and therefore do not take an `hdc_*.md` prefix. Their authoring rules and update discipline are governed canonically by CC substantive Claude Code Architecture Rules canonical (subagent roster §5) (subagent roster) and §Z (skill catalog). See §9.4 for the broader pattern of hub-authored deliverable files.

### Primary-axis judgment test (for new source classification)

When a new source's primary subject matter is ambiguous between `rule` and `mech`, apply all three tests below. The agreement of two out of three determines the prefix.

**Test 1 — Counting test**

Within the source's intended scope, count chapters whose primary content describes "what something is, what counts as a valid X, how X must be structured or formatted" (rule-shaped) versus chapters describing "how a multi-step governed process unfolds, what gates apply at each step, what happens when a step fails" (mech-shaped). The majority axis determines the prefix.

**Test 2 — Replaceability test**

Ask: if a different operator implemented the same intent without reading this source, what would they arrive at differently? If the alternative implementations would diverge primarily in *formats, identifiers, structures, or constraints* — `rule`. If the alternative implementations would diverge primarily in *sequences, gates, transitions, or what triggers what* — `mech`.

**Test 3 — Reader-question test**

Imagine a reader looking up this source for the first time. If their lookup question is "how is X structured / what counts as a valid X / where does X live" — `rule`. If their lookup question is "when does X fire / what comes next after X / what gates apply at X" — `mech`.

**Application**

Apply all three tests; agreement of two out of three determines the prefix. When all three disagree, the source is likely combining two distinct concerns and should be split per §8.6 anti-duplication. The single-axis Document Type rule in §10.4 forbids slash-compounded multi-axis values.

**Retroactivity**

This test does not retroactively reclassify existing sources whose primary-axis judgment was made under earlier conventions; existing classifications stand. The test applies to:
- new canonical sources entering the system
- substantive scope extensions that materially shift a source's center of gravity
- ambiguity disputes between two operators about an existing classification

### Adding a new prefix family

The 7-family registry above (`os` / `prin` / `pol` / `tpl` / `ref` / `rule` / `mech`) is closed by default. Adding an eighth family is rare and requires evidence that the new family carries a distinct primary axis that none of the existing 7 families covers without straddling.

Activation conditions — all of the following must hold:

1. **Distinct primary axis**: the proposed family's center of gravity cannot be honestly classified under any existing prefix per the §9.2 primary-axis judgment test.

2. **Multi-source evidence**: at least two source candidates exist whose primary axes converge on the proposed family. A single source whose axis is borderline does not justify a new family.

3. **One-source-one-job preservation**: the new family does not subsume rules currently load-bearing in another family. Re-homing rules across family boundaries requires §8.8a retirement procedure on the originating sources.

4. **Document Type vocabulary**: a new family value is added to the §10.4 `Document Type` controlled vocabulary in the same revision; Role first-word convention (per §10.4) is declared for the new family.

5. **PI and Hub Claude harness update**: PI's canonical source enumeration is updated to include the new family in the same revision (operator-side via Claude.ai project settings UI).

**Procedure**:

1. Author an Options Paper per [TPL] Options Paper comparing (a) adding the new prefix family vs (b) re-homing the proposed content into an existing family vs (c) leaving the content non-canonical.
2. Run the §9.2 primary-axis judgment test against the proposed family vs each existing family; document the test result in the Options Paper.
3. If the recommendation is "add new family", in the same revision: update §9.2 registry, §10.4 Document Type vocabulary, PI canonical source enumeration, and the first new source(s) under the new family.
4. Family additions trigger §8.5.7 re-architecture threshold re-evaluation.

Family **removal** (retirement of an entire family) follows the same Options-Paper-led path plus §8.8a retirement procedure applied to every member source of the retiring family.

## 9.3 Short-kebab-name rules

- all lowercase
- hyphens only
- descriptive but concise
- stable across revisions (renaming is a superseding operation per §8.8)

## 9.3a Identifier-vs-prose naming convention for unit_type values

Where canonical sources reference `unit_type` values (`walking_skeleton`, `feature`, `app_integration`):

- **As an identifier** — when the value appears as a marker block field value, YAML value, code identifier, or configuration key: use snake_case verbatim. Examples: `unit_type: walking_skeleton`, `prerequisite_units: [walking-skeleton-{phase-N}]`, `unit_type == 'app_integration'`.
- **As a prose noun** — when the value appears in narrative prose referring to the concept rather than the literal field value: use kebab-case. Examples: "the walking-skeleton unit", "the walking-skeleton output canonical set", "walking-skeleton-first ordering rule", "the app-integration unit", "app-integration scope variations".
- **For `feature`** — prose form is plain "feature" (the word is unambiguous English without disambiguation need); no kebab transformation applies.

## 9.4 Non-canonical naming patterns

The naming convention in §9.1–§9.3 governs canonical sources only. The project also produces non-canonical operational artifacts (operator runbooks, manual setup notes, inter-feature operational scratch files) that should be visually and mechanically distinguishable from canonical sources.

### Registered non-canonical pattern

`MANUAL_<short-kebab-name>.md` — all-uppercase prefix, underscore separator, lowercase kebab body. The all-caps prefix marks the file as non-canonical at a glance and prevents accidental confusion with canonical `hdc_<prefix>_<name>.md` files in directory listings, grep searches, and automated tooling.

Use this pattern for:
- operator runbooks for one-time setup actions not yet abstracted into a canonical [RULE] source
- manual operational notes documenting a specific recurring task whose mechanism is not yet stable enough to be canonical
- inter-feature operational scratch files (e.g., release coordination notes, environment troubleshooting logs)

### Non-canonical scope rules

Files matching `MANUAL_*.md`:
- do not go through the source-ready generation protocol in §8.9
- are not included in the consistency-check rule in §8.5
- do not appear in the static-pairing list in §8.5.2
- do not require the canonical source header standard in §10
- can be edited freely without paired-update obligations
- should be promoted to a canonical [RULE] / [TPL] / [OS] source when their content stabilizes per §8.1 durable-first rule and §8.3 abstract-before-storing rule; promotion follows §8.5.1 semantic scan + §8.6 anti-duplication

### Future non-canonical patterns

If additional non-canonical patterns become useful (e.g., `DRAFT_*.md` for in-flight working notes, `SCRATCH_*.md` for short-lived analysis), register them here following the same all-caps-prefix + underscore format. A non-canonical pattern must be registered in this section before being used at scale; ad hoc filename conventions are an anti-drift signal per §12.

### Claude Code skill and subagent definition files

Claude Code skill definitions (`.claude/skills/{skill-name}/SKILL.md`) and subagent definitions (`.claude/agents/{agent-name}.md`) are hub-authored deliverables (Hub Claude drafts the content; **the operator transfers the drafted files into the Development Track monorepo** via [MECH] Cross-Tool Workflow Handoff §3.1) under Anthropic-prescribed Claude Code path conventions. They are not canonical sources at the hub.

Properties:
- **Authoring**: Hub-authored — Hub Claude drafts content based on canonical CC substantive Claude Code Architecture Rules canonical (subagent roster §5) / §Z; operator reviews and transfers into Development Track via operator-mediated handoff per [MECH] Cross-Tool Workflow Handoff §3.1.
- **Storage**: in the Development Track monorepo at the Anthropic-prescribed paths above. There is no parallel hub-canonical mirror copy.
- **Naming**: follows Claude Code's required directory and file conventions (`{skill-name}/SKILL.md`, `{agent-name}.md`), not the canonical `hdc_<prefix>_<name>.md` convention. Skill names follow the project naming convention `hdc-<short-kebab-name>` (e.g., `hdc-arco-enterprise-ui`, `hdc-wcag-accessibility-checker`).
- **Canonical governance**: authoring rules, roster definition, scope policy, load triggers, and update discipline are governed by CC substantive Claude Code Architecture Rules canonical (subagent roster §5) (subagent roster) and §Z (skill catalog). When the canonical [RULE] sections change materially, **Hub Claude drafts the updates to the deliverable files; the operator transfers the updated files** into the Development Track repository under that source's update discipline. This is a paired-update obligation per §8.5.2 (canonical-to-runtime-artifact pairings), not a paired-revision of two canonical sources.
- **Versioning**: tracked through Development Track git history, not through hub canonical source revisions.

When a future kind of hub-authored deliverable file emerges that does not fit canonical naming and is not an operator-personal artifact, register its convention in this sub-section following the same pattern: declare the storage path, **the operator-mediated transfer mechanism per [MECH] Cross-Tool Workflow Handoff**, the canonical [RULE] that governs it, and the paired-update relationship.

---

# 10. Canonical source header standard

## 10.1 Required fields

Every canonical source declares a header block with these fields at minimum:
- Project
- Document Type
- Status
- Role
- Source Category
- Management-System Role

## 10.2 Source Category and Management-System Role declarations

Every canonical source must declare two fields in addition to the standard header:

**Source Category** — declares the canonical source's task-category scope:
- `Cat 1` — management-system work scope
- `Cat 2` — business solution design scope
- `Cat 3` — configuration workbook production scope (currently empty per §2.3.5)
- `Cat 4` — Development Track scope
- `Cross-category` — admissible across multiple categories with explicit per-category constraints declared
- `Meta` — operates above category scope (e.g., this operating model itself)

**Management-System Role** — declares where the source sits relative to the §4 L1-L5 management-system lens:
- An L2-L5 level when the source is itself a management-system output landing at that level
- "Outside L1-L5 hierarchy; governance mechanism / principle / reference / template above the hierarchy" when the source operates as a control or reference layer above L2-L5
- "Meta-level; defines the L1-L5 lens itself" — applicable only to this operating model

The Source Category determines admissible upstream sources per §2.3.2 dependency rules; the Management-System Role determines whether §5.4 level-or-linkage declaration rule fires.

## 10.3 Optional fields

- Phase / phase ontology field
- Status timestamp
- Last-revision summary
- Pairings I participate in (when applicable)
- Format (when format takes a deliberate stance)
- How to use this source (when the source's intended usage pattern is non-obvious)
- Boundary declarations (per §10.3a patterns)
- Relationship to ... fields (per §10.4 Relationship declarations and §8.5.1a Tier B convention)

## 10.3a Boundary declaration patterns

When a canonical source has overlapping scope, adjacent ownership, or potential drift with another canonical source, declare the boundary explicitly using one of the patterns below.

**`Boundary with [adjacent canonical source]`** — for sources that operate in adjacent scope where readers might confuse which source owns what:

Example: `Boundary with [MECH] Application Lifecycle Handoff` declared in [MECH] Cross-Tool Workflow Handoff, naming the lifecycle layer the source operates at (recurrent cross-tool flows) vs the adjacent source's layer (terminal application transfer).

**`Visibility boundary`** — for sources whose content reaches multiple audiences with disjoint context (Hub Claude vs Claude Code vs operator vs CD), declaring which audience can resolve which references.

**`Anti-drift boundary`** — for sources with anti-drift content that could be confused with another canonical source's anti-drift catalog, declaring the partitioning rule.

When in doubt about which pattern fits, default to the named-counterparty form (`Boundary with [X]`).

## 10.4 Controlled vocabulary

### Document Type

Use one of:

| Family | Document Type value | Notes |
|---|---|---|
| `[OS]` | `Operating Model` | Singular meta source |
| `[POL]` | `Policy Architecture Map` | Cat 1 |
| `[PRIN]` | `Principles` | Multiple PRIN sources share this value |
| `[REF]` | `Reference Catalog` | Cat 2/3 reference digests |
| `[RULE]` (format-focused) | `Format Control Specification` | e.g., DingTalk Markdown format |
| `[RULE]` (tool-focused) | `Tool Usage Specification` | e.g., Claude Platform Behavior |
| `[RULE]` (architecture-focused) | `Architecture Specification` | e.g., Claude Code Architecture Rules, Design System Governance |
| `[RULE]` (infrastructure-focused) | `Infrastructure Specification` | e.g., Workspace Topology |
| `[MECH]` (workflow-focused) | `Workflow Orchestration Specification` | e.g., Development Track Workflow, Application Lifecycle Handoff |
| `[MECH]` (governance-focused) | `Governance Mechanism Specification` | e.g., CI/CD Milestone Policy, Development Track Workflow, Application Lifecycle Handoff |
| `[TPL]` | `Template` | All template sources |

When a `[RULE]` source has multi-axis subject matter, use a single value reflecting the **primary axis** (the load-bearing dimension that determines the source's prefix family per §9.2 primary-axis judgment), not a slash-separated compound. Multi-axis compound forms (`X / Y Specification`) are deprecated.

Multiple sources sharing the same Document Type value is acceptable when their primary axes are genuinely the same. Disambiguation between same-typed sources is owned by the Role field (§10.4 Role first word) and the source name itself.

When the controlled vocabulary above is materially extended or revised, every canonical source's Document Type, Status, and Role first-word fields must be re-verified for continued conformance in the same revision. Non-conformance is an anti-drift signal per §12.

### Status

Use one of:
- `Active canonical` for non-template sources
- `Active canonical template` for template sources

No other Status values are permitted for canonical sources.

### Role first word

The Role field's first word should describe the source character. It must not duplicate the Status field. Use family-specific conventions:

| Family | Role first word | Example |
|---|---|---|
| [OS] | `Stable` | `Stable operating baseline for project routing, source governance, ...` |
| [POL] | `Stable` | `Stable policy architecture source for the Digital Solution team` |
| [PRIN] | `Durable` | `Durable decision and design principles for HR digital work in this hub` |
| [REF] | `Canonical` | `Canonical reference catalog of People Journey stages ...` |
| [RULE] | `Stable` | `Stable architecture-rules source for Claude Code projects ...` |
| [MECH] | `Stable` | `Stable milestone-policy source for Claude Code development work ...` |
| [TPL] | `Reusable` | `Reusable template for structured comparison of HR digital solution options ...` |

Do not use `Active canonical` as the Role first word. It duplicates the Status field and reduces information density.

### Relationship declarations

When a source depends on, extends, or is bounded by another canonical source, declare the relationship explicitly. Use:
- `Relationship to [OS]`: when the source derives authority from or supports specific [OS] loops or sections
- `Relationship to [PRIN]`: when the source applies specific [PRIN] judgment principles
- `Relationship to [REF]`: when the source consumes or produces reference-catalog content
- `Relationship to adjacent [TPL] sources`: when the source is part of a template family with tight cross-references
- `Relationship to [RULE] <specific rule>`: when the source co-governs execution with specific rule sources
- `Relationship to [MECH] <specific mechanism>`: when the source co-governs execution with specific mechanism sources
- `Relationship to custom skills`: when the source is referenced by or references a project skill
- `Relationship to specification outputs`: when the source consumes or produces specification artifacts

Per §8.5.1a Tier B convention, these `Relationship to ...` fields are also the canonical home for couplings that semantic search adequately covers (Tier B). When a source authoring or revision identifies a coupling that fails the §8.5.1a Tier A test, the coupling is documented in the relevant `Relationship to ...` field above with explicit § references to the counterparty source, NOT in §8.5.2. This makes `Relationship to ...` fields the primary cross-source dependency record at the source-header level, complementing §8.5.2 which holds only the Tier A (semantic-scan-unreliable) couplings.

### Chapter identifier convention

Canonical sources by default number top-level chapters with sequential integers (`# 1.`, `# 2.`, …). Some sources additionally use single-letter identifiers (`# X.`, `# Y.`, `# Z.`) for chapters whose **stable identity matters across re-numbering**. The current canonical example is [RULE] Claude Code Architecture Rules, which uses `§X` (Agent context scopes), `§Y` (Repository layout), `§Z` (Skill loading rules) between numbered chapters §5 and §6.

Use single-letter identifiers when **all** of the following hold:
- the chapter is heavily cited by other canonical sources (high cross-reference fan-out, e.g., §Y.1 / §Y.4 cited from 10+ files)
- the chapter's content is operationally load-bearing (its contents drive runtime artifacts under §8.5.2 canonical-to-runtime-artifact pairings)
- the chapter is likely to gain or lose adjacent numbered chapters over time

When using single-letter identifiers:
- declare the rationale once in the source's "How to use this source" or §0 chapter
- maintain alphabetical sequence (`X` → `Y` → `Z`); do not skip letters
- subsections under a single-letter chapter use the same family (`§X.1`, `§Y.4.2`)
- positional placement between numbered chapters (e.g., between §5 and §6) is acceptable; the integer sequence resumes after the letter chapters

Default to integer chapters unless the three conditions above all apply. Single-letter identifiers are an exception, not a style preference.

## 10.5 Field order

Header fields appear in this order:

1. `Project`
2. `Document Type`
3. `Status`
4. `Format` (when applicable)
5. `Role`
6. `Source Category`
7. `Management-System Role`
8. `Phase` / phase ontology fields (when applicable)
9. `Pairings I participate in` (when applicable)
10. `Relationship to ...` fields (one per relationship; can be multiple lines)
11. `Boundary with ...` / `Visibility boundary` / `Anti-drift boundary` (when applicable, per §10.3a)
12. `How to use this source` (when applicable, as a separate sub-section below the field list)

Optional fields not used by a given source are omitted, not declared empty.

---

# 11. Format stance

## 11.1 Default

Common Markdown with minimal formatting; no DingTalk-targeted formatting unless the source is destined for DingTalk Docs and the user requests format conversion.

## 11.2 When to declare a different format

Declare a different format in the Format field when the source takes a deliberate stance, e.g., "Strongly structured common Markdown" for sources that rely on tight section numbering.

## 11.3 Long-draft delivery

When a canonical source or specification output exceeds roughly 1500 words, deliver as a file, not inline chat content.

## 11.4 Language defaults

User Preferences (UP) is the authoritative source for response language defaults, internal-reasoning language, and control-file language conventions. This section adds only the project-specific extension:

- **Canonical sources authored for AI + human consumption**: English by default (higher cross-agent consumability across Hub Claude reading, Claude Code reading, and human review)

---

# 12. Anti-drift corrections

Claude should surface anti-drift corrections when any of the following happen:

- a source is being duplicated instead of updated
- a working artifact is being treated as canonical without explicit promotion
- an L4 process map is being written before its L2 or L3 policy anchor is stable
- a canonical source is being generated without the header block and relationship declarations required by §10
- a same-revision pairing in §8.5.2 is being triggered without the paired source being updated in the same revision, or a same-period pairing is being triggered without the paired source being re-verified within the same working period
- language default is being violated (e.g., canonical source authored in Chinese without cause)
- landing rule §5.4 is being skipped
- classification default §5.5 is being violated (e.g., specification artifact being treated as source candidate without explicit promotion)
- a Cat 2/3/4 canonical source cites `[POL]` or an L2-L5 management-system artifact, violating the hard boundary in §2.3.3
- a canonical name change or § re-numbering is made without grep-verifying all citations across canonical sources and updating dependent references in the same revision
- a Source Category declaration is missing from a new canonical source header, or a declared Source Category is inconsistent with the source's actual dependency pattern
- a `Document Type`, `Status`, or `Role first word` field uses a value not in the §10.4 controlled vocabulary, or uses a slash-compounded multi-axis form deprecated as of the §10.4 revision
- a Cat 4 source's §0 / §1 boundary chapter materially changes its owned scope without the §8.5.6 Cat 4 source map being re-verified in the same revision
- a new coupling is registered as `P-NN` in §8.5.2 without applying §8.5.1a Tier discrimination first; or a Tier B coupling is registered as `P-NN` despite being fully discoverable via semantic search and explicit cross-reference in the source's `Relationship to ...` header field
- a §8.5.7 harness re-architecture threshold is crossed (active pairings > 50, anti-drift dimensions > 20, canonical sources > 30, single source > 1500 lines, single source's `Pairings I participate in` > 10 for non-hub sources or > 12 for hub-pattern sources) without an Options Paper evaluation initiated — adding more pairings, sources, or anti-drift dimensions before the evaluation completes is itself a drift signal
- a CC-targeted file (CLAUDE.md, `.claude/agents/*.md`, `.claude/skills/{name}/SKILL.md`, or a hub-produced spec file destined for CC consumption — project-level singletons under monorepo-root `specs/` or app-scoped artifacts under `apps/{app-slug}/specs/**`) carries a bare cross-reference to a hub canonical source — any hub-side filesystem path (e.g., `/mnt/project/...`), or a `[RULE] X §N` / `[MECH] Y §N` reference without the substantive inlined content the reference depends on — violating the visibility boundary declared in §1.4
- a canonical source carries content that does not drive AI behavior at retrieval time — derived statistics, derived counts, restated boilerplate of rules owned elsewhere, "Why X exists" motivation sub-sections, historical status snapshots that are superseded, decorative meta-text, operator-navigation tables, summary closures — violating §0.1.4 AI-consumer-RAG-optimization premise

## 12.1 Lite / Deep response mode

For the authoritative Lite / Deep mode definition, selection logic, and Deep mode's sectioned response structure, see UP.

## 12.2 Source-intent topics

When a topic clearly intends to produce or update canonical source material, Deep mode applies by default and the §8.9 source-ready generation protocol activates before any final Markdown is produced.