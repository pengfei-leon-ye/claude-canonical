# [MECH] Application Lifecycle Handoff

- **Project**: HR Digital Cockpit
- **Document Type**: Workflow Orchestration Specification
- **Status**: Active canonical
- **Role**: Stable source defining how an application produced by the HDC AI-driven Development Track transitions to a human development team for maintenance and enhancement at the application level — including handoff readiness criteria, content scope, mechanism, and re-entry to the AI-dev environment when an application returns for further enhancement
- **Source Category**: Cat 4
- **Management-System Role**: Workflow orchestration specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; conversation discipline rules in [OS] §7.2 apply to the Hub Claude trigger behavior in §6. Cross-source ownership map for the eight Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design).
- **Relationship to [REF] Hub-CD-CC Architecture**: This source covers application-level handoff (AI-dev → human dev team ownership transfer of a complete application). [REF] Hub-CD-CC Architecture covers tool-level topology (Hub/CD/CC three-workspace boundaries and operator-mediated flows within HDC project work). These are orthogonal handoff concerns at different lifecycle layers — the cross-tool flows operate continuously throughout AI-dev (governed by [MECH] Cross-Tool Workflow Handoff), while the application-level handoff is a one-time terminal event for an application's AI-dev period.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: Different lifecycle layer. This source governs the application-level handoff event (AI-dev → human dev team). [MECH] Cross-Tool Workflow Handoff governs the operator-mediated content flows between Hub / CD / CC during AI-dev work. Both apply during the same overall project lifecycle but to different content boundaries. Re-entry per §5 implicitly resumes [MECH] Cross-Tool Workflow Handoff flows for the new app-slug.
- **Relationship to [RULE] Workspace Topology**: Imports WT §5.1 branch topology + §5.2 branch protection. Handoff tag namespace `handoff/{app-slug}/{YYYY-MM-DD}` is intentionally distinct from WT §5.1 working-branch namespace. The handoff tag is the only canonical-recognized tag namespace at the AI-dev side; company-side release tags are out of canonical scope per §0.2.
- **Relationship to [RULE] Claude Code Architecture Rules**: Anchored. §3 content scope consumes CCAR §Y.1 paths + §5 / §X / §Z artifacts.
- **Relationship to [MECH] Development Track Workflow**: Inter-unit. Handoff is an application-level operator action, not a TK in DTW §4 sequence; re-entry (§5) re-enters DTW §4.0 unit_type catalog by starting a new Phase 1 for the returning app.
- **Relationship to [MECH] CI/CD Milestone Policy**: Application-level event after zero, one, or many M5 completions; independent of CI/CD §2.0 per-unit-type milestone semantics.
- **Pairings I participate in**: P-33 (with [RULE] WT §4.6 + [TPL] TDD §3), P-37 (with [MECH] Dev-Loopback §7)

## How to use this source

Use this source when:
- Judging whether an application has reached the maturity threshold for handoff to the human development team
- Preparing the handoff content set
- Executing the handoff event (tagging, acknowledgment, repository-side state changes)
- Bringing an application back into the AI-dev environment for further enhancement after a period of human-team stewardship
- Reviewing whether a Hub Claude conversation has drifted across handoff or re-entry boundaries

Do not use as:
- A cross-tool workflow handoff reference ([MECH] Cross-Tool Workflow Handoff — covers Hub / CD / CC operator-mediated flows within AI-dev work)
- A branch topology reference ([RULE] Workspace Topology §5)
- A TK-by-TK orchestration reference ([MECH] Development Track Workflow §4)
- A milestone gate semantics reference ([MECH] CI/CD Milestone Policy)
- A deployment / release-stage specification (deployment to the operator's working environment is operator personal layer; release-stage CI/CD on the receiving company's infrastructure is out of canonical scope per §0.2)
- A subagent definition reference (CC substantive Claude Code Architecture Rules canonical (subagent roster §5))
- A versioning scheme specification

