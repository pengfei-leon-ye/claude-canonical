# [TPL] UX Design Spec

- **Project**: HR Digital Cockpit
- **Document Type**: Template
- **Status**: Active canonical template
- **Role**: Reusable slim content contract declaring (a) what coverage UX Design Spec **instances at two granularities** must provide — a **phase-level instance** at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` covering cross-cutting UX content for the phase (platform shell, shared visual vocabulary, cross-feature touchpoints, phase-level design decisions, visual regression naming convention, cross-cutting additive index), and **per-feature instances** at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` covering feature-scoped UX content (Affected Tier 1 scope, layout pattern selection, components and interactions, additive plans, a11y, i18n, VR anchors, responsive/motion). Both are CC-authored in the firewalled **S1 (`ux-spec-synthesizer`)** session — the UX-spec synthesis session firewalled from the implementing session (S3) — grounding by default in the feature's PRD/TDD plus the CC DS mirror; on the on-demand CD re-entry path (genuine visual novelty only, proxied by a new design token / new visual language), the CD-authored phase-level design file is pulled back as visual reference and the phase-level instance grounds in its cross-cutting sections while each per-feature instance grounds in that feature's labeled slice. The default app-level path has no CD design file (CD app-level visual is default-retired per [REF] Hub-CD-CC Architecture); and (b) the reviewer checks applied in S1 (synthesis quality, with an independent `ux-spec-cross-checker` reader) for each instance type. Granularity asymmetry between the on-demand design file (one phase-level design file) and the spec output (one phase-level instance + N per-feature instances) is intentional — see [REF] Hub-CD-CC Architecture §3.4.1.
- **Source Category**: Cat 4
- **Management-System Role**: Outside L1-L5 hierarchy; specification-support template; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; admissibility per [OS] §2.3.2 Cat 4 specification templates row (UX Design Spec is one Cat 4 template covering both instance types)
- **Relationship to [PRIN] People Experience Design Principles**: Applies these principles to both phase-level cross-cutting UX content (shell, vocabulary, cross-feature touchpoints) and per-feature UX content scope; the CC-authored UX Design Spec instances preserve principle application at the spec layer — grounded by default in PRD/TDD plus the CC DS mirror, and on the on-demand CD re-entry path additionally in the (principle-aligned) CD design file; this template's reviewer checks surface principle-application gaps at both layers
- **Relationship to [REF] Hub-CD-CC Architecture**: Per §3.4.1 revised, app-level visual design is **default-retired**: by default CC produces Arco-React directly with no CD design file, and the UX Design Spec instances ground in PRD/TDD plus the CC DS mirror. **On-demand only**, on genuine visual novelty (proxied by a new design token / new visual language), CD outputs a **phase-level design file** (CD-native visual artifacts) — hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations, **plus phase-level cross-cutting sections (platform shell, shared visual vocabulary, cross-feature touchpoint maps, phase-level design decisions, visual regression naming convention)** and per-feature internal labeling — which CC pulls back as visual reference. The UX Design Spec instances are CC-authored in the firewalled S1 (`ux-spec-synthesizer`) session at **two granularities**: one **phase-level UX Design Spec instance** synthesizing cross-cutting content, and **N per-feature UX Design Spec instances** (one per tier-1-involved feature) each synthesizing that feature's scope. The content categories enumerated in §2A (phase-level) and §2B (per-feature) of this template define what the CC-authored markdown must cover so downstream consumption (CC S2 acceptance/intent + S3 implementation) is deterministic
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: On the on-demand visual path only (genuine visual novelty — a new design token / new visual language), §4.3 (CC → operator → CD) pushes the feature's PRD/TDD text into the CD project's `uploads/`, the operator designs in CD UI, and §4.2 (CD → operator → CC) returns the resulting design file directly to CC as visual reference — it does not route through Hub. The UX Design Spec instance markdowns (both granularities) are **CC-authored** in the firewalled `ux-spec-synthesizer` session and produced in-repo, not Hub → CC transferred; §3.1 (Hub → operator → CC) carries only the upstream content (PRD / TDD main + phase test plans + slice-lists + OpenAPI) to CC at TK-04 entry
- **Relationship to [MECH] Development Track Workflow**: TK-02 Step 2.2 (on-demand CD app-level design file) is **default-retired**, re-entered only on genuine visual novelty (new design token / new visual language); TK-02 Step 2.3 is CC-side UX Design Spec synthesis in the firewalled **S1** session (`ux-spec-synthesizer` + `ux-spec-cross-checker`), producing (a) one **phase-level UX Design Spec instance** and (b) **N per-feature UX Design Spec instances**, grounded in the Hub-authored PRD/TDD by default and additionally in the design file when on-demand re-entry produced one — authored incrementally just-ahead-of-code per the JIT model, not all-up-front per phase; the relocated **TK-03** (CC **S2** acceptance/intent session) consumes both as the primary textual UX source for per-slice intent / acceptance / test-plan authoring — the phase-level instance for cross-feature touchpoints / shell / shared vocabulary references, the per-feature instance for feature-scoped UX content; the implementing **S3** session consumes both alongside the upstream content, plus the on-demand design file as visual reference when one exists
- **Relationship to [TPL] Technical Design Document Template**: Paired. TDD `§4.{feature-slug}.Header.tier_1_involved` declares whether a feature requires a per-feature UX Design Spec instance, CC-authored in the firewalled S1 session (TK-02 Step 2.3); when any feature in the phase has `tier_1_involved=true`, the phase-level UX Design Spec instance is also produced in S1. Step 2.3 produces one phase-level instance plus iterates per-feature instances, incrementally just-ahead-of-code per the JIT model. The on-demand CD design file (Step 2.2) is **not** a per-phase artifact — it is default-retired, produced only when a feature carries genuine visual novelty (new-token trigger), in which case that feature is labeled as a slice within the design file. The TDD does not carry UX strategy content itself; it references both UX Design Spec instance paths. TDD §2.2.5 Integration boundaries vs phase-level UX Spec §2A.3 Cross-feature touchpoints: TDD captures interface-level contracts (API / event / data); UX Spec captures interaction-level contracts (CTA / jump / mask / state-propagation visible to users) — they are paired but non-overlapping.
- **Relationship to [TPL] PRD-TDD to Intent and Acceptance Conversion Spec**: Paired. Conversion Spec §3.8 reads both the phase-level and per-feature UX Design Spec instances as the source for intent.md UX brief content when Tier 1 is involved in a slice — per-feature instance for screens / interactions / components / a11y / i18n within the slice; phase-level instance for cross-feature touchpoints the slice participates in plus shared vocabulary references. Flow: Hub-authored PRD/TDD (the coherence anchor) → CC S1 UX-spec synthesis (TK-02 Step 2.3, `ux-spec-synthesizer`) → two-tier UX Design Spec instances → CC S2 acceptance/intent (the relocated TK-03, slice intent UX brief extraction) → implementing S3 session. On the on-demand visual path (genuine visual novelty), a CD design file is pulled back into S1 as visual reference grounding the synthesis
- **Relationship to [TPL] Intent and Acceptance Interface Writing Standard**: Paired. Writing Standard §2.3 defines what intent.md UX brief must contain; this template defines what the upstream CC-authored UX Design Spec instances (phase-level + per-feature) must cover so the CC S2 acceptance/intent session (the relocated TK-03) has sufficient material to author the slice-narrow UX brief. The two together close the UX content chain from PRD/TDD (plus the CC DS mirror, and on the on-demand path a CD design file as visual reference) → CC-authored UX Design Spec instances (phase-level + per-feature textual spec) → slice intent UX brief (slice-narrow textual extract)
- **Relationship to [TPL] Phase Test Plan**: Paired. Phase test plan §2 Cross-feature scenario classes and §3 App-scale NFR scenario classes consume cross-feature touchpoint definitions from the phase-level UX Design Spec instance §2A.3 when scenarios cross UI-layer touchpoints; visual regression naming convention used across per-feature test plans (`test_type: visual_regression` cases) is sourced from phase-level UX Design Spec §2A.5. The phase-level instance is **on-demand** in the new model (the cross-cutting categories it carries — touchpoint definitions, VR naming — exist whenever a phase has cross-cutting UX content; they are CC-authored in S1, not contingent on a CD phase-level design file). When a phase's UX content is minimal enough that no phase-level instance is authored, the phase test plan derives cross-cutting scenario classes and VR naming directly from the per-feature instances and the TDD
- **Relationship to [RULE] Design System Governance**: Both CC-authored UX Design Spec instance types ground by default in the feature's PRD/TDD plus the CC DS mirror (read via SK-F per DSG §13.1), and additionally in the CD design file when on-demand re-entry has produced one — per DSG §13.3 CC-side consumption discipline. The per-feature instance's §2B.4 New components or tokens entry, when present, captures the additive change plan that drives the DSG §12 additive update flow; the phase-level instance's §2A.6 is an **index** of cross-cutting additives (additives genuinely shared across multiple features in the phase, with a designated first-owner feature) that cross-references the originating feature's §2B.4 plan — CD authors the corresponding DS instance content change at the originating feature's M4 → merge-to-main milestone per DSG §12.5 (meta-DS authoring is CD's SOT, UNCHANGED), at which point the CC mirror is re-synced via the reviewed CD-generated DS markdown export. The cross-cutting vs feature-specific boundary that §2A.6 / §2B.4 implement is governed by DSG §5.2.4 (reuse-scope criterion); the two are paired (P-54 in [OS] §8.5.2)
- **Pairings I participate in**: P-28 (with [TPL] Conversion Spec §2 + §3.8 + [TPL] TDD §4.{feature-slug}.Module-Decomposition — UX Design Spec content-category structural changes — across §2A or §2B — trigger Conversion Spec UX brief extraction re-verification), P-29 (with [TPL] Intent-Acceptance §2.3 + §3.9 — UX Design Spec content-category structural organization changes across §2A or §2B trigger Writing Standard consumer-side re-verification), P-54 (with [RULE] DSG §5.2.4 — the reuse-scope criterion governs the cross-cutting vs feature-specific classification that §2A.6 / §2B.4 implement; a change to the criterion, or to these sections' classification semantics, re-verifies the other within the same period)

## How to use this source

Use this template when:
- A phase's TDD declares `tier_1_involved: true` for one or more `§4.{feature-slug}` entries at TK-02 Step 2.1, triggering CC-side UX Design Spec instance authoring in the firewalled S1 session (Step 2.3, one phase-level instance + iterated per-feature instances), incrementally just-ahead-of-code per the JIT model
- On the on-demand visual path only (genuine visual novelty — a new design token / new visual language), the `ux-spec-synthesizer` is grounding against a CD design file pulled back as visual reference — applying the phase-level cross-cutting check against the design file's cross-cutting sections plus the per-feature slice check against each tier-1-involved feature's labeled slice
- The `ux-spec-synthesizer` subagent (CC S1) is authoring the phase-level UX Design Spec instance markdown at TK-02 Step 2.3, grounding cross-cutting content (shell / vocabulary / touchpoints / phase decisions / VR naming) in the feature's PRD/TDD plus the CC DS mirror by default, and additionally in the CD design file's cross-cutting sections on the on-demand path
- The `ux-spec-synthesizer` subagent (CC S1) is authoring a per-feature UX Design Spec instance markdown at TK-02 Step 2.3, grounding component / token / pattern claims in the feature's PRD/TDD plus the CC DS mirror by default, and additionally in the relevant feature's labeled slice of the CD design file on the on-demand path
- The `ux-spec-cross-checker` subagent is independently reading the synthesized UX Design Spec instances (phase-level and per-feature) against the grounding material (propose-not-author, mirroring DSG §12.1) before the S1 session finalizes
- The CC S2 acceptance/intent session (the relocated TK-03) is extracting slice-narrow UX brief content — from the per-feature instance for in-slice UX, from the phase-level instance for cross-feature touchpoints the slice participates in plus shared vocabulary references
- The implementing S3 session needs to consume the UX Design Spec instances alongside the upstream content for code generation

Do not use this template:
- As a CD-authoring template — on the on-demand visual path CD produces design files in its CD-native format (per [REF] Hub-CD-CC Architecture §3.4.1); both CC-authored UX Design Spec instance types are the markdown counterparts, not the CD output. CD does not consume this template
- As a substitute for the on-demand CD design file — when the on-demand visual path fires, the design file is the visual source material CC pulls back as reference for the synthesis; it is operator-side / CC visual reference but is not committed to the monorepo unless the operator explicitly opts to commit exports at `apps/{app-slug}/design-references/phase-{N}/`. On the default path there is no design file (app-level visual is default-retired)
- As a substitute for the DS instance — DS instance content lives in CD as SOT, with a CC code-time mirror per [RULE] DSG §1.1 two-way distribution model; this template covers per-phase + per-feature UX scope, not project-wide design system content
- As a Hub-authored deliverable — the UX Design Spec instances are **CC-authored** in the firewalled S1 (`ux-spec-synthesizer`) session, firewalled from the implementing session S3; they are not Hub-authored and not Hub → CC transferred. CC authors them in-repo and consumes them in the relocated TK-03 (S2) and implementation (S3)

## Scope note

This template's scope covers **two distinct UX Design Spec instance types**, distinguished by granularity:

| Instance type | File | Scope | Quantity per phase |
|---|---|---|---|
| **Phase-level UX Design Spec instance** | `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` | Cross-cutting UX content for the phase (shell / vocabulary / touchpoints / phase decisions / VR naming / cross-cutting additive index) | At most one (authored in S1 when the phase has cross-cutting UX content; content categories may be marked "not applicable" when minimal; omitted entirely when the phase has no cross-cutting UX content) |
| **Per-feature UX Design Spec instance** | `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Feature-scoped UX content (one TDD `§4.{feature-slug}` worth of UX scope — multiple slices may then consume one instance) | One per `tier_1_involved=true` feature in the phase |

Both instance types are CC-authored in the firewalled S1 (`ux-spec-synthesizer`) session at TK-02 Step 2.3. The slice-level downstream artifact is intent.md UX brief (CC-authored in the S2 acceptance/intent session — the relocated TK-03, governed by Writing Standard §2.3), which is narrower than per-feature scope and references back to both UX Design Spec instances.

---

# 0. Boundary and position

## 0.1 What this source owns

- **The synthesis nature of the instances**: each CC-authored UX Design Spec instance (phase-level or per-feature) is a **synthesis** — a structuring of the feature's PRD/TDD plus the CC DS mirror (and, on the on-demand path, a CD design file's visual + informal-annotation content) into CC-consumable markdown, integrated with adjacent spec artifacts, not a verbatim transcription. The synthesis in the CC S1 (`ux-spec-synthesizer`) session at TK-02 Step 2.3 is the substantive authoring step that produces CC-consumable content. See [REF] Hub-CD-CC Architecture §3.4.1 + §9.4 for the architectural framing.
- The coverage contracts: what categories of UX content the **phase-level** instance must provide (§2A) when the phase has cross-cutting UX content, and what categories the **per-feature** instance must provide (§2B) when a feature has `tier_1_involved=true`
- The reviewer checks applied in the CC S1 session, by instance type:
  - **Phase-level synthesis-quality check** (with conditional design-file-grounding check on the on-demand path) — §3A
  - **Per-feature synthesis-quality check** (with conditional design-file-grounding check on the on-demand path) — §3B
  - Both check types use the same structural pattern (a grounding-sufficiency check on the synthesis inputs + an authoring quality check on the synthesized markdown) but anchor on different content categories; the `ux-spec-cross-checker` subagent is the independent reader applying them
- The downstream flow declaration: how UX Design Spec instance content (phase-level + per-feature) reaches the CC S2 acceptance/intent session (the relocated TK-03 — slice intent / acceptance / test-plan) and the implementing S3 session (code generation)
- The cross-reference rules between the two instance types (per-feature instance header references phase-level instance; phase-level instance §2A.3 cross-feature touchpoints reference per-feature instances participating in each touchpoint; phase-level instance §2A.6 cross-cutting additive index references first-owner feature's §2B.4 entry)
- Anti-drift red flags specific to UX Design Spec instance authoring and consumption — covering both granularity scope drift (phase-level content in per-feature instance / per-feature content in phase-level instance) and the existing per-feature drift signals

## 0.2 What this source does not own

- The CD-authored design file format (CD-native; visual artifacts including hi-fi mockups, prototypes, wireframes — owned by CD platform behavior per [REF] Hub-CD-CC Architecture §3.4.1; not file-format-specified here)
- The DS instance content (tokens, component inventory, layout patterns) — owned by DSG; lives in CD as SOT with a CC mirror at `specs/design-system.md` per DSG §1.1 two-way distribution model
- The intent.md UX brief content — owned by Writing Standard §2.3; CC-authored in the S2 acceptance/intent session (the relocated TK-03) by extracting slice-narrow subset from this template's instances (both phase-level and per-feature where applicable)
- The accessibility test cases — owned by Test Plan YAML Schema; CC-authored in the S2 acceptance/intent session (the relocated TK-03) by deriving from this template's per-feature instance §2B.5
- TDD `§4.{feature-slug}.Header.tier_1_involved` declaration logic — owned by TDD template
- TDD §2.2.5 Integration boundaries — owned by TDD template; pairs with this template's phase-level §2A.3 Cross-feature touchpoints but does not overlap (TDD = interface-level contracts; UX Spec = interaction-level contracts)
- TK-02 internal step orchestration (Step 2.1 Hub TDD → Step 2.2 on-demand CD design file → Step 2.3 CC S1 synthesis) and the S1→S2→S3 session pipeline — owned by [MECH] Development Track Workflow §4 TK-02
- Cross-tool content transfer mechanics on the on-demand visual path (CC → CD `uploads/` push at §4.3; design file pulled back to CC at §4.2) — owned by [MECH] Cross-Tool Workflow Handoff §4.2 / §4.3

## 0.3 Boundary with downstream consumers

| Downstream consumer | What it consumes from a UX Design Spec instance |
|---|---|
| **CC S2 (relocated TK-03 intent.md authoring)** | Per-feature §2B.1 screens, §2B.3 components and patterns, §2B.5 a11y, §2B.6 i18n — extract slice-relevant subset; **plus phase-level §2A.3 cross-feature touchpoints when the slice participates in a touchpoint, §2A.2 shared vocabulary when the slice consumes a shared visual contract** — into intent.md UX brief per Writing Standard §2.3 |
| **CC S2 (relocated TK-03 acceptance.yaml authoring)** | Per-feature §2B.7 visual regression anchors, §2B.8 motion expectations — extract slice-relevant scenarios for acceptance scenarios per Writing Standard §3.9 |
| **CC S2 (relocated TK-03 test-plan.yaml authoring)** | Per-feature §2B.5 a11y, §2B.7 visual regression anchors — produce `test_type: accessibility` and `test_type: visual_regression` cases per Test Plan YAML Schema; **plus phase-level §2A.5 visual regression naming convention** for case-naming consistency across features |
| **Hub Claude (TK-02 Step 2.1 phase test plan authoring)** | Phase-level §2A.3 cross-feature touchpoints feed phase test plan §2 cross-feature scenario classes; phase-level §2A.5 VR naming convention is referenced by phase test plan §2.2.7 testing strategy. (Phase test plan authoring at Step 2.1 stays Hub-side; when no phase-level instance exists, it derives these from the per-feature instances + TDD) |
| **CC main loop (implementing S3 code generation)** | Full UX Design Spec instances (phase-level + the relevant per-feature), read in-repo at `apps/{app-slug}/specs/ux-design-spec/**`; on the on-demand path the CD design file accompanies as visual reference for visual context during implementation |
| SK-F (`hdc-arco-enterprise-ui` skill at CC runtime) | Per-feature §2B.3 components referenced, §2B.4 New components or tokens; phase-level §2A.2 shared visual vocabulary, §2A.6 cross-cutting additive index — informs code-generation constraints; SK-F additionally grounds in CC DS mirror at `specs/design-system.md` per DSG §13.1 |

CC authors intent / acceptance / test-plan in the firewalled S2 acceptance/intent session (the relocated TK-03 — the content pillar per [REF] Hub-CD-CC Architecture §5.1), grounded in the Hub-authored PRD/TDD as the independent intent root and the CC-authored UX Design Spec instances from S1. The firewall is the **S2 ⊥ S3 session/context boundary** — the implementing session does not author or influence intent/acceptance — not a Hub-vs-CC workspace boundary. The implementing S3 session consumes these in-repo.

---

# 1. Instance landing paths and headers

This template governs two instance types with distinct landing paths. Both are **CC-authored in-repo** in the firewalled S1 (`ux-spec-synthesizer`) session at TK-02 Step 2.3, written directly to the monorepo paths below — they are not Hub-authored and not Hub → CC transferred. The S2 acceptance/intent session and the implementing S3 session read the instances from these monorepo paths.

## 1.1 Phase-level UX Design Spec instance

### 1.1.1 Landing path

```
apps/{app-slug}/specs/ux-design-spec/phase-{N}.md
```

At most one phase-level instance per phase. The file's `{N}` matches the paired phase TDD's `phase_number`. The instance is authored in the CC S1 session whenever the phase has cross-cutting UX content to capture (typically when at least one feature has `tier_1_involved=true`); content categories that do not apply to the phase are explicitly marked "not applicable to this phase" with one-sentence rationale. When a phase has no cross-cutting UX content, the phase-level instance is omitted entirely.

**Source material location**: By default the synthesis grounds in the feature's PRD/TDD plus the CC DS mirror at `specs/design-system.md` (read via SK-F at synthesis time) — there is no CD design file on the default path (app-level visual is default-retired). **On the on-demand visual path only** (genuine visual novelty — a new design token / new visual language), a CD-authored phase-level design file is pulled back into the S1 session via DesignSync MCP read (per [MECH] Cross-Tool Workflow Handoff §4.2); its **cross-cutting sections** (platform shell artboards, shared visual vocabulary artboards, cross-feature touchpoint maps, phase-level design decision logs, VR naming convention annotations) then become additional source material for the phase-level instance. When it exists, the design file is CC/operator-side visual reference and is **not committed to the monorepo by default**; the operator may opt to commit design file exports as auxiliary reference at `apps/{app-slug}/design-references/phase-{N}/`, but the UX Design Spec instance markdowns are the canonical-form artifacts.

### 1.1.2 Instance header (required)

Every phase-level UX Design Spec instance markdown MUST begin with the following header fields:

```markdown
- **app_slug**: <app-slug>
- **phase_number**: <N> (must match paired TDD phase_number)
- **DS instance version**: <semver> (the DS version recorded in the CC DS mirror at `specs/design-system.md` at synthesis time; on the on-demand path, the version recorded in the CD design file when it carries one)
- **Source material**: <on the default path, "PRD/TDD + CC DS mirror (no design file — app-level visual default-retired)"; on the on-demand visual path, additionally a reference to the CD-authored phase-level design file used as visual reference (informal path or operator-managed location), citing the specific cross-cutting sections / artboards (frame / section / page tags for shell / vocab / touchpoints / decisions / VR naming) so the grounding chain from phase spec → design file cross-cutting sections is auditable>
- **Per-feature instances in this phase**: <list of feature-slugs whose per-feature UX Design Spec instances pair with this phase-level instance; must match the set of features with `tier_1_involved=true` in the paired TDD>
- **Status**: Draft | Active | Superseded
- **Authored at**: <date> (CC S1 `ux-spec-synthesizer`, TK-02 Step 2.3)
- **Cross-references**: paired TDD `apps/{app-slug}/specs/tdd/phase-{N}.md`; paired phase test plan `apps/{app-slug}/specs/test-plan/phase-{N}.md`
```

## 1.2 Per-feature UX Design Spec instance

### 1.2.1 Landing path

```
apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md
```

One per-feature instance per `tier_1_involved=true` feature in the phase. Naming convention anchors on `{feature-slug}` matching the TDD `§4.{feature-slug}` entry it pairs with. For walking-skeleton scope (Phase 1 only, rare case where walking-skeleton touches Tier 1), the file is at `apps/{app-slug}/specs/ux-design-spec/walking-skeleton.md` (treated as a feature-slug-equivalent).

**Source material location**: By default the per-feature instance grounds in the feature's PRD/TDD plus the CC DS mirror (read via SK-F) — no CD design file on the default path. On the on-demand visual path, it additionally grounds in **the feature's labeled slice** (frame / section / page tag matching this instance's `feature_slug`) of the CD design file pulled back per [MECH] Cross-Tool Workflow Handoff §4.2, per [REF] Hub-CD-CC Architecture §3.4.1 + [RULE] DSG §13.3 CC-side consumption discipline.

### 1.2.2 Instance header (required)

Every per-feature UX Design Spec instance markdown MUST begin with the following header fields:

```markdown
- **app_slug**: <app-slug>
- **feature_slug**: <feature-slug> (must match TDD §4.{feature-slug}.Header.feature-slug)
- **phase_number**: <N> (must match TDD phase_number)
- **DS instance version**: <semver> (the DS version recorded in the CC DS mirror at `specs/design-system.md` at synthesis time; on the on-demand path, the version recorded in the CD design file when it carries one)
- **Source material**: <on the default path, "PRD/TDD + CC DS mirror (no design file — app-level visual default-retired)"; on the on-demand visual path, additionally a reference to the CD-authored phase-level design file plus the specific per-feature labeled slice within it — the frame / section / page tag matching this instance's `feature_slug` — so the grounding chain from feature spec → design file slice is auditable>
- **Phase-level UX Design Spec ref**: `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` (when a phase-level instance exists for the phase)
- **Status**: Draft | Active | Superseded
- **Authored at**: <date> (CC S1 `ux-spec-synthesizer`, TK-02 Step 2.3)
- **Cross-references**: paired TDD §4.{feature-slug}; paired PRD §7.1 feature entry; phase-level UX Design Spec instance (above)
```

---

# 2. Required content categories

This template defines two parallel content category sets, one per instance type. Coverage means "the instance markdown contains material on this category"; the `ux-spec-synthesizer` grounds each category in the feature's PRD/TDD plus the CC DS mirror by default, and additionally in the CD design file on the on-demand visual path, per DSG §13.3 CC-side consumption discipline. The reviewer checks in §3 verify coverage in the CC S1 session, with `ux-spec-cross-checker` as the independent reader.

## §2A Phase-level instance — content categories

A CC-authored phase-level UX Design Spec instance must cover the categories below when the phase has cross-cutting UX content. Categories that do not apply to a particular phase are explicitly marked "not applicable to this phase" with one-sentence rationale.

**Grounding note (applies to all §2A categories)**: by default the `ux-spec-synthesizer` grounds each category in the feature's PRD/TDD plus the CC DS mirror — there is no CD design file on the default path. Where a category below says "design file" / "artboard" / "as depicted", that is the **on-demand visual path** source (read it as "from the PRD/TDD + CC DS mirror by default, and from the CD design file's corresponding section when on-demand re-entry produced one"). The design-file references are the conditional visual-grounding branch, not a mandatory dependency.

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

Coverage of additive Tier B components, tokens, icons, or locales that are **cross-cutting** — shared across multiple features in the phase (not single-feature additives), per the **[RULE] DSG §5.2.4 reuse-scope criterion** (peer-instantiated across ≥2 features with no single owning feature mediating; a component surfaced in a second feature only through a declared structural seam such as `ObjectPage` facet-body injection is **not** cross-cutting and stays in its owning feature's §2B.4). Each entry:

- Asset name and type (component / token / icon / locale)
- Cross-cutting nature (one sentence on why this additive is genuinely shared, not feature-specific)
- **Originating feature** (the first-owner feature-slug as designated in the CD-authored design file; this is the feature whose `tier_1_involved=true` slice depicts the additive's first use, and whose M4 → merge-to-main milestone will carry the DS instance update per DSG §12.5)
- **Source of additive update plan**: cross-reference to the originating feature's per-feature instance §2B.4 entry where the full additive plan content is authored (per DSG §12.4 minimum change content structure)

This category is an **index**, not a duplicate plan. The DSG §12 additive flow's authoritative artifact remains the originating feature's §2B.4 entry; this index ensures cross-cutting additives are discoverable from the phase-level instance and that downstream consumers (the CC S2 acceptance/intent and implementing S3 sessions) can locate them efficiently.

Single-feature additives (introduced and used only by one feature) stay in that feature's §2B.4 entry and do NOT appear in this index.

If a phase has no cross-cutting additives, this category is marked "not applicable to this phase; no cross-cutting additive components / tokens introduced."

## §2B Per-feature instance — content categories

A CC-authored per-feature UX Design Spec instance for a feature must cover the categories below when that feature has `tier_1_involved=true`.

**Grounding note (applies to all §2B categories)**: by default the `ux-spec-synthesizer` grounds each category in the feature's PRD/TDD plus the CC DS mirror — there is no CD design file on the default path. Where a category below says "design file" / "slice" / "as called out / extracted from / observed in the design file", that is the **on-demand visual path** source (read it as "from the PRD/TDD + CC DS mirror by default, and from the feature's labeled slice of the CD design file when on-demand re-entry produced one"). The design-file references are the conditional visual-grounding branch, not a mandatory dependency.

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
- **Scope**: declare whether this additive is **feature-specific** or **cross-cutting**, per the **[RULE] DSG §5.2.4 reuse-scope criterion** (cross-cutting iff directly instantiated as a peer by slices of ≥2 distinct features with no single owning feature mediating the reuse; a component surfaced in a second feature only through a declared structural seam — e.g. `ObjectPage` facet-body injection — stays feature-specific). If cross-cutting, this feature is the designated first-owner, the asset is registered in the DS instance §4 inventory, and it is also indexed in phase-level §2A.6; if feature-specific, it stays in this §2B.4 entry and is not given a DS instance §4 inventory entry
- Rationale (why existing DS items are insufficient, traceable to specific design file content)
- Proposed specification — for components, composition from Arco primitives or new-built structure as observed in design files; for tokens, value and semantic role
- DS instance update plan — pointer to the DSG additive update process per [RULE] DSG §12.3 + §12.4 minimum change content structure; the change merges into CD SOT at this feature's M4 → merge-to-main milestone per DSG §12.5, with the CC mirror re-synced via the reviewed CD-generated DS markdown export

If the change is breaking rather than additive, do not capture in §2B.4; instead surface as a standalone change file routed through DSG §12.2 breaking-update path before UX Design Spec authoring continues. The `ux-spec-synthesizer` flags the breaking nature to the operator during S1 (TK-02 Step 2.3) authoring.

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

# 3. Reviewer checks (applied in the CC S1 session)

The CC S1 (`ux-spec-synthesizer`) session applies two parallel check sets, one per instance type. Each set follows the same structural pattern: a **grounding-sufficiency check** at entry (verifying the synthesis inputs are sufficient — PRD/TDD + CC DS mirror by default, plus the CD design file on the on-demand visual path) and an **authoring quality check** at exit (verifying the CC-authored markdown covers all required content categories grounded in those inputs). The **design-file quality check** described in §3A.1 / §3B.1 is the **conditional on-demand-path branch** of the grounding-sufficiency check; on the default path (no design file) the grounding-sufficiency check runs against PRD/TDD + the CC DS mirror only.

The check sets run inside the CC S1 session: the `ux-spec-synthesizer` authors and self-checks, and the `ux-spec-cross-checker` subagent is the **independent reader** (propose-not-author, mirroring [RULE] DSG §12.1 propose-not-write) that surfaces grounding / coverage gaps for the synthesizer to resolve. This is a CC-internal synthesis-quality loop, not a Hub TK-02 operator sign-off gate.

The S1 sequencing is: phase-level grounding-sufficiency check (§3A.1) → if pass, phase-level instance authoring (§3A.2) **and** per-feature grounding-sufficiency checks iterated (§3B.1). Per-feature authoring (§3B.2) iterates over the features whose grounding checks passed. Phase-level and per-feature work may interleave in practice (the phase-level instance can be drafted in parallel with per-feature drafts), but S1 finalization requires all checks pass.

## §3A Phase-level instance checks

### 3A.1 Phase-level grounding-sufficiency check (S1 entry)

On the default path this verifies PRD/TDD + the CC DS mirror are sufficient grounding for each §2A.x category. The design-file checks below are the **conditional on-demand-path branch** — they apply only when on-demand re-entry has produced a CD design file.

#### 3A.1.1 Coverage check

For each §2A.x category: the grounding inputs (PRD/TDD + CC DS mirror by default; on the on-demand path, additionally the design file's cross-cutting sections — shell artboards, vocabulary artboards, touchpoint maps, phase-level decision logs, VR naming annotations) contain material sufficient to ground the corresponding markdown category, OR the category is explicitly marked "not applicable to this phase" with one-sentence rationale.

#### 3A.1.2 Alignment check

- Platform shell content matches the phase's actual scope (no shell elements outside this phase's TDD; no missing shell content TDD declared)
- Shared visual vocabulary items are clearly named and resolve against the CC DS mirror — items not yet in the DS (on the on-demand path, items CD flags as new in the slice) are captured as §2A.6 cross-cutting additive index entries with originating-feature designation
- Cross-feature touchpoints (from the TDD by default; depicted in the design file on the on-demand path) align with TDD §2.2.5 Integration boundaries (paired but non-overlapping — every touchpoint with an interface contract has a matching TDD entry)
- Phase-level horizontal decisions are concretely grounded (traceable to a TDD decision or, on the on-demand path, an artboard / annotation visibly demonstrating each; decisions floating without anchors are flagged)
- VR naming convention is derivable (feature prefix table + state vocabulary derivable from the per-feature TDD scope, OR — on the on-demand path — present in the design file's annotations / per-feature labeling)

#### 3A.1.3 Grounding sufficiency check

- Shell IA is concrete enough to author §2A.1 without inventing navigation taxonomy
- Vocabulary items are semantically clear — the `ux-spec-synthesizer` can author each §2A.2 entry with confidence
- Touchpoints (from TDD by default; touchpoint maps on the on-demand path) include both endpoints (origin + destination features) and the trigger condition for each touchpoint
- Phase-level decisions carry rationale (TDD-traceable by default; on the on-demand path, annotation / artboard context)

#### 3A.1.4 Disposition

Three outcomes:

- **Pass** — grounding inputs are sufficient (PRD/TDD + CC DS mirror by default; design file cross-cutting sections on the on-demand path); the `ux-spec-synthesizer` proceeds to phase-level instance authoring (§3A.2)
- **Pass with annotation** — minor gaps the synthesizer annotates inline; proceeds to authoring and notes the annotation context in the phase-level instance where applicable
- **Revise grounding** — material gaps; on the default path the `ux-spec-synthesizer` re-derives from a closer read of PRD/TDD, or surfaces a genuine spec gap to the operator under the incremental-JIT spec-change authority; on the on-demand path, where the gap is in the design file's cross-cutting sections, CC re-enters the on-demand visual loop (re-pull a revised design file per [MECH] Cross-Tool Workflow Handoff §4) — a cheap CC-internal re-grounding, not a Hub-mediated CD bounce (per-feature work may still proceed via §3B if its grounding passed)

### 3A.2 Phase-level instance authoring quality check (S1 exit)

#### 3A.2.1 Coverage check

For each §2A.x category: the CC-authored phase-level instance markdown contains material on this category, or the category is explicitly marked "not applicable to this phase" with one-sentence rationale (consistent with the §3A.1.1 grounding disposition).

#### 3A.2.2 Alignment check

- Every shell / vocabulary / touchpoint reference traces to a grounding source (a PRD/TDD statement or CC DS mirror entry by default; a design file callout in the cross-cutting sections on the on-demand path)
- §2A.3 cross-feature touchpoints reference both endpoints by feature-slug; both feature-slugs appear in the phase-level header's `Per-feature instances in this phase` list
- §2A.6 cross-cutting additive index entries cross-reference the originating feature's per-feature §2B.4 entry by feature-slug + asset name; the originating feature's per-feature instance is authored (or planned to be authored) within the same S1 synthesis pass
- §2A.5 VR naming convention is internally consistent (prefix table covers every `tier_1_involved=true` feature in the phase)

#### 3A.2.3 Downstream sufficiency check

- Each §2A.x category's content is concrete enough that its downstream consumer — per the §0.3 category→consumer map — can author its artifact without inventing detail (e.g. the CC S2 acceptance/intent session authoring intent.md UX brief for slices participating in cross-feature touchpoints; phase test plan §2 cross-feature scenario classes drawing on §2A.3 touchpoints)
- The phase-level instance is self-contained for cross-cutting context: an implementing S3 session reading both the phase-level instance and the active feature's per-feature instance (without access to any design file) can ground all references in the CC DS mirror plus the two instances

#### 3A.2.4 Header completeness check

- All §1.1.2 phase-level header required fields are present and well-formed
- `app_slug`, `phase_number` match the paired TDD `app_slug`, `phase_number`
- `Per-feature instances in this phase` list matches the set of features with `tier_1_involved=true` in the paired TDD
- `DS instance version` matches the DS version recorded in the CC DS mirror at synthesis time (on the on-demand path, the version the CD design file carries)

#### 3A.2.5 Disposition

Three outcomes:

- **Pass** — phase-level instance ready to finalize in S1
- **Pass with annotation** — minor gaps inline-annotated; S1 finalization proceeds but the annotation context flows downstream
- **Revise — return to authoring** — material gaps; the `ux-spec-synthesizer` revises (the `ux-spec-cross-checker` re-reads); if gap is rooted in insufficient grounding, escalate back to §3A.1 (on the on-demand path this may re-enter the on-demand visual loop for the phase-level cross-cutting sections — a cheap CC-internal re-grounding)

## §3B Per-feature instance checks

### 3B.1 Per-feature grounding-sufficiency check (S1 entry, iterated per tier-1-involved feature)

On the default path this verifies PRD/TDD + the CC DS mirror are sufficient grounding for the feature's §2B.x categories. The design-file slice checks below are the **conditional on-demand-path branch** — they apply only when on-demand re-entry has produced a CD design file.

#### 3B.1.1 Coverage check

For each §2B.x category: the grounding inputs (the feature's PRD/TDD + CC DS mirror by default; on the on-demand path, additionally the design file's labeled slice for this feature) contain material sufficient to ground the corresponding markdown category, OR the category is explicitly marked "not applicable to this feature" with one-sentence rationale.

#### 3B.1.2 Alignment check

- Affected Tier 1 scope (from the TDD `§4.{feature-slug}` by default; visible in the design file's labeled slice on the on-demand path) matches the TDD scope it pairs with — no screens or roles outside TDD scope, no missing scope from TDD; on the on-demand path, per-feature internal labeling (frame / section / page tag = feature-slug) is present and unambiguous so the slice boundary is identifiable
- Components grounded by the synthesis are clearly named and resolve against the CC DS mirror (read via SK-F) — components not yet in the DS are captured as §2B.4 additive update plans; cross-cutting additives are also indexed in phase-level §2A.6. On the on-demand path, components CD flags as new in the slice annotations are reconciled with the same §2B.4 path. The `ux-spec-synthesizer` grounds component / token references in the CC DS mirror by default (per DSG §13.3 CC-side consumption discipline); meta-DS authoring authority remains CD's as DS owner (UNCHANGED)
- Layout pattern choices are clearly grounded (TDD-traceable by default; on the on-demand path, annotated in the slice) — deviations from the standard mapping carry rationale
- Token usage is clear enough to author into the per-feature instance (resolved against the CC DS mirror by default; against slice annotations on the on-demand path)
- Accessibility content conforms to DSG §6 stance — no formal WCAG conformance claims; engineering hygiene only

#### 3B.1.3 Grounding sufficiency check

- Per-screen interaction content (from PRD/TDD by default; depicted in the slice on the on-demand path) is concrete enough that the `ux-spec-synthesizer` can author per-feature instance §2B.3 Key interactions without inventing detail
- Accessibility content is concrete enough that the `ux-spec-synthesizer` can author per-feature instance §2B.5 without restating DSG §6 baseline
- Visual states (loading, empty, error) are grounded in PRD/TDD or "per DSG §10 defaults" (or depicted in the slice on the on-demand path) — the `ux-spec-synthesizer` can author per-feature instance §2B.7 visual regression anchors using the phase-level §2A.5 naming convention

#### 3B.1.4 Disposition

Three outcomes:

- **Pass** — grounding inputs are sufficient (PRD/TDD + CC DS mirror by default; design file slice on the on-demand path); the `ux-spec-synthesizer` proceeds to per-feature instance authoring (§3B.2) for this feature
- **Pass with annotation** — minor gaps annotated; proceeds to authoring with annotation context noted in the instance
- **Revise grounding** — material gaps; on the default path the `ux-spec-synthesizer` re-derives from a closer read of the feature's PRD/TDD, or surfaces a genuine spec gap to the operator under the incremental-JIT spec-change authority; on the on-demand path, where the gap is in this feature's slice (or its labeling), CC re-enters the on-demand visual loop for that feature per [MECH] Cross-Tool Workflow Handoff §4 (a cheap CC-internal re-grounding, not a Hub-mediated CD bounce); S1 pauses for this feature only

The per-feature instance itself, when authored, becomes the persistent record of the synthesis.

### 3B.2 Per-feature instance authoring quality check (S1 exit, iterated per tier-1-involved feature)

#### 3B.2.1 Coverage check

For each §2B.x category: the CC-authored per-feature instance markdown contains material on this category, or the category is explicitly marked "not applicable to this feature" with one-sentence rationale (consistent with the §3B.1.1 grounding disposition).

#### 3B.2.2 Alignment check

- Every component reference in §2B.3 traces to a grounding source — the CC DS mirror entry or a PRD/TDD statement by default; on the on-demand path, a component callout in the design file's slice for this feature — or to a phase-level §2A.2 shared vocabulary entry when the component is cross-feature
- Every token reference (where present) traces to a CC DS mirror token (or, on the on-demand path, a token annotation in the design file's slice)
- Every layout pattern reference in §2B.2 traces to a grounding source (TDD / CC DS mirror pattern catalog by default; a pattern annotation in the design file's slice on the on-demand path)
- §2B.4 New components or tokens entries follow [RULE] DSG §12.4 minimum change content structure; the `scope` field correctly declares feature-specific vs cross-cutting; cross-cutting entries have a matching phase-level §2A.6 index entry
- §2B.5 accessibility call-outs are feature-specific (no restatement of DSG §6 baseline)
- §2B.6 i18n call-outs are within DS instance i18n scope or trigger §2B.4 / §2A.6 additive plan
- §2B.7 visual regression anchors follow phase-level §2A.5 naming convention

#### 3B.2.3 Downstream sufficiency check

- Each §2B.x category's content is concrete enough that its downstream consumer — per the §0.3 category→consumer map — can author its artifact without inventing detail (e.g. the CC S2 acceptance/intent session authoring intent.md UX brief, test-plan.yaml `test_type: accessibility` and `test_type: visual_regression` cases when slice-level testing is required)
- The per-feature instance is self-contained for feature-scoped context: an implementing S3 session reading the per-feature instance plus the phase-level instance (without access to any design file) can ground all component / token / pattern references in the CC DS mirror (because SK-F reads the CC mirror at code time)

#### 3B.2.4 Header completeness check

- All §1.2.2 per-feature header required fields are present and well-formed
- `feature_slug`, `app_slug`, `phase_number` match the paired TDD `§4.{feature-slug}.Header`
- `Phase-level UX Design Spec ref` points to the same phase's phase-level instance when one exists
- `DS instance version` matches the DS version recorded in the CC DS mirror at synthesis time (on the on-demand path, the version the CD design file carries)

#### 3B.2.5 Disposition

Three outcomes:

- **Pass** — per-feature instance ready to finalize in S1; the instance is in-repo at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` and available to the S2 acceptance/intent session and S3 implementing session
- **Pass with annotation** — minor gaps inline-annotated; S1 finalization proceeds but the annotation context flows downstream to the S2 acceptance/intent session. A "Pass with annotation" instance signals each gap inline at the affected §2B.x category; an S2 / S3 consumer treats an inline annotation as a flagged gap to surface to the operator rather than silently fill
- **Revise — return to authoring** — material gaps; the `ux-spec-synthesizer` revises the markdown (the `ux-spec-cross-checker` re-reads); if the gap is rooted in insufficient grounding, escalate back to §3B.1 (on the on-demand path this may re-enter the on-demand visual loop for the affected feature's slice)

---

# 4. Anti-drift red flags

The Scope column tags whether the red flag applies to the phase-level instance (`phase`), the per-feature instance (`feature`), or both (`both`).

| Red flag | Scope | What it signals | Response |
|---|---|---|---|
| A per-feature UX Design Spec instance exists for a feature whose TDD `§4.{feature-slug}.Header.tier_1_involved` is `false` | feature | TDD vs UX Spec scope drift; one of the two is wrong | Reconcile TDD and UX Spec scope before proceeding; do not silently accept the spec |
| A phase-level UX Design Spec instance exists but the phase has no cross-cutting UX content (no feature has `tier_1_involved=true`) | phase | S1 authored a phase-level instance without a triggering need; TDD vs UX Spec drift | Reconcile — either confirm a feature should have `tier_1_involved=true` and update TDD, or remove the phase-level instance |
| Phase-level instance's `Per-feature instances in this phase` list does not match TDD's `tier_1_involved=true` feature set | phase | Header drift; instance set inconsistent across the phase | Update the list; verify each named per-feature instance exists at the declared path |
| Per-feature instance's `Phase-level UX Design Spec ref` is absent or points to a non-existent file (when a phase-level instance exists for the phase) | feature | Cross-reference drift; downstream consumers (CC S2 acceptance/intent / S3 implementing) cannot find cross-cutting context | Author the phase-level instance if it should exist, or fix the reference |
| A per-feature instance contains content properly belonging to phase-level scope (platform shell, shared visual vocabulary definitions, cross-feature touchpoint definitions, VR naming convention) | feature | Granularity scope drift; cross-cutting content duplicated per-feature creates synchronization burden | Move content to phase-level §2A; per-feature instance references phase-level by section id |
| A phase-level instance contains content properly belonging to per-feature scope (per-screen interaction detail, feature-specific a11y call-outs, feature-specific VR anchors, feature-specific layout pattern selection) | phase | Granularity scope drift; phase-level instance grows into per-feature detail it should not own | Move content to the relevant per-feature §2B; phase-level instance retains only cross-cutting summary |
| A UX Design Spec instance (phase or feature) covers content that DS instance would own (project-wide token taxonomy, project-wide layout pattern definitions) | both | Boundary violation between UX Spec instance and project-wide DS instance | Route to DSG additive or breaking update path; do not embed project-wide content in any UX Spec instance |
| Per-feature §2B.3 references components not in the DS instance and §2B.4 additive update plan is missing | feature | Incomplete instance; the `ux-spec-synthesizer` authored §2B.3 without grounding the new component in the CC DS mirror (or the on-demand slice) and without raising the §2B.4 additive plan | Return to S1 authoring; flag the missing §2B.4 entry; also surface a §3B.1 grounding-sufficiency failure (the component lacks a DS-mirror entry / a slice callout on the on-demand path) |
| §2B.4 entry declares `scope: cross-cutting` but no matching phase-level §2A.6 index entry exists | both | Cross-cutting additive index drift; the additive is invisible at the phase-level surface | Add the §2A.6 index entry pointing to this §2B.4 entry; verify originating-feature designation is consistent |
| §2A.6 cross-cutting additive index entry exists but the originating feature's §2B.4 entry does not | both | Phantom cross-cutting additive index; downstream consumers cannot find the plan content | Either author the originating feature's §2B.4 entry, or remove the §2A.6 index entry if the additive turned out to be feature-specific |
| §2A.3 cross-feature touchpoint references a feature that is not in the phase-level header's `Per-feature instances in this phase` list | phase | Touchpoint references a phantom feature, or the per-feature instance for that feature was not authored | Reconcile — author the missing per-feature instance, or remove the touchpoint, or update the header list |
| **S1 finalizes a UX Design Spec instance without applying §3A or §3B reviewer checks** | both | Process bypass; the §3 synthesis-quality checks (with `ux-spec-cross-checker` independent read) are the gate | Re-apply applicable checks before S1 finalization; check application is the gate, not the artifact's existence |
| **`ux-spec-cross-checker` authors / edits the UX Design Spec instance directly instead of proposing** | both | Firewall-role violation — the cross-checker is an independent reader (propose-not-author, mirroring DSG §12.1); authoring is the `ux-spec-synthesizer`'s role | Cross-checker reverts to propose-only mode; the `ux-spec-synthesizer` resolves each proposed gap |
| **`[TPL] UX Design Spec` is treated as a CD-authoring template** | both | Misuse — both instance types are CC-authored markdown spec contracts; CD does not consume this template | Reorient: on the on-demand visual path CD produces design files (CD-native visual artifacts) per [REF] Hub-CD-CC Architecture §3.4.1; this template governs the CC-authored markdown counterparts produced in the firewalled S1 session at TK-02 Step 2.3 |
| **A UX Design Spec instance (phase or feature) authored on the on-demand visual path without consulting the CD design file CC pulled back** | both | Authoring without visual grounding when a design file exists; spec content disconnected from the actual UI design. (On the default path there is no design file; grounding is PRD/TDD + CC DS mirror, and this red flag does not apply) | Re-ground the synthesis against the pulled-back design file's cross-cutting sections (phase) or feature's labeled slice (feature) |
| **S2 intent.md UX brief invents content not present in the upstream UX Design Spec instances** (phase-level or per-feature) | both | Downstream authoring drift; the S2 acceptance/intent session must extract from upstream, not invent | Return to the S2 conversion; if the relevant UX Design Spec instance is genuinely silent on a needed UX point, re-author it in S1 — a cheap CC-internal cross-session loop (S2 → S1); on the on-demand path, re-enter the on-demand visual loop only if the design file also lacks the content |
| **Reference to retired path `apps/{app-slug}/specs/ux-bundles/{feature-slug}/` in any spec artifact** | both | Stale reference; the new paths are `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` and `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Update the reference to the new path(s); verify no other spec artifacts carry the stale path |
| **Operator commits on-demand CD design file exports to the monorepo as `specs/ux-design-spec/phase-{N}.md` or `specs/ux-design-spec/{feature-slug}.md`** | both | Path confusion — the design file is a CD-native visual artifact; the `.md` paths are reserved for the CC-authored markdown spec instances | Move design file exports to `apps/{app-slug}/design-references/phase-{N}/` (phase-scoped because the on-demand design file itself is phase-level) or to operator-side storage; ensure the `.md` paths carry only CC-authored markdown |
| **Operator commits on-demand CD design file exports under a `{feature-slug}/` directory** (e.g., `apps/{app-slug}/design-references/{feature-slug}/`) | both | Path-granularity mismatch — the on-demand design file is phase-level (one file per phase covering the tier-1-involved features that triggered visual re-entry); per-feature scope is captured by CD's internal labeling within the file, not by the path | Move exports to the phase-scoped path `apps/{app-slug}/design-references/phase-{N}/`; the per-feature anchor lives inside the design file (frame / section / page tag = feature-slug) and is cited in the per-feature instance's `Source material` header field |

---

# 5. Maintenance discipline

This template is maintained at the slim content-contract level. When content categories (§2A.1–§2A.6 or §2B.1–§2B.8) are added, removed, or re-scoped, the change is reviewed against the paired and related sources declared in this template's header `Relationship to …` fields and `Pairings I participate in`, reconciled against the authoritative pairing register in [OS] §8.5.2.

When new DSG governance affects the synthesis grounding (the default PRD/TDD + CC DS mirror path, or the conditional on-demand design-file path) or the export conformance review (e.g., a change to §13.3 CC-side consumption discipline), the §3A and §3B synthesis-quality checks may need extension to verify the new rule's application.

The phase-level / per-feature granularity split is a structural feature of this template. If a future structural change consolidates the two instance types into one, or further splits them (e.g., app-level instance for shell), the change is itself a structural revision triggering re-verification of P-28 and P-29 (since the §2 organization is the pairing trigger).
