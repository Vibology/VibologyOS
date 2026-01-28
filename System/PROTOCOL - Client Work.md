---
tags: [system, protocol, client-work, privacy, synthesis]
date_created: 2026-01-19
date_updated: 2026-01-28
status: Active
---

# Protocol: Client Work

This protocol standardizes the workflow for client synthesis work, ensuring consistency, data integrity, and appropriate privacy handling across all client engagements.

## Core Principles

1. **Data Integrity First** - No synthesis begins until chart data is calculated and verified
2. **Privacy by Design** - Client information is protected at every stage
3. **Traceable Claims** - Every statement in a reading must be sourced from calculated data
4. **Practical Application** - Readings provide actionable guidance, not abstract speculation

---

## Phase 0: Client Intake

### 0.1 Birth Data Collection

**Required information:**

| Field | Example | Notes |
|-------|---------|-------|
| Full Name | "Szilvia Williams" | For folder naming and greeting only |
| Birth Date | 1976-05-17 | Year, Month, Day |
| Birth Time | 04:04 | Local time at birth location |
| Birth Location | "Kaposvár, Hungary" | City, Country (or precise coordinates) |
| Time Precision | Exact / Approximate / Unknown | Affects what can be calculated |

**Time Precision Levels:**

- **Exact** - Birth certificate or hospital records
- **Approximate** - Parent memory, "early morning," etc. (±15-60 min uncertainty)
- **Rectified** - Time adjusted based on life events (note rectification source)
- **Unknown** - No birth time available (limits HD and house calculations)

**Use Template:** `◈ System/Templates/_TEMPLATE - Client Intake Form.md`

### 0.2 Question Documentation

Document the client's questions clearly before beginning synthesis:

1. **Primary Question** - The main focus of the reading
2. **Secondary Questions** - Additional areas of inquiry
3. **Context** - Relevant life circumstances, recent events, specific concerns

**Question Types and Implications:**

| Question Type | Data Required | Protocol Triggered |
|---------------|---------------|-------------------|
| Natal analysis only | Astrology + HD natal | Standard |
| Timing questions | + Transits | Calculate transits MANDATORY |
| Career/relationship | + Relevant houses | Extended analysis |
| Life transition | + Transits + Profile timing | Full transit workup |

### 0.3 Entity ID Assignment

Assign a two-letter Entity ID for all internal documentation:

**Format:** First initial + Last initial (e.g., "SW" for Szilvia Williams)

**Collision handling:** If Entity ID already exists, append number (SW2, SW3)

**Usage:** YAML frontmatter, git commit messages, internal notes

### 0.4 Privacy Acknowledgment

Before proceeding, confirm:

- [ ] Client understands readings are for personal insight, not professional advice
- [ ] Client consents to data storage for synthesis purposes
- [ ] Retention preferences documented (if client requests deletion timeline)

---

## Phase 1: Data Acquisition

**CRITICAL:** This phase MUST be completed before any synthesis work begins.

### 1.1 Reference Existing Protocol

Follow `PROTOCOL - Chart Data Acquisition.md` completely:

1. **Geolocation Verification** - `verify_geolocation.py`
2. **Astrology Natal Chart** - `get_astro_data.py`
3. **Human Design Chart Data** - `get_hd_data.py`
4. **Human Design Bodygraph Visualization** - Generate `bodygraph.svg`
5. **Transits** (if timing questions) - `get_transit_data.py`

### 1.2 Quality Gate

**DO NOT proceed to Phase 2 until:**

- [ ] Geolocation verified with timezone and DST status
- [ ] astrology.json generated and spot-checked
- [ ] humandesign.json generated and spot-checked
- [ ] bodygraph.svg generated (scalable vector graphic)
- [ ] transits.json generated (if timing questions exist)
- [ ] User verification completed for any unusual data

**If birth time is unknown:**
- Flag synthesis as "time-sensitive data unavailable"
- Proceed with Sun, outer planets, general HD patterns
- Do NOT calculate houses, ascendant, or detailed HD gates

