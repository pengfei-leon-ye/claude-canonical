# [TPL] UX Design Spec

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable slim content contract declaring (a) what coverage a per-feature UX Design Spec instance must provide as Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`, produced by Hub Claude at [MECH] Development Track Workflow TK-02 Step 2.3 from CD-authored design files plus Hub DS mirror grounding; and (b) the reviewer checklists applied at TK-02 Step 2.3 — both the design file quality check (against CD-authored design files entering Step 2.3) and the UX Design Spec instance authoring quality check (against the Hub-authored markdown leaving Step 2.3 before TK-02 sign-off)
- **Source Category**: Cat 4
- **Management-System Role**: Outside L1-L5 hierarchy; specification-support template; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; admissibility per [OS] §2.3.2 Cat 4 specification templates row
- **Relationship to [PRIN] People Experience Design Principles**: Applies these principles to per-feature UX content scope; CD-authored design files are expected to be principle-aligned and the Hub-authored UX Design Spec instance grounded in those design files preserves principle application at the spec layer; this template's reviewer checklists surface principle-application gaps at both layers
- **Relationship to [REF] Hub-CD-CC Architecture**: Per §3.4.1 revised, CD outputs **design files** (CD-native visual artifacts) — hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations — at TK-02 Step 2.2 when a feature has `tier_1_involved=true`. Per §5.2 revised three-way distribution model + §5.4 self-authoring discipline, the UX Design Spec instance markdown counterpart is **Hub-authored** at TK-02 Step 2.3, grounded in CD design files + the Hub DS mirror at `hdc_ref_design-system.md`. The content categories enumerated in §2 of this template define what the Hub-authored markdown must cover so downstream consumption (Hub TK-03 + CC TK-04+) is deterministic
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2.1 (Hub → operator → CD) carries Hub PRD/TDD relevant sections as drop files into CD at TK-02 Step 2.2 entry; §2.2 (CD → operator → Hub) carries CD-authored design files back to Hub for TK-02 Step 2.3 design file quality check + UX Design Spec instance authoring; §3.1 (Hub → operator → CC) carries the completed spec bundle (intent / acceptance / test-plan + Hub-authored UX Design Spec instance + CD design files as visual reference) to CC at TK-04 entry
- **Relationship to [MECH] Development Track Workflow**: TK-02 Step 2.2 produces CD-authored design files when `tier_1_involved=true`; TK-02 Step 2.3 produces the Hub-authored UX Design Spec instance markdown grounded in those design files + the Hub DS mirror; TK-03 consumes the UX Design Spec instance as the primary textual UX source for per-slice intent / acceptance / test-plan authoring; TK-04+ consumes the UX Design Spec instance alongside the spec bundle plus design files as visual reference
- **Relationship to [TPL] Technical Design Document Template**: Paired. TDD `§4.{feature-slug}.Header.tier_1_involved` declares whether a feature requires both CD design files (Step 2.2) and a Hub-authored UX Design Spec instance (Step 2.3) for that feature; when true, both are produced before TK-03 per-slice authoring proceeds. The TDD does not carry UX strategy content itself; it references the UX Design Spec instance path
- **Relationship to [TPL] PRD-TDD to Intent and Acceptance Conversion Spec**: Paired. Conversion Spec §3.8 reads the Hub-authored UX Design Spec instance as the source for intent.md UX brief content when Tier 1 is involved in a slice. Flow: CD design files → Hub TK-02 Step 2.3 → UX Design Spec instance markdown → Hub TK-03 (slice intent UX brief extraction) → spec bundle to CC at TK-04
- **Relationship to [TPL] Intent and Acceptance Interface Writing Standard**: Paired. Writing Standard §2.3 defines what intent.md UX brief must contain; this template defines what the upstream Hub-authored UX Design Spec instance must cover so Hub Claude at TK-03 has sufficient material to author the slice-narrow UX brief. The two together close the UX content chain from CD design files (visual) → Hub UX Design Spec (per-feature textual spec) → slice intent UX brief (slice-narrow textual extract)
- **Relationship to [RULE] Design System Governance**: The Hub-authored UX Design Spec instance is grounded in the Hub DS mirror at `hdc_ref_design-system.md` per DSG §13.3 Hub-side consumption discipline. The UX Design Spec instance's §2.4 New-Components-Or-Tokens entry, when present, captures the additive change plan that drives the DSG §12 additive update flow — CD authors the corresponding instance content change at the originating feature's M4 → merge-to-main milestone per DSG §12.5, at which point both DS mirrors (Hub + CC) are re-synced via CD-generated DS markdown export
- **Pairings I participate in**: P-28 (with [TPL] Conversion Spec §2 + §3.8 + [TPL] TDD §4.{feature-slug}.Module-Decomposition — UX Design Spec content-category §2 structural changes trigger Conversion Spec UX brief extraction re-verification), P-29 (with [TPL] Intent-Acceptance §2.3 + §3.9 — UX Design Spec content-category §2 organization changes trigger Writing Standard consumer-side re-verification)

## How to use this source

Use this template when:
- A phase's TDD declares `tier_1_involved: true` for one or more `§4.{feature-slug}` entries at TK-02 Step 2.1, triggering CD design file production (Step 2.2) followed by Hub-side UX Design Spec instance authoring (Step 2.3) for those features
- Hub Claude is performing the design file quality check at TK-02 Step 2.3 entry (against CD-authored design files just transferred from CD)
- Hub Claude is authoring the per-feature UX Design Spec instance markdown at TK-02 Step 2.3, grounding component / token / pattern claims in the Hub DS mirror
- The operator is reviewing the Hub-authored UX Design Spec instance before TK-02 sign-off
- Hub Claude at TK-03 is extracting slice-narrow UX brief content from the UX Design Spec instance for intent.md authoring
- CC at TK-04+ needs to consume the UX Design Spec instance alongside the spec bundle for code generation

Do not use this template:
- As a CD-authoring template — CD produces design files in its CD-native format (per [REF] Hub-CD-CC Architecture §3.4.1); the UX Design Spec instance is the Hub-authored markdown counterpart, not the CD output. CD does not consume this template
- As a substitute for the CD-authored design files — design files are the visual source material from which Hub authors the UX Design Spec instance markdown; they are operator-side reference for CC TK-04+ (visual context for implementation) but are not committed to the monorepo unless the operator explicitly opts to
- As a substitute for the DS instance — DS instance content lives in CD as SOT, with Hub and CC mirrors per [RULE] DSG §1.1 revised three-way distribution model; this template covers per-feature UX scope, not project-wide design system content
- As a CC-authored deliverable — content of this template's instance is Hub-authored at TK-02 Step 2.3, then consumed by CC at TK-04+; CC does not author UX Design Spec instances

## Scope note

This template's scope is **per-feature UX coverage**, not per-slice. A UX Design Spec instance typically covers one TDD `§4.{feature-slug}` worth of UX scope — multiple slices may then consume one instance. The slice-level downstream artifact is intent.md UX brief (Hub-authored by Hub Claude at TK-03, governed by Writing Standard §2.3), which is narrower and references back to the feature's UX Design Spec instance.

---

# 0. Boundary and position

## 0.1 What this source owns

- **The synthesis nature of the instance**: each UX Design Spec instance is a **Hub-authored synthesis** from CD-authored design files (raw source material) grounded against the current Hub DS mirror — not a transcription of design files into markdown. Design files alone are not CC-consumable specification; the synthesis at TK-02 Step 2.3 is the substantive authoring step that produces CC-consumable content. See [REF] Hub-CD-CC Architecture §3.4.1 + §9.4 for the architectural framing.
- The coverage contract: what categories of UX content the Hub-authored UX Design Spec instance must provide for a feature when `tier_1_involved: true`
- The reviewer checklists applied at TK-02 Step 2.3:
  - **Design file quality check** — applied by Hub Claude + operator against CD-authored design files entering Step 2.3 (per [RULE] DSG §13.3 Hub-side consumption discipline)
  - **UX Design Spec instance authoring quality check** — applied by Hub Claude + operator against the Hub-authored markdown leaving Step 2.3, before TK-02 sign-off
- The downstream flow declaration: how UX Design Spec instance content reaches Hub TK-03 (slice intent / acceptance / test-plan) and CC TK-04+ (code generation)
- Anti-drift red flags specific to UX Design Spec instance authoring and consumption

## 0.2 What this source does not own

- The CD-authored design file format (CD-native; visual artifacts including hi-fi mockups, prototypes, wireframes — owned by CD platform behavior per [REF] Hub-CD-CC Architecture §3.4.1; not file-format-specified here)
- The DS instance content (tokens, component inventory, layout patterns) — owned by DSG; lives in CD as SOT with Hub mirror at `hdc_ref_design-system.md` and CC mirror at `specs/design-system.md` per DSG §1.1 revised three-way distribution model
- The intent.md UX brief content — owned by Writing Standard §2.3; Hub-authored at TK-03 by extracting slice-narrow subset from this template's instance
- The accessibility test cases — owned by Test Plan YAML Schema; Hub-authored at TK-03 by deriving from this template's instance §2.5
- TDD `§4.{feature-slug}.Header.tier_1_involved` declaration logic — owned by TDD template
- TK-02 internal step orchestration (Step 2.1 → Step 2.2 → Step 2.3) — owned by [MECH] Development Track Workflow §4 TK-02
- Cross-tool content transfer mechanics (drop files at Step 2.2 entry; design files transfer back at Step 2.3 entry) — owned by [MECH] Cross-Tool Workflow Handoff §2.1 / §2.2

## 0.3 Boundary with downstream consumers

| Downstream consumer | What it consumes from a UX Design Spec instance |
|---|---|
| **Hub Claude (TK-03 intent.md authoring)** | Per-screen content §2.1, components and patterns §2.3, accessibility call-outs §2.5, i18n call-outs §2.6 — extracts slice-relevant subset into intent.md UX brief per Writing Standard §2.3 |
| **Hub Claude (TK-03 acceptance.yaml authoring)** | Visual regression anchors §2.7, motion expectations §2.8 — extracts slice-relevant scenarios for acceptance scenarios per Writing Standard §3.9 |
| **Hub Claude (TK-03 test-plan.yaml authoring)** | Accessibility call-outs §2.5, visual regression anchors §2.7 — produces `test_type: accessibility` and `test_type: visual_regression` cases per Test Plan YAML Schema |
| **CC main loop (TK-04+ code generation)** | Full UX Design Spec instance markdown via the spec bundle at TK-04 entry; CD-authored design files accompany as visual reference (operator-side) for visual context during implementation |
| SK-F (`hdc-arco-enterprise-ui` skill at CC runtime) | Components referenced §2.3, new-asset additive update plans §2.4 — informs code-generation constraints; SK-F additionally grounds in CC DS mirror at `specs/design-system.md` per DSG §13.1 |

**Important consumer-side change vs prior architecture**: Hub Claude authors intent / acceptance / test-plan at TK-03 (the content pillar per [REF] Hub-CD-CC Architecture §5.1); CC does NOT author these UX-touching fields. CC consumes the completed spec bundle (Hub-authored content) at TK-04 entry. This corrects the prior misattribution that listed CC main loop as the authoring party for intent / acceptance / test-plan UX fields.

---

# 1. Instance landing path

UX Design Spec instances are **Hub-authored markdown files** that land at:

```
apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md
```

The instance is produced at TK-02 Step 2.3 by Hub Claude, then transferred to the assigned_node's working directory alongside other TK-02 outputs at the hub-to-assigned_node onboarding step per [MECH] Cross-Tool Workflow Handoff §3.1. CC reads the instance from the monorepo path at TK-04+.

The instance is **per-feature**, not per-slice. Naming convention anchors on `{feature-slug}` matching the TDD `§4.{feature-slug}` entry it pairs with. For walking-skeleton scope (Phase 1 only, rare case where walking-skeleton touches Tier 1), the file is at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md`.

