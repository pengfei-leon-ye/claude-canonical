# [REF] CC Project Memory Bank Layout

- **Project**: HR Digital Cockpit
- **Document Type**: Reference Catalog
- **Status**: Active canonical
- **Role**: Canonical reference defining the file layout for CC-internal canonical content — the 5-level CLAUDE.md hierarchy and the `.claude/` directory structure (rules, agents, commands, skills, hooks) — including paths, naming conventions, indexing, and update discipline
- **Source Category**: Cat 4
- **Management-System Role**: Reference catalog source; outside L1-L5 hierarchy; not itself an L2–L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; subject to [OS] §8.5 paired-update consistency. The hub-to-CC visibility boundary in [OS] §1.4 applies — this source describes the layout of CC-side files but does not mirror their content into hub canonical.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control) — layout discipline is a management mechanism.
- **Relationship to [REF] Hub-CD-CC Architecture**: Consumed by §4.3 (CC workspace's canonical outputs). This source describes the layout; [REF] Hub-CD-CC Architecture frames why those files exist (the CC workspace's identity).
- **Relationship to [RULE] Claude Code Architecture Rules**: Companion. CCAR owns the substantive rules (subagent roster + scopes + tier architecture + path-scoped rules). This source owns the layout (where files live, how named). CCAR may reference this source for layout details; this source references CCAR for substantive content authority.
- **Relationship to [RULE] Workspace Topology**: Different scope. WT owns the multi-node dev environment layout (machines, tools, GitHub workflow); this source owns CC-internal file layout within a single working directory.
- **Relationship to [MECH] Development Track Workflow**: DTW TKs read CC-internal canonical content following this source's layout (e.g., subagent definitions at `.claude/agents/`, skills at `.claude/skills/`); DTW does not author layout, only references it.
- **Relationship to [MECH] CI/CD Milestone Policy**, [MECH] Code Quality Rule Set, [MECH] Dev-Loopback Mode: These sources govern runtime artifacts that may reference layout paths defined here; they do not author layout.
- **Pairings I participate in**: None (Tier B couplings documented in counterparty source `Relationship to [REF] CC Project Memory Bank Layout` header fields per [OS] §8.5.1a)

## How to use this source

Use this source when:
- Creating a new CC-internal canonical file (subagent, skill, command, hook, rule)
- Adding a new CLAUDE.md to a hierarchy level
- Diagnosing why an agent cannot find an expected file
- Onboarding a new app into the monorepo (per-app CLAUDE.md instantiation)
- Reviewing whether a proposed file location conforms to canonical layout
- Identifying the canonical path for a class of file when authoring spec or rule content

Do not use this source as:
- A substantive rule reference for what subagents do ([RULE] Claude Code Architecture Rules §5)
- A skill catalog ([RULE] Claude Code Architecture Rules §Z)
- A repository layout reference for monorepo-level structure ([RULE] Claude Code Architecture Rules §Y.1)
- A multi-node dev environment layout ([RULE] Workspace Topology)
- A runtime artifact governance reference (respective [MECH] sources)

## Scope note

This source describes the layout (paths, naming, structure) of CC-internal canonical files. Substantive content rules — what each file should contain, what behavior it should govern — live in their respective canonical sources ([RULE] CCAR, [MECH] DTW, [MECH] CI/CD, etc.).

