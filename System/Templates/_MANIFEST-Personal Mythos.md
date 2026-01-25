---
tags: [system, template, manifest, personal-mythos]
system: Personal Mythos
date_created: 2026-01-25
status: canonical
---

# Personal Mythos Section Manifest

This manifest defines approved section names for Personal Mythos Library entries.

---

## Pillar Voice

**Character:** Narrative-psychological, scholarly mystic
**Influences:** Jung (CW), von Franz, Campbell, Hillman, traditional folklore
**Tone:** Depth psychology meets storytelling; never "new age fluffy"—always grounded in scholarship

---

## Required YAML Fields

```yaml
tags: [personal-mythos, {category}, {specific-item}]
system: Personal Mythos
date_created: YYYY-MM-DD

# For Fairy Tales
tale_origin: [Geographic/cultural origin]
source_collection: [Grimm/Andersen/Afanas'ev/etc.]
core_archetype: [Primary archetype]
themes: [List of themes]

# For Archetypes
archetype_category: [Jungian category]
related_archetypes: [List]

# For Synthesis Entries
entry_type: [capstone-synthesis/thematic-overview/reference]
status: [tier-1/tier-2/tier-3-complete]

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
**Primary:** `## Overview`
**Alternates:**
- `## Archetypal Introduction`
- `## Core Pattern`

### DATA Slot (for narrative entries)
**Primary:** `## Plot Summary`
**Alternates:**
- `## The Tale`
- `## Narrative Structure`

**For archetype entries:**
**Primary:** `## Archetypal Cast`
**Alternates:**
- `## Core Attributes`
- `## Defining Characteristics`

**Subsections:**
- `### Principal Figures`
- `### Supporting Characters`
- `### Symbolic Objects`
- `### Key Motifs`

### DEPTH Slot
**Primary:** `## Jungian Analysis`
**Alternates:**
- `## Psychological Depth`
- `## Depth Interpretation`

**Subsections:**
- `### Individuation Journey`
- `### Anima/Animus Dynamics`
- `### Archetypal Encounters`
- `### Developmental Stages`
- `### von Franz Commentary`

### SHADOW Slot
**Primary:** `## Shadow Dynamics`
**Alternates:**
- `## Shadow Work`
- `## The Dark Side`

**Subsections:**
- `### Personal Shadow`
- `### Collective Shadow`
- `### Integration Path`

### PRACTICE Slot
**Primary:** `## Practical Application`
**Alternates:**
- `## Working with This Pattern`
- `## Therapeutic Application`

**Subsections:**
- `### Diagnostic Questions`
- `### For Women`
- `### For Men`
- `### Across Genders`
- `### Shadow Work Exercises`
- `### Dream Work`
- `### Active Imagination`

### LINKS Slot
**Required:** `## Cross-References`

**Subsections:**
- `### Related Tales`
- `### Related Archetypes`
- `### Astrological Parallels`
- `### Tarot Correspondences`
- `### Cross-Pillar Synthesis`

### SOURCES Slot
**Required:** `## Sources`

---

## Citation Style

- **Jung CW:** Volume and paragraph — (CW 9i, ¶ 123) or (CW 9i, p. 45)
- **von Franz:** Work and page — (von Franz, *Shadow and Evil in Fairy Tales*, p. 78)
- **Campbell:** Work reference — (Campbell, *Hero with a Thousand Faces*, Ch. 3)
- **Folklore:** Collection reference — (Grimm, Tale No. 53)
- **Mixed:** Combine as needed for synthesis entries

---

## Special Formatting

### Tale Summaries
Use present tense for plot summaries (narrative convention):
```markdown
The youngest daughter descends into the underworld. She encounters...
```

### Archetypal Cast Format
```markdown
### Archetypal Cast

**The King (Senex):** [Description of function]

**The Princess (Anima):** [Description of function]

**The Witch (Shadow Mother):** [Description of function]
```

### Diagnostic Questions
Use bulleted questions:
```markdown
### Diagnostic Questions

- Where in your life do you feel trapped in the tower?
- What inner voice criticizes your creative expression?
- When did you last encounter the Wise Old Man in dreams?
```

### Gender-Specific Sections
Include when relevant, but always acknowledge fluidity:
```markdown
### For Women
[Specific application]

### For Men
[Specific application]

### Across Genders
[Universal application beyond binary]
```

---

## Entry Types

### Fairy Tale Analysis
Full template. Plot summary essential. Deep Jungian interpretation. Practical shadow work.

### Archetype Entry
May abbreviate plot. Focus on psychological function and manifestations.

### Capstone Synthesis
Extended DEPTH section. Heavy cross-referencing. May span multiple tales/archetypes.

### Thematic Overview
Survey format. May abbreviate PRACTICE. Focus on pattern recognition across sources.

---

## Cross-References

- [[SEMANTIC-SECTION-SYSTEM]] — Master system overview
- [[_TEMPLATE - Library Entry]] — Universal template
