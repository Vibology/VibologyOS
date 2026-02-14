# Phase 1: Source Text Conversion Assessment

**Date:** 2026-02-13
**Status:** Active - Pilot pillar identified
**Purpose:** Convert The Athenaeum PDFs (200 files, 1.9 GB) to markdown with YAML frontmatter

---

## Executive Summary

**Key Findings:**
- ✓ **OCR Status:** 95%+ of tested PDFs have clean, extractable text
- ⚠️ **OCR Required:** Minimal (Ptolemy Tetrabiblos confirmed, possibly a few others)
- ✓ **Extraction Tools:** `pdftotext` available and working (`/opt/homebrew/bin/pdftotext`)
- **Scope:** ~4000-5000 total pages across 199 PDFs

**Pilot Pillar Selected:** **Astrology**
- 8 PDFs, 220 MB, ~4000 pages
- Representative challenges: modern texts + classical sources, one OCR case
- Manageable scope for workflow establishment
- Critical foundational pillar

---

## Pillar-by-Pillar Assessment

### 1. Astrology (8 PDFs, 220 MB)

| File | Pages | Text Quality | Notes |
|------|-------|--------------|-------|
| Chris Brennan - Hellenistic Astrology | 698 | ✓ Clean | Modern scholarly work |
| Liz Greene - Jung's Studies in Astrology | 245 | ✓ Clean | Psycho-astrology synthesis |
| Liz Greene - Saturn: A New Look at an Old Devil | 202 | ✓ Clean | Foundational Greene work (11+ Library citations) |
| Liz Greene - The Astrological Neptune | 635 | ✓ Clean | Outer planet psychology |
| Liz Greene - The Astrology of Fate | 386 | ✓ Clean | Traditional nodes interpretation |
| Ptolemy - Tetrabiblos | 200 | ⚠️ **OCR NEEDED** | Scanned images, Greek characters garbled |
| Vettius Valens - Anthologies (Annotated) | 708 | ✓ Clean | Modern translation/annotation by Riley |
| William Lilly - Christian Astrology | 894 | ✓ Clean | Medieval transmission |

**Total:** ~4000 pages, 87.5% clean extraction, 12.5% OCR needed

**Complexity Assessment:**
- **Structure:** Author-focused organization, mostly single-volume works
- **Formatting:** Mix of academic (footnotes, indices) and popular (chapters, sections)
- **Special Elements:** Astrological glyphs, chart diagrams, tables (especially Valens)
- **OCR Challenge:** Ptolemy only (200 pages, classical Greek text sections)

**Conversion Priority:**
1. Start with clean Greene texts (establish workflow, templating)
2. Tackle Brennan (test large file handling, ~700 pages)
3. Handle Valens (test table preservation, annotations)
4. OCR Ptolemy last (establish OCR workflow separately)

---

### 2. Interdisciplinary (2 PDFs, 13 MB)

| File | Pages | Text Quality | Notes |
|------|-------|--------------|-------|
| Nicholas Culpepper - The Complete Herbal | ~300 | ✓ Clean | Project Gutenberg edition |
| Richard Alan Miller - Magical and Ritual Use of Herbs | ~120 | Not tested | Likely clean |

**Total:** ~420 pages

**Assessment:** Smallest pillar, cleanest extraction. Could be quick win but not representative of broader challenges.

---

### 3. The Tarot (67 PDFs, 423 MB)

**Standalone Texts (13 PDFs):**
- Aleister Crowley - Book of Thoth: ✓ Clean extraction tested
- Arthur Edward Waite - Pictorial Key to Tarot: Not tested
- Dion Fortune - Mystical Qabalah: Not tested
- Israel Regardie (2 works): Not tested
- Gareth Knight (2 volumes): Not tested
- Paul Foster Case, Rachel Pollack, Robert Wang: Not tested
- Sefer Yetzirah, Sefer ha-Bahir: Not tested (Hebrew primary sources)

**The Complete Zohar (54 PDFs):**
- Soncino Press translation organized by Torah portion (parasha)
- Includes: Safra de Tsniuta, Idra Raba, Idra Zuta
- Text quality: Unknown (not tested)
- Estimated 3000-4000 pages total

**Complexity Assessment:**
- **High volume:** 67 files, some very dense (Regardie Golden Dawn system)
- **Hebrew sources:** Sefer Yetzirah, Sefer ha-Bahir, Zohar (may have Hebrew text sections)
- **Zohar challenge:** 54 separate PDFs need consistent structure/linking
- **Special formatting:** Qabalistic diagrams, Tree of Life illustrations, Hebrew letters

