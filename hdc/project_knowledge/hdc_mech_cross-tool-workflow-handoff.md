# [MECH] Cross-Tool Workflow Handoff

- **Project**: HR Digital Cockpit
- **Document Type**: Workflow Orchestration Specification
- **Status**: Active canonical
- **Role**: Stable source defining the content contracts for the three operator-mediated cross-tool handoff paths during AI-dev work (Hub ↔ operator ↔ CD, Hub ↔ operator ↔ CC, CD ↔ operator ↔ CC) — including what content moves in each direction, operator transfer actions, audit steps, integration steps, reminder-form discipline, and the DS markdown export review-and-sync mechanism that maintains the CC DS mirror
- **Source Category**: Cat 4
- **Management-System Role**: Workflow orchestration specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; conversation discipline rules in [OS] §7.2 apply to the Hub Claude trigger behavior in §7. Cross-source ownership map for the Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control).
- **Relationship to [REF] Hub-CD-CC Architecture**: Operationalizes. [REF] Hub-CD-CC Architecture §9 declares the three-path handoff topology, and §9.4 declares the decoupled-by-default discipline during CD research preview; §3.4.1 declares CD outputs design files (CD-native visual artifacts); §5.2 declares the two-way distribution model (CD = SOT / CC = code-time mirror). This source defines the concrete content contracts and operator actions that realize those paths.
- **Relationship to [MECH] Application Lifecycle Handoff**: Distinct lifecycle layer. [MECH] Application Lifecycle Handoff governs the application-level handoff event (AI-dev → human dev team, terminal). This source governs cross-tool content flows during AI-dev work (recurrent during the entire AI-dev period). Both reference operator-mediated discipline but at different boundaries.
- **Relationship to [RULE] Design System Governance**: Anchored. DSG §1.1 owns the two-way distribution model — CD = SOT at the CD workspace, CC = code-time mirror at `specs/design-system.md`. This source operationalizes the cross-tool content flows that maintain that model:
  - CD-authored **design files** flow CD → Hub at TK-02 Step 2.3 entry (§2.2) carrying per-feature visual UX content for Hub-side UX Design Spec instance authoring
  - CD-authored **DS markdown export** flows CD → Hub (DSG §15 export conformance review) → CC mirror at change finalization (per DSG §12.3 + §12.7)
  - Hub-authored **UX Design Spec instance markdown** (Hub TK-02 Step 2.3 output) flows Hub → CC at TK-04 entry alongside other spec artifacts (§3.1)
  - The two-way distribution generates DS-related cross-tool flows in the Hub ↔ CD and Hub ↔ CC handoff paths; cross-tool flows that carry DS-related content apply DSG rules accordingly. DSG §12 additive update path drives DS instance changes at the originating feature's M4 → merge-to-main milestone, at which point the reviewed DS markdown export syncs to the CC mirror
- **Relationship to [RULE] Codex Plugin Usage**: **Migrated to CC substantive canonical (Phase 3)**. The CC → operator → Hub direction in §3.2 includes code review tool output flow; the specific code review tool (historically Codex) is governed by CC substantive Codex Plugin Usage canonical at CC. This source declares only the cross-workspace content contract; the fire-condition and output-processing rules live at CC.
- **Relationship to [RULE] Workspace Topology**: Anchored. Workspace inception governance follows [RULE] Workspace Topology constitutional residue §5; the specific Hub canonical access mechanism at CC is operator-personal infrastructure (declared substantively in §3.1.1). Hub-to-assigned_node onboarding mechanics referenced from §3.1 follow CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4).
- **Relationship to [MECH] Development Track Workflow**: Cross-tool handoffs operate continuously during AI-dev work driven by DTW TK sequence. This source does not author TK orchestration but provides the content contracts that DTW TKs invoke when they touch cross-tool flows. Key TK-bound flows:
  - TK-02 Step 2.2 entry: Hub → CD drop files (§2.1)
  - TK-02 Step 2.2 → Step 2.3: CD → Hub design files transfer (§2.2)
  - TK-03 → TK-04 entry: Hub → CC spec bundle including UX Design Spec instance markdown + design files as visual reference (§3.1)
  - TK-11 code review tool output → Hub: CC → Hub (§3.2; specific tool governed by CC substantive canonical)
  - TK-12 DS change finalization (when applicable): DS markdown export §15 review + sync to the CC mirror (§2.2 + §3.1, operator-mediated)
