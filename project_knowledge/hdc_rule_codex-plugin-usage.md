# [RULE] Codex Plugin Usage

- **Project**: HR Digital Cockpit
- **Document Type**: Tool Usage Specification
- **Status**: Active canonical
- **Role**: Stable tool-usage source for how OpenAI Codex plugin is invoked inside Claude Code projects for cross-model code review and task delegation, including command semantics, trigger logic, evidence path schema, review-gate defaults, and per-app invocation scope rules
- **Source Category**: Cat 4
- **Management-System Role**: Tool usage specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Supports the Development Track routing defined in the Project Operating Model. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §5 (management mechanism over ad hoc control) to sparse deliberate invocation at milestones, the review-gate default-off stance, and the output-reconciliation pattern before user presentation.
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. Codex is a CC-side review tool; Hub-CD-CC Architecture frames why CC is the workspace where second-opinion review fires.
- **Relationship to [RULE] Workspace Topology**: Co-located. Codex executes on the unit's assigned node per WT §3.5; tool stack pinning per WT §3.1 / §3.2.
- **Relationship to [RULE] Claude Code Architecture Rules**: Anchored. Codex evidence path schema sits inside CCAR §Y.1 layout; Pact pair convention `{app-slug}-bff_{domain-name}` anchors to CCAR §Y.4.
- **Relationship to [MECH] Development Track Workflow**: Anchored. Codex fires at TK-11 per DTW §4 (M4 prep code review); trigger mechanics (Manual / Auto / hook) owned by DTW §4; per-unit-type task paths (DTW §4.0) feed Codex §1.4 fire conditions.
- **Relationship to [MECH] CI/CD Milestone Policy**: Anchored. Codex invocations anchor to CI/CD-defined milestones; per-unit-type milestone profile (CI/CD §2.0) feeds Codex §1.4 fire conditions; review-gate stance owned by CI/CD §5.
- **Pairings I participate in**: P-32 (with [MECH] DTW §4.0 + [MECH] CI/CD §2.0)

## How to use this source

Use this source when:
- installing or configuring the Codex plugin in a Claude Code project
- invoking Codex commands during development work
- deciding whether to use Codex for a specific task
- troubleshooting Codex plugin behavior
- understanding the per-app and per-node scope rules that govern Codex invocation in a multi-app monorepo

Do not use this source as:
- a general Codex CLI user manual
- an OpenAI API pricing guide
- a substitute for OpenAI's own Codex documentation
- a co-location semantics reference ([RULE] Workspace Topology §3.5)
- a TK trigger specification ([MECH] Development Track Workflow §4)
- a repository layout reference ([RULE] Claude Code Architecture Rules §Y.1)

---

# 1. Position of Codex in the workspace

## 1.1 Primary role

Codex is not a primary execution environment.

Codex is a cross-model review and delegation tool invoked from within Claude Code.

Primary role:
- Second-opinion code review at M4 prep (TK-11)
- Task delegation when Claude Code benefits from a different model perspective
- Rescue operations when Claude Code is stuck

Codex outputs are consumed within Claude Code sessions; they do not replace Claude Code as the primary agentic environment. Codex review of hub specs (PRD / TDD / acceptance / test plan / intent) is not part of the canonical workflow — spec-level adversarial review is owned by the operator's Hub-side GPT-Claude cross-model review consensus loop at TK-03 sign-off per [MECH] Development Track Workflow §0.4 default operating chain. The M0 entry self-check at TK-04 start is a CC-mechanical structural check, not a Codex-invoked adversarial review.

## 1.2 Co-location with executing node

Codex plugin runs on the slice's `assigned_node` Claude Code instance, never on Hub Claude. This is mechanically forced — Codex is a Claude Code plugin, and Hub Claude does not host Claude Code; therefore Codex cannot fire from Hub Claude regardless of conversational intent.

