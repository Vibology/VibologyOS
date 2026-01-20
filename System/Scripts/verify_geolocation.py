#!/usr/bin/env python3
"""
Geolocation Verification System
Ensures accurate coordinates and timezone for chart calculations.

This script:
1. Geocodes a place name to coordinates
2. Determines the correct timezone (with historical DST awareness)
3. Presents results for user verification
4. Outputs verified location data for use in chart calculations

Usage:
    # Interactive verification
    python verify_geolocation.py --place "Kaposvar, Hungary" --birth-date 1976-05-17

    # Output to JSON
    python verify_geolocation.py --place "New York, USA" --birth-date 1990-06-15 --output location.json

    # With manual coordinate override
    python verify_geolocation.py --lat 46.3594 --lng 17.7968 --birth-date 1976-05-17

    # Non-interactive mode (for scripts)
    python verify_geolocation.py --place "London, UK" --birth-date 1985-03-20 --non-interactive
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

try:
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
except ImportError:
    print("Error: geopy not installed. Run: pip install geopy", file=sys.stderr)
    sys.exit(1)

try:
    from timezonefinder import TimezoneFinder
except ImportError:
    print("Error: timezonefinder not installed. Run: pip install timezonefinder", file=sys.stderr)
    sys.exit(1)

try:
    import pytz
except ImportError:
    print("Error: pytz not installed. Run: pip install pytz", file=sys.stderr)
    sys.exit(1)


# Known location corrections for common ambiguous place names
LOCATION_CORRECTIONS = {
    # Format: "search_term": {"lat": ..., "lng": ..., "timezone": ..., "note": ...}
    # Add corrections for places where geocoding commonly fails
}

# Historical timezone notes for certain regions
TIMEZONE_NOTES = {
    "Europe/Budapest": "Hungary: CET (UTC+1), CEST (UTC+2) during summer. DST observed since 1954 with various rule changes.",
    "America/New_York": "US Eastern: EST (UTC-5), EDT (UTC-4) during summer. DST rules changed in 2007.",
    "Europe/London": "UK: GMT (UTC+0), BST (UTC+1) during summer. Historical variations exist pre-1968.",
}


def geocode_place(place: str, timeout: int = 10) -> Optional[Dict[str, Any]]:
    """
    Geocode a place name to coordinates using Nominatim.

    Args:
        place: Place name (e.g., "Kaposvar, Hungary")
        timeout: Request timeout in seconds

    Returns:
        Dictionary with lat, lng, address, or None if not found
    """
    geolocator = Nominatim(user_agent="vibologyos_chart_calc")

    try:
        location = geolocator.geocode(place, exactly_one=True, addressdetails=True)
        if location:
            return {
                'latitude': location.latitude,
                'longitude': location.longitude,
                'address': location.address,
                'raw': location.raw
            }
    except GeocoderTimedOut:
        print(f"Warning: Geocoding timed out for '{place}'", file=sys.stderr)
    except GeocoderUnavailable:
        print(f"Warning: Geocoding service unavailable", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Geocoding error: {e}", file=sys.stderr)

    return None


def get_timezone_for_location(lat: float, lng: float) -> Optional[str]:
    """
    Determine timezone for given coordinates.

    Args:
        lat: Latitude
        lng: Longitude

    Returns:
        IANA timezone string (e.g., "Europe/Budapest")
    """
    tf = TimezoneFinder()
    return tf.timezone_at(lat=lat, lng=lng)


def get_utc_offset(timezone_str: str, date: datetime) -> Tuple[float, str, bool]:
    """
    Get UTC offset for a timezone on a specific date.

    Args:
        timezone_str: IANA timezone (e.g., "Europe/Budapest")
        date: Date to check (DST varies by date)

    Returns:
        Tuple of (offset_hours, offset_string, is_dst)
    """
    try:
        tz = pytz.timezone(timezone_str)
        # Localize the date to the timezone
        localized = tz.localize(date)

        # Get offset
        offset = localized.utcoffset()
        offset_hours = offset.total_seconds() / 3600

        # Check if DST is in effect
        is_dst = bool(localized.dst())

        # Format offset string
        hours = int(offset_hours)
        minutes = int((offset_hours - hours) * 60)
        if offset_hours >= 0:
            offset_str = f"UTC+{hours}" if minutes == 0 else f"UTC+{hours}:{minutes:02d}"
        else:
            offset_str = f"UTC{hours}" if minutes == 0 else f"UTC{hours}:{abs(minutes):02d}"

        return offset_hours, offset_str, is_dst

    except Exception as e:
        print(f"Warning: Error calculating UTC offset: {e}", file=sys.stderr)
        return 0, "UTC+0", False


def reverse_geocode(lat: float, lng: float) -> Optional[str]:
    """Get address from coordinates."""
    geolocator = Nominatim(user_agent="vibologyos_chart_calc")
    try:
        location = geolocator.reverse((lat, lng), exactly_one=True)
        return location.address if location else None
    except Exception as e:
        print(f"Warning: Reverse geocoding error: {e}", file=sys.stderr)
        return None


def verify_location(place: str = None, lat: float = None, lng: float = None,
                    birth_date: datetime = None, interactive: bool = True) -> Dict[str, Any]:
    """
    Main verification function.

    Args:
        place: Place name to geocode
        lat: Manual latitude (overrides geocoding)
        lng: Manual longitude (overrides geocoding)
        birth_date: Birth date for DST calculation
        interactive: Whether to prompt for user confirmation

    Returns:
        Verified location data
    """
    result = {
        'input': {
            'place': place,
            'manual_lat': lat,
            'manual_lng': lng,
            'birth_date': birth_date.strftime('%Y-%m-%d') if birth_date else None
        },
        'resolved': {},
        'verification_status': 'unverified',
        'warnings': [],
        'notes': []
    }

    # Step 1: Get coordinates
    if lat is not None and lng is not None:
        # Manual coordinates provided
        resolved_lat = lat
        resolved_lng = lng
        result['resolved']['source'] = 'manual_input'

        # Reverse geocode to verify
        address = reverse_geocode(lat, lng)
        if address:
            result['resolved']['reverse_geocoded_address'] = address
    elif place:
        # Geocode the place name
        geo_result = geocode_place(place)
        if geo_result:
            resolved_lat = geo_result['latitude']
            resolved_lng = geo_result['longitude']
            result['resolved']['source'] = 'nominatim_geocoding'
            result['resolved']['geocoded_address'] = geo_result['address']
        else:
            result['verification_status'] = 'failed'
            result['warnings'].append(f"Could not geocode place: '{place}'")
            return result
    else:
        result['verification_status'] = 'failed'
        result['warnings'].append("No place name or coordinates provided")
        return result

    result['resolved']['latitude'] = round(resolved_lat, 6)
    result['resolved']['longitude'] = round(resolved_lng, 6)

    # Step 2: Determine timezone
    timezone = get_timezone_for_location(resolved_lat, resolved_lng)
    if timezone:
        result['resolved']['timezone'] = timezone

        # Add timezone notes if available
        if timezone in TIMEZONE_NOTES:
            result['notes'].append(TIMEZONE_NOTES[timezone])

        # Calculate UTC offset for birth date if provided
        if birth_date:
            offset_hours, offset_str, is_dst = get_utc_offset(timezone, birth_date)
            result['resolved']['utc_offset'] = offset_hours
            result['resolved']['utc_offset_string'] = offset_str
            result['resolved']['dst_active'] = is_dst
    else:
        result['warnings'].append("Could not determine timezone from coordinates")
        result['resolved']['timezone'] = 'UTC'
        result['resolved']['utc_offset'] = 0
        result['resolved']['utc_offset_string'] = 'UTC+0'
        result['resolved']['dst_active'] = False

    # Step 3: Interactive verification
    if interactive and sys.stdin.isatty():
        print("\n" + "=" * 60)
        print("GEOLOCATION VERIFICATION")
        print("=" * 60)

        if place:
            print(f"\nInput place: {place}")
        if lat is not None and lng is not None:
            print(f"Manual coordinates: {lat}, {lng}")

        print(f"\nResolved coordinates:")
        print(f"  Latitude:  {result['resolved']['latitude']}")
        print(f"  Longitude: {result['resolved']['longitude']}")

        if 'geocoded_address' in result['resolved']:
            print(f"\nGeocoded address:")
            print(f"  {result['resolved']['geocoded_address']}")
        if 'reverse_geocoded_address' in result['resolved']:
            print(f"\nReverse geocoded address:")
            print(f"  {result['resolved']['reverse_geocoded_address']}")

        print(f"\nTimezone: {result['resolved'].get('timezone', 'Unknown')}")

        if birth_date:
            print(f"\nFor birth date {birth_date.strftime('%Y-%m-%d')}:")
            print(f"  UTC Offset: {result['resolved'].get('utc_offset_string', 'Unknown')}")
            print(f"  DST Active: {'Yes' if result['resolved'].get('dst_active') else 'No'}")

        if result['notes']:
            print(f"\nNotes:")
            for note in result['notes']:
                print(f"  - {note}")

        if result['warnings']:
            print(f"\nWarnings:")
            for warning in result['warnings']:
                print(f"  ! {warning}")

        print("\n" + "-" * 60)

        # Prompt for confirmation
        while True:
            response = input("\nIs this location data correct? [Y/n/edit]: ").strip().lower()

            if response in ['', 'y', 'yes']:
                result['verification_status'] = 'verified'
                break
            elif response in ['n', 'no']:
                result['verification_status'] = 'rejected'
                print("\nLocation rejected. Please provide correct coordinates manually.")
                break
            elif response in ['e', 'edit']:
                # Allow manual edits
                print("\nEnter correct values (press Enter to keep current):")

                new_lat = input(f"  Latitude [{result['resolved']['latitude']}]: ").strip()
                if new_lat:
                    try:
                        result['resolved']['latitude'] = float(new_lat)
                    except ValueError:
                        print("    Invalid latitude, keeping original")

                new_lng = input(f"  Longitude [{result['resolved']['longitude']}]: ").strip()
                if new_lng:
                    try:
                        result['resolved']['longitude'] = float(new_lng)
                    except ValueError:
                        print("    Invalid longitude, keeping original")

                new_tz = input(f"  Timezone [{result['resolved'].get('timezone', 'UTC')}]: ").strip()
                if new_tz:
                    # Validate timezone
                    try:
                        pytz.timezone(new_tz)
                        result['resolved']['timezone'] = new_tz
                        # Recalculate offset
                        if birth_date:
                            offset_hours, offset_str, is_dst = get_utc_offset(new_tz, birth_date)
                            result['resolved']['utc_offset'] = offset_hours
                            result['resolved']['utc_offset_string'] = offset_str
                            result['resolved']['dst_active'] = is_dst
                    except:
                        print("    Invalid timezone, keeping original")

                result['verification_status'] = 'manually_corrected'
                result['notes'].append("Location data was manually corrected by user")
                break
            else:
                print("Please enter 'y' (yes), 'n' (no), or 'edit'")

    else:
        # Non-interactive mode - auto-verify if geocoding succeeded
        if not result['warnings']:
            result['verification_status'] = 'auto_verified'
        else:
            result['verification_status'] = 'unverified_with_warnings'

    # Add verification timestamp
    result['verification_timestamp'] = datetime.utcnow().isoformat() + 'Z'

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Verify geolocation data for chart calculations'
    )

    parser.add_argument('--place',
                        help='Place name to geocode (e.g., "Kaposvar, Hungary")')
    parser.add_argument('--lat', type=float,
                        help='Manual latitude (overrides geocoding)')
    parser.add_argument('--lng', type=float,
                        help='Manual longitude (overrides geocoding)')
    parser.add_argument('--birth-date',
                        help='Birth date for DST calculation (YYYY-MM-DD)')
    parser.add_argument('--non-interactive', action='store_true',
                        help='Run without interactive prompts')
    parser.add_argument('--output', '-o',
                        help='Output file for verified location data')
    parser.add_argument('--pretty', action='store_true',
                        help='Pretty-print JSON output')

    args = parser.parse_args()

    # Validate inputs
    if not args.place and (args.lat is None or args.lng is None):
        print("Error: Either --place or both --lat and --lng are required", file=sys.stderr)
        sys.exit(1)

    # Parse birth date
    birth_date = None
    if args.birth_date:
        try:
            birth_date = datetime.strptime(args.birth_date, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Invalid date format. Use YYYY-MM-DD", file=sys.stderr)
            sys.exit(1)

    # Run verification
    result = verify_location(
        place=args.place,
        lat=args.lat,
        lng=args.lng,
        birth_date=birth_date,
        interactive=not args.non_interactive
    )

    # Output
    output_str = json.dumps(result, indent=2 if args.pretty else None)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_str)
        print(f"\nVerified location data written to {args.output}", file=sys.stderr)
    else:
        if not args.non_interactive:
            print("\n" + "=" * 60)
            print("VERIFIED LOCATION DATA (JSON)")
            print("=" * 60)
        print(output_str)

    # Exit with appropriate code
    if result['verification_status'] in ['verified', 'auto_verified', 'manually_corrected']:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