**Source material location**: The CD-authored design files that the UX Design Spec instance is grounded in reside in the CD workspace (CD project / file structure) plus the operator's working materials when transferred to Hub at TK-02 Step 2.3 entry. Design files are operator-side reference at TK-04+ (visual context for CC implementation) and are **not committed to the monorepo by default**. The operator may opt to commit design file exports as auxiliary reference at `apps/{app-slug}/design-references/{feature-slug}/` if useful, but the UX Design Spec instance markdown is the canonical-form artifact.

**Instance header (required)**: Every UX Design Spec instance markdown MUST begin with the following header fields:

```markdown
- **app_slug**: <app-slug>
- **feature_slug**: <feature-slug> (must match TDD §4.{feature-slug}.Header.feature-slug)
- **phase_number**: <N> (must match TDD phase_number)
- **DS instance version**: <semver> (from Hub mirror at hdc_ref_design-system.md header at authoring time)
- **DS markdown export reference**: <path or commit reference for the export that populated the Hub mirror Hub Claude consulted>
- **Source design files**: <reference to CD-authored design files used as source material; informal path or operator-managed location>
- **Status**: Draft | Active | Superseded
- **Authored at**: <date> (TK-02 Step 2.3)
- **Cross-references**: paired TDD §4.{feature-slug}; paired PRD §7.1 feature entry
```

