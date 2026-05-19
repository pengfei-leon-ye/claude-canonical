# [RULE] Workspace Topology

- **Project**: HR Digital Cockpit
- **Document Type**: Infrastructure Specification
- **Status**: Active canonical
- **Role**: Stable infrastructure-rules source defining the multi-node development workspace topology for Cat 4 Development Track work, including logical node identity, tool stack per node, GitHub workflow, multi-node parallel production model, and node assignment workflow.
- **Source Category**: Cat 4
- **Management-System Role**: Infrastructure specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Serves the Development Track infrastructure layer referenced by [OS] §7.1 routing; subject to [OS] §8.5 paired-update consistency. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §3 (global core with governed local variance) to node definitions — every node is an equal production peer with no client/server asymmetry, governed by a single shared canonical configuration.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. WT defines the multi-node infrastructure on which the CC workspace executes; Hub-CD-CC Architecture frames why CC is the implementation pillar in the three-workspace tripartition.
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. WT §4 multi-node deployment hosts CCAR §5 subagents + §X scopes + §Y paths.
- **Relationship to [RULE] Codex Plugin Usage**: Co-located. Codex executes on the unit's assigned node; cross-node invocation is an anti-pattern.
- **Relationship to [MECH] Development Track Workflow**: Companion. WT §6 node assignment workflow + §4 unit-type scheduling parity feed DTW §4.0 per-unit-type task paths.
- **Relationship to [MECH] CI/CD Milestone Policy**: M0–M5 evidence is acceptable from any node defined here; the originating node is recorded in evidence files but does not affect gate validation logic.
- **Relationship to [MECH] Application Lifecycle Handoff**: Release artifacts originate from any node's PR; release-channel node neutrality is preserved.
- **Pairings I participate in**: P-10 (with [MECH] DTW §4.0 unit_type catalog), P-11 (with [TPL] TDD §3 walking-skeleton-header), P-14 (with [MECH] Dev-Loopback `apps/{app-slug}/dev/`), P-33 (with [MECH] Application Lifecycle Handoff §5.2 + [TPL] TDD §3), P-52 (with [MECH] Tools Health Cadence §5 P0 inventory)

## How to use this source

Use this source when:
- introducing a new physical machine into the development workspace
- assigning a feature to a node for execution
- reassigning a feature mid-execution
- verifying tool stack parity across nodes
- configuring GitHub branch protection
- diagnosing multi-node parallel execution issues
- evaluating whether a tool or workflow belongs in the canonical tool stack
- performing initial workspace inception (§10)

Do not use this source as:
- a tier architecture reference ([RULE] Claude Code Architecture Rules §1)
- a subagent roster catalog ([RULE] Claude Code Architecture Rules §5)
- a repository layout reference ([RULE] Claude Code Architecture Rules §Y)
- a TK-by-TK orchestration reference ([MECH] Development Track Workflow §4)
- an M-gate semantics reference ([MECH] CI/CD Milestone Policy §2)
- a Codex command catalog ([RULE] Codex Plugin Usage §3)
- a release-channel specification ([MECH] Application Lifecycle Handoff)
- a specification of macOS-level personal configuration (operator personal layer; not regulated by canonical)

---

---

# 1. Boundary and position

## 1.1 What this source owns

- Logical node identity: names, mapping to physical machines, naming convention for future nodes, decoupling from operating-system hostname
- Tool stack required on every node, including version policy (parity-vs-pin separation, reproducibility layer assignment, version specifier strategy, upgrade cadence, mid-execution drift handling)
- Cross-node SSH access topology constraint (§3.6) — minimal declaration only; SSH key management is operator personal layer
- Out-of-scope tools (Cowork, Dispatch) declared as operator personal layer
- Subscription tier handling principle (operator decision)
- Multi-node parallel production model: scheduling parity for the three node-level work unit types (`walking_skeleton`, `feature`, `app_integration`), parallelism unit (slice within a unit; the unit itself for app_integration which has zero customer-facing slices), unit-level node affinity, same-node parallelism mechanism, subagent deployment topology, slice-to-node-capacity matching authority
- Walking-skeleton-first ordering rule and the walking-skeleton output canonical set (§4.6)
- GitHub workflow at the infrastructure level: branch topology, branch protection settings, conflict defense layers
- Node assignment workflow: four-step process, GitHub Issue marker block format including `unit_type` / `unit_id` / `prerequisite_units` fields, reassignment protocol
- Anti-drift red flags for the multi-node infrastructure
- Hub Claude soft compliance trigger phrases for node-related conversations
- Hub Claude observability boundary in the multi-node workspace
- Workspace inception checklist (§10) — once-per-monorepo project-level scaffolding and singletons that exist before any application; per-app skeleton is owned by §4.6.3 walking_skeleton output set, not by inception

## 1.2 What this source does not own

- Tier architecture ([RULE] Claude Code Architecture Rules §1)
- Subagent roster definitions and permission model ([RULE] Claude Code Architecture Rules §5, §X)
- Repository layout structure ([RULE] Claude Code Architecture Rules §Y)
- Skill loading rules ([RULE] Claude Code Architecture Rules §Z)
- Domain package lifecycle and contract testing convention ([RULE] Claude Code Architecture Rules §Y.4)
- Unit_type catalog content (purpose, scope, deliverables of `walking_skeleton`, `feature`, `app_integration`) — owned by [MECH] Development Track Workflow §4; this source consumes the catalog values for scheduling/parallelism/marker semantics
- TK-by-TK semantics ([MECH] Development Track Workflow §4)
- Per-unit-type milestone profile (which M0–M5 subset each unit_type runs through) — owned by [MECH] CI/CD Milestone Policy
- Milestone gate semantics ([MECH] CI/CD Milestone Policy §2)
- Codex command semantics, trigger logic, review-gate defaults, and per-unit-type fire conditions ([RULE] Codex Plugin Usage §3-§5)
- Release artifact format and personal preview boundary ([MECH] Application Lifecycle Handoff)
- Artifact content contracts (respective [TPL] sources)
- macOS-level system configuration (operator personal layer; not regulated by canonical)
- Operational step-by-step setup procedures (operator personal `MANUAL_*.md` artifacts under [OS] §9.4 non-canonical naming pattern)

## 1.3 Relationship to physical machines

Logical node identity (defined in §2) is decoupled from the physical machine's operating-system hostname, model name, vendor-assigned serial, or any other identifier the operator's local environment exposes. The mapping between a logical node and a physical machine is declared once per machine introduction in §2.2 of this source.

macOS hostnames, dock layouts, sleep settings, terminal preferences, and similar OS-level details remain operator personal layer and are not regulated by this source. When a tool surface (e.g., a CI log, a `git config` value, a terminal prompt) emits a physical-machine identifier, the operator translates to the logical name when the value is referenced in canonical artifacts.

---

# 2. Logical node identity

## 2.1 Logical name catalog

The current logical node catalog:

| Logical role | Availability profile | Production peer status |
|---|---|---|
| `dev-node-portable` | Part-time; user-driven open/close; daily-laptop mode (no aggressive sleep prevention; no long tasks while closed) | Equal production peer |
| `dev-node-stationary-1` | 24/7 always-on; `claude remote-control` persistent | Equal production peer |

Future stationary nodes follow the naming convention in §2.3.

