---
tags: [system, plan, human-design, incarnation-cross, library-expansion]
date_created: 2026-01-19
status: Proposed
priority: Medium
estimated_scope: Large (192 entries)
---

# PLAN: Incarnation Cross Library Expansion

## Overview

The Library currently lacks coverage of Incarnation Crosses—a critical component of Human Design that describes the specific life purpose encoded in the Sun and Earth positions at both personality (birth) and design (88 days pre-birth) moments.

This plan outlines the scope, structure, and phased approach for adding comprehensive Incarnation Cross content to the Human Design pillar.

---

## The 192 Incarnation Crosses

Human Design contains **192 distinct Incarnation Crosses**, organized into three categories:

### Right Angle Crosses (64)
- **Orientation:** Personal destiny
- **Theme:** Individual life purpose; the journey is personal
- **Structure:** Four gates forming a cross pattern, with the Personality Sun gate naming the cross

### Left Angle Crosses (64)
- **Orientation:** Transpersonal destiny
- **Theme:** Purpose fulfilled through others; karma with others
- **Structure:** Same gate structure as corresponding Right Angle, but experienced through relationship

### Juxtaposition Crosses (64)
- **Orientation:** Fixed destiny
- **Theme:** Specific, narrow life purpose; geometry that cannot be altered
- **Structure:** Unique fixed fate pattern

**Total: 192 entries needed**

---

## Proposed Library Structure

```
Library/Human Design/
├── Incarnation Crosses/
│   ├── Incarnation Crosses Overview.md
│   ├── Right Angle/
│   │   ├── RAC of the Sphinx.md
│   │   ├── RAC of Eden.md
│   │   ├── RAC of the Vessel of Love.md
│   │   └── ... (64 total)
│   ├── Left Angle/
│   │   ├── LAC of the Sphinx.md
│   │   ├── LAC of Eden.md
│   │   ├── LAC of the Vessel of Love.md
│   │   └── ... (64 total)
│   └── Juxtaposition/
│       ├── JC of Alertness.md
│       ├── JC of Ambition.md
│       └── ... (64 total)
```

---

## Entry Template (Proposed)

```markdown
---
tags: [human-design, incarnation-cross, {right-angle|left-angle|juxtaposition}, gate-{sun-gate}]
cross_type: {Right Angle | Left Angle | Juxtaposition}
gates: [{sun}, {earth}, {design-sun}, {design-earth}]
quarter: {Initiation | Civilization | Duality | Mutation}
theme: {brief thematic description}
date_created: YYYY-MM-DD
tier: {1|2|3}
---

# {Cross Name}

## The Four Gates

### Personality Sun: Gate {N} ({Name})
{Gate description in context of this cross - which center, what it contributes}

### Personality Earth: Gate {N} ({Name})
{Gate description - the grounding/stabilizing element}

### Design Sun: Gate {N} ({Name})
{Gate description - the unconscious drive}

### Design Earth: Gate {N} ({Name})
{Gate description - the unconscious foundation}

## The Cross Theme

{Narrative description of the life purpose this cross encodes - what is the person here to do/be/experience? How do the four gates interact to create a unified purpose?}

## The Quarter Context

{This cross belongs to the Quarter of {X}, which governs {theme}. How does this cross express that quarterly energy?}

## Shadow Expression

{How does this cross manifest when lived unconsciously or through the not-self? What patterns emerge when the purpose is resisted or distorted?}

## Highest Expression

{How does this cross manifest when lived consciously, in alignment with Strategy and Authority? What does fulfillment look like?}

## Cross Variations by Line

{Brief notes on how the six lines of the Personality Sun gate modify the cross expression}

- **Line 1:** {Investigator expression}
- **Line 2:** {Hermit expression}
- **Line 3:** {Martyr expression}
- **Line 4:** {Opportunist expression}
- **Line 5:** {Heretic expression}
- **Line 6:** {Role Model expression}

## Internal Links

- [[Gate {N} - {Name}]]
- [[Gate {N} - {Name}]]
- [[Gate {N} - {Name}]]
- [[Gate {N} - {Name}]]
- [[{Related Profile}]]
- [[{Related Channel if applicable}]]

---

*"{Closing quote or thematic summary}"*
```

---

## Phased Implementation

### Phase 1: Foundation (Priority)
**Scope:** 12 entries
**Focus:** The most commonly encountered crosses + structural foundation

