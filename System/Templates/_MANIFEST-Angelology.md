---
tags: [system, template, manifest, angelology]
system: Angelology
date_created: 2026-01-25
status: canonical
---

# Angelology Section Manifest

This manifest defines approved section names for Angelology Library entries.

---

## Pillar Voice

**Character:** Mystical-scholarly, numinous, reverent
**Influences:** Biblical tradition, Pseudo-Dionysius, Davidson, Qabalistic angelology
**Tone:** Elevated language honoring the sacred; dense scriptural references

---

## Required YAML Fields

```yaml
tags: [angelology, {order/hierarchy}, {specific-angel}]
system: Angelology
date_created: YYYY-MM-DD

# For Angelic Orders
order_number: [1-9]
order_name: [Order name]
hebrew_name: [Hebrew transliteration]
triad: [First/Second/Third Triad]
sephirah: [Associated Sephirah]
planetary: [Planetary correspondence]
function: [Primary function]
human_faculty: [Human faculty correspondence]
hd_center: [Human Design center correspondence]

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
**Primary:** `## Essence`
**Alternates:**
- `## Divine Function`
- `## Angelic Nature`

### DATA Slot
**Primary:** `## Correspondences`
**Alternates:**
- `## Qabalistic Correspondences`
- `## Hierarchical Position`

**Subsections:**
- `### Sephirotic Mapping`
- `### Planetary Rulership`
- `### Hebrew Names`
- `### Biblical References`

### DEPTH Slot
**Primary:** `## Theological Depth`
**Alternates:**
- `## Mystical Significance`
- `## Dionysian Hierarchy`

**Subsections:**
- `### Patristic Commentary`
- `### Qabalistic Interpretation`
- `### Jungian Parallels`

### SHADOW Slot
**Primary:** `## Fallen Aspect`
**Alternates:**
- `## Daimonic Counterpart`
- `## Shadow Manifestation`

### PRACTICE Slot
**Primary:** `## Invocation`
**Alternates:**
- `## Contemplative Practice`
- `## Angelic Meditation`

**Subsections:**
- `### Traditional Prayer`
- `### Qabalistic Invocation`
- `### Vibrational Attunement`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Within Angelology`
- `### Qabalistic Integration` (links to Tarot paths)
- `### Human Design Correspondence`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Scriptural:** Inline parenthetical — (Isaiah 6:1-7), (Ezekiel 1:10)
- **Patristic:** Author, work — (Pseudo-Dionysius, *Celestial Hierarchy*, Ch. 6)
- **Davidson:** Page reference — (Davidson, p. 261)
- **Qabalistic:** Tradition attribution — (Golden Dawn tradition)

---

## Special Formatting

### Hebrew Transliteration
Include Hebrew with English transliteration:
```markdown
**Chaioth ha-Qadesh** (חיות הקדש) — "Holy Living Creatures"
```

### Scriptural Blockquotes
```markdown
> "Holy, holy, holy is the Lord of hosts; the whole earth is full of his glory."
> — Isaiah 6:3
```

### Invocation Format
```markdown
### Traditional Invocation

> *[Prayer text in italics]*
>
> — [Source attribution]
```

---

## Entry Types

### Angelic Order Entry
Full template with all sections. Includes triad position, Sephirotic mapping, biblical foundation.

### Individual Angel Entry
May abbreviate DATA section. Focus on specific function and invocation.

### Overview/Synthesis Entry
May omit SHADOW and PRACTICE if purely expository.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
