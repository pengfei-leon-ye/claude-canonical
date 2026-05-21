# [REF] CC Project Memory Bank Layout

> **RETIRED 2026-05-21** (per [OS] §8.8a source retirement procedure). This canonical source has been retired. Its load-bearing content — the constitutional declaration that CC maintains its own canonical layer, and the Hub↔CC visibility boundary — is framed by **[REF] Hub-CD-CC Architecture**, which absorbs it. Per the 2026-05-21 governance decision: the Hub canonical layer does not maintain a source describing the CC-side canonical layout; how CC structures its own architecture is owned by CC, and CC's adherence to Hub constitutional rules is assured operationally by the operator through Development Track delivery quality (see [OS] §0.1.5). No [OS] §8.10 reserved-empty registry entry is created — the slot is not reserved for re-activation. The file is retained per [OS] §8.8a for historical resolution of past references; the body below is the pre-retirement content and is no longer active canonical.

- **Project**: HR Digital Cockpit
- **Document Type**: Reference Catalog
- **Status**: Retired 2026-05-21 (was: Active canonical)
- **Role**: Constitutional declaration that CC has its own canonical layer for CC-internal canonical content, the high-level structural pattern of that layer, and the visibility boundary between Hub-side and CC-side canonical authority. Substantive layout details (specific paths, naming conventions, indexing rules, update discipline, anti-drift red flags) are owned by CC under its own canonical layer.
- **Source Category**: Cat 4
- **Management-System Role**: Reference catalog source; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; subject to [OS] §8.5 paired-update consistency. The hub-to-CC visibility boundary in [OS] §1.4 applies — this source describes the **existence and constitutional shape** of the CC canonical layer but does not mirror CC-internal substantive content into Hub canonical. The constitutional / substantive boundary in [OS] §0.1.5 (Premise 5) applies: Hub-side owns the constitutional skeleton declared here; CC-side owns the substantive layout details.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control) — the existence of a CC canonical layer is itself a management mechanism.
- **Relationship to [REF] Hub-CD-CC Architecture**: Consumed by §4.3 (CC workspace's canonical outputs). This source declares the existence of the CC canonical layer; [REF] Hub-CD-CC Architecture frames why CC has its own canonical (workspace identity per Premise 5) and governs the decoupled-reference model used between Hub and CC.
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. CCAR's tier-separation discipline is the constitutional anchor for the tier-aligned CLAUDE.md hierarchy declared in §2 below. CC-side substantive CCAR content (specific tier tool choices, file path patterns, repository layout) is consumed by CC's own substantive layout canonical.
- **Relationship to [RULE] Workspace Topology**: Different scope. Workspace Topology's constitutional residue at Hub governs multi-node parity discipline; this source's constitutional residue governs the per-node CC canonical layer existence. CC-side substantive WT content (specific tool stack, version pinning) and CC-side substantive layout content together implement the per-node CC canonical layer.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: Cited by §4 below as the notification protocol for CC → Hub direction when CC substantively changes its canonical layer in ways that affect cross-workspace handoff.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [REF] CC Project Memory Bank Layout` header fields per [OS] §8.5.1a)

## How to use this source

Use this source when:
- Reasoning about the Hub-to-CC architectural boundary and what CC is expected to own
- Authoring cross-workspace handoff documentation that needs to reference CC's canonical layer
- Confirming that a proposed addition belongs at CC (substantive) vs at Hub (constitutional) for CC-internal canonical content

Do not use this source as:
- A canonical reference for specific CC-internal file paths, naming conventions, or layout details (these live at CC under its own canonical layer)
- A substantive guide to authoring CC-internal canonical files (CC owns its own authoring discipline)

## Scope note

This source's Hub-side residue declares the **constitutional shape** of the CC canonical layer: its existence, its high-level structural components, and the visibility boundary that separates Hub-side authority from CC-side authority. The substantive details — what file paths to use, what naming conventions to follow, how files are discovered at runtime, how the layout evolves over time — are owned by CC at CC's own canonical layer location (chosen by CC; not specified at Hub).

---

# 0. Boundary and position

## 0.1 What this source owns

- The constitutional declaration that CC has its own canonical layer
- The high-level structural pattern (tier-aligned CLAUDE.md hierarchy + `.claude/` configuration directory at the per-node working-directory level)
- The visibility boundary between Hub canonical and CC canonical (cross-reference to [OS] §1.4)
- The cross-workspace notification protocol when CC-side canonical changes affect Hub-side handoff documentation

## 0.2 What this source does not own

- Specific paths for CLAUDE.md files at each hierarchy level (CC-owned)
- Specific `.claude/` subdirectory structure and contents (CC-owned)
- Naming conventions, indexing rules, discovery mechanics (CC-owned)
- Update discipline for adding, modifying, renaming, removing CC-internal canonical files (CC-owned)
- Anti-drift red flags specific to CC layout (CC-owned)
- Multi-node parity discipline for CC-internal canonical files (Hub-side WT constitutional residue declares the parity requirement existence; CC-side substantive content implements it)

## 0.3 Position relative to adjacent canonical sources

| Adjacent source | Relationship |
|---|---|
| [OS] | Operates within [OS] §7.1 routing. [OS] §1.4 hub-to-CC visibility boundary applies. [OS] §0.1.5 Premise 5 governs the constitutional / substantive split. |
| [REF] Hub-CD-CC Architecture | Consumed by §4.3 (CC canonical outputs inventory). The decoupled-reference model in [REF] Hub-CD-CC Architecture is the operational basis for how CC consumes Hub constitutional rules. |
| [RULE] Claude Code Architecture Rules | Hub-side constitutional residue of CCAR is the constitutional anchor for the tier-aligned CLAUDE.md hierarchy. |
| [RULE] Workspace Topology | Hub-side constitutional residue of WT declares multi-node parity discipline; CC implements parity for its own canonical layer. |
| [MECH] Cross-Tool Workflow Handoff | Notification protocol for CC → Hub direction when CC layout changes affect handoff documentation. |

---

# 1. Existence declaration

CC has its own canonical layer at a location chosen by CC (conventionally under `<repo-root>/.claude/canonical/` or equivalent within the CC working directory). This canonical layer is independent of the Hub canonical layer:

- Hub does not mirror CC canonical content
- CC does not mirror Hub canonical content
- Both layers are authoritative within their respective scopes per [OS] §0.1.5 Premise 5

CC's canonical layer covers two structural components, declared as constitutional in §2 and §3 below.

---

# 2. CLAUDE.md hierarchy — tier-aligned constitutional structure

CC's canonical layer includes a hierarchy of CLAUDE.md files that anchor session context at successively narrower path scopes within the CC working directory. The hierarchy is **tier-aligned**: each level corresponds to a tier or scope boundary declared by Hub-side [RULE] Claude Code Architecture Rules (CCAR).

The constitutional invariants:
- A project-root CLAUDE.md exists, loaded at every CC session start
- App-scoped and tier-scoped CLAUDE.md files exist where CCAR declares tier boundaries
- The hierarchy levels correspond to CCAR's tier structure; changing the number of levels requires same-revision update of CCAR's tier separation rule

Specific paths, "must reference" content lists, authoring authority per level, and cross-level navigation discipline are CC-owned substantive content.

---

# 3. `.claude/` configuration directory — constitutional anchor

CC's canonical layer includes a `.claude/` directory at the root of the CC working directory. This directory is the constitutional anchor for CC's runtime configuration:
- Subagent definitions
- Skill manifests
- Command implementations
- Lifecycle hooks
- Path-scoped behavioral rules

The constitutional invariants:
- The `.claude/` directory exists at the working-directory root
- Its content category (configuration for CC runtime) is fixed by this declaration
- Sub-categories within `.claude/` (the specific directory layout for subagents, skills, etc.) are CC-owned substantive content

Specific subdirectory structure, file naming conventions, indexing and discovery rules, and the content discipline within each subcategory are CC-owned.

---

# 4. Update notification protocol

When CC substantively changes its canonical layer in ways that affect cross-workspace handoff documentation (Hub-side or CD-side artifacts that reference CC's canonical layer structure), the change is notified to Hub via [MECH] Cross-Tool Workflow Handoff (CC → Hub direction).

Notification triggers (constitutional):
- Adding a new CC canonical artifact that becomes referable from Hub handoff documentation
- Renaming or relocating a CC canonical artifact that is referenced from Hub-side canonical or handoff documentation
- Retiring a CC canonical artifact that is referenced from Hub-side content

Notification non-triggers (CC-internal, no Hub notification required):
- Adding, modifying, or retiring CC canonical artifacts that have no Hub-side or CD-side cross-reference
- Internal restructuring within CC's `.claude/` directory that does not affect cross-workspace handoff
- Any content authoring activity within CC's canonical layer that does not change the cross-workspace interface

CC determines whether a given change crosses the notification threshold; Hub does not audit CC-internal changes. The notification, when sent, follows the [MECH] Cross-Tool Workflow Handoff schema for the CC → Hub direction.

---

# 5. Visibility boundary reminder

Per [OS] §1.4 audience and consumption model:
- Hub Claude does not read CC-internal canonical files via any channel
- CC does not read Hub canonical via Hub-side filesystem path or Hub RAG layer
- Hub constitutional rules reach CC behavior by CC referencing them through its own canonical authoring (CC's CLAUDE.md or canonical-layer files cite Hub canonical by name + §, per the decoupled-reference model in [REF] Hub-CD-CC Architecture)

The CC canonical layer is authoritative for CC operational behavior; Hub canonical residue (this source plus other constitutional residues from Phase 3 splits) declares the architectural shape that CC's layer fits within.

---

# 6. Anti-drift signals (Hub-side)

Hub-side anti-drift signals related to this source's constitutional residue:

- Hub canonical content that purports to specify CC-internal substantive layout details (specific paths, naming conventions, indexing rules) — such content is a [OS] §12 anti-drift signal and should migrate to CC's canonical layer
- Cross-references in Hub canonical that cite specific CC-internal file paths (rather than naming the constitutional anchor declared here)
- New canonical content at Hub that re-derives CC-side substantive layout rules — duplication candidate, migrate to CC

CC-internal anti-drift signals (specific to the substantive layout) are governed by CC's own canonical layer.