---

# 2. Required content categories

A Hub-authored UX Design Spec instance for a feature must cover the categories below. Coverage means "the instance markdown contains material on this category"; Hub Claude grounds each category in the CD-authored design files + Hub DS mirror per DSG §13.3 consumption discipline. The reviewer checklists in §3 verify coverage at TK-02 Step 2.3.

## 2.1 Affected Tier 1 scope

- Screens or UI flows this feature introduces or modifies in this phase (extracted from CD design files)
- Roles affected (Employee / Manager / HRBP / Admin per [PRIN] People Experience Design Principles role taxonomy)
- Responsive target per screen (desktop primary / tablet primary / mobile primary / cross-device per DSG §11.2 platform tier classification)

## 2.2 HDC layout pattern selection

For each screen in §2.1, the HDC layout pattern from the DS instance pattern catalog (referenced via the Hub DS mirror §5). Rationale required only when the pattern choice is non-obvious or deviates from the standard mapping in DS instance for the screen type.

## 2.3 Components and interaction patterns

- **Tier A (Arco components used)** — components from the DS instance Tier A inventory consumed by this feature (referenced via Hub mirror §4)
- **Tier B (HDC custom components used)** — components from the DS instance Tier B inventory consumed by this feature (referenced via Hub mirror §4)
- **Key interactions per screen** — one-sentence descriptions of the load-bearing interactions extracted from CD design files; components implementing each interaction; entry / exit / branching conditions when non-obvious

