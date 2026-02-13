# Library Restructure: Source Texts + Correspondence Tables

**Date Created:** 2026-02-13
**Status:** Planning / Prerequisites
**Goal:** Transform Library from interpreted entries to original source texts + Rosetta Stone correspondence mappings

---

## Vision

**Current State:**
Library consists of 747 interpreted entries written in synthesis voice — translation layer distances users from original sources.

**Proposed State:**
- **The Athenaeum** = original source texts converted to markdown + YAML (Crowley, Ra, Greene, etc.)
- **Correspondence Tables** = Rosetta Stone mappings between systems (the unique connective work)
- **Synthesis** = interpretive essays built on top of sources (clearly separated, in Synthesis/ folder)

**Why:**
- Preserve original voices (Crowley, Ra, Greene, etc.)
- Observatory principle: users look through original instruments, not my lens
- Correspondence tables = unique value (the connective work)
- Synthesis generated on-demand from source data, not pre-digested
- Scholarly integrity and verifiable mappings

### Philosophical Reframe: Five Pillars

**Vibology empowers people to understand and live their own Personal Mythos.**

The five pillars are **universal symbolic languages** with collective shared meaning — structured tools that can map anyone's archetypal landscape:

1. **Astrology** — planetary timing and cosmic positioning
2. **Human Design** — individual genetic imprinting and mechanical navigation
3. **Personal Mythos** — cultural archetypal encoding (Jung, folklore, collective symbols)
4. **Tarot** — Qabalistic pathways and archetypal progression (includes Qabalah)
5. **The Astrolabe** — contemporary archetypal resonance (includes I-Ching)

**Excluded from this project:**
- **Angelology** and **The Magdalene Path** are elements of the practitioner's personal spiritual practice, not universal client-work tools. These will be explored in a separate personal devotional project at a later date.

**Special case:**
- **The Astrolabe** requires no source text conversion — our synthesis work IS the source text (fully original pillar).

### Visual Identity: The Five Platonic Solids

The five pillars are represented by the **Five Platonic Solids** — the complete set of regular convex polyhedra (tetrahedron, cube, octahedron, dodecahedron, icosahedron).