---

# 0. Boundary and position

## 0.1 What this source owns

- Definition of the application-level handoff event: AI-dev environment to human dev team ownership transfer at the application level (an entire app-slug, not a feature, not a slice, not a tool-internal artifact)
- The maturity-threshold judgment criteria (operator judgment side) and the readiness checklist (mechanical side) that gate a handoff
- Handoff content scope: which files and artifacts must, may, and must not accompany the handoff
- Handoff mechanism: source state, transfer form, acknowledgment record
- Re-entry policy when an application returns to the AI-dev environment after human-team stewardship (§5: independent-app approach selected; merge-back approach deferred)
- Hub Claude soft compliance trigger phrases for handoff and re-entry conversations
- Anti-drift red flags specific to handoff and re-entry boundary violations

## 0.2 What this source does not own

- Cross-tool workflow handoff (Hub ↔ operator ↔ CD ↔ CC content flows during AI-dev work; owned by [MECH] Cross-Tool Workflow Handoff)
- Three-workspace topology (Hub / CD / CC boundaries and operator-mediated data flow model; owned by [REF] Hub-CD-CC Architecture)
- Branch topology, branch protection settings, GitHub Issue marker block ([RULE] Workspace Topology §5, §6)
- TK-by-TK orchestration ([MECH] Development Track Workflow §4)
- M5 milestone trigger conditions, evidence paths, completion criteria ([MECH] CI/CD Milestone Policy)
- Deployment to the operator's working environment (operator personal ops; not regulated by canonical)
- Versioning scheme (project-level versioning convention is owned outside this source)
- Subagent, skill, hook artifact definitions (CC substantive Claude Code Architecture Rules canonical (subagent roster §5), §X, §Z)
- Human dev team's internal practices, tooling, or process after handoff (out of scope; canonical ends at the handoff event)

## 0.3 Application lifecycle position

This source covers four named stages and one optional return path:

| Stage | Owner | This source's role |
|---|---|---|
| AI-dev | Operator + AI Development Track | Out of scope (governed by [MECH] Development Track Workflow + sibling sources; cross-tool flows during this stage governed by [MECH] Cross-Tool Workflow Handoff) |
| Maturity threshold | Operator judgment (§2) | **Owned**: criteria + readiness checklist |
| Handoff event | Operator action (§3, §4) | **Owned**: content scope + mechanism + acknowledgment |
| Human-dev | Human dev team | Out of scope (canonical ends at handoff event) |
| Re-entry (optional) | Operator + AI Development Track (§5) | **Owned**: policy and mechanism |

Note on "AI Development Track": throughout this source, the term refers to the full set of mechanisms under [RULE] Claude Code Architecture Rules and [MECH] Development Track Workflow — Hub Claude, the CC main loop (code-writer), the A1–A10 subagents, the Codex review plugin, the SK-F and SK-W skills, hooks, and the workflow that orchestrates them. Handoff covers the artifacts produced by all of these, not subagents alone.

Note on "application-level": throughout this source, the handoff being described is the transfer of ownership of a complete application (an app-slug under `apps/{app-slug}/`) to a human dev team. Cross-tool content flows operating continuously within AI-dev (e.g., Hub spec content reaching CC, CD visual content reaching CC) are not "handoff" in this source's sense; those are governed by [MECH] Cross-Tool Workflow Handoff.

---

# 1. Application lifecycle handoff architecture

This source covers the application-level transition from AI-dev to human-dev, plus the optional return path back to AI-dev.

```
[AI-dev]
   │
   │  features delivered M0 → M5, one or many
   │  (cross-tool flows per [MECH] Cross-Tool Workflow Handoff during this period)
   │
   ▼
[Maturity threshold] — operator judgment per §2
   │
   ▼
[Handoff event] — content + mechanism per §3, §4
   │
   ▼
[Human-dev]
   │
   │  (optional return)
   │
   ▼
[Re-entry to AI-dev] — policy per §5
```

