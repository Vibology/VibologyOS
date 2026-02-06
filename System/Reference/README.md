---
tags: [system, reference, documentation, human-design, astrology, synthesis]
date_created: 2026-02-06
---

# Reference Materials Index

This directory contains authoritative source documents that serve as **lookup tools and verification references** for VibologyOS synthesis work. These are not Library content to be expanded, but rather foundational data tables, calculation standards, and canonical mappings.

---

## The HD Synthesis Index

**File:** `The HD Synthesis Index.pdf`
**Source:** Zeno (IHDS founder) — excerpt from *The Course in Human Design*
**Copyright:** © 2007-2010, Zen Human Design
**Pages:** 12
**Status:** Authoritative canonical reference

### What It Is

The **Synthesis Index** is the complete mapping between the tropical zodiac and the 64 Human Design gates/I-Ching hexagrams. It shows:

- **360° wheel structure:** All 64 gates positioned across the zodiac
- **Precise degree correspondence:** Each gate = 5°37'30" of arc, each line = 56'15"
- **Trigram organization:** Gates grouped by 8 I-Ching trigram families (Heaven, Lake, Fire, Thunder, Earth, Mountain, Water, Wind)
- **Complete lookup tables:** All 64 gates × 6 lines with exact astrological degree ranges
- **Gate keywords:** IHDS canonical names/themes for each gate

### Why It Matters

This document is the **Rosetta Stone for Astrology-HD translation**. It enables:

1. **Precise cross-system synthesis:** Convert any planetary position to its exact gate/line activation
2. **Calculation verification:** Cross-check local chart calculation scripts against IHDS canonical data
3. **Transit tracking:** Map slow-moving planetary transits to generational gate activations
4. **Library enhancement:** Add astrological degree spans to gate entries
5. **Mechanical synthesis:** Move from thematic resonance to exact correspondence

### Structure Overview

**Visual Reference (Pages 1, 3):**
- Bodygraph wheel showing 64 gates overlaid on zodiac
- Trigram color-coding and organization

**Lookup Tables (Pages 4-11):**
- **8 trigram groups** (2 double-page spreads each)
- Each page shows 8 gates belonging to that trigram
- Each gate displays all 6 lines with precise degree ranges
- Format: `[Degree]°[Minute]'[Second]"[Sign symbol]` (e.g., `13°15'00"♏︎`)

**Trigram Spans:**
- **Heaven:** 13°15' Scorpio → 28°15' Sagittarius (Gates 1, 43, 14, 34, 9, 5, 26, 11)
- **Lake:** 28°15' Sagittarius → 13°15' Aquarius (Gates 10, 58, 38, 54, 61, 60, 41, 19)
- **Fire:** 13°15' Aquarius → 28°15' Pisces (Gates 13, 49, 30, 55, 37, 63, 22, 36)
- **Thunder:** 28°15' Pisces → 13°15' Taurus (Gates 25, 17, 21, 51, 42, 3, 27, 24)
- **Earth:** 13°15' Taurus → 28°15' Gemini (Gates 2, 23, 8, 20, 16, 35, 45, 12)
- **Mountain:** 28°15' Gemini → 13°15' Leo (Gates 15, 52, 39, 53, 62, 56, 31, 33)
- **Water:** 13°15' Leo → 28°15' Virgo (Gates 7, 4, 29, 59, 40, 64, 47, 6)
- **Wind:** 28°15' Virgo → 13°15' Scorpio (Gates 46, 18, 48, 57, 32, 50, 28, 44)

### How to Use

#### 1. **Converting Planetary Positions to Gates**

**Example:** Sun at 15°30' Scorpio

