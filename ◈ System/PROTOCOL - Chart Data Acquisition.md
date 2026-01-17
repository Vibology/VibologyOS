---
tags: [system, protocol, data-integrity, astrology, human-design]
date_created: 2026-01-15
date_updated: 2026-01-17
---

# Protocol: Chart Data Acquisition

This protocol ensures **chart data integrity** for all synthesis work involving Astrology and Human Design. It addresses Process Gap #1 (critical data integrity issues) and incorporates lessons learned from the Szilvia Williams synthesis audit.

## Core Principle

**NEVER hallucinate or infer astronomical data.** Every planetary position, every transit date, every timing claim MUST be calculated using verified tools and traceable to a source JSON file.

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

Required information from user:
- **Name** (or entity_id for privacy)
- **Birth Date:** Year, Month, Day
- **Birth Time:** Hour, Minute (local time at birth location)
- **Birth Location:** City, Country (or precise coordinates)

**If birth time is unknown:**
- Astrology: Can calculate Sun, Moon sign (approximate), outer planets
- Human Design: Cannot calculate accurately (Type, Profile, Gates depend on precise time)
- **Action:** Flag as "time-sensitive data unavailable" in synthesis

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
- Channels and Gates
- Variables

### Phase 2b: Calculate Transits (MANDATORY for Timing Questions)

**If the synthesis involves ANY timing questions, transit predictions, or life cycle analysis:**

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

**File Organization:**

```
🤝 Consultations/
└── [Client Name or Entity ID]/
    ├── astrology.json              # Natal chart (PERMANENT)
    ├── humandesign.json            # HD bodygraph (PERMANENT)
    ├── [Reference PDFs]            # External reference docs
    └── YYYY-MM-DD_[Synthesis_Name]/
        ├── location_verification.json   # Geolocation verification
        ├── transits.json                # Calculated transit data
        ├── Verification_Checklist.md    # Completed checklist
        └── Synthesis.md                 # Final synthesis output
```

**Rationale:**
- `astrology.json` and `humandesign.json` are **permanent** natal data - always relevant
- Transit data is **synthesis-specific** - calculated for the questions asked
- Each synthesis gets its own subfolder with all supporting calculations
- Verification checklist ensures traceability

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

## Integration with Synthesis Protocol

**Mandatory sequence:**

1. **Phase 0:** Gather birth data from user
2. **Phase 1b:** Verify geolocation (BEFORE any calculations)
3. **Phase 2:** Calculate natal charts
4. **Phase 2b:** Calculate transits (if timing questions exist)
5. **Phase 3:** User verification
6. **Phase 4:** Save data files
7. **THEN:** Begin Weaver mode / synthesis

**Rule:** Do NOT enter synthesis mode until all data acquisition phases are complete and verified.

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
cd "🤝 Consultations/Joe Lewis"

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

- **2026-01-17:** Virtual environment setup. Created `.venv/` in VibologyOS root, `requirements.txt` for dependency management, `calculate_chart.sh` wrapper script for automatic venv activation. Updated all Quick Reference examples. Addresses dependency persistence issues after system updates (PEP 668 compliance).
- **2026-01-16:** Major revision. Added geolocation verification (`verify_geolocation.py`), transit calculation (`get_transit_data.py`), verification checklist template, updated file organization. Response to transit data hallucination issue in Szilvia Williams synthesis.
- **2026-01-15:** Initial protocol created. Kerykeion v5.6.1 + humandesign_api v1.7.2 installed.
