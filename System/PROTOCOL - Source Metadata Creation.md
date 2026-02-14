# PROTOCOL: Source Metadata Creation

**Purpose:** Efficient creation of comprehensive Source Metadata YAML files for books in The Athenaeum
**Version:** 1.0
**Date:** 2026-02-14
**Context:** The Ephemeris synthesis system

---

## Overview

Source Metadata files index books in The Athenaeum for efficient synthesis work and citation lookup. This protocol defines the **parallel agentic workflow** for indexing large source texts (200+ pages) without context window bloat.

**Key Principle:** Create skeleton in main session, delegate chapter indexing to parallel agents, then merge results.

---

## When to Use This Protocol

**Use parallel agentic workflow for:**
- Books **200+ pages** with multiple chapters
- Technical texts with dense content requiring detailed topic extraction
- Any source requiring comprehensive indexing across many sections

**Use manual/single-session workflow for:**
- Books <200 pages with simple structure
- Sources already partially indexed (completing stubs)
- Single-chapter or article-length sources

---

## Prerequisites

**Required:**
1. PDF file in `~/VibologyOS/The Athenaeum/[Pillar]/`
2. Template: `System/Templates/TEMPLATE - Source Metadata.yml`
3. Target location: `~/VibologyOS/The Ephemeris/Source Metadata/`
4. Naming convention: `[Author-ShortTitle].yml` (e.g., `Greene-Neptune.yml`)

**Verify:**
- PDF is OCR'd and searchable (check `ocr_quality` field in metadata)
- PDF page numbers match internal pagination
- You have book's full bibliographic data (title, author, publisher, year, edition)

---

## Phase 1: Reconnaissance (Main Session)

**Objective:** Understand book structure before indexing begins.

### Step 1: Read Table of Contents
```
Read PDF pages 1-10 (or wherever TOC is located)
```

Extract:
- Total page count
- Part/section structure
- Chapter titles and approximate page ranges
- Special sections (foreword, appendices, bibliography, index)
- Chart/figure lists if applicable

### Step 2: Verify Actual Chapter Breaks

**CRITICAL:** TOC page ranges are often estimates. Verify actual chapter headings in PDF.

```
Read PDF at suspected chapter transitions (e.g., pages 100-110, 135-145)
Look for actual chapter title pages
Record confirmed page ranges
```

**Common issue:** TOC may show "Chapter 2: pages 105-139" but Chapter 2 actually ends at page 104 and Chapter 3 starts at 105.

### Step 3: Index Front Matter (Main Session)

Read and index:
- Introduction (if substantial)
- Foreword/Preface (if relevant to synthesis)
- Author's methodology notes

**Why main session:** Front matter sets context for entire work; keep in primary context.

---

## Phase 2: Skeleton Creation (Main Session)

### Step 1: Copy Template

```bash
cp "System/Templates/TEMPLATE - Source Metadata.yml" \
   "The Ephemeris/Source Metadata/[Author-ShortTitle].yml"
```

### Step 2: Fill Basic Metadata

```yaml
source_id: "[Author-ShortTitle]"
full_title: "[Complete Book Title]"
author: "[Author Name]"
publisher: "[Publisher]"
year: YYYY
edition: "[Edition info]"
pages: XXX
path: "~/VibologyOS/The Athenaeum/[Pillar]/[Filename].pdf"
```

### Step 3: Create Chapter Skeleton

For each chapter, create entry with **verified page ranges**:

```yaml
chapters:
  - number: 1
    title: "[Chapter Title from TOC]"
    part: "[Part name if book has parts]"
    pages: "[verified-start]-[verified-end or TBD]"
    topics:
      - "[Placeholder - will be filled by agent]"
```

**Note:** Leave topics and key_sections as placeholders for agent work.

---

## Phase 3: Parallel Indexing (Agentic)

### Step 1: Determine Batch Size

**Recommended:** Launch 3-4 agents at a time for monitoring ease.

**Considerations:**
- Token budget remaining
- Chapter complexity (dense chapters may take longer)
- Your available attention for reviewing results

### Step 2: Launch Agent Batch

**Template for each agent:**

```
Task tool:
- subagent_type: general-purpose
- description: "Index [Source-ShortTitle] Chapter [N]"
- prompt: |
    Read pages [START]-[END] of `[FULL_PATH_TO_PDF]` and create comprehensive
    chapter metadata for Chapter [N]: "[Chapter Title]".

    Create this structure:

    ```yaml
    - number: [N]
      title: "[Chapter Title]"
      part: "[Part name if applicable]"
      pages: "[START]-[END]"
      topics:
        - "[Comprehensive list of all topics covered]"
        - "[Include: specific names, concepts, case studies]"
        - "[Be specific and thorough - aim for 30-50+ topics for dense chapters]"
      key_sections:
        - section: "[Section name]"
          pages: "[page range]"
          summary: "[What this section covers - 2-3 sentences]"
    ```

    Focus on:
    - [Specific guidance for this chapter's content type]
    - [E.g., "Mythology and deity names", "Case studies", "Technical concepts"]
    - [E.g., "Psychological theories", "Historical figures", "Astrological placements"]

    Return ONLY the YAML chapter entry, nothing else.
```

