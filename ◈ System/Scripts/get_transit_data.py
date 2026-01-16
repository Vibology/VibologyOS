#!/usr/bin/env python3
"""
Transit Data Calculation Script
Calculates precise astronomical transit data for synthesis work.

Features:
- Planetary ingress dates (when planets change signs)
- Return dates (Saturn return, Chiron return, etc.)
- Transits to natal planets (conjunctions, squares, oppositions)
- Optional Human Design gate context

Usage:
    # Find all major transits for 2026
    python get_transit_data.py --start-date 2026-01-01 --end-date 2026-12-31 --pretty

    # Calculate Saturn return for someone with natal Saturn at 28.22° Cancer
    python get_transit_data.py --return-planet saturn --natal-position 118.22 --start-date 2020-01-01 --end-date 2040-01-01

    # Find when Saturn enters Aries
    python get_transit_data.py --ingress-planet saturn --start-date 2025-01-01 --end-date 2030-01-01

    # Full transit report with natal chart comparison
    python get_transit_data.py --natal-file natal_chart.json --start-date 2026-01-01 --end-date 2027-12-31 --pretty
"""

import argparse
import json
import sys
import warnings
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Tuple, Any

# Suppress deprecation warnings from kerykeion
warnings.filterwarnings('ignore', category=DeprecationWarning, module='kerykeion')

try:
    from kerykeion import AstrologicalSubject
except ImportError:
    print("Error: kerykeion not installed. Run: pip install kerykeion", file=sys.stderr)
    sys.exit(1)

# Zodiac signs with their degree ranges
ZODIAC_SIGNS = [
    ("Ari", "Aries", 0, 30),
    ("Tau", "Taurus", 30, 60),
    ("Gem", "Gemini", 60, 90),
    ("Can", "Cancer", 90, 120),
    ("Leo", "Leo", 120, 150),
    ("Vir", "Virgo", 150, 180),
    ("Lib", "Libra", 180, 210),
    ("Sco", "Scorpio", 210, 240),
    ("Sag", "Sagittarius", 240, 270),
    ("Cap", "Capricorn", 270, 300),
    ("Aqu", "Aquarius", 300, 330),
    ("Pis", "Pisces", 330, 360),
]

# Human Design Gate mapping (IGING_CIRCLE_LIST from hd_constants.py)
# The HD wheel starts at Gate 41, offset by 58° from 0° Aries
HD_GATE_SEQUENCE = [
    41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3, 27, 24, 2, 23, 8,
    20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56, 31, 33, 7, 4, 29, 59, 40, 64, 47, 6,
    46, 18, 48, 57, 32, 50, 28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60
]
HD_OFFSET = 58  # Degrees offset to sync zodiac and HD wheels

# Planets to track for transits
OUTER_PLANETS = ['saturn', 'uranus', 'neptune', 'pluto', 'chiron', 'true_north_lunar_node']
ALL_PLANETS = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter'] + OUTER_PLANETS


def get_planet_position(year: int, month: int, day: int, hour: int = 12,
                        minute: int = 0, planet_name: str = 'saturn') -> Dict[str, Any]:
    """Get a planet's position for a specific date/time."""
    chart = AstrologicalSubject(
        name="Transit",
        year=year, month=month, day=day,
        hour=hour, minute=minute,
        lat=0, lng=0,  # Generic location for transits
        tz_str="UTC"
    )

    planet = getattr(chart, planet_name, None)
    if not planet:
        return None

    return {
        'sign': planet.get('sign'),
        'position': planet.get('position'),
        'abs_position': planet.get('abs_pos'),
        'retrograde': planet.get('retrograde', False)
    }


def get_all_planet_positions(year: int, month: int, day: int,
                             hour: int = 12, minute: int = 0,
                             planets: List[str] = None) -> Dict[str, Any]:
    """Get positions for all specified planets on a date."""
    if planets is None:
        planets = OUTER_PLANETS

    chart = AstrologicalSubject(
        name="Transit",
        year=year, month=month, day=day,
        hour=hour, minute=minute,
        lat=0, lng=0,
        tz_str="UTC"
    )

    positions = {}
    for planet_name in planets:
        planet = getattr(chart, planet_name, None)
        if planet:
            positions[planet_name] = {
                'sign': planet.get('sign'),
                'sign_full': get_full_sign_name(planet.get('sign')),
                'position': round(planet.get('position', 0), 4),
                'abs_position': round(planet.get('abs_pos', 0), 4),
                'retrograde': planet.get('retrograde', False),
                'hd_gate': get_hd_gate(planet.get('abs_pos', 0))
            }

    return positions


