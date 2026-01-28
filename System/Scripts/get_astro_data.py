#!/usr/bin/env python3
"""
Astrology Chart Data Acquisition Script
Uses Kerykeion (Swiss Ephemeris wrapper) for precise astronomical calculations.

Usage:
    python get_astro_data.py --name "Name" --year 1990 --month 6 --day 15 \
                             --hour 12 --minute 0 --lat 40.7128 --lng -74.0060

Output: JSON to stdout with full chart data
"""

import argparse
import json
import sys
import warnings
from datetime import datetime, timezone as dt_timezone

# Suppress deprecation warnings from kerykeion
warnings.filterwarnings('ignore', category=DeprecationWarning, module='kerykeion')

try:
    from kerykeion import AstrologicalSubject
except ImportError:
    print("Error: kerykeion not installed. Run: pip install kerykeion", file=sys.stderr)
    sys.exit(1)


def get_chart_data(name: str, year: int, month: int, day: int,
                   hour: int, minute: int, lat: float, lng: float,
                   timezone: str = None, city: str = None, nation: str = None) -> dict:
    """
    Calculate full astrological chart using Swiss Ephemeris.

    Args:
        name: Subject name (for identification)
        year, month, day: Birth date
        hour, minute: Birth time (local time)
        lat, lng: Geographic coordinates
        timezone: Optional IANA timezone (e.g., "America/New_York")
        city: Optional city name (for display in charts)
        nation: Optional nation code (for display in charts)

    Returns:
        Dictionary with full chart data
    """
    # Create chart
    subject = AstrologicalSubject(
        name=name,
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        city=city,
        nation=nation,
        lat=lat,
        lng=lng,
        tz_str=timezone,
        online=False  # Don't try to look up city from coordinates
    )

    # Extract planet data
    planets = {}
    planet_attrs = [
        'sun', 'moon', 'mercury', 'venus', 'mars',
        'jupiter', 'saturn', 'uranus', 'neptune', 'pluto',
        'mean_north_lunar_node', 'true_north_lunar_node', 'chiron'
    ]

    for planet_name in planet_attrs:
        planet = getattr(subject, planet_name, None)
        if planet:
            planets[planet_name] = {
                'sign': planet.get('sign'),
                'position': round(planet.get('position', 0), 4),
                'abs_position': round(planet.get('abs_pos', 0), 4),
                'retrograde': planet.get('retrograde', False),
                'house': planet.get('house')
            }

    # Extract house data
    houses = {}
    house_attrs = [
        'first_house', 'second_house', 'third_house', 'fourth_house',
        'fifth_house', 'sixth_house', 'seventh_house', 'eighth_house',
        'ninth_house', 'tenth_house', 'eleventh_house', 'twelfth_house'
    ]

    for i, house_name in enumerate(house_attrs, 1):
        house = getattr(subject, house_name, None)
        if house:
            houses[f'house_{i}'] = {
                'sign': house.get('sign'),
                'position': round(house.get('position', 0), 4)
            }

    # Build output
    chart_data = {
        'meta': {
            'name': name,
            'birth_date': f"{year}-{month:02d}-{day:02d}",
            'birth_time': f"{hour:02d}:{minute:02d}",
            'coordinates': {'lat': lat, 'lng': lng},
            'timezone': subject.tz_str if hasattr(subject, 'tz_str') else timezone,
            'calculation_timestamp': datetime.now(dt_timezone.utc).isoformat(),
            'engine': 'kerykeion/pyswisseph'
        },
        'planets': planets,
        'houses': houses,
        'angles': {
            'ascendant': {
                'sign': houses.get('house_1', {}).get('sign'),
                'position': houses.get('house_1', {}).get('position')
            },
            'midheaven': {
                'sign': houses.get('house_10', {}).get('sign'),
                'position': houses.get('house_10', {}).get('position')
            }
        },
        'lunar_phase': None  # Populated below if available
    }

    # Handle lunar_phase (may be a Pydantic model)
    lunar_phase = getattr(subject, 'lunar_phase', None)
    if lunar_phase:
        if hasattr(lunar_phase, 'model_dump'):
            chart_data['lunar_phase'] = lunar_phase.model_dump()
        elif hasattr(lunar_phase, 'dict'):
            chart_data['lunar_phase'] = lunar_phase.dict()
        elif isinstance(lunar_phase, dict):
            chart_data['lunar_phase'] = lunar_phase

    return chart_data


def main():
    parser = argparse.ArgumentParser(
        description='Calculate astrological chart data using Swiss Ephemeris'
    )
    parser.add_argument('--name', required=True, help='Subject name')
    parser.add_argument('--year', type=int, required=True, help='Birth year')
    parser.add_argument('--month', type=int, required=True, help='Birth month (1-12)')
    parser.add_argument('--day', type=int, required=True, help='Birth day (1-31)')
    parser.add_argument('--hour', type=int, required=True, help='Birth hour (0-23)')
    parser.add_argument('--minute', type=int, default=0, help='Birth minute (0-59)')
    parser.add_argument('--lat', type=float, required=True, help='Latitude')
    parser.add_argument('--lng', type=float, required=True, help='Longitude')
    parser.add_argument('--timezone', help='IANA timezone (e.g., America/New_York)')
    parser.add_argument('--city', help='City name (for display in chart graphics)')
    parser.add_argument('--nation', help='Nation code, e.g., US, GB (for display in chart graphics)')
    parser.add_argument('--pretty', action='store_true', help='Pretty-print JSON output')

    args = parser.parse_args()

    # Validate inputs
    if not (1800 <= args.year <= 2399):
        print(f"Error: Year {args.year} outside valid range (1800-2399)", file=sys.stderr)
        sys.exit(1)
    if not (1 <= args.month <= 12):
        print(f"Error: Month {args.month} outside valid range (1-12)", file=sys.stderr)
        sys.exit(1)
    if not (1 <= args.day <= 31):
        print(f"Error: Day {args.day} outside valid range (1-31)", file=sys.stderr)
        sys.exit(1)
    if not (-90 <= args.lat <= 90):
        print(f"Error: Latitude {args.lat} outside valid range (-90 to 90)", file=sys.stderr)
        sys.exit(1)
    if not (-180 <= args.lng <= 180):
        print(f"Error: Longitude {args.lng} outside valid range (-180 to 180)", file=sys.stderr)
        sys.exit(1)

    try:
        chart_data = get_chart_data(
            name=args.name,
            year=args.year,
            month=args.month,
            day=args.day,
            hour=args.hour,
            minute=args.minute,
            lat=args.lat,
            lng=args.lng,
            timezone=args.timezone,
            city=args.city,
            nation=args.nation
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
