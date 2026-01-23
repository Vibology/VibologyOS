---
tags: [system, protocol, audit, provenance, library-quality]
date_created: 2026-01-23
status: Active
version: 1.0
---

# Prima Materia Verification Audit Protocol

**Purpose:** Systematically verify that every Library entry (645 files) traces back to source material in the Esoteric Grimoire, not AI training data.

**Outcome:** Complete provenance tracking with confidence that all content follows the Fetch→Refine→Commit protocol.

---

## Phase 1: Provenance Infrastructure (Prerequisites)

### 1.1 Add Verification Tracking to YAML Schema

Add new YAML fields to track verification status:

```yaml
source_verified: true|false|pending
verification_date: YYYY-MM-DD
grimoire_source: "Topic/Section name in Esoteric Grimoire"
```

**Status markers:**
- `true` — Content verified against Grimoire
- `false` — Content cannot be verified (needs rewrite)
- `pending` — Not yet audited

### 1.2 Create Verification Queue Tracker

Create `System/Audit Logs/Prima Materia Verification Queue.md` with:
- All 645 files listed by pillar
- Verification status column
- Priority ranking (based on risk analysis below)

---

## Phase 2: Grimoire Inventory

### 2.1 Catalog Esoteric Grimoire Contents

Before verification, we must understand what's actually IN the Grimoire:

**Action:** Use NotebookLM skill to query Grimoire structure:
- "List all major topic headings and sections"
- "What Human Design content is available?"
- "What Tarot content is available?"
- (Repeat for each pillar)

**Output:** Create `System/Esoteric Grimoire Inventory.md` mapping available source material.

### 2.2 Gap Analysis

Compare Grimoire inventory against Library entries to identify:
- Entries with clear corresponding Grimoire content (verifiable)
- Entries with no apparent Grimoire source (requires investigation)
- Entries that may have been synthesized beyond source (requires judgment)

---

## Phase 3: Verification Execution

### 3.1 Priority Ranking (Risk-Based)

Based on exploration findings, verification order:

| Priority | Pillar | Files | Risk Rationale |
|----------|--------|-------|----------------|
| **P1-CRITICAL** | Human Design (Incarnation Crosses) | 193 | Known protocol violation (NEXT.md confirms rebuild) |
| **P2-HIGH** | Astrology | 37 | Monolithic batch (all Jan 8), no incremental verification |
| **P3-HIGH** | Human Design (non-Cross) | 144 | Large, multi-phase creation, volatile timeline |
| **P4-MEDIUM** | The Tarot | 79 | Two-phase batch, some TBD markers |
| **P5-MEDIUM** | The Window | 72 | Recent batch, "personal naming" in commits |
| **P6-LOWER** | Personal Mythos | 74 | Exceptional depth suggests genuine synthesis |
| **P7-LOWER** | Angelology | 31 | Well-structured, integrated |
| **P8-LOWER** | Magdalene Path | 8 | Small, specialized |
| **P9** | Core Foundations | 5 | Meta-documents, architectural |

### 3.2 Verification Process Per Entry

For each Library entry:

1. **Fetch from Grimoire:** Query NotebookLM for the specific topic
   - "What does the Grimoire say about [Gate 51]?"
   - "What information exists on [The Tower card]?"

2. **Compare against Library entry:**
   - Core facts match? (positions, associations, numbers)
   - Terminology consistent with Grimoire?
   - Any content present in Library but absent from Grimoire? (red flag)

3. **Classify result:**
   - **VERIFIED:** Content traces to Grimoire → Update YAML `source_verified: true`
   - **AUGMENTED:** Core from Grimoire, synthesis added → Acceptable if synthesis is clearly marked
   - **UNVERIFIED:** Cannot confirm source → Flag for rewrite

4. **Log findings:** Document verification status in queue tracker

### 3.3 Batch Verification Strategy

Given 645 files, we'll verify in batches by sub-category:

**Human Design batches:**
- Gates (64 entries)
- Channels (36 entries)
- Incarnation Crosses (193 entries)
- Centers (9 entries)
- Authority types (6 entries)
- Profiles (12 entries)
- Types (5 entries)

**Tarot batches:**
- Major Arcana (22 entries)
- Minor Arcana by suit (4 × 14 entries)

*Continue pattern for each pillar...*

---

## Phase 4: Remediation

### 4.1 Rewrite Protocol for Unverified Entries

For entries flagged `source_verified: false`:

1. **Archive original:** Move to `.archive/Unverified/` with note
2. **Fetch fresh:** Use Scribe persona to retrieve raw Grimoire data
3. **Refine:** Use Weaver persona to synthesize
4. **Write new entry:** Following full Refinement Cycle
5. **Update YAML:** Set `source_verified: true`, `verification_date: [today]`

### 4.2 Handling Entries Beyond Grimoire Scope

If a topic exists in Library but NOT in Grimoire:

**Option A:** Entry represents legitimate synthesis (cross-pillar integration)
- Mark as `source_verified: synthesis` with note explaining derivation

**Option B:** Entry was hallucinated
- Archive and delete from active Library

**Decision rule:** If the entry connects two Grimoire-sourced concepts, it's synthesis. If it introduces novel concepts not traceable to any Grimoire content, it's suspect.

---

## Phase 5: Ongoing Protocol Enforcement

### 5.1 Update CLAUDE.md

Add to Refinement Cycle (Section 4):

> **Phase 1 (Fetch/Scribe):** Pull raw data from NotebookLM. Clinical, objective, tabular.
> **NEW: Record `grimoire_source` in YAML frontmatter.**

### 5.2 Pre-Commit Verification

Before any Library commit, verify:
- [ ] Content was fetched from Grimoire (not composed from training)
- [ ] `source_verified: true` in YAML
- [ ] `grimoire_source` identifies specific Grimoire section

### 5.3 Future Audit Checkpoint

Add to quarterly audit protocol:
- Spot-check 5 random entries per pillar
- Verify `source_verified` field is present and accurate
- Query Grimoire to confirm content still matches

---

## Execution Timeline

| Phase | Scope | Estimated Sessions |
|-------|-------|-------------------|
| Phase 1 | Infrastructure setup | 1 session |
| Phase 2 | Grimoire inventory | 1-2 sessions |
| Phase 3 | Verification (645 files) | 8-12 sessions |
| Phase 4 | Remediation (depends on findings) | Variable |
| Phase 5 | Protocol updates | 1 session |

**Total estimated:** 12-16 sessions for complete verification

---

## Verification Test

After completion, the following should be true:
- Every Library file contains `source_verified: true|synthesis`
- A verification queue tracker documents each file's audit
- Grimoire inventory exists mapping available source material
- Zero entries exist that cannot be traced to prima materia
- Protocol updates prevent future training-data contamination

---

## Critical Files to Modify

**New files to create:**
- `System/Audit Logs/Prima Materia Verification Queue.md`
- `System/Esoteric Grimoire Inventory.md`

**Files to update:**
- All 645 Library files (add verification YAML fields)
- `System/PROTOCOL - Library Maintenance & Audit.md` (add provenance checks)
- `CLAUDE.md` (add pre-commit verification requirement)

**Potential archival:**
- Unknown count until Phase 3 reveals unverified entries

---

*"What cannot be traced to the source cannot be trusted as truth."*
