# [PRIN] People Experience Design Principles

- **Project**: HR Digital Cockpit
- **Document Type**: Principles
- **Status**: Active canonical
- **Role**: Durable topic-specific design principles for People Experience work in this hub
- **Source Category**: Cat 2
- **Management-System Role**: Cross-topic design-judgment layer for People Experience topics; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Boundary note**: Also admissible in Cat 4 UI scope per [OS] §2.3.2.
- **Template position**: No active canonical People Experience design template is designated at this time. When one priority moment must be turned into an explicit design artifact, use a fit-for-purpose chat draft, working memo, roadmap element, or downstream specification artifact until a lighter template is justified.
- **Relationship to [OS]**: Serves the [OS]-defined Think-Specify-Orchestrate-Harvest loops for People Experience topics; narrows the cross-topic digital judgment layer into journey-first experience-design logic.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Companion source. The existing digital-decision principles remain the cross-topic parent judgment layer. This source narrows that judgment into People Experience-specific design logic.
- **Relationship to [REF] People Journey and Moments Catalog**: Uses the catalog as the canonical reference spine for lifecycle stages and moments.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [PRIN] People Experience Design Principles` header fields per [OS] §8.5.1a)

## How to use this source

Use this source when:
- the business issue is primarily about employee, manager, or HRBP experience across a journey, transition, or moment
- the work needs journey-first design logic rather than only system-first or process-first logic
- a lifecycle moment must be prioritized, shaped, or translated into a reusable experience blueprint
- the work will later become a roadmap, prototype brief, PRD, or handoff specification for an ESS, MSS, portal, workflow, or service experience

Do not use this source as:
- a replacement for `[PRIN] HR Digital Decision Design Principles`
- a vendor comparison guide
- a policy manual
- a process repository
- a full journey catalog
- a PRD, handoff spec, or implementation design

# 1. Position in the source architecture

This source is the People-Experience-specific design-judgment layer; for the formal ownership boundary against the parent and reference sources, see the §2.2 table.

# 2. Boundary with `[PRIN] HR Digital Decision Design Principles`

## 2.1 Decomposition axis

- **`[PRIN] HR Digital Decision Design Principles`**
  - decomposition axis = **cross-topic digital judgment**
  - core question = **How should HR Digital work be judged and structured, regardless of topic?**
- **`[PRIN] People Experience Design Principles`**
  - decomposition axis = **People Experience design quality**
  - core question = **How should we design employee-facing or manager-facing experiences once People Experience is the chosen topic?**

## 2.2 Ownership boundary

| Source | Owns | Explicitly excludes |
|---|---|---|
| `[PRIN] HR Digital Decision Design Principles` | business-first reasoning, capability-first judgment, global core vs local variance, lifecycle value, governance and value-realization logic, separation of policy/process/system/data/analytics/governance | topic-specific People Experience rules, journey catalog content, reusable moment blueprints |
| `[PRIN] People Experience Design Principles` | journey-first design rules, moment prioritization logic, persona logic, digital-vs-human interaction logic, manager-led experience logic, continuous listening and iteration logic for People Experience topics | general source-governance rules, policy architecture, full data-governance logic, vendor or platform selection logic, journey catalog reference content |
| `[REF] People Journey and Moments Catalog` | stable lifecycle stages and moments used as reference | principles, prioritization method, design-template logic |

## 2.3 Usage sequence

Use the sources in this order:

1. Apply `[PRIN] HR Digital Decision Design Principles` to frame the business issue, identify the primary design object, and decide whether People Experience is the right topic lens.
2. If People Experience is in scope, apply this source to design the experience logic.
3. Use `[REF] People Journey and Moments Catalog` to choose the lifecycle stage and moment.
4. Use a fit-for-purpose working artifact when one priority moment must become a structured design artifact.
5. Move into roadmap, PRD, prototype, or handoff artifacts only after the above are stable enough.

# 3. Principles

## 3.1 Journey-first, not function-first

Design around the employee's lived journey and the outcome they are trying to achieve, not around HR functional ownership or system module boundaries.

**Rationale**

This prevents the failure where a single employee moment is fragmented across HR function and system silos, so the employee must understand the organization's internal structure to complete one task. Functional ownership is an internal convenience; designing to it pushes the integration burden onto the user.

**Apply by**
- starting from a lifecycle stage and moment
- describing the desired user outcome in plain employee language
- connecting policy, process, system, content, and service around that moment

**Red flags**
- the design is grouped by HR departments only
- the user must understand internal system structure to complete a simple task
- one moment is fragmented across multiple disconnected tools without a deliberate orchestration layer

## 3.2 Moments that matter first

Not every experience point deserves the same design depth. Prioritize the moments that are most common, most memorable, most risky, or most clearly painful.

**Rationale**

This prevents the failure where design effort is spread evenly across every moment, so the consequential moments are under-designed and the trivial ones are over-analyzed. Treating all moments as equally urgent turns the journey catalog into an undifferentiated backlog and stalls real design action.

**Apply by**
- ranking moments by frequency, emotional intensity, business value, risk, or friction
- focusing initial design effort on the most consequential moments
- avoiding lifecycle-wide "boil the ocean" redesign before priority moments are stabilized

**Red flags**
- every moment is treated as equally urgent
- the catalog becomes a backlog dump
- analysis expands faster than design action

## 3.3 Employee lens before HR lens

Describe the moment from the employee, manager, or HRBP point of view before translating it into service, workflow, or system terms.

**Rationale**

This prevents the failure where a moment is framed in HR transaction language from the start, so the design optimizes process and reporting neatness rather than what the user is actually trying to do, know, or feel. Once a moment is named as a transaction, the user's real need becomes invisible to the design.

**Apply by**
- writing the moment in first-person or user-centered language first
- testing whether the design solves what the user is actually trying to do, know, or feel
- treating HR function labels as downstream translation, not the starting point

**Red flags**
- the moment name is only an HR transaction name
- the design is understandable only to HR or system specialists
- the proposed experience solves reporting or process neatness more than user friction

## 3.4 Persona and context over "average employee"

People Experience design should not assume one universal employee. Different personas and contexts experience the same moment differently.

**Rationale**

This prevents the failure where a design built for an "average employee" works acceptably for no one, because the personas whose experience consequences differ most — frontline vs office, new vs tenured, manager vs individual contributor — were never tested. An average employee does not exist; designing for one hides where the experience actually breaks.

**Apply by**
- overlaying persona, location, worker type, manager context, and work environment on the same journey
- separating global invariant moments from persona-specific or local variants
- using persona logic to target design attention where experience consequences differ materially

**Red flags**
- design is built on an "average employee" assumption
- one global design is applied without persona testing
- persona variation is acknowledged but never reflected in design choices

## 3.5 Digital where digital is best, human where human is best

Some moments are best served digitally; others require human empathy, escalation, or interpretation. Design knows when to switch.

**Rationale**

This prevents the failure where moments that need human empathy are forced into self-service to look efficient, so an employee in a high-stakes or emotional situation is reduced to filling in a form. Efficiency optimized without regard to the moment's emotional load degrades exactly the experiences that matter most.

**Apply by**
- mapping when an employee benefits from self-service, automation, or knowledge access
- mapping when an employee benefits from a human (manager, HRBP, specialist) interaction
- making escalation paths clear and short
- using AI thoughtfully, not as a default

**Red flags**
- everything is forced into self-service to look efficient
- empathy-required moments are reduced to a form
- AI is used as a brand statement instead of a service decision

## 3.6 Manager-led experience by design

Many People Experience outcomes hinge on the manager. Design the manager's experience explicitly, not as an afterthought.

**Rationale**

This prevents the failure where an employee experience depends on manager action but the manager is absent from the design, so the experience either fails silently or the manager is handed new responsibilities with no enablement, prompts, or visibility. A journey that relies on managers but does not design for them is relying on chance.

**Apply by**
- making manager moments part of the journey design
- providing manager visibility, prompts, prep, and decision support
- distinguishing manager actions from HR actions and employee actions
- protecting employee experience from manager-process burden when possible

**Red flags**
- the employee experience depends heavily on managers but managers are absent from the design
- manager experience is treated as a separate afterthought
- the design adds manager responsibilities without enablement, guardrails, or signal visibility

## 3.7 Transition quality matters as much as steady-state efficiency

Entry, role change, leave and return, mobility, and exit moments should be designed as transitions, not just as administrative events.

**Rationale**

This prevents the failure where a transition is designed as a status-change transaction that ends at the point of approval, so the employee is left without readiness, support, or ramp-up through the period when experience consequences are highest. Transitions are where trust and retention are won or lost; treating them as paperwork forfeits that.

**Apply by**
- designing for readiness, clarity, support, handover, ramp-up, and follow-through
- recognizing crossboarding, return-to-work, and internal moves as distinct transition journeys
- protecting the first 90 days of a new context as a priority period

**Red flags**
- internal transfers are treated as a basic employee change transaction
- return from leave has no explicit support logic
- the journey ends at the point of approval rather than the point of successful transition

## 3.8 Continuous listening and iteration by design

People Experience design is not finished at launch. It needs feedback signals and management action loops.

**Rationale**

This prevents the failure where a design is treated as complete at launch, so it has no feedback signals and no adjustment mechanism and silently drifts out of fit as the workforce and context change. Surveys without a management action path generate listening fatigue while producing no improvement.

**Apply by**
- defining experience signals, adoption signals, and value signals from the start
- linking measurement to management action rather than to reporting volume
- using lifecycle feedback, friction signals, and support-volume patterns to refine the design

**Red flags**
- surveys exist without a management action path
- adoption is assumed rather than evidenced
- the design has no post-launch adjustment mechanism

## 3.9 Global core journey, governed local variance

Applies `[PRIN] HR Digital Decision Design Principles` §3 (Global core with governed local variance) to People Experience journey and moment design.

**Apply by (PE-specific)**
- defining the global invariant journey and moment first
- separating mandatory local variance from historical habit when overlaying personas, countries, or worker segments on the same journey
- making approved local differences in a moment explicit in terms of reason, owner, and review logic

**Red flags (PE-specific)**
- every country customizes the same moment independently with no governed variance logic
- local preferences are silently absorbed into the core moment design
- global consistency destroys necessary local usability, accessibility, or compliance in a specific moment

**Boundary with §3.4**

§3.4 and §3.9 both address global-invariant-vs-local-variant decomposition but at different layers: §3.4 governs *whether and how* personas and contexts make the same moment differ, so design attention is targeted where experience consequences diverge; §3.9 governs *how an approved difference is held* — which part of a moment stays globally consistent and which local variance is justified, owned, and reviewed. Use §3.4 to discover where personas diverge, and §3.9 to govern the variance that divergence justifies.

## 3.10 Design must land as an artifact

Applies `[PRIN] HR Digital Decision Design Principles` §12 (Make important work executable) to People Experience design output.

**Apply by (PE-specific)**
- naming the next People Experience artifact explicitly (priority-moment blueprint, roadmap element, prototype brief, PRD, or handoff spec)
- converting high-priority moments into a structured working artifact at the lightest useful level
- making owners, dependencies, watch signals, and open issues visible at moment granularity

**Red flags (PE-specific)**
- the moment stays at inspiration level and never becomes a design object
- no priority moment is made explicit enough for product or service design
- the concept cannot survive without verbal explanation of employee-lens logic

## 3.11 Design AI–employee interaction with employee-felt dignity

Applies `[PRIN] HR Digital Decision Design Principles` §13 (Design human–AI collaboration with the same rigor as human-to-human collaboration) to People Experience moments where AI participates in employee-facing service delivery, manager-facing tooling, or HRBP-facing decision support.

PE-specific framing: in People Experience contexts the AI participant interacts with people during moments that carry emotional weight, career consequence, or trust load — onboarding clarity, performance feedback, life-event support, exit conversation. PE-specific design therefore preserves the parent principle's substantive requirements while adding an employee-felt dimension that determines whether the same mechanism lands as supportive or as evaluative-surveillance.

**Apply by (PE-specific)**
- specifying autonomy boundary in employee-recognizable terms — what the AI decides on its own (e.g., routing a benefits question, surfacing leave-policy text), what it surfaces for human handoff (e.g., a manager review, an HRBP escalation), and making this boundary visible to the employee at the moment, not buried in policy
- specifying checkpoint surfacing that respects the moment's emotional load — high-emotion moments (bereavement, return-from-leave, exit) require a human checkpoint by default; low-stakes informational moments may run AI-only with clear escalation paths
- specifying trust calibration with both directions visible — autonomy may expand as the AI's competency boundary is empirically demonstrated, but the employee must perceive expanding autonomy as continued reliability rather than as quiet de-staffing of human support
- specifying fallback path that preserves dignity — when AI is rejected, unavailable, or out of scope, the fallback must not require the employee to re-explain their situation from scratch or queue behind a generic ticket
- designing tone and framing as a first-class design surface, not an afterthought — wording, response timing, and surface-level acknowledgment shape whether the employee experiences AI participation as helpful guidance, neutral utility, or implicit evaluation; this dimension is symmetric across employee-facing AI, manager-facing AI, and HRBP-facing AI

**Red flags (PE-specific)**
- AI participates in high-emotion moments (loss, illness, exit, conflict) without an explicit human checkpoint, on the assumption that "the AI handles it efficiently"
- the employee cannot tell whether the response in front of them came from AI, from a human, or from a hybrid hand-off — and the design treats this opacity as acceptable
- AI checkpoint surfaces to the manager or HRBP carry implicit evaluative framing of the employee (e.g., "this employee asked the same question 4 times" presented as a flag rather than as a service-design signal)
- trust calibration is visible only to the operator side; the employee experiences silently expanding AI autonomy with no signal that the human-handoff threshold is being raised
- fallback path treats AI unavailability as "ticket queue" rather than as warm handoff to a named human role, especially during transition moments (entry, return, exit)
- tone and framing are inherited from generic chatbot defaults instead of being designed against the moment's emotional contour

# 5. Default review questions

Use these questions to review People Experience work. The list is aligned one-to-one with the principles §3.1-§3.11:

1. (§3.1) What lifecycle stage and moment is this work actually about, and is the design organized around the employee's journey rather than HR function or system boundaries?
2. (§3.2) Is this a truly priority moment or just a visible one?
3. (§3.3) Is the moment described from the employee, manager, or HRBP point of view before being translated into service, workflow, or system terms?
4. (§3.4) Which personas and contexts experience this moment differently, and where does that divergence change the design?
5. (§3.5) What part should be digital and what part should remain high-touch?
6. (§3.6) What manager behavior is part of this experience, and is the manager's experience designed explicitly?
7. (§3.7) Are entry, role change, leave-and-return, mobility, and exit moments designed as transitions rather than administrative events?
8. (§3.8) What listening or signal logic, linked to management action, will show whether the design works after launch?
9. (§3.9) What should be standardized globally and what local variance is genuinely justified, owned, and reviewed?
10. (§3.10) What next artifact should this become?
11. (§3.11) Where AI participates in this PE moment, is the AI–employee interaction designed for employee-felt dignity (autonomy boundary, checkpoint, trust calibration, fallback, tone)?
