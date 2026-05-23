# [TPL] UX Design Spec

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable slim content contract declaring (a) what coverage Hub-authored UX Design Spec **instances at two granularities** must provide — a **phase-level instance** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` covering cross-cutting UX content for the phase (platform shell, shared visual vocabulary, cross-feature touchpoints, phase-level design decisions, visual regression naming convention, cross-cutting additive index), and **per-feature instances** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` covering feature-scoped UX content (Affected Tier 1 scope, layout pattern selection, components and interactions, additive plans, a11y, i18n, VR anchors, responsive/motion). Both are Hub-authored at [MECH] Development Track Workflow TK-02 Step 2.3 from the CD-authored phase-level design file — the phase-level instance grounded in the design file's cross-cutting sections plus the union of per-feature labeled slices; each per-feature instance grounded in that feature's labeled slice; and (b) the reviewer checklists applied at TK-02 Step 2.3 for each instance type (design file quality check + authoring quality check). Granularity asymmetry between CD output (one phase-level design file) and Hub output (one phase-level instance + N per-feature instances) is intentional — see [REF] Hub-CD-CC Architecture §3.4.1.
- **Source Category**: Cat 4
- **Management-System Role**: Outside L1-L5 hierarchy; specification-support template; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; admissibility per [OS] §2.3.2 Cat 4 specification templates row (UX Design Spec is one Cat 4 template covering both instance types)
- **Relationship to [PRIN] People Experience Design Principles**: Applies these principles to both phase-level cross-cutting UX content (shell, vocabulary, cross-feature touchpoints) and per-feature UX content scope; CD-authored design files are expected to be principle-aligned and the Hub-authored UX Design Spec instances grounded in those design files preserve principle application at the spec layer; this template's reviewer checklists surface principle-application gaps at both layers
- **Relationship to [REF] Hub-CD-CC Architecture**: Per §3.4.1 revised, CD outputs a **phase-level design file** (CD-native visual artifacts) — hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations, **plus phase-level cross-cutting sections (platform shell, shared visual vocabulary, cross-feature touchpoint maps, phase-level design decisions, visual regression naming convention)** and per-feature internal labeling — at TK-02 Step 2.2 when any feature in the phase has `tier_1_involved=true`. Per §5.2 two-way distribution model + §5.4 self-authoring discipline, the Hub-authored markdown counterparts at TK-02 Step 2.3 are produced at **two granularities**: one **phase-level UX Design Spec instance** synthesizing the design file's cross-cutting sections, and **N per-feature UX Design Spec instances** (one per tier-1-involved feature) each synthesizing that feature's labeled slice. The content categories enumerated in §2A (phase-level) and §2B (per-feature) of this template define what the Hub-authored markdown must cover so downstream consumption (Hub TK-03 + CC TK-04+) is deterministic
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2.1 (Hub → operator → CD) carries Hub PRD/TDD relevant sections as drop files into CD at TK-02 Step 2.2 entry; §2.2 (CD → operator → Hub) carries the CD-authored phase-level design file back to Hub for TK-02 Step 2.3 design file quality checks (both phase-level cross-cutting check + per-feature slice checks) + Hub-authored instance authoring (one phase-level + N per-feature); §3.1 (Hub → operator → CC) carries the completed spec bundle (intent / acceptance / test-plan + **both UX Design Spec instance types** — phase-level + per-feature — + CD design files as visual reference) to CC at TK-04 entry
- **Relationship to [MECH] Development Track Workflow**: TK-02 Step 2.2 produces the CD-authored phase-level design file when any feature in the phase has `tier_1_involved=true`; TK-02 Step 2.3 produces (a) one Hub-authored **phase-level UX Design Spec instance** synthesizing the design file's cross-cutting content, and (b) **per-feature Hub-authored UX Design Spec instances** each grounded in the corresponding feature's labeled slice; TK-03 consumes both as the primary textual UX source for per-slice intent / acceptance / test-plan authoring — the phase-level instance for cross-feature touchpoints / shell / shared vocabulary references, the per-feature instance for feature-scoped UX content; TK-04+ consumes both alongside the spec bundle plus the phase-level design file as visual reference
- **Relationship to [TPL] Technical Design Document Template**: Paired. TDD `§4.{feature-slug}.Header.tier_1_involved` declares whether a feature requires (a) inclusion in the phase-level CD design file as a labeled per-feature slice (Step 2.2) and (b) a Hub-authored per-feature UX Design Spec instance (Step 2.3) for that feature; when any feature in the phase has `tier_1_involved=true`, the phase-level UX Design Spec instance is also produced at Step 2.3. Step 2.2 fires once per phase (covering all tier-1-involved features); Step 2.3 produces one phase-level instance plus iterates per-feature instances. The TDD does not carry UX strategy content itself; it references both UX Design Spec instance paths. TDD §2.2.5 Integration boundaries vs phase-level UX Spec §2A.3 Cross-feature touchpoints: TDD captures interface-level contracts (API / event / data); UX Spec captures interaction-level contracts (CTA / jump / mask / state-propagation visible to users) — they are paired but non-overlapping.
- **Relationship to [TPL] PRD-TDD to Intent and Acceptance Conversion Spec**: Paired. Conversion Spec §3.8 reads both the phase-level and per-feature UX Design Spec instances as the source for intent.md UX brief content when Tier 1 is involved in a slice — per-feature instance for screens / interactions / components / a11y / i18n within the slice; phase-level instance for cross-feature touchpoints the slice participates in plus shared vocabulary references. Flow: CD design files → Hub TK-02 Step 2.3 → two-tier UX Design Spec instances → Hub TK-03 (slice intent UX brief extraction) → spec bundle to CC at TK-04
- **Relationship to [TPL] Intent and Acceptance Interface Writing Standard**: Paired. Writing Standard §2.3 defines what intent.md UX brief must contain; this template defines what the upstream Hub-authored UX Design Spec instances (phase-level + per-feature) must cover so Hub Claude at TK-03 has sufficient material to author the slice-narrow UX brief. The two together close the UX content chain from CD design files (visual) → Hub UX Design Spec instances (phase-level + per-feature textual spec) → slice intent UX brief (slice-narrow textual extract)
- **Relationship to [TPL] Phase Test Plan**: Paired. Phase test plan §2 Cross-feature scenario classes and §3 App-scale NFR scenario classes consume cross-feature touchpoint definitions from the phase-level UX Design Spec instance §2A.3 when scenarios cross UI-layer touchpoints; visual regression naming convention used across per-feature test plans (`test_type: visual_regression` cases) is sourced from phase-level UX Design Spec §2A.5
- **Relationship to [RULE] Design System Governance**: Both Hub-authored UX Design Spec instance types are grounded in the CD-authored design files per DSG §13.3 Hub-side consumption discipline. The per-feature instance's §2B.4 New components or tokens entry, when present, captures the additive change plan that drives the DSG §12 additive update flow; the phase-level instance's §2A.6 is an **index** of cross-cutting additives (additives genuinely shared across multiple features in the phase, with a designated first-owner feature per CD's annotation in the design file) that cross-references the originating feature's §2B.4 plan — CD authors the corresponding DS instance content change at the originating feature's M4 → merge-to-main milestone per DSG §12.5, at which point the CC mirror is re-synced via the reviewed CD-generated DS markdown export
- **Pairings I participate in**: P-28 (with [TPL] Conversion Spec §2 + §3.8 + [TPL] TDD §4.{feature-slug}.Module-Decomposition — UX Design Spec content-category structural changes — across §2A or §2B — trigger Conversion Spec UX brief extraction re-verification), P-29 (with [TPL] Intent-Acceptance §2.3 + §3.9 — UX Design Spec content-category structural organization changes across §2A or §2B trigger Writing Standard consumer-side re-verification)

## How to use this source

Use this template when:
- A phase's TDD declares `tier_1_involved: true` for one or more `§4.{feature-slug}` entries at TK-02 Step 2.1, triggering CD phase-level design file production (Step 2.2, one design file covering all tier-1-involved features in the phase plus phase-level cross-cutting sections) followed by Hub-side UX Design Spec instance authoring (Step 2.3, one phase-level instance + iterated per-feature instances)
- Hub Claude is performing the design file quality check at TK-02 Step 2.3 entry (against CD-authored design files just transferred from CD) — phase-level cross-cutting check against the design file's cross-cutting sections plus per-feature slice check against each tier-1-involved feature's labeled slice
- Hub Claude is authoring the phase-level UX Design Spec instance markdown at TK-02 Step 2.3, grounding cross-cutting content (shell / vocabulary / touchpoints / phase decisions / VR naming) in the CD-authored design file's cross-cutting sections
- Hub Claude is authoring a per-feature UX Design Spec instance markdown at TK-02 Step 2.3, grounding component / token / pattern claims in the relevant feature's labeled slice of the CD-authored design file
- The operator is reviewing the Hub-authored UX Design Spec instances (phase-level and per-feature) before TK-02 sign-off
- Hub Claude at TK-03 is extracting slice-narrow UX brief content — from the per-feature instance for in-slice UX, from the phase-level instance for cross-feature touchpoints the slice participates in plus shared vocabulary references
- CC at TK-04+ needs to consume the UX Design Spec instances alongside the spec bundle for code generation

Do not use this template:
- As a CD-authoring template — CD produces design files in its CD-native format (per [REF] Hub-CD-CC Architecture §3.4.1); both Hub-authored UX Design Spec instance types are the markdown counterparts, not the CD output. CD does not consume this template
- As a substitute for the CD-authored phase-level design file — the design file is the visual source material from which Hub authors both UX Design Spec instance types; it is operator-side reference for CC TK-04+ (visual context for implementation) but is not committed to the monorepo unless the operator explicitly opts to commit exports at `apps/{app-slug}/design-references/phase-{N}/`
- As a substitute for the DS instance — DS instance content lives in CD as SOT, with a CC code-time mirror per [RULE] DSG §1.1 two-way distribution model; this template covers per-phase + per-feature UX scope, not project-wide design system content
- As a CC-authored deliverable — content of this template's instances is Hub-authored at TK-02 Step 2.3, then consumed by CC at TK-04+; CC does not author UX Design Spec instances

## Scope note

This template's scope covers **two distinct UX Design Spec instance types**, distinguished by granularity:

| Instance type | File | Scope | Quantity per phase |
|---|---|---|---|
| **Phase-level UX Design Spec instance** | `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` | Cross-cutting UX content for the phase (shell / vocabulary / touchpoints / phase decisions / VR naming / cross-cutting additive index) | Exactly one (mandatory when Step 2.2 fires; content categories may be marked "not applicable" when minimal) |
| **Per-feature UX Design Spec instance** | `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Feature-scoped UX content (one TDD `§4.{feature-slug}` worth of UX scope — multiple slices may then consume one instance) | One per `tier_1_involved=true` feature in the phase |

Both instance types are Hub-authored at TK-02 Step 2.3. The slice-level downstream artifact is intent.md UX brief (Hub-authored by Hub Claude at TK-03, governed by Writing Standard §2.3), which is narrower than per-feature scope and references back to both UX Design Spec instances.

---

# 0. Boundary and position

## 0.1 What this source owns

- **The synthesis nature of the instances**: each Hub-authored UX Design Spec instance (phase-level or per-feature) is a **synthesis** from CD-authored design files (raw source material) — a structuring of the design files' visual + informal-annotation content into CC-consumable markdown, integrated with adjacent spec artifacts, not a verbatim transcription. Design files alone are not CC-consumable specification; the synthesis at TK-02 Step 2.3 is the substantive authoring step that produces CC-consumable content. See [REF] Hub-CD-CC Architecture §3.4.1 + §9.4 for the architectural framing.
- The coverage contracts: what categories of UX content the **phase-level** instance must provide (§2A) when Step 2.2 fires, and what categories the **per-feature** instance must provide (§2B) when a feature has `tier_1_involved=true`
- The reviewer checklists applied at TK-02 Step 2.3, by instance type:
  - **Phase-level design file quality check + phase-level authoring quality check** — §3A
  - **Per-feature design file quality check + per-feature authoring quality check** — §3B
  - Both check types use the same structural pattern (design file quality check at entry + authoring quality check at exit) but anchor on different content categories
- The downstream flow declaration: how UX Design Spec instance content (phase-level + per-feature) reaches Hub TK-03 (slice intent / acceptance / test-plan) and CC TK-04+ (code generation)
- The cross-reference rules between the two instance types (per-feature instance header references phase-level instance; phase-level instance §2A.3 cross-feature touchpoints reference per-feature instances participating in each touchpoint; phase-level instance §2A.6 cross-cutting additive index references first-owner feature's §2B.4 entry)
- Anti-drift red flags specific to UX Design Spec instance authoring and consumption — covering both granularity scope drift (phase-level content in per-feature instance / per-feature content in phase-level instance) and the existing per-feature drift signals

## 0.2 What this source does not own

- The CD-authored design file format (CD-native; visual artifacts including hi-fi mockups, prototypes, wireframes — owned by CD platform behavior per [REF] Hub-CD-CC Architecture §3.4.1; not file-format-specified here)
- The DS instance content (tokens, component inventory, layout patterns) — owned by DSG; lives in CD as SOT with a CC mirror at `specs/design-system.md` per DSG §1.1 two-way distribution model
- The intent.md UX brief content — owned by Writing Standard §2.3; Hub-authored at TK-03 by extracting slice-narrow subset from this template's instances (both phase-level and per-feature where applicable)
- The accessibility test cases — owned by Test Plan YAML Schema; Hub-authored at TK-03 by deriving from this template's per-feature instance §2B.5
- TDD `§4.{feature-slug}.Header.tier_1_involved` declaration logic — owned by TDD template
- TDD §2.2.5 Integration boundaries — owned by TDD template; pairs with this template's phase-level §2A.3 Cross-feature touchpoints but does not overlap (TDD = interface-level contracts; UX Spec = interaction-level contracts)
- TK-02 internal step orchestration (Step 2.1 → Step 2.2 → Step 2.3) — owned by [MECH] Development Track Workflow §4 TK-02
- Cross-tool content transfer mechanics (drop files at Step 2.2 entry; design files transfer back at Step 2.3 entry) — owned by [MECH] Cross-Tool Workflow Handoff §2.1 / §2.2

## 0.3 Boundary with downstream consumers

| Downstream consumer | What it consumes from a UX Design Spec instance |
|---|---|
| **Hub Claude (TK-03 intent.md authoring)** | Per-feature §2B.1 screens, §2B.3 components and patterns, §2B.5 a11y, §2B.6 i18n — extract slice-relevant subset; **plus phase-level §2A.3 cross-feature touchpoints when the slice participates in a touchpoint, §2A.2 shared vocabulary when the slice consumes a shared visual contract** — into intent.md UX brief per Writing Standard §2.3 |
| **Hub Claude (TK-03 acceptance.yaml authoring)** | Per-feature §2B.7 visual regression anchors, §2B.8 motion expectations — extract slice-relevant scenarios for acceptance scenarios per Writing Standard §3.9 |
| **Hub Claude (TK-03 test-plan.yaml authoring)** | Per-feature §2B.5 a11y, §2B.7 visual regression anchors — produce `test_type: accessibility` and `test_type: visual_regression` cases per Test Plan YAML Schema; **plus phase-level §2A.5 visual regression naming convention** for case-naming consistency across features |
| **Hub Claude (TK-02 Step 2.1 phase test plan authoring)** | Phase-level §2A.3 cross-feature touchpoints feed phase test plan §2 cross-feature scenario classes; phase-level §2A.5 VR naming convention is referenced by phase test plan §2.2.7 testing strategy |
| **CC main loop (TK-04+ code generation)** | Full UX Design Spec instances (phase-level + the relevant per-feature) via the spec bundle at TK-04 entry; CD-authored phase-level design file accompanies as visual reference (operator-side) for visual context during implementation |
| SK-F (`hdc-arco-enterprise-ui` skill at CC runtime) | Per-feature §2B.3 components referenced, §2B.4 New components or tokens; phase-level §2A.2 shared visual vocabulary, §2A.6 cross-cutting additive index — informs code-generation constraints; SK-F additionally grounds in CC DS mirror at `specs/design-system.md` per DSG §13.1 |

Hub Claude authors intent / acceptance / test-plan at TK-03 (the content pillar per [REF] Hub-CD-CC Architecture §5.1); CC does NOT author these UX-touching fields. CC consumes the completed spec bundle (Hub-authored content) at TK-04 entry.

---

# 1. Instance landing paths and headers

This template governs two instance types with distinct landing paths. Both are Hub-authored at TK-02 Step 2.3 and forwarded to the assigned_node's working directory alongside other TK-02 outputs per [MECH] Cross-Tool Workflow Handoff §3.1. CC reads instances from the monorepo paths at TK-04+.

## 1.1 Phase-level UX Design Spec instance

### 1.1.1 Landing path

```
apps/{app-slug}/specs/ux-design-spec/phase-{N}.md
```

One phase-level instance per phase. The file's `{N}` matches the paired phase TDD's `phase_number`. The instance is mandatory whenever TK-02 Step 2.2 fires (i.e., whenever at least one feature in the phase has `tier_1_involved=true`); content categories that do not apply to the phase are explicitly marked "not applicable to this phase" with one-sentence rationale.

**Source material location**: The CD-authored phase-level design file resides in the CD workspace (CD project / file structure) plus the operator's working materials when transferred to Hub at TK-02 Step 2.3 entry. The design file's **cross-cutting sections** (platform shell artboards, shared visual vocabulary artboards, cross-feature touchpoint maps, phase-level design decision logs, VR naming convention annotations) are the primary source material for the phase-level instance. The design file is operator-side reference at TK-04+ (visual context for CC implementation) and is **not committed to the monorepo by default**. The operator may opt to commit design file exports as auxiliary reference at `apps/{app-slug}/design-references/phase-{N}/` if useful, but the UX Design Spec instance markdowns are the canonical-form artifacts.

### 1.1.2 Instance header (required)

Every phase-level UX Design Spec instance markdown MUST begin with the following header fields:

```markdown
- **app_slug**: <app-slug>
- **phase_number**: <N> (must match paired TDD phase_number)
- **DS instance version**: <semver> (the DS version recorded in the CD-authored phase-level design file at authoring time)
- **Source design file**: <reference to the CD-authored phase-level design file used as source material (informal path or operator-managed location); additionally cite the specific cross-cutting sections / artboards (frame / section / page tags for shell / vocab / touchpoints / decisions / VR naming) so the grounding chain from phase spec → design file cross-cutting sections is auditable>
- **Per-feature instances in this phase**: <list of feature-slugs whose per-feature UX Design Spec instances pair with this phase-level instance; must match the set of features with `tier_1_involved=true` in the paired TDD>
- **Status**: Draft | Active | Superseded
- **Authored at**: <date> (TK-02 Step 2.3)
- **Cross-references**: paired TDD `apps/{app-slug}/specs/tdd/phase-{N}.md`; paired phase test plan `apps/{app-slug}/specs/test-plan/phase-{N}.md`
```

## 1.2 Per-feature UX Design Spec instance

### 1.2.1 Landing path

```
apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md
```

One per-feature instance per `tier_1_involved=true` feature in the phase. Naming convention anchors on `{feature-slug}` matching the TDD `§4.{feature-slug}` entry it pairs with. For walking-skeleton scope (Phase 1 only, rare case where walking-skeleton touches Tier 1), the file is at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md` (treated as a feature-slug-equivalent).

**Source material location**: The same CD-authored phase-level design file referenced by the phase-level instance; the per-feature instance grounds in **the feature's labeled slice** (frame / section / page tag matching this instance's `feature_slug`) per [REF] Hub-CD-CC Architecture §3.4.1 + [RULE] DSG §13.3 Hub-side consumption discipline.

