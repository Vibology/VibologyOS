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

# Add Cartographer to path
SCRIPT_DIR = Path(__file__).parent
CARTOGRAPHER_SRC = SCRIPT_DIR.parent / 'Cartographer' / 'src'
sys.path.insert(0, str(CARTOGRAPHER_SRC))

try:
    from cartographer.services.chart_renderer import generate_bodygraph_image
except ImportError:
    print("Error: Cartographer not found. Check path configuration.", file=sys.stderr)
    sys.exit(1)

try:
    from cartographer.services.astro_renderer import render_natal_chart
except ImportError:
    print("Error: Cartographer astro_renderer not found.", file=sys.stderr)
    sys.exit(1)


def generate_bodygraph(output_dir: Path) -> bool:
    """Generate bodygraph.svg (light) and bodygraph-dark.svg (dark) from humandesign.json."""
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
        'channels': {'Channels': hd_data.get('channels', [])}
    }

    # Generate light mode bodygraph
    svg_bytes_light = generate_bodygraph_image(
        chart_data,
        fmt='svg',
        include_panels=True,
        include_summary=False,
        dark_mode=False
    )

    # Write light mode to file
    output_file_light = output_dir / 'bodygraph.svg'
    with open(output_file_light, 'wb') as f:
        f.write(svg_bytes_light)

    print(f"✓ Bodygraph (light): {output_file_light.relative_to(Path.cwd()) if output_file_light.is_relative_to(Path.cwd()) else output_file_light}")

    # Generate dark mode bodygraph
    svg_bytes_dark = generate_bodygraph_image(
        chart_data,
        fmt='svg',
        include_panels=True,
        include_summary=False,
        dark_mode=True
    )

    # Write dark mode to file
    output_file_dark = output_dir / 'bodygraph-dark.svg'
    with open(output_file_dark, 'wb') as f:
        f.write(svg_bytes_dark)

    print(f"✓ Bodygraph (dark): {output_file_dark.relative_to(Path.cwd()) if output_file_dark.is_relative_to(Path.cwd()) else output_file_dark}")

    return True


def generate_natal_chart(output_dir: Path) -> bool:
    """Generate landscape + portrait natal charts from astrology.json."""
    astro_file = output_dir / 'astrology.json'

    if not astro_file.exists():
        print(f"Error: {astro_file} not found", file=sys.stderr)
        return False

    # Load astrology data
    with open(astro_file, 'r') as f:
        astro_data = json.load(f)

    meta = astro_data['meta']

    # Step 1: Generate landscape chart using Cartographer
    svg_bytes, _ = render_natal_chart(
        name=meta['name'],
        year=int(meta['birth_date'].split('-')[0]),
        month=int(meta['birth_date'].split('-')[1]),
        day=int(meta['birth_date'].split('-')[2]),
        hour=int(meta['birth_time'].split(':')[0]),
        minute=int(meta['birth_time'].split(':')[1]),
        lat=meta['coordinates']['lat'],
        lng=meta['coordinates']['lng'],
        tz_str=meta['timezone'],
        output_format='svg',
        city=meta.get('city')
    )

    # Save landscape chart
    landscape_file = output_dir / 'landscape.svg'
    with open(landscape_file, 'wb') as f:
        f.write(svg_bytes)
    print(f"✓ Landscape chart: {landscape_file.relative_to(Path.cwd()) if landscape_file.is_relative_to(Path.cwd()) else landscape_file}")

    # Step 2: Generate portrait charts (dark + light) using portrait_builder.py
    import subprocess
    portrait_builder = SCRIPT_DIR.parent / 'Cartographer' / 'portrait_builder.py'

    if not portrait_builder.exists():
        print(f"Warning: portrait_builder.py not found at {portrait_builder}", file=sys.stderr)
        return True  # Landscape still generated successfully

    try:
        # Get python from Cartographer venv
        venv_python = SCRIPT_DIR.parent / 'Cartographer' / '.venv' / 'bin' / 'python3'

        # Run: python3 portrait_builder.py landscape.svg portrait
        # This creates portrait-light.svg and portrait-dark.svg
        result = subprocess.run(
            [str(venv_python), str(portrait_builder), str(landscape_file), str(output_dir / 'portrait')],
            capture_output=True,
            text=True,
            cwd=output_dir
        )

        if result.returncode == 0:
            print(f"✓ Portrait charts: portrait-light.svg, portrait-dark.svg")
        else:
            print(f"Warning: Portrait generation failed: {result.stderr}", file=sys.stderr)

    except Exception as e:
        print(f"Warning: Portrait generation error: {e}", file=sys.stderr)

    return True


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
