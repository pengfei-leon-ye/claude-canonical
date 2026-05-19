# [MECH] Tools Health Cadence

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable maintenance-protocol source defining the operator-invoked tool-stack health check executed by Hub Claude on demand, including the trigger model, the execution protocol (P0 tool inventory traversal, version drift detection, CVE check, release-note review, Renovate state audit, dev-loopback startup verification, custom-plugin test verification), the quarterly report structure, and the action-item prioritization for upgrade decisions
- **Source Category**: Cat 4
- **Management-System Role**: Governance mechanism specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design).
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates as a Hub Claude–executed protocol. The protocol consumes runtime state (package.json, Dependency Dashboard content, docker compose logs, test results) and produces a maintenance report; the execution is Hub-side, the consequences (tool upgrades, Renovate PR review) are operator-driven actions in CC and on GitHub.
- **Relationship to [RULE] Workspace Topology**: Companion. WT §3 tool stack per node is the inventory authority; this source consumes that inventory in §5 and validates parity as part of §3 execution protocol steps. WT §3.2 version policy + §3.2.5 drift handling owns version specifier strategy; this source consumes those rules when detecting drift.
- **Relationship to [RULE] Claude Code Architecture Rules**: Anchored. CCAR §5 subagent roster + §X agent scopes + §Y repository layout + §Z skill loading are stable structures; this source's HDC custom-plugin verification step references CCAR §5.1's HDC ESLint plugin location at `packages/eslint-plugin-hdc/`.
- **Relationship to [RULE] Codex Plugin Usage**: Anchored. The Claude Code / Codex baseline compliance check in §3 step 7 consumes [MECH] CI/CD Milestone Policy §1.1 tooling baseline as the reference version.
- **Relationship to [MECH] Development Track Workflow**: Independent of TK orchestration. Tools Health Cadence does not insert into the TK-01 → TK-13 sequence; it operates orthogonally as a periodic maintenance event. DTW execution is paused only when a P0 / P1 action item from this protocol requires immediate intervention (e.g., critical CVE in an in-use dependency).
- **Relationship to [MECH] CI/CD Milestone Policy**: Anchored. CI/CD §1.1 tooling baseline (Claude Code version pinning + upgrade verification procedure) is the upgrade-discipline anchor; this source references CI/CD §1.1 in §3 execution step 7 (Claude Code / Codex baseline check) and consumes its upgrade procedure for the Tools Health Cadence's recommended cadence on Claude Code itself.
- **Relationship to [MECH] Code Quality Rule Set**: Companion. CQ §1-§2 declares the P0 tool stack content (eslint, typescript, prettier, vitest, gitleaks, semgrep, osv-scanner, checkstyle, pmd, spotbugs, etc.); this source's §5 P0 inventory mirrors CQ's tool stack and the execution protocol verifies each tool's currency. CQ §8.5 Renovate Governance owns the dependency-update bot configuration; this source's §3 step 6 consumes Renovate's Dependency Dashboard state.
- **Relationship to [MECH] Dev-Loopback Mode**: Anchored. The dev-loopback startup verification (§3 execution step 8) reads §6 walking-skeleton M5 acceptance assertions from [MECH] Dev-Loopback Mode and re-runs a subset locally to detect rot.
- **Relationship to [MECH] Application Lifecycle Handoff**: Inter-event. Tools Health Cadence is independent of application-level handoff timing. A handoff event does not pause Tools Health Cadence; an in-flight Tools Health Day does not block a handoff.
- **Relationship to [MECH] Canonical File Self-Audit**: Parallel mechanisms at different scopes. Canonical File Self-Audit governs canonical source content integrity; Tools Health Cadence governs runtime tool-stack integrity. The two share the "periodic self-check" pattern but operate on disjoint domains and do not cross-reference operationally.
- **Pairings I participate in**: P-49 (with [MECH] CI/CD §1.1 Claude Code baseline), P-50 (with [MECH] CQ §1 tool stack + §8.5 Renovate Governance), P-51 (with [MECH] Dev-Loopback §6 acceptance assertions), P-52 (with [RULE] WT §3 tool stack inventory)

