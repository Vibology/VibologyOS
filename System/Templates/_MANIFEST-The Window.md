---
tags: [system, template, manifest, the-window]
system: The Window
date_created: 2026-01-25
status: canonical
---

# The Window Section Manifest

This manifest defines approved section names for The Window Library entries.

---

## Pillar Voice

**Character:** Contemporary-accessible, synthesis-oriented
**Influences:** 1980s cultural encoding, Human Design mechanics, I-Ching, Gene Keys
**Tone:** Modern oracle language; bridges ancient wisdom to contemporary archetypes; the most "accessible" pillar

---

## Required YAML Fields

```yaml
tags: [the-window, {tier}, {category}, gate-{number}]
system: The Window
date_created: YYYY-MM-DD

# Card Fields
tier: [Archetype/Portal/House]
gate: [1-64]
hexagram: [I-Ching name]
gene_keys: [Shadow → Gift → Siddhi]

# For House Cards
house: [House number if applicable]

# Status
status: [Complete/Draft/Stub]

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
**Primary:** `## Core Domain`
**Alternates:**
- `## Essential Meaning`
- `## Card Overview`

**Format:** Brief, accessible introduction:
```markdown
## Core Domain

*[One-line essence in italics]*

[2-3 paragraph introduction establishing the card's territory]
```

### DATA Slot
**Primary:** `## Correspondences`
**Alternates:**
- `## System Integration`
- `## Structural Framework`

**Subsections:**
- `### The Gate (Human Design)`
- `### The Hexagram (I-Ching)`
- `### The Gene Keys`
- `### The Three Parallel Domains`

**Standard Correspondence Table:**
```markdown
| System | Correspondence |
|--------|----------------|
| Gate | [Number]: [Keynote] |
| Center | [HD Center] |
| Hexagram | [Number]: [Name] |
| Gene Keys | [Shadow] → [Gift] → [Siddhi] |
| Circuit | [Circuit name] |
```

### DEPTH Slot
**Primary:** `## Synthesis Notes`
**Alternates:**
- `## Deeper Patterns`
- `## Integrated Meaning`

**Subsections:**
- `### Cultural Encoding`
- `### Archetypal Resonance`
- `### The Transformation Arc`

**Vibology Synthesis Format:**
```markdown
> *Vibology Synthesis: [Original integration insight]*
```

### SHADOW Slot
**Primary:** `## Shadow Aspect`
**Alternates:**
- `## When Contracted`
- `## The Not-Self Expression`

### PRACTICE Slot
**Primary:** `## Oracle Reading`
**Alternates:**
- `## Divination Use`
- `## When This Card Appears`

**Subsections:**
- `### Core Message`
- `### Shadow Warning`
- `### Gift Invitation`
- `### Siddhi Vision`

**Reading Format:**
```markdown
### When This Card Appears

**Core Message:** [Primary divination meaning]

**Shadow Warning:** [What to watch for]

**Gift Invitation:** [What becomes possible]

**Siddhi Vision:** [Transcendent possibility]
```

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Related Window Cards`
- `### Human Design Gates`
- `### Tarot Correspondences`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Internal:** Reference to Window Blueprint — (Window Blueprint, [section])
- **HD:** Ra attribution — (Ra Uru Hu, Gate [X])
- **Gene Keys:** Rudd reference — (Rudd, Gene Key [X])
- **I-Ching:** Wilhelm translation — (Wilhelm, Hexagram [X])
- **Minimal academic citation:** The Window is synthesis-heavy; cite underlying systems

---

## Special Formatting

### Three Parallel Domains
The Window's unique three-tier structure:
```markdown
### The Three Parallel Domains

**Archetype Domain:** [The eternal pattern]

**Portal Domain:** [The transformative threshold]

**House Domain:** [The lived experience]
```

### Gene Keys Transformation Arc
Standard format:
```markdown
### Gene Keys Pathway

**Shadow:** [Name] — [Brief description]
**Gift:** [Gift] — [Brief description]
**Siddhi:** [Siddhi] — [Brief description]

*The journey from [Shadow] through [Gift] to [Siddhi] mirrors...*
```

### Contemporary Cultural References
When referencing 1980s encoding:
```markdown
> *Cultural Anchor: This gate's energy crystallized in the 1980s through [cultural reference], encoding the archetype of [description].*
```

### Card-Specific Subtitles
Each card may have an evocative subtitle:
```markdown
# The Innovator
*Gate 3: The Energy of Beginning*
```

---

## Entry Types

### Full Card Entry
Complete template. All three domains. Full Gene Keys arc. Comprehensive oracle guidance.

### Archetype Overview
Focus on eternal pattern. May abbreviate House domain. Cross-reference to related cards.

### House Overview
Focus on lived experience. Practical oracle emphasis. May abbreviate Archetype depth.

### System Overview
Survey format for Window system introduction. Cross-reference heavy.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
- [[_TEMPLATE - Window Card Entry]] — Existing Window-specific template (may be deprecated)
