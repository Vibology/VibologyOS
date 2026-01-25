# Prima Materia Citation Remediation Plan

**Created:** 2026-01-23
**Audit Scope:** Cohorts A-D (552 files verified)
**Compliance Rate:** 301/552 (55%) complete
**Remediation Required:** 251/552 (45%) files

---

## Verification Patterns Confirmed

### ✅ Pattern A: Complete (301 files)
**Have BOTH inline footnote citations AND Sources sections**
- Cohort A: Incarnation Crosses (193 files) ✅
- Cohort B: Most Astrology Planets & Signs ✅
- Cohort B: Most Tarot Major Arcana ✅
- Cohort D: Human Design Gates (64 files) ✅

### ⚠️ Pattern B: Missing Inline Citations (129 files)
**Have Sources sections but NO inline footnote citations [^X]**
- Cohort C: 2 Personal Mythos files (Snow White, The Number Seven)
- Cohort D: 67 Window files (all House cards, Archetypes, Portals)
- Cohort D: 56 Minor Arcana Tarot files (all 4 suits)
- **Issue:** Sources are documented at file end, but specific claims lack inline attribution
- **Example:** "Gate 11 mechanics" needs [^1] citation to Ra's Definitive Book

### ⚠️ Pattern C: Missing Sources Section (44 files)
**Have inline footnote citations BUT no Sources section at end**
- Cohort B: 13 Astrology files (12 Houses + Aspects.md)
- Cohort B: 31 HD files (9 Centers + 12 Profiles + 6 Authority + 4 Types)
- **Issue:** Individual claims cited inline, but no consolidated Sources bibliography
- **Example:** 1st House has [^1], [^2], [^3] citations but ends abruptly without "## Sources"

### 🚨 Pattern D: Missing BOTH (78 files - CRITICAL)
**No inline citations AND no Sources sections**
- Cohort B: 4 Astrology files (Aquarius ♒, Pisces ♓, Astrology.md, Transits and Timing.md)
- Cohort C: 74 Personal Mythos files (ALL Jungian, Campbell, Alchemy, Mythology, Fairy Tales)
- Cohort C: 2 Angelology files (The Three Triads, Angelology + HD Integration)
- **Issue:** ZERO scholarly apparatus - pure synthesis without provenance tracking
- **Example:** "The Shadow" file ends with Jung quote but no CW citation, no Sources list

---

## Remediation Strategy

### Phase 1: CRITICAL - Pattern D Files (78 files)
**Priority:** P0 (blocks audit completion)
**Timeline:** 4-5 sessions

#### Batch 1: Astrology Stragglers (4 files)
- Aquarius ♒.md - Add Lilly/Ptolemy citations + Sources
- Pisces ♓.md - Add Lilly/Ptolemy citations + Sources
- Astrology.md - Add overview citations + Sources
- Transits and Timing.md - Add timing citations + Sources

#### Batch 2: Personal Mythos - Jungian Archetypes (12 files)
- Verify CW citations for Shadow, Anima, Animus, Self, Persona, Great Mother, Divine Child, Hero, Wise Old Man, Joker, Shapeshifter, Threshold Guardian
- Add inline [^X] citations to Jung quotes and CW references
- Add Sources section: Jung CW volumes, von Franz, Campbell

#### Batch 3: Personal Mythos - Hero's Journey (12 files)
- Verify Campbell's *Hero with a Thousand Faces* references
- Add inline citations to monomyth stages
- Add Sources: Campbell, Vogler, comparative mythology texts

#### Batch 4: Personal Mythos - Individuation Process (6 files)
- Verify Jung's developmental stages (CW 9i, CW 17)
- Add inline citations to stage definitions
- Add Sources: Jung CW, Edinger, von Franz

#### Batch 5: Personal Mythos - Alchemical Stages (11 files)
- Verify traditional alchemy (Calcination → Rubedo, Nigredo/Albedo/Citrinitas/Rubedo)
- Add inline citations to Jung's *Mysterium Coniunctionis*, Edinger's *Anatomy of the Psyche*
- Add Sources: Jung CW 14, Edinger, Lyndy Abraham

#### Batch 6: Personal Mythos - Fairy Tales (20 files)
- Verify narrative accuracy (Grimm, Perrault, von Franz analyses)
- Add inline citations to von Franz, Bettelheim, Jung interpretations
- Add Sources: Grimm *Complete Fairy Tales*, von Franz *Shadow and Evil*, Bettelheim *Uses of Enchantment*

#### Batch 7: Personal Mythos - World Mythology (12 files)
- Verify canonical mythological narratives (Greek, Norse, Egyptian, etc.)
- Add inline citations to source texts (Hesiod, Edda, Pyramid Texts, etc.)
- Add Sources: Primary texts + scholarly commentaries (Campbell, Eliade, etc.)

#### Batch 8: Personal Mythos Overview + Angelology (3 files)
- Personal Mythos.md - Add framework citations + Sources
- The Three Triads.md - Add Pseudo-Dionysius citations + Sources
- Angelology and Human Design Integration.md - Add cross-system citations + Sources

---

### Phase 2: Pattern C - Add Sources Sections (44 files)
**Priority:** P1 (has citations, needs bibliography)
**Timeline:** 2 sessions

