# HR Digital Design Principles

- **Status:** transformed chat-project replica; not SOT
- **Active source(s):** `2_topics/hr-digital/principles.md`
- **Conversation boundary:** guides HDC reasoning and option comparison only; it does not approve a policy,
  solution, investment, or organizational action

## How to use these principles

Apply the principles at decision moments rather than as a sequential checklist. Red flags are prompts to investigate, not a score.

## 1. Business-first, architecture-enabled

Start with the business outcome, operating problem, decision need, and stakeholder effect. Use architecture to test feasibility, scale, risk, and lifecycle fit.

Ask:

- What becomes better if this succeeds?
- Whose behavior, decision, control, or experience changes?
- Is the proposed architecture enabling the outcome or replacing it as the objective?

Red flag: the discussion begins with product modules or technical structure before the business change is clear.

## 2. Capability-first, not product-first

Define the required capability in business and operating terms before selecting its product expression.

Consider build, buy, extend, partner, pilot, or defer only after the capability boundary is clear. Product feature presence is not proof of need.

## 3. Global core with governed local variance

Define the global invariant first, then classify each proposed local difference:

| Class | Test | Discussion expectation |
|---|---|---|
| Mandatory | A binding authority makes the global default unusable locally. | Name the authority and the affected invariant. |
| Economically justified | The global default is allowable but creates a quantified net loss greater than variance cost. | State the case, owner, complexity cost, and review condition. |
| Preference-based | The difference reflects habit or taste without compulsion or quantified value. | Default to the global invariant. |

“Country-specific” is a location label, not a justification.

## 4. Lifecycle value over short-term convenience

Compare options across introduction, growth, mature operation, and retirement.

Include:

- adoption and change burden;
- maintenance and supportability;
- extensibility and data consequences;
- operating ownership;
- deprecation and transition cost;
- value realization over time.

Launch convenience alone is not lifecycle value.

## 5. Mechanism over ad hoc control

When repeatability matters, discuss an explicit mechanism:

- ownership;
- decision rights;
- review cadence;
- escalation logic;
- exception handling;
- evidence and value signals.

If success depends on one person repeatedly chasing others, the design is incomplete.

## 6. Operation management and value realization by design

A solution proposal should explain how it would be governed, adopted, reviewed, maintained, changed, and retired.

Minimum discussion checks:

- accountable owner;
- access and control logic;
- operating review cadence;
- maintenance and lightweight-change path;
- documentation expectations;
- utilization, experience, risk, and value signals.

## 7. Analytics-informed decisions

Begin with the decision that needs evidence. Then define the signal.

Distinguish:

- leading and lagging indicators;
- diagnostic signals;
- adoption and utilization;
- value and outcome;
- risk and control.

A metric without a management response is reporting volume, not decision support.

## 8. Separate policy, Process, system, data, analytics, and governance

| Object | Question |
|---|---|
| Policy | What must be true and why? |
| Process | How does one bounded unit of work behave? |
| System | What must a solution enable, control, prevent, or record? |
| Data | What entities, definitions, structures, lifecycle rules, and controls are required? |
| Analytics | What decisions need evidence, and how will signals change action? |
| Governance | Who decides, reviews, owns, escalates, and revisits? |

Policy governs or constrains Process; it is not the decomposition parent of Process. Value Stream decomposes into Process, and Process may be supported by SOPs or work instructions.

## 9. Prototype to learn

Use a prototype only when a named uncertainty can be reduced by it.

Before discussing the prototype, state:

- the learning question;
- the smallest scope needed;
- the evidence to observe;
- success, failure, and inconclusive conditions;
- the decision that follows each result.

A prototype is not a hidden commitment to the proposed solution.

## 10. Use MECE for important decomposition

Before creating sibling categories:

- name one decomposition axis;
- define what each category includes and excludes;
- test material overlap;
- test coverage gaps;
- separate ownership from interface relationships.

A neat diagram does not compensate for mixed axes.

## 11. Definition quality before naming quality

Stabilize meaning, scope, inclusion, exclusion, and interfaces before optimizing names.

Provisional names are acceptable during exploration. Freeze terminology only when the underlying logic is stable enough to support decisions.

## 12. Make important reasoning usable

Important discussion should leave the operator with:

- a clear conclusion or decision question;
- the decisive grounds and assumptions;
- the material trade-off or unresolved issue;
- the condition that would change the conclusion;
- the next question or action only when one is genuinely needed.

Conceptual strength without a usable conclusion remains difficult to apply. Usability does not require a
formal artifact.

## 13. Design the human–AI operating relationship explicitly

When AI participates in HR service, decision support, or work alongside humans, discuss:

- what it may do independently;
- what remains a human judgment or checkpoint;
- what reasoning trace or explanation a person needs;
- how a person can challenge or correct an outcome;
- what happens when AI is unavailable, rejected, or out of scope;
- how autonomy should change as evidence and calibrated trust change.

In high-impact employment decisions, opacity, silent autonomy, and tool-default decision rights are red flags.

## 14. Preserve ambiguity rather than fabricate resolution

When a rule, requirement, number, name, or design choice is genuinely unresolved:

- name the ambiguity;
- attribute it to its source;
- show candidate interpretations and consequences;
- request the minimum authoritative clarification;
- keep the issue visible until it is resolved.

An internally tidy draft is not more valuable than an honestly incomplete one.

## 15. Organize HR work by Value Stream and preserve trace

Use one customer-outcome Value Stream spine:

**Value Stream → Process → SOP or work instruction**

Each Value Stream should have a customer, outcome, trigger, and end-to-end owner. Each Process should have one parent Value Stream and separate governing-policy references.

Lifecycle, function, geography, system, risk, and external taxonomies are overlays or views, not competing decomposition trees.

## 16. Match the model to work behavior

Choose a representation based on how the work actually behaves:

- structured flow when dependencies are sufficiently predictable;
- case-oriented treatment when facts emerge and authorized judgment is required;
- explicit decision models when reusable multi-criteria logic matters;
- a hybrid when these behaviors coexist.

Improvement methods should improve the identified system of work, not force every activity into a linear path or erase necessary discretion.

## Decision-use check

For a material HDC recommendation, ask:

- Which principles are load-bearing?
- What evidence supports their application here?
- Where do two principles create a real trade-off?
- What warrant resolves that trade-off?
- What new evidence would change the recommendation?