Cross-node Codex invocation (e.g., specs written on `dev-node-portable` but Codex review fired from a separate Claude Code session on `dev-node-stationary-1`) is an anti-pattern declared in [RULE] Workspace Topology §3.5. This source does not redefine that constraint; it propagates the constraint into command-level usage rules in §3.

The co-location requirement implies a single working principle for the operator: any Codex command runs in the same Claude Code session that owns the worktree for the slice being reviewed. There is no remote-Codex pattern in HDC.

## 1.3 Per-app invocation scope

In the multi-app monorepo, Codex invocations are scoped to a single app at a time. The scope is naturally bounded by the active worktree:

- A Claude Code session executing a slice for `apps/hr-data-asset-mgmt` invokes Codex against that app's source, specs, tests, and consumed `packages/domain/{domain-name}/` packages — not against `apps/mobile-payslip` or other apps' content
- Cross-app Codex review (reviewing app-A while assigned to app-B) is an anti-pattern (§8); the operator should switch to the target app's worktree first, then invoke Codex
- A single Codex command targeting multiple apps in one invocation is not sanctioned; per-app slicing is the canonical pattern

The per-app boundary is intentional. It keeps Codex's review context coherent (one app's design choices and constraints), keeps evidence paths predictable (under the current app's `apps/{app-slug}/`), and prevents cross-app coupling that would erode the monorepo's app-level isolation.

## 1.4 Per-unit-type fire conditions

Codex commands fire under unit-type-specific conditions, derived from the unit_type catalog in [MECH] Development Track Workflow §4.0 and the per-unit-type milestone profile in [MECH] CI/CD Milestone Policy §2.0. The table below is canonical for which Codex commands fire under which unit_type.

| Unit type | `/codex:review` (M4 / TK-11) | Other Codex commands (rescue / status / result / cancel) |
|---|---|---|
| `walking_skeleton` (Phase 1 only, exactly 1 slice) | Fires (M4 in scope per §2.0) | On demand per their respective triggers |
| `feature` (any phase, 1+ slices) | Fires per slice (M4 in scope per slice) | On demand per their respective triggers |
| `app_integration` (any phase, 0 customer-facing slices) | Fires (M4 in scope per §2.0; review target is the unit's PR diff including integration test code, scenario fixtures, and NFR harness) | On demand per their respective triggers |

The table is derived rather than independently declared: M4 milestone semantics are owned by [MECH] CI/CD Milestone Policy; per-unit-type milestone profile is owned by §2.0 of that source; the Codex fire condition for each (command, milestone, unit_type) tuple is the conjunction of "command anchored to milestone" (§3.1 of this source) and "milestone applies to unit_type" (CI/CD §2.0).

**For `app_integration` units**: the M4 fire is uniform with `feature` and `walking_skeleton` units; only the **review target** differs (PR diff content reflects the unit's deliverables, not slice-level production code).

**Out of scope for this source**: when Codex commands fire MANUALLY outside the canonical milestone anchors (§3.1 enumerates non-canonical use cases like "before submitting code for external review") — these manual fires are operator-discretionary and not unit-type-conditional.

---

# 2. Installation

## 2.1 Prerequisites

- Node.js 18.18 or later (HDC follows the current Active LTS line per [RULE] Workspace Topology §3.1)
- ChatGPT subscription (any tier including free) OR OpenAI API key
- Claude Code installed and operational

## 2.2 Installation sequence

Run the following in a Claude Code session:

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/codex:setup
!codex login
/codex:setup
```

The double `/codex:setup` is intentional: first invocation triggers any required Codex CLI installation; second invocation confirms ready state.

Authenticate with ChatGPT Pro account during `!codex login`.

## 2.3 Installation scope vs invocation scope

The Codex plugin installation is **per-Claude-Code-instance** (per-node, in HDC's multi-node topology), not per-project. Each dev node in [RULE] Workspace Topology §2.1 must have the plugin installed once; the installation is shared across all projects and all apps the node executes.

Codex **invocations**, by contrast, are scoped to the active Claude Code session's worktree, which in HDC always belongs to a single app's feature branch. The invocation scope is therefore per-app at runtime, even though the installation is per-node.

Per-project configuration (model selection, reasoning effort) may be placed in `.codex/config.toml` at the monorepo root when needed. The configuration is workspace-wide, not per-app — different apps within the monorepo do not have separate Codex configurations.

---

# 3. Command reference

## 3.1 /codex:review

**Purpose**: standard read-only code review by Codex.

**When to invoke**:
- M4 Merge Decision gate (TK-11 pre-M4 evidence compilation) — primary canonical invocation; auto-triggered per [MECH] Development Track Workflow §4 TK-11
- Before submitting code for external review
- When second-opinion verification is needed

**Scope**: the active app's source and tests, plus consumed domain packages — concretely:

- `apps/{app-slug}/src/**`
- `apps/{app-slug}/tests/**`
- `packages/domain/{domain-name}/**` for domains the active app consumes per Architecture Rules §Y.4

The scope does not extend to other apps in the monorepo. Per-app scope rule per §1.3 applies.

**Output**: review report with observations and suggestions, no code changes made. Written to `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md` when invoked via TK-11. The `codex/` subdirectory under evidence is the canonical Codex evidence location declared in Architecture Rules §Y.1.

**Co-location**: runs on the slice's `assigned_node` per §1.2 and Workspace Topology §3.5.

**Per-unit-type fire conditions**: Per §1.4, `/codex:review` fires at M4 (TK-11) for all three unit types (`walking_skeleton`, `feature`, `app_integration`). Review target varies: for `feature` and `walking_skeleton` units, the target is the slice-level PR diff (production code + tests); for `app_integration` units, the target is the unit's PR diff including integration test code, scenario fixtures, and NFR harness rather than slice-level production code. Output evidence path also varies: `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md` for slice-bearing units; `apps/{app-slug}/evidence/app-int-phase-{N}/codex/codex-review.md` for `app_integration` units (which have no slice-id and use the unit_id as the evidence directory name per [RULE] Workspace Topology §6.2 unit_id semantics).

## 3.3 /codex:rescue

**Purpose**: delegate work entirely to Codex as a subagent.

**When to invoke**:
- Claude Code has failed 3 times on the same issue (per [MECH] CI/CD Milestone Policy §4)
- Specific task type where Codex has demonstrated consistent advantage
- When a fresh perspective is needed to break a loop

**Common forms**:
- `/codex:rescue investigate <issue>` — diagnostic delegation
- `/codex:rescue fix the failing test with the smallest safe patch` — targeted fix delegation
- `/codex:rescue --background <task>` — long-running background delegation

**Outcome**: Codex performs the delegated work and returns results; may create session that can be resumed later.

**Scope and co-location**: rescue invocations follow the per-app scope rule (§1.3) and the co-location rule (§1.2). A rescue command targets the active app's slice; cross-node and cross-app rescue invocations are anti-patterns per §8.

## 3.4 /codex:status

**Purpose**: check running or recent Codex jobs.

**When to invoke**:
- Verifying background job state
- Debugging Codex plugin behavior

## 3.5 /codex:result

**Purpose**: retrieve final stored output from a finished Codex job.

**When to invoke**:
- Reviewing completed background delegation output

## 3.6 /codex:cancel

**Purpose**: cancel an active background Codex job.

**When to invoke**:
- Job is looping or consuming excessive resources
- Task priorities have changed and delegation is no longer wanted

---

# 4. Review gate (experimental feature)

Review gate is an optional feature enabling automatic Codex review via Stop hook.

## 4.1 Default stance

Review gate is **disabled by default** in this project.

Reason: review gate can create long-running Claude/Codex loops that drain usage limits quickly.

## 4.2 When to enable

Enable only when all three conditions hold:
- Specific high-rigor session justifies it
- User is actively monitoring the session in real time
- Usage limits are not a concern for this session

When enabled, the review gate operates on the active assigned_node Claude Code session, not on Hub Claude (Hub Claude has no Codex plugin per §1.2). The gate does not propagate across nodes; if multiple nodes are running in parallel, each enables or disables review gate independently per §2.3 installation-scope rules.

## 4.3 How to enable

`/codex:setup --enable-review-gate`

## 4.4 How to disable

Disable after the session or when limits approach. Re-run `/codex:setup` without the flag.

---

# 5. Model and reasoning effort configuration

Model selection and reasoning effort can be tuned per invocation:

- `/codex:rescue --model <model-id> --effort <low|medium|high> <task>`

Or set project-level defaults in `.codex/config.toml`:

```toml
model = "gpt-5.4-mini"
model_reasoning_effort = "high"
```

Default posture:
- Use medium effort unless task complexity justifies high
- Use minimal or low effort for quick status checks and simple delegations

---

# 6. Cost and usage awareness

Codex usage consumes ChatGPT Pro quota (or OpenAI API credits if configured that way).

Mindfulness rules:
- Do not invoke Codex on trivial tasks (small refactors Claude Code handles well)
- Do not enable review gate on long sessions without monitoring
- Use `/codex:status` before invoking additional work to confirm nothing is stuck
- Background jobs (`--background`) can accumulate; check periodically

---

# 7. Output integration pattern

Codex outputs arrive as reviews, suggestions, or completed tasks.

Integration pattern:
1. Receive Codex output
2. Claude Code reasons about Codex findings
3. Claude Code reconciles with its own analysis
4. Claude Code presents unified recommendation to user
5. User makes decisions based on the reconciled view

Do not surface raw Codex output to user without reconciliation. The value of cross-model review comes from the synthesis, not the duplication.

**TK-11 path** (M4 review): Codex output at `apps/{app-slug}/evidence/{slice-id}/codex/codex-review.md` enters the reconciliation flow before being aggregated into the Test Evidence Report (per [MECH] CI/CD Milestone Policy §6.2).

---

# 8. Anti-drift for Codex usage

> **Scope and ownership**: this section is the **canonical owner** for Codex-tool-specific red flags (invocation pattern drift, co-location and scope drift including cross-node Codex anti-pattern, path drift). Cross-node Codex anti-pattern is the canonical declaration here and at [RULE] Workspace Topology §3.5 — both views are intentional ([RULE] WT §7 captures the multi-node infrastructure perspective; this section captures the tool-co-location perspective). Downstream sources ([MECH] Development Track Workflow §8 — which adds TK-11 step-trigger view) reference this section rather than duplicate the underlying anti-pattern.

Red flags:

**Invocation pattern drift**:
- Review gate enabled but session is unattended
- Codex invoked on tasks where Claude Code has clear advantage (e.g., architecture-aware refactoring within known codebase)
- Codex rescue used repeatedly for the same problem domain (suggests systemic Claude Code gap that should be addressed in CLAUDE.md)
- Codex output surfaced raw without reconciliation
- Background jobs accumulating without review

**Co-location and scope drift** (per §1.2, §1.3):
- Cross-node Codex invocation (mechanically impossible from Hub Claude; possible but anti-pattern between two assigned_node CC sessions on different physical machines)
- Cross-app Codex invocation: running Codex from `apps/A`'s worktree to review `apps/B`'s source — switch to app-B's worktree first
- Operator dialogue with Hub Claude requesting Codex execution — surfaces as a [RULE] Workspace Topology §8 soft-compliance-trigger-phrase pattern (specifically the "Cross-node Codex phrasing" category in WT §8); Hub Claude redirects to assigned_node CC
- Single Codex command targeting multiple apps in one invocation

**Path drift**:
- Codex output landing outside `apps/{app-slug}/evidence/{slice-id}/codex/` or `apps/{app-slug}/reports/m0/{slice-id}/`
- Pre-monorepo paths (root-level `evidence/` or `reports/`) used in command output
- TK-11 codex output not under the `codex/` subdirectory inside `evidence/{slice-id}/`