1. Locate the trigram group containing mid-Scorpio (Heaven: 13°15' Scorpio - 28°15' Sagittarius)
2. Find the gate spanning 15°30' Scorpio
3. Result: **Gate 1, Line 2** (13°15'00"♏︎ - 18°52'30"♏︎)
4. Note Line 2 span: 14°11'15"♏︎ - 15°07'30"♏︎
5. Cross-reference: Gate 1, Line 2 = "Love is Light" (exalted Venus, detriment Mars)

#### 2. **Verifying Chart Calculations**

After running `get_hd_data.py` or `get_astro_data.py`:

1. Extract Sun position from astrology chart (e.g., 20°00' Virgo)
2. Consult Synthesis Index: 20°00' Virgo falls in **Gate 47, Line 3**
3. Check HD chart output: Personality Sun should show Gate 47.3
4. If mismatch occurs, investigate calculation scripts for errors

#### 3. **Enhancing Library Gate Entries**

When expanding/updating gate files in `Library/The Seven Pillars of Understanding/Human Design/Gates/`:

Add to **Core Correspondences** table:

```markdown
| **Astrological Span** | 13°15'00" Scorpio - 18°52'30" Scorpio |
| **I-Ching Trigram** | Heaven (☰) - Pure yang, creative force doubled |
```

Add to **Cross-System Synthesis** section (if applicable):

```markdown
### Astrology: Scorpio Degrees (13°15' - 18°52'30")

Gate 1 occupies the opening degrees of Scorpio, the sign of death/rebirth, transformation, and hidden power. The Creative force (Gate 1) positioned in Scorpio suggests that true creative expression requires **descent into the depths**—the willingness to die to old forms before bringing forth the new.

**Line-by-line astrological progression:**
- Line 1 (13°15' - 14°11'15"): Early Scorpio — Creative force emerging from shadow
- Line 2 (14°11'15" - 15°07'30"): Love as light — Venus exalted, illuminating depths
- [etc.]
```

#### 4. **Cross-System Synthesis Work**

When following `PROTOCOL - Cross-System Synthesis.md` Step 2 (Gather Prima Materia):

**Astrology Section:**
- Note exact planetary degree (e.g., Saturn at 20°45' Virgo)

**Human Design Section:**
- Consult Synthesis Index: Saturn activates Gate 47, Line 3 (Self-Oppression)
- Note planetary exaltation: Line 3 exalted Saturn = "wisdom to recognize self-imposed mental pressure"
- **Convergence point:** Saturn (cosmic teacher through constraint) in Gate 47, Line 3 (mental pressure) with Saturn exaltation = double-reinforced theme of "learning through self-imposed limitation"

#### 5. **Transit Analysis**

For slow-moving planetary transits:

**Example:** Pluto in Aquarius (2024-2043)

1. Pluto enters 13°15' Aquarius (Fire trigram begins)
2. Pluto transits Gates 13, 49, 30, 55, 37, 63, 22, 36 over 20-year period
3. Each gate activation = **generational theme** for cohorts born during that span
4. Synthesis: Pluto (death/rebirth/power) through Fire gates (individuality, revolution, mutation)

### Integration with Existing Protocols

**Referenced by:**
- `PROTOCOL - Chart Data Acquisition.md` — Verification methodology
- `PROTOCOL - Cross-System Synthesis.md` — Prima Materia gathering (Step 2)
- `GUIDE - Synthesis Quick Start.md` — Astrology-HD integration examples

**Supports:**
- Library gate entry enhancement (astrological spans, trigram classification)
- Calculation script verification (Swiss Ephemeris ↔ IHDS canonical correspondence)
- Transit tracking and generational analysis
- Precision synthesis work (exact degree-gate-line mapping)

### Mathematical Foundation

**Key formulas:**

- **360° ÷ 64 gates** = 5°37'30" per gate (5.625°)
- **5°37'30" ÷ 6 lines** = 56'15" per line (0.9375°)
- **Trigram span:** 8 gates = 45° (one-eighth of the wheel)

**Verification:**
- Sun transits one gate in ~5.6 days (360° ÷ 64 ≈ 5.6°/day at 1° per day average)
- Sun transits one line in ~22 hours (5.6 days ÷ 6 lines ≈ 0.93 days)

### Important Notes

**Tropical vs. Sidereal:**
- Human Design uses **tropical zodiac** (same as Western astrology)
- The Synthesis Index degrees are tropical (fixed to seasons, not constellations)
- This differs from Vedic astrology (sidereal) — do not mix systems

**Exactitude:**
- Gate boundaries are **exact to the arc-second** (e.g., 13°15'00")
- This is the IHDS canonical standard
- Minor variations (1-2 arc-minutes) may occur between calculation methods, but IHDS standard is authoritative

**Line Progressions:**
- Lines progress upward (Line 1 = lowest degrees, Line 6 = highest degrees within gate)
- Example: Gate 1, Line 1 starts at 13°15'00"♏︎, Line 6 ends at 18°52'30"♏︎

### Observatory Stance

The Synthesis Index is not interpretation — it is **infrastructure**. Like the telescope mount that holds multiple lenses in precise alignment, this document creates the conditions for accurate observation across Astrology and Human Design simultaneously.

When planetary positions and gate activations converge at the exact degree, the "Third Meaning" emerges not through speculation but through **mechanical correspondence**. The Observatory does not invent this connection; it observes what the mathematics reveal.

---

## Future Reference Materials

As additional authoritative lookup tools are acquired, they will be documented here:

- **Planned:** Hellenistic astrology dignity tables (Ptolemy, Valens, Dorotheus)
- **Planned:** Traditional planetary hours and essential dignities
- **Planned:** Qabalistic correspondence tables (777, Sepher Yetzirah)

---

**Last Updated:** 2026-02-06
**Maintainer:** The Observatory
