# VibologyOS Desktop Application — Concept Document
*Native macOS App for Practitioner Synthesis Work*

**Date:** 2026-02-07
**Status:** Conceptual — not yet in development
**Purpose:** Personal tool for client work and individual practice (not a product for sale)

---

## Core Principle

**The app supports the practitioner — it doesn't replace him.**

Vibology isn't a system to sell. The practitioner is what clients receive: the unique design, the ability to hold space, the capacity to communicate archetypal patterns in language that's meaningful and accessible. The app makes the mechanical work (charts, lookup, data management) effortless so all energy goes into synthesis and presence.

---

## The Core Loop

1. **Client comes to you**
2. **Calculate their charts** (HD + Astrology) → App handles this
3. **Look at the data through instruments** (the Library) → App makes this seamless
4. **Synthesize** — the part that's uniquely you, the part no app replaces
5. **Hold space and communicate** what you see
6. **Keep notes** on what emerged, for continuity → App makes this frictionless

**The app serves steps 1-3 and 6. Steps 4-5 are the practitioner's work.**

---

## Technology

### Platform
- **macOS native** — SwiftUI as primary framework
- **AppKit** where needed (rich text editing, complex UI components)
- **Python interop** — call existing chart calculation scripts via Process

### Why SwiftUI
- Native macOS look and feel (not a web app in a wrapper)
- Sidebar navigation, split views, data tables — all native
- SwiftData/Core Data for client persistence
- Markdown rendering for Library files and session notes
- SVG rendering for bodygraphs
- HTTP capability for Claude API integration

### Existing Infrastructure (Reusable)
- `System/Scripts/get_hd_data.py` — Human Design chart calculation (Kerykeion + HD API)
- `System/Scripts/get_astro_data.py` — Astrology chart calculation (Swiss Ephemeris)
- `System/Scripts/generate_bodygraph_svg.sh` — Bodygraph SVG generation
- `humandesign_api/` — HD API submodule (auto-starts if not running)
- `Library/` — 802 reference files, fully cross-referenced and cited

---

## Modules (Conceptual)

### 1. Client Management
- Client list (sidebar, searchable)
- Client detail view (profile, charts, session history)
- Add client: name, birth date/time/location
- Archive inactive clients
- Database: SQLite via SwiftData or Core Data
- Privacy: entity_id system for anonymization

### 2. Chart Calculation
- Input: Birth data form (name, date, time, location with geocoding)
- Process: Call bundled Python scripts
- Output: HD JSON, Astrology JSON, Bodygraph SVG
- Display: Interactive chart viewer
  - Click a Gate → opens Reference Library entry
  - Click a Center → opens Center description
  - Click a Channel → opens Channel entry
- Save to client profile automatically

### 3. Reference Library Browser
- Load VibologyOS `Library/` markdown files (read-only)
- Navigate by pillar (sidebar tree or tabs)
- Full-text search across all 802 files
- Wikilink navigation (click `[[Gate 12]]` → opens that entry)
- Quick lookup panel (accessible from any module — side panel or popover)
- Tag-based filtering

### 4. Synthesis Workspace
- Markdown editor for session notes and synthesis documents
- Split view: Library lookup panel alongside workspace
- Template system (Initial Reading, Follow-up, Relational, Profile Deep Dive)
- Optional: Claude API integration for AI-assisted synthesis
- Save synthesis to client record

### 5. Session Notes
- Dated session entries per client
- Markdown with inline wikilinks to Library
- Session type tagging (initial, follow-up, relational)
- Follow-up items / action tracking

### 6. Settings
- Anthropic API key (optional — for AI synthesis)
- Data storage location
- Backup preferences
- Export format preferences (PDF template)

---

## Data Architecture (Proposed)

```
~/VibologyOS/                          Reference Library (read-only in app)
  ├── Library/                         802 markdown files across 7 pillars
  ├── Synthesis/                       General synthesis templates
  └── System/                          Protocols, scripts, templates

~/VibologyOS-AppData/                  Application data (app-managed)
  ├── VibologyOS.sqlite                Client database
  ├── Charts/
  │   ├── {client_id}/
  │   │   ├── humandesign.json
  │   │   ├── astrology.json
  │   │   └── bodygraph.svg
  ├── Sessions/
  │   ├── {client_id}/
  │   │   ├── 2026-02-07-initial-reading.md
  │   │   └── 2026-03-15-follow-up.md
  ├── Syntheses/
  │   ├── {client_id}/
  │   │   ├── profile-synthesis.md
  │   │   └── cross-system-integration.md
  └── Backups/
```

