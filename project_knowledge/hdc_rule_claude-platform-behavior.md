# [RULE] Claude Platform Behavior Specification

- **Project**: HR Digital Cockpit
- **Document Type**: Tool Usage Specification
- **Status**: Active canonical
- **Role**: Stable platform-behavior source for Claude.ai deliverable rendering, web search use, and source precedence logic in this project
- **Source Category**: Meta
- **Management-System Role**: Delivery-interface rule; outside L1-L5 hierarchy; admissible across all four task categories per [OS] §2.3.2; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Serves the Think, Specify, and Harvest loops by codifying Claude.ai platform behaviors that affect deliverable landing and information grounding; complements [OS] §11 format and language stance without overlapping it.
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: Companion rule for delivery-surface choices; DingTalk Format Control governs DingTalk-targeted Markdown syntax, while this source governs Claude.ai-native rendering and search behaviors
- **Pairings I participate in**: None currently (per [OS] §8.5.2 as of this revision)

## How to use this source

Use this source when:
- deciding between inline rendering, Artifact rendering, or file download for a deliverable
- deciding whether to invoke web search for a given question
- weighing canonical source authority against web search results
- locating where a given Hub Claude behavioral dimension is owned across canonical sources (§5)
- locating where a given anti-drift red flag dimension is owned across canonical sources (§6)

Do not use this source as:
- a general Claude product documentation reference
- a web research methodology handbook
- a substitute for [OS] §11 format and language stance
- a substitute for [RULE] DingTalk Markdown Format Control when the target render environment is DingTalk
- a substitute for the owner sources themselves (§5 and §6 are read-view indexes only)

---

---

# 1. Artifacts and rendering preference

## 1.1 When to prefer Artifact rendering

Prefer direct Artifact rendering when:
- the deliverable is a rendered document, diagram, or interactive widget that benefits from in-interface review
- the content is for the user's direct review and does not need to be filed, shared externally, or persisted as a canonical source
- the Artifact form factor reduces copy-paste friction for the reviewer

## 1.2 When to prefer file download

Prefer file download when:
- the deliverable will leave the conversation environment (canonical source file, handoff pack, deliverable for external stakeholders)
- the deliverable is a source-ready canonical file being generated under [OS] §8.9
- the long-draft delivery rule in [OS] §11.3 is triggered

## 1.3 Do not force download when Artifact is the better form factor

For internal review deliverables that benefit from live rendering, do not default to file download. Apply §1.1 in preference to §1.2 when the deliverable will not leave the conversation environment.

---

# 2. Web search use

## 2.1 When to search

Invoke web search when:
- information currency materially affects the answer (current state of positions, laws, regulations, product releases, vendor offerings)
- a specific real-world fact is required and is not available in project knowledge or canonical sources
- the question explicitly requires the most current information

## 2.2 When not to search

Do not search the web when:
- the question can be answered from stable knowledge already grounded in canonical sources or project knowledge base
- the question is conceptual, structural, or principle-driven rather than fact-lookup
- searching would displace or dilute canonical source logic

---

# 3. Source precedence over web

## 3.1 Consult canonical first

When canonical sources, project knowledge base, or prior chat context already cover a topic, consult them before searching the web.

## 3.2 Web results as supplementary

Treat web search results as supplementary evidence, not as authority that overrides canonical source logic. When a web result conflicts with canonical source logic, surface the conflict explicitly rather than silently resolving it.

## 3.3 Grounding discipline

When web search is used, ground the response in cited search results. Do not fabricate attribution. Respect copyright and attribution constraints.

---

# 4. Scope exclusions

This source does not define:
- which specific Claude.ai product features are available at any given time (product features change over time and are not a canonical-source concern)
- how to operate external tools outside the Claude.ai surface (Claude Code, Codex plugin, DingTalk, SuccessFactors — see their respective canonical sources or vendor documentation)
- format details for DingTalk-targeted outputs (see [RULE] DingTalk Markdown Format Control Specification)
- general format and language defaults (see [OS] §11)
- long-draft delivery thresholds (see [OS] §11.3)

---

# 5. Hub Claude behavior contract index

This section is a **navigation index**, not a rule source. It enumerates where each dimension of Hub Claude's behavioral contract is owned across the canonical set, so that a reader looking for "how should Hub Claude behave when X" can locate the owner source quickly without scanning every [RULE].

The dimensions are split by topic across multiple owner sources per [OS] §8.2 one-source-one-job rule. This index is a read view; the owner sources remain authoritative. When an owner source's § numbering changes, this index must be updated in the same revision per [OS] §8.5.3 navigation/index discipline.

## 5.1 Index table