def get_full_sign_name(abbrev: str) -> str:
    """Convert abbreviated sign to full name."""
    for short, full, _, _ in ZODIAC_SIGNS:
        if short == abbrev:
            return full
    return abbrev


def get_hd_gate(abs_position: float) -> Dict[str, int]:
    """Convert absolute zodiac position to Human Design Gate and Line."""
    # Apply HD offset (58°) and normalize to 0-360
    hd_position = (abs_position - HD_OFFSET) % 360

    # Each gate spans 5.625° (360° / 64 gates)
    gate_size = 360 / 64
    gate_index = int(hd_position / gate_size)
    gate = HD_GATE_SEQUENCE[gate_index]

    # Each line spans 0.9375° (5.625° / 6 lines)
    position_in_gate = hd_position % gate_size
    line = int(position_in_gate / (gate_size / 6)) + 1

    return {'gate': gate, 'line': line}


def find_ingress_date(planet_name: str, target_sign_start: float,
                      start_date: datetime, end_date: datetime,
                      precision_hours: int = 6) -> Optional[datetime]:
    """
    Binary search to find when a planet crosses into a new sign.

    Args:
        planet_name: Name of planet to track
        target_sign_start: Absolute degree where sign begins (e.g., 0 for Aries)
        start_date: Beginning of search range
        end_date: End of search range
        precision_hours: Stop refining when within this many hours

    Returns:
        datetime of ingress, or None if not found in range
    """
    # First, verify the planet actually crosses this boundary in the range
    start_pos = get_planet_position(start_date.year, start_date.month, start_date.day,
                                    planet_name=planet_name)
    end_pos = get_planet_position(end_date.year, end_date.month, end_date.day,
                                  planet_name=planet_name)

    if not start_pos or not end_pos:
        return None

    start_abs = start_pos['abs_position']
    end_abs = end_pos['abs_position']

    # Handle retrograde motion and sign boundary crossing
    # This is complex because planets can cross a boundary multiple times
    # We'll do a coarse search first, then refine

    current = start_date
    step = timedelta(days=7)  # Check weekly first
    prev_pos = start_abs

    candidates = []

    while current < end_date:
        pos = get_planet_position(current.year, current.month, current.day,
                                  planet_name=planet_name)
        if pos:
            curr_abs = pos['abs_position']

            # Check if we crossed the target boundary
            # Handle the 360->0 wrap
            if target_sign_start == 0:
                # Special case for Aries (0°)
                crossed = (prev_pos > 350 and curr_abs < 10) or (prev_pos < 10 and curr_abs > 350)
            else:
                crossed = (prev_pos < target_sign_start <= curr_abs) or \
                          (prev_pos > target_sign_start >= curr_abs)

            if crossed:
                candidates.append(current - step)  # Go back to before crossing

            prev_pos = curr_abs

        current += step

    # Refine each candidate with binary search
    results = []
    for candidate in candidates:
        refined = binary_search_crossing(planet_name, target_sign_start,
                                         candidate, candidate + step * 2,
                                         precision_hours)
        if refined:
            results.append(refined)

    return results if results else None


def binary_search_crossing(planet_name: str, target_degree: float,
                           start: datetime, end: datetime,
                           precision_hours: int = 6) -> Optional[datetime]:
    """Binary search to find exact crossing time."""
    while (end - start).total_seconds() > precision_hours * 3600:
        mid = start + (end - start) / 2

        start_pos = get_planet_position(start.year, start.month, start.day,
                                        start.hour, start.minute, planet_name)
        mid_pos = get_planet_position(mid.year, mid.month, mid.day,
                                      mid.hour, mid.minute, planet_name)

        if not start_pos or not mid_pos:
            return None

        start_abs = start_pos['abs_position']
        mid_abs = mid_pos['abs_position']

        # Determine which half contains the crossing
        if target_degree == 0:
            # Handle 360->0 wrap for Aries
            start_near = start_abs > 350 or start_abs < 10
            mid_near = mid_abs > 350 or mid_abs < 10
            if start_abs > 180 and mid_abs < 180:
                end = mid
            elif start_abs < 180 and mid_abs > 180:
                start = mid
            elif (start_abs < target_degree) != (mid_abs < target_degree):
                end = mid
            else:
                start = mid
        else:
            if (start_abs < target_degree) != (mid_abs < target_degree):
                end = mid
            else:
                start = mid

    return start + (end - start) / 2


