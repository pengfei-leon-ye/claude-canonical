# [RULE] Design System Governance

- **Project**: HR Digital Cockpit
- **Document Type**: Architecture Specification
- **Status**: Active canonical
- **Role**: Stable governance-rules source defining the design-system framework that constrains all Tier 1 frontend work across the project — design language foundation rules, token taxonomy and consumption discipline, component inventory tiering, layout-pattern governance, accessibility stance, internationalization approach, motion hygiene, iconography rules, content style norms, platform-tier framework, change-process governance, custom-skill integration contract, pairing rules with adjacent canonical sources, reviewer checklist, and anti-drift red flags. The DS instance content itself (tokens, component inventories, layout pattern catalog, etc.) is the source-of-truth in Claude Design (CD-internal); CC carries a read-only code-time mirror at `specs/design-system.md` for code generation, per the two-way distribution model in §1.1. Hub holds no DS instance copy — it holds the governance rules (this source) and consumes CD-authored design files at spec-authoring time.
- **Source Category**: Cat 4
- **Management-System Role**: Governance specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact. The instance it governs is a project-level singleton specification output, not a per-feature artifact.
- **Relationship to [OS]**: Serves the Specify loop by establishing the design-system governance framework that downstream feature-level specification artifacts (PRD, TDD, intent, acceptance, per-feature UX Design Spec instances) must respect; subject to [OS] §8.5 paired-update consistency. Grounded in [OS] §0.1 project-level operating premises and [OS] §0.2 Cat 4 role anchor.
- **Relationship to [PRIN] HR Digital Decision Design Principles**: Applies §3 (global core with governed local variance — Arco Design as global core for HDC's Tier 1 visual layer, regional i18n and RTL as governed variance), §5 (management mechanism over ad hoc control — this governance is the mechanism preventing per-slice visual drift), §6 (operation management and value realization by design — accessibility hygiene and i18n are operation realities captured upfront), §10 (MECE — component inventory)
- **Relationship to [PRIN] People Experience Design Principles**: This rule is the primary implementation carrier for People Experience principles when the topic lens is experience quality and consistency; the dual-platform (PC + mobile) coverage in §11 directly serves People Experience moments-of-truth that occur outside the desktop
- **Relationship to [REF] Hub-CD-CC Architecture**: This rule's SOT-distribution declarations in §1.1 align to §5.2 two-way distribution model (CD = SOT / CC = code-time mirror). CD is the instance SOT; CC carries a read-only mirror at `specs/design-system.md` for code-time consumption. Hub holds no DS instance copy; at TK-02 step 2.3 Hub Claude consumes CD-authored design files (not a DS mirror) per §13.3. When the architecture's distribution model changes substantively, §1.1 of this rule is re-verified.
- **Relationship to [RULE] Claude Code Architecture Rules**: Constrains Tier 1 (React) work exclusively; Tier 2 and Tier 3 are out of scope. The CC mirror of the DS instance is a project-level singleton at the monorepo root per CCAR §Y.1, not under any `apps/{app-slug}/` directory; downstream feature artifacts that reference it (per-feature UX Design Spec instances authored in Hub per `[TPL] UX Design Spec`, intent.md UX brief, test-plan.yaml accessibility cases) are app-scoped under `apps/{app-slug}/specs/...`. The CC mirror is included in CCAR §X.2.1 `business_rules_only` scope allow list as `specs/design-system.md`.
- **Relationship to [MECH] Development Track Workflow**: The DS instance and the CC mirror are established at workspace inception per [RULE] Workspace Topology constitutional residue §5 (workspace inception governance) via initial CD authoring + DS markdown export to the CC mirror location (after the §15 export review per §12). TK-02 step 2.3 consumes CD-authored design files — design file quality check (spec-readiness) + UX Design Spec authoring grounded in the design files — per §13.3. CC mirror is referenced by TK-04 (M0 entry, per-slice spec consumption) and TK-05+ (code writing, M3 visual review). Additive updates to the instance authored in CD propagate to the CC mirror via the §12 sync mechanism in this rule.
- **Relationship to [MECH] Cross-Tool Workflow Handoff**: §2 (Hub ↔ CD path) carries DS-related discussions, DSG governance text into CD as a read-only input for DS instance authoring (per §12.1), CD-authored design files transferred to Hub for TK-02 step 2.3 consumption, and the CD-generated DS markdown export transferred to Hub for the §15 export conformance review; §3 (Hub ↔ CC path) carries DSG governance text into CC and transfers the reviewed DS markdown export to the CC mirror; §4 (CD ↔ CC path, decoupled-by-default during research preview) is currently not directly used for DS sync (the CC mirror receives DS markdown via operator-mediated transfer from CD through the Hub review session). The export-review cadence and triggers are owned by §12 of this rule.
- **Relationship to [MECH] Code Quality Rule Set**: **CQ migrated to CC substantive canonical (Phase 3)**. CC substantive Code Quality Rule Set canonical declares the runtime and build-time tool-level enforcement of Tier 1 visual rules; this rule declares the design-level rules that those tools enforce. Token-consumption rules in §4 and component-inventory rules in §5 are implemented as ESLint rules and dependency-cruiser rules per CC substantive CQ canonical §3. Hub↔CC coordination is governed by the decoupled-reference model in [REF] Hub-CD-CC Architecture §5.4.4.
- **Relationship to adjacent [TPL] sources**:
  - Upstream of `[TPL] UX Design Spec` — DSG governs the design rules; UX Design Spec instances declare per-feature UX coverage Hub-authored from CD design files per [TPL] UX Design Spec §0; the UX Design Spec's component selections and any new-component / new-token plans MUST respect DSG inventory and §12 change flow
  - Upstream of `[TPL] Intent and Acceptance Interface Writing Standard` (intent.md UX brief section authors components and a11y references that MUST respect DSG inventory + §6 stance)
  - Upstream of `[TPL] Test Plan YAML Schema` (accessibility test type cases)
- **Relationship to custom skills**:
  - Consumed at Claude Code runtime by `hdc-arco-enterprise-ui` skill during Tier 1 code generation, by reading the CC mirror at `specs/design-system.md`
  - Consumed at Claude Code runtime by `hdc-wcag-accessibility-checker` skill **on operator demand only** (per §6.3); not auto-invoked
  - Consumed at Hub Claude runtime in TK-02 step 2.3 — Hub Claude grounds in CD-authored design files (Hub holds no DS mirror); this is not a "skill" in the CC sense but a consumption discipline described in §13.3
- **Relationship to [RULE] DingTalk Markdown Format Control Specification**: When DS instance content is uploaded to DingTalk Docs for stakeholder visibility, apply that rule (uploading happens from CD source or the CC mirror, not authored at Hub)
- **Pairings I participate in**: P-19 (with `hdc-arco-enterprise-ui` + `hdc-wcag-accessibility-checker` SKILL.md). P-34 (was: with [MECH] Code Quality Rule Set lint rules) **RETIRED in Phase 3** per [REF] Hub-CD-CC §5.4.4 — counterparty CQ fully migrated to CC substantive canonical; alignment with DSG design-level rules now governed at CC's discretion.

## How to use this source

Use this source when:
- Initializing a new HR Digital Cockpit workstream and the design-system governance framework needs to be applied (CD instance is created; the CC mirror at `specs/design-system.md` is established at workspace inception via CD-generated DS markdown export, reviewed against §15 per §12)
- Introducing a new component, token, or layout pattern that will be reused across slices (governance flow per §12)
- Elevating a locally-invented pattern from one slice into a shared asset
- Reviewing whether a Tier 1 implementation respects the project design system
- Updating accessibility hygiene rules or internationalization scope
- Authoring a feature's UX Design Spec instance (Hub-authored markdown at TK-02 step 2.3 from CD design files; this rule declares the governance baseline for what design content the spec must respect)
- Performing design file quality check at TK-02 step 2.3 (Hub Claude verifies CD-authored design files are spec-ready — complete against PRD/TDD scope, internally consistent, annotations rich enough to author the UX Design Spec instance from — per §13.3)

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

Hub holds no DS instance mirror. At spec-authoring time (TK-02 step 2.3) Hub Claude consumes CD-authored design files, not a DS instance copy; the export conformance review (§12.3) is the Hub-side touchpoint with DS instance content, performed transiently on the export rather than via a persisted mirror.

Update categories:
- **Additive updates** (new component added, new token added, i18n scope expanded, new layout pattern added): authored in CD per a feature's UX needs (the additive plan is captured as the corresponding feature's UX Design Spec instance §2.4 New-Components-Or-Tokens entry, Hub-authored at TK-02 step 2.3). Once approved per §12, CD finalizes the change; CD regenerates the DS markdown export; the export is reviewed Hub-side against §15 per §12.3; on a passing review the **CC mirror** (`specs/design-system.md`) is re-synced, typically at the feature's merge-to-main milestone (see [MECH] Development Track Workflow TK-12 M4 gate).
- **Breaking updates** (token value change, Arco major version upgrade, accessibility hygiene rule change, mobile-tier change): require explicit review gate per §12.2; back-propagate to all affected slices; the CC mirror is re-synced after the CD-side breaking change is finalized and the export passes the §15 review.

