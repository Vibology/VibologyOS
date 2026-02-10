# Current Work Context

**Last Updated:** 2026-02-10
**Current Phase:** Foundation-building — still on the roof, still in observation

---

## System Health Summary

### Library (800 files + 1 synthesis)

| Metric | Value |
|--------|-------|
| Total Files | 802 (800 Library + 1 Synthesis + 1 Template) |
| Cross-References Coverage | 100% (800/800 files) |
| Dead Wikilinks | 5 (all `[[Relevant Entry]]` template placeholders) |
| YAML Compliance | 100% |
| Inline Footnotes Coverage | 100% (800/800 files) |
| Endmatter Standardization | 100% (800/800 files) |
| verified: true | 800/800 (100%) |
| source_verified: true | 800/800 (100%) |
| Stub Files | 0 |

### Observatory (macOS app)

| Component | Status |
|-----------|--------|
| Chart viewing | Bodygraph + Natal Chart SVG rendering |
| Client overview | Birth data, Type, Authority, Profile, Cross, Centers, Channels |
| Client profile tab | Contact info, emergency contact, address, photo, auto-save, edit/read toggle |
| Contextual lookup | All chart data values link to library entries |
| Synthesis viewer | Scans Synthesis/ folder, displays markdown with proper typography |
| Library editor | Edit/reader mode toggle (Cmd+E), save with validation (Cmd+S), unsaved changes protection |
| Print system | Dynamic pagination, orientation support (portrait/landscape), aspect-fit scaling |
| New client creation | Location autocomplete, pre-resolved coordinates to Cartographer |
| Build warnings | 0 |
| Code audit | Complete — all 33 items resolved across 4 phases (2026-02-10) |
| Test coverage | 64 tests across 6 test suites (up from 21) |
| Swift 6 readiness | Sendable on all model structs, @MainActor isolation, StrictConcurrency enabled |
| Dev tooling | Apple Docs MCP server (live SwiftUI/AppKit/Foundation lookup + WWDC transcripts) |

### Cartographer (API)

| Component | Status |
|-----------|--------|
| Astrology | Kerykeion/Swiss Ephemeris, natal chart SVG generation |
| Human Design | Full IHDS calculation, dignity system (exalted/detriment/juxtaposed) |
| Geocoding | Nominatim with NFC Unicode normalization |
| Bodygraph | SVG generation with dignity symbols in planetary panels |
| Portrait chart | Refined layout with compact 18px typography, aligned grids, dark mode optimized |

### Repository Structure

```
VibologyOS/
├── CLAUDE.md (V4.8)
├── Library/ (800 files)
├── Synthesis/General/ (1 exemplar synthesis + template)
├── System/
│   ├── NEXT.md (this file)
│   ├── Protocols (6 active)
│   ├── Templates (manifests + semantic system)
│   ├── Scripts (11 tools: chart calculation + link maintenance + endmatter)
│   ├── Cartographer/ (unified archetypal mapping engine — astrology + HD)
│   └── Audit Logs/
└── .archive/ (three NEXT.md archives)

~/Observatory/           — macOS SwiftUI application (separate git repo)
~/Business/Consultations/ — Client work (outside synthesis engine)
~/Personal/Practice/      — Practitioner-specific protocols
```

---

## Open Questions

- **Client report system (pending service design):** Infrastructure is ready — modular HTML sections → PDF pipeline, light-mode chart assets already generated, WKWebView PDF capture + Core Graphics pagination proven. Architecture: atomic page sections (cover, bodygraph, natal chart, aspects, tarot/oracle, synthesis) that compose into report bundles per service offering. JS-based pre-pagination for intelligent page breaks on flowing text sections. Blocked on: defining core service tiers and which systems each offering includes. Tarot & Oracle content comes from live session — need to determine how that gets captured/structured. Sitting with this.
- **Observatory ceiling:** The app now has viewing + editing capability for library entries. The question remains whether it should grow to include structured cross-referencing, composite chart comparison, transit overlays, or in-app synthesis generation. External git workflow still handles commits. No rush — emotional wave decision.

---

## Immediate Next Actions

**Future consideration (not imminent):**
- Self-hosted AI server (waiting on GPU/RAM price shifts or undeniable necessity)

