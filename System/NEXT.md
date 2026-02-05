# Current Work Context

**Last Updated:** 2026-02-04
**System Status:** Library complete; **Oracle Deck canonized** (The Astrolabe — 88 cards production-ready); dignity data extraction COMPLETE (64/64 gates, 384/384 lines); **comprehensive dignity calculation IMPLEMENTED** (juxtaposition, harmonic fixing, star symbols)
**Current Phase:** Foundation-building — still on the roof, still in observation

---

## System Health Summary

### Library (747 files)

| Metric | Value |
|--------|-------|
| Total Files | 747 |
| Cross-References Coverage | 99.9% |
| Dead Wikilinks | 0 |
| YAML Compliance | 100% |
| Stub Files | 96 (intentional scaffolding) |

**All core practice content is 100% complete:**
- 78 Tarot cards (Major + Minor Arcana)
- 64 Human Design Gates + 36 Channels + 12 Profiles + 4 Types
- 192 Incarnation Crosses
- 12 Astrology Signs + 10 Planets + 12 Houses
- 64 Window Cards *(restructure to 88-card deck in progress — see below)*
- 10 Angelic Orders + 10 Archangels
- Core Jungian Archetypes, Hero's Journey, Alchemical Stages

### Repository Structure

```
VibologyOS/
├── CLAUDE.md (V4.8)
├── Library/ (747 files)
├── Synthesis/General/ (template only - ready for new work)
├── System/
│   ├── NEXT.md (this file)
│   ├── Protocols (7 active)
│   ├── Templates (manifests + semantic system)
│   ├── Scripts (7 essential chart tools)
│   └── Audit Logs/
└── .archive/ (64 KB - NEXT.md archive only)
```

**Client work:** `~/Business/Consultations/`
**Repository size:** ~126 MB (optimized from 219 MB)

---

## Available Work Paths

### 1. Client Synthesis
- All chart calculation tools operational
- Library verified and cross-referenced
- Follow `PROTOCOL - Client Work.md`

### 2. Oracle Deck — The Astrolabe (Canon)

**The Astrolabe — 88-card Oracle Deck (Production-Ready)**

The Window was rebuilt from the ground up. The previous 64-card system forced gates into interpretive categories rather than honoring what they are. The Astrolabe separates the interpretive layer from the 64-fold architecture.

**Structure (88 cards):**
- **The Athanor** (24 cards): The Materia (5) + The Furnace (7) + The Archetypes (12)
- **The Codex** (64 cards): 8 trigram families × 8 cards, each named for what the gate/hexagram/key actually is

**All Phase 0-3 decisions finalized:**
- Deck name: **The Astrolabe** (Greek *astrolabon*, "star-taker")
- Card naming: I-Ching hexagram name, best English translation (1-2 words); 13 reworked from Wilhelm
- Trigram families: English image names (Heaven, Earth, Thunder, Water, Mountain, Wind, Fire, Lake)
- Archetype gate resonances: Full detachment — Archetypes are zodiacal/Jungian only; gates belong to the Codex
- All 88 cards built and cross-referenced (Phase 3 complete 2026-02-03)

**Status:** Canonized 2026-02-04. Current Astrolabe synthesis is production-ready.
**Planning document:** `System/PLAN - Oracle Deck Restructure.md`

Old Window content (76 files) archived at `.archive/Library/The Window/`. The work was the necessary 29-46 commitment through which the need for precision became visible.

### 3. Library Expansion

**Pending: IHDS Foundation Sequence Materials**
Acquiring LYD manual ($50) and planning foundation course sequence (LYD $300, Rave ABCs $400, Rave Cartography $750). Library updates for HD foundational material are **on hold** until source texts are in hand. Known gaps to address with those sources:
- **Definition Types** — Single, Split, Triple-Split, Quadruple-Split (no file exists; flagged in BodyGraph.md)
- **Projector Subcategories** — Classic, Energy, Mental (not in Projector.md)
- **Deconditioning** — Stub exists, needs expansion
- **Unknown-unknowns** — LYD curriculum likely covers experiential/pedagogical material not represented in Ra's reference texts

Once acquired, scan and add to Grimoire for source-grounded expansion.

