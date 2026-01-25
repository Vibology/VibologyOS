---
tags: [system, checklist, verification, quality-control]
date_created: 2026-01-24
status: Active
---

# Verification Quality Control Checklist

**Purpose:** Ensure every file marked as "verified" meets the Prima Materia Verification standard.

**Rule:** NO FILE IS VERIFIED WITHOUT PASSING ALL CHECKS.

---

## Pre-Commit Checklist (Run on EVERY File)

### 1. Inline Citations Check

```bash
# Check if file has inline citations
grep -q "(Davidson\|Wang\|Agrippa\|Bourgeault\|Gospel of\|Ra Uru Hu\|Rudd\|Huang\|Jung\|Davis\|Huxley\|de Quillan\|Estés)" [filename]
```

**Required:** ✓ File must contain inline citations in format: `(Author, p. XX)` or `(Source)`

**Common patterns:**
- `(Davidson, p. 123)`
- `(Wang, Ch. 5)`
- `(Gospel of Mary)`
- `(Bourgeault, 2010)`

**If FAIL:** Add inline citations for all factual claims before proceeding.

---

### 2. References Section Check

```bash
# Check if file has References section
grep -q "^## References" [filename]
```

**Required:** ✓ File must have `## References` section at end (before final `---`)

**Format:**
```markdown
## References

*All citations trace to sources in the Esoteric Grimoire (NotebookLM).*

Author, Name. *Book Title*. Publisher, Year.
- Specific claim: p. XX
- Another claim: pp. XX-XX
- Author cites Secondary Source: Ch. X

[Additional sources...]
```

**If FAIL:** Create References section with full bibliographic details and page numbers.

---

### 3. YAML Frontmatter Check

```bash
# Check if file has verification metadata
grep -q "^verified:" [filename]
grep -q "^date_updated:" [filename]
grep -q "^verification_source:" [filename]
```

**Required:** ✓ YAML frontmatter must include:
```yaml
date_updated: YYYY-MM-DD
verified: YYYY-MM-DD
verification_source: Esoteric Grimoire
```

**If FAIL:** Add verification metadata to frontmatter.

---

### 4. Vibology Synthesis Marking

```bash
# Check for synthesis markers
grep -q "Vibology Synthesis" [filename]
```

**Required (if applicable):** ✓ All original integrations marked with blockquote:
```markdown
> *Vibology Synthesis: The following framework integrates...*
```

**Check manually:** Are there cross-system integrations, Human Design mappings, or original frameworks that should be marked as synthesis?

**If unmarked synthesis exists:** Add blockquote markers.

---

### 5. Orphaned Claims Check

**Manual Review Required:**

Read through the file and identify:
- [ ] Are there factual statements without citations?
- [ ] Are there quotes without attribution?
- [ ] Are there "some scholars say" or "tradition holds" without specifics?

**If YES to any:** Add inline citations or mark as Vibology Synthesis.

---

### 6. Secondary Source Attribution

```bash
# Check for secondary source patterns
grep -i "cites\|cited in\|referenced in\|according to" [filename]
```

**Required format:**
- `Bourgeault cites Williams on mystical substitution (Bourgeault, Ch. 12)`
- NOT: `Williams describes mystical substitution...` (unless Williams is in Grimoire)

**If FAIL:** Rewrite to attribute secondary sources through primary sources.

---

## Quick Verification Command

Run this single command to check all three critical requirements:

```bash
FILE="[filename]"
echo "Checking: $FILE"
echo "1. References section:" && grep -q "^## References" "$FILE" && echo "   ✓ Present" || echo "   ✗ MISSING"
echo "2. Inline citations:" && grep -q "(Davidson\|Wang\|Agrippa\|Bourgeault\|Gospel of" "$FILE" && echo "   ✓ Present" || echo "   ✗ MISSING"
echo "3. Verified date:" && grep -q "^verified:" "$FILE" && echo "   ✓ Present" || echo "   ✗ MISSING"
```

---

## Batch Verification Script

For checking multiple files at once:

```bash
#!/bin/bash
# Check all files in a directory

for file in "$@"; do
  echo "=== $(basename "$file") ==="
  has_refs=$(grep -q "^## References" "$file" && echo "REF✓" || echo "REF✗")
  has_cites=$(grep -q "(Davidson\|Wang\|Agrippa\|Bourgeault\|Gospel of" "$file" && echo "CITE✓" || echo "CITE✗")
  has_verified=$(grep -q "^verified:" "$file" && echo "VER✓" || echo "VER✗")
  echo "$has_refs | $has_cites | $has_verified"
  echo
done
```

**Usage:**
```bash
bash check_verification.sh Library/The\ Seven\ Pillars\ of\ Understanding/Angelology/*.md
```

---

## Remediation Priority

If a file fails verification checks:

1. **Missing References section** → PRIORITY 1 (creates unverifiable claims)
2. **Missing inline citations** → PRIORITY 2 (reduces traceability)
3. **Missing YAML metadata** → PRIORITY 3 (tracking issue, not content issue)
4. **Unmarked synthesis** → PRIORITY 4 (clarity issue)

---

## Pass Criteria

A file is **VERIFIED** only when:

- ✓ All factual claims have inline citations
- ✓ References section exists with full bibliographic details
- ✓ YAML frontmatter includes verification metadata
- ✓ All synthesis content clearly marked
- ✓ No orphaned claims or unsourced statements
- ✓ Secondary sources properly attributed through primary sources

**If any criterion fails, the file is INCOMPLETE and must be remediated.**

---

## Revision History

| Date | Change |
|------|--------|
| 2026-01-24 | Checklist created in response to discovery of 15 incomplete Angelology files |
| 2026-01-24 | Added batch verification script and quick verification command |

---
