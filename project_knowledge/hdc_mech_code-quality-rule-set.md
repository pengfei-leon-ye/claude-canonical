# [MECH] Code Quality Rule Set

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable source defining the code quality rule set across all three tiers (Tier 1 React frontend, Tier 2 Node BFF, Tier 3 Java domain), declaring the authoritative tool stack, rule presets, custom architecture rules, AI-era specific augmentations (including pre-handoff security tooling: secret scanning, light SAST, SCA), severity policy, CI/CD pipeline integration, Renovate dependency-update governance, and governance for rule-set evolution
- **Source Category**: Cat 4
- **Management-System Role**: Governance mechanism specification; outside L1-L5 hierarchy; not itself an L2-L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; classified as a [MECH] family source per [OS] §9.2 / §10.4 (governance mechanism specification, distinct from [RULE]). Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design).
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. CQ defines deterministic code-quality checks that fire in the CC workspace; Hub-CD-CC Architecture frames why CC is the implementation pillar where these checks run.
- **Relationship to [RULE] Claude Code Architecture Rules**: Co-governing. This source implements CCAR §1 tier-boundary rules as machine-executable architecture lint (TS: dependency-cruiser; Java: ArchUnit); same-revision pairing per [OS] §8.5.2.
- **Relationship to [RULE] Workspace Topology**: Anchored. CI integration (§5) operates within WT §1 monorepo layout; per-app and shared-package paths derive from there. §8.5 Renovate Governance complements WT §3.2.5 drift handling for the dependency-update dimension.
- **Relationship to [RULE] Codex Plugin Usage**: Companion. Codex cross-model review at TK-11 / M4 is the AI semantic review layer that complements (not replaces) the deterministic checks declared here.
- **Relationship to [MECH] Development Track Workflow**: Anchored. Defines what "TOOL (lint / type / static analysis)" means at DTW TK-05 and the auto-repair scope for TK-06; static-analysis subset of TK-11 pre-M4 evidence.
- **Relationship to [MECH] CI/CD Milestone Policy**: Anchored. §5 declares which checks fire at which milestone (M1 / M2 / M3 / M4); milestone gate semantics owned by CI/CD.
- **Relationship to [MECH] Tools Health Cadence**: Companion. CQ §1-§2 declares the P0 tool stack content; Tools Health Cadence §5 mirrors that inventory for periodic verification. §8.5 Renovate Governance owns the bot configuration; Tools Health Cadence §3 step 6 consumes Renovate Dependency Dashboard state.
- **Relationship to [MECH] Dev-Loopback Mode**: Companion. Dev-Loopback §4 secret-loading contract (Vault dev mode) interacts with the secret-scanning rules declared in §1.7 and §4.6 of this source; the `hdc/no-inline-secret-literal` custom lint rule (§1.2) enforces "no secret literals in code" which is the negative counterpart to Dev-Loopback's "all secrets through Vault dev mode" contract.
- **Relationship to [MECH] Application Lifecycle Handoff**: At handoff, rule-set configuration files (`.eslintrc.*`, `eslint.config.js`, `tsconfig.json`, `.prettierrc`, `.gitleaks.toml`, `.semgrep.yml`, `osv-scanner.toml`, `pmd-ruleset.xml`, `checkstyle.xml`, `archunit-rules/**`, `dependency-cruiser.config.js`, `renovate.json`) are part of handed-off content scope.
- **Relationship to [RULE] Design System Governance**: DSG §4 (token consumption) and §5 (component inventory) declare design rules; this source declares the lint-level enforcement; same-period pairing per [OS] §8.5.2.
- **Pairings I participate in**: P-12 (with [RULE] CCAR §1), P-20 (with lint and quality config files), P-34 (with [RULE] DSG §4 + §5), P-50 (with [MECH] Tools Health Cadence §3 step 6 + §5 inventory), P-53 (with [MECH] Dev-Loopback §4 secret-loading contract)

## How to use this source

Use this source when:
- Setting up a new app within the HDC monorepo and configuring its quality tooling
- Authoring or reviewing CI workflows that gate code quality
- Designing custom lint rules for a new architecture pattern
- Investigating why a check fires at a specific milestone
- Updating the rule set in response to a new AI failure mode discovered in production
- Reviewing whether a slice's lint and static-analysis evidence is sufficient for M4
- Configuring Renovate for dependency-update governance (§8.5)

Do not use as:
- A milestone gate semantics reference ([MECH] CI/CD Milestone Policy)
- A TK-by-TK orchestration reference ([MECH] Development Track Workflow §4)
- A tier-boundary semantic reference ([RULE] Claude Code Architecture Rules §1)
- A design-system specification ([RULE] Design System Governance)
- A specific tool's user manual (link to upstream tool docs instead)
- A tool-stack maintenance protocol ([MECH] Tools Health Cadence)
- A secret-loading runtime contract ([MECH] Dev-Loopback Mode §4)

---

# 0. Boundary and position

## 0.1 What this source owns

- The authoritative tool stack per Tier (Tier 1 / 2: TypeScript-React-Node; Tier 3: Java)
- The rule preset selection per tool (e.g., "extends typescript-eslint/strict-type-checked")
- Custom architecture lint rules that translate tier-boundary semantics into executable checks
- AI-era specific augmentations: dependency allow-list, hallucinated-import detection, pattern conformance, test-ordering enforcement, secret leakage detection, light SAST, SCA
- Severity policy: which violations block merge, which warn, which are informational
- CI/CD pipeline step ordering and fail-fast policy
- Coverage gate thresholds per Tier
- Rule-set governance: additive vs breaking change process
- Renovate dependency-update governance (§8.5): config policy, grouping strategy, auto-merge rules, operator cadence
- Anti-drift red flags specific to quality tooling

## 0.2 What this source does not own

