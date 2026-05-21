# [TPL] Options Paper

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable template for structured comparison of HR digital solution options before specification or implementation handoff
- **Source Category**: Cross-category
- **Management-System Role**: Decision-support template; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Supports the Think-to-Specify transition by turning a framed decision into a recommendation-ready options comparison; this template's landing logic follows [OS] §5.4.
- **Relationship to [PRIN]**: Applies [PRIN] HR Digital Decision Design Principles §1 (business-first, architecture-enabled), §2 (capability-first, not vendor-first), §3 (global core with governed local variance), §4 (lifecycle value over implementation convenience), §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design), §7 (analytics-informed digital decision making)
- **Relationship to adjacent [TPL] sources**:
  - Use `[TPL] Problem Framing Memo` before this template when the business issue, decision, or boundary is still unclear
  - Use this template before `[TPL] PRD / Prototype / MVP Spec Template` when a solution path must be chosen before specification depth is justified
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: When the final paper is uploaded to DingTalk Docs, apply that rule to normalize the Markdown before upload.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [TPL] Options Paper` header fields per [OS] §8.5.1a)

## How to use this source

Use this template when:
- the business issue and decision are framed well enough to compare credible solution paths
- 2 to 4 real options exist and the trade-offs must be made explicit
- the recommendation must be reviewable across CoE, regional HR, HRBP, and HR solution / delivery stakeholders
- the work needs a durable decision-quality paper rather than a presentation-first artifact

Primary working audience:
- author
- working-level reviewers
- cross-functional reviewers who need logic quality, not slide polish, to challenge the recommendation

Downstream use:
- this template is suitable as a structured source input for later executive briefing, brief-note, or slide generation
- the completed paper should carry the logic that survives compression into a shorter downstream management readout
- this source is not a presentation-layout template

## Working stance

This template is intentionally **review-grade**, not presentation-led.

However, it should still remain **decision-ready, not academic**.

Apply the following writing rules:
- keep the core paper short enough to be read end-to-end without fatigue
- put only decision-relevant content in the core paper
- move supporting detail into optional supporting modules or appendices
- prefer explicit comparison over long narrative description
- make the recommendation clear early, then justify it
- mark uncertainty honestly using tags such as `[Fact]`, `[Assumption]`, `[Unknown]`, `[Decision needed]`, and `[Out of scope]` when useful

## Core-paper and support-module rule

This template uses one depth only, but two reading layers:

### Core paper

Always complete Sections 1 to 8.

These sections should contain the minimum logic needed for:
- review
- challenge
- recommendation
- later conversion into an executive brief or slide deck

### Supporting modules

Complete Section 9 only when the added detail materially improves decision quality.

Do not complete optional modules just because the structure exists.

If a detail does not change the decision, recommendation, guardrail, or next step, leave it out.

## What this template is not

Do not use this template as:
- a first-pass problem framing memo
- a vendor feature catalogue
- a procurement scorecard
- a PRD or handoff specification
- a policy draft
- a process map repository
- a management presentation deck

## Completion standard

The paper is good enough when:
- the decision ask is explicit
- the option set contains real and comparable options
- the recommendation is explicit rather than implied
- the key trade-offs are visible
- business value, governance, architecture, data, analytics, operation management, execution, and ROI logic are visible at the right level
- another person can use the completed paper as the source for a shorter executive readout without requiring extensive verbal backfill

# 1. Document Information

| Item | Content |
|---|---|
| Artifact Type | Options Paper |
| Language Mode | English / Chinese / Bilingual |
| Topic / Decision Name |  |
| Version |  |
| Owner |  |
| Contributors |  |
| Reviewers |  |
| Primary Audience | Author / Working-level reviewers / Cross-functional stakeholders |
| Status | Draft / Decided |
| Decision Forum |  |
| Decision Date or Window |  |
| Related Documents |  |

# 2. Decision Snapshot

## 2.1 Decision ask

- **Decision required**:
- **Recommended option**:
- **Why now**:
- **Decision owner**:
- **Decision forum / approver**:
- **Decision timing**:

## 2.2 Recommendation in one paragraph

State the recommendation directly.

Include:
- what is being recommended
- why it is the best choice now
- what trade-off is being accepted
- what approval or alignment is required

## 2.3 Options at a glance

| Option | One-line description | Relative position | Main caution |
|---|---|---|---|
|  |  |  |  |

## 2.4 What a good decision should achieve

State the outcome the decision should produce.

Prefer business, control, user, and lifecycle value language over technical labels.

# 3. Decision Context and Boundaries

## 3.1 Business context

Describe the business trigger, operating issue, and why this decision exists now.

## 3.2 Problem statement

State the problem to be solved.
Separate symptom from root issue where possible.

## 3.3 In scope

Clarify what this decision will determine now.

## 3.4 Out of scope

Clarify what this paper is not deciding in this round.

## 3.5 Constraints and non-negotiables

| Constraint / Non-negotiable | Type | Why it matters |
|---|---|---|
|  | Legal / Policy / Budget / Time / Platform / Data / Governance / Other |  |

## 3.6 Assumptions, unknowns, and dependencies

| ID | Type | Statement | Decision impact |
|---|---|---|---|
|  | Assumption / Unknown / Dependency / Evidence gap |  |  |

## 3.7 Management-System Linkage (Optional)

Use this subsection only when policy, process, or SOP implications materially affect the option choice.

Do not force the options paper itself into L2-L5.

Instead, state only the relevant links, such as:
- governing policy or sub-policy references
- related process implications
- related SOP or work-instruction implications
- unresolved management-system gaps that could change the recommendation

# 4. Option Set Definition

## 4.1 Comparison baseline

Describe the current state or do-nothing baseline used as the reference point.

## 4.2 Option list

| Option ID | Option name | Option type | Short description | Why included |
|---|---|---|---|---|
|  | Process / System / Data / Governance / Operating Model / Mixed |  |  |  |

## 4.3 Excluded or parked options

| Option or idea | Why excluded from the main comparison |
|---|---|
|  |  |

## 4.4 Comparability check

Before comparing options, make the following explicit:
- are the options mutually exclusive or can they be combined
- are the options at the same decision level
- is one option actually a phased path rather than a true alternative
- is the option set complete enough for the current decision

# 5. Evaluation Logic

## 5.1 Decision criteria

Use the following criteria unless there is a good reason to adapt them.

| Criterion | Core question | Weight (Optional) | Non-negotiable? | Notes |
|---|---|---|---|---|
| Business value | What business outcome, control improvement, or user-behavior change does this option create? |  |  |  |
| Strategic fit | How well does this option support HR digital direction and business priorities? |  |  |  |
| Global deployability | Can this option scale globally with governed local variance? |  |  |  |
| Governance fit | Does this option support decision rights, control logic, compliance expectations, and review cadence? |  |  |  |
| Architecture implications | Does this option fit or improve the target capability and solution landscape? |  |  |  |
| Data and analytics implications | Does this option improve data quality, decision support, and measurement logic without creating unmanaged data burden? |  |  |  |
| Operation management implications | Can this option be governed, adopted, monitored, maintained, and value-reviewed after or beyond implementation? |  |  |  |
| Team / vendor / execution implications | Can the current or target team and vendor model deliver and sustain this option with acceptable complexity and risk? |  |  |  |
| Cost effectiveness and ROI logic | Does the lifecycle value justify the investment, operating cost, and change burden? |  |  |  |
| Risks and trade-offs | Are the major downside risks and accepted trade-offs visible and manageable? |  |  |  |

## 5.2 Rating approach

Use one rating approach consistently across the paper.

Typical choices:
- High / Medium / Low
- Strong / Moderate / Weak
- 1 to 5 scale
- Better / Similar / Worse versus baseline

Rules:
- use `Unclear` when evidence is weak
- do not force false precision
- do not hide a qualitative judgment behind a misleading numeric score

## 5.3 Recommendation rule

Apply the following logic before making a recommendation:
1. eliminate any option that fails a true non-negotiable
2. prefer business and lifecycle value over implementation convenience only
3. prefer global core with governed local variance over unmanaged exception when overall value is comparable
4. treat governance, data, analytics, operation management, and adoption burden as decision criteria, not as post-decision cleanup
5. if uncertainty remains material, recommend a prototype, pilot, staged path, or explicit defer decision rather than pretending the answer is settled

# 6. Cross-Option Comparison

## 6.1 Comparison matrix

Add or remove option columns as needed.

| Criterion | Weight | Option A | Option B | Option C | Decision note |
|---|---|---|---|---|---|
| Business value |  |  |  |  |  |
| Strategic fit |  |  |  |  |  |
| Global deployability |  |  |  |  |  |
| Governance fit |  |  |  |  |  |
| Architecture implications |  |  |  |  |  |
| Data and analytics implications |  |  |  |  |  |
| Operation management implications |  |  |  |  |  |
| Team / vendor / execution implications |  |  |  |  |  |
| Cost effectiveness and ROI logic |  |  |  |  |  |
| Risks and trade-offs |  |  |  |  |  |

## 6.2 What really differentiates the options

State the few differences that actually drive the decision.

Typical drivers:
- business value gap
- governance or control gap
- global deployability gap
- architecture fit gap
- data or analytics value gap
- operating burden gap
- execution risk gap
- lifecycle cost or ROI gap

## 6.3 Stakeholder fit view

| Stakeholder group | Preferred option or concern | Why |
|---|---|---|
| CoE Heads |  |  |
| Regional HR Leaders |  |  |
| HRBP Leaders |  |  |
| HR Solution / Delivery |  |  |
| Other stakeholders |  |  |

## 6.4 Sensitivity or scenario check (Optional)

Use this subsection when the leading option changes under different assumptions.

| Scenario or constraint | Leading option | Why |
|---|---|---|
| Speed first |  |  |
| Lowest cost first |  |  |
| Global consistency first |  |  |
| Local flexibility first |  |  |
| Lowest operating burden first |  |  |

# 7. Recommendation and Trade-offs

## 7.1 Recommended option

State the recommended option clearly.

## 7.2 Why this option wins now

Explain why this option is the right choice now, not only in theory.

## 7.3 Why the alternatives are not recommended now

Explain why the other options lose, are deferred, or should be treated as later-stage possibilities.

## 7.4 Trade-offs consciously accepted

State the trade-offs that are being accepted with the recommendation.

## 7.5 Conditions and guardrails

State the conditions that must remain true for the recommendation to stay valid.

Examples:
- governance guardrails
- phased rollout boundaries
- local variance approval conditions
- architecture or data prerequisites
- adoption and change prerequisites

## 7.6 Decision ask

State the exact approval, endorsement, or alignment required from the decision forum.

# 8. Landing and Next Step

## 8.1 Decision restatement, level-or-linkage declaration, and Own / Watch

Complete this section using the structure below, per [OS] §5.4.

Note: Own and Watch are document-content expectations for this deliverable, not a response-layer reasoning protocol. Per [OS] §5.4, the Level-or-linkage declaration is the only dimension that requires explicit response-layer enforcement; Frame, Land, Own, and Watch are already covered by the default Evidence / Assumptions / Inference / Conclusions / Implications response structure.

### 8.1.1 Decision restatement
Restate the framed business decision in one line and name the recommended option.

- Framed business decision:
- Recommended option:

### 8.1.2 Level-or-linkage declaration
Declare per [OS] §5.4.

- If this options paper is being used as, or converted into, a management-system output, state the intended landing level (L2, L3, L4, or L5) when clear enough, or state the ambiguity and what must be clarified to resolve it.
- If this options paper is being used as a specification output whose downstream correctness depends on management-system context, state the governing management-system linkage when it materially affects framing, review, or downstream design; omit the declaration when linkage is irrelevant.

### 8.1.3 Own

State explicit ownership for the next step.

- Owner:
- Reviewer:
- Decider:

### 8.1.4 Watch
State the signals that will show whether the recommendation is working, with cadence.

| Signal type | Signal | Cadence |
|---|---|---|
| Leading |  |  |
| Lagging |  |  |
| Adoption |  |  |
| Utilization |  |  |
| Value |  |  |

## 8.2 Immediate next steps

State the next artifact explicitly. Typical next artifacts after this options paper include:
- `[TPL] PRD / Prototype / MVP Spec Template` output (PRD, MVP Brief, or Prototype Brief) when the recommended option needs to be specified for build or pilot
- a policy, process map, governance mechanism, or operating-model artifact when the recommendation lands primarily as a management-system output
- a prototype or pilot brief when material uncertainty remains and a learning-first path was recommended
- a further options paper at a narrower decomposition level when this paper surfaces a downstream decision that also needs structured comparison

| Action | Owner | Timing | Expected output |
|---|---|---|---|
|  |  |  |  |

# 9. Supporting Modules (Optional)

Complete only the modules that materially improve decision quality.

## 9.1 Per-option deep dive

Repeat this subsection only for options that need additional explanation.

### Option [ID] — [Option Name]

- **Short description**:
- **When this option makes sense**:
- **When this option does not make sense**:
- **Key dependencies / preconditions**:
- **Likely stakeholder reactions**:
- **Main uncertainties**:

| Dimension | Assessment | Rating | Notes / uncertainty |
|---|---|---|---|
| Business value |  |  |  |
| Strategic fit |  |  |  |
| Global deployability |  |  |  |
| Governance fit |  |  |  |
| Architecture implications |  |  |  |
| Data and analytics implications |  |  |  |
| Operation management implications |  |  |  |
| Team / vendor / execution implications |  |  |  |
| Cost effectiveness and ROI logic |  |  |  |
| Risks and trade-offs |  |  |  |

## 9.2 Business value and ROI notes

Use this module when the economics or value logic needs more than summary treatment.

Suggested content:
- value hypothesis
- benefit categories
- cost categories
- time-to-value logic
- assumptions behind ROI or cost-effectiveness judgment
- what would make the case no longer attractive

## 9.3 Architecture, data, analytics, and operation management notes

Use this module when these implications materially affect the recommendation.

Suggested content:
- architecture fit or target-state implications
- integration or platform constraints
- data ownership, quality, and interoperability implications
- analytics or measurement implications
- operating ownership, review cadence, release response, enhancement path, and documentation expectations

## 9.4 Team, vendor, and execution notes

Use this module when delivery feasibility or operating ownership is a major differentiator.

Suggested content:
- internal capability implications
- vendor dependency or leverage implications
- change burden
- sequencing and implementation complexity
- support model implications

## 9.5 Risks, dependencies, and sensitivity notes

Use this module when the recommendation is sensitive to uncertainty.

Suggested content:
- downside scenarios
- critical dependencies
- unresolved issues
- trigger conditions for re-decision
- pilot or prototype logic when needed

## 9.6 Appendix

Include supporting material only when it improves decision quality.

Examples:
- detailed cost model
- architecture notes
- vendor or market notes
- stakeholder interview summary
- prototype screenshots or linked artifacts
- prior papers or reference material

Use the appendix to support the recommendation, not to hide it.

# 10. Document Quality Checklist

Before circulating the paper for review or using it as the source for an executive readout, check the following:

- [ ] The decision ask is explicit.
- [ ] The recommendation is explicit.
- [ ] The option set contains real and comparable options.
- [ ] The current baseline, constraints, and non-negotiables are visible.
- [ ] Business value, strategic fit, global deployability, governance fit, architecture implications, data and analytics implications, operation management implications, team / vendor / execution implications, cost effectiveness and ROI logic, and risks / trade-offs are all assessed at the right level.
- [ ] The core paper contains the logic needed for later executive compression.
- [ ] Supporting modules are used only where they improve decision quality.
- [ ] The paper is business-first and capability-first, not vendor-first.
- [ ] Lifecycle value is considered, not only implementation convenience.
- [ ] Global invariants and local variance logic are visible.
- [ ] Management-system linkage is stated when materially relevant, without forcing the paper itself into L2-L5.
- [ ] The recommendation explains why the alternatives are not recommended now.
- [ ] The trade-offs are visible and owned.
- [ ] The next artifact, owner, and watch logic are explicit.
- [ ] Material uncertainty is marked honestly.
- [ ] Language mode matches the audience.
- [ ] If the final document will be uploaded to DingTalk Docs, the final Markdown has been normalized per [RULE] DingTalk Markdown Format Control Specification.