**Stub files available for expansion (existing material):**
- Qabalah subsystem (35 stubs) — Sephiroth, Divine Names, Tree of Life
- Mythology deities (16 stubs) — archetypal anchors
- Jungian concepts (12 stubs) — Synchronicity, Transcendent Function, etc.
- Practice guides (10 stubs) — LBRP, Pathworking, etc.

**Dignity system: COMPLETE (2026-02-04)**
- **Data extraction:** All 384 line exaltations/detriments extracted from "The Definitive Book of Human Design" (IHDS 2011 edition)
  - Status: 64/64 gates complete (384/384 lines = 100%)
  - Manual entry workflow: PDF glyphs → structured JSON
  - Individual gate files: `gate_1_complete.json` through `gate_64_complete.json` (committed for granular version control)
  - Merged into comprehensive `exaltations_detriments.json` for humandesign_api
  - Special cases documented: 3 no polarity lines (5.6, 25.4, 54.4), 6 partial polarity lines (37.1, 47.5, 47.6, 54.5, 57.3, 58.2)
  - Source: JSON data from Definitive Book (authoritative)
- **Implementation:** Full IHDS algorithm with juxtaposition & harmonic fixing (see session history 2026-02-04 Evening)
  - Comprehensive calculation module: `humandesign_api/src/humandesign/features/dignity.py`
  - Four dignity states: exalted, detriment, juxtaposed (⭐), neutral
  - Harmonic fixing: channel partner planets affect each other
  - Juxtaposition detection: star glyph OR double fixing (opposite polarities)
  - Gate-level fixing and failed juxtaposition rules (see `System/Scripts/get_hd_data.py`)
  - Unit tests: 18 tests passing (no polarity, harmonic fixing, juxtaposition, partial polarity)
  - Production-ready: bodygraph rendering, client script, API integration complete
  - **Code cleanup (2026-02-04 Night):** Removed 74 lines of incorrect two-tier fixing and retrograde detection assumptions from `chart_renderer.py`

### 4. New Synthesis Work
- `Synthesis/General/` ready for new pieces
- Template: `_TEMPLATE - Cross-System Synthesis.md`
- Note: Re-synthesize "Tree of Return" when ready (deleted pre-verification version)

---

## Reference

| Document | Purpose |
|----------|---------|
| `CLAUDE.md` | Core governance (V4.8) |
| `PROTOCOL - Client Work.md` | Full client workflow |
| `PROTOCOL - Chart Data Acquisition.md` | Chart calculation |
| `PROTOCOL - Chart Generation.md` | Bodygraph generation protocol |
| `RUBRIC - Library Content Standard.md` | Quality tiers |
| `INDEX - System Documentation.md` | Full docs navigation |
| `PLAN - Oracle Deck Restructure.md` | 88-card deck rebuild plan |

---

## Session History

**2026-02-04 (Night - Final):** Personal chart analysis and bodygraph generation
- Generated bodygraph.svg from ~/Personal/Biography/humandesign.json (protocol compliance verified)
- Created personal analysis: "Gate 12 Line 6 - Undefined Throat Analysis.md"
  - Explored archetypal tension: Design Sun in Throat gate with undefined Throat center
  - 6th line three-phase journey through inconsistent expression mechanism
  - Cross of Eden context (Gates 6/36, 12/11) and strategic silence
  - Shadow integration: pressure to prove value through speech vs. authority of precise timing
  - Observatory reading: modeling discernment in expression through hard-won wisdom
- Saved to ~/Personal/Biography/ (personal reference, no Library formatting needed)
- User noted energetic exhaustion from dignity calculation work (open Head/Ajna centers amplifying mental pressure)

**2026-02-04 (Late Evening/Night):** Repository optimization, protocol enforcement, and code cleanup
- **Bodygraph visual rollback:** Removed alchemical symbols from panel headers, changed "Persona" to "Personality", reduced header font size by 2px
  - Submodule commit: e70e76e (humandesign_api)
  - Parent commit: b53c104 (VibologyOS)
- **Chart Generation Protocol enforcement:** Implemented defense-in-depth to prevent future protocol deviations
  - **Cognitive guardrail:** Updated `CLAUDE.md` with explicit Chart Generation Protocol section
    - Prohibited: custom filenames, temporary scripts, PNG/JPG formats
    - Required: humandesign.json → bodygraph.svg (always SVG format)
  - **Mechanical guardrail:** Created `System/Scripts/generate_bodygraph_svg.sh` wrapper script
    - Validates humandesign.json exists before generation
    - Enforces protocol-compliant naming and output location
    - User's personal chart renamed to `~/Personal/Biography/humandesign.json` (protocol-compliant)