- Milestone gate semantics ([MECH] CI/CD Milestone Policy)
- TK-by-TK orchestration ([MECH] Development Track Workflow §4)
- Tier-boundary semantics ([RULE] Claude Code Architecture Rules §1)
- Design-system rules ([RULE] Design System Governance)
- Specific Codex prompt templates ([RULE] Codex Plugin Usage)
- Per-slice test plan content ([TPL] Test Plan YAML Schema)
- Tool-stack maintenance protocol ([MECH] Tools Health Cadence)
- Secret-loading runtime contract ([MECH] Dev-Loopback Mode §4)
- Specific runtime configuration file contents (those live in repo at the paths declared in §5; this source declares what they must satisfy, not their literal content)

## 0.3 Layered structure: policy vs configuration

Quality rules exist in two layers:

| Layer | Owner | Volatility | Examples |
|---|---|---|---|
| **Policy** | This canonical source | Stable across releases | "Tier 1 must enforce typescript-eslint strict-type-checked"; "Tier 1 cannot import from packages/domain"; "PR is blocked if architecture lint fails"; "All apps must run gitleaks pre-commit and CI"; "Renovate security PRs must bypass schedule"; |
| **Configuration** | Repo runtime artifacts | Drifts with tool versions | `apps/{app-slug}/eslint.config.js`; `tsconfig.json`; `pmd-ruleset.xml`; `.archunit/rules/*.java`; `.gitleaks.toml`; `.semgrep.yml`; `osv-scanner.toml`; `renovate.json` |

Per [OS] §8.4 (separate stable from dynamic), policy lives in this canonical source; configuration lives in repo. Configuration is generated from policy (manually or via skill-assisted generation) and is reviewed for compliance with policy at TK-05 / TK-11.

---

# 1. Tier 1 / Tier 2 — TypeScript, React, Node

Both Tier 1 (React frontend) and Tier 2 (Node BFF) share the TypeScript stack and largely share the same rule set. Tier-specific rules are noted where they differ.

## 1.1 Format

- **Tool**: Prettier
- **Mode**: opinionated, no per-rule customization beyond project-level (line width 100, semicolons, trailing comma `all`, single quote)
- **Stage**: separate CI stage from ESLint to avoid conflicts
- **License**: MIT

## 1.2 Lint

- **Tool**: ESLint (latest stable major; flat config)
- **License**: MIT

### Required preset chain

**Scope: ESLint configuration in §1.2 Lint context (Tier 1 React + Tier 2 Node BFF, TypeScript stack).** The base configuration must extend (in order):

1. `@eslint/js` recommended
2. `typescript-eslint` `strict-type-checked` + `stylistic-type-checked` (type-aware variants are mandatory; non-type-aware variants are insufficient)
3. `eslint-plugin-react` `recommended` (Tier 1 only)
4. `eslint-plugin-react-hooks` `recommended` (Tier 1 only)
5. `eslint-plugin-jsx-a11y` `recommended` (Tier 1 only) — at `warn` severity per [RULE] Design System Governance §6 (advisory; no CI gate)
6. `eslint-plugin-import` errors + warnings

### Required rule overrides (default-off but mandatory in HDC)

**Scope: ESLint rule overrides in §1.2 Lint context, applied across both Tier 1 and Tier 2 (TypeScript stack); per-tier additions follow in the next two sub-sections.** The following rules are not in the recommended presets but are mandatory in HDC:

| Rule | Severity | Reason |
|---|---|---|
| `@typescript-eslint/no-floating-promises` | error | Catches missed `await` — high-frequency AI failure mode |
| `@typescript-eslint/no-misused-promises` | error | Catches passing async fn where sync expected |
| `@typescript-eslint/no-explicit-any` | error | Forces explicit type rather than escape hatch |
| `@typescript-eslint/switch-exhaustiveness-check` | error | Catches missed enum branches |
| `@typescript-eslint/no-unused-vars` | error | Default warn → bumped to error |
| `@typescript-eslint/consistent-type-imports` | error | Hygiene |
| `import/no-extraneous-dependencies` | error | Catches AI-hallucinated imports of packages not in `package.json` |
| `import/no-cycle` | error | Catches accidental cyclic dependencies |
| `import/order` | error | Stable import ordering |
| `no-restricted-imports` | error | Architecture-boundary enforcement (see §3.2) |

### Tier 1 only

**Scope: ESLint rules in §1.2 Lint context, additive on top of `Required rule overrides` above; applies to Tier 1 React frontend code under `apps/{app-slug}/src/frontend/` only.**

| Rule | Severity | Reason |
|---|---|---|
| `react-hooks/exhaustive-deps` | error | Default warn → bumped to error |
| `react/jsx-no-target-blank` | error | Security |
| `jsx-a11y/alt-text` | warn | DSG §6 advisory |
| `jsx-a11y/anchor-is-valid` | warn | a11y advisory |
| `jsx-a11y/click-events-have-key-events` | warn | DSG §6 advisory |
| `jsx-a11y/no-noninteractive-element-interactions` | warn | a11y advisory |

### Tier 2 only

**Scope: ESLint rules in §1.2 Lint context, additive on top of `Required rule overrides` above; applies to Tier 2 Node BFF code under `apps/{app-slug}/src/bff/` only.**

| Rule | Severity | Reason |
|---|---|---|
| `no-process-exit` | error | BFF shutdown hygiene |
| `@typescript-eslint/require-await` | warn | Avoid `async` without `await` (style) |

### Custom plugin: HDC architecture rules

A small in-repo ESLint plugin (`packages/eslint-plugin-hdc/`) implements project-specific rules:

| Rule | Severity | Description |
|---|---|---|
| `hdc/no-hardcoded-token-value` | error | Forbids hex colors, px values, raw font sizes in Tier 1 code (DSG §4 enforcement) |
| `hdc/use-arco-component` | error | Forbids raw `<input>`, `<select>`, `<button>`-with-styling in Tier 1 (DSG §5 Tier C enforcement) |
| `hdc/no-cross-app-import` | error | Forbids importing from `apps/{other-app}/**` |
| `hdc/i18n-string-literal` | warn | Flags user-facing string literals not wrapped in i18n call |
| `hdc/no-inline-secret-literal` | error | Detects high-entropy strings and common secret prefixes (`sk-`, `AKIA`, `ghp_`, `xoxb-`, JWT three-segment pattern `eyJ...`) inlined in source code. Negative counterpart to [MECH] Dev-Loopback §4 secret-loading contract (which mandates all secret-class material flow through Vault dev mode); this rule fires when AI agents bypass the contract by inlining a literal |