| Behavior dimension | Owner source | Reference |
|---|---|---|
| Artifacts vs file-download rendering choice | [RULE] Claude Platform Behavior | §1 |
| Web search invocation rules | [RULE] Claude Platform Behavior | §2 |
| Canonical source precedence over web results | [RULE] Claude Platform Behavior | §3 |
| Format defaults (common Markdown, project source readability) | [OS] | §11.1, §11.2 |
| Long-draft file-delivery threshold | [OS] | §11.3 |
| Language defaults (responses in Chinese, control files in English, canonical sources in English) | [OS] | §11.4 |
| DingTalk-targeted output format profiles and allowlist | [RULE] DingTalk Markdown Format Control Specification | §2–§4 |
| Lite vs Deep response mode selection and Deep mode default structure | [OS] | §12.1 |
| Source-intent topic recognition and protocol activation | [OS] | §12.2 |
| Source-ready generation protocol (pre-generation declarations, generation pass, mechanism verification) | [OS] | §8.9 |
| Conversation discipline (continue vs new chat, one-month rule, bridge rule, promotion rule, naming convention) | [OS] | §7.2 |
| Anti-drift correction triggers (cross-cutting) | [OS] | §12 |
| Soft compliance trigger phrases — node assignment, reassignment, Cowork/Dispatch leak, cross-node Codex, version drift, branch protection bypass, walking-skeleton-first ordering phrasing, phase boundary parallelism phrasing | [RULE] Workspace Topology | §8 |
| Soft compliance trigger phrases — TK-gate skip, workspace-shift, sign-off bypass, branch model bypass | [MECH] Development Track Workflow | §9 |
| Soft compliance trigger phrases — handoff intent, ownership transfer, deploy-vs-handoff conflation, re-entry intent, merge-back intent, implicit handoff completion | [MECH] Application Lifecycle Handoff | §6 |
| Hub Claude observability boundary (no node state observation; no auto-update of GitHub Issue marker blocks; no inferred node assignment) | [RULE] Workspace Topology | §9 |

## 5.2 Index scope and limits

This index covers Hub Claude **behavioral** contract — what Hub Claude does, says, declines, defers, or surfaces during conversation. It does not cover:

- Domain judgment principles (those live in [PRIN] HR Digital Decision Design Principles and [PRIN] People Experience Design Principles per [OS] §2.3.2 admissibility rules)
- Artifact content contracts (those live in the relevant [TPL] sources)
- Development Track agent behaviors (those are downstream of Hub Claude and live in [RULE] Claude Code Architecture Rules + [MECH] Development Track Workflow)

When a behavioral dimension cannot be located in this index, the dimension is either (a) genuinely missing from the canonical set and warrants discussion under [OS] §8.6 anti-duplication before authoring a new source, or (b) misclassified by the reader as a behavioral question when it is in fact a domain judgment or artifact contract question.

---

# 6. Anti-drift red flag ownership index

This section is a **navigation index**, not a rule source. It enumerates where each cross-cutting anti-drift red flag dimension is owned across the canonical set, so that a reader looking for "which source declares the canonical statement of red flag X" can locate the owner source quickly without scanning every anti-drift section.

The anti-drift sections in the canonical set are split by topic across multiple owner sources per [OS] §8.2 one-source-one-job rule. This index is a read view; the owner sources remain authoritative. When an owner source's § numbering changes, this index must be updated in the same revision per [OS] §8.5.3 navigation/index discipline.

## 6.1 Index table

