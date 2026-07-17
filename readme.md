# Chat Project Canonical Replication Collection

> **Status:** active operator-declared replication collection.
> **Collection authority:** this file owns the bundle boundary, publication boundary, conversation-delivery
> default, and one-way replication rule. `replication-mapping.md` owns the current source-to-target routes.
> **Replica boundary:** files inside `hdc/` and `investment-advisor/` are transformed replicas for chat-project
> consumption. They are never upstream sources of truth.
> **Audience:** AI runtime consumption in project-specific conversational interfaces.

## Purpose

This collection packages project context for mobile-accessible, project-specific discussion. Each bundle has
the same two-layer shape:

```text
<bundle>/
  project-instructions.md
  canonical/
```

- `project-instructions.md` defines the conversational role, scope, source routing, reasoning posture, and
  response contract.
- `canonical/` contains stable domain principles, methods, doctrine, and reference material needed for the
  project conversation.

The bundles support thinking, analysis, challenge, option comparison, and recommendation. They do not run
work or serve as formal artifact-production systems.

## Publication Boundary

Publish only a bundle's `project-instructions.md` and `canonical/` files to the corresponding chat project.
This root `readme.md` and `replication-mapping.md` are collection-control files and are not chat-project
knowledge-base content.

## Content Boundary

Include only content that remains useful in a conversation:

- project role and discussion scope;
- stable domain principles, methods, doctrine, taxonomies, and reference structures;
- evidence, uncertainty, and reasoning rules needed for sound discussion;
- project-specific facts or commitments that materially change advice.

Exclude:

- model-, provider-, or chat-product-specific behavior;
- CLI, repository, filesystem, connector, tool, skill, agent, subagent, scheduler, hook, or notification
  instructions;
- formal loop, dispatcher, executor, verifier, gate-record, checkpoint, deployment, or transaction mechanics;
- code-production workflows, implementation receipts, and PC execution baselines that do not change the
  conversation itself;
- reusable formal-document templates carried only to make chat produce files;
- destination-specific format rules carried only for export or round-trip handling.

Content about policies, Processes, specifications, or other formal artifacts may remain when those objects
are themselves the subject of discussion. That does not turn the chat response into such an artifact.

## Conversation-Delivery Default

Chat is content-first:

- answer directly in the current conversation;
- use the least structure that makes the reasoning clear;
- treat canonical checklists and response patterns as semantic coverage, not mandatory visible headings;
- do not create or proactively offer a downloadable file, attachment, export, or download link unless the
  user explicitly asks for one;
- do not infer a file request merely because the subject is complex or may later be shared;
- when the user asks for shareable content but not a file, provide polished inline content first;
- do not manufacture owner, reviewer, approval, version, status, RACI, or workflow ceremony unless the topic
  itself requires it;
- never imply that a response changed a system, record, holding, policy, decision, or source of truth.

If the user explicitly asks for a downloadable artifact, first stabilize its purpose, audience, and content.
The resulting file remains a proposed communication artifact unless the user separately assigns it another
status.

## Authority and Refresh

The one-way direction is:

```text
active workspace canonical or project source
  -> conversation-only transformed replica in this collection
  -> chat-project instruction or knowledge-base surface
```

Reverse synchronization is forbidden. A durable improvement discovered in chat must first be accepted into
the appropriate active workspace source; the replica may then be refreshed.

Refresh is on demand. This collection defines no autonomous schedule, freshness SLA, or recurring acceptance
gate. Use `replication-mapping.md` to identify the current active source files, then review semantic changes
against the conversation-only boundary. Do not use hashes as evidence of authority, freshness, or semantic
correctness.

## Bundles

| Bundle | Purpose | Project identity |
|---|---|---|
| `hdc/` | HR Digital, People Experience, policy, management-system, work-architecture, and evidence-backed WuXi Biologics CRDMO workforce and HR Digital context. | Chat-project replica bundle; not a separate immediate-child project identity. |
| `investment-advisor/` | Investor-specific portfolio strategy, selection, monitoring, technical timing, and recommendation discussion. | Chat-project replica bundle; not a separate immediate-child project identity. |