## How to use this source

Use this source when:
- Operator wants to invoke the quarterly tool-stack health check
- A critical CVE in a known tool fires emergency-triggered cadence
- Renovate Dependency Dashboard shows accumulating major-version backlog
- Operator returns to active development after a period of inactivity (>1 month) and wants a baseline-current report
- Hub Claude detects a trigger phrase per §6 and seeks the procedural anchor

Do not use as:
- A milestone gate semantics reference ([MECH] CI/CD Milestone Policy)
- A TK-by-TK orchestration reference ([MECH] Development Track Workflow §4)
- A code quality rule set reference ([MECH] Code Quality Rule Set §1 / §2 / §5)
- A Renovate config specification ([MECH] CQ §8.5)
- A canonical file audit reference ([MECH] Canonical File Self-Audit)
- A vendor-product version comparison guide

---

# 1. Boundary and position

## 1.1 What this source owns

- The trigger model (periodic quarterly, emergency CVE, major-backlog accumulation, re-entry after inactivity) — §2
- The Hub-Claude-executable execution protocol (eleven steps from inventory traversal through report generation) — §3
- The quarterly tools health report structure — §4
- The P0 tool stack inventory across Tier 1/2 (TypeScript), Tier 3 (Java), AI-dev infrastructure, and dev-loopback — §5
- Hub Claude soft compliance trigger phrases for invocation, scope-leak prevention, and ad-hoc tool questions — §6
- Anti-drift red flags specific to maintenance cadence — §7
- The action-item prioritization scheme (P0 / P1 / P2) — embedded in §3 execution

## 1.2 What this source does not own

- The tool stack content per node ([RULE] Workspace Topology §3) — this source consumes WT §3 for its inventory in §5
- Tier-specific quality rule set ([MECH] Code Quality Rule Set §1 / §2) — this source consumes CQ §1 / §2 for tool selection within the P0 inventory
- Renovate config specification ([MECH] CQ §8.5) — this source consumes Renovate Dependency Dashboard state but does not specify Renovate config
- Claude Code version baseline and upgrade verification procedure ([MECH] CI/CD Milestone Policy §1.1) — this source consumes CI/CD §1.1 in §3 step 7
- Canonical file audit ([MECH] Canonical File Self-Audit) — that source audits canonical source text integrity; this source audits runtime tool-stack integrity
- Application-level handoff ([MECH] Application Lifecycle Handoff) — handoff timing is independent of maintenance cadence
- Specific upgrade execution (which exact version to upgrade to, which exact incompatibilities to handle) — this source generates the action item; the operator and AI subagents execute the upgrade

## 1.3 Position relative to other periodic mechanisms

| Mechanism | Cadence | Scope | This source's relationship |
|---|---|---|---|
| [MECH] Tools Health Cadence (this source) | Quarterly + emergency | Runtime tool stack integrity | Owned here |
| [MECH] Canonical File Self-Audit | T1 / T2 / T3 triggers | Canonical source content integrity | Parallel; disjoint domains |
| [MECH] Sign-Off Cleanup Policy | Audit quiescence + operator judgment + handoff prep | Multi-round-revised long-living spec artifact cleanup | Disjoint domain (spec artifacts vs runtime tools) |
| Renovate (continuous bot) | Continuous per [MECH] CQ §8.5 schedule | Dependency updates | This source consumes Renovate state in §3 step 6 |

The four mechanisms are operationally distinct and do not block each other. Concurrent firing is permitted; the operator chooses the order based on attention budget.

---

# 2. Trigger model

## 2.1 Periodic trigger

**Cadence**: once per calendar quarter, fired during the last week of the quarter's last month.