## 2.4 New components or tokens (additive update plan, conditional)

Required only when the CD-authored design files introduce components, tokens, icons, or locale strings not yet in the current DS instance.

For each new asset:
- Asset name and type (component / token / icon / locale)
- Rationale (why existing DS items are insufficient, traceable to specific design file content)
- Proposed specification — for components, composition from Arco primitives or new-built structure as observed in design files; for tokens, value and semantic role
- DS instance update plan — pointer to the DSG additive update process per [RULE] DSG §12.3 + §12.4 minimum change content structure; the change merges into CD SOT at the originating feature's M4 → merge-to-main milestone per DSG §12.5, with both mirrors re-synced via CD-generated DS markdown export

If the change is breaking rather than additive, do not capture in §2.4; instead surface as a standalone change file routed through DSG §12.2 breaking-update path before UX Design Spec authoring continues. Hub Claude flags the breaking nature to the operator during TK-02 Step 2.3 authoring.

## 2.5 Accessibility call-outs (slice-specific only)

Coverage required only when the design files reveal specific accessibility concerns beyond Arco component defaults plus DS instance baseline:

- Feature-specific a11y risks (custom Tier B with non-standard interactions, complex flows needing keyboard-only verification — extracted from interaction flows in design files)
- Optional manual validation items for the operator's M4 smoke test
- Any concerns that warrant an on-demand SK-W audit before release

