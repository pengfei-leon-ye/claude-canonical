# Chat Project Replication Mapping

> **Status:** active collection-control map; not chat-project knowledge-base content.
> **Direction:** active workspace source -> conversation-only replica -> chat-project surface.
> **Source boundary:** only active files inside `ai-workspace` are mapped.
> **Reverse sync:** forbidden.

## Use

This file records only current source-to-target edges. It does not preserve migration history, superseded
sources, rejected content, or transformation receipts.

Refresh is on demand:

1. Re-read every active source file in the applicable row.
2. Compare its current semantics with the replica target.
3. Retain only content useful for conversation.
4. Remove provider, model, product-surface, tool, repository, agent, workflow, execution, mutation,
   notification, formal-template, and destination-format mechanics that do not belong in chat.
5. Preserve the collection-level conversation-delivery default from `readme.md`.
6. Review cross-file terminology and references, then independently verify the affected bundle.

Current project-specific sources override generic topic guidance only within their declared project scope.
If active sources conflict materially or no longer support a target, stop that row's refresh and request an
operator decision. Do not infer authority from an older replica.

## HDC

| Replica target | Active source file(s) | Projection scope |
|---|---|---|
| `hdc/project-instructions.md` | `3_projects/chat-canonical/readme.md`<br>`2_topics/hr-digital/principles.md`<br>`2_topics/hr-digital/people-experience-principles.md`<br>`2_topics/hr-digital/journey-and-moments.md`<br>`2_topics/hr-digital/management-system-lens.md`<br>`2_topics/hr-digital/policy-architecture.md`<br>`3_projects/hdc/canonical/wuxi-biologics-crdmo-workforce-and-hr-digital-context.md` | Conversational role, source routing, reasoning posture, and delivery boundary. |
| `hdc/canonical/hdc_os_conversation-operating-model.md` | `2_topics/hr-digital/readme.md`<br>`2_topics/hr-digital/conventions/glossary.md`<br>`2_topics/hr-digital/principles.md`<br>`2_topics/hr-digital/people-experience-principles.md`<br>`2_topics/hr-digital/management-system-lens.md` | Conversation flow, object classification, evidence discipline, and cross-domain lenses. |
| `hdc/canonical/hdc_os_conversation-output-model.md` | `3_projects/chat-canonical/readme.md`<br>`1_team/charter.md` | Content-first, proportional, inline response shaping and explicit file-request boundary. |
| `hdc/canonical/hdc_prin_hr-digital-design-principles.md` | `2_topics/hr-digital/principles.md` | HR Digital judgment projected without execution or mandatory-artifact mechanics. |
| `hdc/canonical/hdc_prin_people-experience-design-principles.md` | `2_topics/hr-digital/people-experience-principles.md` | People Experience judgment projected without mandatory-artifact mechanics. |
| `hdc/canonical/hdc_ref_people-journey-and-moments-catalog.md` | `2_topics/hr-digital/journey-and-moments.md` | Stable lifecycle-stage and moment reference. |
| `hdc/canonical/hdc_ref_wuxi-biologics-crdmo-workforce-context.md` | `3_projects/hdc/canonical/wuxi-biologics-crdmo-workforce-and-hr-digital-context.md` | Evidence-backed CRDMO operating constraints projected into material workforce, HR-decision, and HR Digital implications. |
| `hdc/canonical/hdc_ref_management-system-lens.md` | `2_topics/hr-digital/management-system-lens.md` | L1–L5 governance and Value Stream work-architecture classification for discussion. |
| `hdc/canonical/hdc_pol_digital-solution-policy-architecture.md` | `2_topics/hr-digital/policy-architecture.md` | Digital Solution policy-domain architecture for discussion. |

## Investment Advisor

| Replica target | Active source file(s) | Projection scope |
|---|---|---|
| `investment-advisor/project-instructions.md` | `3_projects/chat-canonical/readme.md`<br>`3_projects/investment-advisor/canonical/advisor-role.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md`<br>`2_topics/investment-advising/methodology.md` | Conversational advisory role, investor commitments, reasoning posture, and delivery boundary. |
| `investment-advisor/canonical/ia_investor-strategy.md` | `3_projects/investment-advisor/canonical/investor-strategy.md`<br>`2_topics/investment-advising/methodology.md` | Investor-specific doctrine and constraints. |
| `investment-advisor/canonical/ia_advising-methodology.md` | `2_topics/investment-advising/methodology.md`<br>`2_topics/investment-advising/conventions/glossary.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | Selection, recommendation, rebalance, review, and state-separation method. |
| `investment-advisor/canonical/ia_market-monitoring.md` | `2_topics/investment-advising/market-monitoring.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | On-demand gray-rhino evidence review. |
| `investment-advisor/canonical/ia_technical-analysis.md` | `2_topics/investment-advising/technical-analysis.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | Secondary-scale target-zone reasoning after thesis and valuation. |
| `investment-advisor/canonical/ia_portfolio-context.md` | `3_projects/investment-advisor/canonical/templates/portfolio-state.md`<br>`3_projects/investment-advisor/canonical/templates/transaction-log.md`<br>`3_projects/investment-advisor/canonical/advisor-role.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | Conversation input and evidence-state contract; no file-filling requirement. |
| `investment-advisor/canonical/ia_selection-analysis.md` | `3_projects/investment-advisor/canonical/templates/satellite-longlist.md`<br>`3_projects/investment-advisor/canonical/templates/satellite-shortlist.md`<br>`2_topics/investment-advising/methodology.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | Candidate search and finalist analysis; semantic sequence rather than document template. |
| `investment-advisor/canonical/ia_recommendation-contract.md` | `3_projects/investment-advisor/canonical/templates/action-plan.md`<br>`2_topics/investment-advising/methodology.md`<br>`2_topics/investment-advising/technical-analysis.md`<br>`3_projects/investment-advisor/canonical/investor-strategy.md` | Recommendation completeness and adaptive inline expression; no order or file semantics. |