**Recommendation:** Defer until after Astrology pilot. Zohar alone is a sub-project.

---

### 4. Personal Mythos (47 PDFs, 617 MB)

**Major Collections:**
- Jung Collected Works: 14 volumes (CW 1, 2, 4, 7, 8, 9.1, 10, 12, 13, 14, 15, 16, 17, 18)
- Marie-Louise von Franz: 9 works
- James Hillman: 5 works
- Campbell, Bettelheim, Edinger, Huxley, folklore: ~10 works

**Tested:**
- Joseph Campbell - Hero with a Thousand Faces: ✓ Clean extraction (commemorative edition)

**Complexity Assessment:**
- **High scholarly density:** Jung CW is canonical reference work
- **Footnotes/indices:** Extensive scholarly apparatus
- **Volume:** 47 files, estimated 6000-8000 pages
- **Special elements:** Diagrams (mandala imagery), cross-references within CW

**Recommendation:** Second or third conversion batch. Jung CW could be its own sub-project.

---

### 5. Human Design (75 PDFs, 622 MB)

**Structure:**
- Foundations (10 PDFs)
- Primary Health System (13 PDFs)
- Rave Psychology (13 PDFs)
- Variable & Transformation, Lunar & Planetary Color, Holistic Analysis, etc.

**Tested:**
- IHDS - Living Your Design Student Manual: ✓ Clean extraction, well-structured table of contents

**Complexity Assessment:**
- **Largest collection:** 75 files
- **Highly structured:** Educational curriculum with clear hierarchies
- **Specialized terminology:** Consistent HD vocabulary across all texts
- **Diagrams:** Bodygraph illustrations, charts, tables
- **Cross-references:** Curriculum materials reference each other

**Recommendation:** Good candidate for batch 2 or 3. Consistent structure means templating will be efficient once established.

---

## Pilot Pillar: Astrology (Detailed Plan)

### Why Astrology as Pilot?

1. **Manageable scope:** 8 files vs 75 (HD) or 67 (Tarot)
2. **Representative challenges:** Mix of modern + classical, clean text + OCR
3. **Critical foundation:** Most-cited pillar in current Library (Ptolemy 33+, Greene 4+, Valens 6+)
4. **Clear structure:** Author-based organization, mostly single volumes
5. **Workflow testing:** Tests both extraction AND OCR pipelines
6. **Template development:** Greene texts (4 similar works) perfect for YAML template refinement

### Pilot Conversion Workflow

**Phase 1A: Clean Text Extraction (7 PDFs)**

1. **Liz Greene - Saturn** (202 pages)
   - **Purpose:** Establish YAML frontmatter template, test chapter extraction
   - **Output:** One markdown file per chapter OR single file with heading hierarchy
   - **Special elements:** Astrological glyphs (♄, ♈, etc.), case study quotes

2. **Liz Greene - Neptune** (635 pages)
   - **Purpose:** Test large file handling, refine Greene template
   - **Special elements:** Myth references, psychological depth

3. **Liz Greene - Astrology of Fate** (386 pages)
   - **Purpose:** Apply refined template, test footnote preservation

4. **Liz Greene - Jung's Studies** (245 pages)
   - **Purpose:** Complete Greene corpus, validate template consistency