| Red flag dimension | Owner source | Reference | Local variants in |
|---|---|---|---|
| Multi-node infrastructure (tool stack drift, logical role drift, parallelism violations including same-node multi-slice without worktree isolation, GitHub workflow drift, node assignment drift) | [RULE] Workspace Topology | §7 | DTW §8 (TK-step instances); CI/CD §8 (milestone-gate view of subagent-definition divergence) |
| Cross-node Codex invocation anti-pattern | [RULE] WT constitutional residue + CC substantive Codex Plugin Usage canonical (co-owned post-Phase-3) | WT residue §6 + CC-side Codex §8 | DTW §8 (TK-04 / TK-13 trigger-time view) |
| Tier-boundary red flags (Tier 1 / 2 / 3 ownership violations; CLAUDE.md hierarchy missing; Tier 2 entirely removed) | [RULE] CCAR | §8 | CQ §10 (lint-implementation projection) |
| Bias firewall red flags (agent context scope violations; silent scope expansion; per-app context-scopes override) | [RULE] CCAR | §8 + §X.3 | DTW §8 (TK-11 test-plan.yaml patch flow); CI/CD §8 (milestone-gate view) |
| App / domain placement (DSG singleton path; custom skills location; cross-app domain duplication; domain-vs-app code placement; app-slug roster conflict) | [RULE] CCAR | §8 | DTW §8 (TK-step view) |
| Contract testing convention (`{app-slug}-bff_{domain-name}` naming; producer-consumer contract drift; consumer/producer path violations) | [RULE] CCAR | §8 (with §Y.4 conventions) | (none — DTW §8 references this owner) |
| Skill loading (SK-F not active for Tier 1; SK-W not active when applicable; skills outside Anthropic-native location) | [RULE] CCAR §Z.5 | §Z.5 | DTW §8 (TK-03 / TK-06 trigger-time view); CI/CD §8 (milestone-gate view) |
| Spec-to-implementation alignment (implementation diverging from TDD without change control; specs/design-system.md not enforced in Tier 1) | [RULE] CCAR | §8 | (none) |
| Lint-level Tier 1 / Tier 2 / Tier 3 quality (suppression rate; eslint preset chain; tsconfig strict flags; architecture lint disablement; dependency allow-list; coverage threshold; custom HDC plugin; Tier 1 visual rules drift — `hdc/no-hardcoded-token-value`, `hdc/use-arco-component`) | CC substantive Code Quality Rule Set canonical (post-Phase-3; CQ fully migrated to CC) | CC-side CQ §10 | DTW §8 (UX/a11y category references this owner); CI/CD §8 (a11y inverse-drift references) |
| DSG-policy-level governance (formal a11y CI gate without DSG §12 approval; DSG feature-branch updates outside merge path; new Tier 1 component without DSG update plan in TDD) | [RULE] Design System Governance | §12 | CI/CD §8 (milestone view); DTW §8 (TK-step view); CQ §10 (lint-rule projection) |
| Code review tool specific (invocation pattern drift; path drift; M0 review on partial spec bundle; rescue used repeatedly for same problem; cross-app invocation) | CC substantive Codex Plugin Usage canonical (post-Phase-3; Codex fully migrated to CC) | CC-side Codex §8 | (none) |
| Source governance (source duplicated instead of updated; canonical without §10 header; pairing skipped; landing rule §5.4 skipped; classification §5.5 violated; Cat 2/3/4 citing [POL]; canonical name change without grep-verify; CC-targeted file with bare cross-reference) | [OS] | §12 | (none — [OS] §12 is cross-cutting authority) |
| TK-step execution (task silently skipped; hook chain incomplete; sign-off skipped; workspace-dimension violations; intervention budget exceeded; evidence cross-contamination) | [MECH] Development Track Workflow | §8 | (none — DTW-specific) |
| Milestone-gate-specific (user review budget; execution loop hygiene including auto-repair > 3 and stuck recovery skipped; Claude Code tooling baseline; slice-size advisory; TER integrity; operator digest integrity; AI-dev / company-side boundary discipline) | [MECH] CI/CD Milestone Policy | §8 | (none — CI/CD-specific; note: Claude Code tooling baseline here is **distinct from** Node/Java/pnpm tool stack owned by WT §7) |
| Handoff (maturity / readiness; content scope; mechanism including tag namespace collisions; re-entry including walking-skeleton-first ordering for new app's Phase 1; conversation discipline) | [MECH] Application Lifecycle Handoff | §7 | (none — Handoff-specific) |
| Source-authoring neutrality | CC substantive Dev-Loopback Mode canonical (post-Phase-3; DLM fully migrated to CC) | CC-side DLM §8 | Different kind of "anti-drift" — concerns authoring the DLM source itself (brand neutrality, spec reference neutrality, milestone semantics neutrality, repository layout reference neutrality), not runtime operational red flags |

## 6.2 Index scope and limits

This index covers **cross-canonical anti-drift red flag ownership** — which canonical source owns the authoritative statement of each red flag dimension. It does not cover:

- The full enumeration of red flags within each owner source (read the owner's anti-drift § directly)
- Runtime detection mechanism (CI tooling, lint rules, agent invocation hooks — see CC substantive Code Quality Rule Set canonical for deterministic enforcement, [MECH] CI/CD Milestone Policy constitutional residue for milestone-gate enforcement at the interface contract level)
- Anti-drift severity policy (no canonical severity grading — all anti-drift red flags surface as correction prompts under [OS] §12 generic anti-drift logic)

When a red flag dimension cannot be located in this index, the dimension is either (a) genuinely missing from the canonical set and warrants discussion under [OS] §8.6 anti-duplication before authoring a new red flag, or (b) misclassified by the reader as a cross-cutting concern when it is in fact a single-source local issue (e.g., a TK-specific evidence-integrity red flag belongs to DTW §8 alone, not to a cross-cutting category).