**Invocation**: the operator sends Hub Claude a message containing one of the §6 trigger phrases (e.g., "请执行季度工具健康检查"). Hub Claude recognizes the phrase, anchors to this source, and begins the §3 execution protocol.

**No automatic firing**: Hub Claude does NOT autonomously initiate the periodic cadence. The "remember to invoke once per quarter" responsibility is the operator's; the canonical mechanism owns the protocol but not the invocation schedule.

## 2.2 Emergency CVE trigger

**Condition**: a critical CVE (CVSS ≥ 9.0, or vendor-marked as "actively exploited") is announced for a P0 tool listed in §5.

**Invocation**: either:
- Hub Claude perceives the CVE via web search or referenced article and surfaces a recommendation to invoke this protocol's emergency path
- The operator initiates with a phrase such as "{tool} 有紧急 CVE,请执行紧急工具健康检查"

**Scope**: emergency-triggered execution may be a **partial protocol run** — Hub Claude executes only the steps relevant to the affected tool plus dependency-impact assessment, rather than the full eleven-step traversal. The output is a focused emergency report with action items concentrated on the CVE resolution path.

## 2.3 Major-backlog trigger

**Condition**: Renovate Dependency Dashboard accumulates ≥ 2 `framework-major` / `typescript-major` PRs unresolved for ≥ 30 days each, per [MECH] CQ §8.5 Renovate Governance.

**Invocation**: Hub Claude may surface the accumulation when discussing Renovate state and recommend invoking this protocol's full cadence (treating the accumulated backlog as the focus of the next periodic Tools Health Day).

**Scope**: full protocol run. The accumulated major backlog becomes a P0 / P1 priority cluster in the resulting action-item list.

## 2.4 Re-entry trigger (operator returns after inactivity)

**Condition**: the operator has not actively developed in the AI-dev environment for ≥ 30 days (e.g., extended leave, period of work in other domains).

**Invocation**: operator initiates with a phrase such as "我离开了一段时间,请帮我做一次工具栈健康检查". Hub Claude executes the full protocol with an added emphasis on §3 step 7 (Claude Code / Codex baseline currency) and §3 step 4 (90-day CVE retrospective extended to actual elapsed period).

**Scope**: full protocol run with extended retrospective window.

---

# 3. Execution protocol

Hub Claude executes the following eleven steps in order when invoked per §2. Each step produces an intermediate output that the operator may verify before Hub Claude proceeds; Hub Claude SHOULD present intermediate results conversationally and pause for operator acknowledgment at the natural breakpoints (after step 5 P0 inventory currency check, after step 9 self-check results, before step 10 final report).

| Step | Action | Input source | Output |
|---|---|---|---|
| 1 | List P0 tool stack current versions in the operator's environment | Operator pastes `package.json` + `pnpm-workspace.yaml` + parent `pom.xml` / `build.gradle` if applicable + `.tool-versions` if present | Inventory table: tool / declared version / actual installed version (if available) |
| 2 | Compare against prior tools-health report | `reports/tools-health/{YYYY-Q}.md` from prior quarter (operator pastes if exists; first-ever run skips this step) | Version diff table: tool / prior version / current version / change description |
| 3 | Retrieve current stable version of each P0 tool from upstream | Web search per tool's canonical release channel (npm registry, GitHub releases, Maven Central, Apache Foundation, etc.) | "Current → latest stable" table per tool |
| 4 | Retrieve known CVE summary (past 90 days, or extended per §2.4) for each P0 tool | Web search + osv.dev query + GitHub Security Advisories | CVE list per tool: CVE-ID / severity / affected versions / fixed version / status (already-resolved / pending) |
| 5 | Retrieve release notes highlights (past 90 days) for each P0 tool that has a non-trivial version delta | Web search of tool's official release notes / changelog | Highlight bullets per tool: breaking changes / new features / deprecations |
| 6 | Audit Renovate Dependency Dashboard state | Operator pastes the Dependency Dashboard issue body from GitHub | Backlog summary: security PR count + age, minor PR count, major PR count + age, lockfile-maintenance status |
| 7 | Verify Claude Code / Codex versions against [MECH] CI/CD Milestone Policy §1.1 baseline | Operator confirms current versions in use | Baseline compliance status: in compliance / drift detected / upgrade recommended |
| 8 | Verify dev-loopback startup health for at least one HDC app | Operator runs `cd apps/{app-slug}/dev && docker compose up -d` and pastes the docker compose ps + healthcheck status output | Pass / fail status per service; flag deviation from [MECH] Dev-Loopback Mode §2.3 readiness ceiling |
| 9 | Verify HDC custom ESLint plugin tests pass | Operator runs `pnpm --filter eslint-plugin-hdc test` and pastes results | Pass / fail per rule; flag any rule with broken test |
| 10 | Generate quarterly tools health report | Synthesized from steps 1-9 | Markdown report per §4 template; operator saves to `reports/tools-health/{YYYY-Q}.md` |
| 11 | Generate prioritized action items | Synthesized from steps 1-9 | Action item list per §3.1 prioritization scheme |