Plugin source lives in `packages/eslint-plugin-hdc/src/`; rules are unit-tested.

## 1.3 Type check

- **Tool**: tsc (TypeScript Compiler)
- **License**: Apache 2.0
- **Required `tsconfig.json` flags** (mandatory for all apps):
  - `"strict": true`
  - `"noUncheckedIndexedAccess": true`
  - `"exactOptionalPropertyTypes": true`
  - `"noImplicitOverride": true`
  - `"noFallthroughCasesInSwitch": true`
  - `"noPropertyAccessFromIndexSignature": true`
  - `"useUnknownInCatchVariables": true` (default in TS 4.4+ but make explicit)
- **Mode**: full project compile via `tsc --noEmit` in CI; `tsc --build` for actual emission

## 1.4 Architecture lint

- **Tool**: dependency-cruiser
- **License**: MIT
- **Configuration**: `dependency-cruiser.config.js` at monorepo root, with custom rules implementing tier boundaries — see §3.2 for the rule list

## 1.5 Dependency hygiene (dead code / unused dependencies)

- **Tool**: knip (dead code / unused dependencies)
- **License**: ISC
- **Mode**: CI runs in `--strict` mode; unused dependencies fail the gate

## 1.6 Test

- **Unit tests**: Vitest (preferred for new apps) or Jest (allowed for existing); license: MIT
- **Component tests (Tier 1)**: Vitest + `@testing-library/react`; license: MIT
- **Coverage**: c8 / istanbul (built into Vitest); license: ISC / BSD
- **a11y in test (optional)**: `axe-core` via `@axe-core/react` available for engineers to add component-level a11y assertions when desired; not required by CI. License: MPL 2.0

### Coverage thresholds (mandatory)

**Scope: TypeScript test coverage thresholds in §1.6 Test context (Vitest/Jest + c8/istanbul); covers Tier 1 React frontend and Tier 2 Node BFF only. Tier 3 Java thresholds are owned by §2.4.**

| Tier | Line coverage | Branch coverage |
|---|---|---|
| Tier 1 | ≥ 70% | ≥ 60% |
| Tier 2 | ≥ 80% | ≥ 70% |

Coverage below threshold blocks M1 (per CI/CD Milestone Policy).

## 1.7 Secret scanning

**Why**: AI agents periodically inline secret-class literals (API keys, JWT signing secrets, OAuth tokens, OIDC client secrets) during code generation — treating them as "illustrative example values" rather than real secrets. The [MECH] Dev-Loopback §4 secret-loading contract mandates all secret-class material flow through Vault dev mode; secret scanning is the deterministic catch when AI bypasses that contract.

**Mechanism**:

- **Tool**: gitleaks
- **License**: MIT
- **Mode**: pre-commit hook (operator-machine prevention) + CI stage (defense in depth)
- **Ruleset**: gitleaks default ruleset (90+ patterns covering AWS keys, GCP keys, Slack tokens, JWT, private key headers, OAuth client secrets, generic API tokens, etc.) + HDC custom additions in `.gitleaks.toml` for any HDC-specific mock-token prefixes
- **Configuration file**: `<repo-root>/.gitleaks.toml`

**Severity**: error (block merge)

**Complementary**: the `hdc/no-inline-secret-literal` custom ESLint rule in §1.2 fires at lint time before gitleaks (faster IDE feedback); gitleaks is the binding CI gate.

## 1.8 Light SAST

**Why**: AI agents reproduce known-unsafe patterns from training data (e.g., unsafe SQL builders, raw HTML construction prone to XSS, prototype pollution, unsafe deserialization, `eval()` and equivalents, weak crypto usage, hardcoded HTTP-auth credentials, missing CSRF middleware in Express, missing rate limits on auth endpoints, etc.). The `eslint-plugin-security` family is partial coverage; Semgrep provides broader pattern coverage with framework-aware rulesets (React, Express, Node.js).

**Mechanism**:

- **Tool**: Semgrep Community Edition (CE)
- **License**: LGPL 2.1
- **Mode**: CI stage via `semgrep ci` command; pre-commit optional (Semgrep is fast on incremental scans)
- **Ruleset selection** (combined via `extends`):
  - `p/default` — r2c curated cross-language baseline (high precision, low false positives)
  - `p/typescript` — TypeScript-specific
  - `p/javascript` — JavaScript-specific (covers `.js` files in build tooling)
  - `p/react` — React-specific (`dangerouslySetInnerHTML`, XSS via href, etc.)
  - `p/nodejs` — Node.js-specific (used by Tier 2 BFF)
  - `p/owasp-top-ten` — OWASP Top 10 cross-language
  - `p/nodejsscan` — NodeJSScan ruleset (Node.js security specialist)
- **Excluded rulesets** (deliberately):
  - `p/security-audit` — audit-level, requires human review of every finding; would dilute the rule set's signal-to-noise ratio
  - `p/secrets` — overlaps with gitleaks (§1.7); gitleaks is the specialist
  - `p/findsecbugs` — FindSecBugs ruleset transcribed to Semgrep; redundant with the actual SpotBugs + FSB run on Tier 3 (§2.2)
- **Configuration file**: `<repo-root>/.semgrep.yml` (extends the rulesets above; HDC-specific overrides if any)
- **Crossfile dataflow caveat**: Semgrep CE supports single-file taint analysis only; crossfile dataflow is Pro-tier. HDC accepts the single-file limitation as adequate for AI-failure-mode coverage; the operator may revisit if Pro-tier value materializes.

**Severity**:
- `ERROR` rules → block merge
- `WARNING` rules → annotate PR (visible, non-blocking)
- `INFO` rules → log only

