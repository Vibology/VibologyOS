#!/usr/bin/env python3
"""
Human Design Chart Data Acquisition Script
Calls the local humandesign_api (FastAPI) for precise HD calculations.

Usage:
    python get_hd_data.py --name "Name" --year 1990 --month 6 --day 15 \
                          --hour 12 --minute 0 --place "New York, USA"

Prerequisites:
    - HD_API_TOKEN set in environment or .env file (optional)
    - Script will automatically start the API if not running

Output: JSON to stdout with full HD chart data including exaltation/detriment dignities
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from urllib.parse import urlencode
from pathlib import Path

try:
    import httpx
except ImportError:
    print("Error: httpx not installed. Run: pip install httpx", file=sys.stderr)
    sys.exit(1)

# Configuration
DEFAULT_API_URL = "http://127.0.0.1:9021"
DEFAULT_TOKEN = "vibologyos-local-dev-token"


def get_api_token() -> str:
    """Get API token from environment or .env file."""
    token = os.environ.get('HD_API_TOKEN')
    if not token:
        # Try to read from .env file in humandesign_api directory
        env_path = os.path.join(
            os.path.dirname(__file__),
            '..', 'humandesign_api', '.env'
        )
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith('HD_API_TOKEN='):
                        token = line.split('=', 1)[1].strip()
                        break
    return token or DEFAULT_TOKEN


def check_api_health(base_url: str) -> bool:
    """Check if the HD API is running."""
    try:
        response = httpx.get(f"{base_url}/health", timeout=5.0)
        return response.status_code == 200
    except Exception:
        return False


def start_api_server(port: int = 9021) -> bool:
    """
    Start the HD API server if not already running.

    Returns:
        True if server started successfully or is already running
        False if startup failed
    """
    script_dir = Path(__file__).parent
    api_dir = script_dir / '..' / 'humandesign_api'
    api_dir = api_dir.resolve()

    if not api_dir.exists():
        print(f"Error: humandesign_api directory not found at {api_dir}", file=sys.stderr)
        return False

    # Start the API in the background
    try:
        print(f"Starting HD API on port {port}...", file=sys.stderr)

        # Start uvicorn in the background
        process = subprocess.Popen(
            ['uvicorn', 'humandesign.api:app', '--host', '127.0.0.1', '--port', str(port)],
            cwd=str(api_dir),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True  # Detach from parent process
        )

        # Wait up to 10 seconds for API to be ready
        for i in range(20):
            time.sleep(0.5)
            if check_api_health(f"http://127.0.0.1:{port}"):
                print(f"HD API started successfully (PID: {process.pid})", file=sys.stderr)
                return True

        print("Error: API started but health check failed", file=sys.stderr)
        return False

    except FileNotFoundError:
        print("Error: uvicorn not found. Install with: pip install uvicorn", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error starting API: {e}", file=sys.stderr)
        return False


def load_dignity_module():
    """Import the dignity calculation module from humandesign_api."""
    script_dir = Path(__file__).parent
    api_src_path = script_dir / '..' / 'humandesign_api' / 'src'

    # Add to path if not already there
    api_src_str = str(api_src_path.resolve())
    if api_src_str not in sys.path:
        sys.path.insert(0, api_src_str)

    try:
        from humandesign.features.dignity import calculate_dignity, load_dignity_data
        return calculate_dignity, load_dignity_data
    except ImportError as e:
        print(f"Warning: Could not import dignity module: {e}", file=sys.stderr)
        return None, None


def find_planet_at_gate(planets_list: list, gate: int):
    """Find which planet activates a specific gate."""
    for planet in planets_list:
        if planet.get('Gate') == gate:
            return planet.get('Planet')
    return None


def has_line_color_resonance(line: int, color: int) -> bool:
    """
    Check if Line and Color are in Resonance or Harmony (The Fixing Rule).

    Planetary fixing only displays if there's resonance or harmony between Line and Color:
    - Resonance: Line number = Color number (e.g., Line 4 + Color 4)
    - Harmony: Lower/Upper trigram pairs (Line 1↔4, Line 2↔5, Line 3↔6)
    - Dissonance: Neither resonance nor harmony → fixing is "washed out"

    This is used by advanced calculation engines (MMI, Jovian Archive, Human.Design).
    """
    # Resonance: same number
    if line == color:
        return True

    # Harmony: lower/upper trigram pairs
    harmony_pairs = {
        (1, 4), (4, 1),  # Line 1 ↔ Line 4
        (2, 5), (5, 2),  # Line 2 ↔ Line 5
        (3, 6), (6, 3),  # Line 3 ↔ Line 6
    }
    if (line, color) in harmony_pairs:
        return True

    # Dissonance: neither resonance nor harmony
    return False


def calculate_dignity_complete(
    planet_data: dict,
    all_planets: list,
    harmonic_planet_data: dict,
    dignity_data: dict
) -> str:
    """
    Calculate dignity using complete IHDS algorithm.

    Rule Priority:
    1. Gate-Level Fixing (Quantum Synthesis) - bypasses all other rules
    2. Juxtaposition Attempt (opposite polarities) - dissonance causes failure → neutral
    3. Single Polarity (direct OR harmonic) - shows symbol regardless of dissonance

    Key Insight:
    - Dissonance affects EXPERIENCE (quality/stability), not DISPLAY
    - Exception: Juxtaposition attempts with dissonance collapse to neutral ("failed juxtaposition")

    Returns: "exalted", "detriment", "juxtaposed", or "neutral"
    """
    gate = planet_data.get('Gate')
    line = planet_data.get('Line')
    color = planet_data.get('Color')
    planet = planet_data.get('Planet', '').replace('_', ' ')

    # Validate inputs
    if not gate or not line:
        return "neutral"

    gate_str = str(gate)
    line_str = str(line)

    if gate_str not in dignity_data or line_str not in dignity_data[gate_str]:
        return "neutral"

    line_data = dignity_data[gate_str][line_str]

    # Check no_polarity flag
    if line_data.get('no_polarity', False):
        return "neutral"

    exaltation_planets = line_data.get('exaltation_planets', [])
    detriment_planets = line_data.get('detriment_planets', [])
    juxtaposition_planets = line_data.get('juxtaposition_planets', [])

    # LEVEL 1: Gate-Level Fixing (highest priority, bypasses everything)
    # Check if required planet exists elsewhere in this gate (different line or aspect)
    for p in all_planets:
        if p.get('Gate') == gate and p is not planet_data:  # Different activation in same gate
            p_name = p.get('Planet', '').replace('_', ' ')
            if p_name in exaltation_planets:
                return "exalted"  # Gate-level fixing
            if p_name in detriment_planets:
                return "detriment"  # Gate-level fixing

    # LEVEL 2 & 3: Check Direct and Harmonic Fixing
    # (Planet presence = display, regardless of dissonance for single polarity)

    # Check direct fixing
    direct_exalted = planet in exaltation_planets
    direct_detriment = planet in detriment_planets
    direct_juxtaposed = planet in juxtaposition_planets

    # Check harmonic fixing
    harmonic_exalted = False
    harmonic_detriment = False
    harmonic_juxtaposed = False

    if harmonic_planet_data:
        harmonic_planet = harmonic_planet_data.get('Planet', '').replace('_', ' ')
        harmonic_exalted = harmonic_planet in exaltation_planets
        harmonic_detriment = harmonic_planet in detriment_planets
        harmonic_juxtaposed = harmonic_planet in juxtaposition_planets

    # Check for explicit juxtaposition (star glyph in data)
    if direct_juxtaposed or harmonic_juxtaposed:
        return "juxtaposed"

    # Check for juxtaposition attempt (opposite polarities: exaltation + detriment)
    attempting_juxtaposition = False
    if (direct_exalted and harmonic_detriment) or (direct_detriment and harmonic_exalted):
        attempting_juxtaposition = True

    # Failed Juxtaposition Rule:
    # If attempting juxtaposition with dissonance → collapse to neutral
    if attempting_juxtaposition:
        has_dissonance = color is not None and not has_line_color_resonance(line, color)
        if has_dissonance:
            return "neutral"  # Failed juxtaposition - cannot hold tension
        else:
            return "juxtaposed"  # Successful juxtaposition

    # Single Polarity Fixing: Show symbol regardless of dissonance
    # (Dissonance affects quality/experience, not display)
    if direct_exalted or harmonic_exalted:
        return "exalted"
    if direct_detriment or harmonic_detriment:
        return "detriment"

    return "neutral"


def add_dignities_to_planets(
    personality_planets: list,
    design_planets: list,
    calculate_dignity_func,
    dignity_data: dict
):
    """
    Add dignity information to planet dictionaries using the comprehensive IHDS algorithm.

    This implements the complete three-level dignity hierarchy:
    1. Gate-Level Fixing (Quantum Synthesis) - bypasses dissonance completely
    2. Direct Fixing - with Sun Override for dissonance
    3. Harmonic Fixing - dissonance at receiving position always suppresses

    Also includes:
    - No polarity detection
    - Juxtaposition (star glyph or double fixing)
    - Two-tier fixing for Design global planets
    """
    if not dignity_data:
        return

    # Two-tier fixing constants
    GLOBAL_FIXING_PLANETS = {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "North Node", "South Node"}

    # Build personality global positions for Design two-tier fixing
    personality_global_positions = {}
    for planet in personality_planets:
        name = planet.get('Planet', '').replace('_', ' ')
        if name in GLOBAL_FIXING_PLANETS:
            personality_global_positions[name] = (
                planet.get('Gate'),
                planet.get('Line'),
                planet.get('Lon')
            )

    # Combine all planets for gate-level fixing
    all_planets = personality_planets + design_planets

    # Add dignity to personality planets (always self-fixing)
    for planet in personality_planets:
        ch_gate = planet.get('Ch_Gate', 0)

        # Find harmonic planet data (check both Design and Personality for cross-aspect channels)
        harmonic_planet_data = None
        if ch_gate and ch_gate != 0:
            # Check design side first
            for p in design_planets:
                if p.get('Gate') == ch_gate:
                    harmonic_planet_data = p
                    break
            # If not found, check personality side
            if not harmonic_planet_data:
                for p in personality_planets:
                    if p.get('Gate') == ch_gate and p is not planet:
                        harmonic_planet_data = p
                        break

        # Calculate dignity using comprehensive three-level hierarchy
        state = calculate_dignity_complete(
            planet_data=planet,
            all_planets=all_planets,
            harmonic_planet_data=harmonic_planet_data,
            dignity_data=dignity_data
        )

        planet['dignity'] = state if state != "neutral" else None

    # Add dignity to design planets (with two-tier fixing for global planets)
    for planet in design_planets:
        planet_name = planet.get('Planet')
        gate = planet.get('Gate')
        line = planet.get('Line')
        design_lon = planet.get('Lon')
        ch_gate = planet.get('Ch_Gate', 0)
        normalized_planet = planet_name.replace('_', ' ')

        # Find harmonic planet data (check both Design and Personality for cross-aspect channels)
        harmonic_planet_data = None
        if ch_gate and ch_gate != 0:
            # Check design side first
            for p in design_planets:
                if p.get('Gate') == ch_gate and p is not planet:
                    harmonic_planet_data = p
                    break
            # If not found, check personality side
            if not harmonic_planet_data:
                for p in personality_planets:
                    if p.get('Gate') == ch_gate:
                        harmonic_planet_data = p
                        break

        # For self-fixing planets: standard calculation
        if normalized_planet not in GLOBAL_FIXING_PLANETS:
            state = calculate_dignity_complete(
                planet_data=planet,
                all_planets=all_planets,
                harmonic_planet_data=harmonic_planet_data,
                dignity_data=dignity_data
            )
            planet['dignity'] = state if state != "neutral" else None
            continue

        # For global planets: check two-tier fixing
        personality_data = personality_global_positions.get(normalized_planet)
        if personality_data is None:
            planet['dignity'] = None
            continue

        prs_gate, prs_line, prs_lon = personality_data

        # Check if fixing holds (same gate.line or retrograde)
        same_position = (prs_gate, prs_line) == (gate, line)
        is_retrograde = False
        if design_lon is not None and prs_lon is not None:
            delta = prs_lon - design_lon
            if delta > 180:
                delta -= 360
            elif delta < -180:
                delta += 360
            is_retrograde = delta < 0

        if same_position or is_retrograde:
            state = calculate_dignity_complete(
                planet_data=planet,
                all_planets=all_planets,
                harmonic_planet_data=harmonic_planet_data,
                dignity_data=dignity_data
            )
            planet['dignity'] = state if state != "neutral" else None
        else:
            planet['dignity'] = None


def get_hd_chart(
    name: str,
    year: int, month: int, day: int,
    hour: int, minute: int,
    place: str,
    base_url: str = DEFAULT_API_URL
) -> dict:
    """
    Calculate Human Design chart via local API.

    Args:
        name: Subject name (for identification)
        year, month, day: Birth date
        hour, minute: Birth time (local time)
        place: Place name (e.g., "New York, USA" or "Kaposvar, Hungary")
        base_url: API base URL

    Returns:
        Dictionary with full HD chart data
    """
    token = get_api_token()

    # Build query parameters
    params = {
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        'place': place
    }

    # Make API request
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }

    try:
        response = httpx.get(
            f"{base_url}/calculate",
            params=params,
            headers=headers,
            timeout=30.0
        )
        response.raise_for_status()
        api_data = response.json()

    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"API error: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        raise RuntimeError(f"Connection error: {str(e)}")

    # Transform API response to our standard format
    general = api_data.get('general', {})
    channels_data = api_data.get('channels', {})
    gates_data = api_data.get('gates', {})

    # Load dignity calculation module and data
    calculate_dignity_func, load_dignity_data_func = load_dignity_module()
    dignity_data = load_dignity_data_func() if load_dignity_data_func else {}

    # Add dignity to personality and design planets
    personality_planets = gates_data.get('prs', {}).get('Planets', [])
    design_planets = gates_data.get('des', {}).get('Planets', [])

    add_dignities_to_planets(
        personality_planets,
        design_planets,
        calculate_dignity_func,
        dignity_data
    )

    chart_data = {
        'meta': {
            'name': name,
            'birth_date': f"{year}-{month:02d}-{day:02d}",
            'birth_time': f"{hour:02d}:{minute:02d}",
            'place': place or f"{lat}, {lng}",
            'calculation_timestamp': datetime.utcnow().isoformat() + 'Z',
            'engine': 'humandesign_api/pyswisseph'
        },
        'type': {
            'energy_type': general.get('energy_type'),
            'strategy': general.get('strategy'),
            'signature': general.get('signature'),
            'not_self': general.get('not_self'),
            'aura': general.get('aura')
        },
        'authority': {
            'inner_authority': general.get('inner_authority')
        },
        'profile': {
            'profile': general.get('profile'),
            'incarnation_cross': general.get('inc_cross')
        },
        'definition': {
            'definition_type': general.get('definition'),
            'defined_centers': general.get('defined_centers', []),
            'undefined_centers': general.get('undefined_centers', [])
        },
        'variables': general.get('variables', {}),
        'channels': channels_data.get('Channels', []),
        'gates': {
            'personality': personality_planets,
            'design': design_planets
        },
        'planets': {
            'personality': api_data.get('personality', {}),
            'design': api_data.get('design', {})
        },
        'zodiac_sign': general.get('zodiac_sign'),
        'age': general.get('age')
    }

    return chart_data


def main():
    parser = argparse.ArgumentParser(
        description='Calculate Human Design chart data via local API'
    )
    parser.add_argument('--name', required=True, help='Subject name')
    parser.add_argument('--year', type=int, required=True, help='Birth year')
    parser.add_argument('--month', type=int, required=True, help='Birth month (1-12)')
    parser.add_argument('--day', type=int, required=True, help='Birth day (1-31)')
    parser.add_argument('--hour', type=int, required=True, help='Birth hour (0-23)')
    parser.add_argument('--minute', type=int, default=0, help='Birth minute (0-59)')
    parser.add_argument('--place', required=True, help='Birth place (e.g., "New York, USA" or "Kaposvar, Hungary")')
    parser.add_argument('--api-url', default=DEFAULT_API_URL, help='API base URL')
    parser.add_argument('--pretty', action='store_true', help='Pretty-print JSON output')
    parser.add_argument('--check', action='store_true', help='Only check API health')

    args = parser.parse_args()

    # Health check mode
    if args.check:
        if check_api_health(args.api_url):
            print(json.dumps({'status': 'healthy', 'url': args.api_url}))
            sys.exit(0)
        else:
            print(json.dumps({'status': 'unreachable', 'url': args.api_url}))
            sys.exit(1)

    # Validate inputs
    if not (1800 <= args.year <= 2399):
        print(f"Error: Year {args.year} outside valid range (1800-2399)", file=sys.stderr)
        sys.exit(1)

    # Ensure API is running (start if needed)
    if not check_api_health(args.api_url):
        print("HD API not running, attempting to start...", file=sys.stderr)
        if not start_api_server():
            print(json.dumps({
                'error': 'Failed to start HD API',
                'url': args.api_url,
                'hint': 'Try manually: cd System/humandesign_api && uvicorn humandesign.api:app --port 9021'
            }), file=sys.stderr)
            sys.exit(1)

    try:
        chart_data = get_hd_chart(
            name=args.name,
            year=args.year,
            month=args.month,
            day=args.day,
            hour=args.hour,
            minute=args.minute,
            place=args.place,
            base_url=args.api_url
        )

        if args.pretty:
            print(json.dumps(chart_data, indent=2))
        else:
            print(json.dumps(chart_data))

    except Exception as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
