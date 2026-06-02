# [RULE] Design System Governance

- **Project**: HR Digital Cockpit
- **Document Type**: Architecture Specification
- **Status**: Active canonical
- **Role**: Stable governance-rules source defining the design-system framework that constrains all Tier 1 frontend work across the project — design language foundation rules, token taxonomy and consumption discipline, component inventory tiering, layout-pattern governance, accessibility stance, internationalization approach, motion hygiene, iconography rules, content style norms, platform-tier framework, change-process governance, custom-skill integration contract, pairing rules with adjacent canonical sources, reviewer checklist, and anti-drift red flags. The DS instance content itself (tokens, component inventories, layout pattern catalog, etc.) is the source-of-truth in Claude Design (CD-internal); CC carries a read-only code-time mirror at `specs/design-system.md` for code generation, per the two-way distribution model in §1.1. Hub holds no DS instance copy — it holds the governance rules (this source) and consumes CD-authored design files at spec-authoring time.
- **Source Category**: Cat 4
- **Management-System Role**: Governance specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact. The instance it governs is a project-level singleton specification output, not a per-feature artifact.
- **Relationship to [OS]**: Serves the Specify loop by establishing the design-system governance framework that downstream specification artifacts (PRD, TDD, intent, acceptance, UX Design Spec instances at phase-level and per-feature granularities) must respect; subject to [OS] §8.5 paired-update consistency. Grounded in [OS] §0.1 project-level operating premises and [OS] §0.2 Cat 4 role anchor.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §3 (global core with governed local variance — Arco Design as global core for HDC's Tier 1 visual layer, regional i18n and RTL as governed variance), §5 (management mechanism over ad hoc control — this governance is the mechanism preventing per-slice visual drift), §6 (operation management and value realization by design — accessibility hygiene and i18n are operation realities captured upfront), §10 (MECE — component inventory)
- **Relationship to [PRIN] People Experience Design Principles**: This rule is the primary implementation carrier for People Experience principles when the topic lens is experience quality and consistency; the dual-platform (PC + mobile) coverage in §11 directly serves People Experience moments-of-truth that occur outside the desktop
- **Relationship to [REF] Hub-CD-CC Architecture**: This rule's SOT-distribution declarations in §1.1 align to §5.2 two-way distribution model (CD = SOT / CC = code-time mirror). CD is the instance SOT; CC carries a read-only mirror at `specs/design-system.md` for code-time consumption. Hub holds no DS instance copy; at TK-02 step 2.3 Hub Claude consumes CD-authored design files (not a DS mirror) per §13.3. When the architecture's distribution model changes substantively, §1.1 of this rule is re-verified.
- **Relationship to [RULE] Claude Code Architecture Rules**: Constrains Tier 1 (React) work exclusively; Tier 2 and Tier 3 are out of scope. The CC mirror of the DS instance is a project-level singleton at the monorepo root, not under any `apps/{app-slug}/` directory; downstream feature artifacts that reference it (per-feature UX Design Spec instances authored in Hub per `[TPL] UX Design Spec`, intent.md UX brief, test-plan.yaml accessibility cases) are app-scoped under `apps/{app-slug}/specs/...`. The repository-layout and code-scope substantive detail (the monorepo-root placement rule and the `business_rules_only` scope allow list that includes the CC mirror as `specs/design-system.md`) is owned by the CC-side substantive Claude Code Architecture Rules canonical.
- **Relationship to [MECH] Development Track Workflow**: The DS instance and the CC mirror are established at workspace inception per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance) via initial CD authoring + DS markdown export to the CC mirror location (after the §15 export review per §12). TK-02 step 2.3 consumes CD-authored design files — design file quality checks (phase-level cross-cutting check + per-feature slice check; both spec-readiness) + UX Design Spec authoring at two granularities (phase-level + per-feature) grounded in the design files — per §13.3. CC mirror is referenced by TK-04 (M0 entry, per-slice spec consumption) and TK-05+ (code writing, M3 visual review). Additive updates to the instance authored in CD propagate to the CC mirror via the §12 sync mechanism in this rule.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2 (Hub ↔ CD path) carries DS-related discussions, DSG governance text into CD as a read-only input for DS instance authoring (per §12.1), CD-authored design files transferred to Hub for TK-02 step 2.3 consumption, and the CD-generated DS markdown export transferred to Hub for the §15 export conformance review; §3 (Hub ↔ CC path) carries DSG governance text into CC and transfers the reviewed DS markdown export to the CC mirror; §4 (CD ↔ CC path, decoupled-by-default during research preview) is currently not directly used for DS sync (the CC mirror receives DS markdown via operator-mediated transfer from CD through the Hub review session). The export-review cadence and triggers are owned by §12 of this rule.
- **Relationship to [MECH] Code Quality Rule Set**: **CQ migrated to CC substantive canonical (Phase 3)**. CC substantive Code Quality Rule Set canonical declares the runtime and build-time tool-level enforcement of Tier 1 visual rules; this rule declares the design-level rules that those tools enforce. Token-consumption rules in §4 and component-inventory rules in §5 are implemented as ESLint rules and dependency-cruiser rules per CC substantive CQ canonical. Hub↔CC coordination is governed by the decoupled-reference model in [REF] Hub-CD-CC Architecture §5.4.4.
- **Relationship to adjacent [TPL] sources**:
  - Upstream of `[TPL] UX Design Spec` — DSG governs the design rules; UX Design Spec instances declare UX coverage at two granularities (phase-level for cross-cutting content + per-feature for feature-scoped content) Hub-authored from CD design files per [TPL] UX Design Spec §0; UX Design Spec component selections and any new-component / new-token plans MUST respect DSG inventory and §12 change flow (single-feature additive plans live in per-feature instance §2B.4; cross-cutting additives index in phase-level instance §2A.6 with the originating feature's §2B.4 holding the authoritative plan content; the cross-cutting vs feature-specific boundary those sections implement is defined by §5.2.4 reuse-scope criterion, paired with [TPL] UX Design Spec §2A.6 / §2B.4 as P-54)
  - Upstream of `[TPL] Intent and Acceptance Interface Writing Standard` (intent.md UX brief section authors components and a11y references that MUST respect DSG inventory + §6 stance)
  - Upstream of `[TPL] Test Plan YAML Schema` (accessibility test type cases)
- **Relationship to custom skills**:
  - Consumed at Claude Code runtime by `hdc-arco-enterprise-ui` skill during Tier 1 code generation, by reading the CC mirror at `specs/design-system.md`
  - Consumed at Claude Code runtime by `hdc-wcag-accessibility-checker` skill **on operator demand only** (per §6.3); not auto-invoked
  - Consumed at Hub Claude runtime in TK-02 step 2.3 — Hub Claude grounds in CD-authored design files (Hub holds no DS mirror); the Hub-side consumption discipline is described in §13.3
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: When DS instance content is uploaded to DingTalk Docs for stakeholder visibility, apply that rule (uploading happens from CD source or the CC mirror, not authored at Hub)
- **Pairings I participate in**: P-19 (with `hdc-arco-enterprise-ui` + `hdc-wcag-accessibility-checker` SKILL.md). P-54 (with `[TPL] UX Design Spec` §2A.6 / §2B.4 — the §5.2.4 reuse-scope criterion governs the cross-cutting vs feature-specific classification those instance sections implement; a change to the criterion, or to those sections' classification semantics, re-verifies the other within the same period). P-34 (was: with [MECH] Code Quality Rule Set lint rules) **RETIRED in Phase 3** per [REF] Hub-CD-CC §5.4.4 — counterparty CQ fully migrated to CC substantive canonical; alignment with DSG design-level rules now governed at CC's discretion.

## How to use this source

Use this source when:
- Initializing a new HR Digital Cockpit workstream and the design-system governance framework needs to be applied (CD instance is created; the CC mirror at `specs/design-system.md` is established at workspace inception via CD-generated DS markdown export, reviewed against §15 per §12)
- Introducing a new component, token, or layout pattern that will be reused across slices (governance flow per §12)
- Elevating a locally-invented pattern from one slice into a shared asset
- Reviewing whether a Tier 1 implementation respects the project design system
- Updating accessibility hygiene rules or internationalization scope
- Authoring a UX Design Spec instance at TK-02 step 2.3 — phase-level (Hub-authored markdown synthesizing the design file's cross-cutting sections) or per-feature (Hub-authored markdown synthesizing each feature's labeled slice); this rule declares the governance baseline for what design content the instances must respect
- Performing design file quality checks at TK-02 step 2.3 — phase-level check on cross-cutting sections + per-feature check on each labeled slice; Hub Claude verifies CD-authored design files are spec-ready — complete against PRD/TDD scope, internally consistent, annotations rich enough to author the UX Design Spec instances from — per §13.3

Do not use this source as:
- The DS content itself (content is authored in CD as instance SOT; the CC mirror at `specs/design-system.md` is read-only and not directly edited)
- A per-feature or per-slice artifact (the rule is project-level, not feature-level)
- A substitute for the Arco Design official guidelines (this rule adapts and anchors, not replaces)
- A full design system implementation library (the rule captures governance and pointers, not component source code)
- A visual mockup repository (no mockups live here; visual mockups are CD-internal artifacts — specifically, CD-authored design files per [REF] Hub-CD-CC Architecture §3.4.1 — and are not canonical at the Hub layer)

---

---

# 1. Scope and boundary

## 1.1 Singleton instance model and two-way distribution

The DS instance is a **project-level singleton**, not a per-app or per-feature artifact. The instance is created **once at workspace inception** and updated as governed by §12.

Two-way distribution model (per [REF] Hub-CD-CC Architecture §5.2):

| Location | Role | Update mechanism |
|---|---|---|
| **CD (Claude Design)** | **Authoritative SOT** — the authoritative DS instance content; CD-native format | CD authors changes via §12 flow; CD is where instance content originates and where breaking changes are decided; CD generates the DS markdown export at every change finalization for the §15 review and CC-mirror sync (per §12.7) |
| **CC monorepo** at `specs/design-system.md` | **Code-time mirror** — read-only derived from CD SOT via the reviewed CD-generated DS markdown export; consumed by `hdc-arco-enterprise-ui` skill at code generation time | Synced from the DS markdown export — after the §15 export conformance review per §12.3 — at every §12 change finalization (additive: at originating feature's M4 → merge-to-main; breaking: after CD-side breaking change is finalized at the separate review gate); operator-mediated transfer per [MECH] Cross-Tool Workflow Handoff |
| **[RULE] DSG** at Hub PK (this source) | **Governance rules** — topic-level rules that govern DS evolution; not instance content. Hub holds DSG but no DS instance copy. DSG is transferred to CD as a read-only input for DS instance authoring (per §12.1) | Authored at Hub under [MECH] Canonical File Self-Audit governance |

At spec-authoring time (TK-02 step 2.3) Hub Claude consumes CD-authored design files, not a DS instance copy; the export conformance review (§12.3) is the Hub-side touchpoint with DS instance content, performed transiently on the export rather than via a persisted mirror.

Update categories:
- **Additive updates** (new component added, new token added, i18n scope expanded, new layout pattern added): authored in CD per a feature's UX needs (the additive plan is captured as the corresponding feature's per-feature UX Design Spec instance §2B.4 New-Components-Or-Tokens entry, Hub-authored at TK-02 step 2.3). Once approved per §12, CD finalizes the change; CD regenerates the DS markdown export; the export is reviewed Hub-side against §15 per §12.3; on a passing review the **CC mirror** (`specs/design-system.md`) is re-synced, typically at the feature's merge-to-main milestone (see [MECH] Development Track Workflow TK-12 M4 gate).
- **Breaking updates** (token value change, Arco major version upgrade, accessibility hygiene rule change, mobile-tier change): require explicit review gate per §12.2; back-propagate to all affected slices; the CC mirror is re-synced after the CD-side breaking change is finalized and the export passes the §15 review.

There is one instance per project (HDC has exactly one DS instance covering all apps). The instance is shared across all apps, all phases, all features. There is one DS markdown export per instance version, transferred to the CC mirror after the §15 export conformance review.

## 1.2 Boundary with feature-level artifacts

| Artifact | Location | Scope | Contains |
|---|---|---|---|
| DS instance (SOT in CD; CC mirror at `specs/design-system.md`) | CD + CC | Project-level | Design language choice, tokens, component inventory, a11y hygiene rules, i18n scope, motion guidelines, mobile/PC platform split |
| CD-authored design file (per phase, when any feature in the phase has tier_1_involved=true) | CD workspace; transferred to Hub at TK-02 step 2.2 → 2.3; transferred to CC at TK-04 as visual reference | Phase-level (cross-cutting sections + per-feature internally labeled scopes so Hub Step 2.3 can ground phase-level and per-feature UX Design Spec instances respectively) | One CD-native design file per phase: hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations; cross-cutting sections (shell / shared vocabulary / cross-feature touchpoint maps / phase-level decisions / VR naming convention) plus per-feature labeling (frame / section / page tag = feature-slug); covers [TPL] UX Design Spec §2A categories at the phase scope + §2B categories per tier-1-involved feature in CD-native form |
| **Phase-level UX Design Spec instance per `[TPL] UX Design Spec` (Hub-authored markdown at TK-02 step 2.3 from CD design file's cross-cutting sections)** | Hub-authored at `apps/{app-slug}/specs/ux-design-spec/phase-{N}.md` | Phase-level | Platform shell + IA + personas, shared visual vocabulary, cross-feature touchpoints, phase-level horizontal design decisions, visual regression naming convention, cross-cutting new components/tokens additive index; written in markdown for AI-RAG consumption |
| **Per-feature UX Design Spec instance per `[TPL] UX Design Spec` (Hub-authored markdown at TK-02 step 2.3 from the corresponding labeled slice of the CD design file)** | Hub-authored at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Feature-level | Affected Tier 1 scope, components from DS instance referenced by this feature, new components introduced (with §12 update plan; scope: feature-specific or cross-cutting first-owner), feature-specific a11y notes, mobile/PC scope; written in markdown for AI-RAG consumption |
| `apps/{app-slug}/specs/intent/{slice-id}.md` UX brief section | Hub-authored at TK-03 (consumes UX Design Spec instance + design files as visual reference); transferred to CC | Slice-level | Screen list, interaction highlights, i18n/a11y call-outs specific to the slice |
| `apps/{app-slug}/specs/acceptance/{slice-id}.yaml` | Hub-authored at TK-03; transferred to CC | Slice-level | Machine-readable acceptance scenarios including a11y expectations |
| `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` | Hub-authored at TK-03; transferred to CC | Slice-level | Test cases including `test_type: accessibility` |

If content belongs in feature-level artifacts, do not duplicate it into the DS instance. The instance holds project-wide decisions only.

**Path discipline note**: The CC DS mirror is a project-level singleton at the CC-monorepo root `specs/design-system.md` (not under any `apps/{app-slug}/` directory because the design system is shared across all apps). All feature-scoped artifacts referenced above use the `apps/{app-slug}/` prefix; the authoritative repository-layout detail is owned by the CC-side substantive Claude Code Architecture Rules canonical.

## 1.3 Cross-canonical-source boundary

The instance captures project-level design foundation and authoritative lists (tokens, components, layout-pattern mapping, a11y hygiene, i18n scope) and nothing that belongs in an adjacent canonical source: per-feature UX decisions live in UX Design Spec instances; per-slice UX briefs live in intent.md; business logic and feature user value live in the PRD; implementation-level React code lives in code; tool-level lint and architecture-rule enforcement is owned by the CC substantive Code Quality Rule Set canonical.

## 1.4 Feature-agnostic canonical instance (no reverse pointers)

The DS instance MUST be **feature-agnostic**. Instance content (all IT sections + the DS markdown export) MUST NOT contain reverse pointers to the application features / slices / cases it serves: no feature-slug, slice-id, milestone (Mn) reference, or case / issue / decision identifier, and no naming of feature-specific components inside cross-cutting entries. Component reuse is expressed by **design role and reuse-scope topology** (cross-cutting vs feature-specific per Rule 5.2.4), never by enumerating consumers. Per Rule 5.2.4, feature-specific Tier B components are not inventoried in the instance at all — they live in their per-feature UX Design Spec instance §2B.4.

This is the content-level dual of §1.1's distribution rule: just as **Hub holds no DS instance copy**, the **instance holds no downstream feature pointer**. The instance absorbs application-execution feedback to evolve; the context that drove a change (which slices, which cases, as-built reconciliations) lives only in the CD-side change records (per §12.4 change content) and the per-feature UX Design Spec instances — not in the canonical source.

**Not** reverse pointers (allowed in the instance): generic domain / scenario vocabulary (e.g. "employee roster", "approval drawer", "version header"); the instance's own change-ids (IT14) as iteration identifiers and the key into the change records; governance section references (§2A.6 / §2B.4 as concepts, not as "feature-X §2B.4"); design-decision provenance (ratification dates).

---

# 2. Instance section contract

The DS instance must contain coverage for the following section topics. The specific content of each section lives in the instance (in CD as SOT, mirrored to CC); this rule declares only **what topics must be covered**, not what the content must say.

Required instance section topics. Instance topics are labelled `IT1 … IT14` to keep them distinct from this rule's own chapter numbers (`§1 … §16`) — a bare `§N` always refers to a DSG chapter, never an instance topic.

- **IT1 — Design language foundation** — base design system reference and rationale
- **IT2 — Implementation path** — PC implementation, mobile implementation, cross-platform consistency
- **IT3 — Design tokens** — color tokens (Arco semantic overrides + HDC custom accents + HR-specific semantic states), text/background tokens, typography tokens, corporate font stack, spacing tokens, border radius / elevation / other visual tokens, sizing/density tokens, token consumption rules; per-token lifecycle state (`active` / `deprecated` / `removed`) with successor where deprecated
- **IT4 — Component inventory** — Tier A (Arco used directly), Tier B (HDC custom), Tier C (forbidden); cross-platform mapping
- **IT5 — HDC layout patterns to HR scenario mapping** — PC patterns, mobile patterns, cross-platform pattern mapping
- **IT6 — Accessibility stance** — the instance carries a pointer to this rule's §6, not a restated summary
- **IT7 — Internationalization and RTL** — locale coverage and RTL approach
- **IT8 — Motion and animation** — motion principles, `prefers-reduced-motion` handling
- **IT9 — Iconography** — primary icon source, custom icon policy, a11y for icons
- **IT10 — Content style guide** — date / time formats, empty / error patterns, button verbs, terminology, capitalization, mobile copy compaction
- **IT11 — Responsive behavior and platform tiers** — breakpoints, mobile-as-first-class declaration, T1/T2/T3 platform tier framework
- **IT12 — Governance** — change process; the instance carries a pointer to this rule's §12, not a restated summary
- **IT13 — Custom skill integration** — which skills consume the instance and how
- **IT14 — Change log** — chronological log of approved instance changes

There is no leveled instance; this is per-project and single-level.

**Required instance header fields**:
- Schema version (matches this governance rule's revision)
- Instance version (semver)
- Status (`Draft` / `Active` / `Superseded`)
- Created date, last updated date
- Owner
- Design language foundation declaration
- Accessibility stance — a pointer to DSG §6; the instance references the §6 stance, it does not restate it
- Change log location (in-file instance topic IT14 or external reference)
- **DS markdown export reference** — declared path or commit reference for the current export that populated the CC mirror; ensures mirror version traceability per §12.7

---

# 3. Implementation path rules

Governance over the implementation path is twofold:

**Rule 3.1 — Theme injection mechanism**: The corporate VI (visual identity) overrides MUST be applied at build time via Arco's `less-loader` `modifyVars` mechanism, not at runtime via imported CSS files. Runtime CSS overrides defeat tree-shaking, complicate dark-mode extension, and break the single-source-of-truth principle.

**Rule 3.2 — Single monorepo theme source**: There MUST be exactly one theme source for the project at `packages/hdc-corporate-theme/`. Per-app theme duplication (separate `hdc-corporate-theme.css` or `theme.less` files inside `apps/{app-slug}/src/frontend/themes/`) is forbidden.

**Rule 3.3 — No `@arco-themes/...` npm dependency**: The project deliberately avoids the `@arco-themes/...` npm package distribution mechanism — an external package boundary adds version-pinning and supply-chain surface the project does not need for theme delivery.

**Rule 3.4 — PC + mobile library version pinning**: The instance MUST pin both `@arco-design/web-react` (PC) and `@arco-design/mobile-react` (mobile) to declared versions. Cross-app version drift is forbidden.

**Rule 3.5 — Custom component policy**: Components not in Arco standard are allowed only when (a) Arco does not provide a sufficient base, AND (b) the custom component is registered in the instance §4 component inventory as Tier B with a documented rationale.

**Rule 3.6 — External dependency factual verification**: Every DS instance statement about external packages and tooling — package identity, declared version, license, repository URL, official documentation URL, theme API surface, import pattern, browser support — MUST be verified against the project lockfile and the package's official source (repository, registry metadata, official docs) before becoming canonical. The DS instance records `verified_at`, `verified_source`, and `verification_owner` per fact (or per fact-group when several facts share a source). License statements and other legally-loaded fields require legal-review sign-off in addition to source verification. When public sources conflict, the DS records the conflict and marks the field `pending verification` rather than asserting an unverified value. The verification scope covers Tier 1 PC/mobile libraries (§3.4), iconography sources (§9.1), and any other external-package reference appearing in the DS instance.

**Rule 3.7 — Theme-variance readiness**: The token system and the single monorepo theme source (Rule 3.2) MUST NOT be authored so as to foreclose a future governed theme variance — at minimum the active corporate light theme today, with an alternate (dark, or a future regional variant) addable as a **governed additive variance** rather than a token-system rebuild. Dark mode is **not currently active**; this is a forward declaration paralleling the §7.2 RTL-capability stance. The concrete delivery mechanism for an alternate theme (an additional build-time `modifyVars` variant, a runtime attribute / CSS-variable switch layered on the Rule 3.1 build-time corporate palette, or a combination) is **not fixed by this rule** — it is decided when the variant is actually scoped, with the chosen mechanism's API surface verified per Rule 3.6 and reconciled with the Rule 3.1 build-time-override stance at that point. The standing readiness obligation falls on token *authoring* (Rule 4.2.6), which is mechanism-agnostic.

The specific theme values, version pins, and custom component list live in the instance (CD as SOT; the CC mirror carries the same content).

---

# 4. Design token governance

## 4.1 Token taxonomy

The instance MUST organize tokens into the following taxonomies. The taxonomies themselves are governance; the values are instance content.

- **Arco semantic overrides** — colors that override Arco's defaults to match corporate VI (e.g., `primary`, `success`, `warning`, `danger`)
- **HDC custom accents** — colors not in Arco's semantic set but specific to HDC contexts (e.g., process-step state colors, lineage edge colors)
- **HR-specific semantic states** — colors that encode HR domain meaning (e.g., approval-status colors, ownership-binding state colors)
- **Text and background tokens** — text foreground colors, surface backgrounds, container hierarchies
- **Typography tokens** — font sizes, line heights, font weights; aligned with Arco scale
- **Corporate font stack** — primary font family declaration with fallback chain
- **Spacing tokens** — Arco-aligned spacing scale
- **Border radius, elevation, and other visual tokens** — shadow, radius, opacity scales
- **Sizing and density tokens** — control heights, minimum touch-target dimensions, and density-scale steps (`compact` / `standard` / `comfortable`). These back the §11.3 mobile-parity commitment (touch targets are a first-class mobile concern, not a derived PC value) and the §11.2 Tier-3 dense-data-grid screens, so interactive-control sizing is token-driven rather than hardcoded per slice. Arco's PC/mobile component defaults are the floor; the instance declares HDC overrides where corporate density or HR-scenario need diverges.

## 4.2 Token consumption rules

**Rule 4.2.1**: All Tier 1 React code MUST consume tokens through Arco's theme system and corporate VI override. Hardcoded color, typography, or spacing values are forbidden outside Tailwind layout utilities (margin, padding, flex, grid layout-only).

**Rule 4.2.2**: Token names MUST follow the taxonomy in §4.1. Adding a new top-level token category requires governance review per §12 (breaking change).

**Rule 4.2.3**: New tokens within an existing category may be added via the §12 additive update flow.

**Rule 4.2.4**: Token values that diverge from Arco defaults MUST be motivated by corporate VI or HR-specific design need; recorded in the instance with rationale.

**Rule 4.2.5**: Enforcement is via ESLint rules and Tailwind config in CC substantive Code Quality Rule Set canonical; this rule declares the design-level rules, Code Quality Rule Set declares the tool-level enforcement.

**Rule 4.2.6 — Theme-variant token authoring**: Color and elevation tokens MUST be authorable as theme-variant pairs (the light value now; an alternate-theme value addable later) without changing token names or the §4.1 taxonomy. A token whose definition hardcodes a single theme's value in a way that blocks a paired alternate value violates the Rule 3.7 readiness requirement.

## 4.3 Token lifecycle and deprecation

Tokens follow a governed lifecycle that parallels the component tier transitions in §5.4, so a token can be retired without forcing every consumer through a single breaking value-change event.

**Rule 4.3.1 — Lifecycle states**: Every token is in one of `active`, `deprecated`, or `removed`. A newly added token enters `active` via the §12 additive flow (Rule 4.2.3).

**Rule 4.3.2 — Deprecation requires a live successor**: A token MAY move `active → deprecated` only when its replacement token (or an explicit "no replacement — stop using" decision) is already `active` in the instance — mirroring the §5.4 Tier B→C rule that the successor must already exist. The deprecation records the successor token name (or the no-replacement decision) and the rationale in the instance (IT3) and change log (IT14).

**Rule 4.3.3 — Aliasing during transition**: A `deprecated` token SHOULD resolve to its successor's value (alias) for the transition window, so not-yet-migrated slices continue to render correctly. Introducing the alias is an **additive** change (the successor's value semantics do not change) and does not by itself require breaking back-propagation.

**Rule 4.3.4 — Removal is breaking**: Moving `deprecated → removed` (deleting the token from the instance) is a **breaking** change per §12.2 and requires the §12.4 backward-compatibility analysis to confirm no merged slice still references the removed token. Removal MUST NOT occur while any merged slice still consumes the token.

**Rule 4.3.5 — Rename = add successor + deprecate + (later) remove**: A token rename is never an in-place name/value edit. It is modeled as add-successor (additive) → deprecate-old with alias (additive) → remove-old (breaking, after migration). This keeps every step's blast radius governed rather than collapsing a rename into one breaking event.

---

# 5. Component governance

## 5.1 Tier A — Arco components used directly

Components imported from `@arco-design/web-react` (PC) or `@arco-design/mobile-react` (mobile) and used without wrapping or modification (except for token-driven theming).

**Rule 5.1.1**: Tier A components MUST be listed in the instance §4 component inventory with their canonical import path and PC/mobile cross-platform variant declaration.

**Rule 5.1.2**: Tier A components MAY be styled only via the token system (§4) and Arco's documented prop API. Custom CSS overrides on Tier A components are forbidden.

## 5.2 Tier B — HDC custom components

Components built on top of Arco primitives + tokens, specific to HDC's HR domain.

**Rule 5.2.1**: A component qualifies for Tier B only when: (a) it composes Arco primitives + tokens (does NOT use non-Arco third-party UI libraries), AND (b) it encapsulates an HR-specific behavior or visual pattern that recurs — used (or planned for use) in **≥2 slices**, or anticipated by a feature's UX Design Spec instance to recur, AND (c) it is registered **per its reuse scope (Rule 5.2.4)** with documented composition + props + a11y notes — a **cross-cutting** Tier B in the DS instance §4 component inventory (and indexed in the phase-level UX Design Spec §2A.6); a **feature-specific** Tier B in the originating feature's per-feature UX Design Spec instance §2B.4 (not given a DS instance §4 entry).

Qualification (b) examples — compliant: an `ApprovalStatusTag` that renders the HR approval-status colors and label set is used by the leave-request, expense, and onboarding slices, so it recurs across ≥2 slices and qualifies. Non-compliant: a one-off banner styled for a single slice's empty state, used nowhere else and not anticipated to recur — it stays slice-local code, not a Tier B component.

**Rule 5.2.2**: Each Tier B component MUST declare its PC + mobile variant policy (PC-only, mobile-only, or both with stated platform-specific differences if any).

**Rule 5.2.3**: A new Tier B component goes through the §12 additive update flow before being used in slice code.

**Rule 5.2.4 — Reuse-scope sub-classification (cross-cutting vs feature-specific)**: Every Tier B component is additionally classified by reuse scope. Rule 5.2.1(b)'s "recurs in ≥2 slices" test decides Tier-B-hood (custom, not slice-local throwaway); this rule decides whether a qualifying Tier B is **cross-cutting** or **feature-specific**:

- **Cross-cutting** — directly instantiated as a peer by slices of **≥2 distinct features with no single owning feature mediating the reuse**. Registered in the DS instance §4 component inventory **and** indexed in the phase-level UX Design Spec instance §2A.6 cross-cutting additive index (with the originating feature's §2B.4 holding the authoritative plan content per §12.4).
- **Feature-specific** — has a **single owning feature**. Documented in that feature's per-feature UX Design Spec instance §2B.4; **not** given a DS instance §4 inventory entry — **including** when the component is surfaced in a second feature only through a **declared structural seam** rather than independent peer instantiation. A *declared structural seam* is a composition contract in which the host feature receives the component through a slot / injection point owned by a cross-cutting floorplan contract, rather than independently instantiating the component as a peer. The recognized seam is the **`ObjectPage` facet-body injection** contract (a feature injects its own facet body into another feature's `ObjectPage` floorplan); this enumeration is **non-exhaustive** — additional seams are admitted through the §12 governance flow, each judged against the general criterion stated in this paragraph.

Reserving cross-cutting status (DS instance §4 + phase §2A.6) for genuine no-single-owner components keeps the project-level surface that a §12.2 breaking change must back-propagate to *all* consumers as small as the topology warrants. This reuse-scope criterion is paired with `[TPL] UX Design Spec` §2A.6 / §2B.4 (P-54 in [OS] §8.5.2): the criterion here governs the classification those instance sections implement.

**Rule 5.2.5 — Contract-change governance follows reuse scope**: A backward-incompatible change to a **cross-cutting** Tier B component's props or data contract (the kind registered in the DS instance §4 inventory and indexed in the phase-level §2A.6) is a **breaking DS change** per §12.2 and back-propagates to every consuming slice. A **feature-specific** Tier B (single owner, documented only in its feature's §2B.4 per Rule 5.2.4) is governed **within its owning feature** and does NOT trigger the DS §12.2 gate — unless and until it is promoted to cross-cutting, at which point its contract becomes subject to this rule. This keeps the project-level breaking surface as small as the §5.2.4 topology warrants (consistent with the Rule 5.2.4 rationale).

## 5.3 Tier C — Discouraged / forbidden

**Rule 5.3.1**: The following are forbidden in Tier 1 code:
- Non-Arco third-party UI libraries: Material-UI, Ant Design (the parent of Arco, but a separate library), shadcn/ui, Mantine, Chakra UI, any other component library
- WeChat / DingTalk Mini Program component libraries
- Components in slice code that duplicate existing Arco components (use the Arco component instead)
- Components that hardcode visual values outside tokens

**Rule 5.3.2**: The instance §4 component inventory MUST list Tier C explicitly so that violations are auditable.

## 5.4 Tier promotion / demotion

- **Tier A → Tier B promotion** does not apply (Arco components are Tier A by definition)
- **Tier B → Tier A**: not applicable (HDC custom does not become Arco standard)
- **Tier B → Tier C**: when an HDC custom component is deprecated, it moves to Tier C with a stated successor (which must already exist)
- **New Tier B**: §12 additive flow

## 5.5 Cross-platform consistency

Every Tier A and Tier B component listed in the instance §4 inventory MUST declare its platform coverage (PC, mobile, or both). If declared for both, any platform-specific behavior difference MUST be stated.

---

# 6. Accessibility stance

HDC has **no formal WCAG conformance target**. The stance is engineering hygiene rules only, enforced via Arco component defaults and `eslint-plugin-jsx-a11y` at `warn` severity (per CC substantive Code Quality Rule Set canonical). On-demand validation via `hdc-wcag-accessibility-checker` skill is operator-triggered, not automated.

## 6.1 Recommended engineering practices

1. All meaningful interactive elements expose accessible names — Arco defaults handle most cases; custom Tier B components MUST explicitly declare `aria-label` or equivalent semantic markup
2. Decorative-only icons carry `aria-hidden="true"` (or are inserted as CSS background, not as inline SVG)
3. Focus state is visible for all interactive elements — Arco defaults handle this; custom focus styling via tokens must preserve a visible focus ring
4. Color is not the sole signaling channel — semantic state must also carry a non-color cue (icon, text label, pattern)
5. Form fields associate labels via standard `<label for>` or Arco `<Form.Item>` prop; placeholder is NOT used as the only label
6. Tab order follows visual reading order; custom interactive components define `tabIndex` only when default tab order is broken
7. Custom Tier B components that override default keyboard behavior (drag-and-drop, custom graph editors, multi-pane interactions) MUST provide a keyboard alternative for the same action

## 6.2 What is explicitly NOT required

- No formal WCAG 2.0 / 2.1 / 2.2 conformance level targeted (no AA / AAA claim)
- No automated a11y CI gate that blocks merge (lint warnings do not block; this is by design)
- No mandatory `axe-core` run on every slice; SK-W (a11y diagnostic skill) is opt-in
- No required screen-reader walkthrough for every slice; only when a feature's UX Design Spec instance explicitly flags an a11y concern beyond Arco defaults (per `[TPL] UX Design Spec` §2.5)
- No required contrast ratio measurement beyond what Arco's theme system already enforces via tokens

## 6.3 On-demand sanity check

When a feature's per-feature UX Design Spec instance §2B.5 flags a specific a11y concern (custom Tier B with non-standard interactions, complex flow that needs keyboard-only verification, screen with dense interactive content), the operator MAY invoke `hdc-wcag-accessibility-checker` skill manually. The skill wraps `axe-core` and produces a non-binding diagnostic report; findings are advisory.

The skill is NOT invoked at any milestone gate automatically. It is a utility, not a CI step.

## 6.4 Rationale for the stance

HR Digital Cockpit's user base is the internal workforce (employees, managers, HR/IT admin); the audience is known and reachable. The cost of pursuing formal WCAG conformance (audit overhead, certification cycles, edge-case retrofits for content the audience does not consume) is high relative to the benefit. Engineering hygiene via Arco defaults + jsx-a11y `warn` catches the vast majority of real accessibility issues without imposing certification burden.

This is a deliberate design choice, not a deferral. If regulatory or contractual requirements change (e.g., expansion to public-facing surfaces or jurisdictions with mandatory WCAG compliance), this section is the trigger for a breaking governance change per §12.

---

# 7. Internationalization & RTL governance

**Rule 7.1**: The instance MUST declare its launch-language set and locale codes (BCP 47).

**Rule 7.2**: RTL capability MUST be declared in the instance regardless of whether any launch language is RTL, so that future RTL additions do not require breaking governance changes.

**Rule 7.3**: All Tier 1 text MUST resolve via the i18n resource system; hardcoded user-facing strings in code are forbidden (lint-enforced per CC substantive Code Quality Rule Set canonical if configured).

**Rule 7.4**: Text expansion budget — Tier 1 layouts MUST accommodate the longest declared launch language (typically German or French for European-language sets) with at least 30% width margin on dense labels (form field labels, table column headers, button text).

**Rule 7.5**: Date / time / number formats MUST follow user locale at display time; storage MUST use ISO 8601 (dates / times) and IEEE 754 (numbers) for cross-locale safety.

**Rule 7.6**: If a feature introduces a new launch language, the instance §7 i18n scope MUST be updated via §12 additive flow before slice code is merged.

**Rule 7.7 — Pseudo-localization validation**: The §7.4 text-expansion budget is a recommended engineering practice to **validate**, not only declare. Tier 1 layouts SHOULD be exercised under a pseudo-localization mode — accented-character substitution, ~30–40% length inflation, and optional RTL mirroring (per §7.2) — during development or visual review, so the 30% margin on dense labels (form labels, table headers, button text) is empirically confirmed rather than visually estimated. Pseudo-loc is **advisory**: it is not a merge-blocking CI gate (consistent with the §6 stance that a11y/i18n hygiene is enforced by practice and warn-level tooling, not hard gates).

---

# 8. Motion & animation hygiene

**Rule 8.1**: Default motion is Arco's component built-in transitions. Custom motion is allowed only when (a) it serves a user-perceived purpose (state change feedback, attention guidance, spatial continuity), AND (b) it does not violate Rule 8.2.

**Rule 8.2**: Every interactive element MUST honor `prefers-reduced-motion: reduce` — animations are disabled or replaced with instant transitions for users who set this preference.

**Rule 8.3**: Hover-state transitions are limited to 200ms; click / state-change transitions to 300ms; longer durations (page transitions, modal open / close) MUST not exceed 500ms.

**Rule 8.4**: Parallax, autoplay video, decorative bouncing or pulsing animation are forbidden (HR-product audience does not benefit from these patterns; they impose cognitive load).

**Rule 8.5**: Motion-driven feedback for critical state changes (form submission, approval action, error appearance) MUST be paired with a non-motion cue (icon, text, color change) to satisfy §6 accessibility hygiene.

---

# 9. Iconography rules

**Rule 9.1 — Primary icon source**: `@arco-design/web-react/icon` (PC) and `@arco-design/mobile-react/esm/icon` (mobile). Arco icon set is consistent across both platforms.

**Rule 9.2 — Custom icons**: Allowed only for HR-specific symbols not in Arco icon set. Custom icons MUST be added to a documented custom icon set in `apps/{app-slug}/src/frontend/icons/` as inline SVG components, both PC and mobile variants if scoped to both platforms.

**Rule 9.3 — Icon accessibility**: All meaningful icons carry `aria-label` or a text alternative (§6.1 rule 1). Decorative icons carry `aria-hidden="true"`. Icon-only buttons MUST declare an `aria-label`.

**Rule 9.4 — Icon-only UI**: Icon-only buttons / actions are discouraged unless space-constrained (mobile, dense data grids). When used, the icon's meaning MUST be conveyable to screen readers via `aria-label`, AND a tooltip on hover (PC) or accessible-name dialogue should reinforce the meaning for sighted users not yet familiar with the icon.

**Rule 9.5 — Icon import discipline**: Icons MUST be imported individually by name from the §9.1 sources (e.g., `import { IconUser } from '@arco-design/web-react/icon'`). Whole-set or namespace imports (`import * as Icons from ...`) are **forbidden** — they defeat the tree-shaking that the build-time theme path (Rule 3.1) and bundle hygiene rely on. Custom icons (§9.2) are likewise imported per-component, not pulled through an aggregated barrel that imports the entire custom set.

---

# 10. Content style governance

**Rule 10.1 — Date format**: Locale-aware; displayed format follows user locale. Storage in ISO 8601.

**Rule 10.2 — Time format**: 24-hour in system display; 12-hour in user-facing displays where locale convention supports.

**Rule 10.3 — Empty state pattern**: Every list and table MUST have a defined empty state message with optional call-to-action.

**Rule 10.4 — Error message pattern**: What went wrong + what to do about it; no technical jargon in user-facing errors (no stack traces, no internal error codes unless paired with human-readable description).

**Rule 10.5 — Button label verbs**: Action-oriented (e.g., "Save changes" not "OK"); avoid "Submit" where a more specific verb applies. The instance MAY include a canonical verb glossary.

**Rule 10.6 — Terminology consistency**: The instance MUST pick one of {Employee / Colleague / Team member} (or the equivalent in each locale) and enforce consistently.

**Rule 10.7 — Capitalization**: Sentence case for labels and buttons; title case only in page titles. Locale-specific capitalization conventions override this rule.

**Rule 10.8 — Mobile copy compaction**: Mobile labels and button text trimmed to 2–3 words where possible; long labels acceptable only when full meaning loss is unacceptable.

**Rule 10.9 — Voice and tone (HR-sensitive messaging)**: Beyond the mechanical rules above, user-facing copy at HR-sensitive moments — approval rejection, error states, empty states involving personal or employment data, and any negative or corrective message — MUST be respectful, non-blaming, and specific. Rejections state the reason and the next step without attributing fault to the user; errors follow Rule 10.4 (what happened + what to do) without alarming or accusatory phrasing; messages referencing personal or employment data use neutral, privacy-aware wording. This rule is DSG's implementation carrier for the [PRIN] People Experience Design Principles at the copy layer. The instance MAY carry exemplar phrasings for the recurring sensitive moments (rejection, access-denied, data-not-available, pending-approval).

---

# 11. Platform tier framework

## 11.1 Breakpoints

PC (via `@arco-design/web-react`):
- xs: < 480px
- sm: 480px – 767px
- md: 768px – 991px
- lg: 992px – 1199px
- xl: 1200px – 1599px
- xxl: ≥ 1600px

Mobile (via `@arco-design/mobile-react`):
- Mobile is a **separate library** targeting handset web (H5); it is NOT a responsive variant of the PC library.
- Mobile is **first-class platform**, not a "responsive PC" fallback.
- Mobile target: handset H5 in modern mobile browsers (last 2 years iOS Safari and Android Chrome) and DingTalk H5 container.

## 11.2 Platform-tier classification

Every feature's per-feature UX Design Spec instance §2B.1 MUST declare which of these tiers the feature belongs to and the rationale:

- **Tier 1 — PC and mobile both first-class**: All employee-facing self-service flows, all manager-facing workflows that need both desktop convenience and mobile pickup (e.g., approvals).
- **Tier 2 — PC-primary, mobile read-only**: HR back-office workflows where mobile access is needed for visibility but not for action (e.g., dashboards, reports).
- **Tier 3 — PC-only**: Heavy admin tools, complex data grids, multi-pane analytics, configuration screens; show "use desktop" banner on mobile.

## 11.3 Mobile parity policy

Rationale: mobile is a primary access mode — not a secondary fallback — for the employee and manager self-service flows that Tier 1 covers, so Tier 1 parity rules treat the mobile surface as first-class.

For Tier 1 features:
- All read paths MUST be available on mobile within the feature's first release scope
- All write paths declared as mobile-relevant in UX Design Spec instance MUST be available on mobile within the feature's first release scope
- Mobile-specific layouts MUST be designed first-class, not derived from PC layouts

For Tier 2 features:
- Read paths SHOULD be available on mobile (best-effort, not gated)
- Write paths are PC-only

For Tier 3 features:
- Mobile shows a "use desktop" banner; no mobile layout is required

## 11.4 Cross-platform component mapping rule

Every Tier A and Tier B component in the instance §4 inventory MUST declare its PC and mobile variants. When a component is PC-only or mobile-only, the rationale MUST be stated.

## 11.5 Token-sourced sizing for interactive elements

**Rule 11.5 — Token-sourced sizing for interactive elements**: Minimum touch-target dimensions for mobile interactive elements MUST be sourced from the §4.1 sizing/density tokens, never hardcoded in slice code (Arco mobile defaults are the floor). PC dense grids and compact toolbars MAY apply a `compact` density step, also token-sourced. Cross-platform density differences (a control denser on PC than on mobile) MUST be expressed as distinct token values, not as ad-hoc per-slice spacing. This narrows the §4.2.1 Tailwind-layout carve-out for the specific case of interactive-element sizing: a control's height and touch-target dimensions are a token concern, not layout padding to be set ad hoc per slice.

---

# 12. Update flow (core governance)

## 12.1 Who can propose a change

- The project owner
- Hub Claude during hub-side specification production (the proposal originates from a Hub conversation — typically at TK-02 step 2.3 when authoring a phase-level or per-feature UX Design Spec instance reveals a gap in current DS, or at TK-03 slice authoring when an interface need cannot be met); the change is then authored in CD where the instance lives

## 12.2 Change categories

- **Additive** (new component, new token, new locale, new layout pattern, new icon): proposed by Hub Claude in the originating feature's per-feature UX Design Spec instance §2B.4 New-Components-Or-Tokens at TK-02 step 2.3 (Hub-authored markdown); cross-cutting additives (used by multiple features in the phase) are additionally indexed in the phase-level UX Design Spec instance §2A.6 cross-cutting additive index, which cross-references the originating feature's §2B.4 entry holding the authoritative plan content; the proposal travels via operator-mediated transfer to CD per [MECH] Cross-Tool Workflow Handoff §2.1 for CD-side instance authoring; the change merges into the DS instance (CD-side) when the originating feature's slice merges to main (see [MECH] Development Track Workflow TK-12); the CC mirror is re-synced from the reviewed DS markdown export after the CD-side change is finalized.
- **Breaking** (token value change, token removal or rename per §4.3.4–§4.3.5, Arco major version upgrade, accessibility hygiene rule change, mobile-tier reassignment of existing screens, platform-tier downgrade of a feature already shipped, a backward-incompatible change to a registered **cross-cutting** (DS §4-inventoried) Tier B component's props or data contract, and the removal or Tier-C demotion (§5.4) of such a component): requires separate review gate outside the normal TK flow; all affected slices MUST be reviewed before rollout. For a Tier B contract break or a token removal, the §12.4 backward-compatibility analysis MUST enumerate every consuming slice.

## 12.3 Change process

1. Proposer surfaces the need (in a Hub conversation during TK-02 step 2.3 UX Design Spec authoring — phase-level or per-feature, or in a Hub conversation during TK-03 slice authoring, or directly in a CD authoring session)
2. For additive changes: Hub Claude authors the change plan as a §2B.4 entry in the originating feature's per-feature UX Design Spec instance (Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`); if the additive is cross-cutting (used by multiple features in the phase), Hub Claude additionally adds an index entry in the phase-level UX Design Spec instance §2A.6 cross-referencing the §2B.4 entry. For breaking changes: change is drafted in CD-native form as a standalone change file (CD-internal location)
3. **Governance-rule review** (Hub-side, against §3-§11 of this rule):
   - For additive: Hub Claude assists in checking conformance with §3-§11 during TK-02 step 2.3 when authoring the per-feature UX Design Spec instance (the §2B.4 entry) and the phase-level instance (the §2A.6 index when cross-cutting); operator signs off as part of TK-02 sign-off
   - For breaking: a separate review gate is convened; Hub Claude assists in checking conformance against §3-§11 of this rule
4. Optional adversarial review via code review tool — operator transports the change to CC for the optional adversarial-review invocation if desired (specific code review tool governed by CC substantive Codex Plugin Usage canonical post-Phase-3). **Note**: this optional adversarial review for DS changes is independent from the M0 entry self-check at TK-04; the DS-change review here is a separate, optional governance-review pathway, distinct from any TK-sequence M0 / M4 review.
5. Project owner approves or rejects
6. If approved:
   - **CD-side authoring**: CD finalizes the change in the DS instance content. CD authors against the current DSG (transferred to CD as a read-only input per [MECH] Cross-Tool Workflow Handoff §2.1) and self-checks the finalized change against §2-§11 of this rule before export. The change is recorded in the instance change log (instance topic IT14)
   - **DS markdown export regeneration**: CD generates an updated DS markdown export reflecting the new instance state per §12.7 export specification
   - **Export conformance review (Hub-side)**: the export first passes the §12.7 **structural pre-check** (mechanical completeness / shape — IT anchors present, header fields populated, key tables well-formed); only a structurally complete export proceeds to this semantic review. The operator brings the CD-generated DS markdown export into a Hub conversation; Hub Claude reviews the export against the §15 reviewer checklist to confirm the finalized instance conforms to §2-§11 of this rule. This review catches divergence between the approved change plan and what CD actually authored, including any out-of-band CD change. On a material finding, the export returns to CD for correction
   - **CC mirror sync**: on a passing export review, the operator commits the reviewed export to the CC monorepo (`specs/design-system.md`) at the next sync point (additive: at the originating feature's merge-to-main milestone per §12.5; breaking: after CD-side breaking change is finalized at the separate review gate)

## 12.4 Change content minimum structure

A DS instance change (additive or breaking) MUST include:

- **Change identity**: change-id (kebab-case, stable within the change's lifecycle), change type (`additive` or `breaking`), proposer, proposal date, target instance version
- **Affected sections**: list the instance topics (IT1-IT14) this change touches
- **Proposed change content**: the specific additions or modifications. For additive changes, provide the draft instance-topic entries ready to be merged into the instance. For breaking changes, provide both the current value and the proposed value
- **Rationale**: the business or design need motivating the change, traceable to the triggering feature's PRD or the Hub-authored per-feature UX Design Spec instance §2B.4 when applicable (cross-cutting additives additionally reference the phase-level instance §2A.6 index entry)
- **Backward-compatibility analysis** (required for `breaking`; optional for `additive`): list every currently-merged feature slice that uses the affected sections; state for each whether it is unaffected, requires re-review, or requires code change; when re-review or code change is required, state the estimated scope
- **CC enforcement impact** (required for changes touching §3, §4, §5, §11, §12.6, or §16; optional otherwise): states whether the change requires updates to CC-side ESLint rules, dependency-cruiser rules, Tailwind config, `hdc-arco-enterprise-ui` skill prompt, `hdc-wcag-accessibility-checker` skill prompt, package versions, or code-generation review checklists. If none required, state `none` with rationale. This field preserves cross-tool change visibility under the post-P-34 decoupled-reference model (§14.6) without re-coupling enforcement ownership; the field is informational to CC, not a Hub-side enforcement command
- **Adversarial review reference** (optional): if the optional adversarial review described in §12.3 step 4 was invoked, link to or attach the resulting report
- **Approval status**: one of `pending` / `approved` / `rejected` / `deferred`; when approved, record the merge event (slice-id + merge date) that applied this change

For `additive` changes, the originating feature's per-feature UX Design Spec instance §2B.4 carries the authoritative change plan; if cross-cutting, the phase-level UX Design Spec instance §2A.6 index makes the additive discoverable from the phase surface. CD authors the corresponding instance content change at merge time. For `breaking` changes, the proposer produces this content as a standalone change file (CD-internal location) and a separate review gate is convened before rollout per §12.2.

## 12.5 Merge timing

- **Additive merges**: at the originating feature's merge-to-main milestone (slice M4 → merge to `main`, per [MECH] Development Track Workflow TK-12 M4 gate). The DS instance content is finalized in CD; CD regenerates the DS markdown export; the export is reviewed Hub-side against §15 per §12.3; on a passing review the CC mirror (`specs/design-system.md`) is updated via operator-mediated transfer per [MECH] Cross-Tool Workflow Handoff.
- **Breaking merges**: as scheduled by the separate review gate. Affected slices are re-reviewed before the merge; back-propagation work is completed before the breaking change is rolled out; the CC mirror is updated after the CD-side breaking change is finalized and the export passes the §15 review.

Breaking-change rollback: if a finalized breaking change must be reverted, treat the rollback as itself a breaking change — it goes through the §12.2 separate review gate, regenerates the DS markdown export, and re-syncs the CC mirror, so SOT and mirror return to a consistent state together.

**Pending-registration cadence (additive Tier-B registrations must not accrete).** Additive registration is *due* at the originating slice's M4 (above), but the DS markdown export is operator-prompted (§12.7) and exports are commonly batched across slices — so between a slice's M4 and the next export its first-owned Tier-B / cross-cutting registrations sit **pending**. The pending-registration set is a **governed object**, not per-M4 operator memory: each merged slice records its still-unregistered first-owned Tier-B / cross-cutting components (surfaced in that slice's M4 operator digest, tracked in the app `issue-log` under `category: design-debt` until drained). The set MUST be drained — a CD export-registration per §12.3 — no later than the **earliest** of: (a) a wave boundary; (b) the TK-04 entry of any slice that **reuses** a still-unregistered shared widget (so the reuser's A9 compliance audits against a governed instance, not an as-built); (c) the set exceeding an operator-set threshold (default ~5 components). A registration carried past its drain trigger is a §12 governance signal (§12.6 + the periodic red-flag sweep) — surfaced for the operator to run the export, never flagged-and-ignored. This governs the lag that otherwise accumulates as an ad-hoc CC tracker (the W2 `issue-040` case).

## 12.6 Forbidden patterns

- Silent token or component additions in feature branches without instance update
- Custom components in slice code that duplicate existing Arco components
- Hardcoded color, typography, or spacing values in Tier 1 code outside Tailwind layout utilities
- Cross-platform divergence not declared in the instance §4 component inventory mapping table
- **Updates to the CC mirror** (`specs/design-system.md`) without a corresponding CD-side SOT update — the CC mirror is read-only and synced from CD via the reviewed DS markdown export; direct edits create drift between SOT and mirror that CC will operate against incoherently at code generation
- **A first-owned Tier-B / cross-cutting registration carried past its §12.5 drain trigger** — a slice reusing a still-unregistered shared widget (compiling against an as-built rather than the governed DS instance), or the pending-registration set accreting unbounded across waves instead of being drained at a wave boundary / reuse / threshold

## 12.7 DS markdown export specification

The DS markdown export is the canonical artifact that propagates DS instance content from CD SOT to the CC mirror. It is produced by CD on operator prompt at every change finalization (additive merge or breaking-change finalization) and at workspace inception (initial DS setup).

**Content requirement**: The DS markdown export MUST faithfully represent the DS instance content covering all required instance topics declared in §2 (IT1 Design language foundation through IT14 Change log). For each topic:
- **IT3 Design tokens**: List all tokens by taxonomy category with specific values (e.g., `primary: #1664FF`, `spacing-md: 16px`) and any per-token rationale, and each token's lifecycle state (active / deprecated, with successor where deprecated).
- **IT4 Component inventory**: Full list of Tier A (Arco direct), Tier B (HDC custom), Tier C (forbidden) with canonical import paths, PC/mobile variant declarations, and any composition/a11y notes for Tier B components.
- **IT5 Layout patterns**: Full pattern catalog with names, applicable HR scenarios, PC/mobile mappings.
- **IT6 Accessibility stance**: the instance references DSG §6, does not restate it.
- **IT7-IT10**: i18n locale list + RTL declaration, motion principles, iconography sources, content style rules.
- **IT11 Platform tier**: T1/T2/T3 framework restated.
- **IT12-IT14**: Governance pointer to this rule, custom skill integration list, change log.

The export MUST also be **feature-agnostic per §1.4**: no feature-slug / slice-id / Mn milestone / case-id reverse pointer and no named feature-specific component in any IT section (including the IT4 reuse rationale and the IT14 change-log summaries) or the export header.

**Format requirement**: Markdown with stable section anchors (`## §X.Y`) for AI-RAG consumption. Tables for token lists, component inventories, breakpoints. No proprietary CD-internal markup; the export is portable text.

**Versioning**: The export MUST declare the instance version in its header. The CC mirror file `specs/design-system.md` carries the export content with matching version metadata.

**Export header diff summary**: Beyond instance version, each export header MUST declare previous instance version, new instance version, change category (`additive` / `breaking` / `structural`), and the IT section IDs touched (e.g., `IT3, IT4`). Per-token / per-component change detail is recorded in the instance IT14 change log, not duplicated in the export header. The summary lets §12.3 export reviewers locate change surface without scanning the entire export.

**Generation mechanism**: Operator prompts CD to generate the export at each §12.5 sync point. The prompt should request a structured markdown summary covering all §2 topics; CD produces it from the SOT instance content.

**Structural pre-check (gates the §12.3 conformance review)**: Before the §12.3 semantic conformance review consumes reviewer attention, the export passes a lightweight **structural** validation — presence and shape only, no §3–§11 semantics. It confirms: (a) all required instance-topic anchors **IT1–IT14** are present with stable `## §X.Y`-style headers; (b) the **§2 required instance header fields** are populated **and** the **export header diff summary** (previous version, new version, change category, IT sections touched) is present; (c) the **IT3 token list** carries columns `name / value / category / lifecycle-state / rationale-where-divergent`, the **IT4 component inventory** carries `name / tier / import-path / PC-variant / mobile-variant`, and the **IT11 breakpoint table** carries `name / range`; (d) the export SHOULD be scanned for obvious **feature-identifier patterns** (slug-like tokens, `Mn` milestones, `issue-` / `DR-` / `Q-` case-ids) in any IT section or the export header, and returned to CD if found — a heuristic catch for §1.4 reverse pointers. This check is *mechanical* — it needs no design judgment: it cannot judge §3–§11 semantic conformance, and the (d) feature-identifier scan is a pattern-match, not a full §1.4 conformance judgment (full §1.4 conformance is verified at the §15 review, item 17). It runs as the first pass of the §12.3 review (today by Hub Claude in the review conversation; it could later be scripted). On any pre-check failure the export returns to CD **before** the semantic review and operator sign-off, so reviewer effort is spent on §3–§11 semantics rather than on detecting missing sections, malformed tables, or obvious feature identifiers.

**Transfer mechanism**: The operator brings the CD-generated markdown into a Hub conversation for the §12.3 export conformance review; on a passing review, the operator commits it to the CC monorepo per [MECH] Cross-Tool Workflow Handoff.

## 12.8 Rejected and deferred changes

A change whose §12.4 Approval status resolves to `rejected` or `deferred` does not reach CD-side authoring and produces no DS markdown export or CC mirror sync.

- **Rejected**: the change is closed. The §2B.4 New-Components-Or-Tokens entry in the originating feature's per-feature UX Design Spec instance is marked rejected (with the rejection reason) and not carried into the DS instance; any matching phase-level §2A.6 index entry is also marked rejected; the feature proceeds with the existing DS inventory.
- **Deferred**: the change is held for a later instance version. The §2B.4 entry is marked deferred (matching §2A.6 index entry likewise); it is re-proposed through §12.3 when revisited, rather than tracked as an open in-flight change.

In neither case is the DS instance, the DS markdown export, or the CC mirror modified.

---

# 13. Custom skill integration and Hub consumption

The DS instance is consumed at two Claude Code runtime surfaces (`hdc-arco-enterprise-ui` and `hdc-wcag-accessibility-checker` skills, both reading the CC mirror); the Hub-side consumption surface is covered separately in §13.3. Their respective contracts with this rule:

## 13.1 `hdc-arco-enterprise-ui`

- Loaded automatically at Claude Code session start
- Invoked when generating Tier 1 React code (PC or mobile)
- Reads the CC mirror at `specs/design-system.md` and applies tokens, component inventory, layout patterns, and governance rules during code generation
- Skill source: `.claude/skills/hdc-arco-enterprise-ui/SKILL.md`

When this rule changes, the skill MAY need prompt adjustment to track the change. This is a paired-update relationship (P-19 in [OS] §8.5.2).

## 13.2 `hdc-wcag-accessibility-checker`

- An **on-demand sanity-check utility** (per §6.3). NOT auto-invoked at any milestone.
- Operator manually invokes when a screen warrants a spot check or before a major release.
- The skill wraps `axe-core` and produces a non-binding diagnostic report; findings are advisory.
- ESLint `eslint-plugin-jsx-a11y` at `warn` severity (per CC substantive Code Quality Rule Set canonical) is the routine a11y check, not this skill.
- Skill source: `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md`
- The skill name retains "wcag" for stable identifier; functionally it is an a11y diagnostic tool.

These skills are hub-designed specification outputs, not Claude Code runtime artifacts in the canonical sense. They are updated alongside this rule via the §12 governance process when applicable.

## 13.3 Hub-side consumption discipline (TK-02 step 2.3 + export review)

Hub holds no DS instance copy. Hub holds this governance rule (DSG) and consumes CD-authored design files and the CD-generated DS markdown export as transient inputs. Hub-side discipline covers three activities, with the design file quality check and UX Design Spec authoring now applying at two parallel tracks (phase-level for the design file's cross-cutting sections + per-feature for each labeled slice):

- **Design file quality check (spec-readiness)**: When the operator transfers the CD-authored phase-level design file to the Hub session, Hub Claude runs two parallel-able quality-check tracks:
  - **Phase-level track** (per [TPL] UX Design Spec §3A.1): Hub Claude reviews the design file's cross-cutting sections (platform shell artboards, shared visual vocabulary artboards, cross-feature touchpoint maps, phase-level horizontal design decisions, visual regression naming convention annotations) and verifies they are spec-ready at the phase scope — coverage of cross-cutting topics, alignment with TDD §1 + §2 (especially §2.2.5 Integration boundaries when cross-feature touchpoints carry interface contracts), grounding sufficiency for the phase-level UX Design Spec instance authoring.
  - **Per-feature track** (per [TPL] UX Design Spec §3B.1, iterated per tier-1-involved feature): Hub Claude locates the feature's labeled slice (frame / section / page tagged with feature-slug) in the design file, then verifies that slice is spec-ready — complete against that feature's PRD/TDD scope (all required screens, states, and flows covered), internally consistent, carrying annotations rich enough to author the per-feature UX Design Spec instance from, and annotating the DS instance version the design file was authored against (component / token callouts SHOULD reference identifiable DS instance sections where practical, so downstream UX Design Spec references trace to a specific DS state rather than implicit recall). The per-feature internal labeling itself is also verified — a phase-level design file lacking per-feature labels cannot be quality-checked per feature and is returned to CD for labeling before per-feature grounding proceeds.

  Both tracks use the PRD/TDD (which Hub holds) and the design file itself; neither checks DS-conformance against a DS mirror. DS-conformance of the design file is CD's responsibility — CD authored it holding the DS instance. A design file (either cross-cutting section or per-feature slice) introducing a component / token not yet in the DS is a legitimate §12 additive proposal, not a defect; Hub Claude captures it as a per-feature UX Design Spec §2B.4 entry on the originating feature's instance, additionally indexed in the phase-level instance §2A.6 if the additive is cross-cutting. Findings are surfaced to the operator per [TPL] UX Design Spec §3 reviewer checklists.

- **UX Design Spec authoring grounding**: When Hub Claude authors the UX Design Spec instance markdowns (after the corresponding design file quality check passes), it grounds component / token / pattern claims in the **CD-authored design files** at the matching scope:
  - The phase-level UX Design Spec instance grounds in the design file's cross-cutting sections — every shell / vocabulary / touchpoint reference is transcribed from the relevant cross-cutting artboard or annotation.
  - Each per-feature UX Design Spec instance grounds in the corresponding labeled slice — every `component: <name>` reference is transcribed from a component callout in the slice (which CD, as DS owner, authored using the DS instance).

  Hub does not hold an independent DS copy to cross-check against; the design file is the authoritative input. CC verifies the UX Design Spec instances' references against the CC mirror at TK-04 M0 entry via SK-F, and CC code generation is the downstream backstop for any non-canonical reference.

- **Export conformance review**: When CD finalizes a DS instance change and generates a DS markdown export (§12.3 step 6), the operator brings the export into a Hub conversation. Hub Claude reviews the export against the §15 reviewer checklist to confirm the finalized instance conforms to §2-§11. This is the cross-workspace conformance gate — it catches divergence between the approved change plan and what CD authored, and any out-of-band CD change — before the export reaches the CC mirror.

These are not "skills" in the CC sense (Hub Claude does not load `.claude/skills/`); they are consumption disciplines applied directly by Hub Claude during conversation. Hub Claude holds DSG at runtime, so the disciplines track this rule automatically when it changes.

---

# 14. Pairing rules

## 14.1 Pairing with UX Design Spec instances

Both UX Design Spec instance types (phase-level + per-feature, Hub-authored markdown at TK-02 step 2.3 when any feature has `tier_1_involved=true` per `[TPL] UX Design Spec`) MUST reference the current DS instance version (recorded in the CD-authored design file at the time of authoring). Each per-feature instance declares the platform tier (per §11.2) the feature targets. If a feature introduces a new component, token, or layout pattern, the originating feature's per-feature UX Design Spec instance §2B.4 New-Components-Or-Tokens MUST include an update plan (per §12.4 change content structure); cross-cutting additives are additionally indexed in the phase-level instance §2A.6 (the index cross-references the originating feature's §2B.4 entry rather than duplicating the plan content). This triggers the §12 additive flow with CD-side authoring of the actual instance content change.

Both Hub-authored UX Design Spec instances are grounded in the CD-authored design file per §13.3 consumption discipline (phase-level instance in cross-cutting sections; per-feature instance in the corresponding labeled slice).

## 14.2 Pairing with intent.md UX brief

Each slice's intent.md MAY include a UX brief section listing screens and components used. The components referenced MUST exist in the instance §4 component inventory (Tier A or Tier B); platform coverage (PC, mobile, both) MUST be stated. Hub Claude authors the intent.md UX brief at TK-03 by extracting from the slice-relevant subsets of both Hub-authored UX Design Spec instances — the per-feature instance (for in-slice UX content) and the phase-level instance (for cross-feature touchpoints / shared vocabulary the slice consumes) — both of which were authored at TK-02 step 2.3 grounded in the CD-authored design file. The chain of grounding ensures slice-level UX brief content is DS-compliant.

## 14.3 Pairing with test-plan.yaml

`test_type: accessibility` cases in per-slice test-plan.yaml are **optional** per §6.2. When the per-feature UX Design Spec instance §2B.5 declares specific a11y considerations beyond what Arco defaults provide, the slice's test plan MAY include such cases; otherwise the type is not required. There is no automated a11y gate at any milestone.

## 14.4 Pairing with Tier 1 code

All Tier 1 React code references design tokens (§4) and component inventory (§5). The `hdc-arco-enterprise-ui` skill enforces this at code generation time by reading the CC mirror; compliance-checker (A9) audits at M4. Lint-level enforcement of the same rules is owned by CC substantive Code Quality Rule Set canonical.

## 14.5 Pairing with custom skills

Skills §13.1 and §13.2 consume the CC mirror of the DS instance plus this rule's content. Hub Claude §13.3 consumes CD-authored design files plus this rule's content. When this rule or the instance is updated (additive or breaking), the skills may need prompt adjustment and the Hub consumption discipline tracks automatically. This is a paired-update relationship (P-19 in [OS] §8.5.2).

## 14.6 Pairing with CC substantive Code Quality Rule Set canonical (post-Phase-3)

**Pairing status note**: P-34 (was: DSG ↔ [MECH] Code Quality Rule Set lint rules) was **RETIRED in Phase 3** per [REF] Hub-CD-CC §5.4.4 — counterparty CQ fully migrated to CC substantive canonical. The substantive alignment between DSG design-level rules and CC-side lint enforcement is now governed at CC's discretion under the decoupled-reference model.

CC substantive Code Quality Rule Set canonical declares the runtime and build-time tool-level enforcement of Tier 1 visual rules. Token-consumption rules in §4 and component-inventory rules in §5 of this Hub-side DSG canonical are implemented as ESLint rules and dependency-cruiser rules per CC substantive CQ canonical. The accessibility recommendations in §6.1 map to `eslint-plugin-jsx-a11y` rules in CC substantive CQ canonical at `warn` severity (advisory only). When this rule changes the design-level rules, the operator notifies CC for CC-side substantive CQ to update under CC's own discipline; no Hub-side P-NN pairing tracks this Hub↔CC coordination.

---

# 15. Reviewer checklist (for DS instance updates)

When reviewing an instance update for sign-off (additive merge at slice M4 / breaking review gate), verify:

1. Design language foundation rationale references actual HDC context, not generic reasoning
2. Implementation path specifies both PC and mobile library version pin and custom component policy; corporate VI primary color and font stack are declared; theme injection mechanism is explicitly the build-time `less-loader` `modifyVars` path (not a runtime CSS file or `@arco-themes/...` npm package); single monorepo theme source at `packages/hdc-corporate-theme/`
3. Token section lists all custom HDC tokens with VI source values and justification
4. Component inventory is MECE on both PC and mobile; Tier C forbidden list is explicit; cross-platform mapping is complete
4a. Each Tier B component's spec is complete enough for a downstream implementer or reviewer to act on it — at minimum: composition (Arco primitives + tokens consumed), props / data contract, states, PC behavior, mobile behavior, token mapping, accessibility posture, and when-to-use vs when-to-avoid. Richer fields (examples, anti-patterns, content rules, explicit owner) are added when component complexity warrants; the sign-off test is sufficiency for `hdc-arco-enterprise-ui` consumption and human review, not coverage of a fixed field count
4b. Each Tier B component's reuse-scope classification (§5.2.4) is correct and its registration matches the scope — a **cross-cutting** Tier B appears in the DS instance §4 inventory and is indexed in the phase-level §2A.6; a **feature-specific** Tier B (single owner, or surfaced elsewhere only via a declared structural seam) stays in the originating feature's §2B.4 and is absent from the DS instance §4 inventory
5. Layout-pattern mapping covers all major HDC HR scenarios on both PC and mobile
6. Accessibility section is a pointer to this rule's §6 stance and does not restate it (per the §2 header field and §12.7 IT6)
7. i18n declares RTL capability requirement regardless of launch languages
8. Platform tiers (T1/T2/T3) are declared and the instance lists tier defaults
9. Skill integration lists both `hdc-arco-enterprise-ui` and `hdc-wcag-accessibility-checker`; Hub-side consumption discipline per §13.3 is referenced
10. Governance section in the instance references this rule's §12 process
11. No duplication with PRD, UX Design Spec, intent, acceptance scope
12. (Post-sync confirmation) After the CC mirror sync that follows a passing review per §12.3, the CC mirror (`specs/design-system.md`) reflects the reviewed DS markdown export and its version metadata matches the CD-side declared instance version
13. DS markdown export per §12.7 was generated for this update and is referenced in the instance header
14. (If the update touches §4 tokens) token lifecycle states are valid — every deprecation names a live successor (Rule 4.3.2), no token is `removed` while a merged slice still references it (Rule 4.3.4), and any rename followed the add→deprecate→remove sequence (Rule 4.3.5)
15. (If the update registers or changes a Tier B component) a backward-incompatible props/contract change to a **cross-cutting** Tier B is routed as breaking per §12.2 with a §12.4 consuming-slice enumeration; a feature-specific Tier B contract change correctly stays within its owning feature (Rule 5.2.5)
16. Sizing/density tokens (§4.1) are declared where the feature has mobile touch targets or dense grids and are token-sourced not hardcoded (Rule 11.5); any new color/elevation token satisfies theme-variant readiness (Rule 3.7 / Rule 4.2.6)
17. The instance is feature-agnostic (§1.4): no feature-slug / slice-id / milestone (Mn) / case-id reverse pointer in any IT section — including the IT4 component-inventory reuse rationale and the IT14 change-log summaries — and no feature-specific component named in a cross-cutting IT4 entry. Feature-specific components are absent from the IT4 inventory (Rule 5.2.4; cf. item 4b). A fail names a specific instance location carrying a feature identifier

Items 1-11 and 13-17 are verified at the §12.3 export conformance review, before the CC mirror sync; item 12 is verified after the sync, as a post-sync confirmation. Each is a binary pass/fail check: an item fails when the reviewer can name a specific instance section (or specific missing content) that does not satisfy it. If 2+ of the pre-sync items (1-11, 13-17) fail by that test, the instance update is not yet ready for sign-off and the sync does not proceed. Once the sync has occurred, item 12 is the single post-sync confirmation — it must pass for the sync to be considered complete.

---

# 16. Anti-drift red flags

Red flags that should trigger correction:

- Tier 1 code using hardcoded colors, spacing, or typography values (outside Tailwind layout utilities)
- VI overrides applied via runtime CSS files (e.g., `theme.css` imported at app entry) instead of build-time `less-loader` `modifyVars` — violates Rule 3.1 (see §3.1 for the rationale)
- An `@arco-themes/...` npm package introduced as a dependency — violates Rule 3.3 (see §3.3 for the rationale)
- Per-app theme duplication (separate `hdc-corporate-theme.css` or `theme.less` files inside `apps/{app-slug}/src/frontend/themes/`) instead of the single monorepo theme source — violates Rule 3.2 (see §3.2)
- New components introduced in feature code without DS instance update via §12 flow
- Non-Arco third-party UI libraries being imported in Tier 1 (Material-UI, Ant Design, shadcn/ui, Mantine, etc.)
- `hdc-arco-enterprise-ui` skill not being invoked during Tier 1 code generation
- A dedicated a11y CI gate or merge-block introduced for Tier 1 without §12 governance change (the inverse drift — §6 stance is no formal a11y gate)
- Recurring `eslint-plugin-jsx-a11y` warnings ignored across many slices instead of fixed when trivial (the rules are warn-level not because they are unimportant, but because Arco defaults handle most cases — chronic warning accumulation indicates real drift)
- Token values drifting across slices
- Custom Component in Tier B that duplicates an existing Tier A Arco component
- i18n resource files missing for supported languages
- RTL not tested when new components are added
- Mobile feature shipped using PC components (responsive workaround instead of mobile library)
- PC feature shipped using mobile components
- WeChat / DingTalk Mini Program component libraries imported in Tier 1
- **The CC mirror edited directly without corresponding CD-side SOT update** — a §12.6 forbidden pattern (see §12.6 for the rationale)
- **A Hub-side DS instance mirror re-introduced** (a `hdc_ref_*` DS instance copy, or DS instance content inlined into a Hub canonical source or PI) — the two-way model in §1.1 deliberately holds no DS instance copy at Hub; re-introducing one is drift back toward the retired three-way model and re-incurs the lock-step synchronization burden §1.1 removed
- **Feature identifiers in the canonical instance** — a feature-slug / slice-id / Mn milestone / case- or issue-id, or a named feature-specific component, appearing in the DS instance content or the DS markdown export (IT4 component-inventory reuse rationale, IT4 reuse-scope classification, IT14 change-log, export header) — a §1.4 violation: the canonical source is coupling to the downstream cases it serves. The application context belongs in the change records / per-feature specs, not the instance. This is the content dual of the "A Hub-side DS instance mirror re-introduced" red flag above (which is the §1.1 distribution dual)
- **Hub Claude in TK-02 step 2.3 authoring a UX Design Spec instance (phase-level or per-feature) without grounding in the CD-authored design file** — component / token / pattern claims must be transcribed from the design file's cross-cutting sections (phase-level instance) or labeled slice callouts (per-feature instance) per §13.3; ungrounded authoring produces UX Design Spec instances that may reference nonexistent or misnamed DS elements
- **A per-feature UX Design Spec instance §2B.4 declares a cross-cutting additive but no matching phase-level §2A.6 index entry exists** — cross-cutting additives must be discoverable from the phase-level surface; the §2A.6 index is required for any §2B.4 entry with `scope: cross-cutting`
- **A Tier B component misclassified against the §5.2.4 reuse-scope criterion** — a feature-specific component (single owning feature, or surfaced in another feature only through a declared structural seam such as `ObjectPage` facet-body injection) given a DS instance §4 inventory entry instead of staying in its feature's §2B.4; or a genuinely cross-cutting component (peer-instantiated across ≥2 features with no single owning feature mediating) left in a single feature's §2B.4 without the DS instance §4 + phase §2A.6 registration
- **DS markdown export not regenerated at §12 change finalization** — instance content updated in CD SOT but no export produced, leaving the CC mirror stale relative to SOT
- **CC mirror sync bypasses the §15 export review or the operator-mediated transfer** — the CC mirror must be updated only from a DS markdown export that passed the §12.3 export conformance review; a direct CD-to-mirror push bypassing the review or the operator audit violates §12.3 and [MECH] Cross-Tool Workflow Handoff operator-audit discipline
- **Tier B additive proposals chronically deferred or stuck** — proposals raised in per-feature UX Design Spec instance §2B.4 entries remain in `pending` or `deferred` state across multiple TK cycles without resolution or rejection per §12.8; the §12 flow is being avoided or has stalled, and the DS instance is failing to absorb legitimate evolution pressure (the inverse of the §12.6 "silent additions" pattern — proposed correctly but never advanced)
- **A token moved to `removed` while a merged slice still references it**, or a token rename done as an in-place name/value edit instead of the Rule 4.3.5 add→deprecate→remove sequence — violates §4.3
- **A backward-incompatible props/contract change to a registered cross-cutting Tier B component rolled out without the §12.2 breaking gate** and §12.4 consuming-slice analysis — violates Rule 5.2.5 / §12.2
- **Whole-set / namespace icon import** (`import * as Icons` from an Arco icon path, or from a custom-icon barrel) instead of named per-icon imports — violates Rule 9.5, defeats tree-shaking
- **A DS markdown export reaching §12.3 review without having passed the §12.7 structural pre-check** (missing IT anchor, unpopulated header field, malformed token/component/breakpoint table) — the mechanical pre-check must gate the semantic review
- **Hardcoded touch-target or control-height values on mobile interactive elements** instead of §4.1 sizing tokens — violates Rule 11.5, breaks the §11.3 mobile-parity token backing
- **A new color or elevation token authored so a future dark/alternate theme cannot supply a paired value** without a rename or taxonomy change — violates Rule 3.7 / Rule 4.2.6 theme-variance readiness

**Periodic sweep**: These red flags are scanned both at change-flow review (§12.3 export review, §15 reviewer checklist) and as part of [MECH] Canonical File Self-Audit periodic sweep over DSG and the DS instance. Chronic appearance of a red flag is itself a §12 governance signal — the operator surfaces it for breaking-change review or §12.8 resolution rather than continuing to flag-and-ignore.
