# [MECH] Dev-Loopback Mode

- **Project**: HR Digital Cockpit
- **Document Type**: Governance Mechanism Specification
- **Status**: Active canonical
- **Role**: Stable source defining the development-environment runnability requirement that every HDC application produced via Claude Code must satisfy: a single-command, single-machine, end-to-end runnable stack that supports functional testing of all user stories without dependency on external real services. This source owns the dev-loopback's startup contract, fixture content, placeholder implementation pattern (with Tier A / Tier B classification per §4), secret loading contract (Vault dev mode + seed file pattern per §4.4), environment switch gate, and the supplemental walking-skeleton M5 acceptance assertions that bind to dev-loopback completeness.
- **Source Category**: Cat 4
- **Management-System Role**: Governance mechanism specification; outside L1-L5 hierarchy; this source is not itself an L2, L3, L4, or L5 artifact
- **Relationship to [OS]**: Operates within the routing architecture defined in [OS] §7.1; this source is referenced by phase TDD authors per the source-ready generation protocol in [OS] §8.9. Cross-source ownership map for the eleven Cat 4 [RULE] / [MECH] sources is owned by [OS] §8.5.6.
- **Relationship to [PRIN]**: Applies HR Digital Decision Design Principles §5 (management mechanism over ad hoc control), §6 (operation management and value realization by design).
- **Relationship to [REF] Hub-CD-CC Architecture**: Operates inside the CC workspace boundary defined per Hub-CD-CC Architecture §4. Dev-loopback artifacts (`apps/{app-slug}/dev/` runtime files) live in the CC workspace; this source defines the canonical contract those runtime artifacts mirror.
- **Relationship to [RULE] Workspace Topology**: Anchored. Imports WT §4.6.3 walking-skeleton output canonical set; introduces `apps/{app-slug}/dev/` as a sub-element of WT §4.6.3 Output #6 (binding declaration pending §4.6.3 explicit enumeration in a future WT revision).
- **Relationship to [RULE] Claude Code Architecture Rules**: Anchored. `apps/{app-slug}/dev/` extends CCAR §Y.1 app-scoped tree; future §Y.1 enumeration follows §Y.2 path-stability procedure.
- **Relationship to [MECH] Development Track Workflow**: Anchored. TK-04 produces dev-loopback artifacts as part of walking_skeleton output (DTW §4.0.2); TK-05 + TK-08 consume the stack; TK-13 gates on §6 assertions when unit is `walking_skeleton`.
- **Relationship to [MECH] CI/CD Milestone Policy**: Anchored. Walking-skeleton M5 acceptance (CI/CD §2.6) is supplemented by the four §6 dev-loopback-specific assertions; failure blocks M5.
- **Relationship to [MECH] Code Quality Rule Set**: Companion. Placeholder source code is subject to standard CQ §1 / §2 / §3 / §5 / §7 enforcement; the `NOT FOR PROD` annotation in §4.2 is for ENV-switch detection per §5, not a quality waiver. The §4.4 secret-loading contract is the **positive-side** declaration paired with CQ's **negative-side** enforcement (CQ §1.7 gitleaks + CQ §1.2 `hdc/no-inline-secret-literal` custom rule + CQ §4.6 secret leakage detection). Same-revision pairing per [OS] §8.5.2 applies.
- **Relationship to [MECH] Tools Health Cadence**: Anchored. Tools Health Cadence §3 step 8 (dev-loopback startup verification) consumes §6 walking-skeleton M5 acceptance assertions; Tools Health Cadence §5.4 inventories the `hashicorp/vault` image used in §4.4.
- **Relationship to [MECH] Application Lifecycle Handoff**: Inter-unit. Dev-loopback implementations persist across handoff per §7 (NOT decommissioned). `apps/{app-slug}/HANDOFF.md` (this source) is intentionally distinct from `apps/{app-slug}/handoff-record.md` (Handoff §4.3) — technical migration guide vs governance acknowledgment.
- **Pairings I participate in**: P-13 (with [MECH] CI/CD §2.6), P-14 (with [RULE] WT §4.6.3), P-15 (with [RULE] CCAR §Y.1 + §Y.2), P-21 (with `apps/{app-slug}/dev/**` + `HANDOFF.md`), P-37 (with [MECH] Application Lifecycle Handoff §3.1 + §4.3), P-38 (with [MECH] DTW §4.0.2 + TK-04 / TK-05 / TK-08 / TK-13), P-51 (with [MECH] Tools Health Cadence §3 step 8 + §5.4), P-53 (with [MECH] CQ §1.7 + §1.2 + §4.6)