**CRITICAL PDF Reading Limits:**
- Maximum 20 pages per Read tool call
- Agents will automatically paginate if needed
- Provide page ranges that respect this limit or let agent handle pagination

### Step 3: Launch in Parallel

**Example for batch of 3:**

Send single message with three Task tool calls (one per chapter).

```
I'm launching agents for Chapters [N], [N+1], [N+2]...
[Agent 1 task]
[Agent 2 task]
[Agent 3 task]
```

### Step 4: Monitor Completion

Agents will return YAML results when complete. Typical timing:
- Simple chapter (20-30 pages): ~45-60 seconds
- Dense chapter (30-40 pages): ~60-90 seconds

**Note agent IDs** for potential resumption if needed.

---

## Phase 4: Assembly (Main Session)

### Step 1: Verify Agent Results

For each returned YAML chapter entry:

**Check:**
- ✅ Page range is correct
- ✅ Topics list is comprehensive (30+ for dense chapters)
- ✅ Key sections are identified with summaries
- ✅ YAML syntax is valid (proper indentation, no syntax errors)

**If issues found:** Re-launch agent with clarified instructions.

### Step 2: Merge Chapters into Metadata File

Use Edit tool to replace skeleton chapter entries with full agent results.

**Best practice:** Merge in batches (3-4 chapters at a time) rather than all at once.

```yaml
# Replace this skeleton:
  - number: 2
    title: "Chapter Title"
    pages: "XX-XX"
    topics:
      - "[Placeholder]"

# With agent's full result:
  - number: 2
    title: "Chapter Title"
    pages: "75-103"
    topics:
      - "Topic 1 with specific details"
      - "Topic 2 with names and concepts"
      [... 30-50+ topics]
    key_sections:
      - section: "Section Name"
        pages: "75-82"
        summary: "Detailed summary..."
```

### Step 3: Update Metadata

After merging each batch, update the `metadata` section:

```yaml
metadata:
  indexed_by: "Claude (Sonnet 4.5)"
  indexed_date: "YYYY-MM-DD"
  last_updated: "YYYY-MM-DD"
  ocr_quality: "[Excellent/Good/Fair]"
  notes: "[Current completion status]"
  indexing_status: "In progress - Chapters 1-[N] complete, Chapters [N+1]-[END] pending"
```

**When fully complete:**
```yaml
  indexing_status: "Complete - all chapters indexed"
```

---

## Phase 5: Completion

### Step 1: Fill Topic Index

Cross-reference major themes across chapters:

```yaml
topic_index:
  "[Major Topic 1]":
    chapters: [1, 3, 5]
    key_pages: "XX-XX, XX-XX"
    summary: "[Where this topic appears and how it's treated]"
```

**Tip:** Use Grep to search PDF for recurring themes to identify cross-chapter topics.

### Step 2: Complete Cross-Reference Points

Fill in the cross_reference_value section with page ranges for synthesis use:

```yaml
cross_reference_value:
  mythology: "pages [X-X]"
  psychological_interpretation: "pages [X-X]"
  practical_application: "pages [X-X]"
  case_studies: "pages [X-X]"
```

### Step 3: Write Synthesis Notes

In the `synthesis_notes` field, provide:
- Unique contribution of this source
- Methodology/perspective
- Best use cases for synthesis
- Strengths and limitations
- Relationship to other Athenaeum sources

**Length:** 200-400 words, structured with headers.

### Step 4: Final Verification

```bash
# Check YAML syntax
python3 -c "import yaml; yaml.safe_load(open('The Ephemeris/Source Metadata/[filename].yml'))"

# Check file size (should be 12-20K for comprehensive metadata)
ls -lh "The Ephemeris/Source Metadata/[filename].yml"
```

**Expected size:** 12-20K for 400-600 page book with comprehensive indexing.

### Step 5: Commit

```bash
git add "The Ephemeris/Source Metadata/[filename].yml"
git commit -m "Complete source metadata: [Author] - [Short Title]

- [N] chapters fully indexed via parallel agentic workflow
- Comprehensive topic extraction ([total topics])
- Cross-reference points and synthesis notes complete"
```

---

## Best Practices

### Agent Instructions

**DO:**
- ✅ Request YAML-only output (no preamble or explanation)
- ✅ Specify "comprehensive" and "specific" for topic extraction
- ✅ Give context-specific guidance (mythology vs. psychology vs. technical)
- ✅ Request 2-3 sentence summaries for key_sections
- ✅ Include examples of desired specificity in prompt