### 1.2.2 Instance header (required)

Every per-feature UX Design Spec instance markdown MUST begin with the following header fields:

```markdown
- **app_slug**: <app-slug>
- **feature_slug**: <feature-slug> (must match TDD §4.{feature-slug}.Header.feature-slug)
- **phase_number**: <N> (must match TDD phase_number)
- **DS instance version**: <semver> (the DS version recorded in the CD-authored phase-level design file at authoring time)
- **Source design file slice**: <reference to the CD-authored phase-level design file used as source material plus the specific per-feature labeled slice within the design file — the frame / section / page tag matching this instance's `feature_slug` — so the grounding chain from feature spec → design file slice is auditable>
- **Phase-level UX Design Spec ref**: `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` (mandatory pair when this instance exists)
- **Status**: Draft | Active | Superseded
- **Authored at**: <date> (TK-02 Step 2.3)
- **Cross-references**: paired TDD §4.{feature-slug}; paired PRD §7.1 feature entry; phase-level UX Design Spec instance (above)
```

---

# 2. Required content categories

This template defines two parallel content category sets, one per instance type. Coverage means "the instance markdown contains material on this category"; Hub Claude grounds each category in the CD-authored design file per DSG §13.3 consumption discipline. The reviewer checklists in §3 verify coverage at TK-02 Step 2.3.

