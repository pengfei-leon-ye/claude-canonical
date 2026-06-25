# [MECH] Cross-Tool Workflow Handoff

- **Project**: HR Digital Cockpit
- **Document Type**: Workflow Orchestration Specification
- **Status**: Active canonical
- **Role**: Stable source defining the content contracts for the three operator-mediated cross-tool handoff paths during AI-dev work (Hub ↔ operator ↔ CD, Hub ↔ operator ↔ CC, CD ↔ operator ↔ CC) — including what content moves in each direction, operator transfer actions, audit steps, integration steps, reminder-form discipline, the on-demand visual path that seeds a CD design file only on genuine visual novelty (CC pushes PRD/TDD text into the CD project's `uploads/`; operator designs in CD UI; CC pulls the design file back), and the DS markdown export review-and-sync mechanism that maintains the CC DS mirror
- **Source Category**: Cat 4
- **Management-System Role**: Workflow orchestration specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; conversation discipline rules in [OS] §7.2 apply to the Hub Claude trigger behavior in §7. Cross-source ownership map for the Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control).
- **Relationship to [REF] Hub-CD-CC Architecture**: Operationalizes. [REF] Hub-CD-CC Architecture §9 declares the three-path handoff topology, and §9.4 declares the decoupled-by-default discipline during CD research preview; §3.4.1 declares CD outputs design files (CD-native visual artifacts) on the on-demand visual path; §5.2 declares the two-way DS distribution model (CD = SOT / CC = code-time mirror). The [REF] §1.1 surface map assigns detailed-spec authoring (UX-spec synthesis + intent/acceptance/test-plan) to CC in sessions firewalled from the implementing context, and makes CD's app-level visual producer role **default-retired** — re-entered on-demand only on genuine visual novelty (a new design token / new visual language). This source defines the concrete content contracts and operator actions that realize those paths.
- **Relationship to [MECH] Application Lifecycle Handoff**: Distinct lifecycle layer. [MECH] Application Lifecycle Handoff governs the application-level handoff event (AI-dev → human dev team, terminal). This source governs cross-tool content flows during AI-dev work (recurrent during the entire AI-dev period). Both reference operator-mediated discipline but at different boundaries.
- **Relationship to [RULE] Design System Governance**: Anchored. DSG §1.1 owns the two-way distribution model — CD = SOT at the CD workspace, CC = code-time mirror at `specs/design-system.md`. This source operationalizes the cross-tool content flows that maintain that model:
  - CD-authored **design files** are produced only on the on-demand visual path (genuine visual novelty — a new design token / new visual language). On that path CC pushes the feature's PRD/TDD text into the CD project's `uploads/` (§4.3), the operator designs in CD UI, and CC pulls the design file back (§4.2) as visual reference informing code — they do not flow CD → Hub for spec authoring
  - CD-authored **DS markdown export** flows CD → Hub (DSG §15 export conformance review) → CC mirror at change finalization (per DSG §12.3 + §12.7)
  - **UX Design Spec instance markdowns** (UX-spec synthesis) are **CC-authored** in a session firewalled from the implementing context (the relocated TK-02 Step 2.3 synthesis), produced in-repo at `apps/{app-slug}/specs/ux-design-spec/**`; they are not Hub-authored and not Hub → CC transferred
  - The two-way distribution generates DS-related cross-tool flows in the Hub ↔ CD and Hub ↔ CC handoff paths; cross-tool flows that carry DS-related content apply DSG rules accordingly. DSG §12 additive update path drives DS instance changes at the originating feature's M4 → merge-to-main milestone, at which point the reviewed DS markdown export syncs to the CC mirror
