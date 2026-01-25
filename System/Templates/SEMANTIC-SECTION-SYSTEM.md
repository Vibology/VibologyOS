---
tags: [system, template, library, standards]
date_created: 2026-01-25
status: canonical
---

# Semantic Section System

The Semantic Section System provides unified structure across all Library entries while preserving each pillar's distinctive voice and terminology.

---

## Core Principle

Every Library entry follows the same **semantic rhythm**—a sequence of purposes—but each pillar expresses those purposes using its own traditional language.

**The Rhythm:**
```
OPENING → DATA → DEPTH → SHADOW → PRACTICE → LINKS → SOURCES
```

A reader who knows this rhythm can navigate any entry in any pillar, finding equivalent content in predictable locations.

---

## The Seven Semantic Slots

### 1. OPENING
**Purpose:** Establish the entry's core identity and significance in 2-3 paragraphs.
**Contains:** Essential definition, archetypal essence, why this matters.
**Position:** Immediately after title (H1).

### 2. DATA
**Purpose:** Present factual correspondences, mechanics, and reference information.
**Contains:** Tables, lists, dignities, gates, letters, numbers—objective data.
**Position:** After OPENING.

### 3. DEPTH
**Purpose:** Explore psychological, spiritual, and interpretive dimensions.
**Contains:** Jungian analysis, theological meaning, circuitry dynamics, mythological parallels.
**Position:** After DATA.

### 4. SHADOW
**Purpose:** Address distortions, pitfalls, and contracted expressions.
**Contains:** Not-Self patterns, fallen aspects, reversed meanings, shadow dynamics.
**Position:** After DEPTH. *Optional for pure reference entries.*

### 5. PRACTICE
**Purpose:** Provide practical application and integration guidance.
**Contains:** Invocations, strategy integration, divination use, shadow work exercises.
**Position:** After SHADOW. *Optional for pure reference entries.*

### 6. LINKS
**Purpose:** Connect to related entries across the vault.
**Contains:** Wikilinks to related entries within pillar and cross-pillar.
**Position:** Before SOURCES. *Required for all entries.*

### 7. SOURCES
**Purpose:** Document verification and provide bibliography.
**Contains:** Citations, verification notes, grimoire sources.
**Position:** Final section. *Required for all entries.*

---

## Pillar Section Names

Each pillar has approved section names that map to semantic slots:

| Slot | Angelology | Astrology | Human Design | Personal Mythos | Magdalene Path | Tarot | The Window |
|------|------------|-----------|--------------|-----------------|----------------|-------|------------|
| OPENING | Essence | Archetypal Essence | Ra's Definition | Overview | Core Teaching | Qabalistic Position | Core Domain |
| DATA | Correspondences | Dignities & Rulerships | Core Mechanics | Archetypal Cast | The Eight Boughs | Traditional Symbolism | Correspondences |
| DEPTH | Theological Depth | Psychological Depth | Circuitry Analysis | Jungian Analysis | Mystical Depth | Esoteric Interpretation | Synthesis Notes |
| SHADOW | Fallen Aspect | Shadow Expression | Not-Self Patterns | Shadow Dynamics | Kenotic Descent | Reversed Meaning | Shadow Aspect |
| PRACTICE | Invocation | Interpretation Guide | Strategy Integration | Shadow Work | Spiritual Practice | Divination Use | Oracle Reading |
| LINKS | Cross-References | Cross-References | Cross-References | Cross-References | Cross-References | Cross-References | Cross-References |
| SOURCES | Sources | Sources | Sources | Sources | Sources | Sources | Sources |

**Note:** Each pillar's manifest (`_MANIFEST-[Pillar].md`) contains the full list of approved section names and variations.

---

## Required vs Optional Sections

### Always Required
- **OPENING** — Every entry must establish its identity
- **LINKS** — Every entry must connect to related content
- **SOURCES** — Every entry must document its verification

### Conditionally Required
- **DATA** — Required for reference entries (planets, gates, archetypes, cards)
- **DEPTH** — Required for entries beyond simple reference

### Optional
- **SHADOW** — Include when relevant; may omit for purely positive archetypes
- **PRACTICE** — Include when actionable guidance exists

---

## YAML Frontmatter Standards

All Library entries must include:

```yaml
---
# IDENTIFICATION (Required)
tags: [pillar-tag, category, descriptors]
system: [Pillar Name]
date_created: YYYY-MM-DD

# VERIFICATION (Required)
verified: true
verification_date: YYYY-MM-DD
verification_source: "Primary source name"
grimoire_source: "Specific NotebookLM section"
verification_notes: "What is verified vs synthesized"

# PILLAR-SPECIFIC (Variable)
# See individual pillar manifests for required fields
---
```

---

## Formatting Standards

### Headers
- **H1 (`#`):** Title only—one per file
- **H2 (`##`):** Semantic section headers (from pillar manifest)
- **H3 (`###`):** Subsections within semantic sections
- **H4 (`####`):** Rare; use only for deep nesting

### Horizontal Rules
Use `---` to separate major semantic sections for visual clarity.

### Tables
- Use for DATA sections extensively
- Standard markdown table format
- Include headers

### Blockquotes
- Use for primary source quotations
- Use for Vibology Synthesis callouts: `> *Vibology Synthesis: [explanation]*`

### Wikilinks
- `[[Entry Name]]` for same-pillar links
- `[[Pillar/Entry Name]]` for cross-pillar links
- `[[Entry Name|Display Text]]` when display differs from filename

### Citations
- Inline parenthetical for scriptural: (Isaiah 6:1-7)
- Footnotes for scholarly: [^1]
- Bibliography in SOURCES section

---

## Implementation

1. **Pillar Manifests:** Each pillar has a manifest file defining its approved section names
2. **Audit Process:** Existing files audited against their pillar manifest
3. **Remediation:** Non-conforming files updated to use approved sections
4. **New Entries:** Created using pillar-specific template

See: `_TEMPLATE - Library Entry.md` for the universal template with semantic slots.

---

## Cross-Reference

- [[_TEMPLATE - Library Entry]] — Universal entry template
- [[_MANIFEST-Angelology]] — Angelology section names
- [[_MANIFEST-Astrology]] — Astrology section names
- [[_MANIFEST-Human Design]] — Human Design section names
- [[_MANIFEST-Personal Mythos]] — Personal Mythos section names
- [[_MANIFEST-Magdalene Path]] — Magdalene Path section names
- [[_MANIFEST-Tarot]] — Tarot section names
- [[_MANIFEST-The Window]] — The Window section names