There is one instance per project (HDC has exactly one DS instance covering all apps). The instance is shared across all apps, all phases, all features. There is one DS markdown export per instance version, transferred to the CC mirror after the §15 export conformance review.

**Closed-loop rationale**: the DS instance has one SOT (CD) and one mirror (the CC code-time mirror, consumed by SK-F at code generation). Hub holds no DS instance copy — at spec-authoring time Hub consumes CD-authored design files, which carry the component / token / pattern callouts. DS-instance conformance to this governance rule is checked at the two workspaces that execute against the DS (CD at authoring time, holding DSG as a transferred input per §12.1; CC at code generation) plus a Hub-side review of the CD-generated DS markdown export before it reaches the CC mirror (per §12.3). The single mirror removes the lock-step synchronization burden that a multi-mirror model carries.

## 1.2 Boundary with feature-level artifacts

| Artifact | Location | Scope | Contains |
|---|---|---|---|
| DS instance (SOT in CD; CC mirror at `specs/design-system.md`) | CD + CC | Project-level | Design language choice, tokens, component inventory, a11y hygiene rules, i18n scope, motion guidelines, mobile/PC platform split |
| CD-authored design files (per feature, when tier_1_involved=true) | CD workspace; transferred to Hub at TK-02 step 2.2 → 2.3; transferred to CC at TK-04 as visual reference | Feature-level | Hi-fi mockups, prototypes, wireframes, component callouts, interaction flows with embedded textual annotations; cover [TPL] UX Design Spec §2 categories in CD-native form |
| **UX Design Spec instance per `[TPL] UX Design Spec` (Hub-authored markdown at TK-02 step 2.3 from CD design files)** | Hub-authored at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md` | Feature-level | Affected Tier 1 scope, components from DS instance referenced by this feature, new components introduced (with §12 update plan), feature-specific a11y notes, mobile/PC scope; written in markdown for AI-RAG consumption |
| `apps/{app-slug}/specs/intent/{slice-id}.md` UX brief section | Hub-authored at TK-03 (consumes UX Design Spec instance + design files as visual reference); transferred to CC | Slice-level | Screen list, interaction highlights, i18n/a11y call-outs specific to the slice |
| `apps/{app-slug}/specs/acceptance/{slice-id}.yaml` | Hub-authored at TK-03; transferred to CC | Slice-level | Machine-readable acceptance scenarios including a11y expectations |
| `apps/{app-slug}/specs/test-plan/{slice-id}.yaml` | Hub-authored at TK-03; transferred to CC | Slice-level | Test cases including `test_type: accessibility` |

If content belongs in feature-level artifacts, do not duplicate it into the DS instance. The instance holds project-wide decisions only.

**Path discipline note**: The CC DS mirror is a project-level singleton at the CC-monorepo root `specs/design-system.md` (not under any `apps/{app-slug}/` directory because the design system is shared across all apps). All feature-scoped artifacts referenced above use the `apps/{app-slug}/` prefix per CC substantive Claude Code Architecture Rules canonical (repository layout §Y.1).

## 1.3 Cross-canonical-source boundary

The DS instance is bounded by adjacent canonical sources. Content that belongs in these sources should not appear in the instance.

| Content type | Correct source |
|---|---|
| Business logic, workflow definitions, feature user value | PRD |
| Feature-specific UX coverage (screens, components used, layout patterns, new-asset additive update plans, slice-specific a11y) | UX Design Spec instance per `[TPL] UX Design Spec` (Hub-authored markdown at TK-02 step 2.3 from CD design files) |
| Per-feature visual artifacts (mockups, prototypes, interaction flows) | CD-authored design files (per [REF] Hub-CD-CC Architecture §3.4.1) — these are the source material from which UX Design Spec instances are Hub-authored |
| Per-slice UX brief (screen list, interactions, slice-level a11y/i18n call-outs) | intent.md (cross-ref §1.2) |
| Implementation-level React component code | Code |
| Tool-level lint and architecture-rule enforcement | CC substantive Code Quality Rule Set canonical (post-Phase-3) |
| Complete restatement of Arco Design official guidelines | Reference Arco docs, don't duplicate |

The instance captures project-level design foundation and authoritative lists (tokens, components, layout-pattern mapping, a11y hygiene, i18n scope). Per-feature UX decisions live in UX Design Spec instances; per-slice UX briefs live in intent.md.

---

# 2. Instance section contract

The DS instance must contain coverage for the following section topics. The specific content of each section lives in the instance (in CD as SOT, mirrored to CC); this rule declares only **what topics must be covered**, not what the content must say.

Required instance section topics:
1. **Design language foundation** — base design system reference and rationale
2. **Implementation path** — PC implementation, mobile implementation, cross-platform consistency
3. **Design tokens** — color tokens (Arco semantic overrides + HDC custom accents + HR-specific semantic states), text/background tokens, typography tokens, corporate font stack, spacing tokens, border radius / elevation / other visual tokens, token consumption rules
4. **Component inventory** — Tier A (Arco used directly), Tier B (HDC custom), Tier C (forbidden); cross-platform mapping
5. **HDC layout patterns to HR scenario mapping** — PC patterns, mobile patterns, cross-platform pattern mapping
6. **Accessibility stance** — recommended engineering practices, what is explicitly NOT required, on-demand sanity check, rationale
7. **Internationalization and RTL** — locale coverage and RTL approach
8. **Motion and animation** — motion principles, `prefers-reduced-motion` handling
9. **Iconography** — primary icon source, custom icon policy, a11y for icons
10. **Content style guide** — date / time formats, empty / error patterns, button verbs, terminology, capitalization, mobile copy compaction
11. **Responsive behavior and platform tiers** — breakpoints, mobile-as-first-class declaration, T1/T2/T3 platform tier framework
12. **Governance** — change process (this is partially redundant with this rule's §12, but the instance may include a brief summary or pointer)
13. **Custom skill integration** — which skills consume the instance and how
14. **Change log** — chronological log of approved instance changes

All sections §1 through §14 of the instance topic list are required in the instance. There is no leveled instance; this is per-project and single-level.

**Required instance header fields**:
- Schema version (matches this governance rule's revision)
- Instance version (semver)
- Status (`Draft` / `Active` / `Superseded`)
- Created date, last updated date
- Owner
- Design language foundation declaration
- Accessibility stance declaration (must match §6 of this rule)
- Change log location (in-file §14 or external reference)
- **DS markdown export reference** — declared path or commit reference for the current export that populated the CC mirror; ensures mirror version traceability per §12.7

---

# 3. Implementation path rules

Governance over the implementation path is twofold:

**Rule 3.1 — Theme injection mechanism**: The corporate VI (visual identity) overrides MUST be applied at build time via Arco's `less-loader` `modifyVars` mechanism, not at runtime via imported CSS files. Runtime CSS overrides defeat tree-shaking, complicate dark-mode extension, and break the single-source-of-truth principle.

**Rule 3.2 — Single monorepo theme source**: There MUST be exactly one theme source for the project at `packages/hdc-corporate-theme/`. Per-app theme duplication (separate `hdc-corporate-theme.css` or `theme.less` files inside `apps/{app-slug}/src/frontend/themes/`) is forbidden.

**Rule 3.3 — No `@arco-themes/...` npm dependency**: The project deliberately avoids the `@arco-themes/...` npm package distribution mechanism in favor of monorepo-shared theme module per Rule 3.2.

**Rule 3.4 — PC + mobile library version pinning**: The instance MUST pin both `@arco-design/web-react` (PC) and `@arco-design/mobile-react` (mobile) to declared versions. Cross-app version drift is forbidden.

**Rule 3.5 — Custom component policy**: Components not in Arco standard are allowed only when (a) Arco does not provide a sufficient base, AND (b) the custom component is registered in the instance §4 component inventory as Tier B with a documented rationale.

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

## 4.2 Token consumption rules

**Rule 4.2.1**: All Tier 1 React code MUST consume tokens through Arco's theme system and corporate VI override. Hardcoded color, typography, or spacing values are forbidden outside Tailwind layout utilities (margin, padding, flex, grid layout-only).

**Rule 4.2.2**: Token names MUST follow the taxonomy in §4.1. Adding a new top-level token category requires governance review per §12 (breaking change).

**Rule 4.2.3**: New tokens within an existing category may be added via the §12 additive update flow.

**Rule 4.2.4**: Token values that diverge from Arco defaults MUST be motivated by corporate VI or HR-specific design need; recorded in the instance with rationale.

**Rule 4.2.5**: Enforcement is via ESLint rules and Tailwind config in CC substantive Code Quality Rule Set canonical §3.2; this rule declares the design-level rules, Code Quality Rule Set declares the tool-level enforcement.

---

# 5. Component governance

## 5.1 Tier A — Arco components used directly

Components imported from `@arco-design/web-react` (PC) or `@arco-design/mobile-react` (mobile) and used without wrapping or modification (except for token-driven theming).

**Rule 5.1.1**: Tier A components MUST be listed in the instance §4 component inventory with their canonical import path and PC/mobile cross-platform variant declaration.

**Rule 5.1.2**: Tier A components MAY be styled only via the token system (§4) and Arco's documented prop API. Custom CSS overrides on Tier A components are forbidden.

## 5.2 Tier B — HDC custom components

Components built on top of Arco primitives + tokens, specific to HDC's HR domain.

**Rule 5.2.1**: A component qualifies for Tier B only when: (a) it composes Arco primitives + tokens (does NOT use non-Arco third-party UI libraries), AND (b) it encapsulates HR-specific behavior or visual pattern that would otherwise be duplicated across slices, AND (c) it is registered in the instance §4 inventory with documented composition + props + a11y notes.

**Rule 5.2.2**: Each Tier B component MUST declare its PC + mobile variant policy (PC-only, mobile-only, or both with stated platform-specific differences if any).

**Rule 5.2.3**: A new Tier B component goes through the §12 additive update flow before being used in slice code.

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

HDC has **no formal WCAG conformance target**. The stance is engineering hygiene rules only, enforced via Arco component defaults and `eslint-plugin-jsx-a11y` at `warn` severity (per CC substantive Code Quality Rule Set canonical §1.2). On-demand validation via `hdc-wcag-accessibility-checker` skill is operator-triggered, not automated.

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

When a feature's UX Design Spec instance §2.5 flags a specific a11y concern (custom Tier B with non-standard interactions, complex flow that needs keyboard-only verification, screen with dense interactive content), the operator MAY invoke `hdc-wcag-accessibility-checker` skill manually. The skill wraps `axe-core` and produces a non-binding diagnostic report; findings are advisory.

The skill is NOT invoked at any milestone gate automatically. It is a utility, not a CI step.

## 6.4 Rationale for the stance

HR Digital Cockpit's user base is the internal workforce (employees, managers, HR/IT admin); the audience is known and reachable. The cost of pursuing formal WCAG conformance (audit overhead, certification cycles, edge-case retrofits for content the audience does not consume) is high relative to the benefit. Engineering hygiene via Arco defaults + jsx-a11y `warn` catches the vast majority of real accessibility issues without imposing certification burden.

This is a deliberate design choice, not a deferral. If regulatory or contractual requirements change (e.g., expansion to public-facing surfaces or jurisdictions with mandatory WCAG compliance), this section is the trigger for a breaking governance change per §12.

---

# 7. Internationalization & RTL governance

**Rule 7.1**: The instance MUST declare its launch-language set and locale codes (BCP 47).

**Rule 7.2**: RTL capability MUST be declared in the instance regardless of whether any launch language is RTL, so that future RTL additions do not require breaking governance changes.

**Rule 7.3**: All Tier 1 text MUST resolve via the i18n resource system; hardcoded user-facing strings in code are forbidden (lint-enforced per CC substantive Code Quality Rule Set canonical §3.5 if configured).

**Rule 7.4**: Text expansion budget — Tier 1 layouts MUST accommodate the longest declared launch language (typically German or French for European-language sets) with at least 30% width margin on dense labels (form field labels, table column headers, button text).

**Rule 7.5**: Date / time / number formats MUST follow user locale at display time; storage MUST use ISO 8601 (dates / times) and IEEE 754 (numbers) for cross-locale safety.

**Rule 7.6**: If a feature introduces a new launch language, the instance §7 i18n scope MUST be updated via §12 additive flow before slice code is merged.

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

Every feature's UX Design Spec instance §2.1 MUST declare which of these tiers the feature belongs to and the rationale:

- **Tier 1 — PC and mobile both first-class**: All employee-facing self-service flows, all manager-facing workflows that need both desktop convenience and mobile pickup (e.g., approvals).
- **Tier 2 — PC-primary, mobile read-only**: HR back-office workflows where mobile access is needed for visibility but not for action (e.g., dashboards, reports).
- **Tier 3 — PC-only**: Heavy admin tools, complex data grids, multi-pane analytics, configuration screens; show "use desktop" banner on mobile.

## 11.3 Mobile parity policy

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

---

# 12. Update flow (core governance)

## 12.1 Who can propose a change

- The project owner
- Hub Claude during hub-side specification production (the proposal originates from a Hub conversation — typically at TK-02 step 2.3 when authoring a UX Design Spec instance reveals a gap in current DS, or at TK-03 slice authoring when an interface need cannot be met); the change is then authored in CD where the instance lives

## 12.2 Change categories

- **Additive** (new component, new token, new locale, new layout pattern, new icon): proposed by Hub Claude in the feature's UX Design Spec instance §2.4 New-Components-Or-Tokens at TK-02 step 2.3 (Hub-authored markdown); the proposal travels via operator-mediated transfer to CD per [MECH] Cross-Tool Workflow Handoff §2.1 for CD-side instance authoring; the change merges into the DS instance (CD-side) when the originating feature's slice merges to main (see [MECH] Development Track Workflow TK-12); the CC mirror is re-synced from the reviewed DS markdown export after the CD-side change is finalized.
- **Breaking** (token value change, Arco major version upgrade, accessibility hygiene rule change, mobile-tier reassignment of existing screens, platform-tier downgrade of a feature already shipped): requires separate review gate outside the normal TK flow; all affected slices MUST be reviewed before rollout.

## 12.3 Change process

1. Proposer surfaces the need (in a Hub conversation during TK-02 step 2.3 UX Design Spec authoring, or in a Hub conversation during TK-03 slice authoring, or directly in a CD authoring session)
2. For additive changes: Hub Claude authors the change plan as a §2.4 entry in the feature's UX Design Spec instance (Hub-authored markdown at `apps/{app-slug}/specs/ux-design-spec/{feature-slug}.md`). For breaking changes: change is drafted in CD-native form as a standalone change file (CD-internal location)
3. **Governance-rule review** (Hub-side, against §3-§11 of this rule):
   - For additive: Hub Claude assists in checking conformance with §3-§11 during TK-02 step 2.3 when authoring the UX Design Spec instance; operator signs off as part of TK-02 sign-off
   - For breaking: a separate review gate is convened; Hub Claude assists in checking conformance against §3-§11 of this rule
4. Optional adversarial review via code review tool — operator transports the change to CC for the optional adversarial-review invocation if desired (specific code review tool governed by CC substantive Codex Plugin Usage canonical post-Phase-3). **Note**: this optional adversarial review for DS changes is independent from the M0 entry self-check at TK-04; the DS-change review here is a separate, optional governance-review pathway, distinct from any TK-sequence M0 / M4 review.
5. Project owner approves or rejects
6. If approved:
   - **CD-side authoring**: CD finalizes the change in the DS instance content. CD authors against the current DSG (transferred to CD as a read-only input per [MECH] Cross-Tool Workflow Handoff §2.1) and self-checks the finalized change against §2-§11 of this rule before export. The change is recorded in instance §14 change log
   - **DS markdown export regeneration**: CD generates an updated DS markdown export reflecting the new instance state per §12.7 export specification
   - **Export conformance review (Hub-side)**: the operator brings the CD-generated DS markdown export into a Hub conversation; Hub Claude reviews the export against the §15 reviewer checklist to confirm the finalized instance conforms to §2-§11 of this rule. This review catches divergence between the approved change plan and what CD actually authored, including any out-of-band CD change. On a material finding, the export returns to CD for correction
   - **CC mirror sync**: on a passing export review, the operator commits the reviewed export to the CC monorepo (`specs/design-system.md`) at the next sync point (additive: at the originating feature's merge-to-main milestone per §12.5; breaking: after CD-side breaking change is finalized at the separate review gate)

## 12.4 Change content minimum structure

A DS instance change (additive or breaking) MUST include:

- **Change identity**: change-id (kebab-case, stable within the change's lifecycle), change type (`additive` or `breaking`), proposer, proposal date, target instance version
- **Affected sections**: list the §x sub-sections of the instance this change touches
- **Proposed change content**: the specific additions or modifications. For additive changes, provide the draft §x entries ready to be merged into the instance. For breaking changes, provide both the current value and the proposed value
- **Rationale**: the business or design need motivating the change, traceable to the triggering feature's PRD or the Hub-authored UX Design Spec instance §2.4 when applicable
- **Backward-compatibility analysis** (required for `breaking`; optional for `additive`): list every currently-merged feature slice that uses the affected sections; state for each whether it is unaffected, requires re-review, or requires code change; when re-review or code change is required, state the estimated scope
- **Adversarial review reference** (optional): if a Codex adversarial review was invoked, link to or attach the resulting report
- **Approval status**: one of `pending` / `approved` / `rejected` / `deferred`; when approved, record the merge event (slice-id + merge date) that applied this change

For `additive` changes, the Hub-authored UX Design Spec instance §2.4 carries the change plan; CD authors the corresponding instance content change at merge time. For `breaking` changes, the proposer produces this content as a standalone change file (CD-internal location) and a separate review gate is convened before rollout per §12.2.

## 12.5 Merge timing

- **Additive merges**: at the originating feature's merge-to-main milestone (slice M4 → merge to `main`, per [MECH] Development Track Workflow TK-12 M4 gate). The DS instance content is finalized in CD; CD regenerates the DS markdown export; the export is reviewed Hub-side against §15 per §12.3; on a passing review the CC mirror (`specs/design-system.md`) is updated via operator-mediated transfer per [MECH] Cross-Tool Workflow Handoff.
- **Breaking merges**: as scheduled by the separate review gate. Affected slices are re-reviewed before the merge; back-propagation work is completed before the breaking change is rolled out; the CC mirror is updated after the CD-side breaking change is finalized and the export passes the §15 review.

## 12.6 Forbidden patterns

- Silent token or component additions in feature branches without instance update
- Custom components in slice code that duplicate existing Arco components
- Hardcoded color, typography, or spacing values in Tier 1 code outside Tailwind layout utilities
- Cross-platform divergence not declared in the instance §4 component inventory mapping table
- **Updates to the CC mirror** (`specs/design-system.md`) without a corresponding CD-side SOT update — the CC mirror is read-only and synced from CD via the reviewed DS markdown export; direct edits create drift between SOT and mirror that CC will operate against incoherently at code generation

## 12.7 DS markdown export specification

The DS markdown export is the canonical artifact that propagates DS instance content from CD SOT to the CC mirror. It is produced by CD on operator prompt at every change finalization (additive merge or breaking-change finalization) and at workspace inception (initial DS setup).

**Content requirement**: The DS markdown export MUST faithfully represent the DS instance content covering all §2 required section topics (§1 Design language foundation through §14 Change log). For each topic:
- **§3 Design tokens**: List all tokens by taxonomy category with specific values (e.g., `primary: #1664FF`, `spacing-md: 16px`) and any per-token rationale.
- **§4 Component inventory**: Full list of Tier A (Arco direct), Tier B (HDC custom), Tier C (forbidden) with canonical import paths, PC/mobile variant declarations, and any composition/a11y notes for Tier B components.
- **§5 Layout patterns**: Full pattern catalog with names, applicable HR scenarios, PC/mobile mappings.
- **§6 Accessibility stance**: Per §6 of this rule; restated in instance.
- **§7-§10**: i18n locale list + RTL declaration, motion principles, iconography sources, content style rules.
- **§11 Platform tier**: T1/T2/T3 framework restated.
- **§12-§14**: Governance pointer to this rule, custom skill integration list, change log.