## 1.9 SCA (Software Composition Analysis)

**Why**: The §4.1 dependency allow-list catches AI-hallucinated package names but does not catch CVEs in approved packages. AI agents tend to use versions they encountered during training (which may be 1-3 years old) and rarely proactively upgrade. SCA closes the loop by querying CVE databases for the actually-installed versions.

**Mechanism**:

- **Primary tool**: osv-scanner (Google-maintained, OSV.dev database)
- **License**: Apache 2.0
- **Mode**: CI stage; scans `pnpm-lock.yaml`, `pom.xml` / `build.gradle` lockfile equivalents in a single command
- **Secondary tool**: `pnpm audit` (built into pnpm; npm advisory DB)
- **Mode**: optional pre-commit / local-dev convenience check; not the binding CI gate
- **Configuration file**: `<repo-root>/osv-scanner.toml` (Apache 2.0; declares scan scope and ignore policy)

**Severity policy** (CVSS-based):
- `CRITICAL` (CVSS ≥ 9.0) → block merge
- `HIGH` (CVSS 7.0–8.9) → block merge
- `MEDIUM` (CVSS 4.0–6.9) → annotate PR (non-blocking; Renovate per §8.5 expected to resolve over time)
- `LOW` (CVSS < 4.0) → log only

**Complementary**: §8.5 Renovate Governance keeps dependencies current to minimize accumulated CVE exposure; SCA is the catch when Renovate has not yet processed a vulnerability or when the operator has deferred a Renovate PR.

---

# 2. Tier 3 — Java Domain Services

## 2.1 Format

- **Tool**: Spotless + google-java-format
- **License**: Apache 2.0
- **Mode**: enforced via Maven / Gradle plugin in CI; auto-format available locally via build target

## 2.2 Lint and bug detection

- **Tool**: Checkstyle
  - **License**: LGPL 2.1
  - **Ruleset**: Google Java Style (the published `google_checks.xml`)
- **Tool**: PMD
  - **License**: BSD 4-clause
  - **Ruleset**: PMD's `quickstart.xml` plus selected categories from `bestpractices.xml` and `errorprone.xml`
- **Tool**: SpotBugs + Find Security Bugs plugin
  - **License**: LGPL 2.1 / LGPL 3.0
  - **Ruleset**: default + Find Security Bugs detectors enabled
- **Tool**: Error Prone
  - **License**: Apache 2.0
  - **Mode**: Maven / Gradle compile-time plugin; default rule severity, project-specific opt-in for advanced checks (e.g., `Var`, `MissingOverride`)

## 2.3 Architecture lint

- **Tool**: ArchUnit
- **License**: Apache 2.0
- **Configuration**: Rule classes under `packages/domain/{domain-name}/src/test/java/.../arch/**`; rules listed in §3.3

## 2.4 Coverage

- **Tool**: JaCoCo
- **License**: EPL 2.0
- **Coverage thresholds**:

| Tier | Line coverage | Branch coverage |
|---|---|---|
| Tier 3 | ≥ 80% | ≥ 75% |

Coverage below threshold blocks M1 (per CI/CD Milestone Policy).

## 2.5 SCA for Java

Java dependency SCA shares the §1.9 osv-scanner tooling (osv-scanner reads Maven `pom.xml` and Gradle lockfiles natively). No separate Java-stack SCA tool is needed.

---

# 3. Custom architecture lint rules

## 3.1 Purpose

The custom architecture lint rules in this section translate [RULE] Claude Code Architecture Rules §1 tier-boundary semantics into machine-executable checks. Without these, AI agents may silently breach tier boundaries (e.g., importing domain logic from Tier 1, calling repositories from controllers, circular package dependencies).

## 3.2 TypeScript rules (dependency-cruiser + ESLint `no-restricted-imports`)

The following rules are encoded in `dependency-cruiser.config.js` and as `no-restricted-imports` rules where applicable. All rules at severity `error`.

| Rule ID | Statement |
|---|---|
| `tier1-no-direct-tier3` | `apps/{app}/src/frontend/**` cannot import from `packages/domain/**` (Tier 1 must go through Tier 2) |
| `tier1-no-cross-app` | `apps/{app}/src/frontend/**` cannot import from `apps/{other-app}/**` |
| `tier2-no-cross-app` | `apps/{app}/src/bff/**` cannot import from `apps/{other-app}/**` |
| `tier1-no-bff-internals` | `apps/{app}/src/frontend/**` cannot import from `apps/{app}/src/bff/internal/**` (only public BFF API exposed via `apps/{app}/src/bff/api/**` is consumable) |
| `domain-no-cross-domain` | `packages/domain/{X}/src/**` cannot import from `packages/domain/{Y}/src/**` (domain isolation) |
| `tier1-no-arco-mobile-in-pc-scope` | Files under `apps/{app}/src/frontend/web/**` cannot import from `@arco-design/mobile-react` |
| `tier1-no-arco-web-in-mobile-scope` | Files under `apps/{app}/src/frontend/mobile/**` cannot import from `@arco-design/web-react` |
| `no-third-party-ui-tier1` | Tier 1 cannot import from non-Arco React UI libs (MUI, Ant Design, shadcn/ui, etc.) — DSG §5 Tier C enforcement |

## 3.3 Java rules (ArchUnit)

The following ArchUnit rules are mandatory. All written as JUnit tests, naming convention `Arch{RuleName}Test`.

| Rule | Description |
|---|---|
| `DomainIsolation` | No class in `domain.X` package imports from `domain.Y` package |
| `LayeredArchitecture` | controllers → services → repositories, no skip |
| `RepositoryAccess` | Only `*Service` classes call `*Repository` methods (controllers cannot bypass) |
| `TransactionalScope` | `@Transactional` annotation only on `*Service` class methods, never on controllers or repositories |
| `NamingConventions` | Classes ending in `Service`, `Repository`, `Controller` are in the corresponding package; classes in those packages must follow the naming |
| `NoFieldInjection` | No `@Autowired` on fields (constructor injection only) |
| `NoCircularDependency` | No package-level cyclic imports |