Per [RULE] DSG §6, HDC has no formal WCAG conformance target. Routine a11y recommendations apply uniformly to all slices and need not be restated in the instance; this section captures slice-specific concerns only.

## 2.6 Internationalization and RTL call-outs

- New locale coverage required (if any) — list of new locale codes per DS instance i18n scope declaration; if the feature introduces a locale not already in DS instance §7, an additive update via DSG §12 is needed and captured in §2.4
- RTL-specific layout considerations (if any, observed from design files) — text direction, mirrored components, asymmetric spacing
- Text expansion risk areas (dense labels, table columns, status badges) — call-outs where translated text may overflow visual containers, as identified during design file review

## 2.7 Visual regression anchors

- Screens requiring visual regression baselines (input to Hub TK-03 test-plan.yaml `test_type: visual_regression` cases)
- Approved baseline screenshots reference (when baselines exist from prior features or phases in the same app; informal reference to CD design files or to monorepo screenshots if committed)
- Key visual states to anchor (loading, empty, error, success, edge data — as depicted in design files)

## 2.8 Responsive and motion expectations

- Breakpoint-specific layout differences per screen (when non-default; observed in design files)
- Cross-device behavioral expectations (when non-trivial)
- Non-default motion decisions — defaults are Arco component built-in transitions; this section captures only deviations from DSG §8 motion hygiene
- `prefers-reduced-motion` handling beyond DS instance default (per DSG §8.2)

---

# 3. Reviewer checklists (applied at TK-02 Step 2.3)

TK-02 Step 2.3 has two reviewer checklists applied at distinct points in the step:

- **§3.1 Design file quality check** — applied at Step 2.3 entry, when CD-authored design files arrive in Hub from CD via [MECH] Cross-Tool Workflow Handoff §2.2. Verifies design files are sufficient grounding material for Hub to author the UX Design Spec instance markdown
- **§3.2 UX Design Spec instance authoring quality check** — applied at Step 2.3 exit, before TK-02 sign-off. Verifies the Hub-authored markdown covers all §2 categories grounded in design files + Hub DS mirror

Both checklists are operator-side; Hub Claude assists in walking each but does not declare items pass / fail unilaterally — operator decides each disposition.

## 3.1 Design file quality check (Step 2.3 entry)

### 3.1.1 Coverage check

For each §2.x category: design files contain visual / annotation material sufficient to ground the corresponding markdown category, OR the category is explicitly marked "not applicable to this feature" by the operator with one-sentence rationale.

### 3.1.2 Alignment check

- Affected Tier 1 scope visible in design files matches the TDD `§4.{feature-slug}` scope it pairs with — no screens or roles outside TDD scope, no missing scope from TDD
- Components depicted in design files exist in the DS instance Tier A or Tier B inventory (verified via Hub DS mirror §4) — components not in the inventory require either a §2.4 additive update plan OR the design files are incomplete (return to CD)
- Layout pattern choices in design files align with DS instance pattern catalog (Hub mirror §5) — deviations carry rationale in design file annotations
- Token usage in design files (where annotated) aligns with DS instance token taxonomy (Hub mirror §3)
- Accessibility annotations in design files conform to DSG §6 stance — no formal WCAG conformance claims; engineering hygiene only

### 3.1.3 Grounding sufficiency check

- Per-screen interaction content depicted in design files is concrete enough that Hub Claude can author UX Design Spec instance §2.3 Key interactions without inventing detail
- Accessibility annotations in design files are concrete enough that Hub Claude can author UX Design Spec instance §2.5 without restating DSG §6 baseline
- Visual states (loading, empty, error) are depicted in design files or explicitly noted as "per DSG §10 defaults" — Hub Claude can author UX Design Spec instance §2.7 visual regression anchors

### 3.1.4 Disposition

Three outcomes:

- **Pass** — design files are sufficient; Hub Claude proceeds to UX Design Spec instance authoring (Step 2.3 continues)
- **Pass with annotation** — design files have minor gaps the operator annotates; Hub Claude proceeds to authoring but notes the annotation context in the UX Design Spec instance where applicable
- **Reject — return to CD for revision** — design files have material gaps; operator routes back to CD per [MECH] Cross-Tool Workflow Handoff §6 fallback with specific category coverage requests; Step 2.3 pauses until revised design files arrive; Step 2.2 redo for the affected feature