1. Create `Incarnation Crosses Overview.md` explaining the system
2. Create folder structure
3. Write entries for the 12 crosses associated with the four Quarters' "gateway" gates:
   - Quarter of Initiation: Gates 13, 25, 17 (RAC versions)
   - Quarter of Civilization: Gates 2, 7, 15 (RAC versions)
   - Quarter of Duality: Gates 10, 46, 6 (RAC versions)
   - Quarter of Mutation: Gates 53, 42, 36 (RAC versions)

**Deliverable:** Foundation understanding + 13 files

### Phase 2: Right Angle Crosses (Core)
**Scope:** 52 additional entries (completing all 64 RAC)
**Rationale:** Right Angle crosses are the most common (~70% of population)

**Deliverable:** All 64 Right Angle Crosses complete

### Phase 3: Left Angle Crosses
**Scope:** 64 entries
**Rationale:** Left Angle crosses require understanding Right Angle first (they share gates but differ in orientation)

**Deliverable:** All 64 Left Angle Crosses complete

### Phase 4: Juxtaposition Crosses
**Scope:** 64 entries
**Rationale:** Juxtaposition is the rarest (~2% of population); lower priority

**Deliverable:** All 64 Juxtaposition Crosses complete

---

## Quality Standards

Per `RUBRIC - Library Content Standard.md`:

**Tier 1 (Minimum Viable):**
- 500+ words
- All four gates identified and briefly described
- Cross theme articulated
- 4+ wikilinks

**Tier 2 (Standard):**
- 800+ words
- Quarter context included
- Shadow and highest expression described
- Line variations noted
- 6+ wikilinks

**Tier 3 (Comprehensive):**
- 1200+ words
- Full narrative integration
- Cross-system synthesis (astrological correlations, archetypal themes)
- Practical guidance for living the cross
- 10+ wikilinks

**Initial target:** Tier 2 for Phase 1, Tier 1 for Phases 2-4 (with upgrade path)

---

## Dependencies

1. **Gate entries must exist first** — Each cross entry will link to four gate entries. Current status: All 64 gates exist at Tier 3. ✅

2. **Quarter system documentation** — Need to document the Four Quarters (Initiation, Civilization, Duality, Mutation) either as separate entries or in the Overview.

3. **API gate data** — The humandesign_api should ideally return gate positions for accurate cross calculation. Currently returning cross name but not gate data (investigation pending).

---

## Estimated Effort

| Phase | Entries | Est. Words | Est. Time |
|-------|---------|------------|-----------|
| Phase 1 | 13 | 10,000-15,000 | 2-3 sessions |
| Phase 2 | 52 | 26,000-40,000 | 8-12 sessions |
| Phase 3 | 64 | 32,000-50,000 | 10-15 sessions |
| Phase 4 | 64 | 32,000-50,000 | 10-15 sessions |
| **Total** | **193** | **100,000-155,000** | **30-45 sessions** |

This is a significant expansion (~40% increase to Human Design pillar by entry count).

---

## Alternative Approaches

### Option A: Full Build (This Plan)
Build all 192 crosses systematically.
- **Pro:** Complete coverage, authoritative reference
- **Con:** Massive time investment

### Option B: On-Demand Build
Create entries only when needed for client work or personal synthesis.
- **Pro:** Efficient use of time, entries have immediate practical value
- **Con:** Incomplete coverage, no systematic progression

### Option C: Tiered Hybrid
- Phase 1 (systematic): Build overview + all Right Angle crosses (65 entries)
- Phases 2-3 (on-demand): Left Angle and Juxtaposition as needed
- **Pro:** Covers ~70% of population systematically, rest on-demand
- **Con:** Still significant investment for Phase 1

**Recommendation:** Option C (Tiered Hybrid)

---

## Next Steps

1. [ ] User decision on approach (A, B, or C)
2. [ ] Resolve humandesign_api gate data issue (for accurate calculations)
3. [ ] Create `Incarnation Crosses Overview.md` (regardless of approach)
4. [ ] Begin Phase 1 if approved

---

## References

- Jovian Archive materials on Incarnation Crosses
- Ra Uru Hu lectures on life purpose
- Existing Gate entries in Library (for linking)
- RUBRIC - Library Content Standard.md (quality tiers)

---

*"The Incarnation Cross is the costume the soul wears for this particular performance."*