**Separation of concerns:**
- VibologyOS Library = universal reference (unchanged, git-tracked)
- AppData = professional client work (app-managed, backed up separately)
- Personal practice = separate Obsidian vault (`~/Observatory/`) — not in app

---

## UI Sketch (Conceptual)

```
┌──────────────────────────────────────────────────────────────────┐
│ VibologyOS                                              ⚙️      │
├──────────────┬───────────────────────────────────────────────────┤
│              │                                                   │
│ CLIENTS      │  John Doe — Initial Reading                      │
│              │                                                   │
│ ▸ John Doe   │  ┌─────────────┬─────────────────────────────┐   │
│   Jane Smith │  │ BODYGRAPH   │ SESSION NOTES               │   │
│   [+ New]    │  │             │                             │   │
│              │  │  [SVG]      │ ## Type & Strategy          │   │
│──────────────│  │             │                             │   │
│              │  │  Type: MG   │ John is a Manifesting       │   │
│ LIBRARY      │  │  Auth: Emo  │ Generator with Emotional    │   │
│              │  │  Prof: 3/5  │ Authority...                │   │
│ ▸ Human      │  │  Def: Split │                             │   │
│   Design     │  │             │ See [[Emotional Authority]] │   │
│ ▸ Tarot      │  │  [Full      │                             │   │
│ ▸ Astrology  │  │   Chart]    │                             │   │
│ ▸ Angelology │  │             │                             │   │
│ ▸ Personal   │  └─────────────┴─────────────────────────────┘   │
│   Mythos     │                                                   │
│ ▸ Magdalene  │  PREVIOUS SESSIONS                               │
│ ▸ Astrolabe  │  • 2026-02-07 Initial Reading                    │
│              │  • 2026-03-15 Follow-up                          │
│              │                                                   │
└──────────────┴───────────────────────────────────────────────────┘
```

---

## Development Approach

### Philosophy: Discovery Through Use (29-46)

Build the simplest thing that supports the core loop. Use it. Discover what's missing. Expand. Don't over-plan — let the tool reveal what it needs to become through practice.

### Phase 1: Foundation
- Client list + detail view
- Chart calculation (call Python scripts)
- Bodygraph display (SVG rendering)
- Basic session notes (markdown editor)

### Phase 2: Library Integration
- Reference Library browser (load markdown, render wikilinks)
- Quick lookup panel (accessible during synthesis)
- Search across Library

### Phase 3: Synthesis Support
- Template system for session types
- Split-view workspace (Library + notes side by side)
- Export to PDF

### Phase 4: AI Integration (Optional)
- Claude API for synthesis assistance
- Context-aware suggestions (client chart data + Library)

### Phase 5: Discovery
- Whatever the 29-46 reveals through use

---

## Personal Practice (Separate from App)

The practitioner's personal spiritual practice (Magdalene Path, Bough tracking, kenosis audits, contemplative prayer, Uriel work) lives in a **separate Obsidian vault** (`~/Observatory/`), not in the app. The app is a professional tool for client work. Personal practice is private.

**Migration from VibologyOS to Observatory:**
- `Daily Practice Quick Reference.md` → Observatory
- `Practitioner Protocols.md` → Observatory
- `Practices and the Lunar Cycle.md` → Evaluate (may stay as universal teaching)

**VibologyOS Magdalene Path files** edited to remove practitioner-specific "FOR YOU" language, reframed as universal teachings.

---

## Open Questions (To Resolve During Development)

1. **Markdown editor:** SwiftUI-native or AppKit-based? (Depends on needed features)
2. **Chart interactivity:** How clickable should the bodygraph be? (Simple links vs. full interactive viewer)
3. **AI synthesis:** How much AI assistance is helpful vs. intrusive? (Discover through use)
4. **Backup strategy:** Time Machine sufficient, or app-level backup?
5. **Export format:** PDF only, or also HTML/DOCX for client reports?
6. **Search depth:** Full-text only, or semantic search (AI-powered)?
7. **Relational charts:** Synastry/composite support needed? (Probably yes, eventually)
8. **Transit tracking:** Real-time transit display for client charts? (Phase 5 territory)

---

*This document is a conceptual anchor — not a specification. The app will reveal itself through the process of building and using it.*
