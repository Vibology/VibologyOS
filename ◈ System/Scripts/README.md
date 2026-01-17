# Chart Calculation Scripts

This directory contains Python scripts for calculating astrology and Human Design charts with Swiss Ephemeris precision.

## Quick Start

Use the **wrapper script** for automatic virtual environment activation:

```bash
# From anywhere in VibologyOS
"◈ System/Scripts/calculate_chart.sh" astrology --name "Jane Doe" --year 1990 --month 5 --day 15 --hour 14 --minute 30 --lat 40.7128 --lng -74.0060 --timezone "America/New_York" --pretty

"◈ System/Scripts/calculate_chart.sh" humandesign --name "Jane Doe" --year 1990 --month 5 --day 15 --hour 14 --minute 30 --lat 40.7128 --lng -74.0060 --pretty
```

## Setup

### First-Time Installation

```bash
# Navigate to VibologyOS root
cd ~/VibologyOS

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r "◈ System/Scripts/requirements.txt"

# Test installation
"◈ System/Scripts/calculate_chart.sh"
```

### Reinstalling Dependencies

If system updates break the environment:

```bash
cd ~/VibologyOS
source .venv/bin/activate
pip install -r "◈ System/Scripts/requirements.txt"
```

Or rebuild from scratch:

```bash
cd ~/VibologyOS
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r "◈ System/Scripts/requirements.txt"
```

## Scripts

### `calculate_chart.sh` (Wrapper - Recommended)

Automatically activates virtual environment and routes to appropriate script.

**Usage:**
```bash
calculate_chart.sh astrology [OPTIONS]
calculate_chart.sh humandesign [OPTIONS]
```

### `get_astro_data.py`

Calculate natal astrology charts using Kerykeion/Swiss Ephemeris.

**Required arguments:**
- `--name` - Subject name
- `--year`, `--month`, `--day` - Birth date
- `--hour`, `--minute` - Birth time (local time)
- `--lat`, `--lng` - Coordinates
- `--timezone` - IANA timezone (e.g., "America/New_York")

**Optional:**
- `--pretty` - Pretty-print JSON output

**Output:** Complete natal chart with planets, houses, angles

### `get_hd_data.py`

Calculate Human Design bodygraphs via local API.

**Required arguments:**
- `--name` - Subject name
- `--year`, `--month`, `--day` - Birth date
- `--hour`, `--minute` - Birth time
- `--lat`, `--lng` - Coordinates

**Optional:**
- `--pretty` - Pretty-print JSON output
- `--check` - Check API health

**Output:** Type, Authority, Profile, Centers, Channels, Gates

**Note:** Requires HD API running on port 9021

### `get_transit_data.py`

Calculate planetary transits, ingresses, and returns.

**Usage:**
```bash
# Calculate all transits in date range
python3 get_transit_data.py --start-date 2026-01-01 --end-date 2028-12-31 --natal-file astrology.json --pretty

# Find specific ingress
python3 get_transit_data.py --ingress-planet saturn --start-date 2025-01-01 --end-date 2030-01-01 --pretty

# Find planetary return
python3 get_transit_data.py --return-planet chiron --natal-position 29.40 --start-date 2025-01-01 --end-date 2028-01-01 --pretty
```

### `verify_geolocation.py`

Verify coordinates and timezone for a location (requires system geopy).

**Note:** This script uses system-installed `python3-geopy`, not the venv.

## Dependencies

Managed via `requirements.txt`:

**Core:**
- `kerykeion>=4.0.0` - Astrology calculations
- `httpx>=0.24.0` - Human Design API client

**Optional (geolocation):**
- `geopy` - Install system-wide: `sudo apt install python3-geopy`
- `timezonefinder` - Install via pip if needed

## Virtual Environment

**Location:** `~/VibologyOS/.venv/`

**Why:** Protects against system updates removing dependencies (PEP 668 compliance on Fedora/modern distros)

**Activation:**
```bash
cd ~/VibologyOS
source .venv/bin/activate
```

**Deactivation:**
```bash
deactivate
```

## Human Design API

The HD API must be running for Human Design calculations:

```bash
# Start API (port 9021)
cd "◈ System/humandesign_api"
source "../.venv/bin/activate"  # Use main VibologyOS venv
uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &

# Check status
curl -s http://127.0.0.1:9021/health | python3 -m json.tool

# Stop API
pkill -f "uvicorn humandesign"
```

## Troubleshooting

### "kerykeion not found"

Virtual environment not activated. Use the wrapper script or activate manually:
```bash
source ~/VibologyOS/.venv/bin/activate
```

### "HD API unreachable"

Start the API server (see above).

### System updates broke dependencies

Reinstall (see "Reinstalling Dependencies" above).

## See Also

- `◈ System/PROTOCOL - Chart Data Acquisition.md` - Complete workflow
- `◈ System/Templates/_TEMPLATE - Synthesis Verification Checklist.md` - Data integrity checklist