The handoff event is application-scoped, not feature-scoped. A single application can be handed off only when the operator judges it ready as a whole, regardless of how many individual features have completed M5.

---

# 2. Handoff trigger

A handoff requires both the operator's maturity judgment (§2.1) and a mechanical readiness checklist pass (§2.2). Either alone is insufficient.

## 2.1 Maturity criteria (operator judgment)

The operator judges maturity holistically. This source does not codify maturity into a numeric score; the judgment lens is captured below as guiding questions:

- Has the application delivered the core user value the original PRD scope was scoped to?
- Has the user-facing surface area stabilized to the point that further changes are enhancement rather than foundational design?
- Are the integration points with upstream / downstream systems stable enough for human-team maintenance?
- Is the operator's continued involvement in core development an over-investment relative to the application's current value-realization phase?

A "yes" pattern across these questions signals maturity. The judgment is reversible: an application judged mature today can be returned to AI-dev later via §5 re-entry.

## 2.2 Readiness checklist (mechanical)

The following must be true at the moment a handoff event is initiated. Failures are not waivable; the handoff is paused until each item is satisfied.

| # | Item | Verification |
|---|---|---|
| 1 | At least one feature has completed M5 | [MECH] CI/CD Milestone Policy M5 evidence present in `apps/{app-slug}/evidence/**` |
| 2 | All in-flight features have either completed M5 or been explicitly canceled with a recorded decision | No feature branches under `feature/<app-slug>/**` are in M0 → M4 mid-state without an operator cancellation note |
| 3 | All `apps/{app-slug}/specs/**` artifacts (phase PRD, phase TDD, openapi, slice-list, intent, acceptance, phase test plan, feature integration test plan, slice test plan) are committed to `main` | `main` head contains the artifact set per [RULE] Architecture Rules §Y.1 |
| 4 | Evidence chain is complete for every M4-merged feature | `apps/{app-slug}/evidence/{slice-id}/` contains the digest produced at the Codex code review TK per the digest-binding rule (cross-reference [TPL] Test Plan YAML Schema `evidence_required`) |
| 5 | Domain dependencies are explicitly declared | App root `CLAUDE.md` (per Architecture Rules §4.2) lists every consumed `packages/domain/{domain-name}/` and pinned version per Architecture Rules §Y.4.5 |
| 6 | No pending Design System change requests scoped to this app | `specs/design-system-changes/` contains no `{change-id}.md` referencing this app-slug |
| 7 | Long-living hub-produced spec artifacts (phase PRD, phase TDD) for the app have been brought to sign-off form per [MECH] Sign-Off Cleanup Policy | The active `apps/{app-slug}/specs/prd/phase-{N}.md` and `apps/{app-slug}/specs/tdd/phase-{N}.md` carry a `Sign-off: v1.0 ({date})` stamp (or a `v1.X.Y` patch version derived from a prior sign-off); no in-line revision annotations of the patterns documented in Sign-Off §4.1 / §4.2 remain; no governance bookkeeping sections remain |

---

# 3. Handoff content scope

Handoff transfers **complete source state plus supporting artifacts**, not a build artifact, not a deployment package. The receiving human dev team needs everything required to understand, modify, test, and re-deploy the application from source.

## 3.1 Mandatory content

The handoff content set must include all of the following, at the `main`-branch state of the handoff tag (§4.1):

