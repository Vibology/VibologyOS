#!/usr/bin/env python3
"""
Global Section Rename Script for Semantic Section System
Renames H2 headers to match approved section names.

Usage:
    python global_section_rename.py --dry-run  # Preview changes
    python global_section_rename.py            # Apply changes
"""

import os
import re
import argparse
from pathlib import Path

LIBRARY_ROOT = Path("/home/joe/VibologyOS/Library")

# Define exact H2 renames (old -> new)
RENAMES = {
    "## References": "## Sources",
    "## Reference": "## Sources",
    "## Internal Links": "## Cross-References",
}

def find_library_files():
    """Find all markdown files in the Library."""
    files = []
    for root, dirs, filenames in os.walk(LIBRARY_ROOT):
        # Skip archive directories
        if '.archive' in root:
            continue
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(Path(root) / filename)
    return sorted(files)

def process_file(filepath, dry_run=True):
    """Process a single file, applying renames."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    for old, new in RENAMES.items():
        # Match the exact H2 header on its own line
        # Pattern: start of line, the header, optional whitespace, end of line
        pattern = re.compile(r'^' + re.escape(old) + r'\s*$', re.MULTILINE)

        if pattern.search(content):
            content = pattern.sub(new, content)
            changes.append(f"  {old} → {new}")

    if changes and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Rename H2 sections globally')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    files = find_library_files()
    print(f"Found {len(files)} markdown files in Library\n")

    if args.dry_run:
        print("=== DRY RUN MODE (no changes will be written) ===\n")

    total_files_changed = 0
    changes_by_type = {old: 0 for old in RENAMES.keys()}

    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_files_changed += 1
            rel_path = filepath.relative_to(LIBRARY_ROOT)
            print(f"{rel_path}")
            for change in changes:
                print(change)
                # Count by type
                for old in RENAMES.keys():
                    if old in change:
                        changes_by_type[old] += 1
            print()

    print("=" * 50)
    print(f"SUMMARY")
    print("=" * 50)
    print(f"Total files scanned: {len(files)}")
    print(f"Files with changes: {total_files_changed}")
    print()
    print("Changes by type:")
    for old, count in changes_by_type.items():
        new = RENAMES[old]
        print(f"  {old} → {new}: {count} files")

    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply.")
    else:
        print(f"\n[COMPLETE] {total_files_changed} files updated.")

if __name__ == "__main__":
    main()
