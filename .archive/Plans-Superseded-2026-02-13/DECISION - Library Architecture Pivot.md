# Library Architecture Decision: Hybrid Approach

**Date:** 2026-02-13
**Status:** Under consideration — awaiting decision
**Context:** Phase 1 PDF conversion revealed significant challenges

---

## The Challenge

Full PDF-to-markdown conversion has quality issues:
- Page headers/footers create noise throughout documents
- Page numbers fragment paragraph flow
- Layout artifacts from multi-column pages
- Estimated 40-60 sessions of cleanup work for 200 PDFs
- Output quality varies significantly between sources

**Successful pilot:** Greene "Jung's Studies in Astrology" (226 pages) converted cleanly, but still contains page number artifacts and header/footer noise.

---

## Proposed Alternative: Hybrid Architecture

### Three-Layer System

**1. The Athenaeum** (Source PDFs)
- 200 PDFs remain in `~/Athenaeum/` as authoritative sources
- Searchable, readable, no conversion needed
- Organized by pillar (Astrology, HD, Personal Mythos, Tarot, Astrolabe)

**2. Correspondence Tables** (Rosetta Stones)
- Cross-system mappings in `Library/Correspondence Tables/`
- YAML format for machine-readability
- Example: Saturn → HD Gates 60/38/54 → Tarot Devil/World → Qabalah Binah
- Cite source PDFs by page number

**3. Synthesis Documents** (Observatory Content)
- Purpose-built markdown in `Library/Synthesis/`
- Written specifically for contextual display in Observatory
- 2-3 paragraph interpretations with source citations
- Cross-references to related concepts
- Links to PDF page numbers for deep reading

---

## Open Questions

### 1. Synthesis Document Granularity

**Option A: Broad** — One file per topic
- `Saturn-in-Houses.md` covers all 12 houses
- `HD-Gates.md` covers all 64 gates
- Fewer files, easier to maintain
- Harder to navigate, large files

**Option B: Granular** — One file per concept
- `Saturn-in-1st.md`, `Saturn-in-2nd.md`, etc.
- `Gate-01.md`, `Gate-02.md`, etc.
- Precise contextual matches, easier linking
- More files (~700+ documents)

**Option C: Hybrid** — Mix based on content type
- Broad for overviews (planets, houses, centers)
- Granular for specific applications (aspects, gates, cards)

### 2. Authoring Workflow

**Option A: Practitioner-written**
- You write synthesis documents manually
- Highest quality, authentic voice/perspective
- Time-intensive but less than PDF conversion
- Start with high-priority concepts (Saturn, Generator, Major Arcana)

**Option B: AI-assisted drafting**
- Claude drafts from source citations you provide
- You edit/refine for accuracy and voice
- Faster, but requires oversight and verification

**Option C: Hybrid**
- You write critical foundational entries
- Claude drafts supporting entries from verified sources
- All subject to your review and approval

### 3. Correspondence Table Format

**YAML:**
```yaml
# Saturn-Cross-System.yml
planet: Saturn
symbol: "♄"
astrology:
  keywords: [limitation, structure, time]
  sources: ["Greene Saturn p.45-67", "Ptolemy Tetrabiblos 3.4"]
human_design:
  gates: [60, 38, 54]
  sources: ["IHDS Rave ABC p.234"]
tarot:
  cards: ["The World (XXI)", "The Devil (XV)"]
  sources: ["Crowley Book of Thoth p.123"]
```

**Markdown:**
```markdown
# Saturn Cross-System Correspondences

**Astrology:** ♄ Saturn
- Traditional rulerships: Capricorn, Aquarius
- Keywords: limitation, structure, discipline
- Sources: Greene *Saturn* p.45-67

**Human Design:** Gates 60, 38, 54
- Gate 60 (Limitation) - Root Center
- Sources: IHDS *Rave ABC* p.234
```

**Both:** YAML frontmatter + markdown body?

### 4. Current Library Migration

You have 747 existing interpreted entries. Options:

**Option A: Archive and rebuild**
- Move current Library to `.archive/`
- Start fresh with source-verified synthesis
- Cleanest but most work

**Option B: Mine and migrate**
- Use existing entries as templates/structure
- Add source citations and verification
- Preserve good work, upgrade weak entries

**Option C: Selective migration**
- Keep high-quality entries as-is
- Rewrite entries with poor sourcing
- Gradual improvement over time

---

## Advantages of Hybrid Approach

**Compared to PDF conversion:**
- ✓ No cleanup of page headers/footers/numbers
- ✓ No layout artifact removal
- ✓ Write exactly what Observatory needs (not convert what exists)
- ✓ Cite authoritative sources (PDFs) rather than duplicate them
- ✓ Much less total work (write 100-200 synthesis docs vs convert 200 PDFs)

**Compared to current Library:**
- ✓ Source verification (cite page numbers)
- ✓ Cross-system integration (correspondence tables)
- ✓ Purpose-built for Observatory contextual display
- ✓ Easier to maintain and update

**The Observatory principle preserved:**
- Users still look through original instruments (PDFs)
- Synthesis provides navigation and cross-referencing
- Sources remain authoritative and intact

---

## Next Steps (When Ready)

1. **Decide on architecture questions above**
2. **Create pilot synthesis document** (e.g., Saturn overview)
3. **Create pilot correspondence table** (e.g., Saturn cross-system)
4. **Test in Observatory** — Does this UX work?
5. **Refine based on learnings**
6. **Establish workflow and templates**
7. **Begin systematic synthesis work**

---

## Current Status

**The Athenaeum:** 200 PDFs organized and ready
- Astrology: 8 PDFs (7 clean text, 1 needs OCR)
- Human Design: 75 PDFs (complete IHDS curriculum)
- Personal Mythos: 47 PDFs (Jung CW, von Franz, Campbell, etc.)
- The Tarot: 67 PDFs (13 standalone + 54 Complete Zohar)
- Interdisciplinary: 2 PDFs

**Phase 1 Assessment:** Complete (see `PHASE 1 - Source Text Conversion Assessment.md`)

**Pilot Conversion:** Jung's Studies in Astrology (226 pages) — demonstrates both possibility and limitations of PDF conversion approach.

---

**No rush.** This is a foundational architectural decision. Let it settle, observe from the roof (6th line), then decide when clarity emerges.
