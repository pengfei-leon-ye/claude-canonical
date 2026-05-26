# [REF] Hub-CD-CC Architecture

- **Project**: HR Digital Cockpit
- **Document Type**: Reference Catalog
- **Status**: Active canonical
- **Role**: Canonical cross-tool architecture reference defining the three AI workspaces (Hub / Claude Design / Claude Code), their boundaries, data flow, and asset-system relationships
- **Source Category**: Cross-category
- **Management-System Role**: Reference catalog source with cross-category scope (admissible across all four task categories per [OS] §2.3.2); outside L1-L5 hierarchy; not itself an L2, L3, L4, or L5 artifact; carries substantive cross-tool architecture content, not canonical-source governance content
- **Relationship to [OS]**: [OS] owns canonical-source governance (Meta layer per [OS] §2.3.2: admissibility, naming, audit, anti-drift, classification). This source owns the substantive structural architecture of the three AI workspaces and the contracts that govern their interaction (Cross-category layer per [OS] §2.3.2). Both admissible across all four Cat categories.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Cross-topic judgment principles apply within any workspace; this source does not govern judgment, only structural architecture and inter-workspace contracts.
- **Relationship to [REF] People Journey and Moments Catalog**: Different scope. People Journey is a domain reference (HR lifecycle stages); this source is an architectural reference (AI tool architecture).
- **Relationship to adjacent sources within the same family or tightly coupled**:
  - [RULE] Workspace Topology — different scope (multi-node dev environment topology inside CC; this source is hub/CD/CC three-workspace architecture at the AI tool level)
  - [MECH] Development Track Workflow — consumes this source's CC workspace boundary and the revised TK-02 internal structure (Step 2.1 Hub TDD / Step 2.2 CD design files / Step 2.3 Hub UX Design Spec authoring)
  - [MECH] Cross-Tool Workflow Handoff — operationalizes this source's three operator-mediated handoff paths into content contracts
  - [MECH] Application Lifecycle Handoff — distinct flow (AI-dev to human dev team, application-level); not the cross-tool workflow handoff this source describes
  - [RULE] Design System Governance — consumes this source's two-way DS distribution model (CD SOT / CC code-time mirror)
- **Relationship to [RULE] DingTalk MD Format Control**: Cross-category-layer peer per [OS] §2.3.2. Delivery-interface for DingTalk-destined outputs; orthogonal to this source's structural architecture.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [REF] Hub-CD-CC Architecture` header fields per [OS] §8.5.1a)

## How to use this source

Use this document as the primary reference for:
- understanding what each AI workspace (Hub / Claude Design / Claude Code) owns and does not own
- locating the boundary between workspaces for any given content or activity
- understanding the operator-mediated data flow between workspaces
- determining which workspace authors a specific canonical, spec artifact, code, or visual output
- understanding the two-way distribution of Design System content (CD SOT / CC code-time mirror) plus the governance pillar (Hub [RULE] DSG)
- selecting the asset reuse mechanism (Hub [TPL] vs CD Templates vs CD Skills) appropriate to a given task
- understanding the canonical inventory of each workspace
- determining handoff content and audit responsibilities for cross-workspace flows

Do not use this document as:
- a substitute for [OS] (which owns routing, source governance, and project-internal operating discipline)
- a substitute for [RULE] Workspace Topology (which owns multi-node dev environment topology inside the Claude Code workspace)
- a substitute for individual canonical sources owning rules inside each workspace (this source describes architecture, not workspace-internal rules)
- a deployment or operations runbook for any workspace

## Scope note

This source applies to:
- All work executed within Hub Claude for the HDC project (canonical authoring, spec artifact production including per-feature UX Design Spec instances, strategic framing)
- All work executed within Claude Design for the HDC project (DS setup and use, phase-level design file generation, visual artifact generation for HDC content)
- All work executed within Claude Code for the HDC project (code, tests, deployment, CC-internal canonical authoring)
- All cross-workspace flows mediated by the operator

