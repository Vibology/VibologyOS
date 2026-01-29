---
tags: [system, protocol, data-integrity, astrology, human-design]
date_created: 2026-01-15
date_updated: 2026-01-28
---

# Protocol: Chart Data Acquisition

This protocol ensures **chart data integrity** for all synthesis work involving Astrology and Human Design. It addresses Process Gap #1 (critical data integrity issues) and incorporates lessons learned from the Szilvia Williams synthesis audit.

## Protocol Scope

This protocol governs **technical chart calculation and data integrity**:
- Calculation tool usage, scripts, and command syntax
- Data verification methodology and spot-checking
- Error handling and troubleshooting (API failures, geocoding issues)
- Transit calculation mandates (THE CARDINAL RULE)
- Environment setup and dependency management

**Client workflow and synthesis** (intake, question documentation, privacy, delivery, archival) are governed by `PROTOCOL - Client Work.md`.

## Core Principle

**NEVER hallucinate or infer astronomical data.** Every planetary position, every transit date, every timing claim MUST be calculated using verified tools and traceable to a source JSON file.

### THE CARDINAL RULE: ALWAYS CALCULATE TRANSITS

**IF THE CLIENT ASKS ANYTHING INVOLVING TIMING, YOU CALCULATE TRANSITS. PERIOD.**

Questions that REQUIRE transit calculation:
- "When will X happen?"
- "What are the prospects in the next N years?"
- "Is this a good time for Y?"
- "When should I Z?"
- Any question involving future timing, windows, or opportunities

**There is NO EXCUSE for vague timing language.**

❌ **WRONG:** "Transits matter. I can't predict exact timing without running transits, but here's what I know..."
✅ **CORRECT:** Run `get_transit_data.py`, calculate the transits, provide exact dates.

❌ **WRONG:** "Jupiter will expand things when it transits your 7th House (probably in a few years)."
✅ **CORRECT:** "Jupiter enters Virgo (your 7th House) on July 26, 2027 and transits through August 24, 2028."

❌ **WRONG:** "The next 5 years are a transitional window."
✅ **CORRECT:** "Saturn transits your 2nd House Feb 2026-Apr 2028. Jupiter transits your 7th House July 2027-Aug 2028. Here's what each means..."

**This is not optional. This is the entire point of having calculation tools.**

## Problem Statement

Chart data manually entered or inferred during synthesis leads to errors:
- Contradictory center definitions (Defined/Undefined flipped)
- Saturn timing errors (off by 12+ months)
- North Node axis completely wrong (wrong sign entirely)
- Transit dates inferred instead of calculated

**Root Cause:** No verification step between data gathering and synthesis. Transit data trusted from memory/inference instead of calculated from ephemeris.

## Solution Architecture

Three local, free, self-hosted tools provide precise calculations:

| System | Tool | Script | Engine |
|--------|------|--------|--------|
| Geolocation | Nominatim + timezonefinder | `verify_geolocation.py` | OpenStreetMap + pytz |
| Astrology (Natal) | Kerykeion | `get_astro_data.py` | Swiss Ephemeris |
| Astrology (Transits) | Kerykeion | `get_transit_data.py` | Swiss Ephemeris |
| Human Design | humandesign_api | `get_hd_data.py` | Swiss Ephemeris + HD formulas |

**Cost:** $0 (all open-source)
**Data Privacy:** All calculations run locally (no external API calls for chart data)

---

## Pre-Requisites

### Environment Setup (One-Time)

VibologyOS uses a **virtual environment** to isolate Python dependencies and prevent conflicts with system packages. This protects against dependencies being removed during system updates.

**Location:** `.venv/` (in VibologyOS root directory)
**Dependencies:** Managed via `◈ System/Scripts/requirements.txt`

#### Initial Setup

```bash
# Navigate to VibologyOS root
cd ~/VibologyOS

# Create virtual environment (if it doesn't exist)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install required dependencies
pip install -r "◈ System/Scripts/requirements.txt"

# Verify installations
python -c "from kerykeion import AstrologicalSubject; print('Kerykeion OK')"
python -c "import httpx; print('HTTPX OK')"

# Test scripts
"◈ System/Scripts/calculate_chart.sh" astrology --help
"◈ System/Scripts/calculate_chart.sh" humandesign --help
```

#### Reinstalling After System Updates

If system updates remove dependencies or break the virtual environment:

```bash
cd ~/VibologyOS

# Option 1: Reinstall dependencies (usually sufficient)
source .venv/bin/activate
pip install -r "◈ System/Scripts/requirements.txt"

# Option 2: Rebuild virtual environment from scratch (if corrupted)
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r "◈ System/Scripts/requirements.txt"
```

#### Dependencies List

**Core (required):**
- `kerykeion` - Astrology calculations via Swiss Ephemeris
- `httpx` - Human Design API client

**Optional (geolocation verification):**
- `geopy` - Geocoding (install system-wide: `sudo apt install python3-geopy`)
- `timezonefinder` - Timezone from coordinates (install via pip if needed)

**Note:** The wrapper script `calculate_chart.sh` automatically activates the virtual environment, so you don't need to manually activate it for chart calculations.

### Human Design API Server

The HD API must be running for Human Design calculations:

```bash
# Start the HD API server (runs on port 9021)
cd "◈ System/humandesign_api"
source "../Scripts/.venv/bin/activate"
uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &

# Verify it's running
curl -s http://127.0.0.1:9021/health | python3 -m json.tool
```

---

## Data Acquisition Workflow

### Phase 1: Gather Birth Data (Scribe Mode)

**Birth data collection is governed by `PROTOCOL - Client Work.md` Phase 0.1**, which defines:
- Required fields (name, date, time, location)
- Time precision levels (Exact, Approximate, Rectified, Unknown)
- Implications for chart calculation

**For chart calculation purposes, you need:**
- **Name** (for identification in output files)
- **Birth Date:** Year, Month, Day
- **Birth Time:** Hour, Minute (local time at birth location)
- **Birth Location:** City, Country (for geolocation verification and chart rendering)

### Phase 1b: Geolocation Verification (MANDATORY)

**ALWAYS run geolocation verification before chart calculation:**

```bash
cd "◈ System/Scripts"
source .venv/bin/activate

python verify_geolocation.py \
  --place "Kaposvar, Hungary" \
  --birth-date 1976-05-17 \
  --output location_verification.json \
  --pretty
```

**The script will:**
1. Geocode the place name to coordinates
2. Determine the correct IANA timezone
3. Calculate UTC offset for the birth date (with historical DST awareness)
4. Present results for user verification
5. Allow manual corrections if needed

**Output includes:**
- Resolved latitude/longitude
- Timezone (e.g., "Europe/Budapest")
- UTC offset at birth date
- DST status (important: rules vary by era!)
- Verification status

**CRITICAL:** Do NOT proceed to chart calculation until geolocation is verified. Historical DST rules differ from modern rules (e.g., Hungary had no DST from 1957-1979).

### Phase 2: Calculate Natal Charts

Use the **verified coordinates and timezone** from Phase 1b.

#### Astrology Natal Chart

```bash
python get_astro_data.py \
  --name "Subject Name" \
  --year 1976 \
  --month 5 \
  --day 17 \
  --hour 4 \
  --minute 4 \
  --lat 46.356469 \
  --lng 17.788689 \
  --timezone "Europe/Budapest" \
  --pretty > astrology.json
```

**Output includes:**
- All planet positions (Sun through Pluto, nodes, Chiron)
- House cusps (Placidus)
- Ascendant and Midheaven
- Retrograde status
- Absolute zodiac positions (for transit calculations)

#### Human Design Natal Chart

```bash
python get_hd_data.py \
  --name "Subject Name" \
  --year 1976 \
  --month 5 \
  --day 17 \
  --hour 4 \
  --minute 4 \
  --place "Kaposvar, Hungary" \
  --pretty > humandesign.json
```

**Output includes:**
- Energy Type, Strategy, Signature, Not-Self
- Inner Authority
- Profile
- Incarnation Cross
- Definition Type
- Defined/Undefined Centers
- Channels and Gates (with exaltation/detriment dignity for each planet)
- Variables

**Note on Exaltations/Detriments:** Each planet in the gates arrays includes a `dignity` field with values:
- `"exalted"` - Planet is exalted in this gate.line
- `"detriment"` - Planet is in detriment in this gate.line
- `null` - No dignity status for this placement

#### Chart Visualizations (Bodygraph and Natal Chart)

After generating `humandesign.json` and `astrology.json`, generate chart visualizations:

```bash
cd ~/VibologyOS
source .venv/bin/activate

# Generate both bodygraph.svg and natal chart SVG
python3 System/Scripts/generate_chart_visuals.py --output-dir ~/Business/Consultations/ClientName/
```

**Alternative usage:**
```bash
# Generate in current directory (if JSON files are in pwd)
python3 System/Scripts/generate_chart_visuals.py

# Generate only bodygraph
python3 System/Scripts/generate_chart_visuals.py --bodygraph-only

# Generate only natal chart
python3 System/Scripts/generate_chart_visuals.py --natal-only
```

**Outputs:**
- `bodygraph.svg` - HD bodygraph showing:
- Defined/undefined centers with luminous glow effects
- Active channels (all rendered, including split-aspect patterns)
- Gate numbers with activation-type indicators:
  - **Red/black split border**: Both design and personality aspects
  - **Full red border**: Design-only activation
  - **Full black border**: Personality-only activation
- Design and Personality side panels with planetary activations
- `{Name} - Natal Chart.svg` - Astrological natal chart with planetary positions, houses, aspects

**Format rationale:** SVG is the required format for all chart visualizations:
- Scalability without quality loss
- Clean import into Pages/design tools
- Smaller file size for archival
- Professional print quality

### Phase 2b: Calculate Transits (MANDATORY for ANY Timing-Related Questions)

**THIS PHASE IS NON-NEGOTIABLE IF THE CLIENT ASKS ABOUT TIMING.**

If the synthesis involves:
- Future opportunities or challenges ("What are my prospects for X?")
- Timing windows ("When will Y happen?" or "What about the next Z years?")
- Life transitions or thresholds ("What happens at age 50?")
- Career or relationship timing ("Can I make a living doing this?" "Will I find love?")
- ANY question that could involve "when" or "in the next N years"

**YOU MUST CALCULATE TRANSITS BEFORE WRITING THE SYNTHESIS.**

Do not write vague statements like "transits matter but I can't predict timing." That is a violation of this protocol. The entire point of having `get_transit_data.py` is to provide EXACT TIMING.

```bash
python get_transit_data.py \
  --start-date 2026-01-01 \
  --end-date 2028-12-31 \
  --natal-file astrology.json \
  --pretty > transits.json
```

**Output includes:**
- Current planetary positions (with HD gate context)
- All sign ingresses in date range (exact dates)
- Planetary returns (Saturn return, Chiron return, etc.)
- Multiple passes noted for retrograde periods

**Example: Find specific ingress dates:**
```bash
# When does Saturn enter Aries?
python get_transit_data.py --ingress-planet saturn --start-date 2025-01-01 --end-date 2030-01-01 --pretty

# When is the Chiron return for natal Chiron at 29.40°?
python get_transit_data.py --return-planet chiron --natal-position 29.40 --start-date 2025-01-01 --end-date 2028-01-01 --pretty
```

**CRITICAL:**
- NEVER state a transit date without calculating it first
- NEVER infer when a planet enters a sign - calculate it
- NEVER assume modern DST rules for historical dates
- ALL dates in synthesis MUST be traceable to `transits.json`

### Phase 3: Verification (Critical)

**Present raw data to user for spot-check:**

1. **Geolocation Check:**
   - Coordinates look reasonable for the city?
   - Timezone matches expected region?
   - DST status correct for that era?

2. **Astrology Quick Check:**
   - Sun sign matches expected?
   - Moon sign reasonable for date?
   - Saturn position consistent with known Saturn return timing?

3. **Human Design Quick Check:**
   - Type makes sense for the person?
   - Defined centers list is consistent (no contradictions)?
   - Profile feels accurate?

4. **Transit Quick Check (if applicable):**
   - Ingress dates match astronomical almanacs?
   - Return dates are within expected age ranges?

**If discrepancies found:**
- Re-verify birth data with user
- Re-run geolocation verification
- Re-run calculations
- Document any corrections

### Phase 4: Save Data Files

**File organization is governed by `PROTOCOL - Client Work.md` Phase 4.1**, which defines:
- Canonical directory structure for client folders
- Permanent vs. synthesis-specific file placement
- Rationale for SVG format visualizations
- Git commit protocols

**Output from this protocol:**
- `astrology.json` - Natal chart data with city/nation metadata
- `humandesign.json` - HD chart data with dignity annotations
- `bodygraph.svg` - HD bodygraph visualization (SVG format)
- `location_verification.json` - Geolocation verification (if performed)
- `transits.json` - Transit calculations (if timing questions exist)

