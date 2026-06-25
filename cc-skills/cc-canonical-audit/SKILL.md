---
name: cc-canonical-audit
description: Quality-audit Claude Code's own canonical sources — the hdc repo's CLAUDE.md + .claude/** (rules, skills, agents, hooks, config, settings) and the user-global claude-code-global.md — checking structural validity, registry/reference sync, dead references, cross-file consistency, staleness, and self-conformance. Operator-invoked, on-demand, read-only (it reports, never auto-fixes). Out of scope — memory (handled by consolidate-memory) and the claude.ai Hub mirror canonical/hdc/** (handled Hub-side by CFSA, never read).
disable-model-invocation: true
---

# CC Canonical Audit

Active QA of CC's own canonical sources. Operationalizes the declarative drift-signals in hdc rule `cc-canonical-discipline` §Anti-drift — plus structural, staleness, and self-conformance checks that rule states but does not execute. Read-only: emits an actionable report, never auto-edits canonical (a canonical fix triggers `cc-canonical-discipline` §Update-discipline + §Rule-change-propagation, which an unattended audit cannot discharge). Operator-invoked; never auto-fires.

## Scope

| Surface | In/Out | Judge against |
|---|---|---|
| `hdc/CLAUDE.md` + `hdc/.claude/**` — rules, skills, agents, hooks, config, settings.json | **IN — primary** | rule `cc-canonical-discipline`; `CLAUDE.md` §2 boundaries; the 4-carrier model |
| `canonical/claude-code-global.md` | **IN — secondary** | its own stated rules — marker discipline, heuristics-over-hardcoded, AI-consumption, Gates/Sensors structure, internal self-consistency |
| `~/.claude/projects/**/memory/**` | OUT → skill `consolidate-memory` | — |
| `canonical/hdc/**` (claude.ai Hub project canonical) | OUT → Hub-side CFSA | **never read** — CC canonical-source boundary |
| Gitignored per-node runtime: `worktrees/`, `settings.local.json`, `*.local.json`, `.transitions.log`, `.DS_Store`, `.git/` | OUT — not canonical content (content-skip; a *tracked* one is a D6 finding) | — |

**Hard boundary**: never read `canonical/hdc/**`. It is the claude.ai Hub mirror, audited Hub-side by CFSA; reading it to derive CC behavior violates the CC canonical-source boundary. Judge the two IN surfaces only.

## Procedure (CC runs inline — no subagents)

1. **Enumerate** the in-scope surface: git-tracked files under the two IN rows; skip every exempt path. Pull frontmatter from every `.claude/{skills,rules,agents}` file in one sweep. Drive all enumeration and reference sweeps with `git ls-files` / `git grep` (tracked files only) — never raw `grep -r` or `find`, which descend into gitignored `worktrees/` and inflate results.
2. **Run the deterministic resolver** — `python3 <skill-dir>/resolve.py <hdc-repo-path>` (`resolve.py` ships beside this SKILL.md). It mechanically discharges the resolvable parts of D2 / D3 as checks MR1–MR5 (roster parity · token resolution · §-anchor existence · Hub-citation form · orphans), so those no longer ride on a thorough manual sweep — the miss-mode behind real drift. Fold its findings into the report; exit 1 ⇒ ≥1 P0/P1. It never reads `canonical/hdc/**` (Hub handles form-checked only, [OS] §1.4); bare Hub acronyms are prose, not citations.
3. **Run the judgment dimensions** the resolver cannot mechanize — D1 structural, D4 cross-file consistency, D5 staleness, D6 self-conformance, plus any D2/D3 reasoning past mechanical resolution. Resolve-before-flag: resolve a handle/acronym against its registry before flagging it unknown.
4. **Emit** the actionable report (see Output).

Where a check needs a value mirrored into product code or CI config (`apps/*/**`, `tools/*.json`, `*.config.*`, `pom.xml`), the full grep may exceed audit altitude — flag as a slice-level follow-up candidate rather than asserting clean.

## Dimensions

Reference-resolution parts of D2/D3 are mechanized by `resolve.py` (MR1–MR5, Procedure step 2); the set below is the full audit including the judgment parts the script cannot do.

**D1 — Structural / schema validity**
- Skill: `skills/{name}/SKILL.md` present; frontmatter has `description` (required); `name`, if set, matches the dir.
- Rule: `rules/{name}.md` is EITHER `paths:`-scoped OR declared unconditional ("loads at session start"); one that is neither is ambiguous.
- Agent: `agents/{name}.md` has `name` + `description`; `context_scope`, if set, resolves to a scope in `config/context-scopes.yaml`; `tools` well-formed.
- Hook: every `command` in `settings.json` resolves to an existing file under `.claude/hooks/`; imported helpers (e.g. `_m4prep`) exist. A helper module is NOT required to be registered. `settings.json` parses.
- Config / data: every `config/*.yaml`, `tools/*.json` parses and is consumed by some artifact.

**D2 — Registry / reference sync** (`cc-canonical-discipline` §Anti-drift: "referenced but absent, or present but unreferenced")
- Every skill/rule/agent named in `CLAUDE.md` §4 map + §Subagents exists in `.claude/`.
- Every file in `.claude/{skills,rules,agents}/` is referenced from `CLAUDE.md` or another canonical file → unreferenced = orphan.
- **Subagent-roster parity** across its mirrors: `CLAUDE.md` §Subagents ↔ `config/context-scopes.yaml` `agent_assignments` ↔ `hooks/subagent-ledger-gate.py` `NAME`/`HARD_BY_UNIT` ↔ skill `hdc-development-track` roster (`cc-canonical-discipline` §Rule-change-propagation names this exact coupling). Account for documented role-based exclusions before flagging — e.g. an event-triggered reviewer legitimately absent from the per-slice M4 ledger gate is not a miss.

**D3 — Dead references**
- Any file / path / flag / skill / rule / agent / §-anchor named in a canonical file that no longer exists (systematizes the global-canonical "names a file → verify it still exists").
- Hub `[OS]/[REF]/[RULE]/[MECH]` citations are decoupled by design (CC cites Hub by name, never inlines, never resolves into `canonical/hdc/`). Check only that the citation token is well-formed — do NOT attempt to resolve its target.

**D4 — Cross-file consistency**
- `CLAUDE.md` ↔ rule/skill: no substantive duplication (`cc-canonical-discipline` §Anti-drift — detail lives once in the deepest carrier; `CLAUDE.md` references it).
- No two canonical files asserting contradictory values for the same threshold / gate / severity / path.
- A rule's value / threshold / schema vs its in-repo runtime mirror (config, code comment, `tools/*.json`, `vitest.config`, `pom.xml`, CI workflow) — `cc-canonical-discipline` §Rule-change-propagation; product-code reach is a follow-up candidate (see Procedure note).
- global `claude-code-global.md` ↔ hdc `CLAUDE.md`: a project instruction contradicting a global one is drift UNLESS the project file declares the override and its scope (e.g. rule `code-style` explicitly overriding the global no-comments default within `apps/*/src/**` is a legitimate scoped override).

**D5 — Staleness**
- `claude-code-global.md` calibration-history / model-version-bound assumptions whose model version is superseded (its own "model-version re-tune trigger").
- A constitutional rule (no Hub SOT) stated only in a CC file → `cc-canonical-discipline` §Anti-drift "promote to Hub" — flag as a promote-candidate (CC cannot promote; surfaces to operator).
- Dated content / review-date markers past their point.

**D6 — Self-conformance** (does the canonical obey the rules it states)
- AI-consumption regime (`cc-canonical-discipline` §Authoring-principle): a `.claude/**` file carrying narrative / onboarding / motivational padding, or rationale whose deletion would not change AI behavior.
- Naming: kebab-case / lowercase / ASCII / English; `hdc-` prefix on project-specific skills; reserved `CLAUDE.md` / `SKILL.md` respected.
- Carrier placement: an every-session fact buried in a skill instead of `CLAUDE.md`; a path-correlated topic placed as an unconditional rule (or vice-versa); a non-native `.claude/` subdir or custom loading mechanism holding canonical content; a tracked runtime-noise file (exempt list above).
- `CLAUDE.md` within its ≤200-line target.
- `claude-code-global.md` against its OWN preached discipline — marker completeness, heuristics-over-hardcoded altitude, Gates/Sensors structure intact.

## Output

Write `hdc/reports/cc-canonical-audit/{YYYY-MM-DD}.md` (primary, hdc surface) with a clearly-separated `## Secondary — claude-code-global.md` section. Directory materializes on first run.

**Retention** — transient QA snapshots: once every finding is actioned (fixed, or adjudicated no-change), clear the report — the fix commits are the durable trail. No retention obligation (unlike spec-drift's never-delete); do not accrete one report per run.

**Actionable-only** — every entry is a finding + recommendation, or it is cut; no "checked, clean" items. Lead with a one-line per-dimension tally; list dimensions with zero findings together on one `Clean: …` line (coverage stays visible without noise). Per finding: `severity · dimension · location (file:line) · problem · recommendation`. Order by severity.

- **P0** — breaks loading / correctness now: unparseable `settings.json` / config; a registered hook file missing; a skill/rule/agent referenced by `CLAUDE.md` but absent (a dead carrier pointer).
- **P1** — silent drift / latent defect: roster-mirror divergence; rule-value vs config mismatch; orphan artifact; dead reference; cross-file contradiction.
- **P2** — hygiene / staleness: stale calibration entry; AI-consumption padding; naming nit; `CLAUDE.md` over length; committed runtime noise.

If a run cannot complete a dimension at full depth (e.g. a product-code mirror grep deferred), say so in the tally — never present partial coverage as clean (no silent caps).

## Anti-drift (this skill)
- A "clean / all-good" report with no findings AND no explicit per-dimension tally (hides whether it actually ran).
- The audit editing canonical instead of reporting (read-only invariant crossed).
- `canonical/hdc/**` read during a run (boundary crossed).
- Memory content audited here instead of deferred to `consolidate-memory` (seam overlap).
- A finding asserted against product code without the follow-up-candidate caveat when the full grep was not run.