If any intermediate step produces an output the operator cannot supply (e.g., Renovate not yet configured per [MECH] CQ §8.5, custom ESLint plugin not yet implemented per [MECH] CQ §1.2), Hub Claude SHALL note "input unavailable" in the report rather than fabricate a result and SHALL include "set up the missing prerequisite" as an action item.

## 3.1 Action-item prioritization scheme

Action items from step 11 are categorized by priority:

| Priority | Definition | Examples |
|---|---|---|
| **P0** | Address before next development session begins | Critical CVE in actively-used dependency; security PR in Renovate Dependency Dashboard older than 14 days; Claude Code on a version below [MECH] CI/CD §1.1 baseline |
| **P1** | Schedule within current Tools Health Day's working window | Major version upgrade evaluation for a framework with breaking changes (TypeScript, React, Node.js); HDC custom plugin test failures; dev-loopback startup failures |
| **P2** | Address during current Tools Health Day if time permits; otherwise defer to next quarter | Minor / patch backlog cleanup; release-notes-driven feature adoption; lockfile-maintenance commits |

The operator decides which P1 / P2 items to execute within the current session and which to defer; the deferred items carry forward into the next quarter's report as baseline state.

## 3.2 Web search guidance for Hub Claude

When executing steps 3, 4, and 5 (which require current external information), Hub Claude SHALL:

- Query the canonical release channel for each tool, not third-party aggregators where avoidable
- For CVE queries (step 4), prefer osv.dev, GitHub Security Advisories, and the tool's own security disclosures over generic news sources
- Mark confidence and source per the operator's grounding rules — do not present version numbers or CVE-IDs without source attribution
- If a tool's canonical channel is unreachable or unclear, fall back to the operator: "I could not locate the canonical release channel for {tool}; please confirm the version you're using and I'll proceed with that as the baseline"

## 3.3 Step ordering enforcement

Steps 1-5 are sequential by dependency: step 2 needs step 1's output; step 3 builds on step 1; step 4 builds on step 1 and 3; step 5 builds on step 3. Step 6 is independent and may be parallel-executed. Steps 7-9 each require operator action (paste Renovate dashboard, confirm baseline, run dev-loopback, run plugin tests) and may be interleaved at the operator's pace. Steps 10-11 are terminal and require all prior steps complete.

Hub Claude SHOULD NOT skip ahead to step 10 / 11 if any prior step is incomplete or marked "input unavailable", except when the operator explicitly authorizes generating a partial report (e.g., "skip the dev-loopback verification this round, my docker is broken; generate the report based on what we have").

---

# 4. Report structure

The quarterly tools health report MUST follow this structure. Hub Claude generates the report in step 10 of §3, and the operator saves the file to:

```
reports/tools-health/{YYYY-Q}.md
```

where `{YYYY-Q}` is the calendar year and quarter, e.g., `2026-Q2`.

## 4.1 Mandatory sections

```markdown
# Tools Health Report — {YYYY-Q}

**Date**: {YYYY-MM-DD}
**Triggered by**: {periodic | emergency: {CVE-ID or tool} | major-backlog accumulation | re-entry after {N}-day absence}
**Protocol scope**: {full eleven-step traversal | partial: steps {list}}

## 1. P0 tool stack version inventory

| Tool | Declared version | Actual version | Latest stable | Δ semver |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 2. Version change since prior report

{If prior report exists, table of tool / prior / current / change description}
{If first-ever run, state "Baseline run, no prior report to compare against"}

## 3. CVE summary (past 90 days)

| CVE-ID | Affected tool | Severity (CVSS) | Affected versions | Fixed version | Status |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

If no relevant CVEs: state "No CVEs affecting P0 tool stack identified for the retrospective window."

## 4. Release-notes highlights (past 90 days)

| Tool | Notable change | HDC impact |
|---|---|---|
| ... | ... | ... |

## 5. Renovate Dependency Dashboard state

- Security PR backlog: {N} (oldest age: {days})
- Minor / patch PR backlog: {N}
- Major PR backlog: {N} (oldest age: {days})
- Lockfile maintenance: {last run / status}

## 6. Self-verification results

| Check | Status | Notes |
|---|---|---|
| Claude Code version vs [MECH] CI/CD §1.1 baseline | {pass / drift} | ... |
| Codex plugin version | {pass / drift} | ... |
| Dev-loopback startup ({app-slug}) | {pass / fail} | ... |
| HDC custom ESLint plugin tests | {pass / fail} | ... |

## 7. Action items

### P0 (address before next development session)
1. ...

### P1 (address within current Tools Health Day window)
1. ...

### P2 (address if time permits; otherwise defer)
1. ...

## 8. Deferred items carried forward

{Items deferred from prior report's P2 section that remain unaddressed}

## 9. Notes

{Free-form observations: emerging trends, ecosystem signals worth tracking, operator commentary}
```

## 4.2 Report storage

Reports are stored at `reports/tools-health/{YYYY-Q}.md` in the monorepo. The `reports/tools-health/` directory is canonical (committed to git).

Per [OS] §8.4 (separate stable from dynamic), the report files are dynamic instance artifacts; this canonical owns the protocol and structure, not the report contents.

## 4.3 Length discipline

The report is a reference document, not a narrative. Sections SHALL be concise:
- Tables preferred over prose
- One-line entries per item
- Hub Claude SHOULD aim for the full report to fit within 2-3 pages when rendered as Markdown