## How to use this source

Use this source when:
- Authoring a Phase 1 TDD §3 walking-skeleton scope section (this source's §6 is referenced rather than restated)
- Designing the `apps/{app-slug}/dev/` directory contents during Phase 1 walking_skeleton unit execution
- Reviewing a walking_skeleton unit's M5 acceptance evidence for dev-loopback completeness
- Designing a placeholder implementation for any handoff-to-human integration item (SSO, notification publisher, secrets store, orchestration target, transport security, etc.) — see §4.0 Tier A / Tier B classification for whether the item requires a code-layer placeholder or only a configuration-switch contract
- Configuring how dev-time secrets are loaded — see §4.4 secret loading contract (Vault dev mode + seed file pattern)
- Authoring or reviewing the `apps/{app-slug}/HANDOFF.md` migration document at handoff time
- Judging whether a startup detection failure under non-dev ENV is a canonical violation
- Re-entering an application to AI-dev per [MECH] Application Lifecycle Handoff §5 — verifying that the new app's dev-loopback satisfies this source independently

## Do not use as

- A specification of which production tools the app uses for SSO, secrets, KMS, orchestration, tracing, object storage, or messaging (those are instance-level decisions made in phase TDD §1 / §2; this canonical specifies only the dev-loopback placeholder requirement, not the production target)
- A repository layout reference ([RULE] Claude Code Architecture Rules §Y.1)
- A walking-skeleton output canonical set reference ([RULE] Workspace Topology §4.6.3)
- A milestone gate semantics reference ([MECH] CI/CD Milestone Policy §2.6 owns the M5 baseline; this source supplements it for walking_skeleton)
- A handoff event mechanics reference ([MECH] Application Lifecycle Handoff §4 owns the tag, transfer form, and acknowledgment)
- A test-plan template ([TPL] Test Plan YAML Schema)
- A deployment / release-stage specification
- A negative-side lint or scanning rule reference for secret leakage ([MECH] Code Quality Rule Set §1.7 / §1.2 / §4.6 owns those; this source owns only the positive-side contract in §4.4)

---

# 1. Scope of applicability

This source applies to:

- **All HDC-internal applications** developed via the Claude Code Development Track, regardless of phase or feature scope
- **All `unit_type` values** in the unit catalog defined in [MECH] Development Track Workflow §4.0: `walking_skeleton`, `feature`, and `app_integration`. The dev-loopback stack is established by the Phase 1 `walking_skeleton` unit (per §6) and is consumed by every subsequent unit of any type within the same `{app-slug}`

This source does NOT apply to:

- Applications hand-coded by a human development team without Claude Code involvement (no such case is currently in scope; if a future case arises, that work is outside this canonical's authority)
- Applications that have been handed off and are receiving enhancement exclusively by the human dev team (the canonical applies to the AI-dev environment artifacts, which the receiving team inherits but is not bound to maintain in their own development practice)

The dev-loopback contract is binding on the application's `main`-branch state during the AI-dev period and at handoff time; what the receiving team does with it after handoff is governed by their own practice, not this source.

---

# 2. Single-command startup requirement

## 2.1 Fixed entry path

Every application must place its dev-loopback orchestration file at the canonical path:

```
apps/{app-slug}/dev/docker-compose.yaml
```

The `dev/` subdirectory is reserved for development-environment artifacts only. No production deployment configuration shall be placed under `apps/{app-slug}/dev/`.

## 2.2 Single-command contract

The dev-loopback stack must be brought up with a single command executed from the app directory:

```
cd apps/{app-slug}/dev && docker compose up -d
```

No additional setup steps (manual database seeding, manual secret generation, manual Vault initialization, multi-stage initialization scripts) shall be required between cloning the repository and the single command. Bootstrap actions (fixture injection, schema migration, secret seeding under dev ENV per §4.4) must be embedded inside the compose stack as init containers, application startup hooks, or compose dependency declarations.

## 2.3 Stack readiness ceiling

Stack readiness must be reached within **60 seconds** of `docker compose up -d` completing. Stack readiness is defined as: every compose service reports `healthy` via its compose-level healthcheck.

A stack that has not reached readiness within 60 seconds shall be treated as a startup failure. Operators and CI/CD pipelines must enforce this ceiling as a hard timeout, not as a soft target.

## 2.4 Required application endpoints

Every application service in the dev-loopback stack must expose two HTTP endpoints used by the compose healthcheck:

| Endpoint | Semantics |
|---|---|
| `/health` | Liveness probe — service process is running and responsive |
| `/ready` | Readiness probe — service has completed initialization (configuration loaded, dependent services reachable, secrets retrieved from dev Vault per §4.4, fixtures injected if applicable) and is ready to accept traffic |

The compose stack's healthcheck configuration shall poll `/ready`, not `/health`, to determine readiness. `/health` is reserved for liveness-only signaling.

---

# 3. Test fixture mandatory content

## 3.1 Role coverage

The fixture set must contain at least one local account for **every business role** declared in the application's phase PRD role catalog. Role enumeration is the phase PRD's canonical responsibility; this source binds fixture coverage to that enumeration.

If the phase PRD declares `n` business roles, the fixture set shall contain at least `n` accounts, one per role. Multiple accounts per role are permitted and encouraged where role-based access logic is non-trivial.

## 3.2 Aggregate-root state coverage

For each versioned aggregate-root type declared in the phase TDD's data model section (when any such type exists), the fixture set must contain at least:

- One record in `ACTIVE` state
- One record in `DRAFT` state

Applications without versioned aggregate-root types are exempt from this clause; the fixture set need only satisfy §3.1 in that case.

## 3.3 Fixture path

Fixture content must reside at:

```
apps/{app-slug}/dev/fixtures/
```

The internal organization of `fixtures/` (per-role subdirectories, per-aggregate-root subdirectories, format choice) is at the discretion of the walking_skeleton unit's authoring node, but the directory itself is canonical.

## 3.4 Injection trigger

Fixture injection shall occur:

- At application startup
- ONLY when the runtime ENV value (per §5) is `dev`

Non-dev ENV values must NOT trigger fixture injection. Detection of fixture injection logic firing under non-dev ENV is a startup-blocking violation per §5.2.

---

# 4. Placeholder default-implementation requirement

## 4.0 Two-tier classification of handoff-to-human integration items

Handoff-to-human integration items partition into two tiers based on whether the dev-loopback and the production target share the same code or share only an interface:

| Tier | Definition | Example items | Dev-loopback pattern |
|---|---|---|---|
| **Tier A — Configuration-switch** | Same application code runs in dev-loopback and in production; only environment variables, configuration values, and injection wiring change. Protocol layer is shared (e.g., OIDC for SSO, Vault SDK for secrets, JDBC URL for DB connection) | SSO (OIDC / SAML), secrets injection (via Vault SDK per §4.4), TLS certificate provisioning, database connection string, observability endpoint (tracing / metrics collector URL), object storage endpoint | Code reads from environment variables / configuration / dev-time Vault (per §4.4 for secrets); dev-loopback supplies dev-grade values via docker-compose `environment:` block (trivial config) or via Vault dev mode (secrets per §4.4); production supplies production-grade values via the receiving company's secret management. No placeholder interface or default implementation is needed at the code layer; the "placeholder" is the dev-grade configuration value (or dev Vault seed value), not a code construct |
| **Tier B — Implementation-switch** | Dev-loopback uses a code-layer placeholder implementation that satisfies the same interface as the production implementation but with different behavior (e.g., log-only vs real SMTP, in-memory vs real audit logger) | Notification publisher (LogOnly vs real SMTP / IM / SMS), audit logger (console vs SIEM connector), message queue (in-process vs real broker), if production-side requires custom integration code | Code defines an interface; dev-loopback supplies a default implementation satisfying §4.2's four-element pattern; production supplies the real implementation. Switching is wiring-level (DI container, factory selection) rather than configuration-value |

Both tiers must be enumerated in `apps/{app-slug}/HANDOFF.md` per §7.2, but the migration content differs by tier (see §7.2).

**Classification basis (12-Factor App Principle III, "Store config in the environment")**: Tier A items have no code-layer placeholder because the application code never directly couples to dev vs prod implementation — it reads from environment (or for secrets, from a uniformly-accessed Vault SDK whose endpoint changes between dev and prod). Tier B items do require a code-layer placeholder because the dev behavior is functionally different (logging vs sending email) and cannot be encoded as configuration values.

**Trivial configuration vs secret-class material**: trivial non-secret configuration (port numbers, log levels, ENV name, Vault endpoint URL, feature flags) is supplied via the docker-compose `environment:` block directly; it is committed in `docker-compose.yaml` and the operator does not maintain a separate `.env` file. Secret-class material (database passwords, API keys, JWT signing secrets, OAuth client secrets, tokens, certificates) is supplied via the Vault dev mode pattern per §4.4. This separation matches the production analog: in production, trivial config typically comes from environment / configmap, secret-class material comes from the company-side Vault (or equivalent secret manager).

## 4.1 Coverage rule

Every handoff-to-human integration item in the application must have a dev-loopback implementation. A handoff-to-human integration item is any external dependency that the application will rely on in production but that the human dev team is responsible for connecting to a real service after handoff.

No handoff-to-human integration item may be left unimplemented in the dev-loopback stack on the rationale that the production target is unavailable. The dev-loopback's purpose is to make the application end-to-end runnable independent of any external real service.

## 4.2 Placeholder implementation pattern

The four-element pattern below applies to **Tier B** items (implementation-switch). Tier A items follow the configuration-switch pattern described in §4.0 (and §4.4 for the secret-class subset) and do not require a code-layer placeholder interface; their dev-loopback "implementation" is the dev-grade configuration value plus the compose service supplying it (e.g., a Keycloak dev instance for OIDC, a local MinIO instance for object storage, a Vault dev mode instance for secrets per §4.4). Tier A items are still subject to §5 ENV switch gate detection.

Every Tier B placeholder implementation must follow the four-element pattern:

| Element | Requirement |
|---|---|
| Interface contract | The placeholder and the production implementation must share an explicit interface boundary (interface, protocol, or abstract class per the language idiom) |
| Default impl | A working implementation that satisfies the interface, runs locally without external dependency, and produces functionally correct outputs for development and test purposes |
| Test coverage | Unit tests verifying the placeholder satisfies the interface contract; the same test suite must also be runnable against the real production implementation when configured |
| Annotation | Explicit `NOT FOR PROD` annotation in the source code (comment, attribute, or decorator per the language idiom) and corresponding documentation in the application's `apps/{app-slug}/HANDOFF.md` per §7 |

## 4.3 Typical placeholder categories

The following are illustrative — neither exhaustive nor brand-binding. Applications declare their own list in `apps/{app-slug}/HANDOFF.md`. Each item must have a corresponding ENV-switch path defined per §5. The Tier column classifies per §4.0.

| Production target category | Tier | Dev-loopback pattern |
|---|---|---|
| Identity provider / SSO (OIDC / SAML protocol) | A | Local password fallback authentication via dev-grade IDP config (e.g., Keycloak in compose, or library-mode OAuth provider); application code uses OIDC client with configurable issuer URL |
| Cloud secret manager / KMS | A | Vault dev mode in compose per §4.4; code uses Vault SDK with configurable `VAULT_ADDR`; dev-grade secrets seeded from `apps/{app-slug}/dev/vault-seeds.json` (committed mock values) plus optional `apps/{app-slug}/dev/vault-seeds.local.json` (gitignored real-token overrides if needed) |
| Production transport security (TLS) and DNS | A | Self-signed certificates or plain HTTP under dev ENV; code uses configurable URL |
| Production tracing backend | A | Tracing exporter endpoint pointing to local OTLP collector in compose, or no-op exporter; code uses OpenTelemetry SDK uniformly |
| Production object storage | A | Local-filesystem-backed S3-compatible store (e.g., MinIO) in compose; code uses S3 SDK with configurable endpoint |
| Database (PostgreSQL / etc.) | A | Compose-launched DB instance with dev credentials sourced from dev Vault per §4.4; code uses configurable JDBC URL |
| Email transport / Notification publisher | B | Log-only notification publisher writing structured logs; production replaces with real SMTP / IM / SMS implementation |
| Audit logger | B | Console / local-file audit logger; production replaces with SIEM connector |
| Production messaging / queue | B | In-process or local-container queue with the same interface; production replaces with managed broker when requiring custom integration code beyond endpoint URL |
| Production container orchestrator | (N/A) | Single-machine Docker Compose stack; orchestrator selection is a deployment-environment concern, not an in-application integration |

Tier A items are configuration-switch (12-Factor III; for secret-class material, refined by §4.4) and require no in-code placeholder beyond reading config values or Vault SDK calls; Tier B items follow §4.2's four-element placeholder pattern. The category names above are abstract. Specific brand selections (whether for the dev-loopback or the production target) are owned by the phase TDD §1 / §2, not by this source.

## 4.4 Secret loading contract

### 4.4.1 Mechanism

The dev-loopback stack includes a Vault dev mode service. Application services in the same compose stack read secret-class material via the Vault SDK against this dev Vault, using the same code path that would run against the production Vault in the receiving company's environment.

**Compose service**: the dev Vault service uses the `hashicorp/vault` image in development mode (in-memory storage, auto-unsealed, fixed root token via `VAULT_DEV_ROOT_TOKEN_ID`).

**Seeding pattern**: the dev Vault is automatically populated at compose startup from two sources:

| File | Purpose | Git status |
|---|---|---|
| `apps/{app-slug}/dev/vault-seeds.json` | Mock seed values for every secret key the application reads at runtime; values are obvious dev-only literals (e.g., `"dev-db-password"`, `"dev-jwt-signing-key-32-bytes-mock-only"`) | Committed |
| `apps/{app-slug}/dev/vault-seeds.local.json` | Optional override file containing real tokens for third-party API testing during dev; loaded after `vault-seeds.json` and overrides keys present in both | Gitignored |

The compose stack runs a seeding step (init container, depends-on relationship, or `/docker-entrypoint-initvault.d/` script) that reads both files (committed first, local override second when present) and writes their content to the dev Vault's KV-v2 store under paths the application code references.

**Application code access**: application code uses the Vault SDK appropriate to its language (e.g., `node-vault` or equivalent for Tier 2; `spring-vault` or `vault-java-driver` for Tier 3) and reads secrets via KV-v2 paths (typically `secret/data/{app-slug}/{key}`). The Vault SDK call site is the only secret-access pattern in application code; `process.env` is reserved for trivial configuration only.

**Vault endpoint configuration**: `VAULT_ADDR` and `VAULT_TOKEN` are supplied via the compose `environment:` block as trivial configuration (not secrets — these are the access-path-bootstrapping values). Under dev ENV, `VAULT_ADDR=http://vault:8200` and `VAULT_TOKEN` is the fixed dev root token (e.g., `dev-root-token`); under non-dev ENV, the application expects production-grade values supplied by the receiving company's CI/CD wiring and uses AppRole or equivalent production-grade authentication.

### 4.4.2 Operator load profile

The operator's per-secret load under this contract:

| Operator action | Frequency | Load |
|---|---|---|
| Add a new secret key the application reads | Once per new key | Add an entry to `vault-seeds.json` with a mock value (AI agent can generate the file edit); no other operator action |
| Update a mock secret value | Rare | Edit `vault-seeds.json` |
| Provide a real third-party API token for dev testing | Occasional | Create or edit `vault-seeds.local.json` (gitignored); never committed |
| Rotate the dev Vault root token | Never required during dev (in-memory store; fresh on each `docker compose up`) | 0 |

The operator does NOT maintain a `.env` file for secrets. Trivial configuration (PORT, NODE_ENV, LOG_LEVEL, VAULT_ADDR, VAULT_TOKEN-under-dev, feature flags) lives in `docker-compose.yaml`'s `environment:` block, authored by AI agents and committed as code.

### 4.4.3 Handoff implications

At handoff, the receiving team's CI/CD wiring replaces dev Vault with the company-side Vault. The required changes are:

| What changes | What does NOT change |
|---|---|
| `VAULT_ADDR` env var value (now points to company Vault) | Application code Vault SDK call sites (paths and access pattern remain identical) |
| Authentication method (AppRole / token-helper / cloud-IAM-bound, replacing dev root token) | Application code `process.env.VAULT_TOKEN` lookup (the env var name is preserved; the value comes from a different supply mechanism) |
| Vault namespace / policy bindings (company-side governance) | Vault KV-v2 paths the application reads (e.g., `secret/data/{app-slug}/{key}`) — receiving team is responsible for ensuring company Vault contains these paths |
| Optional: migration from KV-v2 to a different secret-engine if company standard differs | The Vault SDK library import in application source |

These changes fall within the §7.2 HANDOFF.md "Production secrets injection flow" category. The contract narrows the secret-integration scope of handoff rework to the configuration and authentication adapter layer, rather than scattering rework across every secret access site in application code.

### 4.4.4 Forbidden patterns

The following patterns violate this §4.4 contract:

- Application source code reading secret-class material from `process.env` (other than `VAULT_ADDR` / `VAULT_TOKEN` themselves) — secrets must flow through Vault SDK calls
- Secret-class literals committed to source files (caught by [MECH] CQ §1.7 gitleaks + §1.2 `hdc/no-inline-secret-literal`)
- A `.env` file present at `apps/{app-slug}/dev/.env` or repo-root `.env` containing secret-class material
- `vault-seeds.local.json` committed to git (must be `.gitignore`d)
- `vault-seeds.json` containing real production tokens (mock-only)
- Vault SDK calls in production-target code that lack a matching dev-Vault-seeded path (would produce silent KV-miss under dev ENV)

---

# 5. ENV switch gate

## 5.1 ENV enumeration

Every application must read an `ENV` value at startup. The canonical enumeration is:

| ENV value | Meaning |
|---|---|
| `dev` | Local developer machine, AI-dev assigned_node, or any non-CI dev environment. Placeholder implementations active; fixtures injected per §3.4; dev Vault reachable at `VAULT_ADDR=http://vault:8200` with fixed dev root token |
| `staging` | M5 staging environment per [MECH] CI/CD Milestone Policy §2.6. Tier B placeholders may be active where the staging environment lacks real upstream connectivity; Tier A items use staging-grade configuration values; dev-grade secrets and fixtures must NOT be present; Vault SDK calls target staging-grade Vault endpoint |
| `prod` | Production environment on the receiving company's CI/CD infrastructure. The AI-dev environment does **not** execute applications under `prod` ENV — the AI-dev CI pipeline only triggers `dev` and `staging`. The `prod` ENV contract is preserved in source code for company-side execution after handoff per [MECH] Application Lifecycle Handoff. All placeholders (both Tier A configuration and Tier B implementation) must be replaced with real implementations / real configuration; all secrets must be production-grade and sourced from company Vault per §4.4.3; no fixtures |

Other ENV values are not canonical. Applications introducing ENV variants beyond the three above must reconcile with this source first.

## 5.2 Mandatory startup detection items

At startup, every application service must perform the following four detection items. Any failure must result in startup failure with explicit error logging and process exit code `1` so that container orchestration and Compose healthchecks recognize the service as unhealthy.

| # | Detection item | Failure condition |
|---|---|---|
| 1 | Secret strength | Under `staging` or `prod` ENV, detection of a dev-grade JWT signing key, dev-grade database password, dev-grade API key, or any other credential pattern matching a dev-baseline value → startup failure + block. This detection covers Tier A items whose dev-vs-prod differentiation is configuration-value (per §4.0). Includes detection of the dev Vault root token (e.g., `dev-root-token` or any value matching `VAULT_DEV_ROOT_TOKEN_ID` patterns from the dev compose stack) appearing as `VAULT_TOKEN` under non-dev ENV. |
| 2 | Vault endpoint | Under `staging` or `prod` ENV, detection of `VAULT_ADDR` pointing to a known dev-loopback value (e.g., `http://vault:8200`, `http://localhost:8200`, or any hostname matching the dev compose service name) → startup failure + block. |
| 3 | Active placeholder | Under `prod` ENV, detection of any Tier B placeholder implementation still active (i.e., not replaced by its real implementation) → startup failure + block. Tier A items are configuration-switch and do not produce code-layer "active placeholder" signals; they are governed by rows 1-2 (secret strength, Vault endpoint) and equivalent configuration-value detection. The AI-dev environment does not execute `prod` ENV, so this detection fires only on company-side production execution after handoff. |
| 4 | Fixture injection | Under any non-`dev` ENV, detection of fixture injection logic firing → startup failure + block |

## 5.3 Failure handling contract

Detection failure must:

- Emit an explicit, machine-readable error code in the application log identifying which detection item failed
- Exit the process with code `1`
- Not retry — the failure indicates a configuration violation, not a transient fault

The compose / orchestrator healthcheck integration shall recognize the exit-code-1 termination as service failure and halt the dependent stack accordingly.

---

# 6. Walking-skeleton M5 acceptance

## 6.1 Supplemental acceptance assertions

The Phase 1 `walking_skeleton` unit's M5 acceptance per [MECH] CI/CD Milestone Policy §2.6 is supplemented by the following four dev-loopback-specific assertions. All four must pass at TK-13 for the walking_skeleton unit's M5 to complete.

| # | Assertion | Verification |
|---|---|---|
| 1 | Single-command full-stack startup | `docker compose up -d` from `apps/{app-slug}/dev/` brings the full stack to readiness within the §2.3 ceiling; all compose services report `healthy`, including the dev Vault service per §4.4.1 and any seeding step that populates dev Vault from `apps/{app-slug}/dev/vault-seeds.json` (and, if present, `vault-seeds.local.json`) |
| 2 | All-roles login | At least one local account per business role declared in the phase PRD role catalog logs in successfully through the application's UI or BFF authentication path |
| 3 | At least one complete business flow end-to-end | One business flow representative of the phase PRD's core user value passes from UI entry through BFF and (where applicable) domain layers, including persistence and retrieval, with secrets successfully retrieved from dev Vault per §4.4 |
| 4 | Schema migration tool locked and working | Migration tool (Flyway or Liquibase) selection committed to `apps/{app-slug}/HANDOFF.md` as a locked Decision Record; first migration script under `apps/{app-slug}/db/migrations/` brings an empty PG instance to the baseline schema (full §8.7 table set per the phase PRD) when `docker compose up -d` runs. Per [MECH] CI/CD Milestone Policy §2.8.2. |

## 6.2 TDD reference rule

The Phase 1 TDD §3 walking-skeleton scope section shall **reference** this source's §6 rather than restate the assertions. Specifically, the dev-loopback acceptance content lands inside `§3.Milestone-choreography-and-acceptance-criteria` (template side: [TPL] Technical Design Document Template §2.3.6) under the M5 acceptance entry. A TDD instance complying with this source's §6 contains a one-line cross-reference of the form:

```
Walking-skeleton M5 acceptance per [MECH] Dev-Loopback Mode §6.
```

This canonical owns the dev-loopback acceptance content as its single source of truth; restating the assertions inline in TDD instances introduces canonical-instance drift risk and is forbidden. When this source's §6 is revised, no TDD instance edit is required (the instance reference remains valid by construction).

## 6.3 Failure routing

Failure on any §6.1 assertion routes per the standard M5 failure path in [MECH] CI/CD Milestone Policy §2.6 (auto rollback + Notification + back to TK-13 or earlier). The dev-loopback canonical does not introduce new failure routing semantics; it adds gating criteria within the existing M5 gate.

---

# 7. Relationship to [MECH] Application Lifecycle Handoff

## 7.1 Persistence rule

The dev-loopback implementation does NOT replace the production handoff. When the Application Lifecycle Handoff triggers (handoff to human dev team per [MECH] Application Lifecycle Handoff §3 and §4), the dev-loopback implementation is **retained** in the handoff content set. Its purpose after handoff is:

- Regression rehearsal (the receiving team can replay the application's behavior locally without provisioning the production stack)
- Emergency fallback (when a production environment incident requires reproduction)
- Onboarding (new members of the receiving team can run the application end-to-end on day one)

Removal or obsolescence of the dev-loopback implementation is not authorized at handoff time. The dev Vault service and `vault-seeds.json` per §4.4 are included in the retained set; `vault-seeds.local.json`, being gitignored, does not transfer (this is intentional — the receiving team supplies their own real-token overrides if regression rehearsal requires external API connectivity).

## 7.2 Handoff document content requirement

The handoff document at `apps/{app-slug}/HANDOFF.md` must contain, at minimum, three categories of placeholder migration content. Content within each category is structured by Tier per §4.0, and the secret-class subset of Tier A is further detailed per §4.4.

| Category | Tier A content (configuration-switch) | Tier B content (implementation-switch) |
|---|---|---|
| Real integration steps | Production-grade configuration values to set (env var names, Vault paths for secret-class Tier A items per §4.4, endpoint URLs to point at); no code change required | Step-by-step procedure for replacing the §4.2 placeholder implementation with its production target (interface mapping, dependency wiring, deployment changes) |
| ENV-switch checklist | Per-item verification: production configuration value reachable and dev-grade value absent under `prod` ENV (typically via §5.2 row 1 secret-strength detection + row 2 Vault endpoint detection) | Per-placeholder verification: production implementation wired and active; placeholder implementation no longer in DI container / factory under `prod` ENV (§5.2 row 3) |
| Production secrets injection flow | For each secret-class Tier A item per §4.4: the Vault KV-v2 path the application reads (e.g., `secret/data/{app-slug}/{key}`), the authentication method change (dev root token → AppRole / IAM / etc.), and the `VAULT_ADDR` value to set; the receiving team must ensure company Vault contains the listed paths and populate them with production-grade values | Per-placeholder description of any credential / token / certificate the real implementation requires (referencing the application's secret-management category, without binding the production tool selection) |

The Tier A vs Tier B split exists so the receiving team's onboarding effort is proportional to actual code-layer complexity: Tier A items are configuration tasks (their CI/CD platform's secret-injection wiring + Vault path population), Tier B items require implementation-swap or wiring changes. The AI-dev side produces the env-var contract, the Vault path catalog, and the placeholder code; the receiving team produces the production wiring.

`apps/{app-slug}/HANDOFF.md` is distinct from `apps/{app-slug}/handoff-record.md` (which is the acknowledgment artifact owned by [MECH] Application Lifecycle Handoff §4.3). Both files may coexist in the same handoff content set; the former is technical migration guidance authored by the AI-dev side, the latter is governance acknowledgment authored after the receiving team confirms.

## 7.3 Re-entry consistency

When an application re-enters the AI-dev environment under the independent-app approach per [MECH] Application Lifecycle Handoff §5, the new app-slug's Phase 1 walking_skeleton unit produces a fresh dev-loopback satisfying this canonical from scratch. The original app's dev-loopback artifacts may be referenced as historical input but are not mechanically inherited.

---

# 8. Anti-drift red flags

## 8.1 Path stability obligation

The `apps/{app-slug}/dev/` extension introduced by this canonical creates a paired-revision obligation per [RULE] Claude Code Architecture Rules §Y.2. The next revision of [RULE] Claude Code Architecture Rules §Y.1 shall enumerate `apps/{app-slug}/dev/` (with the compose file, fixtures subdirectory, `vault-seeds.json` per §4.4, and placeholder-impl convention) as a sub-element of the app-scoped tree; the next revision of [RULE] Workspace Topology §4.6.3 shall enumerate `apps/{app-slug}/dev/` as a sub-element of Output #6 (the walking-skeleton end-to-end runnable proof). Until those revisions land, the cross-references in the metadata block of this canonical are the binding declarations and take precedence by [OS] §8.7a.

## 8.2 Secret loading contract drift

Drift signals specific to §4.4:

- An app's `apps/{app-slug}/dev/docker-compose.yaml` lacks a Vault service or omits the seeding step
- `vault-seeds.json` missing or empty despite the application reading from Vault paths
- `vault-seeds.local.json` committed to git (must be gitignored)
- Application code reading secret-class material via `process.env` other than `VAULT_ADDR` / `VAULT_TOKEN`
- `.env` file present at `apps/{app-slug}/dev/` or repo root containing secret-class material
- Vault SDK calls in application code referencing paths not present in `vault-seeds.json` (silent KV-miss under dev ENV)
- §6.1 assertion 1 (single-command startup) marked passing without Vault service health verification
- HANDOFF.md missing the §4.4 Vault path catalog under the "Production secrets injection flow" category
- Vault seeded with real production tokens in `vault-seeds.json` (mock-only — real tokens go in gitignored `vault-seeds.local.json`)

These drift signals are detected via execution-time verification per §6.1 and via [MECH] CQ §10 anti-drift red flags' secret-loading-contract section (the lint and scanning enforcement). This source owns the policy-level drift catalog; CQ owns the lint-enforcement-level drift catalog. The two sets are complementary.