| Path pattern | Reason mandatory |
|---|---|
| `apps/{app-slug}/src/**` | Application source code (Tier 1 frontend + Tier 2 BFF) |
| `apps/{app-slug}/specs/**` | All specification artifacts (phase PRDs, phase TDDs, openapi, slice-lists, intent, acceptance, phase test plans, feature integration test plans, slice test plans) — the human team needs the design rationale and contracts, not just the code |
| `apps/{app-slug}/tests/**` | All test artifacts (unit, integration, contract, e2e, visual, accessibility, performance) — required to maintain quality on enhancement |
| `apps/{app-slug}/evidence/**` | Evidence chain for all delivered features — required for audit, regression analysis, and value-realization review |
| `apps/{app-slug}/reports/**` | App-scoped reports |
| `apps/{app-slug}/CLAUDE.md` and tier-level `CLAUDE.md` files | Architecture context and tier boundaries — readable by humans even when not used as AI control files |
| `packages/domain/{domain-name}/**` for every domain the app consumes | Domain logic, contracts, and tests on the producer side — the app cannot be maintained without its consumed domains |
| Design System code at the monorepo-level path consumed by the app's Tier 1 | Required for visual consistency on enhancement; refer to [RULE] Design System Governance for the canonical DS code location (DS code is the CC-pillar artifact in the three-way distributed DS per [REF] Hub-CD-CC Architecture §5.2) |
| `apps/{app-slug}/dev/**` | Dev-loopback orchestration (docker compose, fixtures, placeholder implementations) — required for regression rehearsal, emergency fallback, and onboarding per CC substantive Dev-Loopback Mode canonical (HANDOFF.md migration document section); P-37 retired in Phase 3 (counterparty fully migrated to CC) |
| `apps/{app-slug}/HANDOFF.md` | Placeholder migration guide — required for production-target replacement of each dev-loopback placeholder per CC substantive Dev-Loopback Mode canonical |

If a domain is consumed by the handed-off app **and** at least one other app that remains in AI-dev, the domain is included in the handoff content but a copy is also retained in the AI-dev monorepo. This source does not regulate the divergence-control mechanism between the two copies after handoff; that is a §5 re-entry concern.

**Unit-type coverage note**: the path patterns above subsume all three unit_type deliverables produced by the AI-dev environment without per-unit-type enumeration, because the canonical repository layout (per CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1)) places every unit's deliverables under `apps/{app-slug}/`:

- `walking_skeleton` unit (Phase 1 only) deliverables: the six outputs canonically enumerated in CC substantive Workspace Topology canonical (walking-skeleton 6-output set) (app-level CLAUDE.md, app `package.json`, app skeleton dirs, pnpm-workspace.yaml registration coverage, framework configs, and the walking-skeleton end-to-end runnable proof code) all land under `apps/{app-slug}/` and are subsumed by the patterns above
- `feature` unit deliverables: per-slice production code, tests, evidence, and reports — all subsumed
- `app_integration` unit deliverables: integration test code at `apps/{app-slug}/tests/integration/phase/**`, cross-feature test variants, NFR validation harness at `apps/{app-slug}/tests/nfr/**`, and the unit's evidence at `apps/{app-slug}/evidence/app-int-phase-{N}/**` — all subsumed