## §2A Phase-level instance — content categories

A Hub-authored phase-level UX Design Spec instance must cover the categories below when Step 2.2 fires. Categories that do not apply to a particular phase are explicitly marked "not applicable to this phase" with one-sentence rationale.

### 2A.1 Platform shell and information architecture

Coverage of the cross-cutting platform shell established or modified in this phase. Sourced from the design file's platform-shell artboards.

- Shell anatomy (header / topbar / sidebar / footer / persona switcher) as depicted in the design file
- Information architecture: top-level navigation taxonomy; entry-point taxonomy per persona
- Persona scope for the phase (Employee / Manager / HRBP / Admin per [PRIN] People Experience Design Principles role taxonomy; or app-specific personas if the design file declares them — e.g., BU / DM / regular user — with one-sentence justification per persona)
- Shell-level interaction patterns affecting all features (search-bar location, notification entry, persona switching, locale switching, etc.)
- Phase delta when applicable (Phase N ≥ 2: deltas from prior-phase shell baseline rather than restating it)

### 2A.2 Shared visual vocabulary

Coverage of cross-feature visual contracts depicted in the design file's shared-vocabulary artboards. Each entry: vocabulary name + one-sentence semantic contract + where the design file depicts it.

Typical vocabulary categories (instances vary):
- Badge families (status / type / role / category badges shared across features)
- Status visual language (empty / loading / error / no-permission states with shared visual treatment)
- Permission-masking visual language (when the app has data-permission UX)
- Multi-language readout patterns (when i18n surfaces multi-locale content visibly)
- Any other visual contract the design file calls out as shared across features

