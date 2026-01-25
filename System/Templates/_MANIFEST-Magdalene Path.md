---
tags: [system, template, manifest, magdalene-path]
system: The Magdalene Path
date_created: 2026-01-25
status: canonical
---

# Magdalene Path Section Manifest

This manifest defines approved section names for Magdalene Path Library entries.

---

## Pillar Voice

**Character:** Mystical-devotional, scholarly yet intimate
**Influences:** Cynthia Bourgeault, Gnostic gospels, Wisdom tradition, contemplative Christianity
**Tone:** Vertical axis language; kenotic descent; sacred union; never preachy—always invitational

---

## Required YAML Fields

```yaml
tags: [magdalene-path, {category}, {specific-topic}]
system: The Magdalene Path
date_created: YYYY-MM-DD

# Category Fields
category: [Overview/Practice/Gospel/Synthesis]
subsystem: [If applicable: Kenosis/Singleness/etc.]

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
**Primary:** `## Core Teaching`
**Alternates:**
- `## Essential Wisdom`
- `## The Heart of the Matter`

**Format:** Often opens with Vibology Synthesis callout:
```markdown
## Core Teaching

> *Vibology Synthesis: [Contextual framing for this teaching]*

[Main content]
```

### DATA Slot
**Primary:** `## The Eight Boughs`
**Alternates:**
- `## Structural Framework`
- `## Gospel Foundation`

**Subsections:**
- `### The Eight Boughs` (numbered enumeration when applicable)
- `### Textual Foundation`
- `### Key Logia`

**For Gospel-based entries:**
```markdown
### Gospel Foundation

**Gospel of Mary:**
> "[Direct quotation]"
> — Gospel of Mary, [chapter:verse]

**Gospel of Philip:**
> "[Direct quotation]"
> — Gospel of Philip, [saying number]
```

### DEPTH Slot
**Primary:** `## Mystical Depth`
**Alternates:**
- `## Contemplative Dimensions`
- `## Wisdom Interpretation`

**Subsections:**
- `### Bourgeault's Commentary`
- `### Gnostic Context`
- `### The Z-Axis (Vertical Dimension)`
- `### Union of Opposites`

### SHADOW Slot
**Primary:** `## Kenotic Descent`
**Alternates:**
- `## The Path of Letting Go`
- `## Ego Dissolution`

**Subsections:**
- `### What Must Die`
- `### Resistances`
- `### Dark Night Parallels`

### PRACTICE Slot
**Primary:** `## Spiritual Practice`
**Alternates:**
- `## Contemplative Application`
- `## Living the Teaching`

**Subsections:**
- `### Kenosis Practice`
- `### Singleness Meditation`
- `### Substituted Love`
- `### Body-Based Practice`
- `### Lectio Divina Application`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Within the Magdalene Path`
- `### Jungian Parallels`
- `### Qabalistic Correspondences`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Bourgeault:** Work and page — (Bourgeault, *Meaning of Mary Magdalene*, p. 145)
- **Gospels:** Chapter:verse or saying — (Gospel of Mary, 4:7) or (Gospel of Philip, Saying 63)
- **Leloup:** Translation reference — (Leloup, *Gospel of Mary Magdalene*, p. 32)
- **Wisdom tradition:** Author attribution — (Meister Eckhart)

---

## Special Formatting

### Vibology Synthesis Callouts
Use for original integration work:
```markdown
> *Vibology Synthesis: The following integration between Kenosis and the Not-Self is an original contribution, not found in Bourgeault's work.*
```

### Gospel Quotations
Block quote format with precise attribution:
```markdown
> "When the soul had overcome the third Power, it went upwards and saw the fourth Power, which took seven forms."
> — Gospel of Mary, 16:1-4
```

### The Eight Boughs Format
When referencing the complete framework:
```markdown
### The Eight Boughs of Reunion

1. **Conscious Love** — [brief description]
2. **Singleness** — [brief description]
3. **Kenosis** — [brief description]
4. **Substituted Love** — [brief description]
5. **The Bridal Chamber** — [brief description]
6. **Anointing** — [brief description]
7. **Dying Before You Die** — [brief description]
8. **Conscious Resurrection** — [brief description]
```

### Vertical Axis Language
Use Z-axis terminology consistently:
```markdown
The vertical axis (Z-axis) represents the dimension of depth and height—
the descent into kenotic emptying and the ascent toward union.
```

---

## Entry Types

### Core Teaching Entry
Full template. Deep engagement with primary sources. Strong practice section.

### Gospel Commentary
Emphasize DATA (textual foundation) and DEPTH. Practice may be abbreviated.

### Practice Guide
Emphasize PRACTICE section. May abbreviate DATA if practice-focused.

### Overview/Synthesis
Survey format. Cross-reference heavy. May omit SHADOW if purely expository.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