Disposition outcome is recorded in the operator's working conversation log; not persisted as a Hub canonical artifact (the UX Design Spec instance itself, when authored, becomes the persistent record).

## 3.2 UX Design Spec instance authoring quality check (Step 2.3 exit, before TK-02 sign-off)

### 3.2.1 Coverage check

For each §2.x category: the Hub-authored UX Design Spec instance markdown contains material on this category, or the category is explicitly marked "not applicable to this feature" with one-sentence rationale (consistent with the §3.1.1 design file disposition).

### 3.2.2 Alignment check

- Every component reference in §2.3 corresponds to an actual Tier A or Tier B entry in the Hub DS mirror at the version declared in the instance header
- Every token reference (where present) corresponds to an actual taxonomy entry in the Hub DS mirror
- Every layout pattern reference in §2.2 corresponds to an actual pattern in the Hub DS mirror §5
- §2.4 New-Components-Or-Tokens entries follow [RULE] DSG §12.4 minimum change content structure
- §2.5 accessibility call-outs are slice-specific (no restatement of DSG §6 baseline)
- §2.6 i18n call-outs are within DS instance i18n scope or trigger §2.4 additive plan

### 3.2.3 Downstream sufficiency check

- §2.1 + §2.3 content is concrete enough that Hub Claude at TK-03 can author intent.md UX brief per Writing Standard §2.3 without inventing detail
- §2.5 a11y call-outs are concrete enough that Hub Claude at TK-03 can author test-plan.yaml `test_type: accessibility` cases (when slice-level a11y testing is required)
- §2.7 visual regression anchors are concrete enough that Hub Claude at TK-03 can author test-plan.yaml `test_type: visual_regression` cases (when slice-level visual regression is required)
- The UX Design Spec instance is self-contained: a CC TK-04+ session reading the instance markdown (without access to the CD design files) can ground all component / token / pattern references in the CC DS mirror (because SK-F reads the CC mirror at code time)

### 3.2.4 Header completeness check

- All §1 instance header required fields are present and well-formed
- `feature_slug`, `app_slug`, `phase_number` match the paired TDD `§4.{feature-slug}.Header`
- `DS instance version` matches the Hub mirror header version metadata at the time of authoring
- `DS markdown export reference` is present (for traceability per DSG §12.7)

### 3.2.5 Disposition

Three outcomes:

- **Pass** — UX Design Spec instance ready for TK-02 sign-off; the instance is included in the hub-to-assigned_node onboarding transfer set
- **Pass with annotation** — UX Design Spec instance has minor gaps the operator annotates inline in the instance (or in §2.x category placeholders); TK-02 sign-off proceeds but the annotation context flows downstream to TK-03
- **Revise — return to Step 2.3 authoring** — UX Design Spec instance has material gaps; Hub Claude revises the markdown; if the gap is rooted in insufficient design file grounding, escalate back to §3.1 design file quality check disposition (may trigger Step 2.2 redo)

---

# 4. Anti-drift red flags