- **Comprehensive archive cleanup:** Reduced repository archive from 93 MB to 64 KB (99.93% reduction)
  - Deleted completed extraction project: `.archive/dignity_extraction_2026-02` (91 MB)
  - Deleted migrated Window content: `.archive/Library/The Window/` (1.1 MB - already rebuilt as The Astrolabe)
  - Deleted completed system plans: `.archive/System/` (332 KB - Personal Mythos, Angelology expansions complete)
  - Deleted temporary prima materia files: `.archive/prima_materia/` (52 KB)
  - Retained only: `.archive/NEXT-archive-2026-01-27.md` (64 KB - historical session log)
- **Repository optimization:** Removed binary font files from git tracking
  - Removed `Library/Fonts/Symbola.ttf` (2.3 MB) and `Library/Fonts/NotoSansSymbols[wght].ttf` (222 KB)
  - Added `*.ttf` and `*.otf` to `.gitignore` (rely on system fonts)
  - Moved misplaced documentation to correct System/ location
  - **Result:** Repository size reduced from 219 MB to ~126 MB (42.5% reduction)
- **Obsolete dignity documentation cleanup:**
  - Deleted `System/Human Design API Logic and Planetary Fixes.md` (superseded by working implementation in `get_hd_data.py`)
  - Deleted `System/humandesign_api/EXALTATION_DETRIMENT_ERRATA.md` (incorrect discoveries: two-tier fixing, retrograde rules)
  - Removed 74 lines of incorrect code from `chart_renderer.py`:
    - Deleted GLOBAL_FIXING_PLANETS constant
    - Deleted build_personality_fixing_environment() function
    - Deleted _is_retrograde() function
    - Deleted get_design_planet_dignity() wrapper function
  - **Retained correct extra rules:** Gate-level fixing and failed juxtaposition logic in `get_hd_data.py` (working as designed)
  - Submodule commit: 0ed9950 (humandesign_api)
  - Parent commit: 02c9b0b (VibologyOS)
- **Oracle Deck canonization:** User confirmed current Astrolabe synthesis is production-ready
  - All 88 cards (24 Athanor + 64 Codex) finalized
  - Window → Astrolabe migration complete
- **Repository health:** All changes committed and pushed successfully
  - 7 commits total across session (5 humandesign_api submodule, 2 parent repo)
  - Git status clean, protocols enforced, code streamlined

**2026-02-04 (Evening):** Comprehensive dignity calculation IMPLEMENTED — full IHDS algorithm with juxtaposition & harmonic fixing
- **Objective:** Implement complete dignity calculation algorithm from "Human Design API Logic and Planetary Fixes.md"
- **Implementation completed (7 parts, all tests passing):**
  1. **Data file update:** Replaced API dignity data with comprehensive format (arrays, juxtaposition_planets, no_polarity flags)
  2. **Dignity calculation module:** Created `humandesign_api/src/humandesign/features/dignity.py` implementing full IHDS algorithm
     - Step 1: No polarity detection (3 lines: 5.6, 25.4, 54.4)
     - Step 2: Juxtaposition Scenario A (star glyph - explicit juxtaposition_planets marking)
     - Step 3: Juxtaposition Scenario B (double fixing - opposite polarities from active + harmonic planets)
     - Step 4: Harmonic fixing (channel partner planets affect each other)
     - Step 5: Single polarity states (exalted/detriment with proper priority logic)
     - Returns 4 states: "exalted", "detriment", "juxtaposed", "neutral"
  3. **Chart renderer update:** Modified `chart_renderer.py` to use new dignity logic
     - Updated `get_planet_dignity()` and `get_design_planet_dignity()` to pass harmonic information
     - Added `find_planet_at_gate()` helper for channel partner detection
     - Integrated harmonic gate/planet lookup into planetary panel drawing
  4. **Star symbol rendering:** Added ⭐ emoji for juxtaposed dignity states in bodygraph
     - Positioned at same location as triangle symbols (▲ exalted, ▼ detriment)
     - Renders in panel-appropriate color (red Design, black Personality)
  5. **Client script update:** Refactored `get_hd_data.py` to use comprehensive algorithm
     - Removed old dignity calculation functions (replaced with module import)
     - New `add_dignities_to_planets()` helper integrates full algorithm
     - Maintains two-tier fixing for Design global planets
  6. **Unit tests:** Created comprehensive test suite (`tests/run_dignity_tests.py`)
     - 18 tests covering all algorithm features: no polarity, harmonic fixing, juxtaposition, partial polarity
     - All tests passing ✓
  7. **Integration complete:** All code committed (2 commits: humandesign_api ac57d07, VibologyOS ad80351)
