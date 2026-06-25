# [RULE] Workspace Topology

- **Project**: HR Digital Cockpit
- **Document Type**: Infrastructure Specification
- **Status**: Active canonical
- **Role**: Stable declaration of the multi-node development workspace infrastructure: that multiple production-peer nodes exist, the parity discipline that binds them, the walking-skeleton-first ordering rule that governs cross-workspace handoff sequencing, the node-assignment interface contract that anchors TDD `assigned_node` fields and GitHub Issue marker blocks, and workspace inception governance. Substantive operational details (specific tool stack and versions, specific GitHub workflow configuration, specific node-assignment step sequences, anti-drift signals at the operational level, inception checklist contents) are owned by CC under its own substantive canonical.
- **Source Category**: Cat 4
- **Management-System Role**: Infrastructure specification; outside L1-L5 hierarchy
- **Relationship to [OS]**: Serves the Development Track infrastructure layer referenced by [OS] §7.1 routing; subject to [OS] §8.5 paired-update consistency. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side residue carries the constitutional skeleton declared here; CC-side substantive canonical owns the operational details.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §3 (global core with governed local variance) to node definitions — every node is an equal production peer with no client/server asymmetry, governed by a single shared canonical configuration.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary. The multi-node infrastructure is internal to CC; this Hub residue declares the constitutional shape that Hub-authored TDDs and handoff documentation must respect. The CC `.claude/` canonical layer is part of that CC workspace architecture; its multi-node distribution is governed by the parity discipline in §2 below.
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. WT constitutional residue declares multi-node existence; CCAR constitutional residue declares tier separation. The two are orthogonal constitutional dimensions of the CC workspace.
- **Relationship to [MECH] Development Track Workflow**: Companion. The node-assignment workflow declared in §4 below is the infrastructure layer that DTW's TK orchestration runs on. DTW constitutional residue declares TK existence and Hub/CC ownership boundaries; this source declares the multi-node substrate.
- **Relationship to [MECH] CI/CD Milestone Policy**: M-state evidence is acceptable from any node defined here; the originating node is recorded in evidence files but does not affect gate validation logic. This is constitutional — Hub-side handoff documentation can rely on node-neutrality of evidence.
- **Relationship to [MECH] Application Lifecycle Handoff**: Release artifacts originate from any node; release-channel node neutrality is preserved as constitutional invariant.
- **Pairings I participate in**: P-10 (this source's §4 ↔ [MECH] Development Track Workflow §4.0); P-11 ([TPL] TDD §3 ↔ this source's §3); P-33 (with [MECH] Application Lifecycle Handoff §5.2 + [TPL] TDD §3 — TDD `assigned_node` field references logical names from this source's constitutional residue). Pairings P-14 / P-52 from the pre-split version are retired at this Hub residue level; their substantive obligations migrate to CC under the CC-side substantive Workspace Topology canonical.

## How to use this source (Hub-side)

Use this source when:
- Authoring or reviewing Hub-side handoff documentation that names nodes, references parity, or invokes the walking-skeleton-first ordering
- Determining whether a proposed cross-workspace artifact (e.g., a TDD field, an Issue marker schema element) needs constitutional Hub-side approval vs CC-side substantive authoring
- Confirming that a node naming convention reference resolves to an authoritative constitutional declaration

Do not use this source as:
- A specific tool stack reference (CC substantive canonical owns versions, tools, and installation discipline)
- A GitHub workflow configuration reference (CC substantive canonical owns branch protection, conflict-defense layers, automation)
- A node assignment step-by-step procedure (CC substantive canonical owns the four-step workflow execution)
- A workspace inception checklist (CC substantive canonical owns the inception procedure; this source declares only that inception exists)

---

# 0. Boundary and position

## 0.1 What this source owns (constitutional)

- The fact that the CC workspace runs on a multi-node infrastructure with logical node identity
- The logical naming convention for nodes (`dev-node-portable`, `dev-node-stationary-N`)
- The constitutional invariant that nodes are equal production peers — no client/server asymmetry
- The parity discipline as a cross-cutting rule: toolchain versions and `.claude/` canonical content must agree across nodes
- The walking-skeleton-first ordering rule: walking_skeleton unit precedes feature units; cross-workspace handoff sequencing respects this ordering
- The node-assignment interface contract: TDDs carry an `assigned_node` field; GitHub Issues carry a marker block; the schema of these interface elements is constitutional
- Workspace inception governance: that inception exists as a once-per-monorepo activity preceding any application work

## 0.2 What this source does not own

- Specific tool list and version-pinning details (CC substantive)
- Concrete version specifier strategy per tool, reproducibility layer assignment (CC substantive)
- GitHub workflow configuration: branch protection settings, conflict defense mechanisms, automation rules (CC substantive)
- Per-node-assignment step procedures (CC substantive)
- Anti-drift red flags at the operational level (CC substantive; cross-workspace anti-drift signals are noted in §6 below)
- Workspace inception checklist contents (CC substantive)
- macOS-level personal configuration (operator personal layer; not regulated by canonical)
- Operational `MANUAL_*.md` artifacts (operator personal, per [OS] §9.4)

---

# 1. Multi-node infrastructure (constitutional)

## 1.1 Existence and peer model

The CC workspace runs on a multi-node infrastructure. Multiple physical machines, each mapped to a **logical node identity**, can independently execute Development Track work. All nodes are **equal production peers**: no client/server asymmetry, no privileged node, no fallback hierarchy. Any node may execute any feature unit; the only differentiator across nodes is availability profile (e.g., portable laptops are part-time; stationary machines may be always-on).

## 1.2 Logical naming convention

Logical node identity is decoupled from physical hostname, OS-assigned identifier, or vendor serial. Logical names follow the convention:

- `dev-node-portable` — the single portable node (the one-human-one-portable invariant; no `dev-node-portable-2`)
- `dev-node-stationary-N` — stationary nodes numbered starting from 1 (`dev-node-stationary-1`, `dev-node-stationary-2`, …)
- Logical names are kebab-case, lowercase, ASCII only
- Logical names are immutable once declared in CC substantive canonical's logical-to-physical mapping table

The specific list of currently declared logical-to-physical mappings is CC substantive content.

## 1.3 Canonical reference points

Logical node names are the canonical reference used in:
- TDD `assigned_node` field
- GitHub Issue marker blocks
- Evidence files that record originating node
- Any canonical or specification artifact that names a node

OS-level hostnames are not normative for cross-workspace references.

## 1.4 Node-neutral evidence invariant (constitutional)

M-state evidence and release artifacts are valid regardless of originating node. The originating node is recorded in evidence files for traceability but does not affect gate validation logic. Hub-side handoff documentation can rely on this node-neutrality when consuming evidence from any node.

---

# 2. Parity discipline (constitutional cross-cutting rule)

Toolchain versions and the shared `.claude/` canonical content must agree across all nodes at any given moment. **Divergence is an anti-drift signal**, regardless of cause.

Parity is achieved through three mechanisms (existence-declared here; substantive specifics owned by CC):

1. **Committed declaration files**: toolchain versions are pinned in repository-committed files (e.g., `.tool-versions`, `package.json` engines/packageManager, lockfiles); nodes verify their installed versions match the committed declaration. The specific declaration-file inventory and version-specifier strategy is CC substantive content.

2. **Shared `.claude/` canonical content**: subagents, skills, hooks, and rules in `.claude/` are not duplicated per node — they live in the monorepo and each node pulls the same content. (The CC `.claude/` canonical layer is part of the CC workspace architecture per [REF] Hub-CD-CC Architecture; this source declares the parity requirement.)

3. **Upgrade discipline**: toolchain upgrades flow through an automated dependency-upgrade PR cadence (specific tool selection and the PR creation, review, and merge protocol are CC substantive content).

**Scope of parity — what parity applies to and what it does not**:

Parity in this section applies to **CC monorepo-committed content**: toolchain declarations and `.claude/` substantive content. These are subject to the divergence-as-anti-drift-signal rule because they are committed within the monorepo and consumed by per-node Claude Code instances.

Hub canonical content (`hdc_*.md` files in the canonical repository / Hub PK) is **not** subject to per-node parity discipline at CC. Hub canonical follows a **read-from-authoritative-source** model: each CC node accesses the authoritative Hub canonical source independently. Parity emerges naturally because all consumers — Hub Claude via RAG, CC instances via their access mechanism — read from the same authoritative source rather than maintaining synchronized committed copies.

The specific Hub-canonical access mechanism at CC (e.g., local clone of the canonical GitHub repository) is **operator-personal infrastructure**, not canonical-governed. This canonical declares only the contract: Hub canonical is read-only at CC; CC does not modify Hub canonical at its origin.

**Cross-workspace implication**: Hub-side handoff documentation does not need to specify per-node versions because parity guarantees a single effective version at any handoff time.

---

# 3. Walking-skeleton-first ordering rule (constitutional)

For any new app, the walking_skeleton unit precedes all feature units. This is a **constitutional ordering invariant** because it governs cross-workspace handoff sequencing: Hub-authored PRDs and TDDs respect this ordering when designating unit dependencies, and the [MECH] Cross-Tool Workflow Handoff sequencing consumes this ordering.

The walking_skeleton unit's specific output canonical set (Tier 1 placeholder UI, Tier 2 BFF stub, Tier 3 domain skeleton, CLAUDE.md hierarchy instantiation, etc.) is **substantive content** owned by CC substantive canonical. This residue declares only the ordering rule and its cross-workspace effect.

**Anti-drift signal**: A feature unit's TDD that does not reference a prior walking_skeleton unit's outputs is a cross-workspace anti-drift signal per [OS] §12; substantive in-CC anti-drift signals are at CC's WT canonical.

---

# 4. Node-assignment interface contract (constitutional)

The node-assignment workflow exists as a four-step procedure operated by the operator. The specific four steps are CC substantive content. The **interface contract** — the schema of fields and markers that Hub-authored artifacts must populate or reference — is constitutional and declared here.

## 4.1 TDD `assigned_node` field

Every TDD instance carries an `assigned_node` field declaring which logical node will execute the unit. The field value is one of the logical names from §1.2.

## 4.2 GitHub Issue marker block

Every Development Track GitHub Issue carries a marker block declaring `unit_type`, `unit_id`, `assigned_node`, and `prerequisite_units` fields. The block format is constitutional (it is the interface that DTW orchestration consumes); the specific four-step process for populating and acting on the block is CC substantive content.

The constitutional schema:

```
unit_type: <walking_skeleton | feature | app_integration>
unit_id: <kebab-case identifier>
assigned_node: <logical node name from §1.2>
prerequisite_units: <comma-separated unit_ids or 'none'>
```

The constitutional invariant: the four fields above appear in every Issue marker block. Additional fields are CC substantive extensions; their presence is governed at CC substantive canonical.

## 4.3 Reassignment

Mid-execution node reassignment is permitted under CC substantive canonical's reassignment protocol. The constitutional invariant: a reassigned unit's evidence files reflect the final executing node, not the original assignment.

## 4.4 Node retirement

A logical node may be retired (decommissioned) under CC substantive canonical's retirement protocol. The constitutional invariant: a retired logical name is **not reused** for a future node, and historical evidence files that recorded the retired node retain its logical name unchanged. The specific retirement procedure (physical decommission steps, mapping-table update) is CC substantive content.

---

# 5. Workspace inception governance (constitutional)

Workspace inception is a **once-per-monorepo activity** that precedes any application work. The constitutional invariants:

- Inception happens before any walking_skeleton unit can be authored
- Inception establishes project-level singletons (canonical references, monorepo structure, shared tooling) that subsequent application work consumes
- Inception is operator-led; CC executes specific steps per CC substantive canonical

The **specific inception checklist** — what files to create, what tools to verify, what GitHub configuration to apply — is CC substantive content. This residue declares only that inception exists as a constitutional precondition for Development Track work.

**Cross-workspace implication**: Hub-authored documentation that assumes a runnable monorepo (e.g., a PRD referencing `apps/{app-slug}/`) implicitly requires inception to have completed. Hub does not author the inception procedure itself.

---

# 6. Anti-drift signals (Hub-side / cross-workspace)

Anti-drift signals at the cross-workspace level, surfaced here because they involve Hub-authored content or cross-workspace handoff:

- A Hub-authored TDD with `assigned_node` field value that is not in the logical naming convention of §1.2
- A Hub-authored handoff document that assumes a node has different toolchain version than another node (parity discipline violation surfacing at the cross-workspace interface)
- A Hub-authored PRD or TDD that designates a feature unit with no prerequisite walking_skeleton unit (walking-skeleton-first ordering rule violation)
- An [MECH] Cross-Tool Workflow Handoff content contract that references node-level specifics rather than node-neutral evidence (the node-neutrality invariant in §1.4 violation)
- A cross-workspace artifact that re-derives the node-assignment marker block schema from §4 (single-source-of-truth violation)

In-CC operational anti-drift signals (tool version drift detection, GitHub workflow degradation, `.claude/` content divergence detection mechanics) are governed by CC substantive WT canonical.

---

# 7. Hub Claude soft compliance — trigger phrases (Hub-internal substantive)

> **Scope note**: §7 and §8 are **Hub-internal substantive** content per [OS] §0.1.5 Premise 5 — they govern Hub Claude's own conversational behavior in node-related discussions, not cross-workspace interface. They remain at this Hub-side source rather than migrating to CC. Cross-references in this section name the CC substantive WT canonical and the relevant topic in parentheses — they identify where the referenced procedural detail lives at CC under the decoupled-reference model, without citing CC-side section numbers.

When user phrasing in a Hub Claude conversation matches any of the following, Hub Claude SHOULD remind the user of the relevant section of CC substantive WT before proceeding. Hub Claude MUST NOT auto-execute the action; surface as confirmation prompt only.

**Node assignment phrasing** → reference CC substantive WT (node assignment workflow):
- "assign this to portable" / "give this to the air"
- "run this on the mini" / "let stationary-1 take this"
- "switch nodes" / "move this to the other node"
- "split this feature across nodes"

**Reassignment phrasing** → reference CC substantive WT (reassignment protocol):
- "move this feature from <node> to <node>"
- "hand this off to the other node"
- "the portable is closed, reassign"

**Out-of-scope tool phrasing** → reference CC substantive WT (out-of-scope tools — Cowork, Dispatch, etc.):
- "use Cowork to run this TK"
- "let Cowork pick up the slice"
- "send this to Dispatch"
- "have Dispatch handle the merge"

**Cross-node Codex phrasing** → reference CC substantive WT (Codex co-location):
- "run Codex on the other node"
- "Codex review on the mini for this portable slice"

**Tool version drift phrasing** → reference CC substantive WT (version parity rule):
- "the air is on a different node version" / "the mini still has old Java" — parity violation
- "let me just pin Node to a specific patch in engines" / "set engines.node to N.x.y exactly" — exact-pin attempt against version specifier strategy
- "I'll merge this Renovate PR mid-feature" / "let me upgrade Node while the slice is running" — in-flight upgrade violation
- "skip the lockfile, just run pnpm install fresh" / "regenerate the lockfile to fix this" — undermines L1 reproducibility

**Branch protection bypass phrasing** → reference CC substantive WT (branch protection settings):
- "let me push straight to main"
- "skip the PR for this one"
- "merge without review"

**Walking-skeleton-first ordering phrasing** → reference §3 constitutional rule above + CC substantive WT (walking-skeleton output canonical set):
- "start the time-off-request feature slices now" / "begin TK-04 for this feature" / "kick off node-side work for this feature" — when Phase 1 walking-skeleton has not yet reached `status: merged` (specification authoring — Hub PRD/TDD plus the CC-side detailed spec in the firewalled S1/S2 sessions — is NOT gated; the gate is the unit's first node-side implementation milestone)
- "kick off the app-integration tests now" / "start TK-09 for app-int" — when Phase 1 walking-skeleton has not yet reached `status: merged`
- "skip the walking skeleton, jump straight to features" — direct ordering rule violation

**Phase boundary parallelism phrasing** → reference §3 (walking-skeleton ordering) and the three-scenario response below for Phase N → Phase N+1 transitions:
- "start phase N+1 PRD now" / "begin the next phase spec" / "kick off phase 2 work"
- "draft the phase 3 TDD while we're still coding phase 2"
- "let me work on phase N+1 intent/acceptance now"

Hub Claude response logic for phase-boundary phrasing requires the operator to disambiguate which scenario applies, because Hub Claude has no observation of phase state (per §8.1 below):

| Scenario | Trigger condition (operator-declared) | Hub Claude response |
|---|---|---|
| (A) Additive only | Phase N+1 is strictly additive over Phase N: no architecture deltas anticipated in Phase N+1 TDD §1, no foundational change to cross-feature concerns in Phase N+1 TDD §2 | No warning. Phase N+1 PRD/TDD/Intent/Acceptance work proceeds in parallel with Phase N coding/testing |
| (B) Architecture impact | Phase N+1 contains architecture deltas (TDD §1 deltas) that may trigger refactoring of Phase N work-in-flight or already-merged feature units | Soft warning: "Phase N+1 contains architecture deltas; Phase N work-in-flight may need re-verification once Phase N+1 TDD §1 lands. Continue?" — operator explicit acknowledgment recorded before proceeding |
| (C) Phase 1 walking-skeleton not yet merged | Phase N is Phase 1 and the Phase 1 `walking-skeleton` unit has not yet reached `status: merged` (per §3 constitutional walking-skeleton-first ordering rule) | Stronger soft warning: "Phase 1 walking-skeleton not yet merged to main. Phase N+1 PRD work may proceed but no unit can start node-side execution in either phase until Phase 1 walking-skeleton merges per the constitutional ordering rule. Continue?" — operator explicit acknowledgment recorded before proceeding |

**Operational test for "architecture delta"** (the A/B discriminator): a Phase N+1 change counts as an architecture delta if it is any change to TDD §1 module decomposition, tier boundaries, or the shared data model that a Phase N feature depends on. Example pair — adding a new self-contained Phase N+1 feature module that consumes existing APIs is *not* an architecture delta (scenario A); splitting a Phase N shared module in two, or altering a shared data-model entity a Phase N feature reads, *is* an architecture delta (scenario B).

Hub Claude does not auto-classify the scenario; the operator declares which scenario applies in the same conversational turn that triggered the phrase, or Hub Claude asks. The operator's declaration plus Hub Claude's transcribed acknowledgment are conversation-local — they persist only within the current conversation and are not a durable record any later session can read.

Hub Claude reminders are conversational. The operator may override with explicit acknowledgment, but the override itself must be stated in the conversation; this acknowledgment is conversation-local and does not persist beyond the current conversation.

---

# 8. Hub Claude observability boundary (Hub-internal substantive)

## 8.1 No node state observability

Hub Claude has no observation of:
- Which unit (any unit_type) is currently in flight on which node
- Backlog of slices or units remaining on a node
- Current `git status` of any worktree
- Open Claude Code sessions on a node
- In-flight Codex review state
- GitHub Issue marker block current values, including `unit_type`, `unit_id`, `prerequisite_units`, `status`
- Phase 1 walking-skeleton current `status` (whether `assigned` / `in-progress` / `merged`)
- Which phase boundary scenario (A / B / C per §7) applies for any phase transition
- Disk, CPU, or memory pressure on any node

When the operator asks "which node should this go to," Hub Claude does not pretend to have visibility. Hub Claude states explicitly: "I don't observe node state; tell me current backlog and your availability for the next [estimated unit duration], and I can offer an analysis." If the operator does not provide that input, Hub Claude declines to recommend; the operator's pure human judgment drives.

This boundary applies broadly to any state Hub Claude cannot observe — file system content on dev nodes, in-flight Codex sessions, GitHub Issue marker state, and similar runtime conditions. When in doubt, Hub Claude asks rather than assumes.

## 8.2 What Hub Claude must not auto-do

- Update GitHub Issue marker blocks (these are operator actions; Hub Claude transcribes when asked, never authors directly)
- Infer node assignment from context (always confirm with the operator)
- Override the operator's node-assignment judgment (surface concerns as questions, not counter-decisions)
- Recommend reassignment without the operator first declaring intent
