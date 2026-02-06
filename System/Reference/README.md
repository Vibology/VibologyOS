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

## Tarot in Human Design

**File:** `Tarot in Human Design.pdf`
**Source:** Eleanor Haspel-Portner, Ph.D — Unified Life Sciences lecture (August 17, 2003)
**Authority:** Ra Uru Hu teaching (1998 transmission from "the Voice")
**Pages:** 18
**Status:** Authoritative canonical correspondence

### What It Is

This document presents the **canonical mapping between the 22 Major Arcana of the Tarot and the Human Design bodygraph**, as revealed to Ra Uru Hu. It shows:

- **Direct gate-to-card correspondences:** Specific Major Arcana keys mapped to exact gates
- **Bodygraph pathway:** Two spiraling paths (counterclockwise and clockwise) through the centers
- **Qabalistic integration:** How the Tarot Keys align with the Tree of Life within the bodygraph
- **Center-specific placements:** All Major Arcana occur in Ajna, Throat, G-Center, and Sacral
- **Archetypal layering:** How Tarot adds symbolic depth to gate mechanics

### Why It Matters

This document **refutes the common assumption that Tarot and Human Design don't map directly**. It provides:

1. **Canonical correspondence:** Ra Uru Hu's authoritative teaching on Tarot-HD integration (not speculative resonance)
2. **Cross-system synthesis:** Enables Tarot symbolism to deepen gate interpretation with archetypal precision
3. **Library correction:** Many gate entries contain Tarot references that should align with this mapping
4. **Client work enhancement:** Tarot-literate practitioners can bridge both systems mechanically
5. **Archetypal verification:** Confirms or corrects thematic resonances with canonical authority

### Complete Tarot-Gate Correspondence Table

| Tarot Key | Gate/Center | Tarot Key | Gate/Center |
|-----------|-------------|-----------|-------------|
| **0 - The Fool** | Ajna & Sacral Centers | **11 - Justice** | Gate 23 |
| **1 - The Magician** | Gate 62 | **12 - The Hanged Man** | Gate 1 |
| **2 - The High Priestess** | Gate 16 | **13 - Death** | Gate 7 |
| **3 - The Empress** | Gate 20 | **14 - Temperance** | Gate 10 |
| **4 - The Emperor** | Gate 31 | **15 - The Devil** | Gate 15 |
| **5 - The Hierophant** | Gate 8 | **16 - The Tower** | Gate 2 |
| **6 - The Lovers** | Gate 33 | **17 - The Star** | Gate 46 |
| **7 - The Chariot** | Gate 45 | **18 - The Moon** | Gate 25 |
| **8 - Strength** | Gate 12 | **19 - The Sun** | Gate 13 |
| **9 - The Hermit** | Gate 35 | **20 - Judgment** | G-Center (all gates) |
| **10 - Wheel of Fortune** | Gate 56 | **21 - The World** | Ajna & Sacral Centers |

### Gate-Specific vs. Center-Level Mappings

**Critical distinction:** Of the 22 Major Arcana, **19 map to specific individual gates** while **3 map to entire centers**:

#### 19 Gate-Specific Correspondences (Keys 1-19)

Keys 1 through 19 (The Magician through The Sun) each correspond to a single, specific gate. These represent archetypal forces manifesting through precise genetic mechanics.

#### 3 Center-Level Correspondences (Keys 0, 20, 21)

Three cards operate at the center level, representing broader structural functions:

| Card | Center(s) | Structural Role |
|------|-----------|-----------------|
| **Key 0 - The Fool** | Ajna & Sacral | Alpha point - Journey's beginning, bridging consciousness (Ajna) and life force (Sacral) |
| **Key 20 - Judgment** | G-Center (all gates) | Central pivot - Identity and direction, the Self witnessing the entire journey |
| **Key 21 - The World** | Ajna & Sacral | Omega point - Journey's completion, integration of consciousness and manifestation |

**Why this matters:**
- **Gates** = specific mechanics (19 cards provide archetypal depth to individual gate functions)
- **Centers** = energetic functions (3 cards describe broader consciousness/identity/life-force operations)
- **The Fool/World axis** (Keys 0 & 21) spans the **consciousness ↔ manifestation bridge** (Ajna-Sacral)
- **Judgment** (Key 20) occupies the **identity center** (G-Center), the pivot point of self-awareness

When enhancing Library entries:
- **Gate files** (64 gates) → Only 19 have canonical Tarot correspondences
- **Center files** (Ajna, G-Center, Sacral) → Document the 3 center-level correspondences
- **Tarot Major Arcana files** → 19 link to specific gates, 3 link to entire centers