All nodes are equal production peers. No client/server asymmetry exists between any two nodes. Any node may execute any feature; the only differentiator is availability profile.

## 2.2 Logical-to-physical mapping declaration

The mapping is declared once when a physical machine is introduced. The current mapping:

| Logical role | Physical machine | Declared at |
|---|---|---|
| `dev-node-portable` | MacBook Air M5 | 2026-04-26 |
| `dev-node-stationary-1` | Mac Mini M4 | 2026-04-26 |

Re-mapping (e.g., replacing the physical machine that hosts a logical role) is permitted but must be recorded as a new row with a new declaration date, not as an in-place edit, to preserve historical traceability of node assignments referenced in past TDDs and GitHub Issues.

## 2.3 Naming convention for future nodes

- `dev-node-portable` — reserved for the single portable node; one human, one portable; no `dev-node-portable-2` is planned
- `dev-node-stationary-N` — N starts from 1; the next stationary node will be `dev-node-stationary-2`, then `dev-node-stationary-3`, and so on
- Logical names are kebab-case, lowercase, ASCII only
- Logical names are immutable once declared in §2.2; if a different logical role is needed (e.g., a future GPU-equipped node distinct from a generic stationary node), declare a new name family rather than redefining an existing one

## 2.4 Decoupling from operating-system hostname

The logical node name is the canonical reference used in:
- TDD `assigned_node` field
- GitHub Issue marker block
- Evidence files that record originating node
- Any other canonical or specification artifact that names a node

The operating-system hostname (whatever the operator chooses for personal preference) is not normative and is not used as the canonical reference.

When a tool surface emits the OS hostname or a vendor identifier, the operator translates to the logical name when the value is brought into a canonical artifact.

---

# 3. Tool stack per node

## 3.1 Mandatory tools

Every node must be equipped with the following tools at parity. There is no light/heavy split. Every node is fully capable of executing any TK in the Development Track Workflow.

| Tool | Purpose | Version policy |
|---|---|---|
| Claude Desktop (incl. Code tab) | Hub Claude UI; Claude Code session host | Latest stable |
| Claude Code CLI | Development Track main loop execution | See [MECH] CI/CD Milestone Policy §1.1 baseline; otherwise latest stable |
| Claude Code Remote Control | Long-open execution support (primary on stationary nodes; available on portable when desktop+plugged) | Latest stable |
| Codex plugin | Code review at TK-12 (M4 prep) | Latest stable |
| Node.js | Tier 1 / Tier 2 runtime; pnpm prerequisite | Current Active LTS line, expressed as a major-bounded range in `engines.node`; see §3.2 |
| Java | Tier 3 runtime | Current LTS line within Adoptium-supported phase, distribution Temurin or Liberica; LTS major upgrade evaluated when downstream Spring Boot ecosystem confirms support; see §3.2 |
| pnpm | Monorepo workspace tooling | Exact patch via `package.json` `packageManager` field (Corepack constraint); see §3.2 |
| git, GitHub CLI (`gh`) | Source control and PR operations | Latest stable |
| Full `.claude/` directory | Subagents, custom skills (SK-F, SK-W), hooks | Single shared definition; pulled per node from the monorepo |

## 3.2 Version parity rule

This section governs how toolchain versions stay coherent across nodes and across time. It separates two often-conflated concepts (**parity** and **pin**), assigns reproducibility responsibility across the right layers, and codifies the upgrade mechanism.

### 3.2.1 Parity vs pin

**Scope: Toolchain version-management vocabulary in §3.2 context (Tier-1 toolchain reproducibility across nodes); applies to the items in §3.1 (Node.js, Java, pnpm) primarily.**

These are two independent properties:

- **Parity** — versions agree across all nodes at any given moment. A divergence (one node runs a different Node minor or Java patch than another node) is a parity violation regardless of what the baseline declares.
- **Pin** — version is anchored to a specific point in time, immune to "latest stable" drift. A pin is encoded in a committed file (`engines`, `.tool-versions`, `packageManager`, `pnpm-lock.yaml`).

Parity is necessary but not sufficient. Two nodes both running the latest patch of the moment have parity at install time, then drift apart on the next system update if no pin file commits the value to the repository. The repository-committed declaration is the baseline; nodes verify their installed version matches it.

### 3.2.2 Reproducibility layers

**Scope: Toolchain reproducibility layering in §3.2 context (Tier-1 toolchain across multi-node infrastructure); covers application dependencies, toolchain runtime, package manager, deployment artifact, CI runner.**

Reproducibility across the AI Development Track is layered. Each layer carries a distinct strength of lock:

| Layer | Lock strength | Mechanism | Where it lives |
|---|---|---|---|
| L1 — Application dependencies | Strict (byte-equivalent) | Lockfile (`pnpm-lock.yaml`); CI installs with `--frozen-lockfile` | Committed to repo |
| L2 — Toolchain runtime | Major + LTS line | `.tool-versions` (asdf), `engines.node` range in `package.json` | Committed to repo |
| L3 — Package manager | Exact patch | `packageManager` field in `package.json` (Corepack requires exact form `pnpm@X.Y.Z`) | Committed to repo |
| L4 — Deployment artifact | SHA digest | `FROM <base-image>@sha256:...` in Dockerfile (when production containerization is in scope) | Committed to repo, applied at production build time |
| L5 — CI runner | Explicit semver | `actions/setup-node` `node-version` input, reading from L2 file | `.github/workflows/*.yml` |

The cross-time reproducibility of evidence does not depend on freezing L2 forever. It depends on L1 (lockfile) being committed and L4/L5 (when deployed/run in CI) reading from the same baseline files. L2 is the parity anchor for development environments; it may evolve through the upgrade mechanism in §3.2.4 without breaking historical evidence reproduction, because rebuilding a historical commit checks out that commit's L1 lockfile and L2 declaration together.

### 3.2.3 Toolchain version specifier strategy

For each Tier-1 toolchain item, the committed declaration form is:

| Tool | File | Form | Example shape | Rationale |
|---|---|---|---|---|
| Node.js | `package.json` `engines.node` | Major-bounded range | `">=N.0.0 <(N+1).0.0"` where N is the current Active LTS major | Allows minor/patch upgrade without spec churn; rejects accidental cross-major drift. Renovate-maintainer guidance is explicit that exact-pin of `engines` is contrary to ecosystem norms — `engines` is a range field by design. |
| Node.js | `.tool-versions` | Specific minor or patch | `nodejs N.x.y` resolving to current Active LTS | asdf consumes a concrete value to install; range form is not supported. The committed value is the parity baseline; Renovate updates it under §3.2.4 mechanism. |
| Java | `.tool-versions` | Specific patch with distribution | `java temurin-N.x.y+build.LTS` resolving to current Adoptium-supported LTS | asdf java plugin requires distribution-explicit form. Major version is the parity baseline; patch updates flow via §3.2.4. |
| pnpm | `package.json` `packageManager` | Exact patch | `pnpm@X.Y.Z` (no range form supported) | Corepack validates exact `name@version` form; range syntax is not supported by the Corepack contract. Patch-level alignment is mandatory for lockfile schema stability. |

The mismatch between the upper-bound range in `engines.node` and the specific value in `.tool-versions` is intentional: `engines` is a contract communicated to consumers (CI, contributors), while `.tool-versions` is the install instruction for the local node. Both must agree on the major version line (the parity anchor).