**Format requirement**: Markdown with stable section anchors (`## §X.Y`) for AI-RAG consumption. Tables for token lists, component inventories, breakpoints. No proprietary CD-internal markup; the export is portable text.

**Versioning**: The export MUST declare the instance version in its header. The CC mirror file `specs/design-system.md` carries the export content with matching version metadata.

**Generation mechanism**: Operator prompts CD to generate the export at each §12.5 sync point. The prompt should request a structured markdown summary covering all §2 topics; CD produces it from the SOT instance content.

**Transfer mechanism**: The operator brings the CD-generated markdown into a Hub conversation for the §12.3 export conformance review; on a passing review, the operator commits it to the CC monorepo per [MECH] Cross-Tool Workflow Handoff.

---

# 13. Custom skill integration and Hub consumption

The DS instance is consumed at two Claude Code runtime surfaces (`hdc-arco-enterprise-ui` and `hdc-wcag-accessibility-checker` skills, both reading the CC mirror). Hub Claude does not consume the DS instance — at TK-02 step 2.3 it consumes CD-authored design files and reviews the DS markdown export. Their respective contracts with this rule:

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
- ESLint `eslint-plugin-jsx-a11y` at `warn` severity (per CC substantive Code Quality Rule Set canonical §1.2) is the routine a11y check, not this skill.
- Skill source: `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md`
- The skill name retains "wcag" for stable identifier; functionally it is an a11y diagnostic tool.

