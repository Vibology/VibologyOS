#!/usr/bin/env python3
"""
Generate chart visualizations (bodygraph and natal chart) from calculated data.

Usage:
    # Generate both charts in current directory
    python generate_chart_visuals.py

    # Generate in specific directory
    python generate_chart_visuals.py --output-dir ~/Business/Consultations/ClientName/

    # Generate only bodygraph
    python generate_chart_visuals.py --bodygraph-only

    # Generate only natal chart
    python generate_chart_visuals.py --natal-only

Requirements:
    - humandesign.json (for bodygraph)
    - astrology.json (for natal chart)
    - Both must exist in the output directory
"""

import argparse
import json
import sys
from pathlib import Path

# Add humandesign_api to path
SCRIPT_DIR = Path(__file__).parent
HUMANDESIGN_API = SCRIPT_DIR.parent / 'humandesign_api' / 'src'
sys.path.insert(0, str(HUMANDESIGN_API))

try:
    from humandesign.services.chart_renderer import generate_bodygraph_image
except ImportError:
    print("Error: humandesign_api not found. Check path configuration.", file=sys.stderr)
    sys.exit(1)

try:
    from kerykeion import AstrologicalSubject, KerykeionChartSVG
except ImportError:
    print("Error: kerykeion not installed. Run: pip install kerykeion", file=sys.stderr)
    sys.exit(1)


def generate_bodygraph(output_dir: Path) -> bool:
    """Generate bodygraph.svg from humandesign.json."""
    hd_file = output_dir / 'humandesign.json'

    if not hd_file.exists():
        print(f"Error: {hd_file} not found", file=sys.stderr)
        return False

    # Load HD data
    with open(hd_file, 'r') as f:
        hd_data = json.load(f)

    # Transform to API format expected by renderer
    chart_data = {
        'general': {
            'energy_type': hd_data['type']['energy_type'],
            'strategy': hd_data['type']['strategy'],
            'inner_authority': hd_data['authority']['inner_authority'],
            'profile': hd_data['profile']['profile'],
            'inc_cross': hd_data['profile']['incarnation_cross'],
            'defined_centers': hd_data['definition']['defined_centers'],
            'undefined_centers': hd_data['definition']['undefined_centers'],
            'definition': hd_data['definition']['definition_type'],
            'variables': hd_data.get('variables', {})
        },
        'gates': {
            'prs': {'Planets': hd_data['gates']['personality']},
            'des': {'Planets': hd_data['gates']['design']}
        },
        'channels': hd_data.get('channels', [])
    }

    # Generate bodygraph as SVG
    svg_bytes = generate_bodygraph_image(
        chart_data,
        fmt='svg',
        include_panels=True,
        include_summary=False
    )

    # Write to file
    output_file = output_dir / 'bodygraph.svg'
    with open(output_file, 'wb') as f:
        f.write(svg_bytes)

    print(f"✓ Bodygraph: {output_file.relative_to(Path.cwd()) if output_file.is_relative_to(Path.cwd()) else output_file}")
    return True


def generate_natal_chart(output_dir: Path) -> bool:
    """Generate natal chart SVG from astrology.json."""
    astro_file = output_dir / 'astrology.json'

    if not astro_file.exists():
        print(f"Error: {astro_file} not found", file=sys.stderr)
        return False

    # Load astrology data
    with open(astro_file, 'r') as f:
        astro_data = json.load(f)

    meta = astro_data['meta']

    # Create Kerykeion subject
    subject = AstrologicalSubject(
        name=meta['name'],
        year=int(meta['birth_date'].split('-')[0]),
        month=int(meta['birth_date'].split('-')[1]),
        day=int(meta['birth_date'].split('-')[2]),
        hour=int(meta['birth_time'].split(':')[0]),
        minute=int(meta['birth_time'].split(':')[1]),
        lat=meta['coordinates']['lat'],
        lng=meta['coordinates']['lng'],
        city=meta.get('city'),
        nation=meta.get('nation'),
        tz_str=meta['timezone']
    )

    # Kerykeion generates in current directory by default
    # We need to temporarily change directory or move the file
    original_cwd = Path.cwd()

    try:
        # Generate natal chart (Kerykeion generates SVG by default)
        # Note: Kerykeion generates in user's home directory by default
        chart = KerykeionChartSVG(subject, chart_type="Natal")
        chart.makeSVG()

        # Kerykeion names the file: "{name} - Natal Chart.svg" in home directory
        import os
        home_dir = Path.home()
        generated_file = home_dir / f"{meta['name']} - Natal Chart.svg"

        # Move to output directory if generated elsewhere
        if generated_file.exists():
            target_file = output_dir / f"{meta['name']} - Natal Chart.svg"
            generated_file.rename(target_file)
            print(f"✓ Natal chart: {target_file.relative_to(original_cwd) if target_file.is_relative_to(original_cwd) else target_file}")
            return True
        else:
            print(f"Error: Kerykeion did not generate expected file: {generated_file}", file=sys.stderr)
            return False

    finally:
        # Restore original working directory
        pass


def main():
    parser = argparse.ArgumentParser(
        description='Generate chart visualizations from calculated data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate both charts in current directory
  python generate_chart_visuals.py

  # Generate in client folder
  python generate_chart_visuals.py --output-dir ~/Business/Consultations/ClientName/

  # Generate only bodygraph
  python generate_chart_visuals.py --bodygraph-only
        """
    )

    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path.cwd(),
        help='Directory containing JSON files and where SVGs will be saved (default: current directory)'
    )

    parser.add_argument(
        '--bodygraph-only',
        action='store_true',
        help='Generate only the bodygraph (requires humandesign.json)'
    )

    parser.add_argument(
        '--natal-only',
        action='store_true',
        help='Generate only the natal chart (requires astrology.json)'
    )

    args = parser.parse_args()

    # Resolve output directory
    output_dir = args.output_dir.resolve()

    if not output_dir.exists():
        print(f"Error: Output directory does not exist: {output_dir}", file=sys.stderr)
        sys.exit(1)

    if not output_dir.is_dir():
        print(f"Error: Not a directory: {output_dir}", file=sys.stderr)
        sys.exit(1)

    # Determine what to generate
    generate_both = not (args.bodygraph_only or args.natal_only)

    success = True

    if generate_both or args.bodygraph_only:
        if not generate_bodygraph(output_dir):
            success = False

    if generate_both or args.natal_only:
        if not generate_natal_chart(output_dir):
            success = False

    if success:
        print("\n✓ All charts generated successfully")
        sys.exit(0)
    else:
        print("\n✗ Some charts failed to generate", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