`pnpm-lock.yaml` is committed at all times. CI and local installs use `--frozen-lockfile` (or `pnpm install --frozen-lockfile`); a divergence between `package.json` and the lockfile aborts the install rather than silently regenerating.

The current concrete versions in use at any given time live in the committed declaration files (`.tool-versions`, `package.json`) within the monorepo, not in this canonical source. This source declares structure and policy; concrete values evolve under §3.2.4 mechanism without canonical revision.

### 3.2.4 Upgrade cadence and Renovate-driven mechanism

Toolchain upgrades flow through an automated dependency-update pipeline (Renovate or equivalent), not through ad-hoc node-by-node adjustments. The mechanism mirrors the upgrade-verification pattern in [MECH] CI/CD Milestone Policy §1.1 (Claude Code tooling baseline), adapted to the broader Tier-1 toolchain:

| Update type | Cadence trigger | Review path | Auto-merge eligibility |
|---|---|---|---|
| `pnpm-lock.yaml` patch updates of application dependencies | On dependency release | Renovate PR with full CI gate (M0–M3 equivalent test suites pass) | Yes for non-breaking, after CI green |
| Node.js patch within current Active LTS major | Within days of upstream release | Renovate PR with full CI gate | Yes for non-breaking, after CI green; updates `.tool-versions` only |
| Node.js minor within current Active LTS major | Within ~2 weeks of upstream release | Renovate PR with full CI gate; review release notes for ecosystem-affecting changes | Operator decision; default conservative (manual merge) |
| Node.js major LTS rollover (current LTS line → next LTS line) | When the next LTS line stabilizes (typically 1 quarter after `Active LTS` promotion per nodejs.org release schedule) | Deliberate evaluation: read release notes; run one previously-passed slice through full M0 → M5 chain on a worktree using the candidate version; compare evidence against current baseline | Always manual; updates §3.1 table phrasing if needed, `engines.node` range, `.tool-versions`, and pnpm `packageManager` if the rollover requires it |
| pnpm patch/minor (`packageManager`) | On Corepack release | Renovate PR; both nodes run `corepack install` to align | Yes after CI green |
| Java patch within current LTS major | On Adoptium quarterly release | Renovate PR; if Spring Boot does not flag incompatibility, CI gate decides | Yes after CI green |
| Java major LTS rollover (current LTS line → next LTS line) | When ecosystem (Spring Boot, build plugins) confirms support and stability for the new LTS | Same deliberate evaluation as Node major LTS rollover | Always manual |

**No upgrade fires while a unit is in-flight on any node.** The operator checks whether any node has an open working branch (`feature/<app-slug>/<unit-slug>` ahead of `main`) before merging an upgrade PR. If units are in flight, the PR holds until they merge.

> **v0 assumption — to be calibrated**: Renovate config is introduced at workspace inception (per §10) alongside `.claude/` runtime. Pre-Renovate (during the bootstrap-to-inception window), upgrades flow manually through operator-driven PRs following the same cadence intent. Lessons-harvest after the first 3 upgrade events will confirm or revise the auto-merge eligibility rows.

### 3.2.5 Mid-execution drift handling

If a toolchain version on a node diverges from the committed baseline (`.tool-versions`, `engines.node`, `packageManager`) during a unit execution — typically via inadvertent system update or Renovate PR merging while a unit is in-flight — the operator decides between:

(a) **Freezing the version on that node until the unit merges** — the diverging node continues with its current (non-baseline) version; reverting to baseline waits until M5 (or the unit's terminal milestone per its per-unit-type milestone profile in [MECH] CI/CD Milestone Policy).

(b) **Reassigning the unit** to the parity-correct node per §6.3 — the unit continues from a node that matches baseline.

Either choice is recorded in the unit's GitHub Issue marker block (per §6.2) as a `version_drift_note` field appended to the marker block, distinct from the `reassigned_*` fields. The note records what diverged, when, and which option was chosen.

A node whose toolchain version diverges from the committed baseline is excluded from accepting **new** unit execution (§6 step 1) until brought back into parity.

## 3.3 Out of scope — not part of canonical tool stack

The following tools are operator personal convenience layer and are not regulated by this source:

- **Cowork** (Anthropic Desktop persistent-thread feature): personal task automation only — calendar, mail, document handling, cross-application scripts. Cowork is not part of the dev track. Cowork's UX assumes a single continuous conversation across desktop and mobile, which conflicts with the dev track's per-slice context isolation requirement that maps cleanly to Claude Code sessions.
- **Dispatch** (Anthropic): personal convenience tool, decoupled from architecture. Whether and how the operator binds Dispatch is a private choice.

Including Cowork or Dispatch in any TK execution path is an anti-pattern. See §7 for the corresponding red flag.

## 3.4 Subscription tier — operator decision

Multi-node parallel execution increases per-unit-time token consumption proportional to the number of concurrently active nodes. Subscription tier sizing is the operator's operational decision and is not regulated by this source. Phase D execution will produce empirical rate-limit hit data that may inform future tier reassessment; until then, no canonical trigger is encoded.

## 3.5 Codex co-location note

Codex plugin runs co-located with the slice's executing node. Cross-node Codex invocation (e.g., spec written on `dev-node-portable` but Codex review fired on `dev-node-stationary-1`) is an anti-pattern. Codex evidence files (`codex-review.md`) land in `apps/{app-slug}/evidence/{slice-id}/codex/` on the same node that executed TK-05 through TK-11.

Codex command semantics, trigger logic at TK-12, evidence path schema details, and review-gate defaults are owned by [RULE] Codex Plugin Usage; this source declares only the deployment topology constraint (co-located with executing node, no cross-node).

## 3.6 Cross-node SSH access redundancy (minimal canonical declaration)

When the workspace operates more than one declared dev node (per §2.2), each declared dev node is reachable via SSH from each other declared dev node and from the operator's primary working terminal. SSH access is symmetric — any node can reach any other node — providing cross-node redundancy for manual coordination, file inspection, and emergency access during multi-node execution.

SSH is operator-owned: key generation, key rotation, agent forwarding, and `~/.ssh/authorized_keys` files are operator personal infrastructure not regulated by this source.

SSH is **not** the transport for automated CI/CD evidence aggregation — cross-node evidence flows through GitHub Actions runners and PR-based artifact uploads (per §5 and [MECH] CI/CD Milestone Policy §1.2), not through cross-node SSH copy. SSH is also **not** a substitute for the canonical reassignment protocol (§6.3); when a unit needs to move between nodes, it moves via the marker block reassignment workflow, not by SSH-copying state across nodes.

This § declares the topology constraint only (every dev node reachable from every other dev node and from the operator's terminal, when more than one node operates). Procedural setup steps (key generation commands, host alias configuration, trust-bootstrap workflow) live in operator personal artifacts under [OS] §9.4 non-canonical naming pattern.

---

# 4. Multi-node parallel production model

## 4.1 Parallelism unit

The unit of parallelism varies by `unit_type` (the unit_type catalog is owned by [MECH] Development Track Workflow §4):

- **`feature` unit** — the unit of parallelism is the **feature slice**, not the feature, not the TK, not the file. Multiple feature slices may run in parallel — each on a single node, each completing the full M0 → M5 evidence chain on that node.
- **`walking_skeleton` unit** — Phase 1 only; consists of a single slice (the thinnest end-to-end vertical slice that proves the foundational architecture and establishes the CI/CD pipeline for the app). The slice runs the full M0 → M5 chain on one node. See §4.6.
- **`app_integration` unit** — has zero customer-facing capability slices; the unit itself is the parallelism granularity. The unit produces one PR (cross-feature integration tests, NFR validation harness, fixtures) that runs the milestone subset {M2, M3, M4, M5} on one node. M0 and M1 are not applicable because there is no slice-level new feature code. The per-unit-type milestone profile is owned by [MECH] CI/CD Milestone Policy.

The three unit_types share **scheduling parity** at the node-assignment level: any node may host any unit_type; the only differentiator is per-node availability profile (§2.1) and the operator's per-unit assignment judgment (§4.5).

## 4.2 Unit-level node affinity

Once a unit is assigned to a node per §6, all slices belonging to that unit (1 slice for `walking_skeleton`, 1+ for `feature`, 0 for `app_integration`) execute on that same node. No cross-node slice splitting within a single unit is permitted.

Rationale: cross-node slice splitting within a unit would fragment the unit's evidence chain across nodes, requiring evidence aggregation at PR time and introducing time-stamp and git-diff coordination overhead. Unit-level affinity localizes the evidence chain on a single node from M0 through M4 merge (or from M2 through M4 for `app_integration`) and produces a clean PR-time submission.

## 4.3 Same-node multi-slice parallelism

When a single node executes more than one slice concurrently — across slices of the same `feature` unit, or across slices belonging to different units (e.g., one `feature` unit's slice and one `walking_skeleton`'s sole slice — only valid in Phase 1 inception window before §4.6 ordering rule fires) — isolation is achieved via **git worktree** (Anthropic-native; documented in Claude Code's common-workflows guidance). Each concurrent slice runs in its own worktree, each with its own Claude Code session and its own context window.

No custom locking mechanism, no file-based locks, and no GitHub Actions worktree coordinator are introduced. Worktree isolation is the only same-node parallelism mechanism.

## 4.4 Subagent deployment topology — single shared definition, per-node single instance

The monorepo holds one shared `.claude/agents/` configuration. Every node pulls the same definition. Each node runs single subagent instances (one A1, one A2, one A3, etc.); same-node multi-slice parallelism uses worktree isolation per §4.3, not subagent multiplexing.

The subagent roster itself, including agent names, scopes, and bias-firewall context allocation, is owned by [RULE] Claude Code Architecture Rules §5 and §X. This source declares only the deployment topology decision — single shared definition, per-node single instance.

## 4.5 Slice-to-node-capacity matching — operator judgment

Whether a unit is suited to `dev-node-portable` (which has periodic open/close cycles) or `dev-node-stationary-1` (which is 24/7) is the operator's per-unit judgment, not a codified rule. The judgment applies symmetrically to all three unit_types.

Misjudgment cost: if a long-running unit is assigned to `dev-node-portable`, the portable node must stay open and plugged in for the unit's duration. The cost is bounded and recoverable; no canonical rule is needed. Hub Claude is not authorized to recommend node assignment without observed state from the operator. See §9.1 for the Hub Claude observability boundary.

## 4.6 Walking-skeleton-first ordering rule and walking-skeleton output canonical set

### 4.6.1 Applicability

This subsection applies to **Phase 1 only**. Phase N ≥ 2 (additive iterations) does not contain a `walking_skeleton` unit per the phase ontology established in [TPL] TDD §0.7 / §0.8 (Phase 1 vs Phase N ≥ 2 asymmetry).

### 4.6.2 Walking-skeleton-first ordering rule

Within a Phase 1 of a given app, the `walking_skeleton` unit MUST be PR-merged to `main` before any `feature` unit or `app_integration` unit of that phase starts execution.

"Starts execution" means crossing into TK-03 (per-slice interface artifacts) for `feature` units, or into TK-09 (M2 integration test execution) for `app_integration` units. Earlier Hub-side activities (TK-01 phase PRD, TK-02 phase TDD + per-feature slice-lists + node assignments) MAY proceed in parallel with walking-skeleton execution; the gate is the unit's first node-side TK, not the Hub-side specification work.

Rationale: the walking skeleton establishes the foundational architecture (`§1` of phase TDD) and the cross-feature baselines (`§2` of phase TDD) end-to-end through the CI/CD pipeline to `main`. Until walking skeleton is merged, no feature unit's slice can rely on a stable architectural foundation, and no app-integration unit has anything to integrate. Walking-skeleton is production code, not a throwaway prototype, and is shipped to the production environment via M5 in the first or second sprint of the phase. The thinnest-possible-slice principle is anchored on Cockburn 2004 *Crystal Clear* and Freeman & Pryce 2009 *Growing Object-Oriented Software, Guided by Tests*.

Violation handling: if a `feature` unit's TK-03 or an `app_integration` unit's TK-08 begins before walking-skeleton has merged to `main`, surface the violation immediately and pause the offending unit at its current TK boundary. Resume only after walking-skeleton merges. See §7 anti-drift red flags.

### 4.6.3 Walking-skeleton output canonical set

The Phase 1 walking_skeleton unit produces the following six outputs in a single PR (one PR per unit per §4.2 unit-level affinity). Output #6 is the slice's actual feature deliverable; Outputs #1–#5 are app scaffolding committed alongside #6.

| # | Output | Form | Authoritative basis |
|---|---|---|---|
| 1 | `apps/{app-slug}/CLAUDE.md` | New file | Anthropic Claude Code memory documentation: nested CLAUDE.md files in subdirectories are descendant memory files lazy-loaded when Claude reads files in those subdirectories; the file is additive over the project-root CLAUDE.md and takes precedence on conflict |
| 2 | `apps/{app-slug}/package.json` | New file | Required fields per pnpm and Node.js conventions: `name`, `version`, `private: true` (no public publishing), `engines.node` per §3.2.3 specifier strategy, and `packageManager` per §3.2 parity rule. Java apps substitute `pom.xml` or `build.gradle` per their toolchain analogue |
| 3 | `apps/{app-slug}/{src,specs,tests}/` directory skeleton | New directories with minimal placeholder files | `specs/` subtree per the phase-level path conventions established in [RULE] Claude Code Architecture Rules §Y.1 (Batch 1 frozen); `src/` tier organization per Architecture Rules tier policy; `tests/` for slice-level + integration-level test artifacts per [TPL] Test Plan Schema |
| 4 | `pnpm-workspace.yaml` registration coverage | Typically zero-line edit (the recommended `packages: ['apps/*']` glob auto-registers any direct subdirectory of `apps/` that contains a valid `package.json`); occasional one-line append if explicit listing is in use | pnpm official documentation for `pnpm-workspace.yaml`: the `packages` glob includes/excludes directories from the workspace; `apps/*` glob covers all direct subdirectories of `apps/`. For Java apps with no `package.json`, this output is N/A and an analogous Maven/Gradle multi-module registration applies instead |
| 5 | App framework configuration files | New files; framework-dependent | TypeScript + React (BFF / web) typical set: `tsconfig.json`, bundler config (Vite or equivalent), test runner config (Vitest or equivalent), lint config local override. Java apps: `pom.xml` or `build.gradle.kts` covers most analogues. Output #5 is what makes `pnpm install && pnpm build && pnpm test` (or Maven/Gradle equivalents) succeed for the app inside the monorepo |
| 6 | Walking-skeleton end-to-end runnable proof | New code (the slice's deliverable) | The thinnest end-to-end vertical slice that traverses all tiers established in [RULE] Claude Code Architecture Rules. Typical form for a tiered backend-plus-frontend app: a `GET /health` (or analogous probe) routed through every tier (BFF → API → persistence) and rendered through the frontend if applicable. The slice is built, tested, and deployed to staging through the CI/CD pipeline up to M5 per [MECH] CI/CD Milestone Policy. Production deployment is the receiving company's CI/CD responsibility after handoff per [MECH] Application Lifecycle Handoff §0.2 — the AI-dev environment does not perform production deploys. The "production code, not throwaway prototype" framing is anchored on Cockburn 2004 / Freeman & Pryce 2009 and remains valid: the walking skeleton is intended to be deployable to production via the receiving company's pipeline, not a discardable proof-of-concept |

Output #4 mechanism note: when the project root `pnpm-workspace.yaml` uses the recommended `apps/*` glob, adding a new `apps/{app-slug}/` directory with a valid `package.json` (Output #2) is sufficient for pnpm to register the new app at the next `pnpm install`; no explicit edit to `pnpm-workspace.yaml` is required. Verify glob coverage before declaring Output #4 complete; if explicit listing is in use instead, append the new entry.

The output set is the canonical reference for [MECH] Development Track Workflow §4 walking_skeleton task definition (which describes the procedural workflow to produce these outputs) and for [TPL] TDD Template §3 walking skeleton scope (which describes how the outputs are documented in a Phase 1 TDD instance).

### 4.6.4 What §4.6 does not own

- The procedural workflow that produces the six outputs (TK-by-TK steps, agent involvement, evidence collection at each milestone) — owned by [MECH] Development Track Workflow §4 walking_skeleton task definition
- The milestone subset that the walking-skeleton slice runs through (M0 → M1 → M2 → M3 → M4 → M5 full chain) — owned by [MECH] CI/CD Milestone Policy
- The Codex commands fired during walking-skeleton execution — owned by [RULE] Codex Plugin Usage
- How a Phase 1 TDD instance documents its §3 walking skeleton scope (template guidance) — owned by [TPL] TDD Template §3

---

# 5. GitHub workflow

## 5.1 Branch topology

```
main (protected)
└── feature/<app-slug>/<unit-slug> (unprotected, node-owned)
```

- `main` — the only long-lived branch in the AI-dev monorepo; production-ready code by canonical definition. Official handoff artifacts originate here (per [MECH] Application Lifecycle Handoff). M5 staging deploy fires on PR merge to `main` per [MECH] CI/CD Milestone Policy §2.6.
- `feature/<app-slug>/<unit-slug>` — node-owned working branches; one per unit (any unit_type); created by the assigned node at unit onboarding (per §6 step 4). The `feature/...` prefix is retained as the canonical namespace for all node-owned working branches regardless of unit_type; the slug segment carries the unit identity per §6.2 (`<unit-slug>` = `walking-skeleton` for the Phase 1 walking_skeleton unit; the feature-slug for `feature` units; `app-int-phase-{N}` for `app_integration` units)

**Single-branch topology rationale**: the AI-dev environment is a sole-operator workspace. A separate long-lived integration branch (`hdc/feature-development` in prior canonical versions) served multi-developer enterprise patterns where features needed staged convergence before promotion to `main`. With a single operator and rigorous per-unit milestone gating (M0–M4 per [MECH] CI/CD Milestone Policy), feature branches can merge directly to `main` after M4 review without a separate integration step. This reduces operator cognitive load (one merge ceremony instead of two) without compromising functional testing or runnability.

The `<app-slug>/<unit-slug>` form is the globally unique unit-branch identifier; `<unit-slug>` alone needs only app-internal-and-phase-internal uniqueness.

## 5.2 Branch protection settings

| Branch | PR required | CODEOWNERS | CI checks | Force push | Deletion |
|---|---|---|---|---|---|
| `main` | Yes | Suggest reviewer (sole code owner) via CODEOWNERS file; ruleset configured with admin bypass | Required | Blocked | Blocked |
| `feature/**` | No (working branches) | N/A | N/A | Permitted | Permitted (after merge) |

CODEOWNERS membership and admin bypass rules are operator-managed at the GitHub repository level. The ruleset configuration itself is mirrored in repository settings, not in canonical source body.

### Enforcement caveat — GitHub plan dependency

GitHub Free plan does not enforce rulesets on private repositories. Rulesets can be created and shown as Active in repository settings, but force pushes, PR requirements, and force-push blocks will not be hard-enforced by the platform. Rulesets become hard-enforced when the repository moves to a paid plan (GitHub Pro for personal accounts, GitHub Team for organizations) or when the repository is made public.

While on GitHub Free private:
- Ruleset configuration MUST still be created per the table above. Configuration is forward-compatible — once the plan is upgraded, enforcement activates immediately without re-configuration.
- The CODEOWNERS file MUST still be committed at `.github/CODEOWNERS`. It enables PR-creation-time reviewer suggestion regardless of plan, and is forward-compatible with team-based review enforcement once the repository moves to an organization.
- Sole owner self-discipline (operator does not bypass main protection on a whim) replaces hard enforcement during this phase.
- The "Require review from specific teams" rule (formerly "Require review from Code Owners") is not configurable on personal accounts because it requires GitHub Teams — leave it unchecked. CODEOWNERS file remains effective for suggestion.

This caveat is bounded: when the repository graduates (paid plan, organization migration, or made public), the canonical row entries above become directly enforced without revision.

## 5.3 Conflict defense — three-layer redundancy

| Layer | Mechanism | Implemented in |
|---|---|---|
| Human discipline | Operator-driven node assignment per §6; awareness of in-flight work on each node | Operator personal `MANUAL_*.md` artifacts (non-canonical, [OS] §9.4) |
| Technical layer | GitHub branch protection per §5.2 | GitHub repository settings |
| RAG soft compliance | Hub Claude trigger phrase reminders per §8 | This source §8 (RAG-retrievable chunks in Hub Claude conversations) |

No additional locking mechanism (no custom GitHub Actions, no file-based locks, no worktree coordinator script) is introduced. The three layers are deemed sufficient for a sole-decision-maker workflow.

---

# 6. Node assignment workflow

## 6.1 Four-step process

| Step | Action | Owner | Output |
|---|---|---|---|
| 1 | Decide ownership | Operator (pure human judgment) | Node assignment decision |
| 2 | Record in unit-scope-correct TDD location | Operator | For `feature` units: phase TDD `§4.{feature-slug}.Header.assigned_node`. For `walking_skeleton` units: phase TDD `§3.Walking-Skeleton-Header.assigned_node`. For `app_integration` units: GitHub Issue marker block (no per-feature TDD section exists for this unit type). Value: `dev-node-portable \| dev-node-stationary-1 \| dev-node-stationary-N` |
| 3 | Mark GitHub Issue body | Operator | HTML-comment-delimited marker block per §6.2 |
| 4 | Node onboarding | Operator (on assigned node) | `git fetch && git checkout -b feature/<app-slug>/<unit-slug>`, transfer the phase-level spec set produced at TK-01 / TK-02 (`apps/{app-slug}/specs/prd/phase-{N}.md`, `apps/{app-slug}/specs/tdd/phase-{N}.md`, `apps/{app-slug}/specs/openapi.yaml`, `apps/{app-slug}/specs/test-plan/phase-{N}.md`, plus per-feature artifacts under `apps/{app-slug}/specs/slice-list/` and `apps/{app-slug}/specs/test-plan/feature-*.yaml` for `feature` and `walking_skeleton` units), `git push -u`, start Claude Code session, begin the next pending TK appropriate to the unit_type (TK-03 for `feature` and `walking_skeleton`; TK-08 for `app_integration`) per [MECH] Development Track Workflow §4 |

GitHub native `assignee` field stays empty. The HTML-comment-delimited marker block is the canonical record on the Issue side.

**Onboarding timing**: Node onboarding (step 4) fires immediately after TK-02 sign-off in [MECH] Development Track Workflow, so that the unit's first node-side TK and all subsequent TKs execute within the same Claude Code session on the assigned node. For `feature` and `walking_skeleton` units, the chain is TK-03 (per-slice spec production) → TK-04 (M0 entry self-check + first commit + substantive code writing) → TK-05 onwards. For `app_integration` units, the chain begins at TK-08 (M2 cross-feature integration test execution) and proceeds through TK-09 → TK-10 → TK-11 → TK-12 → TK-13. The hub-to-assigned_node specs transfer is part of this onboarding step. The operator does not perform a second onboarding before the unit's first node-side TK.

**Semantic note on TDD section asymmetry across unit types**: `app_integration` units have no per-feature TDD section because their deliverables (cross-feature integration tests, NFR harness) are operationalized through phase test plans rather than per-feature engineering specs. The marker block is the single canonical record for unit-level metadata across all three unit types; TDD §3 (for `walking_skeleton`) and TDD §4 (for `feature`) sections exist additionally for unit types whose work requires foundational or feature-scoped engineering specs to be expressed in detail. Adding a TDD section for `app_integration` would create a vestigial section containing only `assigned_node`, since no other engineering content applies — the marker block already carries that field, and the unit's substantive content lives in [TPL] Test Plan Schema phase-tier and feature-tier outputs.

Hub Claude does not perform any of these four steps automatically. Hub Claude transcribes when asked but does not author or update the marker block. See §9.2.

## 6.2 GitHub Issue marker block format

The marker block is placed at the top of the GitHub Issue body, delimited by HTML comments so it is visually invisible in rendered Markdown but parseable by any tool that scans Issue bodies.

```
<!-- HDC-NODE-ASSIGNMENT -->
unit_type: walking_skeleton | feature | app_integration
unit_id: <kebab-case-stable-id>
prerequisite_units: [<unit_id>, <unit_id>] | []
assigned_node: dev-node-portable | dev-node-stationary-1 | dev-node-stationary-N
assigned_at: YYYY-MM-DD
feature_branch: feature/<app-slug>/<unit-slug>
status: assigned | in-progress | reassigned | merged | abandoned
<!-- /HDC-NODE-ASSIGNMENT -->
```

Field semantics:

- `unit_type` — one of the three values catalogued in [MECH] Development Track Workflow §4. Determines parallelism unit (§4.1), milestone profile ([MECH] CI/CD Milestone Policy), and Codex fire conditions ([RULE] Codex Plugin Usage)
- `unit_id` — kebab-case stable identifier unique within the app's Phase. Recommended naming: `walking-skeleton` for the Phase 1 walking_skeleton unit; the feature-slug for `feature` units (e.g., `time-off-request`); `app-int-phase-{N}` for `app_integration` units (e.g., `app-int-phase-1`)
- `prerequisite_units` — list of `unit_id` values that must reach `status: merged` before this unit may start node-side execution. Empty list `[]` if no prerequisites. In Phase 1, every `feature` and `app_integration` unit must include the `walking-skeleton` unit_id in its `prerequisite_units` per §4.6.2 walking-skeleton-first ordering rule. Hub Claude does not auto-populate this field; the operator records prerequisites at unit-creation time
- `feature_branch` — the GitHub branch on which the unit's work happens. Pattern remains `feature/<app-slug>/<unit-slug>` (no rename of the field name; `<unit-slug>` is the `unit_id` value); the `feature/...` prefix is retained as the branch namespace for all three unit_types to preserve compatibility with §5.1 branch topology and [MECH] Application Lifecycle Handoff §4.1 tag discipline. The "feature" prefix in the namespace is a historical name and now denotes "node-owned working branch" rather than implying the unit is a `feature` unit_type

When the unit undergoes reassignment per §6.3, additional rows are appended to the marker block — not replacing the original `assigned_node` and `assigned_at`:

```
reassigned_from: <previous-logical-node>
reassigned_at: YYYY-MM-DD
```

Multiple reassignments produce multiple appended row pairs in chronological order.

## 6.3 Reassignment protocol

Reassignment requires explicit operator declaration in a Hub Claude conversation, providing the context and rationale. Hub Claude does not initiate reassignment. The mechanical sequence (applies symmetrically to all three unit_types):

| Step | Action | Verification |
|---|---|---|
| 1 | Operator declares reassignment in Hub Claude conversation | Hub Claude transcribes the decision |
| 2 | OLD node: WIP commit + push to `feature/<app-slug>/<unit-slug>` | `git status` clean after commit |
| 3 | Operator updates GitHub Issue marker block: append `reassigned_from`, `reassigned_at`; update `assigned_node` to NEW logical name; `unit_type` / `unit_id` / `prerequisite_units` are immutable across reassignment and are not edited | Marker block reflects current state |
| 4 | NEW node: `git pull --ff-only` on the feature branch | Pull must succeed; non-fast-forward = aborted handoff, return to OLD node |

Non-fast-forward pull on step 4 indicates that the OLD node's WIP push did not complete cleanly or that the NEW node has divergent local state from a prior session. Resolve before reassignment proceeds; do not force-pull.

---

# 7. Anti-drift red flags

> **Scope and ownership**: this section is the **canonical owner** for multi-node infrastructure red flags (tool stack drift; logical role drift; tool stack scope leak; multi-node parallelism violations including same-node multi-slice without worktree isolation, slices distributed across nodes, cross-node Codex invocation; unit_type drift; GitHub workflow drift including direct push to protected branches and force push; node assignment drift). Downstream sources ([MECH] Development Track Workflow §8; [MECH] CI/CD Milestone Policy §9) reference this section rather than duplicate it. Cross-node Codex invocation is co-owned with [RULE] Codex Plugin Usage §8 (tool-co-location view) and [RULE] Workspace Topology §3.5 (anti-pattern declaration).

The following signals should trigger correction before they compound:

**Tool stack drift**:
- Node.js, Java, or pnpm version on one node diverges from the committed baseline (`.tool-versions`, `engines.node` range, or `packageManager` field per §3.2.3)
- `pnpm-lock.yaml` not committed, or CI install not using `--frozen-lockfile`
- Toolchain upgrade PR (Renovate or manual) merged while a feature is in-flight on any node, without the operator's §3.2.5 drift-handling choice recorded
- `engines.node` written as exact-pin (a single concrete version like `"N.x.y"` rather than range form `">=N.0.0 <(N+1).0.0"`) — contrary to §3.2.3 specifier strategy
- Codex plugin missing or disabled on a node currently assigned a feature
- `.claude/` directory on one node lacks subagents, skills, or hooks present on another node (single shared definition violated)

**Logical role drift**:
- TDD `assigned_node` field uses a value not present in §2.1 catalog (e.g., raw macOS hostname, machine model name, "the laptop", "the mini")
- GitHub Issue marker block missing or malformed
- `dev-node-portable` running long tasks while closed (violates §2.1 availability profile)
- A node operating with client/server asymmetry assumption (one node treated as primary and another as helper)

**Tool stack scope leak**:
- Cowork session executing a TK in the Development Track Workflow
- Dispatch invoked as part of a TK execution path
- Cross-node Codex invocation (per §3.5)

**Multi-node parallelism violations**:
- Slices belonging to the same unit (any unit_type) distributed across two nodes (violates §4.2 unit-level node affinity)
- Same-node multi-slice work sharing a single Claude Code session (worktree isolation skipped)
- A subagent instance on one node serving slices from a different node

**Unit_type drift**:
- GitHub Issue marker block carries a `unit_type` value outside the catalog defined in [MECH] Development Track Workflow §4 (e.g., a typo, a legacy "feature_only" form, an arbitrary string)
- `prerequisite_units` field missing or malformed (raw string instead of list, non-existent unit_id referenced)
- A `feature` unit's TK-03 or an `app_integration` unit's TK-08 begins before the Phase 1 `walking-skeleton` unit reaches `status: merged` (violates §4.6.2 walking-skeleton-first ordering rule)
- A Phase N ≥ 2 marker block carries `unit_type: walking_skeleton` (walking-skeleton is Phase 1 only per §4.6.1)
- `app_integration` unit attempting to span multiple phases (per Batch 1 ontology, app_integration is per-phase only)
- Walking-skeleton output canonical set (§4.6.3) partially missing in the walking-skeleton unit's PR (e.g., `apps/{app-slug}/CLAUDE.md` omitted, app skeleton dirs absent, no end-to-end runnable proof code)
- `feature_branch` field used as a unit_type signal (the `feature/...` prefix is namespace-only per §6.2; unit_type is read from the dedicated field, not inferred from the branch path)

**GitHub workflow drift**:
- Direct push to `main` (must be blocked by branch protection)
- PR merged to `main` without going through PR flow (via admin bypass on Free plan, or skipping PR entirely)
- Force push attempted on a protected branch
- Reintroduction of a long-lived integration branch (e.g., `hdc/feature-development`, `develop`, `integration`) between `feature/<app-slug>/<unit-slug>` and `main` without a canonical revision authorizing it (the single-branch topology declared in §5.1 is the canonical default)

**Node assignment drift**:
- Reassignment performed without the four-step protocol in §6.3
- Reassignment with non-fast-forward pull on the NEW node, ignored or force-resolved
- GitHub native `assignee` field used instead of the marker block

---

# 8. Hub Claude soft compliance — trigger phrases

When user phrasing in a Hub Claude conversation matches any of the following, Hub Claude SHOULD remind the user of the relevant section of this source before proceeding. Hub Claude MUST NOT auto-execute the action; surface as confirmation prompt only.

**Node assignment phrasing** → reference §6:
- "assign this to portable" / "give this to the air"
- "run this on the mini" / "let stationary-1 take this"
- "switch nodes" / "move this to the other node"
- "split this feature across nodes"

**Reassignment phrasing** → reference §6.3:
- "move this feature from <node> to <node>"
- "hand this off to the other node"
- "the portable is closed, reassign"

**Cowork / Dispatch scope-leak phrasing** → reference §3.3:
- "use Cowork to run this TK"
- "let Cowork pick up the slice"
- "send this to Dispatch"
- "have Dispatch handle the merge"

**Cross-node Codex phrasing** → reference §3.5:
- "run Codex on the other node"
- "Codex review on the mini for this portable slice"

**Tool version drift phrasing** → reference §3.2:
- "the air is on a different node version" / "the mini still has old Java" — parity violation, reference §3.2.1
- "let me just pin Node to a specific patch in engines" / "set engines.node to N.x.y exactly" — exact-pin attempt against §3.2.3 specifier strategy
- "I'll merge this Renovate PR mid-feature" / "let me upgrade Node while the slice is running" — in-flight upgrade against §3.2.4
- "skip the lockfile, just run pnpm install fresh" / "regenerate the lockfile to fix this" — undermines L1 reproducibility per §3.2.2

**Branch protection bypass phrasing** → reference §5.2:
- "let me push straight to main"
- "skip the PR for this one"
- "merge without review"

**Walking-skeleton-first ordering phrasing** → reference §4.6.2:
- "start the time-off-request feature slices now" / "begin TK-03 for this feature" — when Phase 1 walking-skeleton has not yet reached `status: merged`
- "kick off the app-integration tests now" / "start TK-09 for app-int" — when Phase 1 walking-skeleton has not yet reached `status: merged`
- "skip the walking skeleton, jump straight to features" — direct ordering rule violation

**Phase boundary parallelism phrasing** → reference §4.6 (when applicable to Phase 1 walking-skeleton ordering) and the three-scenario response below for Phase N → Phase N+1 transitions:
- "start phase N+1 PRD now" / "begin the next phase spec" / "kick off phase 2 work"
- "draft the phase 3 TDD while we're still coding phase 2"
- "let me work on phase N+1 intent/acceptance now"

Hub Claude response logic for phase-boundary phrasing requires the operator to disambiguate which scenario applies, because Hub Claude has no observation of phase state (per §9.1):

| Scenario | Trigger condition (operator-declared) | Hub Claude response |
|---|---|---|
| (A) Additive only | Phase N+1 is strictly additive over Phase N: no architecture deltas anticipated in Phase N+1 TDD §1, no foundational change to cross-feature concerns in Phase N+1 TDD §2 | No warning. Phase N+1 PRD/TDD/Intent/Acceptance work proceeds in parallel with Phase N coding/testing |
| (B) Architecture impact | Phase N+1 contains architecture deltas (TDD §1 deltas) that may trigger refactoring of Phase N work-in-flight or already-merged feature units | Soft warning: "Phase N+1 contains architecture deltas; Phase N work-in-flight may need re-verification once Phase N+1 TDD §1 lands. Continue?" — operator explicit acknowledgment recorded before proceeding |
| (C) Phase 1 walking-skeleton not yet merged | Phase N is Phase 1 and the Phase 1 `walking-skeleton` unit has not yet reached `status: merged` (per §4.6.2) | Stronger soft warning: "Phase 1 walking-skeleton not yet merged to main. Phase N+1 PRD work may proceed but no unit can start node-side execution in either phase until Phase 1 walking-skeleton merges per §4.6.2. Continue?" — operator explicit acknowledgment recorded before proceeding |

Hub Claude does not auto-classify the scenario; the operator declares which scenario applies in the same conversational turn that triggered the phrase, or Hub Claude asks. The operator's declaration plus Hub Claude's transcribed acknowledgment form the traceable record for later retrospective review.

Hub Claude reminders are conversational. The operator may override with explicit acknowledgment, but the override itself must be stated in the conversation, preserving traceability for later retrospective review.

---

# 9. Hub Claude observability boundary

## 9.1 No node state observability

Hub Claude has no observation of:
- Which unit (any unit_type) is currently in flight on which node
- Backlog of slices or units remaining on a node
- Current `git status` of any worktree
- Open Claude Code sessions on a node
- In-flight Codex review state
- GitHub Issue marker block current values, including `unit_type`, `unit_id`, `prerequisite_units`, `status`
- Phase 1 walking-skeleton current `status` (whether `assigned` / `in-progress` / `merged`)
- Which phase boundary scenario (A / B / C per §8) applies for any phase transition
- Disk, CPU, or memory pressure on any node

When the operator asks "which node should this go to," Hub Claude does not pretend to have visibility. Hub Claude states explicitly: "I don't observe node state; tell me current backlog and your availability for the next [estimated unit duration], and I can offer an analysis." If the operator does not provide that input, Hub Claude declines to recommend; the operator's pure human judgment per §6 step 1 drives.

This boundary applies broadly to any state Hub Claude cannot observe — file system content on dev nodes, in-flight Codex sessions, GitHub Issue marker state, and similar runtime conditions. When in doubt, Hub Claude asks rather than assumes.

## 9.2 What Hub Claude must not auto-do

- Update GitHub Issue marker blocks (these are operator actions; Hub Claude transcribes when asked, never authors directly)
- Infer node assignment from context (always confirm with the operator)
- Override the operator's node-assignment judgment (surface concerns as questions, not counter-decisions)
- Recommend reassignment without the operator first declaring intent

---

# 10. Workspace inception checklist

## 10.1 Purpose

Workspace inception is the **once-per-monorepo** setup that produces the project-level scaffolding and singletons required before any application exists. It establishes the foundation that subsequent walking_skeleton units (per §4.6) consume when each new app is introduced.

This § replaces the retired TK-00 + TK-00b sequence in [MECH] Development Track Workflow. After inception, the Development Track workflow begins at TK-01 (phase PRD authoring) for the first app's Phase 1; per-app physical scaffolding is owned by the walking_skeleton unit's output set per §4.6.3.

## 10.2 When inception runs

- **Once** at the establishment of the HDC monorepo
- **Operator-initiated** — no automated trigger (no cron, no CI). Execution mechanism is non-canonical and owned by the operator's MANUAL artifact per [OS] §9.4 and §10.5 below; this canonical owns the output contract only.
- **Outside any TK** — inception predates TK-01 of any app's Phase 1
- **Not repeated** — additive updates to inception outputs (e.g., introducing an additional dev node, evolving the Design System Governance) flow through the relevant downstream mechanism, not a re-run of inception

## 10.3 Inception output checklist

Each item declares its owning canonical source for content rules. Inception produces the artifact in the workspace; content correctness is governed by the owning source.

**Monorepo root scaffolding** (project root, no app yet):
- [ ] `CLAUDE.md` (project root) — content rules per [RULE] Claude Code Architecture Rules §4.1
- [ ] `package.json` (workspace root manifest) — pinned `packageManager` field per §3.1 + §3.2.3
- [ ] `pnpm-workspace.yaml` — initial workspace declaration (`apps/*`, `packages/*` globs); empty workspace at this stage
- [ ] `.tool-versions` (or equivalent toolchain manifest) — pinned per §3.1 + §3.2.3
- [ ] `.gitignore` / `.gitattributes` — operator-driven; minimal canonical concern

**`.claude/` runtime config**:
- [ ] `.claude/agents/` — 10 subagent definitions per [RULE] Claude Code Architecture Rules §5.1
- [ ] `.claude/config/context-scopes.yaml` — per [RULE] Claude Code Architecture Rules §X
- [ ] `.claude/skills/hdc-arco-enterprise-ui/SKILL.md` — per [RULE] Claude Code Architecture Rules §Z
- [ ] `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md` — per [RULE] Claude Code Architecture Rules §Z

**`specs/` folder and project-level singletons**:
- [ ] `specs/design-system.md` — DS instance per [RULE] Design System Governance; passes reviewer checklist per that source's §8
- [ ] `specs/design-system-changes/` — empty folder; populated later by per-feature change drafts per [RULE] Design System Governance §12

**Empty container folders** (no content yet):
- [ ] `apps/` — populated subsequently by walking_skeleton units per §4.6.3
- [ ] `packages/` — populated subsequently by feature-driven domain extension per [RULE] Claude Code Architecture Rules §Y.4

**GitHub repository scaffolding**:
- [ ] `main` branch established with branch protection per §5.2
- [ ] Renovate config installed per §3.2.4 (replaces the v0 manual-PR fallback once configured)

**Multi-node bootstrap**:
- [ ] At least one dev node declared per §2.2 with tool-stack parity verified per §3.2
- [ ] Cross-node SSH access established per §3.6 when more than one node operates

## 10.4 Completion criteria

Inception is complete when all items in §10.3 are present and the following hold:
- Project root CLAUDE.md passes reviewer checklist per [RULE] Claude Code Architecture Rules §4.1
- Both SKILL.md files validly formatted and discoverable by Claude Code at runtime
- `specs/design-system.md` passes reviewer checklist per [RULE] Design System Governance §8
- Toolchain pinning files match §3.2.3 specifier strategy on at least one declared dev node
- `pnpm install` succeeds at workspace root with empty `apps/*` glob
- `main` branch protection green per §5.2
- The first declared dev node passes the parity check in §3.2

Once complete, TK-01 of the first app's Phase 1 may begin (per [MECH] Development Track Workflow §4).

## 10.5 What §10 does not cover

- **Per-app physical skeleton** — `apps/{app-slug}/CLAUDE.md` hierarchy, `apps/{app-slug}/package.json`, app skeleton directories, and the new app's `pnpm-workspace.yaml` registration are produced by the first phase's walking_skeleton unit per §4.6.3, not by inception
- **Domain packages** — `packages/domain/{domain-name}/` are feature-driven extensions per [RULE] Claude Code Architecture Rules §Y.4; not part of inception
- **Phase 1 specifications** — phase PRD, phase TDD, phase test plan, feature integration test plans, slice-lists, per-slice intent / acceptance / test-plan are produced in TK-01 / TK-02 / TK-03 of the first app's Phase 1, not by inception
- **DS instance ongoing additive updates** — after inception, the `specs/design-system.md` singleton evolves through the additive-update flow defined in [RULE] Design System Governance §1.1 (per-feature plan produced in TK-02; merge at TK-13 per [MECH] Development Track Workflow); breaking updates follow [RULE] Design System Governance §12 governance. Inception establishes the initial instance only
- **Step-by-step setup procedures** — operator personal `MANUAL_<short-kebab-name>.md` artifacts under [OS] §9.4 non-canonical naming pattern hold the procedural "how to actually run these steps on this physical machine" content; this § declares the canonical output set, not the operational steps
- **Inception execution mechanism** — the conventional MANUAL artifact for inception is `MANUAL_inception.md`. Its content—including whether and how Claude Code is used to produce §10.3 outputs, executor responsibility allocation, permission modes, command sequences, and per-machine peculiarities—is non-canonical per [OS] §9.4 and outside this source's governance.