### 1.3 External Reference Integration

If client provides external chart PDFs or reports:

- Store in client folder as reference
- Cross-check against calculated data for discrepancies
- Prefer calculated data over external sources (unless rectification documented)

---

## Phase 2: Synthesis Work

Client synthesis work falls into two categories: **Initial Reports** (foundational portraits for new clients) and **Targeted Readings** (question-specific synthesis for ongoing work).

### 2.1 Initial Client Report (New Clients)

The Initial Client Report is the foundational document for new client work. It establishes a comprehensive archetypal portrait before addressing specific questions.

**Purpose:** Map the client's core patterns across:
- **Astrology** — Luminaries, planetary positions, angles, major aspects
- **Human Design** — Type, Authority, Profile, Definition, Incarnation Cross, key gates/channels
- **Personal Mythos** — Resonant archetypes, mythological parallels, developmental stage

**When to Use:** First engagement with a new client, OR when a returning client requests a comprehensive overview rather than targeted synthesis.

**Template:** `System/Templates/_TEMPLATE - Initial Client Report.md`

**Sections:**
```
I.    The Invitation (framing)
II.   Data Foundation (Scribe voice - raw mechanics)
III.  The Solar Story (Sun/Conscious HD)
IV.   The Lunar Landscape (Moon/Emotional architecture)
V.    The Persona and Path (Ascendant/Profile)
VI.   The Incarnation Cross (Life purpose)
VII.  Archetypal Resonance (Personal Mythos integration)
VIII. Shadow Cartography (Growth edges)
IX.   Practical Wisdom (Strategy, timing, integration)
X.    The Open Question (What remains unknown)
```

### 2.2 Targeted Readings (Specific Questions)

For clients with specific questions—life transitions, decisions, timing, relationship dynamics—use a focused synthesis structure.

**Template:** `Synthesis/General/_TEMPLATE - Cross-System Synthesis.md`

**Sections:**
```
I.   Header & Greeting
II.  Introduction & Reading Overview
III. Core Design Analysis
     - Astrological Architecture
     - Human Design Mechanics
IV.  Question-Specific Analysis
     - Primary Question Deep Dive
     - Secondary Questions
V.   Cross-System Synthesis
     - Convergence Points
     - Practical Guidance
VI.  Closing & Next Steps
```

### 2.3 Word Count Guidance

| Reading Type | Target Length |
|--------------|---------------|
| Initial Report (comprehensive) | 6,000-10,000 words |
| Standard (natal + questions) | 4,000-6,000 words |
| Focused (1 question) | 1,500-3,000 words |

**Quality over quantity.** A focused 2,000-word reading that addresses the question clearly is better than an 8,000-word dump of generic information.

### 2.4 Voice & Quality Standards

**Voice:** The Weaver persona (scholarly, evocative, numinous)

**Required qualities:**

- [ ] Traceable claims - Every planetary position, transit date, HD mechanic cites source data
- [ ] Practical application - Not just "what is" but "so what" and "now what"
- [ ] Shadow acknowledgment - Honest about challenging patterns, not just positive spin
- [ ] Question-centered - Returns to client's actual questions throughout
- [ ] Jargon balanced - Define esoteric terms, don't assume knowledge

**Prohibited:**

- Vague timing ("soon," "in the coming years") without calculated dates
- Claims not traceable to natal/transit data
- Generic descriptions that could apply to anyone
- Prescriptive life advice (legal/medical/financial)
- AI clichés, filler, or conversational padding

### 2.5 Cross-System Integration

When synthesizing across systems:

- Reference `PROTOCOL - Cross-System Synthesis.md` methodology
- Identify convergence points (where systems agree)
- Note divergence points (where systems offer different perspectives)
- Articulate the "Third Meaning" that emerges from integration

### 2.6 Verification During Synthesis

**While writing:**

- Keep `astrology.json`, `humandesign.json`, and `transits.json` open for reference
- Copy-paste exact positions rather than typing from memory
- Use the Verification Checklist template for complex readings