#### Batch 1: Astrology Houses (12 files)
- Add standardized Sources section to all 12 House files:
  ```markdown
  ## Sources

  - Lilly, William. *Christian Astrology*. Book 1 (house classifications and significations)
  - Ptolemy, Claudius. *Tetrabiblos*. Book 3 (house interpretations)
  - Traditional astrology: Angular/Succedent/Cadent classifications, planetary joys
  ```

#### Batch 2: Astrology Aspects (1 file)
- Aspects.md - Add Lilly's table + modern sources

#### Batch 3: Human Design - Centers (9 files)
- Add standardized Sources to all 9 Center files:
  ```markdown
  ## Sources

  - Ra Uru Hu. *The Definitive Book of Human Design: The Science of Differentiation*
  - Jovian Archive. Human Design System foundational materials
  - Biology verification: [Center-specific biological correlations]
  ```

#### Batch 4: Human Design - Profiles (12 files)
- Add standardized Sources to all 12 Profile files (Ra's keynotes)

#### Batch 5: Human Design - Authority (6 files)
- Add standardized Sources to all 6 Authority files

#### Batch 6: Human Design - Types (4 files)
- Add standardized Sources to all 4 Type files

---

### Phase 3: Pattern B - Add Inline Citations (129 files)
**Priority:** P2 (has bibliography, needs attribution)
**Timeline:** 5-6 sessions

#### Batch 1: Window Files (67 files)
- All files HAVE comprehensive Sources sections (Ra, Rudd, Wilhelm/Baynes, Window synthesis)
- **Task:** Add inline [^X] citations to:
  - Ra's Gate mechanics quotes
  - Gene Keys Shadow/Gift/Siddhi references
  - I-Ching hexagram references
  - Window synthesis claims
- **Example fix for Faith.md:**
  ```markdown
  Gate 11 governs ideation and conceptualization[^1] in the Ajna Center...

  [^1]: Ra Uru Hu, *The Definitive Book of Human Design*
  ```

#### Batch 2: Minor Arcana Tarot (56 files)
- All files HAVE Sources sections (Waite, Golden Dawn, Crowley)
- **Task:** Add inline [^X] citations to:
  - Waite's divinatory meanings (upright/reversed)
  - Golden Dawn elemental dignities
  - Qabalistic path attributions
- **Automation:** Create script to insert citations for Waite quotes

#### Batch 3: Personal Mythos Stragglers (2 files)
- Snow White.md - Add inline citations (has Sources already)
- The Number Seven.md - Add inline citations (has Sources already)

#### Batch 4: Window Overviews (4 files)
- 4 duplicates of "Overview.md" in audit report - verify and add citations

---

## Automation Opportunities

### Script 1: Add Standard Sources Section
**Use case:** Pattern C files (44 files with citations but no Sources)
```bash
# System/Scripts/add_sources_section.sh <pillar> <file_pattern>
# Appends standardized Sources markdown based on pillar
```

### Script 2: Insert Inline Citations for Waite Quotes
**Use case:** Minor Arcana (56 files)
```bash
# System/Scripts/cite_waite_quotes.sh
# Regex match Waite divinatory meanings, append [^1] citation
```

### Script 3: Batch Verification Report
**Use case:** After remediation, re-run audit
```bash
# System/Scripts/audit_citations_and_sources.sh
# Already created - re-run after each phase
```

---

## Success Criteria

### Definition of "Complete"
1. ✅ **Inline citations present:** All core factual claims have [^X] footnote references
2. ✅ **Sources section present:** File ends with "## Sources" listing all Prima Materia references
3. ✅ **Citation accuracy:** Footnotes correctly reference the Sources section
4. ✅ **YAML updated:** `source_verified: true` or `synthesis` as appropriate

### Completion Metrics
- **Target:** 552/552 files (100%) compliance
- **Current:** 301/552 files (55%) compliant
- **Remaining:** 251 files requiring remediation

---

## Timeline Estimate

| Phase | Files | Estimated Sessions | Cumulative Compliance |
|-------|-------|-------------------|----------------------|
| **Current** | — | — | 301/552 (55%) |
| Phase 1: Pattern D | 78 | 4-5 sessions | 379/552 (69%) |
| Phase 2: Pattern C | 44 | 2 sessions | 423/552 (77%) |
| Phase 3: Pattern B | 129 | 5-6 sessions | 552/552 (100%) ✅ |
| **TOTAL** | **251** | **11-13 sessions** | **100% audit complete** |

---

## Next Session Actions

1. **Confirm remediation priority with user**
   - Start with Pattern D (CRITICAL - 78 files missing BOTH)?
   - Or tackle Pattern C first (easiest - 44 files, just add Sources sections)?

2. **Choose starting cohort:**
   - Astrology stragglers (4 files, quickest win)
   - Personal Mythos Jungian Archetypes (12 files, highest scholarly rigor)
   - Astrology Houses (12 files, easiest automation)

3. **Create automation scripts if approved:**
   - `add_sources_section.sh` for Pattern C files
   - `cite_waite_quotes.sh` for Minor Arcana batch processing

4. **Update NEXT.md** with new audit findings and remediation plan

---

*"The archive is only as trustworthy as its citations. Every claim must trace back to Prima Materia—or be clearly marked as synthesis."*