If the action item list alone exceeds 15 items, Hub Claude SHALL surface this as a signal that the cadence is being under-served (likely periodicity is too long, or prior reports' deferred items are accumulating).

---

# 5. P0 tool stack inventory

The P0 inventory is the canonical list Hub Claude traverses in §3 step 1 / step 3 / step 4 / step 5. This inventory MUST be consistent with [RULE] Workspace Topology §3 tool stack and [MECH] Code Quality Rule Set §1 / §2 selections; same-revision pairing applies per [OS] §8.5.2.

## 5.1 Tier 1 / Tier 2 (TypeScript stack)

- `node` (runtime; version policy per [RULE] WT §3.2)
- `pnpm` (workspace tooling; version policy per [RULE] WT §3.2)
- `typescript` (per [MECH] CQ §1.3)
- `eslint` + `@eslint/js` (per [MECH] CQ §1.2 preset chain)
- `typescript-eslint` / `@typescript-eslint/*` (per [MECH] CQ §1.2 preset chain)
- `eslint-plugin-react` + `eslint-plugin-react-hooks` (per [MECH] CQ §1.2)
- `eslint-plugin-jsx-a11y` (per [MECH] CQ §1.2)
- `eslint-plugin-import` (per [MECH] CQ §1.2)
- `prettier` (per [MECH] CQ §1.1)
- `vitest` (per [MECH] CQ §1.6)
- `dependency-cruiser` (per [MECH] CQ §1.4)
- `knip` (per [MECH] CQ §1.5)
- `gitleaks` (per [MECH] CQ §1.7)
- `semgrep` (per [MECH] CQ §1.8)
- `osv-scanner` (per [MECH] CQ §1.9)
- `packages/eslint-plugin-hdc/` (per [MECH] CQ §1.2 custom plugin — the in-repo plugin itself; test status verified at §3 step 9)

## 5.2 Tier 3 (Java stack)

- Java JDK distribution + version (per [RULE] WT §3.1 / §3.2)
- `spotless` + `google-java-format` (per [MECH] CQ §2.1)
- `checkstyle` (per [MECH] CQ §2.2)
- `pmd` (per [MECH] CQ §2.2)
- `spotbugs` + Find Security Bugs plugin (per [MECH] CQ §2.2)
- `error-prone` (per [MECH] CQ §2.2)
- `archunit` (per [MECH] CQ §2.3)
- `osv-scanner` (shared with Tier 1/2 per [MECH] CQ §1.9; verifies Maven / Gradle dependencies)

## 5.3 AI-dev infrastructure

- Claude Code CLI (baseline per [MECH] CI/CD Milestone Policy §1.1)
- Claude Code Remote Control (per [RULE] WT §3.1)
- Codex plugin (per [RULE] Codex Plugin Usage)
- `git` and GitHub CLI (`gh`) (per [RULE] WT §3.1)
- Docker / Docker Compose (consumed by [MECH] Dev-Loopback §2.2)

## 5.4 Dev-loopback infrastructure

- `hashicorp/vault` image (dev mode) (per [MECH] Dev-Loopback §4.3 secret manager pattern)
- Any compose service images declared in the operator's apps' `apps/{app-slug}/dev/docker-compose.yaml` (per [MECH] Dev-Loopback §2.2)

## 5.5 Inventory maintenance

When a new P0 tool is introduced into the project (e.g., new lint plugin in [MECH] CQ, new compose service in [MECH] Dev-Loopback), the corresponding subsection of this §5 SHALL be updated in the same revision per [OS] §8.5.2. Drift between this §5 inventory and the canonical sources from which it is derived is itself an anti-drift signal per §7.

---

# 6. Hub Claude soft compliance — trigger phrases

When user phrasing in a Hub Claude conversation matches any of the following, Hub Claude SHALL anchor to this source and prepare to execute the §3 protocol. Hub Claude MUST NOT begin step 1 until the operator confirms intent (an explicit confirmation such as "yes, proceed" or "go ahead").

**Periodic invocation phrasing** → reference §2.1:
- "请执行季度工具健康检查" / "season tools health check"
- "请进行 tools health day" / "do tools health day"
- "执行工具栈健康检查" / "run the tool stack health check"
- "本季度工具栈维护" / "this quarter's tool stack maintenance"
- "tools health cadence" / "工具健康周期"

**Emergency CVE invocation phrasing** → reference §2.2:
- "{tool} 有 critical CVE,请检查" / "{tool} has critical CVE, please check"
- "紧急工具健康检查 by {CVE-ID}" / "emergency tools health by {CVE-ID}"
- "{tool} 被攻破了" / "{tool} was compromised"

**Re-entry invocation phrasing** → reference §2.4:
- "我离开了一段时间,请检查工具栈" / "I've been away, please check the tool stack"
- "回来开发了,工具栈还行吗" / "back to dev, tool stack ok?"

**Backlog escalation phrasing** → reference §2.3:
- "Renovate dashboard 堆了太多 major PR" / "Renovate dashboard has too many major PRs"
- "依赖更新 backlog 满了" / "dep update backlog is full"

**Scope-leak phrasing (Hub Claude SHALL clarify scope, not auto-broaden)**:
- "顺便也检查一下 specs" → reference [MECH] Canonical File Self-Audit for canonical content audits; this source covers runtime tools only
- "顺便看一下 PRD 质量" → reference [MECH] Canonical File Self-Audit or [MECH] Sign-Off Cleanup Policy depending on intent
- "顺便准备 handoff" → reference [MECH] Application Lifecycle Handoff §2.2 readiness checklist

**Ad-hoc tool questions (do NOT trigger full protocol)**:
- "{tool} 最新版本是多少" / "what's the latest version of {tool}" — Hub Claude answers directly with a web search; surfaces "this is a snapshot, full protocol gives the action items" if the operator wants more
- "{tool} 有什么新版本" / "any new version of {tool}" — same; offers full protocol invocation if multiple tools are queried in sequence (signal of pending Tools Health Day)

Hub Claude reminders are conversational. The operator may override or scope down with explicit acknowledgment, but the override itself must be stated in the conversation, preserving traceability.

---

# 7. Anti-drift red flags

> **Scope and ownership**: this section is the **canonical owner** for Tools Health Cadence–specific red flags (skipped quarters, accumulating P2 deferred items, inventory drift, partial-protocol abuse, report-storage rot). Cross-cutting red flags whose canonical statement lives elsewhere (Renovate backlog age, Claude Code baseline drift, dev-loopback startup failure, custom plugin test failure) are referenced rather than duplicated.

Red flags that should trigger correction:

**Cadence drift**:
- Two consecutive quarters elapsed without the periodic cadence firing (≥ 6 months gap)
- Emergency CVE trigger condition met but the protocol was not invoked within 7 days
- A major-backlog trigger condition has accumulated for ≥ 2 consecutive quarters with no invocation

**Inventory drift**:
- [MECH] CQ adds a new P0 tool (e.g., new lint plugin) but §5 of this source is not updated in the same revision per [OS] §8.5.2
- [RULE] WT §3.1 / §3.2 changes a tool stack member but §5 of this source diverges
- The P0 inventory in §5 includes a tool that was removed from [MECH] CQ or [RULE] WT in a prior revision

**Protocol-abuse drift**:
- A "partial protocol" run is executed when no §2.2 / §2.3 / §2.4 condition is met (i.e., the operator skips steps for convenience rather than for principled scope reduction)
- Hub Claude proceeds past step 10 / 11 with multiple "input unavailable" markers without operator acknowledgment
- Hub Claude autonomously initiates the periodic cadence without operator invocation (the autonomous-firing prohibition in §2.1 is violated)

**Report-storage rot**:
- `reports/tools-health/` directory missing despite ≥ 1 quarterly cadence having fired
- Report files exist but missing one or more §4.1 mandatory sections
- Deferred items from prior reports accumulate beyond 2 quarters without explicit decision (defer-or-execute)

**Cross-cutting red flag projections** (canonical owners elsewhere; referenced here for execution-time detection):
- Claude Code on a version below [MECH] CI/CD Milestone Policy §1.1 baseline — canonical owner CI/CD §1.1; detected in §3 step 7
- Renovate security PR > 14 days unresolved — canonical owner [MECH] CQ §8.5; detected in §3 step 6
- Dev-loopback startup exceeds [MECH] Dev-Loopback §2.3 readiness ceiling — canonical owner Dev-Loopback §2.3; detected in §3 step 8
- HDC custom ESLint plugin tests failing — canonical owner [MECH] CQ §1.2 custom plugin; detected in §3 step 9

**Hub Claude execution drift**:
- Hub Claude generates step-3 / step-4 / step-5 content without web search citation (fabrication risk)
- Hub Claude reorders or skips §3 steps without operator authorization
- Hub Claude consolidates the report into prose form when §4.1 mandates tabular structure
