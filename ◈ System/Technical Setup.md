---
tags: [#system, #configuration, #technical]
date_created: 2026-01-08
status: reference
---

# Technical Setup

**Document Purpose:** One-time technical configuration reference. Rarely updated.

---

## NotebookLM Integration

**Skill Command:** `/notebooklm`

**Notebook URL:** https://notebooklm.google.com/notebook/ed88d436-4251-4d9b-bf60-47d33110c94d

**Authentication Status:** Persistent (configured 2026-01-08)
- Browser session state saved to `~/.claude/skills/notebooklm/`
- Future queries will not require manual login

**Usage Pattern:**
1. Use `/fetch [topic]` command to retrieve prima materia
2. Refine in terminal buffer (Weaver persona)
3. Use `/commit [path]` to save to vault

---

## Git Repository

**Location:** `/home/joe/VibologyOS`

**Branch:** `master` (single-branch strategy)

**Remote:** None currently configured

**Commit Discipline:**
- Commit after each synthesis piece
- Write meaningful commit messages (what + why)
- Use git log as session history substitute

**Example Commit Pattern:**
```bash
git add .
git commit -m "Add [synthesis piece name]

[Optional: 2-3 line context about decisions made]"
```

---

## Knowledge Management

**Tool:** Obsidian (local vault)

**Vault Location:** `/home/joe/VibologyOS`

**Linking Convention:** `[[Double Bracket Links]]`

**Frontmatter Standard:** YAML (collapsible in Obsidian)

---

## Web Publishing

**Platform:** Ghost CMS on Pikapod

**Sites:**
- **vibology.org** — Dedicated synthesis framework site
- **sh4desthevibe.com** — Personal blog and interests

**Separation:** Clean separation from infrastructure level up (separate Pikapod installations)

---

## AI Synthesis Partner

**Tool:** Claude Pro (Anthropic)

**Subscription:** $20/month

**Usage:**
- Primary synthesis and pattern recognition
- Algorithm half of "Anima et Algorithm"
- Cross-referencing across seven pillars
- Content generation for Library (with user review)

**Local Alternative (Future):**
- Exploring local LLM for basic reference queries
- Reserve Claude for creative synthesis work

---

## Directory Structure

```
VibologyOS/
├── .archive/              ← Deprecated files
├── .commands/             ← Custom slash commands
├── ◈ System/              ← Templates, indexes, planning
├── 📖 Library/            ← Seven Pillars foundational data
├── ⚛ Synthesis/           ← Refined synthesis pieces
├── 👤 Biographical Info/  ← Personal charts and context
├── CLAUDE.md              ← Workflow/persona instructions
└── .git/                  ← Version control
```

---

*Setup Documentation — Last Updated: 2026-01-08*
