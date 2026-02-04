#!/usr/bin/env python3
"""
Human Design Chart Data Acquisition Script
Calls the local humandesign_api (FastAPI) for precise HD calculations.

Usage:
    python get_hd_data.py --name "Name" --year 1990 --month 6 --day 15 \
                          --hour 12 --minute 0 --place "New York, USA"

    # Or with coordinates instead of place name:
    python get_hd_data.py --name "Name" --year 1990 --month 6 --day 15 \
                          --hour 12 --minute 0 --lat 40.7128 --lng -74.0060

Prerequisites:
    - humandesign_api running on localhost:9021
    - HD_API_TOKEN set in environment or .env file

Output: JSON to stdout with full HD chart data including exaltation/detriment dignities
"""

import argparse
import json
import os
import sys
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


def add_dignities_to_planets(
    personality_planets: list,
    design_planets: list,
    calculate_dignity_func,
    dignity_data: dict
):
    """
    Add dignity information to planet dictionaries using the comprehensive IHDS algorithm.

    This includes:
    - No polarity detection
    - Juxtaposition (star glyph or double fixing)
    - Harmonic fixing (channel partner planets)
    - Two-tier fixing for Design global planets
    """
    if not calculate_dignity_func or not dignity_data:
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

    # Add dignity to personality planets (always self-fixing)
    for planet in personality_planets:
        planet_name = planet.get('Planet')
        gate = planet.get('Gate')
        line = planet.get('Line')
        ch_gate = planet.get('Ch_Gate', 0)

        # Find harmonic planet
        harmonic_gate = ch_gate if ch_gate and ch_gate != 0 else None
        harmonic_planet = find_planet_at_gate(personality_planets, harmonic_gate) if harmonic_gate else None

        # Calculate dignity
        result = calculate_dignity_func(
            gate=gate,
            line=line,
            active_planet=planet_name,
            harmonic_gate=harmonic_gate,
            harmonic_planet=harmonic_planet,
            dignity_data=dignity_data
        )

        state = result.get("state")
        planet['dignity'] = state if state != "neutral" else None

    # Add dignity to design planets (with two-tier fixing for global planets)
    for planet in design_planets:
        planet_name = planet.get('Planet')
        gate = planet.get('Gate')
        line = planet.get('Line')
        design_lon = planet.get('Lon')
        ch_gate = planet.get('Ch_Gate', 0)
        normalized_planet = planet_name.replace('_', ' ')

        # Find harmonic planet
        harmonic_gate = ch_gate if ch_gate and ch_gate != 0 else None
        harmonic_planet = find_planet_at_gate(design_planets, harmonic_gate) if harmonic_gate else None

        # For self-fixing planets: standard calculation
        if normalized_planet not in GLOBAL_FIXING_PLANETS:
            result = calculate_dignity_func(
                gate=gate,
                line=line,
                active_planet=planet_name,
                harmonic_gate=harmonic_gate,
                harmonic_planet=harmonic_planet,
                dignity_data=dignity_data
            )
            state = result.get("state")
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
            result = calculate_dignity_func(
                gate=gate,
                line=line,
                active_planet=planet_name,
                harmonic_gate=harmonic_gate,
                harmonic_planet=harmonic_planet,
                dignity_data=dignity_data
            )
            state = result.get("state")
            planet['dignity'] = state if state != "neutral" else None
        else:
            planet['dignity'] = None


def get_hd_chart(
    name: str,
    year: int, month: int, day: int,
    hour: int, minute: int,
    place: str = None,
    lat: float = None, lng: float = None,
    base_url: str = DEFAULT_API_URL
) -> dict:
    """
    Calculate Human Design chart via local API.

    Args:
        name: Subject name (for identification)
        year, month, day: Birth date
        hour, minute: Birth time (local time)
        place: Place name (e.g., "New York, USA") - uses geocoding
        lat, lng: Geographic coordinates (alternative to place)
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
    }

    if place:
        params['place'] = place
    elif lat is not None and lng is not None:
        # humandesign_api requires place string, construct one
        params['place'] = f"{lat},{lng}"
    else:
        raise ValueError("Either 'place' or both 'lat' and 'lng' must be provided")

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
    parser.add_argument('--place', help='Birth place (e.g., "New York, USA")')
    parser.add_argument('--lat', type=float, help='Latitude (alternative to --place)')
    parser.add_argument('--lng', type=float, help='Longitude (alternative to --place)')
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
    if not args.place and (args.lat is None or args.lng is None):
        print("Error: Either --place or both --lat and --lng must be provided", file=sys.stderr)
        sys.exit(1)

    if not (1800 <= args.year <= 2399):
        print(f"Error: Year {args.year} outside valid range (1800-2399)", file=sys.stderr)
        sys.exit(1)

    # Check API availability
    if not check_api_health(args.api_url):
        print(json.dumps({
            'error': 'HD API not reachable',
            'url': args.api_url,
            'hint': 'Start the API with: cd humandesign_api && uvicorn humandesign.api:app --port 9021'
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
            lat=args.lat,
            lng=args.lng,
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