These skills are hub-designed specification outputs, not Claude Code runtime artifacts in the canonical sense. They are updated alongside this rule via the §12 governance process when applicable.

## 13.3 Hub-side consumption discipline (TK-02 step 2.3 + export review)

Hub holds no DS instance copy. Hub holds this governance rule (DSG) and consumes CD-authored design files and the CD-generated DS markdown export as transient inputs. Hub-side discipline covers three activities:

- **Design file quality check (spec-readiness)**: When the operator transfers CD-authored design files to the Hub session, Hub Claude verifies the design files are spec-ready — complete against the feature's PRD/TDD scope (all required screens, states, and flows covered), internally consistent, and carrying annotations rich enough to author the UX Design Spec instance from. This check uses the PRD/TDD (which Hub holds) and the design files themselves; it does not check DS-conformance against a DS mirror. DS-conformance of the design files is CD's responsibility — CD authored them holding the DS instance. A design file introducing a component / token not yet in the DS is a legitimate §12 additive proposal, not a defect; Hub Claude captures it as a UX Design Spec §2.4 entry. Findings are surfaced to the operator per [TPL] UX Design Spec §3 reviewer checklist.
- **UX Design Spec authoring grounding**: When Hub Claude authors the per-feature UX Design Spec instance markdown (after the design file quality check passes), it grounds component / token / pattern claims in the **CD-authored design files** — every `component: <name>` reference in the UX Design Spec is transcribed from a component callout in the design files (which CD, as DS owner, authored using the DS instance). Hub does not hold an independent DS copy to cross-check against; the design file is the authoritative input. CC verifies the UX Design Spec's references against the CC mirror at TK-04 M0 entry via SK-F, and CC code generation is the downstream backstop for any non-canonical reference.
- **Export conformance review**: When CD finalizes a DS instance change and generates a DS markdown export (§12.3 step 6), the operator brings the export into a Hub conversation. Hub Claude reviews the export against the §15 reviewer checklist to confirm the finalized instance conforms to §2-§11. This is the cross-workspace conformance gate — it catches divergence between the approved change plan and what CD authored, and any out-of-band CD change — before the export reaches the CC mirror.