**DON'T:**
- ❌ Ask agents to "summarize" (too vague)
- ❌ Request interpretation or synthesis (just extraction)
- ❌ Assign page ranges exceeding PDF read limits without noting agent can paginate
- ❌ Launch all chapters at once if book has 10+ chapters (batch instead)

### Topic Extraction Quality

**Good topics** are specific and synthesis-ready:
- ✅ "Case study: Meher Baba (Sun square Neptune, Pisces mysticism)"
- ✅ "Orphic cosmogony (Phanes-Dionysus, Time/Aion, cosmic egg)"
- ✅ "Charcot versus Bernheim debate on le grand hypnotisme"

**Weak topics** are vague and require re-reading source:
- ❌ "Case studies presented"
- ❌ "Mythology discussed"
- ❌ "Historical debates"

**Target:** 30-50+ topics per dense chapter, 15-25 for lighter chapters.

### Parallel Execution

**Optimize for:**
- 3-4 agents at a time for active monitoring
- Sequential batches if total chapters >12
- Token budget awareness (check periodically)

**Example for 13-chapter book:**
- Batch 1: Chapters 2-4 (Chapter 1 in main session)
- Batch 2: Chapters 5-7
- Batch 3: Chapters 8-10
- Batch 4: Chapters 11-13

---

## Troubleshooting

### Issue: Agent returns incomplete topics list

**Solution:** Re-launch with explicit instruction:
```
"Aim for 40-50+ comprehensive topics. Be exhaustive, not selective."
```

### Issue: Page ranges don't match between agents

**Cause:** Didn't verify actual chapter breaks from PDF.

**Solution:** Read PDF at transition points, confirm headings, update skeleton before launching agents.

### Issue: YAML syntax errors in agent output

**Solution:** Copy agent output, fix indentation manually, then merge. Note pattern for future agent prompts.

### Issue: Agent says "pages XX-XX exceed 20-page limit"

**Solution:** Agent can handle this with pagination. Add to prompt:
```
"Note: You may need to read this chapter in multiple 20-page segments."
```

### Issue: Topics are too general/vague

**Solution:** Provide example topics in prompt:
```
Example of specificity desired:
- "Mithraic tauroctony and symbolic castration of phallic dimension"
NOT: "Mithras discussed"
```

---

## Template Agent Prompt

**Copy and customize for each chapter:**

```
Read pages [START]-[END] of `/Users/joe/VibologyOS/The Athenaeum/[Pillar]/[Filename].pdf`
and create comprehensive chapter metadata for Chapter [N]: "[Chapter Title]".

[If book has parts:] This is Part [N]: [Part Title].

Create this structure:

```yaml
- number: [N]
  title: "[Chapter Title]"
  part: "[Part Title if applicable]"
  pages: "[START]-[END or confirmed end page]"
  topics:
    - "[Comprehensive list - aim for 40-50+ specific topics]"
    - "[Include: proper names, case studies, technical terms, cultural references]"
    - "[Be specific: not 'myths discussed' but 'Orphic cosmogony (Phanes-Dionysus, cosmic egg)']"
  key_sections:
    - section: "[Section name from PDF if visible, or descriptive name]"
      pages: "[page range]"
      summary: "[2-3 sentence summary of what this section covers]"
```

Focus on:
- [Content type: mythology/psychology/technical/etc.]
- [Specific names to capture: deities/people/places/concepts]
- [Case studies or examples if present]
- [Special features: charts, diagrams, extensive footnotes, etc.]

Return ONLY the YAML chapter entry, nothing else.
```

---

## Success Criteria

**A well-indexed source metadata file has:**

- ✅ All chapters comprehensively indexed (30-50+ topics for dense material)
- ✅ Accurate page ranges verified from actual PDF headings
- ✅ Key sections identified with meaningful summaries
- ✅ Topic index cross-referencing major themes
- ✅ Synthesis notes providing context and best-use guidance
- ✅ Valid YAML syntax (python yaml.safe_load passes)
- ✅ 12-20K file size (for 400-600 page source)
- ✅ Committed to git with descriptive message

**Time investment:**
- Phase 1-2 (Reconnaissance + Skeleton): 30-45 minutes
- Phase 3 (Parallel Indexing): 5-10 minutes per batch of 3-4 chapters
- Phase 4-5 (Assembly + Completion): 20-30 minutes
- **Total:** ~2-3 hours for 400-600 page book (vs. 8-12 hours manual)

---

## Related Documents

- `System/Templates/TEMPLATE - Source Metadata.yml` - Base template
- `PROTOCOL - Prima Materia Verification.md` - Source verification before indexing
- `GUIDE - Synthesis Quick Start.md` - Using completed metadata for synthesis work

---

**Version History:**
- 1.0 (2026-02-14): Initial protocol based on Greene-Neptune parallel agentic workflow validation