This source does not apply to:
- Operator activities outside the HDC project scope (per §6 hub canonical scope boundary)
- Internal product governance of Claude Design or Claude Code as platforms (those are Anthropic's product domain; this source describes operator-perceived behavior and HDC-relevant integration)

---

# 0. Boundary and position

## 0.1 What this source owns

This source owns:
- The three-workspace architecture definition (Hub / Claude Design / Claude Code as the three AI workspaces the operator accesses for HDC project work)
- The identity, canonical inputs, canonical outputs, and out-of-scope activities for each workspace
- The operator-mediated data flow model (the three-workspace flows are operator-mediated, not direct-coupled, during the current operating period)
- The content / presentation / implementation tripartition (Hub owns content + governance / CD owns presentation / CC owns implementation)
- The Design System two-way distribution model (CD = SOT; CC = code-time mirror at `specs/design-system.md`; Hub holds the governance rules via [RULE] DSG and no DS instance copy)
- The per-feature UX Design Spec instance authoring model (Hub-authored markdown at TK-02 step 2.3, drawing from CD-authored design files)
- Hub canonical scope boundary (hub canonical covers HDC project work; does not cover operator's general use of CD or CC outside HDC project scope)
- The asset system coexistence model (Hub [TPL] family / CD Templates / CD Skills — three parallel reuse mechanisms)
- The canonical inventory mapping each canonical source to its owning workspace
- The handoff topology (three operator-mediated handoff paths)
- The conditions under which direct CD ↔ CC coupling may be re-enabled

## 0.2 What this source does not own

This source does not own:
- Project routing rules, source governance, anti-drift logic, audience model (owned by [OS])
- Multi-node dev environment topology inside the CC workspace (owned by [RULE] Workspace Topology)
- Internal task orchestration of the Development Track (owned by [MECH] Development Track Workflow, including the TK-02 internal Step 2.1 / 2.2 / 2.3 sub-structure)
- Substantive rules of any individual canonical inside any workspace (owned by their respective canonical sources)
- Design System governance rules and the CC-mirror sync mechanics (owned by [RULE] Design System Governance §1.1 + §12)
- Specific cross-workspace handoff content contracts (owned by [MECH] Cross-Tool Workflow Handoff)
- Application-level handoff from AI-dev track to human dev team (owned by [MECH] Application Lifecycle Handoff)
- Decisions about which workspace receives a given new canonical (placement decisions are made per-source under [OS] §8.9 source-ready generation protocol; this source provides the architectural frame those decisions reference)

## 0.3 Position relative to adjacent canonical sources

| Adjacent source | This source's relationship |
|---|---|
| [OS] Project Operating Model | Companion meta-layer source. [OS] governs operating discipline; this source describes structural architecture. Both admissible across all four Cat categories per [OS] §2.3.2. |
| [PRIN] HR Digital Decision Design Principles | Judgment principles apply within any workspace; this source does not govern judgment. |
| [PRIN] People Experience Design Principles | Domain-specific judgment within Cat 2 / Cat 4 UI scope; orthogonal to structural architecture. |
| [POL] Digital Solution Policy Architecture Map | Policy architecture is exclusively within the Hub workspace's management-system work (Cat 1); this source defines the workspace boundary that locates such work. |
| [REF] People Journey and Moments Catalog | Domain reference for HR lifecycle stages; orthogonal to architectural concerns. |
| [RULE] DingTalk MD Format Control | Cross-category-layer peer per [OS] §2.3.2. Delivery-interface for DingTalk-destined outputs; orthogonal to structural architecture. |
| [RULE] Workspace Topology | Different scope. Multi-node dev environment inside CC; this source is hub/CD/CC at the AI tool level. |
| [RULE] Claude Code Architecture Rules | Operates inside the CC workspace boundary that this source defines. |
| [RULE] Design System Governance | Consumes this source's two-way DS distribution; owns the governance discipline and the CC-mirror sync mechanism. |
| [RULE] Codex Plugin Usage | **Migrated to CC substantive canonical (Phase 3)**. Code review tooling executes inside the CC workspace; the substantive detail is owned by the CC substantive Codex Plugin Usage canonical. |
| [MECH] Development Track Workflow | Consumes this source's CC workspace boundary and the three-path handoff topology; owns the TK-02 internal Step 2.1 / 2.2 / 2.3 sub-structure that operationalizes the Hub-CD interaction. |
| [MECH] Application Lifecycle Handoff | Distinct flow (AI-dev → human dev team); not the cross-tool workflow handoff this source describes. |
| [MECH] Cross-Tool Workflow Handoff | Operationalizes this source's three operator-mediated handoff paths into content contracts. |
| [MECH] CI/CD Milestone Policy | Operates inside the CC workspace boundary that this source defines. |
| [MECH] Code Quality Rule Set | **Migrated to CC substantive canonical (Phase 3)**. Quality enforcement executes inside the CC workspace; canonical governance now at CC. |
| [MECH] Dev-Loopback Mode | **Migrated to CC substantive canonical (Phase 3)**. Dev-environment runnability contract is CC-internal; canonical governance now at CC. |
| [MECH] Tools Health Cadence | **Migrated to CC substantive canonical (Phase 3)**. Periodic tools health inventory is CC-internal; canonical governance now at CC. |
| [MECH] Canonical File Self-Audit | Audits canonical sources held in the Hub workspace; this source defines the Hub workspace's canonical inventory boundary. |
| [MECH] Sign-Off Cleanup Policy | Applies to spec artifacts produced in the Hub workspace; this source defines the Hub workspace's spec authoring scope. |
| [TPL] family (all templates) | Hub-workspace-held content contracts; this source defines the Hub workspace's [TPL] inventory location and contrasts with CD Templates / CD Skills in §7. |

---

# 1. Three-workspace overview

## 1.1 The three workspaces

The HDC project operates across three AI workspaces, each accessed by the operator as a distinct Claude product surface:

| Workspace | Surface | Identity |
|---|---|---|
| **Hub** | claude.ai HDC project | Strategic advisor + content SOT + governance SOT + per-feature UX Design Spec authoring |
| **Claude Design (CD)** | claude.ai/design | DS-aware multi-purpose visual generator workspace; DS SOT; phase-level design file producer (one design file per phase covering all tier-1-involved features in that phase) |
| **Claude Code (CC)** | Assigned dev nodes (dev-node-portable / dev-node-stationary-1) | Dev environment + implementation SOT + CC-internal canonical author + DS code-time mirror holder |

The three are independent Claude product surfaces. They do not share session state directly. All cross-workspace flows go through the operator (§1.2).

## 1.2 Operator as the single mediating node

All cross-workspace data flow is operator-mediated. The directed-tree shape reflects the current operating model: the operator is the only node with simultaneous read/write access to all three workspaces, and the workspaces themselves do not interact directly during the current operating period (§9.4). Specifically:
- Output from one workspace becomes input to another only after the operator has read, audited, and transferred it
- No workspace can push content to another workspace autonomously
- No workspace has read access to another workspace's session state
- Each workspace receives only the content the operator chooses to share with it

This is a property of the current operating period and follows from Claude.ai product architecture (separate Claude products do not share session context). It is not a chosen design constraint imposed by HDC project rules; HDC rules accept it as the operating premise and design around it.

The conditions under which this premise may relax (specifically, direct CD ↔ CC coupling) are documented in §10.

---

# 2. Hub workspace

## 2.1 Identity

The Hub is the HDC project's strategic advisor and the source-of-truth (SOT) for content and governance.

Hub identity has two interlocking roles:
- **Strategic advisor**: framing ambiguous needs, comparing options, making architecture judgments, designing mechanisms, supporting global-core capability harvesting
- **Content + governance SOT**: holding all canonical sources that govern the HDC project, all specification artifact main bodies (including per-feature UX Design Spec instances), and all interface contracts between the three workspaces. This includes DS governance ([RULE] DSG) but not DS instance content — Hub holds no DS instance copy; at TK-02 step 2.3 Hub consumes CD-authored design files, and it reviews the CD-generated DS markdown export against DSG §15 before that export reaches the CC mirror

The Hub does not produce visual artifacts, code, or platform-specific implementation artifacts. Those are CD's and CC's domains respectively (§5).

## 2.2 Canonical inputs

The Hub workspace accepts these canonical input forms:

| Input | Source | Notes |
|---|---|---|
| User Preferences (UP) | Operator account settings | Account-level harness; highest precedence on behavioral rules |
| Project Instructions (PI) | Hub project settings | Project-level harness |
| Project Knowledge (PK) | Hub PK `hdc_*.md` files (synced from GitHub `claude-canonical/hdc/project_knowledge/` folder) | The canonical source set held in the Hub |
| Operator dialogue input | Conversation turn content | Framing, decisions, external materials provided in conversation |
| Operator-mediated CD output | Conversation attachments, pasted content, or dropped files | Materials audited and forwarded by the operator from a CD session: phase-level design file (visual + annotation, with per-feature internal labeling), DS markdown exports for the DSG §15 export conformance review, stakeholder review materials |
| Operator-mediated CC output | Conversation attachments or pasted content | Materials audited and forwarded by the operator from a CC session: Codex review output, CC-internal canonical change notifications, DS code change notifications |

The Hub does not directly access CD or CC. Anything CD or CC produced reaches the Hub only via operator action.

## 2.3 Canonical outputs

The Hub workspace authors:

**Strategic outputs (in-conversation):**
- Framing memos, option comparisons, architectural judgments
- Advisory output ("recommendation lists" the operator decides whether to execute)
- Decision rationales

**Specification artifact main bodies:**
- PRD main body (including IA chapter)
- TDD main body (including Permission Model chapter)
- **Per-feature UX Design Spec instance markdown** (when TDD §4.{feature-slug}.Header.tier_1_involved = true; authored at TK-02 step 2.3 from CD-authored design files; lands at `apps/{slug}/specs/ux-design-spec/{feature-slug}.md`)
- intent main body
- acceptance main body
- Architecture Decision Records (ADRs)
- OpenAPI specifications
- Phase test plan master

**Cross-workspace interface contracts (canonical sources):**
- [MECH] / [TPL] / [REF] family sources that govern interaction with CD and CC
- This source ([REF] Hub-CD-CC Architecture)

**Design System governance (two-way distribution):**
- DS governance rules (owned by [RULE] Design System Governance)
- DS markdown export conformance review — at a DS change finalization, Hub Claude reviews the CD-generated DS markdown export against DSG §15 before it is committed to the CC mirror (per DSG §12.3); Hub does not hold a DS instance copy
- DS change notification anchor (mediating updates between CC code changes, CD instance authoring, and the CC-mirror sync)

**Codex review judgment + archive:**
- After the operator forwards Codex review output from a CC session, the Hub judges and archives the findings into the canonical record

## 2.4 Out-of-scope activities

The Hub does not:
- Produce UI/UX visual designs (CD's domain — CD authors design files which Hub then consumes)
- Author DS instance content (CD's domain as SOT — Hub holds no DS instance copy)
- Maintain CC-side DS code mirror (CC's domain at `specs/design-system.md`)
- Write or modify application code (CC's domain)
- Execute mechanical tool-bound tasks (those execute in CD or CC depending on tool binding)
- Send commands directly to CD or CC (all coupling is operator-mediated, §1.2)
- Govern internal CD or CC product behavior (those are Anthropic's product domain)

## 2.5 Operator action checklist (Hub session)

In a Hub session, the operator:
1. Provides framing, decisions, and external materials as conversation input
2. Receives advisory output and judges whether to execute the recommendations
3. Reviews Hub-produced specification artifact main bodies (PRD, TDD, per-feature UX Design Spec instances, per-slice intent / acceptance / test-plan) and signs off when ready
4. Transfers Hub outputs to CD or CC by attaching, copying, or otherwise carrying content into those product surfaces
5. Transfers CD-authored design files and DS markdown exports into the Hub session for consumption (at TK-02 step 2.3 for design files; at workspace inception / DSG §12 merge for the DS markdown export §15 conformance review)

---

# 3. Claude Design workspace

## 3.1 Identity

Claude Design is a **DS-aware multi-purpose visual generator workspace**. It is the SOT for DS instance content and the producer of the **phase-level design file** for HDC tier-1-involved work — CD designs by application phase (one design file per phase covering all tier-1-involved features in that phase), aligning with CD's natural unit of visual production rather than forcing per-feature splits at design time. It is not a single-purpose UX or DS pillar. CD organizes work into projects (independent visual generation workspaces), each of which can use DS instances as optional context enrichment and can produce many visual artifact forms through skill-based generation.

CD is in research preview status as of this revision (Claude product status, not HDC project status). The HDC project treats CD as a usable workspace with several specific items pending empirical verification (§3.7).

## 3.2 CD internal structure (operator-perceived)

```
Claude Design Workspace:
├── Top level: Design Files / Examples / Design systems (three tabs per current CD surface)
├── DS instances (multiple possible; synthesized from materials; operator-setup; SOT for DS content)
├── Skills (system-provided; combinable with any instance)
├── Templates (operator-authored; reusable across projects)
└── Projects (independent workspaces, design files as main panel)
      ├── Creation modes (orthogonal; DS not required):
      │     ├── Prototype (wireframe / high fidelity)
      │     ├── Slide deck (speaker notes option)
      │     ├── From template
      │     └── Other (open-ended)
      └── Context injection (combinable):
            ├── DS reference (optional)
            ├── Skills selection
            ├── Screenshots
            ├── Codebase attachment
            ├── Figma file
            ├── Free-form prompt
            └── Drop files (images / docs / references / Figma links / folders)
```

DS is one optional context input among many. The operator can create a CD project without setting up a DS first. For HDC tier-1-involved feature work, DS is mandatory context.

## 3.3 Canonical inputs

CD accepts inputs at two distinct lifecycle points:

### 3.3.1 Setup-time inputs (one-time DS instance initialization)

When the operator initializes a DS instance in CD:
- Code source (GitHub repository URL, or a local folder selected via the CD UI)
- Figma `.fig` files (parsed locally in the browser; per CD setup screen note, not uploaded)
- Fonts, logos, and visual assets
- Free-form notes (CD setup form's "Any other notes?" field; may carry brand preferences, design direction descriptions, governance hints)

### 3.3.2 Use-time inputs (per project, per generation)

When the operator creates and operates a CD project for HDC phase-level design work:
- DS instance reference (the HDC DS instance, set up at workspace inception)
- Skills selection (typically Hi-fi design + Interactive prototype for phase-level design work; Wireframe + Make a deck for stakeholder communication)
- **Drop files containing full PRD + TDD relevant sections for all tier-1-involved features in the phase** (per the v1 input strategy in [MECH] Cross-Tool Workflow Handoff §2.1.6 — full text of PRD feature chapters + TDD §4.{feature-slug} content for each tier-1-involved feature, not Hub-pre-extracted)
- **Free-form prompt with operator-authored attention guidance enumerating each tier-1-involved feature** (Hub Claude assists in drafting; directs CD's attention to UI-relevant sections per feature within the dropped PRD/TDD content, and instructs CD to internally label per-feature design file scope by feature-slug for Hub Step 2.3 grounding)
- Optional: existing reference designs (screenshots from competitor analysis, internal precedents), brand direction hints, People Experience principle excerpts

**Critical note on CD's input mechanism**: CD does not consume hub-style structured specification documents as structured specs. CD has no PRD/TDD-parsing mechanism. The full-text drop file + attention prompt strategy gives CD complete information access while using prompt guidance to direct attention to UI-relevant content. The operator's responsibility is to frame the attention prompt so CD focuses appropriately.

## 3.4 Canonical outputs

CD output forms are determined by the skill selected. Currently observable skill families:

| Skill family | Output form |
|---|---|
| Prototype | Wireframe sketches / high-fidelity prototypes / interactive prototypes |
| Slide deck | HTML deck / PPTX (editable) / PPTX (screenshots) / speaker notes (optional) |
| Make a deck | Slide presentation in HTML |
| Animated video | Timeline-based motion design |
| Make tweakable | In-design tweak controls added to output |
| Frontend design | Aesthetic direction for designs outside an existing brand system |
| Wireframe | Ideation wireframes and storyboards |
| Export skills | PDF / standalone HTML / Canva-compatible format |

Within a CD project, the operator may compose multiple skills to produce richer artifacts (e.g., a prototype refined with tweakable controls, then exported as PDF).

### 3.4.1 Outputs relevant to HDC project work

For HDC project work specifically, the operator typically uses CD to produce:

- **Phase-level design file** (when any feature in the phase has TDD `tier_1_involved=true`): one design file per phase covering all tier-1-involved features in that phase — hi-fi mockups, interactive prototypes, wireframes, component callouts, interaction flows, with embedded textual annotations covering design rationale, a11y considerations, i18n notes, responsive behavior, motion expectations. The design file carries content at **two scopes within the single phase-level file**: (i) **cross-cutting sections** depicting content shared across features — platform shell, shared visual vocabulary (badges / status language / masking patterns), cross-feature touchpoint maps, phase-level horizontal design decisions, visual regression naming convention; (ii) **per-feature labeled scopes** for each tier-1-involved feature (frame / section / page tag matching the TDD `feature-slug`) so Hub TK-02 step 2.3 can ground each per-feature UX Design Spec instance in the relevant subset. This design file is **raw source material** from which Hub Claude authors UX Design Spec instances at TK-02 step 2.3 — at **two granularities** (one phase-level instance synthesizing the cross-cutting sections; per-feature instances synthesizing each labeled slice) — not a CC-consumable spec equivalent. The design file contains material on each [TPL] UX Design Spec §2A category at the cross-cutting scope plus each §2B category for every tier-1-involved feature (CD chooses the native form; coverage means the material is present), but **CC does not consume design files directly as specification**: Hub-side synthesis is required to (a) translate visual + informal annotation form into structured markdown that CC can deterministically consume, (b) verify the design file (both its cross-cutting sections and its per-feature slices) is spec-ready against the PRD/TDD scope — the design file quality checks per [RULE] DSG §13.3, which need the PRD/TDD that CD does not hold as structured specs, and (c) produce spec instances integrated with adjacent specification artifacts (PRD, TDD, per-slice intent/acceptance/test-plan) that share the Hub-side authoring context. The CD → Hub → CC chain therefore has a substantive synthesis step at the Hub middle; CD output and CC input are **not at the same content layer**. The file-count asymmetry — one phase-level design file on the CD side, one phase-level instance + N per-feature instances on the Hub side — reflects each workspace's natural unit (CD designs by phase as its unit of visual production; Hub authors structured markdown at the granularity each downstream consumer needs — phase-level for cross-cutting context, per-feature for feature-scoped detail).
- **DS instance content** (additive or breaking changes to DS authored in CD as SOT per [RULE] DSG §12): when CD-side authoring produces new components, tokens, patterns, or other DS evolution, the change is finalized in CD SOT; CD also generates an updated DS markdown export for the DSG §15 conformance review and CC-mirror sync.
- **Stakeholder review materials** (prototypes, slide decks) for operator's own use; not integrated into Hub canonical.

Operator can also use CD skills for purposes outside HDC project scope (per §6.2). When CD is used for non-HDC purposes, hub canonical does not regulate the work, and CD outputs are not subject to hub audit.

### 3.4.2 DS instance content (CD as SOT)

CD holds the SOT for DS instance content. The DS instance lives inside CD with all DS evolution happening there per [RULE] DSG §12. CD also generates:
- DS markdown export — a textual representation of the current DS instance content (components, tokens with values, patterns, a11y baseline, i18n scope). Generated by the operator prompting CD to produce a structured markdown summary of the DS, typically at workspace inception and at every DSG §12 additive/breaking merge.
- The DS markdown export is operator-transferred — after the DSG §15 export conformance review in a Hub conversation — to the CC mirror (as `specs/design-system.md`). The CC mirror is the read-only consumer of this export.

CD-internal concept synthesis artifacts (intermediate sketches, exploratory work, etc.) are NOT mirrored — only the formal DS instance content via the markdown export.

## 3.5 Out-of-scope activities

CD does not:
- Author specification artifact main bodies (Hub's domain — including UX Design Spec instances, which are Hub-authored from CD design files)
- Write production application code (CC's domain)
- Maintain governance rules (Hub's domain via [RULE] DSG)
- Maintain strategic framing (Hub's domain)
- Operate as a canonical SOT for content other than DS instance and design files

## 3.6 Operator action checklist (CD session)

The operator in a CD session:
1. (One-time per DS) Sets up a DS instance — provides code, Figma, assets, notes
2. Creates a project, choosing instance type and skills
3. For HDC per-feature work (tier_1_involved=true): injects context per §3.3.2 (DS reference, skills, full PRD+TDD drop files, attention prompt)
4. Generates output and reviews the result
5. Audits CD output before transfer:
   - For Hub destination at TK-02 step 2.3: extracts design files (visual + annotation) and transfers to Hub session via attachment / paste / drop; Hub Claude then performs quality check and authors UX Design Spec instance
   - For DS mirror sync: prompts CD to generate DS markdown export; brings it into a Hub conversation for the DSG §15 export conformance review, then transfers it to the CC mirror per [RULE] DSG §12

## 3.7 Pending empirical verification (R1 scope)

The following CD operating parameters are not yet empirically verified for HDC project use. Sections of this source that depend on assumptions about these parameters are noted inline; the canonical content remains the current operating premise until verification completes.

| # | Parameter | Verification scope |
|---|---|---|
| 1 | Weekly usage quota | How much quota does a 1 feature × 1 screen generation cycle consume? |
| 2 | Context disjoint property | Does CD genuinely isolate from Hub/CC session state? Any unexpected coupling? |
| 3 | Design file transfer format | Concrete contents (file types, naming, structure) of design files when transferred to Hub, and consumability of those contents for Hub Claude's TK-02 step 2.3 quality check + UX Design Spec authoring |
| 4 | Output quality | Does generated prototype respect DS constraints? Are produced decks professional-grade? Does CD respect the attention prompt directing focus to UI-relevant PRD/TDD content? |
| 5 | DS markdown export quality | Does CD-generated DS markdown faithfully represent the DS instance content (components, tokens with values, patterns)? Is it reviewable by Hub Claude against DSG §15 and consumable by CC SK-F as a code-time spec? |

Verification approach: 1 feature × 1 screen trial within the HDC project (Phase C1 of the Step 2 canonical refactor). DS-related canonical content reaching sign-off is gated on this verification.

---

# 4. Claude Code workspace

## 4.1 Identity

Claude Code is the dev environment and implementation SOT plus the code-time consumption surface for DS content. CC is also the author of its own substantive canonical content (`.claude/rules/`, `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, `.claude/hooks/`), produced based on Hub constitutional input.

CC operates within the multi-node dev environment topology defined in [RULE] Workspace Topology (dev-node-portable / dev-node-stationary-1 logical nodes with parity discipline). Within each node, CC instances operate against the monorepo at `pengfei-leon-ye/claude-hdc` per [MECH] Development Track Workflow.

## 4.2 Canonical inputs

CC accepts these canonical inputs:

| Input | Source | Mechanism |
|---|---|---|
| Hub constitutional canonical set | Hub PK `hdc_*.md` files (synced from GitHub `claude-canonical/hdc/project_knowledge/`) | CC accesses Hub canonical as a **read-only authoritative source** via operator-chosen mechanism (e.g., local clone of the canonical GitHub repository, operator-mediated paste, or any other access method). This canonical declares only the contract — one-way Hub → CC flow, no back-flow, CC consumes Hub canonical without modifying its origin. Specific access mechanism is operator-personal infrastructure, not canonical-governed. |
| Hub spec artifact main bodies | Hub-authored PRD / TDD / per-feature UX Design Spec instances / intent / acceptance / test-plan main | Provided as files in the monorepo at `specs/` paths or operator-transferred per CC session |
| CD-authored design files (visual reference) | CD-exported design files | Operator-mediated transfer at TK-04 alongside Hub UX Design Spec instances; CC consumes design files as **visual reference** during code implementation (visual mockups, component arrangement, motion specifications). CC does NOT author UX-touching field values from design files — those were Hub-authored at TK-03 from the UX Design Spec instance |
| Hub-authored UX Design Spec instance | Hub markdown at `apps/{slug}/specs/ux-design-spec/{feature-slug}.md` | The **primary textual UX specification** consumed by CC at TK-04+ for tier-1 code implementation; this is what CC reads for component selections, interaction patterns, a11y requirements, i18n considerations, responsive behavior. Authored by Hub Claude at TK-02 step 2.3 from CD-authored design files |
| DS code-time mirror | `specs/design-system.md` in monorepo | Read-only mirror of CD DS SOT; synced from CD markdown export per [RULE] DSG §12; consumed by SK-F skill at code-generation time |

CC does not directly access Hub session state or CD session state. All inputs arrive as files in the working directory or operator-pasted content.

## 4.3 Canonical outputs

CC authors:

**Application code and supporting artifacts:**
- Application code (Tier 1 React frontend / Tier 2 Node BFF / Tier 3 Java domain per [RULE] Claude Code Architecture Rules)
- Test code (slice tests per [TPL] Test Plan YAML Schema; phase tests per [TPL] Phase Test Plan)
- Configuration files
- Deployment manifests

**Note on specification artifact UX-touching fields**:

intent UX brief reference fields, acceptance UX-related acceptance criteria, and test-plan a11y / motion / DS-coupling fields are **NOT** authored by CC. They are authored by **Hub Claude at TK-03** consuming the Hub-authored UX Design Spec instance (which itself was authored at TK-02 step 2.3 from CD design files). CC consumes the completed spec at TK-04 for code implementation; design files accompany the spec at TK-04 transfer as visual reference, not as a source for CC field authoring.

**CC-internal canonical files (Substantive at CC):**
- `.claude/rules/*.md` (path-scoped rule files, governed by the CC substantive Claude Code Architecture Rules canonical's context-scope content)
- `.claude/agents/*.md` (subagent definitions, governed by the CC substantive Claude Code Architecture Rules canonical's subagent roster content)
- `.claude/commands/*.md` (code review command shortcuts, governed by the CC substantive Codex Plugin Usage canonical)
- `.claude/skills/{name}/SKILL.md` (skill definitions, governed by the CC substantive Claude Code Architecture Rules canonical's skill loading content)
- `.claude/hooks/*.md` (hook trigger logic, governed by the CC substantive Claude Code Architecture Rules canonical's hook content)
- `CLAUDE.md` at each tier-aligned hierarchy level — this source frames the CLAUDE.md hierarchy's existence (§4.1, §5.4); the specific paths and authoring discipline are owned by the CC substantive Memory Bank Layout canonical

**CC-side artifacts governed by canonical:**
- `.github/workflows/*.yml` (CI pipeline YAML, governed by CC substantive CI/CD Milestone Policy canonical for specific tooling; [MECH] CI/CD constitutional residue at Hub governs the gate identity + Test Evidence Report schema)
- `monorepo-root/configs/eslint/*`, `configs/checkstyle/*` (governed by CC substantive Code Quality Rule Set canonical)
- `monorepo-root/fixtures/*`, `.dev-loopback/*` (governed by CC substantive Dev-Loopback Mode canonical)
- `monorepo-root/docs/workspace-onboarding.md` (governed by CC substantive Workspace Topology canonical for specific tool stack/setup; [RULE] WT constitutional residue at Hub governs multi-node existence + parity invariant)

**DS code-time mirror (Substantive):**
- `specs/design-system.md` — read-only mirror of CD DS SOT, populated from CD-generated DS markdown export per [RULE] DSG §12 sync mechanism; CC does NOT author this content, only mirrors

**Codex review output:**
- Codex code review findings produced at the Codex review TK (TK-11); review object is application code; operator-transferred to Hub for judgment and archive

## 4.4 Out-of-scope activities

CC does not:
- Author specification artifact main bodies (Hub's domain — including UX Design Spec instances)
- Make UI/UX design judgments (CD's domain for visual design; Hub's domain for slice-level textual UX brief authoring)
- Maintain DS governance (Hub's domain for governance pillar via [RULE] DSG)
- Maintain DS instance content (CD's domain as SOT)
- Maintain strategic framing (Hub's domain)
- Send commands directly to Hub or CD (all coupling is operator-mediated)

## 4.5 Operator action checklist (CC session)

The operator in a CC session:
1. Ensures CC has access to current Hub canonical via the operator's chosen mechanism (e.g., local clone of the canonical GitHub repository) — specific mechanism is operator-personal infrastructure, not canonical-governed
2. Reviews CC outputs (code / CC-internal canonical / implementation artifacts)
3. Transfers CC outputs back to the Hub as needed:
   - Code review tool output → Hub judgment and archive
   - CC canonical index information → Hub canonical inventory update
   - DS code change notifications → Hub DSG §12 routing (subsequent CD SOT update + CC-mirror re-sync)

---

# 5. Content / Presentation / Implementation tripartition

## 5.1 Tripartition definition

The three workspaces are distinguished by what kind of substantive content they own:

| Dimension | Location | Examples |
|---|---|---|
| **Content** | Hub | PRD business logic, TDD technical decisions, UX Design Spec instances (phase-level + per-feature; slice-orienting textual UX specifications), governance rules, strategic framing, specification artifact main bodies |
| **Presentation** | CD | UI visual designs, prototypes, slide decks, phase-level design file (per-feature internally labeled), DS instance content (SOT), any visual artifact |
| **Implementation** | CC | Code, tests, deployment artifacts, DS code, CI configurations, executable artifacts |

The tripartition is not strict (DS content is authored in CD but mirrored to CC for code-time consumption; some content has presentation aspects, etc.), but the SOT for each dimension is unambiguous.

## 5.2 Design System as the cross-cutting case (two-way distribution)

The Design System is the canonical example of a single concept distributed across workspaces. The distribution model recognizes that DS content has one SOT and one consumption mirror, with governance held separately:

| DS aspect | Workspace | Specific artifacts |
|---|---|---|
| **Authoritative SOT** | CD | DS instance in CD with uploaded Figma, fonts, logos; CD-synthesized DS concept model; all DS evolution (additive / breaking changes) happens here per [RULE] DSG §12; CD also generates DS markdown export for the §15 review and CC-mirror sync |
| **Code-time mirror** | CC | Read-only mirror at `specs/design-system.md`; consumed by SK-F skill at code-generation time; component code in monorepo derived from this mirror's content |
| **Governance rules (topic-level)** | Hub | [RULE] Design System Governance (governance rules only; not instance content). Hub holds DSG but no DS instance copy; DSG is transferred to CD as a read-only input for DS instance authoring |

**DS distribution rationale (two-way)**: A Design System has one SOT (CD, where design happens) and one consumption mirror (CC, for code generation). Hub holds no DS instance copy:
- CC needs DS content at code-generation time (component existence, token values, pattern usage) — without a CC mirror, code-gen cannot verify DS-coupling correctness. The CC mirror is operationally necessary.
- Hub does **not** need a DS instance copy. At TK-02 step 2.3 Hub consumes CD-authored design files (which carry the component / token / pattern callouts CD wrote against the DS); the design file quality check is a spec-readiness review against the PRD/TDD, not a DS-conformance check against a mirror. The Hub-side touchpoint with DS instance content is the transient export conformance review (per DSG §12.3 / §13.3), performed on the CD-generated export in a Hub conversation — not via a persisted mirror.

Holding governance rules separately from instance content (rules in [RULE] DSG at Hub, content in CD with one CC mirror) keeps the policy layer stable while the instance evolves. DS-instance conformance to DSG is checked at the workspaces that execute against the DS — CD at authoring time (CD holds DSG as a transferred input) and CC at code generation — plus the Hub-side review of the CD-generated export before it reaches the CC mirror.

**DS change propagation (two-way)**:

- **Most common path — CD authors a DS change** (per DSG §12 additive update path triggered by feature design needs):
  1. CD authors the change in CD SOT during a feature's design cycle, against the DSG transferred to CD as a read-only input
  2. Change is finalized in CD SOT at the originating feature's M4 → merge-to-main milestone per DSG §12.5
  3. CD generates an updated DS markdown export reflecting the new instance state
  4. Operator brings the export into a Hub conversation for the DSG §15 export conformance review; on a passing review, the operator commits the export to the CC mirror (`specs/design-system.md`)

- **CC code changes warranting DS reflection** (e.g., new component empirically validated in-slice):
  1. CC surfaces the candidate change in conversation with Hub
  2. Hub routes through DSG §12: operator carries to CD for SOT authoring
  3. Once finalized in CD SOT, the standard CD → export review → CC-mirror sync path applies

- **Hub governance changes** (e.g., new component approval rule in [RULE] DSG):
  1. Governance-only change — DS instance content does not change
  2. Operator carries the [RULE] DSG update to CD for instance discipline observance and to CC for implementation discipline observance
  3. The CC mirror does not re-sync (no instance content change)

## 5.3 Boundary rules

- Each workspace holds the SOT for its dimension; DS content is the explicit cross-cutting case with CD as SOT and one CC mirror consumer
- Cross-dimension collaboration flows through the operator
- Hub canonical does not describe CD's internal presentation rules or CC's internal code rules; those are workspace-internal concerns
- Hub canonical only describes "content contracts between workspaces" (what handoff carries) and "governance of cross-cutting concepts" (e.g., DS governance via [RULE] DSG)

## 5.4 Constitutional vs Substantive canonical content split

The §5.1 tripartition classifies content by ownership dimension (content / presentation / implementation). A second cross-cutting classification distinguishes canonical content by its **maturity / lifecycle layer**: Constitutional vs Substantive. The two classifications are orthogonal — every canonical artifact has both a dimensional location (per §5.1) and a layer status (per this §5.4).

### 5.4.1 Two-layer definition

| Layer | Characteristics | SOT location |
|---|---|---|
| **Constitutional** | Why-anchors and identity declarations; scope boundaries; contractual interfaces between workspaces; low change frequency; format-stable; canonical-quality discipline applies | **Hub** holds SOT |
| **Substantive** | How-rules, configurations, prompts, mechanical details; higher change frequency; runtime-coupled; format may vary across tools; tool's own quality discipline applies | **Tool runtime** holds SOT; Hub holds index only |

### 5.4.2 Layer membership by source family

- **Hub Constitutional** (Hub PK `hdc_*.md` files): `[OS]`, `[POL]`, `[PRIN]`, `[REF]`, `[RULE]`, `[MECH]`, `[TPL]` — all Constitutional. SOT for the why, scope, contracts, and governance the project depends on.
- **Hub spec artifacts** (Hub-authored at `apps/{slug}/specs/...`): PRD instances, TDD instances, UX Design Spec instances (phase-level + per-feature), per-slice intent / acceptance / test-plan, ADRs, OpenAPI specs. These are not Constitutional canonical (no Hub PK location); they are spec artifacts produced under Constitutional template governance.
- **CC Substantive** (Tool runtime at the monorepo): `.claude/rules/`, `.claude/agents/`, `.claude/commands/`, `.claude/skills/{name}/SKILL.md`, `.claude/hooks/`, `CLAUDE.md` at each tier-aligned hierarchy level (specific paths owned by the CC substantive Memory Bank Layout canonical). SOT for path-scoped rule application, subagent prompts, skill loading, hook firing logic. Plus DS code-time mirror at `specs/design-system.md` (Substantive consumption, mirror not SOT).
- **CD Substantive** (Tool runtime at CD): DS instance internal content authored under [RULE] DSG governance rules (CD as SOT for DS content); phase-level design file (CD-native format with embedded annotations, cross-cutting sections, and per-feature internal labeling, authored against [TPL] UX Design Spec coverage framework — §2A for cross-cutting content + §2B for per-feature content — as the upstream quality guide); CD project artifacts.

### 5.4.3 Self-authoring workflow for Substantive content

1. Tool drafts Substantive content informed by the relevant Hub Constitutional sources (e.g., CC drafts `.claude/rules/*.md` under the CC substantive Claude Code Architecture Rules canonical's agent context scope guidance; CD authors DS instance content under [RULE] DSG governance; CD produces the phase-level design file against [TPL] UX Design Spec coverage framework)
2. Operator reviews tool-drafted Substantive content for boundary compliance with the governing Constitutional canonical
3. Tool runtime persists the Substantive content at its native path (CC commits to monorepo paths; CD persists within the CD project)
4. Hub indexes the **existence** of the Substantive content via the relevant `[REF]` source (e.g., this [REF] Hub-CD-CC Architecture §8 inventory indexes CC-internal Substantive content existence) but does **not** mirror the Substantive content itself

### 5.4.4 Relationship to the SPLIT and MIGRATED-OUT canonical sources

Eight Hub canonical sources were structurally restructured during Phase 3 of the Hub-CC architecture refactor (per [OS] §0.1.5 Premise 5 constitutional / substantive boundary). Four were **split** (Hub-side constitutional residue + Hub-internal substantive retained; CC-side substantive externalized); four were **fully migrated** (no Hub residue retained).

**Split sources (4)** — Hub keeps the constitutional skeleton + Hub-internal substantive (e.g., Hub Claude behavior); the operational detail is owned by the corresponding CC-side substantive canonical:

| Hub-side residue retains | CC-side substantive boundary |
|---|---|
| `[RULE] Workspace Topology` — multi-node existence, parity discipline, walking-skeleton-first ordering rule, node-assignment interface contract, workspace inception governance, Hub Claude trigger phrases (Hub-internal substantive), Hub Claude observability boundary (Hub-internal substantive) | The CC-side operational substantive detail is owned by the CC substantive Workspace Topology canonical. |
| `[RULE] Claude Code Architecture Rules` — three-tier architecture identity, Tier 2 thinning rule, permission decision placement principle, CLAUDE.md hierarchy pointer, subagent topology existence, high-level monorepo structure | The CC-side operational substantive detail is owned by the CC substantive Claude Code Architecture Rules canonical. |
| `[MECH] CI/CD Milestone Policy` — M0–M4 ladder identity, per-unit-type milestone profile interface, Test Evidence Report schema, required artifact output gates, multi-node evidence parity invariant | The CC-side operational substantive detail is owned by the CC substantive CI/CD Milestone Policy canonical. |
| `[MECH] Development Track Workflow` — TK chain identity (TK-01 to TK-12), per-unit-type task paths, workspace-by-task mapping, transition mechanism catalog, human intervention budget, failure routing matrix, cross-workspace anti-drift signals; Hub-internal substantive for TK-01/TK-02/TK-03 (Hub-authored), TK-12 (operator merge-decision terminal gate), §9 Hub Claude soft compliance trigger phrases | The CC-side operational substantive detail is owned by the CC substantive Development Track Workflow canonical. |

**Fully migrated sources (4)** — no Hub canonical residue retained; cross-workspace references generalized at Hub:

| Migrated source | CC-side substantive boundary | Hub-side reference adjustment |
|---|---|---|
| `[RULE] Codex Plugin Usage` | The substantive detail is owned by the CC substantive Codex Plugin Usage canonical. | Hub-side handoff documentation refers to "code review enforcement at the CC-side substantive canonical" |
| `[MECH] Code Quality Rule Set` | The substantive detail is owned by the CC substantive Code Quality Rule Set canonical. | Hub-side TDDs reference "code quality enforcement at the CC-side substantive canonical" |
| `[MECH] Dev-Loopback Mode` | The substantive detail is owned by the CC substantive Dev-Loopback Mode canonical. | Hub-side handoff documentation refers to "dev-environment runnability contract at the CC-side substantive canonical" |
| `[MECH] Tools Health Cadence` | The substantive detail is owned by the CC substantive Tools Health Cadence canonical. | Hub-side handoff documentation refers to "periodic tools health inventory at the CC-side substantive canonical" |

Each split source's §0 boundary chapter declares "what this source owns" (Hub-side constitutional + Hub-internal substantive) and "what this source does not own" (CC substantive content externalized + adjacent-source boundaries).

### 5.4.5 Anti-drift signals

- Substantive content (runtime configs, command flags, fixture data) appearing in a Hub Constitutional canonical → externalize to the tool's runtime
- Constitutional content (scope boundary, contractual interface, identity declaration) appearing only in a tool-runtime Substantive file with no Hub canonical SOT → promote to Hub canonical
- A Hub `[REF]` source mirroring Substantive content from a tool runtime rather than indexing its existence → reduce to index pointer
- A Hub-side DS instance mirror re-introduced (a `[REF]` DS instance copy, or DS instance content inlined into a Hub canonical) → the §5.2 two-way model holds no DS instance copy at Hub; the Hub-side DS touchpoint is the transient export conformance review per DSG §12.3, not a persisted mirror

---

# 6. Hub canonical scope boundary

## 6.1 What hub canonical covers

The Hub canonical set covers HDC project work:
- Specification artifact production (PRDs, TDDs, UX Design Spec instances at phase-level and per-feature granularities, intents, acceptances, test plans, ADRs, OpenAPI, IA, Permission Model, phase test plan masters)
- Development Track orchestration (the TK sequence governing AI-dev work, including TK-02 internal Step 2.1 / 2.2 / 2.3 sub-structure)
- Cross-tool workflow handoffs (operator-mediated content flows between Hub/CD/CC for HDC project work)
- Design System governance (the two-way distributed DS for HDC applications, including the CC-mirror sync discipline)
- Application Lifecycle Handoff (AI-dev to human dev team for HDC applications)
- Code quality and milestone gating for HDC applications
- The harness governing how operator and AI work together on HDC project content

## 6.2 What hub canonical does not cover

Hub canonical does not cover:
- Operator's general use of CD for purposes outside HDC project scope (personal slide decks, prototypes unrelated to HDC, non-HDC frontend design ideation)
- Operator's general use of CC for purposes outside HDC project scope (repositories unrelated to HDC, exploratory coding outside the HDC monorepo)
- Operator's general chat use of Claude.ai outside HDC project context
- Internal CD product behavior (the operator's experience of CD's tabs, skills, templates as a Claude product surface — that's Anthropic product domain)
- Internal CC product behavior (Claude Code CLI behavior, plugin behaviors, etc. — Anthropic product domain)

This is a scope boundary, not a content boundary. The same operator may simultaneously be using a workspace for HDC purposes (subject to hub canonical) and for non-HDC purposes (not subject). Hub canonical applies only to the HDC-scoped use. Any canonical reference to CD or CC behavior implicitly means the HDC-scoped use; the qualifier need not be repeated and becomes relevant only when an audit question arises about jurisdiction, which this §6 boundary resolves.

---

# 7. Asset systems and reuse mechanisms

Three asset systems coexist across the three workspaces, each with a distinct purpose:

## 7.1 Hub [TPL] family

**Location**: Hub workspace, `hdc_tpl_*.md` files
**Purpose**: Spec content contract — answers "what content dimensions a specification artifact should cover"
**Examples**: [TPL] PRD Prototype MVP, [TPL] TDD, [TPL] UX Design Spec (the coverage framework for CD design files and the Hub-authoring template for UX Design Spec instances), [TPL] ADR Spec, [TPL] Phase Test Plan, [TPL] Intent and Acceptance Interface Writing Standard, [TPL] Test Plan YAML Schema, [TPL] PRD-TDD to Intent/Acceptance Conversion Spec, [TPL] Options Paper, [TPL] Problem Framing Memo
**Authoring**: Hub-authored, governed by [MECH] Canonical File Self-Audit
**Consumer**: Hub Claude when producing specification artifacts (including UX Design Spec instances at TK-02 step 2.3)

## 7.2 CD Templates

**Location**: Inside CD, per project or shared across operator's CD organization
**Purpose**: Visual instance shortcut — answers "how to quickly generate similar visual artifacts"
**Examples**: Operator-authored slide deck templates, prototype templates, layout templates
**Authoring**: Operator-authored inside CD via Share menu → File type per CD setup screen note
**Consumer**: CD's generation engine when the operator selects "From template" instance type

## 7.3 CD Skills

**Location**: Inside CD, system-provided
**Purpose**: Output form encapsulation — answers "what generation behavior to apply to produce output"
**Observed skills**: see the §3.4 skill-family table for the current observable skill set and the output form each produces
**Authoring**: Provided by the Claude Design product
**Consumer**: CD's generation engine when the operator selects skills for a project

## 7.4 Coexistence rules

The three asset systems run in parallel without overlap:
- Hub [TPL] defines content contracts; CD Templates and CD Skills are about visual form
- Hub [TPL] authoring authority is primary for HDC spec content; CD Templates / Skills do not author HDC spec content (they generate visual artifacts the operator may transfer to Hub for spec authoring)
- A single concept may have parallel presence in multiple systems (e.g., a "feature design" has a Hub [TPL] UX Design Spec content contract — what fields the UX Design Spec instance must cover — and uses CD Skills like Hi-fi design + Interactive prototype to generate the design files that become the source material for the UX Design Spec instance), but the asset roles differ
- Hub canonical does not describe internal rules of CD Templates or CD Skills usage (per §6.2 scope boundary)

---

# 8. Canonical inventory by workspace

## 8.1 Hub-held canonical (current, post-Phase-3 refactor)

Hub workspace holds the canonical set listed under Hub PK `hdc_*.md` files. The current set by family (post-Phase-3 constitutional / substantive split per [OS] §0.1.5 Premise 5):

| Family | Members | Role |
|---|---|---|
| [OS] | Project Operating Model | Meta authority |
| [PRIN] | HR Digital Decision Design Principles, People Experience Design Principles | Cross-topic judgment |
| [POL] | Digital Solution Policy Architecture Map | Cat 1 policy architecture |
| [REF] | People Journey and Moments Catalog, Hub-CD-CC Architecture (this source) | Stable references |
| [RULE] | DingTalk MD Format Control, Workspace Topology (**constitutional residue + Hub-internal substantive post-split** — multi-node operational details migrated to CC), Claude Code Architecture Rules (**constitutional residue post-split** — subagent roster / context scopes / repository layout / skill catalog migrated to CC), Design System Governance | Operational rules across multiple Cat scopes |
| [MECH] | Development Track Workflow (**constitutional residue + Hub-internal substantive post-split** — TK-04~TK-12 execution mechanics migrated to CC), CI/CD Milestone Policy (**constitutional residue post-split** — gate criteria detail migrated to CC), Application Lifecycle Handoff, Cross-Tool Workflow Handoff, Canonical File Self-Audit, Sign-Off Cleanup Policy | Governance mechanisms |
| [TPL] | Options Paper, Problem Framing Memo, PRD Prototype MVP, TDD, UX Design Spec, Test Plan YAML Schema, PRD-TDD to Intent/Acceptance Conversion Spec, Intent and Acceptance Interface Writing Standard, ADR Spec, Phase Test Plan | Content contract templates |

The Phase-3 split and fully-migrated source set is stated authoritatively in §5.4.4.

Notes on inventory:
- **Constitutional / substantive boundary**: per [OS] §0.1.5 Premise 5, Hub canonical owns constitutional content (cross-workspace interface) plus Hub-internal substantive content (e.g., Hub Claude behavior). The CC-side substantive canonical layer at CC's own runtime owns CC-internal operational details. The post-split Hub residues at [RULE] WT, [RULE] CCAR, [MECH] CI/CD, [MECH] DTW retain only the constitutional + Hub-internal-substantive portions; their CC-side substantive content is at CC.

## 8.2 CD-held substantive content

CD workspace holds these substantive content forms (none of which are canonical sources at the Hub):

| Content form | Hub canonical governance | Notes |
|---|---|---|
| DS instance (SOT for DS content) | [RULE] Design System Governance | DS instance authored inside CD as SOT; CD-generated markdown export reviewed Hub-side against DSG §15 then synced to the CC mirror at `specs/design-system.md` per DSG §12 two-way distribution model |
| CD-authored substantive rules within a DS instance | [RULE] Design System Governance | Operator audits the DS markdown export (DSG §15 review) before syncing the CC mirror |
| Phase-level design file (when any feature in the phase has tier_1_involved=true) | [TPL] UX Design Spec (coverage framework) + [MECH] Cross-Tool Workflow Handoff §2.2 (transfer contract) | One CD-native design file per phase with embedded annotations and per-feature internal labeling; transferred to Hub at TK-02 step 2.3 for Hub Claude to consume per-feature in UX Design Spec instance authoring; transferred to CC at TK-04 as visual reference alongside Hub-authored per-feature UX Design Spec instances |
| Operator-authored CD Templates | None (per §7.2 scope) | Outside hub canonical scope |
| Operator-authored CD Projects and stakeholder review outputs | [MECH] Cross-Tool Workflow Handoff (for HDC-scoped projects only) | Output bundles audited before transfer |

## 8.3 CC-held substantive content (post-Phase-3 refactor)

CC workspace holds these substantive content forms (none of which are canonical sources at the Hub, per [OS] §9.4 non-canonical naming, with the **CC-side substantive canonical layer** introduced in Phase 3 per [OS] §0.1.5 Premise 5):

| Content form | Hub canonical governance | Path |
|---|---|---|
| Application code, tests, configurations | [RULE] Claude Code Architecture Rules holds the constitutional residue (tier architecture); the substantive detail is owned by the CC substantive Claude Code Architecture Rules canonical and the CC substantive Code Quality Rule Set canonical | Monorepo files |
| CC-internal canonical files | This source frames the CC canonical layer's existence and tier-aligned hierarchy (§4.1, §5.4); the substantive detail is owned by the CC substantive Memory Bank Layout canonical (CLAUDE.md hierarchy paths and authoring discipline), the CC substantive Claude Code Architecture Rules canonical (`.claude/` rule / agent / skill / hook content discipline), and the CC substantive Codex Plugin Usage canonical (`.claude/commands/` code-review command shortcuts) | `.claude/rules/`, `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, `.claude/hooks/`, `CLAUDE.md`, `apps/{slug}/CLAUDE.md` |
| CI/CD configurations | [MECH] CI/CD Milestone Policy holds the constitutional residue (M0-M4 ladder identity + Test Evidence Report schema); the substantive detail is owned by the CC substantive CI/CD Milestone Policy canonical | `.github/workflows/*.yml` |
| Quality tool configurations | CC substantive Code Quality Rule Set canonical | `monorepo-root/configs/eslint/`, `monorepo-root/configs/checkstyle/`, etc. |
| Fixture / placeholder data | CC substantive Dev-Loopback Mode canonical | `monorepo-root/fixtures/`, `monorepo-root/.dev-loopback/` |
| Code review tooling (Codex) | CC substantive Codex Plugin Usage canonical | CC-internal |
| Periodic tools health inventory | CC substantive Tools Health Cadence canonical | CC-internal |
| DS code-time mirror | [RULE] Design System Governance §12 | `specs/design-system.md` (read-only mirror of CD SOT) |
| Operator-personal manuals | None (operator-personal, per [OS] §9.4) | `MANUAL_*.md` files |

---

# 9. Handoff topology

The three workspaces (Hub / CD / CC) operate as advisor-actor pairs: Hub is the content-and-governance advisor whose output the actors (CD on presentation side, CC on implementation side) consume; CD is the presentation advisor whose design files Hub consumes for UX Design Spec authoring at TK-02 step 2.3 and CC consumes as visual reference at TK-04+. During the current CD research preview operating period, direct CD ↔ CC coupling is intentionally not enabled — all inter-workspace flow is operator-mediated per §9.1 / §9.2 / §9.3 below. The trigger conditions for re-enabling direct CD ↔ CC coupling are recorded in §10.

There are three operator-mediated handoff paths between the workspaces. Each is operationalized by [MECH] Cross-Tool Workflow Handoff into content contracts (what content moves, what audit applies, what acknowledgment closes the handoff).

## 9.1 Hub ↔ operator ↔ CD path

**Hub → operator → CD direction:**

For phase-level design work (TK-02 step 2.2, when any feature in the phase has TDD `tier_1_involved=true`):
- Hub produces strategic framing for the phase, PRD main body (chapters for each tier-1-involved feature), TDD main body (§4.{feature-slug} content for each tier-1-involved feature)
- Operator drops full text of relevant PRD + TDD sections (across all tier-1-involved features in the phase) into a single CD project as drop files (v1 strategy per [MECH] Cross-Tool Workflow Handoff §2.1.6: full text, not Hub-pre-extracted)
- Hub Claude assists the operator in drafting an **attention prompt** that enumerates each tier-1-involved feature and directs CD's focus to UI-relevant content per feature within the dropped specs (e.g., "For feature-A focus on the role matrix in PRD §X.Y / the UI vision in §Z / the frontend-display-affecting fields in TDD §4.feature-A.API-Contracts; for feature-B …"). The attention prompt also instructs CD to internally label per-feature design file scope (frame / section / page tag = feature-slug) so Hub TK-02 Step 2.3 can ground each per-feature UX Design Spec instance in the relevant slice
- Operator pastes the attention prompt into the CD project's free-form prompt area
- DS instance reference is already linked at CD setup; no separate transfer needed per cycle

For DS instance authoring (when DS evolution is needed):
- Hub may propose DS instance changes in conversation; operator routes to CD for SOT authoring per [RULE] DSG §12

For stakeholder communication:
- Operator may transfer Hub-produced content excerpts (option comparisons, framing memos) to CD for slide deck or visual generation purposes; this is not HDC spec work but is still HDC-scoped

**CD → operator → Hub direction:**

For the phase-level design file (TK-02 step 2.3):
- CD produces one phase-level design file covering all tier-1-involved features in the phase (hi-fi mockups, prototypes, wireframes with embedded annotations and per-feature internal labeling)
- Operator audits the design file for HDC project relevance and per-feature coverage completeness against [TPL] UX Design Spec §2 coverage categories
- Operator transfers the design file to Hub session via attachment / paste / drop file
- Hub Claude iterates per tier-1-involved feature: locates the feature's labeled slice in the design file, performs the design file quality check at TK-02 step 2.3 using [TPL] UX Design Spec §3 reviewer checklist — a spec-readiness review against that feature's PRD/TDD scope per [RULE] DSG §13.3
- If a feature's quality check passes: Hub Claude authors that feature's UX Design Spec instance markdown drawing from the relevant design file slice
- If a feature's quality check fails: Hub Claude surfaces findings; operator routes back to CD for revision (Hub → CD direction with updated prompt context targeting that feature's slice or coverage)

For DS instance changes (per DSG §12):
- CD generates DS markdown export reflecting updated SOT content
- Operator brings the export into a Hub conversation for the DSG §15 export conformance review, then transfers it to the CC mirror (`specs/design-system.md`)

## 9.2 Hub ↔ operator ↔ CC path

**Hub → operator → CC direction:**
- Hub produces specification artifact main bodies (PRD, TDD, per-feature UX Design Spec instances, per-slice intent main, acceptance main, test-plan main)
- Hub produces or updates constitutional canonical sources
- Operator transfers content to CC via the operator's chosen mechanism for each content type — for canonical: any access mechanism the operator chooses (e.g., local clone of the canonical GitHub repository, paste, etc.; mechanism is operator-personal infrastructure, not canonical-governed); for spec artifacts: placing files at canonical paths in the monorepo
- Per-feature UX Design Spec instances land at `apps/{slug}/specs/ux-design-spec/{feature-slug}.md`; per-slice spec artifacts land at `apps/{slug}/specs/{intent,acceptance,test-plan}/{slice-id}.{md,yaml}`

**CC → operator → Hub direction:**
- CC produces Codex review output (review object: application code)
- CC produces CC-internal canonical updates (when subagent / skill / hook / rule files change)
- CC produces DS code change notifications (when DS code shifts, routed through DSG §12 for CD SOT authoring + CC-mirror re-sync)
- Operator transfers these to Hub for judgment, archive, or routing

## 9.3 CD ↔ operator ↔ CC path (research-preview-decoupled)

During the current operating period (CD research preview), there is no direct CD ↔ CC coupling. The handoff path is mediated by the operator with explicit audit:

**CD → operator → CC direction:**
- Two content types flow this path:
  - **Phase-level design file** (CD-native format): transferred to CC at TK-04 entry as **visual reference** accompanying the Hub-authored per-feature UX Design Spec instances. CC consumes the design file visually (mockups, layout reference, motion observation) — typically focusing on the slice labeled with the active feature-slug — but does NOT author UX-touching field values from it; those are Hub-authored at TK-03 from the UX Design Spec instance which itself was authored at TK-02 step 2.3 from the relevant design file slice.
  - **DS markdown export** (per DSG §12 sync cycle): transferred to CC mirror at `specs/design-system.md` for code-time DS reference consumption by SK-F skill
- Operator audits both content types for HDC project relevance and sync correctness before transfer

**CC → operator → CD direction:** (not currently a primary flow)
- If CC code changes affect DS visual representation, the operator notifies CD via Hub routing (CC → Hub → CD path through DSG §12)
- Direct CC → CD content flow is rare relative to CD → CC

## 9.4 Direct CD ↔ CC coupling: not enabled, and architecturally non-trivial

CD has a native "Send to Claude Code" handoff path in its product surface. Direct CD ↔ CC coupling is not enabled for HDC project use, and the rationale is **primarily architectural rather than procedural**:

**Architectural primary reason** — CD output and CC input are not at the same content layer. CD produces design files (raw source material in visual + informal annotation form, per §3.4.1); CC consumes UX Design Spec instances at two granularities (phase-level for cross-cutting UX context + per-feature for feature-scoped UX content; structured markdown integrated with PRD / TDD / per-slice spec artifacts). The synthesis from raw material to CC-consumable spec is a substantive authoring step that currently resides at Hub (TK-02 Step 2.3 per [MECH] DTW). Direct CD → CC content transfer would bypass this synthesis, leaving CC with input that is not at its consumption layer.

**Operational secondary reason** — even if CD output could be CC-consumable, the current research-preview operating period adds caution. The operator routes all CD → CC content through audited operator-mediated transfer (§9.3) for traceability and governance.

The two reasons compound but are distinct. The architectural reason is structural to the current three-workspace synthesis division (CD = design SOT, Hub = spec synthesis, CC = code generation). The operational reason would relax with research-preview maturity. The architectural reason would only relax if the synthesis responsibility migrated.

---

# 10. Conditions under which direct CD ↔ CC coupling could become viable

## 10.1 Architectural condition (necessary)

The synthesis step currently at Hub TK-02 Step 2.3 must move — either to CD (CD evolves spec authoring capability) or to CC (CC evolves to consume raw design files directly and synthesize internally) or to a new intermediate workspace replacing Hub's middle role. Without this migration, direct CD ↔ CC coupling leaves a content-layer gap that CC cannot bridge alone.

This is a non-trivial architectural change to the three-workspace responsibility division. It is not predictable on the current roadmap; it is registered here as a structural prerequisite, not a near-term plan.

The architectural condition is treated as shifted when a concrete, observable product capability removes the content-layer gap — for example, CD ships a structured-spec export (design output that is CC-consumable specification, not raw design files), OR CC ships a design-file-ingestion skill (CC can consume raw CD design files and synthesize the spec internally). The §10.3 verification path triggers on such an observable, not on a general belief that CD/CC has "evolved".

## 10.2 Operational conditions (necessary)

If the architectural condition is met, the following operational conditions remain to gate direct coupling:

1. **CD reaches general availability (GA)** — exits research preview status as a Claude product
2. **CD design file transfer format is documented** — concrete file structure and naming of CD design files when transferred is documented stably enough that the consumer (CC, or whichever workspace owns synthesis post-migration) can consume them deterministically; also covers DS markdown export format stability
3. **CD token cost is stabilized** — per-operation token consumption pattern is predictable enough for the HDC operator to budget around

All three operational conditions plus the architectural condition are required. Any operational condition alone (without architectural change) is insufficient — GA + documented format + stable token cost still leave the content-layer gap.

## 10.3 Path to verification

If the operator believes the architectural condition has shifted (e.g., CD's product surface evolves to include spec authoring, or CC evolves to consume design files directly):

1. The operator runs a verification exercise targeting both the architectural condition and the three operational conditions, analogous to the §3.7 R1 verification
2. Verification findings are recorded as an ADR in the Hub workspace per [TPL] ADR Spec
3. The ADR's decision section specifies whether to re-enable direct coupling, and if so, with what initial scope
4. If re-enabled, this source ([REF] Hub-CD-CC Architecture) is revised in the same revision to remove the "decoupled-by-default" framing in §9.4 and replace with the current direct-coupling discipline; §10 itself is revised to reflect the new architectural division

## 10.4 Reversibility

If direct coupling is re-enabled and subsequently produces audit failures or content quality issues, the operator may revert by reverting the ADR and the §9.4 + §10 revision. Reversibility is preserved because the operator remains the controlling node across all coupling states.

---

# 11. Glossary

| Term | Definition |
|---|---|
| Workspace | An AI product surface (Hub, CD, or CC) where the operator works on HDC project content. Not to be confused with multi-node dev environment "workspaces" inside CC, which are owned by [RULE] Workspace Topology. |
| Operator-mediated | A flow that requires explicit operator action (read, audit, transfer) to move content from one workspace to another. The current default for all cross-workspace flows. |
| Hub canonical | A canonical source held at Hub PK `hdc_*.md` under [OS] governance; distinct from the CC-side substantive canonical layer held at the CC tool runtime. |

---

# 12. Revision discipline notes

This source's content is updated under [OS] §8.5.2 same-revision discipline when:
- A new workspace is added or removed (significant architectural change)
- The tripartition assignment changes (e.g., a workspace acquires or loses a dimension)
- The DS distribution model changes (e.g., DS SOT migrates between workspaces; mirror locations change)
- The handoff topology changes (new path added; existing path removed)
- The direct CD ↔ CC coupling status changes per §10
- Hub canonical scope boundary §6 changes (e.g., a new workspace category enters HDC scope)
- The Hub-side UX Design Spec authoring model changes (e.g., reassigning authorship between Hub and CD)

Routine updates (e.g., adding a new canonical to the §8.1 inventory) are made without same-revision constraint, but [OS] §8.5.2 pairing discipline applies if the addition creates new cross-source pairings.

When this source is revised, [OS] §2.3.2 Cross-category layer membership list is checked for consistency with this source's Cross-category layer self-declaration; both must agree.