---

# 4. AI-era specific augmentations

These are checks that exist because AI-Agent-generated code has specific high-frequency failure modes not addressed by traditional rule sets.

## 4.1 Dependency allow-list

**Why**: AI Agents periodically hallucinate package names (e.g., `react-table-pro` when `@tanstack/react-table` is the real package) or pull in cold-start packages that are not maintained.

**Mechanism**:
- A repository-root `tools/dependency-allow-list.json` lists every approved package per ecosystem (npm, Maven)
- A pre-commit hook + CI step (small Node / shell script) compares any added entry in `package.json` / `pom.xml` / `build.gradle` against the allow-list
- New additions require explicit project-owner approval (PR review)
- AI Agents may propose additions in PR but cannot merge them autonomously

**Severity**: error (block merge)

## 4.2 Test ordering enforcement (anti-tautological)

**Why**: When AI Agents generate implementation and tests in the same step, tests reduce to "test what the code does" rather than "test what the code should do" — tautological tests pass but provide no contract verification.

**Mechanism**:
- TK-03 produces `acceptance/{slice-id}.yaml` (test scenarios) and `test-plan/{slice-id}.yaml` (test cases) **before** TK-04 (code writing)
- A CI check verifies that for every PR introducing a new test under `apps/{app-slug}/tests/**`, the corresponding `test-plan/{slice-id}.yaml` entry was committed at least one commit earlier (git log timestamp check)
- Same for ArchUnit rules: rule must precede the implementation it tests

**Severity**: warn (CI annotation, does not block merge); promoted to error if violation rate exceeds 10% across a phase

**Note**: This is a heuristic, not a complete check. It cannot detect AI generating both files in temporal order while still tautological. The deeper protection comes from intent.md / acceptance.yaml being authored before TK-04 per [MECH] Development Track Workflow.

## 4.3 Pattern conformance (custom lint)

**Why**: AI Agents introduce subtle pattern drift across slices (different error-handling styles, different naming for similar concepts, different state management in similar contexts).

**Mechanism**:
- Custom ESLint rules in `packages/eslint-plugin-hdc/` that enforce HDC-specific patterns:
  - All BFF route handlers use a single error-handling middleware (no per-route try-catch with custom format)
  - All async data fetchers in Tier 1 use the project's standard query hook pattern
  - All forms use Arco's `Form` (not raw HTML) and Arco's `Form.useForm` for validation

**Severity**: error for hard patterns, warn for stylistic patterns

## 4.4 Hallucinated import detection

**Why**: Even with allow-list, AI Agents sometimes import from non-existent submodules of allowed packages.

**Mechanism**:
- `tsc` with `"moduleResolution": "Bundler"` or `"Node16"` already catches non-existent imports at type-check time
- This is therefore covered by §1.3 type-check requirement; no additional tooling needed

## 4.5 AI semantic review (cross-model)

Codex cross-model review at TK-11 / M4 is the AI-semantic complement to deterministic checks above. Owned by [RULE] Codex Plugin Usage; cross-referenced here for completeness.

## 4.6 Secret leakage detection

**Why**: AI agents inline secret-class literals during code generation, especially when constructing fixtures, integration tests, dev-loopback configuration, or example code. The [MECH] Dev-Loopback §4 secret-loading contract mandates secrets flow through Vault dev mode; this augmentation is the deterministic catch when AI bypasses the contract.

**Mechanism**:
- §1.7 gitleaks (pre-commit + CI) covers committed source files
- §1.2 `hdc/no-inline-secret-literal` ESLint rule covers IDE-time feedback before commit
- Both reference [MECH] Dev-Loopback §4 as the positive-side contract

**Severity**: error (block merge); see §1.7 / §1.2 for tool-level severity

## 4.7 Light SAST coverage

**Why**: AI training data includes many historical unsafe patterns. The standard ESLint preset chain does not cover security-pattern detection; the bundled `eslint-plugin-jsx-a11y` covers accessibility only; `eslint-plugin-security` is partial. Semgrep with curated security rulesets closes this gap with bounded false-positive cost.

**Mechanism**: see §1.8 — Semgrep CE with `p/default` + `p/typescript` + `p/javascript` + `p/react` + `p/nodejs` + `p/owasp-top-ten` + `p/nodejsscan` rulesets.

**Severity**: ERROR rules block merge; WARNING rules annotate PR.

## 4.8 SCA CVE detection

**Why**: AI tends to use older package versions encountered during training; allow-list does not catch CVEs in approved packages.

**Mechanism**: see §1.9 — osv-scanner + pnpm audit.

**Severity**: CRITICAL + HIGH (CVSS-based) block merge; MEDIUM annotates; LOW logs.

---

# 5. CI/CD pipeline integration

## 5.1 Pipeline order (fail-fast)

The full quality gate pipeline runs in this order. Earlier stages fail fast.

1. Format check (Prettier / Spotless) — seconds
2. Lint (ESLint / Checkstyle + PMD) — seconds
3. Secret scanning (gitleaks) — seconds (§1.7)
4. Type check (tsc / Java compile + Error Prone) — seconds to minutes
5. Light SAST (Semgrep CE) — seconds to minutes (§1.8)
6. Bug detection (SpotBugs + Find Security Bugs) — minutes
7. Architecture lint (dependency-cruiser / ArchUnit) — seconds
8. Dependency allow-list check — seconds
9. SCA CVE scan (osv-scanner) — seconds (§1.9)
10. Test ordering check (heuristic) — seconds
11. Unit tests + coverage gate — minutes
12. Internal integration tests — minutes
13. Knip dead-code / unused-dep check — seconds
14. (M4 only) Codex cross-model review — minutes (out-of-band, see [RULE] Codex Plugin Usage)

## 5.2 Milestone touch points

| Milestone | Stages run | Block on failure |
|---|---|---|
| TK-05 (M1) | 1-13 | All; auto-repair via TK-06 for unit-test failures only |
| TK-11 (M4) | 1-14 (full re-run of 1-13 plus Codex) | All except test-ordering warnings |