5. **Valens - Anthologies** (708 pages)
   - **Purpose:** Test table preservation, annotation handling (Riley's <> clarifications)
   - **Challenge:** Technical astrological tables, lot calculations, margin notes

6. **Brennan - Hellenistic Astrology** (698 pages)
   - **Purpose:** Test modern academic structure, extensive indices/glossaries

7. **Lilly - Christian Astrology** (894 pages)
   - **Purpose:** Test medieval structure, archaic language preservation

**Phase 1B: OCR Pipeline (1 PDF)**

8. **Ptolemy - Tetrabiblos** (200 pages)
   - **Purpose:** Establish OCR workflow for scanned classical texts
   - **Tools:** Tesseract OCR, manual cleanup required
   - **Challenge:** Greek text sections, classical terminology, scanned image quality

### Conversion Granularity Decision

**Options:**
1. **One file per book** — Simple, preserves original structure, huge files
2. **One file per chapter** — Medium granularity, good for reference, many files
3. **One file per major concept** — High granularity, matches current Library, requires editorial decisions

**Recommendation for Pilot:** Start with **one file per book**, assess usability, then decide on chapter-level splitting if needed. Preserve original TOC structure in markdown headings.

### YAML Frontmatter Template (Draft)

```yaml
---
title: "Saturn: A New Look at an Old Devil"
author: "Liz Greene"
date_published: 1976
publisher: "Samuel Weiser / CPA Press"
isbn: "978-1-57863-507-8"
pillar: "Astrology"
tags: [astrology, psycho-astrology, saturn, planets, archetypal-psychology]
source_type: "foundational_text"
library_status: "tier_1_critical"
citation_count: 11
date_converted: 2026-02-13
conversion_method: "pdftotext"
original_file: "Liz Greene - Saturn - A New Look at an Old Devil.pdf"
pages: 202
---
```

### Success Metrics for Pilot

- [ ] All 7 clean PDFs converted to markdown (Greene, Valens, Brennan, Lilly)
- [ ] YAML frontmatter template finalized and documented
- [ ] Astrological glyph handling standardized (Unicode vs [[wikilinks]])
- [ ] Chapter structure preserved and navigable
- [ ] Footnotes/endnotes converted to markdown format
- [ ] One OCR workflow documented (Ptolemy)
- [ ] Conversion protocol written for future batches
- [ ] Estimated time-per-page calculated for remaining pillars

---

## Tools & Infrastructure

### Extraction Tools

| Tool | Path | Purpose |
|------|------|---------|
| pdftotext | `/opt/homebrew/bin/pdftotext` | PDF → plain text extraction |
| pdfinfo | `/opt/homebrew/bin/pdfinfo` | PDF metadata (pages, size, etc.) |
| tesseract | TBD (install if needed) | OCR for scanned PDFs |

### Conversion Scripts (To Be Created)

1. **`convert_pdf_to_md.py`** — Automated extraction + YAML injection
2. **`batch_convert_pillar.sh`** — Run conversion across entire pillar folder
3. **`validate_conversion.py`** — Check YAML completeness, markdown formatting

### Output Structure (Proposed)

```
~/VibologyOS/Library/
  Source Texts/
    Astrology/
      Liz Greene/
        Saturn - A New Look at an Old Devil.md
        The Astrological Neptune.md
        The Astrology of Fate.md
        Jung's Studies in Astrology.md
      Ptolemy/
        Tetrabiblos.md
      Vettius Valens/
        Anthologies.md
      Chris Brennan/
        Hellenistic Astrology.md
      William Lilly/
        Christian Astrology.md
```

**Alternative:** One `Astrology.md` with all sources, separated by `## Author / Title` headers. Decide during pilot.

---

## Open Questions

1. **Granularity:** One file per book, or split by chapter?
2. **Wikilinks:** Should we create [[Author - Book Title]] links in synthesis work, or [[Book Title]] only?
3. **Diagrams:** How to handle astrological charts, bodygraph images, Tree of Life diagrams? (Inline SVG? External files? Text descriptions?)
4. **Cross-references:** Preserve original page numbers for citation integrity? (Yes, likely in YAML `pages: 202`)
5. **Zohar structure:** How to link 54 separate Zohar PDFs? (Master index? One combined file? Keep separate?)
6. **Jung CW structure:** 14 volumes — one file each, or combined? (Likely one per volume)

---

## Next Steps

1. **Create conversion script:** `convert_pdf_to_md.py` with YAML injection
2. **Test on Greene Saturn:** Pilot single-file conversion, refine YAML template
3. **Validate output:** Check glyph rendering, footnote preservation, structure
4. **Document learnings:** Update this file with time estimates, challenges encountered
5. **Iterate on remaining Greene texts:** Refine template based on Saturn learnings
6. **Expand to Valens, Brennan, Lilly:** Apply workflow to rest of Astrology pillar
7. **Establish OCR workflow:** Tackle Ptolemy separately
8. **Write protocol:** Create `PROTOCOL - Source Text Conversion.md` for future batches

---

## Timeline Estimate (Astrology Pilot)

**Conservative estimate:**
- Greene texts (4 books, ~1500 pages): 2-3 sessions
- Valens, Brennan, Lilly (~2300 pages): 3-4 sessions
- Ptolemy OCR (200 pages): 1-2 sessions
- Documentation, refinement: 1 session

**Total:** 7-10 focused sessions to complete Astrology pillar conversion.

**Full library estimate:** 40-60 sessions across all pillars (assumes workflow efficiency gains).

---

**Last Updated:** 2026-02-13
**Status:** Ready to begin Astrology pilot conversion
