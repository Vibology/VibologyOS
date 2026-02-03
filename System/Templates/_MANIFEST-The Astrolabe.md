---
tags: [system, template, manifest, the-astrolabe]
system: The Astrolabe
date_created: 2026-02-03
status: canonical
---

# The Astrolabe Section Manifest

This manifest defines approved section names for The Astrolabe Library entries.

---

## Pillar Voice

**Character:** Contemporary-accessible, synthesis-oriented, precise
**Influences:** I-Ching (primary source), Human Design mechanics, Gene Keys, Jungian archetypes, alchemy, 1980s cultural encoding
**Tone:** Modern oracle language grounded in ancient structure; the instrument reads the sky as it actually is, not as we wish it to be

---

## Card Types

The Astrolabe has two parts with distinct entry structures:

### The Athanor (24 cards) — The interpretive lens
- **The Materia** (5 cards): Prima Materia, Sulphur, Mercury, Salt, The Philosopher's Stone
- **The Furnace** (7 cards): Calcination, Dissolution, Separation, Conjunction, Fermentation, Distillation, Coagulation
- **The Archetypes** (12 cards): Zodiacal/Jungian figures — no gate correspondences

### The Codex (64 cards) — The 64-fold architecture
- Organized by 8 trigram families (lower trigram): Heaven, Earth, Thunder, Water, Mountain, Wind, Fire, Lake
- Each card named for the hexagram (I-Ching, best English translation, 1-2 words)
- Gate/hexagram/Gene Keys correspondences belong here exclusively

---

## Required YAML Fields

### Codex Cards (64)
```yaml
tags: [the-astrolabe, codex, family-of-{trigram}, gate-{number}]
system: The Astrolabe
date_created: YYYY-MM-DD

# Card Identity
card_name: "[I-Ching name]"
hexagram: {number}
gate: {number}
trigram_family: "{Family name}"
lower_trigram: "{trigram}"
upper_trigram: "{trigram}"

# Gene Keys
gene_keys_shadow: ""
gene_keys_gift: ""
gene_keys_siddhi: ""

# Human Design
hd_keynote: ""
hd_center: ""
hd_circuit: ""

# Status
status: [Complete/Draft/Stub]
verified: true
verification_date: YYYY-MM-DD
verification_source: ""
grimoire_source: ""
```

### Athanor: Materia Cards (5)
```yaml
tags: [the-astrolabe, athanor, materia]
system: The Astrolabe
date_created: YYYY-MM-DD

card_name: ""
alchemical_principle: ""

status: [Complete/Draft/Stub]
```

### Athanor: Furnace Cards (7)
```yaml
tags: [the-astrolabe, athanor, furnace]
system: The Astrolabe
date_created: YYYY-MM-DD

card_name: ""
operation: ""
sequence: {1-7}

status: [Complete/Draft/Stub]
```

### Athanor: Archetype Cards (12)
```yaml
tags: [the-astrolabe, athanor, archetype, {zodiac-sign}]
system: The Astrolabe
date_created: YYYY-MM-DD

card_name: ""
zodiac_sign: ""
cultural_icon: ""

status: [Complete/Draft/Stub]
```

---

## Approved Section Names

### Codex Card Sections

#### OPENING Slot
**Primary:** `## Core Identity`
**Alternates:**
- `## Essential Meaning`

**Format:**
```markdown
## Core Identity

*[One-line hexagram essence in italics]*

[2-3 paragraph introduction: what this hexagram IS — its image, its movement, its fundamental nature]
```

#### DATA Slot
**Primary:** `## Correspondences`

**Standard Correspondence Table:**
```markdown
| System | Correspondence |
|--------|----------------|
| Hexagram | [Number]: [Name] |
| Trigrams | [Lower] below [Upper] |
| Gate | [Number]: [HD Keynote] |
| Center | [HD Center] |
| Circuit | [Circuit name] |
| Gene Keys | [Shadow] → [Gift] → [Siddhi] |
```

