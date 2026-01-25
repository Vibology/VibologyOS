---
tags: [system, template, manifest, astrology]
system: Astrology
date_created: 2026-01-25
status: canonical
---

# Astrology Section Manifest

This manifest defines approved section names for Astrology Library entries.

---

## Pillar Voice

**Character:** Poetic-technical, scholarly yet evocative
**Influences:** Hellenistic tradition, Lilly, Ptolemy, modern psychological astrology
**Tone:** Balance of technical precision and mythic imagination; dignities with depth

---

## Required YAML Fields

```yaml
tags: [astrology, {category}, {specific-item}]
system: Astrology
date_created: YYYY-MM-DD

# For Planets
glyph: [Unicode glyph]
alchemical: [Alchemical correspondence]

# For Signs
element: [Fire/Earth/Air/Water]
modality: [Cardinal/Fixed/Mutable]
ruler: [Ruling planet]

# For Houses
house_number: [1-12]
natural_sign: [Associated sign]
angular_type: [Angular/Succedent/Cadent]

# Verification
verified: true
verification_date: YYYY-MM-DD
verification_source: ""
grimoire_source: ""
verification_notes: ""
```

---

## Approved Section Names

### OPENING Slot
**Primary:** `## Archetypal Essence`
**Alternates:**
- `## Essential Nature`
- `## Core Principle`

### DATA Slot
**Primary:** `## Dignities & Rulerships`
**Alternates:**
- `## Essential Dignities`
- `## Core Correspondences`

**Subsections:**
- `### Domicile & Exaltation`
- `### Detriment & Fall`
- `### Triplicity Rulers`
- `### Decans & Bounds`
- `### Alchemical Correspondences`

**Standard Dignities Table:**
```markdown
| Dignity | Sign(s) | Degree (if applicable) |
|---------|---------|------------------------|
| Domicile | | |
| Exaltation | | |
| Detriment | | |
| Fall | | |
```

### DEPTH Slot
**Primary:** `## Psychological Depth`
**Alternates:**
- `## Mythological Resonance`
- `## Jungian Dimensions`

**Subsections:**
- `### Mythic Origins`
- `### Archetypal Function`
- `### Developmental Stages`

### SHADOW Slot
**Primary:** `## Shadow Expression`
**Alternates:**
- `## Afflicted Manifestation`
- `## Debility Patterns`

### PRACTICE Slot
**Primary:** `## Interpretation Guide`
**Alternates:**
- `## Delineation Notes`
- `## House-by-House Analysis`

**Subsections:**
- `### By House Position`
- `### By Aspect`
- `### Timing Considerations`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Within Astrology`
- `### Tarot Correspondences`
- `### Human Design Gates`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Classical:** Author, work — (Ptolemy, *Tetrabiblos*, Book I)
- **Lilly:** Page reference — (Lilly, *Christian Astrology*, p. 67)
- **Modern:** Standard academic — (Arroyo, 1975, p. 43)
- **Footnotes:** Use `[^1]` format for extended citations

---

## Special Formatting

### Glyphs in Titles
Include Unicode glyph with planet/sign name:
```markdown
# The Sun ☉
# Aries ♈
```

### Dignities Tables
Always use table format for dignity data—never prose.

### Degree Notations
Use standard format: `19° Aries` not `19 degrees Aries`

---

## Entry Types

### Planet Entry
Full template. Emphasize dignities, mythology, psychological function.

### Sign Entry
Full template. Include element/modality, developmental arc, shadow.

### House Entry
May abbreviate SHADOW. Focus on life domain and interpretation.

### Aspect Entry
Focus on DATA (orbs, nature) and INTERPRETATION. May omit SHADOW.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
