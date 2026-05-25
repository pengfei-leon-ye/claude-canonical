# [POL] Digital Solution Policy Architecture Map

- **Project**: HR Digital Cockpit
- **Document Type**: Policy Architecture Map
- **Status**: Active canonical
- **Role**: Stable policy architecture source for the Digital Solution team
- **Source Category**: Cat 1
- **Management-System Role**: Policy architecture map; outside L1-L5 hierarchy (this source is a control source above L2-L5 artifacts, not itself an L2, L3, L4, or L5 artifact); governs how L2-L5 artifacts for the Digital Solution team are designed
- **Relationship to [OS]**: Extends [OS] §6 / §6.2 policy-architecture anchors into a reusable Digital Solution policy map.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies [PRIN] HR Digital Decision Design Principles §1 (business-first, architecture-enabled), §3 (global core with governed local variance), §6 (operation management and value realization by design), §10 (apply MECE to important decomposition structures) to policy architecture decisions
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [POL] Digital Solution Policy Architecture Map` header fields per [OS] §8.5.1a)

## How to use this source

Use this source when:
- placing a Digital Solution topic at L2, L3, L4, or L5
- deciding whether a topic belongs in policy, process map, SOP / SWI, or specification
- checking whether a proposed L3 structure is necessary and MECE
- designing downstream detailed policy sources, process maps, governance mechanisms, or specifications

Do not use this source as:
- a detailed policy manual
- a process repository
- an SOP library
- a vendor administration guide
- a build or configuration specification

# 1. Purpose and scope

This source defines the stable minimum policy architecture for the Digital Solution team within the HR functional domain.

It is intended to:
- position the current major L2 policy domains
- clarify when L3 is required and when it is not
- define the minimum stable L3 architecture under Operation Management and Data Asset Management
- set decomposition and boundary rules before detailed policy drafting begins
- connect policy architecture to lifecycle management, governance, and execution

L1 is intentionally not expanded in this source because the functional domain is already fixed as HR by the governing operating model.

# 2. Digital Solution interpretation of the management-system lens

The L1-L5 management-system lens is defined by `[OS] Project Operating Model` §4.2, including each level's role, definition, core purpose, core question, required contents, and exclusion boundaries. This section does not redefine the lens; it maps each level to its Digital Solution team interpretation only.

| Level / status | Digital Solution interpretation |
|---|---|
| L2 | the landing level for the three major Digital Solution policy anchors defined in §3 |
| L3 | used as a default architecture layer for Operation Management and Data Asset Management; not used as a default layer for Project Management Policy in this source (§4.1 is the authority) |
| L4 | the normal landing for project lifecycle flows, live-solution operating flows, and data-management workflows |
| L5 | work instructions for recurring operational steps, reviews, approvals, migrations, release handling, or data tasks |
| Outside L2-L5 | specification outputs should state governing linkage when materially relevant, but should not be force-fit into L2-L5 |

For detailed level definitions, see [OS] §4.2.

# 3. Digital Solution L2 policy architecture

The current stable minimum L2 policy architecture for the Digital Solution team is:

| L2 policy domain | Definition | Intended role | Normal downstream landing |
|---|---|---|---|
| Project Management Policy | The policy domain that governs formal delivery governance for time-bounded Digital Solution work | connect strategic intent to project or program execution pathways and control formal delivery from entry to closure | L2 directly to L4 (no default L3 — see §4.1) |
| Operation Management Policy | The policy domain that governs how a live or post-implementation solution is controlled after or beyond implementation | govern steady-state access, usage, maintenance, lightweight change, and controlled operating artifacts | L2 to minimum stable L3, then to L4 |
| Data Asset Management Policy | The policy domain that governs how solution data is managed as an asset across the lifecycle | govern definition, structure, lifecycle, metadata, quality, and security of data assets | L2 to minimum stable L3, then to L4 |

This is a controlled minimum architecture. It does not claim that every enterprise policy domain belongs inside this map.

# 4. Policy domain logic and decomposition

The decomposition rules that govern when and how L3 architecture is created — including the authoritative L3-creation gate — are consolidated in §5. This chapter applies those rules to each L2 policy domain.

## 4.1 Project Management Policy

**Definition**

Project Management Policy governs the formal management of time-bounded Digital Solution delivery work.

**Landing logic**

In this source, Project Management Policy lands at **L2 only**.  
No default L3 decomposition is used.

**Why no default L3 is used**

The primary decomposition logic needed here is lifecycle flow, not sub-policy segmentation.  
Therefore the next landing is L4, not L3.

External project-management frameworks may be used as coverage references, but they do not define the internal policy architecture by default.

**Default L4 process structure**

| L4 process family | Role | Notes |
|---|---|---|
| Initiation | qualify demand, confirm entry, authorize the work, and establish the delivery baseline entry point | includes initiation standards, entry conditions, and formal start logic |
| Planning | define scope, approach, governance setup, plan components, dependencies, and delivery control basis | includes planning needed to run and control the project |
| Execution and Control | deliver the work while managing scope, schedule, quality, risk, issues, dependencies, and change against the approved baseline | control is explicit here and should not be hidden |
| Deployment and Transition | move from solution-ready to business live use through launch readiness, cutover, data migration, communication readiness, training readiness, and operational handover | may begin during late execution and may overlap with it |
| Closure | formally complete the project, confirm handover and closure criteria, close decisions and records, and capture lessons | steady-state operation after handover belongs outside this process family |

**Boundary rules**

- Project Management Policy ends when formal delivery governance ends.
- Post-handover live-solution operation belongs primarily to Operation Management Policy.
- Program is a delivery pathway choice with shared governance where justified, not a default L3 domain in this source.

## 4.2 Operation Management Policy

**Definition**

Operation Management Policy governs how a live or post-implementation solution is controlled, reviewed, maintained, improved, and value-reviewed over time.

**Landing logic**

Operation Management Policy uses **minimum stable L3 domains** before detailed L4 process design.

**Minimum stable L3 domains**

| L3 domain | Definition | Includes | Explicitly excludes |
|---|---|---|---|
| Permission Management | governs who should have what access and how live-solution access is granted, changed, reviewed, and removed | role-based access logic, access approval, periodic access review, access revocation | broader enterprise identity policy or data-security policy as a whole |
| Utilization and Value Realization Management | governs how usage, adoption, user response, and realized business value are reviewed and acted on | utilization signals, adoption review, feedback review, value realization review, management action based on evidence | technical maintenance activity or reporting for its own sake |
| Maintenance Management | governs how the current live-solution baseline is kept stable, supportable, current, and operable | incident management, service request management, recurring defect handling, release response, configuration management for configured products, run engineering / DevOps for self-developed solutions, routine operational coordination of vendor run teams where relevant | project-scale enhancement work, lightweight enhancement prioritization as a separate control path, or commercial vendor performance management |
| Change Request Management | governs how lightweight enhancements and operating improvements are requested, triaged, prioritized, approved, and either executed in BAU or escalated into formal project delivery | request intake, triage, approval, prioritization, explicit project-boundary escalation | break-fix maintenance or recurring run support |
| Product Documentation and Artifact Management | governs how controlled operating artifacts are owned, maintained, versioned, and used | controlled operating documents, decision records, product and operating artifacts, version discipline | unmanaged file storage or policy / process drafting by accident |

**MECE boundary note**

No additional default L3 sibling is required in this source.

**Boundary rules**

- Operation Management is not the same as technical maintenance.
- Maintenance Management is one L3 domain under Operation Management, not the whole policy.
- Maintenance Management owns break-fix sustainment of the current baseline, including incident, service request, release response, configuration maintenance for configured products, and run engineering / DevOps for self-developed solutions where relevant.
- Change Request Management owns the lightweight enhancement and operating-improvement path. Approved implementation of a lightweight change may still be executed through maintenance mechanisms after the change decision is made.
- Vendor team day-to-day run coordination can sit inside normal operating domains.
- Commercial vendor performance management and renewal judgment remain interfaces to broader procurement or vendor-management policy, not separate L3 domains in this map.
- Every material item must be triaged either to Maintenance Management, Change Request Management, or formal Project Management.

**Triage rubric — break-fix vs lightweight enhancement vs project-scale**

The boundary between Maintenance Management and Change Request Management turns on whether an item is break-fix or a lightweight enhancement; the boundary between Change Request Management and formal Project Management turns on whether an item is lightweight or project-scale. Triage each material item against these three categories:

- **Break-fix** — work that restores or sustains the *current* baseline without changing intended behavior: incident resolution, service requests, recurring defect handling, configuration maintenance, release response. Routes to Maintenance Management.
- **Lightweight enhancement** — a *change to intended behavior* that is small in scope, does not require formal project governance, and can be decided and prioritized through BAU triage rather than a project: a contained capability tweak, a configuration-level improvement, a minor workflow adjustment. Routes to Change Request Management.
- **Project-scale** — a change whose scope, risk, cross-domain impact, or governance need exceeds BAU triage and requires formal delivery governance (entry, planning, controlled execution, closure). Escalates from Change Request Management to formal Project Management.

The decisive test for lightweight vs project-scale: an item is lightweight only when its scope is contained to one solution's operating surface, carries no material cross-domain or architectural impact, and can be approved and prioritized without a project governance entry; if any of those fail, it is project-scale.

*Example pair*:
- *Lightweight enhancement (Change Request Management)*: adding an optional filter to an existing report view in a live solution — contained scope, no architectural change, BAU-triageable.
- *Not lightweight — project-scale (escalates to Project Management)*: replacing the live solution's authentication model — cross-cutting impact, architectural change, requires formal delivery governance; it is not a Change Request Management item even though it begins as a request.

## 4.3 Data Asset Management Policy

**Definition**

Data Asset Management Policy governs how solution data is treated as a managed asset across the solution lifecycle.

**Landing logic**

Data Asset Management Policy uses **minimum stable L3 domains** before detailed L4 process design.

**Minimum stable L3 domains**

| L3 domain | Definition | Includes | Explicitly excludes |
|---|---|---|---|
| Data Standard Management | governs business definitions, naming rules, and allowable-value logic for data assets | definitions, naming, code rules, semantic consistency | one-off local naming habits without governance |
| Data Model Management | governs the structural shape of data and the relationships between data objects | conceptual and logical structures, object relationships, structural rules | ad hoc report layout or extract design |
| Data Lifecycle Management | governs how data is created, changed, retained, archived, and disposed | create, update, retain, archive, delete control logic | isolated clean-up work with no durable control logic |
| Metadata Management | governs the contextual information needed to understand and manage data assets | catalog logic, lineage references, ownership metadata, descriptive metadata | generic document tagging with no data-management role |
| Data Quality Management | governs how data quality is defined, measured, controlled, and improved | rules, thresholds, defect handling, remediation governance, quality review | isolated corrections without control ownership |
| Data Security Management | governs how data assets are protected and handled in a security- and privacy-aligned manner | classification, handling rules, access-protection expectations, data-security controls | the whole of enterprise cyber policy |

**Mandatory cross-cutting control checks**

The following checks apply across the full Data Asset Management architecture:
- data governance and decision rights
- data integration and interoperability

In this source, they are treated as mandatory cross-cutting checks, not default sibling L3 domains.

# 5. Decomposition and boundary rules

The decomposition logic below applies `[PRIN] HR Digital Decision Design Principles` §10 (Apply MECE to important decomposition structures) to policy architecture specifically. The upstream principle is the authoritative source for MECE judgment; the rules below translate it into policy-architecture-specific working rules. This chapter is the single decomposition-rules chapter for this source.

**L3-creation gate (authoritative)**

This is the authoritative L3-creation gate for this source. Use L3 only when one of the following is true:
- a stable sub-policy domain is required to keep the parent policy governable
- governed local variance needs a durable policy layer
- the parent scope cannot remain MECE without a lower policy layer

Anchor for "stable" and "durable": a sub-policy domain is *stable* when its control scope is not expected to be reorganized by the next foreseeable change cycle, and *durable* when it must persist as a standing policy layer rather than being absorbed once a one-off need passes. A layer that would exist only to handle a transient or single-instance need does not clear this gate.

L3 (and any policy-architecture decomposition) must not represent lifecycle stages, workflow phases, project gates, review forums, tools, modules, or vendors — see rule 5 (lifecycle stages) and rule 6 (tool/vendor/module/team labels) below.

**Decomposition and boundary rules**

Use the following rules before creating or changing L3 architecture:

1. Define the parent scope first.
2. Use one decomposition axis per sibling set.
3. Separate ownership from interface.
4. Define inclusion and exclusion before optimizing labels.
5. Do not use lifecycle stages as policy siblings.
6. Do not use tool, vendor, module, or team labels as the primary policy taxonomy.
7. Treat cross-cutting checks as cross-cutting unless a later architecture decision explicitly elevates them.
8. Expand the structure only when coverage gaps or material overlap cannot be solved by clearer boundary definitions — this expansion check is subject to the authoritative L3-creation gate above.

**Fast MECE test**
- Does each sibling own one primary control object?
- Does each sibling exclude something meaningful?
- Is any part of the parent scope still homeless?
- Is a proposed new sibling actually a cross-cutting interface rather than a new domain?

# 6. Policy architecture linkage to lifecycle, governance, and execution

## 6.1 Lifecycle linkage

Lifecycle is an operating lens, not an additional management-system level.

- During introduction and major change, Project Management Policy is usually dominant.
- During steady-state run, Operation Management Policy is usually dominant.
- Across all stages, Data Asset Management Policy remains a continuous control layer.

## 6.2 Governance linkage

Policy architecture must link to governance mechanisms. These mechanisms may be expressed in linked governance sources rather than inside the policy architecture map itself.

## 6.3 Execution linkage

Policy architecture becomes executable through the following chain:

1. L2 or L3 policy defines control intent.
2. Governance mechanisms define how oversight runs.
3. L4 process maps define repeatable workflow.
4. L5 SOP / SWI define how individual steps are executed.
5. Specification outputs define implementation, configuration, change, reporting, or handoff detail where needed.

# 7. Management-system outputs and specification outputs

This section applies the output family classification defined in [OS] §5.1 and §5.2 to the Digital Solution domain. It does **not** redefine the families themselves; for the generic definitions and examples, see [OS] §5.

## 7.1 Digital Solution domain-specific instances

The following are the **domain-specific instances** of each output family in Digital Solution work. The generic output family definitions live in [OS] §5 and are not restated here.

**Management-system outputs specific to this domain** (per [OS] §5.1):
- this policy architecture map itself
- detailed L2 policy sources for Project Management, Operation Management, or Data Asset Management
- L3 sub-policy sources under Operation Management and Data Asset Management (where §4.2 and §4.3 justify them)
- L4 process maps implementing each L2 or L3 policy domain
- L5 SOP / SWI for recurring operational, review, approval, migration, release, or data tasks
- governance mechanisms that run oversight over the above (see §6.2)

**Specification outputs specific to this domain** (per [OS] §5.2):
- PRDs and requirement sets scoped to Digital Solution initiatives
- workflow specifications implementing L4 process maps
- handoff specifications for vendor or implementation team execution
- data specifications applying Data Asset Management L3 logic (standard, model, lifecycle, metadata, quality, security)
- integration specifications crossing solution boundaries
- release briefs and implementation decision logs

## 7.2 Boundary rule (domain application)

Specification outputs in this domain should state governing linkage to the relevant L2 or L3 policy when materially relevant, but should not be forced into the L2-L5 hierarchy by default. For the underlying boundary rule, see [OS] §5.3.

# 8. Change rules for this source

Use the following rules before changing this architecture:

- Do not rename the minimum stable L3 domains without first revisiting their definitions and boundaries.
- Adding a new L2 policy domain is governed by the controlled-minimum L2 architecture rule — see §3.
- Adding a new L3 domain is governed by the authoritative L3-creation gate — see §5.
- The prohibition on a separate L3 domain for vendor commercial performance management is owned by §4.2.
- Update this source before detailed downstream policy drafting begins, per the §1 scope intent.
