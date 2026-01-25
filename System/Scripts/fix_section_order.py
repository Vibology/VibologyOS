#!/usr/bin/env python3
"""
Fix section order: Cross-References should come BEFORE Sources.

The Semantic Section System specifies:
OPENING → DATA → DEPTH → SHADOW → PRACTICE → LINKS → SOURCES

This script swaps ## Sources and ## Cross-References when Sources comes first.

Usage:
    python fix_section_order.py --dry-run  # Preview
    python fix_section_order.py            # Apply
"""

import re
import argparse
from pathlib import Path

LIBRARY_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding")

def process_file(filepath, dry_run=True):
    """Process a single file to fix section order."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern to match Sources section followed by Cross-References section
    # Sources section: starts with ## Sources, ends before ## Cross-References
    # Cross-References section: starts with ## Cross-References, ends at EOF or next ## (but there shouldn't be one)

    # Find if Sources comes before Cross-References (incorrect order)
    sources_match = re.search(r'^## Sources\s*$', content, re.MULTILINE)
    crossref_match = re.search(r'^## Cross-References\s*$', content, re.MULTILINE)

    if not sources_match or not crossref_match:
        return None  # One or both sections missing

    if sources_match.start() > crossref_match.start():
        return None  # Already in correct order (Cross-References before Sources)

    # Sources comes before Cross-References - need to swap
    # Extract both sections with their content

    # Find the end of Sources section (start of Cross-References)
    sources_start = sources_match.start()
    sources_end = crossref_match.start()
    sources_section = content[sources_start:sources_end].rstrip('\n')

    # Find the end of Cross-References section (EOF or could have trailing content)
    crossref_start = crossref_match.start()
    # Cross-References goes to end of file (it should be last, but Sources was after it incorrectly)
    crossref_section = content[crossref_start:].rstrip('\n')

    # Check if there's content after Cross-References that looks like it belongs after
    # For now, assume Cross-References goes to end

    # Rebuild content: everything before Sources + Cross-References + Sources
    before_sources = content[:sources_start].rstrip('\n')

    # New content: before + crossref + sources + any trailing content
    new_content = before_sources + '\n\n' + crossref_section + '\n\n' + sources_section + '\n'

    if new_content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        return "  Swapped: ## Cross-References now before ## Sources"

    return None

def main():
    parser = argparse.ArgumentParser(description='Fix section order (Cross-References before Sources)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(LIBRARY_PATH.rglob('*.md'))
    print(f"Found {len(files)} Library files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    by_pillar = {}

    for filepath in files:
        result = process_file(filepath, dry_run=args.dry_run)
        if result:
            total_changed += 1
            # Get pillar name
            rel_path = filepath.relative_to(LIBRARY_PATH)
            pillar = rel_path.parts[0] if rel_path.parts else "Unknown"
            by_pillar[pillar] = by_pillar.get(pillar, 0) + 1

            if total_changed <= 20:  # Only show first 20 files
                print(f"{rel_path}")
                print(result)
                print()

    if total_changed > 20:
        print(f"... and {total_changed - 20} more files\n")

    print("=" * 50)
    print(f"Files {'to be ' if args.dry_run else ''}modified: {total_changed}")
    print("\nBy pillar:")
    for pillar, count in sorted(by_pillar.items()):
        print(f"  {pillar}: {count}")

    if args.dry_run:
        print("\n[DRY RUN] No files modified. Run without --dry-run to apply.")
    else:
        print(f"\n[COMPLETE] {total_changed} files updated.")

if __name__ == "__main__":
    main()