(The detailed milestone gate semantics are owned by [MECH] CI/CD Milestone Policy; this section only declares which checks fire.)

## 5.3 Configuration file locations

| Tool | File path |
|---|---|
| Prettier | `<repo-root>/.prettierrc` (root, all TS apps inherit) |
| ESLint | `<repo-root>/eslint.config.js` (root) + `apps/{app-slug}/eslint.config.js` (app overrides) |
| TypeScript | `<repo-root>/tsconfig.base.json` + `apps/{app-slug}/tsconfig.json` (extends base) |
| gitleaks | `<repo-root>/.gitleaks.toml` |
| Semgrep | `<repo-root>/.semgrep.yml` |
| osv-scanner | `<repo-root>/osv-scanner.toml` |
| dependency-cruiser | `<repo-root>/dependency-cruiser.config.js` |
| Knip | `<repo-root>/knip.json` |
| Spotless | per-module Maven / Gradle plugin config |
| Checkstyle | `<repo-root>/build-tools/checkstyle.xml` |
| PMD | `<repo-root>/build-tools/pmd-ruleset.xml` |
| SpotBugs / FSB | per-module Maven / Gradle plugin config |
| ArchUnit rules | `packages/domain/{domain-name}/src/test/java/.../arch/**` |
| Custom HDC ESLint plugin | `packages/eslint-plugin-hdc/` |
| Allow-list | `<repo-root>/tools/dependency-allow-list.json` |
| Renovate config | `<repo-root>/renovate.json` (per §8.5) |

## 5.4 Hooks (Claude Code workflow integration)

Per [MECH] Development Track Workflow TK-05:
- PostToolUse hook fires stages 1-4 (format / lint / secret scan / type) on every code-edit tool call
- SubagentStop hook fires stages 5-13 (light SAST through dead-code) at the end of a subagent's work

This makes the cost of a violation low (immediate feedback) and prevents accumulated failure at TK-05 close.

---

# 6. Severity policy

## 6.1 Severity levels

| Level | CI behavior | Local dev behavior |
|---|---|---|
| `error` | Block merge | Red squiggle, fail `--check` |
| `warn` | Annotate PR | Yellow squiggle, no fail |
| `info` | Log only | No squiggle, log only |

## 6.2 Default level by category

| Category | Default level |
|---|---|
| Type errors (tsc, Java compile) | error |
| Format violations | error (run `format:fix` to resolve) |
| ESLint rules from required preset chain | as defined in preset (mostly error) |
| Custom HDC architecture rules | error |
| Architecture lint (dependency-cruiser, ArchUnit) | error |
| Dependency allow-list violations | error |
| Test-ordering heuristic | warn |
| `eslint-plugin-jsx-a11y` rules (Tier 1 only) | warn (advisory; no CI gate) |
| Coverage below threshold | error |
| Knip unused-dep violations | error |
| gitleaks findings | error |
| `hdc/no-inline-secret-literal` | error |
| Semgrep ERROR rules | error |
| Semgrep WARNING rules | warn |
| Semgrep INFO rules | info |
| SCA CVSS CRITICAL / HIGH | error |
| SCA CVSS MEDIUM | warn |
| SCA CVSS LOW | info |

## 6.3 Suppression policy

Suppression of specific rules in code (e.g., `// eslint-disable-next-line`, `// nosemgrep`) is allowed only with:
- Inline justification comment (`// eslint-disable-next-line rule-name -- <reason>` or `// nosemgrep: <rule-id> -- <reason>`)
- The reason must be substantive ("temporary", "TODO", or empty reasons are disallowed)
- Suppression count is tracked; exceeding 1% of LoC across an app triggers a quality-debt review at TK-11

Secret-scanning suppression has a stricter policy:
- gitleaks `# gitleaks:allow` comments require explicit justification AND must be coupled with a paired DR or HANDOFF entry explaining why the literal is intentional and safe (e.g., a documented public test key for an open standard); suppression of gitleaks findings without paired documentation is treated as a §10 anti-drift signal

---

# 7. Coverage gate

(Cross-reference §1.6 and §2.4 thresholds.)

| Tier | Line | Branch |
|---|---|---|
| Tier 1 | ≥ 70% | ≥ 60% |
| Tier 2 | ≥ 80% | ≥ 70% |
| Tier 3 | ≥ 80% | ≥ 75% |

Threshold check fires at TK-05 / M1 (per CI/CD Milestone Policy). Falling below blocks M1 close.

Coverage is computed per-app for Tier 1 / 2; per-domain-package for Tier 3.

---

# 8. Governance

## 8.1 Change categories

- **Additive** (new rule added at warn or info level, new tool added in advisory mode, new architecture rule): the proposing slice's TK-02 includes a Code Quality Rule Set update plan; the rule is added at the slice's M4 merge
- **Breaking** (severity raised from warn to error, threshold raised, new mandatory tool, removal of any rule): requires separate review gate outside the normal TK flow; all in-flight slices must be reviewed for compliance; rollout coordinated to a quiet point in the dev-track sequence

## 8.2 Change file location

`specs/code-quality-rule-set-changes/{change-id}.md`

## 8.3 Change file minimum structure

(Mirrors DSG §12 change file structure.)

- **Change identity**: `change-id`, change type (`additive` or `breaking`), proposer, proposal date, target rule-set version
- **Affected sections**: list the §X subsections this change touches
- **Proposed change content**: rule additions, severity changes, threshold changes, tool additions
- **Rationale**: business or quality reason; AI failure mode references where applicable
- **Backward-compatibility analysis**: list every currently-merged slice whose code would fail under the new rule; estimate fix scope
- **Operator M0 review reference**: M0 entry self-check executes at TK-04 entry per [MECH] Development Track Workflow §4 (the design-freeze function it once served is fulfilled at Hub TK-03 sign-off via the operator GPT-Claude consensus loop); when a rule change proposal benefits from cross-model adversarial assessment, the operator drives this at the Hub TK-03 sign-off step
- **Approval status**: `pending` / `approved` / `rejected` / `deferred`

