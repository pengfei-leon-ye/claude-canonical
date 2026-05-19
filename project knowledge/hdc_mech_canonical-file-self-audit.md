# [MECH] Canonical File Self-Audit

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable governance mechanism for canonical-source and Project Instructions (PI) quality assurance, defining the seven-dimensional self-audit applied to canonical sources and to PI upon creation or substantive revision, the three-tier trigger model that gates audit execution, the three-level severity grading with 2×2 judgment matrix, and the audit report and action plan output formats
- **Source Category**: Meta
- **Management-System Role**: Outside L1-L5 hierarchy; governance mechanism running quality oversight across the canonical source set; not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Operationalizes [OS] §8.5 consistency-check rule by replacing ad-hoc per-conversation MECE / consistency / redundancy checks with a stable canonical mechanism. Extends [OS] §8.9 source-ready generation protocol by adding a post-generation audit pass that runs against the seven-dimensional checklist defined in §3 of this source. Produces signals that map onto [OS] §12 anti-drift correction dimensions per §7.2 of this source. Applies [OS] §10 canonical source header standard as the External Coherence reference point for D2.2 checks. Applies [OS] §0.1.4 AI-consumer-RAG-optimization premise as the basis for D7 AI Consumption Value dimension.
- **Relationship to [PRIN]**: Applies [PRIN] HR Digital Decision Design Principles §5 (management mechanism over ad hoc control) and §14 (preserve ambiguity rather than fabricate resolution). Audit findings preserve ambiguity rather than invent confident answers when the canonical source itself is ambiguous.
- **Relationship to [MECH] Sign-Off Cleanup Policy**: Companion mechanism at the Meta layer. This source governs canonical-source and spec-artifact quality during active revision; Sign-Off Cleanup governs the in-place removal of process content at end-of-revision for long-living spec artifacts. The Audit-quiescence trigger in Sign-Off Cleanup §2 consumes this source's S1 / S2 severity definitions.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [MECH] Canonical File Self-Audit` header fields per [OS] §8.5.1a)

## How to use this source

Use this source as the operational baseline for:
- Auditing a canonical source after creation or substantive revision per the trigger model in §2
- Assigning severity to audit findings using the three-level scheme and 2×2 matrix in §4
- Producing an audit report and action plan in the standard output format defined in §5
- Resolving boundary questions about whether a particular quality concern falls under the seven dimensions or under another governance mechanism

Do not use this source as:
- A general-purpose document quality checker for non-canonical files (the scope is bounded to canonical sources under `/mnt/project/hdc_*.md` per §1.4)
- A replacement for [OS] §8.5 consistency-check rule (this audit operationalizes the rule; it does not supersede it)
- A replacement for [OS] §12 anti-drift corrections (audit findings of certain shapes map onto §12 signals per §7.2; the §12 catalog remains the canonical anti-drift register)
- A replacement for the source-ready generation protocol in [OS] §8.9 (the audit runs after generation; the protocol still owns the pre-generation declarations and same-pass generation discipline)
- A specification quality checker for downstream specification artifacts (PRDs, TDDs, intents, acceptances, test plans) — those artifacts have their own template-level quality discipline

---

# 0. Boundary and position

## 0.1 Owns

This source owns:
- The seven-dimensional canonical-source quality model (D1 Structural Integrity, D2 Coherence, D3 Non-Redundancy, D4 Operationalizability, D5 Soundness, D6 Rationale Transparency, D7 AI Consumption Value)
- The three-tier trigger model (T1 full audit, T2 lite audit, T3 no audit)
- The three-level severity scheme (S1 Blocker, S2 Major, S3 Minor)
- The 2×2 judgment matrix (Behavioral Impact × Centrality)
- The audit report and action plan output format conventions
- The dimension-execution sequencing rule

## 0.2 Does not own

This source does not own:
- The canonical source header standard — owned by [OS] §10
- The naming convention — owned by [OS] §9
- The consistency-check rule itself (semantic scan + static pairings) — owned by [OS] §8.5
- The anti-drift corrections catalog — owned by [OS] §12
- The source-ready generation protocol — owned by [OS] §8.9
- Cross-source pairing assignments (`P-NN`) — owned by [OS] §8.5.2 and §8.5.4 maintenance discipline
- The canonical-layer AI-consumer-RAG-optimization premise — owned by [OS] §0.1.4 (D7 in this source applies the premise as an audit dimension; the premise itself is owned upstream)
- PI's structural standard or organizational convention — operator-managed via Claude.ai project settings
- The Claude.ai project settings UI workflow for applying PI updates

## 0.3 Boundary with adjacent canonical sources

| Adjacent source | This source's relationship |
|---|---|
| [OS] §0.1.4 AI-consumer-RAG-optimization premise | Applies as D7 audit dimension. The premise declares the canonical-layer design constraint; D7 operationalizes it as a per-revision quality check |
| [OS] §8.5 consistency-check rule | Operationalizes. §8.5 says "verify consistency"; this source defines seven dimensions of consistency, gating conditions for the verification, severity grading for findings, and output structure |
| [OS] §8.9 source-ready generation protocol | Extends. §8.9 produces a canonical source via pre-generation declarations + same-pass generation; this source defines an audit that runs after generation completes and before broad use |
| [OS] §10 canonical source header standard | Consumes as reference. D2 External Coherence checks the audited source's header against §10's required fields, controlled vocabulary, and field order |
| [OS] §12 anti-drift corrections | Produces signals onto. Audit findings of certain shapes are also §12 anti-drift signals per §7.2 of this source |
| [OS] §8.5.4 pairing maintenance | Defers to. New couplings discovered during audit are escalated to §8.5.4 for pairing assignment via §8.5.1a Tier discrimination |
| [PRIN] §5 management mechanism over ad hoc control | Embodies. This source is itself a management mechanism replacing ad-hoc audit invocation |
| [PRIN] §14 preserve ambiguity rather than fabricate resolution | Implements at audit time. Findings record ambiguity as a finding rather than auto-resolving it |
| PI (system prompt; not under `/mnt/project/`) | Audits but does not own. PI structure and content are operator-managed via Claude.ai project settings; this audit surfaces quality findings against PI dimensions (adapted per §3.10) but does not define PI's structural standard |

---

# 1. Purpose and applicability

## 1.1 Purpose

Audit canonical sources after creation or substantive revision against a stable seven-dimensional quality model, surface findings at three severity levels, and produce an actionable action plan ordered by severity and modification cost.

## 1.2 Audience and consumer

**Primary consumer**: Hub Claude executing the audit. The trigger detection, dimension checks, severity grading, and output structure all run inside Hub Claude's conversation execution. The operator (Leon) is the recipient of the audit report and the executor of the action plan.

**Out of scope as consumer**: Claude Code instances in Development Track repositories. CC does not consume hub canonical sources directly (per [OS] §1.4 visibility boundary); audit findings about hub canonical sources do not propagate into CC unless the operator manually inlines them into CC-readable files.

## 1.3 Applicability scope