Place these files according to Client Work Protocol Phase 4.1 structure.

---

## Verification Checklist

**MANDATORY:** Complete the verification checklist before finalizing any synthesis.

Template location: `◈ System/Templates/_TEMPLATE - Synthesis Verification Checklist.md`

Copy this template to the synthesis subfolder and complete all items:
- [ ] Geolocation verified
- [ ] Natal charts calculated (not inferred)
- [ ] Transits calculated (not inferred)
- [ ] All claims traceable to source files
- [ ] No vague timing language without bounds

---

## Error Handling

### API Failure Handling

**If HD API is down:**
```bash
# Check status
python get_hd_data.py --check

# If unreachable, restart:
cd "◈ System/humandesign_api"
pkill -f "uvicorn humandesign"
source "../Scripts/.venv/bin/activate"
uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &
```

**Graceful Degradation:** If HD API cannot be started, complete Astrology portion and flag HD data as incomplete.

### Geocoding Failure Handling

If geocoding fails:
1. Try alternative place name formats (e.g., "Kaposvár" vs "Kaposvar")
2. Use manual coordinates from Google Maps
3. Manually specify timezone if known

```bash
# Manual coordinate entry
python verify_geolocation.py --lat 46.3594 --lng 17.7968 --birth-date 1976-05-17
```

### Historical Timezone Considerations

- **Pre-1970:** Many regions had different timezone rules
- **DST variations:** Rules changed frequently (Hungary: no DST 1957-1979)
- **Action:** Always verify with `verify_geolocation.py` which uses pytz historical data

### Missing Birth Time Protocol

If birth time is unavailable:

1. Generate astrology chart with Sun position only
2. Mark as "time-sensitive data unavailable":
   - Moon position (approximate within ~6 degrees)
   - Houses (unavailable)
   - Ascendant (unavailable)
   - Human Design (unavailable)
3. Proceed with synthesis noting limitations

### Correction Protocol (Post-Synthesis Errors)

If errors discovered after synthesis is complete:

1. Create dated correction log entry
2. Move incorrect synthesis to `.archive/` with `superseded_by:` link
3. Re-run ALL acquisition phases with corrected data
4. Compare old vs. new charts, document what changed
5. Re-synthesize from scratch (do not patch incorrect synthesis)

---

## Integration with Client Work Protocol

This protocol is **Phase 1 (Data Acquisition)** of the Client Work Protocol workflow.

**Mandatory sequence within this protocol:**

1. **Phase 1:** Gather birth data (see Client Work Phase 0.1 for specifications)
2. **Phase 1b:** Verify geolocation (BEFORE any calculations)
3. **Phase 2:** Calculate natal charts (astrology, HD, bodygraph visualization)
4. **Phase 2b:** Calculate transits (MANDATORY if timing questions — see THE CARDINAL RULE)
5. **Phase 3:** Verification and user spot-check
6. **Phase 4:** Save data files (structure per Client Work Phase 4.1)
7. **Return to Client Work Protocol** → Phase 2 (Synthesis Work)

**Critical Rule:** Do NOT proceed to synthesis (Client Work Phase 2) until all data acquisition phases are complete and verified per Quality Gate checklist.

---

## Quick Reference

### Using the Wrapper Script (Recommended)

The `calculate_chart.sh` wrapper script automatically activates the virtual environment:

```bash
# Calculate Astrology Natal Chart
"◈ System/Scripts/calculate_chart.sh" astrology \
  --name "Name" \
  --year YYYY --month M --day D \
  --hour H --minute M \
  --lat LAT --lng LNG \
  --timezone "IANA/Timezone" \
  --pretty > astrology.json

# Calculate Human Design Natal Chart
"◈ System/Scripts/calculate_chart.sh" humandesign \
  --name "Name" \
  --year YYYY --month M --day D \
  --hour H --minute M \
  --lat LAT --lng LNG \
  --pretty > humandesign.json

# Example: Full calculation for Joe Lewis
cd "~/Business/Consultations/Joe Lewis"

"../../◈ System/Scripts/calculate_chart.sh" astrology \
  --name "Joe Lewis" \
  --year 1978 --month 9 --day 18 \
  --hour 17 --minute 34 \
  --lat 37.6706 --lng -82.2807 \
  --timezone "America/New_York" \
  --pretty > astrology.json

"../../◈ System/Scripts/calculate_chart.sh" humandesign \
  --name "Joe Lewis" \
  --year 1978 --month 9 --day 18 \
  --hour 17 --minute 34 \
  --lat 37.6706 --lng -82.2807 \
  --pretty > humandesign.json
```