The `pnpm-workspace.yaml` registration entry (or its glob coverage of `apps/*` per CC substantive Workspace Topology canonical (walking-skeleton 6-output set) output #4) is implicit in the project-root content the receiving team needs alongside the app subtree; if the handoff scope filter excludes the project root, the receiving team will have to reconstruct workspace registration. Operator's transfer-form choice (§4.2) determines whether the project root is included.

## 3.2 Recommended content

The following are recommended to accompany the handoff so the receiving team understands how the code was produced. Their absence does not block handoff but reduces the team's ability to reason about the codebase.

| Path pattern | Reason recommended |
|---|---|
| `.claude/agents/**` (relevant subset) | Subagent definitions used during the app's development — explains the bias firewall and context isolation that produced the test code |
| `.claude/skills/hdc-arco-enterprise-ui/**` and `.claude/skills/hdc-wcag-accessibility-checker/**` | Skill definitions: SK-F constrained Tier 1 generation against the Arco-based Design System; SK-W is an on-demand a11y diagnostic utility (no formal WCAG target per DSG §6.3) |
| `.claude/hooks/**` (relevant subset) | Hooks that mediated state transitions during development |
| Project-root `CLAUDE.md` | Workspace-level rules referenced by the app — useful as context |
| `[RULE] Claude Code Architecture Rules` (constitutional residue), `[MECH] Development Track Workflow` (constitutional residue + Hub-internal substantive), `[MECH] CI/CD Milestone Policy` (constitutional residue), `[RULE] Workspace Topology` (constitutional residue + Hub-internal substantive), this source ([MECH] Application Lifecycle Handoff), plus CC substantive canonical files for code review tool, code quality rules, dev-loopback mode, and CC-side execution mechanics | Canonical sources that governed the production process — useful as orientation material; receiving team consults both Hub constitutional residues and the CC substantive canonical layer per the decoupled-reference model in [REF] Hub-CD-CC §5.4.4 |

The recommended content can be packaged as a single "AI-dev provenance bundle" alongside the mandatory content, or omitted by operator decision. Omission should be documented in the handoff acknowledgment record (§4.3).

## 3.3 Out of scope

The following are not transferred:

- Other apps in the monorepo (`apps/{other-slug}/**`) that are not being handed off
- Domains consumed only by other apps
- Node-level configuration (per [RULE] Workspace Topology §1.3, operator personal layer)
- Operator personal manuals (`MANUAL_*.md` per [OS] §9.4 non-canonical naming pattern)
- The operator's working-environment deployment configuration (operator personal ops)
- CD instance setup materials, CD-internal templates, CD project artifacts that did not feed CC consumption (per [REF] Hub-CD-CC Architecture §6 hub canonical scope boundary; CD-internal artifacts that did not become CC-consumable handoff bundles are not part of the application's source state)

---

# 4. Handoff mechanism

## 4.1 Source state

The handoff source state is captured by an **annotated tag on `main`** following the naming convention `handoff/{app-slug}/{YYYY-MM-DD}` (e.g., `handoff/hr-data-asset-mgmt/2026-08-15`).

The handoff tag is the **only canonical-recognized tag namespace at the AI-dev side**. The AI-dev environment does not produce release tags; release tags belong to the receiving company's CI/CD pipeline scope and are out of canonical authority per §0.2. Any tag observed in the AI-dev monorepo that does not follow the `handoff/{app-slug}/{YYYY-MM-DD}` namespace is operator-personal annotation, not canonical artifact.

Tag properties follow the same discipline as any annotated tag on `main`:

- Annotated (not lightweight) — carries creation date, tagger identity, tagging message, optional cryptographic signature
- Immutable once pushed — if a handoff is reversed before the receiving team's acknowledgment, a new handoff tag with a later date is created and the old tag is deprecated via its message; the old tag is not moved
- Signed when the operator's GPG / SSH signing key is configured (recommended; not mechanically enforced by this source)

The tagging message must include: receiving team identifier (name, contact, or unique reference), maturity-judgment summary (one to three sentences referencing §2.1), and a checklist confirmation block listing the §2.2 items as satisfied.

## 4.2 Transfer form

The handoff transfers **complete repository state at the handoff tag**, not a compiled or packaged artifact. Concrete transfer forms acceptable under this source:

- A new repository on the receiving team's git host, populated by `git clone` of the AI-dev monorepo at the handoff tag
- A repository fork with the human team granted owner role
- A tarball / zip archive of the repository state at the handoff tag, when the receiving environment requires offline transfer

When the handoff scope is a single app (typical), the transfer may include the entire monorepo state or a filtered subset using `git filter-repo` (or equivalent) to extract only the mandatory + recommended content per §3. The filter strategy is the operator's choice; this source does not codify a default.

## 4.3 Acknowledgment record

The handoff is not complete until the receiving team's acknowledgment is recorded. The acknowledgment record must include:

- Receiving team's identifier (matching the handoff tag message in §4.1)
- Acknowledgment timestamp
- Optional: receiving team's signed countersignature on the handoff tag

The acknowledgment is recorded in one of two places, operator's choice:

- The handoff tag's GitHub Release notes (when a GitHub Release is created for the handoff tag)
- A dedicated `apps/{app-slug}/handoff-record.md` file committed to `main` after acknowledgment, referencing the handoff tag

Until an acknowledgment is recorded, the application's state is "handoff initiated but not complete." This intermediate state is not a sustainable steady state; if acknowledgment is not received within an operator-defined window, either the handoff is reversed (per §4.1 deprecation flow) or the operator escalates to the receiving team.

---

# 5. Re-entry to AI-dev environment

When an application that has been handed off to a human dev team needs further enhancement that the operator chooses to deliver via the AI Development Track, it returns to the AI-dev environment under the **independent-app approach** declared in this section.

## 5.1 Selected approach: independent app

The returning application is treated as a **new app in the monorepo**, with a distinct `{app-slug}` from the original. Naming convention: `{original-app-slug}-{period-marker}` where period-marker is descriptive (e.g., `hr-data-asset-mgmt-2026q3-enhance`, `hr-data-asset-mgmt-v2-redesign`). The frozen app-slug roster (per [RULE] Architecture Rules §Y) is updated to include the new slug.

The original app's directory remains in the monorepo as a historical reference. It is not deleted. It is not modified by AI-dev work after the handoff event.

## 5.2 Mechanism

The TK sequence for the returning application starts at TK-01 (phase 1 PRD authoring) for the new app-slug. Workspace inception (project-level scaffolding + singletons) is not re-run — it was completed once at the establishment of the monorepo per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance) and the original state applies to the returning app. Re-entry begins a new Phase 1 lifecycle for the new app-slug, which carries the full unit-type partitioning per [MECH] Development Track Workflow §4.0:

- **TK-01**: produces a new phase PRD for `apps/{new-app-slug}/specs/prd/phase-1.md`. The `{new-app-slug}` is decided here per operator pure judgment (immutable once committed) and added to the frozen app-slug roster per [RULE] Architecture Rules §Y. The phase PRD's "Existing PRDs" input pattern (per [MECH] Development Track Workflow §4 TK-01 inputs) naturally includes the original app's `apps/{original-app-slug}/specs/prd/**` (which contains the original app's phase PRDs) as historical reference. The new phase PRD also implicitly carries the architectural foundation that the new app's Phase 1 walking skeleton will validate. Conditional brownfield reconstruct pre-step applies per DTW TK-01 conditional pre-step when the operator judges the original app has behavior worth preserving.
- **TK-02**: produces a new phase TDD at `apps/{new-app-slug}/specs/tdd/phase-1.md` (including §1 foundational architecture, §2 cross-feature concerns, §3 walking skeleton scope, and per-feature `§4.{feature-slug}` sub-sections) plus the paired phase test plan, per-feature integration test plans, per-feature slice-lists, and **per-unit `assigned_node` decisions for the new app's Phase 1 walking_skeleton unit, each feature unit, and any app_integration unit** per [MECH] Development Track Workflow TK-02 outputs. The new phase TDD may declare module reuse from the original app's domain dependencies. Domain consumption (per [RULE] Architecture Rules §Y.4) is independent of app identity, so the new app may consume the same `packages/domain/{domain-name}/` packages the original app consumed
- **Walking-skeleton-first ordering applies** for the new app's Phase 1: the walking_skeleton unit's PR must be merged to `main` (M5 staging deploy completion per [MECH] CI/CD Milestone Policy §2.6) before any feature unit's TK-03 or any app_integration unit's TK-08 begins, per [RULE] Workspace Topology constitutional residue §3 (walking-skeleton-first ordering rule). The new app's physical skeleton (`apps/{new-app-slug}/CLAUDE.md` hierarchy, `apps/{new-app-slug}/package.json`, skeleton directories, `pnpm-workspace.yaml` registration) is produced as part of this walking_skeleton unit's output set per CC substantive Workspace Topology canonical (walking-skeleton 6-output set) — not as a hub-side pre-step. This applies even though the original app's architecture may be very similar — the returning application is a distinct app-slug and runs its own walking skeleton to establish its own CI/CD pipeline assertion
- **TK-03 onwards**: proceed per the unit_type-specific task path defined in [MECH] Development Track Workflow §4.0 (for `feature` and `walking_skeleton` units, TK-03 → TK-11 Codex code review → TK-12 onwards per slice; for `app_integration` units, TK-08 onwards directly)

The human team's modifications during their stewardship period are **not merged back into the AI-dev monorepo**. They are reflected in the human team's repository state, which the operator may consult as additional historical reference material when authoring the new phase PRD / phase TDD, but no mechanical merge happens.

**Source state pointer for re-entry**: when re-authoring the new app's Phase 1 TDD, the operator references the following original-app artifacts as historical input (subject to the operator's judgment on each):

| Artifact | Original-app location | Re-entry usage |
|---|---|---|
| Original phase TDDs (all phases) | `apps/{original-app-slug}/specs/tdd/phase-*.md` | Architectural baseline reference; the new app's §1 may borrow heavily but is authored fresh per the new Phase 1 ontology |
| Original walking_skeleton scope (Phase 1 §3) | `apps/{original-app-slug}/specs/tdd/phase-1.md` §3 | Reference for the new walking_skeleton unit's scope (which tiers traversed, what the runnable proof exercises) |
| Original per-feature engineering specs | `apps/{original-app-slug}/specs/tdd/phase-*.md` §4.{feature-slug} | Reference for new app's `§4.{feature-slug}` sub-sections when features are evolved or carried over |
| Original test plans and evidence | `apps/{original-app-slug}/specs/test-plan/**` and `apps/{original-app-slug}/evidence/**` | Reference for regression policy and known-good behavior; the new app's tests are authored fresh |
| Original handoff-record | `apps/{original-app-slug}/handoff-record.md` (when present per §4.3) | Reference for receiving-team's known-state at handoff time (useful when human-team modifications are not visible in the AI-dev monorepo) |

## 5.3 Merge-back not sanctioned

Merge-back is not a sanctioned re-entry approach under current canonical. The independent-app approach (§5.1) is the only re-entry mechanism. If empirical evidence from re-entry experiences justifies merge-back later, this section will be revised.

---

# 6. Hub Claude soft compliance trigger phrases

## 6.1 Purpose

Hub Claude conversations frequently touch handoff and re-entry topics in informal language. The trigger phrases below are conversational signals that should activate Hub Claude's handoff-boundary clarification behavior — specifically, asking the operator to confirm intent and verify against this source's criteria before proceeding.

The trigger phrases are heuristic, not exhaustive. They prioritize precision over recall. Detection is conversational and non-blocking.

Note on disambiguation from cross-tool handoff: the phrases in this source target **application-level handoff to a human dev team**, not the cross-tool content flows (Hub → CD, Hub → CC, CD → CC) that operate continuously during AI-dev. If a conversation uses "handoff" in the cross-tool sense, Hub Claude routes to [MECH] Cross-Tool Workflow Handoff instead.

## 6.2 The six trigger phrases

When a Hub Claude conversation contains any of the following phrases or their close paraphrases (English or Mandarin / DingTalk-channel paraphrases), Hub Claude must pause and confirm before proceeding:

1. "**hand off / hand it over to** [the team / dev team / human team]" — handoff intent; check §2 readiness
2. "**give the codebase to** [team]" / "**transfer ownership to**" / "**they'll take over**" — explicit ownership-transfer intent; check §3 content scope completeness
3. "**deploy and let** [them] **maintain**" / "**ship it and** [team] **handles** the rest" — handoff-versus-deploy conflation (handoff is source-state ownership transfer, not deployment; the AI-dev side performs no production deploy — deployment is the receiving company's CI/CD action after handoff, per §0.2)
4. "**bring it back / pull it back** [into the AI-dev / our environment]" / "**re-enter** the AI-dev" — re-entry intent; check §5 independent-app approach applies
5. "**merge** [their changes / the team's work] **back into** [the AI repo / this monorepo]" — merge-back intent; flag against §5.3 deferral
6. "**they took over already** / **they're maintaining now**" used to justify a downstream action — implicit handoff-completion claim; check §4.3 acknowledgment record exists

## 6.3 Action upon detection

On detection, Hub Claude:

1. Names the trigger phrase observed (one sentence, no editorializing)
2. Asks the operator to confirm the relevant condition: §2 readiness for triggers 1-3; §5 approach for triggers 4-5; §4.3 acknowledgment for trigger 6
3. If the condition is satisfied, continues with substantive advice
4. If the condition is unmet or unclear, pauses substantive advice until the operator either confirms, defers the question, or explicitly authorizes proceeding without verification

This soft compliance is conversational, not blocking. The intent is to surface canonical boundaries during organic dialogue, not to gate every utterance.

---

# 7. Anti-drift red flags

> **Scope**: this section enumerates **application-level handoff-specific** anti-drift red flags (maturity / readiness, content scope, mechanism, re-entry, conversation). Cross-tool workflow handoff red flags are owned by [MECH] Cross-Tool Workflow Handoff. Cross-cutting red flags whose canonical statement lives elsewhere are referenced inline rather than duplicated. See [OS] §12.3 for the full anti-drift red flag ownership map.

**Maturity / readiness dimension**:
- Handoff initiated without §2.2 checklist completion
- Maturity judgment proceeding without operator awareness of §2.1 lens (e.g., a stakeholder externally pressing for handoff before the operator has formed a maturity judgment)
- M5 evidence claimed but not retrievable in `apps/{app-slug}/evidence/**`

**Content scope dimension**:
- Handoff content set missing any §3.1 mandatory item
- Domain dependency not declared in app root `CLAUDE.md` at handoff time (§3.1 item 5)
- Recommended content (§3.2) silently omitted without note in §4.3 acknowledgment record
- Handoff package conflated with a deployment package (handoff is source state, not built artifact, per §3 opening)
- Cross-tool content flows (per [MECH] Cross-Tool Workflow Handoff) treated as application-level handoff events — these are different lifecycle layers

**Mechanism dimension**:
- Handoff source state created from a branch other than `main`
- Handoff tag created as lightweight (not annotated)
- Handoff tag created without the `handoff/{app-slug}/{YYYY-MM-DD}` prefix per §4.1
- Acknowledgment record absent beyond an operator-defined window without resolution (§4.3)
- Existing handoff tag force-updated to point to a different commit (use a new dated tag instead per §4.1)

**Re-entry dimension**:
- Returning application work landing under the original `{app-slug}` instead of a new slug (violates §5.1)
- Original app directory modified by AI-dev work after handoff (violates §5.1)
- Merge-back attempted without explicit canonical revision authorizing it (violates §5.3 deferral)
- Re-entry attempting to skip walking-skeleton-first ordering for the new app's Phase 1 (e.g., starting `feature` units' TK-03 before the new app's `walking_skeleton` unit merges to `main`) on the rationale that the original app already validated the CI/CD pipeline — the walking-skeleton-first ordering rule per [RULE] Workspace Topology constitutional residue §3 (walking-skeleton-first ordering rule) applies to Phase 1 of every app-slug independently; the new app must establish its own CI/CD pipeline assertion via its own walking_skeleton

**Conversation dimension**:
- Hub Claude advises on handoff or re-entry without invoking §6 trigger phrase check
- Operator and Hub Claude proceed past a §6.2 trigger without the corresponding condition check (§6.3 step 2)
- Cross-tool workflow handoff phrases (e.g., "send the prototype to CC", "bring the CD bundle into the monorepo") misrouted to this source's §6 instead of [MECH] Cross-Tool Workflow Handoff
