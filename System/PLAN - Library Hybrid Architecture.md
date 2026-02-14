# Library Hybrid Architecture: The Definitive Plan

**Date Created:** 2026-02-13
**Status:** ACTIVE — This is the authoritative plan
**Supersedes:** All previous library restructure plans

---

## Vision

Transform the Library from interpreted entries to a three-layer hybrid system:

1. **The Athenaeum** — Source PDFs remain as authoritative references (200 files, 1.9 GB)
2. **Correspondence Tables** — Cross-system Rosetta Stones mapping concepts between pillars
3. **Synthesis Documents** — Purpose-built contextual content for Observatory with clickable citations to sources

**The Observatory Principle Preserved:** Users look through original instruments (PDFs) while synthesis provides navigation and cross-referencing.

---

## Architecture Overview

```
~/Athenaeum/                           # Source PDFs (authoritative)
  Astrology/ (8 PDFs)
  Human Design/ (75 PDFs)
  Personal Mythos/ (47 PDFs)
  The Tarot/ (67 PDFs)
  Interdisciplinary/ (2 PDFs)

~/VibologyOS/Library/
  Correspondence Tables/               # Cross-system mappings (YAML)
    Master-Rosetta-Stone.yml
    Saturn-Cross-System.yml
    Planets-to-Gates.yml
    Tarot-to-Qabalah.yml
    [50-100 total tables]

  Synthesis/                           # Observatory contextual content (Markdown)
    Astrology/
      Planets/
        Saturn.md
        Jupiter.md
      Signs/
        Aries.md
      Houses/
        Fourth-House.md
    Human Design/
      Types/
        Generator.md
      Profiles/
        4-6-Opportunist-Role-Model.md
      Gates/
        Gate-60-Limitation.md
      Centers/
        Solar-Plexus.md
    Personal Mythos/
      Archetypes/
        Shadow.md
        Hero.md
    The Tarot/
      Major-Arcana/
        The-Devil.md
        The-World.md
      Sephiroth/
        Binah.md
    [100-200 total synthesis documents]
```

---

## Layer 1: The Athenaeum (Source PDFs)

**Location:** `~/Athenaeum/`
**Status:** ✓ Complete (200 files, Tier 1 & 2 acquisitions 100%)

### Current Holdings

| Pillar | Count | Status |
|--------|-------|--------|
| Astrology | 8 | 7 clean text, 1 OCR candidate |
| Human Design | 75 | Complete IHDS curriculum |
| Personal Mythos | 47 | Jung CW, von Franz, Campbell, folklore |
| The Tarot | 67 | 13 standalone + 54 Complete Zohar |
| Interdisciplinary | 2 | Herbalism texts |
| **TOTAL** | **199** | Ready for citation |

### File Naming Convention

**Pattern:** `Author-ShortTitle.pdf`

**Examples:**
- `Greene-Saturn.pdf`
- `Greene-Neptune.pdf`
- `IHDS-Rave-ABC.pdf`
- `Ra-Definitive-Book.pdf`
- `Crowley-Thoth.pdf`

### PDF Lookup Table

**File:** `System/source-pdf-map.yml`

```yaml
# Maps short names to full paths for Observatory
Greene-Saturn: "~/Athenaeum/Astrology/Liz Greene - Saturn - A New Look at an Old Devil.pdf"
Greene-Neptune: "~/Athenaeum/Astrology/Liz Greene - The Astrological Neptune and the Quest for Redemption.pdf"
IHDS-Rave-ABC: "~/Athenaeum/Human Design/Foundations/IHDS - Rave ABC - Level 1.pdf"
IHDS-LYD: "~/Athenaeum/Human Design/Foundations/IHDS - Living Your Design Student Manual.pdf"
Crowley-Thoth: "~/Athenaeum/The Tarot/Aleister Crowley - Book of Thoth.pdf"
# [Add all 199 PDFs]
```

---

## Layer 2: Correspondence Tables (Rosetta Stones)

**Location:** `Library/Correspondence Tables/`
**Format:** YAML (machine-readable, structured)
**Purpose:** Map concepts across the five pillars

### Master Rosetta Stone

**File:** `Master-Rosetta-Stone.yml`

Maps core concepts across all systems in one comprehensive table.

