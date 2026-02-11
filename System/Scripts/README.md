# Chart Calculation & Maintenance Scripts

This directory contains Python scripts for calculating astrology and Human Design charts, generating visualizations, and maintaining Library quality.

## Scripts

### Chart Calculation

#### `get_astro_data.py`

Calculate natal astrology charts using Kerykeion/Swiss Ephemeris.

**Required arguments:**
- `--name` - Subject name
- `--year`, `--month`, `--day` - Birth date
- `--hour`, `--minute` - Birth time (local time)
- `--lat`, `--lng` - Coordinates
- `--timezone` - IANA timezone (e.g., "America/New_York")

**Optional:**
- `--pretty` - Pretty-print JSON output

**Output:** Complete natal chart with planets (including Chiron, South Node, Lilith), houses, angles

#### `get_hd_data.py`

Calculate Human Design bodygraphs via Cartographer API.

**Required arguments:**
- `--name` - Subject name
- `--year`, `--month`, `--day` - Birth date
- `--hour`, `--minute` - Birth time
- `--place` - Location as "City, Country" (API geocodes automatically)

**Optional:**
- `--pretty` - Pretty-print JSON output
- `--check` - Check API health
- `--lat`, `--lng` - Pre-resolved coordinates (bypasses geocoding)

**Output:** Type, Authority, Profile, Centers, Channels, Gates with dignity

**Note:** Requires Cartographer API running on port 8000. Script auto-starts if not running.

#### `get_transit_data.py`

Calculate planetary transits, ingresses, and returns.

**Usage:**
```bash
python3 get_transit_data.py --start-date 2026-01-01 --end-date 2028-12-31 --natal-file astrology.json --pretty
python3 get_transit_data.py --ingress-planet saturn --start-date 2025-01-01 --end-date 2030-01-01 --pretty
python3 get_transit_data.py --return-planet chiron --natal-position 29.40 --start-date 2025-01-01 --end-date 2028-01-01 --pretty
```

#### `calculate_chart.sh` (Wrapper)

Automatically activates virtual environment and routes to `get_astro_data.py` or `get_hd_data.py`.

```bash
System/Scripts/calculate_chart.sh astrology [OPTIONS]
System/Scripts/calculate_chart.sh humandesign [OPTIONS]
```

### Chart Visualization

#### `generate_chart_visuals.py`

Generate bodygraph and natal chart SVGs from calculated data. Exports both light and dark mode variants.

**Usage:**
```bash
python3 System/Scripts/generate_chart_visuals.py --output-dir [folder]
```

**Reads:** `humandesign.json` from target directory
**Writes:** `bodygraph.svg`, `bodygraph-dark.svg`, `wheel-dark.svg`, `aspects-dark.svg`

#### `generate_bodygraph_svg.sh`

Shell wrapper for bodygraph SVG generation.

```bash
bash System/Scripts/generate_bodygraph_svg.sh [folder]
```

### Geolocation

#### `verify_geolocation.py`

Verify coordinates and timezone for a location.

### Library Maintenance

#### `scan_dead_links.py`

Scan Library for broken wikilinks. Useful during quarterly audits.

#### `scan_footnotes.py`

Scan Library files for footnote coverage. Useful during quarterly audits.

## Setup

### Virtual Environment

**Location:** `System/Cartographer/.venv/`

```bash
cd ~/VibologyOS/System/Cartographer
source .venv/bin/activate
```

### Dependencies

Managed via `requirements.txt`:

- `kerykeion>=4.0.0` - Astrology calculations (Swiss Ephemeris)
- `httpx>=0.24.0` - Cartographer API client

### Cartographer API

The Cartographer API must be running for Human Design calculations:

```bash
# Start API (port 8000)
cd System/Cartographer
source .venv/bin/activate
uvicorn cartographer.api:app --host 127.0.0.1 --port 8000 &

# Check status
curl -s http://127.0.0.1:8000/health | python3 -m json.tool

# Stop API
pkill -f "uvicorn cartographer"
```

## Troubleshooting

### "kerykeion not found"

Virtual environment not activated:
```bash
source ~/VibologyOS/System/Cartographer/.venv/bin/activate
```

### "HD API unreachable"

Start the Cartographer API (see above). `get_hd_data.py` will attempt auto-start.

## See Also

- `System/PROTOCOL - Chart Data Acquisition.md` - Complete workflow
- `System/CHECKLIST - Verification Quality Control.md` - Data integrity checks

## Archived Scripts

One-time batch scripts from the Library verification campaign (2026-01-24 through 2026-02-07) have been moved to `.archive/System/Scripts/`. These include footnote addition, dead link fixing, endmatter standardization, and verified flag scripts. All completed their purpose — Library is 100% verified and source-verified.
