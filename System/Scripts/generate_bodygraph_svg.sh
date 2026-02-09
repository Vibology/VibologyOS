#!/bin/bash
#
# Generate bodygraph.svg from humandesign.json (protocol-compliant wrapper)
#
# This script enforces protocol standards:
# - Input must be named: humandesign.json
# - Output will be named: bodygraph.svg
# - Format is always: SVG (scalable, archival quality)
# - Location: Same directory as input JSON
#
# Usage:
#   generate_bodygraph_svg.sh [directory]
#   generate_bodygraph_svg.sh              # Uses current directory
#   generate_bodygraph_svg.sh ~/Personal/Biography/
#   generate_bodygraph_svg.sh ~/Business/Consultations/ClientName/
#

set -e  # Exit on error

# Get directory argument (default to current directory)
TARGET_DIR="${1:-.}"

# Check that directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
    echo "❌ Error: Directory does not exist: $TARGET_DIR" >&2
    exit 1
fi

# Resolve to absolute path
TARGET_DIR=$(cd "$TARGET_DIR" && pwd)

# Check that humandesign.json exists
if [[ ! -f "$TARGET_DIR/humandesign.json" ]]; then
    echo "❌ Error: humandesign.json not found in $TARGET_DIR" >&2
    echo "" >&2
    echo "Protocol requires input file named: humandesign.json" >&2
    echo "Generate it with: get_hd_data.py [args] > humandesign.json" >&2
    exit 1
fi

# Get the VibologyOS root (two levels up from this script)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIBOLOGY_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Generate bodygraph using Cartographer's chart_renderer
echo "Generating bodygraph.svg from humandesign.json..."
cd "$VIBOLOGY_ROOT"

python3 << EOF
import json
import sys
from pathlib import Path

# Add Cartographer to path
sys.path.insert(0, '$VIBOLOGY_ROOT/System/Cartographer/src')

from cartographer.services.chart_renderer import generate_bodygraph_image

# Load humandesign.json
hd_file = Path('$TARGET_DIR') / 'humandesign.json'
with open(hd_file) as f:
    hd_data = json.load(f)

# Transform to chart_renderer format (protocol standard)
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

# Generate bodygraph as SVG (protocol format)
svg_bytes = generate_bodygraph_image(
    chart_data,
    fmt='svg',
    include_panels=True,
    include_summary=False
)

# Save as bodygraph.svg in same directory (protocol location)
output = hd_file.parent / 'bodygraph.svg'
with open(output, 'wb') as f:
    f.write(svg_bytes)
EOF

echo ""
echo "✓ Protocol compliance verified:"
echo "  Input:  $TARGET_DIR/humandesign.json"
echo "  Output: $TARGET_DIR/bodygraph.svg"
