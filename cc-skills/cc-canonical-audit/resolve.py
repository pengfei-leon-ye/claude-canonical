#!/usr/bin/env python3
"""Deterministic reference resolver — mechanical backstop for the cc-canonical-audit skill.

Mechanizes the skill's D2 (registry / roster parity) and D3 (dead references) so they
no longer depend on a thorough AI sweep — the failure mode behind real misses
(the 2026-06-15 DS-mirror P1; audit false-positives on registered references).
Conservative by design: flags only high-confidence findings. The skill's AI pass still
owns the judgment dimensions (D1 structural, D4 cross-file, D5 staleness, D6 self-conformance).

Boundary ([OS] §1.4): reads only the passed CC repo (CLAUDE.md + .claude/**). Hub
[HANDLE] citations are form-checked, never resolved into the Hub mirror. Bare Hub
acronyms (DTW, THC, …) are treated as prose, not citations (decided option c).

Usage:  resolve.py <cc-repo-path>
Output: "SEV  MRn  location  problem" per finding; trailing tally on stderr.
Exit:   1 if any P0/P1 finding, else 0.
"""
import re
import subprocess
import sys
from pathlib import Path

KNOWN_HANDLES = {"OS", "PI", "REF", "RULE", "MECH", "PRIN", "POL", "TPL", "UP", "PK"}
ROSTER_SKILL = ".claude/skills/hdc-development-track/SKILL.md"

FIND = []


def flag(sev, mr, loc, msg):
    FIND.append((sev, mr, loc, msg))