- **Relationship to [RULE] Codex Plugin Usage**: **Migrated to CC substantive canonical (Phase 3)**. The CC → operator → Hub direction in §3.2 includes code review tool output flow; the specific code review tool (historically Codex) is governed by CC substantive Codex Plugin Usage canonical at CC. This source declares only the cross-workspace content contract; the fire-condition and output-processing rules live at CC.
- **Relationship to [RULE] Workspace Topology**: Anchored. Workspace inception governance follows [RULE] Workspace Topology constitutional residue §5; the specific Hub canonical access mechanism at CC is operator-personal infrastructure (declared substantively in §3.1.1). Hub-to-assigned_node onboarding mechanics referenced from §3.1 follow CC substantive Workspace Topology canonical (node-assignment 4-step procedure step 4).
- **Relationship to [MECH] Development Track Workflow**: Cross-tool handoffs operate continuously during AI-dev work driven by DTW TK sequence. This source does not author TK orchestration but provides the content contracts that DTW TKs invoke when they touch cross-tool flows. Key TK-bound flows:
  - On-demand visual path (only on genuine visual novelty): CC → CD push of the feature's PRD/TDD text into the CD project's `uploads/` via MCP write (§4.3), then CD → CC pull of the resulting design file via MCP read (§4.2)
  - TK-03 → TK-04 entry: Hub → CC spec bundle = upstream content (PRD / TDD main + phase test plans + slice-lists + OpenAPI) (§3.1). UX-spec synthesis and per-slice intent/acceptance/test-plan are CC-authored in firewalled sessions, not part of the Hub-delivered bundle
  - TK-11 code review tool output → Hub: CC → Hub (§3.2; specific tool governed by CC substantive canonical)
  - TK-12 DS change finalization (when applicable): DS markdown export §15 review + sync to the CC mirror (§2.2 + §3.1, operator-mediated)
- **Relationship to [TPL] UX Design Spec**: Cross-references. UX Design Spec instances at two granularities (phase-level + per-feature) are **CC-authored** in a firewalled synthesis session (the `ux-spec-synthesizer` role, the relocated TK-02 Step 2.3 synthesis), per [TPL] UX Design Spec. When the on-demand visual path fires, the CD-authored design file pulled back via §4.2 is the visual reference grounding that synthesis; on the default path (no visual novelty) the synthesis grounds directly on the PRD/TDD. The instances are produced in-repo by CC, not transferred Hub → CC.
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

The CD ↔ CC path operates under decoupled-by-default discipline during CD research preview (§4.1). On this path runs the **on-demand visual loop** (only on genuine visual novelty): CC → CD seeds a design by pushing the feature's PRD/TDD text into the CD project's `uploads/` (§4.3), and CD → CC returns the resulting design file (§4.2) — both directions remain operator-mediated. The Hub ↔ CD and Hub ↔ CC paths operate continuously throughout AI-dev work.

## 1.2 Operator-mediated discipline

All cross-tool flows require explicit operator action. No workspace can push content to another workspace autonomously. No workspace has read access to another workspace's session state. Each transfer involves:

1. **Origin produces content** (Hub authors PRD / TDD, CC synthesizes the UX-spec and writes code, CD produces a design file on the on-demand visual path, etc.)
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

**Sub-flow B — On-demand visual-path context (HDC-specific, rare)**: CD app-level visual production is **default-retired**; it is **not** triggered per-phase by `tier_1_involved`. A CD design file is produced only on the **on-demand visual path** — entered solely on genuine visual novelty, operationally proxied by "needs a new design token / new visual language" (NOT interaction / IA / component complexity, which CC handles directly plus meta-DS registration). On that path the design seed travels **CC → CD** (CC pushes the feature's PRD/TDD text into the CD project's `uploads/` via MCP write, per §4.3 — the operator then designs in CD UI), so this Hub → CD direction no longer carries a standing per-phase design-file kickoff. The only residual Hub → CD content on the visual path is operator-discretion supplementary framing (strategic context, brand / design preferences) the operator chooses to add into the same CD session, transferred per Sub-flow A general-context mechanics.