| Red flag | What it signals | Response |
|---|---|---|
| A UX Design Spec instance exists for a feature whose TDD `§4.{feature-slug}.Header.tier_1_involved` is `false` | TDD vs UX Spec scope drift; one of the two is wrong | Reconcile TDD and UX Spec scope before proceeding; do not silently accept the spec |
| A UX Design Spec instance covers content that DS instance would own (project-wide token taxonomy, project-wide layout pattern definitions) | Boundary violation between feature-level UX Spec and project-wide DS instance | Route to DSG additive or breaking update path; do not embed project-wide content in feature-level instance |
| UX Design Spec §2.3 references components not in DS instance and §2.4 additive update plan is missing | Incomplete instance; Hub Claude authored §2.3 without grounding in Hub mirror, OR the operator authorized §2.3 component references without insisting on §2.4 additive plan | Return to Step 2.3 authoring; flag the missing §2.4 entry; if the components were depicted in CD design files, also surface a §3.1 design file alignment failure (the design files should have triggered the additive concern earlier) |
| **Operator sign-off on TK-02 without applying §3.1 or §3.2 reviewer checklists** | Process bypass; checklist application is the gate | Re-apply applicable checklists before sign-off; checklist application is the gate, not the artifact's existence |
| **Hub Claude declares any §3 checklist item pass / fail unilaterally without operator decision** | Hub Claude scope violation — Hub Claude assists, does not author UX design judgments | Hub Claude reverts to assist-only mode; operator decides each checklist disposition |
| **`[TPL] UX Design Spec` is treated as a CD-authoring template** | Misuse — this is a Hub-authored markdown spec contract; CD does not consume this template | Reorient: CD produces design files (CD-native visual artifacts) per [REF] Hub-CD-CC Architecture §3.4.1; this template governs the Hub-authored markdown counterpart authored at TK-02 Step 2.3 |
| **A UX Design Spec instance authored at Hub TK-02 Step 2.3 without consulting the Hub DS mirror** | Authoring without grounding violates DSG §13.3 Hub-side consumption discipline | Re-author with mirror grounding; verify every §2.3 component reference, §2.2 pattern reference, and §2.5/§2.6 stance against current Hub mirror |
| **A UX Design Spec instance authored at Hub TK-02 Step 2.3 without consulting CD-authored design files** (when Step 2.2 fired) | Authoring without visual grounding; results in spec content disconnected from actual UI design | Re-author with design file grounding; verify §2.1 screens, §2.3 interactions, §2.7 visual states against design files |
| **TK-03 intent.md UX brief invents content not present in the UX Design Spec instance** | Downstream authoring drift; Hub Claude at TK-03 must extract from the upstream instance, not invent | Return to TK-03 conversion; if the UX Design Spec instance is genuinely silent on a needed UX point, escalate back to TK-02 Step 2.3 for instance revision (route through Step 2.2 if design files also lack the content) |
| **Reference to retired path `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` in any spec artifact** | Stale reference from the prior architecture (when UX content was a CD-authored bundle at this path); the new path is `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Update the reference to the new path; verify no other spec artifacts carry the stale path |
| **Operator commits CD design file exports to the monorepo as `specs/ux-design-spec/{feature-slug}.md`** | Path confusion — design files are CD-native visual artifacts; the `.md` path is reserved for the Hub-authored markdown spec | Move design file exports to `apps/{app-slug}/design-references/{feature-slug}/` (or operator-side storage); ensure `.md` path carries only the Hub-authored markdown |

---

# 5. Maintenance discipline

This template is maintained at the slim content-contract level. When content categories §2.1–§2.8 are added, removed, or re-scoped:

- The change is reviewed against [TPL] TDD `§4.{feature-slug}` paired structure — if TDD per-feature sub-section structure has shifted, this template's coverage scope may need parallel adjustment
- The change is reviewed against [TPL] Conversion Spec §3.8 — if the source-of-UX-brief field changes, this template's downstream flow declaration in §0.3 must be re-verified
- The change is reviewed against [TPL] Intent-Acceptance Writing Standard §2.3 — if UX brief required sub-sections change, this template's §0.3 downstream flow must be re-verified
- The change is reviewed against [RULE] Design System Governance — if SOT-distribution model or §13.3 Hub-side consumption discipline shifts, this template's §1 instance landing path, header fields, and §3 reviewer checklists must be re-verified
- The change is reviewed against [MECH] Development Track Workflow §4 TK-02 Step 2.3 — if the step's role sequence or output set changes, this template's instance authoring location and authoring discipline must be re-verified
- The change is reviewed against [MECH] Cross-Tool Workflow Handoff §2.2 / §3.1 — if the content contracts for CD-authored design file transfer or UX Design Spec instance forwarding change, this template's §0.3 + §1 declarations must be re-verified

When new mirror-related governance is introduced in DSG (e.g., a new Hub mirror consumption rule beyond §13.3), §3.2 alignment check items may need extension to verify the new rule's application.