### Direct Script Usage (Manual venv activation)

If you need to use scripts directly without the wrapper:

```bash
cd ~/VibologyOS
source .venv/bin/activate

# Calculate Astrology Natal Chart
python3 "◈ System/Scripts/get_astro_data.py" \
  --name "Name" \
  --year YYYY --month M --day D \
  --hour H --minute M \
  --lat LAT --lng LNG \
  --timezone "IANA/Timezone" \
  --pretty

# Calculate HD Natal Chart
python3 "◈ System/Scripts/get_hd_data.py" \
  --name "Name" \
  --year YYYY --month M --day D \
  --hour H --minute M \
  --lat LAT --lng LNG \
  --pretty

# Calculate Transits
python3 "◈ System/Scripts/get_transit_data.py" \
  --start-date YYYY-MM-DD \
  --end-date YYYY-MM-DD \
  --natal-file astrology.json \
  --pretty

# Find Ingress Dates
python3 "◈ System/Scripts/get_transit_data.py" \
  --ingress-planet saturn \
  --start-date YYYY-MM-DD \
  --end-date YYYY-MM-DD \
  --pretty

# Find Return Dates
python3 "◈ System/Scripts/get_transit_data.py" \
  --return-planet chiron \
  --natal-position 29.40 \
  --start-date YYYY-MM-DD \
  --end-date YYYY-MM-DD \
  --pretty
```

### Start HD API Server
```bash
cd "◈ System/humandesign_api" && source "../Scripts/.venv/bin/activate" && uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &
```

### Stop HD API Server
```bash
pkill -f "uvicorn humandesign"
```

---

## Version History

- **2026-01-29:** Protocol streamlining: Added Protocol Scope section clarifying technical vs. workflow boundaries. Removed duplicate birth data collection (now references Client Work Phase 0.1). Removed duplicate file organization structure (now references Client Work Phase 4.1). Renamed "Integration with Synthesis Protocol" to "Integration with Client Work Protocol" with clearer handoff sequence. Maintains technical authority for calculations, verification, and THE CARDINAL RULE while delegating workflow concerns to Client Work.
- **2026-01-28:**
  - Added bodygraph SVG generation step in Phase 2 (Human Design Natal Chart section). Documented activation-type indicators (split-aspect gates visible via colored borders). SVG is now the standard format for bodygraph visualizations.
  - Updated `get_hd_data.py` to include exaltation/detriment dignity data in chart JSON. Each planet now has a `dignity` field ("exalted", "detriment", or null) for synthesis traceability.
  - Fixed `get_astro_data.py` to store city/nation in JSON meta output for proper natal chart rendering.
- **2026-01-27:** Updated Consultations folder references to `~/Business/Consultations/`. Client data now stored outside VibologyOS repository.
- **2026-01-17:** **CRITICAL UPDATE - Transit Calculation Requirement Emphasized.** Added "THE CARDINAL RULE: ALWAYS CALCULATE TRANSITS" section with explicit examples of wrong vs. correct approach. Updated Phase 2b language to make transit calculation NON-NEGOTIABLE for any timing-related questions. This update addresses a protocol violation in the initial Joe Lewis synthesis where vague timing language was used instead of calculated transits. ALL FUTURE SYNTHESIS WORK MUST CALCULATE TRANSITS WHEN TIMING IS INVOLVED.
- **2026-01-17:** Virtual environment setup. Created `.venv/` in VibologyOS root, `requirements.txt` for dependency management, `calculate_chart.sh` wrapper script for automatic venv activation. Updated all Quick Reference examples. Addresses dependency persistence issues after system updates (PEP 668 compliance).
- **2026-01-16:** Major revision. Added geolocation verification (`verify_geolocation.py`), transit calculation (`get_transit_data.py`), verification checklist template, updated file organization. Response to transit data hallucination issue in Szilvia Williams synthesis.
- **2026-01-15:** Initial protocol created. Kerykeion v5.6.1 + humandesign_api v1.7.2 installed.