In scope:
- All canonical sources under `/mnt/project/hdc_*.md` (the seven prefix families per [OS] §9.2: `os`, `prin`, `pol`, `tpl`, `ref`, `rule`, `mech`)
- Both new canonical source creation and substantive revision to existing canonical sources
- Project Instructions (PI) as configured in the Claude.ai project settings. Although PI is not stored under `/mnt/project/`, it sits in the three-layer harness (UP > PI > PK) as the project-level instruction layer that shapes Hub Claude behavior with effect comparable to a canonical source. PI is therefore subject to this audit when substantively revised or when explicit audit is requested.

Out of scope:
- User Preferences (UP) — operator's account-level harness that crosses projects
- Non-canonical operational artifacts (`MANUAL_*.md` and other patterns registered in [OS] §9.4)
- Specification outputs (PRDs, TDDs, intents, acceptances, test plans) — these have their own template-level quality discipline
- Claude Code skill and subagent definition files (`.claude/skills/*/SKILL.md`, `.claude/agents/*.md`) — governed by [RULE] Claude Code Architecture Rules §5 and §Z
- Working artifacts in conversation that have not been promoted to canonical via [OS] §8.9 protocol

---

# 2. Trigger model

## 2.1 Three-tier trigger structure

The audit fires automatically when Hub Claude creates or modifies a canonical source. Auto-firing is graduated across three tiers, calibrated so that the audit effort scales with the magnitude and risk profile of the modification.

| Tier | Audit strength | Dimensions activated |
|---|---|---|
| **T1 Full** | Complete seven-dimensional audit | D1, D2, D3, D4, D5, D6, D7 |
| **T2 Lite** | Three-dimensional audit | D2, D4, D7 |
| **T3 None** | No audit fires | — |

D2, D4, and D7 are the T2-active triplet: D2 (Coherence) catches terminology drift and cross-reference rot that minor edits commonly introduce; D4 (Operationalizability) catches inadvertent introduction of ambiguity through rewording; D7 (AI Consumption Value) catches motivation/derived-content accretion that minor "clarification" edits commonly slip in. D1, D3, D5, D6 are structurally insensitive to small edits and do not need to fire on T2-magnitude changes.

## 2.2 Trigger condition table

