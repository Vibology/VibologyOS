---
tags: [system, protocol, maintenance, audit, library-quality]
date_created: 2026-01-10
date_updated: 2026-01-19
version: 1.1
status: Active
---

# Library Maintenance & Audit Protocol

**Current Library Statistics:** See `📖 Library/📖 Library Status.md` for up-to-date entry counts and pillar distribution.

## Purpose

The Library is the foundational knowledge base of VibologyOS. Without systematic maintenance, quality degrades over time through:
- **Dead links** (references to entries that don't exist or have moved)
- **Incomplete stubs** (entries marked TBD or below Tier 1 quality)
- **Outdated synthesis** (insights superseded by deeper understanding)
- **Tag inconsistency** (taxonomy drift as conventions evolve)
- **Orphaned content** (entries with no inbound or outbound wikilinks)

**This protocol establishes:**
1. **Quarterly audit cycles** - Systematic review schedule
2. **Audit checklist** - Specific tasks for each cycle
3. **Link verification process** - How to find and fix dead/broken links
4. **Deprecation standards** - When and how to archive outdated content
5. **Quality thresholds** - Minimum standards for Library entries
6. **Index maintenance** - Keeping master lists current

**Goal:** Preserve Library integrity as it scales—what exists is accurate, what's linked is findable, what's outdated is clearly marked.

---

## I. Audit Cycle Structure

### Frequency: Quarterly (Every 90 Days)

**Rationale:** Quarterly cadence balances thoroughness with feasibility. More frequent audits create maintenance overhead; less frequent allows quality drift.

**Scheduled Reviews:**
- **Q1 (January-March):** Winter audit
- **Q2 (April-June):** Spring audit
- **Q3 (July-September):** Summer audit
- **Q4 (October-December):** Fall audit

**Duration:** Plan for 2-4 hours per quarterly audit (depends on Library size and issues found).

**Trigger Conditions:**
- **Scheduled:** Every 90 days from last audit
- **Threshold-Based:** If Library grows by 50+ entries since last audit, schedule early audit
- **Emergency:** If major restructuring occurs (directory reorganization, tag taxonomy change), run immediate audit

**Next Audit Due:** (Track in NEXT.md or create dedicated tracker file)

---

## II. Quarterly Audit Checklist

Each quarterly audit should systematically work through the following tasks. Track completion with checkboxes.

### Phase 1: Preparation (5-10 minutes)

- [ ] **Create audit log file:** `◈ System/Audit Logs/YYYY-MM-DD - Q[X] Library Audit.md`
- [ ] **Check Library size:** Run `find "📖 Library" -name "*.md" | wc -l` to count current entries
- [ ] **Review recent commits:** Run `git log --oneline --since="90 days ago" -- "📖 Library"` to see what's changed
- [ ] **Note major additions:** Identify new systems, categories, or significant expansions since last audit

### Phase 2: Link Verification (30-45 minutes)

**Goal:** Ensure all wikilinks point to existing entries.

#### 2.1 Extract All Wikilinks

```bash
# Extract all wikilinks from Library files
grep -rh "\[\[.*\]\]" "📖 Library" --include="*.md" | \
  grep -o "\[\[[^]]*\]\]" | \
  sort | uniq > /tmp/all_library_links.txt
```

#### 2.2 Check Each Link Exists

For each unique wikilink:
1. Search for corresponding file: `find "📖 Library" -name "*Link Name*"`
2. If not found, mark as **dead link**
3. Record in audit log with location where link appears

#### 2.3 Common Dead Link Causes

- **Renamed files:** Entry was renamed but old links not updated
- **Moved files:** Entry moved to different category but links still point to old location
- **Planned entries:** Link created before entry exists (acceptable if intentional)
- **Typo:** Link misspelled (e.g., `[[Saturnn]]` instead of `[[Saturn]]`)

#### 2.4 Fix Dead Links

**Automated approach (when possible):**
```bash
# Find and replace across all Library files
grep -rl "\[\[Old Name\]\]" "📖 Library" --include="*.md" | \
  xargs sed -i 's/\[\[Old Name\]\]/\[\[New Name\]\]/g'
```

**Manual approach (when automated unsafe):**
- Read file containing dead link
- Use Edit tool to update link
- Verify fix with grep

**Planned entry links:**
- If link points to planned-but-not-yet-created entry, mark in audit log as "intentional forward reference"
- Consider creating stub entry if link appears in 3+ files

### Phase 3: Incomplete Entry Identification (20-30 minutes)

**Goal:** Find entries below minimum quality threshold (Tier 1 standard).

#### 3.1 Find Small Files (Likely Stubs)

```bash
# Find files under 2KB (approximately <200 lines)
find "📖 Library" -type f -name "*.md" -size -2k
```

#### 3.2 Find Files Marked TBD

```bash
# Search for TBD markers
grep -l "TBD\|To be expanded\|Stub\|Placeholder" "📖 Library" -r --include="*.md"
```

#### 3.3 Check for Missing Sections

For each entry, verify presence of required sections (per Library Content Standard):
- [ ] YAML frontmatter (tags, system, date_created, entity_id if applicable)
- [ ] Overview/Introduction
- [ ] Core Symbolism or Mechanics
- [ ] Jungian/Archetypal Layer
- [ ] Internal Links section
- [ ] At least 3 wikilinks to other Library entries

**Red flags:**
- No YAML frontmatter
- No Internal Links section
- Zero wikilinks
- Under 500 words (likely Tier 0/stub)

#### 3.4 Prioritize Expansion

Mark incomplete entries by priority:
- **High:** Core concepts referenced by 5+ other entries (e.g., [[Saturn]], [[The Tower]], [[Sacral Center]])
- **Medium:** Entries in active work area (e.g., if currently expanding Cups suit, prioritize Cup stubs)
- **Low:** Obscure entries rarely referenced

Document prioritized list in audit log.

### Phase 4: Outdated Content Review (15-30 minutes)

**Goal:** Identify synthesis that may need revision due to deepened understanding.

#### 4.1 Check for Superseded Insights

Look for files containing:
- **Old understanding markers:** "Initial interpretation," "Early understanding," "Version 1"
- **Contradiction notes:** "(This conflicts with...)", "(Revised understanding:...)"
- **Date-sensitive content:** References to "current transit" or "as of [old date]"

#### 4.2 Compare with Recent Synthesis

If same topic covered in:
- **Older Library entry** (e.g., 2025 file on Saturn)
- **Recent synthesis piece** (e.g., 2026 cross-system Saturn synthesis)

The older entry may need:
- **Revision:** Incorporate new insights from synthesis
- **Deprecation:** Mark as superseded and point to newer work
- **Integration:** Merge both into comprehensive unified entry

#### 4.3 Flag for Review

Don't automatically delete or archive—flag for user review:
- Create "Flagged for Review" section in audit log
- Note: "Entry X may be outdated; compare with [newer synthesis Y]"
- Let user decide: revise, deprecate, or keep as-is

### Phase 5: Tag Consistency Check (20-30 minutes)

**Goal:** Ensure all entries follow standardized tag taxonomy (per Search & Navigation Protocol).

#### 5.1 Check Tag Format

All tags should use:
- **Hashtag format:** `#tarot` not `tarot`
- **Lowercase:** `#major-arcana` not `#Major-Arcana`
- **Hyphens for multi-word:** `#human-design` not `#humandesign`
- **Singular form:** `#planet` not `#planets` (except category tags)

```bash
# Find files with non-hashtag tags (old format)
grep -l "^tags: \[" "📖 Library" -r --include="*.md" | \
  xargs grep -L "#"
```

#### 5.2 Verify Required Tags

Each entry must have:
1. **System tag:** `#tarot`, `#astrology`, `#human-design`, etc.
2. **Category tag:** `#major-arcana`, `#planets`, `#type`, etc.

```bash
# Find entries without system tag
grep -L "#tarot\|#astrology\|#human-design\|#qabalah\|#jungian\|#angelology\|#synthesis" \
  "📖 Library" -r --include="*.md"
```

#### 5.3 Fix Tag Inconsistencies

**Batch update when safe:**
- If entire directory needs same fix (e.g., all Tarot files missing hashtags), use sed
- Test on one file first, then apply to all

**Manual update when nuanced:**
- Read file, understand context, apply appropriate tags per taxonomy
- Commit tag fixes separately from content changes for clear git history

### Phase 6: Orphaned Content Detection (15-20 minutes)

**Goal:** Find entries with no inbound or outbound wikilinks—isolated islands in the knowledge graph.

#### 6.1 Find Entries with Zero Outbound Links

```bash
# Files containing no wikilinks
grep -L "\[\[.*\]\]" "📖 Library" -r --include="*.md"
```

**Acceptable cases:**
- Very new entries (created <7 days ago)
- Index files (they list links but may not use wikilink format)

**Action required:**
- Add relevant wikilinks to connect to related concepts
- Cross-reference with other systems

#### 6.2 Find Entries with Zero Inbound Links

For each entry, search if any other file links to it:

```bash
# Example: Does anything link to "Saturn Return"?
grep -l "\[\[Saturn Return\]\]" "📖 Library" -r --include="*.md"
```

**If zero results:**
- Entry exists but nothing references it
- May indicate: too obscure, newly created, or poorly integrated

**Action options:**
- Add references from related entries (e.g., [[Saturn]] should link to [[Saturn ♄|Saturn Return]])
- If truly isolated and low-value, consider archival

#### 6.3 Document Orphans

List all orphaned entries in audit log with:
- Entry name and path
- Reason for orphaning (new? obscure? redundant?)
- Recommended action (integrate, expand, archive)

### Phase 7: Index File Maintenance (15-25 minutes)

**Goal:** Ensure all Index files (e.g., Tarot Master List) are current and accurate.

#### 7.1 List All Index Files

```bash
find "📖 Library" -name "INDEX*" -type f
```

Expected index files (per Search & Navigation Protocol):
- `📖 Library/The Tarot/INDEX - Tarot Master List.md` ✅ (exists)
- `📖 Library/Astrology/INDEX - Astrology Master List.md` (planned)
- `📖 Library/Human Design/INDEX - Human Design Master List.md` (planned)
- Others as needed

#### 7.2 Verify Index Completeness

For each index file:
1. **Read the index:** Check current completion statistics
2. **Compare with directory:** Run `find` to count actual files vs. index count
3. **Identify missing entries:** Any files not listed in index?
4. **Verify status markers:** Do ✅🟡⚪ markers match actual file quality?

#### 7.3 Update Index Files

If discrepancies found:
- Add missing entries to index
- Update completion statistics
- Adjust status markers (✅ Complete, 🟡 Partial, ⚪ Planned)
- Commit index updates with message: "Update [System] Index after Q[X] audit"

### Phase 8: File Structure & Naming (10-15 minutes)

**Goal:** Ensure consistent naming conventions and proper directory placement.

#### 8.1 Check Naming Conventions

**Library entries should follow:**
- **Tarot:** `Card Name.md` (e.g., `The Tower.md`, `Eight of Wands.md`)
- **Astrology:** `Concept - Subconcept.md` (e.g., `Saturn - Lord of Time.md`, `7th House - Partnership.md`)
- **Human Design:** `Type/Center/Gate Name.md` (e.g., `Sacral Center.md`, `Gate 51 - Shock.md`)

```bash
# Find files with inconsistent naming (e.g., underscores, all-caps, etc.)
find "📖 Library" -name "*_*" -o -name "*[A-Z][A-Z][A-Z]*"
```

#### 8.2 Check Directory Placement

**Common misplacements:**
- Tarot card in wrong suit folder (e.g., Cup card in Wands/)
- Synthesis piece accidentally in Library (should be in `⚛ Synthesis/`)
- Personal chart in Library (should be in `👤 Biographical Information/`)

**Verify by spot-checking:**
- Read file to understand content
- Confirm directory matches content
- Move if misplaced (use `git mv` to preserve history)

#### 8.3 Identify Structural Anomalies

Look for:
- **Duplicate entries:** Two files covering same topic (merge or clarify distinction)
- **Misnamed files:** Filename doesn't match content (rename with `git mv`)
- **Wrong file type:** Non-.md files in Library (images should be in assets/)

### Phase 9: Documentation & Reporting (10-15 minutes)

**Goal:** Record audit findings and create actionable follow-up tasks.

#### 9.1 Complete Audit Log

Audit log should include:
- **Summary statistics:** Total files audited, issues found, fixes applied
- **Dead links:** List of broken wikilinks and whether fixed
- **Incomplete entries:** List of stubs needing expansion (prioritized)
- **Outdated content:** Entries flagged for review
- **Orphaned content:** Entries with no links in/out
- **Tag inconsistencies:** Files needing tag updates
- **Structural issues:** Naming/placement problems

#### 9.2 Create Follow-Up Tasks

Extract actionable items from audit findings:
- **Immediate fixes:** Dead links, critical tag errors, misplaced files
- **Short-term improvements:** Expand high-priority stubs, update outdated entries
- **Long-term goals:** Create missing index files, expand low-priority stubs

**Document in:**
- `NEXT.md` (if urgent/high-priority)
- Audit log "Action Items" section
- Process Gaps tracker (if systemic issue discovered)

#### 9.3 Update Audit Tracker

Create or update `◈ System/Audit Logs/Audit Tracker.md` with:
- Date of this audit
- Next audit due date (90 days from now)
- Summary of issues found/resolved
- Link to full audit log

#### 9.4 Commit Audit Results

```bash
git add "◈ System/Audit Logs/"
git commit -m "Q[X] Library Audit: [brief summary of findings]"
```

**Example:**
```
Q1 2026 Library Audit: 12 dead links fixed, 8 stubs prioritized, tags updated
```

---

## III. Link Verification Process (Detailed)

### What Counts as a "Dead Link"?

A wikilink is **dead** if:
1. **No matching file exists:** `find "📖 Library" -name "*Link Text*"` returns empty
2. **File exists but in wrong location:** Link expects `📖 Library/Tarot/The Tower.md` but file is at `📖 Library/Major Arcana/The Tower.md`
3. **Filename mismatch:** Link says `[[The Hanged Man]]` but file is named `The Hanging Man.md` (typo)

A wikilink is **NOT dead** if:
1. **Planned entry:** Link intentionally points to future entry (document in audit log)
2. **External reference:** Link to synthesis piece in `⚛ Synthesis/` or journal entry (acceptable cross-folder linking)

### Link Verification Workflow

#### Step 1: Extract All Unique Wikilinks

```bash
# Create temporary file with all unique wikilinks
grep -rh "\[\[.*\]\]" "📖 Library" --include="*.md" | \
  grep -o "\[\[[^]]*\]\]" | \
  sed 's/\[\[\(.*\)\]\]/\1/' | \
  sort | uniq > /tmp/unique_wikilinks.txt
```

#### Step 2: Check Each Link (Manual or Script)

For each line in `/tmp/unique_wikilinks.txt`:

```bash
# Example: Check if [[Saturn]] resolves
LINK="Saturn"
RESULTS=$(find "📖 Library" -name "*${LINK}*" -type f)

if [ -z "$RESULTS" ]; then
  echo "DEAD LINK: [[${LINK}]]"
else
  echo "OK: [[${LINK}]] -> ${RESULTS}"
fi
```

#### Step 3: Locate Dead Link Sources

For each dead link, find where it's used:

```bash
# Where does [[Dead Link]] appear?
grep -rn "\[\[Dead Link\]\]" "📖 Library" --include="*.md"
```

Output shows:
```
📖 Library/Tarot/Major Arcana/The Tower.md:45:Related to [[Dead Link]]
📖 Library/Astrology/Planets/Saturn.md:89:See also [[Dead Link]]
```

#### Step 4: Determine Fix Strategy

**If file was renamed:**
1. Find new filename: `find "📖 Library" -name "*similar*"`
2. Update all links: `grep -rl "\[\[Old Name\]\]" "📖 Library" | xargs sed -i 's/\[\[Old Name\]\]/\[\[New Name\]\]/g'`

**If file doesn't exist:**
1. Check if it *should* exist (is it a core concept?)
2. **Yes:** Create stub entry with minimal content
3. **No:** Remove dead link or mark as "future reference"

**If typo:**
1. Identify correct spelling
2. Update all instances of typo

#### Step 5: Document in Audit Log

Record:
- Dead link name
- Files where it appeared
- Fix applied (renamed, created stub, removed)
- If "planned entry," note reason and expected creation date

### Link Verification Automation (Advanced)

**Create a bash script for future audits:**

```bash
#!/bin/bash
# link-check.sh - Verify all wikilinks in Library

echo "Extracting all wikilinks..."
grep -rh "\[\[.*\]\]" "📖 Library" --include="*.md" | \
  grep -o "\[\[[^]]*\]\]" | \
  sed 's/\[\[\(.*\)\]\]/\1/' | \
  sort | uniq > /tmp/links.txt

echo "Checking each link..."
while IFS= read -r link; do
  results=$(find "📖 Library" -name "*${link}*" -type f)
  if [ -z "$results" ]; then
    echo "❌ DEAD: [[${link}]]"
    grep -rn "\[\[${link}\]\]" "📖 Library" --include="*.md" | head -n 3
  fi
done < /tmp/links.txt

echo "Done."
```

**Usage during audit:**
```bash
bash link-check.sh > audit-dead-links.txt
```

---

## IV. Deprecation & Archival Standards

### When to Deprecate Content

Deprecate an entry when:
1. **Superseded by better synthesis:** Newer, more comprehensive entry covers same topic
2. **Outdated understanding:** Entry reflects earlier understanding now revised
3. **Redundant:** Duplicate content that should be merged elsewhere
4. **Out of scope:** Entry doesn't fit Library standards (e.g., personal notes, rough drafts)

**Do NOT deprecate:**
- Historical perspective that remains valid (even if not "current" approach)
- Partial entry that's accurate but incomplete (expand instead)
- Entry temporarily contradicting newer work (reconcile instead)

### Deprecation Process

#### Step 1: Create Deprecation Notice

Add to top of deprecated file:

```markdown
---
status: DEPRECATED
date_deprecated: YYYY-MM-DD
superseded_by: [[New Entry Name]]
reason: [Brief explanation]
---

> **⚠️ DEPRECATED:** This entry has been superseded by [[New Entry Name]].
> It remains for historical reference but is no longer maintained.
> **Deprecated:** YYYY-MM-DD
> **Reason:** [Brief explanation of why deprecated]

---

[Original content below...]
```

#### Step 2: Update YAML Frontmatter

```yaml
tags: [deprecated, archived, original-tags]
status: deprecated
date_deprecated: 2026-01-10
superseded_by: "[[New Entry]]"
```

#### Step 3: Move to Archive Directory

```bash
# Move deprecated entry to .archive/
git mv "📖 Library/System/Old Entry.md" ".archive/Library/System/Old Entry.md"
git commit -m "Deprecate: Old Entry (superseded by New Entry)"
```

**Directory structure:**
```
.archive/
└── Library/
    └── [Same structure as main Library]
```

#### Step 4: Update Inbound Links

Find all files linking to deprecated entry:

```bash
grep -rl "\[\[Old Entry\]\]" "📖 Library" --include="*.md"
```

**Options:**
1. **Update link to new entry:** `[[Old Entry]]` → `[[New Entry]]`
2. **Add deprecation note:** `[[Old Entry]] (deprecated; see [[New Entry]])`
3. **Remove link entirely** (if no longer relevant)

#### Step 5: Update Index Files

If entry appears in Index file:
- Mark as `🗄️ Archived` or remove from active list
- Add note: "Superseded by [[New Entry]]"

### Archival vs. Deletion

**Archive (preferred):**
- Content remains in git history
- Accessible for reference if needed
- Preserves intellectual journey

**Delete (rare):**
- Only for content that should never have existed (e.g., accidentally committed private data)
- Use `git rm` with caution

**Default policy:** Archive, don't delete. Disk space is cheap; lost insight is costly.

### Handling Conflicting Entries

If two entries cover same topic but conflict:

**Option 1: Merge**
- Combine both into comprehensive unified entry
- Note evolution of understanding in "Historical Context" section
- Archive the older entry

**Option 2: Reconcile**
- Create synthesis piece exploring the contradiction (see Cross-System Synthesis Protocol)
- Keep both entries, add cross-references explaining relationship

**Option 3: Clarify Scope**
- Rename entries to reflect distinct perspectives (e.g., "Saturn - Psychological" vs. "Saturn - Astronomical")
- Add intro noting relationship to other entry

---

## V. Quality Thresholds & Standards

### Minimum Entry Requirements (Tier 1)

Every Library entry must meet:
- [ ] **YAML frontmatter** with tags, system, date_created
- [ ] **Overview section** (2-3 paragraphs minimum)
- [ ] **Core content** (symbolism, mechanics, or archetypal layer)
- [ ] **Internal Links section** with 3+ wikilinks
- [ ] **500+ words** (excluding frontmatter)
- [ ] **Proper directory placement** (correct system/category folder)

**Entries below this threshold are "stubs"—flag for expansion during audit.**

### Quality Tiers (Reference)

**Tier 0 (Stub):**
- Placeholder entry, <500 words, marked TBD
- Missing key sections
- Purpose: Reserve filename, document that topic exists

**Tier 1 (Foundational):**
- Meets minimum requirements above
- Factual, accurate, but not comprehensive
- Suitable for quick reference

**Tier 2 (Developed):**
- 800-1200 words
- Includes Jungian/archetypal layer
- 5+ wikilinks, cross-system references
- Synthesis of multiple sources

**Tier 3 (Comprehensive):**
- 1500+ words
- Deep synthesis (Prima Materia + archetypal integration)
- Extensive cross-referencing (8+ wikilinks)
- Multiple perspectives (esoteric, psychological, practical)
- Example: Current Wands suit cards (500-line entries)

**Audit focuses on Tier 0 → Tier 1 conversion.** Higher tiers are aspirational; minimum is Tier 1.

### Red Flags During Audit

**Immediate attention required:**
- [ ] No YAML frontmatter
- [ ] File size <1KB (likely empty or near-empty)
- [ ] Zero wikilinks
- [ ] No "Internal Links" section
- [ ] Content is stream-of-consciousness notes (Scribe mode), not refined synthesis
- [ ] Contains personal/private info (should be in `👤 Biographical Information/`)
- [ ] File in wrong directory (e.g., synthesis in Library, Library in synthesis)

**Medium priority:**
- [ ] Entry <500 words but otherwise complete
- [ ] Only 1-2 wikilinks (under-connected)
- [ ] Missing archetypal layer (factual but not integrated)
- [ ] Tags don't follow taxonomy (no hashtags, inconsistent format)

**Low priority (enhancement opportunities):**
- [ ] Could be expanded from Tier 1 → Tier 2
- [ ] Good content but few cross-system references
- [ ] Accurate but dry (could benefit from Weaver voice)

---

## VI. Index File Maintenance

### Purpose of Index Files

Index files provide:
1. **At-a-glance navigation:** See all entries in one place
2. **Status tracking:** What's complete (✅), partial (🟡), planned (⚪), archived (🗄️)
3. **Completion metrics:** X/Y entries complete, Z% progress
4. **Search optimization:** All entries [[wikilinked]] for easy jumping

**Example:** `📖 Library/The Tarot/INDEX - Tarot Master List.md`

### Index File Structure (Standard Template)

```markdown
---
tags: [index, master-list, [system]]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
---

# [System Name] Master List

**Purpose:** Comprehensive index of all [System] entries in the Library.

**Status Legend:**
- ✅ **Complete** (Tier 3: Comprehensive, 1500+ words)
- 🟡 **Partial** (Tier 1-2: Functional but could expand)
- ⚪ **Planned** (Entry does not yet exist)
- 🗄️ **Archived** (Deprecated, moved to .archive/)

**Last Updated:** YYYY-MM-DD

---

## Completion Statistics

**Total Entries:** X
- ✅ Complete: Y (Z%)
- 🟡 Partial: A (B%)
- ⚪ Planned: C (D%)
- 🗄️ Archived: E

---

## [Category 1]

- ✅ [[Entry 1]] - Brief note
- 🟡 [[Entry 2]] - Brief note
- ⚪ Entry 3 (planned) - Brief note

## [Category 2]

[etc.]

---

## Cross-System References

*Notable entries from other systems that heavily reference [System]:*
- [[Entry from other system]] - Why relevant
```

### When to Update Index Files

**Always update index when:**
1. **New entry created:** Add to index with appropriate status marker (usually 🟡 or ✅)
2. **Entry expanded:** Change status (e.g., 🟡 → ✅ when Tier 1 becomes Tier 3)
3. **Entry deprecated:** Change status to 🗄️ or move to "Archived" section
4. **Entry renamed:** Update wikilink in index
5. **Quarterly audit:** Verify all entries listed, update statistics

**Commit index updates:**
- Ideally in same commit as entry change: `git add "Entry.md" "INDEX.md" && git commit -m "Expand Entry + update Index"`
- If batching changes: `git commit -m "Update [System] Index after [work description]"`

### Creating New Index Files

**When to create index for a system:**
- System has 10+ entries (enough content to warrant master list)
- User begins focused work on that system (e.g., starting Astrology expansion)
- During quarterly audit when absence of index hinders navigation

**Process:**
1. Use Index template above
2. List all existing entries with accurate status markers
3. Calculate completion statistics
4. Add to `◈ System/PROTOCOL - Search and Navigation.md` (Section 11.4)
5. Commit: `git commit -m "Create [System] Master Index (X entries tracked)"`

---

## VII. Integration with Other Protocols

### Relationship to Library Content Standard

**Library Content Standard (RUBRIC)** defines *what* a quality entry looks like.
**Library Maintenance Protocol (this document)** defines *how* to keep entries at that standard over time.

**Use together:**
- During audit, check entries against Rubric tiers
- When expanding stubs, follow Rubric guidelines
- Tag inconsistencies should align with Search & Navigation taxonomy (referenced in Rubric)

### Relationship to Search & Navigation Protocol

**Search & Navigation Protocol** defines *how to find* content.
**Library Maintenance Protocol** ensures *what's found is accurate and complete*.

**Overlap areas:**
- Tag taxonomy (maintenance ensures consistency, search relies on it)
- Index files (maintenance updates them, search uses them)
- [[Wikilinks]] (maintenance fixes dead links, search traverses them)

### Relationship to Cross-System Synthesis Protocol

**Cross-System Synthesis** creates *new integrated insights* from Library content.
**Library Maintenance** keeps *source material* from which synthesis draws.

**When synthesis supersedes Library entry:**
- Follow Deprecation standards (Section IV)
- Consider whether insights should graduate back to Library
- Update wikilinks to point to synthesis piece if appropriate

---

## VIII. Audit Log Template

Create new file for each audit: `◈ System/Audit Logs/YYYY-MM-DD - Q[X] Library Audit.md`

```markdown
---
tags: [audit, maintenance, library-quality]
date: YYYY-MM-DD
quarter: Q[X] YYYY
auditor: [Your entity_id or "System"]
---

# Q[X] YYYY Library Audit

**Date:** YYYY-MM-DD
**Duration:** [X hours]
**Library Size:** [X files]
**Changes Since Last Audit:** [Brief summary from git log]

---

## Summary Statistics

- **Total files audited:** X
- **Dead links found:** Y (Z fixed, A remaining)
- **Incomplete entries identified:** B (C high-priority, D medium, E low)
- **Outdated entries flagged:** F
- **Orphaned entries:** G
- **Tag inconsistencies:** H
- **Structural issues:** I

---

## Phase 1: Preparation

- [x] Created audit log file
- [x] Library size: [X] files
- [x] Reviewed commits since [date]: [brief summary]
- [x] Major additions: [list new systems/categories]

---

## Phase 2: Link Verification

### Dead Links Found

1. **[[Link Name 1]]**
   - Appears in: [file1.md:45, file2.md:89]
   - Cause: [renamed/moved/typo/planned]
   - Fix: [action taken or "deferred"]

2. [etc.]

### Planned Entry Links (Intentional Forward References)

1. **[[Future Entry]]**
   - Referenced by: [files]
   - Justification: [why link exists before entry]
   - Expected creation: [timeframe]

---

## Phase 3: Incomplete Entries

### High-Priority Stubs (Expand Soon)

1. **[[Entry 1]]** (📖 Library/System/Entry1.md)
   - Current size: [X words]
   - Missing: [sections/content]
   - Referenced by: [Y files]
   - Priority: High (core concept, heavily referenced)

### Medium-Priority Stubs

[etc.]

### Low-Priority Stubs

[etc.]

---

## Phase 4: Outdated Content

### Entries Flagged for Review

1. **[[Entry Name]]**
   - Reason: [superseded by/conflicts with/date-sensitive]
   - Related newer work: [[Synthesis Piece]]
   - Recommended action: [revise/deprecate/merge]

---

## Phase 5: Tag Consistency

### Files with Tag Issues

1. **Entry.md**
   - Issue: [no hashtags/wrong format/missing system tag]
   - Fix: [action taken]

### Batch Tag Updates Performed

- [Description of batch sed commands if used]

---

## Phase 6: Orphaned Content

### Entries with Zero Outbound Links

1. **[[Entry]]** - [reason] - [action: added links/flagged for expansion]

### Entries with Zero Inbound Links

1. **[[Entry]]** - [reason] - [action: added references from related entries]

---

## Phase 7: Index Maintenance

### Index Files Updated

1. **INDEX - [System] Master List.md**
   - Added: [new entries]
   - Updated status: [entries that changed tier]
   - Statistics: [before] → [after]

### Missing Index Files

- [ ] Astrology (planned, [Y] entries would be included)
- [ ] Human Design (planned, [Z] entries would be included)

---

## Phase 8: File Structure & Naming

### Issues Found

1. **File misplaced:** [Entry.md] should be in [correct directory]
   - Action: [moved/noted for future move]

2. **Naming inconsistency:** [Filename] doesn't match convention
   - Action: [renamed/flagged for review]

---

## Phase 9: Documentation & Reporting

### Action Items (Extracted for NEXT.md or Task List)

**Immediate (Complete This Session):**
- [ ] Fix dead link [[X]] in [files]
- [ ] Move misplaced file [Y]
- [ ] Update tags in [files]

**Short-Term (Next 1-2 Sessions):**
- [ ] Expand high-priority stub [[A]]
- [ ] Expand high-priority stub [[B]]
- [ ] Review flagged outdated entry [[C]]

**Long-Term (Quarterly Goals):**
- [ ] Create Astrology Master Index
- [ ] Expand all medium-priority stubs
- [ ] Reconcile conflicting entries [[D]] and [[E]]

---

## Next Audit Due

**Date:** [90 days from today]
**Anticipated Library Size:** [estimated based on current growth rate]
**Focus Areas for Next Audit:** [any specific concerns to monitor]

---

## Notes

[Any additional observations, patterns noticed, systemic issues to address in protocols]

---

## Commits Related to This Audit

[List git commits made during audit:]
- [commit hash] - [commit message]
- [commit hash] - [commit message]
```

---

## IX. Quarterly Audit Workflow Summary

**Complete checklist for each 90-day audit cycle:**

### Pre-Audit
- [ ] Check calendar: Is audit due? (90 days since last)
- [ ] Create audit log file from template
- [ ] Check Library size and recent git commits

### Audit Phases (2-4 hours)
- [ ] **Phase 1:** Preparation (5-10 min)
- [ ] **Phase 2:** Link verification (30-45 min)
- [ ] **Phase 3:** Incomplete entry identification (20-30 min)
- [ ] **Phase 4:** Outdated content review (15-30 min)
- [ ] **Phase 5:** Tag consistency check (20-30 min)
- [ ] **Phase 6:** Orphaned content detection (15-20 min)
- [ ] **Phase 7:** Index file maintenance (15-25 min)
- [ ] **Phase 8:** File structure & naming (10-15 min)
- [ ] **Phase 9:** Documentation & reporting (10-15 min)

### Post-Audit
- [ ] Complete audit log with all findings
- [ ] Extract action items (immediate/short-term/long-term)
- [ ] Update NEXT.md with immediate priorities if needed
- [ ] Commit audit log to git
- [ ] Update Audit Tracker with next due date
- [ ] Address immediate fixes (dead links, critical errors)

**Total estimated time: 2-4 hours depending on Library size and issues found.**

---

## X. Maintenance Between Audits

### Ongoing Practices (No Formal Schedule)

**When creating new Library entries:**
- [ ] Follow Library Content Standard (minimum Tier 1)
- [ ] Use correct tag taxonomy (hashtags, lowercase, hyphens)
- [ ] Include Internal Links section with 3+ wikilinks
- [ ] Update relevant Index file in same commit

**When editing existing entries:**
- [ ] If expanding significantly, update Index status marker (🟡 → ✅)
- [ ] If referencing new entries, ensure wikilinks are correct
- [ ] If deprecating, follow Deprecation standards (Section IV)

**When you notice issues:**
- [ ] Dead link encountered? Fix immediately (don't wait for audit)
- [ ] Tag inconsistency? Correct in same session
- [ ] Misplaced file? Move with `git mv` to preserve history

**Git commit messages:**
- Clear, specific messages help future audits
- Good: "Expand Saturn entry from 500→1200 words, add Jungian layer"
- Bad: "Update file"

---

## XI. Future Enhancements

**Potential automation (not currently implemented):**

1. **Link checker script:** Automated bash script to extract and verify all wikilinks (prototype in Section III)
2. **Tag validator:** Script to check tag format consistency
3. **Stub finder:** Automated identification of <500 word entries
4. **Index generator:** Script to auto-generate index files from directory contents
5. **Orphan detector:** Automated inbound/outbound link analysis

**When Library scales to 500+ entries, consider implementing automation to reduce manual audit time.**

**For now: Manual process with documented checklists ensures thoroughness and prevents premature optimization.**

---

## XII. Integration with CLAUDE.md

**Session Start Protocol (Section 1):**
- Check `git status` and `git log` (already in protocol)
- Check Process Gaps tracker (already in protocol)
- **Add:** Check if quarterly Library audit is due (calculate days since last audit)

**If audit due, prompt user:**
*"I notice it's been [X] days since the last Library audit (Q[X] YYYY on [date]). The quarterly audit is due. Would you like to:*
- *Run the quarterly Library audit now? (2-4 hours)*
- *Schedule it for later this session?*
- *Defer to next session?"*

**Library Maintenance Cycles Process Gap:**
- Update Process Gaps tracker to mark Gap #4 as 🟢 Complete
- Add completion date and commit reference
- Note impact: "Library quality preservation ensured through systematic quarterly audits"

---

## XIII. Summary & Quick Reference

**Purpose:** Preserve Library integrity as it scales through systematic quarterly audits.

**Frequency:** Every 90 days

**Duration:** 2-4 hours per audit

**Core Tasks:**
1. Link verification (fix dead wikilinks)
2. Incomplete entry identification (find and prioritize stubs)
3. Outdated content review (flag superseded entries)
4. Tag consistency (ensure taxonomy compliance)
5. Orphan detection (connect isolated entries)
6. Index maintenance (keep master lists current)
7. File structure audit (naming, placement)
8. Documentation (audit log, action items)

**Key Standards:**
- **Minimum quality:** Tier 1 (500+ words, 3+ wikilinks, proper YAML)
- **Deprecation:** Mark superseded entries, move to `.archive/`
- **Tags:** Hashtag format, lowercase, hyphens, system + category required
- **Links:** All wikilinks must resolve (or be documented as planned entries)

**Integration:**
- **Library Content Standard:** Defines quality tiers
- **Search & Navigation:** Relies on tag consistency and wikilinks
- **Cross-System Synthesis:** May supersede outdated Library entries

**Audit Log Template:** `◈ System/Audit Logs/YYYY-MM-DD - Q[X] Library Audit.md`

**Next Audit Due:** [Track in audit logs or NEXT.md]

---

*"The library that is not maintained becomes a labyrinth. The labyrinth that is mapped becomes a library once more."*