These are not "skills" in the CC sense (Hub Claude does not load `.claude/skills/`); they are consumption disciplines applied directly by Hub Claude during conversation. Hub Claude holds DSG at runtime, so the disciplines track this rule automatically when it changes.

---

# 14. Pairing rules

## 14.1 Pairing with UX Design Spec instances

Every feature's UX Design Spec instance (Hub-authored markdown at TK-02 step 2.3 when `tier_1_involved=true` per `[TPL] UX Design Spec`) MUST reference the current DS instance version (recorded in the CD-authored design files at the time of authoring) and declare the platform tier (per §11.2) the feature targets. If a feature introduces a new component, token, or layout pattern, the UX Design Spec instance §2.4 New-Components-Or-Tokens MUST include an update plan (per §12.4 change content structure); this triggers the §12 additive flow with CD-side authoring of the actual instance content change.

The Hub-authored UX Design Spec instance is grounded in the CD-authored design files per §13.3 consumption discipline.

## 14.2 Pairing with intent.md UX brief

Each slice's intent.md MAY include a UX brief section listing screens and components used. The components referenced MUST exist in the instance §4 component inventory (Tier A or Tier B); platform coverage (PC, mobile, both) MUST be stated. Hub Claude authors the intent.md UX brief at TK-03 by extracting from the slice-relevant subset of the feature's UX Design Spec instance (which was itself authored at TK-02 step 2.3 grounded in the CD-authored design files) — the chain of grounding ensures slice-level UX brief content is DS-compliant.