**Example structure:**
```yaml
# Master cross-system correspondences
saturn:
  astrology:
    planet: Saturn
    symbol: "♄"
    traditional_rulerships: [Capricorn, Aquarius]
    exaltation: Libra
    keywords: [limitation, structure, time, discipline, maturity, karma]
    sources:
      - "Greene-Saturn p.45-67"
      - "Ptolemy-Tetrabiblos 3.4"
  human_design:
    related_gates: [60, 38, 54]
    gate_60: "Limitation (Root Center)"
    gate_38: "Fighting Spirit (Root/Spleen)"
    gate_54: "Ambition (Root)"
    sources:
      - "IHDS-Rave-ABC p.234"
      - "Ra-Definitive-Book p.456"
  tarot:
    primary: "The World (XXI)"
    related: ["The Devil (XV)", "The Hermit (IX)"]
    sources:
      - "Crowley-Thoth p.123"
      - "Waite-Pictorial-Key p.89"
  qabalah:
    sphere: "Binah (Understanding)"
    path: "32 (Tau - The World card)"
    sources:
      - "Fortune-Mystical-Qabalah p.89"
      - "Knight-Qabalistic-Symbolism-Vol1 p.67"
  personal_mythos:
    archetypes: [Senex, Chronos, Taskmaster, Wise Old Man]
    sources:
      - "Greene-Saturn p.12-34"
      - "Jung-CW9.1 p.123"
```

### Specialized Correspondence Tables

**Create individual tables for specific mappings:**

1. **`Planets-to-Gates.yml`** — Astrological planets ↔ HD Gates
2. **`Planets-to-Tarot.yml`** — Planets ↔ Major Arcana
3. **`Zodiac-to-Gates.yml`** — Signs ↔ HD Gates (I-Ching correlations)
4. **`Tarot-to-Qabalah-Paths.yml`** — 22 Major Arcana ↔ 22 Paths on Tree of Life
5. **`HD-Centers-to-Chakras.yml`** — 9 Centers ↔ 7 Chakras ↔ Planets
6. **`Archetypes-Cross-System.yml`** — Jungian archetypes across all pillars
7. **`Elements-Cross-System.yml`** — Fire/Earth/Air/Water across systems

**Estimated total:** 50-100 correspondence tables

**Time per table:** 30-60 minutes (research, verification, YAML formatting)
**Total workload:** 25-50 hours

---

## Layer 3: Synthesis Documents (Observatory Content)

**Location:** `Library/Synthesis/`
**Format:** Markdown with clickable source citations
**Purpose:** Contextual content displayed when user clicks concepts in Observatory

### Citation Format

**Standard markdown link with custom URL scheme:**

```markdown
([Author, Book Title p.123: "key phrase"](source://PDF-name#page&q=search+terms))
```

**What happens when clicked:**
1. Observatory parses URL: `source://Greene-Saturn#45&q=unconscious+Saturn+fourth`
2. Looks up PDF path from `source-pdf-map.yml`
3. Opens PDF at page 45
4. Searches for "unconscious Saturn fourth"
5. **Highlights matching text** in yellow
6. Centers viewport on first match

**Example citation in context:**
```markdown
Greene describes the unconscious expression of Saturn in the fourth house
as potentially manifesting as "discontent and resentment" stemming from
feeling trapped by circumstances.

([Greene, Saturn p.45: "unconscious...fourth"](source://Greene-Saturn#45&q=unconscious+Saturn+fourth))
```

### Synthesis Document Template

**File:** `System/Templates/TEMPLATE - Synthesis Document.md`

```markdown
---
title: "[Concept Name]"
pillar: "[Astrology/Human Design/Personal Mythos/Tarot/Astrolabe]"
synthesis_type: "interpretive"
primary_sources:
  - "Greene-Saturn"
  - "IHDS-Rave-ABC"
related_concepts:
  - [[Related-Concept-1]]
  - [[Related-Concept-2]]
date_created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

## Overview

[2-3 paragraph synthesis of core concept, drawing from multiple sources]

([Citation 1](source://PDF-name#page&q=search+terms))
([Citation 2](source://PDF-name#page&q=search+terms))

## Key Themes

### Theme 1

[Interpretation with source backing]

([Citation](source://PDF-name#page&q=search+terms))

### Theme 2

[Interpretation with source backing]

([Citation](source://PDF-name#page&q=search+terms))

## Cross-System Correlations

**[Other Pillar 1]:** [Connection description]
([Citation](source://PDF-name#page&q=search+terms))

**[Other Pillar 2]:** [Connection description]
([See Correspondence Table](correspondence://Table-Name))

## Practical Application

[How this concept manifests in real life, client work, etc.]

([Citation](source://PDF-name#page&q=search+terms))

## Further Reading

- [Source Author, *Book Title* Chapter X](source://PDF-name#page)
- [Related synthesis document]([[Related-Synthesis-Document]])
```

### Document Granularity

**Hybrid approach — mix broad and granular based on content type:**

**Broad documents (one file covers category):**
- `Planets-Overview.md` (all 10 planets in one document with sections)
- `Zodiac-Signs.md` (all 12 signs)
- `HD-Types.md` (all 5 types)