## 8.4 Forbidden patterns (in change governance)

- Silent rule additions or severity changes in CI configuration without rule-set source update
- Per-app rule-set divergence not justified in app's CLAUDE.md
- Suppression of rules in CI configuration to "unblock" a slice (the correct path is fix the code or propose a governed rule change)

## 8.5 Renovate dependency-update governance

### 8.5.1 Role and scope

Renovate is the canonical dependency-update bot for the HDC monorepo. It opens PRs for outdated npm and Maven dependencies, monitors OSV-based vulnerability alerts, and supports operator-defined grouping / scheduling / auto-merge rules. This subsection owns the Renovate **policy** (what behavior Renovate must implement); the actual `renovate.json` config file in the repo root is the runtime artifact per §0.3.

### 8.5.2 Required preset baseline

The repo-root `renovate.json` MUST extend the following Renovate presets:

- `config:recommended` (Renovate's curated default best-practices baseline)
- `:dependencyDashboard` (creates and maintains a GitHub issue summarizing pending updates — the operator's primary read view)
- `:semanticCommits` (semantic commit message format for traceability)

### 8.5.3 Required configuration policies

The following policies MUST be reflected in the runtime `renovate.json`:

| Policy | Required value | Rationale |
|---|---|---|
| `osvVulnerabilityAlerts` | `true` | Broader CVE coverage than GitHub native alerts |
| `vulnerabilityAlerts.enabled` | `true` | Standard alert subsystem on |
| `vulnerabilityAlerts.minimumReleaseAge` | `"0 days"` | Security fixes bypass minimum-age delay |
| `vulnerabilityAlerts.schedule` | `["at any time"]` | Security PRs not subject to weekly schedule |
| Default `minimumReleaseAge` | `"7 days"` | Non-security PRs wait 7 days to mitigate malicious package risk; calibrated between Renovate's recommended 14 days (high security tolerance) and 0 days (high update frequency tolerance) |
| Default `schedule` | `["before 4am on saturday"]` (operator timezone) | Quiet period; results visible Monday morning |
| `prConcurrentLimit` | `5` | Caps active PRs to avoid backlog overwhelm |
| `prHourlyLimit` | `2` | Smooths CI load |
| `branchConcurrentLimit` | `8` | Slightly above PR limit to allow grace |
| `lockFileMaintenance.enabled` | `true` | Periodic lockfile freshening |
| `lockFileMaintenance.schedule` | weekly, off-hours | Lockfile churn does not block dev hours |
| `lockFileMaintenance.automerge` | `true` | Lockfile updates are mechanical |

### 8.5.4 Required package rules

The following grouping / auto-merge / labeling rules MUST be reflected in the runtime `renovate.json`:

| Rule purpose | Match criteria | Behavior |
|---|---|---|
| Security PRs surface immediately | `isVulnerabilityAlert: true` for any dep | `schedule: ["at any time"]`, `labels: ["security"]`, manual merge required |
| Dev dependencies patch/minor auto-merge | `matchDepTypes: ["devDependencies"]` + `matchUpdateTypes: ["patch", "minor"]` + `matchCurrentVersion: "!/^0/"` | `automerge: true`, `platformAutomerge: true` |
| Lint/format/test tools minor auto-merge | `matchPackageNames: ["eslint", "prettier", "vitest", "jest", "@typescript-eslint/**", "typescript-eslint"]` + `matchUpdateTypes: ["patch", "minor"]` | `automerge: true`, `platformAutomerge: true` |
| Production patch auto-merge | `matchDepTypes: ["dependencies"]` + `matchUpdateTypes: ["patch"]` + `matchCurrentVersion: "!/^0/"` | `automerge: true`, `platformAutomerge: true` |
| Production minor: manual review | `matchDepTypes: ["dependencies"]` + `matchUpdateTypes: ["minor"]` | `automerge: false`, `labels: ["dependencies-minor"]` |
| Major updates: manual review + 30-day hold | `matchUpdateTypes: ["major"]` | `automerge: false`, `labels: ["dependencies-major", "needs-review"]`, `groupName: "major-{{depName}}"`, `minimumReleaseAge: "30 days"` |
| Framework majors: separate evaluation | `matchPackageNames: ["typescript", "react", "react-dom", "node", "pnpm"]` + `matchUpdateTypes: ["major"]` | `automerge: false`, `labels: ["framework-major"]` |
| Pre-1.0 packages: never auto-merge | `matchCurrentVersion: "/^0/"` (negation of above patch / minor auto-merge rules) | `automerge: false` (default) — pre-1.0 may make breaking changes at any update type per semver |

### 8.5.5 Operator cadence

| Cadence | Action | Estimated time |
|---|---|---|
| Weekly (Monday morning) | Review `security` label PRs; review and merge after CI green | 15 min |
| Monthly | Batch review `dependencies-minor` label PRs | 30 min |
| Quarterly | Process `dependencies-major` / `framework-major` accumulated backlog — performed within Tools Health Day per [MECH] Tools Health Cadence §3 | absorbed into Tools Health Day |
| Continuous (passive) | Dependency Dashboard issue tracks state; no active monitoring | 0 |

### 8.5.6 Active-feature interaction

When an active `feature` or `walking_skeleton` unit is in flight (i.e., a slice is between TK-04 (CC entry) and TK-12 (M4 merge to `main`) per [MECH] Development Track Workflow), Renovate-opened PRs in the same `apps/{app-slug}/` scope SHOULD NOT be merged until the active slice merges, to avoid mid-execution dependency drift breaking the in-flight slice's evidence chain.

Renovate scheduling (§8.5.3 default `schedule`) is designed to fire during quiet windows (weekends), which minimizes overlap with active-feature work; this is a defense, not a guarantee. The operator's weekly cadence (§8.5.5) is the binding ack point.

### 8.5.7 Forbidden patterns

- `renovate.json` modified during active-feature execution without operator awareness (Renovate config edits should batch to Tools Health Day windows)
- Security PRs sitting in Dependency Dashboard > 14 days without resolution
- Auto-merge enabled for pre-1.0 (`/^0/`) packages
- Auto-merge enabled for `major` updates
- `osvVulnerabilityAlerts` disabled
- Dependency Dashboard issue closed / disabled

---

# 9. Cross-source pairing summary

| Pair source | Pairing type | Condition |
|---|---|---|
| [RULE] Claude Code Architecture Rules §1 | Same-revision | Tier-boundary semantic change → architecture lint rule update in §3 |
| [RULE] Design System Governance §4, §2.4 | Same-period | New token / component → custom lint rule in §1.2 (`hdc/no-hardcoded-token-value`, `hdc/use-arco-component`) verified within working period |
| [MECH] CI/CD Milestone Policy | Same-revision | Milestone touch points (§5.2) align with milestone gate definition |
| [MECH] Development Track Workflow §TK-05 / §TK-11 | Same-revision | TK descriptions reference "static analysis clean" — its definition is here |
| [RULE] Codex Plugin Usage | Same-period | Cross-model review touch point in §4.5 |
| [MECH] Application Lifecycle Handoff §3 | Same-period | Configuration files at handoff are listed in handoff content scope |
| [MECH] Dev-Loopback Mode §4 | Same-revision | Secret-loading contract negative-side enforcement (`hdc/no-inline-secret-literal` in §1.2, gitleaks in §1.7) pairs with positive-side contract in Dev-Loopback |
| [MECH] Tools Health Cadence §5 | Same-revision | P0 tool stack inventory in Tools Health §5 mirrors §1-§2 selections here; new tool added in this source → Tools Health §5 update |

---

# 10. Anti-drift red flags

> **Scope and ownership**: this section is the **canonical owner** for lint-level Tier 1 / Tier 2 / Tier 3 quality red flags (suppression rate, eslint preset chain, tsconfig strict flags, architecture lint disablement, dependency allow-list, coverage threshold, custom HDC plugin, Tier 1 visual rules drift, secret-scanning drift, SAST drift, SCA drift, Renovate governance drift). Downstream sources ([MECH] Development Track Workflow §8 UX/a11y; [MECH] CI/CD Milestone Policy §9 accessibility scope) reference this section rather than duplicate it. The Tier 1 visual rules listed here are the lint-implementation projection of [RULE] Design System Governance §4 token consumption + §2.4 component inventory; DSG §12 owns the policy-level governance for changing those rules.

Red flags that should trigger correction:

**Core lint and architecture drift**:
- An app's `eslint.config.js` does not extend the required preset chain
- `tsconfig.json` weakens any of the mandatory strict flags
- Architecture lint rules in `dependency-cruiser.config.js` or ArchUnit are silently disabled or weakened in a feature branch
- Dependency allow-list violations are merged via suppression rather than allow-list update
- Coverage threshold lowered for an app without §8 governance
- Custom HDC lint plugin (`packages/eslint-plugin-hdc/`) is unloaded in any app's config
- Suppression rate exceeds 1% LoC and is not addressed at TK-11
- Tier 1 visual rules (DSG-derived) drift from `hdc/no-hardcoded-token-value` and `hdc/use-arco-component`
- Quality-tooling configuration files diverge across apps without app-CLAUDE.md justification
- AI-era augmentations (allow-list, test-ordering) are silently bypassed
- M1 evidence reports do not include all stages of the §5.1 pipeline output

**Secret-scanning drift** (§1.7 / §1.2 / §4.6):
- gitleaks pre-commit hook missing on operator machines
- gitleaks CI stage missing or skipped
- `hdc/no-inline-secret-literal` rule disabled or unloaded
- gitleaks findings suppressed via `# gitleaks:allow` without paired DR / HANDOFF documentation
- Secret-class literals detected in code despite [MECH] Dev-Loopback §4 secret-loading contract being declared
- High volume of gitleaks suppressions in a single PR (signal of contract bypass attempt)

**Light SAST drift** (§1.8 / §4.7):
- `.semgrep.yml` does not extend the required ruleset baseline (`p/default` + `p/typescript` + `p/javascript` + `p/react` + `p/nodejs` + `p/owasp-top-ten` + `p/nodejsscan`)
- Semgrep CI stage missing or skipped
- ERROR-level Semgrep findings suppressed via `// nosemgrep` without substantive justification
- An app's `.semgrep.yml` weakens severity of an ERROR-level rule to WARNING without §8 governance
- Semgrep version pinned to a stale major release for > 2 quarters without Tools Health Day evaluation

**SCA drift** (§1.9 / §4.8):
- osv-scanner CI stage missing or skipped
- CRITICAL / HIGH CVSS findings suppressed via `osv-scanner.toml` ignores without paired remediation plan
- An app's `osv-scanner.toml` scope-excludes a real dependency path
- `pnpm audit` CI stage configured to mask findings rather than report them
- SCA-detected vulnerabilities pending > 30 days without Renovate PR resolution or operator-acknowledged deferral

**Renovate governance drift** (§8.5):
- `renovate.json` does not extend `config:recommended` + `:dependencyDashboard`
- Dependency Dashboard GitHub issue closed or auto-close enabled
- Security PRs unresolved > 14 days
- Pre-1.0 packages auto-merge enabled
- `major` update auto-merge enabled
- `osvVulnerabilityAlerts: false` or missing
- Renovate PRs merging during active-feature execution without operator awareness
- Renovate disabled for entire repo without §8 governance approval

**Tools Health Cadence interaction drift** (§5 of [MECH] Tools Health Cadence):
- New P0 tool added to this source's §1 / §2 inventory without simultaneous update to [MECH] Tools Health Cadence §5 (per P-50)
- Tool removed from this source's §1 / §2 without simultaneous removal from [MECH] Tools Health Cadence §5

---

# 11. Change log

(In the active canonical: maintain a chronological log of every approved change to this Rule Set, with date, change-id, change type, and one-line summary. Empty at first approval.)
