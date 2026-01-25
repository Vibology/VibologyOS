---
tags: [system, protocol, verification, citation, esoteric-grimoire, quality-assurance]
date_created: 2026-01-24
date_updated: 2026-01-24
status: Active
---

# Prima Materia Verification Protocol

## Purpose

This protocol ensures that all content in the VibologyOS Library is **verifiable, traceable, and trustworthy**. Every factual claim must trace directly to source material in the **Esoteric Grimoire** (NotebookLM). This vault is intended to become the first access point for Vibology Synthesis work—there can be no doubt about its accuracy.

---

## Core Principle

**One Source, One Truth**

The **Esoteric Grimoire** (NotebookLM notebook: "Vibology: Seven Pillars Framework") is the sole authoritative source for prima materia. If content cannot be verified against this notebook, it must be:
1. Flagged as unverified
2. Marked as Vibology Synthesis (our original integration)
3. Removed if neither applies

---

## Source Hierarchy

### Primary Sources (Cite Directly)

These are texts **uploaded to the Esoteric Grimoire**. Cite them with full bibliographic detail:

| Source | In Grimoire | Citation Format |
|--------|-------------|-----------------|
| Bourgeault, *The Meaning of Mary Magdalene* (2010) | ✓ | (Bourgeault, p. XX) or (Bourgeault, Ch. X) |
| de Quillan, *The Gospel of the Beloved Companion* (2010) | ✓ | (de Quillan, Ch. XX:XX) |
| Gospel of Mary (Berlin Codex) | ✓ | (Gospel of Mary) |
| Gospel of Philip (NHL II,3) | ✓ | (Gospel of Philip) |
| Gospel of Thomas (NHL II,2) | ✓ | (Gospel of Thomas, Logion XX) |
| *[Add other uploaded sources as identified]* | | |

### Secondary Sources (Cite as "X cites Y")

When a primary source *mentions* another author or work not in the Grimoire:

**Correct:**
> Bourgeault cites Charles Williams's theology of "mystical substitution" (Bourgeault, Ch. 12).

**Incorrect:**
> Williams, Charles. *Descent into Hell*. 1937. ❌

Secondary sources are only valid insofar as a primary source discusses them. We cannot verify claims against books not in the Grimoire.

### Vibology Synthesis (Mark Clearly)

Original integrations created by us—not direct prima materia—must be clearly marked:

```markdown
> *Vibology Synthesis: The following framework integrates [Source A] with [Source B].*
```

Examples of Vibology Synthesis content:
- Seven-Coordinate Navigation (Z-axis framework)
- Cross-pillar mappings (Magdalene stages ↔ Tarot keys)
- Original interpretive frameworks

Synthesis content should still be *anchored* to verified sources where possible.

---

## Verification Workflow

### Per-File Process

1. **Read the existing file** to understand its claims
2. **Query Esoteric Grimoire** for verification of key concepts
3. **Compare** file content against retrieved prima materia
4. **Add inline citations** linking statements to specific sources
5. **Mark Vibology Synthesis** sections with blockquote notation
6. **Create References section** with complete bibliographic data
7. **Update YAML frontmatter** with verification metadata
8. **Commit** with meaningful message describing changes

### YAML Frontmatter Updates

Add to each verified file:

```yaml
date_updated: YYYY-MM-DD
verified: YYYY-MM-DD
verification_source: Esoteric Grimoire
```

### Inline Citation Format

Use parenthetical citations for readability:

```markdown
The Fifth Way is the path of conscious love practiced in committed partnership (Bourgeault, 109).
```

For chapter references when page numbers unavailable:

```markdown
Substituted love involves the voluntary bearing of burdens (Bourgeault, Ch. 12).
```

For Gnostic texts:

```markdown
The nous exists "between" soul and spirit as the organ of perception (Gospel of Mary).
```

### References Section Format

Place at the end of each file, before the final `---`:

