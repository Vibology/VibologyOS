---
tags: [#system, #workflow, #guide]
date_created: 2026-01-08
status: reference
---

# Workflow Guide: The Streamlined Process

**Document Purpose:** Quick reference for the Fetch → Refine → Commit cycle.

---

## The Three-Phase Cycle

### Phase 1: Fetch (The Scribe)

**Command:** `/fetch [topic]`

**What Happens:**
- NotebookLM skill retrieves raw "Prima Materia" from the notebook
- Data presented in terminal buffer as clinical, archival format
- Tables for structured data, bullets for concepts
- No interpretation, no synthesis—just pure information

**Voice:** Clinical, objective, maximum density

**Example:**
```
/fetch Projector Type mechanics
```

---

### Phase 2: Refine (The Weaver)

**What Happens:**
- Apply Weaver persona to the raw material
- Debate, synthesize, cross-reference across the Seven Pillars
- Integrate Jungian terminology, Tarot correspondences, mythological parallels
- Emerge the "Third Meaning" through dialogue

**Voice:** Scholarly, evocative, numinous

**No command needed—this is conversational synthesis**

---

### Phase 3: Commit (Fixation)

**Command:** `/commit [path/filename]` or manual instruction

**What Happens:**
1. Apply YAML frontmatter with proper tags, system, entity_id, date
2. Add [[double-bracket links]] for key esoteric terms
3. Write file to specified location in `~/VibologyOS/`
4. Update `◈ System/Master Index.md` if adding to Active Synthesis
5. Create git commit with meaningful message

**Git Commit Format:**
```bash
git commit -m "Add [synthesis piece name]

[Optional: 2-3 line context about what was synthesized and why]"
```

---

## File Organization

### Where Things Go

**Synthesis Pieces** (refined, permanent knowledge):
- `⚛ Synthesis/[Topic Name].md`
- Example: `⚛ Synthesis/Projector_Invitation_as_Jungian_Call.md`

**Library Content** (foundational reference):
- `📖 Library/[Pillar]/[Category]/[File].md`
- Example: `📖 Library/Human Design/Types/Projector.md`

**Personal Charts/Transits**:
- `👤 Biographical Information/[Analysis Name].md`
- Example: `👤 Biographical Information/2026 Esoteric Insights.md`

**System/Planning**:
- `◈ System/[Document Name].md`
- Examples: Master Index, Library Build Strategy, Technical Setup

---

## Navigation

### Finding What Exists

**Check Master Index:**
```bash
cat "◈ System/Master Index.md"
```

**Search by keyword:**
```bash
grep -r "keyword" ~/VibologyOS/
```

**View recent work:**
```bash
git log --oneline
```

**See what changed:**
```bash
git diff HEAD~1  # Compare with previous commit
git show [commit-hash]  # Show specific commit
```

---

## Maintenance

### After Creating Synthesis Work

1. ✅ File written with YAML and [[links]]
2. ✅ Master Index updated (if Active Synthesis piece)
3. ✅ Git commit created with description

### Periodic Review

**Weekly:** Check Master Index for phase completion status

**Monthly:** Review Active Synthesis section for cross-reference opportunities

**Quarterly:** Audit [[double-bracket links]] for broken references

---

## Git Discipline

### When to Commit

- **After each synthesis piece** (Weaver-refined work)
- **After completing Library phase** (e.g., all 32 Human Design files)
- **After significant updates** to existing files
- **Before major restructuring** (safety checkpoint)

### Commit Message Structure

**Format:**
```
[Brief summary: what was added/changed]

[Optional body: why this matters, what decisions were made,
context that git diff can't show]
```

**Good Examples:**
```
Add 2026 Esoteric Insights: Jan-Feb transit analysis

Synthesized Aquarius stellium with biographical context,
HD mechanics, and Seven Pillars integration.
```

```
Complete Phase 1: Human Design core mechanics

32 files created (Types, Strategy/Authority, Centers, Profiles).
Tier 1 consultations now enabled.
```

**Bad Examples:**
```
Update files
```

```
More work on astrology stuff
```

---

## Custom Commands

### Available Slash Commands

**`/fetch [topic]`**
- Retrieves raw data from NotebookLM
- Scribe persona (clinical, archival)
- Terminal buffer only—no file write

**`/commit [path]`**
- Takes refined synthesis from conversation
- Applies YAML frontmatter and [[links]]
- Writes to vault
- Updates Master Index
- Creates git commit

---

## The Efficiency Gain

### Old Process (Deprecated)
- Update Session Summary: ~20 min
- Update Master Index: ~5 min
- **Total overhead: 25+ minutes/session**

### New Process (Current)
- Update Master Index (if synthesis piece): ~1 min
- Git commit message: ~2 min
- **Total overhead: 3 minutes/session**

**Time saved: 22 minutes per session**

---

## Quick Reference Card

| Need | Action |
|------|--------|
| Get raw data | `/fetch [topic]` |
| Refine synthesis | Dialogue with Weaver persona |
| Save to vault | `/commit [path]` or manual |
| Find what exists | Check Master Index |
| See session history | `git log` |
| Review changes | `git diff` or `git show` |
| Navigate content | Start at `📖 Library/Start Here.md` |

---

*Workflow established: 2026-01-08 | Optimized for solo practitioner efficiency*
