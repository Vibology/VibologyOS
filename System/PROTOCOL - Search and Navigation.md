---
tags: [system, protocol, search, navigation, taxonomy]
date_created: 2026-01-10
date_updated: 2026-01-19
version: 1.1
status: Active
---

# Search and Navigation Protocol

## Purpose

As the Library grows, efficient search and navigation becomes critical. This protocol defines:

1. **Tag taxonomy** - Standardized tagging conventions across all systems
2. **Search protocols** - How to find content efficiently using available tools
3. **Index system** - Master lists providing at-a-glance navigation
4. **Cross-reference mapping** - How to traverse connections between systems

**Goal:** Make knowledge accessible—what exists can be found, what's connected can be traversed.

---

## I. Current State Assessment

**Current Library Statistics:** See `📖 Library/📖 Library Status.md` for up-to-date entry counts.

### Library Overview (as of 2026-01-19)

**Total Files:** 446 markdown entries (all 7 pillars complete)
**Cross-Reference Density:** 97%+ of files contain [[wikilinks]]
**Systems Represented:** 7 pillars (Angelology, Astrology, Personal Mythos, Human Design, The Magdalene Path, The Tarot, The Window)

**System Breakdown:**
- **Human Design:** 140 files (Types, Centers, Profiles, Authorities, 64 Gates, 36 Channels, Variables)
- **Tarot:** 79 files (22 Major Arcana + 56 Minor Arcana + Overview)
- **Personal Mythos:** 75 files (Jungian Archetypes, Hero's Journey, World Mythology, Fairy Tales)
- **The Window:** 72 files (Twelve Archetypes, Ten Portals, Six Houses)
- **Astrology:** 37 files (Planets, Signs, Houses, Aspects)
- **Angelology:** 31 files (Nine Orders, Ten Archangels, Enochian System)
- **The Magdalene Path:** 8 files (Core practices and framework)
- **Core Foundations:** 5 files (Paradigm documents)

**Directory Structure:**
```
📖 Library/
├── Angelology/
├── Astrology/
│   ├── Planets/
│   ├── Signs/
│   ├── Houses/
│   └── Aspects/
├── Core Foundations/
├── Personal Mythos/
│   └── Jungian Archetypes/
├── Human Design/
│   ├── Types/
│   ├── Centers/
│   ├── Channels/
│   ├── Gates/
│   ├── Profiles/
│   ├── Strategy and Authority/
│   └── Substructure/
├── The Magdalene Path/
├── The Tarot/
│   ├── Major Arcana/
│   ├── Minor Arcana/
│   │   ├── Wands/
│   │   ├── Cups/
│   │   ├── Swords/
│   │   └── Pentacles/
│   ├── Spreads/
│   └── Tree of Life/
└── The Window/
    ├── The 64 Patterns/
    ├── Twelve Archetypes/
    ├── Ten Portals/
    └── Six Lower Houses/
```

### Achievements & Ongoing Considerations

**Resolved:**
- ✅ Tag taxonomy documented (Section II below)
- ✅ Search methodology documented (Section III below)
- ✅ High wikilink density (97%+) enables cross-reference navigation
- ✅ Index system established (Tarot Master Index created as model)

**Ongoing Maintenance:**
- Tag consistency varies across files (gradual migration during regular updates)
- Additional pillar indexes can be created as needed
- Cross-reference maps remain a future enhancement opportunity

---

## II. Tag Taxonomy (Standardized Conventions)

### Core Principle

**Tags should be machine-readable and human-scannable.** They enable both search (grep, Obsidian) and at-a-glance categorization.

### Tagging Standards

**Format:** Use hashtags for all tags in YAML frontmatter (Obsidian best practice)

```yaml
tags: [system, category, specific-descriptor, archetypal-theme]
```

**Examples:**
- `tags: [tarot, major-arcana, archetypal, mercury]`
- `tags: [astrology, planets, archetypal, saturnian]`
- `tags: [human-design, type, generator, sacral]`

### Tag Hierarchy (Four Levels)

#### Level 1: System Tag (Required)

Identifies which of the Seven Pillars this entry belongs to.

**Standard system tags:**
- `#tarot`
- `#astrology`
- `#human-design`
- `#qabalah` or `#the-window` (two names for same pillar)
- `#i-ching` (if distinct from The Window)
- `#jungian` or `#folklore`
- `#angelology`
- `#synthesis` (for cross-system pieces in ⚛ Synthesis/)
- `#system` (for meta/protocol documents in ◈ System/)

**Usage:** First tag in array

#### Level 2: Category Tag (Required)

Identifies the subcategory within the system.

**Tarot category tags:**
- `#major-arcana`
- `#minor-arcana`
- `#court` (for court cards specifically)
- `#wands`, `#cups`, `#swords`, `#pentacles` (suit tags)
- `#spreads`
- `#tree-of-life` (Tarot/Qabalah mapping)

**Astrology category tags:**
- `#planets`
- `#signs`
- `#houses`
- `#aspects`
- `#transits` (for transit analysis documents)
- `#dignity` (for dignity tables, rulership documents)

**Human Design category tags:**
- `#type`
- `#centers`
- `#channels`
- `#gates`
- `#profiles`
- `#strategy`
- `#authority`
- `#definition`

**Usage:** Second tag in array (may have multiple category tags if entry spans categories)

#### Level 3: Specific Descriptors (Optional but Recommended)

Fine-grained tags for searching by quality, element, or attribute.

**Elemental tags:**
- `#fire`, `#water`, `#air`, `#earth` (for elemental correspondences)

**Qabalistic tags:**
- `#kether`, `#chokmah`, `#binah`, `#chesed`, `#geburah`, `#tiphareth`, `#netzach`, `#hod`, `#yesod`, `#malkuth` (Sephiroth)
- `#atziluth`, `#briah`, `#yetzirah`, `#assiah` (Qabalistic Worlds)

**Astrological tags:**
- `#cardinal`, `#fixed`, `#mutable` (modalities)
- `#fire`, `#earth`, `#air`, `#water` (elements, duplicates above)
- Planetary tags: `#mercurial`, `#venusian`, `#martial`, `#jovial`, `#saturnian`, `#uranian`, `#neptunian`, `#plutonian`
- `#personal-planets`, `#social-planets`, `#outer-planets`

**Human Design tags:**
- `#defined`, `#undefined`, `#open` (for center status)
- `#sacral`, `#emotional`, `#splenic`, `#ego`, `#self` (Authority types)
- `#manifestor`, `#generator`, `#manifesting-generator`, `#projector`, `#reflector` (Types)

**Jungian/Archetypal tags:**
- `#shadow`, `#anima`, `#animus`, `#self`, `#persona`, `#ego`
- `#hero-journey`, `#threshold`, `#initiation`, `#death-rebirth`

**Usage:** Third, fourth, fifth tags as needed

#### Level 4: Cross-System Archetypal Themes (Optional)

High-level archetypal themes that span multiple systems. Use sparingly for major patterns.

**Archetypal theme tags:**
- `#archetypal` (general archetypal content)
- `#sovereignty`, `#authority`, `#power`
- `#transformation`, `#death-rebirth`, `#initiation`
- `#integration`, `#individuation`, `#wholeness`
- `#communication`, `#expression`, `#voice`
- `#love`, `#relationship`, `#union`
- `#structure`, `#discipline`, `#mastery`
- `#chaos`, `#disruption`, `#breakthrough`
- `#wisdom`, `#knowledge`, `#gnosis`

**Usage:** Final tag(s) when entry touches major universal themes

### Tag Format Rules

**DO:**
- Use lowercase only: `#tarot` not `#Tarot`
- Use hyphens for multi-word tags: `#major-arcana` not `#MajorArcana` or `#major_arcana`
- Use singular form: `#planet` not `#planets` (except when referring to category itself)
- Be consistent with planetary adjectives: `#saturnian`, `#mercurial`, `#venusian`

**DON'T:**
- Don't use spaces: `#human design` → `#human-design`
- Don't use underscores: `#major_arcana` → `#major-arcana`
- Don't use camelCase: `#MajorArcana` → `#major-arcana`
- Don't create redundant tags: `[#tarot, tarot-cards]` → just `[#tarot]`

### Migration Plan for Existing Files

**Current inconsistency:** Tarot files lack hashtags, others have them.

**Solution:** Gradual migration during regular updates
- When revising a file for content, fix tags to match new standard
- No need for bulk "tag-fix only" commits—combine with content work
- Priority: Fix tags when files are touched for other reasons

**Tag Fixer Command (Optional):**
```bash
# Run only when specifically cleaning up a batch of files
# Adds # to all tags in YAML frontmatter
sed -i 's/tags: \[/tags: \[#/g' file.md
# (This is simplified—would need more sophisticated regex for real use)
```

---

## III. Search Protocols (How to Find Content)

### Available Search Tools

1. **Glob** (file pattern matching) - For finding files by name pattern
2. **Grep** (content search) - For finding files by content, tags, or text
3. **Obsidian** (if user uses it) - Graph view, tag search, backlinks
4. **Index Files** (once created) - Quick reference master lists

### Common Search Scenarios

#### Scenario 1: "Find all entries about [concept]"

**Example:** "Find all entries about Saturn"

**Method 1: Grep by filename**
```bash
find "📖 Library" -type f -name "*Saturn*"
```

**Method 2: Grep by content/tags**
```bash
grep -r "#saturnian" "📖 Library" --include="*.md"
grep -r "\[\[Saturn\]\]" "📖 Library" --include="*.md"
```

**Method 3: Use Index** (once created)
- Check `📖 Library/Astrology/INDEX - Astrology Master List.md`
- Scan "Planets" section for Saturn entry with direct link

**Best Practice:** Start with Index (fastest), fall back to grep if Index incomplete

#### Scenario 2: "Show me all [category] entries"

**Example:** "Show me all Tarot Major Arcana cards"

**Method 1: Glob by directory**
```bash
ls "📖 Library/The Tarot/Major Arcana/"
```

**Method 2: Grep by tag**
```bash
grep -l "#major-arcana" "📖 Library/The Tarot"/**/*.md
```

**Method 3: Use Index**
- Check `📖 Library/The Tarot/INDEX - Tarot Master List.md`
- Major Arcana section lists all 22 cards with links

**Best Practice:** Use Index for overview, use directory listing for raw filenames

#### Scenario 3: "Find all entries tagged with [theme]"

**Example:** "Find all entries dealing with transformation/death-rebirth"

**Method: Grep by archetypal tag**
```bash
grep -l "#transformation" "📖 Library" -r --include="*.md"
grep -l "#death-rebirth" "📖 Library" -r --include="*.md"
```

**Output:** List of files across all systems that share this theme

**Use Case:** Cross-system thematic exploration (e.g., preparing synthesis piece on transformation archetype)

#### Scenario 4: "What references [this entry]?"

**Example:** "What other Library entries reference The Tower card?"

**Method: Grep for wikilink**
```bash
grep -l "\[\[The Tower\]\]" "📖 Library" -r --include="*.md"
grep -l "\[\[16 - The Tower\]\]" "📖 Library" -r --include="*.md"
```

**Note:** Searches for both simple and numbered wikilink formats

**Best Practice:** This finds backlinks—entries that reference The Tower in their text

#### Scenario 5: "Show me incomplete/stub entries"

**Example:** "Which Library entries need expansion?"

**Method 1: Grep for TBD markers**
```bash
grep -l "TBD" "📖 Library" -r --include="*.md"
```

**Method 2: Check file size** (stubs are usually <2KB)
```bash
find "📖 Library" -type f -name "*.md" -size -2k
```

**Use Case:** Identifying Priority 3 work (expanding Tier 1 entries to Tier 3)

#### Scenario 6: "Find entries by element"

**Example:** "Show me all Fire element entries"

**Method: Grep by elemental tag**
```bash
grep -l "#fire" "📖 Library" -r --include="*.md"
```

**Output:** All Tarot Wands, Fire signs (Aries/Leo/Sag), Fire-related archetypes

**Use Case:** Elemental synthesis work, understanding Fire across systems

### Search Best Practices

**1. Start Broad, Then Narrow**
- Begin with Index files (quickest overview)
- Use directory listings for category browsing
- Use grep for specific content/tag searches

**2. Use Multiple Search Terms**
- `grep -l "#saturn" -r` finds by tag
- `grep -l "Saturn" -r` finds by content mention
- `grep -l "\[\[Saturn\]\]" -r` finds by wikilink
- Combine results for comprehensive coverage

**3. Leverage Wikilinks**
- 97% of files have wikilinks—they're the primary cross-reference system
- Searching for `\[\[concept\]\]` reveals connections

**4. Know Your Wildcards**
- `*` matches any characters: `*Saturn*.md` finds "Saturn.md", "Saturn Return.md"
- `**` recursive directory match: `Library/**/*.md` finds all .md files in all subdirectories

**5. Output Modes**
- `-l` (files with matches) - Just filenames
- `-h` (no filename prefix) - Just matched content
- `-C 2` (context lines) - Show 2 lines before/after match
- `-n` (line numbers) - Show which line contains match

---

## IV. Index System (Master Lists)

### Purpose

Index files provide **at-a-glance navigation** for each pillar, showing:
- What exists (completed entries)
- What's missing (planned/stub entries)
- How to access each entry (direct [[wikilinks]])
- Current completion status

### Index File Locations

**One index per major pillar:**

```
📖 Library/Astrology/INDEX - Astrology Master List.md
📖 Library/Human Design/INDEX - Human Design Master List.md
📖 Library/The Tarot/INDEX - Tarot Master List.md
📖 Library/The Window/INDEX - The Window Master List.md
📖 Library/Personal Mythos/INDEX - Personal Mythos & Jungian Master List.md
📖 Library/Angelology/INDEX - Angelology Master List.md
📖 Library/Core Foundations/INDEX - Core Foundations Master List.md
```

**Meta-Index (optional future addition):**
```
📖 Library/INDEX - Complete Library Overview.md
```

### Index File Template

```markdown
---
tags: [index, {system}, navigation]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
---

# {System} Master Index

**Purpose:** At-a-glance navigation for all {System} Library entries

**Last Updated:** YYYY-MM-DD
**Completion Status:** {X}/{Y} entries ({Z}%)

---

## {Category 1}

**Completion:** {X}/{Y} entries

| Entry | Status | Link |
|-------|--------|------|
| {Name} | ✅ Complete | [[{Filename}]] |
| {Name} | 🟡 Stub | [[{Filename}]] |
| {Name} | ⚪ Planned | _Not yet created_ |

---

## {Category 2}

...continue for all categories...

---

## Cross-References

**This system connects to:**
- [[{Other System 1}]] via [{connection type}]
- [[{Other System 2}]] via [{connection type}]

---

## Changelog

- **YYYY-MM-DD:** Index created
- **YYYY-MM-DD:** Updated with {new entries}
```

### Status Indicators

Use emoji for quick visual scanning:

- **✅ Complete** - Entry meets Tier 3 (comprehensive) standard per Library Content Rubric
- **🟡 Partial** - Entry exists but is Tier 1 (stub) or Tier 2 (intermediate)
- **⚪ Planned** - Entry doesn't exist yet but is on roadmap

### Update Protocol

**When to update Index:**
- After committing new Library entries (add to Index in same commit or immediately after)
- During quarterly Library Maintenance Cycles (once that protocol exists)
- When restructuring categories or discovering gaps

**Who updates:**
- Claude updates automatically when creating new entries
- User can update manually if preferred

---

## V. Cross-Reference Mapping System

### Current State

**Wikilink Density:** 97% of Library files contain [[wikilinks]]—excellent foundation for cross-reference mapping!

**Wikilink Conventions:**
- Use `[[double brackets]]` for all cross-references
- Include entry name exactly as filename (with or without extension)
- For Tarot: `[[8 - Strength]]` or `[[Strength]]` both acceptable
- For concepts: `[[Saturn]]`, `[[Generator Type]]`, `[[Shadow]]`

### Internal Links Section (Required in All Library Entries)

Every Library entry must include **"## Internal Links"** section (per Library Content Rubric):

```markdown
## Internal Links

**Cross-System References:**
- [[{Entry from other system}]] - {Brief note on connection}
- [[{Another entry}]] - {Why it's relevant}

**Within-System References:**
- [[{Related entry in same system}]] - {Relationship}

**Synthesis Pieces Referencing This Entry:**
- [[{Synthesis piece}]] - {How it uses this entry}
```

**Purpose:**
- Documents outbound links (what this entry references)
- Documents inbound links (what references this entry)
- Creates bidirectional navigation

### Cross-Reference Search Patterns

**Find all references TO an entry:**
```bash
grep -r "\[\[Saturn\]\]" "📖 Library" --include="*.md"
```

**Find all references FROM an entry:**
- Read the "Internal Links" section of the entry itself

**Find cross-system connections:**
```bash
# Example: Find all Tarot entries that reference Astrology concepts
grep -r "\[\[.*\]\]" "📖 Library/The Tarot" --include="*.md" | grep -i "saturn\|mars\|venus\|mercury"
```

### Cross-Reference Map (Future Enhancement)

**Potential future addition:** Generate visual maps showing connection density
- Which entries are most-referenced (hub nodes)?
- Which systems cross-reference most frequently?
- What are isolated entries (low cross-reference = needs integration)?

**Tool options:**
- Obsidian Graph View (if user uses Obsidian)
- Custom script to generate GraphViz/DOT file from wikilink analysis
- Manual curation in a "Cross-Reference Patterns" document

**Priority:** Low (wikilinks already provide functional navigation)

---

## VI. Search Protocols for Claude

### When Claude Needs to Find Content

**Scenario 1: User asks about a concept Claude hasn't seen recently**

**Example:** User asks "Tell me about Gate 51"

**Claude's search process:**
1. **Check if file exists:** `find "📖 Library/Human Design/Gates" -name "*51*"`
2. **If found, read it:** `Read` tool on the file
3. **If not found, search broader:** `grep -r "Gate 51" "📖 Library"` (might be in overview file)
4. **If still not found:** Notify user, offer to fetch from NotebookLM or create stub

**Scenario 2: User asks for cross-system synthesis**

**Example:** "Compare Saturn and The Devil card"

**Claude's search process:**
1. **Find both entries:**
   - `find "📖 Library" -name "*Saturn*"`
   - `find "📖 Library" -name "*Devil*"`
2. **Read both entries**
3. **Check Internal Links sections** to see if they already reference each other
4. **Proceed with synthesis** using Cross-System Synthesis Protocol

**Scenario 3: User asks "What do we have on [topic]?"**

**Example:** "What do we have on transformation?"

**Claude's search process:**
1. **Search by tag:** `grep -l "#transformation" "📖 Library" -r`
2. **Search by wikilink:** `grep -l "\[\[Transformation\]\]" "📖 Library" -r`
3. **Search by content:** `grep -l "transformation" "📖 Library" -r` (broader)
4. **Report findings** with file paths and brief context
5. **Offer to read specific entries** if user wants details

### Search Preferences for Claude

**Priority order:**
1. **Index files** (fastest, curated)—use when they exist
2. **Grep by tag** (precise, requires standardized tags)
3. **Grep by wikilink** (finds cross-references)
4. **Grep by content** (broadest, may have false positives)
5. **Fallback to NotebookLM** (if local search fails)

**Best practice:**
- Use multiple search methods in parallel (Grep multiple patterns)
- Report what was searched and what was found/not found
- Offer user choice if multiple matches

---

## VII. Maintenance & Evolution

### Regular Maintenance Tasks

**When creating new Library entries (always):**
- [ ] Apply correct tag taxonomy (Section II)
- [ ] Include Internal Links section with cross-references
- [ ] Update relevant Index file to include new entry
- [ ] Git commit includes both entry and updated Index

**Quarterly Library Audit (once protocol exists):**
- [ ] Review Index files for accuracy
- [ ] Update status indicators (✅🟡⚪)
- [ ] Check for dead [[wikilinks]] (links to non-existent files)
- [ ] Standardize any remaining tag inconsistencies
- [ ] Identify stub entries that need expansion

**When restructuring Library:**
- [ ] Update Index files to reflect new organization
- [ ] Update PROTOCOL - Search and Navigation if search patterns change
- [ ] Notify user of structural changes

### Tag Evolution

**As Library grows, tag taxonomy may need refinement:**
- New archetypal themes emerge → add to Level 4 tags
- New systems added → add to Level 1 system tags
- Granularity needs change → add to Level 3 specific descriptors

**Process for adding new tags:**
1. Propose new tag in discussion with user
2. Document in Section II of this protocol
3. Apply to new entries going forward
4. Optionally backfill to existing entries during regular updates

### Index Scalability

**Current plan:** One index per pillar (manageable at 500-1000 total entries)

**If Library grows beyond 1000 entries:**
- Consider splitting indexes by sub-category (e.g., separate index for Tarot Major vs. Minor)
- Create meta-index linking to sub-indexes
- Automate index generation with script (extract filenames + status from directory)

---

## VIII. Quick Reference

### Tag Taxonomy Cheat Sheet

```yaml
# Template
tags: [system, category, specific-descriptor, archetypal-theme]

# Examples
tags: [tarot, major-arcana, fire, transformation]
tags: [astrology, planets, saturnian, authority]
tags: [human-design, type, generator, sacral]
tags: [synthesis, cross-system, death-rebirth]
```

### Common Search Commands

```bash
# Find file by name
find "📖 Library" -name "*keyword*"

# Find files by tag
grep -l "#tag-name" "📖 Library" -r --include="*.md"

# Find files by wikilink
grep -l "\[\[Concept\]\]" "📖 Library" -r --include="*.md"

# Find files by content
grep -l "search term" "📖 Library" -r --include="*.md"

# List all files in category
ls "📖 Library/{System}/{Category}/"

# Find small files (potential stubs)
find "📖 Library" -type f -name "*.md" -size -2k

# Count total files
find "📖 Library" -type f -name "*.md" | wc -l
```

### Index File Locations

- `📖 Library/Astrology/INDEX - Astrology Master List.md`
- `📖 Library/Human Design/INDEX - Human Design Master List.md`
- `📖 Library/The Tarot/INDEX - Tarot Master List.md`
- `📖 Library/The Window/INDEX - The Window Master List.md`
- `📖 Library/Personal Mythos/INDEX - Personal Mythos & Jungian Master List.md`
- `📖 Library/Angelology/INDEX - Angelology Master List.md`

---

## Changelog

- **2026-01-19:** Updated statistics, converted challenges to achievements (v1.1)
- **2026-01-10:** Initial protocol created (v1.0)

---

*"A library without a catalog is a labyrinth. A catalog without a library is an empty promise. Both are required for wisdom to be accessed."*