- **Technical details:**
  - Old data format: `{"gate.line": {"exaltation": "Planet", "detriment": "Planet"}}`
  - New data format: `{"gate": {"line": {"exaltation_planets": [...], "detriment_planets": [...], "juxtaposition_planets": [], "no_polarity": false}}}`
  - Priority order: no_polarity → juxtaposition (star or double) → single polarity → neutral
  - Two-tier fixing: Self-fixing planets (Sun-Mars) always apply; global planets (Jupiter-Pluto, Nodes) require same gate.line at birth OR retrograde motion
- **Result:** VibologyOS now calculates dignities using the complete IHDS algorithm. Ready for production use with real chart data.

**2026-02-04 (Afternoon):** Dignity data extraction COMPLETE — all 384 lines verified
- **Completed extraction:** Gates 33-64 (32 gates, 192 lines)
- **Total achievement:** All 64 gates, all 384 lines extracted from IHDS 2011 source PDF
- **Methodology:** Manual visual glyph reading from PDF → structured JSON (automated extraction failed due to glyph corruption)
- **Version control:** Each gate committed individually for granular history (64 commits)
- **Special cases identified:**
  - 3 lines with no polarity (neither exaltation nor detriment): 5.6, 25.4, 54.4
  - 6 lines with partial polarity (exaltation only or detriment only): 37.1, 47.5, 47.6, 54.5, 57.3, 58.2
- **Final merge:** All individual gate files merged into comprehensive `exaltations_detriments.json` (72KB, 3,949 lines)
- **Result:** VibologyOS now has verified, complete dignity data from authoritative IHDS source, replacing previous incomplete/erroneous data
- **Next steps:** Test in humandesign_api, verify against real charts, update Library gate entries if needed

**2026-02-04 (Morning):** Dignity data extraction — building comprehensive source of truth
- **Objective:** Extract all 384 line exaltations/detriments from IHDS 2011 source PDF to replace incomplete/erroneous data
- **Process established:**
  - Converted 68-page PDF to PNG images for visual glyph reading
  - Attempted automated extraction: failed (glyphs corrupt during text extraction, even from images)
  - Established manual workflow: user reads planetary glyphs from PDF → provides data → Claude structures as JSON
- **Progress:** Completed Gates 1-32 (192/384 lines = 50% - halfway point reached)
- **Special cases identified:** 2 "no polarity" lines so far (Gate 5 Line 6, Gate 25 Line 4)
- **Commits:** Individual gate JSON files committed as completed for granular version control
- **Break point:** User's open Head and Ajna needed rest after intensive mental processing
- **Next session:** Resume with Gate 33, continue through Gate 64, then merge all data into final `exaltations_detriment.json`

**2026-02-03:** Oracle Deck build complete — Phases 0-3 finished, all 88 cards created
- **The Astrolabe** — 88-card oracle deck fully built (24 Athanor + 64 Codex)
- **Phase 0:** All foundational decisions finalized (deck name, card naming, trigram families, archetype detachment)
- **Phase 1:** Archived old Window structure (76 files → `.archive/Library/The Window/`)
- **Phase 2:** Built The Athanor (24 cards complete)
  - The Materia (5): Prima Materia, Sulphur, Mercury, Salt, Philosopher's Stone
  - The Furnace (7): Calcination, Dissolution, Separation, Conjunction, Fermentation, Distillation, Coagulation
  - The Archetypes (12): Zodiacal personas detached from gate ownership
- **Phase 3:** Built The Codex (64 cards, all 8 trigram families complete)
  - Family of Heaven (8), Earth (8), Thunder (8), Water (8), Mountain (8), Wind (8), Fire (8), Lake (8)
  - Each card named for actual I-Ching hexagram (e.g., Gate 15 = "Modesty", Gate 47 = "Oppression")