**Sub-flow C — DS instance authoring input (HDC-specific, when a DS change is needed)**: When a DS instance change has been approved per [RULE] DSG §12, the operator initiates a CD session for CD-side DS instance authoring. The content transferred:
- The current `[RULE] Design System Governance` text — transferred to CD as a **read-only input** so CD authors the DS instance change in conformance with DSG §2-§11 and self-checks the change before generating the DS markdown export. DSG's SOT remains at Hub; CD receives it as a transferred input, not as owned content
- The specific change request — the additive change plan (the originating feature's CC-authored per-feature UX Design Spec instance §2B.4 entry; cross-cutting additives additionally indexed in the phase-level instance §2A.6) or, for a breaking change, the change requirements + rationale traceable to the triggering feature's PRD/TDD

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

For Sub-flow B (on-demand visual-path context):

1. Confirm the on-demand visual path is genuinely warranted — the feature needs a **new design token / new visual language** (NOT interaction / IA / component complexity, which CC handles directly). Absent visual novelty, no CD design file is produced and this sub-flow does not fire
2. The design seed is delivered **CC → CD** per §4.3 (CC pushes the feature's PRD/TDD text into the CD project's `uploads/` via MCP write); the operator does not re-transfer PRD/TDD here
3. Confirm the CD project's DS instance is linked (CD's own DS SOT per [REF] Hub-CD-CC Architecture §5.2; no per-cycle DS transfer needed)
4. The operator designs the screen(s) in CD UI (human-driven), grounded on the seeded PRD/TDD text and the linked DS instance
5. Optionally add supplementary framing (strategic context, brand / design preferences) as free-form CD prompt — this is the only Hub → CD content on the visual path
6. CC pulls the resulting design file back via §4.2 and consumes it as visual reference informing code; the UX-spec synthesis that grounds on it is CC-authored (firewalled `ux-spec-synthesizer` session), not Hub-authored

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
- **For Sub-flow B (on-demand visual path)**: the visual-novelty trigger is genuine — a **new design token / new visual language** is needed (not interaction / IA / component complexity, which CC handles directly + meta-DS registration); the PRD/TDD seed has been delivered into the CD project's `uploads/` via §4.3 (CC → CD MCP write); the CD project's DS instance is linked; any supplementary framing the operator adds is coherent without its original document context

### 2.1.5 CD reception

CD receives all Hub content as **free-form context**, not structured spec. CD does not parse PRD sections, TDD chapters, or IA structures programmatically. The operator's responsibility is to extract and frame the content so CD can use it. For Sub-flow B, the seeded PRD/TDD text in `uploads/` (delivered CC → CD per §4.3) plus any operator-added framing act as the operator's design reference; the design file the operator produces in CD UI on the on-demand visual path is a CD-native visual artifact per [REF] Hub-CD-CC Architecture §3.4.1, pulled back to CC via §4.2.

---

## 2.2 CD → operator → Hub direction

### 2.2.1 What content moves

This direction carries CD-produced content back into Hub. Two distinct sub-flows exist (the design file itself no longer routes through Hub — on the on-demand visual path it returns directly to CC via §4.2, since UX-spec synthesis is CC-authored, not Hub-authored):

**Sub-flow B — DS markdown export review at change finalization (when applicable)**: When a DS change merges at the originating feature's M4 → merge-to-main milestone (per DSG §12.5), CD generates an updated DS markdown export per DSG §12.7. The operator brings the export into the Hub session, where Hub Claude reviews it against the DSG §15 reviewer checklist (the export conformance review per DSG §12.3). On a passing review, the export is committed to the CC mirror (`specs/design-system.md`) — the §3.1 Sub-flow C transfer. Hub retains no copy of the export.

**Sub-flow C — Stakeholder review materials**: Slide decks, prototypes, and other CD outputs for the operator's own use (e.g., presenting to stakeholders) — not integrated into Hub canonical.

### 2.2.2 Source format

CD content exists as:
- CD-generated DS markdown export at change finalization (text-formatted markdown per DSG §12.7 specification)
- CD project-level descriptions / notes
- CD DS instance state (visible to the operator within CD)

(CD-authored design files produced on the on-demand visual path do not travel CD → Hub; they return directly to CC via §4.2.)

### 2.2.3 Operator actions

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

**For Sub-flow B**:
- DS markdown export is complete (covers all DSG §2 section topics) and current (reflects the just-merged DS change)
- The export has passed the DSG §15 conformance review before the CC mirror is committed
- The CC mirror path is writable and not in a stale-snapshot state

### 2.2.5 Hub integration