**Granular documents (one concept per file):**
- Individual planets when deep dive needed: `Saturn.md`, `Pluto.md`
- Individual profiles: `4-6-Opportunist-Role-Model.md`
- Individual gates: `Gate-60-Limitation.md`
- Individual Major Arcana: `The-Devil.md`

**Estimated total:** 100-200 synthesis documents

**Time per document:** 1-2 hours (research, writing, citation verification)
**Total workload:** 100-400 hours

---

## Observatory Integration

### PDF Viewer Requirements

**Technical implementation (macOS/Swift/PDFKit):**

```swift
func openPDFCitation(url: URL) {
    // Parse: source://Greene-Saturn#45&q=unconscious+Saturn+fourth
    let pdfName = url.host // "Greene-Saturn"
    let page = extractPageNumber(from: url) // 45
    let searchTerms = extractSearchQuery(from: url) // "unconscious Saturn fourth"

    // Map to actual PDF path
    let pdfPath = lookupPDFPath(pdfName) // from source-pdf-map.yml

    // Load PDF
    guard let pdfDoc = PDFDocument(url: URL(fileURLWithPath: pdfPath)),
          let pdfPage = pdfDoc.page(at: page - 1) else { return }

    // Search for text on that page
    let selections = pdfPage.selections(for: searchTerms, options: [
        .caseInsensitive: true
    ])

    // Display in PDF view
    pdfView.document = pdfDoc
    pdfView.go(to: pdfPage)

    // Highlight matching text (built-in PDFKit feature)
    pdfView.highlightedSelections = selections

    // Scroll to first match
    if let firstMatch = selections.first {
        pdfView.go(to: firstMatch.bounds(for: pdfPage), on: pdfPage)
    }
}
```

### UI Layout Options

**Recommended: Split Pane**

```
┌──────────────────────┬──────────────────────┐
│                      │                      │
│  Synthesis Markdown  │   PDF Viewer         │
│  (scrollable)        │   (at cited page)    │
│                      │                      │
│  "The 4/6 is..."     │   [PDF content]      │
│  [citation] ←────────┼──→ Page 234          │
│                      │   [highlighted text] │
│                      │                      │
└──────────────────────┴──────────────────────┘
```

**Alternative: Popup/Modal**
- Citation click opens PDF in overlay
- Close to return to synthesis

**Alternative: Tabbed View**
- PDF opens in new Observatory tab
- Keep synthesis tab open
- Switch between as needed

---

## Migration from Current Library

**Current state:** 747 interpreted entries in `Library/`

**Strategy:** Phased selective migration

### Step 1: Archive Current Library

```bash
mkdir -p .archive/Library-v1-Interpreted
mv Library/* .archive/Library-v1-Interpreted/
```

Keep as reference while building new synthesis documents.

### Step 2: Identify High-Quality Entries

**Review criteria:**
- Well-sourced (even if not cited with page numbers)
- Accurate interpretations
- Good structure
- Minimal synthesis needed

**Action:** Mark these for preservation/migration

### Step 3: Extract Structure

Use good existing entries as templates for new synthesis documents:
- Heading structure
- Themes covered
- Cross-references
- Interpretive style

### Step 4: Rebuild with Citations

For entries being migrated:
1. Verify claims against source PDFs
2. Add page-specific citations
3. Update to new synthesis format
4. Add cross-system correlations

### Step 5: Write Net-New Synthesis

For concepts not well-covered in old Library:
- Start fresh using synthesis template
- Research from source PDFs
- Build citations as you write

**Timeline:** Gradual migration over 3-6 months alongside new synthesis work

---

## Implementation Phases

### Phase 1: Foundation (Weeks 1-2)

**Goal:** Build infrastructure and pilots

- [ ] Create `source-pdf-map.yml` (all 199 PDFs mapped)
- [ ] Create synthesis document template
- [ ] Create correspondence table template
- [ ] **Pilot synthesis:** Choose one concept to write completely
  - Option A: `Saturn.md` (high-value, cross-system rich)
  - Option B: `Generator.md` (personal relevance, HD-focused)
  - Option C: `4-6-Opportunist-Role-Model.md` (client-facing priority)
- [ ] **Pilot correspondence table:** `Saturn-Cross-System.yml`
- [ ] Test workflow: write → cite → verify in PDF

### Phase 2: Core Concepts (Weeks 3-8)

**Goal:** Build high-priority synthesis documents

**Astrology (20-30 documents):**
- [ ] All 10 planets (or broad `Planets-Overview.md`)
- [ ] Key signs (Aries, Cancer, Libra, Capricorn at minimum)
- [ ] Angular houses (1st, 4th, 7th, 10th)
- [ ] Major aspects (conjunction, square, trine, opposition)

