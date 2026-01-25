---
tags: [system, template, manifest, human-design]
system: Human Design
date_created: 2026-01-25
status: canonical
---

# Human Design Section Manifest

This manifest defines approved section names for Human Design Library entries.

---

## Pillar Voice

**Character:** Clinical-mechanical, precise, authoritative
**Influences:** Ra Uru Hu's transmissions, Jovian Archive, Gene Keys (Richard Rudd)
**Tone:** Mechanical accuracy first; psychological depth through Gene Keys integration

---

## Required YAML Fields

```yaml
tags: [human-design, {category}, {specific-item}]
system: Human Design
date_created: YYYY-MM-DD

# For Gates
gate_number: [1-64]
hexagram_name: [I-Ching name]
center: [Center name]
circuitry: [Circuit and sub-circuit]
keynote: [Ra's keynote]
biology: [Biological correspondence]
channels: [Associated channels]
gene_keys: [Shadow → Gift → Siddhi]

# For Centers
center_type: [Motor/Awareness/Pressure/Manifestation/Identity]
defined_function: [When defined]
undefined_function: [When undefined]

# For Channels
channel_number: [X-Y format]
channel_name: [Channel name]
circuitry: [Circuit]
type: [Generated/Projected/Manifested]

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
**Primary:** `## Ra's Definition`
**Alternates:**
- `## Mechanical Overview`
- `## Core Function`

**Format:** Open with direct Ra quote when available:
```markdown
## Ra's Definition

> "[Direct quote from Ra Uru Hu]"

[Expansion and context]
```

### DATA Slot
**Primary:** `## Core Mechanics`
**Alternates:**
- `## Core Correspondences`
- `## Mechanical Structure`

**Subsections:**
- `### Line-by-Line Breakdown`
- `### Exalted Expression`
- `### Detriment Expression`
- `### Harmonic Gates`
- `### Channel Dynamics`

**Standard Gate Table:**
```markdown
| Attribute | Value |
|-----------|-------|
| Gate | [Number] |
| Hexagram | [Name] |
| Center | [Name] |
| Circuit | [Name] |
| Keynote | [Ra's keynote] |
| Biology | [Correlation] |
| Gene Key | [Shadow → Gift → Siddhi] |
```

### DEPTH Slot
**Primary:** `## Circuitry Analysis`
**Alternates:**
- `## Circuit Context`
- `## Energetic Dynamics`

**Subsections:**
- `### Individual/Tribal/Collective Function`
- `### Electromagnetic Dynamics` (for channels)
- `### Gene Keys Transformation Arc`

### SHADOW Slot
**Primary:** `## Not-Self Patterns`
**Alternates:**
- `## Undefined/Open Dynamics`
- `## Conditioning Patterns`

**Subsections:**
- `### Defined Not-Self`
- `### Undefined Vulnerability`
- `### Deconditioning Process`

### PRACTICE Slot
**Primary:** `## Strategy Integration`
**Alternates:**
- `## Living Your Design`
- `## Practical Application`

**Subsections:**
- `### By Type`
- `### Authority Alignment`
- `### 7-Year Deconditioning`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Within Human Design`
- `### I-Ching Foundation`
- `### Gene Keys Pathway`
- `### Window Correspondence`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Ra quotes:** Direct quote with context — "Ra Uru Hu, [lecture/book name]"
- **Jovian Archive:** Reference format — (Jovian Archive, Gate [X] Analysis)
- **Gene Keys:** Book reference — (Rudd, *Gene Keys*, p. XX)
- **I-Ching:** Wilhelm translation preferred — (Wilhelm, I-Ching, Hexagram [X])

---

## Special Formatting

### Gate Numbers
Always include gate number prominently:
```markdown
# Gate 12: Standstill
```

### Gene Keys Arc
Standard format for transformation:
```markdown
**Gene Keys Pathway:** Vanity → Discrimination → Purity
```

### Line Breakdowns
Use H4 for individual lines:
```markdown
#### Line 1: [Name]
**Exalted:** [Expression]
**Detriment:** [Expression]
```

### Circuit Notation
```markdown
**Circuitry:** Individual (Knowing Circuit)
```

---

## Entry Types

### Gate Entry
Full template. Line-by-line breakdown essential. Gene Keys integration required.

### Center Entry
Focus on defined vs. undefined dynamics. May abbreviate PRACTICE for overview entries.

### Channel Entry
Emphasize electromagnetic dynamics between gates. Include both gate perspectives.

### Type/Authority Entry
May omit DATA table. Focus on strategy and decision-making mechanics.

### Incarnation Cross Entry
Abbreviated format. Focus on life purpose theme and gate synthesis.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