def git_ls(repo, *globs):
    r = subprocess.run(["git", "-C", str(repo), "ls-files", *globs],
                       capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if l]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: resolve.py <cc-repo-path>")
    repo = Path(sys.argv[1]).resolve()
    files = git_ls(repo, "CLAUDE.md", ".claude/**")
    text = {f: (repo / f).read_text(encoding="utf-8", errors="replace")
            for f in files if (repo / f).is_file()}
    md = {f: t for f, t in text.items() if f.endswith(".md")}

    rules = {Path(f).stem for f in files
             if f.startswith(".claude/rules/") and f.endswith(".md")}
    skills = {Path(f).parts[2] for f in files
              if f.startswith(".claude/skills/") and f.endswith("SKILL.md")}
    agents = {Path(f).stem for f in files
              if f.startswith(".claude/agents/") and f.endswith(".md")}
    INV = {"rule": rules, "skill": skills, "agent": agents}
    PATH = {"rule": lambda n: repo / f".claude/rules/{n}.md",
            "skill": lambda n: repo / f".claude/skills/{n}/SKILL.md",
            "agent": lambda n: repo / f".claude/agents/{n}.md"}

    # ---------- MR1  roster parity across the explicit A{n} mirrors ----------
    # Scope the table parse to the "## Subagent roster" section only — the skill
    # also carries a TK execution table (| A1 | unit fail... |) that would otherwise
    # mis-capture outcome cells as agent names.
    roster_src = md.get(ROSTER_SKILL, "")
    m_sec = re.search(r"^##\s+Subagent roster\b.*?(?=^##\s)", roster_src, re.M | re.S)
    tbl = dict(re.findall(r"\|\s*(A\d+)\s*\|\s*([a-z][a-z0-9-]+)",
                          m_sec.group(0) if m_sec else ""))
    hook = {}
    for f, t in text.items():
        if f.endswith("subagent-ledger-gate.py"):
            hook.update(dict(re.findall(r'"(A\d+)":\s*"([a-z0-9-]+)"', t)))
    h1 = {}
    for f, t in text.items():
        if f.startswith(".claude/agents/"):
            m = re.search(r"^#\s*(A\d+)\s*[—-]\s*([a-z][a-z0-9-]+)", t, re.M)
            if m:
                h1[m.group(1)] = m.group(2)
    for code in sorted(set(tbl) | set(hook) | set(h1)):
        pairs = {("skill-table", tbl.get(code)), ("hook", hook.get(code)), ("agent-h1", h1.get(code))}
        names = {n for _, n in pairs if n}
        if len(names) > 1:
            seen = {s: n for s, n in pairs if n}
            flag("P1", "MR1", f"roster:{code}", f"A-code maps to differing names across mirrors: {seen}")
    roster_names = set(tbl.values()) | set(hook.values()) | set(h1.values())
    for n in sorted(agents - roster_names):
        flag("P1", "MR1", f".claude/agents/{n}.md", "agent file present but absent from the A-code roster mirrors")
    for n in sorted(roster_names - agents):
        flag("P1", "MR1", f"roster:{n}", "agent named in roster but no .claude/agents/<name>.md file")

    # ---------- MR2  token resolution  (rule|skill|agent `<name>`) ----------
    referenced = set()
    tok = re.compile(r"\b(rule|skill|agent)\s+`([a-z0-9-]+)`")
    for f, t in md.items():
        for i, line in enumerate(t.splitlines(), 1):
            for kind, name in tok.findall(line):
                referenced.add(name)
                if name not in INV[kind]:
                    sev = "P0" if f.endswith("CLAUDE.md") else "P1"
                    rel = PATH[kind](name).relative_to(repo)
                    flag(sev, "MR2", f"{f}:{i}", f"{kind} `{name}` does not resolve to {rel}")

    # ---------- MR3  section anchors (carrier-adjacent §<title>) ----------
    sec = re.compile(r"\b(rule|skill|agent)\s+`([a-z0-9-]+)`[^\n]{0,40}?§([A-Za-z][\w-]*)")
    hdr_cache = {}

    def headers(name, kind):
        p = PATH[kind](name)
        if p not in hdr_cache:
            try:
                body = p.read_text(encoding="utf-8", errors="replace")
                hdr_cache[p] = [norm(h) for h in re.findall(r"^#{1,6}\s*(.+)$", body, re.M)]
            except OSError:
                hdr_cache[p] = None
        return hdr_cache[p]

    for f, t in md.items():
        for i, line in enumerate(t.splitlines(), 1):
            for kind, name, title in sec.findall(line):
                if name not in INV[kind]:
                    continue  # MR2 owns the missing-carrier case
                hs = headers(name, kind)
                if hs is None or not norm(title):
                    continue
                if not any(norm(title) in h for h in hs):
                    flag("P1", "MR3", f"{f}:{i}", f"{kind} `{name}` §{title} — no matching section header in target")

    # ---------- MR4  Hub-citation form (bracketed handles only) ----------
    cite = re.compile(r"\[([A-Z]{2,5})\](?!\()")
    for f, t in md.items():
        for i, line in enumerate(t.splitlines(), 1):
            for h in cite.findall(line):
                if h not in KNOWN_HANDLES and re.search(r"\[" + h + r"\][^\n]{0,60}§", line):
                    flag("P2", "MR4", f"{f}:{i}", f"[{h}] used in citation position but not a known Hub handle")

    # ---------- MR5  orphans (rule/skill/agent never referenced) ----------
    allbt = set()
    for t in md.values():
        allbt.update(re.findall(r"`([a-z0-9-]+)`", t))
    refset = referenced | roster_names | allbt
    for n in sorted(rules):
        if n not in refset:
            flag("P1", "MR5", f".claude/rules/{n}.md", "rule file unreferenced (orphan)")
    for n in sorted(skills):
        if n not in refset:
            flag("P1", "MR5", f".claude/skills/{n}/SKILL.md", "skill unreferenced (orphan)")
    for n in sorted(agents):
        if n not in refset:
            flag("P1", "MR5", f".claude/agents/{n}.md", "agent unreferenced (orphan — and not in the roster)")

    # ---------- output ----------
    rank = {"P0": 0, "P1": 1, "P2": 2}
    for sev, mr, loc, msg in sorted(FIND, key=lambda x: (rank[x[0]], x[1], x[2])):
        print(f"{sev}  {mr}  {loc}  {msg}")
    tally = {s: sum(1 for x in FIND if x[0] == s) for s in ("P0", "P1", "P2")}
    print(f"\n# resolve.py: {len(FIND)} finding(s) — "
          f"{tally['P0']} P0, {tally['P1']} P1, {tally['P2']} P2", file=sys.stderr)
    sys.exit(1 if (tally["P0"] or tally["P1"]) else 0)


if __name__ == "__main__":
    main()