Vocabulary items that exist in the current DS instance reference the DS by component / token name; vocabulary items that are additive proposals reference the originating feature's §2B.4 entry per §2A.6 cross-cutting additive index.

### 2A.3 Cross-feature touchpoints

Coverage of UI-layer interaction contracts between features depicted in the design file's touchpoint maps. Each touchpoint:

- Touchpoint id (e.g., `C-01`)
- Origin feature (feature-slug) + destination feature (feature-slug)
- One-sentence contract (e.g., "DRAFT status badge click in metadata-explorer / search → review-approval detail")
- Trigger condition (which user action or state transition fires the touchpoint)
- Components involved (Tier A or Tier B; reference §2A.2 shared vocabulary or per-feature §2B.3 components)
- TDD reference when applicable (cross-link to TDD §2.2.5 Integration boundaries entries when the touchpoint also carries interface-level contracts; the two are paired but the UX touchpoint captures the user-visible interaction, the TDD entry captures the API/event/data contract)

**Boundary with TDD §2.2.5**: TDD captures interface-level contracts (API endpoints, event names, data flow, idempotency). This category captures interaction-level contracts (which CTA jumps where, what visual state propagates, what mask the user sees). When a single feature pair has both an interface contract and an interaction contract, both entries exist — paired but distinct.

### 2A.4 Phase-level horizontal design decisions

Coverage of design decisions affecting multiple features in the phase that warrant traceability. Each decision:

- Decision id (e.g., `DD-01`)
- Decision statement (one sentence)
- Anchor (which design file artboard(s) demonstrate the decision)
- Rationale (when the decision is not obvious)

Examples of phase-level horizontal decisions (instances vary):
- "BU persona is excluded from feature X via shell IA, not via in-feature blocking"
- "Component family Y uses dual-view (matrix + graph); other component families use single-view"
- "Reduced-motion alternative for large-scale visualizations: text fallback instead of animated graph"

This category is lightweight ADR-adjacent — it captures decisions that are too design-scoped for [TPL] ADR Spec but too horizontal for any one per-feature instance. If a decision is large enough to warrant a full ADR, it is recorded as an ADR per [TPL] ADR Spec and referenced here as an index entry rather than restated.

### 2A.5 Visual regression naming convention