**Human Design (30-40 documents):**
- [ ] All 5 types
- [ ] All 12 profiles (or grouped by line)
- [ ] All 9 centers
- [ ] Key gates (Gates 1-64 granular, or grouped by center)

**Personal Mythos (10-15 documents):**
- [ ] Shadow, Anima/Animus, Self, Persona
- [ ] Hero's Journey phases
- [ ] Key archetypes (Senex, Puer, etc.)

**The Tarot (20-30 documents):**
- [ ] All 22 Major Arcana
- [ ] 10 Sephiroth
- [ ] Key Qabalah concepts (Tree of Life, Paths, Qlippoth)

**The Astrolabe (5-10 documents):**
- [ ] I-Ching structure
- [ ] Key hexagrams
- [ ] Gene Keys framework (if synthesizing from HD)

### Phase 3: Correspondence Tables (Weeks 9-12)

**Goal:** Map all major cross-system connections

- [ ] Master Rosetta Stone (comprehensive)
- [ ] Planets ↔ Gates
- [ ] Planets ↔ Tarot
- [ ] Zodiac ↔ Gates
- [ ] Tarot ↔ Qabalah Paths
- [ ] Centers ↔ Chakras ↔ Planets
- [ ] Archetypes cross-system
- [ ] Elements cross-system
- [ ] [Additional specialized tables as needed]

### Phase 4: Observatory Integration (Parallel with Phases 2-3)

**Goal:** Build PDF viewer with citation support

- [ ] Parse `source://` URLs
- [ ] PDF lookup from `source-pdf-map.yml`
- [ ] PDFKit integration
- [ ] Search and highlight implementation
- [ ] UI layout (split pane recommended)
- [ ] Test with pilot synthesis documents

### Phase 5: Expansion (Ongoing)

**Goal:** Complete synthesis library and refine

- [ ] Fill gaps in synthesis coverage
- [ ] Add specialized topics as needed
- [ ] Migrate valuable content from old Library
- [ ] Refine based on usage patterns
- [ ] Add new sources as acquired

---

## Success Metrics

**Phase 1 (Foundation):**
- ✓ Pilot synthesis document written and cited
- ✓ Pilot correspondence table created
- ✓ Workflow tested and validated

**Phase 2 (Core Concepts):**
- ✓ 100+ synthesis documents created
- ✓ All major concepts covered across 5 pillars
- ✓ Citations verified and clickable

**Phase 3 (Correspondence Tables):**
- ✓ 50+ correspondence tables created
- ✓ Master Rosetta Stone complete
- ✓ Cross-system navigation seamless

**Phase 4 (Observatory Integration):**
- ✓ PDF viewer functional with highlighting
- ✓ Citations open to correct page and highlight text
- ✓ User can navigate synthesis → source → synthesis fluidly

**Phase 5 (Expansion):**
- ✓ 200+ synthesis documents (comprehensive coverage)
- ✓ Old Library migrated or deprecated
- ✓ System stable and maintainable

---

## Advantages Over PDF Conversion

**Compared to full PDF-to-markdown conversion:**
- ✓ No page header/footer cleanup
- ✓ No layout artifact removal
- ✓ Write exactly what Observatory needs
- ✓ Cite authoritative sources rather than duplicate
- ✓ **100-400 hours vs 1000+ hours** (estimated)

**Compared to current interpreted Library:**
- ✓ Source verification (every claim cited)
- ✓ Cross-system integration (correspondence tables)
- ✓ Purpose-built for Observatory (not generic entries)
- ✓ Clickable citations (instant source access)
- ✓ Easier to maintain and update

**The Observatory Principle:**
- ✓ Users look through original instruments (PDFs)
- ✓ Synthesis provides navigation and cross-referencing
- ✓ Sources remain authoritative and intact
- ✓ Scholarly integrity preserved

---

## Next Immediate Actions

**When ready to begin implementation:**

1. **Create pilot synthesis document**
   - Choose: Saturn / Generator / 4-6 Profile
   - Research from sources
   - Write with citations
   - Verify all citations open correctly

2. **Create pilot correspondence table**
   - Recommend: `Saturn-Cross-System.yml`
   - Map across all 5 pillars
   - Cite sources
   - Test in synthesis documents

3. **Create source PDF map**
   - `System/source-pdf-map.yml`
   - Map all 199 PDFs with short names

4. **Build Observatory PDF viewer** (parallel technical work)
   - Parse `source://` URLs
   - Implement PDFKit highlighting
   - Create split-pane UI

---

**This is the plan.** No other plans supersede this document.

**Last Updated:** 2026-02-13