## 14.3 Pairing with test-plan.yaml

`test_type: accessibility` cases in per-slice test-plan.yaml are **optional** per §6.2. When a slice's UX Design Spec instance declares specific a11y considerations beyond what Arco defaults provide, the slice's test plan MAY include such cases; otherwise the type is not required. There is no automated a11y gate at any milestone.

## 14.4 Pairing with Tier 1 code

All Tier 1 React code references design tokens (§4) and component inventory (§5). The `hdc-arco-enterprise-ui` skill enforces this at code generation time by reading the CC mirror; compliance-checker (A9) audits at M4. Lint-level enforcement of the same rules is owned by CC substantive Code Quality Rule Set canonical §3.

## 14.5 Pairing with custom skills

Skills §13.1 and §13.2 consume the CC mirror of the DS instance plus this rule's content. Hub Claude §13.3 consumes CD-authored design files plus this rule's content. When this rule or the instance is updated (additive or breaking), the skills may need prompt adjustment and the Hub consumption discipline tracks automatically. This is a paired-update relationship (P-19 in [OS] §8.5.2).

## 14.6 Pairing with CC substantive Code Quality Rule Set canonical (post-Phase-3)

**Pairing status note**: P-34 (was: DSG ↔ [MECH] Code Quality Rule Set lint rules) was **RETIRED in Phase 3** per [REF] Hub-CD-CC §5.4.4 — counterparty CQ fully migrated to CC substantive canonical. The substantive alignment between DSG design-level rules and CC-side lint enforcement is now governed at CC's discretion under the decoupled-reference model.

