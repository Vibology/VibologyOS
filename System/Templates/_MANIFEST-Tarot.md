---
tags: [system, template, manifest, tarot]
system: The Tarot
date_created: 2026-01-25
status: canonical
---

# Tarot Section Manifest

This manifest defines approved section names for Tarot Library entries.

---

## Pillar Voice

**Character:** Esoteric-instructional, Qabalistic precision
**Influences:** Golden Dawn, Crowley (*Book of Thoth*), Wang, Waite, Hebrew letter mysticism
**Tone:** Technical Qabalistic framework with divinatory accessibility; honor both traditions

---

## Required YAML Fields

```yaml
tags: [tarot, {category}, {specific-card}]
system: The Tarot
date_created: YYYY-MM-DD

# For Major Arcana
number: [0-21]
hebrew_letter: [Letter (Character)]
qabalistic_path: [Path number and Sephiroth]
astrological: [Planet/Sign/Element]

# For Minor Arcana
suit: [Wands/Cups/Swords/Pentacles]
number: [Ace-10 or Court]
decan: [If applicable]
sephirah: [Tree of Life position]

# For Court Cards
rank: [Page/Knight/Queen/King]
element: [Suit element]
sub_element: [Rank element]

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
**Primary:** `## Qabalistic Position`
**Alternates:**
- `## Archetypal Essence`
- `## Core Meaning`

**Format for Major Arcana:**
```markdown
## Qabalistic Position

**Path:** [Number] — [Sephirah] to [Sephirah]
**Hebrew Letter:** [Letter] ([Character]) — "[Meaning]"
**Astrological:** [Attribution]
```

### DATA Slot
**Primary:** `## Traditional Symbolism`
**Alternates:**
- `## Correspondences`
- `## Symbolic Structure`

**Subsections:**
- `### Hebrew Letter Mysteries`
- `### Path Correspondences`
- `### Visual Symbolism` (RWS/Thoth imagery analysis)
- `### Elemental Attribution`

**Standard Correspondence Table:**
```markdown
| Attribute | Correspondence |
|-----------|----------------|
| Number | |
| Hebrew Letter | |
| Path | |
| Astrological | |
| Element | |
| Color (King Scale) | |
| Color (Queen Scale) | |
```

### DEPTH Slot
**Primary:** `## Esoteric Interpretation`
**Alternates:**
- `## Mystical Significance`
- `## Path Working`

**Subsections:**
- `### Golden Dawn Teaching`
- `### Crowley's Commentary`
- `### Jungian Parallels`
- `### Alchemical Process`

### SHADOW Slot
**Primary:** `## Reversed Meaning`
**Alternates:**
- `## Shadow Aspect`
- `## Ill-Dignified`

**Subsections:**
- `### Traditional Reversed`
- `### Psychological Shadow`
- `### Blocked Energy`

### PRACTICE Slot
**Primary:** `## Divination Use`
**Alternates:**
- `## Reading Application`
- `## Practical Mysticism`

**Subsections:**
- `### In Readings`
- `### Positional Variations`
- `### Meditation Use`
- `### Path Working Guide`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Within Tarot`
- `### Qabalistic Integration`
- `### Astrological Correspondence`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Crowley:** Work reference — (Crowley, *Book of Thoth*, p. XX)
- **Wang:** Page reference — (Wang, *Qabalistic Tarot*, p. XX)
- **Waite:** Work reference — (Waite, *Pictorial Key*, p. XX)
- **Golden Dawn:** Tradition attribution — (Golden Dawn, *Book T*)
- **Footnotes:** Use `[^1]` for extended scholarly notes

---

## Special Formatting

### Card Titles
Include number for Major Arcana:
```markdown
# 0 - The Fool
# XIII - Death
```

### Hebrew Letter Format
```markdown
**Aleph (א)** — "Ox" — Breath, Air, Spirit
```

### Path Notation
```markdown
**Path 11:** Kether → Chokmah (Connecting Crown to Wisdom)
```

### Upright/Reversed Format
```markdown
### Upright
[Meaning when well-dignified]

### Reversed
[Meaning when ill-dignified]
```

### Thoth vs. RWS Distinctions
When traditions differ:
```markdown
> *Note: The Thoth deck names this card "Lust" rather than "Strength" and assigns it to Leo rather than the Golden Dawn's attribution to Libra.*
```

---

## Entry Types

### Major Arcana Entry
Full template. Extensive Qabalistic analysis. Hebrew letter mysticism. Complete PATH working.

### Minor Arcana Entry
May abbreviate PATH section. Emphasize decan correspondence and practical divination.

### Court Card Entry
Focus on elemental combinations. Character/personality emphasis. May abbreviate DEPTH.

### Suit Overview
Survey format. Cross-reference heavy. Elemental and Qabalistic world correspondence.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