- **Relationship to [TPL] UX Design Spec**: Cross-references. CD-authored design files transferred via §2.2 are the source material for the Hub-authored UX Design Spec instance (authored per [TPL] UX Design Spec at TK-02 Step 2.3). The UX Design Spec instance markdown is transferred via §3.1 to CC at TK-04 entry as part of the spec bundle.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [MECH] Cross-Tool Workflow Handoff` header fields per [OS] §8.5.1a)

## How to use this source

Non-obvious routing cues (the primary cross-tool-transfer uses follow directly from §0.1):
- This source also houses the review of whether a Hub Claude conversation has drifted across cross-tool handoff boundaries — reach for it for that drift review, not only for an active transfer.
- The DS markdown export §15 conformance review and CC-mirror sync mechanics live here, not in [RULE] Design System Governance — consult this source for that review at change finalization.
- This source is **not** an enforcement mechanism: it declares reminder-form discipline (per §5) rather than mechanical enforcement.

## Scope note

This source applies to:
- Cross-tool content flows during AI-dev work between Hub / CD / CC for HDC project content
- Operator transfer actions that mediate these flows
- Audit and integration steps at each end of each transfer
- DS markdown export §15 conformance review and CC-mirror sync mechanics (per DSG §12.3)

This source does not apply to:
- Cross-tool flows for operator activities outside HDC project scope (per [REF] Hub-CD-CC Architecture §6 hub canonical scope boundary)
- Internal product-level behaviors of Claude Design or Claude Code (those are Anthropic product domain)
- Application-level handoff to human dev team (owned by [MECH] Application Lifecycle Handoff)

---

# 0. Boundary and position

## 0.1 What this source owns

- The three operator-mediated cross-tool handoff paths during AI-dev work: Hub ↔ operator ↔ CD, Hub ↔ operator ↔ CC, CD ↔ operator ↔ CC
- Per direction within each path: content contract (what moves), operator transfer actions, audit steps, destination integration steps
- The decoupled-by-default discipline for CD ↔ CC during CD research preview, including the operator-audit gate
- Reminder-form constraints (this source establishes [Enforcement·reminder-only]; Hub Claude surfaces reminders but does not enforce)
- Audit failure handling procedures
- Hub Claude soft compliance trigger phrases for cross-tool handoff conversations
- DS markdown export review and CC-mirror sync mechanics (the cross-tool mechanism realizing the DSG §12.3 export conformance review + CC-mirror sync)
- Anti-drift red flags specific to cross-tool handoff boundary violations

## 0.2 What this source does not own

- The three-workspace topology itself (owned by [REF] Hub-CD-CC Architecture)
- Application-level handoff to human dev team (owned by [MECH] Application Lifecycle Handoff)
- DS governance rules and the two-way distribution model specification (owned by [RULE] Design System Governance §1.1 + §12)
- DS markdown export format specification (owned by [RULE] Design System Governance §12.7)
- DSG §13.3 Hub-side consumption discipline rules (owned by DSG)
- Code review tool fire condition rules (owned by CC substantive Codex Plugin Usage canonical)
- TK-by-TK orchestration (owned by [MECH] Development Track Workflow)
- TK-02 internal step structure (Step 2.1 / Step 2.2 / Step 2.3) — owned by DTW §4 TK-02
- UX Design Spec instance content contract — owned by [TPL] UX Design Spec
- Workspace inception discipline (owned by [RULE] Workspace Topology constitutional residue §5 (workspace inception governance))
- Specification artifact content contracts (owned by their respective [TPL] family sources)
- CD platform internal behaviors (Anthropic product domain)
- CC platform internal behaviors (Anthropic product domain)

---

# 1. Three handoff paths overview

## 1.1 Path inventory

Three operator-mediated paths exist among the Hub / CD / CC workspaces. Each path has two directions, yielding six total transfer directions:

| Path | Direction A | Direction B |
|---|---|---|
| Hub ↔ CD | Hub → operator → CD (§2.1) | CD → operator → Hub (§2.2) |
| Hub ↔ CC | Hub → operator → CC (§3.1) | CC → operator → Hub (§3.2) |
| CD ↔ CC | CD → operator → CC (§4.2) | CC → operator → CD (§4.3) |

The CD ↔ CC path operates under decoupled-by-default discipline during CD research preview (§4.1). The other two paths operate continuously throughout AI-dev work.

## 1.2 Operator-mediated discipline

All cross-tool flows require explicit operator action. No workspace can push content to another workspace autonomously. No workspace has read access to another workspace's session state. Each transfer involves:

1. **Origin produces content** (Hub authors a spec, CD generates design files, CC writes code, etc.)
2. **Operator audits the content** (relevance to destination, quality, scope boundary per [REF] Hub-CD-CC Architecture §6)
3. **Operator transfers the content** (copy / paste / attach / save-as-file as appropriate to destination workspace)
4. **Destination integrates the content** (Hub fills spec field, CD ingests as context, CC reads from working directory, etc.)

The operator's audit is the trust gate. Pre-audit content does not have authoritative status at the destination.

## 1.3 Content contract concept

A content contract for each direction specifies:
- **What content moves**: the substantive content category transferred (e.g., spec main body, design files, DS markdown export, code change notification)
- **Source format**: how the content exists at the origin (e.g., Hub canonical file, CD-native design artifact, CC commit, DS markdown export file)
- **Operator actions**: concrete steps the operator takes to transfer
- **Audit checklist**: what the operator verifies before transfer
- **Destination format**: how the content is integrated at the destination

Content contracts are reminders (per §5), not mechanically enforced contracts. The operator may transfer content that does not meet a contract; in that case, the destination's integration is at the operator's risk.

---

# 2. Hub ↔ operator ↔ CD path

## 2.1 Hub → operator → CD direction

### 2.1.1 What content moves

This direction carries Hub-produced content into a CD session as context for design file generation. Two distinct sub-flows exist:

**Sub-flow A — General context transfer** (any CD session task, including non-HDC-spec design exploration the operator chooses to do with CD):
- Hub spec artifact main body excerpts (PRD content sections, TDD content sections, intent main, acceptance main — relevant portions)
- Strategic framing content (option comparisons, decision rationales)
- Brand / design preferences when articulated by the operator
- People Journey or People Experience principles excerpts when relevant to the design task
- Output expectations stated by the operator

**Sub-flow B — TK-02 Step 2.2 design file production (HDC-specific, structured)**: When a TK-02 Step 2.1 TDD declares `tier_1_involved=true` for one or more features in the phase, the operator initiates **one CD session for the phase** for phase-level design file production (covering all tier-1-involved features in the phase as labeled internal scopes within a single design file — CD designs by phase as its natural unit of visual production, not by feature). The content transferred follows the **CD input strategy v1** owned by [MECH] DTW §4 TK-02 Step 2.2 mechanism note — drop files (PRD + TDD sections for all tier-1-involved features in the phase), attention prompt (enumerating each feature and instructing CD to internally label per-feature design file scope by feature-slug), DS grounding, and output expectations as enumerated there; the phase-level design-file deliverable list is stated in §2.2.1.

**Sub-flow C — DS instance authoring input (HDC-specific, when a DS change is needed)**: When a DS instance change has been approved per [RULE] DSG §12, the operator initiates a CD session for CD-side DS instance authoring. The content transferred:
- The current `[RULE] Design System Governance` text — transferred to CD as a **read-only input** so CD authors the DS instance change in conformance with DSG §2-§11 and self-checks the change before generating the DS markdown export. DSG's SOT remains at Hub; CD receives it as a transferred input, not as owned content
- The specific change request — the additive change plan (the Hub-authored UX Design Spec instance §2.4 entry) or, for a breaking change, the change requirements + rationale traceable to the triggering feature's PRD/TDD

### 2.1.2 Source format

Hub content exists as:
- Hub canonical sources (the `hdc_*.md` file set in the canonical repository / Hub PK); Hub Claude reads them via the RAG layer per [OS] §1.4; the specific access channel that surfaces canonical content into a Hub conversation is operator-personal infrastructure (per §3.1.1)
- Spec artifacts at `apps/{app-slug}/specs/**` or similar
- Conversation-level content produced by Hub Claude

### 2.1.3 Operator actions

For Sub-flow A (general context):

1. Identify which Hub content is relevant to the CD task (operator judgment)
2. Open or create a CD project
3. Transfer content to CD using one or more of:
   - Paste content into the CD project's free-form prompt
   - Drop files (Hub-produced markdown, screenshots, diagrams) into the CD drop-files area
   - Attach references when applicable
4. State output expectations clearly in the CD prompt

For Sub-flow B (TK-02 Step 2.2 design file production):

1. Open one CD project for the phase (one project covers all tier-1-involved features in the phase as labeled internal scopes within a single design file)
2. Drop the full relevant PRD + TDD sections (for every tier-1-involved feature in the phase) as files into CD
3. Confirm the CD project's DS instance is linked (CD's own DS SOT per [REF] Hub-CD-CC Architecture §5.2; no per-cycle DS transfer needed)
4. Paste the attention prompt — enumerating each tier-1-involved feature and directing CD to the UI-relevant sections of the drop files per feature; the prompt also instructs CD to internally label per-feature design file scope (frame / section / page tag = feature-slug) so Hub TK-02 Step 2.3 can ground each per-feature UX Design Spec instance in the relevant slice
5. State the design file output expectations explicitly (per the phase-level design-file deliverable list in §2.2.1, including the per-feature labeling invariant)
6. Initiate CD design file production

For Sub-flow C (DS instance authoring):

1. Open the CD session holding the HDC DS instance
2. Transfer the current `[RULE] Design System Governance` text into the CD session as read-only context
3. Transfer the specific change request (the §2.4 additive plan, or the breaking-change requirements + rationale)
4. State that CD must author the change in conformance with DSG §2-§11 and self-check the change before generating the DS markdown export

### 2.1.4 Audit checklist (pre-transfer)

Before transferring, the operator verifies:
- Content is within HDC project scope (per [REF] Hub-CD-CC Architecture §6)
- Content excerpts are coherent without their original document context (CD does not have access to the surrounding spec)
- No accidental inclusion of non-HDC content
- Output expectations are stated explicitly (CD does not infer from spec structure)
- **For Sub-flow B**: the attention prompt enumerates each tier-1-involved feature with specific UI-relevant sections per feature and includes the per-feature internal labeling instruction (frame / section / page tag = feature-slug); the CD project's DS instance is linked; the TDD `tier_1_involved=true` flag is confirmed for every feature whose PRD/TDD content is in the drop file set; no tier-1-involved feature in the phase is missing from the transfer set

### 2.1.5 CD reception

CD receives all Hub content as **free-form context**, not structured spec. CD does not parse PRD sections, TDD chapters, or IA structures programmatically. The operator's responsibility is to extract and frame the content so CD can use it. For Sub-flow B, the attention prompt acts as CD's reading guide; the design files CD produces are CD-native visual artifacts per [REF] Hub-CD-CC Architecture §3.4.1.

---

## 2.2 CD → operator → Hub direction

### 2.2.1 What content moves

This direction carries CD-produced content back into Hub. Three distinct sub-flows exist:

**Sub-flow A — TK-02 Step 2.2 design file transfer (HDC-specific, structured)**: After CD produces the phase-level design file in a TK-02 Step 2.2 session, the operator transfers the design file back to the Hub session for Step 2.3 (per-feature design file quality check + per-feature UX Design Spec instance authoring, iterated over all tier-1-involved features in the phase against the design file's per-feature labeled slices). Content carried:
- CD-authored phase-level design file (hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations and per-feature internal labeling — frame / section / page tag = feature-slug) per [REF] Hub-CD-CC Architecture §3.4.1
- Any new-component / new-token proposals embedded in the design file (these become the source material for the UX Design Spec instance §2.4 New-Components-Or-Tokens entry on whichever per-feature instance the proposal applies to)

**Sub-flow B — DS markdown export review at change finalization (when applicable)**: When a DS change merges at the originating feature's M4 → merge-to-main milestone (per DSG §12.5), CD generates an updated DS markdown export per DSG §12.7. The operator brings the export into the Hub session, where Hub Claude reviews it against the DSG §15 reviewer checklist (the export conformance review per DSG §12.3). On a passing review, the export is committed to the CC mirror (`specs/design-system.md`) — the §3.1 Sub-flow C transfer. Hub retains no copy of the export.

**Sub-flow C — Stakeholder review materials**: Slide decks, prototypes, and other CD outputs for the operator's own use (e.g., presenting to stakeholders) — not integrated into Hub canonical.

### 2.2.2 Source format

CD content exists as:
- CD-authored design files in CD-native format (visual artifacts; format detail per CD platform; the operator transfers via copy, screenshot, paste, or export as appropriate)
- CD-generated DS markdown export at change finalization (text-formatted markdown per DSG §12.7 specification)
- CD project-level descriptions / notes
- CD DS instance state (visible to the operator within CD)

### 2.2.3 Operator actions

**For Sub-flow A — design file transfer at TK-02 Step 2.3 entry**:

1. Audit the CD-authored phase-level design file against the Hub Step 2.3 entry requirements (per [TPL] UX Design Spec §3.1 design file quality check criteria); confirm per-feature internal labeling is present and unambiguous so Hub Step 2.3 can locate each feature's slice
2. Transfer the design file to the Hub session by appropriate means:
   - Paste screenshots of mockups / prototypes (organized by per-feature labeled slice) into the Hub conversation
   - Drop design file exports (PDF / image / link) into the Hub drop-files area
   - Provide a structured description if visual transfer is partial (e.g., embedded textual annotations transcribed into the Hub conversation, keyed by feature-slug)
3. Hub Claude + operator iterate per tier-1-involved feature in the phase, applying [TPL] UX Design Spec §3.1 reviewer checklist against the feature's labeled slice
4. Per-feature disposition determines next step for that feature:
   - **Pass** or **Pass with annotation** → Hub Claude proceeds to that feature's UX Design Spec instance authoring per [TPL] UX Design Spec §3.2
   - **Reject** → return to CD per §6 fallback; the Step 2.2 redo scope is that feature's slice (or full-phase relabeling when the per-feature labeling itself is broken)
5. Note design file provenance in each UX Design Spec instance header (`Source design files` field per [TPL] UX Design Spec §1) — cite the phase-level design file plus the specific labeled slice (frame / section / page tag) matching this instance's feature-slug

**For Sub-flow B — DS markdown export review at change finalization**:

1. At the originating feature's M4 → merge-to-main milestone (TK-12), trigger DS markdown export generation in CD per DSG §12.7
2. Save the export file (operator-side working copy)
3. Bring the export into a Hub conversation; Hub Claude reviews it against the DSG §15 reviewer checklist (the export conformance review per DSG §12.3) — verifying completeness (covers all DS instance section topics per DSG §2) and conformance to DSG §2-§11. On a material finding, the export returns to CD for correction
4. On a passing review, commit the reviewed export to the **CC mirror**: replace `specs/design-system.md` content with the export; commit to the monorepo on the active branch (the §3.1 Sub-flow C transfer)
5. Verify CC mirror version metadata after sync (header semver matches the export's version)
6. Note the review and sync in the slice's evidence or TK-12 conversation log

**For Sub-flow C — stakeholder review materials**:

- No Hub integration required; the material is operator-personal use, not canonical content

### 2.2.4 Audit checklist (pre-transfer)

Before integrating, the operator verifies:

**For Sub-flow A**:
- The phase-level design file is HDC-project-scoped (no accidental inclusion of CD's non-HDC work)
- Per-feature internal labeling (frame / section / page tag = feature-slug) is present for every tier-1-involved feature in the phase; labels are unambiguous so Hub Step 2.3 can locate each feature's slice without operator interpretation
- For each per-feature slice: the slice covers all §2.x topics required by that feature's UX Design Spec instance (per [TPL] UX Design Spec §3.1.1 coverage check), or category absences are explicitly noted
- For each per-feature slice: the slice aligns with that feature's TDD scope (per [TPL] UX Design Spec §3.1.2 alignment check)
- Component references in the design file are in the Hub DS mirror inventory or have a clear additive plan
- No security-sensitive content (credentials, internal Anthropic content) embedded

**For Sub-flow B**:
- DS markdown export is complete (covers all DSG §2 section topics) and current (reflects the just-merged DS change)
- The export has passed the DSG §15 conformance review before the CC mirror is committed
- The CC mirror path is writable and not in a stale-snapshot state

### 2.2.5 Hub integration

**For Sub-flow A**:
- Hub Claude iterates per tier-1-involved feature: performs the §3.1 design file quality check against that feature's labeled slice (per [TPL] UX Design Spec) and, on `Pass` disposition for the feature, proceeds to that feature's UX Design Spec instance authoring per §3.2 of the same template
- Each Hub-authored UX Design Spec instance markdown lands at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` upon TK-02 sign-off (transferred to the assigned_node working directory at hub-to-assigned_node onboarding per §3.1 below)
- The phase-level design file itself is operator-side reference; not committed to the monorepo unless the operator explicitly opts to commit exports at `apps/{app-slug}/design-references/phase-{N}/` for visual reference at TK-04+ (phase-scoped path because the design file itself is phase-level; per-feature scope within the design file is captured by CD's internal labeling, not by the path)

**For Sub-flow B**:
- The DS markdown export is reviewed against DSG §15 in the Hub session (the export conformance review per DSG §12.3); Hub retains no copy of the export
- On a passing review, the CC mirror (`specs/design-system.md`) is updated to the new DS instance version via the §3.1 Sub-flow C transfer
- Committing the export to the CC mirror without the §15 review having passed constitutes a §8 anti-drift red flag

**For Sub-flow C**:
- No Hub canonical state change

---

# 3. Hub ↔ operator ↔ CC path

## 3.1 Hub → operator → CC direction

### 3.1.1 What content moves

This direction carries Hub-produced content into CC for code implementation work. Multiple sub-flows exist:

**Sub-flow A — Hub canonical access at CC**: CC accesses the Hub canonical set (`hdc_*.md` files in the canonical repository) as a **read-only authoritative source**. This canonical declares the contract: one-way Hub → CC flow; CC consumes Hub canonical without modifying it at origin. The specific access mechanism (local clone of the canonical GitHub repository, operator-mediated paste, or any other method) is **operator-personal infrastructure** and not canonical-governed. Hub canonical updates flow to CC at the operator's discretion — typically at workspace inception and as needed when canonical evolves.

**Sub-flow B — Spec artifact transfer at TK-03 → TK-04 entry**: Hub-authored spec artifacts transferred to the assigned_node working directory at TK-04 entry (or at hub-to-assigned_node onboarding when the unit starts). Content carried:
- PRD main (TK-01 output)
- TDD main (TK-02 Step 2.1 output)
- Phase test plan master (TK-02 Step 2.1 output)
- Feature integration test plans (TK-02 Step 2.1 outputs)
- Per-feature slice-lists (TK-02 Step 2.1 outputs)
- App-scoped OpenAPI (TK-02 Step 2.1 output)
- **Per-feature UX Design Spec instance markdown** (TK-02 Step 2.3 output, when authored — landing at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`)
- Per-slice intent / acceptance / test-plan (TK-03 outputs)
- ADRs (operator-curated, when applicable)
- **CD-authored phase-level design file** (when any feature in the phase has Tier 1 involved) — accompanies as visual reference for CC implementation; CC focuses on the per-feature labeled slice matching the active feature-slug; operator-side reference, not committed to the monorepo unless the operator explicitly opts to commit exports at `apps/{app-slug}/design-references/phase-{N}/` (phase-scoped path because the design file is phase-level)

**Sub-flow C — DS markdown export sync to CC mirror (at change finalization)**: At a feature's M4 → merge-to-main milestone when that slice carries a DS change, the CC mirror at `specs/design-system.md` is updated to the new DS version. The export is first reviewed against DSG §15 in the Hub session (§2.2 Sub-flow B); on a passing review the operator commits the reviewed export to the CC mirror.

**Sub-flow D — Cross-model review reminder content**: Conversational reminders fired at TK-01 / TK-02 sign-offs per [MECH] DTW; transferred informally into CC sessions when downstream TKs are operating in CC.

**Sub-flow E — Operator-curated working memos**: Free-form notes relevant to the current TK.

### 3.1.2 Source format

Hub content exists as:
- Hub canonical files (the `hdc_*.md` file set in the canonical repository / Hub PK)
- Spec artifacts in the monorepo (`apps/{app-slug}/specs/**`) authored in Hub Claude conversations and committed by the operator
- Conversation content (one-off advisory output)

### 3.1.3 Operator actions

**For Sub-flow A — Hub canonical access at CC**:

1. Ensure CC has access to the current Hub canonical source via the operator's chosen mechanism (e.g., local clone of the canonical GitHub repository synced to the latest commit; or operator-mediated paste of relevant content into the CC session) — the mechanism is operator-personal infrastructure per the Sub-flow A declaration above
2. When Hub canonical evolves (new commit lands at `claude-canonical/hdc/project_knowledge/`), the operator refreshes CC's access via the operator's chosen refresh mechanism for the access method established at step 1
3. CC contract: Hub canonical is read-only at CC; CC does not modify Hub canonical at its origin

**For Sub-flow B — spec artifact transfer at TK-03 → TK-04 entry**:

1. Place all Hub-authored spec artifacts at the canonical paths in the monorepo per the repository layout owned by the CC-side substantive Claude Code Architecture Rules canonical (e.g., `apps/{app-slug}/specs/prd/phase-{N}.md`, `apps/{app-slug}/specs/tdd/phase-{N}.md`, `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` when authored at TK-02 Step 2.3, `apps/{app-slug}/specs/intent/{slice-id}.md`, etc.)
2. Commit on the appropriate branch per [RULE] Workspace Topology §5
3. The spec is read by CC from the working directory when relevant TKs execute
4. For the CD-authored phase-level design file (operator-side reference at TK-04+): transfer to the assigned_node operator's working environment; commit only if the operator opts to make it available within the monorepo, in which case the commit path is `apps/{app-slug}/design-references/phase-{N}/`

**For Sub-flow C — DS markdown export sync to CC mirror (at change finalization)**:

1. At the slice's TK-12 M4 → merge-to-main, when this slice carries a DS change, the CD-generated DS markdown export is first reviewed against DSG §15 in the Hub session per §2.2 Sub-flow B
2. On a passing review, update the CC mirror: replace `specs/design-system.md` in the monorepo on the active branch (typically `main` after merge) with the reviewed export
3. Verify CC mirror header version matches the export's declared version after sync
4. The DS markdown export source is the CD-generated export reviewed at §2.2 Sub-flow B

**For Sub-flow D — cross-model review reminder transfer**:

1. The reminder is conversational, not file-based
2. The operator carries the reminder text into the CC session if the TK is being executed in CC (typically TK-01 / TK-02 are executed in Hub, but the reminder may inform downstream CC TKs)

### 3.1.4 Audit checklist (pre-transfer)

Before transferring, the operator verifies:
- Constitutional canonical files are at the current PK state (no stale snapshots)
- Spec artifacts are at sign-off form per [MECH] Sign-Off Cleanup Policy when transferring to the monorepo
- Spec artifact paths match the canonical layout per the repository layout owned by the CC-side substantive Claude Code Architecture Rules canonical
- **For TK-04 entry (Sub-flow B)**: when Tier 1 features are present, the per-feature UX Design Spec instance markdown is present in the transfer set at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`; the M0 entry self-check at TK-04 will validate the markdown's grounding against CC DS mirror via SK-F
- **For DS markdown export sync (Sub-flow C)**: the export has passed the DSG §15 conformance review (§2.2 Sub-flow B) before the CC mirror is committed

### 3.1.5 CC reception

CC reads canonical via the inception-sync snapshot. CC reads spec via monorepo file paths. CC does not maintain a parallel Hub-canonical-mirror copy (per [OS] §1.4 visibility boundary).

For the UX Design Spec instance markdown (when present), CC's TK-04 M0 entry self-check verifies the markdown's component / token / pattern references against the CC DS mirror via SK-F per [MECH] DTW §4 TK-04 mechanism. Design files (when accompanying as visual reference) are not parsed programmatically by CC; the operator may share specific design file images inline in the CC session when CC needs visual context for a specific implementation question.

---

## 3.2 CC → operator → Hub direction

### 3.2.1 What content moves

This direction carries CC-produced content back to Hub:
- Code review tool output (review object: application code; produced at TK-11; the specific code review tool is owned by CC substantive Codex Plugin Usage canonical)
- CC-internal canonical change notifications (when `.claude/rules/`, `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, `.claude/hooks/` files are added, modified, or removed)
- CC-side DS mirror drift detection notifications (when CC's M0 entry self-check, or compliance-checker A9, or SK-F runtime surfaces inconsistency between CC mirror and the in-flight code)
- Architecture decision notes that warrant ADR authoring at Hub

### 3.2.2 Source format

CC content exists as:
- Code review tool output files at `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md` (file path convention per CC substantive Codex Plugin Usage canonical)
- CC-internal canonical files at `.claude/**` and `CLAUDE.md` paths
- CC DS mirror at `specs/design-system.md` (read-only at CC per DSG §12.6)
- CC session conversation content for architectural observations

### 3.2.3 Operator actions

**For code review tool output transfer**:

1. Open the code review file in CC or read its content
2. Copy the review findings into a Hub Claude conversation
3. Hub Claude judges findings (per CC substantive Codex Plugin Usage canonical processing rules)
4. Hub Claude archives the judgment outcome in the appropriate location (e.g., evidence digest, ADR, or Hub conversation log)

**For CC-internal canonical change notifications**:

1. Detection trigger: the operator inspects the CC `.claude/**` git history at TK boundaries (CC does not carry cross-session awareness of its own canonical changes, and the operator drives detection from the durable git record rather than relying on CC to escalate)
2. Note which CC-internal files changed
3. Inform Hub Claude of the change in conversation
4. Hub Claude updates the Hub-side canonical inventory tracking ([REF] Hub-CD-CC Architecture frames the CC canonical layer structurally; the inventory tracking does not mirror individual files)

**For CC-side DS mirror drift detection notifications** (e.g., SK-F runtime flags a component reference not in the CC mirror, or M0 entry self-check finds the CC mirror stale relative to the latest DS instance version):

1. Durable capture: the CC-runtime drift signal (SK-F runtime, compliance-checker A9, or M0 entry self-check) is written to the slice evidence directory rather than left in the ephemeral CC invocation — a transient CC session output is not relayable on its own
2. The operator reviews the slice evidence at the TK-04 / M4 checkpoint and relays the captured drift signal
3. Note the drift signal (which mirror is behind; which component / token / pattern is involved)
4. Inform Hub Claude in conversation
5. Hub Claude routes the drift through [RULE] DSG §12 update path:
   - If the drift is rooted in a DS instance change that has not yet propagated to the CC mirror: trigger a DS markdown export resync via §2.2 Sub-flow B (DSG §15 review) + §3.1 Sub-flow C (CC-mirror commit)
   - If the drift is rooted in a CC-observed need for a DS change (e.g., implementation reveals a missing token): route the change through DSG §12 additive update flow — captured in the originating feature's UX Design Spec instance §2.4 (or as a new UX Design Spec instance §2.4 entry if the originating feature is in-flight), merged into CD SOT at the originating feature's M4, with the CC mirror re-synced via the reviewed DS markdown export at that boundary

**For ADR-warranting architecture observations**:

1. The operator carries the observation into a Hub Claude conversation
2. Hub Claude assists in authoring an ADR per [TPL] ADR Spec
3. The ADR lands at the canonical ADR location (project-root `specs/adrs/` or app-scoped `apps/{app-slug}/specs/adrs/`)

### 3.2.4 Audit checklist (pre-transfer)

Before transferring, the operator verifies:
- Codex review output is complete (not mid-review)
- CC-internal canonical changes are intentional and reviewed
- DS-related observations are concrete (specific component / token / pattern; specific mirror version metadata)
- ADR-warranting observations are sufficiently concrete to author

### 3.2.5 Hub integration

Codex findings receive Hub judgment and archival. Hub-side canonical inventory tracking is updated for CC-internal canonical changes. DS-related drift signals trigger either DS markdown export resync (when caused by mirror lag) or DSG §12 additive update flow (when caused by DS gap). ADRs are authored and indexed.

**Note on the two-way model**: Hub holds no DS instance mirror per DSG §1.1. CC-side DS drift signals that reveal CC-mirror staleness must be resolved via the DS markdown export mechanism (§2.2 Sub-flow B DSG §15 review + §3.1 Sub-flow C CC-mirror commit) rather than by ad-hoc edits — direct edits to the CC mirror violate DSG §12.6 read-only mirror discipline.

---

# 4. CD ↔ operator ↔ CC path

## 4.1 Research-preview default: decoupled-by-default

During CD research preview, this path operates under decoupled-by-default discipline per [REF] Hub-CD-CC Architecture §9.4. The operator-mediated transfer with explicit audit is the only sanctioned mode of CD ↔ CC content movement.

Direct CD ↔ CC coupling — CD's native "Send to Claude Code" handoff path in its product surface — is **not enabled** for HDC project use during this period; the operator routes all CD → CC content through audited operator-mediated transfer per §4.2. The conditions for re-enabling direct coupling are owned by [REF] Hub-CD-CC Architecture §10; when those conditions are satisfied and an ADR records the re-enablement decision, this source is revised in the same revision to update §4.1.

**DS markdown export flow note**: The DS markdown export generated by CD at change finalization (per DSG §12.7) is reviewed Hub-side and synced to the CC mirror. During research preview, this does NOT execute as direct CD → CC transfer; instead it executes as CD → operator → Hub (the DSG §15 export conformance review, per §2.2 Sub-flow B) and then → CC (per §3.1 Sub-flow C, the CC-mirror commit). The operator is the trust gate.

## 4.2 CD → operator → CC direction

### 4.2.1 What content moves

During research preview, this direction is **rare** because the dominant DS-related CD → CC content (DS markdown export at change finalization) is routed through operator-mediated Hub-session-aware sync per §4.1, not as direct CD → CC.

Remaining flows in this direction (rare):
- Standalone CD design references the operator chooses to make available to CC mid-implementation (e.g., a specific design file image the operator drops directly into a CC session as visual context; this typically happens during TK-04+ implementation when CC asks for visual context on a specific UI question)

Note: The CD-authored phase-level design file for TK-02 Step 2.2 is NOT carried directly to CC. It travels CD → Hub (§2.2 Sub-flow A) for Hub TK-02 Step 2.3 per-feature design file quality check + per-feature UX Design Spec instance authoring, then Hub → CC (§3.1 Sub-flow B) as visual reference accompanying the spec bundle at TK-04 entry. The CD → CC path is reserved for incidental visual reference transfers post-TK-04.

### 4.2.2 Source format

CD content exists as:
- CD project-level artifacts accessible from within CD
- Operator-saved exports (screenshots, PDF, image links)

### 4.2.3 Operator actions

1. Audit the CD content for HDC project relevance (per [REF] Hub-CD-CC Architecture §6 scope boundary)
2. Audit content quality against CC implementation requirements
3. Transfer the content to the CC session:
   - Inline relevant design file image into the CC session conversation (typical mid-implementation case)
   - Or place exports at the operator's working location for CC session reference
4. Note the provenance in CC working state if relevant for traceability

### 4.2.4 Audit checklist (pre-transfer)

Before transferring, the operator verifies:
- Content is HDC-project-scoped (no accidental inclusion of non-HDC CD work)
- Content is appropriate to share inline in the CC session (no security-sensitive content; no operator-personal stakeholder materials)
- The transfer is genuinely needed (the spec bundle at TK-04 entry already carried UX Design Spec instance markdown + design files as visual reference; this incidental transfer is for a specific gap not covered by the bundle)

### 4.2.5 CC reception

CC consumes the inline image / reference as visual context for the specific implementation question. The operator's audit is the trust gate; CC does not treat the inline content as canonical specification (the UX Design Spec instance markdown remains the canonical textual UX source).

---

## 4.3 CC → operator → CD direction

### 4.3.1 When this direction fires (rare)

This direction is rare. It fires when:
- CC code changes have implications for DS visual representation that CD's DS instance SOT should reflect — in this case, the flow is CC → operator → Hub (§3.2 CC DS mirror drift signal) → Hub-routed DSG §12 update → CD authors instance content change → DS markdown export sync (§2.2 Sub-flow B + §3.1 Sub-flow C). The direct CC → CD path in this scenario is supplementary (operator may communicate the implementation observation directly to CD as context for the change authoring), not the primary content carrier
- CC implementation surfaces a UI / interaction concern warranting a revisit of the original CD design files (e.g., a state transition turns out to be infeasible as designed)

### 4.3.2 What content moves

- Implementation-observed visual / interaction issues warranting CD-side revision of design files (when the affected feature is in-flight and the design files are being revised)
- Implementation observations supplementing the DSG §12 flow when CC surfaces a need for DS content change

### 4.3.3 Source format

CC implementation observations exist in informal form:
- Free-form natural-language description by the operator paraphrasing the CC-surfaced issue
- Optional accompanying material: code excerpt, screenshot of running implementation, or reference to a specific test failure

### 4.3.4 Operator actions

1. Note the CC observation
2. If the issue requires DS change: route primarily via §3.2 CC → Hub → DSG §12 flow; secondarily communicate the implementation observation to CD as free-form context
3. If the issue requires design file revision (without DS change): open the phase-level CD session that produced the design file containing the affected feature's slice; communicate the observation as free-form prompt naming the feature-slug; CD may produce a revised design file (typically updating the affected feature's slice in place, preserving labeling for other features); if the affected feature is still pre-TK-02-signoff, the revised design file re-enters §2.2 Sub-flow A for per-feature re-check on the affected slice; if post-signoff, the revision may flow into TK-03 escalation routing per [MECH] DTW §4 TK-03 failure routing

### 4.3.5 Audit checklist (pre-transfer)

Before transferring a CC observation to CD, the operator verifies:
- The observation genuinely warrants CD-side action — distinguish "implementation-level adjustment within current design" (handle inside CC) from "design intent revision needed" (warrants CD revisit)
- The DSG §12 path is not the more appropriate route — DS-content-impacting observations belong on the §3.2 CC → Hub → DSG §12 chain primarily, with CD communication secondary; do not bypass DSG §12 for content that should evolve the DS instance
- The affected feature's TK-02 sign-off status is known — pre-signoff observations re-enter §2.2 Sub-flow A; post-signoff observations route into TK-03 failure handling per [MECH] DTW §4
- The CD session for the affected feature's phase is identifiable — there is one phase-level CD session per phase; the operator selects that session (carrying the current canonical design intent for the entire phase including the affected feature's labeled slice)

### 4.3.6 CD reception

CD treats the operator-communicated CC observation as free-form context, same as any §2.1 Hub → CD transfer.

---

# 5. Reminder form constraints

This source declares **[Enforcement·reminder-only]**: Hub Claude surfaces cross-tool handoff content contracts as reminders rather than mechanically enforcing them. The operator may transfer content that does not meet a contract; the destination's integration is then at the operator's risk. Enforcement is reminder-form because cross-tool transfers are operator-physical actions (copy / paste / attach / save-as-file) that Hub Claude cannot intercept or block; the operator therefore carries the residual risk.

## 5.1 Hub Claude reminder forms

When a Hub Claude conversation initiates or references a cross-tool transfer, Hub Claude:
- Surfaces the relevant content contract from this source's §2 / §3 / §4
- Suggests pre-transfer audit checks per §2.x.4 / §3.x.4 / §4.2.4
- Notes the destination integration steps per §2.x.5 / §3.x.5 / §4.2.5
- Flags scope boundary checks per [REF] Hub-CD-CC Architecture §6 when ambiguity may exist
- For DS-related flows: flags the DSG §12.3 export conformance review (the CD-generated export is reviewed against DSG §15 before the CC mirror is committed)

Reminders are conversational and non-blocking. The operator may proceed without invoking a reminder; the reminder simply surfaces the structure if the operator wants to consult it.

## 5.2 Operator-side fallbacks

If a reminder is missed and a transfer proceeds without the documented audit:
- No automatic recovery — the operator may re-invoke Hub Claude later to re-audit retroactively
- If retroactive audit reveals scope leakage or quality issues, fallback per §6
- For DS markdown export sync: if the CC mirror was committed without the DSG §15 export review having passed, the operator must run the §15 review retroactively and correct the CC mirror if the review finds nonconformance

---

# 6. Audit failure handling

## 6.1 Audit failure types

| Failure type | Description |
|---|---|
| Scope leakage | The transferred content includes non-HDC scope content (per [REF] Hub-CD-CC Architecture §6) |
| Content contract violation | The transferred content lacks expected content (e.g., CD-authored phase-level design file missing per-feature internal labeling for some tier-1-involved feature in the phase, or missing component callouts when those were expected; UX Design Spec instance missing §2.x category coverage; DS markdown export missing DSG §2 section coverage) |
| Quality below threshold | The transferred content meets contract but is judged insufficient for HDC use. This is the **residual category**: where a contract-specific quality rubric applies (CD design files → [TPL] UX Design Spec §3.1 design file quality check; spec artifacts at handoff → the Sign-Off form criteria; DS markdown export → DSG §15 reviewer checklist), judge against that rubric first; "quality below threshold" covers only quality shortfalls no contract-specific rubric already names |
| Integration failure | The destination cannot accommodate the transferred content's structure |
| **Export review skipped** | DS markdown export committed to the CC mirror without passing the DSG §15 export conformance review |

## 6.2 Fallback procedures

For each failure type:

**Scope leakage**:
1. Pause the transfer (or reverse it if already executed)
2. Identify the HDC-scoped portion vs the non-HDC portion
3. Re-transfer only the HDC-scoped portion
4. Document the scope clarification in the relevant conversation log

**Content contract violation**:
1. Determine whether the violation is recoverable (operator can supply the missing content) or requires redo at origin
2. If recoverable: operator supplies the missing content manually at the destination
3. If redo: return to the origin workspace for content re-production
4. **For design file content contract violations at §2.2 Sub-flow A**: route through [TPL] UX Design Spec §3.1 Reject disposition — Step 2.2 redo scope is the affected feature's slice (or full-phase relabeling when per-feature labeling itself is broken)

**Quality below threshold**:
1. Reject the transfer for the current cycle
2. Return to the origin workspace for re-production with revised prompts / inputs
3. Document the quality issue if the failure pattern recurs (may trigger reminder revision in this source)

**Integration failure**:
1. Attempt manual integration (operator types content rather than paste-and-go)
2. If manual integration fails, escalate to Hub Claude for advisory on integration approach
3. Pause the cross-tool flow until integration approach is confirmed

**Export review skipped**:
1. Locate the DS markdown export that was committed to the CC mirror without review — preferred path: the CD-generated export from the originating cycle; fallback path: regenerate the export from CD if the original is lost
2. Run the DSG §15 export conformance review retroactively in a Hub conversation
3. If the review finds nonconformance, return the export to CD for correction and re-sync the CC mirror with the corrected export
4. Verify post-fix: the CC mirror header version matches the reviewed export's declared version
5. If the unreviewed export was discovered downstream (e.g., TK-04 M0 entry self-check or SK-F runtime flagged an inconsistency), additionally verify that no code generated during the window consumed nonconformant DS content

In all failure types, the canonical inventory and spec artifact state remain consistent. Failed transfers leave no partial canonical updates.

---

# 7. Hub Claude soft compliance trigger phrases

## 7.1 Purpose

Hub Claude conversations frequently touch cross-tool handoff topics in informal language. The trigger phrases below activate Hub Claude's cross-tool handoff clarification behavior — surfacing the relevant content contract and audit checklist before proceeding.

Detection is conversational and non-blocking.

Note on disambiguation from application-level handoff: trigger phrases in [MECH] Application Lifecycle Handoff §6 target application-level handoff to human dev team. This source's trigger phrases target cross-tool flows during AI-dev work. Hub Claude routes based on the phrase context — if the phrase implies AI-dev → human dev team, route to [MECH] Application Lifecycle Handoff; if the phrase implies Hub / CD / CC content flow, route here.

## 7.2 Trigger phrases for cross-tool handoff

When a Hub Claude conversation contains any of the following phrases or their close paraphrases (English or Mandarin), Hub Claude pauses and surfaces the relevant content contract:

1. "**take this PRD / TDD / spec to CD**" / "**send to CD**" / "**ask CD to design**" — Hub → CD intent; surface §2.1 content contract (note whether it's Sub-flow A general or Sub-flow B TK-02 Step 2.2)
2. **"start the TK-02 Step 2.2 design file for this phase"** / **"open the CD session for the phase's Tier 1 features"** — explicit Hub → CD Sub-flow B intent; surface §2.1 Sub-flow B content contract specifically (drop files covering all tier-1-involved features in the phase + attention prompt enumerating each feature and instructing per-feature internal labeling; CD grounds DS in its own instance per [REF] Hub-CD-CC Architecture §5.2; one CD session per phase, not per feature)
3. "**bring back from CD**" / "**integrate the prototype / design files**" / "**use the CD output**" — CD → Hub intent; surface §2.2 content contract (note which sub-flow: A design files for Step 2.3, B DS markdown export for mirror sync, or C personal stakeholder material)
4. **"transfer the design file back to Hub"** / **"start Step 2.3 with this design file"** — explicit CD → Hub Sub-flow A intent; surface §2.2 Sub-flow A content contract + [TPL] UX Design Spec §3.1 design file quality check (note: the check is iterated per tier-1-involved feature against that feature's labeled slice within the phase-level design file)
5. **"sync the DS markdown export"** / **"review the DS export"** / **"the DS instance changed, propagate"** — DS markdown export review + sync intent; surface §2.2 Sub-flow B (DSG §15 export conformance review) + §3.1 Sub-flow C (CC-mirror commit) per DSG §12.3
6. "**send to CC**" / "**give CC the spec**" / "**inception sync**" — Hub → CC intent; surface §3.1 content contract (note which sub-flow: A inception, B spec bundle at TK-04, C DS markdown sync, D review reminder, E memos)
7. **"transfer the spec bundle for TK-04"** / **"onboard the assigned_node for this unit"** — explicit Hub → CC Sub-flow B intent; surface §3.1 Sub-flow B content contract + verify UX Design Spec instance markdown is in the transfer set when Tier 1 involved
8. "**copy the Codex review back**" / "**transfer to Hub**" (in CC context) / "**update the canonical**" (after CC change) — CC → Hub intent; surface §3.2 content contract
9. **"CC found a DS mirror inconsistency"** / **"M0 self-check flagged mirror drift"** / **"SK-F can't find this component in the mirror"** — CC DS mirror drift signal; surface §3.2.3 routing (either resync via §2.2 Sub-flow B + §3.1 Sub-flow C, or DSG §12 additive update)
10. "**use the CD design files in CC**" / "**hand the design files to CC mid-implementation**" — CD → CC intent; surface §4.2 content contract and the §4.1 decoupled-by-default discipline (note: this is rare; the normal flow routes through Hub via §2.2 + §3.1)
11. "**send CC's feedback to CD**" / "**update CD with the implementation finding**" — CC → CD intent; surface §4.3 content contract (and note that DS-implicating findings primarily route through §3.2 → DSG §12)
12. "**enable direct CD-to-CC**" / "**skip operator audit**" — direct coupling activation intent; surface §4.1 non-enablement and [REF] Hub-CD-CC Architecture §10 re-enablement conditions
13. **"hand-fix `specs/design-system.md`"** / **"patch the CC DS mirror locally"** — CC-mirror direct-edit intent; surface DSG §12.6 read-only mirror discipline

## 7.3 Action upon detection

On detection, Hub Claude:
1. Names the trigger phrase observed (one sentence)
2. Surfaces the relevant content contract section
3. Suggests the audit checklist relevant to the operator's task
4. If the operator wants to proceed with audit, supports; if the operator wants to skip audit, notes the consequence per §5.2 / §6
5. Continues with substantive advice once the operator's intent is clear

This soft compliance is conversational, not blocking.

---

# 8. Anti-drift red flags

> **Scope**: this section enumerates **cross-tool handoff-specific** anti-drift red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced inline rather than duplicated. See [OS] §12.3 for the full anti-drift red flag ownership map.

**Path discipline dimension**:
- A cross-tool transfer attempted without operator audit (e.g., direct CD ↔ CC coupling during research preview, per §4.1)
- Content moved between workspaces without traversing the operator-mediated path (mechanically infeasible currently, but anti-drift includes any future architectural drift toward direct coupling)
- A cross-tool transfer where the operator skipped the relevant audit checklist (per §5.2, this is allowed but creates failure-mode exposure per §6)

**Content contract dimension**:
- **CD-authored phase-level design file transferred to Hub at §2.2 Sub-flow A without applying [TPL] UX Design Spec §3.1 design file quality check per tier-1-involved feature** (skipping the quality check at Step 2.3 entry causes downstream UX Design Spec instance authoring to proceed on potentially insufficient grounding material)
- **Phase-level design file transferred without per-feature internal labeling** — Hub Step 2.3 cannot ground per-feature UX Design Spec instances without the labels; route through §6 fallback for CD to add labeling before Step 2.3 proceeds
- **Hub-authored UX Design Spec instance markdown transferred to CC at §3.1 Sub-flow B without applying [TPL] UX Design Spec §3.2 authoring quality check** (skipping the authoring check before TK-02 sign-off causes downstream TK-03 / TK-04 to consume potentially ungrounded UX content)
- Hub canonical inventory tracking not updated after CC-internal canonical changes (per §3.2.3)
- Codex review output bypasses Hub judgment (per §3.2.3)

**DS two-way distribution dimension**:
- **DS markdown export committed to the CC mirror without the DSG §15 export conformance review** — violates DSG §12.3; route through §6.2 export-review-skipped handling
- **Direct edits to the CC mirror** (`specs/design-system.md`) — violates DSG §12.6 read-only mirror discipline; the CC mirror is exclusively updated via the reviewed CD-generated DS markdown export
- **CC DS mirror drift signal from M0 entry self-check or SK-F runtime ignored** — the drift signal must route through §3.2.3 to either trigger a resync or a DSG §12 additive update; ignoring causes downstream code generation to consume inconsistent DS reference
- **DS markdown export generated at a non-DSG-§12.5 boundary** (e.g., mid-slice export attempted) — exports only generate at the originating feature's M4 → merge-to-main milestone; off-cycle exports create floating-version CC-mirror state
- **A Hub-side DS instance mirror re-introduced** — the two-way model holds no DS instance copy at Hub; re-introducing a Hub DS mirror is drift back toward the retired three-way model (per DSG §16)

**Scope boundary dimension**:
- Cross-tool transfers carrying non-HDC scope content (per [REF] Hub-CD-CC Architecture §6)
- CD instance setup materials (Figma uploads, brand notes) treated as Hub canonical content
- Operator-personal CD output (e.g., stakeholder deck for personal use, per §2.2 Sub-flow C) integrated into Hub spec artifacts

**Audit failure dimension**:
- Failed transfers not handled per §6 fallback procedures (e.g., partial canonical updates left in place after integration failure)
- Quality-failure transfers repeated without root-cause analysis (recurring quality failure may indicate the content contract or origin workspace process needs revision)
- **CD design file quality check `Reject` disposition recurring for the same feature's slice** — likely indicates the attention prompt's per-feature section at §2.1 Sub-flow B was insufficient, or the PRD/TDD drop-file content for that feature lacked enough context for CD; investigate Step 2.2 entry mechanics for that feature's portion of the phase-level transfer

**Reminder discipline dimension**:
- Hub Claude advises on a cross-tool transfer without invoking §7.2 trigger phrase check
- Operator and Hub Claude proceed past a §7.2 trigger without surfacing the relevant content contract (§7.3 step 2)

**Direct coupling dimension**:
- Direct CD ↔ CC coupling attempted while CD is in research preview (violates §4.1)
- Direct coupling re-enabled without [REF] Hub-CD-CC Architecture §10 prerequisites all satisfied and recorded in an ADR

**Path-flow misrouting dimension** (new with revised architecture):
- **CD-authored phase-level design file routed directly to CC at TK-02 Step 2.2 exit** (bypassing the Hub TK-02 Step 2.3 per-feature quality check + per-feature UX Design Spec instance authoring) — the design file must route CD → Hub → CC, not CD → CC directly
- **CD attempts to deliver one design file per feature instead of one design file per phase** — the canonical CD delivery unit is phase-level (covering all tier-1-involved features in the phase as labeled internal scopes); per-feature delivery contradicts CD's natural by-phase design workflow and fragments the Step 2.3 grounding model
- **UX Design Spec instance authored at CC instead of Hub** — the UX Design Spec instance is Hub-authored per [REF] Hub-CD-CC Architecture §5.2 revised; CC consumes but does not author
- **CD attempting to author the UX Design Spec instance markdown** — CD outputs design files (visual artifacts); the markdown counterpart is a Hub-authored deliverable per [TPL] UX Design Spec