**Subsections:**
- `### The Hexagram (I-Ching)` — Image, Judgment, structural analysis
- `### The Gate (Human Design)` — Mechanical keynote, center, circuit
- `### The Gene Keys` — Shadow/Gift/Siddhi transformation arc

#### DEPTH Slot
**Primary:** `## Synthesis Notes`
**Alternates:**
- `## Deeper Patterns`

**Subsections:**
- `### Cultural Encoding` — 1980s crystallization of this energy
- `### Archetypal Resonance` — Jungian/mythological patterns
- `### Cross-System Convergence` — Where multiple systems illuminate the same truth

**Vibology Synthesis Format:**
```markdown
> *Vibology Synthesis: [Original integration insight]*
```

#### SHADOW Slot
**Primary:** `## Shadow Aspect`
**Alternates:**
- `## When Contracted`

#### PRACTICE Slot
**Primary:** `## Oracle Reading`
**Alternates:**
- `## When This Card Appears`

**Reading Format:**
```markdown
### When This Card Appears

**Core Message:** [Primary divination meaning]

**Shadow Warning:** [What to watch for]

**Gift Invitation:** [What becomes possible]

**Siddhi Vision:** [Transcendent possibility]
```

#### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Related Codex Cards` — Same family, channel partners, thematic links
- `### Tarot Correspondences`
- `### Cross-Pillar Synthesis`

#### SOURCES Slot
**Required:** `## Sources`

---

### Athanor: Materia Card Sections

OPENING → DEPTH → PRACTICE → LINKS → SOURCES

- **OPENING:** `## Alchemical Principle` — What this substance IS in the Great Work
- **DEPTH:** `## Synthesis Notes` — Cross-system resonances (Jungian, Qabalistic, elemental)
- **PRACTICE:** `## Oracle Reading` — What it means when drawn

---

### Athanor: Furnace Card Sections

OPENING → DEPTH → PRACTICE → LINKS → SOURCES

- **OPENING:** `## The Operation` — What this stage of transformation does
- **DEPTH:** `## Synthesis Notes` — Correspondences across alchemical traditions
- **PRACTICE:** `## Oracle Reading` — What it means when drawn; what stage of transformation is active

---

### Athanor: Archetype Card Sections

OPENING → DATA → DEPTH → PRACTICE → LINKS → SOURCES

- **OPENING:** `## Archetypal Identity` — The eternal pattern this figure embodies
- **DATA:** `## Correspondences` — Zodiac sign, Jungian archetype, 1980s cultural icon (NO gate references)
- **DEPTH:** `## Synthesis Notes` — Mythological resonance, cultural encoding, Jungian analysis
- **PRACTICE:** `## Oracle Reading` — What it means when drawn; who is present in the work

---

## Citation Style

- **I-Ching:** Wilhelm, Huang, or Karcher as appropriate — (Wilhelm, Hexagram [X]) or (Huang, Hexagram [X])
- **HD:** Ra attribution — (Ra Uru Hu, Gate [X])
- **Gene Keys:** Rudd reference — (Rudd, Gene Key [X])
- **Jungian:** Standard reference — (Jung, CW [vol], [section])
- **Alchemical:** Primary source where available; secondary attribution otherwise

---

## Special Formatting

### Gene Keys Transformation Arc
```markdown
### Gene Keys Pathway

**Shadow:** [Name] — [Brief description]
**Gift:** [Name] — [Brief description]
**Siddhi:** [Name] — [Brief description]

*The journey from [Shadow] through [Gift] to [Siddhi] mirrors...*
```

### Contemporary Cultural References
```markdown
> *Cultural Anchor: This hexagram's energy crystallized in the 1980s through [cultural reference], encoding the archetype of [description].*
```

### Trigram Family Context
```markdown
### Family Context

This card belongs to the **Family of [Trigram]** — [brief family character]. The lower trigram [name] provides [quality], while the upper trigram [name] shapes its expression as [quality].
```

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master section rhythm
- [[_TEMPLATE - Library Entry]] — Universal template