| Modification kind | Tier |
|---|---|
| Creating a new canonical source | T1 |
| Adding or removing a rule (any rule at any level) | T1 |
| Modifying precedence, scope, or authority declarations | T1 |
| Adding or removing a `#` or `##` section | T1 |
| Modifying terminology that is cross-referenced from another canonical source | T1 |
| Modifying examples, rationale text, or explanatory prose without changing rule semantics | T2 |
| Restructuring or expanding rationale without changing rules | T2 |
| Adding clarifying / motivating / contextual prose without changing rule semantics | T2 (D7 specifically catches whether the addition is AI-consumed or operator-readability scaffolding) |
| Typo correction, formatting normalization, whitespace adjustment, pure wording polish without semantic change | T3 |
| Operator declares PI has been substantively revised (any of: adding/removing a canonical-source pointer in PI's enumeration, changing precedence/conflict logic, modifying role definition, modifying boundaries, modifying automatic-activation list, modifying response-mode framing, modifying grounding rules), OR operator explicitly requests PI audit | T1 |
| Operator declares PI typo correction, formatting normalization, or wording polish without semantic change | T3 |
| Operator explicitly requests audit of one or more canonical sources without prior modification | T1 |

**PI trigger asymmetry note**: PI's trigger model differs from canonical sources in detection mechanism. Hub Claude cannot detect cross-session PI changes by inspecting file mtime or comparing against a prior version, because PI lives in the system prompt and is loaded fresh at session start with no diff history. The PI trigger therefore relies on operator declaration — operators should explicitly state "PI has been revised" or "audit PI" when invoking the audit.

## 2.3 Auto-trigger discipline

When a T1 or T2 trigger condition is satisfied, Hub Claude executes the audit automatically without asking the operator whether to skip. The audit is not optional.

- An audit pass adds turns to the conversation. The mechanism is calibrated on the principle that canonical source quality matters more than per-turn velocity, because canonical sources are consumed across every subsequent conversation in the Project.
- Even when the operator is in a fast-iteration mode, T1/T2 conditions trigger the audit. If the operator does not want an audit, the path is to make a T3-class modification, not to request audit skip.

## 2.4 Blocker handling escalation

When a T1 audit produces an S1 Blocker finding, Hub Claude pauses delivery of the canonical source and surfaces the Blocker to the operator before the source is considered usable. The pause is automatic.

Pause semantics:
- The generated canonical source file may exist in `/mnt/user-data/outputs/` after generation completes, but Hub Claude flags it as "blocker-pending" in the audit report
- The operator's path forward is to (a) accept the Blocker and revise the source in the same turn, (b) downgrade the Blocker with explicit justification, or (c) defer Blocker resolution to a follow-up turn with explicit acknowledgment of the temporary inconsistency

When a T1 audit produces only S2 or S3 findings, no pause occurs. The audit report is delivered alongside the canonical source, and the action plan is produced as normal.

---

# 3. The seven audit dimensions

## 3.1 Dimension catalog

| # | Dimension | Primary question | Independent of |
|---|---|---|---|
| **D1** | Structural Integrity (MECE) | Are the source's sub-section categories Mutually Exclusive and Collectively Exhaustive? | D3 (D1 is about taxonomic structure; D3 is about rule content) |
| **D2** | Coherence | Are claims, terminology, cross-references, and precedence declarations internally consistent and externally aligned? | D6 (D2 is about agreement among rules; D6 is about whether each rule explains itself) |
| **D3** | Non-Redundancy | Are there duplicate rules, authority overlap, or concept-drift restatements? | D1 (D3 is about rule semantic duplication regardless of structural location); D7 (D3 catches rule-semantic duplication; D7 catches derived-view duplication) |
| **D4** | Operationalizability | Can two readers apply each rule to the same scenario and reach the same answer? | D6 (D4 is about consistent application; D6 is about generalization to novel cases) |
| **D5** | Soundness | Does each rule serve a justified purpose? Are side effects acknowledged? | D6 (D5 is whether the rule should exist; D6 is whether the file says why) |
| **D6** | Rationale Transparency | Are load-bearing rules' rationales stated, not just implied? | D4, D5 (see independence notes) |
| **D7** | AI Consumption Value | Does each content unit drive AI behavior at retrieval time, per [OS] §0.1.4? | D3 (D7 catches non-AI-consumed content; D3 catches semantic duplication) |

The dimensions are independent in the sense that a source can fail any one while passing the other six.

## 3.2 D1 Structural Integrity (MECE)

### 3.2.1 Definition

D1 checks the source's own sub-section taxonomy for two structural properties:
- **ME (Mutually Exclusive)**: no two sub-sections cover the same topical area at the same level of decomposition
- **CE (Collectively Exhaustive)**: typical scenarios within the source's stated scope are covered; no critical coverage gap exists

D1 is taxonomic, not semantic. It asks "is the file's outline structure clean", not "do the rules say redundant things" (the latter is D3).

### 3.2.2 Check clauses

For ME:
- Examine each pair of sibling sub-sections (same parent, same level). Do their topical areas overlap?
- Examine cross-level relationships. Does a sub-section at one level partially restate a sibling at a different level?

For CE:
- Within the source's stated scope (declared in the header `Role` field and `How to use this source` section), enumerate the typical scenarios a reader would expect to find addressed
- For each typical scenario, verify there is a sub-section that owns it
- Specifically check known-difficult cases: source retirement, source split/merge, exceptions to default behavior, transitions between scopes

### 3.2.3 Failure modes D1 catches

- Two `##` sub-sections cover overlapping topical areas (ME violation, structural)
- A typical scenario within the source's stated scope is unaddressed (CE gap)
- A sub-section is at the wrong level of decomposition relative to its siblings (level mismatch)
- A sub-section's title promises coverage broader or narrower than its content delivers

### 3.2.4 Distinction from D3

D1 is structural: it asks whether the file's outline (sub-section taxonomy) is clean. D3 is content: it asks whether the file contains semantically duplicate rules regardless of where they are structurally located.

A finding belongs to D1 when its locus is the file's outline (two sibling sub-sections cover the same area). A finding belongs to D3 when its locus is rule semantics (two rules say the same thing, possibly in distant sub-sections).

## 3.3 D2 Coherence

D2 splits into two sub-dimensions:

### 3.3.1 D2.1 Internal Coherence

**Definition**: Within the source, claims, terminology, cross-references, and precedence declarations are mutually consistent.

**Check clauses**:
- Terms used consistently throughout the source carry the same meaning across uses
- Cross-references (`§4.2`, `§X.Y`, etc.) resolve to existing sections and the cited content matches the citing claim
- Precedence and conflict-resolution declarations are mutually consistent (no rule pair lacks a precedence declaration when overlap is plausible)
- Bidirectional reference symmetry — when this source declares "see §X for Y" and §X itself promises to define Y, the §X content delivers Y
- **Casing-and-form variant grep coverage**: when an audit involves grep-verifying that a token, identifier, or term has been introduced/renamed/removed consistently across this source, the grep must cover all casing and form variants where Hub Claude or Claude Code would treat the variants as semantically equivalent. Examples: snake_case + kebab-case + space-separated variants of a vocabulary token; singular + plural forms; identifier + prose-noun forms.

**Failure modes D2.1 catches**:
- A term defined in §1 is used in §5 with a drifted meaning
- A cross-reference `§4.2` points to a sub-section that has been renumbered or whose content no longer matches the citing claim
- Two rules apply to overlapping situations without precedence declared
- A precedence rule says "prefer §X" but §X's content actually defers to §Y, creating circular precedence

### 3.3.2 D2.2 External Coherence

**Definition**: Across canonical sources, terminology, scope/authority boundaries, and cross-source references are aligned.

**Check clauses**:
- Terms used in this source that are defined in another canonical source carry the same definition
- Scope and authority boundaries declared in this source's header match the boundaries implied by other sources that reference this one
- Cross-source references resolve to existing sources and sections, with content matching the citing claim
- Where this source claims to own a concept, no other canonical source claims to own the same concept (anti-conflict on ownership)
- Header field conformance to [OS] §10 canonical source header standard, including [OS] §10.4 controlled vocabulary (Document Type, Status, Role first word)
- **Numeric-assertion-vs-authoritative-table consistency**: when an explanatory note inside this source asserts a count, size, or quantity that is also derivable from an authoritative table or registry elsewhere, the two values are verified for consistency. The source's `Pairings I participate in` header field (count and IDs) is verified against the authoritative pairing table at `[OS] §8.5.2`.

**Failure modes D2.2 catches**:
- Cross-source reference to a renamed or restructured target (citation rot)
- Term drift between this source's usage and the owning source's definition
- Two canonical sources both claim authority over the same concept without a resolved precedence
- Header `Document Type`, `Status`, or `Role first word` field uses a value not in the [OS] §10.4 controlled vocabulary
- Required header fields per [OS] §10.1 are missing

## 3.4 D3 Non-Redundancy

### 3.4.1 Definition

No semantically duplicate rules exist within the source or across canonical sources, regardless of where they sit structurally.

### 3.4.2 Check clauses

- Within the source: each rule's semantic content is distinct from every other rule's semantic content. Rules that say the same thing in different words count as duplicates
- Across sources: this source does not duplicate rule content already owned by another canonical source
- Across sources: this source does not claim authority that another canonical source already owns (authority overlap)
- Concept-drift restatement: a rule that "rephrases" another rule with slightly different wording but no new substantive content is still a duplicate

### 3.4.3 Failure modes D3 catches

- Two rules in different sub-sections of the same source say the same thing using different phrasing
- A rule in this source duplicates a rule in another canonical source
- This source's stated authority overlaps with another canonical source's stated authority
- A rule begins as a clarification of an earlier rule but, through revision, has drifted into a near-restatement

### 3.4.4 Distinction from D1 and D7

D1 (structural) vs D3 (semantic content): a finding where two siblings overlap in topical scope is D1; a finding where two rules say the same thing is D3.

D3 (rule-semantic duplication) vs D7 (derived-content non-AI-consumed): D3 catches the case where two rules state the same rule semantics. D7 catches the case where content is a derived view of an authoritative source (count, statistics, restated boilerplate of a rule owned elsewhere) — the content is not a rule, it's a re-expression that adds no AI behavioral signal. A finding where a rule is restated in two places is D3; a finding where a derived count or status snapshot exists alongside the authoritative table is D7.

## 3.5 D4 Operationalizability

### 3.5.1 Definition

Each rule can be applied to a concrete scenario, and two independent readers applying the rule to the same scenario reach the same answer.

### 3.5.2 Check clauses

- **Two-readers test**: for each rule, mentally simulate two readers applying it. If they would reach different answers on a typical scenario within the rule's scope, the rule fails operationalizability
- **Agreeable-language scan**: identify language like "appropriate", "reasonable", "substantial", "material" without operational anchors. Such language sounds principled but fails the two-readers test
- **Decision rubric for gray areas**: where a rule explicitly acknowledges judgment is required, does it provide a decision rubric (a structured list of considerations) rather than pretending a single mechanical answer exists?
- **Boundary examples (case law)**: for the rule's important decision boundaries, does the source provide concrete compliant / non-compliant example pairs?

### 3.5.3 Failure modes D4 catches

- A rule uses agreeable language that sounds principled but offers no operational anchor
- A judgment-required rule states no decision rubric
- A rule with important boundary cases provides no example pairs
- A rule's worded scope is broader than the operational discrimination the rule actually offers

## 3.6 D5 Soundness

### 3.6.1 Definition

Each rule serves a justified purpose traceable to a User Preferences (UP) or Project Instructions (PI) objective. Side effects are acknowledged. The rule's existence is necessary, not ornamental.

### 3.6.2 Check clauses

- **Purpose traceability**: for each rule, can its purpose be traced back to a UP or PI objective?
- **Necessity test**: would the absence of this rule cause an observable downstream failure — an enforced gate going un-enforced, a cross-reference becoming unresolvable, paired sources drifting apart, or Hub Claude producing inconsistent behavior across similar conversations — or is the rule prescribing behavior that would happen anyway?
- **Side-effect disclosure**: where a rule plausibly has known side effects (e.g., raising friction, slowing iteration, creating dependencies), does the source acknowledge them?
- **Mechanism-fatigue check**: is this rule's addition to the canonical set likely to interact with existing mechanisms in a way that produces audit-fatigue, governance overhead, or rule density beyond the [OS] §8.5.7 thresholds?

### 3.6.3 Failure modes D5 catches

- A rule whose purpose cannot be traced upstream — the rule "feels right" but no UP/PI driver justifies it
- A rule that would be true by default — it prescribes behavior Hub Claude would do without the rule
- A rule whose known side effects are not acknowledged in the source
- A new rule that pushes the canonical set toward §8.5.7 re-architecture thresholds without commensurate operational return

## 3.7 D6 Rationale Transparency

### 3.7.1 Definition

Load-bearing rules state their rationale in the text. Rules' purposes are exposed to Hub Claude, not merely implied.

### 3.7.2 Check clauses

- **Load-bearing rationale presence**: for each rule that other rules depend on, or that is cited from another canonical source, is the rationale stated in 1-2 sentences alongside the rule?
- **Hard rule vs principle distinction**: does the source distinguish between hard rules (high-stakes, bright-line; rationale less critical because behavior is binary) and principles (lower-stakes; rationale critical because Hub Claude must generalize to novel cases)?
- **Generalization support**: where Hub Claude may face a situation the rule does not directly cover, does the stated rationale provide enough basis for sensible extrapolation?
- **Distinction from D5**: D5 checks whether the rule *has* a justified purpose (audit-side determination); D6 checks whether the rule *exposes* its purpose in the text (content-side observation).

### 3.7.3 Failure modes D6 catches

- A load-bearing rule stated as a bare imperative with no rationale ("Do not X")
- A short-bullet rule that would benefit from 1-2 sentences of explanation but has none
- A rule that mixes hard-rule semantics (must always X) with principle semantics (generally X) without distinguishing
- A rule whose rationale, once examined, would actually suggest a different rule formulation

### 3.7.4 Distinction from D7

D6 asks whether a rule's rationale is **stated in the text for AI retrieval at decision time**. D7 asks whether a content unit **drives AI behavior at retrieval time at all**.

A rationale stated alongside a load-bearing rule is consumed by Hub Claude when applying or justifying the rule → D6-positive, D7-positive (the rationale drives behavior).

A "Why X exists" subsection placed after the rule definition, explaining the historical motivation for the rule's inclusion in the canonical set, that the AI does not retrieve at rule-application time → D6-positive (rationale is present) but D7-negative (the rationale serves authoring-time historical record, not retrieval-time decision).

**Practical test**: if the rationale would be cited by Hub Claude when explaining or applying a rule to the operator at runtime → keep (D6 + D7 both positive). If the rationale only exists to explain to a future canonical author "why we added this rule" → migrate to git commit history or to a dedicated [TPL] ADR Spec instance (D7-negative).

## 3.8 D7 AI Consumption Value

### 3.8.1 Definition

Each content unit in the canonical source drives AI behavior at retrieval time. Content that does not — derived statistics, derived counts, restated boilerplate of rules owned elsewhere, "Why X exists" motivation sub-sections, historical status snapshots that are superseded, decorative meta-text, operator-navigation tables, summary closures — is a deletion candidate regardless of whether the operator finds it convenient to read.

D7 is the per-revision operationalization of [OS] §0.1.4 canonical-layer AI-consumer-RAG-optimization premise.

### 3.8.2 Sharp test

For each content unit (paragraph, subsection, table, list, header field), apply:

> **"If this content unit were deleted, would any AI behavior measurably degrade?"**

- If **Yes** (the content drives at least one AI behavior at retrieval time — rule application, routing decision, ownership lookup, gate enforcement, cross-reference resolution): the content passes D7.
- If **No** (the content serves operator readability, historical context, derived view of an authoritative source, or rhetorical closure): the content is a D7 deletion candidate.

The test is binary at the per-content-unit level. Multiple D7 failures aggregate into a single finding when they constitute a thematic deletion (e.g., "all motivation sub-sections in §3.x are D7-negative") to avoid flooding the report with one-finding-per-paragraph noise.

### 3.8.3 Check clauses

- **Derived-count check**: does the source contain a count, statistic, percentage, or numeric breakdown that is derivable from an authoritative table or registry at retrieval time? If yes, and the derived value is not itself load-bearing for an AI decision, mark for deletion.
- **Restated-rule-boilerplate check**: does the source restate a rule whose authoritative home is another canonical source, with no added scope or specialization? If yes, and AI consumers can reach the rule via RAG cross-source retrieval, mark for deletion (the restatement is purpose-redundant per [OS] §0.1.4).
- **"Why X exists" subsection check**: does the source contain a subsection or paragraph whose primary content is historical motivation for the rule's inclusion in the canonical set? If yes, and the rationale is not consumed by AI at rule-application time, mark for deletion (migrate to git commit history or ADR).
- **Historical-status-snapshot check**: does the source contain a status snapshot of a prior canonical-set state that has been superseded? If yes, and the snapshot is not load-bearing for AI evaluation of future state transitions, mark for deletion.
- **Operator-navigation-scaffolding check**: does the source contain a table or list whose primary purpose is to help the operator navigate adjacent chapters / sources (e.g., "Boundary with §X", "How this chapter is consumed", "Chapter purpose vs neighbors")? If the content is rule-bearing for cross-source ownership delineation, keep; if the content is decorative navigation for operator reading flow, mark for deletion.
- **Summary-closure check**: does the source contain a closing paragraph that restates the chapter's earlier content for rhetorical closure? If yes, mark for deletion.
- **Decorative-meta-text check**: does the source contain a chapter-opening paragraph or section that describes "what this chapter does" rather than performing it? If yes, and the description is not load-bearing for AI scope-routing, mark for deletion. ([OS] §0 "Why this OS exists" chapter or `## How to use this source` blocks remain valid because they encode AI scope-routing signals; the test is whether the meta-text drives behavior or only describes the chapter to the operator.)

### 3.8.4 Failure modes D7 catches

- A canonical source contains a derived count or statistic that AI does not retrieve at rule-application time
- A canonical source restates a rule already owned by another canonical source as boilerplate "for convenience"
- A canonical source contains "Why X exists" / "Why this dimension exists" / "Rationale:" subsections whose content is historical motivation rather than retrieval-time decision input
- A canonical source contains a chapter-purpose paragraph, boundary-with-adjacent-chapter table, or consumption-meta section that serves operator navigation rather than AI behavior
- A canonical source carries a historical status snapshot of canonical-set state that has been superseded

### 3.8.5 Severity policy for D7 findings

D7 findings default to **S2 Major** under the 2×2 matrix even when behavioral impact is "Low" (deletion candidates do not actively misdirect Hub Claude; they degrade RAG signal density). The default-S2 tie-break overrides the matrix's default cell when:

- The non-AI-consumed content is **derived from an authoritative source** (count, statistic, restated boilerplate, status snapshot) — these are maintenance-cost generators per [OS] §0.1.4 ROI logic; their continued presence creates cumulative drift surface over time
- AND no compelling case is made for the content's AI behavioral role

D7 findings on isolated decorative meta-text (single sentence, one-off occurrence) default to **S3 Minor** per the matrix.

When in doubt between S2 and S3 for D7 findings, prefer S2 (conservative upgrade) — the rationale for [OS] §0.1.4 ROI logic is that per-revision operator review cost is the trade for ongoing RAG signal-to-noise improvement; suppressing D7 findings under-realizes that ROI.

### 3.8.6 Distinction from D3

See §3.4.4. Recapitulated:

- **D3 catches rule-semantic duplication** — two rules saying the same rule semantics in different places (within or across sources)
- **D7 catches derived-content non-AI-consumption** — content that is not a rule, is derivable from an authoritative source, and adds no AI behavioral signal beyond noise

The same physical content rarely activates both D3 and D7 because D3 requires the content to be a rule and D7 typically catches non-rule content (derived views, motivation, boilerplate restatement). When boundary cases occur (e.g., a restated rule that is also derivable as boilerplate from the owning source), record under D7 and note the cross-activation in the finding location.

## 3.9 Dimension orthogonality and execution order

### 3.9.1 Independence

The dimensions are independent: a source can fail any one while passing the other six. One acknowledged residual coupling: a single physical issue can occasionally activate both D1 (structural) and D3 (semantic) simultaneously when two sub-sections both structurally overlap in scope and semantically duplicate rule content. In such cases, the finding is recorded under both dimensions but assigned a single severity to avoid double-counting (see §4 severity grading rules).

### 3.9.2 Execution order

D1 → D3 → D2 → D4 → D6 → D5 → D7

Rationale for placing D7 last:
- D7 is the most aggressive deletion judgment in the framework. Running it last means all other dimensions' findings are already populated; D7 then operates on the cleaned-up rule set rather than on a source still mid-cleanup.
- D7 deletion candidates may sometimes be re-categorized as "rationale that does drive AI behavior" after D5 / D6 surface load-bearing rationale gaps. Running D7 after D5/D6 lets the auditor catch this reclassification.
- D1-D5 + D7 sequence is recommended, not mandatory. An auditor may run dimensions in parallel when context permits.

## 3.10 Dimensional applicability adjustments for PI

PI differs from canonical sources in three structural ways that require dimension-by-dimension adaptation rather than blanket application of the §3.2-§3.8 dimension definitions:

- PI has no §10 header
- PI is pointer-only by design — its preamble explicitly states "PI does not restate behavioral rules already specified in UP, and does not duplicate content already specified in PK"; rationale lives in PK
- PI is operator-managed via the Claude.ai project settings UI rather than via file authoring under `/mnt/project/`

The seven dimensions adapt as follows:

| Dim | Applies to PI? | Adaptation for PI |
|---|---|---|
| **D1** Structural Integrity | Yes | Apply ME/CE within PI's own section ontology (typical sections: Priority/Conflict, Role, Boundaries, Output Classification, Automatic Activations, Response Mode, Grounding). Do not apply [OS] §10 chapter-numbering convention — PI has no canonical chapter scheme |
| **D2.1** Internal Coherence | Yes | Standard within-source coherence checks per §3.3.1 |
| **D2.2** External Coherence | Yes, with header check removed | [OS] §10 header conformance does NOT apply (PI has no §10 header). External coherence for PI is: (a) PI's canonical-source enumeration matches the actual canonical set under `/mnt/project/`; (b) PI cross-references to UP and to canonical sources resolve to existing content; (c) PI's "defer to X" pointers point to current source names and current section numbers |
| **D3** Non-Redundancy | Yes, with explicit success criterion | PI's own preamble declares "PI does not restate behavioral rules already specified in UP, and does not duplicate content already specified in PK". D3 audits this principle directly against PI's text — any inline restatement of UP rules or PK content is a D3 finding regardless of whether the restatement is semantically faithful |
| **D4** Operationalizability | Yes | Standard two-readers test per §3.5 |
| **D5** Soundness | Yes | Standard purpose-traceability and necessity test per §3.6 |
| **D6** Rationale Transparency | **Re-scoped** | PI is intentionally pointer-only; rationale lives in PK by design. D6 for PI checks that PI's pointers correctly resolve to the canonical-source location where rationale lives, NOT that PI itself states rationale. A PI pointer to a renamed or restructured PK target is a D6 finding |
| **D7** AI Consumption Value | Yes, with PI-specific emphasis | PI is pointer-only by design, so the D7 derived-content / motivation / decorative-meta failure modes are particularly salient. D7 for PI checks: (a) PI's pointer text is minimal — no inlined rationale that belongs in PK; (b) PI does not contain "Why this exists" sections or operator-navigation scaffolding; (c) PI's enumeration of canonical sources is purpose-bearing (drives AI retrieval routing) rather than decorative |

---

# 4. Severity grading

## 4.1 Three-level severity scheme

| Level | Definition | Consequence |
|---|---|---|
| **S1 Blocker** | The defect would systematically misdirect Hub Claude or contradict a core rule the operator depends on. Examples: two top-level rules contradict each other without precedence declared; missing required header field; a load-bearing cross-reference resolves to deleted content; a section's stated scope contradicts its actual content | Must be fixed before the canonical source is considered usable. Blocks Hub Claude from acting on the source until resolved |
| **S2 Major** | The defect degrades Hub Claude behavior measurably or introduces significant friction, but does not cause systematic misdirection. Examples: load-bearing rule that fails the two-readers test; known important scenario not covered (CE gap); concept-drift duplicate rule; load-bearing rule without rationale; cross-source authority overlap; D7 derived-content / motivation-subsection that lowers RAG signal density | Should be fixed in the next revision cycle. The canonical source may be used in the interim |
| **S3 Minor** | The defect is cosmetic or low-impact. Examples: suboptimal sub-section ordering; non-load-bearing rule with thin rationale; non-load-bearing rule with mildly ambiguous wording; typographic inconsistency; numbering anomaly; isolated decorative meta-text | Fixed opportunistically when the source is being revised for other reasons |

## 4.2 The 2×2 judgment matrix

Each finding is graded along two binary axes; the cell in the matrix determines severity.

**Axis 1 — Behavioral Impact**:
- **High**: the defect would systematically misdirect Hub Claude or another reader; the misdirection is not corrected by reading neighboring text
- **Low**: the defect produces inconsistency, friction, or sub-optimality but does not misdirect; or the misdirection is corrected by neighboring text

**Axis 2 — Centrality**:
- **Load-bearing**: other rules in this source or in another canonical source depend on this rule; or the rule is cited from User Preferences, Project Instructions, or another canonical source
- **Not load-bearing**: the rule is local, edge-case, or has no downstream dependencies

**The matrix**:

| | Load-bearing | Not load-bearing |
|---|---|---|
| **High Impact** | **S1 Blocker** | **S2 Major** |
| **Low Impact** | **S2 Major** | **S3 Minor** |

**D7 severity override per §3.8.5**: D7 findings on derived-content / purpose-redundancy patterns default to S2 even when Behavioral Impact is "Low" and the content is not directly load-bearing, because the cumulative-drift-surface cost over time exceeds the static behavioral-impact judgment.

## 4.3 Severity assignment examples

| Example finding | Impact | Centrality | Severity |
|---|---|---|---|
| Two rules at top level of §X directly contradict each other; precedence is not declared | High | Load-bearing | **S1 Blocker** |
| A short bullet rule states "only stable, reusable, cross-topic content becomes canonical" but provides no decision rubric for "stable" | Low | Load-bearing | **S2 Major** |
| A cross-reference `§4.2` points to a renamed section; nearby text makes the actual target clear | Low | Load-bearing | **S2 Major** |
| One pairing entry in a 31-row table has a shorter rationale than peer entries | Low | Not load-bearing | **S3 Minor** |
| Sub-section numbering uses `§8.7a` while peers use `§8.7.1` style | Low | Not load-bearing | **S3 Minor** |
| Derived count "active pairings: 31" stated in two places, one of which is derivable from the authoritative §8.5.2 table | Low | Not load-bearing | **S2 Major** (D7 override per §3.8.5) |
| "Why this mechanism exists" subsection with historical pattern motivation, not retrieved at runtime | Low | Not load-bearing | **S2 Major** (D7 override) |

## 4.4 Tie-break rules

When a finding sits ambiguously between cells:
- **Between High and Low Impact**: prefer Low Impact (conservative downgrade) unless the rule is on the conversation's critical path and Hub Claude would predictably act on it without reading further
- **Between Load-bearing and Not load-bearing**: prefer Load-bearing (conservative upgrade) when the rule is at the top level of a chapter, when other rules cite it, or when the rule's removal would cascade into other rules
- **When a single physical issue activates two dimensions**: record the finding under both dimensions in the audit report's dimension column, but assign one severity (do not double-count)
- **D7 tie-break per §3.8.5**: derived-from-authoritative-source content defaults to S2 even in the Low-Impact / Not-load-bearing cell

---

# 5. Output format

## 5.1 Audit report structure

The audit report is produced in conversation as Markdown, with the following structural sections in order:

```
## Canonical File Self-Audit Report

**File**: <path to audited canonical source, or "PI (project settings)">
**Audit trigger**: <T1 / T2 / which trigger condition fired>
**Audited revision**: <description of revision under audit>
**Audit scope**: <full file / specific sections / PI / combined>

### Findings Summary
[Compact table: severity-level rows, finding counts in cells, dimension-column breakdown, target-type breakdown when scope is combined]

### Findings Detail
[Numbered table: F-NN | Target type (canonical / PI) | Severity | Dimension | Location | Description | Impact reasoning | Centrality reasoning]

### Framework Notes (optional)
[Observations about audit framework effectiveness on this particular source; surfaced only when the audit pass revealed framework-side issues]
```

**Combined audit reports for canonical + PI scope**: When an audit pass scopes both PI and one or more canonical sources together, the report is produced as **one combined report** with a `Target type` column in the findings table (values: `canonical` or `PI`), not as two separate reports. The wave-set split in the Action Plan (see §5.2) handles the cost-profile asymmetry between canonical-side and PI-side fixes.

## 5.2 Action plan structure

The action plan is produced as a separate Markdown section after the audit report, with findings grouped into **waves**. Wave assignment is determined by (a) severity and (b) modification cost.

```
## Action Plan

### Wave 1: <descriptive name>
[Highest-severity findings + low-cost batchable fixes]
- F-NN: <action>
- F-NN: <action>

### Wave 2: <descriptive name>
[Next-priority findings, typically D7 deletions and remaining S2 fixes]
- F-NN: <action>

### Wave 3: <descriptive name>
[Opportunistic S3 fixes; defer until other revision opens the source]
```

**Wave organization heuristics**:
- All S1 Blockers in Wave 1
- D7 derived-content deletions grouped together (they share the same modification pattern: remove without semantic substitution)
- D2 cross-reference fixes grouped together (they share the same modification pattern: update citation target)
- High-cost rule rewordings in their own wave to avoid mixing cost profiles
- S3 fixes deferred to the wave where another reason opens the source

**PI-target action plan note**: When the action plan contains PI-target findings, those are routed to a separate wave (typically the last wave) because PI is updated via the Claude.ai project settings UI rather than via file editing in conversation. The wave structure keeps PI-target actions visible alongside canonical-target actions for cross-target dependency tracking, while signaling the different execution channel.

## 5.3 Action plan tone

Each finding's recommended action states what to change, where, and why. Avoid hedge language. State the action as an imperative ("Replace X with Y in §Z because <reason>"), not as a suggestion ("Consider whether X might benefit from Y"). The operator is the decision-maker on whether to execute; the audit's job is to surface what would need to be done if the operator accepts the finding.

## 5.4 What the audit does not produce

- **Direct file rewrites**: the audit surfaces findings and action items. It does not silently rewrite the canonical source.
- **Severity downgrades for operator convenience**: when an S1 Blocker is surfaced, the audit reports it as S1 even if the operator is in a hurry. Downgrading severity is the operator's explicit decision documented in the same conversation.
- **Combined report-and-fix turn for S1**: when an S1 is surfaced, Hub Claude pauses for operator decision rather than auto-fixing in the same turn. S2 and S3 findings can be auto-fixed in the same turn at operator instruction.

---

# 6. Audit execution flow

## 6.1 Audit invocation

When a T1 or T2 trigger fires per §2.2, Hub Claude executes the audit using the audited source's full content (via filesystem or canonical search), its header per [OS] §10, the set of canonical sources cited by or citing the audited file, and the trigger tier per §2.2.

**Verification channel priority for canonical source content**: Hub Claude has two channels through which canonical source content is accessible — the conversation-level filesystem snapshot at `/mnt/project/` and the real-time Claude.ai project knowledge base index queried via `project_knowledge_search`. These two channels are not always synchronized:

- The `/mnt/project/` filesystem snapshot is session-level — captured at conversation start and frozen for the duration of that conversation. It does not refresh when the operator uploads new versions mid-conversation.
- The `project_knowledge_search` index is real-time — it reflects the operator's most recent upload state.

**Operational rule**: when verifying the post-fix state of a recently-uploaded canonical source within the same conversation in which the upload occurred, `project_knowledge_search` is the authoritative channel. A `/mnt/project/` inconsistency in that scenario is a snapshot timing artifact, not a finding. When the audit itself is initiated in a fresh conversation (snapshot taken after all uploads complete), the two channels normally agree and either is admissible.

Audit reports that surface `/mnt/project/` inconsistencies must explicitly state which channel was the authority used and rule out snapshot-timing artifacts before classifying the inconsistency as a finding.

## 6.2 Sequencing of dimensions

Run D1 → D3 → D2 → D4 → D6 → D5 → D7 per §3.9.2.

Within each dimension, collect all findings before moving to the next dimension. Do not let early dimensions' findings short-circuit later dimensions — even if D1 surfaces a structural issue that suggests the audited source needs major rework, complete D2 through D7 anyway so the operator has the full picture before deciding response.

## 6.3 Post-audit Wave organization

After all seven dimensions have run, the auditor groups findings into Waves per §5.2 wave assignment heuristics. Wave organization is content-aware: findings that can be addressed in a single coordinated revision pass are placed in the same Wave, even if their severity differs slightly. D7 findings are typically batchable in a single wave because they share a modification pattern (deletion without semantic substitution).

The auditor states wave organization decisions explicitly in the action plan so the operator can re-balance.

## 6.4 Blocker handling at the end of audit

If the audit surfaces any S1 Blockers:
- The audit report is delivered with all findings (S1, S2, S3) populated
- The canonical source file is flagged "blocker-pending"
- The action plan's Wave 1 explicitly lists S1 Blockers first
- Hub Claude does not present the file for download or invoke `present_files` until the operator has decided how to handle the Blocker

If the audit surfaces only S2 and S3 findings:
- The audit report is delivered alongside the canonical source file
- The file is presented for download via `present_files` normally
- The action plan is delivered as part of the conversation turn

**PI Blocker adaptation**: When a Blocker finding targets PI, Hub Claude is not generating a PI file to gate on, so there is no `present_files` to withhold. Instead:
- Hub Claude surfaces the PI Blocker prominently at the top of the audit report
- Hub Claude recommends operator resolution before relying on PI-governed behavior
- In subsequent conversation turns, Hub Claude notes when the unresolved PI Blocker is operationally in play
- The conversation may continue; the PI Blocker does not gate other unrelated tasks

---

# 7. Relationship to other governance mechanisms

## 7.1 To [OS] §8 source governance

This source operationalizes the consistency-check rule declared in [OS] §8.5. Where §8.5 says "verify consistency", this source defines:
- Which dimensions of consistency are checked (D2.2 External Coherence is the primary cross-source mechanism; D2.1 Internal Coherence checks within-source consistency)
- When the check fires (the trigger model in §2)
- How findings are graded (severity scheme in §4)
- What output is produced (format in §5)

This source does not supersede §8.5. §8.5's semantic-scan-plus-static-pairing two-layer verification mechanism remains canonical; this source's D2.2 check builds on that mechanism rather than replacing it.

## 7.2 To [OS] §12 anti-drift corrections

Some audit findings produced by this source are also signals on the [OS] §12 anti-drift corrections list:

| Audit finding shape | [OS] §12 signal |
|---|---|
| D2.2 finding: canonical name change without grep-verifying citations | §12 item "a canonical name change or § re-numbering is made without grep-verifying all citations across canonical sources" |
| D2.2 finding: Document Type / Status / Role first-word uses non-vocabulary value | §12 item "a `Document Type`, `Status`, or `Role first word` field uses a value not in the §10.4 controlled vocabulary" |
| D2.2 finding: Source Category missing or inconsistent | §12 item "a Source Category declaration is missing from a new canonical source header, or a declared Source Category is inconsistent with the source's actual dependency pattern" |
| D1 CE finding: section approaches [OS] §8.5.7 re-architecture threshold without Options Paper | §12 item "a §8.5.7 harness re-architecture threshold is crossed without an Options Paper evaluation initiated" |
| D2.2 finding: same-revision paired update not honored | §12 item "a same-revision pairing in §8.5.2 is being triggered without the paired source being updated in the same revision" |
| D7 finding: canonical content does not drive AI behavior at retrieval time | §12 item "a canonical source carries content that does not drive AI behavior at retrieval time" |

When an audit finding also constitutes a §12 signal, the audit report flags both: the finding appears under its dimension in the findings table, and a separate "Anti-drift signals" line enumerates the §12-relevant findings for direct operator attention.

This source does not replace §12. The §12 catalog continues to be the canonical anti-drift register; this source only routes audit findings onto §12 where the overlap exists.

## 7.3 To [OS] §8.9 source-ready generation protocol

[OS] §8.9 governs how a canonical source is produced (pre-generation declarations, same-pass generation, mechanism verification). This source defines what happens after generation completes: an audit pass runs against the seven dimensions before the source is considered usable.

The two sources are sequenced:
1. [OS] §8.9 pre-generation declarations
2. [OS] §8.9 single-pass generation
3. [MECH] Canonical File Self-Audit T1 audit (this source)
4. Audit report and action plan output
5. (If S1 Blocker) operator decides response before file is considered usable

This source does not modify the §8.9 generation pass itself. The audit runs after generation completes; it does not interleave with generation.

---

# 8. Failure modes and limitations

## 8.1 What this audit does not catch

The audit has explicit limitations:

- **Semantic correctness of rules**: the audit cannot tell whether a rule actually accomplishes its stated purpose. A rule that is perfectly operationalizable (D4 passes) and has clear rationale (D6 passes) can still be wrong on the merits
- **Anticipatory coverage of unknown scenarios**: D1 CE checks coverage of typical and known-difficult scenarios. It does not check coverage of scenarios the operator and Hub Claude have not yet encountered
- **Cross-conversation coherence**: the audit examines coherence within a single canonical source and against currently-known cross-references. It cannot verify that the source's rules will remain coherent with future canonical-source additions
- **Behavioral verification**: the audit checks the canonical source as text. It does not run Hub Claude against test scenarios to verify the rules actually produce the intended behavior
- **Audit-of-audit limitations**: the audit framework defined in this source is itself a canonical source subject to its own audit. Residual blind spots in the audit framework would, by definition, produce false negatives that the audit cannot self-detect

## 8.2 Dimensional shadowing risk

When two dimensions both activate on the same physical issue (most commonly D1 + D3 on a structural-and-semantic overlap, D4 + D6 on a rule that is both vague and unjustified, or D3 + D7 on a restated rule that is also derivable boilerplate), the reporting convention in §4.4 collapses to a single severity. This is intentional (to avoid double-counting) but creates a small reporting risk: a high-severity issue under one dimension may be partly obscured by a co-activated low-severity issue under another dimension.

Mitigation: the audit report's findings table records both dimensions for shadowed findings, and the operator can inspect the full impact/centrality reasoning per finding. The single-severity assignment is for action-plan ordering, not for hiding the full picture.

## 8.3 Self-application

This source applies to itself. Substantive revisions to this source trigger a T1 audit per §2.2.

The self-application limit: the audit framework cannot identify its own conceptual blind spots, only its own textual issues. If a category of canonical-source quality failure is not captured by any of D1-D7, this source's audit will miss it. The remedy is external — the operator periodically surveys peer projects' specification quality methodologies and considers whether new dimensions should be added.

**Second self-application path (PI)**: This audit framework applies to PI, and PI in turn references this canonical source as part of its automatic-activation enumeration. When this source's PI-scope rules (§1.3 PI item, §2.2 PI trigger rows, §3.10 dimensional adaptations, §5.2 PI Wave assignment, §6.4 PI Blocker adaptation) change substantively, PI's reference to this source must be reviewed for continued accuracy in the next operator-side PI revision cycle. The operator carries the obligation; Hub Claude surfaces a reminder in the audit report when the relevant sections are being revised.

---

# 9. Audit finding disposition

This section owns the discipline for handling audit findings **after** they are surfaced by §3-§5 output. The disposition framework distinguishes finding types and prescribes the appropriate resolution path for each. The disposition log (§9.2) archives operator裁决 across audit cycles.

## 9.1 Finding type taxonomy

Audit findings fall into two distinct types, each with its own disposition path:

| Finding type | Definition | Disposition path |
|---|---|---|
| **Mechanical inconsistency** | Canonical text is internally inconsistent (within one file or across multiple files), or text has not caught up with an already-established design. The design itself is sound; only the text is out of sync. | Apply text fixes in the affected canonical file(s) under same-revision discipline per [OS] §8.5.2. No design decision needed; no operator裁决 required beyond approving the textual correction. Log entry in §9.2 captures: which file(s), which lines, what corrected wording. |
| **Design-intent variance** | Canonical implementation diverges from external audit checklist or expected design as anticipated by an upstream specification. The canonical is internally consistent and has inlined rationale, but conflicts with an outside expectation. | Operator裁决: accept the current canonical (and amend the upstream checklist / expected-design source) **or** revert to the upstream expectation (and modify canonical accordingly). Log entry in §9.2 captures: which finding(s), which alternatives considered, the裁决 rationale, and reversal trigger conditions. |

Distinguishing test: if the question "is the design right?" has an answer in the affirmative when reading the canonical alone (internal rationale present), the finding is design-intent variance; if the question "is the text right?" has the answer "no, the text contradicts itself or another canonical" without invoking any external checklist, the finding is mechanical inconsistency.

A single audit run can surface findings of both types; each is dispositioned independently.

## 9.2 Disposition log

Audit findings dispositions are recorded as entries in this section. Each entry captures the audit cycle, the findings dispositioned, the type, the裁决, and references to any artifacts produced.

### 9.2.1 Disposition log entry schema

| Field | Content |
|---|---|
| Audit cycle | ISO-8601 date of audit run, plus brief scope label |
| Finding ID(s) | Identifier of the finding(s) being dispositioned in this entry |
| Finding type | `Mechanical inconsistency` or `Design-intent variance` |
| Affected canonical | Files or sections that the disposition touches |
| Disposition裁决 | `accept current canonical (amend external)` / `revert canonical (modify to match external)` / `apply text fix` / `retire rule` / `not applicable to project scope` |
| Rationale | One-paragraph rationale linking the裁决 to inlined canonical rationale, design rationale, or scope-applicability judgment |
| Reversal conditions | If applicable: trigger conditions under which the disposition should be revisited |
| Operator authorization date | Date operator signed off on the disposition |
| Produced artifacts | References to revised canonical / amended checklist / disposition memo, if any |

### 9.2.2 Disposition log entries

#### Entry 1 — 2026-05-17 Path B2 canonical refactor verification audit disposition

| Field | Content |
|---|---|
| Audit cycle | 2026-05-16 cross-source consistency audit, 33 sources (32 PK + PI) per `hdc-refactor-verification-rule-set.md` (operator-supplied, v1 dated 2026-05-15) |
| Finding ID(s) | Findings #1 (mechanical), #2 / #3 / #4 (variance), #5 / #6 (mechanical — formal split补完), #7 (mechanical — admissibility table gap), #8 (variance — Hook system), #9 (mechanical — passive voice), #10 / #12 (mechanical —补完), #11 / #13 (not applicable to project scope — retire), #14 (mechanical — clarifying note); 14 total |
| Finding type | Mixed (see Finding ID column for per-finding type) |
| Affected canonical | `hdc_tpl_test-plan-yaml-schema.md`, `hdc_ref_hub-cd-cc-architecture.md`, `hdc_os_project-operating-model.md`, `hdc_ref_cc-project-memory-bank-layout.md`, `hdc_mech_development-track-workflow.md`, `hdc_mech_canonical-file-self-audit.md` (this file) |
| Disposition裁决 | **For Findings #2 / #3 / #4 (variance)**: `accept current canonical (amend external)` — operator accepts current canonical TK-03 = Hub-only producer, CC memory bank 5-level structure, and TK-04 renumbered active task; verification rule set v1 amended to v2 (2026-05-17) updating §C-04 / §E-01 / §F-08 / §J-01 wording. **For Finding #8 / K-07**: `accept current canonical` — Hook system is embedded at verification-rule-application level; no canonical fragment needed; K-07 reworded in rule set v2. **For Findings #11 / F-11 and #13 / K-08**: `not applicable to project scope — retire` — HDC does not use Backlog.md; Pattern A/B not in HDC scope; both rules retired in rule set v2. **For Findings #1 / #5 / #6 / #7 / #9 / #10 / #12 / #14 (mechanical)**: `apply text fix` — affected canonical files revised under same-revision discipline. |
| Rationale | Variance findings #2 / #3 / #4 acceptance rationale: cross-model review consensus loop is Hub-only operable per [MECH] DTW §4 line 383-388; 5-level CLAUDE.md aligns with [RULE] CCAR §X agent context scopes per-tier discipline; TK-04 renumbering preserves serial consistency per H-08 exception clause "unless serial consistency requires". Full alternatives comparison preserved in Options Paper (2026-05-16 chat zone archive). Hook system / Backlog.md / Pattern A-B disposition per operator confirmation 2026-05-17. Mechanical fix findings #1 / #5 / #6 / #7 / #9 / #10 / #12 / #14 each have clear textual corrections that align canonical with established design intent. |
| Reversal conditions | Per-variance reversal triggers: (a) D2 reversal if cross-model review consensus loop moves out of Hub-only operability; (b) D3 reversal if [RULE] CCAR §X agent context scopes simplify; (c) D4 reversal if empirical legacy/new TK-04 collision surfaces in operator workflow. Mechanical fixes have no reversal — they correct established design, not establish new design. |
| Operator authorization date | 2026-05-17 |
| Produced artifacts | `hdc-refactor-verification-rule-set.md` v2 (operator-supplied artifact, 2026-05-17); revised canonical files listed in "Affected canonical" row above; Options Paper preserved in 2026-05-16 chat zone as archival rationale source |

## 9.3 Boundary with adjacent governance mechanisms

This §9 disposition framework is distinct from:

- **§5 Output format** (which owns audit report structure prior to disposition)
- **§6 Audit execution flow** (which owns how the audit is run, including blocker handling at §6.4)
- **[TPL] ADR Spec** (which records forward-looking architecture decisions — typically during TDD review at Cat 4 work)
- **[TPL] Options Paper** (which compares decision options before a裁决 is made; this §9 records the裁决 after Options Paper consideration completes)

The disposition log captures audit-process裁决 archival, not architecture decision archival. When an audit-process裁决 also entails a downstream architecture decision (e.g., an audit surfaces a need to re-enable direct CD↔CC coupling), the architecture decision lands as an ADR per [TPL] ADR Spec §3.3 Meta-layer landing path, and the disposition log entry references the ADR.

## 9.4 Anti-drift red flags for disposition handling

- Audit finding marked as "Mechanical inconsistency" actually carries a design-intent variance disguised as text fix → reclassify as variance and route to operator裁决
- Disposition log entry omitting reversal conditions for design-intent variance → add reversal conditions (variance dispositions should be reversible by future audit cycle if conditions change)
- Same audit finding appearing in multiple consecutive disposition entries without progression → indicates the disposition is not actually closing the finding; re-evaluate finding type or disposition path
- Disposition log entry recording an operator裁决 without inlined rationale → rationale must reference inlined canonical rationale, external evidence, or scope-applicability judgment; bare裁决 without traceability is anti-drift
- ADR authored for what should be a §9 disposition entry → ADRs are forward-looking architecture decisions; audit-finding dispositions belong here
