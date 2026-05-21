# [TPL] Problem Framing Memo

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable template for translating an ambiguous HR business need into a structured digital problem before solution design
- **Source Category**: Cross-category
- **Management-System Role**: Pre-artifact framing template; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Supports the Think loop; this memo's landing logic follows [OS] §5.4, and its anti-drift posture is aligned with the red-flag triggers in [OS] §12.
- **Relationship to [PRIN]**: Applies [PRIN] HR Digital Decision Design Principles §1 (business-first, architecture-enabled), §3 (global core with governed local variance), §10 (apply MECE to important decomposition structures — applied here to problem-type separation), §12 (make important work executable — applied here to recommended next artifact)
- **Relationship to adjacent [TPL] sources**:
  - Use this template before `[TPL] Options Paper` when the business issue, decision, or boundary is still too unclear for real option comparison
  - Use this template before `[TPL] PRD / Prototype / MVP Spec Template` when solutioning pressure exists but the problem, decision, or governing linkage is still not stable enough for specification depth
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: When the final memo is uploaded to DingTalk Docs, apply that rule to normalize the Markdown before upload.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [TPL] Problem Framing Memo` header fields per [OS] §8.5.1a)

## How to use this source

Use this template when:
- the business request is still ambiguous
- stakeholders are reacting to symptoms rather than agreeing on the actual problem
- the work is drifting into solution design too early
- the next artifact is not yet clear

This is a pre-artifact framing template.
Use it to clarify the problem and the next artifact, not to replace the next artifact.

Use it in three passes rather than trying to clarify everything at once.

**What this template is not**

This is a strategic thinking aid for the operator's own pre-artifact decision work in the Cat 1 strategic thinker / policy architect role (per [OS] §0.2), not a PM portfolio piece, a design-thinking workshop deliverable, or a consulting Discovery framework instantiation (Lean Six Sigma DMAIC Define, IDEO design-thinking Discover, McKinsey Issue Tree, etc.). The Memo's purpose is to clarify the operator's framing before deeper work, not to be presented externally or scored against framework conventions. External frameworks may be sources of inspiration; they are not targets to replicate.

### Pass 1 — Frame

**Scope: First of three iterative authoring passes for a Problem Framing Memo (under `How to use this source`); the goal of Pass 1 is to make the business issue and decision explicit before deeper exploration begins.**

Complete:
- 1. Basic Context
- 2. Business Issue and Decision
- 3. Why This Matters Now
- 5. Problem Type and Boundaries
- 11. Landing Summary as a draft

Goal:
- make the business issue and decision explicit

### Pass 2 — Tension and value

**Scope: Second of three iterative authoring passes for a Problem Framing Memo (under `How to use this source`); the goal of Pass 2 is to surface tensions, evidence quality, variance logic, and value logic after Pass 1 has framed the business issue.**

Complete:
- 4. Signals, Evidence, and Unknowns
- 6. Stakeholder Context and Tensions
- 7. Global Core vs Local Variance View
- 8. Business Value and Success Logic

Goal:
- surface tensions, evidence quality, variance logic, and value logic

### Pass 3 — Land

**Scope: Third of three iterative authoring passes for a Problem Framing Memo (under `How to use this source`); the goal of Pass 3 is to decide what artifact should follow the memo, after Pass 1 framed the issue and Pass 2 surfaced tensions and value.**

Complete:
- 9. Likely Management-System Landing or Linkage and Recommended Next Artifact
- 10. Framing Judgment
- 11. Landing Summary as a final version

Goal:
- decide what artifact should follow next
- state likely management-system landing level only when the next artifact is a management-system output and the level is clear enough to help
- state likely management-system linkage only when the next artifact is a specification output and linkage is materially relevant

Working rules:
- start in Lite mode and deepen only when needed
- keep one memo to one decision cluster where possible
- mark uncertainty explicitly using tags such as `[Known]`, `[Assumption]`, `[Unknown]`, `[Decision needed]`, and `[Out of scope]`
- keep specific solution proposals out of scope until the framing is stable enough to justify them
- use the memo to decide the next artifact, not to replace the next artifact
- do not force every memo into one intended landing level
- if the next artifact is a management-system output, state the likely management-system landing level only when it is clear enough to improve next-step quality
- if the next artifact is a specification output, state the likely management-system linkage only when it materially affects framing, review, or downstream design
- if level or linkage is still unclear, make the ambiguity explicit and state what must be clarified next

Do not use this template as:
- a full solution design document
- a vendor evaluation document
- a full policy draft
- a process map
- a project tracker

## Completion standard

The memo is good enough to move forward when:
- the business issue and decision are explicit
- the primary problem type is named
- major stakeholder tensions are visible
- global core versus local variance implications are addressed or deliberately parked
- the value hypothesis is visible
- the next artifact is named
- the likely management-system landing level is stated when the next artifact is a management-system output and the level is clear enough to help the next step
- the likely management-system linkage is stated when the next artifact is a specification output and linkage materially affects direction, review, or downstream design
- material unknowns are visible
- another person can pick up the next step without requiring verbal backfill

# 1. Basic Context

- Topic / working title:
- Date:
- Request source:
- Memo owner:
- Contributors:
- Mode: Lite / Deep
- Status: Draft / Decision-ready

# 2. Business Issue and Decision

- What business issue is being raised?
- What decision needs to be made now?
- What business outcome, risk, or behavior is affected?
- What happens if no decision is made?
- What is the relevant time horizon?
- What is this decision explicitly not trying to solve?

# 3. Why This Matters Now

- What changed or triggered the request?
- Why is this surfacing now rather than earlier?
- What deadline, dependency, risk, or opportunity makes this time-sensitive?
- What is the likely cost of waiting?

# 4. Signals, Evidence, and Unknowns

- What symptoms are visible today?
- What evidence already exists?
- What is assumption or anecdote rather than evidence?
- What is still unknown?
- What is the minimum additional fact needed before moving into solution design?

# 5. Problem Type and Boundaries

- Primary problem type: policy / process / system / data / analytics / governance / operating model / mixed
- Secondary interfaces:
- Why this classification:
- In scope:
- Out of scope:
- What this is not:
- Likely root issue location:
- Boundary note: where does this problem interface with other domains without becoming their full owner?

# 6. Stakeholder Context and Tensions

- Decision owner:
- Reviewers / influencers:
- Affected stakeholder groups:
- Main stakeholder interests:
- Main tensions or trade-offs:
- Dependencies:
- Change sensitivity / political sensitivity:
- What alignment is required before a solution path can be chosen?

# 7. Global Core vs Local Variance View

- Default posture: global core / governed local variance / local exception / unclear
- Why this posture currently seems appropriate:
- What must remain globally consistent?
- What may vary locally?
- What is driving the variance, if any?
- What risk appears if this is treated as fully global when it is not?
- What risk appears if this is treated as local when it should be global?

# 8. Business Value and Success Logic

- Expected business value:
- Value hypothesis: If we address `[X]` for `[Y]`, then `[Z]` should improve because `[logic]`.
- Leading indicators:
- Lagging indicators:
- Adoption or utilization signals to watch:
- Key risks to value realization:
- What would make this effort not worth doing?

# 9. Likely Management-System Landing or Linkage and Recommended Next Artifact

- Recommended next artifact: Options Paper / Policy Note / Policy Architecture / Process Map / Governance Mechanism / PRD / Prototype Brief / MVP Brief / Data & Analytics Spec / Other
- Output family: management-system artifact / specification artifact / unclear yet
- Why this artifact should come next:
- If the next artifact is a management-system output:
  - likely management-system landing level: L2 / L3 / L4 / L5 / unclear yet
  - why this level is the current best fit:
  - what adjacent levels are implicated but should not own the next artifact:
- If the next artifact is a specification output:
  - likely management-system linkage, if materially relevant:
  - what governing policy, sub-policy, process, or SOP / SWI implication appears to matter:
  - what management-system ambiguity, if any, must be clarified before the specification hardens:
- What decision or clarification is needed to move forward now?

# 10. Framing Judgment

- The real problem appears to be:
- The decision required is:
- This is primarily a `[type]` problem with `[secondary types]` interfaces.
- The main global-versus-local implication is:
- The recommended next artifact is:
- The likely management-system landing or linkage implication is:
- One-sentence recommendation for how to proceed now:

# 11. Landing Summary

Complete this section per [OS] §5.4.

Note: Own and Watch below are document-content expectations for this memo, not a reinstatement of FLOW-L as a response-layer reasoning protocol. Per [OS] §5.4, the Level-or-linkage declaration is the only dimension that requires explicit response-layer enforcement; Frame, Land, Own, and Watch are already covered by the default Evidence / Assumptions / Inference / Conclusions / Implications response structure.

- **Business decision restatement**: Restate the framed business decision (reference §2) in one line.
- **Recommended next artifact**: Name the next artifact (reference §9).
- **Level-or-linkage declaration** (per [OS] §5.4):
  - If the next artifact is a management-system output, state the intended landing level (L2, L3, L4, or L5) when clear enough; if still ambiguous, state the ambiguity and what must be clarified to resolve it.
  - If the next artifact is a specification output whose downstream correctness depends on management-system context, state the governing management-system linkage when it materially affects framing, review, or downstream design; omit when linkage is irrelevant.
- **Own**:
  - Owner:
  - Reviewer:
  - Decider:
- **Watch**: State the signals to monitor and at what cadence (leading, lagging, adoption, utilization, value as relevant).

# Completion Check

- The memo is centered on one decision cluster.
- The business issue and decision are explicit.
- The reason this matters now is clear.
- The primary problem type is named before solution design begins.
- The stakeholder tensions are visible.
- The global core versus local variance implication is addressed or deliberately parked.
- The business value and success logic are stated.
- The next artifact is named.
- If the next artifact is a management-system output, a likely landing level is stated only when it materially helps the next step.
- If the next artifact is a specification output, management-system linkage is stated only when it materially affects framing, review, or downstream design.
- If level or linkage is still unclear, the ambiguity and next clarification are explicit.
- Major assumptions and unknowns are visible.
- Another person could take the next step without requiring verbal backfill.
- If the final memo will be uploaded to DingTalk Docs, the Markdown has been normalized per [RULE] DingTalk Markdown Format Control Specification before upload.