---

## Phase 3: Delivery

### 3.1 Final Markdown Review

Before delivery, verify:

**Content Checklist:**

- [ ] All sections from reading template present
- [ ] Client's questions explicitly addressed
- [ ] Timing claims verified against transits.json
- [ ] No placeholder text remaining ("[INSERT]", "TBD", etc.)
- [ ] [[Wikilinks]] resolve to actual Library entries or are removed

**Privacy Checklist:**

- [ ] Full name appears ONLY in greeting/header section
- [ ] Entity ID used in YAML frontmatter
- [ ] No identifying details in tags
- [ ] File ready for storage (no exposed sensitive context)

**Quality Checklist:**

- [ ] Read through once for flow and coherence
- [ ] Check for contradictions within the reading
- [ ] Verify Weaver voice maintained throughout
- [ ] Confirm practical guidance included

### 3.2 File Naming for Deliverable

**Working file:** `Synthesis.md` (in dated subfolder)
**Final file:** `Synthesis_Final.md` (reviewed and ready for delivery)

**Naming convention:**
```
[Client Name] - [Reading Type] - [Date].md
Example: Szilvia Williams - Natal and Career Reading - 2026-01-16.md
```

### 3.3 PDF Conversion

**User handles PDF conversion manually.**

Rationale: PDF design involves aesthetic choices (fonts, layout, colors, graphics) that require human creative control. Markdown is the deliverable from synthesis work; user converts to PDF with preferred design tools.

**Recommended workflow:**
1. Export markdown from Obsidian (or copy to design tool)
2. Apply consistent formatting and design template
3. Review PDF layout and page breaks
4. Save as PDF for client delivery

---

## Phase 4: Archival

### 4.1 File Organization Standard

```
~/Business/Consultations/[Full Name]/
├── astrology.json           (permanent - natal chart data)
├── humandesign.json         (permanent - HD chart data)
├── bodygraph.svg            (permanent - HD visualization, SVG format)
├── natal_chart.svg          (permanent - astrology visualization, if generated)
├── [Reference PDFs]         (permanent - external charts)
└── YYYY-MM-DD_[Reading]/
    ├── location_verification.json
    ├── transits.json
    ├── Verification_Checklist.md
    ├── Synthesis.md         (working draft)
    └── Synthesis_Final.md   (deliverable)
```

**Rationale:**

- **Natal data and visualizations at root** - `astrology.json`, `humandesign.json`, and `bodygraph.svg` are permanent; they apply to all future readings for this client
- **SVG format for visualizations** - Scalable vector graphics ensure quality at any size, clean import into Pages/design tools, professional print quality
- **Transit data in subfolder** - Transits are specific to the questions and date range of each synthesis
- **Each reading gets dated subfolder** - Allows multiple readings over time with clear versioning

### 4.2 Git Commit Protocol

**After completing a client reading:**

