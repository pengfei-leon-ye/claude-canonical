# HDC Digital Solution Policy Architecture

- **Status:** transformed chat-project replica; not SOT
- **Active source(s):** `2_topics/hr-digital/policy-architecture.md`
- **Conversation boundary:** provides a controlled architecture for discussing HR Digital policy domains; it is not an issued policy, approved control framework, Process catalog, or work instruction

## 1. Purpose

The architecture positions the stable minimum policy domains used to discuss governance of HR Digital solutions.

It separates:

- formal time-bounded change;
- operation of a live solution;
- management of solution data as an asset.

It does not claim to contain every enterprise policy domain.

## 2. Management-system placement

| Level or status | HDC interpretation |
|---|---|
| L1 | HR functional context; outside this architecture’s detailed scope. |
| L2 | Landing level for the three major policy anchors. |
| L3 | Durable sub-policy domain, used only where the L2 scope needs stable decomposition. |
| L4 | Process governed or constrained by one or more policies; not a child of the policy in the work architecture. |
| L5 | SOP or work instruction supporting a recurring Process activity. |
| Outside L1–L5 | Specifications and working discussion artifacts, with governing linkage stated only when material. |

## 3. L2 policy anchors

| L2 policy domain | Definition | Intended role |
|---|---|---|
| Project Management Policy | Governs formal, time-bounded HR Digital change. | Connect intent to controlled delivery from initiation through closure. |
| Operation Management Policy | Governs how a live or post-introduction solution is controlled over time. | Cover access, use, maintenance, lightweight change, operating artifacts, and value review. |
| Data Asset Management Policy | Governs solution data across its lifecycle. | Cover meaning, structure, lifecycle, metadata, quality, security, and decision rights. |

## 4. Project Management Policy

Project Management Policy remains at L2 by default. Its lifecycle scopes are coverage lenses rather than L3 policy domains:

| Lifecycle scope | Governance concern |
|---|---|
| Initiation | Qualify the need, confirm sponsorship, and establish the initial change boundary. |
| Planning | Define scope, approach, ownership, dependencies, risks, and the control basis. |
| Delivery and Control | Manage agreed scope, time, quality, risk, issue, dependency, and change. |
| Deployment and Transition | Establish readiness for live use, including data, communication, learning, service, and operating ownership. |
| Closure | Confirm completion, remaining obligations, decision records, transition, and lessons. |

These scopes should not be promoted to L3 merely because they are named phases.

Boundary:

- formal time-bounded change belongs primarily here;
- steady-state control belongs primarily to Operation Management Policy;
- a program is a coordination posture for interdependent projects, not a default policy sub-domain.

## 5. Operation Management Policy

### 5.1 Permission Management

Governs who should have what access and how access is granted, changed, reviewed, and removed.

Includes:

- role-based access logic;
- access approval;
- periodic review;
- revocation.

Excludes the whole of enterprise identity, cyber, or data-security policy.

### 5.2 Utilization and Value Realization Management

Governs how usage, adoption, user response, business value, and management action are reviewed.

Measurement exists to support decisions, not reporting volume.

### 5.3 Maintenance Management

Governs how the current live-solution baseline is kept stable, supportable, current, and operable.

Includes incidents, service requests, recurring defects, release response, configuration maintenance, and routine coordination. It does not own material enhancement decisions.

### 5.4 Change Request Management

Governs how lightweight enhancements and operating improvements are requested, triaged, prioritized, and approved, and when they should become formal project work.

### 5.5 Product Documentation and Artifact Management

Governs ownership, version discipline, maintenance, and intended use of controlled operating artifacts.

It does not justify unmanaged storage or turn every working note into a controlled artifact.

### 5.6 Triage rubric

| Class | Definition | Primary policy route |
|---|---|---|
| Break-fix | Restores or sustains intended current behavior. | Maintenance Management |
| Lightweight enhancement | Changes intended behavior within one contained solution surface, without material cross-domain or architecture impact. | Change Request Management |
| Project-scale change | Has material scope, risk, cross-domain effect, architecture effect, or governance need beyond routine triage. | Project Management Policy |

When containment, impact, or approval route is uncertain, preserve the uncertainty rather than labeling the item lightweight by convenience.

## 6. Data Asset Management Policy

### 6.1 Data Standard Management

Governs business definitions, naming rules, allowable values, and semantic consistency.

### 6.2 Data Model Management

Governs the conceptual and logical shape of data objects, relationships, and structural rules.

### 6.3 Data Lifecycle Management

Governs creation, change, retention, archival, and disposal.

### 6.4 Metadata Management

Governs the contextual information needed to understand and manage data assets, including ownership, lineage, catalog, and descriptive metadata.

### 6.5 Data Quality Management

Governs quality rules, thresholds, measurement, defect treatment, remediation ownership, and review.

### 6.6 Data Security Management

Governs classification, handling, access protection, and privacy-aligned control of solution data.

### 6.7 Mandatory cross-cutting checks

Always consider:

- data governance and decision rights;
- data integration and interoperability.

These are cross-cutting checks unless an explicit architecture decision establishes a durable sub-policy domain.

## 7. When L3 is justified

Create or retain an L3 domain only when:

- a stable sub-policy domain is required to keep the L2 policy governable;
- governed local variance needs a durable policy layer;
- the parent scope cannot remain MECE without a lower policy layer.

L3 must not represent:

- lifecycle stages;
- workflow phases;
- review forums;
- products or modules;
- vendors;
- team names;
- temporary work buckets.

## 8. Decomposition rules

1. Define the parent control scope first.
2. Use one decomposition axis for one sibling set.
3. Give each sibling one primary control object.
4. Define meaningful inclusion and exclusion.
5. Separate ownership from interfaces.
6. Treat a cross-cutting concern as cross-cutting unless durable ownership demands otherwise.
7. Expand only when clearer boundaries cannot resolve material overlap or gaps.

## 9. Relationship to work architecture

Policy and work architecture are related but distinct:

- Policy governs or constrains Process.
- Value Stream decomposes into Process.
- Process may be supported by SOP or work instruction.
- One Process may be governed by several policy references while retaining one parent Value Stream.

Do not present Policy → Process as a parent-child decomposition chain.

## 10. Discussion check

Before proposing a policy-architecture change, ask:

- What control object is currently homeless?
- Can clearer definitions solve the issue without a new domain?
- Is the proposed domain durable?
- Does it mix lifecycle, ownership, product, or team axes?
- What Processes would it govern or constrain?
- What adjacent policy domains must remain explicitly excluded?