def find_return_date(planet_name: str, natal_abs_position: float,
                     start_date: datetime, end_date: datetime,
                     precision_hours: int = 6) -> List[Dict[str, Any]]:
    """
    Find when a transiting planet returns to its natal position.

    Returns list of return dates (there may be multiple due to retrograde).
    """
    results = []
    current = start_date
    step = timedelta(days=7)
    prev_pos = None

    while current < end_date:
        pos = get_planet_position(current.year, current.month, current.day,
                                  planet_name=planet_name)
        if pos:
            curr_abs = pos['abs_position']

            if prev_pos is not None:
                # Check if we crossed the natal position
                crossed_forward = prev_pos < natal_abs_position <= curr_abs
                crossed_backward = prev_pos > natal_abs_position >= curr_abs

                # Handle 360->0 wrap
                if natal_abs_position < 30:
                    crossed_forward = crossed_forward or (prev_pos > 350 and curr_abs < natal_abs_position + 10)
                if natal_abs_position > 330:
                    crossed_backward = crossed_backward or (prev_pos < 10 and curr_abs > natal_abs_position - 10)

                if crossed_forward or crossed_backward:
                    # Refine the date
                    refined = refine_exact_position(planet_name, natal_abs_position,
                                                    current - step, current + step,
                                                    precision_hours)
                    if refined:
                        results.append({
                            'date': refined.strftime('%Y-%m-%d'),
                            'datetime_utc': refined.isoformat() + 'Z',
                            'direction': 'direct' if crossed_forward else 'retrograde'
                        })

            prev_pos = curr_abs

        current += step

    return results


def refine_exact_position(planet_name: str, target_position: float,
                          start: datetime, end: datetime,
                          precision_hours: int = 6) -> Optional[datetime]:
    """Refine search for exact position match."""
    best_date = None
    best_diff = float('inf')

    current = start
    step = timedelta(hours=precision_hours)

    while current < end:
        pos = get_planet_position(current.year, current.month, current.day,
                                  current.hour, current.minute, planet_name)
        if pos:
            diff = abs(pos['abs_position'] - target_position)
            # Handle 360->0 wrap
            diff = min(diff, 360 - diff)

            if diff < best_diff:
                best_diff = diff
                best_date = current

        current += step

    return best_date


def find_all_ingresses(planet_name: str, start_date: datetime,
                       end_date: datetime) -> List[Dict[str, Any]]:
    """Find all sign ingresses for a planet in a date range."""
    ingresses = []

    # Get starting position
    start_pos = get_planet_position(start_date.year, start_date.month, start_date.day,
                                    planet_name=planet_name)
    if not start_pos:
        return ingresses

    current = start_date
    step = timedelta(days=1)
    prev_sign = start_pos['sign']

    while current < end_date:
        pos = get_planet_position(current.year, current.month, current.day,
                                  planet_name=planet_name)
        if pos and pos['sign'] != prev_sign:
            ingresses.append({
                'planet': planet_name,
                'from_sign': get_full_sign_name(prev_sign),
                'to_sign': get_full_sign_name(pos['sign']),
                'date': current.strftime('%Y-%m-%d'),
                'retrograde': pos['retrograde'],
                'hd_gate': get_hd_gate(pos['abs_position'])
            })
            prev_sign = pos['sign']
        elif pos:
            prev_sign = pos['sign']

        current += step

    return ingresses