```bash
git add "~/Business/Consultations/[Client Name]/"
git commit -m "Complete [SW] synthesis: [brief description]

- Systems: Astrology + Human Design [+ transits if applicable]
- Focus: [Primary question topic]
- Deliverable ready for PDF conversion

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

**Privacy note:** Use Entity ID in commit messages, not full name in description body.

### 4.3 Post-Delivery Corrections

If errors are discovered after delivery:

1. **Create correction log** in reading subfolder (`Correction_Log.md`)
2. **Document what was wrong** - Specific error and source
3. **Re-calculate if needed** - Run scripts again if data error
4. **Create corrected synthesis** - New `Synthesis_Corrected.md` file
5. **Do NOT delete original** - Archive with `superseded_by:` metadata
6. **Notify client** - If error materially affects interpretation

### 4.4 Data Retention & Deletion

**Default retention:** Indefinite (for continuity of future readings)

**Client-requested deletion:**

1. Confirm deletion request in writing
2. Remove client folder from `~/Business/Consultations/`
3. Remove from git history (if required): `git filter-branch` or BFG
4. Confirm deletion to client
5. Log deletion date (without client details) in audit log

**GDPR compliance:** Deletion requests honored within 30 days

---

## Privacy Protocol

### Tier 1: Full Name (Limited Use)

**Where Full Name Appears:**
- Consultation folder name (`~/Business/Consultations/Szilvia Williams/`)
- PDF greeting/header ("Dear Szilvia,")
- Direct client communication

**Where Full Name NEVER Appears:**
- YAML frontmatter tags
- Git commit message body
- Library or Synthesis cross-references
- Any file that might be shared or published

### Tier 2: Entity ID (Internal Documentation)

**Where Entity ID Appears:**
- YAML frontmatter: `entity_id: SW`
- Git commit messages: "Complete [SW] synthesis"
- Internal notes and working documents
- Cross-reference links if needed

**Format:** Two-letter initials (SW, JL, etc.)

### Tier 3: Anonymous (Teaching/Publication)

**When to use:**
- Anonymized case studies for teaching
- Published synthesis examples
- Universal archetypal demonstrations

**How to anonymize:**
- Remove all identifying details (name, location, specific dates)
- Change identifying birth data if example is published
- Use generic descriptors ("a Generator with emotional authority")
- Focus on archetypal patterns, not biographical specifics

---

## Integration with Other Protocols

### Chart Data Acquisition Protocol

**Relationship:** Client Work Protocol calls Chart Data Acquisition in Phase 1

**Sequence:**
1. Client intake (this protocol)
2. Data acquisition (Chart Data Acquisition Protocol)
3. Synthesis work (this protocol continues)

### Cross-System Synthesis Protocol

**Relationship:** Client readings ARE cross-system synthesis applied to a specific person

**When to reference:**
- Phase 2 synthesis methodology
- Convergence/divergence analysis
- Quality standards for integration

### Library Maintenance Protocol

**Relationship:** Client work may reveal gaps in Library that need addressing

**Action:** If synthesis reveals missing Library entry needed for proper cross-reference:
1. Note in reading (can link to planned entry)
2. Add to NEXT.md or Library expansion queue
3. Create entry when time permits
4. Update reading with proper link

---

## Quick Reference

### New Client Checklist

```
□ Collect birth data (date, time, location, precision)
□ Document questions (primary, secondary, context)
□ Assign Entity ID
□ Create folder: ~/Business/Consultations/[Full Name]/
□ Run geolocation verification
□ Calculate astrology.json
□ Calculate humandesign.json
□ Generate bodygraph.svg (SVG format)
□ Calculate transits.json (if timing questions)
□ Verify data quality
□ Begin synthesis
```

### Reading Section Template

```
I.   Header (Full name greeting)
II.  Introduction (Reading overview, systems used, questions addressed)
III. Core Design (Astrology architecture + HD mechanics)
IV.  Question Analysis (Specific to client's inquiries)
V.   Synthesis (Cross-system integration, Third Meaning)
VI.  Closing (Practical guidance, next steps)
```

### Privacy Quick Check

```
□ Full name only in folder name and greeting
□ Entity ID in YAML frontmatter
□ No identifying info in tags
□ Git commit uses Entity ID
```

---

## Version History

- **2026-01-28:** Added bodygraph.svg generation to Phase 1 workflow. Updated Quality Gate, File Organization, and New Client Checklist to include SVG visualization as standard deliverable format.
- **2026-01-27:** Added Initial Client Report template (`_TEMPLATE - Initial Client Report.md`) as comprehensive archetypal portrait for new clients. Restructured Phase 2 to distinguish between Initial Reports and Targeted Readings. Updated Consultations folder references to `~/Business/Consultations/`.
- **2026-01-19:** Initial protocol created. Formalizes workflow from Szilvia Williams and Joe Lewis synthesis work. Addresses Process Gap #5.

---

*"The work of synthesis is a sacred trust. Handle client material with the same care you would bring to your own soul work."*