(UX Design Spec instance authoring no longer occurs at Hub — UX-spec synthesis is CC-authored in a firewalled `ux-spec-synthesizer` session, the relocated TK-02 Step 2.3 synthesis. The on-demand design file is CC's visual reference and never routes through Hub.)

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

**Sub-flow B — Upstream-content transfer at TK-03 → TK-04 entry**: Hub-authored **upstream content** transferred to the assigned_node working directory at TK-04 entry (or at hub-to-assigned_node onboarding when the unit starts). The Hub-delivered bundle is the upstream / slow / coherence-anchor layer (PRD / TDD); the detailed-spec layer (UX-spec synthesis + per-slice intent/acceptance/test-plan) is **CC-authored in firewalled sessions**, produced in-repo, and is NOT part of this Hub → CC transfer. Content carried:
- PRD main (TK-01 output)
- TDD main (TK-02 Step 2.1 output)
- Phase test plan master (TK-02 Step 2.1 output)
- Feature integration test plans (TK-02 Step 2.1 outputs)
- Per-feature slice-lists (TK-02 Step 2.1 outputs)
- App-scoped OpenAPI (TK-02 Step 2.1 output)
- ADRs (operator-curated, when applicable)

Not in this bundle (CC-authored in-repo, not Hub-delivered):
- **UX Design Spec instance markdowns** (phase-level + per-feature) — authored by CC's firewalled `ux-spec-synthesizer` session (the relocated TK-02 Step 2.3 synthesis) at `apps/{app-slug}/specs/ux-design-spec/**`
- **Per-slice intent / acceptance / test-plan** — authored by CC's firewalled acceptance/intent session (the relocated TK-03), just-ahead-of-code per increment
- **CD-authored design file** — produced only on the on-demand visual path (genuine visual novelty); when present, CC pulls it directly from CD via §4.2 (CC ← CD MCP read) as visual reference, not via a Hub → CC transfer

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
2. When Hub canonical evolves (a new commit lands in the Hub canonical repository's project-knowledge folder), the operator refreshes CC's access via the operator's chosen refresh mechanism for the access method established at step 1
3. CC contract: Hub canonical is read-only at CC; CC does not modify Hub canonical at its origin

**For Sub-flow B — upstream-content transfer at TK-03 → TK-04 entry**:

1. Place the Hub-authored **upstream content** at the canonical paths in the monorepo per the repository layout owned by the CC-side substantive Claude Code Architecture Rules canonical (e.g., `apps/{app-slug}/specs/prd/phase-{N}.md`, `apps/{app-slug}/specs/tdd/phase-{N}.md`, plus phase test plans, slice-lists, and OpenAPI). The UX Design Spec instances and per-slice intent/acceptance/test-plan are NOT placed here by the operator — CC authors them in-repo in firewalled sessions
2. Commit on the appropriate branch per [RULE] Workspace Topology §5
3. The upstream content is read by CC from the working directory when relevant TKs execute; CC's firewalled sessions then author the detailed spec grounded on it
4. On the on-demand visual path (genuine visual novelty), CC pulls the CD design file directly via §4.2 (CC ← CD MCP read); no operator-mediated Hub → CC design-file transfer is involved

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
- **For TK-04 entry (Sub-flow B)**: the upstream content (PRD / TDD main + phase test plans + slice-lists + OpenAPI) is at sign-off form and at the canonical paths. The UX Design Spec instances are NOT expected in this Hub-delivered set — they are CC-authored in-repo by the firewalled `ux-spec-synthesizer` session; their grounding against the CC DS mirror via SK-F is validated within CC's own authoring + TK-04 M0 entry self-check, not as a Hub-transfer audit
- **For DS markdown export sync (Sub-flow C)**: the export has passed the DSG §15 conformance review (§2.2 Sub-flow B) before the CC mirror is committed

### 3.1.5 CC reception

CC reads canonical via the inception-sync snapshot. CC reads spec via monorepo file paths. CC does not maintain a parallel Hub-canonical-mirror copy (per [OS] §1.4 visibility boundary).

The UX Design Spec instance markdowns (phase-level + per-feature) are **CC-authored** in the firewalled `ux-spec-synthesizer` session, not Hub-delivered; CC's TK-04 M0 entry self-check verifies the authored markdowns' component / token / pattern references against the CC DS mirror via SK-F per [MECH] DTW §4 TK-04 mechanism. On the on-demand visual path, the CD design file CC pulled back (§4.2) is visual reference grounding the synthesis; design files are not parsed programmatically by CC. The operator may also share specific design file images inline in the CC session when CC needs visual context for a specific implementation question.

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
   - If the drift is rooted in a CC-observed need for a DS change (e.g., implementation reveals a missing token): route the change through DSG §12 additive update flow — captured in the originating per-feature UX Design Spec instance §2B.4 (or as a new §2B.4 entry if the originating feature is in-flight); cross-cutting additives additionally indexed in the phase-level UX Design Spec instance §2A.6; merged into CD SOT at the originating feature's M4, with the CC mirror re-synced via the reviewed DS markdown export at that boundary

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

**Transport modernization ≠ re-enablement.** Executing the Flow B DS-mirror sync's *transport* via the DesignSync MCP read-half (below) is **not** a re-enablement of this section's decoupled-by-default discipline: the operator stays the mediating node (the DSG §15 review gates; the fetch is authorized only post-review). Re-enablement per §4.1 / [REF] §10 means *removing* operator mediation, which this does not. See [REF] Hub-CD-CC Architecture §10.5.

**DS markdown export flow note**: The DS markdown export generated by CD at change finalization (per DSG §12.7) is reviewed Hub-side and synced to the CC mirror. This executes as CD → operator → Hub (the DSG §15 export conformance review, per §2.2 Sub-flow B) and then → CC (per §3.1 Sub-flow C, the CC-mirror commit); the operator is the trust gate. The final → CC transport MAY be manual or, as a transport modernization, the **DesignSync MCP read-half** under operator authorization (review-then-fetch; mechanics in DSG §12.7) — transport-within-mediation, not direct CD → CC coupling.

## 4.2 CD → operator → CC direction

### 4.2.1 What content moves

During research preview, this direction carries CD design output back to CC. The dominant DS-related CD → CC content (DS markdown export at change finalization) is routed through operator-mediated Hub-session-aware sync per §4.1, not as direct CD → CC. The substantive CD → CC content is the **on-demand visual-path design file**:
- **On-demand design-file return**: When the on-demand visual path has fired (CC seeded the design via §4.3, the operator designed in CD UI), CC pulls the resulting design file back from the CD project via DesignSync MCP read (`get_file` / `list_files`) under operator authorization, and consumes it as visual reference informing code. This is the ④ step of the on-demand loop (§4.3.1)
- **Standalone CD design references** the operator chooses to make available to CC mid-implementation (e.g., a specific design file image the operator drops directly into a CC session as visual context; this typically happens during TK-04+ implementation when CC asks for visual context on a specific UI question)

Note: There is no standing per-phase CD design file. A CD design file exists only when the on-demand visual path has fired; when it exists, it returns **directly to CC** (CC ← CD MCP read above), not routed through Hub — UX-spec synthesis is CC-authored, so the design file is CC's visual reference, never Hub's authoring input.

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
- The transfer is genuinely needed: for the on-demand design-file return, the on-demand visual path has genuinely fired (a new design token / new visual language was needed) and CC seeded it via §4.3; for an incidental visual reference, it covers a specific gap CC's own CC-authored UX Design Spec instances do not address

### 4.2.5 CC reception

CC consumes the inline image / reference as visual context for the specific implementation question. The operator's audit is the trust gate; CC does not treat the inline content as canonical specification (the **CC-authored** UX Design Spec instance markdowns — phase-level + per-feature, produced by the firewalled `ux-spec-synthesizer` session — remain the canonical textual UX source).

---

## 4.3 CC → operator → CD direction

### 4.3.1 When this direction fires

This direction carries CC-produced content to CD. Its primary, **first-class** sub-flow is the on-demand visual-path seed; two supplementary triggers remain rare.

**Primary sub-flow — on-demand visual-path seed (CC → CD `uploads/` MCP write)**: Fires when the on-demand visual path is entered — i.e., a feature needs a **new design token / new visual language** (genuine visual novelty; NOT interaction / IA / component complexity, which CC handles directly + meta-DS registration). The DesignSync MCP is pure file I/O and cannot make CD *generate*, so the path is human-driven through a four-step loop:

> ① CC pushes the feature's PRD/TDD text into the CD project's `uploads/` via DesignSync MCP write (`write_files` into an existing CD PROJECT-type project) → ② the **operator designs in CD UI (human-driven)** → ③ CC pulls the resulting design file back via MCP read (§4.2 on-demand design-file return) → ④ CC consumes it as visual reference informing code, grounding the firewalled `ux-spec-synthesizer` synthesis.

CC writes only **text spec inputs** (PRD/TDD) into `uploads/` — never design-output bytes (that would make CC the producer, violating "design output = CD") and never an invocation that asks CD to generate. The meta-DS SOT write fence (DSG §12.1 / §12.6 propose-not-write; the DesignSync write-half is never aimed at the DS SOT) is UNCHANGED.

**Supplementary triggers (rare)**:
- CC code changes have implications for DS visual representation that CD's DS instance SOT should reflect — in this case, the flow is CC → operator → Hub (§3.2 CC DS mirror drift signal) → Hub-routed DSG §12 update → CD authors instance content change → DS markdown export sync (§2.2 Sub-flow B + §3.1 Sub-flow C). The direct CC → CD path in this scenario is supplementary (operator may communicate the implementation observation directly to CD as context for the change authoring), not the primary content carrier
- CC implementation surfaces a UI / interaction concern warranting a revisit of a design file produced earlier on the on-demand path (e.g., a state transition turns out to be infeasible as designed)

### 4.3.2 What content moves

- **On-demand visual-path seed (primary)**: the feature's **PRD/TDD text** delivered into the CD project's `uploads/` via DesignSync MCP write — the text spec inputs that the operator designs against in CD UI. NOT design-output bytes, NOT a generate invocation
- Implementation-observed visual / interaction issues warranting CD-side revision of a design file produced earlier on the on-demand path (when the affected feature is in-flight and that design file is being revised)
- Implementation observations supplementing the DSG §12 flow when CC surfaces a need for DS content change

### 4.3.3 Source format

- **On-demand visual-path seed**: structured text spec inputs (the feature's PRD/TDD text) written into the CD project's `uploads/` via the DesignSync MCP write-half (`write_files` against an existing CD PROJECT-type project) — a file-I/O transport, not an operator paraphrase. The meta-DS SOT remains write-fenced; the write targets the app-level CD project's `uploads/`, never the DS SOT
- **Supplementary implementation observations** exist in informal form: free-form natural-language description by the operator paraphrasing the CC-surfaced issue; optional accompanying material — code excerpt, screenshot of running implementation, or reference to a specific test failure

### 4.3.4 Operator actions

**For the on-demand visual-path seed (primary)**:

1. Confirm the on-demand visual path is genuinely warranted (a new design token / new visual language is needed) — absent visual novelty, CC produces Arco-React directly and no CD seed is written
2. CC writes the feature's PRD/TDD text into the CD project's `uploads/` via DesignSync MCP write under operator authorization (the CD project is an existing PROJECT-type project; if one does not yet exist the operator creates the app-level CD project, since `create_project` creates only DESIGN_SYSTEM type — the app-level project is operator-created)
3. The operator opens that CD project and **designs the screen(s) in CD UI (human-driven)**, grounded on the seeded PRD/TDD text and the linked DS instance
4. CC pulls the resulting design file back via §4.2 (CC ← CD MCP read) and consumes it as visual reference; the firewalled `ux-spec-synthesizer` session grounds its synthesis on it

**For supplementary implementation observations**:

1. Note the CC observation
2. If the issue requires DS change: route primarily via §3.2 CC → Hub → DSG §12 flow; secondarily communicate the implementation observation to CD as free-form context
3. If the issue requires revision of a design file produced earlier on the on-demand path (without DS change): open the CD project that produced that design file; communicate the observation as free-form prompt naming the feature-slug; the operator revises the design in CD UI; CC re-pulls the revised design file via §4.2. The detailed-spec re-author that follows (UX-spec synthesis and per-slice intent/acceptance) runs in CC's firewalled sessions per the incremental JIT model, under operator authorization — not at Hub

### 4.3.5 Audit checklist (pre-transfer)

Before transferring CC content to CD, the operator verifies:
- **For the on-demand visual-path seed**: the visual-novelty trigger is genuine (a new design token / new visual language is needed, not interaction / IA / component complexity); the MCP write targets the app-level CD project's `uploads/` and carries only PRD/TDD text spec inputs (no design-output bytes; not the DS SOT); the target CD PROJECT-type project exists (or the operator has created it)
- The observation genuinely warrants CD-side action — distinguish "implementation-level adjustment within current design" (handle inside CC) from "design intent revision needed" (warrants CD revisit)
- The DSG §12 path is not the more appropriate route — DS-content-impacting observations belong on the §3.2 CC → Hub → DSG §12 chain primarily, with CD communication secondary; do not bypass DSG §12 for content that should evolve the DS instance
- For a revision of an existing on-demand design file, the CD project that produced it is identifiable — a CD design file (and its project) exists only because the on-demand visual path fired for that feature; there is no standing per-phase CD session to select

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
| Content contract violation | The transferred content lacks expected content (e.g., on-demand visual-path seed missing the feature's PRD/TDD text inputs in `uploads/`, or an on-demand CD design file lacking the visual coverage CC needs as reference; DS markdown export missing DSG §2 section coverage). UX Design Spec instance coverage (§2A.x / §2B.x) is a **CC-authored**-artifact quality concern checked within CC's `ux-spec-synthesizer` session, not a cross-tool transfer violation |
| Quality below threshold | The transferred content meets contract but is judged insufficient for HDC use. This is the **residual category**: where a contract-specific quality rubric applies (upstream spec artifacts at handoff → the Sign-Off form criteria; DS markdown export → DSG §15 reviewer checklist; an on-demand CD design file → the visual-reference adequacy CC needs to ground its synthesis), judge against that rubric first; "quality below threshold" covers only quality shortfalls no contract-specific rubric already names |
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
4. **For an on-demand CD design file that is inadequate as visual reference**: the operator re-enters the on-demand visual loop (§4.3.4) — refine the seeded PRD/TDD text in `uploads/` and/or the CD-UI design, then CC re-pulls the revised design file via §4.2. There is no per-phase cross-cutting / per-feature-labeling redo, since app-level CD design is on-demand per feature's visual novelty, not a standing per-phase deliverable

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

1. "**take this PRD / TDD / spec to CD**" / "**send to CD**" / "**ask CD to design**" — Hub → CD intent; surface §2.1 content contract (note whether it's Sub-flow A general-context or Sub-flow B on-demand visual-path supplementary framing; the on-demand seed itself is the CC → CD §4.3 push, not a Hub → CD transfer)
2. **"this feature needs a new design token / new visual language"** / **"enter the on-demand visual path for this feature"** / **"seed a CD design for this feature"** — on-demand visual-path intent; surface §4.3.1 primary sub-flow (the ①-④ loop: CC pushes PRD/TDD text into the CD project's `uploads/` via MCP write → operator designs in CD UI → CC pulls the design file back via §4.2 → CC consumes as visual reference) and confirm the trigger is genuine visual novelty (NOT interaction / IA / component complexity, which CC handles directly + meta-DS registration). App-level CD design is default-retired; there is no automatic per-phase Step 2.2 design-file kickoff
3. "**bring back from CD**" / "**integrate the prototype / design files**" / "**use the CD output**" — CD → Hub intent; surface §2.2 content contract (note which sub-flow: B DS markdown export for mirror sync, or C personal stakeholder material). An on-demand design file does NOT come back to Hub — it returns directly to CC via §4.2
4. **"pull the design file back to CC"** / **"the CD design is ready, bring it into implementation"** — on-demand design-file return intent; surface §4.2 on-demand design-file return (CC ← CD MCP read) + note that UX-spec synthesis grounding on it is CC-authored in the firewalled `ux-spec-synthesizer` session, NOT Hub-authored. The design file returns directly to CC, never routed through Hub for Step 2.3 authoring (synthesis is relocated to CC)
5. **"sync the DS markdown export"** / **"review the DS export"** / **"the DS instance changed, propagate"** — DS markdown export review + sync intent; surface §2.2 Sub-flow B (DSG §15 export conformance review) + §3.1 Sub-flow C (CC-mirror commit) per DSG §12.3
6. "**send to CC**" / "**give CC the spec**" / "**inception sync**" — Hub → CC intent; surface §3.1 content contract (note which sub-flow: A inception, B spec bundle at TK-04, C DS markdown sync, D review reminder, E memos)
7. **"transfer the upstream content for TK-04"** / **"onboard the assigned_node for this unit"** — explicit Hub → CC Sub-flow B intent; surface §3.1 Sub-flow B content contract (PRD / TDD main + phase test plans + slice-lists + OpenAPI). Note that UX Design Spec instances and per-slice intent/acceptance/test-plan are CC-authored in firewalled sessions in-repo — they are NOT expected in the Hub-delivered bundle, so do not verify them as part of the transfer set
8. "**copy the Codex review back**" / "**transfer to Hub**" (in CC context) / "**update the canonical**" (after CC change) — CC → Hub intent; surface §3.2 content contract
9. **"CC found a DS mirror inconsistency"** / **"M0 self-check flagged mirror drift"** / **"SK-F can't find this component in the mirror"** — CC DS mirror drift signal; surface §3.2.3 routing (either resync via §2.2 Sub-flow B + §3.1 Sub-flow C, or DSG §12 additive update)
10. "**use the CD design file in CC**" / "**hand the design file to CC mid-implementation**" — CD → CC intent; surface §4.2 content contract and the §4.1 decoupled-by-default discipline. Note: there is no standing mandatory design file; a design file exists only when the on-demand visual path fired, and on that path CC pulls it directly via §4.2 (CC ← CD MCP read) — it does NOT route through Hub
11. "**send CC's feedback to CD**" / "**update CD with the implementation finding**" / "**push the spec inputs into the CD project**" — CC → CD intent; surface §4.3 content contract — the primary sub-flow is the on-demand visual-path seed (CC pushes PRD/TDD text into the CD project's `uploads/` via MCP write, §4.3.1), supplementary triggers are implementation findings (note that DS-implicating findings primarily route through §3.2 → DSG §12)
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
- **On-demand visual-path seed that writes design-output bytes (or a generate invocation) into the CD project instead of PRD/TDD text inputs** — CC delivers only text spec inputs into `uploads/`; writing design output makes CC the producer (violates "design output = CD"), and there is no MCP method to make CD generate
- **An on-demand CD design file pulled into CC as visual reference without CC's `ux-spec-synthesizer` session applying its synthesis quality checks** (consuming the visual reference without the firewalled synthesis grounding it causes downstream code to proceed on ungrounded UX content)
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
- **An on-demand CD design file repeatedly inadequate as visual reference for the same feature** — likely indicates the PRD/TDD text seeded into the CD project's `uploads/` (§4.3) lacked enough context for the operator's CD-UI design, or the visual-novelty trigger was mis-scoped (interaction / IA complexity that CC should handle directly rather than a genuine new-token need); investigate the §4.3 seed content and the trigger judgment

**Reminder discipline dimension**:
- Hub Claude advises on a cross-tool transfer without invoking §7.2 trigger phrase check
- Operator and Hub Claude proceed past a §7.2 trigger without surfacing the relevant content contract (§7.3 step 2)

**Direct coupling dimension**:
- Direct CD ↔ CC coupling attempted while CD is in research preview (violates §4.1)
- Direct coupling re-enabled without [REF] Hub-CD-CC Architecture §10 prerequisites all satisfied and recorded in an ADR

**Path-flow misrouting dimension** (new with revised architecture):
- **An app-level CD design file produced without a genuine visual-novelty trigger** — app-level CD visual is default-retired; a design file is produced only on the on-demand path (a new design token / new visual language). Producing one for interaction / IA / component complexity (which CC handles directly + meta-DS registration) is drift back toward the retired per-phase mandatory-design-file model
- **An on-demand CD design file routed through Hub instead of returning directly to CC** — UX-spec synthesis is CC-authored; the design file is CC's visual reference and returns CC ← CD via §4.2, never CD → Hub for authoring
- **UX Design Spec instance authored at Hub instead of CC** — both UX Design Spec instance types (phase-level + per-feature) are CC-authored in a session firewalled from the implementing context (the `ux-spec-synthesizer` role, the relocated TK-02 Step 2.3 synthesis) per [REF] Hub-CD-CC Architecture §1.1 / §5; Hub authors PRD / TDD upstream content, not the detailed UX-spec. (CC-side authoring of the UX-spec is correct behavior, not drift)
- **CD attempting to author the UX Design Spec instance markdown** (phase-level or per-feature) — CD outputs design files (visual artifacts) only; the markdown counterparts are CC-authored detailed-spec deliverables per [TPL] UX Design Spec
