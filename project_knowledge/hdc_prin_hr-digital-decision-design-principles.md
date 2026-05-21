# [PRIN] HR Digital Decision Design Principles

- **Project**: HR Digital Cockpit
- **Document Type**: Principles
- **Status**: Active canonical
- **Role**: Durable decision and design principles for HR digital work in this hub
- **Source Category**: Cross-category
- **Management-System Role**: Cross-topic judgment layer; outside L1-L5 hierarchy; admissible across all four task categories per [OS] §2.3.2; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Grounded in [OS] §0.1 project-level operating premises. Cross-topic judgment layer per [OS] §2.3.2 (admissible across all four work categories within their respective role anchors per [OS] §0.2).
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [PRIN]` header fields per [OS] §8.5.1a)

## How to use this source

Use this source when:
- framing an HR digital problem
- comparing options or trade-offs
- reviewing a proposed solution, vendor proposal, or design direction
- deciding whether work belongs in policy, process, system, data, analytics, or governance
- challenging work that feels operationally busy but strategically weak
- shaping source-ready artifacts, governance mechanisms, or handoff-ready outputs

Do not use this source as:
- a policy manual
- a process repository
- a vendor feature catalogue
- a project plan
- a substitute for architecture notes, PRDs, governance mechanisms, or operating baselines

## Application discipline

The fourteen principles below function as the operator's self-check tools at decision moments, not as a step-by-step methodology to follow sequentially. Principles are applied — not checked off. Red flags are decision-quality signals, not violations to count.

---

# 1. Business-first, architecture-enabled

**Rule**

Start with the business outcome, operating problem, decision need, and stakeholder impact. Use architecture to enable the right result, not to define the purpose.

**Apply by**
- stating the business change or decision first
- naming the target user behavior, control outcome, or value outcome
- using architecture to test feasibility, scalability, and risk
- refusing to let tool constraints become the business objective

**Red flags**
- the discussion starts with modules, tools, or configurations
- the proposed solution is technically elegant but weakly tied to business value
- stakeholders cannot explain what becomes better if the design succeeds

# 2. Capability-first, not vendor-first

**Rule**

Define the required capability before discussing the product expression of that capability.

**Apply by**
- describing the capability in business and operating terms first
- separating the needed outcome from the current platform implementation
- evaluating build, buy, extend, replace, or defer only after the capability is clearly defined
- keeping platform choice open when ROI, operating-model fit, lifecycle value, global deployability, privacy/compliance needs, or value gaps justify reconsideration

**Red flags**
- vendor terminology appears before capability definition
- product feature availability is treated as proof of business need
- the team optimizes around the current platform before confirming the right capability shape

# 3. Global core with governed local variance

**Rule**

Default toward global consistency, but allow local variance when the variance is justified, governed, and worth its complexity cost.

**Apply by**
- defining the global invariant first
- identifying whether the local difference is mandatory, economically justified, or only preference-based
- making every approved variance explicit in terms of reason, owner, control, and review logic
- designing for reuse before designing for exception

**Red flags**
- local preference is presented as a requirement without justification
- “country-specific” is used without separating legal need from historical habit
- variance is approved without ownership, expiry logic, or review cadence

# 4. Lifecycle value over implementation convenience

**Rule**

Choose designs based on whole-lifecycle value, not just implementation speed or configuration convenience.

**Apply by**
- evaluating introduction, growth, mature, and retirement implications
- testing for maintainability, extensibility, adoption burden, data implications, and change cost
- including post-go-live operating effort in the decision
- preferring the option that remains sound after the project closes, not only during delivery

**Red flags**
- the easiest implementation path creates expensive operating work later
- go-live success is treated as the same thing as solution success
- deprecation, release impact, or downstream change cost are ignored

# 5. Management mechanism over ad hoc control

**Rule**

Where repeatability matters, design a mechanism rather than relying on reminders, heroics, or informal coordination.

**Apply by**
- defining ownership, review cadence, decision rights, and escalation logic
- building lightweight but explicit governance into recurring work
- converting recurring coordination pain into a mechanism design problem
- treating “who decides, who reviews, how issues escalate, how we watch value” as part of the design

**Red flags**
- success depends on one person chasing others
- recurring work has no cadence or triage logic
- decision rights are assumed rather than designed

# 6. Operation management and value realization by design

**Rule**

Do not design only for delivery. Design for how the solution will be governed, adopted, monitored, maintained, and value-reviewed after or beyond implementation.

**Apply by**
- including operating ownership and review logic from the start
- designing permission logic, change paths, documentation expectations, and release response logic early
- defining how adoption, utilization, and value signals will be reviewed after go-live
- treating operation management as a management system, not as a synonym for technical maintenance

**Minimum design checks**
- ownership and operating review cadence
- permission and control logic
- release and maintenance response path
- lightweight enhancement and change path
- documentation and artifact expectations
- utilization and value realization signals

**Red flags**
- post-go-live governance is deferred as “later”
- support and maintenance are confused with full operation management
- no one can explain how the solution will be reviewed six months after launch

# 7. Analytics-informed digital decision making

**Rule**

Use analytics to improve decision quality, adoption visibility, and value realization, not to create reporting for its own sake.

**Apply by**
- starting with the decision that needs evidence
- linking metrics to specific management actions or judgments
- distinguishing leading signals, lagging signals, and diagnostic signals
- ensuring measurement logic supports business and operating decisions

**Red flags**
- metrics exist without a decision use case
- reporting volume is confused with decision quality
- adoption and utilization are assumed rather than evidenced

# 8. Separate policy, process, system, data, analytics, and governance

**Rule**

Treat these as different design objects with different purposes. Do not let ambiguity in one layer get hidden inside another.

**Working definitions**
- **Policy** = what must be true and why
- **Process** = how work flows across roles and steps
- **System** = what the solution must enable, control, automate, or prevent
- **Data** = what entities, definitions, structures, and controls are required
- **Analytics** = what decisions need evidence and how value or behavior will be measured
- **Governance** = who decides, who reviews, what escalates, and how control is maintained

**Apply by**
- classifying the primary issue before solutioning
- resolving policy ambiguity before forcing system decisions
- separating process redesign from tool configuration
- defining interfaces explicitly where multiple layers interact

**Red flags**
- system configuration is used to settle unresolved policy questions
- data quality problems are discussed as process problems without data design analysis
- governance gaps are hidden behind workflow detail

# 9. Prototype to learn, not to over-engineer

**Rule**

Use prototypes to reduce uncertainty, not to smuggle in premature production design.

**Apply by**
- stating the learning question before building
- limiting prototype scope to the uncertainty being tested
- defining success, failure, and next-decision criteria in advance
- using prototypes to test workflow logic, user response, control feasibility, and value assumptions

**Red flags**
- prototype scope expands because “we are already building it”
- no one can state what is being learned
- the prototype becomes a hidden implementation stream without governance

# 10. Apply MECE to important decomposition structures

**Rule**

For formal structures, use a clear decomposition axis and ensure the sibling buckets are mutually exclusive and collectively exhaustive at the chosen level.

**Apply by**
- naming the decomposition axis first
- defining what each sibling includes and excludes
- checking overlap explicitly
- checking coverage gaps against the parent scope explicitly
- separating interface relationships from ownership relationships
- validating the structure before using it in governance, templates, or source files

**Red flags**
- mixed decomposition axes in one structure
- sibling buckets overlap materially
- important parts of the parent scope have no home
- the structure looks neat but cannot support clean ownership or governance

# 11. Definition quality before naming quality

**Rule**

Stabilize scope, boundary, and logic before spending energy on labels.

**Apply by**
- defining what a thing is before optimizing what it is called
- testing inclusion, exclusion, and interface logic before final naming
- accepting provisional names during exploration
- freezing names only after the underlying logic is stable enough to govern work

**Red flags**
- long naming debates while scope remains unclear
- polished labels are used to mask weak boundaries
- teams align on terminology but not on meaning

# 12. Make important work executable

**Rule**

A sound idea is not complete until it can land as an artifact, mechanism, or governed next step.

**Apply by**
- stating the next artifact explicitly
- making owners, reviewers, and decision points visible
- defining what will be watched after the decision is made
- identifying the intended landing level where relevant
- turning principles into a concrete design, policy, mechanism, template, or baseline

**Red flags**
- the work remains conceptually strong but operationally vague
- no next artifact is defined
- no watch logic exists for whether the decision creates value

# 13. Design human–AI collaboration with the same rigor as human-to-human collaboration

**Rule**

When digital work involves AI agents executing on behalf of or alongside humans — whether in HR service delivery to employees, in management decision making, or in HR digital workspace tooling itself — design the human–AI interaction surface with the same rigor as the human-to-human interaction surface. The AI is not a tool to be configured; it is a participant whose interaction with humans must be designed.

**Apply by**
- specifying what the AI decides autonomously vs. what it surfaces for human checkpoint
- specifying what reasoning trace the AI must expose at each checkpoint, and at what abstraction level
- specifying how trust calibration evolves over time — autonomy expands as the AI's competency boundary is empirically demonstrated within scope; autonomy contracts if override rate or correction rate exceeds threshold
- specifying the fallback path that activates when AI output is rejected or AI is unavailable
- applying the principle symmetrically across employee-facing AI, decision-support AI, and operator-facing tooling AI

**Red flags**
- the AI's autonomy boundary is implicit, drifting, or set by tool defaults rather than design
- humans review AI output without a structured checkpoint surface (no digest, no reasoning trace, no escalation criteria)
- trust calibration is not re-evaluated as deployment matures
- no fallback path exists when AI is rejected, unavailable, or out of scope

**Note**

This principle does not preempt vendor-specific or platform-specific behavior; rather, it sets a cross-topic durable judgment lens that applies whenever AI is in the loop. Specific mechanism specifications (e.g., user-review budget, checkpoint cadence, digest format) belong in the relevant [RULE] or [TPL] sources.

# 14. Preserve ambiguity rather than fabricate resolution

**Principle**

When a business rule, requirement, or design decision is genuinely unresolved, preserve the ambiguity as an open question rather than collapse it into a single interpretation. This applies symmetrically to upstream framing work and to downstream specification artifacts: the obligation to surface unresolved ambiguity does not weaken as work moves from framing memo through PRD, TDD, intent, acceptance, and test plan.

**Rationale**

AI authoring loops have a strong drift toward producing plausible-sounding content even when load-bearing facts or decisions are absent. The drift is not a single bad choice but a sequence of small substitutions, each individually defensible: "I'll just pick the more common interpretation"; "I'll write what's most likely the intent"; "I'll pick a number that looks reasonable for now". Each substitution silently consumes a degree of freedom that was the operator's to spend. By the time downstream specification artifacts arrive, ambiguity that should have triggered a decision has been quietly resolved by inference, with no audit trail.

The mechanism that prevents this is not stronger AI judgment — it is a discipline that treats unresolved ambiguity as a first-class artifact element, named explicitly, attributed to its source, with proposed resolutions surfaced for operator decision rather than absorbed silently into prose.

**Apply by**

- naming the ambiguity explicitly in the artifact (framing memo, options paper, PRD, TDD, intent.md, acceptance.yaml, test-plan.yaml, etc.)
- attributing the ambiguity to its source (which stakeholder is undecided, which dependency is unresolved, which prior decision is pending)
- proposing 2–3 candidate resolutions with their downstream impacts when the resolution is materially decision-shaping
- requesting explicit operator authorization before collapsing the ambiguity to a single interpretation
- preserving the ambiguity in downstream artifacts when it remains material — do not silently settle a business-rule gap inside a PRD, TDD, intent, acceptance, or test plan that the upstream framing left open

**Red flags**

- a downstream specification artifact contains plausible-sounding but unverified business rules, numbers, or names
- ambiguity is silently resolved during conversion (PRD → TDD → intent → acceptance) without trace of when or why
- "I'll just pick one" pattern in artifact authoring without surfacing the choice as a decision the operator can review
- the open-questions section becomes a residual category of leftover items rather than a deliberate placeholder for material unknowns
- downstream artifacts contain more specificity than upstream artifacts justify (e.g., a TDD declaring concrete API field types when the PRD left the data shape open)
- a working assumption is added to make an artifact internally consistent without operator authorization, when the alternative resolution would meaningfully change scope or design

**Companion mechanism**

When operating under UP-defined Clarification Gate, this principle's surface-rather-than-fabricate stance is the corresponding upstream judgment: Clarification Gate is the runtime mechanism that fires when fabrication would occur; this principle is the design lens that keeps unresolved ambiguity visible across the artifact chain so the gate fires at the right moments rather than arbitrarily.

## Default review questions

Use these questions to review important HR digital work:
1. What business outcome or operating problem is this design addressing?
2. Is the required capability defined independently of the current vendor?
3. What is the intended global standard, and what local variance is truly justified?
4. What lifecycle cost or value is being created beyond implementation?
5. What mechanism will keep this working after the project ends?
6. What evidence will show adoption, utilization, or value realization?
7. Are policy, process, system, data, analytics, and governance clearly separated?
8. If there is a formal structure, is the decomposition MECE at the chosen level?
9. Are the definitions stable enough to justify the current names?
10. What is the next artifact, and who owns the next decision?
11. Where AI participates, is the human–AI interaction surface designed (autonomy boundary, checkpoint surfacing, trust calibration, fallback path)?
12. Where business or design ambiguity remains material, has it been preserved as an open question with attributed source and candidate resolutions, rather than silently resolved into prose?
