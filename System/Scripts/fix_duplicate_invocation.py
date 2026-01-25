#!/usr/bin/env python3
"""
Fix duplicate ## Invocation sections in Angelology files.

Renames the SECOND occurrence of ## Invocation to ## Contemplative Practice
(an approved alternate per the Angelology Manifest).

Usage:
    python fix_duplicate_invocation.py --dry-run  # Preview
    python fix_duplicate_invocation.py            # Apply
"""

import re
import argparse
from pathlib import Path

ANGELOLOGY_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Angelology")

FILES_WITH_DUPLICATES = [
    "The Archangels/Raphael.md",
    "The Nine Angelic Orders/Angels.md",
    "The Nine Angelic Orders/Cherubim.md",
    "The Nine Angelic Orders/Principalities.md",
    "The Nine Angelic Orders/Seraphim.md",
    "The Nine Angelic Orders/Virtues.md",
]

def fix_duplicate_invocation(filepath, dry_run=True):
    """Fix duplicate ## Invocation by renaming second occurrence."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count occurrences
    matches = list(re.finditer(r'^## Invocation\s*$', content, re.MULTILINE))

    if len(matches) < 2:
        return None  # No duplicate to fix

    # Replace only the second occurrence
    # We'll use the position of the second match
    second_match = matches[1]

    new_content = (
        content[:second_match.start()] +
        "## Contemplative Practice" +
        content[second_match.end():]
    )

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return f"  Second ## Invocation -> ## Contemplative Practice (line {content[:second_match.start()].count(chr(10)) + 1})"

def main():
    parser = argparse.ArgumentParser(description='Fix duplicate Invocation sections')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    fixed = 0
    for rel_path in FILES_WITH_DUPLICATES:
        filepath = ANGELOLOGY_PATH / rel_path
        if filepath.exists():
            result = fix_duplicate_invocation(filepath, dry_run=args.dry_run)
            if result:
                fixed += 1
                print(f"{rel_path}")
                print(result)
                print()

    print("=" * 50)
    print(f"Files {'to be ' if args.dry_run else ''}fixed: {fixed}")
    if args.dry_run:
        print("\n[DRY RUN] No files modified. Run without --dry-run to apply.")
    else:
        print(f"\n[COMPLETE] {fixed} files fixed.")

if __name__ == "__main__":
    main()