### Structure Overview

**Two Spiral Paths:**

1. **Counterclockwise Path (Ajna → G-Center → Sacral):**
   - Begins: Gate 17 → Gate 62 (Throat)
   - Continues through: Gates 16, 20, 31, 8, 33, 45, 12, 35, 56, 23, 8, 1, 7, 10, 15, 2, 46, 25, 13
   - Ends: G-Center (Key 20) → Gate 15 → Sacral (Gate 5)
   - **Represents:** Inner unfolding process of consciousness development

2. **Clockwise Path (Sacral → G-Center → Throat → Ajna):**
   - Begins: Gate 5 → Gate 15 (G-Center)
   - Continues through: Gates 2, 46, 25, 13, 1, 7, 10, 15, 2, G-Center (Key 20), 1, 8, 31, 20, 16, 62, 23, 56, 35, 12, 45, 33, 62
   - Ends: Gate 17 (Ajna)
   - **Represents:** Consciousness transforming into human thought and cognition

**Double Helix Structure:**
- The two paths trace a DNA-like spiral, showing the relationship between inner process and outer manifestation
- Connects to the Qabalistic Tree of Life and Cube of Space
- Links the Mammalian Matrix (sleep/dream states) with the Human Matrix (waking consciousness)

### How to Use

#### 1. **Correcting Gate Entry Tarot References**

When reviewing gate entries in `Library/The Seven Pillars of Understanding/Human Design/Gates/`:

**Check existing Tarot references against canonical mapping:**

Example corrections needed:
- Gate 51 currently references "The Tower" → **Incorrect** (Tower = Gate 2)
- Gate 58 currently references "Strength" → **Incorrect** (Strength = Gate 12)
- Gate 60 references "Temperance" → **Close but imprecise** (Temperance = Gate 10)

**Add canonical correspondence to Cross-System Synthesis section:**

```markdown
### Tarot: The Magician (Gate 62)

According to Ra Uru Hu's teaching documented by Eleanor Haspel-Portner (2003), Gate 62 corresponds to **The Magician** (Atu I / Key 1) in the Major Arcana. This is not thematic resonance but canonical correspondence.

**The Magician's essence:** "As above, so below" — translation between realms, naming, manifesting through word. The Magician takes archetypal forces and gives them form through language and will.

**Gate 62's mechanics:** The voice of detail, naming, organizing facts — "I think." Preponderance of the Small through precise articulation.

**Convergence:** Both The Magician and Gate 62 share the core function of **translation and manifestation through precise naming**. The Magician translates spiritual force into material form; Gate 62 translates abstract patterns into named facts. Mercury (communication, detail) governs both.
```

#### 2. **Gate Entry Enhancement Template**

For gates WITH canonical Tarot correspondence, add this section after I-Ching Hexagram Analysis:

```markdown
### Tarot: [Card Name] (Canonical Correspondence)

**Ra Uru Hu Teaching:** Gate [X] corresponds to **[Card Name]** (Atu [Roman] / Key [Number]) according to the 1998 transmission documented by Eleanor Haspel-Portner.

**Archetypal Essence:** [Brief card meaning from Qabalistic/BOTA tradition]

**Mechanical Convergence:** [How the card's symbolism aligns with gate mechanics]

**Cross-Reference:** See `System/Reference/Tarot in Human Design.pdf` pages [X-X] for pathway context.
```

For gates WITHOUT canonical Tarot correspondence, continue using thematic resonance but clarify:

```markdown
### Tarot: [Card Name] (Thematic Resonance)

While Gate [X] does not have a canonical Tarot correspondence in Ra Uru Hu's teaching, it resonates thematically with **[Card Name]**...

**Note:** This is thematic resonance, not mechanical correspondence. See `System/Reference/Tarot in Human Design.pdf` for canonical mappings.
```

#### 3. **Client Chart Synthesis**

When synthesizing a chart with Tarot correspondences:

1. **Identify activated gates** from HD chart
2. **Map to Tarot Keys** using canonical table above
3. **Layer archetypal meaning** from Tarot onto mechanical gate function
4. **Note special activations:**
   - G-Center gates = Judgment (Key 20) influence
   - Ajna/Sacral = Fool (Key 0) and World (Key 21) bridging consciousness and manifestation

**Example:**