```markdown
## References

*All citations trace to sources in the Esoteric Grimoire (NotebookLM).*

Bourgeault, Cynthia. *The Meaning of Mary Magdalene: Discovering the Woman at the Heart of Christianity*. Boston: Shambhala, 2010.
- Fifth Way definition: p. 109
- Kenosis as "non-clinging": p. 114
- Bourgeault cites Boris Mouravieff on Fifth Way: pp. 109–114

de Quillan, Jehanne. *The Gospel of the Beloved Companion: The Complete Gospel of Mary Magdalene*. CreateSpace, 2010.
- Eight Boughs of Ascent: Ch. 42
```

---

## Quality Gates

Before marking a file as verified, confirm:

- [ ] Every factual claim has inline citation
- [ ] All cited sources are in the Esoteric Grimoire
- [ ] Secondary sources attributed as "X cites Y"
- [ ] Vibology Synthesis sections clearly marked
- [ ] References section lists all cited sources
- [ ] YAML frontmatter includes `verified` date
- [ ] No orphaned claims (unsourced statements)

---

## Handling Unverified Content

### Content exists in file but NOT in Grimoire:

**Option A:** Mark as Vibology Synthesis if it's our original integration
**Option B:** Flag for later sourcing if the source exists but isn't uploaded
**Option C:** Remove if the content cannot be traced to any source

### Flagging for later sourcing:

```markdown
> *[Unverified: Source not in Esoteric Grimoire. Requires upload of [Book Title] to verify.]*
```

---

## Phased Execution Plan

Verification proceeds by pillar, smallest to largest:

| Phase | Pillar | Entries | Status |
|-------|--------|---------|--------|
| 1 | The Magdalene Path | 8 | **In Progress** |
| 2 | Core Foundations | 5 | Pending |
| 3 | Angelology | 31 | Pending |
| 4 | Astrology | 37 | Pending |
| 5 | Personal Mythos | 74 | Pending |
| 6 | The Tarot | 79 | Pending |
| 7 | The Window | 72 | Pending |
| 8 | Human Design | 337 | Pending |

**Total: 643 entries**

### Pace Control

- Maximum 10-15 entries per session (prevents fatigue, maintains rigor)
- One pillar at a time (no jumping between pillars mid-phase)
- Commit after each file or small batch
- Update this document after each milestone

---

## Progress Log

### Phase 1: The Magdalene Path (8 files)

| # | File | Status | Date | Notes |
|---|------|--------|------|-------|
| 1 | The Magdalene Path.md | ✅ Verified | 2026-01-24 | Overview; corrected Pope Gregory date (594 CE) |
| 2 | Anointing and Substituted Love.md | ✅ Verified | 2026-01-24 | Added Williams/Donne via Bourgeault |
| 3 | Kenosis - The Path of Self-Emptying.md | Pending | | |
| 4 | Mary Magdalene - Apostle and Beloved.md | Pending | | |
| 5 | Practices and the Lunar Cycle.md | Pending | | |
| 6 | Sources, Shadows, and Contemporary Practice.md | Pending | | |
| 7 | The Bridal Chamber and Sacred Union.md | Pending | | |
| 8 | The Eight Boughs of Ascent.md | Pending | | |

---

## Known Sources in Esoteric Grimoire

*Update this list as sources are confirmed:*

### Books
- Bourgeault, Cynthia. *The Meaning of Mary Magdalene* (Shambhala, 2010)
- de Quillan, Jehanne. *The Gospel of the Beloved Companion* (CreateSpace, 2010)

### Primary Texts
- Gospel of Mary (Berlin Gnostic Codex, BG 8502,1)
- Gospel of Philip (Nag Hammadi Codex II,3)
- Gospel of Thomas (Nag Hammadi Codex II,2)

### Pending Confirmation
- Karen King, *The Gospel of Mary of Magdala* (2003) — referenced in queries; confirm if uploaded
- *The Nag Hammadi Library in English* (Robinson, ed.) — text appears available; confirm edition

---

## Session Start Checklist

When resuming verification work:

1. Read this protocol document
2. Check `System/NEXT.md` for current priorities
3. Review Progress Log (above) for last completed file
4. Run `git log --oneline -5` to see recent commits
5. Continue with next pending file in sequence

---

## Revision History

| Date | Change |
|------|--------|
| 2026-01-24 | Initial protocol created; methodology established |
| 2026-01-24 | Clarified secondary source citation format |
| 2026-01-24 | Completed files 1-2 of Phase 1 |

---