**Why these symbols:**
- **Mathematical completeness** — Exactly five regular solids exist; no sixth is possible (proven mathematically)
- **Foundational structures** — The basic geometric vocabulary of three-dimensional space
- **Symbolic resonance** — Ancient association with elements (Plato's *Timaeus*), appear throughout nature and sacred geometry
- **Visual distinction** — Each solid has unique, recognizable silhouette

**Visual style:**
- Wireframe with dashed hidden lines (technical/architectural drawing aesthetic)
- Clean line art showing complete geometric structure
- Isometric/orthographic projection revealing multiple faces
- "Blueprint" rather than "icon" — shows the full instrument, not just facade

**Brand application:**
```
        VIBOLOGY
    ─────────────
    △  ◇  ◈  ▢  ⬟
   (Five Platonic solids as geometric icons)
```

Suitable for website headers, business cards, report section markers, Observatory app icon, client-facing materials.

---

## Prerequisites

### 1. Localize All Source Materials

**Current Locations:**
- NotebookLM (various notebooks)
- Google Drive
- Existing PDFs (scattered)
- Current Obsidian vault (has correspondence work)

**Action Required:**
Gather all source texts into a local staging directory before conversion can begin.

**Staging Location (Proposed):**
```
~/VibologyOS/.staging/athenaeum/
  Astrology/
    Liz Greene/
    Ptolemy/
    Vettius Valens/
  Human Design/
    Ra Uru Hu/
    Chaitanyo/
  Personal Mythos/
    Carl Jung/
    Joseph Campbell/
    Marie-Louise von Franz/
  Tarot/
    Aleister Crowley/
    Arthur Edward Waite/
    Israel Regardie/    # Qabalah sources
  # The Astrolabe — no source texts needed (original synthesis)
```

**Folder structure:** Pillar → Author (natural name order) → Source files (PDFs initially, markdown eventually)

---

## File Organization Standards

### Athenaeum Naming Conventions

**Structure:** Folder per author, title-only filenames (natural name order)

**Rationale:**
- **Scales for prolific authors** — Ra Uru Hu has 75+ lectures; flat `{Author - Title}` structure would clutter
- **Natural browsing** — "I want Ra's work" → one folder contains everything
- **Clean filenames** — No redundant author name on every file
- **Clear hierarchy** — Pillar → Author → Work
- **YAML handles search** — Each markdown has author metadata, grep finds anything regardless of folder structure
- **Human-readable** — Use names as you naturally say them ("Liz Greene" not "Greene, Liz")

**Examples:**
```
✓ Liz Greene/Saturn - A New Look at an Old Devil.md
✓ Ra Uru Hu/The Human Design System.md
✓ Carl Jung/Man and His Symbols.md

✗ Greene, Liz/Saturn.md              (formal cataloging, unnecessary)
✗ Liz Greene - Saturn.md             (flat structure, doesn't scale)
✗ Saturn - Liz Greene.md             (title-first, scatters authors)
```

**Special cases:**
- **Multi-author works** — Place in primary author's folder, note collaborators in YAML frontmatter
- **Single-name authors** — Use as-is (Ra Uru Hu/, Ptolemy/)
- **Disambiguation** — If multiple authors share a name, add context in folder name if needed (rare)

**Apply same structure to source PDFs now** — conversion to markdown will be straightforward when ready.

---

## Proposed Library Structure

```
Library/
  Core Foundations/
    CORRESPONDENCES - Master Rosetta Stone.md  ← Canonical cross-system map
    CORRESPONDENCES - Tarot ↔ Astrology ↔ Qabalah.md
    CORRESPONDENCES - HD Gates ↔ I-Ching ↔ Gene Keys ↔ Astrolabe.md
    CORRESPONDENCES - Zodiac ↔ Planets ↔ Tarot.md
    CORRESPONDENCES - [Other mappings as needed].md

  The Athenaeum/  # Source texts converted to searchable markdown
    Astrology/
      Liz Greene/
        Saturn - A New Look at an Old Devil.md
        The Astrological Neptune.md
        The Astrology of Fate.md
      Ptolemy/
        Tetrabiblos.md
      Vettius Valens/
        Anthologies.md

    Human Design/
      Ra Uru Hu/
        The Human Design System.md
        Rave I'Ching.md
        The Four Transformations.md
        [... 72 more lectures]
      Chaitanyo/
        Color Transference.md

    Personal Mythos/
      Carl Jung/
        Man and His Symbols.md
        Memories Dreams Reflections.md
        [CW volumes]
      Joseph Campbell/
        The Hero with a Thousand Faces.md
      Marie-Louise von Franz/
        [Works].md

    Tarot/
      Aleister Crowley/
        The Book of Thoth.md
      Arthur Edward Waite/
        The Pictorial Key to the Tarot.md
      Israel Regardie/
        The Tree of Life.md  # Qabalah integrated

  The Astrolabe/
    # No source texts — original synthesis work lives here
    [Existing Astrolabe entries remain as-is]
```

**YAML Frontmatter (Athenaeum Texts):**
```yaml
---
title: "The Book of Thoth"
author: "Aleister Crowley"
system: "Tarot"
collection: "The Athenaeum"
tags: [athenaeum, source-text, tarot, crowley, thoth]
date_created: YYYY-MM-DD
source_format: "PDF" # or "Epub", "Scanned", etc.
file_location: "Library/The Athenaeum/Tarot/Aleister Crowley/The Book of Thoth.md"
---
```

**Note:** With folder-per-author structure, YAML provides searchable metadata. Grep can find all works by an author, all works in a system, or specific titles regardless of directory hierarchy.

**YAML Frontmatter (Correspondences):**
```yaml
---
title: "Master Rosetta Stone"
type: correspondence-table
systems: [Astrology, Human Design, Personal Mythos, Tarot, The Astrolabe]
tags: [correspondences, rosetta-stone, cross-system]
date_created: YYYY-MM-DD
---
```

---

## Conversion Workflow (Once Localized)

### Phase 1: Source Text Conversion
1. Convert PDFs/epubs to markdown (OCR if needed)
2. Add YAML frontmatter with metadata
3. Structure by pillar/system
4. Preserve original formatting/voice as much as possible

### Phase 2: Correspondence Table Extraction
1. Extract existing correspondence work from current Obsidian vault
2. Cross-reference with source texts for accuracy
3. Build master Rosetta Stone document
4. Create pillar-specific correspondence maps
5. Verify mappings against multiple sources where possible

### Phase 3: Integration
1. Migrate correspondence tables to new Library structure
2. Update existing Synthesis essays to reference source texts
3. Create protocol for new synthesis (must cite sources)
4. Deprecate old interpreted Library entries to `.archive/`

---

## Key Correspondence Tables Needed

Based on five-pillar architecture and existing work:

1. **Master Rosetta Stone** — comprehensive cross-system map (all five pillars)
2. **Tarot ↔ Astrology ↔ Qabalah** — classic Golden Dawn correspondences + planetary rulerships
3. **HD Gates ↔ I-Ching ↔ Gene Keys ↔ Astrolabe** — hexagram mappings across systems
4. **Tarot ↔ Qabalah Paths** — 22 Major Arcana to 22 paths on Tree of Life
5. **Zodiac ↔ Planets ↔ Tarot** — astrological/archetypal synthesis
6. **HD Centers ↔ Chakras ↔ Planets** — energy center correspondences
7. **Personal Mythos ↔ Archetypal Patterns** — Jungian archetypes across systems (Shadow, Anima/Animus, etc.)
8. **[Additional mappings as synthesis work reveals them]**

---

## Source Material Inventory (To Be Completed)

**Astrology:**
- [ ] Liz Greene - Saturn: A New Look at an Old Devil
- [ ] Liz Greene - The Astrological Neptune and the Quest for Redemption
- [ ] Ptolemy - Tetrabiblos
- [ ] Vettius Valens - Anthologies
- [ ] ... [add as gathered]

**Human Design:**
- [ ] Ra Uru Hu - The Human Design System
- [ ] Ra Uru Hu - Rave I'Ching
- [ ] Ra Uru Hu - [Lecture series]
- [ ] ... [add as gathered]

**Personal Mythos:**
- [ ] Carl Jung - [Selected works]
- [ ] Joseph Campbell - [Selected works]
- [ ] [Folklore/mythological sources]
- [ ] ... [add as gathered]

**Tarot (including Qabalah):**
- [ ] Aleister Crowley - The Book of Thoth
- [ ] Arthur Edward Waite - The Pictorial Key to the Tarot
- [ ] Israel Regardie - The Tree of Life
- [ ] ... [add as gathered]

**The Astrolabe:**
- No source texts needed — original synthesis work (already complete)

---

## Next Steps

1. **Localize source materials** from NotebookLM, Google Drive, etc.
2. **Complete source inventory** (update checklist above)
3. **Assess conversion effort** (OCR needs, formatting complexity)
4. **Extract correspondence work** from current Obsidian vault
5. **Build pilot** — convert one pillar as proof-of-concept
6. **Refine workflow** based on pilot learnings
7. **Execute full conversion**

---

## Open Questions

### Architecture
- Should The Athenaeum be organized by pillar or by author?
- How to handle multi-volume works (Greene's planetary series, Ra's lectures)?
- Should correspondence tables live in Core Foundations or alongside source texts?
- What metadata beyond YAML is needed for source provenance?
- How to handle conflicting correspondences between source traditions?

### Observatory Integration
- **Contextual links problem:** Observatory currently links client data (Type, Authority, Profile, Gates, Channels) to synthesized Library entries (e.g., "Library/Human Design/Gates/Gate 01.md"). If we replace those with source texts, contextual lookup breaks. Source texts aren't organized granularly (one file per gate/profile/etc.) — they're organized by author/work/chapter.

**Possible approaches:**
1. **Thin synthesis layer** — keep minimal interpretive entries just for Observatory contextual links (separate from Athenaeum)
2. **Link to correspondences** — contextual links open relevant Rosetta Stone sections instead of interpretive entries
3. **Multi-reference approach** — contextual links show "See: [Ra lecture X], [Greene chapter Y], [Correspondence table Z]"
4. **Just-in-time synthesis** — Observatory generates synthesis on-demand from source texts when clicking links
5. **Hybrid model** — Athenaeum for deep study, Observatory-specific cache for quick contextual reference

**Decision pending:** Need to determine what contextual lookup should *be* in the new architecture. What's the right balance between scholarship (sources) and utility (quick answers)?

## Future Updates

**CLAUDE.md revision:**
Once library restructure is complete, update `CLAUDE.md` section §7 ("The Seven Pillars") to reflect five-pillar architecture and philosophical reframe. Angelology and The Magdalene Path will be noted as separate personal practice work (not part of client-facing Vibology framework).

---

**Status:** Awaiting source material localization before Phase 1 can begin.