Client has **Gate 62 (Personality Sun)**:
- Mechanical: Voice of detail, precision, naming facts
- Tarot (Canonical): The Magician — manifestation through word, "As above, so below"
- Synthesis: "Your Personality Sun in Gate 62 makes you a natural Magician with language — you manifest understanding by naming it precisely. The Magician's gift of translation between realms expresses through your capacity to articulate details that reveal patterns."

#### 4. **Cross-System Synthesis Protocol Integration**

When following `PROTOCOL - Cross-System Synthesis.md`:

**Step 2 (Gather Prima Materia) — Add Tarot Layer:**

**Tarot Section:**
- Check if any activated gates have canonical Tarot correspondences
- Note the archetypal theme from the corresponding Major Arcana
- Research Qabalistic associations (Hebrew letter, path on Tree of Life, astrological attribution)
- **Convergence point:** How does the Tarot archetype deepen understanding of the gate's mechanical function?

**Example Synthesis:**
- **Gate 16 activated** (Skills, Enthusiasm)
- **Tarot:** The High Priestess (Key 2)
- **Qabalah:** Gimel (ג), Path between Kether and Tiphareth, Moon
- **Convergence:** The High Priestess's lunar receptivity and skill in navigating hidden knowledge aligns with Gate 16's capacity to master skills through depth and repetition. The unconscious mastery (High Priestess) manifests through practiced enthusiasm (Gate 16).

### Integration with Existing Protocols

**Referenced by:**
- `PROTOCOL - Cross-System Synthesis.md` — Prima Materia gathering (Tarot as additional layer)
- `GUIDE - Synthesis Quick Start.md` — Archetypal integration examples

**Supports:**
- Library gate entry enhancement (canonical Tarot correspondences)
- Client chart readings (Tarot-HD bridge for archetypal depth)
- Teaching synthesis (demonstrating multi-system convergence with authority)
- Correcting speculative Tarot references with canonical mappings

**Requires correction in:**
- Multiple gate entries currently contain incorrect or speculative Tarot references
- Future systematic review needed to align all gate Tarot sections with canonical mapping

### Important Notes

**Canonical vs. Resonance:**
- This is **Ra Uru Hu's direct teaching**, not Eleanor Haspel-Portner's interpretation
- The mapping was revealed to Ra in 1998 by "the Voice" (same source as HD system)
- Any Tarot reference in gate entries should specify: **canonical correspondence** (if in this table) or **thematic resonance** (if not)

**Pathway Context Matters:**
- Cards don't exist in isolation — their position on the counterclockwise or clockwise spiral adds meaning
- The G-Center acts as a pivot point (Judgment/Key 20)
- The Fool (Key 0) and World (Key 21) bridge Ajna and Sacral, showing consciousness-manifestation axis

**Limitations:**
- Only the 22 Major Arcana are mapped (Minor Arcana are not addressed)
- Only 19 of the 22 Major Arcana map to specific individual gates (Keys 1-19)
- The remaining 3 Major Arcana map to entire centers: The Fool & World (Ajna/Sacral), Judgment (G-Center)
- 45 of 64 gates have no canonical Tarot correspondence (only gates in Ajna, Throat, G-Center, Sacral have correspondences)
- The document presents one valid layout but acknowledges other arrangements are possible

**BOTA Integration:**
- Eleanor Haspel-Portner studied Builders of the Adytum (BOTA) Tarot system
- The correspondences use Rider-Waite deck imagery (with BOTA permission noted)
- Qabalistic attributions follow Paul Foster Case tradition

### Observatory Stance

The Tarot-HD correspondence is not interpretation — it is **revealed structure**. Like discovering that the bodygraph and the Qabalistic Tree of Life share mathematical foundations, this mapping was transmitted rather than deduced.

The Observatory's role is to **observe the correspondence without forcing meaning**. When a gate's mechanics and its canonical Tarot card converge in symbolism, the "Third Meaning" emerges from the overlap. When they diverge, that tension is also data — the archetype and the mechanism offer different lenses on the same human experience.

This is not about making Tarot "fit" Human Design or vice versa. It is about recognizing that both systems describe the same territory from different observational positions. The correspondence reveals **where they're pointing at the same landmarks**.

---

## Future Reference Materials

As additional authoritative lookup tools are acquired, they will be documented here:

- **Planned:** Hellenistic astrology dignity tables (Ptolemy, Valens, Dorotheus)
- **Planned:** Traditional planetary hours and essential dignities
- **Planned:** Qabalistic correspondence tables (777, Sepher Yetzirah)

---

**Last Updated:** 2026-02-06
**Maintainer:** The Observatory
