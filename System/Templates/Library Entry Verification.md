---
tags: [system, template, verification, audit]
date_created: 2026-01-23
---

# Library Entry Verification Template

## Entry Details
- **File Path:** [full path]
- **Pillar:** [pillar name]
- **Date Created:** [YYYY-MM-DD from file]
- **Verification Date:** [YYYY-MM-DD]
- **Verifier:** [session identifier]

---

## Step 1: Grimoire Query (Core Facts)

**Query Used:** "[exact NotebookLM query for core content]"

**Grimoire Response Summary:**
- [Key fact 1 from Grimoire]
- [Key fact 2 from Grimoire]
- [Key fact 3 from Grimoire]
- [Etc.]

**Core Facts Match:** ☐ YES / ☐ NO / ☐ PARTIAL

**Discrepancies (if any):**
- [Note any content in Library absent from Grimoire]
- [Note any contradictions]

---

## Step 2: Synthesis Source Verification (if applicable)

### Jung Citations
- Check all CW (Collected Works) references for accuracy
- Verify quotes match original sources
- **Status:** ☐ VERIFIED / ☐ NOT APPLICABLE / ☐ UNVERIFIED

**Notes:**
- [List any CW citations found and verification status]
- [Note if specific Jung works are referenced (e.g., "CW 9i, p. 123")]

### Mythology References
- Verify Greek/Roman/Egyptian/Hindu mythology accuracy
- Check against standard mythological sources (Larousse, Hamilton, Bulfinch)
- **Status:** ☐ VERIFIED / ☐ NOT APPLICABLE / ☐ UNVERIFIED

**Notes:**
- [List mythological figures/stories referenced]
- [Confirm accuracy against Grimoire mythology inventory]

### Cross-System References
- Verify [[wikilinks]] point to valid integration points
- Confirm cross-pillar correspondences are legitimate
- **Status:** ☐ VERIFIED / ☐ NOT APPLICABLE / ☐ UNVERIFIED

**Notes:**
- [List cross-pillar connections made]
- [Verify correspondences are documented in Grimoire]

### Fairy Tale/Folklore
- Verify tale summaries and interpretations are accurate
- Check against standard folklore sources (Grimm, Andersen, Afanas'ev)
- **Status:** ☐ VERIFIED / ☐ NOT APPLICABLE / ☐ UNVERIFIED

**Notes:**
- [List tales referenced]
- [Confirm plot summaries match original sources]

---

## Step 3: Classification

**Verification Result:**
- ☐ **VERIFIED** — Core content + synthesis sources both trace to legitimate sources
- ☐ **AUGMENTED** — Grimoire + legitimate scholarly synthesis (mark as synthesis)
- ☐ **UNVERIFIED** — Cannot confirm source; flag for remediation

**Grimoire Source:** "[Specific section name in Esoteric Grimoire]"

**Verification Notes:** "[Any additional context: synthesis type, external sources, etc.]"

---

## Step 4: Add Citations

**Inline Footnotes Required:**

For each core fact verified against Grimoire, add inline footnote:
```markdown
The Sun rules Leo and is exalted in Aries at 19°[^1].

[^1]: Lilly, *Christian Astrology*, Book 1, Chapter 4; Ptolemy, *Tetrabiblos*, Book 1
```

**Citation Checklist:**
- ☐ Core facts (dignities, gates, correspondences) cited
- ☐ Direct quotes cited with exact source location
- ☐ Synthesis sections cite multiple sources
- ☐ Personal interpretation clearly marked (not cited to Grimoire)

**Footnotes Section Added:** ☐ YES / ☐ NO

---

## Step 5: YAML to Add

```yaml
source_verified: true | synthesis | false
verification_date: YYYY-MM-DD
grimoire_source: "Section name"
verification_notes: "[If synthesis, explain derivation and external sources verified]"
```

---

## Notes
[Any observations, concerns, or follow-up needed]

---

## Verification Standards Quick Reference

### source_verified: true
- Core facts trace directly to Grimoire
- Synthesis sources verified (Jung CW, mythology, etc.)
- Scholarly citations included from NotebookLM cited works
- High confidence in accuracy

### source_verified: synthesis
- Cross-pillar integration OR
- Scholarly synthesis beyond single Grimoire source
- Core sources verified; synthesis layer documented
- Legitimate Weaver work

### source_verified: pre-verified
- Incarnation Crosses only
- Rebuilt from NotebookLM (commit 6c5dce9)
- Metadata audit confirms consistency

### source_verified: false
- Cannot confirm Grimoire source
- Synthesis sources unverifiable or inaccurate
- Flag for remediation (rewrite or archive)