Coverage of the cross-feature naming rules for visual regression test cases. Sourced from the design file's VR-naming annotations (when present) or inferred from the design file's per-feature labeling. Provides:

- Per-feature prefix table (one prefix per `tier_1_involved=true` feature, e.g., `exp-` for metadata-explorer, `glo-` for business-data-glossary)
- State vocabulary (standardized state suffixes: `empty` / `loading` / `error` / `partial-mask` / `full-mask` / `default` / `dialog` / `403` / `unauthorized` / etc.)
- Naming format (typically `{prefix}-{view}-{state}.png`)

This category provides the convention; concrete per-feature VR anchors live in each per-feature instance §2B.7.

### 2A.6 Cross-cutting new components or tokens (additive index)

Coverage of additive Tier B components, tokens, icons, or locales that are **shared across multiple features in the phase** (not single-feature additives). Each entry:

- Asset name and type (component / token / icon / locale)
- Cross-cutting nature (one sentence on why this additive is genuinely shared, not feature-specific)
- **Originating feature** (the first-owner feature-slug as designated in the CD-authored design file; this is the feature whose `tier_1_involved=true` slice depicts the additive's first use, and whose M4 → merge-to-main milestone will carry the DS instance update per DSG §12.5)
- **Source of additive update plan**: cross-reference to the originating feature's per-feature instance §2B.4 entry where the full additive plan content is authored (per DSG §12.4 minimum change content structure)

This category is an **index**, not a duplicate plan. The DSG §12 additive flow's authoritative artifact remains the originating feature's §2B.4 entry; this index ensures cross-cutting additives are discoverable from the phase-level instance and that downstream consumers (CC TK-04+) can locate them efficiently.

Single-feature additives (introduced and used only by one feature) stay in that feature's §2B.4 entry and do NOT appear in this index.

If a phase has no cross-cutting additives, this category is marked "not applicable to this phase; no cross-cutting additive components / tokens introduced."

## §2B Per-feature instance — content categories

A Hub-authored per-feature UX Design Spec instance for a feature must cover the categories below when that feature has `tier_1_involved=true`.

### 2B.1 Affected Tier 1 scope

- Screens or UI flows this feature introduces or modifies in this phase (extracted from this feature's labeled slice of the CD design file)
- Roles affected (cross-reference phase-level §2A.1 persona scope; restate only the personas active in this feature)
- Responsive target per screen (desktop primary / tablet primary / mobile primary / cross-device per DSG §11.2 platform tier classification)

### 2B.2 HDC layout pattern selection

For each screen in §2B.1, the HDC layout pattern from the DS instance pattern catalog (as called out in the CD-authored design file). Rationale required only when the pattern choice is non-obvious or deviates from the standard screen-type-to-pattern mapping in the DS instance pattern catalog.

### 2B.3 Components and interaction patterns

- **Tier A (Arco components used)** — components from the DS instance Tier A inventory consumed by this feature (as called out in the CD-authored design file)
- **Tier B (HDC custom components used)** — components from the DS instance Tier B inventory consumed by this feature (as called out in the CD-authored design file); when a Tier B is sourced from phase-level §2A.2 shared visual vocabulary, reference the phase-level instance rather than duplicate
- **Key interactions per screen** — one-sentence descriptions of the load-bearing interactions extracted from the CD design file; components implementing each interaction; entry / exit / branching conditions when non-obvious. If an interaction participates in a phase-level §2A.3 cross-feature touchpoint, cross-reference the touchpoint id

### 2B.4 New components or tokens (additive update plan, conditional)

Required only when this feature's slice introduces components, tokens, icons, or locale strings not yet in the current DS instance.

For each new asset:
- Asset name and type (component / token / icon / locale)
- **Scope**: declare whether this additive is **feature-specific** (used only by this feature) or **cross-cutting** (shared with other features in the phase; if cross-cutting, this feature is the designated first-owner and the asset is also indexed in phase-level §2A.6)
- Rationale (why existing DS items are insufficient, traceable to specific design file content)
- Proposed specification — for components, composition from Arco primitives or new-built structure as observed in design files; for tokens, value and semantic role
- DS instance update plan — pointer to the DSG additive update process per [RULE] DSG §12.3 + §12.4 minimum change content structure; the change merges into CD SOT at this feature's M4 → merge-to-main milestone per DSG §12.5, with the CC mirror re-synced via the reviewed CD-generated DS markdown export

If the change is breaking rather than additive, do not capture in §2B.4; instead surface as a standalone change file routed through DSG §12.2 breaking-update path before UX Design Spec authoring continues. Hub Claude flags the breaking nature to the operator during TK-02 Step 2.3 authoring.

### 2B.5 Accessibility call-outs (feature-specific only)

Coverage required only when the design file reveals specific accessibility concerns beyond Arco component defaults plus DS instance baseline:

- Feature-specific a11y risks (custom Tier B with non-standard interactions, complex flows needing keyboard-only verification — extracted from interaction flows in the design file's slice)
- Optional manual validation items for the operator's M4 smoke test
- Any concerns that warrant an on-demand SK-W audit before release (the SK-W skill name is diagnostic and does not imply a formal WCAG conformance target — see DSG §6)

Per [RULE] DSG §6, HDC has no formal WCAG conformance target. Routine a11y recommendations apply uniformly to all slices and need not be restated in the instance; this section captures feature-specific concerns only.

### 2B.6 Internationalization and RTL call-outs

- New locale coverage required (if any) — list of new locale codes per DS instance i18n scope declaration; if the feature introduces a locale not already in DS instance §7, an additive update via DSG §12 is needed and captured in §2B.4 (or in §2A.6 + first-owner feature's §2B.4 if cross-cutting)
- RTL-specific layout considerations (if any, observed from this feature's slice) — text direction, mirrored components, asymmetric spacing
- Text expansion risk areas (dense labels, table columns, status badges) — call-outs where translated text may overflow visual containers, as identified during design file review

### 2B.7 Visual regression anchors

- Screens requiring visual regression baselines (downstream routing per §0.3)
- Approved baseline screenshots reference (when baselines exist from prior features or phases in the same app; informal reference to design files or to monorepo screenshots if committed)
- Key visual states to anchor (loading, empty, error, success, edge data — as depicted in the design file's slice)
- Anchor naming follows phase-level §2A.5 visual regression naming convention; list this feature's specific anchor names

### 2B.8 Responsive and motion expectations

- Breakpoint-specific layout differences per screen (when non-default; observed in the design file's slice)
- Cross-device behavioral expectations (when non-trivial)
- Non-default motion decisions — defaults are Arco component built-in transitions; this section captures only deviations from DSG §8 motion hygiene
- `prefers-reduced-motion` handling beyond DS instance default (per DSG §8.2)

---

# 3. Reviewer checklists (applied at TK-02 Step 2.3)

TK-02 Step 2.3 applies two parallel checklist sets, one per instance type. Each set follows the same structural pattern: a **design file quality check** at entry (verifying the design file is sufficient grounding material for the instance) and an **authoring quality check** at exit (verifying the Hub-authored markdown covers all required content categories grounded in the design file).

Both checklist sets are operator-side; Hub Claude assists in walking each but does not declare items pass / fail unilaterally — operator decides each disposition.

The Step 2.3 sequencing is: phase-level design file quality check (§3A.1) → if pass, phase-level instance authoring (§3A.2) **and** per-feature design file quality checks iterated (§3B.1). Per-feature authoring (§3B.2) iterates over the features whose slice checks passed. Phase-level and per-feature work may interleave in practice (the phase-level instance can be drafted in parallel with per-feature drafts), but TK-02 sign-off requires all checklists pass.

## §3A Phase-level instance checklists

### 3A.1 Phase-level design file quality check (Step 2.3 entry)

#### 3A.1.1 Coverage check

For each §2A.x category: the design file's cross-cutting sections (shell artboards, vocabulary artboards, touchpoint maps, phase-level decision logs, VR naming annotations) contain visual / annotation material sufficient to ground the corresponding markdown category, OR the category is explicitly marked "not applicable to this phase" by the operator with one-sentence rationale.

#### 3A.1.2 Alignment check

- Platform shell content matches the phase's actual scope (no shell elements outside this phase's TDD; no missing shell content TDD declared)
- Shared visual vocabulary items are clearly named and CD-attributed to the DS — items CD flags as new (not yet in the DS) are captured as §2A.6 cross-cutting additive index entries with originating-feature designation
- Cross-feature touchpoints depicted in the design file align with TDD §2.2.5 Integration boundaries (paired but non-overlapping — every touchpoint with an interface contract has a matching TDD entry)
- Phase-level horizontal decisions are concretely depicted (an artboard or annotation visibly demonstrates each decision; decisions floating without anchors are flagged)
- VR naming convention is depicted or stated (feature prefix table + state vocabulary present in the design file's annotations, OR derivable from the design file's per-feature labeling)

#### 3A.1.3 Grounding sufficiency check

- Shell IA is concrete enough to author §2A.1 without inventing navigation taxonomy
- Vocabulary items are visually distinct and semantically annotated — Hub Claude can transcribe each into §2A.2 with confidence
- Touchpoint maps include both endpoints (origin + destination features) and the trigger condition for each touchpoint
- Phase-level decisions carry rationale annotations or are obvious from the artboard context

#### 3A.1.4 Disposition

Three outcomes:

- **Pass** — design file's cross-cutting sections are sufficient; Hub Claude proceeds to phase-level instance authoring (§3A.2)
- **Pass with annotation** — minor gaps the operator annotates; Hub Claude proceeds to authoring and notes the annotation context in the phase-level instance where applicable
- **Reject — return to CD for revision** — material gaps in the phase-level cross-cutting sections (or VR naming convention or touchpoint maps); operator routes back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback; Step 2.2 redo scope is the phase-level cross-cutting sections (per-feature slices may still proceed via §3B if their slices passed)

### 3A.2 Phase-level instance authoring quality check (Step 2.3 exit, before TK-02 sign-off)

#### 3A.2.1 Coverage check

For each §2A.x category: the Hub-authored phase-level instance markdown contains material on this category, or the category is explicitly marked "not applicable to this phase" with one-sentence rationale (consistent with the §3A.1.1 design file disposition).

#### 3A.2.2 Alignment check

- Every shell / vocabulary / touchpoint reference traces to a design file callout in the cross-cutting sections
- §2A.3 cross-feature touchpoints reference both endpoints by feature-slug; both feature-slugs appear in the phase-level header's `Per-feature instances in this phase` list
- §2A.6 cross-cutting additive index entries cross-reference the originating feature's per-feature §2B.4 entry by feature-slug + asset name; the originating feature's per-feature instance is authored (or planned to be authored) within the same TK-02 sign-off
- §2A.5 VR naming convention is internally consistent (prefix table covers every `tier_1_involved=true` feature in the phase)

#### 3A.2.3 Downstream sufficiency check

- Each §2A.x category's content is concrete enough that its downstream consumer — per the §0.3 category→consumer map — can author its artifact without inventing detail (e.g. Hub Claude at TK-03 authoring intent.md UX brief for slices participating in cross-feature touchpoints; phase test plan §2 cross-feature scenario classes drawing on §2A.3 touchpoints)
- The phase-level instance is self-contained for cross-cutting context: a CC TK-04+ session reading both the phase-level instance and the active feature's per-feature instance (without access to the design file) can ground all references in the CC DS mirror plus the two instances

#### 3A.2.4 Header completeness check

- All §1.1.2 phase-level header required fields are present and well-formed
- `app_slug`, `phase_number` match the paired TDD `app_slug`, `phase_number`
- `Per-feature instances in this phase` list matches the set of features with `tier_1_involved=true` in the paired TDD
- `DS instance version` matches the DS version recorded in the CD-authored design file at the time of authoring

#### 3A.2.5 Disposition

Three outcomes:

- **Pass** — phase-level instance ready for TK-02 sign-off
- **Pass with annotation** — minor gaps inline-annotated; TK-02 sign-off proceeds but the annotation context flows downstream
- **Revise — return to authoring** — material gaps; Hub Claude revises; if gap is rooted in insufficient design file grounding, escalate back to §3A.1 (may trigger Step 2.2 redo on the phase-level cross-cutting sections)

## §3B Per-feature instance checklists

### 3B.1 Per-feature design file quality check (Step 2.3 entry, iterated per tier-1-involved feature)

#### 3B.1.1 Coverage check

For each §2B.x category: the design file's labeled slice for this feature contains visual / annotation material sufficient to ground the corresponding markdown category, OR the category is explicitly marked "not applicable to this feature" by the operator with one-sentence rationale.

#### 3B.1.2 Alignment check

- Affected Tier 1 scope visible in the design file's slice labeled for this feature matches the TDD `§4.{feature-slug}` scope it pairs with — no screens or roles outside TDD scope, no missing scope from TDD; per-feature internal labeling (frame / section / page tag = feature-slug) is present and unambiguous so the slice boundary is identifiable
- Components called out in the slice are clearly named and CD-attributed to the DS — components CD flags as new (not yet in the DS) are captured as §2B.4 additive update plans; cross-cutting additives are also indexed in phase-level §2A.6. DS-conformance of the callouts is CD's responsibility as DS owner (DSG §13.3); Hub does not re-verify against a DS mirror
- Layout pattern choices are clearly annotated in the slice — deviations from the standard mapping carry rationale in design file annotations
- Token usage in the slice (where annotated) is clear enough to transcribe into the per-feature instance
- Accessibility annotations in the slice conform to DSG §6 stance — no formal WCAG conformance claims; engineering hygiene only

#### 3B.1.3 Grounding sufficiency check

- Per-screen interaction content depicted in the slice is concrete enough that Hub Claude can author per-feature instance §2B.3 Key interactions without inventing detail
- Accessibility annotations in the slice are concrete enough that Hub Claude can author per-feature instance §2B.5 without restating DSG §6 baseline
- Visual states (loading, empty, error) are depicted in the slice or explicitly noted as "per DSG §10 defaults" — Hub Claude can author per-feature instance §2B.7 visual regression anchors using the phase-level §2A.5 naming convention

#### 3B.1.4 Disposition

Three outcomes:

- **Pass** — design file slice is sufficient; Hub Claude proceeds to per-feature instance authoring (§3B.2) for this feature
- **Pass with annotation** — minor gaps annotated; Hub Claude proceeds to authoring with annotation context noted in the instance
- **Reject — return to CD for revision** — material gaps in this feature's slice (or labeling itself is missing / ambiguous); operator routes back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback with specific category coverage requests targeting the affected feature's slice (or with a labeling-fix request when the labeling is broken); Step 2.3 pauses for this feature; scope of the Step 2.2 redo is the affected feature's slice (or full phase-level relabeling when labeling is broken)

Disposition outcome is recorded in the operator's working conversation log; not persisted as a Hub canonical artifact (the per-feature instance itself, when authored, becomes the persistent record).

### 3B.2 Per-feature instance authoring quality check (Step 2.3 exit, before TK-02 sign-off, iterated per tier-1-involved feature)

#### 3B.2.1 Coverage check

For each §2B.x category: the Hub-authored per-feature instance markdown contains material on this category, or the category is explicitly marked "not applicable to this feature" with one-sentence rationale (consistent with the §3B.1.1 design file disposition).

#### 3B.2.2 Alignment check

- Every component reference in §2B.3 traces to a component callout in the CD-authored design file's slice for this feature (or to a phase-level §2A.2 shared vocabulary entry when the component is cross-feature)
- Every token reference (where present) traces to a token annotation in the design file's slice
- Every layout pattern reference in §2B.2 traces to a pattern annotation in the design file's slice
- §2B.4 New components or tokens entries follow [RULE] DSG §12.4 minimum change content structure; the `scope` field correctly declares feature-specific vs cross-cutting; cross-cutting entries have a matching phase-level §2A.6 index entry
- §2B.5 accessibility call-outs are feature-specific (no restatement of DSG §6 baseline)
- §2B.6 i18n call-outs are within DS instance i18n scope or trigger §2B.4 / §2A.6 additive plan
- §2B.7 visual regression anchors follow phase-level §2A.5 naming convention

#### 3B.2.3 Downstream sufficiency check

- Each §2B.x category's content is concrete enough that its downstream consumer — per the §0.3 category→consumer map — can author its artifact without inventing detail (e.g. Hub Claude at TK-03 authoring intent.md UX brief, test-plan.yaml `test_type: accessibility` and `test_type: visual_regression` cases when slice-level testing is required)
- The per-feature instance is self-contained for feature-scoped context: a CC TK-04+ session reading the per-feature instance plus the phase-level instance (without access to the design file) can ground all component / token / pattern references in the CC DS mirror (because SK-F reads the CC mirror at code time)

#### 3B.2.4 Header completeness check

- All §1.2.2 per-feature header required fields are present and well-formed
- `feature_slug`, `app_slug`, `phase_number` match the paired TDD `§4.{feature-slug}.Header`
- `Phase-level UX Design Spec ref` points to the same phase's phase-level instance and that instance exists
- `DS instance version` matches the DS version recorded in the CD-authored design file at the time of authoring

#### 3B.2.5 Disposition

Three outcomes:

- **Pass** — per-feature instance ready for TK-02 sign-off; the instance is included in the hub-to-assigned_node onboarding transfer set
- **Pass with annotation** — minor gaps inline-annotated; TK-02 sign-off proceeds but the annotation context flows downstream to TK-03. A "Pass with annotation" instance signals each gap inline at the affected §2B.x category; a CC TK-04+ consumer treats an inline annotation as a flagged gap to surface to the operator rather than silently fill
- **Revise — return to Step 2.3 authoring** — material gaps; Hub Claude revises the markdown; if the gap is rooted in insufficient design file grounding, escalate back to §3B.1 (may trigger Step 2.2 redo on the affected feature's slice)

---

# 4. Anti-drift red flags

The Scope column tags whether the red flag applies to the phase-level instance (`phase`), the per-feature instance (`feature`), or both (`both`).

| Red flag | Scope | What it signals | Response |
|---|---|---|---|
| A per-feature UX Design Spec instance exists for a feature whose TDD `§4.{feature-slug}.Header.tier_1_involved` is `false` | feature | TDD vs UX Spec scope drift; one of the two is wrong | Reconcile TDD and UX Spec scope before proceeding; do not silently accept the spec |
| A phase-level UX Design Spec instance exists but no feature in the phase has `tier_1_involved=true` | phase | Step 2.2 / 2.3 fired without trigger; TDD vs UX Spec drift | Reconcile — either confirm a feature should have `tier_1_involved=true` and update TDD, or remove the phase-level instance |
| Phase-level instance's `Per-feature instances in this phase` list does not match TDD's `tier_1_involved=true` feature set | phase | Header drift; instance set inconsistent across the phase | Update the list; verify each named per-feature instance exists at the declared path |
| Per-feature instance's `Phase-level UX Design Spec ref` is absent or points to a non-existent file | feature | Cross-reference drift; downstream consumers (Hub TK-03 / CC TK-04+) cannot find cross-cutting context | Author the phase-level instance if missing, or fix the reference |
| A per-feature instance contains content properly belonging to phase-level scope (platform shell, shared visual vocabulary definitions, cross-feature touchpoint definitions, VR naming convention) | feature | Granularity scope drift; cross-cutting content duplicated per-feature creates synchronization burden | Move content to phase-level §2A; per-feature instance references phase-level by section id |
| A phase-level instance contains content properly belonging to per-feature scope (per-screen interaction detail, feature-specific a11y call-outs, feature-specific VR anchors, feature-specific layout pattern selection) | phase | Granularity scope drift; phase-level instance grows into per-feature detail it should not own | Move content to the relevant per-feature §2B; phase-level instance retains only cross-cutting summary |
| A UX Design Spec instance (phase or feature) covers content that DS instance would own (project-wide token taxonomy, project-wide layout pattern definitions) | both | Boundary violation between UX Spec instance and project-wide DS instance | Route to DSG additive or breaking update path; do not embed project-wide content in any UX Spec instance |
| Per-feature §2B.3 references components not in DS instance and §2B.4 additive update plan is missing | feature | Incomplete instance; Hub Claude authored §2B.3 without grounding in the design file's slice, OR operator authorized §2B.3 component references without insisting on §2B.4 additive plan | Return to Step 2.3 authoring; flag the missing §2B.4 entry; also surface a §3B.1 design file alignment failure if the components were depicted in the slice |
| §2B.4 entry declares `scope: cross-cutting` but no matching phase-level §2A.6 index entry exists | both | Cross-cutting additive index drift; the additive is invisible at the phase-level surface | Add the §2A.6 index entry pointing to this §2B.4 entry; verify originating-feature designation is consistent |
| §2A.6 cross-cutting additive index entry exists but the originating feature's §2B.4 entry does not | both | Phantom cross-cutting additive index; downstream consumers cannot find the plan content | Either author the originating feature's §2B.4 entry, or remove the §2A.6 index entry if the additive turned out to be feature-specific |
| §2A.3 cross-feature touchpoint references a feature that is not in the phase-level header's `Per-feature instances in this phase` list | phase | Touchpoint references a phantom feature, or the per-feature instance for that feature was not authored | Reconcile — author the missing per-feature instance, or remove the touchpoint, or update the header list |
| **Operator sign-off on TK-02 without applying §3A or §3B reviewer checklists** | both | Process bypass; checklist application is the gate | Re-apply applicable checklists before sign-off; checklist application is the gate, not the artifact's existence |
| **Hub Claude declares any §3 checklist item pass / fail unilaterally without operator decision** | both | Hub Claude scope violation — Hub Claude assists, does not author UX design judgments | Hub Claude reverts to assist-only mode; operator decides each checklist disposition |
| **`[TPL] UX Design Spec` is treated as a CD-authoring template** | both | Misuse — both instance types are Hub-authored markdown spec contracts; CD does not consume this template | Reorient: CD produces design files (CD-native visual artifacts) per [REF] Hub-CD-CC Architecture §3.4.1; this template governs the Hub-authored markdown counterparts at TK-02 Step 2.3 |
| **A UX Design Spec instance (phase or feature) authored at Hub TK-02 Step 2.3 without consulting the CD-authored design file** (when Step 2.2 fired) | both | Authoring without visual grounding; results in spec content disconnected from actual UI design | Re-author with design file grounding; verify content against the design file's cross-cutting sections (phase) or feature's labeled slice (feature) |
| **TK-03 intent.md UX brief invents content not present in the upstream UX Design Spec instances** (phase-level or per-feature) | both | Downstream authoring drift; Hub Claude at TK-03 must extract from upstream, not invent | Return to TK-03 conversion; if the relevant UX Design Spec instance is genuinely silent on a needed UX point, escalate back to TK-02 Step 2.3 for instance revision (route through Step 2.2 if design files also lack the content) |
| **Reference to retired path `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` in any spec artifact** | both | Stale reference; the new paths are `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` and `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Update the reference to the new path(s); verify no other spec artifacts carry the stale path |
| **Operator commits CD design file exports to the monorepo as `specs/ux-design-spec/phase-{N}.md` or `specs/ux-design-spec/{feature-slug}.md`** | both | Path confusion — the design file is a CD-native visual artifact; the `.md` paths are reserved for the Hub-authored markdown spec instances | Move design file exports to `apps/{app-slug}/design-references/phase-{N}/` (phase-scoped because the design file itself is phase-level) or to operator-side storage; ensure the `.md` paths carry only Hub-authored markdown |
| **Operator commits CD design file exports under a `{feature-slug}/` directory** (e.g., `apps/{app-slug}/design-references/{feature-slug}/`) | both | Path-granularity mismatch — the design file is phase-level (one file per phase covering all tier-1-involved features); per-feature scope is captured by CD's internal labeling within the file, not by the path | Move exports to the phase-scoped path `apps/{app-slug}/design-references/phase-{N}/`; the per-feature anchor lives inside the design file (frame / section / page tag = feature-slug) and is cited in the per-feature instance's `Source design file slice` header field |

---

# 5. Maintenance discipline

This template is maintained at the slim content-contract level. When content categories (§2A.1–§2A.6 or §2B.1–§2B.8) are added, removed, or re-scoped, the change is reviewed against the paired and related sources declared in this template's header `Relationship to …` fields and `Pairings I participate in`, reconciled against the authoritative pairing register in [OS] §8.5.2.

When new DSG governance affects the design file grounding or the export conformance review (e.g., a change to §13.3 consumption discipline), §3A and §3B checklist items may need extension to verify the new rule's application.

The phase-level / per-feature granularity split is a structural feature of this template. If a future structural change consolidates the two instance types into one, or further splits them (e.g., app-level instance for shell), the change is itself a structural revision triggering re-verification of P-28 and P-29 (since the §2 organization is the pairing trigger).
