---
tags: [system, guide, synthesis, quick-reference]
date_created: 2026-01-19
---

# Synthesis Quick Start Guide

A concise entry point for creating synthesis pieces. This guide answers "which template when?" and provides quality standards at a glance.

---

## 1. Decision Framework: Which Template When?

| **Type of Work** | **Template** | **Location** | **When to Use** |
|------------------|--------------|--------------|-----------------|
| Client reading | `_TEMPLATE - Client Reading.md` | `System/Templates/` | Paid client synthesis with delivery expectations |
| Universal teaching | `_TEMPLATE - Cross-System Synthesis.md` | `Synthesis/General/` | Archetypal patterns anyone could learn from |
| Personal synthesis | Cross-System template | `Biographical/` (separate repo) | Your own integration work |
| Data verification | `_TEMPLATE - Synthesis Verification Checklist.md` | `System/Templates/` | Before any synthesis involving chart data |

**Decision tree:**
1. Is this for a paying client? → **Client Reading template**
2. Is this universal/teaching-focused? → **Cross-System template** in `Synthesis/General/`
3. Is this personal work? → **Cross-System template** in your Biographical folder
4. Does it involve natal/transit data? → Start with **Verification Checklist**

---

## 2. When Exploratory Work Becomes Synthesis

Informal conversation, notes, or journal threads should graduate to formal synthesis when **all five criteria** are met:

- [ ] **Multi-system integration** - Involves 2+ esoteric systems in meaningful dialogue (not just passing mentions)
- [ ] **Practical application** - Provides decision framework, timing guidance, or actionable insight
- [ ] **Third Meaning present** - Contains emergent insight neither system reveals alone
- [ ] **Reference value** - Worth documenting for future consultation or teaching
- [ ] **Substantive content** - 1500+ words of core insight have emerged in conversation

**If all five are checked:** Create formal synthesis piece
**If fewer than five:** Keep in journal/notes until the work matures

---

## 3. Quality Standards Quick Reference

### Content Depth
| Metric | Minimum | Comprehensive |
|--------|---------|---------------|
| Word count | 1,500 words | 6,000+ words |
| Systems integrated | 2 | 4+ |
| [[Wikilinks]] | 5 | 15+ |

### Required Elements
Every synthesis piece must include:
1. **The Question** - What is being asked, why it matters, what's at stake
2. **System Integration** - Multiple systems held in dialogue, convergence and divergence explored
3. **The Third Meaning** - Emergent insight that no single system could reveal alone
4. **Practical Wisdom** - Decision framework, practices, timing guidance

### Voice & Format
**Final synthesis pieces must be written in mythopoetic narrative format:**
- Flowing prose, not tables or bullet-point lists
- Factual data woven naturally into the narrative (e.g., "The Sun at 15° Virgo..." not a planetary position table)
- Scholarly yet evocative—precise in terminology, reaching toward the numinous
- Section headings based on content themes (e.g., "The Guardians at the Gate") not template labels (e.g., "System 1 Analysis")
- The synthesis should read as a unified journey, not a disconnected data report

**Note:** Working notes and data gathering may use tables and clinical formats. The mythopoetic standard applies to final, committed synthesis pieces.

### YAML Frontmatter (Required)
```yaml
tags: [synthesis, cross-system, {system-tags}]
systems_integrated: [List of systems]
entity_id: {Initials / "Universal"}
date_created: YYYY-MM-DD
scope: {Personal / Client / Universal Teaching}
```

---

## 4. Naming Conventions

### Format
`{Date or Archetype} - {Core Question or Pattern}.md`

### Expanded Examples

**Time-bound (use date prefix):**
- `2026-01-19 - Saturn Return at 29 (Astrology + HD + Tarot).md`
- `2026-03-15 - Pluto Square Moon Transit Integration.md`
- `2026-07-01 - Career Crossroads Decision Analysis.md`

**Timeless/archetypal (use descriptive name):**
- `The Tower Archetype - Tarot + Qabalah + Jungian Integration.md`
- `Projector Burnout - HD Conditioning + Astrological Signatures.md`
- `The Wound of Worth - Open Heart Center + Chiron Analysis.md`

**Themed series (use consistent prefix):**
- `Elements Series 01 - Fire Across Systems.md`
- `Saturn Cycles 01 - First Saturn Return (Age 29).md`
- `Gate Deep Dives - Gate 51 Shock and Tower Correspondence.md`

### Rules
- ISO date format (YYYY-MM-DD) when time-bound
- Include systems in subtitle when not obvious from title
- Keep titles under 80 characters
- Use hyphens for readability, not underscores

---

## 5. Folder Structure

```
Synthesis/
├── General/
│   ├── _TEMPLATE - Cross-System Synthesis.md
│   └── [Universal teaching pieces]
└── Themed Collections/
    └── [Multi-part series, systematic explorations]
```

**Placement rules:**
- **General/** - One-off universal insights, teaching demonstrations
- **Themed Collections/** - Multi-part series with shared naming conventions

**NOT in Synthesis/:**
- Personal work → `Biographical/` (separate repo)
- Client work → Client folder (separate repo)
- Library entries → `Library/{System}/`

---

## 6. Quick Checklist Before Committing

Before writing to disk:

**Data integrity:**
- [ ] Chart data calculated (not inferred) via scripts
- [ ] Verification checklist completed for client work

**Content complete:**
- [ ] Prima Materia factual and verifiable
- [ ] Convergence AND divergence points identified
- [ ] Third Meaning explicitly articulated
- [ ] Practical application specific (not vague platitudes)

**Structure correct:**
- [ ] YAML frontmatter complete
- [ ] Minimum 5 [[wikilinks]]
- [ ] Scribe/Weaver voice separation maintained

**Location correct:**
- [ ] Universal → `Synthesis/General/`
- [ ] Series → `Synthesis/Themed Collections/`
- [ ] Personal/client → Appropriate separate repo

---

## 7. Links to Full Documentation

**Complete methodology:**
→ `System/PROTOCOL - Cross-System Synthesis.md` (590 lines, 7-step process, quality rubric)

**Client workflow:**
→ `System/PROTOCOL - Client Work.md` (intake through delivery)

**Content standards:**
→ `System/RUBRIC - Library Content Standard.md` (tier definitions, system-specific appendices)

**Chart data acquisition:**
→ `System/PROTOCOL - Chart Data Acquisition.md` (mandatory pre-synthesis data verification)

**Templates:**
→ `System/Templates/_TEMPLATE - Client Reading.md`
→ `System/Templates/_TEMPLATE - Synthesis Verification Checklist.md`
→ `Synthesis/General/_TEMPLATE - Cross-System Synthesis.md`

---

*"The whole is greater than the sum of its parts—but only when held with intention."*
