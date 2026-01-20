#!/bin/bash
# VibologyOS Chart Calculation Wrapper
# Automatically activates virtual environment and runs chart calculation scripts

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)/.venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Error: Virtual environment not found at $VENV_DIR"
    echo "Run: python3 -m venv $VENV_DIR && source $VENV_DIR/bin/activate && pip install -r $SCRIPT_DIR/requirements.txt"
    exit 1
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Determine which script to run based on first argument
case "$1" in
    astrology|astro)
        shift
        python3 "$SCRIPT_DIR/get_astro_data.py" "$@"
        ;;
    humandesign|hd)
        shift
        python3 "$SCRIPT_DIR/get_hd_data.py" "$@"
        ;;
    verify-location|verify)
        shift
        python3 "$SCRIPT_DIR/verify_geolocation.py" "$@"
        ;;
    *)
        echo "VibologyOS Chart Calculation Wrapper"
        echo ""
        echo "Usage:"
        echo "  $0 astrology [OPTIONS]     Calculate astrology chart"
        echo "  $0 humandesign [OPTIONS]   Calculate Human Design chart"
        echo "  $0 verify-location [ARGS]  Verify geolocation (optional)"
        echo ""
        echo "Examples:"
        echo "  $0 astrology --name 'Jane Doe' --year 1990 --month 5 --day 15 --hour 14 --minute 30 --lat 40.7128 --lng -74.0060 --timezone 'America/New_York' --pretty"
        echo "  $0 humandesign --name 'Jane Doe' --year 1990 --month 5 --day 15 --hour 14 --minute 30 --lat 40.7128 --lng -74.0060 --pretty"
        echo ""
        echo "For full options, run:"
        echo "  $0 astrology --help"
        echo "  $0 humandesign --help"
        exit 1
        ;;
esac