CC substantive Code Quality Rule Set canonical declares the runtime and build-time tool-level enforcement of Tier 1 visual rules. Token-consumption rules in §4 and component-inventory rules in §5 of this Hub-side DSG canonical are implemented as ESLint rules and dependency-cruiser rules per CC substantive CQ canonical §3.2 and §3.3. The accessibility recommendations in §6.1 map to `eslint-plugin-jsx-a11y` rules in CC substantive CQ canonical §1.2 at `warn` severity (advisory only). When this rule changes the design-level rules, the operator notifies CC for CC-side substantive CQ to update under CC's own discipline; no Hub-side P-NN pairing tracks this Hub↔CC coordination.

---

# 15. Reviewer checklist (for DS instance updates)

Before signing off an instance update (additive merge at slice M4 / breaking review gate), verify:

1. Design language foundation rationale references actual HDC context, not generic reasoning
2. Implementation path specifies both PC and mobile library version pin and custom component policy; corporate VI primary color and font stack are declared; theme injection mechanism is explicitly the build-time `less-loader` `modifyVars` path (not a runtime CSS file or `@arco-themes/...` npm package); single monorepo theme source at `packages/hdc-corporate-theme/`
3. Token section lists all custom HDC tokens with VI source values and justification
4. Component inventory is MECE on both PC and mobile; Tier C forbidden list is explicit; cross-platform mapping is complete
5. Layout-pattern mapping covers all major HDC HR scenarios on both PC and mobile
6. Accessibility section explicitly states "no formal WCAG conformance target", lists the recommendations, and confirms enforcement via Arco defaults + jsx-a11y at warn (no CI a11y gate)
7. i18n declares RTL capability requirement regardless of launch languages
8. Platform tiers (T1/T2/T3) are declared and the instance lists tier defaults
9. Skill integration lists both `hdc-arco-enterprise-ui` and `hdc-wcag-accessibility-checker`; Hub-side consumption discipline per §13.3 is referenced
10. Governance section in the instance references this rule's §12 process
11. No duplication with PRD, UX Design Spec, intent, acceptance scope
12. The CC mirror (`specs/design-system.md`) has been re-synced from the reviewed DS markdown export after the update; mirror version metadata matches the CD-side declared instance version
13. DS markdown export per §12.7 was generated for this update and is referenced in the instance header