---

## Recent Session Summary (2026-02-10 late night)

### Observatory build, install, and refinements
- **Built and installed Observatory** to `/Applications/Observatory.app` (Release configuration via xcodebuild)
- **Date input field redesign:** Replaced single MM/DD/YYYY text field with three separate tabbable fields (MM / DD / YYYY). Manual tab navigation between fields, digits-only input filtering, proper date composition.
- **Bodygraph magenta color harmonization:** Updated dark mode design colors to match Synthwave heading palette warm magenta (#FF38B3). Changed `DARK_DESIGN_TEXT` (#FF40BF → #FF38B3), `DARK_DESIGN_HEADER` (#FF66CC → #FF5CC6), panel borders (#DD44BB → #DD309F).
- **Report generation planning:** Explored Pages integration (viable via ScriptingBridge but fragile for production use). Decided on HTML/CSS → PDF pipeline with modular page sections and JS-based intelligent pagination. Pending: service tier definition before template design.
- **Library editor save fix:** `toggleEditMode()` was calling `exitEditMode(saveFirst: false)`, silently discarding edits. Changed to `saveFirst: true` — exiting edit mode now auto-saves.
- **Scroll wheel fix:** WKWebView in SVGView was capturing scroll events, blocking parent ScrollView in Bodygraph and Natal Chart tabs. Added `NonScrollingWebView` subclass that forwards `scrollWheel` to the responder chain.
- Commits: Observatory (`cd345f6` date field, `ca37f23` save fix, `04717e7` scroll fix), Cartographer (`38f33a4` magenta)

---

## Recent Session Summary (2026-02-10 night)

### Observatory code audit — Phase 1-4 comprehensive sweep
Second audit session resolving all 33 remaining items from the 5-agent parallel audit.

- **Phase 1 — Concurrency Isolation (7 items):** Added `@MainActor` to LibraryViewModel, ClientStore, ClientViewModel, LibraryIndex, SearchEngine, TreeNode. Fixed LibraryEntry Hashable to use only `id`. Removed 5+ `MainActor.run {}` blocks, made `exitEditMode`/`toggleEditMode`/`saveCurrentEntry` synchronous.
- **Phase 2 — Correctness Fixes (12 items):** ProfileViewModel fire-and-forget fix, Cmd+E/Cmd+N shortcut conflicts resolved, WebViewPrinter coordinator type filtering, Package.swift resource declarations, duplicate Ascendant row removed, MarkdownWebView change detection, WikilinkParser NSRange fix, YAML escaping, `</script>` injection fix, ClientNotesTab task leak fix, FrontmatterParser POSIX locale.
- **Phase 3 — Test Coverage (6 items):** 3 new test files (LibraryLoaderTests 8 tests, MarkdownRendererTests 17 tests, LibraryWriterTests 5 tests). Expanded FrontmatterParserTests (+3), SearchEngineTests (+4), WikilinkParserTests (+6). Total: 21 → 64 tests.
- **Phase 4 — Polish & Cleanup (14 items):** Sync I/O moved off main thread (LibraryLoader, startEditing), cache eviction for ClientStore, deterministic resolveByPrefix, LibraryLink → Button for accessibility, accessibility labels on 4 view components, static countries array, color deduplication (NSColor source of truth), dead needsBlockSeparator removal, private API drawsBackground replaced, Pillar.accentColor moved to view layer, unused directoryPath removed, StrictConcurrency enabled.
- Net result: +107/-116 lines (Phase 4), +614/-106 lines (Phases 1-3), 0 errors, 0 warnings, 64/64 tests passing
- 42 files changed across 2 commits
- Commits: Observatory `8ea4e55`, `629ef36`, `e00f345` (audit doc)

---

## Recent Session Summary (2026-02-10 evening)

### Observatory code audit — initial sweep
- Comprehensive audit of all 50 source files (~7,300 lines) against current Swift/SwiftUI standards
- **HIGH (5 fixes):** Deleted duplicate root LibraryWriter.swift, moved markdown rendering out of body getter into `.task(id:)`/`.onChange`, cached DateFormatters and NSRegularExpressions as static lets, consolidated sign/center formatting into LibraryLookup (DRY)
- **MEDIUM (7 fixes):** Async client loading via `Task.detached` (file I/O off main thread), replaced blocking `waitUntilExit()` with `process.terminationHandler` in ChartCalculationService, replaced `NSMutableArray` with Sendable `DataBox`, removed dead CDN fallback + cached bundled marked.js, tracked SVG URL in Coordinator instead of unreliable `webView.url`, added `@MainActor` to WebViewPrinter (removed `nonisolated(unsafe)`), removed Cmd+E shortcut conflict in Notes tab
- **LOW (4 fixes):** Cached DateFormatters in FrontmatterParser/ClientNotesTab, added `Sendable` to all 22 model structs (Swift 6 readiness), harmonized regex initialization pattern (`try!` for constant patterns)
- Net result: -600 lines, 0 errors, 0 warnings, 21/21 tests passing
- 30 files changed across Models, Services, ViewModels, Views
- Commit: Observatory `1015961`

---

## Recent Session Summary (2026-02-10)

### Client Profile tab and chart extraction automation
- **Profile tab (new):** Full client profile management as first tab in client panel
  - Contact info (email, phone), mailing address with country dropdown, emergency contact, practice info
  - Profile photo with file picker (copies image to client folder)
  - Edit/read mode toggle with debounced auto-save (1.5s delay, saves to profile.json)
  - Proper binding helpers for nested optional structs (address, emergency contact)
  - `.allowsHitTesting` instead of `.disabled` to prevent photo darkening in read mode
- **Natal chart extraction:** Automated wheel-dark.svg and aspects-dark.svg extraction from portrait-dark.svg
  - ViewBox cropping: wheel (0 0 800 800), aspects (0 1370 800 830)
  - Runs automatically during `generate_chart_visuals.py`
- **Astrology data expansion:** Added Chiron, South Node, and Lilith to get_astro_data.py extraction
- **Contextual data fixes:** Lowercase JSON key mappings for planets/houses, expandSignName helper
- **Cosmetic:** White section titles in bodygraph/natal chart tabs, label alignment (.leading), form field layout
- **Dev tooling:** Installed Apple Docs MCP server (`@kimsungwhee/apple-docs-mcp`) for live SwiftUI/AppKit/Foundation documentation lookup + WWDC transcripts (2014-2025). Installed Node.js via Homebrew as prerequisite.
- Modified ~15 files across Observatory and Cartographer
- Commits: Observatory `5749945` through `6a194de`

---

## Recent Session Summary (2026-02-09 late evening)

### Bodygraph dark mode — Comprehensive luminous redesign
- Complete ground-up rethink of dark mode aesthetic: "stained glass in a dark cathedral" — elements glow from within against darkness
- **Critical fixes from screenshot review:**
  - V1 attempt: Incremental adjustments failed — illegible gate numbers, invisible Personality panel text, unclear structure
  - V2 solution: Abandoned light-mode adaptation, embraced dark mode as its own aesthetic with inverted luminosity hierarchy
  - V3 refinement: Gate numbers corrected (black text on white circles), activation colors unified with panels
- **Core principle:** High contrast, vibrant accents, clear hierarchy. Bright elements on dark background, not dimmed light theme.
- **Color unification:** Channels and gate activations match panel text colors for coherent visual system
- **V4 refinement:** Activation colors changed from coral/cyan to magenta/electric blue to eliminate visual confusion with Sacral (coral) and Spleen (teal) center colors
- **V5 polish:** Panel colors updated to match activation colors (magenta panels for Design, electric blue for Personality) for complete visual coherence
- **V6 revision:** Center colors redesigned as rich jewel tones (deep amethyst, jade, coral, gold, etc.) — muted enough to not compete with activations, saturated enough to be beautiful. Aged stained glass aesthetic creates proper visual hierarchy: Activations (magenta/blue) dominate, centers support.

**Color Palette (Luminous Dark Mode):**
- **Body structure:** #404040 fill, #808080 stroke (medium gray, bright outline — clearly defined silhouette)
- **Body glow:** #555555 outer, #4A4A4A inner (stronger emanation reveals anatomical structure)
- **Undefined channels:** #888888 inactive, #666666 glow (quite visible — full channel anatomy now readable)
- **Undefined centers:** #2A2A2A fill, #606060 stroke (darker than body creates depth, visible borders)
- **Gate numbers:** #FFFFFF active (pure white, maximum contrast), #CCCCCC inactive (very light gray)
- **Defined centers (Rich Jewel Tones - Muted but Beautiful):** Deep, sophisticated colors that support rather than compete with activations
  - Head: #AA77DD (deep amethyst), Ajna: #8899CC (deep indigo), Throat: #6699DD (deep cerulean)
  - G: #EEBB66 (deep gold), Heart: #77CC99 (deep emerald), Solar Plexus: #EEBB77 (deep amber)
  - Spleen: #66BBAA (deep jade), Sacral: #EE9988 (deep coral), Root: #BB8866 (deep sienna)
  - Philosophy: Aged stained glass aesthetic — rich, restrained, luxurious

**Panel Text & Activations (Fully Unified Magenta/Electric Blue System):**
- **Design:** Warm magenta (#FF38B3, matches Synthwave heading palette) for text, channels, and gate borders. Lighter warm magenta header (#FF5CC6), deep magenta tint background (#2A182A), warm magenta panel border (#DD309F), magenta cell dividers (#442240)
- **Personality:** Electric blue (#4488FF) for text, channels, and gate borders. Bright electric blue header (#66AAFF), deep blue tint background (#1A2035), electric blue panel border (#5588DD), blue cell dividers (#2A3550)
- **Why it works:** Single color per aspect creates fully coherent visual system from top to bottom. Magenta and electric blue are distinct from ALL center colors (avoiding coral/Sacral and cyan/Spleen confusion). Panels, channels, borders, and text all speak the same color language. Maximum visual clarity and professional polish.

**Visual hierarchy (bright → dark):**
1. Active gates (white) — most important
2. Defined centers (vibrant colors) — second focus
3. Panel text (bright accents) — readable data
4. Active channels (red/black) — clear activations
5. Body structure (medium gray) — visible framework
6. Undefined channels (light gray) — anatomical context
7. Undefined centers (darker gray) — depth
8. Background (darkest) — recedes

- **Script updates:** `generate_chart_visuals.py` exports both `bodygraph.svg` (light) and `bodygraph-dark.svg` (dark)
- **Observatory integration:** ClientLoader prefers `bodygraph-dark.svg` (matching `portrait-dark.svg`)
- Modified 3 files: `chart_renderer.py` (+130 lines comprehensive redesign), `generate_chart_visuals.py` (+25 lines), `ClientLoader.swift`
- Ready for commit

---

## Recent Session Summary (2026-02-09 evening)

### Portrait natal chart refinement
- Comprehensive layout and typography improvements to portrait chart generator
- **Typography:** Reduced all text to 18px (header, grids) for more compact presentation
- **Grid positioning:** Aligned all grids (planetary, house, elements, qualities) at same top position (y=921)
- **Symbol scaling:** Proportional symbol reduction (planets: 0.77, zodiac: 0.50, retrograde: 0.85)
- **Dark mode colors:** Updated element/quality percentage colors for readability:
  - Fire/Cardinal: #ffaa66 (bright orange)
  - Earth/Fixed: #e6c49a (bright tan)
  - Air: #a0a8ff (bright periwinkle)
  - Water/Mutable: #dd99ff (bright lavender)
- **Bug fixes:** XML validation error (missing wheel filter closing tag), leading space removal from house degrees
- **Spacing:** Increased viewBox height 40px (1750→1790), moved aspect grids down 40px for breathing room
- Modified 1 file: `portrait_builder.py` (+988 lines comprehensive rewrite)
- Commit: Cartographer `5966161`

---

## Recent Session Summary (2026-02-09 morning)

### Observatory library editor implementation
- Added edit/reader mode toggle to Observatory library viewer
- Features: Cmd+E toggle, Cmd+S save, unsaved changes warning, YAML validation
- Architecture: LibraryWriter service with atomic writes and path validation
- Modified 8 files, added LibraryWriter.swift (+418 lines total)
- Dual-mode MarkdownTextView: rendered attributed string (read) vs plain monospaced editing (edit)
- Entry reload after save syncs changes into LibraryIndex and search index
- External git workflow unchanged (commits still handled outside app)
- Commit: Observatory `38fec3b`

---

## Recent Session Summary (2026-02-08)

### Geocoding fix
- Fixed two geocoding issues affecting accented place names (e.g., Kaposvár, Hungary):
  1. NFC Unicode normalization in `geolocation.py` (macOS NFD decomposition broke Nominatim)
  2. Pre-resolved coordinate pass-through from Observatory → get_hd_data.py → Cartographer API (bypasses redundant Nominatim geocoding of verbose MKLocalSearch autocomplete strings)
- Commits: Cartographer `04b091e`, VibologyOS `4458672`, Observatory `d60a065`

### Print system overhaul
- Resolved all 7 Xcode warnings (Swift 6 concurrency + unused variable)
- Replaced static PDF pagination with dynamic `NSView`-based printing (`PDFContentPrintView`)
- Print dialog now includes orientation selector (`.showsOrientation`)
- Aspect-fit scaling prevents blank second pages when printing charts in landscape
- Commit: Observatory `96af520`

### Cartographer migration (completed)
- `get_hd_data.py` fully migrated from old `humandesign_api` to Cartographer (port 8000, module paths, auth header)
- Old `humandesign_api` submodule archived

### Evening: Scale realization and infrastructure assessment
- Full recognition of project scope: API, app, website, + 800-file Library requiring human curation
- Emotional wave processing through 4/6 observation phase — seeing the actual terrain
- Decision made: Local LLM infrastructure (ollama/qwen) insufficient for synthesis work
- Current dependency: Anthropic API for all synthesis tasks
- Generator response to actual scale: the depth will come through doing the work, not through credentials

---

## Completed Milestones

| Milestone | Date | Scope |
|-----------|------|-------|
| Observatory audit Phase 1-4 | 2026-02-10 | 33 items: concurrency isolation, correctness, 43 new tests, polish, Swift 6 prep |
| Observatory audit initial sweep | 2026-02-10 | 16 items: HIGH/MEDIUM/LOW fixes, async loading, Sendable, -600 lines |
| Client profile tab | 2026-02-10 | Contact info, photo, address, auto-save, edit/read toggle |
| Chart extraction automation | 2026-02-10 | wheel-dark.svg + aspects-dark.svg from portrait-dark.svg |
| Portrait chart refinement | 2026-02-09 | Compact 18px typography, aligned grids, dark mode colors |
| Observatory library editor | 2026-02-09 | Edit/reader mode toggle, atomic writes, YAML validation, Cmd+E/S shortcuts |
| Print system overhaul | 2026-02-08 | Dynamic pagination, orientation support, zero warnings |
| Geocoding fix for accented names | 2026-02-08 | NFC normalization + coordinate pass-through |
| Cartographer migration complete | 2026-02-08 | get_hd_data.py ported to Cartographer API |
| Observatory contextual lookup | 2026-02-08 | Client overview chart data → library navigation |
| Observatory synthesis viewer | 2026-02-08 | Viewer-only synthesis tab (CLI generates, GUI displays) |
| First exemplar synthesis | 2026-02-08 | "The 4/6 Profile" across seven systems |
| Library 100% source-verified | 2026-02-08 | All 800 files have primary source validation |
| Library 100% verified | 2026-02-07 | All 800 files passed coherence review |
| Cross-references 100% | 2026-02-07 | All placeholder text replaced |
| Inline footnotes 100% | 2026-02-07 | All files have inline citations |
| Endmatter standardization 100% | 2026-02-07 | Scholarly "Notes" convention applied |
| IHDS dignity calculation | 2026-02-07 | Complete algorithm with gate-level fixing |
| Astrolabe oracle deck canonized | 2026-02-04 | 88 cards production-ready |

---

## Reference

| Document | Purpose |
|----------|---------|
| `CLAUDE.md` | Core governance (V4.8) |
| `PROTOCOL - Client Work.md` | Full client workflow |
| `PROTOCOL - Chart Data Acquisition.md` | Chart calculation |
| `RUBRIC - Library Content Standard.md` | Quality tiers |
| `GUIDE - Synthesis Quick Start.md` | Template selection, quality standards |

---

*For historical work logs, see `.archive/System/NEXT-archive-2026-02-08.md` and earlier archives.*
