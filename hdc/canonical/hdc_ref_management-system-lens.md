# HR Management-System Lens

- **Status:** transformed chat-project replica; not SOT
- **Active source(s):** `2_topics/hr-digital/management-system-lens.md`
- **Conversation boundary:** provides a neutral classification and reasoning lens for HDC discussion; it does not classify a company artifact, assign authority, or create a management-system requirement by itself

## 1. Why the lens exists

The lens prevents policy, Process, SOP, specification, and working notes from being discussed as if they were the same kind of artifact.

It contains two independent axes:

1. a **governance axis** — what governs or constrains;
2. a **work-architecture axis** — how customer-outcome work decomposes.

## 2. Governance axis

### L1 — Functional domain context

Identifies the enterprise function that owns the management-system context, such as HR. L1 is context, not a detailed policy layer.

### L2 — Policy

States what must be true and why for a durable management domain.

Typical content:

- purpose and scope;
- control intent;
- mandatory principles or requirements;
- ownership and decision rights;
- governed boundaries;
- variance logic.

Policy should not be written as a sequence of tasks.

### L3 — Durable sub-policy domain

Narrows an L2 policy only when a stable sub-domain or governed variance needs its own policy logic.

L3 is not a default layer and should not contain lifecycle phases, meeting forums, products, modules, or temporary work.

### L4 — Process

Defines how one bounded unit of work behaves.

A Process may use:

- structured flow;
- adaptive case handling;
- reusable decision logic;
- a deliberate hybrid.

Each Process has one parent Value Stream and may have several governing-policy references.

### L5 — SOP or work instruction

Defines how a recurring activity or control within a Process is performed consistently.

L5 is detailed enough for repeatability but should not replace the end-to-end Process model.

## 3. Work-architecture axis

Use:

**Value Stream → Process → SOP or work instruction**

### Value Stream

An end-to-end system of work organized around a customer and outcome. It has a trigger, outcome, end-to-end owner, and maintained view of flow.

### Process

A bounded unit of work within one Value Stream.

### SOP or work instruction

Detailed guidance for recurring activities within a Process.

### Value Stream Mapping

A way to observe, understand, and improve the current and future flow of a Value Stream. It is not another management-system level.

## 4. Relationship invariant

Keep these relationships separate:

| Relationship | Meaning |
|---|---|
| Policy → Process | Governance or constraint |
| Value Stream → Process | Work decomposition |
| Process → SOP or work instruction | Detailed work trace |
| Value Stream Mapping → Value Stream | Observation and improvement representation |

Policy is not the parent node of Process in the work architecture.

## 5. Artifact classification

### 5.1 Management-system output

An artifact intended to land as Policy, Process, or SOP/work instruction.

It should declare its intended level and respect the boundaries of that level.

### 5.2 Specification output

An artifact describing required product, service, data, integration, reporting, or experience behavior.

It remains outside L1–L5. When materially relevant, it should state which policy or Process governs or constrains it.

### 5.3 Working artifact

A discussion memo, option comparison, draft brief, workshop output, or exploratory model.

It is not automatically a management-system or specification output. Early discussion should default here unless another status is explicit.

### 5.4 Source candidate

A reusable lesson or stable pattern proposed for an authoritative source.

Candidate status is appropriate only when recurrence, abstraction, coverage gap, and maintenance value are credible. A candidate is not authoritative merely because it is well written.

### 5.5 Unresolved or mixed

Use this when an artifact combines types or its intended landing is genuinely unclear. Preserve the ambiguity and identify the clarification needed.

## 6. Classification questions

Ask:

1. What is the artifact trying to govern, describe, or decide?
2. Is it durable management content, a bounded specification, or working discussion?
3. If management content, what level owns its primary purpose?
4. Does it mix control intent with work sequence?
5. Does it mix a Value Stream decomposition with a policy taxonomy?
6. What governing linkage matters without changing the artifact’s type?

## 7. Common category errors

- A lifecycle stage is labeled an L3 policy domain.
- A product module is treated as a policy category.
- A workflow diagram is treated as policy because it contains approvals.
- A detailed specification is forced into L4 or L5.
- A Policy is presented as the parent of a Process.
- A Value Stream map is treated as a static charter or a sixth level.
- A working memo acquires authority through repeated circulation without an explicit decision.

## 8. Discussion output declaration

When level or linkage matters, state:

- output family;
- proposed level, if it is a management-system output;
- governing linkage, if it is a specification;
- unresolved classification question, if material;
- what would need to be decided before the classification changes.