def calculate_transit_report(start_date: datetime, end_date: datetime,
                             planets: List[str] = None,
                             natal_data: Dict = None) -> Dict[str, Any]:
    """
    Generate a comprehensive transit report.

    Args:
        start_date: Start of analysis period
        end_date: End of analysis period
        planets: List of planets to track (defaults to outer planets)
        natal_data: Optional natal chart data for return calculations

    Returns:
        Dictionary with transit data
    """
    if planets is None:
        planets = OUTER_PLANETS

    report = {
        'meta': {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'planets_analyzed': planets,
            'calculation_timestamp': datetime.utcnow().isoformat() + 'Z',
            'engine': 'kerykeion/pyswisseph'
        },
        'current_positions': get_all_planet_positions(
            start_date.year, start_date.month, start_date.day,
            planets=planets
        ),
        'ingresses': {},
        'returns': {}
    }

    # Calculate ingresses for each planet
    for planet in planets:
        ingresses = find_all_ingresses(planet, start_date, end_date)
        if ingresses:
            report['ingresses'][planet] = ingresses

    # Calculate returns if natal data provided
    if natal_data and 'planets' in natal_data:
        for planet in planets:
            if planet in natal_data['planets']:
                natal_pos = natal_data['planets'][planet].get('abs_position')
                if natal_pos is None and 'degrees' in natal_data['planets'][planet]:
                    # Try to reconstruct from sign + degrees
                    sign = natal_data['planets'][planet].get('sign', '')
                    degrees = natal_data['planets'][planet].get('degrees', 0)
                    natal_pos = sign_degrees_to_absolute(sign, degrees)

                if natal_pos:
                    returns = find_return_date(planet, natal_pos, start_date, end_date)
                    if returns:
                        report['returns'][planet] = {
                            'natal_position': natal_pos,
                            'return_dates': returns
                        }

    return report


def sign_degrees_to_absolute(sign: str, degrees: float) -> float:
    """Convert sign + degrees to absolute zodiac position."""
    sign_starts = {
        'Aries': 0, 'Ari': 0,
        'Taurus': 30, 'Tau': 30,
        'Gemini': 60, 'Gem': 60,
        'Cancer': 90, 'Can': 90,
        'Leo': 120,
        'Virgo': 150, 'Vir': 150,
        'Libra': 180, 'Lib': 180,
        'Scorpio': 210, 'Sco': 210,
        'Sagittarius': 240, 'Sag': 240,
        'Capricorn': 270, 'Cap': 270,
        'Aquarius': 300, 'Aqu': 300,
        'Pisces': 330, 'Pis': 330
    }

    start = sign_starts.get(sign, 0)
    return start + degrees


def main():
    parser = argparse.ArgumentParser(
        description='Calculate astrological transit data for synthesis work'
    )

    # Date range
    parser.add_argument('--start-date', required=True,
                        help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', required=True,
                        help='End date (YYYY-MM-DD)')

    # Planet selection
    parser.add_argument('--planets', nargs='+', default=None,
                        help='Planets to analyze (default: outer planets)')
    parser.add_argument('--all-planets', action='store_true',
                        help='Include all planets (Sun through Pluto + Chiron + Nodes)')

    # Specific calculations
    parser.add_argument('--ingress-planet',
                        help='Find all ingresses for a specific planet')
    parser.add_argument('--return-planet',
                        help='Calculate return for a specific planet')
    parser.add_argument('--natal-position', type=float,
                        help='Natal absolute position for return calculation')
    parser.add_argument('--natal-file',
                        help='JSON file with natal chart data')

    # Output options
    parser.add_argument('--pretty', action='store_true',
                        help='Pretty-print JSON output')
    parser.add_argument('--output', '-o',
                        help='Output file (default: stdout)')

    args = parser.parse_args()

    # Parse dates
    try:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
    except ValueError as e:
        print(f"Error parsing date: {e}", file=sys.stderr)
        sys.exit(1)

    # Determine planets to analyze
    planets = args.planets
    if args.all_planets:
        planets = ALL_PLANETS
    elif planets is None:
        planets = OUTER_PLANETS

    # Load natal data if provided
    natal_data = None
    if args.natal_file:
        try:
            with open(args.natal_file, 'r') as f:
                natal_data = json.load(f)
        except Exception as e:
            print(f"Error loading natal file: {e}", file=sys.stderr)
            sys.exit(1)

    # Handle specific calculations
    if args.ingress_planet:
        result = {
            'planet': args.ingress_planet,
            'ingresses': find_all_ingresses(args.ingress_planet, start_date, end_date)
        }
    elif args.return_planet and args.natal_position:
        result = {
            'planet': args.return_planet,
            'natal_position': args.natal_position,
            'returns': find_return_date(args.return_planet, args.natal_position,
                                        start_date, end_date)
        }
    else:
        # Full transit report
        result = calculate_transit_report(start_date, end_date, planets, natal_data)

    # Output
    output_str = json.dumps(result, indent=2 if args.pretty else None, default=str)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_str)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output_str)


if __name__ == '__main__':
    main()