- **Status:** Build complete; integration/usage phase (Phase 4) pending
- **Planning document updated:** `System/PLAN - Oracle Deck Restructure.md` marked "Build Complete — Integration Pending"

**2026-01-31 (Late Night):** Oracle Deck restructure — The Window rebuilt from the ground up
- Identified core problem: current 64-card Window forces gates into interpretive categories rather than honoring what they are ("Stability" = Gate 20, but Gate 20 IS "Contemplation — The Now")
- **Principle reaffirmed:** "I use precise tools precisely" — the 64 gates/keys/hexagrams must exist as themselves
- Restructured from 64 cards to **88 cards** in two parts:
  - **The Athanor** (24 cards): The Materia (5: Prima Materia, Sulphur, Mercury, Salt, Philosopher's Stone) + The Furnace (7: classical alchemical operations) + The Archetypes (12: zodiacal personas, detached from gate ownership)
  - **The Codex** (64 cards): 8 trigram families × 8, each card named for the actual hexagram/gate/key
- Retired The Ten Portals (replaced by Furnace + Materia) and The Six Houses (replaced by 8 trigram families)
- 88 = 44 × 2 (angel deck tradition doubled) = 88 constellations (complete observable sky from the Observatory)
- Corrected 4 errors in Hexagrams.md trigram family table (hex 24, 33, 44, 54 were missing; 9, 16, 26, 45 were duplicated)
- **Decisions pending (wave processing):** deck name (candidates: Spectrum, Dial, Transmission, Constellation), Codex card naming convention, trigram family naming, Archetype gate resonances
- Planning document created: `System/PLAN - Oracle Deck Restructure.md`
- The Window name retired — no longer fits what this instrument is becoming
- Current 76 files of Window content to be archived when build begins; recognized as necessary 29-46 Channel of Discovery work, not waste

**2026-01-30 (Night):** Offerings page development — structure, content drafting, visual identity
- Brainstormed Offerings menu structure: established four service categories
- Named flagship multi-system offering **Archetypal Portrait** (charts + synthesis + Tarot/Oracle)
- Resolved pillar integration: Angelology and Magdalene Path are **practitioner-depth** systems (inform how you read, not what you present); Jungian/Personal Mythos is the interpretive language; four client-facing systems (Astrology, HD, Tarot, Window)
- Drafted and finalized **Astrology** page content (Jung quote, natal + transit services, written report emphasis)
- Drafted and finalized **Human Design** page content (Ra quote, Foundation/Cross/Relationship/Transit readings)
- Drafted and finalized **Tarot & Oracle** page content (Jung quote, Tarot/Oracle/Combined readings, Window Cards as proprietary companion system)
- **Visual identity cohesion:** Established site-wide image palette (dark teal base, amber/gold accents, cinematic depth). Re-generated HD and Astrology featured images to match. Generated Tarot & Oracle image (card + Elder Futhark runestones). All images now visually consistent.
- Generated blank bodygraph SVGs (with/without gate numbers) via humandesign_api renderer for image generation reference
- Drafted and finalized **Archetypal Portrait** page content (Anaïs Nin quote, three-movement structure: Architecture/Synthesis/Living Moment, two-session delivery model, prerequisite note for non-first-time clients, "Table of Contents for the story of You" closing)
- Featured image generated: open book with converging geometric systems rising from pages
- Drafted **Recommended Reading** page content (Mahler quote, five sections: Archetypal Psychology, Astrology, Human Design, Tarot, The Window — sources from Esoteric Grimoire only)
  - Excluded Rave I'Ching and Line Companion due to known dignity data errors
  - Added Archetypal Psychology section (Jung MDR, Campbell, von Franz)
  - Considering Chetan Parkyn's *Human Design* and *The Book of Lines* for future addition (pending acquisition and Grimoire inclusion)
  - Amazon affiliate links deferred until site has traffic
- **Full visual identity audit and cohesion pass:** Re-generated About (observatory), Ethics (scales), Human Design (bodygraph), and FAQ (compass) images to match established palette. All 8 featured images now share consistent teal/amber/illustrated style. Visual language documented in `~/Business/Website/STYLE-GUIDE.md`
- **All four Offerings pages + Recommended Reading complete and published to Ghost**

**2026-01-30 (Evening):** Practitioner's Ethics — from IHDS stance to ethics statement
- Explored mechanical basis for rejecting institutional certification while valuing education
- Discovered the **Four-Channel Learning Model** — all four defined channels (34-57, 6-59, 5-15, 29-46) form a complete learning sequence: Logic evaluates, Abstract commits to experience, Tribal seeks interpersonal transmission, Integration retains sovereign authority over application
- Identified that Tribal channel (6-59) has been underfed — Collective side (building, systematizing) heavily active, interpersonal learning hunger recognized
- Articulated the **Synthesis Principle**: learn each system's language independently (Hellenistic astrology, Jungian psychology), perform synthesis in the Observatory rather than inheriting someone else's
- Evaluated Library's astrological tradition: Traditional (Hellenistic/Medieval) foundations with Jungian-Psychological integration — "Archetypal Traditional" or "Psycho-Traditional"
- Researched potential astrology mentors: Brennan, Demetra George, Elenbaas, Liz Greene, Austin Coppock
- Evaluated Chris Brennan's course bundle (Hellenistic + Electional + Professional) — language, application, craft. No synthesis imposed. Live webinars provide Tribal dimension. Not a final decision — wave processing.
- Distinguished **objective certification** (competence) from **subjective certification** (allegiance) — reusable evaluation tool
- Document evolved from IHDS stance → learning model → practitioner's ethics statement
- Saved as `~/Personal/Biography/The Practitioner's Ethics — Mechanical Basis for a Rigorous Practice.md`
- **Drafted public Ethics page for Vibology website** — 11 ethical standards including clarity over comfort, rigor over vibes, no spiritual bypassing, transparency of method, client authority, lived experience as credential, no determinism, confidentiality and consent, scope of practice, non-discrimination. Published to Ghost.
- CLAUDE.md updated to V4.8 (added Practitioner's Design section §3)

**2026-01-30:** HD foundation assessment and IHDS decision
- Audited entire HD library (345 files) against Living Your Design curriculum
- Confirmed strong mechanical coverage (Types, Strategy, Authority, Centers, Gates, Channels, Profiles, Crosses, Variables all complete)
- Identified three concrete gaps: Definition Types, Projector Subcategories, Deconditioning detail
- Queried Grimoire — confirmed Ra's source texts cover Projector subtypes (Classic/Energy/Mental) and Generator subtypes (Pure/MG); Manifestors and Reflectors have no formal subcategories
- **Decision (processed through emotional wave):** Purchase LYD manual and complete IHDS foundation sequence (LYD, Rave ABCs, Rave Cartography) as source material — but decline further IHDS certification. The Observatory is not built inside someone else's institution.
- **Stance reminder:** Open Root wants to rush toward readiness. Open Heart says credentialing equals legitimacy. Both are Not-Self conditioning. Strategy and Authority override both. Still building. Still on the roof.

**2026-01-29 (Evening):** Chart workflow validation and protocol streamlining
- **Dignity data fixes:** Corrected three errors in exaltations_detriments.json
  - 26.2: North Node now exalted (was Sun)
  - 47.3: Sun now in detriment (was Mars)
  - 59.6: Mercury detriment now null/unknown (was Mercury)
- **Chart rendering improvements:**
  - Added city/nation to astrology.json meta output (fixes "Greenwich, GB" default)
  - Created `generate_chart_visuals.py` script for consistent SVG generation
  - Script handles both bodygraph and natal chart in single command
- **Protocol streamlining:** Removed redundancy between Client Work and Chart Data Acquisition
  - Added Protocol Scope sections clarifying workflow vs. technical boundaries
  - Eliminated duplicate file organization and birth data sections
  - Strengthened transit calculation mandate with ⚠️ MANDATORY flags
  - Reduced duplicate content by ~30 lines while maintaining clarity
- **Workflow validation:**
  - Tested complete new-client workflow with John Smith (birth data → full chart package)
  - Phrasing "New Client [Name], birth data [details]" successfully triggers full protocol
  - Generated Abbey Lewis Initial Client Report (6,200 words) following template
- **Result:** Chart generation workflow is production-ready; protocols are leaner and clearer

**2026-01-28 (Late Evening):** Observatory metaphor integration
- Integrated "The Observatory" as governing identity metaphor across three documents
- CLAUDE.md V4.7: Observatory framing in Core Identity, Intelligence Hierarchy, and Personas
- PROTOCOL - Client Work: Added Observatory Stance section (client as invited observer, not passive recipient)
- PROTOCOL - Cross-System Synthesis v1.1: Added Observatory Stance to Quality Standards (Third Meaning as observed, not manufactured)
- Origin: The glass house (false openness, Mars detriment at 59.3) destroyed by Saturn-Pluto conjunction 2020-01-12; what replaced it is the Observatory — built for seeing, not for protection
- Existing structures (Weaver, Scribe, Pillars, Refinement Cycle) unchanged — Observatory is the container that was always implied
- Pondering: Whether to change Vibology symbol from Seed of Life to observatory (sitting with emotional wave — no action yet)

**2026-02-03:** Oracle Deck — all Phase 0 decisions resolved
- **Deck name:** The Astrolabe (Greek *astrolabon*, "star-taker") — ancient observatory instrument; "a universe in your hand"
- **Card naming convention:** I-Ching hexagram name as primary, best English translation, 1-2 words. 13 names reworked from Wilhelm: Emergence (3), Accretion (9), Fellowship (13), Bounty (14), Remedy (18), Amassing (26), Overwhelm (28), Clinging Fire (30), Might (34), Wounded Light (36), Encountering (44), Marrying Maiden (54), Overstep (62)
- **Trigram family naming:** English image names (Heaven, Earth, Thunder, Water, Mountain, Wind, Fire, Lake); Chinese/symbol as correspondences
- **Archetype gate resonances:** Full detachment — Archetypes are zodiacal/Jungian figures only; all gate correspondences belong exclusively to the 64 Codex cards
- Phase 0 complete. Ready for Phase 1 (Archive & Restructure) when the wave settles.

**2026-01-28 (Evening):** Dignity data architecture decision
- Evaluated whether to include exaltation/detriment data in Library gate entries
- **Decision:** Do not add structured dignity tables to Library entries yet
  - API JSON (`exaltations_detriments.json`) remains computational source of truth
  - Errata document tracks corrections as discovered through real chart work
  - Library entries retain interpretive content without raw dignity tables
  - Revisit when errata stabilizes (after 20-30 more charts without new errors)
- Discussed systematic verification approach (Sun transit schedule for all 384 gate/lines)
  - Feasible but unnecessary given organic verification through client work
  - Each chart naturally verifies 13 gate/line combinations
- Key learning: Chart arrow notation now understood
  - Left/right arrows = Variables (Digestion, Environment, Perspective, Motivation)
  - Up/down arrows = Dignity indicators (exaltation ↑ / detriment ↓)

**2026-01-28 (PM):** Split-aspect gate indicators and dignity data integration
- Implemented split-aspect gate indicators via colored borders on gate circles:
  - Red/black split border: both design and personality aspects
  - Full red border: design-only activation
  - Full black border: personality-only activation
- Changed default bodygraph export format from PNG to SVG for scalability
- Added exaltation/detriment dignity data to `get_hd_data.py` script:
  - Each planet now includes `dignity` field ("exalted", "detriment", or null)
  - Supports synthesis protocol requirement for traceable claims
- Updated protocols:
  - Chart Data Acquisition: Added bodygraph SVG generation step
  - Client Work: Added bodygraph.svg to workflow and file organization
- Generated Szilvia Williams' bodygraph.svg with all new features
- All changes pushed to humandesign_api and VibologyOS repositories

**2026-01-28 (AM):** Human Design API bodygraph renderer improvements
- Replaced PNG triangle images with native SVG paths for exaltation/detriment symbols
- Fixed triangle vertical centering (separate viewBox dimensions for each triangle type)
- Implemented width compensation for equal border padding (exaltation vs detriment)
- Fixed critical API bug: `int(hours)` → `float(hours)` causing incorrect moon calculations
- Triangles now render at 8pt with proper positioning (10px from visible panel borders)
- Documented Gate 23.4 detriment discrepancy in EXALTATION_ERRATA.md

**2026-01-27:** Major repository cleanup and health assessment
- Comprehensive library audit (747 files, 99.9% cross-refs, 0 dead links)
- Deleted 33 temp scripts from root
- Archived 34 maintenance scripts from System/Scripts
- Archived completed plans and abandoned audits
- Updated CLAUDE.md to V4.4
- Relocated Consultations to ~/Business/
- Fresh NEXT.md (archived 64KB historical version)

---

*For historical work logs, see `.archive/System/NEXT-archive-2026-01-27.md`*
