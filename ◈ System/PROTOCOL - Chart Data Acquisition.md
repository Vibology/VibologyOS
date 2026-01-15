---
tags: [system, protocol, data-integrity, astrology, human-design]
date_created: 2026-01-15
---

# Protocol: Chart Data Acquisition

This protocol ensures **chart data integrity** for all synthesis work involving Astrology and Human Design. It addresses Process Gap #1 (critical data integrity issues identified in the Szilvia Williams synthesis).

## Problem Statement

Chart data manually entered or calculated during synthesis leads to errors:
- Contradictory center definitions (Defined/Undefined flipped)
- Saturn timing errors
- North Node axis completely wrong
- House placements inconsistent

**Root Cause:** No verification step between data gathering and synthesis. Chart data trusted from memory/calculation instead of authoritative sources.

## Solution Architecture

Two local, free, self-hosted tools provide precise calculations:

| System | Tool | Engine | Accuracy |
|--------|------|--------|----------|
| Astrology | Kerykeion | Swiss Ephemeris (NASA JPL-derived) | Sub-arcsecond precision |
| Human Design | humandesign_api | Swiss Ephemeris + HD formulas | Production-grade calculations |

**Cost:** $0 (both are open-source)
**Data Privacy:** All calculations run locally (no external API calls)

---

## Pre-Requisites

### Environment Setup (One-Time)

The tools are installed in `◈ System/Scripts/.venv/`:

```bash
# Activate the virtual environment
cd "◈ System/Scripts"
source .venv/bin/activate

# Verify installations
python -c "from kerykeion import AstrologicalSubject; print('Kerykeion OK')"
python get_hd_data.py --check
```

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

The server can run in the background during your session. Stop it with `pkill -f "uvicorn humandesign"`.

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

### Phase 2: Calculate Charts

#### Astrology Chart

```bash
cd "◈ System/Scripts"
source .venv/bin/activate

python get_astro_data.py \
  --name "Subject Name" \
  --year 1990 \
  --month 6 \
  --day 15 \
  --hour 12 \
  --minute 0 \
  --lat 40.7128 \
  --lng -74.0060 \
  --pretty > astro_output.json
```

**Output includes:**
- All planet positions (Sun through Pluto, nodes, Chiron)
- House cusps (Placidus)
- Ascendant and Midheaven
- Retrograde status
- Lunar phase

#### Human Design Chart

```bash
python get_hd_data.py \
  --name "Subject Name" \
  --year 1990 \
  --month 6 \
  --day 15 \
  --hour 12 \
  --minute 0 \
  --place "New York, USA" \
  --pretty > hd_output.json
```

**Output includes:**
- Energy Type, Strategy, Signature, Not-Self
- Inner Authority
- Profile (e.g., "2/4: Hermit Opportunist")
- Incarnation Cross
- Definition Type
- Defined/Undefined Centers
- Channels and Gates
- Variables (Determination, Motivation, etc.)
- Personality and Design planet positions

### Phase 3: Verification (Critical)

**Present raw data to user for spot-check:**

1. **Astrology Quick Check:**
   - Sun sign matches expected?
   - Moon sign reasonable for date?
   - Saturn position consistent with known Saturn return timing?

2. **Human Design Quick Check:**
   - Type makes sense for the person?
   - Defined centers list is consistent (no contradictions)?
   - Profile feels accurate?

**If discrepancies found:**
- Re-verify birth data with user
- Re-run calculation
- Document any corrections

### Phase 4: Save Data Files

Save chart data files alongside synthesis pieces:

```
⚛ Synthesis/
└── Subject_Name_2026-01-15/
    ├── astro_data.json          # Raw astrology output
    ├── hd_data.json             # Raw HD output
    └── Synthesis.md             # The actual synthesis piece
```

Or for client work (using entity_id):

```
🤝 Consultations/
└── SW/
    ├── 2026-01-15_astro_data.json
    ├── 2026-01-15_hd_data.json
    └── 2026-01-15_Reading.md
```

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

### Data Validation

**Automatic checks in scripts:**
- Birth year within valid range (1800-2399)
- Coordinates within valid ranges (lat: -90 to +90, lng: -180 to +180)
- Month/day validity

**Edge cases requiring manual handling:**
- **DST Transition Ambiguity:** If birth time falls during DST transition, calculate both possibilities and ask user to verify
- **Historical Timezone Changes:** Document assumptions for dates before standardized timezones
- **Coordinate Precision:** If exact birth location unknown, use city center coordinates

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
3. Re-run chart acquisition with corrected birth data
4. Compare old vs. new charts, document what changed
5. Re-synthesize from scratch (do not patch incorrect synthesis)

---

## Integration with Synthesis Protocol

**Mandatory:** Data acquisition MUST complete before Weaver mode begins.

Update to `PROTOCOL - Cross-System Synthesis.md`:

> **Step 0 (NEW): Data Acquisition**
> Before gathering Prima Materia from any system, run the chart acquisition scripts for both Astrology and Human Design. Present raw data for user verification. Only proceed to Step 1 (Gather Prima Materia) after data is verified.

---

## Quick Reference

### Start HD API Server
```bash
cd "◈ System/humandesign_api" && source "../Scripts/.venv/bin/activate" && uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &
```

### Calculate Astrology Chart
```bash
cd "◈ System/Scripts" && source .venv/bin/activate && python get_astro_data.py --name "Name" --year YYYY --month M --day D --hour H --minute M --lat LAT --lng LNG --pretty
```

### Calculate HD Chart
```bash
cd "◈ System/Scripts" && source .venv/bin/activate && python get_hd_data.py --name "Name" --year YYYY --month M --day D --hour H --minute M --place "City, Country" --pretty
```

### Check HD API Status
```bash
python get_hd_data.py --check
```

### Stop HD API Server
```bash
pkill -f "uvicorn humandesign"
```

---

## Geocoding Note

The scripts accept either:
- **Place name** (e.g., `--place "New York, USA"`) - uses geocoding service
- **Coordinates** (e.g., `--lat 40.7128 --lng -74.0060`) - bypasses geocoding

For precise work, prefer coordinates. Use online tools like Google Maps to find exact birth location coordinates.

---

## Version History

- **2026-01-15:** Initial protocol created. Kerykeion v5.6.1 + humandesign_api v1.7.2 installed.