This source applies to files within a single CC working directory (a single node's checkout of the monorepo). It does not address how the same layout replicates across multiple dev nodes — that is [RULE] Workspace Topology §4.4 parity discipline.

---

# 0. Boundary and position

## 0.1 What this source owns

- The 5-level CLAUDE.md hierarchy: identity, path, scope, and content category for each level
- The `.claude/` directory layout: structure of `rules/`, `agents/`, `commands/`, `skills/`, `hooks/` sub-directories
- Naming conventions for files within `.claude/` and CLAUDE.md instances
- File indexing and discovery rules (how AI agents locate canonical files within the working directory)
- Update discipline for layout changes (when a new file is added, when a file is renamed, when a file is removed)
- Anti-drift red flags specific to layout discipline

## 0.2 What this source does not own

- Substantive content of CC-internal canonical files (owned by [RULE] CCAR for subagent / skill / hook / rule definitions)
- Subagent permission scopes ([RULE] CCAR §X)
- Subagent roster definition ([RULE] CCAR §5.1)
- Skill loading rules ([RULE] CCAR §Z)
- Monorepo-level layout outside `.claude/` and CLAUDE.md hierarchy ([RULE] CCAR §Y.1)
- Multi-node parity for `.claude/` files ([RULE] Workspace Topology §4.4)
- Build / lint / test config file layout ([MECH] Code Quality Rule Set, [MECH] CI/CD Milestone Policy)
- App / domain code layout ([RULE] CCAR §Y.1, §Y.4)
- Hub-side canonical layout ([OS] §10, §9)

## 0.3 Position relative to adjacent canonical sources

| Adjacent source | Relationship |
|---|---|
| [OS] | Operates within [OS] §7.1 routing. [OS] §1.4 hub-to-CC visibility boundary applies — Hub canonical does not mirror CC-internal file content. |
| [REF] Hub-CD-CC Architecture | Consumed by §4.3 (CC canonical outputs inventory). |
| [RULE] Claude Code Architecture Rules | Substantive authority. CCAR owns the rules; this source owns the layout. |
| [RULE] Workspace Topology | Different scope. WT layout is multi-node + dev environment; this source is within-node CC-internal. |
| [RULE] Codex Plugin Usage | References this source's layout when invoking Codex commands in CC sessions. |
| [RULE] Design System Governance | References DS code layout (in CC monorepo); this source frames CC-internal canonical layout, not code layout. |
| [MECH] Development Track Workflow | Consumes layout for TK inputs / outputs / artifact paths. |
| [MECH] CI/CD Milestone Policy | References this source for `.claude/` layout when CI workflows interact with CC-internal canonical. |
| [MECH] Code Quality Rule Set | References this source for `.claude/rules/` placement of code-quality rule files. |
| [MECH] Dev-Loopback Mode | References this source for fixture / placeholder file placement (separate from this source's layout, but co-resident in the working directory). |
| [MECH] Cross-Tool Workflow Handoff | References this source when CC-side canonical changes are notified back to Hub for index sync (§3.2 CC → Hub direction). |

---

# 1. The CLAUDE.md hierarchy

CLAUDE.md files are the persistent context anchors loaded by Claude Code at session start and on cross-hierarchy file access. The hierarchy has 5 levels mapped to the monorepo structure.

## 1.1 Level 1: Project root CLAUDE.md

**Path**: `HDC_ROOT/CLAUDE.md`

**Load timing**: Loaded at the start of every CC session.

**Responsibility**: Workspace-wide rules, tech stack declaration, milestone policy reference, testing policy reference, Codex plugin usage reference, skill loading declaration, agent roster reference, multi-app and multi-domain organization rules, multi-node deployment reference.

**Must reference**:
- [RULE] Claude Code Architecture Rules
- [RULE] Workspace Topology
- [MECH] Development Track Workflow
- [MECH] CI/CD Milestone Policy
- [RULE] Codex Plugin Usage
- [MECH] Application Lifecycle Handoff
- `specs/design-system.md` as CC mirror of the DS instance (per [RULE] DSG §1.1 three-way distribution model; the DS instance SOT lives in CD)
- `.claude/skills/hdc-arco-enterprise-ui/SKILL.md` (SK-F) and `.claude/skills/hdc-wcag-accessibility-checker/SKILL.md` (SK-W)

**Authoring authority**: Hub-authored constitutional intent; CC-instantiated based on Hub canonical. Produced as part of workspace inception per [RULE] Workspace Topology §10.

## 1.2 Level 2: App root CLAUDE.md

**Path**: `apps/{app-slug}/CLAUDE.md`

**Load timing**: Loaded when CC enters any path under `apps/{app-slug}/`.

**Responsibility**: App-level scope declaration, app-specific tech stack notes, app-scoped specs location, intra-app tier boundary clarifications.

**Contents**:
- App identity (`app-slug` value, app name, app description)
- App-specific dependencies (when an app pins a different version of a shared library than another app, declare it here)
- App-scoped specs location reference (`apps/{app-slug}/specs/**`)
- App-scoped evidence and reports location reference (`apps/{app-slug}/evidence/**`, `apps/{app-slug}/reports/**`)
- Tier 1 and Tier 2 boundaries for this app (cross-reference [RULE] CCAR §1.1, §1.2)
- Domain consumption list for this app (which `packages/domain/{domain-name}/` packages this app's BFF consumes; cross-reference [RULE] CCAR §Y.4 contract testing convention)

**Authoring authority**: Produced as part of the Phase 1 walking_skeleton unit's output set per [RULE] Workspace Topology §4.6.3. The app root CLAUDE.md does not redefine tier boundaries or permission rules; it scopes them to the app and references the canonical definitions in [RULE] CCAR.

## 1.3 Level 3: App frontend CLAUDE.md

**Path**: `apps/{app-slug}/src/frontend/CLAUDE.md`

**Load timing**: Loaded when CC enters `apps/{app-slug}/src/frontend/**`.

**Responsibility**: Tier 1 React layer boundary enforcement within the app.

**Contents**:
- Scope of Tier 1 responsibilities (per [RULE] CCAR §1.1)
- Prohibited activities in Tier 1
- API consumption rules (Tier 1 calls only the same app's Tier 2; never directly calls Tier 3 across `packages/domain/`)
- State management scope
- Testing requirements for Tier 1
- Reference to the CC mirror `specs/design-system.md` as mandatory design constraint (the mirror is read-only at CC per [RULE] DSG §1.1; updates flow from CD SOT)
- Reference to `hdc-arco-enterprise-ui` skill (SK-F) as runtime enforcement

**Authoring authority**: Produced as part of the walking_skeleton output set; subsequent updates as Tier 1 surface evolves per app.

## 1.4 Level 4: App BFF CLAUDE.md

**Path**: `apps/{app-slug}/src/bff/CLAUDE.md`

**Load timing**: Loaded when CC enters `apps/{app-slug}/src/bff/**`.

**Responsibility**: Tier 2 Node/TS layer boundary enforcement within the app.

**Contents**:
- Scope of Tier 2 responsibilities (per [RULE] CCAR §1.2)
- Prohibited activities in Tier 2
- Integration patterns with Tier 3 (consumes domain APIs from `packages/domain/{domain-name}/`)
- Caching boundaries
- Testing requirements for Tier 2
- Consumer-side contract authoring per [RULE] CCAR §Y.4 (this BFF authors `apps/{app-slug}/tests/contract/{app-slug}-bff_{domain-name}/**` Pact contracts)

**Authoring authority**: Produced as part of the walking_skeleton output set; subsequent updates as BFF surface evolves.

## 1.5 Level 5: Domain root CLAUDE.md

**Path**: `packages/domain/{domain-name}/CLAUDE.md`

**Load timing**: Loaded when CC enters `packages/domain/{domain-name}/**`.

**Responsibility**: Tier 3 Java layer boundary enforcement at the domain package root.

**Contents**:
- Scope of Tier 3 responsibilities (per [RULE] CCAR §1.3)
- Core responsibilities of Tier 3 as authoritative tier
- Data permissions ownership
- Transaction boundaries
- API contract stability rules
- Integration patterns
- Testing requirements for Tier 3
- Producer-side contract verification per [RULE] CCAR §Y.4 (this domain verifies the consumer contracts authored by app BFFs in `packages/domain/{domain-name}/tests/contract-verification/**`)
- Domain consumer list (which apps' BFFs currently consume this domain; informational, kept in sync with consuming app CLAUDE.md files)

**Authoring authority**: Produced when the domain is introduced (first feature unit consuming the domain); evolved when the domain's surface or consumers change.

## 1.6 Cross-level navigation discipline

CLAUDE.md files do not duplicate content from other levels. They reference upward (e.g., app root references project root for monorepo conventions) and forward (e.g., app root references its tier-level CLAUDE.md files for tier specifics). The discipline:

- Each level owns its scope; cross-level overlap is anti-drift
- Forward references use relative paths (e.g., `./src/frontend/CLAUDE.md` from app root)
- Upward references can name the parent level without exhaustive copying
- The 5-level hierarchy is not extensible — adding a 6th level requires canonical revision

---

# 2. The `.claude/` directory layout

The `.claude/` directory at the monorepo root holds runtime configuration for Claude Code. Its sub-directories are:

```
.claude/
├── rules/
├── agents/
├── commands/
├── skills/
└── hooks/
```

Each is a distinct content category with its own discipline.

**On-demand creation principle**: The five sub-directories (`rules/`, `agents/`, `commands/`, `skills/`, `hooks/`) are populated **on-demand** as specific rules, agents, commands, skills, or hooks are introduced by canonical governance ([RULE] CCAR for agents and skills; [MECH] DTW for hooks; etc.). The layout itself does not require pre-seeding files — empty subdirectories are valid initial state; subdirectories may even be absent at first inception and created when the first artifact lands. This deliberate emptiness keeps CC working state legible (only artifacts in active use exist) and avoids the anti-pattern of pre-designing artifacts whose triggers do not yet exist.

## 2.1 `.claude/rules/`

**Purpose**: Path-scoped rules that fire when CC operates within specific paths.

**Path pattern**: `.claude/rules/{rule-name}.md` (kebab-case, scoped per rule purpose)

**Content category**: Conditional behavior modifiers tied to specific working-directory paths. Rules are loaded by Claude Code when the working context matches the rule's declared path scope.

**Authoring authority**: Substantive rule content per [RULE] CCAR (specific rule definitions). Layout (file path, naming) per this source.

**Frontmatter `paths:` matching example**: each rule file declares its path scope via YAML frontmatter at the top:

```yaml
---
paths:
  - "apps/*/src/frontend/**"
  - "apps/*/src/frontend/**/*.tsx"
---

# Rule body (path-scoped to Tier 1 React frontend code)

Rule content here applies only when CC's working directory matches one of the
declared paths. Multiple path patterns are OR-combined; the rule fires if any
pattern matches the current working context.
```

Path patterns use glob syntax (`**` matches any depth; `*` matches any single path segment). Patterns SHOULD anchor to canonical repo paths from [RULE] CCAR §Y.1 (e.g., `apps/*/src/frontend/**` for Tier 1; `apps/*/src/bff/**` for Tier 2; `packages/domain/*/src/**` for Tier 3). Wildcard usage broader than necessary is an anti-drift signal — rules should declare the narrowest scope that captures their intent.

## 2.2 `.claude/agents/`

**Purpose**: Subagent definitions (the A1-A10 roster).

**Path pattern**: `.claude/agents/{agent-name}.md`

**Content category**: Per-subagent context scope, permission set, invocation conditions, output contract.

**Authoring authority**: Subagent roster definition owned by [RULE] CCAR §5.1; each agent's content discipline owned by [RULE] CCAR §X (scopes) + §5 (roster); layout (file path, naming) per this source.

**Naming convention**: kebab-case, descriptive of the agent's role (e.g., `test-writer-whitebox.md`, `rca-reporter.md`, `domain-judge.md`).

## 2.3 `.claude/commands/`

**Purpose**: Custom command implementations callable from CC sessions.

**Path pattern**: `.claude/commands/{command-name}.md`

**Content category**: Command invocation surface, expected inputs, behavior contract.

**Authoring authority**: Substantive command logic per [RULE] CCAR or [RULE] Codex Plugin Usage; layout per this source.

**Naming convention**: kebab-case, prefixed by command category when applicable.

## 2.4 `.claude/skills/`

**Purpose**: Custom skill definitions auto-loaded based on declared triggers.

**Path pattern**: `.claude/skills/{skill-name}/SKILL.md`

**Subdirectory structure**: Each skill is a directory containing its `SKILL.md` plus any supporting files (e.g., prompt templates, reference materials).

**Content category**: Skill's purpose, load triggers, prompt content, scope.

**Authoring authority**: Substantive skill content per the SKILL.md itself; layout discipline per this source; canonical governance per [RULE] CCAR §Z.

**Naming convention**: kebab-case, prefixed `hdc-` for HDC project-specific skills (e.g., `hdc-arco-enterprise-ui`, `hdc-wcag-accessibility-checker`).

## 2.5 `.claude/hooks/`

**Purpose**: Lifecycle hooks that fire on Claude Code events (PostToolUse, SubagentStop, Stop, Notification).

**Path pattern**: `.claude/hooks/{hook-name}.md` or `.claude/hooks/{event-type}/{hook-name}.md` (grouped by event type when many hooks accumulate)

**Content category**: Hook firing condition, action sequence, failure routing.

**Authoring authority**: Hook content per [RULE] CCAR / [MECH] DTW (hook is the implementation mechanism for various TKs' transitions); layout per this source.

**Naming convention**: kebab-case, descriptive of the hook's purpose.

---

# 3. Naming conventions

## 3.1 General principles

- All file and directory names use kebab-case (lowercase, hyphen-separated)
- ASCII only; no Unicode in canonical file names
- English only; no localized file names
- Names should be descriptive enough that purpose is clear without opening the file
- Project-specific files prefix with `hdc-` (e.g., `hdc-arco-enterprise-ui`); generic files do not require the prefix

## 3.2 Reserved names

- `CLAUDE.md` is reserved for memory-bank files at every hierarchy level
- `SKILL.md` is reserved for skill manifest files within `.claude/skills/{skill-name}/`
- Single-letter prefixes (e.g., `A1`, `SK-F`, `CX`) are reserved as canonical role codes per [MECH] DTW §2; they are not used as file names

## 3.3 Frozen names

Once a file enters the canonical inventory, its name is frozen except for renames executed under [OS] §8.5.2 same-revision discipline. This applies to:
- All CLAUDE.md files in the 5-level hierarchy
- All `.claude/agents/*.md` files (subagent identity tied to file name)
- All `.claude/skills/{skill-name}/` directories (skill identity tied to directory name)

Renaming a frozen file is a significant change requiring revision of any source that references the file by name.

---

# 4. Indexing and discovery

## 4.1 CLAUDE.md auto-discovery

Claude Code automatically discovers CLAUDE.md files at the hierarchy levels described in §1. No explicit registration is required; the file's presence at the canonical path is sufficient.

When CC navigates the working directory, it loads CLAUDE.md files according to the file's hierarchy level and the active path:
- Project root CLAUDE.md: always loaded at session start
- App root CLAUDE.md: loaded when working directory enters `apps/{app-slug}/`
- Tier-level CLAUDE.md: loaded when working directory enters the tier path
- Domain root CLAUDE.md: loaded when working directory enters `packages/domain/{domain-name}/`

## 4.2 `.claude/` content discovery

`.claude/` content is discovered by Claude Code on session start. Specifically:
- Agents in `.claude/agents/` are registered as invocable subagents
- Skills in `.claude/skills/` are loaded based on their declared triggers (per SKILL.md description fields)
- Hooks in `.claude/hooks/` are registered for their declared event types
- Commands in `.claude/commands/` are registered as callable from CC sessions
- Rules in `.claude/rules/` are loaded conditionally based on working-directory path

## 4.3 Cross-reference resolution

When a canonical source or a CC-internal file references another file by name (e.g., "[RULE] CCAR §5.1 lists subagent A5 (unit-test-auto-repair)"), the reference resolves via this layout source's naming conventions:
- Subagent names match `.claude/agents/{name}.md`
- Skill names match `.claude/skills/{name}/`
- Hook names match `.claude/hooks/{name}.md`

This resolution is mechanical; cross-references that do not resolve under this discipline are anti-drift signals per §6.

---

# 5. Update discipline

## 5.1 Adding a new file

When a new CC-internal canonical file is created:

1. Determine the file's content category (CLAUDE.md / rule / agent / command / skill / hook)
2. Compute the canonical path per §1 / §2
3. Author the file at the canonical path
4. Update any canonical source that should reference the new file (per [OS] §8.5.2 paired-update discipline)
5. Verify cross-reference resolution per §4.3

## 5.2 Modifying an existing file

Most file modifications affect substantive content, not layout. Substantive content modifications are governed by the file's authoritative canonical source (e.g., [RULE] CCAR for subagent content). This source's discipline applies only to layout-level changes:
- Path change (rename / move): see §5.3
- Naming convention change: see §5.3
- Content scope change: refer to the authoritative canonical source

## 5.3 Renaming or moving a file

Renaming or moving a CC-internal canonical file is a significant change that:
1. Requires updating every canonical source that references the file by name
2. Requires updating any CLAUDE.md cross-references to the file
3. Requires `git mv` rather than delete-then-add (preserves history)
4. Is recorded in the relevant canonical source's revision history

## 5.4 Removing a file

When a CC-internal canonical file is removed (e.g., a deprecated subagent):
1. Confirm no canonical source still references the file by name
2. Confirm no CLAUDE.md cross-references the file
3. Confirm runtime behavior (e.g., hook chain, skill loading) does not depend on the file
4. Remove the file with `git rm`
5. Update the canonical source that previously authoritatively referenced the file (if any) to remove the reference

## 5.5 Multi-node parity

When a CC-internal canonical file is added, modified, renamed, or removed, the change applies uniformly across all dev nodes per [RULE] Workspace Topology §4.4 parity discipline. Node-level divergence in CC-internal canonical files is a [RULE] WT §7 anti-drift signal, not regulated by this source.

---

# 6. Anti-drift red flags

> **Scope**: this section enumerates **layout-specific** anti-drift red flags. Cross-cutting red flags whose canonical statement lives elsewhere are referenced inline rather than duplicated. See [RULE] Claude Platform Behavior §5 for the full anti-drift ownership index.

**Path discipline dimension**:
- CLAUDE.md file at a path not matching the 5-level hierarchy in §1
- A 6th level CLAUDE.md introduced (the hierarchy is not extensible without canonical revision)
- `.claude/agents/`, `.claude/skills/`, etc., at a path other than `.claude/`
- Skill definition outside `.claude/skills/{skill-name}/` (e.g., bare `.claude/skills/{name}.md` without enclosing directory)
- Agent definition with `.md` extension missing or with different extension

**Naming dimension**:
- snake_case, camelCase, or PascalCase file names within `.claude/` or CLAUDE.md hierarchy (anti-drift against §3.1 kebab-case discipline)
- Non-ASCII or non-English file names
- `hdc-` prefix missing on project-specific skills
- Subagent file name not matching subagent identity referenced in [RULE] CCAR §5.1
- Reserved name (`CLAUDE.md`, `SKILL.md`) used at a non-canonical path

**Cross-reference dimension**:
- Canonical source references a file by name that does not exist at the layout-prescribed path
- Cross-reference to a file using a non-canonical path (e.g., absolute path when relative is expected, or vice versa)
- Stale reference to a renamed or removed file

**Update discipline dimension**:
- File renamed via delete-then-add instead of `git mv` (loses git history)
- New file added without updating referencing canonical sources per §5.1 step 4
- Removed file's references still present in other canonical sources

**Content category dimension**:
- Rule content placed in `.claude/agents/` or vice versa (content-category leakage)
- Substantive subagent rules duplicated in CLAUDE.md (CLAUDE.md is for navigation and conventions, not for subagent definitions)
- Skill manifest content split across multiple SKILL.md files (each skill has exactly one SKILL.md)

**Multi-node parity dimension** (cross-reference [RULE] WT §7):
- A CC-internal canonical file present on one dev node but missing on another
- File at different paths on different nodes (paths must match across nodes)
- File content divergent across nodes (per [RULE] WT §4.4 parity discipline)