If 2+ items are materially weak, the instance update is not yet ready for sign-off.

---

# 16. Anti-drift red flags

Red flags that should trigger correction:

- Tier 1 code using hardcoded colors, spacing, or typography values (outside Tailwind layout utilities)
- VI overrides applied via runtime CSS files (e.g., `theme.css` imported at app entry) instead of build-time `less-loader` `modifyVars` per §3.1 — runtime CSS overrides defeat tree-shaking, complicate dark-mode extension, and break the single-source-of-truth at `packages/hdc-corporate-theme/`
- An `@arco-themes/...` npm package introduced as a dependency — the project deliberately avoids this distribution mechanism in favor of monorepo-shared theme module per §3.3
- Per-app theme duplication (separate `hdc-corporate-theme.css` or `theme.less` files inside `apps/{app-slug}/src/frontend/themes/`) instead of the single monorepo `packages/hdc-corporate-theme/` source per §3.2
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
- **The CC mirror edited directly without corresponding CD-side SOT update** — the CC mirror at `specs/design-system.md` is read-only and synced from CD via the reviewed DS markdown export; direct edits create drift between SOT and mirror that CC will operate against incoherently at code generation
- **A Hub-side DS instance mirror re-introduced** (a `hdc_ref_*` DS instance copy, or DS instance content inlined into a Hub canonical source or PI) — the two-way model in §1.1 deliberately holds no DS instance copy at Hub; re-introducing one is drift back toward the retired three-way model and re-incurs the lock-step synchronization burden §1.1 removed
- **Hub Claude in TK-02 step 2.3 authoring the UX Design Spec instance without grounding in the CD-authored design files** — component / token / pattern claims must be transcribed from the design files' callouts per §13.3; ungrounded authoring produces UX Design Spec instances that may reference nonexistent or misnamed DS elements
- **DS markdown export not regenerated at §12 change finalization** — instance content updated in CD SOT but no export produced, leaving the CC mirror stale relative to SOT
- **CC mirror sync bypasses the §15 export review or the operator-mediated transfer** — the CC mirror must be updated only from a DS markdown export that passed the §12.3 export conformance review; a direct CD-to-mirror push bypassing the review or the operator audit violates §12.3 and [MECH] Cross-Tool Workflow Handoff operator-audit discipline
